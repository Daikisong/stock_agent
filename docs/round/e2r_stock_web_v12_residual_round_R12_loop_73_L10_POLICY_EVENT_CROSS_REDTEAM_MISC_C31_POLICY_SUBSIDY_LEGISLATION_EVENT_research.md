# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R12
scheduled_loop: 73
completed_round: R12
completed_loop: 73
next_round: R13
next_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: IRA_DIRECT_SUBSIDY_ROUTE_VS_POLICY_THEME_FALSE_POSITIVE
loop_objective: "residual_false_positive_mining | residual_missed_structural_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill"
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

The research question is deliberately narrow: **when a policy/subsidy/legislation event becomes tradable, does the trigger-date evidence already show a company-specific conversion path, or is it only a label riding the same headline?** In C31, the policy headline is the spark; the direct subsidy/order/capacity route is the wick. Without the wick, the spark flashes and dies.

## 1. Current Calibrated Profile Assumption

Current default profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
```

Applied axes assumed active:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does **not** re-propose those global axes. It stress-tests them inside C31 and proposes only shadow sector/canonical refinements.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R12`
- scheduled_loop: `73`
- allowed R12 sector route used here: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`
- fine_archetype_id: `IRA_DIRECT_SUBSIDY_ROUTE_VS_POLICY_THEME_FALSE_POSITIVE`
- round_sector_consistency: `pass`

R12 is treated as a policy/event residual checkpoint rather than a live scan. The chosen C31 set is a historical cross-check of the U.S. clean-energy policy event family around July/August 2022.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact access was used only for duplicate avoidance and schedule sanity. No `src/e2r` code was opened. The currently accessible `md_registry.jsonl` shows earlier conventional R12 agriculture/life-service outputs, while a repository search for the exact v12 R12 Loop 73 C31 file returned no duplicate result. The immediately preceding local v12 output completed `R11 / Loop 73`, so this execution uses `R12 / Loop 73`.

Novelty classification:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 4
new_trigger_family_count = 2
new_independent_case_count = 4
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
```

Duplicate avoidance outcome:

```text
duplicate_low_value_loop = false
schema_rematerialization_only = false
round_schedule_violation = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
| --- | --- |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Tradable shard columns used:

```text
d,o,h,l,c,v,a,mc,s,m
```

Validation status:

```text
price_source_validation = usable_for_historical_calibration
raw_adjustment_caveat = raw_unadjusted_marcap
corporate_action_policy = block candidate-overlapped 180D windows
```

## 5. Historical Eligibility Gate

| symbol | entry_date | entry_price | 180D forward window | profile corporate-action overlap | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| 009830 | 2022-07-29 | 43800 | available | clean_180D_window_profile_candidates_outside_window | True |
| 112610 | 2022-07-29 | 55500 | available | clean_180D_window_profile_candidates_outside_window | True |
| 099220 | 2022-07-29 | 2690 | available | clean_180D_window_profile_candidates_outside_window | True |
| 043200 | 2022-07-29 | 1090 | available | clean_180D_window_profile_candidates_outside_window | True |

All four representative trigger rows are calibration-usable for 30D/90D/180D. 1Y/2Y fields are retained in the machine-readable schema but are not used for this loop’s primary calibration decision.

## 6. Canonical Archetype Compression Map

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  ├─ direct subsidy / tax-credit / manufacturing route
  │    ├─ 009830 Hanwha Solutions: direct clean-energy manufacturing/tax-credit path
  │    └─ 112610 CS Wind: wind-tower manufacturing/order route
  └─ policy-label / theme-only route
       ├─ 099220 SDN: solar policy label without confirmed direct route
       └─ 043200 Paru: renewable policy label without confirmed direct route
```

Compression finding: inside C31, the useful split is **not** “renewable vs non-renewable.” It is **direct policy-to-earnings path vs policy headline without conversion evidence**.

## 7. Case Selection Summary

| case_id | symbol | company | role | case_type | best_trigger | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R12L73_C31_POS_009830_IRA_SOLAR_MANUFACTURING | 009830 | 한화솔루션 | positive | structural_success | IRA direct clean-energy manufacturing/tax-credit path after U.S. Senate agreement became tradable in Korea | current_profile_correct |
| R12L73_C31_POS_112610_IRA_WIND_TOWER | 112610 | 씨에스윈드 | positive | structural_success | IRA clean-energy/wind manufacturing visibility after public policy agreement | current_profile_correct |
| R12L73_C31_CEX_099220_IRA_SOLAR_THEME | 099220 | SDN | counterexample | failed_rerating | IRA/solar policy label without enough durable revenue bridge | current_profile_false_positive |
| R12L73_C31_CEX_043200_IRA_SOLAR_THEME | 043200 | 파루 | counterexample | failed_rerating | IRA/renewable policy label without company-specific revenue bridge | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| metric | count | interpretation |
| --- | --- | --- |
| positive_case_count | 2 | direct subsidy/order/manufacturing route |
| counterexample_count | 2 | policy-label/relative-strength route without company-specific conversion |
| 4B_case_count | 4 | two good 4B overlays and two price-only local 4B warnings |
| 4C_case_count | 2 | counterexamples require hard 4C/loss-of-thesis watch when evidence route fails |

The case balance satisfies the v12 minimum:

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| symbol | trigger_date | trigger_type | Stage2 evidence | Stage3 evidence | 4B/4C evidence separation |
| --- | --- | --- | --- | --- | --- |
| 009830 | 2022-07-28 | Stage2-Actionable | public_event_or_disclosure, policy_or_regulatory_optionality, capacity_or_volume_route, relative_strength | financial_visibility, margin_bridge, multiple_public_sources | 4B=valuation_blowoff,positioning_overheat / 4C=none |
| 112610 | 2022-07-28 | Stage2-Actionable | public_event_or_disclosure, policy_or_regulatory_optionality, customer_or_order_quality, relative_strength | repeat_order_or_conversion, financial_visibility, multiple_public_sources | 4B=valuation_blowoff,positioning_overheat / 4C=none |
| 099220 | 2022-07-28 | Stage2-Actionable | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | none at trigger date | 4B=price_only_local_peak,positioning_overheat / 4C=thesis_evidence_broken |
| 043200 | 2022-07-28 | Stage2-Actionable | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | none at trigger date | 4B=price_only_local_peak / 4C=thesis_evidence_broken |

Guardrail used in this loop:

```text
price action alone is not Stage2/3 evidence.
policy headline alone is not enough for C31 promotion.
later outcome is not used to relabel the trigger date.
```

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry_date | entry_price | window status |
| --- | --- | --- | --- | --- | --- | --- |
| 009830 | 한화솔루션 | atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv | atlas/symbol_profiles/009/009830.json | 2022-07-29 | 43800 | clean_180D_window_profile_candidates_outside_window |
| 112610 | 씨에스윈드 | atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv | atlas/symbol_profiles/112/112610.json | 2022-07-29 | 55500 | clean_180D_window_profile_candidates_outside_window |
| 099220 | SDN | atlas/ohlcv_tradable_by_symbol_year/099/099220/2022.csv | atlas/symbol_profiles/099/099220.json | 2022-07-29 | 2690 | clean_180D_window_profile_candidates_outside_window |
| 043200 | 파루 | atlas/ohlcv_tradable_by_symbol_year/043/043200/2022.csv | atlas/symbol_profiles/043/043200.json | 2022-07-29 | 1090 | clean_180D_window_profile_candidates_outside_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R12L73_C31_009830_T1_STAGE2_IRA_DIRECT_TAX_CREDIT | 009830 | 2022-07-29 | 43800 | 21.23 | 27.63 | 30.14 | -4.68 | -4.68 | -10.73 | 2023-03-31 | 57000 | current_profile_correct |
| R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY | 112610 | 2022-07-29 | 55500 | 27.93 | 45.05 | 45.05 | -4.5 | -4.5 | -4.5 | 2022-11-28 | 80500 | current_profile_correct |
| R12L73_C31_099220_T1_STAGE2_POLICY_LABEL_THEME | 099220 | 2022-07-29 | 2690 | 24.35 | 24.35 | 24.35 | -3.35 | -29.18 | -40.52 | 2022-08-01 | 3345 | current_profile_false_positive |
| R12L73_C31_043200_T1_STAGE2_POLICY_LABEL_THEME | 043200 | 2022-07-29 | 1090 | 14.68 | 14.68 | 14.68 | -7.8 | -24.04 | -29.36 | 2022-08-11 | 1250 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger backtest

| symbol | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | below_entry_30D | below_entry_90D | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 009830 | 2022-07-29 @ 43800 | 21.23 | -4.68 | 27.63 | -4.68 | 30.14 | -10.73 | True | True | policy_direct_path_structural_success_with_controlled_mae |
| 112610 | 2022-07-29 @ 55500 | 27.93 | -4.5 | 45.05 | -4.5 | 45.05 | -4.5 | True | True | policy_direct_path_structural_success |
| 099220 | 2022-07-29 @ 2690 | 24.35 | -3.35 | 24.35 | -29.18 | 24.35 | -40.52 | True | True | false_positive_policy_theme_high_mae |
| 043200 | 2022-07-29 @ 1090 | 14.68 | -7.8 | 14.68 | -24.04 | 14.68 | -29.36 | True | True | false_positive_policy_theme_high_mae |

### Positive vs counterexample aggregate

| group | case_count | avg_MFE_180D_pct | avg_MAE_180D_pct | interpretation |
| --- | --- | --- | --- | --- |
| direct route positives | 2 | 37.59 | -7.62 | policy event converted into durable upside with controlled MAE |
| policy-label counters | 2 | 19.52 | -34.94 | initial upside existed, but high drawdown makes Stage2/Yellow promotion unsafe |
| all selected by P0 | 4 | 28.55 | -21.28 | mixed alignment; current profile over-accepts policy label triggers |

## 13. Current Calibrated Profile Stress Test

| question | answer |
| --- | --- |
| 1. How would current profile judge these cases? | P0 likely accepts all four as at least Stage2-Actionable/Yellow because policy + RS is visible. |
| 2. Did that match MFE/MAE? | It matched 009830 and 112610, but over-accepted 099220 and 043200 where MAE_180D reached -40.52% and -29.36%. |
| 3. Was Stage2 bonus too high? | Not globally. It was too generous when policy evidence lacked a company-specific conversion route. |
| 4. Was Yellow 75 too high/low? | Threshold was acceptable for direct-route cases but too easy for policy-label counters with high RS. |
| 5. Was Green 87/revision 55 too high/low? | Kept. No counterexample justifies loosening Green; C31 should remain revision/direct-route dependent. |
| 6. Was price-only blowoff guard appropriate? | Yes. It should be strengthened as a C31 watch-only guard for theme spikes. |
| 7. Was full 4B non-price requirement appropriate? | Yes. Price-only local peaks were useful warnings but not full 4B without route deterioration evidence. |
| 8. Was hard 4C routing too late or too aggressive? | For policy-label counters, hard 4C was late; route evidence failure should start a thesis-break watch earlier. |

Current profile verdict distribution:

```text
current_profile_correct = 2
current_profile_false_positive = 2
current_profile_error_count = 2
```

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable worked when the policy event had a named, company-specific conversion route. It failed when the same policy event only created a sector label plus relative strength.

Green lateness observations:

| symbol | Stage2 entry | proxy Green/confirmation timing | green_lateness_ratio | verdict |
| --- | --- | --- | --- | --- |
| 009830 | 2022-07-29 @ 43800 | confirmation/earnings path after initial policy rerating | 0.52 | Green somewhat late but still before full observed peak |
| 112610 | 2022-07-29 @ 55500 | order/visibility confirmation after initial policy rerating | 0.43 | Green somewhat late but acceptable |
| 099220 | 2022-07-29 @ 2690 | no confirmed Stage3 Green trigger | not_applicable | do not promote to Green |
| 043200 | 2022-07-29 @ 1090 | no confirmed Stage3 Green trigger | not_applicable | do not promote to Green |

Conclusion: this is not a global argument to loosen Green. It is a C31 argument to **raise the evidence quality of Stage2/Yellow before Green ever matters**.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local proximity | full-window proximity | timing verdict |
| --- | --- | --- | --- | --- |
| 009830 | valuation_blowoff,positioning_overheat | 0.89 | 0.82 | good_full_window_4B_timing |
| 112610 | valuation_blowoff,positioning_overheat | 0.93 | 0.93 | good_full_window_4B_timing |
| 099220 | price_only,positioning_overheat | 0.71 | 0.71 | price_only_local_4B_too_early_but_guard_needed |
| 043200 | price_only | 0.69 | 0.69 | price_only_local_4B_too_early_but_guard_needed |

C31-specific interpretation:

```text
direct-route positives: valuation/positioning 4B can be useful near full-window peak.
policy-label counters: price-only 4B is a warning, not a full thesis-exit signal; the real guardrail is to prevent promotion in the first place.
```

## 16. 4C Protection Audit

| symbol | 4C label | reason |
| --- | --- | --- |
| 009830 | thesis_break_watch_only | positive route not broken in 180D window; 4C not used for weight. |
| 112610 | thesis_break_watch_only | positive route not broken in 180D window; 4C not used for weight. |
| 099220 | hard_4c_late | MAE_180D -40.52% shows thesis-break routing came too late if Stage2 was allowed. |
| 043200 | hard_4c_late | MAE_180D -29.36% shows policy-label trigger should have been capped earlier. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L10_policy_event_directness_gate
candidate = require company-specific policy capture route before Stage2-Actionable promotion
```

Candidate rule:

```text
If large_sector_id == L10_POLICY_EVENT_CROSS_REDTEAM_MISC
and canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
and evidence is only policy headline + relative strength
and no company-specific subsidy/order/customer/capacity route is present at trigger_date,
then cap at Stage2-Watch / narrative-only,
even if RS is strong.
```

Backtest support:

```text
positive direct-route cases: 2
policy-label counterexamples: 2
current_profile_false_positive cases removed: 2
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
axis_1 = C31_direct_subsidy_route_bonus
axis_2 = C31_policy_label_no_direct_route_penalty
```

Proposed C31 shadow rule:

```text
C31 positive promotion requires one of:
- identifiable direct subsidy/tax-credit capture,
- named order/backlog/customer conversion,
- domestic/local production capacity route tied to legislation,
- confirmed margin/revision path.

C31 penalty applies when:
- evidence is policy headline + price action only,
- evidence is sector label without company-level conversion,
- no trigger-date financial visibility exists.
```

## 19. Before / After Backtest Comparison

| profile | profile_id | hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness | avg_4B_local | avg_4B_full | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | current calibrated profile | none | 4 | all four Stage2/Yellow policy-linked triggers | 27.93 | -15.6 | 28.55 | -21.28 | 50% | 0 | 0 | 0.48 | 0.80 | 0.78 | mixed: positives worked but policy-label counters kept too much score |
| P0b | e2r_2_0_baseline_reference | rollback reference | older thresholds / no v12 guard assumption | 4 | all four broad policy triggers | 27.93 | -15.6 | 28.55 | -21.28 | 50% | 0 | 0 | 0.48 | 0.80 | 0.78 | weaker than P0 because it lacks price-only guard and same policy-label issue remains |
| P1 | sector_specific_candidate_profile | L10 policy-event directness gate | add L10 policy_directness_min and policy_label_stage_cap | 4 | selects 009830/112610; blocks 099220/043200 from positive stage | 36.34 | -4.59 | 37.59 | -7.62 | 0% | 0 | 0 | 0.48 | 0.91 | 0.88 | improves MAE by rejecting theme-only triggers |
| P2 | canonical_archetype_candidate_profile | C31 subsidy/legislation event route gate | direct_subsidy_route_bonus + no_direct_route_penalty | 4 | selects direct subsidy/order-route cases only | 36.34 | -4.59 | 37.59 | -7.62 | 0% | 0 | 0 | 0.48 | 0.91 | 0.88 | best score-return alignment inside C31 |
| P3 | counterexample_guard_profile | policy-label guard profile | cap Stage2 Actionable unless company-specific route present | 4 | keeps two positives; demotes two counters | 36.34 | -4.59 | 37.59 | -7.62 | 0% | 0 | 0 | 0.48 | 0.91 | 0.88 | guard is useful but should remain shadow-only pending more sectors |

## 20. Score-Return Alignment Matrix

| symbol | score_before | stage_before | score_after | stage_after | MFE_180D | MAE_180D | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 009830 | 79.0 | Stage3-Yellow | 83.0 | Stage3-Yellow | 30.14 | -10.73 | aligned_positive |
| 112610 | 82.0 | Stage3-Yellow | 86.0 | Stage3-Yellow_near_green | 45.05 | -4.5 | aligned_positive |
| 099220 | 76.0 | Stage3-Yellow | 61.0 | Stage2-Watch | 24.35 | -40.52 | false_positive_removed |
| 043200 | 73.0 | Stage2-Actionable | 58.0 | Stage2-Watch | 14.68 | -29.36 | false_positive_removed |

Mechanism summary: the same policy event is like rain on two fields. In one field there is irrigation, soil, and seed; in the other there is only dust. The rain is real in both places, but only one field can grow earnings.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | IRA_DIRECT_SUBSIDY_ROUTE_VS_POLICY_THEME_FALSE_POSITIVE | 2 | 2 | 4 | 2 | 4 | 0 | 4 | 4 | 2 | True | True | remaining gap: non-renewable C31 policy cases and non-US subsidy cases |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_false_positive
  - policy_label_without_direct_revenue_route
  - high_MAE_after_policy_theme_spike
new_axis_proposed:
  - C31_direct_subsidy_route_bonus
  - C31_policy_label_no_direct_route_penalty
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Historical trigger-level 1D OHLC rows from Songdaiki/stock-web.
- 30D/90D/180D MFE and MAE from entry-date close.
- Clean 180D windows against profile-listed corporate-action candidate dates.
- Positive/counterexample balance inside scheduled R12/L10/C31.
- Current calibrated profile residual false positives.
```

Not validated:

```text
- No live 2026 candidate scan.
- No current recommendation.
- No stock_agent source code.
- No production scoring patch.
- No brokerage or automation logic.
- No newly discovered price route outside stock-web.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_direct_subsidy_route_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,+4,+4,"Direct subsidy/order/manufacturing route separated positives from policy-label counters","Selected positives avg_MFE_180D=37.59 and avg_MAE_180D=-7.62; blocked counters avg_MAE_180D=-34.94","R12L73_C31_009830_T1_STAGE2_IRA_DIRECT_TAX_CREDIT|R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_policy_label_no_direct_route_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,-12,-12,"Policy headline plus relative strength without company-specific capture caused high-MAE false positives","Demotes 099220/043200 from Stage2-Actionable/Yellow to Watch; preserves 009830/112610","R12L73_C31_099220_T1_STAGE2_POLICY_LABEL_THEME|R12L73_C31_043200_T1_STAGE2_POLICY_LABEL_THEME",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L10_policy_event_price_only_4B_watch,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,watch_only,non_price_required,0,"Keep existing 4B non-price requirement, but log price-only local peak as guardrail watch","Avoids treating early theme spike as a thesis-ending full 4B while still warning on overheat","R12L73_C31_099220_T1_STAGE2_POLICY_LABEL_THEME|R12L73_C31_043200_T1_STAGE2_POLICY_LABEL_THEME",4,4,2,low,sector_shadow_only,"existing axis strengthened, not changed"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R12L73_C31_POS_009830_IRA_SOLAR_MANUFACTURING","symbol":"009830","company_name":"한화솔루션","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_DIRECT_CLEAN_ENERGY_MANUFACTURING_SUBSIDY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"IRA direct clean-energy manufacturing/tax-credit path after U.S. Senate agreement became tradable in Korea","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"New independent symbol for this R12/C31 loop; no production scoring change."}
{"row_type":"case","case_id":"R12L73_C31_POS_112610_IRA_WIND_TOWER","symbol":"112610","company_name":"씨에스윈드","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_WIND_TOWER_MANUFACTURING_ORDER_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"IRA clean-energy/wind manufacturing visibility after public policy agreement","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"New independent symbol for this R12/C31 loop; no production scoring change."}
{"row_type":"case","case_id":"R12L73_C31_CEX_099220_IRA_SOLAR_THEME","symbol":"099220","company_name":"SDN","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_SOLAR_THEME_NO_DIRECT_SUBSIDY_ROUTE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"IRA/solar policy label without enough durable revenue bridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_removed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"New independent symbol for this R12/C31 loop; no production scoring change."}
{"row_type":"case","case_id":"R12L73_C31_CEX_043200_IRA_SOLAR_THEME","symbol":"043200","company_name":"파루","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_THEME_NO_DIRECT_SUBSIDY_ROUTE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"IRA/renewable policy label without company-specific revenue bridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_removed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"New independent symbol for this R12/C31 loop; no production scoring change."}
{"row_type":"trigger","trigger_id":"R12L73_C31_009830_T1_STAGE2_IRA_DIRECT_TAX_CREDIT","case_id":"R12L73_C31_POS_009830_IRA_SOLAR_MANUFACTURING","symbol":"009830","company_name":"한화솔루션","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_DIRECT_CLEAN_ENERGY_MANUFACTURING_SUBSIDY","sector":"policy-linked renewable manufacturing","primary_archetype":"direct subsidy/tax-credit path with manufacturing exposure","loop_objective":"residual_false_positive_mining | residual_missed_structural_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"U.S. Inflation Reduction Act climate/tax-credit package became public; company had identifiable solar manufacturing/downstream exposure rather than only a broad renewable-energy label.","evidence_source":"public_policy_event: U.S. Inflation Reduction Act Senate agreement / bill text family; company exposure classified from historical business mix, not live discovery","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility","margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":43800,"MFE_30D_pct":21.23,"MFE_90D_pct":27.63,"MFE_180D_pct":30.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.68,"MAE_90D_pct":-4.68,"MAE_180D_pct":-10.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-31","peak_price":57000,"drawdown_after_peak_pct":-20.88,"green_lateness_ratio":0.52,"four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_direct_path_structural_success_with_controlled_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_candidates_outside_window","same_entry_group_id":"R12L73_C31_009830_2022-07-29_43800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY","case_id":"R12L73_C31_POS_112610_IRA_WIND_TOWER","symbol":"112610","company_name":"씨에스윈드","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_WIND_TOWER_MANUFACTURING_ORDER_ROUTE","sector":"policy-linked wind equipment manufacturing","primary_archetype":"direct renewable manufacturing/order route","loop_objective":"residual_false_positive_mining | residual_missed_structural_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"Policy package was not only a theme headline; wind-tower manufacturing exposure gave a concrete route from subsidy/renewable capex to order and margin visibility.","evidence_source":"public_policy_event: U.S. Inflation Reduction Act Senate agreement / bill text family; company exposure classified from historical business mix, not live discovery","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":55500,"MFE_30D_pct":27.93,"MFE_90D_pct":45.05,"MFE_180D_pct":45.05,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.5,"MAE_90D_pct":-4.5,"MAE_180D_pct":-4.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-11-28","peak_price":80500,"drawdown_after_peak_pct":-23.23,"green_lateness_ratio":0.43,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_direct_path_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_candidates_outside_window","same_entry_group_id":"R12L73_C31_112610_2022-07-29_55500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L73_C31_099220_T1_STAGE2_POLICY_LABEL_THEME","case_id":"R12L73_C31_CEX_099220_IRA_SOLAR_THEME","symbol":"099220","company_name":"SDN","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_SOLAR_THEME_NO_DIRECT_SUBSIDY_ROUTE","sector":"policy-linked solar theme","primary_archetype":"policy label without company-specific conversion","loop_objective":"residual_false_positive_mining | residual_missed_structural_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"Solar policy headline and relative-strength spike were visible, but trigger-date evidence did not prove direct subsidy capture, recurring order conversion, or margin bridge.","evidence_source":"public_policy_event: U.S. Inflation Reduction Act headline family; counterexample classification from absence of trigger-date company-specific direct route","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099220/2022.csv","profile_path":"atlas/symbol_profiles/099/099220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":2690,"MFE_30D_pct":24.35,"MFE_90D_pct":24.35,"MFE_180D_pct":24.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.35,"MAE_90D_pct":-29.18,"MAE_180D_pct":-40.52,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-01","peak_price":3345,"drawdown_after_peak_pct":-52.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.71,"four_b_full_window_peak_proximity":0.71,"four_b_timing_verdict":"price_only_local_4B_too_early_but_guard_needed","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_policy_theme_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_candidates_outside_window","same_entry_group_id":"R12L73_C31_099220_2022-07-29_2690","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L73_C31_043200_T1_STAGE2_POLICY_LABEL_THEME","case_id":"R12L73_C31_CEX_043200_IRA_SOLAR_THEME","symbol":"043200","company_name":"파루","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_RENEWABLE_THEME_NO_DIRECT_SUBSIDY_ROUTE","sector":"policy-linked renewable theme","primary_archetype":"policy label without conversion","loop_objective":"residual_false_positive_mining | residual_missed_structural_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"Renewable-policy linkage was visible as a market theme, but company-specific backlog, subsidy capture, customer quality, and revision evidence were not confirmed at trigger date.","evidence_source":"public_policy_event: U.S. Inflation Reduction Act headline family; counterexample classification from absence of trigger-date company-specific direct route","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/043/043200/2022.csv","profile_path":"atlas/symbol_profiles/043/043200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":1090,"MFE_30D_pct":14.68,"MFE_90D_pct":14.68,"MFE_180D_pct":14.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.8,"MAE_90D_pct":-24.04,"MAE_180D_pct":-29.36,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-11","peak_price":1250,"drawdown_after_peak_pct":-38.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.69,"four_b_full_window_peak_proximity":0.69,"four_b_timing_verdict":"price_only_local_4B_too_early_but_guard_needed","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_policy_theme_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_profile_candidates_outside_window","same_entry_group_id":"R12L73_C31_043200_2022-07-29_1090","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L73_C31_POS_009830_IRA_SOLAR_MANUFACTURING","trigger_id":"R12L73_C31_009830_T1_STAGE2_IRA_DIRECT_TAX_CREDIT","symbol":"009830","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":15,"customer_quality_score":8,"policy_or_regulatory_score":18,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":12,"subsidy_directness_score":10},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":9,"revision_score":10,"relative_strength_score":15,"customer_quality_score":8,"policy_or_regulatory_score":20,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":14,"subsidy_directness_score":14},"weighted_score_after":83.0,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","subsidy_directness_score","capacity_or_shipment_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C31 shadow profile separates direct subsidy/capacity/order route from policy-label-only relative strength; not a production score.","MFE_90D_pct":27.63,"MAE_90D_pct":-4.68,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L73_C31_POS_112610_IRA_WIND_TOWER","trigger_id":"R12L73_C31_112610_T1_STAGE2_IRA_WIND_TOWER_VISIBILITY","symbol":"112610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":17,"customer_quality_score":10,"policy_or_regulatory_score":18,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":11,"subsidy_directness_score":11},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":10,"margin_bridge_score":9,"revision_score":9,"relative_strength_score":17,"customer_quality_score":10,"policy_or_regulatory_score":20,"valuation_repricing_score":9,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":14,"subsidy_directness_score":15},"weighted_score_after":86.0,"stage_label_after":"Stage3-Yellow_near_green","changed_components":["policy_or_regulatory_score","subsidy_directness_score","capacity_or_shipment_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C31 shadow profile separates direct subsidy/capacity/order route from policy-label-only relative strength; not a production score.","MFE_90D_pct":45.05,"MAE_90D_pct":-4.5,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L73_C31_CEX_099220_IRA_SOLAR_THEME","trigger_id":"R12L73_C31_099220_T1_STAGE2_POLICY_LABEL_THEME","symbol":"099220","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":8,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":2,"subsidy_directness_score":1},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"subsidy_directness_score":0},"weighted_score_after":61.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","subsidy_directness_score","capacity_or_shipment_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C31 shadow profile separates direct subsidy/capacity/order route from policy-label-only relative strength; not a production score.","MFE_90D_pct":24.35,"MAE_90D_pct":-29.18,"score_return_alignment_label":"false_positive_removed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L73_C31_CEX_043200_IRA_SOLAR_THEME","trigger_id":"R12L73_C31_043200_T1_STAGE2_POLICY_LABEL_THEME","symbol":"043200","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":17,"valuation_repricing_score":5,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":1,"subsidy_directness_score":0},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":2,"execution_risk_score":-15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"subsidy_directness_score":0},"weighted_score_after":58.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","subsidy_directness_score","capacity_or_shipment_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"C31 shadow profile separates direct subsidy/capacity/order route from policy-label-only relative strength; not a production score.","MFE_90D_pct":14.68,"MAE_90D_pct":-24.04,"score_return_alignment_label":"false_positive_removed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage3_yellow_total_min","stage3_green_total_min"],"residual_error_types_found":["current_profile_false_positive","policy_label_without_direct_revenue_route","high_MAE_after_policy_theme_spike"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R12
completed_loop = 73
next_round = R13
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest observed: source_name=FinanceData/marcap, price_adjustment_status=raw_unadjusted_marcap, max_date=2026-02-20, calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year.
- Stock-Web schema observed: tradable shard columns are d/o/h/l/c/v/a/mc/s/m; MFE/MAE formulas are max-high/min-low over N tradable rows.
- 009830 profile: current/latest name 한화솔루션; corporate-action candidate dates are 1999-04-20 and 2008-07-04, outside this window.
- 112610 profile: current/latest name 씨에스윈드; corporate-action candidate dates are 2021-02-08, 2021-02-22, 2021-03-05, outside this window.
- 099220 profile: current/latest name SDN; corporate-action candidate dates are 2010-05-03 and 2010-05-26, outside this window.
- 043200 profile: current/latest name 파루; listed corporate-action candidate dates end at 2016-06-20, outside this window.
- All trigger-level OHLC values in this MD use the 2022/2023 tradable shards from Songdaiki/stock-web; no live candidate discovery was performed.

