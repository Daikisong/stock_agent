# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C14 — EV demand slowdown 4B·4C / separator-foil call-off risk guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: SEPARATOR_FOIL_EV_DEMAND_SLOWDOWN_CALLOFF_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|EV_demand_slowdown_calloff_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_separator_foil_demand_slowdown_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C14_EV_DEMAND_SLOWDOWN_4B_4C current coverage:
rows=23, symbols=5, date range=2023-07-26~2024-12-20, good/bad S2=0/0, 4B/4C=3/5
top covered symbols: 066970(6), 247540(6), 003670(5), 373220(4), 006400(2)
```

This run avoids those top-covered C14 symbols and adds 006110, 393890, and 361610.  
Each row uses a new `C14 + symbol + trigger_type + entry_date` hard key:
```text
C14 + 006110 + 4B-local-price-only + 2023-10-12
C14 + 393890 + 4B-local-price-only + 2023-07-26
C14 + 361610 + Stage3-Yellow + 2023-07-26
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

C14 should distinguish EV-chain demand slowdown and customer call-off exhaustion from ordinary late-cycle price consolidation:

```text
EV demand slowdown / inventory digestion
→ customer call-off uncertainty
→ separator/foil utilization pressure
→ ASP/input-cost and working-capital squeeze
→ gross margin and revision bridge failure
→ local 4B / 4C-watch routing
```

A battery contract is a reservation book, but an EV slowdown is the customer pushing delivery out. Stage2 should not buy the reservation ledger when call-offs slow, plant utilization softens and margin revisions stop arriving.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C14_006110_SAMAAL_20231012_FOIL_DEMAND_SLOWDOWN_AFTER_BLOWOFF_4B | 006110 | protective_aluminum_foil_blowoff_to_ev_demand_slowdown_4b_success | 2023-10-12 | 152400 | 158900 on 2023-10-17 | 72100 on 2024-06-28 | 4.27% | 4.27% | 4.27% | -52.69% | -54.63% |
| C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_4B | 393890 | separator_EV_demand_slowdown_price_premium_counterexample | 2023-07-26 | 75700 | 87700 on 2023-08-01 | 34350 on 2024-04-08 | 15.85% | 15.85% | 15.85% | -54.62% | -60.83% |
| C14_361610_SKIET_20230726_SEPARATOR_CALLOFF_SLOWDOWN_FALSE_GREEN | 361610 | separator_EV_demand_slowdown_false_green_counterexample | 2023-07-26 | 108600 | 120000 on 2023-07-26 | 59400 on 2023-10-27 | 10.5% | 10.5% | 10.5% | -45.3% | -50.5% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C14 Green should require visible demand resilience, customer call-off conversion, utilization absorption, ASP/input-cost bridge and margin/revision confirmation.
- 361610 is the false-Green/Yellow guard: separator price confirmation looked tradable, but EV demand slowdown and call-off uncertainty overwhelmed residual upside.
- 393890 is the separator price-premium guard: local MFE existed, but the forward MAE was much larger once call-off and utilization proof failed to refresh.

### 4B
- 006110 is the protective 4B anchor. It had valid earlier contract/capacity evidence, but the October 2023 blowoff had already capitalized too much optionality while EV demand/call-off risk was rising.
- 393890 fills the separator 4B pocket. The July 2023 entry required local 4B despite a later short squeeze-like local MFE.
- The core 4B rule is that late price strength in EV-chain material suppliers must not substitute for customer pull, utilization and margin revision.

### 4C
- No hard customer cancellation, contract loss, plant failure or financing break is asserted.
- The failure mode here is EV-demand/call-off exhaustion. Hard 4C should require clearer cancellation, severe utilization collapse, covenant/liquidity break, or explicit margin/revision thesis break; absent that, local 4B/counterexample is the safer label.

## 6. Raw component score breakdown

```json
{
  "C14_006110_SAMAAL_20231012_FOIL_DEMAND_SLOWDOWN_AFTER_BLOWOFF_4B": {
    "ASP_input_cost_margin_bridge": 3,
    "EV_demand_slowdown_salience": 9,
    "customer_calloff_risk": 9,
    "information_confidence": 3,
    "inventory_or_utilization_pressure": 7,
    "market_mispricing": 3,
    "non_price_evidence_refresh": 2,
    "total": 46,
    "valuation_blowoff_risk": 10
  },
  "C14_361610_SKIET_20230726_SEPARATOR_CALLOFF_SLOWDOWN_FALSE_GREEN": {
    "ASP_input_cost_margin_bridge": 3,
    "EV_demand_slowdown_salience": 9,
    "customer_calloff_risk": 8,
    "information_confidence": 3,
    "inventory_or_utilization_pressure": 8,
    "market_mispricing": 4,
    "non_price_evidence_refresh": 2,
    "total": 45,
    "valuation_blowoff_risk": 8
  },
  "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_4B": {
    "ASP_input_cost_margin_bridge": 3,
    "EV_demand_slowdown_salience": 9,
    "customer_calloff_risk": 8,
    "information_confidence": 3,
    "inventory_or_utilization_pressure": 8,
    "market_mispricing": 4,
    "non_price_evidence_refresh": 2,
    "total": 45,
    "valuation_blowoff_risk": 8
  }
}
```

## 7. Current calibrated profile stress test

Suggested C14 guard:
```text
if EV_chain_price_premium and EV_demand_slowdown_calloff_risk_visible:
    block_stage2_green_positive = true
    route_to_local_4B_or_stage3_yellow = true

if customer_calloff_utilization_ASP_margin_revision_bridge_not_refreshing:
    block_stage3_green = true

if hard_cancellation_liquidity_or_utilization_break:
    route_to_4C_watch_or_hard_4C = true
```

Residual errors:
```text
current_profile_error_count = 2
- 393890 / 2023-07-26: separator premium can be over-promoted if price strength substitutes for customer call-off, utilization and margin proof.
- 361610 / 2023-07-26: separator demand confirmation can look like Yellow-to-Green, but fails without renewed customer pull and margin revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -52.69, "MAE_30D_pct": -27.69, "MAE_90D_pct": -47.38, "MFE_180D_pct": 4.27, "MFE_30D_pct": 4.27, "MFE_90D_pct": 4.27, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_006110_SAMAAL_20231012_FOIL_DEMAND_SLOWDOWN_AFTER_BLOWOFF_4B", "case_role": "protective_aluminum_foil_blowoff_to_ev_demand_slowdown_4b_success", "company_name": "삼아알미늄", "corporate_action_window_status": "selected post-2023-02-09 forward window clean; corporate-action candidate is 2023-02-09 and before selected trigger window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful after the aluminum-foil/customer-contract rerating had already capitalized call-off optionality. The stock had valid earlier orderbook/call-off evidence, but at the 2023-10-12 blowoff entry the forward path was dominated by EV-demand slowdown, call-off uncertainty and margin bridge exhaustion; price strength should not have been promoted to fresh Stage2/Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -54.63, "entry_date": "2023-10-12", "entry_price": 152400, "evidence_family": "battery_aluminum_foil_contract_blowoff_after_EV_demand_slowdown_calloff_margin_gap", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_FOIL_EV_DEMAND_SLOWDOWN_CALLOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-06-28", "low_price_180d": 72100, "peak_date": "2023-10-17", "peak_price": 158900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006110.json", "raw_component_score_breakdown": {"ASP_input_cost_margin_bridge": 3, "EV_demand_slowdown_salience": 9, "customer_calloff_risk": 9, "information_confidence": 3, "inventory_or_utilization_pressure": 7, "market_mispricing": 3, "non_price_evidence_refresh": 2, "total": 46, "valuation_blowoff_risk": 10}, "reuse_reason": null, "same_entry_group_id": "C14_006110_SAMAAL_20231012_FOIL_DEMAND_SLOWDOWN_AFTER_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_slowdown_absence_required_for_positive", "customer_calloff_and_delivery_visibility_required", "utilization_ASP_inputcost_margin_revision_route_required"], "stage3_evidence_fields": ["customer_calloff_conversion_required", "utilization_absorption_and_inventory_required", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_separator_foil_price_premium", "EV_demand_slowdown_calloff_risk", "post_peak_drawdown"], "stage4c_evidence_fields": ["EV_demand_slowdown_acceleration", "customer_calloff_gap_or_contract_delay", "utilization_margin_revision_bridge_failure"], "symbol": "006110", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv", "trigger_date": "2023-10-12", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.62, "MAE_30D_pct": -18.1, "MAE_90D_pct": -47.62, "MFE_180D_pct": 15.85, "MFE_30D_pct": 15.85, "MFE_90D_pct": 15.85, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_4B", "case_role": "separator_EV_demand_slowdown_price_premium_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023/2024 forward window", "current_profile_error": true, "current_profile_verdict": "Separator price premium should route to local 4B/counterexample when EV demand slowdown and customer call-off risk are rising while utilization, delivery cadence and margin/revision evidence are not refreshing. The July 2023 trigger had local MFE but much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.83, "entry_date": "2023-07-26", "entry_price": 75700, "evidence_family": "separator_EV_demand_slowdown_calloff_utilization_margin_gap_after_price_premium", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_FOIL_EV_DEMAND_SLOWDOWN_CALLOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-04-08", "low_price_180d": 34350, "peak_date": "2023-08-01", "peak_price": 87700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"ASP_input_cost_margin_bridge": 3, "EV_demand_slowdown_salience": 9, "customer_calloff_risk": 8, "information_confidence": 3, "inventory_or_utilization_pressure": 8, "market_mispricing": 4, "non_price_evidence_refresh": 2, "total": 45, "valuation_blowoff_risk": 8}, "reuse_reason": null, "same_entry_group_id": "C14_393890_WCP_20230726_SEPARATOR_EV_DEMAND_SLOWDOWN_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_slowdown_absence_required_for_positive", "customer_calloff_and_delivery_visibility_required", "utilization_ASP_inputcost_margin_revision_route_required"], "stage3_evidence_fields": ["customer_calloff_conversion_required", "utilization_absorption_and_inventory_required", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_separator_foil_price_premium", "EV_demand_slowdown_calloff_risk", "post_peak_drawdown"], "stage4c_evidence_fields": ["EV_demand_slowdown_acceleration", "customer_calloff_gap_or_contract_delay", "utilization_margin_revision_bridge_failure"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.3, "MAE_30D_pct": -19.61, "MAE_90D_pct": -45.3, "MFE_180D_pct": 10.5, "MFE_30D_pct": 10.5, "MFE_90D_pct": 10.5, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_361610_SKIET_20230726_SEPARATOR_CALLOFF_SLOWDOWN_FALSE_GREEN", "case_role": "separator_EV_demand_slowdown_false_green_counterexample", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023/2024 forward window", "current_profile_error": true, "current_profile_verdict": "Separator demand-slowdown risk should remain Yellow or local 4B when price confirmation is not followed by customer call-off, utilization absorption, delivery cadence, ASP/input-cost pass-through and margin/revision evidence. The July 2023 spike had limited residual upside and a much larger drawdown once EV/customer demand concerns dominated.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.5, "entry_date": "2023-07-26", "entry_price": 108600, "evidence_family": "separator_EV_demand_slowdown_price_confirmation_without_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_FOIL_EV_DEMAND_SLOWDOWN_CALLOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-27", "low_price_180d": 59400, "peak_date": "2023-07-26", "peak_price": 120000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"ASP_input_cost_margin_bridge": 3, "EV_demand_slowdown_salience": 9, "customer_calloff_risk": 8, "information_confidence": 3, "inventory_or_utilization_pressure": 8, "market_mispricing": 4, "non_price_evidence_refresh": 2, "total": 45, "valuation_blowoff_risk": 8}, "reuse_reason": null, "same_entry_group_id": "C14_361610_SKIET_20230726_SEPARATOR_CALLOFF_SLOWDOWN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_slowdown_absence_required_for_positive", "customer_calloff_and_delivery_visibility_required", "utilization_ASP_inputcost_margin_revision_route_required"], "stage3_evidence_fields": ["customer_calloff_conversion_required", "utilization_absorption_and_inventory_required", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["battery_separator_foil_price_premium", "EV_demand_slowdown_calloff_risk", "post_peak_drawdown"], "stage4c_evidence_fields": ["EV_demand_slowdown_acceleration", "customer_calloff_gap_or_contract_delay", "utilization_margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SEPARATOR_FOIL_EV_DEMAND_SLOWDOWN_CALLOFF_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "EV_demand_slowdown_separator_foil_calloff_risk_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C14 EV-demand-slowdown rows should block Stage2/Green for separator/foil premiums when demand slowdown, call-off uncertainty, utilization pressure and margin-revision exhaustion dominate; positive labels require non-price evidence that customer call-offs and margin revisions are still expanding.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C14 + symbol + trigger_type + entry_date.
3. Add C14-specific EV-demand slowdown / customer call-off / utilization / ASP-input-cost / margin-revision / 4B-4C guard only as a shadow candidate until more rows exist.

Candidate rule:
- C14_BLOCK_GREEN_WHEN_EV_DEMAND_SLOWDOWN_CALLOFF_RISK_VISIBLE
- C14_SEPARATOR_FOIL_PRICE_PREMIUM_LOCAL_4B
- C14_GREEN_REQUIRES_CUSTOMER_PULL_UTILIZATION_AND_MARGIN_REVISION
- C14_PRICE_STRENGTH_WITHOUT_CALLOFF_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

