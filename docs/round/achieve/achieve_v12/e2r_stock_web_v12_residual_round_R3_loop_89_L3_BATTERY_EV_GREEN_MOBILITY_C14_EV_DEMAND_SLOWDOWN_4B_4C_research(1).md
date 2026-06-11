# E2R Stock-Web v12 Residual Research — R3 loop 89 / L3 / C14

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 89
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: SEPARATOR_CATHODE_CELL_EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_HARD_4C_VS_CELL_MAKER_FALSE_BREAK
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
  - utilization_calloff_guardrail
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

C14는 “주가가 많이 빠졌다”는 price-only 신호가 아니라, EV 수요 둔화가 실제로 utilization, customer call-off, ASP, inventory, capex delay, margin/FCF break로 이어지는지를 확인하는 bucket이다.

```text
EV demand slowdown / customer call-off headline
  → utilization drop / inventory build / ASP pressure
  → shipment delay / capex deferral / margin break
  → local 4B watch or hard 4C thesis break
  → stock-web 1D OHLC forward path
```

EV 수요 둔화는 공장 컨베이어벨트의 속도가 느려지는 장면이다. 단순 가격 조정은 벨트 위 물건이 잠깐 흔들리는 일이고, hard 4C는 벨트 자체가 멈추며 고객 주문과 가동률이 같이 끊기는 일이다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["361610","393890","066970","373220"],"profile_paths":["atlas/symbol_profiles/361/361610.json","atlas/symbol_profiles/393/393890.json","atlas/symbol_profiles/066/066970.json","atlas/symbol_profiles/373/373220.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv","atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv"],"validation_scope":"2024 trigger-level forward path; 361610/393890/373220 have no corporate-action candidates; 066970 old corporate-action caveats are outside the local 2024 window."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C14 at 21 rows and asks for EV demand slowdown, utilization, call-off, and hard 4C confirmation.
- Existing registry shows C14 parsed through `R3 loop 88`.
- This output uses `R3 loop 89`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file uses separator, cathode, and cell-maker rows to distinguish hard 4C from local 4B/false break.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C14-R3L89-01 | 361610 | SK아이이테크놀로지 | 2024-02-01 | 2024-02-01 | 74800 | 80800 | 29800 | 8.02% | -60.16% | Separator utilization/call-off risk became hard 4C path. |
| C14-R3L89-02 | 393890 | 더블유씨피 | 2024-02-21 | 2024-02-21 | 45750 | 49400 | 16800 | 7.98% | -63.28% | Separator demand slowdown dominated early rebound; hard counterexample. |
| C14-R3L89-03 | 066970 | 엘앤에프 | 2024-03-20 | 2024-03-20 | 178000 | 199000 | 82900 | 11.80% | -53.43% | Cathode rebound failed as demand/call-off risk overwhelmed price. |
| C14-R3L89-04 | 373220 | LG에너지솔루션 | 2024-03-12 | 2024-03-12 | 419500 | 444000 | 311000 | 5.84% | -25.86% | Cell maker drawdown was severe but later rebound argues for 4B watch before hard 4C. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C14-R3L89-01","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_UTILIZATION_CALLOFF_HARD_4C","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"separator_utilization_calloff_hard_4c","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":74800,"peak_price":80800,"peak_date":"2024-02-02","trough_price":29800,"trough_date":"2024-09-11","mfe_pct":8.02,"mae_pct":-60.16,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch","residual_flag":"separator_label_rebound_failed_as_utilization_calloff_risk_dominated","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|361610|separator_utilization_calloff_hard_4c|2024-02-01"}
{"row_type":"trigger","case_id":"C14-R3L89-02","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"SEPARATOR_CUSTOMER_DEMAND_BREAK_HARD_4C","symbol":"393890","name":"더블유씨피","trigger_type":"separator_customer_demand_break_hard_4c","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750,"peak_price":49400,"peak_date":"2024-02-22","trough_price":16800,"trough_date":"2024-09-09","mfe_pct":7.98,"mae_pct":-63.28,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch","residual_flag":"separator_demand_slowdown_path_confirmed_by_low_MFE_high_MAE","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|393890|separator_customer_demand_break_hard_4c|2024-02-21"}
{"row_type":"trigger","case_id":"C14-R3L89-03","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_CUSTOMER_CALLOFF_DEMAND_BREAK","symbol":"066970","name":"엘앤에프","trigger_type":"cathode_customer_calloff_demand_break","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":178000,"peak_price":199000,"peak_date":"2024-03-25","trough_price":82900,"trough_date":"2024-09-10","mfe_pct":11.80,"mae_pct":-53.43,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch_or_4B_to_4C_transition","residual_flag":"cathode_rebound_failed_without_customer_utilization_demand_bridge","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|066970|cathode_customer_calloff_demand_break|2024-03-20"}
{"row_type":"trigger","case_id":"C14-R3L89-04","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CELL_MAKER_EV_SLOWDOWN_FALSE_BREAK_LOCAL_4B","symbol":"373220","name":"LG에너지솔루션","trigger_type":"cell_maker_ev_slowdown_false_break_local_4b","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":419500,"peak_price":444000,"peak_date":"2024-10-08","trough_price":311000,"trough_date":"2024-08-05","mfe_pct":5.84,"mae_pct":-25.86,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_not_automatic_4C","residual_flag":"cell_maker_drawdown_severe_but_later_rebound_requires_non_price_4C_confirmation","dedupe_key":"C14_EV_DEMAND_SLOWDOWN_4B_4C|373220|cell_maker_ev_slowdown_false_break_local_4b|2024-03-12"}
```

## 6. Score-return alignment

### 6.1 Hard 4C separator family

`361610` and `393890` show the cleanest C14 hard-break behavior. Both had small MFE after the entry row and then a large persistent MAE. This is not just price weakness; it is the kind of path that should force the model to ask for utilization, customer call-off, shipment, and inventory confirmation before allowing any Stage2 persistence.

### 6.2 Cathode demand-break path

`066970` shows a cathode version of the same mechanism. The initial rebound was larger than the separator names, but still small relative to the later drawdown. This is where C14 should flip from local 4B watch to hard 4C if customer demand/call-off and margin break are verified.

### 6.3 Cell-maker false-break guard

`373220` shows that not every battery drawdown should be instantly treated as hard 4C. The drawdown was severe, but the later rebound means the scorer should demand exact non-price evidence before labeling the thesis permanently broken. This is a local 4B watch / false-break guardrail row.

## 7. Raw component score simulation

| symbol | EV slowdown evidence | utilization/call-off bridge | margin/FCF break | price confirmation | false-break guard | shadow stage |
|---:|---:|---:|---:|---:|---:|---|
| 361610 | 21 | 20 | 18 | 24 | -2 | Hard 4C watch |
| 393890 | 22 | 20 | 18 | 25 | -2 | Hard 4C watch |
| 066970 | 20 | 17 | 16 | 22 | -4 | 4B→4C transition |
| 373220 | 16 | 10 | 8 | 12 | -8 | Local 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c14_hard_4c_requires_utilization_calloff_margin_break","scope":"C14_EV_DEMAND_SLOWDOWN_4B_4C","candidate_action":"hard_4c_watch","rule":"Do not mark EV/battery drawdown as hard 4C unless utilization drop, customer call-off, shipment delay, ASP pressure, inventory build, margin break, or FCF break is visible.","supporting_cases":["361610","393890","066970"],"counterbalanced_by":["373220"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c14_separator_low_mfe_high_mae_guardrail","scope":"C14_EV_DEMAND_SLOWDOWN_4B_4C","candidate_action":"4b_to_4c_transition_guard","rule":"Separator names with low MFE, persistent high MAE, and no utilization recovery should be escalated from local 4B watch to hard 4C after non-price confirmation.","supporting_cases":["361610","393890"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c14_cell_maker_false_break_guard","scope":"C14_EV_DEMAND_SLOWDOWN_4B_4C","candidate_action":"local_4b_watch_guard","rule":"Cell makers with severe drawdown but later rebound should remain local 4B watch until hard utilization/call-off or margin-break evidence is verified.","supporting_cases":["373220"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","round":"R3","loop":"89","positive_rows":0,"counterexample_rows":4,"new_symbol_count":4,"primary_residual":"C14 needs a sharper distinction between true EV-demand hard 4C in separator/cathode chains and cell-maker local 4B/false-break paths.","candidate_patch_axes":["hard_4c_watch","4b_to_4c_transition_guard","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","sample_count":4,"avg_mfe_pct":8.41,"avg_mae_pct":-50.68,"median_mfe_pct":8.00,"median_mae_pct":-56.80,"interpretation":"C14 rows show low upside and severe downside when EV slowdown converts into utilization/call-off break; cell-maker rebounds require false-break guardrails."}
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
  - no local 2024 corporate-action contamination found for 361610, 393890, 373220; 066970 old caveats are outside local 2024 trigger window
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C14 R3 loop 89 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c14_hard_4c_requires_utilization_calloff_margin_break -> hard_4c_watch
  2. c14_separator_low_mfe_high_mae_guardrail -> 4b_to_4c_transition_guard
  3. c14_cell_maker_false_break_guard -> local_4b_watch_guard

Expected behavior:
- EV slowdown vocabulary alone should not create hard 4C.
- Utilization drop, customer call-off, shipment delay, ASP pressure, inventory build, margin break, or FCF break can justify hard 4C.
- Cell-maker drawdown with later rebound should remain local 4B watch until non-price thesis break is verified.
```
