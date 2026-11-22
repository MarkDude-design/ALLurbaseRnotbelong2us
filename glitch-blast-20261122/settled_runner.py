"""Final unsent-only core pass: actual settled charges + unresolved + in-flight bounds."""
import concurrent.futures as cf
import contextlib,io,json,time,urllib.parse
from decimal import Decimal
from pathlib import Path
import paid_runner as p
import continuation_runner as c
b=p.b;b.OUT=Path('sealed-glitch-settled-results')
state=json.loads((b.BASE/'settled-state.json').read_text())
class Recorder(p.Recorder):
 def save(self):
  with contextlib.redirect_stdout(io.StringIO()):super().save()
  s=json.loads((b.OUT/'summary.json').read_text())
  ledger=next((e for e in reversed(self.events) if e['type']=='budget_state'),{})
  s['budget_state']=ledger;s['cumulative_reservations_usd']=s.pop('reserved_max_total_usd');s['note']='Final receipt reconciliation releases only settled unused reservations. Unknown and in-flight charges retain full published-output bounds. Original deadline and $3 total cap unchanged.'
  (b.OUT/'summary.json').write_text(json.dumps(s,indent=2));print(json.dumps(s),flush=True)

def main():
 r=Recorder();r.add({'type':'start','lane':'C','arms':b.ARMS,'method':'previously unsent core pairs only; original order/assignments',
 'budget_correction':'Original design was actual charges plus outstanding reservations. Prior implementation permanently held even settled unused reservations. Reconcile final receipts, retain unresolved bounds, and release unused settled capacity; no increase to $3.',
 'output_bound':'4096 input plus full published context/output limit; 450 requested cap remains; no retry/fallback',
 'deadline':'2026-11-22T21:03:58Z'})
 if time.time()>=b.DEADLINE:r.add({'type':'abort','reason':'deadline passed'});return
 spent=Decimal(state['settled_actual_usd']);held=Decimal(state['held_unknown_usd']);active=Decimal('0')
 # Read-only generation receipts can settle earlier timed-out streams. No completion is retried.
 for u in state['unknown']:
  if not u.get('generation_id'):continue
  try:
   receipt=b.get_json('generation?id='+urllib.parse.quote(u['generation_id'],safe=''),True)
   d=receipt.get('data') or {};cost=Decimal(str(d['total_cost']))
   if not cost.is_finite() or cost<0:raise ValueError('invalid final generation cost')
   r.add({'type':'charge_reconciliation','model':u['model'],'arm':u['arm'],'generation_id':u['generation_id'],'receipt':receipt,'cost_usd':str(cost),'released_reservation_usd':u['held_usd'],'utc':b.now()})
   held-=Decimal(u['held_usd']);spent+=cost
  except Exception as e:r.add({'type':'charge_reconciliation_unavailable','model':u['model'],'arm':u['arm'],'error_type':type(e).__name__})
 try:
  credits=b.get_json('credits',True);key=b.get_json('auth/key',True);d=credits['data'];avail=Decimal(str(d['total_credits']))-Decimal(str(d['total_usage']))
  if key['data'].get('limit_remaining') is not None:avail=min(avail,Decimal(str(key['data']['limit_remaining'])))
  ceiling=min(Decimal('3'),spent+held+avail)
  r.add({'type':'balance_receipt','utc':b.now(),'credits':credits,'key':key,'ceiling_usd':str(ceiling)})
 except Exception as e:r.add({'type':'abort','reason':'fresh balance unavailable','error_type':type(e).__name__});return
 def budget():r.add({'type':'budget_state','settled_actual_usd':str(spent),'unresolved_held_usd':str(held),'inflight_reserved_usd':str(active),'total_liability_usd':str(spent+held+active),'ceiling_usd':str(ceiling),'utc':b.now()})
 budget();plan=state['remaining_plan'];previous={(e['model'],e['arm']) for e in state['previous_attempted_pairs']}
 assert not previous & {(e['model'],e['arm']) for e in plan}
 r.add({'type':'plan','pairs':plan,'previous_attempted_pairs':state['previous_attempted_pairs']})
 futures={};stop=None;attempted=set();skipped=set()
 def settle(f):
  nonlocal spent,held,active,stop
  amount=futures.pop(f);rec=f.result();r.add(rec);active-=amount
  cost=(rec.get('usage') or {}).get('cost')
  if rec.get('stream_done') and cost is not None:
   cost=Decimal(str(cost));spent+=cost
   if cost>amount:stop='reported charge exceeded full output reservation'
  elif rec.get('type')=='unsent':pass
  else:held+=amount
  if rec.get('http_status') in (401,402):stop='account authentication/credit failure'
  budget()
 with cf.ThreadPoolExecutor(max_workers=4) as pool:
  for e in plan:
   while len(futures)>=4:
    done,_=cf.wait(futures,return_when=cf.FIRST_COMPLETED)
    for f in done:settle(f)
   if stop or time.time()>=b.DEADLINE:stop=stop or 'deadline';break
   model,arm,wave=e['model'],e['arm'],e['wave']
   try:
    live={m['id']:m for m in b.get_json('models')['data']};entry=live.get(model);amount=None if entry is None else c.safe_wc(entry)
   except Exception as exc:
    r.add({'type':'unsent','model':model,'arm':arm,'reason':'live catalog unavailable','error_type':type(exc).__name__});skipped.add((model,arm));continue
   if entry is not None:r.add({'type':'live_catalog_check','model':model,'arm':arm,'entry':{k:entry.get(k) for k in ['id','canonical_slug','pricing','context_length','top_provider']},'utc':b.now()})
   # Wait for unsettled successful calls to release their unused reservations.
   while amount is not None and spent+held+active+amount>ceiling and futures and not stop and time.time()<b.DEADLINE:
    done,_=cf.wait(futures,return_when=cf.FIRST_COMPLETED)
    for f in done:settle(f)
   if stop or time.time()>=b.DEADLINE:stop=stop or 'deadline';break
   if amount is None or spent+held+active+amount>ceiling:
    r.add({'type':'unsent','model':model,'arm':arm,'reason':'unknown full output bound or insufficient settled budget'});skipped.add((model,arm));continue
   active+=amount;r.add({'type':'reservation','model':model,'arm':arm,'reserved_usd':str(amount),'utc':b.now()});budget()
   attempted.add((model,arm));futures[pool.submit(p.call,model,arm,wave,amount,r,entry)]=amount
  for f in list(cf.as_completed(futures)):settle(f)
 for e in plan:
  if (e['model'],e['arm']) not in attempted|skipped:r.add({'type':'unsent','model':e['model'],'arm':e['arm'],'wave':e['wave'],'reason':stop or 'not attempted'})
 try:r.add({'type':'balance_after','utc':b.now(),'credits':b.get_json('credits',True),'key':b.get_json('auth/key',True)})
 except Exception as e:r.add({'type':'balance_after_unavailable','error_type':type(e).__name__})
 budget();r.add({'type':'finished','reason':stop or 'all affordable remaining core pairs processed','utc':b.now()})
if __name__=='__main__':main()
