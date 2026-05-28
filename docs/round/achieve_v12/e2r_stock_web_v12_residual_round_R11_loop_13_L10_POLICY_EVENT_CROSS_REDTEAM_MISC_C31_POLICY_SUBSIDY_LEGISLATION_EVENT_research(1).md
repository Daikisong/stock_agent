# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R11
loop = 13
selection_mode = auto_coverage_gap_fill
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = IRA_CLEAN_ENERGY_TAX_CREDIT_POLICY_EVENT_TO_COMPANY_SPECIFIC_ORDER_REVISION_GUARD
loop_objective = residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | coverage_gap_fill | counterexample_mining
output_file = e2r_stock_web_v12_residual_round_R11_loop_13_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live watchlist, not current stock discovery, not an investment recommendation, and not an implementation patch.

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

The purpose of this loop is not to prove those global axes again. The residual question is narrower: **inside C31 policy/subsidy/legislation events, when does a policy headline become company-specific earnings evidence, and when is it only theme beta?**

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R11 |
| loop | 13 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | IRA_CLEAN_ENERGY_TAX_CREDIT_POLICY_EVENT_TO_COMPANY_SPECIFIC_ORDER_REVISION_GUARD |
| selected coverage gap | R11/C31 under explicit v12 canonical schema |
| primary event family | 2022 U.S. Inflation Reduction Act clean-energy tax-credit shock |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for coverage and duplicate avoidance. `data/e2r/calibration/md_registry.jsonl` shows R11 policy/geopolitics/disaster/event loops 1-8 already existed, but the accessible registry did not expose a v12 canonical `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` row. The representative trigger file is currently empty in the fetched artifact view, so this loop treats C31 as a canonical-compression and coverage-gap fill target rather than a code-level implementation task. fileciteturn1052file0L12-L19 fileciteturn1053file0L1-L3

Duplicate avoidance:

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 1
new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

| Field | Value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The manifest states that the atlas is raw/unadjusted, that zero-volume and invalid OHLC rows are excluded from calibration shards, and that corporate-action-contaminated windows are blocked by default. fileciteturn1049file0L4-L60 Schema validation confirms the tradable shard columns and calibration rules used here. fileciteturn1050file0L17-L28 fileciteturn1050file0L60-L68

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward available | corporate action 180D status | calibration_usable | reason |
|---|---:|---:|---:|---|---:|---|
| R11L13_C31_CS_WIND_IRA_WIND_TOWER_POSITIVE | 112610 | 2022-07-29 | yes | clean_180D_window | true | no 2022-2023 corporate-action candidate overlap; profile candidates are 2021 only |
| R11L13_C31_HD_ENERGY_IRA_SOLAR_POSITIVE_HIGH_MAE | 322000 | 2022-07-29 | yes | clean_180D_window | true | profile has no corporate-action candidates |
| R11L13_C31_DOOSAN_FUELCELL_HYDROGEN_POLICY_COUNTEREX | 336260 | 2022-07-29 | yes | clean_180D_window | true | profile has no corporate-action candidates |
| R11L13_C31_UNISON_IRA_WIND_THEME_COUNTEREX | 018000 | 2022-07-29 | yes | clean_180D_window | true | profile corporate-action candidates do not overlap 2022-07-29~D+180 |
| R11L13_C31_HANWHA_QCELLS_IRA_NARRATIVE_ONLY | 009830 | 2022-07-29 | yes but structurally noisy | blocked_for_weight_calibration | false | 2023 demerger/suspension-like gap and share-count discontinuity; narrative only |

Profile evidence: CS Wind profile lists corporate-action candidates only in February/March 2021, outside this loop's window. fileciteturn1063file0L118-L122 HD현대에너지솔루션 and 두산퓨얼셀 profiles show zero corporate-action candidates. fileciteturn1068file0L90-L100 fileciteturn1072file0L85-L96 유니슨 profile has corporate-action candidates, but the nearest later one is 2024-05-21, outside the 2022-07-29 180D window. fileciteturn1077file0L34-L46

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| IRA_WIND_TOWER_MANUFACTURING_CREDIT_ORDER_VISIBILITY | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | direct policy subsidy / manufacturing credit to wind tower order visibility |
| IRA_SOLAR_MODULE_POLICY_EVENT_WITH_HIGH_MAE | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy subsidy winner, but post-peak MAE requires 4B overlay |
| IRA_HYDROGEN_CREDIT_POLICY_ONLY_LOCAL_BLOWOFF | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy-only hydrogen theme beta without issuer-specific revision closure |
| IRA_WIND_POLICY_THEME_WITHOUT_CUSTOMER_QUALITY | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | broad wind theme proxy without customer/order quality |
| IRA_QCELLS_POLICY_WIN_BUT_STOCK_WEB_DEMERGER_WINDOW_BLOCKED | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | narrative coverage only due stock-web window block |

## 7. Case Selection Summary

The event anchor is the late-July 2022 Manchin-Schumer Inflation Reduction Act agreement, followed by Senate passage on August 7, House passage on August 12, and signing on August 16, 2022. The IRA created clean-energy tax-credit optionality for renewable energy, EVs, manufacturing, hydrogen, and related supply chains. citeturn811501search3 citeturn608525news2

The selected cases intentionally mix direct policy-to-order candidates and policy-only theme beta:

| case_id | role | reason |
|---|---|---|
| CS Wind | structural_success | wind-tower/manufacturing exposure aligned with the policy shock and produced durable 90D/180D MFE |
| HD현대에너지솔루션 | high_mae_success | strong solar-policy MFE, but deep post-peak drawdown demanded high-MAE/4B overlay |
| 두산퓨얼셀 | failed_rerating | hydrogen/fuel-cell policy optionality produced local spike but failed the durable rerating test |
| 유니슨 | failed_rerating | wind theme beta without order/customer quality faded into large MAE |
| 한화솔루션/Qcells | narrative_only | strong real-world IRA linkage, but stock-web 180D calibration is blocked by structural price-window caveat |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
representative_trigger_count = 4
current_profile_error_count = 3
```

The central residual is not that policy events are useless. It is that C31 has two organisms wearing the same costume: a policy subsidy that closes into company-specific order/revision evidence, and a policy headline that merely gives a theme a sugar rush. The former can remain Stage2-Actionable/Yellow; the latter should be capped until issuer-level evidence arrives.

## 9. Evidence Source Map

| Evidence family | Public evidence date | Interpretation |
|---|---:|---|
| IRA clean-energy agreement | 2022-07-27 / 2022-07-28 market reaction | first tradable policy shock for Korean clean-energy names |
| IRA signed into law | 2022-08-16 | legal completion; useful as confirmation, not as first trigger |
| Qcells DOE loan guarantee | 2024-08-08 | validates Hanwha/Qcells' direct policy channel later, but not usable for 2022 entry-weight calibration |
| 2025 clean-energy credit rollback proposals | 2025-05~06 | confirms policy-risk reversal path; not used as positive entry training |

Reuters reported that the U.S. DOE offered a conditional loan guarantee to Qcells for a Georgia solar manufacturing facility, explicitly linking the facility to IRA clean-energy manufacturing incentives. citeturn206948news0 Reuters and Investopedia also reported 2025 attempts to phase down or repeal wind/solar tax credits, useful as later policy-risk stress evidence rather than an entry promotion axis. citeturn641480news2 citeturn811501news1

## 10. Price Data Source Map

| symbol | company_name | profile_path | key price shard(s) |
|---:|---|---|---|
| 112610 | 씨에스윈드 | atlas/symbol_profiles/112/112610.json | atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv; 2023.csv |
| 322000 | HD현대에너지솔루션 | atlas/symbol_profiles/322/322000.json | atlas/ohlcv_tradable_by_symbol_year/322/322000/2022.csv; 2023.csv |
| 336260 | 두산퓨얼셀 | atlas/symbol_profiles/336/336260.json | atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv; 2023.csv |
| 018000 | 유니슨 | atlas/symbol_profiles/018/018000.json | atlas/ohlcv_tradable_by_symbol_year/018/018000/2022.csv; 2023.csv |
| 009830 | 한화솔루션 | atlas/symbol_profiles/009/009830.json | atlas/ohlcv_tradable_by_symbol_year/009/009830/2022.csv; 2023.csv |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | current_profile_verdict | trigger_outcome_label | usable |
|---|---:|---|---:|---:|---:|---|---|---:|
| R11L13_C31_CS_WIND_IRA_WIND_TOWER_POSITIVE | 112610 | Stage2-Actionable | 2022-07-28 | 2022-07-29 | 55500 | current_profile_correct | policy_to_order_visibility_success | true |
| R11L13_C31_HD_ENERGY_IRA_SOLAR_POSITIVE_HIGH_MAE | 322000 | Stage2-Actionable | 2022-07-28 | 2022-07-29 | 50500 | current_profile_too_early | high_mfe_but_policy_spike_fragile | true |
| R11L13_C31_DOOSAN_FUELCELL_HYDROGEN_POLICY_COUNTEREX | 336260 | Stage2-Actionable | 2022-07-28 | 2022-07-29 | 32900 | current_profile_false_positive | policy_only_local_peak_failed_rerating | true |
| R11L13_C31_UNISON_IRA_WIND_THEME_COUNTEREX | 018000 | Stage2-Actionable | 2022-07-28 | 2022-07-29 | 2515 | current_profile_false_positive | broad_policy_theme_failed_without_customer_quality | true |
| R11L13_C31_HANWHA_QCELLS_IRA_NARRATIVE_ONLY | 009830 | Stage2-Actionable | 2022-07-28 | 2022-07-29 | 43800 | current_profile_data_insufficient | narrative_positive_but_blocked_by_structural_price_window | false |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L13_C31_CS_20220729_STAGE2A | 55500 | 27.93 | 45.05 | 45.05 | -4.50 | -4.50 | -4.50 | 2022-11-28 | 80500 | -23.23 |
| R11L13_C31_HDENERGY_20220729_STAGE2A | 50500 | 70.69 | 70.69 | 70.69 | -8.91 | -8.91 | -8.91 | 2022-09-15 | 86200 | -46.64 |
| R11L13_C31_DFC_20220729_STAGE2A | 32900 | 25.38 | 25.38 | 25.38 | -1.82 | -28.12 | -28.12 | 2022-08-16 | 41250 | -42.67 |
| R11L13_C31_UNISON_20220729_STAGE2A | 2515 | 14.31 | 14.31 | 14.31 | -5.77 | -29.42 | -38.97 | 2022-08-25 | 2875 | -46.61 |
| R11L13_C31_HANWHA_20220729_NARRATIVE | 43800 | 27.63 | 27.63 | null | -4.68 | -4.68 | null | 2022-09-15 | 55900 | null |


Observed price anchors:

- CS Wind's 2022-07-29 entry close was 55,500, and subsequent rows show the policy shock moving through the August/November path up to an 80,500 high on 2022-11-28. fileciteturn1065file0L15-L26 fileciteturn1066file0L34-L47
- HD현대에너지솔루션's 2022-07-29 entry close was 50,500, with a 86,200 high on 2022-09-15; this produced the strongest MFE but also the most fragile post-peak path. fileciteturn1069file0L15-L24 fileciteturn1069file0L44-L48
- 두산퓨얼셀 spiked to 41,250 by 2022-08-16, then fell to 23,650 by 2022-10-17, turning the policy move into a failed rerating example. fileciteturn1073file0L16-L28 fileciteturn1074file0L12-L17
- 유니슨's 2022-07-29 entry close was 2,515; the brief high was 2,875, but the 180D path reached a low around 1,535~1,551, making it a policy-theme counterexample. fileciteturn1078file0L16-L25 fileciteturn1080file0L4-L12 fileciteturn1080file0L59-L61

## 13. Current Calibrated Profile Stress Test

| case | current profile likely label | verdict | why |
|---|---|---|---|
| CS Wind | Stage3-Yellow after Stage2-Actionable | current_profile_correct | policy evidence + relative strength + later order visibility align with durable MFE |
| HD현대에너지솔루션 | Stage3-Yellow / possible too-fast promotion | current_profile_too_early | high MFE was real, but post-peak drawdown shows policy winner still needed 4B overlay |
| 두산퓨얼셀 | Stage2-Actionable or weak Yellow due hydrogen policy optionality | current_profile_false_positive | local spike did not close into earnings/revision; MAE exceeded MFE by 90D/180D |
| 유니슨 | Stage2-Actionable due wind policy beta | current_profile_false_positive | no customer/order quality; broad theme faded |
| 한화솔루션 | Stage3-Yellow narrative | current_profile_data_insufficient | direct policy link exists, but calibration price window is blocked |

Existing axes tested:

```text
stage2_actionable_evidence_bonus = existing_axis_kept
stage3_yellow_total_min = existing_axis_kept_but_C31_guard_needed
stage3_green_total_min = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened_within_C31
full_4b_requires_non_price_evidence = existing_axis_strengthened_within_C31
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is assigned in this loop because the purpose is to test **policy event entry** rather than later earnings revision confirmation. Therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C31-specific inference: policy events can justify Stage2-Actionable when the event is concrete and the symbol has direct exposure. Yellow should require at least one of customer/order quality, financial visibility, or repeat conversion. Green should not be generated by policy-event price action alone.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---|
| CS Wind | 80,500 | n/a | n/a | structural positive; 4B overlay not central |
| HD현대에너지솔루션 | 86,200 | 1.00 | 1.00 | high-MFE success, but peak-to-trough drawdown of roughly -46.6% means a 4B risk overlay was needed |
| 두산퓨얼셀 | 41,250 | 1.00 | 1.00 | policy-only local 4B should not become full 4B unless non-price evidence confirms thesis fatigue |
| 유니슨 | 2,875 | 1.00 | 1.00 | price-only local peak; full 4B should remain an overlay, not positive entry training |

C31 lesson: in subsidy/legislation events, price-only local peaks are common. They are useful for risk annotation, but they must not become a full 4B without non-price evidence such as subsidy rollback, contract delay, qualification failure, or margin/revision break.

## 16. 4C Protection Audit

No hard 4C entry is trained in this file. 두산퓨얼셀 and 유니슨 are thesis-break watch examples, not hard 4C rows. The correct label is:

```text
four_c_protection_label = thesis_break_watch_only
```

Reason: the policy thesis was weak or unclosed, but there was no single issuer-specific cancellation/rejection event in the trigger window. Treating them as 4C would overfit price decline.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = evidence is concentrated in L10/C31; not enough cross-sector breadth for a sector-wide L10 rule.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
axis_1 = c31_company_specific_benefit_closure_required
axis_2 = c31_policy_only_theme_cap
axis_3 = c31_high_mae_policy_success_overlay
```

Proposed C31 shadow rule:

```text
if trigger is policy/subsidy/legislation event:
    allow Stage2-Actionable only when public policy event is concrete and symbol exposure is direct
    allow Stage3-Yellow only when issuer-level bridge exists:
        customer/order quality OR capacity route OR confirmed financial visibility OR repeat conversion
    block Stage3-Green when evidence is policy-only or price-only
    cap policy-only theme beta at Stage2-Watch/Actionable
    mark high-MFE but high-drawdown policy winners as high_mae_success and attach 4B overlay
```

## 19. Before / After Backtest Comparison

| profile_id | selected triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 4 | 38.86 | -17.74 | 38.86 | -20.12 | 0.50 | mixed_policy_beta_false_positive |
| P0b_e2r_2_0_baseline_reference | 4 | 38.86 | -17.74 | 38.86 | -20.12 | 0.50 | weaker_than_current |
| P1_sector_specific_candidate_profile | 2 | 57.87 | -6.71 | 57.87 | -6.71 | 0.00 | better_precision |
| P2_canonical_archetype_candidate_profile | 2 | 57.87 | -6.71 | 57.87 | -6.71 | 0.00 | best_alignment |
| P3_counterexample_guard_profile | 1 | 45.05 | -4.50 | 45.05 | -4.50 | 0.00 | high_precision_but_may_miss_high_mae_success |


## 20. Score-Return Alignment Matrix

| symbol | before_score | before_label | after_score | after_label | MFE_90D | MAE_90D | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 112610 | 78.00 | Stage3-Yellow | 82.00 | Stage3-Yellow | 45.05 | -4.50 | aligned_positive |
| 322000 | 76.00 | Stage3-Yellow | 78.00 | Stage3-Yellow_guarded | 70.69 | -8.91 | positive_but_guard_required |
| 336260 | 74.00 | Stage3-Yellow_candidate | 66.00 | Stage2-Watch | 25.38 | -28.12 | false_positive_guard |
| 018000 | 72.00 | Stage2-Actionable | 63.00 | Stage2-Watch_or_Blocked | 14.31 | -29.42 | counterexample_guard |
| 009830 | 82.00 | Stage3-Yellow | 82.00 | NarrativeOnly | 27.63 | -4.68 | data_insufficient |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | IRA_CLEAN_ENERGY_TAX_CREDIT_POLICY_EVENT_TO_COMPANY_SPECIFIC_ORDER_REVISION_GUARD | 2 | 3 | 3 | 0 | 5 | 0 | 4 | 4 | 3 | false | true | C31 now has positive/counterexample/high-MAE/narrative-only coverage; needs additional non-clean-energy policy holdout later |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [policy_only_theme_false_positive, high_mfe_high_mae_policy_success, narrative_positive_but_price_window_blocked]
new_axis_proposed: [c31_company_specific_benefit_closure_required, c31_policy_only_theme_cap, c31_high_mae_policy_success_overlay]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage within C31, full_4b_requires_non_price_evidence within C31]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R11_C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema route
- entry_date and entry_price from tradable shards
- 30D/90D/180D MFE/MAE directionality for 4 calibration-usable cases
- positive/counterexample balance
- C31-specific residual false-positive guard
- narrative-only handling for structurally noisy price window
```

Not validated:

```text
- production scoring code
- stock_agent src/e2r internals
- live 2026 candidate scan
- automated trading
- brokerage API
- global weight promotion
- non-clean-energy policy holdout families
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_company_specific_benefit_closure_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,Policy/legislation headline alone created two false-positive paths; require issuer-level customer/order/revision bridge for promotion.,false_positive_rate falls from 50% to 0% on four usable cases while retaining two positives.,R11L13_C31_CS_20220729_STAGE2A|R11L13_C31_HDENERGY_20220729_STAGE2A|R11L13_C31_DFC_20220729_STAGE2A|R11L13_C31_UNISON_20220729_STAGE2A,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c31_policy_only_theme_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,Policy-only theme beta should be capped at Stage2-Watch/Actionable and cannot cross Yellow unless order/customer quality closes.,Blocks Doosan Fuel Cell and Unison false positives without removing policy optionality.,R11L13_C31_DFC_20220729_STAGE2A|R11L13_C31_UNISON_20220729_STAGE2A,2,2,2,medium,counterexample_guard,not production; post-calibrated residual
shadow_weight,c31_high_mae_policy_success_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,Some policy winners produce large MFE but also deep post-peak drawdown; mark high-MAE success separately from clean structural success.,HD현대에너지솔루션 remains positive but receives 4B overlay after local peak.,R11L13_C31_HDENERGY_20220729_STAGE2A,1,1,0,low,risk_overlay,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R11L13_C31_CS_WIND_IRA_WIND_TOWER_POSITIVE","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_WIND_TOWER_MANUFACTURING_CREDIT_ORDER_VISIBILITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R11L13_C31_CS_20220729_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Manchin-Schumer IRA agreement created clean-energy tax credit optionality; CS Wind had direct wind tower/manufacturing exposure and later price path aligned with the policy-to-order route."}
{"row_type":"case","case_id":"R11L13_C31_HD_ENERGY_IRA_SOLAR_POSITIVE_HIGH_MAE","symbol":"322000","company_name":"HD현대에너지솔루션","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_SOLAR_MODULE_POLICY_EVENT_WITH_HIGH_MAE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R11L13_C31_HDENERGY_20220729_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_guard_required","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Solar module exposure made the IRA policy shock tradeable, but the drawdown after peak shows why C31 needs high-MAE/4B overlay handling."}
{"row_type":"case","case_id":"R11L13_C31_DOOSAN_FUELCELL_HYDROGEN_POLICY_COUNTEREX","symbol":"336260","company_name":"두산퓨얼셀","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_HYDROGEN_CREDIT_POLICY_ONLY_LOCAL_BLOWOFF","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R11L13_C31_DFC_20220729_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"IRA contained hydrogen/fuel-cell incentives, but the stock path behaved like policy-only theme beta rather than company-specific earnings closure."}
{"row_type":"case","case_id":"R11L13_C31_UNISON_IRA_WIND_THEME_COUNTEREX","symbol":"018000","company_name":"유니슨","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_WIND_POLICY_THEME_WITHOUT_CUSTOMER_QUALITY","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R11L13_C31_UNISON_20220729_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Wind policy narrative moved the stock briefly, but customer/order quality was not strong enough to create durable rerating."}
{"row_type":"case","case_id":"R11L13_C31_HANWHA_QCELLS_IRA_NARRATIVE_ONLY","symbol":"009830","company_name":"한화솔루션","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_QCELLS_POLICY_WIN_BUT_STOCK_WEB_DEMERGER_WINDOW_BLOCKED","case_type":"narrative_only","positive_or_counterexample":"counterexample","best_trigger":"R11L13_C31_HANWHA_20220729_NARRATIVE","calibration_usable":false,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"score_price_alignment":"data_insufficient","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Qcells/Hanwha had direct IRA linkage and later DOE loan guarantee evidence, but the 2023 demerger/suspension-like window makes this row narrative-only for weight calibration."}
{"row_type":"trigger","trigger_id":"R11L13_C31_CS_20220729_STAGE2A","case_id":"R11L13_C31_CS_WIND_IRA_WIND_TOWER_POSITIVE","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_WIND_TOWER_MANUFACTURING_CREDIT_ORDER_VISIBILITY","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | coverage_gap_fill | counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"Manchin-Schumer IRA agreement created clean-energy tax credit optionality; CS Wind had direct wind tower/manufacturing exposure and later price path aligned with the policy-to-order route.","evidence_source":"public legislation/news; stock-web OHLC atlas; see Source Notes","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":55500,"MFE_30D_pct":27.93,"MFE_90D_pct":45.05,"MFE_180D_pct":45.05,"MFE_1Y_pct":45.05,"MFE_2Y_pct":null,"MAE_30D_pct":-4.5,"MAE_90D_pct":-4.5,"MAE_180D_pct":-4.5,"MAE_1Y_pct":-23.78,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2022-11-28","peak_price":80500,"drawdown_after_peak_pct":-23.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_overlay_needed_after_peak","four_b_evidence_type":["price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"policy_to_order_visibility_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_CS_WIND_IRA_WIND_TOWER_POSITIVE__2022-07-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_HDENERGY_20220729_STAGE2A","case_id":"R11L13_C31_HD_ENERGY_IRA_SOLAR_POSITIVE_HIGH_MAE","symbol":"322000","company_name":"HD현대에너지솔루션","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_SOLAR_MODULE_POLICY_EVENT_WITH_HIGH_MAE","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | coverage_gap_fill | counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"Solar module exposure made the IRA policy shock tradeable, but the drawdown after peak shows why C31 needs high-MAE/4B overlay handling.","evidence_source":"public legislation/news; stock-web OHLC atlas; see Source Notes","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322000/2022.csv","profile_path":"atlas/symbol_profiles/322/322000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":50500,"MFE_30D_pct":70.69,"MFE_90D_pct":70.69,"MFE_180D_pct":70.69,"MFE_1Y_pct":70.69,"MFE_2Y_pct":null,"MAE_30D_pct":-8.91,"MAE_90D_pct":-8.91,"MAE_180D_pct":-8.91,"MAE_1Y_pct":-15.15,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2022-09-15","peak_price":86200,"drawdown_after_peak_pct":-46.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"4B_overlay_needed_after_peak","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mfe_but_policy_spike_fragile","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_HD_ENERGY_IRA_SOLAR_POSITIVE_HIGH_MAE__2022-07-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_DFC_20220729_STAGE2A","case_id":"R11L13_C31_DOOSAN_FUELCELL_HYDROGEN_POLICY_COUNTEREX","symbol":"336260","company_name":"두산퓨얼셀","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_HYDROGEN_CREDIT_POLICY_ONLY_LOCAL_BLOWOFF","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | coverage_gap_fill | counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"IRA contained hydrogen/fuel-cell incentives, but the stock path behaved like policy-only theme beta rather than company-specific earnings closure.","evidence_source":"public legislation/news; stock-web OHLC atlas; see Source Notes","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv","profile_path":"atlas/symbol_profiles/336/336260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":32900,"MFE_30D_pct":25.38,"MFE_90D_pct":25.38,"MFE_180D_pct":25.38,"MFE_1Y_pct":25.38,"MFE_2Y_pct":null,"MAE_30D_pct":-1.82,"MAE_90D_pct":-28.12,"MAE_180D_pct":-28.12,"MAE_1Y_pct":-28.12,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2022-08-16","peak_price":41250,"drawdown_after_peak_pct":-42.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_only_local_peak_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_DOOSAN_FUELCELL_HYDROGEN_POLICY_COUNTEREX__2022-07-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_UNISON_20220729_STAGE2A","case_id":"R11L13_C31_UNISON_IRA_WIND_THEME_COUNTEREX","symbol":"018000","company_name":"유니슨","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_WIND_POLICY_THEME_WITHOUT_CUSTOMER_QUALITY","sector":"정책·지정학·재난·이벤트","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | coverage_gap_fill | counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"Wind policy narrative moved the stock briefly, but customer/order quality was not strong enough to create durable rerating.","evidence_source":"public legislation/news; stock-web OHLC atlas; see Source Notes","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018000/2022.csv","profile_path":"atlas/symbol_profiles/018/018000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-29","entry_price":2515,"MFE_30D_pct":14.31,"MFE_90D_pct":14.31,"MFE_180D_pct":14.31,"MFE_1Y_pct":14.31,"MFE_2Y_pct":null,"MAE_30D_pct":-5.77,"MAE_90D_pct":-29.42,"MAE_180D_pct":-38.97,"MAE_1Y_pct":-39.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-25","peak_price":2875,"drawdown_after_peak_pct":-46.61,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"broad_policy_theme_failed_without_customer_quality","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_UNISON_IRA_WIND_THEME_COUNTEREX__2022-07-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_CS_WIND_IRA_WIND_TOWER_POSITIVE","trigger_id":"R11L13_C31_CS_20220729_STAGE2A","symbol":"112610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":13,"customer_quality_score":10,"policy_or_regulatory_score":18,"valuation_repricing_score":6,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":10,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":18,"valuation_repricing_score":6,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82.0,"stage_label_after":"Stage3-Yellow","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C31 shadow guard keeps policy optionality, but requires company-specific order/customer/revision closure before promotion; policy-only beta is capped at Stage2-Watch/Actionable.","MFE_90D_pct":45.05,"MAE_90D_pct":-4.5,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_HD_ENERGY_IRA_SOLAR_POSITIVE_HIGH_MAE","trigger_id":"R11L13_C31_HDENERGY_20220729_STAGE2A","symbol":"322000","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":15,"customer_quality_score":4,"policy_or_regulatory_score":18,"valuation_repricing_score":10,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":15,"customer_quality_score":4,"policy_or_regulatory_score":18,"valuation_repricing_score":6,"execution_risk_score":-12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":10},"weighted_score_after":78.0,"stage_label_after":"Stage3-Yellow_guarded","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C31 shadow guard keeps policy optionality, but requires company-specific order/customer/revision closure before promotion; policy-only beta is capped at Stage2-Watch/Actionable.","MFE_90D_pct":70.69,"MAE_90D_pct":-8.91,"score_return_alignment_label":"positive_but_guard_required","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_DOOSAN_FUELCELL_HYDROGEN_POLICY_COUNTEREX","trigger_id":"R11L13_C31_DFC_20220729_STAGE2A","symbol":"336260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":11,"customer_quality_score":2,"policy_or_regulatory_score":16,"valuation_repricing_score":8,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":11,"customer_quality_score":2,"policy_or_regulatory_score":10,"valuation_repricing_score":3,"execution_risk_score":-14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66.0,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C31 shadow guard keeps policy optionality, but requires company-specific order/customer/revision closure before promotion; policy-only beta is capped at Stage2-Watch/Actionable.","MFE_90D_pct":25.38,"MAE_90D_pct":-28.12,"score_return_alignment_label":"false_positive_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_UNISON_IRA_WIND_THEME_COUNTEREX","trigger_id":"R11L13_C31_UNISON_20220729_STAGE2A","symbol":"018000","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":6,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":2,"execution_risk_score":-16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":63.0,"stage_label_after":"Stage2-Watch_or_Blocked","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C31 shadow guard keeps policy optionality, but requires company-specific order/customer/revision closure before promotion; policy-only beta is capped at Stage2-Watch/Actionable.","MFE_90D_pct":14.31,"MAE_90D_pct":-29.42,"score_return_alignment_label":"counterexample_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_HANWHA_QCELLS_IRA_NARRATIVE_ONLY","trigger_id":"R11L13_C31_HANWHA_20220729_NARRATIVE","symbol":"009830","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":13,"policy_or_regulatory_score":18,"valuation_repricing_score":0,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":9},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":13,"policy_or_regulatory_score":18,"valuation_repricing_score":0,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":9},"weighted_score_after":82.0,"stage_label_after":"NarrativeOnly","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C31 shadow guard keeps policy optionality, but requires company-specific order/customer/revision closure before promotion; policy-only beta is capped at Stage2-Watch/Actionable.","MFE_90D_pct":27.63,"MAE_90D_pct":-4.68,"score_return_alignment_label":"data_insufficient","current_profile_verdict":"current_profile_data_insufficient"}
{"row_type":"narrative_only","case_id":"R11L13_C31_HANWHA_QCELLS_IRA_NARRATIVE_ONLY","symbol":"009830","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"stock_web_price_window_blocked_by_2023_demerger_like_structural_window_and_share_count_discontinuity; use for narrative coverage only","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"residual_contribution","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_only_theme_false_positive","high_mfe_high_mae_policy_success","narrative_positive_but_price_window_blocked"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_round = R12
next_large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or relevant sector
next_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
handoff_prompt_executed_now = false
```

## 28. Source Notes

- Stock-Web manifest and schema were fetched from Songdaiki/stock-web. fileciteturn1049file0L4-L60 fileciteturn1050file0L17-L28
- Previous calibration registry was used for coverage/duplicate avoidance only. fileciteturn1052file0L12-L19
- CS Wind, HD현대에너지솔루션, 두산퓨얼셀, 유니슨, and 한화솔루션 profile/price rows were inspected only from profile and OHLC shards under `atlas/`. fileciteturn1063file0L4-L24 fileciteturn1068file0L4-L32 fileciteturn1072file0L4-L28 fileciteturn1076file0L4-L32 fileciteturn1059file0L4-L47
- IRA event chronology and later policy rollback stress context were checked with public sources. citeturn811501search3 citeturn608525news2 citeturn206948news0 citeturn811501news1
