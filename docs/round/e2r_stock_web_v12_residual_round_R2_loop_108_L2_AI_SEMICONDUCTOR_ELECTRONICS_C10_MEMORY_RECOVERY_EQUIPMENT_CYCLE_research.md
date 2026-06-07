# E2R v12 Residual Research — R2 / Loop 108 / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R2
selected_loop: 108
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_EQUIPMENT_ORDER_REVISION_BRIDGE_VS_MEMORY_BETA_AND_CONSUMABLE_LABEL_FADE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
stock_web_price_atlas_access_required: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
output_format: one_standalone_markdown_file
```

## 0. Execution boundary

This is not a live candidate scan, trading recommendation, or `stock_agent` code change.  It is a standalone historical calibration / residual research Markdown file for later batch ingestion by a coding agent.

Permitted work in this run:

- read `Songdaiki/stock-web` price atlas rows;
- confirm historical trigger date and price rows;
- calculate entry / MFE / MAE / peak / drawdown from actual 1D OHLC rows;
- add positive and counterexample rows for C10;
- propose only shadow-rule candidates;
- embed a deferred handoff prompt, but do not execute it.

Not performed:

- no current stock recommendation;
- no live watchlist;
- no brokerage/API work;
- no `stock_agent` source-code inspection;
- no production scoring patch.

## 1. Why this archetype was selected

No-Repeat Index Priority 0 still has thin canonical buckets below the 30-row stability zone.  After the immediately prior Priority 0 fills for C08, C09, C01, C07, and C06, the next thin bucket is:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rows = 21
need_to_30 = 9
need_to_50 = 29
research_focus = memory recovery beta versus real equipment order conversion
```

Therefore this run intentionally selects C10 rather than repeating the prior C06 HBM memory supplier / capacity bucket.

## 2. Price atlas source

```yaml
price_source_repo: Songdaiki/stock-web
price_basis: tradable_raw
atlas_version: 1.0.0
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
zero_volume_rows_excluded_from_calibration: true
corporate_action_contaminated_windows_blocked_by_default: true
```

## 3. Trigger spine

### 3.1 External event spine

The event spine is the 2024 memory recovery turn rather than a single company-specific order disclosure.

- 2024-04-05 Reuters Breakingviews / Samsung context: Samsung estimated a sharp profit rebound for Q1 2024, with stabilizing memory demand and DRAM ASP improvement acting as evidence that the prior memory trough was ending.
- 2024-04-25 Reuters / SK Hynix context: SK Hynix said the memory market was entering a full recovery cycle on AI demand, with strength in HBM and enterprise SSD/NAND demand.

For C10 this spine is only the *macro door opening*.  It is not sufficient for Stage3 by itself.  The calibration question is whether listed equipment/material names convert that memory cycle into actual order, backlog, revenue, margin, or revision evidence.

### 3.2 Entry convention

Entry date is set to **2024-04-25**, the SK Hynix full-recovery public evidence date, using same-day close from stock-web rows.  This deliberately tests whether the broadly visible memory recovery narrative still produced durable equipment alpha after the macro signal became explicit.

## 4. Case table

| case_id | symbol | name | trigger_type | entry_date | entry_close | peak_date | peak_high | trough_date | trough_low | MFE | MAE | classification |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C10-L108-001 | 240810 | 원익IPS | memory_recovery_equipment_beta | 2024-04-25 | 36,950 | 2024-07-04 | 40,300 | 2024-12-09 | 21,150 | +9.07% | -42.76% | counterexample_low_mfe_high_mae |
| C10-L108-002 | 095610 | 테스 | memory_deposition_equipment_beta | 2024-04-25 | 26,100 | 2024-06-27 | 27,800 | 2024-12-09 | 13,090 | +6.51% | -49.85% | hard_counterexample |
| C10-L108-003 | 281820 | 케이씨텍 | memory_cmp_cleaning_equipment_beta | 2024-04-25 | 34,400 | 2024-07-11 | 59,000 | 2024-12-04 | 25,350 | +71.51% | -26.31% | positive_local_but_full_window_4b_watch |
| C10-L108-004 | 074600 | 원익QnC | quartz_consumable_memory_cycle_beta | 2024-04-25 | 31,550 | 2024-06-07 | 41,000 | 2024-12-09 | 16,680 | +29.95% | -47.13% | high_mfe_high_mae_counterexample |

## 5. Case notes

### 5.1 240810 원익IPS — broad memory recovery equipment beta failed durability

- Entry row: 2024-04-25 close 36,950.
- Best post-entry high: 40,300 on 2024-07-04.
- Worst post-entry low: 21,150 on 2024-12-09.
- Result: MFE +9.07%, MAE -42.76%, peak-to-trough after entry -47.52%.

Interpretation: this is not a clean C10 positive.  Memory recovery opened the door, but the equity path did not show enough durable order/revision conversion.  If current profile gives Stage2-Actionable merely for “memory equipment + recovery,” this row is residual error.

### 5.2 095610 테스 — deposition equipment label was a hard fade after explicit recovery signal

- Entry row: 2024-04-25 close 26,100.
- Best post-entry high: 27,800 on 2024-06-27.
- Worst post-entry low: 13,090 on 2024-12-09.
- Result: MFE +6.51%, MAE -49.85%, peak-to-trough after entry -52.91%.

Interpretation: this is a strong 4C-oriented counterexample.  C10 should not treat deposition equipment vocabulary as order conversion.  Without customer order, backlog, revenue timing, and OPM/revision evidence, memory-cycle beta can become a trap.

### 5.3 281820 케이씨텍 — the one strong local route, but still full-window guarded

- Entry row: 2024-04-25 close 34,400.
- Best post-entry high: 59,000 on 2024-07-11.
- Worst post-entry low: 25,350 on 2024-12-04.
- Result: MFE +71.51%, MAE -26.31%, peak-to-trough after entry -57.03%.

Interpretation: this is the useful positive row in this run, but not an unconditional Green.  The local path was strong enough to validate that memory recovery can feed into equipment alpha, yet the later drawdown says the model must demand order/revision confirmation before giving durable Stage3 weight.

### 5.4 074600 원익QnC — consumable / quartz adjacency produced a rally, not durable conversion

- Entry row: 2024-04-25 close 31,550.
- Best post-entry high: 41,000 on 2024-06-07.
- Worst post-entry low: 16,680 on 2024-12-09.
- Result: MFE +29.95%, MAE -47.13%, peak-to-trough after entry -59.32%.

Interpretation: consumables and quartz materials can move with memory capex expectations, but the row argues against promoting material/consumable adjacency to C10 Green without explicit utilization, shipment, price, and margin bridge.

## 6. Residual error diagnosis

### 6.1 Current-profile error family

```text
error_family = memory_recovery_equipment_beta_overcredit
```

The current calibrated profile likely still overcredits:

- memory recovery macro headlines;
- semiconductor equipment labels;
- deposition / cleaning / CMP vocabulary;
- consumable/quartz adjacency;
- short MFE spikes as if they were order conversion.

The actual row set shows a different mechanism:

```text
memory recovery signal
  -> initial beta rally
  -> if order / customer / backlog / revenue / OPM revision bridge is absent
  -> MFE may occur but MAE and full-window fade become dominant
```

### 6.2 Stage reading

| Evidence shape | Stage implication |
|---|---|
| Memory recovery macro only | narrative_only or Stage1 |
| Memory recovery + equipment label + price spike | Stage2 watch, not Actionable |
| Memory recovery + confirmed customer order/backlog/revenue timing | Stage2-Actionable candidate |
| Same + margin/revision confirmation + low MAE | Stage3-Yellow/Green candidate |
| No order bridge + MFE spike + >25% MAE | 4B watch or 4C risk |
| Consumable/material adjacency only | boundary / 4B watch |

## 7. Shadow rule candidate

```yaml
shadow_rule_id: c10_memory_recovery_order_revision_bridge_required
scope:
  large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
  canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
condition:
  - memory_recovery_macro_headline_present: true
  - company_label_includes_semicap_equipment_or_consumable: true
  - missing_company_specific_order_or_backlog_or_revision_bridge: true
action:
  - cap_stage: Stage2_watch
  - disallow_stage3_green: true
  - if_mfe_gt_25_and_mae_lt_minus_25: route_to_4B_watch
  - if_mfe_lt_10_and_mae_lt_minus_30: route_to_4C_candidate
rationale: C10 must distinguish memory-cycle beta from confirmed equipment order conversion.
```

## 8. Machine-readable rows

### 8.1 case_rows.jsonl

```jsonl
{"row_type":"case","case_id":"C10-L108-001","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_REVISION_BRIDGE_VS_MEMORY_BETA_AND_CONSUMABLE_LABEL_FADE","symbol":"240810","name":"원익IPS","trigger_date":"2024-04-25","trigger_type":"memory_recovery_equipment_beta","entry_date":"2024-04-25","entry_price":36950,"peak_date":"2024-07-04","peak_high":40300,"trough_date":"2024-12-09","trough_low":21150,"mfe_pct":9.07,"mae_pct":-42.76,"peak_to_trough_pct":-47.52,"classification":"counterexample_low_mfe_high_mae","profile_error":"overcredit_memory_equipment_beta_without_order_bridge","calibration_usable":true,"verified_url_repair_needed":true}
{"row_type":"case","case_id":"C10-L108-002","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_REVISION_BRIDGE_VS_MEMORY_BETA_AND_CONSUMABLE_LABEL_FADE","symbol":"095610","name":"테스","trigger_date":"2024-04-25","trigger_type":"memory_deposition_equipment_beta","entry_date":"2024-04-25","entry_price":26100,"peak_date":"2024-06-27","peak_high":27800,"trough_date":"2024-12-09","trough_low":13090,"mfe_pct":6.51,"mae_pct":-49.85,"peak_to_trough_pct":-52.91,"classification":"hard_counterexample","profile_error":"deposition_equipment_label_not_order_conversion","calibration_usable":true,"verified_url_repair_needed":true}
{"row_type":"case","case_id":"C10-L108-003","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_REVISION_BRIDGE_VS_MEMORY_BETA_AND_CONSUMABLE_LABEL_FADE","symbol":"281820","name":"케이씨텍","trigger_date":"2024-04-25","trigger_type":"memory_cmp_cleaning_equipment_beta","entry_date":"2024-04-25","entry_price":34400,"peak_date":"2024-07-11","peak_high":59000,"trough_date":"2024-12-04","trough_low":25350,"mfe_pct":71.51,"mae_pct":-26.31,"peak_to_trough_pct":-57.03,"classification":"positive_local_but_full_window_4b_watch","profile_error":"positive_route_requires_order_revision_confirmation","calibration_usable":true,"verified_url_repair_needed":true}
{"row_type":"case","case_id":"C10-L108-004","round":"R2","loop":108,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_EQUIPMENT_ORDER_REVISION_BRIDGE_VS_MEMORY_BETA_AND_CONSUMABLE_LABEL_FADE","symbol":"074600","name":"원익QnC","trigger_date":"2024-04-25","trigger_type":"quartz_consumable_memory_cycle_beta","entry_date":"2024-04-25","entry_price":31550,"peak_date":"2024-06-07","peak_high":41000,"trough_date":"2024-12-09","trough_low":16680,"mfe_pct":29.95,"mae_pct":-47.13,"peak_to_trough_pct":-59.32,"classification":"high_mfe_high_mae_counterexample","profile_error":"consumable_adjacency_not_enough_for_c10_green","calibration_usable":true,"verified_url_repair_needed":true}
```

### 8.2 trigger_rows.jsonl

```jsonl
{"row_type":"trigger","trigger_id":"C10-L108-T01","trigger_date":"2024-04-25","trigger_family":"memory_full_recovery_on_ai_demand","evidence_summary":"SK Hynix said memory market was entering full recovery cycle on AI demand; used as macro trigger spine for C10.","source_url":"https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/","trigger_scope":"macro_sector_spine_not_company_specific_order","used_for_cases":["C10-L108-001","C10-L108-002","C10-L108-003","C10-L108-004"]}
```

### 8.3 score_simulation_rows.jsonl

```jsonl
{"row_type":"score_simulation","case_id":"C10-L108-001","base_label_score":"would_have_overcredited_memory_equipment_beta","recommended_stage":"Stage2_watch_or_4C_candidate","reason":"MFE below 10% and MAE worse than -40% after macro recovery trigger."}
{"row_type":"score_simulation","case_id":"C10-L108-002","base_label_score":"would_have_overcredited_deposition_equipment_beta","recommended_stage":"4C_candidate","reason":"Low MFE, near -50% MAE, no order/revision bridge."}
{"row_type":"score_simulation","case_id":"C10-L108-003","base_label_score":"positive_memory_equipment_recovery_route","recommended_stage":"Stage2_Actionable_candidate_but_not_Green","reason":"Strong MFE but MAE exceeds -25%; requires customer/order/revision evidence for Green."}
{"row_type":"score_simulation","case_id":"C10-L108-004","base_label_score":"would_have_overcredited_quartz_consumable_adjacency","recommended_stage":"4B_watch","reason":"MFE exists but full-window MAE and peak-to-trough drawdown are severe."}
```

### 8.4 aggregate_rows.jsonl

```jsonl
{"row_type":"aggregate","round":"R2","loop":108,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"positive_case_count":1,"counterexample_count":3,"boundary_case_count":1,"current_profile_error_count":4,"verified_url_repair_needed_count":4,"mean_mfe_pct":29.51,"mean_mae_pct":-41.51,"median_mfe_pct":19.51,"median_mae_pct":-44.95}
```

### 8.5 shadow_weight_rows.jsonl

```jsonl
{"row_type":"shadow_weight","shadow_rule_id":"c10_memory_recovery_order_revision_bridge_required","target_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","suggested_effect":"cap_stage_without_order_revision_bridge","production_scoring_changed":false,"rationale":"Three of four rows show memory/equipment beta failed durable conversion; only one row had strong local MFE and still needed 4B guardrail."}
```

### 8.6 residual_contribution_rows.jsonl

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":108,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c10_memory_recovery_order_revision_bridge_required","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to memory recovery equipment and consumable rallies","existing_axis_weakened":null,"next_recommended_archetypes":["C14_EV_DEMAND_SLOWDOWN_4B_4C","C11_BATTERY_ORDERBOOK_RERATING","C02_POWER_GRID_DATACENTER_CAPEX"]}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this in the current research session.

```text
You are the coding agent for Songdaiki/stock_agent.

Input artifact:
- e2r_stock_web_v12_residual_round_R2_loop_108_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md

Task:
1. Parse the embedded JSONL rows.
2. Add these rows to the v12 calibration registry if they are not duplicates.
3. Preserve no-repeat key: canonical_archetype_id + symbol + trigger_type + entry_date.
4. Do not alter production scoring directly.
5. Add only shadow-rule / research calibration artifacts for:
   - c10_memory_recovery_order_revision_bridge_required
6. Keep all rows marked verified_url_repair_needed=true in a URL repair queue until firm-specific customer/order/revision evidence is attached.
7. Treat C10 memory recovery macro headlines as insufficient for Stage3-Green unless company-specific order/backlog/revenue/margin/revision evidence exists.
```

## 10. Final summary block

```text
selected_round: R2
selected_loop: 108
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_EQUIPMENT_ORDER_REVISION_BRIDGE_VS_MEMORY_BETA_AND_CONSUMABLE_LABEL_FADE
selected_priority_bucket: Priority 0
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable case 수: 4
positive_case_count: 1
counterexample_count: 3
boundary_case_count: 1
current_profile_error_count: 4
verified_url_repair_needed_count: 4
do_not_propose_new_weight_delta: false
production_scoring_changed: false
shadow_weight_only: true
auto_selected_coverage_gap: C10 rows 21, 30-row target까지 9 부족, 50-row target까지 29 부족
new_axis_proposed: c10_memory_recovery_order_revision_bridge_required
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C10 memory recovery equipment/consumable rallies
next_recommended_archetypes: C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX
```
