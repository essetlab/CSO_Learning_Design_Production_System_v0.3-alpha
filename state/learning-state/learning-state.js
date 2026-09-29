// SVC-LEARNING-STATE-01. Generic persistence only: no completion field or learning rule.
const copy = value => structuredClone(value);
const uid = () => crypto.randomUUID();
const exact = (o,keys) => o && typeof o==='object' && !Array.isArray(o) && Object.keys(o).sort().join('|')===[...keys].sort().join('|');
export function createLearningState({identity,validatePayload,onReceipt=()=>{}}) {
  const sessionKey=`cso:session:${identity.activityId}`;
  const prefix=`cso:device:${identity.activityId}:`;
  let id=uid(), writer=uid(), sequence=0, expectedDevice=null, opted=false, stopped=false, current=null;
  let sessionEnvelope=null, devices=[], issue=null, chain=Promise.resolve(), incompatible=[];
  const receipts={session:'No work checkpointed yet.',device:'Save on this device is off.',sessionRevision:null,deviceRevision:null};
  const emit=()=>onReceipt({...receipts,opted,issue,sessionVersion:sessionEnvelope?.stamp||null,incompatible:incompatible.length,devices:devices.map(x=>({id:x.draftId,stamp:x.stamp}))});
  const key=()=>prefix+id;
  function decode(raw) {
    if(raw===null)return null;
    const e=JSON.parse(raw);
    if(!exact(e,['schemaVersion','identity','draftId','writer','sequence','stamp','deviceBase','durableOptIn','payload']) || e.schemaVersion!==1 ||
      !exact(e.identity,Object.keys(identity)) || Object.keys(identity).some(k=>e.identity[k]!==identity[k]) ||
      ![e.draftId,e.writer,e.stamp].every(x=>typeof x==='string' && x.length>0) ||
      !(e.deviceBase===null || typeof e.deviceBase==='string') || !Number.isSafeInteger(e.sequence) || e.sequence<0 || typeof e.durableOptIn!=='boolean' || !validatePayload(e.payload)) throw Error('Incompatible or corrupt saved draft.');
    return e;
  }
  function readDevice() { return decode(localStorage.getItem(key())); }
  function envelope(payload) { return {schemaVersion:1,identity:copy(identity),draftId:id,writer,sequence:++sequence,stamp:uid(),deviceBase:expectedDevice,durableOptIn:opted,payload:copy(payload)}; }
  function sessionWrite(e) {
    try {sessionStorage.setItem(sessionKey,JSON.stringify(e)); sessionEnvelope=e; receipts.session='Recoverable after refresh in this session.';receipts.sessionRevision=e.stamp;}
    catch {receipts.session='Refresh recovery is unavailable. Work remains here; copy or download before leaving.';receipts.sessionRevision=null;}
  }
  function lock(task) {
    if(!navigator.locks) return Promise.reject(Error('Device saving requires browser conflict protection.'));
    return navigator.locks.request(key(),task);
  }
  function removeDevice() {
    const disk=readDevice();
    if(disk && disk.stamp!==expectedDevice)throw Error('Device version changed; removal withheld.');
    localStorage.removeItem(key());
  }
  function conflict(message) {stopped=true;issue=message;receipts.device='Device writes paused. Local work is retained.';emit();}
  function save(payload) {
    if(!validatePayload(payload))throw Error('Invalid payload supplied to shared state service.');
    current=copy(payload);
    if(stopped){receipts.session='Recovery is paused while saved versions need a decision. Copy current work before leaving.';emit();return chain;}
    const e=envelope(payload); sessionWrite(e);
    if(opted) {
      receipts.device='Device save pending; latest work is not yet confirmed on this device.';
      chain=chain.then(()=>lock(()=>{
        if(stopped || !opted || e.draftId!==id)return;
        let disk;try{disk=readDevice();}catch{conflict('The device draft is corrupt or incompatible. No record was overwritten.');return;}
        if((disk?.stamp||null)!==expectedDevice){conflict('Another version changed on this device. Choose how to recover; no silent overwrite.');return;}
        const durable={...e,deviceBase:expectedDevice,durableOptIn:true};
        localStorage.setItem(key(),JSON.stringify(durable)); expectedDevice=durable.stamp;
        receipts.device='Saved on this device.';receipts.deviceRevision=durable.stamp;
        // Preserve a newer synchronous session edit while advancing its device baseline.
        if(sessionEnvelope?.draftId===id)sessionWrite({...sessionEnvelope,deviceBase:expectedDevice,durableOptIn:true});
        if(sequence>e.sequence)receipts.device='Newer edits are awaiting device saving.';
      })).catch(()=>{receipts.device='Could not save on this device. See the separate refresh-recovery status; copy or download before closing.';receipts.deviceRevision=null;}).finally(emit);
    }
    emit();return chain;
  }
  function initialize() {
    let raw;
    try{raw=sessionStorage.getItem(sessionKey);sessionEnvelope=decode(raw);}catch{if(typeof raw==='string')incompatible.push({tier:'session',key:sessionKey,raw});stopped=true;issue='Session recovery is unavailable or its record is incompatible. Choose a saved version or explicitly start a new draft.';}
    try {
      for(let n=0;n<localStorage.length;n++) {
        const k=localStorage.key(n);if(!k?.startsWith(prefix))continue;
        try {const e=decode(localStorage.getItem(k));if(e && prefix+e.draftId===k && e.durableOptIn)devices.push(e);else throw Error();}
        catch {const raw=localStorage.getItem(k);if(typeof raw==='string')incompatible.push({tier:'device',key:k,raw});issue='A saved device record is incompatible or corrupt. It has been preserved; choose a valid version or explicitly start new.';stopped=true;}
      }
    } catch {receipts.device='Device storage is unavailable; opt-in saving may fail.';}
    if(sessionEnvelope) {
      id=sessionEnvelope.draftId; sequence=sessionEnvelope.sequence; opted=sessionEnvelope.durableOptIn; expectedDevice=sessionEnvelope.deviceBase;
      const device=devices.find(d=>d.draftId===id);
      if(opted && (device?.stamp||null)!==expectedDevice && device?.stamp!==sessionEnvelope.stamp) {issue='Session and device versions diverged. Neither version has been overwritten.';stopped=true;}
      if(!stopped){current=copy(sessionEnvelope.payload);receipts.session='Recovered work from this active session.';if(opted)receipts.device='Device saving enabled; session work restored.';emit();return copy(current);}
    }
    if(devices.length && !sessionEnvelope){issue=issue||'A device draft is available. Resume it explicitly or start a new draft.';stopped=true;}
    emit();return null;
  }
  function useEnvelope(e) {
    if(!e || !validatePayload(e.payload))throw Error('Cannot load this record.');
    id=e.draftId;sequence=e.sequence;opted=e.durableOptIn;current=copy(e.payload);
    expectedDevice=devices.find(x=>x.draftId===id)?.stamp||null;
    stopped=false;issue=null;save(current);return copy(current);
  }
  function resume(draftId) {const d=devices.find(x=>x.draftId===draftId);return useEnvelope(d);}
  function keepLocal(payload) {
    // Explicit fork: existing durable drafts remain under their own IDs.
    id=uid();sequence=0;expectedDevice=null;opted=false;stopped=false;issue=null;
    receipts.device='New draft: Save on this device is off.';save(payload);return copy(payload);
  }
  function recoverSession() {
    if(!sessionEnvelope)throw Error('No valid session version is available.');
    // Fork so a potentially corrupt/conflicting durable version is never replaced.
    return keepLocal(sessionEnvelope.payload);
  }
  async function enableDevice(payload) {opted=true;emit();await save(payload);}
  async function disableDevice(payload) {
    opted=false;
    try {await chain;await lock(removeDevice);expectedDevice=null;receipts.device='Device saving off; device copy removed.';}
    catch {receipts.device='Device saving off, but the previous device copy could not be removed.';}
    if(!stopped)sessionWrite(envelope(payload));emit();
  }
  async function clear() {
    opted=false;stopped=true;
    const failures=[];
    try{await chain;await lock(removeDevice);}catch{failures.push('device copy');}
    try{sessionStorage.removeItem(sessionKey);}catch{failures.push('session copy');}
    current=null;sessionEnvelope=null;
    id=uid();sequence=0;expectedDevice=null;stopped=false;
    issue=failures.length?`Could not remove ${failures.join(' and ')}. Old data may remain. New work uses a new draft ID.`:null;
    receipts.session='New draft; previous live work cleared.';receipts.device=failures.length?issue:'Device saving off; this draft cleared.';emit();return failures;
  }
  const changed=event=>{
    if(event.key!==key() || !opted)return;
    try{const e=decode(event.newValue);if((e?.stamp||null)!==expectedDevice)conflict('Another tab changed this device draft. Local work is retained; writes are paused.');}
    catch{conflict('Another tab wrote an incompatible device record. Writes are paused.');}
  };
  window.addEventListener('storage',changed);
  function refreshChoices() {
    devices=[];
    try{for(let n=0;n<localStorage.length;n++){const k=localStorage.key(n);if(k?.startsWith(prefix)){try{const e=decode(localStorage.getItem(k));if(e && e.durableOptIn && prefix+e.draftId===k)devices.push(e);}catch{ /* invalid record remains untouched */ }}}}catch{}
    emit();
  }
  async function discardIncompatible() {
    const remaining=[];
    for(const record of incompatible){
      try {
        const storage=record.tier==='session'?sessionStorage:localStorage;
        const remove=()=>{if(storage.getItem(record.key)!==record.raw)throw Error('Record changed.');storage.removeItem(record.key);};
        if(record.tier==='device'){
          if(!navigator.locks)throw Error('Conflict protection unavailable.');
          await navigator.locks.request(record.key,remove);
        }else remove();
      }catch{remaining.push(record);}
    }
    incompatible=remaining;
    issue=remaining.length?'Some incompatible records could not be removed or changed since inspection. They remain untouched.':'Incompatible records removed. Choose a valid saved version or keep current work as a new draft.';
    refreshChoices();return remaining.length===0;
  }
  return {initialize,save,enableDevice,disableDevice,clear,resume,keepLocal,recoverSession,refreshChoices,
    discardIncompatible,
    hasSession:()=>Boolean(sessionEnvelope),getReceipt:()=>({...receipts,opted,issue}),dispose:()=>window.removeEventListener('storage',changed)};
}

export function downloadText(text,filename) {
  const blob=new Blob([text],{type:'text/plain;charset=utf-8'}), url=URL.createObjectURL(blob);
  const link=document.createElement('a');link.href=url;link.download=filename;link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
}
export async function copyText(text) { await navigator.clipboard.writeText(text); }
