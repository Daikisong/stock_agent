# E2R V12 No-Repeat Standalone Residual Research
## R11 / L10 / C31 — Policy subsidy legislation event / East-Sea oil-gas theme 4B guard

metadata:
```text
selected_round: R11
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: EAST_SEA_OIL_GAS_POLICY_THEME_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|policy_to_company_conversion_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_east_sea_oil_gas_policy_theme_4b_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT current coverage:
rows=34, symbols=14, date range=2020-07-15~2024-07-18, good/bad S2=10/10, 4B/4C=1/0
top covered symbols: 112610(6), 034020(4), 336260(4), UNKNOWN_SYMBOL(4), 036460(3)
```

This run avoids those top-covered C31 symbols and adds 004090, 024060, and 117580.  
Each row uses a new `C31 + symbol + trigger_type + entry_date` hard key.

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
004090 한국석유: selected 2024 forward window clean; corporate-action candidates are 1997-08-07, 2021-04-15, 2021-05-07, outside selected test window.
024060 흥구석유: selected 2024 forward window clean; corporate-action candidates are historical and outside selected test window.
117580 대성에너지: corporate_action_candidate_count=0; clean 2024 forward window.
```

## 3. Research thesis

C31 should not treat a policy headline as direct company-level earnings evidence. It should test policy-to-company conversion:

```text
policy / legislation / national project headline
→ direct company entitlement, license, supplier role or project participation
→ project finality and financing
→ order, tariff/spread, volume or revenue conversion
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A policy headline is a lighthouse. It tells the market where to look, but Green should require the ship to dock at the listed company: entitlement, order, revenue and revision.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C31_004090_KOREAPETROLEUM_20240603_EAST_SEA_OIL_GAS_POLICY_THEME_4B | 004090 | protective_policy_event_oil_gas_theme_4b_success | 2024-06-03 | 17950 | 28100 on 2024-06-05 | 12240 on 2024-12-09 | 56.55% | 56.55% | 56.55% | -31.81% | -56.44% |
| C31_024060_HEUNGGOO_20240603_EAST_SEA_OIL_GAS_THEME_FALSE_GREEN | 024060 | oil_distribution_policy_theme_false_green_counterexample | 2024-06-03 | 16250 | 23000 on 2024-10-04 | 11950 on 2024-12-09 | 28.92% | 41.54% | 41.54% | -26.46% | -48.04% |
| C31_117580_DAESUNGENERGY_20240603_EAST_SEA_GAS_POLICY_THEME_4B | 117580 | city_gas_policy_theme_price_premium_counterexample | 2024-06-03 | 10990 | 14100 on 2024-06-04 | 7680 on 2024-12-09 | 28.3% | 28.3% | 28.3% | -30.12% | -45.53% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C31 Green should require direct company entitlement, license/project role, project finality, order/revenue conversion, tariff/spread economics and margin/revision confirmation.
- 024060 is the false-Green/Yellow guard: policy-theme price confirmation remained strong enough to create MFE, but company-level conversion evidence was too weak to justify Green.

### 4B
- 004090 is the protective 4B anchor. The policy event was real as a trading catalyst, but the listed company conversion bridge was not visible enough to sustain a Stage2/Green interpretation.
- 117580 shows the city-gas version of the same failure: policy salience does not automatically create tariff, volume or margin revision evidence.
- The core 4B rule is that policy salience must not be substituted for direct entitlement, project finality, order/revenue conversion and margin revisions.

### 4C
- No hard project cancellation, failed license, or legal rejection is asserted.
- The failure mode is policy-to-company conversion gap: the national project theme can remain real while the listed theme stock fails to convert it into direct, margin-accretive evidence.

## 6. Raw component score breakdown

```json
{
  "C31_004090_KOREAPETROLEUM_20240603_EAST_SEA_OIL_GAS_POLICY_THEME_4B": {
    "direct_company_entitlement": 2,
    "information_confidence": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "order_revenue_conversion": 1,
    "policy_event_salience": 10,
    "project_finality_or_license_bridge": 2,
    "total": 23,
    "valuation_rerating_runway": 1
  },
  "C31_024060_HEUNGGOO_20240603_EAST_SEA_OIL_GAS_THEME_FALSE_GREEN": {
    "direct_company_entitlement": 1,
    "information_confidence": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 4,
    "order_revenue_conversion": 1,
    "policy_event_salience": 10,
    "project_finality_or_license_bridge": 2,
    "total": 23,
    "valuation_rerating_runway": 1
  },
  "C31_117580_DAESUNGENERGY_20240603_EAST_SEA_GAS_POLICY_THEME_4B": {
    "direct_company_entitlement": 1,
    "information_confidence": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "order_revenue_conversion": 1,
    "policy_event_salience": 9,
    "project_finality_or_license_bridge": 2,
    "total": 21,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C31 guard:
```text
if policy_event and direct_company_entitlement_revenue_margin_bridge_visible:
    allow_stage2_actionable = true

if policy_theme_price_premium and no direct_entitlement_project_finality_revenue_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and policy_to_company_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 024060 / 2024-06-03: oil-distribution policy theme can be over-promoted if price confirmation substitutes for direct project revenue and margin evidence.
- 117580 / 2024-06-03: city-gas policy theme can look like actionable policy leverage, but fails without tariff/volume/margin conversion.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -31.81, "MAE_30D_pct": -7.41, "MAE_90D_pct": -14.99, "MFE_180D_pct": 56.55, "MFE_30D_pct": 56.55, "MFE_90D_pct": 56.55, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_004090_KOREAPETROLEUM_20240603_EAST_SEA_OIL_GAS_POLICY_THEME_4B", "case_role": "protective_policy_event_oil_gas_theme_4b_success", "company_name": "한국석유", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 1997-08-07, 2021-04-15, 2021-05-07 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when East-Sea oil/gas policy salience had already been capitalized by oil-theme price action but company-specific revenue conversion evidence was absent. The policy event was real, but without direct license/participation, customer order, reserve economics, capex role and margin/revision bridge, the spike should not be promoted to Stage2 or Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -56.44, "entry_date": "2024-06-03", "entry_price": 17950, "evidence_family": "east_sea_oil_gas_policy_theme_price_premium_without_company_level_license_order_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "EAST_SEA_OIL_GAS_POLICY_THEME_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-12-09", "low_price_180d": 12240, "peak_date": "2024-06-05", "peak_price": 28100, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/004/004090.json", "raw_component_score_breakdown": {"direct_company_entitlement": 2, "information_confidence": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "order_revenue_conversion": 1, "policy_event_salience": 10, "project_finality_or_license_bridge": 2, "total": 23, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C31_004090_KOREAPETROLEUM_20240603_EAST_SEA_OIL_GAS_POLICY_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["policy_or_legislation_event_attention", "direct_company_entitlement_or_project_role_required", "revenue_conversion_margin_revision_route_required"], "stage3_evidence_fields": ["project_finality_or_license_required", "company_specific_revenue_conversion_required", "tariff_spread_order_or_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_event_theme_price_premium", "policy_salience_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_finality_failure", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "004090", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv", "trigger_date": "2024-06-03", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -26.46, "MAE_30D_pct": -15.69, "MAE_90D_pct": -21.91, "MFE_180D_pct": 41.54, "MFE_30D_pct": 28.92, "MFE_90D_pct": 41.54, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_024060_HEUNGGOO_20240603_EAST_SEA_OIL_GAS_THEME_FALSE_GREEN", "case_role": "oil_distribution_policy_theme_false_green_counterexample", "company_name": "흥구석유", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 1997-09-11, 1998-04-08, 1998-08-24, 2008-08-26, 2008-10-06, 2008-10-24 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Oil/gas policy-theme price confirmation should remain Yellow or local 4B when the listed company is not directly converted into project revenue. The row shows why policy salience and liquidity alone should not substitute for direct participation, order/revenue conversion, inventory spread, pricing power and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.04, "entry_date": "2024-06-03", "entry_price": 16250, "evidence_family": "oil_distribution_policy_theme_price_confirmation_without_direct_project_revenue_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "EAST_SEA_OIL_GAS_POLICY_THEME_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-12-09", "low_price_180d": 11950, "peak_date": "2024-10-04", "peak_price": 23000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/024/024060.json", "raw_component_score_breakdown": {"direct_company_entitlement": 1, "information_confidence": 3, "margin_revision_bridge": 1, "market_mispricing": 4, "order_revenue_conversion": 1, "policy_event_salience": 10, "project_finality_or_license_bridge": 2, "total": 23, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C31_024060_HEUNGGOO_20240603_EAST_SEA_OIL_GAS_THEME_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["policy_or_legislation_event_attention", "direct_company_entitlement_or_project_role_required", "revenue_conversion_margin_revision_route_required"], "stage3_evidence_fields": ["project_finality_or_license_required", "company_specific_revenue_conversion_required", "tariff_spread_order_or_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_event_theme_price_premium", "policy_salience_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_finality_failure", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "024060", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024060/2024.csv", "trigger_date": "2024-06-03", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -30.12, "MAE_30D_pct": -18.74, "MAE_90D_pct": -23.48, "MFE_180D_pct": 28.3, "MFE_30D_pct": 28.3, "MFE_90D_pct": 28.3, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_117580_DAESUNGENERGY_20240603_EAST_SEA_GAS_POLICY_THEME_4B", "case_role": "city_gas_policy_theme_price_premium_counterexample", "company_name": "대성에너지", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "City-gas policy-theme premium should route to local 4B or counterexample unless project entitlement, tariff/pass-through economics, volume effect and margin/revision evidence are visible. The price spike had little durable evidence bridge and later reverted.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.53, "entry_date": "2024-06-03", "entry_price": 10990, "evidence_family": "city_gas_policy_theme_price_premium_without_project_entitlement_tariff_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "EAST_SEA_OIL_GAS_POLICY_THEME_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-12-09", "low_price_180d": 7680, "peak_date": "2024-06-04", "peak_price": 14100, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/117/117580.json", "raw_component_score_breakdown": {"direct_company_entitlement": 1, "information_confidence": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "order_revenue_conversion": 1, "policy_event_salience": 9, "project_finality_or_license_bridge": 2, "total": 21, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C31_117580_DAESUNGENERGY_20240603_EAST_SEA_GAS_POLICY_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["policy_or_legislation_event_attention", "direct_company_entitlement_or_project_role_required", "revenue_conversion_margin_revision_route_required"], "stage3_evidence_fields": ["project_finality_or_license_required", "company_specific_revenue_conversion_required", "tariff_spread_order_or_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_event_theme_price_premium", "policy_salience_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["project_finality_failure", "company_entitlement_absence", "revenue_margin_revision_bridge_failure"], "symbol": "117580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/117/117580/2024.csv", "trigger_date": "2024-06-03", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "EAST_SEA_OIL_GAS_POLICY_THEME_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "loop_contribution_label": "policy_event_east_sea_oil_gas_theme_price_premium_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R11",
  "shadow_rule_candidate": "C31 policy-event rows should block Stage2/Green when a policy or legislation headline lacks company-specific entitlement, project finality, order/revenue conversion, tariff/spread economics and margin/revision bridge; theme price premiums should route to local 4B/counterexample even when the policy event itself is real.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C31 + symbol + trigger_type + entry_date.
3. Add C31-specific policy-event / company-entitlement / project-finality / revenue-conversion / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C31_BLOCK_GREEN_WITHOUT_DIRECT_COMPANY_ENTITLEMENT_REVENUE_MARGIN_BRIDGE
- C31_POLICY_THEME_PRICE_PREMIUM_LOCAL_4B
- C31_REQUIRE_PROJECT_FINALITY_LICENSE_ORDER_TARIFF_REVISION
- C31_POLICY_SALIENCE_WITHOUT_COMPANY_CONVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

