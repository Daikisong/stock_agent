# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R11
loop = 10
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM
output_file = e2r_stock_web_v12_residual_round_R11_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_accessed = false
stock_agent_src_accessed = false
stock_agent_patch_written = false
live_candidate_mode = false
current_stock_discovery_allowed = false
```

This v12 loop is a **historical trigger-level residual calibration** file. It is not a current stock recommendation, not a live watchlist, not a broker/API workflow, and not a repository implementation patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does **not** re-prove the already applied global rules. It stress-tests them inside C31 and proposes only shadow-only sector/canonical-archetype residual candidates.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R11 |
| loop | 10 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM |
| loop_objective | residual_false_positive_mining / residual_missed_structural_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill |
| validation stance | historical only; no live candidate discovery |

The C31 question is not “did a policy headline move the stock?” but “did the policy/legislation/subsidy create a company-specific path into orders, tax-credit monetization, capacity utilization, margin bridge, or durable revision?” A policy event without that bridge behaves like a firework: bright, hot, and often gone before the income statement notices.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact review used only for coverage and duplicate avoidance:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/applied_scoring_diff.md
```

Observed context:

```text
discovered_md_count = 398
parsed_document_count = 107
raw_trigger_rows = 4951
validated_trigger_rows = 1940
aggregate_representative_trigger_rows = 1376
rounds_covered = R1~R13
loops_covered = 1~9
main rejected reasons = invalid_price_source, invalid_price_adjustment_status, missing_required_mfe_mae
```

Duplicate search note:

```text
Searched repository artifact text for selected symbols: 009830, 112610, 001470, 053290, 336260.
No exact hit was found through the available GitHub search result for this session.
```

Novelty posture:

```text
new_independent_case_ratio = 5 / 5 = 1.00
required_new_independent_case_ratio = 0.60
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web atlas fields verified before case construction:

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream source | FinanceData/marcap |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| manifest_min_date | 1995-05-02 |
| manifest_max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |
| validation_status | usable_for_historical_calibration |

Caveat retained for every row:

```text
Raw/unadjusted OHLC. Corporate actions are not adjusted.
Tradable shards exclude zero-volume, zero-OHLC, missing-OHLC, and inconsistent-OHLC rows.
Corporate-action-contaminated windows are blocked by default.
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward_180D_available | 180D corporate-action window | calibration_usable | notes |
|---|---:|---:|---:|---|---:|---|
| C31-009830-IRA-SOLAR | 009830 | 2022-08-17 | true | clean_180D_window | true | historical IRA solar/manufacturing policy-to-capacity bridge |
| C31-112610-IRA-WIND | 112610 | 2022-08-17 | true | clean_180D_window | true | historical IRA wind tower/tax-credit/order bridge |
| C31-001470-UKR-REBUILD | 001470 | 2023-05-22 | true | clean_180D_window | true | event premium / reconstruction headline; no company cashflow bridge at trigger |
| C31-053290-POLICY-THEME | 053290 | 2021-03-04 | true | clean_180D_window | true | political/education policy theme; no contract/revision bridge |
| C31-336260-HYDROGEN-POLICY | 336260 | 2022-08-11 | true | clean_180D_window | true | hydrogen policy headline failed to convert into durable order/revision evidence |

## 6. Canonical Archetype Compression Map

| raw/fine event family | mapped canonical_archetype_id | compression rule |
|---|---|---|
| IRA solar manufacturing / domestic tax-credit pathway | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | keep in C31 only if policy is the primary catalyst; score promotion requires company-specific capacity/order/margin bridge |
| IRA wind tower / tax credit / order backlog route | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | same C31 bridge; do not remap into C02 unless grid/data-center capex is the primary thesis |
| Ukraine reconstruction / diplomatic headline | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | event premium; no positive promotion without named project, funded order, or backlog conversion |
| political education/candidate theme | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | cap at narrative/event-watch; no Stage2/3 promotion from political affinity alone |
| hydrogen economy policy headline | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | positive only after policy converts into enforceable procurement, long-term offtake, or margin subsidy |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_role | positive_or_counterexample | best_trigger | current_profile_verdict | calibration_usable |
|---|---:|---|---|---|---|---|---:|
| C31-009830-IRA-SOLAR | 009830 | 한화솔루션 | structural_success | positive | T009830-S2-20220817 | current_profile_correct | true |
| C31-112610-IRA-WIND | 112610 | 씨에스윈드 | structural_success | positive | T112610-S2-20220817 | current_profile_correct | true |
| C31-001470-UKR-REBUILD | 001470 | 삼부토건 | price_moved_without_evidence / 4B_overlay_success | counterexample | T001470-S2-20230522 | current_profile_false_positive | true |
| C31-053290-POLICY-THEME | 053290 | NE능률 | price_moved_without_evidence / 4B_overlay_success | counterexample | T053290-S2-20210304 | current_profile_false_positive | true |
| C31-336260-HYDROGEN-POLICY | 336260 | 두산퓨얼셀 | failed_rerating / 4C_late | counterexample | T336260-S2-20220811 | current_profile_false_positive | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 1
minimum_positive_case_count = 1
minimum_counterexample_count = 1
minimum_calibration_usable_case_count = 3
```

Balance verdict:

```text
positive_case_missing = false
counterexample_search_incomplete = false
max_shadow_delta = not_limited_by_positive_only
```

## 9. Evidence Source Map

This loop uses historical evidence labels rather than live source collection. Evidence source strings are deliberately conservative and designed for later parser verification.

| case_id | trigger_date | evidence_source | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence |
|---|---:|---|---|---|---|---|
| C31-009830-IRA-SOLAR | 2022-08-16 | historical public policy event: U.S. IRA signing + solar manufacturing/tax-credit narrative | policy_or_regulatory_optionality; capacity_or_volume_route; early_revision_signal | margin_bridge; financial_visibility; multiple_public_sources | none at entry | none |
| C31-112610-IRA-WIND | 2022-08-16 | historical public policy event: U.S. IRA signing + wind tower/tax-credit/order visibility narrative | policy_or_regulatory_optionality; customer_or_order_quality; backlog_or_delivery_visibility | margin_bridge; durable_customer_confirmation; multiple_public_sources | none at entry | none |
| C31-001470-UKR-REBUILD | 2023-05-19 | historical public geopolitical/reconstruction headline | policy_or_regulatory_optionality; relative_strength | none | price_only_local_peak; positioning_overheat | thesis_evidence_broken watch only |
| C31-053290-POLICY-THEME | 2021-03-04 | historical public political/education theme flow | policy_or_regulatory_optionality; relative_strength | none | price_only_local_peak; positioning_overheat | thesis_evidence_broken watch only |
| C31-336260-HYDROGEN-POLICY | 2022-08-11 | historical public hydrogen policy/subsidy headline | policy_or_regulatory_optionality; relative_strength | none | price_only_local_peak | failed_policy_to_order_conversion; thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | profile_path | representative_shard_paths | profile caveat |
|---:|---|---|---|---|
| 009830 | 한화솔루션 | atlas/symbol_profiles/009/009830.json | atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv; 2023.csv | old corporate-action candidates outside tested window |
| 112610 | 씨에스윈드 | atlas/symbol_profiles/112/112610.json | atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv; 2023.csv | corporate-action candidates in 2021 only; tested 2022~2023 clean |
| 001470 | 삼부토건 | atlas/symbol_profiles/001/001470.json | atlas/ohlcv_tradable_by_symbol_year/001/001470/2023.csv | older corporate-action candidates outside tested window |
| 053290 | NE능률 | atlas/symbol_profiles/053/053290.json | atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv | older corporate-action candidates outside tested window |
| 336260 | 두산퓨얼셀 | atlas/symbol_profiles/336/336260.json | atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv | no corporate-action candidate in profile |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence | current_profile_verdict |
|---|---|---|---:|---:|---:|---|---|---|---|
| T009830-S2-20220817 | C31-009830-IRA-SOLAR | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 46550 | policy + capacity route + early revision | margin bridge; financial visibility | none | current_profile_correct |
| T009830-YELLOW-20221124 | C31-009830-IRA-SOLAR | Stage3-Yellow | 2022-11-24 | 2022-11-24 | 54000 | prior evidence retained | margin bridge; multi-source confirmation | none | current_profile_correct |
| T112610-S2-20220817 | C31-112610-IRA-WIND | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 63600 | policy + order/backlog route | customer/order bridge emerging | none | current_profile_correct |
| T112610-YELLOW-20221116 | C31-112610-IRA-WIND | Stage3-Yellow | 2022-11-16 | 2022-11-16 | 75800 | prior evidence retained | order/tax-credit quality stronger | none | current_profile_correct |
| T001470-S2-20230522 | C31-001470-UKR-REBUILD | Stage2-Actionable label comparison | 2023-05-19 | 2023-05-22 | 1496 | policy headline + relative strength | none | none at entry | current_profile_false_positive |
| T001470-4B-20230717 | C31-001470-UKR-REBUILD | 4B_overlay_only | 2023-07-17 | 2023-07-17 | 5010 | none | none | price_only_local_peak; positioning_overheat | current_profile_4B_too_early if full 4B |
| T053290-S2-20210304 | C31-053290-POLICY-THEME | Stage2-Actionable label comparison | 2021-03-04 | 2021-03-04 | 4450 | policy/political theme + relative strength | none | none at entry | current_profile_false_positive |
| T053290-4B-20210407 | C31-053290-POLICY-THEME | 4B_overlay_only | 2021-04-07 | 2021-04-07 | 23000 | none | none | price_only_local_peak; positioning_overheat | current_profile_4B_too_early if full 4B |
| T336260-S2-20220811 | C31-336260-HYDROGEN-POLICY | Stage2-Actionable label comparison | 2022-08-11 | 2022-08-11 | 40350 | policy headline + relative strength | none | later failed conversion | current_profile_false_positive |
| T336260-4C-20221013 | C31-336260-HYDROGEN-POLICY | 4C_overlay_only | 2022-10-13 | 2022-10-13 | 24450 | none | none | failed_policy_to_order_conversion; thesis_evidence_broken | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger rows use `calibration_usable=true`, `dedupe_for_aggregate=true`, and `aggregate_group_role=representative`.

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| T009830-S2-20220817 | 46,550 | 20.09 | -3.11 | 20.09 | -3.11 | 22.45 | -16.00 | 2023-03-31 | 57,000 | -32.54 | positive_structural_success with high volatility |
| T112610-S2-20220817 | 63,600 | 11.64 | -6.76 | 26.57 | -10.85 | 38.52 | -10.85 | 2023-04-24 | 88,100 | -12.94 | positive_structural_success |
| T001470-S2-20230522 | 1,496 | 183.09 | -21.66 | 267.65 | -21.66 | 267.65 | -21.66 | 2023-07-17 | 5,500 | -55.00 | price_moved_without_evidence / event premium |
| T053290-S2-20210304 | 4,450 | 476.40 | -21.24 | 591.01 | -21.24 | 591.01 | -21.24 | 2021-06-09 | 30,750 | -56.59 | price_moved_without_evidence / political theme premium |
| T336260-S2-20220811 | 40,350 | 2.23 | -16.98 | 2.23 | -39.41 | 2.23 | -39.41 | 2022-08-16 | 41,250 | -40.73 | failed_policy_to_order_conversion |

Non-representative overlay rows:

| trigger_id | entry_price | overlay_type | local/full relevance | MFE_90D_after_overlay | MAE_90D_after_overlay | verdict |
|---|---:|---|---|---:|---:|---|
| T001470-4B-20230717 | 5,010 | price_only_local_peak | local high near event blowoff, not full fundamental 4B | 9.78 | -51.70 | do_not_treat_as_full_4B without non-price evidence |
| T053290-4B-20210407 | 23,000 | price_only_local_peak | local blowoff before final June spike | 33.70 | -29.78 | price-only 4B too early for full-window 4B |
| T336260-4C-20221013 | 24,450 | failed policy-to-order conversion | late protection after large drawdown | 52.15 | -2.25 | 4C watch useful but late versus entry damage |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual path | stress verdict | residual error |
|---|---|---|---|---|
| C31-009830-IRA-SOLAR | Stage2-Actionable / Stage3-Yellow, no Green until revision confirmation | MFE_180D +22.45%, MAE_180D -16.00% | current_profile_correct | no global change; add C31 bridge clarity |
| C31-112610-IRA-WIND | Stage2-Actionable / Stage3-Yellow | MFE_180D +38.52%, MAE_180D -10.85% | current_profile_correct | no global change; add C31 bridge clarity |
| C31-001470-UKR-REBUILD | could be over-promoted if policy headline + RS are treated as Stage2 evidence | MFE huge but no durable evidence; crash-like drawdown after peak | current_profile_false_positive | event premium must not train positive weights |
| C31-053290-POLICY-THEME | could be over-promoted if political policy theme + RS are treated as Stage2 evidence | MFE huge but no company cashflow bridge | current_profile_false_positive | political/policy affinity should be narrative-only or event-watch |
| C31-336260-HYDROGEN-POLICY | could be Stage2 from policy + RS | MFE_180D only +2.23%, MAE_180D -39.41% | current_profile_false_positive | policy-to-order conversion failure needs fast cap/4C-watch |

Answers to mandatory stress-test questions:

```text
1. current calibrated profile is broadly correct on structural IRA cases but too permissive when policy headline + relative strength impersonate evidence.
2. correct on positive MFE/MAE for 009830 and 112610; false-positive on 001470, 053290, 336260 if the model credits policy headline as evidence.
3. Stage2 bonus is not globally too high, but C31 should require a policy-to-cashflow bridge before the +2 evidence bonus applies.
4. Yellow threshold 75 is acceptable when policy bridge exists; too low when policy bridge is absent.
5. Green threshold 87 / revision 55 should remain strict; C31 should not use policy headline as revision proxy.
6. price-only blowoff guard is appropriate and should be strengthened within C31.
7. full 4B non-price requirement is appropriate; C31 price-only local peaks are often false full-cycle exits.
8. hard 4C routing is appropriate, but C31 should allow fast 4C-watch when policy fails to convert into orders/revision after a defined window.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3/Yellow comparison | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| C31-009830-IRA-SOLAR | 46,550 | 54,000 on 2022-11-24 | 0.81 | Yellow arrived after most of the first policy-to-capacity upside; still acceptable as confirmation, not initial entry |
| C31-112610-IRA-WIND | 63,600 | 75,800 on 2022-11-16 | 0.50 | Yellow moderately late but still before full observed window peak |
| C31-001470-UKR-REBUILD | 1,496 | no confirmed Stage3-Green | not_applicable | no non-price evidence; Green should never trigger from outcome |
| C31-053290-POLICY-THEME | 4,450 | no confirmed Stage3-Green | not_applicable | no non-price evidence; Green should never trigger from outcome |
| C31-336260-HYDROGEN-POLICY | 40,350 | no confirmed Stage3-Green | not_applicable | no policy-to-order conversion; should stay event-watch or 4C-watch |

Formula:

```text
green_lateness_ratio = (Stage3_Green_or_Yellow_entry_price - Stage2_Actionable_entry_price) / (peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B trigger | 4B evidence type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---|---:|---:|---|
| C31-001470-UKR-REBUILD | T001470-4B-20230717 | price_only / positioning_overheat | 0.91 | 0.88 | price-only local 4B looked close, but no non-price evidence; treat as event-premium cap, not full 4B |
| C31-053290-POLICY-THEME | T053290-4B-20210407 | price_only / positioning_overheat | 0.89 | 0.71 | local peak was too early versus full June spike; full 4B requires non-price evidence |
| C31-336260-HYDROGEN-POLICY | T336260-S2-20220811 | price_only / failed conversion later | 1.00 | 1.00 | rally peak was local and full-window peak, but the correct label is failed policy-to-order conversion, not successful 4B graduation |

C31 4B lesson:

```text
Policy/event premiums often create visually perfect local peaks. If the only evidence is price shape, they should be event-premium caps or 4B overlays, never full 4B exits of a valid Stage3 thesis.
```

## 16. 4C Protection Audit

| case_id | 4C trigger | label | protection note |
|---|---|---|---|
| C31-336260-HYDROGEN-POLICY | T336260-4C-20221013 | hard_4c_late | By the time failed conversion was obvious from price path, MAE from Stage2 was already about -39%; a C31 bridge gate would have blocked the positive Stage2 earlier. |
| C31-001470-UKR-REBUILD | narrative only | thesis_break_watch_only | No company-specific funded project/order evidence existed at entry; should be event-watch from the beginning rather than late 4C. |
| C31-053290-POLICY-THEME | narrative only | false_break / theme-only | Political linkage is not a business thesis; therefore there is no thesis to break, only an event premium to cap. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
candidate_axis = l10_policy_event_cashflow_bridge_gate
baseline_value = 0
shadow_tested_value = 1
proposal_type = sector_shadow_only
confidence = medium
```

Rule candidate:

```text
Within L10, policy/regulatory/geopolitical headlines may create Stage0/Event-Watch and query priority, but cannot receive Stage2-Actionable bonus unless at least one of the following is present by trigger date:
- named customer/order/project with funding source,
- explicit subsidy/tax-credit route tied to company capacity or shipments,
- capacity utilization or margin bridge that converts policy into EPS/FCF,
- early analyst/disclosure revision that links the policy to revenue or margin.
```

Expected effect:

```text
- Keeps 009830 and 112610 eligible because policy bridge exists.
- Blocks 001470 and 053290 from positive scoring despite high MFE.
- Keeps 336260 as event-watch until order/revision evidence appears.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_axis = c31_policy_to_cashflow_bridge_required
```

Detailed shadow rules:

1. `c31_policy_to_cashflow_bridge_required = true`
   A C31 trigger cannot pass Stage2-Actionable unless policy evidence is linked to contract/order/capacity/margin/revision.

2. `c31_subsidy_event_premium_cap = true`
   If the trigger is policy headline + relative strength only, cap at Event-Watch/Narrative-only for positive calibration even if later MFE is extreme.

3. `c31_failed_policy_to_order_conversion_fast_4c_watch = true`
   If policy headline rallies and no order/revision evidence appears while 90D MAE exceeds -25%, route to 4C-watch/failed_conversion rather than preserving Stage2 optimism.

4. `c31_price_only_4b_overlay_not_full_4b = true`
   Price-only local peaks inside C31 are overlays and should not train full 4B exit timing.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current global proxy | 5 | 181.51 | -19.25 | 184.37 | -19.83 | 0.60 | 0 | mixed: captures structural but lets event premium contaminate C31 evidence |
| P0b_e2r_2_0_baseline_reference | rollback reference | 5 | 181.51 | -19.25 | 184.37 | -19.83 | 0.80 | 0 | worse: more vulnerable to headline/RS false positives |
| P1_l10_policy_event_cashflow_bridge_gate | sector-specific shadow | 5 | 23.33 | -13.43 | 30.49 | -13.43 | 0.20 | 0 | better: keeps structural cases, blocks theme-only rows from positive aggregate |
| P2_c31_policy_to_cashflow_bridge_required | canonical-archetype shadow | 5 | 23.33 | -13.43 | 30.49 | -13.43 | 0.20 | 0 | best fit for C31 compression |
| P3_c31_event_premium_guard_profile | counterexample guard | 5 | 23.33 | -13.43 | 30.49 | -13.43 | 0.00 for positive promotion | 0 | strongest anti-contamination guard; may under-credit early but unverified policy trades |

Note: Profile averages after P1/P2/P3 include only rows allowed to train positive weight; event-premium rows remain in overlay/red-team calibration.

## 20. Score-Return Alignment Matrix

| case_id | P0 score/stage before | P2 score/stage after | raw component reason | MFE_90D | MAE_90D | alignment label |
|---|---|---|---|---:|---:|---|
| C31-009830-IRA-SOLAR | 76 / Stage3-Yellow | 81 / Stage3-Yellow | policy bridge + capacity route + margin/revision support | 20.09 | -3.11 | score_aligned_positive |
| C31-112610-IRA-WIND | 78 / Stage3-Yellow | 83 / Stage3-Yellow | policy bridge + order/backlog quality | 26.57 | -10.85 | score_aligned_positive |
| C31-001470-UKR-REBUILD | 68 / Stage2-Actionable | 45 / Event-Watch | headline + RS only; no funded project/order | 267.65 | -21.66 | outcome_not_valid_positive_evidence |
| C31-053290-POLICY-THEME | 70 / Stage2-Actionable | 40 / Narrative-only | political affinity, no company cashflow bridge | 591.01 | -21.24 | outcome_not_valid_positive_evidence |
| C31-336260-HYDROGEN-POLICY | 72 / Stage2-Actionable | 55 / Event-Watch / 4C-watch | policy headline failed to convert into order/revision | 2.23 | -39.41 | score_corrected_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM | 2 | 3 | 2 | 1 | 5 | 0 | 8 | 5 | 3 | true | true | Need holdout with non-Korea policy/subsidy cases and more failed subsidy-to-order conversions |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - policy_headline_plus_relative_strength_false_positive
  - event_premium_mfe_contaminates_positive_weight
  - failed_policy_to_order_conversion
  - price_only_local_4b_not_full_4b
new_axis_proposed:
  - c31_policy_to_cashflow_bridge_required
  - c31_subsidy_event_premium_cap
  - c31_failed_policy_to_order_conversion_fast_4c_watch
  - c31_price_only_4b_overlay_not_full_4b
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
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
- Stock-Web manifest/schema inspected.
- Stock-Web profile files checked for all five symbols.
- Representative OHLC rows inspected from tradable shards.
- 30D/90D/180D MFE/MAE computed on tradable_raw basis from inspected stock-web rows.
- Corporate-action contamination screened using profile corporate_action_candidate_dates.
- Same-entry dedupe applied for representative vs overlay rows.
```

Not validated in this loop:

```text
- No stock_agent src/e2r code opened.
- No production scoring implementation inspected.
- No current/live candidate scan performed.
- No broker/API integration attempted.
- No official disclosure parser rerun.
- External evidence parser verification deferred to later implementation/research batch.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_policy_to_cashflow_bridge_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy headline must convert into order/capacity/margin/revision before Stage2 bonus applies","keeps 009830/112610; blocks 001470/053290/336260 false positive training","T009830-S2-20220817|T112610-S2-20220817|T001470-S2-20230522|T053290-S2-20210304|T336260-S2-20220811",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_subsidy_event_premium_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Extreme MFE from event premium cannot train positive entry weights without cashflow bridge","prevents outcome leakage from 001470 and 053290","T001470-S2-20230522|T053290-S2-20210304",2,2,2,medium,canonical_shadow_only,"event premium rows remain useful for red-team/4B overlay"
shadow_weight,c31_failed_policy_to_order_conversion_fast_4c_watch,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy rallies with no order/revision conversion and MAE_90D below -25% should move to 4C-watch","reduces 336260-style prolonged false positive","T336260-S2-20220811|T336260-4C-20221013",1,1,1,low,canonical_shadow_only,"needs more holdout cases before production"
shadow_weight,c31_price_only_4b_overlay_not_full_4b,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 local peaks without non-price evidence are overlay only","aligns with full_4b_requires_non_price_evidence","T001470-4B-20230717|T053290-4B-20210407",2,2,2,medium,canonical_shadow_only,"strengthens existing 4B guardrail within C31"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C31-009830-IRA-SOLAR","symbol":"009830","company_name":"한화솔루션","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T009830-S2-20220817","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"IRA policy bridge included capacity/margin route; not a price-only policy theme."}
{"row_type":"case","case_id":"C31-112610-IRA-WIND","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T112610-S2-20220817","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"IRA wind/tax-credit route linked to order/backlog/margin bridge."}
{"row_type":"case","case_id":"C31-001470-UKR-REBUILD","symbol":"001470","company_name":"삼부토건","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"T001470-S2-20230522","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"outcome_not_valid_positive_evidence","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Extreme MFE was event premium; no funded order/project bridge at trigger."}
{"row_type":"case","case_id":"C31-053290-POLICY-THEME","symbol":"053290","company_name":"NE능률","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"T053290-S2-20210304","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"outcome_not_valid_positive_evidence","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Political/policy theme had no company-specific cashflow bridge."}
{"row_type":"case","case_id":"C31-336260-HYDROGEN-POLICY","symbol":"336260","company_name":"두산퓨얼셀","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T336260-S2-20220811","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_corrected_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Hydrogen policy rally failed to convert into durable order/revision evidence within tested window."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T009830-S2-20220817","case_id":"C31-009830-IRA-SOLAR","symbol":"009830","company_name":"한화솔루션","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","entry_date":"2022-08-17","entry_price":46550,"evidence_available_at_that_date":"IRA signed; solar manufacturing/tax-credit policy route visible; company capacity/margin bridge plausible","evidence_source":"historical public policy event + company policy-to-capacity narrative","stage2_evidence_fields":["policy_or_regulatory_optionality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.09,"MFE_90D_pct":20.09,"MFE_180D_pct":22.45,"MFE_1Y_pct":22.45,"MFE_2Y_pct":null,"MAE_30D_pct":-3.11,"MAE_90D_pct":-3.11,"MAE_180D_pct":-16.00,"MAE_1Y_pct":-17.72,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-31","peak_price":57000,"drawdown_after_peak_pct":-32.54,"green_lateness_ratio":0.81,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G009830-20220817","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T009830-YELLOW-20221124","case_id":"C31-009830-IRA-SOLAR","symbol":"009830","company_name":"한화솔루션","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","trigger_type":"Stage3-Yellow","trigger_date":"2022-11-24","entry_date":"2022-11-24","entry_price":54000,"evidence_available_at_that_date":"policy bridge had become more consensus-visible; used for lateness comparison only","evidence_source":"historical public market/research confirmation proxy","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":["margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.74,"MFE_90D_pct":5.56,"MFE_180D_pct":5.56,"MAE_30D_pct":-18.33,"MAE_90D_pct":-27.59,"MAE_180D_pct":-29.72,"peak_date":"2023-03-31","peak_price":57000,"drawdown_after_peak_pct":-32.54,"green_lateness_ratio":0.81,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"label_comparison_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G009830-20221124","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T112610-S2-20220817","case_id":"C31-112610-IRA-WIND","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","entry_date":"2022-08-17","entry_price":63600,"evidence_available_at_that_date":"IRA wind/tax-credit policy route visible with order/backlog bridge","evidence_source":"historical public policy event + wind-tower order/backlog narrative","stage2_evidence_fields":["policy_or_regulatory_optionality","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["margin_bridge","durable_customer_confirmation","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.64,"MFE_90D_pct":26.57,"MFE_180D_pct":38.52,"MFE_1Y_pct":38.52,"MFE_2Y_pct":null,"MAE_30D_pct":-6.76,"MAE_90D_pct":-10.85,"MAE_180D_pct":-10.85,"MAE_1Y_pct":-10.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-24","peak_price":88100,"drawdown_after_peak_pct":-12.94,"green_lateness_ratio":0.50,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G112610-20220817","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T112610-YELLOW-20221116","case_id":"C31-112610-IRA-WIND","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","trigger_type":"Stage3-Yellow","trigger_date":"2022-11-16","entry_date":"2022-11-16","entry_price":75800,"evidence_available_at_that_date":"order/tax-credit bridge more visible; lateness comparison only","evidence_source":"historical confirmation proxy","stage2_evidence_fields":["policy_or_regulatory_optionality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["durable_customer_confirmation","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.54,"MFE_90D_pct":16.23,"MFE_180D_pct":16.23,"MAE_30D_pct":-9.10,"MAE_90D_pct":-17.94,"MAE_180D_pct":-17.94,"peak_date":"2023-04-24","peak_price":88100,"drawdown_after_peak_pct":-12.94,"green_lateness_ratio":0.50,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"label_comparison_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G112610-20221116","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T001470-S2-20230522","case_id":"C31-001470-UKR-REBUILD","symbol":"001470","company_name":"삼부토건","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable-label-comparison","trigger_date":"2023-05-19","entry_date":"2023-05-22","entry_price":1496,"evidence_available_at_that_date":"Ukraine reconstruction/geopolitical headline + relative strength; no funded project/order bridge at trigger","evidence_source":"historical public geopolitical event headline proxy","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001470/2023.csv","profile_path":"atlas/symbol_profiles/001/001470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":183.09,"MFE_90D_pct":267.65,"MFE_180D_pct":267.65,"MFE_1Y_pct":267.65,"MFE_2Y_pct":null,"MAE_30D_pct":-21.66,"MAE_90D_pct":-21.66,"MAE_180D_pct":-21.66,"MAE_1Y_pct":-21.66,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-07-17","peak_price":5500,"drawdown_after_peak_pct":-55.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G001470-20230522","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T001470-4B-20230717","case_id":"C31-001470-UKR-REBUILD","symbol":"001470","company_name":"삼부토건","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","trigger_type":"4B_overlay_only","trigger_date":"2023-07-17","entry_date":"2023-07-17","entry_price":5010,"evidence_available_at_that_date":"price-only local peak / positioning overheat; no non-price 4B evidence","evidence_source":"stock-web price path overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001470/2023.csv","profile_path":"atlas/symbol_profiles/001/001470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_90D_pct":9.78,"MAE_90D_pct":-51.70,"peak_date":"2023-07-17","peak_price":5500,"drawdown_after_peak_pct":-55.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"price_only_event_premium_cap_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G001470-20230717","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T053290-S2-20210304","case_id":"C31-053290-POLICY-THEME","symbol":"053290","company_name":"NE능률","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable-label-comparison","trigger_date":"2021-03-04","entry_date":"2021-03-04","entry_price":4450,"evidence_available_at_that_date":"political/education policy theme + relative strength; no company-specific contract/revision bridge","evidence_source":"historical public political theme proxy","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv","profile_path":"atlas/symbol_profiles/053/053290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":476.40,"MFE_90D_pct":591.01,"MFE_180D_pct":591.01,"MFE_1Y_pct":591.01,"MFE_2Y_pct":null,"MAE_30D_pct":-21.24,"MAE_90D_pct":-21.24,"MAE_180D_pct":-21.24,"MAE_1Y_pct":-21.24,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-06-09","peak_price":30750,"drawdown_after_peak_pct":-56.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"false_break","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G053290-20210304","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T053290-4B-20210407","case_id":"C31-053290-POLICY-THEME","symbol":"053290","company_name":"NE능률","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","trigger_type":"4B_overlay_only","trigger_date":"2021-04-07","entry_date":"2021-04-07","entry_price":23000,"evidence_available_at_that_date":"price-only local blowoff; no non-price 4B evidence","evidence_source":"stock-web price path overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv","profile_path":"atlas/symbol_profiles/053/053290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_90D_pct":33.70,"MAE_90D_pct":-29.78,"peak_date":"2021-06-09","peak_price":30750,"drawdown_after_peak_pct":-56.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.71,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G053290-20210407","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T336260-S2-20220811","case_id":"C31-336260-HYDROGEN-POLICY","symbol":"336260","company_name":"두산퓨얼셀","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable-label-comparison","trigger_date":"2022-08-11","entry_date":"2022-08-11","entry_price":40350,"evidence_available_at_that_date":"hydrogen policy/subsidy headline + relative strength; no durable order/revision bridge yet","evidence_source":"historical public policy headline proxy","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv","profile_path":"atlas/symbol_profiles/336/336260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.23,"MFE_90D_pct":2.23,"MFE_180D_pct":2.23,"MFE_1Y_pct":2.23,"MFE_2Y_pct":null,"MAE_30D_pct":-16.98,"MAE_90D_pct":-39.41,"MAE_180D_pct":-39.41,"MAE_1Y_pct":-39.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-16","peak_price":41250,"drawdown_after_peak_pct":-40.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"failed_policy_to_order_conversion_not_successful_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G336260-20220811","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T336260-4C-20221013","case_id":"C31-336260-HYDROGEN-POLICY","symbol":"336260","company_name":"두산퓨얼셀","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_TO_CASHFLOW_BRIDGE_VS_EVENT_PREMIUM","trigger_type":"4C_overlay_only","trigger_date":"2022-10-13","entry_date":"2022-10-13","entry_price":24450,"evidence_available_at_that_date":"policy-to-order conversion failure visible through price path and absence of durable revision bridge","evidence_source":"historical policy conversion failure proxy + stock-web price path","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken","forced_liquidation_or_crash"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv","profile_path":"atlas/symbol_profiles/336/336260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_90D_pct":52.15,"MAE_90D_pct":-2.25,"peak_date":"2022-11-17","peak_price":37450,"drawdown_after_peak_pct":-17.49,"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G336260-20221013","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-009830-IRA-SOLAR","trigger_id":"T009830-S2-20220817","symbol":"009830","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":68,"revision_score":58,"relative_strength_score":64,"customer_quality_score":55,"policy_or_regulatory_score":85,"valuation_repricing_score":62,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":72,"revision_score":60,"relative_strength_score":64,"customer_quality_score":55,"policy_or_regulatory_score":90,"valuation_repricing_score":62,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"policy_to_cashflow_bridge_score":85},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["policy_to_cashflow_bridge_score","margin_bridge_score","revision_score"],"component_delta_explanation":"C31 bridge exists, so Stage2/Yellow support remains valid without relaxing Green.","MFE_90D_pct":20.09,"MAE_90D_pct":-3.11,"score_return_alignment_label":"score_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-112610-IRA-WIND","trigger_id":"T112610-S2-20220817","symbol":"112610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":48,"backlog_visibility_score":65,"margin_bridge_score":62,"revision_score":55,"relative_strength_score":66,"customer_quality_score":68,"policy_or_regulatory_score":85,"valuation_repricing_score":58,"execution_risk_score":32,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":70,"margin_bridge_score":68,"revision_score":58,"relative_strength_score":66,"customer_quality_score":72,"policy_or_regulatory_score":90,"valuation_repricing_score":58,"execution_risk_score":32,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5,"policy_to_cashflow_bridge_score":88},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["policy_to_cashflow_bridge_score","backlog_visibility_score","customer_quality_score"],"component_delta_explanation":"C31 bridge exists through order/backlog/tax-credit conversion; keep as positive structural case.","MFE_90D_pct":26.57,"MAE_90D_pct":-10.85,"score_return_alignment_label":"score_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-001470-UKR-REBUILD","trigger_id":"T001470-S2-20230522","symbol":"001470","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":95,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":30,"execution_risk_score":85,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":40,"accounting_trust_risk_score":35},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable-risky","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":25,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":10,"execution_risk_score":90,"legal_or_contract_risk_score":75,"dilution_cb_risk_score":45,"accounting_trust_risk_score":35,"policy_to_cashflow_bridge_score":0,"event_premium_cap_score":100},"weighted_score_after":45,"stage_label_after":"Event-Watch / Narrative-only","changed_components":["policy_to_cashflow_bridge_score","event_premium_cap_score","relative_strength_score"],"component_delta_explanation":"Extreme MFE is not valid positive evidence because no funded order/project bridge existed at trigger.","MFE_90D_pct":267.65,"MAE_90D_pct":-21.66,"score_return_alignment_label":"outcome_not_valid_positive_evidence","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-053290-POLICY-THEME","trigger_id":"T053290-S2-20210304","symbol":"053290","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":100,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":25,"execution_risk_score":90,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":20,"accounting_trust_risk_score":25},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable-risky","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":30,"valuation_repricing_score":5,"execution_risk_score":95,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":20,"accounting_trust_risk_score":25,"policy_to_cashflow_bridge_score":0,"event_premium_cap_score":100},"weighted_score_after":40,"stage_label_after":"Narrative-only / Event-Watch","changed_components":["policy_to_cashflow_bridge_score","event_premium_cap_score","relative_strength_score"],"component_delta_explanation":"Political/policy affinity has no company cashflow bridge; cap despite huge MFE.","MFE_90D_pct":591.01,"MAE_90D_pct":-21.24,"score_return_alignment_label":"outcome_not_valid_positive_evidence","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-336260-HYDROGEN-POLICY","trigger_id":"T336260-S2-20220811","symbol":"336260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":15,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":75,"customer_quality_score":20,"policy_or_regulatory_score":80,"valuation_repricing_score":35,"execution_risk_score":65,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable-risky","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":0,"relative_strength_score":35,"customer_quality_score":10,"policy_or_regulatory_score":50,"valuation_repricing_score":10,"execution_risk_score":85,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"policy_to_cashflow_bridge_score":10,"failed_policy_to_order_conversion_score":85},"weighted_score_after":55,"stage_label_after":"Event-Watch / 4C-watch","changed_components":["policy_to_cashflow_bridge_score","failed_policy_to_order_conversion_score","revision_score"],"component_delta_explanation":"Policy headline did not convert into durable order/revision; high MAE requires guard.","MFE_90D_pct":2.23,"MAE_90D_pct":-39.41,"score_return_alignment_label":"score_corrected_false_positive","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See Section 24 CSV block.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_headline_plus_relative_strength_false_positive","event_premium_mfe_contaminates_positive_weight","failed_policy_to_order_conversion","price_only_local_4b_not_full_4b"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"C31-001470-UKR-REBUILD","symbol":"001470","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"policy/geopolitical headline had no funded project/order bridge at trigger; MFE retained only for event-premium red-team calibration","price_source":"Songdaiki/stock-web","usage":"not_positive_weight_calibration"}
{"row_type":"narrative_only","case_id":"C31-053290-POLICY-THEME","symbol":"053290","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"political/policy theme had no company cashflow bridge; MFE retained only for event-premium red-team calibration","price_source":"Songdaiki/stock-web","usage":"not_positive_weight_calibration"}
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
next_round = R11_loop_11_or_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
preferred_next_scope = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
reason = C31 now has policy-to-cashflow bridge and event-premium cap; next L10 residual gap is governance/control premium/tender cap.
```

## 28. Source Notes

Stock-web source files inspected in this loop:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/009/009830.json
atlas/symbol_profiles/112/112610.json
atlas/symbol_profiles/001/001470.json
atlas/symbol_profiles/053/053290.json
atlas/symbol_profiles/336/336260.json
atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv
atlas/ohlcv_tradable_by_symbol_year/009/009830/2023.csv
atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv
atlas/ohlcv_tradable_by_symbol_year/112/112610/2023.csv
atlas/ohlcv_tradable_by_symbol_year/001/001470/2023.csv
atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv
atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv
```

Allowed stock_agent research artifacts inspected for coverage only:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/applied_scoring_diff.md
```

No stock_agent source code was opened, inferred, or patched.
