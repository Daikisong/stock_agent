# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 117
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: GLOBAL_DISTRIBUTION_SELLTHROUGH_REORDER_OPM_REVISION_HOLDOUT_V117_KFOOD_KBEAUTY_ODM_DTC_LEGACY_CHANNEL_RETAIL_BOUNDARY_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 278470/2025: reused_from_prior_local_C18_C20_boundary_row
    - 003230/2024: reused_from_prior_local_C18_C20_boundary_row
    - 004370/2024: reused_from_prior_local_C18_C20_boundary_row
    - 097950/2024: reused_from_prior_local_C18_C20_boundary_row
    - 161890/2024: reused_from_prior_local_C18_C20_boundary_row
    - 192820/2024: reused_from_prior_local_C18_C20_boundary_row
    - 090430/2024: reused_from_prior_local_C18_C19_C20_boundary_row
    - 383220/2024: reused_from_prior_local_C18_C19_C20_boundary_row
    - 069960/2024: reused_from_prior_local_C19_wrong_archetype_boundary_row
    - 139480/2024: reused_from_prior_local_C19_retail_counterexample_row
    - 257720/2024: cache_miss_or_not_recomputed_this_turn
    - 241710/2024: cache_miss_or_not_recomputed_this_turn
    - 005180/2024: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - global_distribution_to_sellthrough_reorder_OPM_gate
  - Kfood_Kbeauty_distribution_vs_export_reorder_split
  - ODM_reorder_positive_vs_high_MAE_4B_split
  - legacy_China_channel_hard_4C_guard
  - domestic_retail_C19_reclassification_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` remains Priority 0 in the current no-repeat index. The v12 scheduler maps C18~C20 to `R5 / L5_CONSUMER_BRAND_DISTRIBUTION`.

This file continues the local C20 sequence after previously referenced `R5/C20 loop 116`; selected loop is therefore `117`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because fresh C20 candidate shards were unavailable or not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C18/C19/C20 boundary rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C20 is not simply `K-food`, `K-beauty`, `global brand`, or `distribution`.

C20 should reward global distribution only when it becomes repeated, profitable sell-through:

```text
beauty / food / consumer brand / ODM / DTC / global distributor / overseas retail shelf
→ end-market sell-through
→ reorder or repeat buyer signal
→ channel inventory discipline
→ SKU expansion / repeat shipment cadence
→ OPM / gross margin / revision
→ cash conversion
→ price path validation
```

The recurring false positive is:

```text
global distribution headline
brand prestige
legacy China channel rebound
capacity expansion
one-time sell-in
domestic retail margin story
ODM customer growth without margin proof
DTC vertical rerating without CAC/payback proof
```

C20 is the shelf archetype. A product entering the shelf is not the win. The win is when the shelf empties, the distributor reorders, discounts stay controlled, and OPM rises instead of getting eaten by channel inventory or promotion cost. If the evidence is pure export reorder, C18 may be the cleaner bucket. If it is domestic inventory and retail margin, C19 is cleaner. C20 sits between them: global consumer distribution must show sell-through and margin conversion.

The C20 route split in this holdout:

```text
K-beauty ODM/global customer reorder + margin bridge
→ Stage2 can survive

DTC global distribution vertical with huge MFE
→ local 4B until repeat order, CAC/payback and OPM proof

K-food export/global shelf expansion
→ local 4B unless second-order reorder and channel inventory proof exists

capacity construction without near-term sell-through
→ Stage2 cap

legacy China-channel rebound without durable reorder
→ hard 4C

global/apparel brand label without channel inventory normalization
→ hard 4C

domestic department-store/hypermarket inventory margin
→ reclassify to C19, not C20
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 10
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C19_BRAND_RETAIL_INVENTORY_MARGIN
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C20 holdout validation
    - global-distribution-to-sell-through-OPM gate
    - C18/C19/C20 reclassification boundary
    - legacy-channel and channel-inventory hard-4C guards
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
  - R5/C18 loops 144~149
  - R5/C19 loop 142
  - R5/C20 loop 116
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C20 candidate shards were unavailable or not recomputed in this execution
  - exact duplicate C20 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"DTC_KBEAUTY_GLOBAL_DISTRIBUTION_VERTICAL_RERATING_LOCAL_4B","symbol":"278470","name":"에이피알","trigger_type":"Stage4B","entry_date":"2025-02-27","entry_price":60100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.63,"MAE_30D_pct":-8.82,"MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"MFE_180D_pct":365.06,"MAE_180D_pct":-8.82,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|278470|Stage4B|2025-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_DTC_vertical_4B","reuse_reason":"same APR DTC/device global distribution row from C18/C20 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"DTC_Kbeauty_global_distribution_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|278470|Stage4B|2025-02-27","non_price_bridge":"DTC K-beauty device cross-border channel, overseas reorder and margin bridge candidate; CAC/payback and repeat-order proof required","score_alignment":"local 4B; vertical rerating cannot become Green until sell-through, repeat order, CAC/payback and OPM refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KFOOD_GLOBAL_DISTRIBUTION_LATE_ENTRY_HIGH_MAE_LOCAL_4B","symbol":"003230","name":"삼양식품","trigger_type":"Stage4B","entry_date":"2024-06-17","entry_price":686000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.66,"MAE_30D_pct":-15.31,"MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"MFE_180D_pct":37.03,"MAE_180D_pct":-33.60,"forward_high_30d":718000,"forward_low_30d":581000,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":940000,"forward_low_180d":455500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|003230|Stage4B|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_late_entry_4B","reuse_reason":"same Samyang global/K-food export late-entry row from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"Kfood_global_distribution_late_entry_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|Stage4B|2024-06-17","non_price_bridge":"global Buldak/K-food distribution and ASP bridge was real, but entry followed sharp rerating and suffered deep interim drawdown","score_alignment":"real global distribution bridge but late entry; no Green without sell-through, reorder, channel inventory and OPM refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KFOOD_GLOBAL_SHELF_EXPANSION_SECOND_ORDER_REORDER_LOCAL_4B","symbol":"004370","name":"농심","trigger_type":"Stage4B","entry_date":"2024-05-28","entry_price":469000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.72,"MAE_30D_pct":-8.96,"MFE_90D_pct":27.72,"MAE_90D_pct":-23.13,"MFE_180D_pct":27.72,"MAE_180D_pct":-32.41,"forward_high_30d":599000,"forward_low_30d":427000,"forward_high_90d":599000,"forward_low_90d":360500,"forward_high_180d":599000,"forward_low_180d":317000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|004370|Stage4B|2024-05-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_shelf_expansion_4B","reuse_reason":"same Nongshim global shelf-expansion row from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"Kfood_global_shelf_expansion_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|004370|Stage4B|2024-05-28","non_price_bridge":"overseas mainstream shelf expansion and global sales mix bridge, but second-order reorder and channel inventory proof are incomplete","score_alignment":"local 4B; block Stage3-Green until repeat order, channel inventory and OPM bridge refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KFOOD_GLOBAL_CAPACITY_PROXY_WITHOUT_SELLTHROUGH_CAP","symbol":"097950","name":"CJ제일제당","trigger_type":"Stage2-Watch","entry_date":"2024-11-22","entry_price":272000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.39,"MAE_30D_pct":-9.93,"MFE_90D_pct":2.39,"MAE_90D_pct":-14.71,"MFE_180D_pct":2.39,"MAE_180D_pct":-19.12,"forward_high_30d":278500,"forward_low_30d":245000,"forward_high_90d":278500,"forward_low_90d":232000,"forward_high_180d":278500,"forward_low_180d":220500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|097950|Stage2-Watch|2024-11-22","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_capacity_cap","reuse_reason":"same K-food capacity-proxy cap row from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"Kfood_capacity_proxy_cap","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|097950|Stage2-Watch|2024-11-22","non_price_bridge":"global K-food capacity construction proxy without near-term sell-through, repeat order or margin bridge","score_alignment":"cap Stage2; capacity headline alone is not global distribution sell-through evidence"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KBEAUTY_ODM_GLOBAL_CUSTOMER_REORDER_POSITIVE_CONTROL","symbol":"161890","name":"한국콜마","trigger_type":"Stage2-Actionable","entry_date":"2024-05-10","entry_price":55200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.87,"MAE_30D_pct":-10.51,"MFE_90D_pct":35.87,"MAE_90D_pct":-10.51,"MFE_180D_pct":35.87,"MAE_180D_pct":-10.51,"forward_high_30d":75000,"forward_low_30d":49400,"forward_high_90d":75000,"forward_low_90d":49400,"forward_high_180d":75000,"forward_low_180d":49400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|161890|Stage2-Actionable|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Kolmar ODM positive-control row from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ODM_global_reorder_positive_control","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|161890|Stage2-Actionable|2024-05-10","non_price_bridge":"K-beauty ODM global customer reorder and margin bridge with strong MFE and manageable MAE","score_alignment":"Stage2-Actionable; Green requires margin, reorder cadence, customer concentration and revision refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KBEAUTY_ODM_GLOBAL_DISTRIBUTION_HIGH_MAE_LOCAL_4B","symbol":"192820","name":"코스맥스","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_price":157700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.90,"MAE_30D_pct":-6.28,"MFE_90D_pct":31.90,"MAE_90D_pct":-26.44,"MFE_180D_pct":31.90,"MAE_180D_pct":-26.44,"forward_high_30d":208000,"forward_low_30d":147800,"forward_high_90d":208000,"forward_low_90d":116000,"forward_high_180d":208000,"forward_low_180d":116000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|192820|Stage4B|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_ODM_4B","reuse_reason":"same Cosmax ODM 4B control from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ODM_global_distribution_local_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|192820|Stage4B|2024-05-13","non_price_bridge":"K-beauty ODM global demand bridge, but high MAE requires customer mix, channel inventory and OPM refresh","score_alignment":"Stage2 may open; block Green until repeat customer order, inventory and OPM bridge refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_KBEAUTY_CHINA_CHANNEL_WITHOUT_DURABLE_SELLTHROUGH_HARD_4C","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage4C","entry_date":"2024-05-31","entry_price":194200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MAE_30D_pct":-14.68,"MFE_90D_pct":3.24,"MAE_90D_pct":-40.32,"MFE_180D_pct":3.24,"MAE_180D_pct":-48.76,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|090430|Stage4C|2024-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_legacy_channel_hard_4C","reuse_reason":"same Amore legacy channel hard-block row from C18/C19/C20/R13 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"legacy_beauty_channel_hard_4C","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|Stage4C|2024-05-31","non_price_bridge":"legacy beauty / China-channel rebound label without durable sell-through, non-China reorder, channel inventory or OPM bridge","score_alignment":"hard 4C; require new sell-through and reorder evidence before reopening"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"APPAREL_GLOBAL_BRAND_CHANNEL_INVENTORY_NOT_C20_HARD_4C","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_price":74000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|383220|Stage4C|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_brand_inventory_hard_4C","reuse_reason":"same F&F channel inventory hard-block control from C18/C19/C20/R13 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"apparel_global_brand_channel_inventory_hard_4C","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|383220|Stage4C|2024-07-17","non_price_bridge":"apparel/global brand label without beauty/food distribution bridge, export reorder, channel inventory normalization or sell-through proof","score_alignment":"hard 4C; brand label cannot substitute for global distribution sell-through"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"DOMESTIC_RETAIL_MARGIN_WRONG_ARCHETYPE_RECLASSIFY_C19","symbol":"069960","name":"현대백화점","trigger_type":"Stage2-Watch","entry_date":"2024-01-29","entry_price":51200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.90,"MAE_30D_pct":-7.42,"MFE_90D_pct":20.90,"MAE_90D_pct":-7.42,"MFE_180D_pct":20.90,"MAE_180D_pct":-10.45,"forward_high_30d":61900,"forward_low_30d":47400,"forward_high_90d":61900,"forward_low_90d":47400,"forward_high_180d":61900,"forward_low_180d":45850,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|069960|Stage2-Watch|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_C19","reuse_reason":"same domestic-retail reclassification control from C18/C19/C20 rows","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_positive_elsewhere","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|069960|Stage2-Watch|2024-01-29","non_price_bridge":"domestic department-store value-up, retail margin buffer and inventory discipline candidate, not beauty/food global distribution","score_alignment":"cap C20 contribution and reclassify to C19"}
{"row_type":"trigger","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"DOMESTIC_HYPERMARKET_TURNAROUND_NOT_GLOBAL_DISTRIBUTION_HARD_4C","symbol":"139480","name":"이마트","trigger_type":"Stage4C","entry_date":"2024-01-29","entry_price":80900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.39,"MAE_30D_pct":-10.38,"MFE_90D_pct":9.39,"MAE_90D_pct":-21.76,"MFE_180D_pct":9.39,"MAE_180D_pct":-31.77,"forward_high_30d":88500,"forward_low_30d":72500,"forward_high_90d":88500,"forward_low_90d":63300,"forward_high_180d":88500,"forward_low_180d":55200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C20|139480|Stage4C|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_hard_4C","reuse_reason":"same domestic hypermarket counterexample from C19 rows, reused as C20 wrong-archetype false-positive guard","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"domestic_retail_not_global_distribution_hard_4C","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|139480|Stage4C|2024-01-29","non_price_bridge":"domestic hypermarket restructuring and turnaround label without global beauty/food distribution sell-through or OPM proof","score_alignment":"hard 4C / reclassify C19; domestic retail turnaround is not C20 global distribution"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R5","selected_loop":117,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"C20_NEW_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["257720","241710","005180","271560","280360","051900","145720","214150","018290"],"candidate_names":["실리콘투","코스메카코리아","빙그레","오리온","롯데웰푸드","LG생활건강","덴티움-boundary_exclusion_check","클래시스-boundary_exclusion_check","브이티"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards for new C20 beauty/food global distribution candidates were unavailable or not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C20 evidence; distinguish global distribution sell-through from C18 export reorder, C19 domestic retail inventory margin, and C25 medical-device export installed-base effects"}
```

---

## 6. Case analysis

### 6.1 DTC K-beauty vertical row

```yaml
278470:
  entry_price: 60100
  90D_MFE_MAE: +204.99 / -8.82
  180D_MFE_MAE: +365.06 / -8.82
  route: Stage4B / vertical rerating refresh
```

APR is a price-path positive, but the C20 gate should not turn a vertical rerating into Green until repeat purchase, CAC/payback, channel inventory and OPM evidence refresh.

### 6.2 K-food global distribution rows

```yaml
003230:
  90D_MFE_MAE: +4.66 / -33.60
  180D_MFE_MAE: +37.03 / -33.60
  route: late-entry local 4B

004370:
  90D_MFE_MAE: +27.72 / -23.13
  180D_MFE_MAE: +27.72 / -32.41
  route: shelf-expansion local 4B

097950:
  90D_MFE_MAE: +2.39 / -14.71
  180D_MFE_MAE: +2.39 / -19.12
  route: capacity-proxy cap
```

The K-food rows divide the gate cleanly. Samyang and Nongshim show real global distribution demand but need timing, second-order reorder and inventory proof. CJ CheilJedang is a capacity proxy; capacity is not sell-through.

### 6.3 K-beauty ODM rows

```yaml
161890:
  90D_MFE_MAE: +35.87 / -10.51
  route: Stage2-Actionable / Green blocked

192820:
  90D_MFE_MAE: +31.90 / -26.44
  route: local 4B
```

The ODM pair is the clearest positive/4B split. Kolmar can hold Stage2 because the bridge is closer to global customer reorder. Cosmax needs OPM, customer mix and inventory refresh because the drawdown profile was worse.

### 6.4 Legacy channel and brand-label hard blocks

```yaml
hard_blocks:
  - 090430: legacy K-beauty/China channel label without durable sell-through.
  - 383220: global brand/apparel label without channel inventory normalization.
  - 139480: domestic hypermarket turnaround, not global beauty/food distribution.
```

These rows prevent C20 from swallowing every consumer brand story. The word “global” is not a bridge; sell-through and margin are.

### 6.5 Domestic retail reclassification

```yaml
069960:
  90D_MFE_MAE: +20.90 / -7.42
  route: reclassify to C19
```

This can be a valid consumer row, but it is C19 inventory/margin, not C20 global distribution.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 10
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 10
calibration_usable_trigger_count: 10
positive_case_count: 3
counterexample_count: 7
local_4B_watch_count: 5
hard_4C_count: 3
wrong_archetype_reclassification_count: 2
current_profile_error_count: 7
diversity_score_summary: "DTC K-beauty vertical, K-food late-entry, K-food shelf expansion, capacity proxy, ODM positive, ODM high-MAE 4B, legacy channel hard 4C, apparel/brand hard 4C, domestic retail reclassification, hypermarket hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C20 lesson |
|---|---:|---:|---:|---|
| 278470 | DTC vertical 4B | +204.99 / -8.82 | +365.06 / -8.82 | repeat purchase and CAC/payback proof needed |
| 003230 | K-food late-entry 4B | +4.66 / -33.60 | +37.03 / -33.60 | global demand real, timing/MAE bad |
| 004370 | shelf expansion 4B | +27.72 / -23.13 | +27.72 / -32.41 | second-order reorder needed |
| 097950 | capacity proxy cap | +2.39 / -14.71 | +2.39 / -19.12 | capacity is not sell-through |
| 161890 | ODM positive | +35.87 / -10.51 | +35.87 / -10.51 | global customer reorder bridge works |
| 192820 | ODM 4B | +31.90 / -26.44 | +31.90 / -26.44 | OPM/customer mix refresh needed |
| 090430 | legacy channel 4C | +3.24 / -40.32 | +3.24 / -48.76 | China-channel label failed |
| 383220 | brand inventory 4C | +3.24 / -33.99 | +3.24 / -33.99 | brand label not distribution proof |
| 069960 | wrong archetype | +20.90 / -7.42 | +20.90 / -10.45 | C19, not C20 |
| 139480 | domestic retail 4C | +9.39 / -21.76 | +9.39 / -31.77 | hypermarket label failed |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"278470","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":84,"stage_label_after":"Stage4B_vertical_reorder_refresh","changed_components":[],"component_delta_explanation":"DTC K-beauty global bridge is real, but vertical rerating should remain 4B until repeat order, CAC/payback and margin refresh.","MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"score_return_alignment_label":"DTC_global_distribution_vertical_4B","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":3,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":1,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":67,"stage_label_after":"Stage4B_late_entry","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Global K-food distribution was real, but late entry and high MAE require local 4B rather than Green.","MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"score_return_alignment_label":"late_entry_Kfood_global_4B","current_profile_verdict":"current_profile_too_generous_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":63,"stage_label_after":"Stage4B_shelf_reorder_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Overseas shelf expansion needs repeat sell-through, channel inventory and OPM refresh before promotion.","MFE_90D_pct":27.72,"MAE_90D_pct":-23.13,"score_return_alignment_label":"shelf_expansion_distribution_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"097950","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":48,"stage_label_after":"Stage2_cap_capacity_proxy","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Capacity construction proxy did not prove near-term global sell-through, reorder or OPM bridge.","MFE_90D_pct":2.39,"MAE_90D_pct":-14.71,"score_return_alignment_label":"global_capacity_proxy_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"K-beauty ODM global customer reorder bridge validates C20, though Green requires margin and customer concentration refresh.","MFE_90D_pct":35.87,"MAE_90D_pct":-10.51,"score_return_alignment_label":"ODM_global_distribution_positive_control","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":68,"stage_label_after":"Stage4B_ODM_reorder_refresh","changed_components":["revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"ODM global bridge is real but high MAE requires channel inventory, customer mix and OPM refresh.","MFE_90D_pct":31.90,"MAE_90D_pct":-26.44,"score_return_alignment_label":"ODM_high_MAE_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":40,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Legacy beauty/China-channel label lacked durable non-China sell-through, reorder and OPM bridge.","MFE_90D_pct":3.24,"MAE_90D_pct":-40.32,"score_return_alignment_label":"legacy_channel_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"383220","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":59,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Apparel/global brand label lacked beauty/food sell-through and channel inventory normalization.","MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"score_return_alignment_label":"brand_channel_inventory_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"069960","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":50,"stage_label_after":"Reclassify_C19","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Domestic department-store margin/inventory bridge is not beauty/food global distribution; selected archetype contribution should be capped.","MFE_90D_pct":20.90,"MAE_90D_pct":-7.42,"score_return_alignment_label":"wrong_archetype_positive_elsewhere","current_profile_verdict":"requires_reclassification"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"139480","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Domestic hypermarket turnaround label lacked global beauty/food sell-through and suffered deep MAE.","MFE_90D_pct":9.39,"MAE_90D_pct":-21.76,"score_return_alignment_label":"domestic_retail_wrong_archetype_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

---

## 9. Current calibrated profile stress test

The C20 global-distribution-to-sell-through gate held:

```text
K-beauty ODM/global customer reorder with margin bridge
→ Stage2 can survive

DTC K-beauty vertical rerating
→ local 4B until repeat purchase, CAC/payback and OPM proof

K-food global distribution with late entry or channel drawdown
→ local 4B, no Green

shelf expansion without second-order reorder
→ local 4B

capacity construction without sell-through
→ Stage2 cap

legacy China-channel rebound without durable sell-through
→ hard 4C

apparel/global brand label without channel inventory repair
→ hard 4C

domestic retail inventory/margin
→ reclassify to C19
```

### Rule candidate retained, not newly proposed

```text
C20_GLOBAL_DISTRIBUTION_SELLTHROUGH_REORDER_OPM_GATE_V117_HELD_OUT

if C20
and beauty_food_global_distribution_or_brand_label == true
and sellthrough_reorder_channel_inventory_OPM_revision_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C20
and global_distribution_sellthrough_margin_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_reorder_inventory_OPM_refresh = true
```

```text
if C20
and global_distribution_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_channel_inventory_OPM_refresh = true
```

```text
if C20
and capacity_or_brand_proxy_label == true
and near_term_sellthrough_or_reorder_bridge == false:
    cap_stage2_actionable_bonus = true
```

```text
if C20
and legacy_channel_or_brand_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C20
and domestic_retail_inventory_margin_bridge == true
and global_beauty_food_distribution_bridge == false:
    cap_C20_contribution = true
    require_reclassification_to_C19 = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with bridge/4B/4C guards
    eligible_trigger_count: 10
    avg_MFE_90D_pct: 34.86
    avg_MAE_90D_pct: -22.87
    false_positive_risk: high_if_global_brand_capacity_or_legacy_channel_labels_are_left_actionable
    verdict: adequate_only_with_C20_sellthrough_OPM_gate
  P0b_e2r_2_1_reference:
    hypothesis: prior calibrated profile may overcredit global distribution and brand labels
    eligible_trigger_count: 10
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L5 consumer rows require sell-through/channel-inventory/OPM proof
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C20 requires global beauty/food distribution economics, not capacity or brand label
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: legacy channel / brand / domestic retail rows without global distribution sell-through route to 4C/reclassify
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_HOLDOUT_V117 | 3 | 7 | 5 | 3 | 0 | 10 | 10 | 0 | 7 | false | false | 24 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 10
calibration_usable_trigger_count: 10
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 10
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 10
reused_case_ids:
  - C20|278470|Stage4B|2025-02-27
  - C20|003230|Stage4B|2024-06-17
  - C20|004370|Stage4B|2024-05-28
  - C20|097950|Stage2-Watch|2024-11-22
  - C20|161890|Stage2-Actionable|2024-05-10
  - C20|192820|Stage4B|2024-05-13
  - C20|090430|Stage4C|2024-05-31
  - C20|383220|Stage4C|2024-07-17
  - C20|069960|Stage2-Watch|2024-01-29
  - C20|139480|Stage4C|2024-01-29
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C20_global_distribution_sellthrough_OPM_gate
  - C18_C19_C20_reclassification_guard
residual_error_types_found:
  - DTC_vertical_rerating_without_repeat_purchase_proof
  - Kfood_late_entry_high_MAE
  - shelf_expansion_without_second_order
  - capacity_proxy_without_sellthrough
  - legacy_channel_without_reorder
  - domestic_retail_wrong_archetype
new_axis_proposed: null
existing_axis_strengthened:
  - C20_GLOBAL_DISTRIBUTION_SELLTHROUGH_REORDER_OPM_GATE_V117_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C20 candidate shards were unavailable or not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"117","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":0,"reused_case_count":10,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C20_global_distribution_sellthrough_OPM_gate","C18_C19_C20_reclassification_guard"],"residual_error_types_found":["DTC_vertical_rerating_without_repeat_purchase_proof","Kfood_late_entry_high_MAE","shelf_expansion_without_second_order","capacity_proxy_without_sellthrough","legacy_channel_without_reorder","domestic_retail_wrong_archetype"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R5/C20 loop 117 as holdout validation only. Batch it with C20 loop 116, C18 export-channel reorder rows, C19 inventory/margin rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C20 global-distribution-to-sell-through/reorder/OPM gate, DTC vertical 4B guard, capacity-proxy cap, legacy-channel hard-4C guard, and C18/C19/C20 reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice 실리콘투(257720), 코스메카코리아(241710), 빙그레(005180), 오리온(271560), 롯데웰푸드(280360), LG생활건강(051900), 브이티(018290), 덴티움(145720), 클래시스(214150) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R5
completed_loop: 117
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```
