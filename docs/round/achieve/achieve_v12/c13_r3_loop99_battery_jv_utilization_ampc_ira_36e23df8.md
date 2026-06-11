# E2R Stock-Web v12 Residual Research — R3 loop 99 / L3 / C13

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 99
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: CELL_MAKER_JV_UTILIZATION_AMPC_CASH_CONVERSION_RECOVERY_VS_MATERIAL_CHAIN_IRA_LABEL_HIGH_MAE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - JV_utilization_to_AMPC_cash_conversion_bridge_test
  - AMPC_IRA_non_price_bridge_guardrail
  - cell_maker_recovery_counterbalance
  - material_chain_IRA_label_false_stage2_guard
  - C12_customer_contract_separation
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` 전용 residual research다.

C13은 “AMPC”, “IRA”, “북미 JV”, “세액공제”, “현지화 수혜”, “배터리 정책 수혜”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 JV 가동률이 실제 qualified output, AMPC recognition, cash collection, utilization, fixed-cost absorption, working capital, OPM, FCF, EPS revision으로 내려오는지다.

```text
battery JV / AMPC / IRA headline
  → qualified production and JV utilization
  → AMPC recognition / cash conversion / fixed-cost absorption
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

AMPC는 공장 벽에 붙은 세액공제 쿠폰과 같다. 쿠폰이 있어도 라인이 돌고, 적격 물량이 나오고, 비용을 흡수하고, 현금으로 돌아와야 이익이 된다. C13은 “정책 쿠폰이 있다”와 “JV가 돈을 만든다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["373220","006400","096770","020150","393890"],"profile_paths":["atlas/symbol_profiles/373/373220.json","atlas/symbol_profiles/006/006400.json","atlas/symbol_profiles/096/096770.json","atlas/symbol_profiles/020/020150.json","atlas/symbol_profiles/393/393890.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv"],"validation_scope":"2024 trigger-level forward path; 373220/020150/393890 have zero corporate-action candidates; 006400 historical caveats end 2014; 096770 profile fetched from stock-web and selected 2024 rows avoid active local corporate-action windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C13 at 27 rows, 3 rows short of the 30-row minimum stability zone.
- Existing registry shows C13 parsed through `R3 loop 98`.
- This output uses `R3 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C13 loop 98 emphasized separator/silicon-anode/electrolyte materials and IRA/material label spike. This file shifts the residual focus to cell-maker/JV recovery, SK On parent-structure recovery, AMPC cash conversion, and material-chain IRA label false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C13-R3L99-01 | 373220 | LG에너지솔루션 | 2024-08-21 | 2024-08-21 | 350000 | 444000 | 332000 | 26.86% | -5.14% | Cell-maker JV/AMPC recovery path repaired; false-4C counterbalance. |
| C13-R3L99-02 | 006400 | 삼성SDI | 2024-01-26 | 2024-01-26 | 360500 | 494500 | 294500 | 37.17% | -18.31% | Cell-maker/JV utilization rebound worked, but later drawdown demands utilization and FCF guard. |
| C13-R3L99-03 | 096770 | SK이노베이션 | 2024-08-05 | 2024-08-05 | 92800 | 125000 | 91700 | 34.70% | -1.19% | SK On parent/JV AMPC restructuring recovery path worked from depressed entry. |
| C13-R3L99-04 | 020150 | 롯데에너지머티리얼즈 | 2024-03-21 | 2024-03-21 | 47050 | 52400 | 30500 | 11.37% | -35.18% | Copper-foil IRA/customer localization label failed without utilization and margin conversion. |
| C13-R3L99-05 | 393890 | 더블유씨피 | 2024-02-21 | 2024-02-21 | 45750 | 49400 | 16800 | 7.98% | -63.28% | Separator utilization/IRA label did not protect; hard material-chain false Stage2. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C13-R3L99-01","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CELL_MAKER_JV_AMPC_UTILIZATION_RECOVERY_CASH_CONVERSION","symbol":"373220","name":"LG에너지솔루션","trigger_type":"cell_maker_jv_ampc_utilization_recovery_cash_conversion","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000,"peak_price":444000,"peak_date":"2024-10-08","trough_price":332000,"trough_date":"2024-08-21","mfe_pct":26.86,"mae_pct":-5.14,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_recovery_candidate_pending_AMPC_utilization_FCF_URLs","residual_flag":"cell_maker_JV_AMPC_recovery_path_repaired_but_exact_utilization_cash_URLs_required","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|cell_maker_jv_ampc_utilization_recovery_cash_conversion|2024-08-21"}
{"row_type":"trigger","case_id":"C13-R3L99-02","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CELL_MAKER_JV_UTILIZATION_REBOUND_WITH_FCF_GUARD","symbol":"006400","name":"삼성SDI","trigger_type":"cell_maker_jv_utilization_rebound_with_fcf_guard","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":360500,"peak_price":494500,"peak_date":"2024-03-25","trough_price":294500,"trough_date":"2024-08-05","mfe_pct":37.17,"mae_pct":-18.31,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_utilization_FCF_guard","residual_flag":"cell_maker_rebound_positive_but_full_window_drawdown_requires_JV_utilization_margin_FCF_bridge","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|cell_maker_jv_utilization_rebound_with_fcf_guard|2024-01-26"}
{"row_type":"trigger","case_id":"C13-R3L99-03","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SKON_PARENT_JV_AMPC_RESTRUCTURING_RECOVERY_WITH_CASH_GUARD","symbol":"096770","name":"SK이노베이션","trigger_type":"skon_parent_jv_ampc_restructuring_recovery_with_cash_guard","trigger_date":"2024-08-05","entry_date":"2024-08-05","entry_price":92800,"peak_price":125000,"peak_date":"2024-10-10","trough_price":91700,"trough_date":"2024-08-05","mfe_pct":34.70,"mae_pct":-1.19,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_recovery_candidate_pending_parent_BS_AMPC_cash_URLs","residual_flag":"battery_parent_JV_AMPC_recovery_worked_from_depressed_entry_but_parent_balance_sheet_and_cash_conversion_URLs_required","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|096770|skon_parent_jv_ampc_restructuring_recovery_with_cash_guard|2024-08-05"}
{"row_type":"trigger","case_id":"C13-R3L99-04","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_IRA_LOCALIZATION_UTILIZATION_FALSE_STAGE2_HIGH_MAE","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"copper_foil_ira_localization_utilization_false_stage2_high_mae","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":47050,"peak_price":52400,"peak_date":"2024-03-27","trough_price":30500,"trough_date":"2024-08-05","mfe_pct":11.37,"mae_pct":-35.18,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"copper_foil_IRA_localization_label_failed_without_utilization_margin_FCF_bridge","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|020150|copper_foil_ira_localization_utilization_false_stage2_high_mae|2024-03-21"}
{"row_type":"trigger","case_id":"C13-R3L99-05","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_IRA_UTILIZATION_LABEL_HARD_FALSE_STAGE2","symbol":"393890","name":"더블유씨피","trigger_type":"separator_ira_utilization_label_hard_false_stage2","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750,"peak_price":49400,"peak_date":"2024-02-22","trough_price":16800,"trough_date":"2024-09-09","mfe_pct":7.98,"mae_pct":-63.28,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"separator_IRA_utilization_label_failed_under_utilization_and_margin_break","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|393890|separator_ira_utilization_label_hard_false_stage2|2024-02-21"}
```

## 6. Score-return alignment

### 6.1 Cell-maker and battery-parent recovery family

`373220`, `006400`, and `096770` are the constructive C13 side, but with different quality. `373220` and `096770` repaired with limited MAE from depressed entries, while `006400` had strong MFE but later gave back enough to require a sizing guard. C13 should therefore allow recovery-watch or Stage3-Yellow only when JV utilization, AMPC recognition, fixed-cost absorption and FCF evidence are visible.

### 6.2 Material-chain IRA label false Stage2

`020150` and `393890` show why C13 should not let IRA/localization language repair material-chain rows automatically. Copper foil and separator names can sound like localization beneficiaries, but if utilization, customer pull, inventory and margin fail, AMPC/IRA vocabulary does not close the cash bridge.

### 6.3 C12 separation

C12 asks whether the customer actually pulls contracted volume. C13 asks whether the qualified JV or localized production creates cash through AMPC/IRA and utilization. The two can overlap, but they should not rescue each other unless the non-price bridge is explicit.

## 7. Raw component score simulation

| symbol | JV/AMPC/IRA evidence | utilization / qualified output | cash conversion / FCF | price confirmation | MAE/material-chain guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 373220 | 21 | 15 | 12 | 15 | -3 | 60 | 4B recovery-watch / Stage3-Yellow candidate |
| 006400 | 18 | 12 | 8 | 17 | -8 | 47 | Stage2→Yellow with utilization guard |
| 096770 | 18 | 13 | 8 | 16 | -2 | 53 | Stage3-Yellow recovery candidate |
| 020150 | 15 | 5 | 3 | 5 | -16 | 12 | Stage2/local 4B |
| 393890 | 15 | 3 | 2 | 3 | -25 | -2 | Hard counterexample / 4C watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c13_JV_AMPC_requires_utilization_cash_conversion_bridge","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"stage2_required_bridge","rule":"Do not promote battery JV/AMPC/IRA labels above Stage2 unless qualified output, JV utilization, AMPC recognition, fixed-cost absorption, cash conversion, working capital, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["020150","393890"],"counterbalanced_by":["373220","006400","096770"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c13_cell_maker_AMPC_recovery_positive_delta","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"recovery_watch_or_stage3_yellow_candidate","rule":"Cell makers or battery parents can receive recovery-watch/Stage3-Yellow treatment when JV utilization, AMPC recognition, fixed-cost absorption, and FCF bridge are URL-verified.","supporting_cases":["373220","096770"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c13_cell_maker_rebound_sizing_guard","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"stage2_to_yellow_with_utilization_fcf_guard","rule":"Cell-maker JV/AMPC rebounds with large MFE but meaningful full-window MAE should require staged sizing and utilization/FCF proof before promotion.","supporting_cases":["006400"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c13_material_chain_IRA_false_stage2_guard","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"local_4b_or_hard_4c_watch","rule":"Material-chain IRA/localization labels with high MAE should remain local 4B or hard 4C unless utilization, customer pull, inventory and margin evidence repairs the row.","supporting_cases":["020150","393890"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c13_do_not_use_AMPC_as_C12_contract_repair","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"C12_C13_separation_guard","rule":"AMPC/IRA should not repair customer contract/call-off risk unless it directly improves shipment cadence, utilization, working capital, OPM or FCF; otherwise keep C12 call-off risk separate.","supporting_cases":["020150","393890"],"counterbalanced_by":["373220","096770"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","round":"R3","loop":"99","positive_rows":3,"counterexample_rows":2,"new_symbol_count":5,"primary_residual":"C13 should separate cell-maker/battery-parent JV AMPC recovery where utilization and cash conversion can repair the path from material-chain IRA/localization labels that fail under utilization, inventory and margin pressure.","candidate_patch_axes":["stage2_required_bridge","recovery_watch_or_stage3_yellow_candidate","stage2_to_yellow_with_utilization_fcf_guard","local_4b_or_hard_4c_watch","C12_C13_separation_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","sample_count":5,"avg_mfe_pct":23.62,"avg_mae_pct":-24.62,"median_mfe_pct":26.86,"median_mae_pct":-18.31,"interpretation":"C13 can work in cell-maker/JV recovery rows when AMPC and utilization plausibly convert to cash, but material-chain IRA labels need strict local 4B/4C guardrails."}
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
- Ingest this C13 R3 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c13_JV_AMPC_requires_utilization_cash_conversion_bridge -> stage2_required_bridge
  2. c13_cell_maker_AMPC_recovery_positive_delta -> recovery_watch_or_stage3_yellow_candidate
  3. c13_cell_maker_rebound_sizing_guard -> stage2_to_yellow_with_utilization_fcf_guard
  4. c13_material_chain_IRA_false_stage2_guard -> local_4b_or_hard_4c_watch
  5. c13_do_not_use_AMPC_as_C12_contract_repair -> C12_C13_separation_guard

Expected behavior:
- Battery JV/AMPC/IRA vocabulary alone should not create Green.
- Qualified output, JV utilization, AMPC recognition, fixed-cost absorption, cash conversion, OPM, FCF or EPS revision can justify Stage3-Yellow/recovery-watch.
- Material-chain IRA/localization labels with high MAE should stay local 4B or hard 4C unless non-price evidence repairs the row.
- C13 policy-credit logic should not automatically repair C12 customer call-off risk.
```
