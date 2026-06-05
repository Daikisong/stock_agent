# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
```

This file is the corrected final output for this execution. The scheduler state after R13 loop 94 is R1 / loop 95. R1 is the L1 industrials/infra/defense/grid round, and this run fills C02 power-grid/datacenter CAPEX behavior rather than repeating the immediately preceding R1 loop 94 C03 defense-export file.

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
scheduled_round = R1
scheduled_loop = 95
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 95
```

C02 is a capex-to-backlog archetype. A grid/datacenter label is only the switch; the current actually flows through transformer backlog, customer quality, delivery cadence, capacity expansion, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C02_POWER_GRID_DATACENTER_CAPEX = 22 rows / 12 symbols / good-bad Stage2 11-4 / 4B-4C 2-0
top covered symbols include 000500(3), 006340(3), 033100(3), 001440(2), 017040(2), 189860(2)
previous R1 loop-91 C02 family avoided
previous R1 loop-93 C05 symbols avoided: 100840, 094820, 010960
previous R1 loop-94 C03 symbols avoided: 077970, 361390, 024740
previous R13 loop-94 review-only rows do_not_count_as_new_case
```

Selected rows avoid hard duplicates and top repeated C02 symbols:

```text
267260 / Stage2-Actionable / 2024-01-24
237750 / Stage2-Actionable / 2024-05-08
017510 / Stage4B / 2024-07-10
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
| 267260 | atlas/symbol_profiles/267/267260.json | selected 2024 window clean after old 2017~2019 CA candidates |
| 237750 | atlas/symbol_profiles/237/237750.json | no corporate-action candidate |
| 017510 | atlas/symbol_profiles/017/017510.json | selected 2024 window clean after old 1996~1999 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L95_C02_HDHYUNDAIELECTRIC_2024_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_POSITIVE | 267260 | 2024-01-24 | yes | 180 | yes | yes | true |
| R1L95_C02_PNCTECH_2024_GRID_AUTOMATION_CAPEX_FALSE_STAGE2 | 237750 | 2024-05-08 | yes | 180 | yes | yes | true |
| R1L95_C02_SEMYOUNGELECTRIC_2024_TRANSMISSION_FITTING_GRID_EVENT_CAP_4B | 017510 | 2024-07-10 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C02_POWER_GRID_DATACENTER_CAPEX | TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE | Positive Stage2 requires transformer backlog, customer quality, data-center/grid CAPEX linkage, delivery cadence, capacity and margin bridge. |
| C02_POWER_GRID_DATACENTER_CAPEX | GRID_AUTOMATION_FALSE_STAGE2 | Grid automation/protection relay watch without confirmed utility order and margin bridge can become false Stage2. |
| C02_POWER_GRID_DATACENTER_CAPEX | TRANSMISSION_FITTING_EVENT_CAP_4B | Transmission fitting/grid event premium should route to 4B when utility order/backlog bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L95_C02_HDHYUNDAIELECTRIC_2024_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_POSITIVE | 267260 | HD현대일렉트릭 | positive | Transformer/grid backlog and data-center CAPEX bridge produced extreme MFE with shallow initial MAE. |
| R1L95_C02_PNCTECH_2024_GRID_AUTOMATION_CAPEX_FALSE_STAGE2 | 237750 | 피앤씨테크 | counterexample | Grid-automation capex watch had low forward MFE and later drawdown without utility-order bridge. |
| R1L95_C02_SEMYOUNGELECTRIC_2024_TRANSMISSION_FITTING_GRID_EVENT_CAP_4B | 017510 | 세명전기 | counterexample / 4B | Transmission fitting event premium capped on the July spike and then de-rated deeply. |

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
| HD Hyundai Electric transformer/grid/datacenter bridge | historical public/report proxy | true | true | shadow-only positive |
| PNC Tech grid-automation false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Semyoung Electric transmission fitting event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 267260 | atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv | atlas/symbol_profiles/267/267260.json |
| 237750 | atlas/ohlcv_tradable_by_symbol_year/237/237750/2024.csv | atlas/symbol_profiles/237/237750.json |
| 017510 | atlas/ohlcv_tradable_by_symbol_year/017/017510/2024.csv | atlas/symbol_profiles/017/017510.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L95_C02_HDHYUNDAIELECTRIC_2024_STAGE2_ACTIONABLE_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX | 267260 | Stage2-Actionable | 2024-01-24 | 101200 | positive | transformer/grid backlog bridge worked |
| R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH | 237750 | Stage2-Actionable | 2024-05-08 | 6990 | counterexample | grid automation capex false Stage2 |
| R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP | 017510 | Stage4B | 2024-07-10 | 8780 | counterexample/4B | transmission fitting grid event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L95_C02_HDHYUNDAIELECTRIC_2024_STAGE2_ACTIONABLE_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX | 101200 | 41.80 | -5.14 | 210.28 | -5.14 | 270.06 | -5.14 | 2024-07-24 | 374500 | -39.79 |
| R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH | 6990 | 9.30 | -16.17 | 9.30 | -27.47 | 9.30 | -30.04 | 2024-05-08 | 7640 | -41.30 |
| R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP | 8780 | 13.90 | -40.77 | 13.90 | -42.60 | 13.90 | -48.92 | 2024-07-10 | 10000 | -55.15 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C02 Stage2 needs transformer backlog / utility order / customer quality / delivery / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing grid automation or transmission fitting event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE grid-event rows cannot promote without durable order/backlog bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether grid/datacenter CAPEX becomes backlog, capacity and margin.

| symbol | stage quality | explanation |
|---|---|---|
| 267260 | good_stage2_with_later_watch | Transformer backlog and data-center/grid CAPEX bridge produced extreme MFE with shallow MAE. |
| 237750 | bad_stage2 | Grid-automation/protection-relay watch lacked utility-order and margin bridge; forward MFE was low. |
| 017510 | good_4B | Transmission fitting grid premium capped on the July spike and later suffered deep MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 237750 grid automation false Stage2 | 0.91 | 0.91 | false Stage2 due missing utility-order/delivery/margin bridge |
| 017510 transmission fitting cap | 0.88 | 0.88 | good full-window 4B timing after July grid event spike |
| 267260 transformer backlog bridge | n/a | n/a | positive Stage2, but later grid-equipment valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 237750 / 017510
```

No hard 4C candidate is proposed. R1 loop 95 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 power-grid/datacenter CAPEX cases, Stage2 requires verified transformer/order backlog, utility or datacenter customer quality, capacity expansion, delivery cadence, utilization, margin, or revision bridge. Grid, datacenter, power equipment, automation, transmission, relay or smart-grid label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
rule = C02 should split true transformer/grid backlog and datacenter-capex positives from grid-automation false Stage2 and transmission fitting event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 77.83 | -25.07 | 0.67 | mixed; C02 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 77.83 | -25.07 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 grid backlog/order/margin bridge required | 2 | 109.79 | -16.31 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C02 bridge vs event-cap split | 2 | 109.79 | -16.31 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing grid/datacenter themes as positive | 1 | 210.28 | -5.14 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 267260 transformer backlog bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 210.28 | -5.14 | transformer_grid_backlog_datacenter_capex_positive |
| 237750 grid automation false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 9.30 | -27.47 | grid_automation_capex_false_stage2 |
| 017510 transmission fitting cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 13.90 | -42.60 | transmission_fitting_grid_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C02 HD Hyundai Electric transformer/grid/datacenter positive, PNC Tech grid-automation false Stage2, and Semyoung Electric transmission-fitting event-cap 4B split while avoiding top repeated C02 and previous R1 loop93~94 symbols."}
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
residual_error_types_found: transformer_grid_backlog_datacenter_capex_positive, grid_automation_capex_false_stage2, transmission_fitting_grid_event_cap_4B
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
- C02 power-grid/datacenter CAPEX bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,C02_requires_transformer_backlog_customer_capacity_delivery_margin_revision_bridge,0,"C02 Stage2 should require transformer/order backlog, utility/customer quality, datacenter or grid capex linkage, capacity expansion, delivery cadence, margin, or revision bridge, not grid/datacenter/power equipment label alone","HD Hyundai Electric positive worked; PNC Tech and Semyoung Electric event/watch rows failed positive-stage promotion","R1L95_C02_HDHYUNDAIELECTRIC_2024_STAGE2_ACTIONABLE_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX|R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH|R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,cap_bridge_missing_grid_automation_and_transmission_event_premiums_as_4B_watch,0,"Grid automation/transmission fitting event premiums can peak before utility order, delivery and margin bridge is proven","PNC Tech had low forward MFE after a capex watch; Semyoung Electric showed 4B event-cap behavior after July grid spike","R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH|R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,block_positive_stage_when_grid_theme_has_high_or_persistent_MAE_without_order_margin_bridge,0,"High or persistent MAE after bridge-missing grid/datacenter entries should block Stage2/Stage3 promotion unless customer order, delivery and margin evidence survives","PNC Tech MAE90=-27.47 and Semyoung Electric MAE90=-42.60","R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH|R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L95_C02_HDHYUNDAIELECTRIC_2024_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_POSITIVE", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP", "case_type": "structural_success_with_later_grid_equipment_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L95_C02_HDHYUNDAIELECTRIC_2024_STAGE2_ACTIONABLE_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Transformer/power-grid backlog, data-center/grid CAPEX and customer-capacity bridge produced extreme 30D/90D/180D MFE with shallow initial MAE. C02 works when grid/datacenter narrative maps into verified transformer backlog, customer quality, capacity expansion, delivery cadence, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C02_positive_requires_transformer_backlog_customer_capacity_delivery_margin_revision_bridge_not_grid_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017~2019 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L95_C02_PNCTECH_2024_GRID_AUTOMATION_CAPEX_FALSE_STAGE2", "symbol": "237750", "company_name": "피앤씨테크", "round": "R1", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP", "case_type": "failed_rerating_grid_automation_capex_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Grid-automation/protection-relay CAPEX watch produced only a short event premium and then drew down. C02 Stage2 should not be awarded without confirmed utility/customer order, datacenter or grid capex linkage, delivery backlog, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_grid_automation_capex_watch_counts_without_customer_order_delivery_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R1L95_C02_SEMYOUNGELECTRIC_2024_TRANSMISSION_FITTING_GRID_EVENT_CAP_4B", "symbol": "017510", "company_name": "세명전기", "round": "R1", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Transmission fitting / small-cap grid event premium capped on the July spike and then suffered deep 30D/90D/180D MAE. C02 should route bridge-missing transmission/grid event premiums to 4B unless confirmed utility order, backlog, capacity utilization, delivery cadence, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_transmission_fitting_grid_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996~1999 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L95_C02_HDHYUNDAIELECTRIC_2024_STAGE2_ACTIONABLE_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX", "case_id": "R1L95_C02_HDHYUNDAIELECTRIC_2024_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_POSITIVE", "symbol": "267260", "company_name": "HD현대일렉트릭", "round": "R1", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP", "sector": "transformer_power_grid_datacenter_capex_backlog", "primary_archetype": "transformer_backlog_customer_capacity_delivery_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 101200.0, "evidence_available_at_that_date": "transformer/power-grid backlog, datacenter and grid capex expansion, customer capacity expansion, delivery cadence and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["transformer_backlog_proxy", "datacenter_grid_capex_proxy", "customer_quality_proxy", "capacity_delivery_cadence_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["extreme_MFE30", "extreme_MFE90", "extreme_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_grid_equipment_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv", "profile_path": "atlas/symbol_profiles/267/267260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 41.8, "MFE_90D_pct": 210.28, "MFE_180D_pct": 270.06, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.14, "MAE_90D_pct": -5.14, "MAE_180D_pct": -5.14, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-24", "peak_price": 374500.0, "drawdown_after_peak_pct": -39.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_grid_equipment_valuation_4B_watch_needed", "four_b_evidence_type": ["transformer_backlog_bridge", "datacenter_grid_capex", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_transformer_grid_backlog_datacenter_capex_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_2019_CA", "same_entry_group_id": "R1L95_C02_267260_2024-01-24_101200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH", "case_id": "R1L95_C02_PNCTECH_2024_GRID_AUTOMATION_CAPEX_FALSE_STAGE2", "symbol": "237750", "company_name": "피앤씨테크", "round": "R1", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP", "sector": "grid_automation_protection_relay_capex_watch", "primary_archetype": "grid_automation_watch_without_utility_order_delivery_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-08", "entry_date": "2024-05-08", "entry_price": 6990.0, "evidence_available_at_that_date": "grid-automation/protection-relay capex and smart-grid watch without confirmed utility/customer order, delivery backlog or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["grid_automation_capex_watch", "protection_relay_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "MAE90_after_spike", "utility_order_delivery_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237750/2024.csv", "profile_path": "atlas/symbol_profiles/237/237750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.3, "MFE_90D_pct": 9.3, "MFE_180D_pct": 9.3, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.17, "MAE_90D_pct": -27.47, "MAE_180D_pct": -30.04, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-08", "peak_price": 7640.0, "drawdown_after_peak_pct": -41.3, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "grid_automation_capex_watch_was_false_stage2_due_missing_utility_order_delivery_margin_bridge", "four_b_evidence_type": ["grid_automation_event_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_grid_automation_capex_watch_without_utility_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_grid_automation_capex_watch_counts_without_customer_order_delivery_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R1L95_C02_237750_2024-05-08_6990", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP", "case_id": "R1L95_C02_SEMYOUNGELECTRIC_2024_TRANSMISSION_FITTING_GRID_EVENT_CAP_4B", "symbol": "017510", "company_name": "세명전기", "round": "R1", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP", "sector": "transmission_fitting_grid_event_premium", "primary_archetype": "transmission_fitting_grid_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-07-10", "entry_date": "2024-07-10", "entry_price": 8780.0, "evidence_available_at_that_date": "transmission fitting / small-cap power-grid event premium after July grid spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["transmission_fitting_event", "power_grid_theme_spike", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "utility_order_backlog_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017510/2024.csv", "profile_path": "atlas/symbol_profiles/017/017510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.9, "MFE_90D_pct": 13.9, "MFE_180D_pct": 13.9, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -40.77, "MAE_90D_pct": -42.6, "MAE_180D_pct": -48.92, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-10", "peak_price": 10000.0, "drawdown_after_peak_pct": -55.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing_transmission_fitting_grid_event_cap", "four_b_evidence_type": ["grid_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_transmission_fitting_grid_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_transmission_fitting_grid_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_1999_CA", "same_entry_group_id": "R1L95_C02_017510_2024-07-10_8780", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L95_C02_HDHYUNDAIELECTRIC_2024_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_POSITIVE", "trigger_id": "R1L95_C02_HDHYUNDAIELECTRIC_2024_STAGE2_ACTIONABLE_TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX", "symbol": "267260", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 75, "margin_bridge_score": 65, "revision_score": 65, "relative_strength_score": 85, "customer_quality_score": 70, "policy_or_regulatory_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "transformer_grid_backlog_datacenter_capex_positive", "MFE_90D_pct": 210.28, "MAE_90D_pct": -5.14, "score_return_alignment_label": "transformer_grid_backlog_datacenter_capex_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L95_C02_PNCTECH_2024_GRID_AUTOMATION_CAPEX_FALSE_STAGE2", "trigger_id": "R1L95_C02_PNCTECH_2024_STAGE2_FALSE_POSITIVE_GRID_AUTOMATION_CAPEX_WATCH", "symbol": "237750", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "grid_automation_capex_false_stage2", "MFE_90D_pct": 9.3, "MAE_90D_pct": -27.47, "score_return_alignment_label": "grid_automation_capex_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_grid_automation_capex_watch_counts_without_customer_order_delivery_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L95_C02_SEMYOUNGELECTRIC_2024_TRANSMISSION_FITTING_GRID_EVENT_CAP_4B", "trigger_id": "R1L95_C02_SEMYOUNGELECTRIC_2024_STAGE4B_TRANSMISSION_FITTING_GRID_EVENT_CAP", "symbol": "017510", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "transmission_fitting_grid_event_cap_4B_guard", "MFE_90D_pct": 13.9, "MAE_90D_pct": -42.6, "score_return_alignment_label": "transmission_fitting_grid_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_transmission_fitting_grid_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "95", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_GRID_AUTOMATION_FALSE_STAGE2_AND_TRANSMISSION_FITTING_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["transformer_grid_backlog_datacenter_capex_positive", "grid_automation_capex_false_stage2", "transmission_fitting_grid_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C02 rows need explicit transformer/order backlog, utility/datacenter customer quality, capacity, delivery, utilization, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C02 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 95
next_round = R2
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
