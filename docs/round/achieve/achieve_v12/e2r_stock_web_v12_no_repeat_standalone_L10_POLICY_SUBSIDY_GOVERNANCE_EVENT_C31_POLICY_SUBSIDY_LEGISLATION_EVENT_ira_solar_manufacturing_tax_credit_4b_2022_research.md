# E2R V12 No-Repeat Standalone Residual Research
## R12 / L10 / C31 — Policy subsidy legislation event / IRA solar-manufacturing tax-credit 4B guard

metadata:
```text
selected_round: R12
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_SUBSIDY_GOVERNANCE_EVENT
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: IRA_SOLAR_MANUFACTURING_TAX_CREDIT_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|policy_to_company_eligibility_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_SUBSIDY_GOVERNANCE_EVENT_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_ira_solar_manufacturing_tax_credit_4b_2022_research.md
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

This run avoids those top-covered C31 symbols and adds 009830, 322000, and 011930.  
Each row uses a new `C31 + symbol + trigger_type + entry_date` hard key:
```text
C31 + 009830 + Stage2-Actionable + 2022-07-28
C31 + 322000 + 4B-local-price-only + 2022-09-15
C31 + 011930 + Stage3-Yellow + 2022-08-11
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
009830 한화솔루션: selected post-2008 forward window clean; profile corporate-action candidates are 1999-04-20 and 2008-07-04, outside selected trigger window.
322000 HD현대에너지솔루션: corporate_action_candidate_count=0; clean 2022 forward window.
011930 신성이엔지: selected post-2017 forward window clean; profile corporate-action candidates are historical/latest 2017-01-02, outside selected trigger window.
```

## 3. Research thesis

C31 should distinguish policy legislation that converts into company-level earnings from broad policy beta:

```text
policy / subsidy / legislation event
→ direct company eligibility
→ capacity or project execution
→ customer demand or order bridge
→ input-cost / ASP bridge
→ gross margin and revision confirmation
→ Stage2/Green or local 4B cap
```

A subsidy law is a wind at the back. Stage2 can buy when the company has a sail—eligible capacity, customers and margin revision. Green should not buy every flag waving in the wind after the market has already priced the law.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C31_009830_HANWHASOLUTIONS_20220728_IRA_SOLAR_MANUFACTURING_STAGE2 | 009830 | positive_IRA_solar_manufacturing_tax_credit_stage2_success_with_later_4b_refresh | 2022-07-28 | 42250 | 57000 on 2023-03-31 | 39100 on 2023-01-06 | 30.18% | 32.31% | 34.91% | -7.46% | -21.93% |
| C31_322000_HDHES_20220915_IRA_SOLAR_POLICY_PRICE_PREMIUM_4B | 322000 | solar_module_policy_subsidy_price_premium_counterexample | 2022-09-15 | 84500 | 86200 on 2022-09-15 | 47850 on 2022-12-29 | 2.01% | 2.01% | 2.01% | -43.37% | -44.49% |
| C31_011930_SHINSUNGENG_20220811_SOLAR_CLEANROOM_POLICY_FALSE_GREEN | 011930 | solar_cleanroom_policy_beta_false_green_counterexample | 2022-08-11 | 2515 | 2735 on 2022-08-26 | 1545 on 2022-12-29 | 8.75% | 8.75% | 8.75% | -38.57% | -43.51% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 009830 is the positive anchor. The IRA solar-manufacturing route produced strong 30D/90D/180D MFE before the later policy premium needed 4B refresh discipline.
- Stage2 is allowed only when policy salience maps to direct company eligibility, manufacturing/project capacity, customer demand, input-cost/ASP bridge and margin/revision visibility.

### Stage3 / Green
- C31 Green should require direct eligibility, capacity execution, customer/order bridge, input-cost/ASP pass-through and margin/revision confirmation.
- 011930 is the false-Green/Yellow guard: solar/cleanroom policy beta was visible, but the company-level policy-to-margin bridge did not refresh enough to survive the forward path.

### 4B
- 322000 fills the solar-policy price-premium 4B pocket. The September 2022 trigger had almost no residual upside and a much larger drawdown.
- 011930 shows the same failure in policy beta form: policy/legislation excitement can be real while the listed company lacks direct eligibility and margin proof.
- 009830 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the subsidy law.

### 4C
- No hard subsidy denial, project cancellation, customer loss, financing break or accounting break is asserted.
- The C31 break mode here is policy-to-company bridge exhaustion: the legislation can remain directionally real, but incremental eligibility, capacity, customer demand and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C31_009830_HANWHASOLUTIONS_20220728_IRA_SOLAR_MANUFACTURING_STAGE2": {
    "capacity_or_project_execution": 8,
    "customer_demand_or_order_bridge": 7,
    "direct_company_policy_eligibility": 9,
    "information_confidence": 4,
    "input_cost_ASP_margin_bridge": 8,
    "market_mispricing": 9,
    "policy_subsidy_legislation_salience": 11,
    "revision_visibility": 7,
    "total": 71,
    "valuation_rerating_runway": 8
  },
  "C31_011930_SHINSUNGENG_20220811_SOLAR_CLEANROOM_POLICY_FALSE_GREEN": {
    "capacity_or_project_execution": 3,
    "customer_demand_or_order_bridge": 2,
    "direct_company_policy_eligibility": 3,
    "information_confidence": 3,
    "input_cost_ASP_margin_bridge": 2,
    "market_mispricing": 4,
    "policy_subsidy_legislation_salience": 8,
    "revision_visibility": 2,
    "total": 28,
    "valuation_rerating_runway": 1
  },
  "C31_322000_HDHES_20220915_IRA_SOLAR_POLICY_PRICE_PREMIUM_4B": {
    "capacity_or_project_execution": 3,
    "customer_demand_or_order_bridge": 3,
    "direct_company_policy_eligibility": 4,
    "information_confidence": 3,
    "input_cost_ASP_margin_bridge": 2,
    "market_mispricing": 4,
    "policy_subsidy_legislation_salience": 9,
    "revision_visibility": 2,
    "total": 31,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C31 guard:
```text
if policy_subsidy_legislation and direct_eligibility_capacity_customer_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if policy_subsidy_price_premium and no incremental_eligibility_capacity_customer_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and policy_to_company_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 322000 / 2022-09-15: solar-policy premium can be over-promoted if price strength substitutes for direct eligibility, capacity execution and margin proof.
- 011930 / 2022-08-11: solar/cleanroom policy beta can look like Yellow-to-Green, but fails without renewed customer demand, eligibility and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -7.46, "MAE_30D_pct": -1.18, "MAE_90D_pct": -2.13, "MFE_180D_pct": 34.91, "MFE_30D_pct": 30.18, "MFE_90D_pct": 32.31, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_009830_HANWHASOLUTIONS_20220728_IRA_SOLAR_MANUFACTURING_STAGE2", "case_role": "positive_IRA_solar_manufacturing_tax_credit_stage2_success_with_later_4b_refresh", "company_name": "한화솔루션", "corporate_action_window_status": "selected post-2008 forward window clean; profile corporate-action candidates are 1999-04-20 and 2008-07-04, outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when IRA solar-manufacturing subsidy evidence mapped to an actual solar-module platform, US manufacturing exposure, capacity expansion route, downstream demand and margin/revision optionality before the rerating was fully capitalized. Green still requires domestic-content/AMPC-like benefit visibility, customer demand, capex execution, polysilicon/input-cost bridge and margin/revision confirmation; after the policy premium is priced, the same evidence requires local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -21.93, "entry_date": "2022-07-28", "entry_price": 42250, "evidence_family": "IRA_solar_manufacturing_tax_credit_US_module_capacity_policy_to_margin_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "IRA_SOLAR_MANUFACTURING_TAX_CREDIT_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_SUBSIDY_GOVERNANCE_EVENT", "low_date_180d": "2023-01-06", "low_price_180d": 39100, "peak_date": "2023-03-31", "peak_price": 57000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009830.json", "raw_component_score_breakdown": {"capacity_or_project_execution": 8, "customer_demand_or_order_bridge": 7, "direct_company_policy_eligibility": 9, "information_confidence": 4, "input_cost_ASP_margin_bridge": 8, "market_mispricing": 9, "policy_subsidy_legislation_salience": 11, "revision_visibility": 7, "total": 71, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C31_009830_HANWHASOLUTIONS_20220728_IRA_SOLAR_MANUFACTURING_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R12", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_legislation_salience", "direct_company_policy_eligibility", "capacity_customer_margin_revision_route"], "stage3_evidence_fields": ["direct_eligibility_required", "capacity_execution_or_customer_demand_required", "input_cost_ASP_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_subsidy_price_premium", "policy_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_eligibility_gap", "capacity_or_customer_demand_gap", "margin_revision_bridge_failure"], "symbol": "009830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv", "trigger_date": "2022-07-28", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -43.37, "MAE_30D_pct": -32.78, "MAE_90D_pct": -43.37, "MFE_180D_pct": 2.01, "MFE_30D_pct": 2.01, "MFE_90D_pct": 2.01, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_322000_HDHES_20220915_IRA_SOLAR_POLICY_PRICE_PREMIUM_4B", "case_role": "solar_module_policy_subsidy_price_premium_counterexample", "company_name": "HD현대에너지솔루션", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2022 forward window", "current_profile_error": true, "current_profile_verdict": "Solar policy subsidy price premium should route to local 4B or counterexample when the market has already capitalized IRA/manufacturing-policy optionality and incremental direct eligibility, capacity expansion, customer demand, input-cost pass-through and margin/revision evidence do not keep expanding. The September 2022 trigger had almost no residual runway and a large forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.49, "entry_date": "2022-09-15", "entry_price": 84500, "evidence_family": "IRA_solar_policy_price_premium_without_incremental_capacity_customer_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "IRA_SOLAR_MANUFACTURING_TAX_CREDIT_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_SUBSIDY_GOVERNANCE_EVENT", "low_date_180d": "2022-12-29", "low_price_180d": 47850, "peak_date": "2022-09-15", "peak_price": 86200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/322/322000.json", "raw_component_score_breakdown": {"capacity_or_project_execution": 3, "customer_demand_or_order_bridge": 3, "direct_company_policy_eligibility": 4, "information_confidence": 3, "input_cost_ASP_margin_bridge": 2, "market_mispricing": 4, "policy_subsidy_legislation_salience": 9, "revision_visibility": 2, "total": 31, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C31_322000_HDHES_20220915_IRA_SOLAR_POLICY_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R12", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_legislation_salience", "direct_company_policy_eligibility", "capacity_customer_margin_revision_route"], "stage3_evidence_fields": ["direct_eligibility_required", "capacity_execution_or_customer_demand_required", "input_cost_ASP_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_subsidy_price_premium", "policy_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_eligibility_gap", "capacity_or_customer_demand_gap", "margin_revision_bridge_failure"], "symbol": "322000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322000/2022.csv", "trigger_date": "2022-09-15", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.57, "MAE_30D_pct": -11.73, "MAE_90D_pct": -28.83, "MFE_180D_pct": 8.75, "MFE_30D_pct": 8.75, "MFE_90D_pct": 8.75, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_011930_SHINSUNGENG_20220811_SOLAR_CLEANROOM_POLICY_FALSE_GREEN", "case_role": "solar_cleanroom_policy_beta_false_green_counterexample", "company_name": "신성이엔지", "corporate_action_window_status": "selected post-2017 forward window clean; profile corporate-action candidates are historical/latest 2017-01-02 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Solar/cleanroom policy beta should remain Yellow or local 4B when the policy event is not mapped to direct subsidy eligibility, named customer demand, capacity execution, cost pass-through and margin/revision evidence. The August 2022 spike had modest local upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.51, "entry_date": "2022-08-11", "entry_price": 2515, "evidence_family": "solar_cleanroom_policy_beta_without_direct_subsidy_eligibility_customer_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "IRA_SOLAR_MANUFACTURING_TAX_CREDIT_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_SUBSIDY_GOVERNANCE_EVENT", "low_date_180d": "2022-12-29", "low_price_180d": 1545, "peak_date": "2022-08-26", "peak_price": 2735, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011930.json", "raw_component_score_breakdown": {"capacity_or_project_execution": 3, "customer_demand_or_order_bridge": 2, "direct_company_policy_eligibility": 3, "information_confidence": 3, "input_cost_ASP_margin_bridge": 2, "market_mispricing": 4, "policy_subsidy_legislation_salience": 8, "revision_visibility": 2, "total": 28, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C31_011930_SHINSUNGENG_20220811_SOLAR_CLEANROOM_POLICY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R12", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_legislation_salience", "direct_company_policy_eligibility", "capacity_customer_margin_revision_route"], "stage3_evidence_fields": ["direct_eligibility_required", "capacity_execution_or_customer_demand_required", "input_cost_ASP_margin_revision_bridge_required"], "stage4b_evidence_fields": ["policy_subsidy_price_premium", "policy_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_eligibility_gap", "capacity_or_customer_demand_gap", "margin_revision_bridge_failure"], "symbol": "011930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011930/2022.csv", "trigger_date": "2022-08-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "IRA_SOLAR_MANUFACTURING_TAX_CREDIT_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_SUBSIDY_GOVERNANCE_EVENT",
  "loop_contribution_label": "policy_subsidy_legislation_IRA_solar_manufacturing_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R12",
  "shadow_rule_candidate": "C31 policy/subsidy rows should allow Stage2 only when legislation maps to direct company eligibility, capacity/project execution, customer demand, input-cost/ASP bridge and margin revisions; policy beta price premiums should route to Yellow/local 4B when the policy-to-company earnings bridge has not refreshed.",
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
3. Add C31-specific policy/subsidy / direct eligibility / capacity execution / customer-demand / input-cost-ASP / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C31_STAGE2_ALLOWED_ON_DIRECT_ELIGIBILITY_CAPACITY_CUSTOMER_MARGIN_REVISION_BRIDGE
- C31_GREEN_REQUIRES_POLICY_TO_COMPANY_EARNINGS_CONVERSION
- C31_POLICY_SUBSIDY_PRICE_PREMIUM_LOCAL_4B
- C31_PRICE_CONFIRMATION_WITHOUT_POLICY_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R12/L10_POLICY_SUBSIDY_GOVERNANCE_EVENT/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

