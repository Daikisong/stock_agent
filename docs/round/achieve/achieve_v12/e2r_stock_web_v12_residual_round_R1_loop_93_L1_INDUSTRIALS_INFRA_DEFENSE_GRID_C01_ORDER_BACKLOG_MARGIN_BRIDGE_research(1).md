# E2R Stock-Web v12 Residual Research — R1 loop 93 / L1 / C01

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 93
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_AND_LNG_MATERIAL_ORDER_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_HIGH_MAE_EVENT_CAP
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - backlog_to_margin_conversion_guardrail
  - order_headline_vs_margin_bridge_separation
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

이번 파일은 `C01_ORDER_BACKLOG_MARGIN_BRIDGE` 전용 residual research다.

C01은 “수주가 많다”, “수주잔고가 쌓였다”, “조선/기자재 cycle이 좋다”라는 headline을 그대로 Green으로 올리는 bucket이 아니다. 핵심은 수주잔고가 매출 인식, 공정 진행, 원가 통제, mix 개선, margin/revision으로 내려오는지다.

```text
order / backlog / slot visibility
  → delivery schedule / revenue recognition
  → cost-to-complete / mix / change-order protection
  → margin / cash conversion / EPS revision
  → stock-web 1D OHLC forward path
```

수주잔고는 공장 앞에 쌓인 일감이다. 하지만 일감이 이익으로 변하려면 컨베이어벨트가 막히지 않아야 한다. 원가가 새면 수주잔고는 매출이 아니라 미완성 제품 창고가 된다. C01은 “일감”과 “이익” 사이의 벨트를 보는 archetype이다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["329180","010140","042660","017960"],"profile_paths":["atlas/symbol_profiles/329/329180.json","atlas/symbol_profiles/010/010140.json","atlas/symbol_profiles/042/042660.json","atlas/symbol_profiles/017/017960.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv","atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv","atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv","atlas/ohlcv_tradable_by_symbol_year/017/017960/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C01 at 16 rows and asks for order backlog plus margin bridge success/failure separation.
- Existing registry shows C01 parsed through `R1 loop 92`.
- This output uses `R1 loop 93`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file intentionally avoids the prior top-covered C01 cluster and uses large shipbuilding plus LNG material backlog/margin cases.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C01-R1L93-01 | 329180 | HD현대중공업 | 2024-04-26 | 2024-04-26 | 139500 | 222500 | 127200 | 59.50% | -8.82% | Shipbuilding backlog plus margin conversion path worked strongly after order-cycle confirmation. |
| C01-R1L93-02 | 010140 | 삼성중공업 | 2024-03-14 | 2024-03-14 | 9010 | 12280 | 8440 | 36.29% | -6.33% | Large shipbuilder backlog/revision path worked, but needs cost/mix confirmation before Green. |
| C01-R1L93-03 | 042660 | 한화오션 | 2024-03-14 | 2024-03-14 | 27000 | 35300 | 24850 | 30.74% | -7.96% | Order/mix optionality produced MFE, but integration/cost and margin bridge must be proven. |
| C01-R1L93-04 | 017960 | 한국카본 | 2024-07-24 | 2024-07-24 | 12180 | 13350 | 10230 | 9.61% | -16.01% | LNG material backlog headline had MFE but weak asymmetry; margin/cash bridge required. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C01-R1L93-01","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_CONVERSION_LEADER","symbol":"329180","name":"HD현대중공업","trigger_type":"shipbuilding_backlog_margin_conversion_leader","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":139500,"peak_price":222500,"peak_date":"2024-08-09","trough_price":127200,"trough_date":"2024-05-20","mfe_pct":59.50,"mae_pct":-8.82,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_URLs","residual_flag":"positive_backlog_to_margin_path_but_requires_exact_margin_revision_evidence","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|329180|shipbuilding_backlog_margin_conversion_leader|2024-04-26"}
{"row_type":"trigger","case_id":"C01-R1L93-02","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_REVISION_BRIDGE","symbol":"010140","name":"삼성중공업","trigger_type":"shipbuilding_order_backlog_revision_bridge","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":9010,"peak_price":12280,"peak_date":"2024-07-26","trough_price":8440,"trough_date":"2024-04-12","mfe_pct":36.29,"mae_pct":-6.33,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_cost_mix_URLs","residual_flag":"positive_backlog_repricing_but_cost_to_complete_bridge_required","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|shipbuilding_order_backlog_revision_bridge|2024-03-14"}
{"row_type":"trigger","case_id":"C01-R1L93-03","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_NAVAL_COMMERCIAL_ORDER_MIX_OPTIONALITY_MARGIN_GUARD","symbol":"042660","name":"한화오션","trigger_type":"shipbuilding_order_mix_optionality_margin_guard","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":27000,"peak_price":35300,"peak_date":"2024-08-30","trough_price":24850,"trough_date":"2024-04-04","mfe_pct":30.74,"mae_pct":-7.96,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_margin_guardrail","residual_flag":"order_mix_positive_but_integration_cost_margin_bridge_required","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|shipbuilding_order_mix_optionality_margin_guard|2024-03-14"}
{"row_type":"trigger","case_id":"C01-R1L93-04","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"LNG_MATERIAL_BACKLOG_MARGIN_CASH_BRIDGE_HIGH_MAE","symbol":"017960","name":"한국카본","trigger_type":"lng_material_backlog_margin_cash_bridge_high_mae","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":12180,"peak_price":13350,"peak_date":"2024-08-20","trough_price":10230,"trough_date":"2024-08-05","mfe_pct":9.61,"mae_pct":-16.01,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"counterexample_material_backlog_label_without_durable_margin_cash_bridge","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|017960|lng_material_backlog_margin_cash_bridge_high_mae|2024-07-24"}
```

## 6. Score-return alignment

### 6.1 Shipbuilding backlog positive family

`329180` and `010140` show the constructive C01 path. The market was not only buying a single order announcement; it was repricing multi-year slot visibility, delivery schedule, mix, and margin normalization. These rows support a stronger C01 treatment when backlog and cost/mix evidence travel together.

### 6.2 Optionality but still bridge-dependent

`042660` produced meaningful MFE, but the evidence burden is different. Order mix and defense/naval optionality can help, yet integration costs, cost-to-complete, and margin recognition must be verified before a Green treatment.

### 6.3 Material backlog high-MAE case

`017960` shows the weaker side of the supply-chain backlog family. LNG material exposure can rally with shipbuilding order strength, but if the margin/cash conversion bridge is not visible, the asymmetry can deteriorate quickly.

## 7. Raw component score simulation

| symbol | backlog evidence | delivery/revenue bridge | margin/cost bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 329180 | 24 | 22 | 18 | 24 | -4 | 84 | Stage3-Yellow/Green candidate |
| 010140 | 22 | 19 | 16 | 20 | -3 | 74 | Stage3-Yellow candidate |
| 042660 | 20 | 16 | 11 | 18 | -5 | 60 | Stage2/Yellow with margin guard |
| 017960 | 15 | 9 | 5 | 5 | -9 | 25 | Stage2/local 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c01_backlog_requires_margin_cash_bridge","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","candidate_action":"stage2_required_bridge","rule":"Do not promote order/backlog headlines above Stage2 unless delivery schedule, revenue recognition, cost-to-complete, margin, cash conversion, or EPS revision bridge is visible.","supporting_cases":["017960"],"counterbalanced_by":["329180","010140","042660"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c01_shipbuilding_backlog_positive_delta","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Shipbuilding backlog with visible slot duration, higher-margin mix, and revision bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["329180","010140"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c01_order_mix_optionality_margin_guard","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","candidate_action":"stage2_to_yellow_with_margin_guardrail","rule":"Order/mix optionality names can be Yellow candidates, but Green requires integration-cost and margin-recognition confirmation.","supporting_cases":["042660"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c01_lng_material_backlog_high_mae_guard","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","candidate_action":"local_4b_watch_guard","rule":"Supply-chain backlog labels with high MAE and no proven margin/cash bridge should be capped at local 4B watch or event-cap.","supporting_cases":["017960"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","round":"R1","loop":"93","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C01 should separate multi-year shipbuilding backlog and margin conversion from order headline or supply-chain backlog labels without cash bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_margin_guardrail","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","sample_count":4,"avg_mfe_pct":34.04,"avg_mae_pct":-9.78,"median_mfe_pct":33.52,"median_mae_pct":-8.39,"interpretation":"C01 can produce strong upside when backlog converts to margin/revision, but supply-chain order labels need cash and margin proof to avoid 4B-watch paths."}
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
- Ingest this C01 R1 loop 93 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c01_backlog_requires_margin_cash_bridge -> stage2_required_bridge
  2. c01_shipbuilding_backlog_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c01_order_mix_optionality_margin_guard -> stage2_to_yellow_with_margin_guardrail
  4. c01_lng_material_backlog_high_mae_guard -> local_4b_watch_guard

Expected behavior:
- Order/backlog vocabulary alone should not create Green.
- Delivery schedule, revenue recognition, cost-to-complete, margin, cash conversion, or EPS revision can justify Stage3-Yellow/Green.
- Supply-chain backlog labels with high MAE need local 4B/event-cap treatment until non-price bridge is verified.
```
