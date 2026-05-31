# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework backlog / SNT-Hanwha components 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: SNT_HANWHA_DEFENSE_COMPONENTS_EXPORT_FRAMEWORK_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|defense_export_framework_to_component_backlog_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_snt_hanwha_defense_components_4b_2022_research.md
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

This run avoids those top-covered C03 symbols and adds 003570, 272210, and 000880.  
Each row uses a new `C03 + symbol + trigger_type + entry_date` hard key:
```text
C03 + 003570 + Stage2-Actionable + 2022-07-27
C03 + 272210 + Stage3-Yellow + 2022-07-29
C03 + 000880 + 4B-local-price-only + 2022-07-29
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
003570 SNT다이내믹스: selected 2022 forward window clean; historical corporate-action candidates outside selected trigger window.
272210 한화시스템: selected post-2021-06-23 forward window clean; corporate-action candidate is before selected trigger window.
000880 한화: selected post-1999 forward window clean; historical corporate-action candidates outside selected trigger window.
```

## 3. Research thesis

C03 should distinguish defense export framework evidence that converts into platform/component backlog from defense group or systems beta already paid in price:

```text
defense export framework / geopolitical demand
→ platform or customer specificity
→ signed backlog quality and delivery schedule
→ capacity allocation and working-capital load
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A defense framework is a gate opening. Stage2 can buy when a platform or component walks through the gate with backlog and delivery cadence. Green should require the walk, the schedule and the margin bridge, not just the sound of the gate.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_003570_SNTDYNAMICS_20220727_DEFENSE_DRIVETRAIN_COMPONENT_STAGE2 | 003570 | positive_defense_drivetrain_component_export_framework_stage2_success_with_later_4b_refresh | 2022-07-27 | 8080 | 12800 on 2022-08-26 | 7970 on 2022-07-27 | 58.42% | 58.42% | 58.42% | -1.36% | -36.64% |
| C03_272210_HANWHASYSTEMS_20220729_DEFENSE_SYSTEMS_FRAMEWORK_FALSE_GREEN | 272210 | defense_systems_export_framework_false_green_counterexample | 2022-07-29 | 14550 | 16200 on 2022-09-01 | 10150 on 2022-10-13 | 9.97% | 11.34% | 11.34% | -30.24% | -37.35% |
| C03_000880_HANWHA_20220729_DEFENSE_GROUP_THEME_4B | 000880 | defense_group_theme_price_premium_counterexample | 2022-07-29 | 27550 | 32950 on 2022-08-30 | 23250 on 2022-10-13 | 19.6% | 19.6% | 19.6% | -15.61% | -29.44% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 003570 is the positive anchor. The July 2022 defense export-framework route produced strong 30D/90D MFE before the August premium required 4B refresh discipline.
- Stage2 is allowed only when export framework salience maps to platform/customer specificity, backlog conversion, delivery schedule and margin/revision visibility.

### Stage3 / Green
- C03 Green should require signed backlog quality, delivery schedule, platform/customer scope, capacity allocation, working-capital discipline and margin/revision confirmation.
- 272210 is the false-Green/Yellow guard: defense systems price confirmation was visible, but incremental direct contract, delivery and margin evidence did not refresh enough to survive the forward path.

### 4B
- 000880 fills the defense group/theme price-premium 4B pocket. The move had defense beta, but group-level price heat was weaker than direct backlog-to-margin evidence.
- 272210 shows the systems version of the same failure: export-framework salience can be real while the listed-company trigger lacks enough signed backlog and margin proof.
- 003570 also demonstrates that valid Stage2 can become local 4B after the rerating capitalizes the component/backlog option.

### 4C
- No hard export cancellation, delivery failure, customer loss or accounting break is asserted.
- The C03 break mode here is backlog-to-margin exhaustion: export salience may remain directionally real, but incremental signed backlog, delivery cadence and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C03_000880_HANWHA_20220729_DEFENSE_GROUP_THEME_4B": {
    "delivery_schedule_visibility": 2,
    "export_framework_visibility": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "platform_specificity": 4,
    "signed_backlog_quality": 2,
    "total": 28,
    "valuation_rerating_runway": 1,
    "working_capital_risk_control": 3
  },
  "C03_003570_SNTDYNAMICS_20220727_DEFENSE_DRIVETRAIN_COMPONENT_STAGE2": {
    "delivery_schedule_visibility": 7,
    "export_framework_visibility": 10,
    "information_confidence": 4,
    "margin_revision_bridge": 6,
    "market_mispricing": 9,
    "platform_specificity": 8,
    "signed_backlog_quality": 7,
    "total": 64,
    "valuation_rerating_runway": 8,
    "working_capital_risk_control": 5
  },
  "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_SYSTEMS_FRAMEWORK_FALSE_GREEN": {
    "delivery_schedule_visibility": 3,
    "export_framework_visibility": 8,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "platform_specificity": 5,
    "signed_backlog_quality": 3,
    "total": 32,
    "valuation_rerating_runway": 1,
    "working_capital_risk_control": 3
  }
}
```

## 7. Current calibrated profile stress test

Suggested C03 guard:
```text
if defense_export_framework and platform_customer_backlog_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if defense_group_or_systems_price_premium and no incremental_backlog_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and backlog_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 272210 / 2022-07-29: defense systems/framework confirmation can be over-promoted if price strength substitutes for signed backlog and margin proof.
- 000880 / 2022-07-29: defense group premium can look actionable, but fails without direct export framework, backlog conversion and margin revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -1.36, "MAE_30D_pct": -1.36, "MAE_90D_pct": -1.36, "MFE_180D_pct": 58.42, "MFE_30D_pct": 58.42, "MFE_90D_pct": 58.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_003570_SNTDYNAMICS_20220727_DEFENSE_DRIVETRAIN_COMPONENT_STAGE2", "case_role": "positive_defense_drivetrain_component_export_framework_stage2_success_with_later_4b_refresh", "company_name": "SNT다이내믹스", "corporate_action_window_status": "selected post-2015 forward window clean; historical corporate-action candidates are outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when the defense export-framework shock mapped to a specific armored-vehicle component supplier and the market had not yet fully capitalized backlog/delivery optionality. Green still requires signed backlog, delivery cadence, platform/customer specificity, capacity and margin/revision confirmation; after the August 2022 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -36.64, "entry_date": "2022-07-27", "entry_price": 8080, "evidence_family": "defense_export_framework_armored_vehicle_component_backlog_delivery_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "SNT_HANWHA_DEFENSE_COMPONENTS_EXPORT_FRAMEWORK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-07-27", "low_price_180d": 7970, "peak_date": "2022-08-26", "peak_price": 12800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003570.json", "raw_component_score_breakdown": {"delivery_schedule_visibility": 7, "export_framework_visibility": 10, "information_confidence": 4, "margin_revision_bridge": 6, "market_mispricing": 9, "platform_specificity": 8, "signed_backlog_quality": 7, "total": 64, "valuation_rerating_runway": 8, "working_capital_risk_control": 5}, "reuse_reason": null, "same_entry_group_id": "C03_003570_SNTDYNAMICS_20220727_DEFENSE_DRIVETRAIN_COMPONENT_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "platform_or_customer_specificity", "backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_backlog_quality_required", "delivery_schedule_and_platform_scope_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_group_or_systems_price_premium", "backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_loss_or_delivery_delay", "framework_not_converted_to_company_backlog", "margin_revision_bridge_failure"], "symbol": "003570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003570/2022.csv", "trigger_date": "2022-07-27", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -30.24, "MAE_30D_pct": -5.15, "MAE_90D_pct": -30.24, "MFE_180D_pct": 11.34, "MFE_30D_pct": 9.97, "MFE_90D_pct": 11.34, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_SYSTEMS_FRAMEWORK_FALSE_GREEN", "case_role": "defense_systems_export_framework_false_green_counterexample", "company_name": "한화시스템", "corporate_action_window_status": "selected post-2021-06-23 forward window clean; corporate-action candidate is before selected trigger window", "current_profile_error": true, "current_profile_verdict": "Defense systems/export-framework price confirmation should remain Yellow or local 4B when framework salience is not followed by incremental direct contract scope, signed backlog, delivery schedule and margin/revision evidence. The July 2022 trigger had limited residual upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.35, "entry_date": "2022-07-29", "entry_price": 14550, "evidence_family": "defense_systems_export_framework_price_confirmation_without_incremental_signed_backlog_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SNT_HANWHA_DEFENSE_COMPONENTS_EXPORT_FRAMEWORK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-13", "low_price_180d": 10150, "peak_date": "2022-09-01", "peak_price": 16200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/272/272210.json", "raw_component_score_breakdown": {"delivery_schedule_visibility": 3, "export_framework_visibility": 8, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "platform_specificity": 5, "signed_backlog_quality": 3, "total": 32, "valuation_rerating_runway": 1, "working_capital_risk_control": 3}, "reuse_reason": null, "same_entry_group_id": "C03_272210_HANWHASYSTEMS_20220729_DEFENSE_SYSTEMS_FRAMEWORK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "platform_or_customer_specificity", "backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_backlog_quality_required", "delivery_schedule_and_platform_scope_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_group_or_systems_price_premium", "backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_loss_or_delivery_delay", "framework_not_converted_to_company_backlog", "margin_revision_bridge_failure"], "symbol": "272210", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -15.61, "MAE_30D_pct": -7.99, "MAE_90D_pct": -15.61, "MFE_180D_pct": 19.6, "MFE_30D_pct": 19.6, "MFE_90D_pct": 19.6, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_000880_HANWHA_20220729_DEFENSE_GROUP_THEME_4B", "case_role": "defense_group_theme_price_premium_counterexample", "company_name": "한화", "corporate_action_window_status": "selected post-1999 forward window clean; historical corporate-action candidates are outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Defense group/theme price premium should route to local 4B/counterexample unless the move is backed by direct export framework conversion, signed backlog, delivery schedule, capacity allocation and margin/revision evidence. Group-level defense beta is weaker than platform-specific backlog conversion.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.44, "entry_date": "2022-07-29", "entry_price": 27550, "evidence_family": "defense_group_export_theme_price_premium_without_direct_backlog_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SNT_HANWHA_DEFENSE_COMPONENTS_EXPORT_FRAMEWORK_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-13", "low_price_180d": 23250, "peak_date": "2022-08-30", "peak_price": 32950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000880.json", "raw_component_score_breakdown": {"delivery_schedule_visibility": 2, "export_framework_visibility": 7, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "platform_specificity": 4, "signed_backlog_quality": 2, "total": 28, "valuation_rerating_runway": 1, "working_capital_risk_control": 3}, "reuse_reason": null, "same_entry_group_id": "C03_000880_HANWHA_20220729_DEFENSE_GROUP_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "platform_or_customer_specificity", "backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_backlog_quality_required", "delivery_schedule_and_platform_scope_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_group_or_systems_price_premium", "backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_loss_or_delivery_delay", "framework_not_converted_to_company_backlog", "margin_revision_bridge_failure"], "symbol": "000880", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000880/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SNT_HANWHA_DEFENSE_COMPONENTS_EXPORT_FRAMEWORK_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_backlog_snt_hanwha_components_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense-export framework rows should allow Stage2 when platform/customer specificity, signed backlog, delivery cadence and margin revision bridge are visible; group-level or systems/component price premiums should route to Yellow/local 4B when direct backlog-to-margin evidence has not refreshed.",
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
3. Add C03-specific defense export framework / platform specificity / signed backlog / delivery schedule / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C03_STAGE2_ALLOWED_ON_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_REVISION_BRIDGE
- C03_GREEN_REQUIRES_PLATFORM_CUSTOMER_SCOPE_SIGNED_BACKLOG_DELIVERY_REVISION
- C03_DEFENSE_GROUP_OR_SYSTEMS_PRICE_PREMIUM_LOCAL_4B
- C03_PRICE_CONFIRMATION_WITHOUT_BACKLOG_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

