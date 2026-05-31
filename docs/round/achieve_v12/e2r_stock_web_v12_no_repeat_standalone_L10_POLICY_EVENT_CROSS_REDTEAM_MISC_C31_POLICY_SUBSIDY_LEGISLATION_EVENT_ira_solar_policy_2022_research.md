# E2R V12 No-Repeat Standalone Residual Research
## R11 / L10 / C31 — IRA solar policy subsidy conversion guard

metadata:
```text
selected_round: R11
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: IRA_SOLAR_POLICY_SUBSIDY_CONVERSION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_ira_solar_policy_2022_research.md
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

This run avoids the repeated C31 symbols above and adds 009830, 322000, and 010060.  
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
009830 한화솔루션: 2022 window clean; corporate-action candidates are 1999-04-20 and 2008-07-04.
322000 HD현대에너지솔루션: corporate_action_candidate_count=0.
010060 OCI: 2022 window clean; corporate-action candidates are 1999-04-16, 2001-05-18, 2023-05-30, 2023-10-13.
```

## 3. Research thesis

C31 is not a policy-headline bucket. It should test whether legislation actually travels through the pipeline:

```text
policy / legislation / subsidy headline
→ funded budget or enforceable subsidy
→ company-specific order / capacity / manufacturing route
→ margin bridge
→ revision confirmation
```

The 2022 IRA solar policy window is useful because it produced real attention and strong price movement, but it also shows why policy premium must be separated from company-level conversion.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C31_009830_HANWHA_SOLUTIONS_20220812_IRA_SOLAR_POLICY_STAGE2_4B | 009830 | policy_positive_but_4b_required | 2022-08-12 | 46250 | 55900 on 2022-09-15 | 39100 on 2023-01-06 | 20.86% | -15.46% | -30.05% |
| C31_322000_HDHES_20220812_IRA_SOLAR_POLICY_PRICE_ONLY_BLOWOFF | 322000 | policy_event_blowoff_counterexample | 2022-08-12 | 55500 | 86200 on 2022-09-15 | 47850 on 2022-12-29 | 55.32% | -13.78% | -44.49% |
| C31_010060_OCI_20220812_POLYSILICON_POLICY_SPREAD_FALSE_GREEN | 010060 | policy_spread_false_green_counterexample | 2022-08-12 | 125500 | 135500 on 2022-08-24 | 80000 on 2022-12-29 | 7.97% | -36.25% | -40.96% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- IRA / solar policy attention created valid Stage2 routes.
- 009830 and 322000 show that the market rapidly priced policy optionality.

### Stage3 / Green
- C31 Green should require more than legislation text or theme beta.
- The required bridge is funded subsidy/order/capacity conversion plus margin or revision confirmation.

### 4B
- 322000 is the purest local 4B example: large MFE after policy premium, followed by a heavy post-peak drawdown.
- 009830 had a better company-level route, but still needed local 4B discipline after policy premium expanded.

### 4C
- No hard legal/accounting break is asserted.
- The C31 break mode here is conversion failure: the statute is real, but the company-level EPS/FCF bridge is not yet real enough.

## 6. Raw component score breakdown

```json
{
  "C31_009830_HANWHA_SOLUTIONS_20220812_IRA_SOLAR_POLICY_STAGE2_4B": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 55,
    "valuation_rerating_runway": 8,
    "visibility_quality": 9
  },
  "C31_010060_OCI_20220812_POLYSILICON_POLICY_SPREAD_FALSE_GREEN": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 36,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  },
  "C31_322000_HDHES_20220812_IRA_SOLAR_POLICY_PRICE_ONLY_BLOWOFF": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 32,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C31 guard:
```text
if policy_subsidy_event and no funded_budget_or_company_specific_conversion:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if policy_premium_price_run and no margin_revision_bridge:
    route_to_local_4B_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 322000 / 2022-08-12: policy beta plus large MFE could be misread as Green, but it is better treated as local 4B.
- 010060 / 2022-08-12: polysilicon/policy tailwind without durable company-specific IRA conversion is a Yellow/counterexample row.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -15.46, "MAE_30D_pct": -2.49, "MAE_90D_pct": -7.46, "MFE_180D_pct": 20.86, "MFE_30D_pct": 20.86, "MFE_90D_pct": 20.86, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_009830_HANWHA_SOLUTIONS_20220812_IRA_SOLAR_POLICY_STAGE2_4B", "case_role": "policy_positive_but_4b_required", "company_name": "한화솔루션", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 attention worked, but full Green needs funded manufacturing/subsidy conversion and margin bridge; local 4B needed after policy premium.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.05, "entry_date": "2022-08-12", "entry_price": 46250, "evidence_family": "ira_solar_manufacturing_subsidy_policy_to_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "IRA_SOLAR_POLICY_SUBSIDY_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2023-01-06", "low_price_180d": 39100, "peak_date": "2022-09-15", "peak_price": 55900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009830.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 55, "valuation_rerating_runway": 8, "visibility_quality": 9}, "reuse_reason": null, "same_entry_group_id": "C31_009830_HANWHA_SOLUTIONS_20220812_IRA_SOLAR_POLICY_STAGE2_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["ira_or_legislation_event", "solar_policy_tailwind", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["funded_subsidy_or_budget_conversion_required", "domestic_manufacturing_or_order_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_event_without_company_specific_conversion", "margin_or_revision_fade", "policy_beta_mean_reversion"], "symbol": "009830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv", "trigger_date": "2022-08-12", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -13.78, "MAE_30D_pct": -13.78, "MAE_90D_pct": -13.78, "MFE_180D_pct": 55.32, "MFE_30D_pct": 55.32, "MFE_90D_pct": 55.32, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_322000_HDHES_20220812_IRA_SOLAR_POLICY_PRICE_ONLY_BLOWOFF", "case_role": "policy_event_blowoff_counterexample", "company_name": "HD현대에너지솔루션", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Solar policy beta and price strength should become local 4B, not Green, if subsidy/order conversion is not company-specific.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.49, "entry_date": "2022-08-12", "entry_price": 55500, "evidence_family": "ira_solar_policy_beta_without_funded_order_margin_conversion", "evidence_url_pending": false, "fine_archetype_id": "IRA_SOLAR_POLICY_SUBSIDY_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2022-12-29", "low_price_180d": 47850, "peak_date": "2022-09-15", "peak_price": 86200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/322/322000.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 32, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C31_322000_HDHES_20220812_IRA_SOLAR_POLICY_PRICE_ONLY_BLOWOFF", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["ira_or_legislation_event", "solar_policy_tailwind", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["funded_subsidy_or_budget_conversion_required", "domestic_manufacturing_or_order_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_event_without_company_specific_conversion", "margin_or_revision_fade", "policy_beta_mean_reversion"], "symbol": "322000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322000/2022.csv", "trigger_date": "2022-08-12", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.25, "MAE_30D_pct": -7.17, "MAE_90D_pct": -36.25, "MFE_180D_pct": 7.97, "MFE_30D_pct": 7.97, "MFE_90D_pct": 7.97, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_010060_OCI_20220812_POLYSILICON_POLICY_SPREAD_FALSE_GREEN", "case_role": "policy_spread_false_green_counterexample", "company_name": "OCI", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Policy/spread tailwind without durable domestic subsidy conversion or revision bridge should stay Yellow/Watch.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.96, "entry_date": "2022-08-12", "entry_price": 125500, "evidence_family": "polysilicon_policy_spread_without_durable_ira_conversion", "evidence_url_pending": false, "fine_archetype_id": "IRA_SOLAR_POLICY_SUBSIDY_CONVERSION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2022-12-29", "low_price_180d": 80000, "peak_date": "2022-08-24", "peak_price": 135500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010060.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 5, "total": 36, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C31_010060_OCI_20220812_POLYSILICON_POLICY_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R11", "source_proxy_only": false, "stage2_evidence_fields": ["ira_or_legislation_event", "solar_policy_tailwind", "relative_strength_after_policy_event"], "stage3_evidence_fields": ["funded_subsidy_or_budget_conversion_required", "domestic_manufacturing_or_order_conversion_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_event_without_company_specific_conversion", "margin_or_revision_fade", "policy_beta_mean_reversion"], "symbol": "010060", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010060/2022.csv", "trigger_date": "2022-08-12", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "IRA_SOLAR_POLICY_SUBSIDY_CONVERSION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "loop_contribution_label": "policy_event_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R11",
  "shadow_rule_candidate": "C31 policy/subsidy event rows should cap at Stage2/Yellow unless legislation converts into funded budget, company-specific subsidy/order visibility, margin bridge, or revision confirmation; price-only policy premium should be routed to local 4B.",
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
3. Treat C31 as a conversion guard: legislation alone is Stage2/Yellow until funded budget, company-specific subsidy/order visibility, and margin/revision bridge close.

Candidate rule:
- C31_POLICY_EVENT_REQUIRES_FUNDED_COMPANY_SPECIFIC_CONVERSION
- C31_POLICY_PREMIUM_LOCAL_4B
- C31_SUBSIDY_WITHOUT_MARGIN_REVISION_STAGE2_CAP

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

