# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R3
selected_loop: 139
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CUSTOMER_CONTRACT_TO_CALL_OFF_UTILIZATION_MARGIN_HOLDOUT_V139_CELL_SEPARATOR_FOIL_MATERIAL_PROXY_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 373220/2024: reused_from_prior_local_C12_loop_138_customer_diversification_positive_row
    - 361610/2024: reused_from_prior_local_C12_loop_138_separator_customer_pull_hard_4C
    - 011790/2024: reused_from_prior_local_C12_C13_C15_C16_battery_material_4B
    - 006110/2024: reused_from_prior_local_C12_C13_C15_C16_foil_4B
    - 018470/2024: reused_from_prior_local_C12_C13_C15_C16_hard_4C
    - 006400/2024: not_recomputed_this_turn_future_cell_OEM_calloff_candidate
    - 096770/2024: not_recomputed_this_turn_future_cell_calloff_AMPC_boundary
    - 003670/2024: not_recomputed_this_turn_future_material_customer_calloff_candidate
    - 247540/2024: not_recomputed_this_turn_future_cathode_calloff_candidate
    - 121600/2024: not_recomputed_this_turn_future_material_customer_calloff_candidate
    - 278280/2024: not_recomputed_this_turn_future_electrolyte_customer_calloff_candidate
    - 393890/2024: not_recomputed_this_turn_future_separator_customer_contract_candidate
    - 348370/2024: not_recomputed_this_turn_future_electrolyte_supply_contract_candidate
    - 357780/2024: not_recomputed_this_turn_future_material_supplier_contract_candidate
    - 066970/2024: not_recomputed_this_turn_future_cathode_calloff_candidate
    - 299030/2024: not_recomputed_this_turn_future_battery_component_candidate
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - customer_contract_to_call_off_gate
  - demand_risk_vs_AMPC_policy_split
  - separator_customer_pull_hard_4C_guard
  - material_event_reclassification_guard
  - foil_capacity_proxy_high_MAE_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` remains a Priority 0 archetype. The current no-repeat index marks C12 as below the 30-row minimum, and the v12 scheduler maps C11~C14 to `R3 / L3_BATTERY_EV_GREEN_MOBILITY`.

This file continues the local R3/C12 battery sequence after `R3/C12 loop 138` and the latest `R3/C13 loop 138`; selected loop is therefore `139` for this C12 holdout.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct fresh C12 customer-contract/call-off candidate shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C13/C31/C15/C16 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC, then reinterpret them through the C12 customer-call-off lens. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

```yaml
loop_139_note:
  independence_status: duplicate_holdout_only
  fresh_reprice_status: not_recomputed_this_execution
  reason: C12 remains under-covered, but this run reuses prior C12/C13/C15/C16 boundary rows and must not create a new weight delta.
```


C12 should not reward a signed battery customer name unless that customer actually calls off volume.

C12 is the battery demand-conversion archetype:

```text
customer contract / offtake / supply agreement / named OEM / battery material customer
→ call-off schedule
→ utilization
→ shipment cadence
→ ASP / margin
→ working capital and inventory quality
→ cash conversion
→ price path validation
```

The recurrent false positive is:

```text
customer name
long-term contract vocabulary
capacity expansion
battery policy / AMPC / IRA label
separator localization
foil or material proxy
commodity material beta
```

A contract is like a restaurant reservation. The revenue arrives only when the customer sits down, orders, pays, and comes back. C12 therefore needs call-off, utilization, and margin evidence, not just customer or policy vocabulary.

The C12 route split:

```text
customer call-off + utilization + margin bridge
→ keep Stage2

AMPC/IRA support without call-off proof
→ cap C12 and route policy/cash question to C13/C31

separator/customer localization label without utilization
→ hard 4C

battery material event with unclear dominant driver
→ local 4B / reclassification watch

foil capacity proxy with high MFE and high MAE
→ local 4B until customer call-off and margin refresh

battery proxy / commodity material beta with low MFE and deep MAE
→ hard 4C
```

The key distinction versus C13:

```text
C13 asks: does AMPC/JV/utilization policy reach cash?
C12 asks: did the customer actually call off volume and protect margin?
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 5
  actual_trigger_rows: 5
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
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
    - C12 holdout validation
    - customer-contract-to-call-off bridge gate
    - demand-risk versus AMPC/IRA split
    - material proxy false-positive guard
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
  - R3/C12 loops 137~138
  - R3/C13 loops 136~138
  - R11/C31 loops 103~108
  - R4/C15 loops 105~108
  - R4/C16 loops 112~115
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct fresh C12 customer-contract candidate shards were unavailable or cache-missed in this execution
  - exact duplicate C12 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R3","selected_loop":139,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_DIVERSIFICATION_AND_UTILIZATION_BRIDGE_POSITIVE_BUT_CALL_OFF_REFRESH_REQUIRED","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_price":332500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.50,"MAE_30D_pct":-6.47,"MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"MFE_180D_pct":33.53,"MAE_180D_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C12|373220|Stage2-Actionable|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same LGES positive battery-policy/utilization row from C13/C31 guardrails, reinterpreted for C12 call-off risk","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"customer_diversification_utilization_positive_control","novelty_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|373220|Stage2-Actionable|2024-07-25","non_price_bridge":"customer diversification, utilization, ESS/non-EV demand and AMPC support point toward call-off durability but require shipment cadence proof","score_alignment":"keep Stage2; block Green until customer call-off, shipment cadence, margin and working-capital bridge refresh"}
{"row_type":"trigger","selected_round":"R3","selected_loop":139,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SEPARATOR_CUSTOMER_PULL_ABSENT_LOCALIZATION_LABEL_HARD_4C","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C12|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same separator policy false-positive row from C13/C31 guardrails, reinterpreted as C12 customer-pull failure","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"separator_customer_pull_hard_counterexample","novelty_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|361610|Stage4C|2024-05-16","non_price_bridge":"separator/localization exposure without customer pull, utilization, parent financing, shipment cadence or cash-conversion bridge","score_alignment":"hard 4C; customer/localization label cannot substitute for call-off and utilization"}
{"row_type":"trigger","selected_round":"R3","selected_loop":139,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_MATERIAL_EVENT_WITHOUT_CUSTOMER_CALLOFF_DOMINANT_DRIVER_RECLASSIFICATION_4B","symbol":"011790","name":"SKC","trigger_type":"Stage4B","entry_date":"2024-05-23","entry_price":117000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":70.94,"MAE_30D_pct":0.00,"MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"MFE_180D_pct":70.94,"MAE_180D_pct":-20.17,"forward_high_30d":200000,"forward_low_30d":117000,"forward_high_90d":200000,"forward_low_90d":107600,"forward_high_180d":200000,"forward_low_180d":93400,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C12|011790|Stage4B|2024-05-23","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_event_contamination_4B","reuse_reason":"same SKC battery/material event row from C13/C16/C17 guardrails, reinterpreted as C12 call-off split","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"battery_material_event_local_4B","novelty_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|011790|Stage4B|2024-05-23","non_price_bridge":"battery/material event-driven MFE rather than confirmed customer call-off, shipment cadence, utilization or margin bridge","score_alignment":"local 4B; cap C12 contribution unless customer call-off and margin economics are refreshed"}
{"row_type":"trigger","selected_round":"R3","selected_loop":139,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_FOIL_CAPACITY_PROXY_HIGH_MFE_HIGH_MAE_LOCAL_4B","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage4B","entry_date":"2024-05-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.34,"MAE_30D_pct":-7.28,"MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"MFE_180D_pct":28.34,"MAE_180D_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C12|006110|Stage4B|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_foil_4B","reuse_reason":"same aluminium battery-foil high-MAE row from C13/C15/C16 guardrails, reinterpreted as C12 capacity proxy split","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"foil_capacity_proxy_local_4B","novelty_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|006110|Stage4B|2024-05-20","non_price_bridge":"aluminium battery-foil capacity/material label without refreshed customer order, call-off schedule, utilization, ASP/margin or working-capital bridge","score_alignment":"local 4B only; block Green until customer call-off, utilization and margin bridge refresh"}
{"row_type":"trigger","selected_round":"R3","selected_loop":139,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ALUMINIUM_ROLLING_BATTERY_PROXY_LOW_MFE_DEEP_MAE_HARD_4C","symbol":"018470","name":"조일알미늄","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":2470,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.29,"MAE_30D_pct":-17.41,"MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"MFE_180D_pct":7.29,"MAE_180D_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C12|018470|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same aluminium rolling hard counterexample from C13/C15/C16 guardrails, reinterpreted as C12 battery-proxy false-positive control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"battery_proxy_hard_4C","novelty_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|018470|Stage4C|2024-05-20","non_price_bridge":"aluminium rolling commodity beta / battery proxy label without customer call-off, utilization, shipment cadence, margin or cash bridge","score_alignment":"hard 4C; low MFE and high MAE reject customer-contract/call-off bridge"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R3","selected_loop":139,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_NEW_CUSTOMER_CONTRACT_CALLOFF_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["006400","096770","003670","247540","121600","278280","357780","348370"],"candidate_names":["삼성SDI","SK이노베이션","포스코퓨처엠","에코프로비엠","나노신소재","천보","솔브레인","엔켐"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C12 evidence; distinguish true customer call-off from AMPC/JV C13, material spread C15, resource supply C16, and chemical spread C17"}
```

---

## 6. Case analysis

### 6.1 LG Energy Solution / 373220 — customer diversification positive-control, call-off refresh required

```yaml
entry_price: 332500
90D_MFE_MAE: +33.53 / -6.47
180D_MFE_MAE: +33.53 / -6.47
route: Stage2-Actionable
```

This row can survive C12 only if the evidence is framed as customer diversification and demand durability rather than just AMPC policy. The price path is favorable, but C12 still needs shipment cadence, call-off schedule, margin and working-capital confirmation before Green.

### 6.2 SK IE Technology / 361610 — separator localization hard 4C

```yaml
entry_price: 57600
90D_MFE_MAE: +1.04 / -46.27
180D_MFE_MAE: +1.04 / -60.68
route: Stage4C
```

This is the hard counterexample. A separator/localization label is not a customer call-off. Without customer pull and utilization, the label collapses.

### 6.3 SKC / 011790 — battery material event contamination 4B

```yaml
entry_price: 117000
90D_MFE_MAE: +70.94 / -8.03
180D_MFE_MAE: +70.94 / -20.17
route: Stage4B / reclassification watch
```

The price move is real, but C12 must ask whether the MFE came from customer call-off or from a battery-material event. Without call-off evidence, this is not a clean C12 positive.

### 6.4 Sam-A Aluminium / 006110 — foil capacity proxy 4B

```yaml
entry_price: 75500
90D_MFE_MAE: +28.34 / -47.55
180D_MFE_MAE: +28.34 / -53.58
route: Stage4B
```

The row shows why high MFE must not be promoted mechanically. Capacity and foil proxy evidence needs the customer to actually pull product.

### 6.5 Choil Aluminium / 018470 — battery proxy hard 4C

```yaml
entry_price: 2470
90D_MFE_MAE: +7.29 / -41.30
180D_MFE_MAE: +7.29 / -44.70
route: Stage4C
```

This row blocks commodity/battery-proxy vocabulary. C12 needs direct call-off and utilization evidence.

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
diversity_score_summary: "customer diversification positive, separator hard 4C, battery-material event 4B/reclassification, foil high-MFE 4B, aluminium battery-proxy hard 4C covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C12 lesson |
|---|---:|---:|---:|---|
| 373220 | customer diversification positive | +33.53 / -6.47 | +33.53 / -6.47 | demand bridge can survive, call-off refresh needed |
| 361610 | separator hard 4C | +1.04 / -46.27 | +1.04 / -60.68 | localization label fails |
| 011790 | material event 4B | +70.94 / -8.03 | +70.94 / -20.17 | dominant-driver reclassification needed |
| 006110 | foil 4B | +28.34 / -47.55 | +28.34 / -53.58 | customer/utilization refresh needed |
| 018470 | proxy hard 4C | +7.29 / -41.30 | +7.29 / -44.70 | battery-proxy label fails |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable_GreenBlocked","changed_components":["margin_bridge_score","policy_or_regulatory_score"],"component_delta_explanation":"Customer diversification and demand bridge can support Stage2, but C12 requires call-off and shipment cadence proof before Green.","MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"score_return_alignment_label":"customer_diversification_positive_calloff_refresh_required","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":61,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":36,"stage_label_after":"Stage4C","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","relative_strength_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"Separator/localization label lacked customer pull, shipment cadence and utilization; price path confirms hard 4C.","MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"score_return_alignment_label":"separator_customer_pull_absent_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":57,"stage_label_after":"Stage4B_dominant_driver_reclassification","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"High MFE was dominated by battery/material event mechanics rather than C12 customer call-off and shipment cadence.","MFE_90D_pct":70.94,"MAE_90D_pct":-8.03,"score_return_alignment_label":"battery_material_event_reclassification_4B","current_profile_verdict":"cap_or_reclassify"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"006110","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":71,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":56,"stage_label_after":"Stage4B_foil_calloff_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Foil/capacity proxy had high MFE but customer call-off, shipment cadence and margin bridge were unrefreshed; severe MAE blocks Green.","MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"score_return_alignment_label":"foil_capacity_high_MAE_local_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"018470","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Aluminium rolling battery-proxy label lacked customer call-off, utilization, shipment cadence, margin and cash bridge.","MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"score_return_alignment_label":"battery_proxy_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

---

## 9. Current calibrated profile stress test

The C12 customer-contract-to-call-off gate held:

```text
customer diversification + utilization bridge
→ Stage2 can survive, but Green blocked until call-off cadence

separator/localization label without customer pull
→ hard 4C

battery-material event without customer call-off
→ local 4B / reclassify

foil capacity proxy with high MFE and severe MAE
→ local 4B, no Green

battery proxy / commodity material beta with low MFE and deep MAE
→ hard 4C
```

### Rule candidate retained, not newly proposed

```text
C12_CUSTOMER_CONTRACT_TO_CALLOFF_UTILIZATION_MARGIN_GATE_V139_HELD_OUT

if C12
and customer_contract_offtake_supply_agreement_or_battery_customer_label == true
and calloff_schedule_shipment_cadence_utilization_margin_or_working_capital_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C12
and customer_diversification_utilization_or_calloff_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_calloff_margin_working_capital_refresh = true
```

```text
if C12
and localization_separator_or_material_customer_label == true
and utilization_customer_pull_or_shipment_bridge == false
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C12
and battery_material_or_capacity_proxy == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -20
and customer_calloff_margin_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C12
and dominant_driver_belongs_to_C13_C15_C16_or_C17 == true:
    cap_C12_contribution = true
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
    false_positive_risk: high_if_customer_label_or_material_proxy_rows_are_left_actionable
    verdict: adequate_only_with_C12_calloff_margin_bridge_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for battery customer/material/proxy labels
    eligible_trigger_count: 5
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L3 battery rows require customer call-off and utilization bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C12 requires call-off schedule and shipment cadence, not customer label
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: localization/material proxy rows without call-off route hard 4C or 4B cap
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | CUSTOMER_CONTRACT_TO_CALLOFF_HOLDOUT_V139 | 1 | 4 | 2 | 2 | 0 | 5 | 5 | 0 | 4 | false | false | 14 |

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
  - C12|373220|Stage2-Actionable|2024-07-25
  - C12|361610|Stage4C|2024-05-16
  - C12|011790|Stage4B|2024-05-23
  - C12|006110|Stage4B|2024-05-20
  - C12|018470|Stage4C|2024-05-20
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C12_customer_contract_to_calloff_gate
  - dominant_driver_reclassification_guard
residual_error_types_found:
  - customer_label_without_calloff
  - separator_localization_without_customer_pull
  - battery_material_event_wrong_bridge
  - foil_capacity_proxy_high_MAE
  - battery_proxy_commodity_false_positive
new_axis_proposed: null
existing_axis_strengthened:
  - C12_CUSTOMER_CONTRACT_TO_CALLOFF_UTILIZATION_MARGIN_GATE_V139_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C12 customer-contract/call-off candidate shards were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"139","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":0,"reused_case_count":5,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C12_customer_contract_to_calloff_gate","dominant_driver_reclassification_guard"],"residual_error_types_found":["customer_label_without_calloff","separator_localization_without_customer_pull","battery_material_event_wrong_bridge","foil_capacity_proxy_high_MAE","battery_proxy_commodity_false_positive"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R3/C12 loop 139 as holdout validation only. Batch it with C12 loops 137~138, existing C12 rows, C13 AMPC/JV rows, C15/C16/C17 material/resource rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C12 customer-contract-to-call-off/utilization/margin gate and dominant-driver reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should directly reprice 삼성SDI(006400), SK이노베이션(096770), 포스코퓨처엠(003670), 에코프로비엠(247540), 나노신소재(121600), 천보(278280), 솔브레인(357780), 엔켐(348370), 더블유씨피(393890), SK아이이테크놀로지(361610), 엘앤에프(066970), 금양(001570), 탑머티리얼(360070) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R3
completed_loop: 139
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C19_BRAND_RETAIL_INVENTORY_MARGIN
  - C27_CONTENT_IP_GLOBAL_MONETIZATION
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
