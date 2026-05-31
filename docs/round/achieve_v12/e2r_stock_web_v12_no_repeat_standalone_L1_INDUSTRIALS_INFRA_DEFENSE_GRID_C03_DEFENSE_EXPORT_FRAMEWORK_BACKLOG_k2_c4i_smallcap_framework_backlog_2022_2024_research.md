# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework backlog guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: K2_C4I_DEFENSE_ELECTRONICS_FRAMEWORK_BACKLOG_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_k2_c4i_smallcap_framework_backlog_2022_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG current coverage:
rows=7, symbols=4, date range=2022-07-29~2024-11-12, good/bad S2=4/1, 4B/4C=0/0
top covered symbols: 012450(3), 079550(2), 047810(1), 065450(1)
```

This run avoids those top-covered C03 symbols and adds 064350, 272210, and 005870.  
Each row uses a new `C03 + symbol + trigger_type + entry_date` hard key.

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
064350 현대로템: 2022 forward window clean; corporate-action candidate is 2020-08-14, outside selected test window.
272210 한화시스템: 2022 forward window clean; corporate-action candidate is 2021-06-23, outside selected test window.
005870 휴니드: 2024/2025 forward window clean; corporate-action candidates are historical and outside selected test window.
```

## 3. Research thesis

C03 should not treat a defense export framework headline as fully converted backlog. It should test whether the framework becomes signed, delivered program economics:

```text
defense export framework attention
→ signed tranche and program scope
→ backlog conversion and customer acceptance
→ delivery schedule
→ margin, working capital and revision bridge
→ rerating
```

A framework agreement is the runway, not the aircraft. Stage2 can move when the runway opens, but Green should require the plane: signed scope, delivery slots, accepted systems, cash conversion and margin.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_064350_HYUNDAIROTEM_20220729_K2_POLAND_FRAMEWORK_STAGE2 | 064350 | positive_k2_export_framework_backlog_stage2_success_with_later_4b | 2022-07-29 | 26550 | 32850 on 2022-08-26 | 23050 on 2022-10-27 | 23.73% | 23.73% | 23.73% | -13.18% | -29.83% |
| C03_272210_HANWHASYSTEM_20220729_DEFENSE_C4I_FRAMEWORK_FALSE_GREEN | 272210 | defense_c4i_framework_false_green_counterexample | 2022-07-29 | 14550 | 16200 on 2022-09-01 | 10150 on 2022-10-13 | 11.34% | 11.34% | 11.34% | -30.24% | -37.35% |
| C03_005870_HUNEED_20241112_DEFENSE_ELECTRONICS_SMALLCAP_4B | 005870 | smallcap_defense_electronics_price_premium_counterexample_with_full_window_retest | 2024-11-12 | 9670 | 10840 on 2025-03-24 | 6550 on 2024-12-09 | 0.62% | 12.1% | 12.1% | -32.26% | -34.32% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Defense export frameworks can be valid Stage2 routes when the first tranche, customer acceptance and delivery economics are plausibly close enough to backlog conversion.
- 064350 is the positive anchor: the July 2022 K2/Poland route produced a strong 30D MFE before the late-2022 drawdown showed why framework evidence must mature into signed delivery and margin evidence.

### Stage3 / Green
- C03 Green should require signed scope, tranche conversion, customer acceptance, delivery schedule, working-capital plan, margin and revision confirmation.
- 272210 shows why defense electronics/C4I framework exposure should stay Yellow when the program-specific conversion bridge is weak. The stock confirmed price briefly, but then fell hard as the framework-to-earnings path did not carry the valuation.

### 4B
- 005870 fills the missing local 4B pocket. The November 2024 defense-electronics small-cap spike had theme heat, but the immediate drawdown demanded non-price proof before re-entry.
- 064350 also required later 4B discipline after the original Stage2 rerating became a priced export-framework premium.
- For 005870, the later full-window retest does not erase the local 4B signal; it means the model needs a separate evidence refresh gate rather than treating the original spike as Green.

### 4C
- No hard contract cancellation or delivery failure is asserted.
- The C03 break mode is conversion gap: the framework or defense theme remains real, but signed scope, customer acceptance, delivery cadence, working capital, margin and revision evidence do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C03_005870_HUNEED_20241112_DEFENSE_ELECTRONICS_SMALLCAP_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 23,
    "valuation_rerating_runway": 2,
    "visibility_quality": 4
  },
  "C03_064350_HYUNDAIROTEM_20220729_K2_POLAND_FRAMEWORK_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 54,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  },
  "C03_272210_HANWHASYSTEM_20220729_DEFENSE_C4I_FRAMEWORK_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 28,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C03 guard:
```text
if defense_export_framework_attention and signed_tranche_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if framework_or_smallcap_defense_price_premium and no signed_scope_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and framework_to_order_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 272210 / 2022-07-29: defense electronics framework beta can be over-promoted if the model treats framework attention as signed C4I scope, delivery and margin proof.
- 005870 / 2024-11-12: small-cap defense electronics price premium can become theme-only without program backlog, delivery cadence and revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.18, "MAE_30D_pct": -9.42, "MAE_90D_pct": -13.18, "MFE_180D_pct": 23.73, "MFE_30D_pct": 23.73, "MFE_90D_pct": 23.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20220729_K2_POLAND_FRAMEWORK_STAGE2", "case_role": "positive_k2_export_framework_backlog_stage2_success_with_later_4b", "company_name": "현대로템", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidate is 2020-08-14 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when K-defense export framework/orderbook attention attached to a credible K2 tank delivery backlog before the program economics were fully priced. Green still requires signed tranche conversion, delivery schedule, margin, working-capital and revision bridge; after the August 2022 rerating, the same evidence needed 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.83, "entry_date": "2022-07-29", "entry_price": 26550, "evidence_family": "defense_export_framework_contract_k2_tank_backlog_delivery_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "K2_C4I_DEFENSE_ELECTRONICS_FRAMEWORK_BACKLOG_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-27", "low_price_180d": 23050, "peak_date": "2022-08-26", "peak_price": 32850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 54, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20220729_K2_POLAND_FRAMEWORK_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "signed_tranche_or_program_backlog_visibility", "delivery_schedule_or_margin_revision_signal"], "stage3_evidence_fields": ["signed_scope_and_tranche_conversion_required", "delivery_schedule_and_customer_acceptance_required", "margin_working_capital_or_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_to_signed_order_conversion_gap", "delivery_or_customer_acceptance_delay", "margin_working_capital_revision_bridge_failure"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -30.24, "MAE_30D_pct": -5.15, "MAE_90D_pct": -30.24, "MFE_180D_pct": 11.34, "MFE_30D_pct": 11.34, "MFE_90D_pct": 11.34, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_272210_HANWHASYSTEM_20220729_DEFENSE_C4I_FRAMEWORK_FALSE_GREEN", "case_role": "defense_c4i_framework_false_green_counterexample", "company_name": "한화시스템", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidate is 2021-06-23 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Defense electronics/C4I framework attention should stay Yellow when signed scope, program allocation, export customer delivery schedule, margin and revision evidence do not keep expanding after the framework headline. Price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.35, "entry_date": "2022-07-29", "entry_price": 14550, "evidence_family": "defense_systems_framework_theme_without_signed_scope_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "K2_C4I_DEFENSE_ELECTRONICS_FRAMEWORK_BACKLOG_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-13", "low_price_180d": 10150, "peak_date": "2022-09-01", "peak_price": 16200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/272/272210.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 28, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C03_272210_HANWHASYSTEM_20220729_DEFENSE_C4I_FRAMEWORK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "signed_tranche_or_program_backlog_visibility", "delivery_schedule_or_margin_revision_signal"], "stage3_evidence_fields": ["signed_scope_and_tranche_conversion_required", "delivery_schedule_and_customer_acceptance_required", "margin_working_capital_or_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_to_signed_order_conversion_gap", "delivery_or_customer_acceptance_delay", "margin_working_capital_revision_bridge_failure"], "symbol": "272210", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -32.26, "MAE_30D_pct": -32.26, "MAE_90D_pct": -32.26, "MFE_180D_pct": 12.1, "MFE_30D_pct": 0.62, "MFE_90D_pct": 12.1, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_005870_HUNEED_20241112_DEFENSE_ELECTRONICS_SMALLCAP_4B", "case_role": "smallcap_defense_electronics_price_premium_counterexample_with_full_window_retest", "company_name": "휴니드", "corporate_action_window_status": "clean_2024/2025_forward_window; corporate-action candidates are historical and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Small-cap defense electronics price premium should route to local 4B when theme heat is not followed by explicit program scope, backlog conversion, delivery cadence, margin and revision evidence. A later full-window retest does not erase the local 4B warning; it requires fresh non-price evidence before re-entry.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.32, "entry_date": "2024-11-12", "entry_price": 9670, "evidence_family": "defense_electronics_smallcap_price_premium_without_program_backlog_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "K2_C4I_DEFENSE_ELECTRONICS_FRAMEWORK_BACKLOG_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 6550, "peak_date": "2025-03-24", "peak_price": 10840, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005870.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 23, "valuation_rerating_runway": 2, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C03_005870_HUNEED_20241112_DEFENSE_ELECTRONICS_SMALLCAP_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "signed_tranche_or_program_backlog_visibility", "delivery_schedule_or_margin_revision_signal"], "stage3_evidence_fields": ["signed_scope_and_tranche_conversion_required", "delivery_schedule_and_customer_acceptance_required", "margin_working_capital_or_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_to_signed_order_conversion_gap", "delivery_or_customer_acceptance_delay", "margin_working_capital_revision_bridge_failure"], "symbol": "005870", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005870/2024.csv", "trigger_date": "2024-11-12", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "K2_C4I_DEFENSE_ELECTRONICS_FRAMEWORK_BACKLOG_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_backlog_k2_c4i_smallcap_new_symbols_and_4b_gap",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense export/framework backlog rows should allow Stage2 when framework export attention is backed by signed tranche conversion, program backlog and delivery economics, but Stage3 Green requires signed scope, delivery schedule, customer acceptance, margin, working-capital and revision bridge; small-cap or defense-electronics price premium without program-backlog proof should route to Yellow/local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C03 + symbol + trigger_type + entry_date.
3. Add C03-specific defense export framework / signed tranche / delivery / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C03_STAGE2_ALLOWED_ON_FRAMEWORK_WITH_SIGNED_TRANCHE_DELIVERY_MARGIN_BRIDGE
- C03_GREEN_REQUIRES_SIGNED_SCOPE_CUSTOMER_ACCEPTANCE_DELIVERY_WORKING_CAPITAL_REVISION
- C03_DEFENSE_FRAMEWORK_PRICE_PREMIUM_LOCAL_4B
- C03_SMALLCAP_DEFENSE_THEME_WITHOUT_PROGRAM_BACKLOG_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

