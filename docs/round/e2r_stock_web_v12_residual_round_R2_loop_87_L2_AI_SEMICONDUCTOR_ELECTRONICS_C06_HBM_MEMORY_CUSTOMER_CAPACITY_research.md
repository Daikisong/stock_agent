# E2R Stock-Web v12 Residual Research — R2 Loop 87 / L2 / C06

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 87,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 87,
  "computed_next_round": "R3",
  "computed_next_loop": 87,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "fine_archetype_id": "MEMORY_HBM_HOLDCO_ADVANCED_PACKAGE_SUBSTRATE_MATERIAL_CUSTOMER_CAPACITY_BRIDGE_VS_MATERIAL_THEME_FADE",
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 87
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
computed_next_round = R3
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R2 loop87 moves to C06 because recent R2 runs covered C07/C08 equipment and test-socket routes. C06 is the memory-customer / HBM-capacity route.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
C06 top-covered symbols = 000660 / 005930 / UNKNOWN_SYMBOL / 007660 / 222800 / 353200
selected_loop87_symbols = 402340 / 009150 / 014680
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 402340 | SK스퀘어 | `atlas/symbol_profiles/402/402340.json` | no profile-level CA candidate |
| 009150 | 삼성전기 | `atlas/symbol_profiles/009/009150.json` | old CA candidates through 1999; selected 2024 window clean |
| 014680 | 한솔케미칼 | `atlas/symbol_profiles/014/014680.json` | old CA candidates through 1999; selected 2024 window clean |

## 5. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R2L87-C06-01 | 402340 | SK스퀘어 | Stage2-Actionable | 2024-02-13 | 65,700 | 65.91 | -7.31 | current_profile_partially_correct_local_4B_watch_needed |
| R2L87-C06-02 | 009150 | 삼성전기 | Stage2-Actionable | 2024-02-13 | 139,200 | 26.8 | -9.48 | current_profile_partially_correct_package_customer_margin_watch_needed |
| R2L87-C06-03 | 014680 | 한솔케미칼 | Stage2-FalsePositive | 2024-02-13 | 183,200 | 16.81 | -36.52 | current_profile_false_positive_high_MAE_material_theme |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_HOLDCO_DIRECT_MEMORY_CAPACITY_PROXY | keep Stage2 with local 4B watch only if direct earnings-through bridge is source-repaired |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | ADVANCED_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY | keep Stage2 with customer/order/capacity/margin bridge watch |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | MEMORY_MATERIAL_THEME_HIGH_MAE_FADE | reject material-cycle MFE without customer volume, utilization and margin conversion |

## 7. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C06 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: HBM/customer capacity plan, customer mix, packaging/substrate demand, utilization, ASP/mix, earnings-through and gross/OP margin bridge.

## 8. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 402340 | `atlas/ohlcv_tradable_by_symbol_year/402/402340/2024.csv` | `atlas/symbol_profiles/402/402340.json` |
| 009150 | `atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv` | `atlas/symbol_profiles/009/009150.json` |
| 014680 | `atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv` | `atlas/symbol_profiles/014/014680.json` |

## 9. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 402340 | 65,700 | 23.29 | -7.31 | 31.66 | -7.31 | 65.91 | -7.31 | 2024-07-11 / 109,000 | -37.71 |
| 009150 | 139,200 | 7.76 | -5.82 | 26.80 | -5.82 | 26.80 | -9.48 | 2024-07-17 / 176,500 | -28.61 |
| 014680 | 183,200 | 16.81 | -7.59 | 16.81 | -9.33 | 16.81 | -36.52 | 2024-03-21 / 214,000 | -45.70 |

## 10. Case-by-Case Trigger Grid

### Case 1 — 402340 / SK스퀘어

C06 HBM/memory capacity holdco proxy positive with local 4B watch. The February entry produced a large MFE into July. However, holdco rerating is not direct memory-capacity proof, so it needs earnings-through, NAV-discount and direct beneficiary bridge repair.

### Case 2 — 009150 / 삼성전기

C06 advanced package/substrate customer-capacity positive with margin watch. The February entry produced a moderate MFE into July, but still requires HBM/AI-server customer mapping, utilization, ASP/mix and margin bridge before clean Green.

### Case 3 — 014680 / 한솔케미칼

C06 memory-material theme false positive. The March MFE faded into a deep MAE by September. Material-cycle rebound should not validate C06 unless customer volume, utilization, ASP/cost spread and margin conversion are explicit.

## 11. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C06, the residual is whether HBM/memory MFE becomes clean Stage2/Green before direct customer capacity, ASP/mix, utilization and earnings-through bridge are proven.

## 12. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R2L87-C06-01 | 0.82 | 0.72 | local 4B watch after holdco memory MFE if direct earnings bridge stalls |
| R2L87-C06-02 | 0.72 | 0.62 | package/substrate MFE allowed only with customer-capacity margin watch |
| R2L87-C06-03 | 0.35 | 0.30 | memory-material theme rejected without customer utilization and margin bridge |

## 13. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_customer_capacity_or_margin_break
hard_4c_price_only_allowed = false
```

## 14. Sector / Canonical Rule Candidate

```text
rule_scope = no_new_global_rule
canonical_archetype_rule_candidate = C06_HBM_memory_direct_customer_capacity_ASP_margin_bridge_required
confidence = low
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 25.09 | -7.49 | may over-credit proxy/material-cycle HBM MFE | needs C06 customer-capacity bridge repair |
| P1 canonical shadow bridge profile | 3 | keeps 402340/009150 with watch | demotes 014680 | better alignment, source repair required |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | canonical rule |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | MEMORY_HBM_HOLDCO_ADVANCED_PACKAGE_SUBSTRATE_MATERIAL_CUSTOMER_CAPACITY_BRIDGE_VS_MATERIAL_THEME_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 1 | yes |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - HBM_proxy_without_direct_customer_capacity_bridge
  - memory_material_theme_false_positive_high_MAE
  - source_proxy_runtime_promotion_risk
  - local_4B_late_after_memory_MFE
new_axis_proposed: false
existing_axis_strengthened:
  - C06_HBM_memory_direct_customer_capacity_ASP_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
do_not_propose_new_weight_delta: true
```

## 18. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- direct HBM customer capacity source
- utilization / ASP / mix source
- earnings-through and margin conversion
- production scoring implementation
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_HBM_memory_direct_customer_capacity_ASP_margin_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Require direct customer mapping, capacity utilization, ASP/mix, earnings-through and gross/OP margin conversion before clean Stage2/Green","keeps 402340/009150 with local 4B/customer-capacity watch; demotes 014680","R2L87-C06-01-S2A-20240213|R2L87-C06-02-S2A-20240213|R2L87-C06-03-S2FP-20240213",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 20. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L87-C06-01", "symbol": "402340", "company_name": "SK스퀘어", "round": "R2", "loop": 87, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "MEMORY_HBM_HOLDCO_ADVANCED_PACKAGE_SUBSTRATE_MATERIAL_CUSTOMER_CAPACITY_BRIDGE_VS_MATERIAL_THEME_FADE", "positive_or_counterexample": "positive", "best_trigger": "R2L87-C06-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM_memory_capacity_holdco_MFE_positive_but_local_4B_and_direct_memory_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C06 holdco/proxy positives need direct memory-capacity beneficiary mapping, customer mix, earnings-through bridge and valuation-discount bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R2L87-C06-01-S2A-20240213", "case_id": "R2L87-C06-01", "symbol": "402340", "company_name": "SK스퀘어", "round": "R2", "loop": 87, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "MEMORY_HBM_HOLDCO_ADVANCED_PACKAGE_SUBSTRATE_MATERIAL_CUSTOMER_CAPACITY_BRIDGE_VS_MATERIAL_THEME_FADE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "source_proxy_only HBM/memory customer capacity, package substrate or material cycle evidence; primary customer/capacity/margin URLs pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["HBM_customer_capacity_proxy", "memory_cycle_proxy", "relative_strength_proxy"], "stage3_evidence_fields": ["direct_customer_mapping", "capacity_utilization", "ASP_or_mix", "earnings_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["memory_MFE_without_customer_capacity_bridge", "post_peak_drawdown", "source_proxy_gap"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/402/402340/2024.csv", "profile_path": "atlas/symbol_profiles/402/402340.json", "entry_date": "2024-02-13", "entry_price": 65700, "MFE_30D_pct": 23.29, "MAE_30D_pct": -7.31, "MFE_90D_pct": 31.66, "MAE_90D_pct": -7.31, "MFE_180D_pct": 65.91, "MAE_180D_pct": -7.31, "peak_date": "2024-07-11", "peak_price": 109000, "drawdown_after_peak_pct": -37.71, "four_b_timing_verdict": "local_4B/watch after memory-capacity MFE if direct customer/capacity/margin bridge stalls", "four_c_protection_label": "hard_4C_requires_non_price_customer_capacity_or_margin_break", "trigger_outcome_label": "HBM_memory_capacity_holdco_MFE_positive_but_local_4B_and_direct_memory_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "calibration_usable": true, "forward_window_trading_days": 180, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L87-C06-01", "trigger_id": "R2L87-C06-01-S2A-20240213", "symbol": "402340", "raw_component_scores_before": {"HBM_customer_capacity_score": 45, "direct_customer_mapping_score": 35, "capacity_utilization_score": 40, "ASP_or_mix_score": 35, "earnings_through_score": 35, "gross_margin_bridge_score": 35, "relative_strength_score": 70, "valuation_blowoff_risk_score": 70, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"HBM_customer_capacity_score": 45, "direct_customer_mapping_score": 35, "capacity_utilization_score": 40, "ASP_or_mix_score": 35, "earnings_through_score": 35, "gross_margin_bridge_score": 35, "relative_strength_score": 70, "valuation_blowoff_risk_score": 82, "source_quality_score": 10, "4B_watch_score": 85}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/customer-capacity bridge watch", "changed_components": ["direct_customer_mapping_score", "capacity_utilization_score", "ASP_or_mix_score", "earnings_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C06 requires HBM/memory capacity signal to convert into direct customer mapping, capacity utilization, ASP/mix, earnings-through and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 31.66, "MAE_90D_pct": -7.31, "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R2L87-C06-02", "symbol": "009150", "company_name": "삼성전기", "round": "R2", "loop": 87, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "MEMORY_HBM_HOLDCO_ADVANCED_PACKAGE_SUBSTRATE_MATERIAL_CUSTOMER_CAPACITY_BRIDGE_VS_MATERIAL_THEME_FADE", "positive_or_counterexample": "positive", "best_trigger": "R2L87-C06-02-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "score_price_alignment": "advanced_package_customer_capacity_MFE_positive_but_customer_order_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_package_customer_margin_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C06 package/substrate positives need HBM or AI-server customer mapping, capacity utilization, ASP/mix and margin conversion before clean Green."}
{"row_type": "trigger", "trigger_id": "R2L87-C06-02-S2A-20240213", "case_id": "R2L87-C06-02", "symbol": "009150", "company_name": "삼성전기", "round": "R2", "loop": 87, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "MEMORY_HBM_HOLDCO_ADVANCED_PACKAGE_SUBSTRATE_MATERIAL_CUSTOMER_CAPACITY_BRIDGE_VS_MATERIAL_THEME_FADE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "source_proxy_only HBM/memory customer capacity, package substrate or material cycle evidence; primary customer/capacity/margin URLs pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["HBM_customer_capacity_proxy", "memory_cycle_proxy", "relative_strength_proxy"], "stage3_evidence_fields": ["direct_customer_mapping", "capacity_utilization", "ASP_or_mix", "earnings_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["memory_MFE_without_customer_capacity_bridge", "post_peak_drawdown", "source_proxy_gap"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv", "profile_path": "atlas/symbol_profiles/009/009150.json", "entry_date": "2024-02-13", "entry_price": 139200, "MFE_30D_pct": 7.76, "MAE_30D_pct": -5.82, "MFE_90D_pct": 26.8, "MAE_90D_pct": -5.82, "MFE_180D_pct": 26.8, "MAE_180D_pct": -9.48, "peak_date": "2024-07-17", "peak_price": 176500, "drawdown_after_peak_pct": -28.61, "four_b_timing_verdict": "local_4B/watch after memory-capacity MFE if direct customer/capacity/margin bridge stalls", "four_c_protection_label": "hard_4C_requires_non_price_customer_capacity_or_margin_break", "trigger_outcome_label": "advanced_package_customer_capacity_MFE_positive_but_customer_order_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_package_customer_margin_watch_needed", "corporate_action_window_status": "clean_2024_window_after_old_1999_CA_candidate", "calibration_usable": true, "forward_window_trading_days": 180, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L87-C06-02", "trigger_id": "R2L87-C06-02-S2A-20240213", "symbol": "009150", "raw_component_scores_before": {"HBM_customer_capacity_score": 45, "direct_customer_mapping_score": 35, "capacity_utilization_score": 40, "ASP_or_mix_score": 35, "earnings_through_score": 35, "gross_margin_bridge_score": 35, "relative_strength_score": 70, "valuation_blowoff_risk_score": 70, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"HBM_customer_capacity_score": 45, "direct_customer_mapping_score": 35, "capacity_utilization_score": 40, "ASP_or_mix_score": 35, "earnings_through_score": 35, "gross_margin_bridge_score": 35, "relative_strength_score": 70, "valuation_blowoff_risk_score": 82, "source_quality_score": 10, "4B_watch_score": 85}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/customer-capacity bridge watch", "changed_components": ["direct_customer_mapping_score", "capacity_utilization_score", "ASP_or_mix_score", "earnings_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C06 requires HBM/memory capacity signal to convert into direct customer mapping, capacity utilization, ASP/mix, earnings-through and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 26.8, "MAE_90D_pct": -5.82, "current_profile_verdict": "current_profile_partially_correct_package_customer_margin_watch_needed"}
{"row_type": "case", "case_id": "R2L87-C06-03", "symbol": "014680", "company_name": "한솔케미칼", "round": "R2", "loop": 87, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "MEMORY_HBM_HOLDCO_ADVANCED_PACKAGE_SUBSTRATE_MATERIAL_CUSTOMER_CAPACITY_BRIDGE_VS_MATERIAL_THEME_FADE", "positive_or_counterexample": "counterexample", "best_trigger": "R2L87-C06-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "score_price_alignment": "memory_material_MFE_then_deep_MAE_customer_capacity_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_material_theme", "price_source": "Songdaiki/stock-web", "notes": "Memory-material capacity rebound should remain RiskWatch unless customer volume, utilization, ASP/cost spread and margin conversion are source-repaired."}
{"row_type": "trigger", "trigger_id": "R2L87-C06-03-S2FP-20240213", "case_id": "R2L87-C06-03", "symbol": "014680", "company_name": "한솔케미칼", "round": "R2", "loop": 87, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "MEMORY_HBM_HOLDCO_ADVANCED_PACKAGE_SUBSTRATE_MATERIAL_CUSTOMER_CAPACITY_BRIDGE_VS_MATERIAL_THEME_FADE", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "source_proxy_only HBM/memory customer capacity, package substrate or material cycle evidence; primary customer/capacity/margin URLs pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["HBM_customer_capacity_proxy", "memory_cycle_proxy", "relative_strength_proxy"], "stage3_evidence_fields": ["direct_customer_mapping", "capacity_utilization", "ASP_or_mix", "earnings_through", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["memory_MFE_without_customer_capacity_bridge", "post_peak_drawdown", "source_proxy_gap"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv", "profile_path": "atlas/symbol_profiles/014/014680.json", "entry_date": "2024-02-13", "entry_price": 183200, "MFE_30D_pct": 16.81, "MAE_30D_pct": -7.59, "MFE_90D_pct": 16.81, "MAE_90D_pct": -9.33, "MFE_180D_pct": 16.81, "MAE_180D_pct": -36.52, "peak_date": "2024-03-21", "peak_price": 214000, "drawdown_after_peak_pct": -45.7, "four_b_timing_verdict": "local_4B/watch after memory-capacity MFE if direct customer/capacity/margin bridge stalls", "four_c_protection_label": "hard_4C_requires_non_price_customer_capacity_or_margin_break", "trigger_outcome_label": "memory_material_MFE_then_deep_MAE_customer_capacity_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_material_theme", "corporate_action_window_status": "clean_2024_window_after_old_1999_CA_candidate", "calibration_usable": true, "forward_window_trading_days": 180, "is_new_independent_case": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L87-C06-03", "trigger_id": "R2L87-C06-03-S2FP-20240213", "symbol": "014680", "raw_component_scores_before": {"HBM_customer_capacity_score": 20, "direct_customer_mapping_score": 5, "capacity_utilization_score": 10, "ASP_or_mix_score": 5, "earnings_through_score": 5, "gross_margin_bridge_score": 5, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "source_quality_score": 15, "4B_watch_score": 80}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"HBM_customer_capacity_score": 20, "direct_customer_mapping_score": 0, "capacity_utilization_score": 0, "ASP_or_mix_score": 0, "earnings_through_score": 0, "gross_margin_bridge_score": 0, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "source_quality_score": 5, "4B_watch_score": 92}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Memory-material theme RiskWatch", "changed_components": ["direct_customer_mapping_score", "capacity_utilization_score", "ASP_or_mix_score", "earnings_through_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score"], "component_delta_explanation": "C06 requires HBM/memory capacity signal to convert into direct customer mapping, capacity utilization, ASP/mix, earnings-through and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 16.81, "MAE_90D_pct": -9.33, "current_profile_verdict": "current_profile_false_positive_high_MAE_material_theme"}
{"row_type": "shadow_weight", "axis": "C06_HBM_memory_direct_customer_capacity_ASP_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "HBM/memory-capacity rerating requires direct customer mapping, capacity utilization, ASP/mix, earnings-through and gross/OP margin conversion; proxy or material-cycle MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 402340/009150 with local 4B/customer-capacity watch; demotes 014680 high-MAE memory-material theme false positive", "trigger_ids": "R2L87-C06-01-S2A-20240213|R2L87-C06-02-S2A-20240213|R2L87-C06-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R2", "loop": 87, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["HBM_proxy_without_direct_customer_capacity_bridge", "memory_material_theme_false_positive_high_MAE", "source_proxy_runtime_promotion_risk", "local_4B_late_after_memory_MFE"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 21. Deferred Coding Agent Handoff Prompt

Use only `calibration_usable=true` rows. Do not treat `source_proxy_only/evidence_url_pending` rows as runtime promotion-ready. For C06, test a canonical guard requiring direct customer mapping, capacity utilization, ASP/mix, earnings-through and margin conversion before clean Stage2/Green.

## 22. Next Round State

```text
completed_round = R2
completed_loop = 87
next_round = R3
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
