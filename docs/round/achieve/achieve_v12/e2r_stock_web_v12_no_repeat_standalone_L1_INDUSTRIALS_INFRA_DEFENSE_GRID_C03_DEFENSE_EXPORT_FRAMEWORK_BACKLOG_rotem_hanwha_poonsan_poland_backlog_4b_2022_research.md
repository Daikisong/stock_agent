# E2R V12 No-Repeat Standalone Residual Research
## R1 / L1 / C03 — Defense export framework backlog / Rotem-Hanwha-Poonsan 4B guard

metadata:
```text
selected_round: R1
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: ROTEM_HANWHA_POONSAN_POLAND_BACKLOG_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|defense_export_framework_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_rotem_hanwha_poonsan_poland_backlog_4b_2022_research.md
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
Each row uses a new `C03 + symbol + trigger_type + entry_date` hard key:
```text
C03 + 064350 + Stage2-Actionable + 2022-07-29
C03 + 272210 + Stage3-Yellow + 2022-08-26
C03 + 103140 + 4B-local-price-only + 2022-09-05
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
064350 현대로템: selected post-2020 forward window clean; profile corporate-action candidate is 2020-08-14 and outside selected trigger window.
272210 한화시스템: selected post-2021 forward window clean; profile corporate-action candidate is 2021-06-23 and outside selected trigger window.
103140 풍산: corporate_action_candidate_count=0; clean 2022/2023 forward window.
```

## 3. Research thesis

C03 should split real defense export framework/backlog conversion from defense export theme beta already paid in price:

```text
defense export framework / named platform
→ named customer or country quality
→ contract/framework finality
→ delivery cadence and production capacity
→ working-capital discipline
→ margin and revision bridge
→ Stage2/Green or local 4B cap
```

A defense export framework is not just a headline; it is a convoy schedule. Stage2 can buy when the convoy has a named destination, named platform and credible delivery path. Green should not buy the parade after the market has already priced the convoy and fresh margin evidence is missing.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_EXPORT_STAGE2 | 064350 | positive_defense_export_framework_backlog_stage2_success_with_later_4b_refresh | 2022-07-29 | 26550 | 32850 on 2022-08-26 | 23200 on 2022-10-26 | 23.73% | 23.73% | 23.73% | -12.62% | -29.38% |
| C03_272210_HANWHASYSTEMS_20220826_DEFENSE_SYSTEM_EXPORT_FALSE_GREEN | 272210 | defense_system_export_framework_false_green_counterexample | 2022-08-26 | 15800 | 16200 on 2022-09-01 | 10150 on 2022-10-13 | 2.53% | 2.53% | 2.53% | -35.76% | -37.35% |
| C03_103140_POONGSAN_20220905_AMMO_EXPORT_FRAMEWORK_PRICE_PREMIUM_4B | 103140 | ammo_export_framework_price_premium_local_4B_counterexample | 2022-09-05 | 31600 | 34750 on 2022-12-28 | 24150 on 2022-09-28 | 4.43% | 9.97% | 9.97% | -23.58% | -10.94% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 064350 is the positive anchor. The July 2022 Poland K2 export framework route produced useful MFE before the August 2022 premium required 4B refresh discipline.
- Stage2 is allowed only when defense export salience maps to named customer/country, platform specificity, contract/framework finality, delivery cadence and margin/revision visibility.
- 가격만 있는 early entry는 금지된다. This positive row is included because the trigger family is named export-framework/backlog evidence, not price-only momentum.

### Stage3 / Green
- C03 Green should require contract or framework finality, production/delivery cadence, backlog conversion, working-capital discipline and margin revision.
- 272210 is the false-Green/Yellow guard: defense-system export salience was visible, but the August 2022 price had tiny residual upside and much larger forward MAE when named-order-to-margin evidence did not refresh.

### 4B
- 103140 fills the ammunition/export-framework price-premium 4B pocket. Defense-cycle salience remained directionally real, but the September 2022 entry first suffered a large MAE before later recovery.
- 272210 shows the same failure in defense-systems form: export theme salience can remain real while the listed-company earnings bridge is too stale for Green.
- 064350 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the named export-framework option.

### 4C
- No hard contract cancellation, delivery failure, sanctions block, customer loss or accounting break is asserted.
- The C03 break mode here is framework-to-margin exhaustion: the export story may remain directionally real, but incremental named order, delivery cadence, working capital and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_EXPORT_STAGE2": {
    "contract_finality_or_backlog_visibility": 8,
    "defense_export_framework_salience": 10,
    "delivery_cadence_and_capacity": 6,
    "information_confidence": 4,
    "margin_revision_bridge": 5,
    "market_mispricing": 8,
    "named_customer_or_country_quality": 10,
    "platform_specificity": 9,
    "total": 71,
    "valuation_rerating_runway": 7,
    "working_capital_quality": 4
  },
  "C03_103140_POONGSAN_20220905_AMMO_EXPORT_FRAMEWORK_PRICE_PREMIUM_4B": {
    "contract_finality_or_backlog_visibility": 3,
    "defense_export_framework_salience": 7,
    "delivery_cadence_and_capacity": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "named_customer_or_country_quality": 3,
    "platform_specificity": 5,
    "total": 36,
    "valuation_rerating_runway": 2,
    "working_capital_quality": 3
  },
  "C03_272210_HANWHASYSTEMS_20220826_DEFENSE_SYSTEM_EXPORT_FALSE_GREEN": {
    "contract_finality_or_backlog_visibility": 3,
    "defense_export_framework_salience": 8,
    "delivery_cadence_and_capacity": 2,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "named_customer_or_country_quality": 4,
    "platform_specificity": 5,
    "total": 35,
    "valuation_rerating_runway": 1,
    "working_capital_quality": 3
  }
}
```

## 7. Current calibrated profile stress test

Suggested C03 guard:
```text
if defense_export_framework and named_country_platform_contract_delivery_margin_bridge_visible:
    allow_stage2_actionable = true

if defense_export_price_premium and no incremental_named_order_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and framework_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 272210 / 2022-08-26: defense-system export confirmation can be over-promoted if price strength substitutes for named order, delivery and margin proof.
- 103140 / 2022-09-05: ammunition/export-framework premium can look actionable, but fails without refreshed contract/backlog and revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.62, "MAE_30D_pct": -9.42, "MAE_90D_pct": -12.62, "MFE_180D_pct": 23.73, "MFE_30D_pct": 23.73, "MFE_90D_pct": 23.73, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_EXPORT_STAGE2", "case_role": "positive_defense_export_framework_backlog_stage2_success_with_later_4b_refresh", "company_name": "현대로템", "corporate_action_window_status": "selected post-2020 forward window clean; profile corporate-action candidate is 2020-08-14 and outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when the Poland K2 export framework converted defense-policy salience into a named platform, named customer/country, backlog option and delivery visibility before the rerating was fully capitalized. Green still requires contract finality, production/delivery cadence, margin/revision bridge, working-capital discipline and follow-on order visibility; after the August 2022 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.38, "entry_date": "2022-07-29", "entry_price": 26550, "evidence_family": "Poland_K2_tank_export_framework_named_order_backlog_delivery_option_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "ROTEM_HANWHA_POONSAN_POLAND_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-26", "low_price_180d": 23200, "peak_date": "2022-08-26", "peak_price": 32850, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064350.json", "raw_component_score_breakdown": {"contract_finality_or_backlog_visibility": 8, "defense_export_framework_salience": 10, "delivery_cadence_and_capacity": 6, "information_confidence": 4, "margin_revision_bridge": 5, "market_mispricing": 8, "named_customer_or_country_quality": 10, "platform_specificity": 9, "total": 71, "valuation_rerating_runway": 7, "working_capital_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C03_064350_HYUNDAIROTEM_20220729_POLAND_K2_EXPORT_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_salience", "named_customer_or_country_quality", "contract_backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["named_contract_or_framework_finality_required", "delivery_cadence_and_capacity_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "export_backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_delay_or_framework_nonconversion", "delivery_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "064350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv", "trigger_date": "2022-07-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -35.76, "MAE_30D_pct": -30.7, "MAE_90D_pct": -35.76, "MFE_180D_pct": 2.53, "MFE_30D_pct": 2.53, "MFE_90D_pct": 2.53, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_272210_HANWHASYSTEMS_20220826_DEFENSE_SYSTEM_EXPORT_FALSE_GREEN", "case_role": "defense_system_export_framework_false_green_counterexample", "company_name": "한화시스템", "corporate_action_window_status": "selected post-2021 forward window clean; profile corporate-action candidate is 2021-06-23 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Defense-system export price confirmation should remain Yellow or local 4B when the stock has defense export salience but lacks fresh named order, project/framework conversion, backlog delivery cadence and margin/revision evidence. The August 2022 trigger had tiny residual upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.35, "entry_date": "2022-08-26", "entry_price": 15800, "evidence_family": "defense_systems_export_theme_price_confirmation_without_incremental_named_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "ROTEM_HANWHA_POONSAN_POLAND_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-10-13", "low_price_180d": 10150, "peak_date": "2022-09-01", "peak_price": 16200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/272/272210.json", "raw_component_score_breakdown": {"contract_finality_or_backlog_visibility": 3, "defense_export_framework_salience": 8, "delivery_cadence_and_capacity": 2, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "named_customer_or_country_quality": 4, "platform_specificity": 5, "total": 35, "valuation_rerating_runway": 1, "working_capital_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C03_272210_HANWHASYSTEMS_20220826_DEFENSE_SYSTEM_EXPORT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_salience", "named_customer_or_country_quality", "contract_backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["named_contract_or_framework_finality_required", "delivery_cadence_and_capacity_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "export_backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_delay_or_framework_nonconversion", "delivery_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "272210", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2022.csv", "trigger_date": "2022-08-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -23.58, "MAE_30D_pct": -23.58, "MAE_90D_pct": -23.58, "MFE_180D_pct": 9.97, "MFE_30D_pct": 4.43, "MFE_90D_pct": 9.97, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_id": "C03_103140_POONGSAN_20220905_AMMO_EXPORT_FRAMEWORK_PRICE_PREMIUM_4B", "case_role": "ammo_export_framework_price_premium_local_4B_counterexample", "company_name": "풍산", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2022/2023 forward window", "current_profile_error": true, "current_profile_verdict": "Ammunition/export-framework premium should route to local 4B or counterexample when the market has already capitalized defense-cycle optionality and fresh named order, export framework conversion, delivery cadence and margin/revision evidence do not refresh. The September 2022 trigger had drawdown before later recovery, so it should not be treated as clean Stage2/Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -10.94, "entry_date": "2022-09-05", "entry_price": 31600, "evidence_family": "ammunition_export_framework_copper_defense_theme_price_premium_without_named_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "ROTEM_HANWHA_POONSAN_POLAND_BACKLOG_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "low_date_180d": "2022-09-28", "low_price_180d": 24150, "peak_date": "2022-12-28", "peak_price": 34750, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/103/103140.json", "raw_component_score_breakdown": {"contract_finality_or_backlog_visibility": 3, "defense_export_framework_salience": 7, "delivery_cadence_and_capacity": 3, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "named_customer_or_country_quality": 3, "platform_specificity": 5, "total": 36, "valuation_rerating_runway": 2, "working_capital_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C03_103140_POONGSAN_20220905_AMMO_EXPORT_FRAMEWORK_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R1", "source_proxy_only": false, "stage2_evidence_fields": ["defense_export_framework_salience", "named_customer_or_country_quality", "contract_backlog_delivery_margin_revision_route"], "stage3_evidence_fields": ["named_contract_or_framework_finality_required", "delivery_cadence_and_capacity_required", "margin_revision_and_working_capital_bridge_required"], "stage4b_evidence_fields": ["defense_export_theme_price_premium", "export_backlog_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_delay_or_framework_nonconversion", "delivery_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "103140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2022.csv", "trigger_date": "2022-09-05", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "ROTEM_HANWHA_POONSAN_POLAND_BACKLOG_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "loop_contribution_label": "defense_export_framework_backlog_new_symbols_rotem_hanwha_systems_poonsan_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R1",
  "shadow_rule_candidate": "C03 defense-export rows should allow Stage2 when named customer/country, platform specificity, contract/framework finality, delivery cadence and margin-revision bridge are visible, but route defense export price premiums to Yellow/local 4B when named-order-to-margin evidence has not refreshed.",
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
3. Add C03-specific defense export framework / named customer-country / platform specificity / contract finality / delivery cadence / working-capital / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C03_STAGE2_ALLOWED_ON_NAMED_EXPORT_FRAMEWORK_DELIVERY_MARGIN_REVISION_BRIDGE
- C03_GREEN_REQUIRES_CONTRACT_FINALITY_DELIVERY_BACKLOG_WORKING_CAPITAL_REVISION
- C03_DEFENSE_EXPORT_PRICE_PREMIUM_LOCAL_4B
- C03_PRICE_CONFIRMATION_WITHOUT_FRAMEWORK_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.

