# E2R Stock-Web v12 Residual Research — R2 loop 99 / L2 / C10

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 99
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_EQUIPMENT_PARTS_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_BETA_LABEL_HIGH_MAE_DECAY
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - memory_recovery_beta_vs_order_conversion_test
  - utilization_margin_bridge_guardrail
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

이번 파일은 `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` 전용 residual research다.

C10은 “메모리 회복”, “반도체 장비”, “부품/소재 cycle”이라는 말만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 memory cycle beta가 실제 장비 order, utilization, consumable/parts reorder, margin/revision으로 내려오는지다.

```text
memory recovery / equipment cycle label
  → customer order / utilization / parts reorder
  → delivery schedule / ASP or mix recovery
  → margin / OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

메모리 회복 beta는 공장 조명이 다시 켜지는 장면이다. 하지만 장비회사와 부품회사가 돈을 버는 순간은 조명이 아니라 라인이 실제로 돌고, 소모품이 다시 주문되고, 원가를 넘는 마진이 찍힐 때다. C10은 이 조명과 컨베이어벨트를 구분한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["084370","074600","064760","000990"],"profile_paths":["atlas/symbol_profiles/084/084370.json","atlas/symbol_profiles/074/074600.json","atlas/symbol_profiles/064/064760.json","atlas/symbol_profiles/000/000990.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv","atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv","atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv"],"validation_scope":"2024 trigger-level forward path; old corporate-action profile caveats are outside local windows or absent; local 2024 rows are used as tradable_raw calibration rows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C10 at 21 rows, 9 rows short of the 30-row minimum stability zone.
- Registry shows C10 parsed through `R2 loop 98`.
- This output uses `R2 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file shifts into front-end memory equipment, quartz/consumable parts, SiC ring/parts, and non-HBM foundry beta decay.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C10-R2L99-01 | 084370 | 유진테크 | 2024-04-04 | 2024-04-04 | 46500 | 60000 | 34000 | 29.03% | -26.88% | Memory equipment order-cycle MFE existed, but later drawdown needs utilization/order/margin proof. |
| C10-R2L99-02 | 074600 | 원익QnC | 2024-03-20 | 2024-03-20 | 30750 | 41000 | 22250 | 33.33% | -27.64% | Quartz/parts utilization recovery created upside, but high MAE blocks automatic Green. |
| C10-R2L99-03 | 064760 | 티씨케이 | 2024-03-29 | 2024-03-29 | 130100 | 149900 | 80600 | 15.22% | -38.05% | SiC ring/parts memory recovery label was fragile without durable reorder/margin bridge. |
| C10-R2L99-04 | 000990 | DB하이텍 | 2024-06-20 | 2024-06-20 | 57100 | 58900 | 35200 | 3.15% | -38.35% | Foundry/memory recovery beta spike failed; strong counterexample for generic recovery labels. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C10-R2L99-01","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_DEPOSITION_EQUIPMENT_ORDER_CYCLE_HIGH_MAE_GUARD","symbol":"084370","name":"유진테크","trigger_type":"memory_deposition_equipment_order_cycle_high_mae_guard","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":46500,"peak_price":60000,"peak_date":"2024-05-28","trough_price":34000,"trough_date":"2024-10-23","mfe_pct":29.03,"mae_pct":-26.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_high_MAE_guardrail","residual_flag":"memory_equipment_order_cycle_MFE_but_utilization_margin_bridge_required","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|084370|memory_deposition_equipment_order_cycle_high_mae_guard|2024-04-04"}
{"row_type":"trigger","case_id":"C10-R2L99-02","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_PARTS_UTILIZATION_REORDER_MARGIN_BRIDGE_HIGH_MAE","symbol":"074600","name":"원익QnC","trigger_type":"quartz_parts_utilization_reorder_margin_bridge_high_mae","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":30750,"peak_price":41000,"peak_date":"2024-06-07","trough_price":22250,"trough_date":"2024-10-23","mfe_pct":33.33,"mae_pct":-27.64,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"quartz_parts_recovery_positive_but_reorder_margin_bridge_required","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|074600|quartz_parts_utilization_reorder_margin_bridge_high_mae|2024-03-20"}
{"row_type":"trigger","case_id":"C10-R2L99-03","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SIC_RING_PARTS_MEMORY_RECOVERY_REORDER_DECAY","symbol":"064760","name":"티씨케이","trigger_type":"sic_ring_parts_memory_recovery_reorder_decay","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":130100,"peak_price":149900,"peak_date":"2024-06-14","trough_price":80600,"trough_date":"2024-10-31","mfe_pct":15.22,"mae_pct":-38.05,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"parts_recovery_label_decayed_without_durable_order_margin_bridge","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|064760|sic_ring_parts_memory_recovery_reorder_decay|2024-03-29"}
{"row_type":"trigger","case_id":"C10-R2L99-04","round":"R2","loop":"99","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"GENERIC_FOUNDRY_MEMORY_RECOVERY_BETA_FALSE_STAGE2","symbol":"000990","name":"DB하이텍","trigger_type":"generic_foundry_memory_recovery_beta_false_stage2","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":57100,"peak_price":58900,"peak_date":"2024-06-20","trough_price":35200,"trough_date":"2024-09-09","mfe_pct":3.15,"mae_pct":-38.35,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"memory_recovery_beta_spike_without_equipment_order_utilization_margin_bridge","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|000990|generic_foundry_memory_recovery_beta_false_stage2|2024-06-20"}
```

## 6. Score-return alignment

### 6.1 Equipment and parts MFE is real, but not enough

`084370` and `074600` show why C10 exists. Memory equipment/parts names can produce meaningful MFE when the market starts pricing a cycle turn. But both paths later produced deep drawdown. The model should not treat the first price leg as proof of order conversion; it needs utilization, shipment, parts reorder, and margin confirmation.

### 6.2 Parts recovery decay

`064760` shows the fragile middle case. A SiC ring/parts recovery label can rally on memory cycle expectation, but if reorder and margin bridge are not durable, the forward path can become high-MAE despite initial MFE.

### 6.3 Generic memory beta false positive

`000990` is the hard counterexample. It is a memory-adjacent semiconductor beta name, but not a clean memory equipment/order-cycle row. The price path had tiny MFE and severe MAE. This should be capped as 4B/4C watch when non-price bridge is absent.

## 7. Raw component score simulation

| symbol | equipment/parts specificity | order/utilization bridge | margin/revision bridge | price confirmation | MAE/logic guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 084370 | 20 | 13 | 10 | 16 | -12 | 47 | Stage2/Yellow with high-MAE guardrail |
| 074600 | 19 | 14 | 10 | 17 | -13 | 47 | Stage2/Yellow with high-MAE guardrail |
| 064760 | 18 | 8 | 6 | 8 | -16 | 24 | Stage2/local 4B watch |
| 000990 | 5 | 2 | 2 | 1 | -18 | -8 | Hard counterexample / 4C watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c10_memory_recovery_requires_order_utilization_margin_bridge","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_action":"stage2_required_bridge","rule":"Do not promote memory recovery/equipment-cycle labels above Stage2 unless customer order, utilization, shipment, parts reorder, OPM, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["064760","000990"],"counterbalanced_by":["084370","074600"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c10_high_mae_parts_cycle_guardrail","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_action":"local_4b_watch_guard","rule":"If memory equipment/parts MFE is followed by deep MAE and no verified order/reorder/margin bridge, cap at local 4B watch or event-cap.","supporting_cases":["084370","074600","064760"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c10_generic_memory_beta_false_stage2_guard","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_action":"hard_4c_watch","rule":"Generic foundry or memory beta with small MFE and severe MAE should be marked hard counterexample/4C watch, not persistent Stage2.","supporting_cases":["000990"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c10_utilization_reorder_positive_delta","scope":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","candidate_action":"stage3_yellow_candidate_delta","rule":"Equipment/parts names with verified utilization, repeat order/reorder, and margin bridge can receive Stage3-Yellow treatment, but not Green while MAE remains severe.","supporting_cases":["084370","074600"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","round":"R2","loop":"99","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C10 needs sharper separation between memory recovery beta and actual equipment/parts order, utilization, reorder, and margin conversion.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_watch","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","sample_count":4,"avg_mfe_pct":20.18,"avg_mae_pct":-32.73,"median_mfe_pct":22.13,"median_mae_pct":-32.85,"interpretation":"C10 memory-equipment beta can create MFE, but without order/utilization/margin bridge the drawdown is often larger than the upside."}
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
  - historical corporate-action caveats, where present, are outside local 2024 windows
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
  1. c10_memory_recovery_requires_order_utilization_margin_bridge -> stage2_required_bridge
  2. c10_high_mae_parts_cycle_guardrail -> local_4b_watch_guard
  3. c10_generic_memory_beta_false_stage2_guard -> hard_4c_watch
  4. c10_utilization_reorder_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Memory recovery vocabulary alone should not create Green.
- Customer order, utilization, shipment, parts reorder, OPM, margin, FCF, or EPS revision can justify Stage3-Yellow.
- Generic foundry or memory beta with small MFE and severe MAE should become hard counterexample / 4C watch.
```
