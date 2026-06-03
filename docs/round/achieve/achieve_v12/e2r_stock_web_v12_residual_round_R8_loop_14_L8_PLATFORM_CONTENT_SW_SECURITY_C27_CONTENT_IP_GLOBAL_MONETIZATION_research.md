# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R8_loop_14_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
scheduled_round: R8
scheduled_loop: 14
completed_round: R8
completed_loop: 14
next_round: R9
next_loop: 14
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GLOBAL_GAME_IP_MONETIZATION_CONVERSION
loop_objective:
  - coverage_gap_fill
  - residual_false_positive_mining
  - counterexample_mining
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
current_stock_discovery_allowed: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
```

This loop adds **3** new independent cases, **2** counterexamples, and **1** residual error for **R8 / L8_PLATFORM_CONTENT_SW_SECURITY / C27_CONTENT_IP_GLOBAL_MONETIZATION**.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Applied global axes assumed already active:

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

This MD does **not** re-prove those global rules. It tests a C27-specific residual: in games/content names, a launch, trailer, review, or ranking signal can be mistaken for monetization. The research question is whether C27 needs a separate **monetization-conversion gate**.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R8 |
| scheduled_loop | 14 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| fine_archetype_id | GLOBAL_GAME_IP_MONETIZATION_CONVERSION |
| round_sector_consistency | pass |
| selected scope | Korean listed game/content IP stocks with actual stock-web 1D OHLC |
| excluded scope | live candidates, stock_agent source code, current recommendations |

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`, so the round-sector pair is valid. C27 was chosen because prior R8 coverage can easily over-collapse platform/SW and game-IP cases: a chart can move like a rocket on a trailer, but the business is only changing if the audience is converted into spend, retention, or recurring operating leverage.

## 3. Previous Coverage / Duplicate Avoidance Check

The local schedule state from the prior generated MD ended at `R7 / loop 14` and computed `next_round=R8 / next_loop=14`. The stock_agent registry available in `main` shows older R8 platform/content/SW research files through earlier loops, but the current sandbox-generated v12 sequence is ahead of the repository registry. Therefore this run follows the immediate prior handoff state, not the stale main-branch registry.

Duplicate-avoidance result:

| Check | Result |
|---|---|
| same symbol + same trigger_date + same entry_date reused | no |
| same canonical_archetype reused | yes, intentionally |
| new independent symbols | 3 |
| new trigger families | 4 |
| expected duplicate value | low |
| novelty gate | pass |

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest was checked before the case rows were assembled.

| Manifest field | Value |
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

Important caveat: the OHLC data are raw/unadjusted. Corporate-action contaminated windows are blocked for weight calibration. The three representative cases below have clean 180D windows under the inspected symbol profiles.

## 5. Historical Eligibility Gate

| Case | Symbol | Entry date | 180D available by manifest max_date | Corporate-action contamination | Calibration usable |
|---|---:|---:|---:|---:|---:|
| Cookie Run: Kingdom launch conversion | 194480 | 2021-01-21 | yes | none in profile | true |
| Lies of P release quality without durable monetization | 095660 | 2023-09-19 | yes | no post-2009 candidate in window | true |
| DokeV Gamescom trailer buzz | 263750 | 2021-08-25 | yes | prior 2021-04-16 outside 180D window | true |

The metaphor here is simple: **C27 is not a movie poster. It is the ticket counter after the poster works.** The market may pay for the poster for a while, but the scoring rule should reward the turnstile only when traffic converts into revenue.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | Compression rule |
|---|---|---|
| mobile_game_launch_rank_conversion | C27_CONTENT_IP_GLOBAL_MONETIZATION | positive only if launch attention converts into repeat ranking, downloads, or monetization evidence |
| premium_package_game_quality_release | C27_CONTENT_IP_GLOBAL_MONETIZATION | quality/review signal is not enough without unit-sales visibility or follow-on IP monetization |
| global_trailer_reveal_buzz | C27_CONTENT_IP_GLOBAL_MONETIZATION | trailer attention is Stage2/event attention; cannot promote Stage3 by itself |
| price_only_content_IP_blowoff | C27_CONTENT_IP_GLOBAL_MONETIZATION | 4B overlay allowed, full 4B requires non-price deterioration |

## 7. Case Selection Summary

| case_id | Symbol | Company | Role | Why selected |
|---|---:|---|---|---|
| R8L14_C27_194480_COOKIE_RUN_KINGDOM_20210121 | 194480 | 데브시스터즈 | structural_success | Launch became a monetization/ranking conversion route; extreme MFE validates C27 positive path. |
| R8L14_C27_095660_LIES_OF_P_RELEASE_20230919 | 095660 | 네오위즈 | failed_rerating | Quality release without durable monetization bridge; current proxy can over-score product quality. |
| R8L14_C27_263750_DOKEV_TRAILER_20210825 | 263750 | 펄어비스 | price_moved_without_evidence | Trailer/global attention moved price, but commercialization was absent; useful price-only guardrail case. |

## 8. Positive vs Counterexample Balance

| Count type | Count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| representative_trigger_count | 3 |
| new_independent_case_count | 3 |

The balance is intentionally counterexample-heavy because C27’s residual error is not “missing all IP winners.” It is subtler: **the model can confuse applause with cash register sound.**

## 9. Evidence Source Map

| Trigger family | Evidence allowed at trigger date | Evidence not allowed |
|---|---|---|
| mobile game launch conversion | launch, rankings/downloads/revenue-app evidence, relative strength | later annual financials backfilled into trigger |
| premium package game release | release, reviews, platform availability | later sequel/DLC news unless separately triggered |
| trailer/global showcase | public showcase, media attention, relative strength | treating trailer attention as Stage3 monetization |
| price-only 4B overlay | local peak, valuation expansion, positioning overheat | treating price-only as full 4B exit |

## 10. Price Data Source Map

| Symbol | Company | Profile path | Price shard path(s) | Corporate action status |
|---:|---|---|---|---|
| 194480 | 데브시스터즈 | atlas/symbol_profiles/194/194480.json | atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv | clean, no candidate dates |
| 095660 | 네오위즈 | atlas/symbol_profiles/095/095660.json | atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv; 2024.csv | historical candidates only, outside window |
| 263750 | 펄어비스 | atlas/symbol_profiles/263/263750.json | atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv; 2022.csv | 2021-04-16 candidate outside entry~D+180 |

## 11. Case-by-Case Trigger Grid

| trigger_id | Symbol | Type | Trigger date | Entry date | Entry price | Role | Current profile verdict |
|---|---:|---|---:|---:|---:|---|---|
| R8L14_T01_194480_STAGE2_ACTIONABLE_COOKIE_RUN_KINGDOM_LAUNCH | 194480 | Stage2-Actionable | 2021-01-21 | 2021-01-21 | 17,250 | representative | current_profile_correct |
| R8L14_T02_194480_PRICE_ONLY_4B_LOCAL_PEAK | 194480 | 4B-overlay | 2021-09-27 | 2021-09-27 | 186,000 | 4B overlay | current_profile_correct |
| R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE | 095660 | Stage2-Actionable | 2023-09-19 | 2023-09-19 | 34,500 | representative | current_profile_false_positive |
| R8L14_T04_095660_4C_THESIS_BREAK_WATCH | 095660 | 4C-watch | 2023-10-05 | 2023-10-05 | 23,350 | 4C overlay | current_profile_4C_too_late |
| R8L14_T05_263750_STAGE2_TRAILER_BUZZ_DOKEV_GAMESCOM | 263750 | Stage2-trailer-buzz | 2021-08-25 | 2021-08-25 | 70,000 | representative | current_profile_correct |
| R8L14_T06_263750_4B_PRICE_ONLY_OVERLAY | 263750 | 4B-overlay | 2021-11-17 | 2021-11-17 | 141,000 | 4B overlay | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

| trigger_id | Entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | Peak date | Peak price | Outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R8L14_T01_194480_STAGE2_ACTIONABLE_COOKIE_RUN_KINGDOM_LAUNCH | 17,250 | 300.00% | -12.75% | 833.33% | -12.75% | 1056.52% | -12.75% | 2021-09-27 | 199,500 | structural_success |
| R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE | 34,500 | 3.04% | -32.32% | 3.04% | -32.32% | 3.04% | -44.64% | 2023-09-19 | 35,550 | failed_rerating |
| R8L14_T05_263750_STAGE2_TRAILER_BUZZ_DOKEV_GAMESCOM | 70,000 | 45.71% | -3.14% | 107.43% | -3.14% | 107.43% | -3.14% | 2021-11-17 | 145,200 | price_moved_without_monetization_evidence |

### Overlay triggers

| trigger_id | Entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | 4B local proximity | 4B full-window proximity | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| R8L14_T02_194480_PRICE_ONLY_4B_LOCAL_PEAK | 186,000 | 7.26% | -40.86% | 7.26% | -40.86% | 0.925 | 0.925 | good local peak but price-only |
| R8L14_T04_095660_4C_THESIS_BREAK_WATCH | 23,350 | 32.55% | -0.64% | 32.55% | -8.99% | n/a | n/a | thesis-break watch only |
| R8L14_T06_263750_4B_PRICE_ONLY_OVERLAY | 141,000 | 2.98% | -5.25% | 2.98% | -34.89% | 0.944 | 0.944 | good local peak but price-only |

## 13. Current Calibrated Profile Stress Test

| Case | Current proxy judgment | Actual MFE/MAE fit | Residual |
|---|---|---|---|
| 194480 | Promotable Stage2/Yellow; Green only after conversion/revision | correct | none |
| 095660 | Could over-score as quality/IP global release | false positive | quality-release evidence needs monetization guard |
| 263750 | Price-only guard should block positive Stage3 | correct | still useful for C27 guard calibration |

Stress-test answers:

1. Current calibrated profile handles 194480 correctly because non-price conversion evidence existed.
2. Current calibrated profile is vulnerable in 095660 if product quality is treated like revenue conversion.
3. Stage2 actionable bonus is not globally wrong; it needs a C27 evidence-quality filter.
4. Yellow 75 is too permissive for C27 when the score is made of release/review/trailer evidence.
5. Green 87 / revision 55 should remain strict; C27 Green should require monetization conversion or visible operating leverage.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate.
8. Hard 4C should not be forced by price alone; use thesis-break watch until monetization evidence is actually broken.

## 14. Stage2 / Yellow / Green Comparison

| Case | Stage2 trigger | Stage3-Yellow candidate | Stage3-Green candidate | green_lateness_ratio |
|---|---|---|---|---|
| 194480 | 2021-01-21 | 2021-01-21/after early conversion evidence | after ranking/download/revenue conversion | 0.0~0.3 estimated |
| 095660 | 2023-09-19 | should be capped below Yellow unless monetization appears | no confirmed Green | not_applicable |
| 263750 | 2021-08-25 | should be event-watch, not Yellow | no confirmed Green | not_applicable |

C27 needs a gate: `quality_release_signal != monetization_conversion_signal`.

## 15. 4B Local vs Full-window Timing Audit

| Trigger | Local proximity | Full-window proximity | Evidence type | Verdict |
|---|---:|---:|---|---|
| 194480 4B | 0.925 | 0.925 | price_only, valuation_blowoff, positioning_overheat | overlay useful; not full 4B without non-price deterioration |
| 263750 4B | 0.944 | 0.944 | price_only, valuation_blowoff, positioning_overheat | overlay useful; not full 4B without commercialization delay/financial evidence |
| 095660 4C-watch | n/a | n/a | thesis_evidence_broken watch | not hard 4C by price alone |

## 16. 4C Protection Audit

| Case | 4C route | Label |
|---|---|---|
| 194480 | no thesis-break in initial 180D | not_applicable |
| 095660 | quality launch failed to convert into durable rerating | thesis_break_watch_only |
| 263750 | trailer buzz did not equal monetization; no hard failure yet | thesis_break_watch_only |

## 17. Sector-Specific Rule Candidate

No broad R8 sector-specific rule is proposed. The evidence here is too specific to games/content IP. This is not a platform advertising rule, not a general software retention rule, and not a security-contract rule.

```text
sector_specific_rule_candidate = false
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

Proposed C27 shadow axes:

1. `C27_ip_monetization_conversion_bonus = +4`
   - Applies when launch/trailer/release evidence is accompanied by ranking, downloads, revenue conversion, repeat purchase, live-service retention, royalty, or operating-leverage evidence.

2. `C27_trailer_or_review_quality_guard = -8`
   - Applies when evidence is only trailer buzz, review quality, awards, or platform availability without monetization conversion.

3. `C27_price_only_4B_overlay_not_full_exit = keep`
   - Price-only local peaks are valid overlay rows but should not become full 4B exits without non-price evidence.

## 19. Before / After Backtest Comparison

| Profile | Hypothesis | Eligible trigger count | Avg MFE 90D | Avg MAE 90D | False positive rate | Score-return alignment |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 314.60% | -16.07% | 33.3% | mixed |
| P0b e2r_2_0_baseline_reference | looser quality/event scoring | 3 | 314.60% | -16.07% | 66.7% | weak |
| P1 sector_specific_candidate_profile | no sector-wide change | 3 | 314.60% | -16.07% | 33.3% | mixed |
| P2 canonical_archetype_candidate_profile | add C27 monetization gate | 3 | 314.60% | -16.07% | 0.0% selected-positive false positive | improved |
| P3 counterexample_guard_profile | cap trailer/review-only events below Yellow | 3 | 314.60% | -16.07% | 0.0% | improved but conservative |

## 20. Score-Return Alignment Matrix

| Trigger | Score before | Stage before | Score after | Stage after | Return alignment |
|---|---:|---|---:|---|---|
| 194480 Cookie Run launch | 83 | Stage3-Yellow | 88 | Stage3-Green | aligned |
| 095660 Lies of P release | 76 | Stage3-Yellow | 67 | Stage2-Watch | improved |
| 263750 DokeV trailer | 75 | Stage3-Yellow | 59 | Stage2-Watch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | GLOBAL_GAME_IP_MONETIZATION_CONVERSION | 1 | 2 | 2 | 1 | 3 | 0 | 6 | 3 | 1 | false | true | C27 still needs more non-game content/IP examples, but game-IP monetization conversion gap is partially filled. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 1
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage3_green_revision_min
residual_error_types_found:
  - quality_release_without_monetization_false_positive
  - trailer_buzz_price_move_without_revenue
  - price_only_4B_overlay_not_full_exit
new_axis_proposed:
  - C27_ip_monetization_conversion_bonus
  - C27_trailer_or_review_quality_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- symbol profile availability and corporate-action caveat
- actual tradable OHLC rows for selected entry / peak / drawdown windows
- representative trigger-level MFE / MAE direction
- C27 positive vs counterexample balance
- current profile stress-test verdicts
```

Not validated:

```text
- live 2026 candidate status
- real-time price after stock-web manifest max_date
- production stock_agent scoring code
- exact broker-executable signals
- revised financial statement ingestion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_ip_monetization_conversion_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,4,+4,"Reward launch/trailer/release evidence only when monetization conversion exists.","Preserves 194480 positive and demotes 095660/263750 event-only rows.","R8L14_T01|R8L14_T03|R8L14_T05",3,3,2,medium,canonical_archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_trailer_or_review_quality_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,-8,-8,"Trailer/review quality is event attention, not Stage3 monetization proof.","Blocks false positive quality/trailer promotions.","R8L14_T03|R8L14_T05",2,2,2,medium,canonical_archetype_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "source_name": "FinanceData/marcap", "source_repo_url": "https://github.com/FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546, "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"], "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L14_C27_194480_COOKIE_RUN_KINGDOM_20210121", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L14_T01_194480_STAGE2_ACTIONABLE_COOKIE_RUN_KINGDOM_LAUNCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Launch evidence quickly converted into app-store/ranking monetization and durable global IP evidence; price response was structural rather than only trailer buzz."}
{"row_type": "case", "case_id": "R8L14_C27_095660_LIES_OF_P_RELEASE_20230919", "symbol": "095660", "company_name": "네오위즈", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "quality_evidence_without_durable_monetization_failed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A high-quality global package release was not enough; without visible live-service, repeat revenue, or scalable IP monetization bridge, the trigger had poor MFE/MAE."}
{"row_type": "case", "case_id": "R8L14_C27_263750_DOKEV_TRAILER_20210825", "symbol": "263750", "company_name": "펄어비스", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R8L14_T05_263750_STAGE2_TRAILER_BUZZ_DOKEV_GAMESCOM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_trailer_buzz_not_monetization", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Trailer/global attention produced tradable upside but lacked monetization conversion evidence; useful as a 4B/guardrail counterexample rather than a positive promotion sample."}
{"row_type": "trigger", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": 1056.52, "MFE_2Y_pct": 1056.52, "MAE_1Y_pct": -12.75, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R8L14_T01_194480_STAGE2_ACTIONABLE_COOKIE_RUN_KINGDOM_LAUNCH", "case_id": "R8L14_C27_194480_COOKIE_RUN_KINGDOM_20210121", "symbol": "194480", "company_name": "데브시스터즈", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-21", "entry_date": "2021-01-21", "entry_price": 17250, "evidence_available_at_that_date": "Cookie Run: Kingdom launch/global mobile RPG release; early ranking and download conversion evidence treated as Stage2-Actionable, not pure price.", "evidence_source": "Public game release information; stock-web 2021 tradable shard lines around 2021-01-21 and 2021-09/10 peak.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["repeat_order_or_conversion", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "MFE_30D_pct": 300.0, "MFE_90D_pct": 833.33, "MFE_180D_pct": 1056.52, "MAE_30D_pct": -12.75, "MAE_90D_pct": -12.75, "MAE_180D_pct": -12.75, "peak_date": "2021-09-27", "peak_price": 199500, "drawdown_after_peak_pct": -41.1, "trigger_outcome_label": "structural_success_with_extreme_MFE", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "194480_20210121_17250"}
{"row_type": "trigger", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": 7.26, "MFE_2Y_pct": 7.26, "MAE_1Y_pct": -55.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.925, "four_b_full_window_peak_proximity": 0.925, "four_b_timing_verdict": "good_local_peak_but_price_only_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "trigger_id": "R8L14_T02_194480_PRICE_ONLY_4B_LOCAL_PEAK", "case_id": "R8L14_C27_194480_COOKIE_RUN_KINGDOM_20210121", "symbol": "194480", "company_name": "데브시스터즈", "trigger_type": "4B-overlay", "trigger_date": "2021-09-27", "entry_date": "2021-09-27", "entry_price": 186000, "evidence_available_at_that_date": "Local price blowoff after global IP monetization run; this row is overlay-only and deliberately not treated as full 4B without non-price deterioration.", "evidence_source": "Stock-web 2021 tradable row around 2021-09-27; no independent non-price 4B evidence used.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "MFE_30D_pct": 7.26, "MFE_90D_pct": 7.26, "MFE_180D_pct": 7.26, "MAE_30D_pct": -40.86, "MAE_90D_pct": -40.86, "MAE_180D_pct": -50.0, "peak_date": "2021-09-27", "peak_price": 199500, "drawdown_after_peak_pct": -41.1, "trigger_outcome_label": "4B_overlay_success_price_only", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "194480_20210927_186000"}
{"row_type": "trigger", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": 3.04, "MFE_2Y_pct": 3.04, "MAE_1Y_pct": -44.64, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE", "case_id": "R8L14_C27_095660_LIES_OF_P_RELEASE_20230919", "symbol": "095660", "company_name": "네오위즈", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-09-19", "entry_date": "2023-09-19", "entry_price": 34500, "evidence_available_at_that_date": "Lies of P commercial release / global package-game quality event. Evidence was product-quality heavy, but repeat monetization and durable operating-leverage evidence were not visible at the trigger.", "evidence_source": "Public release information; stock-web 2023/2024 tradable shards around 2023-09-19 to 2024-06.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv|atlas/ohlcv_tradable_by_symbol_year/095/095660/2024.csv", "profile_path": "atlas/symbol_profiles/095/095660.json", "MFE_30D_pct": 3.04, "MFE_90D_pct": 3.04, "MFE_180D_pct": 3.04, "MAE_30D_pct": -32.32, "MAE_90D_pct": -32.32, "MAE_180D_pct": -44.64, "peak_date": "2023-09-19", "peak_price": 35550, "drawdown_after_peak_pct": -46.27, "trigger_outcome_label": "failed_rerating_quality_event_without_monetization_bridge", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "095660_20230919_34500"}
{"row_type": "trigger", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": 32.55, "MFE_2Y_pct": 32.55, "MAE_1Y_pct": -18.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "trigger_id": "R8L14_T04_095660_4C_THESIS_BREAK_WATCH", "case_id": "R8L14_C27_095660_LIES_OF_P_RELEASE_20230919", "symbol": "095660", "company_name": "네오위즈", "trigger_type": "4C-watch", "trigger_date": "2023-10-05", "entry_date": "2023-10-05", "entry_price": 23350, "evidence_available_at_that_date": "Post-release market repricing showed that quality-release evidence had not converted into durable IP monetization; this is thesis-break watch, not automatic hard 4C.", "evidence_source": "Stock-web 2023 row around 2023-10-05; no later evidence backfilled into initial Stage2 trigger.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv|atlas/ohlcv_tradable_by_symbol_year/095/095660/2024.csv", "profile_path": "atlas/symbol_profiles/095/095660.json", "MFE_30D_pct": 32.55, "MFE_90D_pct": 32.55, "MFE_180D_pct": 32.55, "MAE_30D_pct": -0.64, "MAE_90D_pct": -8.99, "MAE_180D_pct": -18.2, "peak_date": "2023-11-10", "peak_price": 30950, "drawdown_after_peak_pct": -38.29, "trigger_outcome_label": "4C_watch_useful_but_not_hard_failure_route", "current_profile_verdict": "current_profile_4C_too_late", "same_entry_group_id": "095660_20231005_23350"}
{"row_type": "trigger", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": 107.43, "MFE_2Y_pct": 107.43, "MAE_1Y_pct": -3.14, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R8L14_T05_263750_STAGE2_TRAILER_BUZZ_DOKEV_GAMESCOM", "case_id": "R8L14_C27_263750_DOKEV_TRAILER_20210825", "symbol": "263750", "company_name": "펄어비스", "trigger_type": "Stage2-trailer-buzz", "trigger_date": "2021-08-25", "entry_date": "2021-08-25", "entry_price": 70000, "evidence_available_at_that_date": "DokeV global trailer / Gamescom visibility event. This is public attention and content pipeline evidence, but not monetization conversion.", "evidence_source": "Public Gamescom/DokeV trailer information; stock-web 2021/2022 tradable shards around 2021-08-25 to 2022-04.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv|atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv", "profile_path": "atlas/symbol_profiles/263/263750.json", "MFE_30D_pct": 45.71, "MFE_90D_pct": 107.43, "MFE_180D_pct": 107.43, "MAE_30D_pct": -3.14, "MAE_90D_pct": -3.14, "MAE_180D_pct": -3.14, "peak_date": "2021-11-17", "peak_price": 145200, "drawdown_after_peak_pct": -30.03, "trigger_outcome_label": "price_moved_without_monetization_evidence", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "263750_20210825_70000"}
{"row_type": "trigger", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_CONVERSION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|residual_false_positive_mining|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": 2.98, "MFE_2Y_pct": 2.98, "MAE_1Y_pct": -35.67, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.944, "four_b_full_window_peak_proximity": 0.944, "four_b_timing_verdict": "good_local_peak_but_price_only_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "trigger_id": "R8L14_T06_263750_4B_PRICE_ONLY_OVERLAY", "case_id": "R8L14_C27_263750_DOKEV_TRAILER_20210825", "symbol": "263750", "company_name": "펄어비스", "trigger_type": "4B-overlay", "trigger_date": "2021-11-17", "entry_date": "2021-11-17", "entry_price": 141000, "evidence_available_at_that_date": "Post-trailer valuation/positioning blowoff without commercialization evidence; overlay-only row.", "evidence_source": "Stock-web 2021 tradable row around 2021-11-17 and 2022 forward window.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv|atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv", "profile_path": "atlas/symbol_profiles/263/263750.json", "MFE_30D_pct": 2.98, "MFE_90D_pct": 2.98, "MFE_180D_pct": 2.98, "MAE_30D_pct": -5.25, "MAE_90D_pct": -34.89, "MAE_180D_pct": -35.67, "peak_date": "2021-11-17", "peak_price": 145200, "drawdown_after_peak_pct": -35.67, "trigger_outcome_label": "4B_overlay_success_price_only", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "263750_20211117_141000"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L14_C27_194480_COOKIE_RUN_KINGDOM_20210121", "trigger_id": "R8L14_T01_194480_STAGE2_ACTIONABLE_COOKIE_RUN_KINGDOM_LAUNCH", "symbol": "194480", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 18, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 12, "relative_strength_score": 18, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88.0, "stage_label_after": "Stage3-Green", "changed_components": ["ip_monetization_conversion_bonus"], "component_delta_explanation": "Mobile IP launch converted into app-ranking/download/revenue quality, lifting C27 from Yellow to Green.", "MFE_90D_pct": 833.33, "MAE_90D_pct": -12.75, "score_return_alignment_label": "structural_success_with_extreme_MFE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L14_C27_095660_LIES_OF_P_RELEASE_20230919", "trigger_id": "R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE", "symbol": "095660", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 22, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 4, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 67.0, "stage_label_after": "Stage2-Watch", "changed_components": ["monetization_bridge_guard"], "component_delta_explanation": "High game quality is not enough for C27 if durable monetization route is not visible.", "MFE_90D_pct": 3.04, "MAE_90D_pct": -32.32, "score_return_alignment_label": "failed_rerating_quality_event_without_monetization_bridge", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L14_C27_263750_DOKEV_TRAILER_20210825", "trigger_id": "R8L14_T05_263750_STAGE2_TRAILER_BUZZ_DOKEV_GAMESCOM", "symbol": "263750", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 59.0, "stage_label_after": "Stage2-Watch", "changed_components": ["trailer_buzz_not_monetization_guard"], "component_delta_explanation": "Trailer/global attention can move price but should not promote to Stage3 without launch/revenue conversion.", "MFE_90D_pct": 107.43, "MAE_90D_pct": -3.14, "score_return_alignment_label": "price_moved_without_monetization_evidence", "current_profile_verdict": "current_profile_correct"}
{"row_type": "shadow_weight", "axis": "C27_ip_monetization_conversion_bonus", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "baseline_value": 0, "tested_value": 4, "delta": "+4", "reason": "C27 should reward evidence that content IP attention has converted into durable monetization, not merely trailer/review quality.", "backtest_effect": "Keeps 194480 positive while demoting 095660/263750 buzz-only or quality-only rows.", "trigger_ids": "R8L14_T01_194480_STAGE2_ACTIONABLE_COOKIE_RUN_KINGDOM_LAUNCH|R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE|R8L14_T05_263750_STAGE2_TRAILER_BUZZ_DOKEV_GAMESCOM", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "shadow_weight", "axis": "C27_trailer_or_review_quality_guard", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "baseline_value": 0, "tested_value": -8, "delta": "-8", "reason": "Trailer/review/product-quality events are event attention, not Stage3 monetization proof.", "backtest_effect": "Blocks false promotion in Neowiz and Pearl Abyss while preserving Devsisters because Devsisters has conversion evidence.", "trigger_ids": "R8L14_T03_095660_STAGE2_ACTIONABLE_LIES_OF_P_RELEASE|R8L14_T05_263750_STAGE2_TRAILER_BUZZ_DOKEV_GAMESCOM", "calibration_usable_count": 2, "new_independent_case_count": 2, "counterexample_count": 2, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "residual_contribution", "round": "R8", "loop": "14", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "scheduled_round": "R8", "scheduled_loop": "14", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 1, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage3_green_revision_min"], "residual_error_types_found": ["quality_release_without_monetization_false_positive", "trailer_buzz_price_move_without_revenue", "price_only_4B_overlay_not_full_exit"], "diversity_score_summary": "new_symbol_count=3; new_trigger_family_count=4; positive=1; counterexample=2; current_profile_error=1", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R8
completed_loop = 14
next_round = R9
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web repository observations used in this MD:

- `atlas/manifest.json`: manifest `max_date=2026-02-20`, `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.
- `atlas/symbol_profiles/194/194480.json`: Devsisters profile, no corporate-action candidate dates in inspected profile.
- `atlas/symbol_profiles/095/095660.json`: Neowiz profile, corporate-action candidates are historical and outside the 2023/2024 calibration window.
- `atlas/symbol_profiles/263/263750.json`: Pearl Abyss profile, one corporate-action candidate on 2021-04-16, outside the DokeV trigger window.
- `atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv`: Devsisters entry, run-up, and 2021-09/10 peak rows.
- `atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv` and `2024.csv`: Neowiz entry and post-release drawdown rows.
- `atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv` and `2022.csv`: Pearl Abyss DokeV trailer run-up and subsequent overlay window.

Public event references used only to anchor historical trigger dates:

- Cookie Run: Kingdom public release date in January 2021.
- Lies of P public release date in September 2023.
- DokeV Gamescom Opening Night Live gameplay trailer world premiere in August 2021.

No current/live stock recommendation, no live scan, and no production score patch is included.

