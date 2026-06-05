# E2R Stock-Web v12 Residual Research — R2 Loop 88 — L2 / C10

```text
metadata_schema: e2r_stock_web_v12_sector_archetype_residual
scheduled_round: R2
scheduled_loop: 88
completed_round: R2
completed_loop: 88
next_round: R3
next_loop: 88
round_schedule_status: valid
round_sector_consistency: pass

large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_CYCLE_FADE
sector: AI / semiconductor / electronics
primary_archetype: memory recovery equipment cycle
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression

price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection Rationale

R13 loop 87 completed the prior loop checkpoint, so the scheduler rotates to `R1 / loop 88`; the previous run completed R1, therefore this execution is `R2 / loop 88`.  
R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`.

Within R2, `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` remains a useful residual bucket because the first-order memory-cycle recovery rule is easy to over-credit. The key unresolved question is whether a memory equipment rally is backed by order/revenue conversion, or whether it is only a cycle-beta rebound that later becomes high-MAE.

No-Repeat handling:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date

selected cases:
- C10 / 240810 / Stage2-Actionable / 2024-02-29
- C10 / 039030 / Stage2-Actionable / 2024-02-28
- C10 / 036930 / Stage2-Actionable / 2024-02-28

reused_case_count: 0
new_independent_case_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 2
```

## 2. Stock-Web Price Source Validation

Stock-web manifest basis:

```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
```

Profile checks:

| symbol | company | profile path | profile status | corporate action window |
|---|---|---|---|---|
| 240810 | 원익IPS | `atlas/symbol_profiles/240/240810.json` | active_like, available through 2026-02-20 | `corporate_action_candidate_count=0`, usable |
| 039030 | 이오테크닉스 | `atlas/symbol_profiles/039/039030.json` | active_like, available through 2026-02-20 | old 2003 candidate only, no overlap with 2024 window |
| 036930 | 주성엔지니어링 | `atlas/symbol_profiles/036/036930.json` | active_like, available through 2026-02-20 | old 2000 candidate only, no overlap with 2024 window |

All representative trigger rows below are 30D/90D/180D calibration usable.

## 3. Case Table

| case_id | symbol | company | trigger_date | entry_price | outcome | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | interpretation |
|---|---:|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| R2L88_C10_240810_MEMORY_RECOVERY_ORDER_CONVERSION_FADE | 240810 | 원익IPS | 2024-02-29 | 32800 | counterexample | 36.7 | -12.8 | 36.7 | -12.8 | 36.7 | -32.3 | early_MFE_then_high_MAE_cycle_fade |
| R2L88_C10_039030_LASER_ADVANCED_MEMORY_RECOVERY_PEAK_CAPTURE | 039030 | 이오테크닉스 | 2024-02-28 | 202000 | positive_with_4B_overlay | 31.7 | -15.0 | 31.7 | -15.6 | 31.7 | -35.9 | structural_success_but_4B_needed |
| R2L88_C10_036930_ALD_MEMORY_RECOVERY_ORDER_QUALITY_COUNTEREXAMPLE | 036930 | 주성엔지니어링 | 2024-02-28 | 40000 | counterexample | 3.6 | -16.4 | 3.6 | -23.4 | 3.6 | -44.6 | failed_rerating_high_MAE |

## 4. Case Notes

### 4.1 `240810` 원익IPS — early recovery MFE, later high-MAE fade

The 2024-02-29 breakout created a valid Stage2-like memory recovery entry. It generated strong early MFE, but the same window later rolled into a large 180D drawdown. This is the classic C10 trap: memory recovery beta looks like earnings recovery before order conversion is actually proven.

```text
entry_date: 2024-02-29
entry_price: 32800
local_peak: 2024-04-08 high 44850
180D low proxy: 2024-11-14 low 22200
verdict: counterexample / cycle-fade after early MFE
```

### 4.2 `039030` 이오테크닉스 — positive structural move, but 4B guard needed

The 2024-02-28 move worked as an early Stage2 entry and produced a high-quality 30D/90D MFE path. But after the April spike, the same case also shows why C10 needs local 4B or valuation/positioning guard. The signal was not wrong; the failure is treating the early MFE as a permanent Green unlock without a peak-capture or revision-slowdown overlay.

```text
entry_date: 2024-02-28
entry_price: 202000
local/full observed peak: 2024-04-04 high 266000
180D low proxy: 2024-08-05 low 129400
verdict: positive with 4B overlay
```

### 4.3 `036930` 주성엔지니어링 — memory-recovery theme without durable order conversion

The 2024-02-28 price move had enough memory recovery momentum to look actionable, but forward returns were weak and the downside became severe. This is a C10 false-positive example where the order-quality bridge should have blocked Stage2-Actionable or reduced independent evidence weight.

```text
entry_date: 2024-02-28
entry_price: 40000
local_peak: 2024-04-08 high 41450
180D low proxy: 2024-08-05 low 22150
verdict: failed rerating / high-MAE counterexample
```

## 5. Machine-Readable Trigger Rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L88_C10_240810_2024-02-29_STAGE2_ACTIONABLE", "case_id": "R2L88_C10_240810_MEMORY_RECOVERY_ORDER_CONVERSION_FADE", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_CYCLE_FADE", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable / MemoryRecoveryEquipmentCycle", "trigger_date": "2024-02-29", "evidence_available_at_that_date": "NAND/DRAM wafer equipment recovery expectations and domestic memory customer capex normalization; order-conversion bridge still incomplete at trigger date.", "evidence_source": "source_proxy_public_news_and_broker_note_memory_capex_recovery", "stage2_evidence_fields": "memory/customer capex recovery; equipment revenue conversion watch; relative strength", "stage3_evidence_fields": "confirmed order/backlog conversion, margin bridge, customer pull-in; not fully available for all cases", "stage4b_evidence_fields": "price_only_cycle_fade_watch", "stage4c_evidence_fields": "cycle fade / order slippage / high MAE after failed conversion", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "profile_path": "atlas/symbol_profiles/240/240810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-29", "entry_price": 32800, "MFE_30D_pct": 36.7, "MFE_90D_pct": 36.7, "MFE_180D_pct": 36.7, "MFE_1Y_pct": "not_used_in_calibration", "MFE_2Y_pct": "not_used_in_calibration", "MAE_30D_pct": -12.8, "MAE_90D_pct": -12.8, "MAE_180D_pct": -32.3, "MAE_1Y_pct": "not_used_in_calibration", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 44850, "drawdown_after_peak_pct": -50.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_primary_4B_case", "four_b_evidence_type": "price_only_cycle_fade_watch", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "counterexample", "current_profile_verdict": "current_profile_overcredits_stage2_if_order_conversion_missing", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": "", "corporate_action_window_status": "clear_180D_window; profile corporate_action_candidate_count=0", "same_entry_group_id": "C10_240810_2024-02-29_32800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L88_C10_039030_2024-02-28_STAGE2_ACTIONABLE", "case_id": "R2L88_C10_039030_LASER_ADVANCED_MEMORY_RECOVERY_PEAK_CAPTURE", "symbol": "039030", "company_name": "이오테크닉스", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_CYCLE_FADE", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable / LaserMemoryRecoveryEquipment", "trigger_date": "2024-02-28", "evidence_available_at_that_date": "HBM/advanced packaging and laser process recovery narrative converted into strong early RS; still needed valuation/4B guard after spring blowoff.", "evidence_source": "source_proxy_public_news_and_broker_note_hbm_laser_advanced_packaging", "stage2_evidence_fields": "memory/customer capex recovery; equipment revenue conversion watch; relative strength", "stage3_evidence_fields": "confirmed order/backlog conversion, margin bridge, customer pull-in; not fully available for all cases", "stage4b_evidence_fields": "valuation_blowoff|revision_slowdown", "stage4c_evidence_fields": "cycle fade / order slippage / high MAE after failed conversion", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-28", "entry_price": 202000, "MFE_30D_pct": 31.7, "MFE_90D_pct": 31.7, "MFE_180D_pct": 31.7, "MFE_1Y_pct": "not_used_in_calibration", "MFE_2Y_pct": "not_used_in_calibration", "MAE_30D_pct": -15.0, "MAE_90D_pct": -15.6, "MAE_180D_pct": -35.9, "MAE_1Y_pct": "not_used_in_calibration", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-04", "peak_price": 266000, "drawdown_after_peak_pct": -51.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_and_valuation_local_4B_needed", "four_b_evidence_type": "valuation_blowoff|revision_slowdown", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_with_4B_overlay", "current_profile_verdict": "current_profile_ok_for_stage2_but_needs_local_4B_after_blowoff", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": "", "corporate_action_window_status": "clear_180D_window; only old 2003 corporate-action candidate outside window", "same_entry_group_id": "C10_039030_2024-02-28_202000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L88_C10_036930_2024-02-28_STAGE2_ACTIONABLE", "case_id": "R2L88_C10_036930_ALD_MEMORY_RECOVERY_ORDER_QUALITY_COUNTEREXAMPLE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_CYCLE_FADE", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable / MemoryRecoveryEquipmentOrderQualityTest", "trigger_date": "2024-02-28", "evidence_available_at_that_date": "Memory recovery + ALD equipment theme created a Stage2-like breakout, but customer/order conversion and sustained margin visibility were insufficient.", "evidence_source": "source_proxy_public_news_and_broker_note_memory_ald_cycle", "stage2_evidence_fields": "memory/customer capex recovery; equipment revenue conversion watch; relative strength", "stage3_evidence_fields": "confirmed order/backlog conversion, margin bridge, customer pull-in; not fully available for all cases", "stage4b_evidence_fields": "price_only_cycle_fade_watch", "stage4c_evidence_fields": "cycle fade / order slippage / high MAE after failed conversion", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "profile_path": "atlas/symbol_profiles/036/036930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-28", "entry_price": 40000, "MFE_30D_pct": 3.6, "MFE_90D_pct": 3.6, "MFE_180D_pct": 3.6, "MFE_1Y_pct": "not_used_in_calibration", "MFE_2Y_pct": "not_used_in_calibration", "MAE_30D_pct": -16.4, "MAE_90D_pct": -23.4, "MAE_180D_pct": -44.6, "MAE_1Y_pct": "not_used_in_calibration", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 41450, "drawdown_after_peak_pct": -46.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_primary_4B_case", "four_b_evidence_type": "price_only_cycle_fade_watch", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "counterexample", "current_profile_verdict": "current_profile_false_positive_without_order_conversion_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": "", "corporate_action_window_status": "clear_180D_window; old 2000 corporate-action candidate outside window", "same_entry_group_id": "C10_036930_2024-02-28_40000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

## 6. Score Simulation Rows

```jsonl
{"row_type": "score_simulation", "case_id": "R2L88_C10_240810_MEMORY_RECOVERY_ORDER_CONVERSION_FADE", "symbol": "240810", "profile_id": "P0_to_P3_research_proxy", "profile_scope": "canonical_archetype_specific", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "order_intake_quality_score": 2, "positioning_overheat_score": 4, "thesis_break_score": 5}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "order_intake_quality_score": 1, "positioning_overheat_score": 4, "thesis_break_score": 7}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch/Counterexample", "component_delta_explanation": "C10 adjustment requires order/revenue conversion and downgrades memory-recovery theme-only cases; adds local 4B/cycle-fade watch after early MFE spike."}
{"row_type": "score_simulation", "case_id": "R2L88_C10_039030_LASER_ADVANCED_MEMORY_RECOVERY_PEAK_CAPTURE", "symbol": "039030", "profile_id": "P0_to_P3_research_proxy", "profile_scope": "canonical_archetype_specific", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "order_intake_quality_score": 5, "positioning_overheat_score": 4, "thesis_break_score": 2}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "order_intake_quality_score": 5, "positioning_overheat_score": 4, "thesis_break_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "component_delta_explanation": "C10 adjustment requires order/revenue conversion and downgrades memory-recovery theme-only cases; adds local 4B/cycle-fade watch after early MFE spike."}
{"row_type": "score_simulation", "case_id": "R2L88_C10_036930_ALD_MEMORY_RECOVERY_ORDER_QUALITY_COUNTEREXAMPLE", "symbol": "036930", "profile_id": "P0_to_P3_research_proxy", "profile_scope": "canonical_archetype_specific", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "order_intake_quality_score": 2, "positioning_overheat_score": 2, "thesis_break_score": 5}, "weighted_score_before": 63, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "order_intake_quality_score": 1, "positioning_overheat_score": 2, "thesis_break_score": 7}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch/Counterexample", "component_delta_explanation": "C10 adjustment requires order/revenue conversion and downgrades memory-recovery theme-only cases; adds local 4B/cycle-fade watch after early MFE spike."}
```

## 7. Aggregate Metric Row

```jsonl
{"row_type": "aggregate_metric", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_CYCLE_FADE", "case_count": 3, "new_independent_case_count": 3, "positive_case_count": 1, "counterexample_count": 2, "calibration_usable_case_count": 3, "avg_MFE_90D_pct": 24.0, "avg_MAE_90D_pct": -17.3, "avg_MFE_180D_pct": 24.0, "avg_MAE_180D_pct": -37.6, "false_positive_rate": 0.67, "score_return_alignment_verdict": "mixed: Stage2 can be early, but C10 needs explicit order-conversion + 4B/cycle-fade guard"}
```

## 8. Shadow Rule Candidate

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": "88", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_CYCLE_FADE", "rule_scope": "canonical_archetype_specific", "existing_axis_tested": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "existing_axis_kept": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "new_axis_proposed": null, "candidate_rule": "Within C10, memory recovery beta should not receive full Stage2-Actionable credit unless at least one order/revenue conversion bridge is visible. Early MFE spike above +25% should create local 4B watch if margin/revision bridge lags.", "promotion_recommendation": "hold_for_more_evidence", "do_not_propose_new_weight_delta": true, "rationale": "Only three new cases; positive/counterexample balance is good, but evidence sources remain proxy-level. Use as residual error material, not production patch."}
```

## 9. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | calibration_usable_case_count | new_symbol_count | 4B_or_4C_case_count | status |
|---|---|---|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | WAFER_PROCESS_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_VS_CYCLE_FADE | 1 | 2 | 3 | 3 | 1 | residual_error_found |

## 10. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- full_4b_requires_non_price_evidence
- price_only_blowoff_blocks_positive_stage

residual_error_types_found:
- memory-cycle beta over-credited before order conversion
- early MFE followed by high-MAE cycle fade
- lack of local 4B/valuation guard after advanced-equipment spike

new_axis_proposed: null
existing_axis_strengthened: null
existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- full_4b_requires_non_price_evidence
- price_only_blowoff_blocks_positive_stage

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: insufficient non-proxy evidence source depth; keep as residual/counterexample material
loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this in the research session.

When batch-applying v12 research artifacts, ingest this MD as C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE residual evidence only.
Use the JSONL trigger rows for representative calibration rows.
Do not add a global scoring patch.
If additional R2/C10 cases confirm the same pattern, consider a canonical-specific guard:
  - C10 Stage2-Actionable requires explicit order/revenue conversion or revision bridge, not memory-cycle beta alone.
  - C10 early MFE spike above +25% with weak order bridge should create local 4B watch, not automatic Green.
Keep production_scoring_changed=false until this is supported by more non-proxy evidence.
```

## 12. Round State

```text
completed_round = R2
completed_loop = 88
next_round = R3
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
