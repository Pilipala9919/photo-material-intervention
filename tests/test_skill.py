#!/usr/bin/env python3
from pathlib import Path
import re,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
errors=[]
sk=(ROOT/'SKILL.md').read_text()
if not sk.startswith('---\n'): errors.append('missing YAML frontmatter')
if not re.search(r'^name: photo-material-intervention$',sk,re.M): errors.append('wrong skill name')
if not re.search(r'^description: .{80,}$',sk,re.M): errors.append('description missing/too short')
if not re.search(r'^author: Pilipala9919$',sk,re.M): errors.append('author attribution missing')
if 'github.com/Pilipala9919/photo-material-intervention' not in sk: errors.append('canonical source missing')
if '[diagnostic router](references/diagnostic-router.md)' not in sk: errors.append('diagnostic router is not mandatory')
router=(ROOT/'references/diagnostic-router.md').read_text() if (ROOT/'references/diagnostic-router.md').is_file() else ''
for route in ['DIRECT_ART','CLEAN_THEN_ART','PREP_THEN_ART','ASK','DECLINE']:
 if route not in router: errors.append('missing diagnostic route '+route)
for clause in ['one diagnosis, one medium decision, one generation','PHOTO_PREP` alone is never the final deliverable']:
 if clause not in (router+'\n'+sk): errors.append('missing art-routing rule '+clause)
for f in ['references/diagnostic-router.md','references/visual-diagnosis.md','references/obstruction-removal.md','references/medium-selection.md','references/prompt-compiler.md','references/quality-gate.md','references/motion-design.md','references/recipes/portal-woodcut.md','references/recipes/paint-stop-charcoal.md','references/recipes/sunlight-screenprint.md','scripts/inspect_image.py','scripts/create_edit_input.py','scripts/compare_output.py','agents/openai.yaml','LICENSE','LICENSES/MIT.txt','LICENSES/CC-BY-4.0.txt','NOTICE','CITATION.cff']:
 if not (ROOT/f).is_file(): errors.append('missing '+f)
for m in re.findall(r'\]\(([^)]+\.md)\)',sk):
 if not (ROOT/m).is_file(): errors.append('broken link '+m)
for s in (ROOT/'scripts').glob('*.py'):
 r=subprocess.run([sys.executable,'-m','py_compile',str(s)],capture_output=True,text=True)
 if r.returncode: errors.append(f'compile {s.name}: {r.stderr.strip()}')
# No private media or generated request payloads in a public skill.
for p in ROOT.rglob('*'):
 if p.is_file() and (p.suffix.lower() in {'.jpg','.jpeg','.png','.webp','.heic'} or p.name.endswith('-input.json')): errors.append('private/generated artifact '+str(p.relative_to(ROOT)))
if errors:
 print('\n'.join('FAIL: '+x for x in errors));sys.exit(1)
print('PASS: skill structure, links, scripts, and privacy checks')
