# E2R Stock-Web v12 Residual Research — R3 loop 99 / L3 / C13

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 99
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: CELL_MAKER_JV_UTILIZATION_AMPC_IRA_CASH_CONVERSION_BRIDGE_VS_POLICY_SUBSIDY_LABEL_AND_MATERIAL_CAPACITY_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - JV_utilization_AMPC_cash_bridge_test
  - AMPC_IRA_vs_customer_calloff_boundary_guard
  - policy_subsidy_false_stage2_guard
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

이번 파일은 `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` 전용 residual research다.

C13은 “IRA”, “AMPC”, “북미 JV”, “미국 공장”, “정책 수혜” 같은 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 JV 가동률이 실제 출하량과 AMPC 인식으로 연결되고, 그 보조금 성격의 이익이 cash conversion, margin, FCF, EPS revision으로 내려오는지다.

```text
battery JV / AMPC / IRA headline
  → US plant utilization / shipment / qualifying production
  → AMPC recognition / cost absorption / cash conversion
  → margin / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

AMPC는 공장에 붙은 전기 보조 장치와 같다. 콘센트가 있어도 라인이 돌지 않으면 전기는 흘러가지 않는다. C13은 “정책 콘센트가 있다”와 “공장이 실제로 전류를 흘려 현금을 만든다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["373220","096770","006400","003670"],"profile_paths":["atlas/symbol_profiles/373/373220.json","atlas/symbol_profiles/096/096770.json","atlas/symbol_profiles/006/006400.json","atlas/symbol_profiles/003/003670.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv"],"validation_scope":"2024 trigger-level forward path; 373220 has no corporate-action candidates; 096770 caveat is 2024-11-20 so the selected pre-caveat path is treated as valid; 006400 caveats are historical; 003670 caveats are 2015/2021 and outside selected 2024 local windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C13 at 27 rows and asks for JV utilization, AMPC, utilization, and cash conversion expansion.
- Existing registry shows C13 parsed through `R3 loop 98`.
- This output uses `R3 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates cell-maker AMPC/utilization recovery, SK On/policy bridge, cell-maker rebound decay, and cathode material capacity label false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C13-R3L99-01 | 373220 | LG에너지솔루션 | 2024-08-21 | 2024-08-21 | 350000 | 444000 | 332000 | 26.86% | -5.14% | Cell-maker AMPC/JV utilization recovery path worked with contained MAE. |
| C13-R3L99-02 | 096770 | SK이노베이션 | 2024-08-27 | 2024-08-27 | 109800 | 125000 | 105200 | 13.84% | -4.19% | SK On / AMPC-policy recovery path was constructive before corporate-action caveat window. |
| C13-R3L99-03 | 006400 | 삼성SDI | 2024-08-21 | 2024-08-21 | 328500 | 393500 | 235500 | 19.79% | -28.31% | Cell-maker rebound had MFE but later decay says utilization/FCF bridge was insufficient. |
| C13-R3L99-04 | 003670 | 포스코퓨처엠 | 2024-09-02 | 2024-09-02 | 246500 | 264000 | 201000 | 7.10% | -18.46% | Battery-material capacity/policy label was weaker; AMPC/JV evidence cannot be transferred mechanically. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C13-R3L99-01","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CELL_MAKER_AMPC_JV_UTILIZATION_RECOVERY_CASH_BRIDGE","symbol":"373220","name":"LG에너지솔루션","trigger_type":"cell_maker_ampc_jv_utilization_recovery_cash_bridge","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000,"peak_price":444000,"peak_date":"2024-10-08","trough_price":332000,"trough_date":"2024-08-21","mfe_pct":26.86,"mae_pct":-5.14,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_AMPC_utilization_FCF_URLs","residual_flag":"positive_cell_maker_AMPC_utilization_path_but_requires_cash_conversion_URLs","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|cell_maker_ampc_jv_utilization_recovery_cash_bridge|2024-08-21"}
{"row_type":"trigger","case_id":"C13-R3L99-02","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SK_ON_AMPC_IRA_POLICY_UTILIZATION_BRIDGE_PRE_CA_WINDOW","symbol":"096770","name":"SK이노베이션","trigger_type":"sk_on_ampc_ira_policy_utilization_bridge_pre_ca_window","trigger_date":"2024-08-27","entry_date":"2024-08-27","entry_price":109800,"peak_price":125000,"peak_date":"2024-10-10","trough_price":105200,"trough_date":"2024-09-04","mfe_pct":13.84,"mae_pct":-4.19,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_candidate_pending_utilization_URLs","residual_flag":"policy_AMPC_recovery_constructive_but_needs_real_utilization_cash_bridge","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|096770|sk_on_ampc_ira_policy_utilization_bridge_pre_ca_window|2024-08-27"}
{"row_type":"trigger","case_id":"C13-R3L99-03","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CELL_MAKER_AMPC_REBOUND_HIGH_MAE_FCF_DECAY","symbol":"006400","name":"삼성SDI","trigger_type":"cell_maker_ampc_rebound_high_mae_fcf_decay","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":328500,"peak_price":393500,"peak_date":"2024-09-30","trough_price":235500,"trough_date":"2024-11-15","mfe_pct":19.79,"mae_pct":-28.31,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"cell_maker_policy_rebound_decayed_without_durable_utilization_FCF_bridge","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|cell_maker_ampc_rebound_high_mae_fcf_decay|2024-08-21"}
{"row_type":"trigger","case_id":"C13-R3L99-04","round":"R3","loop":"99","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_MATERIAL_CAPACITY_POLICY_LABEL_FALSE_STAGE2","symbol":"003670","name":"포스코퓨처엠","trigger_type":"battery_material_capacity_policy_label_false_stage2","trigger_date":"2024-09-02","entry_date":"2024-09-02","entry_price":246500,"peak_price":264000,"peak_date":"2024-09-30","trough_price":201000,"trough_date":"2024-09-10","mfe_pct":7.10,"mae_pct":-18.46,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"material_capacity_label_should_not_inherit_cell_maker_AMPC_score_without_utilization_cash_bridge","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|003670|battery_material_capacity_policy_label_false_stage2|2024-09-02"}
```

## 6. Score-return alignment

### 6.1 Cell-maker AMPC/utilization positive family

`373220` is the cleanest C13 positive path in this sample. The price path after 2024-08-21 made strong MFE with limited MAE. This supports treating cell-maker AMPC/JV utilization recovery as a Stage3-Yellow candidate, but only when shipment, qualifying production, AMPC recognition, and FCF evidence are present.

### 6.2 Policy recovery but not proof by itself

`096770` shows a constructive but less direct path. The price action before the 2024-11-20 corporate-action caveat window was positive and controlled, but the rule should still require evidence that policy/AMPC vocabulary is tied to real utilization and cash conversion, not just balance-sheet or merger/policy sympathy.

### 6.3 Rebound decay and material-label transfer risk

`006400` and `003670` are the guardrail rows. `006400` initially worked, but the drawdown later became much larger than the entry cushion. `003670` shows why C13 should not transfer cell-maker AMPC/JV scores to all battery material/capacity names. Material capacity or policy vocabulary should remain Stage2/local 4B unless utilization and cash conversion bridge is visible.

## 7. Raw component score simulation

| symbol | JV/AMPC/IRA evidence | utilization/shipment bridge | AMPC/cash conversion | margin/FCF bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 373220 | 22 | 18 | 17 | 14 | 19 | -3 | 78 | Stage3-Yellow candidate |
| 096770 | 18 | 13 | 12 | 9 | 12 | -2 | 62 | Stage2→Yellow candidate |
| 006400 | 18 | 10 | 8 | 5 | 12 | -12 | 41 | Stage2/Yellow high-MAE guard |
| 003670 | 12 | 5 | 4 | 3 | 4 | -9 | 19 | Stage2/local 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c13_ampc_ira_requires_utilization_cash_bridge","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"stage2_required_bridge","rule":"Do not promote JV/AMPC/IRA/policy labels above Stage2 unless utilization, shipment, qualifying production, AMPC recognition, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["006400","003670"],"counterbalanced_by":["373220","096770"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c13_cell_maker_ampc_positive_delta","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"stage3_yellow_candidate_delta","rule":"Cell makers with verified JV utilization, qualifying production, AMPC recognition, and cash conversion can receive Stage3-Yellow treatment; Green requires drawdown containment and exact URL evidence.","supporting_cases":["373220","096770"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c13_policy_rebound_high_mae_guardrail","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"local_4b_watch_guard","rule":"If AMPC/IRA/policy rebound MFE is followed by deep MAE and FCF bridge is absent, cap at local 4B or event-cap until utilization evidence repairs the row.","supporting_cases":["006400"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c13_material_capacity_peer_transfer_guard","scope":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","candidate_action":"canonical_boundary_guard","rule":"Do not transfer cell-maker JV/AMPC score to battery material capacity labels unless the material name has its own shipment, utilization, cash conversion, and margin bridge.","supporting_cases":["003670"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","round":"R3","loop":"99","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C13 should separate cell-maker JV/AMPC utilization recovery from generic policy subsidy and battery-material capacity labels without FCF/cash conversion bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","local_4b_watch_guard","canonical_boundary_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","sample_count":4,"avg_mfe_pct":16.90,"avg_mae_pct":-14.03,"median_mfe_pct":16.82,"median_mae_pct":-11.80,"interpretation":"C13 can produce constructive paths when cell-maker utilization and AMPC/cash conversion are real, but policy or material-capacity labels decay without utilization and FCF evidence."}
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
  1. c13_ampc_ira_requires_utilization_cash_bridge -> stage2_required_bridge
  2. c13_cell_maker_ampc_positive_delta -> stage3_yellow_candidate_delta
  3. c13_policy_rebound_high_mae_guardrail -> local_4b_watch_guard
  4. c13_material_capacity_peer_transfer_guard -> canonical_boundary_guard

Expected behavior:
- JV/AMPC/IRA vocabulary alone should not create Green.
- Utilization, shipment, qualifying production, AMPC recognition, margin, FCF or EPS revision can justify Stage3-Yellow.
- Material-capacity labels must not inherit cell-maker AMPC/JV scores without their own cash-conversion bridge.
```
