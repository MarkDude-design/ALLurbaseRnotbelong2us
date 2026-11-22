"""Resume ONLY previously unsent core pairs; full published context output reservation."""
import concurrent.futures as cf
import contextlib,io,json,time
from decimal import Decimal
from pathlib import Path
import paid_runner as p
b=p.b;b.OUT=Path('sealed-glitch-continuation-results')
state=json.loads((b.BASE/'continuation-state.json').read_text())
PRIOR=Decimal(state['previous_reserved_usd'])

def safe_wc(m):
 prices=p.price(m)
 context=m.get('context_length')
 top=(m.get('top_provider') or {}).get('max_completion_tokens')
 if not prices or not isinstance(context,int) or context<=0:return None
 # Reserve the full model context as output; also cover any larger published output limit.
 limit=max(context,top if isinstance(top,int) and top>0 else 0)
 return p.INPUT_RESERVE*prices[0]+limit*prices[1]

class Recorder(p.Recorder):
 def save(self):
  with contextlib.redirect_stdout(io.StringIO()):super().save()
  s=json.loads((b.OUT/'summary.json').read_text());s['prior_paid_reservations_including_excess_usd']=str(PRIOR)
  s['combined_max_reserved_usd']=str(PRIOR+Decimal(s['reserved_max_total_usd']))
  s['note']='Only previously UNSENT core pairs. Full published context/output limit reserved; original 450-token request unchanged. No retries or fallback.'
  (b.OUT/'summary.json').write_text(json.dumps(s,indent=2));print(json.dumps(s),flush=True)

def main():
 r=Recorder();r.add({'type':'start','lane':'C','prior_run':state['prior_run'],'arms':b.ARMS,'prior_reserved_usd':str(PRIOR),
  'reason':'First paid run stopped on billed reasoning beyond max_tokens. Preserve prior results; safely continue unsent pairs only.',
  'reservation_rule':'4096 input plus FULL published context length as output, or larger advertised output limit; no released reservations; prior excess added',
  'sampling':'budget trim to G1/G4/CONTROL; all unattempted expansion arms remain unsent',
  'unchanged':'original GO/deadline; prompt; 450 requested tokens; no retries/fallback; four workers'})
 if time.time()>=b.DEADLINE:r.add({'type':'abort','reason':'deadline passed'});return
 try:
  credits=b.get_json('credits',True);key=b.get_json('auth/key',True);d=credits['data']
  avail=Decimal(str(d['total_credits']))-Decimal(str(d['total_usage']))
  if key['data'].get('limit_remaining') is not None:avail=min(avail,Decimal(str(key['data']['limit_remaining'])))
  budget=min(Decimal('3')-PRIOR,avail)
  r.add({'type':'balance_receipt','utc':b.now(),'credits':credits,'key':key,'run_budget_usd':str(budget),'prior_reserved_usd':str(PRIOR)})
  cat=b.get_json('models');entries={m['id']:m for m in cat['data']}
 except Exception as e:r.add({'type':'abort','reason':'fresh balance/catalog failed','error_type':type(e).__name__});return
 if budget<=0:r.add({'type':'abort','reason':'no reserved budget remains'});return
 previous={(e['model'],e['arm']) for e in state['previous_attempted_pairs']}
 plan=[e for e in state['remaining_plan'] if e['wave']<3]
 assert not previous & {(e['model'],e['arm']) for e in plan}
 r.add({'type':'plan','pairs':plan,'previous_attempted_pairs':state['previous_attempted_pairs'],
        'catalog':[{'id':m['id'],'canonical_slug':m.get('canonical_slug'),'pricing':m.get('pricing'),'context_length':m.get('context_length'),'top_provider':m.get('top_provider')} for m in cat['data']]})
 reserved=Decimal('0');futures={};stop=None;attempted=set();skipped=set()
 with cf.ThreadPoolExecutor(max_workers=4) as pool:
  for index,e in enumerate(plan):
   model,arm,wave=e['model'],e['arm'],e['wave']
   while len(futures)>=4:
    completed,_=cf.wait(futures,return_when=cf.FIRST_COMPLETED)
    for f in completed:
     futures.pop(f);rec=f.result();r.add(rec)
     if rec['type']=='result':
      cost=(rec.get('usage') or {}).get('cost')
      if cost is not None and Decimal(str(cost))>Decimal(rec['reserved_usd']):stop='reported cost exceeded full-context reservation'
      if rec.get('http_status') in (401,402):stop='account authentication/credit failure'
   if stop or time.time()>=b.DEADLINE:stop=stop or 'deadline';break
   possible=[safe_wc(entries[x['model']]) for x in plan[index:] if x['model'] in entries]
   positive=[x for x in possible if x is not None]
   if positive and min(positive)>budget-reserved:stop='remaining permanent reservations exhausted';break
   try:
    live={m['id']:m for m in b.get_json('models')['data']};entry=live.get(model);amount=None if entry is None else safe_wc(entry)
   except Exception as exc:
    r.add({'type':'unsent','model':model,'arm':arm,'reason':'live catalog unavailable','error_type':type(exc).__name__});skipped.add((model,arm));continue
   if amount is None or reserved+amount>budget:
    r.add({'type':'unsent','model':model,'arm':arm,'reason':'unknown full output bound or insufficient permanent reservation'});skipped.add((model,arm));continue
   if time.time()>=b.DEADLINE:stop='deadline';break
   reserved+=amount;r.add({'type':'reservation','model':model,'arm':arm,'reserved_usd':str(amount),'reserved_total_usd':str(reserved),'combined_reserved_usd':str(PRIOR+reserved),'utc':b.now()})
   attempted.add((model,arm));futures[pool.submit(p.call,model,arm,wave,amount,r,entry)]=(model,arm)
  for f in cf.as_completed(futures):r.add(f.result())
 for e in state['remaining_plan']:
  if (e['model'],e['arm']) not in attempted|skipped:r.add({'type':'unsent','model':e['model'],'arm':e['arm'],'wave':e['wave'],'reason':'budget trim expansion' if e['wave']>=3 else stop or 'not attempted'})
 try:r.add({'type':'balance_after','utc':b.now(),'credits':b.get_json('credits',True),'key':b.get_json('auth/key',True)})
 except Exception as e:r.add({'type':'balance_after_unavailable','error_type':type(e).__name__})
 r.add({'type':'finished','reason':stop or 'all affordable unsent core pairs processed','utc':b.now()})
if __name__=='__main__':main()
