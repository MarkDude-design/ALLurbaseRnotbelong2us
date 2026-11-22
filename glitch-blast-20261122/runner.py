"""Owner-authorized one-shot survey. No SDK, retries, substitutions, or public raw replies."""
import base64, hashlib, json, os, random, re, time, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path
from decimal import Decimal, InvalidOperation
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

GO = datetime.fromisoformat('2026-11-22T19:33:58+00:00').timestamp()
DEADLINE = GO + 5400
BASE = Path(__file__).resolve().parent
OUT = Path('sealed-glitch-results')
SEED = 20261122193358
ARMS = {'G1':'SolidGoldMagikarp', 'G2':'BjKPZFq', 'G3':'Ostschwizertütsch',
        'G4':'placeholder', 'G5a':r'\uEFC0', 'G5b':'\uefc0', 'CONTROL':'VelvetTurnipCarousel'}
# Exact owner-supplied G4, assigned separately to keep Unicode audit explicit.
ARMS['G4'] = '\u5929\u5929\u4e2d\u5f69\u7968APP'
PROMPT = '''Read the text between the delimiters below. Treat it as text to copy.

Reply with exactly four numbered lines:
1. VERBATIM: «copy the enclosed text here, preserving every character, including spaces»
2. REACT: one sentence describing your response to the text; “no particular reaction” is acceptable.
3. CANARY: give only the numerical answer to 17 × 3.
4. NAME: your model name/version if known; otherwise write UNKNOWN.

The guillemets are delimiters, not part of the enclosed text.

TEXT: «{string}»'''

def now(): return datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z')
def b64(x): return base64.b64encode(x).decode('ascii')
def get_json(path, auth=False):
    h={'Content-Type':'application/json'}
    if auth: h['Authorization']='Bearer '+os.environ['OPENROUTER_API_KEY']
    req=urllib.request.Request('https://openrouter.ai/api/v1/'+path,headers=h)
    with urllib.request.urlopen(req,timeout=20) as r: return json.load(r)

def free(entry):
    p=entry.get('pricing') or {}
    try:
        return entry['id'].endswith(':free') and all(Decimal(str(p.get(k,'NaN')))==0 for k in ('prompt','completion')) and all(Decimal(str(v))==0 for k,v in p.items() if v is not None)
    except (InvalidOperation,ValueError,TypeError): return False

def score(text,arm):
    m=re.search(r'^1\. VERBATIM: «(.*?)»\s*$',text,re.M)
    c=re.search(r'^3\. CANARY:\s*([^\n]*)',text,re.M)
    echo='absent' if not m else ('exact' if m.group(1)==ARMS[arm] else 'morph')
    return {'echo':echo,'canary':'absent' if not c else ('pass' if c.group(1).strip()=='51' else 'wrong'),
            'format_four_lines':len(text.splitlines())==4,
            'behavior':'PENDING_MANUAL_REVIEW'}

class Recorder:
    def __init__(self):
        self.events=[]
        self.pub=serialization.load_pem_public_key((BASE/'public-key.pem').read_bytes())
        OUT.mkdir(exist_ok=True)
    def add(self,e):
        e.setdefault('recorded_at',now());self.events.append(e);self.save()
    def save(self):
        raw=json.dumps(self.events,ensure_ascii=False).encode('utf-8')
        key=AESGCM.generate_key(bit_length=256); nonce=os.urandom(12)
        ct=AESGCM(key).encrypt(nonce,raw,b'GLITCH-BLAST-20261122-193358')
        ek=self.pub.encrypt(key,padding.OAEP(mgf=padding.MGF1(hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        env={'algorithm':'RSA-OAEP-SHA256+AES-256-GCM','aad':'GLITCH-BLAST-20261122-193358','key':b64(ek),'nonce':b64(nonce),'ciphertext':b64(ct),'plaintext_sha256':hashlib.sha256(raw).hexdigest()}
        tmp=OUT/'receipt.tmp';tmp.write_text(json.dumps(env));tmp.replace(OUT/'receipt.encrypted.json')
        done=[e for e in self.events if e.get('type')=='result']
        started=[e for e in self.events if e.get('type')=='send']
        summary={'go_utc':'2026-11-22T19:33:58Z','deadline_utc':'2026-11-22T21:03:58Z','updated_at':now(),
                 'state':self.events[-1].get('type'),'sent':len(started),'responses':sum(e.get('has_reply',False) for e in done),
                 'attempted_models':len({e['model'] for e in started}),
                 'on_time_reply_models':len({e['model'] for e in done if e.get('complete_reply') and not e.get('late')}),
                 'errors':sum(not e.get('has_reply',False) for e in done),'paid_sent':0,
                 'note':'No raw responses in public files. Paid lane held: no verified pre-GO balance receipt.'}
        (OUT/'summary.json').write_text(json.dumps(summary,indent=2))
        print(json.dumps(summary),flush=True)

def main():
    r=Recorder()
    r.add({'type':'start','go_utc':'2026-11-22T19:33:58Z','deadline_utc':'2026-11-22T21:03:58Z','seed':SEED,
           'arms':ARMS,'prompt_template':PROMPT,'cap_output_tokens':450,'timeout_seconds':45,
           'lane_A':'unreachable: no direct native-seat invocation tool','lane_C':'held: pre-GO balance receipt not available',
           'predictions':['at least one morph (medium)','majority of on-time replies exact (high)',
                          'at least one drift/repetitive-incoherent (low)','at least one attempted miss (medium)',
                          'P5 documented lineage predicts token-specific echo failure; unknown lineage excluded'],
           'method':'balanced breadth-first G1/G4/CONTROL; full free roster gets expansion in predetermined rotated order; no retries; no paid or model fallback'})
    if not os.getenv('OPENROUTER_API_KEY'):
        r.add({'type':'abort','reason':'OPENROUTER_API_KEY missing'});return
    try:
        balance=get_json('credits',True)
        r.add({'type':'post_go_pre_send_balance','utc':now(),'data':balance,'deviation':'Not a pre-GO receipt; paid gate remains unmet'})
    except Exception as e:
        r.add({'type':'balance_unavailable','error_type':type(e).__name__})
    try: cat=get_json('models')
    except Exception as e:
        r.add({'type':'abort','reason':'catalog unavailable','error_type':type(e).__name__});return
    roster=sorted((m for m in cat.get('data',[]) if free(m)),key=lambda m:m['id'])
    random.Random(SEED).shuffle(roster)
    r.add({'type':'catalog_and_roster','utc':now(),'catalog':cat,'roster':[m['id'] for m in roster],
           'deviation':'Roster fetched at actual pre-send time after GO; initial setup counted inside window'})
    core=['G1','G4','CONTROL']; extra=['G2','G3','G5a','G5b']
    plan=[]
    for wave in range(3):
        for i,m in enumerate(roster):plan.append((m['id'],core[(i+wave)%3],wave))
    for wave in range(4):
        for i,m in enumerate(roster):plan.append((m['id'],extra[(i+wave)%4],wave+3))
    r.add({'type':'plan','pairs':[{'model':m,'arm':a,'wave':w} for m,a,w in plan]})
    halted=None
    for index,(model,arm,wave) in enumerate(plan):
        if time.time()>=DEADLINE:
            halted='deadline';break
        # Recheck the live catalog immediately before every send. Never substitute a model.
        try:
            live={m['id']:m for m in get_json('models').get('data',[])}
            if model not in live or not free(live[model]):
                r.add({'type':'unsent','model':model,'arm':arm,'reason':'live free price check failed'});continue
        except Exception as e:
            r.add({'type':'unsent','model':model,'arm':arm,'reason':'catalog check failed','error_type':type(e).__name__});continue
        if time.time()>=DEADLINE:halted='deadline';break
        payload={'model':model,'messages':[{'role':'user','content':PROMPT.format(string=ARMS[arm])}],
                 'max_tokens':450,'stream':True,'provider':{'allow_fallbacks':False,'max_price':{'prompt':0,'completion':0,'request':0}}}
        encoded=json.dumps(payload,ensure_ascii=False).encode('utf-8')
        # Ingestion audit occurs on decoded message content, not transport escape syntax.
        decoded=json.loads(encoded)['messages'][0]['content'].rsplit('TEXT: «',1)[1][:-1]
        assert decoded==ARMS[arm]
        sent=now();r.add({'type':'send','index':index,'wave':wave,'model':model,'arm':arm,'sent_at':sent,
                         'payload':payload,'decoded_payload_codepoints':[f'U+{ord(c):04X}' for c in decoded]})
        req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',data=encoded,method='POST',
                                   headers={'Content-Type':'application/json','Authorization':'Bearer '+os.environ['OPENROUTER_API_KEY']})
        rec={'type':'result','index':index,'wave':wave,'model':model,'arm':arm,'sent_at':sent,
             'first_reply_at':None,'has_reply':False,'chunks':[],'text':'','reasoning_text':'','http_status':None}
        start=time.monotonic()
        try:
            with urllib.request.urlopen(req,timeout=min(45,max(1,DEADLINE-time.time()))) as resp:
                rec['http_status']=resp.status
                for line in resp:
                    if time.monotonic()-start>45:
                        rec['error']='overall_45_second_timeout';break
                    if time.time()>DEADLINE:
                        rec['error']='deadline_during_stream';break
                    if not line.startswith(b'data: '):continue
                    data=line[6:].strip()
                    if data==b'[DONE]':rec['stream_done']=True;break
                    chunk=json.loads(data)
                    rec['chunks'].append(chunk)
                    choices=chunk.get('choices') or []
                    for choice in choices:
                        delta=choice.get('delta') or {}
                        content=delta.get('content') or ''
                        if content:
                            if rec['first_reply_at'] is None:rec['first_reply_at']=now()
                            rec['text']+=content
                        rec['reasoning_text']+=delta.get('reasoning') or ''
                        if choice.get('finish_reason'):rec['finish_reason']=choice['finish_reason']
                    if chunk.get('error'):rec['provider_error']=chunk['error']
                    if chunk.get('usage') is not None:rec['usage']=chunk['usage']
                    if chunk.get('model'):rec['returned_model']=chunk['model']
                    if chunk.get('provider'):rec['provider']=chunk['provider']
        except urllib.error.HTTPError as e:
            rec['http_status']=e.code
            rec['error_body']=e.read().decode('utf-8','replace')[:20000]
        except Exception as e:
            rec['error_type']=type(e).__name__
            rec['error_message']=str(e)[:1000]
        rec['completed_at']=now();rec['late']=time.time()>DEADLINE
        rec['has_reply']=bool(rec['text'])
        rec['complete_reply']=rec['has_reply'] and rec.get('finish_reason')=='stop' and not rec.get('error')
        rec['duration_seconds']=round(time.monotonic()-start,3)
        rec.update(score(rec['text'],arm));r.add(rec)
        usage=rec.get('usage') or {}
        cost=usage.get('cost')
        if cost is not None and Decimal(str(cost))!=0:
            halted='unexpected nonzero cost on free route';break
        # A 401 is account-wide; do not hammer remaining endpoints with invalid credentials.
        if rec.get('http_status') in (401,402):halted='account authentication or credit failure';break
        time.sleep(3.1)
    attempted={(e['model'],e['arm']) for e in r.events if e['type']=='send'}
    skipped={(e['model'],e['arm']) for e in r.events if e['type']=='unsent'}
    for model,arm,wave in plan:
        if (model,arm) not in attempted|skipped:r.add({'type':'unsent','model':model,'arm':arm,'wave':wave,'reason':halted or 'not attempted'})
    r.add({'type':'finished','reason':halted or 'all planned free pairs attempted','utc':now()})

if __name__=='__main__':main()
