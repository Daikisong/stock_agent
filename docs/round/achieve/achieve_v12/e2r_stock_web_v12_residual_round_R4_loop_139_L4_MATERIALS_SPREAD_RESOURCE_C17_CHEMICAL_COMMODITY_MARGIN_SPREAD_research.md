# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 139
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_COMMODITY_SPREAD_MARGIN_FCF_HOLDOUT_V139_PETROCHEM_SYNTHETIC_RUBBER_POLYSILICON_EPOXY_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_new_symbol_shards:
    - 011170/2024: cache_miss_or_reused_from_prior_local_file
    - 006650/2024: cache_miss_or_reused_from_prior_local_file
    - 011780/2024: cache_miss_or_reused_from_prior_local_file
    - 009830/2024: cache_miss_or_reused_from_prior_local_file
    - 010060/2024: cache_miss_or_reused_from_prior_local_file
    - 298000/2024: reused_from_C15_C17_guardrail
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - chemical_feedstock_to_product_spread_gate
  - commodity_label_vs_margin_FCF_split
  - solar_polysilicon_event_contamination_guard
  - petrochemical_balance_sheet_hard_4C_guard
  - specialty_chemical_slow_positive_watch
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` remains a Priority 0 archetype. The current no-repeat index marks C17 as below the 30-row minimum, and the v12 scheduler maps C15~C17 to `R4 / L4_MATERIALS_SPREAD_RESOURCE`.

This file continues the local C17 sequence after previously referenced `R4/C17 loop 138`; selected loop is therefore `139`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct fresh symbol-year shard recomputation was unavailable in this execution. The trigger rows below reuse current-session stock-web-derived C17/C15/C16 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C17 should not reward the phrase `commodity recovery`.

C17 should reward the spread that reaches the income statement:

```text
feedstock price / product price / operating-rate cycle / commodity rebound
→ product spread
→ utilization
→ inventory gain or loss
→ margin / FCF / revision
→ price path validation
```

The recurring false positive is:

```text
petrochemical bottom call
chemical label
solar / polysilicon / battery-material event
one-quarter inventory gain
China reopening beta
low-PBR commodity value label
```

A product price rally is only the wind. C17 needs the sail angle: whether the company’s feedstock, product mix, operating rate, debt load and inventory accounting convert that wind into margin and cash.

The route split in this holdout pass:

1. **Specialty or synthetic-rubber margin bridge**
   - Stage2 can survive when product spread and FCF path are visible.

2. **Petrochemical generic bottom-call**
   - Low MFE and deep MAE without product spread repair route to hard 4C.

3. **Balance-sheet-stressed chemical label**
   - Chemical label with leverage and no spread repair hard-blocks.

4. **Polysilicon / solar event contamination**
   - Tradable MFE can exist, but C17 contribution is capped unless product spread and cash bridge dominate.

5. **Epoxy / specialty slow watch**
   - Watch only until feedstock/product spread and order/margin refresh.

6. **Battery material event misfile**
   - High MFE may belong to C13/C16/C15 rather than C17.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 10
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C17 holdout validation
    - chemical spread-to-margin gate
    - petrochemical hard 4C guard
    - event contamination reclassification guard
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
  - R4/C17 loops 136~138
  - R4/C15 loops 105~108
  - R4/C16 loops 112~115
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C17 candidate shards were unavailable or not recomputed in this execution
  - exact duplicate C17 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPREAD_MARGIN_FCF_POSITIVE_CONTROL","symbol":"011780","name":"금호석유","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_price":133600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.34,"MAE_30D_pct":-3.82,"MFE_90D_pct":23.20,"MAE_90D_pct":-7.11,"MFE_180D_pct":31.29,"MAE_180D_pct":-7.11,"forward_high_30d":154100,"forward_low_30d":128500,"forward_high_90d":164600,"forward_low_90d":124100,"forward_high_180d":175400,"forward_low_180d":124100,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|011780|Stage2-Actionable|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same synthetic-rubber/specialty spread row from prior C17 local files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"synthetic_rubber_spread_positive_control","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|Stage2-Actionable|2024-02-26","non_price_bridge":"synthetic rubber and specialty chemical product-spread recovery with balance-sheet and FCF bridge","score_alignment":"Stage2 can survive; Green requires product-spread and FCF revision refresh"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PAINT_SILICONE_SPECIALTY_MARGIN_POSITIVE_CONTROL_REUSED","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_price":244000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.62,"MAE_30D_pct":-2.46,"MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"MFE_180D_pct":41.39,"MAE_180D_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|002380|Stage2-Actionable|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same KCC material/specialty margin row from C15 and C17 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"specialty_margin_positive_control","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|002380|Stage2-Actionable|2024-01-30","non_price_bridge":"paint/silicone/specialty material margin recovery and FCF bridge","score_alignment":"keep Stage2; block Green until product-spread and revision evidence refresh"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEM_NCC_BOTTOM_CALL_NO_SPREAD_REPAIR_HARD_4C","symbol":"011170","name":"롯데케미칼","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":118000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.24,"MAE_30D_pct":-12.29,"MFE_90D_pct":4.24,"MAE_90D_pct":-30.93,"MFE_180D_pct":4.24,"MAE_180D_pct":-43.64,"forward_high_30d":123000,"forward_low_30d":103500,"forward_high_90d":123000,"forward_low_90d":81500,"forward_high_180d":123000,"forward_low_180d":66500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|011170|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same NCC bottom-call hard-block row from prior C17 local files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"petrochemical_bottom_call_hard_4C","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|Stage4C|2024-05-20","non_price_bridge":"petrochemical bottom-call label without naphtha-to-product spread repair, utilization recovery, FCF or balance-sheet bridge","score_alignment":"hard 4C; generic petrochemical recovery failed"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEM_LOW_MFE_DEEP_MAE_SPREAD_ABSENT_HARD_4C","symbol":"006650","name":"대한유화","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":151000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.65,"MAE_30D_pct":-16.56,"MFE_90D_pct":2.65,"MAE_90D_pct":-34.77,"MFE_180D_pct":2.65,"MAE_180D_pct":-48.34,"forward_high_30d":155000,"forward_low_30d":126000,"forward_high_90d":155000,"forward_low_90d":98500,"forward_high_180d":155000,"forward_low_180d":78000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|006650|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same petrochemical low-MFE/deep-MAE row from prior C17 local files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"petrochemical_spread_absent_hard_4C","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|006650|Stage4C|2024-05-20","non_price_bridge":"commodity chemical label without product spread, export order, utilization, FCF or balance-sheet repair","score_alignment":"hard 4C; low MFE and deep MAE reject C17 bridge"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PP_PETROCHEM_LEVERAGE_SPREAD_BALANCE_SHEET_HARD_4C","symbol":"298000","name":"효성화학","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":71000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.41,"MAE_30D_pct":-16.20,"MFE_90D_pct":9.01,"MAE_90D_pct":-22.39,"MFE_180D_pct":9.01,"MAE_180D_pct":-60.35,"forward_high_30d":72000,"forward_low_30d":59500,"forward_high_90d":77400,"forward_low_90d":55100,"forward_high_180d":77400,"forward_low_180d":28150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|298000|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Hyosung Chemical PP hard counterexample row from C15/C17 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"leveraged_chemical_hard_4C","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298000|Stage4C|2024-05-20","non_price_bridge":"PP/petrochemical label without product-spread repair, FCF or balance-sheet relief","score_alignment":"hard 4C; severe 180D MAE shows chemical label failed"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SOLAR_POLYSILICON_SPREAD_EVENT_CONTAMINATION_LOCAL_4B","symbol":"010060","name":"OCI홀딩스","trigger_type":"Stage4B","entry_date":"2024-02-27","entry_price":95100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.82,"MAE_30D_pct":-6.83,"MFE_90D_pct":25.13,"MAE_90D_pct":-17.56,"MFE_180D_pct":25.13,"MAE_180D_pct":-31.23,"forward_high_30d":113000,"forward_low_30d":88600,"forward_high_90d":119000,"forward_low_90d":78400,"forward_high_180d":119000,"forward_low_180d":65400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|010060|Stage4B|2024-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_solar_poly_4B","reuse_reason":"same polysilicon/spread local-4B row from prior C17 local files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"polysilicon_spread_local_4B","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|010060|Stage4B|2024-02-27","non_price_bridge":"polysilicon and solar-material spread exposure with policy/supply event noise; product spread and cash conversion refresh needed","score_alignment":"local 4B; block Green until polysilicon spread, shipment and FCF bridge refresh"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SOLAR_CHEMICAL_VALUE_LABEL_NO_SPREAD_REPAIR_HARD_4C","symbol":"009830","name":"한화솔루션","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":28000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.36,"MAE_30D_pct":-21.43,"MFE_90D_pct":5.36,"MAE_90D_pct":-36.43,"MFE_180D_pct":5.36,"MAE_180D_pct":-43.75,"forward_high_30d":29500,"forward_low_30d":22000,"forward_high_90d":29500,"forward_low_90d":17800,"forward_high_180d":29500,"forward_low_180d":15750,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|009830|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_solar_chemical_hard_4C","reuse_reason":"same solar/chemical spread failure row from prior C17 local files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"solar_chemical_label_hard_4C","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|009830|Stage4C|2024-05-20","non_price_bridge":"solar/chemical value label without product spread repair, utilization, inventory normalization or FCF bridge","score_alignment":"hard 4C; value label and policy beta failed C17 spread test"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"EPOXY_SPECIALTY_SPREAD_SLOW_WATCH","symbol":"007690","name":"국도화학","trigger_type":"Stage2-Watch","entry_date":"2024-04-30","entry_price":40700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.86,"MAE_30D_pct":-5.90,"MFE_90D_pct":7.86,"MAE_90D_pct":-13.51,"MFE_180D_pct":11.92,"MAE_180D_pct":-13.51,"forward_high_30d":43900,"forward_low_30d":38300,"forward_high_90d":43900,"forward_low_90d":35200,"forward_high_180d":45550,"forward_low_180d":35200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|007690|Stage2-Watch|2024-04-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_slow_watch","reuse_reason":"same epoxy/specialty chemical watch row from prior C17 local files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"specialty_slow_watch","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|007690|Stage2-Watch|2024-04-30","non_price_bridge":"epoxy/specialty chemical spread watch with modest MFE and no decisive FCF/revision bridge","score_alignment":"Stage2-Watch; require product-spread and order/margin refresh before Actionable"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"BATTERY_MATERIAL_EVENT_MISFILE_NOT_C17_GREEN","symbol":"011790","name":"SKC","trigger_type":"Stage4B","entry_date":"2024-05-23","entry_price":117000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":70.94,"MAE_30D_pct":0.00,"MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"MFE_180D_pct":70.94,"MAE_180D_pct":-20.17,"forward_high_30d":200000,"forward_low_30d":117000,"forward_high_90d":200000,"forward_low_90d":107600,"forward_high_180d":200000,"forward_low_180d":93400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|011790|Stage4B|2024-05-23","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_event_contamination_4B","reuse_reason":"same SKC battery/material event contamination row from C16/C17 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"battery_material_event_misfile_4B","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011790|Stage4B|2024-05-23","non_price_bridge":"battery/material event-driven MFE rather than confirmed chemical commodity product-spread, margin or FCF bridge","score_alignment":"local 4B; cap C17 contribution and require reclassification if battery/material event bridge dominates"}
{"row_type":"trigger","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"BIOCHEMICAL_SPECIALTY_LABEL_NO_MARGIN_BRIDGE_LOCAL_4B","symbol":"161000","name":"애경케미칼","trigger_type":"Stage4B","entry_date":"2024-04-09","entry_price":14500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.76,"MAE_30D_pct":-11.72,"MFE_90D_pct":22.76,"MAE_90D_pct":-24.83,"MFE_180D_pct":22.76,"MAE_180D_pct":-39.31,"forward_high_30d":17800,"forward_low_30d":12800,"forward_high_90d":17800,"forward_low_90d":10900,"forward_high_180d":17800,"forward_low_180d":8800,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C17|161000|Stage4B|2024-04-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_specialty_4B","reuse_reason":"same specialty/biochemical theme high-MAE row from prior C17 local files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"specialty_label_local_4B","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|161000|Stage4B|2024-04-09","non_price_bridge":"specialty/biochemical label with tradable MFE but no refreshed product-spread, margin or FCF bridge","score_alignment":"local 4B; do not promote until margin/revision bridge refresh"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R4","selected_loop":139,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_NEW_CHEMICAL_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["051910","004000","014680","178920","096770"],"candidate_names":["LG화학","롯데정밀화학","한솔케미칼","PI첨단소재","SK이노베이션"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were unavailable or not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C17 evidence; distinguish product-spread margin bridge from battery, governance, or generic commodity beta"}
```

---

## 6. Case analysis

### 6.1 Positive controls — spread became margin

```yaml
positive_controls:
  - 011780: synthetic rubber / specialty spread bridge.
  - 002380: paint/silicone/specialty margin bridge.
```

These rows remind the gate not to over-block. C17 is allowed to score a chemical name when the spread reaches margin and FCF.

### 6.2 Petrochemical bottom-call failures

```yaml
hard_4C_rows:
  - 011170: NCC bottom-call without spread repair.
  - 006650: commodity chemical label with low MFE and deep MAE.
  - 298000: leveraged PP/petrochemical label without balance-sheet repair.
```

These rows are the core counterexample set. They show that “bottom call” is not the same as margin repair.

### 6.3 Solar / polysilicon / chemical value labels

```yaml
solar_related:
  - 010060: polysilicon spread/event row, local 4B.
  - 009830: solar/chemical value label hard 4C.
```

Solar-related chemical rows need product spread, shipment and FCF confirmation. Policy or value beta is not enough.

### 6.4 Specialty watch and event contamination

```yaml
watch_or_4B:
  - 007690: epoxy/specialty chemical slow watch.
  - 011790: battery-material event misfile, not C17 Green.
  - 161000: specialty/biochemical label local 4B.
```

These rows should stay in the inspection bay until margin/revision refresh appears.

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
local_4B_watch_count: 4
hard_4C_count: 5
wrong_archetype_reclassification_count: 1
current_profile_error_count: 7
diversity_score_summary: "synthetic-rubber positive, specialty positive, NCC hard 4C, petrochemical leverage hard 4C, solar/polysilicon 4B/4C, epoxy watch, battery-material misfile and specialty high-MAE 4B covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C17 lesson |
|---|---:|---:|---:|---|
| 011780 | synthetic-rubber positive | +23.20 / -7.11 | +31.29 / -7.11 | spread/margin bridge validates |
| 002380 | specialty margin positive | +20.49 / -7.79 | +41.39 / -7.79 | margin/FCF bridge validates |
| 011170 | NCC hard 4C | +4.24 / -30.93 | +4.24 / -43.64 | bottom-call failed |
| 006650 | petrochem hard 4C | +2.65 / -34.77 | +2.65 / -48.34 | low MFE/deep MAE |
| 298000 | leveraged PP hard 4C | +9.01 / -22.39 | +9.01 / -60.35 | balance-sheet bridge absent |
| 010060 | polysilicon 4B | +25.13 / -17.56 | +25.13 / -31.23 | spread/event needs refresh |
| 009830 | solar chemical 4C | +5.36 / -36.43 | +5.36 / -43.75 | value label failed |
| 007690 | epoxy watch | +7.86 / -13.51 | +11.92 / -13.51 | modest MFE, needs margin proof |
| 011790 | battery-material misfile | +70.94 / -8.03 | +70.94 / -20.17 | dominant bridge belongs elsewhere |
| 161000 | specialty 4B | +22.76 / -24.83 | +22.76 / -39.31 | high MFE, no durable margin bridge |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Synthetic-rubber and specialty spread bridge validated with controlled MAE.","MFE_90D_pct":23.20,"MAE_90D_pct":-7.11,"score_return_alignment_label":"synthetic_rubber_spread_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"002380","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Paint/silicone specialty material margin bridge validated; controlled MAE supports Stage2 hold.","MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"score_return_alignment_label":"specialty_margin_positive_control","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":4},"weighted_score_before":59,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Generic NCC bottom-call lacked product spread repair and price path rejected it.","MFE_90D_pct":4.24,"MAE_90D_pct":-30.93,"score_return_alignment_label":"NCC_bottom_call_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","dilution_cb_risk_score"],"component_delta_explanation":"Petrochemical label lacked spread/FCF bridge and showed low MFE with deep MAE.","MFE_90D_pct":2.65,"MAE_90D_pct":-34.77,"score_return_alignment_label":"petrochemical_spread_absent_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"298000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","dilution_cb_risk_score"],"component_delta_explanation":"PP/petrochemical label did not become spread repair or FCF; severe 180D drawdown confirms hard 4C.","MFE_90D_pct":9.01,"MAE_90D_pct":-22.39,"score_return_alignment_label":"leveraged_PP_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"010060","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":73,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":62,"stage_label_after":"Stage4B_polysilicon_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Polysilicon spread/event exposure had tradable MFE, but 180D MAE and policy/supply noise require FCF refresh.","MFE_90D_pct":25.13,"MAE_90D_pct":-17.56,"score_return_alignment_label":"polysilicon_event_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"009830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_before":59,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","dilution_cb_risk_score"],"component_delta_explanation":"Solar/chemical value label lacked spread repair, utilization or FCF bridge.","MFE_90D_pct":5.36,"MAE_90D_pct":-36.43,"score_return_alignment_label":"solar_chemical_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"007690","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":[],"component_delta_explanation":"Epoxy/specialty spread row is legitimate watch but lacks decisive MFE and FCF/revision proof.","MFE_90D_pct":7.86,"MAE_90D_pct":-13.51,"score_return_alignment_label":"epoxy_slow_watch","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"011790","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":58,"stage_label_after":"Stage4B_event_contamination","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"High MFE was dominated by battery/material event mechanics rather than C17 chemical product-spread/FCF bridge.","MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"score_return_alignment_label":"battery_material_event_misfile","current_profile_verdict":"cap_or_reclassify"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"161000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":54,"stage_label_after":"Stage4B_specialty_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Specialty/biochemical label had tradable MFE but no durable product-spread or FCF bridge.","MFE_90D_pct":22.76,"MAE_90D_pct":-24.83,"score_return_alignment_label":"specialty_high_MAE_local_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
```

---

## 9. Current calibrated profile stress test

The C17 chemical-spread-to-margin bridge gate held:

```text
specialty/synthetic-rubber spread with margin and FCF bridge
→ keep Stage2

generic NCC/petrochemical bottom-call
→ hard 4C without product spread repair

leveraged chemical label
→ hard 4C when balance-sheet bridge absent

solar/polysilicon event
→ local 4B until product spread and FCF refresh

epoxy/specialty slow row
→ Watch, not Actionable

battery-material event mechanics
→ cap C17 and reclassify if dominant

specialty high-MFE high-MAE row
→ local 4B, no Green
```

### Rule candidate retained, not newly proposed

```text
C17_CHEMICAL_FEEDSTOCK_TO_PRODUCT_SPREAD_MARGIN_GATE_V139_HELD_OUT

if C17
and chemical_commodity_recovery_or_value_label == true
and product_spread_utilization_inventory_margin_FCF_revision_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C17
and product_spread_margin_FCF_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if C17
and petrochemical_bottom_call == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C17
and chemical_or_solar_material_label == true
and MFE_90D_pct >= +20
and MAE_180D_pct <= -20
and refreshed_product_spread_FCF_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C17
and dominant_driver_is_battery_policy_resource_or_governance_event == true:
    cap_C17_contribution = true
    require_reclassification = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 10
    avg_MFE_90D_pct: 19.31
    avg_MAE_90D_pct: -20.93
    false_positive_risk: high_if_petrochemical_or_solar_chemical_labels_are_left_actionable
    verdict: adequate_only_with_C17_spread_margin_FCF_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for commodity bottom-call and label beta
    eligible_trigger_count: 10
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L4 chemical names require product-spread and FCF conversion
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C17 requires feedstock-to-product spread bridge, not commodity label
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: NCC/petrochemical bottom-calls with low MFE/deep MAE route hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_COMMODITY_SPREAD_MARGIN_FCF_HOLDOUT_V139 | 3 | 7 | 4 | 5 | 0 | 10 | 10 | 0 | 7 | false | false | 18 |

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
  - C17|011780|Stage2-Actionable|2024-02-26
  - C17|002380|Stage2-Actionable|2024-01-30
  - C17|011170|Stage4C|2024-05-20
  - C17|006650|Stage4C|2024-05-20
  - C17|298000|Stage4C|2024-05-20
  - C17|010060|Stage4B|2024-02-27
  - C17|009830|Stage4C|2024-05-20
  - C17|007690|Stage2-Watch|2024-04-30
  - C17|011790|Stage4B|2024-05-23
  - C17|161000|Stage4B|2024-04-09
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C17_chemical_feedstock_to_product_spread_margin_gate
  - dominant_driver_reclassification_guard
residual_error_types_found:
  - petrochemical_bottom_call_without_spread_repair
  - leveraged_chemical_balance_sheet_failure
  - solar_polysilicon_event_contamination
  - battery_material_event_wrong_bridge
  - specialty_high_MFE_without_FCF_bridge
new_axis_proposed: null
existing_axis_strengthened:
  - C17_CHEMICAL_FEEDSTOCK_TO_PRODUCT_SPREAD_MARGIN_GATE_V139_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C17 candidate shards were unavailable or not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"139","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":0,"reused_case_count":10,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C17_chemical_feedstock_to_product_spread_margin_gate","dominant_driver_reclassification_guard"],"residual_error_types_found":["petrochemical_bottom_call_without_spread_repair","leveraged_chemical_balance_sheet_failure","solar_polysilicon_event_contamination","battery_material_event_wrong_bridge","specialty_high_MFE_without_FCF_bridge"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R4/C17 loop 139 as holdout validation only. Batch it with C17 loops 136~138, C15/C16 adjacent material/resource rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C17 chemical feedstock-to-product spread/margin/FCF bridge gate and dominant-driver reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should reprice LG화학(051910), 롯데정밀화학(004000), 한솔케미칼(014680), PI첨단소재(178920), SK이노베이션(096770) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R4
completed_loop: 139
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
