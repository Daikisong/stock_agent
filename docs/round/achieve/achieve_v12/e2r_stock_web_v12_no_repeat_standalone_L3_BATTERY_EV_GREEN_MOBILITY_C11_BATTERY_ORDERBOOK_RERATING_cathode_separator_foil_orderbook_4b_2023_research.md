# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C11 — Battery orderbook rerating / cathode-separator-foil 4B guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: CATHODE_SEPARATOR_FOIL_ORDERBOOK_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|orderbook_to_calloff_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_cathode_separator_foil_orderbook_4b_2023_research.md
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

This run avoids those top-covered C11 symbols and adds 005070, 393890, and 006110.  
Each row uses a new `C11 + symbol + trigger_type + entry_date` hard key:
```text
C11 + 005070 + Stage2-Actionable + 2023-03-31
C11 + 393890 + 4B-local-price-only + 2023-07-26
C11 + 006110 + Stage3-Yellow + 2023-07-26
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
005070 코스모신소재: selected post-2019 forward window clean; historical corporate-action candidates outside selected test window.
393890 더블유씨피: corporate_action_candidate_count=0; clean 2023/2024 forward window.
006110 삼아알미늄: selected post-2023-02-09 forward window clean; prior corporate-action candidates outside selected trigger window.
```

## 3. Research thesis

C11 should split fresh battery orderbook discovery from late-cycle orderbook optionality already paid in price:

```text
battery cathode / separator / foil orderbook
→ customer contract quality and call-off cadence
→ delivery schedule and utilization ramp
→ ASP/input-cost pass-through and working-capital quality
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A battery orderbook is a reservation ledger. Stage2 can buy the ledger when reservations are turning into call-offs and margins. Green should require the customer to pull volume and the plant to earn the spread, not just a larger ledger multiple.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C11_005070_COSMOAMT_20230331_CATHODE_ORDERBOOK_RERATING_STAGE2 | 005070 | positive_cathode_orderbook_stage2_success_with_later_4b_refresh | 2023-03-31 | 153900 | 242500 on 2023-06-13 | 149000 on 2023-05-15 | 29.69% | 57.57% | 57.57% | -3.18% | -60.95% |
| C11_393890_WCP_20230726_SEPARATOR_ORDERBOOK_PREMIUM_4B | 393890 | separator_orderbook_capacity_price_premium_counterexample | 2023-07-26 | 75700 | 87700 on 2023-08-01 | 34350 on 2024-04-08 | 15.85% | 15.85% | 15.85% | -54.62% | -60.83% |
| C11_006110_SAMAAL_20230726_ALUMINUMFOIL_ORDERBOOK_FALSE_GREEN | 006110 | aluminum_foil_orderbook_false_green_counterexample | 2023-07-26 | 117300 | 135500 on 2023-07-26 | 80200 on 2024-01-25 | 15.52% | 15.52% | 15.52% | -31.63% | -40.81% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 005070 is the positive anchor. The March 2023 cathode orderbook/capacity route produced strong MFE before the later premium required 4B refresh discipline.
- Stage2 is allowed only when customer/orderbook salience maps to call-off, delivery schedule, utilization, ASP/input-cost and margin/revision visibility.

### Stage3 / Green
- C11 Green should require customer call-off and delivery schedule, utilization/capacity absorption, ASP/input-cost pass-through and margin/revision confirmation.
- 006110 is the false-Green/Yellow guard: aluminum-foil orderbook price confirmation was visible, but incremental call-off/utilization/margin evidence did not refresh enough to survive the forward path.

### 4B
- 393890 fills the separator orderbook price-premium 4B pocket. The July 2023 trigger had local upside but forward MAE overwhelmed the residual MFE.
- 006110 shows the foil version of the same failure: orderbook optionality can remain plausible while the price has already paid for too much without call-off and revision proof.
- 005070 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the orderbook pipeline.

### 4C
- No hard customer cancellation, plant failure, accounting break or financing break is asserted.
- The C11 break mode here is orderbook-to-calloff exhaustion: order visibility may remain real, but incremental call-off, utilization and margin revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C11_005070_COSMOAMT_20230331_CATHODE_ORDERBOOK_RERATING_STAGE2": {
    "ASP_input_cost_bridge": 7,
    "battery_orderbook_visibility": 10,
    "capacity_delivery_schedule": 8,
    "customer_contract_quality": 9,
    "information_confidence": 4,
    "margin_revision_bridge": 8,
    "market_mispricing": 9,
    "total": 70,
    "utilization_calloff_bridge": 8,
    "valuation_rerating_runway": 7
  },
  "C11_006110_SAMAAL_20230726_ALUMINUMFOIL_ORDERBOOK_FALSE_GREEN": {
    "ASP_input_cost_bridge": 3,
    "battery_orderbook_visibility": 7,
    "capacity_delivery_schedule": 4,
    "customer_contract_quality": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 32,
    "utilization_calloff_bridge": 3,
    "valuation_rerating_runway": 1
  },
  "C11_393890_WCP_20230726_SEPARATOR_ORDERBOOK_PREMIUM_4B": {
    "ASP_input_cost_bridge": 3,
    "battery_orderbook_visibility": 7,
    "capacity_delivery_schedule": 5,
    "customer_contract_quality": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 33,
    "utilization_calloff_bridge": 3,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C11 guard:
```text
if battery_orderbook and calloff_delivery_utilization_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if battery_orderbook_price_premium and no incremental_calloff_delivery_ASP_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and orderbook_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 393890 / 2023-07-26: separator orderbook premium can be over-promoted if price strength substitutes for customer call-off and margin proof.
- 006110 / 2023-07-26: aluminum-foil orderbook confirmation can look like Yellow-to-Green, but fails without renewed utilization and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -3.18, "MAE_30D_pct": -7.02, "MAE_90D_pct": -3.18, "MFE_180D_pct": 57.57, "MFE_30D_pct": 29.69, "MFE_90D_pct": 57.57, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_005070_COSMOAMT_20230331_CATHODE_ORDERBOOK_RERATING_STAGE2", "case_role": "positive_cathode_orderbook_stage2_success_with_later_4b_refresh", "company_name": "코스모신소재", "corporate_action_window_status": "clean post-2019 corporate-action forward window; historical corporate-action candidates outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when cathode-material customer/orderbook visibility, capacity expansion and utilization leverage were visible before the rerating was fully capitalized. Green still requires customer call-off, delivery schedule, utilization ramp, ASP/input-cost pass-through and margin/revision confirmation; after the June/July 2023 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.95, "entry_date": "2023-03-31", "entry_price": 153900, "evidence_family": "battery_cathode_material_orderbook_capacity_customer_contract_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "CATHODE_SEPARATOR_FOIL_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-05-15", "low_price_180d": 149000, "peak_date": "2023-06-13", "peak_price": 242500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005070.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 7, "battery_orderbook_visibility": 10, "capacity_delivery_schedule": 8, "customer_contract_quality": 9, "information_confidence": 4, "margin_revision_bridge": 8, "market_mispricing": 9, "total": 70, "utilization_calloff_bridge": 8, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C11_005070_COSMOAMT_20230331_CATHODE_ORDERBOOK_RERATING_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_visibility", "customer_contract_or_calloff_quality", "capacity_delivery_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_delivery_schedule_required", "utilization_and_capacity_absorption_required", "ASP_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_calloff_gap", "utilization_or_delivery_delay", "margin_revision_bridge_failure"], "symbol": "005070", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005070/2023.csv", "trigger_date": "2023-03-31", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.62, "MAE_30D_pct": -18.1, "MAE_90D_pct": -47.62, "MFE_180D_pct": 15.85, "MFE_30D_pct": 15.85, "MFE_90D_pct": 15.85, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_393890_WCP_20230726_SEPARATOR_ORDERBOOK_PREMIUM_4B", "case_role": "separator_orderbook_capacity_price_premium_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023/2024 forward window", "current_profile_error": true, "current_profile_verdict": "Separator orderbook/capacity price premium should route to local 4B or counterexample when the market has already capitalized customer/order optionality and incremental customer call-off, utilization, ASP/input-cost and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.83, "entry_date": "2023-07-26", "entry_price": 75700, "evidence_family": "separator_orderbook_price_premium_without_customer_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CATHODE_SEPARATOR_FOIL_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-04-08", "low_price_180d": 34350, "peak_date": "2023-08-01", "peak_price": 87700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "battery_orderbook_visibility": 7, "capacity_delivery_schedule": 5, "customer_contract_quality": 5, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 33, "utilization_calloff_bridge": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C11_393890_WCP_20230726_SEPARATOR_ORDERBOOK_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_visibility", "customer_contract_or_calloff_quality", "capacity_delivery_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_delivery_schedule_required", "utilization_and_capacity_absorption_required", "ASP_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_calloff_gap", "utilization_or_delivery_delay", "margin_revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -31.63, "MAE_30D_pct": -15.26, "MAE_90D_pct": -21.57, "MFE_180D_pct": 15.52, "MFE_30D_pct": 15.52, "MFE_90D_pct": 15.52, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_006110_SAMAAL_20230726_ALUMINUMFOIL_ORDERBOOK_FALSE_GREEN", "case_role": "aluminum_foil_orderbook_false_green_counterexample", "company_name": "삼아알미늄", "corporate_action_window_status": "selected post-2023-02-09 forward window clean; prior corporate-action candidates outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Battery aluminum-foil orderbook price confirmation should stay Yellow or local 4B when price strength is not followed by fresh customer call-off, utilization, delivery cadence, ASP/input-cost pass-through and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.81, "entry_date": "2023-07-26", "entry_price": 117300, "evidence_family": "battery_aluminumfoil_orderbook_price_confirmation_without_incremental_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CATHODE_SEPARATOR_FOIL_ORDERBOOK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-01-25", "low_price_180d": 80200, "peak_date": "2023-07-26", "peak_price": 135500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006110.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "battery_orderbook_visibility": 7, "capacity_delivery_schedule": 4, "customer_contract_quality": 5, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 32, "utilization_calloff_bridge": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C11_006110_SAMAAL_20230726_ALUMINUMFOIL_ORDERBOOK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_orderbook_visibility", "customer_contract_or_calloff_quality", "capacity_delivery_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_and_delivery_schedule_required", "utilization_and_capacity_absorption_required", "ASP_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_orderbook_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_to_calloff_gap", "utilization_or_delivery_delay", "margin_revision_bridge_failure"], "symbol": "006110", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CATHODE_SEPARATOR_FOIL_ORDERBOOK_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_orderbook_rerating_cathode_separator_foil_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C11 battery orderbook rows should allow Stage2 when orderbook/customer evidence maps to call-off, delivery schedule, utilization, ASP/input-cost and margin-revision bridge, but should route late-cycle cathode/separator/foil premiums to local 4B/Yellow when incremental orderbook-to-margin evidence has not refreshed.",
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
3. Add C11-specific battery orderbook / customer call-off / delivery schedule / utilization / ASP-input-cost / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C11_STAGE2_ALLOWED_ON_CALLOFF_DELIVERY_UTILIZATION_MARGIN_REVISION_BRIDGE
- C11_GREEN_REQUIRES_ORDERBOOK_TO_CALLOFF_ASP_INPUT_COST_REVISION
- C11_BATTERY_ORDERBOOK_PRICE_PREMIUM_LOCAL_4B
- C11_ORDERBOOK_OPTIONALITY_WITHOUT_CALLOFF_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

