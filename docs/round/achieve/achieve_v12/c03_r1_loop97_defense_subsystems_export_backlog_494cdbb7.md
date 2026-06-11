# E2R Stock-Web v12 Residual Research — R1 loop 97 / L1 / C03

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 97
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_SUBSYSTEMS_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_SENSOR_SPACE_DEFENSE_THEME_SPIKE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill_to_50
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - defense_subsystem_export_backlog_delivery_bridge_test
  - powertrain_smallarms_sensor_space_defense_margin_guardrail
  - subsystem_vs_prime_exporter_score_separation
  - high_MAE_false_stage2_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG`의 두 번째 보강축이다.

직전 C03 loop 96은 prime defense exporter, land-system leader, missile/precision weapon, aircraft prime, defense electronics late-chase를 다뤘다. 이번 loop 97은 한 단계 아래의 subsystem 계층을 다룬다. 즉 방산 powertrain, small-arms/vehicle components, infrared sensor, rugged mission computer, space-defense communication이 실제 export framework와 backlog delivery, customer acceptance, OPM/FCF bridge로 이어지는지 점검한다.

```text
defense subsystem / export framework headline
  → firm subsystem contract / platform inclusion / delivery schedule
  → acceptance / production slot / working capital / margin
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

방산 subsystem은 전차와 미사일의 심장·눈·신경이다. 완성품 수출 story가 커도, 하위 부품사가 실제 납품 단가와 물량, 검수, 현금화를 받지 못하면 주가는 테마의 연기만 마시고 꺼진다. C03은 prime exporter와 subsystem을 같은 점수로 보지 않는다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["003570","064960","214430","448710","361390"],"profile_paths":["atlas/symbol_profiles/003/003570.json","atlas/symbol_profiles/064/064960.json","atlas/symbol_profiles/214/214430.json","atlas/symbol_profiles/448/448710.json","atlas/symbol_profiles/361/361390.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv","atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv","atlas/ohlcv_tradable_by_symbol_year/214/214430/2024.csv","atlas/ohlcv_tradable_by_symbol_year/448/448710/2024.csv","atlas/ohlcv_tradable_by_symbol_year/361/361390/2024.csv"],"validation_scope":"2024 trigger-level forward path; 003570 caveats are historical and end 2006; 214430 caveats are 2017; 448710 has zero corporate-action candidates; 361390 caveats are 2021; selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C03 at 30 rows and 20 rows short of the 50-row practical calibration target.
- Repo registry shows C03 parsed through `R1 loop 95`; the prior local session emitted C03 R1 loop 96, so this file uses C03 R1 loop 97.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file uses symbols not used in C03 loop 96: `003570`, `064960`, `214430`, `448710`, `361390`.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C03-R1L97-01 | 003570 | SNT다이내믹스 | 2024-07-26 | 2024-07-26 | 21150 | 28200 | 18600 | 33.33% | -12.06% | Powertrain/transmission subsystem export path worked, but August drawdown requires delivery and working-capital guard. |
| C03-R1L97-02 | 064960 | SNT모티브 | 2024-03-06 | 2024-03-06 | 46650 | 49650 | 39500 | 6.43% | -15.33% | Small-arms/vehicle component defense label had weak MFE and needs margin bridge before promotion. |
| C03-R1L97-03 | 214430 | 아이쓰리시스템 | 2024-03-06 | 2024-03-06 | 34850 | 51200 | 24600 | 46.92% | -29.41% | Infrared sensor/defense electronics optionality created MFE, but high MAE blocks Green. |
| C03-R1L97-04 | 448710 | 코츠테크놀로지 | 2024-03-06 | 2024-03-06 | 19000 | 29750 | 15760 | 56.58% | -17.05% | Rugged mission-computer subsystem rerated, but later drawdown needs delivery/margin proof. |
| C03-R1L97-05 | 361390 | 제노코 | 2024-02-22 | 2024-02-22 | 17510 | 17740 | 11290 | 1.31% | -35.52% | Space-defense communication label was low-MFE/high-MAE false Stage2. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C03-R1L97-01","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_POWERTRAIN_TRANSMISSION_EXPORT_DELIVERY_MARGIN_BRIDGE","symbol":"003570","name":"SNT다이내믹스","trigger_type":"defense_powertrain_transmission_export_delivery_margin_bridge","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":21150,"peak_price":28200,"peak_date":"2024-10-23","trough_price":18600,"trough_date":"2024-08-05","mfe_pct":33.33,"mae_pct":-12.06,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_delivery_margin_guard","residual_flag":"subsystem_powertrain_export_path_positive_but_requires_platform_delivery_working_capital_OPM_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|003570|defense_powertrain_transmission_export_delivery_margin_bridge|2024-07-26"}
{"row_type":"trigger","case_id":"C03-R1L97-02","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"SMALL_ARMS_VEHICLE_COMPONENT_DEFENSE_LABEL_LOW_MFE_MARGIN_GUARD","symbol":"064960","name":"SNT모티브","trigger_type":"small_arms_vehicle_component_defense_label_low_mfe_margin_guard","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":46650,"peak_price":49650,"peak_date":"2024-09-12","trough_price":39500,"trough_date":"2024-08-05","mfe_pct":6.43,"mae_pct":-15.33,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"small_arms_vehicle_component_label_low_MFE_without_fresh_export_backlog_margin_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064960|small_arms_vehicle_component_defense_label_low_mfe_margin_guard|2024-03-06"}
{"row_type":"trigger","case_id":"C03-R1L97-03","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"INFRARED_SENSOR_DEFENSE_ELECTRONICS_OPTIONALITY_HIGH_MAE_GUARD","symbol":"214430","name":"아이쓰리시스템","trigger_type":"infrared_sensor_defense_electronics_optionality_high_mae_guard","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":34850,"peak_price":51200,"peak_date":"2024-03-29","trough_price":24600,"trough_date":"2024-08-05","mfe_pct":46.92,"mae_pct":-29.41,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"sensor_optional_MFE_but_delivery_acceptance_customer_margin_bridge_required","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|214430|infrared_sensor_defense_electronics_optionality_high_mae_guard|2024-03-06"}
{"row_type":"trigger","case_id":"C03-R1L97-04","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"RUGGED_MISSION_COMPUTER_SUBSYSTEM_DELIVERY_MARGIN_BRIDGE_WITH_HIGH_MAE_GUARD","symbol":"448710","name":"코츠테크놀로지","trigger_type":"rugged_mission_computer_subsystem_delivery_margin_bridge_with_high_mae_guard","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":19000,"peak_price":29750,"peak_date":"2024-04-09","trough_price":15760,"trough_date":"2024-09-09","mfe_pct":56.58,"mae_pct":-17.05,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_subsystem_margin_guard","residual_flag":"rugged_computer_defense_subsystem_rerating_worked_but_later_MAE_requires_contract_delivery_OPM_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|448710|rugged_mission_computer_subsystem_delivery_margin_bridge_with_high_mae_guard|2024-03-06"}
{"row_type":"trigger","case_id":"C03-R1L97-05","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"SPACE_DEFENSE_COMMUNICATION_LABEL_LOW_MFE_HIGH_MAE_FALSE_STAGE2","symbol":"361390","name":"제노코","trigger_type":"space_defense_communication_label_low_mfe_high_mae_false_stage2","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":17510,"peak_price":17740,"peak_date":"2024-02-22","trough_price":11290,"trough_date":"2024-09-11","mfe_pct":1.31,"mae_pct":-35.52,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"space_defense_comm_label_tiny_MFE_high_MAE_without_export_contract_delivery_margin_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|361390|space_defense_communication_label_low_mfe_high_mae_false_stage2|2024-02-22"}
```

## 6. Score-return alignment

### 6.1 Subsystem winners are not prime exporters

`003570`, `214430`, and `448710` show that subsystem names can create real MFE when the market infers platform inclusion, export order flow, and delivery leverage. But the MAE is materially larger than in prime defense winners. C03 should therefore promote subsystem rows only after platform-level contract, delivery schedule, customer acceptance, working capital and OPM/FCF evidence is visible.

### 6.2 Low-MFE component and space-defense labels

`064960` and `361390` are the false-stage side. They had defense vocabulary, but the forward path did not show strong asymmetry from the selected trigger. C03 should cap small-arms/vehicle-component and space-defense communication labels when there is no fresh backlog/delivery/margin bridge.

### 6.3 Mechanism

The key separation is prime contract versus embedded subsystem. A prime exporter can own backlog visibility; a subsystem supplier must prove it is actually inside the platform, has accepted delivery schedule, and can convert that schedule into margin and cash.

## 7. Raw component score simulation

| symbol | export/framework evidence | subsystem platform inclusion | delivery/acceptance | margin/FCF bridge | price confirmation | MAE/timing guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 003570 | 17 | 16 | 12 | 9 | 13 | -6 | 61 | Stage2→Yellow |
| 064960 | 13 | 8 | 5 | 4 | 2 | -7 | 25 | Stage2/local 4B |
| 214430 | 16 | 13 | 8 | 6 | 15 | -14 | 44 | Stage2→Yellow high-MAE guard |
| 448710 | 16 | 14 | 9 | 6 | 17 | -8 | 54 | Stage2→Yellow with margin guard |
| 361390 | 12 | 5 | 3 | 2 | 0 | -16 | 6 | Hard counterexample/local 4B |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c03_subsystem_export_requires_platform_delivery_margin_bridge","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_required_bridge","rule":"Do not promote defense subsystem/export-framework labels above Stage2 unless platform inclusion, firm contract, delivery schedule, customer acceptance, working capital, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["064960","361390"],"counterbalanced_by":["003570","214430","448710"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_powertrain_transmission_subsystem_positive_delta","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_to_yellow_with_delivery_guard","rule":"Defense powertrain/transmission subsystem rows can become Yellow when export platform delivery, working capital, and OPM bridge are URL-verified.","supporting_cases":["003570"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_sensor_rugged_computer_high_MAE_guard","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_to_yellow_with_high_MAE_guardrail","rule":"Sensor and rugged mission-computer rows can produce MFE, but high MAE blocks Green unless customer acceptance and margin/FCF bridge is verified.","supporting_cases":["214430","448710"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_small_arms_vehicle_component_low_MFE_guard","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_or_local_4b_watch","rule":"Small-arms/vehicle-component defense labels with low MFE should remain Stage2/local 4B without fresh backlog, export, or margin evidence.","supporting_cases":["064960"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_space_defense_comm_false_stage2_guard","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"hard_counterexample_or_local_4b","rule":"Space-defense communication labels with tiny MFE and high MAE should be hard counterexamples unless firm contract and delivery/margin evidence repairs the row.","supporting_cases":["361390"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","round":"R1","loop":"97","positive_rows":3,"counterexample_rows":2,"new_symbol_count":5,"primary_residual":"C03 should separate subsystem export/delivery candidates from prime exporters; powertrain, sensor and mission-computer rows can work, but small-arms/vehicle-component and space-defense labels need strict local 4B/false Stage2 caps unless platform delivery and margin evidence appears.","candidate_patch_axes":["stage2_required_bridge","stage2_to_yellow_with_delivery_guard","stage2_to_yellow_with_high_MAE_guardrail","stage2_or_local_4b_watch","hard_counterexample_or_local_4b"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","sample_count":5,"avg_mfe_pct":28.91,"avg_mae_pct":-21.87,"median_mfe_pct":33.33,"median_mae_pct":-17.05,"interpretation":"Subsystem C03 rows show lower quality than prime exporters: MFE exists, but MAE is large unless platform inclusion, delivery and OPM/FCF bridge are verified."}
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
- Ingest this C03 R1 loop 97 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c03_subsystem_export_requires_platform_delivery_margin_bridge -> stage2_required_bridge
  2. c03_powertrain_transmission_subsystem_positive_delta -> stage2_to_yellow_with_delivery_guard
  3. c03_sensor_rugged_computer_high_MAE_guard -> stage2_to_yellow_with_high_MAE_guardrail
  4. c03_small_arms_vehicle_component_low_MFE_guard -> stage2_or_local_4b_watch
  5. c03_space_defense_comm_false_stage2_guard -> hard_counterexample_or_local_4b

Expected behavior:
- Defense subsystem vocabulary alone should not create Green.
- Platform inclusion, firm contract, delivery schedule, customer acceptance, working capital, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Small-arms/vehicle-component and space-defense communication rows with low MFE/high MAE should stay capped until fresh non-price evidence appears.
```
