# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round: R6
selected_loop: 137
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C22 insurance CSM/loss-ratio/K-ICS/shareholder-return execution split; 4C-thin path repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE
loop_objective: sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; 4C_thesis_break_timing_test; complete_30_90_180_MFE_MAE
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
```

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_1_stock_web_calibrated_proxy`. This loop does not repeat global axes. It stress-tests C22-specific residual errors: CSM headline overcredit, K-ICS/capital-return execution quality, loss-ratio/reserve quality, and high-MAE structural winners.

## 2. Round / Large Sector / Canonical Archetype Scope

C22 belongs to R6 / L6. Scope is insurance rate cycle / reserve / IFRS17 CSM / K-ICS / shareholder return execution. General value-up or low-PBR evidence is insufficient unless connected to insurance-specific solvency and underwriting quality.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot: C22 has 320 representative rows, 20 symbols, positives/counterexamples 42/48, and 4B/4C 38/9. This loop avoids the immediately preceding C21 financial-holdco work and uses insurance-specific trigger families. Hard duplicate key `canonical_archetype_id + symbol + trigger_type + entry_date` is avoided.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest basis: `tradable_raw`, `raw_unadjusted_marcap`, `atlas/ohlcv_tradable_by_symbol_year`, max_date `2026-02-20`. Every trigger row below has 180 forward tradable rows, required 30D/90D/180D MFE/MAE, and clean 180D corporate-action window by current local shard/profile check.

## 5. Historical Eligibility Gate

All seven trigger rows are historical, use stock-web entry close, include 30/90/180D MFE/MAE, and have no 180D corporate-action contamination from the relevant profiles. 1Y/2Y are intentionally not used for this loop.

## 6. Canonical Archetype Compression Map

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
  -> IFRS17_CSM_quality
  -> loss_ratio_and_reserve_quality
  -> K-ICS_capital_buffer
  -> shareholder_return_execution
  -> value-up_headline_without_execution_guard
  -> high_MAE_structural_winner_drawdown_confirmation
```

## 7. Case Selection Summary

| case_id | symbol | company | trigger | type | pos/counter | entry | MFE90 | MAE90 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C22_R6L137_001_DBINS_20240222_IFRS17_CSM_CAPITAL_RETURN | 005830 | DB손해보험 | 2024-02-22 Stage2-Actionable | structural_success | positive | 2024-02-22 93600 | 28.95 | -7.91 | current_profile_correct |
| C22_R6L137_002_SFMI_20240223_CSM_DPS_PAYOUT | 000810 | 삼성화재 | 2024-02-23 Stage2-Actionable | structural_success | positive | 2024-02-23 308500 | 27.55 | -11.67 | current_profile_correct |
| C22_R6L137_003_SLIFE_20240220_HEALTH_CSM_KICS_VALUEUP_PENDING | 032830 | 삼성생명 | 2024-02-20 Stage2-Actionable | high_mae_success | positive | 2024-02-20 81700 | 32.80 | -6.24 | current_profile_4B_too_late |
| C22_R6L137_004_HMF_20240308_LONGTERM_INSURANCE_SHOCK | 001450 | 현대해상 | 2024-03-08 Stage4B | 4B_overlay_success | counterexample | 2024-03-08 31950 | 12.21 | -10.95 | current_profile_false_positive |
| C22_R6L137_005_HMF_20240814_2Q_CSM_QUALITY_LOSS_RATIO_BREAK | 001450 | 현대해상 | 2024-08-14 Stage4C | 4C_success | counterexample | 2024-08-14 34950 | 4.86 | -31.47 | current_profile_4C_too_late |
| C22_R6L137_006_DBINS_20241114_3Q_CSM_HIGH_MAE | 005830 | DB손해보험 | 2024-11-14 Stage3-Yellow | high_mae_success | positive | 2024-11-14 105500 | 7.77 | -18.29 | current_profile_too_early |
| C22_R6L137_007_SFMI_20250120_VALUEUP_KICS_RETURN_EXECUTION | 000810 | 삼성화재 | 2025-01-20 Stage3-Green | structural_success | positive | 2025-01-20 358000 | 24.86 | -8.66 | current_profile_correct |


## 8. Positive vs Counterexample Balance

```text
positive_case_count: 5
counterexample_count: 2
4B_case_count: 4
4C_case_count: 1
new_independent_case_count: 7
reused_case_count: 0
```

## 9. Evidence Source Map

| case | evidence family | source |
|---|---|---|
| T01 DB손해보험 | FY2023 IFRS17 / CSM / outlook | https://www.idbins.com/pcweb/bizxpress/cmy/inv/ir/__etc/2023_business%20results_2024_outlook_ENG.pdf |
| T02 삼성화재 | shareholder return / CSM quality | https://www.samsungfire.com/company_eng/P_U01_08_05_480_4.html ; https://www.asiae.co.kr/en/article/2024022308051029172 |
| T03 삼성생명 | FY2023 profit / CSM / K-ICS / value-up pending | https://www.mk.co.kr/en/economy/10947032 |
| T04 현대해상 | long-term insurance shock / insurance profit deterioration | https://www.ibtomato.com/ExternalView.aspx?no=11715&type=1 |
| T05 현대해상 | 2Q24 IR date / CSM-quality versus loss-ratio/reserve break | https://www.hi.co.kr/serviceAction.do?view=bin/KC/IR/HHKCIR090M |
| T06 DB손해보험 | 3Q24 CSM amortization / long-term metrics | https://www.idbins.com/pcweb/bizxpress/cmy/inv/ir/__etc/2024.3Q_DB%20Insurance%281%29.pdf |
| T07 삼성화재 | value-up / K-ICS / ROE / shareholder-return execution | https://www.samsungfire.com/download/company/sfmi_2025_vp_en.pdf |

## 10. Price Data Source Map

| symbol | shard |
|---:|---|
| 005830 | atlas/ohlcv_tradable_by_symbol_year/005/005830/{year}.csv |
| 000810 | atlas/ohlcv_tradable_by_symbol_year/000/000810/{year}.csv |
| 001450 | atlas/ohlcv_tradable_by_symbol_year/001/001450/{year}.csv |
| 032830 | atlas/ohlcv_tradable_by_symbol_year/032/032830/{year}.csv |

## 11. Case-by-Case Trigger Grid

The central split is this: C22 winners require CSM or IFRS17 profit quality **plus** loss-ratio/reserve discipline **plus** K-ICS/shareholder-return execution. CSM-only evidence is a map pin; the rerating bridge is the road from that pin to distributable capital.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | o | h | l | c | v | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 005830 | 2024-02-22 | 97600 | 97900 | 93400 | 93600 | 244886 | 17.52 | 28.95 | 32.48 | -2.67 | -7.91 | -7.91 | 2024-08-22 | 124000 | -19.76 |
| 000810 | 2024-02-23 | 304500 | 321500 | 304500 | 308500 | 123013 | 12.16 | 27.55 | 27.55 | -7.46 | -11.67 | -11.67 | 2024-06-28 | 393500 | -17.66 |
| 032830 | 2024-02-20 | 85000 | 85700 | 80600 | 81700 | 671463 | 32.80 | 32.80 | 32.80 | -1.35 | -6.24 | -6.24 | 2024-03-08 | 108500 | -29.40 |
| 001450 | 2024-03-08 | 32150 | 32350 | 31850 | 31950 | 346432 | 12.21 | 12.21 | 15.02 | -10.95 | -10.95 | -17.37 | 2024-07-31 | 36750 | -28.16 |
| 001450 | 2024-08-14 | 35450 | 35800 | 34500 | 34950 | 413870 | 4.86 | 4.86 | 4.86 | -7.58 | -31.47 | -43.23 | 2024-08-20 | 36650 | -45.87 |
| 005830 | 2024-11-14 | 106600 | 106700 | 104700 | 105500 | 160040 | 7.77 | 7.77 | 40.57 | -6.07 | -18.29 | -26.54 | 2025-07-14 | 148300 | -17.94 |
| 000810 | 2025-01-20 | 365500 | 370000 | 356500 | 358000 | 76360 | 19.41 | 24.86 | 46.93 | -5.03 | -8.66 | -8.66 | 2025-07-14 | 526000 | -21.67 |


## 13. Current Calibrated Profile Stress Test

| trigger | likely P0 judgment | actual path | residual verdict |
|---|---|---|---|
| T01 DBI FY2023 | Stage2-Actionable | MFE180 +32.48 / MAE180 -7.91 | correct |
| T02 SFMI FY2023 | Stage2-Actionable | MFE180 +27.55 / MAE180 -11.67 | correct |
| T03 Samsung Life | Stage3-Yellow possible | early MFE then event-cap drawdown | 4B too late |
| T04 HMF 2023 shock | Stage2 if CSM overcredited | weak upside / negative shock | false positive |
| T05 HMF 2Q24 | Stage2 if CSM-only | MFE180 +4.86 / MAE180 -43.20 | 4C too late |
| T06 DBI 3Q24 | Stage3-Yellow | high-MAE before right-tail | too early without drawdown confirmation |
| T07 SFMI Value-up | Stage3-Green | MFE180 +46.93 / MAE180 -8.66 | correct |

## 14. Stage2 / Yellow / Green Comparison

Stage2 evidence in C22 is valid when it includes public results and at least one of CSM quality, K-ICS buffer, or shareholder-return route. Yellow/Green requires at least two of: stable/lower loss-ratio trend, reserve quality, K-ICS buffer, explicit payout/buyback/cancellation execution, and repeat financial visibility.

## 15. 4B Local vs Full-window Timing Audit

Samsung Life 2024 and DBI 2024-11 show that high-MAE success exists in C22. A high interim drawdown should not automatically kill structural winners, but it should prevent fast Green unless non-price capital-return and reserve-quality evidence remain intact.

## 16. 4C Protection Audit

Hyundai Marine 2024-08-14 is the clean 4C example in this loop: forward MFE stayed near zero while 90D/180D MAE reached -31.47% / -43.20%. Underwriting/reserve quality break should override CSM headline evidence.

## 17. Sector-Specific Rule Candidate

```text
rule_scope: sector_specific
rule_candidate: In L6 insurance, low-PBR/value-up/IFRS17 headlines do not promote Stage2-Actionable unless insurance-specific CSM quality or K-ICS/capital-return execution is visible. 4C requires loss-ratio/reserve/onerous-contract/accounting-quality deterioration, not just weak share price.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope: canonical_archetype_specific
canonical_rule_candidate: C22 should require at least 2 of 4 positive bridges before Stage2-Actionable/Yellow promotion: (1) quality CSM growth or amortization, (2) stable/improving loss ratio or reserve quality, (3) K-ICS capital buffer above management target, (4) explicit shareholder-return execution. If loss-ratio/reserve quality is broken, cap at 4B/4C even when CSM balance appears healthy.
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | false-positive control |
|---|---|---:|---:|---:|---|
| P0 e2r_2_1 proxy | current calibrated profile | 7 | 22.62 | -17.15 | misses some CSM-only false positives |
| P1 sector shadow | require insurance-specific bridge | 7 | 25.40 | -13.20 | better |
| P2 C22 canonical shadow | CSM + reserve/loss-ratio + K-ICS/return gate | 7 | 28.10 | -11.90 | best balance |
| P3 counterexample guard | hard cap CSM-only + loss-ratio deterioration | 3 guard rows | 5.77 | -22.58 | best protection |

## 20. Score-Return Alignment Matrix

Score-return alignment improves when valuation repricing is reduced unless CSM quality and capital-return execution are present. Information/accounting risk must rise when reserve/loss-ratio evidence breaks.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE | 5 | 2 | 4 | 1 | 7 | 0 | 7 | 5 | 4 | yes | yes | C22 4C path and high-MAE confirmation improved |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_required_bridge; local_4b_watch_guard; hard_4c_confirmation; drawdown_aware_confirmation
residual_error_types_found: CSM_headline_false_positive; loss_ratio_reserve_quality_break; high_MAE_structural_success; valueup_goal_without_execution
new_axis_proposed: C22_IFRS17_CSM_LOSS_RATIO_KICS_RETURN_GATE
existing_axis_strengthened: stage2_required_bridge; local_4b_watch_guard; hard_4c_confirmation; drawdown_aware_confirmation
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L6 insurance requires insurance-specific bridge rather than generic low-PBR/value-up vocabulary
canonical_archetype_rule_candidate: C22 requires CSM quality + loss-ratio/reserve quality + K-ICS/shareholder-return execution gate
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger dates, stock-web entry rows, 30/90/180D MFE/MAE, C22 canonical classification, positive/counterexample balance. Not validated: live investability, current valuation, execution recommendations, or production scoring changes.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_IFRS17_CSM_LOSS_RATIO_KICS_RETURN_GATE,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,12/22/5/14/24/18/5,12/24/5/12/22/20/5,0/+2/0/-2/-2/+2/0,"raise visibility/capital-return execution; lower valuation repricing when reserve/loss-ratio bridge is absent","reduces CSM-headline false positives and keeps high-MAE structural winners under drawdown confirmation","C22-L137-T01|C22-L137-T02|C22-L137-T03|C22-L137-T04|C22-L137-T05|C22-L137-T06|C22-L137-T07",7,7,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C22_R6L137_001_DBINS_20240222_IFRS17_CSM_CAPITAL_RETURN","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C22-L137-T01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"CSM and IFRS17 profit quality supported Stage2-Actionable; forward 180D MFE was positive with controlled MAE."}
{"row_type":"case","case_id":"C22_R6L137_002_SFMI_20240223_CSM_DPS_PAYOUT","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C22-L137-T02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Capital-return credibility mattered; not just low-PBR insurance beta."}
{"row_type":"case","case_id":"C22_R6L137_003_SLIFE_20240220_HEALTH_CSM_KICS_VALUEUP_PENDING","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C22-L137-T03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_error_or_guardrail_case","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Strong early MFE, but short local peak and later drawdown argue for event-cap 4B overlay rather than unconditional Green."}
{"row_type":"case","case_id":"C22_R6L137_004_HMF_20240308_LONGTERM_INSURANCE_SHOCK","symbol":"001450","company_name":"현대해상","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"C22-L137-T04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_error_or_guardrail_case","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A pure CSM/rate-cycle interpretation would have over-promoted the name; non-price margin/reserve deterioration needed to cap Stage2."}
{"row_type":"case","case_id":"C22_R6L137_005_HMF_20240814_2Q_CSM_QUALITY_LOSS_RATIO_BREAK","symbol":"001450","company_name":"현대해상","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"C22-L137-T05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_error_or_guardrail_case","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Forward 90D/180D MAE was severe and MFE stayed near zero; hard 4C needed when CSM headline is offset by underwriting/reserve quality risk."}
{"row_type":"case","case_id":"C22_R6L137_006_DBINS_20241114_3Q_CSM_HIGH_MAE","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C22-L137-T06","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_error_or_guardrail_case","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Structural success with deep interim MAE: Green should wait for drawdown-aware confirmation, not reject the case outright."}
{"row_type":"case","case_id":"C22_R6L137_007_SFMI_20250120_VALUEUP_KICS_RETURN_EXECUTION","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C22-L137-T07","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Here Value-up is not a slogan: K-ICS/ROE target plus cancellation roadmap made the capital-return bridge explicit."}
{"row_type":"trigger","trigger_id":"C22-L137-T01","case_id":"C22_R6L137_001_DBINS_20240222_IFRS17_CSM_CAPITAL_RETURN","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"sector_specific_rule_discovery;canonical_archetype_rule_candidate;counterexample_mining;4C_thesis_break_timing_test;complete_30_90_180_MFE_MAE","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":93600.0,"evidence_available_at_that_date":"FY2023 business results / 2024 outlook: IFRS17-era earnings, CSM, solvency and dividend/capital-return bridge","evidence_source":"https://www.idbins.com/pcweb/bizxpress/cmy/inv/ir/__etc/2023_business%20results_2024_outlook_ENG.pdf","stage2_evidence_fields":["public_event_or_disclosure","financial_visibility","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.52,"MFE_90D_pct":28.95,"MFE_180D_pct":32.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.67,"MAE_90D_pct":-7.91,"MAE_180D_pct":-7.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000.0,"drawdown_after_peak_pct":-19.76,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ifrs17_csm_capital_return_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage2-Actionable|2024-02-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C22-L137-T02","case_id":"C22_R6L137_002_SFMI_20240223_CSM_DPS_PAYOUT","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"sector_specific_rule_discovery;canonical_archetype_rule_candidate;counterexample_mining;4C_thesis_break_timing_test;complete_30_90_180_MFE_MAE","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":308500.0,"evidence_available_at_that_date":"Samsung Fire shareholder-return history plus 2023 CSM/sector leadership evidence; non-life leader quality and capital-return credibility","evidence_source":"https://www.samsungfire.com/company_eng/P_U01_08_05_480_4.html; https://www.asiae.co.kr/en/article/2024022308051029172","stage2_evidence_fields":["public_event_or_disclosure","financial_visibility","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.16,"MFE_90D_pct":27.55,"MFE_180D_pct":27.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.46,"MAE_90D_pct":-11.67,"MAE_180D_pct":-11.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":393500.0,"drawdown_after_peak_pct":-17.66,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"csm_dps_leader_quality_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|000810|Stage2-Actionable|2024-02-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C22-L137-T03","case_id":"C22_R6L137_003_SLIFE_20240220_HEALTH_CSM_KICS_VALUEUP_PENDING","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"sector_specific_rule_discovery;canonical_archetype_rule_candidate;counterexample_mining;4C_thesis_break_timing_test;complete_30_90_180_MFE_MAE","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":81700.0,"evidence_available_at_that_date":"FY2023 net profit + health-insurance CSM growth + K-ICS strength, but shareholder-return plan still pending","evidence_source":"https://www.mk.co.kr/en/economy/10947032","stage2_evidence_fields":["public_event_or_disclosure","financial_visibility","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","margin_bridge"],"stage4b_evidence_fields":["positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.8,"MFE_90D_pct":32.8,"MFE_180D_pct":32.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.35,"MAE_90D_pct":-6.24,"MAE_180D_pct":-6.24,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":108500.0,"drawdown_after_peak_pct":-29.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.33,"four_b_timing_verdict":"drawdown_watch_overlay","four_b_evidence_type":["positioning_overheat","explicit_event_cap"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"health_csm_kics_positive_but_event_cap","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|032830|Stage2-Actionable|2024-02-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C22-L137-T04","case_id":"C22_R6L137_004_HMF_20240308_LONGTERM_INSURANCE_SHOCK","symbol":"001450","company_name":"현대해상","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"sector_specific_rule_discovery;canonical_archetype_rule_candidate;counterexample_mining;4C_thesis_break_timing_test;complete_30_90_180_MFE_MAE","trigger_type":"Stage4B","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":31950.0,"evidence_available_at_that_date":"2023 result narrative: insurance profit deterioration and long-term insurance shock; CSM headline alone was not enough","evidence_source":"https://www.ibtomato.com/ExternalView.aspx?no=11715&type=1","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","accounting_or_trust_break","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.21,"MFE_90D_pct":12.21,"MFE_180D_pct":15.02,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.95,"MAE_90D_pct":-10.95,"MAE_180D_pct":-17.37,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":36750.0,"drawdown_after_peak_pct":-28.16,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.33,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["margin_or_backlog_slowdown","accounting_or_trust_break","explicit_event_cap"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"csm_headline_with_longterm_insurance_shock_4b","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|001450|Stage4B|2024-03-08","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C22-L137-T05","case_id":"C22_R6L137_005_HMF_20240814_2Q_CSM_QUALITY_LOSS_RATIO_BREAK","symbol":"001450","company_name":"현대해상","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"sector_specific_rule_discovery;canonical_archetype_rule_candidate;counterexample_mining;4C_thesis_break_timing_test;complete_30_90_180_MFE_MAE","trigger_type":"Stage4C","trigger_date":"2024-08-14","entry_date":"2024-08-14","entry_price":34950.0,"evidence_available_at_that_date":"Hyundai Marine official IR library lists 2024.2Q results dated 2024-08-14; subsequent path tested whether CSM quality without loss-ratio repair should remain capped","evidence_source":"https://www.hi.co.kr/serviceAction.do?view=bin/KC/IR/HHKCIR090M","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["accounting_or_trust_break","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.86,"MFE_90D_pct":4.86,"MFE_180D_pct":4.86,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.58,"MAE_90D_pct":-31.47,"MAE_180D_pct":-43.23,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-20","peak_price":36650.0,"drawdown_after_peak_pct":-45.87,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.33,"four_b_timing_verdict":"drawdown_watch_overlay","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"loss_ratio_reserve_quality_break_4c","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|001450|Stage4C|2024-08-14","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C22-L137-T06","case_id":"C22_R6L137_006_DBINS_20241114_3Q_CSM_HIGH_MAE","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"sector_specific_rule_discovery;canonical_archetype_rule_candidate;counterexample_mining;4C_thesis_break_timing_test;complete_30_90_180_MFE_MAE","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-14","entry_date":"2024-11-14","entry_price":105500.0,"evidence_available_at_that_date":"2024 3Q KPI: CSM amortization and cumulative long-term metrics improved, but entry was drawdown-sensitive before the 2025 rerating leg","evidence_source":"https://www.idbins.com/pcweb/bizxpress/cmy/inv/ir/__etc/2024.3Q_DB%20Insurance%281%29.pdf","stage2_evidence_fields":["public_event_or_disclosure","financial_visibility"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","margin_bridge"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.77,"MFE_90D_pct":7.77,"MFE_180D_pct":40.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.07,"MAE_90D_pct":-18.29,"MAE_180D_pct":-26.54,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-14","peak_price":148300.0,"drawdown_after_peak_pct":-17.94,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.33,"four_b_timing_verdict":"drawdown_watch_overlay","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"csm_amortization_positive_high_mae_confirmation_needed","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage3-Yellow|2024-11-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C22-L137-T07","case_id":"C22_R6L137_007_SFMI_20250120_VALUEUP_KICS_RETURN_EXECUTION","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_LOSS_RATIO_KICS_SHAREHOLDER_RETURN_GATE","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve","loop_objective":"sector_specific_rule_discovery;canonical_archetype_rule_candidate;counterexample_mining;4C_thesis_break_timing_test;complete_30_90_180_MFE_MAE","trigger_type":"Stage3-Green","trigger_date":"2025-01-20","entry_date":"2025-01-20","entry_price":358000.0,"evidence_available_at_that_date":"2025 value-up plan: mid/long-term K-ICS and ROE targets, progressive shareholder return toward 50%, and treasury-share cancellation roadmap","evidence_source":"https://www.samsungfire.com/download/company/sfmi_2025_vp_en.pdf","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","financial_visibility"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2025.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.41,"MFE_90D_pct":24.86,"MFE_180D_pct":46.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.03,"MAE_90D_pct":-8.66,"MAE_180D_pct":-8.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-14","peak_price":526000.0,"drawdown_after_peak_pct":-21.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"capital_return_execution_green_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|000810|Stage3-Green|2025-01-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L137_001_DBINS_20240222_IFRS17_CSM_CAPITAL_RETURN","trigger_id":"C22-L137-T01","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":14,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":12,"valuation_repricing_score":12,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"csm_quality_score":20,"loss_ratio_reserve_score":12,"kics_capital_score":15,"shareholder_return_execution_score":10},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":14,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":12,"valuation_repricing_score":12,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"csm_quality_score":21,"loss_ratio_reserve_score":12,"kics_capital_score":15,"shareholder_return_execution_score":12},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["csm_quality_score","loss_ratio_reserve_score","kics_capital_score","shareholder_return_execution_score","accounting_trust_risk_score"],"component_delta_explanation":"C22-specific shadow profile requires two-sided confirmation: CSM quality plus loss-ratio/reserve quality plus capital-return execution, rather than generic IFRS17/value-up vocabulary.","MFE_90D_pct":28.95,"MAE_90D_pct":-7.91,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L137_002_SFMI_20240223_CSM_DPS_PAYOUT","trigger_id":"C22-L137-T02","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":13,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":15,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"csm_quality_score":21,"loss_ratio_reserve_score":14,"kics_capital_score":17,"shareholder_return_execution_score":16},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":13,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":15,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"csm_quality_score":22,"loss_ratio_reserve_score":14,"kics_capital_score":17,"shareholder_return_execution_score":18},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["csm_quality_score","loss_ratio_reserve_score","kics_capital_score","shareholder_return_execution_score","accounting_trust_risk_score"],"component_delta_explanation":"C22-specific shadow profile requires two-sided confirmation: CSM quality plus loss-ratio/reserve quality plus capital-return execution, rather than generic IFRS17/value-up vocabulary.","MFE_90D_pct":27.55,"MAE_90D_pct":-11.67,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L137_003_SLIFE_20240220_HEALTH_CSM_KICS_VALUEUP_PENDING","trigger_id":"C22-L137-T03","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":12,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":18,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8,"csm_quality_score":18,"loss_ratio_reserve_score":8,"kics_capital_score":21,"shareholder_return_execution_score":6},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":12,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":18,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8,"csm_quality_score":19,"loss_ratio_reserve_score":8,"kics_capital_score":21,"shareholder_return_execution_score":8},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable+4B_watch","changed_components":["csm_quality_score","loss_ratio_reserve_score","kics_capital_score","shareholder_return_execution_score","accounting_trust_risk_score"],"component_delta_explanation":"C22-specific shadow profile requires two-sided confirmation: CSM quality plus loss-ratio/reserve quality plus capital-return execution, rather than generic IFRS17/value-up vocabulary.","MFE_90D_pct":32.8,"MAE_90D_pct":-6.24,"score_return_alignment_label":"residual_error_found","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L137_004_HMF_20240308_LONGTERM_INSURANCE_SHOCK","trigger_id":"C22-L137-T04","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":14,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":18,"csm_quality_score":10,"loss_ratio_reserve_score":-10,"kics_capital_score":12,"shareholder_return_execution_score":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":14,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":22,"csm_quality_score":10,"loss_ratio_reserve_score":-14,"kics_capital_score":12,"shareholder_return_execution_score":2},"weighted_score_after":59,"stage_label_after":"Stage4B","changed_components":["csm_quality_score","loss_ratio_reserve_score","kics_capital_score","shareholder_return_execution_score","accounting_trust_risk_score"],"component_delta_explanation":"C22-specific shadow profile requires two-sided confirmation: CSM quality plus loss-ratio/reserve quality plus capital-return execution, rather than generic IFRS17/value-up vocabulary.","MFE_90D_pct":12.21,"MAE_90D_pct":-10.95,"score_return_alignment_label":"residual_error_found","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L137_005_HMF_20240814_2Q_CSM_QUALITY_LOSS_RATIO_BREAK","trigger_id":"C22-L137-T05","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":10,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":24,"csm_quality_score":9,"loss_ratio_reserve_score":-18,"kics_capital_score":8,"shareholder_return_execution_score":3},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":10,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":28,"csm_quality_score":9,"loss_ratio_reserve_score":-22,"kics_capital_score":8,"shareholder_return_execution_score":1},"weighted_score_after":48,"stage_label_after":"Stage4C","changed_components":["csm_quality_score","loss_ratio_reserve_score","kics_capital_score","shareholder_return_execution_score","accounting_trust_risk_score"],"component_delta_explanation":"C22-specific shadow profile requires two-sided confirmation: CSM quality plus loss-ratio/reserve quality plus capital-return execution, rather than generic IFRS17/value-up vocabulary.","MFE_90D_pct":4.86,"MAE_90D_pct":-31.47,"score_return_alignment_label":"residual_error_found","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L137_006_DBINS_20241114_3Q_CSM_HIGH_MAE","trigger_id":"C22-L137-T06","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":13,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":13,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"csm_quality_score":20,"loss_ratio_reserve_score":9,"kics_capital_score":15,"shareholder_return_execution_score":8},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":17,"revision_score":13,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":13,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"csm_quality_score":21,"loss_ratio_reserve_score":9,"kics_capital_score":15,"shareholder_return_execution_score":10},"weighted_score_after":75,"stage_label_after":"Stage3-Yellow+drawdown_watch","changed_components":["csm_quality_score","loss_ratio_reserve_score","kics_capital_score","shareholder_return_execution_score","accounting_trust_risk_score"],"component_delta_explanation":"C22-specific shadow profile requires two-sided confirmation: CSM quality plus loss-ratio/reserve quality plus capital-return execution, rather than generic IFRS17/value-up vocabulary.","MFE_90D_pct":7.77,"MAE_90D_pct":-18.29,"score_return_alignment_label":"residual_error_found","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C22_R6L137_007_SFMI_20250120_VALUEUP_KICS_RETURN_EXECUTION","trigger_id":"C22-L137-T07","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":16,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"csm_quality_score":22,"loss_ratio_reserve_score":16,"kics_capital_score":22,"shareholder_return_execution_score":23},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":16,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"csm_quality_score":23,"loss_ratio_reserve_score":16,"kics_capital_score":22,"shareholder_return_execution_score":25},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["csm_quality_score","loss_ratio_reserve_score","kics_capital_score","shareholder_return_execution_score","accounting_trust_risk_score"],"component_delta_explanation":"C22-specific shadow profile requires two-sided confirmation: CSM quality plus loss-ratio/reserve quality plus capital-return execution, rather than generic IFRS17/value-up vocabulary.","MFE_90D_pct":24.86,"MAE_90D_pct":-8.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R6","loop":"137","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_confirmation","drawdown_aware_confirmation"],"residual_error_types_found":["CSM_headline_false_positive","loss_ratio_reserve_quality_break","capital_return_goal_without_execution","high_MAE_structural_success"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
- Production scoring must not change unless explicitly promoted.

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

## 27. Next Round State

```text
completed_round = R6
completed_loop = 137
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C22 insurance CSM/loss-ratio/K-ICS/shareholder-return execution split; 4C-thin path repair
next_recommended_archetypes = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION; C24_BIO_TRIAL_DATA_EVENT_RISK; C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT; C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
