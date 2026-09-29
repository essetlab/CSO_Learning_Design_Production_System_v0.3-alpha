// INT-EVIDENCE-DECISION-01 owns learning state; storage service has no learning authority.
export const clone=x=>structuredClone(x);
export const norm=x=>x.trim().replace(/\s+/gu,' ');
export const words=x=>norm(x)?norm(x).split(/\s+/u).length:0;
export const T=x=>(x.match(/[\p{L}\p{N}]/gu)||[]).length>=2;
const exact=(o,keys)=>o&&typeof o==='object'&&!Array.isArray(o)&&Object.keys(o).sort().join('|')===[...keys].sort().join('|');
export function createModel(c){
 const sourceIds=c.case.evidence.map(e=>e.id),u=c.case.update.id,roles=c.authoring.interpretations.ids,fields=c.authoring.decision.fields,qs=c.authoring.review.criteria.map(q=>q.id);
 const map=(ids,fn)=>Object.fromEntries(ids.map(id=>[id,fn()]));
 const fresh=()=>({stage:1,sourceNotes:map(sourceIds,()=>({text:'',use:''})),interpretations:map(roles,()=>({claim:'',limitation:'',confidence:'',informing:[],limiting:[]})),decision:{route:'',interpretationIds:[],...map(fields.map(f=>f.id),()=> '')},firstSnapshot:null,updateReleased:false,updateNote:'',adaptationDisposition:'',adaptationRationale:'',contentRevision:0,criterionReview:map(qs,()=>({judgment:'',reason:'',followUp:''})),reviewRevision:null,acknowledgment:null});
 const text=(v,max)=>T(v)&&words(v)<=max;
 const links=(a,ids)=>a.length>=1&&a.length<=3&&new Set(a).size===a.length&&a.every(x=>ids.includes(x));
 function predicates(s){
  const E=sourceIds.every(id=>text(s.sourceNotes[id].text,30)&&c.authoring.source_notes.required_use.includes(s.sourceNotes[id].use));
  const ids=s.updateReleased?[...sourceIds,u]:sourceIds;
  const I=roles.every(id=>{const x=s.interpretations[id];return text(x.claim,55)&&text(x.limitation,40)&&c.authoring.interpretations.confidence.includes(x.confidence)&&links(x.informing,ids)&&links(x.limiting,ids);});
  const D=E&&I&&c.authoring.decision.options.some(x=>x.id===s.decision.route)&&s.decision.interpretationIds.length===2&&new Set(s.decision.interpretationIds).size===2&&roles.every(x=>s.decision.interpretationIds.includes(x))&&fields.every(f=>text(s.decision[f.id],f.max_words));
  const old=s.firstSnapshot,U=!!old&&s.updateReleased&&text(s.updateNote,45);
  const changed=old&&roles.some(id=>['claim','limitation'].some(k=>norm(s.interpretations[id][k])!==norm(old.interpretations[id][k])));
  const action=old&&['action','verification','accountBack'].some(k=>norm(s.decision[k])!==norm(old.decision[k]));
  const disposition=old&&(s.adaptationDisposition===(old.decision.route===s.decision.route?'retain_decision':'change_decision'));
  const A=!!(U&&D&&changed&&action&&disposition&&text(s.adaptationRationale,60)&&roles.some(id=>s.interpretations[id].informing.includes(u)||s.interpretations[id].limiting.includes(u)));
  const R=s.reviewRevision===s.contentRevision&&qs.every(id=>{const q=s.criterionReview[id];return ['addressed','needs_follow_up'].includes(q.judgment)&&text(q.reason,35)&&words(q.followUp)<=35&&(q.judgment!=='needs_follow_up'||text(q.followUp,35));});
  const F=!!(s.acknowledgment&&s.acknowledgment.revision===s.contentRevision&&s.acknowledgment.signature===JSON.stringify(s.criterionReview));
  return {E,I,D,U,A,R,F,COMPLETE:E&&I&&D&&U&&A&&R&&F};
 }
 function invalidate(s){s.contentRevision++;s.reviewRevision=null;s.acknowledgment=null;}
 function edit(s,path,value){let o=s;for(const k of path.slice(0,-1))o=o[k];const k=path.at(-1),old=o[k];o[k]=value;if(norm(old)!==norm(value))invalidate(s);}
 function toggle(s,path,value){let o=s;for(const k of path.slice(0,-1))o=o[k];const k=path.at(-1);o[k]=o[k].includes(value)?o[k].filter(v=>v!==value):[...o[k],value];invalidate(s);}
 function reviewEdit(s,id,key,value){s.criterionReview[id][key]=value;s.acknowledgment=null;}
 function capture(s){if(!predicates(s).D)return false;if(!s.firstSnapshot)s.firstSnapshot=clone({sourceNotes:s.sourceNotes,interpretations:s.interpretations,decision:s.decision,revision:s.contentRevision});s.updateReleased=true;s.stage=4;return true;}
 function review(s){if(!predicates(s).A)return false;s.reviewRevision=s.contentRevision;s.acknowledgment=null;s.stage=5;return true;}
 function acknowledge(s){const p=predicates(s);if(!(p.E&&p.I&&p.D&&p.U&&p.A&&p.R))return false;s.acknowledgment={revision:s.contentRevision,signature:JSON.stringify(s.criterionReview)};return true;}
 function revise(s){s.reviewRevision=null;s.acknowledgment=null;s.stage=4;}
 const refs=(a,ids)=>Array.isArray(a)&&new Set(a).size===a.length&&a.every(x=>typeof x==='string'&&ids.includes(x));
 const sourceShape=o=>exact(o,sourceIds)&&sourceIds.every(id=>exact(o[id],['text','use'])&&typeof o[id].text==='string'&&['',...c.authoring.source_notes.required_use].includes(o[id].use));
 const interpretationShape=(o,ids)=>exact(o,roles)&&roles.every(id=>exact(o[id],['claim','limitation','confidence','informing','limiting'])&&typeof o[id].claim==='string'&&typeof o[id].limitation==='string'&&['',...c.authoring.interpretations.confidence].includes(o[id].confidence)&&refs(o[id].informing,ids)&&refs(o[id].limiting,ids));
 const decisionShape=o=>exact(o,['route','interpretationIds',...fields.map(f=>f.id)])&&['',...c.authoring.decision.options.map(x=>x.id)].includes(o.route)&&refs(o.interpretationIds,roles)&&fields.every(f=>typeof o[f.id]==='string');
 const integer=x=>Number.isSafeInteger(x)&&x>=0;
 function validate(s){
  if(!exact(s,Object.keys(fresh()))||!Number.isInteger(s.stage)||s.stage<1||s.stage>5||!integer(s.contentRevision)||typeof s.updateReleased!=='boolean')return false;
  if(!sourceShape(s.sourceNotes)||!interpretationShape(s.interpretations,s.updateReleased?[...sourceIds,u]:sourceIds)||!decisionShape(s.decision)||!['updateNote','adaptationRationale'].every(k=>typeof s[k]==='string')||!['','retain_decision','change_decision'].includes(s.adaptationDisposition))return false;
  if(!exact(s.criterionReview,qs)||!qs.every(id=>{const q=s.criterionReview[id];return exact(q,['judgment','reason','followUp'])&&['','addressed','needs_follow_up'].includes(q.judgment)&&typeof q.reason==='string'&&typeof q.followUp==='string';}))return false;
  if(s.firstSnapshot!==null){const v=s.firstSnapshot;if(!exact(v,['sourceNotes','interpretations','decision','revision'])||!integer(v.revision)||v.revision>s.contentRevision||!sourceShape(v.sourceNotes)||!interpretationShape(v.interpretations,sourceIds)||!decisionShape(v.decision))return false;if(!predicates({...fresh(),sourceNotes:v.sourceNotes,interpretations:v.interpretations,decision:v.decision}).D)return false;}
  if(s.updateReleased!==!!s.firstSnapshot)return false;
  if(!s.firstSnapshot&&(s.updateNote||s.adaptationRationale||s.adaptationDisposition||s.reviewRevision!==null||s.acknowledgment!==null||qs.some(id=>Object.values(s.criterionReview[id]).some(Boolean))))return false;
  if(s.reviewRevision!==null&&(!integer(s.reviewRevision)||s.reviewRevision>s.contentRevision))return false;
  const a=s.acknowledgment;if(a!==null&&(!exact(a,['revision','signature'])||!integer(a.revision)||a.revision>s.contentRevision||typeof a.signature!=='string'))return false;
  return true;
 }
 function restore(payload){if(!validate(payload))throw Error('Incompatible decision record or first snapshot.');const s=clone(payload),p=predicates(s);if(!p.A||s.reviewRevision!==s.contentRevision){s.reviewRevision=null;s.acknowledgment=null;}if(!predicates(s).F)s.acknowledgment=null;if(s.stage>=4&&!s.firstSnapshot)s.stage=3;if(s.stage===5&&!p.A)s.stage=4;if(s.stage===3&&!(p.E&&p.I))s.stage=p.E?2:1;if(s.stage===2&&!p.E)s.stage=1;return s;}
 function errors(s,phase){const out=[];const add=(id,message)=>out.push({id,message});const t=(id,v,max,label)=>{if(!T(v))add(id,`Add a brief note for ${label}; short phrases are enough.`);else if(words(v)>max)add(id,`Keep ${label} to ${max} words or fewer. Your text is retained.`);};
  if(['evidence','interpretation','decision','adaptation'].includes(phase))sourceIds.forEach(id=>{t(`source-${id}`,s.sourceNotes[id].text,30,id);if(!s.sourceNotes[id].use)add(`use-${id}`,`Mark how ${id} contributes.`);});
  if(['interpretation','decision','adaptation'].includes(phase))roles.forEach(id=>{const x=s.interpretations[id];t(`claim-${id}`,x.claim,55,id);t(`limitation-${id}`,x.limitation,40,`${id} limitation`);if(!x.confidence)add(`confidence-${id}`,'Choose a provisional confidence.');for(const k of ['informing','limiting'])if(!links(x[k],s.updateReleased?[...sourceIds,u]:sourceIds))add(`${k}-${id}`,`Link 1–3 ${k} evidence records for ${id}.`);});
  if(['decision','adaptation'].includes(phase)){if(!s.decision.route)add('decision-route','Choose a provisional decision route.');if(!roles.every(id=>s.decision.interpretationIds.includes(id)))add('decision-links','Connect both interpretation roles to the decision.');fields.forEach(f=>t(`decision-${f.id}`,s.decision[f.id],f.max_words,f.id));}
  if(phase==='adaptation'){t('update-note',s.updateNote,45,'U01 implication');t('adaptation-rationale',s.adaptationRationale,60,'adaptation rationale');if(!predicates(s).A)add('adaptation-disposition','Respond to U01: link it, revise an interpretation and action/verification/account-back, and mark whether the decision route changed.');}
  if(phase==='review')qs.forEach(id=>{const q=s.criterionReview[id];if(!q.judgment)add(`review-${id}-judgment`,`Review ${id}.`);t(`review-${id}-reason`,q.reason,35,`${id} reason`);if(q.judgment==='needs_follow_up'||words(q.followUp)>35)t(`review-${id}-followUp`,q.followUp,35,`${id} follow-up`);});
  return out;
 }
 return {fresh,predicates,edit,toggle,reviewEdit,capture,review,acknowledge,revise,validate,restore,errors};
}
