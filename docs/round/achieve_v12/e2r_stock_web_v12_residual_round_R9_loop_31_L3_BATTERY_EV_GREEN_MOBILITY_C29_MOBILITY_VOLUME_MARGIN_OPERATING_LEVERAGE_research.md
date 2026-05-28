# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R9
loop = 31
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE
output_file = e2r_stock_web_v12_residual_round_R9_loop_31_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

This file is historical calibration research only. It is not a live watchlist, a recommendation list, a production patch, or a broker/API workflow.

## 1. Current Calibrated Profile Assumption

`e2r_2_1_stock_web_calibrated_proxy` is the current profile. Existing global axes are treated as already applied; this loop tests C29-specific residual rules only.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R9 |
| loop | 31 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| selected objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; green_strictness_stress_test; 4B_non_price_requirement_stress_test |
| selected symbols | 028670 팬오션; 044450 KSS해운; 003490 대한항공; 298690 에어부산; 005880 대한해운 narrative-only |
| positive/counterexample balance | 2 positive / 2 counterexample / 1 narrative-only blocked row |

## 3. Previous Coverage / Duplicate Avoidance Check

Prior local/registry coverage already included R9/C29 rows for OEM/auto-parts and some reopening/LCC examples. This loop avoids the already used HMM, 현대글로비스, 제주항공, 진에어, 티웨이, 현대차, 기아, HL만도, 현대위아, and SL representative rows. It adds four same-archetype new symbols and a separate blocked narrative-only shipping row.

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 0
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest and schema were checked: source is FinanceData/marcap, price basis is `tradable_raw`, price status is `raw_unadjusted_marcap`, and the manifest max date is 2026-02-20. The schema defines the tradable shard columns and the MFE/MAE formula used here. fileciteturn977file0 fileciteturn978file0

## 5. Historical Eligibility Gate

| Symbol | Profile path | Corporate-action status | Calibration status |
|---:|---|---|---|
| 028670 | atlas/symbol_profiles/028/028670.json | no 2020-2021 tested-window candidate; profile candidates are historical pre-2020 | usable |
| 044450 | atlas/symbol_profiles/044/044450.json | candidates only 2008/2016; no 2021 tested-window overlap | usable |
| 003490 | atlas/symbol_profiles/003/003490.json | 2021-03-24 candidate before selected 2021-11-08 entry; tested forward window clean | usable |
| 298690 | atlas/symbol_profiles/298/298690.json | 2022 candidates before selected 2023 trigger; tested window clean | usable |
| 005880 | atlas/symbol_profiles/005/005880.json | 2020-10-12 and 2021-06-30 candidates overlap same shipping-cycle window | narrative_only / blocked |

Profile and row excerpts used: 팬오션 profile and 2020/2021 rows; KSS해운 profile and 2021 rows; 대한항공 profile and 2021/2022 rows; 에어부산 profile and 2023 rows; 대한해운 profile for the corporate-action block. fileciteturn990file0turn991file0turn992file0turn995file0turn996file0turn997file0turn998file0turn999file0turn1002file0turn1003file0turn993file0turn994file0

## 6. Canonical Archetype Compression Map

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
├── SHIPPING_RATE_MARGIN_LEVERAGE
│   ├── 028670 팬오션: freight-rate/utilization/margin bridge positive
│   └── 044450 KSS해운: specialized carrier positive but needs contract/margin confirmation before Green
└── AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN
    ├── 003490 대한항공: reopening volume without unit margin/revision closure
    └── 298690 에어부산: LCC price spike without durable margin bridge
```

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | pos/counter | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R9L31_C29_028670_PAN_OCEAN_DRYBULK_RATE_MARGIN | 028670 | 팬오션 | structural_success | TR_R9L31_C29_028670_STAGE2A_20201116 | positive | current_profile_correct |
| R9L31_C29_044450_KSS_LPG_CARRIER_CONTRACT_RATE | 044450 | KSS해운 | high_mae_success | TR_R9L31_C29_044450_STAGE2A_20210416 | positive | current_profile_too_early |
| R9L31_C29_003490_KOREANAIR_REOPENING_VOLUME_FALSE_POSITIVE | 003490 | 대한항공 | failed_rerating | TR_R9L31_C29_003490_REOPENING_FALSE_20211108 | counterexample | current_profile_false_positive |
| R9L31_C29_298690_AIRBUSAN_REOPENING_PRICE_SPIKE_COUNTER | 298690 | 에어부산 | price_moved_without_evidence | TR_R9L31_C29_298690_REOPENING_SPIKE_20230120 | counterexample | current_profile_false_positive |
| R9L31_C29_005880_KOREA_LINE_CORP_ACTION_BLOCK | 005880 | 대한해운 | narrative_only | TR_R9L31_C29_005880_NARRATIVE_ONLY_BLOCKED_20201116 | narrative_only | current_profile_data_insufficient |


## 8. Positive vs Counterexample Balance

- positive_case_count = 2
- counterexample_count = 2
- narrative_only_blocked = 1
- calibration_usable_case_count = 4
- current_profile_error_count = 3

The mechanism is cleanly split. Shipping rate/margin rows behave like C29 positives when rate/utilization evidence turns into margin and revision. Airline/LCC reopening rows show the opposite: volume can return while unit margin, fuel/FX, debt, or dilution risk keeps the equity path weak.

## 9. Evidence Source Map

| Family | Positive use | Counterexample guard |
|---|---|---|
| freight/rate | Pan Ocean, KSS shipping route | not enough if price-only or corporate-action contaminated |
| volume/reopening | useful as Stage2 optionality | capped below Green unless unit margin/revision appears |
| margin bridge | required for C29 promotion | absent in Korean Air/Air Busan rows |
| 4B overlay | valuation/revision fatigue after rate blowoff | price-only local spike cannot train positive entries |

## 10. Price Data Source Map

| Symbol | Shard(s) | Profile |
|---:|---|---|
| 028670 | atlas/ohlcv_tradable_by_symbol_year/028/028670/2020.csv; 2021.csv | atlas/symbol_profiles/028/028670.json |
| 044450 | atlas/ohlcv_tradable_by_symbol_year/044/044450/2021.csv | atlas/symbol_profiles/044/044450.json |
| 003490 | atlas/ohlcv_tradable_by_symbol_year/003/003490/2021.csv; 2022.csv | atlas/symbol_profiles/003/003490.json |
| 298690 | atlas/ohlcv_tradable_by_symbol_year/298/298690/2023.csv | atlas/symbol_profiles/298/298690.json |
| 005880 | blocked narrative-only | atlas/symbol_profiles/005/005880.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | verdict | agg |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| TR_R9L31_C29_028670_STAGE2A_20201116 | 028670 | Stage2-Actionable | 2020-11-16 | 4,230 | 12.77 | -5.32 | 74.7 | -5.32 | 110.87 | -5.32 | 2021-06-29 / 8920 | current_profile_correct | representative |
| TR_R9L31_C29_044450_STAGE2A_20210416 | 044450 | Stage2-Actionable | 2021-04-16 | 11,200 | 43.75 | -4.02 | 43.75 | -4.02 | 43.75 | -7.14 | 2021-05-13 / 16100 | current_profile_too_early | representative |
| TR_R9L31_C29_003490_REOPENING_FALSE_20211108 | 003490 | Stage2-Actionable-candidate-Rejected | 2021-11-08 | 31,150 | 0.32 | -18.3 | 0.32 | -18.3 | 4.49 | -25.2 | 2022-04-06 / 32550 | current_profile_false_positive | representative |
| TR_R9L31_C29_298690_REOPENING_SPIKE_20230120 | 298690 | Stage2-Actionable-candidate-Rejected | 2023-01-20 | 4,250 | 12.47 | -7.88 | 12.47 | -30.24 | 12.47 | -36.47 | 2023-01-30 / 4780 | current_profile_false_positive | representative |
| TR_R9L31_C29_005880_NARRATIVE_ONLY_BLOCKED_20201116 | 005880 | narrative_only | 2020-11-16 |  | None | None | None | None | None | None | None / None | current_profile_data_insufficient | narrative_only |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows only: Pan Ocean, KSS해운, 대한항공, 에어부산. 대한해운 is not included in quantitative calibration because of corporate-action contamination.

| Bucket | Avg MFE90 | Avg MAE90 | Avg MFE180 | Avg MAE180 | Note |
|---|---:|---:|---:|---:|---|
| positives | 59.23 | -4.67 | 77.31 | -6.23 | shipping rate/margin bridge worked |
| counterexamples | 6.40 | -24.27 | 8.48 | -30.84 | reopening volume failed without unit-margin closure |
| all representative | 32.82 | -14.47 | 42.90 | -18.54 | C29 needs rate/unit-margin split |

## 13. Current Calibrated Profile Stress Test

1. Current profile likely handles Pan Ocean correctly because non-price margin/rate evidence closes before full Green.
2. Current profile is too early for KSS if a local specialized-carrier spike is promoted to Green without confirmed contract/margin durability.
3. Current profile would over-promote Korean Air and Air Busan if reopening volume evidence is treated like margin evidence.
4. Yellow 75 is not too low for shipping positives, but it is too permissive for airline/LCC reopening rows without unit margin.
5. Green 87 / revision 55 should be kept and strengthened in C29 when the evidence is volume-only.
6. Price-only blowoff guard is strengthened by the Air Busan path.
7. Full 4B non-price requirement is kept: KSS price spike is overlay-only; Pan Ocean later 4B needs valuation/revision fatigue, not just a local high.
8. Hard 4C routing is not the main axis here; these are mostly 4B/failed-rerating rows rather than thesis-break rows.

## 14. Stage2 / Yellow / Green Comparison

| Case | Stage2 entry | Green-like confirmation | peak | green_lateness_ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| Pan Ocean | 4,230 | not separately modeled | 8,920 | not_applicable | Stage2/Yellow works once freight-rate margin bridge appears |
| KSS해운 | 11,200 | not separately modeled | 16,100 | not_applicable | fast MFE but Green should wait for contract/margin confirmation |
| Korean Air | 31,150 | no confirmed Green | 32,550 | not_applicable | volume-only reopening failed |
| Air Busan | 4,250 | no confirmed Green | 4,780 | not_applicable | price-only local spike failed |

## 15. 4B Local vs Full-window Timing Audit

| Case | 4B evidence | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| Pan Ocean | valuation/revision fatigue later, not at entry | n/a | n/a | full 4B needs non-price slowdown |
| KSS해운 | price spike / positioning only | 1.00 | 1.00 | overlay-only until margin durability is checked |
| Korean Air | revision/margin slowdown | n/a | n/a | failed-rerating guard, not positive entry |
| Air Busan | price-only local peak | 1.00 | 1.00 | price-only local 4B cannot train positive |

## 16. 4C Protection Audit

No hard 4C thesis-break row is used for positive/negative calibration in this loop. Korean Air/Air Busan are failed-rerating/4B-risk rows, not hard 4C rows.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
candidate_axis = c29_rate_or_unit_margin_bridge_required
rule = C29 promotion requires rate/unit-margin/revision closure; volume/reopening alone is capped at Stage2-watch or Stage2-Actionable, not Green.
```

## 18. Canonical-Archetype Rule Candidate

C29 should split “volume” into two different engines:

- **Rate/margin volume**: shipping freight-rate or utilization evidence that converts into margin/revision can promote.
- **Reopening/headline volume**: passenger or travel recovery without unit margin, fuel/FX, and balance-sheet repair should be capped.

## 19. Before / After Backtest Comparison

| profile_id | scope | selected cases | avg_MFE90 | avg_MAE90 | false_positive_rate | alignment |
|---|---|---|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | all representative | 32.82 | -14.47 | 50% among volume-only rows | mixed |
| P0b e2r_2_0_baseline_reference | rollback | all representative | 32.82 | -14.47 | higher | over-promotes volume-only rows |
| P1 sector_specific_candidate_profile | L3 | shipping promoted, airline watched | 59.23 | -4.67 | 0% among promoted | improved |
| P2 canonical_archetype_candidate_profile | C29 | margin-bridge positives only | 59.23 | -4.67 | 0% among promoted | best |
| P3 counterexample_guard_profile | C29 guard | volume-only rejected | 59.23 | -4.67 | 0% but conservative | safe but may miss early airline inflections |

## 20. Score-Return Alignment Matrix

| case_id | before | after | MFE90/MAE90 | alignment |
|---|---|---|---|---|
| Pan Ocean | Stage3-Yellow | Stage3-Green | 74.70 / -5.32 | aligned positive |
| KSS해운 | Stage2-Actionable | Stage2 + 4B-watch | 43.75 / -4.02 | positive but overlay needed |
| Korean Air | Stage2-Actionable | Watch/no-positive-promotion | 0.32 / -18.30 | guard improves |
| Air Busan | false Stage2 | Narrative-only/4B-risk | 12.47 / -30.24 | false positive removed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | shipping_rate_margin / airline_reopening_counter | 2 | 2 | 2 | 0 | 4 | 0 | 4 | 4 | 3 | true | true | shipping positives added; airline volume-only guard added |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_green_revision_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
residual_error_types_found: shipping_rate_margin_positive; airline_reopening_volume_false_positive; LCC_price_spike_without_margin_bridge
new_axis_proposed: c29_rate_or_unit_margin_bridge_required; c29_reopening_volume_only_green_cap
existing_axis_strengthened: stage3_green_revision_min in C29; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R9/C29 transport/airline/shipping residual split after prior OEM/LCC rows
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest/schema, selected symbol profiles, entry rows, forward windows, 30D/90D/180D MFE/MAE proxies, corporate-action contamination gate, positive/counterexample balance, and C29-specific shadow rules.

Not validated: live signals, current valuation, production code behavior, brokerage execution, or any investment recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_rate_or_unit_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Shipping/airline volume evidence must close into rate/unit margin/revision before Green promotion","keeps Pan Ocean positive and blocks Korean Air/Air Busan reopening-only false positives","TR_R9L31_C29_028670_STAGE2A_20201116|TR_R9L31_C29_003490_REOPENING_FALSE_20211108|TR_R9L31_C29_298690_REOPENING_SPIKE_20230120",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_reopening_volume_only_green_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Reopening/travel capacity is not sufficient for Stage3-Green without unit margin, fuel/FX, and balance-sheet repair evidence","reduces false-positive promotion in airline/LCC rows","TR_R9L31_C29_003490_REOPENING_FALSE_20211108|TR_R9L31_C29_298690_REOPENING_SPIKE_20230120",2,2,2,medium,canonical_shadow_only,"not production; guard only"
shadow_weight,c29_price_spike_4b_overlay_only,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Local price spike without non-price margin evidence is overlay-only and cannot train positive entry weights","Air Busan spike had positive MFE but severe peak drawdown; KSS spike needs contract confirmation","TR_R9L31_C29_044450_STAGE2A_20210416|TR_R9L31_C29_298690_REOPENING_SPIKE_20230120",2,2,1,low_to_medium,canonical_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R9L31_C29_028670_PAN_OCEAN_DRYBULK_RATE_MARGIN", "symbol": "028670", "company_name": "팬오션", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R9L31_C29_028670_STAGE2A_20201116", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_drybulk_rate_margin_leverage", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Drybulk/freight-rate recovery and sector operating leverage were visible before full 2021 profit confirmation; the case tests whether C29 shipping requires rate × utilization × margin closure rather than price-only strength."}
{"row_type": "case", "case_id": "R9L31_C29_044450_KSS_LPG_CARRIER_CONTRACT_RATE", "symbol": "044450", "company_name": "KSS해운", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R9L31_C29_044450_STAGE2A_20210416", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_high_mfe_but_contract_confirmation_required", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Specialized LPG/gas-carrier volume and rate sensitivity produced a fast MFE, but the 2021 spike behaved like a narrower contract/charter-rate pocket rather than broad shipping beta."}
{"row_type": "case", "case_id": "R9L31_C29_003490_KOREANAIR_REOPENING_VOLUME_FALSE_POSITIVE", "symbol": "003490", "company_name": "대한항공", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R9L31_C29_003490_REOPENING_FALSE_20211108", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_reopening_volume_without_margin", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Reopening/travel-volume option existed, but passenger-volume recovery did not yet close into unit margin/revision; fuel, balance-sheet, and reopening uncertainty dominated the forward path."}
{"row_type": "case", "case_id": "R9L31_C29_298690_AIRBUSAN_REOPENING_PRICE_SPIKE_COUNTER", "symbol": "298690", "company_name": "에어부산", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R9L31_C29_298690_REOPENING_SPIKE_20230120", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_moved_without_margin_evidence", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "LCC reopening price spike had travel-volume evidence, but did not carry margin bridge, balance-sheet repair, or durable revision evidence at the trigger."}
{"row_type": "case", "case_id": "R9L31_C29_005880_KOREA_LINE_CORP_ACTION_BLOCK", "symbol": "005880", "company_name": "대한해운", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "case_type": "narrative_only", "positive_or_counterexample": "narrative_only", "best_trigger": "TR_R9L31_C29_005880_NARRATIVE_ONLY_BLOCKED_20201116", "calibration_usable": false, "is_new_independent_case": false, "reuse_reason": "corporate_action_window_blocked", "independent_evidence_weight": 0.0, "score_price_alignment": "narrative_only_corporate_action_contaminated", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "대한해운 belongs to the same shipping-beta family, but the profile lists 2020-10-12 and 2021-06-30 corporate-action candidates, so it is kept out of weight calibration."}
{"row_type": "trigger", "trigger_id": "TR_R9L31_C29_028670_STAGE2A_20201116", "case_id": "R9L31_C29_028670_PAN_OCEAN_DRYBULK_RATE_MARGIN", "symbol": "028670", "company_name": "팬오션", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "sector": "모빌리티·운송·레저 / 해운", "primary_archetype": "drybulk freight rate margin operating leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-11-16", "evidence_available_at_that_date": "Drybulk/freight-rate recovery and sector operating leverage were visible before full 2021 profit confirmation; the case tests whether C29 shipping requires rate × utilization × margin closure rather than price-only strength.", "evidence_source": "public shipping-rate / earnings-turn narrative; OHLC rows checked in stock-web 2020/2021 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "confirmed_revision"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028670/2020.csv|atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv", "profile_path": "atlas/symbol_profiles/028/028670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-11-16", "entry_price": 4230, "MFE_30D_pct": 12.77, "MFE_90D_pct": 74.7, "MFE_180D_pct": 110.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.32, "MAE_90D_pct": -5.32, "MAE_180D_pct": -5.32, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-29", "peak_price": 8920, "drawdown_after_peak_pct": -17.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_drybulk_rate_margin_leverage", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R9L31_028670_2020-11-16_4230", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R9L31_C29_044450_STAGE2A_20210416", "case_id": "R9L31_C29_044450_KSS_LPG_CARRIER_CONTRACT_RATE", "symbol": "044450", "company_name": "KSS해운", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "sector": "모빌리티·운송·레저 / 해운", "primary_archetype": "specialized gas carrier rate and contract leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-04-16", "evidence_available_at_that_date": "Specialized LPG/gas-carrier volume and rate sensitivity produced a fast MFE, but the 2021 spike behaved like a narrower contract/charter-rate pocket rather than broad shipping beta.", "evidence_source": "public shipping-rate / contract-margin narrative; OHLC rows checked in stock-web 2021 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/044/044450/2021.csv", "profile_path": "atlas/symbol_profiles/044/044450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-04-16", "entry_price": 11200, "MFE_30D_pct": 43.75, "MFE_90D_pct": 43.75, "MFE_180D_pct": 43.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.02, "MAE_90D_pct": -4.02, "MAE_180D_pct": -7.14, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-13", "peak_price": 16100, "drawdown_after_peak_pct": -25.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_spike_needs_contract_margin_confirmation_before_green", "four_b_evidence_type": ["positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_high_mfe_but_contract_confirmation_required", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R9L31_044450_2021-04-16_11200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R9L31_C29_003490_REOPENING_FALSE_20211108", "case_id": "R9L31_C29_003490_KOREANAIR_REOPENING_VOLUME_FALSE_POSITIVE", "symbol": "003490", "company_name": "대한항공", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "sector": "모빌리티·운송·레저 / 항공", "primary_archetype": "airline reopening volume without unit margin closure", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable-candidate-Rejected", "trigger_date": "2021-11-08", "evidence_available_at_that_date": "Reopening/travel-volume option existed, but passenger-volume recovery did not yet close into unit margin/revision; fuel, balance-sheet, and reopening uncertainty dominated the forward path.", "evidence_source": "public reopening/travel narrative; OHLC rows checked in stock-web 2021/2022 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "revision_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003490/2021.csv|atlas/ohlcv_tradable_by_symbol_year/003/003490/2022.csv", "profile_path": "atlas/symbol_profiles/003/003490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-08", "entry_price": 31150, "MFE_30D_pct": 0.32, "MFE_90D_pct": 0.32, "MFE_180D_pct": 4.49, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.3, "MAE_90D_pct": -18.3, "MAE_180D_pct": -25.2, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-06", "peak_price": 32550, "drawdown_after_peak_pct": -28.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "reopening_volume_without_unit_margin_failed", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_reopening_volume_without_margin", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R9L31_003490_2021-11-08_31150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R9L31_C29_298690_REOPENING_SPIKE_20230120", "case_id": "R9L31_C29_298690_AIRBUSAN_REOPENING_PRICE_SPIKE_COUNTER", "symbol": "298690", "company_name": "에어부산", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "sector": "모빌리티·운송·레저 / LCC", "primary_archetype": "low-cost-carrier reopening spike without durable margin", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable-candidate-Rejected", "trigger_date": "2023-01-20", "evidence_available_at_that_date": "LCC reopening price spike had travel-volume evidence, but did not carry margin bridge, balance-sheet repair, or durable revision evidence at the trigger.", "evidence_source": "public reopening/travel narrative; OHLC rows checked in stock-web 2023 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298690/2023.csv", "profile_path": "atlas/symbol_profiles/298/298690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-01-20", "entry_price": 4250, "MFE_30D_pct": 12.47, "MFE_90D_pct": 12.47, "MFE_180D_pct": 12.47, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.88, "MAE_90D_pct": -30.24, "MAE_180D_pct": -36.47, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-01-30", "peak_price": 4780, "drawdown_after_peak_pct": -43.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_should_not_train_positive", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "price_moved_without_margin_evidence", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_R9L31_298690_2023-01-20_4250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R9L31_C29_005880_NARRATIVE_ONLY_BLOCKED_20201116", "case_id": "R9L31_C29_005880_KOREA_LINE_CORP_ACTION_BLOCK", "symbol": "005880", "company_name": "대한해운", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "DRYBULK_LNG_LPG_SHIPPING_RATE_MARGIN_LEVERAGE | AIRLINE_REOPENING_VOLUME_WITHOUT_UNIT_MARGIN_COUNTEREXAMPLE", "sector": "모빌리티·운송·레저 / 해운", "primary_archetype": "shipping beta blocked by corporate action", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "narrative_only", "trigger_date": "2020-11-16", "evidence_available_at_that_date": "대한해운 belongs to the same shipping-beta family, but the profile lists 2020-10-12 and 2021-06-30 corporate-action candidates, so it is kept out of weight calibration.", "evidence_source": "stock-web symbol profile only; not used for weight calibration", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005880/2020.csv|atlas/ohlcv_tradable_by_symbol_year/005/005880/2021.csv", "profile_path": "atlas/symbol_profiles/005/005880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-11-16", "entry_price": null, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": null, "peak_price": null, "drawdown_after_peak_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "blocked_by_corporate_action_contamination", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "narrative_only_corporate_action_contaminated", "current_profile_verdict": "current_profile_data_insufficient", "calibration_usable": false, "forward_window_trading_days": null, "calibration_block_reasons": ["corporate_action_contaminated_180D_window"], "corporate_action_window_status": "blocked_by_corporate_action_candidate_2021-06-30", "same_entry_group_id": "SEG_R9L31_005880_BLOCKED", "dedupe_for_aggregate": false, "aggregate_group_role": "narrative_only", "is_new_independent_case": false, "reuse_reason": "corporate_action_window_blocked", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L31_C29_028670_PAN_OCEAN_DRYBULK_RATE_MARGIN", "trigger_id": "TR_R9L31_C29_028670_STAGE2A_20201116", "symbol": "028670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "freight_rate_or_reopening_score": 9}, "weighted_score_before": 81, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 7, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 10, "freight_rate_or_reopening_score": 10}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "capacity_or_shipment_score", "freight_rate_or_reopening_score"], "component_delta_explanation": "C29 shadow split: freight/rate × utilization × margin bridge can promote; reopening volume alone is capped or routed to 4B-watch.", "MFE_90D_pct": 74.7, "MAE_90D_pct": -5.32, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L31_C29_044450_KSS_LPG_CARRIER_CONTRACT_RATE", "trigger_id": "TR_R9L31_C29_044450_STAGE2A_20210416", "symbol": "044450", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 6, "freight_rate_or_reopening_score": 7}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 6, "freight_rate_or_reopening_score": 7}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable / 4B-watch", "changed_components": ["execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C29 shadow split: freight/rate × utilization × margin bridge can promote; reopening volume alone is capped or routed to 4B-watch.", "MFE_90D_pct": 43.75, "MAE_90D_pct": -4.02, "score_return_alignment_label": "positive_but_overlay_needed", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L31_C29_003490_KOREANAIR_REOPENING_VOLUME_FALSE_POSITIVE", "trigger_id": "TR_R9L31_C29_003490_REOPENING_FALSE_20211108", "symbol": "003490", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "freight_rate_or_reopening_score": 8}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "freight_rate_or_reopening_score": 8}, "weighted_score_after": 62, "stage_label_after": "Watch / no-positive-promotion", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "C29 shadow split: freight/rate × utilization × margin bridge can promote; reopening volume alone is capped or routed to 4B-watch.", "MFE_90D_pct": 0.32, "MAE_90D_pct": -18.3, "score_return_alignment_label": "guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L31_C29_298690_AIRBUSAN_REOPENING_PRICE_SPIKE_COUNTER", "trigger_id": "TR_R9L31_C29_298690_REOPENING_SPIKE_20230120", "symbol": "298690", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "freight_rate_or_reopening_score": 9}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable false positive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 8, "freight_rate_or_reopening_score": 9}, "weighted_score_after": 47, "stage_label_after": "Narrative-only / 4B-risk", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C29 shadow split: freight/rate × utilization × margin bridge can promote; reopening volume alone is capped or routed to 4B-watch.", "MFE_90D_pct": 12.47, "MAE_90D_pct": -30.24, "score_return_alignment_label": "false_positive_removed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R9", "loop": "31", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["shipping_rate_margin_positive", "airline_reopening_volume_false_positive", "LCC_price_spike_without_margin_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R9/C29 had OEM/LCC rows; this loop adds clean shipping-rate positives and airline/LCC reopening-only counterexamples without reusing HMM/Glovis/Jeju/JinAir/Tway."}
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
next_round = R4 / C15_MATERIAL_SPREAD_SUPERCYCLE or R8 / C27 holdout
avoid_reusing = 028670, 044450, 003490, 298690 C29 same trigger dates
```

## 28. Source Notes

- Stock-Web manifest/schema: `atlas/manifest.json`, `atlas/schema.json`.
- Symbol profiles checked: 028670, 044450, 003490, 298690, 005880.
- Price shards checked: 028/028670/2020.csv, 028/028670/2021.csv, 044/044450/2021.csv, 003/003490/2021.csv, 003/003490/2022.csv, 298/298690/2023.csv.
- Evidence source labels are historical event-family labels for calibration. In repository ingestion, attach original filings/IR/news PDFs where available before any promotion batch.
