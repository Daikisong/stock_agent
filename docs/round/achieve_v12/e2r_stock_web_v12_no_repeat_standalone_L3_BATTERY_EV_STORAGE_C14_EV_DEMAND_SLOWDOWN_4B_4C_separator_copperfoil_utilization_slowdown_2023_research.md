# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C14 — EV demand slowdown 4B/4C / separator-copperfoil utilization guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_STORAGE
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: SEPARATOR_COPPERFOIL_UTILIZATION_SLOWDOWN_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_4C_gap_fill|EV_demand_slowdown_utilization_calloff_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_STORAGE_C14_EV_DEMAND_SLOWDOWN_4B_4C_separator_copperfoil_utilization_slowdown_2023_research.md
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

This run avoids those top-covered C14 symbols and adds 361610, 020150, and 011790.  
Each row uses a new `C14 + symbol + trigger_type + entry_date` hard key:
```text
C14 + 361610 + 4B-protective + 2023-06-12
C14 + 020150 + Stage3-Yellow + 2023-07-05
C14 + 011790 + 4B-local-price-only + 2023-06-13
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

C14 should distinguish true EV-demand recovery from a recovery-looking price bounce inside unresolved volume/utilization slowdown:

```text
EV demand slowdown
→ customer call-off or volume risk
→ shipment cadence and backlog conversion
→ separator / copper-foil utilization
→ ASP/mix and working-capital pressure
→ margin and revision bridge
→ local/protective 4B or 4C watch until repair
```

An EV slowdown is a conveyor belt losing speed. Stage2 can buy only when the belt visibly accelerates again. A price bounce while shipments, utilization and margin revisions remain unresolved is just the belt making noise, not freight moving.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C14_361610_SKIET_20230612_SEPARATOR_EV_DEMAND_SLOWDOWN_4B_PROTECTIVE | 361610 | protective_separator_EV_demand_slowdown_4B_success | 2023-06-12 | 103000 | 103900 on 2023-06-12 | 58700 on 2023-10-31 | 0.87% | 0.87% | 0.87% | -43.01% | -43.5% |
| C14_020150_LOTTEEM_20230705_COPPERFOIL_EV_DEMAND_FALSE_GREEN | 020150 | copperfoil_EV_demand_slowdown_false_green_counterexample | 2023-07-05 | 58000 | 59700 on 2023-07-26 | 36650 on 2023-10-26 | 2.93% | 2.93% | 2.93% | -36.81% | -38.61% |
| C14_011790_SKC_20230613_COPPERFOIL_EV_DEMAND_PRICE_PREMIUM_4B | 011790 | copperfoil_EV_demand_slowdown_price_premium_4B_counterexample | 2023-06-13 | 110000 | 111500 on 2023-06-13 | 68000 on 2023-10-23 | 1.36% | 1.36% | 1.36% | -38.18% | -39.01% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C14 Stage2/Green requires visible demand repair: customer call-off clarity, shipment cadence, utilization recovery, ASP/mix stabilization, working-capital quality and margin/revision confirmation.
- 가격만 있는 rebound는 Stage2/Green positive로 금지된다. The positive row here is protective 4B, not a buy-positive Green row.

### Stage3 / Green
- C14 Green should be blocked when EV-demand slowdown is still unresolved and price confirmation substitutes for utilization or margin evidence.
- 020150 is the false-Green/Yellow guard: copper-foil recovery-looking price confirmation had tiny residual upside and a much larger forward drawdown when utilization-to-margin evidence did not refresh.

### 4B
- 361610 is the protective 4B anchor. The separator/customer-capacity story remained real, but the June 2023 price path had almost no residual runway and a large full-window drawdown.
- 011790 fills the copper-foil price-premium 4B pocket.
- The core 4B rule is that EV-recovery salience should not substitute for shipment cadence, utilization and margin-revision evidence.

### 4C
- No hard customer cancellation or accounting break is asserted.
- The C14 break mode here is utilization-to-margin exhaustion: the EV demand story may remain directionally real, but incremental call-off clarity, utilization, ASP/mix and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C14_011790_SKC_20230613_COPPERFOIL_EV_DEMAND_PRICE_PREMIUM_4B": {
    "ASP_mix_margin_revision_bridge": 2,
    "EV_demand_slowdown_salience": 9,
    "customer_calloff_or_volume_risk": 9,
    "information_confidence": 3,
    "price_premium_or_blowoff_risk": 9,
    "shipment_cadence_quality": 2,
    "total": 39,
    "utilization_recovery_visibility": 2,
    "valuation_rerating_runway": 0,
    "working_capital_quality": 3
  },
  "C14_020150_LOTTEEM_20230705_COPPERFOIL_EV_DEMAND_FALSE_GREEN": {
    "ASP_mix_margin_revision_bridge": 2,
    "EV_demand_slowdown_salience": 9,
    "customer_calloff_or_volume_risk": 9,
    "information_confidence": 3,
    "price_premium_or_blowoff_risk": 8,
    "shipment_cadence_quality": 2,
    "total": 39,
    "utilization_recovery_visibility": 2,
    "valuation_rerating_runway": 1,
    "working_capital_quality": 3
  },
  "C14_361610_SKIET_20230612_SEPARATOR_EV_DEMAND_SLOWDOWN_4B_PROTECTIVE": {
    "ASP_mix_margin_revision_bridge": 2,
    "EV_demand_slowdown_salience": 10,
    "customer_calloff_or_volume_risk": 10,
    "information_confidence": 4,
    "price_premium_or_blowoff_risk": 10,
    "shipment_cadence_quality": 2,
    "total": 43,
    "utilization_recovery_visibility": 2,
    "valuation_rerating_runway": 0,
    "working_capital_quality": 3
  }
}
```

## 7. Current calibrated profile stress test

Suggested C14 guard:
```text
if EV_recovery_price_bounce and no calloff_shipment_utilization_margin_revision_bridge:
    block_stage2_green_positive = true
    route_to_stage3_yellow_or_local_4B = true

if utilization_or_volume_risk_visible and valuation_runway_thin:
    route_to_protective_4B = true

if post_peak_drawdown and utilization_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 020150 / 2023-07-05: copper-foil recovery confirmation can be over-promoted if price strength substitutes for utilization and margin proof.
- 011790 / 2023-06-13: copper-foil EV-demand premium can look actionable, but fails without refreshed customer call-off, shipment and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -43.01, "MAE_30D_pct": -12.91, "MAE_90D_pct": -20.97, "MFE_180D_pct": 0.87, "MFE_30D_pct": 0.87, "MFE_90D_pct": 0.87, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_361610_SKIET_20230612_SEPARATOR_EV_DEMAND_SLOWDOWN_4B_PROTECTIVE", "case_role": "protective_separator_EV_demand_slowdown_4B_success", "company_name": "SK아이이테크놀로지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023 forward window", "current_profile_error": false, "current_profile_verdict": "Protective 4B routing was useful: separator/customer-capacity optionality was visible, but the June 2023 price already capitalized much of the recovery while EV demand, utilization, shipment cadence and margin revision risk were unresolved. The full-window path had almost no residual MFE and a large MAE, so it should not be promoted to Stage2/Green without utilization recovery, customer call-off clarity and margin bridge evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.5, "entry_date": "2023-06-12", "entry_price": 103000, "evidence_family": "separator_customer_capacity_EV_demand_slowdown_utilization_margin_risk_4B_route", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_UTILIZATION_SLOWDOWN_4B_GUARD", "forward_window_trading_days": 180, "historical_name": null, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-10-31", "low_price_180d": 58700, "peak_date": "2023-06-12", "peak_price": 103900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/361/361610.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 2, "EV_demand_slowdown_salience": 10, "customer_calloff_or_volume_risk": 10, "information_confidence": 4, "price_premium_or_blowoff_risk": 10, "shipment_cadence_quality": 2, "total": 43, "utilization_recovery_visibility": 2, "valuation_rerating_runway": 0, "working_capital_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C14_361610_SKIET_20230612_SEPARATOR_EV_DEMAND_SLOWDOWN_4B_PROTECTIVE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_slowdown_absence_or_reversal_required_for_positive", "customer_calloff_visibility_required", "utilization_shipment_margin_revision_route_required"], "stage3_evidence_fields": ["EV_demand_volume_recovery_required", "shipment_cadence_and_customer_calloff_clarity_required", "utilization_ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["EV_demand_slowdown_price_premium_or_rebound", "utilization_recovery_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_volume_shortfall", "utilization_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "361610", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv", "trigger_date": "2023-06-12", "trigger_type": "4B-protective", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.81, "MAE_30D_pct": -18.88, "MAE_90D_pct": -31.98, "MFE_180D_pct": 2.93, "MFE_30D_pct": 2.93, "MFE_90D_pct": 2.93, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_020150_LOTTEEM_20230705_COPPERFOIL_EV_DEMAND_FALSE_GREEN", "case_role": "copperfoil_EV_demand_slowdown_false_green_counterexample", "company_name": "롯데에너지머티리얼즈", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023 forward window; name changed from 일진머티리얼즈 to 롯데에너지머티리얼즈 during the research window", "current_profile_error": true, "current_profile_verdict": "Copper-foil EV-demand-slowdown confirmation should remain Yellow or local 4B when price strength is not backed by customer call-off clarity, shipment cadence, utilization recovery, ASP/mix and margin/revision evidence. The July 2023 trigger had tiny residual MFE and a much larger forward MAE, so a recovery-looking bounce was not a clean Stage2/Green positive.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.61, "entry_date": "2023-07-05", "entry_price": 58000, "evidence_family": "copperfoil_EV_demand_slowdown_price_confirmation_without_utilization_shipment_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_UTILIZATION_SLOWDOWN_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "일진머티리얼즈", "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-10-26", "low_price_180d": 36650, "peak_date": "2023-07-26", "peak_price": 59700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020150.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 2, "EV_demand_slowdown_salience": 9, "customer_calloff_or_volume_risk": 9, "information_confidence": 3, "price_premium_or_blowoff_risk": 8, "shipment_cadence_quality": 2, "total": 39, "utilization_recovery_visibility": 2, "valuation_rerating_runway": 1, "working_capital_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C14_020150_LOTTEEM_20230705_COPPERFOIL_EV_DEMAND_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_slowdown_absence_or_reversal_required_for_positive", "customer_calloff_visibility_required", "utilization_shipment_margin_revision_route_required"], "stage3_evidence_fields": ["EV_demand_volume_recovery_required", "shipment_cadence_and_customer_calloff_clarity_required", "utilization_ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["EV_demand_slowdown_price_premium_or_rebound", "utilization_recovery_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_volume_shortfall", "utilization_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "020150", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2023.csv", "trigger_date": "2023-07-05", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.18, "MAE_30D_pct": -10.91, "MAE_90D_pct": -24.18, "MFE_180D_pct": 1.36, "MFE_30D_pct": 1.36, "MFE_90D_pct": 1.36, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_011790_SKC_20230613_COPPERFOIL_EV_DEMAND_PRICE_PREMIUM_4B", "case_role": "copperfoil_EV_demand_slowdown_price_premium_4B_counterexample", "company_name": "SKC", "corporate_action_window_status": "selected 2023 forward window clean; historical name/corporate-action candidates are outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Copper-foil EV-demand-slowdown premium should route to local 4B/counterexample when the market has already paid for recovery optionality and fresh customer call-off, utilization, shipment cadence, ASP/mix and margin-revision evidence do not refresh. The June 2023 trigger had almost no residual upside and a large drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -39.01, "entry_date": "2023-06-13", "entry_price": 110000, "evidence_family": "copperfoil_EV_demand_slowdown_price_premium_without_calloff_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SEPARATOR_COPPERFOIL_UTILIZATION_SLOWDOWN_4B_GUARD", "forward_window_trading_days": 180, "historical_name": null, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_STORAGE", "low_date_180d": "2023-10-23", "low_price_180d": 68000, "peak_date": "2023-06-13", "peak_price": 111500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011790.json", "raw_component_score_breakdown": {"ASP_mix_margin_revision_bridge": 2, "EV_demand_slowdown_salience": 9, "customer_calloff_or_volume_risk": 9, "information_confidence": 3, "price_premium_or_blowoff_risk": 9, "shipment_cadence_quality": 2, "total": 39, "utilization_recovery_visibility": 2, "valuation_rerating_runway": 0, "working_capital_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C14_011790_SKC_20230613_COPPERFOIL_EV_DEMAND_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["EV_demand_slowdown_absence_or_reversal_required_for_positive", "customer_calloff_visibility_required", "utilization_shipment_margin_revision_route_required"], "stage3_evidence_fields": ["EV_demand_volume_recovery_required", "shipment_cadence_and_customer_calloff_clarity_required", "utilization_ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["EV_demand_slowdown_price_premium_or_rebound", "utilization_recovery_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_calloff_or_volume_shortfall", "utilization_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "011790", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv", "trigger_date": "2023-06-13", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SEPARATOR_COPPERFOIL_UTILIZATION_SLOWDOWN_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_STORAGE",
  "loop_contribution_label": "EV_demand_slowdown_separator_copperfoil_new_symbols_utilization_calloff_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C14 EV-demand-slowdown rows should block Stage2/Green when customer call-off, utilization, shipment cadence, ASP/mix and margin-revision evidence are unresolved; separator/copper-foil recovery bounces should route to Yellow/local or protective 4B until volume and margin bridge refreshes.",
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
3. Add C14-specific EV-demand slowdown / customer call-off / utilization / shipment cadence / ASP-mix / working-capital / margin-revision / local-protective-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C14_BLOCK_GREEN_WITHOUT_CALLOFF_SHIPMENT_UTILIZATION_MARGIN_REVISION_BRIDGE
- C14_EV_RECOVERY_PRICE_BOUNCE_ROUTES_TO_LOCAL_4B
- C14_PROTECTIVE_4B_WHEN_UTILIZATION_OR_VOLUME_RISK_DOMINATES
- C14_PRICE_CONFIRMATION_WITHOUT_UTILIZATION_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_STORAGE/C14_EV_DEMAND_SLOWDOWN_4B_4C.

