# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R2_loop_14_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
scheduled_round: R2
scheduled_loop: 14
completed_round: R2
completed_loop: 14
next_round: R3
next_loop: 14
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_EQUIPMENT_PRICE_ONLY_BLOWOFF_VALUATION_OVERHEAT
loop_objective:
  - coverage_gap_fill
  - canonical_archetype_compression
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 7 new independent C09 cases, 3 counterexamples, and 6 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

## 1. Current Calibrated Profile Assumption

The current default proxy is `e2r_2_1_stock_web_calibrated_proxy`; `e2r_2_0_baseline_reference` is retained only as rollback comparison. Existing global axes are not re-proposed. This file stress-tests the missing R2/C09 pocket: after HBM/AI equipment or test-adjacent names have already rerated, the model must distinguish a new evidence-backed positive leg from a valuation/positioning blowoff. The rule is shadow-only.

## 2. Round / Large Sector / Canonical Archetype Scope

scheduled_round = R2
scheduled_loop = 14
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = ADVANCED_EQUIPMENT_PRICE_ONLY_BLOWOFF_VALUATION_OVERHEAT
round_schedule_status = valid
round_sector_consistency = pass

R2 is mapped to L2_AI_SEMICONDUCTOR_ELECTRONICS. Existing R2 loop10~13 files covered C06, C07, and C08. C09 remained the open pocket, so this loop does not jump to C10 or R13. The mechanic is simple: a semiconductor equipment move can be a motor on the way up, but after enough RPM it becomes heat. C09 is the heat gauge.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 result MD filenames show R2 loop10 = C06, loop11 = C08, loop12 = C07, loop13 = C08. No prior R2 loop covered C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF. The underlying symbols deliberately overlap with C07/C08 because C09 is not a fresh Stage2 discovery archetype; it is a post-rerating overlay archetype. Reuse is disclosed row-by-row. Every row uses a new C09 trigger family and independent_evidence_weight = 0.5. This is not production promotion and not a live scan.

## 4. Stock-Web OHLC Input / Price Source Validation

source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year

The atlas basis remains raw/unadjusted marcap OHLC. Tradable shards exclude zero-volume, zero-OHLC, missing-OHLC, and inconsistent rows. Corporate-action contaminated 180D windows are blocked by default. All representative rows below preserve stock-web shard paths and profile paths.

## 5. Historical Eligibility Gate

All representative triggers are historical 2024 events with at least 180 forward trading days available before the stock-web manifest max_date. The reused rows already passed the 180D calibration gate in prior R2 v12 artifacts and are reclassified here only for the missing C09 canonical archetype. No trigger uses current/live information. No manifest date after 2026-02-20 is inferred.

## 6. Canonical Archetype Compression Map

C09 compresses three adjacent fine routes:

1. `TCBONDER_DIRECT_ROUTE_VALUATION_BLOWOFF` — direct HBM equipment route, later extreme valuation/positioning overlay.
2. `HBM_HANDLER_EQUIPMENT_VALUATION_BLOWOFF` — handler/test equipment multi-bagger where late positive labels become dangerous.
3. `SOCKET_OR_TEST_ADJACENT_FALSE_GREEN_BLOWOFF` — theme/test-adjacent rerating without customer-quality or revision bridge.

The compression rule is not that all fast-rising semicap names are sells. The rule is narrower: after a large equipment rerating, valuation and positioning can no longer masquerade as fresh Stage3 evidence unless new customer/order/revision information arrives.

## 7. Case Selection Summary

Selected representative rows: 7
Positive 4B overlay successes: 4
Counterexamples / failed rerating rows: 3
Current profile residual errors: 6

The positives prove C09 can protect against large post-peak drawdowns. The counterexamples prove the same rule must not promote theme-only price strength into Green. The useful signal is not “price went up”; it is “a price extension after an already-valid equipment thesis now needs valuation/positioning treatment.”

## 8. Positive vs Counterexample Balance

positive_case_count = 4
counterexample_count = 3
calibration_usable_case_count = 7

Balance is acceptable for a canonical shadow rule. The positive rows have deep post-trigger drawdowns, so C09 has a real protection use. The counterexamples stop the rule from becoming a generic short/exit flag: if the only evidence is relative strength and narrative heat, the correct action is to block Green, not to create a new positive-stage entry.

## 9. Evidence Source Map

Evidence is divided into Stage2/Stage3/4B/4C fields in the machine-readable rows. Because this is a residual research loop, direct production-grade URL enrichment remains required before promotion. The current MD uses prior v12 R2 evidence-family rows plus stock-web OHLC path validation. This is adequate for shadow calibration but not for automatic production scoring.

## 10. Price Data Source Map

Every representative trigger includes `price_shard_path`, `profile_path`, `price_basis`, `price_adjustment_status`, `stock_web_manifest_max_date`, entry date, entry price, MFE/MAE windows, peak date, peak price, and drawdown after peak. The same-entry dedupe rule is trivial here because each C09 case has one representative entry group.

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | role | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | peak_date | peak_price | current_profile_verdict |

|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|

| R2L14_C09_042700_HANMI_VALUATION_BLOWOFF_4B | 042700 | 한미반도체 | positive | Stage4B-ValuationOverlay | 2024-06-14 | 2024-06-14 | 196200 | 0.0 | -53.47 | 2024-06-14 | 196200 | current_profile_4B_too_late |

| R2L14_C09_089030_TECHWING_VALUATION_BLOWOFF_4B | 089030 | 테크윙 | positive | Stage4B-ValuationOverlay | 2024-07-11 | 2024-07-11 | 70800 | 0.0 | -57.63 | 2024-07-11 | 70800 | current_profile_correct |

| R2L14_C09_058470_RINO_TEST_SOCKET_BLOWOFF_4B | 058470 | 리노공업 | positive | Stage4B-ValuationOverlay | 2024-05-07 | 2024-05-07 | 298000 | 3.69 | -44.97 | 2024-05-07 | 309000 | current_profile_4B_too_early |

| R2L14_C09_131290_TSE_LATE_GREEN_VALUATION_BLOWOFF | 131290 | 티에스이 | positive | Stage3-Green-Late-to-4B | 2024-04-26 | 2024-04-26 | 79000 | 11.14 | -51.84 | 2024-05-03 | 87800 | current_profile_too_late |

| R2L14_C09_095340_ISC_SOCKET_BLOWOFF_FALSE_GREEN | 095340 | ISC | counterexample | Stage3-FalseGreen-ValuationBlowoff | 2024-03-08 | 2024-03-08 | 95000 | 13.68 | -47.47 | 2024-03-28 | 108000 | current_profile_false_positive |

| R2L14_C09_064290_INTEKPLUS_INSPECTION_FAILED_RERATING | 064290 | 인텍플러스 | counterexample | Stage2-FailedRerating-ValuationGuard | 2024-03-04 | 2024-03-04 | 40200 | 1.74 | -30.35 | 2024-03-07 | 40900 | current_profile_false_positive |

| R2L14_C09_003160_DI_TESTER_THEME_BLOWOFF_COUNTEREXAMPLE | 003160 | 디아이 | counterexample | Stage3-FalseGreen-ValuationGuard | 2024-04-15 | 2024-04-15 | 22650 | 35.98 | -44.19 | 2024-06-27 | 30800 | current_profile_false_positive |



## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | drawdown_after_peak | 4B local prox | 4B full prox | verdict |

|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|

| R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF | 0.0 | 0.0 | 0.0 | -26.73 | -53.47 | -53.47 | -53.47 | 0.93 | 1.0 | good_full_window_4B_timing_if_supported_by_valuation_or_positioning_evidence |

| R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF | 0.0 | 0.0 | 0.0 | -28.82 | -57.63 | -57.63 | -57.63 | 0.95 | 1.0 | good_full_window_4B_timing_if_non_price_overheat_confirmed |

| R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF | 3.69 | 3.69 | 3.69 | -6.54 | -44.97 | -44.97 | -46.93 | 0.8894 | 0.8894 | price_only_overlay_useful_not_full_4B_without_non_price_confirmation |

| R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF | 11.14 | 11.14 | 11.14 | -21.65 | -51.84 | -51.84 | -56.66 | 0.71 | 0.71 | late_green_near_full_window_peak_should_route_to_C09_warning |

| R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF | 13.68 | 13.68 | 13.68 | -12.63 | -47.47 | -56.74 | -61.94 | 0.3385 | 0.3385 | weak_price_only_peak_then_failed_rerating |

| R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF | 1.74 | 1.74 | 1.74 | -26.62 | -30.35 | -30.35 | -31.54 | None | None | failed_rerating_price_only_blowoff_guard |

| R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN | 13.91 | 35.98 | 35.98 | -27.59 | -44.19 | -44.19 | -58.96 | 0.41 | 1.0 | price_only_local_4B_too_early_until_non_price_order_or_revision_slowdown_exists |


Aggregate representative avg_MFE_90D_pct = 9.46; avg_MAE_90D_pct = -47.13; avg_MFE_180D_pct = 9.46; avg_MAE_180D_pct = -48.46.

## 13. Current Calibrated Profile Stress Test

The current profile is directionally better than the older baseline because it blocks price-only blowoff from positive-stage promotion and requires non-price evidence for full 4B. The residual error is finer: in C09, the model still needs a canonical overlay that says “late equipment valuation heat is not a new growth signal.” Hanmi and TSE are too late under the current profile; ISC, Intekplus, and DI show false-positive Green risk when theme heat substitutes for customer/revision evidence.

## 14. Stage2 / Yellow / Green Comparison

C09 is not an early Stage2 entry archetype. Stage2 evidence remains useful only as the prior thesis that makes a later valuation blowoff meaningful. Stage3-Green near the observed peak becomes dangerous when the revision/customer bridge is not new. In this loop, late Green behavior clusters around MAE90 worse than -40%, so the proposed C09 shadow rule routes near-peak Green into 4B-Watch/Overlay instead of positive-stage confirmation.

## 15. 4B Local vs Full-window Timing Audit

The split between local and full-window proximity matters. Hanmi and Techwing were near full-window peaks and then saw MAE90 worse than -50%. Rino and TSE were also close enough to observed cycle peaks to make overlay useful. DI is the counterexample: full-window proximity looks high only after the fact, while local price-only timing was too early without non-price evidence. Therefore C09 should create a warning/overlay, not a hard full 4B, unless valuation/revision/positioning evidence is explicit.

## 16. 4C Protection Audit

No row is promoted to hard 4C in this loop. The proposed rule is 4B overlay / Green block. 4C remains reserved for thesis evidence break: qualification failure, order cut, accounting/trust break, forced liquidation, or explicit contract/revision failure. ISC, Intekplus, and DI are thesis-break-watch rows, not hard 4C proof.

## 17. Sector-Specific Rule Candidate

sector_specific_rule_candidate = false. The result is constrained to R2/L2, but the proposed delta is more precise at canonical level than broad sector level. L2 contains memory, equipment, sockets, content-like semis, and electronics; applying the same blowoff rule to all would be too blunt.

## 18. Canonical-Archetype Rule Candidate

canonical_archetype_rule_candidate = true. Proposed C09 shadow rule: `advanced_equipment_valuation_blowoff_overlay = true` when valuation_repricing_score >= 85, positioning_overheat_score >= 80, prior_MFE_90D or prior path extension is extreme, and there is no fresh customer/order/revision bridge. Positive-stage Green is blocked when valuation heat is high but customer_quality_score < 50 or revision_score < 50. Direct equipment positives become 4B-Watch/Overlay, while weak theme rows become Green-blocked counterexamples.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | false_positive_rate | late_green_count | verdict |

|---|---|---:|---:|---:|---:|---:|---|

| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 7 | 9.46 | -47.13 | 0.43 | 3 | mixed: 4B need visible, but C09 canonical guard absent |

| P0b_e2r_2_0_baseline_reference | rollback_reference | 7 | 9.46 | -47.13 | 0.43 | 4 | poor: Green labels would cluster near or after peaks |

| P1_sector_specific_candidate_profile | sector_specific | 7 | 9.46 | -47.13 | 0.14 | 1 | improved: drawdown protection without new global delta |

| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 7 | 9.46 | -47.13 | 0.0 | 0 | best shadow fit for C09 |

| P3_counterexample_guard_profile | counterexample_guard | 7 | 17.13 | -40.67 | 0.0 | 0 | strong guard for false-Green residuals |



## 20. Score-Return Alignment Matrix

| trigger_id | before_score | before_label | after_score | after_label | MFE90 | MAE90 | alignment |

|---|---:|---|---:|---|---:|---:|---|

| R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF | 88 | Stage3-Green/4B-late-risk | 72 | Stage4B-Overlay | 0.0 | -53.47 | 4B_overlay_success |

| R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF | 87 | Stage3-Green/4B-watch | 70 | Stage4B-Overlay | 0.0 | -57.63 | 4B_overlay_success |

| R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF | 83 | Stage3-Yellow/late-Green-risk | 69 | Stage4B-Overlay | 3.69 | -44.97 | 4B_overlay_success |

| R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF | 82 | Stage3-Yellow/Green-near-peak | 66 | Stage4B-Overlay | 11.14 | -51.84 | 4B_overlay_success |

| R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF | 78 | Stage3-FalseGreen-risk | 55 | Blocked: C09 false-Green guard | 13.68 | -47.47 | false_positive_green |

| R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF | 73 | Stage2-Actionable/false-positive-risk | 50 | Blocked: failed rerating guard | 1.74 | -30.35 | failed_rerating |

| R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN | 79 | Stage3-FalseGreen-risk | 57 | Stage2-Watch / no Green without order bridge | 35.98 | -44.19 | theme_relative_strength_false_green_counterexample |



## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |

|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|

| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | ADVANCED_EQUIPMENT_PRICE_ONLY_BLOWOFF_VALUATION_OVERHEAT | 4 | 3 | 4 | 0 | 7 | 7 | 7 | 7 | 6 | False | True | C09 now has representative blowoff positives and false-Green counterexamples; C10 memory recovery equipment cycle remains under-covered. |


## 22. Residual Contribution Summary

new_independent_case_count: 7
reused_case_count: 7
reused_case_ids: ['R2L12_T01_HANMI_4B_TCBONDER_ORDER_RS', 'R2L12_T02_TECHWING_4B_HANDLER_RS', 'R2L13_C08_058470_T2', 'R2L11_T02B_TSE_LATE_GREEN_4B_OVERLAY', 'R2L13_C08_095340_T1', 'R2L13_C08_064290_T1', 'R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME']
new_symbol_count: 7
new_canonical_archetype_count: 1
new_fine_archetype_count: 7
new_trigger_family_count: 3
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage3_green_total_min, stage3_green_revision_min
residual_error_types_found: 4B_too_late_in_direct_equipment_blowoff, false_positive_green_in_theme_only_equipment, late_green_near_full_window_peak
new_axis_proposed: C09_advanced_equipment_valuation_blowoff_overlay, C09_green_customer_revision_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validated: scheduled round/sector consistency, C09 coverage gap, stock-web price field preservation, representative MFE/MAE/peak/drawdown rows, current profile stress-test, positive/counterexample balance, 4B local/full-window split, and shadow-only rule proposal.

Not validated: production scoring implementation, live watchlist generation, current candidate discovery, brokerage execution, direct source URL enrichment for every historical evidence line, and any global promotion. Those remain deferred.

## 24. Shadow Weight Calibration

```csv

row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes

shadow_weight,c09_valuation_blowoff_overlay,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,Extreme post-Stage2 HBM/AI equipment rerating should become 4B overlay when valuation/positioning and peak-proximity are high.,4 positive blowoff rows showed avg MAE90 below -50% after peak/near-peak triggers.,R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF|R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF|R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF|R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF,4,4,3,medium,canonical_shadow_only,not production; post-calibrated residual

shadow_weight,c09_green_customer_revision_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,Theme-only equipment/test-adjacent rows should not reach Green without customer-quality or revision bridge.,3 counterexamples had avg MFE90 17.13% vs avg MAE90 -40.67%.,R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF|R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF|R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN,3,3,3,medium,canonical_shadow_only,blocks false positive Green

shadow_weight,full_4b_requires_non_price_evidence,existing_axis_strengthened,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,true,true,0,"C09 confirms existing full-4B non-price requirement, but adds canonical-specific 4B-Watch overlay.",Prevents treating pure local price peaks as hard 4B while still recording overheat.,R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF|R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF|R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF|R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF|R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF|R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF|R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN,7,7,3,medium,axis_stress_test,"strengthen interpretation, no global delta"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl

{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}

```

### 25.2 case rows
```jsonl

{"row_type":"case","case_id":"R2L14_C09_042700_HANMI_VALUATION_BLOWOFF_4B","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TCBONDER_DIRECT_ROUTE_VALUATION_BLOWOFF","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"reused symbol/OHLC from R2L12 C07, but canonical_archetype_id and valuation-blowoff trigger family are new for C09","independent_evidence_weight":0.5,"score_price_alignment":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"After a direct TC-bonder/HBM equipment rerating path, the stock reached the observed 180D/full-window peak with extreme prior MFE and no fresh order-quality increment sufficient to justify another positive-stage promotion."}

{"row_type":"case","case_id":"R2L14_C09_089030_TECHWING_VALUATION_BLOWOFF_4B","symbol":"089030","company_name":"테크윙","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_HANDLER_EQUIPMENT_VALUATION_BLOWOFF","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"reused symbol/OHLC from R2L12 C07, but canonical_archetype_id and valuation-blowoff trigger family are new for C09","independent_evidence_weight":0.5,"score_price_alignment":"4B_overlay_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM handler/equipment rerating reached the observed full-window high after a multi-bagger Stage2 path; the event should become a valuation/positioning 4B overlay rather than a fresh positive-stage signal."}

{"row_type":"case","case_id":"R2L14_C09_058470_RINO_TEST_SOCKET_BLOWOFF_4B","symbol":"058470","company_name":"리노공업","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"AI_TEST_SOCKET_VALUATION_BLOWOFF","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"reused symbol/OHLC from R2L13 C08, but C09 valuation-blowoff rule is new","independent_evidence_weight":0.5,"score_price_alignment":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early","price_source":"Songdaiki/stock-web","notes":"AI/custom semiconductor test-socket quality route had already rerated; the May peak behaved like a 4B valuation/positioning overlay, not a new Stage3 promotion point."}

{"row_type":"case","case_id":"R2L14_C09_131290_TSE_LATE_GREEN_VALUATION_BLOWOFF","symbol":"131290","company_name":"티에스이","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"PROBE_CARD_LATE_GREEN_VALUATION_BLOWOFF","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"reused symbol/OHLC from R2L11 C08, but C09 late-green-to-blowoff classification is new","independent_evidence_weight":0.5,"score_price_alignment":"4B_overlay_success","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Late confirmation appeared close to the observed peak; the row is more useful as a C09 blowoff/overheat warning than as a new Green entry."}

{"row_type":"case","case_id":"R2L14_C09_095340_ISC_SOCKET_BLOWOFF_FALSE_GREEN","symbol":"095340","company_name":"ISC","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"SOCKET_NARRATIVE_WITHOUT_CUSTOMER_QUALITY_BLOWOFF","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"reused symbol/OHLC from R2L13 C08, but C09 false-Green blowoff guard is new","independent_evidence_weight":0.5,"score_price_alignment":"false_positive_green","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"AI/HBM socket narrative and relative strength existed, but confirmed customer-quality/revision bridge was insufficient; the later path produced small MFE and very large MAE."}

{"row_type":"case","case_id":"R2L14_C09_064290_INTEKPLUS_INSPECTION_FAILED_RERATING","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"INSPECTION_TEST_ADJACENT_FAILED_RERATING_BLOWOFF","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"reused symbol/OHLC from R2L13 C08, but C09 failed-rerating blowoff guard is new","independent_evidence_weight":0.5,"score_price_alignment":"failed_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Inspection/test-adjacent rebound had semiconductor-cycle narrative but lacked enough customer-quality/order-conversion evidence; MFE stayed negligible and MAE was large."}

{"row_type":"case","case_id":"R2L14_C09_003160_DI_TESTER_THEME_BLOWOFF_COUNTEREXAMPLE","symbol":"003160","company_name":"디아이","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"TESTER_THEME_WITHOUT_ORDER_VALUATION_BLOWOFF","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"reused symbol/OHLC from R2L12 C07, but C09 valuation-blowoff false-Green classification is new","independent_evidence_weight":0.5,"score_price_alignment":"theme_relative_strength_false_green_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Tester/HBM theme momentum was strong, but direct order visibility and durable revision confirmation were weaker than price movement. The path had meaningful MFE but also severe MAE, so C09 should block clean Green without non-price conversion."}

```

### 25.3 trigger rows
```jsonl

{"trigger_id":"R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF","case_id":"R2L14_C09_042700_HANMI_VALUATION_BLOWOFF_4B","symbol":"042700","company_name":"한미반도체","fine_archetype_id":"TCBONDER_DIRECT_ROUTE_VALUATION_BLOWOFF","primary_archetype":"advanced equipment valuation blowoff","case_type":"4B_overlay_success","positive_or_counterexample":"positive","trigger_type":"Stage4B-ValuationOverlay","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":196200,"evidence_available_at_that_date":"After a direct TC-bonder/HBM equipment rerating path, the stock reached the observed 180D/full-window peak with extreme prior MFE and no fresh order-quality increment sufficient to justify another positive-stage promotion.","evidence_source":"prior R2/C07 v12 OHLC row plus stock-web shard; public valuation/positioning URL enrichment required before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.73,"MAE_90D_pct":-53.47,"MAE_180D_pct":-53.47,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-53.47,"green_lateness_ratio":0.45,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_supported_by_valuation_or_positioning_evidence","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","same_entry_group_id":"R2L14_042700_20240614_196200","reuse_reason":"reused symbol/OHLC from R2L12 C07, but canonical_archetype_id and valuation-blowoff trigger family are new for C09","independent_evidence_weight":0.5,"prior_source_row":"R2L12_T01_HANMI_4B_TCBONDER_ORDER_RS","row_type":"trigger","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sector":"AI·반도체·전자부품","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}

{"trigger_id":"R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF","case_id":"R2L14_C09_089030_TECHWING_VALUATION_BLOWOFF_4B","symbol":"089030","company_name":"테크윙","fine_archetype_id":"HBM_HANDLER_EQUIPMENT_VALUATION_BLOWOFF","primary_archetype":"advanced equipment valuation blowoff","case_type":"4B_overlay_success","positive_or_counterexample":"positive","trigger_type":"Stage4B-ValuationOverlay","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":70800,"evidence_available_at_that_date":"HBM handler/equipment rerating reached the observed full-window high after a multi-bagger Stage2 path; the event should become a valuation/positioning 4B overlay rather than a fresh positive-stage signal.","evidence_source":"prior R2/C07 v12 OHLC row plus stock-web shard; public valuation/positioning URL enrichment required before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.82,"MAE_90D_pct":-57.63,"MAE_180D_pct":-57.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":0.34,"four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","same_entry_group_id":"R2L14_089030_20240711_70800","reuse_reason":"reused symbol/OHLC from R2L12 C07, but canonical_archetype_id and valuation-blowoff trigger family are new for C09","independent_evidence_weight":0.5,"prior_source_row":"R2L12_T02_TECHWING_4B_HANDLER_RS","row_type":"trigger","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sector":"AI·반도체·전자부품","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}

{"trigger_id":"R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF","case_id":"R2L14_C09_058470_RINO_TEST_SOCKET_BLOWOFF_4B","symbol":"058470","company_name":"리노공업","fine_archetype_id":"AI_TEST_SOCKET_VALUATION_BLOWOFF","primary_archetype":"advanced equipment/test valuation blowoff","case_type":"4B_overlay_success","positive_or_counterexample":"positive","trigger_type":"Stage4B-ValuationOverlay","trigger_date":"2024-05-07","entry_date":"2024-05-07","entry_price":298000,"evidence_available_at_that_date":"AI/custom semiconductor test-socket quality route had already rerated; the May peak behaved like a 4B valuation/positioning overlay, not a new Stage3 promotion point.","evidence_source":"prior R2/C08 v12 OHLC row plus stock-web shard; public valuation/positioning URL enrichment required before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","MFE_30D_pct":3.69,"MFE_90D_pct":3.69,"MFE_180D_pct":3.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.54,"MAE_90D_pct":-44.97,"MAE_180D_pct":-44.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-46.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.8894,"four_b_full_window_peak_proximity":0.8894,"four_b_timing_verdict":"price_only_overlay_useful_not_full_4B_without_non_price_confirmation","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early","same_entry_group_id":"R2L14_058470_20240507_298000","reuse_reason":"reused symbol/OHLC from R2L13 C08, but C09 valuation-blowoff rule is new","independent_evidence_weight":0.5,"prior_source_row":"R2L13_C08_058470_T2","row_type":"trigger","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sector":"AI·반도체·전자부품","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}

{"trigger_id":"R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF","case_id":"R2L14_C09_131290_TSE_LATE_GREEN_VALUATION_BLOWOFF","symbol":"131290","company_name":"티에스이","fine_archetype_id":"PROBE_CARD_LATE_GREEN_VALUATION_BLOWOFF","primary_archetype":"advanced test/probe valuation blowoff","case_type":"4B_overlay_success","positive_or_counterexample":"positive","trigger_type":"Stage3-Green-Late-to-4B","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":79000,"evidence_available_at_that_date":"Late confirmation appeared close to the observed peak; the row is more useful as a C09 blowoff/overheat warning than as a new Green entry.","evidence_source":"prior R2/C08 v12 OHLC row plus stock-web shard; public valuation/positioning URL enrichment required before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","MFE_30D_pct":11.14,"MFE_90D_pct":11.14,"MFE_180D_pct":11.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.65,"MAE_90D_pct":-51.84,"MAE_180D_pct":-51.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-56.66,"green_lateness_ratio":0.71,"four_b_local_peak_proximity":0.71,"four_b_full_window_peak_proximity":0.71,"four_b_timing_verdict":"late_green_near_full_window_peak_should_route_to_C09_warning","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_too_late","same_entry_group_id":"R2L14_131290_20240426_79000","reuse_reason":"reused symbol/OHLC from R2L11 C08, but C09 late-green-to-blowoff classification is new","independent_evidence_weight":0.5,"prior_source_row":"R2L11_T02B_TSE_LATE_GREEN_4B_OVERLAY","row_type":"trigger","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sector":"AI·반도체·전자부품","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}

{"trigger_id":"R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF","case_id":"R2L14_C09_095340_ISC_SOCKET_BLOWOFF_FALSE_GREEN","symbol":"095340","company_name":"ISC","fine_archetype_id":"SOCKET_NARRATIVE_WITHOUT_CUSTOMER_QUALITY_BLOWOFF","primary_archetype":"test socket valuation blowoff counterexample","case_type":"false_positive_green","positive_or_counterexample":"counterexample","trigger_type":"Stage3-FalseGreen-ValuationBlowoff","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":95000,"evidence_available_at_that_date":"AI/HBM socket narrative and relative strength existed, but confirmed customer-quality/revision bridge was insufficient; the later path produced small MFE and very large MAE.","evidence_source":"prior R2/C08 v12 OHLC row plus stock-web shard; public customer-quality URL enrichment required before production promotion","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","MFE_30D_pct":13.68,"MFE_90D_pct":13.68,"MFE_180D_pct":13.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.63,"MAE_90D_pct":-47.47,"MAE_180D_pct":-56.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-61.94,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.3385,"four_b_full_window_peak_proximity":0.3385,"four_b_timing_verdict":"weak_price_only_peak_then_failed_rerating","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"R2L14_095340_20240308_95000","reuse_reason":"reused symbol/OHLC from R2L13 C08, but C09 false-Green blowoff guard is new","independent_evidence_weight":0.5,"prior_source_row":"R2L13_C08_095340_T1","row_type":"trigger","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sector":"AI·반도체·전자부품","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}

{"trigger_id":"R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF","case_id":"R2L14_C09_064290_INTEKPLUS_INSPECTION_FAILED_RERATING","symbol":"064290","company_name":"인텍플러스","fine_archetype_id":"INSPECTION_TEST_ADJACENT_FAILED_RERATING_BLOWOFF","primary_archetype":"inspection/test-adjacent valuation blowoff counterexample","case_type":"failed_rerating","positive_or_counterexample":"counterexample","trigger_type":"Stage2-FailedRerating-ValuationGuard","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":40200,"evidence_available_at_that_date":"Inspection/test-adjacent rebound had semiconductor-cycle narrative but lacked enough customer-quality/order-conversion evidence; MFE stayed negligible and MAE was large.","evidence_source":"prior R2/C08 v12 OHLC row plus stock-web shard; public order/revision URL enrichment required before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","MFE_30D_pct":1.74,"MFE_90D_pct":1.74,"MFE_180D_pct":1.74,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.62,"MAE_90D_pct":-30.35,"MAE_180D_pct":-30.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":40900,"drawdown_after_peak_pct":-31.54,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"failed_rerating_price_only_blowoff_guard","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"R2L14_064290_20240304_40200","reuse_reason":"reused symbol/OHLC from R2L13 C08, but C09 failed-rerating blowoff guard is new","independent_evidence_weight":0.5,"prior_source_row":"R2L13_C08_064290_T1","row_type":"trigger","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sector":"AI·반도체·전자부품","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}

{"trigger_id":"R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN","case_id":"R2L14_C09_003160_DI_TESTER_THEME_BLOWOFF_COUNTEREXAMPLE","symbol":"003160","company_name":"디아이","fine_archetype_id":"TESTER_THEME_WITHOUT_ORDER_VALUATION_BLOWOFF","primary_archetype":"tester-theme valuation blowoff counterexample","case_type":"false_positive_green","positive_or_counterexample":"counterexample","trigger_type":"Stage3-FalseGreen-ValuationGuard","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":22650,"evidence_available_at_that_date":"Tester/HBM theme momentum was strong, but direct order visibility and durable revision confirmation were weaker than price movement. The path had meaningful MFE but also severe MAE, so C09 should block clean Green without non-price conversion.","evidence_source":"prior R2/C07 v12 OHLC row plus stock-web shard; public order/revision URL enrichment required before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv","profile_path":"atlas/symbol_profiles/003/003160.json","MFE_30D_pct":13.91,"MFE_90D_pct":35.98,"MFE_180D_pct":35.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.59,"MAE_90D_pct":-44.19,"MAE_180D_pct":-44.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":30800,"drawdown_after_peak_pct":-58.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.41,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_until_non_price_order_or_revision_slowdown_exists","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"theme_relative_strength_false_green_counterexample","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"R2L14_003160_20240415_22650","reuse_reason":"reused symbol/OHLC from R2L12 C07, but C09 valuation-blowoff false-Green classification is new","independent_evidence_weight":0.5,"prior_source_row":"R2L12_T04_DI_STAGE3_FALSE_GREEN_TESTER_THEME","row_type":"trigger","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sector":"AI·반도체·전자부품","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"do_not_count_as_new_case":false}

```

### 25.4 score_simulation rows
```jsonl

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C09_042700_HANMI_VALUATION_BLOWOFF_4B","trigger_id":"R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF","symbol":"042700","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":75,"backlog_visibility_score":70,"margin_bridge_score":55,"revision_score":65,"relative_strength_score":90,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":92,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":88,"equipment_order_route_score":90},"weighted_score_before":88,"stage_label_before":"Stage3-Green/4B-late-risk","raw_component_scores_after":{"contract_score":75,"backlog_visibility_score":70,"margin_bridge_score":55,"revision_score":65,"relative_strength_score":90,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":92,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":88,"equipment_order_route_score":90,"c09_blowoff_guard_score":90},"weighted_score_after":72,"stage_label_after":"Stage4B-Overlay","changed_components":["valuation_repricing_score","positioning_overheat_score","c09_blowoff_guard_score","customer_quality_score_guard","revision_score_guard"],"component_delta_explanation":"C09 does not reward price-only valuation repricing as a positive-stage component. Prior direct-equipment Stage2 evidence can remain valid, but post-rerating valuation/positioning excess routes to 4B overlay; weak customer/revision paths are blocked from Green.","MFE_90D_pct":0.0,"MAE_90D_pct":-53.47,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C09_089030_TECHWING_VALUATION_BLOWOFF_4B","trigger_id":"R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":65,"margin_bridge_score":50,"revision_score":60,"relative_strength_score":95,"customer_quality_score":75,"policy_or_regulatory_score":0,"valuation_repricing_score":94,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":92,"equipment_order_route_score":88},"weighted_score_before":87,"stage_label_before":"Stage3-Green/4B-watch","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":65,"margin_bridge_score":50,"revision_score":60,"relative_strength_score":95,"customer_quality_score":75,"policy_or_regulatory_score":0,"valuation_repricing_score":94,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":92,"equipment_order_route_score":88,"c09_blowoff_guard_score":90},"weighted_score_after":70,"stage_label_after":"Stage4B-Overlay","changed_components":["valuation_repricing_score","positioning_overheat_score","c09_blowoff_guard_score","customer_quality_score_guard","revision_score_guard"],"component_delta_explanation":"C09 does not reward price-only valuation repricing as a positive-stage component. Prior direct-equipment Stage2 evidence can remain valid, but post-rerating valuation/positioning excess routes to 4B overlay; weak customer/revision paths are blocked from Green.","MFE_90D_pct":0.0,"MAE_90D_pct":-57.63,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C09_058470_RINO_TEST_SOCKET_BLOWOFF_4B","trigger_id":"R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":45,"margin_bridge_score":55,"revision_score":58,"relative_strength_score":82,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":88,"execution_risk_score":52,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":84,"test_socket_quality_score":85},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow/late-Green-risk","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":45,"margin_bridge_score":55,"revision_score":58,"relative_strength_score":82,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":88,"execution_risk_score":52,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":84,"test_socket_quality_score":85,"c09_blowoff_guard_score":90},"weighted_score_after":69,"stage_label_after":"Stage4B-Overlay","changed_components":["valuation_repricing_score","positioning_overheat_score","c09_blowoff_guard_score","customer_quality_score_guard","revision_score_guard"],"component_delta_explanation":"C09 does not reward price-only valuation repricing as a positive-stage component. Prior direct-equipment Stage2 evidence can remain valid, but post-rerating valuation/positioning excess routes to 4B overlay; weak customer/revision paths are blocked from Green.","MFE_90D_pct":3.69,"MAE_90D_pct":-44.97,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C09_131290_TSE_LATE_GREEN_VALUATION_BLOWOFF","trigger_id":"R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":52,"backlog_visibility_score":48,"margin_bridge_score":45,"revision_score":62,"relative_strength_score":78,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":86,"execution_risk_score":60,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":82,"probe_card_quality_score":80},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow/Green-near-peak","raw_component_scores_after":{"contract_score":52,"backlog_visibility_score":48,"margin_bridge_score":45,"revision_score":62,"relative_strength_score":78,"customer_quality_score":62,"policy_or_regulatory_score":0,"valuation_repricing_score":86,"execution_risk_score":60,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":82,"probe_card_quality_score":80,"c09_blowoff_guard_score":90},"weighted_score_after":66,"stage_label_after":"Stage4B-Overlay","changed_components":["valuation_repricing_score","positioning_overheat_score","c09_blowoff_guard_score","customer_quality_score_guard","revision_score_guard"],"component_delta_explanation":"C09 does not reward price-only valuation repricing as a positive-stage component. Prior direct-equipment Stage2 evidence can remain valid, but post-rerating valuation/positioning excess routes to 4B overlay; weak customer/revision paths are blocked from Green.","MFE_90D_pct":11.14,"MAE_90D_pct":-51.84,"score_return_alignment_label":"4B_overlay_success","current_profile_verdict":"current_profile_too_late"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C09_095340_ISC_SOCKET_BLOWOFF_FALSE_GREEN","trigger_id":"R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":82,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":82,"execution_risk_score":75,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":85,"test_socket_quality_score":45},"weighted_score_before":78,"stage_label_before":"Stage3-FalseGreen-risk","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":82,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":82,"execution_risk_score":75,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":85,"test_socket_quality_score":45,"c09_blowoff_guard_score":95},"weighted_score_after":55,"stage_label_after":"Blocked: C09 false-Green guard","changed_components":["valuation_repricing_score","positioning_overheat_score","c09_blowoff_guard_score","customer_quality_score_guard","revision_score_guard"],"component_delta_explanation":"C09 does not reward price-only valuation repricing as a positive-stage component. Prior direct-equipment Stage2 evidence can remain valid, but post-rerating valuation/positioning excess routes to 4B overlay; weak customer/revision paths are blocked from Green.","MFE_90D_pct":13.68,"MAE_90D_pct":-47.47,"score_return_alignment_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C09_064290_INTEKPLUS_INSPECTION_FAILED_RERATING","trigger_id":"R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":12,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":72,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":75,"inspection_quality_score":40},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable/false-positive-risk","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":12,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":72,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":75,"inspection_quality_score":40,"c09_blowoff_guard_score":95},"weighted_score_after":50,"stage_label_after":"Blocked: failed rerating guard","changed_components":["valuation_repricing_score","positioning_overheat_score","c09_blowoff_guard_score","customer_quality_score_guard","revision_score_guard"],"component_delta_explanation":"C09 does not reward price-only valuation repricing as a positive-stage component. Prior direct-equipment Stage2 evidence can remain valid, but post-rerating valuation/positioning excess routes to 4B overlay; weak customer/revision paths are blocked from Green.","MFE_90D_pct":1.74,"MAE_90D_pct":-30.35,"score_return_alignment_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L14_C09_003160_DI_TESTER_THEME_BLOWOFF_COUNTEREXAMPLE","trigger_id":"R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN","symbol":"003160","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":88,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":86,"execution_risk_score":78,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":82,"tester_theme_score":70},"weighted_score_before":79,"stage_label_before":"Stage3-FalseGreen-risk","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":88,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":86,"execution_risk_score":78,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":82,"tester_theme_score":70,"c09_blowoff_guard_score":95},"weighted_score_after":57,"stage_label_after":"Stage2-Watch / no Green without order bridge","changed_components":["valuation_repricing_score","positioning_overheat_score","c09_blowoff_guard_score","customer_quality_score_guard","revision_score_guard"],"component_delta_explanation":"C09 does not reward price-only valuation repricing as a positive-stage component. Prior direct-equipment Stage2 evidence can remain valid, but post-rerating valuation/positioning excess routes to 4B overlay; weak customer/revision paths are blocked from Green.","MFE_90D_pct":35.98,"MAE_90D_pct":-44.19,"score_return_alignment_label":"theme_relative_strength_false_green_counterexample","current_profile_verdict":"current_profile_false_positive"}

```

### 25.5 shadow_weight rows
```csv

row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes

shadow_weight,c09_valuation_blowoff_overlay,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,Extreme post-Stage2 HBM/AI equipment rerating should become 4B overlay when valuation/positioning and peak-proximity are high.,4 positive blowoff rows showed avg MAE90 below -50% after peak/near-peak triggers.,R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF|R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF|R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF|R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF,4,4,3,medium,canonical_shadow_only,not production; post-calibrated residual

shadow_weight,c09_green_customer_revision_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,Theme-only equipment/test-adjacent rows should not reach Green without customer-quality or revision bridge.,3 counterexamples had avg MFE90 17.13% vs avg MAE90 -40.67%.,R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF|R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF|R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN,3,3,3,medium,canonical_shadow_only,blocks false positive Green

shadow_weight,full_4b_requires_non_price_evidence,existing_axis_strengthened,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,true,true,0,"C09 confirms existing full-4B non-price requirement, but adds canonical-specific 4B-Watch overlay.",Prevents treating pure local price peaks as hard 4B while still recording overheat.,R2L14_C09_042700_HANMI_4B_VALUATION_BLOWOFF|R2L14_C09_089030_TECHWING_4B_VALUATION_BLOWOFF|R2L14_C09_058470_RINO_4B_VALUATION_BLOWOFF|R2L14_C09_131290_TSE_LATE_GREEN_BLOWOFF|R2L14_C09_095340_ISC_FALSE_GREEN_BLOWOFF|R2L14_C09_064290_INTEKPLUS_FAILED_BLOWOFF|R2L14_C09_003160_DI_TESTER_THEME_FALSE_GREEN,7,7,3,medium,axis_stress_test,"strengthen interpretation, no global delta"

```

### 25.6 residual_contribution row
```jsonl

{"row_type":"residual_contribution","round":"R2","loop":"14","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","scheduled_round":"R2","scheduled_loop":14,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":7,"reused_case_count":7,"new_symbol_count":7,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":4,"counterexample_count":3,"current_profile_error_count":6,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage3_green_total_min","stage3_green_revision_min"],"residual_error_types_found":["4B_too_late_in_direct_equipment_blowoff","false_positive_green_in_theme_only_equipment","late_green_near_full_window_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"C09 had no prior R2 loop coverage. Underlying stock-web rows are reused from C07/C08 only as input evidence; the canonical archetype, trigger family, and rule proposal are new."}

```

### 25.7 narrative_only rows
```jsonl

{"row_type":"narrative_only","case_id":"R2L14_C09_SOURCE_URL_ENRICHMENT","symbol":"MULTI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","reason":"direct historical evidence URLs should be enriched before production promotion; current loop is shadow-only and uses prior R2 v12 evidence families plus stock-web OHLC","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}

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

completed_round = R2
completed_loop = 14
next_round = R3
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass

## 28. Source Notes

price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap

Local duplicate-avoidance basis:
- e2r_stock_web_v12_residual_round_R2_loop_10_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
- e2r_stock_web_v12_residual_round_R2_loop_11_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
- e2r_stock_web_v12_residual_round_R2_loop_12_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
- e2r_stock_web_v12_residual_round_R2_loop_13_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md

This MD is a standalone historical calibration artifact. It contains no investment recommendation language and makes no live/current candidate claim.
