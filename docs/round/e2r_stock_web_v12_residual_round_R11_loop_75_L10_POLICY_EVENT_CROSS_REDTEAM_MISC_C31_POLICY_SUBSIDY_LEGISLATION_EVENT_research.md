# E2R Stock-Web v12 Residual Research — R11 Loop 75 / L10 / C31

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 75,
  "computed_next_round": "R12",
  "computed_next_loop": 75,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_event_bridge_guardrail",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R10 / loop 75.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 75
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1 policy-defense linkage
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
computed_next_round = R12
computed_next_loop = 75
```

R11 was routed to C31 because this is a policy-event bridge guardrail, not a normal education or consumer-sector operating-leverage round.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C31 concentration in:

```text
112610, 034020, 336260, UNKNOWN_SYMBOL, 036460
```

This run uses three different symbols:

```text
339950 / 아이비김영 / medical-school quota admission-demand lifecycle
133750 / 메가엠디 / medical-school quota education-policy proxy fade
053290 / NE능률 / broad education-policy proxy fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate.
```

## Research thesis

C31 is not “policy headline went up.”

For education-policy rows, the bridge must pass through:

```text
policy event
→ direct beneficiary mapping
→ paid enrollment / course demand
→ retention / revenue / margin bridge
→ durable rerating
```

A policy headline is a school bell.  
The investment bridge is whether students actually enroll and pay tuition.

---

## Case 1 — Policy lifecycle candidate: 339950 / 아이비김영

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is transfer/admission-course demand, paid enrollment, retention and margin bridge evidence.

```text
evidence_family = MEDICAL_SCHOOL_QUOTA_POLICY_TRANSFER_ADMISSION_PRIVATE_EDU_DEMAND_BRIDGE_CANDIDATE
case_role = policy_lifecycle_positive_with_later_4b_watch
trigger_date = 2024-02-05
entry_date = 2024-02-06
entry_price = 1,821
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv`:

```text
2024-02-06,1821,1988,1731,1750
2024-02-20,1850,2335,1808,2300
2024-02-22,2050,2665,2010,2665
2024-02-26,2555,2965,2430,2475
2024-08-05,1732,1749,1480,1600
```

### Backtest

```text
MFE_30D  = +62.82%
MAE_30D  = -6.64%
MFE_90D  = +62.82%
MAE_90D  = -7.91%
MFE_180D = +62.82%
MAE_180D = -18.73%
peak_180 = 2,965 on 2024-02-26
trough_180 = 1,480 on 2024-08-05
peak_to_later_drawdown = -50.08%
```

### Interpretation

This is the tradable lifecycle winner.  
The policy shock produced real MFE. But the post-peak drawdown says it should not be permanent Green without enrollment/revenue bridge.

Correct treatment:

```text
source repair first
possible policy lifecycle Stage2-Yellow
later local 4B if admission-demand evidence fades
```

---

## Case 2 — Counterexample / local 4B: 133750 / 메가엠디

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests medical-school quota policy proxy beta without enough paid-enrollment and margin bridge.

```text
evidence_family = MEDICAL_SCHOOL_QUOTA_POLICY_EDU_PROXY_WITH_WEAK_PAID_ENROLLMENT_MARGIN_BRIDGE
case_role = counterexample_policy_proxy_local4b
trigger_date = 2024-02-05
entry_date = 2024-02-06
entry_price = 3,515
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/133/133750/2024.csv`:

```text
2024-02-06,3515,3670,2975,2995
2024-02-20,3090,3450,3070,3325
2024-03-20,3030,3105,2855,2880
2024-08-05,2005,2035,1647,1740
2024-08-19,2435,2705,2285,2500
```

### Backtest

```text
MFE_30D  = +4.41%
MAE_30D  = -18.78%
MFE_90D  = +4.41%
MAE_90D  = -29.59%
MFE_180D = +4.41%
MAE_180D = -53.14%
peak_180 = 3,670 on 2024-02-06
trough_180 = 1,647 on 2024-08-05
peak_to_later_drawdown = -55.12%
```

### Interpretation

This is the policy-proxy failure.  
The entry gap had no durable follow-through, and MAE opened quickly.

C31 should classify this as:

```text
false Stage2 / local 4B-watch
```

unless paid enrollment, course demand and margin evidence is repaired.

---

## Case 3 — Counterexample / local 4B: 053290 / NE능률

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests broad education-policy beta without direct revenue bridge.

```text
evidence_family = MEDICAL_SCHOOL_QUOTA_POLICY_EDUCATION_THEME_WITH_WEAK_DIRECT_REVENUE_BRIDGE
case_role = counterexample_education_theme_local4b
trigger_date = 2024-02-05
entry_date = 2024-02-06
entry_price = 6,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/053/053290/2024.csv`:

```text
2024-02-06,6200,6300,5240,5240
2024-02-20,5600,5990,5600,5790
2024-03-22,5180,5220,4530,4725
2024-08-05,3390,3390,2745,2880
2024-08-19,3495,4540,3345,4380
2024-08-28,4605,5200,4345,4345
```

### Backtest

```text
MFE_30D  = +1.61%
MAE_30D  = -26.94%
MFE_90D  = +1.61%
MAE_90D  = -27.34%
MFE_180D = +1.61%
MAE_180D = -55.73%
peak_180 = 6,300 on 2024-02-06
trough_180 = 2,745 on 2024-08-05
peak_to_later_drawdown = -56.43%
```

### Interpretation

This is the broad education-theme fade.  
The later August rebound was visible, but the original February trigger should not have been durable Stage2.

Correct treatment:

```text
policy headline only
→ no direct paid-enrollment/revenue bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
stage2_required_bridge = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C31_education_policy_weight = true
do_not_treat_medical_school_quota_headline_as_Green_without_enrollment_bridge = true
do_not_convert_policy_proxy_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE
```

This fine archetype covers:

```text
1. admission/transfer education beneficiary with MFE → policy lifecycle candidate after source repair
2. medical-school quota education proxy without paid-enrollment bridge → false Stage2 / local 4B
3. broad education-policy beta without direct revenue bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE", "symbol": "339950", "company_name": "아이비김영", "round": "R11", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "case_type": "policy_subsidy_legislation_event_education_admission_policy", "positive_or_counterexample": "policy_lifecycle_positive", "best_trigger": "Stage2-PolicyLifecycle / MedicalQuotaAdmissionDemandBridgeWithLater4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 can allow a policy-event lifecycle candidate when a medical-school quota policy shock connects to transfer/admission-course demand, paid enrollment, retention and margin bridge. Ivy Kimyoung produced large MFE, but the post-peak drawdown says lifecycle local 4B is mandatory if the policy-demand bridge fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy medical-school quota, paid enrollment, admission demand, course demand, retention and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE", "symbol": "133750", "company_name": "메가엠디", "round": "R11", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "case_type": "policy_subsidy_legislation_event_education_admission_policy", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / MedicalQuotaPolicyProxyFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat medical-school quota policy education-proxy spikes as durable Stage2 unless paid enrollment, course demand, retention or margin bridge is visible. MegaMD had a small MFE and then a deep MAE/drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy medical-school quota, paid enrollment, admission demand, course demand, retention and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE", "symbol": "053290", "company_name": "NE능률", "round": "R11", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "case_type": "policy_subsidy_legislation_event_education_admission_policy", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / EducationPolicyProxyFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C31 should not treat broad education-policy beta as durable Stage2 unless the policy connects to direct product demand, paid course enrollment, channel expansion or margin bridge. NE Neungyule had only tiny MFE and then severe drawdown before later theme rebounds.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy medical-school quota, paid enrollment, admission demand, course demand, retention and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE", "case_id": "R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE", "symbol": "339950", "company_name": "아이비김영", "round": "R11", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-PolicyLifecycle / MedicalQuotaAdmissionDemandBridgeWithLater4B", "trigger_date": "2024-02-05", "entry_date": "2024-02-06", "entry_price": 1821.0, "evidence_available_at_that_date": "MEDICAL_SCHOOL_QUOTA_POLICY_TRANSFER_ADMISSION_PRIVATE_EDU_DEMAND_BRIDGE_CANDIDATE", "evidence_source": "source_proxy_manual_verification_required:IVY_KIMYOUNG_2024_MEDICAL_SCHOOL_QUOTA_TRANSFER_ADMISSION_ENROLLMENT_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "education_or_admission_proxy", "paid_enrollment_or_revenue_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "retention_or_margin_bridge_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv", "profile_path": "atlas/symbol_profiles/339/339950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 62.82, "MFE_90D_pct": 62.82, "MFE_180D_pct": 62.82, "MAE_30D_pct": -6.64, "MAE_90D_pct": -7.91, "MAE_180D_pct": -18.73, "peak_date": "2024-02-26", "peak_price": 2965.0, "drawdown_after_peak_pct": -50.08, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_education_peak_if_enrollment_or_revenue_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_enrollment_revenue_margin_or_policy_failure_break", "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when a medical-school quota policy shock connects to transfer/admission-course demand, paid enrollment, retention and margin bridge. Ivy Kimyoung produced large MFE, but the post-peak drawdown says lifecycle local 4B is mandatory if the policy-demand bridge fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_MEDICAL_SCHOOL_QUOTA_POLICY_20240206_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE", "case_id": "R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE", "symbol": "133750", "company_name": "메가엠디", "round": "R11", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / MedicalQuotaPolicyProxyFade", "trigger_date": "2024-02-05", "entry_date": "2024-02-06", "entry_price": 3515.0, "evidence_available_at_that_date": "MEDICAL_SCHOOL_QUOTA_POLICY_EDU_PROXY_WITH_WEAK_PAID_ENROLLMENT_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MEGA_MD_2024_MEDICAL_SCHOOL_QUOTA_POLICY_PAID_ENROLLMENT_COURSE_DEMAND_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "education_or_admission_proxy", "paid_enrollment_or_revenue_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "retention_or_margin_bridge_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/133/133750/2024.csv", "profile_path": "atlas/symbol_profiles/133/133750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.41, "MFE_90D_pct": 4.41, "MFE_180D_pct": 4.41, "MAE_30D_pct": -18.78, "MAE_90D_pct": -29.59, "MAE_180D_pct": -53.14, "peak_date": "2024-02-06", "peak_price": 3670.0, "drawdown_after_peak_pct": -55.12, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_education_peak_if_enrollment_or_revenue_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_enrollment_revenue_margin_or_policy_failure_break", "trigger_outcome_label": "counterexample_policy_proxy_local4b", "current_profile_verdict": "C31 should not treat medical-school quota policy education-proxy spikes as durable Stage2 unless paid enrollment, course demand, retention or margin bridge is visible. MegaMD had a small MFE and then a deep MAE/drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_MEDICAL_SCHOOL_QUOTA_POLICY_20240206_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE", "case_id": "R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE", "symbol": "053290", "company_name": "NE능률", "round": "R11", "loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|policy_event_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / EducationPolicyProxyFade", "trigger_date": "2024-02-05", "entry_date": "2024-02-06", "entry_price": 6200.0, "evidence_available_at_that_date": "MEDICAL_SCHOOL_QUOTA_POLICY_EDUCATION_THEME_WITH_WEAK_DIRECT_REVENUE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NE_NEUNGYULE_2024_MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_DIRECT_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["policy_event", "education_or_admission_proxy", "paid_enrollment_or_revenue_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "retention_or_margin_bridge_candidate"], "stage4b_evidence_fields": ["policy_proxy_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053290/2024.csv", "profile_path": "atlas/symbol_profiles/053/053290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.61, "MFE_90D_pct": 1.61, "MFE_180D_pct": 1.61, "MAE_30D_pct": -26.94, "MAE_90D_pct": -27.34, "MAE_180D_pct": -55.73, "peak_date": "2024-02-06", "peak_price": 6300.0, "drawdown_after_peak_pct": -56.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_policy_education_peak_if_enrollment_or_revenue_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_enrollment_revenue_margin_or_policy_failure_break", "trigger_outcome_label": "counterexample_education_theme_local4b", "current_profile_verdict": "C31 should not treat broad education-policy beta as durable Stage2 unless the policy connects to direct product demand, paid course enrollment, channel expansion or margin bridge. NE Neungyule had only tiny MFE and then severe drawdown before later theme rebounds.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C31_MEDICAL_SCHOOL_QUOTA_POLICY_20240206_GROUP", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE", "trigger_id": "TRG_R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE", "symbol": "339950", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "direct_revenue_bridge_score": 9, "paid_enrollment_score": 10, "retention_or_course_demand_score": 10, "margin_bridge_score": 8, "relative_strength_score": 14, "execution_risk_score": 10, "theme_proxy_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 68, "stage_label_before": "Policy lifecycle candidate after source repair", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "direct_revenue_bridge_score": 11, "paid_enrollment_score": 12, "retention_or_course_demand_score": 12, "margin_bridge_score": 10, "relative_strength_score": 12, "execution_risk_score": 11, "theme_proxy_risk_score": 13, "source_confidence_score": 2}, "weighted_score_after": 74, "stage_label_after": "Policy lifecycle Stage2-Yellow candidate after source repair + local 4B", "changed_components": ["policy_or_regulatory_score", "direct_revenue_bridge_score", "paid_enrollment_score", "execution_risk_score", "theme_proxy_risk_score"], "component_delta_explanation": "Cap education-policy proxy scores unless medical quota policy connects to paid enrollment, admission demand, retention and margin bridge.", "MFE_90D_pct": 62.82, "MAE_90D_pct": -7.91, "score_return_alignment_label": "policy_lifecycle_with_later_4b", "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when a medical-school quota policy shock connects to transfer/admission-course demand, paid enrollment, retention and margin bridge. Ivy Kimyoung produced large MFE, but the post-peak drawdown says lifecycle local 4B is mandatory if the policy-demand bridge fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE", "trigger_id": "TRG_R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE", "symbol": "133750", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "direct_revenue_bridge_score": 2, "paid_enrollment_score": 3, "retention_or_course_demand_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 19, "theme_proxy_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "direct_revenue_bridge_score": 1, "paid_enrollment_score": 1, "retention_or_course_demand_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 21, "theme_proxy_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 38, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_revenue_bridge_score", "paid_enrollment_score", "execution_risk_score", "theme_proxy_risk_score"], "component_delta_explanation": "Cap education-policy proxy scores unless medical quota policy connects to paid enrollment, admission demand, retention and margin bridge.", "MFE_90D_pct": 4.41, "MAE_90D_pct": -29.59, "score_return_alignment_label": "policy_proxy_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat medical-school quota policy education-proxy spikes as durable Stage2 unless paid enrollment, course demand, retention or margin bridge is visible. MegaMD had a small MFE and then a deep MAE/drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE", "trigger_id": "TRG_R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE", "symbol": "053290", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"policy_or_regulatory_score": 15, "direct_revenue_bridge_score": 2, "paid_enrollment_score": 3, "retention_or_course_demand_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 19, "theme_proxy_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"policy_or_regulatory_score": 9, "direct_revenue_bridge_score": 1, "paid_enrollment_score": 1, "retention_or_course_demand_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 21, "theme_proxy_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 38, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["policy_or_regulatory_score", "direct_revenue_bridge_score", "paid_enrollment_score", "execution_risk_score", "theme_proxy_risk_score"], "component_delta_explanation": "Cap education-policy proxy scores unless medical quota policy connects to paid enrollment, admission demand, retention and margin bridge.", "MFE_90D_pct": 1.61, "MAE_90D_pct": -27.34, "score_return_alignment_label": "policy_proxy_false_positive_bridge_gap", "current_profile_verdict": "C31 should not treat broad education-policy beta as durable Stage2 unless the policy connects to direct product demand, paid course enrollment, channel expansion or margin bridge. NE Neungyule had only tiny MFE and then severe drawdown before later theme rebounds."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C31 education-policy symbols outside top-covered resource/energy/policy set, +1 medical-school quota trigger family, +1 policy lifecycle MFE winner, +2 education-policy proxy local-4B counterexamples, no hard duplicate", "residual_contribution_label": "policy_event_bridge_guardrail_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "axis": "medical_school_quota_education_policy_admission_demand_bridge_vs_edu_theme_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C31 should split education policy proxy spikes from verified enrollment/revenue bridge. Stage2 requires policy event plus paid enrollment, admission/transfer demand, course retention, direct revenue or margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["339950", "133750", "053290"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "stage2_required_bridge", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C31 education-policy events need enrollment/revenue proof. Ivy Kimyoung shows a medical-school quota policy lifecycle MFE winner requiring later local 4B; MegaMD and NE Neungyule show education-policy proxy beta fading into local 4B when paid-enrollment and margin bridge are absent."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
339950:
  corporate_action_candidate_dates = 2020-10-13
  selected window = 2024-02-06~D+180
  contamination = false

133750:
  corporate_action_candidate_dates = none
  selected window = 2024-02-06~D+180
  contamination = false

053290:
  corporate_action_candidate_dates = 2007-10-19, 2007-10-31, 2009-07-17
  selected window = 2024-02-06~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C31 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C31 rule-shape discovery,
but coding-agent promotion requires non-proxy medical-school quota, paid enrollment, admission demand, course demand, retention and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C31 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
medical_school_quota_education_policy_admission_demand_bridge_vs_edu_theme_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 339950, 133750 and 053290.
4. Keep generic C31 policy-event weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - policy event is explicit,
   - direct beneficiary mapping is visible,
   - paid enrollment, admission/transfer demand, retention or revenue bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is explicitly lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is education-policy proxy beta only,
   - enrollment/revenue/margin bridge is absent or stale,
   - MAE_30D <= -20%, MAE_90D <= -20%, or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price enrollment collapse, policy reversal, course-demand failure, revenue/margin break, financing or liquidity evidence.
8. Emit before/after diagnostics and reject if verified policy beneficiary lifecycle positives are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 75
next_round = R12
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

