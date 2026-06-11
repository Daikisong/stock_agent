# E2R Stock-Web v12 Residual Research — R2 loop 99 / L2 / C10

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 99
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: QUARTZ_SILICON_PARTS_SIC_RING_MEMORY_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_PARTS_LABEL_LATE_CHASE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - memory_recovery_to_utilization_order_margin_bridge_test
  - quartz_silicon_parts_cycle_guardrail
  - SiC_ring_utilization_OPM_bridge_test
  - memory_parts_late_chase_4B_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` 전용 residual research다.

C10은 “메모리 업황 회복”, “장비 사이클”, “소모품 반등”, “quartz/silicon parts”, “SiC ring”이라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 memory recovery beta가 실제 고객 가동률, 장비/소모품 order, utilization, ASP/mix, inventory normalization, OPM/FCF/revision으로 내려오는지다.

```text
memory recovery / equipment-cycle headline
  → customer utilization / capex or consumable order
  → quartz, silicon parts, SiC ring, chamber utilization
  → ASP/mix, inventory normalization, OPM/FCF/revision
  → stock-web 1D OHLC forward path
```

메모리 회복은 반도체 공장의 온도가 올라가는 장면과 같다. 온도가 오른다고 모든 부품사가 바로 이익을 남기는 것은 아니다. 실제 장비가 돌고, chamber가 닳고, 소모품 reorder와 마진이 돌아올 때 C10의 회로가 닫힌다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["074600","064760","101160"],"profile_paths":["atlas/symbol_profiles/074/074600.json","atlas/symbol_profiles/064/064760.json","atlas/symbol_profiles/101/101160.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv","atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv","atlas/ohlcv_tradable_by_symbol_year/101/101160/2024.csv"],"validation_scope":"2024 trigger-level forward path; 074600 caveats are 2004/2017, 064760 has zero corporate-action candidates, 101160 caveat is 2014; selected 2024 windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C10 at 21 rows, 9 rows short of the 30-row minimum stability zone.
- Existing registry shows C10 parsed through `R2 loop 98`.
- This output uses `R2 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C10 loop 98 emphasized quartz/silicon parts, SSD test, and late chase. This file compresses quartz positive-with-drawdown, SiC ring positive-with-cycle decay, weak silicon-parts conversion, and same quartz leader late-chase.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C10-R2L99-01 | 074600 | 원익QnC | 2024-03-20 | 2024-03-20 | 30750 | 41000 | 22450 | 33.33% | -26.99% | Quartz/parts recovery made MFE, but utilization and OPM bridge must be verified. |
| C10-R2L99-02 | 064760 | 티씨케이 | 2024-03-21 | 2024-03-21 | 106000 | 149900 | 80600 | 41.42% | -23.96% | SiC ring / memory utilization recovery worked, but later cycle drawdown blocks automatic Green. |
| C10-R2L99-03 | 101160 | 월덱스 | 2024-03-21 | 2024-03-21 | 25150 | 26150 | 21400 | 3.98% | -14.91% | Silicon parts label had weak MFE; memory recovery beta did not convert cleanly. |
| C10-R2L99-04 | 074600 | 원익QnC | 2024-06-07 | 2024-06-07 | 40950 | 41000 | 22450 | 0.12% | -45.18% | Same quartz leader, late-chase after extension became local 4B/event-cap. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C10-R2L99-01","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_PARTS_MEMORY_RECOVERY_UTILIZATION_OPM_BRIDGE","symbol":"074600","name":"원익QnC","trigger_type":"quartz_parts_memory_recovery_utilization_opm_bridge","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":30750,"peak_price":41000,"peak_date":"2024-06-07","trough_price":22450,"trough_date":"2024-10-22","mfe_pct":33.33,"mae_pct":-26.99,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_utilization_OPM_guard","residual_flag":"quartz_parts_MFE_but_full_window_drawdown_requires_utilization_inventory_OPM_bridge","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|074600|quartz_parts_memory_recovery_utilization_opm_bridge|2024-03-20"}
{"row_type":"trigger","case_id":"C10-R2L99-02","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SIC_RING_MEMORY_UTILIZATION_RECOVERY_HIGH_MAE_GUARD","symbol":"064760","name":"티씨케이","trigger_type":"sic_ring_memory_utilization_recovery_high_mae_guard","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":106000,"peak_price":149900,"peak_date":"2024-06-14","trough_price":80600,"trough_date":"2024-10-31","mfe_pct":41.42,"mae_pct":-23.96,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_cycle_drawdown_guard","residual_flag":"SiC_ring_utilization_recovery_positive_but_later_cycle_drawdown_blocks_Green","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|064760|sic_ring_memory_utilization_recovery_high_mae_guard|2024-03-21"}
{"row_type":"trigger","case_id":"C10-R2L99-03","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SILICON_PARTS_MEMORY_RECOVERY_LOW_MFE_FALSE_STAGE2","symbol":"101160","name":"월덱스","trigger_type":"silicon_parts_memory_recovery_low_mfe_false_stage2","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":25150,"peak_price":26150,"peak_date":"2024-04-02","trough_price":21400,"trough_date":"2024-05-31","mfe_pct":3.98,"mae_pct":-14.91,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"silicon_parts_memory_recovery_label_low_MFE_without_order_utilization_OPM_bridge","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|101160|silicon_parts_memory_recovery_low_mfe_false_stage2|2024-03-21"}
{"row_type":"trigger","case_id":"C10-R2L99-04","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_PARTS_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"074600","name":"원익QnC","trigger_type":"quartz_parts_leader_late_chase_price_only_extension_4b","trigger_date":"2024-06-07","entry_date":"2024-06-07","entry_price":40950,"peak_price":41000,"peak_date":"2024-06-07","trough_price":22450,"trough_date":"2024-10-22","mfe_pct":0.12,"mae_pct":-45.18,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_quartz_parts_recovery_story_late_chase_without_fresh_order_OPM_evidence","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|074600|quartz_parts_leader_late_chase_price_only_extension_4b|2024-06-07"}
```

## 6. Score-return alignment

### 6.1 Parts recovery can work, but C10 needs non-price bridge

`074600` and `064760` show that memory recovery can create meaningful MFE in quartz/SiC ring names. However, both later suffered material drawdown. C10 should not treat recovery beta as Green unless utilization, order cadence, inventory normalization, ASP/mix and OPM/FCF bridge are visible.

### 6.2 Weak conversion family

`101160` is the low-MFE row. It had the same memory-parts vocabulary but did not produce strong forward asymmetry from the selected trigger. This is exactly where C10 needs a conversion test: is the customer actually raising utilization and reordering, or is the row just moving with sector beta?

### 6.3 Same story, bad timing

The `074600` late-chase row shows timing risk. The same quartz parts story became a very poor entry when the trigger followed the June price extension. This is a local 4B/event-cap case unless fresh order or OPM evidence appears.

## 7. Raw component score simulation

| symbol | memory recovery evidence | utilization/order bridge | ASP/mix/inventory | OPM/FCF bridge | price confirmation | MAE/late-chase guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 074600 early | 18 | 13 | 10 | 9 | 15 | -13 | 52 | Stage2/Yellow with utilization guard |
| 064760 | 19 | 14 | 11 | 10 | 17 | -12 | 59 | Stage2/Yellow with cycle guard |
| 101160 | 14 | 5 | 4 | 3 | 2 | -7 | 21 | Stage2/local 4B |
| 074600 late | 18 | 5 | 4 | 3 | 1 | -20 | 11 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c10_memory_recovery_requires_utilization_order_OPM_bridge","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_action":"stage2_required_bridge","rule":"Do not promote memory recovery / equipment-cycle labels above Stage2 unless customer utilization, capex/consumable order, chamber usage, ASP/mix, inventory normalization, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["101160","074600_late"],"counterbalanced_by":["074600_early","064760"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c10_quartz_sic_parts_positive_but_guarded_delta","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_action":"stage2_to_yellow_with_high_MAE_guardrail","rule":"Quartz and SiC ring names can receive Yellow treatment when memory recovery is tied to utilization and order cadence, but high MAE blocks Green until OPM/FCF evidence is URL-verified.","supporting_cases":["074600_early","064760"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c10_silicon_parts_low_MFE_false_stage2_guard","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_action":"local_4b_watch_guard","rule":"Silicon parts rows with low MFE should remain local 4B unless utilization and reorder evidence repairs the row.","supporting_cases":["101160"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c10_parts_leader_late_chase_4b_guard","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_action":"local_4b_watch_guard","rule":"If memory parts leader entry follows a price extension and lacks fresh order/OPM evidence, cap at local 4B or event-cap.","supporting_cases":["074600_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","round":"R2","loop":"99","positive_rows":2,"counterexample_rows":2,"new_symbol_count":3,"primary_residual":"C10 should separate quartz/SiC memory-parts recovery with utilization/order evidence from low-MFE silicon-parts beta and late-chase price-only extensions.","candidate_patch_axes":["stage2_required_bridge","stage2_to_yellow_with_high_MAE_guardrail","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","sample_count":4,"avg_mfe_pct":19.71,"avg_mae_pct":-27.01,"median_mfe_pct":18.66,"median_mae_pct":-25.48,"interpretation":"C10 memory recovery labels can produce MFE, but most rows require strict utilization/order/OPM bridge and timing guards because late-cycle drawdown is large."}
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
- Ingest this C10 R2 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c10_memory_recovery_requires_utilization_order_OPM_bridge -> stage2_required_bridge
  2. c10_quartz_sic_parts_positive_but_guarded_delta -> stage2_to_yellow_with_high_MAE_guardrail
  3. c10_silicon_parts_low_MFE_false_stage2_guard -> local_4b_watch_guard
  4. c10_parts_leader_late_chase_4b_guard -> local_4b_watch_guard

Expected behavior:
- Memory recovery / equipment-cycle vocabulary alone should not create Green.
- Customer utilization, capex/consumable order, chamber usage, ASP/mix, inventory normalization, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Low-MFE silicon-parts and late-chase quartz rows should remain local 4B until fresh non-price evidence appears.
```
