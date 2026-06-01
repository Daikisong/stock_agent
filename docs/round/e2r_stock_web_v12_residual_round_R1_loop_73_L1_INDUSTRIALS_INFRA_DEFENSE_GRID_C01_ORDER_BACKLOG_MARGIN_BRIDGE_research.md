# E2R Stock-Web v12 Residual Research — R1 Loop 73 / L1 / C01

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 73,
  "computed_next_round": "R2",
  "computed_next_loop": 73,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION",
  "loop_objective": [
    "coverage_gap_fill",
    "residual_missed_structural_mining",
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
```

## Round / scope resolution

Previous completed state in this interactive run: R13 / loop 72.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 73
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
computed_next_round = R2
computed_next_loop = 73
```

R1 was routed to C01 because the current No-Repeat coverage table begins at C03 and does not yet show C01 as a populated coverage row.  
This is therefore a true R1 coverage-gap fill rather than another defense/nuclear rerun.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
329180 / HD현대중공업 / Stage2-Actionable-ShipbuildingBacklogMarginBridge / 2024-04-26
010620 / HD현대미포 / Stage2-Actionable-MidshipMarginRecovery / 2024-06-24
097230 / HJ중공업 / Stage2-FalsePositive / OrderBetaWeakMargin / 2024-06-03
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are marked source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C01 is not “orders are up.”

The true bridge is:

```text
order backlog
→ delivery-slot scarcity / high-value mix / customer quality
→ margin conversion
→ revision visibility
→ durable rerating
```

In shipbuilding, the dock is the factory and the calendar is the contract.  
A full dock only matters if the next vessels carry better margins, not just more steel.

The residual split is:

```text
C01 positive:
  LNG/naval/high-value backlog + delivery slot visibility + margin conversion + controlled MAE

C01 false positive:
  order or shipbuilding beta + weak margin conversion + later MAE/drawdown

C01 local 4B:
  backlog/order excitement fades before margin evidence refreshes
```

---

## Case 1 — Positive after source repair: 329180 / HD현대중공업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is LNG/naval backlog, delivery-slot visibility, high-value vessel mix, and margin conversion.

```text
evidence_family = SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_CONVERSION_BRIDGE
case_role = positive
trigger_date = 2024-04-25
entry_date = 2024-04-26
entry_price = 130,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv` and `2025.csv`:

```text
2024-04-26,130000,140600,129700,139500
2024-05-20,131300,131500,127200,128100
2024-07-26,184500,210000,183500,207500
2025-02-13,353000,371500,344000,366000
2025-03-28,274000,280000,272500,280000
```

### Backtest

```text
MFE_30D  = +12.31%
MAE_30D  = -2.15%
MFE_90D  = +61.54%
MAE_90D  = -2.15%
MFE_180D = +185.77%
MAE_180D = -2.15%
peak_180 = 371,500 on 2025-02-13
trough_180 = 127,200 on 2024-05-20
peak_to_later_drawdown = -26.65%
```

### Interpretation

This is the clean C01 structural success shape.  
The early MAE stayed small while MFE compounded. This supports a rule that lets Stage2 appear before the full price breakout if the backlog-to-margin bridge is verified.

But runtime promotion must wait for non-proxy evidence.

---

## Case 2 — Positive with later 4B-watch: 010620 / HD현대미포

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is mid-size vessel product mix, backlog recovery, and margin conversion.

```text
evidence_family = MID_SIZE_VESSEL_PRODUCT_MIX_BACKLOG_MARGIN_RECOVERY
case_role = positive_with_later_4b_watch
trigger_date = 2024-06-21
entry_date = 2024-06-24
entry_price = 80,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv` and `2025.csv`:

```text
2024-06-24,80500,87800,79900,86900
2024-07-26,106400,114900,105800,113200
2024-07-31,116500,122800,115600,117500
2025-01-21,132000,144300,130700,141800
2025-03-31,99500,107400,99500,105400
```

### Backtest

```text
MFE_30D  = +42.73%
MAE_30D  = -0.75%
MFE_90D  = +52.55%
MAE_90D  = -0.75%
MFE_180D = +79.25%
MAE_180D = -0.75%
peak_180 = 144,300 on 2025-01-21
trough_180 = 79,900 on 2024-06-24
peak_to_later_drawdown = -31.05%
```

### Interpretation

This is a strong positive route with a lifecycle caveat.  
The entry quality was good and early MAE was tiny. But after the peak, the drawdown opened enough that C01 should support a later local 4B-watch if the margin bridge stops refreshing.

The rule is not “shipbuilding always stays Green.”  
It is:

```text
backlog-to-margin bridge → Stage2/Green possible
later bridge stale + drawdown → local 4B-watch
```

---

## Case 3 — Counterexample: 097230 / HJ중공업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests order and sector beta without clear backlog quality or margin conversion.

```text
evidence_family = SHIPBUILDING_AND_CONSTRUCTION_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION
case_role = counterexample
trigger_date = 2024-06-03
entry_date = 2024-06-03
entry_price = 3,285
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv`:

```text
2024-06-03,3285,3570,3280,3460
2024-06-19,3480,3785,3290,3300
2024-08-05,3010,3100,2700,2790
2024-09-09,2670,2920,2585,2705
2024-10-31,2200,2330,2180,2290
```

### Backtest

```text
MFE_30D  = +15.22%
MAE_30D  = -7.76%
MFE_90D  = +15.22%
MAE_90D  = -21.31%
MFE_180D = +15.22%
MAE_180D = -33.64%
peak_180 = 3,785 on 2024-06-19
trough_180 = 2,180 on 2024-10-31
peak_to_later_drawdown = -42.40%
```

### Interpretation

This is the C01 false-positive shape.  
A small shipbuilding/order beta move is not enough. Without explicit backlog quality and margin conversion, the stock can give back the move and open local 4B risk.

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
do_not_raise_generic_C01_order_weight = true
do_not_treat_all_shipbuilding_order_beta_as_Green = true
do_not_convert_later_shipbuilding_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION
```

This fine archetype covers:

```text
1. LNG/naval/high-value backlog + margin conversion → Stage2/Green possible after source repair
2. mid-size vessel product mix and margin recovery → Stage2 possible, later local 4B if bridge fades
3. generic shipbuilding/construction order beta without margin proof → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE", "symbol": "329180", "company_name": "HD현대중공업", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "case_type": "shipbuilding_backlog_margin_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-ShipbuildingBacklogMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should allow Stage2 when shipbuilding backlog is not just order volume but connects to LNG/naval mix, rising newbuild prices and margin conversion. The stock-web path shows structural MFE with controlled early MAE, but source repair is needed before runtime weight promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web price path usable; non-proxy backlog/margin/order evidence must be attached before promotion."}
{"row_type": "case", "case_id": "R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE", "symbol": "010620", "company_name": "HD현대미포", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "case_type": "shipbuilding_backlog_margin_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-MidshipMarginRecovery", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should capture mid-size vessel backlog recovery when product mix and margin conversion are visible. But after the 2025 peak, a later local 4B-watch is needed if the margin bridge stops refreshing or drawdown opens.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web price path usable; non-proxy backlog/margin/order evidence must be attached before promotion."}
{"row_type": "case", "case_id": "R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION", "symbol": "097230", "company_name": "HJ중공업", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "case_type": "shipbuilding_backlog_margin_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / OrderBetaWeakMargin", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should not treat shipbuilding/construction order beta as Stage2 unless backlog quality and margin conversion are explicit. HJ Heavy produced a short MFE but later opened drawdown, making it a false Stage2 / local 4B-watch candidate.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web price path usable; non-proxy backlog/margin/order evidence must be attached before promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE", "case_id": "R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE", "symbol": "329180", "company_name": "HD현대중공업", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-ShipbuildingBacklogMarginBridge", "trigger_date": "2024-04-25", "entry_date": "2024-04-26", "entry_price": 130000.0, "evidence_available_at_that_date": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_CONVERSION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HD_HYUNDAI_HEAVY_INDUSTRIES_2024_LNG_NAVAL_BACKLOG_MARGIN_CONVERSION_BRIDGE", "stage2_evidence_fields": ["order_backlog", "margin_bridge_candidate", "shipbuilding_cycle"], "stage3_evidence_fields": ["relative_strength", "backlog_to_margin_conversion_candidate"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv", "profile_path": "atlas/symbol_profiles/329/329180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.31, "MFE_90D_pct": 61.54, "MFE_180D_pct": 185.77, "MAE_30D_pct": -2.15, "MAE_90D_pct": -2.15, "MAE_180D_pct": -2.15, "peak_date": "2025-02-13", "peak_price": 371500.0, "drawdown_after_peak_pct": -26.65, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_break", "trigger_outcome_label": "positive", "current_profile_verdict": "C01 should allow Stage2 when shipbuilding backlog is not just order volume but connects to LNG/naval mix, rising newbuild prices and margin conversion. The stock-web path shows structural MFE with controlled early MAE, but source repair is needed before runtime weight promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C01_SHIPBUILDING_329180_2024-04-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE", "case_id": "R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE", "symbol": "010620", "company_name": "HD현대미포", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-MidshipMarginRecovery", "trigger_date": "2024-06-21", "entry_date": "2024-06-24", "entry_price": 80500.0, "evidence_available_at_that_date": "MID_SIZE_VESSEL_PRODUCT_MIX_BACKLOG_MARGIN_RECOVERY", "evidence_source": "source_proxy_manual_verification_required:HD_HYUNDAI_MIPO_2024_MID_SIZE_VESSEL_PRODUCT_MIX_BACKLOG_MARGIN_RECOVERY", "stage2_evidence_fields": ["order_backlog", "margin_bridge_candidate", "shipbuilding_cycle"], "stage3_evidence_fields": ["relative_strength", "backlog_to_margin_conversion_candidate"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv", "profile_path": "atlas/symbol_profiles/010/010620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.73, "MFE_90D_pct": 52.55, "MFE_180D_pct": 79.25, "MAE_30D_pct": -0.75, "MAE_90D_pct": -0.75, "MAE_180D_pct": -0.75, "peak_date": "2025-01-21", "peak_price": 144300.0, "drawdown_after_peak_pct": -31.05, "green_lateness_ratio": null, "four_b_local_peak_proximity": "later_local_4b_after_peak", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C01 should capture mid-size vessel backlog recovery when product mix and margin conversion are visible. But after the 2025 peak, a later local 4B-watch is needed if the margin bridge stops refreshing or drawdown opens.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C01_SHIPBUILDING_010620_2024-06-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION", "case_id": "R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION", "symbol": "097230", "company_name": "HJ중공업", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / OrderBetaWeakMargin", "trigger_date": "2024-06-03", "entry_date": "2024-06-03", "entry_price": 3285.0, "evidence_available_at_that_date": "SHIPBUILDING_AND_CONSTRUCTION_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "evidence_source": "source_proxy_manual_verification_required:HJ_HEAVY_INDUSTRIES_2024_ORDER_BETA_WEAK_MARGIN_CONVERSION", "stage2_evidence_fields": ["order_backlog", "margin_bridge_candidate", "shipbuilding_cycle"], "stage3_evidence_fields": ["relative_strength", "backlog_to_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv", "profile_path": "atlas/symbol_profiles/097/097230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.22, "MFE_90D_pct": 15.22, "MFE_180D_pct": 15.22, "MAE_30D_pct": -7.76, "MAE_90D_pct": -21.31, "MAE_180D_pct": -33.64, "peak_date": "2024-06-19", "peak_price": 3785.0, "drawdown_after_peak_pct": -42.4, "green_lateness_ratio": null, "four_b_local_peak_proximity": "later_local_4b_after_peak", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_bridge_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C01 should not treat shipbuilding/construction order beta as Stage2 unless backlog quality and margin conversion are explicit. HJ Heavy produced a short MFE but later opened drawdown, making it a false Stage2 / local 4B-watch candidate.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C01_SHIPBUILDING_097230_2024-06-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE", "trigger_id": "TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE", "symbol": "329180", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 12, "margin_bridge_score": 12, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 14, "margin_bridge_score": 15, "revision_score": 11, "relative_strength_score": 14, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green candidate after source repair", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Raise only if verified backlog-to-margin evidence exists; cap when order beta lacks margin conversion.", "MFE_90D_pct": 61.54, "MAE_90D_pct": -2.15, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "C01 should allow Stage2 when shipbuilding backlog is not just order volume but connects to LNG/naval mix, rising newbuild prices and margin conversion. The stock-web path shows structural MFE with controlled early MAE, but source repair is needed before runtime weight promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE", "trigger_id": "TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE", "symbol": "010620", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 12, "margin_bridge_score": 12, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 14, "margin_bridge_score": 15, "revision_score": 11, "relative_strength_score": 14, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green candidate after source repair", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Raise only if verified backlog-to-margin evidence exists; cap when order beta lacks margin conversion.", "MFE_90D_pct": 52.55, "MAE_90D_pct": -0.75, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "C01 should capture mid-size vessel backlog recovery when product mix and margin conversion are visible. But after the 2025 peak, a later local 4B-watch is needed if the margin bridge stops refreshing or drawdown opens."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION", "trigger_id": "TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION", "symbol": "097230", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 6, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 56, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 45, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Raise only if verified backlog-to-margin evidence exists; cap when order beta lacks margin conversion.", "MFE_90D_pct": 15.22, "MAE_90D_pct": -21.31, "score_return_alignment_label": "false_positive_bridge_gap", "current_profile_verdict": "C01 should not treat shipbuilding/construction order beta as Stage2 unless backlog quality and margin conversion are explicit. HJ Heavy produced a short MFE but later opened drawdown, making it a false Stage2 / local 4B-watch candidate."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 73, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 2, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 C01 symbols, +2 shipbuilding backlog/margin trigger families, +2 structural positives, +1 weak-margin order-beta counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 73, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "axis": "shipbuilding_lng_naval_backlog_margin_bridge_vs_order_beta_weak_margin_conversion", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C01 should split verified backlog-to-margin conversion from simple order/basket beta. Stage2/Green requires backlog quality, delivery slot visibility, newbuild price/mix and margin conversion. Weak order beta with no margin bridge should be local 4B-watch when MAE/drawdown opens.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["329180", "010620", "097230"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 73, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C01 needs a shipbuilding-specific bridge: LNG/naval/high-value backlog and margin conversion can justify early Stage2, but order-volume beta without margin proof should be capped or routed to local 4B-watch."}
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
329180:
  corporate_action_candidate_dates = none
  selected window = 2024-04-26~D+180
  contamination = false

010620:
  corporate_action_candidate_dates = 1999-07-14, 2004-01-29, 2018-12-04, 2018-12-26
  selected window = 2024-06-24~D+180
  contamination = false

097230:
  corporate_action_candidate_dates = 2013-04-05, 2014-08-29, 2019-05-21, 2019-05-23
  selected window = 2024-06-03~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C01 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C01 rule-shape discovery,
but coding-agent promotion requires non-proxy order/backlog/margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C01 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
shipbuilding_lng_naval_backlog_margin_bridge_vs_order_beta_weak_margin_conversion

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 329180, 010620 and 097230.
4. Keep generic C01 order/backlog weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - backlog quality is explicitly evidenced,
   - delivery slots or orderbook visibility are strong,
   - customer/vessel mix supports margin conversion,
   - revision or margin bridge is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is order/shipbuilding beta only,
   - margin bridge is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if verified backlog-to-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 73
next_round = R2
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

