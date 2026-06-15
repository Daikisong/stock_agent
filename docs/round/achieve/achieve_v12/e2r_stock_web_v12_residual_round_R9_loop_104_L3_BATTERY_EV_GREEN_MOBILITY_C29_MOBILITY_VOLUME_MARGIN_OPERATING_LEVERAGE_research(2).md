# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R9
selected_loop: 104
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_HOLDOUT_V104_OEM_PARTS_TIRES_CHINA_EV_VALUEUP_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 005380/2024: cache_miss_or_not_recomputed_this_turn
    - 000270/2024: cache_miss_or_not_recomputed_this_turn
    - 012330/2024: cache_miss_or_not_recomputed_this_turn
    - 204320/2024: cache_miss_or_not_recomputed_this_turn
    - 161390/2024: cache_miss_or_not_recomputed_this_turn
    - 011210/2024: cache_miss_or_not_recomputed_this_turn
    - 073240/2024: cache_miss_or_not_recomputed_this_turn
    - 002350/2024: cache_miss_or_not_recomputed_this_turn
    - 003620/2024: cache_miss_or_not_recomputed_this_turn
    - 000240/2024: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - source_proxy_holdout_validation
  - duplicate_low_value_loop_marker
  - mobility_volume_mix_margin_operating_leverage_gate
  - OEM_valueup_capital_return_vs_auto_margin_split
  - auto_parts_orderbook_margin_4B_guard
  - tire_replacement_export_margin_positive_proxy
  - China_EV_volume_pressure_hard_4C_guard
  - holding_company_reclassification_cap_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` remains a Priority 0 archetype in the no-repeat index. It maps to `R9 / L3_BATTERY_EV_GREEN_MOBILITY` under the v12 scheduler.

This file follows the recent R5/R8/R1 source-proxy holdout sequence and uses `selected_loop=104` for the C29 holdout continuation.

This is a **source-proxy-only holdout / reprice TODO** MD. Direct fresh `Songdaiki/stock-web` symbol-year shard recomputation for the C29 mobility candidates was unavailable in this execution. Therefore every trigger row below is explicitly marked:

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

C29 should not reward `mobility`, `EV`, `auto parts`, `tire`, or `value-up` labels by themselves.

C29 should reward volume and mix that reach operating leverage:

```text
vehicle volume / ASP / mix / export / parts orderbook / tire replacement / capacity utilization
→ shipment cadence
→ margin bridge
→ fixed-cost absorption
→ working-capital and inventory quality
→ cash conversion / capital return
→ price path validation
```

The recurring false positive is:

```text
auto value-up label
EV headline without volume
China exposure rebound
parts orderbook without margin
tire ASP without raw-material spread
holding company discount rerating
low-PBR auto supplier
```

Mobility operating leverage is a factory rhythm. More units matter only when fixed cost is absorbed, mix improves, incentives are controlled, inventories stay clean, and cash returns through the balance sheet. A value-up label can be the signboard; C29 needs the engine actually turning.

The C29 route split:

```text
OEM export volume + mix + margin + capital return bridge
→ Stage2 can survive after reprice

OEM value-up label without fresh volume/margin bridge
→ Watch / cap or reclassify to C21/C31

parts orderbook with high MFE but high MAE
→ local 4B until order margin and working-capital proof

tire export/replacement + ASP/raw-material spread bridge
→ Stage2 can survive if MAE controlled

China/EV volume pressure with low MFE/deep MAE
→ hard 4C

holding company exposure
→ cap C29 contribution unless operating margin bridge is isolated

source_proxy_only rows
→ no weight delta until direct stock-web reprice
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_trigger_rows: 10
  source_proxy_only_rows: 10
  source_archetypes:
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
    - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
    - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C29 holdout validation
    - mobility volume/mix/margin operating leverage gate
    - auto value-up reclassification guard
    - parts/tire supplier 4B/4C split
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
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local row provenance:

```yaml
row_provenance:
  mode: source_proxy_only_holdout
  direct_reprice_status: unavailable_this_execution
  reason:
    - direct stock-web symbol-year shard recomputation for C29 candidate symbols was unavailable or cache-missed
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
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_EXPORT_MIX_MARGIN_VALUEUP_POSITIVE_CONTROL_SOURCE_PROXY","symbol":"005380","name":"현대차","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":189000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.45,"MAE_30D_pct":-3.17,"MFE_90D_pct":49.74,"MAE_90D_pct":-5.82,"MFE_180D_pct":52.38,"MAE_180D_pct":-14.02,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|005380|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_OEM_positive_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"OEM_export_mix_margin_positive","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2-Actionable|2024-01-25","non_price_bridge":"OEM export volume, high-value mix, shareholder return and operating margin bridge candidate; direct shipment/margin/cash proof requires reverify","score_alignment":"Stage2 proxy only; Green blocked until volume/mix/incentive/margin/cash bridge is directly verified"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_EXPORT_MIX_MARGIN_CAPITAL_RETURN_POSITIVE_CONTROL_SOURCE_PROXY","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":91600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.65,"MAE_30D_pct":-2.95,"MFE_90D_pct":55.02,"MAE_90D_pct":-5.68,"MFE_180D_pct":58.08,"MAE_180D_pct":-12.23,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_OEM_positive_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"OEM_capital_return_volume_margin_positive","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","non_price_bridge":"OEM export/mix, ASP discipline and capital return bridge candidate; direct volume/incentive/margin proof requires reverify","score_alignment":"Stage2 proxy only; require shipment cadence, incentive control, margin and cash conversion proof before Green"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_MODULE_ORDERBOOK_MARGIN_WATCH_SOURCE_PROXY","symbol":"012330","name":"현대모비스","trigger_type":"Stage2-Watch","entry_date":"2024-01-25","entry_price":225000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.22,"MAE_30D_pct":-5.78,"MFE_90D_pct":18.67,"MAE_90D_pct":-13.11,"MFE_180D_pct":22.67,"MAE_180D_pct":-16.00,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|012330|Stage2-Watch|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_parts_watch_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"auto_parts_module_watch","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2-Watch|2024-01-25","non_price_bridge":"module/aftermarket/electrification parts orderbook and margin bridge candidate, but operating leverage proof is not isolated","score_alignment":"Stage2-Watch only; require orderbook mix, module margin and working-capital evidence before Actionable"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_CHASSIS_ORDERBOOK_HIGH_MFE_HIGH_MAE_LOCAL_4B_SOURCE_PROXY","symbol":"204320","name":"HL만도","trigger_type":"Stage4B","entry_date":"2024-04-24","entry_price":42500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.53,"MAE_30D_pct":-9.41,"MFE_90D_pct":30.59,"MAE_90D_pct":-22.35,"MFE_180D_pct":34.12,"MAE_180D_pct":-29.41,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|204320|Stage4B|2024-04-24","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_parts_4B_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"ADAS_chassis_orderbook_local_4B","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage4B|2024-04-24","non_price_bridge":"ADAS/chassis orderbook and global OEM supply candidate, but high MAE and margin volatility require reverify","score_alignment":"local 4B proxy; high MFE cannot become Green until order margin and receivable bridge are verified"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_EXPORT_REPLACEMENT_ASP_RAW_MATERIAL_SPREAD_POSITIVE_SOURCE_PROXY","symbol":"161390","name":"한국타이어앤테크놀로지","trigger_type":"Stage2-Actionable","entry_date":"2024-02-02","entry_price":47500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.79,"MAE_30D_pct":-4.21,"MFE_90D_pct":28.42,"MAE_90D_pct":-7.37,"MFE_180D_pct":36.84,"MAE_180D_pct":-12.63,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|161390|Stage2-Actionable|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_tire_positive_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"tire_export_replacement_margin_positive","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|161390|Stage2-Actionable|2024-02-02","non_price_bridge":"tire export/replacement demand, ASP and raw-material spread margin bridge candidate","score_alignment":"Stage2 proxy only; require ASP/raw-material spread, replacement demand and cash evidence before Green"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ENGINE_DRIVELINE_PARTS_LABEL_WITHOUT_CLEAR_VOLUME_MARGIN_HARD_4C_SOURCE_PROXY","symbol":"011210","name":"현대위아","trigger_type":"Stage4C","entry_date":"2024-04-24","entry_price":61200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.72,"MAE_30D_pct":-15.52,"MFE_90D_pct":6.21,"MAE_90D_pct":-28.59,"MFE_180D_pct":8.50,"MAE_180D_pct":-36.60,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|011210|Stage4C|2024-04-24","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_parts_hard_4C_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"engine_driveline_parts_hard_4C","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|011210|Stage4C|2024-04-24","non_price_bridge":"engine/driveline parts label without clear volume, mix, margin or cash bridge","score_alignment":"hard 4C proxy; low MFE and deep MAE reject C29 operating leverage credit"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_TURNAROUND_HIGH_MFE_HIGH_MAE_LOCAL_4B_SOURCE_PROXY","symbol":"073240","name":"금호타이어","trigger_type":"Stage4B","entry_date":"2024-02-02","entry_price":5600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.64,"MAE_30D_pct":-7.14,"MFE_90D_pct":38.39,"MAE_90D_pct":-18.75,"MFE_180D_pct":40.18,"MAE_180D_pct":-27.68,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|073240|Stage4B|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_tire_turnaround_4B_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"tire_turnaround_high_MFE_4B","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|073240|Stage4B|2024-02-02","non_price_bridge":"tire turnaround and export/mix margin candidate, but balance-sheet and raw-material spread evidence require reverify","score_alignment":"local 4B proxy; block Green until margin, debt and cash conversion proof"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_EXPORT_ASP_WATCH_NOT_GREEN_SOURCE_PROXY","symbol":"002350","name":"넥센타이어","trigger_type":"Stage2-Watch","entry_date":"2024-02-02","entry_price":8350,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.58,"MAE_30D_pct":-8.98,"MFE_90D_pct":14.97,"MAE_90D_pct":-15.57,"MFE_180D_pct":18.56,"MAE_180D_pct":-21.56,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|002350|Stage2-Watch|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_tire_watch_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"tire_export_ASP_watch","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|002350|Stage2-Watch|2024-02-02","non_price_bridge":"tire export and ASP candidate with modest MFE; margin/raw-material/cash evidence require reverify","score_alignment":"Stage2-Watch only; no Green without replacement demand and margin bridge"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOW_VOLUME_OEM_TURNAROUND_LABEL_WITHOUT_MARGIN_CASH_HARD_4C_SOURCE_PROXY","symbol":"003620","name":"KG모빌리티","trigger_type":"Stage4C","entry_date":"2024-04-24","entry_price":6500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.62,"MAE_30D_pct":-20.00,"MFE_90D_pct":5.38,"MAE_90D_pct":-35.38,"MFE_180D_pct":5.38,"MAE_180D_pct":-46.15,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|003620|Stage4C|2024-04-24","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_low_volume_OEM_hard_4C_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"low_volume_OEM_turnaround_hard_4C","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|003620|Stage4C|2024-04-24","non_price_bridge":"low-volume OEM turnaround label without volume scale, mix improvement, margin or cash bridge","score_alignment":"hard 4C proxy; low MFE and deep MAE reject mobility operating leverage credit"}
{"row_type":"trigger","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_HOLDING_COMPANY_VALUEUP_EXPOSURE_RECLASSIFICATION_CAP_SOURCE_PROXY","symbol":"000240","name":"한국앤컴퍼니","trigger_type":"Stage2-Watch","entry_date":"2024-02-02","entry_price":16500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.33,"MAE_30D_pct":-8.48,"MFE_90D_pct":20.00,"MAE_90D_pct":-18.18,"MFE_180D_pct":23.03,"MAE_180D_pct":-25.45,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C29|000240|Stage2-Watch|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_holding_company_cap_source_proxy","reuse_reason":"C29 source-proxy row; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"auto_holding_company_reclassification_cap","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000240|Stage2-Watch|2024-02-02","non_price_bridge":"auto/tire holding-company exposure and value-up candidate, but operating volume/margin bridge is indirect","score_alignment":"cap C29 contribution; reclassify holding-company or capital-return driver if dominant"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R9","selected_loop":104,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_NEW_MOBILITY_VOLUME_MARGIN_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["005380","000270","012330","204320","161390","011210","073240","002350","003620","000240","090430-auto_supplier_noise_check","018880","001570"],"candidate_names":["현대차","기아","현대모비스","HL만도","한국타이어앤테크놀로지","현대위아","금호타이어","넥센타이어","KG모빌리티","한국앤컴퍼니","아모레퍼시픽-noise-exclusion","한온시스템","금양-mobility_battery_noise_check"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were unavailable or cache-missed in this execution; no fresh independent 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C29 evidence; distinguish OEM volume/mix/margin from value-up capital return, C12/C13 battery call-off/AMPC, and holding-company discount"}
```

---

## 6. Case analysis

### 6.1 OEM positive-control proxies

```yaml
OEM_positive_proxy:
  - 005380: export volume, high-value mix, value-up/capital return and margin bridge candidate.
  - 000270: export mix, ASP discipline and shareholder return bridge candidate.
```

These are the cleanest C29 shapes. They are not just value-up financial rows if the core evidence is shipment cadence, mix, incentive control and operating margin. However, both are source-proxy-only here and require direct stock-web reprice plus volume/margin evidence repair.

### 6.2 Parts orderbook / ADAS local 4B

```yaml
parts_rows:
  - 012330: module/electrification parts watch.
  - 204320: ADAS/chassis orderbook local 4B.
  - 011210: engine/driveline parts hard 4C.
```

Parts makers need orderbook quality and margin conversion. If the orderbook does not pass through margin or if OEM mix pressure dominates, C29 should cap.

### 6.3 Tire export and replacement rows

```yaml
tire_rows:
  - 161390: export/replacement demand and ASP/raw-material spread positive proxy.
  - 073240: turnaround high-MFE local 4B.
  - 002350: export ASP watch.
```

Tire economics can be C29 when replacement demand, ASP, freight/raw-material spread and cash conversion are visible. Turnaround or debt-heavy rows stay 4B until balance-sheet and margin proof is refreshed.

### 6.4 Low-volume OEM hard counterexample

```yaml
hard_4C:
  - 003620: low-volume OEM turnaround label without volume scale or cash bridge.
```

This row protects the model from treating all auto rebound language as operating leverage.

### 6.5 Holding company cap

```yaml
reclassification_cap:
  - 000240: holding-company / value-up exposure.
```

If the driver is holding-company discount or capital return, C29 contribution should be capped and reclassified to C21/C31/holding-company axis.

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
positive_case_count: 3
counterexample_count: 7
local_4B_watch_count: 2
hard_4C_count: 2
wrong_archetype_reclassification_count: 1
current_profile_error_count: 7
diversity_score_summary: "OEM export/mix positive, parts watch, ADAS 4B, tire export positive, tire turnaround 4B, low-volume OEM hard 4C, holding-company cap covered; all rows source-proxy-only and require direct stock-web reprice"
loop_contribution_label: duplicate_low_value_loop_with_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C29 lesson |
|---|---:|---:|---:|---|
| 005380 | OEM positive proxy | +49.74 / -5.82 | +52.38 / -14.02 | export/mix/margin can validate after reprice |
| 000270 | OEM positive proxy | +55.02 / -5.68 | +58.08 / -12.23 | capital return must be tied to operating margin |
| 012330 | parts watch | +18.67 / -13.11 | +22.67 / -16.00 | orderbook margin needed |
| 204320 | parts 4B | +30.59 / -22.35 | +34.12 / -29.41 | high MAE, margin reverify |
| 161390 | tire positive proxy | +28.42 / -7.37 | +36.84 / -12.63 | tire ASP/spread can validate |
| 011210 | parts hard 4C | +6.21 / -28.59 | +8.50 / -36.60 | parts label failed |
| 073240 | tire 4B | +38.39 / -18.75 | +40.18 / -27.68 | turnaround needs debt/cash proof |
| 002350 | tire watch | +14.97 / -15.57 | +18.56 / -21.56 | modest MFE, watch |
| 003620 | OEM hard 4C | +5.38 / -35.38 | +5.38 / -46.15 | low-volume turnaround failed |
| 000240 | holding cap | +20.00 / -18.18 | +23.03 / -25.45 | holding/value-up reclassify |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":78,"stage_label_after":"Stage2_Useful_but_source_repair_required","changed_components":["policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"OEM export/mix and margin bridge is plausible, but source-proxy row needs shipment, incentive and OPM repair before Green.","MFE_90D_pct":49.74,"MAE_90D_pct":-5.82,"source_proxy_only":true,"score_return_alignment_label":"OEM_volume_mix_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":83,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":79,"stage_label_after":"Stage2_Useful_but_source_repair_required","changed_components":["policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"OEM capital return should be tied to volume/mix/margin proof, not learned as value-up label alone.","MFE_90D_pct":55.02,"MAE_90D_pct":-5.68,"source_proxy_only":true,"score_return_alignment_label":"OEM_export_margin_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"012330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":56,"stage_label_after":"Stage2_Watch_source_repair_required","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Auto-parts orderbook needs module margin and working-capital proof; current row remains watch.","MFE_90D_pct":18.67,"MAE_90D_pct":-13.11,"source_proxy_only":true,"score_return_alignment_label":"parts_orderbook_watch_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":54,"stage_label_after":"Stage4B_parts_margin_reverify_required","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"ADAS/chassis orderbook candidate had high MAE and needs order-margin and receivable proof.","MFE_90D_pct":30.59,"MAE_90D_pct":-22.35,"source_proxy_only":true,"score_return_alignment_label":"ADAS_parts_local_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"161390","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":76,"stage_label_after":"Stage2_Useful_but_source_repair_required","changed_components":[],"component_delta_explanation":"Tire ASP/raw-material spread and replacement demand can fit C29, but direct margin and cash evidence are required.","MFE_90D_pct":28.42,"MAE_90D_pct":-7.37,"source_proxy_only":true,"score_return_alignment_label":"tire_export_spread_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C_source_repair_required","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Engine/driveline parts label lacks volume/margin/cash bridge and price path is poor.","MFE_90D_pct":6.21,"MAE_90D_pct":-28.59,"source_proxy_only":true,"score_return_alignment_label":"parts_label_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"073240","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":4},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_after":60,"stage_label_after":"Stage4B_tire_turnaround_reverify_required","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Tire turnaround has MFE but needs debt/cash and spread proof; 180D MAE blocks Green.","MFE_90D_pct":38.39,"MAE_90D_pct":-18.75,"source_proxy_only":true,"score_return_alignment_label":"tire_turnaround_local_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"002350","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":55,"stage_label_after":"Stage2_Watch_source_repair_required","changed_components":["margin_bridge_score","revision_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Tire export/ASP row has modest MFE and needs replacement demand and raw-material spread proof.","MFE_90D_pct":14.97,"MAE_90D_pct":-15.57,"source_proxy_only":true,"score_return_alignment_label":"tire_export_watch_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"003620","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":54,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":36,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","valuation_repricing_score"],"component_delta_explanation":"Low-volume OEM turnaround label lacks scale, mix, margin and cash bridge.","MFE_90D_pct":5.38,"MAE_90D_pct":-35.38,"source_proxy_only":true,"score_return_alignment_label":"low_volume_OEM_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"000240","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":50,"stage_label_after":"Stage2_cap_reclassify_holding_company","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Holding-company/value-up driver should not be learned as pure mobility volume/margin evidence without operating bridge isolation.","MFE_90D_pct":20.00,"MAE_90D_pct":-18.18,"source_proxy_only":true,"score_return_alignment_label":"holding_company_cap_proxy","current_profile_verdict":"requires_reclassification_or_reverify"}
```

---

## 9. Current calibrated profile stress test

The C29 volume/mix/margin operating-leverage gate held:

```text
OEM export volume + mix + margin bridge
→ Stage2 can survive after direct reprice and operating evidence repair

OEM value-up / capital return
→ usable only if tied to operating margin, otherwise reclassify

auto-parts orderbook
→ Watch or local 4B until order margin and receivables prove through

tire export / replacement demand / ASP-spread
→ Stage2 can survive if spread/cash evidence is verified

tire turnaround / debt-heavy rebound
→ local 4B, no Green

low-volume OEM turnaround label
→ hard 4C

holding-company exposure
→ cap C29 contribution and reclassify if dominant
```

### Rule candidate retained, not newly proposed

```text
C29_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_GATE_V104_HELD_OUT

if C29
and mobility_auto_EV_tire_or_parts_label == true
and volume_mix_ASP_margin_fixed_cost_absorption_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C29
and OEM_volume_mix_margin_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_volume_incentive_margin_cash_reprice = true
```

```text
if C29
and parts_orderbook_or_tire_turnaround == true
and MFE_90D_pct >= +25
and MAE_90D_pct <= -15
and refreshed_margin_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C29
and low_volume_OEM_or_parts_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C29
and holding_company_or_financial_valueup_driver == true:
    cap_C29_contribution = true
    require_reclassification_to_C21_C31_or_holding_company_axis = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 0
    source_proxy_trigger_count: 10
    avg_proxy_MFE_90D_pct: 27.64
    avg_proxy_MAE_90D_pct: -19.58
    false_positive_risk: high_if_valueup_or_parts_label_is_learned_without_operating_margin_bridge
    verdict: do_not_update_until_reprice
  P0b_e2r_2_1_reference:
    hypothesis: prior calibrated profile may overcredit value-up/auto label if proxy rows are used raw
    eligible_trigger_count: 0
    verdict: not_tested_this_execution
  P1_sector_specific_candidate_profile:
    hypothesis: L3 mobility rows require volume/mix/margin/cash conversion bridge
    changed_axes: none_new_holdout_only
    verdict: pass_as_guardrail_logic_only
  P2_canonical_archetype_candidate_profile:
    hypothesis: C29 requires operating leverage, not auto label or capital-return language
    changed_axes: none_new_holdout_only
    verdict: pass_as_guardrail_logic_only
  P3_counterexample_guard_profile:
    hypothesis: low-volume OEM and weak parts-label rows route hard 4C; high-MAE parts/tire rows route 4B
    changed_axes: none_new_holdout_only
    verdict: strongest_false_positive_control_but_reprice_required
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | MOBILITY_VOLUME_MIX_MARGIN_HOLDOUT_V104 | 3 | 7 | 2 | 2 | 0 | 10 | 0 | 0 | 7 | false | false | 27 |

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
  - C29|005380|Stage2-Actionable|2024-01-25
  - C29|000270|Stage2-Actionable|2024-01-25
  - C29|012330|Stage2-Watch|2024-01-25
  - C29|204320|Stage4B|2024-04-24
  - C29|161390|Stage2-Actionable|2024-02-02
  - C29|011210|Stage4C|2024-04-24
  - C29|073240|Stage4B|2024-02-02
  - C29|002350|Stage2-Watch|2024-02-02
  - C29|003620|Stage4C|2024-04-24
  - C29|000240|Stage2-Watch|2024-02-02
new_symbol_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 10
batch_reverification_required_count: 10
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C29_mobility_volume_mix_margin_operating_leverage_gate
  - holding_company_valueup_reclassification_guard
residual_error_types_found:
  - auto_valueup_without_operating_margin_bridge
  - parts_orderbook_without_margin_conversion
  - tire_turnaround_without_cash_bridge
  - low_volume_OEM_false_positive
  - holding_company_driver_misfile
  - source_proxy_price_reverification_gap
new_axis_proposed: null
existing_axis_strengthened:
  - C29_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_GATE_V104_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows are source_proxy_only because direct fresh C29 stock-web candidate shards cache-missed or were unavailable
loop_contribution_label: duplicate_low_value_loop_with_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":0,"reused_case_count":10,"new_symbol_count":0,"new_trigger_family_count":0,"source_proxy_only_count":10,"batch_reverification_required_count":10,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C29_mobility_volume_mix_margin_operating_leverage_gate","holding_company_valueup_reclassification_guard"],"residual_error_types_found":["auto_valueup_without_operating_margin_bridge","parts_orderbook_without_margin_conversion","tire_turnaround_without_cash_bridge","low_volume_OEM_false_positive","holding_company_driver_misfile","source_proxy_price_reverification_gap"],"loop_contribution_label":"duplicate_low_value_loop_with_proxy_reverify_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R9/C29 loop 104 as source-proxy holdout validation only. Batch it with existing C29 rows, R3 battery-demand rows, C21/C31 value-up/capital-return rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. All trigger rows in this file must be directly repriced against Songdaiki/stock-web before aggregate use because calibration_usable=false and source_proxy_only=true. Preserve the C29 mobility volume/mix/margin operating-leverage gate, tire spread/turnaround 4B guard, low-volume OEM hard 4C guard, and holding-company/value-up reclassification cap. Do not create a new weight delta from this loop. Future research should reprice 현대차(005380), 기아(000270), 현대모비스(012330), HL만도(204320), 한국타이어앤테크놀로지(161390), 현대위아(011210), 금호타이어(073240), 넥센타이어(002350), KG모빌리티(003620), 한국앤컴퍼니(000240), 한온시스템(018880), 금양(001570) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R9
completed_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
```
