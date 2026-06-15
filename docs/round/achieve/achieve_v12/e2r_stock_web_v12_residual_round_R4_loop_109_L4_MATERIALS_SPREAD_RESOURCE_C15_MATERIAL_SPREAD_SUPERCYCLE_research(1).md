# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 109
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: MATERIAL_SPREAD_ASP_VOLUME_MARGIN_FCF_HOLDOUT_V109_CHEMICAL_METAL_FOIL_POLYSILICON_PROCESSING_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 002380/2024: reused_from_prior_local_C15_C17_row
    - 011780/2024: reused_from_prior_local_C17_row
    - 010130/2024: reused_from_prior_local_C16_C32_row
    - 011790/2024: reused_from_prior_local_C16_C17_row
    - 103140/2024: reused_from_prior_local_C15_C16_row
    - 006110/2024: reused_from_prior_local_C15_C16_row
    - 018470/2024: reused_from_prior_local_C15_C16_row
    - 298000/2024: reused_from_prior_local_C15_C17_row
    - 011170/2024: reused_from_prior_local_C17_row
    - 006650/2024: reused_from_prior_local_C17_row
    - 010060/2024: reused_from_prior_local_C17_row
    - 009830/2024: reused_from_prior_local_C17_row
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - material_label_to_ASP_volume_margin_FCF_gate
  - chemical_spread_positive_vs_NCC_bottom_call_split
  - metal_processing_vs_commodity_beta_split
  - high_MFE_high_MAE_4B_guard
  - governance_event_contamination_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C15_MATERIAL_SPREAD_SUPERCYCLE` remains Priority 0 in the current no-repeat index. The v12 scheduler maps C15~C17 to `R4 / L4_MATERIALS_SPREAD_RESOURCE`.

This file continues the local C15 sequence after `R4/C15 loop 108`; selected loop is therefore `109`.

This is a **dedupe-aware holdout validation / adjacent-row reuse** MD. It does not claim fresh independent stock-web evidence because direct fresh C15 candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C15/C16/C17/C32 boundary rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C15 should not reward `materials`, `metal`, `chemical`, `copper`, `aluminium`, `battery foil`, or `polysilicon` as labels.

C15 should reward a materials cycle only when the spread becomes company economics:

```text
raw-material price / product price / commodity cycle / material shortage / processing capacity
→ ASP
→ volume or utilization
→ inventory gain/loss
→ product spread
→ gross margin / OPM / FCF / revision
→ price path validation
```

The recurring false positive is:

```text
commodity beta
material-supercycle vocabulary
battery-material sympathy
resource/security headline
one-quarter inventory gain
capacity proxy without utilization
high-MFE low-float theme
```

A material price move is the tide. C15 asks whether the company owns a boat, not merely whether the water rose. The score should move only when ASP, utilization, inventory accounting, product spread and cash conversion are visible.

The C15 route split in this holdout:

```text
company-specific material spread + margin/FCF bridge
→ Stage2 can survive

chemical/synthetic-rubber spread with controlled MAE
→ Stage2 can survive, though C17 boundary remains

smelter/supply-tightness bridge later contaminated by governance/tender
→ local 4B / cap and reclassify later window to C32

battery-material event or foil label with high MFE/high MAE
→ local 4B until utilization/order/margin refresh

dual-use copper processing bridge with high MAE
→ local 4B until order/margin/cash proof

generic aluminium/copper rolling beta or petrochemical bottom call
→ hard 4C

polysilicon/solar chemical event
→ local 4B unless product spread and FCF bridge refresh

solar/chemical value label
→ hard 4C when spread repair fails
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_trigger_rows: 12
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
    - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C15 holdout validation
    - material-spread-to-margin-FCF gate
    - chemical/material boundary split
    - commodity beta false-positive guard
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
  - R4/C15 loops 104~108
  - R4/C16 loops 112~115
  - R4/C17 loops 136~139
  - R12/C32 governance-contamination rows
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C15 candidate shards were not recomputed in this execution
  - exact duplicate C15 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIALTY_SILICONE_PAINT_MATERIAL_MARGIN_POSITIVE_CONTROL","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_price":244000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.62,"MAE_30D_pct":-2.46,"MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"MFE_180D_pct":41.39,"MAE_180D_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|002380|Stage2-Actionable|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same KCC C15/C17 material margin positive-control row from prior loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"specialty_material_margin_positive_control","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|002380|Stage2-Actionable|2024-01-30","non_price_bridge":"paint/silicone/specialty materials margin and FCF bridge rather than generic commodity beta","score_alignment":"keep Stage2; block Green until margin, revision and FCF refresh"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SYNTHETIC_RUBBER_SPECIALTY_SPREAD_POSITIVE_C17_BOUNDARY","symbol":"011780","name":"금호석유","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_price":133600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.34,"MAE_30D_pct":-3.82,"MFE_90D_pct":23.20,"MAE_90D_pct":-7.11,"MFE_180D_pct":31.29,"MAE_180D_pct":-7.11,"forward_high_30d":154100,"forward_low_30d":128500,"forward_high_90d":164600,"forward_low_90d":124100,"forward_high_180d":175400,"forward_low_180d":124100,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|011780|Stage2-Actionable|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_chemical_positive_boundary","reuse_reason":"same synthetic-rubber/specialty spread row from C17 files, reused as C15 boundary positive","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"chemical_spread_positive_boundary","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|011780|Stage2-Actionable|2024-02-26","non_price_bridge":"synthetic rubber and specialty chemical product-spread recovery with balance-sheet and FCF bridge","score_alignment":"Stage2 can survive; if product-spread mechanics dominate, reclassify to C17 boundary"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ZINC_SMELTER_SUPPLY_TIGHTNESS_WITH_GOVERNANCE_CONTAMINATION_CAP","symbol":"010130","name":"고려아연","trigger_type":"Stage4B","entry_date":"2024-04-09","entry_price":469000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.40,"MAE_30D_pct":-3.94,"MFE_90D_pct":16.42,"MAE_90D_pct":-3.94,"MFE_180D_pct":68.66,"MAE_180D_pct":-3.94,"forward_high_30d":499000,"forward_low_30d":450500,"forward_high_90d":546000,"forward_low_90d":450500,"forward_high_180d":791000,"forward_low_180d":450500,"corporate_action_window_status":"governance_tender_event_contamination_after_2024_09_13","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|010130|Stage4B|2024-04-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_contamination_4B","reuse_reason":"same Korea Zinc supply-tightness row from C16/C32 controls, reused as C15 smelter spread contamination check","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"smelter_spread_positive_with_governance_cap","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010130|Stage4B|2024-04-09","non_price_bridge":"zinc TC collapse and smelter supply-tightness spread candidate, but later tender/control-premium event contaminates 180D interpretation","score_alignment":"local 4B/cap; do not learn later governance-driven 180D MFE as material-spread Green"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"BATTERY_MATERIAL_EVENT_HIGH_MFE_DOMINANT_DRIVER_4B","symbol":"011790","name":"SKC","trigger_type":"Stage4B","entry_date":"2024-05-23","entry_price":117000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":70.94,"MAE_30D_pct":0.00,"MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"MFE_180D_pct":70.94,"MAE_180D_pct":-20.17,"forward_high_30d":200000,"forward_low_30d":117000,"forward_high_90d":200000,"forward_low_90d":107600,"forward_high_180d":200000,"forward_low_180d":93400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|011790|Stage4B|2024-05-23","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_event_contamination_4B","reuse_reason":"same SKC battery/material event row from C16/C17/C13 guardrails, reused as C15 dominant-driver split","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"battery_material_event_local_4B","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|011790|Stage4B|2024-05-23","non_price_bridge":"battery/material event-driven MFE rather than confirmed material spread, utilization, margin or FCF bridge","score_alignment":"local 4B; cap C15 contribution unless ASP/utilization/margin economics are refreshed"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"DUAL_USE_COPPER_PROCESSING_HIGH_MAE_LOCAL_4B","symbol":"103140","name":"풍산","trigger_type":"Stage4B","entry_date":"2024-04-26","entry_price":62900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.44,"MAE_30D_pct":-10.17,"MFE_90D_pct":25.44,"MAE_90D_pct":-25.28,"MFE_180D_pct":25.44,"MAE_180D_pct":-26.63,"forward_high_30d":78900,"forward_low_30d":56500,"forward_high_90d":78900,"forward_low_90d":47000,"forward_high_180d":78900,"forward_low_180d":46150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|103140|Stage4B|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_processing_4B","reuse_reason":"same Poongsan dual-use processing row from C15/C16 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"dual_use_processing_local_4B","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|103140|Stage4B|2024-04-26","non_price_bridge":"actual copper/non-ferrous processing plus defense dual-use supply relevance; high MAE requires order/margin/cash refresh","score_alignment":"Stage2 can open only with refreshed processing margin and cash evidence; otherwise local 4B"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINIUM_BATTERY_FOIL_HIGH_MFE_HIGH_MAE_LOCAL_4B","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage4B","entry_date":"2024-05-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.34,"MAE_30D_pct":-7.28,"MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"MFE_180D_pct":28.34,"MAE_180D_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|006110|Stage4B|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_foil_4B","reuse_reason":"same Sam-A Aluminium foil row from C15/C16/C13 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"foil_high_MFE_high_MAE_local_4B","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|006110|Stage4B|2024-05-20","non_price_bridge":"aluminium battery-foil material label without refreshed customer order, utilization, ASP/margin or cash bridge","score_alignment":"local 4B only; block Green until order/utilization/margin bridge refresh"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINIUM_ROLLING_COMMODITY_BETA_LOW_MFE_HIGH_MAE_HARD_4C","symbol":"018470","name":"조일알미늄","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":2470,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.29,"MAE_30D_pct":-17.41,"MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"MFE_180D_pct":7.29,"MAE_180D_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|018470|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same aluminium rolling hard counterexample from C15/C16/C13 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"aluminium_commodity_beta_hard_4C","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|018470|Stage4C|2024-05-20","non_price_bridge":"aluminium rolling commodity beta without company-specific ASP, utilization, margin or FCF bridge","score_alignment":"hard 4C; low MFE and high MAE reject material-spread bridge"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"PETROCHEM_PP_MATERIAL_LABEL_MARGIN_BALANCE_SHEET_DECAY_HARD_4C","symbol":"298000","name":"효성화학","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":71000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.41,"MAE_30D_pct":-16.20,"MFE_90D_pct":9.01,"MAE_90D_pct":-22.39,"MFE_180D_pct":9.01,"MAE_180D_pct":-60.35,"forward_high_30d":72000,"forward_low_30d":59500,"forward_high_90d":77400,"forward_low_90d":55100,"forward_high_180d":77400,"forward_low_180d":28150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|298000|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same Hyosung Chemical PP/petrochemical hard counterexample from C15/C17 loops","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"petrochemical_material_hard_4C","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|298000|Stage4C|2024-05-20","non_price_bridge":"PP/petrochemical material label without product-spread repair, FCF or balance-sheet relief","score_alignment":"hard 4C; severe 180D MAE shows material label failed"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NCC_PETROCHEM_BOTTOM_CALL_NO_SPREAD_REPAIR_HARD_4C","symbol":"011170","name":"롯데케미칼","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":118000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.24,"MAE_30D_pct":-12.29,"MFE_90D_pct":4.24,"MAE_90D_pct":-30.93,"MFE_180D_pct":4.24,"MAE_180D_pct":-43.64,"forward_high_30d":123000,"forward_low_30d":103500,"forward_high_90d":123000,"forward_low_90d":81500,"forward_high_180d":123000,"forward_low_180d":66500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|011170|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_NCC_hard_4C","reuse_reason":"same Lotte Chemical NCC bottom-call hard-block row from C17 files, reused as C15 false-positive check","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"NCC_bottom_call_hard_4C","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|011170|Stage4C|2024-05-20","non_price_bridge":"NCC/petrochemical bottom-call label without naphtha-to-product spread repair, utilization recovery, FCF or balance-sheet bridge","score_alignment":"hard 4C; generic petrochemical recovery failed material-spread test"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"PETROCHEM_LOW_MFE_DEEP_MAE_SPREAD_ABSENT_HARD_4C","symbol":"006650","name":"대한유화","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":151000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.65,"MAE_30D_pct":-16.56,"MFE_90D_pct":2.65,"MAE_90D_pct":-34.77,"MFE_180D_pct":2.65,"MAE_180D_pct":-48.34,"forward_high_30d":155000,"forward_low_30d":126000,"forward_high_90d":155000,"forward_low_90d":98500,"forward_high_180d":155000,"forward_low_180d":78000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|006650|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_petrochem_hard_4C","reuse_reason":"same petrochemical low-MFE/deep-MAE row from C17 files, reused as C15 false-positive check","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"petrochemical_spread_absent_hard_4C","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|006650|Stage4C|2024-05-20","non_price_bridge":"commodity chemical label without product spread, utilization, FCF or balance-sheet repair","score_alignment":"hard 4C; low MFE and deep MAE reject material-spread bridge"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"POLYSILICON_SPREAD_EVENT_CONTAMINATION_LOCAL_4B","symbol":"010060","name":"OCI홀딩스","trigger_type":"Stage4B","entry_date":"2024-02-27","entry_price":95100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.82,"MAE_30D_pct":-6.83,"MFE_90D_pct":25.13,"MAE_90D_pct":-17.56,"MFE_180D_pct":25.13,"MAE_180D_pct":-31.23,"forward_high_30d":113000,"forward_low_30d":88600,"forward_high_90d":119000,"forward_low_90d":78400,"forward_high_180d":119000,"forward_low_180d":65400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|010060|Stage4B|2024-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_poly_4B","reuse_reason":"same polysilicon/spread local-4B row from C17 files, reused as C15 solar-material spread check","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"polysilicon_spread_event_local_4B","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010060|Stage4B|2024-02-27","non_price_bridge":"polysilicon and solar-material spread exposure with policy/supply event noise; product spread and cash conversion refresh needed","score_alignment":"local 4B; block Green until polysilicon spread, shipment and FCF bridge refresh"}
{"row_type":"trigger","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SOLAR_CHEMICAL_VALUE_LABEL_NO_SPREAD_REPAIR_HARD_4C","symbol":"009830","name":"한화솔루션","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":28000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.36,"MAE_30D_pct":-21.43,"MFE_90D_pct":5.36,"MAE_90D_pct":-36.43,"MFE_180D_pct":5.36,"MAE_180D_pct":-43.75,"forward_high_30d":29500,"forward_low_30d":22000,"forward_high_90d":29500,"forward_low_90d":17800,"forward_high_180d":29500,"forward_low_180d":15750,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C15|009830|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_solar_chemical_hard_4C","reuse_reason":"same solar/chemical spread failure row from C17 files, reused as C15 material false-positive check","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"solar_chemical_value_label_hard_4C","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|009830|Stage4C|2024-05-20","non_price_bridge":"solar/chemical value label without product spread repair, utilization, inventory normalization or FCF bridge","score_alignment":"hard 4C; value label and policy beta failed material-spread test"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R4","selected_loop":109,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_NEW_MATERIAL_SPREAD_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["005490","003670","010130","001120","014680","178920","096770","011790","161000"],"candidate_names":["POSCO홀딩스","포스코퓨처엠","고려아연","LX인터내셔널","한솔케미칼","PI첨단소재","SK이노베이션","SKC","애경케미칼"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were unavailable or not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C15 evidence; distinguish ASP/volume/margin/FCF conversion from C16 resource policy, C17 chemical spread, C13 battery utilization and C32 governance contamination"}
```

---

## 6. Case analysis

### 6.1 Clean material-spread positives

```yaml
positive_controls:
  - 002380: specialty silicone/paint margin bridge.
  - 011780: synthetic rubber / specialty spread bridge; C17 boundary positive.
```

These rows show that C15 should not become a blanket hard-block. The right material story is not the commodity word; it is spread flowing into margin and FCF.

### 6.2 Smelter and governance contamination

```yaml
010130:
  90D_MFE_MAE: +16.42 / -3.94
  180D_MFE_MAE: +68.66 / -3.94
  route: local 4B / C32 contamination cap
```

The supply-tightness bridge may be real, but the later tender/control-premium path contaminates the full-window read. C15 must not learn governance MFE as material spread.

### 6.3 Battery-material and foil high-MFE 4B rows

```yaml
4B_rows:
  - 011790: battery/material event MFE; dominant-driver reclassification needed.
  - 006110: battery foil MFE but severe MAE; utilization/margin proof needed.
  - 103140: copper processing bridge but high MAE; order/margin refresh needed.
  - 010060: polysilicon spread/event; FCF refresh needed.
```

These rows are tradable but not automatically promotable. The bridge is the factory margin, not the ticker heat.

### 6.4 Hard 4C counterexamples

```yaml
hard_4C_rows:
  - 018470: aluminium rolling commodity beta.
  - 298000: leveraged PP/petrochemical label.
  - 011170: NCC bottom-call.
  - 006650: petrochemical spread absent.
  - 009830: solar/chemical value label.
```

The common failure is the same: material language without spread repair, utilization, balance-sheet relief or FCF.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 12
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 12
calibration_usable_trigger_count: 12
positive_case_count: 2
counterexample_count: 10
local_4B_watch_count: 5
hard_4C_count: 5
wrong_archetype_reclassification_count: 3
current_profile_error_count: 9
diversity_score_summary: "specialty material positive, synthetic rubber positive, smelter contamination, battery-material event, copper processing, foil 4B, aluminium hard 4C, petrochemical hard 4C, polysilicon 4B and solar chemical hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_adjacent_reuse_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C15 lesson |
|---|---:|---:|---:|---|
| 002380 | specialty positive | +20.49 / -7.79 | +41.39 / -7.79 | margin/FCF bridge validates |
| 011780 | chemical spread positive | +23.20 / -7.11 | +31.29 / -7.11 | product-spread boundary works |
| 010130 | smelter contamination | +16.42 / -3.94 | +68.66 / -3.94 | cap governance-contaminated window |
| 011790 | material event 4B | +70.94 / -8.03 | +70.94 / -20.17 | dominant-driver reclassification |
| 103140 | processing 4B | +25.44 / -25.28 | +25.44 / -26.63 | order/margin refresh needed |
| 006110 | foil 4B | +28.34 / -47.55 | +28.34 / -53.58 | high MFE no Green |
| 018470 | aluminium 4C | +7.29 / -41.30 | +7.29 / -44.70 | commodity beta failed |
| 298000 | PP 4C | +9.01 / -22.39 | +9.01 / -60.35 | balance-sheet bridge absent |
| 011170 | NCC 4C | +4.24 / -30.93 | +4.24 / -43.64 | bottom-call failed |
| 006650 | petrochem 4C | +2.65 / -34.77 | +2.65 / -48.34 | spread absent |
| 010060 | polysilicon 4B | +25.13 / -17.56 | +25.13 / -31.23 | event/spread refresh needed |
| 009830 | solar chemical 4C | +5.36 / -36.43 | +5.36 / -43.75 | value label failed |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"002380","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"Specialty material spread reached margin/FCF with controlled MAE.","MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"score_return_alignment_label":"specialty_material_margin_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable_C17_boundary","changed_components":[],"component_delta_explanation":"Synthetic rubber spread validates material economics but may be more specific to C17 chemical spread.","MFE_90D_pct":23.20,"MAE_90D_pct":-7.11,"score_return_alignment_label":"chemical_spread_positive_boundary","current_profile_verdict":"current_profile_correct_if_boundary_handled"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"010130","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":61,"stage_label_after":"Stage4B_governance_contamination_cap","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Smelter/supply-tightness bridge became contaminated by later tender mechanics.","MFE_90D_pct":16.42,"MAE_90D_pct":-3.94,"score_return_alignment_label":"smelter_spread_governance_contamination","current_profile_verdict":"requires_C32_contamination_cap"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"011790","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":57,"stage_label_after":"Stage4B_dominant_driver_reclassification","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"High MFE was dominated by battery/material event mechanics rather than verified ASP/utilization/FCF bridge.","MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"score_return_alignment_label":"battery_material_event_reclassification_4B","current_profile_verdict":"cap_or_reclassify"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"103140","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":64,"stage_label_after":"Stage4B_processing_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Real processing bridge exists, but high MAE requires order/margin/cash refresh.","MFE_90D_pct":25.44,"MAE_90D_pct":-25.28,"score_return_alignment_label":"processing_bridge_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"006110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":71,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":56,"stage_label_after":"Stage4B_foil_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Foil/resource label had high MFE but margin/utilization bridge was unrefreshed and MAE severe.","MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"score_return_alignment_label":"foil_high_MAE_local_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"018470","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":41,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Aluminium rolling commodity beta lacked company-specific ASP/utilization and price path rejected it.","MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"score_return_alignment_label":"aluminium_beta_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"298000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","dilution_cb_risk_score"],"component_delta_explanation":"PP/petrochemical label did not become spread repair or FCF; severe 180D drawdown confirms hard 4C.","MFE_90D_pct":9.01,"MAE_90D_pct":-22.39,"score_return_alignment_label":"leveraged_PP_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":4},"weighted_score_before":59,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Generic NCC bottom-call lacked product spread repair and price path rejected it.","MFE_90D_pct":4.24,"MAE_90D_pct":-30.93,"score_return_alignment_label":"NCC_bottom_call_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","dilution_cb_risk_score"],"component_delta_explanation":"Petrochemical label lacked spread/FCF bridge and showed low MFE with deep MAE.","MFE_90D_pct":2.65,"MAE_90D_pct":-34.77,"score_return_alignment_label":"petrochemical_spread_absent_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"010060","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":73,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":62,"stage_label_after":"Stage4B_polysilicon_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Polysilicon spread/event exposure had tradable MFE, but 180D MAE and policy/supply noise require FCF refresh.","MFE_90D_pct":25.13,"MAE_90D_pct":-17.56,"score_return_alignment_label":"polysilicon_event_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"009830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_before":59,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":2,"accounting_trust_risk_score":5},"weighted_score_after":37,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","dilution_cb_risk_score"],"component_delta_explanation":"Solar/chemical value label lacked spread repair, utilization or FCF bridge.","MFE_90D_pct":5.36,"MAE_90D_pct":-36.43,"score_return_alignment_label":"solar_chemical_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

---

## 9. Current calibrated profile stress test

The C15 material-spread-to-margin gate held:

```text
specialty material spread with margin/FCF bridge
→ keep Stage2

synthetic-rubber / chemical product spread with controlled MAE
→ Stage2 can survive but C17 boundary should remain visible

smelter/supply-tightness row later contaminated by tender
→ local 4B / cap and reclassify later window to C32

battery-material or foil event with high MFE and high MAE
→ local 4B, no Green

dual-use copper processing with high MAE
→ local 4B until order/margin/cash bridge refresh

generic aluminium rolling / petrochemical bottom-call / solar-chemical value label
→ hard 4C without spread repair and FCF bridge
```

### Rule candidate retained, not newly proposed

```text
C15_MATERIAL_SPREAD_ASP_VOLUME_MARGIN_FCF_GATE_V109_HELD_OUT

if C15
and material_commodity_metal_chemical_or_battery_material_label == true
and ASP_volume_utilization_inventory_margin_FCF_or_revision_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C15
and company_specific_spread_margin_FCF_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_margin_FCF_refresh = true
```

```text
if C15
and material_label_high_MFE == true
and MAE_90D_pct <= -20
and refreshed_margin_FCF_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C15
and commodity_beta_or_bottom_call == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C15
and governance_tender_or_policy_event_dominates_forward_window == true:
    cap_C15_contribution = true
    require_reclassification = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 12
    avg_MFE_90D_pct: 21.88
    avg_MAE_90D_pct: -23.67
    false_positive_risk: high_if_material_label_or_high_MFE_theme_rows_are_left_actionable
    verdict: adequate_only_with_C15_margin_FCF_gate
  P0b_e2r_2_1_reference:
    hypothesis: prior profile may overcredit material supercycle and high-MFE theme rows
    eligible_trigger_count: 12
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L4 material rows require ASP/volume/margin/FCF proof
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C15 requires company-level material spread conversion, not commodity beta
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: petrochemical, aluminium and solar-chemical labels without spread repair route hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | MATERIAL_SPREAD_ASP_VOLUME_MARGIN_FCF_HOLDOUT_V109 | 2 | 10 | 5 | 5 | 0 | 12 | 12 | 0 | 9 | false | false | 24 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 12
calibration_usable_trigger_count: 12
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 12
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
reused_case_count: 12
reused_case_ids:
  - C15|002380|Stage2-Actionable|2024-01-30
  - C15|011780|Stage2-Actionable|2024-02-26
  - C15|010130|Stage4B|2024-04-09
  - C15|011790|Stage4B|2024-05-23
  - C15|103140|Stage4B|2024-04-26
  - C15|006110|Stage4B|2024-05-20
  - C15|018470|Stage4C|2024-05-20
  - C15|298000|Stage4C|2024-05-20
  - C15|011170|Stage4C|2024-05-20
  - C15|006650|Stage4C|2024-05-20
  - C15|010060|Stage4B|2024-02-27
  - C15|009830|Stage4C|2024-05-20
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C15_material_spread_ASP_volume_margin_FCF_gate
  - adjacent_archetype_reclassification_guard
residual_error_types_found:
  - material_label_without_margin_FCF
  - high_MFE_material_theme_high_MAE
  - petrochemical_bottom_call_without_spread_repair
  - solar_chemical_value_label_without_FCF
  - governance_tender_contamination
new_axis_proposed: null
existing_axis_strengthened:
  - C15_MATERIAL_SPREAD_ASP_VOLUME_MARGIN_FCF_GATE_V109_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C15 candidate shards were unavailable or not recomputed
loop_contribution_label: duplicate_low_value_loop_with_adjacent_reuse_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"109","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":0,"reused_case_count":12,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C15_material_spread_ASP_volume_margin_FCF_gate","adjacent_archetype_reclassification_guard"],"residual_error_types_found":["material_label_without_margin_FCF","high_MFE_material_theme_high_MAE","petrochemical_bottom_call_without_spread_repair","solar_chemical_value_label_without_FCF","governance_tender_contamination"],"loop_contribution_label":"duplicate_low_value_loop_with_adjacent_reuse_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R4/C15 loop 109 as holdout validation only. Batch it with C15 loops 104~108, C16/C17 material-resource-chemical boundary rows, C32 governance-contamination rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C15 material-spread-to-ASP/volume/margin/FCF gate, high-MFE/high-MAE 4B guard, petrochemical hard-4C guard, and adjacent-archetype reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice POSCO홀딩스(005490), 포스코퓨처엠(003670), 고려아연(010130), LX인터내셔널(001120), 한솔케미칼(014680), PI첨단소재(178920), SK이노베이션(096770), SKC(011790), 애경케미칼(161000) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R4
completed_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```
