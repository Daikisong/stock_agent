# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 107
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_HOLDOUT_V107_SEARCH_TALKBIZ_CREATOR_COMMERCE_ADTECH_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 035420/2024: source_proxy_reverify_required_from_loop_106
    - 035720/2024: source_proxy_reverify_required_from_loop_106
    - 067160/2024: source_proxy_reverify_required_from_loop_106
    - 042000/2024: source_proxy_reverify_required_from_loop_106
    - 089600/2024: source_proxy_reverify_required_from_loop_106
    - 216050/2024: source_proxy_reverify_required_from_loop_106
    - 237820/2024: source_proxy_reverify_required_from_loop_106
    - 214270/2024: source_proxy_reverify_required_from_loop_106
    - 060250/2024: source_proxy_reverify_required_from_loop_106
    - 030000/2024: source_proxy_reverify_required_from_loop_106
    - 035600/2024: not_recomputed_this_turn_future_payment_platform_boundary
    - 064260/2024: not_recomputed_this_turn_future_payment_digital_boundary
    - 068790/2024: not_recomputed_this_turn_platform_noise_check
    - 032080/2024: not_recomputed_this_turn_adtech_boundary
    - 376300/2024: not_recomputed_this_turn_creator_platform_boundary
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - source_proxy_holdout_validation
  - duplicate_low_value_loop_marker
  - platform_ad_revenue_to_operating_leverage_gate
  - search_ads_and_commerce_take_rate_positive_proxy
  - creator_platform_ads_subscription_operating_leverage_proxy
  - talkbiz_ad_recovery_false_positive_guard
  - adtech_agency_low_MFE_high_MAE_hard_4C_guard
  - source_proxy_reverification_required
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` remains Priority 0 in the no-repeat index. The v12 scheduler maps C26~C28 to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`.

This file continues the local R8/C26 sequence after `R8/C26 loop 106`; selected loop is therefore `107`.

This is a **source-proxy-only holdout / reprice TODO** MD. Direct fresh `Songdaiki/stock-web` symbol-year shard recomputation for the C26 candidates was not completed in this execution. Therefore every trigger row below is explicitly marked:

```yaml
source_proxy_only: true
batch_reverification_required: true
calibration_usable: false
independent_evidence_weight: 0.0
do_not_count_as_new_case: true
```

The MFE/MAE fields below are included only to preserve the v12 row shape and to describe intended validation windows. They must be recomputed from `Songdaiki/stock-web` before aggregate scoring, promotion, or weight updates. No production scoring is changed.

---

## 1. Research thesis

C26 should not reward the words `platform`, `AI`, `ad recovery`, or `commerce` by themselves.

C26 should reward platform revenue only when the revenue recovery flows through the cost structure:

```text
search / display / commerce / creator platform / adtech / payment platform / media rep label
→ ad inventory or transaction volume
→ take-rate or ARPU
→ retention / traffic quality
→ fixed-cost absorption
→ operating leverage
→ margin and cash conversion
→ price path validation
```

The recurring false positive is:

```text
ad recovery label
AI platform story
commerce partnership headline
creator economy theme
payment volume beta
one-quarter margin rebound
ad agency multiple rerating
```

A platform has operating leverage only when extra revenue falls through the same cost base. A traffic rebound is the water rising; C26 asks whether the turbine spins. If the extra traffic is bought with promotions, low-margin payment processing, or one-off commerce subsidy, it is not clean C26 evidence.

The C26 route split:

```text
search / commerce / creator platform revenue + margin bridge
→ Stage2 can survive after reprice and evidence repair

traffic or ad recovery label with weak OPM proof
→ Stage2-Watch / cap

AI platform or commerce partnership with high MFE and high MAE
→ local 4B, no Green

talkbiz / display ad recovery with low MFE and deep MAE
→ hard 4C

adtech / agency label without retained platform take-rate
→ hard 4C

payment platform volume without take-rate / OPM leverage
→ cap or reclassify away from C26
```

The key distinction versus adjacent R8 archetypes:

```text
C26 asks: does platform traffic / ad inventory / GMV create operating leverage?
C27 asks: does content or game IP monetize repeatedly?
C28 asks: does software/security contract revenue renew and expand?
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_trigger_rows: 10
  source_proxy_only_rows: 10
  source_archetypes:
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C27_CONTENT_IP_GLOBAL_MONETIZATION
    - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C26 holdout validation
    - platform ad revenue / operating leverage gate
    - ad recovery false-positive guard
    - AI commerce theme 4B guard
    - proxy row reprice TODO
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows are blocked by default.
```

Local row provenance:

```yaml
row_provenance:
  mode: source_proxy_only_holdout
  direct_reprice_status: not_recomputed_this_execution
  reason:
    - C26 loop 107 intentionally reuses loop 106 source-proxy rows as a dedupe holdout
    - no direct stock-web OHLC recomputation was completed for these C26 rows in this execution
    - exact same_entry_group_id rows from loop 106 must be deduped during aggregate ingest
    - trigger rows are retained as v12 schema-compatible TODO rows
    - no row in this file should create new weight delta
  all_trigger_rows:
    source_proxy_only: true
    batch_reverification_required: true
    calibration_usable: false
    independent_evidence_weight: 0.0
    do_not_count_as_new_case: true
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_COMMERCE_AD_INVENTORY_OPERATING_LEVERAGE_WATCH_SOURCE_PROXY","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Watch","entry_date":"2024-02-02","entry_price":207000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.80,"MAE_30D_pct":-9.66,"MFE_90D_pct":8.94,"MAE_90D_pct":-17.15,"MFE_180D_pct":11.59,"MAE_180D_pct":-24.15,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|035420|Stage2-Watch|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_search_platform_watch_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"search_commerce_ad_inventory_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035420|Stage2-Watch|2024-02-02","non_price_bridge":"search ads, commerce take-rate, cloud/AI and platform cost leverage candidate, but OPM/traffic quality and cash bridge require reverify","score_alignment":"Stage2-Watch only; require ad inventory, take-rate, OPM and cash conversion proof before Actionable"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALKBIZ_PLATFORM_AD_RECOVERY_LABEL_WITHOUT_OPM_HARD_4C_SOURCE_PROXY","symbol":"035720","name":"카카오","trigger_type":"Stage4C","entry_date":"2024-02-02","entry_price":57000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.51,"MAE_30D_pct":-12.28,"MFE_90D_pct":3.51,"MAE_90D_pct":-28.95,"MFE_180D_pct":5.26,"MAE_180D_pct":-36.84,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|035720|Stage4C|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"talkbiz_ad_recovery_false_positive","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage4C|2024-02-02","non_price_bridge":"talkbiz/ad platform recovery label without clean OPM leverage, governance/risk cleanup or cash bridge","score_alignment":"hard 4C/source-proxy; ad recovery label failed without operating leverage proof"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"CREATOR_LIVE_PLATFORM_AD_SUBSCRIPTION_OPERATING_LEVERAGE_POSITIVE_SOURCE_PROXY","symbol":"067160","name":"SOOP","trigger_type":"Stage2-Actionable","entry_date":"2024-01-31","entry_price":100000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.00,"MAE_30D_pct":-6.50,"MFE_90D_pct":58.00,"MAE_90D_pct":-10.50,"MFE_180D_pct":70.00,"MAE_180D_pct":-17.00,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|067160|Stage2-Actionable|2024-01-31","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"creator_platform_operating_leverage_positive","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage2-Actionable|2024-01-31","non_price_bridge":"creator/live platform with ad, subscription, donation and traffic operating leverage candidate; margin and retention require reverify","score_alignment":"Stage2 proxy only; Green blocked until traffic quality, ARPU, OPM and cash proof are directly verified"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"COMMERCE_PLATFORM_PARTNERSHIP_GMV_OPERATING_LEVERAGE_HIGH_MAE_LOCAL_4B_SOURCE_PROXY","symbol":"042000","name":"카페24","trigger_type":"Stage4B","entry_date":"2024-06-19","entry_price":35500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.03,"MAE_30D_pct":-9.86,"MFE_90D_pct":84.51,"MAE_90D_pct":-24.65,"MFE_180D_pct":92.96,"MAE_180D_pct":-35.21,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|042000|Stage4B|2024-06-19","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_commerce_platform_4B_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"commerce_platform_partnership_local_4B","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|042000|Stage4B|2024-06-19","non_price_bridge":"commerce platform partnership/GMV operating leverage candidate, but high MAE and conversion proof gap require reverify","score_alignment":"local 4B proxy; high MFE cannot become Green without merchant retention, take-rate, OPM and cash proof"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_PLATFORM_MEDIAREP_WATCH_NO_RETENTION_PROOF_SOURCE_PROXY","symbol":"089600","name":"나스미디어","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":22000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.82,"MAE_30D_pct":-8.18,"MFE_90D_pct":9.09,"MAE_90D_pct":-18.64,"MFE_180D_pct":12.27,"MAE_180D_pct":-27.73,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|089600|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_adtech_watch_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"digital_ad_platform_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|089600|Stage2-Watch|2024-02-26","non_price_bridge":"digital ad platform/media rep candidate, but retained advertiser demand and OPM bridge not isolated","score_alignment":"Stage2-Watch/source-proxy; require ad spend recovery, take-rate and margin bridge"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"MOBILE_ADTECH_LABEL_LOW_MFE_HIGH_MAE_HARD_4C_SOURCE_PROXY","symbol":"216050","name":"인크로스","trigger_type":"Stage4C","entry_date":"2024-02-26","entry_price":14200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.23,"MAE_30D_pct":-14.79,"MFE_90D_pct":4.23,"MAE_90D_pct":-31.69,"MFE_180D_pct":4.23,"MAE_180D_pct":-39.44,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|216050|Stage4C|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"mobile_adtech_label_hard_4C","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|216050|Stage4C|2024-02-26","non_price_bridge":"mobile adtech label without retained advertiser demand, platform take-rate or operating leverage bridge","score_alignment":"hard 4C/source-proxy; low MFE and deep MAE reject C26 bridge"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PERFORMANCE_AD_AGENCY_LABEL_WITHOUT_PLATFORM_LEVERAGE_HARD_4C_SOURCE_PROXY","symbol":"237820","name":"플레이디","trigger_type":"Stage4C","entry_date":"2024-02-26","entry_price":7200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.64,"MAE_30D_pct":-18.06,"MFE_90D_pct":7.64,"MAE_90D_pct":-35.42,"MFE_180D_pct":7.64,"MAE_180D_pct":-45.83,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|237820|Stage4C|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"performance_ad_agency_hard_4C","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|237820|Stage4C|2024-02-26","non_price_bridge":"performance ad agency label without platform-scale inventory, take-rate or operating leverage bridge","score_alignment":"hard 4C/source-proxy; agency revenue should not be learned as platform operating leverage"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_MARKETING_THEME_NO_PLATFORM_RETENTION_HARD_4C_SOURCE_PROXY","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-02-26","entry_price":2760,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.80,"MAE_30D_pct":-22.46,"MFE_90D_pct":5.80,"MAE_90D_pct":-38.77,"MFE_180D_pct":5.80,"MAE_180D_pct":-49.28,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|214270|Stage4C|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"digital_marketing_theme_hard_4C","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|214270|Stage4C|2024-02-26","non_price_bridge":"digital marketing / ad theme without platform retention, recurring ad inventory or OPM leverage bridge","score_alignment":"hard 4C/source-proxy; marketing theme failed C26 operating leverage gate"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PAYMENT_PLATFORM_VOLUME_WITHOUT_TAKE_RATE_OPM_RECLASSIFICATION_CAP_SOURCE_PROXY","symbol":"060250","name":"NHN KCP","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":10400,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.62,"MAE_30D_pct":-12.50,"MFE_90D_pct":14.42,"MAE_90D_pct":-20.19,"MFE_180D_pct":17.31,"MAE_180D_pct":-29.81,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|060250|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_payment_reclassification_cap_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"payment_platform_reclassification_cap","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|060250|Stage2-Watch|2024-02-26","non_price_bridge":"payment platform volume candidate, but take-rate, OPM and platform operating leverage are not isolated","score_alignment":"cap C26 contribution; reclassify if dominant bridge is payment processing rather than ad/platform leverage"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_MACRO_RECOVERY_WITHOUT_PLATFORM_TAKE_RATE_STAGE2_CAP_SOURCE_PROXY","symbol":"030000","name":"제일기획","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":19000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.42,"MAE_30D_pct":-6.84,"MFE_90D_pct":12.63,"MAE_90D_pct":-10.53,"MFE_180D_pct":15.79,"MAE_180D_pct":-16.32,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C26|030000|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_agency_macro_watch_source_proxy","reuse_reason":"C26 source-proxy row reused from loop 106; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ad_agency_macro_recovery_cap","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|030000|Stage2-Watch|2024-02-26","non_price_bridge":"advertising agency macro recovery candidate, but platform ad inventory and take-rate leverage are not isolated","score_alignment":"Stage2-Watch/cap; agency recovery should not be learned as platform operating leverage without proof"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"C26_NEW_PLATFORM_AD_REVENUE_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["035420","035720","067160","042000","089600","216050","237820","214270","060250","030000","035600","064260","068790"],"candidate_names":["NAVER","카카오","SOOP","카페24","나스미디어","인크로스","플레이디","FSN","NHN KCP","제일기획","KG이니시스","다날","DMS-platform_noise_check"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were not recomputed in this execution; no fresh independent 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C26 evidence; distinguish platform ad operating leverage from C27 content/IP, C28 software retention, payment processing volume and agency macro recovery"}
```

---

## 6. Case analysis

### 6.1 Search / commerce platform watch

```yaml
row:
  - 035420: search ads, commerce take-rate, cloud/AI and platform cost leverage candidate
route: Stage2-Watch source-proxy
```

NAVER-like platform economics can fit C26, but the row should not be promoted unless ad inventory, take-rate, traffic quality, OPM and cash conversion are directly checked.

### 6.2 Talkbiz / platform ad recovery false positive

```yaml
row:
  - 035720: ad recovery label without clean OPM leverage
route: Stage4C source-proxy
```

Platform label alone is not enough. If the recovery is dragged by governance, non-core losses, subsidy costs or weak margin flow-through, C26 must hard-cap.

### 6.3 Creator / live platform positive-control proxy

```yaml
row:
  - 067160: creator platform, ad/subscription/donation operating leverage candidate
route: Stage2-Actionable proxy, Green blocked
```

This is the cleanest C26 shape in this proxy batch. The business can show operating leverage when traffic and paid participation flow through a fixed-cost platform. Direct reprice and evidence repair remain mandatory.

### 6.4 Commerce platform partnership 4B

```yaml
row:
  - 042000: commerce platform partnership/GMV operating leverage
route: local 4B
```

High MFE can appear when commerce distribution changes, but Green requires merchant retention, take-rate and OPM proof.

### 6.5 Adtech / agency hard 4C rows

```yaml
hard_4C_rows:
  - 216050: mobile adtech label
  - 237820: performance ad agency label
  - 214270: digital marketing theme
```

These rows protect the model from treating ad-agency cyclicality as platform leverage. Agency revenue can recover without retained platform economics.

### 6.6 Payment / agency reclassification caps

```yaml
reclassification_or_cap:
  - 060250: payment platform volume without isolated take-rate/OPM leverage.
  - 030000: agency macro recovery without platform take-rate leverage.
```

The row can be economically valid, but not clean C26 unless the operating leverage comes from platform take-rate economics.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 10
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 10
batch_reverification_required_count: 10
calibration_usable_case_count: 0
calibration_usable_trigger_count: 0
positive_case_count: 2
counterexample_count: 8
local_4B_watch_count: 1
hard_4C_count: 4
wrong_archetype_reclassification_count: 3
current_profile_error_count: 8
diversity_score_summary: "search/commerce platform watch, talkbiz hard 4C, creator platform positive proxy, commerce platform 4B, adtech hard 4C, digital marketing hard 4C, payment and agency reclassification caps covered; all rows source-proxy-only and require direct stock-web reprice"
loop_contribution_label: duplicate_low_value_loop_with_source_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C26 lesson |
|---|---:|---:|---:|---|
| 035420 | search/commerce watch | +8.94 / -17.15 | +11.59 / -24.15 | platform label needs OPM proof |
| 035720 | talkbiz hard 4C | +3.51 / -28.95 | +5.26 / -36.84 | ad recovery label failed |
| 067160 | creator platform positive proxy | +58.00 / -10.50 | +70.00 / -17.00 | traffic/ARPU leverage can work |
| 042000 | commerce platform 4B | +84.51 / -24.65 | +92.96 / -35.21 | partnership MFE needs take-rate proof |
| 089600 | ad platform watch | +9.09 / -18.64 | +12.27 / -27.73 | retained advertiser demand needed |
| 216050 | adtech 4C | +4.23 / -31.69 | +4.23 / -39.44 | adtech label failed |
| 237820 | agency 4C | +7.64 / -35.42 | +7.64 / -45.83 | agency revenue not platform leverage |
| 214270 | digital marketing 4C | +5.80 / -38.77 | +5.80 / -49.28 | theme failed |
| 060250 | payment cap | +14.42 / -20.19 | +17.31 / -29.81 | payment volume reclassify |
| 030000 | agency macro watch | +12.63 / -10.53 | +15.79 / -16.32 | agency macro, not platform take-rate |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":1,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":60,"stage_label_after":"Stage2_Watch_source_repair_required","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Search/commerce platform economics may fit C26, but ad inventory, take-rate and OPM bridge are not directly verified.","MFE_90D_pct":8.94,"MAE_90D_pct":-17.15,"source_proxy_only":true,"score_return_alignment_label":"search_commerce_platform_watch_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C_source_repair_required","changed_components":["contract_score","margin_bridge_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Talkbiz/ad recovery label lacked clean OPM leverage and price path was weak.","MFE_90D_pct":3.51,"MAE_90D_pct":-28.95,"source_proxy_only":true,"score_return_alignment_label":"talkbiz_ad_recovery_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":80,"stage_label_after":"Stage2_Useful_but_source_repair_required","changed_components":[],"component_delta_explanation":"Creator/live platform traffic and ARPU can produce operating leverage, but direct price and evidence repair are required.","MFE_90D_pct":58.00,"MAE_90D_pct":-10.50,"source_proxy_only":true,"score_return_alignment_label":"creator_platform_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"042000","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":59,"stage_label_after":"Stage4B_commerce_platform_reverify_required","changed_components":["contract_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Commerce platform partnership created MFE, but high MAE and unverified merchant/take-rate evidence block Green.","MFE_90D_pct":84.51,"MAE_90D_pct":-24.65,"source_proxy_only":true,"score_return_alignment_label":"commerce_platform_high_MAE_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"089600","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":45,"stage_label_after":"Stage2_cap_source_repair_required","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Digital ad platform/media rep candidate lacks retained advertiser demand and OPM leverage evidence.","MFE_90D_pct":9.09,"MAE_90D_pct":-18.64,"source_proxy_only":true,"score_return_alignment_label":"digital_ad_platform_watch_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"216050","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":56,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Mobile adtech label lacked retained demand and platform take-rate; low MFE/deep MAE blocks positive credit.","MFE_90D_pct":4.23,"MAE_90D_pct":-31.69,"source_proxy_only":true,"score_return_alignment_label":"mobile_adtech_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"237820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Performance ad agency label lacks platform-scale inventory and operating leverage.","MFE_90D_pct":7.64,"MAE_90D_pct":-35.42,"source_proxy_only":true,"score_return_alignment_label":"performance_ad_agency_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"214270","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":55,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":36,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Digital marketing theme failed platform retention and OPM leverage checks.","MFE_90D_pct":5.80,"MAE_90D_pct":-38.77,"source_proxy_only":true,"score_return_alignment_label":"digital_marketing_theme_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"060250","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":54,"stage_label_after":"Stage2_cap_reclassify_payment","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Payment volume requires take-rate/OPM proof and may belong outside C26 ad-platform leverage.","MFE_90D_pct":14.42,"MAE_90D_pct":-20.19,"source_proxy_only":true,"score_return_alignment_label":"payment_platform_reclassification_cap_proxy","current_profile_verdict":"requires_reclassification_or_reverify"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"030000","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":55,"stage_label_after":"Stage2_Watch_agency_cap","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Agency macro recovery lacks platform ad inventory or take-rate leverage bridge.","MFE_90D_pct":12.63,"MAE_90D_pct":-10.53,"source_proxy_only":true,"score_return_alignment_label":"ad_agency_macro_watch_proxy","current_profile_verdict":"reverify_before_use"}
```

---

## 9. Current calibrated profile stress test

The C26 platform-ad-operating-leverage gate held:

```text
search/commerce platform label
→ Watch until take-rate, OPM and traffic quality prove through

talkbiz/ad recovery label without OPM leverage
→ hard 4C

creator/live platform with traffic + ARPU + margin bridge
→ Stage2 can survive after reprice

commerce platform partnership with high MFE and high MAE
→ local 4B, no Green

adtech / agency / digital marketing labels
→ hard 4C unless platform take-rate and operating leverage are isolated

payment processing volume
→ cap or reclassify unless platform take-rate leverage is proven
```

### Rule candidate retained, not newly proposed

```text
C26_PLATFORM_AD_REVENUE_TO_OPERATING_LEVERAGE_GATE_V107_HELD_OUT

if C26
and platform_ad_commerce_AI_or_traffic_label == true
and ad_inventory_take_rate_ARPU_retention_OPM_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C26
and platform_revenue_operating_leverage_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_OPM_cash_reprice = true
```

```text
if C26
and AI_or_commerce_platform_theme == true
and MFE_90D_pct >= +40
and MAE_90D_pct <= -20
and retained_revenue_or_take_rate_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C26
and adtech_agency_or_marketing_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C26
and dominant_driver_belongs_to_C27_C28_payment_processing_or_agency_macro == true:
    cap_C26_contribution = true
    require_reclassification = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 0
    source_proxy_trigger_count: 10
    avg_proxy_MFE_90D_pct: 20.88
    avg_proxy_MAE_90D_pct: -25.10
    false_positive_risk: high_if_platform_or_ad_recovery_labels_are_left_actionable
    verdict: do_not_update_until_reprice
  P0b_e2r_2_1_reference:
    hypothesis: prior calibrated profile may overcredit ad/platform label if proxy rows are used raw
    eligible_trigger_count: 0
    verdict: not_tested_this_execution
  P1_sector_specific_candidate_profile:
    hypothesis: L8 platform rows require take-rate/ARPU/OPM/cash bridge
    changed_axes: none_new_holdout_only
    verdict: pass_as_guardrail_logic_only
  P2_canonical_archetype_candidate_profile:
    hypothesis: C26 requires operating leverage, not traffic or ad-recovery language
    changed_axes: none_new_holdout_only
    verdict: pass_as_guardrail_logic_only
  P3_counterexample_guard_profile:
    hypothesis: adtech/agency/payment labels without platform take-rate route to 4C/cap
    changed_axes: none_new_holdout_only
    verdict: strongest_false_positive_control_but_reprice_required
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_HOLDOUT_V107 | 2 | 8 | 1 | 4 | 0 | 10 | 0 | 0 | 8 | false | false | 27 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 10
calibration_usable_trigger_count: 0
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 10
source_proxy_only_count: 10
batch_reverification_required_count: 10
narrative_only_or_rejected_count: 10
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: reprice_all_rows_before_aggregate_use
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 10
reused_case_ids:
  - C26|035420|Stage2-Watch|2024-02-02
  - C26|035720|Stage4C|2024-02-02
  - C26|067160|Stage2-Actionable|2024-01-31
  - C26|042000|Stage4B|2024-06-19
  - C26|089600|Stage2-Watch|2024-02-26
  - C26|216050|Stage4C|2024-02-26
  - C26|237820|Stage4C|2024-02-26
  - C26|214270|Stage4C|2024-02-26
  - C26|060250|Stage2-Watch|2024-02-26
  - C26|030000|Stage2-Watch|2024-02-26
new_symbol_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 10
batch_reverification_required_count: 10
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C26_platform_ad_revenue_operating_leverage_gate
  - C27_C28_payment_agency_reclassification_guard
residual_error_types_found:
  - ad_recovery_label_without_OPM_bridge
  - commerce_platform_theme_without_take_rate_proof
  - adtech_agency_label_without_platform_inventory
  - payment_volume_misfile
  - source_proxy_price_reverification_gap
new_axis_proposed: null
existing_axis_strengthened:
  - C26_PLATFORM_AD_REVENUE_TO_OPERATING_LEVERAGE_GATE_V107_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows are source_proxy_only and reused from loop 106 because direct fresh C26 stock-web candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_source_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"107","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":0,"reused_case_count":10,"new_symbol_count":0,"new_trigger_family_count":0,"source_proxy_only_count":10,"batch_reverification_required_count":10,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C26_platform_ad_revenue_operating_leverage_gate","C27_C28_payment_agency_reclassification_guard"],"residual_error_types_found":["ad_recovery_label_without_OPM_bridge","commerce_platform_theme_without_take_rate_proof","adtech_agency_label_without_platform_inventory","payment_volume_misfile","source_proxy_price_reverification_gap"],"loop_contribution_label":"duplicate_low_value_loop_with_source_proxy_reverify_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R8/C26 loop 107 as source-proxy holdout validation only. Batch it with C26 loop 106, existing C26 rows, C27/C28 adjacent L8 rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. All trigger rows in this file must be directly repriced against Songdaiki/stock-web before aggregate use because calibration_usable=false and source_proxy_only=true. Preserve the C26 platform-ad-revenue-to-operating-leverage gate, AI/commerce-theme 4B guard, adtech/agency hard 4C guard, and payment/agency reclassification cap. Do not create a new weight delta from this loop. Future research should directly reprice NAVER(035420), 카카오(035720), SOOP(067160), 카페24(042000), 나스미디어(089600), 인크로스(216050), 플레이디(237820), FSN(214270), NHN KCP(060250), 제일기획(030000), KG이니시스(035600), 다날(064260), 와이즈버즈(273060), 엔비티(236810), 모비데이즈(363260) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R8
completed_loop: 107
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
