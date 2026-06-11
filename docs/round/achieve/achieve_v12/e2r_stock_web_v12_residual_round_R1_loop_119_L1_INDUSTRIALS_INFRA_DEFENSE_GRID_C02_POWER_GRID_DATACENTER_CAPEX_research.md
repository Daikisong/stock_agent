# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 119
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_ASP_DELIVERY_VISIBILITY_HOLDOUT_V119_TRANSFORMER_SWITCHGEAR_CABLE_THEME_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 267260/2024: source_proxy_reverify_required_from_loop_118
    - 298040/2024: source_proxy_reverify_required_from_loop_118
    - 010120/2024: source_proxy_reverify_required_from_loop_118
    - 103590/2024: source_proxy_reverify_required_from_loop_118
    - 001440/2024: source_proxy_reverify_required_from_loop_118
    - 000500/2024: source_proxy_reverify_required_from_loop_118
    - 033100/2024: source_proxy_reverify_required_from_loop_118
    - 006260/2024: source_proxy_reverify_required_from_loop_118
    - 024840/2024: source_proxy_reverify_required_from_loop_118
    - 017510/2024: source_proxy_reverify_required_from_loop_118
    - 006340/2024: not_recomputed_this_turn_future_C02_cable_candidate
    - 014910/2024: not_recomputed_this_turn_future_C02_grid_component_candidate
    - 080010/2024: not_recomputed_this_turn_future_C02_noise_check
    - 004090/2024: not_recomputed_this_turn_future_grid_component_candidate
    - 006200/2024: not_recomputed_this_turn_future_electrical_material_boundary
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - power_grid_datacenter_capex_to_backlog_margin_gate
  - transformer_switchgear_Capa_lock_positive_proxy
  - cable_material_theme_high_MAE_guard
  - holding_company_reclassification_cap_guard
  - source_proxy_reverification_required
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C02_POWER_GRID_DATACENTER_CAPEX` remains a Priority 0 archetype. The current no-repeat index marks C02 at 24 representative rows, still below the 30-row minimum. The v12 scheduler maps C01~C05 to `R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID`.

This file continues the local R1/C02 holdout after `R1/C02 loop 118`; selected loop is therefore `119`.

This is a **dedupe-aware source-proxy holdout / reprice TODO** MD. Direct fresh `Songdaiki/stock-web` symbol-year shard recomputation for the C02 candidates was not completed in this execution. Therefore every trigger row below is explicitly marked:

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

C02 should not reward `power grid`, `AI data center`, or `transformer shortage` as a label.

C02 should reward grid/data-center CAPEX only when it reaches execution economics:

```text
grid capex / data-center power demand / transformer shortage / switchgear expansion / cable capex
→ named backlog or order visibility
→ capacity lock / long-cycle delivery slot
→ ASP and mix improvement
→ margin and working-capital discipline
→ delivery cadence and cash conversion
→ price path validation
```

The recurring false positive is:

```text
AI data-center label
electric equipment theme
cable/copper material theme
low-float grid hardware blowoff
holding company discount rerating
generic power-equipment vocabulary
```

A transformer shortage is a traffic jam at the factory gate. C02 scores only when the company owns the delivery slot, has pricing power, and converts backlog into margin and cash. If the price move is mostly copper beta, theme heat, or holding-company rerating, C02 should cap and reclassify.

The C02 route split:

```text
transformer/switchgear backlog + capacity lock + ASP/margin bridge
→ Stage2 can survive

long-cycle backlog with high MFE but high MAE
→ local 4B until delivery/margin refresh

cable/copper theme without order/margin bridge
→ local 4B or hard 4C

holding company exposure
→ cap C02 and reclassify to holding/portfolio discount axis

small grid hardware label with low MFE/deep MAE
→ hard 4C

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
    - C02_POWER_GRID_DATACENTER_CAPEX
    - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
    - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C02 holdout validation
    - grid/datacenter capex to backlog/margin/cash gate
    - transformer/switchgear positive-control shape
    - cable/copper theme false-positive guard
    - source-proxy reprice TODO
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
  direct_reprice_status: not_recomputed_this_execution
  reason:
    - C02 loop 119 intentionally reuses loop 118 source-proxy rows as a dedupe holdout
    - no direct stock-web OHLC recomputation was completed for these C02 rows in this execution
    - exact same_entry_group_id rows from loop 118 must be deduped during aggregate ingest
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
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_BACKLOG_CAPACITY_LOCK_ASP_MARGIN_POSITIVE_CONTROL_SOURCE_PROXY","symbol":"267260","name":"HD현대일렉트릭","trigger_type":"Stage2-Actionable","entry_date":"2024-02-07","entry_price":96000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":46.88,"MAE_30D_pct":-6.25,"MFE_90D_pct":132.29,"MAE_90D_pct":-6.25,"MFE_180D_pct":210.42,"MAE_180D_pct":-8.85,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|267260|Stage2-Actionable|2024-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"transformer_backlog_Capa_lock_positive_control","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage2-Actionable|2024-02-07","non_price_bridge":"transformer backlog, overseas grid capex, capacity lock and ASP/mix improvement candidate; direct backlog/margin/cash evidence requires reverify","score_alignment":"Stage2 proxy only; Green blocked until backlog, delivery, ASP and working-capital cash bridge are directly verified"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_SWITCHGEAR_BACKLOG_MARGIN_POSITIVE_WITH_CAPACITY_EXPANSION_SOURCE_PROXY","symbol":"298040","name":"효성중공업","trigger_type":"Stage2-Actionable","entry_date":"2024-02-07","entry_price":177000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.98,"MAE_30D_pct":-8.47,"MFE_90D_pct":115.25,"MAE_90D_pct":-8.47,"MFE_180D_pct":190.96,"MAE_180D_pct":-12.43,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|298040|Stage2-Actionable|2024-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"transformer_switchgear_backlog_positive","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|298040|Stage2-Actionable|2024-02-07","non_price_bridge":"transformer/switchgear backlog and capacity expansion candidate with global grid demand; margin and cash bridge require reverify","score_alignment":"Stage2 proxy only; require delivery-slot, margin and receivable proof before Green"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_DATACENTER_CAPEX_ORDER_VISIBILITY_POSITIVE_CONTROL_SOURCE_PROXY","symbol":"010120","name":"LS ELECTRIC","trigger_type":"Stage2-Actionable","entry_date":"2024-04-08","entry_price":121000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":54.55,"MAE_30D_pct":-4.55,"MFE_90D_pct":122.31,"MAE_90D_pct":-9.09,"MFE_180D_pct":156.20,"MAE_180D_pct":-15.70,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|010120|Stage2-Actionable|2024-04-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"switchgear_datacenter_capex_positive","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|010120|Stage2-Actionable|2024-04-08","non_price_bridge":"switchgear, automation, data-center/grid capex order visibility candidate; backlog and segment margin require reverify","score_alignment":"Stage2 proxy only; Green requires order conversion, ASP/mix and delivery-margin evidence"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_TRANSFORMER_ORDER_BACKLOG_HIGH_MFE_HIGH_MAE_LOCAL_4B_SOURCE_PROXY","symbol":"103590","name":"일진전기","trigger_type":"Stage4B","entry_date":"2024-04-08","entry_price":19000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":63.16,"MAE_30D_pct":-7.89,"MFE_90D_pct":126.32,"MAE_90D_pct":-24.74,"MFE_180D_pct":145.79,"MAE_180D_pct":-31.58,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|103590|Stage4B|2024-04-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_high_MFE_high_MAE_4B_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed in this execution","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"cable_transformer_high_MAE_local_4B","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage4B|2024-04-08","non_price_bridge":"power cable/transformer order backlog candidate with high theme beta; high MAE requires backlog, ASP, delivery and working-capital proof","score_alignment":"local 4B proxy; high MFE cannot become Green without delivery-margin evidence"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HV_CABLE_EXPORT_BACKLOG_LOCAL_4B_COPPER_BETA_GUARD_SOURCE_PROXY","symbol":"001440","name":"대한전선","trigger_type":"Stage4B","entry_date":"2024-04-08","entry_price":12600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.86,"MAE_30D_pct":-8.73,"MFE_90D_pct":74.60,"MAE_90D_pct":-27.78,"MFE_180D_pct":89.68,"MAE_180D_pct":-36.51,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|001440|Stage4B|2024-04-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_cable_4B_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"HV_cable_export_backlog_local_4B","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|001440|Stage4B|2024-04-08","non_price_bridge":"HV cable export/backlog and grid capex candidate, but copper/material beta and dilution/working-capital risks require reverify","score_alignment":"local 4B proxy; cap until backlog margin and cash conversion are proven"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"CABLE_THEME_LOW_FLOAT_HIGH_MFE_HIGH_MAE_LOCAL_4B_SOURCE_PROXY","symbol":"000500","name":"가온전선","trigger_type":"Stage4B","entry_date":"2024-04-08","entry_price":33000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":112.12,"MAE_30D_pct":-5.45,"MFE_90D_pct":151.52,"MAE_90D_pct":-35.76,"MFE_180D_pct":151.52,"MAE_180D_pct":-48.48,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|000500|Stage4B|2024-04-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_cable_theme_4B_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"cable_theme_low_float_local_4B","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|000500|Stage4B|2024-04-08","non_price_bridge":"cable/grid theme and possible export capacity leverage, but high MAE and low-float theme risk require reverify","score_alignment":"local 4B; do not learn theme MFE as C02 Green"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_SMALLCAP_CAPA_LOCK_POSITIVE_WITH_LIQUIDITY_4B_SOURCE_PROXY","symbol":"033100","name":"제룡전기","trigger_type":"Stage4B","entry_date":"2024-03-11","entry_price":39200,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":83.67,"MAE_30D_pct":-6.38,"MFE_90D_pct":160.20,"MAE_90D_pct":-14.80,"MFE_180D_pct":160.20,"MAE_180D_pct":-32.65,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|033100|Stage4B|2024-03-11","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_smallcap_transformer_4B_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"smallcap_transformer_capacity_lock_local_4B","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|033100|Stage4B|2024-03-11","non_price_bridge":"small-cap transformer capacity/backlog candidate with strong MFE; liquidity, margin and delivery-cash evidence require reverify","score_alignment":"local 4B; cap until direct backlog/ASP/margin proof is verified"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HOLDING_COMPANY_POWER_CABLE_TRANSFORMER_EXPOSURE_RECLASSIFICATION_CAP_SOURCE_PROXY","symbol":"006260","name":"LS","trigger_type":"Stage2-Watch","entry_date":"2024-04-08","entry_price":105000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.19,"MAE_30D_pct":-5.71,"MFE_90D_pct":68.57,"MAE_90D_pct":-16.67,"MFE_180D_pct":75.24,"MAE_180D_pct":-28.57,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|006260|Stage2-Watch|2024-04-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_reclassification_cap_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"holding_company_reclassification_cap","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|006260|Stage2-Watch|2024-04-08","non_price_bridge":"holding-company exposure to power cable/switchgear/grid equipment; direct C02 backlog and margin bridge not isolated","score_alignment":"cap C02 contribution; reclassify holding/portfolio discount if dominant"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"COPPER_CABLE_MATERIAL_THEME_WITHOUT_BACKLOG_MARGIN_BRIDGE_HARD_4C_SOURCE_PROXY","symbol":"024840","name":"KBI메탈","trigger_type":"Stage4C","entry_date":"2024-04-08","entry_price":2800,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":50.00,"MAE_30D_pct":-17.86,"MFE_90D_pct":50.00,"MAE_90D_pct":-42.86,"MFE_180D_pct":50.00,"MAE_180D_pct":-53.57,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|024840|Stage4C|2024-04-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"copper_cable_material_theme_hard_4C","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|024840|Stage4C|2024-04-08","non_price_bridge":"copper/cable material theme without visible grid/datacenter backlog, delivery slot, ASP/mix or margin cash bridge","score_alignment":"hard 4C proxy; high MFE with deep MAE must not become C02 positive"}
{"row_type":"trigger","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_HARDWARE_THEME_WITHOUT_ORDER_VISIBILITY_HARD_4C_SOURCE_PROXY","symbol":"017510","name":"세명전기","trigger_type":"Stage4C","entry_date":"2024-04-08","entry_price":5250,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.52,"MAE_30D_pct":-13.33,"MFE_90D_pct":29.52,"MAE_90D_pct":-38.10,"MFE_180D_pct":29.52,"MAE_180D_pct":-48.57,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C02|017510|Stage4C|2024-04-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C_source_proxy","reuse_reason":"C02 source-proxy row reused from loop 118; direct stock-web shard not recomputed","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"grid_hardware_theme_hard_4C","novelty_key":"C02_POWER_GRID_DATACENTER_CAPEX|017510|Stage4C|2024-04-08","non_price_bridge":"grid hardware theme without direct order visibility, backlog conversion or margin/cash bridge","score_alignment":"hard 4C proxy; require direct order and delivery evidence before reopening"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_NEW_POWER_GRID_DATACENTER_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["267260","298040","010120","103590","001440","000500","033100","006260","024840","017510","006340","014910","080010"],"candidate_names":["HD현대일렉트릭","효성중공업","LS ELECTRIC","일진전기","대한전선","가온전선","제룡전기","LS","KBI메탈","세명전기","대원전선","성문전자","이상네트웍스-grid_noise_check"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were not recomputed in this execution; no fresh independent 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C02 evidence; distinguish transformer/switchgear backlog and delivery-margin bridge from cable/copper theme, C15/C16 material beta, holding-company discount and AI-data-center label"}
```

---

## 6. Case analysis

### 6.1 Transformer / switchgear positive-control proxies

```yaml
positive_proxy_rows:
  - 267260: transformer backlog and capacity lock candidate.
  - 298040: transformer/switchgear backlog and capacity expansion candidate.
  - 010120: switchgear/datacenter capex order visibility candidate.
```

These are the C02-positive shapes. The business logic is clear: long-cycle equipment, capacity scarcity, ASP/mix improvement, global grid/data-center demand. But all three are `source_proxy_only` in this execution, so the scorer must reprice them directly and verify backlog, delivery cadence, segment margin and receivables before use.

### 6.2 Cable / power-line high-MFE high-MAE rows

```yaml
local_4B_proxy_rows:
  - 103590: power cable/transformer backlog candidate but high MAE.
  - 001440: HV cable backlog candidate with copper/material beta risk.
  - 000500: cable theme / possible export capacity leverage, high MAE.
  - 033100: small-cap transformer capacity lock candidate, liquidity and margin reverify required.
```

These rows can be real, but they are exactly where 4B belongs. High MFE proves that the market cared; high MAE proves the evidence was not yet mature enough for Green.

### 6.3 Holding company exposure

```yaml
reclassification_proxy:
  - 006260: LS holding-company exposure to power cable / switchgear / grid equipment.
```

The operating exposure can be real, but C02 should not steal holding-company discount or portfolio rerating evidence. If the bridge is indirect, C02 contribution must be capped.

### 6.4 Theme hard 4C rows

```yaml
hard_4C_proxy_rows:
  - 024840: copper/cable material theme without backlog/margin bridge.
  - 017510: grid hardware theme without order visibility.
```

These rows protect the model from learning theme heat as execution. A cable or grid word is not backlog; backlog is a delivery book with margin and cash.

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
local_4B_watch_count: 4
hard_4C_count: 2
wrong_archetype_reclassification_count: 1
current_profile_error_count: 7
diversity_score_summary: "transformer/switchgear positive proxies, cable high-MAE 4B, holding-company reclassification cap, copper/cable hard 4C and grid hardware hard 4C covered; all rows source-proxy-only and require direct stock-web reprice"
loop_contribution_label: duplicate_low_value_loop_with_source_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C02 lesson |
|---|---:|---:|---:|---|
| 267260 | transformer positive proxy | +132.29 / -6.25 | +210.42 / -8.85 | backlog/CAPA lock can validate after reprice |
| 298040 | transformer/switchgear proxy | +115.25 / -8.47 | +190.96 / -12.43 | margin/cash proof needed |
| 010120 | switchgear/DC capex proxy | +122.31 / -9.09 | +156.20 / -15.70 | order conversion proof needed |
| 103590 | cable/transformer 4B | +126.32 / -24.74 | +145.79 / -31.58 | high MFE, delivery-margin reverify |
| 001440 | HV cable 4B | +74.60 / -27.78 | +89.68 / -36.51 | copper/material beta risk |
| 000500 | cable theme 4B | +151.52 / -35.76 | +151.52 / -48.48 | theme MFE no Green |
| 033100 | small transformer 4B | +160.20 / -14.80 | +160.20 / -32.65 | liquidity/margin reverify |
| 006260 | holding cap | +68.57 / -16.67 | +75.24 / -28.57 | cap C02 if holding discount dominates |
| 024840 | copper/cable 4C | +50.00 / -42.86 | +50.00 / -53.57 | theme heat failed bridge |
| 017510 | grid hardware 4C | +29.52 / -38.10 | +29.52 / -48.57 | no direct order visibility |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":86,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":86,"stage_label_after":"Stage2_Useful_but_source_repair_required","changed_components":[],"component_delta_explanation":"Transformer backlog/CAPA-lock shape fits C02, but direct stock-web reprice and segment margin/cash evidence are required before promotion.","MFE_90D_pct":132.29,"MAE_90D_pct":-6.25,"source_proxy_only":true,"score_return_alignment_label":"transformer_backlog_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":84,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":81,"stage_label_after":"Stage2_Useful_but_source_repair_required","changed_components":["margin_bridge_score"],"component_delta_explanation":"Transformer/switchgear bridge is plausible, but margin and working-capital proof are not directly verified in this run.","MFE_90D_pct":115.25,"MAE_90D_pct":-8.47,"source_proxy_only":true,"score_return_alignment_label":"transformer_switchgear_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":77,"stage_label_after":"Stage2_Useful_but_source_repair_required","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Switchgear/datacenter capex bridge needs direct order-conversion and segment-margin verification.","MFE_90D_pct":122.31,"MAE_90D_pct":-9.09,"source_proxy_only":true,"score_return_alignment_label":"switchgear_datacenter_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"103590","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":76,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":59,"stage_label_after":"Stage4B_source_repair_required","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Cable/transformer row has high MFE but high MAE; delivery-margin evidence is not directly verified.","MFE_90D_pct":126.32,"MAE_90D_pct":-24.74,"source_proxy_only":true,"score_return_alignment_label":"cable_transformer_high_MAE_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"001440","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":4},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":1,"accounting_trust_risk_score":5},"weighted_score_after":58,"stage_label_after":"Stage4B_cable_reverify_required","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"HV cable exposure may be real but copper beta, dilution/working-capital and margin bridge need verification.","MFE_90D_pct":74.60,"MAE_90D_pct":-27.78,"source_proxy_only":true,"score_return_alignment_label":"HV_cable_local_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"000500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":52,"stage_label_after":"Stage4B_theme_reverify_required","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Cable theme MFE is not enough; high MAE and low-float risk require order/margin proof.","MFE_90D_pct":151.52,"MAE_90D_pct":-35.76,"source_proxy_only":true,"score_return_alignment_label":"cable_theme_high_MAE_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"033100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":68,"stage_label_after":"Stage4B_smallcap_transformer_reverify_required","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Small-cap transformer row may have real capacity lock, but liquidity and margin/cash proof are not verified; 180D MAE blocks Green.","MFE_90D_pct":160.20,"MAE_90D_pct":-14.80,"source_proxy_only":true,"score_return_alignment_label":"smallcap_transformer_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"006260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":48,"stage_label_after":"Reclassify_holding_company_or_Stage2_cap","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Holding-company exposure should not be learned as pure C02 backlog/margin evidence unless operating bridge is isolated.","MFE_90D_pct":68.57,"MAE_90D_pct":-16.67,"source_proxy_only":true,"score_return_alignment_label":"holding_company_C02_cap_proxy","current_profile_verdict":"requires_reclassification_or_operating_bridge"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"024840","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Copper/cable material theme lacks direct grid/datacenter backlog and margin bridge; deep MAE implies hard block.","MFE_90D_pct":50.00,"MAE_90D_pct":-42.86,"source_proxy_only":true,"score_return_alignment_label":"copper_cable_theme_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"017510","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C_source_repair_required","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Grid hardware theme lacks order visibility and cash bridge; deep MAE blocks positive C02 credit.","MFE_90D_pct":29.52,"MAE_90D_pct":-38.10,"source_proxy_only":true,"score_return_alignment_label":"grid_hardware_theme_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
```

---

## 9. Current calibrated profile stress test

The C02 grid/datacenter-capex execution gate held:

```text
transformer/switchgear backlog with capacity lock
→ Stage2 can survive after direct reprice and margin/cash proof

cable export/backlog with copper beta and high MAE
→ local 4B, no Green

small-cap transformer/cable theme with huge MFE
→ local 4B until liquidity, delivery and margin proof

holding company exposure
→ cap C02 and reclassify if holding discount dominates

copper/cable material theme without direct backlog
→ hard 4C

grid hardware theme without order visibility
→ hard 4C
```

### Rule candidate retained, not newly proposed

```text
C02_POWER_GRID_DATACENTER_CAPEX_TO_BACKLOG_MARGIN_CASH_GATE_V119_HELD_OUT

if C02
and power_grid_datacenter_transformer_switchgear_or_cable_label == true
and backlog_delivery_slot_ASP_margin_working_capital_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C02
and transformer_switchgear_backlog_Capa_lock_bridge == true
and MFE_90D_pct >= +50
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_backlog_margin_cash_reprice = true
```

```text
if C02
and cable_or_grid_theme == true
and MFE_90D_pct >= +50
and MAE_90D_pct <= -20
and direct_backlog_margin_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C02
and holding_company_exposure == true
and operating_backlog_margin_bridge_isolated == false:
    cap_C02_contribution = true
    require_reclassification = true
```

```text
if C02
and copper_material_or_grid_hardware_theme == true
and MAE_90D_pct <= -30
and direct_order_visibility == false:
    route = Stage4C
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 0
    source_proxy_trigger_count: 10
    avg_proxy_MFE_90D_pct: 103.07
    avg_proxy_MAE_90D_pct: -22.61
    false_positive_risk: high_if_theme_MFE_is_learned_without_direct_backlog_margin_bridge
    verdict: do_not_update_until_reprice
  P0b_e2r_2_1_reference:
    hypothesis: prior calibrated profile likely overcredits theme heat if proxy rows are used raw
    eligible_trigger_count: 0
    verdict: not_tested_this_execution
  P1_sector_specific_candidate_profile:
    hypothesis: L1 grid/datacenter capex requires direct backlog/delivery/margin/cash bridge
    changed_axes: none_new_holdout_only
    verdict: pass_as_guardrail_logic_only
  P2_canonical_archetype_candidate_profile:
    hypothesis: C02 requires transformer/switchgear/cable execution, not AI data-center or copper theme
    changed_axes: none_new_holdout_only
    verdict: pass_as_guardrail_logic_only
  P3_counterexample_guard_profile:
    hypothesis: cable/copper/grid hardware theme rows without direct order visibility route to 4B/4C
    changed_axes: none_new_holdout_only
    verdict: strongest_false_positive_control_but_reprice_required
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | POWER_GRID_DATACENTER_CAPEX_HOLDOUT_V119 | 3 | 7 | 4 | 2 | 0 | 10 | 0 | 0 | 7 | false | false | 6 |

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
  - C02|267260|Stage2-Actionable|2024-02-07
  - C02|298040|Stage2-Actionable|2024-02-07
  - C02|010120|Stage2-Actionable|2024-04-08
  - C02|103590|Stage4B|2024-04-08
  - C02|001440|Stage4B|2024-04-08
  - C02|000500|Stage4B|2024-04-08
  - C02|033100|Stage4B|2024-03-11
  - C02|006260|Stage2-Watch|2024-04-08
  - C02|024840|Stage4C|2024-04-08
  - C02|017510|Stage4C|2024-04-08
new_symbol_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 10
batch_reverification_required_count: 10
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C02_grid_datacenter_capex_to_backlog_margin_cash_gate
  - holding_company_reclassification_guard
residual_error_types_found:
  - theme_MFE_without_direct_backlog_margin_bridge
  - cable_copper_material_beta_contamination
  - smallcap_grid_hardware_order_visibility_gap
  - holding_company_exposure_misfile
  - source_proxy_price_reverification_gap
new_axis_proposed: null
existing_axis_strengthened:
  - C02_POWER_GRID_DATACENTER_CAPEX_TO_BACKLOG_MARGIN_CASH_GATE_V119_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows are source_proxy_only and reused from loop 118 because direct fresh C02 stock-web candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_source_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"119","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":0,"reused_case_count":10,"new_symbol_count":0,"new_trigger_family_count":0,"source_proxy_only_count":10,"batch_reverification_required_count":10,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C02_grid_datacenter_capex_to_backlog_margin_cash_gate","holding_company_reclassification_guard"],"residual_error_types_found":["theme_MFE_without_direct_backlog_margin_bridge","cable_copper_material_beta_contamination","smallcap_grid_hardware_order_visibility_gap","holding_company_exposure_misfile","source_proxy_price_reverification_gap"],"loop_contribution_label":"duplicate_low_value_loop_with_source_proxy_reverify_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R1/C02 loop 119 as source-proxy holdout validation only. Batch it with C02 loop 118, existing C02 rows, C03/C05 adjacent L1 industrial rows, C15/C16 material contamination rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. All trigger rows in this file must be directly repriced against Songdaiki/stock-web before aggregate use because calibration_usable=false and source_proxy_only=true. Preserve the C02 grid/datacenter-capex-to-backlog-margin-cash gate, cable/copper theme 4B/4C guard, and holding-company reclassification guard, but do not create a new weight delta from this loop. Future research should directly reprice HD현대일렉트릭(267260), 효성중공업(298040), LS ELECTRIC(010120), 일진전기(103590), 대한전선(001440), 가온전선(000500), 제룡전기(033100), LS(006260), KBI메탈(024840), 세명전기(017510), 대원전선(006340), 성문전자(014910), 광명전기(017040), 피앤씨테크(237750), 서전기전(189860) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R1
completed_loop: 119
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```
