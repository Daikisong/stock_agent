# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R3
selected_loop: 98
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows / C14 rows 11 need-to-30 19
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: mixed_C14_battery_equipment_capex_delay_calloff_boundary_fourth_pass
loop_objective: coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression | sector_specific_rule_discovery
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_residual_round_R3_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop is a C14 fourth-pass residual study. It fills the EV-demand-slowdown archetype with battery-equipment and downstream CAPEX-delay cases that sit on the C14/C12 boundary. Static No-Repeat coverage says C14 has 11 representative rows. Current-session local adjustment already added three C14 files; this file is intended to take the session-adjusted C14 count from 26 to 31 while using five symbols not previously used inside C14 in this session.

## 1. Current Calibrated Profile Assumption

Baseline proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`. Existing axes are treated as already applied: `stage2_required_bridge`, `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `local_4b_watch_guard`, and `hard_4c_thesis_break_routes_to_4c`.

The question here is narrower than the global rule. C14 should not hard-4C every EV slowdown headline. But when a battery-equipment or material-equipment supplier shows downstream investment delay, revenue-recognition extension, single-customer CAPA dependency, or missing delivery/margin bridge, Stage3 should be blocked and the row should route to Stage2-Watch/4B until explicit recovery evidence appears.

## 2. Round / Large Sector / Canonical Archetype Scope

- `C14_EV_DEMAND_SLOWDOWN_4B_4C` maps to `R3 / L3_BATTERY_EV_GREEN_MOBILITY`.
- Scope: EV demand slowdown, battery-equipment downstream CAPEX delay, customer call-off watch, utilization/order timing, Stage2-to-4B protection, and hard-4C confirmation threshold.
- Boundary with C12: C12 asks whether a customer contract/call-off can be trusted. C14 asks whether the broader EV slowdown has already become a demand/capex/utilization break.
- Non-scope: generic battery orderbook rerating without slowdown risk is C11; AMPC/JV utilization is C13.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index marks C14 as Priority 0 with 11 rows and need-to-30 of 19. Current-session duplicate avoidance excludes previous C14 symbols:

```text
361610, 006400, 003670, 247540, 373220,
093370, 278280, 348370, 121600, 336370,
066970, 393890, 011790, 020150, 005070
```

This file uses five new C14 symbols:

```text
222080 씨아이에스
137400 피엔티
299030 하나기술
277880 티에스아이
382840 원준
```

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No hard duplicate is present under C14. Some symbols were previously useful in C12, but this file reclassifies a distinct C14 boundary: EV-chain equipment CAPEX delay and hard-4C threshold, not contract/call-off scoring alone.

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
source: Songdaiki/stock-web
source_url: https://github.com/Songdaiki/stock-web
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
profile_root: atlas/symbol_profiles
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
```

MFE/MAE formula uses the stock-web schema convention: `MFE_N_pct = (max high from entry_date through N trading rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N trading rows / entry_price - 1) * 100`.

## 5. Historical Eligibility Gate

| symbol | trigger_date | entry_date | forward_window_trading_days | calibration_usable | corporate_action_window_status |
|---|---:|---:|---:|---|---|
| 222080 | 2023-12-28 | 2023-12-28 | 180 | true | clean_180D_window |
| 137400 | 2024-06-05 | 2024-06-07 | 180 | true | clean_180D_window |
| 299030 | 2025-01-17 | 2025-01-20 | 180 | true | clean_180D_window |
| 277880 | 2024-02-07 | 2024-02-08 | 180 | true | clean_180D_window |
| 382840 | 2022-08-24 | 2022-08-25 | 180 | true | clean_180D_window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | compressed canonical | calibration meaning |
|---|---|---|
| C14_BATTERY_EQUIPMENT_DOWNSTREAM_CAPEX_DELAY_4B_PROTECTION | C14 | Explicit downstream investment delay blocks Stage3 and routes to 4B watch, not hard 4C if orders are not canceled. |
| C14_BATTERY_EQUIPMENT_BACKLOG_LATE_CHASE_HIGH_MAE | C14 | Large backlog without delivery/margin bridge can become high-MAE late chase under EV slowdown. |
| C14_PILOT_LINE_PO_OFFSET_TO_EV_SLOWDOWN_NOT_HARD_4C | C14 | A pilot-line PO can offset hard-4C routing but should not unlock Green before mass-production conversion. |
| C14_UNDISCLOSED_CUSTOMER_EQUIPMENT_CONTRACT_HIGH_MAE | C14 | Large undisclosed-customer contracts need customer/delivery/margin confirmation. |
| C14_SINGLE_CUSTOMER_BATTERY_MATERIAL_CAPEX_DEPENDENCY_HIGH_MAE | C14 | Single-customer CAPA expansion dependency amplifies EV-chain slowdown risk. |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role | current_profile_verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228 | 222080 | 씨아이에스 | Stage4B | 2023-12-28 | 2023-12-28 | 11,000 | 5.9091 | -14.5455 | 37.3636 | -14.5455 | 37.3636 | -29.0909 | positive_protection | current_profile_correct |
| C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607 | 137400 | 피엔티 | Stage2-Actionable | 2024-06-05 | 2024-06-07 | 78,000 | 14.7436 | -31.6667 | 14.7436 | -41.0897 | 14.7436 | -53.0769 | counterexample | current_profile_false_positive |
| C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120 | 299030 | 하나기술 | Stage2-Actionable | 2025-01-17 | 2025-01-20 | 23,200 | 9.6983 | -12.5000 | 12.5000 | -23.4483 | 42.4569 | -23.4483 | positive | current_profile_correct |
| C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208 | 277880 | 티에스아이 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 8,390 | 10.7271 | -5.8403 | 10.7271 | -16.3290 | 10.7271 | -35.6377 | counterexample | current_profile_false_positive |
| C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825 | 382840 | 원준 | Stage2-Actionable | 2022-08-24 | 2022-08-25 | 33,350 | 5.8471 | -44.6777 | 5.8471 | -51.8741 | 5.8471 | -51.8741 | counterexample | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 2
counterexample_count: 3
4B_case_count: 5
4C_case_count: 0
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
current_profile_error_count: 3
new_independent_case_count: 5
reused_case_count: 0
new_symbol_count_inside_C14: 5
```

The useful result is not a new global 4C rule. The useful result is a C14-specific split: EV slowdown plus explicit customer inventory, production stop, order cut, utilization collapse, or operating-loss confirmation can be hard 4C; equipment backlog, pilot PO, or downstream CAPEX delay without cancellation should route to Stage2-Watch/4B.

## 9. Evidence Source Map

| symbol | evidence date | source URL | evidence used |
|---|---:|---|---|
| 222080 | 2023-12-28 | https://securities.miraeasset.com/bbs/download/2119746.pdf?attachmentId=2119746 | Mirae report cut 4Q23 revenue and operating-profit forecasts sharply because downstream battery equipment investment timing was delayed, even though expected backlog remained large. |
| 137400 | 2024-06-05 | https://www.thelec.kr/news/articleView.html?idxno=28363 | The Elec reported management targets and a very large order backlog, but the revenue plan still depended on future LFP/battery-material equipment conversion rather than already confirmed utilization/margin recovery. |
| 299030 | 2025-01-17 | https://www.venturesquare.net/en/1027651/ | VentureSquare reported a formal PO for all-solid-state WIP equipment from a domestic battery maker to be supplied to a pilot line in 1H25; this is real non-price evidence but still pilot-line rather than mass-production conversion. |
| 277880 | 2024-02-07 | https://www.thebell.co.kr/front/newsview.asp?key=202402060834513600109361 | The Bell reported a large mixing-system equipment supply contract and increased backlog, but counterparty and delivery/margin details were not enough to disprove EV-chain capex timing risk. |
| 382840 | 2022-08-24 | https://ssl.pstatic.net/imgstock/upload/research/company/1661296011156.pdf | Yuanta/Naver report tied new orders and backlog momentum to POSCO Chemical CAPA expansion; the forward path shows why single-customer CAPA dependency should be treated as EV-chain slowdown amplifier. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | corporate-action status |
|---|---|---|---|
| 222080 | atlas/ohlcv_tradable_by_symbol_year/222/222080/2023.csv | atlas/symbol_profiles/222/222080.json | clean_180D_window |
| 137400 | atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv | atlas/symbol_profiles/137/137400.json | clean_180D_window |
| 299030 | atlas/ohlcv_tradable_by_symbol_year/299/299030/2025.csv | atlas/symbol_profiles/299/299030.json | clean_180D_window |
| 277880 | atlas/ohlcv_tradable_by_symbol_year/277/277880/2024.csv | atlas/symbol_profiles/277/277880.json | clean_180D_window |
| 382840 | atlas/ohlcv_tradable_by_symbol_year/382/382840/2022.csv | atlas/symbol_profiles/382/382840.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228 — 씨아이에스 (222080)
- Evidence: Mirae report cut 4Q23 revenue and operating-profit forecasts sharply because downstream battery equipment investment timing was delayed, even though expected backlog remained large.
- Price alignment: entry 2023-12-28 at 11,000; 90D MFE/MAE 37.3636% / -14.5455%; 180D MFE/MAE 37.3636% / -29.0909%; peak 2024-03-11 at 15,110; drawdown after peak -48.3786%.
- Calibration conclusion: ev_downstream_capex_delay_blocks_green_but_not_hard_4c.

### C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607 — 피엔티 (137400)
- Evidence: The Elec reported management targets and a very large order backlog, but the revenue plan still depended on future LFP/battery-material equipment conversion rather than already confirmed utilization/margin recovery.
- Price alignment: entry 2024-06-07 at 78,000; 90D MFE/MAE 14.7436% / -41.0897%; 180D MFE/MAE 14.7436% / -53.0769%; peak 2024-06-19 at 89,500; drawdown after peak -59.1061%.
- Calibration conclusion: backlog_headline_does_not_override_ev_capex_timing_risk.

### C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120 — 하나기술 (299030)
- Evidence: VentureSquare reported a formal PO for all-solid-state WIP equipment from a domestic battery maker to be supplied to a pilot line in 1H25; this is real non-price evidence but still pilot-line rather than mass-production conversion.
- Price alignment: entry 2025-01-20 at 23,200; 90D MFE/MAE 12.5000% / -23.4483%; 180D MFE/MAE 42.4569% / -23.4483%; peak 2025-10-21 at 33,050; drawdown after peak -12.8593%.
- Calibration conclusion: pilot_order_can_block_hard_4c_but_not_unlock_green.

### C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208 — 티에스아이 (277880)
- Evidence: The Bell reported a large mixing-system equipment supply contract and increased backlog, but counterparty and delivery/margin details were not enough to disprove EV-chain capex timing risk.
- Price alignment: entry 2024-02-08 at 8,390; 90D MFE/MAE 10.7271% / -16.3290%; 180D MFE/MAE 10.7271% / -35.6377%; peak 2024-03-12 at 9,290; drawdown after peak -41.8730%.
- Calibration conclusion: large_equipment_contract_without_named_customer_or_delivery_bridge.

### C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825 — 원준 (382840)
- Evidence: Yuanta/Naver report tied new orders and backlog momentum to POSCO Chemical CAPA expansion; the forward path shows why single-customer CAPA dependency should be treated as EV-chain slowdown amplifier.
- Price alignment: entry 2022-08-25 at 33,350; 90D MFE/MAE 5.8471% / -51.8741%; 180D MFE/MAE 5.8471% / -51.8741%; peak 2022-08-29 at 35,300; drawdown after peak -54.5326%.
- Calibration conclusion: single_customer_capa_plan_is_not_demand_resilience.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | corp_action |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 222080 | 2023-12-28 | 11,000 | 5.9091 | -14.5455 | 37.3636 | -14.5455 | 37.3636 | -29.0909 | 2024-03-11 | 15,110 | -48.3786 | clean_180D_window |
| 137400 | 2024-06-07 | 78,000 | 14.7436 | -31.6667 | 14.7436 | -41.0897 | 14.7436 | -53.0769 | 2024-06-19 | 89,500 | -59.1061 | clean_180D_window |
| 299030 | 2025-01-20 | 23,200 | 9.6983 | -12.5000 | 12.5000 | -23.4483 | 42.4569 | -23.4483 | 2025-10-21 | 33,050 | -12.8593 | clean_180D_window |
| 277880 | 2024-02-08 | 8,390 | 10.7271 | -5.8403 | 10.7271 | -16.3290 | 10.7271 | -35.6377 | 2024-03-12 | 9,290 | -41.8730 | clean_180D_window |
| 382840 | 2022-08-25 | 33,350 | 5.8471 | -44.6777 | 5.8471 | -51.8741 | 5.8471 | -51.8741 | 2022-08-29 | 35,300 | -54.5326 | clean_180D_window |

Aggregate path:

```yaml
mean_MFE_90D_pct: 16.2363
mean_MAE_90D_pct: -29.4573
mean_MFE_180D_pct: 22.2277
mean_MAE_180D_pct: -38.6256
```

## 13. Current Calibrated Profile Stress Test

| symbol | before stage | before score | after stage | after score | residual implication |
|---:|---|---:|---|---:|---|
| 222080 | Stage3-Yellow | 77.0 | Stage2-Watch/4B | 66.0 | ev_downstream_capex_delay_blocks_green_but_not_hard_4c |
| 137400 | Stage3-Yellow | 78.5 | Stage2-Watch/4B | 63.5 | backlog_headline_does_not_override_ev_capex_timing_risk |
| 299030 | Stage2-Actionable | 69.0 | Stage2-Actionable/Watch | 70.5 | pilot_order_can_block_hard_4c_but_not_unlock_green |
| 277880 | Stage3-Yellow | 76.0 | Stage2-Watch/4B | 62.5 | large_equipment_contract_without_named_customer_or_delivery_bridge |
| 382840 | Stage3-Yellow | 75.5 | Stage2-Watch/4B | 60.5 | single_customer_capa_plan_is_not_demand_resilience |

Residual error types found:

```text
battery_equipment_backlog_late_chase_high_MAE
downstream_capex_delay_green_block
pilot_PO_offset_not_green
single_customer_capa_dependency_high_MAE
do_not_hard_4c_without_explicit_order_cut_or_production_stop
```

## 14. Stage3 Yellow / Green Lateness Audit

No row deserves immediate Stage3-Green at trigger. The audit is not that Green was too late; it is that C14 can accidentally over-promote backlog/CAPA narratives into Yellow before the EV-chain demand break is resolved. Hana Technology is the only row where a pilot-line PO provides enough non-price evidence to avoid hard 4C, but even there the correct state is Stage2-Actionable/Watch, not Green.

## 15. 4B / 4C Timing Audit

- 4B local vs full-window split: PNT, TSI, and Wonjun have limited MFE and severe full-window MAE, so C14 should prefer local 4B/watch when backlog or customer CAPA evidence lacks delivery and margin confirmation.
- 4C protection: none of these rows should be hard 4C at trigger because none has explicit cancellation, order cut, customer call-off, production stop, or utilization collapse at the trigger date. The rule should escalate to hard 4C only after those facts appear.
- Positive protection: CIS shows why a 4B block can be correct even if later MFE opens; the drawdown after peak was almost -48.4%, so Green without a watch overlay would still be unsafe.

## 16. Proposed Sector / Canonical Shadow Rule

```text
C14_EV_SLOWDOWN_EQUIPMENT_CAPEX_DELAY_REQUIRES_EXPLICIT_ORDER_CUT_OR_UTILIZATION_BREAK_FOR_4C
```

Rule text:

```text
For C14, battery-equipment backlog or customer CAPA plans under EV slowdown should remain Stage2-Watch/4B unless delivery timing, mass-production conversion, utilization recovery, and margin bridge are confirmed. Route hard 4C only when there is explicit customer call-off, order cut, production stop, utilization collapse, operating-loss thesis break, or inventory-driven shutdown evidence. Do not treat pilot-line PO as Stage3-Green; treat it as a hard-4C blocker and Stage2-Actionable evidence until mass-production conversion appears.
```

Existing axes strengthened:

```text
stage2_required_bridge
local_4b_watch_guard
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
price_only_blowoff_blocks_positive_stage
```

## 17. Machine-Readable Rows JSONL

```jsonl
{"row_type":"case","case_id":"C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228","symbol":"222080","company_name":"씨아이에스","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_BATTERY_EQUIPMENT_DOWNSTREAM_CAPEX_DELAY_4B_PROTECTION","case_type":"downstream_investment_delay_4b_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228_Stage4B_2023-12-28","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ev_downstream_capex_delay_blocks_green_but_not_hard_4c","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Mirae report cut 4Q23 revenue and operating-profit forecasts sharply because downstream battery equipment investment timing was delayed, even though expected backlog remained large."}
{"row_type":"trigger","trigger_id":"C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228_Stage4B_2023-12-28","case_id":"C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228","symbol":"222080","company_name":"씨아이에스","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_BATTERY_EQUIPMENT_DOWNSTREAM_CAPEX_DELAY_4B_PROTECTION","sector":"battery_ev_green_mobility","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2023-12-28","evidence_available_at_that_date":"Mirae report cut 4Q23 revenue and operating-profit forecasts sharply because downstream battery equipment investment timing was delayed, even though expected backlog remained large.","evidence_source":"https://securities.miraeasset.com/bbs/download/2119746.pdf?attachmentId=2119746","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["customer_capex_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222080/2023.csv","profile_path":"atlas/symbol_profiles/222/222080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-28","entry_price":11000.0,"MFE_30D_pct":5.9091,"MFE_90D_pct":37.3636,"MFE_180D_pct":37.3636,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.5455,"MAE_90D_pct":-14.5455,"MAE_180D_pct":-29.0909,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-11","peak_price":15110.0,"drawdown_after_peak_pct":-48.3786,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"local_or_full_window_watch","four_b_full_window_peak_proximity":"full_window_drawdown_confirms_watch","four_b_timing_verdict":"4b_watch_required_before_green","four_b_evidence_type":["customer_capex_delay","delivery_or_revenue_timing_risk","single_customer_dependency"],"four_c_protection_label":"do_not_route_hard_4c_without_explicit_order_cut_or_production_stop","trigger_outcome_label":"ev_downstream_capex_delay_blocks_green_but_not_hard_4c","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|222080|2023-12-28|11000.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228","trigger_id":"C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228_Stage4B_2023-12-28","symbol":"222080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":80,"backlog_visibility_score":86,"margin_bridge_score":52,"revision_score":55,"relative_strength_score":58,"customer_quality_score":66,"valuation_repricing_score":60,"execution_risk_score":48,"legal_or_contract_risk_score":30,"accounting_trust_risk_score":10},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":72,"backlog_visibility_score":72,"margin_bridge_score":48,"revision_score":50,"relative_strength_score":50,"customer_quality_score":62,"valuation_repricing_score":48,"execution_risk_score":72,"legal_or_contract_risk_score":50,"accounting_trust_risk_score":10},"weighted_score_after":66.0,"stage_label_after":"Stage2-Watch/4B","changed_components":["customer_capex_delay_gate","delivery_revenue_confirmation_gate","hard_4c_requires_explicit_cut_or_stop"],"component_delta_explanation":"Mirae report cut 4Q23 revenue and operating-profit forecasts sharply because downstream battery equipment investment timing was delayed, even though expected backlog remained large.","MFE_90D_pct":37.3636,"MAE_90D_pct":-14.5455,"score_return_alignment_label":"ev_downstream_capex_delay_blocks_green_but_not_hard_4c","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607","symbol":"137400","company_name":"피엔티","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_BATTERY_EQUIPMENT_BACKLOG_LATE_CHASE_HIGH_MAE","case_type":"large_backlog_without_delivery_margin_bridge_high_mae","positive_or_counterexample":"counterexample","best_trigger":"C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607_Stage2_Actionable_2024-06-07","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"backlog_headline_does_not_override_ev_capex_timing_risk","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The Elec reported management targets and a very large order backlog, but the revenue plan still depended on future LFP/battery-material equipment conversion rather than already confirmed utilization/margin recovery."}
{"row_type":"trigger","trigger_id":"C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607_Stage2_Actionable_2024-06-07","case_id":"C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607","symbol":"137400","company_name":"피엔티","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_BATTERY_EQUIPMENT_BACKLOG_LATE_CHASE_HIGH_MAE","sector":"battery_ev_green_mobility","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-05","evidence_available_at_that_date":"The Elec reported management targets and a very large order backlog, but the revenue plan still depended on future LFP/battery-material equipment conversion rather than already confirmed utilization/margin recovery.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=28363","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["customer_capex_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","profile_path":"atlas/symbol_profiles/137/137400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-07","entry_price":78000.0,"MFE_30D_pct":14.7436,"MFE_90D_pct":14.7436,"MFE_180D_pct":14.7436,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-31.6667,"MAE_90D_pct":-41.0897,"MAE_180D_pct":-53.0769,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":89500.0,"drawdown_after_peak_pct":-59.1061,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"local_or_full_window_watch","four_b_full_window_peak_proximity":"full_window_drawdown_confirms_watch","four_b_timing_verdict":"4b_watch_required_before_green","four_b_evidence_type":["customer_capex_delay","delivery_or_revenue_timing_risk","single_customer_dependency"],"four_c_protection_label":"do_not_route_hard_4c_without_explicit_order_cut_or_production_stop","trigger_outcome_label":"backlog_headline_does_not_override_ev_capex_timing_risk","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|137400|2024-06-07|78000.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607","trigger_id":"C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607_Stage2_Actionable_2024-06-07","symbol":"137400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":76,"backlog_visibility_score":86,"margin_bridge_score":40,"revision_score":42,"relative_strength_score":58,"customer_quality_score":66,"valuation_repricing_score":60,"execution_risk_score":48,"legal_or_contract_risk_score":30,"accounting_trust_risk_score":10},"weighted_score_before":78.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":66,"margin_bridge_score":34,"revision_score":38,"relative_strength_score":42,"customer_quality_score":54,"valuation_repricing_score":40,"execution_risk_score":84,"legal_or_contract_risk_score":62,"accounting_trust_risk_score":10},"weighted_score_after":63.5,"stage_label_after":"Stage2-Watch/4B","changed_components":["customer_capex_delay_gate","delivery_revenue_confirmation_gate","hard_4c_requires_explicit_cut_or_stop"],"component_delta_explanation":"The Elec reported management targets and a very large order backlog, but the revenue plan still depended on future LFP/battery-material equipment conversion rather than already confirmed utilization/margin recovery.","MFE_90D_pct":14.7436,"MAE_90D_pct":-41.0897,"score_return_alignment_label":"backlog_headline_does_not_override_ev_capex_timing_risk","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120","symbol":"299030","company_name":"하나기술","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_PILOT_LINE_PO_OFFSET_TO_EV_SLOWDOWN_NOT_HARD_4C","case_type":"pilot_line_po_offsets_ev_slowdown_watch_not_green","positive_or_counterexample":"positive","best_trigger":"C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120_Stage2_Actionable_2025-01-20","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"pilot_order_can_block_hard_4c_but_not_unlock_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"VentureSquare reported a formal PO for all-solid-state WIP equipment from a domestic battery maker to be supplied to a pilot line in 1H25; this is real non-price evidence but still pilot-line rather than mass-production conversion."}
{"row_type":"trigger","trigger_id":"C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120_Stage2_Actionable_2025-01-20","case_id":"C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120","symbol":"299030","company_name":"하나기술","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_PILOT_LINE_PO_OFFSET_TO_EV_SLOWDOWN_NOT_HARD_4C","sector":"battery_ev_green_mobility","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-17","evidence_available_at_that_date":"VentureSquare reported a formal PO for all-solid-state WIP equipment from a domestic battery maker to be supplied to a pilot line in 1H25; this is real non-price evidence but still pilot-line rather than mass-production conversion.","evidence_source":"https://www.venturesquare.net/en/1027651/","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["customer_capex_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/299/299030/2025.csv","profile_path":"atlas/symbol_profiles/299/299030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-01-20","entry_price":23200.0,"MFE_30D_pct":9.6983,"MFE_90D_pct":12.5,"MFE_180D_pct":42.4569,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.5,"MAE_90D_pct":-23.4483,"MAE_180D_pct":-23.4483,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-21","peak_price":33050.0,"drawdown_after_peak_pct":-12.8593,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"local_or_full_window_watch","four_b_full_window_peak_proximity":"full_window_drawdown_confirms_watch","four_b_timing_verdict":"4b_watch_required_before_green","four_b_evidence_type":["customer_capex_delay","delivery_or_revenue_timing_risk","single_customer_dependency"],"four_c_protection_label":"do_not_route_hard_4c_without_explicit_order_cut_or_production_stop","trigger_outcome_label":"pilot_order_can_block_hard_4c_but_not_unlock_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|299030|2025-01-20|23200.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120","trigger_id":"C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120_Stage2_Actionable_2025-01-20","symbol":"299030","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":80,"backlog_visibility_score":86,"margin_bridge_score":52,"revision_score":55,"relative_strength_score":58,"customer_quality_score":66,"valuation_repricing_score":60,"execution_risk_score":48,"legal_or_contract_risk_score":30,"accounting_trust_risk_score":10},"weighted_score_before":69.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":72,"backlog_visibility_score":72,"margin_bridge_score":48,"revision_score":50,"relative_strength_score":50,"customer_quality_score":62,"valuation_repricing_score":48,"execution_risk_score":72,"legal_or_contract_risk_score":50,"accounting_trust_risk_score":10},"weighted_score_after":70.5,"stage_label_after":"Stage2-Actionable/Watch","changed_components":["customer_capex_delay_gate","delivery_revenue_confirmation_gate","hard_4c_requires_explicit_cut_or_stop"],"component_delta_explanation":"VentureSquare reported a formal PO for all-solid-state WIP equipment from a domestic battery maker to be supplied to a pilot line in 1H25; this is real non-price evidence but still pilot-line rather than mass-production conversion.","MFE_90D_pct":12.5,"MAE_90D_pct":-23.4483,"score_return_alignment_label":"pilot_order_can_block_hard_4c_but_not_unlock_green","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208","symbol":"277880","company_name":"티에스아이","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_UNDISCLOSED_CUSTOMER_EQUIPMENT_CONTRACT_HIGH_MAE","case_type":"undisclosed_customer_large_contract_not_enough_under_ev_capex_slowdown","positive_or_counterexample":"counterexample","best_trigger":"C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208_Stage2_Actionable_2024-02-08","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"large_equipment_contract_without_named_customer_or_delivery_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The Bell reported a large mixing-system equipment supply contract and increased backlog, but counterparty and delivery/margin details were not enough to disprove EV-chain capex timing risk."}
{"row_type":"trigger","trigger_id":"C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208_Stage2_Actionable_2024-02-08","case_id":"C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208","symbol":"277880","company_name":"티에스아이","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_UNDISCLOSED_CUSTOMER_EQUIPMENT_CONTRACT_HIGH_MAE","sector":"battery_ev_green_mobility","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","evidence_available_at_that_date":"The Bell reported a large mixing-system equipment supply contract and increased backlog, but counterparty and delivery/margin details were not enough to disprove EV-chain capex timing risk.","evidence_source":"https://www.thebell.co.kr/front/newsview.asp?key=202402060834513600109361","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["customer_capex_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/277/277880/2024.csv","profile_path":"atlas/symbol_profiles/277/277880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":8390.0,"MFE_30D_pct":10.7271,"MFE_90D_pct":10.7271,"MFE_180D_pct":10.7271,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.8403,"MAE_90D_pct":-16.329,"MAE_180D_pct":-35.6377,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":9290.0,"drawdown_after_peak_pct":-41.873,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"local_or_full_window_watch","four_b_full_window_peak_proximity":"full_window_drawdown_confirms_watch","four_b_timing_verdict":"4b_watch_required_before_green","four_b_evidence_type":["customer_capex_delay","delivery_or_revenue_timing_risk","single_customer_dependency"],"four_c_protection_label":"do_not_route_hard_4c_without_explicit_order_cut_or_production_stop","trigger_outcome_label":"large_equipment_contract_without_named_customer_or_delivery_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|277880|2024-02-08|8390.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208","trigger_id":"C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208_Stage2_Actionable_2024-02-08","symbol":"277880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":76,"backlog_visibility_score":86,"margin_bridge_score":40,"revision_score":42,"relative_strength_score":58,"customer_quality_score":66,"valuation_repricing_score":60,"execution_risk_score":48,"legal_or_contract_risk_score":30,"accounting_trust_risk_score":10},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":66,"margin_bridge_score":34,"revision_score":38,"relative_strength_score":42,"customer_quality_score":54,"valuation_repricing_score":40,"execution_risk_score":84,"legal_or_contract_risk_score":62,"accounting_trust_risk_score":10},"weighted_score_after":62.5,"stage_label_after":"Stage2-Watch/4B","changed_components":["customer_capex_delay_gate","delivery_revenue_confirmation_gate","hard_4c_requires_explicit_cut_or_stop"],"component_delta_explanation":"The Bell reported a large mixing-system equipment supply contract and increased backlog, but counterparty and delivery/margin details were not enough to disprove EV-chain capex timing risk.","MFE_90D_pct":10.7271,"MAE_90D_pct":-16.329,"score_return_alignment_label":"large_equipment_contract_without_named_customer_or_delivery_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825","symbol":"382840","company_name":"원준","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_SINGLE_CUSTOMER_BATTERY_MATERIAL_CAPEX_DEPENDENCY_HIGH_MAE","case_type":"single_customer_capa_dependency_ev_slowdown_amplifier","positive_or_counterexample":"counterexample","best_trigger":"C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825_Stage2_Actionable_2022-08-25","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"single_customer_capa_plan_is_not_demand_resilience","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Yuanta/Naver report tied new orders and backlog momentum to POSCO Chemical CAPA expansion; the forward path shows why single-customer CAPA dependency should be treated as EV-chain slowdown amplifier."}
{"row_type":"trigger","trigger_id":"C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825_Stage2_Actionable_2022-08-25","case_id":"C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825","symbol":"382840","company_name":"원준","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_SINGLE_CUSTOMER_BATTERY_MATERIAL_CAPEX_DEPENDENCY_HIGH_MAE","sector":"battery_ev_green_mobility","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-24","evidence_available_at_that_date":"Yuanta/Naver report tied new orders and backlog momentum to POSCO Chemical CAPA expansion; the forward path shows why single-customer CAPA dependency should be treated as EV-chain slowdown amplifier.","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1661296011156.pdf","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["customer_capex_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/382/382840/2022.csv","profile_path":"atlas/symbol_profiles/382/382840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-25","entry_price":33350.0,"MFE_30D_pct":5.8471,"MFE_90D_pct":5.8471,"MFE_180D_pct":5.8471,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-44.6777,"MAE_90D_pct":-51.8741,"MAE_180D_pct":-51.8741,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-29","peak_price":35300.0,"drawdown_after_peak_pct":-54.5326,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"local_or_full_window_watch","four_b_full_window_peak_proximity":"full_window_drawdown_confirms_watch","four_b_timing_verdict":"4b_watch_required_before_green","four_b_evidence_type":["customer_capex_delay","delivery_or_revenue_timing_risk","single_customer_dependency"],"four_c_protection_label":"do_not_route_hard_4c_without_explicit_order_cut_or_production_stop","trigger_outcome_label":"single_customer_capa_plan_is_not_demand_resilience","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C|382840|2022-08-25|33350.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825","trigger_id":"C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825_Stage2_Actionable_2022-08-25","symbol":"382840","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":76,"backlog_visibility_score":86,"margin_bridge_score":40,"revision_score":42,"relative_strength_score":58,"customer_quality_score":66,"valuation_repricing_score":60,"execution_risk_score":48,"legal_or_contract_risk_score":30,"accounting_trust_risk_score":10},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":66,"margin_bridge_score":34,"revision_score":38,"relative_strength_score":42,"customer_quality_score":54,"valuation_repricing_score":40,"execution_risk_score":84,"legal_or_contract_risk_score":62,"accounting_trust_risk_score":10},"weighted_score_after":60.5,"stage_label_after":"Stage2-Watch/4B","changed_components":["customer_capex_delay_gate","delivery_revenue_confirmation_gate","hard_4c_requires_explicit_cut_or_stop"],"component_delta_explanation":"Yuanta/Naver report tied new orders and backlog momentum to POSCO Chemical CAPA expansion; the forward path shows why single-customer CAPA dependency should be treated as EV-chain slowdown amplifier.","MFE_90D_pct":5.8471,"MAE_90D_pct":-51.8741,"score_return_alignment_label":"single_customer_capa_plan_is_not_demand_resilience","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"aggregate","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"mixed_C14_battery_equipment_capex_delay_calloff_boundary_fourth_pass","new_independent_case_count":5,"reused_case_count":0,"positive_case_count":2,"counterexample_count":3,"four_b_case_count":5,"four_c_case_count":0,"current_profile_error_count":3,"calibration_usable_rows":5,"representative_rows":5,"mean_MFE_90D_pct":16.2363,"mean_MAE_90D_pct":-29.4573,"mean_MFE_180D_pct":22.2277,"mean_MAE_180D_pct":-38.6256,"rule_candidate":"C14_EV_SLOWDOWN_EQUIPMENT_CAPEX_DELAY_REQUIRES_EXPLICIT_ORDER_CUT_OR_UTILIZATION_BREAK_FOR_4C"}
{"row_type":"shadow_weight","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","shadow_rule_id":"C14_EV_SLOWDOWN_EQUIPMENT_CAPEX_DELAY_REQUIRES_EXPLICIT_ORDER_CUT_OR_UTILIZATION_BREAK_FOR_4C","shadow_weight_only":true,"production_scoring_changed":false,"proposed_effect":"increase execution_risk/calloff_risk penalty when downstream battery-equipment capex delay or single-customer CAPA dependency is visible; do not route hard 4C without explicit order cut, production stop, utilization collapse, or customer call-off","do_not_apply_now":true}
{"row_type":"residual_contribution","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["battery_equipment_backlog_late_chase_high_MAE","downstream_capex_delay_green_block","pilot_PO_offset_not_green","single_customer_capa_dependency_high_MAE","do_not_hard_4c_without_explicit_calloff"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 18. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for stock_agent. Do not use this prompt during the research session. Later, when batch-applying research MDs, ingest this file as a standard V12 result:

e2r_stock_web_v12_residual_round_R3_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md

Use only the machine-readable rows above for deterministic scoring updates. Treat the proposed C14 axis as a shadow candidate, not a production change:

- C14_EV_SLOWDOWN_EQUIPMENT_CAPEX_DELAY_REQUIRES_EXPLICIT_ORDER_CUT_OR_UTILIZATION_BREAK_FOR_4C

Validate all trigger rows against stock-web tradable shards. Require all six canonical price fields: MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date. Do not apply a hard-4C rule from this loop alone; this loop proposes a C14 watch-to-4C escalator only when explicit order cut, customer call-off, production stop, utilization collapse, or operating-loss thesis break appears.
```

## 19. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 20. Research State for Next Loop

```yaml
completed_round: R3
completed_loop: 98
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_rows: 5
positive_case_count: 2
counterexample_count: 3
4B_case_count: 5
4C_case_count: 0
current_profile_error_count: 3
do_not_propose_new_weight_delta: false
static_no_repeat_C14_rows_before: 11
static_no_repeat_C14_rows_after_if_accepted: 16
current_session_adjusted_C14_rows_before: 26
current_session_adjusted_C14_rows_after_if_accepted: 31
sector_specific_rule_candidate: L3_C14_BATTERY_EQUIPMENT_EV_SLOWDOWN_CAPEX_DELAY_GATE
canonical_archetype_rule_candidate: C14_EV_SLOWDOWN_EQUIPMENT_CAPEX_DELAY_REQUIRES_EXPLICIT_ORDER_CUT_OR_UTILIZATION_BREAK_FOR_4C
loop_contribution_label: canonical_archetype_rule_candidate
existing_axis_strengthened: stage2_required_bridge | local_4b_watch_guard | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
next_recommended_archetypes: C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_if_still_below_30 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_followup_if_below_50 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C05_EPC_MEGA_CONTRACT_MARGIN_GAP_followup_if_below_50
```
