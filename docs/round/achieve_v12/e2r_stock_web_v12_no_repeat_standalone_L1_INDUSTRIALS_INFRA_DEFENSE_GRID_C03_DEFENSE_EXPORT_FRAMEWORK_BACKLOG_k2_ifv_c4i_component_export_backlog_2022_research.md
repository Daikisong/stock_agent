# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework backlog / K2-C4I-component conversion guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: K2_IFV_C4I_COMPONENT_EXPORT_BACKLOG_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|export_framework_to_company_backlog_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_k2_ifv_c4i_component_export_backlog_2022_research.md
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

This run avoids those top-covered C03 symbols and adds 064350, 272210, and 064960.  
Each row uses a new `C03 + symbol + trigger_type + entry_date` hard key.

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
064350 현대로템: selected 2022/2023 forward window clean; corporate-action candidate is 2020-08-14, outside selected test window.
272210 한화시스템: selected 2022/2023 forward window clean; corporate-action candidate is 2021-06-23, outside selected test window.
064960 SNT모티브: selected 2022/2023 forward window clean; corporate-action candidates are 2002-12-24, 2012-12-26 and later 2025-01-24/2025-02-26, outside selected test window.
```

## 3. Research thesis

C03 should distinguish a defense export framework that becomes company-level backlog from platform-sympathy that only borrows the headline:

```text
defense export framework / geopolitical demand
→ direct signed order or backlog quality
→ export financing, customer allocation and delivery schedule
→ production capacity, working capital and parts localization
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

An export framework is a gate opening. Stage2 can buy the company that actually drives the tank through the gate; Green should require the gate to become signed backlog, delivery schedule and margin revision.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_064350_HYUNDAIROTEM_20220729_K2_EXPORT_BACKLOG_STAGE2 | 064350 | positive_k2_tank_export_framework_backlog_stage2_success | 2022-07-29 | 26550 | 32850 on 2022-08-26 | 23050 on 2022-10-27 | 23.73% | 23.73% | 23.73% | -13.18% | -29.83% |
| C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_EXPORT_FALSE_GREEN | 272210 | defense_electronics_export_framework_false_green_counterexample | 2022-07-29 | 14550 | 16200 on 2022-09-01 | 10150 on 2022-10-13 | 10.31% | 11.34% | 11.34% | -30.24% | -37.35% |
| C03_064960_SNTMOTIVE_20220825_DEFENSE_COMPONENT_EXPORT_PREMIUM_4B | 064960 | defense_component_export_price_premium_counterexample | 2022-08-25 | 46300 | 52300 on 2023-04-12 | 40000 on 2022-10-13 | 8.42% | 8.42% | 12.96% | -13.61% | -17.5% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 064350 is the positive anchor. The K2/export-framework route had a direct platform-to-backlog bridge and produced meaningful MFE before later 4B discipline was needed.
- Stage2 is allowed only when export-framework salience maps to a named platform, signed order/backlog, delivery schedule, export financing and margin/revision visibility.

### Stage3 / Green
- C03 Green should require direct signed backlog, customer allocation, financing/project finality, delivery schedule, production capacity and margin/revision confirmation.
- 272210 is the false-Green guard: defense-electronics/system theme confirmation did not provide enough company-specific signed order and margin bridge relative to the price-implied expectation.

### 4B
- 064960 fills the component-sympathy 4B pocket. The component story may be real, but platform-level export heat is not enough without incremental direct order and margin proof.
- 064350 also demonstrates that a valid Stage2 can become 4B refresh once the export framework is capitalized.
- The key rule is that platform-sympathy and component-sympathy should not be substituted for listed-company order-to-margin conversion.

### 4C
- No hard export cancellation, failed financing or contract loss is asserted.
- The C03 break mode is conversion gap: a real defense export framework can exist while a non-prime or adjacent supplier lacks direct signed backlog, delivery schedule and margin revision.

## 6. Raw component score breakdown

```json
{
  "C03_064350_HYUNDAIROTEM_20220729_K2_EXPORT_BACKLOG_STAGE2": {
    "capacity_and_working_capital_bridge": 7,
    "export_framework_visibility": 11,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 9,
    "platform_delivery_schedule": 9,
    "signed_order_or_backlog_quality": 10,
    "total": 64,
    "valuation_rerating_runway": 7
  },
  "C03_064960_SNTMOTIVE_20220825_DEFENSE_COMPONENT_EXPORT_PREMIUM_4B": {
    "capacity_and_working_capital_bridge": 3,
    "export_framework_visibility": 6,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "platform_delivery_schedule": 3,
    "signed_order_or_backlog_quality": 3,
    "total": 24,
    "valuation_rerating_runway": 1
  },
  "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_EXPORT_FALSE_GREEN": {
    "capacity_and_working_capital_bridge": 3,
    "export_framework_visibility": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "platform_delivery_schedule": 3,
    "signed_order_or_backlog_quality": 3,
    "total": 26,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C03 guard:
```text
if defense_export_framework and direct_signed_backlog_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if platform_sympathy_or_component_sympathy and no direct_signed_order_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_stage3_yellow_or_local_4B = true

if post_peak_drawdown and framework_to_company_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 272210 / 2022-07-29: defense-electronics export sympathy can be over-promoted if price confirmation substitutes for direct signed backlog and margin proof.
- 064960 / 2022-08-25: defense component export sympathy can become price-only when incremental order, capacity and margin evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.18, "MAE_30D_pct": -9.42, "MAE_90D_pct": -13.18, "MFE_180D_pct": 23.73, "MFE_30D_pct": 23.73, "MFE_90D_pct": 23.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20220729_K2_EXPORT_BACKLOG_STAGE2", "case_role": "positive_k2_tank_export_framework_backlog_stage2_success", "company_name": "현대로템", "corporate_action_window_status": "clean_2022_2023_forward_window; corporate-action candidate is 2020-08-14 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when a defense export framework was attached to a named platform and visible delivery/backlog path. Green still requires signed order conversion, export-financing/project finality, production schedule, domestic capacity allocation, working-capital burden and margin/revision confirmation; after the August 2022 premium, fresh order-to-margin evidence was required before treating the rerating as still actionable.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.83, "entry_date": "2022-07-29", "entry_price": 26550, "evidence_family": "k2_export_framework_signed_order_backlog_delivery_schedule_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "K2_IFV_C4I_COMPONENT_EXPORT_BACKLOG_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-27", "low_price_180d": 23050, "peak_date": "2022-08-26", "peak_price": 32850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"capacity_and_working_capital_bridge": 7, "export_framework_visibility": 11, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 9, "platform_delivery_schedule": 9, "signed_order_or_backlog_quality": 10, "total": 64, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20220729_K2_EXPORT_BACKLOG_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "signed_order_or_backlog_quality", "delivery_schedule_and_margin_revision_route"], "stage3_evidence_fields": ["direct_signed_backlog_required", "customer_allocation_export_financing_delivery_schedule_required", "capacity_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "platform_or_component_sympathy_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["export_framework_to_signed_order_gap", "delivery_schedule_or_financing_delay", "margin_revision_bridge_failure"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -30.24, "MAE_30D_pct": -2.75, "MAE_90D_pct": -30.24, "MFE_180D_pct": 11.34, "MFE_30D_pct": 10.31, "MFE_90D_pct": 11.34, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_EXPORT_FALSE_GREEN", "case_role": "defense_electronics_export_framework_false_green_counterexample", "company_name": "한화시스템", "corporate_action_window_status": "clean_2022_2023_forward_window; corporate-action candidate is 2021-06-23 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Defense electronics/system-integration price confirmation should remain Yellow unless the export framework is mapped to direct signed backlog, customer allocation, delivery milestones, project financing and margin/revision evidence. Theme sympathy around a platform export is not the same as company-level order conversion.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.35, "entry_date": "2022-07-29", "entry_price": 14550, "evidence_family": "defense_electronics_export_framework_theme_price_confirmation_without_direct_signed_backlog_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "K2_IFV_C4I_COMPONENT_EXPORT_BACKLOG_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-13", "low_price_180d": 10150, "peak_date": "2022-09-01", "peak_price": 16200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/272/272210.json", "raw_component_score_breakdown": {"capacity_and_working_capital_bridge": 3, "export_framework_visibility": 7, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "platform_delivery_schedule": 3, "signed_order_or_backlog_quality": 3, "total": 26, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_EXPORT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "signed_order_or_backlog_quality", "delivery_schedule_and_margin_revision_route"], "stage3_evidence_fields": ["direct_signed_backlog_required", "customer_allocation_export_financing_delivery_schedule_required", "capacity_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "platform_or_component_sympathy_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["export_framework_to_signed_order_gap", "delivery_schedule_or_financing_delay", "margin_revision_bridge_failure"], "symbol": "272210", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -13.61, "MAE_30D_pct": -11.23, "MAE_90D_pct": -13.61, "MFE_180D_pct": 12.96, "MFE_30D_pct": 8.42, "MFE_90D_pct": 8.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064960_SNTMOTIVE_20220825_DEFENSE_COMPONENT_EXPORT_PREMIUM_4B", "case_role": "defense_component_export_price_premium_counterexample", "company_name": "SNT모티브", "corporate_action_window_status": "clean_2022_2023_forward_window; corporate-action candidates are 2002-12-24, 2012-12-26 and later 2025-01-24/2025-02-26, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Defense component export sympathy should route to local 4B or counterexample when the stock has already capitalized framework optimism and incremental signed order, customer allocation, delivery schedule, capacity utilization and margin/revision evidence do not refresh. Component exposure needs direct order-to-margin conversion, not platform-level theme heat.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -17.5, "entry_date": "2022-08-25", "entry_price": 46300, "evidence_family": "defense_component_export_sympathy_price_premium_without_incremental_order_capacity_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "K2_IFV_C4I_COMPONENT_EXPORT_BACKLOG_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-13", "low_price_180d": 40000, "peak_date": "2023-04-12", "peak_price": 52300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064960.json", "raw_component_score_breakdown": {"capacity_and_working_capital_bridge": 3, "export_framework_visibility": 6, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "platform_delivery_schedule": 3, "signed_order_or_backlog_quality": 3, "total": 24, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C03_064960_SNTMOTIVE_20220825_DEFENSE_COMPONENT_EXPORT_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "signed_order_or_backlog_quality", "delivery_schedule_and_margin_revision_route"], "stage3_evidence_fields": ["direct_signed_backlog_required", "customer_allocation_export_financing_delivery_schedule_required", "capacity_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "platform_or_component_sympathy_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["export_framework_to_signed_order_gap", "delivery_schedule_or_financing_delay", "margin_revision_bridge_failure"], "symbol": "064960", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064960/2022.csv", "trigger_date": "2022-08-25", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "K2_IFV_C4I_COMPONENT_EXPORT_BACKLOG_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_backlog_k2_c4i_component_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense export rows should allow Stage2 when export framework evidence maps to direct signed order/backlog, delivery schedule, export financing, capacity and margin-revision bridge; platform-sympathy or component-sympathy price premiums should remain Yellow/local 4B unless the listed company has direct order-to-margin conversion.",
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
3. Add C03-specific defense export framework / signed backlog / delivery schedule / export financing / capacity / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C03_STAGE2_ALLOWED_ON_DIRECT_SIGNED_BACKLOG_DELIVERY_MARGIN_BRIDGE
- C03_GREEN_REQUIRES_EXPORT_FINANCING_CUSTOMER_ALLOCATION_CAPACITY_REVISION
- C03_PLATFORM_COMPONENT_SYMPATHY_PRICE_PREMIUM_LOCAL_4B
- C03_EXPORT_FRAMEWORK_WITHOUT_COMPANY_ORDER_TO_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

