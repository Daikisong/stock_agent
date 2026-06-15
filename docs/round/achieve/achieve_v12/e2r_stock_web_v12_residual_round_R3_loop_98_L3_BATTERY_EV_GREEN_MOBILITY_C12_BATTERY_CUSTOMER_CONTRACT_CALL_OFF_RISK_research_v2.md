# E2R Stock-Web v12 Residual Research — R3 loop 98 / L3 / C12

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 98
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CATHODE_CELL_COPPER_FOIL_CUSTOMER_CONTRACT_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_HIGH_MAE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - customer_contract_calloff_guardrail
  - demand_ramp_vs_AMPC_IRA_separation
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

이번 파일은 `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` 전용 residual research다.

C12는 “고객 계약”, “장기 공급”, “cell maker와 협력”, “배터리 소재 수주”라는 headline만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 계약된 물량이 실제 call-off 없이 출하되고, 고객 ramp와 utilization이 살아 있으며, ASP와 margin/FCF로 내려오는지다.

```text
battery customer contract / long-term supply label
  → customer call-off or shipment schedule
  → utilization / inventory / ASP and delivery cadence
  → margin / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

배터리 고객 계약은 항구의 선적 예약표와 같다. 예약표에는 배가 떠난다고 적혀 있어도, 고객이 물량을 미루면 컨테이너는 항구에 남고 재고·가동률·마진이 함께 무거워진다. C12는 “예약표”와 “실제 출항”을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["247540","003670","096770","336370"],"profile_paths":["atlas/symbol_profiles/247/247540.json","atlas/symbol_profiles/003/003670.json","atlas/symbol_profiles/096/096770.json","atlas/symbol_profiles/336/336370.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv"],"validation_scope":"2024 trigger-level forward path; 247540 corporate-action caveats are in 2022, 003670 caveats are in 2015/2021, 096770 caveat is 2024-11-20 and selected path ends before the caveat window, 336370 caveats are January 2024 so selected trigger starts after the caveat windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C12 at 27 rows, 3 rows short of the 30-row minimum stability zone.
- Existing registry shows C12 parsed through `R3 loop 97`.
- This output uses `R3 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates cathode major names, cell/customer AMPC separation, and copper-foil contract call-off risk.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C12-R3L98-01 | 247540 | 에코프로비엠 | 2024-03-25 | 2024-03-25 | 291000 | 296500 | 148700 | 1.89% | -48.90% | Cathode customer-contract label failed when demand/call-off risk dominated. |
| C12-R3L98-02 | 003670 | 포스코퓨처엠 | 2024-03-12 | 2024-03-12 | 336000 | 341000 | 195500 | 1.49% | -41.82% | Major cathode/anode material contract label produced almost no MFE and deep MAE. |
| C12-R3L98-03 | 096770 | SK이노베이션 | 2024-04-02 | 2024-04-02 | 121800 | 125000 | 91700 | 2.63% | -24.71% | Cell/customer contract label had limited MFE before utilization/AMPC/call-off concerns dominated. |
| C12-R3L98-04 | 336370 | 솔루스첨단소재 | 2024-03-27 | 2024-03-27 | 16970 | 21700 | 11200 | 27.87% | -34.00% | Copper-foil customer contract optionality made MFE, but high MAE shows call-off and margin risk. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C12-R3L98-01","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CONTRACT_CALLOFF_DEMAND_BREAK_HIGH_MAE","symbol":"247540","name":"에코프로비엠","trigger_type":"cathode_customer_contract_calloff_demand_break_high_mae","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":291000,"peak_price":296500,"peak_date":"2024-03-25","trough_price":148700,"trough_date":"2024-09-10","mfe_pct":1.89,"mae_pct":-48.90,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4C_watch_or_local_4B_to_4C_transition","residual_flag":"customer_contract_label_failed_without_shipment_utilization_margin_bridge","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|247540|cathode_customer_contract_calloff_demand_break_high_mae|2024-03-25"}
{"row_type":"trigger","case_id":"C12-R3L98-02","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"MAJOR_CATHODE_ANODE_MATERIAL_CUSTOMER_CONTRACT_FALSE_STAGE2","symbol":"003670","name":"포스코퓨처엠","trigger_type":"major_cathode_anode_material_customer_contract_false_stage2","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":336000,"peak_price":341000,"peak_date":"2024-03-13","trough_price":195500,"trough_date":"2024-08-05","mfe_pct":1.49,"mae_pct":-41.82,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"major_customer_contract_label_decayed_without_calloff_delivery_margin_bridge","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|003670|major_cathode_anode_material_customer_contract_false_stage2|2024-03-12"}
{"row_type":"trigger","case_id":"C12-R3L98-03","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CELL_CUSTOMER_CONTRACT_AMPC_IRA_SEPARATION_CALLOFF_RISK","symbol":"096770","name":"SK이노베이션","trigger_type":"cell_customer_contract_ampc_ira_separation_calloff_risk","trigger_date":"2024-04-02","entry_date":"2024-04-02","entry_price":121800,"peak_price":125000,"peak_date":"2024-10-10","trough_price":91700,"trough_date":"2024-08-05","mfe_pct":2.63,"mae_pct":-24.71,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"AMPC_IRA_or_customer_contract_vocabulary_cannot_replace_real_utilization_delivery_margin_bridge","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|096770|cell_customer_contract_ampc_ira_separation_calloff_risk|2024-04-02"}
{"row_type":"trigger","case_id":"C12-R3L98-04","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_CUSTOMER_CONTRACT_OPTIONALITY_HIGH_MAE_GUARD","symbol":"336370","name":"솔루스첨단소재","trigger_type":"copper_foil_customer_contract_optionality_high_mae_guard","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":16970,"peak_price":21700,"peak_date":"2024-04-12","trough_price":11200,"trough_date":"2024-09-10","mfe_pct":27.87,"mae_pct":-34.00,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"copper_foil_contract_optionality_needs_calloff_delivery_margin_proof_before_promotion","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|336370|copper_foil_customer_contract_optionality_high_mae_guard|2024-03-27"}
```

## 6. Score-return alignment

### 6.1 Cathode contract labels as false Stage2

`247540` and `003670` are strong C12 counterexamples. Both had customer-contract or long-term supply vocabulary that might look investable, yet the forward path produced tiny MFE and large MAE. That is the core C12 failure mode: a contract headline cannot be scored as durable if customer call-off, shipment cadence, utilization, ASP, and margin bridge are not visible.

### 6.2 AMPC/IRA separation

`096770` shows why C12 must stay separate from C13. AMPC/IRA or cell-maker policy support can matter, but C12 is about whether customer contracts actually ship. The price path had only limited MFE and meaningful drawdown before later recovery, so the row should remain local 4B/Stage2 unless utilization and margin conversion are verified.

### 6.3 Copper-foil optionality with high MAE

`336370` shows the optionality family. A customer-contract/copper-foil narrative can create meaningful MFE, but the later drawdown is too deep for automatic promotion. This is a Yellow candidate only if exact delivery, call-off, and margin evidence exists.

## 7. Raw component score simulation

| symbol | customer contract evidence | shipment/call-off bridge | utilization/ASP bridge | margin/FCF bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 247540 | 18 | 4 | 4 | 2 | 1 | -21 | 8 | Hard 4C watch |
| 003670 | 18 | 5 | 4 | 3 | 1 | -19 | 12 | Hard counterexample |
| 096770 | 15 | 8 | 7 | 5 | 3 | -11 | 27 | Stage2/local 4B watch |
| 336370 | 17 | 10 | 8 | 6 | 15 | -15 | 41 | Yellow with high-MAE guard |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c12_customer_contract_requires_calloff_delivery_margin_bridge","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"stage2_required_bridge","rule":"Do not promote battery customer contract/long-term supply labels above Stage2 unless call-off, delivery schedule, shipment cadence, utilization, ASP, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["247540","003670","096770"],"counterbalanced_by":["336370"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c12_cathode_contract_false_stage2_guard","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"hard_4c_watch","rule":"Cathode/material names with tiny MFE and deep MAE after contract vocabulary should be marked hard counterexample or 4B-to-4C transition until customer shipment evidence repairs the thesis.","supporting_cases":["247540","003670"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c12_ampc_ira_separation_guard","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"canonical_boundary_guard","rule":"AMPC/IRA or policy subsidy vocabulary must not substitute for customer call-off and delivery evidence in C12; route subsidy-specific evidence to C13 unless customer shipping economics are visible.","supporting_cases":["096770"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c12_copper_foil_yellow_optional_delta","scope":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","candidate_action":"stage2_to_yellow_with_high_MAE_guardrail","rule":"Copper-foil contract optionality can be Yellow only when call-off, delivery, and margin conversion are verified; high MAE blocks Green.","supporting_cases":["336370"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","round":"R3","loop":"98","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C12 should separate customer-contract vocabulary from actual call-off, delivery schedule, shipment cadence, utilization, ASP and margin conversion; cathode/material labels can be severe false Stage2 paths.","candidate_patch_axes":["stage2_required_bridge","hard_4c_watch","canonical_boundary_guard","stage2_to_yellow_with_high_MAE_guardrail"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","sample_count":4,"avg_mfe_pct":8.47,"avg_mae_pct":-37.36,"median_mfe_pct":2.26,"median_mae_pct":-37.91,"interpretation":"C12 rows show poor asymmetry when customer contract labels are not tied to call-off, shipment and margin evidence; optionality can rally but needs strict MAE guardrails."}
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
  1. c12_customer_contract_requires_calloff_delivery_margin_bridge -> stage2_required_bridge
  2. c12_cathode_contract_false_stage2_guard -> hard_4c_watch
  3. c12_ampc_ira_separation_guard -> canonical_boundary_guard
  4. c12_copper_foil_yellow_optional_delta -> stage2_to_yellow_with_high_MAE_guardrail

Expected behavior:
- Battery customer contract vocabulary alone should not create Green.
- Customer call-off, shipment cadence, utilization, ASP, margin, FCF or EPS revision can justify Yellow/Stage3 only after verification.
- AMPC/IRA evidence should not substitute for C12 customer shipping evidence.
```
