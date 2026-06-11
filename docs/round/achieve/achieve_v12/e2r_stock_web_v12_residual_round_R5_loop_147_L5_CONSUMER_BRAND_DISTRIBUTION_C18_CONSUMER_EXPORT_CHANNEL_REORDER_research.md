# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 147
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: SECOND_ORDER_EXPORT_REORDER_HOLDOUT_VALIDATION_V147_DTC_KFOOD_KBEAUTY_DOMESTIC_RETAIL_RECLASSIFICATION
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - additional_C18_candidate_shards: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - export_reorder_second_order_gate
  - domestic_retail_wrong_archetype_guard
  - high_MFE_high_MAE_4B_vs_hard_4C_split
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C18_CONSUMER_EXPORT_CHANNEL_REORDER` remains a Priority 0 archetype in the no-repeat index. The v12 scheduler maps C18~C20 to `R5 / L5_CONSUMER_BRAND_DISTRIBUTION`.

This file continues the local C18 sequence after `R5/C18 loop 146`; selected loop is therefore `147`.

This is a **dedupe-aware holdout validation** MD. It does not claim fresh independent stock-web evidence because additional C18 candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C18/C19/C20 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C18 should pay for the second order, not the first headline.

```text
consumer export / K-food / K-beauty / DTC / ODM / overseas shelf entry
→ sell-through
→ repeat order
→ inventory quality
→ margin / revision / cash
→ price path validation
```

The false-positive shape is:

```text
global brand label
capacity headline
shelf-entry headline
legacy brand rebound
domestic retail margin
```

These may be adjacent, but C18 needs the overseas channel to reorder. If the channel only takes the first shipment and inventory piles up, the row should not become Stage2-Actionable or Green.

This holdout pass validates six route types:

1. **DTC/device export vertical bridge**
   - Real bridge, but vertical rerating remains local 4B until repeat order and margin refresh.

2. **K-food export bridge with late-entry risk**
   - Bridge can be real, but bad entry timing/high MAE blocks immediate Green.

3. **Mainstream shelf expansion**
   - Strong MFE can happen, but repeat sell-through and margin refresh are required.

4. **Capacity proxy**
   - Factory/capacity buildout is not near-term reorder.

5. **K-beauty ODM reorder**
   - Customer reorder / ODM export bridge is a cleaner Stage2 route.

6. **Domestic retail / brand inventory wrong room**
   - Domestic margin/inventory belongs to C19; legacy brand/channel label without reorder is hard 4C.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 10
  source_archetypes:
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
    - C19_BRAND_RETAIL_INVENTORY_MARGIN
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C18 holdout validation
    - export reorder second-order gate
    - local 4B vs hard 4C split
    - domestic retail reclassification guard
    - no production scoring changes
```

---

## 3. Source validation

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
  - R5/C18 loop 144
  - R5/C18 loop 145
  - R5/C18 loop 146
  - R5/C20 loops 114~115
  - R5/C19 loop 141
  - R13 accounting-trust loops 12~13
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional C18 candidate shards were not recomputed in this execution
  - exact duplicate C18 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DTC_DEVICE_EXPORT_VERTICAL_REORDER_BRIDGE_LOCAL_4B","symbol":"278470","name":"에이피알","trigger_type":"Stage4B","entry_date":"2025-02-27","entry_price":60100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":20.63,"MAE_30D_pct":-8.82,"MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"MFE_180D_pct":365.06,"MAE_180D_pct":-8.82,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|278470|Stage4B|2025-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_vertical_4B","reuse_reason":"same APR DTC/device export bridge row from C18 loop 144 / 146 and R13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"real_bridge_vertical_4B","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|278470|Stage4B|2025-02-27","non_price_bridge":"DTC/device global channel expansion, overseas demand, revenue and reorder bridge","score_alignment":"local 4B; vertical rerating requires repeat order, channel inventory and margin refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_EXPORT_LATE_ENTRY_LOCAL_4B","symbol":"003230","name":"삼양식품","trigger_type":"Stage4B","entry_date":"2024-06-17","entry_price":686000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.66,"MAE_30D_pct":-15.31,"MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"MFE_180D_pct":37.03,"MAE_180D_pct":-33.60,"forward_high_30d":718000,"forward_low_30d":581000,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":940000,"forward_low_180d":455500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|003230|Stage4B|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_late_entry_4B","reuse_reason":"same Samyang late-entry export bridge row from C18 loops 145~146","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"real_bridge_late_entry_local_4B","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|003230|Stage4B|2024-06-17","non_price_bridge":"Buldak export, ASP, overseas shipment and capacity support; post-spike entry created high MAE before later validation","score_alignment":"Stage2 bridge may survive, but no immediate Green; require reorder, ASP and margin refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_MAINSTREAM_SHELF_EXPANSION_LOCAL_4B","symbol":"004370","name":"농심","trigger_type":"Stage4B","entry_date":"2024-05-28","entry_price":469000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":27.72,"MAE_30D_pct":-8.96,"MFE_90D_pct":27.72,"MAE_90D_pct":-23.13,"MFE_180D_pct":27.72,"MAE_180D_pct":-32.41,"forward_high_30d":599000,"forward_low_30d":427000,"forward_high_90d":599000,"forward_low_90d":360500,"forward_high_180d":599000,"forward_low_180d":317000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|004370|Stage4B|2024-05-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_shelf_expansion_4B","reuse_reason":"same Nongshim shelf-expansion row from C18 loops 145~146","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"shelf_expansion_local_4B","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|004370|Stage4B|2024-05-28","non_price_bridge":"overseas mainstream shelf expansion and overseas sales mix bridge, but repeat sell-through and margin proof needed","score_alignment":"local 4B; block Stage3-Green until repeat order, channel inventory and margin bridge refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_CAPACITY_PROXY_WITHOUT_REORDER_CAP","symbol":"097950","name":"CJ제일제당","trigger_type":"Stage2-Watch","entry_date":"2024-11-22","entry_price":272000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.39,"MAE_30D_pct":-9.93,"MFE_90D_pct":2.39,"MAE_90D_pct":-14.71,"MFE_180D_pct":2.39,"MAE_180D_pct":-19.12,"forward_high_30d":278500,"forward_low_30d":245000,"forward_high_90d":278500,"forward_low_90d":232000,"forward_high_180d":278500,"forward_low_180d":220500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|097950|Stage2-Watch|2024-11-22","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_capacity_cap","reuse_reason":"same capacity-proxy cap row from C18 loops 145~146","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"capacity_proxy_cap","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|097950|Stage2-Watch|2024-11-22","non_price_bridge":"global K-food capacity construction proxy without near-term repeat order, sell-through or margin bridge","score_alignment":"cap Stage2; capacity headline alone is not C18 reorder evidence"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KBEAUTY_ODM_EXPORT_REORDER_POSITIVE_CONTROL","symbol":"161890","name":"한국콜마","trigger_type":"Stage2-Actionable","entry_date":"2024-05-10","entry_price":55200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":35.87,"MAE_30D_pct":-10.51,"MFE_90D_pct":35.87,"MAE_90D_pct":-10.51,"MFE_180D_pct":35.87,"MAE_180D_pct":-10.51,"forward_high_30d":75000,"forward_low_30d":49400,"forward_high_90d":75000,"forward_low_90d":49400,"forward_high_180d":75000,"forward_low_180d":49400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|161890|Stage2-Actionable|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Kolmar ODM positive-control row from C18 loops 145~146","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ODM_export_positive_control","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|161890|Stage2-Actionable|2024-05-10","non_price_bridge":"K-beauty ODM/export reorder bridge with strong MFE and contained MAE","score_alignment":"Stage2-Actionable; Green requires margin and reorder evidence refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KBEAUTY_ODM_EXPORT_REORDER_HIGH_MAE_LOCAL_4B","symbol":"192820","name":"코스맥스","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_price":157700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":31.90,"MAE_30D_pct":-6.28,"MFE_90D_pct":31.90,"MAE_90D_pct":-26.44,"MFE_180D_pct":31.90,"MAE_180D_pct":-26.44,"forward_high_30d":208000,"forward_low_30d":147800,"forward_high_90d":208000,"forward_low_90d":116000,"forward_high_180d":208000,"forward_low_180d":116000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|192820|Stage4B|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_ODM_4B","reuse_reason":"same Cosmax ODM 4B control from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ODM_export_local_4B","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|192820|Stage4B|2024-05-13","non_price_bridge":"K-beauty ODM global reorder and customer demand bridge; high MAE requires inventory and margin refresh","score_alignment":"Stage2 may open; block Green until repeat customer order, channel inventory and margin bridge refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"LEGACY_BEAUTY_CHANNEL_LABEL_WITHOUT_REORDER_HARD_4C","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage4C","entry_date":"2024-05-31","entry_price":194200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.24,"MAE_30D_pct":-14.68,"MFE_90D_pct":3.24,"MAE_90D_pct":-40.32,"MFE_180D_pct":3.24,"MAE_180D_pct":-48.76,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|090430|Stage4C|2024-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Amore legacy label hard-block row from C18/C20/R13 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"legacy_brand_hard_4C","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|090430|Stage4C|2024-05-31","non_price_bridge":"legacy beauty/China-channel rebound label without durable non-China sell-through, reorder, margin or cash bridge","score_alignment":"hard 4C; require new sell-through and reorder evidence before reopening"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_GLOBAL_BRAND_CHANNEL_INVENTORY_HARD_4C","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_price":74000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|383220|Stage4C|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same F&F channel inventory hard-block control from C18/C20/R13 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"channel_inventory_hard_4C","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|383220|Stage4C|2024-07-17","non_price_bridge":"apparel/global brand label without sell-through, channel inventory normalization or reorder proof","score_alignment":"hard 4C; require channel-inventory and repeat-order evidence before reopen"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DOMESTIC_RETAIL_MARGIN_WRONG_ARCHETYPE_RECLASSIFY_C19","symbol":"069960","name":"현대백화점","trigger_type":"Stage2-Watch","entry_date":"2024-01-29","entry_price":51200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":20.90,"MAE_30D_pct":-7.42,"MFE_90D_pct":20.90,"MAE_90D_pct":-5.86,"MFE_180D_pct":20.90,"MAE_180D_pct":-10.45,"forward_high_30d":61900,"forward_low_30d":47400,"forward_high_90d":61900,"forward_low_90d":48200,"forward_high_180d":61900,"forward_low_180d":45850,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|069960|Stage2-Watch|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype","reuse_reason":"same domestic-retail reclassification control from C18 loops 145~146 / C19 row","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_positive_elsewhere","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|069960|Stage2-Watch|2024-01-29","non_price_bridge":"domestic department-store value-up, retail margin buffer and inventory discipline candidate, not export-channel reorder","score_alignment":"cap C18 contribution and reclassify to C19"}
{"row_type":"trigger","selected_round":"R5","selected_loop":147,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DOMESTIC_HYPERMARKET_TURNAROUND_LABEL_C18_FALSE_POSITIVE","symbol":"139480","name":"이마트","trigger_type":"Stage4C","entry_date":"2024-01-29","entry_price":80900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.39,"MAE_30D_pct":-10.38,"MFE_90D_pct":9.39,"MAE_90D_pct":-21.76,"MFE_180D_pct":9.39,"MAE_180D_pct":-31.77,"forward_high_30d":88500,"forward_low_30d":72500,"forward_high_90d":88500,"forward_low_90d":63300,"forward_high_180d":88500,"forward_low_180d":55200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C18|139480|Stage4C|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_hard_4C","reuse_reason":"same domestic hypermarket counterexample from C18 loops 145~146 / C19 row","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_counterexample","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|139480|Stage4C|2024-01-29","non_price_bridge":"domestic hypermarket restructuring and turnaround label without export reorder, sell-through or durable margin proof","score_alignment":"hard 4C for C18; if researched, use C19 inventory/margin lens with strict proof"}
```

---

## 5. Case analysis

### 5.1 Real bridge but 4B rows

```yaml
local_4B_bridge_rows:
  - 278470: DTC/device vertical bridge; needs reorder and margin refresh.
  - 003230: K-food export bridge real, but late entry caused high MAE.
  - 004370: mainstream shelf expansion needs repeat sell-through.
  - 192820: ODM bridge needs inventory and margin refresh.
```

These are not hard 4C rows. They still have an inspectable bridge.

### 5.2 Stage2 / positive-control rows

```yaml
positive_control_rows:
  - 161890: ODM export reorder bridge.
```

The model should keep Stage2 only while the reorder and margin bridge stays refreshed.

### 5.3 Hard 4C / false-positive rows

```yaml
hard_4C_rows:
  - 090430: legacy beauty / China-channel label without durable reorder.
  - 383220: apparel global brand label without channel inventory repair.
  - 139480: domestic hypermarket turnaround label, not export reorder.
```

These rows should not stay in 4B.

### 5.4 Reclassification rows

```yaml
reclassification_rows:
  - 069960: domestic department-store margin bridge belongs to C19, not C18.
```

A valid domestic retail bridge is not an export reorder bridge.

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 10
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 10
calibration_usable_trigger_count: 10
positive_case_count: 4
counterexample_count: 6
local_4B_watch_count: 5
hard_4C_count: 4
wrong_archetype_reclassification_count: 2
current_profile_error_count: 6
diversity_score_summary: "DTC, K-food, K-beauty ODM, capacity proxy, brand hard 4C, domestic retail reclassification covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C18 lesson |
|---|---:|---:|---:|---|
| 278470 | DTC vertical 4B | +204.99 / -8.82 | +365.06 / -8.82 | real bridge, refresh needed |
| 003230 | late-entry export 4B | +4.66 / -33.60 | +37.03 / -33.60 | bridge real, timing poor |
| 004370 | shelf expansion 4B | +27.72 / -23.13 | +27.72 / -32.41 | second order needed |
| 097950 | capacity proxy cap | +2.39 / -14.71 | +2.39 / -19.12 | capacity not reorder |
| 161890 | ODM positive | +35.87 / -10.51 | +35.87 / -10.51 | customer reorder bridge |
| 192820 | ODM 4B | +31.90 / -26.44 | +31.90 / -26.44 | margin/inventory refresh needed |
| 090430 | legacy hard 4C | +3.24 / -40.32 | +3.24 / -48.76 | brand label fails |
| 383220 | channel inventory hard 4C | +3.24 / -33.99 | +3.24 / -33.99 | inventory repair absent |
| 069960 | wrong archetype | +20.90 / -5.86 | +20.90 / -10.45 | C19, not C18 |
| 139480 | domestic retail false positive | +9.39 / -21.76 | +9.39 / -31.77 | domestic turnaround not export |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"278470","raw_export_channel":5,"raw_sellthrough_reorder":4,"raw_inventory_quality":3,"raw_margin_bridge":4,"raw_price_validation":5,"raw_label_only_risk":0,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_DTCRefresh"}
{"row_type":"score_simulation","symbol":"003230","raw_export_channel":5,"raw_sellthrough_reorder":4,"raw_inventory_quality":2,"raw_margin_bridge":3,"raw_price_validation":2,"raw_label_only_risk":1,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_LateEntry"}
{"row_type":"score_simulation","symbol":"004370","raw_export_channel":4,"raw_sellthrough_reorder":3,"raw_inventory_quality":2,"raw_margin_bridge":2,"raw_price_validation":2,"raw_label_only_risk":2,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_ShelfExpansion"}
{"row_type":"score_simulation","symbol":"097950","raw_export_channel":2,"raw_sellthrough_reorder":1,"raw_inventory_quality":1,"raw_margin_bridge":1,"raw_price_validation":0,"raw_label_only_risk":4,"raw_wrong_archetype_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_CapacityProxy"}
{"row_type":"score_simulation","symbol":"161890","raw_export_channel":4,"raw_sellthrough_reorder":4,"raw_inventory_quality":3,"raw_margin_bridge":4,"raw_price_validation":4,"raw_label_only_risk":0,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_ODMReorder"}
{"row_type":"score_simulation","symbol":"192820","raw_export_channel":4,"raw_sellthrough_reorder":3,"raw_inventory_quality":2,"raw_margin_bridge":2,"raw_price_validation":3,"raw_label_only_risk":1,"raw_wrong_archetype_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_ODMRefresh"}
{"row_type":"score_simulation","symbol":"090430","raw_export_channel":1,"raw_sellthrough_reorder":0,"raw_inventory_quality":0,"raw_margin_bridge":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_wrong_archetype_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_LegacyBrand"}
{"row_type":"score_simulation","symbol":"383220","raw_export_channel":1,"raw_sellthrough_reorder":0,"raw_inventory_quality":0,"raw_margin_bridge":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_wrong_archetype_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_ChannelInventory"}
{"row_type":"score_simulation","symbol":"069960","raw_export_channel":0,"raw_sellthrough_reorder":0,"raw_inventory_quality":3,"raw_margin_bridge":3,"raw_price_validation":3,"raw_label_only_risk":3,"raw_wrong_archetype_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyToC19"}
{"row_type":"score_simulation","symbol":"139480","raw_export_channel":0,"raw_sellthrough_reorder":0,"raw_inventory_quality":1,"raw_margin_bridge":1,"raw_price_validation":0,"raw_label_only_risk":5,"raw_wrong_archetype_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_C18FalsePositive"}
```

---

## 8. Current calibrated profile stress test

The C18 second-order gate held again:

```text
DTC / ODM / export sell-through with bridge -> keep Stage2 or local 4B
shelf expansion with high MAE -> local 4B, no Green
capacity proxy without near-term reorder -> cap
legacy brand/channel label without reorder -> hard 4C
domestic retail margin/inventory -> reclassify to C19
```

### Rule candidate retained, not newly proposed

```text
C18_EXPORT_REORDER_SECOND_ORDER_GATE_V147_HELD_OUT

if C18
and consumer_export_or_global_brand_label == true
and sellthrough_reorder_inventory_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C18
and export_channel_reorder_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_repeat_order_inventory_margin_refresh = true
```

```text
if C18
and capacity_construction_or_global_proxy_label == true
and near_term_sellthrough_reorder_bridge == false:
    cap_stage2_actionable_bonus = true
```

```text
if C18
and domestic_retail_margin_or_inventory_bridge == true
and export_reorder_bridge == false:
    cap_C18_contribution = true
    require_reclassification_to_C19 = true
```

```text
if C18
and MFE_90D_pct < +10
and MAE_90D_pct <= -20
and export_reorder_bridge == false:
    route = Stage4C
```

---

## 9. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 10
calibration_usable_trigger_count: 10
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 10
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 10. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
new_axis_proposed: null
existing_axis_strengthened:
  - C18_EXPORT_REORDER_SECOND_ORDER_GATE_V147_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the C18 second-order export reorder gate across DTC, K-food, K-beauty ODM, capacity proxy, brand hard 4C, and domestic retail reclassification controls."
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R5/C18 loop 147 as holdout validation only. Batch it with C18 loops 141~146, C19 inventory/margin rows, C20 distribution rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C18 export reorder second-order gate, but do not create a new weight delta from this loop because no new independent case was added.
```

---

## 12. Next research state

```yaml
completed_round: R5
completed_loop: 147
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```
