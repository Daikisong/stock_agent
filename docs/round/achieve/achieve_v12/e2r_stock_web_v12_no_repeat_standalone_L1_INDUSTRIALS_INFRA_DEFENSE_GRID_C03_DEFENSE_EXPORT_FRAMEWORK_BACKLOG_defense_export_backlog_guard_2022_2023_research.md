# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework backlog guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_REVISION_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_defense_export_backlog_guard_2022_2023_research.md
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

This run avoids those top-covered C03 symbols and adds 064350, 272210, and 103140.  
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
064350 현대로템: 2022/2023 forward window clean; corporate-action candidate is 2020-08-14.
272210 한화시스템: 2022/2023 forward window clean; corporate-action candidate is 2021-06-23.
103140 풍산: corporate_action_candidate_count=0.
```

## 3. Research thesis

C03 is not a generic defense-theme bucket. It should test whether a government framework or geopolitical demand shock becomes company-level backlog:

```text
defense export framework / country program / ammunition demand
→ company-specific award or backlog
→ delivery schedule
→ margin and revision bridge
→ rerating
```

The danger is "framework heat." A framework agreement can shine like a runway light, but if the company-level contract, delivery timing, and margin are not visible, the aircraft has not actually taken off.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_064350_HYUNDAIROTEM_20220729_K2_POLAND_EXPORT_BACKLOG_STAGE2 | 064350 | positive_export_backlog_stage2_success_with_drawdown | 2022-07-29 | 26550 | 32850 on 2022-08-26 | 23050 on 2022-10-27 | 23.73% | 23.73% | 23.73% | -13.18% | -29.83% |
| C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_FRAMEWORK_FALSE_GREEN | 272210 | framework_exposure_false_green_counterexample | 2022-07-29 | 14550 | 16200 on 2022-09-01 | 10200 on 2023-01-03 | 11.34% | 11.34% | 11.34% | -29.9% | -37.04% |
| C03_103140_POONGSAN_20230221_MUNITIONS_EXPORT_BACKLOG_STAGE2 | 103140 | positive_munitions_export_stage2_success | 2023-02-21 | 36400 | 45250 on 2023-06-26 | 33300 on 2023-08-17 | 7.83% | 24.31% | 24.31% | -8.52% | -26.41% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Defense export framework attention and geopolitical demand are valid routing signals.
- 064350 shows a strong Stage2 path: the price moved quickly after the framework/backlog narrative became visible.
- 103140 adds a munitions-demand route, where Stage2 can work if demand and pricing power connect to margin revision.

### Stage3 / Green
- C03 Green should require firm contract or backlog conversion, delivery schedule, margin bridge, and revision confirmation.
- 272210 is the guardrail counterexample: defense electronics exposure and framework adjacency are not enough if the company-specific order/revision bridge is unclear.

### 4B
- 064350 demonstrates that even a valid defense-export thesis can require 4B discipline after a sharp rerating and subsequent drawdown.
- A local 4B watch is allowed on price premium, but full-window 4B should require non-price evidence such as delivery saturation or revision deceleration.

### 4C
- No hard accounting break is asserted.
- The C03 break mode is usually a conversion gap: the national framework remains real, but the company-level backlog/margin path does not close fast enough.

## 6. Raw component score breakdown

```json
{
  "C03_064350_HYUNDAIROTEM_20220729_K2_POLAND_EXPORT_BACKLOG_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 58,
    "valuation_rerating_runway": 10,
    "visibility_quality": 12
  },
  "C03_103140_POONGSAN_20230221_MUNITIONS_EXPORT_BACKLOG_STAGE2": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 55,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  },
  "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_FRAMEWORK_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 32,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C03 guard:
```text
if defense_export_framework and no firm_contract_backlog_delivery_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if direct_platform_or_munitions_backlog and delivery_margin_revision_bridge_visible:
    allow_stage3_green_candidate = true

if indirect_defense_electronics_theme_without_company_level_award:
    route_to_counterexample_or_yellow = true
```

Residual error:
```text
current_profile_error_count = 1
- 272210 / 2022-07-29: framework-adjacent defense electronics can be over-promoted if the model does not require company-level backlog and margin conversion.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.18, "MAE_30D_pct": -9.42, "MAE_90D_pct": -13.18, "MFE_180D_pct": 23.73, "MFE_30D_pct": 23.73, "MFE_90D_pct": 23.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20220729_K2_POLAND_EXPORT_BACKLOG_STAGE2", "case_role": "positive_export_backlog_stage2_success_with_drawdown", "company_name": "현대로템", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when the export framework and backlog route were visible, but Green should require executable contract/backlog conversion, delivery schedule, margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.83, "entry_date": "2022-07-29", "entry_price": 26550, "evidence_family": "defense_export_framework_k2_tank_backlog_to_stage2_rerating", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-27", "low_price_180d": 23050, "peak_date": "2022-08-26", "peak_price": 32850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 58, "valuation_rerating_runway": 10, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20220729_K2_POLAND_EXPORT_BACKLOG_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "customer_country_or_program_visibility", "relative_strength_or_backlog_claim"], "stage3_evidence_fields": ["firm_contract_or_backlog_conversion_required", "delivery_schedule_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_without_company_level_award", "delivery_or_margin_delay", "revision_gap"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -29.9, "MAE_30D_pct": -5.15, "MAE_90D_pct": -26.8, "MFE_180D_pct": 11.34, "MFE_30D_pct": 11.34, "MFE_90D_pct": 11.34, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_FRAMEWORK_FALSE_GREEN", "case_role": "framework_exposure_false_green_counterexample", "company_name": "한화시스템", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Defense framework exposure should stay Yellow when the company-level backlog and margin bridge are indirect or delayed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.04, "entry_date": "2022-07-29", "entry_price": 14550, "evidence_family": "defense_electronics_framework_theme_without_backlog_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2023-01-03", "low_price_180d": 10200, "peak_date": "2022-09-01", "peak_price": 16200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/272/272210.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 6, "total": 32, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_ELECTRONICS_FRAMEWORK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "customer_country_or_program_visibility", "relative_strength_or_backlog_claim"], "stage3_evidence_fields": ["firm_contract_or_backlog_conversion_required", "delivery_schedule_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_without_company_level_award", "delivery_or_margin_delay", "revision_gap"], "symbol": "272210", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -8.52, "MAE_30D_pct": -2.61, "MAE_90D_pct": -2.61, "MFE_180D_pct": 24.31, "MFE_30D_pct": 7.83, "MFE_90D_pct": 24.31, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_103140_POONGSAN_20230221_MUNITIONS_EXPORT_BACKLOG_STAGE2", "case_role": "positive_munitions_export_stage2_success", "company_name": "풍산", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 can work when munition demand/backlog and pricing power are tied to margin revision, but Green must still require non-price export order and margin bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -26.41, "entry_date": "2023-02-21", "entry_price": 36400, "evidence_family": "munitions_export_demand_backlog_margin_stage2_rerating", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2023-08-17", "low_price_180d": 33300, "peak_date": "2023-06-26", "peak_price": 45250, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/103/103140.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 55, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C03_103140_POONGSAN_20230221_MUNITIONS_EXPORT_BACKLOG_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "customer_country_or_program_visibility", "relative_strength_or_backlog_claim"], "stage3_evidence_fields": ["firm_contract_or_backlog_conversion_required", "delivery_schedule_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_framework_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_without_company_level_award", "delivery_or_margin_delay", "revision_gap"], "symbol": "103140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2023.csv", "trigger_date": "2023-02-21", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_new_symbols_and_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense-export framework rows should permit Stage2 on framework/backlog attention, but Stage3 Green requires firm contract/backlog conversion, delivery schedule, margin and revision bridge; indirect electronics exposure should remain Yellow/counterexample until company-level award evidence closes.",
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
3. Add C03-specific framework-to-backlog/delivery/margin bridge logic only as a shadow candidate until more rows exist.

Candidate rule:
- C03_GREEN_REQUIRES_FIRM_CONTRACT_BACKLOG_DELIVERY_MARGIN_REVISION
- C03_FRAMEWORK_ATTENTION_STAGE2_CAP
- C03_INDIRECT_DEFENSE_ELECTRONICS_FALSE_GREEN_COUNTEREXAMPLE
- C03_VALID_EXPORT_PLATFORM_RERATING_LOCAL_4B_WATCH

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

