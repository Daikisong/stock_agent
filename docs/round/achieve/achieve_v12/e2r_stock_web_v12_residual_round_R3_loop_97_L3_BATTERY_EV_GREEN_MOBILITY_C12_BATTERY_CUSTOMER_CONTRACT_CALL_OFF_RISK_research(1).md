# E2R stock-web v12 residual research — R3 loop 97 / L3_BATTERY_EV_GREEN_MOBILITY / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R3
selected_loop = 97
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_SHIPMENT_BRIDGE_VS_CONTRACT_LABEL_SPIKE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
auto_selected_coverage_gap = C12 rows 27, 30-row minimum까지 3 부족
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection memo

C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK remains a Priority 0 thin archetype in the No-Repeat Index. The gap is small but important: C12 is where battery orderbook language has to pass through a narrower gate than C11. The bridge is not “contract exists.” The bridge is customer call-off discipline, shipment conversion, utilization, margin, and cash conversion.

This run therefore compresses C12 into a sharper residual question:

> When the market sees battery customer/contract/capacity language, does the evidence prove committed shipment conversion, or is it only a label that can be cut, deferred, or called off?

C12 is a valve, not a pump. C11 can reward an orderbook when the pipe is filling; C12 asks whether the customer can still close the valve before the revenue reaches the income statement.

## 2. Price source validation

Stock-web manifest basis used for this run:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis = tradable_raw
```

Validated symbol profiles and yearly shards:

| symbol | name | profile path | OHLC shard(s) used | calibration caveat |
|---:|---|---|---|---|
| 361610 | SK아이이테크놀로지 | `atlas/symbol_profiles/361/361610.json` | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv` | active_like, no corporate-action caveat |
| 066970 | 엘앤에프 | `atlas/symbol_profiles/066/066970.json` | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv` | active_like, KOSDAQ GLOBAL → KOSPI later; no corporate-action caveat in selected 2023 window |
| 278280 | 천보 | `atlas/symbol_profiles/278/278280.json` | `atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv` | active_like, no corporate-action caveat |

This run does not use live/current candidate discovery. Future price path is used only as historical calibration label, not as evidence available at trigger date.

## 3. Novelty / duplicate check

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_detected_in_this_run = false
same_symbol_reuse_from_recent_generated_outputs = false
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
reused_case_count = 0
```

Inspected registry metadata already contains C12 files, but the visible metadata points to prior battery-can, equipment, precursor, supercapacitor, and generic material call-off coverage. This run uses a different compression: separator ramp validation, cathode customer/demand call-off break, and electrolyte shipment/utilization break. The row-level key is new in this session and not a loop-only rematerialization.

## 4. Case table

| case | symbol | classification | trigger / entry | peak / trough used | MFE | MAE | C12 lesson |
|---|---:|---|---:|---|---:|---:|---|
| Separator ramp with call-off risk screened out | 361610 | positive_stage2_actionable | trigger 2023-04-03, entry 2023-04-03 @ 75,900 | peak 2023-06-12 high 103,900; trough 2023-04-03 low 72,300 | +36.89% | -4.74% | When customer ramp/utilization evidence is visible, C12 should not over-block a real Stage2 → Yellow bridge. |
| Cathode contract/capacity label without shipment conversion | 066970 | counterexample_high_mae_calloff | trigger 2023-04-19, entry 2023-04-19 @ 337,000 | peak 2023-04-19 high 346,000; trough 2023-11-01 low 127,900 | +2.67% | -62.05% | Contract/customer language without call-off and shipment conversion protection is a classic C12 trap. |
| Electrolyte demand deferral / utilization break | 278280 | counterexample_fast_4c | trigger 2023-04-11, entry 2023-04-11 @ 281,500 | peak 2023-04-11 high 292,000; trough 2023-04-26 low 180,100 | +3.73% | -36.02% | Electrolyte/material contract language decays fast when customer orders can be deferred and utilization is not defended. |

## 5. Trigger-level notes

### 5.1 SK아이이테크놀로지 — positive C12 bridge

Entry row: 2023-04-03 close 75,900. The local path reached 103,900 on 2023-06-12, while the initial trough was 72,300 on the trigger row. This gives a useful positive C12 case: the market was not merely rewarding a battery vocabulary word. It had a separator/ramp path that behaved like an actual customer conversion bridge.

```text
C12 positive condition:
- customer/channel evidence implies shipment conversion, not just contract vocabulary
- utilization/ramp bridge is visible before price runs too far
- MAE is tolerable before MFE appears
- Stage2-Actionable can be allowed, but Stage3-Green still waits for margin/revision confirmation
```

The profile should not treat C12 only as a bear filter. C12 should be a gate: when the valve is demonstrably open, Stage2-Actionable can pass.

### 5.2 엘앤에프 — customer/capacity label became call-off risk

Entry row: 2023-04-19 close 337,000. The same local area printed only a small high of 346,000, then the full-window path collapsed to 127,900 by 2023-11-01. The MFE/MAE shape is asymmetric in the wrong direction.

```text
C12 negative condition:
- contract/customer/capacity words exist
- shipment conversion is not proven
- customer call-off or demand deferral can still dominate
- price has almost no follow-through after entry
- should be Stage2-watch-only / 4B risk / hard 4C once margin-utilization break appears
```

The residual error is subtle. A broad battery orderbook model may still see high conviction; C12 must ask whether the customer can avoid taking volume. If yes, the orderbook is only a promise-shaped shadow.

### 5.3 천보 — electrolyte call-off/utilization break

Entry row: 2023-04-11 close 281,500. The path briefly marked 292,000, then fell to 180,100 within the same April window. That is not a slow valuation reset; it is a hard check on contract-quality assumptions.

```text
C12 hard-break condition:
- material/electrolyte demand depends on customer utilization
- customer order deferral is not separated from signed-capacity rhetoric
- price breaks before a new margin or shipment bridge appears
- fast 4C or hard watch should activate earlier than generic Stage2
```

This case supports treating C12 call-off risk as a thesis-break route when a customer volume assumption fails before sales/margin evidence arrives.

## 6. Current calibrated profile stress test

Current calibrated profile proxy:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Stress result:

| rule axis | expected behavior | residual found |
|---|---|---|
| Stage2-Actionable bonus | Reward non-price bridge | Works for 361610 only if call-off risk is screened out by ramp/utilization evidence. |
| price-only blowoff block | Block pure price spike | Needs C12-specific vocabulary: contract/capacity labels should not count unless shipment conversion is visible. |
| full_4b_requires_non_price_evidence | Prevent late chase | Should be scoped to customer call-off: if only contract label exists after a price run, force 4B watch. |
| hard_4c_thesis_break_routes_to_4c | Route thesis breaks to 4C | Should trigger earlier when utilization/shipment/customer intake breaks before margin evidence. |

## 7. Proposed shadow rule candidate

```text
new_axis_proposed = c12_customer_calloff_shipment_conversion_required_for_stage2_actionable_shadow_only
axis_type = canonical_archetype_specific_guardrail
large_sector_scope = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_scope = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
production_scoring_changed = false
shadow_weight_only = true
```

Rule candidate:

```text
IF canonical_archetype_id == C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
AND evidence contains customer_contract / capacity / orderbook / supply_agreement language
AND shipment_conversion_evidence == weak
AND utilization_or_margin_bridge == weak
THEN block Stage2-Actionable bonus;
     keep Stage2-watch-only or 4B-watch;
     route to hard 4C if explicit customer deferral/call-off/utilization cut appears.

ELSE IF customer ramp + utilization + shipment conversion are visible
AND MAE path remains tolerable before MFE follow-through
THEN allow Stage2-Actionable / Stage3-Yellow watch,
     but do not unlock Green without revision/margin confirmation.
```

This is not a global battery rule. It is a C12-specific valve rule. C11 asks whether the orderbook pipe exists; C12 asks whether the customer can still close the valve.

## 8. Machine-readable rows

### 8.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_root":"atlas/ohlcv_tradable_by_symbol_year","symbols":["361610","066970","278280"],"validation_scope":"historical_trigger_level_calibration_only"}
```

### 8.2 case rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_SHIPMENT_BRIDGE_VS_CONTRACT_LABEL_SPIKE","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"C12_separator_customer_ramp_calloff_screened_out","trigger_date":"2023-04-03","entry_date":"2023-04-03","entry_price":75900,"peak_date":"2023-06-12","peak_price":103900,"trough_date":"2023-04-03","trough_price":72300,"mfe_pct":36.89,"mae_pct":-4.74,"classification":"positive_stage2_actionable","current_profile_error":false,"evidence_family":"separator_ramp_utilization_customer_conversion","trigger_family":"shipment_conversion_bridge_positive","usable_for_aggregate":true,"representative":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_SHIPMENT_BRIDGE_VS_CONTRACT_LABEL_SPIKE","symbol":"066970","name":"엘앤에프","trigger_type":"C12_cathode_customer_contract_label_without_shipment_conversion","trigger_date":"2023-04-19","entry_date":"2023-04-19","entry_price":337000,"peak_date":"2023-04-19","peak_price":346000,"trough_date":"2023-11-01","trough_price":127900,"mfe_pct":2.67,"mae_pct":-62.05,"classification":"counterexample_high_mae_calloff","current_profile_error":true,"evidence_family":"cathode_customer_capacity_label_calloff_risk","trigger_family":"shipment_conversion_missing_negative","usable_for_aggregate":true,"representative":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_SHIPMENT_BRIDGE_VS_CONTRACT_LABEL_SPIKE","symbol":"278280","name":"천보","trigger_type":"C12_electrolyte_customer_utilization_deferral_break","trigger_date":"2023-04-11","entry_date":"2023-04-11","entry_price":281500,"peak_date":"2023-04-11","peak_price":292000,"trough_date":"2023-04-26","trough_price":180100,"mfe_pct":3.73,"mae_pct":-36.02,"classification":"counterexample_fast_4c","current_profile_error":true,"evidence_family":"electrolyte_customer_order_deferral_utilization_break","trigger_family":"fast_calloff_thesis_break_negative","usable_for_aggregate":true,"representative":true}
```

### 8.3 trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"361610","trigger_type":"C12_separator_customer_ramp_calloff_screened_out","trigger_date":"2023-04-03","entry_date":"2023-04-03","entry_price":75900,"mfe_pct":36.89,"mae_pct":-4.74,"stage_at_trigger":"Stage2-Actionable","stage_after_path":"Stage3-Yellow_watch","price_path_label":"positive_bridge_validated","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|361610|C12_separator_customer_ramp_calloff_screened_out|2023-04-03|2023-04-03"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"066970","trigger_type":"C12_cathode_customer_contract_label_without_shipment_conversion","trigger_date":"2023-04-19","entry_date":"2023-04-19","entry_price":337000,"mfe_pct":2.67,"mae_pct":-62.05,"stage_at_trigger":"Stage2_watch_or_4B_watch","stage_after_path":"hard_4C_customer_calloff_break","price_path_label":"counterexample_high_mae","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|066970|C12_cathode_customer_contract_label_without_shipment_conversion|2023-04-19|2023-04-19"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"278280","trigger_type":"C12_electrolyte_customer_utilization_deferral_break","trigger_date":"2023-04-11","entry_date":"2023-04-11","entry_price":281500,"mfe_pct":3.73,"mae_pct":-36.02,"stage_at_trigger":"Stage2_watch","stage_after_path":"fast_4C_customer_utilization_break","price_path_label":"counterexample_fast_break","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|278280|C12_electrolyte_customer_utilization_deferral_break|2023-04-11|2023-04-11"}
```

### 8.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"361610","raw_component_score_breakdown":{"customer_contract_quality":18,"shipment_conversion":18,"utilization_bridge":17,"margin_cash_bridge":11,"information_confidence":14,"red_team_risk":8},"total_score_proxy":86,"profile_decision":"allow_stage2_actionable_yellow_watch","calibrated_profile_stress_result":"positive_allowed_if_calloff_screened_out"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"066970","raw_component_score_breakdown":{"customer_contract_quality":16,"shipment_conversion":5,"utilization_bridge":4,"margin_cash_bridge":3,"information_confidence":10,"red_team_risk":18},"total_score_proxy":56,"profile_decision":"block_stage2_actionable_or_route_4B_4C","calibrated_profile_stress_result":"current_profile_error_if_contract_label_gets_bonus"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"278280","raw_component_score_breakdown":{"customer_contract_quality":12,"shipment_conversion":4,"utilization_bridge":3,"margin_cash_bridge":3,"information_confidence":12,"red_team_risk":20},"total_score_proxy":54,"profile_decision":"hard_watch_fast_4C_if_deferral_visible","calibrated_profile_stress_result":"needs_customer_calloff_thesis_break_route"}
```

### 8.5 aggregate metric

```jsonl
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_count":3,"trigger_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"median_mfe_pct":3.73,"median_mae_pct":-36.02,"mean_mfe_pct":14.43,"mean_mae_pct":-34.27,"recommended_shadow_axis":"c12_customer_calloff_shipment_conversion_required_for_stage2_actionable_shadow_only","do_not_propose_new_weight_delta":false}
```

### 8.6 shadow weight / residual contribution

```jsonl
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"c12_customer_calloff_shipment_conversion_required_for_stage2_actionable_shadow_only","suggested_direction":"increase_guardrail_weight","production_scoring_changed":false,"rationale":"Two of three cases show that contract/customer labels without shipment conversion create high-MAE failures; one positive case shows the gate should allow Stage2 only when call-off risk is screened out."}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c12_customer_calloff_shipment_conversion_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C12 contract/capacity label spikes","existing_axis_weakened":null,"next_recommended_archetypes":["C13_BATTERY_JV_UTILIZATION_AMPC_IRA","C24_BIO_TRIAL_DATA_EVENT_RISK","C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"]}
```

## 9. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
diversity_score_summary = C12 Priority 0 부족권 + separator ramp positive와 cathode/electrolyte call-off failure counterexamples 균형
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C12 rows 27, 30-row minimum까지 3 부족
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c12_customer_calloff_shipment_conversion_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C12 contract/capacity label spikes
existing_axis_weakened = null
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent in a later batch implementation session.

Do not treat this Markdown as production code. Ingest it as one v12 sector-archetype residual research file.

Task:
1. Parse machine-readable JSONL rows from this MD.
2. Validate that large_sector_id == L3_BATTERY_EV_GREEN_MOBILITY and canonical_archetype_id == C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.
3. Confirm price_source_validation rows against Songdaiki/stock-web tradable_raw shards.
4. Add cases/triggers only if their dedupe keys are not already present.
5. Evaluate the shadow axis:
   c12_customer_calloff_shipment_conversion_required_for_stage2_actionable_shadow_only
6. Do not loosen Stage3-Green thresholds.
7. Consider only a guardrail/profile-scope patch if multiple independent C12 rows support the same direction.
8. Keep production_scoring_changed = false unless a separate batch promotion plan approves it.

Implementation intent:
- For C12, contract/customer/orderbook/capacity labels should not receive Stage2-Actionable bonus unless shipment conversion, utilization, or margin/cash bridge is visible.
- If explicit customer deferral, call-off, utilization cut, or shipment failure appears, route to 4B/4C watch earlier.
- If customer ramp and shipment conversion are visible, allow Stage2-Actionable / Yellow watch but still require revision/margin for Green.
```
