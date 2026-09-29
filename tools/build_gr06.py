"""Materialize exact frozen GR-06 content; no local learner logic or storage."""
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json').read_text(encoding='utf-8'))
folder=ROOT/'golden-references/GR-06'
folder.mkdir(exist_ok=True)
styles=['tokens/tokens.css','foundations/base.css','foundations/accessibility.css','foundations/motion.css','shell/course-shell.css','ui/button/button.css','ui/status/status.css','ui/save-state/save-state.css','learning-blocks/work-artifact/work-artifact.css','compositions/evidence-decision/source-interpretation-decision-update.css']
links='\n'.join(f'<link rel="stylesheet" href="../../{s}">' for s in styles)
encoded=json.dumps(c,ensure_ascii=False).replace('</','<\\/')
page=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><title>GR-06 · Evidence to decision</title>{links}</head>
<body><div data-cso-shell data-variant="standard" data-skip-label="Skip to learning content" data-course-title="Human Rights-Based Approach in CSO Practice" data-course-context="Evidence to decision" data-progress-label="Practice workspace" data-progress-percent="0" data-drawer-eyebrow="HRBA COURSE"></div>
<template data-shell-menu><a href="#main">Evidence workspace</a></template>
<main id="main" class="evidence-cycle" tabindex="-1"><header class="evidence-header"><p>EVIDENCE TO DECISION</p><h1>Decide what the evidence supports</h1><p>{html.escape(c['case']['brief'])}</p><p>Fictional training case · approximately 20–30 minutes. Concise phrases welcome; maxima are limits, not targets. Structure checks do not judge the quality of your reasoning.</p></header>
<noscript><h2>Interactive workspace unavailable</h2><p>JavaScript is required for recovery and review. No completion is recorded here.</p><p><a href="exercise.txt">Read the full case and exercise as plain text</a> and keep your work in your own document.</p></noscript><div data-evidence-workspace></div></main>
<div data-cso-learning-actions data-status="Complete the evidence, decision, adaptation and review."></div><script src="../../shell/course-shell.js"></script><script type="application/json" data-evidence-contract>{encoded}</script><script type="module" src="../../interactions/evidence-decision/evidence-decision.js"></script></body></html>
'''
(folder/'index.html').write_text(page,encoding='utf-8')
text=['GR-06 · SYNTHETIC TRAINING EXERCISE',c['case']['brief']]
for e in c['case']['evidence']: text.append(f"{e['id']} | {e['source']} | {e['scope']}\n{e['text']}\nLimitation: {e['limitation']}")
text += ['TASK: Write a source note for each record (30 words maximum), then a primary interpretation and an alternative or unresolved interpretation. Link informing and limiting evidence; state uncertainty. No equal likelihood is implied.', 'Choose trial, verify, retain or escalate. Write a reason, alternative, action, responsibility boundary, verification and account-back plan. Preserve this first version before reading the later update.', 'LATER UPDATE — read after preserving decision v1',c['case']['update']['text'],c['case']['update']['limitation'],'Adapt an interpretation and action, verification or account-back; link U01 and explain the change. The route may stay the same. Compare both versions and review each criterion.']
text += [q['id']+': '+q['prompt'] for q in c['authoring']['review']['criteria']]
text += ['Record addressed or needs_follow_up, a reason and any unresolved action. This text fallback does not grant completion. Retain your own document.']
(folder/'exercise.txt').write_text('\n\n'.join(text)+'\n',encoding='utf-8')
print('GR-06 exact frozen case materialized')
