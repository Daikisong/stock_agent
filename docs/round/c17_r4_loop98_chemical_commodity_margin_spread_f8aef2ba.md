# E2R Stock-Web v12 Residual Research — R4 loop 98 / L4 / C17

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 98
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: NAPHTHA_ETHYLENE_SYNTHETIC_RUBBER_SPANDEX_PP_FEEDSTOCK_SPREAD_MARGIN_FCF_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_AND_LATE_CHASE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - commodity_spread_bridge_test
  - petrochem_feedstock_false_stage2_guard
  - synthetic_rubber_positive_delta_with_sizing_guard
  - spandex_PP_capacity_false_stage2_guard
  - chemical_late_chase_local_4B_guard
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

C17은 “원재료 하락”, “유가 안정”, “스프레드 개선”, “중국 경기 회복”, “화학 업황 바닥”이라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 feedstock과 제품 가격의 spread가 실제 ASP, volume, utilization, inventory valuation, working capital, OPM, FCF, EPS revision으로 내려오는지다.

```text
chemical commodity / feedstock spread headline
  → naphtha, ethylene, propylene, BD, PX, spandex, PP spread
  → volume / utilization / inventory valuation / cost pass-through
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

화학 spread는 공장의 밸브 압력과 같다. 압력이 올라간다고 탱크에 현금이 차지는 않는다. 실제 제품가가 버티고, 원료비가 새지 않고, 재고평가와 가동률이 맞물릴 때만 마진이 관을 타고 흐른다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["011170","011780","298020","298000"],"profile_paths":["atlas/symbol_profiles/011/011170.json","atlas/symbol_profiles/011/011780.json","atlas/symbol_profiles/298/298020.json","atlas/symbol_profiles/298/298000.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","atlas/ohlcv_tradable_by_symbol_year/298/298020/2024.csv","atlas/ohlcv_tradable_by_symbol_year/298/298000/2024.csv"],"validation_scope":"2024 trigger-level forward path; 011170 caveat is 2023-02-13, 011780 caveat is 2001-01-16, 298020 and 298000 have zero corporate-action candidates. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C17 at 29 rows, 1 row short of the 30-row minimum stability zone.
- Existing registry shows C17 parsed through `R4 loop 97`.
- This output uses `R4 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C17 loop 94/97 emphasized silicone/paint/chlor-alkali/semiconductor chemical/polysilicon/gas families. This file shifts to naphtha/ethylene petrochemical feedstock, synthetic rubber, spandex, PP/PDH and late-chase timing risk.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C17-R4L98-01 | 011780 | 금호석유화학 | 2024-01-29 | 2024-01-29 | 125400 | 163900 | 115200 | 30.70% | -8.13% | Synthetic rubber/BD spread rebound path worked, but needs ASP/volume/OPM evidence. |
| C17-R4L98-02 | 011170 | 롯데케미칼 | 2024-01-24 | 2024-01-24 | 128700 | 140800 | 76500 | 9.40% | -40.56% | Naphtha/ethylene petrochemical rebound label failed without spread and FCF conversion. |
| C17-R4L98-03 | 298020 | 효성티앤씨 | 2024-03-28 | 2024-03-28 | 308500 | 341000 | 265000 | 10.53% | -14.10% | Spandex spread recovery was tradable but not enough for Green without utilization/margin bridge. |
| C17-R4L98-04 | 298000 | 효성화학 | 2024-01-25 | 2024-01-25 | 71700 | 79900 | 39400 | 11.44% | -45.05% | PP/PDH feedstock spread label became hard high-MAE false Stage2. |
| C17-R4L98-05 | 011780 | 금호석유화학 | 2024-09-27 | 2024-09-27 | 158100 | 162300 | 132600 | 2.66% | -16.13% | Same synthetic-rubber quality row, late-chase after price extension became local 4B guard. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C17-R4L98-01","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_BD_SPREAD_MARGIN_BRIDGE_POSITIVE_WITH_SIZING_GUARD","symbol":"011780","name":"금호석유화학","trigger_type":"synthetic_rubber_bd_spread_margin_bridge_positive_with_sizing_guard","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":125400,"peak_price":163900,"peak_date":"2024-02-19","trough_price":115200,"trough_date":"2024-01-29","mfe_pct":30.70,"mae_pct":-8.13,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_BD_spread_OPM_FCF_URLs","residual_flag":"synthetic_rubber_spread_rebound_worked_but_requires_volume_ASP_OPM_FCF_bridge","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|synthetic_rubber_bd_spread_margin_bridge_positive_with_sizing_guard|2024-01-29"}
{"row_type":"trigger","case_id":"C17-R4L98-02","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NAPHTHA_ETHYLENE_PETROCHEM_SPREAD_FALSE_STAGE2_HIGH_MAE","symbol":"011170","name":"롯데케미칼","trigger_type":"naphtha_ethylene_petrochem_spread_false_stage2_high_mae","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":128700,"peak_price":140800,"peak_date":"2024-02-01","trough_price":76500,"trough_date":"2024-09-09","mfe_pct":9.40,"mae_pct":-40.56,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"petrochem_rebound_label_failed_without_ethylene_spread_inventory_FCF_bridge","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|naphtha_ethylene_petrochem_spread_false_stage2_high_mae|2024-01-24"}
{"row_type":"trigger","case_id":"C17-R4L98-03","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_SPREAD_RECOVERY_WITH_UTILIZATION_MARGIN_GUARD","symbol":"298020","name":"효성티앤씨","trigger_type":"spandex_spread_recovery_with_utilization_margin_guard","trigger_date":"2024-03-28","entry_date":"2024-03-28","entry_price":308500,"peak_price":341000,"peak_date":"2024-07-23","trough_price":265000,"trough_date":"2024-09-20","mfe_pct":10.53,"mae_pct":-14.10,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_utilization_margin_guard","residual_flag":"spandex_recovery_tradable_but_needs_utilization_ASP_OPM_FCF_bridge","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298020|spandex_spread_recovery_with_utilization_margin_guard|2024-03-28"}
{"row_type":"trigger","case_id":"C17-R4L98-04","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PP_PDH_FEEDSTOCK_SPREAD_FALSE_STAGE2_HIGH_MAE","symbol":"298000","name":"효성화학","trigger_type":"pp_pdh_feedstock_spread_false_stage2_high_mae","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":71700,"peak_price":79900,"peak_date":"2024-02-19","trough_price":39400,"trough_date":"2024-10-22","mfe_pct":11.44,"mae_pct":-45.05,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"PP_PDH_spread_label_failed_without_feedstock_pass_through_OPM_FCF_bridge","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298000|pp_pdh_feedstock_spread_false_stage2_high_mae|2024-01-25"}
{"row_type":"trigger","case_id":"C17-R4L98-05","round":"R4","loop":"98","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"011780","name":"금호석유화학","trigger_type":"synthetic_rubber_late_chase_price_only_extension_4b","trigger_date":"2024-09-27","entry_date":"2024-09-27","entry_price":158100,"peak_price":162300,"peak_date":"2024-09-30","trough_price":132600,"trough_date":"2024-10-22","mfe_pct":2.66,"mae_pct":-16.13,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_synthetic_rubber_story_late_chase_without_fresh_spread_margin_evidence","dedupe_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|synthetic_rubber_late_chase_price_only_extension_4b|2024-09-27"}
```

## 6. Score-return alignment

### 6.1 Synthetic rubber can work when spread is credible

`011780` early is the constructive C17 row. The path had meaningful MFE with contained entry-day MAE. This supports treating synthetic rubber/BD spread improvement as a Stage3-Yellow candidate, but only after product spread, volume, utilization, inventory and OPM/FCF evidence is visible.

### 6.2 Commodity petrochem labels are often false Stage2

`011170` and `298000` are the warning rows. Both had plausible commodity-chemical recovery vocabulary, but the forward paths opened deep MAE. In C17, a spread headline should not override weak utilization, inventory valuation, overcapacity, feedstock pass-through and FCF pressure.

### 6.3 Middle recovery and timing guard

`298020` is a middle row: spandex recovery was tradable but not durable enough for Green without margin conversion. The `011780` late-chase row shows that even a better chemical spread family can become poor risk/reward when entry follows price extension and lacks fresh spread/margin evidence.

## 7. Raw component score simulation

| symbol | spread evidence | utilization/volume | inventory/cost pass-through | OPM/FCF bridge | price confirmation | MAE/timing guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 011780 early | 21 | 16 | 14 | 13 | 18 | -4 | 68 | Stage3-Yellow candidate |
| 011170 | 17 | 5 | 4 | 3 | 5 | -18 | 16 | Hard counterexample/local 4B |
| 298020 | 18 | 10 | 9 | 7 | 8 | -7 | 45 | Stage2→Yellow with guard |
| 298000 | 16 | 4 | 3 | 2 | 5 | -20 | 10 | Hard counterexample / 4C watch |
| 011780 late | 21 | 6 | 5 | 4 | 1 | -12 | 25 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c17_chemical_spread_requires_utilization_inventory_OPM_FCF_bridge","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"stage2_required_bridge","rule":"Do not promote chemical commodity/spread labels above Stage2 unless product spread, volume, utilization, inventory valuation, cost pass-through, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["011170","298000","011780_late"],"counterbalanced_by":["011780_early","298020"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c17_synthetic_rubber_positive_delta","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"stage3_yellow_candidate_delta","rule":"Synthetic rubber/BD spread rows can receive Yellow treatment when spread, volume, utilization and OPM/FCF evidence is URL-verified.","supporting_cases":["011780_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c17_petrochem_feedstock_false_stage2_guard","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"hard_counterexample_or_local_4b","rule":"Naphtha/ethylene or PP/PDH petrochemical rebound rows with small MFE and deep MAE should remain local 4B or hard counterexample until feedstock pass-through and FCF evidence repairs the row.","supporting_cases":["011170","298000"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c17_spandex_recovery_yellow_with_margin_guard","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"stage2_to_yellow_with_utilization_margin_guard","rule":"Spandex recovery can be Yellow only when utilization, ASP/mix, inventory and OPM bridge are visible; moderate MAE blocks Green.","supporting_cases":["298020"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c17_chemical_late_chase_4b_guard","scope":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","candidate_action":"local_4b_watch_guard","rule":"If chemical spread entry follows a price extension and lacks fresh spread/margin evidence, cap at local 4B or event-cap even for better chemical quality rows.","supporting_cases":["011780_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","round":"R4","loop":"98","positive_rows":1,"counterexample_rows":4,"new_symbol_count":4,"primary_residual":"C17 should separate true synthetic-rubber spread improvement from generic petrochemical/feedstock recovery labels, spandex partial recovery, and late-chase price-only extension without OPM/FCF bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","hard_counterexample_or_local_4b","stage2_to_yellow_with_utilization_margin_guard","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","sample_count":5,"avg_mfe_pct":12.95,"avg_mae_pct":-25.19,"median_mfe_pct":10.53,"median_mae_pct":-16.13,"interpretation":"C17 commodity-chemical labels show poor asymmetry unless spread improvement closes into volume, utilization, inventory normalization, OPM and FCF; synthetic rubber can work, but petrochem feedstock and PP/PDH labels need strict guardrails."}
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
- Ingest this C17 R4 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c17_chemical_spread_requires_utilization_inventory_OPM_FCF_bridge -> stage2_required_bridge
  2. c17_synthetic_rubber_positive_delta -> stage3_yellow_candidate_delta
  3. c17_petrochem_feedstock_false_stage2_guard -> hard_counterexample_or_local_4b
  4. c17_spandex_recovery_yellow_with_margin_guard -> stage2_to_yellow_with_utilization_margin_guard
  5. c17_chemical_late_chase_4b_guard -> local_4b_watch_guard

Expected behavior:
- Chemical commodity/spread vocabulary alone should not create Green.
- Product spread, volume, utilization, inventory valuation, cost pass-through, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Petrochemical feedstock, PP/PDH and late-chase rows should remain capped until fresh non-price evidence repairs the row.
```
