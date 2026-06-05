# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R12_loop_95_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

This file is the corrected final output for this execution. The scheduler state after R11 loop 95 is R12 / loop 95. R12 is the L10 policy/event/cross-redteam/misc round, and this run fills C31 policy/subsidy/legislation event behavior rather than repeating the immediately preceding R12 loop 94 C32 governance/control-premium file.

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
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 95
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_sector_consistency = pass
computed_next_round = R13
computed_next_loop = 95
```

C31 is a policy-to-cashflow bridge archetype. A policy, subsidy, tourism, childcare or legislation headline is the speech; the evidence is budget allocation, channel throughput, customer or visitor conversion, subsidy-to-sales mechanics, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT = 97 rows / 70 symbols / good-bad Stage2 35-25 / 4B-4C 5-0
top covered symbols include 013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
previous R12 loop-89 C31 symbols avoided: 071320, 100220, 339950
previous R12 loop-91 C31 symbols avoided: 272210, 032820, 457550
previous R12 loop-94 C32 symbols avoided: 267250, 034730, 000240
previous R11 loop-94 C31 symbols avoided: 034020, 126880, 119850
previous R11 loop-95 C03 symbols avoided: 272210, 211270, 451760
```

Selected rows avoid hard duplicates and top repeated C31 symbols:

```text
034230 / Stage2-Actionable / 2024-03-07
159580 / Stage2-Actionable / 2024-01-03
407400 / Stage4B / 2024-01-03
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
| 034230 | atlas/symbol_profiles/034/034230.json | no CA candidate; KOSDAQ to KOSPI market transfer continuity noted |
| 159580 | atlas/symbol_profiles/159/159580.json | selected 2024 window clean after old 2018 CA candidate |
| 407400 | atlas/symbol_profiles/407/407400.json | selected 2024 window clean after old 2023 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R12L95_C31_PARADISE_2024_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_POSITIVE | 034230 | 2024-03-07 | yes | 180 | yes | yes | true |
| R12L95_C31_ZEROSEVEN_2024_LOW_BIRTH_POLICY_FALSE_STAGE2 | 159580 | 2024-01-03 | yes | 180 | yes | yes | true |
| R12L95_C31_GGUMBI_2024_INFANT_CARE_POLICY_EVENT_CAP_4B | 407400 | 2024-01-03 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | CASINO_TOURISM_POLICY_CHANNEL_BRIDGE | Positive Stage2 requires policy-to-channel traffic, visitor/drop mix, regulatory visibility, margin and revision bridge. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | LOW_BIRTH_POLICY_FALSE_STAGE2 | Low-birth subsidy watch without budget-to-sales/channel bridge can become false Stage2. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | INFANT_CARE_POLICY_EVENT_CAP_4B | Infant-care policy event premium should route to 4B when subsidy mechanics and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R12L95_C31_PARADISE_2024_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_POSITIVE | 034230 | 파라다이스 | positive | Tourism/casino policy-to-channel recovery produced moderate MFE with controlled early MAE. |
| R12L95_C31_ZEROSEVEN_2024_LOW_BIRTH_POLICY_FALSE_STAGE2 | 159580 | 제로투세븐 | counterexample | Low-birth policy spike lacked subsidy-to-sales and channel/margin bridge. |
| R12L95_C31_GGUMBI_2024_INFANT_CARE_POLICY_EVENT_CAP_4B | 407400 | 꿈비 | counterexample / 4B | Infant-care policy event premium capped on the January spike and then de-rated deeply. |

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
| Paradise tourism/casino policy bridge | historical public/report proxy | true | true | shadow-only positive |
| ZeroToSeven low-birth policy false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Ggumbi infant-care policy event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 034230 | atlas/ohlcv_tradable_by_symbol_year/034/034230/2024.csv | atlas/symbol_profiles/034/034230.json |
| 159580 | atlas/ohlcv_tradable_by_symbol_year/159/159580/2024.csv | atlas/symbol_profiles/159/159580.json |
| 407400 | atlas/ohlcv_tradable_by_symbol_year/407/407400/2024.csv | atlas/symbol_profiles/407/407400.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R12L95_C31_PARADISE_2024_STAGE2_ACTIONABLE_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE | 034230 | Stage2-Actionable | 2024-03-07 | 13550 | positive | casino/tourism policy-channel bridge worked |
| R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH | 159580 | Stage2-Actionable | 2024-01-03 | 8020 | counterexample | low-birth policy false Stage2 |
| R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP | 407400 | Stage4B | 2024-01-03 | 13410 | counterexample/4B | infant-care policy event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R12L95_C31_PARADISE_2024_STAGE2_ACTIONABLE_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE | 13550 | 15.94 | -3.84 | 15.94 | -3.84 | 15.94 | -9.96 | 2024-05-02 | 15710 | -22.34 |
| R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH | 8020 | 7.11 | -19.20 | 7.11 | -32.29 | 7.11 | -40.27 | 2024-01-18 | 8590 | -36.79 |
| R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP | 13410 | 9.62 | -27.37 | 9.62 | -40.79 | 9.62 | -40.79 | 2024-01-03 | 14700 | -45.99 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C31 Stage2 needs budget/subsidy-to-sales/channel/margin/revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing low-birth/childcare policy premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE policy-event rows cannot promote without durable budget/sales bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether policy rhetoric becomes channel traffic or sales mechanics.

| symbol | stage quality | explanation |
|---|---|---|
| 034230 | good_stage2_with_later_watch | Tourism/casino channel bridge produced moderate MFE and controlled early MAE. |
| 159580 | bad_stage2 | Low-birth policy spike lacked sales/reorder/margin bridge and later suffered high MAE. |
| 407400 | good_4B | Infant-care policy event premium capped on the January spike and then drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 159580 low-birth false Stage2 | 0.93 | 0.93 | false Stage2 due missing subsidy-to-sales/channel/margin bridge |
| 407400 infant-care event cap | 0.91 | 0.91 | good 4B timing after January low-birth policy event premium |
| 034230 tourism channel bridge | n/a | n/a | positive Stage2, but later tourism/casino valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 159580 / 407400
```

No hard 4C candidate is introduced in this R12 loop 95 file. The counterexamples are policy-premium/bridge-missing rows, not hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 policy/subsidy/legislation event cases, Stage2 requires verified policy-to-revenue mechanics, budget/subsidy allocation, channel throughput, visitor or customer conversion, sales/reorder durability, margin, or revision bridge. Policy, subsidy, tourism, childcare, low-birth, legislation or theme label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rule = C31 should split true policy-to-channel/budget/sales positives from subsidy-policy false Stage2 and childcare policy event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 10.89 | -25.64 | 0.67 | mixed; C31 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 10.89 | -25.64 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L10 budget/channel/margin bridge required | 2 | 11.53 | -18.07 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C31 bridge vs event-cap split | 2 | 11.53 | -18.07 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing policy themes as positive | 1 | 15.94 | -3.84 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 034230 tourism/casino bridge | 65 | Stage2-Watch | 73 | Stage2-Actionable | 15.94 | -3.84 | casino_tourism_policy_channel_positive |
| 159580 low-birth false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 7.11 | -32.29 | low_birth_policy_false_stage2 |
| 407400 infant-care cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 9.62 | -40.79 | infant_care_policy_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C31 Paradise tourism/casino policy channel positive, ZeroToSeven low-birth policy false Stage2, and Ggumbi infant-care policy event-cap 4B split while avoiding top repeated C31 and previous R12/R11 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: casino_tourism_policy_channel_positive, low_birth_policy_false_stage2, infant_care_policy_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,C31_requires_policy_to_channel_budget_sales_margin_revision_bridge,0,"C31 Stage2 should require policy-to-revenue mechanics, budget/subsidy allocation, channel throughput, visitor or customer conversion, sales/reorder durability, margin, or revision bridge, not policy/subsidy/legislation headline alone","Paradise positive worked; ZeroToSeven and Ggumbi event/watch rows failed positive-stage promotion","R12L95_C31_PARADISE_2024_STAGE2_ACTIONABLE_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE|R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH|R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,cap_bridge_missing_low_birth_and_policy_event_premiums_as_4B_watch,0,"Low-birth, childcare, tourism and other policy premiums can peak before budget, channel and margin bridge is proven","ZeroToSeven had temporary policy MFE then high MAE; Ggumbi showed clean 4B event-cap behavior after January policy spike","R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH|R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,block_positive_stage_when_policy_theme_has_high_or_persistent_MAE_without_budget_sales_margin_bridge,0,"High or persistent MAE after bridge-missing C31 entries should block Stage2/Stage3 promotion unless budget-to-sales, channel, traffic and margin evidence survives","ZeroToSeven MAE90=-32.29 and Ggumbi MAE90=-40.79","R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH|R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R12L95_C31_PARADISE_2024_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_POSITIVE", "symbol": "034230", "company_name": "파라다이스", "round": "R12", "loop": "95", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP", "case_type": "moderate_structural_success_with_later_tourism_policy_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R12L95_C31_PARADISE_2024_STAGE2_ACTIONABLE_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Tourism/casino policy and inbound-channel recovery bridge produced moderate 30D/90D MFE with controlled early MAE. C31 works when a policy or tourism reopening narrative maps into actual visitor/channel throughput, VIP/drop or mass-traffic mix, regulatory visibility, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C31_positive_requires_policy_to_channel_traffic_margin_revision_bridge_not_tourism_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean despite KOSDAQ→KOSPI market transfer in June 2024; OHLC continuity is usable. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R12L95_C31_ZEROSEVEN_2024_LOW_BIRTH_POLICY_FALSE_STAGE2", "symbol": "159580", "company_name": "제로투세븐", "round": "R12", "loop": "95", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP", "case_type": "failed_rerating_low_birth_policy_subsidy_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Low-birth policy / childcare subsidy watch spiked early but failed to prove subsidy-to-sales conversion, reorder durability or margin/revision bridge. C31 Stage2 should not be awarded when policy headlines do not convert into revenue mechanics.", "current_profile_verdict": "current_profile_false_positive_if_low_birth_policy_watch_counts_without_subsidy_to_sales_channel_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2018 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R12L95_C31_GGUMBI_2024_INFANT_CARE_POLICY_EVENT_CAP_4B", "symbol": "407400", "company_name": "꿈비", "round": "R12", "loop": "95", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Infant-care / low-birth policy event premium capped around the January spike and then suffered deep MAE. C31 should route bridge-missing childcare-policy event premiums to 4B unless budget, subsidy mechanics, channel sales, reorder, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_infant_care_policy_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2023 corporate-action candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R12L95_C31_PARADISE_2024_STAGE2_ACTIONABLE_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE", "case_id": "R12L95_C31_PARADISE_2024_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_POSITIVE", "symbol": "034230", "company_name": "파라다이스", "round": "R12", "loop": "95", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP", "sector": "casino_tourism_policy_inbound_channel_recovery", "primary_archetype": "policy_to_channel_traffic_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-07", "entry_date": "2024-03-07", "entry_price": 13550.0, "evidence_available_at_that_date": "tourism/casino policy visibility, inbound-channel recovery, visitor/drop traffic mix, regulatory stability and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["tourism_policy_visibility_proxy", "inbound_channel_recovery_proxy", "visitor_drop_mix_proxy", "margin_revision_bridge_proxy", "regulatory_stability_proxy"], "stage3_evidence_fields": ["moderate_MFE30", "moderate_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_tourism_policy_valuation_watch", "market_transfer_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034230/2024.csv", "profile_path": "atlas/symbol_profiles/034/034230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.94, "MFE_90D_pct": 15.94, "MFE_180D_pct": 15.94, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.84, "MAE_90D_pct": -3.84, "MAE_180D_pct": -9.96, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-02", "peak_price": 15710.0, "drawdown_after_peak_pct": -22.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_tourism_policy_valuation_4B_watch_needed", "four_b_evidence_type": ["policy_to_channel_bridge", "inbound_traffic_recovery", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_casino_tourism_policy_channel_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate_market_transfer_continuity_2024-06-24", "same_entry_group_id": "R12L95_C31_034230_2024-03-07_13550", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH", "case_id": "R12L95_C31_ZEROSEVEN_2024_LOW_BIRTH_POLICY_FALSE_STAGE2", "symbol": "159580", "company_name": "제로투세븐", "round": "R12", "loop": "95", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP", "sector": "low_birth_policy_childcare_subsidy_watch", "primary_archetype": "low_birth_policy_watch_without_subsidy_to_sales_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 8020.0, "evidence_available_at_that_date": "low-birth policy / childcare subsidy watch without confirmed budget-to-sales conversion, channel sell-through or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["low_birth_policy_watch", "childcare_subsidy_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["temporary_MFE_then_high_MAE", "subsidy_to_sales_bridge_missing", "post_policy_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/159/159580/2024.csv", "profile_path": "atlas/symbol_profiles/159/159580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.11, "MFE_90D_pct": 7.11, "MFE_180D_pct": 7.11, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.2, "MAE_90D_pct": -32.29, "MAE_180D_pct": -40.27, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-18", "peak_price": 8590.0, "drawdown_after_peak_pct": -36.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "low_birth_policy_watch_was_false_stage2_due_missing_subsidy_to_sales_channel_margin_bridge", "four_b_evidence_type": ["low_birth_policy_premium", "bridge_missing", "temporary_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_low_birth_policy_watch_without_subsidy_sales_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_low_birth_policy_watch_counts_without_subsidy_to_sales_channel_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2018_CA", "same_entry_group_id": "R12L95_C31_159580_2024-01-03_8020", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP", "case_id": "R12L95_C31_GGUMBI_2024_INFANT_CARE_POLICY_EVENT_CAP_4B", "symbol": "407400", "company_name": "꿈비", "round": "R12", "loop": "95", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP", "sector": "infant_care_low_birth_policy_event_premium", "primary_archetype": "infant_care_policy_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 13410.0, "evidence_available_at_that_date": "infant-care / low-birth policy event premium after January policy spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["infant_care_policy_event", "low_birth_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "budget_channel_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/407/407400/2024.csv", "profile_path": "atlas/symbol_profiles/407/407400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.62, "MFE_90D_pct": 9.62, "MFE_180D_pct": 9.62, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.37, "MAE_90D_pct": -40.79, "MAE_180D_pct": -40.79, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-03", "peak_price": 14700.0, "drawdown_after_peak_pct": -45.99, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "good_full_window_4B_timing_infant_care_low_birth_policy_event_cap", "four_b_evidence_type": ["low_birth_policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_infant_care_low_birth_policy_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_infant_care_policy_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2023_CA", "same_entry_group_id": "R12L95_C31_407400_2024-01-03_13410", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L95_C31_PARADISE_2024_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_POSITIVE", "trigger_id": "R12L95_C31_PARADISE_2024_STAGE2_ACTIONABLE_CASINO_TOURISM_POLICY_CHANNEL_BRIDGE", "symbol": "034230", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 60, "customer_quality_score": 40, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 65, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 45, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 60, "customer_quality_score": 50, "policy_or_regulatory_score": 60, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "casino_tourism_policy_channel_positive", "MFE_90D_pct": 15.94, "MAE_90D_pct": -3.84, "score_return_alignment_label": "casino_tourism_policy_channel_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L95_C31_ZEROSEVEN_2024_LOW_BIRTH_POLICY_FALSE_STAGE2", "trigger_id": "R12L95_C31_ZEROSEVEN_2024_STAGE2_FALSE_POSITIVE_LOW_BIRTH_POLICY_WATCH", "symbol": "159580", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 70, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "low_birth_policy_false_stage2", "MFE_90D_pct": 7.11, "MAE_90D_pct": -32.29, "score_return_alignment_label": "low_birth_policy_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_low_birth_policy_watch_counts_without_subsidy_to_sales_channel_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L95_C31_GGUMBI_2024_INFANT_CARE_POLICY_EVENT_CAP_4B", "trigger_id": "R12L95_C31_GGUMBI_2024_STAGE4B_INFANT_CARE_POLICY_EVENT_CAP", "symbol": "407400", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "infant_care_policy_event_cap_4B_guard", "MFE_90D_pct": 9.62, "MAE_90D_pct": -40.79, "score_return_alignment_label": "infant_care_policy_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_infant_care_policy_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "95", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CASINO_TOURISM_POLICY_CHANNEL_BRIDGE_VS_LOW_BIRTH_POLICY_FALSE_STAGE2_AND_INFANT_CARE_POLICY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["casino_tourism_policy_channel_positive", "low_birth_policy_false_stage2", "infant_care_policy_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C31 rows need explicit policy-to-revenue mechanics, budget/subsidy allocation, channel throughput, visitor/customer conversion, sales/reorder durability, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C31 policy/subsidy event rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 95
next_round = R13
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
