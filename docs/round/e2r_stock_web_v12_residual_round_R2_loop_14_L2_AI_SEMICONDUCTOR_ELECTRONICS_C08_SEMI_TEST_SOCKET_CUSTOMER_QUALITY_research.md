# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH
output_file = e2r_stock_web_v12_residual_round_R2_loop_14_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

## 1. Current Calibrated Profile Assumption

The current default proxy is `e2r_2_1_stock_web_calibrated`. The already-applied axes are treated as fixed unless stress-tested: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min = 75`, `stage3_green_total_min = 87`, `stage3_green_revision_min = 55`, `stage3_cross_evidence_green_buffer`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`.

This MD does not re-argue those global axes. It tests a narrower C08 residual: **test-socket / probe-pin relative strength must be separated into durable customer-quality evidence versus theme-only or acquisition/valuation spikes**.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R2
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH
loop_objective = sector_specific_rule_discovery | counterexample_mining | 4B_non_price_requirement_stress_test | green_strictness_stress_test | coverage_gap_fill
```

R2 is consistent with L2. C08 is used instead of C07 because the case set is centered on socket / probe / interface-board quality rather than HBM bonder order conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only as a coverage / duplicate-avoidance signal. No `src/e2r` code was opened. The conversation-local previous v12 state ended at R1 / loop 14 and pointed to R2 / loop 14. The repository registry available during the run contained historical calibration rounds but did not expose a complete v12 filename registry in the allowed chunk, so this MD follows the prior `next_round` state and writes R2 / loop 14.

Duplicate avoidance outcome:

- same symbol + same trigger date + same entry group repeated: `false`
- new independent C08 symbols: `4`
- new trigger families: `5` including one 4B overlay row
- reused representative cases: `0`

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The manifest reports `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, and the calibration shard root under `atlas/ohlcv_tradable_by_symbol_year`. The schema confirms the tradable columns `d,o,h,l,c,v,a,mc,s,m` and the MFE/MAE formula using max high / min low from tradable rows.

## 5. Historical Eligibility Gate

All representative triggers below are historical, have an entry row in the tradable shard, have at least 180 forward trading days before the stock-web manifest max date, and have no corporate-action candidate inside the representative entry-to-D+180 window.

| case_id | symbol | entry_date | price_shard | profile | 180D status | corporate action status |
| --- | --- | --- | --- | --- | --- | --- |
| R2L14_C08_058470_LEENO_20240122 | 058470 | 2024-01-22 | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/symbol_profiles/058/058470.json | usable | clean_180D_window |
| R2L14_C08_131290_TSE_20240222 | 131290 | 2024-02-22 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json | usable | clean_180D_window |
| R2L14_C08_095340_ISC_20240311 | 095340 | 2024-03-11 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json | usable | clean_180D_window |
| R2L14_C08_098120_MICROCONTACT_20240122 | 098120 | 2024-01-22 | atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv | atlas/symbol_profiles/098/098120.json | usable | clean_180D_window |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | The signal is not generic semiconductor equipment; the decisive axis is customer-quality and socket/probe durability. |
| THEME_ONLY_SMALL_CAP_SOCKET_SYMPATHY | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Kept inside C08 as a counterexample guard, not as a separate positive archetype. |
| VALUATION_SPIKE_WITHOUT_CUSTOMER_CONVERSION | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | A C08-specific residual error: valuation and acquisition narrative can mimic socket quality. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | best_trigger | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R2L14_C08_058470_LEENO_20240122 | 058470 | 리노공업 | high_mae_success | positive | T_R2L14_058470_STAGE2A_20240122 | current_profile_too_early |
| R2L14_C08_131290_TSE_20240222 | 131290 | 티에스이 | structural_success | positive | T_R2L14_131290_STAGE2A_20240222 | current_profile_correct |
| R2L14_C08_095340_ISC_20240311 | 095340 | ISC | false_positive_green | counterexample | T_R2L14_095340_STAGE2A_20240311 | current_profile_false_positive |
| R2L14_C08_098120_MICROCONTACT_20240122 | 098120 | 마이크로컨텍솔 | failed_rerating | counterexample | T_R2L14_098120_STAGE2A_20240122 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
representative_trigger_count = 4
4B_overlay_trigger_count = 1
minimum_new_independent_case_ratio = 1.00
```

The balance is deliberate: 리노공업 and 티에스이 show that customer-quality socket/probe exposure can work, but ISC and 마이크로컨텍솔 show that a valuation or theme-only spike can imitate the same surface pattern and then suffer high MAE.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B / 4C evidence |
|---|---|---|---|
| R2L14_C08_058470_LEENO_20240122 | customer quality, relative strength, early revision | financial visibility, low red-team risk | watch only |
| R2L14_C08_131290_TSE_20240222 | customer/order quality, relative strength, volume route | repeat conversion, financial visibility | later 4B overlay row |
| R2L14_C08_095340_ISC_20240311 | customer-quality narrative, relative strength | multiple sources but not enough confirmed conversion | valuation blowoff / price-only local peak |
| R2L14_C08_098120_MICROCONTACT_20240122 | relative strength only | none | price-only local peak, thesis evidence broken |

## 10. Price Data Source Map

| symbol | company | tradable shard | profile | price basis |
| --- | --- | --- | --- | --- |
| 058470 | 리노공업 | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/symbol_profiles/058/058470.json | tradable_raw / raw_unadjusted_marcap |
| 131290 | 티에스이 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json | tradable_raw / raw_unadjusted_marcap |
| 095340 | ISC | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json | tradable_raw / raw_unadjusted_marcap |
| 098120 | 마이크로컨텍솔 | atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv | atlas/symbol_profiles/098/098120.json | tradable_raw / raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_R2L14_058470_STAGE2A_20240122 | 058470 | 리노공업 | Stage2-Actionable | 2024-01-22 | 234000 | 32.05 | -19.7 | 32.05 | -19.7 | current_profile_too_early | representative |
| T_R2L14_131290_STAGE2A_20240222 | 131290 | 티에스이 | Stage2-Actionable | 2024-02-22 | 61300 | 43.23 | -13.54 | 43.23 | -24.39 | current_profile_correct | representative |
| T_R2L14_095340_STAGE2A_20240311 | 095340 | ISC | Stage2-Actionable | 2024-03-11 | 93700 | 15.26 | -35.86 | 15.26 | -56.14 | current_profile_false_positive | representative |
| T_R2L14_098120_STAGE2A_20240122 | 098120 | 마이크로컨텍솔 | Stage2-Actionable | 2024-01-22 | 12770 | 3.37 | -30.62 | 3.37 | -30.62 | current_profile_false_positive | representative |
| T_R2L14_131290_4B_20240503 | 131290 | 티에스이 | Stage4B-overlay | 2024-05-03 | 80000 | 9.75 | -42.06 | 9.75 | -42.06 | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_R2L14_058470_STAGE2A_20240122 | 2024-01-22 | 234000 | 1.92 | -19.7 | 32.05 | -19.7 | 32.05 | -19.7 | 2024-05-07 | 309000 | -30.58 |
| T_R2L14_131290_STAGE2A_20240222 | 2024-02-22 | 61300 | 12.89 | -10.28 | 43.23 | -13.54 | 43.23 | -24.39 | 2024-05-03 | 87800 | -47.21 |
| T_R2L14_095340_STAGE2A_20240311 | 2024-03-11 | 93700 | 15.26 | -17.93 | 15.26 | -35.86 | 15.26 | -56.14 | 2024-03-28 | 108000 | -61.94 |
| T_R2L14_098120_STAGE2A_20240122 | 2024-01-22 | 12770 | 3.37 | -21.85 | 3.37 | -30.62 | 3.37 | -30.62 | 2024-01-25 | 13200 | -32.88 |
| T_R2L14_131290_4B_20240503 | 2024-05-03 | 80000 | 9.75 | -23.88 | 9.75 | -42.06 | 9.75 | -42.06 | 2024-05-03 | 87800 | -47.21 |

## 13. Current Calibrated Profile Stress Test

The current profile was broadly correct on the durable customer-quality positives, but still too permissive for theme-only or valuation-heavy socket narratives.

| question | finding |
|---|---|
| Did Stage2 bonus help? | Yes for 리노공업 / 티에스이; too generous for 마이크로컨텍솔. |
| Was Yellow threshold 75 enough? | It separated some positives, but ISC still sits near a false-positive Green boundary. |
| Was Green threshold 87 / revision 55 too strict? | Not too strict; C08 needs a customer-quality sub-gate before Green. |
| Was price-only blowoff guard appropriate? | Yes, strengthened by ISC and TSE 4B overlay. |
| Was full 4B non-price requirement appropriate? | Yes; TSE 4B row had local timing but lacked non-price deterioration proof. |
| Was hard 4C routing too late? | Not on 마이크로컨텍솔; theme-only failure should route to 4C/watch earlier. |

## 14. Stage2 / Yellow / Green Comparison

Green lateness was not the central residual here. The residual is more like a metal detector: the same “relative strength” beep can come from gold or scrap. Customer-quality proof is the second detector.

| case | Stage2 Actionable entry | likely Green condition | green_lateness_ratio | interpretation |
|---|---:|---|---:|---|
| 리노공업 | 234000 | customer quality + financial visibility | 0.18 | Green not badly late, but MAE is high. |
| 티에스이 | 61300 | customer quality + conversion proof | 0.34 | Some lateness, still acceptable. |
| ISC | 93700 | should not Green without customer conversion | 0.72 | Green would be too late / too close to spike. |
| 마이크로컨텍솔 | 12770 | no confirmed Green trigger | N/A | Theme-only row should not promote. |

## 15. 4B Local vs Full-window Timing Audit

The TSE overlay shows why local peak proximity alone is not enough. The 4B entry on 2024-05-03 was near the local/full-window peak, but the evidence type was price-only. Under the current calibrated profile, this remains a 4B watch overlay rather than a full 4B thesis exit.

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | verdict |
| --- | --- | --- | --- | --- |
| T_R2L14_095340_STAGE2A_20240311 | 0.8 | 0.8 | price_only,valuation_blowoff | price_only_local_4B_too_early_without_non_price_confirmation |
| T_R2L14_098120_STAGE2A_20240122 | 0.0 | 0.0 | price_only | price_only_local_4B_too_early |
| T_R2L14_131290_4B_20240503 | 0.71 | 0.71 | price_only,valuation_blowoff | local_peak_timing_good_but_price_only_not_full_4B |

## 16. 4C Protection Audit

마이크로컨텍솔 is the cleanest 4C protection example in this loop: once the row remained theme-only and failed to add customer-quality evidence, the drawdown profile showed that watch/4C protection would have been useful. ISC is a watch-only thesis-break row rather than a hard 4C, because the business narrative was not proven false; the price row mainly says the entry was too hot.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = false`.

The finding sits inside R2, but the sample is still one canonical cluster. It should not become a broad L2 rule for all AI/semiconductor names.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

Candidate C08 shadow rule:

```text
if canonical_archetype_id == C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY:
    require customer_quality_score >= 14 for Stage3-Green eligibility
    if relative_strength_score is high but customer_quality_score < 8:
        cap positive stage at Stage2-Watch or Stage2-Actionable
    if valuation_repricing_score is high and repeat_order_or_conversion evidence is absent:
        apply valuation_spike_without_conversion_penalty
```

## 19. Before / After Backtest Comparison

| profile_id | scope | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_default | 23.48 | -24.93 | 23.48 | -32.71 | 0.5 | mixed; too much credit to theme-only relative strength |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 23.48 | -24.93 | 23.48 | -32.71 | 0.75 | worse; over-promotes price-only socket themes |
| P1_L2_sector_specific_candidate_profile | sector_specific | 22.57 | -16.62 | 37.64 | -22.05 | 0.25 | better, but scope should stay canonical unless more R2 names confirm |
| P2_C08_canonical_archetype_candidate_profile | canonical_archetype_specific | 22.57 | -16.62 | 37.64 | -22.05 | 0.0 | best shadow profile for this MD |
| P3_counterexample_guard_profile | counterexample_guard | 9.31 | -33.24 | 9.31 | -43.38 | 0.0 | use as guard, not positive profile |

## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | MFE90 / MAE90 | alignment |
|---|---|---|---|---|
| 리노공업 | 76.5 / Stage3-Yellow | 80.5 / Stage3-Yellow | 32.05 / -19.70 | positive but high-MAE |
| 티에스이 | 78.0 / Stage3-Yellow | 82.0 / Stage3-Yellow | 43.23 / -13.54 | aligned |
| ISC | 86.0 / near Green | 74.0 / Stage2-Actionable | 15.26 / -35.86 | guard needed |
| 마이크로컨텍솔 | 73.0 / Stage2-Actionable | 62.0 / Stage2-Watch | 3.37 / -30.62 | guard needed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH | 2 | 2 | 2 | 1 | 4 | 0 | 5 | 4 | 2 | False | True | C08 now has positive/counterexample balance; still needs non-KOSDAQ large-cap memory interface holdout. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: theme_only_socket_false_positive, valuation_spike_without_customer_conversion, high_MAE_success_needs_position_sizing_guard
new_axis_proposed: C08_customer_quality_min, C08_theme_only_relative_strength_block, C08_valuation_spike_without_conversion_penalty
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-web manifest/schema/universe availability.
- 4 representative historical entry rows and one 4B overlay row.
- 30D / 90D / 180D MFE and MAE from tradable_raw OHLC rows.
- Corporate-action window status at profile level.
- Current calibrated profile stress-test labels.

Not validated:

- No live candidate scan.
- No current recommendation.
- No `stock_agent` source-code inspection or patching.
- No broker or auto-trading integration.
- No production score change.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_min,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,10,14,+4,"Durable customer-quality evidence separated 리노공업/티에스이 from ISC/마이크로컨텍솔 counterexamples","false_positive_rate fell from 0.50 to 0.00 in P2","T_R2L14_058470_STAGE2A_20240122|T_R2L14_131290_STAGE2A_20240222|T_R2L14_095340_STAGE2A_20240311|T_R2L14_098120_STAGE2A_20240122",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C08_theme_only_relative_strength_block,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,true,true,0,"Theme-only socket relative strength caused high-MAE failed rerating in small-cap case","guards MicroContactsol-like rows from Stage3 promotion","T_R2L14_098120_STAGE2A_20240122",1,1,1,medium,canonical_shadow_only,"existing price-only blowoff guard strengthened, not global delta"
shadow_weight,C08_valuation_spike_without_conversion_penalty,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,-6,-6,"ISC showed valuation / acquisition narrative spike without enough conversion evidence","reduces near-Green false positive","T_R2L14_095340_STAGE2A_20240311",1,1,1,low,canonical_shadow_only,"do not apply globally"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R2L14_C08_058470_LEENO_20240122","symbol":"058470","company_name":"리노공업","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T_R2L14_058470_STAGE2A_20240122","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"AI/HBM-facing test socket and probe-pin demand narrative with durable customer-quality reputation; price row used only after non-price business-quality evidence existed."}
{"row_type":"case","case_id":"R2L14_C08_131290_TSE_20240222","symbol":"131290","company_name":"티에스이","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R2L14_131290_STAGE2A_20240222","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Probe card / interface-board / socket exposure began to price with AI-memory test-chain relative strength; customer-quality evidence was present but less durable than pure socket leaders."}
{"row_type":"case","case_id":"R2L14_C08_095340_ISC_20240311","symbol":"095340","company_name":"ISC","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T_R2L14_095340_STAGE2A_20240311","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_error","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Post-acquisition socket narrative and HBM exposure were visible, but the row shows the trigger was already near a short-window spike; customer-conversion proof was not enough for Green."}
{"row_type":"case","case_id":"R2L14_C08_098120_MICROCONTACT_20240122","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R2L14_098120_STAGE2A_20240122","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_error","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Socket-theme sympathy and small-cap relative strength existed, but no durable top-tier customer-quality route was visible enough to justify Stage3-Green."}
{"row_type":"trigger","trigger_id":"T_R2L14_058470_STAGE2A_20240122","case_id":"R2L14_C08_058470_LEENO_20240122","symbol":"058470","company_name":"리노공업","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":234000,"evidence_available_at_that_date":"AI/HBM-facing test socket and probe-pin demand narrative with durable customer-quality reputation; price row used only after non-price business-quality evidence existed.","evidence_source":"historical public disclosure / IR / market report evidence label; OHLC from stock-web","stage2_evidence_fields":["customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.92,"MFE_90D_pct":32.05,"MFE_180D_pct":32.05,"MFE_1Y_pct":32.05,"MFE_2Y_pct":null,"MAE_30D_pct":-19.7,"MAE_90D_pct":-19.7,"MAE_180D_pct":-19.7,"MAE_1Y_pct":-30.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-30.58,"green_lateness_ratio":0.18,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_MAE_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L14_C08_058470_LEENO_20240122_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R2L14_131290_STAGE2A_20240222","case_id":"R2L14_C08_131290_TSE_20240222","symbol":"131290","company_name":"티에스이","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":61300,"evidence_available_at_that_date":"Probe card / interface-board / socket exposure began to price with AI-memory test-chain relative strength; customer-quality evidence was present but less durable than pure socket leaders.","evidence_source":"historical public disclosure / IR / market report evidence label; OHLC from stock-web","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.89,"MFE_90D_pct":43.23,"MFE_180D_pct":43.23,"MFE_1Y_pct":43.23,"MFE_2Y_pct":null,"MAE_30D_pct":-10.28,"MAE_90D_pct":-13.54,"MAE_180D_pct":-24.39,"MAE_1Y_pct":-24.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-47.21,"green_lateness_ratio":0.34,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_but_cycle_peak_fast","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L14_C08_131290_TSE_20240222_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R2L14_095340_STAGE2A_20240311","case_id":"R2L14_C08_095340_ISC_20240311","symbol":"095340","company_name":"ISC","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-11","entry_date":"2024-03-11","entry_price":93700,"evidence_available_at_that_date":"Post-acquisition socket narrative and HBM exposure were visible, but the row shows the trigger was already near a short-window spike; customer-conversion proof was not enough for Green.","evidence_source":"historical public disclosure / IR / market report evidence label; OHLC from stock-web","stage2_evidence_fields":["customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.26,"MFE_90D_pct":15.26,"MFE_180D_pct":15.26,"MFE_1Y_pct":15.26,"MFE_2Y_pct":null,"MAE_30D_pct":-17.93,"MAE_90D_pct":-35.86,"MAE_180D_pct":-56.14,"MAE_1Y_pct":-56.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-61.94,"green_lateness_ratio":0.72,"four_b_local_peak_proximity":0.8,"four_b_full_window_peak_proximity":0.8,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_confirmation","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L14_C08_095340_ISC_20240311_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R2L14_098120_STAGE2A_20240122","case_id":"R2L14_C08_098120_MICROCONTACT_20240122","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":12770,"evidence_available_at_that_date":"Socket-theme sympathy and small-cap relative strength existed, but no durable top-tier customer-quality route was visible enough to justify Stage3-Green.","evidence_source":"historical public disclosure / IR / market report evidence label; OHLC from stock-web","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv","profile_path":"atlas/symbol_profiles/098/098120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.37,"MFE_90D_pct":3.37,"MFE_180D_pct":3.37,"MFE_1Y_pct":3.37,"MFE_2Y_pct":null,"MAE_30D_pct":-21.85,"MAE_90D_pct":-30.62,"MAE_180D_pct":-30.62,"MAE_1Y_pct":-30.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-25","peak_price":13200,"drawdown_after_peak_pct":-32.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"counterexample_theme_only_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L14_C08_098120_MICROCONTACT_20240122_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R2L14_131290_4B_20240503","case_id":"R2L14_C08_131290_TSE_20240222","symbol":"131290","company_name":"티에스이","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_TEST_SOCKET_CUSTOMER_QUALITY_RELATIVE_STRENGTH","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill","trigger_type":"Stage4B-overlay","trigger_date":"2024-05-03","entry_date":"2024-05-03","entry_price":80000,"evidence_available_at_that_date":"Local price blowoff after the Stage2-Actionable row; no separate non-price deterioration was available at the 4B date.","evidence_source":"historical public disclosure / IR / market report evidence label; OHLC from stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.75,"MFE_90D_pct":9.75,"MFE_180D_pct":9.75,"MFE_1Y_pct":9.75,"MFE_2Y_pct":null,"MAE_30D_pct":-23.88,"MAE_90D_pct":-42.06,"MAE_180D_pct":-42.06,"MAE_1Y_pct":-42.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-47.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.71,"four_b_full_window_peak_proximity":0.71,"four_b_timing_verdict":"local_peak_timing_good_but_price_only_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_price_only_limited","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L14_C08_131290_TSE_20240222_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, different trigger family for 4B timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C08_058470_LEENO_20240122","trigger_id":"T_R2L14_058470_STAGE2A_20240122","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":14,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"test_socket_quality_score":18,"customer_concentration_visibility_score":9},"weighted_score_before":76.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":14,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"test_socket_quality_score":20,"customer_concentration_visibility_score":9},"weighted_score_after":80.5,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","test_socket_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile separates durable customer-quality sockets/probe pins from theme-only relative strength or acquisition/valuation spikes.","MFE_90D_pct":32.05,"MAE_90D_pct":-19.7,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C08_131290_TSE_20240222","trigger_id":"T_R2L14_131290_STAGE2A_20240222","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":10,"relative_strength_score":17,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"test_socket_quality_score":15,"customer_concentration_visibility_score":7},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":10,"relative_strength_score":17,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"test_socket_quality_score":17,"customer_concentration_visibility_score":7},"weighted_score_after":82.0,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","test_socket_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile separates durable customer-quality sockets/probe pins from theme-only relative strength or acquisition/valuation spikes.","MFE_90D_pct":43.23,"MAE_90D_pct":-13.54,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C08_095340_ISC_20240311","trigger_id":"T_R2L14_095340_STAGE2A_20240311","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":7,"relative_strength_score":18,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"test_socket_quality_score":12,"customer_concentration_visibility_score":3},"weighted_score_before":86.0,"stage_label_before":"Stage3-Yellow_near_Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":7,"relative_strength_score":18,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":-13,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"test_socket_quality_score":8,"customer_concentration_visibility_score":3},"weighted_score_after":74.0,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","test_socket_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile separates durable customer-quality sockets/probe pins from theme-only relative strength or acquisition/valuation spikes.","MFE_90D_pct":15.26,"MAE_90D_pct":-35.86,"score_return_alignment_label":"guard_needed_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C08_098120_MICROCONTACT_20240122","trigger_id":"T_R2L14_098120_STAGE2A_20240122","symbol":"098120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":15,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"test_socket_quality_score":4,"customer_concentration_visibility_score":0},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"test_socket_quality_score":0,"customer_concentration_visibility_score":0},"weighted_score_after":62.0,"stage_label_after":"Stage2-Watch","changed_components":["customer_quality_score","test_socket_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile separates durable customer-quality sockets/probe pins from theme-only relative strength or acquisition/valuation spikes.","MFE_90D_pct":3.37,"MAE_90D_pct":-30.62,"score_return_alignment_label":"guard_needed_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"profile_comparison","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default","profile_hypothesis":"Current global profile with Stage2 bonus and Green strictness.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative only","avg_MFE_90D_pct":23.48,"avg_MAE_90D_pct":-24.93,"avg_MFE_180D_pct":23.48,"avg_MAE_180D_pct":-32.71,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.41,"avg_four_b_local_peak_proximity":0.5,"avg_four_b_full_window_peak_proximity":0.5,"score_return_alignment_verdict":"mixed; too much credit to theme-only relative strength"}
{"row_type":"profile_comparison","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Old baseline without v2.1 calibrated guardrails.","changed_axes":["rollback_reference_only"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative only","avg_MFE_90D_pct":23.48,"avg_MAE_90D_pct":-24.93,"avg_MFE_180D_pct":23.48,"avg_MAE_180D_pct":-32.71,"false_positive_rate":0.75,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":0.39,"avg_four_b_local_peak_proximity":0.5,"avg_four_b_full_window_peak_proximity":0.5,"score_return_alignment_verdict":"worse; over-promotes price-only socket themes"}
{"row_type":"profile_comparison","profile_id":"P1_L2_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"Within AI/semiconductor, require customer-quality proof before allowing Stage3 promotion for test-socket names.","changed_axes":["customer_quality_confirmation_gate","valuation_spike_haircut"],"changed_thresholds":{"theme_only_relative_strength_max_stage":"Stage2-Watch"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative only","avg_MFE_90D_pct":22.57,"avg_MAE_90D_pct":-16.62,"avg_MFE_180D_pct":37.64,"avg_MAE_180D_pct":-22.05,"false_positive_rate":0.25,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.26,"avg_four_b_local_peak_proximity":0.5,"avg_four_b_full_window_peak_proximity":0.5,"score_return_alignment_verdict":"better, but scope should stay canonical unless more R2 names confirm"}
{"row_type":"profile_comparison","profile_id":"P2_C08_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C08 should score durable customer-quality sockets higher, and haircut acquisition/theme-only relative strength.","changed_axes":["test_socket_customer_quality_min","theme_only_socket_block","valuation_without_conversion_penalty"],"changed_thresholds":{"C08_Green_requires_customer_quality_score_min":14},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative only","avg_MFE_90D_pct":22.57,"avg_MAE_90D_pct":-16.62,"avg_MFE_180D_pct":37.64,"avg_MAE_180D_pct":-22.05,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.26,"avg_four_b_local_peak_proximity":0.5,"avg_four_b_full_window_peak_proximity":0.5,"score_return_alignment_verdict":"best shadow profile for this MD"}
{"row_type":"profile_comparison","profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"Reject Stage3 promotion when relative strength is unsupported by customer-conversion or margin/revision proof.","changed_axes":["theme_only_block","execution_risk_penalty"],"changed_thresholds":{"C08_theme_only_promote_allowed":false},"eligible_trigger_count":4,"selected_entry_trigger_per_case":"representative only","avg_MFE_90D_pct":9.31,"avg_MAE_90D_pct":-33.24,"avg_MFE_180D_pct":9.31,"avg_MAE_180D_pct":-43.38,"false_positive_rate":0.0,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":0.72,"avg_four_b_local_peak_proximity":0.4,"avg_four_b_full_window_peak_proximity":0.4,"score_return_alignment_verdict":"use as guard, not positive profile"}
{"row_type":"residual_contribution","round":"R2","loop":"14","scheduled_round":"R2","scheduled_loop":"14","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["theme_only_socket_false_positive","valuation_spike_without_customer_conversion","high_MAE_success_needs_position_sizing_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"4 new C08 symbols, 5 trigger families, 2 positive + 2 counterexamples"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_min,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,10,14,+4,"Durable customer-quality evidence separated 리노공업/티에스이 from ISC/마이크로컨텍솔 counterexamples","false_positive_rate fell from 0.50 to 0.00 in P2","T_R2L14_058470_STAGE2A_20240122|T_R2L14_131290_STAGE2A_20240222|T_R2L14_095340_STAGE2A_20240311|T_R2L14_098120_STAGE2A_20240122",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C08_theme_only_relative_strength_block,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,true,true,0,"Theme-only socket relative strength caused high-MAE failed rerating in small-cap case","guards MicroContactsol-like rows from Stage3 promotion","T_R2L14_098120_STAGE2A_20240122",1,1,1,medium,canonical_shadow_only,"existing price-only blowoff guard strengthened, not global delta"
shadow_weight,C08_valuation_spike_without_conversion_penalty,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,-6,-6,"ISC showed valuation / acquisition narrative spike without enough conversion evidence","reduces near-Green false positive","T_R2L14_095340_STAGE2A_20240311",1,1,1,low,canonical_shadow_only,"do not apply globally"
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
completed_round = R2
completed_loop = 14
next_round = R3
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Primary price atlas: `Songdaiki/stock-web`.
- Manifest max date used for forward-window availability: `2026-02-20`.
- Price basis: `tradable_raw`; adjustment status: `raw_unadjusted_marcap`.
- Representative price shards used: `058/058470/2024.csv`, `131/131290/2024.csv`, `095/095340/2024.csv`, `098/098120/2024.csv`.
- Symbol profiles used: `058/058470.json`, `131/131290.json`, `095/095340.json`, `098/098120.json`.
- The external business-evidence labels are historical labels for calibration context, not live recommendation research.

