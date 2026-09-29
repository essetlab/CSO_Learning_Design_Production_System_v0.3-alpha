"""Materialize the frozen GR-05 case; learner logic remains in shared objects."""
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'prototype-specs/GR-05_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json').read_text(encoding='utf-8'))
folder=ROOT/'golden-references/GR-05'
folder.mkdir(exist_ok=True)
styles=['tokens/tokens.css','foundations/base.css','foundations/accessibility.css','foundations/motion.css','shell/course-shell.css','ui/button/button.css','ui/status/status.css','ui/save-state/save-state.css','learning-blocks/work-artifact/work-artifact.css','compositions/repair-studio/repair-studio.css']
links='\n'.join(f'  <link rel="stylesheet" href="../../{s}">' for s in styles)
fallback=html.escape(c['case']['brief'])
original=''.join(f'<h3>{html.escape(f["label"])}</h3><p>{html.escape(c["case"]["original_note"][f["id"]])}</p>' for f in c['authoring']['fields'])
page=f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <title>GR-05 Â· Deep Build / Repair Studio</title>
{links}
</head>
<body>
  <div data-cso-shell data-variant="standard" data-skip-label="Skip to learning content" data-course-title="Human Rights-Based Approach in CSO Practice" data-course-context="Deep Build / Repair Studio" data-progress-label="Practice workspace" data-progress-percent="0" data-drawer-eyebrow="HRBA COURSE"></div>
  <template data-shell-menu><a href="#main">Repair workspace</a></template>
  <main id="main" class="repair-studio" tabindex="-1">
    <header class="studio-header"><p class="studio-eyebrow">DEEP BUILD / REPAIR STUDIO</p><h1>Repair the market participation plan</h1><p>Diagnose the evidence, write an improvement, then revise it under a practical constraint. Keep your two versions and explain your decisions.</p><p>Fictional training case Â· approximately 25â€“35 minutes. Use short phrases where they communicate your reasoning. This workspace checks structure; you review quality.</p></header>
    <noscript><h2>Interactive workspace unavailable</h2><p>JavaScript is required for draft recovery and review. No completion is recorded here.</p><p>{fallback}</p><h2>The original note</h2>{original}<p><a href="exercise.txt">Read the exercise as plain text</a> and retain your work in your own document.</p></noscript>
    <div data-repair-workspace></div>
  </main>
  <div data-cso-learning-actions data-status="Complete the repair, reviews and final acknowledgment."></div>
  <script src="../../shell/course-shell.js"></script>
  <script type="application/json" data-repair-contract>{json.dumps(c,ensure_ascii=False).replace('</','<\\/')}</script>
  <script type="module" src="../../interactions/build-repair/build-repair.js"></script>
</body>
</html>
'''
(folder/'index.html').write_text(page,encoding='utf-8')
text=[c['contract']['title'],c['case']['brief'],'ORIGINAL NOTE',*c['case']['original_note'].values(),'EVIDENCE',*[f"{e['id']}: {e['text']}" for e in c['case']['evidence']],'TASK','Diagnose each original section using 1â€“3 evidence links. Write four repaired sections; preserve a first version. Review each criterion and give reasons and follow-up actions where needed.','C01: '+c['case']['challenge']['text'],'Revise participation plus accountability or evidence. Explain the connected change. Compare both versions and review again. This text fallback does not grant completion.',*[f"{q['id']}: {q['question']} {q['guidance']}" for q in c['criteria']]]
(folder/'exercise.txt').write_text('\n\n'.join(text)+'\n',encoding='utf-8')
print('GR-05 page and text fallback materialized from frozen revision 2')
