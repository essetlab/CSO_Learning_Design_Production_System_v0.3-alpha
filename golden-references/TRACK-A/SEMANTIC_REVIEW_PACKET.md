# Track A independent semantic-review packet

**PENDING — H01–H10 independent human judgment.**

Synthetic semantic-review evidence only. These are the exact approved specification fixtures, not model answers, learner-visible prepared answers, real plans or independent competence evidence.

Track A is an assessment/readiness rehearsal, not an independent competence-certification system. The learner/reviewer produces a readiness recommendation against transparent criteria. Runtime structural completion, route selection or deterministic feedback must never be represented as independent professional competence judgment, certification, organizational authorization, public-plan approval or formal assessor decision. A simulated/deterministic reviewer may demonstrate the assessment contract only when clearly labelled as simulated.

Frozen source: `prototype-specs/TRACK_A_SEMANTIC_REVIEW_FIXTURES_v0.1.json`. SHA-256: `2e94209cb695f02b06eb7067d0a962749a9acf4b8c22d0e61399994bd2772769`.

Contract SHA-256: `e3271be534980f10e38ba1835a97f6e49291b2afdd24fc5ea09613cca56cf043`. No fixture text has been improved or rewritten. Automated trajectory execution establishes structural viability only.

## Case and bounded next step

You are practising as a peer reviewer of one fictional learner’s HRBA work about market participation in Jiru Amba. Recommend whether this work is ready for a supervised rehearsal of an accessible account-back conversation. This is not permission to collect real complaints, approve a public plan or certify the author. Review the work, its rehearsal evidence and its limits; the learner can challenge your recommendation or provide clarification.

Supervised rehearsal of an accessible account-back conversation using fictional concerns; no live implementation or public authorization.

## Exact initial evidence

### TA-E01 v1 — Repaired participation note

Fictional learner draft; self-authored plan, not observed delivery

Women vendors and persons with disabilities should influence market priorities before the planning team finalizes the plan. Offer short visits at agreed times, spoken summaries and an accessible small conversation. Record which proposal changes the draft and explain any proposal the planning team cannot take forward.

Limitation: A proposed method demonstrates planning, not successful participation or confirmed influence in practice.

### TA-E02 v1 — Observation from the practice conversation

Synthetic peer observation of a role-play, not field monitoring

In the role-play, the learner offered a spoken summary and asked the vendor role about a suitable time. A suggestion to move the practice conversation earlier was added to the draft before the mock decision. The observer did not test access with a disability role or check that an explanation reached anyone.

Limitation: One rehearsal supports a bounded capability claim. It does not establish population coverage, consistent performance or real-world receipt.

### TA-E03 v1 — Learner’s readiness claim

Synthetic self-review attached to the draft

All planned activities are complete, so the work is ready. Awra has approved the final public plan. The explanation was prepared, which means everyone received a response.

Limitation: This is the learner’s claim. Compare it with the observed rehearsal and the response check; do not treat confidence or completion as corroboration.

### TA-E04 v1 — Responsibility and response check

Synthetic tutor checklist for this practice bundle; not independent certification

The planning team holds public decision authority. Awra can support dialogue and refer concerns; it cannot approve the public plan. The rehearsal produced an explanation draft, but no delivery or receipt check is recorded. The next supervised exercise can practise accessible account-back without claiming that real concerns have been resolved.

Limitation: This checklist clarifies roles and the record’s limits. It does not prove that the learner can carry out the next step without supervision.

## Transparent criteria

### TA-K01 — Specific, accessible participation planning

Does the work connect named rights-holders, a practical access adjustment and an opportunity to influence a decision?

A specific plan plus a bounded illustration can support readiness for a supervised rehearsal, without claiming universal access or delivery.

### TA-K02 — Evidence of influence, with limits

Does the bundle show a proposal affecting a draft before a decision, and distinguish this from attendance or activity completion?

Trace a particular change to rehearsal evidence and keep its scope visible; artifact count is not sufficiency.

### TA-K03 — Responsible account-back within authority

Does the learner distinguish preparation, delivery and receipt, respect the planning team’s authority and identify a safe next account-back check?

A coherent role boundary and feasible supervised next check can support this limited next step. Actual response or public approval cannot be inferred.

## Later clarification — only after initial record and consequence inspection

TA-U01

I confused a prepared explanation with confirmed receipt. The planning team decides; Awra supports the conversation and referral. Before any real use, I will ask the planning team to check the explanation and agree a safe response route. In the next supervised rehearsal, I will use a spoken summary and check understanding with the participant role.

This correction improves the account and proposes a feasible next check. It is still self-reported intention, not proof of real delivery or receipt.

## Exact positive trajectories

### P01 — Revise then proceed only to supervised rehearsal, with unresolved real-use checks

```json

{
  "id": "P01",
  "purpose": "Revise then proceed only to supervised rehearsal, with unresolved real-use checks",
  "initial": {
    "bundle_version": 1,
    "mappings": {
      "TA-K01": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "access_not_tested"
        ],
        "gap_priority": "during_supervised_step"
      },
      "TA-K02": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E03",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "evidence_scope_limited"
        ],
        "gap_priority": "before_real_use"
      },
      "TA-K03": {
        "state": "conflicting",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E03",
            "version": 1,
            "role": "limits_or_contradicts"
          },
          {
            "artifact_id": "TA-E04",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "claim_conflicts_with_record",
          "receipt_unverified"
        ],
        "gap_priority": "before_next_step"
      }
    },
    "route": "revise",
    "rationale": "The rehearsal shows a specific influence on timing, but the self-review overclaims receipt and public approval. Correct those claims before the next supervised step.",
    "next_step_note": "Ask the learner to distinguish preparation from receipt and name the planning team’s authority; reconsider the corrected account with the tutor."
  },
  "current": {
    "bundle_version": 2,
    "mappings": {
      "TA-K01": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "access_not_tested"
        ],
        "gap_priority": "during_supervised_step"
      },
      "TA-K02": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "evidence_scope_limited"
        ],
        "gap_priority": "before_real_use"
      },
      "TA-K03": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E03",
            "version": 2,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E04",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "receipt_unverified"
        ],
        "gap_priority": "before_real_use"
      }
    },
    "route": "proceed",
    "rationale": "The clarification now respects authority and distinguishes preparation from receipt. Together with the rehearsal, this supports another supervised practice conversation, not unsupervised work or verified public response.",
    "next_step_note": "The tutor should test accessible explanation and understanding in the next rehearsal; verify a safe response route before any real use."
  },
  "disposition": "amend_recommendation",
  "unresolved": [
    "Disability access not rehearsed",
    "No real delivery or receipt evidence"
  ]
}

```

### P02 — Retain revise after clarification; credible not-yet without forced prose

```json

{
  "id": "P02",
  "purpose": "Retain revise after clarification; credible not-yet without forced prose",
  "initial": {
    "bundle_version": 1,
    "mappings": {
      "TA-K01": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "access_not_tested"
        ],
        "gap_priority": "during_supervised_step"
      },
      "TA-K02": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E03",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "evidence_scope_limited"
        ],
        "gap_priority": "before_real_use"
      },
      "TA-K03": {
        "state": "conflicting",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E03",
            "version": 1,
            "role": "limits_or_contradicts"
          },
          {
            "artifact_id": "TA-E04",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "claim_conflicts_with_record",
          "receipt_unverified"
        ],
        "gap_priority": "before_next_step"
      }
    },
    "route": "revise",
    "rationale": "The bundle does not yet demonstrate accessible account-back. A clear plan and a timing change are useful, but supervised evidence of explaining and checking understanding is still needed.",
    "next_step_note": "Ask the tutor to observe an accessible account-back rehearsal and review the learner’s response before judging readiness again."
  },
  "current": {
    "bundle_version": 2,
    "mappings": {
      "TA-K01": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "access_not_tested"
        ],
        "gap_priority": "during_supervised_step"
      },
      "TA-K02": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "evidence_scope_limited"
        ],
        "gap_priority": "before_real_use"
      },
      "TA-K03": {
        "state": "insufficient",
        "links": [
          {
            "artifact_id": "TA-E03",
            "version": 2,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E04",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "receipt_unverified"
        ],
        "gap_priority": "before_next_step"
      }
    },
    "route": "revise",
    "rationale": "The bundle does not yet demonstrate accessible account-back. A clear plan and a timing change are useful, but supervised evidence of explaining and checking understanding is still needed.",
    "next_step_note": "Ask the tutor to observe an accessible account-back rehearsal and review the learner’s response before judging readiness again."
  },
  "disposition": "retain_recommendation",
  "unresolved": [
    "Correction is intention, not observed account-back"
  ]
}

```

### P03 — Seek tutor review without pretending public authorization exists

```json

{
  "id": "P03",
  "purpose": "Seek tutor review without pretending public authorization exists",
  "initial": {
    "bundle_version": 1,
    "mappings": {
      "TA-K01": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "access_not_tested"
        ],
        "gap_priority": "during_supervised_step"
      },
      "TA-K02": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E03",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "evidence_scope_limited"
        ],
        "gap_priority": "before_real_use"
      },
      "TA-K03": {
        "state": "conflicting",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E03",
            "version": 1,
            "role": "limits_or_contradicts"
          },
          {
            "artifact_id": "TA-E04",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "claim_conflicts_with_record",
          "receipt_unverified"
        ],
        "gap_priority": "before_next_step"
      }
    },
    "route": "seek_review",
    "rationale": "The learner’s approval and receipt claims conflict with the role check. I can flag that boundary, but a tutor should review readiness for the supervised step.",
    "next_step_note": "Send the conflicting criterion and source versions to the tutor in a real review process; here, request the exercise clarification and retain the record."
  },
  "current": {
    "bundle_version": 2,
    "mappings": {
      "TA-K01": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "access_not_tested"
        ],
        "gap_priority": "during_supervised_step"
      },
      "TA-K02": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "evidence_scope_limited"
        ],
        "gap_priority": "before_real_use"
      },
      "TA-K03": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E03",
            "version": 2,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E04",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "receipt_unverified"
        ],
        "gap_priority": "before_real_use"
      }
    },
    "route": "seek_review",
    "rationale": "The clarification resolves the stated authority confusion, but I want tutor review of the planned understanding check before recommending the supervised step. It does not establish actual receipt.",
    "next_step_note": "Ask the tutor to review the account-back plan; the learner can prepare a fictional spoken summary while awaiting review."
  },
  "disposition": "retain_recommendation",
  "unresolved": [
    "Tutor review not actually sent or received"
  ]
}

```

### P04 — Defer with precise missing evidence and reconsideration trigger

```json

{
  "id": "P04",
  "purpose": "Defer with precise missing evidence and reconsideration trigger",
  "initial": {
    "bundle_version": 1,
    "mappings": {
      "TA-K01": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "access_not_tested"
        ],
        "gap_priority": "during_supervised_step"
      },
      "TA-K02": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E03",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "evidence_scope_limited"
        ],
        "gap_priority": "before_real_use"
      },
      "TA-K03": {
        "state": "missing",
        "links": [
          {
            "artifact_id": "TA-E04",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "receipt_unverified"
        ],
        "gap_priority": "before_next_step"
      }
    },
    "route": "defer",
    "rationale": "I need evidence of how the learner explains a response and checks understanding before recommending this next step. The current record documents preparation rather than that performance.",
    "next_step_note": "Arrange a short supervised demonstration with the tutor, then reconsider this criterion; retain the existing participation evidence."
  },
  "current": {
    "bundle_version": 2,
    "mappings": {
      "TA-K01": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E01",
            "version": 1,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "access_not_tested"
        ],
        "gap_priority": "during_supervised_step"
      },
      "TA-K02": {
        "state": "sufficient",
        "links": [
          {
            "artifact_id": "TA-E02",
            "version": 1,
            "role": "supports"
          }
        ],
        "gap_markers": [
          "evidence_scope_limited"
        ],
        "gap_priority": "before_real_use"
      },
      "TA-K03": {
        "state": "insufficient",
        "links": [
          {
            "artifact_id": "TA-E03",
            "version": 2,
            "role": "supports"
          },
          {
            "artifact_id": "TA-E04",
            "version": 1,
            "role": "limits_or_contradicts"
          }
        ],
        "gap_markers": [
          "receipt_unverified"
        ],
        "gap_priority": "before_next_step"
      }
    },
    "route": "defer",
    "rationale": "The corrected intention is relevant but does not demonstrate the explanation or understanding check. I would defer my recommendation until a short supervised demonstration is available.",
    "next_step_note": "Ask the tutor for a bounded demonstration and re-review its observation alongside this clarification."
  },
  "disposition": "retain_recommendation",
  "unresolved": [
    "Criterion evidence still insufficient for this reviewer’s recommendation"
  ]
}

```

## Exact negative counterexamples

Do not accept these simply because text and route fields are structurally valid. They are review-only negative evidence.

```json

[
  {
    "id": "N01",
    "title": "Artifact-count assessment",
    "claim": "Four documents are present, so every criterion is sufficient.",
    "dimensions": "H01,H03,H10",
    "expected_human_critique": "Reject as semantic evidence: counts do not prove capability."
  },
  {
    "id": "N02",
    "title": "Receipt and authority confusion",
    "claim": "Awra approved the plan and a drafted message proves everyone received a response.",
    "dimensions": "H02,H04,H05",
    "expected_human_critique": "Reject: directly overclaims what the supplied record establishes."
  },
  {
    "id": "N03",
    "title": "Suppressed contradiction",
    "claim": "Remove E03 and its conflicting claim from the first record so the plan looks ready.",
    "dimensions": "H02,H07",
    "expected_human_critique": "Reject: preserve historical contradictions and exact source versions."
  },
  {
    "id": "N04",
    "title": "Stale approval",
    "claim": "Keep the old acknowledged assessment active after the source version changes.",
    "dimensions": "H07,H10",
    "expected_human_critique": "Reject: current assessment invalidates, even if the chosen route remains the same."
  },
  {
    "id": "N05",
    "title": "Indefinite defer",
    "claim": "Wait until everything is perfect.",
    "dimensions": "H06,H08,H09",
    "expected_human_critique": "Reject: lacks a proportionate evidence request, owner and reconsideration trigger."
  },
  {
    "id": "N06",
    "title": "Word/keyword pseudo-grading",
    "claim": "The answer has enough words and includes rights-holder, so mark the reviewer competent.",
    "dimensions": "H03,H09,H10",
    "expected_human_critique": "Reject: structural bounds and vocabulary cannot grant competence."
  },
  {
    "id": "N07",
    "title": "Forced proceed",
    "claim": "Revise and seek review are wrong because Continue requires proceeding.",
    "dimensions": "H05,H08,H10",
    "expected_human_critique": "Reject: practice completion is independent of readiness route."
  },
  {
    "id": "N08",
    "title": "False external assessor",
    "claim": "The app says a qualified tutor approved this work although nobody reviewed it.",
    "dimensions": "H05,H10",
    "expected_human_critique": "Reject: deterministic guidance is not independent assessment."
  }
]

```

## Independent judgment form

For each dimension record PASS / REVISE / FAIL, rationale, fixture IDs, reviewer/provenance and the exact fixture hash above. Do not infer semantic PASS from runtime navigation.

### H01 — Evidence-to-criterion fit

Each link actually supports or limits its own criterion, not a convenient document count.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H02 — Contradiction and absence

Unsupported receipt/approval claims and untested access remain visible; missing is not forced into sufficient.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H03 — Quality versus completion

Four artifacts, opened sources and valid fields do not establish capability.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H04 — Uncertainty and scope

A synthetic rehearsal and clarification support only bounded claims; no population or delivery inference.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H05 — Authority

Peer practice, author self-review, tutor review, public decision authority and credentials remain distinct.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H06 — Proportionate next step

Remediation is feasible, owned and matched to the gap, with a point for reconsideration.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H07 — Version-dependent assessment

New E03 invalidates the current outcome; old reasoning is retained as history, never silently current.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H08 — Agency in not yet

Revise, defer and seek review are legitimate; work is preserved and the next route is understandable.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H09 — Concise meaningful reasoning

The two brief fields explain enough without filler; structured mappings reduce burden. No generic repeated boilerplate.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.

### H10 — Honest completion and differentiation

Practice completion is not competence judgment; no keyword/minimum-word grading; experience is substantially lighter than GR05/06.

Judgment: **PENDING**. Rationale / exact fixture IDs: not yet supplied.
