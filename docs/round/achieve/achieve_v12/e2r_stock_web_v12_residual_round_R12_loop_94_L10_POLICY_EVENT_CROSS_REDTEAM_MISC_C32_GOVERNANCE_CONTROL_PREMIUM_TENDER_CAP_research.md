# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R12_loop_94_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

This file is the corrected final output for this execution. The scheduler state after R11 loop 94 is R12 / loop 94. R12 is the L10 policy/event/misc round, and this run fills C32 governance/control-premium/tender-cap behavior while avoiding the top repeated C32 symbols and the prior R12 loop 88~93 symbols.

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
scheduled_round = R12
scheduled_loop = 94
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
round_sector_consistency = pass
computed_next_round = R13
computed_next_loop = 94
```

C32 is an execution bridge archetype. A governance or control-premium headline is the invitation; the actual transaction is NAV visibility, portfolio asset value, capital-return execution, tender/buyback mechanics, ownership probability, buyer/regulatory path and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP = 41 rows / 22 symbols / good-bad Stage2 16-12 / 4B-4C 3-0
top covered symbols include 010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2)
previous R12 loop-88 C32 symbols avoided: 000400, 040300, 006040
previous R12 loop-89 C31 symbols avoided: 071320, 100220, 339950
previous R12 loop-90 C32 symbols avoided: 003240, 008930, 064850
previous R12 loop-91 C31 symbols avoided: 272210, 032820, 457550
previous R12 loop-92 C32 symbols avoided: 028260, 004990, 001040
previous R12 loop-93 C32 symbols avoided: 402340, 180640, 034120
previous R11 loop-94 C31 symbols avoided: 034020, 126880, 119850
```

Selected rows avoid hard duplicates and top repeated C32 symbols:

```text
267250 / Stage2-Actionable / 2024-04-23
034730 / Stage2-Actionable / 2024-02-01
000240 / Stage4B / 2024-02-02
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
| 267250 | atlas/symbol_profiles/267/267250.json | selected 2024 window clean after old 2017/2021 CA candidates |
| 034730 | atlas/symbol_profiles/034/034730.json | selected 2024 window clean after old 2015 CA candidate |
| 000240 | atlas/symbol_profiles/000/000240.json | selected 2024 window clean after old 1997~2013 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R12L94_C32_HDHYUNDAI_2024_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_POSITIVE | 267250 | 2024-04-23 | yes | 180 | yes | yes | true |
| R12L94_C32_SK_2024_HOLDCO_VALUEUP_FALSE_STAGE2 | 034730 | 2024-02-01 | yes | 180 | yes | yes | true |
| R12L94_C32_HANKOOKANDCOMPANY_2024_CONTROL_PREMIUM_EVENT_CAP_4B | 000240 | 2024-02-02 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | HOLDCO_NAV_CAPITAL_RETURN_BRIDGE | Positive Stage2 requires NAV visibility, capital-return execution, portfolio value, governance execution and revision bridge. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | HOLDCO_VALUEUP_FALSE_STAGE2 | Holdco value-up watch without portfolio monetization and capital-return bridge can become false Stage2. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_EVENT_CAP_4B | Tender/control-premium aftermath premium should route to 4B when execution bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R12L94_C32_HDHYUNDAI_2024_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_POSITIVE | 267250 | HD현대 | positive | Holding-company NAV/capital-return bridge produced positive MFE after the April reset with shallow MAE. |
| R12L94_C32_SK_2024_HOLDCO_VALUEUP_FALSE_STAGE2 | 034730 | SK | counterexample | Holdco value-up premium was temporary and later de-rated without execution bridge. |
| R12L94_C32_HANKOOKANDCOMPANY_2024_CONTROL_PREMIUM_EVENT_CAP_4B | 000240 | 한국앤컴퍼니 | counterexample / 4B | Tender/control-premium aftermath premium capped after the February spike and then de-rated. |

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
| HD Hyundai holdco NAV/capital-return bridge | historical public/report proxy | true | true | shadow-only positive |
| SK holdco value-up false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Hankook & Company control-premium event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 267250 | atlas/ohlcv_tradable_by_symbol_year/267/267250/2024.csv | atlas/symbol_profiles/267/267250.json |
| 034730 | atlas/ohlcv_tradable_by_symbol_year/034/034730/2024.csv | atlas/symbol_profiles/034/034730.json |
| 000240 | atlas/ohlcv_tradable_by_symbol_year/000/000240/2024.csv | atlas/symbol_profiles/000/000240.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R12L94_C32_HDHYUNDAI_2024_STAGE2_ACTIONABLE_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE | 267250 | Stage2-Actionable | 2024-04-23 | 64700 | positive | NAV/capital-return bridge worked |
| R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH | 034730 | Stage2-Actionable | 2024-02-01 | 197000 | counterexample | holdco value-up false Stage2 |
| R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP | 000240 | Stage4B | 2024-02-02 | 18720 | counterexample/4B | control-premium/tender aftermath event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R12L94_C32_HDHYUNDAI_2024_STAGE2_ACTIONABLE_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE | 64700 | 7.26 | -2.16 | 27.51 | -2.16 | 27.51 | -2.16 | 2024-07-17 | 82500 | -3.15 |
| R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH | 197000 | 7.61 | -5.48 | 7.61 | -15.63 | 7.61 | -23.50 | 2024-02-23 | 212000 | -26.56 |
| R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP | 18720 | 3.95 | -15.49 | 3.95 | -18.16 | 3.95 | -24.04 | 2024-02-08 | 19460 | -20.09 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C32 Stage2 needs NAV / capital-return / tender / ownership-control / asset-value execution bridge |
| local_4b_watch_guard | strengthen: bridge-missing control-premium/tender/holdco value-up event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high or persistent MAE governance/control-premium rows cannot promote without durable execution bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether governance/control-premium narrative becomes measurable execution.

| symbol | stage quality | explanation |
|---|---|---|
| 267250 | good_stage2_with_later_watch | NAV and capital-return bridge produced positive MFE with shallow MAE. |
| 034730 | bad_stage2 | Value-up premium lacked portfolio monetization/capital-return execution bridge and later de-rated. |
| 000240 | good_4B | Tender/control-premium aftermath premium capped after the February spike and then bled down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 034730 holdco value-up false Stage2 | 0.93 | 0.93 | false Stage2 due missing NAV/capital-return execution bridge |
| 000240 control-premium tender cap | 0.96 | 0.96 | acceptable full-window 4B timing after February control-premium spike |
| 267250 NAV/capital-return bridge | n/a | n/a | positive Stage2, but later holdco NAV valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 034730 / 000240
```

No hard 4C candidate is proposed. R12 loop 94 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 governance/control-premium/tender-cap cases, Stage2 requires verified NAV visibility, capital-return execution, tender/buyback mechanics, ownership-control event probability, buyer/regulatory path, asset-value realization, portfolio monetization, or revision bridge. Governance, value-up, holding-company, control-premium, tender or sale label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rule = C32 should split true NAV/capital-return/tender execution positives from holdco value-up false Stage2 and control-premium event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 13.02 | -11.98 | 0.67 | mixed; C32 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 13.02 | -11.98 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L10 governance execution bridge required | 2 | 17.56 | -8.90 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C32 bridge vs event-cap split | 2 | 17.56 | -8.90 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing governance/control-premium themes as positive | 1 | 27.51 | -2.16 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 267250 NAV/capital-return bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 27.51 | -2.16 | holdco_NAV_capital_return_positive |
| 034730 holdco value-up false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 7.61 | -15.63 | holdco_valueup_false_stage2 |
| 000240 control-premium cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 3.95 | -18.16 | control_premium_tender_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C32 HD Hyundai holdco NAV/capital-return positive, SK holdco value-up false Stage2, and Hankook & Company control-premium/tender aftermath event-cap 4B split while avoiding top repeated C32 symbols and previous R12/R11 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: holdco_NAV_capital_return_positive, holdco_valueup_false_stage2, control_premium_tender_event_cap_4B
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
- C32 governance/control-premium/tender-cap bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,C32_requires_NAV_capital_return_tender_control_premium_execution_revision_bridge,0,"C32 Stage2 should require NAV visibility, capital-return execution, tender/buyback mechanics, ownership-event probability, asset-value realization, portfolio monetization, or revision bridge, not governance/value-up/control-premium label alone","HD Hyundai positive worked; SK and Hankook & Company event/watch rows failed positive-stage promotion","R12L94_C32_HDHYUNDAI_2024_STAGE2_ACTIONABLE_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE|R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH|R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,cap_bridge_missing_holdco_valueup_and_control_premium_event_rows_as_4B_watch,0,"Holdco value-up/control-premium/tender aftermath premiums can peak before execution, ownership probability and capital-return bridge is proven","SK had temporary MFE then de-rated; Hankook & Company showed control-premium event-cap behavior after February spike","R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH|R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,block_positive_stage_when_governance_control_premium_theme_has_high_or_persistent_MAE_without_execution_bridge,0,"High or persistent MAE after bridge-missing governance/control-premium entries should block Stage2/Stage3 promotion unless tender, capital-return, ownership and execution evidence survives","SK MAE180=-23.50 and Hankook & Company MAE180=-24.04","R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH|R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R12L94_C32_HDHYUNDAI_2024_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_POSITIVE", "symbol": "267250", "company_name": "HD현대", "round": "R12", "loop": "94", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP", "case_type": "structural_success_with_later_holdco_NAV_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R12L94_C32_HDHYUNDAI_2024_STAGE2_ACTIONABLE_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Holding-company NAV discount / capital-return / portfolio asset-value bridge produced positive 90D/180D MFE after the April reset with controlled forward MAE. C32 works when governance/value-up narrative maps into NAV visibility, capital-allocation mechanics, buyback/dividend optionality, portfolio value realization and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C32_positive_requires_NAV_capital_return_portfolio_value_execution_revision_bridge_not_holdco_valueup_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017/2021 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R12L94_C32_SK_2024_HOLDCO_VALUEUP_FALSE_STAGE2", "symbol": "034730", "company_name": "SK", "round": "R12", "loop": "94", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP", "case_type": "failed_rerating_holdco_valueup_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Holding-company value-up / NAV discount watch had a temporary February premium but later lost the bridge. C32 Stage2 should not be awarded without explicit capital-return execution, portfolio monetization, tender/buyback mechanics, governance event probability, asset-value realization and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_holdco_valueup_watch_counts_without_NAV_capital_return_execution_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2015 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R12L94_C32_HANKOOKANDCOMPANY_2024_CONTROL_PREMIUM_EVENT_CAP_4B", "symbol": "000240", "company_name": "한국앤컴퍼니", "round": "R12", "loop": "94", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Control-premium / tender aftermath event premium capped around the February spike and then de-rated. C32 should route bridge-missing control-premium/tender aftermath rows to 4B unless tender mechanics, ownership probability, buyer path, regulatory visibility, asset value realization and capital-return bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_tender_aftermath_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997~2013 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R12L94_C32_HDHYUNDAI_2024_STAGE2_ACTIONABLE_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE", "case_id": "R12L94_C32_HDHYUNDAI_2024_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_POSITIVE", "symbol": "267250", "company_name": "HD현대", "round": "R12", "loop": "94", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP", "sector": "holdco_NAV_capital_return_portfolio_asset_value", "primary_archetype": "NAV_discount_capital_return_portfolio_value_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-23", "entry_date": "2024-04-23", "entry_price": 64700.0, "evidence_available_at_that_date": "holding-company NAV discount narrowing, portfolio asset value visibility, capital-allocation discipline, dividend/buyback optionality and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["NAV_visibility_proxy", "portfolio_asset_value_proxy", "capital_return_optionality_proxy", "governance_execution_bridge", "revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "positive_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_holdco_NAV_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267250/2024.csv", "profile_path": "atlas/symbol_profiles/267/267250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.26, "MFE_90D_pct": 27.51, "MFE_180D_pct": 27.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.16, "MAE_90D_pct": -2.16, "MAE_180D_pct": -2.16, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 82500.0, "drawdown_after_peak_pct": -3.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_holdco_NAV_valuation_4B_watch_needed", "four_b_evidence_type": ["NAV_discount_repricing", "capital_return_execution", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_holdco_NAV_capital_return_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_2021_CA", "same_entry_group_id": "R12L94_C32_267250_2024-04-23_64700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH", "case_id": "R12L94_C32_SK_2024_HOLDCO_VALUEUP_FALSE_STAGE2", "symbol": "034730", "company_name": "SK", "round": "R12", "loop": "94", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP", "sector": "holdco_valueup_NAV_discount_watch", "primary_archetype": "holdco_valueup_watch_without_capital_return_portfolio_monetization_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 197000.0, "evidence_available_at_that_date": "holding-company value-up/NAV discount watch and governance rerating expectation without confirmed portfolio monetization, buyback/cancellation or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["holdco_valueup_watch", "NAV_discount_sympathy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["temporary_MFE_then_MAE", "capital_return_execution_bridge_missing", "portfolio_value_realization_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034730/2024.csv", "profile_path": "atlas/symbol_profiles/034/034730.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.61, "MFE_90D_pct": 7.61, "MFE_180D_pct": 7.61, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.48, "MAE_90D_pct": -15.63, "MAE_180D_pct": -23.5, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 212000.0, "drawdown_after_peak_pct": -26.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "holdco_valueup_watch_was_false_stage2_due_missing_NAV_capital_return_execution_bridge", "four_b_evidence_type": ["holdco_valueup_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_holdco_valueup_watch_without_NAV_capital_return_bridge", "current_profile_verdict": "current_profile_false_positive_if_holdco_valueup_watch_counts_without_NAV_capital_return_execution_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2015_CA", "same_entry_group_id": "R12L94_C32_034730_2024-02-01_197000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP", "case_id": "R12L94_C32_HANKOOKANDCOMPANY_2024_CONTROL_PREMIUM_EVENT_CAP_4B", "symbol": "000240", "company_name": "한국앤컴퍼니", "round": "R12", "loop": "94", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP", "sector": "control_premium_tender_aftermath_event_premium", "primary_archetype": "control_premium_tender_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 18720.0, "evidence_available_at_that_date": "control-premium / tender aftermath / governance event premium after late-January to early-February spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["control_premium_event", "tender_aftermath_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "MAE_recheck", "tender_ownership_execution_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000240/2024.csv", "profile_path": "atlas/symbol_profiles/000/000240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.95, "MFE_90D_pct": 3.95, "MFE_180D_pct": 3.95, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.49, "MAE_90D_pct": -18.16, "MAE_180D_pct": -24.04, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-08", "peak_price": 19460.0, "drawdown_after_peak_pct": -20.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "acceptable_full_window_4B_timing_control_premium_tender_aftermath_event_cap", "four_b_evidence_type": ["control_premium_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_control_premium_tender_aftermath_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_tender_aftermath_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2013_CA", "same_entry_group_id": "R12L94_C32_000240_2024-02-02_18720", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L94_C32_HDHYUNDAI_2024_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_POSITIVE", "trigger_id": "R12L94_C32_HDHYUNDAI_2024_STAGE2_ACTIONABLE_HOLDCO_NAV_CAPITAL_RETURN_BRIDGE", "symbol": "267250", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 45, "valuation_repricing_score": 65, "execution_risk_score": 50, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 55, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 55, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "holdco_NAV_capital_return_positive", "MFE_90D_pct": 27.51, "MAE_90D_pct": -2.16, "score_return_alignment_label": "holdco_NAV_capital_return_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L94_C32_SK_2024_HOLDCO_VALUEUP_FALSE_STAGE2", "trigger_id": "R12L94_C32_SK_2024_STAGE2_FALSE_POSITIVE_HOLDCO_VALUEUP_WATCH", "symbol": "034730", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 45, "valuation_repricing_score": 65, "execution_risk_score": 50, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "holdco_valueup_false_stage2", "MFE_90D_pct": 7.61, "MAE_90D_pct": -15.63, "score_return_alignment_label": "holdco_valueup_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_holdco_valueup_watch_counts_without_NAV_capital_return_execution_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L94_C32_HANKOOKANDCOMPANY_2024_CONTROL_PREMIUM_EVENT_CAP_4B", "trigger_id": "R12L94_C32_HANKOOKANDCOMPANY_2024_STAGE4B_CONTROL_PREMIUM_EVENT_CAP", "symbol": "000240", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 45, "valuation_repricing_score": 65, "execution_risk_score": 50, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "control_premium_tender_event_cap_4B_guard", "MFE_90D_pct": 3.95, "MAE_90D_pct": -18.16, "score_return_alignment_label": "control_premium_tender_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_tender_aftermath_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "94", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HOLDCO_NAV_CAPITAL_RETURN_BRIDGE_VS_HOLDCO_VALUEUP_FALSE_STAGE2_AND_CONTROL_PREMIUM_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["holdco_NAV_capital_return_positive", "holdco_valueup_false_stage2", "control_premium_tender_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C32 rows need explicit NAV, tender/buyback, capital-return, buyer/regulatory, ownership-control or asset-value realization bridge before positive promotion.
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
10. Add tests that bridge-missing C32 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 94
next_round = R13
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
