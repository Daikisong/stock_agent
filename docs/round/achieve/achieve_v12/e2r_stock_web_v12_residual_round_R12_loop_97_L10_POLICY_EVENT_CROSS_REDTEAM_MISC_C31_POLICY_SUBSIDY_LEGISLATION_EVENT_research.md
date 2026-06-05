# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | policy_legislation_bridge_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R12_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

This file is the corrected final output for this execution. The scheduler state after R11 loop 97 is R12 / loop 97. R12 is the L10 policy/event/cross-redteam/misc round. This run fills C31 policy/subsidy/legislation event behavior rather than repeating the immediately preceding R12 loop 96 C32 governance/control-premium file or R12 loop 95 C31 symbols.

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
policy_legislation_bridge_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 97
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_sector_consistency = pass
computed_next_round = R13
computed_next_loop = 97
```

C31 is a policy/subsidy/legislation bridge archetype. A policy headline is the public notice on the wall; the investable signal only starts to breathe when legislation, rulemaking, procurement, adoption, revenue conversion, margin and revision are connected.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT = 97 rows / 70 symbols / good-bad Stage2 35-25 / 4B-4C 5-0
top covered symbols include 013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
previous R12 loop-95 C31 symbols avoided: 034230, 159580, 407400
previous R12 loop-96 C32 symbols avoided: 001750, 040300, 008930
previous R11 loop-97 C03 symbols avoided: 077970, 361390, 024740
previous R10 loop-97 C30 symbols avoided: 097230, 016250, 046940
```

Selected rows avoid hard duplicates and top repeated C31 symbols:

```text
115500 / Stage2-Actionable / 2024-02-06
032850 / Stage2-Actionable / 2024-02-16
094480 / Stage4B / 2024-01-03
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
| 115500 | atlas/symbol_profiles/115/115500.json | no corporate-action candidate |
| 032850 | atlas/symbol_profiles/032/032850.json | selected 2024 window clean after old 1999/2000 CA candidates |
| 094480 | atlas/symbol_profiles/094/094480.json | selected 2024 window clean after old 2008/2009 CA and name-history candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R12L97_C31_KCS_2024_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE_POSITIVE | 115500 | 2024-02-06 | yes | 180 | yes | yes | true |
| R12L97_C31_BITCOMPUTER_2024_TELEMEDICINE_POLICY_FALSE_STAGE2 | 032850 | 2024-02-16 | yes | 180 | yes | yes | true |
| R12L97_C31_GALAXIAMONEYTREE_2024_STO_DIGITAL_ASSET_EVENT_CAP_4B | 094480 | 2024-01-03 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE | Positive Stage2 requires institutional pilot, procurement or service scope, rulemaking/standardization, contract channel, margin and revision bridge. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | TELEMEDICINE_POLICY_FALSE_STAGE2 | Telemedicine policy watch without implementation, reimbursement and adoption/revenue bridge can become false Stage2. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | STO_DIGITAL_ASSET_EVENT_CAP_4B | STO/digital-asset legislation premium should route to 4B when rulemaking, authorization and volume-fee bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R12L97_C31_KCS_2024_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE_POSITIVE | 115500 | 케이씨에스 | positive | CBDC/digital infrastructure policy bridge produced strong MFE with shallow initial MAE. |
| R12L97_C31_BITCOMPUTER_2024_TELEMEDICINE_POLICY_FALSE_STAGE2 | 032850 | 비트컴퓨터 | counterexample | Telemedicine policy event watch had high MAE without reimbursement/adoption/revenue bridge. |
| R12L97_C31_GALAXIAMONEYTREE_2024_STO_DIGITAL_ASSET_EVENT_CAP_4B | 094480 | 갤럭시아머니트리 | counterexample / 4B | STO/digital-asset legislation event premium capped in the January spike and then de-rated sharply. |

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
| KCS CBDC/digital infrastructure policy bridge | historical public/news-report proxy | true | true | shadow-only positive |
| Bit Computer telemedicine policy false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Galaxia Moneytree STO/digital-asset event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 115500 | atlas/ohlcv_tradable_by_symbol_year/115/115500/2024.csv | atlas/symbol_profiles/115/115500.json |
| 032850 | atlas/ohlcv_tradable_by_symbol_year/032/032850/2024.csv | atlas/symbol_profiles/032/032850.json |
| 094480 | atlas/ohlcv_tradable_by_symbol_year/094/094480/2024.csv | atlas/symbol_profiles/094/094480.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE | 115500 | Stage2-Actionable | 2024-02-06 | 7060 | positive | CBDC/digital-infra policy-legislation bridge worked |
| R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH | 032850 | Stage2-Actionable | 2024-02-16 | 8380 | counterexample | telemedicine policy false Stage2 |
| R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP | 094480 | Stage4B | 2024-01-03 | 12000 | counterexample/4B | STO/digital-asset legislation event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE | 7060 | 32.01 | -1.98 | 32.01 | -12.18 | 32.01 | -12.18 | 2024-02-15 | 9320 | -33.48 |
| R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH | 8380 | 10.86 | -25.54 | 10.86 | -30.43 | 18.97 | -34.61 | 2024-07-22 | 9970 | n/a |
| R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP | 12000 | 2.92 | -34.17 | 2.92 | -47.75 | 2.92 | -54.00 | 2024-01-03 | 12350 | -55.30 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C31 Stage2 needs implementation / rulemaking / procurement / adoption / revenue / margin / revision bridge |
| policy_legislation_bridge_guardrail | strengthen: policy and legislation labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing telemedicine and STO/digital-asset policy premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE policy rows cannot promote without durable implementation bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether policy/event narrative becomes legislation implementation and monetization evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 115500 | good_stage2_with_later_watch | Institutional CBDC/digital-infra policy bridge produced strong MFE but later valuation watch remains necessary. |
| 032850 | bad_stage2 | Telemedicine policy watch lacked implementation/reimbursement/revenue bridge and showed high MAE. |
| 094480 | good_4B | STO/digital-asset legislation premium peaked in the first spike and then de-rated sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 032850 telemedicine policy false Stage2 | 0.90 | 0.84 | false Stage2 due missing implementation / reimbursement / revenue bridge |
| 094480 STO/digital-asset cap | 0.97 | 0.97 | good full-window 4B timing after January STO/digital-asset legislation premium |
| 115500 CBDC policy bridge | n/a | n/a | positive Stage2, but later policy-event valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = policy_implementation_thesis_break_watch_only / legislation_thesis_break_watch_only
```

No hard 4C candidate is introduced in this R12 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 policy/subsidy/legislation event cases, Stage2 requires verified implementation, bill passage or rulemaking, procurement/service scope, institutional adoption, reimbursement or fee path, revenue conversion, margin, or revision bridge. Policy, subsidy, legislation, CBDC, STO, telemedicine, government-pilot or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rule = C31 should split true implementation/procurement/adoption/revenue positives from telemedicine false Stage2 and STO/digital-asset event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 15.26 | -30.12 | 0.67 | mixed; C31 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 15.26 | -30.12 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L10 implementation/procurement/revenue bridge required | 2 | 21.44 | -21.31 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C31 bridge vs event-cap split | 2 | 21.44 | -21.31 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing policy themes as positive | 1 | 32.01 | -12.18 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 115500 CBDC policy bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 32.01 | -12.18 | CBDC_policy_legislation_positive |
| 032850 telemedicine false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 10.86 | -30.43 | telemedicine_policy_false_stage2 |
| 094480 STO/digital-asset cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.92 | -47.75 | STO_legislation_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C31 KCS CBDC/digital infrastructure policy-legislation positive, Bit Computer telemedicine policy false Stage2, and Galaxia Moneytree STO/digital-asset legislation event-cap 4B while avoiding top repeated C31 and previous R12/R11 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, policy_legislation_bridge_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: CBDC_policy_legislation_positive, telemedicine_policy_false_stage2, STO_legislation_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, policy_legislation_bridge_guardrail, high_MAE_guardrail
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
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,C31_requires_legislation_implementation_procurement_adoption_revenue_margin_revision_bridge,0,"C31 Stage2 should require bill passage, rulemaking or implementation, procurement/service scope, institutional adoption, revenue conversion, margin, or revision bridge, not policy/subsidy/legislation label alone","KCS positive worked; Bit Computer and Galaxia Moneytree event/watch rows failed positive-stage promotion","R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE|R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH|R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,cap_bridge_missing_telemedicine_and_STO_policy_event_premiums_as_4B_watch,0,"Telemedicine and STO/digital-asset legislation premiums can peak before implementation, reimbursement, rulemaking, platform authorization and revenue bridge is proven","Bit Computer had high MAE after telemedicine policy watch; Galaxia Moneytree showed clean 4B event-cap behavior after January STO/digital-asset spike","R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH|R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,block_positive_stage_when_policy_theme_has_high_or_persistent_MAE_without_implementation_bridge,0,"High or persistent MAE after bridge-missing C31 entries should block Stage2/Stage3 promotion unless implementation, adoption, revenue and margin evidence survives","Bit Computer MAE90=-30.43 and Galaxia Moneytree MAE90=-47.75","R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH|R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R12L97_C31_KCS_2024_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE_POSITIVE", "symbol": "115500", "company_name": "케이씨에스", "round": "R12", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP", "case_type": "moderate_structural_success_with_later_policy_event_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "CBDC/digital-infrastructure policy and legislation bridge produced strong 30D/90D MFE with shallow initial MAE, then later mean reversion. C31 works when policy/event narrative maps into institution-backed pilot demand, procurement or service scope, standardization/legislation visibility, installed-base or contract channel, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C31_positive_requires_institutional_pilot_procurement_legislation_scope_margin_revision_bridge_not_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R12L97_C31_BITCOMPUTER_2024_TELEMEDICINE_POLICY_FALSE_STAGE2", "symbol": "032850", "company_name": "비트컴퓨터", "round": "R12", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP", "case_type": "failed_rerating_telemedicine_policy_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Telemedicine policy/strike-related event watch spiked but then suffered high MAE and required repeated policy repricing. C31 Stage2 should not be awarded without legal implementation, payer/reimbursement path, hospital or clinic adoption, revenue conversion, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_telemedicine_policy_watch_counts_without_implementation_reimbursement_adoption_revenue_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1999/2000 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R12L97_C31_GALAXIAMONEYTREE_2024_STO_DIGITAL_ASSET_EVENT_CAP_4B", "symbol": "094480", "company_name": "갤럭시아머니트리", "round": "R12", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "STO/digital-asset legislation event premium capped in the first January spike and then de-rated sharply. C31 should route bridge-missing legislation/policy event premiums to 4B unless bill passage, rulemaking, platform authorization, transaction volume, fee conversion, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_STO_digital_asset_legislation_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2008/2009 corporate-action and name-history candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE", "case_id": "R12L97_C31_KCS_2024_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE_POSITIVE", "symbol": "115500", "company_name": "케이씨에스", "round": "R12", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP", "sector": "CBDC_digital_infrastructure_policy_pilot_legislation", "primary_archetype": "institutional_pilot_procurement_legislation_scope_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | policy_legislation_bridge_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 7060.0, "evidence_available_at_that_date": "CBDC/digital infrastructure policy pilot, public-sector standardization, institution-backed procurement or service-scope and margin/revision bridge proxy after February base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_report_proxy", "stage2_evidence_fields": ["institutional_pilot_proxy", "procurement_scope_proxy", "legislation_standardization_proxy", "installed_base_contract_channel_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_policy_event_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/115/115500/2024.csv", "profile_path": "atlas/symbol_profiles/115/115500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.01, "MFE_90D_pct": 32.01, "MFE_180D_pct": 32.01, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.98, "MAE_90D_pct": -12.18, "MAE_180D_pct": -12.18, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 9320.0, "drawdown_after_peak_pct": -33.48, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_policy_event_valuation_4B_watch_needed", "four_b_evidence_type": ["CBDC_policy_pilot_bridge", "procurement_legislation_scope", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_CBDC_digital_infra_policy_legislation_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R12L97_C31_115500_2024-02-06_7060", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH", "case_id": "R12L97_C31_BITCOMPUTER_2024_TELEMEDICINE_POLICY_FALSE_STAGE2", "symbol": "032850", "company_name": "비트컴퓨터", "round": "R12", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP", "sector": "telemedicine_policy_reimbursement_adoption_watch", "primary_archetype": "telemedicine_policy_watch_without_implementation_reimbursement_adoption_revenue_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | policy_legislation_bridge_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-16", "entry_date": "2024-02-16", "entry_price": 8380.0, "evidence_available_at_that_date": "telemedicine policy / medical-strike event watch without confirmed legal implementation, payer/reimbursement pathway, hospital adoption, revenue conversion or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["telemedicine_policy_watch", "medical_strike_policy_event", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["high_MAE30", "persistent_MAE90", "implementation_reimbursement_revenue_bridge_missing"], "stage4c_evidence_fields": ["policy_implementation_thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032850/2024.csv", "profile_path": "atlas/symbol_profiles/032/032850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.86, "MFE_90D_pct": 10.86, "MFE_180D_pct": 18.97, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -25.54, "MAE_90D_pct": -30.43, "MAE_180D_pct": -34.61, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-22", "peak_price": 9970.0, "drawdown_after_peak_pct": "not_calculated_after_peak_window_truncated", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.84, "four_b_timing_verdict": "telemedicine_policy_watch_was_false_stage2_due_missing_implementation_reimbursement_revenue_bridge", "four_b_evidence_type": ["telemedicine_policy_premium", "bridge_missing", "high_MAE"], "four_c_protection_label": "policy_implementation_thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_telemedicine_policy_watch_without_reimbursement_revenue_bridge", "current_profile_verdict": "current_profile_false_positive_if_telemedicine_policy_watch_counts_without_implementation_reimbursement_adoption_revenue_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1999_2000_CA", "same_entry_group_id": "R12L97_C31_032850_2024-02-16_8380", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP", "case_id": "R12L97_C31_GALAXIAMONEYTREE_2024_STO_DIGITAL_ASSET_EVENT_CAP_4B", "symbol": "094480", "company_name": "갤럭시아머니트리", "round": "R12", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP", "sector": "STO_digital_asset_legislation_platform_event_premium", "primary_archetype": "STO_digital_asset_legislation_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | policy_legislation_bridge_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 12000.0, "evidence_available_at_that_date": "STO/digital-asset legislation event premium without confirmed bill passage, rulemaking, platform authorization, transaction-volume fee conversion or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["STO_legislation_event", "digital_asset_policy_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE30", "deep_MAE30", "bill_rulemaking_volume_bridge_missing"], "stage4c_evidence_fields": ["legislation_thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094480/2024.csv", "profile_path": "atlas/symbol_profiles/094/094480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.92, "MFE_90D_pct": 2.92, "MFE_180D_pct": 2.92, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -34.17, "MAE_90D_pct": -47.75, "MAE_180D_pct": -54.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-03", "peak_price": 12350.0, "drawdown_after_peak_pct": -55.3, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing_STO_digital_asset_legislation_event_cap", "four_b_evidence_type": ["STO_legislation_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "legislation_thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_STO_digital_asset_legislation_premium", "current_profile_verdict": "current_profile_4B_too_late_if_STO_digital_asset_legislation_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2008_2009_CA_and_name_history_candidates", "same_entry_group_id": "R12L97_C31_094480_2024-01-03_12000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L97_C31_KCS_2024_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE_POSITIVE", "trigger_id": "R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE", "symbol": "115500", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 60, "customer_quality_score": 35, "policy_or_regulatory_score": 65, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 50, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 70, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "CBDC_digital_infra_policy_legislation_positive", "MFE_90D_pct": 32.01, "MAE_90D_pct": -12.18, "score_return_alignment_label": "CBDC_policy_legislation_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L97_C31_BITCOMPUTER_2024_TELEMEDICINE_POLICY_FALSE_STAGE2", "trigger_id": "R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH", "symbol": "032850", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 70, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "telemedicine_policy_false_stage2", "MFE_90D_pct": 10.86, "MAE_90D_pct": -30.43, "score_return_alignment_label": "telemedicine_policy_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_telemedicine_policy_watch_counts_without_implementation_reimbursement_adoption_revenue_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L97_C31_GALAXIAMONEYTREE_2024_STO_DIGITAL_ASSET_EVENT_CAP_4B", "trigger_id": "R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP", "symbol": "094480", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 25, "policy_or_regulatory_score": 70, "valuation_repricing_score": 65, "execution_risk_score": 60, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 95, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "STO_digital_asset_legislation_event_cap_4B_guard", "MFE_90D_pct": 2.92, "MAE_90D_pct": -47.75, "score_return_alignment_label": "STO_legislation_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_STO_digital_asset_legislation_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "DIGITAL_ASSET_STO_CBDC_LEGISLATION_BRIDGE_VS_TELEMEDICINE_POLICY_FALSE_STAGE2_AND_DIGITAL_ASSET_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "policy_legislation_bridge_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["CBDC_policy_legislation_positive", "telemedicine_policy_false_stage2", "STO_legislation_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C31 rows need explicit implementation, bill passage or rulemaking, procurement/service scope, institutional adoption, reimbursement or fee path, revenue conversion, margin or revision bridge before positive promotion.
- In C31, bridge-missing policy/legislation event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C31 policy/subsidy/legislation event rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 97
next_round = R13
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
