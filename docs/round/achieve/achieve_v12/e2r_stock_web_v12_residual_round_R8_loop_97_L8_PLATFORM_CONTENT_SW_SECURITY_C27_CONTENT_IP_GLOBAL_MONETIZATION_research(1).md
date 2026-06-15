# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | IP_global_monetization_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. After local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19 supplementation, C27 is the next unsupplemented Priority 0 archetype. Previous C27 symbols from loops 90/93/96 and top-covered C27 names are avoided.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
IP_global_monetization_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 97
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C27 is a content/IP monetization archetype. The IP title is the poster on the wall; the investable signal is whether release/tour cadence, fandom demand, platform distribution, repeat monetization, margin and revision all convert into cash.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION = 24 rows / Priority 0
previous C27 loop symbols avoided: 419530, 408900, 417180, 194480, 035760, 160550, 432430, 048910, 289220
top-covered C27 names avoided where possible: 035760, 251270, 035900, 194480, 419530, 036420
recent local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C27 trigger families:

```text
041510 / Stage2-Actionable / 2024-02-07
352820 / Stage2-Actionable / 2024-03-27
299900 / Stage4B / 2024-03-13
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
| 041510 | atlas/symbol_profiles/041/041510.json | selected 2024 window clean after old 2002/2005 CA candidates |
| 352820 | atlas/symbol_profiles/352/352820.json | no corporate-action candidate |
| 299900 | atlas/symbol_profiles/299/299900.json | selected 2024 window clean after old 2020/2023 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L97_C27_SM_2024_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_POSITIVE | 041510 | 2024-02-07 | yes | 180 | yes | yes | true |
| R8L97_C27_HYBE_2024_LABEL_PLATFORM_IP_RISK_FALSE_STAGE2 | 352820 | 2024-03-27 | yes | 180 | yes | yes | true |
| R8L97_C27_WYSIWYG_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B | 299900 | 2024-03-13 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C27_CONTENT_IP_GLOBAL_MONETIZATION | ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE | Positive Stage2 requires release/tour pipeline, global fandom monetization, platform/distribution economics, margin and revision bridge. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | LABEL_PLATFORM_RISK_FALSE_STAGE2 | Label/platform IP watch without release breadth, governance/risk control and margin bridge can become false Stage2. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | VIRTUAL_PRODUCTION_EVENT_CAP_4B | Virtual production / AI-content premium should route to 4B when backlog, ownership and monetization bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L97_C27_SM_2024_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_POSITIVE | 041510 | 에스엠 | positive | Artist IP/global tour/fandom monetization bridge produced strong 90D MFE with shallow early MAE. |
| R8L97_C27_HYBE_2024_LABEL_PLATFORM_IP_RISK_FALSE_STAGE2 | 352820 | 하이브 | counterexample | Label/platform IP rebound watch had limited MFE and then persistent MAE as risk overwhelmed the monetization label. |
| R8L97_C27_WYSIWYG_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B | 299900 | 위지윅스튜디오 | counterexample / 4B | Virtual-production/AI-content event premium capped in the March spike and then de-rated sharply. |

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
| SM artist IP global tour/fandom bridge | historical public/report proxy | true | true | shadow-only positive |
| HYBE label/platform IP risk false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| WYSIWYG virtual production AI-content event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 041510 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2024.csv | atlas/symbol_profiles/041/041510.json |
| 352820 | atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv | atlas/symbol_profiles/352/352820.json |
| 299900 | atlas/ohlcv_tradable_by_symbol_year/299/299900/2024.csv | atlas/symbol_profiles/299/299900.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L97_C27_SM_2024_STAGE2_ACTIONABLE_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE | 041510 | Stage2-Actionable | 2024-02-07 | 73200 | positive | artist IP/global monetization bridge worked |
| R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH | 352820 | Stage2-Actionable | 2024-03-27 | 224000 | counterexample | label/platform IP false Stage2 |
| R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP | 299900 | Stage4B | 2024-03-13 | 2820 | counterexample/4B | virtual production AI-content event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L97_C27_SM_2024_STAGE2_ACTIONABLE_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE | 73200 | 12.84 | -4.37 | 37.57 | -4.37 | 37.57 | -23.09 | 2024-05-27 | 100700 | -44.09 |
| R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH | 224000 | 6.47 | -10.80 | 6.47 | -20.22 | 6.47 | -28.66 | 2024-04-22 | 238500 | -33.88 |
| R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP | 2820 | 20.57 | -20.04 | 20.57 | -41.67 | 20.57 | -41.67 | 2024-03-13 | 3400 | -51.62 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C27 Stage2 needs IP release/tour pipeline / global fandom monetization / platform distribution / margin / revision bridge |
| IP_global_monetization_guardrail | strengthen: content/IP label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing label/platform and virtual-production premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C27 rows cannot promote without durable monetization/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether content/IP narrative becomes repeatable monetization and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 041510 | good_stage2_with_later_watch | Global artist IP monetization bridge produced strong MFE, but later valuation/label-risk watch remains necessary. |
| 352820 | bad_stage2 | Label/platform IP watch lacked risk-control and margin bridge, producing limited MFE and persistent MAE. |
| 299900 | good_4B | Virtual production / AI-content premium peaked immediately and later de-rated deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 352820 label/platform IP false Stage2 | 0.94 | 0.94 | false Stage2 due missing release-pipeline / governance / margin bridge |
| 299900 virtual production cap | 0.83 | 0.83 | good full-window 4B timing after AI-content event premium |
| 041510 artist IP bridge | n/a | n/a | positive Stage2, but later artist-IP valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 352820 / 299900
```

No hard 4C candidate is introduced in this C27 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 content/IP global monetization cases, Stage2 requires verified release or tour pipeline, global fandom demand, platform/distribution economics, repeat monetization, margin and revision bridge. Content, IP, artist, label, virtual production, AI content or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
rule = C27 should split true global IP monetization/margin positives from label-platform risk false Stage2 and virtual-production event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 21.54 | -22.09 | 0.67 | mixed; C27 monetization bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 21.54 | -22.09 | 0.67 | weaker C27 bridge split |
| P1 sector_specific_candidate_profile | L8 IP monetization/margin bridge required | 2 | 22.02 | -12.30 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C27 bridge vs event-cap split | 2 | 22.02 | -12.30 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing content/IP themes as positive | 1 | 37.57 | -4.37 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 041510 artist IP bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 37.57 | -4.37 | content_IP_global_monetization_positive |
| 352820 label/platform false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 6.47 | -20.22 | label_platform_IP_false_stage2 |
| 299900 virtual production cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 20.57 | -41.67 | virtual_production_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C27 is the next unsupplemented Priority 0 archetype after local C08/C09/C01/C07/C06/C10/C14/C11/C02/C13/C19 supplementation. This run adds SM, HYBE, and WYSIWYG Studio while avoiding prior C27 symbols 419530, 408900, 417180, 194480, 035760, 160550, 432430, 048910, 289220 and top-covered C27 names."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, IP_global_monetization_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: content_IP_global_monetization_positive, label_platform_IP_false_stage2, virtual_production_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, IP_global_monetization_guardrail, high_MAE_guardrail
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
- C27 content/IP global monetization bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,C27_requires_global_IP_release_tour_fandom_platform_margin_revision_bridge,0,"C27 Stage2 should require global IP monetization, release/tour pipeline, fandom demand, platform/distribution economics, margin, and revision bridge, not content/IP label alone","SM positive worked; HYBE and WYSIWYG event/watch rows failed positive-stage promotion","R8L97_C27_SM_2024_STAGE2_ACTIONABLE_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE|R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH|R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,cap_bridge_missing_label_platform_and_virtual_production_event_premiums_as_4B_watch,0,"Label/platform and virtual-production content premiums can peak before release pipeline, IP ownership, repeat monetization and margin bridge is proven","HYBE had limited MFE and persistent MAE after March rebound; WYSIWYG showed 4B event-cap behavior after March AI-content spike","R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH|R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,block_positive_stage_when_content_IP_theme_has_high_or_persistent_MAE_without_monetization_margin_bridge,0,"High or persistent MAE after bridge-missing C27 entries should block Stage2/Stage3 promotion unless release pipeline, IP monetization and margin evidence survives","HYBE MAE180=-28.66 and WYSIWYG MAE90=-41.67","R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH|R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L97_C27_SM_2024_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_POSITIVE", "symbol": "041510", "company_name": "에스엠", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP", "case_type": "structural_success_with_later_artist_IP_valuation_and_label_risk_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L97_C27_SM_2024_STAGE2_ACTIONABLE_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Artist IP / global tour / fandom monetization bridge produced strong 90D MFE from the February trough with shallow early MAE. C27 works when IP optionality is tied to global monetization, release/tour schedule, fandom demand, platform/distribution take rate, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C27_positive_requires_global_IP_release_tour_fandom_monetization_margin_revision_bridge_not_content_IP_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2002/2005 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R8L97_C27_HYBE_2024_LABEL_PLATFORM_IP_RISK_FALSE_STAGE2", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP", "case_type": "failed_rerating_label_platform_IP_monetization_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Label/platform IP rebound watch after the March rally had limited forward MFE and then persistent MAE as label governance and IP concentration risk overwhelmed the monetization label. C27 Stage2 should not be awarded without release pipeline, artist/IP concentration control, platform monetization, margin, governance and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_label_platform_IP_watch_counts_without_release_pipeline_governance_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R8L97_C27_WYSIWYG_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B", "symbol": "299900", "company_name": "위지윅스튜디오", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Virtual-production / AI-content event premium capped in the March spike and then de-rated sharply. C27 should route bridge-missing content-tech premiums to 4B unless production backlog, IP ownership, platform distribution, repeat monetization, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2020/2023 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L97_C27_SM_2024_STAGE2_ACTIONABLE_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE", "case_id": "R8L97_C27_SM_2024_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_POSITIVE", "symbol": "041510", "company_name": "에스엠", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP", "sector": "artist_IP_global_tour_fandom_monetization", "primary_archetype": "global_IP_release_tour_fandom_monetization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | IP_global_monetization_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 73200.0, "evidence_available_at_that_date": "artist IP / global tour and fandom monetization bridge proxy after February trough; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["artist_IP_proxy", "global_tour_release_pipeline_proxy", "fandom_monetization_proxy", "platform_distribution_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "strong_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_artist_IP_valuation_watch", "label_risk_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2024.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.84, "MFE_90D_pct": 37.57, "MFE_180D_pct": 37.57, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.37, "MAE_90D_pct": -4.37, "MAE_180D_pct": -23.09, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-27", "peak_price": 100700.0, "drawdown_after_peak_pct": -44.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_artist_IP_valuation_and_label_risk_4B_watch_needed", "four_b_evidence_type": ["artist_IP_monetization_bridge", "global_tour_fandom", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_artist_IP_global_monetization_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2002_2005_CA", "same_entry_group_id": "R8L97_C27_041510_2024-02-07_73200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH", "case_id": "R8L97_C27_HYBE_2024_LABEL_PLATFORM_IP_RISK_FALSE_STAGE2", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP", "sector": "label_platform_artist_IP_governance_risk", "primary_archetype": "label_platform_watch_without_release_pipeline_governance_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | IP_global_monetization_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "entry_date": "2024-03-27", "entry_price": 224000.0, "evidence_available_at_that_date": "label/platform IP recovery watch after March rebound without confirmed release-pipeline breadth, artist/IP concentration control, governance risk containment, platform monetization or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["label_platform_IP_watch", "global_fandom_theme", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "high_MAE90", "release_pipeline_governance_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv", "profile_path": "atlas/symbol_profiles/352/352820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.47, "MFE_90D_pct": 6.47, "MFE_180D_pct": 6.47, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.8, "MAE_90D_pct": -20.22, "MAE_180D_pct": -28.66, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-22", "peak_price": 238500.0, "drawdown_after_peak_pct": -33.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "label_platform_IP_watch_was_false_stage2_due_missing_release_pipeline_governance_margin_revision_bridge", "four_b_evidence_type": ["label_platform_IP_premium", "bridge_missing", "governance_concentration_risk"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_label_platform_IP_watch_without_governance_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_label_platform_IP_watch_counts_without_release_pipeline_governance_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R8L97_C27_352820_2024-03-27_224000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "case_id": "R8L97_C27_WYSIWYG_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B", "symbol": "299900", "company_name": "위지윅스튜디오", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP", "sector": "virtual_production_AI_content_event_premium", "primary_archetype": "virtual_production_AI_content_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | IP_global_monetization_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-13", "entry_date": "2024-03-13", "entry_price": 2820.0, "evidence_available_at_that_date": "virtual-production / AI-content event premium without confirmed production backlog, IP ownership, platform distribution, repeat monetization, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["virtual_production_AI_content_event", "content_tech_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "production_backlog_monetization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/299/299900/2024.csv", "profile_path": "atlas/symbol_profiles/299/299900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.57, "MFE_90D_pct": 20.57, "MFE_180D_pct": 20.57, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.04, "MAE_90D_pct": -41.67, "MAE_180D_pct": -41.67, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 3400.0, "drawdown_after_peak_pct": -51.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.83, "four_b_full_window_peak_proximity": 0.83, "four_b_timing_verdict": "good_full_window_4B_timing_virtual_production_AI_content_event_cap_due_missing_backlog_monetization_margin_bridge", "four_b_evidence_type": ["virtual_production_AI_content_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_virtual_production_AI_content_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2020_2023_CA", "same_entry_group_id": "R8L97_C27_299900_2024-03-13_2820", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R8L97_C27_SM_2024_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_POSITIVE", "trigger_id": "R8L97_C27_SM_2024_STAGE2_ACTIONABLE_ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE", "symbol": "041510", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 55, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "artist_IP_global_tour_fandom_monetization_positive", "MFE_90D_pct": 37.57, "MAE_90D_pct": -4.37, "score_return_alignment_label": "content_IP_global_monetization_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R8L97_C27_HYBE_2024_LABEL_PLATFORM_IP_RISK_FALSE_STAGE2", "trigger_id": "R8L97_C27_HYBE_2024_STAGE2_FALSE_POSITIVE_LABEL_PLATFORM_IP_RISK_WATCH", "symbol": "352820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 65, "customer_quality_score": 50, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 15}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "label_platform_IP_governance_false_stage2", "MFE_90D_pct": 6.47, "MAE_90D_pct": -20.22, "score_return_alignment_label": "label_platform_IP_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_label_platform_IP_watch_counts_without_release_pipeline_governance_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R8L97_C27_WYSIWYG_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B", "trigger_id": "R8L97_C27_WYSIWYG_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "symbol": "299900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 65, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "virtual_production_AI_content_event_cap_4B_guard", "MFE_90D_pct": 20.57, "MAE_90D_pct": -41.67, "score_return_alignment_label": "virtual_production_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "97", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ARTIST_IP_GLOBAL_TOUR_FANDOM_MONETIZATION_BRIDGE_VS_LABEL_PLATFORM_RISK_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "IP_global_monetization_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["content_IP_global_monetization_positive", "label_platform_IP_false_stage2", "virtual_production_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- C27 rows need explicit release/tour pipeline, global fandom demand, platform/distribution economics, repeat monetization, margin and revision bridge before positive promotion.
- In C27, bridge-missing content/IP event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C27 content/IP global monetization rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R8
completed_loop = 97
completed_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 0 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
