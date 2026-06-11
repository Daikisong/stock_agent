# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R3
selected_loop: 138
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: AMPC_IRA_JV_UTILIZATION_TO_CASH_CONVERSION_HOLDOUT_V138_CELL_SEPARATOR_FOIL_MATERIAL_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 373220/2024: reused_from_prior_local_C13_loop_137_AMPC_positive_row
    - 361610/2024: reused_from_prior_local_C13_loop_137_separator_hard_4C_row
    - 011790/2024: reused_from_prior_local_C13_C15_C16_battery_material_4B_row
    - 006110/2024: reused_from_prior_local_C13_C15_C16_foil_4B_row
    - 018470/2024: reused_from_prior_local_C13_C15_C16_hard_4C_row
    - 006400/2024: not_recomputed_this_turn_future_cell_OEM_calloff_AMPC_candidate
    - 096770/2024: not_recomputed_this_turn_future_cell_AMPC_JV_boundary
    - 003670/2024: not_recomputed_this_turn_future_material_JV_utilization_candidate
    - 247540/2024: not_recomputed_this_turn_future_cathode_customer_JV_candidate
    - 121600/2024: not_recomputed_this_turn_future_material_utilization_candidate
    - 278280/2024: not_recomputed_this_turn_future_electrolyte_material_candidate
    - 393890/2024: not_recomputed_this_turn_future_separator_capacity_candidate
    - 348370/2024: not_recomputed_this_turn_future_electrolyte_AMPC_boundary
    - 357780/2024: not_recomputed_this_turn_future_material_supplier_boundary
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - AMPC_IRA_JV_utilization_to_cash_gate
  - separator_policy_label_hard_4C_guard
  - battery_material_event_reclassification_guard
  - foil_high_MFE_high_MAE_local_4B_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C13_BATTERY_JV_UTILIZATION_AMPC_IRA` remains a Priority 0 archetype. The current no-repeat index marks C13 as below the 30-row minimum, and the v12 scheduler maps C11~C14 to `R3 / L3_BATTERY_EV_GREEN_MOBILITY`.

This file continues the local C13 sequence after `R3/C13 loop 137`; selected loop is therefore `138`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct fresh C13 AMPC/JV/utilization candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C13/C31/C15/C16 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

```yaml
loop_138_note:
  independence_status: duplicate_holdout_only
  fresh_reprice_status: not_recomputed_this_execution
  reason: C13 remains under-covered, but this run reuses prior C13/C12/C15/C16/C31 boundary rows and must not create a new weight delta.
```


C13 should not reward the words `AMPC`, `IRA`, `JV`, or `localization` by themselves.

C13 should reward only when the policy/JV headline reaches battery operating cash:

```text
IRA / AMPC / JV / localization / battery supply-chain policy
→ named cell or material capacity
→ utilization / customer call-off
→ AMPC recognition and cash conversion
→ customer diversification or ESS / non-EV pull
→ margin, working capital and FCF bridge
→ price path validation
```

The recurring false positive is:

```text
battery policy label
separator localization
battery material theme
foil capacity proxy
commodity material beta
AMPC headline without utilization
```

A tax credit is not cash until production, utilization and qualification pull it through the factory gate. A JV is not cash until the line runs, the customer calls off volume, and the accounting bridge shows up.

The C13 route split remains:

```text
AMPC/IRA + utilization/customer/cash bridge
→ keep Stage2

AMPC/IRA label without utilization
→ cap or hard 4C

separator/localization label without customer pull
→ hard 4C

battery material event with unclear dominant driver
→ local 4B / reclassification watch

foil or material high-MFE high-MAE
→ local 4B until customer/utilization/margin refresh

commodity material beta with low MFE/deep MAE
→ hard 4C
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 5
  actual_trigger_rows: 5
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
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
    - C13 holdout validation
    - AMPC/IRA utilization-to-cash bridge gate
    - separator/localization false-positive guard
    - battery material reclassification guard
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
  - R3/C13 loop 135
  - R3/C13 loop 136
  - R3/C13 loop 137
  - R11/C31 loops 103~108
  - R4/C15 loops 105~108
  - R4/C16 loops 112~115
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C13 candidate shards were unavailable or returned cache miss in this execution
  - exact duplicate C13 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R3","selected_loop":138,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_IRA_UTILIZATION_CUSTOMER_DIVERSIFICATION_CASH_BRIDGE_POSITIVE","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_price":332500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.50,"MAE_30D_pct":-6.47,"MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"MFE_180D_pct":33.53,"MAE_180D_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C13|373220|Stage2-Actionable|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same LGES AMPC/IRA utilization row from C31/C13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"AMPC_IRA_positive_control","novelty_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Actionable|2024-07-25","non_price_bridge":"IRA/AMPC support plus utilization, customer diversification and ESS/non-EV demand bridge","score_alignment":"keep Stage2; block Green until AMPC cash conversion, utilization and customer call-off refresh"}
{"row_type":"trigger","selected_round":"R3","selected_loop":138,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_LOCALIZATION_POLICY_LABEL_WITHOUT_UTILIZATION_HARD_4C","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C13|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same separator policy false-positive row from C31/C13 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"separator_policy_hard_counterexample","novelty_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|361610|Stage4C|2024-05-16","non_price_bridge":"separator/localization policy exposure without customer pull, utilization, parent financing or cash-conversion bridge","score_alignment":"hard 4C; localization or AMPC-adjacent label cannot substitute for utilization and cashflow"}
{"row_type":"trigger","selected_round":"R3","selected_loop":138,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_MATERIAL_EVENT_HIGH_MFE_DOMINANT_DRIVER_RECLASSIFICATION_4B","symbol":"011790","name":"SKC","trigger_type":"Stage4B","entry_date":"2024-05-23","entry_price":117000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":70.94,"MAE_30D_pct":0.00,"MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"MFE_180D_pct":70.94,"MAE_180D_pct":-20.17,"forward_high_30d":200000,"forward_low_30d":117000,"forward_high_90d":200000,"forward_low_90d":107600,"forward_high_180d":200000,"forward_low_180d":93400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C13|011790|Stage4B|2024-05-23","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_event_contamination_4B","reuse_reason":"same SKC battery/material event row from C16/C17 guardrails; reused as C13 dominant-driver split","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"battery_material_event_local_4B","novelty_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|011790|Stage4B|2024-05-23","non_price_bridge":"battery/material event-driven MFE rather than confirmed cell JV utilization, customer call-off or AMPC cash bridge","score_alignment":"local 4B; cap C13 contribution unless JV/utilization/customer economics are refreshed"}
{"row_type":"trigger","selected_round":"R3","selected_loop":138,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_FOIL_CAPACITY_PROXY_HIGH_MFE_HIGH_MAE_LOCAL_4B","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage4B","entry_date":"2024-05-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.34,"MAE_30D_pct":-7.28,"MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"MFE_180D_pct":28.34,"MAE_180D_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C13|006110|Stage4B|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_foil_4B","reuse_reason":"same aluminium battery-foil high-MAE row from C15/C16 guardrails; reused as C13 customer-utilization proxy split","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"foil_capacity_proxy_local_4B","novelty_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006110|Stage4B|2024-05-20","non_price_bridge":"aluminium battery-foil capacity/material label without refreshed customer order, utilization, ASP/margin or AMPC-linked cash bridge","score_alignment":"local 4B only; block Green until order/utilization/margin bridge refresh"}
{"row_type":"trigger","selected_round":"R3","selected_loop":138,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"ALUMINIUM_ROLLING_BATTERY_PROXY_LOW_MFE_DEEP_MAE_HARD_4C","symbol":"018470","name":"조일알미늄","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":2470,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.29,"MAE_30D_pct":-17.41,"MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"MFE_180D_pct":7.29,"MAE_180D_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C13|018470|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same aluminium rolling hard counterexample from C15/C16 guardrails; reused as C13 battery-proxy false-positive control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"battery_proxy_hard_4C","novelty_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|018470|Stage4C|2024-05-20","non_price_bridge":"aluminium rolling commodity beta / battery proxy label without customer call-off, utilization, margin or AMPC cash bridge","score_alignment":"hard 4C; low MFE and high MAE reject battery-JV/utilization bridge"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R3","selected_loop":138,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_NEW_BATTERY_JV_AMPC_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["373220","006400","096770","003670","247540","121600","278280"],"candidate_names":["LG에너지솔루션","삼성SDI","SK이노베이션","포스코퓨처엠","에코프로비엠","나노신소재","천보"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C13 evidence; distinguish AMPC/JV utilization cash bridge from C12 customer-calloff risk and C15/C16 material spread/resource labels"}
```

---

## 6. Case analysis

### 6.1 LG Energy Solution / 373220 — AMPC/IRA utilization positive-control

```yaml
entry_price: 332500
90D_MFE_MAE: +33.53 / -6.47
180D_MFE_MAE: +33.53 / -6.47
route: Stage2-Actionable
```

This is the C13 positive-control. The policy bridge is not merely an IRA label: the row carries utilization, customer diversification and ESS/non-EV demand as the reason AMPC support can reach cash conversion. Green is still blocked until AMPC cash recognition and customer call-off refresh.

### 6.2 SK IE Technology / 361610 — separator/localization hard 4C

```yaml
entry_price: 57600
90D_MFE_MAE: +1.04 / -46.27
180D_MFE_MAE: +1.04 / -60.68
route: Stage4C
```

This is the strongest C13 hard counterexample. Localization and separator policy exposure cannot replace utilization, parent financing and customer pull.

### 6.3 SKC / 011790 — battery material event contamination 4B

```yaml
entry_price: 117000
90D_MFE_MAE: +70.94 / -8.03
180D_MFE_MAE: +70.94 / -20.17
route: Stage4B / reclassification watch
```

The MFE is real, but C13 must ask whether the dominant driver is JV/utilization/AMPC cash conversion or a battery-material event. Without that bridge, the row remains 4B and may belong to C15/C16/C17.

### 6.4 Sam-A Aluminium / 006110 — foil capacity proxy 4B

```yaml
entry_price: 75500
90D_MFE_MAE: +28.34 / -47.55
180D_MFE_MAE: +28.34 / -53.58
route: Stage4B
```

High MFE proves tradability, not durability. This is a foil/capacity proxy row, and customer order, utilization and margin evidence must refresh before promotion.

### 6.5 Choil Aluminium / 018470 — battery proxy hard 4C

```yaml
entry_price: 2470
90D_MFE_MAE: +7.29 / -41.30
180D_MFE_MAE: +7.29 / -44.70
route: Stage4C
```

This row blocks the tendency to use battery proxy vocabulary as a bridge. It failed both price path and non-price bridge.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 5
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 1
counterexample_count: 4
local_4B_watch_count: 2
hard_4C_count: 2
wrong_archetype_reclassification_count: 1
current_profile_error_count: 4
diversity_score_summary: "AMPC positive, separator hard 4C, battery-material event 4B/reclassification, foil high-MFE 4B, aluminium battery-proxy hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C13 lesson |
|---|---:|---:|---:|---|
| 373220 | AMPC/IRA positive | +33.53 / -6.47 | +33.53 / -6.47 | utilization/cash bridge validates |
| 361610 | separator hard 4C | +1.04 / -46.27 | +1.04 / -60.68 | localization label fails |
| 011790 | material event 4B | +70.94 / -8.03 | +70.94 / -20.17 | dominant-driver reclassification needed |
| 006110 | foil 4B | +28.34 / -47.55 | +28.34 / -53.58 | customer/utilization refresh needed |
| 018470 | proxy hard 4C | +7.29 / -41.30 | +7.29 / -44.70 | battery-proxy label fails |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":85,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":["revision_score","accounting_trust_risk_score"],"component_delta_explanation":"AMPC/IRA support reached utilization and customer demand bridge with controlled MAE; Green still needs cash conversion refresh.","MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"score_return_alignment_label":"AMPC_cash_bridge_positive","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Separator/localization label lacked utilization, customer pull, parent financing and cash conversion.","MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"score_return_alignment_label":"separator_policy_label_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":58,"stage_label_after":"Stage4B_dominant_driver_reclassification","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"High MFE was dominated by battery/material event mechanics rather than C13 JV/utilization/AMPC cash bridge.","MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"score_return_alignment_label":"battery_material_event_reclassification_4B","current_profile_verdict":"cap_or_reclassify"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"006110","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":71,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":56,"stage_label_after":"Stage4B_foil_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Foil/capacity proxy had high MFE but customer/utilization/margin bridge was unrefreshed and MAE severe.","MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"score_return_alignment_label":"foil_capacity_high_MAE_local_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"018470","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":41,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Aluminium rolling battery-proxy label lacked customer call-off, utilization, margin and AMPC cash bridge.","MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"score_return_alignment_label":"battery_proxy_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

---

## 9. Current calibrated profile stress test

The C13 AMPC/JV-utilization-to-cash gate held:

```text
AMPC/IRA with utilization and customer demand bridge
→ Stage2 can survive

separator/localization label without utilization
→ hard 4C

battery-material event without JV/utilization cash bridge
→ local 4B / reclassify

foil capacity proxy with high MFE and severe MAE
→ local 4B, no Green

battery proxy / commodity material beta with low MFE and deep MAE
→ hard 4C
```

### Rule candidate retained, not newly proposed

```text
C13_AMPC_IRA_JV_UTILIZATION_TO_CASH_CONVERSION_GATE_V138_HELD_OUT

if C13
and AMPC_IRA_JV_localization_or_battery_policy_label == true
and utilization_customer_calloff_AMPC_cash_margin_or_FCF_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C13
and AMPC_IRA_cash_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_cash_conversion_refresh = true
```

```text
if C13
and separator_or_localization_label == true
and utilization_customer_pull_or_parent_financing_bridge == false
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C13
and battery_material_or_capacity_proxy == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -20
and utilization_customer_margin_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C13
and dominant_driver_belongs_to_C12_C15_C16_or_C17 == true:
    cap_C13_contribution = true
    require_reclassification = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 5
    avg_MFE_90D_pct: 28.23
    avg_MAE_90D_pct: -29.92
    false_positive_risk: high_if_AMPC_or_localization_labels_are_left_actionable
    verdict: adequate_only_with_C13_utilization_cash_bridge_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for IRA/AMPC/JV/localization labels
    eligible_trigger_count: 5
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L3 battery rows require utilization/customer/cash conversion bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C13 requires AMPC/JV utilization and cash conversion, not material proxy
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: separator/localization and battery-proxy rows without utilization route to hard 4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | AMPC_IRA_JV_UTILIZATION_TO_CASH_HOLDOUT_V138 | 1 | 4 | 2 | 2 | 0 | 5 | 5 | 0 | 4 | false | false | 15 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 5
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
reused_case_count: 5
reused_case_ids:
  - C13|373220|Stage2-Actionable|2024-07-25
  - C13|361610|Stage4C|2024-05-16
  - C13|011790|Stage4B|2024-05-23
  - C13|006110|Stage4B|2024-05-20
  - C13|018470|Stage4C|2024-05-20
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C13_AMPC_IRA_JV_utilization_to_cash_gate
  - dominant_driver_reclassification_guard
residual_error_types_found:
  - AMPC_label_without_cash_conversion
  - separator_localization_without_utilization
  - battery_material_event_wrong_bridge
  - foil_capacity_proxy_high_MAE
  - battery_proxy_commodity_false_positive
new_axis_proposed: null
existing_axis_strengthened:
  - C13_AMPC_IRA_JV_UTILIZATION_TO_CASH_CONVERSION_GATE_V138_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C13 AMPC/JV/utilization candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"138","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","new_independent_case_count":0,"reused_case_count":5,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C13_AMPC_IRA_JV_utilization_to_cash_gate","dominant_driver_reclassification_guard"],"residual_error_types_found":["AMPC_label_without_cash_conversion","separator_localization_without_utilization","battery_material_event_wrong_bridge","foil_capacity_proxy_high_MAE","battery_proxy_commodity_false_positive"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R3/C13 loop 138 as holdout validation only. Batch it with C13 loops up to 137, C31 policy rows, C15/C16/C17 material/resource rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C13 AMPC/IRA/JV utilization-to-cash conversion gate and dominant-driver reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice LG에너지솔루션(373220), 삼성SDI(006400), SK이노베이션(096770), 포스코퓨처엠(003670), 에코프로비엠(247540), 나노신소재(121600), 천보(278280), 더블유씨피(393890), SK아이이테크놀로지(361610), 엔켐(348370), 솔브레인(357780), 엘앤에프(066970) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R3
completed_loop: 138
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C19_BRAND_RETAIL_INVENTORY_MARGIN
  - C27_CONTENT_IP_GLOBAL_MONETIZATION
  - C02_POWER_GRID_DATACENTER_CAPEX
```
