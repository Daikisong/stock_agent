# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R4_loop_16_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
scheduled_round: R4
scheduled_loop: 16
completed_round: R4
completed_loop: 16
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: NONFERROUS_STEEL_PRODUCT_SPREAD_PASS_THROUGH_GUARD
loop_objective: ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "stage2_actionable_bonus_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test"]
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
round_schedule_status: valid
round_sector_consistency: pass
created_at_utc: 2026-05-29T01:46:57.712420+00:00
```

This loop adds **4** new independent cases, **2** counterexamples, and **4** residual errors for **R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE**.

No live candidate scan was performed, no broker/API/trading action was performed, no `stock_agent` source code was opened, and no production scoring was changed. This is a standalone historical calibration artifact.

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

C15 behaves like a furnace, not a headline machine. Price heat matters only when it is contained by product-specific spread duration and pass-through. A price-only beta spike can glow red for a week and still leave no ingot for earnings.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
| --- | --- |
| scheduled_round | R4 |
| scheduled_loop | 16 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE |
| fine_archetype_id | NONFERROUS_STEEL_PRODUCT_SPREAD_PASS_THROUGH_GUARD |
| loop_objective | coverage_gap_fill / sector_specific_rule_discovery / canonical_archetype_compression / counterexample_mining / stage2_actionable_bonus_stress_test / green_strictness_stress_test / 4B_non_price_requirement_stress_test |

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`, so the round-sector pair passes the hard gate. C15 is selected because local R4 coverage was heavier in C17 and the C15 row set still needed small/mid nonferrous and special-steel counterexamples.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 state showed R4 loops 10~15 already complete, with C17 repeated, C15 covered once, and C16 covered once. Prior C15 symbols were `005490`, `004020`, `103140`, and `010130`; prior C16 symbols included `025860`, `047400`, and `000910`. This file uses `025820`, `012800`, `018470`, and `001430`, so there is no same symbol + same trigger_date + same entry_date reuse.
| duplicate gate | status |
| --- | --- |
| same symbol + same trigger_date + same entry_date reused | no |
| same canonical archetype repeated with new symbols/families | yes, allowed |
| minimum_new_independent_case_ratio | 4/4 = 1.00 |
| minimum_new_symbol_count | 4 >= 2 |
| minimum_counterexample_count | 2 >= 1 |
| minimum_positive_case_count | 2 >= 1 |

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
| --- | --- |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The manifest max date is used as the forward-window ceiling. Price basis is `tradable_raw`; raw/unadjusted corporate-action caveats remain active. Calibration-safe tradable shards exclude zero-volume and invalid OHLC rows.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | corporate-action status | selected 180D window | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| 025820 | 이구산업 | atlas/symbol_profiles/025/025820.json | clean_180D_window; corporate_action_candidate_dates=1996-01-03|2007-04-30|2007-07-11, no overlap | entry~D+180 does not overlap candidate dates | true |
| 012800 | 대창 | atlas/symbol_profiles/012/012800.json | clean_180D_window; corporate_action_candidate_dates=1998-12-15|2008-04-16, no overlap | entry~D+180 does not overlap candidate dates | true |
| 018470 | 조일알미늄 | atlas/symbol_profiles/018/018470.json | clean_180D_window; corporate_action_candidate_dates=1996-01-03|1999-12-07|2012-05-04, no overlap | entry~D+180 does not overlap candidate dates | true |
| 001430 | 세아베스틸지주 | atlas/symbol_profiles/001/001430.json | clean_180D_window; corporate_action_candidate_dates=1996-01-03|1997-01-03|1999-04-08|1999-05-18|2003-12-26, no overlap | entry~D+180 does not overlap candidate dates | true |

All representative triggers are historical, have an entry date inside stock-web tradable shards, have at least 180 forward trading days before the manifest max date, and have no corporate-action candidate overlap in the tested 180D window.

## 6. Canonical Archetype Compression Map
| fine_archetype_id | canonical_archetype_id | compression logic |
| --- | --- | --- |
| COPPER_ROLLED_PRODUCT_PASS_THROUGH_SUPERCYCLE | C15_MATERIAL_SPREAD_SUPERCYCLE | positive only when copper price converts into product spread/pass-through |
| COPPER_BETA_WITHOUT_DURABLE_PASS_THROUGH | C15_MATERIAL_SPREAD_SUPERCYCLE | counterexample: price beta without spread duration is not Green |
| ALUMINUM_ROLLED_PRODUCT_SUPERCYCLE_WITH_4B_OVERLAY | C15_MATERIAL_SPREAD_SUPERCYCLE | positive entry plus 4B overlay separation |
| SPECIAL_STEEL_LATE_CYCLE_SPREAD_FALSE_POSITIVE | C15_MATERIAL_SPREAD_SUPERCYCLE | counterexample: late special-steel spread headline after local peak |

## 7. Case Selection Summary
| case_id | symbol | company | role | case_type | current_profile_verdict | why selected |
| --- | --- | --- | --- | --- | --- | --- |
| R4L16_C15_025820_LEECU_COPPER_SPREAD_20210415 | 025820 | 이구산업 | positive | structural_success | current_profile_missed_structural | structural_copper_spread_success_before_full_revision |
| R4L16_C15_012800_DAECHANG_LATE_COPPER_BETA_20210511 | 012800 | 대창 | counterexample | false_positive_green | current_profile_false_positive | late_copper_beta_false_positive_after_spread_move |
| R4L16_C15_018470_CHOIL_ALUMINUM_SUPERCYCLE_20210713 | 018470 | 조일알미늄 | positive | high_mae_success | current_profile_4B_too_late | aluminum_spread_success_but_4B_overlay_required |
| R4L16_C15_001430_SEAHBESTEEL_LATE_SPECIAL_STEEL_20210511 | 001430 | 세아베스틸지주 | counterexample | failed_rerating | current_profile_false_positive | late_special_steel_spread_false_positive |

## 8. Positive vs Counterexample Balance
| metric | value |
| --- | --- |
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 5 |

## 9. Evidence Source Map
| symbol | trigger_date | evidence family | source status | validation use |
| --- | --- | --- | --- | --- |
| 025820 | 2021-04-15 | COPPER_ROLLED_PRODUCT_PASS_THROUGH_SUPERCYCLE | Songdaiki/stock-web tradable rows; historical public copper/nonferrous spread context; exact contemporaneous report URL enrichment pending | historical calibration only; no live scan |
| 012800 | 2021-05-11 | COPPER_BETA_WITHOUT_DURABLE_PASS_THROUGH | Songdaiki/stock-web tradable rows; historical copper/brass product spread context; exact contemporaneous report URL enrichment pending | historical calibration only; no live scan |
| 018470 | 2021-07-13 | ALUMINUM_ROLLED_PRODUCT_SUPERCYCLE_WITH_4B_OVERLAY | Songdaiki/stock-web tradable rows; historical aluminum/product spread context; exact contemporaneous report URL enrichment pending | historical calibration only; no live scan |
| 001430 | 2021-05-11 | SPECIAL_STEEL_LATE_CYCLE_SPREAD_FALSE_POSITIVE | Songdaiki/stock-web tradable rows; historical special-steel spread context; exact contemporaneous report URL enrichment pending | historical calibration only; no live scan |

## 10. Price Data Source Map
| symbol | price_shard_path | profile_path | sampled stock-web rows used |
| --- | --- | --- | --- |
| 025820 | atlas/ohlcv_tradable_by_symbol_year/025/025820/2021.csv | atlas/symbol_profiles/025/025820.json | 2021-04-15 close 3,255; 2021-05-07 high 5,520 |
| 012800 | atlas/ohlcv_tradable_by_symbol_year/012/012800/2021.csv | atlas/symbol_profiles/012/012800.json | 2021-05-11 close 2,910; 2021-05-12 high 3,015; 2021-05-26 low 2,300 |
| 018470 | atlas/ohlcv_tradable_by_symbol_year/018/018470/2021.csv | atlas/symbol_profiles/018/018470.json | 2021-07-13 close 1,045; 2021-09-08 high 3,805; 2021-12-01 low 1,970 |
| 001430 | atlas/ohlcv_tradable_by_symbol_year/001/001430/2021.csv | atlas/symbol_profiles/001/001430.json | 2021-05-11 close 34,350; 2021-05-11 high 36,450; 2021-05-26 low 28,450 |

## 11. Case-by-Case Trigger Grid
| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 | stage3 | 4B | 4C | aggregate role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L16_C15_025820_T1 | 025820 | Stage2-Actionable | 2021-04-15 | 2021-04-15 | 3255 | public_event_or_disclosure,relative_strength,capacity_or_volume_route,early_revision_signal | margin_bridge,financial_visibility | positioning_overheat,valuation_blowoff |  | representative |
| R4L16_C15_012800_T1 | 012800 | Stage3-Green-risk | 2021-05-11 | 2021-05-11 | 2910 | public_event_or_disclosure,relative_strength | multiple_public_sources | positioning_overheat,price_only_local_peak | thesis_evidence_broken | representative |
| R4L16_C15_018470_T1 | 018470 | Stage2-Actionable | 2021-07-13 | 2021-07-13 | 1045 | public_event_or_disclosure,capacity_or_volume_route,relative_strength,early_revision_signal | margin_bridge,multiple_public_sources,financial_visibility | valuation_blowoff,positioning_overheat,price_only_local_peak |  | representative |
| R4L16_C15_001430_T1 | 001430 | Stage3-Green-risk | 2021-05-11 | 2021-05-11 | 34350 | public_event_or_disclosure,relative_strength,early_revision_signal | confirmed_revision,margin_bridge | positioning_overheat,margin_or_backlog_slowdown | thesis_evidence_broken | representative |
| R4L16_C15_018470_4B_OVERLAY_20210908 | 018470 | 4B-Watch-Overlay | 2021-09-08 | 2021-09-08 | 3605 |  |  | valuation_blowoff,positioning_overheat,price_only_local_peak |  | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | symbol | entry | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L16_C15_025820_T1 | 025820 | 2021-04-15 | 3255 | 69.59 | 69.59 | 69.59 | -8.45 | -8.45 | -15.51 | 2021-05-07 | 5520 | -32.97 | structural_copper_spread_success_before_full_revision |
| R4L16_C15_012800_T1 | 012800 | 2021-05-11 | 2910 | 3.61 | 3.61 | 3.61 | -20.96 | -20.96 | -20.96 | 2021-05-12 | 3015 | -23.71 | late_copper_beta_false_positive_after_spread_move |
| R4L16_C15_018470_T1 | 018470 | 2021-07-13 | 1045 | 82.78 | 264.11 | 264.11 | -1.44 | -1.44 | -1.44 | 2021-09-08 | 3805 | -48.23 | aluminum_spread_success_but_4B_overlay_required |
| R4L16_C15_001430_T1 | 001430 | 2021-05-11 | 34350 | 6.11 | 6.11 | 6.11 | -17.18 | -17.18 | -27.07 | 2021-05-11 | 36450 | -31.55 | late_special_steel_spread_false_positive |
| R4L16_C15_018470_4B_OVERLAY_20210908 | 018470 | 2021-09-08 | 3605 | 5.55 | 5.55 | 5.55 | -17.34 | -43.13 | -48.23 | 2021-09-08 | 3805 | -48.23 | 4B_overlay_success_for_high_MAE_success |

## 13. Current Calibrated Profile Stress Test
| case | current profile likely action | actual MFE/MAE alignment | verdict |
| --- | --- | --- | --- |
| 025820 | Stage2-Actionable but not enough for Yellow/Green due small-cap spread evidence | 69.59% MFE90 with -8.45% MAE90: too conservative | current_profile_missed_structural |
| 012800 | May overheat could be promoted by price-beta + relative strength | 3.61% MFE90 versus -20.96% MAE90: false positive | current_profile_false_positive |
| 018470 | Entry reasonable but no overlay timing | 264.11% MFE90 but -48.23% drawdown after peak: 4B too late | current_profile_4B_too_late |
| 001430 | Late steel spread confirmation risks Green-borderline | 6.11% MFE90 versus -17.18% MAE90: false positive | current_profile_false_positive |

Existing Stage2 bonus is kept but C15 needs a product-spread component gate. Yellow/Green thresholds are not globally changed; the rule is a shadow component guard. Price-only blowoff and full 4B non-price requirement are strengthened, not re-proposed globally.

## 14. Stage2 / Yellow / Green Comparison
| symbol | Stage2 entry quality | Yellow/Green risk | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- |
| 025820 | good: spread and pass-through early | Green too strict without small-cap spread bridge | not_applicable | missed structural positive |
| 012800 | bad if entered after price spike | Green too loose if relative strength dominates | 1.00+ local peak risk | late beta false positive |
| 018470 | good Stage2 entry | Green acceptable only with 4B overlay | 0.10~0.30 conceptual | large upside but later overlay needed |
| 001430 | late Stage2/Green | Green too loose after local peak | 1.00 local peak risk | late special-steel false positive |

## 15. 4B Local vs Full-window Timing Audit
| trigger | symbol | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
| --- | --- | --- | --- | --- | --- |
| R4L16_C15_018470_4B_OVERLAY_20210908 | 018470 | 1.0 | 1.0 | price_only|valuation_blowoff|positioning_overheat | good timing as watch overlay; price-only cannot be treated as full 4B exit |
| R4L16_C15_012800_T1 | 012800 | near local peak | near full observed peak | price_only|positioning_overheat | representative trigger should be downgraded |
| R4L16_C15_001430_T1 | 001430 | near local peak | near full observed peak | margin slowdown|positioning overheat | late-cycle Green should be blocked |

## 16. 4C Protection Audit
| symbol | 4C evidence field | protection label | comment |
| --- | --- | --- | --- |
| 012800 | thesis_evidence_broken | hard_4c_success_if_beta_break_confirmed | Commodity beta faded quickly after local peak; 4C protects against using late price spike as evidence. |
| 001430 | thesis_evidence_broken | hard_4c_success_if_inventory_cycle_break_confirmed | Late spread/inventory cycle reversal explains the negative MAE. |
| 018470 | none in representative entry | thesis_break_watch_only | The problem is overlay timing, not immediate thesis break. |

## 17. Sector-Specific Rule Candidate

**L4 sector shadow rule:** add `L4_product_spread_duration_bonus` only when the spread is product-specific and has a pass-through or margin bridge. Add `L4_inventory_cycle_guard` when the evidence is mostly price beta after a local peak.
| axis | scope | direction | reason |
| --- | --- | --- | --- |
| L4_product_spread_duration_bonus | sector_specific | +1 to +2 | captures small/mid nonferrous positives before full revision |
| L4_inventory_cycle_guard | sector_specific | -2 to -4 | blocks late steel/copper beta when upside is already consumed |

## 18. Canonical-Archetype Rule Candidate

**C15 canonical shadow rule:** product-specific spread duration + input-cost pass-through should be rewarded; price-only commodity beta after a local peak should be capped at Stage2-Watch unless confirmed margin or customer/order evidence arrives.
| axis | scope | tested delta | backtest effect |
| --- | --- | --- | --- |
| C15_spread_duration_pass_through_bonus | canonical_archetype_specific | +2 to +4 | keeps 025820 and 018470 as valid positives |
| C15_late_beta_inventory_guard | canonical_archetype_specific | -4 to -8 | downgrades 012800 and 001430 false positives |

## 19. Before / After Backtest Comparison
| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | alignment |
| --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | global_current_proxy | 4 | 85.86 | -12.01 | 0.5 | mixed; price beta overpromotes late copper/special-steel cases |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 85.86 | -12.01 | 0.75 | worse; late beta is confused with spread evidence |
| P1_sector_specific_candidate_profile | sector_specific | 4 | 85.86 | -12.01 | 0.25 | better; rejects late beta while keeping copper/aluminum positives |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 4 | 85.86 | -12.01 | 0.0 | best candidate; separates durable product-spread from late-cycle beta |
| P3_counterexample_guard_profile | counterexample_guard | 4 | 166.85 | -4.94 | 0.0 | safest but may undercount moderate steel spread positives |

## 20. Score-Return Alignment Matrix
| symbol | before score/label | after score/label | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- |
| 025820 | 74 / Stage2-Actionable | 82 / Stage3-Yellow-shadow | 69.59 | -8.45 | structural_copper_spread_success_before_full_revision |
| 012800 | 88 / Stage3-Green-borderline | 66 / Stage2-Watch-shadow | 3.61 | -20.96 | late_copper_beta_false_positive_after_spread_move |
| 018470 | 81 / Stage3-Yellow | 86 / Stage3-Yellow-plus-4B-watch-shadow | 264.11 | -1.44 | aluminum_spread_success_but_4B_overlay_required |
| 001430 | 87 / Stage3-Green-borderline | 69 / Stage2-Watch-shadow | 6.11 | -17.18 | late_special_steel_spread_false_positive |

Raw component detail is available in the `score_simulation` JSONL rows below. Canonical keys are present for every score row; supplemental C15 keys include `spread_duration_score`, `product_specificity_score`, `input_cost_pass_through_score`, `inventory_cycle_risk_score`, `event_premium_exclusion_score`, and `positioning_overheat_score`.

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | NONFERROUS_STEEL_PRODUCT_SPREAD_PASS_THROUGH_GUARD | 2 | 2 | 1 | 2 | 4 | 0 | 5 | 4 | 4 | True | True | C15 small/mid nonferrous and late-cycle false-positive coverage improved; still needs holdout in zinc/nickel and pulp/material subfamilies |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"]
residual_error_types_found: ["missed_small_midcap_spread_positive", "late_copper_beta_false_positive", "4B_overlay_late_after_aluminum_spread_success", "late_special_steel_false_positive"]
new_axis_proposed: ["C15_spread_duration_pass_through_bonus", "C15_late_beta_inventory_guard"]
existing_axis_strengthened: ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]
existing_axis_weakened: []
existing_axis_kept: ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "hard_4c_thesis_break_routes_to_4c"]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: "canonical_archetype_rule_candidate"
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope
| scope | included? | notes |
| --- | --- | --- |
| historical trigger-level OHLC backtest | yes | stock-web tradable_raw rows only |
| current/live candidate discovery | no | explicitly disabled |
| stock_agent code inspection or patch | no | not performed |
| production scoring change | no | shadow-only |
| brokerage/API/auto-trading | no | not performed |
| 1Y/2Y quantitative weight calibration | no | 30/90/180D are used for weight proposal; 1Y/2Y left null in rows |

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C15_spread_duration_pass_through_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Reward product-specific spread duration plus pass-through evidence","Keeps 025820/018470 positives without global threshold change","R4L16_C15_025820_T1|R4L16_C15_018470_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C15_late_beta_inventory_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Downgrade price-only commodity beta after local peak or inventory-cycle reversal","Blocks 012800/001430 false positives","R4L16_C15_012800_T1|R4L16_C15_001430_T1",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R4L16_C15_025820_LEECU_COPPER_SPREAD_20210415","symbol":"025820","company_name":"이구산업","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_ROLLED_PRODUCT_PASS_THROUGH_SUPERCYCLE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L16_C15_025820_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_copper_spread_success_before_full_revision","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"new R4/C15 symbol and trigger family; not live discovery; historical calibration only"}
{"row_type":"case","case_id":"R4L16_C15_012800_DAECHANG_LATE_COPPER_BETA_20210511","symbol":"012800","company_name":"대창","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_BETA_WITHOUT_DURABLE_PASS_THROUGH","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R4L16_C15_012800_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late_copper_beta_false_positive_after_spread_move","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new R4/C15 symbol and trigger family; not live discovery; historical calibration only"}
{"row_type":"case","case_id":"R4L16_C15_018470_CHOIL_ALUMINUM_SUPERCYCLE_20210713","symbol":"018470","company_name":"조일알미늄","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_ROLLED_PRODUCT_SUPERCYCLE_WITH_4B_OVERLAY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R4L16_C15_018470_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aluminum_spread_success_but_4B_overlay_required","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new R4/C15 symbol and trigger family; not live discovery; historical calibration only"}
{"row_type":"case","case_id":"R4L16_C15_001430_SEAHBESTEEL_LATE_SPECIAL_STEEL_20210511","symbol":"001430","company_name":"세아베스틸지주","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIAL_STEEL_LATE_CYCLE_SPREAD_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L16_C15_001430_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late_special_steel_spread_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new R4/C15 symbol and trigger family; not live discovery; historical calibration only"}
{"row_type":"trigger","trigger_id":"R4L16_C15_025820_T1","case_id":"R4L16_C15_025820_LEECU_COPPER_SPREAD_20210415","symbol":"025820","company_name":"이구산업","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_ROLLED_PRODUCT_PASS_THROUGH_SUPERCYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"material_spread_supercycle","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","green_strictness_stress_test","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2021-04-15","entry_date":"2021-04-15","entry_price":3255,"evidence_available_at_that_date":"Copper price/spread and rolled-product pass-through were visible before a fully confirmed revision narrative. The stock-web row shows the 2021-04-15 close at 3,255 and the following copper-beta peak at 5,520 on 2021-05-07.","evidence_source":"Songdaiki/stock-web tradable rows; historical public copper/nonferrous spread context; exact contemporaneous report URL enrichment pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025820/2021.csv","profile_path":"atlas/symbol_profiles/025/025820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":69.59,"MFE_90D_pct":69.59,"MFE_180D_pct":69.59,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.45,"MAE_90D_pct":-8.45,"MAE_180D_pct":-15.51,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-07","peak_price":5520,"drawdown_after_peak_pct":-32.97,"green_lateness_ratio":"not_applicable_or_case_specific","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"representative_entry_not_4B","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_copper_spread_success_before_full_revision","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; corporate_action_candidate_dates=1996-01-03|2007-04-30|2007-07-11, no overlap","same_entry_group_id":"025820_2021-04-15_3255","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L16_C15_012800_T1","case_id":"R4L16_C15_012800_DAECHANG_LATE_COPPER_BETA_20210511","symbol":"012800","company_name":"대창","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_BETA_WITHOUT_DURABLE_PASS_THROUGH","sector":"소재·스프레드·전략자원","primary_archetype":"material_spread_supercycle","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","green_strictness_stress_test","4B_non_price_requirement_stress_test"],"trigger_type":"Stage3-Green-risk","trigger_date":"2021-05-11","entry_date":"2021-05-11","entry_price":2910,"evidence_available_at_that_date":"By the time the copper-beta move had become obvious, the stock had already consumed most of the 2021 copper theme. The next-day high was only 3,015 while the 30D low reached 2,300, making it a clean counterexample to price-beta-as-spread proof.","evidence_source":"Songdaiki/stock-web tradable rows; historical copper/brass product spread context; exact contemporaneous report URL enrichment pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012800/2021.csv","profile_path":"atlas/symbol_profiles/012/012800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.61,"MFE_90D_pct":3.61,"MFE_180D_pct":3.61,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.96,"MAE_90D_pct":-20.96,"MAE_180D_pct":-20.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-12","peak_price":3015,"drawdown_after_peak_pct":-23.71,"green_lateness_ratio":"not_applicable_or_case_specific","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"representative_entry_not_4B","four_b_evidence_type":["positioning_overheat","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"late_copper_beta_false_positive_after_spread_move","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; corporate_action_candidate_dates=1998-12-15|2008-04-16, no overlap","same_entry_group_id":"012800_2021-05-11_2910","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L16_C15_018470_T1","case_id":"R4L16_C15_018470_CHOIL_ALUMINUM_SUPERCYCLE_20210713","symbol":"018470","company_name":"조일알미늄","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_ROLLED_PRODUCT_SUPERCYCLE_WITH_4B_OVERLAY","sector":"소재·스프레드·전략자원","primary_archetype":"material_spread_supercycle","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","green_strictness_stress_test","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2021-07-13","entry_date":"2021-07-13","entry_price":1045,"evidence_available_at_that_date":"Aluminum sheet/rolled-product spread and tight supply narrative produced a genuine supercycle leg. The row sequence from 2021-07-13 to 2021-09-08 shows a move from 1,045 close to a 3,805 high, but the later drawdown argues for a separate 4B overlay rather than rejecting the entry signal.","evidence_source":"Songdaiki/stock-web tradable rows; historical aluminum/product spread context; exact contemporaneous report URL enrichment pending","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018470/2021.csv","profile_path":"atlas/symbol_profiles/018/018470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":82.78,"MFE_90D_pct":264.11,"MFE_180D_pct":264.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.44,"MAE_90D_pct":-1.44,"MAE_180D_pct":-1.44,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-08","peak_price":3805,"drawdown_after_peak_pct":-48.23,"green_lateness_ratio":"not_applicable_or_case_specific","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"representative_entry_not_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"aluminum_spread_success_but_4B_overlay_required","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; corporate_action_candidate_dates=1996-01-03|1999-12-07|2012-05-04, no overlap","same_entry_group_id":"018470_2021-07-13_1045","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L16_C15_001430_T1","case_id":"R4L16_C15_001430_SEAHBESTEEL_LATE_SPECIAL_STEEL_20210511","symbol":"001430","company_name":"세아베스틸지주","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIAL_STEEL_LATE_CYCLE_SPREAD_FALSE_POSITIVE","sector":"소재·스프레드·전략자원","primary_archetype":"material_spread_supercycle","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","green_strictness_stress_test","4B_non_price_requirement_stress_test"],"trigger_type":"Stage3-Green-risk","trigger_date":"2021-05-11","entry_date":"2021-05-11","entry_price":34350,"evidence_available_at_that_date":"Special-steel price momentum and steel spread beta looked attractive at the local high, but the stock-web path delivered only 6.11% MFE versus -17.18% 30D MAE. This is a late-cycle counterexample requiring inventory-cycle and pass-through guards.","evidence_source":"Songdaiki/stock-web tradable rows; historical special-steel spread context; exact contemporaneous report URL enrichment pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge"],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001430/2021.csv","profile_path":"atlas/symbol_profiles/001/001430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.11,"MFE_90D_pct":6.11,"MFE_180D_pct":6.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.18,"MAE_90D_pct":-17.18,"MAE_180D_pct":-27.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-11","peak_price":36450,"drawdown_after_peak_pct":-31.55,"green_lateness_ratio":"not_applicable_or_case_specific","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"representative_entry_not_4B","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"late_special_steel_spread_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; corporate_action_candidate_dates=1996-01-03|1997-01-03|1999-04-08|1999-05-18|2003-12-26, no overlap","same_entry_group_id":"001430_2021-05-11_34350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L16_C15_018470_4B_OVERLAY_20210908","case_id":"R4L16_C15_018470_CHOIL_ALUMINUM_SUPERCYCLE_20210713","symbol":"018470","company_name":"조일알미늄","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_ROLLED_PRODUCT_SUPERCYCLE_WITH_4B_OVERLAY","sector":"소재·스프레드·전략자원","primary_archetype":"material_spread_supercycle","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","green_strictness_stress_test","4B_non_price_requirement_stress_test"],"trigger_type":"4B-Watch-Overlay","trigger_date":"2021-09-08","entry_date":"2021-09-08","entry_price":3605,"evidence_available_at_that_date":"Stock-web row shows 2021-09-08 high 3,805 after the aluminum rerating; this is a price/positioning overlay only and is not a Stage2/Stage3 promotion trigger.","evidence_source":"Songdaiki/stock-web tradable rows, 018470 2021.csv","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018470/2021.csv","profile_path":"atlas/symbol_profiles/018/018470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.55,"MFE_90D_pct":5.55,"MFE_180D_pct":5.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.34,"MAE_90D_pct":-43.13,"MAE_180D_pct":-48.23,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-08","peak_price":3805,"drawdown_after_peak_pct":-48.23,"green_lateness_ratio":"not_applicable_4B_overlay","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_and_full_window_4B_timing_but_price_only_not_full_exit","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_for_high_MAE_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"018470_2021-09-08_3605","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case overlay timing only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L16_C15_025820_LEECU_COPPER_SPREAD_20210415","trigger_id":"R4L16_C15_025820_T1","symbol":"025820","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":5,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":12,"product_specificity_score":14,"input_cost_pass_through_score":8,"inventory_cycle_risk_score":-1,"event_premium_exclusion_score":0,"positioning_overheat_score":-2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":5,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":12,"product_specificity_score":14,"input_cost_pass_through_score":8,"inventory_cycle_risk_score":-1,"event_premium_exclusion_score":0,"positioning_overheat_score":-2},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"P0 proxy; no C15 shadow spread-duration/pass-through guard applied.","MFE_90D_pct":69.59,"MAE_90D_pct":-8.45,"score_return_alignment_label":"structural_copper_spread_success_before_full_revision","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R4L16_C15_025820_LEECU_COPPER_SPREAD_20210415","trigger_id":"R4L16_C15_025820_T1","symbol":"025820","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":5,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":12,"product_specificity_score":14,"input_cost_pass_through_score":8,"inventory_cycle_risk_score":-1,"event_premium_exclusion_score":0,"positioning_overheat_score":-2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":4,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":9,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":16,"product_specificity_score":18,"input_cost_pass_through_score":11,"inventory_cycle_risk_score":-1,"event_premium_exclusion_score":0,"positioning_overheat_score":-2},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-shadow","changed_components":["spread_duration_score","product_specificity_score","input_cost_pass_through_score","margin_bridge_score","revision_score"],"component_delta_explanation":"C15 shadow separates product-specific spread duration and input-cost pass-through from late price beta or inventory-cycle premium.","MFE_90D_pct":69.59,"MAE_90D_pct":-8.45,"score_return_alignment_label":"structural_copper_spread_success_before_full_revision","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L16_C15_012800_DAECHANG_LATE_COPPER_BETA_20210511","trigger_id":"R4L16_C15_012800_T1","symbol":"012800","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":17,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":13,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":5,"product_specificity_score":6,"input_cost_pass_through_score":2,"inventory_cycle_risk_score":-8,"event_premium_exclusion_score":0,"positioning_overheat_score":-8},"weighted_score_before":88,"stage_label_before":"Stage3-Green-borderline","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":17,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":13,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":5,"product_specificity_score":6,"input_cost_pass_through_score":2,"inventory_cycle_risk_score":-8,"event_premium_exclusion_score":0,"positioning_overheat_score":-8},"weighted_score_after":88,"stage_label_after":"Stage3-Green-borderline","changed_components":[],"component_delta_explanation":"P0 proxy; no C15 shadow spread-duration/pass-through guard applied.","MFE_90D_pct":3.61,"MAE_90D_pct":-20.96,"score_return_alignment_label":"late_copper_beta_false_positive_after_spread_move","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R4L16_C15_012800_DAECHANG_LATE_COPPER_BETA_20210511","trigger_id":"R4L16_C15_012800_T1","symbol":"012800","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":17,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":13,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":5,"product_specificity_score":6,"input_cost_pass_through_score":2,"inventory_cycle_risk_score":-8,"event_premium_exclusion_score":0,"positioning_overheat_score":-8},"weighted_score_before":88,"stage_label_before":"Stage3-Green-borderline","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":-11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":5,"product_specificity_score":4,"input_cost_pass_through_score":0,"inventory_cycle_risk_score":-12,"event_premium_exclusion_score":0,"positioning_overheat_score":-8},"weighted_score_after":66,"stage_label_after":"Stage2-Watch-shadow","changed_components":["relative_strength_score","valuation_repricing_score","execution_risk_score","inventory_cycle_risk_score","product_specificity_score","input_cost_pass_through_score"],"component_delta_explanation":"C15 shadow separates product-specific spread duration and input-cost pass-through from late price beta or inventory-cycle premium.","MFE_90D_pct":3.61,"MAE_90D_pct":-20.96,"score_return_alignment_label":"late_copper_beta_false_positive_after_spread_move","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L16_C15_018470_CHOIL_ALUMINUM_SUPERCYCLE_20210713","trigger_id":"R4L16_C15_018470_T1","symbol":"018470","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":6,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":11,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":15,"product_specificity_score":14,"input_cost_pass_through_score":9,"inventory_cycle_risk_score":-3,"event_premium_exclusion_score":0,"positioning_overheat_score":-5},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":6,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":11,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":15,"product_specificity_score":14,"input_cost_pass_through_score":9,"inventory_cycle_risk_score":-3,"event_premium_exclusion_score":0,"positioning_overheat_score":-5},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"P0 proxy; no C15 shadow spread-duration/pass-through guard applied.","MFE_90D_pct":264.11,"MAE_90D_pct":-1.44,"score_return_alignment_label":"aluminum_spread_success_but_4B_overlay_required","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R4L16_C15_018470_CHOIL_ALUMINUM_SUPERCYCLE_20210713","trigger_id":"R4L16_C15_018470_T1","symbol":"018470","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":6,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":11,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":15,"product_specificity_score":14,"input_cost_pass_through_score":9,"inventory_cycle_risk_score":-3,"event_premium_exclusion_score":0,"positioning_overheat_score":-5},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":6,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":11,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":18,"product_specificity_score":16,"input_cost_pass_through_score":11,"inventory_cycle_risk_score":-3,"event_premium_exclusion_score":0,"positioning_overheat_score":-8},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-plus-4B-watch-shadow","changed_components":["spread_duration_score","product_specificity_score","input_cost_pass_through_score","positioning_overheat_score"],"component_delta_explanation":"C15 shadow separates product-specific spread duration and input-cost pass-through from late price beta or inventory-cycle premium.","MFE_90D_pct":264.11,"MAE_90D_pct":-1.44,"score_return_alignment_label":"aluminum_spread_success_but_4B_overlay_required","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L16_C15_001430_SEAHBESTEEL_LATE_SPECIAL_STEEL_20210511","trigger_id":"R4L16_C15_001430_T1","symbol":"001430","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":8,"product_specificity_score":10,"input_cost_pass_through_score":4,"inventory_cycle_risk_score":-8,"event_premium_exclusion_score":0,"positioning_overheat_score":-9},"weighted_score_before":87,"stage_label_before":"Stage3-Green-borderline","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":8,"product_specificity_score":10,"input_cost_pass_through_score":4,"inventory_cycle_risk_score":-8,"event_premium_exclusion_score":0,"positioning_overheat_score":-9},"weighted_score_after":87,"stage_label_after":"Stage3-Green-borderline","changed_components":[],"component_delta_explanation":"P0 proxy; no C15 shadow spread-duration/pass-through guard applied.","MFE_90D_pct":6.11,"MAE_90D_pct":-17.18,"score_return_alignment_label":"late_special_steel_spread_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R4L16_C15_001430_SEAHBESTEEL_LATE_SPECIAL_STEEL_20210511","trigger_id":"R4L16_C15_001430_T1","symbol":"001430","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":8,"product_specificity_score":10,"input_cost_pass_through_score":4,"inventory_cycle_risk_score":-8,"event_premium_exclusion_score":0,"positioning_overheat_score":-9},"weighted_score_before":87,"stage_label_before":"Stage3-Green-borderline","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":8,"product_specificity_score":10,"input_cost_pass_through_score":1,"inventory_cycle_risk_score":-13,"event_premium_exclusion_score":0,"positioning_overheat_score":-11},"weighted_score_after":69,"stage_label_after":"Stage2-Watch-shadow","changed_components":["relative_strength_score","valuation_repricing_score","inventory_cycle_risk_score","input_cost_pass_through_score","positioning_overheat_score"],"component_delta_explanation":"C15 shadow separates product-specific spread duration and input-cost pass-through from late price beta or inventory-cycle premium.","MFE_90D_pct":6.11,"MAE_90D_pct":-17.18,"score_return_alignment_label":"late_special_steel_spread_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"global_current_proxy","profile_hypothesis":"current calibrated profile without C15 spread-duration/pass-through shadow guard","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["R4L16_C15_025820_T1","R4L16_C15_012800_T1","R4L16_C15_018470_T1","R4L16_C15_001430_T1"],"avg_MFE_90D_pct":85.86,"avg_MAE_90D_pct":-12.01,"avg_MFE_180D_pct":85.86,"avg_MAE_180D_pct":-16.25,"false_positive_rate":0.5,"missed_structural_count":1,"late_green_count":2,"avg_green_lateness_ratio":"mixed","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed; price beta overpromotes late copper/special-steel cases"}
{"profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"weaker guard overcredits commodity beta after local peaks","changed_axes":["legacy_lower_thresholds"],"changed_thresholds":{"green":"legacy"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["R4L16_C15_025820_T1","R4L16_C15_012800_T1","R4L16_C15_018470_T1","R4L16_C15_001430_T1"],"avg_MFE_90D_pct":85.86,"avg_MAE_90D_pct":-12.01,"avg_MFE_180D_pct":85.86,"avg_MAE_180D_pct":-16.25,"false_positive_rate":0.75,"missed_structural_count":0,"late_green_count":3,"avg_green_lateness_ratio":"worse","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"worse; late beta is confused with spread evidence"}
{"profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"L4 materials require product-specific spread duration and input-cost pass-through","changed_axes":["L4_product_spread_duration_bonus","L4_inventory_cycle_guard"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["R4L16_C15_025820_T1","R4L16_C15_012800_T1","R4L16_C15_018470_T1","R4L16_C15_001430_T1"],"avg_MFE_90D_pct":85.86,"avg_MAE_90D_pct":-12.01,"avg_MFE_180D_pct":85.86,"avg_MAE_180D_pct":-16.25,"false_positive_rate":0.25,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":"improved","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better; rejects late beta while keeping copper/aluminum positives"}
{"profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C15 should reward spread duration + pass-through and penalize late price-only commodity beta","changed_axes":["C15_spread_duration_pass_through_bonus","C15_late_beta_inventory_guard"],"changed_thresholds":{"Green":"unchanged; component-gated"},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["R4L16_C15_025820_T1","R4L16_C15_012800_T1","R4L16_C15_018470_T1","R4L16_C15_001430_T1"],"avg_MFE_90D_pct":85.86,"avg_MAE_90D_pct":-12.01,"avg_MFE_180D_pct":85.86,"avg_MAE_180D_pct":-16.25,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"best","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best candidate; separates durable product-spread from late-cycle beta"}
{"profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"very hard guard for late commodity beta after obvious local peak","changed_axes":["late_beta_not_stage3_green_without_pass_through"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":["R4L16_C15_025820_T1","R4L16_C15_018470_T1"],"avg_MFE_90D_pct":166.85,"avg_MAE_90D_pct":-4.94,"avg_MFE_180D_pct":166.85,"avg_MAE_180D_pct":-8.47,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"best_after_exclusion","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safest but may undercount moderate steel spread positives"}
{"row_type":"residual_contribution","round":"R4","loop":"16","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["missed_small_midcap_spread_positive","late_copper_beta_false_positive","4B_overlay_late_after_aluminum_spread_success","late_special_steel_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

```text
completed_round = R4
completed_loop = 16
next_round = R5
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest was checked for source name, price adjustment status, max date, row counts, shard roots, schema path, and universe path.
- Symbol profiles were checked for first/last dates, year files, row status counts, corporate-action candidate dates, major discontinuity flags, and raw/unadjusted caveats.
- OHLC examples were sampled from `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2021.csv` for all representative trigger rows.
- All rows remain historical calibration rows. They are not current candidates, not recommendations, and not production scoring changes.
