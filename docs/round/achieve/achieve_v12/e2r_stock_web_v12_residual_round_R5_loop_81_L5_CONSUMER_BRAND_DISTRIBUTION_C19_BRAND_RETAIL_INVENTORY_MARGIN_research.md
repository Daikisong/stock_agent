# E2R Stock-Web v12 Residual Research — R5 Loop 81 / L5 / C19

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 81,
  "computed_next_round": "R6",
  "computed_next_loop": 81,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "brand_retail_inventory_margin_guardrail",
    "department_mart_convenience_inventory_margin_bridge",
    "retail_valueup_theme_fade_boundary",
    "bounded_recovery_no_forced4C_guard",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
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

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R4 / loop 81.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 81
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
computed_next_round = R6
computed_next_loop = 81
```

R5 was routed to C19 because loop 80 R5 used C20.  
This file tests department-store / mart / convenience-store inventory and margin bridges rather than beauty/global distribution.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C19 concentration in:

```text
UNKNOWN_SYMBOL, 036620, 298540, 383220, 337930
```

This run uses three different symbols:

```text
023530 / 롯데쇼핑 / department-store retail value-up inventory margin lifecycle
139480 / 이마트 / mart inventory and restructuring margin fade
282330 / BGF리테일 / convenience-store recovery no-hard-4C boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C19 is not “유통주 value-up이 올랐다.”

The mechanism must pass through:

```text
retail value-up / restructuring / channel recovery headline
→ inventory turnover or same-store sales
→ channel mix and cost control
→ revenue recovery
→ margin bridge
→ durable rerating
```

리테일 마진은 매장의 조명이 아니라 창고와 계산대의 호흡이다.  
C19가 보려는 것은 headline이 실제 재고 회전, 객단가, 비용 통제, 매출, 마진으로 반복되는지다.

---

## Case 1 — Retail margin lifecycle candidate: 023530 / 롯데쇼핑

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is retail value-up, inventory turnover, cost control, channel mix, revenue recovery and margin bridge evidence.

```text
evidence_family = DEPARTMENT_STORE_RETAIL_VALUEUP_INVENTORY_TURNOVER_COST_CONTROL_REVENUE_MARGIN_BRIDGE
case_role = positive_retail_margin_valueup_candidate_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 81,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/023/023530/2024.csv`:

```text
2024-02-01,81200,86500,81200,86000
2024-02-08,91200,92000,89100,90100
2024-02-13,90800,92100,82700,83200
2024-03-13,74200,74200,71500,72600
2024-04-05,71100,72000,70900,71300
2024-08-05,63000,63100,58100,58300
2024-09-05,62100,64400,61700,63600
2024-10-31,65200,66000,64200,66000
```

### Backtest

```text
MFE_30D  = +13.30%
MAE_30D  = -11.95%
MFE_90D  = +13.30%
MAE_90D  = -12.19%
MFE_180D = +13.30%
MAE_180D = -28.45%
peak_180 = 92,000 on 2024-02-08
trough_180 = 58,100 on 2024-08-05
peak_to_later_drawdown = -36.85%
```

### Interpretation

This is a C19 lifecycle candidate, not durable Green.  
The initial value-up / retail margin move was tradable, but the later MAE path requires bridge refresh.

Correct treatment:

```text
verified inventory turnover / cost control / revenue / margin bridge → Stage2-Yellow possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 139480 / 이마트

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests mart retail restructuring / value-up beta without enough inventory cleanup, channel mix and margin bridge.

```text
evidence_family = MART_RETAIL_VALUEUP_ONLINE_OFFLINE_RESTRUCTURING_INVENTORY_MARGIN_BRIDGE_WEAK
case_role = counterexample_mart_inventory_margin_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 76,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/139/139480/2024.csv`:

```text
2024-02-01,76100,81100,76000,79100
2024-02-02,79900,88500,79400,87400
2024-02-26,75200,75300,72500,73100
2024-04-08,65100,65100,63400,63500
2024-08-05,61200,61300,55400,56700
2024-09-05,63600,65800,63300,65300
2024-10-31,64600,65300,63600,65300
```

### Backtest

```text
MFE_30D  = +16.29%
MAE_30D  = -4.73%
MFE_90D  = +16.29%
MAE_90D  = -16.82%
MFE_180D = +16.29%
MAE_180D = -27.20%
peak_180 = 88,500 on 2024-02-02
trough_180 = 55,400 on 2024-08-05
peak_to_later_drawdown = -37.40%
```

### Interpretation

This is a C19 retail restructuring false-positive boundary.  
The early spike did not validate durable inventory/margin rerating.

Correct treatment:

```text
mart / retail restructuring theme beta
→ no verified inventory cleanup / channel mix / margin bridge
→ local 4B-watch
```

---

## Case 3 — Recovery / no-hard-4C boundary: 282330 / BGF리테일

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests convenience-store recovery with incomplete durable rerating bridge.

```text
evidence_family = CONVENIENCE_STORE_RETAIL_SAME_STORE_SALES_MIX_COST_CONTROL_MARGIN_WITH_RECOVERY_BUT_WEAK_RERATING_BRIDGE
case_role = overbearish_counterexample_recovery_no_hard4c_no_durable_stage2
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 139,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv`:

```text
2024-02-01,139200,143100,139100,140800
2024-03-07,131400,131400,121500,122500
2024-03-25,118100,118100,116700,117000
2024-07-24,101600,103800,101000,102700
2024-08-05,112400,114500,107000,109500
2024-09-25,123500,125000,119800,119800
2024-10-31,114100,116700,111800,115700
```

### Backtest

```text
MFE_30D  = +2.80%
MAE_30D  = -12.79%
MFE_90D  = +2.80%
MAE_90D  = -16.31%
MFE_180D = +2.80%
MAE_180D = -27.44%
peak_180 = 143,100 on 2024-02-01
trough_180 = 101,000 on 2024-07-24
peak_to_later_drawdown = -29.42%
later_recovery_high = 125,000 on 2024-09-25
```

### Interpretation

This is not durable Stage2, but it is also not hard 4C.  
There was recovery evidence after the low, so the correct result is RiskWatch/local-4B caution rather than a confirmed business-break label.

Correct treatment:

```text
convenience-store recovery watch
→ no durable Stage2 without SSSG / mix / cost-control / margin bridge
→ no hard 4C without confirmed non-price demand or margin break
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
inventory_margin_bridge_required = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
recovery_no_hard4c_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C19_retail_valueup_weight = true
do_not_treat_all_retail_MFE_as_Green = true
do_not_convert_retail_drawdown_to_hard_4C_without_non_price_inventory_demand_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE
```

This fine archetype covers:

```text
1. department-store value-up / inventory margin bridge → Stage2-Yellow possible after source repair
2. mart restructuring beta without margin bridge → false Stage2 / local 4B
3. convenience-store recovery without hard break → RiskWatch / no durable Stage2 / no hard 4C
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L81-C19-023530-LOTTE-SHOPPING-RETAIL-MARGIN-VALUEUP-LIFECYCLE", "symbol": "023530", "company_name": "롯데쇼핑", "round": "R5", "loop": "81", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-DepartmentRetailInventoryMarginValueupBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should allow department-store/retail positives only when value-up or channel recovery maps to inventory turnover, cost control, revenue mix and margin bridge. Lotte Shopping had a tradable early MFE but later high MAE, so it is lifecycle-managed rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy inventory turnover, same-store sales, channel mix, cost control, revenue recovery and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L81-C19-139480-EMART-MART-INVENTORY-MARGIN-FADE", "symbol": "139480", "company_name": "이마트", "round": "R5", "loop": "81", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / MartRetailInventoryMarginBridgeFadeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should not treat mart/value-up or retail restructuring beta as durable Stage2 unless inventory cleanup, online/offline mix, cost control, revenue recovery and margin bridge are visible. E-Mart had a sharp early MFE and then a high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy inventory turnover, same-store sales, channel mix, cost control, revenue recovery and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L81-C19-282330-BGF-RETAIL-CONVENIENCE-MARGIN-BOUNDED-RECOVERY", "symbol": "282330", "company_name": "BGF리테일", "round": "R5", "loop": "81", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-ConvenienceRetailMarginRecoveryNoDurableStage2NoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should not call bounded convenience-store recovery hard 4C when no non-price margin or demand break is confirmed, but it also should not mark durable Stage2 without same-store sales, mix, cost control and margin bridge. BGF Retail is a RiskWatch/no-hard-4C boundary.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy inventory turnover, same-store sales, channel mix, cost control, revenue recovery and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L81-C19-023530-LOTTE-SHOPPING-RETAIL-MARGIN-VALUEUP-LIFECYCLE", "case_id": "R5L81-C19-023530-LOTTE-SHOPPING-RETAIL-MARGIN-VALUEUP-LIFECYCLE", "symbol": "023530", "company_name": "롯데쇼핑", "round": "R5", "loop": "81", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "Stage2-Lifecycle-DepartmentRetailInventoryMarginValueupBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 81200.0, "evidence_available_at_that_date": "DEPARTMENT_STORE_RETAIL_VALUEUP_INVENTORY_TURNOVER_COST_CONTROL_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_SHOPPING_2024_RETAIL_VALUEUP_INVENTORY_TURNOVER_COST_CONTROL_MARGIN_BRIDGE", "stage2_evidence_fields": ["inventory_turnover_or_channel_mix_candidate", "cost_control_or_same_store_sales_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "valueup_or_restructuring_candidate"], "stage4b_evidence_fields": ["retail_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/023/023530/2024.csv", "profile_path": "atlas/symbol_profiles/023/023530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.3, "MFE_90D_pct": 13.3, "MFE_180D_pct": 13.3, "MAE_30D_pct": -11.95, "MAE_90D_pct": -12.19, "MAE_180D_pct": -28.45, "peak_date": "2024-02-08", "peak_price": 92000.0, "drawdown_after_peak_pct": -36.85, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_inventory_margin_peak_if_SSSG_channel_mix_cost_control_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_inventory_overhang_demand_break_margin_collapse_financing_or_control_break", "trigger_outcome_label": "positive_retail_margin_valueup_candidate_with_later_4b_watch", "current_profile_verdict": "C19 should allow department-store/retail positives only when value-up or channel recovery maps to inventory turnover, cost control, revenue mix and margin bridge. Lotte Shopping had a tradable early MFE but later high MAE, so it is lifecycle-managed rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C19_RETAIL_INVENTORY_MARGIN_023530_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L81-C19-139480-EMART-MART-INVENTORY-MARGIN-FADE", "case_id": "R5L81-C19-139480-EMART-MART-INVENTORY-MARGIN-FADE", "symbol": "139480", "company_name": "이마트", "round": "R5", "loop": "81", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "Stage2-FalsePositive / MartRetailInventoryMarginBridgeFadeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 76100.0, "evidence_available_at_that_date": "MART_RETAIL_VALUEUP_ONLINE_OFFLINE_RESTRUCTURING_INVENTORY_MARGIN_BRIDGE_WEAK", "evidence_source": "source_proxy_manual_verification_required:EMART_2024_RETAIL_RESTRUCTURING_INVENTORY_COST_CONTROL_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["inventory_turnover_or_channel_mix_candidate", "cost_control_or_same_store_sales_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "valueup_or_restructuring_candidate"], "stage4b_evidence_fields": ["retail_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/139/139480/2024.csv", "profile_path": "atlas/symbol_profiles/139/139480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.29, "MFE_90D_pct": 16.29, "MFE_180D_pct": 16.29, "MAE_30D_pct": -4.73, "MAE_90D_pct": -16.82, "MAE_180D_pct": -27.2, "peak_date": "2024-02-02", "peak_price": 88500.0, "drawdown_after_peak_pct": -37.4, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_inventory_margin_peak_if_SSSG_channel_mix_cost_control_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_inventory_overhang_demand_break_margin_collapse_financing_or_control_break", "trigger_outcome_label": "counterexample_mart_inventory_margin_local4b", "current_profile_verdict": "C19 should not treat mart/value-up or retail restructuring beta as durable Stage2 unless inventory cleanup, online/offline mix, cost control, revenue recovery and margin bridge are visible. E-Mart had a sharp early MFE and then a high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C19_RETAIL_INVENTORY_MARGIN_139480_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L81-C19-282330-BGF-RETAIL-CONVENIENCE-MARGIN-BOUNDED-RECOVERY", "case_id": "R5L81-C19-282330-BGF-RETAIL-CONVENIENCE-MARGIN-BOUNDED-RECOVERY", "symbol": "282330", "company_name": "BGF리테일", "round": "R5", "loop": "81", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "RiskWatch-ConvenienceRetailMarginRecoveryNoDurableStage2NoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 139200.0, "evidence_available_at_that_date": "CONVENIENCE_STORE_RETAIL_SAME_STORE_SALES_MIX_COST_CONTROL_MARGIN_WITH_RECOVERY_BUT_WEAK_RERATING_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:BGF_RETAIL_2024_CONVENIENCE_STORE_SSSG_MIX_COST_CONTROL_MARGIN_BRIDGE", "stage2_evidence_fields": ["inventory_turnover_or_channel_mix_candidate", "cost_control_or_same_store_sales_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "valueup_or_restructuring_candidate"], "stage4b_evidence_fields": ["retail_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv", "profile_path": "atlas/symbol_profiles/282/282330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.8, "MFE_90D_pct": 2.8, "MFE_180D_pct": 2.8, "MAE_30D_pct": -12.79, "MAE_90D_pct": -16.31, "MAE_180D_pct": -27.44, "peak_date": "2024-02-01", "peak_price": 143100.0, "drawdown_after_peak_pct": -29.42, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_inventory_margin_peak_if_SSSG_channel_mix_cost_control_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_inventory_overhang_demand_break_margin_collapse_financing_or_control_break", "trigger_outcome_label": "overbearish_counterexample_recovery_no_hard4c_no_durable_stage2", "current_profile_verdict": "C19 should not call bounded convenience-store recovery hard 4C when no non-price margin or demand break is confirmed, but it also should not mark durable Stage2 without same-store sales, mix, cost control and margin bridge. BGF Retail is a RiskWatch/no-hard-4C boundary.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C19_RETAIL_INVENTORY_MARGIN_282330_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L81-C19-023530-LOTTE-SHOPPING-RETAIL-MARGIN-VALUEUP-LIFECYCLE", "trigger_id": "TRG_R5L81-C19-023530-LOTTE-SHOPPING-RETAIL-MARGIN-VALUEUP-LIFECYCLE", "symbol": "023530", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_turnover_score": 13, "same_store_or_channel_mix_score": 13, "cost_control_score": 12, "revenue_recovery_score": 12, "margin_bridge_score": 13, "relative_strength_score": 9, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"inventory_turnover_score": 15, "same_store_or_channel_mix_score": 15, "cost_control_score": 14, "revenue_recovery_score": 14, "margin_bridge_score": 15, "relative_strength_score": 8, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["inventory_turnover_score", "same_store_or_channel_mix_score", "cost_control_score", "revenue_recovery_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory turnover, same-store sales/channel mix, cost control, revenue recovery and margin bridge; cap retail value-up theme beta when bridge fails to refresh while preserving recovery/no-hard-4C rows from overblocking.", "MFE_90D_pct": 13.3, "MAE_90D_pct": -12.19, "score_return_alignment_label": "retail_inventory_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C19 should allow department-store/retail positives only when value-up or channel recovery maps to inventory turnover, cost control, revenue mix and margin bridge. Lotte Shopping had a tradable early MFE but later high MAE, so it is lifecycle-managed rather than durable Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L81-C19-139480-EMART-MART-INVENTORY-MARGIN-FADE", "trigger_id": "TRG_R5L81-C19-139480-EMART-MART-INVENTORY-MARGIN-FADE", "symbol": "139480", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_turnover_score": 4, "same_store_or_channel_mix_score": 3, "cost_control_score": 2, "revenue_recovery_score": 2, "margin_bridge_score": 1, "relative_strength_score": 9, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"inventory_turnover_score": 3, "same_store_or_channel_mix_score": 1, "cost_control_score": 1, "revenue_recovery_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["inventory_turnover_score", "same_store_or_channel_mix_score", "cost_control_score", "revenue_recovery_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory turnover, same-store sales/channel mix, cost control, revenue recovery and margin bridge; cap retail value-up theme beta when bridge fails to refresh while preserving recovery/no-hard-4C rows from overblocking.", "MFE_90D_pct": 16.29, "MAE_90D_pct": -16.82, "score_return_alignment_label": "false_positive_retail_inventory_bridge_gap", "current_profile_verdict": "C19 should not treat mart/value-up or retail restructuring beta as durable Stage2 unless inventory cleanup, online/offline mix, cost control, revenue recovery and margin bridge are visible. E-Mart had a sharp early MFE and then a high-MAE fade."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L81-C19-282330-BGF-RETAIL-CONVENIENCE-MARGIN-BOUNDED-RECOVERY", "trigger_id": "TRG_R5L81-C19-282330-BGF-RETAIL-CONVENIENCE-MARGIN-BOUNDED-RECOVERY", "symbol": "282330", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_turnover_score": 7, "same_store_or_channel_mix_score": 7, "cost_control_score": 6, "revenue_recovery_score": 5, "margin_bridge_score": 5, "relative_strength_score": 3, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"inventory_turnover_score": 6, "same_store_or_channel_mix_score": 6, "cost_control_score": 5, "revenue_recovery_score": 4, "margin_bridge_score": 4, "relative_strength_score": 4, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / no durable Stage2 and no hard 4C", "changed_components": ["inventory_turnover_score", "same_store_or_channel_mix_score", "cost_control_score", "revenue_recovery_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory turnover, same-store sales/channel mix, cost control, revenue recovery and margin bridge; cap retail value-up theme beta when bridge fails to refresh while preserving recovery/no-hard-4C rows from overblocking.", "MFE_90D_pct": 2.8, "MAE_90D_pct": -16.31, "score_return_alignment_label": "recovery_no_hard4c_retail_boundary", "current_profile_verdict": "C19 should not call bounded convenience-store recovery hard 4C when no non-price margin or demand break is confirmed, but it also should not mark durable Stage2 without same-store sales, mix, cost control and margin bridge. BGF Retail is a RiskWatch/no-hard-4C boundary."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 81, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_MART_CONVENIENCE_RETAIL_INVENTORY_MARGIN_VALUEUP_BRIDGE_VS_RETAIL_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C19 retail/inventory-margin symbols outside top-covered 036620/298540/383220/337930 set, +3 department/mart/convenience trigger families, +1 retail margin lifecycle candidate, +1 mart local-4B counterexample, +1 convenience recovery no-hard-4C boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 81, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "axis": "department_mart_convenience_retail_inventory_margin_valueup_bridge_vs_retail_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C19 should split verified retail inventory/margin and channel-mix rerating from generic retail value-up/restructuring beta. Stage2 requires inventory turnover, same-store sales or channel mix, cost control, revenue recovery and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Recovery/no-hard-4C rows should not be converted to hard 4C without non-price demand/margin break evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["023530", "139480", "282330"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 81, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "existing_axis_strengthened": ["stage2_required_bridge", "inventory_margin_bridge_required", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "recovery_no_hard4c_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C19 needs retail inventory turnover, same-store sales/channel mix, cost control, revenue recovery and margin proof. Lotte Shopping is a lifecycle candidate after source repair; E-Mart shows retail restructuring beta fading into local 4B; BGF Retail shows a recovery/no-hard-4C boundary where durable Stage2 is not validated but hard 4C is too harsh."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
023530:
  name = 롯데쇼핑
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

139480:
  name = 이마트
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

282330:
  name = BGF리테일
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C19 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C19 retail inventory/margin rule-shape discovery,
but coding-agent promotion requires non-proxy inventory turnover, same-store sales, channel mix, cost control, revenue recovery and margin bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R5/C19 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
department_mart_convenience_retail_inventory_margin_valueup_bridge_vs_retail_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 023530, 139480 and 282330.
4. Keep generic C19 retail/inventory-margin weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - retail value-up / restructuring / channel recovery premise is explicit,
   - inventory turnover or same-store sales is visible,
   - channel mix and cost control are visible,
   - revenue recovery and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is retail value-up/restructuring theme beta only,
   - inventory/channel/cost/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price inventory overhang, demand break, margin collapse, financing or control break.
8. Emit before/after diagnostics and reject if verified retail margin positives or recovery/no-hard-4C rows are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 81
next_round = R6
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

