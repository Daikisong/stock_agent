# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_4b_watch_guard | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_91_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
```

This file is the corrected final output for this execution. The immediately previous tool run recreated an R1/C02 file, but the actual scheduler state after R1 loop 91 is R2 / loop 91. This round fills the under-covered C06 HBM memory/customer-capacity archetype.

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
scheduled_round = R2
scheduled_loop = 91
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 91
```

R2 permits L2 AI/semiconductor/electronics research. Previous R2 loop 90 used C07 HBM equipment/order, so this loop shifts upstream to C06 memory customer-capacity and contrasts true HBM capacity evidence against memory-adjacent theme spikes.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY = 7 rows / 6 symbols / good-bad Stage2 4-1 / 4B-4C 0-0
top covered symbols include 000660(2), 005930(1), 009150(1), 014680(1), 067310(1), 402340(1)
previous R2 loop-90 C07 symbols avoided: 232140, 036200, 039440
previous R1 loop-91 C02 symbols avoided: 298040, 119850, 010120
```

Selected rows avoid hard duplicates:

```text
000660 / Stage2-Actionable / 2024-02-22
080220 / Stage2-Actionable / 2024-01-24
253590 / Stage4B / 2024-07-04
```

`000660` is a soft expansion because it is a known C06 anchor, so its independent evidence weight is reduced to 0.75. `080220` and `253590` are new C06 symbols in this fine split.

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
| 000660 | atlas/symbol_profiles/000/000660.json | selected 2024 window clean after old CA candidates |
| 080220 | atlas/symbol_profiles/080/080220.json | selected 2024 window clean after 2009-07-24 CA |
| 253590 | atlas/symbol_profiles/253/253590.json | selected 2024/2025 window clean after 2019-01-31 SPAC/merger CA |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L91_C06_SKHYNIX_2024_HBM_CUSTOMER_CAPACITY_BRIDGE_POSITIVE | 000660 | 2024-02-22 | yes | 180 | yes | yes | true |
| R2L91_C06_JEJUSEMI_2024_ONDEVICE_AI_MEMORY_THEME_FALSE_STAGE2 | 080220 | 2024-01-24 | yes | 180 | yes | yes | true |
| R2L91_C06_NEOSEM_2024_CXL_SSD_MEMORY_TEST_THEME_EVENT_CAP_4B | 253590 | 2024-07-04 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE | Positive Stage2 requires HBM customer allocation, capacity tightness, ASP/mix, and revision bridge. |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | ONDEVICE_AI_MEMORY_FALSE_STAGE2 | On-device AI/low-power memory label without HBM capacity bridge can become high-MAE false Stage2. |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | CXL_SSD_MEMORY_THEME_EVENT_CAP_4B | CXL/SSD/memory-test premium should route to 4B when capacity/order bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L91_C06_SKHYNIX_2024_HBM_CUSTOMER_CAPACITY_BRIDGE_POSITIVE | 000660 | SK하이닉스 | positive | HBM customer-capacity bridge produced strong MFE with shallow early MAE. |
| R2L91_C06_JEJUSEMI_2024_ONDEVICE_AI_MEMORY_THEME_FALSE_STAGE2 | 080220 | 제주반도체 | counterexample | On-device AI memory theme had limited MFE and severe MAE. |
| R2L91_C06_NEOSEM_2024_CXL_SSD_MEMORY_TEST_THEME_EVENT_CAP_4B | 253590 | 네오셈 | counterexample / 4B | CXL/SSD memory-test theme premium capped and then de-rated. |

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
| SK Hynix HBM capacity bridge | historical public/report proxy | true | true | shadow-only positive |
| Jeju Semiconductor AI memory false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| NeoSem CXL/SSD memory cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000660 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | atlas/symbol_profiles/000/000660.json |
| 080220 | atlas/ohlcv_tradable_by_symbol_year/080/080220/2024.csv | atlas/symbol_profiles/080/080220.json |
| 253590 | atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv; 2025.csv | atlas/symbol_profiles/253/253590.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L91_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_CUSTOMER_CAPACITY_BRIDGE | 000660 | Stage2-Actionable | 2024-02-22 | 156500 | positive | HBM customer-capacity bridge worked |
| R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME | 080220 | Stage2-Actionable | 2024-01-24 | 33800 | counterexample | AI memory theme false Stage2 |
| R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP | 253590 | Stage4B | 2024-07-04 | 15530 | counterexample/4B | CXL/SSD memory theme event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L91_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_CUSTOMER_CAPACITY_BRIDGE | 156500 | 21.73 | -2.04 | 58.79 | -2.04 | 58.79 | -17.38 | 2024-07-11 | 248500 | -47.97 |
| R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME | 33800 | 14.05 | -34.32 | 14.05 | -38.91 | 14.05 | -66.30 | 2024-01-25 | 38550 | -70.45 |
| R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP | 15530 | 11.20 | -44.56 | 11.20 | -52.22 | 11.20 | -52.22 | 2024-07-04 | 17270 | -57.03 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C06 Stage2 needs HBM customer-capacity / ASP / revision bridge |
| local_4b_watch_guard | strengthen: memory-adjacent theme premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE memory-theme rows cannot promote without durable customer-capacity bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is HBM customer-capacity bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 000660 | good_stage2 | HBM customer-capacity/revision bridge produced strong MFE with shallow early MAE. |
| 080220 | bad_stage2 | On-device AI memory theme lacked HBM customer-capacity bridge and drew down severely. |
| 253590 | good_4B | CXL/SSD memory-theme premium capped and then de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 080220 AI memory false Stage2 | 0.88 | 0.88 | on-device AI memory theme spike was false Stage2 due missing HBM customer-capacity bridge |
| 253590 CXL/SSD memory cap | 1.00 | 1.00 | good full-window 4B timing |
| 000660 HBM capacity bridge | n/a | n/a | positive Stage2, but later HBM memory valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 080220 / 253590
```

No hard 4C candidate is proposed. R2 loop 91 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 HBM memory/customer-capacity cases, Stage2 requires verified HBM customer allocation, capacity tightness, delivery schedule, ASP/mix, gross-margin recovery, or revision bridge. AI memory, on-device AI, CXL, SSD, or memory-test theme label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
rule = C06 should split true HBM customer-capacity positives from AI-memory false Stage2 and CXL/SSD memory-theme event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 28.01 | -31.06 | 0.67 | mixed; C06 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 28.01 | -31.06 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L2 HBM customer-capacity bridge required | 2 | 36.42 | -20.48 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C06 bridge vs event-cap split | 2 | 36.42 | -20.48 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing memory themes as positive | 1 | 58.79 | -2.04 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 000660 HBM capacity bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 58.79 | -2.04 | HBM_customer_capacity_bridge_positive |
| 080220 AI memory false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 14.05 | -38.91 | AI_memory_theme_false_stage2 |
| 253590 CXL/SSD cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.20 | -52.22 | CXL_SSD_memory_theme_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C06 HBM customer-capacity positive, on-device AI memory false Stage2, and CXL/SSD memory-theme event-cap 4B split."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: HBM_customer_capacity_bridge_positive, AI_memory_theme_false_stage2, CXL_SSD_memory_theme_event_cap_4B
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
- C06 HBM memory customer-capacity bridge vs memory-theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,configured,C06_requires_HBM_customer_capacity_ASP_revision_bridge,0,"C06 Stage2 should require HBM customer allocation, capacity tightness, ASP/mix, delivery, margin, or revision bridge, not AI-memory or memory-theme label alone","SK Hynix positive worked; Jeju Semiconductor and NeoSem theme/event rows failed positive-stage promotion","R2L91_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_CUSTOMER_CAPACITY_BRIDGE|R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME|R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,configured,cap_memory_adjacent_theme_premiums_as_4B_watch,0,"On-device AI memory, CXL, SSD, and memory-test premiums can peak before HBM customer-capacity evidence appears","Jeju Semiconductor had severe drawdown after theme spike; NeoSem showed full-window 4B event-cap behavior","R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME|R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,configured,block_positive_stage_when_memory_theme_has_high_MAE_without_customer_capacity_bridge,0,"High MAE after memory-adjacent theme spike should block Stage2/Stage3 promotion unless HBM customer-capacity and revision evidence survives","Jeju Semiconductor MAE180=-66.30 and NeoSem MAE90=-52.22","R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME|R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L91_C06_SKHYNIX_2024_HBM_CUSTOMER_CAPACITY_BRIDGE_POSITIVE", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "91", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP", "case_type": "structural_success_soft_expansion", "positive_or_counterexample": "positive", "best_trigger": "R2L91_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_CUSTOMER_CAPACITY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Soft expansion: 000660 already appears in C06 coverage, but this row uses a new entry date / HBM customer-capacity bridge family and is not a hard duplicate.", "independent_evidence_weight": 0.75, "score_price_alignment": "HBM memory customer capacity / high-quality customer demand bridge produced strong 30D/90D/180D MFE with shallow early MAE. C06 works when memory price recovery is backed by HBM customer allocation, capacity tightness, and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C06_positive_requires_customer_capacity_revision_bridge_not_memory_label_only", "price_source": "Songdaiki/stock-web", "notes": "Modern 2024 window clean after old corporate-action candidates. Reduced weight because 000660 is a known C06 anchor symbol."}
{"row_type": "case", "case_id": "R2L91_C06_JEJUSEMI_2024_ONDEVICE_AI_MEMORY_THEME_FALSE_STAGE2", "symbol": "080220", "company_name": "제주반도체", "round": "R2", "loop": "91", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP", "case_type": "failed_rerating_high_mae_theme", "positive_or_counterexample": "counterexample", "best_trigger": "R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "On-device AI / low-power memory theme spike had only limited forward MFE and then severe 90D/180D MAE. C06 Stage2 should not be awarded unless HBM-grade customer capacity, ASP, and revision bridge are verified.", "current_profile_verdict": "current_profile_false_positive_if_AI_memory_theme_counts_without_HBM_customer_capacity_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2009 CA candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R2L91_C06_NEOSEM_2024_CXL_SSD_MEMORY_TEST_THEME_EVENT_CAP_4B", "symbol": "253590", "company_name": "네오셈", "round": "R2", "loop": "91", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "CXL/SSD memory-test theme premium capped around the July spike and then de-rated sharply. Memory-adjacent theme premium should route to 4B unless customer capacity, order, and margin/revision bridge are visible.", "current_profile_verdict": "current_profile_4B_too_late_if_CXL_SSD_memory_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024/2025 window clean after 2019 SPAC/merger CA candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L91_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_CUSTOMER_CAPACITY_BRIDGE", "case_id": "R2L91_C06_SKHYNIX_2024_HBM_CUSTOMER_CAPACITY_BRIDGE_POSITIVE", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "91", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP", "sector": "HBM_memory_customer_capacity", "primary_archetype": "HBM_customer_allocation_capacity_ASP_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_4b_watch_guard | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 156500.0, "evidence_available_at_that_date": "HBM memory customer demand, customer allocation, capacity tightness, ASP and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["HBM_customer_allocation_proxy", "capacity_tightness", "memory_ASP_recovery_proxy", "revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "very_high_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["valuation_watch_after_HBM_memory_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.73, "MFE_90D_pct": 58.79, "MFE_180D_pct": 58.79, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.04, "MAE_90D_pct": -2.04, "MAE_180D_pct": -17.38, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 248500.0, "drawdown_after_peak_pct": -47.97, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_HBM_memory_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "HBM_memory_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_HBM_customer_capacity_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R2L91_C06_000660_2024-02-22_156500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "soft_expansion_same_C06_symbol_new_entry_date_and_trigger_family", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME", "case_id": "R2L91_C06_JEJUSEMI_2024_ONDEVICE_AI_MEMORY_THEME_FALSE_STAGE2", "symbol": "080220", "company_name": "제주반도체", "round": "R2", "loop": "91", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP", "sector": "ondevice_AI_memory_theme", "primary_archetype": "AI_memory_theme_without_HBM_customer_capacity_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_4b_watch_guard | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 33800.0, "evidence_available_at_that_date": "on-device AI / low-power memory theme spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["AI_memory_theme_spike", "low_power_memory_narrative", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "deep_MAE90", "HBM_customer_capacity_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080220/2024.csv", "profile_path": "atlas/symbol_profiles/080/080220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.05, "MFE_90D_pct": 14.05, "MFE_180D_pct": 14.05, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -34.32, "MAE_90D_pct": -38.91, "MAE_180D_pct": -66.3, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-25", "peak_price": 38550.0, "drawdown_after_peak_pct": -70.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "ondevice_AI_memory_theme_spike_was_false_stage2_due_missing_HBM_customer_capacity_bridge", "four_b_evidence_type": ["AI_memory_theme_premium", "positioning_overheat", "customer_capacity_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_ondevice_AI_memory_theme_without_HBM_customer_capacity_bridge", "current_profile_verdict": "current_profile_false_positive_if_AI_memory_theme_counts_without_HBM_customer_capacity_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R2L91_C06_080220_2024-01-24_33800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP", "case_id": "R2L91_C06_NEOSEM_2024_CXL_SSD_MEMORY_TEST_THEME_EVENT_CAP_4B", "symbol": "253590", "company_name": "네오셈", "round": "R2", "loop": "91", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP", "sector": "CXL_SSD_memory_test_theme", "primary_archetype": "CXL_SSD_memory_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_4b_watch_guard | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-07-04", "entry_date": "2024-07-04", "entry_price": 15530.0, "evidence_available_at_that_date": "CXL/SSD memory-test and memory-cycle premium after July spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["CXL_SSD_memory_theme", "memory_test_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "customer_capacity_order_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv|atlas/ohlcv_tradable_by_symbol_year/253/253590/2025.csv", "profile_path": "atlas/symbol_profiles/253/253590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.2, "MFE_90D_pct": 11.2, "MFE_180D_pct": 11.2, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -44.56, "MAE_90D_pct": -52.22, "MAE_180D_pct": -52.22, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-04", "peak_price": 17270.0, "drawdown_after_peak_pct": -57.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_CXL_SSD_memory_theme_cap", "four_b_evidence_type": ["memory_theme_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_CXL_SSD_memory_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2019_SPAC_CA", "same_entry_group_id": "R2L91_C06_253590_2024-07-04_15530", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L91_C06_SKHYNIX_2024_HBM_CUSTOMER_CAPACITY_BRIDGE_POSITIVE", "trigger_id": "R2L91_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_CUSTOMER_CAPACITY_BRIDGE", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "HBM_customer_capacity_bridge_positive", "MFE_90D_pct": 58.79, "MAE_90D_pct": -2.04, "score_return_alignment_label": "HBM_customer_capacity_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L91_C06_JEJUSEMI_2024_ONDEVICE_AI_MEMORY_THEME_FALSE_STAGE2", "trigger_id": "R2L91_C06_JEJUSEMI_2024_STAGE2_FALSE_POSITIVE_ONDEVICE_AI_MEMORY_THEME", "symbol": "080220", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "AI_memory_theme_false_stage2", "MFE_90D_pct": 14.05, "MAE_90D_pct": -38.91, "score_return_alignment_label": "AI_memory_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_AI_memory_theme_counts_without_HBM_customer_capacity_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L91_C06_NEOSEM_2024_CXL_SSD_MEMORY_TEST_THEME_EVENT_CAP_4B", "trigger_id": "R2L91_C06_NEOSEM_2024_STAGE4B_CXL_SSD_MEMORY_THEME_CAP", "symbol": "253590", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "CXL_SSD_memory_theme_event_cap_4B_guard", "MFE_90D_pct": 11.2, "MAE_90D_pct": -52.22, "score_return_alignment_label": "CXL_SSD_memory_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_CXL_SSD_memory_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "91", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_ONDEVICE_AI_MEMORY_AND_CXL_SSD_THEME_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 2, "same_archetype_new_symbol_count": 2, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["HBM_customer_capacity_bridge_positive", "AI_memory_theme_false_stage2", "CXL_SSD_memory_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R2
completed_loop = 91
next_round = R3
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
