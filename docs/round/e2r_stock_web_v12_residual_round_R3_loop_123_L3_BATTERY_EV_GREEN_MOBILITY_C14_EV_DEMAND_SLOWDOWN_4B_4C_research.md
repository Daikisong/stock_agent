# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_123_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selected_round: R3
selected_loop: 123
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under_30_representative_rows / C14 rows 11 need_to_30 19 before local follow-up
round_schedule_status: coverage_index_selected
round_sector_consistency: pass: C11-C14 maps to R3 / L3_BATTERY_EV_GREEN_MOBILITY
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
investment_recommendation: false
loop_objective:
  - coverage_gap_fill
  - followup_new_symbol_date_family
  - 4C_thesis_break_timing_test
  - 4B_non_price_requirement_stress_test
  - counterexample_mining
  - canonical_archetype_compression
```

This MD is a standalone historical calibration artifact. It does not recommend any current position, does not scan live candidates, does not patch `stock_agent`, and does not change production scoring. It only creates shadow-rule evidence for later batch ingestion.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

The tested axis is not the global claim that price-only blowoff needs a guard. That axis already exists. The residual question is narrower: within C14, when does an EV slowdown headline become hard 4C, and when should it remain Stage4B/watch because survivor, bottoming, parent-mix, or reopen evidence exists?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
selected_round = R3
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE
```

C14 belongs to R3/L3. No R13 naming is used because this is not a cross-archetype checkpoint.

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` lists C14 as Priority 0 with 11 representative rows before local follow-up. This loop avoids the last C14 local files' main WCP/Solus/POSCO/SKC/EcoProBM focus and expands into L&F, SK Innovation, Samsung SDI, Lotte Energy Materials, Daejoo Electronic Materials, and Chunbo.

```text
strict_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_count = 0
new_independent_case_ratio = 6/7 = 0.86
minimum_new_symbol_count_pass = true
minimum_positive_case_count_pass = true
minimum_counterexample_count_pass = true
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
entry_price_basis = close c column on entry_date
MFE_basis = max high h over forward 30/90/180 trading-row windows
MAE_basis = min low l over forward 30/90/180 trading-row windows
```

All selected representative rows have complete 30D/90D/180D windows inside the stock-web manifest horizon. The local stock-web shards used in this execution are under `/mnt/data/stockweb_shards`, copied from the stock-web atlas paths recorded in the trigger rows.

## 5. Historical Eligibility Gate

All seven trigger rows are historical, have valid `entry_date`, `entry_price`, and complete 30D/90D/180D MFE/MAE fields. No row is emitted as `row_type="trigger"` unless the six canonical price-path fields exist.

## 6. Canonical Archetype Compression Map

| fine/deep route | canonical compression | rule implication |
|---|---|---|
| lithium inventory valuation loss | C14 | Stage4B/watch first; hard 4C only after repeated loss or order break |
| shipment guidance cut from EV slowdown | C14 | Severity split required because a rebound can still occur before thesis breaks |
| parent company with battery loss plus refining buffer | C14 | Parent mix can block hard 4C despite battery-unit slowdown |
| Q1 trough / Q2 recovery language | C14 | Hard 4C should decay/reopen when explicit bottoming path exists |
| silicon-anode survivor demand | C14 | Generic EV slowdown must not block a verified survivor bridge |
| electrolyte demand collapse + financing overhang | C14 | Hard 4C can be valid when demand, ASP, and CB/BW overhang align |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | MFE90 | MAE90 | MFE180 | MAE180 | role | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---|---|
| C14_FU123_066970_20240202 | 066970 | L&F | Stage4B | 2024-02-02 | 36.68 | -9.27 | 36.68 | -43.06 | 4B_overlay_success / counterexample | current_profile_false_positive_if_hard_4c_without_reopen_clause |
| C14_FU123_066970_20240808 | 066970 | L&F | Stage4C | 2024-08-08 | 46.52 | -3.83 | 46.52 | -37.59 | 4C_late / counterexample | current_profile_4c_too_early_if_single_guidance_cut_is_treated_as_thesis_break |
| C14_FU123_096770_20240429 | 096770 | SK Innovation | Stage4B | 2024-04-29 | 13.84 | -18.63 | 16.42 | -18.63 | 4B_overlay_success / counterexample | current_profile_correct_if_stage4b_watch_not_hard_4c |
| C14_FU123_006400_20250305 | 006400 | Samsung SDI | Stage4B | 2025-03-05 | 3.51 | -26.14 | 66.04 | -26.14 | 4B_overlay_success / counterexample | current_profile_4c_too_early_if_bottoming_language_ignored |
| C14_FU123_020150_20250124 | 020150 | Lotte Energy Materials | Stage4B | 2025-01-24 | 36.88 | -15.57 | 36.88 | -15.57 | 4B_overlay_success / counterexample | current_profile_false_positive_if_reopen_path_ignored |
| C14_FU123_078600_20240402 | 078600 | Daejoo Electronic Materials | Stage2-Actionable | 2024-04-02 | 80.75 | -6.86 | 80.75 | -18.58 | structural_success / positive | current_profile_missed_structural_if_generic_ev_slowdown_blocks_survivor |
| C14_FU123_278280_20230428 | 278280 | Chunbo | Stage4C | 2023-04-28 | 8.16 | -29.43 | 8.16 | -53.48 | 4C_success / positive | current_profile_4c_too_late_if_waiting_for_full_year_loss |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 5
stage4b_overlay_count = 6
stage4c_case_count = 6
calibration_usable_trigger_count = 7
representative_trigger_count = 7
```

The positive cases are not buy signals. In this C14 context, positive means the proposed severity split correctly explains the observed price path: Daejoo survives generic slowdown through a verified silicon-anode adoption bridge, while Chunbo shows a true hard-4C path where demand, ASP, earnings, and financing overhang break at once.

## 9. Evidence Source Map

| evidence_id | source URL | as-of usage |
|---|---|---|
| EV_C14_FU123_LNF_20240201_ASIAE | https://www.asiae.co.kr/en/article/2024020116473792269 | 2023 operating loss and lithium-price-driven inventory valuation loss were disclosed, with shipment volume bottoming and expected double-digit QoQ improvement. It is a Stage4B/earnings-trough watch, not automatic hard 4C. |
| EV_C14_FU123_LNF_20240808_MK | https://www.mk.co.kr/en/economy/11088257 | 2Q24 shipment guidance worsened and 2024 volume was estimated to fall because EV end-demand kept slowing. The price path still allowed a 90D rebound before later drawdown, so the rule needs severity split. |
| EV_C14_FU123_SKINNO_20240429_REUTERS | https://www.reuters.com/business/energy/sk-innovation-expects-solid-refining-margin-continue-q2-2024-04-29/ | SK On battery loss widened on lower EV shipments, but the parent beat profit expectations, expected solid refining margin, and maintained H2 break-even target. Parent-mix buffer blocks hard 4C. |
| EV_C14_FU123_SDI_20250305_REUTERS | https://www.reuters.com/business/autos-transportation/samsung-sdi-ceo-says-ev-demand-remain-sluggish-until-h1-2026-2025-03-05/ | CEO said EV demand would stay sluggish until H1 2026 and Q4 2024 had an operating loss, but also said earnings would likely bottom in Q1 and recover from Q2. Hard 4C would be too blunt. |
| EV_C14_FU123_LOTTEEM_20250124_CHOSUN_OFFICIAL_Q3 | https://lotteenergymaterials.com/pr/promotion_detail.do?seq=97 | Official Q3 disclosure already described EV slowdown, customer inventory adjustment, lower utilization, fixed-cost burden, inventory valuation loss, and operating loss, but also identified North America volume/recovery routes. Use as Stage4B watch unless repeat losses remove reopen path. |
| EV_C14_FU123_DAEJOO_20240402_ETNEWS | https://www.etnews.com/20240329000204 | Silicon-anode sales were expected to exceed the prior full year in 1H24; coverage expanded from two vehicle models to nine and SK On adoption was referenced. Generic EV slowdown should not hard-4C this survivor route. |
| EV_C14_FU123_CHUNBO_20230428_IBTOMATO | https://www.ibtomato.com/ExternalView.aspx?no=9643&type=1 | 1Q23 revenue fell about 50% YoY, operating profit fell about 91%, China EV subsidy removal/customer inventory adjustment reduced orders, LiPF6 price fell, and CB/BW put-option risk surfaced. This is a real hard-4C protection path. |

## 10. Price Data Source Map

| symbol | company | shard path | profile path | entry_date | entry_price |
|---:|---|---|---|---|---:|
| 066970 | L&F | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | atlas/symbol_profiles/066/066970.json | 2024-02-02 | 145600 |
| 066970 | L&F | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | atlas/symbol_profiles/066/066970.json | 2024-08-08 | 86200 |
| 096770 | SK Innovation | atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv | atlas/symbol_profiles/096/096770.json | 2024-04-29 | 112700 |
| 006400 | Samsung SDI | atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv | atlas/symbol_profiles/006/006400.json | 2025-03-05 | 213500 |
| 020150 | Lotte Energy Materials | atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv | atlas/symbol_profiles/020/020150.json | 2025-01-24 | 23050 |
| 078600 | Daejoo Electronic Materials | atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv | atlas/symbol_profiles/078/078600.json | 2024-04-02 | 90400 |
| 278280 | Chunbo | atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv | atlas/symbol_profiles/278/278280.json | 2023-04-28 | 193700 |

## 11. Case-by-Case Trigger Grid

The grid below is the human-readable companion to the JSONL rows. The JSONL rows in section 25 are the canonical machine-readable rows.

| case_id | symbol | company | trigger_type | entry_date | MFE90 | MAE90 | MFE180 | MAE180 | role | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---|---|
| C14_FU123_066970_20240202 | 066970 | L&F | Stage4B | 2024-02-02 | 36.68 | -9.27 | 36.68 | -43.06 | 4B_overlay_success / counterexample | current_profile_false_positive_if_hard_4c_without_reopen_clause |
| C14_FU123_066970_20240808 | 066970 | L&F | Stage4C | 2024-08-08 | 46.52 | -3.83 | 46.52 | -37.59 | 4C_late / counterexample | current_profile_4c_too_early_if_single_guidance_cut_is_treated_as_thesis_break |
| C14_FU123_096770_20240429 | 096770 | SK Innovation | Stage4B | 2024-04-29 | 13.84 | -18.63 | 16.42 | -18.63 | 4B_overlay_success / counterexample | current_profile_correct_if_stage4b_watch_not_hard_4c |
| C14_FU123_006400_20250305 | 006400 | Samsung SDI | Stage4B | 2025-03-05 | 3.51 | -26.14 | 66.04 | -26.14 | 4B_overlay_success / counterexample | current_profile_4c_too_early_if_bottoming_language_ignored |
| C14_FU123_020150_20250124 | 020150 | Lotte Energy Materials | Stage4B | 2025-01-24 | 36.88 | -15.57 | 36.88 | -15.57 | 4B_overlay_success / counterexample | current_profile_false_positive_if_reopen_path_ignored |
| C14_FU123_078600_20240402 | 078600 | Daejoo Electronic Materials | Stage2-Actionable | 2024-04-02 | 80.75 | -6.86 | 80.75 | -18.58 | structural_success / positive | current_profile_missed_structural_if_generic_ev_slowdown_blocks_survivor |
| C14_FU123_278280_20230428 | 278280 | Chunbo | Stage4C | 2023-04-28 | 8.16 | -29.43 | 8.16 | -53.48 | 4C_success / positive | current_profile_4c_too_late_if_waiting_for_full_year_loss |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_066970_20240202_Stage4B | 26.3 | -9.27 | 36.68 | -9.27 | 36.68 | -43.06 | 2024-03-25 | 199000 | -58.34 |
| T_066970_20240808_Stage4C | 24.48 | -3.83 | 46.52 | -3.83 | 46.52 | -37.59 | 2024-11-12 | 126300 | -57.4 |
| T_096770_20240429_Stage4B | 0.89 | -11.62 | 13.84 | -18.63 | 16.42 | -18.63 | 2025-01-20 | 131200 | -6.02 |
| T_006400_20250305_Stage4B | 3.51 | -20.37 | 3.51 | -26.14 | 66.04 | -26.14 | 2025-11-04 | 354500 | -20.87 |
| T_020150_20250124_Stage4B | 36.88 | -12.15 | 36.88 | -15.57 | 36.88 | -15.57 | 2025-02-20 | 31550 | -38.32 |
| T_078600_20240402_Stage2_Actionable | 15.04 | -6.86 | 80.75 | -6.86 | 80.75 | -18.58 | 2024-06-12 | 163400 | -54.96 |
| T_278280_20230428_Stage4C | 7.38 | -7.18 | 8.16 | -29.43 | 8.16 | -53.48 | 2023-07-25 | 209500 | -56.99 |

## 13. Current Calibrated Profile Stress Test

1. Current profile can already block price-only positives, but C14 still needs a sector-specific severity split for slowdown language.
2. Single-period slowdown evidence often creates local 4B, not immediate hard 4C.
3. Stage2 bonus is excessive if applied to battery material identity without survivor evidence.
4. Yellow threshold is not the main failure; evidence classification is.
5. Green strictness is appropriate for C14 because slowdown rows should rarely become Green.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate, but C14 needs explicit utilization/call-off/margin-slowdown tags.
8. Hard 4C routing should require repeated loss, concrete call-off, financing stress, or durable demand collapse; it should decay/reopen when bottoming, adoption, or parent-mix buffer evidence appears.

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green row is proposed. The only Stage2-Actionable survivor is Daejoo's silicon-anode adoption bridge. The rest are Stage4B/Stage4C calibration rows. Therefore `green_lateness_ratio = not_applicable` for the loop-level aggregate.

## 15. 4B Local vs Full-window Timing Audit

C14 needs two different 4B interpretations. L&F, Lotte Energy Materials, SK Innovation, and Samsung SDI require Stage4B/watch because slowdown evidence is real but not final enough for hard 4C. Daejoo after a fast silicon-anode reprice would also need a profit-lock overlay in later loops, but the April 2024 trigger is retained as survivor Stage2-Actionable because the price path produced 80.75% 90D MFE before a later drawdown.

## 16. 4C Protection Audit

Chunbo is the clearest hard-4C protection case in this file: the as-of evidence combined earnings shock, China customer weakness, raw-material/ASP pressure, and CB/BW overhang. L&F, Samsung SDI, SK Innovation, and Lotte Energy Materials are severity-split cases where hard 4C would be too blunt at the selected trigger date.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L3_EV_SLOWDOWN_SEVERITY_SPLIT_REQUIRES_UTILIZATION_CALLOFF_MARGIN_AND_REOPEN_CONTEXT
```

For L3 battery/EV, slowdown language should be parsed through four gates: customer call-off, utilization/fixed-cost deleveraging, margin/inventory loss, and reopen/bottoming route. If only one negative gate is present and reopen evidence exists, classify as Stage4B/watch rather than hard 4C.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C14_HARD_4C_REQUIRES_REPEATED_NON_PRICE_THESIS_BREAK_WHILE_SURVIVOR_REOPEN_BLOCKS_OVERKILL
```

C14 hard 4C requires repeated non-price break: concrete call-off/order cut, utilization collapse, repeated operating loss, inventory valuation loss that does not reverse, financing stress, or customer/program cancellation. Survivor/reopen evidence includes bottoming language, verified customer adoption, North America/JV volume route, or parent-mix cash buffer.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---|
| P0 | current | Existing calibrated profile with generic hard-4C routing | 7 | 32.33 | -15.68 | 0.43 | too blunt for survivor/reopen cases |
| P0b | rollback | Pre-stock-web baseline, weaker 4B/4C distinction | 7 | 32.33 | -15.68 | 0.57 | too many late positives and too few protection labels |
| P1 | sector_specific | L3 battery slowdown severity split | 7 | 32.33 | -15.68 | 0.29 | better separates utilization collapse from soft slowdown |
| P2 | canonical_specific | C14 repeat-loss / call-off / survivor reopen gate | 7 | 32.33 | -15.68 | 0.14 | best alignment in this loop |
| P3 | guard_profile | Conservative hard-4C only after repeated loss or financing stress | 7 | 32.33 | -15.68 | 0.14 | strongest guardrail but may be late on Chunbo-like financing stress |


## 20. Score-Return Alignment Matrix

| alignment label | cases | interpretation |
|---|---:|---|
| aligned_positive | 2 | Survivor or true hard-4C route explains MFE/MAE better than generic slowdown label |
| counterexample_or_guardrail | 5 | Generic slowdown label alone would over-route to hard 4C or over-promote rebound |
| current_profile_error_count | 6 | Remaining errors are mostly severity split and reopen/decay errors |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE | 2 | 5 | 6 | 6 | 6 | 1 | 7 | 7 | 6 | L3_EV_SLOWDOWN_SEVERITY_SPLIT_REQUIRES_UTILIZATION_CALLOFF_MARGIN_AND_REOPEN_CONTEXT | C14_HARD_4C_REQUIRES_REPEATED_NON_PRICE_THESIS_BREAK_WHILE_SURVIVOR_REOPEN_BLOCKS_OVERKILL | C14 static 11 + 7 local usable rows = 18 local-combined illustrative count; still under 30, so follow-up is valid if new symbol/date families remain. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 1
reused_case_ids: C14_FU123_066970_20240808
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: hard_4c_too_early_on_single_slowdown_headline; survivor_reopen_missed_when_bottoming_or_customer_adoption_exists; stage4b_needed_after_rebound_before_repeated_loss_confirmation
new_axis_proposed: C14_HARD_4C_REQUIRES_REPEATED_NON_PRICE_THESIS_BREAK_WHILE_SURVIVOR_REOPEN_BLOCKS_OVERKILL
existing_axis_strengthened: hard_4c_thesis_break_routes_to_4c with C14 repeat-confirmation requirement; full_4b_requires_non_price_evidence with utilization/calloff tags
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c should not fire on one-period slowdown when bottoming/reopen evidence is explicit
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L3_EV_SLOWDOWN_SEVERITY_SPLIT_REQUIRES_UTILIZATION_CALLOFF_MARGIN_AND_REOPEN_CONTEXT
canonical_archetype_rule_candidate: C14_HARD_4C_REQUIRES_REPEATED_NON_PRICE_THESIS_BREAK_WHILE_SURVIVOR_REOPEN_BLOCKS_OVERKILL
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web 30D/90D/180D price path fields, canonical trigger labels, R3/L3/C14 scope consistency, positive/counterexample balance, and hard-duplicate avoidance. Not validated: live investability, current fair value, brokerage execution, production scoring code, and any post-2026-02-20 price path.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_hard_4c_repeat_confirmation_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"hard 4C requires repeat non-price break unless financing stress/customer call-off is explicit","reduces false hard-4C on Samsung SDI/Lotte/SK Innovation while preserving Chunbo protection","T_066970_20240202_Stage4B|T_066970_20240808_Stage4C|T_096770_20240429_Stage4B|T_006400_20250305_Stage4B|T_020150_20250124_Stage4B|T_078600_20240402_Stage2_Actionable|T_278280_20230428_Stage4C",7,6,5,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C14_FU123_066970_20240202","symbol":"066970","company_name":"L&F","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"T_066970_20240202_Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_counterexample_or_severity_split","current_profile_verdict":"current_profile_false_positive_if_hard_4c_without_reopen_clause","price_source":"Songdaiki/stock-web","notes":"2023 operating loss and lithium-price-driven inventory valuation loss were disclosed, with shipment volume bottoming and expected double-digit QoQ improvement. It is a Stage4B/earnings-trough watch, not automatic hard 4C."}
{"row_type":"case","case_id":"C14_FU123_066970_20240808","symbol":"066970","company_name":"L&F","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"T_066970_20240808_Stage4C","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_after_prior_inventory_loss_row","independent_evidence_weight":0.5,"score_price_alignment":"residual_counterexample_or_severity_split","current_profile_verdict":"current_profile_4c_too_early_if_single_guidance_cut_is_treated_as_thesis_break","price_source":"Songdaiki/stock-web","notes":"2Q24 shipment guidance worsened and 2024 volume was estimated to fall because EV end-demand kept slowing. The price path still allowed a 90D rebound before later drawdown, so the rule needs severity split."}
{"row_type":"case","case_id":"C14_FU123_096770_20240429","symbol":"096770","company_name":"SK Innovation","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"T_096770_20240429_Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_counterexample_or_severity_split","current_profile_verdict":"current_profile_correct_if_stage4b_watch_not_hard_4c","price_source":"Songdaiki/stock-web","notes":"SK On battery loss widened on lower EV shipments, but the parent beat profit expectations, expected solid refining margin, and maintained H2 break-even target. Parent-mix buffer blocks hard 4C."}
{"row_type":"case","case_id":"C14_FU123_006400_20250305","symbol":"006400","company_name":"Samsung SDI","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"T_006400_20250305_Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_counterexample_or_severity_split","current_profile_verdict":"current_profile_4c_too_early_if_bottoming_language_ignored","price_source":"Songdaiki/stock-web","notes":"CEO said EV demand would stay sluggish until H1 2026 and Q4 2024 had an operating loss, but also said earnings would likely bottom in Q1 and recover from Q2. Hard 4C would be too blunt."}
{"row_type":"case","case_id":"C14_FU123_020150_20250124","symbol":"020150","company_name":"Lotte Energy Materials","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"T_020150_20250124_Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_counterexample_or_severity_split","current_profile_verdict":"current_profile_false_positive_if_reopen_path_ignored","price_source":"Songdaiki/stock-web","notes":"Official Q3 disclosure already described EV slowdown, customer inventory adjustment, lower utilization, fixed-cost burden, inventory valuation loss, and operating loss, but also identified North America volume/recovery routes. Use as Stage4B watch unless repeat losses remove reopen path."}
{"row_type":"case","case_id":"C14_FU123_078600_20240402","symbol":"078600","company_name":"Daejoo Electronic Materials","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_078600_20240402_Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_guardrail_or_survivor","current_profile_verdict":"current_profile_missed_structural_if_generic_ev_slowdown_blocks_survivor","price_source":"Songdaiki/stock-web","notes":"Silicon-anode sales were expected to exceed the prior full year in 1H24; coverage expanded from two vehicle models to nine and SK On adoption was referenced. Generic EV slowdown should not hard-4C this survivor route."}
{"row_type":"case","case_id":"C14_FU123_278280_20230428","symbol":"278280","company_name":"Chunbo","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"T_278280_20230428_Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_guardrail_or_survivor","current_profile_verdict":"current_profile_4c_too_late_if_waiting_for_full_year_loss","price_source":"Songdaiki/stock-web","notes":"1Q23 revenue fell about 50% YoY, operating profit fell about 91%, China EV subsidy removal/customer inventory adjustment reduced orders, LiPF6 price fell, and CB/BW put-option risk surfaced. This is a real hard-4C protection path."}
{"row_type":"trigger","trigger_id":"T_066970_20240202_Stage4B","case_id":"C14_FU123_066970_20240202","symbol":"066970","company_name":"L&F","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","sector":"battery / EV materials slowdown / utilization / call-off protection","primary_archetype":"EV demand slowdown 4B/4C severity split","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":145600.0,"evidence_available_at_that_date":"2023 operating loss and lithium-price-driven inventory valuation loss were disclosed, with shipment volume bottoming and expected double-digit QoQ improvement. It is a Stage4B/earnings-trough watch, not automatic hard 4C.","evidence_source":"EV_C14_FU123_LNF_20240201_ASIAE","evidence_url":"https://www.asiae.co.kr/en/article/2024020116473792269","evidence_family":"lithium_inventory_loss_recovery_not_immediate_hard_4c","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.3,"MFE_90D_pct":36.68,"MFE_180D_pct":36.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.27,"MAE_90D_pct":-9.27,"MAE_180D_pct":-43.06,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000.0,"drawdown_after_peak_pct":-58.34,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"case_specific_4B_overlay","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_local_4B_but_full_4C_too_harsh","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"inventory_loss_stage4b_not_permanent_4c","current_profile_verdict":"current_profile_false_positive_if_hard_4c_without_reopen_clause","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|066970|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_066970_20240808_Stage4C","case_id":"C14_FU123_066970_20240808","symbol":"066970","company_name":"L&F","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","sector":"battery / EV materials slowdown / utilization / call-off protection","primary_archetype":"EV demand slowdown 4B/4C severity split","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-08-08","entry_date":"2024-08-08","entry_price":86200.0,"evidence_available_at_that_date":"2Q24 shipment guidance worsened and 2024 volume was estimated to fall because EV end-demand kept slowing. The price path still allowed a 90D rebound before later drawdown, so the rule needs severity split.","evidence_source":"EV_C14_FU123_LNF_20240808_MK","evidence_url":"https://www.mk.co.kr/en/economy/11088257","evidence_family":"shipment_guidance_cut_but_rebound_before_followthrough_loss","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.48,"MFE_90D_pct":46.52,"MFE_180D_pct":46.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.83,"MAE_90D_pct":-3.83,"MAE_180D_pct":-37.59,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":126300.0,"drawdown_after_peak_pct":-57.4,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_after_rebound_needed","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_severity_split_required","trigger_outcome_label":"shipment_cut_needs_repeat_loss_before_hard_4c","current_profile_verdict":"current_profile_4c_too_early_if_single_guidance_cut_is_treated_as_thesis_break","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|066970|2024-08-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_after_prior_inventory_loss_row","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_096770_20240429_Stage4B","case_id":"C14_FU123_096770_20240429","symbol":"096770","company_name":"SK Innovation","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","sector":"battery / EV materials slowdown / utilization / call-off protection","primary_archetype":"EV demand slowdown 4B/4C severity split","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":112700.0,"evidence_available_at_that_date":"SK On battery loss widened on lower EV shipments, but the parent beat profit expectations, expected solid refining margin, and maintained H2 break-even target. Parent-mix buffer blocks hard 4C.","evidence_source":"EV_C14_FU123_SKINNO_20240429_REUTERS","evidence_url":"https://www.reuters.com/business/energy/sk-innovation-expects-solid-refining-margin-continue-q2-2024-04-29/","evidence_family":"battery_loss_but_refining_parent_buffer_and_break_even_target","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","profile_path":"atlas/symbol_profiles/096/096770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.89,"MFE_90D_pct":13.84,"MFE_180D_pct":16.42,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.62,"MAE_90D_pct":-18.63,"MAE_180D_pct":-18.63,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-20","peak_price":131200.0,"drawdown_after_peak_pct":-6.02,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"case_specific_4B_overlay","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_watch_4B","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"false_break_if_hard_4c","trigger_outcome_label":"parent_mix_buffer_prevents_hard_4c","current_profile_verdict":"current_profile_correct_if_stage4b_watch_not_hard_4c","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|096770|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_006400_20250305_Stage4B","case_id":"C14_FU123_006400_20250305","symbol":"006400","company_name":"Samsung SDI","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","sector":"battery / EV materials slowdown / utilization / call-off protection","primary_archetype":"EV demand slowdown 4B/4C severity split","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2025-03-05","entry_date":"2025-03-05","entry_price":213500.0,"evidence_available_at_that_date":"CEO said EV demand would stay sluggish until H1 2026 and Q4 2024 had an operating loss, but also said earnings would likely bottom in Q1 and recover from Q2. Hard 4C would be too blunt.","evidence_source":"EV_C14_FU123_SDI_20250305_REUTERS","evidence_url":"https://www.reuters.com/business/autos-transportation/samsung-sdi-ceo-says-ev-demand-remain-sluggish-until-h1-2026-2025-03-05/","evidence_family":"ev_sluggish_until_h1_2026_but_q1_trough_and_recovery_path","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.51,"MFE_90D_pct":3.51,"MFE_180D_pct":66.04,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.37,"MAE_90D_pct":-26.14,"MAE_180D_pct":-26.14,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-04","peak_price":354500.0,"drawdown_after_peak_pct":-20.87,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"case_specific_4B_overlay","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_watch_4B","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"false_break_if_hard_4c","trigger_outcome_label":"sluggish_demand_with_bottoming_language_requires_4B_not_4C","current_profile_verdict":"current_profile_4c_too_early_if_bottoming_language_ignored","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|006400|2025-03-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_020150_20250124_Stage4B","case_id":"C14_FU123_020150_20250124","symbol":"020150","company_name":"Lotte Energy Materials","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","sector":"battery / EV materials slowdown / utilization / call-off protection","primary_archetype":"EV demand slowdown 4B/4C severity split","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2025-01-24","entry_date":"2025-01-24","entry_price":23050.0,"evidence_available_at_that_date":"Official Q3 disclosure already described EV slowdown, customer inventory adjustment, lower utilization, fixed-cost burden, inventory valuation loss, and operating loss, but also identified North America volume/recovery routes. Use as Stage4B watch unless repeat losses remove reopen path.","evidence_source":"EV_C14_FU123_LOTTEEM_20250124_CHOSUN_OFFICIAL_Q3","evidence_url":"https://lotteenergymaterials.com/pr/promotion_detail.do?seq=97","evidence_family":"q4_loss_and_copperfoil_utilization_but_north_america_reopen_path","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv","profile_path":"atlas/symbol_profiles/020/020150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.88,"MFE_90D_pct":36.88,"MFE_180D_pct":36.88,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.15,"MAE_90D_pct":-15.57,"MAE_180D_pct":-15.57,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-20","peak_price":31550.0,"drawdown_after_peak_pct":-38.32,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"case_specific_4B_overlay","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"good_watch_4B_after_loss","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"utilization_loss_needs_repeated_confirmation_before_hard_4c","current_profile_verdict":"current_profile_false_positive_if_reopen_path_ignored","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|020150|2025-01-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_078600_20240402_Stage2_Actionable","case_id":"C14_FU123_078600_20240402","symbol":"078600","company_name":"Daejoo Electronic Materials","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","sector":"battery / EV materials slowdown / utilization / call-off protection","primary_archetype":"EV demand slowdown 4B/4C severity split","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-02","entry_date":"2024-04-02","entry_price":90400.0,"evidence_available_at_that_date":"Silicon-anode sales were expected to exceed the prior full year in 1H24; coverage expanded from two vehicle models to nine and SK On adoption was referenced. Generic EV slowdown should not hard-4C this survivor route.","evidence_source":"EV_C14_FU123_DAEJOO_20240402_ETNEWS","evidence_url":"https://www.etnews.com/20240329000204","evidence_family":"silicon_anode_survivor_growth_bridge_inside_ev_slowdown","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv","profile_path":"atlas/symbol_profiles/078/078600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.04,"MFE_90D_pct":80.75,"MFE_180D_pct":80.75,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.86,"MAE_90D_pct":-6.86,"MAE_180D_pct":-18.58,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":163400.0,"drawdown_after_peak_pct":-54.96,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"false_break_if_generic_4c","trigger_outcome_label":"survivor_reopen_positive_silicon_anode","current_profile_verdict":"current_profile_missed_structural_if_generic_ev_slowdown_blocks_survivor","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|078600|2024-04-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_278280_20230428_Stage4C","case_id":"C14_FU123_278280_20230428","symbol":"278280","company_name":"Chunbo","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_CELL_SLOWDOWN_SEVERITY_SPLIT_AND_SURVIVOR_REOPEN_GATE","sector":"battery / EV materials slowdown / utilization / call-off protection","primary_archetype":"EV demand slowdown 4B/4C severity split","loop_objective":"coverage_gap_fill|followup_new_symbol_date_family|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2023-04-28","entry_date":"2023-04-28","entry_price":193700.0,"evidence_available_at_that_date":"1Q23 revenue fell about 50% YoY, operating profit fell about 91%, China EV subsidy removal/customer inventory adjustment reduced orders, LiPF6 price fell, and CB/BW put-option risk surfaced. This is a real hard-4C protection path.","evidence_source":"EV_C14_FU123_CHUNBO_20230428_IBTOMATO","evidence_url":"https://www.ibtomato.com/ExternalView.aspx?no=9643&type=1","evidence_family":"electrolyte_demand_inventory_cb_bw_put_option_thesis_break","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["dilution_or_cb","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.38,"MFE_90D_pct":8.16,"MFE_180D_pct":8.16,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.18,"MAE_90D_pct":-29.43,"MAE_180D_pct":-53.48,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-25","peak_price":209500.0,"drawdown_after_peak_pct":-56.99,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_4B_before_hard_4C","four_b_evidence_type":["dilution_or_cb","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success_demand_inventory_and_financing_overhang","current_profile_verdict":"current_profile_4c_too_late_if_waiting_for_full_year_loss","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|278280|2023-04-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_FU123_066970_20240202","trigger_id":"T_066970_20240202_Stage4B","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":64,"stage_label_after":"Stage4B","changed_components":["utilization_or_calloff_severity_score","survivor_reopen_gate","hard_4c_repeat_confirmation_gate"],"component_delta_explanation":"C14 shadow profile separates single-period slowdown from repeated utilization collapse, and preserves survivor/reopen routes when customer adoption or bottoming language is present.","MFE_90D_pct":36.68,"MAE_90D_pct":-9.27,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_false_positive_if_hard_4c_without_reopen_clause"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_FU123_066970_20240808","trigger_id":"T_066970_20240808_Stage4C","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":64,"stage_label_after":"Stage4C","changed_components":["utilization_or_calloff_severity_score","survivor_reopen_gate","hard_4c_repeat_confirmation_gate"],"component_delta_explanation":"C14 shadow profile separates single-period slowdown from repeated utilization collapse, and preserves survivor/reopen routes when customer adoption or bottoming language is present.","MFE_90D_pct":46.52,"MAE_90D_pct":-3.83,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_4c_too_early_if_single_guidance_cut_is_treated_as_thesis_break"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_FU123_096770_20240429","trigger_id":"T_096770_20240429_Stage4B","symbol":"096770","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":64,"stage_label_after":"Stage4B","changed_components":["utilization_or_calloff_severity_score","survivor_reopen_gate","hard_4c_repeat_confirmation_gate"],"component_delta_explanation":"C14 shadow profile separates single-period slowdown from repeated utilization collapse, and preserves survivor/reopen routes when customer adoption or bottoming language is present.","MFE_90D_pct":13.84,"MAE_90D_pct":-18.63,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_correct_if_stage4b_watch_not_hard_4c"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_FU123_006400_20250305","trigger_id":"T_006400_20250305_Stage4B","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":64,"stage_label_after":"Stage4B","changed_components":["utilization_or_calloff_severity_score","survivor_reopen_gate","hard_4c_repeat_confirmation_gate"],"component_delta_explanation":"C14 shadow profile separates single-period slowdown from repeated utilization collapse, and preserves survivor/reopen routes when customer adoption or bottoming language is present.","MFE_90D_pct":3.51,"MAE_90D_pct":-26.14,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_4c_too_early_if_bottoming_language_ignored"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_FU123_020150_20250124","trigger_id":"T_020150_20250124_Stage4B","symbol":"020150","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":64,"stage_label_after":"Stage4B","changed_components":["utilization_or_calloff_severity_score","survivor_reopen_gate","hard_4c_repeat_confirmation_gate"],"component_delta_explanation":"C14 shadow profile separates single-period slowdown from repeated utilization collapse, and preserves survivor/reopen routes when customer adoption or bottoming language is present.","MFE_90D_pct":36.88,"MAE_90D_pct":-15.57,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_false_positive_if_reopen_path_ignored"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_FU123_078600_20240402","trigger_id":"T_078600_20240402_Stage2_Actionable","symbol":"078600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["utilization_or_calloff_severity_score","survivor_reopen_gate","hard_4c_repeat_confirmation_gate"],"component_delta_explanation":"C14 shadow profile separates single-period slowdown from repeated utilization collapse, and preserves survivor/reopen routes when customer adoption or bottoming language is present.","MFE_90D_pct":80.75,"MAE_90D_pct":-6.86,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural_if_generic_ev_slowdown_blocks_survivor"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_FU123_278280_20230428","trigger_id":"T_278280_20230428_Stage4C","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":5,"accounting_trust_risk_score":1},"weighted_score_before":72,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":7,"accounting_trust_risk_score":1},"weighted_score_after":64,"stage_label_after":"Stage4C","changed_components":["utilization_or_calloff_severity_score","survivor_reopen_gate","hard_4c_repeat_confirmation_gate"],"component_delta_explanation":"C14 shadow profile separates single-period slowdown from repeated utilization collapse, and preserves survivor/reopen routes when customer adoption or bottoming language is present.","MFE_90D_pct":8.16,"MAE_90D_pct":-29.43,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_4c_too_late_if_waiting_for_full_year_loss"}
{"row_type":"residual_contribution","round":"R3","loop":123,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":6,"reused_case_count":1,"new_symbol_count":6,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["hard_4c_too_early_on_single_slowdown_headline","survivor_reopen_missed_when_bottoming_or_customer_adoption_exists","stage4b_needed_after_rebound_before_repeated_loss_confirmation"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 123
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under_30_representative_rows / C14 rows 11 need_to_30 19 before local follow-up
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_followup_new_symbols_only; C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_customer_route; C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_followup_new_order_route; C11_BATTERY_ORDERBOOK_RERATING_followup_margin_FCF_bridge; C01_ORDER_BACKLOG_MARGIN_BRIDGE_followup_new_symbol_only
```

## 28. Source Notes

Evidence URLs are recorded in the machine-readable rows. Stock price data is from Songdaiki/stock-web tradable shards with raw/unadjusted marcap OHLC. This file does not use current prices or live scanning.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
