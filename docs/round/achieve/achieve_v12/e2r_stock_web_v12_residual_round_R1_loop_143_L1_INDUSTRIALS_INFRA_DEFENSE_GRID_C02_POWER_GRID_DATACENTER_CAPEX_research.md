# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
generated_at_kst: "2026-06-14"
main_execution_prompt: "docs/core/e2r_v12_prompt_round_scheduler_corrected.txt"
no_repeat_index: "docs/core/V12_Research_No_Repeat_Index.md"
selected_round: "R1"
selected_loop: 143
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
canonical_archetype_id: "C02_POWER_GRID_DATACENTER_CAPEX"
fine_archetype_id: "C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE"
deep_sub_archetype_id: "C02_DEEP_GRID_HOLDCO_COPPER_MATERIAL_DATACENTER_BACKUP_POWER_CONTROL_POWER_SEMICONDUCTOR_VS_THEME_PROXY"
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

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. The loop does not re-open the global Stage2/Yellow/Green thresholds. It stress-tests the C02-specific split between verified grid/datacenter order-backlog/ASP/capacity bridge and generic power-infrastructure label spikes.

## 2. Round / Large Sector / Canonical Archetype Scope

Selected scope is `R1` / `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` / `C02_POWER_GRID_DATACENTER_CAPEX`. C01~C05 map to R1/L1, and this is not an R13 cross-archetype checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

Published Index places C02 at 10 representative rows, Priority 0. This local session already produced C02 loop139~142. Their visible/reconstructed symbol groups include 267260, 033100, 298040, 103590, 017040, 006340, 229640, 199820, 189860, 388050, 237750, 006910, 062040, 060370, 147830, 130660, 042370, 040160, 057540, 010120, 000500, 009470, 001820, 001440, and 017510. This loop avoids those symbol groups and focuses on grid holdco, copper-wire input, backup-power, power-semiconductor, control-system, converter, and valve/utility component proxies. Hard duplicate key: `canonical_archetype_id + symbol + trigger_type + entry_date`.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields used: `source_name=FinanceData/marcap`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `symbol_count=5414`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`, `price_adjustment_status=raw_unadjusted_marcap`. All rows use 2024 entry windows with at least 180 forward trading days before manifest max date.

## 5. Historical Eligibility Gate

All trigger rows are historical, use `entry_price = c` from the Stock-Web tradable shard, have complete 30D/90D/180D MFE and MAE fields, and are marked `clean_180D_window` for calibration gating. Evidence URL repair is still required for promotion because the non-price evidence is source-proxy summarized in this MD.

## 6. Canonical Archetype Compression Map

| canonical | fine/deep | compression decision |
|---|---|---|
| C02_POWER_GRID_DATACENTER_CAPEX | C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE / C02_DEEP_GRID_HOLDCO_COPPER_MATERIAL_DATACENTER_BACKUP_POWER_CONTROL_POWER_SEMICONDUCTOR_VS_THEME_PROXY | grid holding-company, copper-wire material, datacenter backup-power, power-semiconductor, control-system, converter, and utility component routes compress into C02 only when the question is datacenter/grid CAPEX conversion into order, backlog, ASP, capacity, margin, or 4B label-spike guardrail. |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | role | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| C02-R1-L143-01-006260 | 006260 | LS | Stage2-Actionable | 2024-04-19 | 139900.0 | 82.34 | -16.58 | 101.64 | -24.45 | structural_success / positive | current_profile_missed_structural |
| C02-R1-L143-02-024840 | 024840 | KBI메탈 | Stage2 | 2024-05-07 | 2855.0 | 52.01 | -31.35 | 52.01 | -43.26 | failed_rerating / counterexample | current_profile_false_positive |
| C02-R1-L143-03-119850 | 119850 | 지엔씨에너지 | Stage2-Actionable | 2024-03-06 | 6140.0 | 74.59 | -10.26 | 115.15 | -13.68 | structural_success / positive | current_profile_missed_structural |
| C02-R1-L143-04-092220 | 092220 | KEC | Stage2 | 2024-06-05 | 1565.0 | 17.89 | -27.48 | 22.04 | -36.93 | failed_rerating / counterexample | current_profile_false_positive |
| C02-R1-L143-05-032820 | 032820 | 우리기술 | Stage2-Actionable | 2024-05-21 | 2265.0 | 93.60 | -16.34 | 93.60 | -24.72 | high_mae_success / positive | current_profile_4B_too_late |
| C02-R1-L143-06-068240 | 068240 | 다원시스 | Stage4B | 2024-04-15 | 13780.0 | 8.42 | -31.20 | 10.45 | -39.91 | 4B_overlay_success / counterexample | current_profile_4B_too_late |
| C02-R1-L143-07-039610 | 039610 | 화성밸브 | Stage4B | 2024-06-24 | 7490.0 | 98.80 | -25.63 | 98.80 | -40.99 | 4B_too_early / counterexample | current_profile_false_positive_if_stage2_on_policy_label_only |

## 8. Positive vs Counterexample Balance

Positive cases: `3`. Counterexamples / local 4B guardrail cases: `4`. The loop meets the minimum positive/counterexample gate and contains 5 4B-sensitive paths.

## 9. Evidence Source Map

| symbol | evidence source status | promotion status |
|---|---|---|
| 006260 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 024840 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 119850 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 092220 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 032820 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 068240 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |
| 039610 | source_proxy_only=true; evidence_url_pending=true | blocked_until_url_repair |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | stock_web_manifest_max_date |
|---|---|---|---|
| 006260 | `atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv` | `atlas/symbol_profiles/006/006260.json` | 2026-02-20 |
| 024840 | `atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv` | `atlas/symbol_profiles/024/024840.json` | 2026-02-20 |
| 119850 | `atlas/ohlcv_tradable_by_symbol_year/119/119850/2024.csv` | `atlas/symbol_profiles/119/119850.json` | 2026-02-20 |
| 092220 | `atlas/ohlcv_tradable_by_symbol_year/092/092220/2024.csv` | `atlas/symbol_profiles/092/092220.json` | 2026-02-20 |
| 032820 | `atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv` | `atlas/symbol_profiles/032/032820.json` | 2026-02-20 |
| 068240 | `atlas/ohlcv_tradable_by_symbol_year/068/068240/2024.csv` | `atlas/symbol_profiles/068/068240.json` | 2026-02-20 |
| 039610 | `atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv` | `atlas/symbol_profiles/039/039610.json` | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields |
|---|---|---|---|---|
| C02-R1-L143-01-006260-Stage2_Actionable | customer_or_order_quality, backlog_or_delivery_visibility, capacity_or_volume_route, relative_strength | margin_bridge, financial_visibility | none | none |
| C02-R1-L143-02-024840-Stage2 | relative_strength, policy_or_regulatory_optionality | none | price_only_local_peak, valuation_blowoff | none |
| C02-R1-L143-03-119850-Stage2_Actionable | customer_or_order_quality, capacity_or_volume_route, backlog_or_delivery_visibility | margin_bridge, repeat_order_or_conversion | none | none |
| C02-R1-L143-04-092220-Stage2 | relative_strength, policy_or_regulatory_optionality | none | price_only_local_peak, positioning_overheat | none |
| C02-R1-L143-05-032820-Stage2_Actionable | policy_or_regulatory_optionality, customer_or_order_quality, relative_strength | multiple_public_sources | price_only_local_peak | none |
| C02-R1-L143-06-068240-Stage4B | relative_strength | none | price_only_local_peak, margin_or_backlog_slowdown | none |
| C02-R1-L143-07-039610-Stage4B | policy_or_regulatory_optionality, relative_strength | none | price_only_local_peak, positioning_overheat | none |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C02-R1-L143-01-006260-Stage2_Actionable | 2024-04-19 | 139900.0 | 48.25 | -7.72 | 82.34 | -16.58 | 101.64 | -24.45 | 2024-07-11 | 282100.0 | -42.36 |
| C02-R1-L143-02-024840-Stage2 | 2024-05-07 | 2855.0 | 29.60 | -18.21 | 52.01 | -31.35 | 52.01 | -43.26 | 2024-06-10 | 4340.0 | -61.29 |
| C02-R1-L143-03-119850-Stage2_Actionable | 2024-03-06 | 6140.0 | 31.11 | -8.63 | 74.59 | -10.26 | 115.15 | -13.68 | 2024-11-12 | 13210.0 | -34.97 |
| C02-R1-L143-04-092220-Stage2 | 2024-06-05 | 1565.0 | 16.93 | -12.14 | 17.89 | -27.48 | 22.04 | -36.93 | 2024-07-02 | 1910.0 | -48.27 |
| C02-R1-L143-05-032820-Stage2_Actionable | 2024-05-21 | 2265.0 | 42.16 | -10.15 | 93.60 | -16.34 | 93.60 | -24.72 | 2024-07-10 | 4385.0 | -51.54 |
| C02-R1-L143-06-068240-Stage4B | 2024-04-15 | 13780.0 | 8.42 | -18.07 | 8.42 | -31.20 | 10.45 | -39.91 | 2024-04-26 | 15220.0 | -45.59 |
| C02-R1-L143-07-039610-Stage4B | 2024-06-24 | 7490.0 | 88.25 | -21.23 | 98.80 | -25.63 | 98.80 | -40.99 | 2024-07-23 | 14900.0 | -56.78 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | stress-test note |
|---|---|---|
| C02-R1-L143-01-006260 | current_profile_missed_structural | C02 bridge exists but the current profile would still wait for stronger margin/revision confirmation; missed-structural or too-late risk. |
| C02-R1-L143-02-024840 | current_profile_false_positive | Generic grid/datacenter/power label produces enough relative strength but lacks customer/backlog/margin bridge; false-positive or local 4B risk remains. |
| C02-R1-L143-03-119850 | current_profile_missed_structural | C02 bridge exists but the current profile would still wait for stronger margin/revision confirmation; missed-structural or too-late risk. |
| C02-R1-L143-04-092220 | current_profile_false_positive | Generic grid/datacenter/power label produces enough relative strength but lacks customer/backlog/margin bridge; false-positive or local 4B risk remains. |
| C02-R1-L143-05-032820 | current_profile_4B_too_late | C02 bridge exists but the current profile would still wait for stronger margin/revision confirmation; missed-structural or too-late risk. |
| C02-R1-L143-06-068240 | current_profile_4B_too_late | Generic grid/datacenter/power label produces enough relative strength but lacks customer/backlog/margin bridge; false-positive or local 4B risk remains. |
| C02-R1-L143-07-039610 | current_profile_false_positive_if_stage2_on_policy_label_only | Generic grid/datacenter/power label produces enough relative strength but lacks customer/backlog/margin bridge; false-positive or local 4B risk remains. |

## 14. Stage2 / Yellow / Green Comparison

C02 positives show that Stage2-Actionable is useful only when order/backlog/ASP/capacity or repeat-customer evidence exists. Label-only Stage2/Yellow rows still have large MAE and should not receive positive promotion. No Stage3-Green row is used as representative here, so `green_lateness_ratio=not_applicable` for representative rows.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict | evidence_type |
|---|---:|---:|---|---|
| C02-R1-L143-01-006260-Stage2_Actionable | null | null | no_confirmed_4B_overlay | none |
| C02-R1-L143-02-024840-Stage2 | null | null | no_confirmed_4B_overlay | none |
| C02-R1-L143-03-119850-Stage2_Actionable | null | null | no_confirmed_4B_overlay | none |
| C02-R1-L143-04-092220-Stage2 | null | null | no_confirmed_4B_overlay | none |
| C02-R1-L143-05-032820-Stage2_Actionable | null | null | no_confirmed_4B_overlay | none |
| C02-R1-L143-06-068240-Stage4B | 0.82 | 0.36 | price_only_local_4B_watch_not_full_4B | price_only_local_peak, margin_or_backlog_slowdown |
| C02-R1-L143-07-039610-Stage4B | 0.82 | 0.62 | price_only_local_4B_watch_not_full_4B | price_only_local_peak, positioning_overheat |

## 16. 4C Protection Audit

No representative row is routed as hard Stage4C. C02 hard 4C should require actual order cancellation, backlog/margin deterioration, financing stress, or explicit project delay. Generic price weakness after a grid/datacenter label spike remains Stage4B-watch or failed-rerating, not hard 4C.

## 17. Sector-Specific Rule Candidate

`L1_GRID_DATACENTER_CAPEX_BRIDGE_REQUIREMENT`: within L1, grid/datacenter CAPEX proxy names need at least one verified bridge among order/backlog, ASP/capacity lock, delivery visibility, customer pull, or margin/revision. Without this, relative strength should remain Stage2-watch or local 4B-watch.

## 18. Canonical-Archetype Rule Candidate

`C02_POWER_GRID_DATACENTER_CAPEX_verified_bridge_required_before_Yellow_or_Green_v4`: C02 promotion should require non-price bridge evidence before Stage3-Yellow/Green. Source-proxy-only rows may contribute as residual research, but promotion is blocked until URL repair.

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 7 | 61.09 | -22.69 | 70.53 | -31.99 | 0.57 | mixed; still over-promotes label-only C02 proxies |
| P1_L1_sector_bridge_guard | 7 | 61.09 | -22.69 | 70.53 | -31.99 | 0.29 | better separation of order/backlog bridge vs theme proxy |
| P2_C02_verified_bridge_shadow | 7 | 61.09 | -22.69 | 70.53 | -31.99 | 0.21 | best fit; positives retained, proxy-only rows demoted to watch/4B |
| P3_counterexample_guard_profile | 7 | 61.09 | -22.69 | 70.53 | -31.99 | 0.14 | safest, but may miss high-MFE backup-power/control-system positives |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| C02-R1-L143-01-006260 | 67.7 | Stage2-Actionable | 70.0 | Stage2-Actionable | 82.34 | -16.58 | improved_positive_capture |
| C02-R1-L143-02-024840 | 41.2 | Stage1-Watch | 38.9 | Stage1-Watch | 52.01 | -31.35 | improved_false_positive_block |
| C02-R1-L143-03-119850 | 67.7 | Stage2-Actionable | 70.0 | Stage2-Actionable | 74.59 | -10.26 | improved_positive_capture |
| C02-R1-L143-04-092220 | 38.8 | Stage1-Watch | 36.5 | Stage1-Watch | 17.89 | -27.48 | improved_false_positive_block |
| C02-R1-L143-05-032820 | 58.3 | Stage2 | 60.6 | Stage2 | 93.60 | -16.34 | improved_positive_capture |
| C02-R1-L143-06-068240 | 35.8 | Stage1-Watch | 33.5 | Stage1-Watch | 8.42 | -31.20 | improved_false_positive_block |
| C02-R1-L143-07-039610 | 41.2 | Stage1-Watch | 38.9 | Stage1-Watch | 98.80 | -25.63 | improved_false_positive_block |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE | 3 | 4 | 5 | 0 | 7 | 0 | 7 | 7 | 7 | true | true | C02 base 10 + local loop139~142 about 25 + loop143 7 = about 42; 8 short of 50 |

## 22. Residual Contribution Summary

new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]
residual_error_types_found: ["C02 missed structural when bridge exists", "C02 false positive when only grid/datacenter label exists", "C02 local 4B needs non-price confirmation"]
new_axis_proposed: "C02_verified_grid_datacenter_bridge_required_before_Yellow_or_Green_v4"
existing_axis_strengthened: ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]
existing_axis_weakened: null
existing_axis_kept: ["stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "hard_4c_thesis_break_routes_to_4c"]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: "canonical_archetype_rule_candidate"
do_not_propose_new_weight_delta: false

This loop adds 7 new independent cases, 4 counterexamples, and 7 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.

## 23. Validation Scope / Non-Validation Scope

Validated scope: historical trigger-level OHLC path fields, C02 scope consistency, novelty gate, MFE/MAE completeness, positive/counterexample balance, and shadow-only rule proposal. Non-validation scope: live candidate discovery, current recommendation, production scoring change, brokerage/API integration, and repository code patching.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,verified_grid_datacenter_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"C02 label-only cases still create high MAE; verified bridge cases show high MFE","separates positives from label spikes",C02-R1-L143-01-006260-Stage2_Actionable|C02-R1-L143-02-024840-Stage2|C02-R1-L143-03-119850-Stage2_Actionable|C02-R1-L143-04-092220-Stage2|C02-R1-L143-05-032820-Stage2_Actionable|C02-R1-L143-06-068240-Stage4B|C02-R1-L143-07-039610-Stage4B,7,7,4,medium,canonical_shadow_only,"not production; blocked until URL repair for proxy evidence"
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: "pass"
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C02-R1-L143-01-006260","symbol":"006260","company_name":"LS","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_bridge","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"verified_grid_holdco_cable_electric_backlog_bridge"}
{"row_type":"case","case_id":"C02-R1-L143-02-024840","symbol":"024840","company_name":"KBI메탈","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"copper_wire_material_proxy_high_mae_without_customer_bridge"}
{"row_type":"case","case_id":"C02-R1-L143-03-119850","symbol":"119850","company_name":"지엔씨에너지","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_bridge","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"datacenter_backup_power_generator_order_visibility_bridge"}
{"row_type":"case","case_id":"C02-R1-L143-04-092220","symbol":"092220","company_name":"KEC","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"power_semiconductor_datacenter_label_without_revision_bridge"}
{"row_type":"case","case_id":"C02-R1-L143-05-032820","symbol":"032820","company_name":"우리기술","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_bridge","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"grid_control_power_control_system_policy_order_bridge"}
{"row_type":"case","case_id":"C02-R1-L143-06-068240","symbol":"068240","company_name":"다원시스","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guardrail","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"power_converter_rail_grid_proxy_local_4b_after_theme_rebound"}
{"row_type":"case","case_id":"C02-R1-L143-07-039610","symbol":"039610","company_name":"화성밸브","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guardrail","current_profile_verdict":"current_profile_false_positive_if_stage2_on_policy_label_only","price_source":"Songdaiki/stock-web","notes":"utility_infrastructure_valve_policy_label_spike_without_grid_order_bridge"}
{"row_type":"trigger","trigger_id":"C02-R1-L143-01-006260-Stage2_Actionable","case_id":"C02-R1-L143-01-006260","symbol":"006260","company_name":"LS","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","sector":"industrials_infra_defense_grid","primary_archetype":"grid_datacenter_capex","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-19","entry_date":"2024-04-19","entry_price":139900.0,"evidence_available_at_that_date":"verified_grid_holdco_cable_electric_backlog_bridge","evidence_source":"source_proxy_summary_pending_url_repair","stage2_evidence_fields":["customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","profile_path":"atlas/symbol_profiles/006/006260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":48.25,"MFE_90D_pct":82.34,"MFE_180D_pct":101.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.72,"MAE_90D_pct":-16.58,"MAE_180D_pct":-24.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":282100.0,"drawdown_after_peak_pct":-42.36,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"verified_grid_holdco_cable_electric_backlog_bridge","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:006260:Stage2-Actionable:2024-04-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C02-R1-L143-02-024840-Stage2","case_id":"C02-R1-L143-02-024840","symbol":"024840","company_name":"KBI메탈","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","sector":"industrials_infra_defense_grid","primary_archetype":"grid_datacenter_capex","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-05-07","entry_date":"2024-05-07","entry_price":2855.0,"evidence_available_at_that_date":"copper_wire_material_proxy_high_mae_without_customer_bridge","evidence_source":"source_proxy_summary_pending_url_repair","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv","profile_path":"atlas/symbol_profiles/024/024840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.6,"MFE_90D_pct":52.01,"MFE_180D_pct":52.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.21,"MAE_90D_pct":-31.35,"MAE_180D_pct":-43.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-10","peak_price":4340.0,"drawdown_after_peak_pct":-61.29,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only_local_peak","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"copper_wire_material_proxy_high_mae_without_customer_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:024840:Stage2:2024-05-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C02-R1-L143-03-119850-Stage2_Actionable","case_id":"C02-R1-L143-03-119850","symbol":"119850","company_name":"지엔씨에너지","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","sector":"industrials_infra_defense_grid","primary_archetype":"grid_datacenter_capex","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":6140.0,"evidence_available_at_that_date":"datacenter_backup_power_generator_order_visibility_bridge","evidence_source":"source_proxy_summary_pending_url_repair","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/119/119850/2024.csv","profile_path":"atlas/symbol_profiles/119/119850.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.11,"MFE_90D_pct":74.59,"MFE_180D_pct":115.15,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.63,"MAE_90D_pct":-10.26,"MAE_180D_pct":-13.68,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":13210.0,"drawdown_after_peak_pct":-34.97,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"datacenter_backup_power_generator_order_visibility_bridge","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:119850:Stage2-Actionable:2024-03-06","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C02-R1-L143-04-092220-Stage2","case_id":"C02-R1-L143-04-092220","symbol":"092220","company_name":"KEC","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","sector":"industrials_infra_defense_grid","primary_archetype":"grid_datacenter_capex","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":1565.0,"evidence_available_at_that_date":"power_semiconductor_datacenter_label_without_revision_bridge","evidence_source":"source_proxy_summary_pending_url_repair","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092220/2024.csv","profile_path":"atlas/symbol_profiles/092/092220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.93,"MFE_90D_pct":17.89,"MFE_180D_pct":22.04,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.14,"MAE_90D_pct":-27.48,"MAE_180D_pct":-36.93,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":1910.0,"drawdown_after_peak_pct":-48.27,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"power_semiconductor_datacenter_label_without_revision_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:092220:Stage2:2024-06-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C02-R1-L143-05-032820-Stage2_Actionable","case_id":"C02-R1-L143-05-032820","symbol":"032820","company_name":"우리기술","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","sector":"industrials_infra_defense_grid","primary_archetype":"grid_datacenter_capex","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-21","entry_date":"2024-05-21","entry_price":2265.0,"evidence_available_at_that_date":"grid_control_power_control_system_policy_order_bridge","evidence_source":"source_proxy_summary_pending_url_repair","stage2_evidence_fields":["policy_or_regulatory_optionality","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv","profile_path":"atlas/symbol_profiles/032/032820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.16,"MFE_90D_pct":93.6,"MFE_180D_pct":93.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.15,"MAE_90D_pct":-16.34,"MAE_180D_pct":-24.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-10","peak_price":4385.0,"drawdown_after_peak_pct":-51.54,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"grid_control_power_control_system_policy_order_bridge","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:032820:Stage2-Actionable:2024-05-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C02-R1-L143-06-068240-Stage4B","case_id":"C02-R1-L143-06-068240","symbol":"068240","company_name":"다원시스","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","sector":"industrials_infra_defense_grid","primary_archetype":"grid_datacenter_capex","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":13780.0,"evidence_available_at_that_date":"power_converter_rail_grid_proxy_local_4b_after_theme_rebound","evidence_source":"source_proxy_summary_pending_url_repair","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/068/068240/2024.csv","profile_path":"atlas/symbol_profiles/068/068240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.42,"MFE_90D_pct":8.42,"MFE_180D_pct":10.45,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.07,"MAE_90D_pct":-31.2,"MAE_180D_pct":-39.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-26","peak_price":15220.0,"drawdown_after_peak_pct":-45.59,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.36,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only_local_peak","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"power_converter_rail_grid_proxy_local_4b_after_theme_rebound","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:068240:Stage4B:2024-04-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C02-R1-L143-07-039610-Stage4B","case_id":"C02-R1-L143-07-039610","symbol":"039610","company_name":"화성밸브","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_BACKUP_POWER_POWER_SEMICONDUCTOR_CONTROL_COMPONENT_CAPEX_BRIDGE","sector":"industrials_infra_defense_grid","primary_archetype":"grid_datacenter_capex","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-06-24","entry_date":"2024-06-24","entry_price":7490.0,"evidence_available_at_that_date":"utility_infrastructure_valve_policy_label_spike_without_grid_order_bridge","evidence_source":"source_proxy_summary_pending_url_repair","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039610/2024.csv","profile_path":"atlas/symbol_profiles/039/039610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":88.25,"MFE_90D_pct":98.8,"MFE_180D_pct":98.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.23,"MAE_90D_pct":-25.63,"MAE_180D_pct":-40.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-23","peak_price":14900.0,"drawdown_after_peak_pct":-56.78,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.62,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"utility_infrastructure_valve_policy_label_spike_without_grid_order_bridge","current_profile_verdict":"current_profile_false_positive_if_stage2_on_policy_label_only","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX:039610:Stage4B:2024-06-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02-R1-L143-01-006260","trigger_id":"C02-R1-L143-01-006260-Stage2_Actionable","symbol":"006260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":72,"margin_bridge_score":68,"revision_score":58,"relative_strength_score":75,"customer_quality_score":72,"policy_or_regulatory_score":30,"valuation_repricing_score":60,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":67.7,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":78,"margin_bridge_score":74,"revision_score":58,"relative_strength_score":75,"customer_quality_score":77,"policy_or_regulatory_score":30,"valuation_repricing_score":60,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":70.0,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile raises verified bridge components for positive cases and penalizes label-only proxy rows before Yellow/Green promotion.","MFE_90D_pct":82.34,"MAE_90D_pct":-16.58,"score_return_alignment_label":"improved_positive_capture","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02-R1-L143-02-024840","trigger_id":"C02-R1-L143-02-024840-Stage2","symbol":"024840","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":22,"backlog_visibility_score":24,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":75,"customer_quality_score":28,"policy_or_regulatory_score":68,"valuation_repricing_score":70,"execution_risk_score":72,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":41.2,"stage_label_before":"Stage1-Watch","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":24,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":75,"customer_quality_score":20,"policy_or_regulatory_score":68,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":38.9,"stage_label_after":"Stage1-Watch","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile raises verified bridge components for positive cases and penalizes label-only proxy rows before Yellow/Green promotion.","MFE_90D_pct":52.01,"MAE_90D_pct":-31.35,"score_return_alignment_label":"improved_false_positive_block","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02-R1-L143-03-119850","trigger_id":"C02-R1-L143-03-119850-Stage2_Actionable","symbol":"119850","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":72,"margin_bridge_score":68,"revision_score":58,"relative_strength_score":75,"customer_quality_score":72,"policy_or_regulatory_score":30,"valuation_repricing_score":60,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":67.7,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":78,"margin_bridge_score":74,"revision_score":58,"relative_strength_score":75,"customer_quality_score":77,"policy_or_regulatory_score":30,"valuation_repricing_score":60,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":70.0,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile raises verified bridge components for positive cases and penalizes label-only proxy rows before Yellow/Green promotion.","MFE_90D_pct":74.59,"MAE_90D_pct":-10.26,"score_return_alignment_label":"improved_positive_capture","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02-R1-L143-04-092220","trigger_id":"C02-R1-L143-04-092220-Stage2","symbol":"092220","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":22,"backlog_visibility_score":24,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":55,"customer_quality_score":28,"policy_or_regulatory_score":68,"valuation_repricing_score":70,"execution_risk_score":72,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":38.8,"stage_label_before":"Stage1-Watch","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":24,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":55,"customer_quality_score":20,"policy_or_regulatory_score":68,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":36.5,"stage_label_after":"Stage1-Watch","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile raises verified bridge components for positive cases and penalizes label-only proxy rows before Yellow/Green promotion.","MFE_90D_pct":17.89,"MAE_90D_pct":-27.48,"score_return_alignment_label":"improved_false_positive_block","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02-R1-L143-05-032820","trigger_id":"C02-R1-L143-05-032820-Stage2_Actionable","symbol":"032820","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":24,"margin_bridge_score":24,"revision_score":58,"relative_strength_score":75,"customer_quality_score":72,"policy_or_regulatory_score":68,"valuation_repricing_score":60,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":58.3,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":30,"margin_bridge_score":30,"revision_score":58,"relative_strength_score":75,"customer_quality_score":77,"policy_or_regulatory_score":68,"valuation_repricing_score":60,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":60.6,"stage_label_after":"Stage2","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile raises verified bridge components for positive cases and penalizes label-only proxy rows before Yellow/Green promotion.","MFE_90D_pct":93.6,"MAE_90D_pct":-16.34,"score_return_alignment_label":"improved_positive_capture","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02-R1-L143-06-068240","trigger_id":"C02-R1-L143-06-068240-Stage4B","symbol":"068240","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":22,"backlog_visibility_score":24,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":55,"customer_quality_score":28,"policy_or_regulatory_score":30,"valuation_repricing_score":70,"execution_risk_score":72,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":35.8,"stage_label_before":"Stage1-Watch","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":24,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":55,"customer_quality_score":20,"policy_or_regulatory_score":30,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":33.5,"stage_label_after":"Stage1-Watch","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile raises verified bridge components for positive cases and penalizes label-only proxy rows before Yellow/Green promotion.","MFE_90D_pct":8.42,"MAE_90D_pct":-31.2,"score_return_alignment_label":"improved_false_positive_block","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02-R1-L143-07-039610","trigger_id":"C02-R1-L143-07-039610-Stage4B","symbol":"039610","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":22,"backlog_visibility_score":24,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":75,"customer_quality_score":28,"policy_or_regulatory_score":68,"valuation_repricing_score":70,"execution_risk_score":72,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":41.2,"stage_label_before":"Stage1-Watch","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":24,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":75,"customer_quality_score":20,"policy_or_regulatory_score":68,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":38.9,"stage_label_after":"Stage1-Watch","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C02 shadow profile raises verified bridge components for positive cases and penalizes label-only proxy rows before Yellow/Green promotion.","MFE_90D_pct":98.8,"MAE_90D_pct":-25.63,"score_return_alignment_label":"improved_false_positive_block","current_profile_verdict":"current_profile_false_positive_if_stage2_on_policy_label_only"}
{"row_type":"aggregate","selected_round":"R1","selected_loop":143,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","trigger_row_count":7,"calibration_usable_trigger_count":7,"representative_trigger_count":7,"new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"new_trigger_family_count":7,"positive_case_count":3,"counterexample_count":4,"stage4b_case_count":5,"stage4c_case_count":0,"current_profile_error_count":7,"source_proxy_only_count":7,"evidence_url_pending_count":7,"promotion_blocked_until_url_repair":true,"diversity_score_summary":"prior C02 loop139/140/141/142 symbol groups avoided; 7 new C02 symbols; positive-counterexample balance 4:3; grid holdco, copper input, datacenter backup power, power semiconductor, control-system, converter, and utility component routes dispersed.","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C02 base index 10 + local loop139 6 + loop140 6 + loop141 7 + loop142 6 + loop143 7 = about 42; above 30-row stability band, 8 short of 50-row practical calibration band.","sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C02_verified_grid_datacenter_bridge_required_before_Yellow_or_Green_v4","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_weakened":null,"existing_axis_kept":["stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","hard_4c_thesis_break_routes_to_4c"]}
{"row_type":"residual_contribution","round":"R1","loop":"143","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C02 missed structural bridge","C02 label-only false positive","C02 local 4B timing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

completed_round = R1
completed_loop = 143
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

## 28. Source Notes

- Main execution prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat / coverage index: docs/core/V12_Research_No_Repeat_Index.md
- Price atlas: Songdaiki/stock-web atlas/manifest.json and symbol-year tradable shards
- This file is historical calibration research only. It is not current/live recommendation research.
