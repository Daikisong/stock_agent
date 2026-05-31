# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C11 — Battery orderbook rerating / CNT-slurry and equipment 4B guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_STORAGE
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: CNT_SLURRY_EQUIPMENT_ORDERBOOK_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|battery_orderbook_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_STORAGE_C11_BATTERY_ORDERBOOK_RERATING_cnt_slurry_equipment_orderbook_4b_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C11_BATTERY_ORDERBOOK_RERATING current coverage:
rows=14, symbols=6, date range=2023-01-31~2024-06-24, good/bad S2=6/2, 4B/4C=0/1
top covered symbols: 247540(6), 003670(3), 348370(2), 066970(1), 373220(1)
```

This run avoids those top-covered C11 symbols and adds 121600, 222080, and 382480.  
Each row uses a new `C11 + symbol + trigger_type + entry_date` hard key:
```text
C11 + 121600 + Stage2-Actionable + 2023-01-31
C11 + 222080 + Stage3-Yellow + 2023-03-29
C11 + 382480 + 4B-local-price-only + 2023-04-04
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
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
```

Selected profiles:
```text
121600 나노신소재: selected post-2015 forward window clean; corporate-action candidate is 2015-12-17, outside selected trigger window.
222080 씨아이에스: selected post-2017 forward window clean; corporate-action candidate is 2017-01-20, outside selected trigger window.
382480 지아이텍: selected post-2022 forward window clean; corporate-action candidate is 2022-04-05, outside selected trigger window.
```

## 3. Research thesis

C11 should distinguish real battery orderbook rerating from orderbook-theme price premium already paid in price:

```text
battery orderbook / customer capacity expansion
→ customer quality and contract durability
→ shipment cadence and backlog conversion
→ capacity execution and working-capital control
→ ASP/mix and margin revision bridge
→ Stage2/Green or local 4B cap
```

A battery orderbook is a conveyor belt. Stage2 can buy when the belt is visibly loading—customer, shipment cadence, capacity and margin bridge. Green should not buy the sound of the belt after the market has already priced the next containers.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C11_121600_NANOMATERIAL_20230131_CNT_ORDERBOOK_RERATING_STAGE2 | 121600 | positive_CNT_conductive_additive_orderbook_rerating_stage2_success_with_later_4b_refresh | 2023-01-31 | 83700 | 193700 on 2023-04-10 | 82900 on 2023-01-31 | 95.1% | 131.42% | 131.42% | -0.96% | -41.35% |
| C11_222080_CIS_20230329_ELECTRODE_EQUIPMENT_ORDERBOOK_FALSE_GREEN | 222080 | electrode_equipment_orderbook_false_green_counterexample | 2023-03-29 | 13920 | 16440 on 2023-03-30 | 8970 on 2023-10-31 | 18.1% | 18.1% | 18.1% | -35.56% | -45.44% |
| C11_382480_GITECH_20230404_BATTERY_TOOLING_PRICE_PREMIUM_4B | 382480 | battery_tooling_orderbook_price_premium_4b_counterexample | 2023-04-04 | 5290 | 5590 on 2023-04-04 | 2800 on 2023-10-26 | 5.67% | 5.67% | 5.67% | -47.07% | -49.91% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 121600 is the positive anchor. The January 2023 CNT conductive-additive / customer-capacity route produced very strong MFE before the April 2023 premium required 4B refresh discipline.
- Stage2 is allowed only when battery orderbook salience maps to customer quality, capacity bridge, shipment cadence, ASP/mix and margin/revision visibility.
- 가격만 있는 early entry는 금지된다. This positive row is included because the trigger family is orderbook/customer-capacity evidence, not price-only momentum.

### Stage3 / Green
- C11 Green should require customer order quality, delivery cadence, backlog conversion, utilization/working-capital control, ASP/mix and margin/revision confirmation.
- 222080 is the false-Green/Yellow guard: electrode-equipment orderbook price confirmation was visible, but the March 2023 trigger had limited residual upside and a much larger forward MAE when orderbook-to-margin evidence did not refresh.

### 4B
- 382480 fills the battery tooling/equipment price-premium 4B pocket. The April 2023 trigger had almost no residual upside and a large full-window drawdown.
- 222080 shows the same failure in electrode-equipment form: the orderbook story can remain directionally real while the listed-company earnings bridge is too stale for Green.
- 121600 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the customer-capacity/orderbook option.

### 4C
- No hard customer call-off, order cancellation, delivery failure, liquidity break or accounting break is asserted.
- The C11 break mode here is orderbook-to-margin exhaustion: the battery orderbook story may remain directionally real, but incremental customer order, delivery cadence, utilization and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C11_121600_NANOMATERIAL_20230131_CNT_ORDERBOOK_RERATING_STAGE2": {
    "ASP_mix_margin_revision_bridge": 8,
    "battery_orderbook_visibility": 10,
    "capacity_execution_quality": 7,
    "customer_quality_or_capacity_bridge": 9,
    "information_confidence": 4,
    "market_mispricing": 9,
    "relative_strength_quality": 9,
    "shipment_cadence_backlog_conversion": 8,
    "total": 72,
    "valuation_rerating_runway": 8
  },
  "C11_222080_CIS_20230329_ELECTRODE_EQUIPMENT_ORDERBOOK_FALSE_GREEN": {
    "ASP_mix_margin_revision_bridge": 2,
    "battery_orderbook_visibility": 8,
    "capacity_execution_quality": 3,
    "customer_quality_or_capacity_bridge": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "relative_strength_quality": 5,
    "shipment_cadence_backlog_conversion": 3,
    "total": 33,
    "valuation_rerating_runway": 1
  },
  "C11_382480_GITECH_20230404_BATTERY_TOOLING_PRICE_PREMIUM_4B": {
    "ASP_mix_margin_revision_bridge": 2,
    "battery_orderbook_visibility": 7,
    "capacity_execution_quality": 2,
    "customer_quality_or_capacity_bridge": 3,
    "information_confidence": 3,
    "market_mispricing": 4,
    "relative_strength_quality": 5,
    "shipment_cadence_backlog_conversion": 3,
    "total": 30,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C11 guard:
```text
if battery_orderbook and customer_quality_capacity_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if battery_equipment_or_tooling_price_premium and no incremental_customer_order_delivery_utilization_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and orderbook_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 222080 / 2023-03-29: electrode-equipment orderbook confirmation can be over-promoted if price strength substitutes for refreshed delivery and margin proof.
- 382480 / 2023-04-04: battery tooling/orderbook premium can look actionable, but fails without renewed customer-quality and margin revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -0.96, "MAE_30D_pct": -0.96, "MAE_90D_pct": -0.96, "MFE_180D_pct": 131.42, "MFE_30D_pct": 95.1, "MFE_90D_pct": 131.42, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_121600_NANOMATERIAL_20230131_CNT_ORDERBOOK_RERATING_STAGE2", "case_role": "positive_CNT_conductive_additive_orderbook_rerating_stage2_success_with_later_4b_refresh", "company_name": "나노신소재", "corporate_action_window_status": "selected post-2015 forward window clean; profile corporate-action candidate is 2015-12-17 and outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when CNT conductive-additive demand, customer-capacity expansion, orderbook optionality and ASP/mix margin leverage were visible before the rerating was fully capitalized. Green still requires customer/order durability, capacity conversion, shipment cadence, margin/revision bridge and valuation runway; after the April 2023 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.35, "entry_date": "2023-01-31", "entry_price": 83700, "evidence_family": "battery_CNT_slurry_conductive_additive_customer_capacity_orderbook_rerating_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "CNT_SLURRY_EQUIPMENT_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-01-31", "low_price_180d": 82900, "peak_date": "2023-04-10", "peak_price": 193700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/121/121600.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 8, "battery_orderbook_visibility": 10, "capacity_execution_quality": 7, "customer_quality_or_capacity_bridge": 9, "information_confidence": 4, "market_mispricing": 9, "relative_strength_quality": 9, "shipment_cadence_backlog_conversion": 8, "total": 72, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C11_121600_NANOMATERIAL_20230131_CNT_ORDERBOOK_RERATING_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_visibility", "customer_quality_or_capacity_bridge", "shipment_cadence_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["customer_order_quality_required", "delivery_cadence_and_backlog_conversion_required", "utilization_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_order_gap", "delivery_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "121600", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2023.csv", "trigger_date": "2023-01-31", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -35.56, "MAE_30D_pct": -13.07, "MAE_90D_pct": -16.16, "MFE_180D_pct": 18.1, "MFE_30D_pct": 18.1, "MFE_90D_pct": 18.1, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_222080_CIS_20230329_ELECTRODE_EQUIPMENT_ORDERBOOK_FALSE_GREEN", "case_role": "electrode_equipment_orderbook_false_green_counterexample", "company_name": "씨아이에스", "corporate_action_window_status": "selected post-2017 forward window clean; profile corporate-action candidate is 2017-01-20 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Battery electrode-equipment orderbook price confirmation should remain Yellow or local 4B when price strength is not backed by fresh customer order quality, delivery cadence, capacity utilization, working-capital control and margin/revision evidence. The March 2023 trigger had limited residual MFE and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.44, "entry_date": "2023-03-29", "entry_price": 13920, "evidence_family": "battery_electrode_equipment_orderbook_price_confirmation_without_incremental_customer_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CNT_SLURRY_EQUIPMENT_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-10-31", "low_price_180d": 8970, "peak_date": "2023-03-30", "peak_price": 16440, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/222/222080.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 2, "battery_orderbook_visibility": 8, "capacity_execution_quality": 3, "customer_quality_or_capacity_bridge": 4, "information_confidence": 3, "market_mispricing": 4, "relative_strength_quality": 5, "shipment_cadence_backlog_conversion": 3, "total": 33, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C11_222080_CIS_20230329_ELECTRODE_EQUIPMENT_ORDERBOOK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_visibility", "customer_quality_or_capacity_bridge", "shipment_cadence_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["customer_order_quality_required", "delivery_cadence_and_backlog_conversion_required", "utilization_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_order_gap", "delivery_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "222080", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/222/222080/2023.csv", "trigger_date": "2023-03-29", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -47.07, "MAE_30D_pct": -14.84, "MAE_90D_pct": -27.88, "MFE_180D_pct": 5.67, "MFE_30D_pct": 5.67, "MFE_90D_pct": 5.67, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_382480_GITECH_20230404_BATTERY_TOOLING_PRICE_PREMIUM_4B", "case_role": "battery_tooling_orderbook_price_premium_4b_counterexample", "company_name": "지아이텍", "corporate_action_window_status": "selected post-2022 forward window clean; profile corporate-action candidate is 2022-04-05 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Battery tooling/orderbook premium should route to local 4B or counterexample when the market has already capitalized equipment optionality and fresh customer order, delivery cadence, utilization and margin/revision evidence do not refresh. The April 2023 trigger had almost no residual upside and a large full-window drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.91, "entry_date": "2023-04-04", "entry_price": 5290, "evidence_family": "battery_slot_die_tooling_orderbook_theme_price_premium_without_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CNT_SLURRY_EQUIPMENT_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-10-26", "low_price_180d": 2800, "peak_date": "2023-04-04", "peak_price": 5590, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/382/382480.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 2, "battery_orderbook_visibility": 7, "capacity_execution_quality": 2, "customer_quality_or_capacity_bridge": 3, "information_confidence": 3, "market_mispricing": 4, "relative_strength_quality": 5, "shipment_cadence_backlog_conversion": 3, "total": 30, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C11_382480_GITECH_20230404_BATTERY_TOOLING_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_visibility", "customer_quality_or_capacity_bridge", "shipment_cadence_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["customer_order_quality_required", "delivery_cadence_and_backlog_conversion_required", "utilization_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_order_gap", "delivery_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "382480", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/382/382480/2023.csv", "trigger_date": "2023-04-04", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CNT_SLURRY_EQUIPMENT_ORDERBOOK_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_STORAGE",
  "loop_contribution_label": "battery_orderbook_rerating_cnt_slurry_equipment_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C11 battery-orderbook rows should allow Stage2 when orderbook visibility maps to customer quality, capacity bridge, shipment cadence, ASP/mix and margin-revision evidence; equipment/tooling price premiums should route to Yellow/local 4B when the orderbook-to-margin bridge has not refreshed.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C11 + symbol + trigger_type + entry_date.
3. Add C11-specific battery orderbook / customer quality / capacity bridge / delivery cadence / utilization-working-capital / ASP-mix / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C11_STAGE2_ALLOWED_ON_CUSTOMER_CAPACITY_ORDERBOOK_MARGIN_REVISION_BRIDGE
- C11_GREEN_REQUIRES_CUSTOMER_ORDER_DELIVERY_UTILIZATION_ASP_MIX_REVISION
- C11_BATTERY_EQUIPMENT_TOOLING_PRICE_PREMIUM_LOCAL_4B
- C11_PRICE_CONFIRMATION_WITHOUT_ORDERBOOK_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_STORAGE/C11_BATTERY_ORDERBOOK_RERATING.

