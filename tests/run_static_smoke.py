from pathlib import Path
from bs4 import BeautifulSoup
import json, yaml, re, sys
ROOT=Path(__file__).resolve().parents[1]
refs=['GR-02','GR-04','GR-01']
errors=[]; report={}
for gr in refs:
    p=ROOT/'golden-references'/gr/'index.html'
    soup=BeautifulSoup(p.read_text(),'html.parser')
    item={}
    item['h1_count']=len(soup.find_all('h1'))
    item['shell_placeholder']=bool(soup.select_one('[data-cso-shell]'))
    item['static_shell_markup_present']=bool(soup.select_one('.appbar'))
    item['local_css_exists']=(p.parent/'reference.css').exists()
    paths=[]
    for tag,attr in [('link','href'),('script','src'),('img','src')]:
        for node in soup.find_all(tag):
            val=node.get(attr)
            if not val or val.startswith(('http:','https:','#','data:')): continue
            target=(p.parent/val).resolve()
            paths.append((val,target.exists()))
            if not target.exists(): errors.append(f'{gr}: missing dependency {val}')
    item['dependencies']=paths
    if item['h1_count']!=1: errors.append(f'{gr}: expected one H1')
    if not item['shell_placeholder']: errors.append(f'{gr}: missing shared shell placeholder')
    if item['static_shell_markup_present']: errors.append(f'{gr}: duplicated shell markup in reference')
    css=(p.parent/'reference.css').read_text()
    if ':root' in css: errors.append(f'{gr}: local :root token block found')
    if re.search(r'#[0-9a-fA-F]{3,8}\b',css): errors.append(f'{gr}: raw hex in local CSS')
    report[gr]=item

# Interaction data consistency
soup=BeautifulSoup((ROOT/'golden-references/GR-02/index.html').read_text(),'html.parser')
form=soup.select_one('[data-single-choice-feedback]')
responses=json.loads(soup.select_one('script[data-choice-responses]').string)
values={x.get('value') for x in form.select('input[type=radio]')}
if values != set(responses): errors.append('GR-02: response keys do not match option values')
report['GR-02']['choice_keys_match']=values==set(responses)

soup=BeautifulSoup((ROOT/'golden-references/GR-04/index.html').read_text(),'html.parser')
form=soup.select_one('[data-single-choice-feedback]')
responses=json.loads(soup.select_one('script[data-choice-responses]').string)
values={x.get('value') for x in form.select('input[type=radio]')}
if values != set(responses): errors.append('GR-04: response keys do not match option values')
report['GR-04']['choice_keys_match']=values==set(responses)
report['GR-04']['strongest_option_present']='B' in responses and responses['B'].get('rowState')=='strongest'

soup=BeautifulSoup((ROOT/'golden-references/GR-01/index.html').read_text(),'html.parser')
report['GR-01']['practice_focus_options']=len(soup.select('input[name=practice-focus]'))
if report['GR-01']['practice_focus_options']!=5: errors.append('GR-01: expected five practice-focus options')
if not soup.select_one('[data-practice-focus]'): errors.append('GR-01: practice-focus shared behavior hook missing')

# Shared code is referenced by more than one GR
text='\n'.join((ROOT/'golden-references'/gr/'index.html').read_text() for gr in refs)
shared_refs={
 'tokens':'../../tokens/tokens.css',
 'shell_css':'../../shell/course-shell.css',
 'shell_js':'../../shell/course-shell.js',
 'button':'../../ui/button/button.css'
}
report['shared_reference_counts']={k:text.count(v) for k,v in shared_refs.items()}
for k,c in report['shared_reference_counts'].items():
    if c<3: errors.append(f'shared dependency {k} expected in all three references; found {c}')

report['status']='pass' if not errors else 'fail'; report['errors']=errors
(ROOT/'tests/static-smoke-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
sys.exit(0 if not errors else 1)
