# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework backlog / Rotem-ammo-comms 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: ROTANK_AMMO_COMMS_BACKLOG_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|defense_export_framework_to_backlog_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_rotank_ammo_comms_backlog_4b_2022_2024_research.md
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

This run avoids those top-covered C03 symbols and adds 064350, 103140, and 005870.  
Each row uses a new `C03 + symbol + trigger_type + entry_date` hard key:
```text
C03 + 064350 + Stage2-Actionable + 2022-07-27
C03 + 103140 + Stage3-Yellow + 2023-03-02
C03 + 005870 + 4B-local-price-only + 2024-11-12
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
064350 현대로템: selected post-2020-08-14 forward window clean; corporate-action candidate is before selected trigger window.
103140 풍산: corporate_action_candidate_count=0; clean 2023 forward window.
005870 휴니드: selected post-2007 forward window clean; historical corporate-action candidates latest 2007-05-09, outside selected trigger window.
```

## 3. Research thesis

C03 should distinguish defense export framework evidence that converts into backlog and delivery from defense theme beta already paid in price:

```text
defense export framework / geopolitical demand
→ platform or customer specificity
→ signed backlog quality and delivery schedule
→ capacity allocation and working-capital load
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A defense framework is a gate opening. Stage2 can buy when a platform walks through the gate with backlog and delivery cadence. Green should require the walk, the schedule and the margin bridge, not just the sound of the gate.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_064350_HYUNDAIROTEM_20220727_POLAND_K2_FRAMEWORK_STAGE2 | 064350 | positive_defense_export_framework_backlog_stage2_success_with_later_4b_refresh | 2022-07-27 | 25000 | 32850 on 2022-08-26 | 23500 on 2022-10-13 | 31.4% | 31.4% | 31.4% | -6.0% | -28.46% |
| C03_103140_POONGSAN_20230302_AMMO_EXPORT_PRICE_CONFIRMATION_FALSE_GREEN | 103140 | ammo_export_framework_false_green_counterexample | 2023-03-02 | 38550 | 39600 on 2023-04-03 | 31750 on 2023-10-04 | 2.72% | 2.72% | 2.72% | -17.64% | -19.82% |
| C03_005870_HUNEED_20241112_DEFENSE_COMMS_THEME_4B | 005870 | defense_comms_theme_price_premium_counterexample | 2024-11-12 | 9670 | 10840 on 2025-03-24 | 6550 on 2024-12-09 | 0.62% | 12.1% | 12.1% | -32.26% | -34.32% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 064350 is the positive anchor. The Poland/K2 export-framework route produced strong MFE before the later premium required 4B refresh discipline.
- Stage2 is allowed only when export framework salience maps to platform/customer specificity, backlog conversion, delivery schedule and margin/revision visibility.

### Stage3 / Green
- C03 Green should require signed backlog quality, delivery schedule, platform/customer scope, capacity allocation, working-capital discipline and margin/revision confirmation.
- 103140 is the false-Green/Yellow guard: ammo/export theme price confirmation was visible, but incremental direct contract, delivery and margin evidence did not refresh enough to survive the forward path.

### 4B
- 005870 fills the defense communications/theme price-premium 4B pocket. The November 2024 spike had event momentum but lacked enough direct backlog-to-margin evidence at trigger time.
- 103140 shows the ammo version of the same failure: defense demand can be real while the listed-company trigger still lacks signed backlog and margin proof.
- 064350 also demonstrates that valid Stage2 can become local 4B after the rerating capitalizes the export framework.

### 4C
- No hard export cancellation, delivery failure, customer loss or accounting break is asserted.
- The C03 break mode here is backlog-to-margin exhaustion: export salience may remain directionally real, but incremental signed backlog, delivery cadence and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C03_005870_HUNEED_20241112_DEFENSE_COMMS_THEME_4B": {
    "delivery_schedule_visibility": 2,
    "export_framework_visibility": 6,
    "information_confidence": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 4,
    "platform_specificity": 4,
    "signed_backlog_quality": 2,
    "total": 26,
    "valuation_rerating_runway": 1,
    "working_capital_risk_control": 3
  },
  "C03_064350_HYUNDAIROTEM_20220727_POLAND_K2_FRAMEWORK_STAGE2": {
    "delivery_schedule_visibility": 8,
    "export_framework_visibility": 11,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 9,
    "platform_specificity": 10,
    "signed_backlog_quality": 8,
    "total": 70,
    "valuation_rerating_runway": 8,
    "working_capital_risk_control": 5
  },
  "C03_103140_POONGSAN_20230302_AMMO_EXPORT_PRICE_CONFIRMATION_FALSE_GREEN": {
    "delivery_schedule_visibility": 3,
    "export_framework_visibility": 7,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "platform_specificity": 6,
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

if defense_theme_price_premium and no incremental_backlog_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and backlog_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 103140 / 2023-03-02: ammo/export confirmation can be over-promoted if price strength substitutes for signed backlog and margin proof.
- 005870 / 2024-11-12: defense communications theme premium can look actionable, but fails without direct export framework, backlog conversion and margin revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -6.0, "MAE_30D_pct": -3.8, "MAE_90D_pct": -6.0, "MFE_180D_pct": 31.4, "MFE_30D_pct": 31.4, "MFE_90D_pct": 31.4, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20220727_POLAND_K2_FRAMEWORK_STAGE2", "case_role": "positive_defense_export_framework_backlog_stage2_success_with_later_4b_refresh", "company_name": "현대로템", "corporate_action_window_status": "selected post-2020-08-14 forward window clean; corporate-action candidate is 2020-08-14 and outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when the Poland/K2 export-framework story mapped to a specific platform, likely backlog conversion, delivery schedule and long-duration defense export optionality before the rerating was fully capitalized. Green still requires signed backlog quality, delivery cadence, margin/revision bridge, working-capital strain and valuation runway.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.46, "entry_date": "2022-07-27", "entry_price": 25000, "evidence_family": "defense_export_framework_K2_tank_backlog_delivery_schedule_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "ROTANK_AMMO_COMMS_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-13", "low_price_180d": 23500, "peak_date": "2022-08-26", "peak_price": 32850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"delivery_schedule_visibility": 8, "export_framework_visibility": 11, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 9, "platform_specificity": 10, "signed_backlog_quality": 8, "total": 70, "valuation_rerating_runway": 8, "working_capital_risk_control": 5}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20220727_POLAND_K2_FRAMEWORK_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "platform_or_customer_specificity", "backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_backlog_quality_required", "delivery_schedule_and_platform_scope_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_loss_or_delivery_delay", "customer_framework_not_converted_to_backlog", "margin_revision_bridge_failure"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "trigger_date": "2022-07-27", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -17.64, "MAE_30D_pct": -7.39, "MAE_90D_pct": -12.45, "MFE_180D_pct": 2.72, "MFE_30D_pct": 2.72, "MFE_90D_pct": 2.72, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_103140_POONGSAN_20230302_AMMO_EXPORT_PRICE_CONFIRMATION_FALSE_GREEN", "case_role": "ammo_export_framework_false_green_counterexample", "company_name": "풍산", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2023 forward window", "current_profile_error": true, "current_profile_verdict": "Ammo/export price confirmation should remain Yellow or local 4B when defense-demand salience is not followed by incremental signed contract backlog, customer delivery schedule, capacity allocation and margin/revision evidence. The March 2023 trigger had tiny residual upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -19.82, "entry_date": "2023-03-02", "entry_price": 38550, "evidence_family": "ammo_export_theme_price_confirmation_without_incremental_contract_backlog_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "ROTANK_AMMO_COMMS_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2023-10-04", "low_price_180d": 31750, "peak_date": "2023-04-03", "peak_price": 39600, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/103/103140.json", "raw_component_score_breakdown": {"delivery_schedule_visibility": 3, "export_framework_visibility": 7, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "platform_specificity": 6, "signed_backlog_quality": 3, "total": 32, "valuation_rerating_runway": 1, "working_capital_risk_control": 3}, "reuse_reason": null, "same_entry_group_id": "C03_103140_POONGSAN_20230302_AMMO_EXPORT_PRICE_CONFIRMATION_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "platform_or_customer_specificity", "backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_backlog_quality_required", "delivery_schedule_and_platform_scope_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_loss_or_delivery_delay", "customer_framework_not_converted_to_backlog", "margin_revision_bridge_failure"], "symbol": "103140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2023.csv", "trigger_date": "2023-03-02", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -32.26, "MAE_30D_pct": -32.26, "MAE_90D_pct": -32.26, "MFE_180D_pct": 12.1, "MFE_30D_pct": 0.62, "MFE_90D_pct": 12.1, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_005870_HUNEED_20241112_DEFENSE_COMMS_THEME_4B", "case_role": "defense_comms_theme_price_premium_counterexample", "company_name": "휴니드", "corporate_action_window_status": "selected post-2007 forward window clean; historical corporate-action candidates latest 2007-05-09 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Defense communications/theme price premium should route to local 4B/counterexample unless the move is backed by direct export framework, named customer contract, backlog conversion, delivery schedule and margin/revision evidence. Later theme re-acceleration should not rewrite a weak price-only trigger as clean Stage2/Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.32, "entry_date": "2024-11-12", "entry_price": 9670, "evidence_family": "defense_comms_export_theme_price_premium_without_direct_contract_backlog_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "ROTANK_AMMO_COMMS_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2024-12-09", "low_price_180d": 6550, "peak_date": "2025-03-24", "peak_price": 10840, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005870.json", "raw_component_score_breakdown": {"delivery_schedule_visibility": 2, "export_framework_visibility": 6, "information_confidence": 3, "margin_revision_bridge": 1, "market_mispricing": 4, "platform_specificity": 4, "signed_backlog_quality": 2, "total": 26, "valuation_rerating_runway": 1, "working_capital_risk_control": 3}, "reuse_reason": null, "same_entry_group_id": "C03_005870_HUNEED_20241112_DEFENSE_COMMS_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_visibility", "platform_or_customer_specificity", "backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["signed_backlog_quality_required", "delivery_schedule_and_platform_scope_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_loss_or_delivery_delay", "customer_framework_not_converted_to_backlog", "margin_revision_bridge_failure"], "symbol": "005870", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005870/2024.csv", "trigger_date": "2024-11-12", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "ROTANK_AMMO_COMMS_BACKLOG_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_backlog_rotank_ammo_comms_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense-export rows should allow Stage2 only when export framework evidence maps to platform/customer specificity, signed backlog quality, delivery schedule and margin-revision bridge; price premiums in ammo/comms/theme names should route to Yellow/local 4B when direct backlog-to-margin evidence has not refreshed.",
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
- C03_DEFENSE_THEME_PRICE_PREMIUM_LOCAL_4B
- C03_PRICE_CONFIRMATION_WITHOUT_BACKLOG_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

