# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_95_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R5 loop 95 is R6 / loop 95. R6 is the L6 financial/capital-return/digital-finance round, and this run fills C22 insurance rate-cycle/reserve behavior rather than repeating the immediately preceding R6 loop 94 C21 financial ROE/PBR file.

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
scheduled_round = R6
scheduled_loop = 95
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 95
```

C22 is an insurance quality bridge archetype. The rate/reserve label is just the policy paper; the premium becomes evidence only when CSM/reserve adequacy, earnings quality, policy persistency, capital-return mechanics, margin and revision are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE = 37 rows / 12 symbols / good-bad Stage2 10-11 / 4B-4C 2-0
top covered symbols include 000370(7), 003690(7), 082640(6), 000540(4), 000810(3), 005830(3)
previous R6 loop-91 C22 symbols avoided: 085620, 000540, 000400
previous R6 loop-93 C22 symbols avoided: 032830, 001450, 088350
previous R6 loop-94 C21 symbols avoided: 055550, 006800, 041190
previous R5 loop-95 C20 symbols avoided: 002790, 027050, 003350
```

Selected rows avoid hard duplicates and top repeated C22 symbols:

```text
138040 / Stage2-Actionable / 2024-01-24
244920 / Stage2-Actionable / 2024-05-17
211050 / Stage4B / 2024-05-08
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
| 138040 | atlas/symbol_profiles/138/138040.json | selected 2024 window clean after old 2011/2014/2023 CA candidates |
| 244920 | atlas/symbol_profiles/244/244920.json | no corporate-action candidate |
| 211050 | atlas/symbol_profiles/211/211050.json | post-2024-04-29 CA-candidate boundary clean window with caveat |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L95_C22_MERITZFINANCIAL_2024_INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_POSITIVE | 138040 | 2024-01-24 | yes | 180 | yes | yes | true |
| R6L95_C22_APLUSASSET_2024_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2 | 244920 | 2024-05-17 | yes | 180 | yes | yes | true |
| R6L95_C22_INCARFINANCIAL_2024_INSURANCE_BROKER_COMMISSION_EVENT_CAP_4B | 211050 | 2024-05-08 | yes | 180 | yes | caveated-clean | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE | Positive Stage2 requires rate/reserve earnings quality, CSM/reserve adequacy, capital-return execution, ROE/PBR and revision bridge. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2 | Agency commission/value-up watch without persistency and margin bridge can become false Stage2. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_BROKER_EVENT_CAP_4B | Insurance broker/commission event premium should route to 4B when policy persistency and commission-margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L95_C22_MERITZFINANCIAL_2024_INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_POSITIVE | 138040 | 메리츠금융지주 | positive | Insurance rate/reserve/capital-return bridge produced strong MFE with shallow early MAE. |
| R6L95_C22_APLUSASSET_2024_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2 | 244920 | 에이플러스에셋 | counterexample | Agency commission/value-up watch had low MFE without persistency/margin bridge. |
| R6L95_C22_INCARFINANCIAL_2024_INSURANCE_BROKER_COMMISSION_EVENT_CAP_4B | 211050 | 인카금융서비스 | counterexample / 4B | Broker commission event premium capped after the early-May spike and later suffered high MAE. |

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
| Meritz Financial insurance holdco rate/reserve capital-return bridge | historical public/report proxy | true | true | shadow-only positive |
| A Plus Asset insurance-agency commission false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Incar Financial insurance-broker commission event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 138040 | atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv | atlas/symbol_profiles/138/138040.json |
| 244920 | atlas/ohlcv_tradable_by_symbol_year/244/244920/2024.csv | atlas/symbol_profiles/244/244920.json |
| 211050 | atlas/ohlcv_tradable_by_symbol_year/211/211050/2024.csv | atlas/symbol_profiles/211/211050.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L95_C22_MERITZFINANCIAL_2024_STAGE2_ACTIONABLE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE | 138040 | Stage2-Actionable | 2024-01-24 | 61900 | positive | insurance holdco rate/reserve capital-return bridge worked |
| R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH | 244920 | Stage2-Actionable | 2024-05-17 | 4270 | counterexample | insurance-agency commission false Stage2 |
| R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP | 211050 | Stage4B | 2024-05-08 | 5700 | counterexample/4B | insurance-broker commission event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L95_C22_MERITZFINANCIAL_2024_STAGE2_ACTIONABLE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE | 61900 | 41.03 | -2.75 | 42.65 | -2.75 | 71.89 | -2.75 | 2024-10-18 | 106400 | -29.79 |
| R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH | 4270 | 5.39 | -6.67 | 6.09 | -17.21 | 6.09 | -17.21 | 2024-08-16 | 4530 | -21.96 |
| R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP | 5700 | 13.68 | -9.30 | 13.68 | -27.72 | 13.68 | -27.72 | 2024-05-08 | 6480 | -36.42 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C22 Stage2 needs rate/reserve/CSM quality, persistency, capital return, ROE/PBR and revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing insurance agency/broker event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE insurance-commission rows cannot promote without persistency/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether insurance value-up becomes reserve quality, persistency and capital-return execution.

| symbol | stage quality | explanation |
|---|---|---|
| 138040 | good_stage2_with_later_watch | Rate/reserve and capital-return bridge produced strong MFE with shallow MAE. |
| 244920 | bad_stage2 | Agency commission watch lacked persistency/margin bridge and produced low MFE. |
| 211050 | good_4B | Broker commission event premium capped around the early-May spike and later suffered high MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 244920 insurance-agency false Stage2 | 0.94 | 0.94 | false Stage2 due missing persistency/commission-margin/capital-return bridge |
| 211050 insurance-broker cap | 0.88 | 0.88 | acceptable full-window 4B timing after early-May broker-commission event spike |
| 138040 insurance holdco bridge | n/a | n/a | positive Stage2, but later insurance value-up valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 244920 / 211050
```

No hard 4C candidate is proposed. R6 loop 95 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 insurance rate/reserve-cycle cases, Stage2 requires verified rate/reserve earnings quality, CSM or reserve adequacy, policy persistency, capital-return execution, ROE/PBR discount narrowing, margin, or revision bridge. Insurance, agency, broker, commission, value-up, rate or reserve label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
rule = C22 should split true rate/reserve/capital-return positives from insurance-agency commission false Stage2 and broker-commission event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 20.81 | -15.89 | 0.67 | mixed; C22 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 20.81 | -15.89 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L6 reserve/persistency/capital-return bridge required | 2 | 24.37 | -9.98 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C22 bridge vs event-cap split | 2 | 24.37 | -9.98 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing insurance commission themes as positive | 1 | 42.65 | -2.75 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 138040 insurance holdco bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 42.65 | -2.75 | insurance_holdco_rate_reserve_capital_return_positive |
| 244920 insurance-agency false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 6.09 | -17.21 | insurance_agency_commission_false_stage2 |
| 211050 broker commission cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 13.68 | -27.72 | insurance_broker_commission_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C22 Meritz Financial insurance-holdco rate/reserve capital-return positive, A Plus Asset insurance-agency commission false Stage2, and Incar Financial insurance-broker commission event-cap 4B split while avoiding top repeated C22 symbols and previous R6 loop93~94 symbols."}
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
residual_error_types_found: insurance_holdco_rate_reserve_capital_return_positive, insurance_agency_commission_false_stage2, insurance_broker_commission_event_cap_4B
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
- C22 insurance rate-cycle/reserve bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,C22_requires_rate_reserve_CSM_capital_return_persistency_margin_revision_bridge,0,"C22 Stage2 should require rate/reserve-cycle earnings quality, CSM or reserve adequacy, policy persistency, capital-return execution, ROE/PBR discount narrowing, margin, or revision bridge, not insurance/value-up/commission label alone","Meritz Financial positive worked; A Plus Asset and Incar Financial event/watch rows failed positive-stage promotion","R6L95_C22_MERITZFINANCIAL_2024_STAGE2_ACTIONABLE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE|R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH|R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,cap_bridge_missing_insurance_agency_and_broker_commission_event_premiums_as_4B_watch,0,"Insurance agency/broker commission premiums can peak before policy persistency, commission quality and margin bridge is proven","A Plus Asset had low MFE after commission watch; Incar Financial showed 4B event-cap behavior after the May insurance-broker spike","R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH|R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,block_positive_stage_when_insurance_commission_theme_has_high_or_persistent_MAE_without_persistency_margin_bridge,0,"High or persistent MAE after bridge-missing insurance-commission entries should block Stage2/Stage3 promotion unless persistency, capital-return and margin evidence survives","A Plus Asset MAE180=-17.21 and Incar Financial MAE90=-27.72","R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH|R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L95_C22_MERITZFINANCIAL_2024_INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_POSITIVE", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "95", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP", "case_type": "structural_success_with_later_insurance_valueup_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L95_C22_MERITZFINANCIAL_2024_STAGE2_ACTIONABLE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Insurance holding-company rate/reserve cycle, earnings quality and capital-return execution bridge produced strong 30D/90D/180D MFE with shallow early MAE. C22 works when insurance-rate/reserve narrative maps into CSM/earnings durability, reserve adequacy, shareholder-return mechanics, buyback/cancellation probability, ROE/PBR discount narrowing and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C22_positive_requires_insurance_rate_reserve_capital_return_ROE_revision_bridge_not_insurance_valueup_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2011/2014/2023 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L95_C22_APLUSASSET_2024_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2", "symbol": "244920", "company_name": "에이플러스에셋", "round": "R6", "loop": "95", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP", "case_type": "failed_rerating_insurance_agency_commission_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Insurance agency/commission value-up watch had only low forward MFE and then meaningful drawdown. C22 Stage2 should not be awarded without confirmed commission growth quality, persistency, insurer product mix, capital-return mechanics, operating leverage, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_insurance_agency_commission_watch_counts_without_persistency_margin_capital_return_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R6L95_C22_INCARFINANCIAL_2024_INSURANCE_BROKER_COMMISSION_EVENT_CAP_4B", "symbol": "211050", "company_name": "인카금융서비스", "round": "R6", "loop": "95", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Insurance broker/commission event premium after the post-corporate-action April reset and May spike capped quickly and later suffered high 90D/180D MAE. C22 should route bridge-missing insurance-broker commission event premiums to 4B unless policy persistency, new-contract quality, commission margin, capital-return optionality and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_broker_commission_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Profile flags old CA candidates including 2024-04-29; selected entry after the 2024-04-29 boundary, so the post-boundary 180D window is used with caveat. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L95_C22_MERITZFINANCIAL_2024_STAGE2_ACTIONABLE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_id": "R6L95_C22_MERITZFINANCIAL_2024_INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_POSITIVE", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "95", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP", "sector": "insurance_holdco_rate_reserve_capital_return_ROE_PBR", "primary_archetype": "insurance_rate_reserve_capital_return_ROE_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 61900.0, "evidence_available_at_that_date": "insurance rate/reserve-cycle earnings durability, CSM/reserve adequacy, capital-return execution, buyback/cancellation optionality and ROE/PBR revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["insurance_rate_cycle_proxy", "reserve_CSM_quality_proxy", "capital_return_policy_proxy", "buyback_cancellation_optionality_proxy", "ROE_PBR_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "strong_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_insurance_valueup_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv", "profile_path": "atlas/symbol_profiles/138/138040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 41.03, "MFE_90D_pct": 42.65, "MFE_180D_pct": 71.89, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.75, "MAE_90D_pct": -2.75, "MAE_180D_pct": -2.75, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-18", "peak_price": 106400.0, "drawdown_after_peak_pct": -29.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_insurance_valueup_valuation_4B_watch_needed", "four_b_evidence_type": ["insurance_rate_reserve_bridge", "capital_return_execution", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_insurance_holdco_rate_reserve_capital_return_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_2014_2023_CA", "same_entry_group_id": "R6L95_C22_138040_2024-01-24_61900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH", "case_id": "R6L95_C22_APLUSASSET_2024_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2", "symbol": "244920", "company_name": "에이플러스에셋", "round": "R6", "loop": "95", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP", "sector": "insurance_agency_commission_valueup_watch", "primary_archetype": "insurance_agency_commission_watch_without_persistency_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 4270.0, "evidence_available_at_that_date": "insurance agency commission growth/value-up watch without confirmed policy persistency, insurer product mix, margin or capital-return bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["insurance_agency_commission_watch", "financial_valueup_sympathy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "persistency_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/244/244920/2024.csv", "profile_path": "atlas/symbol_profiles/244/244920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.39, "MFE_90D_pct": 6.09, "MFE_180D_pct": 6.09, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.67, "MAE_90D_pct": -17.21, "MAE_180D_pct": -17.21, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-16", "peak_price": 4530.0, "drawdown_after_peak_pct": -21.96, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "insurance_agency_commission_watch_was_false_stage2_due_missing_persistency_margin_capital_return_bridge", "four_b_evidence_type": ["insurance_agency_commission_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_insurance_agency_commission_watch_without_persistency_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_insurance_agency_commission_watch_counts_without_persistency_margin_capital_return_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R6L95_C22_244920_2024-05-17_4270", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP", "case_id": "R6L95_C22_INCARFINANCIAL_2024_INSURANCE_BROKER_COMMISSION_EVENT_CAP_4B", "symbol": "211050", "company_name": "인카금융서비스", "round": "R6", "loop": "95", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP", "sector": "insurance_broker_commission_event_premium", "primary_archetype": "insurance_broker_commission_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-08", "entry_date": "2024-05-08", "entry_price": 5700.0, "evidence_available_at_that_date": "insurance broker/commission event premium after post-2024-04-29 reset and early-May spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["insurance_broker_commission_event", "financial_valueup_smallcap_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "policy_persistency_commission_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/211/211050/2024.csv", "profile_path": "atlas/symbol_profiles/211/211050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.68, "MFE_90D_pct": 13.68, "MFE_180D_pct": 13.68, "MFE_1Y_pct": "not_calculated_due_post_CA_boundary_window", "MFE_2Y_pct": "not_calculated_due_post_CA_boundary_window", "MAE_30D_pct": -9.3, "MAE_90D_pct": -27.72, "MAE_180D_pct": -27.72, "MAE_1Y_pct": "not_calculated_due_post_CA_boundary_window", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-08", "peak_price": 6480.0, "drawdown_after_peak_pct": -36.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "acceptable_full_window_4B_timing_insurance_broker_commission_event_cap_after_post_CA_reset", "four_b_evidence_type": ["insurance_broker_commission_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_insurance_broker_commission_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_broker_commission_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-04-29_CA_candidate_boundary_clean_window_with_caveat", "same_entry_group_id": "R6L95_C22_211050_2024-05-08_5700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L95_C22_MERITZFINANCIAL_2024_INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_POSITIVE", "trigger_id": "R6L95_C22_MERITZFINANCIAL_2024_STAGE2_ACTIONABLE_INSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE", "symbol": "138040", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 45, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 55, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "insurance_holdco_rate_reserve_capital_return_positive", "MFE_90D_pct": 42.65, "MAE_90D_pct": -2.75, "score_return_alignment_label": "insurance_holdco_rate_reserve_capital_return_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L95_C22_APLUSASSET_2024_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2", "trigger_id": "R6L95_C22_APLUSASSET_2024_STAGE2_FALSE_POSITIVE_INSURANCE_AGENCY_COMMISSION_WATCH", "symbol": "244920", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "insurance_agency_commission_false_stage2", "MFE_90D_pct": 6.09, "MAE_90D_pct": -17.21, "score_return_alignment_label": "insurance_agency_commission_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_insurance_agency_commission_watch_counts_without_persistency_margin_capital_return_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L95_C22_INCARFINANCIAL_2024_INSURANCE_BROKER_COMMISSION_EVENT_CAP_4B", "trigger_id": "R6L95_C22_INCARFINANCIAL_2024_STAGE4B_INSURANCE_BROKER_COMMISSION_EVENT_CAP", "symbol": "211050", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 20, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 40, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "insurance_broker_commission_event_cap_4B_guard", "MFE_90D_pct": 13.68, "MAE_90D_pct": -27.72, "score_return_alignment_label": "insurance_broker_commission_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_broker_commission_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "95", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_HOLDCO_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_AGENCY_COMMISSION_FALSE_STAGE2_AND_INSURANCE_BROKER_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["insurance_holdco_rate_reserve_capital_return_positive", "insurance_agency_commission_false_stage2", "insurance_broker_commission_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C22 rows need explicit rate/reserve earnings quality, CSM/reserve adequacy, policy persistency, capital-return execution, ROE/PBR discount, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C22 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 95
next_round = R7
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
