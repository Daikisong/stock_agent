# E2R Stock-Web v12 Residual Research — R2 loop 97 / L2 / C08

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 97
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_CONSUMABLE_REPEAT_DEMAND_MARGIN_BRIDGE_VS_SOCKET_LABEL_PRICE_SPIKE_AND_SMALLCAP_DECAY
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - customer_qualification_consumable_reorder_bridge_test
  - socket_probe_card_margin_bridge_guardrail
  - late_chase_high_MAE_guardrail
  - smallcap_socket_false_stage2_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY` 전용 residual research다.

C08은 “테스트소켓”, “프로브카드”, “HBM test”, “고객 qualification”, “반도체 소모품”이라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 고객 qualification이 실제 양산 적용, 반복 소모품/reorder, ASP/mix, gross margin, OPM/FCF/revision으로 내려오는지다.

```text
semi test socket / probe-card / customer quality headline
  → customer qualification / design-in / mass-production adoption
  → consumable repeat demand / reorder / utilization
  → ASP or mix uplift / gross margin / OPM / FCF bridge
  → stock-web 1D OHLC forward path
```

테스트소켓은 반도체 공정의 검사 장갑과 같다. 장갑을 낀다는 소식은 시작일 뿐이고, 진짜 돈은 고객 라인에서 계속 닳고 다시 주문되는 순간에 생긴다. C08은 “테스트 label”과 “반복 소모품 매출”을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["058470","095340","131290","098120"],"profile_paths":["atlas/symbol_profiles/058/058470.json","atlas/symbol_profiles/095/095340.json","atlas/symbol_profiles/131/131290.json","atlas/symbol_profiles/098/098120.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv"],"validation_scope":"2024 trigger-level forward path; 058470 caveats are 2013 and 2025-04-25 so selected 2024 window is before the 2025 caveat; 095340 caveats are 2014 and 2023-10-20 and outside selected 2024 windows; 131290 and 098120 caveats are 2011 and outside selected 2024 windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C08 at 14 rows, 16 rows short of the 30-row minimum stability zone.
- Existing registry shows C08 parsed through `R2 loop 96`.
- This output uses `R2 loop 97`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates high-quality probe/socket installed-base rerating, socket label false Stage2, probe-card high-MAE bridge, and smallcap socket decay.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C08-R2L97-01 | 058470 | 리노공업 | 2024-03-08 | 2024-03-08 | 215500 | 309000 | 200500 | 43.39% | -6.96% | High-quality probe/socket customer-quality path worked with controlled early MAE. |
| C08-R2L97-02 | 095340 | ISC | 2024-03-08 | 2024-03-08 | 95000 | 108000 | 41100 | 13.68% | -56.74% | Socket/HBM-test label produced MFE but collapsed without durable reorder/margin bridge. |
| C08-R2L97-03 | 131290 | 티에스이 | 2024-04-24 | 2024-04-24 | 64200 | 87800 | 38050 | 36.76% | -40.73% | Probe-card/test customer-quality optionality worked briefly, but high MAE blocks Green. |
| C08-R2L97-04 | 098120 | 마이크로컨텍솔 | 2024-04-26 | 2024-04-26 | 10700 | 11130 | 4965 | 4.02% | -53.60% | Smallcap socket label had tiny MFE and severe decay; hard false Stage2 guard. |
| C08-R2L97-05 | 058470 | 리노공업 | 2024-05-07 | 2024-05-07 | 298000 | 309000 | 164000 | 3.69% | -44.97% | Same quality leader but late-chase after extension became high-MAE 4B/event-cap. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C08-R2L97-01","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HIGH_QUALITY_PROBE_SOCKET_CUSTOMER_QUALIFICATION_CONSUMABLE_MARGIN_BRIDGE","symbol":"058470","name":"리노공업","trigger_type":"high_quality_probe_socket_customer_qualification_consumable_margin_bridge","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":215500,"peak_price":309000,"peak_date":"2024-05-07","trough_price":200500,"trough_date":"2024-03-11","mfe_pct":43.39,"mae_pct":-6.96,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_customer_reorder_margin_URLs","residual_flag":"positive_quality_socket_probe_path_but_requires_exact_customer_reorder_OPM_URLs","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|058470|high_quality_probe_socket_customer_qualification_consumable_margin_bridge|2024-03-08"}
{"row_type":"trigger","case_id":"C08-R2L97-02","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SOCKET_HBM_TEST_LABEL_FALSE_STAGE2_WITHOUT_REORDER_MARGIN","symbol":"095340","name":"ISC","trigger_type":"socket_hbm_test_label_false_stage2_without_reorder_margin","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":95000,"peak_price":108000,"peak_date":"2024-03-28","trough_price":41100,"trough_date":"2024-08-05","mfe_pct":13.68,"mae_pct":-56.74,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"socket_label_MFE_failed_without_durable_customer_reorder_margin_bridge","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|095340|socket_hbm_test_label_false_stage2_without_reorder_margin|2024-03-08"}
{"row_type":"trigger","case_id":"C08-R2L97-03","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_TEST_CUSTOMER_QUALITY_OPTIONALITY_HIGH_MAE_GUARD","symbol":"131290","name":"티에스이","trigger_type":"probe_card_test_customer_quality_optionality_high_mae_guard","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":64200,"peak_price":87800,"peak_date":"2024-05-03","trough_price":38050,"trough_date":"2024-08-05","mfe_pct":36.76,"mae_pct":-40.73,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"probe_card_optional_MFE_but_customer_qualification_and_OPM_bridge_required","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|131290|probe_card_test_customer_quality_optionality_high_mae_guard|2024-04-24"}
{"row_type":"trigger","case_id":"C08-R2L97-04","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SMALLCAP_SOCKET_CUSTOMER_QUALITY_LABEL_TINY_MFE_DECAY","symbol":"098120","name":"마이크로컨텍솔","trigger_type":"smallcap_socket_customer_quality_label_tiny_mfe_decay","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":10700,"peak_price":11130,"peak_date":"2024-04-29","trough_price":4965,"trough_date":"2024-09-09","mfe_pct":4.02,"mae_pct":-53.60,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"smallcap_socket_label_tiny_MFE_high_MAE_without_customer_reorder_bridge","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|098120|smallcap_socket_customer_quality_label_tiny_mfe_decay|2024-04-26"}
{"row_type":"trigger","case_id":"C08-R2L97-05","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"QUALITY_SOCKET_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"058470","name":"리노공업","trigger_type":"quality_socket_leader_late_chase_price_only_extension_4b","trigger_date":"2024-05-07","entry_date":"2024-05-07","entry_price":298000,"peak_price":309000,"peak_date":"2024-05-07","trough_price":164000,"trough_date":"2024-08-05","mfe_pct":3.69,"mae_pct":-44.97,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_quality_leader_late_chase_without_fresh_customer_reorder_evidence","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|058470|quality_socket_leader_late_chase_price_only_extension_4b|2024-05-07"}
```

## 6. Score-return alignment

### 6.1 Quality socket/probe winner

`058470` early is the constructive C08 family. The path had strong MFE and contained initial MAE. It supports a stronger Stage3-Yellow/Green candidate treatment only when customer qualification, mass-production adoption, consumable repeat orders, ASP/mix, and OPM evidence are verified.

### 6.2 Socket/probe-card label is not enough

`095340`, `131290`, and `098120` show the false-positive family. Each had plausible test socket/probe-card vocabulary, but the forward path showed either small MFE or deep drawdown. C08 should not treat “socket/test” as a direct HBM winner unless repeat demand and margin conversion are visible.

### 6.3 Same leader, different timing

The `058470` late-chase row is the timing guard. The same high-quality company became a poor risk/reward entry after price extension. This argues for a local 4B/event-cap rule when the entry follows a large run and lacks fresh customer/reorder evidence.

## 7. Raw component score simulation

| symbol | customer qualification | consumable/reorder | ASP/mix bridge | OPM/FCF bridge | price confirmation | MAE/late-chase guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 058470 early | 23 | 21 | 17 | 19 | 20 | -3 | 82 | Stage3-Yellow/Green candidate |
| 095340 | 17 | 7 | 6 | 4 | 5 | -23 | 16 | Hard counterexample / local 4B |
| 131290 | 18 | 10 | 8 | 6 | 15 | -17 | 40 | Stage2/Yellow with high-MAE guard |
| 098120 | 10 | 4 | 3 | 2 | 1 | -24 | -4 | Hard counterexample / 4C watch |
| 058470 late | 23 | 7 | 5 | 4 | 2 | -19 | 22 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c08_socket_requires_customer_qualification_reorder_margin_bridge","scope":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","candidate_action":"stage2_required_bridge","rule":"Do not promote semi test socket/probe-card labels above Stage2 unless customer qualification, design-in, mass-production adoption, consumable reorder, utilization, ASP/mix, gross margin, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["095340","131290","098120","058470_late"],"counterbalanced_by":["058470_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c08_quality_probe_socket_positive_delta","scope":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"High-quality probe/socket names with verified customer qualification, repeat consumable demand, and OPM/revision bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["058470_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c08_smallcap_socket_false_stage2_guard","scope":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","candidate_action":"hard_4c_watch","rule":"Smallcap socket labels with tiny MFE and severe MAE should be hard counterexamples unless customer qualification and reorder evidence repairs the row.","supporting_cases":["098120"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c08_late_chase_quality_leader_4b_guard","scope":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","candidate_action":"local_4b_watch_guard","rule":"Even quality socket/probe leaders should be capped at local 4B/event-cap when entry follows a large price extension and lacks fresh customer/reorder evidence.","supporting_cases":["058470_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","round":"R2","loop":"97","positive_rows":1,"counterexample_rows":4,"new_symbol_count":4,"primary_residual":"C08 should separate genuine customer-qualified repeat-consumable probe/socket winners from socket/probe-card labels, smallcap event spikes, and late-chase entries without fresh reorder/margin evidence.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","hard_4c_watch","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","sample_count":5,"avg_mfe_pct":20.31,"avg_mae_pct":-40.60,"median_mfe_pct":13.68,"median_mae_pct":-44.97,"interpretation":"C08 upside is concentrated in verified high-quality repeat-consumable models; generic socket/test labels and late-chase entries often decay into high-MAE false Stage2 paths."}
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
- Ingest this C08 R2 loop 97 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c08_socket_requires_customer_qualification_reorder_margin_bridge -> stage2_required_bridge
  2. c08_quality_probe_socket_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c08_smallcap_socket_false_stage2_guard -> hard_4c_watch
  4. c08_late_chase_quality_leader_4b_guard -> local_4b_watch_guard

Expected behavior:
- Test socket/probe-card vocabulary alone should not create Green.
- Customer qualification, design-in, mass-production adoption, consumable reorder, ASP/mix, OPM, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Smallcap socket labels and late-chase entries should be capped when MFE is small or MAE dominates.
```
