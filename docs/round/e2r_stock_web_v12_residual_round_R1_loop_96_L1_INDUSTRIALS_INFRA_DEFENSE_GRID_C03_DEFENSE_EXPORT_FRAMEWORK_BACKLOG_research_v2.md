# E2R Stock-Web v12 Residual Research — R1 loop 96 / L1 / C03

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 96
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: AEROSPACE_MISSILE_LAND_SYSTEMS_AIRCRAFT_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE_AND_SLOW_DELIVERY
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - export_backlog_to_delivery_margin_bridge_test
  - late_chase_high_MAE_guardrail
  - defense_theme_peer_transfer_guard
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

C03은 “방산 수출”, “폴란드/중동/유럽 계약”, “백로그”, “방산 대장주”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 수출 프레임워크가 실제 계약 확정, delivery schedule, 생산능력, 환율/원가, OPM/FCF/EPS revision으로 내려오는지다.

```text
defense export / framework agreement / backlog headline
  → firm contract / delivery schedule / production capacity
  → cost-to-complete / FX / working capital / mix
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

방산 수출 프레임워크는 격납고에 걸린 출격 명령서와 같다. 명령서가 있어도 실제 출격과 정비, 탄약, 납품 일정, 대금 회수가 연결되어야 이익이 된다. C03은 “수출 기대”와 “인도·마진·현금화”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["012450","079550","064350","047810"],"profile_paths":["atlas/symbol_profiles/012/012450.json","atlas/symbol_profiles/079/079550.json","atlas/symbol_profiles/064/064350.json","atlas/symbol_profiles/047/047810.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv","atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv"],"validation_scope":"2024 trigger-level forward path; 079550 and 047810 have zero corporate-action candidates; 012450 caveats are old historical windows; 064350 caveat is 2020-08-14 and outside selected 2024 windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C03 at 30 rows and asks for defense export contract, backlog, delivery schedule, and margin conversion expansion.
- Existing registry shows C03 parsed through `R1 loop 95`.
- This output uses `R1 loop 96`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates aerospace/engine leader, missile/precision weapon leader, land systems exporter, slow aircraft delivery bridge, and same-leader late-chase event-cap risk.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C03-R1L96-01 | 012450 | 한화에어로스페이스 | 2024-02-26 | 2024-02-26 | 166200 | 425000 | 155800 | 155.72% | -6.26% | Aerospace/land-defense export backlog and margin conversion path worked strongly. |
| C03-R1L96-02 | 079550 | LIG넥스원 | 2024-02-14 | 2024-02-14 | 127000 | 265000 | 115400 | 108.66% | -9.13% | Missile/precision weapon export framework rerating worked with manageable initial MAE. |
| C03-R1L96-03 | 064350 | 현대로템 | 2024-03-29 | 2024-03-29 | 36800 | 68000 | 34100 | 84.78% | -7.34% | Land systems/K2 export delivery path produced large MFE after spring trigger. |
| C03-R1L96-04 | 047810 | 한국항공우주 | 2024-07-29 | 2024-07-29 | 54600 | 60500 | 48000 | 10.81% | -12.09% | Aircraft export/delivery label was weaker; margin/delivery bridge must be verified. |
| C03-R1L96-05 | 012450 | 한화에어로스페이스 | 2024-10-21 | 2024-10-21 | 381500 | 425000 | 318500 | 11.40% | -16.51% | Same leader but late-chase entry needs local 4B/event-cap guard. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C03-R1L96-01","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"AEROSPACE_ENGINE_LAND_DEFENSE_EXPORT_BACKLOG_MARGIN_CONVERSION_LEADER","symbol":"012450","name":"한화에어로스페이스","trigger_type":"aerospace_engine_land_defense_export_backlog_margin_conversion_leader","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":166200,"peak_price":425000,"peak_date":"2024-11-12","trough_price":155800,"trough_date":"2024-02-26","mfe_pct":155.72,"mae_pct":-6.26,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_delivery_margin_URLs","residual_flag":"positive_export_backlog_margin_path_but_requires_delivery_FCF_URLs","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|aerospace_engine_land_defense_export_backlog_margin_conversion_leader|2024-02-26"}
{"row_type":"trigger","case_id":"C03-R1L96-02","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"MISSILE_PRECISION_WEAPON_EXPORT_FRAMEWORK_DELIVERY_BACKLOG_BRIDGE","symbol":"079550","name":"LIG넥스원","trigger_type":"missile_precision_weapon_export_framework_delivery_backlog_bridge","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":127000,"peak_price":265000,"peak_date":"2024-10-22","trough_price":115400,"trough_date":"2024-02-14","mfe_pct":108.66,"mae_pct":-9.13,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_contract_delivery_URLs","residual_flag":"positive_precision_weapon_export_path_but_contract_delivery_margin_bridge_required","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|079550|missile_precision_weapon_export_framework_delivery_backlog_bridge|2024-02-14"}
{"row_type":"trigger","case_id":"C03-R1L96-03","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"LAND_SYSTEMS_EXPORT_DELIVERY_MARGIN_BRIDGE","symbol":"064350","name":"현대로템","trigger_type":"land_systems_export_delivery_margin_bridge","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":36800,"peak_price":68000,"peak_date":"2024-10-18","trough_price":34100,"trough_date":"2024-03-29","mfe_pct":84.78,"mae_pct":-7.34,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_delivery_margin_URLs","residual_flag":"land_systems_export_MFE_strong_but_delivery_and_working_capital_bridge_required","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|land_systems_export_delivery_margin_bridge|2024-03-29"}
{"row_type":"trigger","case_id":"C03-R1L96-04","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"AIRCRAFT_EXPORT_DELIVERY_SLOW_CONVERSION_MARGIN_GUARD","symbol":"047810","name":"한국항공우주","trigger_type":"aircraft_export_delivery_slow_conversion_margin_guard","trigger_date":"2024-07-29","entry_date":"2024-07-29","entry_price":54600,"peak_price":60500,"peak_date":"2024-10-30","trough_price":48000,"trough_date":"2024-08-05","mfe_pct":10.81,"mae_pct":-12.09,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_delivery_guard","residual_flag":"aircraft_export_label_MFE_limited_without_clear_delivery_margin_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|047810|aircraft_export_delivery_slow_conversion_margin_guard|2024-07-29"}
{"row_type":"trigger","case_id":"C03-R1L96-05","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"012450","name":"한화에어로스페이스","trigger_type":"defense_leader_late_chase_price_only_extension_4b","trigger_date":"2024-10-21","entry_date":"2024-10-21","entry_price":381500,"peak_price":425000,"peak_date":"2024-11-12","trough_price":318500,"trough_date":"2024-11-26","mfe_pct":11.40,"mae_pct":-16.51,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_leader_late_chase_without_fresh_delivery_margin_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|defense_leader_late_chase_price_only_extension_4b|2024-10-21"}
```

## 6. Score-return alignment

### 6.1 Export backlog winners

`012450`, `079550`, and `064350` show the constructive C03 family. These are not simple “defense theme” rows. The forward price paths imply the market was repricing export backlog, production visibility, delivery schedule, and margin conversion.

### 6.2 Aircraft delivery bridge is slower

`047810` shows why C03 should not transfer leader scores to every defense aerospace name. The MFE was modest and the entry drawdown was larger than the upside cushion. Aircraft export and delivery programs need specific delivery, cash collection, and margin bridge proof before promotion.

### 6.3 Same leader, different timing

The `012450` late-chase row is the guardrail. Same company, same broad defense-export story, but the late October entry had much worse asymmetry. C03 should therefore include a late-chase event-cap guard even for the strongest names.

## 7. Raw component score simulation

| symbol | export/framework evidence | delivery/backlog bridge | margin/FCF bridge | price confirmation | MAE/late-chase guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 012450 early | 24 | 22 | 18 | 25 | -3 | 86 | Stage3-Yellow/Green candidate |
| 079550 | 23 | 20 | 16 | 24 | -4 | 79 | Stage3-Yellow/Green candidate |
| 064350 | 21 | 18 | 14 | 22 | -4 | 71 | Stage3-Yellow candidate |
| 047810 | 17 | 9 | 7 | 5 | -7 | 31 | Stage2/Yellow with delivery guard |
| 012450 late | 24 | 8 | 6 | 4 | -13 | 29 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c03_defense_export_requires_delivery_margin_fcf_bridge","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_required_bridge","rule":"Do not promote defense export/framework/backlog labels above Stage2 unless firm contract, delivery schedule, production capacity, cost-to-complete, FX/working-capital control, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["047810","012450_late"],"counterbalanced_by":["012450_early","079550","064350"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_export_backlog_leader_positive_delta","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Defense exporters with visible delivery schedule, production capacity, backlog conversion, and margin/FCF bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["012450_early","079550","064350"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_aircraft_delivery_slow_conversion_guard","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_to_yellow_with_delivery_guard","rule":"Aircraft export/program names require stricter delivery and margin proof than land/missile leaders; modest MFE with meaningful MAE should stay Stage2/Yellow.","supporting_cases":["047810"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_defense_leader_late_chase_4b_guard","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"local_4b_watch_guard","rule":"If defense-export leader entry follows large price extension and lacks fresh delivery/margin evidence, cap at local 4B watch or event-cap even when the company is structurally strong.","supporting_cases":["012450_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","round":"R1","loop":"96","positive_rows":3,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C03 should distinguish true defense export backlog/delivery/margin conversion from slower aircraft delivery bridges and late-chase price-only extension in sector leaders.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_delivery_guard","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","sample_count":5,"avg_mfe_pct":74.27,"avg_mae_pct":-10.27,"median_mfe_pct":84.78,"median_mae_pct":-9.13,"interpretation":"C03 can generate very strong upside when export backlog converts into delivery and margin, but aircraft slow-delivery and late-chase entries require strict 4B/YELLOW guardrails."}
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
  1. c03_defense_export_requires_delivery_margin_fcf_bridge -> stage2_required_bridge
  2. c03_export_backlog_leader_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c03_aircraft_delivery_slow_conversion_guard -> stage2_to_yellow_with_delivery_guard
  4. c03_defense_leader_late_chase_4b_guard -> local_4b_watch_guard

Expected behavior:
- Defense export/backlog vocabulary alone should not create Green.
- Firm contract, delivery schedule, production capacity, cost-to-complete, FX/working-capital control, OPM, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Late-chase entries and slow aircraft delivery bridges should remain capped until fresh delivery/margin evidence appears.
```
