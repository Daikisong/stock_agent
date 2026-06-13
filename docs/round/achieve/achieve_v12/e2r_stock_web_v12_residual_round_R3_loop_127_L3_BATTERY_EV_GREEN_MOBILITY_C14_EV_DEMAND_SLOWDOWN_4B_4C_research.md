# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R3
selected_loop = 127
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = mixed_c14_demand_slowdown_calloff_utilization_customer_offset_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R3/L3/C14.

## 1. Current Calibrated Profile Assumption

The working proxy remains `e2r_2_1_stock_web_calibrated_proxy`: Stage2 actionable evidence bonus exists, Green is strict, price-only blowoff does not promote positive stage, full 4B requires non-price evidence, and hard 4C requires thesis-break evidence. This MD does not modify production scoring. It only creates a C14-specific shadow rule candidate.

## 2. Round / Large Sector / Canonical Archetype Scope

C14 belongs to R3 / L3. The selected scope is not a general battery orderbook rerating study. It is the defensive EV-demand-slowdown branch: customer inventory adjustment, utilization loss, customer call-off, ASP collapse, loss conversion, and the timing boundary between Stage4B watch and hard Stage4C.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index marks C14 as Priority 0 with 11 rows, needing 19 additional rows to reach the 30-row minimum stability zone and 39 additional rows to reach the 50-row practical calibration zone. The latest top C14 covered symbols shown in the index are not used as the core set here. This loop uses 003670, 278280, 393890, and 336370. The second WCP trigger is same-symbol but a different trigger family: August 2024 Stage4B watch evidence versus November 2024 loss-conversion hard 4C confirmation.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest fields checked: source_name `FinanceData/marcap`, price_adjustment_status `raw_unadjusted_marcap`, max_date `2026-02-20`, calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`, raw_shard_root `atlas/ohlcv_raw_by_symbol_year`, schema_path `atlas/schema.json`, universe_path `atlas/universe/all_symbols.csv`.

## 5. Historical Eligibility Gate

All representative trigger rows have an entry date inside the stock-web tradable shard, an entry close, at least 180 forward trading rows, and complete `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`. The 180D windows are clean for corporate-action contamination. Solus had profile corporate-action candidates before the 2024-02-08 entry window; they do not overlap the 180D window. WCP has no profile corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| CATHODE_ASP_INVENTORY_MARGIN_SHOCK_RELIEF_RALLY | C14_EV_DEMAND_SLOWDOWN_4B_4C | Cathode price and inventory shock can be Stage4B first when backlog/customer offset leaves a relief-rally path. |
| ELECTROLYTE_LITHIUM_SALT_ASP_VOLUME_DELAY_4C | C14_EV_DEMAND_SLOWDOWN_4B_4C | Electrolyte/LiPF6 ASP collapse plus line conversion/shipment collapse is hard-4C evidence. |
| SEPARATOR_EV_DEMAND_RIVIAN_ORDER_CUT_LOW_MARGIN_WATCH | C14_EV_DEMAND_SLOWDOWN_4B_4C | Customer order cut plus low-margin separator evidence is Stage4B watch and requires later confirmation. |
| SEPARATOR_EV_CHASM_LOSS_CONVERSION_TARGET_CUT_4C | C14_EV_DEMAND_SLOWDOWN_4B_4C | Target cut, operating loss conversion, volume and OPM estimate cuts confirm hard 4C. |
| BATTERY_COPPER_FOIL_EV_SLOWDOWN_OFFSET_BY_CUSTOMER_SUPPLY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV slowdown vocabulary is blocked from hard 4C when customer-requested supply expansion offsets macro slowdown. |

## 7. Case Selection Summary

| case_id | symbol | company | trigger | role | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| C14_R3L127_003670_20240124 | 003670 | 포스코퓨처엠 | Stage4B | counterexample | 2024-01-24 | 261,000 | 30.65 | -7.85 | 30.65 | -25.10 | current_profile_4B_too_early |
| C14_R3L127_278280_20230823 | 278280 | 천보 | Stage4C | positive | 2023-08-23 | 139,800 | 11.52 | -31.19 | 11.52 | -49.07 | current_profile_correct |
| C14_R3L127_393890_20240807 | 393890 | 더블유씨피 | Stage4B | positive | 2024-08-07 | 21,000 | 5.24 | -48.38 | 5.24 | -67.86 | current_profile_4C_too_late |
| C14_R3L127_393890_20241122 | 393890 | 더블유씨피 | Stage4C | positive | 2024-11-22 | 12,140 | 11.12 | -42.26 | 11.12 | -44.40 | current_profile_correct |
| C14_R3L127_336370_20240208 | 336370 | 솔루스첨단소재 | Stage4C | counterexample | 2024-02-08 | 11,470 | 89.19 | -2.70 | 104.88 | -2.70 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 2
4C_case_count = 3
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
representative_trigger_count = 5
```

C14 is a protection archetype, so positive cases mean correct defensive labeling, not bullish rerating. Chunbo and WCP November are hard-4C successes. WCP August is a useful Stage4B watch success because the evidence did not yet fully break the thesis, but the later price path required escalation. POSCO Future M and Solus are counterexamples showing that slowdown vocabulary alone can be too early or false when order/customer/mix offset remains alive.

## 9. Evidence Source Map

| symbol | trigger_date | source | evidence interpretation |
|---:|---:|---|---|
| 003670 | 2024-01-23 | Yonhap News, https://www.yna.co.kr/view/AKR20240123125451003 | 2023 OP fell sharply; customer inventory adjustment, EV demand slowdown, and lithium/raw material price decline hurt profitability. |
| 278280 | 2023-08-22 | Dealsite, https://dealsite.co.kr/articles/108862/068020 | LiPF6 selling price decline, LiFSI line conversion and shipment collapse, EV demand below expectation; CB/BW funding was also a risk overlay. |
| 393890 | 2024-08-06 | Hana Securities PDF, https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/08/05/WCP_2Q24Re.pdf | Europe EV slowdown and customer Samsung SDI battery revenue decline; Rivian order cut; WCP still kept profit structure, so Stage4B watch rather than immediate hard 4C. |
| 393890 | 2024-11-22 | Energy Economy, https://m.ekn.kr/view.php?key=20241122027265331 | 4Q operating-loss conversion forecast, volume estimate cuts, OPM estimate cut, and target-price downgrade; hard 4C confirmation. |
| 336370 | 2024-02-07 | CEO Score Daily, https://www.ceoscoredaily.com/page/view/2024020717214677994 | Two-year operating loss and EV slowdown were real, but battery foil sales growth and customer-requested supply expansion created a hard-4C false break. |
| 336370 | 2025-02-06 | Solus official newsroom, https://www.solusadvancedmaterials.com/kr/media/newsDetail?id=106 | Later validation note: company said 2024 battery foil sales grew more than 60% and Hungary utilization exceeded 80% despite EV demand weakness. |

## 10. Price Data Source Map

| symbol | profile_path | entry shard | forward shard coverage | profile corporate-action status |
|---:|---|---|---|---|
| 003670 | atlas/symbol_profiles/003/003670.json | atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv | 2024 | profile candidates 2015-05-04, 2021-02-03; no 180D overlap |
| 278280 | atlas/symbol_profiles/278/278280.json | atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv | 2023-2024 | no corporate-action candidate |
| 393890 | atlas/symbol_profiles/393/393890.json | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | 2024-2025 | no corporate-action candidate |
| 336370 | atlas/symbol_profiles/336/336370.json | atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv | 2024 | profile candidates 2024-01-08, 2024-01-30; before entry and no 180D overlap |

## 11. Case-by-Case Trigger Grid

### Case 1 — POSCO Future M / 003670 / Stage4B too early counterexample

The evidence was severe: earnings shock, EV demand slowdown, customer inventory adjustment, and lithium price decline. But the price path still delivered +30.65% MFE in 90D/180D before the 180D low. C14 should not promote this to hard 4C on slowdown language alone. The better label is Stage4B thesis-break watch with customer/utilization confirmation pending.

### Case 2 — Chunbo / 278280 / hard 4C success

The evidence contained ASP decline, product line conversion, shipment collapse, and EV demand below expectation. That is not just macro slowdown vocabulary; it is a volume-price-execution break. The 180D MAE reached -49.07%, and the 180D MFE was only +11.52%.

### Case 3 — WCP / 393890 / August 2024 Stage4B watch success

August evidence showed customer order pressure and low-margin conditions, but also said WCP maintained a profit structure. This should not be hard 4C yet. It is a Stage4B watch row that becomes highly useful because the subsequent path was very weak, with 180D MAE -67.86%.

### Case 4 — WCP / 393890 / November 2024 hard 4C success

By November, the same symbol had a different trigger family: operating-loss conversion forecast, estimate cuts, and target-price downgrade. This is the confirmation layer that turns the August watch into hard 4C. It also provides a clean same-symbol new-trigger-family sample.

### Case 5 — Solus Advanced Materials / 336370 / false 4C break

Solus shows the opposite edge: loss and EV slowdown text existed, but battery foil growth and customer-requested supply expansion were already visible. The 180D path gave +104.88% MFE and -2.70% MAE. Later official company commentary confirmed that 2024 battery foil sales expanded strongly despite EV front-industry weakness.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | clean window |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TRG_C14_R3L127_003670_20240124 | 2024-01-24 | 261,000 | 28.93 | -7.85 | 30.65 | -7.85 | 30.65 | -25.10 | 2024-03-13 | 341,000 | -42.67 | clean_180D_window |
| TRG_C14_R3L127_278280_20230823 | 2023-08-23 | 139,800 | 11.52 | -16.88 | 11.52 | -31.19 | 11.52 | -49.07 | 2023-08-30 | 155,900 | -54.33 | clean_180D_window |
| TRG_C14_R3L127_393890_20240807 | 2024-08-07 | 21,000 | 5.24 | -20.00 | 5.24 | -48.38 | 5.24 | -67.86 | 2024-08-16 | 22,100 | -69.46 | clean_180D_window |
| TRG_C14_R3L127_393890_20241122 | 2024-11-22 | 12,140 | 11.12 | -11.37 | 11.12 | -42.26 | 11.12 | -44.40 | 2024-11-26 | 13,490 | -49.96 | clean_180D_window |
| TRG_C14_R3L127_336370_20240208 | 2024-02-08 | 11,470 | 24.67 | -2.70 | 89.19 | -2.70 | 104.88 | -2.70 | 2024-07-01 | 23,500 | -52.34 | clean_180D_window |


## 13. Current Calibrated Profile Stress Test

| case_id | likely current judgement | actual path alignment | residual diagnosis |
|---|---|---|---|
| C14_R3L127_003670_20240124 | Stage4B/4C risk because EV slowdown + earnings shock | Mixed: +30.65% MFE before -25.10% MAE | Hard 4C too early if triggered before customer/utilization confirmation. |
| C14_R3L127_278280_20230823 | Stage4C allowed because price/volume/execution break was explicit | Correct: 180D MAE -49.07% | Existing hard-4C axis kept and strengthened. |
| C14_R3L127_393890_20240807 | Stage4B watch; escalation may wait | Too late if never escalated: 180D MAE -67.86% | Need explicit watch-to-4C escalation rule. |
| C14_R3L127_393890_20241122 | Stage4C allowed after loss forecast/estimate cuts | Correct: 90D MAE -42.26%, 180D MAE -44.40% | Confirms hard 4C when non-price evidence is complete. |
| C14_R3L127_336370_20240208 | Naive C14 would hard-4C due loss + EV slowdown | Wrong: 180D MFE +104.88%, MAE -2.70% | Customer supply expansion and battery foil growth should block hard 4C. |

## 14. Stage2 / Yellow / Green Comparison

This loop is not a Green unlock study. No Stage3-Green row is proposed. C14 rows are defensive overlays: Stage4B and Stage4C. Green lateness is therefore `not_applicable`. The Stage comparison lesson is that an EV-demand-slowdown narrative must not erase positive Stage2 evidence when company-level customer share, utilization, or supply-growth offset is present.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B/4C timing verdict | local/full interpretation |
|---|---|---|
| 003670 | price_only_local_4B_too_early if made hard 4C immediately | Early evidence caught risk, but full hard 4C before the +30% relief path would be too harsh. |
| 278280 | hard_4c_success | Little post-trigger upside versus large drawdown; not merely local price overheat. |
| 393890 Aug | 4b_watch_success_needs_later_4c_confirmation | Watch signal was right; full 4C needed November confirmation. |
| 393890 Nov | hard_4c_success | Hard 4C was well-supported by non-price loss/estimate evidence. |
| 336370 | false_break | Hard 4C would have blocked a +104.88% 180D upside path. |

## 16. 4C Protection Audit

C14 needs a two-step protection map. First, Stage4B watch should fire on one-layer risk: demand slowdown, ASP decline, inventory adjustment, customer order softness, or low OPM. Second, hard Stage4C should require at least two confirmation layers: actual loss conversion or severe margin bridge break; customer call-off/order cut or utilization collapse; and lack of customer-share/order/mix offset.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L3_EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_GATE_V1
scope = L3_BATTERY_EV_GREEN_MOBILITY
rule = In L3, EV-demand-slowdown language alone should open Stage4B watch, not hard 4C. Hard 4C requires customer call-off/order cut or utilization collapse plus margin/loss confirmation. If customer share gain, supply expansion, or utilization offset exists, keep as watch or false-break review.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C14_CUSTOMER_OFFSET_AND_4C_CONFIRMATION_GATE_V1
scope = C14_EV_DEMAND_SLOWDOWN_4B_4C
positive defense examples = 278280_20230823, 393890_20241122
watch-to-4C escalation example = 393890_20240807 -> 393890_20241122
false-break examples = 003670_20240124, 336370_20240208
```

The rule behaves like a fire alarm with two sensors. Smoke from macro EV slowdown turns on watch. The sprinkler should release only when the heat sensor also confirms company-level call-off, utilization collapse, loss conversion, or thesis break.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | Existing hard 4C and 4B rules without C14 customer-offset nuance | 5 | 29.54 | -26.48 | 32.68 | -37.83 | 0.40 | 1 | mixed; too harsh on Solus/POSCOF, too late on WCP Aug escalation |
| P0b_e2r_2_0_baseline_reference | rollback reference | More likely to under-handle 4C protection and treat slowdown as generic cycle noise | 5 | 29.54 | -26.48 | 32.68 | -37.83 | 0.20 | 2 | weaker protection for Chunbo/WCP |
| P1_L3_sector_specific_candidate_profile | sector shadow | Require utilization/call-off/margin confirmation for hard 4C | 5 | 29.54 | -26.48 | 32.68 | -37.83 | 0.20 | 0 | better watch-vs-hard-4C separation |
| P2_C14_canonical_candidate_profile | canonical shadow | Add customer-offset blocker and escalation path from watch to hard 4C | 5 | 29.54 | -26.48 | 32.68 | -37.83 | 0.00 | 0 | best alignment in this case set |
| P3_counterexample_guard_profile | guard shadow | Block hard 4C if customer supply growth/utilization offset is explicit | 5 | 29.54 | -26.48 | 32.68 | -37.83 | 0.00 | 1 | prevents Solus false break but may need escalation trigger for WCP |

## 20. Score-Return Alignment Matrix

The component simulations are research proxies only. They are meant to describe why the case should move between watch and hard 4C; they are not production score output.

| case | before score direction | after score direction | alignment |
|---|---|---|---|
| POSCO Future M | too much hard-break risk if slowdown text dominates | lower hard-4C confidence until customer call-off/utilization confirmation | improves |
| Chunbo | high execution and dilution/CB risk, explicit volume/ASP break | stronger hard-4C confidence | improves |
| WCP Aug | watch, but escalation trigger not explicit enough | Stage4B watch plus escalation requirement | improves |
| WCP Nov | hard 4C already appropriate | hard 4C confirmed | kept |
| Solus | loss + EV slowdown could falsely dominate | customer supply/growth offset blocks hard 4C | improves |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed_c14_demand_slowdown_calloff_utilization_customer_offset_leaf_set | 3 | 2 | 2 | 3 | 5 | 0 | 5 | 5 | 3 | L3_EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_GATE_V1 | C14_CUSTOMER_OFFSET_AND_4C_CONFIRMATION_GATE_V1 | C14 rows 11 -> 16 if accepted; need 14 to 30, 34 to 50 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c|price_only_blowoff_blocks_positive_stage
residual_error_types_found: hard_4c_too_early_when_customer_offset_exists|hard_4c_too_late_after_watch_when_loss_confirmation_appears|4b_watch_needed_before_full_4c
new_axis_proposed: c14_customer_offset_and_4c_confirmation_gate
existing_axis_strengthened: full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_on_slowdown_vocabulary_alone
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L3_EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_GATE_V1
canonical_archetype_rule_candidate: C14_CUSTOMER_OFFSET_AND_4C_CONFIRMATION_GATE_V1
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical C14 defense-label calibration, clean 180D stock-web OHLC path, watch-vs-hard-4C timing, and customer-offset false-break control. Non-validation scope: live stock discovery, current investment recommendation, production scoring changes, or any brokerage/API workflow.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_customer_offset_and_4c_confirmation_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Hard 4C should require company-level confirmation and should be blocked by explicit customer supply/utilization offset.","Reduced false breaks in 003670/336370 while preserving protection in 278280/393890.","TRG_C14_R3L127_003670_20240124|TRG_C14_R3L127_278280_20230823|TRG_C14_R3L127_393890_20240807|TRG_C14_R3L127_393890_20241122|TRG_C14_R3L127_336370_20240208",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,l3_watch_to_hard_4c_escalation,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Stage4B watch should escalate when later loss conversion, volume estimate cut, or OPM cut appears.","WCP August watch plus November hard 4C creates a clean escalation ladder.","TRG_C14_R3L127_393890_20240807|TRG_C14_R3L127_393890_20241122",2,2,0,low,sector_shadow_only,"same symbol but different trigger family"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C14_R3L127_003670_20240124","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_ASP_INVENTORY_MARGIN_SHOCK_RELIEF_RALLY","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ev_slowdown_margin_shock_but_relief_rally_counterexample","current_profile_verdict":"current_profile_4B_too_early","price_source":"Songdaiki/stock-web","notes":"Demand slowdown and inventory adjustment were real, but 180D path still had +30.65% MFE before -25.10% MAE. C14 should use Stage4B watch first unless customer call-off/utilization evidence confirms hard 4C."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L127_003670_20240124","case_id":"C14_R3L127_003670_20240124","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_ASP_INVENTORY_MARGIN_SHOCK_RELIEF_RALLY","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-01-23","entry_date":"2024-01-24","entry_price":261000.0,"evidence_available_at_that_date":"Yonhap News, 2024-01-23, POSCO Future M 2023 earnings shock / EV demand slowdown / customer inventory / lithium price decline, https://www.yna.co.kr/view/AKR20240123125451003","evidence_source":"Yonhap News, 2024-01-23, POSCO Future M 2023 earnings shock / EV demand slowdown / customer inventory / lithium price decline, https://www.yna.co.kr/view/AKR20240123125451003","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.93,"MFE_90D_pct":30.65,"MFE_180D_pct":30.65,"MFE_1Y_pct":30.65,"MFE_2Y_pct":null,"MAE_30D_pct":-7.85,"MAE_90D_pct":-7.85,"MAE_180D_pct":-25.1,"MAE_1Y_pct":-52.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":341000.0,"drawdown_after_peak_pct":-42.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["margin_or_backlog_slowdown","valuation_blowoff","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"ev_slowdown_margin_shock_but_relief_rally_counterexample","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_003670_2024-01-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L127_003670_20240124","trigger_id":"TRG_C14_R3L127_003670_20240124","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":59.1,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":60.7,"stage_label_after":"Stage4B","changed_components":["customer_offset_gate","utilization_or_call_off_confirmation","loss_or_margin_confirmation"],"component_delta_explanation":"C14 shadow gate increases hard-4C confidence only when slowdown language is paired with customer call-off/utilization loss and margin/loss confirmation; it suppresses hard-4C when customer supply growth offsets macro slowdown.","MFE_90D_pct":30.65,"MAE_90D_pct":-7.85,"score_return_alignment_label":"ev_slowdown_margin_shock_but_relief_rally_counterexample","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"case","case_id":"C14_R3L127_278280_20230823","symbol":"278280","company_name":"천보","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"ELECTROLYTE_LITHIUM_SALT_ASP_VOLUME_DELAY_4C","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"electrolyte_price_volume_delay_hard_4c_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"This is a clean hard-4C protection sample: price had only +11.52% 180D MFE and -49.07% 180D MAE after the trigger."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L127_278280_20230823","case_id":"C14_R3L127_278280_20230823","symbol":"278280","company_name":"천보","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"ELECTROLYTE_LITHIUM_SALT_ASP_VOLUME_DELAY_4C","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2023-08-22","entry_date":"2023-08-23","entry_price":139800.0,"evidence_available_at_that_date":"Dealsite, 2023-08-22, Chunbo LiPF6 ASP decline, LiFSI line conversion / shipment collapse, EV demand below expectation, https://dealsite.co.kr/articles/108862/068020","evidence_source":"Dealsite, 2023-08-22, Chunbo LiPF6 ASP decline, LiFSI line conversion / shipment collapse, EV demand below expectation, https://dealsite.co.kr/articles/108862/068020","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","dilution_or_cb","execution_risk"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.52,"MFE_90D_pct":11.52,"MFE_180D_pct":11.52,"MFE_1Y_pct":11.52,"MFE_2Y_pct":null,"MAE_30D_pct":-16.88,"MAE_90D_pct":-31.19,"MAE_180D_pct":-49.07,"MAE_1Y_pct":-64.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-30","peak_price":155900.0,"drawdown_after_peak_pct":-54.33,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_prior_stage2_anchor","four_b_evidence_type":["margin_or_backlog_slowdown","dilution_or_cb","execution_risk"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"electrolyte_price_volume_delay_hard_4c_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_278280_2023-08-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L127_278280_20230823","trigger_id":"TRG_C14_R3L127_278280_20230823","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":5,"accounting_trust_risk_score":1},"weighted_score_before":34.4,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":10,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":6,"accounting_trust_risk_score":1},"weighted_score_after":30.0,"stage_label_after":"Stage4C","changed_components":["customer_offset_gate","utilization_or_call_off_confirmation","loss_or_margin_confirmation"],"component_delta_explanation":"C14 shadow gate increases hard-4C confidence only when slowdown language is paired with customer call-off/utilization loss and margin/loss confirmation; it suppresses hard-4C when customer supply growth offsets macro slowdown.","MFE_90D_pct":11.52,"MAE_90D_pct":-31.19,"score_return_alignment_label":"electrolyte_price_volume_delay_hard_4c_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C14_R3L127_393890_20240807","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_EV_DEMAND_RIVIAN_ORDER_CUT_LOW_MARGIN_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"separator_customer_order_cut_4b_watch_success","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Initial evidence still said profit structure held, so Stage4B watch was cleaner than hard 4C. But the path deteriorated severely: 180D MAE -67.86%, so the profile should escalate if later loss confirmation appears."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L127_393890_20240807","case_id":"C14_R3L127_393890_20240807","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_EV_DEMAND_RIVIAN_ORDER_CUT_LOW_MARGIN_WATCH","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-08-06","entry_date":"2024-08-07","entry_price":21000.0,"evidence_available_at_that_date":"Hana Securities PDF, 2024-08-06, WCP 2Q24 review; Europe EV demand slowdown, Samsung SDI battery revenue decline, Rivian cylindrical EV order cut, low OPM, https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/08/05/WCP_2Q24Re.pdf","evidence_source":"Hana Securities PDF, 2024-08-06, WCP 2Q24 review; Europe EV demand slowdown, Samsung SDI battery revenue decline, Rivian cylindrical EV order cut, low OPM, https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/08/05/WCP_2Q24Re.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.24,"MFE_90D_pct":5.24,"MFE_180D_pct":5.24,"MFE_1Y_pct":5.24,"MFE_2Y_pct":null,"MAE_30D_pct":-20.0,"MAE_90D_pct":-48.38,"MAE_180D_pct":-67.86,"MAE_1Y_pct":-67.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-16","peak_price":22100.0,"drawdown_after_peak_pct":-69.46,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4b_watch_success_needs_later_4c_confirmation","four_b_evidence_type":["margin_or_backlog_slowdown","contract_delay","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"separator_customer_order_cut_4b_watch_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_393890_2024-08-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L127_393890_20240807","trigger_id":"TRG_C14_R3L127_393890_20240807","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":50.5,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":48.9,"stage_label_after":"Stage4B","changed_components":["customer_offset_gate","utilization_or_call_off_confirmation","loss_or_margin_confirmation"],"component_delta_explanation":"C14 shadow gate increases hard-4C confidence only when slowdown language is paired with customer call-off/utilization loss and margin/loss confirmation; it suppresses hard-4C when customer supply growth offsets macro slowdown.","MFE_90D_pct":5.24,"MAE_90D_pct":-48.38,"score_return_alignment_label":"separator_customer_order_cut_4b_watch_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"case","case_id":"C14_R3L127_393890_20241122","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_EV_CHASM_LOSS_CONVERSION_TARGET_CUT_4C","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_after_prior_4B_watch","independent_evidence_weight":0.5,"score_price_alignment":"separator_loss_conversion_target_cut_hard_4c_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"This is the hard-4C confirmation following the August watch. 180D MFE was only +11.12% while 90D/180D MAE reached -42.26%/-44.40%."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L127_393890_20241122","case_id":"C14_R3L127_393890_20241122","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_EV_CHASM_LOSS_CONVERSION_TARGET_CUT_4C","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-11-22","entry_date":"2024-11-22","entry_price":12140.0,"evidence_available_at_that_date":"Energy Economy, 2024-11-22 08:40, KB Securities target cut, WCP 4Q operating loss forecast and separator volume/OPM estimate downgrade, https://m.ekn.kr/view.php?key=20241122027265331","evidence_source":"Energy Economy, 2024-11-22 08:40, KB Securities target cut, WCP 4Q operating loss forecast and separator volume/OPM estimate downgrade, https://m.ekn.kr/view.php?key=20241122027265331","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay","valuation_blowoff"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.12,"MFE_90D_pct":11.12,"MFE_180D_pct":11.12,"MFE_1Y_pct":11.12,"MFE_2Y_pct":null,"MAE_30D_pct":-11.37,"MAE_90D_pct":-42.26,"MAE_180D_pct":-44.4,"MAE_1Y_pct":-48.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-26","peak_price":13490.0,"drawdown_after_peak_pct":-49.96,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_prior_stage2_anchor","four_b_evidence_type":["margin_or_backlog_slowdown","contract_delay","valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"separator_loss_conversion_target_cut_hard_4c_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_393890_2024-11-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_after_prior_4B_watch","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L127_393890_20241122","trigger_id":"TRG_C14_R3L127_393890_20241122","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":9,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":36.0,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":10,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":34.4,"stage_label_after":"Stage4C","changed_components":["customer_offset_gate","utilization_or_call_off_confirmation","loss_or_margin_confirmation"],"component_delta_explanation":"C14 shadow gate increases hard-4C confidence only when slowdown language is paired with customer call-off/utilization loss and margin/loss confirmation; it suppresses hard-4C when customer supply growth offsets macro slowdown.","MFE_90D_pct":11.12,"MAE_90D_pct":-42.26,"score_return_alignment_label":"separator_loss_conversion_target_cut_hard_4c_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C14_R3L127_336370_20240208","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_COPPER_FOIL_EV_SLOWDOWN_OFFSET_BY_CUSTOMER_SUPPLY","case_type":"false_break","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ev_slowdown_keyword_false_4c_battery_foil_customer_offset","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"EV slowdown and loss language was real, but customer-requested supply expansion and battery foil growth made a hard 4C wrong. 180D MFE was +104.88% with only -2.70% MAE."}
{"row_type":"trigger","trigger_id":"TRG_C14_R3L127_336370_20240208","case_id":"C14_R3L127_336370_20240208","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_COPPER_FOIL_EV_SLOWDOWN_OFFSET_BY_CUSTOMER_SUPPLY","sector":"battery_ev_green_mobility","primary_archetype":"ev_demand_slowdown_4b_4c","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-02-07","entry_date":"2024-02-08","entry_price":11470.0,"evidence_available_at_that_date":"CEO Score Daily, 2024-02-07, Solus Advanced Materials two-year operating loss / EV market slowdown, but battery foil sales growth and 2024 customer-requested supply expansion target, https://www.ceoscoredaily.com/page/view/2024020717214677994","evidence_source":"CEO Score Daily, 2024-02-07, Solus Advanced Materials two-year operating loss / EV market slowdown, but battery foil sales growth and 2024 customer-requested supply expansion target, https://www.ceoscoredaily.com/page/view/2024020717214677994","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.67,"MFE_90D_pct":89.19,"MFE_180D_pct":104.88,"MFE_1Y_pct":104.88,"MFE_2Y_pct":null,"MAE_30D_pct":-2.7,"MAE_90D_pct":-2.7,"MAE_180D_pct":-2.7,"MAE_1Y_pct":-33.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-01","peak_price":23500.0,"drawdown_after_peak_pct":-52.34,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_prior_stage2_anchor","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"false_break","trigger_outcome_label":"ev_slowdown_keyword_false_4c_battery_foil_customer_offset","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_336370_2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L127_336370_20240208","trigger_id":"TRG_C14_R3L127_336370_20240208","symbol":"336370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":62.6,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":67.9,"stage_label_after":"Stage4C","changed_components":["customer_offset_gate","utilization_or_call_off_confirmation","loss_or_margin_confirmation"],"component_delta_explanation":"C14 shadow gate increases hard-4C confidence only when slowdown language is paired with customer call-off/utilization loss and margin/loss confirmation; it suppresses hard-4C when customer supply growth offsets macro slowdown.","MFE_90D_pct":89.19,"MAE_90D_pct":-2.7,"score_return_alignment_label":"ev_slowdown_keyword_false_4c_battery_foil_customer_offset","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"127","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["hard_4c_too_early_when_customer_offset_exists","hard_4c_too_late_after_watch_when_loss_confirmation_appears","4b_watch_needed_before_full_4c"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 127
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|C11_BATTERY_ORDERBOOK_RERATING|C01_ORDER_BACKLOG_MARGIN_BRIDGE|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

Next execution should re-read the latest `V12_Research_No_Repeat_Index.md` and avoid mechanical R1→R13 sequencing. If this C14 loop is accepted, C14 coverage moves from 11 to 16 representative rows, so C10 becomes the next lowest untouched Priority 0 candidate in this local session.

## 28. Source Notes

- `Songdaiki/stock-web` manifest/schema were used only for historical price validation.
- Evidence sources are historical and tied to trigger dates.
- This document is not a live stock recommendation and does not change production scoring.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
