// INT-BUILD-REPAIR-01: the only owner of activity predicates and review validity.
export const clone = value => structuredClone(value);
export const normalize = value => value.trim().replace(/\s+/gu, ' ');
export const words = value => normalize(value) ? normalize(value).split(/\s+/u).length : 0;
export const authored = value => (value.match(/[\p{L}\p{N}]/gu) || []).length >= 2;
export const reviewSignature = value => JSON.stringify(value);

export function createModel(contract) {
  const fields = contract.authoring.fields.map(f => f.id);
  const criteria = contract.criteria.map(q => q.id);
  const evidence = contract.case.evidence.map(e => e.id);
  const map = (keys, make) => Object.fromEntries(keys.map(k => [k, make(k)]));
  const blankReview = () => map(criteria, () => ({judgment:'', reason:'', followUp:''}));
  const fresh = () => ({stage:1, contentRevision:0, diagnoses:map(fields, () => ({text:'', evidence:[]})),
    draft:map(fields, () => ''), draftEvidence:map(fields, () => []), firstReviewSnapshot:null,
    firstCriterionReview:blankReview(), challengeRevealed:false, revisionNote:'',
    finalCriterionReview:blankReview(), finalReviewRevision:null, finalAcknowledgment:null});
  const textOK = (text, max) => authored(text) && words(text) <= max;
  const refsOK = ids => ids.length >= 1 && ids.length <= 3 && new Set(ids).size === ids.length && ids.every(id => evidence.includes(id));
  const reviewOK = review => criteria.every(id => {
    const q = review[id];
    return ['addressed','needs_follow_up'].includes(q.judgment) && textOK(q.reason,35) && words(q.followUp)<=35 &&
      (q.judgment !== 'needs_follow_up' || textOK(q.followUp,35));
  });
  function predicates(s) {
    const D = fields.every(id => textOK(s.diagnoses[id].text,50) && refsOK(s.diagnoses[id].evidence));
    const A = D && contract.authoring.fields.every(f => textOK(s.draft[f.id],f.max_words) && refsOK(s.draftEvidence[f.id]) && normalize(s.draft[f.id]) !== normalize(contract.case.original_note[f.id]));
    const R1 = Boolean(s.firstReviewSnapshot) && reviewOK(s.firstCriterionReview);
    const old = s.firstReviewSnapshot?.draft;
    const C = Boolean(s.challengeRevealed && old && normalize(s.draft.participation) !== normalize(old.participation) &&
      (normalize(s.draft.accountability) !== normalize(old.accountability) || normalize(s.draft.evidence) !== normalize(old.evidence)) && textOK(s.revisionNote,70));
    const R2 = s.finalReviewRevision === s.contentRevision && reviewOK(s.finalCriterionReview);
    const F = Boolean(s.finalAcknowledgment && s.finalAcknowledgment.revision === s.contentRevision && s.finalAcknowledgment.review === reviewSignature(s.finalCriterionReview));
    return {D,A,R1,C,R2,F,COMPLETE:D && A && R1 && C && R2 && F};
  }
  function invalidate(s) { s.contentRevision++; s.finalReviewRevision=null; s.finalAcknowledgment=null; }
  function edit(s, kind, id, value) {
    let previous;
    if (kind==='draft') { previous=s.draft[id]; s.draft[id]=value; }
    if (kind==='diagnosis') { previous=s.diagnoses[id].text; s.diagnoses[id].text=value; }
    if (kind==='revision') { previous=s.revisionNote; s.revisionNote=value; }
    if (typeof previous==='string' && normalize(previous)!==normalize(value)) invalidate(s);
  }
  function bind(s, kind, id, value) {
    const target = kind==='diagnosis' ? s.diagnoses[id].evidence : s.draftEvidence[id];
    const next = target.includes(value) ? target.filter(x=>x!==value) : [...target,value];
    if (kind==='diagnosis') s.diagnoses[id].evidence=next; else s.draftEvidence[id]=next;
    invalidate(s);
  }
  function reviewEdit(s, which, id, key, value) {
    s[which][id][key]=value; s.finalAcknowledgment=null;
    if (which==='firstCriterionReview' && !predicates(s).R1) s.finalReviewRevision=null;
  }
  function startFirstReview(s) {
    if (!predicates(s).A) return false;
    if (!s.firstReviewSnapshot) s.firstReviewSnapshot=clone({revision:s.contentRevision,draft:s.draft,diagnoses:s.diagnoses,draftEvidence:s.draftEvidence});
    s.stage=3; return true;
  }
  function challenge(s) { if (!predicates(s).R1) return false; s.challengeRevealed=true; s.stage=4; return true; }
  function startFinalReview(s) {
    const p=predicates(s); if (!(p.A && p.R1 && p.C)) return false;
    s.finalReviewRevision=s.contentRevision; s.finalAcknowledgment=null; s.stage=5; return true;
  }
  function acknowledge(s) {
    const p=predicates(s); if (!(p.D && p.A && p.R1 && p.C && p.R2)) return false;
    s.finalAcknowledgment={revision:s.contentRevision,review:reviewSignature(s.finalCriterionReview)}; return true;
  }
  function revise(s) { s.finalReviewRevision=null; s.finalAcknowledgment=null; s.stage=4; }

  // Strict shape validation permits unfinished and over-limit drafts but not invented state.
  const exact = (o, keys) => o && typeof o==='object' && !Array.isArray(o) && Object.keys(o).sort().join('|')===[...keys].sort().join('|');
  const strings = o => exact(o,fields) && fields.every(id=>typeof o[id]==='string');
  const refShape = a => Array.isArray(a) && a.every(x=>typeof x==='string' && evidence.includes(x)) && new Set(a).size===a.length;
  const bindings = o => exact(o,fields) && fields.every(id=>refShape(o[id]));
  const diagnosisShape = o => exact(o,fields) && fields.every(id=>exact(o[id],['text','evidence']) && typeof o[id].text==='string' && refShape(o[id].evidence));
  const reviewShape = o => exact(o,criteria) && criteria.every(id=>exact(o[id],['judgment','reason','followUp']) &&
    ['', 'addressed','needs_follow_up'].includes(o[id].judgment) && typeof o[id].reason==='string' && typeof o[id].followUp==='string');
  function validate(s) {
    if (!exact(s,Object.keys(fresh())) || !Number.isSafeInteger(s.contentRevision) || s.contentRevision<0 || !Number.isInteger(s.stage) || s.stage<1 || s.stage>5) return false;
    if (!diagnosisShape(s.diagnoses) || !strings(s.draft) || !bindings(s.draftEvidence) || !reviewShape(s.firstCriterionReview) || !reviewShape(s.finalCriterionReview) || typeof s.revisionNote!=='string' || typeof s.challengeRevealed!=='boolean') return false;
    const snap=s.firstReviewSnapshot;
    if (snap!==null && (!exact(snap,['revision','draft','diagnoses','draftEvidence']) || !Number.isSafeInteger(snap.revision) || snap.revision<0 || snap.revision>s.contentRevision || !strings(snap.draft) || !diagnosisShape(snap.diagnoses) || !bindings(snap.draftEvidence))) return false;
    if (snap && !predicates({...fresh(),draft:snap.draft,diagnoses:snap.diagnoses,draftEvidence:snap.draftEvidence}).A) return false;
    if (!snap && (s.challengeRevealed || s.finalReviewRevision!==null || s.finalAcknowledgment!==null || Object.values(s.firstCriterionReview).some(q=>q.judgment || q.reason || q.followUp))) return false;
    if (s.finalReviewRevision!==null && (!Number.isSafeInteger(s.finalReviewRevision) || s.finalReviewRevision<0 || s.finalReviewRevision>s.contentRevision)) return false;
    const ack=s.finalAcknowledgment;
    if (ack!==null && (!exact(ack,['revision','review']) || !Number.isSafeInteger(ack.revision) || ack.revision<0 || ack.revision>s.contentRevision || typeof ack.review!=='string')) return false;
    return true;
  }
  function restore(payload) {
    if (!validate(payload)) throw Error('Draft structure or snapshot is incompatible.');
    const s=clone(payload), p=predicates(s);
    if (!(p.A && p.R1 && p.C && p.R2)) { s.finalReviewRevision=null; s.finalAcknowledgment=null; }
    if (!predicates(s).F) s.finalAcknowledgment=null;
    if (s.stage>=4 && !p.R1) s.stage=3;
    if (s.stage>=3 && !s.firstReviewSnapshot) s.stage=2;
    if (s.stage===5 && !(p.A && p.R1 && p.C)) s.stage=4;
    return s;
  }
  function errors(s, phase) {
    const list=[];
    const checkText=(id,value,max,label)=>{if(!authored(value))list.push({id,message:`Add a brief note for ${label}; words or short phrases are enough.`});else if(words(value)>max)list.push({id,message:`Keep ${label} to ${max} words or fewer. Your work is retained.`});};
    if (phase==='diagnosis' || phase==='draft') fields.forEach(id=>{checkText(`diagnosis-${id}`,s.diagnoses[id].text,50,`${id} diagnosis`); if(!refsOK(s.diagnoses[id].evidence))list.push({id:`diagnosis-evidence-${id}`,message:`Link the ${id} diagnosis to 1–3 evidence items from the case.`});});
    if (phase==='draft' || phase==='revision') contract.authoring.fields.forEach(f=>{checkText(`draft-${f.id}`,s.draft[f.id],f.max_words,f.label);if(!refsOK(s.draftEvidence[f.id]))list.push({id:`draft-evidence-${f.id}`,message:`Link ${f.label} to 1–3 evidence items from the case.`});if(normalize(s.draft[f.id])===normalize(contract.case.original_note[f.id]))list.push({id:`draft-${f.id}`,message:'This section still matches the original. Write your repair before reviewing.'});});
    if (phase==='revision') {checkText('revision-note',s.revisionNote,70,'revision explanation');if(!predicates(s).C)list.push({id:'draft-participation',message:contract.structural_feedback.revision_absent});}
    if (phase==='firstCriterionReview' || phase==='finalCriterionReview') criteria.forEach(id=>{const q=s[phase][id]; if(!q.judgment)list.push({id:`${phase}-${id}-judgment`,message:`Review ${id} and explain your judgment.`});checkText(`${phase}-${id}-reason`,q.reason,35,`${id} reason`);if(q.judgment==='needs_follow_up' || words(q.followUp)>35)checkText(`${phase}-${id}-followUp`,q.followUp,35,`${id} next action`);});
    return list;
  }
  return {fresh,predicates,edit,bind,reviewEdit,startFirstReview,challenge,startFinalReview,acknowledge,revise,validate,restore,errors};
}
