# E2R Stock-Web v12 Residual Research — R3 loop 98 / L3 / C12

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 98
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CELL_MAKER_CUSTOMER_CONTRACT_RECOVERY_VS_CATHODE_SEPARATOR_COPPER_FOIL_CALLOFF_UTILIZATION_MARGIN_BREAK
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - customer_contract_to_shipment_margin_bridge_test
  - calloff_utilization_inventory_guardrail
  - cathode_separator_copper_foil_true_calloff_high_MAE_guard
  - cell_maker_false_calloff_recovery_4B_test
  - AMPC_IRA_separation_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` 전용 residual research다.

C12는 “고객 계약”, “장기공급”, “셀 고객”, “동박/분리막/양극재 공급계약”, “AMPC/IRA 수혜”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 고객 계약이 실제 shipment cadence, call-off risk, utilization, inventory, ASP, working capital, OPM, FCF, guidance/revision으로 내려오는지다.

```text
battery customer contract / long-term supply headline
  → customer call-off / shipment cadence / utilization
  → inventory, ASP, working capital, margin pressure
  → 4B price-only protection vs 4C thesis break
  → stock-web 1D OHLC forward path
```

배터리 고객계약은 공장 라인의 주문 신호와 같다. 신호가 켜졌다고 컨베이어가 계속 도는 것은 아니다. 고객이 물량을 실제로 당기고, call-off가 없고, 재고와 판가가 버티고, 마진이 남을 때만 계약이 이익으로 변한다. C12는 “계약이 있다”와 “고객이 실제로 당긴다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["006400","020150","247540","393890","373220"],"profile_paths":["atlas/symbol_profiles/006/006400.json","atlas/symbol_profiles/020/020150.json","atlas/symbol_profiles/247/247540.json","atlas/symbol_profiles/393/393890.json","atlas/symbol_profiles/373/373220.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv"],"validation_scope":"2024 trigger-level forward path; 006400 caveats are historical and end 2014; 020150/393890/373220 have zero corporate-action candidates; 247540 caveats are 2022. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C12 at 27 rows, 3 rows short of the 30-row minimum stability zone.
- Existing registry shows C12 parsed through `R3 loop 97`.
- This output uses `R3 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C12 loop 96/97 emphasized electrolyte, CNT, copper foil, major chemical, battery cap/case labels. This file compresses cell-maker customer-contract recovery, copper-foil call-off high MAE, cathode true call-off, separator hard call-off, and cell-maker false-calloff 4B recovery.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C12-R3L98-01 | 006400 | 삼성SDI | 2024-01-26 | 2024-01-26 | 360500 | 494500 | 294500 | 37.17% | -18.31% | Cell-maker contract/rebound path worked temporarily, but later utilization/call-off risk required guard. |
| C12-R3L98-02 | 020150 | 롯데에너지머티리얼즈 | 2024-03-21 | 2024-03-21 | 47050 | 52400 | 30500 | 11.37% | -35.18% | Copper-foil customer contract/call-off label created MFE but later high MAE. |
| C12-R3L98-03 | 247540 | 에코프로비엠 | 2024-03-25 | 2024-03-25 | 291000 | 296500 | 148700 | 1.89% | -48.90% | Cathode customer contract/call-off true 4C: tiny MFE and deep MAE. |
| C12-R3L98-04 | 393890 | 더블유씨피 | 2024-02-21 | 2024-02-21 | 45750 | 49400 | 16800 | 7.98% | -63.28% | Separator utilization/call-off hard break; contract label did not protect. |
| C12-R3L98-05 | 373220 | LG에너지솔루션 | 2024-08-21 | 2024-08-21 | 350000 | 444000 | 332000 | 26.86% | -5.14% | Cell-maker false-calloff recovery/4B: price weakness repaired without hard thesis break. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C12-R3L98-01","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CELL_MAKER_CUSTOMER_CONTRACT_REBOUND_WITH_CALLOFF_UTILIZATION_GUARD","symbol":"006400","name":"삼성SDI","trigger_type":"cell_maker_customer_contract_rebound_with_calloff_utilization_guard","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":360500,"peak_price":494500,"peak_date":"2024-03-25","trough_price":294500,"trough_date":"2024-08-05","mfe_pct":37.17,"mae_pct":-18.31,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_utilization_calloff_guard","residual_flag":"cell_maker_rebound_positive_but_later_drawdown_requires_customer_shipment_margin_bridge","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|006400|cell_maker_customer_contract_rebound_with_calloff_utilization_guard|2024-01-26"}
{"row_type":"trigger","case_id":"C12-R3L98-02","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_CUSTOMER_CONTRACT_CALLOFF_HIGH_MAE_GUARD","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"copper_foil_customer_contract_calloff_high_mae_guard","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":47050,"peak_price":52400,"peak_date":"2024-03-27","trough_price":30500,"trough_date":"2024-08-05","mfe_pct":11.37,"mae_pct":-35.18,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"copper_foil_contract_label_failed_without_customer_pull_inventory_margin_bridge","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|020150|copper_foil_customer_contract_calloff_high_mae_guard|2024-03-21"}
{"row_type":"trigger","case_id":"C12-R3L98-03","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CONTRACT_CALLOFF_TRUE_4C","symbol":"247540","name":"에코프로비엠","trigger_type":"cathode_customer_contract_calloff_true_4c","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":291000,"peak_price":296500,"peak_date":"2024-03-25","trough_price":148700,"trough_date":"2024-09-10","mfe_pct":1.89,"mae_pct":-48.90,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch","residual_flag":"cathode_contract_label_tiny_MFE_high_MAE_true_calloff_or_demand_break","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|247540|cathode_customer_contract_calloff_true_4c|2024-03-25"}
{"row_type":"trigger","case_id":"C12-R3L98-04","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SEPARATOR_CUSTOMER_CONTRACT_UTILIZATION_CALLOFF_HARD_BREAK","symbol":"393890","name":"더블유씨피","trigger_type":"separator_customer_contract_utilization_calloff_hard_break","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750,"peak_price":49400,"peak_date":"2024-02-22","trough_price":16800,"trough_date":"2024-09-09","mfe_pct":7.98,"mae_pct":-63.28,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch","residual_flag":"separator_contract_label_failed_under_utilization_calloff_margin_break","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|393890|separator_customer_contract_utilization_calloff_hard_break|2024-02-21"}
{"row_type":"trigger","case_id":"C12-R3L98-05","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CELL_MAKER_FALSE_CALLOFF_RECOVERY_4B_PROTECTION","symbol":"373220","name":"LG에너지솔루션","trigger_type":"cell_maker_false_calloff_recovery_4b_protection","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000,"peak_price":444000,"peak_date":"2024-10-08","trough_price":332000,"trough_date":"2024-08-21","mfe_pct":26.86,"mae_pct":-5.14,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"4B_price_only_or_Stage3-Yellow_recovery_candidate_pending_customer_shipment_URLs","residual_flag":"cell_maker_price_weakness_recovered_so_false_4C_unless_non_price_calloff_thesis_break_exists","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|373220|cell_maker_false_calloff_recovery_4b_protection|2024-08-21"}
```

## 6. Score-return alignment

### 6.1 Customer contract is not the same as shipment pull

`020150`, `247540`, and `393890` are the hard warning family. Each had plausible customer-contract or battery-supply vocabulary, but the forward path showed either tiny MFE or severe MAE. C12 should demand proof of customer pull, shipment cadence, utilization, inventory normalization and margin/FCF conversion before promotion.

### 6.2 Cell makers need a separate 4B/4C decision

`006400` had a tradable rebound from January, but later gave back enough to require sizing and utilization guardrails. `373220` is the counterbalance: price weakness repaired strongly from the August entry, so hard 4C should not be applied by price alone unless non-price call-off evidence confirms a thesis break.

### 6.3 AMPC/IRA separation

C12 should not let AMPC/IRA vocabulary repair a broken customer-contract row automatically. AMPC or policy support belongs in C13 unless it directly improves shipment, utilization, margin, FCF, or working capital for the specific customer-contract thesis.

## 7. Raw component score simulation

| symbol | customer contract evidence | shipment/utilization | call-off/inventory risk | margin/FCF bridge | price confirmation | 4B/4C guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 006400 | 18 | 12 | 9 | 8 | 17 | -8 | 56 | Stage2→Yellow with guard |
| 020150 | 17 | 7 | 4 | 4 | 6 | -16 | 22 | Stage2/local 4B |
| 247540 | 18 | 4 | 2 | 2 | 1 | -22 | 5 | Hard 4C watch |
| 393890 | 17 | 3 | 2 | 2 | 3 | -25 | 2 | Hard 4C watch |
| 373220 | 18 | 12 | 11 | 9 | 15 | -3 | 62 | 4B/recovery-watch or Yellow candidate |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c12_customer_contract_requires_shipment_utilization_margin_bridge","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"stage2_required_bridge","rule":"Do not promote battery customer-contract/long-term-supply labels above Stage2 unless shipment cadence, customer pull, utilization, inventory normalization, ASP, working capital, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["020150","247540","393890"],"counterbalanced_by":["006400","373220"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c12_material_chain_true_calloff_4c_guard","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"hard_4c_watch","rule":"Cathode, separator, or copper-foil rows with tiny/modest MFE and severe MAE after customer-contract vocabulary should be hard 4C or local 4B unless call-off and utilization evidence repairs the row.","supporting_cases":["020150","247540","393890"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c12_cell_maker_false_calloff_recovery_guard","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"4b_price_only_protection_or_recovery_watch","rule":"Cell-maker rows that recover strongly after price weakness should remain 4B/recovery-watch unless non-price customer call-off, utilization or margin-break evidence confirms thesis break.","supporting_cases":["373220"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c12_cell_maker_rebound_sizing_guard","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"stage2_to_yellow_with_utilization_calloff_guard","rule":"Cell-maker customer-contract rebounds can become Yellow when shipment and margin evidence appears, but meaningful later MAE requires staged sizing and call-off checks.","supporting_cases":["006400"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c12_ampc_ira_separation_guard","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"do_not_use_policy_credit_as_contract_repair","rule":"AMPC/IRA language should not repair a C12 customer-contract row unless it directly improves shipment, utilization, working capital, OPM or FCF for the contract thesis; otherwise route it to C13.","supporting_cases":["020150","247540","393890"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","round":"R3","loop":"98","positive_rows":2,"counterexample_rows":3,"new_symbol_count":5,"primary_residual":"C12 should separate cell-maker false-calloff recovery from cathode, separator, and copper-foil customer-contract labels that fail under utilization, call-off, inventory and margin pressure.","candidate_patch_axes":["stage2_required_bridge","hard_4c_watch","4b_price_only_protection_or_recovery_watch","stage2_to_yellow_with_utilization_calloff_guard","do_not_use_policy_credit_as_contract_repair"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","sample_count":5,"avg_mfe_pct":17.85,"avg_mae_pct":-34.16,"median_mfe_pct":11.37,"median_mae_pct":-35.18,"interpretation":"C12 material-chain customer-contract labels showed poor asymmetry when call-off/utilization risk dominated, while cell-maker rows require separate 4B/4C recovery and shipment-margin tests."}
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
- Ingest this C12 R3 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c12_customer_contract_requires_shipment_utilization_margin_bridge -> stage2_required_bridge
  2. c12_material_chain_true_calloff_4c_guard -> hard_4c_watch
  3. c12_cell_maker_false_calloff_recovery_guard -> 4b_price_only_protection_or_recovery_watch
  4. c12_cell_maker_rebound_sizing_guard -> stage2_to_yellow_with_utilization_calloff_guard
  5. c12_ampc_ira_separation_guard -> do_not_use_policy_credit_as_contract_repair

Expected behavior:
- Battery customer-contract vocabulary alone should not create Green.
- Shipment cadence, customer pull, utilization, inventory normalization, ASP, working capital, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Cathode, separator, and copper-foil rows with severe MAE should become hard 4C/local 4B unless non-price evidence repairs the row.
- Cell-maker recovery rows should not be hard-4C by price alone.
```
