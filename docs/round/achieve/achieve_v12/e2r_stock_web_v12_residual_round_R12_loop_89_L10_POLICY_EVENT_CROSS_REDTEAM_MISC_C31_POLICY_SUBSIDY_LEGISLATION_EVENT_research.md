---
artifact_type: e2r_stock_web_v12_residual_research
scheduled_round: R12
scheduled_loop: 89
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: MEDICAL_SCHOOL_QUOTA_EDUCATION_SERVICE_POLICY_EVENT_TO_REAL_REVENUE_BRIDGE
created_at: 2026-06-03
current_default_profile_proxy: e2r_2_1_stock_web_calibrated
previous_baseline_reference: e2r_2_0_baseline
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
do_not_propose_new_weight_delta: true
completed_round: R12
completed_loop: 89
next_round: R13
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
---

# E2R v12 Residual Research — R12 / loop 89

## 0. Execution frame

This run follows the v12 round scheduler after the completed `R11 / loop 89` artifact. The next slot is therefore:

```text
scheduled_round = R12
scheduled_loop  = 89
```

R12 allows a policy/event axis. I selected:

```text
large_sector_id          = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id   = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id        = MEDICAL_SCHOOL_QUOTA_EDUCATION_SERVICE_POLICY_EVENT_TO_REAL_REVENUE_BRIDGE
```

The selected event is the Korean medical school quota expansion headline in February 2024. The policy was broad, highly visible, and immediately tradable for education-service names, but the bridge from policy headline to actual listed-company earnings was fragile. That makes it useful for C31 residual-error calibration.

## 1. No-repeat and coverage logic

No-Repeat handling:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols:

```text
100220 비상교육
215200 메가스터디교육
095720 웅진씽크빅
```

These are used as a same-archetype new-symbol expansion for the C31 policy/legislation branch. The run deliberately avoids repeating the recent R12 value-up case set and does not reuse the R11 C04 nuclear policy names.

## 2. Policy thesis and residual-error hypothesis

### Hypothesis

The old failure mode is:

```text
medical-school quota expansion headline
  -> education/private-tutoring theme recognition
  -> price spike
  -> Stage2-Actionable / Stage3-Yellow over-promotion
```

But the durable E2R bridge should be stricter:

```text
policy event
  -> addressable student/parent demand
  -> course/category fit
  -> enrollment / paid seat conversion
  -> ARPU or pricing power
  -> margin / OP / EPS bridge
  -> sustained rerating
```

Without that bridge, a theme spike should be capped as Watch, local 4B, or false-positive candidate.

## 3. Case table

| symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_price | MFE | low_date | low_price | MAE | classification |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 100220 | 비상교육 | 2024-02-06 | 2024-02-06 | 5,060 | 2024-02-21 | 8,420 | +66.40% | 2024-08-05 | 3,990 | -21.15% | positive price path, but local 4B/theme-only |
| 215200 | 메가스터디교육 | 2024-02-06 | 2024-02-06 | 63,100 | 2024-02-08 | 68,900 | +9.19% | 2024-09-23 | 42,450 | -32.73% | counterexample |
| 095720 | 웅진씽크빅 | 2024-02-06 | 2024-02-06 | 2,475 | 2024-02-21 | 2,780 | +12.32% | 2024-09-09 | 1,640 | -33.74% | hard 4C candidate |

## 4. Case notes

### 4.1 100220 비상교육 — price-positive but local 4B, not Green

`100220` is the clearest local price winner. It closed at 5,060 on 2024-02-06, then moved to a high of 8,420 on 2024-02-21. That is a strong short-term MFE.

But the later path is the key. The same stock traded down to 3,990 on 2024-08-05, which is below the event entry and far below the spike high. This means the initial policy interpretation produced a tradable dislocation, but not a stable Stage3-Green rerating.

Residual interpretation:

```text
allow: Stage2-Actionable / local 4B watch
block: Stage3-Green unless enrollment/revenue/OP bridge appears
```

### 4.2 215200 메가스터디교육 — leader name, weak policy conversion

`215200` is more directly attached to entrance education than many theme stocks. That makes it a good positive-control candidate. Yet the actual price path is weak: the 2024-02-06 entry close was 63,100, while the best nearby high was 68,900 on 2024-02-08. The later drawdown to 42,450 by 2024-09-23 dominates the small MFE.

Residual interpretation:

```text
education leader label alone is insufficient.
require actual paid enrollment / medical-track revenue contribution / margin bridge.
```

### 4.3 095720 웅진씽크빅 — broad education exposure is not enough

`095720` had only a small MFE after the policy headline, then fell sharply. From 2,475 entry close on 2024-02-06, the stock only reached 2,780 on 2024-02-21, then later traded to 1,640 on 2024-09-09.

Residual interpretation:

```text
broad learning-content exposure ≠ medical entrance demand conversion.
route to Stage4C/hard negative candidate if the policy event has no product-fit bridge.
```

## 5. Calibration implications

### 5.1 C31 branch rule candidate

Proposed shadow rule candidate:

```text
For C31 education-policy events:
    if evidence is only policy headline + sector/theme price spike:
        cap max stage at Watch or Stage2-Actionable
        require local 4B overlay after fast +30% price-only MFE
    if company-specific evidence includes:
        - named product/course fit
        - actual enrollment or paid-seat conversion
        - ARPU/pricing/mix bridge
        - margin/OP/EPS bridge
    then:
        allow Stage3-Yellow or Stage3-Green evaluation
```

### 5.2 Why this matters

This branch is not about whether the policy is real. The policy was real. The failure is that a real policy can still be too far away from listed-company earnings. In market terms, the policy is the match; E2R should ask whether there is dry wood at the company level.

## 6. Machine-readable rows

### 6.1 case rows

```jsonl
{"row_type": "case", "scheduled_round": "R12", "scheduled_loop": 89, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_SERVICE_POLICY_EVENT_TO_REAL_REVENUE_BRIDGE", "symbol": "100220", "name": "비상교육", "trigger_type": "Stage2-Actionable-Local4B-Watch", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 5060, "mfe_peak_date": "2024-02-21", "mfe_peak_price": 8420, "mfe_pct": 66.4, "mae_low_date": "2024-08-05", "mae_low_price": 3990, "mae_pct": -21.15, "peak_to_low_drawdown_pct": -52.61, "classification": "positive_price_path_but_local_4b_policy_theme_only", "calibration_usable": true, "blocked_reason": "", "residual_error": "policy headline created strong MFE but lacked durable revenue/enrollment bridge; should cap at Actionable/4B watch without segment evidence"}
{"row_type": "case", "scheduled_round": "R12", "scheduled_loop": 89, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_SERVICE_POLICY_EVENT_TO_REAL_REVENUE_BRIDGE", "symbol": "215200", "name": "메가스터디교육", "trigger_type": "Stage2-FalsePositive-Candidate", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 63100, "mfe_peak_date": "2024-02-08", "mfe_peak_price": 68900, "mfe_pct": 9.19, "mae_low_date": "2024-09-23", "mae_low_price": 42450, "mae_pct": -32.73, "peak_to_low_drawdown_pct": -38.39, "classification": "counterexample", "calibration_usable": true, "blocked_reason": "", "residual_error": "real education leader did not convert policy headline into sustained rerating without admission-volume/ASP/course-enrollment bridge"}
{"row_type": "case", "scheduled_round": "R12", "scheduled_loop": 89, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_SERVICE_POLICY_EVENT_TO_REAL_REVENUE_BRIDGE", "symbol": "095720", "name": "웅진씽크빅", "trigger_type": "Stage4C-HardNegative-Candidate", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 2475, "mfe_peak_date": "2024-02-21", "mfe_peak_price": 2780, "mfe_pct": 12.32, "mae_low_date": "2024-09-09", "mae_low_price": 1640, "mae_pct": -33.74, "peak_to_low_drawdown_pct": -41.01, "classification": "hard_4c_candidate", "calibration_usable": true, "blocked_reason": "", "residual_error": "general learning-content exposure was treated as policy beta, but customer/product fit to medical entrance demand was weak"}
```

### 6.2 trigger rows

```jsonl
{"row_type": "trigger", "trigger_family": "policy_subsidy_legislation_event", "policy_event": "medical_school_quota_expansion_2025", "event_date": "2024-02-06", "general_rule_candidate": "education-service policy headline must require channel-specific enrollment, product fit, price/seat utilization, and OP/EPS bridge before Green", "stage_router_implication": "policy-only theme pop may remain Watch/Stage2-Actionable, but Stage3-Green requires non-price conversion evidence", "do_not_propose_new_weight_delta": true}
```

### 6.3 score simulation rows

```jsonl
{"row_type": "score_simulation", "profile": "e2r_2_1_stock_web_calibrated", "case_set": "R12_loop89_C31_medical_quota_education_service", "expected_old_failure": "policy keyword and theme-price spike could over-promote education stocks to Stage2-Actionable/Yellow without revenue conversion", "shadow_rule_candidate": "C31 education-policy branch: require product-fit + enrollment/reorder/ARPU bridge; otherwise cap to Watch or local 4B after +30% price-only MFE", "production_change_now": false}
```

### 6.4 aggregate row

```json
{
  "row_type": "aggregate",
  "scheduled_round": "R12",
  "scheduled_loop": 89,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_SERVICE_POLICY_EVENT_TO_REAL_REVENUE_BRIDGE",
  "new_independent_case_count": 3,
  "same_archetype_new_symbol_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "local_4b_overlay_case_count": 1,
  "hard_4c_candidate_count": 1,
  "calibration_usable_trigger_count": 3,
  "loop_contribution_label": "residual_error_found",
  "canonical_archetype_rule_candidate": true,
  "do_not_propose_new_weight_delta": true
}
```

## 7. Deferred Coding Agent Handoff Prompt

```text
You are working in Songdaiki/stock_agent.

Apply no production scoring change immediately.

Use this artifact as a deferred calibration input:
- file: e2r_stock_web_v12_residual_round_R12_loop_89_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
- profile context: e2r_2_1_stock_web_calibrated
- canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
- fine_archetype_id: MEDICAL_SCHOOL_QUOTA_EDUCATION_SERVICE_POLICY_EVENT_TO_REAL_REVENUE_BRIDGE

Implement only after batch review:
1. Add a C31 education-policy branch guard.
2. If evidence is policy headline + education-sector label only, cap at Watch/Stage2-Actionable.
3. Require product-fit + enrollment/revenue/ARPU/margin bridge before Stage3-Yellow/Green.
4. Add local 4B overlay when price-only MFE exceeds +30% without non-price bridge.
5. Keep raw score contribution visible in debug output; do not silently suppress evidence.
6. Add these cases to calibration JSONL fixtures only after no-repeat key validation:
   - C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 100220 / Stage2-Actionable-Local4B-Watch / 2024-02-06
   - C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 215200 / Stage2-FalsePositive-Candidate / 2024-02-06
   - C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 095720 / Stage4C-HardNegative-Candidate / 2024-02-06
```

## 8. Final scheduler state

```text
completed_round = R12
completed_loop  = 89
next_round      = R13
next_loop       = 89
round_schedule_status = valid
round_sector_consistency = pass
```
