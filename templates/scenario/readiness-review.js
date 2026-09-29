// TPL-SCENARIO-01 opt-in readiness-review. Arrangement only; defaults untouched.
export function arrangeReadiness(host,{variant}={}) {
  if(variant!=='readiness-review')throw Error('Explicit readiness-review opt-in required.');
  const regions={};
  for(const name of ['criteria','dossier','recommendation','history','retention']) {
    const region=document.createElement('section');region.className='readiness-'+name;
    region.setAttribute('aria-label',name==='criteria'?'Criterion mapping':name);
    host.append(region);regions[name]=region;
  }
  host.classList.add('readiness-review');return regions;
}
