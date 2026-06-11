# E2R Stock-Web v12 Residual Research — R5 loop 98 / L5 / C20

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R5
selected_loop: 98
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_ODM_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_BRIDGE_VS_LEGACY_BRAND_CHINA_REBOUND_HIGH_MAE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - sellthrough_opm_revision_guardrail
  - legacy_china_rebound_false_stage2_test
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

이번 파일은 `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` 전용 residual research다.

C20은 C18의 “수출 채널/재주문”보다 한 단계 넓다. 핵심은 K-beauty/K-food가 글로벌 유통망에서 실제 sell-through, OPM, EPS revision으로 번역되는지다. 그래서 C20은 단순한 “중국 리오프닝”, “화장품 rebound”, “브랜드 sympathy”를 그대로 Green으로 올리면 안 된다.

```text
K-beauty / K-food global distribution label
  → channel depth / sell-through / reorder
  → SKU expansion / geography diversification
  → OPM / EPS revision / cash conversion
  → stock-web 1D OHLC forward path
```

C20은 매대가 아니라 계산대다. 입점 뉴스가 매대에 상품을 올리는 일이라면, sell-through와 OPM은 계산대에서 돈이 찍히는 일이다. 이번 샘플은 이 두 순간을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["192820","161890","090430","051900"],"profile_paths":["atlas/symbol_profiles/192/192820.json","atlas/symbol_profiles/161/161890.json","atlas/symbol_profiles/090/090430.json","atlas/symbol_profiles/051/051900.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","atlas/ohlcv_tradable_by_symbol_year/161/161890/2024.csv","atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv"],"validation_scope":"2024 trigger-level forward path; old corporate-action profile caveats outside local windows are not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C20 at 33 rows and asks for K-food/K-beauty global distribution, sell-through, OPM/revision expansion.
- Existing registry shows C20 latest parsed file at `R5 loop 97`.
- This output uses `R5 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file intentionally separates ODM/global-distribution winners from legacy brand China-rebound or beauty-label sympathy paths.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C20-R5L98-01 | 192820 | 코스맥스 | 2024-05-10 | 2024-05-10 | 149900 | 208000 | 116000 | 38.76% | -22.62% | ODM/global beauty positive MFE, but deep MAE means Green requires sell-through/OPM/revision proof. |
| C20-R5L98-02 | 161890 | 한국콜마 | 2024-05-10 | 2024-05-10 | 55200 | 78700 | 49400 | 42.57% | -10.51% | Stronger ODM/global distribution path; better candidate when margin/revision bridge is verified. |
| C20-R5L98-03 | 090430 | 아모레퍼시픽 | 2024-04-30 | 2024-04-30 | 169500 | 200500 | 115900 | 18.29% | -31.62% | Legacy brand/China rebound label produced high MAE; needs channel diversification and margin bridge. |
| C20-R5L98-04 | 051900 | LG생활건강 | 2024-04-30 | 2024-04-30 | 420000 | 480000 | 321000 | 14.29% | -23.57% | Legacy cosmetics rebound with limited MFE versus deep MAE; event-cap counterexample. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C20-R5L98-01","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_CHANNEL_SELLTHROUGH_OPM_BRIDGE_HIGH_MAE","symbol":"192820","name":"코스맥스","trigger_type":"k_beauty_odm_global_channel_sellthrough_opm_bridge_high_mae","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":149900,"peak_price":208000,"peak_date":"2024-06-14","trough_price":116000,"trough_date":"2024-08-13","mfe_pct":38.76,"mae_pct":-22.62,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_high_MAE_guardrail","residual_flag":"positive_mfe_but_green_requires_sellthrough_opm_revision_bridge","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|192820|k_beauty_odm_global_channel_sellthrough_opm_bridge_high_mae|2024-05-10"}
{"row_type":"trigger","case_id":"C20-R5L98-02","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_DISTRIBUTION_MARGIN_REVISION_BRIDGE","symbol":"161890","name":"한국콜마","trigger_type":"k_beauty_odm_global_distribution_margin_revision_bridge","trigger_date":"2024-05-10","entry_date":"2024-05-10","entry_price":55200,"peak_price":78700,"peak_date":"2024-09-30","trough_price":49400,"trough_date":"2024-05-10","mfe_pct":42.57,"mae_pct":-10.51,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_URLs","residual_flag":"best_positive_path_if_OPM_EPS_revision_bridge_verified","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|161890|k_beauty_odm_global_distribution_margin_revision_bridge|2024-05-10"}
{"row_type":"trigger","case_id":"C20-R5L98-03","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BEAUTY_BRAND_CHINA_REBOUND_HIGH_MAE_COUNTEREXAMPLE","symbol":"090430","name":"아모레퍼시픽","trigger_type":"legacy_beauty_brand_china_rebound_high_mae","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":169500,"peak_price":200500,"peak_date":"2024-05-31","trough_price":115900,"trough_date":"2024-08-13","mfe_pct":18.29,"mae_pct":-31.62,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap_not_Green","residual_flag":"counterexample_legacy_china_rebound_without_durable_sellthrough_margin_bridge","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|legacy_beauty_brand_china_rebound_high_mae|2024-04-30"}
{"row_type":"trigger","case_id":"C20-R5L98-04","round":"R5","loop":"98","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_COSMETICS_CHINA_REBOUND_EVENT_CAP","symbol":"051900","name":"LG생활건강","trigger_type":"legacy_cosmetics_china_rebound_event_cap","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":420000,"peak_price":480000,"peak_date":"2024-05-23","trough_price":321000,"trough_date":"2024-08-05","mfe_pct":14.29,"mae_pct":-23.57,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"counterexample_legacy_brand_rebound_low_mfe_high_mae","dedupe_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|051900|legacy_cosmetics_china_rebound_event_cap|2024-04-30"}
```

## 6. Score-return alignment

### 6.1 ODM/global distribution positive family

`192820` and `161890` show that C20 works best when the market is not merely buying “beauty” but buying a global ODM/channel-margin story. The upside is large, especially for `161890`, but `192820` also shows that even a strong C20 name can suffer a deep drawdown after the first price burst. Green needs non-price proof.

### 6.2 Legacy brand false-positive family

`090430` and `051900` are useful counterexamples. Both can rally on China-rebound / legacy-brand beauty vocabulary, but without durable sell-through, geography diversification, OPM, and EPS revision bridge the forward path can become high-MAE. These should not be scored like ODM global-distribution winners.

### 6.3 Mechanism

C20 should behave like a distributor’s cash register. Brand fame gets a product into the shop. Sell-through and OPM prove customers are repeatedly taking it off the shelf at profitable prices. The model should reward the second mechanism, not just the first image.

## 7. Raw component score simulation

| symbol | global distribution evidence | sell-through/reorder | OPM/EPS revision bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 192820 | 22 | 15 | 14 | 19 | -11 | 59 | Stage3-Yellow with high-MAE guardrail |
| 161890 | 21 | 17 | 18 | 22 | -5 | 73 | Stage3-Yellow/Green candidate pending URLs |
| 090430 | 17 | 7 | 6 | 9 | -14 | 25 | Stage2/event-cap |
| 051900 | 15 | 6 | 5 | 7 | -12 | 21 | Stage2/local 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c20_global_distribution_requires_sellthrough_opm_revision_bridge","scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","candidate_action":"stage2_required_bridge","rule":"Do not promote K-beauty/K-food global distribution labels above Stage2 unless sell-through, reorder/channel depth, OPM, EPS revision, or cash conversion bridge is visible.","supporting_cases":["090430","051900"],"counterbalanced_by":["192820","161890"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c20_legacy_china_rebound_false_positive_guard","scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","candidate_action":"local_4b_watch_guard","rule":"Legacy beauty brand or China-rebound vocabulary should be capped at event-cap/local 4B watch when price confirmation is followed by high MAE and no margin/revision bridge.","supporting_cases":["090430","051900"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c20_odm_global_distribution_positive_delta","scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","candidate_action":"stage3_yellow_candidate_delta","rule":"ODM/global-distribution names with channel depth plus OPM/EPS revision bridge can receive stronger Stage3-Yellow treatment; Green requires drawdown and bridge verification.","supporting_cases":["192820","161890"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","round":"R5","loop":"98","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C20 needs sharper separation between ODM/global distribution with OPM/revision bridge and legacy beauty/China rebound labels with high-MAE decay.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","sample_count":4,"avg_mfe_pct":28.48,"avg_mae_pct":-22.08,"median_mfe_pct":28.53,"median_mae_pct":-23.09,"interpretation":"C20 can deliver large MFE, but the asymmetry is only attractive when sell-through and OPM/EPS revision bridge are visible; legacy rebound labels create high-MAE traps."}
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
  1. c20_global_distribution_requires_sellthrough_opm_revision_bridge -> stage2_required_bridge
  2. c20_legacy_china_rebound_false_positive_guard -> local_4b_watch_guard
  3. c20_odm_global_distribution_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- K-beauty/K-food global distribution vocabulary alone should not create Green.
- Verified sell-through, channel depth, OPM, EPS revision, or cash conversion can justify Stage3-Yellow.
- Legacy beauty/China rebound labels should be capped at event-cap/local 4B watch when high-MAE decay follows.
```
