// TPL-DEEP-WORKSPACE-01: arrangement and required slots only; no activity state.
import {node} from '../../learning-blocks/work-artifact/work-artifact.js';
export function arrangeWorkspace(host,configuration={}) {
  if(configuration.variant==='evidence-decision') {
    const nav=node('nav',{'aria-label':configuration.stageLabel||'Evidence and decision stages',class:'evidence-stages'});
    const reference=node('aside',{'aria-label':configuration.referenceLabel||'Evidence sources and limitations',class:'evidence-reference'});
    const work=node('section',{class:'evidence-work','aria-labelledby':'stage-title'});
    host.append(nav,node('div',{class:'cso-evidence-decision--source-interpretation-decision-update'},[reference,work]));
    return {nav,reference,work};
  }
  const nav=node('nav',{'aria-label':'Repair stages',class:'studio-stages'});
  const reference=node('aside',{class:'studio-reference','aria-label':'Original note and case evidence'});
  const work=node('section',{class:'studio-work','aria-labelledby':'stage-title'});
  host.append(nav,node('div',{class:'studio-grid'},[reference,work]));
  return {nav,reference,work};
}
