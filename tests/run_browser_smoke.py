from pathlib import Path
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parents[1]
viewports={'1440x900':(1440,900),'1024x768':(1024,768),'390x844':(390,844),'320x568':(320,568),'720x900':(720,900)}
refs={'GR-02':'golden-references/GR-02/index.html','GR-04':'golden-references/GR-04/index.html','GR-01':'golden-references/GR-01/index.html'}
results={}
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--allow-file-access-from-files'])
    for gr,path in refs.items():
        results[gr]={}
        url=(ROOT/path).as_uri()
        for label,(w,h) in viewports.items():
            page=browser.new_page(viewport={'width':w,'height':h})
            page.goto(url,wait_until='load')
            page.wait_for_timeout(150)
            results[gr][label]=page.evaluate("""() => ({scrollWidth:document.documentElement.scrollWidth,clientWidth:document.documentElement.clientWidth,h1:document.querySelectorAll('h1').length,shell:!!document.querySelector('.appbar'),navy:getComputedStyle(document.documentElement).getPropertyValue('--color-brand-navy').trim()})""")
            page.close()
    page=browser.new_page(viewport={'width':1440,'height':900}); page.goto((ROOT/refs['GR-02']).as_uri()+'?state=complete',wait_until='load');page.wait_for_timeout(150)
    results['behavior_gr02']=page.evaluate("() => ({continueDisabled:document.getElementById('continueButton').disabled,feedbackHidden:document.getElementById('feedback').hidden})");page.close()
    page=browser.new_page(viewport={'width':1440,'height':900}); page.goto((ROOT/refs['GR-04']).as_uri()+'?state=complete&choice=B',wait_until='load');page.wait_for_timeout(150)
    results['behavior_gr04']=page.evaluate("() => ({continueDisabled:document.getElementById('continueButton').disabled,feedbackHidden:document.getElementById('feedback').hidden,selected:document.querySelector('input[name=decision-choice]:checked')?.value})");page.close()
    page=browser.new_page(viewport={'width':390,'height':844}); page.goto((ROOT/refs['GR-01']).as_uri()+'?focus=Design%20stronger%20projects',wait_until='load');page.wait_for_timeout(150)
    results['behavior_gr01']=page.evaluate("() => ({selected:document.querySelector('input[name=practice-focus]:checked')?.value,heroLoaded:document.querySelector('.hero__visual img')?.complete})");page.close()
    browser.close()
results['pass']=all(v['scrollWidth']==v['clientWidth'] and v['h1']==1 and v['shell'] and v['navy']=='#0F172A' for gr in ['GR-02','GR-04','GR-01'] for v in results[gr].values()) and not results['behavior_gr02']['continueDisabled'] and not results['behavior_gr04']['continueDisabled']
(ROOT/'tests/smoke-results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
raise SystemExit(0 if results['pass'] else 1)
