# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only
scheduled_round = R9
scheduled_loop = 73
completed_round = R9
completed_loop = 73
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION
output_file = e2r_stock_web_v12_residual_round_R9_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.


## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`. Rollback reference: `e2r_2_0_baseline_reference`.

This MD does not re-prove the global Stage2 bonus or Green lateness rule. It tests a narrower C14 residual: generic EV slowdown, cathode ASP pressure, or separator utilization risk can be a real 4B/4C guardrail, but it becomes a trap if it mechanically demotes names that still have named customer/orderbook, policy localization, or capacity-route evidence. The rule should behave like a circuit breaker with a fuse label, not like a darkness switch for the whole EV shelf.

| existing calibrated axis | status | C14 interpretation |
|---|---|---|
| stage2_actionable_evidence_bonus | existing_axis_tested | still useful when named customer/orderbook or policy capacity evidence is intact |
| stage3_yellow_total_min | existing_axis_kept | threshold can stay; composition must change |
| stage3_green_total_min / revision_min | existing_axis_kept | no global weakening proposed |
| price_only_blowoff_blocks_positive_stage | existing_axis_strengthened | battery/materials blowoff without ASP/utilization repair should remain blocked |
| full_4b_requires_non_price_evidence | existing_axis_strengthened | full 4B/4C requires non-price slowdown evidence, not just a local high |
| hard_4c_thesis_break_routes_to_4c | existing_axis_strengthened | hard 4C should fire when company-specific call-off/utilization/ASP break appears; generic sector headlines alone are too broad |


## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 73 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C |
| fine_archetype_id | EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION |
| round_sector_consistency | pass |
| loop_objective | 4C_thesis_break_timing_test; 4B_non_price_requirement_stress_test; residual_false_positive_mining; residual_missed_structural_mining; sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill |

R9 is treated as the mobility/EV residual round, so `L3_BATTERY_EV_GREEN_MOBILITY` is valid. The selected C14 scope is not a current-stock scan and not a battery recommendation list. It is a historical stress test of when EV slowdown should block positive stages and when a company-specific exception should survive.


## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 outputs show loop 73 completed through R8. Existing R9 loop 71/72 already covered C29 mobility operating leverage, including auto OEMs, suppliers, and tires. This run therefore fills R9/loop 73 with C14 rather than rematerializing C29.

```text
scheduled_round = R9
scheduled_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

Duplicate-risk check:

| duplicate component | result |
|---|---|
| same canonical_archetype_id | allowed and useful |
| exact C14 symbol + trigger_type + entry_date duplicate | none |
| reused case table | none |
| reused symbol with new trigger family | 247540 only, independent because trigger date/family differs from prior C14 row |
| schema rematerialization | no |


## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest was read for this run.

|field|value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```


## 5. Historical Eligibility Gate

| symbol | company | profile_path | status | corporate-action window | 180D usable |
|---:|---|---|---|---|---|
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | active_like / tradable_ohlcv | candidate dates outside selected 180D window | true |
| 393890 | 더블유씨피 | atlas/symbol_profiles/393/393890.json | active_like / tradable_ohlcv | no candidate dates in selected window | true |
| 003670 | 포스코퓨처엠 | atlas/symbol_profiles/003/003670.json | active_like / tradable_ohlcv | candidates outside 2023 selected 180D window | true |
| 348370 | 엔켐 | atlas/symbol_profiles/348/348370.json | active_like / tradable_ohlcv | no candidate dates | true |

All representative entries exist in tradable shards and have at least 180 forward trading rows before the manifest max date. No representative row is used if the 180D corporate-action window is contaminated.


## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C

fine_archetype compression:
- company_specific_calloff_ASP_utilization_break -> C14
- separator_capacity_customer_concentration_break -> C14
- generic_EV_slowdown_headline_only -> C14 watch-only, not hard 4C
- policy_localization_named_orderbook_exception -> C14 exception guard
```

The compression thesis: C14 is not “EV down, therefore sell/demote.” It is a split between broken evidence and still-intact evidence. Hard 4C is valid when the thesis gearbox loses teeth: call-off, ASP, utilization, or customer-quality evidence breaks. It is too blunt when the company still has policy, customer, capacity, or orderbook proof.


## 7. Case Selection Summary

|case_id|symbol|company|role|positive/counter|trigger family|entry|MFE90|MAE90|MFE180|MAE180|current verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS|247540|에코프로비엠|4C_success|positive|contract_size_without_ASP_utilization_after_sector_blowoff|2023-12-04|9.6|-34.67|9.6|-53.97|current_profile_false_positive|
|R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS|393890|더블유씨피|4C_success|positive|separator_capacity_theme_customer_concentration_utilization_break|2024-01-05|1.94|-38.78|1.94|-45.71|current_profile_false_positive|
|R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK|003670|포스코퓨처엠|missed_structural|counterexample|named_customer_orderbook_policy_exception_to_generic_EV_slowdown|2023-01-31|88.62|-5.58|209.82|-5.58|current_profile_missed_structural|
|R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK|348370|엔켐|missed_structural|counterexample|policy_localization_capacity_relative_strength_exception_to_generic_EV_slowdown|2024-01-10|347.28|-2.27|347.28|-2.27|current_profile_4C_too_early|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 4
4C_case_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
representative_trigger_count = 4
```

Here, “positive” means positive evidence for the C14 guardrail, not a bullish stock call. 247540 and 393890 are positive guardrail cases because 4C/watch protection would have prevented large forward drawdowns. 003670 and 348370 are counterexamples because generic EV slowdown would have broken a still-valid structural route too early.


## 9. Evidence Source Map

| evidence family | C14 hard-4C success rows | C14 false-break exception rows |
|---|---|---|
| public_event_or_disclosure | present but not sufficient | present with named customer/orderbook or policy route |
| customer_or_order_quality | weak or deteriorating | stronger / named / policy-reinforced |
| capacity_or_volume_route | capacity theme can fail if utilization weakens | capacity route can be positive if backed by localization/customer evidence |
| margin_bridge | broken or unproven | intact enough at trigger |
| ASP/utilization | broken or missing | not yet broken at trigger |
| policy_or_regulatory_optionality | insufficient alone | can support exception if tied to supply route |
| thesis_evidence_broken | hard 4C/watch | false break if not yet present |


## 10. Price Data Source Map

|symbol|tradable shard|profile|
|---|---|---|
|247540|atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv|atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv|atlas/symbol_profiles/247/247540.json|
|393890|atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv|atlas/symbol_profiles/393/393890.json|
|003670|atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv|atlas/symbol_profiles/003/003670.json|
|348370|atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv|atlas/symbol_profiles/348/348370.json|


## 11. Case-by-Case Trigger Grid

|case_id|symbol|company|role|positive/counter|trigger family|entry|MFE90|MAE90|MFE180|MAE180|current verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS|247540|에코프로비엠|4C_success|positive|contract_size_without_ASP_utilization_after_sector_blowoff|2023-12-04|9.6|-34.67|9.6|-53.97|current_profile_false_positive|
|R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS|393890|더블유씨피|4C_success|positive|separator_capacity_theme_customer_concentration_utilization_break|2024-01-05|1.94|-38.78|1.94|-45.71|current_profile_false_positive|
|R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK|003670|포스코퓨처엠|missed_structural|counterexample|named_customer_orderbook_policy_exception_to_generic_EV_slowdown|2023-01-31|88.62|-5.58|209.82|-5.58|current_profile_missed_structural|
|R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK|348370|엔켐|missed_structural|counterexample|policy_localization_capacity_relative_strength_exception_to_generic_EV_slowdown|2024-01-10|347.28|-2.27|347.28|-2.27|current_profile_4C_too_early|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|symbol|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|T_R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS|247540|2023-12-04|323000|9.6|-13.0|9.6|-34.67|9.6|-53.97|2023-12-04|354000|-58.0|
|T_R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS|393890|2024-01-05|49000|1.94|-21.84|1.94|-38.78|1.94|-45.71|2024-01-08|49950|-46.75|
|T_R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK|003670|2023-01-31|224000|22.77|-5.58|88.62|-5.58|209.82|-5.58|2023-07-26|694000|-66.5|
|T_R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK|348370|2024-01-10|88200|283.22|-2.27|347.28|-2.27|347.28|-2.27|2024-04-08|394500|-54.75|

Representative rows are deduped for aggregate metrics. No overlay-only row is counted as a separate independent case in this MD.


## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| How would current profile judge these cases? | It would handle generic Stage2/4B rules but does not fully split C14 hard-break evidence from policy/orderbook exceptions. |
| Did that align with MFE/MAE? | Mixed: 247540/393890 needed a harder guard; 003670/348370 needed an exception to avoid false-break. |
| Was Stage2 bonus too strong? | Too strong for 247540/393890, not strong enough for 003670/348370 if a generic C14 penalty dominates. |
| Was Yellow 75 too strict/loose? | Composition matters more than the threshold. |
| Was Green 87 / revision 55 too strict/loose? | Kept. The rule proposal is not a Green threshold change. |
| Was price-only blowoff guard appropriate? | Yes, strengthened around 247540/393890. |
| Was full 4B non-price requirement appropriate? | Yes, strengthened. |
| Was hard 4C too late or too early? | Both can happen: too late without ASP/utilization break, too early if generic EV slowdown overrides named policy/orderbook evidence. |


## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2/Actionable entry | Stage3/Green issue | green_lateness_ratio |
|---:|---|---|---|
| 247540 | watch/demotion should replace positive Stage2 | no clean Green in window | not_applicable |
| 393890 | watch/demotion should replace positive Stage2 | no clean Green in window | not_applicable |
| 003670 | Stage2 should survive generic EV slowdown because named orderbook was intact | Green later would still work, but Stage2 captured most upside | approx 0.22 from prior C11 audit |
| 348370 | Stage2 should survive generic slowdown because policy/capacity/RS evidence was intact | Green after price repricing would be materially late | approx 0.41 from prior C11 audit |

The audit confirms the residual is not “lower Green thresholds.” It is “do not let a C14 slowdown guard erase a still-valid company-specific bridge.”


## 15. 4B Local vs Full-window Timing Audit

| symbol | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 247540 | 0.98 | 0.98 | good full-window 4B/4C timing when margin/ASP bridge is broken |
| 393890 | 0.30 | 0.30 | early warning only; full guard requires utilization/margin evidence |
| 003670 | 0.715 | 0.715 | 4B works near later blowoff, but would be false if used at initial Stage2 entry |
| 348370 | 0.86 | 0.86 | 4B works after overheat, not before policy/capacity exception expires |

This split is the core C14 finding. Full 4B/4C should be evidence-driven. A price-only or sector-only local high is just a shadow on the dashboard; non-price break evidence is the oil-pressure warning.


## 16. 4C Protection Audit

| symbol | four_c_protection_label | interpretation |
|---:|---|---|
| 247540 | hard_4c_success_after_margin_bridge_break | 4C/watch protected against a >50% 180D drawdown after a weak contract-size trigger. |
| 393890 | hard_4c_success_after_utilization_break | capacity/orderbook theme needed utilization/customer proof; without it, MAE dominated. |
| 003670 | false_break_if_generic_slowdown_used_before_orderbook_thesis_break | hard 4C before named orderbook thesis break would have missed a >200% 180D MFE. |
| 348370 | false_break_if_generic_slowdown_used_before_policy_capacity_exception_expires | generic slowdown would have blocked a high-MFE policy/capacity path. |


## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = C14_policy_orderbook_exception_guard
proposal = If generic EV slowdown evidence appears but named customer/orderbook, policy localization, or capacity-route evidence remains intact, route to 4B-watch or Stage2 exception, not hard 4C.
```

This is not a bullish override. It is a false-break guard. The exception expires once call-off, ASP, utilization, or thesis-break evidence appears.


## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C14_company_specific_calloff_utilization_required
proposal = Hard 4C in C14 requires company-specific call-off/order cut, ASP/margin break, utilization collapse, qualification/customer evidence break, or repeated financial visibility deterioration.
```

Generic EV slowdown headlines can support watch/4B, but not hard 4C by themselves.


## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current|global profile without C14 split|4|all 4 representative triggers|111.86|-20.32|142.16|-26.88|0.50|2|mixed; false positives and false breaks coexist|
|P0b e2r_2_0_baseline_reference|rollback|pre-stock-web reference|4|all 4 representative triggers|111.86|-20.32|142.16|-26.88|0.50|2|inferior; lacks current hard-4C discipline|
|P1 sector_specific_candidate_profile|sector_specific|require company-specific call-off/utilization for hard 4C|4|247540/393890 demoted; 003670/348370 exception|111.86|-20.32|142.16|-26.88|0.00|0|improved guard/exception split|
|P2 canonical_archetype_candidate_profile|canonical_specific|C14 split: hard break vs policy/orderbook exception|4|all 4 with C14 composition rules|111.86|-20.32|142.16|-26.88|0.00|0|best explanatory alignment|
|P3 counterexample_guard_profile|guard|hard 4C blocked if named customer/policy bridge intact|2|003670/348370 only|217.95|-3.92|278.55|-3.92|0.00|0|reduces false-break risk|


## 20. Score-Return Alignment Matrix

| symbol | current verdict | MFE90 | MAE90 | MFE180 | MAE180 | alignment repair |
|---:|---|---:|---:|---:|---:|---|
| 247540 | current_profile_false_positive | 9.60 | -34.67 | 9.60 | -53.97 | demote contract-size trigger without ASP/utilization repair |
| 393890 | current_profile_false_positive | 1.94 | -38.78 | 1.94 | -45.71 | demote separator capacity theme without utilization/customer proof |
| 003670 | current_profile_missed_structural | 88.62 | -5.58 | 209.82 | -5.58 | allow named orderbook exception before thesis break |
| 348370 | current_profile_4C_too_early | 347.28 | -2.27 | 347.28 | -2.27 | allow policy/capacity exception before overheat/break evidence |


## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C14_EV_DEMAND_SLOWDOWN_4B_4C|EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION|2|2|4|4|4|0|4|4|4|True|True|more separator/electrolyte/cathode holdout useful, but loop minimum satisfied|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: residual_false_positive_mining, residual_missed_structural_mining, 4C_too_early_false_break, hard_4C_success_after_utilization_break
new_axis_proposed: C14_company_specific_calloff_utilization_required; C14_policy_orderbook_exception_guard
existing_axis_strengthened: hard_4c_thesis_break_routes_to_4c; full_4b_requires_non_price_evidence; price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```


## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical 1D OHLC rows from Songdaiki/stock-web tradable shards.
- Representative trigger rows with clean 180D windows.
- C14-specific 4B/4C timing and Stage2 false-break stress test.
- Shadow-only sector/canonical rule candidates.

Non-validation scope:

- No live candidate discovery.
- No investment recommendation.
- No stock_agent source-code inspection.
- No production scoring change.
- No broker/API/auto-trading action.


## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_company_specific_calloff_utilization_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Generic EV slowdown should become hard 4C only with company-specific call-off, ASP, utilization, or thesis-break evidence","Blocks 247540/393890 false positives while preserving non-price evidence requirement","T_R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS|T_R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C14_policy_orderbook_exception_guard,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Named customer/orderbook or policy-localized capacity route should prevent premature hard 4C from generic slowdown headlines","Prevents missed-structural false breaks in 003670/348370","T_R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK|T_R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK",4,4,2,low_to_medium,sector_shadow_only,"not production; exception requires non-price bridge"
```


## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS", "symbol": "247540", "company_name": "에코프로비엠", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "Stage4C-Watch/Stage2-Demotion", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Same symbol appeared in earlier C14 with a later 2024 trigger, but this is a different 2023 orderbook-without-margin trigger family; it is not the same entry group."}
{"row_type": "case", "case_id": "R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS", "symbol": "393890", "company_name": "더블유씨피", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "Stage4C-Watch/Stage2-Demotion", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "New C14 symbol in the local v12 ledger; the clean 180D path supports a company-specific utilization/call-off guard."}
{"row_type": "case", "case_id": "R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION", "case_type": "missed_structural", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable/Anti-4C-Exception", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "exception_needed_before_demote", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Uses the same stock-web row set previously validated under C11, but this MD tests the opposite C14 failure mode: hard 4C too early when named orderbook evidence is still intact."}
{"row_type": "case", "case_id": "R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK", "symbol": "348370", "company_name": "엔켐", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION", "case_type": "missed_structural", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable/Policy-Capacity-Exception", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "exception_needed_before_demote", "current_profile_verdict": "current_profile_4C_too_early", "price_source": "Songdaiki/stock-web", "notes": "New C14 symbol in the local v12 ledger; the path tests a slowdown false-break rather than another orderbook promotion proof."}
{"row_type": "trigger", "trigger_id": "T_R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS", "case_id": "R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS", "symbol": "247540", "company_name": "에코프로비엠", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown 4B/4C split with company-specific call-off versus policy/orderbook exception", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C-Watch/Stage2-Demotion", "trigger_date": "2023-12-01", "entry_date": "2023-12-04", "entry_price": 323000, "evidence_available_at_that_date": "Long-term supply/orderbook headline was visible, but after the 2023 battery blowoff the non-price margin/ASP/utilization bridge was broken; C14 should block positive rerating unless customer call-off or utilization evidence repairs.", "evidence_source": "historical public disclosure/news proxy; stock-web OHLC rows previously validated from listed shards; no live candidate discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv|atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.6, "MFE_90D_pct": 9.6, "MFE_180D_pct": 9.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.0, "MAE_90D_pct": -34.67, "MAE_180D_pct": -53.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-04", "peak_price": 354000, "drawdown_after_peak_pct": -58.0, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_with_non_price_margin_guard", "four_b_evidence_type": "valuation_blowoff|positioning_overheat|margin_or_backlog_slowdown", "four_c_protection_label": "hard_4c_success_after_margin_bridge_break", "trigger_outcome_label": "hard_4c_success_contract_size_false_positive_blocked", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L73_C14_247540_2023-12-04_323000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS", "case_id": "R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS", "symbol": "393890", "company_name": "더블유씨피", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown 4B/4C split with company-specific call-off versus policy/orderbook exception", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C-Watch/Stage2-Demotion", "trigger_date": "2024-01-05", "entry_date": "2024-01-05", "entry_price": 49000, "evidence_available_at_that_date": "Separator capacity/orderbook narrative existed, but customer concentration, utilization risk and EV demand slowdown made it unlike a named high-quality rerating route.", "evidence_source": "historical public disclosure/news proxy; stock-web OHLC rows previously validated from listed shards; no live candidate discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "backlog_or_delivery_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.94, "MFE_90D_pct": 1.94, "MFE_180D_pct": 1.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.84, "MAE_90D_pct": -38.78, "MAE_180D_pct": -45.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-08", "peak_price": 49950, "drawdown_after_peak_pct": -46.75, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "early_warning_not_full_4B_until_utilization_margin_evidence", "four_b_evidence_type": "margin_or_backlog_slowdown|positioning_overheat", "four_c_protection_label": "hard_4c_success_after_utilization_break", "trigger_outcome_label": "hard_4c_success_capacity_theme_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L73_C14_393890_2024-01-05_49000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK", "case_id": "R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown 4B/4C split with company-specific call-off versus policy/orderbook exception", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable/Anti-4C-Exception", "trigger_date": "2023-01-30", "entry_date": "2023-01-31", "entry_price": 224000, "evidence_available_at_that_date": "Named customer/orderbook and delivery visibility preceded the 2023 cathode rerating. A generic EV slowdown or materials de-rating guard would have been too blunt before the margin/orderbook bridge cracked.", "evidence_source": "historical public disclosure/news proxy; stock-web OHLC rows previously validated from listed shards; no live candidate discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.77, "MFE_90D_pct": 88.62, "MFE_180D_pct": 209.82, "MFE_1Y_pct": 209.82, "MFE_2Y_pct": null, "MAE_30D_pct": -5.58, "MAE_90D_pct": -5.58, "MAE_180D_pct": -5.58, "MAE_1Y_pct": -66.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.5, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.715, "four_b_full_window_peak_proximity": 0.715, "four_b_timing_verdict": "good_full_window_4B_timing_only_after_non_price_overheat", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "false_break_if_generic_slowdown_used_before_orderbook_thesis_break", "trigger_outcome_label": "generic_EV_slowdown_false_break_missed_structural", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L73_C14_003670_2023-01-31_224000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK", "case_id": "R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK", "symbol": "348370", "company_name": "엔켐", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_COMPANY_SPECIFIC_CALLOFF_VS_POLICY_ORDERBOOK_EXCEPTION", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown 4B/4C split with company-specific call-off versus policy/orderbook exception", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable/Policy-Capacity-Exception", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 88200, "evidence_available_at_that_date": "Electrolyte supply-chain rerating, US localization/policy option and relative strength created an exception to generic EV slowdown hard-4C routing before later overheat risk emerged.", "evidence_source": "historical public disclosure/news proxy; stock-web OHLC rows previously validated from listed shards; no live candidate discovery", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "profile_path": "atlas/symbol_profiles/348/348370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 283.22, "MFE_90D_pct": 347.28, "MFE_180D_pct": 347.28, "MFE_1Y_pct": 347.28, "MFE_2Y_pct": null, "MAE_30D_pct": -2.27, "MAE_90D_pct": -2.27, "MAE_180D_pct": -2.27, "MAE_1Y_pct": -10.2, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-04-08", "peak_price": 394500, "drawdown_after_peak_pct": -54.75, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_overheat_present", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "false_break_if_generic_slowdown_used_before_policy_capacity_exception_expires", "trigger_outcome_label": "generic_EV_slowdown_false_break_policy_capacity_exception", "current_profile_verdict": "current_profile_4C_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L73_C14_348370_2024-01-10_88200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS", "trigger_id": "T_R9L73_C14_247540_20231204_ORDERBOOK_WITHOUT_MARGIN_4C_SUCCESS", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 45, "margin_bridge_score": 18, "revision_score": 15, "relative_strength_score": 25, "customer_quality_score": 35, "policy_or_regulatory_score": 30, "valuation_repricing_score": 35, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable-false-positive-risk", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 25, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 72, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 5, "utilization_score": 10, "thesis_break_score": 70}, "weighted_score_after": 62, "stage_label_after": "Stage4C-Watch/positive-blocked", "changed_components": ["margin_bridge_score", "execution_risk_score", "asp_or_spread_score", "utilization_score", "thesis_break_score", "policy_or_regulatory_score"], "component_delta_explanation": "C14 shadow guard demotes contract/capacity evidence when ASP, utilization, and customer call-off risk are broken.", "MFE_90D_pct": 9.6, "MAE_90D_pct": -34.67, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS", "trigger_id": "T_R9L73_C14_393890_20240105_SEPARATOR_UTILIZATION_4C_SUCCESS", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 45, "margin_bridge_score": 18, "revision_score": 15, "relative_strength_score": 25, "customer_quality_score": 35, "policy_or_regulatory_score": 30, "valuation_repricing_score": 35, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable-false-positive-risk", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 15, "customer_quality_score": 25, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 72, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 5, "utilization_score": 10, "thesis_break_score": 70}, "weighted_score_after": 62, "stage_label_after": "Stage4C-Watch/positive-blocked", "changed_components": ["margin_bridge_score", "execution_risk_score", "asp_or_spread_score", "utilization_score", "thesis_break_score", "policy_or_regulatory_score"], "component_delta_explanation": "C14 shadow guard demotes contract/capacity evidence when ASP, utilization, and customer call-off risk are broken.", "MFE_90D_pct": 1.94, "MAE_90D_pct": -38.78, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK", "trigger_id": "T_R9L73_C14_003670_20230131_POLICY_ORDERBOOK_EXCEPTION_FALSE_BREAK", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 60, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 65, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable/4C-risk", "raw_component_scores_after": {"contract_score": 68, "backlog_visibility_score": 70, "margin_bridge_score": 45, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 75, "valuation_repricing_score": 48, "execution_risk_score": 32, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 75, "asp_or_spread_score": 45, "utilization_score": 42, "thesis_break_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow-or-Green-exception", "changed_components": ["margin_bridge_score", "execution_risk_score", "asp_or_spread_score", "utilization_score", "thesis_break_score", "policy_or_regulatory_score"], "component_delta_explanation": "C14 shadow exception prevents generic EV slowdown from overriding named orderbook, policy localization, or capacity evidence before thesis break.", "MFE_90D_pct": 88.62, "MAE_90D_pct": -5.58, "score_return_alignment_label": "exception_needed_before_demote", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK", "trigger_id": "T_R9L73_C14_348370_20240110_POLICY_CAPACITY_EXCEPTION_FALSE_BREAK", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 60, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 65, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable/4C-risk", "raw_component_scores_after": {"contract_score": 68, "backlog_visibility_score": 70, "margin_bridge_score": 45, "revision_score": 35, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 75, "valuation_repricing_score": 48, "execution_risk_score": 32, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 75, "asp_or_spread_score": 45, "utilization_score": 42, "thesis_break_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow-or-Green-exception", "changed_components": ["margin_bridge_score", "execution_risk_score", "asp_or_spread_score", "utilization_score", "thesis_break_score", "policy_or_regulatory_score"], "component_delta_explanation": "C14 shadow exception prevents generic EV slowdown from overriding named orderbook, policy localization, or capacity evidence before thesis break.", "MFE_90D_pct": 347.28, "MAE_90D_pct": -2.27, "score_return_alignment_label": "exception_needed_before_demote", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "residual_contribution", "round": "R9", "loop": "73", "scheduled_round": "R9", "scheduled_loop": 73, "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["residual_false_positive_mining", "residual_missed_structural_mining", "4C_too_early_false_break", "hard_4C_success_after_utilization_break"], "diversity_score_summary": "new_symbols=3; same_archetype_new_trigger_family=4; counterexamples=2; residual_errors=4; wrong_round_penalty=0; duplicate_key_conflict=0; new_independent_case_ratio=1.00", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R9
completed_loop = 73
next_round = R10
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```


## 28. Source Notes

- `Songdaiki/stock-web/atlas/manifest.json` was used for manifest max date and shard roots.
- `Songdaiki/stock-web/atlas/schema.json` defines raw and tradable shard columns and calibration usability rules.
- Stock-Web price basis is `tradable_raw`; price adjustment status is `raw_unadjusted_marcap`.
- Quantitative rows reference these tradable shard paths: `247/247540/2023.csv`, `247/247540/2024.csv`, `393/393890/2024.csv`, `003/003670/2023.csv`, `348/348370/2024.csv`.
- Local duplicate scan used existing v12 files in `/mnt/data` only as research artifact / duplicate-avoidance context, not as stock_agent source code.

