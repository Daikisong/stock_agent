# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | call_off_risk_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R2 loop 97 is R3 / loop 97. R3 is the L3 battery/EV/green-mobility round, and this run fills C12 battery customer contract / call-off risk rather than repeating the immediately preceding R3 loop 96 C11 orderbook rerating file, R9 loop 96 C29 mobility file, or R9 loop 95 C14 demand-slowdown file.

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
call_off_risk_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 97
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 97
```

C12 is a customer contract and call-off durability archetype. A battery contract headline is the purchase order cover page; the signal only becomes usable when customer quality, call-off durability, delivery cadence, utilization, ASP/mix, margin and revision survive together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK = 28 rows / 11 symbols / good-bad Stage2 9-6 / 4B-4C 0-0
top covered symbols include 121600(7), 278280(5), 020150(4), 348370(3), 091580(2), 137400(2)
previous R3 loop-96 C11 symbols avoided: 006110, 079810, 417010
previous R3 loop-95 C13 symbols avoided: 014820, 093370, 450080
previous R9 loop-95 C14 symbols avoided: 361610, 393890, 025900
previous R9 loop-96 C29 symbols avoided: 204320, 118990, 317120
previous R2 loop-97 C06 symbols avoided: 031980, 036540, 080220
```

Selected rows avoid hard duplicates and top repeated C12 symbols:

```text
011790 / Stage2-Actionable / 2024-02-06
243840 / Stage2-Actionable / 2024-05-17
419050 / Stage4B / 2024-01-11
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
| 011790 | atlas/symbol_profiles/011/011790.json | selected 2024 window clean after old 1998/2001 CA candidates |
| 243840 | atlas/symbol_profiles/243/243840.json | entry after 2024-04-26 CA-candidate boundary; post-boundary 180D window used |
| 419050 | atlas/symbol_profiles/419/419050.json | selected 2024 window clean after old 2023 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L97_C12_SKC_2024_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_POSITIVE | 011790 | 2024-02-06 | yes | 180 | yes | yes | true |
| R3L97_C12_SHINHEUNGSEC_2024_BATTERY_CAP_CALLOFF_FALSE_STAGE2_POST_CA | 243840 | 2024-05-17 | yes | 180 | yes | post-CA clean | true |
| R3L97_C12_SAMGIEV_2024_BATTERY_CASE_EVENT_CAP_4B | 419050 | 2024-01-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE | Positive Stage2 requires customer contract quality, call-off recovery, delivery slot visibility, utilization, ASP/mix, margin and revision bridge. |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | BATTERY_CAP_CALLOFF_FALSE_STAGE2 | Battery cap/component call-off watch without delivery/utilization/margin bridge can become false Stage2. |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | BATTERY_CASE_EVENT_CAP_4B | Battery-case / EV component contract event premium should route to 4B when call-off and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L97_C12_SKC_2024_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_POSITIVE | 011790 | SKC | positive | Copper-foil customer contract bridge produced very strong MFE with shallow early MAE. |
| R3L97_C12_SHINHEUNGSEC_2024_BATTERY_CAP_CALLOFF_FALSE_STAGE2_POST_CA | 243840 | 신흥에스이씨 | counterexample | Post-CA battery cap call-off watch had a short MFE burst and then high 90D/180D MAE. |
| R3L97_C12_SAMGIEV_2024_BATTERY_CASE_EVENT_CAP_4B | 419050 | 삼기이브이 | counterexample / 4B | Battery-case event premium capped on the January spike and then drifted into persistent drawdown. |

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
| SKC copper-foil customer contract bridge | historical public/report proxy | true | true | shadow-only positive |
| Shinheung SEC post-CA battery cap call-off false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Samgi EV battery-case contract event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 011790 | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv | atlas/symbol_profiles/011/011790.json |
| 243840 | atlas/ohlcv_tradable_by_symbol_year/243/243840/2024.csv | atlas/symbol_profiles/243/243840.json |
| 419050 | atlas/ohlcv_tradable_by_symbol_year/419/419050/2024.csv | atlas/symbol_profiles/419/419050.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE | 011790 | Stage2-Actionable | 2024-02-06 | 81100 | positive | copper-foil customer contract bridge worked |
| R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA | 243840 | Stage2-Actionable | 2024-05-17 | 9230 | counterexample | post-CA battery cap call-off false Stage2 |
| R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP | 419050 | Stage4B | 2024-01-11 | 3320 | counterexample/4B | battery-case customer contract event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE | 81100 | 56.97 | -3.45 | 146.61 | -3.45 | 146.61 | -3.45 | 2024-06-18 | 200000 | -47.85 |
| R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA | 9230 | 13.43 | -6.82 | 13.43 | -30.88 | 13.43 | -30.88 | 2024-06-26 | 10470 | -39.06 |
| R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP | 3320 | 3.31 | -17.77 | 3.31 | -24.40 | 3.31 | -32.23 | 2024-01-11 | 3430 | -34.40 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C12 Stage2 needs customer contract quality / call-off durability / delivery / utilization / margin / revision bridge |
| call_off_risk_guardrail | strengthen: post-CA or component rebounds cannot promote unless call-off and delivery evidence survive |
| local_4b_watch_guard | strengthen: bridge-missing battery component contract premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE call-off watch rows block positive promotion |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether customer-contract narrative becomes delivery, call-off and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 011790 | good_stage2_with_later_watch | Customer-contract/call-off bridge produced very strong MFE with shallow MAE. |
| 243840 | bad_stage2 | Post-CA battery cap call-off watch lacked delivery/utilization/margin bridge and later suffered high MAE. |
| 419050 | good_4B | Battery-case contract premium capped on the event spike and later drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 243840 battery cap call-off false Stage2 | 0.88 | 0.88 | false Stage2 due missing customer call-off / delivery / utilization / margin bridge |
| 419050 battery-case event cap | 0.97 | 0.97 | good full-window 4B timing after January battery-component event premium |
| 011790 copper-foil contract bridge | n/a | n/a | positive Stage2, but later copper-foil valuation and call-off watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 243840 / 419050
```

No hard 4C candidate is introduced in this R3 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery customer-contract / call-off risk cases, Stage2 requires verified customer quality, call-off durability/recovery, delivery-slot visibility, utilization, ASP/mix, margin, or revision bridge. Contract, customer, battery component, copper foil, cap assembly, case, EV parts or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
rule = C12 should split true customer-contract/call-off/delivery/margin positives from post-CA call-off false Stage2 and battery-component event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 54.45 | -19.58 | 0.67 | mixed; C12 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 54.45 | -19.58 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L3 customer/call-off/margin bridge required | 2 | 80.02 | -17.17 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C12 bridge vs event-cap split | 2 | 80.02 | -17.17 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery contract themes as positive | 1 | 146.61 | -3.45 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 011790 copper-foil bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 146.61 | -3.45 | copper_foil_customer_contract_positive |
| 243840 cap call-off false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 13.43 | -30.88 | battery_cap_calloff_false_stage2 |
| 419050 battery-case cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 3.31 | -24.40 | battery_case_contract_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C12 SKC copper-foil customer contract positive, Shinheung SEC post-CA battery cap call-off false Stage2, and Samgi EV battery-case contract event-cap 4B while avoiding top repeated C12 and previous R3/R9/R2 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, call_off_risk_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: copper_foil_customer_contract_positive, battery_cap_calloff_false_stage2, battery_case_contract_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, call_off_risk_guardrail, high_MAE_guardrail
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
- C12 battery customer contract / call-off risk bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,configured,C12_requires_customer_quality_calloff_delivery_utilization_margin_revision_bridge,0,"C12 Stage2 should require customer quality, call-off durability/recovery, delivery-slot visibility, utilization, ASP/mix, margin, or revision bridge, not battery contract/customer label alone","SKC positive worked; Shinheung SEC and Samgi EV event/watch rows failed positive-stage promotion","R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE|R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA|R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,configured,cap_bridge_missing_battery_component_contract_event_premiums_as_4B_watch,0,"Battery component and customer-contract premiums can peak before call-off, delivery and margin bridge is proven","Shinheung SEC had high MAE after post-CA call-off watch; Samgi EV showed 4B event-cap behavior after the January battery-case spike","R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA|R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,configured,block_positive_stage_when_battery_contract_theme_has_high_or_persistent_MAE_without_calloff_bridge,0,"High or persistent MAE after bridge-missing C12 entries should block Stage2/Stage3 promotion unless customer call-off, delivery and margin evidence survives","Shinheung SEC MAE90=-30.88 and Samgi EV MAE180=-32.23","R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA|R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L97_C12_SKC_2024_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_POSITIVE", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP", "case_type": "structural_success_with_later_battery_contract_calloff_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Copper-foil / battery customer-contract bridge produced very strong 30D/90D/180D MFE with shallow early MAE. C12 works when battery contract narrative maps into real customer quality, call-off durability, delivery slot visibility, utilization, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C12_positive_requires_customer_quality_calloff_delivery_utilization_margin_revision_bridge_not_contract_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1998/2001 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L97_C12_SHINHEUNGSEC_2024_BATTERY_CAP_CALLOFF_FALSE_STAGE2_POST_CA", "symbol": "243840", "company_name": "신흥에스이씨", "round": "R3", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP", "case_type": "failed_rerating_battery_cap_calloff_bridge_missing_post_CA", "positive_or_counterexample": "counterexample", "best_trigger": "R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Post-CA battery cap / customer call-off watch produced only a short MFE burst and then high 90D/180D MAE. C12 Stage2 should not be awarded without confirmed customer call-off recovery, delivery schedule, utilization, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_battery_cap_calloff_watch_counts_without_customer_calloff_delivery_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Profile flags a 2024-04-26 corporate-action candidate. Entry is after that boundary, so post-CA 180D window is used with caveat."}
{"row_type": "case", "case_id": "R3L97_C12_SAMGIEV_2024_BATTERY_CASE_EVENT_CAP_4B", "symbol": "419050", "company_name": "삼기이브이", "round": "R3", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery-case / EV component event premium capped on the January spike and then bled into persistent drawdown. C12 should route bridge-missing battery component contract premiums to 4B unless customer order, call-off durability, delivery slot, utilization, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_battery_case_contract_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2023 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE", "case_id": "R3L97_C12_SKC_2024_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_POSITIVE", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP", "sector": "copper_foil_battery_customer_contract_calloff_delivery_margin", "primary_archetype": "customer_quality_calloff_delivery_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | call_off_risk_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 81100.0, "evidence_available_at_that_date": "battery copper-foil customer contract/call-off recovery, delivery-slot visibility, utilization, ASP/mix and margin/revision bridge proxy after February washout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_contract_quality_proxy", "calloff_recovery_proxy", "delivery_slot_visibility_proxy", "utilization_bridge_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "very_strong_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_copper_foil_valuation_watch", "post_peak_calloff_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv", "profile_path": "atlas/symbol_profiles/011/011790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 56.97, "MFE_90D_pct": 146.61, "MFE_180D_pct": 146.61, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.45, "MAE_90D_pct": -3.45, "MAE_180D_pct": -3.45, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 200000.0, "drawdown_after_peak_pct": -47.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_copper_foil_valuation_and_calloff_4B_watch_needed", "four_b_evidence_type": ["customer_contract_bridge", "calloff_delivery_visibility", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_copper_foil_customer_contract_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1998_2001_CA", "same_entry_group_id": "R3L97_C12_011790_2024-02-06_81100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA", "case_id": "R3L97_C12_SHINHEUNGSEC_2024_BATTERY_CAP_CALLOFF_FALSE_STAGE2_POST_CA", "symbol": "243840", "company_name": "신흥에스이씨", "round": "R3", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP", "sector": "battery_cap_component_customer_calloff_watch_post_CA", "primary_archetype": "battery_component_calloff_watch_without_customer_delivery_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | call_off_risk_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 9230.0, "evidence_available_at_that_date": "post-CA battery-cap / EV component customer call-off watch without confirmed customer call-off recovery, delivery schedule, utilization, ASP/mix or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_cap_calloff_watch", "post_CA_rebound_watch", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["short_MFE_then_high_MAE", "customer_delivery_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/243/243840/2024.csv", "profile_path": "atlas/symbol_profiles/243/243840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.43, "MFE_90D_pct": 13.43, "MFE_180D_pct": 13.43, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.82, "MAE_90D_pct": -30.88, "MAE_180D_pct": -30.88, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 10470.0, "drawdown_after_peak_pct": -39.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "battery_cap_calloff_watch_was_false_stage2_due_missing_customer_delivery_utilization_margin_bridge", "four_b_evidence_type": ["battery_component_post_CA_premium", "bridge_missing", "high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_battery_cap_calloff_watch_without_customer_delivery_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_battery_cap_calloff_watch_counts_without_customer_calloff_delivery_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-04-26_CA_candidate_boundary_clean_window_with_caveat", "same_entry_group_id": "R3L97_C12_243840_2024-05-17_9230", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP", "case_id": "R3L97_C12_SAMGIEV_2024_BATTERY_CASE_EVENT_CAP_4B", "symbol": "419050", "company_name": "삼기이브이", "round": "R3", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP", "sector": "battery_case_EV_component_customer_contract_event_premium", "primary_archetype": "battery_case_contract_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | call_off_risk_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-11", "entry_date": "2024-01-11", "entry_price": 3320.0, "evidence_available_at_that_date": "battery-case / EV component contract event premium after January battery-component spike without confirmed customer call-off, delivery slot or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["battery_case_contract_event", "EV_component_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE90", "persistent_MAE180", "customer_calloff_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/419/419050/2024.csv", "profile_path": "atlas/symbol_profiles/419/419050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.31, "MFE_90D_pct": 3.31, "MFE_180D_pct": 3.31, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.77, "MAE_90D_pct": -24.4, "MAE_180D_pct": -32.23, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-11", "peak_price": 3430.0, "drawdown_after_peak_pct": -34.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing_battery_case_contract_event_cap", "four_b_evidence_type": ["battery_case_contract_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_battery_case_customer_contract_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_battery_case_contract_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2023_CA_candidates", "same_entry_group_id": "R3L97_C12_419050_2024-01-11_3320", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L97_C12_SKC_2024_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_POSITIVE", "trigger_id": "R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE", "symbol": "011790", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 65, "policy_or_regulatory_score": 15, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "copper_foil_customer_contract_calloff_positive", "MFE_90D_pct": 146.61, "MAE_90D_pct": -3.45, "score_return_alignment_label": "copper_foil_customer_contract_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L97_C12_SHINHEUNGSEC_2024_BATTERY_CAP_CALLOFF_FALSE_STAGE2_POST_CA", "trigger_id": "R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA", "symbol": "243840", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_cap_calloff_false_stage2", "MFE_90D_pct": 13.43, "MAE_90D_pct": -30.88, "score_return_alignment_label": "battery_cap_calloff_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_battery_cap_calloff_watch_counts_without_customer_calloff_delivery_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L97_C12_SAMGIEV_2024_BATTERY_CASE_EVENT_CAP_4B", "trigger_id": "R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP", "symbol": "419050", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "battery_case_contract_event_cap_4B_guard", "MFE_90D_pct": 3.31, "MAE_90D_pct": -24.4, "score_return_alignment_label": "battery_case_contract_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_battery_case_contract_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "97", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_BATTERY_CAP_CALL_OFF_FALSE_STAGE2_AND_BATTERY_CASE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "call_off_risk_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["copper_foil_customer_contract_positive", "battery_cap_calloff_false_stage2", "battery_case_contract_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C12 rows need explicit customer quality, call-off durability/recovery, delivery-slot visibility, utilization, ASP/mix, margin or revision bridge before positive promotion.
- In C12, bridge-missing battery component contract-premium rows with short MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C12 battery customer contract / call-off rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 97
next_round = R4
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
