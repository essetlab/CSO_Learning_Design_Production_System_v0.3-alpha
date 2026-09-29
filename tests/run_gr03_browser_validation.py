from pathlib import Path
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parents[1]
URL='http://127.0.0.1:8765/golden-references/GR-03/index.html'
viewports={'1920x1080':(1920,1080),'1440x900':(1440,900),'1024x768':(1024,768),'768x1024':(768,1024),'390x844':(390,844),'320x568':(320,568)}
results={'viewports':{},'behavior':{},'keyboard':{},'reduced_motion':{},'image_failure':{}}
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--allow-file-access-from-files'])
    for label,(w,h) in viewports.items():
        page=browser.new_page(viewport={'width':w,'height':h})
        page.goto(URL,wait_until='load'); page.wait_for_timeout(120)
        results['viewports'][label]=page.evaluate("""() => ({
          scrollWidth:document.documentElement.scrollWidth,clientWidth:document.documentElement.clientWidth,
          h1:document.querySelectorAll('h1').length,shell:!!document.querySelector('.appbar'),
          stageHidden:document.querySelector('[data-interpretation-stage]').hidden,
          imageComplete:document.querySelector('[data-perspective-scene-image]').complete
        })""")
        page.close()
    page=browser.new_page(viewport={'width':1440,'height':900}); page.goto(URL,wait_until='load')
    for id in ['presence','agenda','voice']: page.click(f'[data-perspective-control="{id}"]')
    unlocked=page.eval_on_selector('[data-interpretation-stage]','e=>!e.hidden')
    states={}
    for choice in ['A','B','C','D']:
        page.check(f'input[name="gr03-interpretation"][value="{choice}"]'); page.click('[data-interpretation-review]'); page.wait_for_timeout(40)
        states[choice]=page.evaluate("""() => ({feedbackHidden:document.getElementById('interpretationFeedback').hidden,continueDisabled:document.getElementById('continueButton').disabled,title:document.querySelector('[data-feedback-title]').textContent})""")
        page.click('[data-interpretation-revise]')
        states[choice]['afterReviseDisabled']=page.eval_on_selector('#continueButton','e=>e.disabled')
    results['behavior']={'stageUnlocked':unlocked,'choices':states}
    page.close()

    page=browser.new_page(viewport={'width':390,'height':844}); page.goto(URL,wait_until='load')
    # keyboard complete lenses
    page.focus('[data-perspective-control="presence"]'); page.keyboard.press('Enter'); page.focus('[data-perspective-control="agenda"]'); page.keyboard.press('Space'); page.focus('[data-perspective-control="voice"]'); page.keyboard.press('Enter')
    results['keyboard']['stageUnlocked']=page.eval_on_selector('[data-interpretation-stage]','e=>!e.hidden')
    page.click('[data-shell-menu-button]'); page.keyboard.press('Escape'); results['keyboard']['menuFocusReturned']=page.evaluate("() => document.activeElement === document.querySelector('[data-shell-menu-button]')")
    page.close()

    page=browser.new_page(viewport={'width':390,'height':844},reduced_motion='reduce'); page.goto(URL,wait_until='load')
    results['reduced_motion']['scrollBehavior']=page.evaluate("() => getComputedStyle(document.documentElement).scrollBehavior")
    page.close()

    page=browser.new_page(viewport={'width':390,'height':844})
    page.route('**/AST-HRBA-GR03-VOICE-SAFETY-EXISTING-01.webp',lambda route: route.abort())
    page.goto(URL,wait_until='load'); page.wait_for_timeout(100)
    results['image_failure']=page.evaluate("""() => ({sceneMissing:document.querySelector('.perspective-scene').classList.contains('is-image-missing'),fallbackVisible:getComputedStyle(document.querySelector('.perspective-image-fallback')).display!=='none'})""")
    page.close(); browser.close()

pass_view=all(v['scrollWidth']==v['clientWidth'] and v['h1']==1 and v['shell'] for v in results['viewports'].values())
pass_choices=results['behavior']['stageUnlocked'] and all((not x['feedbackHidden']) and (not x['continueDisabled']) and x['afterReviseDisabled'] for x in results['behavior']['choices'].values())
results['pass']=pass_view and pass_choices and results['keyboard']['stageUnlocked'] and results['keyboard']['menuFocusReturned'] and results['image_failure'].get('fallbackVisible')
(ROOT/'tests/gr03-browser-validation.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,indent=2))
raise SystemExit(0 if results['pass'] else 1)
