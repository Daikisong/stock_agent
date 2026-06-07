# E2R Stock-Web v12 Residual Research — R1 loop 96 / L1 / C03

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 96
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: K_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_CONVERSION_VS_DEFENSE_ELECTRONICS_SENSOR_LATE_CHASE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill_to_50
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - defense_export_framework_to_delivery_margin_bridge_test
  - backlog_delivery_schedule_cash_conversion_guardrail
  - missile_precision_weapon_export_positive_delta
  - aircraft_export_framework_midcase_guard
  - defense_electronics_sensor_late_chase_false_stage2_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` 전용 residual research다.

C03은 “방산 수출”, “폴란드/중동/동유럽 framework”, “K-방산”, “지정학 리스크”, “방산전자/센서/우주방산”이라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 수출 framework가 실제 firm contract, delivery schedule, production slot, backlog quality, FX/cost pass-through, working capital, OPM, FCF, EPS revision으로 내려오는지다.

```text
defense export / framework / geopolitical headline
  → firm contract / option exercise / delivery schedule
  → production capacity / backlog quality / FX and cost pass-through
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

방산 framework는 탄약고의 출고 예약표와 같다. 예약표가 있다 해도 실제 계약서가 닫히고, 생산 슬롯이 배정되고, 납품과 대금 회수가 이어져야 포탄이 매출로 바뀐다. C03은 “수출 이야기가 있다”와 “납품·마진·현금이 닫혔다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["012450","064350","079550","047810","272210"],"profile_paths":["atlas/symbol_profiles/012/012450.json","atlas/symbol_profiles/064/064350.json","atlas/symbol_profiles/079/079550.json","atlas/symbol_profiles/047/047810.json","atlas/symbol_profiles/272/272210.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv","atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv","atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv"],"validation_scope":"2024 trigger-level forward path; 012450 caveats end 2009, 064350 caveat is 2020, 079550/047810 have zero corporate-action candidates, and 272210 caveat is 2021. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C03 at 30 rows and 20 rows short of the 50-row practical calibration target.
- Existing registry shows C03 parsed through `R1 loop 95`.
- This output uses `R1 loop 96`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C03 loop 95 emphasized land systems / defense electronics / rugged computing export backlog. This file compresses prime defense exporter backlog, K2 tank delivery conversion, missile precision weapon export, aircraft export framework middle case, and defense electronics/sensor late-chase false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C03-R1L96-01 | 012450 | 한화에어로스페이스 | 2024-02-26 | 2024-02-26 | 166200 | 425000 | 155800 | 155.72% | -6.26% | Prime defense-export backlog framework rerated explosively; delivery/margin bridge candidate. |
| C03-R1L96-02 | 064350 | 현대로템 | 2024-07-26 | 2024-07-26 | 47750 | 68000 | 41000 | 42.41% | -14.14% | K2 export/delivery backlog worked, but August drawdown requires sizing and delivery-cash guard. |
| C03-R1L96-03 | 079550 | LIG넥스원 | 2024-03-06 | 2024-03-06 | 168500 | 265000 | 160800 | 57.27% | -4.57% | Missile/precision weapon export path showed strong MFE and controlled initial MAE. |
| C03-R1L96-04 | 047810 | 한국항공우주 | 2024-07-26 | 2024-07-26 | 51100 | 60500 | 48000 | 18.40% | -6.07% | Aircraft export framework/recovery worked moderately; delivery and program margin bridge needed. |
| C03-R1L96-05 | 272210 | 한화시스템 | 2024-07-24 | 2024-07-24 | 22250 | 23400 | 16530 | 5.17% | -25.71% | Defense electronics/sensor late-chase label had tiny MFE and high MAE; false Stage2 guard. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C03-R1L96-01","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"PRIME_DEFENSE_EXPORT_BACKLOG_DELIVERY_MARGIN_CONVERSION","symbol":"012450","name":"한화에어로스페이스","trigger_type":"prime_defense_export_backlog_delivery_margin_conversion","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":166200,"peak_price":425000,"peak_date":"2024-11-12","trough_price":155800,"trough_date":"2024-02-26","mfe_pct":155.72,"mae_pct":-6.26,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_delivery_OPM_FCF_URLs","residual_flag":"prime_defense_export_backlog_positive_but_exact_contract_delivery_margin_cash_URLs_required","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|prime_defense_export_backlog_delivery_margin_conversion|2024-02-26"}
{"row_type":"trigger","case_id":"C03-R1L96-02","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"K2_TANK_EXPORT_DELIVERY_BACKLOG_MARGIN_BRIDGE_WITH_SIZING_GUARD","symbol":"064350","name":"현대로템","trigger_type":"k2_tank_export_delivery_backlog_margin_bridge_with_sizing_guard","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":47750,"peak_price":68000,"peak_date":"2024-10-18","trough_price":41000,"trough_date":"2024-08-05","mfe_pct":42.41,"mae_pct":-14.14,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_delivery_schedule_cash_URLs","residual_flag":"K2_export_delivery_path_worked_but_August_drawdown_requires_sizing_and_working_capital_guard","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|k2_tank_export_delivery_backlog_margin_bridge_with_sizing_guard|2024-07-26"}
{"row_type":"trigger","case_id":"C03-R1L96-03","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"MISSILE_PRECISION_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","symbol":"079550","name":"LIG넥스원","trigger_type":"missile_precision_weapon_export_backlog_margin_bridge","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":168500,"peak_price":265000,"peak_date":"2024-10-22","trough_price":160800,"trough_date":"2024-03-15","mfe_pct":57.27,"mae_pct":-4.57,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_export_order_margin_URLs","residual_flag":"missile_precision_weapon_export_path_positive_but_requires_customer_delivery_OPM_FCF_URLs","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|079550|missile_precision_weapon_export_backlog_margin_bridge|2024-03-06"}
{"row_type":"trigger","case_id":"C03-R1L96-04","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"AIRCRAFT_EXPORT_FRAMEWORK_PROGRAM_DELIVERY_MARGIN_GUARD","symbol":"047810","name":"한국항공우주","trigger_type":"aircraft_export_framework_program_delivery_margin_guard","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":51100,"peak_price":60500,"peak_date":"2024-10-30","trough_price":48000,"trough_date":"2024-08-05","mfe_pct":18.40,"mae_pct":-6.07,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_program_margin_guard","residual_flag":"aircraft_export_framework_midcase_requires_program_delivery_acceptance_margin_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|047810|aircraft_export_framework_program_delivery_margin_guard|2024-07-26"}
{"row_type":"trigger","case_id":"C03-R1L96-05","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_ELECTRONICS_SENSOR_LATE_CHASE_FALSE_STAGE2_HIGH_MAE","symbol":"272210","name":"한화시스템","trigger_type":"defense_electronics_sensor_late_chase_false_stage2_high_mae","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":22250,"peak_price":23400,"peak_date":"2024-07-30","trough_price":16530,"trough_date":"2024-09-09","mfe_pct":5.17,"mae_pct":-25.71,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_false_Stage2","residual_flag":"defense_electronics_sensor_label_late_chase_failed_without_export_contract_delivery_margin_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|272210|defense_electronics_sensor_late_chase_false_stage2_high_mae|2024-07-24"}
```

## 6. Score-return alignment

### 6.1 Defense export backlog winners

`012450` and `079550` are the strongest C03 positive family. The price paths suggest that the market rewarded export framework, backlog, precision weapon systems, production visibility and margin conversion. These rows can justify Stage3-Yellow/Green candidates after exact contract, delivery, margin and FCF evidence is URL-verified.

### 6.2 Land systems and aircraft midcases

`064350` and `047810` worked, but not identically. `064350` had larger MFE and larger drawdown; it needs a sizing guard tied to delivery schedule, working capital and cost pass-through. `047810` was a more moderate aircraft export/program row; it should be Yellow only when program delivery, acceptance, and margin bridge is visible.

### 6.3 Defense electronics/sensor late-chase trap

`272210` is the local 4B/false Stage2 guardrail. Defense electronics, sensor and space-defense vocabulary can spike, but without fresh export contract, delivery schedule and margin bridge, a late-chase entry can carry poor asymmetry. This row should not inherit prime defense exporter scores.

## 7. Raw component score simulation

| symbol | export/framework evidence | backlog/delivery schedule | margin/FCF bridge | price confirmation | MAE/timing guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 012450 | 24 | 21 | 18 | 25 | -3 | 85 | Stage3-Yellow/Green candidate |
| 064350 | 22 | 17 | 13 | 17 | -7 | 62 | Stage3-Yellow with sizing guard |
| 079550 | 23 | 18 | 15 | 21 | -2 | 75 | Stage3-Yellow/Green candidate |
| 047810 | 18 | 12 | 8 | 9 | -4 | 43 | Stage2→Yellow with program guard |
| 272210 | 15 | 5 | 3 | 2 | -13 | 12 | Local 4B / false Stage2 |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c03_defense_export_requires_contract_delivery_margin_FCF_bridge","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_required_bridge","rule":"Do not promote defense export/framework/geopolitical labels above Stage2 unless firm contract, option exercise, delivery schedule, production capacity, backlog quality, FX/cost pass-through, working capital, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["272210","047810"],"counterbalanced_by":["012450","064350","079550"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_prime_defense_export_positive_delta","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Prime defense exporters and precision weapon names with verified export backlog, delivery cadence and margin/FCF bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["012450","079550"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_land_systems_delivery_sizing_guard","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage3_yellow_candidate_with_sizing_guard","rule":"Land systems export backlog rows can be Yellow/Stage3 candidates, but meaningful interim MAE requires staged sizing, delivery schedule and working-capital guard.","supporting_cases":["064350"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_aircraft_export_program_margin_guard","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_to_yellow_with_program_guard","rule":"Aircraft export framework rows should require program delivery, acceptance, cost execution and margin bridge before promotion beyond Stage2.","supporting_cases":["047810"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_defense_electronics_sensor_late_chase_guard","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"local_4b_or_false_stage2_guard","rule":"Defense electronics, sensor, or space-defense rows with late-chase entry, tiny MFE and high MAE should remain local 4B unless fresh export contract and delivery/margin evidence repairs the row.","supporting_cases":["272210"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","round":"R1","loop":"96","positive_rows":3,"counterexample_rows":2,"new_symbol_count":5,"primary_residual":"C03 should separate prime defense export and missile/land-system backlog winners from aircraft midcases and defense-electronics/sensor late-chase labels that lack firm contract, delivery schedule and margin/FCF bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage3_yellow_candidate_with_sizing_guard","stage2_to_yellow_with_program_guard","local_4b_or_false_stage2_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","sample_count":5,"avg_mfe_pct":55.79,"avg_mae_pct":-11.35,"median_mfe_pct":42.41,"median_mae_pct":-6.26,"interpretation":"C03 can produce very strong upside when export framework becomes delivery backlog and margin conversion, but late-chase defense electronics/sensor labels need strict 4B/Stage2 caps."}
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
- Ingest this C03 R1 loop 96 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c03_defense_export_requires_contract_delivery_margin_FCF_bridge -> stage2_required_bridge
  2. c03_prime_defense_export_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c03_land_systems_delivery_sizing_guard -> stage3_yellow_candidate_with_sizing_guard
  4. c03_aircraft_export_program_margin_guard -> stage2_to_yellow_with_program_guard
  5. c03_defense_electronics_sensor_late_chase_guard -> local_4b_or_false_stage2_guard

Expected behavior:
- Defense export/framework/geopolitical vocabulary alone should not create Green.
- Firm contract, option exercise, delivery schedule, production capacity, backlog quality, FX/cost pass-through, working capital, OPM, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Defense electronics/sensor late-chase rows should remain local 4B or false Stage2 until fresh non-price evidence appears.
```
