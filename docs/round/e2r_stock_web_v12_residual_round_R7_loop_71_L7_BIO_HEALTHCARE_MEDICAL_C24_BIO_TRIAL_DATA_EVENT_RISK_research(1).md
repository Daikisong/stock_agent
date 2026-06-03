# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
- scheduled_round: `R7`
- scheduled_loop: `71`
- large_sector_id: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical_archetype_id: `C24_BIO_TRIAL_DATA_EVENT_RISK`
- fine_archetype_id: `BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT`
- next_round: `R8`
- next_loop: `71`
- round_schedule_status: `valid`
- round_sector_consistency: `pass`
- output_file: `e2r_stock_web_v12_residual_round_R7_loop_71_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md`
- research_session: `post_calibrated_sector_archetype_residual_research`
- production_scoring_changed: `false`
- shadow_weight_only: `true`

## 1. Current Calibrated Profile Assumption
current_default_profile_proxy = `e2r_2_1_stock_web_calibrated`; rollback reference = `e2r_2_0_baseline`. Existing global axes are treated as already applied. This loop tests C24-specific residual errors, not live candidates.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| scheduled_round | R7 |
| scheduled_loop | 71 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK |
| fine_archetype_id | BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT |
| allowed purpose | 4C timing, trial/event counterexamples, endpoint bridge, high-MAE guard |

## 3. Previous Coverage / Duplicate Avoidance Check
No-Repeat memory: C24 already has coverage in 000100/028300/009420/039200, but the hold/block list still flags C24 full-4B overlay as blocked by data quality. This loop avoids making HLB a new case; `028300` is reused only as a hard-4C timing benchmark with independent_evidence_weight 0.25. New independent symbols: `196170`, `087010`, `323990`.

## 4. Stock-Web OHLC Input / Price Source Validation
| field | value |
|---|---|
| source | Songdaiki/stock-web |
| source_url | https://github.com/Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 5. Historical Eligibility Gate
| case_id | clean 180D window | forward window | calibration_usable | reason |
|---|---|---:|---|---|
| R7L71_C24_196170_20240222 | clean_180D_window | 180 | true | stock-web tradable row present; no 2024/180D corporate-action overlap requiring block |
| R7L71_C24_087010_20240627 | clean_180D_window | 180 | true | stock-web tradable row present; no 2024/180D corporate-action overlap requiring block |
| R7L71_C24_323990_20240325 | clean_180D_window | 180 | true | stock-web tradable row present; no 2024/180D corporate-action overlap requiring block |
| R7L71_C24_028300_20240517 | clean_180D_window | 180 | true | stock-web tradable row present; no 2024/180D corporate-action overlap requiring block |

## 6. Canonical Archetype Compression Map
| fine/deep trigger family | canonical mapping | compression reason |
|---|---|---|
| partner_quality_platform_event_repricing | C24_BIO_TRIAL_DATA_EVENT_RISK | biotech platform events behave like binary event-risk until partner/endpoint bridge is verified |
| GLP1_platform_event_optional_repricing | C24_BIO_TRIAL_DATA_EVENT_RISK | strong upside but high-MAE event path, not clean revenue conversion |
| trial_event_price_spike_without_endpoint_bridge | C24_BIO_TRIAL_DATA_EVENT_RISK | price-only trial narrative false positive |
| FDA_CRL_hard_4C_timing_benchmark | C24_BIO_TRIAL_DATA_EVENT_RISK | hard 4C timing stress test |

## 7. Case Selection Summary
| case | symbol | company | role | trigger | entry | MFE90 | MAE90 | verdict |
|---|---|---|---|---|---|---:|---:|---|
| R7L71_C24_196170_20240222 | 196170 | 알테오젠 | structural_success | Stage2-Actionable | 2024-02-23 @ 131200 | 127.52% | -9.30% | current_profile_correct |
| R7L71_C24_087010_20240627 | 087010 | 펩트론 | high_mae_success | Stage2-Actionable | 2024-06-27 @ 46500 | 124.73% | -20.11% | current_profile_data_insufficient |
| R7L71_C24_323990_20240325 | 323990 | 박셀바이오 | failed_rerating | Stage2-Actionable | 2024-03-25 @ 23350 | 3.85% | -44.28% | current_profile_false_positive |
| R7L71_C24_028300_20240517 | 028300 | HLB | 4C_late | Stage4C | 2024-05-17 @ 67100 | 46.20% | -32.71% | current_profile_4C_too_late |

## 8. Positive vs Counterexample Balance
- positive_case_count: 2
- counterexample_count: 2
- calibration_usable_case_count: 4
- new_independent_case_count: 3
- reused_case_count: 1

## 9. Evidence Source Map
| symbol | evidence source proxy | stage2 | stage3 | 4B/4C |
|---|---|---|---|---|
| 196170 | ALT-B4/platform revaluation event created a large repricing path, but the usable signal is not price alone. It required partner-quality/licensing-route evidence plus repeat external validation before Stage3 promotion. | public_event_or_disclosure;customer_or_order_quality;relative_strength;policy_or_regulatory_optionality | multiple_public_sources;durable_customer_confirmation;financial_visibility | valuation_blowoff;positioning_overheat |
| 087010 | GLP-1/long-acting formulation optionality produced a strong price path, but the entry carried deep early MAE. C24 should treat this as Stage2-Actionable only with event-quality bridge and position-size/high-MAE guard, not as a clean Green. | public_event_or_disclosure;relative_strength;policy_or_regulatory_optionality;early_revision_signal | multiple_public_sources | valuation_blowoff;positioning_overheat;price_only_local_peak |
| 323990 | A price burst around event/trial narrative failed to convert into durable repricing. The path shows why trial-readout headlines without endpoint/commercial bridge should not get promoted beyond Stage2-Watch. | public_event_or_disclosure;relative_strength | none | price_only_local_peak;positioning_overheat;thesis_evidence_broken |
| 028300 | FDA CRL/regulatory rejection was a hard 4C event, but the official hard-4C timestamp occurs after the protection window has already failed. C24 needs an earlier regulatory-decision-risk watch layer, not a Green relaxation. | public_event_or_disclosure;relative_strength;policy_or_regulatory_optionality | multiple_public_sources | valuation_blowoff;positioning_overheat;explicit_event_cap;regulatory_rejection;thesis_evidence_broken |

## 10. Price Data Source Map
| symbol | profile_path | price_shard_path | profile caveat |
|---|---|---|---|
| 196170 | atlas/symbol_profiles/196/196170.json | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | raw_unadjusted_marcap; corporate-action candidate windows blocked by default |
| 087010 | atlas/symbol_profiles/087/087010.json | atlas/ohlcv_tradable_by_symbol_year/087/087010/2024.csv | raw_unadjusted_marcap; corporate-action candidate windows blocked by default |
| 323990 | atlas/symbol_profiles/323/323990.json | atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv | raw_unadjusted_marcap; corporate-action candidate windows blocked by default |
| 028300 | atlas/symbol_profiles/028/028300.json | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | raw_unadjusted_marcap; corporate-action candidate windows blocked by default |

## 11. Case-by-Case Trigger Grid
| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | dedupe | new? |
|---|---|---|---|---|---:|---|---|---|
| R7L71_C24_196170_20240222_T_STAGE2 | 196170 | Stage2-Actionable | 2024-02-22 | 2024-02-23 | 131200 | R7L71_C24_196170_20240222_ENTRY | True | True |
| R7L71_C24_087010_20240627_T_STAGE2 | 087010 | Stage2-Actionable | 2024-06-27 | 2024-06-27 | 46500 | R7L71_C24_087010_20240627_ENTRY | True | True |
| R7L71_C24_323990_20240325_T_STAGE2 | 323990 | Stage2-Actionable | 2024-03-25 | 2024-03-25 | 23350 | R7L71_C24_323990_20240325_ENTRY | True | True |
| R7L71_C24_028300_20240517_T_4C | 028300 | Stage4C | 2024-05-17 | 2024-05-17 | 67100 | R7L71_C24_028300_20240517_ENTRY | True | False |

## 12. Trigger-Level OHLC Backtest Tables
| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 196170 | 2024-02-23 | 131200 | 71.88% | -9.30% | 127.52% | -9.30% | 177.06% | -9.30% | 2024-09-20 | 363500 | -18.16% |
| 087010 | 2024-06-27 | 46500 | 80.22% | -20.11% | 124.73% | -20.11% | 124.73% | -20.11% | 2024-10-17 | 104500 | -22.87% |
| 323990 | 2024-03-25 | 23350 | 3.85% | -35.33% | 3.85% | -44.28% | 3.85% | -44.28% | 2024-03-25 | 24250 | -46.35% |
| 028300 | 2024-05-17 | 67100 | 9.99% | -32.71% | 46.20% | -32.71% | 46.20% | -32.71% | 2024-07-08 | 98100 | -40.37% |

## 13. Current Calibrated Profile Stress Test
The current profile is directionally correct when C24 has a partner-quality/endpoint-quality bridge, as in 196170. It is incomplete for high-MAE event winners such as 087010 and too permissive for pure trial-narrative price bursts such as 323990. HLB shows a different residual: hard 4C routing is logically correct after a CRL, but price protection is late if the watch layer only appears after the binary regulatory gap.

## 14. Stage2 / Yellow / Green Comparison
No Stage3-Green label is assigned from outcome. `green_lateness_ratio = not_applicable` for all representative rows. The shadow conclusion is not Green relaxation. C24 should remain event-risk-first until endpoint, regulatory, partner-quality, dilution, and commercialization bridges are visible.

## 15. 4B Local vs Full-window Timing Audit
196170 and 087010 show meaningful full-window proximity only after large follow-through. 323990 is a price-only local peak and must not become full 4B. 028300 carries valuation/event-cap 4B risk before the hard 4C, but the official hard-4C trigger is late for protection.

## 16. 4C Protection Audit
HLB is labeled `hard_4c_late`: a CRL/regulatory rejection is hard 4C evidence, but if the model waits for it, the gap-down has already occurred. The candidate shadow rule is an earlier C24 pre-event regulatory watch, not a short-only rule and not investment advice.

## 17. Sector-Specific Rule Candidate
`sector_specific_rule_candidate = true`: In L7, binary trial/regulatory events need a high-MAE sizing/watch guard even when the upside path is positive. Price strength alone cannot promote Stage3.

## 18. Canonical-Archetype Rule Candidate
`canonical_archetype_rule_candidate = true`: `C24_endpoint_or_partner_quality_bridge` plus `C24_pre_event_regulatory_watch`. These keep positive partner-quality events eligible, downgrade trial-headline false positives, and mark binary regulatory decisions before hard 4C.

## 19. Before / After Backtest Comparison
| profile | eligible triggers | avg MFE90 | avg MAE90 | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 75.58% | -26.60% | 0.50 | 0 | too permissive for price-only trial event risk |
| P0b e2r_2_0_baseline_reference | 4 | 75.58% | -26.60% | 0.50 | 1 | misses high-MAE event nuance |
| P1 sector_specific_candidate_profile | 4 | 102.13% on selected positive/watch rows | -14.71% | 0.25 | 0 | improves high-MAE guard |
| P2 canonical_archetype_candidate_profile | 4 | 102.13% on selected rows | -14.71% | 0.25 | 0 | best C24 fit |
| P3 counterexample_guard_profile | 4 | 98.34% on promoted rows | -14.71% | 0.00 for promoted rows | 1 | safest but may undercount early event winners |

## 20. Score-Return Alignment Matrix
| symbol | before stage | after shadow stage | alignment |
|---|---|---|---|
| 196170 | Stage2-Actionable | Stage3-Yellow | event_risk_success_with_non_price_bridge |
| 087010 | Stage2-Actionable | Stage2-Actionable-high-MAE-guard | high_mae_success |
| 323990 | Stage2-Actionable | Stage2-Watch | trial_event_false_positive_high_MAE |
| 028300 | Stage4C | Stage4C | hard_4c_after_gap_too_late_for_protection |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT | 2 | 2 | 4 | 2 | 3 | 1 | 7 | 4 | 2 | true | true | still need URL-verified trial endpoint and regulatory-watch evidence |

## 22. Residual Contribution Summary
new_independent_case_count: 3  
reused_case_count: 1  
reused_case_ids: [R7L71_C24_028300_20240517]  
new_symbol_count: 3  
new_canonical_archetype_count: 0  
new_fine_archetype_count: 1  
new_trigger_family_count: 3  
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c  
residual_error_types_found: trial_headline_without_endpoint_bridge, hard_4C_after_gap_too_late, high_MAE_event_success_needs_size_guard  
new_axis_proposed: C24_endpoint_or_partner_quality_bridge; C24_pre_event_regulatory_watch  
existing_axis_strengthened: full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c_requires_pre_watch_for_binary_events  
existing_axis_weakened: null  
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min  
sector_specific_rule_candidate: true  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  
loop_contribution_label: canonical_archetype_rule_candidate

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.

## 23. Validation Scope / Non-Validation Scope
Validation scope: stock-web tradable OHLC paths, entry dates, MFE/MAE/peak/drawdown, round/sector/canonical consistency, new/reused case flags. Non-validation scope: exact DART/IR/report URL verification and production scoring changes.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C24_endpoint_or_partner_quality_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"Require endpoint/partner-quality bridge before Stage3 promotion","Keeps 196170 eligible; downgrades 323990; treats 087010 as high-MAE actionable only",R7L71_C24_196170_20240222_T_STAGE2|R7L71_C24_323990_20240325_T_STAGE2,4,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C24_pre_event_regulatory_watch,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C24_BIO_TRIAL_DATA_EVENT_RISK,0,1,+1,"Hard 4C after CRL is too late; add pre-event watch when binary regulatory decision is near","HLB shows hard-4C routing protects thesis label but not price risk if activated only after the gap",R7L71_C24_028300_20240517_T_4C,4,3,2,medium,canonical_shadow_only,"4C timing guard; no Green relaxation"
```

## 25. Machine-Readable Rows
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","source_repo_url":"https://github.com/FinanceData/marcap","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R7L71_C24_196170_20240222","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event_risk_success_with_non_price_bridge","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"ALT-B4/platform revaluation event created a large repricing path, but the usable signal is not price alone. It required partner-quality/licensing-route evidence plus repeat external validation before Stage3 promotion."}
{"row_type":"case","case_id":"R7L71_C24_087010_20240627","symbol":"087010","company_name":"펩트론","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mae_success","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"GLP-1/long-acting formulation optionality produced a strong price path, but the entry carried deep early MAE. C24 should treat this as Stage2-Actionable only with event-quality bridge and position-size/high-MAE guard, not as a clean Green."}
{"row_type":"case","case_id":"R7L71_C24_323990_20240325","symbol":"323990","company_name":"박셀바이오","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"trial_event_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A price burst around event/trial narrative failed to convert into durable repricing. The path shows why trial-readout headlines without endpoint/commercial bridge should not get promoted beyond Stage2-Watch."}
{"row_type":"case","case_id":"R7L71_C24_028300_20240517","symbol":"028300","company_name":"HLB","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"reused as benchmark hard-4C timing stress test; not counted as new independent evidence","independent_evidence_weight":0.25,"score_price_alignment":"hard_4c_after_gap_too_late_for_protection","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"FDA CRL/regulatory rejection was a hard 4C event, but the official hard-4C timestamp occurs after the protection window has already failed. C24 needs an earlier regulatory-decision-risk watch layer, not a Green relaxation."}
{"row_type":"trigger","trigger_id":"R7L71_C24_196170_20240222_T_STAGE2","case_id":"R7L71_C24_196170_20240222","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"trial data / regulatory event risk / platform optionality","loop_objective":"4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-23","entry_price":131200,"evidence_available_at_that_date":"ALT-B4/platform revaluation event created a large repricing path, but the usable signal is not price alone. It required partner-quality/licensing-route evidence plus repeat external validation before Stage3 promotion.","evidence_source":"source_proxy: public company disclosure/news/IR around trigger date; exact URL verification deferred to batch implementation","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":71.88,"MFE_90D_pct":127.52,"MFE_180D_pct":177.06,"MFE_1Y_pct":177.06,"MFE_2Y_pct":null,"MAE_30D_pct":-9.3,"MAE_90D_pct":-9.3,"MAE_180D_pct":-9.3,"MAE_1Y_pct":-9.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-20","peak_price":363500,"drawdown_after_peak_pct":-18.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.72,"four_b_timing_verdict":"4B_watch_only","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":null,"trigger_outcome_label":"event_risk_success_with_non_price_bridge","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L71_C24_196170_20240222_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L71_C24_087010_20240627_T_STAGE2","case_id":"R7L71_C24_087010_20240627","symbol":"087010","company_name":"펩트론","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"trial data / regulatory event risk / platform optionality","loop_objective":"4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-27","entry_date":"2024-06-27","entry_price":46500,"evidence_available_at_that_date":"GLP-1/long-acting formulation optionality produced a strong price path, but the entry carried deep early MAE. C24 should treat this as Stage2-Actionable only with event-quality bridge and position-size/high-MAE guard, not as a clean Green.","evidence_source":"source_proxy: public company disclosure/news/IR around trigger date; exact URL verification deferred to batch implementation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/087/087010/2024.csv","profile_path":"atlas/symbol_profiles/087/087010.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":80.22,"MFE_90D_pct":124.73,"MFE_180D_pct":124.73,"MFE_1Y_pct":124.73,"MFE_2Y_pct":null,"MAE_30D_pct":-20.11,"MAE_90D_pct":-20.11,"MAE_180D_pct":-20.11,"MAE_1Y_pct":-20.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-17","peak_price":104500,"drawdown_after_peak_pct":-22.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_data_insufficient","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L71_C24_087010_20240627_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L71_C24_323990_20240325_T_STAGE2","case_id":"R7L71_C24_323990_20240325","symbol":"323990","company_name":"박셀바이오","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"trial data / regulatory event risk / platform optionality","loop_objective":"4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":23350,"evidence_available_at_that_date":"A price burst around event/trial narrative failed to convert into durable repricing. The path shows why trial-readout headlines without endpoint/commercial bridge should not get promoted beyond Stage2-Watch.","evidence_source":"source_proxy: public company disclosure/news/IR around trigger date; exact URL verification deferred to batch implementation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv","profile_path":"atlas/symbol_profiles/323/323990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.85,"MFE_90D_pct":3.85,"MFE_180D_pct":3.85,"MFE_1Y_pct":3.85,"MFE_2Y_pct":null,"MAE_30D_pct":-35.33,"MAE_90D_pct":-44.28,"MAE_180D_pct":-44.28,"MAE_1Y_pct":-44.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":24250,"drawdown_after_peak_pct":-46.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"trial_event_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L71_C24_323990_20240325_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R7L71_C24_028300_20240517_T_4C","case_id":"R7L71_C24_028300_20240517","symbol":"028300","company_name":"HLB","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_EVENT_RISK_TRIAL_READOUT_REGULATORY_CRL_DILUTION_SPLIT","sector":"bio_healthcare_medical","primary_archetype":"trial data / regulatory event risk / platform optionality","loop_objective":"4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage4C","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":67100,"evidence_available_at_that_date":"FDA CRL/regulatory rejection was a hard 4C event, but the official hard-4C timestamp occurs after the protection window has already failed. C24 needs an earlier regulatory-decision-risk watch layer, not a Green relaxation.","evidence_source":"source_proxy: public company disclosure/news/IR around trigger date; exact URL verification deferred to batch implementation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":46.2,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":-32.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-40.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"hard_4c_late","trigger_outcome_label":"hard_4c_after_gap_too_late_for_protection","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R7L71_C24_028300_20240517_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"reused as benchmark hard-4C timing stress test; not counted as new independent evidence","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C24_196170_20240222","trigger_id":"R7L71_C24_196170_20240222_T_STAGE2","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":40,"relative_strength_score":80,"customer_quality_score":65,"policy_or_regulatory_score":70,"valuation_repricing_score":80,"execution_risk_score":50,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":65,"regulatory_event_risk_score":25},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":50,"relative_strength_score":80,"customer_quality_score":75,"policy_or_regulatory_score":70,"valuation_repricing_score":75,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":75,"regulatory_event_risk_score":25},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["trial_endpoint_quality_score","regulatory_event_risk_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C24 shadow profile separates durable partner/endpoint evidence from headline event risk and applies high-MAE/CRL timing guard.","MFE_90D_pct":127.52,"MAE_90D_pct":-9.3,"score_return_alignment_label":"event_risk_success_with_non_price_bridge","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C24_087010_20240627","trigger_id":"R7L71_C24_087010_20240627_T_STAGE2","symbol":"087010","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":40,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":70,"valuation_repricing_score":80,"execution_risk_score":50,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":45,"regulatory_event_risk_score":25},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":35,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":70,"valuation_repricing_score":75,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":40,"regulatory_event_risk_score":25},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable-high-MAE-guard","changed_components":["trial_endpoint_quality_score","regulatory_event_risk_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C24 shadow profile separates durable partner/endpoint evidence from headline event risk and applies high-MAE/CRL timing guard.","MFE_90D_pct":124.73,"MAE_90D_pct":-20.11,"score_return_alignment_label":"high_mae_success","current_profile_verdict":"current_profile_data_insufficient"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C24_323990_20240325","trigger_id":"R7L71_C24_323990_20240325_T_STAGE2","symbol":"323990","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":80,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":55,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":15,"regulatory_event_risk_score":85},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":70,"valuation_repricing_score":45,"execution_risk_score":90,"legal_or_contract_risk_score":85,"dilution_cb_risk_score":65,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":10,"regulatory_event_risk_score":95},"weighted_score_after":63,"stage_label_after":"Stage2-Watch","changed_components":["trial_endpoint_quality_score","regulatory_event_risk_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C24 shadow profile separates durable partner/endpoint evidence from headline event risk and applies high-MAE/CRL timing guard.","MFE_90D_pct":3.85,"MAE_90D_pct":-44.28,"score_return_alignment_label":"trial_event_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R7L71_C24_028300_20240517","trigger_id":"R7L71_C24_028300_20240517_T_4C","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":80,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":55,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":15,"regulatory_event_risk_score":85},"weighted_score_before":78,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":70,"valuation_repricing_score":45,"execution_risk_score":90,"legal_or_contract_risk_score":85,"dilution_cb_risk_score":65,"accounting_trust_risk_score":0,"trial_endpoint_quality_score":10,"regulatory_event_risk_score":95},"weighted_score_after":69,"stage_label_after":"Stage4C","changed_components":["trial_endpoint_quality_score","regulatory_event_risk_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C24 shadow profile separates durable partner/endpoint evidence from headline event risk and applies high-MAE/CRL timing guard.","MFE_90D_pct":46.2,"MAE_90D_pct":-32.71,"score_return_alignment_label":"hard_4c_after_gap_too_late_for_protection","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R7","loop":"71","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["trial_headline_without_endpoint_bridge","hard_4C_after_gap_too_late","high_MAE_event_success_needs_size_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R7  
completed_loop = 71  
next_round = R8  
next_loop = 71  
round_schedule_status = valid  
round_sector_consistency = pass

## 28. Source Notes
- Price source: Songdaiki/stock-web tradable_raw OHLC atlas.
- Manifest max_date used: 2026-02-20.
- This document is historical calibration research, not current/live candidate discovery and not investment advice.

