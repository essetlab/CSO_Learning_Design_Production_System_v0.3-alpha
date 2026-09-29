// BLK-ASSESSMENT-BUNDLE-01: representation only; no readiness/completion authority.
export const clone = value => structuredClone(value);
export const normalized = value => String(value).normalize('NFC').trim().replace(/\s+/gu, ' ');
export function sources(contract, version) {
  return contract.case.artifacts.map(source => {
    const u = contract.case.update;
    return version === 2 && source.id === u.replaces_id
      ? {...clone(source), version:u.replacement_version, title:u.title, text:u.text, limitation:u.limitation, source:u.provenance}
      : clone(source);
  });
}
// Full canonical source text is the fingerprint: no lossy hash or hidden authority.
export const fingerprint = source => JSON.stringify(source);
export function representation(contract, state) {
  return [contract.case.designation, contract.case.next_step,
    contract.freeze_authority.boundary,
    'Current evidence', JSON.stringify(sources(contract,state.bundleVersion),null,2),
    'Current mapping and recommendation',JSON.stringify({rows:state.rows,route:state.route,rationale:state.rationale,next_step_note:state.next_step_note},null,2),
    'Immutable initial recommendation',JSON.stringify(state.firstRecord,null,2),
    'Current reconsideration',JSON.stringify(state.currentRecord,null,2),
    'Reconsideration disposition: '+state.disposition,
    'This export is practice work, not a submission, competence judgment or authorization.'].join('\n\n');
}
