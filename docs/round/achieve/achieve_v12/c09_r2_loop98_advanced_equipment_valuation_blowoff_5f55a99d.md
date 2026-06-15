# E2R Stock-Web v12 Residual Research — R2 loop 98 / L2 / C09

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 98
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_ALD_CVD_METROLOGY_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - advanced_equipment_valuation_guardrail
  - order_delivery_margin_bridge_test
  - late_chase_high_MAE_guardrail
  - equipment_label_false_stage2_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` 전용 residual research다.

C09는 “ALD/CVD”, “EUV/advanced equipment”, “metrology”, “vacuum/process equipment”, “HBM/AI capex 수혜”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 고급 장비 narrative가 실제 customer order, delivery acceptance, capacity ramp, backlog, gross margin, OPM/FCF/revision으로 내려오는지다.

```text
advanced equipment / valuation rerating headline
  → customer order / delivery schedule / acceptance
  → capacity ramp / backlog quality / utilization
  → gross margin / OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

고급 장비 valuation은 정밀 렌즈와 같다. 렌즈가 비싸 보여도, 실제 고객 라인에 들어가고 검사에 통과해 반복 주문과 마진을 만들 때만 현미경은 초점을 맞춘다. C09는 “정밀 장비 label”과 “수주·납품·마진 초점”을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["036930","140860","083310","240810"],"profile_paths":["atlas/symbol_profiles/036/036930.json","atlas/symbol_profiles/140/140860.json","atlas/symbol_profiles/083/083310.json","atlas/symbol_profiles/240/240810.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv","atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv","atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv"],"validation_scope":"2024 trigger-level forward path; 140860 and 240810 have zero corporate-action candidates; 036930 caveat is 2000; 083310 caveats are 2007, so selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C09 at 15 rows, 15 rows short of the 30-row minimum stability zone.
- Existing registry shows C09 parsed through `R2 loop 97`.
- This output uses `R2 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates ALD/CVD advanced equipment blowoff, advanced metrology quality premium, vacuum equipment false Stage2, large equipment order-bridge failure, and same-leader late-chase guardrail.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C09-R2L98-01 | 036930 | 주성엔지니어링 | 2024-02-28 | 2024-02-28 | 40000 | 41450 | 22150 | 3.63% | -44.63% | ALD/CVD advanced-equipment label blew off without durable order/margin bridge. |
| C09-R2L98-02 | 140860 | 파크시스템스 | 2024-08-08 | 2024-08-08 | 185500 | 219500 | 168800 | 18.33% | -9.00% | Advanced metrology quality premium was more resilient, but still requires order/revision proof. |
| C09-R2L98-03 | 083310 | 엘오티베큠 | 2024-02-22 | 2024-02-22 | 23350 | 24450 | 9880 | 4.71% | -57.69% | Vacuum/process-equipment label created only a short spike before hard MAE. |
| C09-R2L98-04 | 240810 | 원익IPS | 2024-03-29 | 2024-03-29 | 41500 | 44850 | 26950 | 8.07% | -35.06% | Large semi-equipment rebound failed without clear order/delivery/OPM bridge. |
| C09-R2L98-05 | 036930 | 주성엔지니어링 | 2024-06-28 | 2024-06-28 | 37350 | 39050 | 22150 | 4.55% | -40.70% | Same advanced-equipment leader late-chase after extension became local 4B/event-cap. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C09-R2L98-01","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ALD_CVD_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_NO_ORDER_MARGIN_BRIDGE","symbol":"036930","name":"주성엔지니어링","trigger_type":"ald_cvd_advanced_equipment_valuation_blowoff_no_order_margin_bridge","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":40000,"peak_price":41450,"peak_date":"2024-04-08","trough_price":22150,"trough_date":"2024-08-05","mfe_pct":3.63,"mae_pct":-44.63,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"advanced_equipment_label_spike_failed_without_customer_order_OPM_bridge","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|036930|ald_cvd_advanced_equipment_valuation_blowoff_no_order_margin_bridge|2024-02-28"}
{"row_type":"trigger","case_id":"C09-R2L98-02","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_METROLOGY_QUALITY_PREMIUM_ORDER_REVISION_BRIDGE","symbol":"140860","name":"파크시스템스","trigger_type":"advanced_metrology_quality_premium_order_revision_bridge","trigger_date":"2024-08-08","entry_date":"2024-08-08","entry_price":185500,"peak_price":219500,"peak_date":"2024-10-24","trough_price":168800,"trough_date":"2024-09-05","mfe_pct":18.33,"mae_pct":-9.00,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_order_margin_URLs","residual_flag":"metrology_quality_premium_more_resilient_but_needs_order_OPM_revision_bridge","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|140860|advanced_metrology_quality_premium_order_revision_bridge|2024-08-08"}
{"row_type":"trigger","case_id":"C09-R2L98-03","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"VACUUM_PROCESS_EQUIPMENT_LABEL_FALSE_STAGE2_HIGH_MAE","symbol":"083310","name":"엘오티베큠","trigger_type":"vacuum_process_equipment_label_false_stage2_high_mae","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":23350,"peak_price":24450,"peak_date":"2024-02-23","trough_price":9880,"trough_date":"2024-08-05","mfe_pct":4.71,"mae_pct":-57.69,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"vacuum_equipment_label_tiny_MFE_high_MAE_without_delivery_margin_bridge","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|083310|vacuum_process_equipment_label_false_stage2_high_mae|2024-02-22"}
{"row_type":"trigger","case_id":"C09-R2L98-04","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LARGE_SEMI_EQUIPMENT_REBOUND_ORDER_BRIDGE_FAILURE","symbol":"240810","name":"원익IPS","trigger_type":"large_semi_equipment_rebound_order_bridge_failure","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":41500,"peak_price":44850,"peak_date":"2024-04-08","trough_price":26950,"trough_date":"2024-10-25","mfe_pct":8.07,"mae_pct":-35.06,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"large_equipment_rebound_failed_without_order_delivery_OPM_bridge","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|240810|large_semi_equipment_rebound_order_bridge_failure|2024-03-29"}
{"row_type":"trigger","case_id":"C09-R2L98-05","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"036930","name":"주성엔지니어링","trigger_type":"advanced_equipment_leader_late_chase_price_only_extension_4b","trigger_date":"2024-06-28","entry_date":"2024-06-28","entry_price":37350,"peak_price":39050,"peak_date":"2024-06-28","trough_price":22150,"trough_date":"2024-08-05","mfe_pct":4.55,"mae_pct":-40.70,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_leader_late_chase_without_fresh_order_margin_evidence","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|036930|advanced_equipment_leader_late_chase_price_only_extension_4b|2024-06-28"}
```

## 6. Score-return alignment

### 6.1 Valuation blowoff false positives

`036930`, `083310`, and `240810` are the core warning family. Each had advanced-equipment vocabulary and at least a short-lived spike, but the forward path opened deep MAE. C09 should treat these as valuation blowoff / false Stage2 unless customer order, delivery acceptance, and OPM/FCF bridge are visible.

### 6.2 Quality premium can be Yellow, not automatic Green

`140860` behaves differently. The drawdown was materially more controlled than the generic equipment rows, and MFE was larger than the initial MAE. Still, the scorer should not promote pure metrology quality premium to Green without exact order/revision and margin evidence.

### 6.3 Same leader, different timing

The `036930` late-chase row shows that even an advanced-equipment leader can become a bad C09 entry when the trigger is mostly price extension. C09 therefore needs a late-chase cap that is separate from company quality.

## 7. Raw component score simulation

| symbol | equipment specificity | order/delivery bridge | margin/revision bridge | price confirmation | MAE/late-chase guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 036930 early | 21 | 5 | 4 | 2 | -21 | 11 | Hard counterexample/local 4B |
| 140860 | 22 | 13 | 12 | 13 | -5 | 55 | Stage3-Yellow candidate |
| 083310 | 15 | 3 | 2 | 1 | -25 | -4 | Hard 4C watch |
| 240810 | 18 | 6 | 5 | 4 | -15 | 18 | Stage2/local 4B |
| 036930 late | 21 | 4 | 3 | 1 | -20 | 9 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c09_advanced_equipment_requires_order_delivery_margin_bridge","scope":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","candidate_action":"stage2_required_bridge","rule":"Do not promote advanced semi equipment labels above Stage2 unless customer order, delivery schedule, acceptance, backlog quality, capacity ramp, gross margin, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["036930_early","083310","240810","036930_late"],"counterbalanced_by":["140860"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c09_metrology_quality_yellow_delta","scope":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","candidate_action":"stage3_yellow_candidate_delta","rule":"Advanced metrology or high-quality equipment names can receive Stage3-Yellow treatment when price confirmation is paired with order/revision and margin evidence; Green requires stronger URL-verified bridge.","supporting_cases":["140860"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c09_equipment_label_high_mae_guardrail","scope":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","candidate_action":"hard_4c_watch_or_local_4b","rule":"Advanced equipment labels with tiny MFE and deep MAE should be marked local 4B or hard 4C watch until order, delivery and OPM evidence repairs the row.","supporting_cases":["036930_early","083310","240810"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c09_late_chase_price_only_extension_guard","scope":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","candidate_action":"local_4b_watch_guard","rule":"If an advanced-equipment entry follows a price extension and lacks fresh order/margin evidence, cap at local 4B or event-cap even for sector leaders.","supporting_cases":["036930_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","round":"R2","loop":"98","positive_rows":1,"counterexample_rows":4,"new_symbol_count":4,"primary_residual":"C09 should separate high-quality metrology equipment with controlled drawdown from generic advanced-equipment valuation blowoff where order/delivery/margin bridge is absent and MAE dominates.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","hard_4c_watch_or_local_4b","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sample_count":5,"avg_mfe_pct":7.86,"avg_mae_pct":-37.42,"median_mfe_pct":4.71,"median_mae_pct":-40.70,"interpretation":"C09 advanced-equipment vocabulary shows poor asymmetry unless order, delivery acceptance, OPM and FCF bridge are visible; quality metrology can be Yellow but not automatic Green."}
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
- Ingest this C09 R2 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c09_advanced_equipment_requires_order_delivery_margin_bridge -> stage2_required_bridge
  2. c09_metrology_quality_yellow_delta -> stage3_yellow_candidate_delta
  3. c09_equipment_label_high_mae_guardrail -> hard_4c_watch_or_local_4b
  4. c09_late_chase_price_only_extension_guard -> local_4b_watch_guard

Expected behavior:
- Advanced semi equipment vocabulary alone should not create Green.
- Customer order, delivery schedule, acceptance, backlog quality, capacity ramp, gross margin, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Valuation blowoff and late-chase rows should be capped when MFE is tiny and MAE dominates.
```
