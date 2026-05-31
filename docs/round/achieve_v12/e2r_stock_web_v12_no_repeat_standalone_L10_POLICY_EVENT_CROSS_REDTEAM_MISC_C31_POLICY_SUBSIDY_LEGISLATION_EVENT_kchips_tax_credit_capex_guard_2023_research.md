# E2R V12 No-Repeat Standalone Residual Research
## R13 / L10 / C31 — Policy subsidy / legislation K-Chips tax-credit guard

metadata:
```text
selected_round: R13
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KCHIPS_TAX_CREDIT_CAPEX_ELIGIBILITY_REVISION_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_kchips_tax_credit_capex_guard_2023_research.md
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

This run avoids those top-covered C31 symbols and adds 000660, 000990, and 108320.  
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
000660 SK하이닉스: 2023 forward window clean; corporate-action candidates are old and outside the selected test window.
000990 DB하이텍: 2023 forward window clean; corporate-action candidates are old and outside the selected test window.
108320 LX세미콘: 2023 forward window clean; corporate-action candidates are 2010 and outside the selected test window.
```

## 3. Research thesis

C31 should not treat a subsidy or tax-credit headline as earnings. It should test whether legislation becomes eligible capex and revision:

```text
policy subsidy / legislation attention
→ direct eligibility
→ capex timing or investment schedule
→ customer demand and utilization
→ margin and revision bridge
→ rerating
```

Policy is the permit, not the plant. Stage2 can follow the permit early, but Green should require a machine, a customer, and an income-statement bridge.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C31_000660_SKHYNIX_20230330_KCHIPS_TAX_CREDIT_HBM_CAPEX_STAGE2 | 000660 | positive_kchips_tax_credit_capex_stage2_success | 2023-03-30 | 88800 | 143700 on 2023-12-22 | 82700 on 2023-04-06 | 4.17% | 36.37% | 61.82% | -6.87% | -3.13% |
| C31_000990_DBHITEK_20230330_KCHIPS_LEGACY_FOUNDRY_FALSE_GREEN | 000990 | legacy_foundry_tax_credit_false_green_counterexample | 2023-03-30 | 61100 | 83600 on 2023-04-04 | 47500 on 2023-09-27 | 36.82% | 36.82% | 36.82% | -22.26% | -43.18% |
| C31_108320_LXSEMICON_20230330_KCHIPS_FABLESS_DISPLAY_FALSE_GREEN | 108320 | fabless_display_policy_beta_false_green_counterexample | 2023-03-30 | 110700 | 126900 on 2023-07-05 | 71200 on 2023-11-01 | 7.5% | 11.02% | 14.63% | -35.68% | -43.89% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Policy subsidy and tax-credit legislation can be a valid Stage2 route only when the company has direct eligibility and an earnings bridge.
- 000660 is the positive anchor. K-Chips tax-credit legislation mattered because it later connected to memory/HBM capex, customer mix and revision evidence. The policy headline alone was not the full signal.

### Stage3 / Green
- C31 Green should require direct eligibility, capex timing, customer demand, utilization, margin and revision confirmation.
- 000990 and 108320 show why broad semiconductor policy beta should stay Yellow when the earnings path is indirect, already priced, or not supported by utilization and revisions.

### 4B
- DB하이텍 had a sharp policy-adjacent spike around the trigger, then a long drawdown. The model should treat this as policy premium needing incremental non-price confirmation.
- LX세미콘 had enough theme strength to trade, but not enough direct capex/tax-credit earnings bridge to remain Green.

### 4C
- No hard legal repeal or subsidy removal is asserted.
- The C31 break mode here is policy-to-earnings conversion failure: the legislation is real, but direct eligibility, capex execution, demand, utilization, margin and revision do not carry the price.

## 6. Raw component score breakdown

```json
{
  "C31_000660_SKHYNIX_20230330_KCHIPS_TAX_CREDIT_HBM_CAPEX_STAGE2": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 4,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 58,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  },
  "C31_000990_DBHITEK_20230330_KCHIPS_LEGACY_FOUNDRY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 3,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 28,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C31_108320_LXSEMICON_20230330_KCHIPS_FABLESS_DISPLAY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C31 guard:
```text
if policy_subsidy_legislation and direct_capex_eligibility and revision_bridge_visible:
    allow_stage2_actionable = true

if policy_beta_price_premium and no direct_eligibility_customer_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and policy_to_earnings_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 000990 / 2023-03-30: legacy foundry policy beta can be over-promoted if the model treats tax-credit attention as utilization and margin proof.
- 108320 / 2023-03-30: fabless/display semiconductor beta can look like policy Green, but the later path argues for Yellow/counterexample unless direct eligible capex and revision bridge are visible.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -6.87, "MAE_30D_pct": -6.87, "MAE_90D_pct": -6.87, "MFE_180D_pct": 61.82, "MFE_30D_pct": 4.17, "MFE_90D_pct": 36.37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_000660_SKHYNIX_20230330_KCHIPS_TAX_CREDIT_HBM_CAPEX_STAGE2", "case_role": "positive_kchips_tax_credit_capex_stage2_success", "company_name": "SK하이닉스", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when K-Chips tax-credit legislation met real memory/HBM capex and revision optionality. Policy did not carry the stock alone; customer mix, HBM capacity, capex timing and earnings revisions had to become visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -3.13, "entry_date": "2023-03-30", "entry_price": 88800, "evidence_family": "kchips_tax_credit_hbm_capex_memory_policy_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "KCHIPS_TAX_CREDIT_CAPEX_ELIGIBILITY_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2023-04-06", "low_price_180d": 82700, "peak_date": "2023-12-22", "peak_price": 143700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 4, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 58, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C31_000660_SKHYNIX_20230330_KCHIPS_TAX_CREDIT_HBM_CAPEX_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_or_tax_credit_legislation_attention", "direct_capex_eligibility_or_investment_schedule", "customer_demand_margin_revision_bridge"], "stage3_evidence_fields": ["direct_eligibility_confirmation_required", "capex_timing_and_customer_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_subsidy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_earnings_conversion_gap", "demand_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "000660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv", "trigger_date": "2023-03-30", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -22.26, "MAE_30D_pct": -1.31, "MAE_90D_pct": -1.31, "MFE_180D_pct": 36.82, "MFE_30D_pct": 36.82, "MFE_90D_pct": 36.82, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_000990_DBHITEK_20230330_KCHIPS_LEGACY_FOUNDRY_FALSE_GREEN", "case_role": "legacy_foundry_tax_credit_false_green_counterexample", "company_name": "DB하이텍", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Legacy foundry tax-credit attention should stay Yellow when customer demand, utilization, capex eligibility, margin and revision evidence do not keep expanding after the policy spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.18, "entry_date": "2023-03-30", "entry_price": 61100, "evidence_family": "kchips_tax_credit_legacy_foundry_price_spike_without_capacity_customer_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "KCHIPS_TAX_CREDIT_CAPEX_ELIGIBILITY_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2023-09-27", "low_price_180d": 47500, "peak_date": "2023-04-04", "peak_price": 83600, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/000/000990.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 3, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 28, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C31_000990_DBHITEK_20230330_KCHIPS_LEGACY_FOUNDRY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_or_tax_credit_legislation_attention", "direct_capex_eligibility_or_investment_schedule", "customer_demand_margin_revision_bridge"], "stage3_evidence_fields": ["direct_eligibility_confirmation_required", "capex_timing_and_customer_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_subsidy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_earnings_conversion_gap", "demand_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "000990", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv", "trigger_date": "2023-03-30", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -35.68, "MAE_30D_pct": -11.11, "MAE_90D_pct": -11.11, "MFE_180D_pct": 14.63, "MFE_30D_pct": 7.5, "MFE_90D_pct": 11.02, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_108320_LXSEMICON_20230330_KCHIPS_FABLESS_DISPLAY_FALSE_GREEN", "case_role": "fabless_display_policy_beta_false_green_counterexample", "company_name": "LX세미콘", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Fabless/display semiconductor names should not become Green on K-Chips tax-credit beta unless the firm has direct eligible capex, customer demand, pricing/mix, margin and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.89, "entry_date": "2023-03-30", "entry_price": 110700, "evidence_family": "kchips_tax_credit_display_fabless_policy_beta_without_capex_eligibility_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "KCHIPS_TAX_CREDIT_CAPEX_ELIGIBILITY_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "low_date_180d": "2023-11-01", "low_price_180d": 71200, "peak_date": "2023-07-05", "peak_price": 126900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/108/108320.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C31_108320_LXSEMICON_20230330_KCHIPS_FABLESS_DISPLAY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R13", "source_proxy_only": false, "stage2_evidence_fields": ["policy_subsidy_or_tax_credit_legislation_attention", "direct_capex_eligibility_or_investment_schedule", "customer_demand_margin_revision_bridge"], "stage3_evidence_fields": ["direct_eligibility_confirmation_required", "capex_timing_and_customer_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["policy_subsidy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_earnings_conversion_gap", "demand_or_utilization_disappointment", "margin_revision_bridge_failure"], "symbol": "108320", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/108/108320/2023.csv", "trigger_date": "2023-03-30", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "KCHIPS_TAX_CREDIT_CAPEX_ELIGIBILITY_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "loop_contribution_label": "policy_subsidy_legislation_kchips_semiconductor_capex_eligibility_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R13",
  "shadow_rule_candidate": "C31 policy-subsidy/legislation rows should allow Stage2 when legislation directly maps to eligible capex, customer demand, margin and revision evidence; policy beta without direct capex eligibility or earnings bridge should stay Yellow/local 4B or counterexample.",
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
3. Add C31-specific policy-subsidy / direct-eligibility / capex-to-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C31_STAGE2_ALLOWED_ON_POLICY_WITH_DIRECT_ELIGIBILITY_AND_REVISION_BRIDGE
- C31_GREEN_REQUIRES_CAPEX_TIMING_CUSTOMER_DEMAND_MARGIN_REVISION
- C31_POLICY_BETA_PRICE_PREMIUM_LOCAL_4B
- C31_POLICY_WITHOUT_DIRECT_EARNINGS_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R13/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

