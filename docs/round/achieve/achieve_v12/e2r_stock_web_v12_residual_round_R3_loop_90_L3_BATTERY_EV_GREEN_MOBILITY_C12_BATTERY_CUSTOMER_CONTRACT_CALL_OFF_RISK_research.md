# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
```

This loop continues loop 90 after R2. It adds 3 C12 battery customer-contract / call-off risk cases: one battery can customer-contract bridge positive, one process-equipment customer call-off false Stage2, and one EV parts customer-program 4B event-cap counterexample.

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
scheduled_round = R3
scheduled_loop = 90
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 90
```

R3 permits L3 battery/EV/green mobility research. Previous R3 loop 89 used C11, and R9 loop 89 used C13, so this loop fills C12: customer contract, call-off, reorder, volume, and margin-conversion risk.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK = 28 rows / 11 symbols / good-bad Stage2 9-6 / 4B-4C 0-0
top covered symbols include 121600(7), 278280(5), 020150(4), 348370(3), 091580(2), 137400(2)
previous R3 loop-88 C14 symbols avoided: 361610, 051910, 011790
previous R3 loop-89 C11 symbols avoided: 078600, 382840, 418550
previous R9 loop-89 C13 symbols avoided: 004490, 243840, 393890
```

Selected rows avoid hard duplicates and the top repeated C12 symbols:

```text
002710 / Stage2-Actionable / 2024-01-26
290670 / Stage2-Actionable / 2024-02-21
396300 / Stage4B / 2024-03-08
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
| 002710 | atlas/symbol_profiles/002/002710.json | selected 2024 window clean; CA candidate is 2009-05-08 |
| 290670 | atlas/symbol_profiles/290/290670.json | selected 2024 window clean; CA candidates are 2019-11-06 / 2019-11-26 |
| 396300 | atlas/symbol_profiles/396/396300.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L90_C12_TCCSTEEL_2024_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_POSITIVE | 002710 | 2024-01-26 | yes | 180 | yes | yes | true |
| R3L90_C12_DAEBOMAGNETIC_2024_CUSTOMER_CALLOFF_FALSE_STAGE2 | 290670 | 2024-02-21 | yes | 180 | yes | yes | true |
| R3L90_C12_SEAMECHANICS_2024_EV_PARTS_CUSTOMER_PROGRAM_EVENT_CAP_4B | 396300 | 2024-03-08 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE | Positive Stage2 requires customer contract, reorder, volume, and margin bridge. |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | PROCESS_EQUIPMENT_CALLOFF_FALSE_STAGE2 | Process equipment/call-off recovery label without contract bridge can become false Stage2. |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | EV_PARTS_CUSTOMER_PROGRAM_EVENT_CAP_4B | Customer-program premium should route to 4B when call-off/volume economics are capped or unverified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L90_C12_TCCSTEEL_2024_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_POSITIVE | 002710 | TCC스틸 | positive | Battery can/customer-contract bridge produced strong MFE before later valuation reset. |
| R3L90_C12_DAEBOMAGNETIC_2024_CUSTOMER_CALLOFF_FALSE_STAGE2 | 290670 | 대보마그네틱 | counterexample | Process-equipment/call-off recovery watch had weak MFE and large MAE. |
| R3L90_C12_SEAMECHANICS_2024_EV_PARTS_CUSTOMER_PROGRAM_EVENT_CAP_4B | 396300 | 세아메카닉스 | counterexample / 4B | EV parts customer-program premium capped near the March spike and then de-rated. |

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
| TCC Steel battery can/customer bridge | historical public/report proxy | true | true | shadow-only positive |
| Daebo Magnetic call-off false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Sea Mechanics customer-program cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 002710 | atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv | atlas/symbol_profiles/002/002710.json |
| 290670 | atlas/ohlcv_tradable_by_symbol_year/290/290670/2024.csv | atlas/symbol_profiles/290/290670.json |
| 396300 | atlas/ohlcv_tradable_by_symbol_year/396/396300/2024.csv | atlas/symbol_profiles/396/396300.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L90_C12_TCCSTEEL_2024_STAGE2_ACTIONABLE_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE | 002710 | Stage2-Actionable | 2024-01-26 | 47100 | positive | customer-contract/reorder bridge worked |
| R3L90_C12_DAEBOMAGNETIC_2024_STAGE2_FALSE_POSITIVE_CALLOFF_RISK | 290670 | Stage2-Actionable | 2024-02-21 | 30400 | counterexample | call-off recovery false Stage2 |
| R3L90_C12_SEAMECHANICS_2024_STAGE4B_EV_PARTS_CUSTOMER_PROGRAM_CAP | 396300 | Stage4B | 2024-03-08 | 4080 | counterexample/4B | EV parts customer-program event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L90_C12_TCCSTEEL_2024_STAGE2_ACTIONABLE_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE | 47100 | 82.38 | -6.79 | 82.38 | -6.79 | 82.38 | -42.68 | 2024-02-21 | 85900 | -68.57 |
| R3L90_C12_DAEBOMAGNETIC_2024_STAGE2_FALSE_POSITIVE_CALLOFF_RISK | 30400 | 9.21 | -7.89 | 9.21 | -24.34 | 9.21 | -49.34 | 2024-03-08 | 33200 | -53.61 |
| R3L90_C12_SEAMECHANICS_2024_STAGE4B_EV_PARTS_CUSTOMER_PROGRAM_CAP | 4080 | 4.90 | -11.52 | 4.90 | -22.92 | 4.90 | -43.38 | 2024-03-08 | 4280 | -46.03 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C12 Stage2 needs customer contract / reorder / volume / margin bridge |
| local_4b_watch_guard | strengthen: call-off recovery and customer-program premiums should route to 4B watch when bridge is missing |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is customer-contract bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 002710 | good_stage2 | Customer-contract/reorder bridge produced large MFE before later reset. |
| 290670 | bad_stage2 | Call-off recovery label failed without durable customer/order bridge. |
| 396300 | good_4B | Customer-program premium capped and then de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 290670 call-off false Stage2 | 0.92 | 0.92 | call-off recovery was false Stage2 / event-cap-like |
| 396300 customer-program cap | 1.00 | 1.00 | good full-window 4B timing |
| 002710 customer-contract bridge | n/a | n/a | positive Stage2, but later contract-premium valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 290670 / 396300
```

No hard 4C candidate is proposed. R3 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery customer-contract/call-off cases, Stage2 requires verified customer contract, call-off/order conversion, reorder, volume, utilization, margin, or revision bridge. Battery parts, process equipment, or customer-program label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
rule = C12 should split customer-contract/reorder positives from call-off recovery false Stage2 and customer-program event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 32.16 | -18.02 | 0.67 | mixed; C12 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 32.16 | -18.02 | 0.67 | weaker bridge/call-off guard |
| P1 sector_specific_candidate_profile | L3 customer-contract bridge required | 2 | 45.80 | -15.57 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C12 bridge vs event-cap split | 2 | 45.80 | -15.57 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing customer-program themes as positive | 1 | 82.38 | -6.79 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 002710 customer-contract bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 82.38 | -6.79 | battery_can_customer_contract_bridge_positive |
| 290670 call-off false Stage2 | 66 | Stage2-Actionable | 53 | Stage1/Watch | 9.21 | -24.34 | customer_calloff_recovery_false_stage2 |
| 396300 customer-program cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.90 | -22.92 | EV_parts_customer_program_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C12 battery can/customer contract bridge positive, battery process-equipment customer call-off false Stage2, and EV parts customer-program event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: battery_can_customer_contract_bridge_positive, customer_calloff_recovery_false_stage2, EV_parts_customer_program_event_cap_4B
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
- C12 customer contract / call-off risk bridge vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,configured,C12_requires_customer_contract_reorder_volume_margin_bridge,0,"C12 Stage2 should require verified customer contract, call-off, reorder, volume, utilization, margin, or revision bridge, not battery-parts/customer-program label alone","TCC Steel positive worked; Daebo Magnetic and Sea Mechanics event/call-off rows failed positive-stage promotion","R3L90_C12_TCCSTEEL_2024_STAGE2_ACTIONABLE_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE|R3L90_C12_DAEBOMAGNETIC_2024_STAGE2_FALSE_POSITIVE_CALLOFF_RISK|R3L90_C12_SEAMECHANICS_2024_STAGE4B_EV_PARTS_CUSTOMER_PROGRAM_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,configured,cap_customer_program_and_calloff_premiums_as_4B_watch,0,"Customer-program or call-off recovery premiums can peak before durable customer/volume/margin bridge appears","Daebo Magnetic and Sea Mechanics showed weak MFE with deep 180D MAE after bridge-missing spikes","R3L90_C12_DAEBOMAGNETIC_2024_STAGE2_FALSE_POSITIVE_CALLOFF_RISK|R3L90_C12_SEAMECHANICS_2024_STAGE4B_EV_PARTS_CUSTOMER_PROGRAM_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L90_C12_TCCSTEEL_2024_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_POSITIVE", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R3L90_C12_TCCSTEEL_2024_STAGE2_ACTIONABLE_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Not in top C12 covered symbols; appears as a prior C13-adjacent symbol but selected as a new C12 customer-contract bridge role.", "independent_evidence_weight": 1.0, "score_price_alignment": "Battery can / customer-contract and reorder bridge produced strong 30D/90D MFE with controlled early MAE; later deep drawdown confirms the need for 4B valuation watch after the contract premium run.", "current_profile_verdict": "current_profile_kept_but_C12_positive_requires_customer_contract_reorder_margin_bridge_not_battery_parts_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; 2009 corporate-action candidate is outside window. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L90_C12_DAEBOMAGNETIC_2024_CUSTOMER_CALLOFF_FALSE_STAGE2", "symbol": "290670", "company_name": "대보마그네틱", "round": "R3", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP", "case_type": "failed_rerating_customer_calloff", "positive_or_counterexample": "counterexample", "best_trigger": "R3L90_C12_DAEBOMAGNETIC_2024_STAGE2_FALSE_POSITIVE_CALLOFF_RISK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery process-equipment / customer call-off recovery label produced only small forward MFE and large later MAE; C12 Stage2 should not be awarded without customer contract, utilization, order, or margin bridge.", "current_profile_verdict": "current_profile_false_positive_if_battery_process_equipment_theme_counts_without_customer_contract_reorder_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2019 corporate-action candidates; source-proxy only."}
{"row_type": "case", "case_id": "R3L90_C12_SEAMECHANICS_2024_EV_PARTS_CUSTOMER_PROGRAM_EVENT_CAP_4B", "symbol": "396300", "company_name": "세아메카닉스", "round": "R3", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L90_C12_SEAMECHANICS_2024_STAGE4B_EV_PARTS_CUSTOMER_PROGRAM_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV parts/customer-program premium capped near the March spike and then de-rated; customer-program theme should route to 4B unless confirmed call-off, volume, and margin bridge appears.", "current_profile_verdict": "current_profile_4B_too_late_if_EV_parts_customer_program_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in selected 2024 window; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L90_C12_TCCSTEEL_2024_STAGE2_ACTIONABLE_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE", "case_id": "R3L90_C12_TCCSTEEL_2024_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_POSITIVE", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP", "sector": "battery_can_customer_contract_reorder", "primary_archetype": "battery_can_customer_contract_reorder_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "entry_date": "2024-01-26", "entry_price": 47100.0, "evidence_available_at_that_date": "battery can / customer contract, reorder visibility, and margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_contract_visibility", "battery_can_reorder_proxy", "volume_margin_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "controlled_entry_MAE"], "stage4b_evidence_fields": ["valuation_watch_after_contract_premium_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv", "profile_path": "atlas/symbol_profiles/002/002710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 82.38, "MFE_90D_pct": 82.38, "MFE_180D_pct": 82.38, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.79, "MAE_90D_pct": -6.79, "MAE_180D_pct": -42.68, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-21", "peak_price": 85900.0, "drawdown_after_peak_pct": -68.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_contract_premium_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "customer_contract_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_battery_can_customer_contract_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L90_C12_002710_2024-01-26_47100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "new C12 customer-contract role; not a hard duplicate", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L90_C12_DAEBOMAGNETIC_2024_STAGE2_FALSE_POSITIVE_CALLOFF_RISK", "case_id": "R3L90_C12_DAEBOMAGNETIC_2024_CUSTOMER_CALLOFF_FALSE_STAGE2", "symbol": "290670", "company_name": "대보마그네틱", "round": "R3", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP", "sector": "battery_process_equipment_customer_calloff", "primary_archetype": "customer_calloff_recovery_without_contract_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 30400.0, "evidence_available_at_that_date": "battery process-equipment / customer demand recovery and call-off risk proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_process_equipment_theme", "customer_calloff_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE180", "customer_contract_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/290/290670/2024.csv", "profile_path": "atlas/symbol_profiles/290/290670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.21, "MFE_90D_pct": 9.21, "MFE_180D_pct": 9.21, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.89, "MAE_90D_pct": -24.34, "MAE_180D_pct": -49.34, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-08", "peak_price": 33200.0, "drawdown_after_peak_pct": -53.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "battery_process_equipment_calloff_recovery_was_false_stage2", "four_b_evidence_type": ["price_only", "positioning_overheat", "customer_contract_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_customer_calloff_recovery_without_contract_bridge", "current_profile_verdict": "current_profile_false_positive_if_battery_process_equipment_theme_counts_without_customer_contract_reorder_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L90_C12_290670_2024-02-21_30400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L90_C12_SEAMECHANICS_2024_STAGE4B_EV_PARTS_CUSTOMER_PROGRAM_CAP", "case_id": "R3L90_C12_SEAMECHANICS_2024_EV_PARTS_CUSTOMER_PROGRAM_EVENT_CAP_4B", "symbol": "396300", "company_name": "세아메카닉스", "round": "R3", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP", "sector": "EV_parts_customer_program_calloff", "primary_archetype": "EV_parts_customer_program_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-08", "entry_date": "2024-03-08", "entry_price": 4080.0, "evidence_available_at_that_date": "EV battery parts / customer-program premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EV_parts_customer_program_theme", "relative_strength_spike", "customer_calloff_expectation"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/396/396300/2024.csv", "profile_path": "atlas/symbol_profiles/396/396300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.9, "MFE_90D_pct": 4.9, "MFE_180D_pct": 4.9, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.52, "MAE_90D_pct": -22.92, "MAE_180D_pct": -43.38, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-08", "peak_price": 4280.0, "drawdown_after_peak_pct": -46.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_EV_parts_customer_program_event_cap", "four_b_evidence_type": ["customer_calloff_risk", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_EV_parts_customer_program_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L90_C12_396300_2024-03-08_4080", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L90_C12_TCCSTEEL_2024_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_POSITIVE", "trigger_id": "R3L90_C12_TCCSTEEL_2024_STAGE2_ACTIONABLE_BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 60, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "battery_can_customer_contract_bridge_positive", "MFE_90D_pct": 82.38, "MAE_90D_pct": -6.79, "score_return_alignment_label": "battery_can_customer_contract_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L90_C12_DAEBOMAGNETIC_2024_CUSTOMER_CALLOFF_FALSE_STAGE2", "trigger_id": "R3L90_C12_DAEBOMAGNETIC_2024_STAGE2_FALSE_POSITIVE_CALLOFF_RISK", "symbol": "290670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "customer_calloff_recovery_false_stage2", "MFE_90D_pct": 9.21, "MAE_90D_pct": -24.34, "score_return_alignment_label": "customer_calloff_recovery_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_battery_process_equipment_theme_counts_without_customer_contract_reorder_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L90_C12_SEAMECHANICS_2024_EV_PARTS_CUSTOMER_PROGRAM_EVENT_CAP_4B", "trigger_id": "R3L90_C12_SEAMECHANICS_2024_STAGE4B_EV_PARTS_CUSTOMER_PROGRAM_CAP", "symbol": "396300", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 5, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "EV_parts_customer_program_event_cap_4B_guard", "MFE_90D_pct": 4.9, "MAE_90D_pct": -22.92, "score_return_alignment_label": "EV_parts_customer_program_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_EV_parts_customer_program_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_CAN_CUSTOMER_CONTRACT_BRIDGE_VS_PROCESS_EQUIPMENT_AND_EV_PARTS_CALLOFF_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["battery_can_customer_contract_bridge_positive", "customer_calloff_recovery_false_stage2", "EV_parts_customer_program_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_round = R3
completed_loop = 90
next_round = R4
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
