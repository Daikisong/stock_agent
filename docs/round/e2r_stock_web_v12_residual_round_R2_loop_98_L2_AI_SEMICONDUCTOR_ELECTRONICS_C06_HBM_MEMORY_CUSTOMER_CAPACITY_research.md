# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | HBM_customer_capacity_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_98_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. The duplicate C07 artifact produced during this run is not the final artifact because C07 was already finalized immediately before. After local C08/C09/C01/C07 supplementation, C06 is the next thin Priority 0 archetype.

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
HBM_customer_capacity_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 98
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C06 is a customer-capacity and HBM mix archetype. The word “HBM” is only the label on the wafer box; the usable signal is named customer capacity, HBM mix, supply allocation, ASP, FCF/margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY = 21 rows / Priority 0
previous R2 loop-97 C06 symbols avoided: 031980, 036540, 080220
recent local C08/C09/C01/C07 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C06 trigger families:

```text
000660 / Stage2-Actionable / 2024-02-06
067310 / Stage2-Actionable / 2024-04-04
254490 / Stage4B / 2024-04-02
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
| 000660 | atlas/symbol_profiles/000/000660.json | selected 2024 window clean after old 1998~2003 CA candidates |
| 067310 | atlas/symbol_profiles/067/067310.json | selected 2024 window clean after old 2009/2021 CA candidates |
| 254490 | atlas/symbol_profiles/254/254490.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L98_C06_SKHYNIX_2024_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_POSITIVE | 000660 | 2024-02-06 | yes | 180 | yes | yes | true |
| R2L98_C06_HANAMICRON_2024_OSAT_HBM_CAPA_HIGH_MAE_FALSE_STAGE2 | 067310 | 2024-04-04 | yes | 180 | yes | yes | true |
| R2L98_C06_MIRAESCM_2024_MEMORY_DISTRIBUTION_HBM_EVENT_CAP_4B | 254490 | 2024-04-02 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE | Positive Stage2 requires named customer capacity, HBM mix, supply allocation, ASP, FCF/margin and revision bridge. |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | OSAT_HBM_CAPA_HIGH_MAE_FALSE_STAGE2 | OSAT/HBM capacity watch without customer call-off and utilization/margin bridge can become false Stage2. |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | MEMORY_DISTRIBUTION_EVENT_CAP_4B | Memory distributor HBM premium should route to 4B when allocation, inventory and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L98_C06_SKHYNIX_2024_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_POSITIVE | 000660 | SK하이닉스 | positive | HBM customer capacity/mix bridge produced strong 30D/90D/180D MFE with shallow early MAE. |
| R2L98_C06_HANAMICRON_2024_OSAT_HBM_CAPA_HIGH_MAE_FALSE_STAGE2 | 067310 | 하나마이크론 | counterexample | OSAT/HBM capacity watch had low MFE and high MAE without customer call-off/utilization bridge. |
| R2L98_C06_MIRAESCM_2024_MEMORY_DISTRIBUTION_HBM_EVENT_CAP_4B | 254490 | 미래반도체 | counterexample / 4B | Memory-distribution HBM sympathy premium capped at the early-April spike and later de-rated. |

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
| SK hynix HBM customer-capacity/mix bridge | historical public/report proxy | true | true | shadow-only positive |
| Hana Micron OSAT/HBM capacity false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Mirae Semiconductor memory-distribution HBM event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000660 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | atlas/symbol_profiles/000/000660.json |
| 067310 | atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv | atlas/symbol_profiles/067/067310.json |
| 254490 | atlas/ohlcv_tradable_by_symbol_year/254/254490/2024.csv | atlas/symbol_profiles/254/254490.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L98_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE | 000660 | Stage2-Actionable | 2024-02-06 | 138000 | positive | HBM customer-capacity/mix bridge worked |
| R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH | 067310 | Stage2-Actionable | 2024-04-04 | 33300 | counterexample | OSAT/HBM capacity false Stage2 |
| R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP | 254490 | Stage4B | 2024-04-02 | 21650 | counterexample/4B | memory-distribution HBM event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L98_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE | 138000 | 33.26 | -4.35 | 76.09 | -4.35 | 80.07 | -4.35 | 2024-07-11 | 248500 | -41.45 |
| R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH | 33300 | 3.60 | -18.47 | 3.60 | -41.29 | 3.60 | -43.39 | 2024-04-04 | 34500 | -43.33 |
| R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP | 21650 | 10.85 | -9.56 | 10.85 | -23.79 | 10.85 | -25.40 | 2024-04-02 | 24000 | -32.08 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C06 Stage2 needs named customer CAPA / HBM mix / ASP / supply allocation / FCF-margin / revision bridge |
| HBM_customer_capacity_guardrail | strengthen: HBM or memory labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing OSAT and memory-distribution premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C06 rows cannot promote without durable customer-capacity bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether HBM memory narrative becomes customer-capacity and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 000660 | good_stage2_with_later_watch | HBM capacity/mix bridge produced strong MFE and shallow MAE, but later valuation watch remains necessary. |
| 067310 | bad_stage2 | OSAT/HBM capacity watch lacked customer call-off/utilization bridge and produced low MFE with high MAE. |
| 254490 | good_4B | Memory-distribution HBM premium peaked at the early-April event high and later drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 067310 OSAT HBM capacity false Stage2 | 0.97 | 0.97 | false Stage2 due missing customer call-off / utilization / mix / margin bridge |
| 254490 memory distribution HBM cap | 0.90 | 0.90 | good full-window 4B timing after memory-distribution HBM sympathy premium |
| 000660 HBM memory capacity bridge | n/a | n/a | positive Stage2, but later HBM memory valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 067310 / 254490
```

No hard 4C candidate is introduced in this C06 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 HBM memory customer-capacity cases, Stage2 requires verified named customer capacity, HBM mix, supply allocation, ASP expansion, FCF or margin conversion, and revision bridge. HBM, memory, OSAT capacity, packaging, memory distribution or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
rule = C06 should split true customer-capacity/HBM-mix/margin positives from OSAT capacity false Stage2 and memory-distribution event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 30.18 | -23.14 | 0.67 | mixed; C06 bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 30.18 | -23.14 | 0.67 | weaker C06 bridge split |
| P1 sector_specific_candidate_profile | L2 customer-capacity/mix bridge required | 2 | 39.85 | -14.07 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C06 bridge vs event-cap split | 2 | 39.85 | -14.07 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing HBM memory themes as positive | 1 | 76.09 | -4.35 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 000660 HBM capacity bridge | 66 | Stage2-Watch | 82 | Stage2-Actionable | 76.09 | -4.35 | HBM_customer_capacity_positive |
| 067310 OSAT HBM false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 3.60 | -41.29 | OSAT_HBM_capacity_false_stage2 |
| 254490 memory distribution cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 10.85 | -23.79 | memory_distribution_HBM_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C06 is Priority 0 with 21 rows in the No-Repeat index and remains thin after local C08/C09/C01/C07 supplementation. This run adds SK hynix, Hana Micron, and Mirae Semiconductor rows while avoiding previous C06 symbols 031980, 036540, 080220."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, HBM_customer_capacity_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: HBM_customer_capacity_positive, OSAT_HBM_capacity_false_stage2, memory_distribution_HBM_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, HBM_customer_capacity_guardrail, high_MAE_guardrail
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
- C06 HBM memory customer-capacity bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,configured,C06_requires_customer_CAPA_HBM_mix_ASP_FCF_margin_revision_bridge,0,"C06 Stage2 should require named customer capacity, HBM mix, supply allocation, ASP, FCF/margin, and revision bridge, not HBM/memory label alone","SK hynix positive worked; Hana Micron and Mirae Semiconductor event/watch rows failed positive-stage promotion","R2L98_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE|R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH|R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,configured,cap_bridge_missing_OSAT_and_memory_distribution_HBM_event_premiums_as_4B_watch,0,"OSAT capacity and memory-distribution premiums can peak before customer call-off, utilization, ASP spread, inventory and margin bridge is proven","Hana Micron had low MFE and high MAE after OSAT capacity watch; Mirae Semiconductor showed 4B event-cap behavior after the early-April HBM sympathy spike","R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH|R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,configured,block_positive_stage_when_HBM_memory_theme_has_high_or_persistent_MAE_without_customer_capacity_bridge,0,"High or persistent MAE after bridge-missing C06 entries should block Stage2/Stage3 promotion unless customer capacity, HBM mix and margin evidence survives","Hana Micron MAE90=-41.29 and Mirae Semiconductor MAE90=-23.79","R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH|R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L98_C06_SKHYNIX_2024_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_POSITIVE", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP", "case_type": "structural_success_with_later_HBM_memory_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L98_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM memory customer-capacity and mix bridge produced strong 30D/90D/180D MFE with shallow early MAE. C06 works when HBM narrative maps into named customer capacity, HBM mix, ASP, supply allocation, FCF/margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C06_positive_requires_customer_CAPA_HBM_mix_ASP_FCF_margin_revision_bridge_not_HBM_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1998~2003 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L98_C06_HANAMICRON_2024_OSAT_HBM_CAPA_HIGH_MAE_FALSE_STAGE2", "symbol": "067310", "company_name": "하나마이크론", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP", "case_type": "failed_rerating_OSAT_HBM_capacity_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "OSAT / HBM-capacity watch after the April spike had only small forward MFE and then severe drawdown. C06 Stage2 should not be awarded without customer call-off, capacity utilization, package/test mix, ASP, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_OSAT_HBM_capacity_watch_counts_without_customer_calloff_utilization_mix_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2009/2021 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R2L98_C06_MIRAESCM_2024_MEMORY_DISTRIBUTION_HBM_EVENT_CAP_4B", "symbol": "254490", "company_name": "미래반도체", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Memory distribution / HBM sympathy event premium capped after the early-April spike and then de-rated. C06 should route bridge-missing memory distributor premiums to 4B unless customer capacity allocation, inventory turns, ASP spread, revenue conversion, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_memory_distribution_HBM_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L98_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE", "case_id": "R2L98_C06_SKHYNIX_2024_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_POSITIVE", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP", "sector": "HBM_memory_customer_capacity_mix_ASP_margin", "primary_archetype": "customer_CAPA_HBM_mix_ASP_FCF_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | HBM_customer_capacity_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 138000.0, "evidence_available_at_that_date": "HBM memory customer capacity, high-end memory mix, ASP expansion, supply allocation and margin/revision bridge proxy after February base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_CAPA_proxy", "HBM_mix_proxy", "ASP_proxy", "supply_allocation_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "very_strong_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_HBM_memory_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 33.26, "MFE_90D_pct": 76.09, "MFE_180D_pct": 80.07, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.35, "MAE_90D_pct": -4.35, "MAE_180D_pct": -4.35, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 248500.0, "drawdown_after_peak_pct": -41.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_HBM_memory_valuation_4B_watch_needed", "four_b_evidence_type": ["HBM_customer_capacity_bridge", "HBM_mix_ASP", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_HBM_memory_customer_capacity_mix_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1998_1999_2000_2001_2002_2003_CA", "same_entry_group_id": "R2L98_C06_000660_2024-02-06_138000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH", "case_id": "R2L98_C06_HANAMICRON_2024_OSAT_HBM_CAPA_HIGH_MAE_FALSE_STAGE2", "symbol": "067310", "company_name": "하나마이크론", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP", "sector": "OSAT_HBM_capacity_package_test_watch", "primary_archetype": "OSAT_HBM_capacity_watch_without_customer_calloff_utilization_mix_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | HBM_customer_capacity_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-04", "entry_date": "2024-04-04", "entry_price": 33300.0, "evidence_available_at_that_date": "OSAT / HBM package-test capacity watch after April memory spike without confirmed customer call-off, utilization, package/test mix, ASP or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["OSAT_HBM_capacity_watch", "package_test_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "high_MAE90", "customer_calloff_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv", "profile_path": "atlas/symbol_profiles/067/067310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.6, "MFE_90D_pct": 3.6, "MFE_180D_pct": 3.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.47, "MAE_90D_pct": -41.29, "MAE_180D_pct": -43.39, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-04", "peak_price": 34500.0, "drawdown_after_peak_pct": -43.33, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "OSAT_HBM_capacity_watch_was_false_stage2_due_missing_customer_calloff_utilization_mix_margin_bridge", "four_b_evidence_type": ["OSAT_HBM_capacity_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_OSAT_HBM_capacity_watch_without_customer_calloff_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_OSAT_HBM_capacity_watch_counts_without_customer_calloff_utilization_mix_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2009_2021_CA", "same_entry_group_id": "R2L98_C06_067310_2024-04-04_33300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP", "case_id": "R2L98_C06_MIRAESCM_2024_MEMORY_DISTRIBUTION_HBM_EVENT_CAP_4B", "symbol": "254490", "company_name": "미래반도체", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP", "sector": "memory_distribution_HBM_sympathy_event_premium", "primary_archetype": "memory_distribution_HBM_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | HBM_customer_capacity_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-02", "entry_date": "2024-04-02", "entry_price": 21650.0, "evidence_available_at_that_date": "memory distribution / HBM sympathy event premium without confirmed customer allocation, inventory turn, ASP spread, revenue conversion or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["memory_distribution_event", "HBM_sympathy_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "inventory_ASP_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/254/254490/2024.csv", "profile_path": "atlas/symbol_profiles/254/254490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.85, "MFE_90D_pct": 10.85, "MFE_180D_pct": 10.85, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.56, "MAE_90D_pct": -23.79, "MAE_180D_pct": -25.4, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-02", "peak_price": 24000.0, "drawdown_after_peak_pct": -32.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_memory_distribution_HBM_event_cap_due_missing_inventory_ASP_margin_bridge", "four_b_evidence_type": ["memory_distribution_HBM_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_memory_distribution_HBM_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_memory_distribution_HBM_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R2L98_C06_254490_2024-04-02_21650", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C06_SKHYNIX_2024_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_POSITIVE", "trigger_id": "R2L98_C06_SKHYNIX_2024_STAGE2_ACTIONABLE_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 55, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 65, "margin_bridge_score": 65, "revision_score": 65, "relative_strength_score": 80, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "HBM_memory_customer_capacity_mix_positive", "MFE_90D_pct": 76.09, "MAE_90D_pct": -4.35, "score_return_alignment_label": "HBM_customer_capacity_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C06_HANAMICRON_2024_OSAT_HBM_CAPA_HIGH_MAE_FALSE_STAGE2", "trigger_id": "R2L98_C06_HANAMICRON_2024_STAGE2_FALSE_POSITIVE_OSAT_HBM_CAPA_WATCH", "symbol": "067310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "OSAT_HBM_capacity_false_stage2", "MFE_90D_pct": 3.6, "MAE_90D_pct": -41.29, "score_return_alignment_label": "OSAT_HBM_capacity_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_OSAT_HBM_capacity_watch_counts_without_customer_calloff_utilization_mix_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C06_MIRAESCM_2024_MEMORY_DISTRIBUTION_HBM_EVENT_CAP_4B", "trigger_id": "R2L98_C06_MIRAESCM_2024_STAGE4B_MEMORY_DISTRIBUTION_HBM_EVENT_CAP", "symbol": "254490", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "memory_distribution_HBM_event_cap_4B_guard", "MFE_90D_pct": 10.85, "MAE_90D_pct": -23.79, "score_return_alignment_label": "memory_distribution_HBM_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_memory_distribution_HBM_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_MIX_BRIDGE_VS_OSAT_CAPA_HIGH_MAE_FALSE_STAGE2_AND_MEMORY_DISTRIBUTION_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "HBM_customer_capacity_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["HBM_customer_capacity_positive", "OSAT_HBM_capacity_false_stage2", "memory_distribution_HBM_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C06 rows need explicit named customer capacity, HBM mix, supply allocation, ASP expansion, FCF/margin conversion and revision bridge before positive promotion.
- In C06, bridge-missing HBM memory event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C06 HBM memory customer-capacity rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R2
completed_loop = 98
completed_canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
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
