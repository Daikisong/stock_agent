# E2R Stock-Web v12 Residual Research — R3 loop 94 / L3 / C11

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 94
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: CELL_AND_EQUIPMENT_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_CATHODE_SEPARATOR_ORDERBOOK_LABEL_HIGH_MAE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - orderbook_to_FCF_margin_bridge_test
  - utilization_calloff_guardrail
  - high_MAE_guardrail
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

C11은 “배터리 수주잔고”, “장기 계약”, “orderbook”, “고객사 CAPA”라는 headline만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 수주잔고가 실제 출하, 가동률, ASP, AMPC/IRA 효과, FCF, margin/revision으로 내려오는지다.

```text
battery orderbook / long-term contract headline
  → customer ramp / shipment schedule / utilization
  → ASP, mix, AMPC or cost absorption
  → margin, FCF, EPS revision bridge
  → stock-web 1D OHLC forward path
```

Orderbook은 식당 예약장과 같다. 예약이 꽉 차 있어도 손님이 오지 않거나 메뉴 단가가 무너지면 매출과 마진은 남지 않는다. C11은 예약장 숫자가 아니라 실제 테이블 회전과 계산서 금액을 본다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["373220","137400","006400","393890","066970"],"profile_paths":["atlas/symbol_profiles/373/373220.json","atlas/symbol_profiles/137/137400.json","atlas/symbol_profiles/006/006400.json","atlas/symbol_profiles/393/393890.json","atlas/symbol_profiles/066/066970.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv"],"validation_scope":"2024 trigger-level forward path; 373220 and 393890 have no corporate-action candidates; 137400/006400/066970 historical caveats are outside the local 2024 trigger windows used here."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C11 at 23 rows and asks whether battery orderbook converts into FCF/margin.
- Existing registry shows C11 parsed through `R3 loop 93`.
- This output uses `R3 loop 94`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates cell maker/plant equipment positive rerating from cathode/separator orderbook label decay.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C11-R3L94-01 | 373220 | LG에너지솔루션 | 2024-08-21 | 2024-08-21 | 350000 | 444000 | 332000 | 26.86% | -5.14% | Cell maker orderbook/AMPC/ramp recovery path; positive but still needs margin/FCF bridge. |
| C11-R3L94-02 | 137400 | 피엔티 | 2024-05-22 | 2024-05-22 | 46850 | 89500 | 44200 | 91.04% | -5.66% | Battery equipment orderbook/customer ramp positive path; strongest bridge candidate in sample. |
| C11-R3L94-03 | 006400 | 삼성SDI | 2024-08-21 | 2024-08-21 | 328500 | 393500 | 235500 | 19.79% | -28.31% | Cell maker rebound had MFE but later decay shows orderbook label needs FCF/margin proof. |
| C11-R3L94-04 | 393890 | 더블유씨피 | 2024-02-21 | 2024-02-21 | 45750 | 49400 | 16800 | 7.98% | -63.28% | Separator orderbook label failed when utilization/call-off risk dominated. |
| C11-R3L94-05 | 066970 | 엘앤에프 | 2024-03-20 | 2024-03-20 | 178000 | 199000 | 82900 | 11.80% | -53.43% | Cathode orderbook/customer contract label failed without margin/FCF conversion. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C11-R3L94-01","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CELL_MAKER_ORDERBOOK_AMPC_RAMP_MARGIN_FCF_BRIDGE","symbol":"373220","name":"LG에너지솔루션","trigger_type":"cell_maker_orderbook_ampc_ramp_margin_fcf_bridge","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000,"peak_price":444000,"peak_date":"2024-10-08","trough_price":332000,"trough_date":"2024-08-21","mfe_pct":26.86,"mae_pct":-5.14,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_FCF_margin_URLs","residual_flag":"positive_cell_maker_rerating_but_requires_margin_FCF_orderbook_bridge","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|373220|cell_maker_orderbook_ampc_ramp_margin_fcf_bridge|2024-08-21"}
{"row_type":"trigger","case_id":"C11-R3L94-02","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_RAMP_STRONG_POSITIVE","symbol":"137400","name":"피엔티","trigger_type":"battery_equipment_orderbook_customer_ramp_strong_positive","trigger_date":"2024-05-22","entry_date":"2024-05-22","entry_price":46850,"peak_price":89500,"peak_date":"2024-06-19","trough_price":44200,"trough_date":"2024-05-22","mfe_pct":91.04,"mae_pct":-5.66,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_order_URLs","residual_flag":"strong_equipment_orderbook_customer_ramp_path_but_needs_cash_margin_URLs","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|137400|battery_equipment_orderbook_customer_ramp_strong_positive|2024-05-22"}
{"row_type":"trigger","case_id":"C11-R3L94-03","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CELL_MAKER_ORDERBOOK_REBOUND_HIGH_MAE_DECAY","symbol":"006400","name":"삼성SDI","trigger_type":"cell_maker_orderbook_rebound_high_mae_decay","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":328500,"peak_price":393500,"peak_date":"2024-09-30","trough_price":235500,"trough_date":"2024-11-15","mfe_pct":19.79,"mae_pct":-28.31,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"cell_maker_orderbook_label_rebounded_then_decayed_without_sustained_FCF_margin_bridge","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|006400|cell_maker_orderbook_rebound_high_mae_decay|2024-08-21"}
{"row_type":"trigger","case_id":"C11-R3L94-04","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SEPARATOR_ORDERBOOK_LABEL_UTILIZATION_CALLOFF_FAILURE","symbol":"393890","name":"더블유씨피","trigger_type":"separator_orderbook_label_utilization_calloff_failure","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750,"peak_price":49400,"peak_date":"2024-02-22","trough_price":16800,"trough_date":"2024-09-09","mfe_pct":7.98,"mae_pct":-63.28,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"separator_orderbook_label_failed_without_utilization_customer_ramp_bridge","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|393890|separator_orderbook_label_utilization_calloff_failure|2024-02-21"}
{"row_type":"trigger","case_id":"C11-R3L94-05","round":"R3","loop":"94","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_CONTRACT_MARGIN_FAILURE","symbol":"066970","name":"엘앤에프","trigger_type":"cathode_orderbook_customer_contract_margin_failure","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":178000,"peak_price":199000,"peak_date":"2024-03-25","trough_price":82900,"trough_date":"2024-09-10","mfe_pct":11.80,"mae_pct":-53.43,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4B_to_4C_watch","residual_flag":"cathode_orderbook_label_failed_without_margin_FCF_conversion","dedupe_key":"C11_BATTERY_ORDERBOOK_RERATING|066970|cathode_orderbook_customer_contract_margin_failure|2024-03-20"}
```

## 6. Score-return alignment

### 6.1 Positive orderbook-to-ramp family

`373220` and `137400` show the constructive C11 family. The cell maker row has a clean recovery path when the market re-prices orderbook, AMPC, and utilization recovery. The equipment row is stronger: PNT-like battery equipment orderbook and customer ramp can create large MFE with contained MAE.

### 6.2 Same orderbook label, weak conversion

`006400` is not a pure failure, but it is not Green either. It had MFE after the entry row, then deteriorated into a deep drawdown. This is exactly why C11 needs a margin/FCF bridge, not just a “battery orderbook” label.

### 6.3 Separator/cathode hard counterexamples

`393890` and `066970` are the hard warning family. Separator and cathode orderbook labels looked investable on headline vocabulary, but utilization, demand, call-off, ASP, and margin pressure dominated the forward path. C11 should treat these as hard counterexamples unless non-price evidence proves the orderbook can convert into cash.

## 7. Raw component score simulation

| symbol | orderbook evidence | customer ramp/utilization | margin/FCF bridge | price confirmation | MAE/logic guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 373220 | 21 | 18 | 13 | 18 | -3 | 67 | Stage3-Yellow candidate |
| 137400 | 22 | 21 | 16 | 25 | -3 | 81 | Stage3-Yellow/Green candidate |
| 006400 | 17 | 12 | 7 | 12 | -12 | 36 | Stage2/Yellow with high-MAE guardrail |
| 393890 | 14 | 4 | 2 | 3 | -22 | 1 | Hard counterexample / 4C watch |
| 066970 | 15 | 5 | 3 | 5 | -20 | 8 | Hard counterexample / 4B→4C watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c11_orderbook_requires_customer_ramp_margin_fcf_bridge","scope":"C11_BATTERY_ORDERBOOK_RERATING","candidate_action":"stage2_required_bridge","rule":"Do not promote battery orderbook/long-term contract labels above Stage2 unless customer ramp, shipment schedule, utilization, ASP, margin, FCF, AMPC/cost absorption, or EPS revision bridge is visible.","supporting_cases":["006400","393890","066970"],"counterbalanced_by":["373220","137400"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c11_equipment_orderbook_positive_delta","scope":"C11_BATTERY_ORDERBOOK_RERATING","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Battery equipment names with verified orderbook, customer ramp, delivery schedule, and margin/cash bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["137400"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c11_cell_maker_orderbook_yellow_delta","scope":"C11_BATTERY_ORDERBOOK_RERATING","candidate_action":"stage3_yellow_candidate_delta","rule":"Cell makers with orderbook plus utilization/AMPC recovery can be Stage3-Yellow candidates, but Green needs FCF and margin conversion proof.","supporting_cases":["373220","006400"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c11_separator_cathode_orderbook_false_stage2_guard","scope":"C11_BATTERY_ORDERBOOK_RERATING","candidate_action":"hard_4c_watch","rule":"Separator/cathode orderbook labels with low MFE and severe MAE should become hard counterexamples when utilization/call-off/margin break is not repaired.","supporting_cases":["393890","066970"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","round":"R3","loop":"94","positive_rows":2,"counterexample_rows":3,"new_symbol_count":5,"primary_residual":"C11 needs sharper separation between orderbook label strength and actual customer ramp, utilization, margin, FCF conversion; equipment orderbook can work while separator/cathode labels can hard-fail.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage3_yellow_candidate_delta","hard_4c_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","sample_count":5,"avg_mfe_pct":31.49,"avg_mae_pct":-31.16,"median_mfe_pct":19.79,"median_mae_pct":-28.31,"interpretation":"C11 has large upside when orderbook converts into customer ramp and cash/margin, but the same vocabulary creates severe downside in separator/cathode chains when utilization and call-off risk dominate."}
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
  - historical corporate-action caveats, where present, are outside local 2024 trigger windows
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C11 R3 loop 94 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c11_orderbook_requires_customer_ramp_margin_fcf_bridge -> stage2_required_bridge
  2. c11_equipment_orderbook_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c11_cell_maker_orderbook_yellow_delta -> stage3_yellow_candidate_delta
  4. c11_separator_cathode_orderbook_false_stage2_guard -> hard_4c_watch

Expected behavior:
- Battery orderbook vocabulary alone should not create Green.
- Customer ramp, shipment schedule, utilization, ASP, AMPC/cost absorption, margin, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Separator/cathode orderbook rows with low MFE and severe MAE should become hard counterexamples unless utilization/cash conversion recovers.
```
