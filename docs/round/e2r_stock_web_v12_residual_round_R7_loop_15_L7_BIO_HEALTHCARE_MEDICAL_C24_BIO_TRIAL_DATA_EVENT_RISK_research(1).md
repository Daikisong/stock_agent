# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| research_session | post_calibrated_sector_archetype_residual_research |
| mode | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 |
| scheduled_round | R7 |
| scheduled_loop | 15 |
| completed_round | R7 |
| completed_loop | 15 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK |
| fine_archetype_id | CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE |
| output_file | e2r_stock_web_v12_residual_round_R7_loop_15_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md |
| price_source | Songdaiki/stock-web |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| production_scoring_changed | false |
| shadow_weight_only | true |
| stock_agent_code_accessed | false |
| stock_agent_code_patch_written | false |
| handoff_prompt_embedded | true |
| handoff_prompt_executed_now | false |

This loop adds 3 new independent cases, 1 counterexample, and 4 residual errors for `R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK`.

## 1. Current Calibrated Profile Assumption

The current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`, with the already-applied global axes assumed active:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does **not** re-prove those global axes. It asks a narrower question: inside C24, when does a clinical-data or partnered-asset event deserve Stage2/Yellow, when must Green be delayed, and when does a failed endpoint become immediate 4C?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R7 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK |
| fine_archetype_id | CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE |
| round_sector_consistency | pass |
| rule_scope_selected | canonical_archetype_specific |
| sector_specific_rule_candidate | false |
| canonical_archetype_rule_candidate | true |

R7 maps directly to `L7_BIO_HEALTHCARE_MEDICAL`. C24 is selected because previous R7 v12 local outputs already covered C25 in loops 10/13 and C23 in loops 11/14. Loop 12 covered C24, but it was concentrated in Yuhan/Oscotec/Shinpoong/HLB. This file adds three independent C24 symbols: HanAll, ABL Bio, and SillaJen.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 outputs inspected:

```text
R7 loop 10 -> C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
R7 loop 11 -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
R7 loop 12 -> C24_BIO_TRIAL_DATA_EVENT_RISK
R7 loop 13 -> C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
R7 loop 14 -> C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

Avoided C24 loop 12 symbols:

```text
000100 유한양행
039200 오스코텍
019170 신풍제약
028300 HLB
084990 헬릭스미스 narrative-only
```

This loop uses only new independent aggregate symbols for C24:

```text
009420 한올바이오파마
298380 에이비엘바이오
215600 신라젠
```

Novelty status:

```text
same_symbol_same_trigger_date_research = false
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 5
minimum_new_independent_case_ratio = 1.00
round_schedule_status = valid
round_sector_consistency = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields read from `Songdaiki/stock-web`:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX,KOSDAQ,KOSDAQ GLOBAL,KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Important caveat: price rows are raw/unadjusted FinanceData/marcap OHLC. Corporate-action contaminated 180D windows are blocked by default.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | first-last | trading_days | CA status |
| --- | --- | --- | --- | --- | --- |
| 009420 | 한올바이오파마 | atlas/symbol_profiles/009/009420.json | 1995-05-02 ~ 2026-02-20 | 7757 | 2015 and older candidates only; clean 2023-2024 window |
| 298380 | 에이비엘바이오 | atlas/symbol_profiles/298/298380.json | 2018-12-19 ~ 2026-02-20 | 1759 | no corporate-action candidates |
| 215600 | 신라젠 | atlas/symbol_profiles/215/215600.json | 2016-12-06 ~ 2026-02-20 | 1654 | 2022/2024 candidates outside 2019-2020 window |

All three aggregate cases have usable 180-trading-day forward windows in stock-web and no corporate-action candidate inside the calibrated 180D window. SillaJen has later corporate-action candidates in 2022 and 2024, but the 2019-2020 futility window is clean for this calibration purpose.

## 6. Canonical Archetype Compression Map

```text
IMVT1402_PHASE1_PARTNERED_DATA_RERATING
  -> C24_BIO_TRIAL_DATA_EVENT_RISK
  -> fine: partnered clinical data, high-MAE success

ABL301_SANOFI_LICENSE_PARTNER_VALIDATION
  -> C24_BIO_TRIAL_DATA_EVENT_RISK
  -> fine: clinical asset partner validation, not endpoint success

PEXAVEC_PHASE3_FUTILITY
  -> C24_BIO_TRIAL_DATA_EVENT_RISK
  -> fine: binary Phase3 thesis-break / hard 4C route
```

C24 should not split by disease area. The reusable grammar is evidence quality: endpoint success, partner validation, follow-on de-risking, event-cap risk, and thesis break.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R7L15-C24-009420-HANALL-IMVT1402-PH1-HIGHMAE-SUCCESS | 009420 | 한올바이오파마 | high_mae_success | positive | R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927 | current_profile_too_early |
| R7L15-C24-298380-ABL-SANOFI-ABL301-HIGHMAE-SUCCESS | 298380 | 에이비엘바이오 | high_mae_success | positive | R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112 | current_profile_too_early |
| R7L15-C24-215600-SILLAJEN-PEXAVEC-FUTILITY-4C | 215600 | 신라젠 | false_positive_green | counterexample | R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_representative_trigger_count = 3
```

The balance is intentionally asymmetric: two cases show that C24 events can be real but high-MAE, and one case shows the hard failure cliff. That is enough for a canonical C24 shadow rule, but not enough for a broad healthcare-sector rule.

## 9. Evidence Source Map

| symbol | company | event family | trigger_date | evidence interpretation |
|---|---|---|---|---|
| 009420 | 한올바이오파마 | IMVT-1402 Phase 1 positive data | 2023-09-26 | Real partner/readout signal; Stage2 allowed, clean Green delayed due high-MAE data-event path |
| 298380 | 에이비엘바이오 | ABL301/Sanofi license validation | 2022-01-12 | Partner quality validates platform, but endpoint/regulatory proof is not yet complete |
| 215600 | 신라젠 | Pexa-Vec Phase 3 futility | 2019-08-02 | Pre-readout expectation was false Green; futility is hard 4C thesis break |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | entry_date | entry_price |
| --- | --- | --- | --- | --- | --- |
| 009420 | 한올바이오파마 | atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009420/2024.csv | atlas/symbol_profiles/009/009420.json | 2023-09-27 | 32650 |
| 009420 | 한올바이오파마 | atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009420/2024.csv | atlas/symbol_profiles/009/009420.json | 2023-12-27 | 44300 |
| 298380 | 에이비엘바이오 | atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv | atlas/symbol_profiles/298/298380.json | 2022-01-12 | 26150 |
| 215600 | 신라젠 | atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv|atlas/ohlcv_tradable_by_symbol_year/215/215600/2020.csv | atlas/symbol_profiles/215/215600.json | 2019-08-01 | 44550 |
| 215600 | 신라젠 | atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv|atlas/ohlcv_tradable_by_symbol_year/215/215600/2020.csv | atlas/symbol_profiles/215/215600.json | 2019-08-02 | 31200 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | trigger_outcome_label | current_profile_verdict | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927 | 009420 | Stage2-Actionable | 2023-09-26 | 2023-09-27 | 32650 | 21.75 | 43.19 | 43.19 | -12.56 | -12.56 | -12.56 | high_mae_structural_success | current_profile_too_early | True |
| R7L15-C24-009420-T2-PRICE-ONLY-4B-OVERLAY-20231227 | 009420 | Stage4B-Overlay | 2023-12-27 | 2023-12-27 | 44300 | 5.53 | 5.53 | 5.53 | -35.55 | -35.55 | -35.55 | 4B_overlay_success_but_price_only | current_profile_correct | False |
| R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112 | 298380 | Stage2-Actionable | 2022-01-12 | 2022-01-12 | 26150 | 33.08 | 33.08 | 33.08 | -8.99 | -26.58 | -27.53 | partner_validation_high_mae_success | current_profile_too_early | True |
| R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801 | 215600 | Stage3-Green-candidate-false-positive | 2019-08-01 | 2019-08-01 | 44550 | 2.02 | 2.02 | 2.02 | -79.8 | -82.45 | -82.45 | false_positive_green | current_profile_false_positive | True |
| R7L15-C24-215600-T2-HARD-4C-FUTILITY-20190802 | 215600 | Stage4C | 2019-08-02 | 2019-08-02 | 31200 | 0.0 | 0.0 | 0.0 | -71.15 | -74.94 | -74.94 | 4C_success | current_profile_4C_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows:

| trigger_id | entry | high basis | low basis | interpretation |
|---|---:|---|---|---|
| R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927 | 32,650 | 39,750 / 46,750 / 46,750 | 28,550 / 28,550 / 28,550 | positive but high-MAE; Green should wait for follow-on de-risking |
| R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112 | 26,150 | 34,800 / 34,800 / 34,800 | 23,800 / 19,200 / 18,950 | partner validation had real upside but high 90D/180D MAE |
| R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801 | 44,550 | 45,450 / 45,450 / 45,450 | 9,000 / 7,820 / 7,820 | binary clinical-event false positive; endpoint evidence absent |

Overlay-only rows:

| trigger_id | role | why not aggregate |
|---|---|---|
| R7L15-C24-009420-T2-PRICE-ONLY-4B-OVERLAY-20231227 | 4B overlay | same HanAll case; tests local/full peak proximity |
| R7L15-C24-215600-T2-HARD-4C-FUTILITY-20190802 | 4C overlay | same SillaJen case; tests hard thesis-break routing |

## 13. Current Calibrated Profile Stress Test

1. Current calibrated profile would likely allow HanAll/ABL as Stage2-Actionable or Yellow candidates because there is non-price evidence and partner validation.
2. The price path says that is not wrong, but it is dangerous if promoted to clean Green: HanAll MAE_90D = -12.56%, ABL MAE_90D = -26.58%.
3. Existing Stage2 bonus is appropriate; the issue is not Stage2, it is premature Green on C24 data/partner headlines.
4. Yellow threshold 75 is acceptable for partnered validation if endpoint or dose-response interpretation is visible.
5. Green 87 / revision 55 is too permissive for C24 if it can be reached via relative strength + partner headline without follow-on clinical/regulatory bridge.
6. Price-only blowoff guard is strengthened: HanAll December 2023 was a valid 4B overlay, not a full thesis-exit without non-price slowdown.
7. Full 4B non-price requirement is kept.
8. Hard 4C routing is strengthened: SillaJen futility should route immediately to 4C.

Verdicts:

```text
009420 = current_profile_too_early
298380 = current_profile_too_early
215600 pre-futility = current_profile_false_positive
215600 futility = current_profile_4C_too_late
```

## 14. Stage2 / Yellow / Green Comparison

C24 has a different rhythm than EPS-revision sectors. A Stage2 data event can be real and still draw down sharply because data interpretation, dose-response, FDA path, and partner economics remain unresolved.

| symbol | Stage2 entry | likely Green condition | measured issue |
|---|---:|---|---|
| 009420 | 32,650 | follow-on dose/Phase2/regulatory bridge | +43.19% MFE_90 but -12.56% MAE_90 |
| 298380 | 26,150 | clinical/regulatory proof beyond license headline | +33.08% MFE_90 but -26.58% MAE_90 |
| 215600 | 44,550 false Green candidate | endpoint success required | -82.45% MAE_90 |

`green_lateness_ratio` is mostly not applicable because no clean C24 Green trigger was confirmed before the later evidence bridge. The rule is: C24 can be Stage2/Actionable on real data, but Green requires endpoint quality plus interpretability or commercial/regulatory bridge.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---|---|
| R7L15-C24-009420-T2-PRICE-ONLY-4B-OVERLAY-20231227 | 0.83 | 0.83 | price_only, valuation_blowoff, positioning_overheat | local 4B overlay only; not full 4B without non-price slowdown |
| R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801 | n/a | n/a | explicit_event_cap, positioning_overheat | event-cap guard should block Green before data |

## 16. 4C Protection Audit

SillaJen is the hard 4C test. A pre-event Green candidate at 44,550 suffered `MAE_90D = -82.45%`. The hard 4C row on 2019-08-02 still had severe downside, but it correctly terminates the prior trial-success thesis.

```text
four_c_protection_label = hard_4c_success
hard_4c_thesis_break_routes_to_4c = strengthened
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

R7 contains too many subdomains: devices, biologics, trial-stage biotech, commercial pharma, and medical AI. The evidence here is C24-specific, not a general healthcare-sector promotion rule.

## 18. Canonical-Archetype Rule Candidate

Proposed C24 shadow rules:

```text
C24_partner_validated_data_high_MAE_guard:
    If data/partner evidence is real but endpoint/regulatory bridge is incomplete,
    allow Stage2-Actionable or Yellow-watch,
    but require follow-on de-risking before clean Green.

C24_endpoint_or_interpretation_bridge_required_for_Green:
    Green requires endpoint quality, dose-response interpretability,
    partner continuation, or regulatory/commercial route.
    License headline alone is not enough.

C24_binary_trial_failure_4C_hard_route:
    Failed pivotal endpoint, futility stop, regulatory rejection,
    or thesis evidence break routes directly to 4C.

C24_price_only_4B_overlay:
    Local data-event rerating peak can be 4B overlay,
    but full 4B requires non-price slowdown/delay/funding/endpoint risk evidence.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 3 | 26.1 | -40.53 | 26.1 | -40.85 | 1/3 | 0 | 0 | too permissive for C24 Green on binary/partner headlines |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 3 | 26.1 | -40.53 | 26.1 | -40.85 | 1/3+ | 1 | 1 | less structured; confuses license event and endpoint event |
| P1_R7_sector_specific_candidate_profile | sector_specific | 3 | 26.1 | -40.53 | 26.1 | -40.85 | 1/3 | 0 | 0 | too broad for all healthcare; not proposed as sector-wide |
| P2_C24_trial_data_event_shadow_profile | canonical_archetype_specific | 3 | 26.1 | -40.53 | 26.1 | -40.85 | 0/3 after guard | 0 | 0 | best alignment: Stage2 allowed, Green delayed, 4C hard failure routed |
| P3_C24_counterexample_guard_profile | guard_profile | 3 | 26.1 | -40.53 | 26.1 | -40.85 | 0/3 after guard | 1 | 0 | safe but may under-credit real partner validation |

## 20. Score-Return Alignment Matrix

| symbol | P0 label | P2 C24 label | actual path | alignment |
|---|---|---|---|---|
| 009420 | Yellow/Green candidate | Stage2-Actionable / high-MAE watch | +43.19% MFE_90, -12.56% MAE_90 | P2 better |
| 298380 | Yellow/Green candidate | Stage2-Actionable / partner-validation watch | +33.08% MFE_90, -26.58% MAE_90 | P2 better |
| 215600 | false Green candidate | C24 binary event blocked; 4C after futility | -82.45% MAE_90 | P2 much better |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE | 2 | 1 | 1 | 1 | 3 | 0 | 5 | 3 | 4 | false | true | C24 now has additional partner-validation high-MAE and hard futility failure rows beyond loop 12 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C24_partner_validation_high_MAE
  - C24_binary_trial_event_false_green
  - C24_hard_futility_4C_route
  - price_only_4B_overlay_without_non_price_slowdown
new_axis_proposed:
  - C24_partner_validated_data_high_MAE_guard
  - C24_endpoint_or_interpretation_bridge_required_for_Green
  - C24_binary_trial_failure_4C_hard_route
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web OHLC rows for entry, high, low, close
- stock-web manifest max_date = 2026-02-20
- symbol profiles and corporate-action candidate windows
- 30D/90D/180D MFE and MAE
- positive vs counterexample balance
- C24-specific current profile stress test
```

Not validated:

```text
- live/current stock recommendations
- current Stage3 candidates
- broker/API execution
- production code integration
- exact future revenue/royalty realization
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_partner_validated_data_high_MAE_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"Partnered Phase1/license validation created real MFE but also -12% to -27% MAE before durable follow-on confirmation.","Keeps HanAll/ABL as Stage2-Actionable or Yellow watch instead of clean Green.","R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927|R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C24_binary_trial_event_no_endpoint_green_block,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"SillaJen pre-futility setup shows relative strength/event anticipation can suffer >80% MAE when endpoint success is absent.","Blocks pre-readout Green and routes futility to 4C.","R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801|R7L15-C24-215600-T2-HARD-4C-FUTILITY-20190802",3,3,1,high,canonical_shadow_only,"strengthens existing price-only and hard 4C axes"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"case_id":"R7L15-C24-009420-HANALL-IMVT1402-PH1-HIGHMAE-SUCCESS","symbol":"009420","company_name":"한올바이오파마","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_high_MAE_after_data_guard","current_profile_verdict":"current_profile_too_early","notes":"Partnered Phase 1 data created a real rerating, but the path drew down materially after the December local peak; C24 should keep data-positive cases below clean Green until follow-on de-risking.","row_type":"case","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE","price_source":"Songdaiki/stock-web"}
{"case_id":"R7L15-C24-298380-ABL-SANOFI-ABL301-HIGHMAE-SUCCESS","symbol":"298380","company_name":"에이비엘바이오","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_initial_rerating_but_high_90D_180D_MAE","current_profile_verdict":"current_profile_too_early","notes":"Large partner validation produced immediate MFE, but the unproven clinical/regulatory bridge caused -26% to -28% forward MAE.","row_type":"case","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE","price_source":"Songdaiki/stock-web"}
{"case_id":"R7L15-C24-215600-SILLAJEN-PEXAVEC-FUTILITY-4C","symbol":"215600","company_name":"신라젠","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_blocked_after_C24_binary_event_guard","current_profile_verdict":"current_profile_false_positive","notes":"Pre-readout expectation carried event-cap risk; futility converted directly into hard 4C.","row_type":"case","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE","price_source":"Songdaiki/stock-web"}
{"trigger_id":"R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927","case_id":"R7L15-C24-009420-HANALL-IMVT1402-PH1-HIGHMAE-SUCCESS","symbol":"009420","company_name":"한올바이오파마","sector":"bio_partnered_autoimmune_platform","primary_archetype":"clinical_data_partner_validation","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-26","entry_date":"2023-09-27","entry_price":32650,"evidence_available_at_that_date":"Immunovant reported positive Phase 1 data for IMVT-1402; HanAll owns the partnered FcRn antibody origin/rights. Korean market entry is next tradable day because U.S. news timing made same-day KRX reaction unavailable.","evidence_source":"Immunovant/Investopedia public report dated 2023-09-26; stock-web 009420 rows 2023-09-27, 2023-12-27, 2024-01~2024-06.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":21.75,"MFE_90D_pct":43.19,"MFE_180D_pct":43.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.56,"MAE_90D_pct":-12.56,"MAE_180D_pct":-12.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-27","peak_price":46750,"drawdown_after_peak_pct":-38.93,"green_lateness_ratio":"not_applicable:no_C24_Green_before_follow_on_de-risking","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_structural_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile CA dates 1996-12-24,2006-05-10,2006-07-19,2015-08-18 outside window","same_entry_group_id":"R7L15-G001-009420-20230927-32650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009420/2024.csv","profile_path":"atlas/symbol_profiles/009/009420.json","row_type":"trigger","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L15-C24-009420-T2-PRICE-ONLY-4B-OVERLAY-20231227","case_id":"R7L15-C24-009420-HANALL-IMVT1402-PH1-HIGHMAE-SUCCESS","symbol":"009420","company_name":"한올바이오파마","sector":"bio_partnered_autoimmune_platform","primary_archetype":"clinical_data_partner_validation","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-12-27","entry_date":"2023-12-27","entry_price":44300,"evidence_available_at_that_date":"Vertical rerating into local peak after Phase 1 data, but no new non-price slowdown, failure, or delay evidence at that point.","evidence_source":"stock-web 009420 2023-12-27 high/close and subsequent 2024 drawdown rows.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"MFE_30D_pct":5.53,"MFE_90D_pct":5.53,"MFE_180D_pct":5.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-35.55,"MAE_90D_pct":-35.55,"MAE_180D_pct":-35.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-27","peak_price":46750,"drawdown_after_peak_pct":-38.93,"green_lateness_ratio":"not_applicable:4B_overlay_only","four_b_local_peak_proximity":0.83,"four_b_full_window_peak_proximity":0.83,"four_b_timing_verdict":"price_only_local_peak_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success_but_price_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L15-G001-009420-4B-20231227-44300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same HanAll case, separate 4B timing audit only","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv|atlas/ohlcv_tradable_by_symbol_year/009/009420/2024.csv","profile_path":"atlas/symbol_profiles/009/009420.json","row_type":"trigger","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112","case_id":"R7L15-C24-298380-ABL-SANOFI-ABL301-HIGHMAE-SUCCESS","symbol":"298380","company_name":"에이비엘바이오","sector":"bio_partnered_neurodegenerative_platform","primary_archetype":"clinical_asset_partner_validation","loop_objective":"coverage_gap_fill|green_strictness_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-01-12","entry_date":"2022-01-12","entry_price":26150,"evidence_available_at_that_date":"Sanofi/ABL301 global license event validated a clinical-stage bispecific platform, but follow-on clinical/regulatory proof was not yet present.","evidence_source":"company/public licensing disclosure around 2022-01-12; stock-web 298380 2022 rows.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":33.08,"MFE_90D_pct":33.08,"MFE_180D_pct":33.08,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.99,"MAE_90D_pct":-26.58,"MAE_180D_pct":-27.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-21","peak_price":34800,"drawdown_after_peak_pct":-45.55,"green_lateness_ratio":"not_applicable:no_confirmed_C24_Green_before_follow_on_trial_bridge","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"partner_validation_high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile has no corporate-action candidate dates","same_entry_group_id":"R7L15-G002-298380-20220112-26150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv","profile_path":"atlas/symbol_profiles/298/298380.json","row_type":"trigger","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801","case_id":"R7L15-C24-215600-SILLAJEN-PEXAVEC-FUTILITY-4C","symbol":"215600","company_name":"신라젠","sector":"bio_oncology_binary_phase3_event","primary_archetype":"binary_trial_event_failure","loop_objective":"counterexample_mining|residual_false_positive_mining|4C_thesis_break_timing_test","trigger_type":"Stage3-Green-candidate-false-positive","trigger_date":"2019-08-01","entry_date":"2019-08-01","entry_price":44550,"evidence_available_at_that_date":"Pre-event oncology Phase 3 expectation/relative-strength setup before the Pexa-Vec futility shock; no confirmed endpoint success was available.","evidence_source":"pre-futility market setup + stock-web 215600 2019 rows.","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":2.02,"MFE_90D_pct":2.02,"MFE_180D_pct":2.02,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-79.8,"MAE_90D_pct":-82.45,"MAE_180D_pct":-82.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-08-01","peak_price":45450,"drawdown_after_peak_pct":-82.79,"green_lateness_ratio":"not_applicable:false_positive_pre_readout","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"event_cap_should_block_green_without_endpoint_data","four_b_evidence_type":["positioning_overheat","explicit_event_cap","price_only"],"four_c_protection_label":"hard_4c_success_after_futility","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile CA dates 2022-10-13,2024-07-09 outside 2019-2020 window","same_entry_group_id":"R7L15-G003-215600-20190801-44550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv|atlas/ohlcv_tradable_by_symbol_year/215/215600/2020.csv","profile_path":"atlas/symbol_profiles/215/215600.json","row_type":"trigger","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R7L15-C24-215600-T2-HARD-4C-FUTILITY-20190802","case_id":"R7L15-C24-215600-SILLAJEN-PEXAVEC-FUTILITY-4C","symbol":"215600","company_name":"신라젠","sector":"bio_oncology_binary_phase3_event","primary_archetype":"binary_trial_event_failure","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2019-08-02","entry_date":"2019-08-02","entry_price":31200,"evidence_available_at_that_date":"Pexa-Vec Phase 3 futility / DMC-style stop signal broke the trial success thesis.","evidence_source":"public futility announcement around 2019-08-02; stock-web 215600 2019/2020 rows.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":["safety_or_trial_failure","thesis_evidence_broken"],"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-71.15,"MAE_90D_pct":-74.94,"MAE_180D_pct":-74.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-08-02","peak_price":31200,"drawdown_after_peak_pct":-74.94,"green_lateness_ratio":"not_applicable:4C_overlay_only","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L15-G003-215600-4C-20190802-31200","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same SillaJen case; 4C protection audit only","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv|atlas/ohlcv_tradable_by_symbol_year/215/215600/2020.csv","profile_path":"atlas/symbol_profiles/215/215600.json","row_type":"trigger","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_DATA_PARTNER_VALIDATION_HIGH_MAE_AND_HARD_FAILURE_ROUTE","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L15-C24-009420-HANALL-IMVT1402-PH1-HIGHMAE-SUCCESS","trigger_id":"R7L15-C24-009420-T1-IMVT1402-PH1-STAGE2A-20230927","symbol":"009420","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":12,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":10,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":10,"trial_data_quality_score":11,"partner_bridge_score":9,"binary_event_risk_score":-8,"commercialization_bridge_score":0,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":7,"relative_strength_score":10,"customer_quality_score":15,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":-11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":11,"trial_data_quality_score":12,"partner_bridge_score":10,"binary_event_risk_score":-14,"commercialization_bridge_score":0,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable / C24 high-MAE watch","changed_components":["binary_event_risk_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Partnered Phase 1 data is real Stage2 evidence, but high-MAE data-event grammar blocks immediate clean Green until follow-on dose/Phase2/regulatory bridge appears.","MFE_90D_pct":43.19,"MAE_90D_pct":-12.56,"score_return_alignment_label":"partial_alignment_after_high_MAE_guard","current_profile_verdict":"current_profile_too_early","row_type":"score_simulation","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK"}
{"profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L15-C24-298380-ABL-SANOFI-ABL301-HIGHMAE-SUCCESS","trigger_id":"R7L15-C24-298380-T1-ABL301-SANOFI-STAGE2A-20220112","symbol":"298380","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":14,"customer_quality_score":18,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":5,"trial_data_quality_score":6,"partner_bridge_score":16,"binary_event_risk_score":-6,"commercialization_bridge_score":0,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":11,"customer_quality_score":18,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":-13,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":5,"trial_data_quality_score":6,"partner_bridge_score":16,"binary_event_risk_score":-12,"commercialization_bridge_score":0,"thesis_break_score":0,"positioning_overheat_score":0},"weighted_score_after":75,"stage_label_after":"Stage2-Actionable / partner-validation watch","changed_components":["execution_risk_score","binary_event_risk_score","valuation_repricing_score"],"component_delta_explanation":"Large pharma partner validation is not equal to endpoint success; C24 should require clinical follow-on bridge before Green.","MFE_90D_pct":33.08,"MAE_90D_pct":-26.58,"score_return_alignment_label":"high_MFE_but_high_MAE_guard_needed","current_profile_verdict":"current_profile_too_early","row_type":"score_simulation","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK"}
{"profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L15-C24-215600-SILLAJEN-PEXAVEC-FUTILITY-4C","trigger_id":"R7L15-C24-215600-T1-PRE-FUTILITY-FALSE-GREEN-20190801","symbol":"215600","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":18,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":15,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":0,"trial_data_quality_score":0,"partner_bridge_score":0,"binary_event_risk_score":-8,"commercialization_bridge_score":0,"thesis_break_score":0,"positioning_overheat_score":18},"weighted_score_before":87,"stage_label_before":"Stage3-Green_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"clinical_endpoint_score":0,"trial_data_quality_score":0,"partner_bridge_score":0,"binary_event_risk_score":-28,"commercialization_bridge_score":0,"thesis_break_score":-25,"positioning_overheat_score":18},"weighted_score_after":38,"stage_label_after":"Stage4C_watch / Green blocked","changed_components":["clinical_endpoint_score","binary_event_risk_score","thesis_break_score","execution_risk_score"],"component_delta_explanation":"C24 binary Phase3 event without endpoint success must cap Stage3 and route to 4C immediately when futility is disclosed.","MFE_90D_pct":2.02,"MAE_90D_pct":-82.45,"score_return_alignment_label":"false_positive_blocked_after","current_profile_verdict":"current_profile_false_positive","row_type":"score_simulation","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK"}
{"row_type":"residual_contribution","round":"R7","loop":"15","scheduled_round":"R7","scheduled_loop":15,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C24_partner_validation_high_MAE","C24_binary_trial_event_false_green","C24_hard_futility_4C_route","price_only_4B_overlay_without_non_price_slowdown"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R7
completed_loop = 15
next_round = R8
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files checked:

```text
atlas/manifest.json
atlas/symbol_profiles/009/009420.json
atlas/symbol_profiles/298/298380.json
atlas/symbol_profiles/215/215600.json
atlas/ohlcv_tradable_by_symbol_year/009/009420/2023.csv
atlas/ohlcv_tradable_by_symbol_year/009/009420/2024.csv
atlas/ohlcv_tradable_by_symbol_year/298/298380/2022.csv
atlas/ohlcv_tradable_by_symbol_year/215/215600/2019.csv
atlas/ohlcv_tradable_by_symbol_year/215/215600/2020.csv
```

Research artifact context checked locally:

```text
R7 loop10 C25
R7 loop11 C23
R7 loop12 C24
R7 loop13 C25
R7 loop14 C23
```

Public event sources were used only to establish historical event semantics; quantitative backtest values come from stock-web OHLC rows.

