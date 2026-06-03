# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C13 — Battery JV utilization / AMPC / IRA guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: IRA_AMPC_JV_UTILIZATION_MARGIN_REVISION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_4C_guard_validation|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_ira_ampc_utilization_2022_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA current coverage:
rows=16, symbols=3, date range=2022-05-25~2025-04-08, good/bad S2=2/9, 4B/4C=1/0
top covered symbols: 006400(7), 373220(7), 096770(2)
```

C13 has a narrow listed-symbol universe. This run therefore accepts same-symbol soft reuse only where the trigger family, entry date, Stage transition and failure mode differ from existing rows.  
Each row uses a new `C13 + symbol + trigger_type + entry_date` hard key.

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
373220 LG에너지솔루션: corporate_action_candidate_count=0.
006400 삼성SDI: 2023 forward window clean; corporate-action candidates are old, outside the selected test window.
096770 SK이노베이션: 2023/2024 forward window clean; corporate-action candidate is 2024-11-20, outside the selected forward window.
```

## 3. Research thesis

C13 should not treat IRA, AMPC, or JV capacity as direct earnings. It should test whether policy and capacity become usable, credit-earning production:

```text
IRA / AMPC / JV capacity attention
→ qualified production volume
→ utilization and customer call-off
→ AMPC accounting and cash realization
→ margin and revision bridge
→ rerating
```

The policy credit is like a coupon book. It only has value when the factory produces qualified cells, customers call them off, and the accounting bridge turns coupons into margin. A plant announcement without utilization is still an empty kitchen.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C13_373220_LGES_20220816_IRA_AMPC_JV_CAPACITY_STAGE2 | 373220 | positive_ira_ampc_capacity_stage2_success_with_later_4b | 2022-08-16 | 460500 | 629000 on 2022-11-11 | 415000 on 2022-10-04 | 12.05% | 36.59% | 36.59% | -9.88% | -33.07% |
| C13_006400_SAMSUNGSDI_20230411_AMPC_JV_UTILIZATION_FALSE_GREEN | 006400 | jv_capacity_ampc_false_green_counterexample | 2023-04-11 | 767000 | 779000 on 2023-04-12 | 417000 on 2023-11-13 | 1.56% | 1.56% | 1.56% | -45.63% | -46.47% |
| C13_096770_SKINNOV_20230726_AMPC_JV_UTILIZATION_PRICE_PREMIUM_4B | 096770 | ampc_jv_utilization_4b_counterexample | 2023-07-26 | 204500 | 229500 on 2023-07-26 | 108300 on 2024-01-22 | 12.22% | 12.22% | 12.22% | -47.04% | -52.81% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- IRA/AMPC attention and US JV capacity visibility can be valid Stage2 research routes.
- 373220 on 2022-08-16 is the positive anchor: policy and capacity optionality produced a clear forward MFE before the later policy-capacity premium needed 4B discipline.

### Stage3 / Green
- C13 Green should require qualified production volume, utilization, customer call-off, AMPC accounting, margin capture and revision evidence.
- 006400 on 2023-04-11 is the false-Green guard: policy/JV/capacity attention did not protect the stock once utilization and revision evidence failed to carry the valuation.

### 4B
- 096770 on 2023-07-26 is the late premium row. The market capitalized AMPC/JV optionality quickly, but the later path shows that loss reduction, utilization, capex burden, and revision bridge were not enough.
- A real policy subsidy can still become a bad late entry if the model fails to distinguish installed capacity from utilized qualified production.

### 4C
- No hard accounting break is asserted.
- The C13 break mode is utilization and accounting conversion failure: the policy remains real, but the stock does not receive enough qualified production, call-off, margin, or revision evidence to carry the premium.

## 6. Raw component score breakdown

```json
{
  "C13_006400_SAMSUNGSDI_20230411_AMPC_JV_UTILIZATION_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 32,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  },
  "C13_096770_SKINNOV_20230726_AMPC_JV_UTILIZATION_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C13_373220_LGES_20220816_IRA_AMPC_JV_CAPACITY_STAGE2": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 3,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 59,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C13 guard:
```text
if IRA_AMPC_JV_attention and early_capacity_visibility:
    allow_stage2_actionable = true

if AMPC_JV_capacity_price_premium and no qualified_production_utilization_calloff_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if utilization_shortfall_or_AMPC_accounting_uncertainty:
    cap_stage = Stage3-Yellow
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 006400 / 2023-04-11: JV/AMPC policy attention can be over-promoted if the model does not require qualified production volume and utilization evidence.
- 096770 / 2023-07-26: AMPC/JV optionality can become price-only when battery loss reduction, utilization and revision bridge do not close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -9.88, "MAE_30D_pct": -7.27, "MAE_90D_pct": -9.88, "MFE_180D_pct": 36.59, "MFE_30D_pct": 12.05, "MFE_90D_pct": 36.59, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_373220_LGES_20220816_IRA_AMPC_JV_CAPACITY_STAGE2", "case_role": "positive_ira_ampc_capacity_stage2_success_with_later_4b", "company_name": "LG에너지솔루션", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when IRA/AMPC policy and US JV capacity visibility created a credible cell-maker margin route, but Green still requires utilization, qualified production volume, customer call-off, AMPC accounting and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -33.07, "entry_date": "2022-08-16", "entry_price": 460500, "evidence_family": "ira_ampc_us_jv_capacity_customer_utilization_visibility_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2022-10-04", "low_price_180d": 415000, "peak_date": "2022-11-11", "peak_price": 629000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/373/373220.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 3, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 10, "total": 59, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C13_373220_LGES_20220816_IRA_AMPC_JV_CAPACITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["IRA_AMPC_policy_attention", "battery_JV_capacity_or_qualified_production_visibility", "customer_calloff_or_utilization_claim"], "stage3_evidence_fields": ["qualified_production_volume_required", "utilization_customer_calloff_required", "AMPC_accounting_margin_revision_bridge_required"], "stage4b_evidence_fields": ["AMPC_JV_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["utilization_shortfall", "AMPC_or_tax_credit_accounting_disappointment", "margin_loss_or_revision_bridge_failure"], "symbol": "373220", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv", "trigger_date": "2022-08-16", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.63, "MAE_30D_pct": -13.56, "MAE_90D_pct": -14.86, "MFE_180D_pct": 1.56, "MFE_30D_pct": 1.56, "MFE_90D_pct": 1.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_006400_SAMSUNGSDI_20230411_AMPC_JV_UTILIZATION_FALSE_GREEN", "case_role": "jv_capacity_ampc_false_green_counterexample", "company_name": "삼성SDI", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or outside selected test window", "current_profile_error": true, "current_profile_verdict": "JV/AMPC policy attention should stay Yellow if utilization, qualified production volume, margin capture and revision duration do not support the valuation already paid.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.47, "entry_date": "2023-04-11", "entry_price": 767000, "evidence_family": "battery_jv_ampc_policy_attention_without_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-13", "low_price_180d": 417000, "peak_date": "2023-04-12", "peak_price": 779000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006400.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 32, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C13_006400_SAMSUNGSDI_20230411_AMPC_JV_UTILIZATION_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["IRA_AMPC_policy_attention", "battery_JV_capacity_or_qualified_production_visibility", "customer_calloff_or_utilization_claim"], "stage3_evidence_fields": ["qualified_production_volume_required", "utilization_customer_calloff_required", "AMPC_accounting_margin_revision_bridge_required"], "stage4b_evidence_fields": ["AMPC_JV_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["utilization_shortfall", "AMPC_or_tax_credit_accounting_disappointment", "margin_loss_or_revision_bridge_failure"], "symbol": "006400", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv", "trigger_date": "2023-04-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -47.04, "MAE_30D_pct": -17.31, "MAE_90D_pct": -41.27, "MFE_180D_pct": 12.22, "MFE_30D_pct": 12.22, "MFE_90D_pct": 12.22, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_096770_SKINNOV_20230726_AMPC_JV_UTILIZATION_PRICE_PREMIUM_4B", "case_role": "ampc_jv_utilization_4b_counterexample", "company_name": "SK이노베이션", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late AMPC/JV price premium should route to local 4B or counterexample unless cell utilization, loss reduction, capex burden, customer call-off and revision bridge improve.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.81, "entry_date": "2023-07-26", "entry_price": 204500, "evidence_family": "battery_jv_ampc_price_premium_without_utilization_loss_margin_repair", "evidence_url_pending": false, "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_MARGIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-01-22", "low_price_180d": 108300, "peak_date": "2023-07-26", "peak_price": 229500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/096/096770.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C13_096770_SKINNOV_20230726_AMPC_JV_UTILIZATION_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["IRA_AMPC_policy_attention", "battery_JV_capacity_or_qualified_production_visibility", "customer_calloff_or_utilization_claim"], "stage3_evidence_fields": ["qualified_production_volume_required", "utilization_customer_calloff_required", "AMPC_accounting_margin_revision_bridge_required"], "stage4b_evidence_fields": ["AMPC_JV_capacity_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["utilization_shortfall", "AMPC_or_tax_credit_accounting_disappointment", "margin_loss_or_revision_bridge_failure"], "symbol": "096770", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_MARGIN_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "battery_jv_ampc_ira_utilization_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C13 battery JV/AMPC/IRA rows should allow Stage2 on early policy/JV/capacity visibility, but Stage3 Green requires qualified production volume, utilization, customer call-off, AMPC accounting, margin and revision bridge; late policy-capacity price premium should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C13 + symbol + trigger_type + entry_date.
3. Because C13 has a narrow listed-symbol universe, accept same-symbol soft reuse only when date, trigger family, Stage transition or failure mode differs.
4. Add C13-specific IRA/AMPC/JV utilization/accounting-margin guard only as a shadow candidate until more rows exist.

Candidate rule:
- C13_STAGE2_ALLOWED_ON_EARLY_IRA_AMPC_JV_CAPACITY_VISIBILITY
- C13_GREEN_REQUIRES_QUALIFIED_PRODUCTION_UTILIZATION_CALLOFF_MARGIN_REVISION
- C13_AMPC_JV_POLICY_PREMIUM_LOCAL_4B
- C13_UTILIZATION_ACCOUNTING_OR_LOSS_REDUCTION_GAP_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.

