# E2R Stock-Web v12 Residual Research — R3 loop 100 / L3 / C11

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 100
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_CELL_SEPARATOR_CATHODE_ORDERBOOK_DELIVERY_MARGIN_FCF_BRIDGE_VS_ORDERBOOK_LABEL_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - orderbook_to_delivery_acceptance_margin_bridge_test
  - equipment_orderbook_positive_with_drawdown_guard
  - separator_cathode_orderbook_false_stage2_guard
  - cell_orderbook_recovery_counterbalance
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C11_BATTERY_ORDERBOOK_RERATING` 전용 residual research다.

C11은 “수주잔고”, “orderbook”, “장기공급”, “배터리 장비 납품”, “셀/소재 capacity”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 orderbook이 실제 납품 스케줄, 고객 검수, 매출 인식, 운전자본, OPM, FCF, EPS revision으로 내려오는지다.

```text
battery orderbook / long-term supply headline
  → delivery schedule / customer acceptance / shipment cadence
  → revenue recognition / working capital / receivables
  → margin / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

수주잔고는 공장 벽에 붙은 주문서와 같다. 주문서가 두꺼워도 컨베이어가 돌고, 고객 검수가 끝나고, 대금이 들어와야 이익이 된다. C11은 “주문서의 두께”와 “현금으로 남는 납품”을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["137400","393890","066970","003670","373220"],"profile_paths":["atlas/symbol_profiles/137/137400.json","atlas/symbol_profiles/393/393890.json","atlas/symbol_profiles/066/066970.json","atlas/symbol_profiles/003/003670.json","atlas/symbol_profiles/373/373220.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv"],"validation_scope":"2024 trigger-level forward path; 137400 caveats are 2012/2019, 393890 and 373220 have zero corporate-action candidates, 066970 caveats are 2016/2021, and 003670 caveats are 2015/2021. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C11 at 23 rows, 7 rows short of the 30-row minimum stability zone.
- Existing registry shows C11 parsed through `R3 loop 99`.
- This output uses `R3 loop 100`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C11 loop 99 emphasized battery equipment automation / thermal processing / demagnetization orderbook. This file shifts to roll-to-roll equipment, separator/cathode/material orderbook false Stage2, and cell orderbook recovery counterbalance.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C11-R3L100-01 | 137400 | 피엔티 | 2024-03-05 | 2024-03-05 | 44050 | 64100 | 36300 | 45.52% | -17.59% | Roll-to-roll battery equipment orderbook worked, but drawdown requires delivery/acceptance/FCF guard. |
| C11-R3L100-02 | 393890 | 더블유씨피 | 2024-02-21 | 2024-02-21 | 45750 | 49400 | 16800 | 7.98% | -63.28% | Separator orderbook/capacity label failed badly without utilization and margin conversion. |
| C11-R3L100-03 | 066970 | 엘앤에프 | 2024-03-20 | 2024-03-20 | 178000 | 199000 | 82900 | 11.80% | -53.43% | Cathode long-term orderbook label failed under ASP/margin/FCF pressure. |
| C11-R3L100-04 | 003670 | 포스코퓨처엠 | 2024-03-12 | 2024-03-12 | 336000 | 341000 | 195500 | 1.49% | -41.82% | Major cathode/material orderbook label produced tiny MFE and deep MAE. |
| C11-R3L100-05 | 373220 | LG에너지솔루션 | 2024-08-21 | 2024-08-21 | 350000 | 444000 | 332000 | 26.86% | -5.14% | Cell orderbook/recovery path repaired; counterbalance against over-hard 4C treatment. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C11-R3L100-01","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ROLL_TO_ROLL_BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE","symbol":"137400","name":"피엔티","trigger_type":"roll_to_roll_battery_equipment_orderbook_delivery_acceptance_margin_bridge","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":44050,"peak_price":64100,"peak_date":"2024-10-10","trough_price":36300,"trough_date":"2024-04-08","mfe_pct":45.52,"mae_pct":-17.59,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_drawdown_guard","residual_flag":"battery_equipment_orderbook_positive_but_delivery_acceptance_OPM_FCF_URLs_required","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|137400|roll_to_roll_battery_equipment_orderbook_delivery_acceptance_margin_bridge|2024-03-05"}
{"row_type":"trigger","case_id":"C11-R3L100-02","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SEPARATOR_ORDERBOOK_CAPACITY_LABEL_FALSE_STAGE2_HIGH_MAE","symbol":"393890","name":"더블유씨피","trigger_type":"separator_orderbook_capacity_label_false_stage2_high_mae","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750,"peak_price":49400,"peak_date":"2024-02-22","trough_price":16800,"trough_date":"2024-09-09","mfe_pct":7.98,"mae_pct":-63.28,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"separator_orderbook_label_failed_without_utilization_delivery_margin_bridge","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|393890|separator_orderbook_capacity_label_false_stage2_high_mae|2024-02-21"}
{"row_type":"trigger","case_id":"C11-R3L100-03","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_LONG_TERM_ORDERBOOK_ASP_MARGIN_FCF_BREAK","symbol":"066970","name":"엘앤에프","trigger_type":"cathode_long_term_orderbook_asp_margin_fcf_break","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":178000,"peak_price":199000,"peak_date":"2024-03-25","trough_price":82900,"trough_date":"2024-09-10","mfe_pct":11.80,"mae_pct":-53.43,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_or_false_Stage2","residual_flag":"cathode_orderbook_label_failed_under_ASP_margin_FCF_pressure","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|066970|cathode_long_term_orderbook_asp_margin_fcf_break|2024-03-20"}
{"row_type":"trigger","case_id":"C11-R3L100-04","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"MAJOR_CATHODE_MATERIAL_ORDERBOOK_TINY_MFE_HIGH_MAE","symbol":"003670","name":"포스코퓨처엠","trigger_type":"major_cathode_material_orderbook_tiny_mfe_high_mae","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":336000,"peak_price":341000,"peak_date":"2024-03-13","trough_price":195500,"trough_date":"2024-08-05","mfe_pct":1.49,"mae_pct":-41.82,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4B_to_4C","residual_flag":"major_material_orderbook_label_tiny_MFE_high_MAE_without_margin_FCF_bridge","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|003670|major_cathode_material_orderbook_tiny_mfe_high_mae|2024-03-12"}
{"row_type":"trigger","case_id":"C11-R3L100-05","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CELL_ORDERBOOK_RECOVERY_FALSE_4C_COUNTERBALANCE","symbol":"373220","name":"LG에너지솔루션","trigger_type":"cell_orderbook_recovery_false_4c_counterbalance","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000,"peak_price":444000,"peak_date":"2024-10-08","trough_price":332000,"trough_date":"2024-08-21","mfe_pct":26.86,"mae_pct":-5.14,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_recovery_candidate_pending_order_margin_URLs","residual_flag":"cell_orderbook_recovery_repaired_price_path_but_exact_delivery_FCF_URLs_required","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|373220|cell_orderbook_recovery_false_4c_counterbalance|2024-08-21"}
```

## 6. Score-return alignment

### 6.1 Equipment orderbook can work, but delivery bridge is required

`137400` is the constructive equipment-orderbook row. The price path eventually produced strong MFE, but the early drawdown was meaningful. This argues for staged treatment: battery equipment orderbook can become Yellow/Stage3 only when delivery acceptance, revenue recognition, OPM and FCF bridge are visible.

### 6.2 Material orderbook labels can be severe false Stage2

`393890`, `066970`, and `003670` are the false-stage family. Each had plausible orderbook/capacity vocabulary, yet the forward path showed deep MAE. C11 should not promote separator or cathode orderbook labels when utilization, ASP, margin and FCF are breaking.

### 6.3 Cell orderbook recovery counterbalance

`373220` is the counterbalance. The row repaired strongly after price weakness and shows why C11 should avoid turning all battery orderbook weakness into hard 4C. If the forward path repairs and non-price order/margin evidence is not broken, it can stay recovery-watch or Stage3-Yellow candidate.

## 7. Raw component score simulation

| symbol | orderbook evidence | delivery / acceptance | utilization / shipment | margin / FCF bridge | price confirmation | MAE / 4C guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 137400 | 20 | 13 | 12 | 10 | 18 | -8 | 65 | Stage2→Yellow / Stage3 candidate with guard |
| 393890 | 17 | 4 | 3 | 2 | 3 | -25 | 4 | Hard counterexample / 4C |
| 066970 | 18 | 5 | 4 | 2 | 5 | -22 | 12 | Hard 4C / false Stage2 |
| 003670 | 18 | 4 | 3 | 2 | 1 | -18 | 10 | Hard counterexample / 4B→4C |
| 373220 | 18 | 12 | 13 | 10 | 15 | -3 | 65 | Stage3-Yellow recovery candidate |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c11_orderbook_requires_delivery_acceptance_margin_FCF_bridge","scope":"C11_BATTERY_ORDERBOOK_RERATING","candidate_action":"stage2_required_bridge","rule":"Do not promote battery orderbook/long-term-supply labels above Stage2 unless delivery schedule, customer acceptance, shipment cadence, revenue recognition, working capital, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["393890","066970","003670"],"counterbalanced_by":["137400","373220"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c11_equipment_orderbook_positive_but_drawdown_guard","scope":"C11_BATTERY_ORDERBOOK_RERATING","candidate_action":"stage2_to_yellow_with_drawdown_guard","rule":"Battery equipment orderbook rows can receive Yellow/Stage3 treatment when delivery acceptance and margin evidence appears, but meaningful MAE requires staged sizing and URL-verified bridge.","supporting_cases":["137400"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c11_separator_cathode_orderbook_false_stage2_guard","scope":"C11_BATTERY_ORDERBOOK_RERATING","candidate_action":"hard_4c_watch_or_4b_to_4c","rule":"Separator/cathode/material orderbook labels with tiny MFE and severe MAE should be hard counterexamples unless utilization, ASP, margin and FCF evidence repairs the thesis.","supporting_cases":["393890","066970","003670"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c11_cell_orderbook_recovery_counterbalance","scope":"C11_BATTERY_ORDERBOOK_RERATING","candidate_action":"recovery_watch_or_stage3_yellow_candidate","rule":"Cell orderbook rows that recover strongly after price weakness should not be hard-4C by price alone; require non-price thesis break before downgrade.","supporting_cases":["373220"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","round":"R3","loop":"100","positive_rows":2,"counterexample_rows":3,"new_symbol_count":5,"primary_residual":"C11 should separate equipment/cell orderbook paths that can repair through delivery and margin from separator/cathode orderbook labels that fail under utilization, ASP, and FCF pressure.","candidate_patch_axes":["stage2_required_bridge","stage2_to_yellow_with_drawdown_guard","hard_4c_watch_or_4b_to_4c","recovery_watch_or_stage3_yellow_candidate"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","sample_count":5,"avg_mfe_pct":18.73,"avg_mae_pct":-36.25,"median_mfe_pct":11.80,"median_mae_pct":-41.82,"interpretation":"C11 orderbook vocabulary has poor asymmetry unless delivery acceptance, utilization, margin and FCF bridge is visible; equipment and cell recovery can work, but separator/cathode labels often decay into high-MAE false Stage2."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - local 2024 OHLC rows were checked from stock-web tradable shards
  - selected local windows avoid active corporate-action contamination
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C11 R3 loop 100 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c11_orderbook_requires_delivery_acceptance_margin_FCF_bridge -> stage2_required_bridge
  2. c11_equipment_orderbook_positive_but_drawdown_guard -> stage2_to_yellow_with_drawdown_guard
  3. c11_separator_cathode_orderbook_false_stage2_guard -> hard_4c_watch_or_4b_to_4c
  4. c11_cell_orderbook_recovery_counterbalance -> recovery_watch_or_stage3_yellow_candidate

Expected behavior:
- Battery orderbook / long-term supply vocabulary alone should not create Green.
- Delivery schedule, customer acceptance, shipment cadence, revenue recognition, working capital, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Separator/cathode orderbook rows with severe MAE should be hard counterexamples unless utilization/margin evidence repairs the row.
```
