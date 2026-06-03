# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C02 — Power-grid transformer / data-center CAPEX orderbook-capacity guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX
fine_archetype_id: TRANSFORMER_ORDERBOOK_CAPACITY_MARGIN_4B_GUARD
loop_objective: coverage_gap_fill|canonical_not_listed_in_index_table|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|grid_orderbook_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX_transformer_orderbook_capacity_4b_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX is not listed in the visible archetype coverage table of V12_Research_No_Repeat_Index.md lines 45~90.
Therefore this run treats C02 as a coverage gap and uses new hard keys:
C02 + 267260 + Stage2-Actionable + 2024-01-23
C02 + 010120 + 4B-local-price-only + 2024-05-24
C02 + 103590 + Stage3-Yellow + 2024-05-29
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
267260 HD현대일렉트릭: selected 2024 forward window clean; corporate-action candidates end in 2019 and are outside selected test window.
010120 LS ELECTRIC: selected 2024 forward window clean; corporate-action candidates are historical and outside selected test window.
103590 일진전기: selected post-2024-02-13 forward window clean; corporate-action candidate is before selected trigger window.
```

## 3. Research thesis

C02 should distinguish fresh transformer/grid orderbook evidence from already-capitalized capacity optionality:

```text
power grid / data-center CAPEX demand
→ signed transformer orderbook and customer quality
→ capacity allocation and delivery schedule
→ ASP/mix and input-cost pass-through
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A transformer backlog is a queue at the factory gate. Stage2 can buy the queue when capacity is scarce and margins are still being revised upward; Green should require the queue to become delivery, ASP/mix and margin revision, not just a higher queue multiple.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C02_267260_HDELECTRIC_20240123_TRANSFORMER_ORDERBOOK_STAGE2 | 267260 | positive_transformer_orderbook_capacity_margin_stage2_success_with_later_4b_refresh | 2024-01-23 | 100000 | 374500 on 2024-07-24 | 96000 on 2024-01-24 | 43.5% | 214.0% | 274.5% | -4.0% | -39.79% |
| C02_010120_LSELECTRIC_20240524_GRID_CAPEX_PRICE_PREMIUM_4B | 010120 | grid_capex_equipment_price_premium_counterexample | 2024-05-24 | 231000 | 274500 on 2024-07-24 | 126200 on 2024-09-09 | 5.63% | 18.83% | 18.83% | -45.37% | -54.03% |
| C02_103590_ILJINELEC_20240529_TRANSFORMER_CABLE_FALSE_GREEN | 103590 | transformer_cable_orderbook_false_green_counterexample | 2024-05-29 | 28600 | 30250 on 2024-05-29 | 16600 on 2024-09-09 | 5.77% | 5.77% | 5.77% | -41.96% | -45.12% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 267260 is the positive anchor. The January 2024 transformer orderbook/capacity route produced very large MFE before the July premium required 4B refresh discipline.
- Stage2 is allowed only when grid/data-center demand is connected to orderbook quality, capacity allocation, delivery schedule, ASP/mix and margin/revision visibility.

### Stage3 / Green
- C02 Green should require signed orderbook quality, customer delivery schedule, capacity allocation, ASP/mix, input-cost pass-through and margin/revision confirmation.
- 103590 is the false-Green guard: transformer/cable price confirmation was visible, but the May 2024 premium had small residual upside and later a much larger MAE once incremental order-to-margin evidence failed to refresh.

### 4B
- 010120 fills the grid-capex equipment price-premium pocket. The theme and orderbook were real, but the May 2024 price already paid for too much capacity optionality.
- 103590 shows the same problem in transformer/cable beta: a real grid story can become local 4B when revisions no longer accelerate enough for the price already paid.
- 267260 also demonstrates that a valid Stage2 can transition into 4B once the rerating has capitalized the orderbook.

### 4C
- No hard contract cancellation, capacity failure or accounting break is asserted.
- The C02 break mode is evidence exhaustion: orderbook optionality may remain real, but incremental delivery cadence, ASP/mix and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C02_010120_LSELECTRIC_20240524_GRID_CAPEX_PRICE_PREMIUM_4B": {
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
  "C02_103590_ILJINELEC_20240529_TRANSFORMER_CABLE_FALSE_GREEN": {
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
  "C02_267260_HDELECTRIC_20240123_TRANSFORMER_ORDERBOOK_STAGE2": {
    "ASP_mix_input_cost_bridge": 8,
    "capacity_allocation_tightness": 10,
    "delivery_schedule_visibility": 8,
    "grid_capex_demand_visibility": 11,
    "information_confidence": 4,
    "margin_revision_bridge": 9,
    "market_mispricing": 10,
    "total": 78,
    "transformer_orderbook_quality": 10,
    "valuation_rerating_runway": 8
  }
}
```

## 7. Current calibrated profile stress test

Suggested C02 guard:
```text
if grid_transformer_orderbook and capacity_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if transformer_grid_price_premium and no incremental_order_delivery_ASP_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and orderbook_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 010120 / 2024-05-24: grid-capex equipment premium can be over-promoted if the model treats price heat as fresh delivery and margin proof.
- 103590 / 2024-05-29: transformer/cable confirmation can look like Yellow-to-Green, but fails without renewed capacity, delivery and margin bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -4.0, "MAE_30D_pct": -4.0, "MAE_90D_pct": -4.0, "MFE_180D_pct": 274.5, "MFE_30D_pct": 43.5, "MFE_90D_pct": 214.0, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX", "case_id": "C02_267260_HDELECTRIC_20240123_TRANSFORMER_ORDERBOOK_STAGE2", "case_role": "positive_transformer_orderbook_capacity_margin_stage2_success_with_later_4b_refresh", "company_name": "HD현대일렉트릭", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2017-11-17, 2017-11-28, 2017-12-11, 2018-11-23, 2018-12-18, 2019-12-30 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when transformer/order backlog, capacity tightness and margin leverage were visible before the rerating was fully capitalized. Green still requires order quality, delivery schedule, capacity allocation, ASP/mix, input cost and margin/revision bridge; after the July 2024 premium, the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -39.79, "entry_date": "2024-01-23", "entry_price": 100000, "evidence_family": "power_grid_transformer_data_center_capex_backlog_capacity_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "TRANSFORMER_ORDERBOOK_CAPACITY_MARGIN_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-01-24", "low_price_180d": 96000, "peak_date": "2024-07-24", "peak_price": 374500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/267/267260.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 8, "capacity_allocation_tightness": 10, "delivery_schedule_visibility": 8, "grid_capex_demand_visibility": 11, "information_confidence": 4, "margin_revision_bridge": 9, "market_mispricing": 10, "total": 78, "transformer_orderbook_quality": 10, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C02_267260_HDELECTRIC_20240123_TRANSFORMER_ORDERBOOK_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["power_grid_or_data_center_capex_visibility", "transformer_orderbook_and_capacity_tightness", "delivery_schedule_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["signed_orderbook_and_customer_quality_required", "capacity_allocation_delivery_schedule_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["grid_transformer_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "capacity_or_input_cost_margin_bridge_failure", "revision_momentum_break"], "symbol": "267260", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv", "trigger_date": "2024-01-23", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.37, "MAE_30D_pct": -19.91, "MAE_90D_pct": -45.37, "MFE_180D_pct": 18.83, "MFE_30D_pct": 5.63, "MFE_90D_pct": 18.83, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX", "case_id": "C02_010120_LSELECTRIC_20240524_GRID_CAPEX_PRICE_PREMIUM_4B", "case_role": "grid_capex_equipment_price_premium_counterexample", "company_name": "LS ELECTRIC", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 1995-09-28, 1999-04-08, 1999-07-26, 2003-04-16 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Grid-capex equipment price premium should route to local 4B or counterexample when the stock has already capitalized order/capacity optionality and incremental delivery schedule, ASP/mix, capacity allocation and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -54.03, "entry_date": "2024-05-24", "entry_price": 231000, "evidence_family": "grid_equipment_price_premium_without_incremental_order_capacity_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "TRANSFORMER_ORDERBOOK_CAPACITY_MARGIN_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-09-09", "low_price_180d": 126200, "peak_date": "2024-07-24", "peak_price": 274500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010120.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 4, "capacity_allocation_tightness": 5, "delivery_schedule_visibility": 4, "grid_capex_demand_visibility": 8, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "total": 38, "transformer_orderbook_quality": 6, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C02_010120_LSELECTRIC_20240524_GRID_CAPEX_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["power_grid_or_data_center_capex_visibility", "transformer_orderbook_and_capacity_tightness", "delivery_schedule_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["signed_orderbook_and_customer_quality_required", "capacity_allocation_delivery_schedule_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["grid_transformer_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "capacity_or_input_cost_margin_bridge_failure", "revision_momentum_break"], "symbol": "010120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "trigger_date": "2024-05-24", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.96, "MAE_30D_pct": -19.23, "MAE_90D_pct": -41.96, "MFE_180D_pct": 5.77, "MFE_30D_pct": 5.77, "MFE_90D_pct": 5.77, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX", "case_id": "C02_103590_ILJINELEC_20240529_TRANSFORMER_CABLE_FALSE_GREEN", "case_role": "transformer_cable_orderbook_false_green_counterexample", "company_name": "일진전기", "corporate_action_window_status": "selected post-2024-02-13 forward window clean; corporate-action candidate is 2024-02-13 and before selected trigger window", "current_profile_error": true, "current_profile_verdict": "Transformer/cable price confirmation should remain Yellow or local 4B when the market has already capitalized capacity/order optionality and incremental delivery cadence, capacity allocation, ASP/mix and margin/revision evidence do not refresh.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.12, "entry_date": "2024-05-29", "entry_price": 28600, "evidence_family": "transformer_cable_price_confirmation_without_incremental_capacity_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "TRANSFORMER_ORDERBOOK_CAPACITY_MARGIN_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-09-09", "low_price_180d": 16600, "peak_date": "2024-05-29", "peak_price": 30250, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/103/103590.json", "raw_component_score_breakdown": {"ASP_mix_input_cost_bridge": 4, "capacity_allocation_tightness": 5, "delivery_schedule_visibility": 4, "grid_capex_demand_visibility": 8, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "total": 37, "transformer_orderbook_quality": 5, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C02_103590_ILJINELEC_20240529_TRANSFORMER_CABLE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["power_grid_or_data_center_capex_visibility", "transformer_orderbook_and_capacity_tightness", "delivery_schedule_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["signed_orderbook_and_customer_quality_required", "capacity_allocation_delivery_schedule_required", "ASP_mix_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["grid_transformer_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_delivery_gap", "capacity_or_input_cost_margin_bridge_failure", "revision_momentum_break"], "symbol": "103590", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv", "trigger_date": "2024-05-29", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TRANSFORMER_ORDERBOOK_CAPACITY_MARGIN_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "grid_transformer_orderbook_capacity_data_center_capex_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C02 grid/transformer rows should allow Stage2 when orderbook quality, capacity tightness, delivery schedule, ASP/mix and margin-revision bridge are visible, but should route to local 4B/Yellow when price already capitalizes capacity optionality and incremental order-to-margin evidence has not refreshed.",
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
3. Add C02-specific power-grid / transformer orderbook / capacity allocation / delivery schedule / ASP-mix / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C02_STAGE2_ALLOWED_ON_ORDERBOOK_CAPACITY_DELIVERY_MARGIN_REVISION_BRIDGE
- C02_GREEN_REQUIRES_CUSTOMER_ORDERBOOK_DELIVERY_ASP_MIX_REVISION
- C02_TRANSFORMER_GRID_PRICE_PREMIUM_LOCAL_4B
- C02_PRICE_CONFIRMATION_WITHOUT_INCREMENTAL_ORDER_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_TRANSFORMER_DATA_CENTER_CAPEX.

