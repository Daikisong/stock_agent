# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_93_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
```

This file is the corrected final output for this execution. The scheduler state after R7 loop 93 is R8 / loop 93. R8 is the L8 platform/content/software/security round, and this run fills C27 content-IP global monetization after R8 loop 92 used C26, loop 91 used C28, and loop 90 used C27 with different symbols.

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
scheduled_round = R8
scheduled_loop = 93
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
round_sector_consistency = pass
computed_next_round = R9
computed_next_loop = 93
```

C27 is a crowded content/IP archetype, so this loop avoids the top repeated names and tests whether global/live-ops monetization bridge can be separated from content-platform and film-studio event premiums.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION = 39 rows / 15 symbols / good-bad Stage2 20-6 / 4B-4C 3-1
top covered symbols include 263750(5), 112040(4), 122870(4), 293490(4), 259960(3), 376300(3)
previous R8 loop-89 C26 symbols avoided: 067160, 216050, 273060
previous R8 loop-90 C27 symbols avoided: 419530, 408900, 417180
previous R8 loop-91 C28 symbols avoided: 170790, 136540, 356890
previous R8 loop-92 C26 symbols avoided: 042000, 089600, 123570
previous R7 loop-93 C24 symbols avoided: 039200, 950220, 174900
```

Selected rows avoid hard duplicates and top repeated C27 symbols:

```text
194480 / Stage2-Actionable / 2024-02-07
035760 / Stage2-Actionable / 2024-02-08
160550 / Stage4B / 2024-02-26
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
| 194480 | atlas/symbol_profiles/194/194480.json | no corporate-action candidate |
| 035760 | atlas/symbol_profiles/035/035760.json | selected 2024 window clean after old 2006/2010/2018 CA candidates |
| 160550 | atlas/symbol_profiles/160/160550.json | selected 2024 window clean after old 2015 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L93_C27_DEVSISTERS_2024_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_POSITIVE | 194480 | 2024-02-07 | yes | 180 | yes | yes | true |
| R8L93_C27_CJENM_2024_CONTENT_PLATFORM_TV_COMMERCE_FALSE_STAGE2 | 035760 | 2024-02-08 | yes | 180 | yes | yes | true |
| R8L93_C27_NEW_2024_FILM_STUDIO_CONTENT_EVENT_CAP_4B | 160550 | 2024-02-26 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C27_CONTENT_IP_GLOBAL_MONETIZATION | GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE | Positive Stage2 requires global launch/distribution, live-ops engagement, IP monetization, ARPU, margin and revision bridge. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | CONTENT_PLATFORM_FALSE_STAGE2 | Content/platform value-up label without IP export/royalty and margin bridge can become false Stage2. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | FILM_STUDIO_EVENT_CAP_4B | Film/studio content event premium should route to 4B when box-office/OTT monetization and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L93_C27_DEVSISTERS_2024_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_POSITIVE | 194480 | 데브시스터즈 | positive | Game IP global/live-ops monetization bridge produced high MFE with controlled initial MAE. |
| R8L93_C27_CJENM_2024_CONTENT_PLATFORM_TV_COMMERCE_FALSE_STAGE2 | 035760 | CJ ENM | counterexample | Content/platform value-up watch had capped MFE and later drawdown. |
| R8L93_C27_NEW_2024_FILM_STUDIO_CONTENT_EVENT_CAP_4B | 160550 | NEW | counterexample / 4B | Film/studio content premium capped on the February spike and then de-rated severely. |

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
| Devsisters game IP global/live-ops bridge | historical public/report proxy | true | true | shadow-only positive |
| CJ ENM content platform false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| NEW film/studio content event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 194480 | atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv | atlas/symbol_profiles/194/194480.json |
| 035760 | atlas/ohlcv_tradable_by_symbol_year/035/035760/2024.csv | atlas/symbol_profiles/035/035760.json |
| 160550 | atlas/ohlcv_tradable_by_symbol_year/160/160550/2024.csv | atlas/symbol_profiles/160/160550.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L93_C27_DEVSISTERS_2024_STAGE2_ACTIONABLE_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION | 194480 | Stage2-Actionable | 2024-02-07 | 37200 | positive | game IP global/live-ops monetization bridge worked |
| R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH | 035760 | Stage2-Actionable | 2024-02-08 | 86200 | counterexample | content platform value-up false Stage2 |
| R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP | 160550 | Stage4B | 2024-02-26 | 4010 | counterexample/4B | film/studio content event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L93_C27_DEVSISTERS_2024_STAGE2_ACTIONABLE_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION | 37200 | 34.95 | -2.55 | 64.52 | -2.55 | 105.11 | -4.30 | 2024-06-26 | 76300 | -47.77 |
| R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH | 86200 | 3.60 | -16.24 | 3.60 | -18.79 | 3.60 | -28.42 | 2024-02-08 | 89300 | -30.91 |
| R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP | 4010 | 13.97 | -24.69 | 13.97 | -32.67 | 13.97 | -47.51 | 2024-02-26 | 4570 | -53.94 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C27 Stage2 needs global distribution / IP monetization / live-ops or slate economics / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing content/IP event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE content/IP rows cannot promote without durable monetization bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is content-IP monetization bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 194480 | good_stage2_with_later_watch | Game IP/live-ops bridge produced high 90D/180D MFE, but later valuation watch remains needed. |
| 035760 | bad_stage2 | Content-platform value-up watch lacked IP export/royalty/margin bridge and had capped MFE. |
| 160550 | good_4B | Film/studio event premium capped on the February spike and later had large MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 035760 content-platform false Stage2 | 0.97 | 0.97 | false Stage2 due missing IP export/royalty/margin bridge |
| 160550 film/studio event cap | 0.88 | 0.88 | good full-window 4B timing after high-MAE confirmation |
| 194480 game IP monetization bridge | n/a | n/a | positive Stage2, but later content-IP valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 035760 / 160550
```

No hard 4C candidate is proposed. R8 loop 93 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 content/IP global monetization cases, Stage2 requires verified global launch/distribution, live-ops engagement, IP export/royalty conversion, box-office/OTT monetization, platform traffic, margin, or revision bridge. Content, IP, film, platform, game, webtoon, TV-commerce or value-up label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
rule = C27 should split true global/live-ops/IP-monetization positives from content-platform false Stage2 and film/studio event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 27.36 | -18.00 | 0.67 | mixed; C27 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 27.36 | -18.00 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L8 global/IP monetization bridge required | 2 | 34.06 | -10.67 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C27 bridge vs event-cap split | 2 | 34.06 | -10.67 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing content/IP themes as positive | 1 | 64.52 | -2.55 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 194480 game IP monetization bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 64.52 | -2.55 | game_IP_global_liveops_monetization_positive |
| 035760 content platform false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 3.60 | -18.79 | content_platform_valueup_false_stage2 |
| 160550 film/studio cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 13.97 | -32.67 | film_studio_content_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C27 game-IP global/live-ops monetization positive, content-platform value-up false Stage2, and film-studio content event-cap 4B split while avoiding top repeated C27 symbols."}
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
residual_error_types_found: game_IP_global_liveops_monetization_positive, content_platform_valueup_false_stage2, film_studio_content_event_cap_4B
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
- C27 content-IP global monetization bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,C27_requires_global_IP_monetization_distribution_margin_revision_bridge,0,"C27 Stage2 should require global launch/distribution, live-ops or slate monetization, IP export/royalty conversion, platform traffic, margin, or revision bridge, not content/IP headline alone","Devsisters positive worked; CJ ENM and NEW event/watch rows failed positive-stage promotion","R8L93_C27_DEVSISTERS_2024_STAGE2_ACTIONABLE_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION|R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH|R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,cap_bridge_missing_content_platform_and_film_studio_event_premiums_as_4B_watch,0,"Content/IP event premiums can peak before IP export, royalty, box-office, OTT or live-ops margin bridge is proven","CJ ENM had capped MFE after value-up spike; NEW showed 4B event-cap behavior after February content spike","R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH|R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,block_positive_stage_when_content_IP_theme_has_high_MAE_without_monetization_bridge,0,"High or persistent MAE after bridge-missing content/IP entries should block Stage2/Stage3 promotion unless monetization, distribution and margin evidence survives","CJ ENM MAE180=-28.42 and NEW MAE180=-47.51","R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH|R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L93_C27_DEVSISTERS_2024_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_POSITIVE", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "93", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP", "case_type": "structural_success_with_later_content_IP_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L93_C27_DEVSISTERS_2024_STAGE2_ACTIONABLE_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Game IP global/live-ops monetization bridge produced high 30D/90D and very high 180D MFE with controlled initial MAE. C27 works when content/IP narrative maps into live service KPIs, global launch cadence, monetization ARPU, platform distribution, cost discipline and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C27_positive_requires_global_liveops_monetization_distribution_revision_bridge_not_IP_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R8L93_C27_CJENM_2024_CONTENT_PLATFORM_TV_COMMERCE_FALSE_STAGE2", "symbol": "035760", "company_name": "CJ ENM", "round": "R8", "loop": "93", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP", "case_type": "failed_rerating_content_platform_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Content/platform value-up and TV-commerce recovery watch had capped forward MFE and then persistent drawdown. C27 Stage2 should not be awarded without content slate profitability, IP export/royalty evidence, platform subscriber/traffic conversion, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_content_platform_valueup_counts_without_IP_export_royalty_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2006/2010/2018 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R8L93_C27_NEW_2024_FILM_STUDIO_CONTENT_EVENT_CAP_4B", "symbol": "160550", "company_name": "NEW", "round": "R8", "loop": "93", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Film/studio content event premium capped on the February spike and then suffered large 90D/180D MAE. C27 should route bridge-missing film/content event premiums to 4B unless box-office/OTT monetization, overseas rights, library value, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_film_studio_content_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2015 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L93_C27_DEVSISTERS_2024_STAGE2_ACTIONABLE_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION", "case_id": "R8L93_C27_DEVSISTERS_2024_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_POSITIVE", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "93", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP", "sector": "game_IP_global_liveops_monetization", "primary_archetype": "game_IP_global_launch_liveops_ARPU_distribution_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 37200.0, "evidence_available_at_that_date": "game IP relaunch/global launch cadence, live-ops engagement, monetization ARPU, platform distribution and cost/margin revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["global_launch_cadence_proxy", "liveops_engagement_proxy", "monetization_ARPU_proxy", "platform_distribution_bridge", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["high_MFE30", "high_MFE90", "very_high_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_content_IP_valuation_watch", "post_peak_drawdown_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.95, "MFE_90D_pct": 64.52, "MFE_180D_pct": 105.11, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.55, "MAE_90D_pct": -2.55, "MAE_180D_pct": -4.3, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 76300.0, "drawdown_after_peak_pct": -47.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_content_IP_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "game_IP_monetization_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_game_IP_global_liveops_monetization_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R8L93_C27_194480_2024-02-07_37200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH", "case_id": "R8L93_C27_CJENM_2024_CONTENT_PLATFORM_TV_COMMERCE_FALSE_STAGE2", "symbol": "035760", "company_name": "CJ ENM", "round": "R8", "loop": "93", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP", "sector": "content_platform_TV_commerce_valueup_watch", "primary_archetype": "content_platform_watch_without_IP_export_royalty_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-08", "entry_date": "2024-02-08", "entry_price": 86200.0, "evidence_available_at_that_date": "content platform / TV-commerce recovery and value-up watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["content_platform_recovery_watch", "TV_commerce_valueup_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capped_MFE90", "IP_export_royalty_margin_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035760/2024.csv", "profile_path": "atlas/symbol_profiles/035/035760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.6, "MFE_90D_pct": 3.6, "MFE_180D_pct": 3.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.24, "MAE_90D_pct": -18.79, "MAE_180D_pct": -28.42, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-08", "peak_price": 89300.0, "drawdown_after_peak_pct": -30.91, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "content_platform_valueup_watch_was_false_stage2_due_missing_IP_export_royalty_margin_bridge", "four_b_evidence_type": ["content_platform_valueup_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_content_platform_watch_without_IP_export_royalty_bridge", "current_profile_verdict": "current_profile_false_positive_if_content_platform_valueup_counts_without_IP_export_royalty_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2006_2010_2018_CA", "same_entry_group_id": "R8L93_C27_035760_2024-02-08_86200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP", "case_id": "R8L93_C27_NEW_2024_FILM_STUDIO_CONTENT_EVENT_CAP_4B", "symbol": "160550", "company_name": "NEW", "round": "R8", "loop": "93", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP", "sector": "film_studio_content_event_premium", "primary_archetype": "film_studio_content_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 4010.0, "evidence_available_at_that_date": "film/studio content event premium after February content spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["film_studio_content_event", "boxoffice_OTT_monetization_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "boxoffice_OTT_royalty_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/160/160550/2024.csv", "profile_path": "atlas/symbol_profiles/160/160550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.97, "MFE_90D_pct": 13.97, "MFE_180D_pct": 13.97, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -24.69, "MAE_90D_pct": -32.67, "MAE_180D_pct": -47.51, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 4570.0, "drawdown_after_peak_pct": -53.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing_film_studio_content_event_cap_after_high_MAE_confirmation", "four_b_evidence_type": ["film_content_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_film_studio_content_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_film_studio_content_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2015_CA", "same_entry_group_id": "R8L93_C27_160550_2024-02-26_4010", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L93_C27_DEVSISTERS_2024_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_POSITIVE", "trigger_id": "R8L93_C27_DEVSISTERS_2024_STAGE2_ACTIONABLE_GAME_IP_GLOBAL_LIVEOPS_MONETIZATION", "symbol": "194480", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 55, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 50, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "game_IP_global_liveops_monetization_positive", "MFE_90D_pct": 64.52, "MAE_90D_pct": -2.55, "score_return_alignment_label": "game_IP_global_liveops_monetization_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L93_C27_CJENM_2024_CONTENT_PLATFORM_TV_COMMERCE_FALSE_STAGE2", "trigger_id": "R8L93_C27_CJENM_2024_STAGE2_FALSE_POSITIVE_CONTENT_PLATFORM_VALUEUP_WATCH", "symbol": "035760", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "content_platform_valueup_false_stage2", "MFE_90D_pct": 3.6, "MAE_90D_pct": -18.79, "score_return_alignment_label": "content_platform_valueup_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_content_platform_valueup_counts_without_IP_export_royalty_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L93_C27_NEW_2024_FILM_STUDIO_CONTENT_EVENT_CAP_4B", "trigger_id": "R8L93_C27_NEW_2024_STAGE4B_FILM_STUDIO_CONTENT_EVENT_CAP", "symbol": "160550", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "film_studio_content_event_cap_4B_guard", "MFE_90D_pct": 13.97, "MAE_90D_pct": -32.67, "score_return_alignment_label": "film_studio_content_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_film_studio_content_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "93", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_BRIDGE_VS_CONTENT_PLATFORM_FALSE_STAGE2_AND_FILM_STUDIO_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["game_IP_global_liveops_monetization_positive", "content_platform_valueup_false_stage2", "film_studio_content_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Content/IP rows need global distribution, IP monetization, traffic, margin, or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C27 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 93
next_round = R9
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
