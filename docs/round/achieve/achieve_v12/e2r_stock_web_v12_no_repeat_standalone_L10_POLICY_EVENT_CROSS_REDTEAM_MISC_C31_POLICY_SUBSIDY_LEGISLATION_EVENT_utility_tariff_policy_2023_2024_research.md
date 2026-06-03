# E2R V12 No-Repeat Standalone Residual Research
## R13 / L10 / C31 — Utility tariff / public policy pass-through guard

metadata:
```text
selected_round: R13
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: UTILITY_TARIFF_PUBLIC_POLICY_PASS_THROUGH_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_utility_tariff_policy_2023_2024_research.md
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

This run avoids those top-covered C31 symbols and adds 071320, 015760, and 130660.  
Each row uses a new `C31 + symbol + trigger_type + entry_date` hard key.

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
071320 지역난방공사: corporate_action_candidate_count=0.
015760 한국전력: corporate_action_candidate_count=0.
130660 한전산업: corporate_action_candidate_count=0; 14 non-tradable zero-volume raw rows are excluded from tradable calibration shards.
```

## 3. Research thesis

C31 should not treat a policy headline as earnings. It should ask whether the policy converts into company-level pass-through:

```text
policy / subsidy / tariff / legislation event
→ explicit formula or regulatory cadence
→ regulated revenue or subsidy conversion
→ cost pass-through and debt/margin bridge
→ revision confirmation
→ rerating
```

The useful distinction is between a rule and a rumor. A tariff formula is a pipe; a policy headline is only a signpost. The model should pay for the pipe, not the signpost.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C31_071320_KDH_20240126_HEAT_TARIFF_NORMALIZATION_POLICY_STAGE2_SUCCESS | 071320 | positive_tariff_policy_stage2_success | 2024-01-26 | 29000 | 53900 on 2024-06-18 | 27500 on 2024-01-26 | 76.9% | 85.86% | 85.86% | -5.17% | -25.14% |
| C31_015760_KEPCO_20230515_ELECTRICITY_TARIFF_HIKE_FALSE_GREEN | 015760 | tariff_hike_false_green_counterexample | 2023-05-15 | 19280 | 20850 on 2023-07-13 | 16030 on 2023-10-24 | 4.25% | 8.14% | 8.14% | -16.86% | -23.12% |
| C31_130660_KEPID_20240718_NUCLEAR_PUBLIC_POLICY_PRICE_PREMIUM_4B | 130660 | public_policy_price_premium_counterexample | 2024-07-18 | 17740 | 19500 on 2024-07-18 | 8880 on 2024-12-09 | 9.92% | 9.92% | 9.92% | -49.94% | -54.46% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Policy, tariff and public-utility events can be valid Stage2 routes.
- 071320 is the positive anchor: the heat-tariff/pass-through policy route produced a strong rerating window when the market could connect regulated revenue to operating leverage.

### Stage3 / Green
- C31 Green should require more than the headline: explicit pass-through or subsidy formula, cadence, regulated-revenue conversion, debt/margin and revision bridge.
- 015760 shows the false-Green risk. A tariff hike can help, but partial pass-through does not automatically repair debt, fuel-cost burden and revision quality.

### 4B
- 130660 is the local 4B guard. Public policy/nuclear-utility price premium expanded sharply, but without company-level contract or regulated-revenue conversion, it should not be fresh Green.
- Policy events often have a short half-life: price reacts to the headline before the income statement can prove it.

### 4C
- No hard 4C/accounting break is asserted.
- The break mode is conversion failure: the policy remains real, but the stock does not receive enough company-level revenue, cost-pass-through, debt relief or revision evidence to carry the premium.

## 6. Raw component score breakdown

```json
{
  "C31_015760_KEPCO_20230515_ELECTRICITY_TARIFF_HIKE_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 4,
    "market_mispricing": 7,
    "total": 32,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  },
  "C31_071320_KDH_20240126_HEAT_TARIFF_NORMALIZATION_POLICY_STAGE2_SUCCESS": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 57,
    "valuation_rerating_runway": 10,
    "visibility_quality": 12
  },
  "C31_130660_KEPID_20240718_NUCLEAR_PUBLIC_POLICY_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C31 guard:
```text
if policy_tariff_event and explicit_formula_plus_revenue_conversion_visible:
    allow_stage2_actionable_or_green_candidate = true

if policy_event_headline and no cost_pass_through_debt_margin_revision_bridge:
    cap_stage = Stage3-Yellow
    block_stage3_green = true

if public_policy_price_premium and no company_level_contract_or_revenue_conversion:
    route_to_local_4B_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 015760 / 2023-05-15: electricity tariff hike can be over-promoted if fuel-cost pass-through, debt burden and revision bridge are not required.
- 130660 / 2024-07-18: public-utility/nuclear policy premium can become a price-only blowoff when company-level contract or regulated revenue does not close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -5.17, "MAE_30D_pct": -5.17, "MAE_90D_pct": -5.17, "MFE_180D_pct": 85.86, "MFE_30D_pct": 76.9, "MFE_90D_pct": 85.86, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_071320_KDH_20240126_HEAT_TARIFF_NORMALIZATION_POLICY_STAGE2_SUCCESS", "case_role": "positive_tariff_policy_stage2_success", "company_name": "지역난방공사", "corporate_action_window_status": "clean_180d_by_profile_or_no_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when heat-tariff normalization and pass-through policy could connect to operating leverage; Green still requires explicit tariff formula, cost-pass-through durability, debt and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -25.14, "entry_date": "2024-01-26", "entry_price": 29000, "evidence_family": "district_heat_tariff_normalization_policy_pass_through_operating_leverage", "evidence_url_pending": false, "fine_archetype_id": "UTILITY_TARIFF_PUBLIC_POLICY_PASS_THROUGH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-01-26", "low_price_180d": 27500, "peak_date": "2024-06-18", "peak_price": 53900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/071/071320.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 57, "valuation_rerating_runway": 10, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C31_071320_KDH_20240126_HEAT_TARIFF_NORMALIZATION_POLICY_STAGE2_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["policy_tariff_or_subsidy_event_attention", "regulated_price_or_public_policy_route", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["cost_pass_through_or_subsidy_formula_required", "regulated_revenue_conversion_required", "debt_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_event_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_disappointment_or_regulatory_cadence_gap", "cost_pass_through_shortfall", "debt_or_margin_revision_break"], "symbol": "071320", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv", "trigger_date": "2024-01-26", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -16.86, "MAE_30D_pct": -5.96, "MAE_90D_pct": -5.96, "MFE_180D_pct": 8.14, "MFE_30D_pct": 4.25, "MFE_90D_pct": 8.14, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_015760_KEPCO_20230515_ELECTRICITY_TARIFF_HIKE_FALSE_GREEN", "case_role": "tariff_hike_false_green_counterexample", "company_name": "한국전력", "corporate_action_window_status": "clean_180d_by_profile_or_no_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Electricity tariff hikes should not become Green unless fuel-cost pass-through, regulatory cadence, debt burden and revision bridge close; partial tariff hikes can remain Yellow/counterexample.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -23.12, "entry_date": "2023-05-15", "entry_price": 19280, "evidence_family": "electricity_tariff_hike_policy_without_full_cost_pass_through_debt_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "UTILITY_TARIFF_PUBLIC_POLICY_PASS_THROUGH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2023-10-24", "low_price_180d": 16030, "peak_date": "2023-07-13", "peak_price": 20850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/015/015760.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 4, "market_mispricing": 7, "total": 32, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C31_015760_KEPCO_20230515_ELECTRICITY_TARIFF_HIKE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["policy_tariff_or_subsidy_event_attention", "regulated_price_or_public_policy_route", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["cost_pass_through_or_subsidy_formula_required", "regulated_revenue_conversion_required", "debt_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_event_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_disappointment_or_regulatory_cadence_gap", "cost_pass_through_shortfall", "debt_or_margin_revision_break"], "symbol": "015760", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/015/015760/2023.csv", "trigger_date": "2023-05-15", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -49.94, "MAE_30D_pct": -32.81, "MAE_90D_pct": -28.13, "MFE_180D_pct": 9.92, "MFE_30D_pct": 9.92, "MFE_90D_pct": 9.92, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_130660_KEPID_20240718_NUCLEAR_PUBLIC_POLICY_PRICE_PREMIUM_4B", "case_role": "public_policy_price_premium_counterexample", "company_name": "한전산업", "corporate_action_window_status": "clean_180d_by_profile_or_no_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Nuclear/public-utility policy premium should route to local 4B or Yellow unless company-level contract, regulated-revenue conversion, margin and revision evidence close.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -54.46, "entry_date": "2024-07-18", "entry_price": 17740, "evidence_family": "public_utility_nuclear_policy_event_premium_without_contract_revenue_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "UTILITY_TARIFF_PUBLIC_POLICY_PASS_THROUGH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2024-12-09", "low_price_180d": 8880, "peak_date": "2024-07-18", "peak_price": 19500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/130/130660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C31_130660_KEPID_20240718_NUCLEAR_PUBLIC_POLICY_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["policy_tariff_or_subsidy_event_attention", "regulated_price_or_public_policy_route", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["cost_pass_through_or_subsidy_formula_required", "regulated_revenue_conversion_required", "debt_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_event_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_disappointment_or_regulatory_cadence_gap", "cost_pass_through_shortfall", "debt_or_margin_revision_break"], "symbol": "130660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv", "trigger_date": "2024-07-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "UTILITY_TARIFF_PUBLIC_POLICY_PASS_THROUGH_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "loop_contribution_label": "utility_tariff_public_policy_pass_through_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R13",
  "shadow_rule_candidate": "C31 policy/subsidy/legislation rows should allow Stage2 on policy event attention, but Stage3 Green requires explicit pass-through/subsidy formula, regulated-revenue conversion, debt/margin and revision bridge; policy price premium without company-level conversion should route to local 4B or counterexample.",
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
3. Add C31-specific policy/tariff/subsidy pass-through conversion guard only as a shadow candidate until more rows exist.

Candidate rule:
- C31_GREEN_REQUIRES_POLICY_FORMULA_REVENUE_CONVERSION_MARGIN_REVISION
- C31_TARIFF_HEADLINE_WITHOUT_COST_PASS_THROUGH_STAGE3_CAP
- C31_PUBLIC_POLICY_PRICE_PREMIUM_LOCAL_4B
- C31_POLICY_HEADLINE_WITHOUT_COMPANY_LEVEL_CONVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

