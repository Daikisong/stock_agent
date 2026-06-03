# E2R Stock-Web v12 Residual Research — R2 Loop 75 / L2 / C06

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 75,
  "computed_next_round": "R3",
  "computed_next_loop": 75,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
  "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE",
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

Previous completed state in this interactive run: R1 / loop 75.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 75
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
computed_next_round = R3
computed_next_loop = 75
```

R2 was routed to C06 because loop 74 used C07 and loop 73 used C08.  
C06 is thin and concentrated in memory-maker rows, so this file tests memory-adjacent AI server substrate and package-substrate bridge risk.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C06 is concentrated in:

```text
UNKNOWN_SYMBOL, 000660, 005930
```

This run uses three different symbols:

```text
007660 / 이수페타시스 / AI server memory-network substrate customer-capacity bridge
353200 / 대덕전자 / FC-BGA/package substrate beta fade
222800 / 심텍 / DDR5/HBM memory substrate cycle fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate.
```

## Research thesis

C06 is not only “memory maker went up.”

The mechanism can extend to suppliers only when:

```text
AI/HBM memory demand
→ customer capacity or order visibility
→ utilization / ASP / delivery slot
→ margin conversion
→ durable rerating
```

A substrate name is not automatically an HBM winner.  
The bridge is the customer-capacity ledger.

---

## Case 1 — Positive with lifecycle 4B: 007660 / 이수페타시스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is AI server/HBM-adjacent network PCB customer capacity, order visibility, utilization and margin bridge evidence.

```text
evidence_family = AI_SERVER_HBM_MEMORY_NETWORK_PCB_CUSTOMER_CAPACITY_ORDER_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-03-01
entry_date = 2024-03-04
entry_price = 31,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv`:

```text
2024-03-04,31350,37550,30650,36700
2024-03-28,43150,46500,42950,44900
2024-07-24,46050,49700,46050,47350
2024-08-05,36900,37700,30900,33250
2024-11-18,22250,22400,21000,21250
```

### Backtest

```text
MFE_30D  = +48.33%
MAE_30D  = -2.23%
MFE_90D  = +58.53%
MAE_90D  = -2.23%
MFE_180D = +58.53%
MAE_180D = -33.01%
peak_180 = 49,700 on 2024-07-24
trough_180 = 21,000 on 2024-11-18
peak_to_later_drawdown = -57.75%
```

### Interpretation

This is the C06 supplier positive.  
The price path supports a customer-capacity / AI server demand bridge, but the later drawdown says C06 needs lifecycle local 4B if order or margin evidence stops refreshing.

---

## Case 2 — Counterexample / local 4B: 353200 / 대덕전자

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests FC-BGA/package-substrate beta without enough customer-capacity and margin refresh.

```text
evidence_family = FCBGA_MEMORY_PACKAGE_SUBSTRATE_AI_BETA_WITH_WEAK_CUSTOMER_CAPACITY_MARGIN_REFRESH
case_role = counterexample
trigger_date = 2024-03-20
entry_date = 2024-03-21
entry_price = 24,250
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv`:

```text
2024-03-21,24250,24600,23900,24250
2024-04-02,27900,28050,26500,26900
2024-08-05,20400,20500,17500,18580
2024-10-25,16190,16320,15550,15820
```

### Backtest

```text
MFE_30D  = +15.67%
MAE_30D  = -8.87%
MFE_90D  = +15.67%
MAE_90D  = -13.20%
MFE_180D = +15.67%
MAE_180D = -35.88%
peak_180 = 28,050 on 2024-04-02
trough_180 = 15,550 on 2024-10-25
peak_to_later_drawdown = -44.56%
```

### Interpretation

This is not enough for durable C06.  
The MFE was modest and the later MAE was severe. Without customer capacity and margin evidence, this is local 4B-watch rather than Green.

---

## Case 3 — Counterexample / local 4B: 222800 / 심텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests DDR5/HBM memory-substrate restocking beta without durable customer/order/margin bridge.

```text
evidence_family = DDR5_HBM_MEMORY_SUBSTRATE_RESTOCKING_BETA_WITH_WEAK_CUSTOMER_ORDER_MARGIN_BRIDGE
case_role = counterexample
trigger_date = 2024-03-20
entry_date = 2024-03-21
entry_price = 30,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv`:

```text
2024-03-21,30100,31400,29800,31150
2024-04-02,33750,34450,32400,33000
2024-08-05,27200,27500,22950,23800
2024-10-25,16520,16520,15700,15880
```

### Backtest

```text
MFE_30D  = +14.45%
MAE_30D  = -6.31%
MFE_90D  = +14.45%
MAE_90D  = -12.13%
MFE_180D = +14.45%
MAE_180D = -47.84%
peak_180 = 34,450 on 2024-04-02
trough_180 = 15,700 on 2024-10-25
peak_to_later_drawdown = -54.43%
```

### Interpretation

This is the memory-substrate beta fade.  
The initial recovery was tradable, but it did not confirm durable C06 without customer/order/utilization and margin evidence.

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
do_not_raise_generic_C06_memory_supplier_weight = true
do_not_treat_all_memory_substrate_MFE_as_Green = true
do_not_convert_memory_supplier_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE
```

This fine archetype covers:

```text
1. AI server/HBM-adjacent customer-capacity bridge → Stage2 possible after source repair
2. FC-BGA/package substrate beta without customer-capacity refresh → false Stage2 / local 4B
3. DDR5/HBM memory substrate restocking beta without order/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY", "symbol": "007660", "company_name": "이수페타시스", "round": "R2", "loop": "75", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "case_type": "hbm_memory_customer_capacity", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AIServerMemorySubstrateCapacityBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C06 should not be limited to Samsung/SK Hynix memory makers. It should include AI server/HBM-adjacent memory-network substrate suppliers when customer capacity, order visibility and margin bridge are explicit. Isu Petasys produced strong MFE but later severe drawdown, so lifecycle local 4B is required if bridge evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer capacity, order, utilization, ASP/margin and AI/HBM memory demand evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE", "symbol": "353200", "company_name": "대덕전자", "round": "R2", "loop": "75", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "case_type": "hbm_memory_customer_capacity", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / PackageSubstrateBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C06 should not treat package substrate or AI memory-adjacent beta as durable Stage2 unless customer capacity, utilization, order or margin bridge refreshes. Daeduck Electronics produced limited MFE and then a severe 180D MAE path, making it a false Stage2/local 4B row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer capacity, order, utilization, ASP/margin and AI/HBM memory demand evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE", "symbol": "222800", "company_name": "심텍", "round": "R2", "loop": "75", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "case_type": "hbm_memory_customer_capacity", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / MemorySubstrateCycleFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C06 should not reward memory substrate restocking beta unless customer order, utilization, ASP or margin bridge is visible. Simmtech produced only moderate MFE and then a deep late-2024 drawdown, so it belongs in false Stage2/local 4B-watch until bridge evidence is repaired.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer capacity, order, utilization, ASP/margin and AI/HBM memory demand evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY", "case_id": "R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY", "symbol": "007660", "company_name": "이수페타시스", "round": "R2", "loop": "75", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-AIServerMemorySubstrateCapacityBridge", "trigger_date": "2024-03-01", "entry_date": "2024-03-04", "entry_price": 31350.0, "evidence_available_at_that_date": "AI_SERVER_HBM_MEMORY_NETWORK_PCB_CUSTOMER_CAPACITY_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ISU_PETASYS_2024_AI_SERVER_MEMORY_NETWORK_PCB_CUSTOMER_CAPACITY_ORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["AI_HBM_memory_demand_candidate", "customer_capacity_or_order_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv", "profile_path": "atlas/symbol_profiles/007/007660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 48.33, "MFE_90D_pct": 58.53, "MFE_180D_pct": 58.53, "MAE_30D_pct": -2.23, "MAE_90D_pct": -2.23, "MAE_180D_pct": -33.01, "peak_date": "2024-07-24", "peak_price": 49700.0, "drawdown_after_peak_pct": -57.75, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_memory_substrate_capacity_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_utilization_ASP_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C06 should not be limited to Samsung/SK Hynix memory makers. It should include AI server/HBM-adjacent memory-network substrate suppliers when customer capacity, order visibility and margin bridge are explicit. Isu Petasys produced strong MFE but later severe drawdown, so lifecycle local 4B is required if bridge evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C06_MEMORY_CAPACITY_007660_2024-03-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE", "case_id": "R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE", "symbol": "353200", "company_name": "대덕전자", "round": "R2", "loop": "75", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / PackageSubstrateBetaFade", "trigger_date": "2024-03-20", "entry_date": "2024-03-21", "entry_price": 24250.0, "evidence_available_at_that_date": "FCBGA_MEMORY_PACKAGE_SUBSTRATE_AI_BETA_WITH_WEAK_CUSTOMER_CAPACITY_MARGIN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:DAEDUCK_ELECTRONICS_2024_FCBGA_MEMORY_PACKAGE_SUBSTRATE_CUSTOMER_CAPACITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["AI_HBM_memory_demand_candidate", "customer_capacity_or_order_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv", "profile_path": "atlas/symbol_profiles/353/353200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.67, "MFE_90D_pct": 15.67, "MFE_180D_pct": 15.67, "MAE_30D_pct": -8.87, "MAE_90D_pct": -13.2, "MAE_180D_pct": -35.88, "peak_date": "2024-04-02", "peak_price": 28050.0, "drawdown_after_peak_pct": -44.56, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_memory_substrate_capacity_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_utilization_ASP_or_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C06 should not treat package substrate or AI memory-adjacent beta as durable Stage2 unless customer capacity, utilization, order or margin bridge refreshes. Daeduck Electronics produced limited MFE and then a severe 180D MAE path, making it a false Stage2/local 4B row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C06_MEMORY_CAPACITY_353200_2024-03-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE", "case_id": "R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE", "symbol": "222800", "company_name": "심텍", "round": "R2", "loop": "75", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / MemorySubstrateCycleFade", "trigger_date": "2024-03-20", "entry_date": "2024-03-21", "entry_price": 30100.0, "evidence_available_at_that_date": "DDR5_HBM_MEMORY_SUBSTRATE_RESTOCKING_BETA_WITH_WEAK_CUSTOMER_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SIMMTECH_2024_DDR5_HBM_MEMORY_SUBSTRATE_CUSTOMER_ORDER_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["AI_HBM_memory_demand_candidate", "customer_capacity_or_order_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv", "profile_path": "atlas/symbol_profiles/222/222800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.45, "MFE_90D_pct": 14.45, "MFE_180D_pct": 14.45, "MAE_30D_pct": -6.31, "MAE_90D_pct": -12.13, "MAE_180D_pct": -47.84, "peak_date": "2024-04-02", "peak_price": 34450.0, "drawdown_after_peak_pct": -54.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_memory_substrate_capacity_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_utilization_ASP_or_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C06 should not reward memory substrate restocking beta unless customer order, utilization, ASP or margin bridge is visible. Simmtech produced only moderate MFE and then a deep late-2024 drawdown, so it belongs in false Stage2/local 4B-watch until bridge evidence is repaired.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C06_MEMORY_CAPACITY_222800_2024-03-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY", "trigger_id": "TRG_R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY", "symbol": "007660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"customer_capacity_score": 13, "order_visibility_score": 12, "utilization_score": 12, "margin_bridge_score": 12, "relative_strength_score": 15, "customer_quality_score": 12, "valuation_repricing_score": 11, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_before": 83, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"customer_capacity_score": 15, "order_visibility_score": 14, "utilization_score": 13, "margin_bridge_score": 14, "relative_strength_score": 15, "customer_quality_score": 12, "valuation_repricing_score": 10, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["customer_capacity_score", "order_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified AI/HBM memory customer capacity, order, utilization and margin bridge; cap substrate beta when bridge evidence fails to refresh.", "MFE_90D_pct": 58.53, "MAE_90D_pct": -2.23, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C06 should not be limited to Samsung/SK Hynix memory makers. It should include AI server/HBM-adjacent memory-network substrate suppliers when customer capacity, order visibility and margin bridge are explicit. Isu Petasys produced strong MFE but later severe drawdown, so lifecycle local 4B is required if bridge evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE", "trigger_id": "TRG_R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE", "symbol": "353200", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"customer_capacity_score": 5, "order_visibility_score": 3, "utilization_score": 4, "margin_bridge_score": 2, "relative_strength_score": 7, "customer_quality_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 16, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_capacity_score": 3, "order_visibility_score": 2, "utilization_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "customer_quality_score": 3, "valuation_repricing_score": 4, "execution_risk_score": 19, "source_confidence_score": 2}, "weighted_score_after": 41, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_capacity_score", "order_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified AI/HBM memory customer capacity, order, utilization and margin bridge; cap substrate beta when bridge evidence fails to refresh.", "MFE_90D_pct": 15.67, "MAE_90D_pct": -13.2, "score_return_alignment_label": "false_positive_memory_substrate_bridge_gap", "current_profile_verdict": "C06 should not treat package substrate or AI memory-adjacent beta as durable Stage2 unless customer capacity, utilization, order or margin bridge refreshes. Daeduck Electronics produced limited MFE and then a severe 180D MAE path, making it a false Stage2/local 4B row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE", "trigger_id": "TRG_R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE", "symbol": "222800", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"customer_capacity_score": 5, "order_visibility_score": 3, "utilization_score": 4, "margin_bridge_score": 2, "relative_strength_score": 7, "customer_quality_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 16, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_capacity_score": 3, "order_visibility_score": 2, "utilization_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "customer_quality_score": 3, "valuation_repricing_score": 4, "execution_risk_score": 19, "source_confidence_score": 2}, "weighted_score_after": 41, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_capacity_score", "order_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified AI/HBM memory customer capacity, order, utilization and margin bridge; cap substrate beta when bridge evidence fails to refresh.", "MFE_90D_pct": 14.45, "MAE_90D_pct": -12.13, "score_return_alignment_label": "false_positive_memory_substrate_bridge_gap", "current_profile_verdict": "C06 should not reward memory substrate restocking beta unless customer order, utilization, ASP or margin bridge is visible. Simmtech produced only moderate MFE and then a deep late-2024 drawdown, so it belongs in false Stage2/local 4B-watch until bridge evidence is repaired."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 75, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C06 memory-adjacent symbols outside Samsung/SK Hynix, +3 AI server/package/memory substrate trigger families, +1 strong capacity-bridge positive, +2 substrate beta-fade counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 75, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "axis": "ai_server_memory_substrate_customer_capacity_bridge_vs_package_substrate_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C06 should split verified AI/HBM memory customer-capacity order bridges from generic package or memory substrate beta. Stage2 requires customer capacity, order visibility, utilization, ASP/margin or AI server memory demand evidence. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["007660", "353200", "222800"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 75, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C06 should extend beyond memory makers only if the supplier has customer-capacity/order bridge. Isu Petasys shows AI server memory-network substrate positive after source repair; Daeduck Electronics and Simmtech show package/memory substrate beta fading into local 4B when customer/order/margin bridge is absent."}
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
007660:
  corporate_action_candidate_dates = 2021-11-18
  selected window = 2024-03-04~D+180
  contamination = false

353200:
  corporate_action_candidate_dates = none
  selected window = 2024-03-21~D+180
  contamination = false

222800:
  corporate_action_candidate_dates = 2015-09-22, 2020-05-20
  selected window = 2024-03-21~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C06 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C06 rule-shape discovery,
but coding-agent promotion requires non-proxy AI/HBM memory customer capacity, order, utilization, ASP and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C06 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
ai_server_memory_substrate_customer_capacity_bridge_vs_package_substrate_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 007660, 353200 and 222800.
4. Keep generic C06 memory-supplier weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - AI/HBM memory demand is explicit,
   - customer capacity or order bridge is visible,
   - utilization, ASP or delivery-slot evidence is visible,
   - margin/revision bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is package/memory substrate beta only,
   - customer capacity or margin bridge is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, order cut, utilization collapse, ASP/margin break or financing evidence.
8. Emit before/after diagnostics and reject if verified AI server memory-substrate positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 75
next_round = R3
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

