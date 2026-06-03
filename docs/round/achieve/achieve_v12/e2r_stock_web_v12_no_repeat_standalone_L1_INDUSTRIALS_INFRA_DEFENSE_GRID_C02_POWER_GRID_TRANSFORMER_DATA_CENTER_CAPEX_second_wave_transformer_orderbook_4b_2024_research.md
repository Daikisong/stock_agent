# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C02 — Power-grid transformer / second-wave orderbook-capacity 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX
fine_archetype_id: SECOND_WAVE_TRANSFORMER_ORDERBOOK_CAPACITY_4B_GUARD
loop_objective: coverage_gap_fill|canonical_not_listed_in_index_table|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_local_vs_full_window_split|grid_orderbook_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX_second_wave_transformer_orderbook_4b_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX is not listed in the visible archetype coverage table of V12_Research_No_Repeat_Index.md lines 45~90.
This run also avoids the previous local file's earlier C02 trigger dates by using second-wave July 2024 trigger keys:
C02 + 267260 + 4B-local-price-only + 2024-07-24
C02 + 010120 + Stage3-Yellow + 2024-07-24
C02 + 103590 + 4B-local-price-only + 2024-07-15
```

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
active_like_symbol_count: 2868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
267260 HD현대일렉트릭: selected 2024/2025 forward window clean; corporate-action candidates end in 2019 and are outside selected test window.
010120 LS ELECTRIC: selected 2024/2025 forward window clean; corporate-action candidates are historical and outside selected test window.
103590 일진전기: selected post-2024-02-13 forward window clean; corporate-action candidate is before selected trigger window.
```

## 3. Research thesis

C02 should split **fresh orderbook rerating** from **second-wave orderbook optionality already capitalized**:

```text
power grid / data-center CAPEX demand
→ signed transformer orderbook and customer quality
→ capacity allocation and delivery schedule
→ ASP/mix and input-cost pass-through
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A transformer orderbook is a factory queue. Stage2 can buy the queue when scarce capacity and margins are still being discovered. In the second wave, Green should require the next delivery slot, ASP/mix and revision bridge—not just a higher queue multiple.

## 4. Case table

| case_id | symbol | role | entry | entry_price | local_peak_90D | full_peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_90D | MAE_180D | local DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C02_267260_HDELECTRIC_20240724_TRANSFORMER_ORDERBOOK_SECOND_WAVE_4B | 267260 | protective_second_wave_transformer_orderbook_price_premium_4b_success | 2024-07-24 | 365500 | 374500 | 450000 on 2025-01-24 | 225500 on 2024-09-09 | 2.46% | 2.46% | 23.12% | -38.3% | -38.3% | -39.79% |
| C02_010120_LSELECTRIC_20240724_GRID_EQUIPMENT_SECOND_WAVE_FALSE_GREEN | 010120 | grid_equipment_second_wave_false_green_counterexample | 2024-07-24 | 260000 | 274500 | 303500 on 2025-02-19 | 126200 on 2024-09-09 | 5.58% | 5.58% | 16.73% | -51.46% | -51.46% | -54.03% |
| C02_103590_ILJINELEC_20240715_TRANSFORMER_CABLE_SECOND_WAVE_4B | 103590 | transformer_cable_second_wave_price_premium_counterexample | 2024-07-15 | 29400 | 30200 | 37550 on 2025-01-24 | 16600 on 2024-09-09 | 2.72% | 2.72% | 27.72% | -43.54% | -43.54% | -45.03% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean fresh Stage2/Green positive. 267260 is a **protective 4B success**, not a fresh Stage2 row.
- C02 Green should require signed orderbook quality, customer delivery schedule, capacity allocation, ASP/mix, input-cost pass-through and margin/revision confirmation.
- 010120 is the false-Green/Yellow guard: the second-wave grid-equipment move had a later full-window recovery, but the local path first suffered a large drawdown that Green should have guarded against.

### 4B
- 267260 is the protective local 4B anchor. The full window later reached a higher peak, but the local 4B drawdown was severe before that recovery.
- 010120 and 103590 show the same second-wave problem in grid-equipment and transformer/cable beta: a real grid story can become local 4B when price has already paid for orderbook optionality.
- This MD explicitly separates local 4B proximity from full-window peak behavior, because a later recovery should not erase a poor immediate trigger-quality signal.

### 4C
- No hard contract cancellation, capacity failure or accounting break is asserted.
- The C02 break mode is evidence exhaustion: orderbook optionality may remain real, but incremental delivery cadence, ASP/mix and margin revisions do not support the price already paid at the second-wave trigger.

## 6. Raw component score breakdown

```json
{
  "C02_010120_LSELECTRIC_20240724_GRID_EQUIPMENT_SECOND_WAVE_FALSE_GREEN": {
    "ASP_mix_input_cost_bridge": 4,
    "capacity_allocation_tightness": 5,
    "delivery_schedule_visibility": 4,
    "grid_capex_demand_visibility": 8,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "total": 38,
    "transformer_orderbook_quality": 6,
    "valuation_rerating_runway": 1
  },
  "C02_103590_ILJINELEC_20240715_TRANSFORMER_CABLE_SECOND_WAVE_4B": {
    "ASP_mix_input_cost_bridge": 4,
    "capacity_allocation_tightness": 5,
    "delivery_schedule_visibility": 4,
    "grid_capex_demand_visibility": 8,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "total": 37,
    "transformer_orderbook_quality": 5,
    "valuation_rerating_runway": 1
  },
  "C02_267260_HDELECTRIC_20240724_TRANSFORMER_ORDERBOOK_SECOND_WAVE_4B": {
    "ASP_mix_input_cost_bridge": 5,
    "capacity_allocation_tightness": 7,
    "delivery_schedule_visibility": 5,
    "grid_capex_demand_visibility": 10,
    "information_confidence": 3,
    "margin_revision_bridge": 4,
    "market_mispricing": 4,
    "total": 47,
    "transformer_orderbook_quality": 8,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C02 guard:
```text
if grid_transformer_orderbook and capacity_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if second_wave_transformer_price_premium and no incremental_order_delivery_ASP_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if local_4B_drawdown_large and later_full_window_recovery:
    preserve_local_4B_label = true
    do_not_relabel_as_fresh_stage2 = true
```

Residual errors:
```text
current_profile_error_count = 2
- 010120 / 2024-07-24: second-wave grid-equipment confirmation can be over-promoted if the model ignores local 4B proximity and waits for later full-window recovery.
- 103590 / 2024-07-15: transformer/cable price premium can look actionable, but fails locally without renewed capacity, delivery and margin bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -38.3, "MAE_30D_pct": -34.88, "MAE_90D_pct": -38.3, "MFE_180D_pct": 23.12, "MFE_30D_pct": 2.46, "MFE_90D_pct": 2.46, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX", "case_id": "C02_267260_HDELECTRIC_20240724_TRANSFORMER_ORDERBOOK_SECOND_WAVE_4B", "case_role": "protective_second_wave_transformer_orderbook_price_premium_4b_success", "company_name": "HD현대일렉트릭", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidates end in 2019 and are outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when transformer orderbook/capacity optionality had already been heavily capitalized. The full 180D window later produced a higher peak, but the immediate path first showed a large local drawdown; Green needed renewed delivery schedule, capacity allocation, ASP/mix and margin/revision evidence rather than price premium alone.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.11, "entry_date": "2024-07-24", "entry_price": 365500, "evidence_family": "second_wave_transformer_orderbook_price_premium_without_incremental_capacity_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_TRANSFORMER_ORDERBOOK_CAPACITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "local_drawdown_after_local_peak_pct": -39.79, "local_peak_90D_price": 374500, "low_date_180d": "2024-09-09", "low_price_180d": 225500, "peak_date": "2025-01-24", "peak_price": 450000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/267/267260.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 5, "capacity_allocation_tightness": 7, "delivery_schedule_visibility": 5, "grid_capex_demand_visibility": 10, "information_confidence": 3, "margin_revision_bridge": 4, "market_mispricing": 4, "total": 47, "transformer_orderbook_quality": 8, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C02_267260_HDELECTRIC_20240724_TRANSFORMER_ORDERBOOK_SECOND_WAVE_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_power_grid_or_data_center_capex_visibility", "transformer_orderbook_capacity_optional_value_already_capitalized", "incremental_delivery_ASP_mix_margin_revision_route_required"], "stage3_evidence_fields": ["signed_orderbook_and_customer_quality_required", "capacity_allocation_delivery_schedule_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["second_wave_grid_transformer_price_premium", "orderbook_optional_value_already_capitalized", "local_post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "capacity_or_input_cost_margin_bridge_failure", "revision_momentum_break"], "symbol": "267260", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv", "trigger_date": "2024-07-24", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -51.46, "MAE_30D_pct": -51.46, "MAE_90D_pct": -51.46, "MFE_180D_pct": 16.73, "MFE_30D_pct": 5.58, "MFE_90D_pct": 5.58, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX", "case_id": "C02_010120_LSELECTRIC_20240724_GRID_EQUIPMENT_SECOND_WAVE_FALSE_GREEN", "case_role": "grid_equipment_second_wave_false_green_counterexample", "company_name": "LS ELECTRIC", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidates are historical and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Grid-equipment second-wave price confirmation should remain Yellow or local 4B when the market has already capitalized order/capacity optionality and incremental delivery, ASP/mix, capacity allocation and margin/revision evidence have not refreshed. The row demonstrates why local 4B proximity must be split from a later full-window recovery.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.63, "entry_date": "2024-07-24", "entry_price": 260000, "evidence_family": "second_wave_grid_equipment_price_confirmation_without_incremental_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_TRANSFORMER_ORDERBOOK_CAPACITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "local_drawdown_after_local_peak_pct": -54.03, "local_peak_90D_price": 274500, "low_date_180d": "2024-09-09", "low_price_180d": 126200, "peak_date": "2025-02-19", "peak_price": 303500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010120.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 4, "capacity_allocation_tightness": 5, "delivery_schedule_visibility": 4, "grid_capex_demand_visibility": 8, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "total": 38, "transformer_orderbook_quality": 6, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C02_010120_LSELECTRIC_20240724_GRID_EQUIPMENT_SECOND_WAVE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_power_grid_or_data_center_capex_visibility", "transformer_orderbook_capacity_optional_value_already_capitalized", "incremental_delivery_ASP_mix_margin_revision_route_required"], "stage3_evidence_fields": ["signed_orderbook_and_customer_quality_required", "capacity_allocation_delivery_schedule_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["second_wave_grid_transformer_price_premium", "orderbook_optional_value_already_capitalized", "local_post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "capacity_or_input_cost_margin_bridge_failure", "revision_momentum_break"], "symbol": "010120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "trigger_date": "2024-07-24", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -43.54, "MAE_30D_pct": -38.78, "MAE_90D_pct": -43.54, "MFE_180D_pct": 27.72, "MFE_30D_pct": 2.72, "MFE_90D_pct": 2.72, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX", "case_id": "C02_103590_ILJINELEC_20240715_TRANSFORMER_CABLE_SECOND_WAVE_4B", "case_role": "transformer_cable_second_wave_price_premium_counterexample", "company_name": "일진전기", "corporate_action_window_status": "selected post-2024-02-13 forward window clean; corporate-action candidate is before selected trigger window", "current_profile_error": true, "current_profile_verdict": "Transformer/cable second-wave price premium should route to local 4B or counterexample unless incremental orderbook, delivery cadence, capacity allocation, ASP/mix and margin/revision evidence refresh. The stock later recovered, but the immediate 4B path was a severe drawdown before any later full-window peak.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.27, "entry_date": "2024-07-15", "entry_price": 29400, "evidence_family": "second_wave_transformer_cable_price_premium_without_incremental_capacity_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_TRANSFORMER_ORDERBOOK_CAPACITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "local_drawdown_after_local_peak_pct": -45.03, "local_peak_90D_price": 30200, "low_date_180d": "2024-09-09", "low_price_180d": 16600, "peak_date": "2025-01-24", "peak_price": 37550, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/103/103590.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 4, "capacity_allocation_tightness": 5, "delivery_schedule_visibility": 4, "grid_capex_demand_visibility": 8, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "total": 37, "transformer_orderbook_quality": 5, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C02_103590_ILJINELEC_20240715_TRANSFORMER_CABLE_SECOND_WAVE_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["second_wave_power_grid_or_data_center_capex_visibility", "transformer_orderbook_capacity_optional_value_already_capitalized", "incremental_delivery_ASP_mix_margin_revision_route_required"], "stage3_evidence_fields": ["signed_orderbook_and_customer_quality_required", "capacity_allocation_delivery_schedule_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["second_wave_grid_transformer_price_premium", "orderbook_optional_value_already_capitalized", "local_post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "capacity_or_input_cost_margin_bridge_failure", "revision_momentum_break"], "symbol": "103590", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv", "trigger_date": "2024-07-15", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SECOND_WAVE_TRANSFORMER_ORDERBOOK_CAPACITY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "second_wave_grid_transformer_orderbook_capacity_local_4b_full_window_split",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C02 second-wave grid/transformer rows should split local 4B proximity from full-window recovery: after orderbook optionality is capitalized, Green requires incremental delivery schedule, capacity allocation, ASP/mix and margin-revision evidence, not price confirmation alone.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C02 + symbol + trigger_type + entry_date.
3. Preserve local 4B proximity even when the full forward window later recovers.
4. Add C02-specific second-wave transformer / grid orderbook / capacity allocation / delivery schedule / ASP-mix / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C02_STAGE2_ALLOWED_ON_ORDERBOOK_CAPACITY_DELIVERY_MARGIN_REVISION_BRIDGE
- C02_GREEN_REQUIRES_CUSTOMER_ORDERBOOK_DELIVERY_ASP_MIX_REVISION
- C02_SECOND_WAVE_TRANSFORMER_GRID_PRICE_PREMIUM_LOCAL_4B
- C02_LOCAL_4B_DRAWDOWN_NOT_ERASED_BY_LATER_FULL_WINDOW_RECOVERY

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX.

