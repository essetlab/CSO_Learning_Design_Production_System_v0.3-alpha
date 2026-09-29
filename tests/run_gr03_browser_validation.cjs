/* Windows-capable companion to the existing Python runner. No product markup is replaced. */
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const os = require('node:os');
const root = path.resolve(__dirname, '..');
const out = path.join(__dirname, 'gr03-screenshots');
fs.mkdirSync(out, { recursive: true });
const run = process.env.GR03_RUN || 'final';
const report = { run, date: new Date().toISOString(), environment: { os: `${os.type()} ${os.release()} ${os.arch()}`, framework: `Playwright ${require('playwright/package.json').version}`, browser: 'Google Chrome', mode: 'headless' }, checks: [], screenshots: [], errors: [] };
const port = Number(process.env.GR03_PORT || 8766);
const url = `http://127.0.0.1:${port}/golden-references/GR-03/index.html`;
const lens = id => `[data-perspective-control="${id}"]`;
const server = http.createServer((req, res) => {
  const file = path.resolve(root, '.' + decodeURIComponent(new URL(req.url, url).pathname));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  fs.readFile(file, (err, data) => {
    if (err) { res.writeHead(404).end(); return; }
    res.setHeader('Content-Type', ({'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.webp':'image/webp','.png':'image/png'})[path.extname(file)] || 'application/octet-stream');
    res.end(data);
  });
});
function check(name, passed, details) { report.checks.push({ name, passed: !!passed, details }); }
async function shot(page, name) { const file = `${run}-${name}.png`; await page.evaluate(()=>scrollTo(0,0)); await page.waitForTimeout(350); await page.screenshot({ path: path.join(out, file), fullPage: true, animations:'disabled' }); report.screenshots.push(`tests/gr03-screenshots/${file}`); }
async function fresh(browser, size = [1440,900], extra = {}) {
  const page = await browser.newPage({ viewport: { width:size[0], height:size[1] }, ...extra });
  page.on('pageerror', error => report.errors.push(error.message));
  await page.goto(url); return page;
}
async function explore(page) { for (const id of ['presence','agenda','voice']) await page.locator(lens(id)).click(); }
async function layout(page, label) {
  await page.waitForTimeout(250);
  const geometry = await page.evaluate(() => {
    const de = document.documentElement;
    const clipped = [...document.querySelectorAll('main p, main h1, main h2, main h3, main h4, .option-row__content, .feedback, button')].filter(e => {
      if (!e.getClientRects().length || e.closest('[hidden], [inert], .visually-hidden, .sr-only')) return false;
      const r=e.getBoundingClientRect(); return r.left < -1 || r.right > de.clientWidth+1 || e.scrollWidth > e.clientWidth+2;
    }).map(e=>({text:e.textContent.trim().slice(0,100),width:e.clientWidth,scroll:e.scrollWidth}));
    return { scrollWidth:de.scrollWidth,clientWidth:de.clientWidth,clipped };
  });
  check(`${label}: no horizontal overflow or text clipping`, geometry.scrollWidth===geometry.clientWidth && !geometry.clipped.length, geometry);
  const unreachable=[];
  for (const selector of ['[data-shell-menu-button]',lens('presence'),lens('agenda'),lens('voice'),'[data-interpretation-review]','[data-interpretation-revise]','#continueButton']) {
    const el=page.locator(selector);
    if (!await el.isVisible()) continue;
    await el.scrollIntoViewIfNeeded();
    const hit = await el.evaluate(e=>{const r=e.getBoundingClientRect(), x=r.x+r.width/2,y=r.y+r.height/2;const top=document.elementFromPoint(x,y);return x>=0&&x<=innerWidth&&y>=0&&y<=innerHeight&&(top===e||e.contains(top));});
    if (!hit) unreachable.push(selector);
  }
  check(`${label}: controls reachable and unobscured`, !unreachable.length, unreachable);
}
async function flow(page,label,allChoices=true) {
  check(`${label}: initial gating`, await page.locator('#continueButton').isDisabled() && await page.locator('[data-interpretation-stage]').isHidden() && await page.locator('[data-visited="true"]').count()===0 && await page.locator('input:checked').count()===0);
  for (const [i,id] of ['presence','agenda','voice'].entries()) {
    await page.locator(lens(id)).click();
    check(`${label}: ${id} opens and gates interpretation`, await page.locator(`#perspective-${id}`).isVisible() && await page.locator(lens(id)).getAttribute('aria-expanded')==='true' && await page.locator('[data-interpretation-stage]').isVisible()===(i===2));
    check(`${label}: ${id} visited has text`, (await page.locator(lens(id)).innerText()).includes('Viewed'));
    check(`${label}: empty prompt hidden after ${id}`,await page.locator('[data-perspective-empty]').isHidden());
  }
  await page.locator(lens('presence')).click();
  check(`${label}: reopen visited lens`, await page.locator('#perspective-presence').isVisible() && await page.locator('[data-visited="true"]').count()===3);
  check(`${label}: no preselection and review disabled`, await page.locator('input:checked').count()===0 && await page.locator('[data-interpretation-review]').isDisabled());
  const responses=await page.locator('[data-interpretation-responses]').evaluate(e=>JSON.parse(e.textContent));
  for (const choice of (allChoices?['A','B','C','D']:['A'])) {
    await page.locator(`input[value="${choice}"]`).check();
    check(`${label}: ${choice} selection before review`, await page.locator('[data-interpretation-review]').isEnabled() && await page.locator('#interpretationFeedback').isHidden() && await page.locator('#continueButton').isDisabled());
    await page.locator('[data-interpretation-review]').click();
    check(`${label}: ${choice} exact feedback and completion`, await page.locator('[data-feedback-title]').innerText()===responses[choice].title && await page.locator('[data-feedback-body]').innerText()===responses[choice].body && await page.locator('#continueButton').isEnabled());
    await layout(page,`${label} feedback ${choice}`);
    if (choice==='A') await shot(page,`${label}-feedback-A-completed`);
    await page.locator('[data-interpretation-revise]').click();
    check(`${label}: ${choice} revision resets completion and preserves state`, await page.locator('#continueButton').isDisabled() && await page.locator('#interpretationFeedback').isHidden() && await page.locator(`input[value="${choice}"]`).isChecked() && await page.locator('[data-visited="true"]').count()===3);
    await page.locator('[data-interpretation-review]').click();
    check(`${label}: ${choice} re-review completes`,await page.locator('#continueButton').isEnabled());
    await page.locator('[data-interpretation-revise]').click();
  }
}
async function tabTo(page,selector,trail) {
  for (let i=0;i<30;i++) {
    if(await page.locator(selector).evaluate(e=>e===document.activeElement)) return;
    await page.keyboard.press('Tab');
    trail.push(await page.evaluate(()=>({tag:document.activeElement.tagName,text:document.activeElement.textContent.trim().slice(0,60),value:document.activeElement.value,focusVisible:document.activeElement.matches(':focus-visible'),outline:getComputedStyle(document.activeElement).outlineStyle})));
  }
  throw Error(`Tab could not reach ${selector}`);
}
async function main() {
  await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(port,'127.0.0.1',resolve);});
  const browser=await chromium.launch({channel:'chrome',headless:true}); report.environment.version=browser.version();
  try {
    await require('./gr03_content_stress.cjs').runStress(browser,{check,layout,shot,url});
    for(const size of [[1920,1080],[1440,900],[1024,768],[768,1024],[390,844],[320,568]]) {
      const label=size.join('x'),page=await fresh(browser,size);
      await layout(page,`${label} initial`); await page.evaluate(()=>scrollTo(0,0)); await shot(page,`${label}-initial`);
      await flow(page,label);
      check(`${label}: mobile panels follow their controls`, await page.evaluate(()=>!matchMedia('(max-width:48rem)').matches || [...document.querySelectorAll('[data-perspective-control]')].every(c=>c.nextElementSibling?.id===c.getAttribute('aria-controls'))));
      await page.close();
    }
    for(const size of [[1440,900],[390,844]]) {
      const page=await fresh(browser,size),trail=[];const label=`keyboard-${size.join('x')}`;
      await tabTo(page,'[data-shell-menu-button]',trail); await page.keyboard.press('Enter');
      check(`${label}: Menu opens`,await page.locator('[data-shell-menu-button]').getAttribute('aria-expanded')==='true');
      check(`${label}: Menu accessible name`,await page.getByRole('button',{name:'Menu',exact:true}).count()===1);
      await page.keyboard.press('Escape');
      check(`${label}: Escape returns focus`,await page.locator('[data-shell-menu-button]').evaluate(e=>e===document.activeElement));
      for(const [i,id] of ['presence','agenda','voice'].entries()) { await tabTo(page,lens(id),trail); await page.keyboard.press(i===1?'Space':'Enter'); }
      await tabTo(page,'input[value="A"]',trail); await page.keyboard.press('Space'); await page.keyboard.press('ArrowDown');
      check(`${label}: native radio arrows`,await page.locator('input[value="B"]').isChecked());
      await tabTo(page,'[data-interpretation-review]',trail); await page.keyboard.press('Enter');
      await tabTo(page,'[data-interpretation-revise]',trail); await page.keyboard.press('Enter');
      check(`${label}: revision focus to selected radio`,await page.locator('input[value="B"]').evaluate(e=>e===document.activeElement));
      await tabTo(page,'[data-interpretation-review]',trail); await page.keyboard.press('Space');
      await tabTo(page,'#continueButton',trail);
      check(`${label}: complete with keyboard, visible focus`,await page.locator('#continueButton').isEnabled() && trail.every(x=>x.focusVisible && x.outline!=='none'),trail);
      await shot(page,label+'-complete'); await page.close();
    }
    {
      const page=await fresh(browser,[1440,900],{reducedMotion:'reduce'});
      await page.evaluate(()=>{window.scrollCalls=[];const original=Element.prototype.scrollIntoView;Element.prototype.scrollIntoView=function(options){window.scrollCalls.push(options);return original.call(this,options)};});
      await flow(page,'reduced-motion',false);
      const motion=await page.evaluate(()=>({reduced:matchMedia('(prefers-reduced-motion: reduce)').matches,animation:getComputedStyle(document.querySelector('.perspective-panel')).animationDuration,transition:getComputedStyle(document.querySelector('.perspective-marker')).transitionDuration,scroll:getComputedStyle(document.documentElement).scrollBehavior,calls:window.scrollCalls}));
      check('reduced motion: no explicit smooth scroll',motion.reduced&&motion.scroll==='auto'&&motion.calls.every(x=>x.behavior!=='smooth'),motion);
      await page.close();
    }
    for(const size of [[1440,900],[390,844]]) {
      const page=await browser.newPage({viewport:{width:size[0],height:size[1]}});
      await page.route('**/AST-HRBA-GR03-VOICE-SAFETY-EXISTING-01.webp',route=>route.abort()); await page.goto(url);
      const label=`image-failure-${size.join('x')}`;
      check(`${label}: fallback visible and broken image hidden`,await page.locator('.perspective-image-fallback').isVisible() && await page.locator('[data-perspective-scene-image]').isHidden());
      check(`${label}: fallback text does not overlap controls`,await page.evaluate(()=>{const t=document.querySelector('.perspective-image-fallback').getBoundingClientRect();return [...document.querySelectorAll('[data-perspective-control]')].every(c=>{const r=c.getBoundingClientRect();return r.bottom<=t.top||r.top>=t.bottom||r.right<=t.left||r.left>=t.right;});}));
      await flow(page,label,false); await shot(page,label); await page.close();
    }
    {
      const page=await browser.newPage({viewport:{width:390,height:844}}); let release;
      const delayed=new Promise(resolve=>release=resolve);
      await page.route('**/AST-HRBA-GR03-VOICE-SAFETY-EXISTING-01.webp',async route=>{await delayed;await route.continue();});
      await page.goto(url,{waitUntil:'domcontentloaded'});
      await explore(page);await page.locator('input[value="D"]').check();await page.locator('[data-interpretation-review]').click();
      check('delayed image: learning completes before image load',await page.locator('#continueButton').isEnabled() && await page.locator('[data-perspective-scene-image]').evaluate(e=>!e.complete));
      const before=await page.locator('.perspective-scene__caption').evaluate(e=>e.getBoundingClientRect().top+scrollY);
      release();await page.waitForLoadState('load');
      const after=await page.locator('.perspective-scene__caption').evaluate(e=>e.getBoundingClientRect().top+scrollY);
      check('delayed image: stable reserved geometry',Math.abs(before-after)<2,{before,after});await shot(page,'delayed-image-completed');await page.close();
    }
  } finally { await browser.close();server.close(); }
}
main().catch(error=>{report.errors.push(error.stack);server.close();}).finally(()=>{
  report.automated_pass=report.checks.every(x=>x.passed)&&!report.errors.length;
  report.content_stress={checks:report.checks.filter(x=>x.name.startsWith('stress')),pass:report.checks.filter(x=>x.name.startsWith('stress')).every(x=>x.passed)};
  report.actual_zoom=JSON.parse(fs.readFileSync(path.join(__dirname,'gr03-native-zoom-validation.json'),'utf8'));
  // Native evidence is reviewed separately; an automated rerun never upgrades the governed decision.
  report.pass=false;
  report.status='FAIL';
  fs.writeFileSync(path.join(__dirname,`gr03-browser-validation${run==='final'?'':'-'+run}.json`),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify({automated_pass:report.automated_pass,status:report.status,checks:report.checks.length,failures:report.checks.filter(x=>!x.passed),errors:report.errors},null,2));
  process.exitCode=report.automated_pass?0:1;
});
