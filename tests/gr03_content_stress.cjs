/* Only intercept the browser's HTML response; production HTML is never written. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '..');
const limits = JSON.parse(fs.readFileSync(path.join(root,'prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json'),'utf8')).content_limits.maximum_words;
const words = 'Community participants describe meaningful participation through careful observation of priorities influence representation consultation opportunities established practices and available evidence while respecting uncertainty about individual experiences and the conditions supporting safe contributions';
function text(n) { const list=words.split(/\s+/); return Array.from({length:n},(_,i)=>list[i%list.length]).join(' ')+'.'; }
const fixture = Object.fromEntries(Object.entries(limits).map(([k,n])=>[k,text(n)]));
async function runStress(browser, {check,layout,shot,url}) {
  const production=path.join(root,'golden-references/GR-03/index.html');
  const hash=()=>crypto.createHash('sha256').update(fs.readFileSync(production)).digest('hex');
  const before=hash();
  check('stress: exact frozen word counts',Object.entries(fixture).every(([k,v])=>v.split(/\s+/).length===limits[k]),{limits,fixture,word_count_rule:'Whitespace-delimited tokens; punctuation does not add words. Test convention only.'});
  for(const [width,height] of [[1920,1080],[1440,900],[1024,768],[768,1024],[390,844],[320,568]]) {
    const page=await browser.newPage({viewport:{width,height}});
    const label=`stress-${width}x${height}`;
    // The initializer is injected before the product scripts register state handlers.
    await page.route('**/golden-references/GR-03/index.html',async route=>{
      const response=await route.fetch(); let html=await response.text();
      const script=`<script>(()=>{const f=${JSON.stringify(fixture)};
        document.querySelectorAll('[data-perspective-control]').forEach(c=>c.children[1].textContent=f.perspective_label);
        document.querySelectorAll('.perspective-evidence').forEach(p=>{p.children[0].querySelector('p').textContent=f.observation;p.children[1].querySelector('p').textContent=f.interpretation;p.children[2].querySelector('p').textContent=f.limitation;});
        document.querySelectorAll('.option-row__content').forEach(p=>p.textContent=f.answer_option);
        const node=document.querySelector('[data-interpretation-responses]'), data=JSON.parse(node.textContent);
        Object.values(data).forEach(r=>r.body=f.feedback);node.textContent=JSON.stringify(data);
      })();<\/script>`;
      html=html.replace('<script src="../../shell/course-shell.js">',script+'<script src="../../shell/course-shell.js">');
      await route.fulfill({response,body:html});
    });
    await page.goto(url);
    const actualCounts=await page.evaluate(()=>{
      const count=e=>e.textContent.trim().split(/\s+/).length;
      return {
        perspective_label:[...document.querySelectorAll('[data-perspective-control]')].map(c=>count(c.children[1])),
        observation:[...document.querySelectorAll('.perspective-evidence')].map(e=>count(e.children[0].querySelector('p'))),
        interpretation:[...document.querySelectorAll('.perspective-evidence')].map(e=>count(e.children[1].querySelector('p'))),
        limitation:[...document.querySelectorAll('.perspective-evidence')].map(e=>count(e.children[2].querySelector('p'))),
        answer_option:[...document.querySelectorAll('.option-row__content')].map(count),
        feedback:Object.values(JSON.parse(document.querySelector('[data-interpretation-responses]').textContent)).map(r=>r.body.split(/\s+/).length)
      };
    });
    check(`${label}: injected content reaches every frozen maximum`,Object.entries(actualCounts).every(([k,counts])=>counts.length>0&&counts.every(n=>n===limits[k])),actualCounts);
    await layout(page,`${label} initial`);
    await inspectStress(page,label+' initial',check,fixture);
    await shot(page,label+'-initial');
    for(const id of ['presence','agenda','voice']) {
      await page.locator(`[data-perspective-control="${id}"]`).click();
      await page.waitForTimeout(250);
      await inspectStress(page,`${label} ${id}`,check,fixture);
    }
    await page.locator('input[value="D"]').check();
    await page.locator('[data-interpretation-review]').click();
    await layout(page,label+' feedback');
    await inspectStress(page,label+' feedback',check,fixture);
    check(`${label}: complete option and feedback text`,await page.locator('.option-row__content').evaluateAll((els,expected)=>els.length===4&&els.every(e=>e.textContent===expected),fixture.answer_option) && await page.locator('[data-feedback-body]').innerText()===fixture.feedback);
    check(`${label}: completion and mobile disclosure`,await page.locator('#continueButton').isEnabled() && await page.evaluate(()=>!matchMedia('(max-width:48rem)').matches || [...document.querySelectorAll('[data-perspective-control]')].every(c=>c.nextElementSibling?.id===c.getAttribute('aria-controls'))));
    await shot(page,label+'-feedback-completed');
    await page.locator('[data-interpretation-revise]').click();
    check(`${label}: revision disables completion`,await page.locator('#continueButton').isDisabled());
    await page.locator('[data-interpretation-review]').click();
    await page.locator('#continueButton').scrollIntoViewIfNeeded();
    check(`${label}: re-review restores reachable Continue`,await page.locator('#continueButton').isEnabled());
    await page.close();
  }
  check('stress: production learner HTML byte-for-byte unchanged',hash()===before,{before,after:hash()});
}
async function inspectStress(page,label,check) {
  const result=await page.evaluate(()=>{
    const de=document.documentElement;
    const visible=e=>e.getClientRects().length&&!e.closest('[hidden],[inert],.visually-hidden');
    const clipping=[];
    for(const el of document.querySelectorAll('.perspective-marker span,.perspective-evidence p,.option-row__content,[data-feedback-body]')) {
      if(!visible(el)) continue;
      const range=document.createRange(); range.selectNodeContents(el);
      for(const r of range.getClientRects()) {
        if(r.left<0||r.right>de.clientWidth+1) clipping.push(el.textContent);
        for(let p=el;p&&p!==document.body;p=p.parentElement) {
          const s=getComputedStyle(p),b=p.getBoundingClientRect();
          if(/hidden|clip/.test(s.overflowX)&& (r.left<b.left-1||r.right>b.right+1)) clipping.push(el.textContent);
          if(/hidden|clip/.test(s.overflowY)&& (r.top<b.top-1||r.bottom>b.bottom+1)) clipping.push(el.textContent);
        }
      }
    }
    const controls=[...document.querySelectorAll('[data-perspective-control]')].map(e=>{const r=e.getBoundingClientRect();return {id:e.dataset.perspectiveControl,x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom};});
    const caption=document.querySelector('.perspective-scene__caption').getBoundingClientRect();
    const overlaps=[];
    const intersect=(a,b)=>a.x<b.right&&a.right>b.x&&a.y<b.bottom&&a.bottom>b.y;
    for(let i=0;i<controls.length;i++) {if(intersect(controls[i],caption)) overlaps.push(controls[i].id+' / scene caption');for(let j=i+1;j<controls.length;j++) if(intersect(controls[i],controls[j])) overlaps.push(controls[i].id+' / '+controls[j].id);}
    return {scrollWidth:de.scrollWidth,clientWidth:de.clientWidth,clipping:[...new Set(clipping)],controls,overlaps,viewportHeight:innerHeight};
  });
  check(`${label}: stress text is not clipped`,!result.clipping.length&&result.scrollWidth===result.clientWidth,result);
  // 44px is the shared touch minimum; screen-height bound is an explicit test heuristic, not a new authoring limit.
  check(`${label}: stress controls fit and do not overlap`,!result.overlaps.length&&result.controls.every(c=>c.width>=44&&c.height>=44&&c.height<result.viewportHeight/2),result);
}
module.exports={runStress};
