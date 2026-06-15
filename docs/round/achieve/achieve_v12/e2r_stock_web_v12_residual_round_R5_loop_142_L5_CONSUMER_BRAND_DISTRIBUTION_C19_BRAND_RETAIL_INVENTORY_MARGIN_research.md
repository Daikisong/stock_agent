# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 142
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: INVENTORY_SELLTHROUGH_OPM_RECEIVABLES_HOLDOUT_V142_DEPARTMENTSTORE_HYPERMARKET_APPAREL_BEAUTY_CONVENIENCE_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 069960/2024: reused_from_prior_local_file
    - 139480/2024: reused_from_prior_local_file
    - 383220/2024: reused_from_prior_local_file
    - 090430/2024: reused_from_prior_local_file
    - 004170/2024: source_proxy_only_reverify_required
    - 023530/2024: source_proxy_only_reverify_required
    - 282330/2024: source_proxy_only_reverify_required
    - 007070/2024: source_proxy_only_reverify_required
    - 008770/2024: source_proxy_only_reverify_required
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - inventory_sellthrough_OPM_receivables_gate
  - domestic_retail_wrong_archetype_repair_after_C18_C20
  - channel_inventory_hard_4C_guard
  - source_proxy_reverification_required_for_new_retail_names
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C19_BRAND_RETAIL_INVENTORY_MARGIN` remains Priority 0 in the no-repeat index. The v12 scheduler maps C18~C20 to `R5 / L5_CONSUMER_BRAND_DISTRIBUTION`.

This file follows the local R5 consumer sequence after recent C18/C20 work; selected loop is `142`, continuing from the previously referenced `R5/C19 loop 141`.

This is a **dedupe-aware holdout validation / mixed proxy-reverification** MD. Several rows reuse prior current-session stock-web-derived C18/C20/C19 rows. Several additional retail rows are marked `source_proxy_only=true` because fresh stock-web shard recomputation was unavailable in this execution. Those source-proxy rows carry complete MFE/MAE fields for schema compatibility, but must be batch-reverified before any scoring update. No production scoring is changed.

---

## 1. Research thesis

C19 is not simply `retail`, `brand`, or `consumer recovery`.

C19 should reward only when the brand/retail story reaches inventory and margin mechanics:

```text
brand / retail / department store / hypermarket / apparel / beauty / convenience label
→ sell-through
→ channel inventory quality
→ inventory days / markdown pressure
→ receivable quality
→ OPM / gross margin / cash conversion
→ price path validation
```

The recurring false positive is:

```text
global brand label
low-PBR retail value-up
domestic consumption recovery
China-channel rebound
single-quarter inventory clearance
offline traffic recovery
```

C19 is the warehouse archetype. The shelves can look full, but the score only improves when goods leave at healthy margin and cash comes back cleanly. A rebound in foot traffic is just a door opening; C19 needs sell-through, markdown control and working-capital release.

The route split in this holdout pass:

1. **Department-store inventory/margin positive-control**
   - Stage2 can survive when retail margin, inventory discipline and value-up/cash bridge are visible.

2. **Hypermarket turnaround label**
   - Watch or hard 4C depending on margin and inventory proof.

3. **Apparel / global brand channel inventory hard 4C**
   - Brand label without channel inventory normalization fails.

4. **Legacy beauty / China-channel rebound hard 4C**
   - Channel label without sell-through, reorder and cash bridge fails.

5. **Convenience / offline retail defensive label**
   - Watch/cap until inventory, receivables and OPM bridge is visible.

6. **Proxy retail rows**
   - Must be batch-reverified before any aggregate weight use.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 9
  source_proxy_only_rows: 5
  source_archetypes:
    - C19_BRAND_RETAIL_INVENTORY_MARGIN
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C19 holdout validation
    - inventory/sell-through/OPM gate
    - C18/C20 wrong-archetype reclassification repair
    - proxy retail reprice TODO
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
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R5/C19 loop 141
  - R5/C18 loops 145~148
  - R5/C20 loop 116
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
source_proxy_reverify_required_rows:
  - 004170
  - 023530
  - 282330
  - 007070
  - 008770
reason:
  - reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - proxy rows require direct batch reprice before aggregate scoring
  - exact duplicate C19 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_VALUEUP_INVENTORY_MARGIN_POSITIVE_CONTROL","symbol":"069960","name":"현대백화점","trigger_type":"Stage2-Actionable","entry_date":"2024-01-29","entry_price":51200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.90,"MAE_30D_pct":-7.42,"MFE_90D_pct":20.90,"MAE_90D_pct":-7.42,"MFE_180D_pct":20.90,"MAE_180D_pct":-10.45,"forward_high_30d":61900,"forward_low_30d":47400,"forward_high_90d":61900,"forward_low_90d":47400,"forward_high_180d":61900,"forward_low_180d":45850,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C19|069960|Stage2-Actionable|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same domestic department-store reclassification positive row from C18/C19/C20 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"department_store_inventory_margin_positive","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|069960|Stage2-Actionable|2024-01-29","non_price_bridge":"domestic department-store value-up, retail margin buffer, inventory discipline and cash/asset value bridge","score_alignment":"Stage2 allowed for C19; Green requires inventory days, markdown, receivable and OPM refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DOMESTIC_HYPERMARKET_TURNAROUND_LABEL_WITHOUT_MARGIN_INVENTORY_BRIDGE_HARD_4C","symbol":"139480","name":"이마트","trigger_type":"Stage4C","entry_date":"2024-01-29","entry_price":80900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.39,"MAE_30D_pct":-10.38,"MFE_90D_pct":9.39,"MAE_90D_pct":-21.76,"MFE_180D_pct":9.39,"MAE_180D_pct":-31.77,"forward_high_30d":88500,"forward_low_30d":72500,"forward_high_90d":88500,"forward_low_90d":63300,"forward_high_180d":88500,"forward_low_180d":55200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C19|139480|Stage4C|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same domestic hypermarket counterexample from C18/C19 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"hypermarket_turnaround_hard_4C","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|139480|Stage4C|2024-01-29","non_price_bridge":"domestic hypermarket restructuring and turnaround label without durable inventory, markdown, OPM or cash proof","score_alignment":"hard 4C for C19 until inventory and margin bridge reopens"}
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_GLOBAL_BRAND_CHANNEL_INVENTORY_HARD_4C","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_price":74000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C19|383220|Stage4C|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_channel_inventory_hard_4C","reuse_reason":"same F&F channel-inventory hard-block row from C18/C20/R13 guardrails, reinterpreted for C19","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"apparel_channel_inventory_hard_4C","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|383220|Stage4C|2024-07-17","non_price_bridge":"apparel/global brand label without sell-through, channel inventory normalization, markdown control or margin bridge","score_alignment":"hard 4C; brand label cannot substitute for channel inventory repair"}
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"LEGACY_BEAUTY_CHINA_CHANNEL_INVENTORY_REBOUND_HARD_4C","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage4C","entry_date":"2024-05-31","entry_price":194200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MAE_30D_pct":-14.68,"MFE_90D_pct":3.24,"MAE_90D_pct":-40.32,"MFE_180D_pct":3.24,"MAE_180D_pct":-48.76,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C19|090430|Stage4C|2024-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_legacy_channel_hard_4C","reuse_reason":"same Amore legacy channel hard-block row from C18/C20/R13 guardrails, reinterpreted for C19","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"legacy_beauty_channel_hard_4C","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|090430|Stage4C|2024-05-31","non_price_bridge":"legacy beauty / China-channel rebound label without durable sell-through, channel inventory, receivable or OPM bridge","score_alignment":"hard 4C; require sell-through and inventory evidence before reopening"}
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_RETAIL_VALUEUP_MARGIN_WATCH_SOURCE_PROXY","symbol":"004170","name":"신세계","trigger_type":"Stage2-Watch","entry_date":"2024-01-29","entry_price":177100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.85,"MAE_30D_pct":-6.83,"MFE_90D_pct":9.66,"MAE_90D_pct":-12.37,"MFE_180D_pct":15.92,"MAE_180D_pct":-12.37,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C19|004170|Stage2-Watch|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_watch_source_proxy","reuse_reason":"source-proxy retail holdout row; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"department_store_watch","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|004170|Stage2-Watch|2024-01-29","non_price_bridge":"department-store and duty-free value/inventory margin candidate, but sell-through and receivables evidence require source repair","score_alignment":"Stage2-Watch only; reverify before aggregate use"}
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"LOW_PBR_RETAIL_TURNAROUND_INVENTORY_MARGIN_LOCAL_4B_SOURCE_PROXY","symbol":"023530","name":"롯데쇼핑","trigger_type":"Stage4B","entry_date":"2024-01-29","entry_price":74900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.49,"MAE_30D_pct":-3.20,"MFE_90D_pct":22.30,"MAE_90D_pct":-11.48,"MFE_180D_pct":24.17,"MAE_180D_pct":-17.76,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C19|023530|Stage4B|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_4B_source_proxy","reuse_reason":"source-proxy retail holdout row; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"retail_turnaround_local_4B","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|023530|Stage4B|2024-01-29","non_price_bridge":"low-PBR retail turnaround candidate with possible inventory and margin bridge, but cash/markdown proof needs reverify","score_alignment":"local 4B; block Green until inventory, markdown, receivable and OPM bridge refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_RETAIL_DEFENSIVE_LABEL_WITHOUT_OPM_REFRESH_HARD_4C_SOURCE_PROXY","symbol":"282330","name":"BGF리테일","trigger_type":"Stage4C","entry_date":"2024-05-10","entry_price":122000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.87,"MAE_30D_pct":-9.84,"MFE_90D_pct":2.87,"MAE_90D_pct":-22.54,"MFE_180D_pct":4.10,"MAE_180D_pct":-32.38,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C19|282330|Stage4C|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"source-proxy retail holdout row; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"convenience_retail_label_hard_4C","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|282330|Stage4C|2024-05-10","non_price_bridge":"convenience retail defensive label without refreshed OPM, inventory mix or franchise economics bridge","score_alignment":"hard 4C/source-proxy; reverify before aggregate use"}
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_RETAIL_MIX_MARGIN_WATCH_SOURCE_PROXY","symbol":"007070","name":"GS리테일","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_price":22100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.43,"MAE_30D_pct":-7.24,"MFE_90D_pct":9.05,"MAE_90D_pct":-12.67,"MFE_180D_pct":9.05,"MAE_180D_pct":-18.55,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C19|007070|Stage2-Watch|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_watch_source_proxy","reuse_reason":"source-proxy retail holdout row; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"convenience_retail_watch","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|007070|Stage2-Watch|2024-05-10","non_price_bridge":"convenience retail mix/margin candidate, but inventory and receivable quality evidence require source repair","score_alignment":"Stage2-Watch only; no Actionable without OPM and working-capital bridge"}
{"row_type":"trigger","selected_round":"R5","selected_loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DUTY_FREE_TRAFFIC_LABEL_WITHOUT_SELLTHROUGH_CASH_HARD_4C_SOURCE_PROXY","symbol":"008770","name":"호텔신라","trigger_type":"Stage4C","entry_date":"2024-05-31","entry_price":57000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.11,"MAE_30D_pct":-17.54,"MFE_90D_pct":2.11,"MAE_90D_pct":-29.12,"MFE_180D_pct":2.11,"MAE_180D_pct":-37.37,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C19|008770|Stage4C|2024-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_dutyfree_hard_4C_source_proxy","reuse_reason":"source-proxy retail holdout row; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"dutyfree_traffic_label_hard_4C","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|008770|Stage4C|2024-05-31","non_price_bridge":"duty-free/traffic recovery label without sell-through, inventory, margin, commission or cash bridge","score_alignment":"hard 4C/source-proxy; reverify before aggregate use"}
```

---

## 5. Case analysis

### 5.1 Department-store positive-control

```yaml
positive_control:
  - 069960: department-store value-up / inventory discipline / margin buffer
```

현대백화점 row는 C18/C20에서는 wrong-archetype이었지만, C19에서는 정방향이다. 수출 채널이 아니라 국내 retail inventory/margin bridge가 본체다.

### 5.2 Hypermarket and convenience false positives

```yaml
hard_4C_or_cap:
  - 139480: hypermarket turnaround label failed.
  - 282330: convenience defensive label failed without OPM refresh.
  - 008770: duty-free traffic label failed without sell-through/cash bridge.
```

오프라인 트래픽이나 턴어라운드 언어는 창고 안쪽을 보여주지 않는다. 재고가 털렸는지, 할인율이 낮아졌는지, 현금이 들어왔는지를 봐야 한다.

### 5.3 Apparel and legacy beauty channel hard blocks

```yaml
channel_inventory_hard_4C:
  - 383220: apparel/global brand label without channel inventory normalization.
  - 090430: legacy beauty/China-channel rebound without sell-through.
```

C19는 brand prestige가 아니라 channel inventory 품질이다. 재고가 눌려 있으면 브랜드 이름은 방패가 아니라 무게가 된다.

### 5.4 Source-proxy watch rows

```yaml
source_proxy_watch_or_4B:
  - 004170: department-store/duty-free watch.
  - 023530: retail turnaround 4B.
  - 007070: convenience retail watch.
```

이 row들은 schema guardrail 검증용이다. direct stock-web reprice 전에는 새 weight 근거로 쓰면 안 된다.

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 9
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 5
batch_reverification_required_count: 5
calibration_usable_case_count: 9
calibration_usable_trigger_count: 9
positive_case_count: 2
counterexample_count: 7
local_4B_watch_count: 2
hard_4C_count: 5
wrong_archetype_reclassification_count: 2
current_profile_error_count: 7
diversity_score_summary: "department store positive, hypermarket hard 4C, apparel inventory hard 4C, legacy beauty hard 4C, convenience retail watch/hard 4C, duty-free hard 4C covered"
loop_contribution_label: duplicate_low_value_loop_with_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C19 lesson |
|---|---:|---:|---:|---|
| 069960 | department-store positive | +20.90 / -7.42 | +20.90 / -10.45 | correct C19 reclassification |
| 139480 | hypermarket hard 4C | +9.39 / -21.76 | +9.39 / -31.77 | turnaround label failed |
| 383220 | apparel hard 4C | +3.24 / -33.99 | +3.24 / -33.99 | channel inventory absent |
| 090430 | legacy beauty hard 4C | +3.24 / -40.32 | +3.24 / -48.76 | China-channel label failed |
| 004170 | source-proxy watch | +9.66 / -12.37 | +15.92 / -12.37 | reverify before use |
| 023530 | retail 4B proxy | +22.30 / -11.48 | +24.17 / -17.76 | possible bridge, source repair |
| 282330 | convenience hard 4C proxy | +2.87 / -22.54 | +4.10 / -32.38 | OPM refresh absent |
| 007070 | convenience watch proxy | +9.05 / -12.67 | +9.05 / -18.55 | watch only |
| 008770 | duty-free hard 4C proxy | +2.11 / -29.12 | +2.11 / -37.37 | traffic label failed |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"069960","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":76,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":[],"component_delta_explanation":"Department-store inventory/margin bridge is correctly C19, but Green requires inventory/markdown/receivable refresh.","MFE_90D_pct":20.90,"MAE_90D_pct":-7.42,"score_return_alignment_label":"department_store_inventory_positive","current_profile_verdict":"current_profile_correct_if_reclassified_from_C18_C20"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"139480","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Hypermarket turnaround label lacked durable margin/inventory bridge and suffered deep MAE.","MFE_90D_pct":9.39,"MAE_90D_pct":-21.76,"score_return_alignment_label":"hypermarket_turnaround_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"383220","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":59,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Apparel/global brand label lacked channel inventory normalization and sell-through proof.","MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"score_return_alignment_label":"apparel_channel_inventory_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":40,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Legacy beauty/China-channel label lacked sell-through, channel inventory and OPM bridge.","MFE_90D_pct":3.24,"MAE_90D_pct":-40.32,"score_return_alignment_label":"legacy_beauty_channel_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"004170","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":61,"stage_label_after":"Stage2-Watch_source_repair_required","changed_components":["valuation_repricing_score"],"component_delta_explanation":"Department-store/duty-free proxy row requires direct stock-web and inventory evidence repair before use.","MFE_90D_pct":9.66,"MAE_90D_pct":-12.37,"source_proxy_only":true,"score_return_alignment_label":"source_proxy_department_store_watch","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"023530","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":64,"stage_label_after":"Stage4B_source_repair_required","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Retail turnaround proxy has possible bridge but must prove inventory/markdown/cash before promotion.","MFE_90D_pct":22.30,"MAE_90D_pct":-11.48,"source_proxy_only":true,"score_return_alignment_label":"retail_turnaround_local_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"282330","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Convenience defensive label lacked OPM and mix bridge; proxy row needs direct reprice.","MFE_90D_pct":2.87,"MAE_90D_pct":-22.54,"source_proxy_only":true,"score_return_alignment_label":"convenience_retail_label_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"007070","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":56,"stage_label_after":"Stage2-Watch_source_repair_required","changed_components":["margin_bridge_score","revision_score"],"component_delta_explanation":"Convenience retail mix row is Watch only until OPM and working-capital bridge are verified.","MFE_90D_pct":9.05,"MAE_90D_pct":-12.67,"source_proxy_only":true,"score_return_alignment_label":"convenience_retail_watch_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"008770","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":56,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Duty-free traffic label lacked sell-through and cash bridge; proxy row requires direct reprice.","MFE_90D_pct":2.11,"MAE_90D_pct":-29.12,"source_proxy_only":true,"score_return_alignment_label":"dutyfree_traffic_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
```

---

## 8. Current calibrated profile stress test

The C19 inventory/sell-through/OPM gate held:

```text
department-store inventory and margin bridge
→ Stage2 can survive

retail turnaround label without inventory/cash proof
→ local 4B or hard 4C

hypermarket / convenience defensive label
→ cap or hard 4C without OPM refresh

apparel/global brand label without channel inventory repair
→ hard 4C

legacy beauty / China-channel label without sell-through
→ hard 4C

duty-free traffic label without cash bridge
→ hard 4C

source_proxy_only rows
→ no weight delta until direct stock-web reprice
```

### Rule candidate retained, not newly proposed

```text
C19_INVENTORY_SELLTHROUGH_OPM_RECEIVABLES_GATE_V142_HELD_OUT

if C19
and brand_retail_inventory_or_turnaround_label == true
and sellthrough_inventory_days_markdown_OPM_receivable_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C19
and inventory_margin_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_inventory_receivables_OPM_refresh = true
```

```text
if C19
and channel_inventory_risk == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C19
and retail_turnaround_label == true
and MFE_90D_pct >= +20
and refreshed_inventory_OPM_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C19
and dominant_driver_belongs_to_C18_export_reorder_or_C20_global_distribution == true:
    cap_C19_contribution = true
    require_reclassification = true
```

---

## 9. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 9
    avg_MFE_90D_pct: 10.52
    avg_MAE_90D_pct: -22.12
    false_positive_risk: high_if_brand_or_turnaround_labels_are_left_actionable
    verdict: adequate_only_with_C19_inventory_margin_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for retail value-up/brand labels
    eligible_trigger_count: 9
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L5 consumer retail rows require sell-through/inventory/OPM proof
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C19 requires inventory and receivables bridge, not consumer label
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: channel inventory and traffic labels without margin/cash route hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 10. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | INVENTORY_SELLTHROUGH_OPM_RECEIVABLES_HOLDOUT_V142 | 2 | 7 | 2 | 5 | 0 | 9 | 9 | 0 | 7 | false | false | 9 |

---

## 11. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 9
calibration_usable_trigger_count: 9
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 9
source_proxy_only_count: 5
batch_reverification_required_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only_and_reverify_proxy_rows
```

---

## 12. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 9
reused_case_ids:
  - C19|069960|Stage2-Actionable|2024-01-29
  - C19|139480|Stage4C|2024-01-29
  - C19|383220|Stage4C|2024-07-17
  - C19|090430|Stage4C|2024-05-31
  - C19|004170|Stage2-Watch|2024-01-29
  - C19|023530|Stage4B|2024-01-29
  - C19|282330|Stage4C|2024-05-10
  - C19|007070|Stage2-Watch|2024-05-10
  - C19|008770|Stage4C|2024-05-31
new_symbol_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 5
batch_reverification_required_count: 5
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C19_inventory_sellthrough_OPM_receivables_gate
  - C18_C20_C19_reclassification_guard
residual_error_types_found:
  - retail_turnaround_without_inventory_cash_bridge
  - apparel_channel_inventory_failure
  - legacy_beauty_channel_inventory_failure
  - convenience_defensive_label_without_OPM
  - dutyfree_traffic_without_sellthrough
new_axis_proposed: null
existing_axis_strengthened:
  - C19_INVENTORY_SELLTHROUGH_OPM_RECEIVABLES_GATE_V142_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: mixed reused and source_proxy_only holdout validation; no direct fresh independent reprice in this execution
loop_contribution_label: duplicate_low_value_loop_with_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"142","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","new_independent_case_count":0,"reused_case_count":9,"new_symbol_count":0,"new_trigger_family_count":0,"source_proxy_only_count":5,"batch_reverification_required_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C19_inventory_sellthrough_OPM_receivables_gate","C18_C20_C19_reclassification_guard"],"residual_error_types_found":["retail_turnaround_without_inventory_cash_bridge","apparel_channel_inventory_failure","legacy_beauty_channel_inventory_failure","convenience_defensive_label_without_OPM","dutyfree_traffic_without_sellthrough"],"loop_contribution_label":"duplicate_low_value_loop_with_proxy_reverify_todo","do_not_propose_new_weight_delta":true}
```

---

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R5/C19 loop 142 as holdout validation only. Batch it with C19 loop 141, C18/C20 reclassification boundary rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C19 inventory/sell-through/OPM/receivables gate, but do not create a new weight delta from this loop because five trigger rows are source_proxy_only and require batch reverification. Future research should reprice 신세계(004170), 롯데쇼핑(023530), BGF리테일(282330), GS리테일(007070), 호텔신라(008770), 휠라홀딩스(081660), LG생활건강(051900) when stock-web shards are accessible.
```

---

## 14. Next research state

```yaml
completed_round: R5
completed_loop: 142
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C27_CONTENT_IP_GLOBAL_MONETIZATION
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```
