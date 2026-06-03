# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework backlog guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_BACKLOG_SMALLCAP_PRICE_PREMIUM_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_defense_export_backlog_smallcap_guard_2022_2025_research.md
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

This run avoids those top-covered C03 symbols and adds 064350, 272210, and 010820.  
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
064350 현대로템: 2022 forward window clean; corporate-action candidate is 2020-08-14, outside the selected test window.
272210 한화시스템: 2024/2025 forward window clean; corporate-action candidate is 2021-06-23, outside the selected test window.
010820 퍼스텍: 2024 forward window uses tradable rows; long historical corporate-action caveat is treated as outside the selected 2024 test window.
```

## 3. Research thesis

C03 should not treat every defense headline as a backlog rerating. It should test whether a defense event crosses from attention into signed export economics:

```text
defense export / framework attention
→ contract conversion
→ delivery schedule and customer-country visibility
→ working-capital, margin and revenue conversion
→ revision bridge
→ rerating
```

The mechanism is the difference between a parade and a purchase order. A parade can move price for a week. C03 Green should pay for the factory schedule, the contract scope, and the invoice path.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_EXPORT_FRAMEWORK_STAGE2 | 064350 | positive_export_framework_stage2_success_with_later_4b | 2022-07-29 | 26550 | 32850 on 2022-08-26 | 23050 on 2022-10-27 | 23.73% | 23.73% | 23.73% | -13.18% | -29.83% |
| C03_272210_HANWHASYSTEMS_20241107_DEFENSE_ELECTRONICS_BACKLOG_STAGE2 | 272210 | positive_defense_electronics_backlog_stage2_success | 2024-11-07 | 21200 | 62000 on 2025-07-31 | 19570 on 2024-12-10 | 42.45% | 104.72% | 192.45% | -7.69% | -23.31% |
| C03_010820_FIRSTEC_20240117_GEOPOLITICAL_DEFENSE_THEME_PRICE_PREMIUM_4B | 010820 | geopolitical_defense_theme_without_backlog_counterexample | 2024-01-17 | 3765 | 3990 on 2024-01-17 | 2555 on 2024-09-09 | 5.98% | 5.98% | 5.98% | -32.14% | -35.96% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Defense export framework, signed backlog and customer-country visibility are valid Stage2 routes.
- 064350 is the clean export-framework anchor: Poland/K2-related attention produced a Stage2 MFE before the later drawdown required risk discipline.
- 272210 adds a different positive path: defense electronics/system backlog and export optionality can produce a slower but larger rerating when the order pipeline keeps broadening.

### Stage3 / Green
- C03 Green should require more than a defense headline. It needs contract conversion, delivery schedule, revenue recognition, margin, working capital and revision evidence.
- 064350 and 272210 show why Stage2 can be early and useful. They also show why the model must keep asking whether the framework becomes delivered backlog.

### 4B
- 010820 is the small-cap price-premium guard. The defense/geopolitical theme spike appeared without sufficient export-framework or backlog conversion.
- 4B should activate when the market prices defense beta before signed backlog and delivery evidence arrive.

### 4C
- No hard contract cancellation or accounting break is asserted.
- The C03 break mode here is conversion failure: the theme remains real, but framework-to-contract, delivery, margin and revision do not carry the price already paid.

## 6. Raw component score breakdown

```json
{
  "C03_010820_FIRSTEC_20240117_GEOPOLITICAL_DEFENSE_THEME_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 4,
    "capital_allocation": 1,
    "eps_fcf_explosion": 3,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 19,
    "valuation_rerating_runway": 1,
    "visibility_quality": 3
  },
  "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_EXPORT_FRAMEWORK_STAGE2": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 2,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 59,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  },
  "C03_272210_HANWHASYSTEMS_20241107_DEFENSE_ELECTRONICS_BACKLOG_STAGE2": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 56,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C03 guard:
```text
if defense_export_framework and contract_scope_delivery_visibility:
    allow_stage2_actionable = true

if defense_price_premium and no contract_conversion_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if geopolitical_theme_attention and no signed_backlog_or_customer_country_visibility:
    cap_stage = Stage3-Yellow
    route_to_counterexample_or_4B = true
```

Residual error:
```text
current_profile_error_count = 1
- 010820 / 2024-01-17: small-cap defense/geopolitical price premium can be over-promoted if the model treats theme heat as export backlog.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.18, "MAE_30D_pct": -9.42, "MAE_90D_pct": -13.18, "MFE_180D_pct": 23.73, "MFE_30D_pct": 23.73, "MFE_90D_pct": 23.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_EXPORT_FRAMEWORK_STAGE2", "case_role": "positive_export_framework_stage2_success_with_later_4b", "company_name": "현대로템", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when a real export-framework route and delivery/backlog visibility separated the company from generic defense beta, but Green still requires contract conversion, margin, working-capital and delivery-revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.83, "entry_date": "2022-07-29", "entry_price": 26550, "evidence_family": "poland_k2_tank_export_framework_backlog_delivery_route", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_EXPORT_BACKLOG_SMALLCAP_PRICE_PREMIUM_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-27", "low_price_180d": 23050, "peak_date": "2022-08-26", "peak_price": 32850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 2, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 11, "total": 59, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_EXPORT_FRAMEWORK_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "signed_backlog_or_order_scope_claim", "delivery_schedule_or_customer_country_visibility"], "stage3_evidence_fields": ["contract_conversion_required", "delivery_schedule_and_revenue_conversion_required", "margin_working_capital_revision_bridge_required"], "stage4b_evidence_fields": ["defense_theme_or_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_to_contract_conversion_gap", "delivery_or_margin_bridge_failure", "geopolitical_theme_without_backlog"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -7.69, "MAE_30D_pct": -7.69, "MAE_90D_pct": -7.69, "MFE_180D_pct": 192.45, "MFE_30D_pct": 42.45, "MFE_90D_pct": 104.72, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_272210_HANWHASYSTEMS_20241107_DEFENSE_ELECTRONICS_BACKLOG_STAGE2", "case_role": "positive_defense_electronics_backlog_stage2_success", "company_name": "한화시스템", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when defense electronics/system backlog and export optionality began converting into a broader order pipeline; Green still requires order scope, delivery cadence, margin and revision proof.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -23.31, "entry_date": "2024-11-07", "entry_price": 21200, "evidence_family": "defense_electronics_system_export_backlog_satellite_radar_delivery_route", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_EXPORT_BACKLOG_SMALLCAP_PRICE_PREMIUM_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-10", "low_price_180d": 19570, "peak_date": "2025-07-31", "peak_price": 62000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/272/272210.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 56, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C03_272210_HANWHASYSTEMS_20241107_DEFENSE_ELECTRONICS_BACKLOG_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "signed_backlog_or_order_scope_claim", "delivery_schedule_or_customer_country_visibility"], "stage3_evidence_fields": ["contract_conversion_required", "delivery_schedule_and_revenue_conversion_required", "margin_working_capital_revision_bridge_required"], "stage4b_evidence_fields": ["defense_theme_or_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_to_contract_conversion_gap", "delivery_or_margin_bridge_failure", "geopolitical_theme_without_backlog"], "symbol": "272210", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv", "trigger_date": "2024-11-07", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -32.14, "MAE_30D_pct": -15.94, "MAE_90D_pct": -15.94, "MFE_180D_pct": 5.98, "MFE_30D_pct": 5.98, "MFE_90D_pct": 5.98, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_010820_FIRSTEC_20240117_GEOPOLITICAL_DEFENSE_THEME_PRICE_PREMIUM_4B", "case_role": "geopolitical_defense_theme_without_backlog_counterexample", "company_name": "퍼스텍", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window where present", "current_profile_error": true, "current_profile_verdict": "Small-cap defense theme price premium should route to local 4B or counterexample unless explicit export framework, signed backlog, delivery schedule, margin and revision bridge are visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -35.96, "entry_date": "2024-01-17", "entry_price": 3765, "evidence_family": "defense_geopolitical_tension_price_premium_without_export_framework_backlog_conversion", "evidence_url_pending": false, "fine_archetype_id": "DEFENSE_EXPORT_BACKLOG_SMALLCAP_PRICE_PREMIUM_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-09-09", "low_price_180d": 2555, "peak_date": "2024-01-17", "peak_price": 3990, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010820.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 4, "capital_allocation": 1, "eps_fcf_explosion": 3, "information_confidence": 3, "market_mispricing": 4, "total": 19, "valuation_rerating_runway": 1, "visibility_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C03_010820_FIRSTEC_20240117_GEOPOLITICAL_DEFENSE_THEME_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_attention", "signed_backlog_or_order_scope_claim", "delivery_schedule_or_customer_country_visibility"], "stage3_evidence_fields": ["contract_conversion_required", "delivery_schedule_and_revenue_conversion_required", "margin_working_capital_revision_bridge_required"], "stage4b_evidence_fields": ["defense_theme_or_export_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["framework_to_contract_conversion_gap", "delivery_or_margin_bridge_failure", "geopolitical_theme_without_backlog"], "symbol": "010820", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv", "trigger_date": "2024-01-17", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "DEFENSE_EXPORT_BACKLOG_SMALLCAP_PRICE_PREMIUM_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_backlog_new_symbols_and_smallcap_4b_counterexample",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense-export/framework rows should allow Stage2 on real export framework, signed backlog or defense-electronics order scope, but Stage3 Green requires contract conversion, delivery schedule, margin, working-capital and revision bridge; geopolitical/smallcap defense price premium without backlog should route to local 4B or counterexample.",
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
3. Add C03-specific defense export/framework/backlog conversion guard only as a shadow candidate until more rows exist.

Candidate rule:
- C03_STAGE2_ALLOWED_ON_EXPORT_FRAMEWORK_OR_SIGNED_BACKLOG
- C03_GREEN_REQUIRES_CONTRACT_SCOPE_DELIVERY_MARGIN_REVISION
- C03_DEFENSE_THEME_WITHOUT_BACKLOG_LOCAL_4B
- C03_GEOPOLITICAL_SMALLCAP_PREMIUM_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

