import {createModel} from './model.js';
import {node,diagnosis,draft,comparison,rubric,writingField,representation} from '../../learning-blocks/work-artifact/work-artifact.js';
import {createLearningState,downloadText,copyText} from '../../state/learning-state/learning-state.js';
import {arrangeWorkspace} from '../../templates/deep-workspace/deep-workspace.js';

const config=document.querySelector('[data-repair-contract]');
if(config)mount(JSON.parse(config.textContent));
export function mount(c) {
  const model=createModel(c);let s=model.fresh(),store;
  const host=document.querySelector('[data-repair-workspace]');
  const {nav,reference,work}=arrangeWorkspace(host);
  const announce=node('p',{role:'status','aria-live':'polite',class:'studio-status',id:'work-status'});
  const saving=node('section',{class:'studio-save','aria-label':'Draft recovery and device saving'});
  const sessionReceipt=node('p',{id:'session-receipt',class:'save-state'}),deviceReceipt=node('p',{id:'device-receipt',class:'save-state'});
  const consent=node('input',{type:'checkbox',id:'device-consent'});
  const issue=node('div',{class:'studio-recovery',hidden:''});
  const exportArea=node('section',{'aria-label':'Retain your work'});
  const output=node('pre',{class:'work-package',id:'export-text',tabindex:'0',hidden:''});
  const errors=node('section',{class:'studio-errors',id:'error-summary',tabindex:'-1','aria-label':'Please check your work',hidden:''});
  const action=(label,fn,id)=>{const b=node('button',{type:'button',class:'button button--secondary',text:label,...(id?{id}:{})});b.addEventListener('click',fn);return b;};
  const primary=(label,fn,id)=>{const b=action(label,fn,id);b.className='button button--primary';return b;};
  const controls=node('div',{class:'studio-actions'},[
    action('Show text to copy',()=>{output.textContent=representation(c,s,model.predicates(s).COMPLETE);output.hidden=false;output.focus();},'show-text'),
    action('Copy current work',async()=>{output.textContent=representation(c,s,model.predicates(s).COMPLETE);output.hidden=false;try{await copyText(output.textContent);announce.textContent='Current work copied.';}catch{announce.textContent='Clipboard unavailable. Select and copy the complete text below.';output.focus();}},'copy-work'),
    action('Download text',()=>{try{downloadText(representation(c,s,model.predicates(s).COMPLETE),'market-participation-improvement-note.txt');announce.textContent='Text download prepared. Check your browser downloads.';}catch{output.textContent=representation(c,s,model.predicates(s).COMPLETE);output.hidden=false;announce.textContent='Download unavailable. Select and copy the text below.';}},'download-work'),
    action('Clear this draft',async()=>{if(!confirm('Clear this draft, including both versions, reviews and device/session copies? Other drafts are not affected.'))return;await store.clear();s=model.fresh();render();announce.textContent='Live draft cleared. Check storage status for any removal failures.';},'clear-draft')]);
  saving.append(node('h2',{text:'Keep your work'}),node('p',{text:'Refresh recovery is automatic in this active session. To keep work after closing, choose Save on this device. On a shared device, other people may see a saved draft. Browser session restoration can also retain session data; use Clear this draft when needed.'}),node('label',{for:'device-consent'},[consent,'Save on this device']),sessionReceipt,deviceReceipt,issue);
  exportArea.append(controls,output);host.append(announce,saving,exportArea);
  consent.addEventListener('change',async()=>{if(consent.checked)await store.enableDevice(s);else await store.disableDevice(s);});
  function receipts(r) {
    sessionReceipt.textContent=r.session;deviceReceipt.textContent=r.device;consent.checked=r.opted;consent.disabled=Boolean(r.issue);
    issue.hidden=!r.issue;issue.replaceChildren();
    if(r.issue){issue.append(node('p',{text:r.issue}));
      const options=node('div',{class:'studio-actions'});
      const recover=fn=>{try{s=model.restore(fn());store.save(s);render();announce.textContent='Chosen work restored. Review status was recomputed.';}catch(error){announce.textContent=error.message;}};
      if(store?.hasSession())options.append(action(`Recover session version ${r.sessionVersion} as a new draft`,()=>recover(()=>store.recoverSession())));
      for(const d of r.devices||[])options.append(action(`Resume device draft ${d.id.slice(0,8)} · version ${d.stamp}`,()=>recover(()=>store.resume(d.id))));
      options.append(action('Keep current work as a new draft',()=>{if(confirm('Keep the current on-page work as a new draft? The previous session copy will be replaced; device records remain unchanged.'))recover(()=>store.keepLocal(s));}));
      options.append(action('Refresh saved-version choices',()=>store.refreshChoices()));issue.append(options);
      if(r.incompatible)options.append(action('Discard incompatible saved records',async()=>{if(confirm('Permanently discard the incompatible records identified at startup? Valid saved drafts and current on-page work are retained.'))await store.discardIncompatible();}));
    }
  }
  store=createLearningState({identity:{activityId:'GR-05',contractVersion:c.contract.version,contractRevision:c.contract.revision,caseVersion:'0.1'},validatePayload:model.validate,onReceipt:receipts});
  const recovered=store.initialize();if(recovered){s=model.restore(recovered);store.save(s);}
  reference.append(node('h2',{text:'The original and the evidence'}),node('p',{text:'Fictional training case · Jiru Amba'}),node('p',{text:c.case.brief}));
  const original=node('details',{open:''},[node('summary',{text:'Read the original note'})]);
  c.authoring.fields.forEach(f=>original.append(node('h3',{text:f.label}),node('p',{text:c.case.original_note[f.id]})));reference.append(original);
  const evidence=node('details',{open:''},[node('summary',{text:'Case evidence E01–E05'})]);
  c.case.evidence.forEach(e=>evidence.append(node('p',{id:`evidence-${e.id}`,tabindex:'-1',text:`${e.id} · ${e.text}`})));reference.append(evidence);
  const stages=c.stages.map((stage,i)=>{
    const b=action(`${i+1}. ${stage.label}`,()=>{
      if(i===2&&!s.firstReviewSnapshot)model.startFirstReview(s);else s.stage=i+1;
      save();render();
    });b.setAttribute('aria-describedby',`stage-help-${i+1}`);
    nav.append(node('div',{},[b,node('span',{id:`stage-help-${i+1}`,class:'visually-hidden',text:['Always available','Write after diagnosis','Review a structurally complete draft','Complete the first criterion review first','Revise under C01 and begin final review first'][i]})]));return b;
  });
  function save(){store.save(s);update();if(!output.hidden)output.textContent=representation(c,s,model.predicates(s).COMPLETE);}
  function update() {
    const p=model.predicates(s), available=[true,p.D||Object.values(s.draft).some(Boolean),p.A||Boolean(s.firstReviewSnapshot),p.R1&&s.challengeRevealed,p.A&&p.R1&&p.C&&s.finalReviewRevision===s.contentRevision];
    stages.forEach((b,i)=>{b.disabled=!available[i];if(s.stage===i+1)b.setAttribute('aria-current','step');else b.removeAttribute('aria-current');});
    const next=document.querySelector('#continueButton');if(next)next.disabled=!p.COMPLETE;
    const status=document.querySelector('#completionStatus');if(status)status.textContent=p.COMPLETE?'Reviewed training draft. You can continue or revise.':'Complete the repair, reviews and final acknowledgment.';
    const stale='Current work needs review before Continue can enable. Your first reviewed draft is preserved.';
    if(s.finalReviewRevision===null && s.firstReviewSnapshot && announce.textContent!==stale)announce.textContent=stale;
  }
  function checkpoint(composing){if(composing){store.save(s);const next=document.querySelector('#continueButton');if(next)next.disabled=true;}else save();}
  const edit=(kind,id,value,composing=false)=>{model.edit(s,kind,id,value);checkpoint(composing);};
  const bind=(kind,id,value)=>{model.bind(s,kind,id,value);save();};
  const reviewEdit=(which,id,key,value,composing=false)=>{model.reviewEdit(s,which,id,key,value);checkpoint(composing);};
  function showErrors(list) {
    work.querySelectorAll('[data-structure-error]').forEach(e=>{const target=document.getElementById(e.dataset.structureError);if(target){target.removeAttribute('aria-invalid');target.setAttribute('aria-describedby',(target.getAttribute('aria-describedby')||'').split(' ').filter(id=>id!==e.id).join(' '));}e.remove();});
    errors.replaceChildren(node('h3',{text:'Structure check: please revise these points'}));
    const ul=node('ul');
    function describe(e){const target=document.getElementById(e.id);if(!target)return;const id=`error-${e.id}`;if(!document.getElementById(id))target.after(node('p',{id,'data-structure-error':e.id,text:e.message}));target.setAttribute('aria-invalid','true');const refs=new Set((target.getAttribute('aria-describedby')||'').split(' ').filter(Boolean));refs.add(id);target.setAttribute('aria-describedby',[...refs].join(' '));}
    function focusError(e){let target=document.getElementById(e.id);if(!target){s.stage=e.id.startsWith('diagnosis')?1:e.id.startsWith('firstCriterionReview')?3:e.id.startsWith('finalCriterionReview')?5:s.firstReviewSnapshot?4:2;render();target=document.getElementById(e.id);}describe(e);requestAnimationFrame(()=>{target?.focus();target?.scrollIntoView({block:'center',behavior:'auto'});});}
    list.forEach(e=>{describe(e);const a=node('a',{href:`#${e.id}`,text:e.message});a.addEventListener('click',event=>{event.preventDefault();focusError(e);});ul.append(node('li',{},[a]));});
    if(!list.length)ul.append(node('li',{text:'Review the diagnosis, draft and current revision before continuing.'}));
    errors.append(ul);errors.hidden=false;if(list.length)focusError(list[0]);else errors.focus();
  }
  function render() {
    work.replaceChildren();errors.hidden=true;
    const title=node('h2',{id:'stage-title',tabindex:'-1',text:`${s.stage}. ${c.stages[s.stage-1].label}`});work.append(title,errors);
    if(s.stage===1){work.append(node('p',{text:'Explain a weakness in each original section. Link your diagnosis to evidence; a clear short phrase is enough.'}),diagnosis(c,s,edit,bind),primary('Write the repair',()=>{if(!model.predicates(s).D)return showErrors(model.errors(s,'diagnosis'));s.stage=2;save();render();},'to-draft'));}
    if(s.stage===2){work.append(node('p',{text:'Write your own four-section improvement. No prepared answer or automatic grade will replace your reasoning.'}),draft(c,s,edit,bind),primary('Review draft 1',()=>{if(!model.startFirstReview(s))return showErrors(model.errors(s,'draft'));save();render();},'review-first'));}
    if(s.stage===3){work.append(node('p',{text:'Structure checked. This first reviewed draft is now preserved. Compare the original with your work, then record your criterion review.'}),comparison(c,c.case.original_note,s.firstReviewSnapshot.draft,'Original','Draft 1 — preserved'),rubric(c,s.firstCriterionReview,'firstCriterionReview',reviewEdit),primary('Apply the feasibility constraint',()=>{if(!model.challenge(s))return showErrors(model.errors(s,'firstCriterionReview'));save();render();},'to-challenge'));}
    if(s.stage===4){work.append(node('aside',{class:'studio-challenge'},[node('h3',{text:'C01 · A feasibility constraint'}),node('p',{text:c.case.challenge.text})]),draft(c,s,edit,bind),writingField({id:'revision-note',label:'Explain your connected revision',value:s.revisionNote,max:70,hint:c.authoring.revision_note.prompt+' '+c.authoring.revision_note.soft_guidance,onInput:(v,composing)=>edit('revision','',v,composing)}),primary('Compare and review this version',()=>{if(!model.startFinalReview(s))return showErrors([...(!model.predicates(s).D?model.errors(s,'diagnosis'):[]),...model.errors(s,'revision')]);save();render();},'review-final'));}
    if(s.stage===5){work.append(node('p',{text:'Structure checked. Compare your preserved first draft with the current version. Review each criterion again; unresolved points can remain as explicit follow-up.'}),comparison(c,s.firstReviewSnapshot.draft,s.draft,'Draft 1 — preserved','Current draft'),rubric(c,s.finalCriterionReview,'finalCriterionReview',reviewEdit),node('p',{text:c.output.quality_label}),primary('Acknowledge this reviewed package',()=>{if(!model.acknowledge(s))return showErrors(model.errors(s,'finalCriterionReview'));save();announce.textContent='Current package acknowledged. Continue is enabled. This is a reviewed training draft, not approval for real-world use.';},'acknowledge'),action('Revise this draft',()=>{model.revise(s);save();render();},'revise'));}
    update();requestAnimationFrame(()=>{title.focus({preventScroll:true});title.scrollIntoView({block:'start',behavior:'auto'});});
  }
  render();
}
