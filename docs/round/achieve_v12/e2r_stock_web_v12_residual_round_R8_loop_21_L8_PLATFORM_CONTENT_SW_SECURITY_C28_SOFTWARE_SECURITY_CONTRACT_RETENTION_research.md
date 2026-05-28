# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only
round = R8
loop = 21
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = CLOUD_ERP_CONTRACT_RETENTION_OPERATING_LEVERAGE / NAC_EDR_ZERO_TRUST_SECURITY_CONTRACT_RETENTION / SECURITY_SOFTWARE_POLITICAL_AFFINITY_FALSE_POSITIVE
output_file = e2r_stock_web_v12_residual_round_R8_loop_21_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live watchlist, not an investment recommendation, not a production scoring patch, and not an auto-trading instruction.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The loop does **not** re-prove the global Stage2 bonus or the generic Green-lateness rule. It stress-tests whether C28 needs a narrower contract-retention gate and a political/founder-affinity false-positive guard.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R8
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
loop_objective = coverage_gap_fill | residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

### Why this scope

C28 sits at the seam where software/security companies can show real structural contract-retention rerating, but the same labels can also absorb public cyber-event, election/founder-affinity, or pure price momentum. In practical scoring, that is like hearing a fire alarm in a building: it can mean a real fire, a drill, or a faulty sensor. C28 needs the detector to check for smoke, not just loudness.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were checked only for coverage and duplicate avoidance. The calibration ingest summary shows broad historical ingestion across R1-R13 and 1,376 aggregate representative trigger rows, but GitHub code search did not return an existing `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` row or the selected symbol combination (`012510`, `053800`, `263860`) in the calibration artifacts queried during this run.

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
auto_selected_coverage_gap = C28 lacks balanced positive/counterexample/4B coverage.
```

No `stock_agent/src/e2r` code was opened, inferred, or patched.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest was read before case construction.

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Manifest facts used in this loop:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

All price rows are `tradable_raw` from `atlas/ohlcv_tradable_by_symbol_year`, not adjusted close. Therefore the windows are blocked if corporate-action candidate dates overlap the 180D calibration window.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | profile caveat | selected 180D window status |
|---|---|---|---|---|
| 012510 | 더존비즈온 | atlas/symbol_profiles/012/012510.json | corporate-action candidate dates only in 2002, 2006, 2009 | clean_180D_window |
| 263860 | 지니언스 | atlas/symbol_profiles/263/263860.json | corporate-action candidate dates only in 2018 | clean_180D_window |
| 053800 | 안랩 | atlas/symbol_profiles/053/053800.json | corporate-action candidate date only in 2005 | clean_180D_window |

Each representative trigger has:

```text
entry_date in tradable shard = true
forward_180D_available_by_manifest_max_date = true
high/low/close/volume present = true
corporate_action_contaminated_180D_window = false
```

## 6. Canonical Archetype Compression Map

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
├─ CLOUD_ERP_CONTRACT_RETENTION_OPERATING_LEVERAGE
│  └─ 012510 더존비즈온: positive structural software/ERP recurring-revenue rerating
├─ NAC_EDR_ZERO_TRUST_SECURITY_CONTRACT_RETENTION
│  └─ 263860 지니언스: positive but high-MAE security software rerating
└─ SECURITY_SOFTWARE_POLITICAL_AFFINITY_FALSE_POSITIVE
   └─ 053800 안랩: political/founder-affinity false positive
```

The canonical compression point is this: C28 is **not** "any software/security stock that rises." It is a contract-retention / repeat-order / recurring-revenue archetype. Price strength is the microphone; contract retention is the singer.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | calibration_usable | is_new_independent_case | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L21_C28_012510_DUZON_CLOUD_ERP_RETENTION | 012510 | 더존비즈온 | structural_success | positive | R8L21_C28_012510_T1_STAGE2_ACTIONABLE | True | True | current_profile_correct |
| R8L21_C28_263860_GENIANS_NAC_EDR_ZERO_TRUST | 263860 | 지니언스 | high_mae_success | positive | R8L21_C28_263860_T1_STAGE2_ACTIONABLE | True | True | current_profile_4B_too_late |
| R8L21_C28_053800_AHNLAB_POLITICAL_AFFINITY_FALSE_POSITIVE | 053800 | 안랩 | price_moved_without_evidence | counterexample | R8L21_C28_053800_T1_FALSE_STAGE2 | True | True | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 3
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 6
representative_trigger_count = 3
```

Balance verdict: usable for a canonical-archetype shadow rule, not enough for a global rule. The counterexample is not a weak example: AhnLab produced very high MFE, but the evidence family was wrong. That is exactly the type of mistake a calibrated system should avoid.

## 9. Evidence Source Map

| case_id | evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence | evidence quality note |
|---|---|---|---|---|---|
| R8L21_C28_012510_DUZON_CLOUD_ERP_RETENTION | cloud ERP / enterprise software recurring-revenue route | product/business route + visible repricing | financial visibility / public multiple-source family | valuation/positioning after fast rerating | positive evidence family, but Green still needs confirmed revision/retention KPI |
| R8L21_C28_263860_GENIANS_NAC_EDR_ZERO_TRUST | NAC / EDR / zero-trust security demand | policy/customer/order-quality route + relative strength | multiple-source visibility, not full Green | small-cap overheat and post-peak drawdown | Stage2/Yellow positive; 4B overlay should arrive earlier |
| R8L21_C28_053800_AHNLAB_POLITICAL_AFFINITY_FALSE_POSITIVE | founder/political affinity route | public event + relative strength only | none | price-only blowoff / event cap | must not promote C28 positive stage without contract-retention evidence |

Evidence-source limitation: this run prioritizes stock-web OHLC validation. For Duzon and Genian, evidence families are treated as research-proxy public evidence categories rather than primary-source filing extraction. The proposed rule is therefore shadow-only and should be confirmed against primary filings/IR before production promotion.

## 10. Price Data Source Map

| symbol | shard(s) used | key rows |
|---|---|---|
| 012510 | `atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv`, `2021.csv` | entry 2020-05-07 close 95,600; peak 2020-09-08 high 136,000; 1Y drawdown low proxy 83,100 |
| 263860 | `atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv` | entry 2023-05-17 close 11,770; peak 2023-06-13 high 17,640; 180D low proxy 10,210 |
| 053800 | `atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv` | entry 2022-03-03 close 70,800; peak 2022-03-24 high 218,500; 180D low proxy 58,900 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | trigger_outcome_label | current_profile_verdict | dedupe_for_aggregate | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L21_C28_012510_T1_STAGE2_ACTIONABLE | 012510 | 더존비즈온 | Stage2-Actionable | 2020-05-07 | 2020-05-07 | 95600 | 29.18 | 42.26 | 42.26 | -5.96 | -5.96 | -5.96 | 2020-09-08 | 136000 | structural_success | current_profile_correct | True | representative |
| R8L21_C28_012510_T2_4B_OVERLAY | 012510 | 더존비즈온 | Stage4B-Overlay | 2020-09-08 | 2020-09-08 | 120000 | 13.33 | 13.33 | 13.33 | -15.42 | -18.33 | -30.75 | 2020-09-08 | 136000 | 4B_overlay_success | current_profile_4B_too_late | False | 4B_overlay_only |
| R8L21_C28_263860_T1_STAGE2_ACTIONABLE | 263860 | 지니언스 | Stage2-Actionable | 2023-05-17 | 2023-05-17 | 11770 | 49.87 | 49.87 | 49.87 | -4.59 | -9.09 | -13.25 | 2023-06-13 | 17640 | high_mae_success | current_profile_4B_too_late | True | representative |
| R8L21_C28_263860_T2_4B_OVERLAY | 263860 | 지니언스 | Stage4B-Overlay | 2023-06-13 | 2023-06-13 | 17170 | 2.74 | 2.74 | 2.74 | -35.7 | -37.68 | -40.54 | 2023-06-13 | 17640 | 4B_overlay_success | current_profile_4B_too_late | False | 4B_overlay_only |
| R8L21_C28_053800_T1_FALSE_STAGE2 | 053800 | 안랩 | False-Stage2-Actionable | 2022-03-03 | 2022-03-03 | 70800 | 208.62 | 208.62 | 208.62 | -5.65 | -5.65 | -16.81 | 2022-03-24 | 218500 | price_moved_without_evidence | current_profile_false_positive | True | representative |
| R8L21_C28_053800_T2_4B_PRICE_ONLY | 053800 | 안랩 | Stage4B-Overlay | 2022-03-23 | 2022-03-23 | 175800 | 24.29 | 24.29 | 24.29 | -46.53 | -53.92 | -66.5 | 2022-03-24 | 218500 | 4B_overlay_success | current_profile_false_positive | False | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger metrics

| trigger_id | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L21_C28_012510_T1_STAGE2_ACTIONABLE | 2020-05-07 | 95600 | 29.18 | 42.26 | 42.26 | -5.96 | -5.96 | -5.96 | 2020-09-08 | 136000 | -38.9 |
| R8L21_C28_263860_T1_STAGE2_ACTIONABLE | 2023-05-17 | 11770 | 49.87 | 49.87 | 49.87 | -4.59 | -9.09 | -13.25 | 2023-06-13 | 17640 | -42.12 |
| R8L21_C28_053800_T1_FALSE_STAGE2 | 2022-03-03 | 70800 | 208.62 | 208.62 | 208.62 | -5.65 | -5.65 | -16.81 | 2022-03-24 | 218500 | -73.04 |

### 4B overlay trigger metrics

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | peak_date | peak_price | drawdown_after_peak_pct | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L21_C28_012510_T2_4B_OVERLAY | 2020-09-08 | 120000 | 13.33 | -15.42 | 2020-09-08 | 136000 | -38.9 | 0.6 | 0.6 | good_local_4B_overlay_but_not_full_exit_without_non_price_slowdown | valuation_blowoff, positioning_overheat, price_only |
| R8L21_C28_263860_T2_4B_OVERLAY | 2023-06-13 | 17170 | 2.74 | -35.7 | 2023-06-13 | 17640 | -42.12 | 0.92 | 0.92 | good_local_4B_timing_for_smallcap_security_without_full_thesis_break | price_only, positioning_overheat, valuation_blowoff |
| R8L21_C28_053800_T2_4B_PRICE_ONLY | 2022-03-23 | 175800 | 24.29 | -46.53 | 2022-03-24 | 218500 | -73.04 | 0.71 | 0.71 | price_only_local_4B_too_early_for_full_exit_but_correct_as_false_positive_guard | price_only, positioning_overheat, control_premium_or_event_premium |

## 13. Current Calibrated Profile Stress Test

### 012510 더존비즈온

Current profile likely treats the case as Stage2-Actionable / Yellow, not immediate Green. That was directionally correct: the 90D and 180D MFE were both +42.26%, while early MAE was limited to -5.96%. The existing Stage2 bonus is useful here. The Green threshold and revision-min guard should be kept because the score should wait for recurring/retention/revision confirmation rather than upgrade solely from price strength.

### 263860 지니언스

Current profile likely captures Stage2/Yellow but may leave 4B overlay too late. The case delivered +49.87% MFE, but after the 2023-06-13 peak it drew down -42.12%. The lesson is not to block Stage2; the lesson is to attach a small-cap security 4B overlay when the move becomes fast and repeat-order/retention conversion is still unconfirmed.

### 053800 안랩

This is the residual false positive. The stock moved +208.62% from the selected trigger to the 2022-03-24 high, but the evidence route is political/founder-affinity, not contract-retention. If the current profile gives Stage2 credit for `public_event_or_disclosure + relative_strength` without checking the event family, it will admit the wrong kind of C28 case. The later -73.04% peak-to-trough drawdown confirms that high MFE alone is not enough.

```text
current_profile_error_count = 2
- current_profile_false_positive: 053800
- current_profile_4B_too_late: 263860
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable entry | Stage3-Yellow / Green status | green_lateness_ratio | interpretation |
|---|---:|---|---|---|
| 더존비즈온 | 95,600 | Yellow allowed, Green wait | not_applicable | Stage2 captures the move; Green should require confirmed retention/revision |
| 지니언스 | 11,770 | Yellow only, Green wait | not_applicable | Stage2 captures move but needs 4B overlay after +45%+ MFE |
| 안랩 | 70,800 | no positive Stage3 allowed | not_applicable | Green must be blocked; evidence family is wrong |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R8L21_C28_012510_T2_4B_OVERLAY | 0.60 | 0.60 | decent local overlay, but no hard exit without non-price slowdown |
| R8L21_C28_263860_T2_4B_OVERLAY | 0.92 | 0.92 | good local 4B timing for small-cap security software |
| R8L21_C28_053800_T2_4B_PRICE_ONLY | 0.71 | 0.71 | correct as false-positive risk overlay; not positive C28 evidence |

C28-specific 4B rule candidate:

```text
if canonical_archetype_id == C28
and MFE_30D_pct >= 45
and repeat_order_or_retention_conversion is not confirmed
and relative_strength_score is the main score driver:
    add smallcap_security_4B_overlay
    do_not_upgrade_to_Stage3_Green
```

## 16. 4C Protection Audit

No hard 4C thesis-break trigger is promoted in this loop. AhnLab is treated as `false_break` rather than a C28 thesis-break because it never had a valid C28 positive thesis. Genian is `thesis_break_watch_only`: the collapse says the 4B overlay was needed, but this loop does not prove a hard contract-retention break.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The result is concentrated in C28. Do not generalize to all L8 software/content/platform cases yet.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

Proposed shadow-only rules:

```text
1. c28_contract_retention_or_repeat_order_required_for_green
2. c28_political_founder_affinity_guard
3. c28_smallcap_security_mfe_4b_overlay
```

These are not production changes. They are candidates for the later batch implementation ledger.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 3 | 100.25 | -6.9 | 100.25 | -12.01 | 33.33 | 0 | 1 | mixed_alignment_requires_C28_guard |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 3 | 100.25 | -6.9 | 100.25 | -12.01 | 33.33 | 0 | 0 | high_MFE_but_poor_quality_due_false_positive |
| P1_L8_sector_specific_candidate_profile | sector_specific | 2 | 46.06 | -7.53 | 46.06 | -9.61 | 0.0 | 0 | 1 | better_precision |
| P2_C28_canonical_archetype_candidate_profile | canonical_archetype_specific | 2 | 46.06 | -7.53 | 46.06 | -9.61 | 0.0 | 0 | 0 | best_precision_without_losing_positive_cases |
| P3_C28_counterexample_guard_profile | counterexample_guard | 2 | 46.06 | -7.53 | 46.06 | -9.61 | 0.0 | 0 | 1 | strong_counterexample_filter |

## 20. Score-Return Alignment Matrix

| symbol | before label | after label | 90D MFE / MAE | alignment |
|---|---|---|---|---|
| 012510 | Stage3-Yellow | Stage3-Yellow | +42.26 / -5.96 | aligned positive; keep Stage2/Yellow, require retention KPI for Green |
| 263860 | Stage3-Yellow | Stage2-Actionable + 4B overlay | +49.87 / -9.09 | positive but high-MAE; overlay helps |
| 053800 | false Stage2 candidate | Narrative-only / 4B risk | +208.62 / -5.65 | high MFE but wrong evidence; removed from positive calibration |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | CLOUD_ERP_CONTRACT_RETENTION_OPERATING_LEVERAGE / NAC_EDR_ZERO_TRUST_SECURITY_CONTRACT_RETENTION / SECURITY_SOFTWARE_POLITICAL_AFFINITY_FALSE_POSITIVE | 2 | 1 | 3 | 0 | 3 | 0 | 6 | 3 | 2 | False | True | C28 now has positive cloud ERP + positive/high-MAE security + political-affinity false-positive counterexample; still needs pure retention renewal-loss 4C case. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

residual_error_types_found:
- security_public_event_false_positive
- political_founder_affinity_false_positive
- smallcap_security_4B_late

new_axis_proposed:
- c28_contract_retention_or_repeat_order_required_for_green
- c28_political_founder_affinity_guard
- c28_smallcap_security_mfe_4b_overlay

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage within C28
- full_4b_requires_non_price_evidence within C28
- stage3_green_revision_min within C28

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- ticker profile paths and corporate-action caveats
- selected entry_date / entry_price
- 30D / 90D / 180D MFE and MAE based on stock-web tradable rows
- local vs full-window 4B proximity for the selected overlay triggers
- positive/counterexample balance
- dedupe fields and representative-trigger separation
```

Not validated:

```text
- production scoring code
- stock_agent src/e2r implementation
- live candidate scan
- broker/API integration
- primary filing extraction for every evidence item
- 2Y quantitative calibration for all cases
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_contract_retention_or_repeat_order_required_for_green,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,Duzon/Genian positives work as Stage2/Yellow only when contract-retention/recurring-revenue route is present; AhnLab political blowoff fails this gate.,keeps 2/2 positive representative cases while blocking 1/1 false-positive representative case,R8L21_C28_012510_T1_STAGE2_ACTIONABLE|R8L21_C28_263860_T1_STAGE2_ACTIONABLE|R8L21_C28_053800_T1_FALSE_STAGE2,3,3,1,medium,canonical_archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c28_political_founder_affinity_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,AhnLab showed +208.62% MFE and then -73.04% peak drawdown without contract-retention evidence; the driver was founder/political event premium.,removes a high-MFE but wrong-evidence false positive from C28 positive calibration,R8L21_C28_053800_T1_FALSE_STAGE2|R8L21_C28_053800_T2_4B_PRICE_ONLY,2,1,1,medium,canonical_archetype_shadow_only,not production; political-affinity route should be narrative_only or 4B risk
shadow_weight,c28_smallcap_security_mfe_4b_overlay,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,none,MFE_30D>45% and no repeat_order_conversion,+1,Genian reached +49.87% MFE then suffered -42.12% peak drawdown; local 4B overlay should appear before full thesis break.,reduces late-4B residual without downgrading the initial Stage2 case,R8L21_C28_263860_T1_STAGE2_ACTIONABLE|R8L21_C28_263860_T2_4B_OVERLAY,2,1,0,low_to_medium,canonical_archetype_shadow_only,not production; use as overlay only
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"case_id": "R8L21_C28_012510_DUZON_CLOUD_ERP_RETENTION", "symbol": "012510", "company_name": "더존비즈온", "round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_ERP_CONTRACT_RETENTION_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "software_contract_retention", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L21_C28_012510_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2-Actionable with recurring cloud/ERP contract-retention evidence aligned with +42.26% 90D/180D MFE and controlled early MAE.", "current_profile_verdict": "current_profile_correct", "notes": "Positive C28 sample: contract/retention/operating leverage, not price-only software theme.", "row_type": "case", "price_source": "Songdaiki/stock-web"}
{"case_id": "R8L21_C28_263860_GENIANS_NAC_EDR_ZERO_TRUST", "symbol": "263860", "company_name": "지니언스", "round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NAC_EDR_ZERO_TRUST_SECURITY_CONTRACT_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "security_contract_retention", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R8L21_C28_263860_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "NAC/EDR/zero-trust security evidence aligned with +49.87% MFE but required earlier 4B overlay due -42.12% post-peak drawdown.", "current_profile_verdict": "current_profile_4B_too_late", "notes": "Positive but high-MAE small-cap security software sample; teaches 4B overlay rather than Green promotion.", "row_type": "case", "price_source": "Songdaiki/stock-web"}
{"case_id": "R8L21_C28_053800_AHNLAB_POLITICAL_AFFINITY_FALSE_POSITIVE", "symbol": "053800", "company_name": "안랩", "round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "SECURITY_SOFTWARE_POLITICAL_AFFINITY_FALSE_POSITIVE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "security_contract_retention", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R8L21_C28_053800_T1_FALSE_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Massive +208.62% MFE was driven by political/founder-affinity event route, not contract retention; later -73.04% peak-to-trough validates false-positive guard.", "current_profile_verdict": "current_profile_false_positive", "notes": "Counterexample: cybersecurity label plus relative strength must not become C28 Stage2/3 without contract/retention evidence.", "row_type": "case", "price_source": "Songdaiki/stock-web"}
{"round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R8L21_C28_012510_T1_STAGE2_ACTIONABLE", "case_id": "R8L21_C28_012510_DUZON_CLOUD_ERP_RETENTION", "symbol": "012510", "company_name": "더존비즈온", "fine_archetype_id": "CLOUD_ERP_CONTRACT_RETENTION_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "software_contract_retention", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "4B_non_price_requirement_stress_test"], "trigger_type": "Stage2-Actionable", "trigger_date": "2020-05-07", "entry_date": "2020-05-07", "entry_price": 95600, "evidence_available_at_that_date": "Cloud ERP / WEHAGO / enterprise software recurring-revenue route was already public; selected trigger uses first strong stock-web reaction day after cloud/ERP demand repricing.", "evidence_source": "public company/IR/news evidence family; price row exact from stock-web 012/012510/2020.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "MFE_30D_pct": 29.18, "MFE_90D_pct": 42.26, "MFE_180D_pct": 42.26, "MFE_1Y_pct": 42.26, "MFE_2Y_pct": null, "MAE_30D_pct": -5.96, "MAE_90D_pct": -5.96, "MAE_180D_pct": -5.96, "MAE_1Y_pct": -13.08, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-09-08", "peak_price": 136000, "drawdown_after_peak_pct": -38.9, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L21_C28_012510_ENTRY_2020-05-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R8L21_C28_012510_T2_4B_OVERLAY", "case_id": "R8L21_C28_012510_DUZON_CLOUD_ERP_RETENTION", "symbol": "012510", "company_name": "더존비즈온", "fine_archetype_id": "CLOUD_ERP_CONTRACT_RETENTION_OPERATING_LEVERAGE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "software_contract_retention", "loop_objective": ["4B_non_price_requirement_stress_test"], "trigger_type": "Stage4B-Overlay", "trigger_date": "2020-09-08", "entry_date": "2020-09-08", "entry_price": 120000, "evidence_available_at_that_date": "Valuation/rerating speed had outrun near-term confirmed retention evidence; 136000 high formed same day but close fell to 120000.", "evidence_source": "stock-web price row plus valuation/positioning overlay family; not a positive promotion trigger", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "MFE_30D_pct": 13.33, "MFE_90D_pct": 13.33, "MFE_180D_pct": 13.33, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.42, "MAE_90D_pct": -18.33, "MAE_180D_pct": -30.75, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-09-08", "peak_price": 136000, "drawdown_after_peak_pct": -38.9, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.6, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "good_local_4B_overlay_but_not_full_exit_without_non_price_slowdown", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L21_C28_012510_ENTRY_2020-09-08", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R8L21_C28_263860_T1_STAGE2_ACTIONABLE", "case_id": "R8L21_C28_263860_GENIANS_NAC_EDR_ZERO_TRUST", "symbol": "263860", "company_name": "지니언스", "fine_archetype_id": "NAC_EDR_ZERO_TRUST_SECURITY_CONTRACT_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "security_contract_retention", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test"], "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-17", "entry_date": "2023-05-17", "entry_price": 11770, "evidence_available_at_that_date": "Security software/NAC/EDR/zero-trust demand route plus visible stock-web accumulation; selected as C28 small-cap positive/high-MAE case.", "evidence_source": "public security software evidence family; price row exact from stock-web 263/263860/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv", "profile_path": "atlas/symbol_profiles/263/263860.json", "MFE_30D_pct": 49.87, "MFE_90D_pct": 49.87, "MFE_180D_pct": 49.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.59, "MAE_90D_pct": -9.09, "MAE_180D_pct": -13.25, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-13", "peak_price": 17640, "drawdown_after_peak_pct": -42.12, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L21_C28_263860_ENTRY_2023-05-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R8L21_C28_263860_T2_4B_OVERLAY", "case_id": "R8L21_C28_263860_GENIANS_NAC_EDR_ZERO_TRUST", "symbol": "263860", "company_name": "지니언스", "fine_archetype_id": "NAC_EDR_ZERO_TRUST_SECURITY_CONTRACT_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "security_contract_retention", "loop_objective": ["4B_non_price_requirement_stress_test"], "trigger_type": "Stage4B-Overlay", "trigger_date": "2023-06-13", "entry_date": "2023-06-13", "entry_price": 17170, "evidence_available_at_that_date": "Small-cap security rerating reached +45%+ within a short window; no verified repeat-order conversion in this run, so overlay rather than full thesis exit.", "evidence_source": "stock-web price row plus small-cap security rerating overlay family", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv", "profile_path": "atlas/symbol_profiles/263/263860.json", "MFE_30D_pct": 2.74, "MFE_90D_pct": 2.74, "MFE_180D_pct": 2.74, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -35.7, "MAE_90D_pct": -37.68, "MAE_180D_pct": -40.54, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-13", "peak_price": 17640, "drawdown_after_peak_pct": -42.12, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_local_4B_timing_for_smallcap_security_without_full_thesis_break", "four_b_evidence_type": ["price_only", "positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L21_C28_263860_ENTRY_2023-06-13", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R8L21_C28_053800_T1_FALSE_STAGE2", "case_id": "R8L21_C28_053800_AHNLAB_POLITICAL_AFFINITY_FALSE_POSITIVE", "symbol": "053800", "company_name": "안랩", "fine_archetype_id": "SECURITY_SOFTWARE_POLITICAL_AFFINITY_FALSE_POSITIVE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "security_contract_retention", "loop_objective": ["residual_false_positive_mining", "counterexample_mining"], "trigger_type": "False-Stage2-Actionable", "trigger_date": "2022-03-03", "entry_date": "2022-03-03", "entry_price": 70800, "evidence_available_at_that_date": "Security-company label and founder/political event route were public, but no contract-retention or confirmed enterprise security order evidence was identified for C28 promotion.", "evidence_source": "Ahn Cheol-soo / AhnLab political-affinity public background plus stock-web 053/053800/2022.csv price rows", "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "MFE_30D_pct": 208.62, "MFE_90D_pct": 208.62, "MFE_180D_pct": 208.62, "MFE_1Y_pct": 208.62, "MFE_2Y_pct": null, "MAE_30D_pct": -5.65, "MAE_90D_pct": -5.65, "MAE_180D_pct": -16.81, "MAE_1Y_pct": -16.81, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -73.04, "green_lateness_ratio": "not_applicable:false_positive_no_confirmed_stage3", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "false_break", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L21_C28_053800_ENTRY_2022-03-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R8L21_C28_053800_T2_4B_PRICE_ONLY", "case_id": "R8L21_C28_053800_AHNLAB_POLITICAL_AFFINITY_FALSE_POSITIVE", "symbol": "053800", "company_name": "안랩", "fine_archetype_id": "SECURITY_SOFTWARE_POLITICAL_AFFINITY_FALSE_POSITIVE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "security_contract_retention", "loop_objective": ["4B_non_price_requirement_stress_test"], "trigger_type": "Stage4B-Overlay", "trigger_date": "2022-03-23", "entry_date": "2022-03-23", "entry_price": 175800, "evidence_available_at_that_date": "One-day/short-window political-affinity blowoff; no non-price security contract evidence, so local 4B overlay only and not a full C28 thesis signal.", "evidence_source": "stock-web price row plus political-affinity/founder route", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "MFE_30D_pct": 24.29, "MFE_90D_pct": 24.29, "MFE_180D_pct": 24.29, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -46.53, "MAE_90D_pct": -53.92, "MAE_180D_pct": -66.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -73.04, "green_lateness_ratio": "not_applicable:4B_false_positive", "four_b_local_peak_proximity": 0.71, "four_b_full_window_peak_proximity": 0.71, "four_b_timing_verdict": "price_only_local_4B_too_early_for_full_exit_but_correct_as_false_positive_guard", "four_b_evidence_type": ["price_only", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "false_break", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L21_C28_053800_ENTRY_2022-03-23", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "P2_C28_canonical_archetype_candidate_profile", "case_id": "R8L21_C28_012510_DUZON_CLOUD_ERP_RETENTION", "trigger_id": "R8L21_C28_012510_T1_STAGE2_ACTIONABLE", "symbol": "012510", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 17, "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 13, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 10, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 19, "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 15, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 10, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 83, "stage_label_after": "Stage3-Yellow", "changed_components": ["contract_score", "+2", "customer_quality_score", "+1"], "component_delta_explanation": "C28 candidate adds contract-retention/recurring-revenue quality but does not force Green without confirmed retention KPI/revision >55.", "MFE_90D_pct": 42.26, "MAE_90D_pct": -5.96, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P2_C28_canonical_archetype_candidate_profile", "case_id": "R8L21_C28_263860_GENIANS_NAC_EDR_ZERO_TRUST", "trigger_id": "R8L21_C28_263860_T1_STAGE2_ACTIONABLE", "symbol": "263860", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 13, "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 9, "relative_strength_score": 19, "customer_quality_score": 12, "policy_or_regulatory_score": 14, "valuation_repricing_score": 11, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 9, "relative_strength_score": 17, "customer_quality_score": 12, "policy_or_regulatory_score": 14, "valuation_repricing_score": 11, "execution_risk_score": -5, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable", "changed_components": ["relative_strength_score", "-2", "execution_risk_score", "-5"], "component_delta_explanation": "Small-cap security strength is real but high post-peak drawdown argues for Stage2/Yellow only plus early 4B overlay, not Green.", "MFE_90D_pct": 49.87, "MAE_90D_pct": -9.09, "score_return_alignment_label": "positive_but_high_mae", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "P2_C28_canonical_archetype_candidate_profile", "case_id": "R8L21_C28_053800_AHNLAB_POLITICAL_AFFINITY_FALSE_POSITIVE", "trigger_id": "R8L21_C28_053800_T1_FALSE_STAGE2", "symbol": "053800", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 0, "relative_strength_score": 24, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 22, "execution_risk_score": "unknown_or_not_supported", "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable_false_positive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -18, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 39, "stage_label_after": "Narrative-Only/4B-Risk", "changed_components": ["relative_strength_score", "-16", "policy_or_regulatory_score", "-6", "valuation_repricing_score", "-22", "execution_risk_score", "-18"], "component_delta_explanation": "Political/founder-affinity route strips the public-event and relative-strength credit from C28 positive scoring.", "MFE_90D_pct": 208.62, "MAE_90D_pct": -5.65, "score_return_alignment_label": "false_positive_removed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "shadow_weight", "axis": "c28_contract_retention_or_repeat_order_required_for_green", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Duzon/Genian positives work as Stage2/Yellow only when contract-retention/recurring-revenue route is present; AhnLab political blowoff fails this gate.", "backtest_effect": "keeps 2/2 positive representative cases while blocking 1/1 false-positive representative case", "trigger_ids": "R8L21_C28_012510_T1_STAGE2_ACTIONABLE|R8L21_C28_263860_T1_STAGE2_ACTIONABLE|R8L21_C28_053800_T1_FALSE_STAGE2", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "shadow_weight", "axis": "c28_political_founder_affinity_guard", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "AhnLab showed +208.62% MFE and then -73.04% peak drawdown without contract-retention evidence; the driver was founder/political event premium.", "backtest_effect": "removes a high-MFE but wrong-evidence false positive from C28 positive calibration", "trigger_ids": "R8L21_C28_053800_T1_FALSE_STAGE2|R8L21_C28_053800_T2_4B_PRICE_ONLY", "calibration_usable_count": 2, "new_independent_case_count": 1, "counterexample_count": 1, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; political-affinity route should be narrative_only or 4B risk"}
{"row_type": "shadow_weight", "axis": "c28_smallcap_security_mfe_4b_overlay", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "baseline_value": "none", "tested_value": "MFE_30D>45% and no repeat_order_conversion", "delta": "+1", "reason": "Genian reached +49.87% MFE then suffered -42.12% peak drawdown; local 4B overlay should appear before full thesis break.", "backtest_effect": "reduces late-4B residual without downgrading the initial Stage2 case", "trigger_ids": "R8L21_C28_263860_T1_STAGE2_ACTIONABLE|R8L21_C28_263860_T2_4B_OVERLAY", "calibration_usable_count": 2, "new_independent_case_count": 1, "counterexample_count": 0, "confidence": "low_to_medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; use as overlay only"}
{"row_type": "residual_contribution", "round": "R8", "loop": "21", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["security_public_event_false_positive", "political_founder_affinity_false_positive", "smallcap_security_4B_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R8_C27_CONTENT_IP_GLOBAL_MONETIZATION or R13_C32_HARD_4C_AFTERPATH
reason = C28 now has a starter positive/counterexample/4B set; remaining gap is a true contract-renewal failure 4C case.
```

## 28. Source Notes

Primary price validation:

- Songdaiki/stock-web `atlas/manifest.json`.
- Songdaiki/stock-web symbol profiles:
  - `atlas/symbol_profiles/012/012510.json`
  - `atlas/symbol_profiles/263/263860.json`
  - `atlas/symbol_profiles/053/053800.json`
- Songdaiki/stock-web tradable shards:
  - `atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/012/012510/2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv`

Coverage artifact:

- `stock_agent/reports/e2r_calibration/ingest_summary.md`

Public background used for the AhnLab false-positive interpretation:

- 2022 South Korean presidential election context and Ahn Cheol-soo political/founder background from public encyclopedic/news-linked references.
