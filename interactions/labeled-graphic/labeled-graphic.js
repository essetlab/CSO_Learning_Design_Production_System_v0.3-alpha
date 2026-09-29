
(() => {
  document.querySelectorAll('[data-perspective-explorer]').forEach(explorer => {
    const controls = [...explorer.querySelectorAll('[data-perspective-control]')];
    const panels = [...explorer.querySelectorAll('[data-perspective-panel]')];
    const rail = explorer.querySelector('[data-perspective-rail]');
    const progress = explorer.querySelector('[data-perspective-progress]');
    const interpretation = document.querySelector('[data-interpretation-stage]');
    const readiness = document.querySelector('[data-perspective-ready-status]');
    const mobile = matchMedia('(max-width: 48rem)');
    const visited = new Set();
    const scene=explorer.querySelector('.perspective-scene');
    function arrangeMarkers(){
      scene?.classList.remove('is-controls-stacked');
      if(!scene || mobile.matches || scene.classList.contains('is-image-missing')) return;
      const bounds=scene.getBoundingClientRect();
      const caption=scene.querySelector('.perspective-scene__caption')?.getBoundingClientRect();
      const rects=controls.map(c=>c.getBoundingClientRect());
      const overlaps=(a,b)=>b && a.left<b.right && a.right>b.left && a.top<b.bottom && a.bottom>b.top;
      const unsafe=rects.some((r,i)=>r.left<bounds.left || r.right>bounds.right || r.bottom>bounds.bottom || overlaps(r,caption) || rects.slice(i+1).some(other=>overlaps(r,other)));
      scene.classList.toggle('is-controls-stacked',unsafe);
    }

    function panelFor(control){ return explorer.querySelector(`#${CSS.escape(control.getAttribute('aria-controls'))}`); }
    function itemFor(control){ return control.closest('[data-perspective-item]'); }
    function movePanels(){
      controls.forEach(control => {
        const panel = panelFor(control); if(!panel) return;
        if(mobile.matches) itemFor(control)?.appendChild(panel); else rail?.appendChild(panel);
      });
    }
    function updateProgress(){
      const count=visited.size;
      if(progress) progress.innerHTML=`<span>Explored</span><strong>${count} of ${controls.length}</strong>`;
      controls.forEach(c => {
        const id=c.dataset.perspectiveControl;
        const seen=visited.has(id);
        c.dataset.visited=seen?'true':'false';
        const s=c.querySelector('[data-visited-status]'); if(s) s.textContent=seen?'Viewed':'';
      });
      if(count===controls.length && interpretation?.hidden){
        interpretation.hidden=false;
        if(readiness) readiness.textContent='All three perspectives explored. You can now interpret the evidence.';
      }
      arrangeMarkers();
    }
    function select(control, focusPanel=false){
      const target=panelFor(control); if(!target) return;
      const id=control.dataset.perspectiveControl;
      const wasOpen=control.getAttribute('aria-expanded')==='true';
      if(mobile.matches && wasOpen){
        control.setAttribute('aria-expanded','false'); target.hidden=true; return;
      }
      controls.forEach(c => c.setAttribute('aria-expanded','false'));
      panels.forEach(p => p.hidden=true);
      control.setAttribute('aria-expanded','true'); target.hidden=false;
      const empty=explorer.querySelector('[data-perspective-empty]'); if(empty) empty.hidden=true;
      visited.add(id); updateProgress();
      if(focusPanel && !mobile.matches) target.focus({preventScroll:true});
    }
    controls.forEach(control => control.addEventListener('click',()=>select(control,false)));
    movePanels(); mobile.addEventListener('change',()=>{ movePanels(); const open=controls.find(c=>c.getAttribute('aria-expanded')==='true'); if(open){ const p=panelFor(open); if(p) p.hidden=false; } });
    updateProgress();
    let previousWidth=explorer.clientWidth;
    new ResizeObserver(()=>{const width=explorer.clientWidth;if(width!==previousWidth){previousWidth=width;arrangeMarkers();}}).observe(explorer);
    document.fonts?.ready.then(arrangeMarkers);

    const image=explorer.querySelector('[data-perspective-scene-image]');
    const markImageMissing=()=>image?.closest('.perspective-scene')?.classList.add('is-image-missing');
    image?.addEventListener('error',markImageMissing);
    if(image?.complete && image.naturalWidth===0) markImageMissing();

    const params=new URLSearchParams(location.search);
    if(params.get('state')==='complete') controls.forEach(c=>{ visited.add(c.dataset.perspectiveControl); });
    if(params.get('state')==='complete'){ updateProgress(); select(controls[1]||controls[0],false); }
  });

  document.querySelectorAll('[data-gr03-interpretation]').forEach(form => {
    const responsesNode=form.parentElement.querySelector('script[data-interpretation-responses]');
    const responses=responsesNode ? JSON.parse(responsesNode.textContent) : {};
    const feedback=document.getElementById(form.dataset.feedbackId || 'interpretationFeedback');
    const label=feedback?.querySelector('[data-feedback-label]');
    const title=feedback?.querySelector('[data-feedback-title]');
    const body=feedback?.querySelector('[data-feedback-body]');
    const continueButton=document.getElementById('continueButton');
    const completionStatus=document.getElementById('completionStatus');
    const revise=feedback?.querySelector('[data-interpretation-revise]');
    const reviewButton=form.querySelector('[data-interpretation-review]');
    const clearButton=form.querySelector('[data-interpretation-clear]');
    const radios=[...form.querySelectorAll('input[type="radio"]')];
    const defaultStatus='Explore all three perspectives, then review one interpretation.';
    const readyStatus='All perspectives explored. Choose and review one interpretation.';
    const completeStatus='Interpretation reviewed. You can continue or revise.';

    function allExplored(){ return !document.querySelector('[data-interpretation-stage]')?.hidden; }
    function clearRowStates(){ form.querySelectorAll('[data-option-row]').forEach(r=>r.removeAttribute('data-feedback-state')); }
    function syncReview(){ if(reviewButton) reviewButton.disabled = !allExplored() || !radios.some(r=>r.checked); }
    function resetForRevision(){
      if(feedback) feedback.hidden=true;
      clearRowStates();
      if(continueButton) continueButton.disabled=true;
      if(completionStatus) completionStatus.textContent=readyStatus;
      syncReview();
      (radios.find(r=>r.checked)||radios[0])?.focus();
    }
    radios.forEach(r=>r.addEventListener('change',syncReview));
    clearButton?.addEventListener('click',()=>{ form.reset(); clearRowStates(); if(feedback) feedback.hidden=true; if(continueButton) continueButton.disabled=true; if(completionStatus) completionStatus.textContent=readyStatus; syncReview(); radios[0]?.focus(); });
    form.addEventListener('submit',e=>{
      e.preventDefault();
      if(!allExplored()) return;
      const checked=radios.find(r=>r.checked); if(!checked){ radios[0]?.focus(); return; }
      const r=responses[checked.value]; if(!r||!feedback) return;
      clearRowStates();
      const row=form.querySelector(`[data-option-row="${CSS.escape(checked.value)}"]`); if(row) row.dataset.feedbackState=r.rowState || 'review';
      feedback.dataset.state=r.state || 'review';
      if(label) label.textContent=r.label || 'Interpretation feedback';
      if(title) title.textContent=r.title || '';
      if(body) body.textContent=r.body || '';
      feedback.hidden=false;
      if(continueButton) continueButton.disabled=false;
      if(completionStatus) completionStatus.textContent=completeStatus;
      feedback.focus({preventScroll:true});
      feedback.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'nearest'});
    });
    revise?.addEventListener('click',resetForRevision);
    const observer=new MutationObserver(syncReview); const stage=document.querySelector('[data-interpretation-stage]'); if(stage) observer.observe(stage,{attributes:true,attributeFilter:['hidden']});
    syncReview();

    const params=new URLSearchParams(location.search);
    if(params.get('state')==='complete'){
      const choice=params.get('choice') || 'B';
      const radio=radios.find(r=>r.value===choice); if(radio){ radio.checked=true; setTimeout(()=>{ syncReview(); form.requestSubmit(); },0); }
    }
  });
})();
