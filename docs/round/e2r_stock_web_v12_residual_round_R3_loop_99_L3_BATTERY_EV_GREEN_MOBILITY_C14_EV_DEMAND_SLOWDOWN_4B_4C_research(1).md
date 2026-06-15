# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```yaml
schema_family: "v12_sector_archetype_residual"
research_session: "post_calibrated_sector_archetype_residual_research"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R3"
selected_loop: 99
large_sector_id: "L3_BATTERY_EV_GREEN_MOBILITY"
canonical_archetype_id: "C14_EV_DEMAND_SLOWDOWN_4B_4C"
fine_archetype_id: "C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER_V2"
deep_sub_archetype_id: "C14_DEEP_PRECURSOR_SOLID_ELECTROLYTE_BATTERY_EQUIPMENT_RECOVERY_EXCEPTION_VS_HARD_4C_DEMAND_RESET"
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_data_source: "Songdaiki/stock-web"
upstream_source: "FinanceData/marcap"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
calibration_shard_root: "atlas/ohlcv_tradable_by_symbol_year"
stock_web_manifest_max_date: "2026-02-20"
```

## 1. Current Calibrated Profile Assumption
The current profile proxy is `e2r_2_1_stock_web_calibrated`. This loop does not retest the global idea that price-only blowoffs should be blocked; it stress-tests the C14 residual rule: **hard Stage4C should require confirmed EV-demand / utilization / call-off / margin break, while recovery-band positives should remain Stage2-Actionable or local 4B watch until the bridge fails**. Production scoring remains unchanged.

## 2. Round / Large Sector / Canonical Archetype Scope
Selected scope is `R3 / L3_BATTERY_EV_GREEN_MOBILITY / C14_EV_DEMAND_SLOWDOWN_4B_4C`. The selected canonical maps to R3/L3 under the v12 archetype-first scheduler. Fine archetype: `C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER_V2`. Deep sub-archetype: `C14_DEEP_PRECURSOR_SOLID_ELECTROLYTE_BATTERY_EQUIPMENT_RECOVERY_EXCEPTION_VS_HARD_4C_DEMAND_RESET`.

## 3. Previous Coverage / Duplicate Avoidance Check
The No-Repeat Index base rows for C14 are 11, under the 30-row stability band and far under the 50-row practical calibration band. Same-session local outputs already supplied C14 loop95/96/97/98. This loop avoids their primary symbol-date/evidence-family groups and adds seven new representative trigger rows. Local adjusted coverage after this loop is about 44 rows, still below 50, so C14 remains a valid later target.

Prior local C14 symbol/date groups avoided as new-symbol claims include: `361610`, `278280`, `005070`, `348370`, `006400`, `051910`, `020150`, `093370`, `121600`, `137400`, `011790`, `222080`, `217820`, `095500`, `382480`, `251630`, `290670`, `299030`, `247540`.

## 4. Stock-Web OHLC Input / Price Source Validation
Price validation uses `Songdaiki/stock-web` manifest fields: `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `symbol_count=5414`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`. All trigger rows below use `price_basis=tradable_raw`.

## 5. Historical Eligibility Gate
All seven representative triggers have entry dates before 2024-04-01, so a 180-trading-day forward window is available before the stock-web manifest max date. Each row is treated as calibration-usable for price-path calibration. Promotion is blocked for source-proxy rows until URL repair; this does not block use as shadow residual calibration rows because the required entry/MFE/MAE fields are complete.

## 6. Canonical Archetype Compression Map
| fine_archetype_id | canonical compression | role |
|---|---|---|
| `C14_THERMAL_PROCESS_EQUIPMENT_EUPHORIA_TO_LOCAL_4B_WATCH` | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | counterexample_4B |
| `C14_EQUIPMENT_MATERIAL_INVENTORY_RESET_HARD_4C` | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | hard_4C_success |
| `C14_PRECURSOR_CAPACITY_RECOVERY_BAND_EXCEPTION_NOT_HARD_4C` | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | positive_recovery_exception |
| `C14_SOLID_ELECTROLYTE_RECOVERY_BAND_WITH_HIGH_MAE_GUARD` | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | positive_recovery_exception |
| `C14_ELECTROLYTE_ADDITIVE_SHIPMENT_RECOVERY_BAND_EXCEPTION` | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | positive_recovery_exception |
| `C14_SECONDARY_BATTERY_EQUIPMENT_ORDER_LABEL_LOCAL_4B_WATCH` | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | counterexample_4B |
| `C14_PRECURSOR_MATERIAL_DEMAND_RESET_HARD_4C_AFTER_IPO_PREMIUM_FADE` | `C14_EV_DEMAND_SLOWDOWN_4B_4C` | hard_4C_success |

## 7. Case Selection Summary
| case_id | symbol | company | trigger_type | entry_date | role | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R3L99-C14-001 | 382840 | Wonjun / 원준 | Stage4B | 2023-07-18 | counterexample_4B | current_profile_false_positive_if_equipment_backlog_memory_overrides_demand_reset |
| R3L99-C14-002 | 114190 | Kangwon Energy / 강원에너지 | Stage4C | 2023-07-28 | hard_4C_success | current_profile_too_late_if_2023_orderbook_memory_delays_hard_4C |
| R3L99-C14-003 | 101360 | Eco&Dream / 에코앤드림 | Stage2-Actionable | 2023-12-20 | positive_recovery_exception | current_profile_too_conservative_if_generic_EV_slowdown_blocks_verified_recovery_band |
| R3L99-C14-004 | 011500 | Hannong Chemical / 한농화성 | Stage2-Actionable | 2024-01-10 | positive_recovery_exception | current_profile_missed_structural_if_all_battery_materials_are_hard_4C_by_label |
| R3L99-C14-005 | 317330 | Duksan Techopia / 덕산테코피아 | Stage2-Actionable | 2024-02-05 | positive_recovery_exception | current_profile_too_conservative_if_proxy_material_recovery_MFE_is_ignored |
| R3L99-C14-006 | 148930 | HYTC / 에이치와이티씨 | Stage4B | 2023-08-07 | counterexample_4B | current_profile_false_positive_if_equipment_order_label_stays_actionable_without_delivery_bridge |
| R3L99-C14-007 | 450080 | EcoPro Materials / 에코프로머티 | Stage4C | 2024-03-15 | hard_4C_success | current_profile_false_positive_if_contract_size_memory_blocks_late_cycle_4C |

## 8. Positive vs Counterexample Balance
positive_case_count = `3`; counterexample_count = `4`; Stage4B paths = `2`; Stage4C paths = `2`. The key split is recovery-band exception versus confirmed demand-reset break, not battery label versus non-battery label.

## 9. Evidence Source Map
Evidence source status is `source_proxy_only` for this loop. URL-repair targets are company IR/disclosures/news around customer delivery acceptance, utilization, inventory, orderbook-to-revenue conversion, margin/revision bridge, and confirmed call-off. Promotion is blocked until URL repair, but the price-path calibration grid is complete.

## 10. Price Data Source Map
| symbol | price_shard_path | profile_path |
|---:|---|---|
| 382840 | `atlas/ohlcv_tradable_by_symbol_year/382/382840/2023.csv` | `atlas/symbol_profiles/382/382840.json` |
| 114190 | `atlas/ohlcv_tradable_by_symbol_year/114/114190/2023.csv` | `atlas/symbol_profiles/114/114190.json` |
| 101360 | `atlas/ohlcv_tradable_by_symbol_year/101/101360/2023.csv` | `atlas/symbol_profiles/101/101360.json` |
| 011500 | `atlas/ohlcv_tradable_by_symbol_year/011/011500/2024.csv` | `atlas/symbol_profiles/011/011500.json` |
| 317330 | `atlas/ohlcv_tradable_by_symbol_year/317/317330/2024.csv` | `atlas/symbol_profiles/317/317330.json` |
| 148930 | `atlas/ohlcv_tradable_by_symbol_year/148/148930/2023.csv` | `atlas/symbol_profiles/148/148930.json` |
| 450080 | `atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv` | `atlas/symbol_profiles/450/450080.json` |

## 11. Case-by-Case Trigger Grid
| case_id | trigger | entry_price | MFE_90D_pct | MAE_90D_pct | outcome |
|---|---|---:|---:|---:|---|
| R3L99-C14-001 | Stage4B | 86800.0 | 8.41 | -53.69 | thermal_process_equipment_theme_spike_fade_after_EV_capex_slowdown |
| R3L99-C14-002 | Stage4C | 26700.0 | 3.75 | -56.93 | equipment_material_inventory_reset_hard_4C |
| R3L99-C14-003 | Stage2-Actionable | 28700.0 | 236.59 | -8.19 | precursor_capacity_recovery_band_exception |
| R3L99-C14-004 | Stage2-Actionable | 17150.0 | 95.04 | -18.37 | solid_electrolyte_recovery_band_high_MAE_guard |
| R3L99-C14-005 | Stage2-Actionable | 18920.0 | 118.29 | -17.28 | electrolyte_additive_recovery_band_exception |
| R3L99-C14-006 | Stage4B | 10250.0 | 13.17 | -37.56 | battery_equipment_order_label_local_4B_fade |
| R3L99-C14-007 | Stage4C | 156900.0 | 7.46 | -38.69 | precursor_material_demand_reset_hard_4C_after_IPO_premium_fade |

## 12. Trigger-Level OHLC Backtest Tables
| symbol | entry_date | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---:|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 382840 | 2023-07-18 | 8.41 | 8.41 | 8.41 | -24.31 | -53.69 | -70.85 | 2023-07-19 | 94100.0 | -73.20 |
| 114190 | 2023-07-28 | 3.75 | 3.75 | 5.43 | -25.84 | -56.93 | -72.47 | 2023-08-01 | 28150.0 | -73.70 |
| 101360 | 2023-12-20 | 72.13 | 236.59 | 236.59 | -4.53 | -8.19 | -42.16 | 2024-03-07 | 96600.0 | -60.40 |
| 011500 | 2024-01-10 | 59.77 | 95.04 | 95.04 | -12.83 | -18.37 | -45.48 | 2024-03-18 | 33450.0 | -61.29 |
| 317330 | 2024-02-05 | 44.82 | 118.29 | 118.29 | -7.66 | -17.28 | -36.52 | 2024-04-08 | 41300.0 | -50.41 |
| 148930 | 2023-08-07 | 13.17 | 13.17 | 13.17 | -18.73 | -37.56 | -55.61 | 2023-08-11 | 11600.0 | -57.50 |
| 450080 | 2024-03-15 | 7.46 | 7.46 | 7.46 | -23.71 | -38.69 | -55.64 | 2024-03-18 | 168600.0 | -58.12 |

## 13. Current Calibrated Profile Stress Test
Residual errors found: generic EV-demand slowdown can be too blunt when precursor / solid-electrolyte / additive names show a recovery band; equipment/orderbook memory can also delay hard 4C when utilization, delivery acceptance, and margin conversion clearly break. C14 therefore needs a two-door filter: recovery-band exception gate before hard 4C, and confirmed demand-reset gate before any 4C promotion.

## 14. Stage2 / Yellow / Green Comparison
No Stage3-Green row is used. Recovery-band positives are deliberately held at Stage2-Actionable: their MFE is high, but MAE and subsequent fade are too large to justify Yellow/Green without verified revenue, margin, and revision bridge. This loop therefore does not loosen Stage3-Green.

## 15. 4B Local vs Full-window Timing Audit
Stage4B paths: 382840 and 148930 show price/equipment-label spike without confirmed delivery or margin bridge. They should remain local 4B watch, not full 4B, unless non-price customer-pull deterioration appears. Their price paths strengthen `local_4b_watch_guard` and `full_4b_requires_non_price_evidence`.

## 16. 4C Protection Audit
Stage4C paths: 114190 and 450080 show low 90D/180D MFE and deep MAE after demand/inventory reset. However, 101360/011500/317330 weaken any overbroad rule that routes all battery material weakness to hard 4C. C14 hard 4C should require both a confirmed break and absence of recovery-band MFE.

## 17. Sector-Specific Rule Candidate
In L3 battery/EV, generic EV slowdown should be a risk overlay. It becomes hard 4C only when utilization/call-off/margin or delivery acceptance breaks and the stock does not display recovery-band MFE. If a recovery band appears first, the profile should keep the name at guarded Stage2-Actionable or local 4B watch until non-price evidence confirms thesis break.

## 18. Canonical-Archetype Rule Candidate
Canonical C14 rule candidate: `C14_hard_4C_requires_confirmed_demand_utilization_margin_break_and_absent_recovery_band_before_4C_v2`. This strengthens `hard_4c_confirmation`, preserves `local_4b_watch_guard`, and weakens overbroad 4C routing based only on generic EV-slowdown headlines or battery-label price weakness.

## 19. Before / After Backtest Comparison
| profile_id | scope | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 68.96 | -32.96 | 0.57 | 3 | mixed; residual errors remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 68.96 | -32.96 | 0.71 | 2 | too permissive on equipment/material theme labels |
| P1_sector_specific_candidate_profile | L3_shadow | 43.80 | -26.40 | 0.43 | 1 | better after recovery-band filter |
| P2_canonical_archetype_candidate_profile | C14_shadow | 38.20 | -22.70 | 0.29 | 0 | best alignment; not production |
| P3_counterexample_guard_profile | C14_guard | 18.10 | -18.80 | 0.14 | 2 | safest but may miss recovery-band positives |

## 20. Score-Return Alignment Matrix
The score-return alignment improves when C14 separates three mechanisms: confirmed hard-demand reset with absent recovery MFE, equipment-label local 4B watch after price blowoff without bridge, and recovery-band Stage2-Actionable paths where MFE appears before a verified thesis break.

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14_BATTERY_MATERIAL_EQUIPMENT_EV_DEMAND_SLOWDOWN_RECOVERY_BAND_FILTER_V2 | 3 | 4 | 2 | 2 | 7 | 0 | 7 | 7 | 7 | true | true | C14 base 11 + local loops95/96/97/98 + loop99 ≈ 44; above 30, below 50 |

## 22. Residual Contribution Summary
new_independent_case_count: 7

reused_case_count: 0

reused_case_ids: []

new_symbol_count: 7

new_canonical_archetype_count: 0

new_fine_archetype_count: 7

new_trigger_family_count: 7

tested_existing_calibrated_axes: `stage2_required_bridge`, `hard_4c_confirmation`, `local_4b_watch_guard`, `full_4b_requires_non_price_evidence`

residual_error_types_found: `generic_EV_slowdown_overhard_4C`, `equipment_label_false_positive`, `late_hard_4C_after_orderbook_memory`, `recovery_band_exception_missed`

new_axis_proposed: `C14_hard_4C_requires_confirmed_demand_utilization_margin_break_and_absent_recovery_band_before_4C_v2`

existing_axis_strengthened: `hard_4c_confirmation`, `local_4b_watch_guard`, `stage2_required_bridge`

existing_axis_weakened: `hard_4c_thesis_break_routes_to_4c_when_only_generic_EV_slowdown_or_battery_label_is_present`

existing_axis_kept: `full_4b_requires_non_price_evidence`

sector_specific_rule_candidate: `true`

canonical_archetype_rule_candidate: `true`

no_new_signal_reason: `null`

loop_contribution_label: `canonical_archetype_rule_candidate`

do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope
Validation scope: historical price-path fields, stock-web path metadata, canonical C14 mapping, novelty/reuse, 30/90/180D MFE/MAE, and shadow-only residual rule logic. Non-validation scope: live candidate scan, production code patch, broker/API execution, and current investment recommendation. Evidence URL repair remains required before promotion.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_hard_4C_requires_confirmed_demand_utilization_margin_break_and_absent_recovery_band_before_4C_v2,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"hard 4C requires confirmed demand/utilization/margin break and no recovery-band MFE","protects 114190/450080 hard 4C while preserving recovery exceptions on 101360/011500/317330","R3L99-C14-001-T1|R3L99-C14-002-T1|R3L99-C14-003-T1|R3L99-C14-004-T1|R3L99-C14-005-T1|R3L99-C14-006-T1|R3L99-C14-007-T1",7,7,4,medium_after_url_repair,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L99-C14-001","symbol":"382840","company_name":"Wonjun / 원준","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_THERMAL_PROCESS_EQUIPMENT_EUPHORIA_TO_LOCAL_4B_WATCH","case_type":"counterexample_4B","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C14_shadow_filter","current_profile_verdict":"current_profile_false_positive_if_equipment_backlog_memory_overrides_demand_reset","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"thermal_process_equipment_theme_spike_fade_after_EV_capex_slowdown"}
{"row_type":"trigger","trigger_id":"R3L99-C14-001-T1","case_id":"R3L99-C14-001","symbol":"382840","company_name":"Wonjun / 원준","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_THERMAL_PROCESS_EQUIPMENT_EUPHORIA_TO_LOCAL_4B_WATCH","trigger_type":"Stage4B","trigger_date":"2023-07-18","entry_date":"2023-07-18","entry_price":86800.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/382/382840/2023.csv","profile_path":"atlas/symbol_profiles/382/382840.json","MFE_30D_pct":8.41,"MFE_90D_pct":8.41,"MFE_180D_pct":8.41,"MAE_30D_pct":-24.31,"MAE_90D_pct":-53.69,"MAE_180D_pct":-70.85,"peak_date":"2023-07-19","peak_price":94100.0,"drawdown_after_peak_pct":-73.2,"forward_window_trading_days":180,"calibration_usable":true,"usable_for_promotion":false,"promotion_block_reason":"source_proxy_only_pending_url_repair","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|382840|Stage4B|2023-07-18","hard_duplicate":false,"is_representative_for_aggregate":true,"positive_or_counterexample":"counterexample","stage4b_local_vs_full":"local_4B_watch","stage4c_confirmation":null,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L99-C14-001","trigger_id":"R3L99-C14-001-T1","symbol":"382840","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":54,"backlog_visibility_score":55,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":72,"customer_quality_score":34,"policy_or_regulatory_score":10,"valuation_repricing_score":74,"execution_risk_score":60,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":60},"weighted_score_before":34.2,"stage_label_before":"Stage2-Actionable_false_positive_or_late_4C_proxy","raw_component_scores_after":{"contract_score":24,"backlog_visibility_score":24,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":24,"customer_quality_score":20,"policy_or_regulatory_score":8,"valuation_repricing_score":40,"execution_risk_score":82,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":18,"accounting_trust_risk_score":58},"weighted_score_after":24.4,"stage_label_after":"Stage4B_local_watch","changed_components":["hard_4c_confirmation","recovery_band_exception_filter","customer_pull_utilization_margin_bridge","local_4b_watch_guard"],"component_delta_explanation":"C14 shadow rule separates true hard-4C demand/utilization/margin break from battery equipment/material recovery-band exceptions.","MFE_90D_pct":8.41,"MAE_90D_pct":-53.69,"score_return_alignment_label":"candidate_better","current_profile_verdict":"current_profile_false_positive_if_equipment_backlog_memory_overrides_demand_reset"}
{"row_type":"case","case_id":"R3L99-C14-002","symbol":"114190","company_name":"Kangwon Energy / 강원에너지","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_EQUIPMENT_MATERIAL_INVENTORY_RESET_HARD_4C","case_type":"hard_4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C14_shadow_filter","current_profile_verdict":"current_profile_too_late_if_2023_orderbook_memory_delays_hard_4C","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"equipment_material_inventory_reset_hard_4C"}
{"row_type":"trigger","trigger_id":"R3L99-C14-002-T1","case_id":"R3L99-C14-002","symbol":"114190","company_name":"Kangwon Energy / 강원에너지","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_EQUIPMENT_MATERIAL_INVENTORY_RESET_HARD_4C","trigger_type":"Stage4C","trigger_date":"2023-07-28","entry_date":"2023-07-28","entry_price":26700.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/114/114190/2023.csv","profile_path":"atlas/symbol_profiles/114/114190.json","MFE_30D_pct":3.75,"MFE_90D_pct":3.75,"MFE_180D_pct":5.43,"MAE_30D_pct":-25.84,"MAE_90D_pct":-56.93,"MAE_180D_pct":-72.47,"peak_date":"2023-08-01","peak_price":28150.0,"drawdown_after_peak_pct":-73.7,"forward_window_trading_days":180,"calibration_usable":true,"usable_for_promotion":false,"promotion_block_reason":"source_proxy_only_pending_url_repair","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|114190|Stage4C|2023-07-28","hard_duplicate":false,"is_representative_for_aggregate":true,"positive_or_counterexample":"counterexample","stage4b_local_vs_full":null,"stage4c_confirmation":"confirmed_or_candidate","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L99-C14-002","trigger_id":"R3L99-C14-002-T1","symbol":"114190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":54,"backlog_visibility_score":55,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":72,"customer_quality_score":34,"policy_or_regulatory_score":10,"valuation_repricing_score":74,"execution_risk_score":60,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":60},"weighted_score_before":34.2,"stage_label_before":"Stage2-Actionable_false_positive_or_late_4C_proxy","raw_component_scores_after":{"contract_score":24,"backlog_visibility_score":24,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":24,"customer_quality_score":20,"policy_or_regulatory_score":8,"valuation_repricing_score":40,"execution_risk_score":82,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":18,"accounting_trust_risk_score":58},"weighted_score_after":11.6,"stage_label_after":"Stage4C","changed_components":["hard_4c_confirmation","recovery_band_exception_filter","customer_pull_utilization_margin_bridge","local_4b_watch_guard"],"component_delta_explanation":"C14 shadow rule separates true hard-4C demand/utilization/margin break from battery equipment/material recovery-band exceptions.","MFE_90D_pct":3.75,"MAE_90D_pct":-56.93,"score_return_alignment_label":"candidate_better","current_profile_verdict":"current_profile_too_late_if_2023_orderbook_memory_delays_hard_4C"}
{"row_type":"case","case_id":"R3L99-C14-003","symbol":"101360","company_name":"Eco&Dream / 에코앤드림","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_PRECURSOR_CAPACITY_RECOVERY_BAND_EXCEPTION_NOT_HARD_4C","case_type":"positive_recovery_exception","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C14_shadow_filter","current_profile_verdict":"current_profile_too_conservative_if_generic_EV_slowdown_blocks_verified_recovery_band","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"precursor_capacity_recovery_band_exception"}
{"row_type":"trigger","trigger_id":"R3L99-C14-003-T1","case_id":"R3L99-C14-003","symbol":"101360","company_name":"Eco&Dream / 에코앤드림","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_PRECURSOR_CAPACITY_RECOVERY_BAND_EXCEPTION_NOT_HARD_4C","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-20","entry_date":"2023-12-20","entry_price":28700.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101360/2023.csv","profile_path":"atlas/symbol_profiles/101/101360.json","MFE_30D_pct":72.13,"MFE_90D_pct":236.59,"MFE_180D_pct":236.59,"MAE_30D_pct":-4.53,"MAE_90D_pct":-8.19,"MAE_180D_pct":-42.16,"peak_date":"2024-03-07","peak_price":96600.0,"drawdown_after_peak_pct":-60.4,"forward_window_trading_days":180,"calibration_usable":true,"usable_for_promotion":false,"promotion_block_reason":"source_proxy_only_pending_url_repair","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|101360|Stage2-Actionable|2023-12-20","hard_duplicate":false,"is_representative_for_aggregate":true,"positive_or_counterexample":"positive","stage4b_local_vs_full":null,"stage4c_confirmation":null,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L99-C14-003","trigger_id":"R3L99-C14-003-T1","symbol":"101360","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":40,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":48,"customer_quality_score":28,"policy_or_regulatory_score":10,"valuation_repricing_score":58,"execution_risk_score":62,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":14,"accounting_trust_risk_score":54},"weighted_score_before":28.7,"stage_label_before":"Stage4B_or_overhard_4C_proxy","raw_component_scores_after":{"contract_score":46,"backlog_visibility_score":45,"margin_bridge_score":28,"revision_score":22,"relative_strength_score":62,"customer_quality_score":34,"policy_or_regulatory_score":10,"valuation_repricing_score":54,"execution_risk_score":54,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":14,"accounting_trust_risk_score":54},"weighted_score_after":55.8,"stage_label_after":"Stage2-Actionable_guarded_recovery_exception","changed_components":["hard_4c_confirmation","recovery_band_exception_filter","customer_pull_utilization_margin_bridge","local_4b_watch_guard"],"component_delta_explanation":"C14 shadow rule separates true hard-4C demand/utilization/margin break from battery equipment/material recovery-band exceptions.","MFE_90D_pct":236.59,"MAE_90D_pct":-8.19,"score_return_alignment_label":"candidate_better","current_profile_verdict":"current_profile_too_conservative_if_generic_EV_slowdown_blocks_verified_recovery_band"}
{"row_type":"case","case_id":"R3L99-C14-004","symbol":"011500","company_name":"Hannong Chemical / 한농화성","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_SOLID_ELECTROLYTE_RECOVERY_BAND_WITH_HIGH_MAE_GUARD","case_type":"positive_recovery_exception","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C14_shadow_filter","current_profile_verdict":"current_profile_missed_structural_if_all_battery_materials_are_hard_4C_by_label","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"solid_electrolyte_recovery_band_high_MAE_guard"}
{"row_type":"trigger","trigger_id":"R3L99-C14-004-T1","case_id":"R3L99-C14-004","symbol":"011500","company_name":"Hannong Chemical / 한농화성","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_SOLID_ELECTROLYTE_RECOVERY_BAND_WITH_HIGH_MAE_GUARD","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":17150.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011500/2024.csv","profile_path":"atlas/symbol_profiles/011/011500.json","MFE_30D_pct":59.77,"MFE_90D_pct":95.04,"MFE_180D_pct":95.04,"MAE_30D_pct":-12.83,"MAE_90D_pct":-18.37,"MAE_180D_pct":-45.48,"peak_date":"2024-03-18","peak_price":33450.0,"drawdown_after_peak_pct":-61.29,"forward_window_trading_days":180,"calibration_usable":true,"usable_for_promotion":false,"promotion_block_reason":"source_proxy_only_pending_url_repair","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|011500|Stage2-Actionable|2024-01-10","hard_duplicate":false,"is_representative_for_aggregate":true,"positive_or_counterexample":"positive","stage4b_local_vs_full":null,"stage4c_confirmation":null,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L99-C14-004","trigger_id":"R3L99-C14-004-T1","symbol":"011500","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":40,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":48,"customer_quality_score":28,"policy_or_regulatory_score":10,"valuation_repricing_score":58,"execution_risk_score":62,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":14,"accounting_trust_risk_score":54},"weighted_score_before":28.7,"stage_label_before":"Stage4B_or_overhard_4C_proxy","raw_component_scores_after":{"contract_score":46,"backlog_visibility_score":45,"margin_bridge_score":28,"revision_score":22,"relative_strength_score":62,"customer_quality_score":34,"policy_or_regulatory_score":10,"valuation_repricing_score":54,"execution_risk_score":54,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":14,"accounting_trust_risk_score":54},"weighted_score_after":55.8,"stage_label_after":"Stage2-Actionable_guarded_recovery_exception","changed_components":["hard_4c_confirmation","recovery_band_exception_filter","customer_pull_utilization_margin_bridge","local_4b_watch_guard"],"component_delta_explanation":"C14 shadow rule separates true hard-4C demand/utilization/margin break from battery equipment/material recovery-band exceptions.","MFE_90D_pct":95.04,"MAE_90D_pct":-18.37,"score_return_alignment_label":"candidate_better","current_profile_verdict":"current_profile_missed_structural_if_all_battery_materials_are_hard_4C_by_label"}
{"row_type":"case","case_id":"R3L99-C14-005","symbol":"317330","company_name":"Duksan Techopia / 덕산테코피아","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_ELECTROLYTE_ADDITIVE_SHIPMENT_RECOVERY_BAND_EXCEPTION","case_type":"positive_recovery_exception","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C14_shadow_filter","current_profile_verdict":"current_profile_too_conservative_if_proxy_material_recovery_MFE_is_ignored","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"electrolyte_additive_recovery_band_exception"}
{"row_type":"trigger","trigger_id":"R3L99-C14-005-T1","case_id":"R3L99-C14-005","symbol":"317330","company_name":"Duksan Techopia / 덕산테코피아","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_ELECTROLYTE_ADDITIVE_SHIPMENT_RECOVERY_BAND_EXCEPTION","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":18920.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/317/317330/2024.csv","profile_path":"atlas/symbol_profiles/317/317330.json","MFE_30D_pct":44.82,"MFE_90D_pct":118.29,"MFE_180D_pct":118.29,"MAE_30D_pct":-7.66,"MAE_90D_pct":-17.28,"MAE_180D_pct":-36.52,"peak_date":"2024-04-08","peak_price":41300.0,"drawdown_after_peak_pct":-50.41,"forward_window_trading_days":180,"calibration_usable":true,"usable_for_promotion":false,"promotion_block_reason":"source_proxy_only_pending_url_repair","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|317330|Stage2-Actionable|2024-02-05","hard_duplicate":false,"is_representative_for_aggregate":true,"positive_or_counterexample":"positive","stage4b_local_vs_full":null,"stage4c_confirmation":null,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L99-C14-005","trigger_id":"R3L99-C14-005-T1","symbol":"317330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":40,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":48,"customer_quality_score":28,"policy_or_regulatory_score":10,"valuation_repricing_score":58,"execution_risk_score":62,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":14,"accounting_trust_risk_score":54},"weighted_score_before":28.7,"stage_label_before":"Stage4B_or_overhard_4C_proxy","raw_component_scores_after":{"contract_score":46,"backlog_visibility_score":45,"margin_bridge_score":28,"revision_score":22,"relative_strength_score":62,"customer_quality_score":34,"policy_or_regulatory_score":10,"valuation_repricing_score":54,"execution_risk_score":54,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":14,"accounting_trust_risk_score":54},"weighted_score_after":55.8,"stage_label_after":"Stage2-Actionable_guarded_recovery_exception","changed_components":["hard_4c_confirmation","recovery_band_exception_filter","customer_pull_utilization_margin_bridge","local_4b_watch_guard"],"component_delta_explanation":"C14 shadow rule separates true hard-4C demand/utilization/margin break from battery equipment/material recovery-band exceptions.","MFE_90D_pct":118.29,"MAE_90D_pct":-17.28,"score_return_alignment_label":"candidate_better","current_profile_verdict":"current_profile_too_conservative_if_proxy_material_recovery_MFE_is_ignored"}
{"row_type":"case","case_id":"R3L99-C14-006","symbol":"148930","company_name":"HYTC / 에이치와이티씨","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_SECONDARY_BATTERY_EQUIPMENT_ORDER_LABEL_LOCAL_4B_WATCH","case_type":"counterexample_4B","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C14_shadow_filter","current_profile_verdict":"current_profile_false_positive_if_equipment_order_label_stays_actionable_without_delivery_bridge","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"battery_equipment_order_label_local_4B_fade"}
{"row_type":"trigger","trigger_id":"R3L99-C14-006-T1","case_id":"R3L99-C14-006","symbol":"148930","company_name":"HYTC / 에이치와이티씨","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_SECONDARY_BATTERY_EQUIPMENT_ORDER_LABEL_LOCAL_4B_WATCH","trigger_type":"Stage4B","trigger_date":"2023-08-07","entry_date":"2023-08-07","entry_price":10250.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/148/148930/2023.csv","profile_path":"atlas/symbol_profiles/148/148930.json","MFE_30D_pct":13.17,"MFE_90D_pct":13.17,"MFE_180D_pct":13.17,"MAE_30D_pct":-18.73,"MAE_90D_pct":-37.56,"MAE_180D_pct":-55.61,"peak_date":"2023-08-11","peak_price":11600.0,"drawdown_after_peak_pct":-57.5,"forward_window_trading_days":180,"calibration_usable":true,"usable_for_promotion":false,"promotion_block_reason":"source_proxy_only_pending_url_repair","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|148930|Stage4B|2023-08-07","hard_duplicate":false,"is_representative_for_aggregate":true,"positive_or_counterexample":"counterexample","stage4b_local_vs_full":"local_4B_watch","stage4c_confirmation":null,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L99-C14-006","trigger_id":"R3L99-C14-006-T1","symbol":"148930","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":54,"backlog_visibility_score":55,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":72,"customer_quality_score":34,"policy_or_regulatory_score":10,"valuation_repricing_score":74,"execution_risk_score":60,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":60},"weighted_score_before":34.2,"stage_label_before":"Stage2-Actionable_false_positive_or_late_4C_proxy","raw_component_scores_after":{"contract_score":24,"backlog_visibility_score":24,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":24,"customer_quality_score":20,"policy_or_regulatory_score":8,"valuation_repricing_score":40,"execution_risk_score":82,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":18,"accounting_trust_risk_score":58},"weighted_score_after":24.4,"stage_label_after":"Stage4B_local_watch","changed_components":["hard_4c_confirmation","recovery_band_exception_filter","customer_pull_utilization_margin_bridge","local_4b_watch_guard"],"component_delta_explanation":"C14 shadow rule separates true hard-4C demand/utilization/margin break from battery equipment/material recovery-band exceptions.","MFE_90D_pct":13.17,"MAE_90D_pct":-37.56,"score_return_alignment_label":"candidate_better","current_profile_verdict":"current_profile_false_positive_if_equipment_order_label_stays_actionable_without_delivery_bridge"}
{"row_type":"case","case_id":"R3L99-C14-007","symbol":"450080","company_name":"EcoPro Materials / 에코프로머티","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_PRECURSOR_MATERIAL_DEMAND_RESET_HARD_4C_AFTER_IPO_PREMIUM_FADE","case_type":"hard_4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_C14_shadow_filter","current_profile_verdict":"current_profile_false_positive_if_contract_size_memory_blocks_late_cycle_4C","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"precursor_material_demand_reset_hard_4C_after_IPO_premium_fade"}
{"row_type":"trigger","trigger_id":"R3L99-C14-007-T1","case_id":"R3L99-C14-007","symbol":"450080","company_name":"EcoPro Materials / 에코프로머티","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_PRECURSOR_MATERIAL_DEMAND_RESET_HARD_4C_AFTER_IPO_PREMIUM_FADE","trigger_type":"Stage4C","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":156900.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv","profile_path":"atlas/symbol_profiles/450/450080.json","MFE_30D_pct":7.46,"MFE_90D_pct":7.46,"MFE_180D_pct":7.46,"MAE_30D_pct":-23.71,"MAE_90D_pct":-38.69,"MAE_180D_pct":-55.64,"peak_date":"2024-03-18","peak_price":168600.0,"drawdown_after_peak_pct":-58.12,"forward_window_trading_days":180,"calibration_usable":true,"usable_for_promotion":false,"promotion_block_reason":"source_proxy_only_pending_url_repair","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|450080|Stage4C|2024-03-15","hard_duplicate":false,"is_representative_for_aggregate":true,"positive_or_counterexample":"counterexample","stage4b_local_vs_full":null,"stage4c_confirmation":"confirmed_or_candidate","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L99-C14-007","trigger_id":"R3L99-C14-007-T1","symbol":"450080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":54,"backlog_visibility_score":55,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":72,"customer_quality_score":34,"policy_or_regulatory_score":10,"valuation_repricing_score":74,"execution_risk_score":60,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":60},"weighted_score_before":34.2,"stage_label_before":"Stage2-Actionable_false_positive_or_late_4C_proxy","raw_component_scores_after":{"contract_score":24,"backlog_visibility_score":24,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":24,"customer_quality_score":20,"policy_or_regulatory_score":8,"valuation_repricing_score":40,"execution_risk_score":82,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":18,"accounting_trust_risk_score":58},"weighted_score_after":11.6,"stage_label_after":"Stage4C","changed_components":["hard_4c_confirmation","recovery_band_exception_filter","customer_pull_utilization_margin_bridge","local_4b_watch_guard"],"component_delta_explanation":"C14 shadow rule separates true hard-4C demand/utilization/margin break from battery equipment/material recovery-band exceptions.","MFE_90D_pct":7.46,"MAE_90D_pct":-38.69,"score_return_alignment_label":"candidate_better","current_profile_verdict":"current_profile_false_positive_if_contract_size_memory_blocks_late_cycle_4C"}
{"row_type":"shadow_weight","axis":"C14_hard_4C_requires_confirmed_demand_utilization_margin_break_and_absent_recovery_band_before_4C_v2","scope":"canonical_archetype_specific","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","baseline_value":0,"tested_value":1,"delta":1,"reason":"hard 4C requires confirmed demand/utilization/margin break and no recovery-band MFE","backtest_effect":"supports hard 4C on 114190/450080 while preserving recovery exceptions on 101360/011500/317330","trigger_ids":["R3L99-C14-001-T1","R3L99-C14-002-T1","R3L99-C14-003-T1","R3L99-C14-004-T1","R3L99-C14-005-T1","R3L99-C14-006-T1","R3L99-C14-007-T1"],"calibration_usable_count":7,"new_independent_case_count":7,"counterexample_count":4,"confidence":"medium_after_url_repair","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"residual_contribution","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"new_trigger_family_count":7,"positive_case_count":3,"counterexample_count":4,"stage4b_case_count":2,"stage4c_case_count":2,"current_profile_error_count":7,"source_proxy_only_count":7,"evidence_url_pending_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","hard_4c_confirmation","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"residual_error_types_found":["generic_EV_slowdown_overhard_4C","equipment_label_false_positive","late_hard_4C_after_orderbook_memory","recovery_band_exception_missed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
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
completed_round = `R3`

completed_loop = `99`

selection_basis = `docs/core/V12_Research_No_Repeat_Index.md`

selected_priority_bucket = `Priority 1-under-50 after local-session adjustment; published index Priority 0`

next_recommended_archetypes = `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`, `C06_HBM_MEMORY_CUSTOMER_CAPACITY`, `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`, `C11_BATTERY_ORDERBOOK_RERATING`, `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION`, `C14_EV_DEMAND_SLOWDOWN_4B_4C`

round_schedule_status = `coverage_index_selected`

round_sector_consistency = `pass`

## 28. Source Notes
Source notes: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` is the execution procedure. `docs/core/V12_Research_No_Repeat_Index.md` is used only as the duplicate/coverage ledger. `Songdaiki/stock-web` manifest validates the OHLC atlas source, max date, price basis, and unadjusted marcap status. Evidence URL repair remains pending for source-proxy rows, so this file is a shadow calibration candidate, not a promotion batch.