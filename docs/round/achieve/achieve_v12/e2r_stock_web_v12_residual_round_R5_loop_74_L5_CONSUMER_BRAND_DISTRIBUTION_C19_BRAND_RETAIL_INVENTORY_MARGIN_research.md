# E2R Stock-Web v12 Residual Research — R5 Loop 74 / L5 / C19

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 74,
  "computed_next_round": "R6",
  "computed_next_loop": 74,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
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

Previous completed state in this interactive run: R4 / loop 74.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 74
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
computed_next_round = R6
computed_next_loop = 74
```

R5 was routed to C19 because C20 is already heavily covered and loop 73 had used C18.  
This file tests offline retail value-up, department-store traffic/margin, and grocery inventory-turnaround beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C19 is concentrated in:

```text
UNKNOWN_SYMBOL, 036620, 298540, 383220, 337930
```

This run uses three different symbols:

```text
069960 / 현대백화점 / department-store value-up traffic margin bridge
004170 / 신세계 / department-store margin RiskWatch boundary
139480 / 이마트 / grocery retail turnaround price beta
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate.
```

## Research thesis

C19 is not “retail stock went up.”

The mechanism is:

```text
retail traffic / inventory discipline / duty-free or online loss improvement
→ margin conversion
→ value-up or valuation rerating
→ durable price path
```

A store can be full and still not profitable.  
C19 cares whether the checkout line turns into margin.

---

## Case 1 — Positive slow bridge: 069960 / 현대백화점

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is department-store traffic, inventory discipline, duty-free recovery, low-PBR/value-up and margin bridge evidence.

```text
evidence_family = DEPARTMENT_STORE_VALUEUP_LOW_PBR_TRAFFIC_DUTYFREE_INVENTORY_MARGIN_BRIDGE
case_role = positive_slow_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 53,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/069/069960/2024.csv`:

```text
2024-02-01,53700,58400,53500,58100
2024-02-07,58800,61900,57000,59100
2024-06-19,48750,48750,48050,48050
2024-08-05,47850,48000,44050,45100
```

### Backtest

```text
MFE_30D  = +15.27%
MAE_30D  = -6.52%
MFE_90D  = +15.27%
MAE_90D  = -10.52%
MFE_180D = +15.27%
MAE_180D = -17.97%
peak_180 = 61,900 on 2024-02-07
trough_180 = 44,050 on 2024-08-05
peak_to_later_drawdown = -28.84%
```

### Interpretation

This is a C19 positive-slow anchor.  
The path had controlled drawdown relative to other retail names, and the first rerating was not immediately erased. But it should still not become Green without non-price traffic, inventory, duty-free or margin evidence.

---

## Case 2 — RiskWatch boundary: 004170 / 신세계

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is department-store traffic, duty-free recovery, margin and inventory bridge evidence.

```text
evidence_family = DEPARTMENT_STORE_DUTYFREE_TRAFFIC_MARGIN_VALUEUP_WITH_WEAK_SUSTAINED_BRIDGE
case_role = riskwatch_boundary_case
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 170,900
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv`:

```text
2024-02-01,170900,179200,170900,178600
2024-02-19,184400,190300,183200,189500
2024-08-05,151600,152100,138800,142100
2024-09-27,160900,164600,160000,162300
```

### Backtest

```text
MFE_30D  = +11.35%
MAE_30D  = -4.51%
MFE_90D  = +11.35%
MAE_90D  = -12.52%
MFE_180D = +11.35%
MAE_180D = -18.78%
peak_180 = 190,300 on 2024-02-19
trough_180 = 138,800 on 2024-08-05
peak_to_later_drawdown = -27.06%
```

### Interpretation

This is not a hard negative.  
It is a boundary case. Shinsegae's first value-up move was tradable, but without stronger sustained duty-free/traffic/margin evidence it should stay RiskWatch rather than durable Green.

---

## Case 3 — Counterexample / local 4B: 139480 / 이마트

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests grocery retail turnaround and value-up price beta without enough visible inventory/margin bridge.

```text
evidence_family = GROCERY_RETAIL_TURNAROUND_VALUEUP_PRICE_BETA_WITH_WEAK_INVENTORY_MARGIN_BRIDGE
case_role = counterexample_with_later_recovery_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 76,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/139/139480/2024.csv`:

```text
2024-02-01,76100,81100,76000,79100
2024-02-02,79900,88500,79400,87400
2024-08-05,61200,61300,55400,56700
2024-12-26,71600,75500,69900,75500
```

### Backtest

```text
MFE_30D  = +16.29%
MAE_30D  = -9.20%
MFE_90D  = +16.29%
MAE_90D  = -16.95%
MFE_180D = +16.29%
MAE_180D = -27.20%
peak_180 = 88,500 on 2024-02-02
trough_180 = 55,400 on 2024-08-05
peak_to_later_drawdown = -37.40%
```

### Interpretation

This is the C19 false-positive path with later recovery watch.

The early value-up/grocery turnaround move was real, but not durable enough to be Green. The later December recovery means it should not be hard 4C. The correct treatment is local 4B-watch until inventory, online-loss and store-margin evidence refreshes.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C19_retail_valueup_weight = true
do_not_treat_all_low_PBR_retail_beta_as_Green = true
do_not_convert_retail_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA
```

This fine archetype covers:

```text
1. department-store traffic / duty-free / margin bridge → Stage2 possible after source repair
2. department-store value-up with weak sustained evidence → RiskWatch boundary
3. grocery retail turnaround price beta without margin refresh → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN", "symbol": "069960", "company_name": "현대백화점", "round": "R5", "loop": "74", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-DepartmentStoreValueupMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should allow Stage2 only when low-PBR/value-up retail attention connects to traffic, inventory discipline, duty-free recovery or margin conversion. Hyundai Department Store produced a controlled-MAE positive path, but later drawdown still needs local 4B-watch if the margin bridge stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy traffic, inventory, value-up, duty-free, online-loss and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH", "symbol": "004170", "company_name": "신세계", "round": "R5", "loop": "74", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "riskwatch_boundary", "best_trigger": "Stage2-RiskWatch / DepartmentStoreMarginBridgeWeak", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should distinguish stable department-store value-up from durable inventory/margin rerating. Shinsegae had early MFE but later MAE opened and the return path was not strong enough to qualify as durable Green without stronger traffic/duty-free/margin evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy traffic, inventory, value-up, duty-free, online-loss and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA", "symbol": "139480", "company_name": "이마트", "round": "R5", "loop": "74", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / GroceryTurnaroundPriceBetaLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should not treat grocery retail/value-up price beta as durable Stage2 unless inventory turns, SSG/online losses, store traffic and margin bridge improve. E-Mart had early MFE but then opened deep MAE and a large post-peak drawdown, so the first signal should be local 4B-watch rather than Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy traffic, inventory, value-up, duty-free, online-loss and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN", "case_id": "R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN", "symbol": "069960", "company_name": "현대백화점", "round": "R5", "loop": "74", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-DepartmentStoreValueupMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 53700.0, "evidence_available_at_that_date": "DEPARTMENT_STORE_VALUEUP_LOW_PBR_TRAFFIC_DUTYFREE_INVENTORY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_DEPARTMENT_STORE_2024_VALUEUP_TRAFFIC_DUTYFREE_INVENTORY_MARGIN_BRIDGE", "stage2_evidence_fields": ["retail_valueup", "traffic_or_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "store_traffic_or_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/069/069960/2024.csv", "profile_path": "atlas/symbol_profiles/069/069960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.27, "MFE_90D_pct": 15.27, "MFE_180D_pct": 15.27, "MAE_30D_pct": -6.52, "MAE_90D_pct": -10.52, "MAE_180D_pct": -17.97, "peak_date": "2024-02-07", "peak_price": 61900.0, "drawdown_after_peak_pct": -28.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_valueup_or_inventory_margin_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_inventory_margin_or_traffic_break", "trigger_outcome_label": "positive_slow_with_later_4b_watch", "current_profile_verdict": "C19 should allow Stage2 only when low-PBR/value-up retail attention connects to traffic, inventory discipline, duty-free recovery or margin conversion. Hyundai Department Store produced a controlled-MAE positive path, but later drawdown still needs local 4B-watch if the margin bridge stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "share_count_change_inside_window": false, "same_entry_group_id": "C19_RETAIL_MARGIN_069960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH", "case_id": "R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH", "symbol": "004170", "company_name": "신세계", "round": "R5", "loop": "74", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-RiskWatch / DepartmentStoreMarginBridgeWeak", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 170900.0, "evidence_available_at_that_date": "DEPARTMENT_STORE_DUTYFREE_TRAFFIC_MARGIN_VALUEUP_WITH_WEAK_SUSTAINED_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SHINSEGAE_2024_DEPARTMENT_STORE_DUTYFREE_TRAFFIC_MARGIN_VALUEUP_BRIDGE", "stage2_evidence_fields": ["retail_valueup", "traffic_or_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "store_traffic_or_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv", "profile_path": "atlas/symbol_profiles/004/004170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.35, "MFE_90D_pct": 11.35, "MFE_180D_pct": 11.35, "MAE_30D_pct": -4.51, "MAE_90D_pct": -12.52, "MAE_180D_pct": -18.78, "peak_date": "2024-02-19", "peak_price": 190300.0, "drawdown_after_peak_pct": -27.06, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_valueup_or_inventory_margin_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_inventory_margin_or_traffic_break", "trigger_outcome_label": "riskwatch_boundary_case", "current_profile_verdict": "C19 should distinguish stable department-store value-up from durable inventory/margin rerating. Shinsegae had early MFE but later MAE opened and the return path was not strong enough to qualify as durable Green without stronger traffic/duty-free/margin evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "share_count_change_inside_window": false, "same_entry_group_id": "C19_RETAIL_MARGIN_004170_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA", "case_id": "R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA", "symbol": "139480", "company_name": "이마트", "round": "R5", "loop": "74", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / GroceryTurnaroundPriceBetaLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 76100.0, "evidence_available_at_that_date": "GROCERY_RETAIL_TURNAROUND_VALUEUP_PRICE_BETA_WITH_WEAK_INVENTORY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:EMART_2024_GROCERY_RETAIL_TURNAROUND_INVENTORY_MARGIN_ONLINE_LOSS_BRIDGE", "stage2_evidence_fields": ["retail_valueup", "traffic_or_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "store_traffic_or_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/139/139480/2024.csv", "profile_path": "atlas/symbol_profiles/139/139480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.29, "MFE_90D_pct": 16.29, "MFE_180D_pct": 16.29, "MAE_30D_pct": -9.2, "MAE_90D_pct": -16.95, "MAE_180D_pct": -27.2, "peak_date": "2024-02-02", "peak_price": 88500.0, "drawdown_after_peak_pct": -37.4, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_valueup_or_inventory_margin_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_inventory_margin_or_traffic_break", "trigger_outcome_label": "counterexample_with_later_recovery_watch", "current_profile_verdict": "C19 should not treat grocery retail/value-up price beta as durable Stage2 unless inventory turns, SSG/online losses, store traffic and margin bridge improve. E-Mart had early MFE but then opened deep MAE and a large post-peak drawdown, so the first signal should be local 4B-watch rather than Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "share_count_change_inside_window": false, "same_entry_group_id": "C19_RETAIL_MARGIN_139480_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN", "trigger_id": "TRG_R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN", "symbol": "069960", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"traffic_or_same_store_score": 10, "inventory_turn_score": 9, "margin_bridge_score": 12, "online_or_dutyfree_loss_bridge_score": 9, "capital_return_or_valueup_score": 12, "relative_strength_score": 11, "valuation_repricing_score": 12, "execution_risk_score": 5, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"traffic_or_same_store_score": 12, "inventory_turn_score": 11, "margin_bridge_score": 14, "online_or_dutyfree_loss_bridge_score": 10, "capital_return_or_valueup_score": 9, "relative_strength_score": 10, "valuation_repricing_score": 10, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["margin_bridge_score", "inventory_turn_score", "execution_risk_score", "capital_return_or_valueup_score"], "component_delta_explanation": "Reward only verified traffic/inventory/margin conversion; cap low-PBR or retail value-up price beta when store traffic, duty-free, online losses or inventory evidence fails to refresh.", "MFE_90D_pct": 15.27, "MAE_90D_pct": -10.52, "score_return_alignment_label": "aligned_positive_slow", "current_profile_verdict": "C19 should allow Stage2 only when low-PBR/value-up retail attention connects to traffic, inventory discipline, duty-free recovery or margin conversion. Hyundai Department Store produced a controlled-MAE positive path, but later drawdown still needs local 4B-watch if the margin bridge stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH", "trigger_id": "TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH", "symbol": "004170", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"traffic_or_same_store_score": 4, "inventory_turn_score": 4, "margin_bridge_score": 4, "online_or_dutyfree_loss_bridge_score": 9, "capital_return_or_valueup_score": 12, "relative_strength_score": 11, "valuation_repricing_score": 12, "execution_risk_score": 14, "source_confidence_score": 2}, "weighted_score_before": 62, "stage_label_before": "RiskWatch / no durable Green", "raw_component_scores_after": {"traffic_or_same_store_score": 3, "inventory_turn_score": 3, "margin_bridge_score": 2, "online_or_dutyfree_loss_bridge_score": 10, "capital_return_or_valueup_score": 9, "relative_strength_score": 10, "valuation_repricing_score": 10, "execution_risk_score": 17, "source_confidence_score": 2}, "weighted_score_after": 56, "stage_label_after": "RiskWatch / no durable Green", "changed_components": ["margin_bridge_score", "inventory_turn_score", "execution_risk_score", "capital_return_or_valueup_score"], "component_delta_explanation": "Reward only verified traffic/inventory/margin conversion; cap low-PBR or retail value-up price beta when store traffic, duty-free, online losses or inventory evidence fails to refresh.", "MFE_90D_pct": 11.35, "MAE_90D_pct": -12.52, "score_return_alignment_label": "riskwatch_boundary", "current_profile_verdict": "C19 should distinguish stable department-store value-up from durable inventory/margin rerating. Shinsegae had early MFE but later MAE opened and the return path was not strong enough to qualify as durable Green without stronger traffic/duty-free/margin evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA", "trigger_id": "TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA", "symbol": "139480", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"traffic_or_same_store_score": 4, "inventory_turn_score": 4, "margin_bridge_score": 4, "online_or_dutyfree_loss_bridge_score": 3, "capital_return_or_valueup_score": 12, "relative_strength_score": 8, "valuation_repricing_score": 12, "execution_risk_score": 14, "source_confidence_score": 2}, "weighted_score_before": 55, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"traffic_or_same_store_score": 3, "inventory_turn_score": 3, "margin_bridge_score": 2, "online_or_dutyfree_loss_bridge_score": 2, "capital_return_or_valueup_score": 9, "relative_strength_score": 5, "valuation_repricing_score": 10, "execution_risk_score": 17, "source_confidence_score": 2}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["margin_bridge_score", "inventory_turn_score", "execution_risk_score", "capital_return_or_valueup_score"], "component_delta_explanation": "Reward only verified traffic/inventory/margin conversion; cap low-PBR or retail value-up price beta when store traffic, duty-free, online losses or inventory evidence fails to refresh.", "MFE_90D_pct": 16.29, "MAE_90D_pct": -16.95, "score_return_alignment_label": "false_positive_retail_valueup_bridge_gap", "current_profile_verdict": "C19 should not treat grocery retail/value-up price beta as durable Stage2 unless inventory turns, SSG/online losses, store traffic and margin bridge improve. E-Mart had early MFE but then opened deep MAE and a large post-peak drawdown, so the first signal should be local 4B-watch rather than Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 74, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 2, "positive_case_count": 1, "counterexample_count": 1, "riskwatch_boundary_case_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C19 department/grocery retail symbols, +2 value-up/inventory-margin trigger families, +1 controlled-MAE department-store positive, +1 riskwatch boundary, +1 grocery value-up false-positive, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 74, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "axis": "department_store_valueup_traffic_margin_vs_grocery_turnaround_price_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C19 should split verified department-store traffic/inventory/margin bridge from retail value-up price beta. Stage2 requires traffic, inventory-turn, duty-free or online-loss improvement, margin conversion and controlled MAE. Grocery turnaround beta with post-peak drawdown should route to local 4B-watch unless non-price margin evidence refreshes.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["069960", "004170", "139480"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 74, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C19 needs retail margin proof. Hyundai Department Store is a controlled-MAE value-up/traffic positive; Shinsegae is a department-store RiskWatch boundary; E-Mart is a grocery retail value-up beta that opened local 4B risk before later recovery."}
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
069960:
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

004170:
  corporate_action_candidate_dates = 1996-01-03, 2004-12-22, 2011-02-01, 2011-02-25, 2011-06-10
  selected window = 2024-02-01~D+180
  contamination = false

139480:
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C19 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C19 rule-shape discovery,
but coding-agent promotion requires non-proxy traffic, inventory-turn, duty-free/online loss, value-up and margin evidence.
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
department_store_valueup_traffic_margin_vs_grocery_turnaround_price_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 069960, 004170 and 139480.
4. Keep generic C19 retail value-up weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - store traffic, same-store sales or duty-free/online-loss bridge is explicit,
   - inventory discipline or gross-margin recovery is visible,
   - value-up or capital-return evidence is not price-only,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is low-PBR retail/value-up beta only,
   - inventory or margin evidence is weak/stale,
   - MAE_90D <= -15~20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration in traffic, inventory, online losses, duty-free, liquidity or margin.
8. Emit before/after diagnostics and reject if verified department-store margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 74
next_round = R6
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

