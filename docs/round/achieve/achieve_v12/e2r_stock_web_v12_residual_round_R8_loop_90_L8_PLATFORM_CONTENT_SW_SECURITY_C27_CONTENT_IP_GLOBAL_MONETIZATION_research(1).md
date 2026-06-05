# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_90_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
```

This loop continues loop 90 after R7. It adds 3 C27 content/IP global-monetization cases: one kids animation IP merchandising positive, one outsourced-animation false Stage2, and one webtoon/platform 4B event-cap counterexample.

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
scheduled_round = R8
scheduled_loop = 90
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
round_sector_consistency = pass
computed_next_round = R9
computed_next_loop = 90
```

R8 permits L8 platform/content/software/security research. Previous R8 loop 88 used C28, and R8 loop 89 used C26, so this loop fills C27 and tests whether content/IP narratives convert into owned-IP monetization, merchandise sell-through, licensing, overseas distribution, paid traffic, margin, or revision bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION = 39 rows / 15 symbols / good-bad Stage2 20-6 / 4B-4C 3-1
top covered symbols include 263750(5), 112040(4), 122870(4), 293490(4), 259960(3), 376300(3)
previous R8 loop-88 C28 symbols avoided: 030520, 053800, 263800
previous R8 loop-89 C26 symbols avoided: 067160, 216050, 273060
```

Selected rows avoid those repeated combinations and the top repeated C27 symbols:

```text
419530 / Stage2-Actionable / 2024-07-12
408900 / Stage2-Actionable / 2024-06-26
417180 / Stage4B / 2024-01-24
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
| 419530 | atlas/symbol_profiles/419/419530.json | no corporate-action candidate |
| 408900 | atlas/symbol_profiles/408/408900.json | selected 2024-06-26 post-2024-04-26 CA window |
| 417180 | atlas/symbol_profiles/417/417180.json | selected 2024 window clean after 2023-12-05 CA |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L90_C27_SAMG_2024_KIDS_IP_MERCH_GLOBAL_MONETIZATION_POSITIVE | 419530 | 2024-07-12 | yes | 180 | yes | yes | true |
| R8L90_C27_STUDIOMIR_2024_OUTSOURCE_ANIMATION_FALSE_STAGE2 | 408900 | 2024-06-26 | yes | 180 | yes | post-CA | true |
| R8L90_C27_FINGERSTORY_2024_WEBTOON_PLATFORM_THEME_EVENT_CAP_4B | 417180 | 2024-01-24 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C27_CONTENT_IP_GLOBAL_MONETIZATION | KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION | Positive Stage2 requires owned-IP, merchandise sell-through, licensing, overseas distribution, margin, and revision bridge. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | OUTSOURCE_ANIMATION_FALSE_STAGE2 | Content production/outsource label without owned-IP or recurring monetization can become false Stage2. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | WEBTOON_PLATFORM_THEME_EVENT_CAP_4B | Webtoon/IP platform premium should route to 4B when paid traffic/licensing/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L90_C27_SAMG_2024_KIDS_IP_MERCH_GLOBAL_MONETIZATION_POSITIVE | 419530 | SAMG엔터 | positive | Kids animation IP / merchandise monetization path produced very high 90D/180D MFE with shallow MAE. |
| R8L90_C27_STUDIOMIR_2024_OUTSOURCE_ANIMATION_FALSE_STAGE2 | 408900 | 스튜디오미르 | counterexample | Outsourced animation production recovery had high MAE and lacked owned-IP monetization bridge. |
| R8L90_C27_FINGERSTORY_2024_WEBTOON_PLATFORM_THEME_EVENT_CAP_4B | 417180 | 핑거스토리 | counterexample / 4B | Webtoon/platform theme premium capped at the January spike and then de-rated. |

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
| SAMG kids IP / merch monetization | historical public/report proxy | true | true | shadow-only positive |
| Studio Mir outsource animation false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Finger Story webtoon platform cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 419530 | atlas/ohlcv_tradable_by_symbol_year/419/419530/2024.csv; 2025.csv | atlas/symbol_profiles/419/419530.json |
| 408900 | atlas/ohlcv_tradable_by_symbol_year/408/408900/2024.csv | atlas/symbol_profiles/408/408900.json |
| 417180 | atlas/ohlcv_tradable_by_symbol_year/417/417180/2024.csv | atlas/symbol_profiles/417/417180.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L90_C27_SAMG_2024_STAGE2_ACTIONABLE_KIDS_IP_MERCH_MONETIZATION | 419530 | Stage2-Actionable | 2024-07-12 | 9740 | positive | owned-IP merchandise/licensing bridge worked |
| R8L90_C27_STUDIOMIR_2024_STAGE2_FALSE_POSITIVE_OUTSOURCE_ANIMATION | 408900 | Stage2-Actionable | 2024-06-26 | 3605 | counterexample | outsource animation false Stage2 |
| R8L90_C27_FINGERSTORY_2024_STAGE4B_WEBTOON_PLATFORM_THEME_CAP | 417180 | Stage4B | 2024-01-24 | 4245 | counterexample/4B | webtoon platform event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L90_C27_SAMG_2024_STAGE2_ACTIONABLE_KIDS_IP_MERCH_MONETIZATION | 9740 | 47.74 | -3.59 | 101.54 | -3.59 | 264.48 | -3.59 | 2025-04-11 | 35500 | -57.18 |
| R8L90_C27_STUDIOMIR_2024_STAGE2_FALSE_POSITIVE_OUTSOURCE_ANIMATION | 3605 | 1.53 | -32.73 | 24.27 | -38.28 | 25.80 | -38.28 | 2024-10-07 | 4535 | -49.17 |
| R8L90_C27_FINGERSTORY_2024_STAGE4B_WEBTOON_PLATFORM_THEME_CAP | 4245 | 13.78 | -22.14 | 13.78 | -22.14 | 13.78 | -50.53 | 2024-01-24 | 4830 | -56.52 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C27 Stage2 needs owned-IP / revenue / merch / licensing / overseas distribution / margin bridge |
| local_4b_watch_guard | strengthen: content production and webtoon/platform theme premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is IP monetization bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 419530 | good_stage2 | Owned IP converted into merchandise/licensing monetization premium. |
| 408900 | bad_stage2 | Content production label lacked owned-IP/recurring monetization bridge and had high MAE. |
| 417180 | good_4B | Webtoon platform theme premium capped at the event spike. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 408900 outsource animation false Stage2 | 0.81 | 0.81 | content-production recovery was false Stage2 due missing owned-IP monetization bridge |
| 417180 webtoon platform cap | 1.00 | 1.00 | good full-window 4B timing |
| 419530 kids-IP monetization bridge | n/a | n/a | positive Stage2, but later IP valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 408900 / 417180
```

No hard 4C candidate is proposed. R8 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 content/IP monetization cases, Stage2 requires verified owned-IP, revenue conversion, merchandise sell-through, licensing, overseas distribution, paid traffic, recurring contract, margin, or revision bridge. Content, webtoon, animation, OTT, or platform label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
rule = C27 should split owned-IP monetization positives from outsource-production false Stage2 and webtoon/platform event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 46.53 | -21.34 | 0.67 | mixed; C27 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 46.53 | -21.34 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L8 owned-IP monetization bridge required | 2 | 62.91 | -20.94 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C27 bridge vs event-cap split | 2 | 62.91 | -20.94 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing content themes as positive | 1 | 101.54 | -3.59 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 419530 kids IP bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 101.54 | -3.59 | kids_IP_merch_global_monetization_positive |
| 408900 outsource animation false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 24.27 | -38.28 | outsourced_animation_false_stage2 |
| 417180 webtoon platform cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 13.78 | -22.14 | webtoon_platform_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C27 kids-animation IP merchandising positive, outsourced-animation false Stage2, and webtoon-platform theme event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: kids_IP_merch_global_monetization_positive, outsourced_animation_false_stage2, webtoon_platform_event_cap_4B
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
- C27 content/IP global monetization bridge vs content-theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,C27_requires_owned_IP_revenue_merch_licensing_or_margin_bridge,0,"C27 Stage2 should require owned IP, revenue conversion, merchandise sell-through, licensing, overseas distribution, paid traffic, margin, or revision bridge, not content/webtoon/theme label alone","SAMG positive worked; Studio Mir and Finger Story theme/event rows failed positive-stage promotion","R8L90_C27_SAMG_2024_STAGE2_ACTIONABLE_KIDS_IP_MERCH_MONETIZATION|R8L90_C27_STUDIOMIR_2024_STAGE2_FALSE_POSITIVE_OUTSOURCE_ANIMATION|R8L90_C27_FINGERSTORY_2024_STAGE4B_WEBTOON_PLATFORM_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,cap_webtoon_platform_and_content_production_theme_premiums_as_4B_watch,0,"Content production and webtoon/platform theme premiums can peak before verified monetization or margin bridge appears","Studio Mir showed high-MAE false Stage2; Finger Story showed event-cap behavior with deep 180D MAE","R8L90_C27_STUDIOMIR_2024_STAGE2_FALSE_POSITIVE_OUTSOURCE_ANIMATION|R8L90_C27_FINGERSTORY_2024_STAGE4B_WEBTOON_PLATFORM_THEME_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L90_C27_SAMG_2024_KIDS_IP_MERCH_GLOBAL_MONETIZATION_POSITIVE", "symbol": "419530", "company_name": "SAMG엔터", "round": "R8", "loop": "90", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L90_C27_SAMG_2024_STAGE2_ACTIONABLE_KIDS_IP_MERCH_MONETIZATION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Kids animation IP / merchandise / global monetization bridge produced very high 90D and 180D MFE with shallow early MAE; C27 works when IP awareness converts into product sell-through, licensing, overseas distribution, and margin/revision bridge.", "current_profile_verdict": "current_profile_kept_but_C27_positive_requires_IP_to_revenue_merch_licensing_margin_bridge_not_content_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R8L90_C27_STUDIOMIR_2024_OUTSOURCE_ANIMATION_FALSE_STAGE2", "symbol": "408900", "company_name": "스튜디오미르", "round": "R8", "loop": "90", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R8L90_C27_STUDIOMIR_2024_STAGE2_FALSE_POSITIVE_OUTSOURCE_ANIMATION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "2024-04-05 and 2024-04-26 corporate-action candidates were blocked; selected post-CA 2024-06-26 row only.", "independent_evidence_weight": 0.5, "score_price_alignment": "Outsource animation / content-production recovery label produced little near-term upside and high 90D MAE; C27 Stage2 should not be awarded without owned-IP, licensing, recurring contract, or margin bridge.", "current_profile_verdict": "current_profile_false_positive_if_content_production_theme_counts_without_owned_IP_or_recurring_monetization_bridge", "price_source": "Songdaiki/stock-web", "notes": "Reduced weight because selected window is post-CA and source-proxy only."}
{"row_type": "case", "case_id": "R8L90_C27_FINGERSTORY_2024_WEBTOON_PLATFORM_THEME_EVENT_CAP_4B", "symbol": "417180", "company_name": "핑거스토리", "round": "R8", "loop": "90", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L90_C27_FINGERSTORY_2024_STAGE4B_WEBTOON_PLATFORM_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Webtoon/platform theme premium capped around the January spike and then de-rated; webtoon/IP platform theme should route to 4B unless conversion into paid traffic, licensing, overseas sales, or margin bridge is verified.", "current_profile_verdict": "current_profile_4B_too_late_if_webtoon_platform_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after 2023-12-05 CA candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L90_C27_SAMG_2024_STAGE2_ACTIONABLE_KIDS_IP_MERCH_MONETIZATION", "case_id": "R8L90_C27_SAMG_2024_KIDS_IP_MERCH_GLOBAL_MONETIZATION_POSITIVE", "symbol": "419530", "company_name": "SAMG엔터", "round": "R8", "loop": "90", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP", "sector": "kids_animation_IP_merch_global_monetization", "primary_archetype": "kids_IP_merch_licensing_sellthrough_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "entry_date": "2024-07-12", "entry_price": 9740.0, "evidence_available_at_that_date": "kids animation IP, merchandise sell-through, licensing, overseas distribution and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["owned_IP_awareness", "merchandise_sellthrough_proxy", "licensing_distribution_bridge", "margin_revision_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "very_high_MFE90", "very_high_MFE180", "shallow_entry_MAE"], "stage4b_evidence_fields": ["valuation_watch_after_IP_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/419/419530/2024.csv|atlas/ohlcv_tradable_by_symbol_year/419/419530/2025.csv", "profile_path": "atlas/symbol_profiles/419/419530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 47.74, "MFE_90D_pct": 101.54, "MFE_180D_pct": 264.48, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.59, "MAE_90D_pct": -3.59, "MAE_180D_pct": -3.59, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-04-11", "peak_price": 35500.0, "drawdown_after_peak_pct": -57.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_IP_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "IP_monetization_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_kids_IP_merch_monetization_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L90_C27_419530_2024-07-12_9740", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L90_C27_STUDIOMIR_2024_STAGE2_FALSE_POSITIVE_OUTSOURCE_ANIMATION", "case_id": "R8L90_C27_STUDIOMIR_2024_OUTSOURCE_ANIMATION_FALSE_STAGE2", "symbol": "408900", "company_name": "스튜디오미르", "round": "R8", "loop": "90", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP", "sector": "animation_outsource_content_production", "primary_archetype": "content_production_recovery_without_owned_IP_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 3605.0, "evidence_available_at_that_date": "animation content-production recovery and global OTT content theme proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["animation_production_theme", "global_content_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "high_MAE90", "owned_IP_monetization_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/408/408900/2024.csv", "profile_path": "atlas/symbol_profiles/408/408900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.53, "MFE_90D_pct": 24.27, "MFE_180D_pct": 25.8, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -32.73, "MAE_90D_pct": -38.28, "MAE_180D_pct": -38.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-07", "peak_price": 4535.0, "drawdown_after_peak_pct": -49.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.81, "four_b_full_window_peak_proximity": 0.81, "four_b_timing_verdict": "content_production_recovery_was_false_stage2_due_missing_owned_IP_monetization_bridge", "four_b_evidence_type": ["price_only", "positioning_overheat", "owned_IP_monetization_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_content_production_without_owned_IP_bridge", "current_profile_verdict": "current_profile_false_positive_if_content_production_theme_counts_without_owned_IP_or_recurring_monetization_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-04-26_CA_window", "same_entry_group_id": "R8L90_C27_408900_2024-06-26_3605", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "post-CA row only; 2024-04-05 and 2024-04-26 corporate-action candidates blocked from entry selection", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L90_C27_FINGERSTORY_2024_STAGE4B_WEBTOON_PLATFORM_THEME_CAP", "case_id": "R8L90_C27_FINGERSTORY_2024_WEBTOON_PLATFORM_THEME_EVENT_CAP_4B", "symbol": "417180", "company_name": "핑거스토리", "round": "R8", "loop": "90", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP", "sector": "webtoon_platform_IP_theme", "primary_archetype": "webtoon_platform_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 4245.0, "evidence_available_at_that_date": "webtoon/IP platform theme premium after January spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["webtoon_platform_theme", "IP_platform_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/417/417180/2024.csv", "profile_path": "atlas/symbol_profiles/417/417180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.78, "MFE_90D_pct": 13.78, "MFE_180D_pct": 13.78, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.14, "MAE_90D_pct": -22.14, "MAE_180D_pct": -50.53, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 4830.0, "drawdown_after_peak_pct": -56.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_webtoon_platform_theme_cap", "four_b_evidence_type": ["IP_platform_theme_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_webtoon_platform_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023-12-05_CA", "same_entry_group_id": "R8L90_C27_417180_2024-01-24_4245", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L90_C27_SAMG_2024_KIDS_IP_MERCH_GLOBAL_MONETIZATION_POSITIVE", "trigger_id": "R8L90_C27_SAMG_2024_STAGE2_ACTIONABLE_KIDS_IP_MERCH_MONETIZATION", "symbol": "419530", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 60, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 50, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "kids_IP_merch_global_monetization_positive", "MFE_90D_pct": 101.54, "MAE_90D_pct": -3.59, "score_return_alignment_label": "kids_IP_merch_global_monetization_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L90_C27_STUDIOMIR_2024_OUTSOURCE_ANIMATION_FALSE_STAGE2", "trigger_id": "R8L90_C27_STUDIOMIR_2024_STAGE2_FALSE_POSITIVE_OUTSOURCE_ANIMATION", "symbol": "408900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "outsourced_animation_false_stage2", "MFE_90D_pct": 24.27, "MAE_90D_pct": -38.28, "score_return_alignment_label": "outsourced_animation_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_content_production_theme_counts_without_owned_IP_or_recurring_monetization_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L90_C27_FINGERSTORY_2024_WEBTOON_PLATFORM_THEME_EVENT_CAP_4B", "trigger_id": "R8L90_C27_FINGERSTORY_2024_STAGE4B_WEBTOON_PLATFORM_THEME_CAP", "symbol": "417180", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "webtoon_platform_event_cap_4B_guard", "MFE_90D_pct": 13.78, "MAE_90D_pct": -22.14, "score_return_alignment_label": "webtoon_platform_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_webtoon_platform_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "90", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KIDS_ANIMATION_IP_MERCH_GLOBAL_MONETIZATION_BRIDGE_VS_OUTSOURCE_ANIMATION_AND_WEBTOON_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["kids_IP_merch_global_monetization_positive", "outsourced_animation_false_stage2", "webtoon_platform_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","reason":"all selected rows have usable 180D stock-web windows; 408900 entry was shifted after the 2024-04-05 and 2024-04-26 corporate-action candidates","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R8
completed_loop = 90
next_round = R9
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
