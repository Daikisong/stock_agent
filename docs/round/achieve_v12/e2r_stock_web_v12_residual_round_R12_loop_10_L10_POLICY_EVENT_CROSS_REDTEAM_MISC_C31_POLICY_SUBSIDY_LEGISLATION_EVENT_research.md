# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R12
scheduled_loop: 10
completed_round: R12
completed_loop: 10
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: POLICY_EVENT_SUPPLY_SECURITY_ONLINE_EDUCATION_FOOD_SAFETY_THEME_GUARD
output_file: e2r_stock_web_v12_residual_round_R12_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds **4** new independent cases, **2** counterexamples, and **3** residual errors for `R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT`.

## 1. Current Calibrated Profile Assumption

`P0 = e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as existing infrastructure, not new discoveries:

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

The research question here is narrower: **when does a policy/event shock become a tradable Stage2 signal, and when is it only an event premium that must be capped before Stage3-Green?**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R12 |
| scheduled_loop | 10 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | POLICY_EVENT_SUPPLY_SECURITY_ONLINE_EDUCATION_FOOD_SAFETY_THEME_GUARD |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; canonical_archetype_compression |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R12 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` and under-covered service/agri/misc areas. This file therefore uses C31, not an R13 cross-archetype checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact reviewed: `reports/e2r_calibration/by_round/R12.md`.

R12 already has broad representative-trigger volume, so this loop avoids merely re-proving global Stage2/Green thresholds. It adds a **C31-specific split**:

1. policy/event shock with real demand or supply-security route,
2. policy/event shock with no cash-flow bridge,
3. political/person theme without legislation or procurement,
4. food-safety fear event without reorder/channel conversion.

No selected representative row reuses the same symbol + trigger_date + entry_date + evidence family from the immediately preceding R6~R11 loop files.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---|
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

Price basis: `tradable_raw`. Adjustment status: `raw_unadjusted_marcap`. MFE/MAE are rounded from stock-web tradable shard rows.

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| all trigger dates are historical | pass |
| entry rows exist in tradable shards | pass |
| forward 180 trading days available by manifest max_date | pass |
| positive OHLCV fields present | pass |
| 30D/90D/180D MFE/MAE computed | pass |
| corporate action contamination in selected 180D windows | none detected from symbol profiles |
| calibration_usable_case_count | 4 |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | included fine_archetypes | compression rule |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | GRAIN_FEED_SUPPLY_SECURITY_PRICE_SHOCK; COVID_REMOTE_EDUCATION_POLICY_DEMAND; FOOD_SAFETY_IMPORT_BAN_CONSUMER_SUBSTITUTION_THEME; POLITICAL_PERSON_THEME_NOT_POLICY_CONTRACT | compress all into C31, but split `official/cash-flow route` from `fear/person/theme-only` |

## 7. Case Selection Summary

| case_id | symbol | role | trigger_family | why selected | new? |
|---|---:|---|---|---|---|
| `R12L10C31_HANILFEED_GRAIN_SHOCK_2022` | `005860` | positive / missed_structural | food_security_grain_price_shock | C31 policy/event path with clean stock-web 180D window | true |
| `R12L10C31_YBMNET_REMOTE_EDU_2020` | `057030` | positive / structural_success | remote_education_policy_demand | C31 policy/event path with clean stock-web 180D window | true |
| `R12L10C31_CJSEAFOOD_FUKUSHIMA_2023` | `011150` | counterexample / failed_rerating | food_safety_event_import_substitution | C31 policy/event path with clean stock-web 180D window | true |
| `R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021` | `053290` | counterexample / price_moved_without_evidence | political_person_event_without_policy_cashflow | C31 policy/event path with clean stock-web 180D window | true |

## 8. Positive vs Counterexample Balance

| count field | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 4 |
| 4C/watch case_count | 2 |
| calibration_usable_case_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |

Positive cases are not used to re-prove the global Stage2 bonus. They test whether C31 needs an **event-to-cashflow bridge** before Green. Counterexamples test where event headlines should remain watch-only.

## 9. Evidence Source Map

| case | evidence source class | what is allowed for scoring | what is blocked |
|---|---|---|---|
| 한일사료 | global food-security / grain shock | Stage2-Actionable if supply shock can plausibly affect pricing and demand | Green without confirmed margin/revision bridge |
| YBM넷 | COVID online-class / remote education demand | Stage2-Actionable with direct demand optionality | Green without retention/revenue proof |
| CJ씨푸드 | Fukushima treated-water / food-safety fear | event-risk watch and 4B overlay | Stage2 promotion if no channel reorder / substitution evidence |
| NE능률 | political/person theme | price-risk and 4B/4C protection only | policy-stage promotion without legislation, subsidy, procurement, or contract |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | profile caveat | clean 180D? |
|---:|---|---|---|---|
| `005860` | `atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv` | `atlas/symbol_profiles/005/005860.json` | corporate-action candidates exist historically but none overlap selected 180D window | yes |
| `057030` | `atlas/ohlcv_tradable_by_symbol_year/057/057030/2020.csv` | `atlas/symbol_profiles/057/057030.json` | corporate-action candidates exist historically but none overlap selected 180D window | yes |
| `011150` | `atlas/ohlcv_tradable_by_symbol_year/011/011150/2023.csv` | `atlas/symbol_profiles/011/011150.json` | corporate-action candidates exist historically but none overlap selected 180D window | yes |
| `053290` | `atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv` | `atlas/symbol_profiles/053/053290.json` | corporate-action candidates exist historically but none overlap selected 180D window | yes |

## 11. Case-by-Case Trigger Grid

| trigger_id | case | type | evidence at date | Stage2 fields | Stage3 fields | 4B/4C fields | dedupe |
|---|---|---|---|---|---|---|---|
| `R12_C31_005860_STAGE2A_20220224` | 한일사료 | Stage2-Actionable | Russia-Ukraine war shock raised global grain/feed cost and food-security optionality; company-specific public evidence was still event/supply-route, not durable order backlog. | public_event_or_disclosure, policy_or_regulatory_optionality, capacity_or_volume_route | financial_visibility | valuation_blowoff, positioning_overheat, price_only_local_peak | representative |
| `R12_C31_005860_4B_20220425` | 한일사료 | Stage4B overlay | price/positioning peak after event run | none | none | valuation_blowoff, positioning_overheat, price_only_local_peak | overlay_only |
| `R12_C31_057030_STAGE2A_20200221` | YBM넷 | Stage2-Actionable | School closure / online-class transition created direct demand optionality for online education providers; later price action required retention/revenue validation before Green. | public_event_or_disclosure, policy_or_regulatory_optionality, capacity_or_volume_route, relative_strength | multiple_public_sources | valuation_blowoff, positioning_overheat, price_only_local_peak | representative |
| `R12_C31_057030_4B_20200828` | YBM넷 | Stage4B overlay | price/positioning peak after event run | none | none | valuation_blowoff, positioning_overheat, price_only_local_peak | overlay_only |
| `R12_C31_011150_STAGE2WATCH_20230822` | CJ씨푸드 | Stage2_event_premium_risk_watch | Fukushima treated-water release / seafood-import fear produced a rapid seafood-stock move, but no durable channel reorder, margin bridge, or repeat-order proof was visible at trigger time. | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | none | price_only_local_peak, positioning_overheat, thesis_evidence_broken | representative |
| `R12_C31_011150_4B_20230823` | CJ씨푸드 | Stage4B overlay | price/positioning peak after event run | none | none | price_only_local_peak, positioning_overheat | overlay_only |
| `R12_C31_053290_STAGE2WATCH_20210304` | NE능률 | Stage2_event_premium_risk_watch | Political/person-related education-policy theme drove price, but trigger evidence did not contain a legislated subsidy, official procurement route, contract, or earnings bridge. | relative_strength, public_event_or_disclosure | none | valuation_blowoff, positioning_overheat, price_only_local_peak, thesis_evidence_broken | representative |
| `R12_C31_053290_4B_20210609` | NE능률 | Stage4B overlay | price/positioning peak after event run | none | none | valuation_blowoff, positioning_overheat, price_only_local_peak | overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| case | trigger | entry | price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | profile verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 한일사료 `005860` | 2022-02-24 | 2022-02-24 | 2,555 | 85.52% | 520.35% | 520.35% | -18.59% | -18.59% | -18.59% | 2022-04-25 / 15,850 | current_profile_missed_structural |
| YBM넷 `057030` | 2020-02-21 | 2020-02-21 | 4,175 | 161.08% | 173.05% | 254.49% | -21.44% | -21.44% | -21.44% | 2020-08-28 / 14,800 | current_profile_correct |
| CJ씨푸드 `011150` | 2023-08-22 | 2023-08-22 | 3,495 | 22.03% | 22.03% | 22.03% | -23.03% | -28.76% | -28.76% | 2023-08-23 / 4,265 | current_profile_false_positive |
| NE능률 `053290` | 2021-03-04 | 2021-03-04 | 4,450 | 476.40% | 591.01% | 591.01% | -21.24% | -21.24% | -21.24% | 2021-06-09 / 30,750 | current_profile_4B_too_late |

## 13. Current Calibrated Profile Stress Test

| case | P0 likely label | verdict | explanation |
|---|---|---|---|
| 한일사료 | Stage2-Actionable / Yellow watch | current_profile_missed_structural | supply-security shock produced huge MFE before ordinary revision evidence; C31 needs a narrow route for event-to-pricing bridge |
| YBM넷 | Stage2-Actionable | current_profile_correct | direct policy/demand event worked, but late blowoff confirms Green must wait for revenue/retention proof |
| CJ씨푸드 | Stage2-Actionable candidate | current_profile_false_positive | fear event had limited upside and sustained MAE; no reorder bridge |
| NE능률 | Stage2-Actionable candidate or price watch | current_profile_4B_too_late | huge MFE does not validate policy evidence; the useful calibration is 4B/4C protection, not Green promotion |

Applied global axes are mostly kept. The residual is a **C31 archetype guard**: policy/event language is not enough; it must become official demand, supply-security pricing, procurement, subsidy, or revenue conversion.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 result | Yellow implication | Green implication | green_lateness_ratio |
|---|---|---|---|---|
| 한일사료 | useful and early | could be Yellow if price shock plus margin pass-through is visible | Green only after confirmed financial bridge | not_applicable |
| YBM넷 | useful and early | Yellow with online-user/revenue indications | Green blocked without retention | not_applicable |
| CJ씨푸드 | watch-only; not Actionable | no Yellow | no Green | not_applicable |
| NE능률 | watch-only; not Actionable | no Yellow | no Green | not_applicable |

## 15. 4B Local vs Full-window Timing Audit

| case | local peak | full observed peak proxy | 4B verdict | evidence type |
|---|---|---|---|---|
| 한일사료 | 2022-04-25 / 15,850 | same | good local 4B after blowoff; full 4B needs exhaustion evidence | valuation_blowoff; positioning_overheat |
| YBM넷 | 2020-08-28 / 14,800 | same | good full-window 4B timing after event-driven blowoff | valuation_blowoff; positioning_overheat |
| CJ씨푸드 | 2023-08-23 / 4,265 | same | price-only local 4B; not full positive-stage evidence | price_only; positioning_overheat |
| NE능률 | 2021-06-09 / 30,750 | same | 4B should dominate; political theme is not Green | price_only; valuation_blowoff |

## 16. 4C Protection Audit

| case | 4C label | protection logic |
|---|---|---|
| 한일사료 | thesis_break_watch_only | after supply shock/war premium fades, lack of sustained earnings bridge should trigger risk reduction |
| YBM넷 | thesis_break_watch_only | reopening / normalization weakens remote-only thesis unless retention data offsets it |
| CJ씨푸드 | hard_4c_success | event fear dissipates without channel conversion; avoids MAE drift |
| NE능률 | hard_4c_success | political-person narrative breaks because no binding policy/procurement evidence exists |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`, but only as L10/C31 shadow logic.

Candidate rule:

```text
For L10 policy/event cases, Stage2-Actionable may be allowed when the event has an official demand, supply-security, procurement, subsidy, or channel-conversion path. Stage3-Green must require a second bridge: confirmed revenue, margin, contract, repeated order, subsidy allocation, or financial revision.
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

C31-specific guard:

```text
C31 headline/policy/person/fear events without official cash-flow route are event-premium watch rows. They can calibrate 4B/4C protection but cannot promote Stage2-Actionable or Stage3-Green.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 `e2r_2_1_stock_web_calibrated_proxy` | default | existing axes only | 4 | 326.61% | -22.51% | 0.50 | 1 | good on global 4B guard, weak on C31 event-quality split |
| P0b `e2r_2_0_baseline_reference` | rollback | lower event guard | 4 | 326.61% | -22.51% | 0.75 | 1 | over-promotes price/event themes |
| P1 `sector_specific_candidate_profile` | L10 | event_quality_gate + event_to_cashflow_bridge | 4 | 326.61% | -22.51% | 0.25 | 0 | better separates policy demand from pure event premium |
| P2 `canonical_archetype_candidate_profile` | C31 | official_policy_or_supply_shock + channel_conversion required for Green | 4 | 326.61% | -22.51% | 0.25 | 0 | strongest explanatory fit |
| P3 `counterexample_guard_profile` | C31 guard | political_person_theme_block + food_safety_no_reorder_cap | 2 | 306.52% | -25.00% | 0.00 | 0 | blocks false Green while keeping Stage2 watch |

## 20. Score-Return Alignment Matrix

| symbol | before score / label | after score / label | return alignment |
|---:|---|---|---|
| 005860 | 72 / Stage2-Actionable | 78 / Stage3-Yellow_candidate_only | after better recognizes supply-security shock but still blocks Green |
| 057030 | 76 / Stage2-Actionable | 78 / Stage2-Actionable_with_policy_event_bridge | after preserves useful Stage2 without Green overfit |
| 011150 | 74 / Stage2-Actionable_candidate | 62 / Stage2_event_premium_risk_watch | after avoids false positive |
| 053290 | 75 / Stage2-Actionable_candidate | 58 / price_only_event_premium_watch | after blocks political/person theme promotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POLICY_EVENT_SUPPLY_SECURITY_ONLINE_EDUCATION_FOOD_SAFETY_THEME_GUARD | 2 | 2 | 4 | 2 | 4 | 0 | 7 | 4 | 3 | true | true | Needs more official subsidy/procurement cases; event-premium guard now better represented |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - missed_supply_security_event
  - food_safety_event_false_positive
  - political_person_theme_4B_late
new_axis_proposed: null
existing_axis_strengthened:
  - C31 event_to_cashflow_bridge
  - C31 political_person_theme_block
  - C31 food_safety_no_reorder_cap
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web tradable-row OHLC path for four C31 cases,
- clean 180D windows based on symbol profile corporate-action dates,
- MFE/MAE and event-to-return alignment,
- C31 positive/counterexample split,
- local/full-window 4B overlay distinction.

Not validated:

- live watchlist or 2026 candidate scan,
- production scoring code,
- brokerage/autotrading,
- exact company earnings attribution beyond proxy component scoring.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_event_to_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Require policy/event to pass through to official demand, supply-security pricing, channel conversion, subsidy, or procurement before Green","Reduces CJ/NE false Green while preserving Hanil/YBM Stage2 optionality","R12_C31_005860_STAGE2A_20220224|R12_C31_057030_STAGE2A_20200221|R12_C31_011150_STAGE2WATCH_20230822|R12_C31_053290_STAGE2WATCH_20210304",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_political_person_theme_block,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Political/person association without legislated subsidy/procurement/contract is event-premium watch, not Stage2-Actionable promotion","Blocks NE-style price-only theme from positive calibration despite large MFE","R12_C31_053290_STAGE2WATCH_20210304",1,1,1,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,c31_food_safety_no_reorder_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Food-safety shock requires channel reorder or inventory conversion before Green; fear-only substitution gets capped","Reduces CJ seafood false positive and improves 4B timing","R12_C31_011150_STAGE2WATCH_20230822",1,1,1,medium,counterexample_guard,"not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L10C31_HANILFEED_GRAIN_SHOCK_2022", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GRAIN_FEED_SUPPLY_SECURITY_PRICE_SHOCK", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "R12_C31_005860_STAGE2A_20220224", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 event was early and economically real, but current profile needs a C31 rule that requires policy/supply shock to pass through to pricing or volume before Green.", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "large_mfe_but_event_blowoff"}
{"row_type": "trigger", "trigger_id": "R12_C31_005860_STAGE2A_20220224", "case_id": "R12L10C31_HANILFEED_GRAIN_SHOCK_2022", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GRAIN_FEED_SUPPLY_SECURITY_PRICE_SHOCK", "sector": "agri_feed_supply_security", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Russia-Ukraine war shock raised global grain/feed cost and food-security optionality; company-specific public evidence was still event/supply-route, not durable order backlog.", "evidence_source": "External event context: 2022 global food-price shock / Ukraine grain disruption; price rows: stock-web 005860 2022 shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 2555, "MFE_30D_pct": 85.52, "MFE_90D_pct": 520.35, "MFE_180D_pct": 520.35, "MFE_1Y_pct": 520.35, "MFE_2Y_pct": 520.35, "MAE_30D_pct": -18.59, "MAE_90D_pct": -18.59, "MAE_180D_pct": -18.59, "MAE_1Y_pct": -18.59, "MAE_2Y_pct": -18.59, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-25", "peak_price": 15850, "drawdown_after_peak_pct": -82.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B_until_non_price_or_exhaustion_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "large_mfe_but_event_blowoff", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C31_HANILFEED_GRAIN_SHOCK_2022_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10C31_HANILFEED_GRAIN_SHOCK_2022", "trigger_id": "R12_C31_005860_STAGE2A_20220224", "symbol": "005860", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow_candidate_only", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Stage2 event was early and economically real, but current profile needs a C31 rule that requires policy/supply shock to pass through to pricing or volume before Green.", "MFE_90D_pct": 520.35, "MAE_90D_pct": -18.59, "score_return_alignment_label": "large_mfe_but_event_blowoff", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "trigger", "trigger_id": "R12_C31_005860_4B_20220425", "case_id": "R12L10C31_HANILFEED_GRAIN_SHOCK_2022", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "GRAIN_FEED_SUPPLY_SECURITY_PRICE_SHOCK", "sector": "agri_feed_supply_security", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2022-04-25", "evidence_available_at_that_date": "local/full-window price blowoff after event run; non-price evidence varies by case and is used only as overlay, not promotion", "evidence_source": "stock-web peak row and historical event exhaustion context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-25", "entry_price": 15850, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2022-04-25", "peak_price": 15850, "drawdown_after_peak_pct": -82.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_timing_but_full_4B_requires_non_price_context", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_after_event_peak", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C31_HANILFEED_GRAIN_SHOCK_2022_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay for same case", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "case", "case_id": "R12L10C31_YBMNET_REMOTE_EDU_2020", "symbol": "057030", "company_name": "YBM넷", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_REMOTE_EDUCATION_POLICY_DEMAND", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12_C31_057030_STAGE2A_20200221", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2-Actionable captured event demand; Green should remain blocked without recurring-user or revenue-retention bridge.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "positive_stage2_event_with_late_blowoff"}
{"row_type": "trigger", "trigger_id": "R12_C31_057030_STAGE2A_20200221", "case_id": "R12L10C31_YBMNET_REMOTE_EDU_2020", "symbol": "057030", "company_name": "YBM넷", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_REMOTE_EDUCATION_POLICY_DEMAND", "sector": "education_service_online", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-02-21", "evidence_available_at_that_date": "School closure / online-class transition created direct demand optionality for online education providers; later price action required retention/revenue validation before Green.", "evidence_source": "External event context: COVID-era school closures and online classes in Korea; price rows: stock-web 057030 2020 shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/057/057030/2020.csv", "profile_path": "atlas/symbol_profiles/057/057030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-02-21", "entry_price": 4175, "MFE_30D_pct": 161.08, "MFE_90D_pct": 173.05, "MFE_180D_pct": 254.49, "MFE_1Y_pct": 254.49, "MFE_2Y_pct": 254.49, "MAE_30D_pct": -21.44, "MAE_90D_pct": -21.44, "MAE_180D_pct": -21.44, "MAE_1Y_pct": -21.44, "MAE_2Y_pct": -35.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-08-28", "peak_price": 14800, "drawdown_after_peak_pct": -76.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B_until_non_price_or_exhaustion_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_stage2_event_with_late_blowoff", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C31_YBMNET_REMOTE_EDU_2020_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10C31_YBMNET_REMOTE_EDU_2020", "trigger_id": "R12_C31_057030_STAGE2A_20200221", "symbol": "057030", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 1, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 1, "policy_or_regulatory_score": 4, "valuation_repricing_score": 2, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable_with_policy_event_bridge", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Stage2-Actionable captured event demand; Green should remain blocked without recurring-user or revenue-retention bridge.", "MFE_90D_pct": 173.05, "MAE_90D_pct": -21.44, "score_return_alignment_label": "positive_stage2_event_with_late_blowoff", "current_profile_verdict": "current_profile_correct"}
{"row_type": "trigger", "trigger_id": "R12_C31_057030_4B_20200828", "case_id": "R12L10C31_YBMNET_REMOTE_EDU_2020", "symbol": "057030", "company_name": "YBM넷", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "COVID_REMOTE_EDUCATION_POLICY_DEMAND", "sector": "education_service_online", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2020-08-28", "evidence_available_at_that_date": "local/full-window price blowoff after event run; non-price evidence varies by case and is used only as overlay, not promotion", "evidence_source": "stock-web peak row and historical event exhaustion context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/057/057030/2020.csv", "profile_path": "atlas/symbol_profiles/057/057030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-08-28", "entry_price": 14800, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2020-08-28", "peak_price": 14800, "drawdown_after_peak_pct": -76.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_timing_but_full_4B_requires_non_price_context", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_after_event_peak", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C31_YBMNET_REMOTE_EDU_2020_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay for same case", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "case", "case_id": "R12L10C31_CJSEAFOOD_FUKUSHIMA_2023", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SAFETY_IMPORT_BAN_CONSUMER_SUBSTITUTION_THEME", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12_C31_011150_STAGE2WATCH_20230822", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Current profile could still over-credit policy/event visibility if it ignores absence of actual reorder / channel conversion evidence.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "event_premium_faded"}
{"row_type": "trigger", "trigger_id": "R12_C31_011150_STAGE2WATCH_20230822", "case_id": "R12L10C31_CJSEAFOOD_FUKUSHIMA_2023", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SAFETY_IMPORT_BAN_CONSUMER_SUBSTITUTION_THEME", "sector": "food_safety_seafood_event", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2023-08-22", "evidence_available_at_that_date": "Fukushima treated-water release / seafood-import fear produced a rapid seafood-stock move, but no durable channel reorder, margin bridge, or repeat-order proof was visible at trigger time.", "evidence_source": "External event context: Japan Fukushima treated-water release and seafood import reactions; price rows: stock-web 011150 2023 shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011150/2023.csv", "profile_path": "atlas/symbol_profiles/011/011150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-22", "entry_price": 3495, "MFE_30D_pct": 22.03, "MFE_90D_pct": 22.03, "MFE_180D_pct": 22.03, "MFE_1Y_pct": 22.03, "MFE_2Y_pct": 22.03, "MAE_30D_pct": -23.03, "MAE_90D_pct": -28.76, "MAE_180D_pct": -28.76, "MAE_1Y_pct": -28.76, "MAE_2Y_pct": -28.76, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-23", "peak_price": 4265, "drawdown_after_peak_pct": -41.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B_until_non_price_or_exhaustion_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_premium_faded", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C31_CJSEAFOOD_FUKUSHIMA_2023_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10C31_CJSEAFOOD_FUKUSHIMA_2023", "trigger_id": "R12_C31_011150_STAGE2WATCH_20230822", "symbol": "011150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 1, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable_candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 1, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "Stage2_event_premium_risk_watch", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Current profile could still over-credit policy/event visibility if it ignores absence of actual reorder / channel conversion evidence.", "MFE_90D_pct": 22.03, "MAE_90D_pct": -28.76, "score_return_alignment_label": "event_premium_faded", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "trigger", "trigger_id": "R12_C31_011150_4B_20230823", "case_id": "R12L10C31_CJSEAFOOD_FUKUSHIMA_2023", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "FOOD_SAFETY_IMPORT_BAN_CONSUMER_SUBSTITUTION_THEME", "sector": "food_safety_seafood_event", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2023-08-23", "evidence_available_at_that_date": "local/full-window price blowoff after event run; non-price evidence varies by case and is used only as overlay, not promotion", "evidence_source": "stock-web peak row and historical event exhaustion context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011150/2023.csv", "profile_path": "atlas/symbol_profiles/011/011150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-23", "entry_price": 4265, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2023-08-23", "peak_price": 4265, "drawdown_after_peak_pct": -41.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_timing_but_full_4B_requires_non_price_context", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_after_event_peak", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C31_CJSEAFOOD_FUKUSHIMA_2023_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay for same case", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "case", "case_id": "R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021", "symbol": "053290", "company_name": "NE능률", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLITICAL_PERSON_THEME_NOT_POLICY_CONTRACT", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R12_C31_053290_STAGE2WATCH_20210304", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Large MFE is not enough. C31 should treat non-binding political/person themes as event-premium rows and calibrate 4B/4C protection, not Stage3-Green promotion.", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "huge_price_event_but_not_fundamental_policy"}
{"row_type": "trigger", "trigger_id": "R12_C31_053290_STAGE2WATCH_20210304", "case_id": "R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021", "symbol": "053290", "company_name": "NE능률", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLITICAL_PERSON_THEME_NOT_POLICY_CONTRACT", "sector": "education_policy_person_theme", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2_event_premium_risk_watch", "trigger_date": "2021-03-04", "evidence_available_at_that_date": "Political/person-related education-policy theme drove price, but trigger evidence did not contain a legislated subsidy, official procurement route, contract, or earnings bridge.", "evidence_source": "External event context: 2021 Korean political-theme trading; price rows: stock-web 053290 2021 shard.", "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv", "profile_path": "atlas/symbol_profiles/053/053290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-03-04", "entry_price": 4450, "MFE_30D_pct": 476.4, "MFE_90D_pct": 591.01, "MFE_180D_pct": 591.01, "MFE_1Y_pct": 591.01, "MFE_2Y_pct": 591.01, "MAE_30D_pct": -21.24, "MAE_90D_pct": -21.24, "MAE_180D_pct": -21.24, "MAE_1Y_pct": -30.34, "MAE_2Y_pct": -55.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-09", "peak_price": 30750, "drawdown_after_peak_pct": -84.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B_until_non_price_or_exhaustion_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "huge_price_event_but_not_fundamental_policy", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021_ENTRY", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021", "trigger_id": "R12_C31_053290_STAGE2WATCH_20210304", "symbol": "053290", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 1, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage2-Actionable_candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 1, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "price_only_event_premium_watch", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Large MFE is not enough. C31 should treat non-binding political/person themes as event-premium rows and calibrate 4B/4C protection, not Stage3-Green promotion.", "MFE_90D_pct": 591.01, "MAE_90D_pct": -21.24, "score_return_alignment_label": "huge_price_event_but_not_fundamental_policy", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "trigger", "trigger_id": "R12_C31_053290_4B_20210609", "case_id": "R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021", "symbol": "053290", "company_name": "NE능률", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLITICAL_PERSON_THEME_NOT_POLICY_CONTRACT", "sector": "education_policy_person_theme", "primary_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2021-06-09", "evidence_available_at_that_date": "local/full-window price blowoff after event run; non-price evidence varies by case and is used only as overlay, not promotion", "evidence_source": "stock-web peak row and historical event exhaustion context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053290/2021.csv", "profile_path": "atlas/symbol_profiles/053/053290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-06-09", "entry_price": 30750, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": "2021-06-09", "peak_price": 30750, "drawdown_after_peak_pct": -84.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_timing_but_full_4B_requires_non_price_context", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_after_event_peak", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L10C31_NEEDU_POLITICAL_POLICY_THEME_2021_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay for same case", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "residual_contribution", "round": "R12", "loop": "10", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "new_symbols=4; new_trigger_families=4; counterexamples=2; residual_errors=3; wrong_round_penalty=0", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["missed_supply_security_event", "food_safety_event_false_positive", "political_person_theme_4B_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied `e2r_2_1_stock_web_calibrated` profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
- Do not apply global deltas unless multiple `large_sector_id` values support the same direction.
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
completed_loop = 10
next_round = R13
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest: `atlas/manifest.json` with `max_date=2026-02-20`.
- Stock-web schema: `atlas/schema.json`; MFE/MAE formulas follow schema definitions.
- Stock-web symbol profiles checked: `005860`, `057030`, `011150`, `053290`.
- Price shards checked: `005860/2022.csv`, `057030/2020.csv`, `011150/2023.csv`, `053290/2021.csv`.
- Historical context sources used only to classify event families: global food-price shock from Ukraine war, Korea COVID online-class transition, Fukushima treated-water release and seafood reaction, and 2021 Korean political/person theme trading.
- This MD is not investment advice and contains no current/live candidate scan.

