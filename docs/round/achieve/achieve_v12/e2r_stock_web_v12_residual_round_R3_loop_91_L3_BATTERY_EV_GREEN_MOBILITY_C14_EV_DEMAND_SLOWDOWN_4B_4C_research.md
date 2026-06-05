# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | 4B_4C_protection_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
```

This file is the corrected final output for this execution. The actual scheduler state after R2 loop 91 is R3 / loop 91. C14 is a protection archetype, so this loop intentionally prioritizes hard-4C, false-4C, and 4B timing behavior rather than adding a conventional positive Stage2 case.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
false_4c_recheck = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
stage2_required_bridge = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 91
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 91
```

R3 permits L3 battery/EV/green mobility research. Previous R3 loop 90 used C12 and R2 loop 91 used C06, so this loop fills the C14 EV-demand protection axis.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C = 21 rows / 14 symbols / good-bad Stage2 3-3 / 4B-4C 6-4
top covered symbols include 006400(3), 373220(3), 095500(2), 247540(2), 278280(2), 003670(1)
previous R3 loop-88 C14 symbols avoided: 361610, 051910, 011790
previous R3 loop-90 C12 symbols avoided: 002710, 290670, 396300
previous R2 loop-91 C06 symbols avoided: 000660, 080220, 253590
```

Selected rows avoid hard duplicates and top repeated C14 symbols:

```text
066970 / Stage4C / 2024-03-25
089980 / Stage4C / 2024-02-23
336370 / Stage4B / 2024-04-11
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
| 066970 | atlas/symbol_profiles/066/066970.json | selected 2024 window clean after 2016/2021 CA candidates |
| 089980 | atlas/symbol_profiles/089/089980.json | no corporate-action candidate |
| 336370 | atlas/symbol_profiles/336/336370.json | selected post-2024-01-30 CA window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L91_C14_LENF_2024_EV_DEMAND_SLOWDOWN_HARD_4C | 066970 | 2024-03-25 | yes | 180 | yes | yes | true |
| R3L91_C14_SANGAFRONTEC_2024_EV_MEMBRANE_FALSE_4C_RECOVERY | 089980 | 2024-02-23 | yes | 180 | yes | yes | true |
| R3L91_C14_SOLUS_2024_COPPER_FOIL_EV_DEMAND_EVENT_CAP_4B | 336370 | 2024-04-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_DEMAND_SLOWDOWN_HARD_4C | Hard 4C needs order, ASP, utilization, and margin bridge break plus severe drawdown. |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_MEMBRANE_FALSE_4C_RECOVERY | If drawdown is contained and recovery emerges, hard 4C must be rechecked. |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | COPPER_FOIL_EV_DEMAND_EVENT_CAP_4B | Bridge-missing material recovery premium should route to 4B/watch. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L91_C14_LENF_2024_EV_DEMAND_SLOWDOWN_HARD_4C | 066970 | 엘앤에프 | hard 4C | EV cathode demand/margin thesis break produced weak MFE and severe 180D MAE. |
| R3L91_C14_SANGAFRONTEC_2024_EV_MEMBRANE_FALSE_4C_RECOVERY | 089980 | 상아프론테크 | false 4C | Component slowdown watch recovered; hard 4C would be too harsh. |
| R3L91_C14_SOLUS_2024_COPPER_FOIL_EV_DEMAND_EVENT_CAP_4B | 336370 | 솔루스첨단소재 | 4B | Copper-foil recovery premium capped and then de-rated severely. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 0
counterexample_count = 3
4B_case_count = 1
4C_case_count = 2
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

C14 is a protection archetype, so `positive_case_count=0` is intentional.

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| L&F demand/margin break | historical public/report proxy | true | true | hard-4C protection |
| Sanga Frontec false-4C recovery | historical public/news proxy | true | true | false-4C recheck |
| Solus copper-foil event cap | historical public/news proxy | true | true | 4B overlay |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | atlas/symbol_profiles/066/066970.json |
| 089980 | atlas/ohlcv_tradable_by_symbol_year/089/089980/2024.csv | atlas/symbol_profiles/089/089980.json |
| 336370 | atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv | atlas/symbol_profiles/336/336370.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L91_C14_LENF_2024_STAGE4C_EV_DEMAND_SLOWDOWN_MARGIN_THESIS_BREAK | 066970 | Stage4C | 2024-03-25 | 186300 | hard 4C | EV cathode demand/margin break |
| R3L91_C14_SANGAFRONTEC_2024_FALSE_4C_EV_MEMBRANE_RECOVERY_RECHECK | 089980 | Stage4C | 2024-02-23 | 20950 | false 4C | recheck; recovery emerged |
| R3L91_C14_SOLUS_2024_STAGE4B_COPPER_FOIL_EV_DEMAND_EVENT_CAP | 336370 | Stage4B | 2024-04-11 | 19900 | 4B | copper-foil recovery premium cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L91_C14_LENF_2024_STAGE4C_EV_DEMAND_SLOWDOWN_MARGIN_THESIS_BREAK | 186300 | 6.82 | -15.35 | 6.82 | -28.34 | 6.82 | -55.50 | 2024-03-25 | 199000 | -57.04 |
| R3L91_C14_SANGAFRONTEC_2024_FALSE_4C_EV_MEMBRANE_RECOVERY_RECHECK | 20950 | 9.31 | -10.98 | 27.92 | -10.98 | 28.40 | -14.08 | 2024-07-11 | 26900 | -33.09 |
| R3L91_C14_SOLUS_2024_STAGE4B_COPPER_FOIL_EV_DEMAND_EVENT_CAP | 19900 | 8.79 | -24.37 | 8.79 | -49.25 | 8.79 | -54.02 | 2024-04-11 | 21650 | -60.23 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| hard_4c_thesis_break_routes_to_4c | strengthen: hard 4C needs order/ASP/utilization/margin bridge break |
| false_4c_recheck | strengthen: not every EV slowdown watch is hard 4C |
| local_4b_watch_guard | strengthen: copper-foil recovery premium should route to 4B when bridge is missing |
| high_MAE_guardrail | strengthen: severe MAE confirms 4B/4C protection logic |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green row is introduced. The useful split is protection quality:

| symbol | stage quality | explanation |
|---|---|---|
| 066970 | good hard 4C | Weak MFE and severe MAE after demand/margin break. |
| 089980 | false 4C | Recovery path argues against automatic hard 4C. |
| 336370 | good 4B | Event premium capped and then de-rated severely. |

```text
green_lateness_ratio = not_applicable
reason = C14 protection round, no Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 066970 hard 4C | 1.00 | 1.00 | hard 4C EV demand/margin thesis break |
| 089980 false 4C | 0.78 | 0.78 | false 4C recheck needed |
| 336370 copper-foil cap | 1.00 | 1.00 | good full-window 4B timing |

## 16. 4C Protection Audit

```text
4C_case_count = 2
hard_4C_success_count = 1
false_4C_recheck_count = 1
```

This is the core contribution of the loop: C14 should be sharp enough to catch genuine demand/margin breaks, but not so blunt that it kills delayed-recovery component cases.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery/EV demand slowdown cases, hard 4C requires verified order, ASP, utilization, margin, customer call-off, or revision break plus severe MAE. If drawdown is contained and later recovery appears, use false-4C recheck/watch. Bridge-missing battery-material recovery spikes route to 4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
rule = C14 should split hard demand/margin thesis breaks from false-4C recoveries and bridge-missing 4B event caps. C14 rows are protection/risk calibration, not positive-stage promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | hard_4C_precision | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 14.51 | -29.52 | mixed | C14 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 14.51 | -29.52 | weaker | over/under-routes 4C |
| P1 sector_specific_candidate_profile | L3 hard-4C bridge-break required | 3 | 14.51 | -29.52 | better | distinguishes hard 4C and false 4C |
| P2 canonical_archetype_candidate_profile | C14 4B/4C split | 3 | 14.51 | -29.52 | best | best explanatory fit |
| P3 counterexample_guard_profile | reject all C14 as positive | 3 | 14.51 | -29.52 | safest | no positive promotion |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 066970 hard 4C | 70 | Stage2/Yellow-like | 42 | Stage4C-protection | 6.82 | -28.34 | hard_4C_EV_demand_slowdown_margin_break |
| 089980 false 4C | 45 | Stage4C-risk | 58 | Stage2-Watch/recheck | 27.92 | -10.98 | false_4C_recovery_recheck |
| 336370 4B cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.79 | -49.25 | copper_foil_EV_demand_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP", "positive_case_count": 0, "counterexample_count": 3, "4B_case_count": 1, "4C_case_count": 2, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 3, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C14 hard EV-demand 4C, false-4C recovery, and copper-foil event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: hard_4c_thesis_break_routes_to_4c, local_4b_watch_guard, stage2_required_bridge, high_MAE_guardrail, price_only_blowoff_blocks_positive_stage
residual_error_types_found: hard_4C_EV_demand_slowdown_margin_break, false_4C_recovery_recheck, copper_foil_EV_demand_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: hard_4c_thesis_break_routes_to_4c, false_4c_recheck, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: protection_archetype_no_positive_promotion
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
- C14 hard 4C vs false 4C vs 4B event-cap split
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
shadow_weight,hard_4c_thesis_break_routes_to_4c,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,C14_hard_4C_requires_order_ASP_utilization_margin_break,0,"C14 hard 4C should fire when EV demand slowdown maps into customer order, ASP, utilization, and margin bridge break with severe MAE","L&F had weak MFE and deep MAE after demand/margin thesis break","R3L91_C14_LENF_2024_STAGE4C_EV_DEMAND_SLOWDOWN_MARGIN_THESIS_BREAK",1,1,1,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,false_4c_recheck,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,avoid_4C_when_component_slowdown_later_recovers_without_deep_MAE,0,"C14 should not route every EV component slowdown watch to hard 4C; if MAE is contained and recovery emerges, use recheck/watch","Sanga Frontec had MFE90=27.92 and MAE90=-10.98, so hard 4C would be too harsh","R3L91_C14_SANGAFRONTEC_2024_FALSE_4C_EV_MEMBRANE_RECOVERY_RECHECK",1,1,1,low,false_4C_shadow_only,"counterweight against over-aggressive 4C"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,cap_bridge_missing_copper_foil_recovery_premiums_as_4B_watch,0,"Battery material recovery premiums can peak before utilization and margin bridge is proven","Solus Advanced Materials capped near the April spike and then suffered severe MAE","R3L91_C14_SOLUS_2024_STAGE4B_COPPER_FOIL_EV_DEMAND_EVENT_CAP",1,1,1,medium,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L91_C14_LENF_2024_EV_DEMAND_SLOWDOWN_HARD_4C", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP", "case_type": "hard_4c_thesis_break_protection", "positive_or_counterexample": "counterexample", "best_trigger": "R3L91_C14_LENF_2024_STAGE4C_EV_DEMAND_SLOWDOWN_MARGIN_THESIS_BREAK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV cathode demand slowdown / margin and customer-order deterioration produced weak forward MFE and severe 180D MAE; C14 should route this to 4C/watch rather than positive Stage2 when order, ASP, utilization, and margin bridge break.", "current_profile_verdict": "current_profile_kept_and_hard_4C_protection_should_block_EV_cathode_positive_stage", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2016/2021 CA candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R3L91_C14_SANGAFRONTEC_2024_EV_MEMBRANE_FALSE_4C_RECOVERY", "symbol": "089980", "company_name": "상아프론테크", "round": "R3", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP", "case_type": "false_4c_recovery_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L91_C14_SANGAFRONTEC_2024_FALSE_4C_EV_MEMBRANE_RECOVERY_RECHECK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV membrane/component slowdown watch had controlled MAE and later 90D/180D recovery. C14 hard 4C should not fire when the price path stabilizes and bridge evidence is merely delayed rather than broken.", "current_profile_verdict": "current_profile_false_4C_risk_if_EV_component_slowdown_watch_is_treated_as_thesis_break_without_margin_bridge_failure", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile; useful false-4C recheck case. Source-proxy only."}
{"row_type": "case", "case_id": "R3L91_C14_SOLUS_2024_COPPER_FOIL_EV_DEMAND_EVENT_CAP_4B", "symbol": "336370", "company_name": "솔루스첨단소재", "round": "R3", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L91_C14_SOLUS_2024_STAGE4B_COPPER_FOIL_EV_DEMAND_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper-foil / EV-demand recovery premium capped around the April spike and then suffered severe drawdown; bridge-missing battery material recovery premium should route to 4B/watch unless utilization and margin bridge survive.", "current_profile_verdict": "current_profile_4B_too_late_if_copper_foil_EV_demand_recovery_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected post-2024-01-30 CA window only; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L91_C14_LENF_2024_STAGE4C_EV_DEMAND_SLOWDOWN_MARGIN_THESIS_BREAK", "case_id": "R3L91_C14_LENF_2024_EV_DEMAND_SLOWDOWN_HARD_4C", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP", "sector": "EV_cathode_demand_slowdown_margin", "primary_archetype": "EV_cathode_order_ASP_utilization_margin_break_4C", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_4C_protection_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2024-03-25", "entry_date": "2024-03-25", "entry_price": 186300.0, "evidence_available_at_that_date": "EV cathode demand slowdown, customer order/ASP/utilization and margin deterioration proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["EV_cathode_recovery_watch", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_ASP_bridge_break", "utilization_margin_break", "deep_MAE180"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.82, "MFE_90D_pct": 6.82, "MFE_180D_pct": 6.82, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.35, "MAE_90D_pct": -28.34, "MAE_180D_pct": -55.5, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 199000.0, "drawdown_after_peak_pct": -57.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "hard_4C_EV_demand_slowdown_margin_thesis_break", "four_b_evidence_type": ["EV_demand_slowdown", "positioning_overheat", "margin_bridge_break"], "four_c_protection_label": "hard_4C_thesis_break", "trigger_outcome_label": "hard_4C_success_EV_cathode_demand_slowdown_margin_break", "current_profile_verdict": "current_profile_kept_and_hard_4C_protection_should_block_EV_cathode_positive_stage", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2021_CA", "same_entry_group_id": "R3L91_C14_066970_2024-03-25_186300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_4C", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L91_C14_SANGAFRONTEC_2024_FALSE_4C_EV_MEMBRANE_RECOVERY_RECHECK", "case_id": "R3L91_C14_SANGAFRONTEC_2024_EV_MEMBRANE_FALSE_4C_RECOVERY", "symbol": "089980", "company_name": "상아프론테크", "round": "R3", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP", "sector": "EV_membrane_component_slowdown_recovery", "primary_archetype": "false_4C_component_recovery_bridge_recheck", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_4C_protection_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 20950.0, "evidence_available_at_that_date": "EV membrane/component slowdown watch with delayed recovery bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EV_component_recovery_watch", "membrane_component_demand_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["slow_recovery_watch"], "stage4c_evidence_fields": ["false_4C_recheck", "no_deep_MAE90", "later_MFE90_recovery"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089980/2024.csv", "profile_path": "atlas/symbol_profiles/089/089980.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.31, "MFE_90D_pct": 27.92, "MFE_180D_pct": 28.4, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.98, "MAE_90D_pct": -10.98, "MAE_180D_pct": -14.08, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 26900.0, "drawdown_after_peak_pct": -33.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "false_4C_component_recovery_recheck_needed", "four_b_evidence_type": ["EV_component_recovery_watch", "delayed_bridge", "not_price_only"], "four_c_protection_label": "false_4C_recheck", "trigger_outcome_label": "false_4C_recovery_EV_membrane_component", "current_profile_verdict": "current_profile_false_4C_risk_if_EV_component_slowdown_watch_is_treated_as_thesis_break_without_margin_bridge_failure", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L91_C14_089980_2024-02-23_20950", "dedupe_for_aggregate": true, "aggregate_group_role": "false_4C_recheck", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L91_C14_SOLUS_2024_STAGE4B_COPPER_FOIL_EV_DEMAND_EVENT_CAP", "case_id": "R3L91_C14_SOLUS_2024_COPPER_FOIL_EV_DEMAND_EVENT_CAP_4B", "symbol": "336370", "company_name": "솔루스첨단소재", "round": "R3", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP", "sector": "copper_foil_EV_demand_recovery_theme", "primary_archetype": "copper_foil_EV_demand_recovery_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_4C_protection_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-11", "entry_date": "2024-04-11", "entry_price": 19900.0, "evidence_available_at_that_date": "battery copper-foil / EV-demand recovery premium after April spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["copper_foil_EV_recovery_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv", "profile_path": "atlas/symbol_profiles/336/336370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.79, "MFE_90D_pct": 8.79, "MFE_180D_pct": 8.79, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -24.37, "MAE_90D_pct": -49.25, "MAE_180D_pct": -54.02, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-11", "peak_price": 21650.0, "drawdown_after_peak_pct": -60.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_copper_foil_EV_demand_event_cap", "four_b_evidence_type": ["EV_demand_recovery_theme", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_copper_foil_EV_demand_recovery_premium", "current_profile_verdict": "current_profile_4B_too_late_if_copper_foil_EV_demand_recovery_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-01-30_CA_window", "same_entry_group_id": "R3L91_C14_336370_2024-04-11_19900", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L91_C14_LENF_2024_EV_DEMAND_SLOWDOWN_HARD_4C", "trigger_id": "R3L91_C14_LENF_2024_STAGE4C_EV_DEMAND_SLOWDOWN_MARGIN_THESIS_BREAK", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 60, "customer_quality_score": 25, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 70, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2/Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 20, "execution_risk_score": 95, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage4C-protection", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "customer_quality_score"], "component_delta_explanation": "hard_4C_EV_demand_slowdown_margin_break", "MFE_90D_pct": 6.82, "MAE_90D_pct": -28.34, "score_return_alignment_label": "hard_4C_EV_demand_slowdown_margin_break", "current_profile_verdict": "current_profile_kept_and_hard_4C_protection_should_block_EV_cathode_positive_stage"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L91_C14_SANGAFRONTEC_2024_EV_MEMBRANE_FALSE_4C_RECOVERY", "trigger_id": "R3L91_C14_SANGAFRONTEC_2024_FALSE_4C_EV_MEMBRANE_RECOVERY_RECHECK", "symbol": "089980", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 60, "customer_quality_score": 25, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 70, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 45, "stage_label_before": "Stage4C-risk", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 45, "customer_quality_score": 25, "policy_or_regulatory_score": 10, "valuation_repricing_score": 35, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch/recheck", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "customer_quality_score"], "component_delta_explanation": "false_4C_recovery_recheck", "MFE_90D_pct": 27.92, "MAE_90D_pct": -10.98, "score_return_alignment_label": "false_4C_recovery_recheck", "current_profile_verdict": "current_profile_false_4C_risk_if_EV_component_slowdown_watch_is_treated_as_thesis_break_without_margin_bridge_failure"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L91_C14_SOLUS_2024_COPPER_FOIL_EV_DEMAND_EVENT_CAP_4B", "trigger_id": "R3L91_C14_SOLUS_2024_STAGE4B_COPPER_FOIL_EV_DEMAND_EVENT_CAP", "symbol": "336370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 60, "customer_quality_score": 25, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 70, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "customer_quality_score"], "component_delta_explanation": "copper_foil_EV_demand_event_cap_4B_guard", "MFE_90D_pct": 8.79, "MAE_90D_pct": -49.25, "score_return_alignment_label": "copper_foil_EV_demand_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_copper_foil_EV_demand_recovery_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "91", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_HARD_4C_VS_MEMBRANE_FALSE_4C_RECOVERY_AND_COPPER_FOIL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 0, "counterexample_count": 3, "4B_case_count": 1, "4C_case_count": 2, "tested_existing_calibrated_axes": ["hard_4c_thesis_break_routes_to_4c", "local_4b_watch_guard", "stage2_required_bridge", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["hard_4C_EV_demand_slowdown_margin_break", "false_4C_recovery_recheck", "copper_foil_EV_demand_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reason":"all selected rows have usable 180D stock-web windows; C14 is protection/risk calibration, not positive-stage promotion","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C14 protection rows should not promote Stage2/Stage3.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-4C rows should weaken over-aggressive 4C routing but must not become positive promotion without non-price bridge.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
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
10. Add tests that C14 protection rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 91
next_round = R4
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
