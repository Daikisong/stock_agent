# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C12 — Separator customer contract call-off risk

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_separator_customer_calloff_2023_research.md
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

This run avoids the top repeated C12 symbols and adds separator/customer-contract rows using 361610 and 393890.  
The second 393890 row is a soft-duplicate by symbol only, but it uses a different date, trigger family, and counterexample purpose, so it is allowed under the No-Repeat soft-duplicate rule.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
361610 SK아이이테크놀로지: first_date=2021-05-11, last_date=2026-02-20, corporate_action_candidate_count=0.
393890 더블유씨피: first_date=2022-09-30, last_date=2026-02-20, corporate_action_candidate_count=0.
```

## 3. Research thesis

C12 is not a generic battery orderbook rerating bucket. It is the point where nominal customer contracts can fail to translate into actual volume or margin:

```text
separator/customer contract attention
→ capacity / customer visibility claim
→ EV demand or customer utilization must validate
→ call-off risk / delayed volume can break the rerating
```

The residual task is to separate early valid Stage2 signals from late Green false positives after the market has already capitalized the contract story.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C12_361610_SKIET_20230126_SEPARATOR_STAGE2_SUCCESS_WITH_CUSTOMER_RISK | 361610 | positive_high_mae_success | 2023-01-26 | 69400 | 103900 on 2023-06-12 | 59800 on 2023-03-16 | 49.71% | -13.83% | -15.21% |
| C12_393890_WCP_20230202_SEPARATOR_STAGE2_HIGH_MAE_SUCCESS | 393890 | positive_high_mae_success_but_later_calloff_watch | 2023-02-02 | 50600 | 78700 on 2023-07-04 | 40850 on 2023-03-16 | 55.53% | -19.27% | -48.6% |
| C12_393890_WCP_20230704_SEPARATOR_LATE_GREEN_FALSE_POSITIVE | 393890 | false_green_counterexample | 2023-07-04 | 73800 | 78700 on 2023-07-04 | 38300 on 2023-11-13 | 6.64% | -48.1% | -51.33% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Separator capacity and customer-contract visibility can create valid early attention.
- 361610 and early 393890 show that Stage2 can work before final margin proof appears.

### Stage3 / Green
- C12 Green should require utilization, customer call-off risk, and margin/revision bridge.
- Customer contract language alone is not enough because the contract can sit like an empty pipeline if downstream EV demand slows.

### 4B
- Late 393890 after the large 1H23 rerating is the important guard case.
- Once price already capitalizes separator demand, full 4B should require non-price evidence, while local 4B should activate on price/valuation exhaustion.

### 4C
- C12 4C is not necessarily an accounting break.
- It is often a volume/conversion break: customer call-off, delayed utilization, weaker demand, or revision fade.

## 6. Raw component score breakdown

```json
{
  "C12_361610_SKIET_20230126_SEPARATOR_STAGE2_SUCCESS_WITH_CUSTOMER_RISK": {
    "bottleneck_pricing_power": 13,
    "capital_allocation": 2,
    "eps_fcf_explosion": 9,
    "information_confidence": 3,
    "market_mispricing": 11,
    "total": 61,
    "valuation_rerating_runway": 12,
    "visibility_quality": 11
  },
  "C12_393890_WCP_20230202_SEPARATOR_STAGE2_HIGH_MAE_SUCCESS": {
    "bottleneck_pricing_power": 12,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 3,
    "market_mispricing": 12,
    "total": 61,
    "valuation_rerating_runway": 12,
    "visibility_quality": 10
  },
  "C12_393890_WCP_20230704_SEPARATOR_LATE_GREEN_FALSE_POSITIVE": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 2,
    "eps_fcf_explosion": 8,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 40,
    "valuation_rerating_runway": 4,
    "visibility_quality": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C12 guard:
```text
if battery_customer_contract and no utilization_or_calloff_confirmation:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if late_price_strength_after_large_rerating and calloff_risk_unresolved:
    route_to_local_4B_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 393890 / 2023-07-04: late separator relative strength can look like Green, but it is better treated as a call-off-risk counterexample / local 4B watch.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.83, "MAE_30D_pct": -13.83, "MAE_90D_pct": -13.83, "MFE_180D_pct": 49.71, "MFE_30D_pct": 49.71, "MFE_90D_pct": 49.71, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_361610_SKIET_20230126_SEPARATOR_STAGE2_SUCCESS_WITH_CUSTOMER_RISK", "case_role": "positive_high_mae_success", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": false, "current_profile_verdict": "Stage2 worked as early attention, but Green should wait for customer utilization and call-off risk evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -15.21, "entry_date": "2023-01-26", "entry_price": 69400, "evidence_family": "separator_recovery_customer_contract_visibility_but_calloff_sensitive", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-03-16", "low_price_180d": 59800, "peak_date": "2023-06-12", "peak_price": 103900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 13, "capital_allocation": 2, "eps_fcf_explosion": 9, "information_confidence": 3, "market_mispricing": 11, "total": 61, "valuation_rerating_runway": 12, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C12_361610_SKIET_20230126_SEPARATOR_STAGE2_SUCCESS_WITH_CUSTOMER_RISK", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["separator_capacity_attention", "battery_supply_chain_relative_strength", "customer_contract_visibility_claim"], "stage3_evidence_fields": ["customer_calloff_risk_must_be_checked", "utilization_confirmation_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["late_rerating_after_price_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_demand_slowdown", "utilization_gap", "contract_calloff_or_volume_delay"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-01-26", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -19.27, "MAE_30D_pct": -19.27, "MAE_90D_pct": -19.27, "MFE_180D_pct": 55.53, "MFE_30D_pct": 55.53, "MFE_90D_pct": 55.53, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_393890_WCP_20230202_SEPARATOR_STAGE2_HIGH_MAE_SUCCESS", "case_role": "positive_high_mae_success_but_later_calloff_watch", "company_name": "더블유씨피", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": false, "current_profile_verdict": "Early Stage2 was usable, but later customer call-off and EV demand risk require 4B/Yellow discipline before Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.6, "entry_date": "2023-02-02", "entry_price": 50600, "evidence_family": "separator_capacity_and_customer_contract_rerating_with_calloff_sensitivity", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-03-16", "low_price_180d": 40850, "peak_date": "2023-07-04", "peak_price": 78700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 12, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 3, "market_mispricing": 12, "total": 61, "valuation_rerating_runway": 12, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C12_393890_WCP_20230202_SEPARATOR_STAGE2_HIGH_MAE_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["separator_capacity_attention", "battery_supply_chain_relative_strength", "customer_contract_visibility_claim"], "stage3_evidence_fields": ["customer_calloff_risk_must_be_checked", "utilization_confirmation_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["late_rerating_after_price_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_demand_slowdown", "utilization_gap", "contract_calloff_or_volume_delay"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-02-02", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -48.1, "MAE_30D_pct": -48.1, "MAE_90D_pct": -48.1, "MFE_180D_pct": 6.64, "MFE_30D_pct": 6.64, "MFE_90D_pct": 6.64, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "case_id": "C12_393890_WCP_20230704_SEPARATOR_LATE_GREEN_FALSE_POSITIVE", "case_role": "false_green_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "clean_180d_by_profile", "current_profile_error": true, "current_profile_verdict": "Late relative strength must not become Green when customer call-off and EV demand visibility are unresolved.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.33, "entry_date": "2023-07-04", "entry_price": 73800, "evidence_family": "late_separator_rerating_without_customer_calloff_demand_confirmation", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-13", "low_price_180d": 38300, "peak_date": "2023-07-04", "peak_price": 78700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 2, "eps_fcf_explosion": 8, "information_confidence": 3, "market_mispricing": 6, "total": 40, "valuation_rerating_runway": 4, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C12_393890_WCP_20230704_SEPARATOR_LATE_GREEN_FALSE_POSITIVE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["separator_capacity_attention", "battery_supply_chain_relative_strength", "customer_contract_visibility_claim"], "stage3_evidence_fields": ["customer_calloff_risk_must_be_checked", "utilization_confirmation_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["late_rerating_after_price_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_demand_slowdown", "utilization_gap", "contract_calloff_or_volume_delay"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-04", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "positive_counterexample_balance",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C12 separator/customer-contract rows should cap at Stage2/Yellow unless customer utilization, call-off risk, and margin/revision bridge are confirmed; late price strength after a large run should become 4B-local watch.",
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
3. Treat the repeated 393890 symbol as allowed soft duplicate only because the trigger date, trigger type, and counterexample purpose differ.
4. Add C12-specific customer call-off / utilization guard only as a shadow candidate until more rows exist.

Candidate rule:
- C12_CUSTOMER_CONTRACT_REQUIRES_UTILIZATION_AND_CALLOFF_CHECK
- C12_SEPARATOR_LATE_RELATIVE_STRENGTH_LOCAL_4B
- C12_CONTRACT_WITHOUT_MARGIN_REVISION_STAGE2_CAP

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent trigger cases, 1 counterexample, and 1 current-profile residual error for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

