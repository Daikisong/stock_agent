# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_93_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

This file starts loop 93 after the completed R13 loop 92 cross-archetype review. R1 is the L1 industrials / infrastructure / defense / grid round, so this run fills the under-covered C05 EPC mega-contract / margin-gap archetype with a plant-EPC export-order positive, a civil-EPC low-MFE false Stage2, and a power-plant service / EPC event-cap 4B row.

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
scheduled_loop = 93
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 93
```

C05 is comparatively thin in the no-repeat ledger. This loop avoids the top-covered C05 symbols and avoids the recent R1/R11 L1 symbol sets.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP = 10 rows / 9 symbols / good-bad Stage2 3-4 / 4B-4C 0-0
top covered symbols include 053690(2), 002150(1), 011560(1), 023350(1), 023960(1), 054930(1)
previous R1 loop-92 C01 symbols avoided: 082740, 096350, 075580
previous R1 loop-91 C02 symbols avoided: 298040, 119850, 010120
previous R11 loop-92 C04 symbols avoided: 051600, 046120, 006910
previous R11 loop-91 C03 symbols avoided: 012450, 214430, 013810
```

Selected rows avoid hard duplicates and top repeated C05 symbols:

```text
100840 / Stage2-Actionable / 2024-06-03
010960 / Stage2-Actionable / 2024-02-01
094820 / Stage4B / 2024-05-27
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
| 100840 | atlas/symbol_profiles/100/100840.json | entry after 2024-04-16 and 2024-05-17 CA candidates; selected window clean after transition |
| 010960 | atlas/symbol_profiles/010/010960.json | selected 2024 window clean after old 2008/2010 CA candidates |
| 094820 | atlas/symbol_profiles/094/094820.json | selected 2024 window clean after old 2011 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L93_C05_SNTENERGY_2024_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_POSITIVE | 100840 | 2024-06-03 | yes | 180 | yes | yes | true |
| R1L93_C05_SAMHODEV_2024_CIVIL_EPC_ORDER_CATCHUP_FALSE_STAGE2 | 010960 | 2024-02-01 | yes | 180 | yes | yes | true |
| R1L93_C05_ILJINPOWER_2024_POWER_PLANT_SERVICE_EPC_EVENT_CAP_4B | 094820 | 2024-05-27 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE | Positive Stage2 requires firm EPC/project award, order backlog, delivery capacity, execution margin and revision bridge. |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | CIVIL_EPC_FALSE_STAGE2 | Civil EPC / infra order catch-up label without contract-backlog margin bridge can become low-MFE false Stage2. |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | POWER_PLANT_SERVICE_EVENT_CAP_4B | Power-plant service / EPC policy event premium should route to 4B when project and margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L93_C05_SNTENERGY_2024_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_POSITIVE | 100840 | SNT에너지 | positive | Post-transition plant-EPC export order/margin bridge produced very high MFE with controlled MAE. |
| R1L93_C05_SAMHODEV_2024_CIVIL_EPC_ORDER_CATCHUP_FALSE_STAGE2 | 010960 | 삼호개발 | counterexample | Civil EPC catch-up produced low forward MFE and no durable rerating. |
| R1L93_C05_ILJINPOWER_2024_POWER_PLANT_SERVICE_EPC_EVENT_CAP_4B | 094820 | 일진파워 | counterexample / 4B | Power plant service/EPC event premium capped near the May spike and then de-rated severely. |

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
| SNT Energy plant-EPC export order bridge | historical public/report proxy | true | true | shadow-only positive |
| Samho Development civil EPC false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Iljin Power service/EPC event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 100840 | atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv and 2025.csv | atlas/symbol_profiles/100/100840.json |
| 010960 | atlas/ohlcv_tradable_by_symbol_year/010/010960/2024.csv | atlas/symbol_profiles/010/010960.json |
| 094820 | atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv | atlas/symbol_profiles/094/094820.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L93_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE | 100840 | Stage2-Actionable | 2024-06-03 | 10050 | positive | plant EPC export-order margin bridge worked |
| R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP | 010960 | Stage2-Actionable | 2024-02-01 | 3410 | counterexample | civil EPC order catch-up false Stage2 |
| R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP | 094820 | Stage4B | 2024-05-27 | 14170 | counterexample/4B | power plant service EPC event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L93_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE | 10050 | 60.20 | -4.28 | 60.20 | -4.28 | 232.34 | -4.28 | 2025-02-25 | 33400 | -9.13 |
| R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP | 3410 | 3.52 | -3.96 | 6.60 | -6.30 | 7.04 | -9.38 | 2024-07-30 | 3650 | -15.34 |
| R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP | 14170 | 7.27 | -14.47 | 7.27 | -39.94 | 7.27 | -39.94 | 2024-05-29 | 15200 | -44.01 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C05 Stage2 needs firm EPC/project award, order backlog, delivery capacity, execution margin and revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing EPC/policy/service premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE EPC event rows cannot promote without durable project/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is EPC order-backlog and margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 100840 | good_stage2_with_later_watch | Post-transition plant-EPC order/margin bridge produced very high 30D/90D/180D MFE. |
| 010960 | bad_stage2 | Civil EPC order catch-up had low forward MFE and no durable bridge. |
| 094820 | good_4B | Power plant service/EPC event premium capped after May spike and suffered severe MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 010960 civil EPC false Stage2 | 0.93 | 0.93 | low-MFE false Stage2 due missing contract-backlog margin bridge |
| 094820 power plant service EPC cap | 0.93 | 0.93 | good 4B timing after event premium capped and MAE90 reached -39.94 |
| 100840 plant EPC bridge | n/a | n/a | positive Stage2, but later EPC valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 010960 / 094820
```

No hard 4C candidate is proposed. R1 loop 93 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 EPC / mega-contract / project-margin cases, Stage2 requires verified firm EPC/project award, order backlog, delivery capacity, execution margin, contract profitability, or revision bridge. EPC, civil infra, service, policy, nuclear, power-plant, or mega-contract label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rule = C05 should split true EPC order-backlog/margin positives from civil-EPC low-MFE false Stage2 and power-plant service event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 24.69 | -16.84 | 0.67 | mixed; C05 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 24.69 | -16.84 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 EPC order/margin bridge required | 2 | 33.40 | -5.29 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C05 bridge vs event-cap split | 2 | 33.40 | -5.29 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing EPC themes as positive | 1 | 60.20 | -4.28 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 100840 plant EPC bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 60.20 | -4.28 | plant_EPC_export_order_margin_positive |
| 010960 civil EPC false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 6.60 | -6.30 | civil_EPC_order_catchup_false_stage2 |
| 094820 service EPC cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 7.27 | -39.94 | power_plant_service_EPC_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C05 plant EPC export-order margin positive, civil EPC low-MFE false Stage2, and power-plant service EPC event-cap 4B split using non-top-covered C05 symbols."}
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
residual_error_types_found: plant_EPC_export_order_margin_positive, civil_EPC_order_catchup_false_stage2, power_plant_service_EPC_event_cap_4B
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
- C05 EPC mega-contract margin-gap bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,C05_requires_firm_EPC_order_backlog_delivery_margin_revision_bridge,0,"C05 Stage2 should require firm EPC/project award, order backlog, delivery capacity, execution margin, or revision bridge, not EPC/project/policy label alone","SNT Energy positive worked; Samho Development and Iljin Power event/watch rows failed positive-stage promotion","R1L93_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE|R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP|R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,cap_bridge_missing_EPC_policy_and_service_event_premiums_as_4B_watch,0,"EPC/project/service event premiums can peak before order backlog and margin bridge is proven","Samho Development was rangebound with low MFE; Iljin Power showed event-cap behavior after May spike and deep MAE","R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP|R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,block_positive_stage_when_EPC_theme_has_high_MAE_without_project_margin_bridge,0,"High MAE after a bridge-missing EPC/project theme should block Stage2/Stage3 promotion unless project backlog and margin evidence survives","Iljin Power MAE90=-39.94; Samho Development had low forward MFE without backlog margin bridge","R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP|R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L93_C05_SNTENERGY_2024_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_POSITIVE", "symbol": "100840", "company_name": "SNT에너지", "round": "R1", "loop": "93", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP", "case_type": "structural_success_with_corporate_action_guard_and_later_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L93_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Plant equipment / EPC export-order backlog and margin-revision bridge after the 2024 share-count transition produced very high 30D/90D/180D MFE with controlled initial MAE. C05 works when mega-contract narrative maps into order backlog, delivery capacity, execution margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C05_positive_requires_EPC_order_backlog_delivery_margin_revision_bridge_not_contract_label_only", "price_source": "Songdaiki/stock-web", "notes": "Entry deliberately placed after 2024-04-16 and 2024-05-17 corporate-action candidate dates; selected window is clean after transition. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L93_C05_SAMHODEV_2024_CIVIL_EPC_ORDER_CATCHUP_FALSE_STAGE2", "symbol": "010960", "company_name": "삼호개발", "round": "R1", "loop": "93", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP", "case_type": "failed_rerating_civil_EPC_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Civil EPC / infrastructure order catch-up watch produced only low forward MFE and no durable rerating. C05 Stage2 should not be awarded unless contract size, backlog conversion, margin bridge and revision evidence are visible.", "current_profile_verdict": "current_profile_false_positive_if_civil_EPC_order_catchup_counts_without_contract_backlog_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2008/2010 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R1L93_C05_ILJINPOWER_2024_POWER_PLANT_SERVICE_EPC_EVENT_CAP_4B", "symbol": "094820", "company_name": "일진파워", "round": "R1", "loop": "93", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Power plant service / EPC-policy event premium capped around the May spike and then suffered severe MAE. C05 should route bridge-missing power/EPC event premiums to 4B unless firm project award, service backlog, execution margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_power_plant_service_EPC_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2011 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L93_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE", "case_id": "R1L93_C05_SNTENERGY_2024_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_POSITIVE", "symbol": "100840", "company_name": "SNT에너지", "round": "R1", "loop": "93", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP", "sector": "plant_equipment_EPC_export_order_margin", "primary_archetype": "plant_EPC_export_order_backlog_delivery_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-03", "entry_date": "2024-06-03", "entry_price": 10050.0, "evidence_available_at_that_date": "plant equipment / EPC export order backlog, delivery capacity, margin and revision bridge proxy after 2024 corporate-action transition; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["EPC_export_order_proxy", "order_backlog_visibility_proxy", "delivery_capacity_proxy", "margin_revision_bridge_proxy", "post_CA_price_clean_window"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "very_high_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_plant_EPC_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv", "profile_path": "atlas/symbol_profiles/100/100840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 60.2, "MFE_90D_pct": 60.2, "MFE_180D_pct": 232.34, "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -4.28, "MAE_90D_pct": -4.28, "MAE_180D_pct": -4.28, "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-25", "peak_price": 33400.0, "drawdown_after_peak_pct": -9.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_plant_EPC_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "EPC_order_backlog_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_plant_EPC_export_order_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_entry_after_2024-04-16_and_2024-05-17_CA_candidates", "same_entry_group_id": "R1L93_C05_100840_2024-06-03_10050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP", "case_id": "R1L93_C05_SAMHODEV_2024_CIVIL_EPC_ORDER_CATCHUP_FALSE_STAGE2", "symbol": "010960", "company_name": "삼호개발", "round": "R1", "loop": "93", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP", "sector": "civil_EPC_infra_order_catchup_watch", "primary_archetype": "civil_EPC_order_catchup_without_backlog_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 3410.0, "evidence_available_at_that_date": "civil EPC / infrastructure order catch-up and construction recovery watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["civil_EPC_order_catchup_watch", "infra_recovery_theme", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "contract_backlog_margin_bridge_missing", "rangebound_after_spike"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010960/2024.csv", "profile_path": "atlas/symbol_profiles/010/010960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.52, "MFE_90D_pct": 6.6, "MFE_180D_pct": 7.04, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.96, "MAE_90D_pct": -6.3, "MAE_180D_pct": -9.38, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-30", "peak_price": 3650.0, "drawdown_after_peak_pct": -15.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "civil_EPC_order_catchup_was_false_stage2_due_missing_contract_backlog_margin_bridge", "four_b_evidence_type": ["civil_EPC_catchup_premium", "rangebound_low_MFE", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_civil_EPC_order_catchup_without_contract_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_civil_EPC_order_catchup_counts_without_contract_backlog_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2008_2010_CA", "same_entry_group_id": "R1L93_C05_010960_2024-02-01_3410", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP", "case_id": "R1L93_C05_ILJINPOWER_2024_POWER_PLANT_SERVICE_EPC_EVENT_CAP_4B", "symbol": "094820", "company_name": "일진파워", "round": "R1", "loop": "93", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP", "sector": "power_plant_service_EPC_policy_event", "primary_archetype": "power_plant_service_EPC_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-27", "entry_date": "2024-05-27", "entry_price": 14170.0, "evidence_available_at_that_date": "power plant service / EPC policy event premium after May spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["power_plant_service_event", "EPC_policy_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "project_service_backlog_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv", "profile_path": "atlas/symbol_profiles/094/094820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.27, "MFE_90D_pct": 7.27, "MFE_180D_pct": 7.27, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.47, "MAE_90D_pct": -39.94, "MAE_180D_pct": -39.94, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-29", "peak_price": 15200.0, "drawdown_after_peak_pct": -44.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing_power_plant_service_EPC_event_cap", "four_b_evidence_type": ["EPC_policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_power_plant_service_EPC_policy_premium", "current_profile_verdict": "current_profile_4B_too_late_if_power_plant_service_EPC_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_CA", "same_entry_group_id": "R1L93_C05_094820_2024-05-27_14170", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L93_C05_SNTENERGY_2024_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R1L93_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE", "symbol": "100840", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 25, "valuation_repricing_score": 50, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "plant_EPC_export_order_margin_positive", "MFE_90D_pct": 60.2, "MAE_90D_pct": -4.28, "score_return_alignment_label": "plant_EPC_export_order_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L93_C05_SAMHODEV_2024_CIVIL_EPC_ORDER_CATCHUP_FALSE_STAGE2", "trigger_id": "R1L93_C05_SAMHODEV_2024_STAGE2_FALSE_POSITIVE_CIVIL_EPC_ORDER_CATCHUP", "symbol": "010960", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "civil_EPC_order_catchup_false_stage2", "MFE_90D_pct": 6.6, "MAE_90D_pct": -6.3, "score_return_alignment_label": "civil_EPC_order_catchup_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_civil_EPC_order_catchup_counts_without_contract_backlog_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L93_C05_ILJINPOWER_2024_POWER_PLANT_SERVICE_EPC_EVENT_CAP_4B", "trigger_id": "R1L93_C05_ILJINPOWER_2024_STAGE4B_POWER_PLANT_SERVICE_EPC_EVENT_CAP", "symbol": "094820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "power_plant_service_EPC_event_cap_4B_guard", "MFE_90D_pct": 7.27, "MAE_90D_pct": -39.94, "score_return_alignment_label": "power_plant_service_EPC_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_power_plant_service_EPC_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "93", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "PLANT_EPC_EXPORT_ORDER_MARGIN_BRIDGE_VS_CIVIL_EPC_FALSE_STAGE2_AND_POWER_PLANT_SERVICE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["plant_EPC_export_order_margin_positive", "civil_EPC_order_catchup_false_stage2", "power_plant_service_EPC_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
10. Add tests that bridge-missing C05 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 93
next_round = R2
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
