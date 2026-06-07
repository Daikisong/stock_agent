# E2R stock-web v12 residual research — R3 loop 98 / L3_BATTERY_EV_GREEN_MOBILITY / C13_BATTERY_JV_UTILIZATION_AMPC_IRA

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R3
selected_loop = 98
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = BATTERY_JV_AMPC_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_POLICY_CREDIT_AND_CAPACITY_LABEL_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
auto_selected_coverage_gap = C13 rows 27, 30-row minimum까지 3 부족
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

C13_BATTERY_JV_UTILIZATION_AMPC_IRA remains a thin Priority 0 archetype. It is adjacent to C11 and C12 but it is not the same machine.

- C11 asks whether an orderbook can rerate the equity.
- C12 asks whether a customer can call off the order.
- C13 asks whether a JV / AMPC / IRA / utilization bridge actually turns policy credit and capacity into cash conversion.

C13 is the toll gate between policy subsidy and earnings power. A policy headline can light the road, but the toll is only paid when the plant runs, credits are collectible, utilization rises, and margin/cash conversion survives.

This run therefore tests three C13 shapes:

1. a cell-maker rebound where AMPC/JV/utilization evidence allowed a real Stage2-to-Yellow bridge;
2. a large-cap cell-maker rally where JV/capacity language failed to defend utilization and price collapsed;
3. a separator/utilization case where a plant-ramp label generated MFE but then left a high-MAE event-cap tail.

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
| 373220 | LG에너지솔루션 | `atlas/symbol_profiles/373/373220.json` | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv` | active_like, no corporate-action caveat |
| 006400 | 삼성SDI | `atlas/symbol_profiles/006/006400.json` | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv` | active_like; selected 2024 window avoids corporate-action blocked window |
| 361610 | SK아이이테크놀로지 | `atlas/symbol_profiles/361/361610.json` | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv` | active_like, no corporate-action caveat |

This run does not use live/current candidate discovery. Future price path is used only as historical calibration label, not as evidence available at trigger date.

## 3. Novelty / duplicate check

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_detected_in_this_run = false
same_symbol_reuse_from_recent_generated_outputs = soft_reuse_possible_across_adjacent_C12/C14_but_not_same_canonical_key
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
reused_case_count = 0
```

Registry metadata already contains prior C13 files, but the visible metadata points to broad AMPC/JV/utilization, electrolyte, packaging, and cell/false-Stage2 coverage. This run compresses C13 into a narrower rule candidate: **JV/AMPC credit cannot be treated as earnings evidence unless utilization and cash conversion are visible.**

The selected row keys are:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 373220 | C13_cell_AMPC_JV_utilization_rebound | 2024-08-21 | 2024-08-21
C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 006400 | C13_cell_JV_capacity_label_without_utilization | 2024-03-25 | 2024-03-25
C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 361610 | C13_separator_utilization_event_cap_high_MAE | 2023-06-02 | 2023-06-02
```

## 4. Case table

| case | symbol | classification | trigger / entry | peak / trough used | MFE | MAE | C13 lesson |
|---|---:|---|---:|---|---:|---:|---|
| Cell AMPC/JV/utilization rebound | 373220 | positive_stage2_actionable | trigger 2024-08-21, entry 2024-08-21 @ 350,000 | peak 2024-10-08 high 444,000; trough 2024-08-21 low 332,000 | +26.86% | -5.14% | C13 can allow Stage2-Actionable when AMPC/JV language is tied to utilization recovery and the MAE stays contained. |
| Cell JV/capacity label without utilization durability | 006400 | counterexample_high_mae | trigger 2024-03-25, entry 2024-03-25 @ 486,000 | peak 2024-03-25 high 494,500; trough 2024-08-05 low 294,500 | +1.75% | -39.40% | JV/capacity rhetoric without plant utilization and margin/cash bridge should not get an automatic Stage2 bonus. |
| Separator utilization event-cap tail | 361610 | mixed_mfe_high_mae_event_cap | trigger 2023-06-02, entry 2023-06-02 @ 97,500 | peak 2023-07-26 high 120,000; trough 2023-09-27 low 73,100 | +23.08% | -25.03% | Utilization labels can produce strong MFE but still need 4B/high-MAE protection when the path rolls over before cash conversion proof. |

## 5. Trigger-level notes

### 5.1 LG에너지솔루션 — AMPC/JV/utilization rebound with contained MAE

Entry row: 2024-08-21 close 350,000. The path reached 444,000 on 2024-10-08 while the local trough stayed at 332,000 on the trigger row. The MFE/MAE pair is asymmetric in the right direction.

```text
C13 positive condition:
- AMPC / JV / IRA vocabulary is not enough by itself
- utilization recovery and shipment/margin bridge must be visible or strongly inferable
- drawdown before follow-through remains tolerable
- Stage2-Actionable / Stage3-Yellow watch can pass
- Green still requires revision and cash-conversion confirmation
```

The useful distinction is that the policy credit is not treated as free earnings. It is a receivable-like bridge that must travel through plant utilization.

### 5.2 삼성SDI — capacity/JV label without durable utilization

Entry row: 2024-03-25 close 486,000. The path gave almost no upside after entry, then printed 294,500 on 2024-08-05. The MFE was only +1.75%, while MAE was -39.40%.

```text
C13 negative condition:
- price has already chased JV/capacity/IRA language
- utilization and margin/cash conversion are not proven
- no fresh revision bridge appears before drawdown
- Stage2-Actionable bonus should be blocked
- full-window 4B/high-MAE guard should override headline optimism
```

This is the C13 trap: the plant exists, the policy credit exists, and the market can still be wrong if the utilization valve is not open.

### 5.3 SK아이이테크놀로지 — utilization event-cap with high-MAE tail

Entry row: 2023-06-02 close 97,500. The path hit 120,000 on 2023-07-26, but later fell to 73,100 by 2023-09-27. This case is not a pure false positive because MFE existed. It is a C13 event-cap case: the first leg was real enough for trading, but not durable enough for Green.

```text
C13 mixed condition:
- utilization/ramp label can generate MFE
- if cash conversion and durable customer intake are not confirmed, protect against high MAE
- Stage2-Actionable may be allowed only with a tighter 4B/high-MAE exit clock
- Green should remain locked until recurring utilization, margin, and cash conversion are visible
```

C13 should therefore distinguish “tradable bridge” from “structural rerating bridge.” The former can be Stage2/Yelow watch; the latter needs cash conversion.

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
| Stage2-Actionable bonus | Reward non-price bridge | Works for 373220, but only when utilization recovery is attached to JV/AMPC evidence. |
| price-only blowoff block | Block pure price spike | Needs C13-specific version: policy credit/JV/capacity labels can behave like price-only evidence if utilization is weak. |
| full_4b_requires_non_price_evidence | Prevent late chase | Should be strengthened for C13 when MFE appears before cash conversion proof. |
| hard_4c_thesis_break_routes_to_4c | Route thesis breaks to 4C | Should trigger when utilization/cash conversion breaks after policy-credit optimism. |
| high-MAE protection | Avoid “good story, bad path” | Needed for 006400 and 361610 because policy/JV vocabulary did not protect the path. |

## 7. Proposed shadow rule candidate

```text
new_axis_proposed = c13_jv_ampc_utilization_cash_conversion_required_for_stage2_actionable_shadow_only
axis_type = canonical_archetype_specific_guardrail
large_sector_scope = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_scope = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
production_scoring_changed = false
shadow_weight_only = true
```

Rule candidate:

```text
IF canonical_archetype_id == C13_BATTERY_JV_UTILIZATION_AMPC_IRA
AND evidence contains JV / AMPC / IRA / capacity expansion / subsidy-credit language
AND utilization_bridge == weak
AND cash_conversion_or_margin_bridge == weak
THEN block Stage2-Actionable bonus;
     keep Stage2-watch-only or 4B-watch;
     do not unlock Stage3-Green;
     route to 4C if utilization cut, customer ramp delay, subsidy collectability risk, or margin/cash break appears.

ELSE IF utilization_bridge is visible
AND AMPC/JV economics appear collectible
AND MAE remains contained before MFE follow-through
THEN allow Stage2-Actionable / Stage3-Yellow watch;
     still require revision/margin/cash evidence before Green.
```

This is not a generic battery-positive patch. It is a C13-specific credit-to-cash valve. AMPC is not earnings until it passes through utilization and collection.

## 8. Machine-readable rows

### 8.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_root":"atlas/ohlcv_tradable_by_symbol_year","symbols":["373220","006400","361610"],"validation_scope":"historical_trigger_level_calibration_only"}
```

### 8.2 case rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_POLICY_CREDIT_AND_CAPACITY_LABEL_FALSE_POSITIVE","symbol":"373220","name":"LG에너지솔루션","trigger_type":"C13_cell_AMPC_JV_utilization_rebound","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000,"peak_date":"2024-10-08","peak_price":444000,"trough_date":"2024-08-21","trough_price":332000,"mfe_pct":26.86,"mae_pct":-5.14,"classification":"positive_stage2_actionable","current_profile_error":false,"evidence_family":"cell_AMPC_JV_utilization_recovery","trigger_family":"utilization_credit_to_cash_bridge_positive","usable_for_aggregate":true,"representative":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_POLICY_CREDIT_AND_CAPACITY_LABEL_FALSE_POSITIVE","symbol":"006400","name":"삼성SDI","trigger_type":"C13_cell_JV_capacity_label_without_utilization","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":486000,"peak_date":"2024-03-25","peak_price":494500,"trough_date":"2024-08-05","trough_price":294500,"mfe_pct":1.75,"mae_pct":-39.40,"classification":"counterexample_high_mae","current_profile_error":true,"evidence_family":"cell_JV_capacity_policy_label_utilization_weak","trigger_family":"credit_capacity_label_without_cash_bridge_negative","usable_for_aggregate":true,"representative":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_JV_AMPC_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_POLICY_CREDIT_AND_CAPACITY_LABEL_FALSE_POSITIVE","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"C13_separator_utilization_event_cap_high_MAE","trigger_date":"2023-06-02","entry_date":"2023-06-02","entry_price":97500,"peak_date":"2023-07-26","peak_price":120000,"trough_date":"2023-09-27","trough_price":73100,"mfe_pct":23.08,"mae_pct":-25.03,"classification":"mixed_mfe_high_mae_event_cap","current_profile_error":true,"evidence_family":"separator_utilization_ramp_without_durable_cash_conversion","trigger_family":"utilization_event_cap_high_mae","usable_for_aggregate":true,"representative":true}
```

### 8.3 trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"373220","trigger_type":"C13_cell_AMPC_JV_utilization_rebound","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000,"mfe_pct":26.86,"mae_pct":-5.14,"stage_at_trigger":"Stage2-Actionable","stage_after_path":"Stage3-Yellow_watch","price_path_label":"positive_bridge_validated","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|C13_cell_AMPC_JV_utilization_rebound|2024-08-21|2024-08-21"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"006400","trigger_type":"C13_cell_JV_capacity_label_without_utilization","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":486000,"mfe_pct":1.75,"mae_pct":-39.40,"stage_at_trigger":"Stage2_watch_or_4B_watch","stage_after_path":"high_MAE_4C_watch","price_path_label":"counterexample_high_mae","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|C13_cell_JV_capacity_label_without_utilization|2024-03-25|2024-03-25"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"361610","trigger_type":"C13_separator_utilization_event_cap_high_MAE","trigger_date":"2023-06-02","entry_date":"2023-06-02","entry_price":97500,"mfe_pct":23.08,"mae_pct":-25.03,"stage_at_trigger":"Stage2-Actionable","stage_after_path":"4B_high_MAE_watch","price_path_label":"mixed_MFE_high_MAE_event_cap","dedupe_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|361610|C13_separator_utilization_event_cap_high_MAE|2023-06-02|2023-06-02"}
```

### 8.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"373220","raw_component_score_breakdown":{"JV_AMPC_policy_credit":18,"utilization_bridge":18,"margin_cash_conversion":15,"customer_ramp_visibility":15,"information_confidence":14,"red_team_risk":7},"total_score_proxy":87,"profile_decision":"allow_stage2_actionable_yellow_watch","calibrated_profile_stress_result":"positive_allowed_if_utilization_and_credit_collectability_are_visible"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"006400","raw_component_score_breakdown":{"JV_AMPC_policy_credit":17,"utilization_bridge":5,"margin_cash_conversion":4,"customer_ramp_visibility":7,"information_confidence":10,"red_team_risk":19},"total_score_proxy":62,"profile_decision":"block_stage2_actionable_or_route_4B_high_MAE_watch","calibrated_profile_stress_result":"current_profile_error_if_capacity_JV_label_gets_bonus"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"361610","raw_component_score_breakdown":{"JV_AMPC_policy_credit":8,"utilization_bridge":15,"margin_cash_conversion":6,"customer_ramp_visibility":13,"information_confidence":12,"red_team_risk":16},"total_score_proxy":70,"profile_decision":"allow_stage2_watch_but_activate_4B_high_MAE_exit_clock","calibrated_profile_stress_result":"MFE_exists_but_Green_locked_without_cash_conversion"}
```

### 8.5 aggregate metric

```jsonl
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","case_count":3,"trigger_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"median_mfe_pct":23.08,"median_mae_pct":-25.03,"mean_mfe_pct":17.23,"mean_mae_pct":-23.19,"recommended_shadow_axis":"c13_jv_ampc_utilization_cash_conversion_required_for_stage2_actionable_shadow_only","do_not_propose_new_weight_delta":false}
```

### 8.6 shadow weight / residual contribution

```jsonl
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"c13_jv_ampc_utilization_cash_conversion_required_for_stage2_actionable_shadow_only","weight_delta_proposal":{"utilization_bridge":"+","margin_cash_conversion":"+","JV_AMPC_policy_credit":"conditional_not_standalone","red_team_risk":"+ when utilization weak"},"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c13_jv_ampc_utilization_cash_conversion_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C13 JV/AMPC/capacity-label rallies","existing_axis_weakened":null,"do_not_propose_new_weight_delta":false,"reason":"C13 needs a credit-to-cash valve: JV/AMPC/capacity evidence is insufficient without utilization and margin/cash conversion."}
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
diversity_score_summary = C13 Priority 0 부족권 + cell AMPC/JV positive + cell capacity false positive + separator utilization event-cap high-MAE tail
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c13_jv_ampc_utilization_cash_conversion_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C13 JV/AMPC/capacity-label rallies
existing_axis_weakened = null
next_recommended_archetypes = C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation agent for Songdaiki/stock_agent.

Do not treat this Markdown as production code. Ingest it as a v12 sector-archetype residual research artifact.

Target file:
docs/round/e2r_stock_web_v12_residual_round_R3_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md

Task:
1. Parse all machine-readable JSONL rows.
2. Validate that price_source_validation uses Songdaiki/stock-web tradable_raw shards.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add case/trigger rows only if representative and usable_for_aggregate.
5. Treat the proposed axis as shadow-only:
   c13_jv_ampc_utilization_cash_conversion_required_for_stage2_actionable_shadow_only
6. Do not globally raise or lower battery weights.
7. If this axis is promoted later, scope it only to:
   large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
   canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
8. Preserve guardrails:
   production_scoring_changed = false for this research file.
   hard_4c_thesis_break_routes_to_4c remains enabled.
   full_4b_requires_non_price_evidence remains enabled.
```
