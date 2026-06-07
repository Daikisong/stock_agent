# E2R Stock-Web v12 Residual Research — R5 loop 98 / L5 / C20

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 98
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_BRIDGE_VS_LARGE_BRAND_CHANNEL_REBOUND_INVENTORY_DECAY
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - global_distribution_sellthrough_bridge_test
  - OPM_revision_bridge_test
  - large_brand_channel_inventory_false_stage2_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` 전용 residual research다.

C20은 “K-food”, “K-beauty”, “글로벌 유통”, “미국/중국/동남아 채널 확장”, “브랜드 인지도”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 글로벌 유통망 확대가 실제 sell-through, channel depth, distributor reorder, inventory quality, gross margin, OPM, EPS revision으로 내려오는지다.

```text
K-food / K-beauty global distribution headline
  → sell-through / distribution depth / repeat order
  → inventory days / receivables / channel stuffing check
  → gross margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

글로벌 유통은 해외 마트 진열대와 같다. 한 번 진열되는 것은 입장권이고, 진짜 가치는 매대가 비고 다시 채워지는 속도에서 나온다. C20은 “해외에 깔렸다”와 “해외에서 반복적으로 돈이 된다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["003230","271560","241710","090430"],"profile_paths":["atlas/symbol_profiles/003/003230.json","atlas/symbol_profiles/271/271560.json","atlas/symbol_profiles/241/241710.json","atlas/symbol_profiles/090/090430.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv","atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv","atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv"],"validation_scope":"2024 trigger-level forward path; 271560 has zero corporate-action candidates; 003230 caveat is 2003 and outside local 2024 window; 241710 caveats are 2018 and outside local 2024 window; 090430 caveat is 2015 and outside local 2024 window."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C20 at 33 rows and asks for K-food/K-beauty global distribution, sell-through, and OPM/revision expansion.
- Existing registry shows C20 parsed through `R5 loop 97`.
- This output uses `R5 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates instant-noodle global distribution, confectionery steady global channel, K-beauty ODM global distribution, and large-brand channel rebound decay.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C20-R5L98-01 | 003230 | 삼양식품 | 2024-04-19 | 2024-04-19 | 271000 | 718000 | 265000 | 164.94% | -2.21% | K-food global distribution and OPM/revision rerating worked explosively. |
| C20-R5L98-02 | 271560 | 오리온 | 2024-06-10 | 2024-06-10 | 97900 | 106700 | 90100 | 8.99% | -7.97% | Existing global channel helped but did not create high-conviction rerating without stronger revision bridge. |
| C20-R5L98-03 | 241710 | 코스메카코리아 | 2024-05-09 | 2024-05-09 | 44200 | 98500 | 41900 | 122.85% | -5.20% | K-beauty global distribution / ODM sell-through winner. |
| C20-R5L98-04 | 090430 | 아모레퍼시픽 | 2024-04-30 | 2024-04-30 | 169500 | 200500 | 114600 | 18.29% | -32.39% | Large brand/channel rebound failed when inventory and repeat sell-through proof was weak. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C20-R5L98-01","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_INSTANT_NOODLE_GLOBAL_DISTRIBUTION_OPM_REVISION_LEADER","symbol":"003230","name":"삼양식품","trigger_type":"k_food_instant_noodle_global_distribution_opm_revision_leader","trigger_date":"2024-04-19","entry_date":"2024-04-19","entry_price":271000,"peak_price":718000,"peak_date":"2024-06-19","trough_price":265000,"trough_date":"2024-04-19","mfe_pct":164.94,"mae_pct":-2.21,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_sellthrough_OPM_URLs","residual_flag":"strong_K_food_global_distribution_OPM_revision_path_but_exact_sellthrough_channel_URLs_required","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|k_food_instant_noodle_global_distribution_opm_revision_leader|2024-04-19"}
{"row_type":"trigger","case_id":"C20-R5L98-02","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"GLOBAL_CONFECTIONERY_CHANNEL_STEADY_BUT_LOW_RERATING","symbol":"271560","name":"오리온","trigger_type":"global_confectionery_channel_steady_but_low_rerating","trigger_date":"2024-06-10","entry_date":"2024-06-10","entry_price":97900,"peak_price":106700,"peak_date":"2024-06-18","trough_price":90100,"trough_date":"2024-07-03","mfe_pct":8.99,"mae_pct":-7.97,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_revision_guard","residual_flag":"global_channel_exists_but_OPM_revision_rerating_weak_without_fresh_sellthrough_evidence","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|271560|global_confectionery_channel_steady_but_low_rerating|2024-06-10"}
{"row_type":"trigger","case_id":"C20-R5L98-03","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_ODM_SELLTHROUGH_STRONG_POSITIVE","symbol":"241710","name":"코스메카코리아","trigger_type":"k_beauty_global_distribution_odm_sellthrough_strong_positive","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":44200,"peak_price":98500,"peak_date":"2024-09-27","trough_price":41900,"trough_date":"2024-05-13","mfe_pct":122.85,"mae_pct":-5.20,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_distribution_OPM_URLs","residual_flag":"strong_K_beauty_global_distribution_ODM_path_but_exact_sellthrough_and_margin_URLs_required","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|241710|k_beauty_global_distribution_odm_sellthrough_strong_positive|2024-05-09"}
{"row_type":"trigger","case_id":"C20-R5L98-04","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LARGE_BEAUTY_BRAND_GLOBAL_CHANNEL_REBOUND_INVENTORY_DECAY","symbol":"090430","name":"아모레퍼시픽","trigger_type":"large_beauty_brand_global_channel_rebound_inventory_decay","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":169500,"peak_price":200500,"peak_date":"2024-05-31","trough_price":114600,"trough_date":"2024-10-31","mfe_pct":18.29,"mae_pct":-32.39,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"large_brand_channel_rebound_failed_without_repeat_sellthrough_inventory_OPM_bridge","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|large_beauty_brand_global_channel_rebound_inventory_decay|2024-04-30"}
```

## 6. Score-return alignment

### 6.1 True global distribution winners

`003230` and `241710` are the constructive C20 family. The price paths show not merely theme participation but a market belief that overseas distribution, sell-through, and operating leverage were changing the earnings base. These rows support Stage3-Yellow/Green candidate treatment after exact URL verification.

### 6.2 Global channel without enough rerating

`271560` shows the steady-channel boundary case. The company has global distribution characteristics, but the selected 2024 trigger did not create strong price asymmetry. C20 should not over-score “global presence” without fresh sell-through and revision acceleration.

### 6.3 Large brand channel rebound trap

`090430` is the false Stage2 row. A major brand can produce a powerful channel-rebound story and short MFE, but if inventory quality, sell-through, and margin revision fail, the later path becomes high-MAE. This is exactly why C20 needs a sell-through and OPM bridge.

## 7. Raw component score simulation

| symbol | global distribution | sell-through / channel depth | inventory / receivables | OPM / revision bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 003230 | 24 | 22 | 18 | 23 | 25 | -1 | 91 | Stage3-Yellow/Green candidate |
| 271560 | 18 | 10 | 10 | 7 | 5 | -5 | 45 | Stage2/Yellow with revision guard |
| 241710 | 23 | 21 | 16 | 19 | 24 | -2 | 85 | Stage3-Yellow/Green candidate |
| 090430 | 19 | 7 | 4 | 5 | 6 | -15 | 26 | Stage2/local 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c20_global_distribution_requires_sellthrough_OPM_revision_bridge","scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","candidate_action":"stage2_required_bridge","rule":"Do not promote K-food/K-beauty/global-distribution labels above Stage2 unless sell-through, distribution depth, repeat order, inventory quality, receivable quality, gross margin, OPM, or EPS revision bridge is visible.","supporting_cases":["271560","090430"],"counterbalanced_by":["003230","241710"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c20_kfood_kbeauty_distribution_positive_delta","scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"K-food or K-beauty names with verified overseas sell-through, channel depth, operating leverage, and revision bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["003230","241710"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c20_global_presence_low_rerating_guard","scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","candidate_action":"stage2_to_yellow_with_revision_guard","rule":"Global presence alone should remain Stage2/Yellow when MFE is small and no fresh sell-through or OPM revision acceleration is visible.","supporting_cases":["271560"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c20_large_brand_inventory_false_stage2_guard","scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","candidate_action":"local_4b_watch_guard","rule":"Large beauty brand rebound rows with high MAE should remain local 4B watch when sell-through, channel inventory, and OPM bridge are weak.","supporting_cases":["090430"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","round":"R5","loop":"98","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C20 should separate true K-food/K-beauty global distribution engines with sell-through and OPM revision from global-presence labels or large-brand channel rebounds without inventory quality.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_revision_guard","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sample_count":4,"avg_mfe_pct":78.77,"avg_mae_pct":-11.94,"median_mfe_pct":70.57,"median_mae_pct":-6.59,"interpretation":"C20 can produce explosive upside when global sell-through and OPM revision are real, but global presence or large-brand rebound vocabulary alone creates weak or high-MAE paths."}
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
- Ingest this C20 R5 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c20_global_distribution_requires_sellthrough_OPM_revision_bridge -> stage2_required_bridge
  2. c20_kfood_kbeauty_distribution_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c20_global_presence_low_rerating_guard -> stage2_to_yellow_with_revision_guard
  4. c20_large_brand_inventory_false_stage2_guard -> local_4b_watch_guard

Expected behavior:
- K-food/K-beauty/global-distribution vocabulary alone should not create Green.
- Sell-through, distribution depth, repeat order, inventory quality, gross margin, OPM, or EPS revision can justify Stage3-Yellow.
- Large-brand channel rebound and global presence labels should be capped when MAE dominates or revision bridge is absent.
```
