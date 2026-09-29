// INT-READINESS-REVIEW-01 exclusively owns structural review state.
import {clone,normalized,sources,fingerprint} from '../../learning-blocks/assessment-bundle/assessment-bundle.js';
export function createModel(c) {
  const ids=c.criteria.map(x=>x.id), artifactIds=c.case.artifacts.map(x=>x.id);
  const emptyRow=()=>({state:'',links:[],gaps:[],priority:''});
  const fresh=()=>({schema:1,bundleVersion:1,opened:[],rows:Object.fromEntries(ids.map(id=>[id,emptyRow()])),route:'',rationale:'',next_step_note:'',revision:0,firstRecord:null,consequence:false,disposition:'',reviewed:{},currentRecord:null,compared:false,acknowledged:false,composing:[]});
  const sourceSet=s=>sources(c,s.bundleVersion);
  const token=s=>`${s.bundleVersion}:${s.revision}`;
  const textValid=(v,max,required)=>typeof v==='string' && v.length<=600 && normalized(v).split(/\s+/u).filter(Boolean).length<=max && (!required || (normalized(v).match(/[\p{L}\p{N}]/gu)||[]).length>=2);
  function rowValid(row,s) {
    if(!row || !c.mapping.states.includes(row.state) || !Array.isArray(row.links) || row.links.length>4 || !Array.isArray(row.gaps) || row.gaps.length>3 || new Set(row.gaps).size!==row.gaps.length || row.gaps.some(g=>!c.mapping.gap_markers.includes(g))) return false;
    if(row.gaps.length && !c.mapping.gap_priority.includes(row.priority))return false;
    if(new Set(row.links.map(l=>l.id)).size!==row.links.length || row.links.some(l=>!c.mapping.link_roles.includes(l.role)||!sourceSet(s).some(a=>a.id===l.id&&a.version===l.version)))return false;
    const support=row.links.some(l=>l.role==='supports'),limit=row.links.some(l=>l.role==='limits_or_contradicts');
    return row.state==='sufficient'?support:row.gaps.length>0 && (row.state==='missing'?!support:row.state==='insufficient'?row.links.length>0:support&&limit);
  }
  const semanticDraft=s=>JSON.stringify({rows:ids.map(id=>({...s.rows[id],gaps:[...s.rows[id].gaps].sort(),links:s.rows[id].links.map(({id,role})=>({id,role})).sort((a,b)=>a.id.localeCompare(b.id))})),route:s.route,rationale:normalized(s.rationale),next_step_note:normalized(s.next_step_note)});
  function snapshot(s) {return {bundleVersion:s.bundleVersion,revision:s.revision,sources:sourceSet(s).map(a=>({id:a.id,version:a.version,fingerprint:fingerprint(a)})),rows:clone(s.rows),route:s.route,rationale:s.rationale,next_step_note:s.next_step_note,disposition:s.disposition};}
  const comparable=record=>({...record,rationale:normalized(record.rationale),next_step_note:normalized(record.next_step_note)});
  const sameRecord=(record,s)=>record&&JSON.stringify(comparable(record))===JSON.stringify(comparable(snapshot(s)));
  function predicates(s) {
    const E=sourceSet(s).every(a=>s.opened.includes(`${a.id}:${a.version}`));
    const M=ids.every(id=>rowValid(s.rows[id],s))&&new Set(ids.flatMap(id=>s.rows[id].links.map(l=>l.id))).size>=2;
    const required=s.route!=='proceed'||ids.some(id=>s.rows[id].gaps.length||s.rows[id].state!=='sufficient');
    const J=c.decision_routes.some(r=>r.id===s.route)&&textValid(s.rationale,45,true)&&textValid(s.next_step_note,35,required)&&!s.composing.length;
    const C=!!s.firstRecord&&s.consequence===true,U=s.bundleVersion===2;
    const disposition=s.disposition==='retain_recommendation'||(s.disposition==='amend_recommendation'&&s.firstRecord&&semanticDraft(s)!==semanticDraft(s.firstRecord));
    const R=!!(E&&M&&J&&C&&U&&disposition&&ids.every(id=>s.reviewed[id]===token(s))&&sameRecord(s.currentRecord,s)&&s.compared);
    const F=R&&s.acknowledged===true;
    return {E,M,J,C,U,R,F,complete:!!(E&&M&&J&&C&&U&&R&&F)};
  }
  function invalidate(s) {s.revision++;s.reviewed={};s.currentRecord=null;s.compared=false;s.acknowledged=false;}
  function act(input,event) {
    const s=clone(input),p=predicates(s);
    switch(event.type) {
      case 'inspect': {const a=sourceSet(s).find(a=>a.id===event.id);if(a&&!s.opened.includes(`${a.id}:${a.version}`))s.opened.push(`${a.id}:${a.version}`);break;}
      case 'row': if(ids.includes(event.id)&&JSON.stringify(s.rows[event.id])!==JSON.stringify(event.value)){s.rows[event.id]=clone(event.value);invalidate(s);}break;
      case 'edit': if(['route','rationale','next_step_note','disposition'].includes(event.field)&&typeof event.value==='string'){if(normalized(s[event.field])!==normalized(event.value))invalidate(s);s[event.field]=event.value;}break;
      case 'composition': s.composing=event.active?[...new Set([...s.composing,event.field])]:s.composing.filter(f=>f!==event.field);if(event.active){s.currentRecord=null;s.compared=false;s.acknowledged=false;}break;
      case 'initial': if(p.E&&p.M&&p.J&&!s.firstRecord)s.firstRecord=snapshot(s);break;
      case 'consequence': if(s.firstRecord)s.consequence=true;break;
      case 'clarify': if(p.C&&s.bundleVersion===1){s.bundleVersion=2;invalidate(s);}break;
      case 'confirm': if(s.bundleVersion===2&&ids.includes(event.id)&&rowValid(s.rows[event.id],s))s.reviewed[event.id]=token(s);break;
      case 'review': if(p.E&&p.M&&p.J&&p.C&&p.U&&ids.every(id=>s.reviewed[id]===token(s))&&(s.disposition==='retain_recommendation'||s.disposition==='amend_recommendation'&&semanticDraft(s)!==semanticDraft(s.firstRecord))) {s.currentRecord=snapshot(s);s.compared=false;s.acknowledged=false;}break;
      case 'compare': if(sameRecord(s.currentRecord,s))s.compared=true;break;
      case 'acknowledge': if(p.R)s.acknowledged=true;break;
      case 'revise': invalidate(s);break;
      default: break;
    }
    return s;
  }
  function validate(s) {
    try {
      if(!s||Object.keys(s).sort().join()!==Object.keys(fresh()).sort().join()||s.schema!==1||![1,2].includes(s.bundleVersion)||!Number.isSafeInteger(s.revision)||s.revision<0)return false;
      if(!Array.isArray(s.opened)||new Set(s.opened).size!==s.opened.length||s.opened.some(t=>!c.case.artifacts.some(a=>t===`${a.id}:1`)&&t!==`${c.case.update.replaces_id}:2`))return false;
      if(!Array.isArray(s.composing)||s.composing.some(f=>!['rationale','next_step_note'].includes(f))||!['consequence','compared','acknowledged'].every(k=>typeof s[k]==='boolean'))return false;
      if(!['route','rationale','next_step_note','disposition'].every(k=>typeof s[k]==='string')||s.route&&!c.decision_routes.some(r=>r.id===s.route)||s.disposition&&!c.feedback.challenge_options.includes(s.disposition))return false;
      const shapeRows=rows=>rows&&Object.keys(rows).sort().join()===ids.slice().sort().join()&&ids.every(id=>{
        const r=rows[id];return r&&Object.keys(r).sort().join()==='gaps,links,priority,state'&&['',...c.mapping.states].includes(r.state)&&['',...c.mapping.gap_priority].includes(r.priority)&&Array.isArray(r.gaps)&&r.gaps.length<=3&&new Set(r.gaps).size===r.gaps.length&&r.gaps.every(g=>c.mapping.gap_markers.includes(g))&&Array.isArray(r.links)&&r.links.length<=4&&new Set(r.links.map(l=>l.id)).size===r.links.length&&r.links.every(l=>Object.keys(l).sort().join()==='id,role,version'&&artifactIds.includes(l.id)&&c.mapping.link_roles.includes(l.role)&&(l.version===1||l.id===c.case.update.replaces_id&&l.version===2));
      });
      if(!shapeRows(s.rows)||!s.reviewed||typeof s.reviewed!=='object'||Object.keys(s.reviewed).some(id=>!ids.includes(id)||s.reviewed[id]!==token(s)))return false;
      const validSnapshot=(record,version)=>{
        if(!record||record.bundleVersion!==version||!Number.isSafeInteger(record.revision)||record.revision>s.revision||record.revision<0||!shapeRows(record.rows))return false;
        const probe={...fresh(),...record,opened:sources(c,version).map(a=>`${a.id}:${a.version}`)};
        return JSON.stringify(record)===JSON.stringify(snapshot(probe))&&predicates(probe).M&&predicates(probe).J;
      };
      if(s.firstRecord&&!validSnapshot(s.firstRecord,1))return false;
      if(s.bundleVersion===2&&(!s.firstRecord||!s.consequence)||s.consequence&&!s.firstRecord)return false;
      if(s.currentRecord&&(!validSnapshot(s.currentRecord,2)||!sameRecord(s.currentRecord,s)))return false;
      if(s.compared&&!s.currentRecord||s.acknowledged&&!predicates(s).R)return false;
      return true;
    }catch{return false;}
  }
  function restore(payload){if(!validate(payload))throw Error('Incompatible or corrupt Track A work; no restoration performed.');const s=clone(payload);s.composing=[];return s;}
  return {fresh,act,predicates,validate,restore,sourceSet,rowValid,textValid,snapshot};
}
