# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R11_loop_88_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

This loop continues loop 88 after R10. It adds 3 C31 policy/event cases: one utility tariff/receivable policy-to-cashflow positive and two education/digital-policy theme cap counterexamples.

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
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 88
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_sector_consistency = pass
computed_next_round = R12
computed_next_loop = 88
```

R11 permits L10 policy/event research. This loop avoids the prior R11 loop-87 IRA / wind / hydrogen / solar symbols and shifts the test to policy conversion quality: tariff/receivable/cashflow repair versus education policy theme.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT = 97 rows / 70 symbols / good-bad Stage2 35-25 / 4B-4C 5-0
top covered symbols include 013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
previous loop-87 symbols avoided: 112610, 336260, 009830
```

Selected rows:

```text
036460 / Stage2-Actionable / 2024-01-29
053290 / Stage2-Actionable / 2024-01-30
057030 / Stage4B / 2024-02-29
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
| 036460 | atlas/symbol_profiles/036/036460.json | no corporate-action candidate |
| 053290 | atlas/symbol_profiles/053/053290.json | selected 2024 window clean; CA candidates are 2007/2009 |
| 057030 | atlas/symbol_profiles/057/057030.json | selected 2024 window clean; CA candidates are 2005/2010 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R11L88_C31_KOGAS_2024_TARIFF_RECEIVABLE_POLICY_REPAIR_POSITIVE | 036460 | 2024-01-29 | yes | 180 | yes | yes | true |
| R11L88_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2 | 053290 | 2024-01-30 | yes | 180 | yes | yes | true |
| R11L88_C31_YBMNET_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B | 057030 | 2024-02-29 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR | Positive Stage2 requires policy-to-tariff, receivable, cashflow, or earnings repair. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | EDUCATION_POLICY_THEME_FALSE_STAGE2 | Education-policy headlines without revenue/contract conversion can be false Stage2. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | DIGITAL_EDU_POLICY_EVENT_CAP | Digital education theme spikes route to 4B unless contract/revenue bridge is verified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R11L88_C31_KOGAS_2024_TARIFF_RECEIVABLE_POLICY_REPAIR_POSITIVE | 036460 | 한국가스공사 | positive | Utility policy converted into tariff/receivable/cashflow repair optionality and strong MFE. |
| R11L88_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2 | 053290 | NE능률 | counterexample | Education policy theme spike failed to create durable revenue conversion. |
| R11L88_C31_YBMNET_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B | 057030 | YBM넷 | counterexample / 4B | Digital education policy premium capped early and then drifted lower. |

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
| KOGAS tariff/receivable repair | historical public/report proxy | true | true | shadow-only positive |
| NE Neungyule education theme | historical public/news proxy | true | true | false-Stage2 guardrail |
| YBM Net digital education cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 036460 | atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv | atlas/symbol_profiles/036/036460.json |
| 053290 | atlas/ohlcv_tradable_by_symbol_year/053/053290/2024.csv | atlas/symbol_profiles/053/053290.json |
| 057030 | atlas/ohlcv_tradable_by_symbol_year/057/057030/2024.csv | atlas/symbol_profiles/057/057030.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R11L88_C31_KOGAS_2024_STAGE2_ACTIONABLE_TARIFF_RECEIVABLE_REPAIR | 036460 | Stage2-Actionable | 2024-01-29 | 26300 | positive | policy-to-cashflow bridge worked |
| R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME | 053290 | Stage2-Actionable | 2024-01-30 | 5510 | counterexample | education policy theme false Stage2 |
| R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP | 057030 | Stage4B | 2024-02-29 | 4905 | counterexample/4B | digital education policy theme cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L88_C31_KOGAS_2024_STAGE2_ACTIONABLE_TARIFF_RECEIVABLE_REPAIR | 26300 | 20.91 | -11.03 | 102.66 | -11.03 | 145.25 | -11.03 | 2024-06-20 | 64500 | -43.41 |
| R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME | 5510 | 15.25 | -7.44 | 15.25 | -27.77 | 15.25 | -50.18 | 2024-01-30 | 6350 | -56.77 |
| R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP | 4905 | 13.76 | -18.45 | 13.76 | -26.50 | 13.76 | -39.65 | 2024-02-29 | 5580 | -46.95 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C31 Stage2 needs policy-to-cashflow, tariff, contract, order, subsidy, or revenue conversion |
| local_4b_watch_guard | strengthen: education/digital-policy theme premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 036460 | good_stage2 | Policy could plausibly map into tariff/receivable/cashflow repair. |
| 053290 | bad_stage2 | Policy theme did not become revenue or contract conversion. |
| 057030 | good_4B | Digital education theme premium capped and then drew down. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 053290 education theme | 1.00 | 1.00 | policy_theme_spike_was_event_cap_false_stage2 |
| 057030 digital education cap | 1.00 | 1.00 | good_full_window_4B_timing_digital_education_policy_event_cap |
| 036460 tariff/receivable bridge | n/a | n/a | positive Stage2; later policy/resource valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 053290 / 057030
```

No hard 4C candidate is proposed. R11 loop 88 is about policy conversion bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 policy/subsidy/legislation cases, Stage2 requires policy-to-cashflow conversion: tariff repair, receivable normalization, signed contract/order, confirmed subsidy, revenue bridge, or margin/revision bridge. Policy headline/theme alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rule = C31 should split real policy-to-cashflow positives from education/digital-policy theme caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 43.89 | -21.77 | 0.67 | mixed; C31 conversion split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 43.89 | -21.77 | 0.67 | weaker bridge/theme guard |
| P1 sector_specific_candidate_profile | L10 policy conversion bridge required | 2 | 58.96 | -19.40 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C31 policy bridge vs event-cap split | 2 | 58.96 | -19.40 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject policy-theme caps as positive | 1 | 102.66 | -11.03 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 036460 tariff/receivable | 66 | Stage2-Watch | 74 | Stage2-Actionable | 102.66 | -11.03 | policy_to_tariff_receivable_cashflow_positive |
| 053290 education false Stage2 | 66 | Stage2-Actionable | 53 | Stage1/Watch | 15.25 | -27.77 | education_policy_theme_false_stage2 |
| 057030 digital education cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 13.76 | -26.50 | digital_education_policy_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C31 utility tariff/receivable policy repair positive and education/digital-policy theme-cap guardrails using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: utility_policy_tariff_receivable_repair_positive, education_policy_theme_false_stage2, digital_education_policy_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
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
- C31 policy-to-cashflow bridge vs education/digital-policy theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,C31_requires_policy_to_cashflow_contract_or_tariff_bridge,0,"C31 Stage2 should require policy-to-cashflow/tariff/contract/subsidy conversion, not policy headline or theme label alone","KOGAS positive worked; NE Neungyule and YBM Net policy-theme rows failed positive-stage promotion","R11L88_C31_KOGAS_2024_STAGE2_ACTIONABLE_TARIFF_RECEIVABLE_REPAIR|R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME|R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,cap_policy_theme_premiums_as_4B_watch,0,"Education/digital-policy theme premiums can peak before verified revenue, contract, or subsidy conversion appears","NE Neungyule and YBM Net showed event-cap behavior and high MAE after policy-theme spikes","R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME|R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L88_C31_KOGAS_2024_TARIFF_RECEIVABLE_POLICY_REPAIR_POSITIVE", "symbol": "036460", "company_name": "한국가스공사", "round": "R11", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L88_C31_KOGAS_2024_STAGE2_ACTIONABLE_TARIFF_RECEIVABLE_REPAIR", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Utility policy/tariff receivable repair and energy-resource policy optionality produced high 90D/180D MFE; C31 works only when policy can map into tariff, receivable, or cashflow repair.", "current_profile_verdict": "current_profile_kept_but_C31_positive_requires_policy_to_cashflow_or_tariff_bridge_not_policy_headline_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of tariff/receivable policy evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R11L88_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2", "symbol": "053290", "company_name": "NE능률", "round": "R11", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Education-policy theme spike failed to become durable revenue/contract/subsidy conversion; later MAE dominated the short-lived MFE.", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge", "price_source": "Songdaiki/stock-web", "notes": "Education policy/theme false Stage2 row; source-proxy only."}
{"row_type": "case", "case_id": "R11L88_C31_YBMNET_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B", "symbol": "057030", "company_name": "YBM넷", "round": "R11", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Digital-education policy premium capped quickly and then drifted lower; policy theme without contract/revenue conversion should route to 4B watch.", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Education/digital-learning policy event-cap row; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R11L88_C31_KOGAS_2024_STAGE2_ACTIONABLE_TARIFF_RECEIVABLE_REPAIR", "case_id": "R11L88_C31_KOGAS_2024_TARIFF_RECEIVABLE_POLICY_REPAIR_POSITIVE", "symbol": "036460", "company_name": "한국가스공사", "round": "R11", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP", "sector": "utility_energy_policy_tariff", "primary_archetype": "tariff_receivable_policy_cashflow_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-29", "entry_date": "2024-01-29", "entry_price": 26300.0, "evidence_available_at_that_date": "utility tariff / receivable repair and energy-policy optionality proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["tariff_receivable_repair_proxy", "policy_cashflow_bridge", "energy_resource_policy_optionality", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE90", "high_MFE180", "policy_to_cashflow_repair_path"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_policy_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036460/2024.csv", "profile_path": "atlas/symbol_profiles/036/036460.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.91, "MFE_90D_pct": 102.66, "MFE_180D_pct": 145.25, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.03, "MAE_90D_pct": -11.03, "MAE_180D_pct": -11.03, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-20", "peak_price": 64500.0, "drawdown_after_peak_pct": -43.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_policy_resource_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "policy_event_premium", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_tariff_receivable_policy_repair_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L88_C31_036460_2024-01-29_26300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "case_id": "R11L88_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2", "symbol": "053290", "company_name": "NE능률", "round": "R11", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP", "sector": "education_policy_theme", "primary_archetype": "education_policy_theme_without_revenue_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-30", "entry_date": "2024-01-30", "entry_price": 5510.0, "evidence_available_at_that_date": "education policy / digital textbook / policy theme proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["education_policy_theme", "digital_textbook_or_curriculum_policy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_spike", "weak_conversion_bridge", "post_peak_drawdown"], "stage4c_evidence_fields": ["theme_fade_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053290/2024.csv", "profile_path": "atlas/symbol_profiles/053/053290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.25, "MFE_90D_pct": 15.25, "MFE_180D_pct": 15.25, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.44, "MAE_90D_pct": -27.77, "MAE_180D_pct": -50.18, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-30", "peak_price": 6350.0, "drawdown_after_peak_pct": -56.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "policy_theme_spike_was_event_cap_false_stage2", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_education_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L88_C31_053290_2024-01-30_5510", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "case_id": "R11L88_C31_YBMNET_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B", "symbol": "057030", "company_name": "YBM넷", "round": "R11", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP", "sector": "digital_education_policy_theme", "primary_archetype": "digital_education_policy_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-29", "entry_date": "2024-02-29", "entry_price": 4905.0, "evidence_available_at_that_date": "digital education / policy theme premium proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["digital_education_policy_theme", "relative_strength_spike", "policy_event_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/057/057030/2024.csv", "profile_path": "atlas/symbol_profiles/057/057030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.76, "MFE_90D_pct": 13.76, "MFE_180D_pct": 13.76, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.45, "MAE_90D_pct": -26.5, "MAE_180D_pct": -39.65, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-29", "peak_price": 5580.0, "drawdown_after_peak_pct": -46.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_digital_education_policy_event_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L88_C31_057030_2024-02-29_4905", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L88_C31_KOGAS_2024_TARIFF_RECEIVABLE_POLICY_REPAIR_POSITIVE", "trigger_id": "R11L88_C31_KOGAS_2024_STAGE2_ACTIONABLE_TARIFF_RECEIVABLE_REPAIR", "symbol": "036460", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 75, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 45, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "policy_to_tariff_receivable_cashflow_positive", "MFE_90D_pct": 102.66, "MAE_90D_pct": -11.03, "score_return_alignment_label": "policy_to_tariff_receivable_cashflow_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L88_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2", "trigger_id": "R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "symbol": "053290", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 75, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 45, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["policy_or_regulatory_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "education_policy_theme_false_stage2", "MFE_90D_pct": 15.25, "MAE_90D_pct": -27.77, "score_return_alignment_label": "education_policy_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L88_C31_YBMNET_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B", "trigger_id": "R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "symbol": "057030", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 75, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 45, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["policy_or_regulatory_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "digital_education_policy_event_cap_4B_guard", "MFE_90D_pct": 13.76, "MAE_90D_pct": -26.5, "score_return_alignment_label": "digital_education_policy_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "UTILITY_TARIFF_RECEIVABLE_POLICY_REPAIR_VS_EDUCATION_POLICY_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["utility_policy_tariff_receivable_repair_positive", "education_policy_theme_false_stage2", "digital_education_policy_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 88
next_round = R12
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
