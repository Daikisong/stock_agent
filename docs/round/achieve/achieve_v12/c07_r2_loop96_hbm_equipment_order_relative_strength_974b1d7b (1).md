# E2R Stock-Web v12 Residual Research — R2 loop 96 / L2 / C07

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 96
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TC_BONDER_TEST_HANDLER_MEMORY_TESTER_ORDER_REVISION_RELATIVE_STRENGTH_VS_LATE_CHASE_AND_TESTER_THEME_DECAY
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - HBM_equipment_relative_strength_to_order_revision_bridge_test
  - TC_bonder_and_test_handler_leader_positive_delta
  - memory_tester_optionality_high_MAE_guardrail
  - HBM_equipment_late_chase_event_cap_guard
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

C07은 “HBM 장비”, “TC bonder”, “test handler”, “memory tester”, “advanced packaging equipment”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 상대강도가 실제 고객 order, delivery schedule, capacity ramp, ASP/mix, gross margin, OPM/FCF/EPS revision으로 내려오는지다.

```text
HBM equipment relative-strength headline
  → customer order / purchase order / capacity ramp
  → delivery schedule / acceptance / utilization
  → ASP or mix uplift / OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

HBM 장비 상대강도는 공장 라인에 불이 켜지는 장면이다. 그러나 장비주 이익은 불빛이 아니라 실제 발주서, 납품 검수, 반복 CAPEX, 마진으로 전류가 흐를 때 생긴다. C07은 “상대강도”와 “발주·마진 전환”을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["042700","089030","003160"],"profile_paths":["atlas/symbol_profiles/042/042700.json","atlas/symbol_profiles/089/089030.json","atlas/symbol_profiles/003/003160.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv"],"validation_scope":"2024 trigger-level forward path; selected local windows avoid active corporate-action contamination. 042700 caveats end 2022, 089030 caveats end 2022, and 003160 caveats are historical 1997/1998/1999."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C07 at 18 rows, 12 rows short of the 30-row minimum stability zone.
- Existing registry shows C07 parsed through `R2 loop 95`.
- This output uses `R2 loop 96`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C07 rows touched HBM test equipment, deposition equipment, laser/chiller/scrubber/ALD equipment, and test handler order bridges. This file compresses TC-bonder, HBM test-handler, memory-tester optionality, and late-chase timing guardrails.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C07-R2L96-01 | 042700 | 한미반도체 | 2024-03-26 | 2024-03-26 | 112500 | 196200 | 91200 | 74.40% | -18.93% | TC-bonder HBM leader path worked, but full-window drawdown requires sizing/order-revision guard. |
| C07-R2L96-02 | 089030 | 테크윙 | 2024-03-12 | 2024-03-12 | 26850 | 70800 | 25200 | 163.69% | -6.15% | HBM test-handler/order relative-strength path was the cleanest positive sample. |
| C07-R2L96-03 | 003160 | 디아이 | 2024-04-04 | 2024-04-04 | 16140 | 30800 | 10910 | 90.83% | -32.40% | Memory tester/HBM equipment optionality made MFE, but high MAE blocks Green. |
| C07-R2L96-04 | 042700 | 한미반도체 | 2024-06-14 | 2024-06-14 | 179900 | 196200 | 91200 | 9.06% | -49.31% | Same TC-bonder leader, late-chase after extension became local 4B/event-cap. |
| C07-R2L96-05 | 089030 | 테크윙 | 2024-07-11 | 2024-07-11 | 68700 | 70800 | 30000 | 3.06% | -56.33% | Same HBM test-handler winner, late entry without fresh order evidence became high-MAE. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C07-R2L96-01","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"TC_BONDER_HBM_ORDER_REVISION_RELATIVE_STRENGTH_LEADER","symbol":"042700","name":"한미반도체","trigger_type":"tc_bonder_hbm_order_revision_relative_strength_leader","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":112500,"peak_price":196200,"peak_date":"2024-06-14","trough_price":91200,"trough_date":"2024-10-29","mfe_pct":74.40,"mae_pct":-18.93,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_with_sizing_guard","residual_flag":"TC_bonder_relative_strength_positive_but_requires_exact_order_revision_margin_URLs","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|tc_bonder_hbm_order_revision_relative_strength_leader|2024-03-26"}
{"row_type":"trigger","case_id":"C07-R2L96-02","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_ORDER_CAPACITY_RELATIVE_STRENGTH_LEADER","symbol":"089030","name":"테크윙","trigger_type":"hbm_test_handler_order_capacity_relative_strength_leader","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":26850,"peak_price":70800,"peak_date":"2024-07-11","trough_price":25200,"trough_date":"2024-03-12","mfe_pct":163.69,"mae_pct":-6.15,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_order_capacity_URLs","residual_flag":"clean_HBM_test_handler_relative_strength_positive_path_requires_order_revenue_URLs","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|hbm_test_handler_order_capacity_relative_strength_leader|2024-03-12"}
{"row_type":"trigger","case_id":"C07-R2L96-03","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_TESTER_HBM_OPTIONALITY_HIGH_MAE_GUARD","symbol":"003160","name":"디아이","trigger_type":"memory_tester_hbm_optionality_high_mae_guard","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":16140,"peak_price":30800,"peak_date":"2024-06-27","trough_price":10910,"trough_date":"2024-09-09","mfe_pct":90.83,"mae_pct":-32.40,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"memory_tester_HBM_optionality_MFE_but_high_MAE_requires_order_OPM_bridge","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|003160|memory_tester_hbm_optionality_high_mae_guard|2024-04-04"}
{"row_type":"trigger","case_id":"C07-R2L96-04","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"TC_BONDER_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"042700","name":"한미반도체","trigger_type":"tc_bonder_leader_late_chase_price_only_extension_4b","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":179900,"peak_price":196200,"peak_date":"2024-06-14","trough_price":91200,"trough_date":"2024-10-29","mfe_pct":9.06,"mae_pct":-49.31,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_TCB_leader_late_chase_without_fresh_order_revision_bridge","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|tc_bonder_leader_late_chase_price_only_extension_4b|2024-06-14"}
{"row_type":"trigger","case_id":"C07-R2L96-05","round":"R2","loop":"96","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_LEADER_LATE_CHASE_HIGH_MAE_4B","symbol":"089030","name":"테크윙","trigger_type":"hbm_test_handler_leader_late_chase_high_mae_4b","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":68700,"peak_price":70800,"peak_date":"2024-07-11","trough_price":30000,"trough_date":"2024-09-09","mfe_pct":3.06,"mae_pct":-56.33,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_HBM_test_handler_winner_late_entry_without_fresh_order_evidence","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|hbm_test_handler_leader_late_chase_high_mae_4b|2024-07-11"}
```

## 6. Score-return alignment

### 6.1 HBM equipment relative strength can work

`042700` early and `089030` early show the constructive C07 family. TC bonder and HBM test-handler leaders can generate large MFE when relative strength is backed by plausible customer order and capacity-ramp narratives. However, `042700` shows that even the best leader can later produce deep drawdown if the entry is not staged.

### 6.2 Memory tester optionality is not enough

`003160` shows the middle family. It can make huge MFE during the HBM/tester theme, but the later drawdown is too large for automatic Green. The model should ask whether the order, delivery, revenue, and OPM bridge is real rather than simply transferring TC-bonder/test-handler scores to every memory tester name.

### 6.3 Same winner, different entry

`042700` late and `089030` late are the timing guardrails. The same companies that worked earlier became poor risk/reward when the trigger was mostly price extension. C07 needs a local 4B/event-cap rule for late-chase entries without fresh order/revision evidence.

## 7. Raw component score simulation

| symbol | HBM equipment specificity | customer order/revision | delivery/capacity ramp | OPM/FCF bridge | price confirmation | MAE/late-chase guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 042700 early | 24 | 20 | 17 | 15 | 20 | -8 | 68 | Stage3-Yellow/Green candidate with sizing guard |
| 089030 early | 23 | 21 | 18 | 15 | 25 | -3 | 79 | Stage3-Yellow/Green candidate |
| 003160 | 16 | 9 | 8 | 5 | 18 | -15 | 41 | Stage2/Yellow high-MAE guard |
| 042700 late | 24 | 6 | 5 | 4 | 2 | -22 | 19 | Local 4B/event-cap |
| 089030 late | 23 | 6 | 5 | 4 | 1 | -25 | 14 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c07_hbm_equipment_requires_order_revision_margin_bridge","scope":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_action":"stage2_required_bridge","rule":"Do not promote HBM equipment relative-strength labels above Stage2 unless customer order, delivery schedule, capacity ramp, acceptance, ASP/mix, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["003160","042700_late","089030_late"],"counterbalanced_by":["042700_early","089030_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c07_tcb_testhandler_positive_delta","scope":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"TC-bonder and HBM test-handler leaders with verified customer orders, capacity ramp, and revision/margin bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["042700_early","089030_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c07_memory_tester_optionality_high_MAE_guard","scope":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_action":"stage2_to_yellow_with_high_MAE_guardrail","rule":"Memory tester/HBM optionality can be Yellow only when order and OPM bridge is verified; high MAE blocks Green even if MFE is large.","supporting_cases":["003160"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c07_late_chase_hbm_equipment_4b_guard","scope":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_action":"local_4b_watch_guard","rule":"If an HBM equipment leader entry follows a large price extension and lacks fresh order/revision evidence, cap at local 4B or event-cap.","supporting_cases":["042700_late","089030_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","round":"R2","loop":"96","positive_rows":2,"counterexample_rows":3,"new_symbol_count":3,"primary_residual":"C07 should separate true TC-bonder/HBM test-handler order-relative-strength winners from generic memory-tester optionality and late-chase price-only extensions without fresh order/revision evidence.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_high_MAE_guardrail","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","sample_count":5,"avg_mfe_pct":68.21,"avg_mae_pct":-32.62,"median_mfe_pct":74.40,"median_mae_pct":-32.40,"interpretation":"C07 has explosive upside when HBM equipment relative strength is tied to order/capacity/revision, but late-chase and generic tester rows rapidly become high-MAE false Stage2 paths."}
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
- Ingest this C07 R2 loop 96 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c07_hbm_equipment_requires_order_revision_margin_bridge -> stage2_required_bridge
  2. c07_tcb_testhandler_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c07_memory_tester_optionality_high_MAE_guard -> stage2_to_yellow_with_high_MAE_guardrail
  4. c07_late_chase_hbm_equipment_4b_guard -> local_4b_watch_guard

Expected behavior:
- HBM equipment relative-strength vocabulary alone should not create Green.
- Customer order, delivery schedule, capacity ramp, acceptance, ASP/mix, OPM, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Memory tester optionality and late-chase HBM equipment entries should remain capped until fresh order/revision evidence appears.
```
