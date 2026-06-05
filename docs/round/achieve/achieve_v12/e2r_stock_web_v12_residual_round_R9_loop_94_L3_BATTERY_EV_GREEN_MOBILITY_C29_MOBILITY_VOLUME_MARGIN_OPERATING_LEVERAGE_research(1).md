# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_94_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R8 loop 94 is R9 / loop 94. R9 permits the L3 mobility/battery route or the L9 construction route. This run uses the L3 mobility route and fills C29 mobility volume/margin operating-leverage behavior rather than repeating the immediately preceding R9 loop 93 C14 EV-demand-slowdown file.

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
scheduled_round = R9
scheduled_loop = 94
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 94
```

C29 is a production-volume and operating-leverage archetype. Auto-parts labels are not enough: the mechanism needs OEM production schedule, customer mix, overseas throughput, utilization, ASP/mix, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE = 60 rows / 27 symbols / good-bad Stage2 26-13 / 4B-4C 6-0
top covered symbols include 011210(7), 000270(5), 005380(5), 005850(5), 010690(5), 018880(3)
previous R9 loop-93 C14 symbols avoided: 096770, 222080, 086520
previous R8 loop-94 C28 symbols avoided: 030520, 053800, 434480
```

Selected rows avoid hard duplicates and top repeated C29 symbols:

```text
015750 / Stage2-Actionable / 2024-01-24
009900 / Stage2-Actionable / 2024-01-24
123410 / Stage4B / 2024-04-26
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
| 015750 | atlas/symbol_profiles/015/015750.json | selected 2024 window clean after old 1996~2018 CA candidates |
| 009900 | atlas/symbol_profiles/009/009900.json | selected 2024 window clean after old 2021 CA candidate |
| 123410 | atlas/symbol_profiles/123/123410.json | selected 2024 window clean after old 2012 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L94_C29_SUNGWOOHITEC_2024_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_POSITIVE | 015750 | 2024-01-24 | yes | 180 | yes | yes | true |
| R9L94_C29_MYOUNGSHIN_2024_EV_BODY_PARTS_VOLUME_FALSE_STAGE2 | 009900 | 2024-01-24 | yes | 180 | yes | yes | true |
| R9L94_C29_KOREAFT_2024_HYBRID_PARTS_MOBILITY_EVENT_CAP_4B | 123410 | 2024-04-26 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE | Positive Stage2 requires OEM volume schedule, customer mix, overseas throughput, utilization, margin and revision bridge. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV_BODY_PARTS_FALSE_STAGE2 | EV/body-parts volume watch without OEM/utilization/margin bridge can become false Stage2. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | HYBRID_PARTS_EVENT_CAP_4B | Hybrid/eco-car parts event premium should route to 4B when order and margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R9L94_C29_SUNGWOOHITEC_2024_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_POSITIVE | 015750 | 성우하이텍 | positive | Auto-parts global volume/margin bridge produced strong MFE with shallow early MAE. |
| R9L94_C29_MYOUNGSHIN_2024_EV_BODY_PARTS_VOLUME_FALSE_STAGE2 | 009900 | 명신산업 | counterexample | EV body-parts volume watch had low MFE and persistent MAE without utilization/margin bridge. |
| R9L94_C29_KOREAFT_2024_HYBRID_PARTS_MOBILITY_EVENT_CAP_4B | 123410 | 코리아에프티 | counterexample / 4B | Hybrid-parts event premium capped near the late-April spike and then de-rated. |

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
| Sungwoo Hitech global auto-parts volume/margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Myoungshin EV body-parts false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| KoreaFT hybrid-parts event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 015750 | atlas/ohlcv_tradable_by_symbol_year/015/015750/2024.csv | atlas/symbol_profiles/015/015750.json |
| 009900 | atlas/ohlcv_tradable_by_symbol_year/009/009900/2024.csv | atlas/symbol_profiles/009/009900.json |
| 123410 | atlas/ohlcv_tradable_by_symbol_year/123/123410/2024.csv | atlas/symbol_profiles/123/123410.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R9L94_C29_SUNGWOOHITEC_2024_STAGE2_ACTIONABLE_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE | 015750 | Stage2-Actionable | 2024-01-24 | 8130 | positive | auto-parts global volume/margin bridge worked |
| R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH | 009900 | Stage2-Actionable | 2024-01-24 | 16730 | counterexample | EV body-parts volume false Stage2 |
| R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP | 123410 | Stage4B | 2024-04-26 | 7700 | counterexample/4B | hybrid-parts mobility event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L94_C29_SUNGWOOHITEC_2024_STAGE2_ACTIONABLE_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE | 8130 | 35.18 | -1.85 | 35.18 | -1.85 | 35.18 | -3.44 | 2024-02-26 | 10990 | -28.57 |
| R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH | 16730 | 5.92 | -4.54 | 5.92 | -15.18 | 5.92 | -18.11 | 2024-02-02 | 17720 | -19.92 |
| R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP | 7700 | 6.36 | -19.74 | 6.36 | -32.34 | 6.36 | -36.36 | 2024-04-26 | 8190 | -36.39 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C29 Stage2 needs OEM volume / customer mix / utilization / operating leverage / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing mobility and hybrid-parts event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE mobility-event rows cannot promote without durable volume/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether mobility volume becomes operating leverage:

| symbol | stage quality | explanation |
|---|---|---|
| 015750 | good_stage2_with_later_watch | OEM/global volume and margin bridge produced strong MFE with shallow early MAE. |
| 009900 | bad_stage2 | EV body-parts volume watch lacked utilization/margin bridge and produced only low MFE. |
| 123410 | good_4B | Hybrid-parts event premium capped near the late-April spike and then de-rated sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 009900 EV body-parts false Stage2 | 0.94 | 0.94 | false Stage2 due missing OEM volume/utilization/margin bridge |
| 123410 hybrid-parts cap | 0.94 | 0.94 | good full-window 4B timing after late-April mobility event spike |
| 015750 auto-parts margin bridge | n/a | n/a | positive Stage2, but later auto-parts valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 009900 / 123410
```

No hard 4C candidate is proposed. R9 loop 94 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 mobility volume/margin cases, Stage2 requires verified OEM production volume, customer mix, overseas throughput, utilization, ASP/mix, operating leverage, margin, or revision bridge. Auto-parts, EV, hybrid, eco-car, mobility, body-parts or theme label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rule = C29 should split true OEM-volume/utilization/margin positives from EV/body-parts volume false Stage2 and hybrid-parts event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 15.82 | -16.46 | 0.67 | mixed; C29 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 15.82 | -16.46 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 OEM volume/utilization/margin bridge required | 2 | 20.55 | -8.52 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C29 bridge vs event-cap split | 2 | 20.55 | -8.52 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing mobility volume themes as positive | 1 | 35.18 | -1.85 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 015750 auto-parts volume bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 35.18 | -1.85 | auto_parts_global_volume_margin_positive |
| 009900 EV body-parts false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 5.92 | -15.18 | EV_body_parts_volume_false_stage2 |
| 123410 hybrid-parts cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.36 | -32.34 | hybrid_parts_mobility_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C29 Sungwoo Hitech auto-parts volume/margin positive, Myoungshin EV body-parts volume false Stage2, and KoreaFT hybrid-parts mobility event-cap 4B split while avoiding top repeated C29 symbols and previous R9 loop93 C14 symbols."}
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
residual_error_types_found: auto_parts_global_volume_margin_positive, EV_body_parts_volume_false_stage2, hybrid_parts_mobility_event_cap_4B
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
- C29 mobility volume/margin operating-leverage bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,C29_requires_OEM_volume_customer_mix_utilization_operating_leverage_margin_revision_bridge,0,"C29 Stage2 should require OEM/customer volume recovery, production schedule, customer mix, overseas throughput, utilization, operating leverage, margin, or revision bridge, not mobility/EV/auto-parts label alone","Sungwoo Hitech positive worked; Myoungshin and KoreaFT event/watch rows failed positive-stage promotion","R9L94_C29_SUNGWOOHITEC_2024_STAGE2_ACTIONABLE_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE|R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH|R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,cap_bridge_missing_mobility_and_hybrid_parts_event_premiums_as_4B_watch,0,"Mobility/hybrid parts event premiums can peak before OEM volume, order and margin bridge is proven","Myoungshin had low forward MFE after EV body-parts watch; KoreaFT showed event-cap behavior after late-April hybrid-parts spike","R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH|R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,block_positive_stage_when_mobility_theme_has_high_or_persistent_MAE_without_volume_margin_bridge,0,"High or persistent MAE after bridge-missing mobility entries should block Stage2/Stage3 promotion unless OEM volume, utilization and margin evidence survives","Myoungshin MAE180=-18.11 and KoreaFT MAE90=-32.34","R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH|R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L94_C29_SUNGWOOHITEC_2024_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_POSITIVE", "symbol": "015750", "company_name": "성우하이텍", "round": "R9", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP", "case_type": "structural_success_with_later_auto_parts_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R9L94_C29_SUNGWOOHITEC_2024_STAGE2_ACTIONABLE_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Auto-parts global volume / body-module operating leverage bridge produced strong 30D/90D/180D MFE with shallow early MAE. C29 works when the mobility volume narrative maps into customer production schedule, overseas plant throughput, order mix, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C29_positive_requires_global_volume_order_mix_utilization_margin_revision_bridge_not_auto_parts_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996~2018 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R9L94_C29_MYOUNGSHIN_2024_EV_BODY_PARTS_VOLUME_FALSE_STAGE2", "symbol": "009900", "company_name": "명신산업", "round": "R9", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP", "case_type": "failed_rerating_EV_body_parts_volume_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV/body-parts volume recovery watch had only low forward MFE and then persistent MAE. C29 Stage2 should not be awarded without verified OEM production recovery, customer mix, utilization, operating leverage, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_EV_body_parts_volume_watch_counts_without_OEM_volume_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R9L94_C29_KOREAFT_2024_HYBRID_PARTS_MOBILITY_EVENT_CAP_4B", "symbol": "123410", "company_name": "코리아에프티", "round": "R9", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Hybrid/eco-car parts mobility event premium capped around the late-April spike and then drew down sharply. C29 should route bridge-missing hybrid-parts event premiums to 4B unless OEM volume, order backlog, utilization, ASP/mix, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_hybrid_parts_mobility_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2012 corporate-action candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L94_C29_SUNGWOOHITEC_2024_STAGE2_ACTIONABLE_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE", "case_id": "R9L94_C29_SUNGWOOHITEC_2024_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_POSITIVE", "symbol": "015750", "company_name": "성우하이텍", "round": "R9", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP", "sector": "auto_parts_global_volume_body_module_operating_leverage", "primary_archetype": "OEM_volume_customer_mix_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 8130.0, "evidence_available_at_that_date": "auto-parts global volume recovery, overseas customer production, body-module order mix, utilization and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["OEM_volume_schedule_proxy", "global_customer_mix_proxy", "overseas_plant_throughput_proxy", "utilization_margin_bridge_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "strong_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_auto_parts_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/015/015750/2024.csv", "profile_path": "atlas/symbol_profiles/015/015750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.18, "MFE_90D_pct": 35.18, "MFE_180D_pct": 35.18, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.85, "MAE_90D_pct": -1.85, "MAE_180D_pct": -3.44, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 10990.0, "drawdown_after_peak_pct": -28.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_auto_parts_valuation_4B_watch_needed", "four_b_evidence_type": ["global_volume_margin_bridge", "customer_mix", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_auto_parts_global_volume_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_2018_CA", "same_entry_group_id": "R9L94_C29_015750_2024-01-24_8130", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH", "case_id": "R9L94_C29_MYOUNGSHIN_2024_EV_BODY_PARTS_VOLUME_FALSE_STAGE2", "symbol": "009900", "company_name": "명신산업", "round": "R9", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP", "sector": "EV_body_parts_volume_recovery_watch", "primary_archetype": "EV_body_parts_volume_watch_without_OEM_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 16730.0, "evidence_available_at_that_date": "EV/body-parts volume recovery and mobility beta watch without confirmed OEM volume, customer mix, utilization or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EV_body_parts_volume_watch", "mobility_beta_recovery", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "persistent_MAE180", "OEM_volume_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009900/2024.csv", "profile_path": "atlas/symbol_profiles/009/009900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.92, "MFE_90D_pct": 5.92, "MFE_180D_pct": 5.92, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.54, "MAE_90D_pct": -15.18, "MAE_180D_pct": -18.11, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 17720.0, "drawdown_after_peak_pct": -19.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "EV_body_parts_volume_watch_was_false_stage2_due_missing_OEM_volume_utilization_margin_bridge", "four_b_evidence_type": ["mobility_volume_watch", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_EV_body_parts_volume_watch_without_utilization_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_EV_body_parts_volume_watch_counts_without_OEM_volume_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2021_CA", "same_entry_group_id": "R9L94_C29_009900_2024-01-24_16730", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP", "case_id": "R9L94_C29_KOREAFT_2024_HYBRID_PARTS_MOBILITY_EVENT_CAP_4B", "symbol": "123410", "company_name": "코리아에프티", "round": "R9", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP", "sector": "hybrid_eco_car_parts_mobility_event_premium", "primary_archetype": "hybrid_parts_mobility_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 7700.0, "evidence_available_at_that_date": "hybrid/eco-car parts and mobility event premium after late-April spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["hybrid_parts_event", "eco_car_mobility_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "OEM_volume_order_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/123/123410/2024.csv", "profile_path": "atlas/symbol_profiles/123/123410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.36, "MFE_90D_pct": 6.36, "MFE_180D_pct": 6.36, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.74, "MAE_90D_pct": -32.34, "MAE_180D_pct": -36.36, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-26", "peak_price": 8190.0, "drawdown_after_peak_pct": -36.39, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_hybrid_parts_mobility_event_cap", "four_b_evidence_type": ["hybrid_parts_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_hybrid_parts_mobility_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_hybrid_parts_mobility_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2012_CA", "same_entry_group_id": "R9L94_C29_123410_2024-04-26_7700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L94_C29_SUNGWOOHITEC_2024_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_POSITIVE", "trigger_id": "R9L94_C29_SUNGWOOHITEC_2024_STAGE2_ACTIONABLE_AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE", "symbol": "015750", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 55, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 50, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "auto_parts_global_volume_margin_positive", "MFE_90D_pct": 35.18, "MAE_90D_pct": -1.85, "score_return_alignment_label": "auto_parts_global_volume_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L94_C29_MYOUNGSHIN_2024_EV_BODY_PARTS_VOLUME_FALSE_STAGE2", "trigger_id": "R9L94_C29_MYOUNGSHIN_2024_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS_VOLUME_WATCH", "symbol": "009900", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EV_body_parts_volume_false_stage2", "MFE_90D_pct": 5.92, "MAE_90D_pct": -15.18, "score_return_alignment_label": "EV_body_parts_volume_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_EV_body_parts_volume_watch_counts_without_OEM_volume_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L94_C29_KOREAFT_2024_HYBRID_PARTS_MOBILITY_EVENT_CAP_4B", "trigger_id": "R9L94_C29_KOREAFT_2024_STAGE4B_HYBRID_PARTS_MOBILITY_EVENT_CAP", "symbol": "123410", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "hybrid_parts_mobility_event_cap_4B_guard", "MFE_90D_pct": 6.36, "MAE_90D_pct": -32.34, "score_return_alignment_label": "hybrid_parts_mobility_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_hybrid_parts_mobility_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_GLOBAL_VOLUME_MARGIN_BRIDGE_VS_EV_BODY_PARTS_FALSE_STAGE2_AND_HYBRID_PARTS_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["auto_parts_global_volume_margin_positive", "EV_body_parts_volume_false_stage2", "hybrid_parts_mobility_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C29 rows need explicit OEM/customer volume, production schedule, utilization, ASP/mix, operating leverage, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C29 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 94
next_round = R10
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
