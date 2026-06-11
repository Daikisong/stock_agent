# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 116
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: KBEAUTY_KFOOD_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_HOLDOUT_V116
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - global_distribution_sellthrough_opm_revision_gate
  - K_food_K_beauty_second_order_validation
  - legacy_channel_hard_4C_guard
  - capacity_proxy_cap_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` remains Priority 0 in the current no-repeat index. The v12 scheduler maps C18~C20 to `R5 / L5_CONSUMER_BRAND_DISTRIBUTION`.

This file continues the local C20 sequence after previously referenced `R5/C20 loop 115`; selected loop is therefore `116`.

This is a **dedupe-aware holdout validation** MD. It does not claim fresh independent stock-web evidence because additional C20 candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C18/C20/C19 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C20 is not simply `K-food` or `K-beauty` as a label.

C20 should reward global distribution that becomes measurable sell-through and margin:

```text
K-food / K-beauty / global channel expansion / ODM / DTC device
→ overseas shelf or platform entry
→ sell-through
→ repeat order
→ channel inventory quality
→ OPM / revision / cash
→ price path validation
```

The recurring false positive:

```text
global brand label
legacy China rebound
factory capacity proxy
one-time shipment
domestic retail margin
```

A shelf is a doorway. C20 needs the room: repeat demand, inventory quality, and operating margin.

This holdout pass validates six route types:

1. **DTC K-beauty vertical rerating**
   - Real bridge and large MFE can exist.
   - Still local 4B until reorder, inventory and margin refresh.

2. **K-food export with late-entry risk**
   - Bridge may be real.
   - Poor entry timing and high MAE block immediate Green.

3. **Mainstream shelf expansion**
   - Strong MFE can occur before second-order proof.
   - Repeat sell-through and OPM refresh remain required.

4. **K-beauty ODM reorder**
   - Customer reorder and ODM export bridge is the cleaner Stage2 path.

5. **Capacity proxy**
   - Capacity construction without near-term sell-through is not C20 Actionable.

6. **Legacy channel / brand label failure**
   - Legacy beauty or global-apparel labels without sell-through and channel inventory repair route to hard 4C or reclassification.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 9
  source_archetypes:
    - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
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
    - C20 holdout validation
    - global distribution second-order gate
    - capacity proxy cap guard
    - local 4B vs hard 4C split
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
  - R5/C18 loops 144~148
  - R5/C20 loops 114~115
  - R5/C19 loop 141
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional C20 candidate shards were not recomputed in this execution
  - exact duplicate C20 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"DTC_KBEAUTY_DEVICE_GLOBAL_DISTRIBUTION_VERTICAL_LOCAL_4B","symbol":"278470","name":"에이피알","trigger_type":"Stage4B","entry_date":"2025-02-27","entry_price":60100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.63,"MAE_30D_pct":-8.82,"MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"MFE_180D_pct":365.06,"MAE_180D_pct":-8.82,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|278470|Stage4B|2025-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_vertical_4B","reuse_reason":"same APR DTC/device distribution row from C18/C20 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"DTC_vertical_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|278470|Stage4B|2025-02-27","non_price_bridge":"DTC K-beauty device global distribution, overseas demand, reorder and margin bridge","score_alignment":"local 4B; vertical rerating requires repeat order, channel inventory and margin refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KFOOD_EXPORT_LATE_ENTRY_GLOBAL_DISTRIBUTION_LOCAL_4B","symbol":"003230","name":"삼양식품","trigger_type":"Stage4B","entry_date":"2024-06-17","entry_price":686000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.66,"MAE_30D_pct":-15.31,"MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"MFE_180D_pct":37.03,"MAE_180D_pct":-33.60,"forward_high_30d":718000,"forward_low_30d":581000,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":940000,"forward_low_180d":455500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|003230|Stage4B|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_late_entry_4B","reuse_reason":"same Samyang late-entry export row from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"K_food_late_entry_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|Stage4B|2024-06-17","non_price_bridge":"Buldak export, overseas shipment, ASP and capacity support; post-spike entry created high MAE before later validation","score_alignment":"real bridge but late entry; no Green without reorder, ASP and OPM refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KFOOD_MAINSTREAM_SHELF_EXPANSION_OPM_REFRESH_LOCAL_4B","symbol":"004370","name":"농심","trigger_type":"Stage4B","entry_date":"2024-05-28","entry_price":469000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.72,"MAE_30D_pct":-8.96,"MFE_90D_pct":27.72,"MAE_90D_pct":-23.13,"MFE_180D_pct":27.72,"MAE_180D_pct":-32.41,"forward_high_30d":599000,"forward_low_30d":427000,"forward_high_90d":599000,"forward_low_90d":360500,"forward_high_180d":599000,"forward_low_180d":317000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|004370|Stage4B|2024-05-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_shelf_expansion_4B","reuse_reason":"same Nongshim shelf-expansion row from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"K_food_shelf_expansion_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|004370|Stage4B|2024-05-28","non_price_bridge":"overseas mainstream shelf expansion and overseas sales mix bridge, but repeat sell-through and margin proof needed","score_alignment":"local 4B; block Stage3-Green until repeat order, channel inventory and OPM bridge refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KFOOD_CAPACITY_PROXY_WITHOUT_SELLTHROUGH_CAP","symbol":"097950","name":"CJ제일제당","trigger_type":"Stage2-Watch","entry_date":"2024-11-22","entry_price":272000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.39,"MAE_30D_pct":-9.93,"MFE_90D_pct":2.39,"MAE_90D_pct":-14.71,"MFE_180D_pct":2.39,"MAE_180D_pct":-19.12,"forward_high_30d":278500,"forward_low_30d":245000,"forward_high_90d":278500,"forward_low_90d":232000,"forward_high_180d":278500,"forward_low_180d":220500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|097950|Stage2-Watch|2024-11-22","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_capacity_cap","reuse_reason":"same capacity-proxy cap row from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"capacity_proxy_cap","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|097950|Stage2-Watch|2024-11-22","non_price_bridge":"global K-food capacity construction proxy without near-term repeat order, sell-through or margin bridge","score_alignment":"cap Stage2; capacity headline alone is not C20 distribution evidence"}
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KBEAUTY_ODM_GLOBAL_REORDER_POSITIVE_CONTROL","symbol":"161890","name":"한국콜마","trigger_type":"Stage2-Actionable","entry_date":"2024-05-10","entry_price":55200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.87,"MAE_30D_pct":-10.51,"MFE_90D_pct":35.87,"MAE_90D_pct":-10.51,"MFE_180D_pct":35.87,"MAE_180D_pct":-10.51,"forward_high_30d":75000,"forward_low_30d":49400,"forward_high_90d":75000,"forward_low_90d":49400,"forward_high_180d":75000,"forward_low_180d":49400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|161890|Stage2-Actionable|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same Kolmar ODM positive-control row from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ODM_export_positive_control","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|161890|Stage2-Actionable|2024-05-10","non_price_bridge":"K-beauty ODM/export reorder bridge with strong MFE and contained MAE","score_alignment":"Stage2-Actionable; Green requires margin and reorder evidence refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KBEAUTY_ODM_GLOBAL_REORDER_HIGH_MAE_LOCAL_4B","symbol":"192820","name":"코스맥스","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_price":157700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.90,"MAE_30D_pct":-6.28,"MFE_90D_pct":31.90,"MAE_90D_pct":-26.44,"MFE_180D_pct":31.90,"MAE_180D_pct":-26.44,"forward_high_30d":208000,"forward_low_30d":147800,"forward_high_90d":208000,"forward_low_90d":116000,"forward_high_180d":208000,"forward_low_180d":116000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|192820|Stage4B|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_ODM_4B","reuse_reason":"same Cosmax ODM 4B control from C18/C20 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ODM_export_local_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|192820|Stage4B|2024-05-13","non_price_bridge":"K-beauty ODM global reorder and customer demand bridge; high MAE requires inventory and margin refresh","score_alignment":"Stage2 may open; block Green until repeat customer order, channel inventory and OPM bridge refresh"}
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_KBEAUTY_CHINA_CHANNEL_LABEL_WITHOUT_REORDER_HARD_4C","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage4C","entry_date":"2024-05-31","entry_price":194200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MAE_30D_pct":-14.68,"MFE_90D_pct":3.24,"MAE_90D_pct":-40.32,"MFE_180D_pct":3.24,"MAE_180D_pct":-48.76,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|090430|Stage4C|2024-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Amore legacy label hard-block row from C18/C20/R13 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"legacy_brand_hard_4C","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|Stage4C|2024-05-31","non_price_bridge":"legacy beauty/China-channel rebound label without durable non-China sell-through, reorder, margin or cash bridge","score_alignment":"hard 4C; require new sell-through and reorder evidence before reopening"}
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"APPAREL_GLOBAL_BRAND_CHANNEL_INVENTORY_NOT_C20_HARD_4C","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_price":74000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|383220|Stage4C|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same F&F channel inventory hard-block control from C18/C20/R13 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"channel_inventory_hard_4C","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|383220|Stage4C|2024-07-17","non_price_bridge":"apparel/global brand label without sell-through, channel inventory normalization or reorder proof","score_alignment":"hard 4C; not clean C20 K-food/K-beauty distribution without inventory and reorder proof"}
{"row_type":"trigger","selected_round":"R5","selected_loop":116,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"DOMESTIC_RETAIL_MARGIN_WRONG_ARCHETYPE_RECLASSIFY_C19","symbol":"069960","name":"현대백화점","trigger_type":"Stage2-Watch","entry_date":"2024-01-29","entry_price":51200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.90,"MAE_30D_pct":-7.42,"MFE_90D_pct":20.90,"MAE_90D_pct":-5.86,"MFE_180D_pct":20.90,"MAE_180D_pct":-10.45,"forward_high_30d":61900,"forward_low_30d":47400,"forward_high_90d":61900,"forward_low_90d":48200,"forward_high_180d":61900,"forward_low_180d":45850,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C20|069960|Stage2-Watch|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype","reuse_reason":"same domestic-retail reclassification control from C18/C19 rows","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"wrong_archetype_positive_elsewhere","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|069960|Stage2-Watch|2024-01-29","non_price_bridge":"domestic department-store value-up, retail margin buffer and inventory discipline candidate, not K-food/K-beauty global distribution","score_alignment":"cap C20 contribution and reclassify to C19"}
```

---

## 5. Case analysis

### 5.1 Real global distribution but local 4B

```yaml
local_4B_bridge_rows:
  - 278470: DTC/device vertical bridge; needs repeat order and margin refresh.
  - 003230: K-food export bridge real, but late entry caused high MAE.
  - 004370: mainstream shelf expansion needs repeat sell-through.
  - 192820: ODM bridge needs inventory and margin refresh.
```

These rows are not dead, but they are still in the inspection bay. C20 should not translate high MFE into Green without second-order validation.

### 5.2 Positive-control row

```yaml
positive_control_rows:
  - 161890: ODM export reorder bridge.
```

This is a clean C20 control: customer reorder and margin evidence can support Stage2, though Green still needs refresh.

### 5.3 False positives and hard 4C rows

```yaml
hard_4C_rows:
  - 090430: legacy beauty / China-channel label without durable reorder.
  - 383220: apparel/global brand label without channel inventory repair.
```

C20 should not reward a global label if sell-through and OPM never reach the ledger.

### 5.4 Wrong archetype row

```yaml
reclassification_rows:
  - 069960: domestic department-store margin/inventory bridge belongs to C19, not C20.
```

A domestic retail bridge can be real and still fail C20. The passport must match the border.

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 9
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 9
calibration_usable_trigger_count: 9
positive_case_count: 4
counterexample_count: 5
local_4B_watch_count: 5
hard_4C_count: 2
wrong_archetype_reclassification_count: 1
current_profile_error_count: 5
diversity_score_summary: "DTC, K-food, K-beauty ODM, capacity proxy, legacy channel hard 4C, domestic retail reclassification covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C20 lesson |
|---|---:|---:|---:|---|
| 278470 | DTC vertical 4B | +204.99 / -8.82 | +365.06 / -8.82 | real bridge, refresh needed |
| 003230 | K-food late-entry 4B | +4.66 / -33.60 | +37.03 / -33.60 | bridge real, timing poor |
| 004370 | shelf expansion 4B | +27.72 / -23.13 | +27.72 / -32.41 | second order needed |
| 097950 | capacity proxy cap | +2.39 / -14.71 | +2.39 / -19.12 | capacity not sell-through |
| 161890 | ODM positive | +35.87 / -10.51 | +35.87 / -10.51 | customer reorder bridge |
| 192820 | ODM 4B | +31.90 / -26.44 | +31.90 / -26.44 | OPM/inventory refresh needed |
| 090430 | legacy hard 4C | +3.24 / -40.32 | +3.24 / -48.76 | channel label fails |
| 383220 | channel inventory hard 4C | +3.24 / -33.99 | +3.24 / -33.99 | inventory repair absent |
| 069960 | wrong archetype | +20.90 / -5.86 | +20.90 / -10.45 | C19, not C20 |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"278470","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":84,"stage_label_after":"Stage4B_vertical_refresh","changed_components":[],"component_delta_explanation":"DTC K-beauty device bridge is real, but vertical rerating should remain 4B until repeat order and margin refresh.","MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"score_return_alignment_label":"real_distribution_vertical_4B","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":3,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":1,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":67,"stage_label_after":"Stage4B_late_entry","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"K-food export bridge was real, but late entry and high MAE require local 4B rather than Green.","MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"score_return_alignment_label":"late_entry_K_food_bridge_4B","current_profile_verdict":"current_profile_too_generous_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"004370","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":63,"stage_label_after":"Stage4B_shelf_expansion_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Mainstream overseas shelf expansion needs repeat sell-through and OPM refresh before promotion.","MFE_90D_pct":27.72,"MAE_90D_pct":-23.13,"score_return_alignment_label":"shelf_expansion_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"097950","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":48,"stage_label_after":"Stage2_cap_capacity_proxy","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Capacity buildout proxy did not prove near-term global sell-through, reorder or OPM bridge.","MFE_90D_pct":2.39,"MAE_90D_pct":-14.71,"score_return_alignment_label":"capacity_proxy_cap","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"161890","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"K-beauty ODM export reorder bridge validated; Green still requires margin/reorder refresh.","MFE_90D_pct":35.87,"MAE_90D_pct":-10.51,"score_return_alignment_label":"ODM_global_distribution_positive_control","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":68,"stage_label_after":"Stage4B_ODM_refresh","changed_components":["revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"ODM bridge is real but high MAE requires channel inventory and margin refresh.","MFE_90D_pct":31.90,"MAE_90D_pct":-26.44,"score_return_alignment_label":"ODM_high_MAE_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":40,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Legacy K-beauty China-channel label lacked durable non-China sell-through, reorder and OPM bridge.","MFE_90D_pct":3.24,"MAE_90D_pct":-40.32,"score_return_alignment_label":"legacy_channel_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"383220","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":59,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Apparel/global brand label lacked channel inventory normalization and reorder proof; not clean C20.","MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"score_return_alignment_label":"channel_inventory_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"069960","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":50,"stage_label_after":"Reclassify_C19","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Domestic department-store margin/inventory bridge is not K-food/K-beauty global distribution; selected archetype contribution should be capped.","MFE_90D_pct":20.90,"MAE_90D_pct":-5.86,"score_return_alignment_label":"wrong_archetype_positive_elsewhere","current_profile_verdict":"requires_reclassification"}
```

---

## 8. Current calibrated profile stress test

The C20 global distribution second-order gate held:

```text
K-food / K-beauty global distribution with sell-through bridge
→ keep Stage2 or local 4B

shelf expansion with high MAE
→ local 4B, no Green

capacity proxy without near-term sell-through
→ cap

legacy brand / China-channel label without reorder
→ hard 4C

domestic retail margin / inventory
→ reclassify to C19
```

### Rule candidate retained, not newly proposed

```text
C20_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_GATE_V116_HELD_OUT

if C20
and global_beauty_food_distribution_label == true
and sellthrough_reorder_inventory_OPM_revision_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C20
and global_distribution_reorder_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_repeat_order_inventory_OPM_refresh = true
```

```text
if C20
and capacity_construction_or_global_proxy_label == true
and near_term_sellthrough_reorder_bridge == false:
    cap_stage2_actionable_bonus = true
```

```text
if C20
and domestic_retail_margin_or_inventory_bridge == true
and global_K_food_K_beauty_distribution_bridge == false:
    cap_C20_contribution = true
    require_reclassification_to_C19 = true
```

```text
if C20
and MFE_90D_pct < +10
and MAE_90D_pct <= -20
and global_distribution_reorder_bridge == false:
    route = Stage4C
```

---

## 9. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 9
    avg_MFE_90D_pct: 37.77
    avg_MAE_90D_pct: -21.93
    false_positive_risk: high_if_global_brand_or_capacity_labels_are_left_actionable
    verdict: adequate_only_with_C20_second_order_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for global brand/channel labels
    eligible_trigger_count: 9
    false_positive_rate: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L5 consumer global distribution requires sell-through/reorder/OPM bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C20 requires second-order global distribution, not capacity or brand proxy
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: legacy brand/channel labels without reorder should route to 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 10. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_HOLDOUT_V116 | 4 | 5 | 5 | 2 | 0 | 9 | 9 | 0 | 5 | false | false | 24 |

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
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 12. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 9
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
new_symbol_count: 0
new_trigger_family_count: 0
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - global_distribution_sellthrough_OPM_gate
residual_error_types_found:
  - capacity_proxy_without_sellthrough
  - shelf_expansion_without_second_order
  - legacy_channel_label_without_sellthrough
  - domestic_retail_wrong_archetype
new_axis_proposed: null
existing_axis_strengthened:
  - C20_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_GATE_V116_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after additional C20 candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"116","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":0,"reused_case_count":9,"new_symbol_count":0,"new_trigger_family_count":0,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","global_distribution_sellthrough_OPM_gate"],"residual_error_types_found":["capacity_proxy_without_sellthrough","shelf_expansion_without_second_order","legacy_channel_label_without_sellthrough","domestic_retail_wrong_archetype"],"loop_contribution_label":"duplicate_low_value_loop","do_not_propose_new_weight_delta":true}
```

---

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R5/C20 loop 116 as holdout validation only. Batch it with C20 loops 110~115, C18 export reorder rows, C19 inventory/margin rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C20 global distribution sell-through/OPM gate, but do not create a new weight delta from this loop because no new independent case was added.
```

---

## 14. Next research state

```yaml
completed_round: R5
completed_loop: 116
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
