# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_94_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R2 loop 94 is R3 / loop 94. R3 is the L3 battery/EV/green mobility round, and this run fills C12 customer-contract/call-off risk behavior rather than repeating the immediately preceding R3 loop 93 C11 orderbook rerating file.

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
scheduled_round = R3
scheduled_loop = 94
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 94
```

C12 is where a contract headline either becomes a conveyor belt or remains a signboard. The useful split is whether customer call-off, volume durability, capacity utilization and margin bridge actually move together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK = 28 rows / 11 symbols / good-bad Stage2 9-6 / 4B-4C 0-0
top covered symbols include 121600(7), 278280(5), 020150(4), 348370(3), 091580(2), 137400(2)
previous R3 loop-90 C12 symbols avoided: 002710, 290670, 396300
previous R3 loop-91 C14 symbols avoided: 066970, 089980, 336370
previous R3 loop-92 C13 symbols avoided: 006400, 373220, 393890
previous R3 loop-93 C11 symbols avoided: 317330, 382840, 008730
previous R2 loop-94 C07 symbols avoided: 089030, 253590, 425420
```

Selected rows avoid hard duplicates and top repeated C12 symbols:

```text
036830 / Stage2-Actionable / 2024-02-02
418550 / Stage2-Actionable / 2024-02-21
078600 / Stage4B / 2024-06-12
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
| 036830 | atlas/symbol_profiles/036/036830.json | selected 2024 window clean after old 2020 CA candidates |
| 418550 | atlas/symbol_profiles/418/418550.json | no corporate-action candidate |
| 078600 | atlas/symbol_profiles/078/078600.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L94_C12_SOULBRAINHOLDINGS_2024_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_POSITIVE | 036830 | 2024-02-02 | yes | 180 | yes | yes | true |
| R3L94_C12_JEO_2024_CNT_MATERIAL_CALLOFF_FALSE_STAGE2 | 418550 | 2024-02-21 | yes | 180 | yes | yes | true |
| R3L94_C12_DAEJOO_2024_SILICON_ANODE_CALLOFF_EVENT_CAP_4B | 078600 | 2024-06-12 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE | Positive Stage2 requires durable customer call-off, capacity utilization, ASP/mix, margin and revision bridge. |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | CNT_MATERIAL_CALLOFF_FALSE_STAGE2 | CNT/material call-off watch without customer ramp and margin bridge can become false Stage2. |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | SILICON_ANODE_EVENT_CAP_4B | Silicon-anode call-off event premium should route to 4B when qualification/call-off volume and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L94_C12_SOULBRAINHOLDINGS_2024_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_POSITIVE | 036830 | 솔브레인홀딩스 | positive | Customer call-off / capacity / margin bridge produced very high MFE with shallow entry MAE. |
| R3L94_C12_JEO_2024_CNT_MATERIAL_CALLOFF_FALSE_STAGE2 | 418550 | 제이오 | counterexample | CNT call-off watch had short rebound but severe 180D MAE without customer/margin bridge. |
| R3L94_C12_DAEJOO_2024_SILICON_ANODE_CALLOFF_EVENT_CAP_4B | 078600 | 대주전자재료 | counterexample / 4B | Silicon-anode call-off premium capped at the June spike and then de-rated. |

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
| Soulbrain Holdings electrolyte customer call-off bridge | historical public/report proxy | true | true | shadow-only positive |
| JEO CNT material call-off false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Daejoo silicon-anode call-off event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 036830 | atlas/ohlcv_tradable_by_symbol_year/036/036830/2024.csv | atlas/symbol_profiles/036/036830.json |
| 418550 | atlas/ohlcv_tradable_by_symbol_year/418/418550/2024.csv | atlas/symbol_profiles/418/418550.json |
| 078600 | atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv | atlas/symbol_profiles/078/078600.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L94_C12_SOULBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN | 036830 | Stage2-Actionable | 2024-02-02 | 45950 | positive | electrolyte customer call-off/capacity bridge worked |
| R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH | 418550 | Stage2-Actionable | 2024-02-21 | 26650 | counterexample | CNT material call-off false Stage2 |
| R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP | 078600 | Stage4B | 2024-06-12 | 160000 | counterexample/4B | silicon-anode call-off event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L94_C12_SOULBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN | 45950 | 91.08 | -3.48 | 102.83 | -3.48 | 102.83 | -3.48 | 2024-06-10 | 93200 | -34.55 |
| R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH | 26650 | 11.07 | -4.88 | 11.07 | -4.88 | 11.07 | -44.73 | 2024-02-22 | 29600 | -50.24 |
| R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP | 160000 | 2.13 | -16.88 | 2.13 | -42.19 | 2.13 | -42.19 | 2024-06-12 | 163400 | -43.39 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C12 Stage2 needs customer call-off / capacity utilization / ASP / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing call-off event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high or later MAE rows cannot promote without durable customer/margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is call-off bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 036830 | good_stage2_with_later_watch | Call-off/capacity/margin bridge produced very high MFE with shallow entry MAE. |
| 418550 | bad_stage2 | CNT call-off watch lacked durable ramp/margin bridge and later de-rated. |
| 078600 | good_4B | Silicon-anode call-off premium capped at the June spike and then suffered high MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 418550 CNT material false Stage2 | 0.90 | 0.90 | false Stage2 because later 180D MAE exposed missing customer/margin bridge |
| 078600 silicon-anode call-off cap | 0.98 | 0.98 | good full-window 4B timing after June call-off event spike |
| 036830 electrolyte call-off bridge | n/a | n/a | positive Stage2, but later battery-material valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 418550 / 078600
```

No hard 4C candidate is proposed. R3 loop 94 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 customer contract/call-off cases, Stage2 requires verified customer call-off durability, customer ramp, capacity utilization, ASP/mix, margin, or revision bridge. Contract, call-off, qualification, electrolyte, CNT, silicon-anode, material or customer headline alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
rule = C12 should split true call-off/capacity/margin positives from customer-ramp false Stage2 and silicon-anode event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 38.68 | -16.85 | 0.67 | mixed; C12 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 38.68 | -16.85 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 customer call-off/margin bridge required | 2 | 56.95 | -4.18 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C12 bridge vs event-cap split | 2 | 56.95 | -4.18 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery call-off themes as positive | 1 | 102.83 | -3.48 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 036830 electrolyte call-off bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 102.83 | -3.48 | electrolyte_customer_calloff_positive |
| 418550 CNT call-off false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 11.07 | -4.88 | CNT_material_calloff_false_stage2 |
| 078600 silicon-anode cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.13 | -42.19 | silicon_anode_calloff_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C12 electrolyte customer call-off/capacity positive, CNT material call-off false Stage2, and silicon-anode call-off event-cap 4B split while avoiding top repeated C12 symbols."}
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
residual_error_types_found: electrolyte_customer_calloff_positive, CNT_material_calloff_false_stage2, silicon_anode_calloff_event_cap_4B
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
- C12 battery customer contract/call-off bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,configured,C12_requires_customer_calloff_capacity_ASP_utilization_margin_revision_bridge,0,"C12 Stage2 should require durable customer call-off, capacity utilization, ASP/mix, customer ramp, margin, or revision bridge, not contract/call-off/material label alone","Soulbrain Holdings positive worked; JEO and Daejoo event/watch rows failed positive-stage promotion","R3L94_C12_SOULBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN|R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH|R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,configured,cap_bridge_missing_battery_calloff_event_premiums_as_4B_watch,0,"Battery material/customer call-off event premiums can peak before call-off volume and margin bridge is proven","JEO had short MFE then severe later MAE; Daejoo showed 4B event-cap behavior after June silicon-anode spike","R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH|R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,configured,block_positive_stage_when_calloff_theme_has_high_or_later_MAE_without_customer_margin_bridge,0,"High or later-cycle MAE after bridge-missing call-off entries should block Stage2/Stage3 promotion unless call-off, utilization, ASP and margin evidence survives","JEO MAE180=-44.73 and Daejoo MAE90=-42.19","R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH|R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L94_C12_SOULBRAINHOLDINGS_2024_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_POSITIVE", "symbol": "036830", "company_name": "솔브레인홀딩스", "round": "R3", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP", "case_type": "structural_success_with_later_battery_material_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L94_C12_SOULBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Electrolyte / battery-material customer call-off, capacity and margin bridge produced very high 30D/90D/180D MFE with shallow entry MAE. C12 works when the battery contract story maps into customer call-off durability, capacity utilization, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C12_positive_requires_customer_calloff_capacity_margin_revision_bridge_not_contract_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2020 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L94_C12_JEO_2024_CNT_MATERIAL_CALLOFF_FALSE_STAGE2", "symbol": "418550", "company_name": "제이오", "round": "R3", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP", "case_type": "failed_rerating_calloff_durability_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "CNT/battery-material call-off watch produced a short rebound but later suffered severe 180D MAE. C12 Stage2 should not be awarded without confirmed call-off durability, customer ramp, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_CNT_material_calloff_watch_counts_without_customer_ramp_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R3L94_C12_DAEJOO_2024_SILICON_ANODE_CALLOFF_EVENT_CAP_4B", "symbol": "078600", "company_name": "대주전자재료", "round": "R3", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Silicon-anode / battery customer call-off event premium capped around the June spike and then suffered high 90D/180D MAE. C12 should route bridge-missing silicon-anode call-off premiums to 4B unless customer qualification, call-off volume, ASP, utilization and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_silicon_anode_calloff_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L94_C12_SOULBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN", "case_id": "R3L94_C12_SOULBRAINHOLDINGS_2024_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_POSITIVE", "symbol": "036830", "company_name": "솔브레인홀딩스", "round": "R3", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP", "sector": "electrolyte_customer_calloff_capacity_margin", "primary_archetype": "customer_calloff_capacity_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 45950.0, "evidence_available_at_that_date": "electrolyte/battery-material customer call-off durability, capacity utilization, ASP/mix and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_calloff_durability_proxy", "capacity_utilization_proxy", "ASP_mix_bridge_proxy", "margin_revision_bridge_proxy", "relative_strength_confirmation"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "very_high_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_battery_material_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036830/2024.csv", "profile_path": "atlas/symbol_profiles/036/036830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 91.08, "MFE_90D_pct": 102.83, "MFE_180D_pct": 102.83, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.48, "MAE_90D_pct": -3.48, "MAE_180D_pct": -3.48, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-10", "peak_price": 93200.0, "drawdown_after_peak_pct": -34.55, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_battery_material_valuation_4B_watch_needed", "four_b_evidence_type": ["customer_calloff_bridge", "capacity_utilization", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_electrolyte_customer_calloff_capacity_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2020_CA", "same_entry_group_id": "R3L94_C12_036830_2024-02-02_45950", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH", "case_id": "R3L94_C12_JEO_2024_CNT_MATERIAL_CALLOFF_FALSE_STAGE2", "symbol": "418550", "company_name": "제이오", "round": "R3", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP", "sector": "CNT_battery_material_customer_calloff_watch", "primary_archetype": "CNT_material_calloff_watch_without_customer_ramp_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 26650.0, "evidence_available_at_that_date": "CNT/battery-material customer call-off and ramp watch without confirmed durable volume, utilization or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["CNT_material_calloff_watch", "customer_ramp_expectation", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["short_MFE_rebound", "severe_MAE180", "calloff_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/418/418550/2024.csv", "profile_path": "atlas/symbol_profiles/418/418550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.07, "MFE_90D_pct": 11.07, "MFE_180D_pct": 11.07, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.88, "MAE_90D_pct": -4.88, "MAE_180D_pct": -44.73, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 29600.0, "drawdown_after_peak_pct": -50.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "CNT_material_calloff_watch_was_false_stage2_due_missing_customer_ramp_margin_bridge", "four_b_evidence_type": ["battery_material_calloff_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_CNT_material_calloff_without_customer_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_CNT_material_calloff_watch_counts_without_customer_ramp_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R3L94_C12_418550_2024-02-21_26650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP", "case_id": "R3L94_C12_DAEJOO_2024_SILICON_ANODE_CALLOFF_EVENT_CAP_4B", "symbol": "078600", "company_name": "대주전자재료", "round": "R3", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP", "sector": "silicon_anode_customer_calloff_event_premium", "primary_archetype": "silicon_anode_calloff_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-12", "entry_date": "2024-06-12", "entry_price": 160000.0, "evidence_available_at_that_date": "silicon-anode customer call-off / qualification event premium after June spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["silicon_anode_calloff_event", "customer_qualification_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "customer_calloff_ASP_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv", "profile_path": "atlas/symbol_profiles/078/078600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.13, "MFE_90D_pct": 2.13, "MFE_180D_pct": 2.13, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.88, "MAE_90D_pct": -42.19, "MAE_180D_pct": -42.19, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-12", "peak_price": 163400.0, "drawdown_after_peak_pct": -43.39, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_silicon_anode_calloff_event_cap", "four_b_evidence_type": ["silicon_anode_calloff_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_silicon_anode_calloff_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_silicon_anode_calloff_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R3L94_C12_078600_2024-06-12_160000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L94_C12_SOULBRAINHOLDINGS_2024_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_POSITIVE", "trigger_id": "R3L94_C12_SOULBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN", "symbol": "036830", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 55, "policy_or_regulatory_score": 10, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "electrolyte_customer_calloff_positive", "MFE_90D_pct": 102.83, "MAE_90D_pct": -3.48, "score_return_alignment_label": "electrolyte_customer_calloff_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L94_C12_JEO_2024_CNT_MATERIAL_CALLOFF_FALSE_STAGE2", "trigger_id": "R3L94_C12_JEO_2024_STAGE2_FALSE_POSITIVE_CNT_MATERIAL_CALLOFF_WATCH", "symbol": "418550", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "CNT_material_calloff_false_stage2", "MFE_90D_pct": 11.07, "MAE_90D_pct": -4.88, "score_return_alignment_label": "CNT_material_calloff_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_CNT_material_calloff_watch_counts_without_customer_ramp_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L94_C12_DAEJOO_2024_SILICON_ANODE_CALLOFF_EVENT_CAP_4B", "trigger_id": "R3L94_C12_DAEJOO_2024_STAGE4B_SILICON_ANODE_CALLOFF_EVENT_CAP", "symbol": "078600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "silicon_anode_calloff_event_cap_4B_guard", "MFE_90D_pct": 2.13, "MAE_90D_pct": -42.19, "score_return_alignment_label": "silicon_anode_calloff_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_silicon_anode_calloff_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "94", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE_VS_CNT_MATERIAL_CALLOFF_FALSE_STAGE2_AND_SILICON_ANODE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["electrolyte_customer_calloff_positive", "CNT_material_calloff_false_stage2", "silicon_anode_calloff_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C12 rows need explicit customer call-off, ramp, capacity, ASP, utilization, margin or revision bridge before positive promotion.
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
10. Add tests that bridge-missing C12 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 94
next_round = R4
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
