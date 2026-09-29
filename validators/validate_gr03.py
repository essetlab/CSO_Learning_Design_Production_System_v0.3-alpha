#!/usr/bin/env python3
from pathlib import Path
import json, sys
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
errors=[]; report={}
def load(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
components={x['id'] for x in load('registries/components.json')['objects']}
comps={x['id'] for x in load('registries/compositions.json')['objects']}
pats={x['id'] for x in load('registries/patterns.json')['objects']}
assets={x['id']:x for x in load('registries/assets.json')['assets']}
for oid in ['BLK-PERSPECTIVE-01','INT-LABELED-GRAPHIC-01']:
    if oid not in components: errors.append(f'unknown component {oid}')
if 'CMP-PERSPECTIVE-01' not in comps: errors.append('unknown composition CMP-PERSPECTIVE-01')
for oid in ['IP-INTERPRET-01','IP-PERSPECTIVE-01']:
    if oid not in pats: errors.append(f'unknown pattern {oid}')
aid='AST-HRBA-GR03-VOICE-SAFETY-EXISTING-01'
if aid not in assets: errors.append('GR-03 asset not registered')
elif not (ROOT/assets[aid]['path']).is_file(): errors.append('GR-03 asset file missing')
p=ROOT/'golden-references/GR-03/index.html'; soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
report['h1_count']=len(soup.find_all('h1'))
report['perspective_controls']=len(soup.select('[data-perspective-control]'))
report['perspective_panels']=len(soup.select('[data-perspective-panel]'))
report['interpretation_options']=len(soup.select('input[name="gr03-interpretation"]'))
report['local_css_empty']=(p.parent/'reference.css').read_text(encoding='utf-8')==''
report['shell_placeholder']=bool(soup.select_one('[data-cso-shell]'))
if report['h1_count']!=1: errors.append('expected one H1')
if report['perspective_controls']!=3 or report['perspective_panels']!=3: errors.append('expected exactly three perspectives')
if report['interpretation_options']!=4: errors.append('expected exactly four interpretation options')
if not report['local_css_empty']: errors.append('GR-03 local CSS must remain empty')
if not report['shell_placeholder']: errors.append('shared shell placeholder missing')
for tag,attr in [('link','href'),('script','src'),('img','src')]:
    for node in soup.find_all(tag):
        val=node.get(attr)
        if not val or val.startswith(('http:','https:','#','data:')): continue
        if not (p.parent/val).resolve().exists(): errors.append(f'missing dependency {val}')
contract=load('prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json')
limits=contract['content_limits']['maximum_words']
fields={
    'perspective_label':[c.select('span')[1].get_text() for c in soup.select('[data-perspective-control]')],
    'observation':[e.select('section p')[0].get_text() for e in soup.select('.perspective-evidence')],
    'interpretation':[e.select('section p')[1].get_text() for e in soup.select('.perspective-evidence')],
    'limitation':[e.select('section p')[2].get_text() for e in soup.select('.perspective-evidence')],
    'answer_option':[e.get_text() for e in soup.select('.option-row__content')],
    'feedback':[r['body'] for r in json.loads(soup.select_one('[data-interpretation-responses]').string).values()]
}
report['content_limits']=limits
report['content_word_counts']={field:[len(value.split()) for value in values] for field,values in fields.items()}
for field,counts in report['content_word_counts'].items():
    if any(count>limits[field] for count in counts): errors.append(f'{field}: frozen maximum exceeded')
report['status']='pass' if not errors else 'fail'; report['errors']=errors
(ROOT/'tests/gr03-static-validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
raise SystemExit(0 if not errors else 1)
