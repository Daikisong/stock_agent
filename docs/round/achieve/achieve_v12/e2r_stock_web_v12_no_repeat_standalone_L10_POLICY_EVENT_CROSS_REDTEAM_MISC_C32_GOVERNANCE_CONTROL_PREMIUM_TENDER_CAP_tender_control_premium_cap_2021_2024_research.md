# E2R V12 No-Repeat Standalone Residual Research
## R13 / L10 / C32 — Governance control premium / public tender cap guard

metadata:
```text
selected_round: R13
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: PUBLIC_TENDER_CONTROL_PREMIUM_CAP_SPREAD_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_tender_control_premium_cap_2021_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP current coverage:
rows=64, symbols=10, date range=2020-11-16~2024-12-06, good/bad S2=22/13, 4B/4C=12/4
top covered symbols: 010130(18), 041510(14), 000240(5), 고려아연(5), 에스엠(4)
```

This run avoids those top-covered C32 symbols and adds 003410, 115390, and 009240.  
Each row uses a new `C32 + symbol + trigger_type + entry_date` hard key.

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
009240 한샘: corporate_action_candidate_count=0.
003410 쌍용C&E: selected 2024 forward window is clean relative to old corporate-action candidates; delisting/tender end-state is treated as an event-specific caveat.
115390 락앤락: corporate_action_candidate_count=0; inactive/delisted-like row status is an event-specific caveat after the selected tender-cap window.
```

## 3. Research thesis

C32 should not treat every governance headline as a fundamental rerating. It needs to split two very different mechanisms:

```text
firm public tender / delisting offer
→ offer price becomes a ceiling/floor reference
→ residual spread and completion probability determine return

loose control-premium headline
→ price gaps before a firm tender floor
→ fundamental bridge must still prove itself
→ otherwise local 4B/counterexample
```

A tender is a bridge with a toll booth. A control-premium rumor is only a road sign. The model should not pay bridge prices for a sign.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C32_003410_SSANGYONGCNE_20240205_PUBLIC_TENDER_CAP_POSITIVE | 003410 | positive_tender_cap_convergence | 2024-02-05 | 6940 | 7040 on 2024-03-15 | 6780 on 2024-03-05 | 1.44% | 1.44% | 1.44% | -2.31% | -0.57% |
| C32_115390_LOCKNLOCK_20240418_PUBLIC_TENDER_CAP_POSITIVE | 115390 | positive_tender_cap_convergence | 2024-04-18 | 8680 | 8890 on 2024-05-08 | 8630 on 2024-05-14 | 2.42% | 2.42% | 2.42% | -0.58% | -2.92% |
| C32_009240_HANSSEM_20210714_CONTROL_PREMIUM_FALSE_GREEN | 009240 | control_premium_false_green_counterexample | 2021-07-14 | 146500 | 149000 on 2021-07-14 | 68900 on 2022-01-28 | 1.71% | 1.71% | 1.71% | -52.97% | -53.76% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Firm public-tender or delisting-offer visibility can create a Stage2 spread/cap trade.
- 003410 and 115390 are positive cap-convergence rows: the price path compressed toward the offer cap with limited residual movement. The correct question was not “how much can earnings rerate?” but “what is the remaining spread and completion probability?”

### Stage3 / Green
- C32 Green should not be granted merely because a control premium exists.
- If a firm tender floor exists, the trade should be modeled as capped event-spread, not open-ended Green.
- If no firm tender floor exists, the stock needs a separate operating, margin, capital-return or strategic-value bridge.

### 4B
- 009240 is the control-premium false-Green row. The stock gapped on control-premium expectations, but there was no tender-floor behavior to protect the entry and no durable fundamental bridge to carry the premium.
- Local 4B should activate after the price gap when incremental non-price evidence fails to expand.

### 4C
- No hard deal-failure 4C is asserted here.
- The C32 break mode in this file is cap-mechanism mismatch: the market prices a control event, but the model must know whether it is a capped spread trade or a loose premium that can evaporate.

## 6. Raw component score breakdown

```json
{
  "C32_003410_SSANGYONGCNE_20240205_PUBLIC_TENDER_CAP_POSITIVE": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 4,
    "eps_fcf_explosion": 2,
    "information_confidence": 4,
    "market_mispricing": 8,
    "total": 35,
    "valuation_rerating_runway": 1,
    "visibility_quality": 13
  },
  "C32_009240_HANSSEM_20210714_CONTROL_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 2,
    "eps_fcf_explosion": 3,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 21,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  },
  "C32_115390_LOCKNLOCK_20240418_PUBLIC_TENDER_CAP_POSITIVE": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 4,
    "eps_fcf_explosion": 2,
    "information_confidence": 4,
    "market_mispricing": 7,
    "total": 33,
    "valuation_rerating_runway": 1,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C32 guard:
```text
if firm_public_tender_offer and offer_price_visible:
    classify = capped_event_spread
    block_open_ended_stage3_green = true
    score_completion_probability_and_remaining_spread = true

if control_premium_headline and no firm_tender_floor:
    cap_stage = Stage3-Yellow
    route_to_local_4B_watch = true

if post_gap_drawdown and no fundamental_or_capital_return_bridge:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 009240 / 2021-07-14: control-premium price gap can be over-promoted if the model treats the headline like a tender floor.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -2.31, "MAE_30D_pct": -2.31, "MAE_90D_pct": -2.31, "MFE_180D_pct": 1.44, "MFE_30D_pct": 1.44, "MFE_90D_pct": 1.44, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_003410_SSANGYONGCNE_20240205_PUBLIC_TENDER_CAP_POSITIVE", "case_role": "positive_tender_cap_convergence", "company_name": "쌍용C&E", "corporate_action_window_status": "clean_selected_forward_window; delisting/tender end-state handled as event-specific caveat where applicable", "current_profile_error": false, "current_profile_verdict": "Tender/delisting cap logic worked: once the public-offer price was effectively the ceiling, the useful signal was cap-convergence and downside control, not an open-ended Green rerating.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -0.57, "entry_date": "2024-02-05", "entry_price": 6940, "evidence_family": "public_tender_delisting_cap_convergence_with_limited_residual_upside", "evidence_url_pending": false, "fine_archetype_id": "PUBLIC_TENDER_CONTROL_PREMIUM_CAP_SPREAD_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-03-05", "low_price_180d": 6780, "peak_date": "2024-03-15", "peak_price": 7040, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003410.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 4, "eps_fcf_explosion": 2, "information_confidence": 4, "market_mispricing": 8, "total": 35, "valuation_rerating_runway": 1, "visibility_quality": 13}, "reuse_reason": null, "same_entry_group_id": "C32_003410_SSANGYONGCNE_20240205_PUBLIC_TENDER_CAP_POSITIVE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["governance_control_premium_or_public_tender_attention", "firm_offer_price_or_control_transaction_visibility", "completion_probability_or_spread_capture_signal"], "stage3_evidence_fields": ["firm_tender_floor_or_contractual_offer_required", "residual_spread_and_completion_probability_required", "fundamental_margin_or_capital_return_bridge_required_if_no_tender_floor"], "stage4b_evidence_fields": ["control_premium_price_gap", "tender_cap_or_offer_price_ceiling", "post_gap_residual_upside_exhaustion"], "stage4c_evidence_fields": ["deal_completion_or_tender_failure_risk", "control_premium_without_offer_floor", "fundamental_bridge_failure_after_price_gap"], "symbol": "003410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003410/2024.csv", "trigger_date": "2024-02-05", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -0.58, "MAE_30D_pct": -0.58, "MAE_90D_pct": -0.58, "MFE_180D_pct": 2.42, "MFE_30D_pct": 2.42, "MFE_90D_pct": 2.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_115390_LOCKNLOCK_20240418_PUBLIC_TENDER_CAP_POSITIVE", "case_role": "positive_tender_cap_convergence", "company_name": "락앤락", "corporate_action_window_status": "clean_selected_forward_window; delisting/tender end-state handled as event-specific caveat where applicable", "current_profile_error": false, "current_profile_verdict": "Public tender cap treatment was correct: the stock behaved like a spread/cap situation, where the edge is offer completion probability and remaining spread, not fundamental rerating.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -2.92, "entry_date": "2024-04-18", "entry_price": 8680, "evidence_family": "public_tender_cap_spread_capture_with_low_path_volatility", "evidence_url_pending": false, "fine_archetype_id": "PUBLIC_TENDER_CONTROL_PREMIUM_CAP_SPREAD_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-05-14", "low_price_180d": 8630, "peak_date": "2024-05-08", "peak_price": 8890, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/115/115390.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 4, "eps_fcf_explosion": 2, "information_confidence": 4, "market_mispricing": 7, "total": 33, "valuation_rerating_runway": 1, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C32_115390_LOCKNLOCK_20240418_PUBLIC_TENDER_CAP_POSITIVE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["governance_control_premium_or_public_tender_attention", "firm_offer_price_or_control_transaction_visibility", "completion_probability_or_spread_capture_signal"], "stage3_evidence_fields": ["firm_tender_floor_or_contractual_offer_required", "residual_spread_and_completion_probability_required", "fundamental_margin_or_capital_return_bridge_required_if_no_tender_floor"], "stage4b_evidence_fields": ["control_premium_price_gap", "tender_cap_or_offer_price_ceiling", "post_gap_residual_upside_exhaustion"], "stage4c_evidence_fields": ["deal_completion_or_tender_failure_risk", "control_premium_without_offer_floor", "fundamental_bridge_failure_after_price_gap"], "symbol": "115390", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/115/115390/2024.csv", "trigger_date": "2024-04-18", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -52.97, "MAE_30D_pct": -27.99, "MAE_90D_pct": -44.71, "MFE_180D_pct": 1.71, "MFE_30D_pct": 1.71, "MFE_90D_pct": 1.71, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32_009240_HANSSEM_20210714_CONTROL_PREMIUM_FALSE_GREEN", "case_role": "control_premium_false_green_counterexample", "company_name": "한샘", "corporate_action_window_status": "clean_selected_forward_window; delisting/tender end-state handled as event-specific caveat where applicable", "current_profile_error": true, "current_profile_verdict": "Control-premium headlines should not become Green when there is no firm tender floor or operating-recovery bridge; after the price gap, the signal should route to local 4B/counterexample.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.76, "entry_date": "2021-07-14", "entry_price": 146500, "evidence_family": "control_premium_headline_without_fundamental_margin_recovery_or_tender_floor", "evidence_url_pending": false, "fine_archetype_id": "PUBLIC_TENDER_CONTROL_PREMIUM_CAP_SPREAD_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2022-01-28", "low_price_180d": 68900, "peak_date": "2021-07-14", "peak_price": 149000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009240.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 2, "eps_fcf_explosion": 3, "information_confidence": 3, "market_mispricing": 4, "total": 21, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C32_009240_HANSSEM_20210714_CONTROL_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["governance_control_premium_or_public_tender_attention", "firm_offer_price_or_control_transaction_visibility", "completion_probability_or_spread_capture_signal"], "stage3_evidence_fields": ["firm_tender_floor_or_contractual_offer_required", "residual_spread_and_completion_probability_required", "fundamental_margin_or_capital_return_bridge_required_if_no_tender_floor"], "stage4b_evidence_fields": ["control_premium_price_gap", "tender_cap_or_offer_price_ceiling", "post_gap_residual_upside_exhaustion"], "stage4c_evidence_fields": ["deal_completion_or_tender_failure_risk", "control_premium_without_offer_floor", "fundamental_bridge_failure_after_price_gap"], "symbol": "009240", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv", "trigger_date": "2021-07-14", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "PUBLIC_TENDER_CONTROL_PREMIUM_CAP_SPREAD_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "loop_contribution_label": "governance_tender_cap_control_premium_new_symbols_added",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R13",
  "shadow_rule_candidate": "C32 governance/control-premium rows should split firm public-tender cap spread from loose control-premium price gaps: tender-cap rows are spread/completion-probability trades, while control-premium headlines without a firm tender floor should route to local 4B or counterexample unless fundamental margin/capital-return bridge also closes.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C32 + symbol + trigger_type + entry_date.
3. Add C32-specific tender-cap / control-premium split only as a shadow candidate until more rows exist.

Candidate rule:
- C32_TENDER_CAP_CLASSIFY_AS_EVENT_SPREAD_NOT_GREEN
- C32_GREEN_BLOCK_IF_OFFER_PRICE_CAPS_UPSIDE
- C32_CONTROL_PREMIUM_WITHOUT_TENDER_FLOOR_LOCAL_4B
- C32_POST_GAP_NO_FUNDAMENTAL_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

