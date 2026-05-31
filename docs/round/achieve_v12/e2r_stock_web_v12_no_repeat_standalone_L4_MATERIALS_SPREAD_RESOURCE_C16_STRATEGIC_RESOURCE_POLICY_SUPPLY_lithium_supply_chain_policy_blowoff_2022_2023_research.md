# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy supply / lithium supply-chain 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_SUPPLY_CHAIN_POLICY_BLOWOFF_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|lithium_resource_policy_supply_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_lithium_supply_chain_policy_blowoff_2022_2023_research.md
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

This run avoids those top-covered C16 symbols and adds 001570, 095500, and 101670.  
Each row uses a new `C16 + symbol + trigger_type + entry_date` hard key:
```text
C16 + 001570 + Stage2-Actionable + 2022-08-10
C16 + 095500 + Stage3-Yellow + 2023-03-24
C16 + 101670 + 4B-local-price-only + 2023-04-07
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
001570 금양: selected 2022/2023 forward window uses post-historical split-adjustment era; raw/unadjusted caveat acknowledged.
095500 미래나노텍: selected 2023 forward window clean; historical corporate-action candidates are 2007-2009 and outside selected trigger window.
101670 하이드로리튬: selected 2023 forward window stops before the 2023-12-22 corporate-action candidate; name changed from 코리아에스이 to 하이드로리튬 before selected trigger window.
```

## 3. Research thesis

C16 should split real strategic-resource discovery from lithium resource policy/supply-chain optionality already paid in price:

```text
strategic resource / lithium policy supply
→ resource or offtake specificity
→ supply-chain localization
→ capacity execution and financing quality
→ customer/contract visibility
→ margin and revision bridge
→ Stage2/Green or local 4B cap
```

A strategic resource story is a mine plan, not a metal label. Stage2 can buy when the shaft, buyer, financing and conversion route are becoming visible. Green should not buy the label after the market has already priced every unbuilt ton of lithium.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C16_001570_KUMYANG_20220810_LITHIUM_POLICY_SUPPLY_STAGE2 | 001570 | positive_lithium_resource_policy_supply_chain_stage2_success_with_later_4b_refresh | 2022-08-10 | 10350 | 89700 on 2023-04-11 | 8600 on 2022-08-10 | 108.7% | 300.97% | 766.67% | -16.91% | -35.9% |
| C16_095500_MIRAENANOTECH_20230324_LITHIUM_SUPPLY_CHAIN_FALSE_GREEN | 095500 | lithium_material_supply_chain_false_green_counterexample | 2023-03-24 | 32700 | 36900 on 2023-04-03 | 15000 on 2023-10-26 | 12.84% | 12.84% | 12.84% | -54.13% | -59.35% |
| C16_101670_HYDROLITHIUM_20230407_LITHIUM_EXTRACTION_PRICE_PREMIUM_4B | 101670 | lithium_extraction_policy_supply_price_premium_4b_counterexample | 2023-04-07 | 53700 | 60900 on 2023-04-07 | 10280 on 2023-10-31 | 13.41% | 13.41% | 13.41% | -80.86% | -83.12% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 001570 is the positive anchor. The August 2022 lithium/strategic-resource supply-chain route produced very strong MFE before the 2023 premium required 4B refresh discipline.
- Stage2 is allowed only when strategic-resource policy salience maps to resource/offtake specificity, supply-chain localization, capacity execution, financing quality, customer visibility and margin/revision visibility.
- 가격만 있는 early entry는 금지된다. This positive row is included because the trigger family is lithium policy/supply-chain optionality, not price-only momentum.

### Stage3 / Green
- C16 Green should require resource/offtake specificity, capacity execution, financing quality, customer/contract visibility and margin/revision bridge.
- 095500 is the false-Green/Yellow guard: lithium supply-chain price confirmation was visible, but the March 2023 trigger had limited residual MFE and a much larger full-window drawdown when resource-to-margin evidence did not refresh.

### 4B
- 101670 fills the lithium extraction/strategic-resource price-premium 4B pocket. The April 2023 trigger had limited local MFE and a very large forward drawdown.
- 095500 shows the same failure in materials supply-chain form: critical-mineral optionality can remain directionally real while the listed-company earnings bridge is too stale for Green.
- 001570 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the lithium supply-chain option.

### 4C
- No hard mine cancellation, offtake termination, financing failure or accounting break is asserted.
- The C16 break mode here is resource-to-margin exhaustion: the lithium story may remain directionally real, but incremental resource/offtake, capacity execution, financing and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C16_001570_KUMYANG_20220810_LITHIUM_POLICY_SUPPLY_STAGE2": {
    "capacity_execution_bridge": 6,
    "customer_quality_or_contract_visibility": 4,
    "financing_and_working_capital_quality": 3,
    "information_confidence": 4,
    "margin_revision_bridge": 3,
    "market_mispricing": 9,
    "resource_or_offtake_specificity": 6,
    "strategic_resource_policy_salience": 10,
    "supply_chain_localization_visibility": 9,
    "total": 62,
    "valuation_rerating_runway": 8
  },
  "C16_095500_MIRAENANOTECH_20230324_LITHIUM_SUPPLY_CHAIN_FALSE_GREEN": {
    "capacity_execution_bridge": 3,
    "customer_quality_or_contract_visibility": 2,
    "financing_and_working_capital_quality": 2,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "resource_or_offtake_specificity": 3,
    "strategic_resource_policy_salience": 8,
    "supply_chain_localization_visibility": 7,
    "total": 35,
    "valuation_rerating_runway": 1
  },
  "C16_101670_HYDROLITHIUM_20230407_LITHIUM_EXTRACTION_PRICE_PREMIUM_4B": {
    "capacity_execution_bridge": 2,
    "customer_quality_or_contract_visibility": 2,
    "financing_and_working_capital_quality": 2,
    "information_confidence": 3,
    "margin_revision_bridge": 1,
    "market_mispricing": 3,
    "resource_or_offtake_specificity": 3,
    "strategic_resource_policy_salience": 9,
    "supply_chain_localization_visibility": 7,
    "total": 32,
    "valuation_rerating_runway": 0
  }
}
```

## 7. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_policy and resource_offtake_capacity_financing_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if lithium_resource_price_premium and no incremental_resource_offtake_capacity_financing_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and resource_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 095500 / 2023-03-24: lithium supply-chain confirmation can be over-promoted if price strength substitutes for refreshed offtake, capacity and margin proof.
- 101670 / 2023-04-07: lithium extraction premium can look actionable, but fails without renewed resource/offtake, financing and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -16.91, "MAE_30D_pct": -16.91, "MAE_90D_pct": -16.91, "MFE_180D_pct": 766.67, "MFE_30D_pct": 108.7, "MFE_90D_pct": 300.97, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_001570_KUMYANG_20220810_LITHIUM_POLICY_SUPPLY_STAGE2", "case_role": "positive_lithium_resource_policy_supply_chain_stage2_success_with_later_4b_refresh", "company_name": "금양", "corporate_action_window_status": "selected 2022/2023 forward window uses post-historical split-adjustment era; profile corporate-action/name candidates are historical or outside selected trigger logic", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when lithium/critical-mineral policy salience, domestic supply-chain optionality, capacity narrative and material-supply scarcity were visible before the rerating was fully capitalized. Green still requires non-price evidence: credible resource or offtake path, capacity execution, customer visibility, financing discipline and margin/revision bridge. After the 2023 premium, the same story required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -35.9, "entry_date": "2022-08-10", "entry_price": 10350, "evidence_family": "lithium_resource_policy_supply_chain_domestic_materials_optional_capacity_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_SUPPLY_CHAIN_POLICY_BLOWOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-08-10", "low_price_180d": 8600, "peak_date": "2023-04-11", "peak_price": 89700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001570.json", "raw_component_score_breakdown": {"capacity_execution_bridge": 6, "customer_quality_or_contract_visibility": 4, "financing_and_working_capital_quality": 3, "information_confidence": 4, "margin_revision_bridge": 3, "market_mispricing": 9, "resource_or_offtake_specificity": 6, "strategic_resource_policy_salience": 10, "supply_chain_localization_visibility": 9, "total": 62, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C16_001570_KUMYANG_20220810_LITHIUM_POLICY_SUPPLY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_salience", "supply_chain_localization_visibility", "resource_offtake_capacity_margin_revision_route"], "stage3_evidence_fields": ["resource_or_offtake_specificity_required", "capacity_execution_and_financing_quality_required", "customer_contract_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_lithium_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_or_offtake_nonconversion", "financing_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "001570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001570/2022.csv", "trigger_date": "2022-08-10", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.13, "MAE_30D_pct": -27.83, "MAE_90D_pct": -38.23, "MFE_180D_pct": 12.84, "MFE_30D_pct": 12.84, "MFE_90D_pct": 12.84, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_095500_MIRAENANOTECH_20230324_LITHIUM_SUPPLY_CHAIN_FALSE_GREEN", "case_role": "lithium_material_supply_chain_false_green_counterexample", "company_name": "미래나노텍", "corporate_action_window_status": "selected 2023 forward window clean; historical corporate-action candidates are 2007-2009 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Lithium supply-chain price confirmation should remain Yellow or local 4B when the market has already capitalized critical-mineral optionality and fresh offtake, capacity execution, financing, customer quality and margin/revision evidence do not refresh. The March 2023 trigger had limited residual MFE and a large full-window drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -59.35, "entry_date": "2023-03-24", "entry_price": 32700, "evidence_family": "lithium_material_supply_chain_price_confirmation_without_offtake_capacity_financing_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_SUPPLY_CHAIN_POLICY_BLOWOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-26", "low_price_180d": 15000, "peak_date": "2023-04-03", "peak_price": 36900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/095/095500.json", "raw_component_score_breakdown": {"capacity_execution_bridge": 3, "customer_quality_or_contract_visibility": 2, "financing_and_working_capital_quality": 2, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "resource_or_offtake_specificity": 3, "strategic_resource_policy_salience": 8, "supply_chain_localization_visibility": 7, "total": 35, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_095500_MIRAENANOTECH_20230324_LITHIUM_SUPPLY_CHAIN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_salience", "supply_chain_localization_visibility", "resource_offtake_capacity_margin_revision_route"], "stage3_evidence_fields": ["resource_or_offtake_specificity_required", "capacity_execution_and_financing_quality_required", "customer_contract_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_lithium_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_or_offtake_nonconversion", "financing_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "095500", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv", "trigger_date": "2023-03-24", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -80.86, "MAE_30D_pct": -44.32, "MAE_90D_pct": -46.37, "MFE_180D_pct": 13.41, "MFE_30D_pct": 13.41, "MFE_90D_pct": 13.41, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_101670_HYDROLITHIUM_20230407_LITHIUM_EXTRACTION_PRICE_PREMIUM_4B", "case_role": "lithium_extraction_policy_supply_price_premium_4b_counterexample", "company_name": "하이드로리튬", "corporate_action_window_status": "selected 2023 forward window stops before the 2023-12-22 corporate-action candidate; name changed from 코리아에스이 to 하이드로리튬 before selected trigger window", "current_profile_error": true, "current_profile_verdict": "Lithium extraction/strategic-resource premium should route to local 4B/counterexample when the policy and resource story is already in price and fresh resource/offtake, capacity ramp, financing, customer and margin/revision evidence do not refresh. The April 2023 trigger had limited local MFE and a very large forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -83.12, "entry_date": "2023-04-07", "entry_price": 53700, "evidence_family": "lithium_extraction_strategic_resource_price_premium_without_resource_offtake_capacity_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_SUPPLY_CHAIN_POLICY_BLOWOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-31", "low_price_180d": 10280, "peak_date": "2023-04-07", "peak_price": 60900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/101/101670.json", "raw_component_score_breakdown": {"capacity_execution_bridge": 2, "customer_quality_or_contract_visibility": 2, "financing_and_working_capital_quality": 2, "information_confidence": 3, "margin_revision_bridge": 1, "market_mispricing": 3, "resource_or_offtake_specificity": 3, "strategic_resource_policy_salience": 9, "supply_chain_localization_visibility": 7, "total": 32, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C16_101670_HYDROLITHIUM_20230407_LITHIUM_EXTRACTION_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_salience", "supply_chain_localization_visibility", "resource_offtake_capacity_margin_revision_route"], "stage3_evidence_fields": ["resource_or_offtake_specificity_required", "capacity_execution_and_financing_quality_required", "customer_contract_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_lithium_price_premium", "resource_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_or_offtake_nonconversion", "financing_or_working_capital_slippage", "margin_revision_bridge_failure"], "symbol": "101670", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/101/101670/2023.csv", "trigger_date": "2023-04-07", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "LITHIUM_SUPPLY_CHAIN_POLICY_BLOWOFF_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "strategic_resource_policy_supply_lithium_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource/lithium rows should allow Stage2 only when policy salience maps to resource/offtake specificity, supply-chain localization, capacity execution, financing quality and margin revision; lithium resource price premiums should route to Yellow/local 4B when resource-to-margin evidence has not refreshed.",
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
3. Add C16-specific strategic-resource / lithium policy / resource-offtake / capacity execution / financing / customer-contract / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_STAGE2_ALLOWED_ON_RESOURCE_OFFTAKE_CAPACITY_FINANCING_MARGIN_REVISION_BRIDGE
- C16_GREEN_REQUIRES_RESOURCE_SPECIFICITY_OFFTAKE_CAPACITY_FINANCING_CUSTOMER_REVISION
- C16_LITHIUM_RESOURCE_PRICE_PREMIUM_LOCAL_4B
- C16_PRICE_CONFIRMATION_WITHOUT_RESOURCE_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

