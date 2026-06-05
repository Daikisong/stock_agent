# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_96_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
```

This file is the corrected final output for this execution. The scheduler state after R7 loop 96 is R8 / loop 96. R8 is the L8 platform/content/software/security round, and this run fills C27 content/IP global monetization rather than repeating the immediately preceding R8 loop 95 C26 ad-revenue file or R8 loop 94 C28 software/security file.

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
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 96
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
round_sector_consistency = pass
computed_next_round = R9
computed_next_loop = 96
```

C27 is a content/IP-to-monetization bridge archetype. A webtoon, animation, AI-content or VFX label is only the poster; the evidence is distribution, IP-library leverage, title slate, recurring monetization channel, licensing economics, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION = 39 rows / 15 symbols / good-bad Stage2 20-6 / 4B-4C 3-1 / reuse 6-6
top covered symbols include 263750(5), 112040(4), 122870(4), 293490(4), 259960(3), 376300(3)
previous R8 loop-90 C27 symbols avoided: 419530, 408900, 417180
previous R8 loop-93 C27 symbols avoided: 194480, 035760, 160550
previous R8 loop-94 C28 symbols avoided: 030520, 053800, 434480
previous R8 loop-95 C26 symbols avoided: 214320, 236810, 417860
previous R7 loop-96 C24 symbols avoided: 310210, 203400, 084990
```

Selected rows avoid hard duplicates and top repeated C27 symbols:

```text
432430 / Stage2-Actionable / 2024-02-06
048910 / Stage2-Actionable / 2024-01-24
289220 / Stage4B / 2024-01-09
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
| 432430 | atlas/symbol_profiles/432/432430.json | no corporate-action candidate |
| 048910 | atlas/symbol_profiles/048/048910.json | selected 2024 window clean after old 2007 CA candidate |
| 289220 | atlas/symbol_profiles/289/289220.json | selected 2024 window clean after old 2021/2022 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L96_C27_YLAB_2024_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_POSITIVE | 432430 | 2024-02-06 | yes | 180 | yes | yes | true |
| R8L96_C27_DAEWONMEDIA_2024_LEGACY_ANIMATION_IP_FALSE_STAGE2 | 048910 | 2024-01-24 | yes | 180 | yes | yes | true |
| R8L96_C27_GIANTSTEP_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B | 289220 | 2024-01-09 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C27_CONTENT_IP_GLOBAL_MONETIZATION | WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE | Positive Stage2 requires IP-library leverage, platform distribution, title slate, monetization channel, margin and revision bridge. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | LEGACY_ANIMATION_IP_FALSE_STAGE2 | Legacy animation/character-IP watch without distribution/slate/licensing bridge can become false Stage2. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B | AI/VFX/virtual-production event premium should route to 4B when recurring contract and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L96_C27_YLAB_2024_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_POSITIVE | 432430 | 와이랩 | positive | Webtoon/IP optionality produced strong 30D/90D MFE, but later deep drawdown requires 4B valuation watch. |
| R8L96_C27_DAEWONMEDIA_2024_LEGACY_ANIMATION_IP_FALSE_STAGE2 | 048910 | 대원미디어 | counterexample | Legacy animation/IP watch had brief MFE but persistent drawdown without distribution/slate bridge. |
| R8L96_C27_GIANTSTEP_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B | 289220 | 자이언트스텝 | counterexample / 4B | AI/VFX content event premium capped around the January spike and then de-rated sharply. |

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
| YLab webtoon/IP monetization bridge | historical public/report proxy | true | true | shadow-only positive |
| Daewon Media legacy animation/IP false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| GiantStep AI/VFX content event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 432430 | atlas/ohlcv_tradable_by_symbol_year/432/432430/2024.csv | atlas/symbol_profiles/432/432430.json |
| 048910 | atlas/ohlcv_tradable_by_symbol_year/048/048910/2024.csv | atlas/symbol_profiles/048/048910.json |
| 289220 | atlas/ohlcv_tradable_by_symbol_year/289/289220/2024.csv | atlas/symbol_profiles/289/289220.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L96_C27_YLAB_2024_STAGE2_ACTIONABLE_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE | 432430 | Stage2-Actionable | 2024-02-06 | 9530 | positive | webtoon/IP global monetization bridge worked, but later 4B watch required |
| R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH | 048910 | Stage2-Actionable | 2024-01-24 | 13020 | counterexample | legacy animation/IP false Stage2 |
| R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP | 289220 | Stage4B | 2024-01-09 | 16300 | counterexample/4B | virtual-production / AI-content event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L96_C27_YLAB_2024_STAGE2_ACTIONABLE_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE | 9530 | 55.19 | -4.09 | 88.77 | -4.09 | 88.77 | -51.84 | 2024-06-07 | 17990 | -74.49 |
| R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH | 13020 | 10.37 | -13.75 | 10.37 | -25.50 | 10.37 | -32.03 | 2024-01-24 | 14370 | -38.41 |
| R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP | 16300 | 6.32 | -33.68 | 6.32 | -45.09 | 6.32 | -61.35 | 2024-01-10 | 17330 | -63.65 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C27 Stage2 needs distribution / IP library / slate / monetization channel / licensing / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing content/IP and AI/VFX premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE content-event rows cannot promote without durable monetization bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether content/IP narrative becomes distribution, slate and monetization economics.

| symbol | stage quality | explanation |
|---|---|---|
| 432430 | good_stage2_with_later_watch | Webtoon/IP monetization bridge produced strong MFE, but later drawdown makes 4B valuation watch mandatory. |
| 048910 | bad_stage2 | Legacy IP watch lacked distribution/slate/licensing bridge and drifted down after brief premium. |
| 289220 | good_4B | AI/VFX event premium capped around the January spike and later suffered high MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 048910 legacy animation/IP false Stage2 | 0.91 | 0.91 | false Stage2 due missing distribution/slate/licensing bridge |
| 289220 AI/VFX content cap | 0.94 | 0.94 | good full-window 4B timing after January AI-content event premium |
| 432430 webtoon/IP bridge | n/a | n/a | positive Stage2, but later webtoon/IP valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 048910 / 289220
```

No hard 4C candidate is introduced in this R8 loop 96 file. The counterexamples are bridge-missing / event-cap rows, not hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 content/IP global monetization cases, Stage2 requires verified platform distribution, IP-library leverage, title/production slate, recurring monetization channel, licensing economics, margin, or revision bridge. Webtoon, animation, character IP, AI-content, VFX, virtual-production, K-content or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
rule = C27 should split true distribution/IP-library/slate/monetization positives from legacy-IP false Stage2 and AI/VFX event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 35.15 | -24.89 | 0.67 | mixed; C27 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 35.15 | -24.89 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L8 distribution/slate/monetization bridge required | 2 | 49.57 | -14.80 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C27 bridge vs event-cap split | 2 | 49.57 | -14.80 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing content/IP themes as positive | 1 | 88.77 | -4.09 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 432430 webtoon/IP bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 88.77 | -4.09 | webtoon_IP_global_monetization_positive_with_later_4B_watch |
| 048910 legacy IP false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 10.37 | -25.50 | legacy_animation_IP_false_stage2 |
| 289220 AI/VFX cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.32 | -45.09 | virtual_production_AI_content_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C27 YLab webtoon/IP monetization positive, Daewon Media legacy animation/IP false Stage2, and GiantStep virtual-production/AI-content event-cap 4B while avoiding top repeated C27 and previous R8/R7 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: webtoon_IP_global_monetization_positive, legacy_animation_IP_false_stage2, virtual_production_AI_content_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,C27_requires_distribution_IP_library_slate_monetization_margin_revision_bridge,0,"C27 Stage2 should require platform distribution, IP-library leverage, production/title slate, recurring monetization channel, licensing economics, margin, or revision bridge, not content/IP/AI/VFX label alone","YLab positive worked; Daewon Media and GiantStep event/watch rows failed positive-stage promotion","R8L96_C27_YLAB_2024_STAGE2_ACTIONABLE_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE|R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH|R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,cap_bridge_missing_content_IP_and_AI_VFX_event_premiums_as_4B_watch,0,"Legacy IP, AI/VFX and virtual-production event premiums can peak before distribution, slate, recurring contract and margin bridge is proven","Daewon Media had brief MFE then drawdown; GiantStep showed 4B event-cap behavior after January AI-content spike","R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH|R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,configured,block_positive_stage_when_content_IP_theme_has_high_or_persistent_MAE_without_monetization_bridge,0,"High or persistent MAE after bridge-missing C27 entries should block Stage2/Stage3 promotion unless distribution, slate, licensing and margin evidence survives","Daewon Media MAE90=-25.50 and GiantStep MAE90=-45.09","R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH|R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L96_C27_YLAB_2024_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_POSITIVE", "symbol": "432430", "company_name": "와이랩", "round": "R8", "loop": "96", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "case_type": "structural_success_with_later_webtoon_IP_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L96_C27_YLAB_2024_STAGE2_ACTIONABLE_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Webtoon/IP global optionality and content monetization bridge produced strong 30D/90D MFE, but the later deep drawdown confirms that C27 positives still need post-peak 4B valuation watch. C27 works when the content/IP label maps into platform distribution, IP library leverage, production slate, monetization channel, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C27_positive_requires_distribution_IP_library_slate_monetization_margin_revision_bridge_not_content_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R8L96_C27_DAEWONMEDIA_2024_LEGACY_ANIMATION_IP_FALSE_STAGE2", "symbol": "048910", "company_name": "대원미디어", "round": "R8", "loop": "96", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "case_type": "failed_rerating_legacy_animation_IP_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Legacy animation/IP monetization watch produced only a brief premium and then drifted into persistent drawdown. C27 Stage2 should not be awarded without confirmed distribution deal, new title slate, licensing/reorder, overseas channel, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_legacy_animation_IP_watch_counts_without_distribution_slate_licensing_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2007 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R8L96_C27_GIANTSTEP_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B", "symbol": "289220", "company_name": "자이언트스텝", "round": "R8", "loop": "96", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Virtual-production / AI-content event premium capped around the January spike and then suffered severe MAE. C27 should route bridge-missing AI/VFX/content-tech premiums to 4B unless contract backlog, recurring production slate, platform customer, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021/2022 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L96_C27_YLAB_2024_STAGE2_ACTIONABLE_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE", "case_id": "R8L96_C27_YLAB_2024_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_POSITIVE", "symbol": "432430", "company_name": "와이랩", "round": "R8", "loop": "96", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "sector": "webtoon_IP_global_monetization_platform_distribution", "primary_archetype": "IP_library_distribution_slate_monetization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 9530.0, "evidence_available_at_that_date": "webtoon/IP global monetization optionality, platform distribution, title slate and IP-library leverage proxy after February pullback; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["IP_library_proxy", "platform_distribution_proxy", "production_slate_proxy", "monetization_channel_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "later_high_MAE_requires_4B_watch"], "stage4b_evidence_fields": ["later_webtoon_IP_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/432/432430/2024.csv", "profile_path": "atlas/symbol_profiles/432/432430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 55.19, "MFE_90D_pct": 88.77, "MFE_180D_pct": 88.77, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.09, "MAE_90D_pct": -4.09, "MAE_180D_pct": -51.84, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-07", "peak_price": 17990.0, "drawdown_after_peak_pct": -74.49, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_webtoon_IP_valuation_4B_watch_needed_after_June_peak", "four_b_evidence_type": ["webtoon_IP_distribution_bridge", "monetization_channel", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_webtoon_IP_global_monetization_bridge_success_with_later_4B_watch", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R8L96_C27_432430_2024-02-06_9530", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH", "case_id": "R8L96_C27_DAEWONMEDIA_2024_LEGACY_ANIMATION_IP_FALSE_STAGE2", "symbol": "048910", "company_name": "대원미디어", "round": "R8", "loop": "96", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "sector": "legacy_animation_character_IP_monetization_watch", "primary_archetype": "legacy_IP_watch_without_distribution_slate_licensing_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 13020.0, "evidence_available_at_that_date": "legacy animation/character IP monetization watch without confirmed distribution deal, new title slate, licensing/reorder, overseas channel or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["legacy_animation_IP_watch", "character_IP_monetization_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["brief_MFE_then_persistent_MAE", "distribution_slate_licensing_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/048/048910/2024.csv", "profile_path": "atlas/symbol_profiles/048/048910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.37, "MFE_90D_pct": 10.37, "MFE_180D_pct": 10.37, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.75, "MAE_90D_pct": -25.5, "MAE_180D_pct": -32.03, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 14370.0, "drawdown_after_peak_pct": -38.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "legacy_animation_IP_watch_was_false_stage2_due_missing_distribution_slate_licensing_margin_bridge", "four_b_evidence_type": ["legacy_IP_event_premium", "bridge_missing", "persistent_drawdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_legacy_animation_IP_watch_without_distribution_slate_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_legacy_animation_IP_watch_counts_without_distribution_slate_licensing_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2007_CA", "same_entry_group_id": "R8L96_C27_048910_2024-01-24_13020", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "case_id": "R8L96_C27_GIANTSTEP_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B", "symbol": "289220", "company_name": "자이언트스텝", "round": "R8", "loop": "96", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "sector": "virtual_production_AI_content_event_premium", "primary_archetype": "virtual_production_AI_content_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-09", "entry_date": "2024-01-09", "entry_price": 16300.0, "evidence_available_at_that_date": "virtual-production / AI-content / VFX event premium after January AI-content spike without confirmed recurring contract backlog, platform customer, production slate or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["virtual_production_AI_event", "content_tech_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "contract_slate_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/289/289220/2024.csv", "profile_path": "atlas/symbol_profiles/289/289220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.32, "MFE_90D_pct": 6.32, "MFE_180D_pct": 6.32, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -33.68, "MAE_90D_pct": -45.09, "MAE_180D_pct": -61.35, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-10", "peak_price": 17330.0, "drawdown_after_peak_pct": -63.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_virtual_production_AI_content_event_cap", "four_b_evidence_type": ["AI_content_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_virtual_production_AI_content_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_2022_CA", "same_entry_group_id": "R8L96_C27_289220_2024-01-09_16300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L96_C27_YLAB_2024_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_POSITIVE", "trigger_id": "R8L96_C27_YLAB_2024_STAGE2_ACTIONABLE_WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE", "symbol": "432430", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 55, "relative_strength_score": 80, "customer_quality_score": 50, "policy_or_regulatory_score": 5, "valuation_repricing_score": 45, "execution_risk_score": 40, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "webtoon_IP_global_monetization_positive_with_later_4B_watch", "MFE_90D_pct": 88.77, "MAE_90D_pct": -4.09, "score_return_alignment_label": "webtoon_IP_global_monetization_positive_with_later_4B_watch", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L96_C27_DAEWONMEDIA_2024_LEGACY_ANIMATION_IP_FALSE_STAGE2", "trigger_id": "R8L96_C27_DAEWONMEDIA_2024_STAGE2_FALSE_POSITIVE_LEGACY_ANIMATION_IP_WATCH", "symbol": "048910", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "legacy_animation_IP_false_stage2", "MFE_90D_pct": 10.37, "MAE_90D_pct": -25.5, "score_return_alignment_label": "legacy_animation_IP_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_legacy_animation_IP_watch_counts_without_distribution_slate_licensing_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L96_C27_GIANTSTEP_2024_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP_4B", "trigger_id": "R8L96_C27_GIANTSTEP_2024_STAGE4B_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "symbol": "289220", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "virtual_production_AI_content_event_cap_4B_guard", "MFE_90D_pct": 6.32, "MAE_90D_pct": -45.09, "score_return_alignment_label": "virtual_production_AI_content_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_virtual_production_AI_content_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "96", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_OPTIONALITY_BRIDGE_VS_LEGACY_ANIMATION_IP_FALSE_STAGE2_AND_VIRTUAL_PRODUCTION_AI_CONTENT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["webtoon_IP_global_monetization_positive", "legacy_animation_IP_false_stage2", "virtual_production_AI_content_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C27 rows need explicit platform distribution, IP-library leverage, title/production slate, recurring monetization channel, licensing economics, margin or revision bridge before positive promotion.
- In C27, bridge-missing content/IP event-premium rows with low MFE/high MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C27 content/IP rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 96
next_round = R9
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
