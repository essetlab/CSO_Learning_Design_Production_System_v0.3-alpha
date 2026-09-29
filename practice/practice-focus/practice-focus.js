(() => {
  document.querySelectorAll('[data-practice-focus]').forEach(form => {
    const storageKey=form.dataset.storageKey || 'cso-practice-focus';
    const saveState=form.querySelector('[data-save-state]');
    const clear=form.querySelector('[data-focus-clear]');
    function read(){ try{return localStorage.getItem(storageKey);}catch(e){return null;} }
    function save(value){ try{ if(value)localStorage.setItem(storageKey,value); else localStorage.removeItem(storageKey); return true;}catch(e){return false;} }
    function update(value,saved){
      const text=saveState?.querySelector('[data-save-text]');
      if(!saveState || !text) return;
      if(value){ saveState.dataset.saved=saved?'true':'false'; text.textContent=saved?'Saved for this prototype. You can change this later.':'Selected for this session. Saving is unavailable in this browser.'; if(clear)clear.hidden=false; }
      else { saveState.dataset.saved='false'; text.textContent='No practice focus selected — that is completely fine.'; if(clear)clear.hidden=true; }
    }
    form.addEventListener('change',e=>{ if(e.target.name!=='practice-focus')return; update(e.target.value,save(e.target.value)); });
    clear?.addEventListener('click',()=>{ form.reset(); save(''); update('',true); form.querySelector('input[name="practice-focus"]')?.focus(); });
    const restored=read(); if(restored){ const r=[...form.querySelectorAll('input[name="practice-focus"]')].find(x=>x.value===restored); if(r){r.checked=true; update(restored,true);} }
    const params=new URLSearchParams(location.search); const q=params.get('focus'); if(q){ const r=[...form.querySelectorAll('input[name="practice-focus"]')].find(x=>x.value===q); if(r){r.checked=true;update(q,false);} }
  });
})();
