# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R11_loop_93_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

This file is the corrected final output for this execution. The scheduler state after R10 loop 93 is R11 / loop 93. R11 allows policy/event cross-sector routing; this run uses L10 and fills C31 policy/subsidy/legislation event behavior.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 93
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_sector_consistency = pass
computed_next_round = R12
computed_next_loop = 93
```

C31 is vulnerable to label error. The word "policy" often behaves like a bright signboard: it pulls attention before the cash register exists. This loop asks whether the policy label has a working bridge into revenue, budget, tariff, funding, legal clarity, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT = 97 rows / 70 symbols / good-bad Stage2 35-25 / 4B-4C 5-0
top covered symbols include 013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
previous R11 loop-88 C31 symbols avoided: 036460, 053290, 057030
previous R11 loop-89 C03 symbols avoided: 064350, 010820, 099320
previous R11 loop-90 C05 symbols avoided: 047040, 028050, 052690
previous R11 loop-91 C03 symbols avoided: 012450, 214430, 013810
previous R11 loop-92 C04 symbols avoided: 051600, 046120, 006910
previous R10 loop-93 C30 symbols avoided: 012630, 001840, 025950
```

Selected rows avoid hard duplicates and top repeated C31 symbols:

```text
130660 / Stage2-Actionable / 2024-04-26
105840 / Stage2-Actionable / 2024-01-24
034300 / Stage4B / 2024-05-29
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 130660 | atlas/symbol_profiles/130/130660.json | no corporate-action candidate |
| 105840 | atlas/symbol_profiles/105/105840.json | selected 2024 window clean after old 2012 CA candidates |
| 034300 | atlas/symbol_profiles/034/034300.json | selected 2024 entry after 2024-02-06 CA candidate; inactive-like caveat |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R11L93_C31_KEPCOINDUSTRIAL_2024_POWER_POLICY_O_AND_M_TARIFF_BRIDGE_POSITIVE | 130660 | 2024-04-26 | yes | 180 | yes | yes | true |
| R11L93_C31_WOOJIN_2024_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2 | 105840 | 2024-01-24 | yes | 180 | yes | yes | true |
| R11L93_C31_SHINSEGAECONST_2024_RESTRUCTURING_POLICY_EVENT_CAP_4B | 034300 | 2024-05-29 | yes | 180 | yes | caveated | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POWER_POLICY_O_AND_M_TARIFF_BRIDGE | Positive Stage2 requires policy-to-revenue mechanics, O&M/service revenue, tariff/capacity visibility, order quality, margin and revision bridge. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2 | Nuclear/policy headline without order, budget, tariff, margin or revision bridge can become false Stage2. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | RESTRUCTURING_POLICY_EVENT_CAP_4B | Restructuring or policy-support premium should route to 4B when funding/legal/balance bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R11L93_C31_KEPCOINDUSTRIAL_2024_POWER_POLICY_O_AND_M_TARIFF_BRIDGE_POSITIVE | 130660 | 한전산업 | positive | Power policy translated into O&M/service revenue and tariff/capacity bridge; MFE was very large. |
| R11L93_C31_WOOJIN_2024_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2 | 105840 | 우진 | counterexample | Nuclear-policy headline had low MFE and persistent MAE without budget/order bridge. |
| R11L93_C31_SHINSEGAECONST_2024_RESTRUCTURING_POLICY_EVENT_CAP_4B | 034300 | 신세계건설 | counterexample / 4B | Restructuring/policy-support premium capped after the late-May spike and then drew down. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| KEPCO Industrial power-policy O&M bridge | historical public/report proxy | true | true | shadow-only positive |
| Woojin nuclear-policy false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Shinsegae Construction restructuring event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 130660 | atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv | atlas/symbol_profiles/130/130660.json |
| 105840 | atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv | atlas/symbol_profiles/105/105840.json |
| 034300 | atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv | atlas/symbol_profiles/034/034300.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R11L93_C31_KEPCOINDUSTRIAL_2024_STAGE2_ACTIONABLE_POWER_POLICY_O_AND_M_TARIFF_BRIDGE | 130660 | Stage2-Actionable | 2024-04-26 | 7750 | positive | power-policy O&M/tariff bridge worked |
| R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE | 105840 | Stage2-Actionable | 2024-01-24 | 9090 | counterexample | nuclear-policy headline false Stage2 |
| R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP | 034300 | Stage4B | 2024-05-29 | 14700 | counterexample/4B | restructuring policy-support event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L93_C31_KEPCOINDUSTRIAL_2024_STAGE2_ACTIONABLE_POWER_POLICY_O_AND_M_TARIFF_BRIDGE | 7750 | 88.00 | -1.94 | 151.61 | -1.94 | 151.61 | -1.94 | 2024-07-18 | 19500 | -45.13 |
| R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE | 9090 | 0.77 | -11.44 | 3.63 | -15.07 | 3.63 | -22.33 | 2024-03-19 | 9420 | -30.15 |
| R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP | 14700 | 26.87 | -18.03 | 26.87 | -24.15 | 26.87 | -24.15 | 2024-05-30 | 18650 | -40.21 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C31 Stage2 needs policy-to-revenue / order-budget / tariff-subsidy / legal-funding / margin bridge. |
| local_4b_watch_guard | strengthen: bridge-missing policy/restructuring event premiums should route to 4B watch. |
| high_MAE_guardrail | strengthen: policy headline rows cannot promote when MFE is weak and MAE persists. |
| full_4b_requires_non_price_evidence | keep. |
| price_only_blowoff_blocks_positive_stage | keep. |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted. |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether policy becomes a measurable bridge or remains a headline.

| symbol | stage quality | explanation |
|---|---|---|
| 130660 | good_stage2_with_later_watch | Policy translated into O&M/service and tariff/capacity bridge; MFE was very high. |
| 105840 | bad_stage2 | Nuclear-policy headline did not carry order/budget/margin bridge; forward MFE was weak. |
| 034300 | good_4B | Restructuring/policy-support event premium capped near the late-May spike and then drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 105840 nuclear-policy false Stage2 | 0.97 | 0.97 | false Stage2 due missing order/budget/margin bridge |
| 034300 restructuring event cap | 0.79 | 0.79 | acceptable 4B timing after high-MAE confirmation; inactive-like profile caveat retained |
| 130660 power-policy bridge | n/a | n/a | positive Stage2, but later policy-event valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 105840 / 034300
```

No hard 4C candidate is proposed. R11 loop 93 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 policy/event cases, Stage2 requires verified policy-to-revenue mechanics, order/budget passage, tariff/subsidy mechanics, legal/funding clarity, customer visibility, margin, or revision bridge. Policy, subsidy, legislation, nuclear headline, public support, restructuring or value-up label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rule = C31 should split true policy-to-revenue positives from policy-headline false Stage2 and restructuring/policy-support event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 60.70 | -13.72 | 0.67 | mixed; C31 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 60.70 | -13.72 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L10 policy-to-revenue bridge required | 2 | 77.62 | -8.51 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C31 bridge vs event-cap split | 2 | 77.62 | -8.51 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing policy headlines as positive | 1 | 151.61 | -1.94 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 130660 power-policy O&M bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 151.61 | -1.94 | power_policy_O_and_M_tariff_bridge_positive |
| 105840 nuclear-policy false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 3.63 | -15.07 | nuclear_policy_headline_false_stage2 |
| 034300 restructuring cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 26.87 | -24.15 | restructuring_policy_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C31 power-policy O&M/tariff bridge positive, nuclear-policy headline false Stage2, and restructuring policy-support event-cap 4B split while avoiding top repeated C31 symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: power_policy_O_and_M_tariff_bridge_positive, nuclear_policy_headline_false_stage2, restructuring_policy_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C31 policy/subsidy/legislation event bridge vs false Stage2 / event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,C31_requires_policy_to_revenue_order_budget_tariff_margin_revision_bridge,0,"C31 Stage2 should require policy to revenue mechanics, order/budget passage, tariff/subsidy mechanics, customer visibility, funding/legal clarity, margin, or revision bridge, not policy headline alone","KEPCO Industrial positive worked; Woojin and Shinsegae Construction event/watch rows failed positive-stage promotion","R11L93_C31_KEPCOINDUSTRIAL_2024_STAGE2_ACTIONABLE_POWER_POLICY_O_AND_M_TARIFF_BRIDGE|R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE|R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,cap_bridge_missing_policy_headline_and_restructuring_event_premiums_as_4B_watch,0,"Policy/restructuring event premiums can peak before legal, budget, funding and margin bridge is proven","Woojin had low MFE after nuclear-policy headline; Shinsegae Construction showed 4B event-cap behavior after late-May restructuring spike","R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE|R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,block_positive_stage_when_policy_headline_has_high_or_persistent_MAE_without_bridge,0,"High or persistent MAE after bridge-missing policy entries should block Stage2/Stage3 promotion unless budget, order, legal/funding and margin evidence survives","Woojin MAE180=-22.33 and Shinsegae Construction MAE90=-24.15","R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE|R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L93_C31_KEPCOINDUSTRIAL_2024_POWER_POLICY_O_AND_M_TARIFF_BRIDGE_POSITIVE", "symbol": "130660", "company_name": "한전산업", "round": "R11", "loop": "93", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP", "case_type": "structural_success_with_later_policy_event_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L93_C31_KEPCOINDUSTRIAL_2024_STAGE2_ACTIONABLE_POWER_POLICY_O_AND_M_TARIFF_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Power-policy / O&M service / tariff-capacity bridge produced very high 30D/90D/180D MFE with shallow early MAE. C31 works when policy narrative maps into operating-service revenue, public-utility capex, tariff/capacity visibility, order quality, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C31_positive_requires_policy_to_revenue_OandM_tariff_margin_revision_bridge_not_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R11L93_C31_WOOJIN_2024_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2", "symbol": "105840", "company_name": "우진", "round": "R11", "loop": "93", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP", "case_type": "failed_rerating_policy_headline_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear-policy headline watch had near-zero forward MFE and persistent drawdown. C31 Stage2 should not be awarded without order award, budget passage, tariff/subsidy mechanics, customer visibility, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_nuclear_policy_headline_counts_without_order_budget_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2012 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R11L93_C31_SHINSEGAECONST_2024_RESTRUCTURING_POLICY_EVENT_CAP_4B", "symbol": "034300", "company_name": "신세계건설", "round": "R11", "loop": "93", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP", "case_type": "event_cap_4b_counterexample_after_post_CA_window", "positive_or_counterexample": "counterexample", "best_trigger": "R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Construction restructuring / policy-support event premium capped around the late-May spike and then drew down. C31 should route bridge-missing restructuring or policy-support premiums to 4B unless legally confirmed support, funding, balance repair, execution and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_restructuring_policy_support_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Entry is after 2024-02-06 corporate-action candidate; 2024 post-CA window reviewed as source-proxy only because profile later becomes inactive/delisted-like."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R11L93_C31_KEPCOINDUSTRIAL_2024_STAGE2_ACTIONABLE_POWER_POLICY_O_AND_M_TARIFF_BRIDGE", "case_id": "R11L93_C31_KEPCOINDUSTRIAL_2024_POWER_POLICY_O_AND_M_TARIFF_BRIDGE_POSITIVE", "symbol": "130660", "company_name": "한전산업", "round": "R11", "loop": "93", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP", "sector": "power_policy_O_and_M_tariff_capacity_service", "primary_archetype": "policy_to_revenue_O_and_M_tariff_capacity_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 7750.0, "evidence_available_at_that_date": "power policy, public utility O&M/service revenue, tariff/capacity visibility, order quality and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["policy_to_revenue_proxy", "O_and_M_service_revenue_proxy", "tariff_capacity_visibility_proxy", "public_utility_order_quality_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_policy_event_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv", "profile_path": "atlas/symbol_profiles/130/130660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 88.0, "MFE_90D_pct": 151.61, "MFE_180D_pct": 151.61, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.94, "MAE_90D_pct": -1.94, "MAE_180D_pct": -1.94, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 19500.0, "drawdown_after_peak_pct": -45.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_policy_event_valuation_4B_watch_needed", "four_b_evidence_type": ["policy_to_revenue_bridge", "valuation_repricing", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_power_policy_O_and_M_tariff_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R11L93_C31_130660_2024-04-26_7750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE", "case_id": "R11L93_C31_WOOJIN_2024_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2", "symbol": "105840", "company_name": "우진", "round": "R11", "loop": "93", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP", "sector": "nuclear_policy_headline_watch", "primary_archetype": "nuclear_policy_headline_without_order_budget_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 9090.0, "evidence_available_at_that_date": "nuclear policy headline / project expectation watch without confirmed order, budget, tariff or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_policy_headline", "project_expectation_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE30", "low_MFE90", "order_budget_margin_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv", "profile_path": "atlas/symbol_profiles/105/105840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.77, "MFE_90D_pct": 3.63, "MFE_180D_pct": 3.63, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.44, "MAE_90D_pct": -15.07, "MAE_180D_pct": -22.33, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-19", "peak_price": 9420.0, "drawdown_after_peak_pct": -30.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "nuclear_policy_headline_was_false_stage2_due_missing_order_budget_margin_revision_bridge", "four_b_evidence_type": ["policy_headline_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_nuclear_policy_headline_without_order_budget_bridge", "current_profile_verdict": "current_profile_false_positive_if_nuclear_policy_headline_counts_without_order_budget_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2012_CA", "same_entry_group_id": "R11L93_C31_105840_2024-01-24_9090", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP", "case_id": "R11L93_C31_SHINSEGAECONST_2024_RESTRUCTURING_POLICY_EVENT_CAP_4B", "symbol": "034300", "company_name": "신세계건설", "round": "R11", "loop": "93", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP", "sector": "construction_restructuring_policy_support_event_premium", "primary_archetype": "restructuring_policy_support_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-29", "entry_date": "2024-05-29", "entry_price": 14700.0, "evidence_available_at_that_date": "construction restructuring / policy-support event premium after late-May spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["restructuring_policy_support_event", "balance_repair_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "legal_funding_balance_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.87, "MFE_90D_pct": 26.87, "MFE_180D_pct": 26.87, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.03, "MAE_90D_pct": -24.15, "MAE_180D_pct": -24.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-30", "peak_price": 18650.0, "drawdown_after_peak_pct": -40.21, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.79, "four_b_full_window_peak_proximity": 0.79, "four_b_timing_verdict": "acceptable_4B_timing_restructuring_policy_event_cap_after_high_MAE_confirmation", "four_b_evidence_type": ["restructuring_policy_support_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_restructuring_policy_support_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_restructuring_policy_support_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2024-02-06_CA_candidate_but_inactive_like_profile_caveat", "same_entry_group_id": "R11L93_C31_034300_2024-05-29_14700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L93_C31_KEPCOINDUSTRIAL_2024_POWER_POLICY_O_AND_M_TARIFF_BRIDGE_POSITIVE", "trigger_id": "R11L93_C31_KEPCOINDUSTRIAL_2024_STAGE2_ACTIONABLE_POWER_POLICY_O_AND_M_TARIFF_BRIDGE", "symbol": "130660", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 70, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 55, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 45, "policy_or_regulatory_score": 75, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "power_policy_O_and_M_tariff_bridge_positive", "MFE_90D_pct": 151.61, "MAE_90D_pct": -1.94, "score_return_alignment_label": "power_policy_O_and_M_tariff_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L93_C31_WOOJIN_2024_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2", "trigger_id": "R11L93_C31_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_POLICY_HEADLINE", "symbol": "105840", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 70, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "nuclear_policy_headline_false_stage2", "MFE_90D_pct": 3.63, "MAE_90D_pct": -15.07, "score_return_alignment_label": "nuclear_policy_headline_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_nuclear_policy_headline_counts_without_order_budget_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L93_C31_SHINSEGAECONST_2024_RESTRUCTURING_POLICY_EVENT_CAP_4B", "trigger_id": "R11L93_C31_SHINSEGAECONST_2024_STAGE4B_RESTRUCTURING_POLICY_EVENT_CAP", "symbol": "034300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 70, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "restructuring_policy_event_cap_4B_guard", "MFE_90D_pct": 26.87, "MAE_90D_pct": -24.15, "score_return_alignment_label": "restructuring_policy_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_restructuring_policy_support_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "93", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POWER_POLICY_O_AND_M_TARIFF_BRIDGE_VS_NUCLEAR_POLICY_HEADLINE_FALSE_STAGE2_AND_RESTRUCTURING_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["power_policy_O_and_M_tariff_bridge_positive", "nuclear_policy_headline_false_stage2", "restructuring_policy_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C31 rows need explicit policy-to-revenue, budget/order, tariff/subsidy, legal/funding or margin bridge before positive promotion.
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
10. Add tests that bridge-missing C31 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 93
next_round = R12
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
