# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C11 — Battery orderbook rerating / CNT-silicon-anode-equipment 4B guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: CNT_SILICON_ANODE_EQUIPMENT_ORDERBOOK_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_cnt_anode_equipment_orderbook_2023_research.md
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

This run avoids those top-covered C11 symbols and adds 121600, 078600, and 222080.  
Each row uses a new `C11 + symbol + trigger_type + entry_date` hard key.

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
121600 나노신소재: selected 2023 forward window clean; corporate-action candidate is 2015-12-17, outside selected test window.
078600 대주전자재료: corporate_action_candidate_count=0.
222080 씨아이에스: selected 2023 forward window clean; corporate-action candidate is 2017-01-20, outside selected test window.
```

## 3. Research thesis

C11 should distinguish a fresh battery orderbook rerating from an already-capitalized customer/orderbook option:

```text
battery orderbook / customer allocation attention
→ customer call-off and allocation share
→ capacity ramp, utilization or delivery acceptance
→ ASP/mix, input-cost pass-through and working-capital quality
→ gross margin and revision bridge
→ rerating or local 4B cap
```

An orderbook is a reservation book. Stage2 can buy the moment reservations become credible production, but Green should require the customer to call off volume, the line to run, and the invoice to survive cost and yield pressure.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C11_121600_NANONEWMAT_20230209_CNT_ADDITIVE_ORDERBOOK_STAGE2 | 121600 | positive_cnt_conductive_additive_orderbook_stage2_success_with_later_4b_refresh | 2023-02-09 | 109200 | 193700 on 2023-04-10 | 91600 on 2023-02-09 | 49.54% | 77.38% | 77.38% | -16.12% | -41.35% |
| C11_078600_DAEJOO_20230718_SILICON_ANODE_ORDERBOOK_PREMIUM_4B | 078600 | silicon_anode_orderbook_price_premium_counterexample | 2023-07-18 | 115800 | 117500 on 2023-07-26 | 67500 on 2023-11-01 | 1.47% | 1.47% | 1.47% | -41.71% | -42.55% |
| C11_222080_CIS_20230330_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_GREEN | 222080 | battery_equipment_orderbook_false_green_counterexample | 2023-03-30 | 14630 | 16440 on 2023-03-30 | 8970 on 2023-10-31 | 12.37% | 12.37% | 12.37% | -38.69% | -45.44% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 121600 is the positive anchor. The February 2023 CNT conductive-additive orderbook/capacity route produced a large MFE before the April premium required 4B discipline.
- Stage2 is allowed only when non-price evidence connects the orderbook to customer allocation, call-off cadence, capacity ramp, utilization and revision visibility.

### Stage3 / Green
- C11 Green should require customer call-off, allocation share, capacity ramp, delivery acceptance, ASP/mix, input-cost pass-through, working-capital quality and margin/revision confirmation.
- 222080 is the false-Green guard: equipment-orderbook price confirmation did not by itself prove delivery acceptance, revenue recognition cadence, working-capital quality or margin revision.

### 4B
- 078600 fills the silicon-anode 4B pocket. The July 2023 premium had almost no additional upside and then drew down as call-off, capacity/utilization and margin evidence did not refresh.
- 222080 shows the equipment-orderbook version of the same failure: orderbook salience without delivery/margin conversion became a large 180D MAE.
- 121600 also demonstrates that valid Stage2 evidence can become local 4B after the rerating has already capitalized the orderbook.

### 4C
- No hard customer cancellation, plant impairment or accounting break is asserted.
- The C11 break mode is orderbook-to-call-off exhaustion: the orderbook may remain plausible, but customer call-off, utilization, delivery acceptance, working capital and margin revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C11_078600_DAEJOO_20230718_SILICON_ANODE_ORDERBOOK_PREMIUM_4B": {
    "ASP_mix_and_input_cost": 3,
    "capacity_ramp_and_calloff": 3,
    "customer_orderbook_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "total": 22,
    "valuation_rerating_runway": 1
  },
  "C11_121600_NANONEWMAT_20230209_CNT_ADDITIVE_ORDERBOOK_STAGE2": {
    "ASP_mix_and_input_cost": 8,
    "capacity_ramp_and_calloff": 9,
    "customer_orderbook_visibility": 10,
    "information_confidence": 4,
    "margin_revision_bridge": 8,
    "market_mispricing": 10,
    "total": 57,
    "valuation_rerating_runway": 8
  },
  "C11_222080_CIS_20230330_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_GREEN": {
    "ASP_mix_and_input_cost": 3,
    "capacity_ramp_and_calloff": 3,
    "customer_orderbook_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 21,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C11 guard:
```text
if battery_orderbook and customer_calloff_capacity_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if battery_orderbook_price_premium and no incremental_calloff_utilization_ASP_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if equipment_orderbook_confirmation and no delivery_acceptance_working_capital_margin_bridge:
    keep_stage3_yellow_or_counterexample = true
```

Residual errors:
```text
current_profile_error_count = 2
- 078600 / 2023-07-18: silicon-anode orderbook premium can be over-promoted if the model treats price premium as call-off and margin proof.
- 222080 / 2023-03-30: battery-equipment orderbook confirmation can look like Green, but fails without delivery acceptance, revenue cadence and working-capital bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -16.12, "MAE_30D_pct": -16.12, "MAE_90D_pct": -16.12, "MFE_180D_pct": 77.38, "MFE_30D_pct": 49.54, "MFE_90D_pct": 77.38, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_121600_NANONEWMAT_20230209_CNT_ADDITIVE_ORDERBOOK_STAGE2", "case_role": "positive_cnt_conductive_additive_orderbook_stage2_success_with_later_4b_refresh", "company_name": "나노신소재", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2015-12-17 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when CNT conductive-additive orderbook and capacity-expansion visibility separated from generic battery beta before the rerating was fully capitalized. Green still requires customer allocation, call-off cadence, utilization, ASP/mix, capex ramp and margin/revision bridge; after the April 2023 premium the same evidence required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.35, "entry_date": "2023-02-09", "entry_price": 109200, "evidence_family": "cnt_conductive_additive_customer_orderbook_capacity_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "CNT_SILICON_ANODE_EQUIPMENT_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-02-09", "low_price_180d": 91600, "peak_date": "2023-04-10", "peak_price": 193700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/121/121600.json", "raw_component_score_breakdown": {"ASP_mix_and_input_cost": 8, "capacity_ramp_and_calloff": 9, "customer_orderbook_visibility": 10, "information_confidence": 4, "margin_revision_bridge": 8, "market_mispricing": 10, "total": 57, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C11_121600_NANONEWMAT_20230209_CNT_ADDITIVE_ORDERBOOK_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_or_customer_allocation_attention", "capacity_ramp_or_delivery_schedule_visibility", "calloff_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_allocation_required", "capacity_ramp_delivery_acceptance_required", "ASP_mix_input_cost_working_capital_margin_revision_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "rerating_or_contract_option_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_calloff_gap", "delivery_acceptance_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "121600", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2023.csv", "trigger_date": "2023-02-09", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.71, "MAE_30D_pct": -26.25, "MAE_90D_pct": -41.71, "MFE_180D_pct": 1.47, "MFE_30D_pct": 1.47, "MFE_90D_pct": 1.47, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_078600_DAEJOO_20230718_SILICON_ANODE_ORDERBOOK_PREMIUM_4B", "case_role": "silicon_anode_orderbook_price_premium_counterexample", "company_name": "대주전자재료", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2023_forward_window", "current_profile_error": true, "current_profile_verdict": "Silicon-anode orderbook price premium should route to local 4B or counterexample when the stock has already capitalized the customer/orderbook option and incremental call-off, utilization, ASP/mix, yield and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.55, "entry_date": "2023-07-18", "entry_price": 115800, "evidence_family": "silicon_anode_customer_orderbook_price_premium_without_incremental_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CNT_SILICON_ANODE_EQUIPMENT_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-01", "low_price_180d": 67500, "peak_date": "2023-07-26", "peak_price": 117500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/078/078600.json", "raw_component_score_breakdown": {"ASP_mix_and_input_cost": 3, "capacity_ramp_and_calloff": 3, "customer_orderbook_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "total": 22, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C11_078600_DAEJOO_20230718_SILICON_ANODE_ORDERBOOK_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_or_customer_allocation_attention", "capacity_ramp_or_delivery_schedule_visibility", "calloff_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_allocation_required", "capacity_ramp_delivery_acceptance_required", "ASP_mix_input_cost_working_capital_margin_revision_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "rerating_or_contract_option_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_calloff_gap", "delivery_acceptance_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "078600", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078600/2023.csv", "trigger_date": "2023-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.69, "MAE_30D_pct": -9.77, "MAE_90D_pct": -13.06, "MFE_180D_pct": 12.37, "MFE_30D_pct": 12.37, "MFE_90D_pct": 12.37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_222080_CIS_20230330_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_GREEN", "case_role": "battery_equipment_orderbook_false_green_counterexample", "company_name": "씨아이에스", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2017-01-20 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Battery-equipment orderbook confirmation should stay Yellow when price confirmation is not followed by delivery schedule, customer acceptance, revenue recognition cadence, working-capital quality, input-cost pass-through and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.44, "entry_date": "2023-03-30", "entry_price": 14630, "evidence_family": "battery_equipment_orderbook_price_confirmation_without_delivery_acceptance_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CNT_SILICON_ANODE_EQUIPMENT_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 8970, "peak_date": "2023-03-30", "peak_price": 16440, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/222/222080.json", "raw_component_score_breakdown": {"ASP_mix_and_input_cost": 3, "capacity_ramp_and_calloff": 3, "customer_orderbook_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 21, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C11_222080_CIS_20230330_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_or_customer_allocation_attention", "capacity_ramp_or_delivery_schedule_visibility", "calloff_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_allocation_required", "capacity_ramp_delivery_acceptance_required", "ASP_mix_input_cost_working_capital_margin_revision_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "rerating_or_contract_option_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_calloff_gap", "delivery_acceptance_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "222080", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/222/222080/2023.csv", "trigger_date": "2023-03-30", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CNT_SILICON_ANODE_EQUIPMENT_ORDERBOOK_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_orderbook_rerating_cnt_silicon_anode_equipment_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C11 battery orderbook rows should allow Stage2 when customer allocation/orderbook evidence is backed by call-off cadence, capacity ramp, utilization, ASP/mix and margin/revision bridge, but route price-premium or equipment-orderbook confirmation to local 4B/Yellow when delivery, acceptance, working-capital and margin evidence have not refreshed.",
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
3. Add C11-specific battery orderbook / customer call-off / capacity ramp / utilization / delivery acceptance / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C11_STAGE2_ALLOWED_ON_ORDERBOOK_CALLOFF_CAPACITY_MARGIN_REVISION_BRIDGE
- C11_GREEN_REQUIRES_CUSTOMER_ALLOCATION_UTILIZATION_DELIVERY_ACCEPTANCE_REVISION
- C11_ORDERBOOK_PRICE_PREMIUM_LOCAL_4B
- C11_EQUIPMENT_ORDERBOOK_WITHOUT_DELIVERY_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

