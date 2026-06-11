# E2R Stock-Web v12 Residual Research — R2 loop 96 / L2 / C07

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 96
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TC_BONDER_TEST_HANDLER_REFLOW_LASER_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE_4B
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - HBM_equipment_order_revision_bridge_test
  - late_chase_high_MAE_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` 전용 residual research다.

C07은 “HBM 장비”, “TC bonder”, “test handler”, “laser”, “reflow” 같은 label을 그대로 Green으로 올리는 bucket이 아니다. C07의 핵심은 장비 상대강도가 실제 고객 order, delivery schedule, capacity ramp, OPM/revision으로 이어지는지다.

```text
HBM equipment relative strength
  → customer order / design-in / capacity ramp
  → shipment and delivery schedule
  → margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

HBM 장비 상대강도는 기계실의 회전음과 같다. 소리가 커졌다고 모두 매출이 되는 것은 아니다. 실제로 order가 들어오고, 납품이 되고, margin이 남을 때만 모터가 바퀴를 굴린다. 이번 파일은 그 회전음과 실제 추진력을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["042700","089030","031980","039030"],"profile_paths":["atlas/symbol_profiles/042/042700.json","atlas/symbol_profiles/089/089030.json","atlas/symbol_profiles/031/031980.json","atlas/symbol_profiles/039/039030.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats are outside local 2024 windows and are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C07 at 18 rows, 12 rows short of the 30-row minimum stability zone.
- Existing registry shows C07 parsed through `R2 loop 95`.
- This output uses `R2 loop 96`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file compresses TC-bonder leader, test-handler leader, reflow/packaging equipment, laser equipment, and late-chase high-MAE cases.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C07-R2L96-01 | 042700 | 한미반도체 | 2024-02-08 | 2024-02-08 | 78500 | 196200 | 60400 | 150.00% | -23.06% | TC-bonder/HBM order-relative-strength positive path, but early volatility requires sizing guard. |
| C07-R2L96-02 | 089030 | 테크윙 | 2024-05-20 | 2024-05-20 | 41000 | 70800 | 35600 | 72.68% | -13.17% | Test-handler/HBM order bridge positive path with better controlled MAE than theme spikes. |
| C07-R2L96-03 | 031980 | 피에스케이홀딩스 | 2024-05-20 | 2024-05-20 | 55800 | 85300 | 36900 | 52.87% | -33.87% | Reflow/packaging equipment MFE existed, but high MAE says margin/revision bridge must be verified. |
| C07-R2L96-04 | 039030 | 이오테크닉스 | 2024-04-04 | 2024-04-04 | 259000 | 281000 | 91200 | 8.49% | -64.79% | Laser/HBM equipment label late-stage blowoff without durable order bridge; hard 4B/4C watch. |
| C07-R2L96-05 | 042700 | 한미반도체 | 2024-06-13 | 2024-06-13 | 189000 | 196200 | 91300 | 3.81% | -51.69% | Same leader, different timing: late chase after extension produced small MFE and severe MAE. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C07-R2L96-01","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"TC_BONDER_HBM_ORDER_RELATIVE_STRENGTH_POSITIVE_HIGH_MAE","symbol":"042700","name":"한미반도체","trigger_type":"tc_bonder_hbm_order_relative_strength_positive_high_mae","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":78500,"peak_price":196200,"peak_date":"2024-06-14","trough_price":60400,"trough_date":"2024-02-08","mfe_pct":150.00,"mae_pct":-23.06,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_with_sizing_guard","residual_flag":"strong_positive_but_requires_order_delivery_margin_URLs_and_drawdown_guard","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|tc_bonder_hbm_order_relative_strength_positive_high_mae|2024-02-08"}
{"row_type":"trigger","case_id":"C07-R2L96-02","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_ORDER_DELIVERY_REVISION_BRIDGE","symbol":"089030","name":"테크윙","trigger_type":"hbm_test_handler_order_delivery_revision_bridge","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":41000,"peak_price":70800,"peak_date":"2024-07-11","trough_price":35600,"trough_date":"2024-05-20","mfe_pct":72.68,"mae_pct":-13.17,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_order_URLs","residual_flag":"positive_test_handler_bridge_but_customer_order_revenue_URLs_required","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|hbm_test_handler_order_delivery_revision_bridge|2024-05-20"}
{"row_type":"trigger","case_id":"C07-R2L96-03","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"REFLOW_PACKAGING_EQUIPMENT_ORDER_STRENGTH_HIGH_MAE_GUARD","symbol":"031980","name":"피에스케이홀딩스","trigger_type":"reflow_packaging_equipment_order_strength_high_mae_guard","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":55800,"peak_price":85300,"peak_date":"2024-06-19","trough_price":36900,"trough_date":"2024-09-09","mfe_pct":52.87,"mae_pct":-33.87,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_high_MAE_guardrail","residual_flag":"positive_MFE_but_margin_revision_bridge_and_MAE_guard_required","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|reflow_packaging_equipment_order_strength_high_mae_guard|2024-05-20"}
{"row_type":"trigger","case_id":"C07-R2L96-04","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"LASER_HBM_EQUIPMENT_LABEL_LATE_STAGE_BLOWOFF_HARD_4B_4C","symbol":"039030","name":"이오테크닉스","trigger_type":"laser_hbm_equipment_label_late_stage_blowoff_hard_4b_4c","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":259000,"peak_price":281000,"peak_date":"2024-04-12","trough_price":91200,"trough_date":"2024-10-29","mfe_pct":8.49,"mae_pct":-64.79,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_4B_or_4C_watch_not_Green","residual_flag":"counterexample_equipment_label_without_fresh_order_margin_bridge","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039030|laser_hbm_equipment_label_late_stage_blowoff_hard_4b_4c|2024-04-04"}
{"row_type":"trigger","case_id":"C07-R2L96-05","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"TC_BONDER_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"042700","name":"한미반도체","trigger_type":"tc_bonder_leader_late_chase_price_only_extension_4b","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":189000,"peak_price":196200,"peak_date":"2024-06-14","trough_price":91300,"trough_date":"2024-09-19","mfe_pct":3.81,"mae_pct":-51.69,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_leader_late_chase_without_fresh_order_bridge","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|tc_bonder_leader_late_chase_price_only_extension_4b|2024-06-13"}
```

## 6. Score-return alignment

### 6.1 True relative-strength winner family

`042700` early and `089030` show the constructive C07 family. The price path was not merely “semiconductor beta”; it was a concentrated repricing of HBM equipment bottleneck value. However, even the strongest row needs order, delivery, customer, and margin evidence before production Green.

### 6.2 Positive but high-MAE bridge

`031980` shows the middle case. Reflow/packaging equipment relative strength can create large MFE, but when the drawdown later overwhelms the entry cushion, the row should remain Stage2/Yellow with strict MAE and revision guardrails.

### 6.3 Equipment label blowoff

`039030` and the `042700` late-chase row are the warning signs. Same sector, same HBM equipment vocabulary, but timing changed the trade from bridge-backed repricing to price-only extension. C07 therefore needs a late-chase 4B guard even when the underlying company quality is high.

## 7. Raw component score simulation

| symbol | equipment specificity | order/customer bridge | margin/revision bridge | price confirmation | MAE/late-chase guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 042700 early | 25 | 20 | 16 | 25 | -9 | 77 | Stage3-Yellow/Green candidate |
| 089030 | 22 | 17 | 13 | 22 | -6 | 68 | Stage3-Yellow candidate |
| 031980 | 18 | 12 | 9 | 17 | -14 | 42 | Stage2/Yellow with guardrail |
| 039030 | 17 | 5 | 4 | 3 | -24 | 5 | Hard 4B/4C watch |
| 042700 late | 25 | 6 | 5 | 2 | -22 | 16 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c07_hbm_equipment_requires_order_delivery_margin_bridge","scope":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_action":"stage2_required_bridge","rule":"Do not promote HBM equipment relative-strength labels above Stage2 unless customer order, design-in, delivery schedule, capacity ramp, OPM, EPS revision, or margin bridge is visible.","supporting_cases":["039030","042700_late"],"counterbalanced_by":["042700_early","089030","031980"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c07_tc_bonder_test_handler_positive_delta","scope":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"TC-bonder and HBM test-handler leaders with visible order backlog, customer delivery path, and margin/revision bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["042700_early","089030"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c07_late_chase_price_only_4b_guard","scope":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_action":"local_4b_watch_guard","rule":"If C07 entry follows large price extension and lacks fresh order/revision evidence, cap at local 4B watch or event-cap even for sector leaders.","supporting_cases":["042700_late","039030"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c07_reflow_packaging_high_mae_guard","scope":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_action":"stage2_to_yellow_with_high_MAE_guardrail","rule":"Reflow/packaging equipment names can be Yellow candidates when MFE appears, but Green requires drawdown containment plus customer/order and OPM bridge.","supporting_cases":["031980"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","round":"R2","loop":"96","positive_rows":3,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C07 needs sharper timing control: HBM equipment leaders can be true winners, but the same label after price extension becomes local 4B/event-cap without fresh order and margin evidence.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","local_4b_watch_guard","stage2_to_yellow_with_high_MAE_guardrail"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","sample_count":5,"avg_mfe_pct":57.57,"avg_mae_pct":-37.32,"median_mfe_pct":52.87,"median_mae_pct":-33.87,"interpretation":"C07 has explosive upside in true HBM equipment leaders, but drawdown is severe when entries are late or bridge evidence is missing."}
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
  - historical corporate-action profile caveats, where present, are outside local 2024 windows
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C07 R2 loop 96 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c07_hbm_equipment_requires_order_delivery_margin_bridge -> stage2_required_bridge
  2. c07_tc_bonder_test_handler_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c07_late_chase_price_only_4b_guard -> local_4b_watch_guard
  4. c07_reflow_packaging_high_mae_guard -> stage2_to_yellow_with_high_MAE_guardrail

Expected behavior:
- HBM equipment vocabulary alone should not create Green.
- Customer order, delivery schedule, capacity ramp, OPM, EPS revision, or margin bridge can justify Stage3-Yellow/Green.
- Late price-only extension should be capped at local 4B/event-cap even for sector leaders.
```
