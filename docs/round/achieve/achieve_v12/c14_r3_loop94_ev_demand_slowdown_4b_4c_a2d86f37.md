# E2R Stock-Web v12 Residual Research — R3 loop 94 / L3 / C14

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 94
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: CATHODE_SEPARATOR_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_CELL_MAKER_FALSE_4C_RECOVERY_4B
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_4C_protection_test
  - stage2_actionable_bonus_stress_test
  - demand_slowdown_utilization_calloff_guardrail
  - hard_4C_thesis_break_timing_test
  - false_4C_recovery_4B_test
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C14_EV_DEMAND_SLOWDOWN_4B_4C` 전용 residual research다.

C14는 “EV 수요 둔화”, “가동률 하락”, “call-off”, “재고 조정”, “판가 하락”이라는 label만으로 모든 배터리 밸류체인을 hard 4C로 처리하는 bucket이 아니다. 핵심은 실제 수요 둔화가 고객 call-off, utilization, inventory, ASP, margin, FCF, guidance break로 이어지는지, 아니면 가격만 먼저 무너졌다가 회복되는 4B/false-4C인지다.

```text
EV demand slowdown / call-off / utilization headline
  → shipment cut / utilization drop / inventory burden
  → ASP pressure / margin and FCF break
  → 4B price-only protection vs hard 4C thesis break
  → stock-web 1D OHLC forward path
```

EV 수요 둔화는 공장 라인 속도가 느려지는 장면과 같다. 벨트가 잠깐 느려졌는지, 아예 전원이 내려갔는지를 구분해야 한다. C14는 “느려짐”과 “논리 전원 차단”을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["247540","003670","393890","066970","373220"],"profile_paths":["atlas/symbol_profiles/247/247540.json","atlas/symbol_profiles/003/003670.json","atlas/symbol_profiles/393/393890.json","atlas/symbol_profiles/066/066970.json","atlas/symbol_profiles/373/373220.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv"],"validation_scope":"2024 trigger-level forward path; 247540 caveats are 2022, 003670 caveats are 2015/2021, 393890 and 373220 have zero corporate-action candidates, 066970 caveats are 2016/2021. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C14 at 21 rows, 9 rows short of the 30-row minimum stability zone.
- Existing registry shows C14 parsed through `R3 loop 93`.
- This output uses `R3 loop 94`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates cathode/material true 4C, separator hard utilization break, cathode ASP/margin break, and cell-maker false-4C recovery/4B protection.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C14-R3L94-01 | 247540 | 에코프로비엠 | 2024-03-25 | 2024-03-25 | 291000 | 296500 | 148700 | 1.89% | -48.90% | Cathode EV-demand slowdown hard 4C: tiny MFE and large MAE. |
| C14-R3L94-02 | 003670 | 포스코퓨처엠 | 2024-03-12 | 2024-03-12 | 336000 | 341000 | 195500 | 1.49% | -41.82% | Major battery material 4C: customer/capacity label failed under demand slowdown. |
| C14-R3L94-03 | 393890 | 더블유씨피 | 2024-02-21 | 2024-02-21 | 45750 | 49400 | 16800 | 7.98% | -63.28% | Separator utilization/call-off hard 4C. |
| C14-R3L94-04 | 066970 | 엘앤에프 | 2024-03-20 | 2024-03-20 | 178000 | 199000 | 82900 | 11.80% | -53.43% | Cathode ASP/margin break: bounce was insufficient versus demand slowdown thesis break. |
| C14-R3L94-05 | 373220 | LG에너지솔루션 | 2024-08-21 | 2024-08-21 | 350000 | 444000 | 332000 | 26.86% | -5.14% | Cell-maker false-4C recovery/4B: price drawdown did not become hard thesis break. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C14-R3L94-01","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_EV_DEMAND_SLOWDOWN_TRUE_4C","symbol":"247540","name":"에코프로비엠","trigger_type":"cathode_ev_demand_slowdown_true_4c","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":291000,"peak_price":296500,"peak_date":"2024-03-25","trough_price":148700,"trough_date":"2024-09-10","mfe_pct":1.89,"mae_pct":-48.90,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch","residual_flag":"cathode_material_tiny_MFE_high_MAE_EV_demand_slowdown_true_4C","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|247540|cathode_ev_demand_slowdown_true_4c|2024-03-25"}
{"row_type":"trigger","case_id":"C14-R3L94-02","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"MAJOR_BATTERY_MATERIAL_CUSTOMER_CAPACITY_DEMAND_BREAK_4C","symbol":"003670","name":"포스코퓨처엠","trigger_type":"major_battery_material_customer_capacity_demand_break_4c","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":336000,"peak_price":341000,"peak_date":"2024-03-13","trough_price":195500,"trough_date":"2024-08-05","mfe_pct":1.49,"mae_pct":-41.82,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_or_4B_to_4C_transition","residual_flag":"major_material_capacity_label_failed_under_EV_demand_slowdown","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|003670|major_battery_material_customer_capacity_demand_break_4c|2024-03-12"}
{"row_type":"trigger","case_id":"C14-R3L94-03","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_UTILIZATION_CALLOFF_HARD_4C","symbol":"393890","name":"더블유씨피","trigger_type":"separator_utilization_calloff_hard_4c","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750,"peak_price":49400,"peak_date":"2024-02-22","trough_price":16800,"trough_date":"2024-09-09","mfe_pct":7.98,"mae_pct":-63.28,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch","residual_flag":"separator_utilization_calloff_break_high_MAE_hard_4C","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|393890|separator_utilization_calloff_hard_4c|2024-02-21"}
{"row_type":"trigger","case_id":"C14-R3L94-04","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_ASP_MARGIN_BREAK_TRUE_4C","symbol":"066970","name":"엘앤에프","trigger_type":"cathode_asp_margin_break_true_4c","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":178000,"peak_price":199000,"peak_date":"2024-03-25","trough_price":82900,"trough_date":"2024-09-10","mfe_pct":11.80,"mae_pct":-53.43,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch","residual_flag":"cathode_ASP_margin_break_high_MAE_true_4C","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|066970|cathode_asp_margin_break_true_4c|2024-03-20"}
{"row_type":"trigger","case_id":"C14-R3L94-05","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CELL_MAKER_FALSE_4C_RECOVERY_4B_PROTECTION","symbol":"373220","name":"LG에너지솔루션","trigger_type":"cell_maker_false_4c_recovery_4b_protection","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000,"peak_price":444000,"peak_date":"2024-10-08","trough_price":332000,"trough_date":"2024-08-21","mfe_pct":26.86,"mae_pct":-5.14,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"4B_price_only_or_Stage3_Yellow_recovery_candidate_pending_utilization_URLs","residual_flag":"cell_maker_price_break_recovered_so_false_4C_unless_non_price_thesis_break_exists","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|373220|cell_maker_false_4c_recovery_4b_protection|2024-08-21"}
```

## 6. Score-return alignment

### 6.1 True 4C material family

`247540`, `003670`, `393890`, and `066970` are the hard warning family. They show tiny or modest MFE, then severe MAE. The common mechanism is that demand slowdown, utilization pressure, call-off, ASP and margin break dominated the forward path. These rows should not be protected as mere 4B price noise unless non-price evidence shows repair.

### 6.2 False-4C / 4B recovery family

`373220` is the counterbalance. It had an EV-demand-slowdown backdrop, but the forward path from the selected entry recovered strongly with limited MAE. C14 should therefore avoid hard 4C promotion when price-only weakness repairs and utilization/AMPC/customer ramp evidence does not show a thesis break.

### 6.3 Mechanism

C14 should work like a circuit breaker, not a permanent kill switch. When demand slowdown is connected to call-off, utilization collapse, inventory burden and margin/FCF break, it should protect as hard 4C. When price breaks but the operating bridge repairs, it should remain 4B or recovery-watch.

## 7. Raw component score simulation

| symbol | demand slowdown evidence | call-off/utilization | ASP/inventory pressure | margin/FCF break | price path | 4B/4C stage |
|---:|---:|---:|---:|---:|---:|---|
| 247540 | 21 | 19 | 18 | 17 | hard negative | Hard 4C |
| 003670 | 20 | 17 | 16 | 15 | hard negative | Hard 4C / 4B→4C |
| 393890 | 22 | 21 | 18 | 17 | hard negative | Hard 4C |
| 066970 | 21 | 18 | 19 | 17 | hard negative | Hard 4C |
| 373220 | 12 | 8 | 7 | 5 | repaired | 4B / false 4C |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c14_demand_slowdown_requires_calloff_utilization_margin_break_for_4C","scope":"C14_EV_DEMAND_SLOWDOWN_4B_4C","candidate_action":"hard_4C_required_bridge","rule":"Do not mark EV-demand slowdown rows as hard 4C unless call-off, shipment cut, utilization drop, inventory burden, ASP pressure, margin break, FCF break, or guidance break is visible.","supporting_cases":["247540","003670","393890","066970"],"counterbalanced_by":["373220"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c14_cathode_separator_true_4C_guard","scope":"C14_EV_DEMAND_SLOWDOWN_4B_4C","candidate_action":"hard_4C_watch","rule":"Cathode/separator rows with tiny MFE and severe MAE after EV demand slowdown vocabulary should be treated as true 4C unless non-price repair appears.","supporting_cases":["247540","003670","393890","066970"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c14_false_4C_cell_maker_recovery_guard","scope":"C14_EV_DEMAND_SLOWDOWN_4B_4C","candidate_action":"4B_price_only_protection","rule":"Cell-maker rows that recover strongly after price weakness should remain 4B or recovery-watch unless utilization, customer ramp, FCF, or guidance evidence confirms thesis break.","supporting_cases":["373220"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c14_material_chain_high_MAE_sizing_block","scope":"C14_EV_DEMAND_SLOWDOWN_4B_4C","candidate_action":"position_sizing_block_or_no_green","rule":"Material-chain rows with MAE below -40% and no non-price repair must be blocked from Green and treated as hard counterexample for promotion logic.","supporting_cases":["247540","003670","393890","066970"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","round":"R3","loop":"94","positive_rows":1,"counterexample_rows":4,"new_symbol_count":5,"primary_residual":"C14 should separate true cathode/separator EV-demand hard 4C from cell-maker price weakness that repairs into 4B/false-4C recovery.","candidate_patch_axes":["hard_4C_required_bridge","hard_4C_watch","4B_price_only_protection","position_sizing_block_or_no_green"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","sample_count":5,"avg_mfe_pct":10.80,"avg_mae_pct":-42.51,"median_mfe_pct":7.98,"median_mae_pct":-48.90,"interpretation":"C14 material-chain rows showed severe high-MAE thesis-break behavior, but cell-maker recovery rows warn against overusing hard 4C when the forward path repairs."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying 4C or 4B promotion logic
  - local 2024 OHLC rows were checked from stock-web tradable shards
  - selected local windows avoid active corporate-action contamination
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C14 R3 loop 94 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c14_demand_slowdown_requires_calloff_utilization_margin_break_for_4C -> hard_4C_required_bridge
  2. c14_cathode_separator_true_4C_guard -> hard_4C_watch
  3. c14_false_4C_cell_maker_recovery_guard -> 4B_price_only_protection
  4. c14_material_chain_high_MAE_sizing_block -> position_sizing_block_or_no_green

Expected behavior:
- EV-demand slowdown vocabulary alone should not automatically hard-4C every battery row.
- Cathode/separator/material rows with call-off, utilization, ASP, margin, FCF or guidance break should become hard 4C.
- Cell-maker rows that recover strongly after price weakness should remain 4B/recovery-watch unless non-price thesis break is verified.
```
