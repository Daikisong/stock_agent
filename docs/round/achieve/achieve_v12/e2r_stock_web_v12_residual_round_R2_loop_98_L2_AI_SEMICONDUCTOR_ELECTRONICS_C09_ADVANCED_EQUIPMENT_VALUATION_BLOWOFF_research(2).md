# E2R Stock-Web v12 Residual Research — R2 loop 98 / L2 / C09

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 98
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_DEPOSITION_METROLOGY_PROCESS_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_HIGH_MAE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - valuation_blowoff_guardrail
  - order_margin_bridge_test
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

이번 파일은 `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` 전용 residual research다.

C09는 “ALD/CVD/inspection/metrology/EUV/advanced equipment”라는 단어가 보였다는 이유로 Stage3-Green을 주는 bucket이 아니다. 장비주는 주문서가 오기 전에도 먼저 달린다. 하지만 가격이 먼저 달린 구간과 실제 order/margin bridge가 뒤따른 구간은 분리해야 한다.

```text
advanced equipment / process technology / AI-HBM capex label
  → actual order / customer acceptance / delivery schedule
  → revenue recognition / utilization / product-mix margin
  → OPM / EPS revision / cash-flow bridge
  → stock-web 1D OHLC forward path
```

장비주 valuation은 압축공기 같다. 수주와 마진이 밸브가 되면 힘이 된다. 밸브 없이 압력만 올라가면 blowoff 뒤에 역류가 온다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["240810","036810","140860","079370"],"profile_paths":["atlas/symbol_profiles/240/240810.json","atlas/symbol_profiles/036/036810.json","atlas/symbol_profiles/140/140860.json","atlas/symbol_profiles/079/079370.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv","atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv","atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local post-trigger windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C09 at 15 rows, with 15 rows needed just to reach the 30-row minimum stability zone.
- Existing registry shows C09 parsed through `R2 loop 97`.
- This output uses `R2 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file emphasizes advanced deposition / EUV-pellicle-support / metrology quality / process equipment event-cap paths.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C09-R2L98-01 | 240810 | 원익IPS | 2024-03-29 | 2024-03-29 | 41500 | 44850 | 26950 | 8.07% | -35.06% | Advanced deposition equipment label spike without enough order/margin bridge; high-MAE false Stage2. |
| C09-R2L98-02 | 036810 | 에프에스티 | 2024-04-09 | 2024-04-09 | 27900 | 32100 | 17070 | 15.05% | -38.82% | EUV/pellicle/chiller-style advanced equipment optionality produced MFE but later collapsed. |
| C09-R2L98-03 | 140860 | 파크시스템스 | 2024-09-23 | 2024-09-23 | 184700 | 219500 | 174300 | 18.84% | -5.63% | Metrology quality name with contained MAE; positive C09 bridge candidate pending exact order/margin proof. |
| C09-R2L98-04 | 079370 | 제우스 | 2024-05-21 | 2024-05-21 | 19350 | 19950 | 14180 | 3.10% | -26.72% | Process equipment/robot label had low MFE and large MAE; event-cap counterexample. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C09-R2L98-01","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF_NO_ORDER_MARGIN_BRIDGE","symbol":"240810","name":"원익IPS","trigger_type":"advanced_deposition_equipment_valuation_blowoff_no_order_margin_bridge","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":41500,"peak_price":44850,"peak_date":"2024-04-08","trough_price":26950,"trough_date":"2024-10-25","mfe_pct":8.07,"mae_pct":-35.06,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch_not_Green","residual_flag":"advanced_equipment_label_spike_without_order_margin_bridge","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|240810|advanced_deposition_equipment_valuation_blowoff_no_order_margin_bridge|2024-03-29"}
{"row_type":"trigger","case_id":"C09-R2L98-02","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"EUV_PELLICLE_CHILLER_OPTIONALITY_BLOWOFF_HIGH_MAE","symbol":"036810","name":"에프에스티","trigger_type":"euv_pellicle_chiller_optionality_blowoff_high_mae","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":27900,"peak_price":32100,"peak_date":"2024-08-01","trough_price":17070,"trough_date":"2024-10-25","mfe_pct":15.05,"mae_pct":-38.82,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_Yellow_watch_with_high_MAE_guardrail","residual_flag":"optionality_mfe_but_later_order_margin_absence_high_mae","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|036810|euv_pellicle_chiller_optionality_blowoff_high_mae|2024-04-09"}
{"row_type":"trigger","case_id":"C09-R2L98-03","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_METROLOGY_QUALITY_ORDER_MARGIN_BRIDGE_CANDIDATE","symbol":"140860","name":"파크시스템스","trigger_type":"advanced_metrology_quality_order_margin_bridge_candidate","trigger_date":"2024-09-23","entry_date":"2024-09-23","entry_price":184700,"peak_price":219500,"peak_date":"2024-10-24","trough_price":174300,"trough_date":"2024-09-23","mfe_pct":18.84,"mae_pct":-5.63,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_order_margin_URLs","residual_flag":"quality_metrology_positive_but_green_requires_order_revision_bridge","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|140860|advanced_metrology_quality_order_margin_bridge_candidate|2024-09-23"}
{"row_type":"trigger","case_id":"C09-R2L98-04","round":"R2","loop":"98","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"PROCESS_EQUIPMENT_ROBOT_EVENT_CAP_LOW_MFE_HIGH_MAE","symbol":"079370","name":"제우스","trigger_type":"process_equipment_robot_event_cap_low_mfe_high_mae","trigger_date":"2024-05-21","entry_date":"2024-05-21","entry_price":19350,"peak_price":19950,"peak_date":"2024-05-21","trough_price":14180,"trough_date":"2024-07-22","mfe_pct":3.10,"mae_pct":-26.72,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_local_4B_watch","residual_flag":"process_equipment_label_low_mfe_without_order_margin_bridge","dedupe_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|079370|process_equipment_robot_event_cap_low_mfe_high_mae|2024-05-21"}
```

## 6. Score-return alignment

### 6.1 Blowoff / false Stage2 family

`240810` and `036810` are the core C09 warning. The market recognized advanced process equipment and EUV-adjacent optionality, but the forward path punished entries that did not have URL-verified order, delivery, utilization, margin, or revision bridge. These should be capped at Stage2/Yellow watch or local 4B watch until non-price bridge arrives.

### 6.2 Quality metrology exception

`140860` shows that C09 is not a blanket short/avoid bucket. A quality metrology name can re-rate with contained MAE when the market believes the order/margin bridge. Still, Green requires exact non-price evidence because the same valuation regime can turn into blowoff when order conversion is late.

### 6.3 Event-cap equipment label

`079370` shows a low-MFE/high-MAE path. Equipment or robot/process vocabulary alone was not enough. Without order backlog, revenue recognition, and margin bridge, the stock behaved like an event-cap rather than an advanced-equipment compounder.

## 7. Raw component score simulation

| symbol | advanced equipment evidence | order/delivery bridge | margin/revision bridge | valuation risk | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 240810 | 22 | 7 | 5 | -15 | 5 | -14 | 10 | Event-cap / local 4B watch |
| 036810 | 21 | 8 | 5 | -14 | 10 | -15 | 15 | Stage2 watch with high-MAE guard |
| 140860 | 22 | 16 | 14 | -6 | 19 | -3 | 62 | Stage3-Yellow candidate |
| 079370 | 15 | 5 | 3 | -10 | 2 | -12 | 3 | Event-cap / false Stage2 |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c09_advanced_equipment_requires_order_margin_bridge","scope":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","candidate_action":"stage2_required_bridge","rule":"Do not promote advanced-equipment labels above Stage2 unless order, delivery schedule, customer acceptance, utilization, OPM, EPS revision, or cash-flow bridge is visible.","supporting_cases":["240810","036810","079370"],"counterbalanced_by":["140860"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c09_valuation_blowoff_high_mae_guardrail","scope":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","candidate_action":"local_4b_watch_guard","rule":"If advanced equipment price strength is followed by high MAE and no verified non-price bridge, cap at local 4B watch or event-cap.","supporting_cases":["240810","036810","079370"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c09_metrology_quality_positive_delta","scope":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","candidate_action":"stage3_yellow_candidate_delta","rule":"Advanced metrology or process-control names with verified order/margin bridge and contained MAE can receive Stage3-Yellow treatment, but Green requires exact URL evidence.","supporting_cases":["140860"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","round":"R2","loop":"98","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C09 needs sharper separation between advanced-equipment valuation blowoff and verified order/margin/revision bridge.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","sample_count":4,"avg_mfe_pct":11.27,"avg_mae_pct":-26.56,"median_mfe_pct":11.56,"median_mae_pct":-30.89,"interpretation":"C09 advanced-equipment labels often create poor asymmetry unless order/margin/revision bridge is verified; metrology quality can work but needs evidence."}
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
  - 079370 has 2024 Jan/Feb corporate-action profile caveats, but the selected May trigger path is post-caveat and treated as a local historical calibration row only
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
  1. c09_advanced_equipment_requires_order_margin_bridge -> stage2_required_bridge
  2. c09_valuation_blowoff_high_mae_guardrail -> local_4b_watch_guard
  3. c09_metrology_quality_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Advanced-equipment vocabulary alone should not create Green.
- Verified order, delivery schedule, customer acceptance, utilization, OPM, EPS revision, or cash-flow bridge can justify Stage3-Yellow.
- High-MAE equipment blowoffs should be capped at event-cap/local 4B watch.
```
