# E2R Stock-Web v12 Residual Research — R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R7
selected_loop = 103
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_DEVICE_EXPORT_INSTALLED_BASE_REIMBURSEMENT_BRIDGE_VS_APPROVAL_AND_REIMBURSEMENT_LABEL_HIGH_MAE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 1. Selection / novelty check

C25 is a Priority 1 archetype in the v12 no-repeat index: 33 rows and 17 more rows needed to reach the 50-row practical calibration target. C25 belongs to R7 / L7_BIO_HEALTHCARE_MEDICAL. This run therefore avoids bio drug approval/trial cases and focuses only on medical device export, installed base, consumables, reimbursement, or clinical-adoption routes.

Hard-duplicate key rule used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected cases:

| case_id | symbol | name | trigger family | duplicate status | role |
|---|---:|---|---|---|---|
| C25-103-01 | 214150 | Classys | aesthetic device export / installed-base bridge | new | positive |
| C25-103-02 | 145720 | Dentium | dental implant VBP / China volume bridge | new | positive with full-window fade watch |
| C25-103-03 | 338220 | VUNO | medical-AI reimbursement/approval label without repeat revenue proof | new | counterexample / source-proxy-only |

## 2. Case studies

### 2.1 C25-103-01 — Classys (214150): aesthetic medical device export and installed-base bridge

Classys is treated as a C25 medical-device export case, not a C20 beauty-distribution case, because the economic driver is non-invasive aesthetic treatment equipment, overseas installed base, and downstream consumable/service pull-through. The external evidence quality is moderate: public secondary sources identify Classys as a South Korean medical-device company focused on non-invasive aesthetic treatment technologies and exporting to more than 60 countries. The price trigger is the 2024-05-09 breakout row in stock-web.

```text
symbol = 214150
name = Classys / 클래시스
entry_date = 2024-05-09
entry_price = 48,500
peak_date = 2024-10-21
peak_price = 62,900
trough_date = 2024-12-09
trough_price = 40,000
MFE = +29.69%
MAE = -17.53%
classification = positive_with_high_mae_watch
```

Interpretation:

```text
The market did reward the medical-device export / installed-base bridge, but it also demanded a 4B/high-MAE overlay. This is not a clean Green case unless the runner can verify repeat device sales, consumables, service revenue, and geography-specific distributor quality.
```

### 2.2 C25-103-02 — Dentium (145720): China dental implant VBP / affordability-volume bridge

Dentium is treated as a dental implant export/reimbursement-adjacent case. The direct company-specific external evidence remains weaker than ideal, but the China dental implant volume-based procurement mechanism is relevant to the sector: Reuters later described the model as lowering implant prices for end customers and boosting demand by unlocking a large patient pool. The stock-web path shows a strong 2023 positive phase, followed by a full-window fade. This makes it a useful positive-with-fade-control case rather than a simple Green.

```text
symbol = 145720
name = Dentium / 덴티움
entry_date = 2023-01-19
entry_price = 108,500
peak_date = 2023-06-02
peak_price = 185,000
trough_date = 2023-10-20
trough_price = 93,100
MFE = +70.51%
MAE = -14.19%
classification = positive_with_full_window_fade_watch
```

Interpretation:

```text
C25 should allow Stage2-Actionable / Yellow when reimbursement or procurement policy genuinely unlocks implant volume. But it should not promote to durable Green unless the runner can verify company-level ASP, unit volume, distributor inventory, and margin retention after price cuts.
```

### 2.3 C25-103-03 — VUNO (338220): medical-AI reimbursement/approval label, but high-MAE source-proxy counterexample

VUNO is included as a C25 counterexample because medical-AI / reimbursement / hospital-adoption headlines can create strong local MFE without stable commercialization proof. External source verification for the exact trigger remains source_proxy_only in this run, so the row is usable for price-path calibration and negative guardrail design, but should be repaired with a verified URL before production-weight learning.

```text
symbol = 338220
name = VUNO / 뷰노
entry_date = 2023-07-19
entry_price = 40,200
peak_date = 2023-09-07
peak_price = 69,500
trough_date = 2023-10-24
trough_price = 23,900
MFE = +72.89%
MAE = -40.55%
classification = counterexample_high_mfe_high_mae_source_proxy_only
```

Interpretation:

```text
This is exactly the failure mode C25 needs to catch: device/reimbursement/AI labels can produce a strong spike, but without reimbursement runway, hospital adoption conversion, recurring revenue, and sales-cycle proof, full-window drawdown risk is too large. This should route to 4B/local-watch unless non-price evidence confirms conversion.
```

## 3. Current calibrated profile stress test

Current profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual error found:

| case | expected current behavior | residual risk |
|---|---|---|
| Classys | Stage2-Actionable or Yellow only when export/installed-base bridge is verified | still risks over-scoring if device export is treated as generic K-beauty momentum |
| Dentium | Yellow allowed, Green blocked without ASP/unit/margin retention proof | full-window fade shows China VBP volume bridge needs margin proof |
| VUNO | local 4B / source-proxy block until verified reimbursement-to-revenue bridge | high-MFE/high-MAE makes it dangerous if reimbursement label is over-weighted |

## 4. Proposed shadow rule candidate

```text
new_axis_proposed = c25_installed_base_reimbursement_recurring_revenue_bridge_required_for_stage2_actionable_shadow_only
```

Candidate rule:

```text
For C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT:

If trigger evidence is only:
- overseas approval / registration,
- generic export headline,
- medical-AI reimbursement label,
- distributor agreement without sell-through,
- procurement/reimbursement policy without company-level margin bridge,
then cap at Stage2 / local 4B watch.

Allow Stage2-Actionable or Stage3-Yellow only if at least two of the following are verified:
1. installed base expansion or device shipment conversion,
2. recurring consumable/service revenue or repeat procedure volume,
3. reimbursement/coverage actually linked to billable procedure or hospital adoption,
4. distributor sell-through rather than channel inventory,
5. ASP/unit/margin bridge after reimbursement or procurement price change,
6. revision/OPM evidence within the next reporting window.

Stage3-Green should require:
- non-price bridge evidence,
- revision quality,
- low early MAE or controlled event-cap drawdown,
- no source_proxy_only evidence.
```

## 5. Machine-readable rows

### 5.1 case rows

```jsonl
{"row_type":"case","case_id":"C25-103-01","selected_round":"R7","selected_loop":103,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_BRIDGE","symbol":"214150","name":"클래시스","trigger_type":"aesthetic_device_export_installed_base_bridge","entry_date":"2024-05-09","entry_price":48500,"peak_date":"2024-10-21","peak_price":62900,"trough_date":"2024-12-09","trough_price":40000,"mfe_pct":29.69,"mae_pct":-17.53,"classification":"positive_with_high_mae_watch","calibration_usable":true,"source_quality":"verified_secondary_plus_stock_web"}
{"row_type":"case","case_id":"C25-103-02","selected_round":"R7","selected_loop":103,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_VBP_VOLUME_BRIDGE_MARGIN_WATCH","symbol":"145720","name":"덴티움","trigger_type":"dental_implant_vbp_volume_bridge","entry_date":"2023-01-19","entry_price":108500,"peak_date":"2023-06-02","peak_price":185000,"trough_date":"2023-10-20","trough_price":93100,"mfe_pct":70.51,"mae_pct":-14.19,"classification":"positive_with_full_window_fade_watch","calibration_usable":true,"source_quality":"sector_verified_company_bridge_needs_repair"}
{"row_type":"case","case_id":"C25-103-03","selected_round":"R7","selected_loop":103,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_LABEL_HIGH_MAE","symbol":"338220","name":"뷰노","trigger_type":"medical_ai_reimbursement_label_without_recurring_revenue_proof","entry_date":"2023-07-19","entry_price":40200,"peak_date":"2023-09-07","peak_price":69500,"trough_date":"2023-10-24","trough_price":23900,"mfe_pct":72.89,"mae_pct":-40.55,"classification":"counterexample_high_mfe_high_mae_source_proxy_only","calibration_usable":true,"source_quality":"source_proxy_only_url_repair_required"}
```

### 5.2 trigger rows

```jsonl
{"row_type":"trigger","case_id":"C25-103-01","symbol":"214150","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":48500,"trigger_family":"aesthetic_device_export_installed_base_bridge","price_path_label":"positive_high_mae_watch","mfe_pct":29.69,"mae_pct":-17.53,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214150|aesthetic_device_export_installed_base_bridge|2024-05-09"}
{"row_type":"trigger","case_id":"C25-103-02","symbol":"145720","trigger_date":"2023-01-19","entry_date":"2023-01-19","entry_price":108500,"trigger_family":"dental_implant_vbp_volume_bridge","price_path_label":"positive_with_full_window_fade_watch","mfe_pct":70.51,"mae_pct":-14.19,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|145720|dental_implant_vbp_volume_bridge|2023-01-19"}
{"row_type":"trigger","case_id":"C25-103-03","symbol":"338220","trigger_date":"2023-07-19","entry_date":"2023-07-19","entry_price":40200,"trigger_family":"medical_ai_reimbursement_label_without_recurring_revenue_proof","price_path_label":"counterexample_high_mfe_high_mae","mfe_pct":72.89,"mae_pct":-40.55,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|338220|medical_ai_reimbursement_label_without_recurring_revenue_proof|2023-07-19"}
```

### 5.3 score simulation / shadow weight rows

```jsonl
{"row_type":"score_simulation","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","case_id":"C25-103-01","current_profile_expected":"Stage2_Actionable_or_Yellow","proposed_shadow_effect":"Require installed-base or recurring revenue bridge before Green","production_scoring_changed":false}
{"row_type":"score_simulation","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","case_id":"C25-103-02","current_profile_expected":"Stage2_Actionable_or_Yellow_with_margin_watch","proposed_shadow_effect":"Require ASP/unit/margin proof after procurement/reimbursement price change","production_scoring_changed":false}
{"row_type":"score_simulation","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","case_id":"C25-103-03","current_profile_expected":"4B_or_source_proxy_block","proposed_shadow_effect":"Block source_proxy_only reimbursement labels from positive promotion","production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c25_installed_base_reimbursement_recurring_revenue_bridge_required_for_stage2_actionable_shadow_only","scope":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","suggested_direction":"new_axis_candidate","production_scoring_changed":false,"reason":"C25 price paths show that medical-device approvals, export labels, and reimbursement keywords can produce large MFE but require installed-base, recurring revenue, sell-through, reimbursement, and margin evidence to avoid high-MAE failures."}
```

## 6. Aggregate summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
verified_url_repair_needed_count = 1
```

Residual contribution:

```text
loop_contribution_label = canonical_archetype_rule_candidate
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
new_axis_proposed = c25_installed_base_reimbursement_recurring_revenue_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C25 approval/export/reimbursement-label rallies
existing_axis_weakened = null
```

## 7. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

When batching v12 residual MD files into stock_agent:
1. Parse this MD as one C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT residual file.
2. Add the three trigger rows only after duplicate-key validation.
3. Treat the VUNO row as source_proxy_only and require URL repair before production-weight learning.
4. Consider a shadow-only C25 axis named:
   c25_installed_base_reimbursement_recurring_revenue_bridge_required_for_stage2_actionable_shadow_only
5. Do not patch production scoring directly from this single MD.
6. Aggregate with other C25/C23/C24 medical-device/bio files to prevent overlap between drug approval, trial event, and device reimbursement routes.
```

## 8. Final response metadata

```text
이번 라운드: R7 / Loop 103 / L7_BIO_HEALTHCARE_MEDICAL
selected_round: R7
selected_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: MEDICAL_DEVICE_EXPORT_INSTALLED_BASE_REIMBURSEMENT_BRIDGE_VS_APPROVAL_AND_REIMBURSEMENT_LABEL_HIGH_MAE
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
diversity_score_summary: C25 Priority 1 보강 + Classys aesthetic-device export bridge / Dentium dental implant VBP volume bridge / VUNO medical-AI reimbursement-label high-MAE counterexample 분리
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C25 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c25_installed_base_reimbursement_recurring_revenue_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C25 approval/export/reimbursement-label rallies
existing_axis_weakened: null
next_recommended_archetypes: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C22_INSURANCE_RATE_CYCLE_RESERVE, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```
