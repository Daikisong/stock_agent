# E2R Stock-Web v12 Residual Research — R5 loop 99 / L5 / C18

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 99
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_BRAND_CHANNEL_REBOUND_INVENTORY_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - export_channel_reorder_bridge_test
  - ODM_repeat_order_margin_bridge_test
  - brand_channel_inventory_false_stage2_guard
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

이번 파일은 `C18_CONSUMER_EXPORT_CHANNEL_REORDER` 전용 residual research다.

C18은 “수출 증가”, “해외 채널”, “K-beauty/K-food 확산”, “리오프닝 소비재”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 export/channel headline이 실제 reorder, sell-through, ODM/OEM 생산 반복, receivable quality, inventory burden, OPM/revision으로 내려오는지다.

```text
consumer export / channel expansion headline
  → sell-through / repeat order / distributor reorder
  → inventory days / receivables / channel stuffing check
  → gross margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

수출 채널은 매장 진열대와 비슷하다. 물건이 처음 깔리는 것은 입점이고, 진짜 실력은 다시 주문이 들어오는 순간이다. C18은 “진열됐다”와 “반복해서 팔린다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["192820","161890","241710","090430"],"profile_paths":["atlas/symbol_profiles/192/192820.json","atlas/symbol_profiles/161/161890.json","atlas/symbol_profiles/241/241710.json","atlas/symbol_profiles/090/090430.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv","atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv","atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv"],"validation_scope":"2024 trigger-level forward path; 192820 and 161890 have zero corporate-action candidates; 241710 caveats are 2018 and outside local 2024 windows; 090430 caveat is 2015 and outside local 2024 windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C18 at 33 rows and asks for export channel, reorder, repeat demand, and inventory-burden expansion.
- Existing registry shows C18 parsed through `R5 loop 98`.
- This output uses `R5 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C18 loop 98 emphasized K-food / instant noodle / icecream / health food. This file shifts the fine family to K-beauty ODM / brand channel reorder and inventory false-positive separation.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C18-R5L99-01 | 192820 | 코스맥스 | 2024-04-01 | 2024-04-01 | 130000 | 208000 | 120300 | 60.00% | -7.46% | ODM export/order channel rerating worked; reorder and OPM bridge candidate. |
| C18-R5L99-02 | 161890 | 한국콜마 | 2024-05-31 | 2024-05-31 | 64300 | 75000 | 56800 | 16.64% | -11.66% | ODM export reorder path was positive but drawdown requires staging and receivables check. |
| C18-R5L99-03 | 241710 | 코스메카코리아 | 2024-05-09 | 2024-05-09 | 44200 | 98500 | 41900 | 122.85% | -5.20% | ODM/channel reorder winner; strongest repeat-order positive in this sample. |
| C18-R5L99-04 | 090430 | 아모레퍼시픽 | 2024-04-30 | 2024-04-30 | 169500 | 200500 | 114600 | 18.29% | -32.39% | Brand/channel rebound had MFE but inventory/channel risk later dominated. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C18-R5L99-01","round":"R5","loop":"99","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_ODM_EXPORT_REORDER_MARGIN_BRIDGE","symbol":"192820","name":"코스맥스","trigger_type":"k_beauty_odm_export_reorder_margin_bridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":130000,"peak_price":208000,"peak_date":"2024-06-14","trough_price":120300,"trough_date":"2024-04-04","mfe_pct":60.00,"mae_pct":-7.46,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_reorder_OPM_URLs","residual_flag":"positive_ODM_export_channel_path_but_requires_sellthrough_reorder_receivable_margin_bridge","dedupe_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|192820|k_beauty_odm_export_reorder_margin_bridge|2024-04-01"}
{"row_type":"trigger","case_id":"C18-R5L99-02","round":"R5","loop":"99","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_ODM_REPEAT_ORDER_WITH_RECEIVABLE_GUARD","symbol":"161890","name":"한국콜마","trigger_type":"k_beauty_odm_repeat_order_with_receivable_guard","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":64300,"peak_price":75000,"peak_date":"2024-06-19","trough_price":56800,"trough_date":"2024-07-19","mfe_pct":16.64,"mae_pct":-11.66,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_reorder_margin_guard","residual_flag":"ODM_export_reorder_positive_but_staging_and_channel_receivables_required","dedupe_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|161890|k_beauty_odm_repeat_order_with_receivable_guard|2024-05-31"}
{"row_type":"trigger","case_id":"C18-R5L99-03","round":"R5","loop":"99","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_ODM_CHANNEL_REORDER_STRONG_POSITIVE","symbol":"241710","name":"코스메카코리아","trigger_type":"k_beauty_odm_channel_reorder_strong_positive","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":44200,"peak_price":98500,"peak_date":"2024-09-27","trough_price":41900,"trough_date":"2024-05-13","mfe_pct":122.85,"mae_pct":-5.20,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_exact_reorder_OPM_URLs","residual_flag":"strong_ODM_channel_reorder_path_but_exact_sellthrough_margin_URLs_required","dedupe_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|241710|k_beauty_odm_channel_reorder_strong_positive|2024-05-09"}
{"row_type":"trigger","case_id":"C18-R5L99-04","round":"R5","loop":"99","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"LARGE_BRAND_CHANNEL_REBOUND_INVENTORY_FALSE_STAGE2","symbol":"090430","name":"아모레퍼시픽","trigger_type":"large_brand_channel_rebound_inventory_false_stage2","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":169500,"peak_price":200500,"peak_date":"2024-05-31","trough_price":114600,"trough_date":"2024-10-31","mfe_pct":18.29,"mae_pct":-32.39,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"brand_channel_rebound_failed_without_repeat_sellthrough_inventory_margin_bridge","dedupe_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|090430|large_brand_channel_rebound_inventory_false_stage2|2024-04-30"}
```

## 6. Score-return alignment

### 6.1 ODM export/reorder winners

`192820` and `241710` are the constructive C18 family. The price path was not just “K-beauty theme” volatility; it behaved like the market was repricing repeat export orders, ODM production leverage, and margin expansion. These rows support a stronger Stage3-Yellow/Green candidate treatment after URL verification.

### 6.2 Reorder positive but staging-sensitive

`161890` worked, but the drawdown after entry was not trivial. This means the model should allow Yellow only when reorder quality, receivables, inventory, and OPM bridge are visible. ODM export channel strength is not a blanket Green signal.

### 6.3 Brand/channel rebound false Stage2

`090430` is the warning row. A large brand can produce a channel-rebound MFE, but if sell-through and inventory quality fail, the later MAE dominates. This is the classic C18 false-positive: export/channel vocabulary without repeat demand and clean inventory.

## 7. Raw component score simulation

| symbol | export/channel evidence | reorder/sell-through | inventory/receivables | OPM/revision bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 192820 | 22 | 18 | 14 | 16 | 22 | -4 | 78 | Stage3-Yellow/Green candidate |
| 161890 | 19 | 14 | 11 | 12 | 13 | -6 | 63 | Stage2→Yellow with guard |
| 241710 | 23 | 21 | 16 | 18 | 25 | -3 | 85 | Stage3-Yellow/Green candidate |
| 090430 | 17 | 6 | 4 | 5 | 6 | -15 | 23 | Stage2/local 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c18_export_channel_requires_reorder_sellthrough_margin_bridge","scope":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","candidate_action":"stage2_required_bridge","rule":"Do not promote consumer export/channel labels above Stage2 unless sell-through, distributor reorder, repeat demand, inventory days, receivable quality, gross margin, OPM, or EPS revision bridge is visible.","supporting_cases":["090430"],"counterbalanced_by":["192820","161890","241710"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c18_odm_reorder_positive_delta","scope":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"K-beauty ODM names with verified repeat export orders, clean receivables, and OPM/revision bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["192820","241710"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c18_reorder_positive_staging_guard","scope":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","candidate_action":"stage2_to_yellow_with_reorder_guard","rule":"ODM/channel names with positive MFE but double-digit MAE should require staged treatment and exact reorder/sell-through proof before promotion.","supporting_cases":["161890"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c18_large_brand_inventory_false_stage2_guard","scope":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","candidate_action":"local_4b_watch_guard","rule":"Large brand/channel rebound rows with later high MAE should remain local 4B watch when inventory and sell-through evidence are absent.","supporting_cases":["090430"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","round":"R5","loop":"99","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C18 should separate repeat export-channel reorder engines, especially ODMs, from large-brand channel rebound labels that fail when sell-through and inventory quality are weak.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_reorder_guard","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","sample_count":4,"avg_mfe_pct":54.45,"avg_mae_pct":-14.18,"median_mfe_pct":39.15,"median_mae_pct":-9.56,"interpretation":"C18 can produce very strong upside in ODM/channel reorder winners, but brand/channel rebound labels need inventory and sell-through guardrails to avoid false Stage2 paths."}
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
- Ingest this C18 R5 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c18_export_channel_requires_reorder_sellthrough_margin_bridge -> stage2_required_bridge
  2. c18_odm_reorder_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c18_reorder_positive_staging_guard -> stage2_to_yellow_with_reorder_guard
  4. c18_large_brand_inventory_false_stage2_guard -> local_4b_watch_guard

Expected behavior:
- Consumer export/channel vocabulary alone should not create Green.
- Sell-through, distributor reorder, repeat demand, inventory days, receivable quality, gross margin, OPM, or EPS revision can justify Stage3-Yellow.
- Brand rebound with high MAE should remain local 4B watch unless inventory and repeat-order evidence repairs the row.
```
