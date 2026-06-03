# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C12 — Battery customer contract call-off risk / separator-foil 4B guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: SEPARATOR_FOIL_CUSTOMER_CALLOFF_RISK_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|customer_contract_to_calloff_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_separator_foil_calloff_risk_4b_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK current coverage:
rows=15, symbols=9, date range=2023-01-31~2024-07-25, good/bad S2=4/0, 4B/4C=0/0
top covered symbols: UNKNOWN_SYMBOL(4), 247540(2), 278280(2), 003670(1), 005070(1)
```

This run avoids those top-covered C12 symbols and adds 006110, 393890, and 361610.  
Each row uses a new `C12 + symbol + trigger_type + entry_date` hard key:
```text
C12 + 006110 + Stage2-Actionable + 2023-03-31
C12 + 393890 + 4B-local-price-only + 2023-07-26
C12 + 361610 + Stage3-Yellow + 2023-07-26
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
006110 삼아알미늄: selected post-2023-02-09 forward window clean; corporate-action candidate is before selected trigger window.
393890 더블유씨피: corporate_action_candidate_count=0; clean 2023/2024 forward window.
361610 SK아이이테크놀로지: corporate_action_candidate_count=0; clean 2023/2024 forward window.
```

## 3. Research thesis

C12 should distinguish customer contract evidence that becomes call-off and utilization from contract optionality already paid in price:

```text
battery customer contract / long-term supply agreement
→ customer call-off cadence and delivery schedule
→ capacity utilization and absorption
→ ASP/input-cost pass-through and working capital
→ gross margin and revision bridge
→ Stage2/Green or local 4B/4C watch
```

A battery contract is a reservation book. Stage2 can buy it when reservations turn into call-offs, shipments and margins. Green should require the customer to pull volume and the plant to earn the spread, not just a larger contract headline multiple.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C12_006110_SAMAAL_20230331_BATTERY_FOIL_CALLOFF_STAGE2 | 006110 | positive_battery_aluminum_foil_contract_calloff_stage2_success_with_later_4b_refresh | 2023-03-31 | 72100 | 158900 on 2023-10-17 | 65900 on 2023-05-09 | 38.97% | 94.31% | 120.39% | -8.6% | -37.26% |
| C12_393890_WCP_20230726_SEPARATOR_CALLOFF_RISK_4B | 393890 | separator_contract_calloff_price_premium_counterexample | 2023-07-26 | 75700 | 87700 on 2023-08-01 | 34350 on 2024-04-08 | 15.85% | 15.85% | 15.85% | -54.62% | -60.83% |
| C12_361610_SKIET_20230726_SEPARATOR_CALLOFF_FALSE_GREEN | 361610 | separator_contract_calloff_false_green_counterexample | 2023-07-26 | 108600 | 120000 on 2023-07-26 | 59400 on 2023-10-27 | 10.5% | 10.5% | 10.5% | -45.3% | -50.5% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 006110 is the positive anchor. Battery aluminum-foil contract/capacity evidence converted into a strong price path before the later 2023 premium required 4B refresh discipline.
- Stage2 is allowed only when customer-contract salience maps to call-off cadence, delivery schedule, utilization absorption, ASP/input-cost and margin/revision visibility.

### Stage3 / Green
- C12 Green should require customer call-off conversion, capacity utilization absorption, delivery schedule, ASP/input-cost bridge and margin/revision confirmation.
- 361610 is the false-Green/Yellow guard: separator contract/capacity price confirmation was visible, but the July 2023 price had limited residual upside and a much larger drawdown once call-off and utilization concerns dominated.

### 4B
- 393890 fills the separator contract price-premium 4B pocket. The July 2023 trigger had local MFE but much larger forward MAE when customer call-off and margin proof failed to refresh.
- 006110 also demonstrates that valid Stage2 can become local 4B after the rerating capitalizes the customer-contract pipeline.
- The core 4B rule is that long-term customer contract optionality must not substitute for actual call-off, utilization and margin revision.

### 4C
- No hard customer cancellation, contract loss, plant failure, liquidity break or accounting break is asserted.
- The C12 break mode here is call-off exhaustion: contract visibility may remain real, but incremental customer pull, utilization and margin revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C12_006110_SAMAAL_20230331_BATTERY_FOIL_CALLOFF_STAGE2": {
    "ASP_input_cost_bridge": 7,
    "calloff_cadence_quality": 8,
    "capacity_delivery_schedule": 8,
    "customer_contract_visibility": 10,
    "information_confidence": 4,
    "margin_revision_bridge": 8,
    "market_mispricing": 9,
    "total": 69,
    "utilization_absorption": 8,
    "valuation_rerating_runway": 7
  },
  "C12_361610_SKIET_20230726_SEPARATOR_CALLOFF_FALSE_GREEN": {
    "ASP_input_cost_bridge": 3,
    "calloff_cadence_quality": 3,
    "capacity_delivery_schedule": 4,
    "customer_contract_visibility": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 30,
    "utilization_absorption": 3,
    "valuation_rerating_runway": 1
  },
  "C12_393890_WCP_20230726_SEPARATOR_CALLOFF_RISK_4B": {
    "ASP_input_cost_bridge": 3,
    "calloff_cadence_quality": 3,
    "capacity_delivery_schedule": 4,
    "customer_contract_visibility": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "total": 30,
    "utilization_absorption": 3,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C12 guard:
```text
if battery_customer_contract and calloff_delivery_utilization_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if battery_contract_price_premium and no incremental_calloff_utilization_ASP_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and contract_to_calloff_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 393890 / 2023-07-26: separator contract premium can be over-promoted if price strength substitutes for customer call-off and utilization proof.
- 361610 / 2023-07-26: separator call-off confirmation can look like Yellow-to-Green, but fails without renewed utilization and margin revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -8.6, "MAE_30D_pct": -8.6, "MAE_90D_pct": -8.6, "MFE_180D_pct": 120.39, "MFE_30D_pct": 38.97, "MFE_90D_pct": 94.31, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_006110_SAMAAL_20230331_BATTERY_FOIL_CALLOFF_STAGE2", "case_role": "positive_battery_aluminum_foil_contract_calloff_stage2_success_with_later_4b_refresh", "company_name": "삼아알미늄", "corporate_action_window_status": "selected post-2023-02-09 forward window clean; corporate-action candidate is 2023-02-09 and before selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when battery aluminum-foil customer contract visibility, capacity expansion and delivery/call-off optionality were visible before the rerating was fully capitalized. Green still requires customer call-off cadence, delivery schedule, utilization, ASP/input-cost pass-through and margin/revision confirmation; after the October 2023 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.26, "entry_date": "2023-03-31", "entry_price": 72100, "evidence_family": "battery_aluminum_foil_customer_contract_calloff_capacity_delivery_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_FOIL_CUSTOMER_CALLOFF_RISK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-05-09", "low_price_180d": 65900, "peak_date": "2023-10-17", "peak_price": 158900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006110.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 7, "calloff_cadence_quality": 8, "capacity_delivery_schedule": 8, "customer_contract_visibility": 10, "information_confidence": 4, "margin_revision_bridge": 8, "market_mispricing": 9, "total": 69, "utilization_absorption": 8, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C12_006110_SAMAAL_20230331_BATTERY_FOIL_CALLOFF_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_visibility", "customer_calloff_cadence", "delivery_utilization_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_conversion_required", "utilization_and_capacity_absorption_required", "ASP_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_contract_calloff_price_premium", "contract_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_gap_or_customer_demand_slowdown", "utilization_or_delivery_delay", "margin_revision_bridge_failure"], "symbol": "006110", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv", "trigger_date": "2023-03-31", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.62, "MAE_30D_pct": -18.1, "MAE_90D_pct": -47.62, "MFE_180D_pct": 15.85, "MFE_30D_pct": 15.85, "MFE_90D_pct": 15.85, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_393890_WCP_20230726_SEPARATOR_CALLOFF_RISK_4B", "case_role": "separator_contract_calloff_price_premium_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023/2024 forward window", "current_profile_error": true, "current_profile_verdict": "Separator customer-contract price premium should route to local 4B or counterexample when the market has already capitalized contract optionality and incremental customer call-off, utilization, delivery cadence, ASP/input-cost and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.83, "entry_date": "2023-07-26", "entry_price": 75700, "evidence_family": "separator_customer_contract_price_premium_without_incremental_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_FOIL_CUSTOMER_CALLOFF_RISK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-04-08", "low_price_180d": 34350, "peak_date": "2023-08-01", "peak_price": 87700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "calloff_cadence_quality": 3, "capacity_delivery_schedule": 4, "customer_contract_visibility": 7, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 30, "utilization_absorption": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C12_393890_WCP_20230726_SEPARATOR_CALLOFF_RISK_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_visibility", "customer_calloff_cadence", "delivery_utilization_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_conversion_required", "utilization_and_capacity_absorption_required", "ASP_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_contract_calloff_price_premium", "contract_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_gap_or_customer_demand_slowdown", "utilization_or_delivery_delay", "margin_revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.3, "MAE_30D_pct": -19.61, "MAE_90D_pct": -45.3, "MFE_180D_pct": 10.5, "MFE_30D_pct": 10.5, "MFE_90D_pct": 10.5, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_361610_SKIET_20230726_SEPARATOR_CALLOFF_FALSE_GREEN", "case_role": "separator_contract_calloff_false_green_counterexample", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023/2024 forward window", "current_profile_error": true, "current_profile_verdict": "Separator call-off risk should remain Yellow or local 4B when price confirmation is not followed by customer call-off, utilization absorption, delivery cadence, ASP/input-cost pass-through and margin/revision evidence. The July 2023 spike had limited residual upside and a much larger forward MAE once EV/customer demand concerns dominated.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.5, "entry_date": "2023-07-26", "entry_price": 108600, "evidence_family": "separator_customer_contract_calloff_price_confirmation_without_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_FOIL_CUSTOMER_CALLOFF_RISK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-27", "low_price_180d": 59400, "peak_date": "2023-07-26", "peak_price": 120000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "calloff_cadence_quality": 3, "capacity_delivery_schedule": 4, "customer_contract_visibility": 7, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "total": 30, "utilization_absorption": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C12_361610_SKIET_20230726_SEPARATOR_CALLOFF_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_customer_contract_visibility", "customer_calloff_cadence", "delivery_utilization_ASP_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_conversion_required", "utilization_and_capacity_absorption_required", "ASP_input_cost_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_contract_calloff_price_premium", "contract_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["calloff_gap_or_customer_demand_slowdown", "utilization_or_delivery_delay", "margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SEPARATOR_FOIL_CUSTOMER_CALLOFF_RISK_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_customer_contract_calloff_risk_separator_foil_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C12 battery customer-contract rows should allow Stage2 when customer contract evidence maps to call-off cadence, delivery schedule, utilization absorption, ASP/input-cost bridge and margin-revision evidence, but should route separator/foil contract premiums to Yellow/local 4B when customer call-off or utilization evidence has not refreshed.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C12 + symbol + trigger_type + entry_date.
3. Add C12-specific battery customer-contract / call-off / delivery schedule / utilization / ASP-input-cost / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C12_STAGE2_ALLOWED_ON_CONTRACT_CALLOFF_DELIVERY_UTILIZATION_MARGIN_REVISION_BRIDGE
- C12_GREEN_REQUIRES_CUSTOMER_PULL_UTILIZATION_ASP_INPUT_COST_REVISION
- C12_CONTRACT_PRICE_PREMIUM_LOCAL_4B
- C12_PRICE_CONFIRMATION_WITHOUT_CALLOFF_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

