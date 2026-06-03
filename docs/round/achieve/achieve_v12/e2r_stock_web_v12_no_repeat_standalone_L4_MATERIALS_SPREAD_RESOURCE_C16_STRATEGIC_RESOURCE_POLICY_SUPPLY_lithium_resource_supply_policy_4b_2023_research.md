# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy supply / lithium-resource 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_RESOURCE_SUPPLY_POLICY_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|strategic_resource_project_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_lithium_resource_supply_policy_4b_2023_research.md
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
Each row uses a new `C16 + symbol + trigger_type + entry_date` hard key:
```text
C16 + 005490 + Stage2-Actionable + 2023-03-31
C16 + 001570 + 4B-local-price-only + 2023-07-26
C16 + 005420 + Stage3-Yellow + 2023-07-26
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
005490 POSCO홀딩스: corporate_action_candidate_count=0; clean 2023 forward window.
001570 금양: selected 2023/2024 forward window clean; historical corporate-action candidates latest 2007-10-23, outside selected test window.
005420 코스모화학: selected 2023/2024 forward window clean; historical corporate-action candidates latest 2019-12-24, outside selected test window.
```

## 3. Research thesis

C16 should distinguish real strategic-resource supply conversion from resource-policy optionality already paid in price:

```text
strategic-resource policy / supply-chain security
→ resource project finality or vertical integration
→ offtake/customer bridge and feedstock visibility
→ capex timetable and execution
→ ASP/input-cost and working-capital bridge
→ gross margin and revision confirmation
→ Stage2/Green or local 4B cap
```

A resource headline is a mine on the map. Stage2 can buy the route when the road, buyer, plant and margin bridge are visible. Green should not pay mine-level multiples for a road that has not yet reached cash flow.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C16_005490_POSCOHOLDINGS_20230331_LITHIUM_VERTICAL_SUPPLY_STAGE2 | 005490 | positive_lithium_vertical_supply_resource_policy_stage2_success_with_later_4b_refresh | 2023-03-31 | 368000 | 764000 on 2023-07-26 | 356000 on 2023-05-15 | 18.48% | 107.61% | 107.61% | -3.26% | -47.71% |
| C16_001570_KEUMYANG_20230726_LITHIUM_RESOURCE_PRICE_PREMIUM_4B | 001570 | lithium_resource_policy_price_premium_counterexample | 2023-07-26 | 152200 | 194000 on 2023-07-26 | 72300 on 2024-01-26 | 27.46% | 27.46% | 27.46% | -52.5% | -62.73% |
| C16_005420_COSMOCHEM_20230726_BATTERY_RESOURCE_RECYCLING_PREMIUM_4B | 005420 | battery_resource_recycling_policy_false_green_counterexample | 2023-07-26 | 58200 | 65300 on 2023-07-26 | 28550 on 2024-01-26 | 12.2% | 12.2% | 12.2% | -50.95% | -56.28% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 005490 is the positive anchor. The March 2023 lithium/resource vertical-supply route produced a large 90D/180D MFE before the July premium required 4B refresh discipline.
- Stage2 is allowed only when policy/resource salience maps to project finality, vertical integration, offtake/customer bridge, capex timetable, ASP/input-cost and margin/revision visibility.

### Stage3 / Green
- C16 Green should require resource project finality, offtake/customer or feedstock bridge, capex execution, ASP/input-cost pass-through and margin/revision confirmation.
- 005420 is the false-Green/Yellow guard: battery-resource recycling and strategic supply confirmation were real themes, but the July 2023 price confirmation did not supply enough incremental volume/margin evidence after the premium.

### 4B
- 001570 fills the lithium-resource policy price-premium 4B pocket. The trigger had a sharp local high, but forward MAE overwhelmed residual upside.
- 005420 shows the recycling/materials version of the same failure: resource-supply optionality can remain plausible while the price already paid for too much without project-to-margin proof.
- 005490 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the resource pipeline.

### 4C
- No hard project cancellation, impairment or financing break is asserted.
- The C16 break mode here is optionality exhaustion: strategic-resource policy remains relevant, but incremental project finality, offtake, capex execution and margin revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C16_001570_KEUMYANG_20230726_LITHIUM_RESOURCE_PRICE_PREMIUM_4B": {
    "ASP_input_cost_bridge": 3,
    "capex_execution_and_timetable": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "offtake_customer_bridge": 2,
    "resource_project_finality": 3,
    "strategic_resource_policy_visibility": 8,
    "total": 29,
    "valuation_rerating_runway": 1
  },
  "C16_005420_COSMOCHEM_20230726_BATTERY_RESOURCE_RECYCLING_PREMIUM_4B": {
    "ASP_input_cost_bridge": 3,
    "capex_execution_and_timetable": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "offtake_customer_bridge": 3,
    "resource_project_finality": 3,
    "strategic_resource_policy_visibility": 7,
    "total": 29,
    "valuation_rerating_runway": 1
  },
  "C16_005490_POSCOHOLDINGS_20230331_LITHIUM_VERTICAL_SUPPLY_STAGE2": {
    "ASP_input_cost_bridge": 7,
    "capex_execution_and_timetable": 7,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 9,
    "offtake_customer_bridge": 7,
    "resource_project_finality": 8,
    "strategic_resource_policy_visibility": 10,
    "total": 67,
    "valuation_rerating_runway": 8
  }
}
```

## 7. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_policy and project_offtake_capex_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if lithium_resource_price_premium and no incremental_project_finality_offtake_capex_margin_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and resource_optionality_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 001570 / 2023-07-26: lithium-resource policy premium can be over-promoted if the model treats price heat as project finality, offtake and margin proof.
- 005420 / 2023-07-26: battery-resource recycling confirmation can look like Yellow-to-Green, but fails without renewed feedstock, volume and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -3.26, "MAE_30D_pct": -3.26, "MAE_90D_pct": -3.26, "MFE_180D_pct": 107.61, "MFE_30D_pct": 18.48, "MFE_90D_pct": 107.61, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_005490_POSCOHOLDINGS_20230331_LITHIUM_VERTICAL_SUPPLY_STAGE2", "case_role": "positive_lithium_vertical_supply_resource_policy_stage2_success_with_later_4b_refresh", "company_name": "POSCO홀딩스", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2023_forward_window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when lithium/resource vertical-integration and strategic supply policy evidence mapped to a large balance-sheet sponsor, project pipeline and future margin/revision optionality before the rerating was fully capitalized. Green still requires resource project finality, production timetable, offtake/customer bridge, capex execution, ASP/input-cost and margin/revision confirmation; after the July 2023 premium, the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.71, "entry_date": "2023-03-31", "entry_price": 368000, "evidence_family": "lithium_resource_vertical_supply_policy_project_pipeline_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_SUPPLY_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-05-15", "low_price_180d": 356000, "peak_date": "2023-07-26", "peak_price": 764000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 7, "capex_execution_and_timetable": 7, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 9, "offtake_customer_bridge": 7, "resource_project_finality": 8, "strategic_resource_policy_visibility": 10, "total": 67, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C16_005490_POSCOHOLDINGS_20230331_LITHIUM_VERTICAL_SUPPLY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_supply_visibility", "resource_project_finality_or_vertical_integration", "offtake_customer_capex_ASP_margin_revision_route"], "stage3_evidence_fields": ["resource_project_finality_required", "offtake_customer_or_feedstock_bridge_required", "capex_timetable_ASP_input_cost_margin_revision_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_project_finality_gap", "offtake_or_feedstock_supply_gap", "margin_revision_bridge_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "trigger_date": "2023-03-31", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -52.5, "MAE_30D_pct": -30.75, "MAE_90D_pct": -45.47, "MFE_180D_pct": 27.46, "MFE_30D_pct": 27.46, "MFE_90D_pct": 27.46, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_001570_KEUMYANG_20230726_LITHIUM_RESOURCE_PRICE_PREMIUM_4B", "case_role": "lithium_resource_policy_price_premium_counterexample", "company_name": "금양", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidates are historical and latest 2007-10-23, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Lithium-resource policy premium should route to local 4B or counterexample when the stock has already capitalized resource-project optionality and incremental project finality, offtake/customer bridge, capex timetable, financing and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -62.73, "entry_date": "2023-07-26", "entry_price": 152200, "evidence_family": "lithium_resource_policy_price_premium_without_resource_project_finality_offtake_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_SUPPLY_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-01-26", "low_price_180d": 72300, "peak_date": "2023-07-26", "peak_price": 194000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001570.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "capex_execution_and_timetable": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "offtake_customer_bridge": 2, "resource_project_finality": 3, "strategic_resource_policy_visibility": 8, "total": 29, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_001570_KEUMYANG_20230726_LITHIUM_RESOURCE_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_supply_visibility", "resource_project_finality_or_vertical_integration", "offtake_customer_capex_ASP_margin_revision_route"], "stage3_evidence_fields": ["resource_project_finality_required", "offtake_customer_or_feedstock_bridge_required", "capex_timetable_ASP_input_cost_margin_revision_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_project_finality_gap", "offtake_or_feedstock_supply_gap", "margin_revision_bridge_failure"], "symbol": "001570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -50.95, "MAE_30D_pct": -19.67, "MAE_90D_pct": -46.31, "MFE_180D_pct": 12.2, "MFE_30D_pct": 12.2, "MFE_90D_pct": 12.2, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_005420_COSMOCHEM_20230726_BATTERY_RESOURCE_RECYCLING_PREMIUM_4B", "case_role": "battery_resource_recycling_policy_false_green_counterexample", "company_name": "코스모화학", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidates are historical and latest 2019-12-24, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Battery-resource recycling and strategic supply price confirmation should stay Yellow or route to local 4B when price strength is not followed by resource feedstock visibility, customer/offtake bridge, capacity utilization, ASP/input-cost pass-through and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -56.28, "entry_date": "2023-07-26", "entry_price": 58200, "evidence_family": "battery_resource_recycling_policy_price_confirmation_without_incremental_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_SUPPLY_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-01-26", "low_price_180d": 28550, "peak_date": "2023-07-26", "peak_price": 65300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005420.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "capex_execution_and_timetable": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "offtake_customer_bridge": 3, "resource_project_finality": 3, "strategic_resource_policy_visibility": 7, "total": 29, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_005420_COSMOCHEM_20230726_BATTERY_RESOURCE_RECYCLING_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_supply_visibility", "resource_project_finality_or_vertical_integration", "offtake_customer_capex_ASP_margin_revision_route"], "stage3_evidence_fields": ["resource_project_finality_required", "offtake_customer_or_feedstock_bridge_required", "capex_timetable_ASP_input_cost_margin_revision_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_project_finality_gap", "offtake_or_feedstock_supply_gap", "margin_revision_bridge_failure"], "symbol": "005420", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005420/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "LITHIUM_RESOURCE_SUPPLY_POLICY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "strategic_resource_lithium_supply_policy_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource rows should allow Stage2 when policy/resource evidence maps to project finality, vertical integration, offtake/customer bridge, capex timetable, ASP/input-cost and margin-revision evidence, but should route to local 4B/Yellow when lithium/resource price premium has already capitalized optionality and incremental project-to-margin evidence has not refreshed.",
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
3. Add C16-specific strategic-resource / lithium / project-finality / offtake / capex / ASP-input-cost / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_STAGE2_ALLOWED_ON_PROJECT_OFFTAKE_CAPEX_MARGIN_REVISION_BRIDGE
- C16_GREEN_REQUIRES_RESOURCE_FINALITY_OFFTAKE_FEEDSTOCK_ASP_INPUT_COST_REVISION
- C16_LITHIUM_RESOURCE_POLICY_PRICE_PREMIUM_LOCAL_4B
- C16_RESOURCE_OPTIONALITY_WITHOUT_PROJECT_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

