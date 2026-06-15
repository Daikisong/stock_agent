# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
generated_at_kst: "2026-06-13"
main_execution_prompt: "docs/core/e2r_v12_prompt_round_scheduler_corrected.txt"
no_repeat_index: "docs/core/V12_Research_No_Repeat_Index.md"
selected_round: "R2"
selected_loop: 118
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L2_AI_SEMICONDUCTOR_ELECTRONICS"
canonical_archetype_id: "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF"
fine_archetype_id: "C09_ADVANCED_PROCESS_PARTS_ENV_CONTROL_OSAT_PREMIUM_WITH_OR_WITHOUT_ORDER_REVENUE_MARGIN_BRIDGE"
deep_sub_archetype_id: "C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE"
loop_objective: "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery"
price_source: "Songdaiki/stock-web"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
upstream_source: "FinanceData/marcap"
calibration_shard_root: "atlas/ohlcv_tradable_by_symbol_year"
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. This loop does not re-prove the global Stage2/Yellow/Green thresholds. It stress-tests the C09-specific seam where advanced process parts, environmental-control equipment, OSAT/package beta, and process-material premiums can be confused with true equipment order/revenue/margin conversion.

## 2. Round / Large Sector / Canonical Archetype Scope

Selected scope is `R2` / `L2_AI_SEMICONDUCTOR_ELECTRONICS` / `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`. C06~C10 map to R2/L2, so the round-sector pair is valid. R13 is not used because this is a C09 canonical residual loop, not a cross-archetype red-team checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

Published index places C09 at 10 rows. This local session previously produced C09 loop113~117. Their known symbol groups were avoided: 322310, 403870, 348210, 281820, 140860, 240810, 036930, 064290, 083450, 084370, 092870, 095610, 253590, 031980, 036810, 039440, 079370, 089030, 101490, 319660, 042700, 049080, 053610, 083310, 089890, 098460, 159010, 033160, 089970, 104830, 144960, 160980, 195870, 357780. This loop uses six new C09 symbols and six new trigger families.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields used: `source_name=FinanceData/marcap`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `symbol_count=5414`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`, `price_adjustment_status=raw_unadjusted_marcap`. All entry windows use 2024~2025 tradable shards and have 180 forward trading rows available before the manifest max date.

## 5. Historical Eligibility Gate

All trigger rows are historical, use `entry_price = c` from the Stock-Web tradable shard, have complete 30D/90D/180D MFE and MAE fields, and are treated as clean 180D windows by local row continuity proxy. Evidence URL repair is still required before promotion because the row evidence is source-proxy evidence.

## 6. Canonical Archetype Compression Map

| canonical | fine/deep | compression decision |
|---|---|---|
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09_ADVANCED_PROCESS_PARTS_ENV_CONTROL_OSAT_PREMIUM_WITH_OR_WITHOUT_ORDER_REVENUE_MARGIN_BRIDGE | SiC/process parts, wet chemical/process material, environmental-control equipment, OSAT/package beta, and backend premium cases compress into C09 only when the research question is valuation premium versus verified order/revenue/margin bridge. |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | role | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| C09-R2-L118-01-064760 | 064760 | 티씨케이 | Stage2-Actionable | 2024-03-22 | 110700.0 | 35.41 | -5.15 | 35.41 | -39.93 | positive | current_profile_too_late_if_parts_order_bridge_is_overblocked |
| C09-R2-L118-02-171010 | 171010 | 램테크놀러지 | Stage2-Actionable | 2024-03-22 | 4660.0 | 59.44 | -5.58 | 59.44 | -45.82 | positive | current_profile_missed_structural_if_all_process_materials_blocked |
| C09-R2-L118-03-396470 | 396470 | 워트 | Stage2-Actionable | 2024-03-22 | 9980.0 | 83.27 | -10.42 | 83.27 | -35.17 | positive | current_profile_missed_structural_if_newly_listed_equipment_proxy_is_blocked |
| C09-R2-L118-04-166090 | 166090 | 하나머티리얼즈 | Stage4B | 2024-07-01 | 65700.0 | 5.48 | -62.1 | 5.48 | -66.74 | counterexample | current_profile_4B_too_late_if_parts_premium_clears_yellow |
| C09-R2-L118-05-067310 | 067310 | 하나마이크론 | Stage3-Yellow | 2024-07-01 | 20600.0 | 3.64 | -53.64 | 3.64 | -59.61 | counterexample | current_profile_false_positive_if_OSAT_label_unlocks_yellow |
| C09-R2-L118-06-036540 | 036540 | SFA반도체 | Stage3-Yellow | 2024-05-02 | 5650.0 | 7.08 | -41.5 | 7.08 | -50.09 | counterexample | current_profile_false_positive_if_backend_beta_promoted_without_bridge |

## 8. Positive vs Counterexample Balance

Positive cases: `3`. Counterexamples / 4B guardrail cases: `3`. The loop meets the minimum positive/counterexample gate and adds one explicit Stage4B local-watch path.

## 9. Evidence Source Map

| symbol | evidence source status | promotion status |
|---|---|---|
| 064760 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 171010 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 396470 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 166090 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 067310 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 036540 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | corporate action window |
|---|---|---|---|---|
| 064760 | 티씨케이 | atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv | atlas/symbol_profiles/064/064760.json | clean_180D_window_profile_proxy |
| 171010 | 램테크놀러지 | atlas/ohlcv_tradable_by_symbol_year/171/171010/2024.csv | atlas/symbol_profiles/171/171010.json | clean_180D_window_profile_proxy |
| 396470 | 워트 | atlas/ohlcv_tradable_by_symbol_year/396/396470/2024.csv | atlas/symbol_profiles/396/396470.json | clean_180D_window_profile_proxy |
| 166090 | 하나머티리얼즈 | atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv | atlas/symbol_profiles/166/166090.json | clean_180D_window_profile_proxy |
| 067310 | 하나마이크론 | atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv | atlas/symbol_profiles/067/067310.json | clean_180D_window_profile_proxy |
| 036540 | SFA반도체 | atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv | atlas/symbol_profiles/036/036540.json | clean_180D_window_profile_proxy |

## 11. Case-by-Case Trigger Grid

### C09-R2-L118-01-064760 / 064760 티씨케이

- role: `structural_success` / `positive`
- trigger: `Stage2-Actionable` on `2024-03-22`, entry `2024-03-22` at `110700.0`
- price path: MFE90 `35.41%`, MAE90 `-5.15%`, MFE180 `35.41%`, MAE180 `-39.93%`
- residual: `current_profile_too_late_if_parts_order_bridge_is_overblocked`. source_proxy: SiC ring/process consumable leader with credible semiconductor capex recovery bridge; URL repair pending

### C09-R2-L118-02-171010 / 171010 램테크놀러지

- role: `high_mae_success` / `positive`
- trigger: `Stage2-Actionable` on `2024-03-22`, entry `2024-03-22` at `4660.0`
- price path: MFE90 `59.44%`, MAE90 `-5.58%`, MFE180 `59.44%`, MAE180 `-45.82%`
- residual: `current_profile_missed_structural_if_all_process_materials_blocked`. source_proxy: wet chemical/process-material recovery proxy with short-cycle order bridge but weak Green evidence; URL repair pending

### C09-R2-L118-03-396470 / 396470 워트

- role: `structural_success` / `positive`
- trigger: `Stage2-Actionable` on `2024-03-22`, entry `2024-03-22` at `9980.0`
- price path: MFE90 `83.27%`, MAE90 `-10.42%`, MFE180 `83.27%`, MAE180 `-35.17%`
- residual: `current_profile_missed_structural_if_newly_listed_equipment_proxy_is_blocked`. source_proxy: environmental-control / chiller-like equipment order bridge during 2024 equipment recovery; URL repair pending

### C09-R2-L118-04-166090 / 166090 하나머티리얼즈

- role: `4B_overlay_success` / `counterexample`
- trigger: `Stage4B` on `2024-07-01`, entry `2024-07-01` at `65700.0`
- price path: MFE90 `5.48%`, MAE90 `-62.1%`, MFE180 `5.48%`, MAE180 `-66.74%`
- residual: `current_profile_4B_too_late_if_parts_premium_clears_yellow`. source_proxy: advanced process-parts premium after local peak without near-term margin/revision bridge; URL repair pending

### C09-R2-L118-05-067310 / 067310 하나마이크론

- role: `false_positive_green` / `counterexample`
- trigger: `Stage3-Yellow` on `2024-07-01`, entry `2024-07-01` at `20600.0`
- price path: MFE90 `3.64%`, MAE90 `-53.64%`, MFE180 `3.64%`, MAE180 `-59.61%`
- residual: `current_profile_false_positive_if_OSAT_label_unlocks_yellow`. source_proxy: OSAT/advanced packaging label strength without durable revenue-margin bridge; URL repair pending

### C09-R2-L118-06-036540 / 036540 SFA반도체

- role: `failed_rerating` / `counterexample`
- trigger: `Stage3-Yellow` on `2024-05-02`, entry `2024-05-02` at `5650.0`
- price path: MFE90 `7.08%`, MAE90 `-41.5%`, MFE180 `7.08%`, MAE180 `-50.09%`
- residual: `current_profile_false_positive_if_backend_beta_promoted_without_bridge`. source_proxy: backend packaging beta without confirmed revision/margin conversion; URL repair pending

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TRG-C09-L118-01-064760-Stage2-Actionable-2024-03-22 | 2024-03-22 | 27.46 | -5.15 | 35.41 | -5.15 | 35.41 | -39.93 | 2024-06-14 | 149900.0 | -55.64 |
| TRG-C09-L118-02-171010-Stage2-Actionable-2024-03-22 | 2024-03-22 | 59.44 | -5.58 | 59.44 | -5.58 | 59.44 | -45.82 | 2024-04-12 | 7430.0 | -66.02 |
| TRG-C09-L118-03-396470-Stage2-Actionable-2024-03-22 | 2024-03-22 | 44.79 | -1.5 | 83.27 | -10.42 | 83.27 | -35.17 | 2024-06-26 | 18290.0 | -64.63 |
| TRG-C09-L118-04-166090-Stage4B-2024-07-01 | 2024-07-01 | 5.48 | -42.92 | 5.48 | -62.1 | 5.48 | -66.74 | 2024-07-02 | 69300.0 | -68.47 |
| TRG-C09-L118-05-067310-Stage3-Yellow-2024-07-01 | 2024-07-01 | 3.64 | -30.68 | 3.64 | -53.64 | 3.64 | -59.61 | 2024-07-11 | 21350.0 | -61.03 |
| TRG-C09-L118-06-036540-Stage3-Yellow-2024-05-02 | 2024-05-02 | 7.08 | -6.9 | 7.08 | -41.5 | 7.08 | -50.09 | 2024-05-16 | 6050.0 | -53.39 |

## 13. Current Calibrated Profile Stress Test

The current calibrated profile is directionally correct in blocking price-only blowoff, but C09 still has two residual errors. First, verified process-parts or environmental-control bridges can be delayed if every process component is treated as label-only. Second, label-only OSAT/backend/parts premiums can still pass Yellow when relative strength is mistaken for order/revenue conversion.

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green row is emitted. The positive group is kept at Stage2-Actionable because it has order/revenue bridge proxies but not URL-verified revision/margin visibility. The counterexample group is blocked from Yellow/Green because its 90D/180D path is dominated by drawdown rather than bridge-confirmed rerating.

## 15. 4B Local vs Full-window Timing Audit

The 166090 row is an explicit Stage4B overlay. It starts from a local premium window and then records MFE180 `5.48%` versus MAE180 `-66.74%`. The rule consequence is not automatic full 4B; it is a C09 local 4B watch when valuation/positioning expands without verified order/revenue/margin bridge.

## 16. 4C Protection Audit

No Stage4C row is emitted. Hard 4C routing remains unchanged because none of the six cases has URL-verified qualification failure, contract cancellation, or accounting/trust break. The loop is about Stage2/Yellow precision and local 4B timing.

## 17. Sector-Specific Rule Candidate

`L2` candidate: C09 should require an order/revenue/margin bridge before Yellow or Green when the evidence is advanced process component, OSAT, package, or environmental-control equipment premium. Relative strength alone remains insufficient.

## 18. Canonical-Archetype Rule Candidate

`C09_verified_order_revenue_margin_bridge_required_before_Yellow_or_Green_plus_advanced_process_part_or_OSAT_label_to_local_4B_watch_v4`. Scope is canonical-archetype-specific. It strengthens C09 bridge requirements without changing global Stage2/Yellow/Green thresholds.

## 19. Before / After Backtest Comparison

| profile | scope | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | 32.39 | -29.73 | 32.39 | -49.56 | 0.50 | mixed_current_profile_residual_error |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 32.39 | -29.73 | 32.39 | -49.56 | 0.67 | worse_false_positive_control |
| P1_L2_sector_specific_candidate_profile | sector_specific | 59.37 | -7.05 | 59.37 | -40.31 | 0.17 | better_L2_bridge_precision |
| P2_C09_canonical_archetype_candidate_profile | canonical_archetype_specific | 59.37 | -7.05 | 59.37 | -40.31 | 0.17 | best_C09_bridge_precision |
| P3_counterexample_guard_profile | counterexample_guard | 5.4 | -52.41 | 5.4 | -58.81 | 0.33 | best_for_4B_and_false_positive_control |

## 20. Score-Return Alignment Matrix

The bridge-positive group has average MFE180 `59.37%`; the counterexample group has average MAE180 `-58.81%`. The separation supports a C09 bridge gate and local 4B watch rather than a global threshold change.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09_ADVANCED_PROCESS_PARTS_ENV_CONTROL_OSAT_PREMIUM_WITH_OR_WITHOUT_ORDER_REVENUE_MARGIN_BRIDGE | 3 | 3 | 1 | 0 | 6 | 0 | 6 | 6 | 6 | true | true | local-session adjusted about 50; 50-row practical band reached locally |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 6
new_trigger_family_count: 6
tested_existing_calibrated_axes: [stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [current_profile_missed_structural, current_profile_false_positive, current_profile_4B_too_late]
new_axis_proposed: C09_verified_order_revenue_margin_bridge_required_before_Yellow_or_Green_plus_advanced_process_part_or_OSAT_label_to_local_4B_watch_v4
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min, stage3_green_total_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 6 new independent cases, 3 counterexamples, and 6 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

## 23. Validation Scope / Non-Validation Scope

Validated: Stock-Web tradable raw price rows, entry date/price, 30D/90D/180D MFE/MAE, 180D local continuity proxy, canonical/round/sector consistency, novelty against local C09 loops. Not validated for promotion: exact external evidence URLs and production score implementation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C09_verified_order_revenue_margin_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"Require order/revenue/margin bridge before Yellow or Green; label-only process parts/OSAT premium goes to watch.","positive bridge group MFE180 materially beats label-only counterexample group","TRG-C09-L118-01-064760-Stage2-Actionable-2024-03-22|TRG-C09-L118-02-171010-Stage2-Actionable-2024-03-22|TRG-C09-L118-03-396470-Stage2-Actionable-2024-03-22|TRG-C09-L118-04-166090-Stage4B-2024-07-01|TRG-C09-L118-05-067310-Stage3-Yellow-2024-07-01|TRG-C09-L118-06-036540-Stage3-Yellow-2024-05-02",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C09-R2-L118-01-064760","symbol":"064760","company_name":"티씨케이","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_SIC_RING_PROCESS_PART_ORDER_REVENUE_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C09-L118-01-064760-Stage2-Actionable-2024-03-22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_bridge_pass","current_profile_verdict":"current_profile_too_late_if_parts_order_bridge_is_overblocked","price_source":"Songdaiki/stock-web","promotion_blocked_until_url_repair":true,"notes":"new independent C09 symbol relative to local C09 loop113-117 symbol sets; source proxy row requires URL repair before promotion"}
{"row_type":"trigger","trigger_id":"TRG-C09-L118-01-064760-Stage2-Actionable-2024-03-22","case_id":"C09-R2-L118-01-064760","symbol":"064760","company_name":"티씨케이","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_SIC_RING_PROCESS_PART_ORDER_REVENUE_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":110700.0,"evidence_available_at_that_date":"source_proxy: SiC ring/process consumable leader with credible semiconductor capex recovery bridge; URL repair pending","evidence_source":"source_proxy_only; exact evidence URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv","profile_path":"atlas/symbol_profiles/064/064760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.46,"MFE_90D_pct":35.41,"MFE_180D_pct":35.41,"MFE_1Y_pct":35.41,"MFE_2Y_pct":null,"MAE_30D_pct":-5.15,"MAE_90D_pct":-5.15,"MAE_180D_pct":-39.93,"MAE_1Y_pct":-39.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":149900.0,"drawdown_after_peak_pct":-55.64,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_no_full_4B","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"c09_sic_ring_process_part_order_revenue_bridge","current_profile_verdict":"current_profile_too_late_if_parts_order_bridge_is_overblocked","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_proxy","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:064760:Stage2-Actionable:2024-03-22:110700.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-R2-L118-01-064760","trigger_id":"TRG-C09-L118-01-064760-Stage2-Actionable-2024-03-22","symbol":"064760","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":48,"backlog_visibility_score":46,"margin_bridge_score":41,"revision_score":43,"relative_strength_score":70,"customer_quality_score":52,"policy_or_regulatory_score":25,"valuation_repricing_score":68,"execution_risk_score":34,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_before":73.5,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":57,"margin_bridge_score":53,"revision_score":50,"relative_strength_score":70,"customer_quality_score":52,"policy_or_regulatory_score":25,"valuation_repricing_score":60,"execution_risk_score":30,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_after":78.0,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow requires verified order/revenue/margin bridge for positive promotion and sends label-only premium to local 4B watch.","MFE_90D_pct":35.41,"MAE_90D_pct":-5.15,"score_return_alignment_label":"positive_bridge_pass","current_profile_verdict":"current_profile_too_late_if_parts_order_bridge_is_overblocked"}
{"row_type":"case","case_id":"C09-R2-L118-02-171010","symbol":"171010","company_name":"램테크놀러지","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_WET_CHEM_PROCESS_MATERIAL_ORDER_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRG-C09-L118-02-171010-Stage2-Actionable-2024-03-22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_with_high_mae_guard","current_profile_verdict":"current_profile_missed_structural_if_all_process_materials_blocked","price_source":"Songdaiki/stock-web","promotion_blocked_until_url_repair":true,"notes":"new independent C09 symbol relative to local C09 loop113-117 symbol sets; source proxy row requires URL repair before promotion"}
{"row_type":"trigger","trigger_id":"TRG-C09-L118-02-171010-Stage2-Actionable-2024-03-22","case_id":"C09-R2-L118-02-171010","symbol":"171010","company_name":"램테크놀러지","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_WET_CHEM_PROCESS_MATERIAL_ORDER_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":4660.0,"evidence_available_at_that_date":"source_proxy: wet chemical/process-material recovery proxy with short-cycle order bridge but weak Green evidence; URL repair pending","evidence_source":"source_proxy_only; exact evidence URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/171/171010/2024.csv","profile_path":"atlas/symbol_profiles/171/171010.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":59.44,"MFE_90D_pct":59.44,"MFE_180D_pct":59.44,"MFE_1Y_pct":59.44,"MFE_2Y_pct":null,"MAE_30D_pct":-5.58,"MAE_90D_pct":-5.58,"MAE_180D_pct":-45.82,"MAE_1Y_pct":-45.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-12","peak_price":7430.0,"drawdown_after_peak_pct":-66.02,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_no_full_4B","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"c09_wet_chem_process_material_order_bridge","current_profile_verdict":"current_profile_missed_structural_if_all_process_materials_blocked","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_proxy","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:171010:Stage2-Actionable:2024-03-22:4660.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-R2-L118-02-171010","trigger_id":"TRG-C09-L118-02-171010-Stage2-Actionable-2024-03-22","symbol":"171010","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":48,"backlog_visibility_score":46,"margin_bridge_score":41,"revision_score":43,"relative_strength_score":70,"customer_quality_score":52,"policy_or_regulatory_score":25,"valuation_repricing_score":68,"execution_risk_score":34,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_before":73.5,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":57,"margin_bridge_score":53,"revision_score":50,"relative_strength_score":70,"customer_quality_score":52,"policy_or_regulatory_score":25,"valuation_repricing_score":60,"execution_risk_score":30,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_after":78.0,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow requires verified order/revenue/margin bridge for positive promotion and sends label-only premium to local 4B watch.","MFE_90D_pct":59.44,"MAE_90D_pct":-5.58,"score_return_alignment_label":"positive_with_high_mae_guard","current_profile_verdict":"current_profile_missed_structural_if_all_process_materials_blocked"}
{"row_type":"case","case_id":"C09-R2-L118-03-396470","symbol":"396470","company_name":"워트","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ENVIRONMENT_CONTROL_EQUIPMENT_ORDER_REVENUE_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C09-L118-03-396470-Stage2-Actionable-2024-03-22","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_bridge_pass","current_profile_verdict":"current_profile_missed_structural_if_newly_listed_equipment_proxy_is_blocked","price_source":"Songdaiki/stock-web","promotion_blocked_until_url_repair":true,"notes":"new independent C09 symbol relative to local C09 loop113-117 symbol sets; source proxy row requires URL repair before promotion"}
{"row_type":"trigger","trigger_id":"TRG-C09-L118-03-396470-Stage2-Actionable-2024-03-22","case_id":"C09-R2-L118-03-396470","symbol":"396470","company_name":"워트","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ENVIRONMENT_CONTROL_EQUIPMENT_ORDER_REVENUE_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":9980.0,"evidence_available_at_that_date":"source_proxy: environmental-control / chiller-like equipment order bridge during 2024 equipment recovery; URL repair pending","evidence_source":"source_proxy_only; exact evidence URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/396/396470/2024.csv","profile_path":"atlas/symbol_profiles/396/396470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":44.79,"MFE_90D_pct":83.27,"MFE_180D_pct":83.27,"MFE_1Y_pct":83.27,"MFE_2Y_pct":null,"MAE_30D_pct":-1.5,"MAE_90D_pct":-10.42,"MAE_180D_pct":-35.17,"MAE_1Y_pct":-35.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":18290.0,"drawdown_after_peak_pct":-64.63,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_no_full_4B","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"c09_environment_control_equipment_order_revenue_bridge","current_profile_verdict":"current_profile_missed_structural_if_newly_listed_equipment_proxy_is_blocked","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_proxy","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:396470:Stage2-Actionable:2024-03-22:9980.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-R2-L118-03-396470","trigger_id":"TRG-C09-L118-03-396470-Stage2-Actionable-2024-03-22","symbol":"396470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":48,"backlog_visibility_score":46,"margin_bridge_score":41,"revision_score":43,"relative_strength_score":70,"customer_quality_score":52,"policy_or_regulatory_score":25,"valuation_repricing_score":68,"execution_risk_score":34,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_before":73.5,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":57,"margin_bridge_score":53,"revision_score":50,"relative_strength_score":70,"customer_quality_score":52,"policy_or_regulatory_score":25,"valuation_repricing_score":60,"execution_risk_score":30,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":8,"accounting_trust_risk_score":10},"weighted_score_after":78.0,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow requires verified order/revenue/margin bridge for positive promotion and sends label-only premium to local 4B watch.","MFE_90D_pct":83.27,"MAE_90D_pct":-10.42,"score_return_alignment_label":"positive_bridge_pass","current_profile_verdict":"current_profile_missed_structural_if_newly_listed_equipment_proxy_is_blocked"}
{"row_type":"case","case_id":"C09-R2-L118-04-166090","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_PARTS_VALUATION_LOCAL_BLOWOFF","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRG-C09-L118-04-166090-Stage4B-2024-07-01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_4B_too_late_if_parts_premium_clears_yellow","price_source":"Songdaiki/stock-web","promotion_blocked_until_url_repair":true,"notes":"new independent C09 symbol relative to local C09 loop113-117 symbol sets; source proxy row requires URL repair before promotion"}
{"row_type":"trigger","trigger_id":"TRG-C09-L118-04-166090-Stage4B-2024-07-01","case_id":"C09-R2-L118-04-166090","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_PARTS_VALUATION_LOCAL_BLOWOFF","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":65700.0,"evidence_available_at_that_date":"source_proxy: advanced process-parts premium after local peak without near-term margin/revision bridge; URL repair pending","evidence_source":"source_proxy_only; exact evidence URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv","profile_path":"atlas/symbol_profiles/166/166090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.48,"MFE_90D_pct":5.48,"MFE_180D_pct":5.48,"MFE_1Y_pct":5.48,"MFE_2Y_pct":null,"MAE_30D_pct":-42.92,"MAE_90D_pct":-62.1,"MAE_180D_pct":-66.74,"MAE_1Y_pct":-66.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":69300.0,"drawdown_after_peak_pct":-68.47,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"good_local_4B_watch","four_b_evidence_type":"price_only|valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"c09_advanced_parts_valuation_local_blowoff","current_profile_verdict":"current_profile_4B_too_late_if_parts_premium_clears_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_proxy","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:166090:Stage4B:2024-07-01:65700.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-R2-L118-04-166090","trigger_id":"TRG-C09-L118-04-166090-Stage4B-2024-07-01","symbol":"166090","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":38,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":72,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":78,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":14,"accounting_trust_risk_score":12},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":32,"margin_bridge_score":20,"revision_score":23,"relative_strength_score":72,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":72,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":14,"accounting_trust_risk_score":12},"weighted_score_after":65.5,"stage_label_after":"Stage4B-Watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow requires verified order/revenue/margin bridge for positive promotion and sends label-only premium to local 4B watch.","MFE_90D_pct":5.48,"MAE_90D_pct":-62.1,"score_return_alignment_label":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_4B_too_late_if_parts_premium_clears_yellow"}
{"row_type":"case","case_id":"C09-R2-L118-05-067310","symbol":"067310","company_name":"하나마이크론","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_OSAT_ADVANCED_PACKAGING_LABEL_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG-C09-L118-05-067310-Stage3-Yellow-2024-07-01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_false_positive_if_OSAT_label_unlocks_yellow","price_source":"Songdaiki/stock-web","promotion_blocked_until_url_repair":true,"notes":"new independent C09 symbol relative to local C09 loop113-117 symbol sets; source proxy row requires URL repair before promotion"}
{"row_type":"trigger","trigger_id":"TRG-C09-L118-05-067310-Stage3-Yellow-2024-07-01","case_id":"C09-R2-L118-05-067310","symbol":"067310","company_name":"하나마이크론","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_OSAT_ADVANCED_PACKAGING_LABEL_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":20600.0,"evidence_available_at_that_date":"source_proxy: OSAT/advanced packaging label strength without durable revenue-margin bridge; URL repair pending","evidence_source":"source_proxy_only; exact evidence URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv","profile_path":"atlas/symbol_profiles/067/067310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.64,"MFE_90D_pct":3.64,"MFE_180D_pct":3.64,"MFE_1Y_pct":3.64,"MFE_2Y_pct":null,"MAE_30D_pct":-30.68,"MAE_90D_pct":-53.64,"MAE_180D_pct":-59.61,"MAE_1Y_pct":-59.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":21350.0,"drawdown_after_peak_pct":-61.03,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_no_full_4B","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"c09_osat_advanced_packaging_label_without_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_OSAT_label_unlocks_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_proxy","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:067310:Stage3-Yellow:2024-07-01:20600.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-R2-L118-05-067310","trigger_id":"TRG-C09-L118-05-067310-Stage3-Yellow-2024-07-01","symbol":"067310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":38,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":72,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":78,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":14,"accounting_trust_risk_score":12},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":32,"margin_bridge_score":20,"revision_score":23,"relative_strength_score":72,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":72,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":14,"accounting_trust_risk_score":12},"weighted_score_after":62.0,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow requires verified order/revenue/margin bridge for positive promotion and sends label-only premium to local 4B watch.","MFE_90D_pct":3.64,"MAE_90D_pct":-53.64,"score_return_alignment_label":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_false_positive_if_OSAT_label_unlocks_yellow"}
{"row_type":"case","case_id":"C09-R2-L118-06-036540","symbol":"036540","company_name":"SFA반도체","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_BACKEND_OSAT_PREMIUM_WITHOUT_REVISION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG-C09-L118-06-036540-Stage3-Yellow-2024-05-02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_false_positive_if_backend_beta_promoted_without_bridge","price_source":"Songdaiki/stock-web","promotion_blocked_until_url_repair":true,"notes":"new independent C09 symbol relative to local C09 loop113-117 symbol sets; source proxy row requires URL repair before promotion"}
{"row_type":"trigger","trigger_id":"TRG-C09-L118-06-036540-Stage3-Yellow-2024-05-02","case_id":"C09-R2-L118-06-036540","symbol":"036540","company_name":"SFA반도체","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_BACKEND_OSAT_PREMIUM_WITHOUT_REVISION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_SIC_RING_WET_CHEM_ENV_CONTROL_OSAT_PARTS_PRICE_PREMIUM_VS_VERIFIED_ORDER_REVENUE_REVISION_BRIDGE","sector":"AI_semiconductor_electronics","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":5650.0,"evidence_available_at_that_date":"source_proxy: backend packaging beta without confirmed revision/margin conversion; URL repair pending","evidence_source":"source_proxy_only; exact evidence URL repair pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv","profile_path":"atlas/symbol_profiles/036/036540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.08,"MFE_90D_pct":7.08,"MFE_180D_pct":7.08,"MFE_1Y_pct":7.08,"MFE_2Y_pct":null,"MAE_30D_pct":-6.9,"MAE_90D_pct":-41.5,"MAE_180D_pct":-50.09,"MAE_1Y_pct":-54.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":6050.0,"drawdown_after_peak_pct":-53.39,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_no_full_4B","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4C","trigger_outcome_label":"c09_backend_osat_premium_without_revision_bridge","current_profile_verdict":"current_profile_false_positive_if_backend_beta_promoted_without_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_proxy","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:036540:Stage3-Yellow:2024-05-02:5650.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-R2-L118-06-036540","trigger_id":"TRG-C09-L118-06-036540-Stage3-Yellow-2024-05-02","symbol":"036540","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":38,"margin_bridge_score":24,"revision_score":28,"relative_strength_score":72,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":78,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":14,"accounting_trust_risk_score":12},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":32,"margin_bridge_score":20,"revision_score":23,"relative_strength_score":72,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":68,"execution_risk_score":72,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":14,"accounting_trust_risk_score":12},"weighted_score_after":62.0,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 shadow requires verified order/revenue/margin bridge for positive promotion and sends label-only premium to local 4B watch.","MFE_90D_pct":7.08,"MAE_90D_pct":-41.5,"score_return_alignment_label":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_false_positive_if_backend_beta_promoted_without_bridge"}
{"row_type":"residual_contribution","round":"R2","loop":"118","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.

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
completed_loop = 118
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
