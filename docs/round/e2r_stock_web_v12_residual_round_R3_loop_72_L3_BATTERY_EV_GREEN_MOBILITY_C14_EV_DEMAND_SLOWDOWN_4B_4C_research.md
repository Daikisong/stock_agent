# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R3
scheduled_loop = 72
completed_round = R3
completed_loop = 72
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT
output_file = e2r_stock_web_v12_residual_round_R3_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The tested residual is not whether price-only blowoff should be blocked. That global rule is kept. The new question is narrower: inside C14, a generic EV-demand slowdown headline should not be equivalent to company-specific customer call-off, utilization collapse, ASP compression, or margin bridge failure.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R3 |
| scheduled_loop | 72 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C |
| fine_archetype_id | EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT |
| loop_objective | 4C_thesis_break_timing_test; counterexample_mining; sector_specific_rule_discovery; coverage_gap_fill |
| round_sector_consistency | pass |

## 3. Previous Coverage / Duplicate Avoidance Check

No stock_agent source code was opened. This run treats the previous loop state as R2/Loop72 completed and therefore resolves to R3/Loop72. The selected cases avoid the immediately preceding C08 semiconductor/test-socket work and stay inside R3. All four representative cases use a new C14 trigger-family split: generic EV-demand slowdown versus company-specific call-off/utilization/ASP evidence.

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_atlas_repo | https://github.com/Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |

## 5. Historical Eligibility Gate

All four representative trigger rows are historical events with entry dates inside stock-web tradable shards. Each has at least 180 forward trading days available before the manifest max date. The selected 2024 windows do not overlap each symbol's corporate-action candidate dates.

| symbol | company | profile status | corporate action window | calibration_usable |
|---|---:|---|---|---|
| 247540 | 에코프로비엠 | active_like, 2019-03-05~2026-02-20 | 2022 candidates only, outside 2024 window | true |
| 066970 | 엘앤에프 | active_like, KOSDAQ→KOSPI transition in 2024 | 2016/2021 candidates only, outside 2024 window | true |
| 373220 | LG에너지솔루션 | active_like, no corporate-action candidates | clean | true |
| 006400 | 삼성SDI | active_like, old 2014 candidate only | outside 2024 window | true |

## 6. Canonical Archetype Compression Map

| canonical | fine split | scoring implication |
|---|---|---|
| C14_EV_DEMAND_SLOWDOWN_4B_4C | customer_calloff_or_order_cut | hard 4C candidate if tied to company-specific order/customer evidence |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | ASP_margin_utilization_break | 4B/4C upgrade if price damage is supported by margin/ASP bridge |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | generic_EV_headline_only | Stage2-watch or 4B-watch only, not hard 4C |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | AMPC_or_customer_quality_exception | prevents automatic demotion for large cell makers |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | entry | entry_price | headline thesis |
|---|---:|---|---|---|---:|---:|---|
| R3L72_C14_247540_20240430_4C_SUCCESS | 247540 | 에코프로비엠 | 4C_success | positive | 2024-04-30 | 238,500 | ASP/utilization/cathode demand break |
| R3L72_C14_066970_20240430_4C_SUCCESS | 066970 | 엘앤에프 | 4C_success | positive | 2024-04-30 | 163,900 | customer/volume uncertainty and cathode margin compression |
| R3L72_C14_373220_20240430_4B_TOO_EARLY | 373220 | LG에너지솔루션 | 4B_too_early | counterexample | 2024-04-30 | 389,000 | generic EV slowdown not enough for hard 4C |
| R3L72_C14_006400_20240131_4B_TOO_EARLY | 006400 | 삼성SDI | high_mae_success | counterexample | 2024-01-31 | 372,500 | generic demand slowdown preceded a major rebound |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
```

The positive side says that C14 can protect capital when EV-demand slowdown is anchored in company-specific customer/order/ASP/utilization evidence. The counterexample side says that broad demand headlines alone can be too blunt: large cell makers with AMPC, customer quality, or mixed exposure may rebound before the real down-leg appears.

## 9. Evidence Source Map

| evidence family | allowed use in this MD | not allowed use |
|---|---|---|
| generic EV-demand slowdown headline | 4B-watch / risk overlay | hard 4C by itself |
| customer call-off / order cut | hard 4C candidate | positive promotion |
| ASP / margin / utilization break | 4B/4C upgrade | Green confirmation without financial bridge |
| AMPC / IRA / customer quality bridge | exception/guard against early hard 4C | price-only promotion |

## 10. Price Data Source Map

| symbol | tradable shard | profile path | entry row source |
|---:|---|---|---|
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | atlas/symbol_profiles/247/247540.json | 2024-04-30 c=238500 |
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | atlas/symbol_profiles/066/066970.json | 2024-04-30 c=163900 |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json | 2024-04-30 c=389000 |
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | atlas/symbol_profiles/006/006400.json | 2024-01-31 c=372500 |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | stage2 fields | stage3 fields | 4B fields | 4C fields | current verdict |
|---:|---|---|---|---|---|---|
| 247540 | Stage4C-Watch/Stage2-Demotion | public_event, early_revision | financial_visibility | margin/backlog slowdown | call_off, thesis_broken | current_profile_correct |
| 066970 | Stage4C-Watch/Stage2-Demotion | public_event, early_revision | financial_visibility | margin/backlog slowdown | call_off, thesis_broken | current_profile_correct |
| 373220 | Stage4B-Watch | public_event | unsupported | positioning/watch | thesis_break_watch_only | current_profile_4B_too_early |
| 006400 | Stage4B-Watch | public_event | unsupported | positioning/watch | thesis_break_watch_only | current_profile_4C_too_early |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 247540 | 2024-04-30 | 238,500 | 3.14% | -23.90% | 3.14% | -37.65% | 3.14% | -55.97% | 2024-04-30 | 246,000 | -57.32% |
| 066970 | 2024-04-30 | 163,900 | 7.99% | -10.62% | 7.99% | -49.42% | 7.99% | -50.58% | 2024-06-13 | 177,000 | -54.24% |
| 373220 | 2024-04-30 | 389,000 | 2.06% | -16.20% | 7.71% | -19.54% | 14.14% | -19.54% | 2024-10-08 | 444,000 | -22.18% |
| 006400 | 2024-01-31 | 372,500 | 9.66% | -3.22% | 32.75% | -13.02% | 32.75% | -36.78% | 2024-03-25 | 494,500 | -52.38% |

## 13. Current Calibrated Profile Stress Test

| tested axis | verdict |
|---|---|
| stage2_actionable_evidence_bonus | kept, but C14 requires non-price customer/order/margin bridge before promotion |
| stage3_yellow_total_min | kept |
| stage3_green_total_min / revision_min | kept |
| price_only_blowoff_blocks_positive_stage | strengthened |
| full_4b_requires_non_price_evidence | strengthened |
| hard_4c_thesis_break_routes_to_4c | strengthened with C14-specific evidence gate |

## 14. Stage2 / Yellow / Green Comparison

For the two positive C14 risk cases, Stage3-Green was not the key comparison. The useful distinction is Stage2-watch versus 4C-watch. A generic EV-demand slowdown belongs in Stage2-watch/4B-watch. Once customer call-off, utilization damage, or ASP/margin break is visible, the same headline should become a hard 4C or positive-stage block.

```text
green_lateness_ratio = not_applicable
reason = C14 risk timing test, not positive Green confirmation test
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | local proximity | full-window proximity | verdict |
|---:|---:|---:|---|
| 247540 | 0.90 | 0.85 | good_full_window_4B_timing |
| 066970 | 0.88 | 0.83 | good_full_window_4B_timing |
| 373220 | 0.35 | 0.25 | price_only_local_4B_too_early |
| 006400 | 0.40 | 0.18 | price_only_local_4B_too_early |

## 16. 4C Protection Audit

| symbol | protection label | interpretation |
|---:|---|---|
| 247540 | hard_4c_success | hard 4C/watch blocked a large 180D drawdown |
| 066970 | hard_4c_success | customer/ASP bridge was useful before the drawdown |
| 373220 | false_break | broad EV slowdown alone was too blunt |
| 006400 | false_break | early hard 4C would have missed a +32.75% rebound |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = C14_EV_demand_slowdown_requires_customer_calloff_ASP_or_utilization_bridge_for_hard_4C
baseline_value = generic_demand_slowdown_can_overweight_negative_stage
tested_value = generic_headline_watch_only; company_specific_bridge_hard_4C
delta = +1 guard strength, not production
confidence = low_to_medium
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
canonical_rule_candidate = true
rule = Do not route generic EV demand slowdown headlines directly to hard 4C unless at least one of customer call-off, order cut, utilization break, ASP/margin bridge failure, or explicit thesis evidence break is present.
counter_rule = If a cell maker has AMPC/IRA/customer-quality offset and no direct customer/order cut, route to 4B-watch rather than hard 4C.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | score_return_alignment |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 12.90% | -29.91% | 0.50 | 0 | mixed |
| P0b e2r_2_0_baseline_reference | 4 | 12.90% | -29.91% | 0.75 | 1 | weaker guard |
| P1 sector_specific_candidate_profile | 4 | 5.57% selected-risk-positive / 20.23% watch-only counterexamples | -43.54% selected-risk-positive / -16.28% watch-only counterexamples | 0.25 | 0 | improved |
| P2 canonical_archetype_candidate_profile | 4 | same as P1 | same as P1 | 0.25 | 0 | improved |
| P3 counterexample_guard_profile | 4 | avoids hard-4C on 373220/006400 | preserves 247540/066970 protection | 0.00 for generic-headline hard-4C | 0 | best explanation |

## 20. Score-Return Alignment Matrix

| symbol | current_profile_verdict | score-return alignment | residual |
|---:|---|---|---|
| 247540 | current_profile_correct | aligned | none |
| 066970 | current_profile_correct | aligned | none |
| 373220 | current_profile_4B_too_early | mixed | generic headline over-penalty |
| 006400 | current_profile_4C_too_early | mixed | early hard 4C missed rebound |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT | 2 | 2 | 4 | 2 | 4 | 0 | 4 | 4 | 2 | true | true | needs more 2022-2023 cycle holdout and overseas EV OEM call-off cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - generic_EV_slowdown_hard_4C_too_early
  - cell_maker_AMPC_customer_bridge_exception
new_axis_proposed: C14_EV_demand_slowdown_requires_customer_calloff_ASP_or_utilization_bridge_for_hard_4C
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c_with_C14_evidence_gate
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Actual stock-web tradable OHLC rows for all representative entry dates.
- 30D/90D/180D MFE and MAE based on raw unadjusted tradable rows.
- Corporate-action candidate windows do not overlap the 2024 entry windows used for calibration.

Not validated:
- No live watchlist.
- No current candidate recommendation.
- No stock_agent source-code inspection.
- No production scoring change.
- Evidence text is historical research proxy language and should be re-linked to formal disclosures/news during implementation ingestion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_hard_4C_requires_company_specific_calloff_ASP_or_utilization_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"generic EV slowdown alone over-routes some cell makers to hard 4C","keeps 247540/066970 protection while reducing 373220/006400 false-breaks","TRG_247540_20240430_4C_SUCCESS|TRG_066970_20240430_4C_SUCCESS|TRG_373220_20240430_4B_TOO_EARLY|TRG_006400_20240131_4B_TOO_EARLY",4,4,2,low_to_medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C14_generic_EV_headline_demote_to_4B_watch_not_hard_4C,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"cell-maker rebounds show hard 4C too early without call-off","improves false positive guard","TRG_373220_20240430_4B_TOO_EARLY|TRG_006400_20240131_4B_TOO_EARLY",2,2,2,low,sector_shadow_only,"watch-only guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L72_C14_247540_20240430_4C_SUCCESS", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "Stage4C-Watch/Stage2-Demotion", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Q1 materials/cathode ASP and EV demand slowdown; downstream call-off/utilization risk visible enough to demote positive rerating unless customer bridge repaired."}
{"row_type": "case", "case_id": "R3L72_C14_066970_20240430_4C_SUCCESS", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "Stage4C-Watch/Stage2-Demotion", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Customer/volume uncertainty plus cathode margin compression; 2024 KOSPI transfer did not repair the operating bridge, so generic rerating should be blocked."}
{"row_type": "case", "case_id": "R3L72_C14_373220_20240430_4B_TOO_EARLY", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT", "case_type": "4B_too_early", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B-Watch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_guardrail_needed", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "Generic EV demand slowdown headline without direct customer call-off; cell-maker AMPC/IRA and large-customer bridge meant hard 4C should not be automatic."}
{"row_type": "case", "case_id": "R3L72_C14_006400_20240131_4B_TOO_EARLY", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B-Watch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_guardrail_needed", "current_profile_verdict": "current_profile_4C_too_early", "price_source": "Songdaiki/stock-web", "notes": "Early-2024 EV slowdown and de-stocking narrative was real, but without direct call-off evidence the name still produced a large tradable rebound before the later drawdown."}
{"row_type": "trigger", "trigger_id": "TRG_247540_20240430_4C_SUCCESS", "case_id": "R3L72_C14_247540_20240430_4C_SUCCESS", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / call-off / utilization risk", "loop_objective": "4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage4C-Watch/Stage2-Demotion", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 238500, "evidence_available_at_that_date": "Q1 materials/cathode ASP and EV demand slowdown; downstream call-off/utilization risk visible enough to demote positive rerating unless customer bridge repaired.", "evidence_source": "historical public disclosure/news proxy; no live candidate discovery; stock-web OHLC verified", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "contract_delay"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.14, "MFE_90D_pct": 3.14, "MFE_180D_pct": 3.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.9, "MAE_90D_pct": -37.65, "MAE_180D_pct": -55.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-30", "peak_price": 246000, "drawdown_after_peak_pct": -57.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.85, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["margin_or_backlog_slowdown", "revision_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L72_C14_247540_20240430_4C_SUCCESS_EG", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_066970_20240430_4C_SUCCESS", "case_id": "R3L72_C14_066970_20240430_4C_SUCCESS", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / call-off / utilization risk", "loop_objective": "4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage4C-Watch/Stage2-Demotion", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 163900, "evidence_available_at_that_date": "Customer/volume uncertainty plus cathode margin compression; 2024 KOSPI transfer did not repair the operating bridge, so generic rerating should be blocked.", "evidence_source": "historical public disclosure/news proxy; no live candidate discovery; stock-web OHLC verified", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "contract_delay"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.99, "MFE_90D_pct": 7.99, "MFE_180D_pct": 7.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.62, "MAE_90D_pct": -49.42, "MAE_180D_pct": -50.58, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 177000, "drawdown_after_peak_pct": -54.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.85, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["margin_or_backlog_slowdown", "revision_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L72_C14_066970_20240430_4C_SUCCESS_EG", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_373220_20240430_4B_TOO_EARLY", "case_id": "R3L72_C14_373220_20240430_4B_TOO_EARLY", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / call-off / utilization risk", "loop_objective": "4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 389000, "evidence_available_at_that_date": "Generic EV demand slowdown headline without direct customer call-off; cell-maker AMPC/IRA and large-customer bridge meant hard 4C should not be automatic.", "evidence_source": "historical public disclosure/news proxy; no live candidate discovery; stock-web OHLC verified", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.06, "MFE_90D_pct": 7.71, "MFE_180D_pct": 14.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.2, "MAE_90D_pct": -19.54, "MAE_180D_pct": -19.54, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-08", "peak_price": 444000, "drawdown_after_peak_pct": -22.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_break", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L72_C14_373220_20240430_4B_TOO_EARLY_EG", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_006400_20240131_4B_TOO_EARLY", "case_id": "R3L72_C14_006400_20240131_4B_TOO_EARLY", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_CUSTOMER_CALLOFF_ASP_UTILIZATION_SPLIT", "sector": "battery_ev_green_mobility", "primary_archetype": "EV demand slowdown / call-off / utilization risk", "loop_objective": "4C_thesis_break_timing_test|counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-01-31", "entry_date": "2024-01-31", "entry_price": 372500, "evidence_available_at_that_date": "Early-2024 EV slowdown and de-stocking narrative was real, but without direct call-off evidence the name still produced a large tradable rebound before the later drawdown.", "evidence_source": "historical public disclosure/news proxy; no live candidate discovery; stock-web OHLC verified", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["unknown_or_not_supported"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.66, "MFE_90D_pct": 32.75, "MFE_180D_pct": 32.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.22, "MAE_90D_pct": -13.02, "MAE_180D_pct": -36.78, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 494500, "drawdown_after_peak_pct": -52.38, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "price_rebound_before_late_4C", "current_profile_verdict": "current_profile_4C_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L72_C14_006400_20240131_4B_TOO_EARLY_EG", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L72_C14_247540_20240430_4C_SUCCESS", "trigger_id": "TRG_247540_20240430_4C_SUCCESS", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 0, "asp_or_spread_score": 65, "thesis_break_score": 55}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow-or-4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 0, "asp_or_spread_score": 75, "thesis_break_score": 70}, "weighted_score_after": 78, "stage_label_after": "Stage4C-Watch/positive-blocked", "changed_components": ["execution_risk_score", "asp_or_spread_score", "thesis_break_score"], "component_delta_explanation": "Company-specific ASP/utilization/call-off bridge upgrades slowdown from generic watch to hard negative overlay.", "MFE_90D_pct": 3.14, "MAE_90D_pct": -37.65, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L72_C14_066970_20240430_4C_SUCCESS", "trigger_id": "TRG_066970_20240430_4C_SUCCESS", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 0, "asp_or_spread_score": 65, "thesis_break_score": 55}, "weighted_score_before": 72, "stage_label_before": "Stage3-Yellow-or-4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 0, "asp_or_spread_score": 75, "thesis_break_score": 70}, "weighted_score_after": 78, "stage_label_after": "Stage4C-Watch/positive-blocked", "changed_components": ["execution_risk_score", "asp_or_spread_score", "thesis_break_score"], "component_delta_explanation": "Company-specific ASP/utilization/call-off bridge upgrades slowdown from generic watch to hard negative overlay.", "MFE_90D_pct": 7.99, "MAE_90D_pct": -49.42, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L72_C14_373220_20240430_4B_TOO_EARLY", "trigger_id": "TRG_373220_20240430_4B_TOO_EARLY", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 35, "valuation_repricing_score": 0, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 0, "asp_or_spread_score": 0, "thesis_break_score": 35}, "weighted_score_before": 70, "stage_label_before": "Stage4C-risk-too-early", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 45, "valuation_repricing_score": 0, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 0, "asp_or_spread_score": 0, "thesis_break_score": 25}, "weighted_score_after": 63, "stage_label_after": "Stage2-watch/4B-watch-only", "changed_components": ["execution_risk_score", "asp_or_spread_score", "thesis_break_score"], "component_delta_explanation": "Generic EV slowdown without direct call-off is demoted; hard 4C waits for customer/order/utilization break.", "MFE_90D_pct": 7.71, "MAE_90D_pct": -19.54, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L72_C14_006400_20240131_4B_TOO_EARLY", "trigger_id": "TRG_006400_20240131_4B_TOO_EARLY", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 35, "valuation_repricing_score": 0, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 0, "asp_or_spread_score": 0, "thesis_break_score": 35}, "weighted_score_before": 70, "stage_label_before": "Stage4C-risk-too-early", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 45, "valuation_repricing_score": 0, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 0, "asp_or_spread_score": 0, "thesis_break_score": 25}, "weighted_score_after": 63, "stage_label_after": "Stage2-watch/4B-watch-only", "changed_components": ["execution_risk_score", "asp_or_spread_score", "thesis_break_score"], "component_delta_explanation": "Generic EV slowdown without direct call-off is demoted; hard 4C waits for customer/order/utilization break.", "MFE_90D_pct": 32.75, "MAE_90D_pct": -13.02, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "residual_contribution", "round": "R3", "loop": "72", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["generic_EV_slowdown_hard_4C_too_early", "cell_maker_AMPC_customer_bridge_exception"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R3
completed_loop = 72
next_round = R4
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Price source: Songdaiki/stock-web, manifest max date 2026-02-20.
- All OHLC values are raw/unadjusted tradable rows.
- 247540 profile: corporate action candidate dates 2022-06-27 and 2022-07-15 only, outside this loop's 2024 windows.
- 066970 profile: corporate action candidate dates 2016-02-19 and 2021-08-11 only, outside this loop's 2024 windows.
- 373220 profile: no corporate action candidates.
- 006400 profile: old candidate dates only, outside this loop's 2024 windows.

