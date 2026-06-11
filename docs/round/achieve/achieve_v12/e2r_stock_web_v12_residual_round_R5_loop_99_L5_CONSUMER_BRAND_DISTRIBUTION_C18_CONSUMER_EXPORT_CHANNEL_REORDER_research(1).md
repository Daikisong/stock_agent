# E2R Stock-Web v12 Residual Research — R5 loop 99 / L5 / C18

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 99
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_SAUCE_TUNA_SNACK_PLANT_BASED_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - reorder_sellthrough_margin_guardrail
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

C18은 “K-food 수출”, “해외 채널”, “글로벌 유통”이라는 단어를 곧바로 Green으로 바꾸는 bucket이 아니다. C18의 진짜 다리는 아래와 같다.

```text
export-channel / distributor expansion headline
  → reorder / repeat demand / sell-through
  → SKU expansion / channel depth
  → gross margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

수출 채널은 진열대와 같다. 진열대에 한 번 올라간 것은 “입점”이고, 같은 자리에 계속 채워지는 것은 “reorder”다. C18은 이 둘을 구분해야 한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["248170","049770","271560","017810"],"profile_paths":["atlas/symbol_profiles/248/248170.json","atlas/symbol_profiles/049/049770.json","atlas/symbol_profiles/271/271560.json","atlas/symbol_profiles/017/017810.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/248/248170/2024.csv","atlas/ohlcv_tradable_by_symbol_year/049/049770/2024.csv","atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv","atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv"],"validation_scope":"2024 trigger-level forward path; old corporate-action profile caveats outside local windows are not local rejection; inactive-like profile caveat on 049770 is post-2024 and does not block local 2024 path."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C18 at 33 rows and asks for export channel, reorder, repeat demand, and inventory-burden expansion.
- Existing registry shows C18 latest parsed file at `R5 loop 98`.
- This output uses `R5 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file intentionally shifts from prior ramen/ice-cream-heavy families toward sauce, processed tuna/food, global snack, and plant-based/health channel paths.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C18-R5L99-01 | 248170 | 샘표식품 | 2024-06-12 | 2024-06-12 | 33350 | 45500 | 27000 | 36.43% | -19.04% | Sauce/K-food export channel spike with real MFE but high-MAE; needs reorder/margin proof before Green. |
| C18-R5L99-02 | 049770 | 동원F&B | 2024-05-20 | 2024-05-20 | 40400 | 48900 | 39400 | 21.04% | -2.48% | Processed food/tuna channel path with cleaner MFE/MAE; candidate for reorder-margin bridge. |
| C18-R5L99-03 | 271560 | 오리온 | 2024-06-10 | 2024-06-10 | 97900 | 106700 | 81800 | 8.99% | -16.45% | Global snack channel label produced limited MFE and meaningful MAE; channel label alone is weak. |
| C18-R5L99-04 | 017810 | 풀무원 | 2024-05-17 | 2024-05-17 | 13760 | 18410 | 13250 | 33.79% | -3.71% | Plant-based/health/US-channel path with strong MFE and contained MAE; positive bridge candidate pending URLs. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C18-R5L99-01","round":"R5","loop":"99","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_SAUCE_EXPORT_CHANNEL_REORDER_HIGH_MAE","symbol":"248170","name":"샘표식품","trigger_type":"k_food_sauce_export_channel_reorder_high_mae","trigger_date":"2024-06-12","entry_date":"2024-06-12","entry_price":33350,"peak_price":45500,"peak_date":"2024-06-20","trough_price":27000,"trough_date":"2024-08-05","mfe_pct":36.43,"mae_pct":-19.04,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_high_MAE_guardrail","residual_flag":"positive_mfe_but_reorder_margin_bridge_required_before_green","dedupe_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|248170|k_food_sauce_export_channel_reorder_high_mae|2024-06-12"}
{"row_type":"trigger","case_id":"C18-R5L99-02","round":"R5","loop":"99","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"PROCESSED_FOOD_TUNA_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE","symbol":"049770","name":"동원F&B","trigger_type":"processed_food_tuna_export_channel_reorder_margin_bridge","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":40400,"peak_price":48900,"peak_date":"2024-06-17","trough_price":39400,"trough_date":"2024-06-03","mfe_pct":21.04,"mae_pct":-2.48,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_URLs","residual_flag":"cleaner_positive_asymmetry_if_reorder_margin_bridge_verified","dedupe_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|049770|processed_food_tuna_export_channel_reorder_margin_bridge|2024-05-20"}
{"row_type":"trigger","case_id":"C18-R5L99-03","round":"R5","loop":"99","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GLOBAL_SNACK_CHANNEL_LABEL_LOW_MFE_HIGH_MAE","symbol":"271560","name":"오리온","trigger_type":"global_snack_channel_label_low_mfe_high_mae","trigger_date":"2024-06-10","entry_date":"2024-06-10","entry_price":97900,"peak_price":106700,"peak_date":"2024-06-18","trough_price":81800,"trough_date":"2024-08-05","mfe_pct":8.99,"mae_pct":-16.45,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap_not_Green","residual_flag":"counterexample_global_channel_label_without_sellthrough_revision_bridge","dedupe_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|271560|global_snack_channel_label_low_mfe_high_mae|2024-06-10"}
{"row_type":"trigger","case_id":"C18-R5L99-04","round":"R5","loop":"99","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"PLANT_BASED_HEALTH_FOOD_US_CHANNEL_REORDER_BRIDGE","symbol":"017810","name":"풀무원","trigger_type":"plant_based_health_food_us_channel_reorder_bridge","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":13760,"peak_price":18410,"peak_date":"2024-06-14","trough_price":13250,"trough_date":"2024-05-21","mfe_pct":33.79,"mae_pct":-3.71,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_URLs","residual_flag":"positive_channel_reorder_candidate_but_requires_exact_sellthrough_margin_URLs","dedupe_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|017810|plant_based_health_food_us_channel_reorder_bridge|2024-05-17"}
```

## 6. Score-return alignment

### 6.1 Positive channel bridge candidates

`049770` and `017810` show the cleanest C18 behavior in this sample. Both have meaningful MFE with contained MAE. That pattern is consistent with a true channel/reorder bridge rather than a one-day consumer-label spike. Exact URL verification is still required before any production patch.

### 6.2 High-MAE positive path

`248170` shows why C18 needs staging. A sauce/K-food channel narrative can create a large MFE, but the follow-through can still pass through a deep drawdown. That is not an automatic Green; it is Stage2/Yellow with reorder and margin proof required.

### 6.3 Counterexample path

`271560` shows the weak version of a global snack channel label. The stock made limited MFE but later produced a larger MAE. When the model sees only “global channel” vocabulary without sell-through, SKU expansion, distributor reorder, or revision bridge, it should cap the row at event-cap or local 4B watch.

## 7. Raw component score simulation

| symbol | export/channel evidence | reorder/sell-through | margin/revision bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 248170 | 20 | 12 | 8 | 18 | -10 | 48 | Stage2/Yellow with high-MAE guardrail |
| 049770 | 18 | 16 | 14 | 17 | -2 | 63 | Stage3-Yellow candidate |
| 271560 | 16 | 7 | 5 | 5 | -9 | 24 | Event-cap / local 4B watch |
| 017810 | 19 | 17 | 13 | 20 | -3 | 66 | Stage3-Yellow candidate |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c18_export_channel_requires_reorder_sellthrough_margin_bridge","scope":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","candidate_action":"stage2_required_bridge","rule":"Do not promote consumer export/channel labels above Stage2 unless reorder, sell-through, SKU expansion, distributor depth, OPM, or EPS revision bridge is visible.","supporting_cases":["271560"],"counterbalanced_by":["049770","017810","248170"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c18_high_mae_channel_spike_guardrail","scope":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","candidate_action":"local_4b_watch_guard","rule":"If export-channel MFE is paired with deep MAE and no confirmed reorder/margin bridge, cap at Stage2/Yellow or local 4B watch until non-price bridge is verified.","supporting_cases":["248170","271560"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c18_reorder_margin_positive_delta","scope":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","candidate_action":"stage3_yellow_candidate_delta","rule":"If export channel evidence is paired with repeated reorder/sell-through and margin/revision bridge, allow stronger Stage3-Yellow treatment even without a large price breakout, subject to MAE guardrail.","supporting_cases":["049770","017810"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","round":"R5","loop":"99","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C18 needs stronger separation between export-channel label strength and verified reorder/sell-through/margin bridge, with MAE guardrails for sauce/global-snack label spikes.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","sample_count":4,"avg_mfe_pct":25.06,"avg_mae_pct":-10.42,"median_mfe_pct":27.42,"median_mae_pct":-10.08,"interpretation":"C18 can work when reorder/sell-through and margin bridge are real, but generic global-channel labels often generate low-MFE/high-MAE paths."}
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
  - 049770 has inactive-like profile status after 2025 but local 2024 path is usable as historical calibration row
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
  2. c18_high_mae_channel_spike_guardrail -> local_4b_watch_guard
  3. c18_reorder_margin_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Export-channel vocabulary alone should not create Green.
- Verified reorder, sell-through, SKU/channel depth, OPM, or EPS revision can justify Stage3-Yellow.
- Deep-MAE channel spikes should be capped at local 4B watch or event-cap until non-price bridge is verified.
```
