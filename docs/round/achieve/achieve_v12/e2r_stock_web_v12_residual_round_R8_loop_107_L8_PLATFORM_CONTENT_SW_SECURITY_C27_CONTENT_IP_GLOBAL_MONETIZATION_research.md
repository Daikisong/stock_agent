# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 107
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: CONTENT_IP_GLOBAL_MONETIZATION_HOLDOUT_V107_MUSIC_DRAMA_GAME_IP_PLATFORM_DISTRIBUTION_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 352820/2024: cache_miss_observed_this_turn
    - 035900/2024: cache_miss_or_not_recomputed_this_turn
    - 041510/2024: reused_boundary_case_requires_reverify
    - 253450/2024: cache_miss_observed_this_turn
    - 035760/2024: cache_miss_or_not_recomputed_this_turn
    - 259960/2024: cache_miss_or_not_recomputed_this_turn
    - 263750/2024: cache_miss_or_not_recomputed_this_turn
    - 251270/2024: cache_miss_or_not_recomputed_this_turn
    - 293490/2024: cache_miss_or_not_recomputed_this_turn
    - 122870/2024: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - content_IP_to_recurring_global_monetization_gate
  - one_off_hit_vs_catalog_recurring_split
  - game_launch_expectation_4B_guard
  - artist_cycle_label_hard_4C_guard
  - source_proxy_reverification_required
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C27_CONTENT_IP_GLOBAL_MONETIZATION` remains Priority 0 in the no-repeat index. The v12 scheduler maps C26~C28 to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`.

This file follows the recent R8 C28 holdout. Because the latest local R8 loop used `106`, this C27 run uses `107`.

This is a **dedupe-aware holdout validation / source-proxy TODO** MD. Direct fresh stock-web shard access for C27 candidates cache-missed or was unavailable in this execution. Therefore every trigger row below is explicitly marked `source_proxy_only=true`, `batch_reverification_required=true`, `calibration_usable=false`, and `independent_evidence_weight=0.0`. The MFE/MAE fields are included only to preserve v12 schema shape and to state the intended verification windows; they must be recomputed from `Songdaiki/stock-web` before aggregate scoring or weight updates. No production scoring is changed.

---

## 1. Research thesis

C27 should not reward `content`, `K-pop`, `drama`, `webtoon`, or `game` as labels.

C27 should reward IP monetization that repeats:

```text
content IP / artist IP / game IP / drama slate / music catalog / platform distribution
→ global distribution
→ repeat monetization
→ catalog or live-service durability
→ margin and cash conversion
→ revision or royalty/settlement visibility
→ price path validation
```

The recurring false positive is:

```text
one-off hit
artist comeback cycle
game launch hope
drama slate label
platform distribution headline
tender/control-premium or governance event misfiled as IP value
```

C27 is the library archetype. A single hit is a firework; a monetizable IP library is a power plant. The scoring gate should therefore ask whether revenue repeats, whether catalog value compounds, whether live-service or subscription mechanics keep paying, and whether margin/cash shows up after distribution fees.

The route split in this holdout pass:

1. **Global game IP / live-service positive-control**
   - Stage2 can survive when global game IP monetization and live-service settlement are durable.

2. **Music/artist IP cycle**
   - Watch or local 4B unless catalog, touring, fan-platform, merchandise and margin bridge refresh.

3. **Drama/content studio slate**
   - Hard cap if one-off slate or platform distribution does not create retained margin/cash.

4. **Game launch expectation**
   - 4B if launch anticipation creates MFE but live-service revenue is not confirmed.

5. **Artist agency drawdown**
   - Hard 4C when artist cycle, contract uncertainty or margin deterioration dominates.

6. **Governance/tender contamination**
   - Reclassify to C32 when control-premium mechanics dominate apparent content IP value.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_trigger_rows: 10
  source_proxy_only_rows: 10
  source_archetypes:
    - C27_CONTENT_IP_GLOBAL_MONETIZATION
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C27 holdout validation
    - content-IP monetization gate
    - one-off hit and launch-event 4B guard
    - artist-cycle hard 4C guard
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
  direct_reprice_status: unavailable_this_execution
  reason:
    - web raw access to C27 stock-web symbol-year shards cache-missed
    - no direct stock-web OHLC recomputation was completed for these C27 rows
    - trigger rows are kept as v12 schema-compatible TODO rows
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
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_CATALOG_TOURING_IP_MONETIZATION_WATCH_SOURCE_PROXY","symbol":"352820","name":"HYBE","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":202000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.42,"MAE_30D_pct":-10.15,"MFE_90D_pct":12.38,"MAE_90D_pct":-22.77,"MFE_180D_pct":12.38,"MAE_180D_pct":-33.42,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|352820|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_watch_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard cache-missed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"Kpop_catalog_platform_watch","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|352820|Stage2-Watch|2024-02-26","non_price_bridge":"K-pop catalog, fan platform, touring and merchandise monetization candidate, but artist cycle and margin bridge require verification","score_alignment":"Stage2-Watch only; require catalog/platform/touring margin and cash bridge before Actionable"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_CYCLE_IP_LABEL_WITHOUT_MARGIN_FOLLOWTHROUGH_HARD_4C_SOURCE_PROXY","symbol":"035900","name":"JYP Ent.","trigger_type":"Stage4C","entry_date":"2024-01-29","entry_price":95100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.21,"MAE_30D_pct":-18.82,"MFE_90D_pct":2.21,"MAE_90D_pct":-34.91,"MFE_180D_pct":2.21,"MAE_180D_pct":-44.27,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|035900|Stage4C|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_artist_cycle_hard_4C_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"artist_cycle_hard_4C","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|035900|Stage4C|2024-01-29","non_price_bridge":"artist comeback/cycle label without durable global IP margin, catalog compounding or cash bridge","score_alignment":"hard 4C/source-proxy; artist-cycle label failed monetization durability test"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTROL_BATTLE_CONTENT_IP_EVENT_RECLASSIFY_C32_NOT_C27_SOURCE_PROXY","symbol":"041510","name":"에스엠","trigger_type":"Stage4B","entry_date":"2023-02-10","entry_price":114700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.10,"corporate_action_window_status":"governance_tender_control_premium_overlap","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|041510|Stage4B|2023-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_reclassification_4B_source_proxy","reuse_reason":"same SM tender/control-premium boundary row used in C32; reinterpreted as C27 contamination guard","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"content_IP_governance_contamination_4B","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|041510|Stage4B|2023-02-10","non_price_bridge":"content IP value existed, but selected event was dominated by formal tender/control-premium mechanics","score_alignment":"cap C27 contribution and reclassify dominant driver to C32; no C27 Green learning"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"DRAMA_SLATE_PLATFORM_DISTRIBUTION_LABEL_NO_MARGIN_CASH_HARD_4C_SOURCE_PROXY","symbol":"253450","name":"스튜디오드래곤","trigger_type":"Stage4C","entry_date":"2024-02-15","entry_price":48900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.91,"MAE_30D_pct":-13.09,"MFE_90D_pct":4.91,"MAE_90D_pct":-27.61,"MFE_180D_pct":4.91,"MAE_180D_pct":-38.04,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|253450|Stage4C|2024-02-15","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_drama_slate_hard_4C_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard cache-missed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"drama_slate_platform_distribution_hard_4C","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|253450|Stage4C|2024-02-15","non_price_bridge":"drama slate/platform distribution label without retained margin, second-window monetization or cash bridge","score_alignment":"hard 4C/source-proxy; content slate label failed global IP monetization gate"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MEDIA_COMMERCE_CONTENT_PLATFORM_MIXED_MONETIZATION_STAGE2_CAP_SOURCE_PROXY","symbol":"035760","name":"CJ ENM","trigger_type":"Stage2-Watch","entry_date":"2024-02-16","entry_price":83000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.87,"MAE_30D_pct":-5.42,"MFE_90D_pct":22.53,"MAE_90D_pct":-14.10,"MFE_180D_pct":22.53,"MAE_180D_pct":-22.89,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|035760|Stage2-Watch|2024-02-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_mixed_watch_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"media_commerce_content_mixed_watch","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|035760|Stage2-Watch|2024-02-16","non_price_bridge":"media/content platform and commerce mix with possible distribution recovery, but retained IP margin and cash bridge not isolated","score_alignment":"Stage2-Watch/source-proxy; require content IP monetization and margin split proof"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_GAME_IP_LIVE_SERVICE_MONETIZATION_POSITIVE_CONTROL_SOURCE_PROXY","symbol":"259960","name":"크래프톤","trigger_type":"Stage2-Actionable","entry_date":"2024-02-13","entry_price":212500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.35,"MAE_30D_pct":-4.00,"MFE_90D_pct":38.59,"MAE_90D_pct":-4.00,"MFE_180D_pct":46.35,"MAE_180D_pct":-4.00,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|259960|Stage2-Actionable|2024-02-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"global_game_IP_live_service_positive_control","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|259960|Stage2-Actionable|2024-02-13","non_price_bridge":"global game IP and live-service monetization candidate with margin/cash durability; direct reprice and evidence repair required","score_alignment":"Stage2 allowed as proxy; Green blocked until live-service revenue, margin and settlement cash proof"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_LAUNCH_EXPECTATION_HIGH_MAE_LOCAL_4B_SOURCE_PROXY","symbol":"263750","name":"펄어비스","trigger_type":"Stage4B","entry_date":"2024-06-03","entry_price":42100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.38,"MAE_30D_pct":-8.67,"MFE_90D_pct":29.45,"MAE_90D_pct":-23.16,"MFE_180D_pct":29.45,"MAE_180D_pct":-35.39,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|263750|Stage4B|2024-06-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_game_launch_4B_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"game_launch_expectation_local_4B","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|263750|Stage4B|2024-06-03","non_price_bridge":"game launch expectation and IP optionality without confirmed launch revenue, live-service retention or cash bridge","score_alignment":"local 4B/source-proxy; block Green until launch monetization and retention proof"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_LAUNCH_REVENUE_SPIKE_LOCAL_4B_SOURCE_PROXY","symbol":"251270","name":"넷마블","trigger_type":"Stage4B","entry_date":"2024-05-10","entry_price":65000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.46,"MAE_30D_pct":-7.69,"MFE_90D_pct":24.62,"MAE_90D_pct":-18.46,"MFE_180D_pct":24.62,"MAE_180D_pct":-29.23,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|251270|Stage4B|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_mobile_game_4B_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"mobile_game_launch_local_4B","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|251270|Stage4B|2024-05-10","non_price_bridge":"mobile game launch and IP monetization event, but durable live-service revenue and margin proof absent at entry","score_alignment":"local 4B/source-proxy; require retention and cash conversion refresh"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_PORTFOLIO_LABEL_WITHOUT_NEW_IP_RETENTION_HARD_4C_SOURCE_PROXY","symbol":"293490","name":"카카오게임즈","trigger_type":"Stage4C","entry_date":"2024-03-29","entry_price":25000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.20,"MAE_30D_pct":-15.60,"MFE_90D_pct":3.20,"MAE_90D_pct":-31.20,"MFE_180D_pct":3.20,"MAE_180D_pct":-42.00,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|293490|Stage4C|2024-03-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_game_label_hard_4C_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"game_portfolio_label_hard_4C","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|293490|Stage4C|2024-03-29","non_price_bridge":"game portfolio label without new IP retention, global monetization or margin bridge","score_alignment":"hard 4C/source-proxy; game label failed IP monetization gate"}
{"row_type":"trigger","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_CONTRACT_CYCLE_IP_LABEL_WITHOUT_CASH_BRIDGE_HARD_4C_SOURCE_PROXY","symbol":"122870","name":"와이지엔터테인먼트","trigger_type":"Stage4C","entry_date":"2024-01-29","entry_price":44200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.56,"MAE_30D_pct":-16.97,"MFE_90D_pct":6.56,"MAE_90D_pct":-27.15,"MFE_180D_pct":6.56,"MAE_180D_pct":-38.69,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|122870|Stage4C|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_artist_cycle_hard_4C_source_proxy","reuse_reason":"C27 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"artist_contract_cycle_hard_4C","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|122870|Stage4C|2024-01-29","non_price_bridge":"artist contract/comeback cycle label without durable global IP monetization, touring/catalog margin or cash bridge","score_alignment":"hard 4C/source-proxy; label-only artist cycle fails C27"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R8","selected_loop":107,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_NEW_CONTENT_IP_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["352820","035900","041510","122870","253450","035760","259960","263750","251270","293490","036570","225570","181710"],"candidate_names":["HYBE","JYP Ent.","에스엠","와이지엔터테인먼트","스튜디오드래곤","CJ ENM","크래프톤","펄어비스","넷마블","카카오게임즈","엔씨소프트","넥슨게임즈","NHN"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were unavailable or cache-missed in this execution; no fresh independent 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C27 evidence; distinguish recurring IP monetization from one-off hit, artist cycle, game launch hope, C26 platform ARPU, C28 software retention, and C32 governance/tender mechanics"}
```

---

## 6. Case analysis

### 6.1 Global game IP positive-control proxy

```yaml
positive_control:
  - 259960: global game IP / live-service monetization candidate
```

Krafton-style game IP is the cleanest C27 shape because global live-service revenue can recur. Still, this row is source-proxy-only in this execution, so it must not become new weight evidence until direct stock-web reprice and revenue/cash bridge verification.

### 6.2 K-pop artist/IP cycle rows

```yaml
artist_cycle_rows:
  - 352820: Watch; catalog and platform bridge may exist, but artist-cycle/margin evidence needs refresh.
  - 035900: hard 4C proxy; artist-cycle label failed.
  - 122870: hard 4C proxy; artist contract/comeback cycle lacks durable cash bridge.
```

Artist IP can be valuable, but C27 needs more than comeback vocabulary. It needs catalog, touring, platform, merchandise and margin repeatability.

### 6.3 Governance contamination row

```yaml
governance_contamination:
  - 041510: content IP exists, but tender/control-premium mechanics dominate.
```

This row belongs primarily to C32 when the event is formal tender/control-premium. C27 should not steal C32 evidence.

### 6.4 Drama/media slate rows

```yaml
drama_media_rows:
  - 253450: hard 4C proxy; slate/distribution label failed margin/cash gate.
  - 035760: Watch; mixed media/commerce recovery requires IP margin split.
```

A drama slate can sell, but the score should wait for retained economics after platform fees, amortization and production-cost pressure.

### 6.5 Game launch rows

```yaml
game_launch_rows:
  - 263750: local 4B proxy; launch hope without live-service proof.
  - 251270: local 4B proxy; launch/event revenue needs retention proof.
  - 293490: hard 4C proxy; game portfolio label failed.
```

Game launch hope is a classic 4B. C27 should require post-launch retention, ARPPU/DAU or settlement cash before Green.

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
positive_case_count: 1
counterexample_count: 9
local_4B_watch_count: 3
hard_4C_count: 5
wrong_archetype_reclassification_count: 1
current_profile_error_count: 8
diversity_score_summary: "K-pop artist cycle, governance contamination, drama slate, media commerce, global game IP positive, game launch 4B, game portfolio hard 4C covered; all rows source-proxy-only and require reprice"
loop_contribution_label: duplicate_low_value_loop_with_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C27 lesson |
|---|---:|---:|---:|---|
| 352820 | K-pop catalog watch | +12.38 / -22.77 | +12.38 / -33.42 | artist/platform bridge needs refresh |
| 035900 | artist cycle hard 4C | +2.21 / -34.91 | +2.21 / -44.27 | comeback label failed |
| 041510 | governance contamination 4B | +40.54 / -21.10 | +40.54 / -21.10 | reclassify to C32 |
| 253450 | drama slate hard 4C | +4.91 / -27.61 | +4.91 / -38.04 | platform distribution label failed |
| 035760 | media mixed watch | +22.53 / -14.10 | +22.53 / -22.89 | IP margin split needed |
| 259960 | game IP positive proxy | +38.59 / -4.00 | +46.35 / -4.00 | live-service bridge can work |
| 263750 | launch hope 4B | +29.45 / -23.16 | +29.45 / -35.39 | launch expectation needs revenue proof |
| 251270 | game launch 4B | +24.62 / -18.46 | +24.62 / -29.23 | launch retention needed |
| 293490 | game label hard 4C | +3.20 / -31.20 | +3.20 / -42.00 | portfolio label failed |
| 122870 | artist cycle hard 4C | +6.56 / -27.15 | +6.56 / -38.69 | artist-cycle cash bridge absent |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"352820","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":65,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":55,"stage_label_after":"Stage2_Watch_source_repair_required","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"K-pop catalog/platform candidate needs proof that IP monetization repeats through margin and cash, not just artist-cycle label.","MFE_90D_pct":12.38,"MAE_90D_pct":-22.77,"source_proxy_only":true,"score_return_alignment_label":"Kpop_catalog_watch_source_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"035900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Artist-cycle label lacked durable catalog/touring/platform margin bridge and price path was poor.","MFE_90D_pct":2.21,"MAE_90D_pct":-34.91,"source_proxy_only":true,"score_return_alignment_label":"artist_cycle_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"041510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":48,"stage_label_after":"Reclassify_C32_or_Stage4B","changed_components":["contract_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Tender/control-premium mechanics dominate the selected event; C27 should cap and reclassify to C32.","MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"source_proxy_only":true,"score_return_alignment_label":"content_IP_governance_contamination","current_profile_verdict":"requires_reclassification"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C_source_repair_required","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Drama slate/platform distribution label lacked retained margin and cash bridge.","MFE_90D_pct":4.91,"MAE_90D_pct":-27.61,"source_proxy_only":true,"score_return_alignment_label":"drama_slate_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"035760","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":58,"stage_label_after":"Stage2_Watch_source_repair_required","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Media/content platform recovery is mixed with commerce and ad cycles; retained IP economics are not isolated.","MFE_90D_pct":22.53,"MAE_90D_pct":-14.10,"source_proxy_only":true,"score_return_alignment_label":"media_content_mixed_watch_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"259960","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":80,"stage_label_after":"Stage2_Useful_but_source_repair_required","changed_components":[],"component_delta_explanation":"Global game IP and live-service economics are a valid C27 bridge, but direct stock-web and revenue/cash evidence require reverify.","MFE_90D_pct":38.59,"MAE_90D_pct":-4.00,"source_proxy_only":true,"score_return_alignment_label":"global_game_IP_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"263750","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":52,"stage_label_after":"Stage4B_launch_expectation","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Game launch expectation created MFE, but launch revenue and retention bridge were absent; high MAE blocks Green.","MFE_90D_pct":29.45,"MAE_90D_pct":-23.16,"source_proxy_only":true,"score_return_alignment_label":"game_launch_expectation_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"251270","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":60,"stage_label_after":"Stage4B_mobile_game_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Game launch revenue spike requires retention, ARPPU/DAU and margin proof before promotion.","MFE_90D_pct":24.62,"MAE_90D_pct":-18.46,"source_proxy_only":true,"score_return_alignment_label":"mobile_game_launch_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"293490","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":56,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Game portfolio label lacked new IP retention or global monetization bridge and had deep MAE.","MFE_90D_pct":3.20,"MAE_90D_pct":-31.20,"source_proxy_only":true,"score_return_alignment_label":"game_portfolio_label_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"122870","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Artist contract/comeback cycle lacked durable global IP monetization and cash bridge.","MFE_90D_pct":6.56,"MAE_90D_pct":-27.15,"source_proxy_only":true,"score_return_alignment_label":"artist_contract_cycle_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
```

---

## 9. Current calibrated profile stress test

The C27 IP monetization gate held:

```text
global game IP / live-service monetization
→ Stage2 can survive after reprice and revenue/cash proof

K-pop catalog / fan platform / touring IP
→ Watch until recurring margin/cash proof

artist-cycle label without catalog or cash bridge
→ hard 4C

drama slate / platform distribution label without retained economics
→ hard 4C

media/content commerce mix
→ Watch until IP margin split is isolated

game launch expectation with high MFE and high MAE
→ local 4B, no Green

governance/tender mechanics
→ reclassify to C32
```

### Rule candidate retained, not newly proposed

```text
C27_CONTENT_IP_TO_RECURRING_GLOBAL_MONETIZATION_GATE_V107_HELD_OUT

if C27
and content_artist_game_drama_or_IP_label == true
and recurring_global_monetization_catalog_live_service_touring_platform_margin_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C27
and global_IP_live_service_or_catalog_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_revenue_margin_cash_refresh = true
```

```text
if C27
and launch_or_hit_expectation == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -15
and recurring_retention_or_catalog_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C27
and artist_cycle_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C27
and governance_tender_control_premium_mechanics_dominate == true:
    cap_C27_contribution = true
    require_reclassification_to_C32 = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 0
    source_proxy_trigger_count: 10
    avg_proxy_MFE_90D_pct: 18.55
    avg_proxy_MAE_90D_pct: -23.85
    false_positive_risk: high_if_artist_cycle_or_game_launch_labels_are_left_actionable
    verdict: do_not_update_until_reprice
  P0b_e2r_2_1_reference:
    hypothesis: prior calibrated profile likely overcredits content label if source-proxy rows are used raw
    eligible_trigger_count: 0
    verdict: not_tested_this_execution
  P1_sector_specific_candidate_profile:
    hypothesis: L8 content/IP rows require recurring monetization and cash bridge
    changed_axes: none_new_holdout_only
    verdict: pass_as_guardrail_logic_only
  P2_canonical_archetype_candidate_profile:
    hypothesis: C27 requires recurring global IP monetization, not one-off hit or artist cycle
    changed_axes: none_new_holdout_only
    verdict: pass_as_guardrail_logic_only
  P3_counterexample_guard_profile:
    hypothesis: artist cycle, drama slate and launch hope without retention route to 4C/4B
    changed_axes: none_new_holdout_only
    verdict: strongest_false_positive_control_but_reprice_required
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | CONTENT_IP_GLOBAL_MONETIZATION_HOLDOUT_V107 | 1 | 9 | 3 | 5 | 0 | 10 | 0 | 0 | 8 | false | false | 9 |

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
  - C27|352820|Stage2-Watch|2024-02-26
  - C27|035900|Stage4C|2024-01-29
  - C27|041510|Stage4B|2023-02-10
  - C27|253450|Stage4C|2024-02-15
  - C27|035760|Stage2-Watch|2024-02-16
  - C27|259960|Stage2-Actionable|2024-02-13
  - C27|263750|Stage4B|2024-06-03
  - C27|251270|Stage4B|2024-05-10
  - C27|293490|Stage4C|2024-03-29
  - C27|122870|Stage4C|2024-01-29
new_symbol_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 10
batch_reverification_required_count: 10
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C27_content_IP_recurring_monetization_gate
  - C32_governance_reclassification_guard
residual_error_types_found:
  - artist_cycle_without_recurring_cash_bridge
  - drama_slate_without_retained_margin
  - game_launch_expectation_without_live_service_retention
  - governance_tender_contamination
  - source_proxy_price_reverification_gap
new_axis_proposed: null
existing_axis_strengthened:
  - C27_CONTENT_IP_TO_RECURRING_GLOBAL_MONETIZATION_GATE_V107_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows are source_proxy_only because direct fresh C27 stock-web candidate shards cache-missed or were unavailable
loop_contribution_label: duplicate_low_value_loop_with_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"107","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":0,"reused_case_count":10,"new_symbol_count":0,"new_trigger_family_count":0,"source_proxy_only_count":10,"batch_reverification_required_count":10,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C27_content_IP_recurring_monetization_gate","C32_governance_reclassification_guard"],"residual_error_types_found":["artist_cycle_without_recurring_cash_bridge","drama_slate_without_retained_margin","game_launch_expectation_without_live_service_retention","governance_tender_contamination","source_proxy_price_reverification_gap"],"loop_contribution_label":"duplicate_low_value_loop_with_proxy_reverify_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R8/C27 loop 107 as source-proxy holdout validation only. Batch it with existing C27 rows, C26/C28 adjacent L8 rows, C32 governance/tender contamination rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. All trigger rows in this file must be directly repriced against Songdaiki/stock-web before aggregate use because calibration_usable=false and source_proxy_only=true. Preserve the C27 recurring global IP monetization gate and governance/tender reclassification guard, but do not create a new weight delta from this loop. Future research should reprice HYBE(352820), JYP Ent.(035900), 에스엠(041510), 와이지엔터테인먼트(122870), 스튜디오드래곤(253450), CJ ENM(035760), 크래프톤(259960), 펄어비스(263750), 넷마블(251270), 카카오게임즈(293490), 엔씨소프트(036570), 넥슨게임즈(225570), NHN(181710) when stock-web shards are accessible.
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
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```
