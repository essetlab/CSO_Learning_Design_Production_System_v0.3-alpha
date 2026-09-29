(() => {
  document.querySelectorAll('[data-single-choice-feedback]').forEach(form => {
    const configScript = form.parentElement.querySelector('script[type="application/json"][data-choice-responses]');
    if (!configScript) return;
    const responses = JSON.parse(configScript.textContent);
    const feedback = document.getElementById(form.dataset.feedbackId || 'feedback');
    const label = feedback?.querySelector('[data-feedback-label]');
    const title = feedback?.querySelector('[data-feedback-title]');
    const body = feedback?.querySelector('[data-feedback-body]');
    const reasoning = feedback?.querySelector('[data-feedback-reasoning]');
    const continueButton = document.getElementById('continueButton');
    const completionStatus = document.getElementById('completionStatus');
    const clear = form.querySelector('[data-choice-clear]');
    const revise = feedback?.querySelector('[data-choice-revise]');
    const radioName = form.dataset.radioName;
    const defaultStatus = form.dataset.defaultStatus || 'Review a response to continue.';
    const completeStatus = form.dataset.completeStatus || 'Feedback reviewed. You can continue or revise.';

    function rows(){ return [...form.querySelectorAll('[data-option-row]')]; }
    function clearStates(){ rows().forEach(row => row.removeAttribute('data-feedback-state')); }
    function show(value, focus=true){
      const r=responses[value]; if(!r || !feedback) return;
      clearStates();
      const row=form.querySelector(`[data-option-row="${CSS.escape(value)}"]`);
      if(row && r.rowState) row.dataset.feedbackState=r.rowState;
      feedback.dataset.state=r.state || '';
      if(label) label.textContent=r.label || 'Feedback';
      if(title) title.textContent=r.title || '';
      if(body) body.textContent=r.body || '';
      if(reasoning) reasoning.hidden = r.showReasoning === false;
      feedback.hidden=false;
      if(continueButton) continueButton.disabled=false;
      if(completionStatus) completionStatus.textContent=completeStatus;
      if(focus){ feedback.focus({preventScroll:true}); feedback.scrollIntoView({behavior:'smooth',block:'nearest'}); }
    }
    function reset(status=defaultStatus, clearSelection=false){
      if(clearSelection) form.reset();
      if(feedback) feedback.hidden=true;
      if(reasoning) reasoning.hidden=true;
      clearStates();
      if(continueButton) continueButton.disabled=true;
      if(completionStatus) completionStatus.textContent=status;
    }

    form.addEventListener('submit', e => {
      e.preventDefault();
      const checked=form.querySelector(`input[name="${CSS.escape(radioName)}"]:checked`);
      if(!checked){ form.querySelector(`input[name="${CSS.escape(radioName)}"]`)?.focus(); return; }
      show(checked.value,true);
    });
    clear?.addEventListener('click',()=>{ reset(defaultStatus,true); form.querySelector(`input[name="${CSS.escape(radioName)}"]`)?.focus(); });
    revise?.addEventListener('click',()=>{ reset(form.dataset.reviseStatus || 'Revise your response, then review the feedback again.',false); (form.querySelector(`input[name="${CSS.escape(radioName)}"]:checked`) || form.querySelector(`input[name="${CSS.escape(radioName)}"]`))?.focus(); });

    const params=new URLSearchParams(location.search);
    if(params.get('state')==='complete'){
      const qa=params.get('choice') || form.dataset.qaCompleteValue;
      const radio=form.querySelector(`input[name="${CSS.escape(radioName)}"][value="${CSS.escape(qa)}"]`);
      if(radio){ radio.checked=true; show(radio.value,false); }
    }
  });
})();
