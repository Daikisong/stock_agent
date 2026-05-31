# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy supply / lithium bankability guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_RESOURCE_SUPPLY_POLICY_BANKABILITY_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_lithium_resource_supply_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY current coverage:
rows=7, symbols=4, date range=2019-05-20~2023-10-23, good/bad S2=2/0, 4B/4C=0/0
top covered symbols: 005290(2), 027580(2), 047400(2), 093370(1)
```

This run avoids those top-covered C16 symbols and adds 005490, 001570, and 005420.  
Each row uses a new `C16 + symbol + trigger_type + entry_date` hard key.

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
005490 POSCO홀딩스: corporate_action_candidate_count=0.
001570 금양: 2023 forward window clean; corporate-action candidates are old, outside the test window.
005420 코스모화학: 2023 forward window clean; corporate-action candidate is 2019-12-24, outside the test window.
```

## 3. Research thesis

C16 is not a generic “resource theme” bucket. It should test whether policy/resource attention becomes bankable supply:

```text
strategic resource policy / supply-security attention
→ resource control or recycling route
→ capex, processing capacity, and production schedule
→ offtake or customer conversion
→ margin and revision bridge
→ rerating
```

The guard is bankability. A resource story can glow like ore in a headlamp, but until it has rights, capex, processing, offtake, and cash-flow conversion, it is still only a map—not a mine.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C16_005490_POSCOHOLDINGS_20230413_LITHIUM_RESOURCE_STAGE2_SUCCESS_WITH_4B | 005490 | positive_resource_supply_stage2_success_with_later_4b | 2023-04-13 | 391500 | 764000 on 2023-07-26 | 356000 on 2023-05-15 | 11.37% | 95.15% | 95.15% | -9.07% | -47.71% |
| C16_001570_GEUMYANG_20230711_LITHIUM_RESOURCE_OPTIONALITY_FALSE_GREEN | 001570 | resource_optionality_false_green_counterexample | 2023-07-11 | 105900 | 194000 on 2023-07-26 | 83000 on 2023-10-27 | 83.19% | 83.19% | 83.19% | -21.62% | -57.22% |
| C16_005420_COSMOCHEM_20230403_RECYCLING_RESOURCE_PRICE_PREMIUM_FALSE_GREEN | 005420 | recycling_resource_premium_counterexample | 2023-04-03 | 64800 | 94600 on 2023-04-10 | 31250 on 2023-10-31 | 45.99% | 45.99% | 45.99% | -51.77% | -66.97% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Strategic resource policy attention and supply-chain security premiums are valid routing signals.
- 005490 is the positive anchor: the lithium/resource route had enough real asset and integrated supply-chain credibility to justify Stage2 attention before the late-July blowoff.

### Stage3 / Green
- C16 Green should require bankable resource control, production or processing capacity, offtake visibility, and margin/revision bridge.
- 001570 and 005420 show why resource optionality should not be promoted simply because the price path confirmed theme heat.

### 4B
- 005490 still required local 4B discipline after the resource/lithium story was heavily capitalized.
- 001570 and 005420 are sharper 4B/counterexample rows: the market paid for strategic supply before the resource-to-cash-flow bridge became hard enough.

### 4C
- No hard accounting break is asserted.
- The C16 break mode is bankability failure: the story may remain strategically plausible, but the equity rerating fails when financing, capex, offtake, margin or revision evidence does not arrive.

## 6. Raw component score breakdown

```json
{
  "C16_001570_GEUMYANG_20230711_LITHIUM_RESOURCE_OPTIONALITY_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 4
  },
  "C16_005420_COSMOCHEM_20230403_RECYCLING_RESOURCE_PRICE_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 30,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C16_005490_POSCOHOLDINGS_20230413_LITHIUM_RESOURCE_STAGE2_SUCCESS_WITH_4B": {
    "bottleneck_pricing_power": 12,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 60,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_attention and no bankable_resource_production_offtake_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if resource_policy_price_premium and no incremental_non_price_bankability_evidence:
    route_to_local_4B_watch = true

if post_peak_drawdown and cashflow_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 001570 / 2023-07-11: lithium/resource optionality can be over-promoted if the model does not demand bankable resource, offtake and cash-flow evidence.
- 005420 / 2023-04-03: recycling/resource premium can look like Green, but the later path argues for Yellow/4B/counterexample treatment when margin and revision duration are missing.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -9.07, "MAE_30D_pct": -9.07, "MAE_90D_pct": -9.07, "MFE_180D_pct": 95.15, "MFE_30D_pct": 11.37, "MFE_90D_pct": 95.15, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_005490_POSCOHOLDINGS_20230413_LITHIUM_RESOURCE_STAGE2_SUCCESS_WITH_4B", "case_role": "positive_resource_supply_stage2_success_with_later_4b", "company_name": "POSCO홀딩스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful because lithium/resource supply optionality had real asset and integrated supply-chain routes; later local 4B was still required after valuation capitalized the story.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.71, "entry_date": "2023-04-13", "entry_price": 391500, "evidence_family": "lithium_resource_policy_integrated_supply_route_with_real_asset_visibility", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_SUPPLY_POLICY_BANKABILITY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-05-15", "low_price_180d": 356000, "peak_date": "2023-07-26", "peak_price": 764000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 12, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 60, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C16_005490_POSCOHOLDINGS_20230413_LITHIUM_RESOURCE_STAGE2_SUCCESS_WITH_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_attention", "resource_asset_or_recycling_route_claim", "supply_chain_security_premium"], "stage3_evidence_fields": ["bankable_resource_control_required", "production_schedule_or_processing_capacity_required", "offtake_margin_revision_bridge_required"], "stage4b_evidence_fields": ["resource_policy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_optional_claim_without_cashflow", "financing_or_capex_gap", "margin_or_revision_duration_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "trigger_date": "2023-04-13", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -21.62, "MAE_30D_pct": -3.68, "MAE_90D_pct": -21.62, "MFE_180D_pct": 83.19, "MFE_30D_pct": 83.19, "MFE_90D_pct": 83.19, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_001570_GEUMYANG_20230711_LITHIUM_RESOURCE_OPTIONALITY_FALSE_GREEN", "case_role": "resource_optionality_false_green_counterexample", "company_name": "금양", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Lithium/resource optionality should not become Green without bankable resource control, financing, production schedule, offtake, and cash-flow bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -57.22, "entry_date": "2023-07-11", "entry_price": 105900, "evidence_family": "lithium_resource_optional_claim_without_bankable_production_cashflow_bridge", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_SUPPLY_POLICY_BANKABILITY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-27", "low_price_180d": 83000, "peak_date": "2023-07-26", "peak_price": 194000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001570.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C16_001570_GEUMYANG_20230711_LITHIUM_RESOURCE_OPTIONALITY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_attention", "resource_asset_or_recycling_route_claim", "supply_chain_security_premium"], "stage3_evidence_fields": ["bankable_resource_control_required", "production_schedule_or_processing_capacity_required", "offtake_margin_revision_bridge_required"], "stage4b_evidence_fields": ["resource_policy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_optional_claim_without_cashflow", "financing_or_capex_gap", "margin_or_revision_duration_failure"], "symbol": "001570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv", "trigger_date": "2023-07-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -51.77, "MAE_30D_pct": -25.08, "MAE_90D_pct": -30.48, "MFE_180D_pct": 45.99, "MFE_30D_pct": 45.99, "MFE_90D_pct": 45.99, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_005420_COSMOCHEM_20230403_RECYCLING_RESOURCE_PRICE_PREMIUM_FALSE_GREEN", "case_role": "recycling_resource_premium_counterexample", "company_name": "코스모화학", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Recycling/resource price premium should stay Yellow unless real feedstock, processing capacity, margin and revision duration are visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -66.97, "entry_date": "2023-04-03", "entry_price": 64800, "evidence_family": "battery_recycling_resource_supply_price_premium_without_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_SUPPLY_POLICY_BANKABILITY_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-31", "low_price_180d": 31250, "peak_date": "2023-04-10", "peak_price": 94600, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005420.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 30, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C16_005420_COSMOCHEM_20230403_RECYCLING_RESOURCE_PRICE_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_attention", "resource_asset_or_recycling_route_claim", "supply_chain_security_premium"], "stage3_evidence_fields": ["bankable_resource_control_required", "production_schedule_or_processing_capacity_required", "offtake_margin_revision_bridge_required"], "stage4b_evidence_fields": ["resource_policy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_optional_claim_without_cashflow", "financing_or_capex_gap", "margin_or_revision_duration_failure"], "symbol": "005420", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005420/2023.csv", "trigger_date": "2023-04-03", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "LITHIUM_RESOURCE_SUPPLY_POLICY_BANKABILITY_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "strategic_resource_policy_supply_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource supply rows should permit Stage2 on policy/resource attention, but Stage3 Green requires bankable resource control, production or processing capacity, offtake, margin and revision bridge; resource optionality without cash-flow conversion should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C16 + symbol + trigger_type + entry_date.
3. Add C16-specific strategic-resource bankability guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_GREEN_REQUIRES_BANKABLE_RESOURCE_PRODUCTION_OFFTAKE_MARGIN_REVISION
- C16_RESOURCE_OPTIONALITY_STAGE2_YELLOW_CAP
- C16_RESOURCE_POLICY_PRICE_PREMIUM_LOCAL_4B
- C16_RECYCLING_RESOURCE_WITHOUT_MARGIN_DURATION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

