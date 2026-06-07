# E2R Stock-Web v12 Residual Research — R4 loop 98 / L4 / C17

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 98
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: SYNTHETIC_RUBBER_SPANDEX_PETROCHEM_ETHYLENE_NAPHTHA_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_HIGH_MAE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - commodity_spread_to_margin_bridge_test
  - feedstock_pass_through_guardrail
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

이번 파일은 `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` 전용 residual research다.

C17은 “화학 업황 반등”, “원재료 가격 하락”, “스프레드 개선”, “범용 화학 회복” 같은 headline을 곧바로 Stage3-Green으로 올리는 bucket이 아니다. 핵심은 원재료/제품 가격 차이가 실제 ASP, volume, 가동률, 재고평가, pass-through, OPM/FCF로 내려오는지다.

```text
chemical / commodity spread headline
  → product ASP and feedstock pass-through
  → utilization / inventory valuation / volume mix
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

화학 spread는 파이프의 압력차와 같다. 압력차가 생겨도 밸브가 막히면 공장 밖으로 현금이 흐르지 않는다. C17은 “가격 차이가 있다”와 “그 차이가 마진으로 남는다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["011780","298020","011170","006650"],"profile_paths":["atlas/symbol_profiles/011/011780.json","atlas/symbol_profiles/298/298020.json","atlas/symbol_profiles/011/011170.json","atlas/symbol_profiles/006/006650.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv","atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv"],"validation_scope":"2024 trigger-level forward path; selected corporate-action caveats are historical and outside the local 2024 windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C17 at 29 rows, only 1 row short of the 30-row minimum stability zone.
- Existing registry shows C17 parsed through `R4 loop 97`.
- This output uses `R4 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file shifts into synthetic rubber, spandex, petrochemical cracker, and ethylene/naphtha spread paths.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C17-R4L98-01 | 011780 | 금호석유화학 | 2024-04-29 | 2024-04-29 | 138300 | 167000 | 120700 | 20.75% | -12.73% | Synthetic rubber/phenol spread path produced MFE, but drawdown says margin bridge must be verified. |
| C17-R4L98-02 | 298020 | 효성티앤씨 | 2024-04-17 | 2024-04-17 | 340500 | 421500 | 267500 | 23.79% | -21.44% | Spandex spread recovery had real MFE, but high MAE blocks automatic Green. |
| C17-R4L98-03 | 011170 | 롯데케미칼 | 2024-04-29 | 2024-04-29 | 107700 | 125500 | 76500 | 16.53% | -28.97% | Petrochemical spread rebound label failed without durable feedstock/OPM bridge. |
| C17-R4L98-04 | 006650 | 대한유화 | 2024-04-11 | 2024-04-11 | 148000 | 161000 | 91500 | 8.78% | -38.18% | Ethylene/naphtha spread label produced weak MFE and severe MAE; hard counterexample candidate. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C17-R4L98-01","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_PHENOL_SPREAD_MARGIN_BRIDGE_HIGH_MAE","symbol":"011780","name":"금호석유화학","trigger_type":"synthetic_rubber_phenol_spread_margin_bridge_high_mae","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":138300,"peak_price":167000,"peak_date":"2024-07-15","trough_price":120700,"trough_date":"2024-08-05","mfe_pct":20.75,"mae_pct":-12.73,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_margin_bridge","residual_flag":"positive_spread_MFE_but_OPM_inventory_pass_through_bridge_required","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|synthetic_rubber_phenol_spread_margin_bridge_high_mae|2024-04-29"}
{"row_type":"trigger","case_id":"C17-R4L98-02","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_SPREAD_RECOVERY_HIGH_MAE_GUARD","symbol":"298020","name":"효성티앤씨","trigger_type":"spandex_spread_recovery_high_mae_guard","trigger_date":"2024-04-17","entry_date":"2024-04-17","entry_price":340500,"peak_price":421500,"peak_date":"2024-05-17","trough_price":267500,"trough_date":"2024-08-05","mfe_pct":23.79,"mae_pct":-21.44,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_high_MAE_guardrail","residual_flag":"spandex_spread_recovery_positive_but_drawdown_and_margin_durability_need_guard","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298020|spandex_spread_recovery_high_mae_guard|2024-04-17"}
{"row_type":"trigger","case_id":"C17-R4L98-03","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEM_CRACKER_SPREAD_REBOUND_FALSE_STAGE2","symbol":"011170","name":"롯데케미칼","trigger_type":"petrochem_cracker_spread_rebound_false_stage2","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":107700,"peak_price":125500,"peak_date":"2024-05-20","trough_price":76500,"trough_date":"2024-09-09","mfe_pct":16.53,"mae_pct":-28.97,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"generic_petrochemical_spread_label_decayed_without_OPM_FCF_bridge","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|petrochem_cracker_spread_rebound_false_stage2|2024-04-29"}
{"row_type":"trigger","case_id":"C17-R4L98-04","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"ETHYLENE_NAPHTHA_SPREAD_WEAK_MFE_HIGH_MAE_COUNTEREXAMPLE","symbol":"006650","name":"대한유화","trigger_type":"ethylene_naphtha_spread_weak_mfe_high_mae","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":148000,"peak_price":161000,"peak_date":"2024-05-20","trough_price":91500,"trough_date":"2024-09-10","mfe_pct":8.78,"mae_pct":-38.18,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4C_watch","residual_flag":"ethylene_naphtha_spread_label_failed_without_utilization_inventory_margin_bridge","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|006650|ethylene_naphtha_spread_weak_mfe_high_mae|2024-04-11"}
```

## 6. Score-return alignment

### 6.1 Specialty spread can work, but still needs proof

`011780` and `298020` show that C17 is not a blanket short bucket. Synthetic rubber, phenol, and spandex spread narratives can produce real MFE. But both rows also show meaningful drawdown after the first leg, so production scoring should require OPM, inventory, ASP, and feedstock pass-through confirmation before Green.

### 6.2 Generic petrochemical spread false positives

`011170` and `006650` are the warning family. Generic cracker or ethylene/naphtha spread recovery vocabulary can rally, but if utilization, inventory valuation, and FCF do not improve, the forward path becomes high-MAE. These rows should not be scored like specialty spread winners.

### 6.3 Mechanism

C17 should behave like a refinery valve. Product price and feedstock cost create pressure, but margin only appears when the valve is open: utilization, pass-through, volume mix, inventory valuation, and cash conversion all have to line up.

## 7. Raw component score simulation

| symbol | spread evidence | utilization/volume | feedstock/pass-through | OPM/FCF bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 011780 | 20 | 13 | 13 | 10 | 15 | -6 | 65 | Stage2/Yellow with bridge |
| 298020 | 21 | 12 | 12 | 9 | 17 | -10 | 61 | Stage2/Yellow with high-MAE guard |
| 011170 | 16 | 7 | 6 | 3 | 8 | -14 | 26 | Stage2/local 4B watch |
| 006650 | 14 | 5 | 4 | 2 | 3 | -18 | 10 | Hard counterexample / 4C watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c17_chemical_spread_requires_OPM_FCF_bridge","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"stage2_required_bridge","rule":"Do not promote chemical/commodity spread labels above Stage2 unless product ASP, utilization, volume mix, feedstock pass-through, inventory valuation, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["011170","006650"],"counterbalanced_by":["011780","298020"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c17_specialty_spread_positive_delta","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"stage3_yellow_candidate_delta","rule":"Specialty chemical spread names can receive Stage3-Yellow treatment when spread evidence is paired with utilization and OPM/FCF bridge, but Green requires drawdown containment.","supporting_cases":["011780","298020"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c17_petrochem_cracker_false_stage2_guard","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"local_4b_watch_guard","rule":"Generic petrochemical cracker or ethylene/naphtha spread labels should be capped at local 4B/event-cap when MFE is modest and later MAE dominates.","supporting_cases":["011170","006650"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c17_utilization_inventory_break_hard_counterexample","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"hard_4c_watch","rule":"If chemical spread vocabulary is followed by weak MFE, severe MAE, and no utilization/inventory/FCF repair, mark as hard counterexample or 4C watch.","supporting_cases":["006650"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","round":"R4","loop":"98","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C17 should separate specialty spread recovery with OPM/FCF bridge from generic petrochemical spread labels that decay under utilization and inventory pressure.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","local_4b_watch_guard","hard_4c_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","sample_count":4,"avg_mfe_pct":17.46,"avg_mae_pct":-25.33,"median_mfe_pct":18.64,"median_mae_pct":-25.20,"interpretation":"C17 spread labels can produce tradable MFE, but asymmetry is poor unless utilization, pass-through, OPM and FCF bridge are visible."}
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
  - selected profile corporate-action caveats are historical and outside the 2024 trigger windows
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C17 R4 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c17_chemical_spread_requires_OPM_FCF_bridge -> stage2_required_bridge
  2. c17_specialty_spread_positive_delta -> stage3_yellow_candidate_delta
  3. c17_petrochem_cracker_false_stage2_guard -> local_4b_watch_guard
  4. c17_utilization_inventory_break_hard_counterexample -> hard_4c_watch

Expected behavior:
- Chemical/commodity spread vocabulary alone should not create Green.
- Product ASP, utilization, volume mix, feedstock pass-through, inventory valuation, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Generic cracker and ethylene/naphtha rows with modest MFE and severe MAE should be capped or marked hard counterexample.
```
