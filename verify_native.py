#!/usr/bin/env python3
"""Offline native Calendar checks in an already running, owned card-host.
No provider credentials, fake provider replies, model calls or remote writes.
"""
import argparse,hashlib,json,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
p=argparse.ArgumentParser();p.add_argument('--port',type=int,required=True);p.add_argument('--binary',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--restart-check',action='store_true');a=p.parse_args()
r=Path(__file__).resolve().parent;a.out.mkdir(parents=True,exist_ok=True);endpoint=f'http://127.0.0.1:{a.port}'
def call(route,**q):
 with urlopen(endpoint+'/'+route+('?' + urlencode(q) if q else ''),timeout=10) as result:data=json.load(result)
 if 'err' in data:raise RuntimeError(data['err'])
 return data
def rows():return [w for w in call('snap')['s'] if w.get('ty')!='Splash']
def find(*,text=None,widget=None,seconds=5):
 until=time.monotonic()+seconds
 while time.monotonic()<until:
  found=[w for w in rows() if (text is None or w.get('t')==text) and (widget is None or w.get('i')==widget) and w['r'][2]>0 and w['r'][3]>0]
  if len(found)==1:return found[0]
  if len(found)>1:raise AssertionError('ambiguous native selector')
  time.sleep(.03)
 raise AssertionError((text,widget))
def click(**q):
 w=find(**q);x,y,width,height=w['r'];assert 0<=y<892
 call('click',x=x+width/2,y=y+height/2,wait=0)
def contains(text):
 until=time.monotonic()+5
 while time.monotonic()<until:
  if any(text in w.get('t','') for w in rows()):return
  time.sleep(.03)
 raise AssertionError(text)
def visible(widget):
 for direction in (-1,1):
  for _ in range(7):
   try:
    w=find(widget=widget,seconds=.15)
    if w['r'][3]>=40:return w
   except AssertionError:pass
   call('m',k='scroll',x=330,y=510,dy=280*direction,precise=1,wait=0)
 return find(widget=widget)
def type_text(widget,value):
 visible(widget);click(widget=widget)
 call('k',k='press',c='KeyA',cmd=1,wait=0);call('t',t=value,wait=0)
 until=time.monotonic()+3
 while time.monotonic()<until:
  if find(widget=widget).get('val')==value:return
  time.sleep(.03)
 raise AssertionError('typed value did not reach native input')
def capture(name):
 until=time.monotonic()+8
 while True:
  try:data=call('g');break
  except RuntimeError as e:
   if 'grab frame could not be submitted at arming; retry' not in str(e) or time.monotonic()>until:raise
   time.sleep(.1)
 dest=a.out/(name+'.png');dest.write_bytes(Path(data['png']).read_bytes())
 (a.out/(name+'.snapshot.json')).write_text(json.dumps(rows(),indent=2)+'\n')
checks=[]
contains('Google sign-in unavailable')
if a.restart_check:
 click(text='Resume draft');visible('e_title');assert find(widget='e_title')['val']=='Synthetic planning session'
 assert find(widget='e_date')['val']=='2026-10-15';assert find(widget='e_end_date')['val']=='2026-10-15'
 assert find(widget='e_time')['val']=='10:30';assert find(widget='e_end_time')['val']=='11:00'
 visible('e_zone');assert find(widget='e_zone')['val']=='America/Los_Angeles'
 visible('e_notes');assert find(widget='e_notes')['val']=='Bring synthetic planning notes.\nNo real calendar write.'
 capture('04-restarted-draft');checks.append('exact_local_draft_restored_after_process_restart')
 click(text='Discard local draft');contains('Local draft discarded. Google Calendar is unchanged.')
 click(text='Resume draft');contains('No unfinished draft. Tap + Event to begin.')
 capture('05-discarded');checks.append('discard_removes_local_draft_only')
else:
 capture('01-empty-agenda');checks.append('honest_empty_and_missing_service_state')
 click(text='Resume draft');contains('No unfinished draft.')
 click(text='Refresh');contains('Connect Google')
 click(text='Account');contains('No Google account connected.')
 click(text='Connect Google');contains('no service answers "auth" on this device')
 click(text='Back to agenda');checks.append('unavailable_auth_and_empty_resume_remain_usable')
 click(text='+ Event')
 for widget,value in [('e_title','Synthetic planning session'),('e_date','2026-10-15'),('e_time','10:30'),('e_end_date','2026-10-15'),('e_end_time','11:00'),('e_zone','America/Los_Angeles'),('e_place','Fictional meeting room'),('e_notes','Bring synthetic planning notes.\nNo real calendar write.')]:type_text(widget,value)
 capture('02-local-notes');visible('e_title');capture('02-local-draft');checks.append('local_draft_accepts_complete_dates_timezone_and_multiline_notes')
 click(text='Keep draft');contains('Draft retained.')
 click(text='Resume draft');visible('e_title');assert find(widget='e_title')['val']=='Synthetic planning session'
 click(widget='kind_button');assert find(widget='kind_button')['t']=='All day ✓'
 click(widget='kind_button');assert find(widget='kind_button')['t']=='Timed event';checks.append('all_day_toggle_round_trip_preserves_draft')
 click(text='Review & Save');contains('Keep this draft, then connect Google and choose a calendar.')
 capture('03-account-required');checks.append('review_without_account_refused_and_draft_retained')
 click(text='Keep draft');contains('Draft retained.')
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
receipt={'schema':1,'recorded_at':datetime.now(timezone.utc).isoformat(),'platform':'macOS hidden card-host 412x892 logical','source_sha256':sha(r/'bundle/main.splash'),'manifest_sha256':sha(r/'bundle/manifest.json'),'binary_sha256':sha(a.binary),'driver_sha256':sha(Path(__file__)),'checks':checks,'passed':True,'screenshots':{x.name:sha(x) for x in a.out.glob('*.png')},'restart_check':a.restart_check,'live_google':False,'model_used':False,'provider_writes':False,'visual_review':'separate original-image inspection required'}
(a.out/('restart-receipt.json' if a.restart_check else 'receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'passed':True,'checks':len(checks),'restart':a.restart_check}))
