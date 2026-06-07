# E2R Stock-Web v12 Residual Research — R2 loop 97 / L2 / C08

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 97
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_SOCKET_THEME_HIGH_MAE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - customer_qualification_to_repeat_order_bridge_test
  - socket_theme_high_MAE_guardrail
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

C08은 “테스트 소켓”, “프로브/인터페이스”, “HBM/AI 반도체 수혜”라는 단어만으로 Green을 주는 bucket이 아니다. 이 archetype의 핵심은 고객 qualification이 반복 소모품 수요와 margin/revision으로 이어지는지다.

```text
test socket / probe / interface / customer qualification label
  → customer approval / design-in / device generation change
  → repeat consumable order / utilization / ASP-mix
  → gross margin / OPM / revision bridge
  → stock-web 1D OHLC forward path
```

소켓은 반도체 테스트의 작은 접점이다. 하지만 투자에서는 그 접점이 고객 승인과 반복 구매로 이어질 때만 회로가 닫힌다. 단순 “소켓 테마”는 스파크이고, customer-qualified recurring consumable은 전류다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["095340","131290","080580","058470"],"profile_paths":["atlas/symbol_profiles/095/095340.json","atlas/symbol_profiles/131/131290.json","atlas/symbol_profiles/080/080580.json","atlas/symbol_profiles/058/058470.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv","atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C08 at 14 rows, with 16 rows needed just to reach the 30-row minimum stability zone.
- Existing registry shows C08 parsed through `R2 loop 96`.
- This output uses `R2 loop 97`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file emphasizes socket/probe/interface customer-quality bridge versus socket-theme price spike and high-MAE decay.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C08-R2L97-01 | 095340 | ISC | 2024-09-23 | 2024-09-23 | 55900 | 66300 | 53500 | 18.60% | -4.29% | Socket leader second-leg positive path; qualification/repeat-order bridge candidate. |
| C08-R2L97-02 | 131290 | 티에스이 | 2024-09-23 | 2024-09-23 | 47900 | 56000 | 42100 | 16.91% | -12.11% | Probe/interface rebound with MFE but entry-day/early MAE requires staging. |
| C08-R2L97-03 | 080580 | 오킨스전자 | 2024-02-01 | 2024-02-01 | 13350 | 14430 | 4865 | 8.09% | -63.56% | Socket theme spike without durable customer/repeat-order bridge; hard counterexample. |
| C08-R2L97-04 | 058470 | 리노공업 | 2024-03-08 | 2024-03-08 | 215500 | 278500 | 164000 | 29.23% | -23.90% | High-quality socket/probe leader had real MFE, but late-cycle drawdown still demands guardrail. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C08-R2L97-01","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SOCKET_LEADER_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE","symbol":"095340","name":"ISC","trigger_type":"socket_leader_customer_qualification_repeat_consumable_margin_bridge","trigger_date":"2024-09-23","entry_date":"2024-09-23","entry_price":55900,"peak_price":66300,"peak_date":"2024-10-30","trough_price":53500,"trough_date":"2024-09-23","mfe_pct":18.60,"mae_pct":-4.29,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_customer_URLs","residual_flag":"positive_second_leg_but_requires_repeat_order_margin_bridge","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|095340|socket_leader_customer_qualification_repeat_consumable_margin_bridge|2024-09-23"}
{"row_type":"trigger","case_id":"C08-R2L97-02","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_INTERFACE_CUSTOMER_QUALITY_REBOUND_WITH_MAE_GUARD","symbol":"131290","name":"티에스이","trigger_type":"probe_interface_customer_quality_rebound_with_mae_guard","trigger_date":"2024-09-23","entry_date":"2024-09-23","entry_price":47900,"peak_price":56000,"peak_date":"2024-10-25","trough_price":42100,"trough_date":"2024-09-23","mfe_pct":16.91,"mae_pct":-12.11,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_MAE_guardrail","residual_flag":"positive_but_design_in_and_repeat_consumable_bridge_required","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|131290|probe_interface_customer_quality_rebound_with_mae_guard|2024-09-23"}
{"row_type":"trigger","case_id":"C08-R2L97-03","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SOCKET_THEME_EVENT_SPIKE_WITHOUT_REPEAT_ORDER_HIGH_MAE","symbol":"080580","name":"오킨스전자","trigger_type":"socket_theme_event_spike_without_repeat_order_high_mae","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":13350,"peak_price":14430,"peak_date":"2024-02-02","trough_price":4865,"trough_date":"2024-08-05","mfe_pct":8.09,"mae_pct":-63.56,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"socket_label_price_spike_without_customer_quality_repeat_order_bridge","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|080580|socket_theme_event_spike_without_repeat_order_high_mae|2024-02-01"}
{"row_type":"trigger","case_id":"C08-R2L97-04","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"QUALITY_SOCKET_PROBE_LEADER_MFE_WITH_CYCLE_DRAWDOWN_GUARD","symbol":"058470","name":"리노공업","trigger_type":"quality_socket_probe_leader_mfe_with_cycle_drawdown_guard","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":215500,"peak_price":278500,"peak_date":"2024-04-04","trough_price":164000,"trough_date":"2024-08-05","mfe_pct":29.23,"mae_pct":-23.90,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_cycle_MAE_guardrail","residual_flag":"quality_leader_positive_but_green_requires_revision_and_drawdown_containment","dedupe_key":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|058470|quality_socket_probe_leader_mfe_with_cycle_drawdown_guard|2024-03-08"}
```

## 6. Score-return alignment

### 6.1 Positive customer-quality bridge candidate

`095340` is the cleanest second-leg setup in this sample. The post-entry path had a contained trough and later upside into late October. That is the behavior C08 wants, but the non-price bridge still matters: customer qualification, design-in, recurring socket/consumable order, and margin/revision must be verified before Green.

### 6.2 Positive but staging-sensitive interface path

`131290` shows a more volatile bridge. It eventually made a useful MFE, but the entry row itself had a deep low. The model should allow Stage2→Yellow only with position/staging guardrails and require customer-quality evidence before any stronger promotion.

### 6.3 Theme spike hard failure

`080580` is the hard warning. It had a quick event MFE, but the forward path was dominated by a major drawdown. This row should teach the scorer not to treat socket vocabulary as customer-quality evidence. A socket label without repeat order or margin bridge is not C08 Green; it is event-cap/4C watch.

### 6.4 Quality leader still needs cycle guard

`058470` shows why a high-quality company is not automatically a low-risk entry. The leader produced strong MFE, but later cycle drawdown was large. The C08 rule should reward leader quality only when revision and drawdown containment survive the forward path.

## 7. Raw component score simulation

| symbol | customer-quality evidence | repeat consumable/order bridge | margin/revision bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 095340 | 21 | 16 | 13 | 18 | -3 | 65 | Stage3-Yellow candidate |
| 131290 | 18 | 13 | 10 | 16 | -6 | 51 | Stage2/Yellow with guardrail |
| 080580 | 11 | 3 | 2 | 4 | -22 | -2 | Hard counterexample / 4C watch |
| 058470 | 23 | 16 | 15 | 21 | -11 | 64 | Stage3-Yellow with cycle-MAE guard |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c08_socket_requires_customer_quality_repeat_order_bridge","scope":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","candidate_action":"stage2_required_bridge","rule":"Do not promote test-socket/probe/interface labels above Stage2 unless customer qualification, design-in, repeat consumable order, utilization, ASP mix, or margin/revision bridge is visible.","supporting_cases":["080580"],"counterbalanced_by":["095340","131290","058470"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c08_socket_theme_high_mae_guardrail","scope":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","candidate_action":"hard_4c_watch","rule":"If socket/test label MFE is followed by severe MAE and no verified customer-quality bridge, mark as hard counterexample or 4C watch.","supporting_cases":["080580"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c08_quality_leader_cycle_drawdown_guard","scope":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","candidate_action":"local_4b_watch_guard","rule":"Even quality socket/probe leaders should not receive Green when forward drawdown is large unless revision durability and repeat consumable evidence are verified.","supporting_cases":["058470"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c08_customer_qualified_second_leg_positive_delta","scope":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","candidate_action":"stage3_yellow_candidate_delta","rule":"Customer-qualified socket/probe names with repeat consumable bridge and contained MAE can receive stronger Stage3-Yellow treatment.","supporting_cases":["095340","131290"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","round":"R2","loop":"97","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C08 needs sharper separation between socket/test label strength and verified customer qualification plus repeat consumable margin bridge.","candidate_patch_axes":["stage2_required_bridge","hard_4c_watch","local_4b_watch_guard","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","sample_count":4,"avg_mfe_pct":18.21,"avg_mae_pct":-25.97,"median_mfe_pct":17.76,"median_mae_pct":-18.01,"interpretation":"C08 can produce strong MFE in quality leaders and second-leg setups, but socket-theme labels can generate severe MAE unless customer qualification and repeat-order bridge are real."}
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
  - historical corporate-action profile caveats, where present, are outside the local 2024 trigger windows used here
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
  1. c08_socket_requires_customer_quality_repeat_order_bridge -> stage2_required_bridge
  2. c08_socket_theme_high_mae_guardrail -> hard_4c_watch
  3. c08_quality_leader_cycle_drawdown_guard -> local_4b_watch_guard
  4. c08_customer_qualified_second_leg_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Socket/probe/interface vocabulary alone should not create Green.
- Customer qualification, design-in, repeat consumable order, utilization, ASP mix, margin, or revision bridge can justify Stage3-Yellow.
- Theme spikes with severe MAE should become hard counterexample / 4C watch.
- Quality leaders still need drawdown and revision durability guardrails.
```
