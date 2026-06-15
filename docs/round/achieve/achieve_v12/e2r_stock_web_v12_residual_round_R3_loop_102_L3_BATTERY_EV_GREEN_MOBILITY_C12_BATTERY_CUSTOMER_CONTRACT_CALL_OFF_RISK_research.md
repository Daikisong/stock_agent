---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 102
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_SECOND_PASS_VS_PARENT_BALANCE_SHEET_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web v12 Residual Research — R3/L3/C12 Battery Customer Contract Call-off Risk Second Pass

```text
output_file = e2r_stock_web_v12_residual_round_R3_loop_102_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round = R3
selected_loop = 102
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_SECOND_PASS_VS_PARENT_BALANCE_SHEET_FALSE_POSITIVE
```

## 1. Coverage-index selection

`V12_Research_No_Repeat_Index.md` keeps C12 in Priority 0 with 16 static representative rows and a need-to-30 gap. A conversation-local C12 loop 101 file already added four rows using 348370, 247540, 361610, and 278280, so this second pass avoids those exact C12 symbol/entry combinations and adds 373220, 096770, 011790, and 051910. The goal is not to restate the global 4B non-price rule, but to isolate a battery-specific failure mode: customer contract headlines and AMPC/IRA labels are often upstream of real call-off, utilization, and cash conversion evidence.

```text
selection_reason = C12 remains under-covered; need more customer-demand/call-off false-positive and high-MAE guard rows.
selected_priority_bucket = Priority 0
static_index_rows = 16
conversation_local_prior_c12_rows = 20
conversation_local_after_this_loop = 24
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_count = 0
same_canonical_archetype_research = allowed
```

## 2. Price atlas validation

```jsonl
{"row_type": "price_source_validation", "price_source": "Songdaiki/stock-web", "source_name": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK"}
{"row_type": "price_source_validation", "symbol": "373220", "name": "LG에너지솔루션", "profile": "atlas/symbol_profiles/373/373220.json", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "corporate_action_candidate_count": 0, "has_major_raw_discontinuity": false, "calibration_caveat": "", "calibration_usable": true}
{"row_type": "price_source_validation", "symbol": "096770", "name": "SK이노베이션", "profile": "atlas/symbol_profiles/096/096770.json", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv", "corporate_action_candidate_count": 1, "has_major_raw_discontinuity": true, "calibration_caveat": "corporate action candidate at 2024-11-20; entries selected so 180D window ends before contamination", "calibration_usable": true}
{"row_type": "price_source_validation", "symbol": "011790", "name": "SKC", "profile": "atlas/symbol_profiles/011/011790.json", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv", "corporate_action_candidate_count": 2, "has_major_raw_discontinuity": true, "calibration_caveat": "historic corporate actions only, no overlap with 2024 180D window", "calibration_usable": true}
{"row_type": "price_source_validation", "symbol": "051910", "name": "LG화학", "profile": "atlas/symbol_profiles/051/051910.json", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv", "corporate_action_candidate_count": 0, "has_major_raw_discontinuity": false, "calibration_caveat": "", "calibration_usable": true}
```

## 3. Case rows

```jsonl
{"row_type": "case", "case_id": "C12_R3_L102_CASE_001", "symbol": "373220", "name": "LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_role": "failed_rerating_calloff_counterexample", "trigger_family": "cell_customer_inventory_destocking_calloff_vs_amPC_label", "entry_date": "2024-03-12", "entry_price": 419500.0, "evidence_url_pending": true, "source_proxy_only": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C12_R3_L102_CASE_002", "symbol": "096770", "name": "SK이노베이션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_role": "mixed_parent_battery_calloff_watch", "trigger_family": "parent_battery_turnaround_customer_contract_vs_balance_sheet_drag", "entry_date": "2024-01-29", "entry_price": 120300.0, "evidence_url_pending": true, "source_proxy_only": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C12_R3_L102_CASE_003", "symbol": "011790", "name": "SKC", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_role": "mixed_positive_local_4b_watch", "trigger_family": "copper_foil_customer_demand_restocking_vs_contract_calloff_bridge", "entry_date": "2024-04-05", "entry_price": 138100.0, "evidence_url_pending": true, "source_proxy_only": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "C12_R3_L102_CASE_004", "symbol": "051910", "name": "LG화학", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_role": "failed_cathode_customer_calloff_counterexample", "trigger_family": "cathode_material_customer_demand_calloff_margin_drag", "entry_date": "2024-02-16", "entry_price": 504000.0, "evidence_url_pending": true, "source_proxy_only": true, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

## 4. Trigger-level backtest rows: 30D / 90D / 180D MFE-MAE

Every trigger uses the next available tradable row when needed; in this pass all entry dates are present in the tradable shard. Metrics are based on raw/unadjusted OHLC from stock-web and are therefore blocked if a corporate-action candidate overlaps the forward window. No selected 180D window is blocked.

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "case_id": "C12_R3_L102_CASE_001", "same_entry_group_id": "C12_373220_2024-03-12_Stage2-Actionable", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "selected_round": "R3", "selected_loop": 102, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_SECOND_PASS_VS_PARENT_BALANCE_SHEET_FALSE_POSITIVE", "symbol": "373220", "name": "LG에너지솔루션", "trigger_type": "Stage2-Actionable", "trigger_family": "cell_customer_inventory_destocking_calloff_vs_amPC_label", "entry_date": "2024-03-12", "entry_price": 419500.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_basis": "trading_days", "calibration_usable": true, "peak_30d_date": "2024-03-13", "peak_30d_high": 422000.0, "mfe_30d_pct": 0.6, "trough_30d_date": "2024-04-08", "trough_30d_low": 358000.0, "mae_30d_pct": -14.66, "peak_90d_date": "2024-03-13", "peak_90d_high": 422000.0, "mfe_90d_pct": 0.6, "trough_90d_date": "2024-06-28", "trough_90d_low": 322500.0, "mae_90d_pct": -23.12, "peak_180d_date": "2024-10-08", "peak_180d_high": 444000.0, "mfe_180d_pct": 5.84, "trough_180d_date": "2024-08-08", "trough_180d_low": 311000.0, "mae_180d_pct": -25.86, "score_return_alignment": "aligned_counterexample", "current_profile_error": "Stage2-Actionable may fire on customer/AMPC label before utilization and customer order cadence recover; the path has limited MFE and deep MAE.", "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "case_id": "C12_R3_L102_CASE_002", "same_entry_group_id": "C12_096770_2024-01-29_Stage2-Actionable", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "selected_round": "R3", "selected_loop": 102, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_SECOND_PASS_VS_PARENT_BALANCE_SHEET_FALSE_POSITIVE", "symbol": "096770", "name": "SK이노베이션", "trigger_type": "Stage2-Actionable", "trigger_family": "parent_battery_turnaround_customer_contract_vs_balance_sheet_drag", "entry_date": "2024-01-29", "entry_price": 120300.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_basis": "trading_days", "calibration_usable": true, "peak_30d_date": "2024-02-06", "peak_30d_high": 130900.0, "mfe_30d_pct": 8.81, "trough_30d_date": "2024-02-29", "trough_30d_low": 116700.0, "mae_30d_pct": -2.99, "peak_90d_date": "2024-02-06", "peak_90d_high": 130900.0, "mfe_90d_pct": 8.81, "trough_90d_date": "2024-05-31", "trough_90d_low": 99600.0, "mae_90d_pct": -17.21, "peak_180d_date": "2024-02-06", "peak_180d_high": 130900.0, "mfe_180d_pct": 8.81, "trough_180d_date": "2024-08-07", "trough_180d_low": 98000.0, "mae_180d_pct": -18.54, "score_return_alignment": "mixed_local_mfe_high_mae", "current_profile_error": "A parent-level EV/battery turnaround tag can preserve Stage2 but should be capped until SK On-style customer volume, funding, and call-off evidence clear parent balance-sheet drag.", "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "case_id": "C12_R3_L102_CASE_003", "same_entry_group_id": "C12_011790_2024-04-05_Stage2-Actionable", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "selected_round": "R3", "selected_loop": 102, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_SECOND_PASS_VS_PARENT_BALANCE_SHEET_FALSE_POSITIVE", "symbol": "011790", "name": "SKC", "trigger_type": "Stage2-Actionable", "trigger_family": "copper_foil_customer_demand_restocking_vs_contract_calloff_bridge", "entry_date": "2024-04-05", "entry_price": 138100.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_basis": "trading_days", "calibration_usable": true, "peak_30d_date": "2024-04-09", "peak_30d_high": 149700.0, "mfe_30d_pct": 8.4, "trough_30d_date": "2024-05-17", "trough_30d_low": 101300.0, "mae_30d_pct": -26.65, "peak_90d_date": "2024-06-18", "peak_90d_high": 200000.0, "mfe_90d_pct": 44.82, "trough_90d_date": "2024-05-17", "trough_90d_low": 101300.0, "mae_90d_pct": -26.65, "peak_180d_date": "2024-06-18", "peak_180d_high": 200000.0, "mfe_180d_pct": 44.82, "trough_180d_date": "2024-11-15", "trough_180d_low": 93400.0, "mae_180d_pct": -32.37, "score_return_alignment": "mixed_local_mfe_high_mae", "current_profile_error": "This is the positive control for preserving local MFE, but the model must split early restocking rally from durable customer contract/call-off conversion because MAE stayed extreme.", "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "case_id": "C12_R3_L102_CASE_004", "same_entry_group_id": "C12_051910_2024-02-16_Stage4B", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "selected_round": "R3", "selected_loop": 102, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_TO_CASH_BRIDGE_SECOND_PASS_VS_PARENT_BALANCE_SHEET_FALSE_POSITIVE", "symbol": "051910", "name": "LG화학", "trigger_type": "Stage4B", "trigger_family": "cathode_material_customer_demand_calloff_margin_drag", "entry_date": "2024-02-16", "entry_price": 504000.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_basis": "trading_days", "calibration_usable": true, "peak_30d_date": "2024-02-19", "peak_30d_high": 520000.0, "mfe_30d_pct": 3.17, "trough_30d_date": "2024-04-02", "trough_30d_low": 420500.0, "mae_30d_pct": -16.57, "peak_90d_date": "2024-02-19", "peak_90d_high": 520000.0, "mfe_90d_pct": 3.17, "trough_90d_date": "2024-07-19", "trough_90d_low": 326000.0, "mae_90d_pct": -35.32, "peak_180d_date": "2024-02-19", "peak_180d_high": 520000.0, "mfe_180d_pct": 3.17, "trough_180d_date": "2024-11-15", "trough_180d_low": 267500.0, "mae_180d_pct": -46.92, "score_return_alignment": "aligned_counterexample", "current_profile_error": "Cathode/customer mix label plus low valuation can look actionable, but without customer call-off reversal and margin recovery it should remain 4B/4C rather than Stage3.", "evidence_url_pending": true, "source_proxy_only": true}
```

## 5. Human-readable path notes

### C12_R3_L102_CASE_001 — 373220 LG에너지솔루션
- Entry: 2024-03-12 close 419,500.
- 30D path: MFE 0.6% at 2024-03-13 / MAE -14.66% at 2024-04-08.
- 90D path: MFE 0.6% at 2024-03-13 / MAE -23.12% at 2024-06-28.
- 180D path: MFE 5.84% at 2024-10-08 / MAE -25.86% at 2024-08-08.
- Residual thesis: Large-cell customer demand recovery label without utilization/call-off evidence remained a high-MAE false positive.

### C12_R3_L102_CASE_002 — 096770 SK이노베이션
- Entry: 2024-01-29 close 120,300.
- 30D path: MFE 8.81% at 2024-02-06 / MAE -2.99% at 2024-02-29.
- 90D path: MFE 8.81% at 2024-02-06 / MAE -17.21% at 2024-05-31.
- 180D path: MFE 8.81% at 2024-02-06 / MAE -18.54% at 2024-08-07.
- Residual thesis: The entry had small local upside but never converted into a clean 90/180D rerating because customer demand and funding quality stayed unresolved.

### C12_R3_L102_CASE_003 — 011790 SKC
- Entry: 2024-04-05 close 138,100.
- 30D path: MFE 8.4% at 2024-04-09 / MAE -26.65% at 2024-05-17.
- 90D path: MFE 44.82% at 2024-06-18 / MAE -26.65% at 2024-05-17.
- 180D path: MFE 44.82% at 2024-06-18 / MAE -32.37% at 2024-11-15.
- Residual thesis: SKC shows why C12 should not block every battery-demand recovery label, but it must demand customer reorder/utilization evidence before Green.

### C12_R3_L102_CASE_004 — 051910 LG화학
- Entry: 2024-02-16 close 504,000.
- 30D path: MFE 3.17% at 2024-02-19 / MAE -16.57% at 2024-04-02.
- 90D path: MFE 3.17% at 2024-02-19 / MAE -35.32% at 2024-07-19.
- 180D path: MFE 3.17% at 2024-02-19 / MAE -46.92% at 2024-11-15.
- Residual thesis: LG화학 is the clean counterexample where customer-demand/cathode recovery language failed to defend a 90/180D path.

## 6. Current calibrated profile stress test

The current profile already blocks pure price-only blowoff and requires non-price evidence for full 4B. C12 still needs a sharper sector-level condition because customer-contract headlines, AMPC/IRA labels, or parent turnaround language can look like Stage2-Actionable while the true bottleneck is customer call-off, utilization, and working-capital conversion. In practice the model needs to separate three states: (1) signed or talked-about customer framework, (2) actual call-off/order cadence and utilization stabilization, and (3) cash conversion after inventories and capex absorb the contract.

```jsonl
{"row_type": "score_simulation", "axis": "C12_customer_calloff_utilization_bridge", "before_profile": "e2r_2_1_stock_web_calibrated", "candidate_shadow_rule": "require customer call-off/order cadence or utilization evidence before Stage3-Yellow for C12", "expected_effect": "reduce LGES/LG화학 style false positives without deleting SKC local MFE cases"}
{"row_type": "score_simulation", "axis": "C12_parent_balance_sheet_guard", "before_profile": "e2r_2_1_stock_web_calibrated", "candidate_shadow_rule": "parent battery subsidiary turnaround cannot exceed Stage2 unless funding, customer volume, and margin bridge are present", "expected_effect": "caps SK이노베이션-like parent beta until battery-cash bridge clears"}
{"row_type": "score_simulation", "axis": "C12_local_mfe_preservation", "before_profile": "e2r_2_1_stock_web_calibrated", "candidate_shadow_rule": "allow local 4B/watch when restocking rally produces MFE but attach high-MAE guard and avoid Green", "expected_effect": "preserves SKC type tradeable rebound while preventing durable rerating label"}
```

## 7. Aggregate / residual contribution

```jsonl
{"row_type": "aggregate", "selected_round": "R3", "selected_loop": 102, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "new_independent_case_count": 4, "reused_case_count": 0, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "calibration_usable_case_count": 4, "calibration_usable_trigger_count": 4, "positive_case_count": 1, "mixed_positive_count": 1, "counterexample_count": 2, "local_4b_watch_count": 3, "current_profile_error_count": 4, "median_mfe_180d_pct": 7.33, "median_mae_180d_pct": -29.11, "auto_selected_coverage_gap_static_index": "C12 rows 16 -> 20 if accepted", "auto_selected_coverage_gap_conversation_local": "C12 rows 20 -> 24 if accepted; still Priority 0, need 6 to reach 30", "residual_contribution_label": "canonical_archetype_rule_candidate"}
{"row_type": "shadow_weight", "production_scoring_changed": false, "do_not_propose_new_weight_delta": false, "new_axis_proposed": ["C12_customer_calloff_utilization_cash_bridge_required", "C12_parent_battery_balance_sheet_drag_guard", "C12_local_mfe_high_MAE_split", "C12_signed_contract_without_calloff_stage3_cap", "C12_working_capital_inventory_absorption_required"], "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "high_MAE_guardrail"], "existing_axis_weakened": null}
{"row_type": "residual_contribution", "new_failure_mode": "battery customer contract/call-off label can precede utilization and cash conversion by multiple quarters", "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "why_global_rule_insufficient": "global price-only/4B guard catches pure spikes but does not distinguish signed framework, customer call-off cadence, inventory absorption, and parent balance-sheet contamination", "batch_implementation_hint": "implement as C12 shadow guard and not as broad C11/C13/C29 battery-sector penalty"}
```

## 8. Proposed C12-specific shadow rule

```text
C12_customer_calloff_utilization_cash_bridge_required:
  For C12, customer contract / supply agreement / AMPC / IRA / battery turnaround labels may produce Stage2-Actionable, but Stage3-Yellow requires at least one non-price bridge: customer call-off volume, utilization stabilization, shipment/revenue cadence, or working-capital/inventory absorption evidence.
C12_parent_battery_balance_sheet_drag_guard:
  Parent-company battery subsidiary exposure cannot reach Stage3-Green unless battery losses/funding needs and parent balance-sheet drag are explicitly resolved.
C12_local_mfe_high_MAE_split:
  If 30~90D MFE is strong but MAE exceeds -25%, keep as local 4B/watch rather than durable Stage3 unless customer cadence evidence appears.
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent. Do not rerun research. Ingest this MD as a v12 residual research artifact only after batch review. Extract JSONL rows with row_type in [case, trigger, score_simulation, aggregate, shadow_weight, residual_contribution]. Do not modify production scoring directly. If accepted, map proposed axes to C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK shadow rules and test against existing v12 validation rows. Preserve stock-web price_basis=tradable_raw and block corporate-action contaminated windows by default.
```

## 10. Next research state

```text
completed_round = R3
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_third_pass_to_30, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
