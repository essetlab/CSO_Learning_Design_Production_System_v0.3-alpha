// Narrow evidence check only. Does not replace or modify any regression fixture.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {createModel,authored,words} from '../interactions/build-repair/model.js';
const root=path.resolve(import.meta.dirname,'..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex');
const f=read('tests/gr05-v25-semantic-review-fixture.json'),old=read('tests/gr05-example-work.json'),c=read('prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json');
const checks=[],check=(name,passed,details)=>checks.push({name,passed:!!passed,...(details?{details}:{})}),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
check('fixture explicitly synthetic semantic-review evidence only',f.purpose.includes('SYNTHETIC SEMANTIC-REVIEW EVIDENCE ONLY'));
for(const key of ['diagnoses','links','draft','revision','rationale'])check('unchanged approved '+key,same(f[key],old[key]));
check('frozen case including evidence/original/C01 unchanged',same(f.case,c.case));
check('frozen criteria unchanged',same(f.criteria,c.criteria));
check('v2 is exactly existing v1 plus existing revisions',same(f.current,{...old.draft,...old.revision}));
for(const [p,h]of Object.entries(f.source_hashes))check('source hash '+p,hash(p)===h);
for(const round of ['firstCriterionReview','finalCriterionReview']){
 check(round+' has exactly Q01â€“Q04',same(Object.keys(f[round]),c.criteria.map(q=>q.id)));
 check(round+' reasons and follow-ups are distinct',new Set(Object.values(f[round]).map(x=>x.reason)).size===4&&new Set(Object.values(f[round]).map(x=>x.followUp)).size===4);
 for(const [id,row]of Object.entries(f[round]))for(const key of ['reason','followUp'])check(`${round} ${id} ${key}: T and 35-word maximum`,authored(row[key])&&words(row[key])<=35,{words:words(row[key])});
}
const m=createModel(c),s=m.fresh();
for(const field of c.authoring.fields){m.edit(s,'diagnosis',field.id,f.diagnoses[field.id]);for(const e of f.links[field.id])m.bind(s,'diagnosis',field.id,e);m.edit(s,'draft',field.id,f.draft[field.id]);for(const e of f.links[field.id])m.bind(s,'draft',field.id,e);}
check('unchanged diagnosis and draft satisfy existing bounds/T/links',m.predicates(s).A);
check('v1 review starts',m.startFirstReview(s));
function review(round){for(const [id,row]of Object.entries(f[round]))for(const [key,value]of Object.entries(row))m.reviewEdit(s,round,id,key,value);}
review('firstCriterionReview');check('first criterion round satisfies existing contract',m.predicates(s).R1);check('C01 release allowed',m.challenge(s));
for(const [id,text]of Object.entries(f.revision))m.edit(s,'draft',id,text);m.edit(s,'revision','',f.rationale);check('unchanged connected revision satisfies contract',m.predicates(s).C);check('final review starts',m.startFinalReview(s));review('finalCriterionReview');check('acknowledgment allowed',m.acknowledge(s));
check('existing completion allows unresolved follow-up',m.predicates(s).COMPLETE&&Object.values(s.finalCriterionReview).some(x=>x.judgment==='needs_follow_up'));
check('completed state remains schema-valid',m.validate(s));
const packet=fs.readFileSync(path.join(root,'golden-references/GR-05/GR-05_V25_SEMANTIC_REVIEW_PACKET.md'),'utf8');
check('packet contains exact fixture review text',Object.values(f.firstCriterionReview).concat(Object.values(f.finalCriterionReview)).every(row=>packet.includes(row.reason)&&packet.includes(row.followUp)));
check('packet includes unchanged authored artifact',Object.values(f.diagnoses).concat(Object.values(f.draft),Object.values(f.current),[f.rationale,f.case.challenge.text]).every(text=>packet.includes(text)));
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);}
const runtime=['golden-references','interactions','learning-blocks','compositions','templates','state','shell','practice','ui'].flatMap(d=>walk(path.join(root,d))).filter(p=>/\.(html|js|css|yaml|json)$/.test(p)&&!p.endsWith('GR-05_BUILD_MANIFEST.json'));
const names=['gr05-v25-semantic-review-fixture.json','GR-05_V25_SEMANTIC_REVIEW_PACKET.md'];
check('no runtime dependency on semantic fixture or packet',runtime.every(p=>!names.some(n=>fs.readFileSync(p,'utf8').includes(n))));
check('existing browser regression runners still use historical fixture only',['tests/run_gr05_browser_validation.cjs','tests/run_gr05_keyboard_resilience.cjs'].every(p=>{const t=fs.readFileSync(path.join(root,p),'utf8');return t.includes('gr05-example-work.json')&&!t.includes('gr05-v25-semantic-review-fixture');}));
const baseline=read('tests/GR05_V25_PRESERVATION_BASELINE.json').hashes;
const changed=Object.keys(baseline).filter(p=>hash(p)!==baseline[p]);check('protected production/candidates/automated evidence/historical packet unchanged',!changed.length,{files:Object.keys(baseline).length,changed});
const governed=read('tests/GR05_VALIDATION_RESULT.json');
check('governed review pass recorded',governed.final_status==='PASS_FOR_WAVE_2_SYSTEM_REVIEW');
check('V05 and V25 review passes recorded',governed.matrix.find(x=>x.id==='V05').status==='PASS_REVIEW_REPORTED'&&governed.matrix.find(x=>x.id==='V25').status==='PASS_REVIEW_REPORTED');
const result={status:checks.every(x=>x.passed)?'PASS':'FAIL',scope:'Evidence isolation, exact artifact preservation, existing structural T/maxima and completion compatibility only; no automated semantic grade or browser regression rerun.',checks};
fs.writeFileSync(path.join(root,'tests/GR05_V25_SEMANTIC_FIXTURE_CHECKS.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,checks:checks.length,failures:checks.filter(x=>!x.passed)},null,2));if(result.status==='FAIL')process.exitCode=1;
