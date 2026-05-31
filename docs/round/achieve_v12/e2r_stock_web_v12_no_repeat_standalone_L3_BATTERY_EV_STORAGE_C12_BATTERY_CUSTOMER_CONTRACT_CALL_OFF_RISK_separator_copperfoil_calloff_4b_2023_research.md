# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C12 — Battery customer contract call-off risk / separator-copperfoil 4B guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_STORAGE
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: SEPARATOR_COPPERFOIL_CONTRACT_CALLOFF_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|battery_customer_contract_calloff_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_STORAGE_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_separator_copperfoil_calloff_4b_2023_research.md
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

This run avoids those top-covered C12 symbols and adds 361610, 020150, and 011790.  
Each row uses a new `C12 + symbol + trigger_type + entry_date` hard key:
```text
C12 + 361610 + 4B-protective + 2023-04-04
C12 + 020150 + Stage3-Yellow + 2023-03-03
C12 + 011790 + 4B-local-price-only + 2023-03-31
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
361610 SK아이이테크놀로지: corporate_action_candidate_count=0; clean 2023 forward window.
020150 롯데에너지머티리얼즈: corporate_action_candidate_count=0; clean 2023 forward window. Name changed from 일진머티리얼즈 to 롯데에너지머티리얼즈 during the 2023 research window.
011790 SKC: selected 2023 forward window clean; historical name/corporate-action candidates are outside selected trigger window.
```

## 3. Research thesis

C12 should split real battery customer contract durability from battery contract/capacity optionality already paid in price:

```text
battery separator / copper-foil customer contract
→ customer call-off visibility
→ shipment cadence and backlog conversion
→ utilization and working-capital quality
→ ASP/mix and margin revision bridge
→ Stage2/Green or local/protective 4B cap
```

A battery customer contract is a loading dock, not the delivered freight. Stage2 can buy when containers are leaving the dock on schedule. Green should not pay for the dock after customers can still slow call-offs and margins have not yet followed.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C12_361610_SKIET_20230404_SEPARATOR_CUSTOMER_CALLOFF_4B_PROTECTIVE | 361610 | protective_separator_customer_contract_calloff_4B_success | 2023-04-04 | 85600 | 103900 on 2023-06-12 | 58700 on 2023-10-31 | 10.75% | 21.38% | 21.38% | -31.43% | -43.5% |
| C12_020150_LOTTEEM_20230303_COPPERFOIL_CONTRACT_FALSE_GREEN | 020150 | copperfoil_customer_contract_false_green_counterexample | 2023-03-03 | 71300 | 75000 on 2023-03-06 | 36650 on 2023-10-26 | 5.19% | 5.19% | 5.19% | -48.6% | -51.13% |
| C12_011790_SKC_20230331_COPPERFOIL_CONTRACT_PREMIUM_4B | 011790 | copperfoil_contract_price_premium_local_4B_counterexample | 2023-03-31 | 114300 | 122300 on 2023-04-05 | 68000 on 2023-10-23 | 7.0% | 7.0% | 7.0% | -40.51% | -44.4% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- No row in this MD is counted as a clean Stage2/Green positive.
- C12 Stage2 requires customer call-off visibility, shipment cadence, utilization, working-capital quality, ASP/mix and margin/revision confirmation.
- 가격만 있는 entry는 Stage2/Green positive로 금지된다. The positive row here is protective 4B, not a buy-positive Green row.

### Stage3 / Green
- C12 Green should require contract durability, customer call-off clarity, delivery cadence, utilization, working-capital and margin/revision bridge.
- 020150 is the false-Green/Yellow guard: copper-foil/customer optionality and name-change salience were visible, but customer-volume-to-margin evidence did not refresh and the forward drawdown overwhelmed residual upside.

### 4B
- 361610 is the protective 4B anchor. The separator/customer-capacity story had real thematic value, but price premium was already high while utilization and call-off risk were not resolved.
- 011790 fills the copper-foil contract premium 4B pocket.
- The core 4B rule is that customer/contract salience should not substitute for shipment cadence, utilization and margin-revision evidence.

### 4C
- No hard customer cancellation or accounting break is asserted.
- The C12 break mode here is call-off-to-margin exhaustion: the orderbook/customer story may remain directionally real, but incremental shipment, utilization, ASP/mix and revision evidence no longer supports the price already paid.

## 6. Raw component score breakdown

```json
{
  "C12_011790_SKC_20230331_COPPERFOIL_CONTRACT_PREMIUM_4B": {
    "ASP_mix_margin_revision_bridge": 2,
    "calloff_or_volume_risk": 9,
    "customer_contract_visibility": 8,
    "information_confidence": 3,
    "price_premium_or_blowoff_risk": 8,
    "shipment_cadence_visibility": 3,
    "total": 40,
    "utilization_recovery_bridge": 3,
    "valuation_rerating_runway": 1,
    "working_capital_quality": 3
  },
  "C12_020150_LOTTEEM_20230303_COPPERFOIL_CONTRACT_FALSE_GREEN": {
    "ASP_mix_margin_revision_bridge": 2,
    "calloff_or_volume_risk": 9,
    "customer_contract_visibility": 7,
    "information_confidence": 3,
    "price_premium_or_blowoff_risk": 8,
    "shipment_cadence_visibility": 3,
    "total": 38,
    "utilization_recovery_bridge": 2,
    "valuation_rerating_runway": 1,
    "working_capital_quality": 3
  },
  "C12_361610_SKIET_20230404_SEPARATOR_CUSTOMER_CALLOFF_4B_PROTECTIVE": {
    "ASP_mix_margin_revision_bridge": 2,
    "calloff_or_volume_risk": 10,
    "customer_contract_visibility": 7,
    "information_confidence": 4,
    "price_premium_or_blowoff_risk": 9,
    "shipment_cadence_visibility": 3,
    "total": 42,
    "utilization_recovery_bridge": 3,
    "valuation_rerating_runway": 1,
    "working_capital_quality": 3
  }
}
```

## 7. Current calibrated profile stress test

Suggested C12 guard:
```text
if battery_contract_price_premium and no customer_calloff_shipment_utilization_margin_revision_bridge:
    block_stage2_green_positive = true
    route_to_stage3_yellow_or_local_4B = true

if calloff_or_utilization_risk_visible and valuation_runway_thin:
    route_to_protective_4B = true

if post_peak_drawdown and customer_volume_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 020150 / 2023-03-03: copper-foil customer-contract confirmation can be over-promoted if price strength and name-change/acquisition salience substitute for shipment/margin evidence.
- 011790 / 2023-03-31: copper-foil contract premium can look actionable, but fails without refreshed customer call-off, utilization and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -31.43, "MAE_30D_pct": -12.97, "MAE_90D_pct": -12.97, "MFE_180D_pct": 21.38, "MFE_30D_pct": 10.75, "MFE_90D_pct": 21.38, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_361610_SKIET_20230404_SEPARATOR_CUSTOMER_CALLOFF_4B_PROTECTIVE", "case_role": "protective_separator_customer_contract_calloff_4B_success", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023 forward window", "current_profile_error": false, "current_profile_verdict": "Protective 4B routing was useful: the separator/customer-capacity story had real thematic value, but by April 2023 a large part of orderbook optionality was already capitalized while EV demand, utilization, pricing and customer call-off risk remained insufficiently resolved. This should not be promoted to Stage2/Green without customer call-off visibility, shipment cadence, utilization recovery and margin/revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.5, "entry_date": "2023-04-04", "entry_price": 85600, "evidence_family": "battery_separator_customer_capacity_contract_calloff_risk_price_premium_4B_route", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_CONTRACT_CALLOFF_4B_GUARD", "forward_window_trading_days": 180, "historical_name": null, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-10-31", "low_price_180d": 58700, "peak_date": "2023-06-12", "peak_price": 103900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 2, "calloff_or_volume_risk": 10, "customer_contract_visibility": 7, "information_confidence": 4, "price_premium_or_blowoff_risk": 9, "shipment_cadence_visibility": 3, "total": 42, "utilization_recovery_bridge": 3, "valuation_rerating_runway": 1, "working_capital_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C12_361610_SKIET_20230404_SEPARATOR_CUSTOMER_CALLOFF_4B_PROTECTIVE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["customer_contract_visibility", "calloff_or_volume_risk_absence_required", "shipment_cadence_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_visibility_required", "shipment_cadence_and_capacity_utilization_required", "ASP_mix_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_contract_or_capacity_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_volume_shortfall", "utilization_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-04-04", "trigger_type": "4B-protective", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -48.6, "MAE_30D_pct": -13.04, "MAE_90D_pct": -34.01, "MFE_180D_pct": 5.19, "MFE_30D_pct": 5.19, "MFE_90D_pct": 5.19, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_020150_LOTTEEM_20230303_COPPERFOIL_CONTRACT_FALSE_GREEN", "case_role": "copperfoil_customer_contract_false_green_counterexample", "company_name": "롯데에너지머티리얼즈", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023 forward window; name changed from 일진머티리얼즈 to 롯데에너지머티리얼즈 during the 2023 research window", "current_profile_error": true, "current_profile_verdict": "Copper-foil/customer-contract price confirmation should remain Yellow or local 4B when acquisition/name-change salience and customer optionality are not followed by fresh call-off visibility, shipment cadence, utilization, ASP/mix and margin-revision evidence. The March 2023 trigger had limited residual MFE and a large full-window drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.13, "entry_date": "2023-03-03", "entry_price": 71300, "evidence_family": "copperfoil_customer_contract_name_change_price_confirmation_without_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_CONTRACT_CALLOFF_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "일진머티리얼즈", "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-10-26", "low_price_180d": 36650, "peak_date": "2023-03-06", "peak_price": 75000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020150.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 2, "calloff_or_volume_risk": 9, "customer_contract_visibility": 7, "information_confidence": 3, "price_premium_or_blowoff_risk": 8, "shipment_cadence_visibility": 3, "total": 38, "utilization_recovery_bridge": 2, "valuation_rerating_runway": 1, "working_capital_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C12_020150_LOTTEEM_20230303_COPPERFOIL_CONTRACT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["customer_contract_visibility", "calloff_or_volume_risk_absence_required", "shipment_cadence_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_visibility_required", "shipment_cadence_and_capacity_utilization_required", "ASP_mix_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_contract_or_capacity_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_volume_shortfall", "utilization_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "020150", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2023.csv", "trigger_date": "2023-03-03", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -40.51, "MAE_30D_pct": -13.3, "MAE_90D_pct": -21.26, "MFE_180D_pct": 7.0, "MFE_30D_pct": 7.0, "MFE_90D_pct": 7.0, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_011790_SKC_20230331_COPPERFOIL_CONTRACT_PREMIUM_4B", "case_role": "copperfoil_contract_price_premium_local_4B_counterexample", "company_name": "SKC", "corporate_action_window_status": "selected 2023 forward window clean; historical corporate-action/name candidates are outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Copper-foil contract premium should route to local 4B/counterexample when the market has already capitalized battery orderbook optionality and fresh customer call-off, shipment cadence, utilization, working-capital and margin/revision evidence do not refresh. The March 2023 trigger had small residual MFE and a much larger drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.4, "entry_date": "2023-03-31", "entry_price": 114300, "evidence_family": "copperfoil_customer_contract_price_premium_without_incremental_calloff_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_CONTRACT_CALLOFF_4B_GUARD", "forward_window_trading_days": 180, "historical_name": null, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-10-23", "low_price_180d": 68000, "peak_date": "2023-04-05", "peak_price": 122300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011790.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 2, "calloff_or_volume_risk": 9, "customer_contract_visibility": 8, "information_confidence": 3, "price_premium_or_blowoff_risk": 8, "shipment_cadence_visibility": 3, "total": 40, "utilization_recovery_bridge": 3, "valuation_rerating_runway": 1, "working_capital_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C12_011790_SKC_20230331_COPPERFOIL_CONTRACT_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["customer_contract_visibility", "calloff_or_volume_risk_absence_required", "shipment_cadence_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_calloff_visibility_required", "shipment_cadence_and_capacity_utilization_required", "ASP_mix_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_contract_or_capacity_price_premium", "orderbook_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_volume_shortfall", "utilization_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "011790", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv", "trigger_date": "2023-03-31", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SEPARATOR_COPPERFOIL_CONTRACT_CALLOFF_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_STORAGE",
  "loop_contribution_label": "battery_customer_contract_calloff_separator_copperfoil_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C12 battery contract/call-off rows should block Stage2/Green when customer call-off risk, utilization, shipment cadence, ASP/mix and working-capital-to-margin evidence are unresolved; separator/copper-foil contract price premiums should route to Yellow/local 4B or protective 4B until customer volume and margin revision bridge refreshes.",
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
3. Add C12-specific customer call-off / contract durability / shipment cadence / utilization / ASP-mix / working-capital / margin-revision / local-protective-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C12_BLOCK_GREEN_WITHOUT_CALLOFF_SHIPMENT_UTILIZATION_MARGIN_REVISION_BRIDGE
- C12_BATTERY_CONTRACT_PRICE_PREMIUM_ROUTES_TO_LOCAL_4B
- C12_PROTECTIVE_4B_WHEN_UTILIZATION_OR_CALLOFF_RISK_DOMINATES
- C12_PRICE_CONFIRMATION_WITHOUT_CUSTOMER_VOLUME_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_STORAGE/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

