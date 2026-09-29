// BLK-WORK-ARTIFACT-01: text-only fields, evidence associations, comparison and export.
export function node(tag,attrs={},children=[]) {
  const el=document.createElement(tag);
  for(const [key,value] of Object.entries(attrs)){if(key==='text')el.textContent=value;else if(key==='value')el.value=value;else if(key==='checked')el.checked=value;else if(key==='class')el.className=value;else el.setAttribute(key,String(value));}
  for(const child of Array.isArray(children)?children:[children])el.append(typeof child==='string'?document.createTextNode(child):child);
  return el;
}
const wordCount = text => text.trim() ? text.trim().split(/\s+/u).length : 0;
export function writingField({id,label,value,max,hint,onInput,required=true}) {
  const area=node('textarea',{id,value,rows:4,'aria-required':String(required),'aria-describedby':`${id}-hint ${id}-count`});
  const count=node('p',{id:`${id}-count`,class:'work-meta',text:`${wordCount(value)} / ${max} words maximum · no minimum word count`});
  const fit=()=>{area.style.height='auto';area.style.height=`${area.scrollHeight+2}px`;};
  let composing=false;
  const input=()=>{fit();count.textContent=`${wordCount(area.value)} / ${max} words maximum · no minimum word count`;onInput(area.value,composing);};
  area.addEventListener('compositionstart',()=>{composing=true;onInput(area.value,true);});
  area.addEventListener('compositionend',()=>{composing=false;input();});
  area.addEventListener('input',input);
  requestAnimationFrame(fit);
  return node('div',{class:'work-field'},[node('label',{for:id,text:label}),node('p',{id:`${id}-hint`,class:'work-hint',text:hint}),area,count]);
}
export function evidencePicker(contract,id,values,onChange) {
  const box=node('fieldset',{id,tabindex:'-1',class:'work-evidence'},[node('legend',{text:'Link 1–3 evidence items'})]);
  contract.case.evidence.forEach(e=>{
    const input=node('input',{type:'checkbox',id:`${id}-${e.id}`,checked:values.includes(e.id)});
    input.addEventListener('change',()=>onChange(e.id));
    box.append(node('div',{class:'work-evidence-item'},[node('label',{for:input.id},[input,`${e.id} · ${e.text}`])]));
  });return box;
}
export function diagnosis(contract,s,edit,bind) {
  const result=node('div');
  contract.authoring.fields.forEach(f=>result.append(node('section',{class:'work-section'},[
    node('h3',{text:f.label}),node('blockquote',{text:contract.case.original_note[f.id]}),
    writingField({id:`diagnosis-${f.id}`,label:`${f.label}: what needs repair?`,value:s.diagnoses[f.id].text,max:50,hint:'Name the weakness and link it to case evidence. A concise phrase or sentence is enough.',onInput:(v,composing)=>edit('diagnosis',f.id,v,composing)}),
    evidencePicker(contract,`diagnosis-evidence-${f.id}`,s.diagnoses[f.id].evidence,e=>bind('diagnosis',f.id,e))
  ])));return result;
}
export function draft(contract,s,edit,bind) {
  const result=node('div');
  contract.authoring.fields.forEach(f=>result.append(node('section',{class:'work-section'},[
    writingField({id:`draft-${f.id}`,label:f.label,value:s.draft[f.id],max:f.max_words,hint:`${f.prompt} ${f.soft_guidance}`,onInput:(v,composing)=>edit('draft',f.id,v,composing)}),
    node('details',{},[node('summary',{text:'Read the original section'}),node('blockquote',{text:contract.case.original_note[f.id]})]),
    evidencePicker(contract,`draft-evidence-${f.id}`,s.draftEvidence[f.id],e=>bind('draft',f.id,e))
  ])));return result;
}
export function comparison(contract,before,after,beforeLabel,afterLabel) {
  const result=node('div',{class:'work-comparison'});
  contract.authoring.fields.forEach(f=>{
    const changed=before[f.id].trim().replace(/\s+/gu,' ')!==after[f.id].trim().replace(/\s+/gu,' ');
    result.append(node('section',{class:'work-section'},[node('h3',{text:f.label}),node('p',{class:'work-meta',text:changed?'Changed':'Unchanged'}),
      node('div',{class:'work-pair'},[node('div',{},[node('h4',{text:beforeLabel}),node('p',{class:'work-copy',text:before[f.id]||'Not written'})]),node('div',{},[node('h4',{text:afterLabel}),node('p',{class:'work-copy',text:after[f.id]||'Not written'})])])
    ]));
  });return result;
}
export function rubric(contract,review,which,onChange) {
  const result=node('div');
  contract.criteria.forEach(q=>{
    const id=`${which}-${q.id}`, data=review[q.id];
    const select=node('select',{id:`${id}-judgment`,'aria-required':'true'},[node('option',{value:'',text:'Choose your judgment'}),node('option',{value:'addressed',text:'Addressed in this draft'}),node('option',{value:'needs_follow_up',text:'Needs follow-up'})]); select.value=data.judgment;
    const next=writingField({id:`${id}-followUp`,label:'One next action',value:data.followUp,max:35,required:data.judgment==='needs_follow_up',hint:'Required when this criterion needs follow-up. Brief phrases are welcome.',onInput:(v,composing)=>onChange(which,q.id,'followUp',v,composing)});
    next.hidden=data.judgment!=='needs_follow_up' && wordCount(data.followUp)<=35;
    select.addEventListener('change',()=>{next.hidden=select.value!=='needs_follow_up' && wordCount(next.querySelector('textarea').value)<=35;next.querySelector('textarea').setAttribute('aria-required',String(select.value==='needs_follow_up'));onChange(which,q.id,'judgment',select.value);});
    result.append(node('section',{class:'work-section'},[node('h3',{text:`${q.id} · ${q.question}`}),node('p',{text:q.guidance}),node('label',{for:select.id,text:'Your criterion review'}),select,
      writingField({id:`${id}-reason`,label:'Why this judgment?',value:data.reason,max:35,hint:'Give a concise reason connected to your wording. This is your review, not an automatic quality grade.',onInput:(v,composing)=>onChange(which,q.id,'reason',v,composing)}),next]));
  });return result;
}
export function representation(c,s,complete) {
  const parts=[c.output.name,'FICTIONAL TRAINING CASE — '+c.case.type,c.output.quality_label];
  const add=(title,text)=>parts.push(`\n${title}\n${text}`);
  add('CASE EVIDENCE',c.case.evidence.map(e=>`${e.id}: ${e.text}`).join('\n'));
  add('ORIGINAL NOTE',c.authoring.fields.map(f=>`${f.label}: ${c.case.original_note[f.id]}`).join('\n'));
  add('CURRENT DIAGNOSIS',c.authoring.fields.map(f=>`${f.label}: ${s.diagnoses[f.id].text}\nEvidence: ${s.diagnoses[f.id].evidence.join(', ')}`).join('\n'));
  add('FROZEN DRAFT 1',s.firstReviewSnapshot?c.authoring.fields.map(f=>`${f.label}: ${s.firstReviewSnapshot.draft[f.id]}\nEvidence: ${s.firstReviewSnapshot.draftEvidence[f.id].join(', ')}\nOriginal diagnosis: ${s.firstReviewSnapshot.diagnoses[f.id].text}\nDiagnosis evidence: ${s.firstReviewSnapshot.diagnoses[f.id].evidence.join(', ')}`).join('\n'):'Not reviewed yet');
  add('CURRENT DRAFT',c.authoring.fields.map(f=>`${f.label}: ${s.draft[f.id]}\nEvidence: ${s.draftEvidence[f.id].join(', ')}`).join('\n'));
  add('V1 / CURRENT COMPARISON',s.firstReviewSnapshot?c.authoring.fields.map(f=>`${f.label}\nBefore: ${s.firstReviewSnapshot.draft[f.id]}\nAfter: ${s.draft[f.id]}\n${s.firstReviewSnapshot.draft[f.id].trim().replace(/\s+/gu,' ')===s.draft[f.id].trim().replace(/\s+/gu,' ')?'Unchanged':'Changed'}`).join('\n'):'Available after first review');
  for(const [key,label] of [['firstCriterionReview','FIRST CRITERION REVIEW'],['finalCriterionReview','FINAL CRITERION REVIEW']])add(label,c.criteria.map(q=>`${q.id}: ${s[key][q.id].judgment||'Not reviewed'}\nReason: ${s[key][q.id].reason}\nFollow-up: ${s[key][q.id].followUp}`).join('\n'));
  add('C01',s.challengeRevealed?c.case.challenge.text:'Not released yet');add('REVISION EXPLANATION',s.revisionNote);
  add('VERSIONS AND STATUS',`Contract ${c.contract.version} revision ${c.contract.revision}; case 0.1; work revision ${s.contentRevision}\n${complete?'Work cycle acknowledged':'Draft — review/acknowledgment incomplete'}`);
  return parts.join('\n');
}
