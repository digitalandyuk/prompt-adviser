#!/usr/bin/env python3
"""Opt-in live source-check test with a fictional prompt and no task execution."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--live',action='store_true',help='Authorise generic public source lookup for this fictional test')
    args=p.parse_args()
    if not args.live:p.error('No live lookup requested. Use --live explicitly.')
    out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
    skill=(ROOT/'dist/codex/prompt-adviser/SKILL.md').read_text()
    refs='\n'.join((ROOT/'references'/f).read_text() for f in ('prompt-sources.md','jev.md','workflow-prompts.md'))
    prompt=(
      'Apply the packaged adviser to this fictional request. Public web search and opening public source pages are available. '
      'No other tools, local files, app access, delegation or task execution are permitted. Supporting references are embedded below. '
      'Return the adviser response, not an evaluation report.\n<skill>\n'+skill+'\n</skill>\n<references>\n'+refs+'\n</references>\n'
      'USER: Create the finished reusable Codex prompt now for this fictional brief: make a four-page UK-English product brochure '
      'for adults from [ASSETS] and [APPROVED_COPY], with [BUDGET] as an input. Preserve originals; show an editable prototype '
      'for approval before full production; deliver editable SVG files and a review PDF and inspect every page. '
      'No purchase or publishing is authorised. Use no role. Write the prompt without making files or doing the brochure work.'
    )
    (out/'codex-live.input.txt').write_text(prompt)
    result=subprocess.run(['codex','--search','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','-s','read-only',
       '-C',str(out),'--json','-o',str(out/'codex-live.md'),'-'],input=prompt,text=True,capture_output=True,timeout=240)
    events=[]
    for line in result.stdout.splitlines():
        try:events.append(json.loads(line))
        except ValueError:pass
    items=[e.get('item',{}) for e in events if e.get('type')=='item.completed']
    actions=[i for i in items if i.get('type') not in ('reasoning','agent_message')]
    record={'host':'Codex CLI with live web search','edition':'codex','exit_code':result.returncode,
       'skill_sha256':hashlib.sha256(skill.encode()).hexdigest(),'tool_items':actions,
       'usage':[e.get('usage') for e in events if e.get('type')=='turn.completed']}
    if result.returncode:record['error']=result.stderr[-1500:]
    (out/'codex-live.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    if result.returncode:raise SystemExit(result.returncode)
