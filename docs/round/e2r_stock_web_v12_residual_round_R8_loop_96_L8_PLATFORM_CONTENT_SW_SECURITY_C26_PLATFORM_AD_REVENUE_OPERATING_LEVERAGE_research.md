# E2R Stock-Web v12 Residual Research — R8 loop 96 / L8 / C26

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 96
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: SEARCH_COMMERCE_LIVE_PLATFORM_AD_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_AND_ADREP_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - ad_revenue_operating_leverage_bridge_test
  - traffic_migration_guardrail
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

이번 파일은 `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` 전용 residual research다.

C26은 “광고 회복”, “플랫폼 트래픽”, “디지털 광고”, “AI/추천/커머스” 같은 label을 곧바로 Stage3-Green으로 올리는 bucket이 아니다. C26의 핵심은 플랫폼 표면의 traffic headline이 실제 ad load, take-rate, cost discipline, operating leverage로 번역되는지 확인하는 것이다.

```text
platform traffic / search-commerce / live-stream / digital ad recovery
  → monetizable inventory / ad load / take-rate / paid traffic quality
  → fixed-cost leverage / sales mix / operating margin
  → EPS revision or cash-flow bridge
  → stock-web 1D OHLC forward path
```

트래픽은 사람들이 광장에 모이는 장면이고, 광고 영업 레버리지는 그 광장에서 실제 상점 매출이 고정비를 넘어서기 시작하는 장면이다. C26은 “광장이 붐빈다”와 “상점이 돈을 번다”를 분리해야 한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["035420","035720","067160","089600","216050"],"profile_paths":["atlas/symbol_profiles/035/035420.json","atlas/symbol_profiles/035/035720.json","atlas/symbol_profiles/067/067160.json","atlas/symbol_profiles/089/089600.json","atlas/symbol_profiles/216/216050.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv","atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv","atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv","atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv","atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C26 at 36 rows and asks for platform ad revenue recovery plus operating leverage confirmation.
- Existing registry shows C26 parsed through `R8 loop 95`.
- This output uses `R8 loop 96`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file emphasizes search-commerce platform, messaging platform, live platform, media rep, and adtech false-stage families in one compressed C26 stress test.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C26-R8L96-01 | 035420 | NAVER | 2024-07-05 | 2024-07-05 | 168100 | 181600 | 151100 | 8.03% | -10.11% | Search-commerce ad recovery had controlled but limited MFE; requires margin/revision bridge before Green. |
| C26-R8L96-02 | 035720 | 카카오 | 2024-07-05 | 2024-07-05 | 41500 | 44000 | 32900 | 6.02% | -20.72% | Messaging/platform ad label lacked durable operating leverage; high-MAE counterexample. |
| C26-R8L96-03 | 067160 | SOOP | 2024-06-20 | 2024-06-20 | 117000 | 143800 | 84900 | 22.91% | -27.44% | Live platform traffic/ad/subscription optionality produced MFE but deep drawdown demands bridge proof. |
| C26-R8L96-04 | 089600 | 나스미디어 | 2024-07-09 | 2024-07-09 | 17170 | 18470 | 15200 | 7.57% | -11.47% | Media rep ad recovery label was tradable but not enough for Green without OPM/revision. |
| C26-R8L96-05 | 216050 | 인크로스 | 2024-06-12 | 2024-06-12 | 8330 | 8450 | 7120 | 1.44% | -14.53% | Adtech/performance marketing label failed to create operating leverage; false Stage2 family. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C26-R8L96-01","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_COMMERCE_AD_OPERATING_LEVERAGE_CONTROLLED_MFE","symbol":"035420","name":"NAVER","trigger_type":"search_commerce_ad_revenue_operating_leverage_controlled_mfe","trigger_date":"2024-07-05","entry_date":"2024-07-05","entry_price":168100,"peak_price":181600,"peak_date":"2024-07-12","trough_price":151100,"trough_date":"2024-08-05","mfe_pct":8.03,"mae_pct":-10.11,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_pending_margin_revision_bridge","residual_flag":"platform_ad_recovery_limited_mfe_needs_operating_leverage_bridge","dedupe_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|search_commerce_ad_revenue_operating_leverage_controlled_mfe|2024-07-05"}
{"row_type":"trigger","case_id":"C26-R8L96-02","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MESSAGING_PLATFORM_AD_RECOVERY_LABEL_HIGH_MAE_COUNTEREXAMPLE","symbol":"035720","name":"카카오","trigger_type":"messaging_platform_ad_recovery_label_high_mae","trigger_date":"2024-07-05","entry_date":"2024-07-05","entry_price":41500,"peak_price":44000,"peak_date":"2024-07-12","trough_price":32900,"trough_date":"2024-09-09","mfe_pct":6.02,"mae_pct":-20.72,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"counterexample_platform_label_without_margin_or_revision_bridge","dedupe_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|messaging_platform_ad_recovery_label_high_mae|2024-07-05"}
{"row_type":"trigger","case_id":"C26-R8L96-03","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_PLATFORM_TRAFFIC_AD_SUBSCRIPTION_OPERATING_LEVERAGE_HIGH_MAE","symbol":"067160","name":"SOOP","trigger_type":"live_platform_traffic_ad_subscription_operating_leverage_high_mae","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":117000,"peak_price":143800,"peak_date":"2024-07-11","trough_price":84900,"trough_date":"2024-08-05","mfe_pct":22.91,"mae_pct":-27.44,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_high_MAE_guardrail","residual_flag":"positive_MFE_but_traffic_migration_and_margin_bridge_must_be_verified","dedupe_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|live_platform_traffic_ad_subscription_operating_leverage_high_mae|2024-06-20"}
{"row_type":"trigger","case_id":"C26-R8L96-04","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MEDIA_REP_AD_RECOVERY_OPM_BRIDGE_REQUIRED","symbol":"089600","name":"나스미디어","trigger_type":"media_rep_ad_recovery_opm_bridge_required","trigger_date":"2024-07-09","entry_date":"2024-07-09","entry_price":17170,"peak_price":18470,"peak_date":"2024-07-17","trough_price":15200,"trough_date":"2024-09-10","mfe_pct":7.57,"mae_pct":-11.47,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_Yellow_watch_not_Green","residual_flag":"media_rep_recovery_label_requires_OPM_revision_bridge","dedupe_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|089600|media_rep_ad_recovery_opm_bridge_required|2024-07-09"}
{"row_type":"trigger","case_id":"C26-R8L96-05","round":"R8","loop":"96","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_PERFORMANCE_MARKETING_FALSE_STAGE2_LOW_MFE","symbol":"216050","name":"인크로스","trigger_type":"adtech_performance_marketing_false_stage2_low_mfe","trigger_date":"2024-06-12","entry_date":"2024-06-12","entry_price":8330,"peak_price":8450,"peak_date":"2024-06-20","trough_price":7120,"trough_date":"2024-07-05","mfe_pct":1.44,"mae_pct":-14.53,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_false_Stage2","residual_flag":"adtech_label_without_operating_leverage_low_mfe_high_mae","dedupe_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|adtech_performance_marketing_false_stage2_low_mfe|2024-06-12"}
```

## 6. Score-return alignment

### 6.1 Platform-core controlled path

`035420` is not a failure, but it is not a clean Green either. The price path after 2024-07-05 produced controlled but limited MFE. That fits a search-commerce ad recovery candidate where the model needs proof of cost discipline and advertising operating leverage, not just traffic or AI/search narrative.

### 6.2 Platform label high-MAE path

`035720` shows the platform label trap. The stock could briefly respond to platform/ad recovery sympathy, but the later path had much larger downside than upside. That is a classic C26 false Stage2 risk when the model cannot see real ad load, take-rate, or margin bridge.

### 6.3 Live platform optionality

`067160` has the strongest MFE in this sample, but also the deepest early MAE among the positive candidates. Live platform traffic migration and ad/subscription monetization can be real, but the position should not be promoted to Green until revenue quality and margin conversion are verified.

### 6.4 Media rep / adtech false positives

`089600` and `216050` show that ad recovery labels outside the dominant platform layer often need stricter proof. Media rep or adtech vocabulary can make a short spike, but without OPM/revision bridge the model should cap at Yellow/event-cap or local 4B watch.

## 7. Raw component score simulation

| symbol | platform/ad evidence | monetizable inventory | operating leverage | EPS/revision bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 035420 | 21 | 17 | 12 | 10 | 10 | -5 | 65 | Stage2/Yellow pending bridge |
| 035720 | 18 | 10 | 5 | 4 | 6 | -10 | 33 | Stage2/local 4B watch |
| 067160 | 20 | 18 | 13 | 9 | 19 | -13 | 66 | Stage3-Yellow with high-MAE guardrail |
| 089600 | 15 | 10 | 7 | 5 | 8 | -6 | 39 | Stage2/Yellow watch |
| 216050 | 12 | 7 | 3 | 2 | 1 | -8 | 17 | Event-cap / false Stage2 |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c26_platform_ad_requires_operating_leverage_revision_bridge","scope":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","candidate_action":"stage2_required_bridge","rule":"Do not promote platform/ad recovery labels above Stage2 unless monetizable inventory, ad load, take-rate, cost discipline, OPM, EPS revision, or cash-flow bridge is visible.","supporting_cases":["035720","089600","216050"],"counterbalanced_by":["035420","067160"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c26_high_mae_traffic_label_guardrail","scope":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","candidate_action":"local_4b_watch_guard","rule":"If platform traffic/ad-recovery MFE is paired with deep MAE and no margin bridge, cap at local 4B watch or event-cap until non-price evidence arrives.","supporting_cases":["035720","067160"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c26_mediarep_adtech_false_stage2_guard","scope":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","candidate_action":"false_stage2_block","rule":"Media rep/adtech labels require stronger OPM and revision evidence than platform-core names; otherwise treat as false Stage2 or event-cap.","supporting_cases":["089600","216050"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c26_live_platform_positive_delta","scope":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","candidate_action":"stage3_yellow_candidate_delta","rule":"Live-platform names with verified traffic migration, monetization quality, and margin bridge can receive stronger Stage3-Yellow treatment; Green requires drawdown containment.","supporting_cases":["067160"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","round":"R8","loop":"96","positive_rows":2,"counterexample_rows":3,"new_symbol_count":5,"primary_residual":"C26 needs stronger separation between platform/ad-recovery vocabulary and actual monetizable inventory, OPM, EPS revision, or cash-flow bridge.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","false_stage2_block","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","sample_count":5,"avg_mfe_pct":9.59,"avg_mae_pct":-16.85,"median_mfe_pct":7.57,"median_mae_pct":-14.53,"interpretation":"C26 ad-recovery labels often have limited upside unless operating leverage is real; live-platform optionality can work, but high-MAE guardrails are necessary."}
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
  - historical corporate-action profile caveats are outside the local 2024 trigger windows used here
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C26 R8 loop 96 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c26_platform_ad_requires_operating_leverage_revision_bridge -> stage2_required_bridge
  2. c26_high_mae_traffic_label_guardrail -> local_4b_watch_guard
  3. c26_mediarep_adtech_false_stage2_guard -> false_stage2_block
  4. c26_live_platform_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Platform traffic/ad-recovery vocabulary alone should not create Green.
- Monetizable inventory, ad load, take-rate, cost discipline, OPM, EPS revision, or cash-flow bridge can justify Stage3-Yellow.
- Media rep/adtech labels should be stricter than platform-core names unless OPM/revision is verified.
- Live-platform traffic migration can be constructive, but deep-MAE paths require sizing/staging guardrails.
```
