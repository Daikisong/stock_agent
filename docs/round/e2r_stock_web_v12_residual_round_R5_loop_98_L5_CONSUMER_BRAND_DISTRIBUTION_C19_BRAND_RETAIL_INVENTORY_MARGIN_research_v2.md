# E2R Stock-Web v12 Residual Research — R5 loop 98 / L5 / C19

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 98
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: CONVENIENCE_STORE_TRAFFIC_MIX_RETAIL_INVENTORY_MARGIN_BRIDGE_VS_HYPERMARKET_DEPARTMENT_STORE_VALUEUP_LOW_MFE_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - inventory_margin_guardrail
  - convenience_store_traffic_mix_margin_bridge_test
  - hypermarket_department_store_valueup_false_stage2_guard
  - channel_inventory_OPM_receivable_bridge_test
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

이번 파일은 `C19_BRAND_RETAIL_INVENTORY_MARGIN` 전용 residual research다.

C19는 “브랜드”, “리테일 반등”, “저PBR 유통주”, “편의점 안정 성장”, “대형마트/백화점 턴어라운드” 같은 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 매출 회복이 실제 sell-through, inventory days, markdown pressure, receivable quality, traffic/mix, gross margin, OPM/revision으로 내려오는지다.

```text
brand / retail / value-up / traffic headline
  → sell-through / traffic / product mix / same-store sales
  → inventory days / markdown / receivables / channel stuffing check
  → gross margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

리테일은 매장 문이 열렸다고 끝나는 장사가 아니다. 진짜 신호는 진열대가 비고, 할인 없이 다시 채워지고, 재고가 현금으로 바뀌는 속도다. C19는 “사람이 들어왔다”와 “마진이 남았다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["282330","007070","139480","023530"],"profile_paths":["atlas/symbol_profiles/282/282330.json","atlas/symbol_profiles/007/007070.json","atlas/symbol_profiles/139/139480.json","atlas/symbol_profiles/023/023530.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv","atlas/ohlcv_tradable_by_symbol_year/007/007070/2024.csv","atlas/ohlcv_tradable_by_symbol_year/139/139480/2024.csv","atlas/ohlcv_tradable_by_symbol_year/023/023530/2024.csv"],"validation_scope":"2024 trigger-level forward path; 282330/139480/023530 have zero corporate-action candidates; 007070 has 2021 and 2024-12-23 caveats, so selected 2024 path stops before the 2024-12-23 caveat window."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C19 at 24 rows, 6 rows short of the 30-row minimum stability zone.
- Existing registry shows C19 parsed through `R5 loop 97`.
- This output uses `R5 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C19 rows covered department store, duty-free, apparel, footwear, and fashion-inventory families. This file shifts to convenience-store traffic/mix, hypermarket value-up rebound, and department-store low-MFE retail false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C19-R5L98-01 | 282330 | BGF리테일 | 2024-08-01 | 2024-08-01 | 108300 | 125000 | 102700 | 15.42% | -5.17% | Convenience-store traffic/mix recovery path worked with contained MAE. |
| C19-R5L98-02 | 007070 | GS리테일 | 2024-08-02 | 2024-08-02 | 22450 | 23200 | 20050 | 3.34% | -10.69% | Convenience-store/retail label had weak MFE and needed OPM/channel proof. |
| C19-R5L98-03 | 139480 | 이마트 | 2024-01-29 | 2024-01-29 | 80900 | 88500 | 55600 | 9.39% | -31.27% | Hypermarket/value-up rebound failed without inventory, online-loss and OPM repair. |
| C19-R5L98-04 | 023530 | 롯데쇼핑 | 2024-02-01 | 2024-02-01 | 86000 | 92100 | 58100 | 7.09% | -32.44% | Department-store/retail value-up rebound was low-MFE/high-MAE; margin bridge required. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C19-R5L98-01","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_STORE_TRAFFIC_MIX_INVENTORY_MARGIN_BRIDGE","symbol":"282330","name":"BGF리테일","trigger_type":"convenience_store_traffic_mix_inventory_margin_bridge","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":108300,"peak_price":125000,"peak_date":"2024-09-25","trough_price":102700,"trough_date":"2024-08-01","mfe_pct":15.42,"mae_pct":-5.17,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_traffic_mix_OPM_URLs","residual_flag":"convenience_store_positive_path_but_requires_traffic_mix_inventory_margin_bridge","dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|282330|convenience_store_traffic_mix_inventory_margin_bridge|2024-08-01"}
{"row_type":"trigger","case_id":"C19-R5L98-02","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_STORE_RETAIL_LABEL_LOW_MFE_MARGIN_GUARD","symbol":"007070","name":"GS리테일","trigger_type":"convenience_store_retail_label_low_mfe_margin_guard","trigger_date":"2024-08-02","entry_date":"2024-08-02","entry_price":22450,"peak_price":23200,"peak_date":"2024-08-05","trough_price":20050,"trough_date":"2024-10-25","mfe_pct":3.34,"mae_pct":-10.69,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_OPM_channel_guard","residual_flag":"convenience_store_label_weak_MFE_without_OPM_inventory_bridge","dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|007070|convenience_store_retail_label_low_mfe_margin_guard|2024-08-02"}
{"row_type":"trigger","case_id":"C19-R5L98-03","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"HYPERMARKET_VALUEUP_REBOUND_INVENTORY_OPM_FALSE_STAGE2","symbol":"139480","name":"이마트","trigger_type":"hypermarket_valueup_rebound_inventory_opm_false_stage2","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":80900,"peak_price":88500,"peak_date":"2024-02-02","trough_price":55600,"trough_date":"2024-07-23","mfe_pct":9.39,"mae_pct":-31.27,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_false_Stage2","residual_flag":"hypermarket_valueup_rebound_failed_without_inventory_online_loss_OPM_repair","dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|139480|hypermarket_valueup_rebound_inventory_opm_false_stage2|2024-01-29"}
{"row_type":"trigger","case_id":"C19-R5L98-04","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_RETAIL_VALUEUP_LOW_MFE_HIGH_MAE_GUARD","symbol":"023530","name":"롯데쇼핑","trigger_type":"department_store_retail_valueup_low_mfe_high_mae_guard","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":86000,"peak_price":92100,"peak_date":"2024-02-13","trough_price":58100,"trough_date":"2024-08-05","mfe_pct":7.09,"mae_pct":-32.44,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_Stage2_with_inventory_margin_guard","residual_flag":"retail_valueup_label_low_MFE_high_MAE_without_inventory_margin_revision_bridge","dedupe_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|023530|department_store_retail_valueup_low_mfe_high_mae_guard|2024-02-01"}
```

## 6. Score-return alignment

### 6.1 Convenience-store positive but bridge-dependent

`282330` is the constructive C19 row in this sample. The forward path after the August entry created meaningful MFE with limited MAE. That supports a Stage3-Yellow candidate when traffic, mix, franchise economics, inventory quality, and OPM/revision are verified.

### 6.2 Same retail stability label, weaker conversion

`007070` is the caution row inside the convenience-store family. The move was tradable but weak; the later drawdown means a convenience-store label alone should not create Green. The model needs evidence that retail traffic and mix improvement actually reach gross margin and OPM.

### 6.3 Hypermarket / department-store value-up false Stage2

`139480` and `023530` are the main guardrail rows. Low-PBR or retail value-up rebound vocabulary produced short MFE, but inventory quality, markdowns, online losses, fixed-cost leverage, and OPM/FCF gaps dominated the forward path. These should remain local 4B or Stage2 until non-price repair is visible.

## 7. Raw component score simulation

| symbol | retail/brand evidence | sell-through/traffic | inventory/markdown | OPM/revision bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 282330 | 18 | 17 | 14 | 13 | 16 | -3 | 65 | Stage3-Yellow candidate |
| 007070 | 16 | 10 | 9 | 7 | 4 | -6 | 40 | Stage2/Yellow with guard |
| 139480 | 16 | 5 | 3 | 3 | 5 | -15 | 17 | Local 4B / false Stage2 |
| 023530 | 17 | 6 | 4 | 4 | 4 | -15 | 20 | Local 4B / Stage2 guard |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c19_retail_requires_sellthrough_inventory_OPM_bridge","scope":"C19_BRAND_RETAIL_INVENTORY_MARGIN","candidate_action":"stage2_required_bridge","rule":"Do not promote brand/retail/value-up labels above Stage2 unless sell-through, traffic, product mix, inventory days, markdown pressure, receivable quality, gross margin, OPM, or EPS revision bridge is visible.","supporting_cases":["007070","139480","023530"],"counterbalanced_by":["282330"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c19_convenience_store_positive_delta","scope":"C19_BRAND_RETAIL_INVENTORY_MARGIN","candidate_action":"stage3_yellow_candidate_delta","rule":"Convenience-store names with verified traffic, mix improvement, franchise economics, inventory quality, and OPM/revision bridge can receive Stage3-Yellow treatment.","supporting_cases":["282330"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c19_convenience_store_low_MFE_guard","scope":"C19_BRAND_RETAIL_INVENTORY_MARGIN","candidate_action":"stage2_to_yellow_with_OPM_channel_guard","rule":"Convenience-store retail rows with small MFE and later drawdown should remain Stage2/Yellow until OPM and channel/inventory evidence is verified.","supporting_cases":["007070"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c19_hypermarket_department_store_false_stage2_guard","scope":"C19_BRAND_RETAIL_INVENTORY_MARGIN","candidate_action":"local_4b_watch_guard","rule":"Hypermarket or department-store value-up rebounds with low MFE and high MAE should remain local 4B watch unless inventory, markdown, OPM and FCF repair evidence appears.","supporting_cases":["139480","023530"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","round":"R5","loop":"98","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C19 should separate traffic/mix-based convenience-store margin recovery from hypermarket and department-store value-up rebounds that lack inventory, markdown, OPM and FCF repair.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","stage2_to_yellow_with_OPM_channel_guard","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","sample_count":4,"avg_mfe_pct":8.81,"avg_mae_pct":-19.89,"median_mfe_pct":8.24,"median_mae_pct":-20.98,"interpretation":"C19 retail labels show poor asymmetry unless traffic/sell-through and inventory-to-OPM bridge are visible; convenience-store quality can work but still needs URL-verified margin evidence."}
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
- Ingest this C19 R5 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c19_retail_requires_sellthrough_inventory_OPM_bridge -> stage2_required_bridge
  2. c19_convenience_store_positive_delta -> stage3_yellow_candidate_delta
  3. c19_convenience_store_low_MFE_guard -> stage2_to_yellow_with_OPM_channel_guard
  4. c19_hypermarket_department_store_false_stage2_guard -> local_4b_watch_guard

Expected behavior:
- Brand/retail/value-up vocabulary alone should not create Green.
- Sell-through, traffic, product mix, inventory days, markdown pressure, receivable quality, gross margin, OPM, or EPS revision can justify Stage3-Yellow.
- Hypermarket/department-store low-MFE high-MAE rebounds should stay local 4B until inventory and margin evidence repairs the row.
```
