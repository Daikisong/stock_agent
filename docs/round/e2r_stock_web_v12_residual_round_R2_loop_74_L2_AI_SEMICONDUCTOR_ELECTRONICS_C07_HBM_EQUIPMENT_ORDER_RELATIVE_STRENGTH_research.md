# E2R Stock-Web v12 Residual Research — R2 Loop 74 / L2 / C07

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 74,
  "computed_next_round": "R3",
  "computed_next_loop": 74,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE",
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
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R1 / loop 74.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 74
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
computed_next_round = R3
computed_next_loop = 74
```

R2 was routed to C07 because loop 73 had already filled C08, and C07 remains thin in the No-Repeat table.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C07 is concentrated in `042700`, `089030`, `039030`, `058470`, and `095340`.  
This run uses three different symbols:

```text
084370 / 유진테크 / front-end deposition equipment relative strength
036810 / 에프에스티 / EUV pellicle/chiller ancillary equipment relative strength
095610 / 테스 / equipment beta bridge fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C07 is not “semiconductor equipment stock went up.”

The correct mechanism is:

```text
AI/HBM or DRAM capex attention
→ named equipment order or customer adoption
→ backlog or delivery-slot visibility
→ margin/revision bridge
→ durable rerating
```

A hot equipment candle is a spark.  
A customer order is the circuit closing.

The residual split is:

```text
C07 positive:
  equipment order / customer adoption / backlog evidence
  + relative strength
  + controlled early MAE

C07 false positive:
  HBM equipment beta
  + no order/backlog/margin refresh
  + later MAE or post-peak drawdown

C07 local 4B:
  relative-strength peak fades before bridge evidence refreshes
```

---

## Case 1 — Positive with later 4B-watch: 084370 / 유진테크

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is front-end deposition equipment order, HBM/DRAM customer capex, backlog and margin bridge evidence.

```text
evidence_family = DRAM_HBM_FRONTEND_DEPOSITION_EQUIPMENT_ORDER_RELATIVE_STRENGTH_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-03-20
entry_date = 2024-03-21
entry_price = 37,750
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv`:

```text
2024-03-21,37750,41900,37400,41450
2024-04-24,50800,56600,50200,53000
2024-05-28,53800,60000,53600,56500
2024-12-02,33800,34450,31600,31850
```

### Backtest

```text
MFE_30D  = +49.93%
MAE_30D  = -0.93%
MFE_90D  = +58.94%
MAE_90D  = -0.93%
MFE_180D = +58.94%
MAE_180D = -16.29%
peak_180 = 60,000 on 2024-05-28
trough_180 = 31,600 on 2024-12-02
peak_to_later_drawdown = -47.33%
```

### Interpretation

This is a good C07 positive-shaped path.  
The early relative strength was real and MAE was small. But after the peak, the drawdown says the model needs a later local 4B-watch unless order/backlog/margin evidence refreshes.

---

## Case 2 — Positive with severe later 4B-watch: 036810 / 에프에스티

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is EUV pellicle/chiller or ancillary equipment customer adoption, order timing and margin bridge evidence.

```text
evidence_family = EUV_PELLICLE_CHILLER_ANCILLARY_EQUIPMENT_RELATIVE_STRENGTH_WITH_LATER_BRIDGE_FADE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-08
entry_date = 2024-04-09
entry_price = 25,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv`:

```text
2024-04-09,25100,29800,25100,27900
2024-04-29,33800,38400,33400,33700
2024-06-11,40300,41850,39000,40200
2024-12-09,15170,15300,14190,14190
```

### Backtest

```text
MFE_30D  = +52.99%
MAE_30D  = +0.00%
MFE_90D  = +66.73%
MAE_90D  = +0.00%
MFE_180D = +66.73%
MAE_180D = -43.47%
peak_180 = 41,850 on 2024-06-11
trough_180 = 14,190 on 2024-12-09
peak_to_later_drawdown = -66.09%
```

### Interpretation

This is the C07 lifecycle warning in its purest form.  
The first half looks like Stage2/Green. The second half says the bridge stopped feeding the price.

FST should be treated as:

```text
Stage2 possible after source repair
later local 4B-watch if customer/order evidence fails to refresh
```

---

## Case 3 — Counterexample / local 4B: 095610 / 테스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests equipment beta without durable customer order/backlog/margin refresh.

```text
evidence_family = SEMICONDUCTOR_EQUIPMENT_HBM_CAPEX_BETA_WITH_WEAK_ORDER_MARGIN_REFRESH
case_role = counterexample
trigger_date = 2024-04-01
entry_date = 2024-04-02
entry_price = 23,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv`:

```text
2024-04-02,23500,26400,23150,25150
2024-04-17,30000,32900,28500,29300
2024-07-22,21900,22000,21200,21300
2024-12-09,14090,14090,13090,13090
```

### Backtest

```text
MFE_30D  = +40.00%
MAE_30D  = -4.04%
MFE_90D  = +40.00%
MAE_90D  = -9.79%
MFE_180D = +40.00%
MAE_180D = -44.30%
peak_180 = 32,900 on 2024-04-17
trough_180 = 13,090 on 2024-12-09
peak_to_later_drawdown = -60.21%
```

### Interpretation

This is the C07 false-positive path.  
The first move was strong, but the bridge did not hold. If order/backlog/margin evidence is not visible, the correct label is:

```text
false Stage2 / local 4B-watch
```

not durable Green.

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
do_not_raise_generic_C07_equipment_weight = true
do_not_treat_all_HBM_equipment_beta_as_Green = true
do_not_convert_equipment_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE
```

This fine archetype covers:

```text
1. deposition equipment order/customer bridge → Stage2 possible after source repair
2. ancillary equipment relative strength → Stage2 possible, but later local 4B if bridge fades
3. equipment beta without order/margin refresh → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "74", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "case_type": "hbm_equipment_order_relative_strength", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-DepositionEquipmentRelativeStrength", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 should allow Stage2 when front-end deposition equipment relative strength connects to HBM/DRAM capex, customer order visibility and margin bridge. Eugene Tech produced high MFE with limited entry MAE, but later post-peak drawdown means a lifecycle local 4B guard is needed if order/margin evidence stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web price path usable; non-proxy order/customer/backlog/margin evidence must be attached before promotion."}
{"row_type": "case", "case_id": "R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS", "symbol": "036810", "company_name": "에프에스티", "round": "R2", "loop": "74", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "case_type": "hbm_equipment_order_relative_strength", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AncillaryEquipmentRelativeStrength", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 can include ancillary equipment when relative strength is tied to customer adoption, capex timing and margin conversion. FST had strong early MFE, but the later collapse shows that price strength must decay into local 4B if order/customer bridge evidence fails to refresh.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web price path usable; non-proxy order/customer/backlog/margin evidence must be attached before promotion."}
{"row_type": "case", "case_id": "R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "74", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "case_type": "hbm_equipment_order_relative_strength", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / EquipmentBetaBridgeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 should not treat a one-month equipment beta spike as durable Stage2 unless named customer order, HBM-related capex, backlog or margin bridge refreshes. TES had strong initial MFE but later opened severe MAE and drawdown, making it a local 4B-watch / false Stage2 row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web price path usable; non-proxy order/customer/backlog/margin evidence must be attached before promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "case_id": "R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "symbol": "084370", "company_name": "유진테크", "round": "R2", "loop": "74", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-DepositionEquipmentRelativeStrength", "trigger_date": "2024-03-20", "entry_date": "2024-03-21", "entry_price": 37750.0, "evidence_available_at_that_date": "DRAM_HBM_FRONTEND_DEPOSITION_EQUIPMENT_ORDER_RELATIVE_STRENGTH_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:EUGENE_TECH_2024_DRAM_HBM_FRONTEND_DEPOSITION_ORDER_RELATIVE_STRENGTH_MARGIN_BRIDGE", "stage2_evidence_fields": ["equipment_order_candidate", "relative_strength", "hbm_capex_or_customer_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "order_backlog_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv", "profile_path": "atlas/symbol_profiles/084/084370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 49.93, "MFE_90D_pct": 58.94, "MFE_180D_pct": 58.94, "MAE_30D_pct": -0.93, "MAE_90D_pct": -0.93, "MAE_180D_pct": -16.29, "peak_date": "2024-05-28", "peak_price": 60000.0, "drawdown_after_peak_pct": -47.33, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_relative_strength_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_customer_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C07 should allow Stage2 when front-end deposition equipment relative strength connects to HBM/DRAM capex, customer order visibility and margin bridge. Eugene Tech produced high MFE with limited entry MAE, but later post-peak drawdown means a lifecycle local 4B guard is needed if order/margin evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C07_EQUIPMENT_RS_084370_2024-03-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS", "case_id": "R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS", "symbol": "036810", "company_name": "에프에스티", "round": "R2", "loop": "74", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-AncillaryEquipmentRelativeStrength", "trigger_date": "2024-04-08", "entry_date": "2024-04-09", "entry_price": 25100.0, "evidence_available_at_that_date": "EUV_PELLICLE_CHILLER_ANCILLARY_EQUIPMENT_RELATIVE_STRENGTH_WITH_LATER_BRIDGE_FADE", "evidence_source": "source_proxy_manual_verification_required:FST_2024_EUV_PELLICLE_CHILLER_ANCILLARY_EQUIPMENT_CUSTOMER_ADOPTION_ORDER_BRIDGE", "stage2_evidence_fields": ["equipment_order_candidate", "relative_strength", "hbm_capex_or_customer_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "order_backlog_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv", "profile_path": "atlas/symbol_profiles/036/036810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 52.99, "MFE_90D_pct": 66.73, "MFE_180D_pct": 66.73, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -43.47, "peak_date": "2024-06-11", "peak_price": 41850.0, "drawdown_after_peak_pct": -66.09, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_relative_strength_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_customer_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C07 can include ancillary equipment when relative strength is tied to customer adoption, capex timing and margin conversion. FST had strong early MFE, but the later collapse shows that price strength must decay into local 4B if order/customer bridge evidence fails to refresh.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C07_EQUIPMENT_RS_036810_2024-04-09", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE", "case_id": "R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "74", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / EquipmentBetaBridgeFade", "trigger_date": "2024-04-01", "entry_date": "2024-04-02", "entry_price": 23500.0, "evidence_available_at_that_date": "SEMICONDUCTOR_EQUIPMENT_HBM_CAPEX_BETA_WITH_WEAK_ORDER_MARGIN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:TES_2024_SEMI_EQUIPMENT_HBM_CAPEX_ORDER_MARGIN_REFRESH_BRIDGE", "stage2_evidence_fields": ["equipment_order_candidate", "relative_strength", "hbm_capex_or_customer_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "order_backlog_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv", "profile_path": "atlas/symbol_profiles/095/095610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.0, "MFE_90D_pct": 40.0, "MFE_180D_pct": 40.0, "MAE_30D_pct": -4.04, "MAE_90D_pct": -9.79, "MAE_180D_pct": -44.3, "peak_date": "2024-04-17", "peak_price": 32900.0, "drawdown_after_peak_pct": -60.21, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_relative_strength_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_customer_or_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C07 should not treat a one-month equipment beta spike as durable Stage2 unless named customer order, HBM-related capex, backlog or margin bridge refreshes. TES had strong initial MFE but later opened severe MAE and drawdown, making it a local 4B-watch / false Stage2 row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C07_EQUIPMENT_RS_095610_2024-04-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "trigger_id": "TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "symbol": "084370", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 10, "revision_score": 9, "relative_strength_score": 16, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 9, "margin_bridge_score": 12, "revision_score": 10, "relative_strength_score": 16, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Yellow/Green candidate after source repair + lifecycle 4B", "changed_components": ["relative_strength_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified HBM/DRAM equipment order, customer adoption, backlog or margin bridge; cap pure equipment beta when bridge evidence fails to refresh.", "MFE_90D_pct": 58.94, "MAE_90D_pct": -0.93, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C07 should allow Stage2 when front-end deposition equipment relative strength connects to HBM/DRAM capex, customer order visibility and margin bridge. Eugene Tech produced high MFE with limited entry MAE, but later post-peak drawdown means a lifecycle local 4B guard is needed if order/margin evidence stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS", "trigger_id": "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS", "symbol": "036810", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 8, "margin_bridge_score": 10, "revision_score": 9, "relative_strength_score": 16, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 9, "margin_bridge_score": 12, "revision_score": 10, "relative_strength_score": 16, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Yellow/Green candidate after source repair + lifecycle 4B", "changed_components": ["relative_strength_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified HBM/DRAM equipment order, customer adoption, backlog or margin bridge; cap pure equipment beta when bridge evidence fails to refresh.", "MFE_90D_pct": 66.73, "MAE_90D_pct": 0.0, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C07 can include ancillary equipment when relative strength is tied to customer adoption, capex timing and margin conversion. FST had strong early MFE, but the later collapse shows that price strength must decay into local 4B if order/customer bridge evidence fails to refresh."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE", "trigger_id": "TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE", "symbol": "095610", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 55, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 6, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 44, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["relative_strength_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified HBM/DRAM equipment order, customer adoption, backlog or margin bridge; cap pure equipment beta when bridge evidence fails to refresh.", "MFE_90D_pct": 40.0, "MAE_90D_pct": -9.79, "score_return_alignment_label": "false_positive_equipment_beta_bridge_gap", "current_profile_verdict": "C07 should not treat a one-month equipment beta spike as durable Stage2 unless named customer order, HBM-related capex, backlog or margin bridge refreshes. TES had strong initial MFE but later opened severe MAE and drawdown, making it a local 4B-watch / false Stage2 row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 74, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused/new C07 symbols, +3 deposition/chiller/equipment-beta families, +2 equipment relative-strength positives, +1 bridge-fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 74, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "axis": "frontend_deposition_chiller_equipment_relative_strength_vs_hbm_equipment_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C07 should split verified equipment order/customer/backlog relative-strength from price-only HBM equipment beta. Stage2 requires customer order, capex slot, adoption, backlog or margin bridge. If early MFE is followed by stale evidence and large post-peak drawdown, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["084370", "036810", "095610"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 74, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C07 needs verified equipment order/customer bridge. Eugene Tech and FST show relative-strength positives with lifecycle drawdown; TES shows equipment beta fading into local 4B when order/margin refresh fails."}
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
084370:
  corporate_action_candidate_dates = 2007-05-17, 2010-01-22, 2012-06-07
  selected window = 2024-03-21~D+180
  contamination = false

036810:
  corporate_action_candidate_dates = 2000-05-02, 2004-06-17
  selected window = 2024-04-09~D+180
  contamination = false

095610:
  corporate_action_candidate_dates = 2011-08-10, 2011-08-29, 2016-05-09
  selected window = 2024-04-02~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C07 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C07 rule-shape discovery,
but coding-agent promotion requires non-proxy order, customer, capex, backlog and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C07 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
frontend_deposition_chiller_equipment_relative_strength_vs_hbm_equipment_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 084370, 036810 and 095610.
4. Keep generic C07 equipment weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - named equipment order, customer adoption or capex slot evidence is explicit,
   - backlog or delivery visibility is present,
   - margin/revision bridge is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is HBM/equipment beta only,
   - order/backlog/margin bridge is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, customer loss, margin break, or thesis deterioration evidence.
8. Emit before/after diagnostics and reject if verified equipment-order positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 74
next_round = R3
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

