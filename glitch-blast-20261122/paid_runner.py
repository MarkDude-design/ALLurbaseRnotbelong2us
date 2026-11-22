"""Paid continuation: Mark amended balance timing in-thread; same deadline/cap."""
import concurrent.futures as cf
import contextlib, io, json, os, random, threading, time, urllib.request, urllib.error
from decimal import Decimal, InvalidOperation
from pathlib import Path
import runner as b

b.OUT=Path('sealed-glitch-paid-results')
CAP=Decimal('3.00'); WORKERS=4; INPUT_RESERVE=4096
lock=threading.RLock()

def price(m):
 p=m.get('pricing') or {}
 try:
  a,c=Decimal(str(p['prompt'])),Decimal(str(p['completion']))
  if not a.is_finite() or not c.is_finite() or a<0 or c<0:return None
  for k,v in p.items():
   if k not in ('prompt','completion','input_cache_read','input_cache_write') and v is not None and Decimal(str(v))!=0:return None
  return a,c
 except (KeyError,TypeError,ValueError,InvalidOperation):return None

def wc(m):
 p=price(m)
 return None if p is None else INPUT_RESERVE*p[0]+450*p[1]

class Recorder(b.Recorder):
 def add(self,e):
  with lock:super().add(e)
 def save(self):
  with contextlib.redirect_stdout(io.StringIO()):super().save()
  done=[e for e in self.events if e.get('type')=='result'];starts=[e for e in self.events if e.get('type')=='send']
  s={'go_utc':'2026-11-22T19:33:58Z','deadline_utc':'2026-11-22T21:03:58Z','updated_at':b.now(),
   'state':self.events[-1]['type'],'sent':len(starts),'attempted_models':len({e['model'] for e in starts}),
   'on_time_complete_reply_models':len({e['model'] for e in done if e.get('complete_reply') and not e.get('late')}),
   'visible_reply_count':sum(e.get('has_reply',False) for e in done),
   'reserved_max_total_usd':str(sum(Decimal(e['reserved_usd']) for e in self.events if e['type']=='reservation')),
   'reported_actual_subtotal_usd':str(sum(Decimal(str(e['usage']['cost'])) for e in done if (e.get('usage') or {}).get('cost') is not None)),
   'missing_cost_receipts':sum((e.get('usage') or {}).get('cost') is None for e in done),
   'note':'All raw replies encrypted. Unknown charges retain their full reservation. No retries or fallback.'}
  (b.OUT/'summary.json').write_text(json.dumps(s,indent=2));print(json.dumps(s),flush=True)

def call(model,arm,wave,reserve,r,entry):
 text=b.PROMPT.format(string=b.ARMS[arm]);pp,pc=price(entry)
 payload={'model':model,'messages':[{'role':'user','content':text}],'max_tokens':450,'stream':True,
          'provider':{'allow_fallbacks':False,'max_price':{'prompt':float(pp*1000000),'completion':float(pc*1000000),'request':0}}}
 enc=json.dumps(payload,ensure_ascii=False).encode('utf-8')
 assert len(enc)<INPUT_RESERVE
 decoded=json.loads(enc)['messages'][0]['content'].rsplit('TEXT: «',1)[1][:-1];assert decoded==b.ARMS[arm]
 if time.time()>=b.DEADLINE:return {'type':'unsent','model':model,'arm':arm,'reason':'deadline before worker send'}
 sent=b.now();r.add({'type':'send','model':model,'arm':arm,'wave':wave,'sent_at':sent,'reserved_usd':str(reserve),'payload':payload,
                    'decoded_payload_codepoints':[f'U+{ord(c):04X}' for c in decoded]})
 rec={'type':'result','model':model,'arm':arm,'wave':wave,'sent_at':sent,'first_reply_at':None,'http_status':None,
      'text':'','reasoning_text':'','chunks':[],'reserved_usd':str(reserve)};t=time.monotonic()
 req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',data=enc,method='POST',
          headers={'Content-Type':'application/json','Authorization':'Bearer '+os.environ['OPENROUTER_API_KEY']})
 try:
  with urllib.request.urlopen(req,timeout=min(45,max(1,b.DEADLINE-time.time()))) as resp:
   rec['http_status']=resp.status
   for line in resp:
    if time.monotonic()-t>45:rec['error']='overall_45_second_timeout';break
    if time.time()>b.DEADLINE:rec['error']='deadline_during_stream';break
    if not line.startswith(b'data: '):continue
    data=line[6:].strip()
    if data==b'[DONE]':rec['stream_done']=True;break
    chunk=json.loads(data);rec['chunks'].append(chunk)
    for ch in chunk.get('choices') or []:
     d=ch.get('delta') or {};content=d.get('content') or ''
     if content:
      if rec['first_reply_at'] is None:rec['first_reply_at']=b.now()
      rec['text']+=content
     rec['reasoning_text']+=d.get('reasoning') or ''
     if ch.get('finish_reason'):rec['finish_reason']=ch['finish_reason']
    if chunk.get('error'):rec['provider_error']=chunk['error']
    if chunk.get('usage') is not None:rec['usage']=chunk['usage']
    for k in ('model','provider','id'):
     if chunk.get(k):rec['returned_'+k]=chunk[k]
 except urllib.error.HTTPError as e:
  rec['http_status']=e.code;rec['error_body']=e.read().decode('utf-8','replace')[:20000]
 except Exception as e:rec['error_type']=type(e).__name__;rec['error_message']=str(e)[:1000]
 rec['completed_at']=b.now();rec['late']=time.time()>b.DEADLINE;rec['has_reply']=bool(rec['text'])
 rec['complete_reply']=rec['has_reply'] and rec.get('finish_reason')=='stop' and not rec.get('error')
 rec['duration_seconds']=round(time.monotonic()-t,3);rec.update(b.score(rec['text'],arm));return rec

def main():
 r=Recorder();r.add({'type':'start','lane':'C','owner_amendment':'Mark said Yep to fresh pre-send balance check and paid sends under unchanged $3 cap/deadline.',
 'workers':WORKERS,'input_token_reserve':INPUT_RESERVE,'output_cap':450,'no_retries':True,'no_fallback':True,
 'free_run':'45061953647 finished 2026-11-22T19:46:45Z; 77 attempts; excluded from paid roster',
 'roster_rule':'distinct canonical slugs, text input/output, synchronous endpoint, explicit finite nonnegative token prices, zero other request charges; cheapest variant per slug; full core worst-case fits cap; freeze then seed shuffle',
 'method':'core breadth-first rotated G1/G4/CONTROL then expansion rotated G2/G3/G5a/G5b as budget/time permit',
 'budget_rule':'Sum of permanent reservations for ALL attempted requests, including errors, never exceeds min($3, account credit, key allowance). Actual costs recorded separately; no released reservations.'})
 if time.time()>=b.DEADLINE:r.add({'type':'abort','reason':'deadline passed'});return
 if not os.getenv('OPENROUTER_API_KEY'):r.add({'type':'abort','reason':'key unavailable'});return
 try:
  credits=b.get_json('credits',True);key=b.get_json('auth/key',True)
  d=credits['data'];avail=Decimal(str(d['total_credits']))-Decimal(str(d['total_usage']))
  kd=key['data'];remaining=kd.get('limit_remaining')
  if remaining is not None:avail=min(avail,Decimal(str(remaining)))
  budget=min(CAP,avail)
  r.add({'type':'balance_receipt','utc':b.now(),'credits':credits,'key':key,'available_usd':str(avail),'run_budget_usd':str(budget),'timing':'post-GO, before paid sends; owner amendment accepted'})
  if budget<=0:r.add({'type':'abort','reason':'no balance'});return
  catalog=b.get_json('models')
 except Exception as e:r.add({'type':'abort','reason':'balance or catalog unavailable','error_type':type(e).__name__});return
 free_slugs={m.get('canonical_slug',m['id'].removesuffix(':free')) for m in catalog['data'] if m['id'].endswith(':free')}
 selected={}
 for m in catalog['data']:
  mid=m['id'];slug=m.get('canonical_slug',mid)
  arch=m.get('architecture') or {}
  if slug in free_slugs or ':free' in mid or ':batch' in mid or mid.startswith('openrouter/'):continue
  if 'text' not in arch.get('input_modalities',[]) or 'text' not in arch.get('output_modalities',[]):continue
  w=wc(m)
  if w is None or w<=0:continue
  if slug not in selected or w<wc(selected[slug]):selected[slug]=m
 roster=sorted(selected.values(),key=lambda m:(wc(m),m['id']))
 while roster and sum(wc(m)*3 for m in roster)>budget:roster.pop()
 random.Random(b.SEED+1).shuffle(roster)
 fields=['id','canonical_slug','name','pricing','architecture','supported_parameters','context_length']
 r.add({'type':'catalog_and_roster','utc':b.now(),'seed':b.SEED+1,'roster':[m['id'] for m in roster],
        'catalog':[ {k:m.get(k) for k in fields} for m in catalog['data']],
        'core_worst_case_usd':str(sum(wc(m)*3 for m in roster))})
 core=['G1','G4','CONTROL'];extra=['G2','G3','G5a','G5b'];plan=[]
 for wave in range(3):
  for i,m in enumerate(roster):plan.append((m['id'],core[(i+wave)%3],wave))
 for wave in range(4):
  for i,m in enumerate(roster):plan.append((m['id'],extra[(i+wave)%4],wave+3))
 r.add({'type':'plan','pairs':[{'model':m,'arm':a,'wave':w} for m,a,w in plan]})
 reserved=Decimal('0');futures={};stop=None;attempted=set();skipped=set()
 with cf.ThreadPoolExecutor(max_workers=WORKERS) as pool:
  for model,arm,wave in plan:
   while len(futures)>=WORKERS:
    finished,_=cf.wait(futures,return_when=cf.FIRST_COMPLETED)
    for fut in finished:
     futures.pop(fut);rec=fut.result();r.add(rec)
     if rec['type']=='result':
      cost=(rec.get('usage') or {}).get('cost')
      if cost is not None and Decimal(str(cost))>Decimal(rec['reserved_usd']):stop='reported cost exceeded reservation'
      if rec.get('http_status') in (401,402):stop='account authentication/credit failure'
   if stop or time.time()>=b.DEADLINE:stop=stop or 'deadline';break
   try:
    live={m['id']:m for m in b.get_json('models')['data']};entry=live.get(model);reserve=None if entry is None else wc(entry)
   except Exception as e:
    r.add({'type':'unsent','model':model,'arm':arm,'reason':'live catalog unavailable','error_type':type(e).__name__});skipped.add((model,arm));continue
   if reserve is None or reserved+reserve>budget:
    r.add({'type':'unsent','model':model,'arm':arm,'reason':'price missing or permanent reservation ceiling'});skipped.add((model,arm));continue
   if time.time()>=b.DEADLINE:stop='deadline';break
   reserved+=reserve;r.add({'type':'reservation','model':model,'arm':arm,'reserved_usd':str(reserve),'reserved_total_usd':str(reserved),'utc':b.now()})
   attempted.add((model,arm));futures[pool.submit(call,model,arm,wave,reserve,r,entry)]=(model,arm)
  for fut in cf.as_completed(futures):r.add(fut.result())
 for model,arm,wave in plan:
  if (model,arm) not in attempted|skipped:r.add({'type':'unsent','model':model,'arm':arm,'wave':wave,'reason':stop or 'not sent'})
 try:r.add({'type':'balance_after','utc':b.now(),'credits':b.get_json('credits',True),'key':b.get_json('auth/key',True)})
 except Exception as e:r.add({'type':'balance_after_unavailable','error_type':type(e).__name__})
 r.add({'type':'finished','reason':stop or 'all affordable planned paid pairs attempted','utc':b.now()})

if __name__=='__main__':main()
