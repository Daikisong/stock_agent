# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R11
scheduled_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD
output_file = e2r_stock_web_v12_residual_round_R11_loop_15_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`; the rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed here: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`.

This R11 run tests a residual question: when a policy statute is real, does the equity have a direct policy-to-revenue route, or is it only wearing the event like a borrowed coat?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 15
allowed_large_sector_for_R11 = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or policy-defense-linked L1
selected_large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_sector_consistency = pass
```

R11 is a policy/event residual round. The selected scope stays inside L10 and uses C31, not a sector-specific consumer, finance, biotech, or platform round.

## 3. Previous Coverage / Duplicate Avoidance Check

Prior local v12 R11 files were treated as already-covered coverage:

- R11 Loop 10: C32 governance/control premium.
- R11 Loop 11: C31 value-up, energy-policy, and oil-event cases.
- R11 Loop 12: C32 governance/control premium holdout.
- R11 Loop 13: C31 COVID/test kit policy-event stress.
- R11 Loop 14: C31 IRA battery and EV-policy cases.

The current loop avoids those symbol families. It adds a wind/renewable-policy branch under C31 with four new symbols: `112610`, `389260`, `297090`, and `100130`.

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
duplicate_low_value_loop = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The schema basis is `tradable_raw`; tradable rows require positive OHLCV and exclude zero-volume/invalid rows. Corporate-action-contaminated windows are blocked for weight calibration.

## 5. Historical Eligibility Gate

All four representative cases pass the 180-trading-day forward-window gate from the 2022-08-17 entry date. None has a corporate-action candidate date inside the representative 180D calibration window.

|symbol|company|entry_date|forward_window|corporate_action_window_status|calibration_usable|
|---|---|---:|---:|---|---|
|112610|씨에스윈드|2022-08-17|180|clean_180D_window|true|
|389260|대명에너지|2022-08-17|180|clean_180D_window|true|
|297090|씨에스베어링|2022-08-17|180|clean_180D_window|true|
|100130|동국S&C|2022-08-17|180|clean_180D_window|true|

`018000` was left narrative-only because a later wind-policy window would be contaminated by a 2024-05-21 corporate-action candidate.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD
compressed_rule_family = policy statute/event -> direct route check -> supplier/theme guard -> 4B local blowoff watch
```

C31 should not treat every beneficiary mention equally. A statute can be real while the equity route remains foggy. The proposed compression distinguishes:

1. Direct policy-to-revenue route: `112610`.
2. High-beta policy developer repricing: `389260`.
3. Loose supplier/fabrication proxy: `297090`, `100130`.

## 7. Case Selection Summary

|case_id|symbol|company|role|entry|MFE90/MAE90|profile_error|new|
|---|---|---|---|---|---|---|---|
|R11L15-C31-112610-IRA-WIND-TOWER|112610|씨에스윈드|structural_success|2022-08-17 / 63600|26.57 / -10.85|current_profile_missed_structural|true|
|R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE|389260|대명에너지|high_mae_success|2022-08-17 / 26450|39.89 / -24.95|current_profile_4B_too_late|true|
|R11L15-C31-297090-IRA-BEARING-PROXY|297090|씨에스베어링|false_positive_green|2022-08-17 / 11450|15.72 / -38.78|current_profile_false_positive|true|
|R11L15-C31-100130-IRA-FABRICATION-PROXY|100130|동국S&C|failed_rerating|2022-08-17 / 7110|9.0 / -31.01|current_profile_false_positive|true|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
```

Positive cases are not “the policy existed.” They are cases where the policy had a visible route into orders, assets, or revenue. Counterexamples are cases where the policy narrative existed but did not carry enough contemporaneous route visibility.

## 9. Evidence Source Map

|case_id|Stage2 evidence|Stage3 evidence|4B evidence|4C evidence|
|---|---|---|---|---|
|R11L15-C31-112610-IRA-WIND-TOWER|public law, policy optionality, direct wind-tower route, customer/order quality|financial visibility, multiple sources, durable customer confirmation|none|none|
|R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE|public law, renewable developer policy-beta, relative strength|limited multiple-source support|valuation blowoff, positioning overheat, price-only local peak|none|
|R11L15-C31-297090-IRA-BEARING-PROXY|public law, wind supplier proxy, relative strength|none|price-only local peak, positioning overheat|thesis evidence not confirmed|
|R11L15-C31-100130-IRA-FABRICATION-PROXY|public law, loose wind fabrication association|none|price-only local peak|thesis evidence not confirmed|

## 10. Price Data Source Map

|symbol|company|price_shard_path|profile_path|profile status|
|---|---|---|---|---|
|112610|씨에스윈드|atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv|atlas/symbol_profiles/112/112610.json|usable_with_caveat; no 180D overlap|
|389260|대명에너지|atlas/ohlcv_tradable_by_symbol_year/389/389260/2022.csv|atlas/symbol_profiles/389/389260.json|clean_tradable_path|
|297090|씨에스베어링|atlas/ohlcv_tradable_by_symbol_year/297/297090/2022.csv|atlas/symbol_profiles/297/297090.json|usable_with_caveat; CA candidates pre-entry|
|100130|동국S&C|atlas/ohlcv_tradable_by_symbol_year/100/100130/2022.csv|atlas/symbol_profiles/100/100130.json|clean_tradable_path|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|trigger|entry|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|peak|verdict|aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R11L15-C31-112610-S2A-20220816|112610|Stage2-Actionable|2022-08-16|2022-08-17 / 63600|11.64|26.57|38.52|-6.76|-10.85|-10.85|2023-04-24 / 88100|current_profile_missed_structural|representative|
|R11L15-C31-389260-S2A-20220816|389260|Stage2-Actionable|2022-08-16|2022-08-17 / 26450|39.89|39.89|39.89|-19.66|-24.95|-38.56|2022-09-01 / 37000|current_profile_4B_too_late|representative|
|R11L15-C31-297090-S2A-20220816|297090|Stage2-Actionable|2022-08-16|2022-08-17 / 11450|15.72|15.72|15.72|-26.64|-38.78|-38.78|2022-08-25 / 13250|current_profile_false_positive|representative|
|R11L15-C31-100130-S2A-20220816|100130|Stage2-Actionable|2022-08-16|2022-08-17 / 7110|9.0|9.0|9.0|-24.75|-31.01|-37.41|2022-08-25 / 7750|current_profile_false_positive|representative|
|R11L15-C31-389260-4B-20220901|389260|Stage4B-overlay|2022-09-01|2022-09-01 / 35100|5.41|5.41|5.41|-39.46|-43.45|-53.7|2022-09-01 / 37000|current_profile_4B_too_late|4B_overlay_only|


## 12. Trigger-Level OHLC Backtest Tables

The backtest uses `entry_price = c` on the entry-date row. MFE is max high over the forward window divided by entry close. MAE is min low over the forward window divided by entry close.

|symbol|entry_price|max_high_30D|max_high_90D|max_high_180D|min_low_30D|min_low_90D|min_low_180D|
|---|---:|---:|---:|---:|---:|---:|---:|
|112610|63600|71000|80500|88100|59300|56700|56700|
|389260|26450|37000|37000|37000|21250|19850|16250|
|297090|11450|13250|13250|13250|8400|7010|7010|
|100130|7110|7750|7750|7750|5350|4905|4450|

## 13. Current Calibrated Profile Stress Test

|case_id|current profile likely judgment|actual outcome|stress verdict|
|---|---|---|---|
|112610|Cautious Yellow because policy alone should not promote|Direct-route winner with +38.52% 180D MFE and tolerable -10.85% 180D MAE|current_profile_missed_structural|
|389260|Policy-beta Yellow but no immediate 4B risk overlay|+39.89% fast MFE followed by -56.08% drawdown after peak|current_profile_4B_too_late|
|297090|May become Yellow/Green if generic wind supplier route is overcounted|Only +15.72% MFE vs -38.78% 90D MAE|current_profile_false_positive|
|100130|May become actionable if loose wind fabrication association is overcounted|Only +9.00% MFE vs -36.57% 90D MAE|current_profile_false_positive|

Applied global axes are mostly kept. The gap is not “we need more policy bonus.” It is “policy bonus needs route congruence and loose-proxy guard.”

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable is useful for direct-route cases. It is dangerous when a symbol only shares the theme label.

```text
112610: Stage2-Actionable should be allowed to become Green when direct route + order/customer quality exists.
389260: Stage2-Actionable can be allowed, but local 4B watch should appear after fast policy-beta blowoff.
297090: Stage2-Actionable should not become Green without supplier-specific order/revision bridge.
100130: Stage2-Actionable should remain watch-only without route visibility.
```

Green lateness ratios are not computed because this run does not use a later confirmed Stage3-Green trigger. The point is a same-date C31 route guard, not a Yellow/Green timing retest.

## 15. 4B Local vs Full-window Timing Audit

`389260` provides the 4B timing row.

```text
Stage2_Actionable_entry_price = 26450
Stage4B_overlay_entry_price = 35100
local_peak_price_after_Stage2_Actionable = 37000
full_window_peak_price_after_Stage2_Actionable = 37000
four_b_local_peak_proximity = 0.82
four_b_full_window_peak_proximity = 0.82
four_b_timing_verdict = good_local_4B_watch_but_price_only_not_full_exit
do_not_treat_as_full_4B = true
```

The lesson is narrow: price-only local peak can create a risk watch, but it still should not become a full 4B exit without non-price evidence.

## 16. 4C Protection Audit

No full 4C calibration is proposed. The two counterexamples are `thesis_break_watch_only`: the route did not mature into durable evidence, but there was no hard contract cancellation or accounting/trust break at the trigger date.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = The rule is not for all L10 policy/event rows. It is specific to C31 policy subsidy / legislation events where route congruence separates direct beneficiaries from loose theme proxies.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
axis = c31_policy_route_congruence_and_theme_supplier_guard
```

Proposed shadow rule:

```text
If C31 policy/subsidy event exists:
    reward only symbols with visible policy-to-revenue route, order/customer quality, or asset/project exposure.
    keep loose supplier/theme proxy at Stage2-watch unless order/revision bridge is also present.
    after local price blowoff, create 4B-watch but not full 4B unless non-price risk evidence exists.
```

## 19. Before / After Backtest Comparison

|profile_id|hypothesis|eligible|avg_MFE90|avg_MAE90|false_positive_rate|missed_structural_count|score_return_alignment|
|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current profile|4|22.8|-26.4|2/4|1|mixed|
|P0b e2r_2_0_baseline_reference|older, looser policy theme handling|4|22.8|-26.4|2-3/4|1|weak|
|P1 sector_specific_candidate_profile|no broad sector delta proposed because sample is canonical policy-event, not whole L10|4|33.23|-17.9|not_promoted_by_sector|1|not_primary|
|P2 canonical_archetype_candidate_profile|route-congruence boost + supplier guard|4|33.23|-17.9|0/2 selected positives|0|best|
|P3 counterexample_guard_profile|strictly blocks loose supplier/fabrication proxy without order/revision bridge|4|positive-only 33.23|positive-only -17.90|0/2|1|conservative|


## 20. Score-Return Alignment Matrix

|symbol|before score/label|after score/label|MFE90|MAE90|alignment|
|---|---:|---:|---:|---:|---|
|112610|82.0 / Stage3-Yellow|89.0 / Stage3-Green|26.57|-10.85|improved direct-route positive|
|389260|76.0 / Stage3-Yellow|80.0 / Stage3-Yellow+4B-watch|39.89|-24.95|improved risk labeling, not promotion|
|297090|77.0 / Stage3-Yellow|69.0 / Stage2-watch|15.72|-38.78|false-positive reduced|
|100130|74.0 / Stage2-Actionable/Yellow-border|63.0 / Stage2-watch|9.00|-36.57|false-positive reduced|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD|2|2|1|0|4|0|5|4|4|False|True|direct-route vs loose-supplier policy theme split covered; still needs non-wind policy holdout|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_false_positive
  - current_profile_4B_too_late
new_axis_proposed:
  - c31_policy_route_congruence_and_theme_supplier_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: same_archetype_new_symbol +16; new_symbol +12; new_trigger_family +16; counterexample_gap +8; residual_error +20; new_regime +3; penalties 0; estimated +75
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual stock-web tradable OHLC rows.
- Entry-date close and 30D/90D/180D MFE/MAE.
- Symbol profile windows and corporate-action overlap checks.
- Positive/counterexample split for C31 wind/renewable policy-event route.

Not validated:

- No live 2026 candidate discovery.
- No production scoring code.
- No stock_agent source tree.
- No brokerage or auto-trading route.
- No global weight promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_route_congruence_score,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Direct policy-to-revenue route separates 112610 success from loose supplier proxies","Improves false-positive filtering while preserving direct-route winner","R11L15-C31-112610-S2A-20220816|R11L15-C31-297090-S2A-20220816|R11L15-C31-100130-S2A-20220816",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_policy_theme_supplier_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Loose wind supplier/fabrication proxy without visible order/revision bridge caused high MAE","Blocks policy-only promotion for 297090 and 100130","R11L15-C31-297090-S2A-20220816|R11L15-C31-100130-S2A-20220816",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_price_only_local_4b_watch,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Early policy event blowoff can mark local risk but not full thesis-break 4B without non-price evidence","Adds 4B watch for 389260 high-MAE success","R11L15-C31-389260-4B-20220901",1,0,0,low,overlay_shadow_only,"4B overlay only; not positive-stage promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R11L15-C31-112610-IRA-WIND-TOWER","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R11L15-C31-112610-S2A-20220816","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Direct wind-tower route translated policy into durable order/revenue optionality; current proxy was likely too conservative because it penalized policy-only without enough route congruence."}
{"row_type":"case","case_id":"R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE","symbol":"389260","company_name":"대명에너지","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R11L15-C31-389260-S2A-20220816","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"High early MFE confirms policy-beta utility, but drawdown shows why policy theme needs route-congruence plus local 4B watch, not unconditional Green."}
{"row_type":"case","case_id":"R11L15-C31-297090-IRA-BEARING-PROXY","symbol":"297090","company_name":"씨에스베어링","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R11L15-C31-297090-S2A-20220816","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The policy event was real, but supplier proxy did not carry sufficient route visibility; MFE/MAE alignment argues for a guard, not promotion."}
{"row_type":"case","case_id":"R11L15-C31-100130-IRA-FABRICATION-PROXY","symbol":"100130","company_name":"동국S&C","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R11L15-C31-100130-S2A-20220816","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A loose policy association was not enough; the path decayed after a small local spike."}
{"row_type":"trigger","trigger_id":"R11L15-C31-112610-S2A-20220816","case_id":"R11L15-C31-112610-IRA-WIND-TOWER","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","evidence_available_at_that_date":"US Inflation Reduction Act became signed law; wind PTC/ITC route directly maps to tower demand, while company had US-facing wind-tower exposure.","evidence_source":"historical public law/event plus company route classification; price rows from stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-17","entry_price":63600,"MFE_30D_pct":11.64,"MFE_90D_pct":26.57,"MFE_180D_pct":38.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.76,"MAE_90D_pct":-10.85,"MAE_180D_pct":-10.85,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-24","peak_price":88100,"drawdown_after_peak_pct":-18.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"policy_route_structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L15-C31-112610-IRA-WIND-TOWER|2022-08-17|63600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L15-C31-389260-S2A-20220816","case_id":"R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE","symbol":"389260","company_name":"대명에너지","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","evidence_available_at_that_date":"IRA renewable subsidy event and local renewable developer optionality created fast repricing, but the forward path was price-volatility dominated and needed early 4B overlay.","evidence_source":"historical public law/event plus developer policy-beta route; price rows from stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/389/389260/2022.csv","profile_path":"atlas/symbol_profiles/389/389260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-17","entry_price":26450,"MFE_30D_pct":39.89,"MFE_90D_pct":39.89,"MFE_180D_pct":39.89,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.66,"MAE_90D_pct":-24.95,"MAE_180D_pct":-38.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-09-01","peak_price":37000,"drawdown_after_peak_pct":-56.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"policy_beta_high_mae_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE|2022-08-17|26450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L15-C31-297090-S2A-20220816","case_id":"R11L15-C31-297090-IRA-BEARING-PROXY","symbol":"297090","company_name":"씨에스베어링","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","evidence_available_at_that_date":"Generic wind-component supplier proxy reacted to IRA theme, but component route did not provide enough visible margin/order bridge at trigger date.","evidence_source":"historical public law/event plus supplier proxy classification; price rows from stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/297/297090/2022.csv","profile_path":"atlas/symbol_profiles/297/297090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-17","entry_price":11450,"MFE_30D_pct":15.72,"MFE_90D_pct":15.72,"MFE_180D_pct":15.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.64,"MAE_90D_pct":-38.78,"MAE_180D_pct":-38.78,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-25","peak_price":13250,"drawdown_after_peak_pct":-47.09,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_supplier_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L15-C31-297090-IRA-BEARING-PROXY|2022-08-17|11450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L15-C31-100130-S2A-20220816","case_id":"R11L15-C31-100130-IRA-FABRICATION-PROXY","symbol":"100130","company_name":"동국S&C","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","evidence_available_at_that_date":"IRA wind theme mapped only loosely to domestic tower/fabrication exposure; no contemporaneous durable order/revision bridge was visible.","evidence_source":"historical public law/event plus wind fabrication proxy classification; price rows from stock-web shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/100/100130/2022.csv","profile_path":"atlas/symbol_profiles/100/100130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-17","entry_price":7110,"MFE_30D_pct":9.0,"MFE_90D_pct":9.0,"MFE_180D_pct":9.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.75,"MAE_90D_pct":-31.01,"MAE_180D_pct":-37.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-25","peak_price":7750,"drawdown_after_peak_pct":-42.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_without_route_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L15-C31-100130-IRA-FABRICATION-PROXY|2022-08-17|7110","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L15-C31-389260-4B-20220901","case_id":"R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE","symbol":"389260","company_name":"대명에너지","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_WIND_ROUTE_CONGRUENCE_AND_POLICY_THEME_GUARD","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2022-09-01","evidence_available_at_that_date":"Price/volume blowoff after policy theme repricing; no new durable non-price 4B evidence beyond positioning/valuation heat.","evidence_source":"historical public law/event plus developer policy-beta route; price rows from stock-web shard","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/389/389260/2022.csv","profile_path":"atlas/symbol_profiles/389/389260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-09-01","entry_price":35100,"MFE_30D_pct":5.41,"MFE_90D_pct":5.41,"MFE_180D_pct":5.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-39.46,"MAE_90D_pct":-43.45,"MAE_180D_pct":-53.7,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-09-01","peak_price":37000,"drawdown_after_peak_pct":-56.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"good_local_4B_watch_but_price_only_not_full_exit","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE|2022-09-01|35100","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case used only for 4B overlay timing audit; not counted as new aggregate case","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L15-C31-112610-IRA-WIND-TOWER","trigger_id":"R11L15-C31-112610-S2A-20220816","symbol":"112610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"route_congruence_score":4,"policy_theme_purity_score":8,"positioning_overheat_score":4,"thesis_break_score":0},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"route_congruence_score":9,"policy_theme_purity_score":8,"positioning_overheat_score":4,"thesis_break_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green","changed_components":["route_congruence_score","policy_theme_supplier_guard","positioning_overheat_score"],"component_delta_explanation":"After profile rewards direct policy-to-revenue route and penalizes loose supplier/theme proxy without order/revision bridge.","MFE_90D_pct":26.57,"MAE_90D_pct":-10.85,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L15-C31-389260-IRA-DEVELOPER-HIGHMAE","trigger_id":"R11L15-C31-389260-S2A-20220816","symbol":"389260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":9,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"route_congruence_score":5,"policy_theme_purity_score":7,"positioning_overheat_score":8,"thesis_break_score":2},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":9,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"route_congruence_score":5,"policy_theme_purity_score":7,"positioning_overheat_score":10,"thesis_break_score":2},"weighted_score_after":80.0,"stage_label_after":"Stage3-Yellow+4B-watch","changed_components":["route_congruence_score","policy_theme_supplier_guard","positioning_overheat_score"],"component_delta_explanation":"After profile rewards direct policy-to-revenue route and penalizes loose supplier/theme proxy without order/revision bridge.","MFE_90D_pct":39.89,"MAE_90D_pct":-24.95,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L15-C31-297090-IRA-BEARING-PROXY","trigger_id":"R11L15-C31-297090-S2A-20220816","symbol":"297090","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":9,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"route_congruence_score":6,"policy_theme_purity_score":4,"positioning_overheat_score":7,"thesis_break_score":6},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":9,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"route_congruence_score":3,"policy_theme_purity_score":4,"positioning_overheat_score":7,"thesis_break_score":6},"weighted_score_after":69.0,"stage_label_after":"Stage2-watch","changed_components":["route_congruence_score","policy_theme_supplier_guard","positioning_overheat_score"],"component_delta_explanation":"After profile rewards direct policy-to-revenue route and penalizes loose supplier/theme proxy without order/revision bridge.","MFE_90D_pct":15.72,"MAE_90D_pct":-38.78,"score_return_alignment_label":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L15-C31-100130-IRA-FABRICATION-PROXY","trigger_id":"R11L15-C31-100130-S2A-20220816","symbol":"100130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":9,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"route_congruence_score":5,"policy_theme_purity_score":4,"positioning_overheat_score":4,"thesis_break_score":6},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable/Yellow-border","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":9,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"route_congruence_score":2,"policy_theme_purity_score":4,"positioning_overheat_score":4,"thesis_break_score":6},"weighted_score_after":63.0,"stage_label_after":"Stage2-watch","changed_components":["route_congruence_score","policy_theme_supplier_guard","positioning_overheat_score"],"component_delta_explanation":"After profile rewards direct policy-to-revenue route and penalizes loose supplier/theme proxy without order/revision bridge.","MFE_90D_pct":9.0,"MAE_90D_pct":-31.01,"score_return_alignment_label":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R11","loop":"15","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","scheduled_round":"R11","scheduled_loop":15,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R11L15-C31-018000-UNISON-BLOCKED-20240521","symbol":"018000","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"유니슨은 풍력 정책 테마에 자주 연결되지만 symbol profile has corporate_action_candidate_date 2024-05-21, so nearby 2024 policy-theme windows are blocked for weight calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_route_congruence_score,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Direct policy-to-revenue route separates 112610 success from loose supplier proxies","Improves false-positive filtering while preserving direct-route winner","R11L15-C31-112610-S2A-20220816|R11L15-C31-297090-S2A-20220816|R11L15-C31-100130-S2A-20220816",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_policy_theme_supplier_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Loose wind supplier/fabrication proxy without visible order/revision bridge caused high MAE","Blocks policy-only promotion for 297090 and 100130","R11L15-C31-297090-S2A-20220816|R11L15-C31-100130-S2A-20220816",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_price_only_local_4b_watch,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Early policy event blowoff can mark local risk but not full thesis-break 4B without non-price evidence","Adds 4B watch for 389260 high-MAE success","R11L15-C31-389260-4B-20220901",1,0,0,low,overlay_shadow_only,"4B overlay only; not positive-stage promotion"
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 15
next_round = R12
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes


- Manifest check: `atlas/manifest.json` reports source `FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, calibration root `atlas/ohlcv_tradable_by_symbol_year`, raw root `atlas/ohlcv_raw_by_symbol_year`, and zero-volume/corporate-action caveats.
- Schema check: `atlas/schema.json` confirms tradable shard columns `d,o,h,l,c,v,a,mc,s,m` and MFE/MAE definitions over tradable rows.
- Universe check: `atlas/universe/all_symbols.csv` is present and maps codes to profile paths.
- Symbol profile checks:
  - `112610`: no 2022~2023 corporate-action window overlap; tradable rows available through 2026-02-20.
  - `389260`: no corporate-action candidate dates; tradable rows available through 2026-02-20.
  - `297090`: 2022-07 corporate-action candidates predate entry; no 2022-08-17~180D overlap.
  - `100130`: no corporate-action candidates.
  - `018000`: corporate-action candidate date 2024-05-21, so a later wind-policy narrative was left narrative-only.

