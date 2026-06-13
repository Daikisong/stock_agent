# E2R Stock-Web V12 Residual Research — R2 / Loop 129 / L2 / C06

```yaml
document_type: stock_web_v12_sector_archetype_residual_calibration_md
output_filename: e2r_stock_web_v12_residual_round_R2_loop_129_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 129
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: mixed_hbm_customer_capacity_qualification_and_booked_supply_leaf_set
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

The coverage ledger says C06_HBM_MEMORY_CUSTOMER_CAPACITY is still Priority 0 with 17 representative rows, needing 13 rows to reach 30 and 33 rows to reach 50. This run intentionally does not continue the immediately previous in-session C02, C09, C14, and C10 axes. It moves to the next thin L2 canonical archetype while staying in the valid R2 / L2 mapping.

C06 is not merely "memory is recovering." It is the narrower bridge where HBM customer qualification, booked or sold-out capacity, product mix, ASP, and revision visibility turn a memory-cycle headline into a rerating-quality event. The gate is the customer-capacity pipe: if the pipe is attached to a named customer and filled with booked capacity, the rerating water can flow; if the pipe is only a label on the wall, the price path often leaks into 4B or false Stage2.

## 2. Price atlas and profile audit

```yaml
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
mfe_mae_formula: entry 이후 N tradable rows 안의 max(high), min(low)를 entry_price와 비교
forward_window_required: 180 tradable days
symbols:
  "000660":
    name: SK하이닉스
    profile_path: atlas/symbol_profiles/000/000660.json
    profile_last_date: 2026-02-20
    corporate_action_candidate_dates: ["1998-07-03","1999-01-07","1999-07-06","1999-10-27","2000-01-07","2001-06-27","2002-06-07","2003-04-14","2003-04-21"]
    entry_windows_status: clean_2024_entries_to_D180
  "005930":
    name: 삼성전자
    profile_path: atlas/symbol_profiles/005/005930.json
    profile_last_date: 2026-02-20
    corporate_action_candidate_dates: ["1996-01-03","1997-01-03","2018-05-04"]
    entry_windows_status: clean_2024_entries_to_D180
```

All five trigger rows have entry_date, entry_price, trigger_type, full 30/90/180D MFE and MAE, canonical large sector ID, canonical archetype ID, and corporate-action status. No row uses compact MFE/MAE aliases.

## 3. Case design

| case | symbol | trigger_date | entry_date | intended role | observed price path |
|---|---:|---:|---:|---|---|
| SK hynix FY2023 Q4 HBM swing-profit inflection | 000660 | 2024-01-25 | 2024-01-26 | positive | 180D MFE +82.72%, MAE -3.16% |
| SK hynix Q1 2024 HBM recovery and customer bridge | 000660 | 2024-04-25 | 2024-04-26 | positive but watch MAE | 180D MFE +39.76%, MAE -18.62% |
| SK hynix Q2 2024 sold-out HBM after rerating | 000660 | 2024-07-25 | 2024-07-26 | local 4B / high-MAE counterexample | 90D MFE +7.40%, MAE -24.56% |
| Samsung HBM Nvidia qualification gap | 005930 | 2024-05-24 | 2024-05-24 | 4B / false Stage2 block | 180D MFE +17.00%, MAE -34.26% |
| Samsung Q2 guidance with HBM unlock unresolved | 005930 | 2024-07-05 | 2024-07-05 | Stage2 not actionable | 180D MFE +1.95%, MAE -42.71% |

## 4. Evidence interpretation

### 4.1 SK hynix positive: customer-capacity bridge before full rerating

The January 2024 SK hynix trigger is the cleanest C06 shape. The evidence was not just "memory bottom." It included HBM/AI demand and an operating profit swing after a downcycle. Entry on the next tradable day, 2024-01-26, captured a strong 180D path with shallow MAE.

The April 2024 trigger became stronger because Reuters described a Q1 2024 beat, highest profit since Q2 2022, advanced DRAM/HBM sales, HBM investment, and Nvidia-linked supply position. This supports Stage3-Yellow but not a free Green unlock, because by April the stock had already traveled far and the later 180D MAE widened to -18.62%.

### 4.2 SK hynix counterexample: real bridge can still be bad entry after rerating

The July 2024 SK hynix trigger had real non-price evidence: record revenue, highest quarterly profit since 2018, strong HBM demand, sold-out or nearly sold-out HBM capacity. But the entry quality was poor after a large prior run. The stock fell to a 90D MAE of -24.56% before the later recovery.

This is not a thesis-break 4C. It is a local 4B / high-MAE guardrail case: the bridge is real, but the elevator arrived after the crowd had already packed into it.

### 4.3 Samsung counterexamples: earnings recovery without HBM customer unlock

Samsung's May 2024 trigger is a direct customer-qualification gap. Reuters reported that Samsung's latest HBM chips had not yet passed Nvidia's tests due to heat and power consumption problems according to sources, while Samsung disputed the framing and said optimization with customers was proceeding. That is exactly the C06 risk: if the named customer qualification is unresolved, memory recovery alone should not be upgraded to Stage2-Actionable.

Samsung's July 2024 Q2 guidance showed huge operating-profit recovery. But the C06-specific customer-capacity gate was still not firm enough at the entry. Reuters later reported Samsung was bullish on AI demand and that Q2 HBM revenue rose about 50% QoQ, but also noted Nvidia approval was key to meeting the HBM target. Price path confirmed the guardrail: from a 2024-07-05 close entry, 180D MFE was only +1.95% while MAE reached -42.71%.

## 5. Raw component score breakdown

| trigger_id | EPS/FCF | visibility | bottleneck/pricing | mispricing | valuation | capital allocation | info confidence | raw total | shadow corrected stage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C06_000660_2024Q4_FY23_HBM_SWING_PROFIT_ENTRY_20240126 | 18 | 15 | 16 | 13 | 9 | 4 | 9 | 84 | Stage2-Actionable |
| C06_000660_2024Q1_HBM_FULL_RECOVERY_ENTRY_20240426 | 20 | 18 | 18 | 10 | 7 | 5 | 10 | 88 | Stage3-Yellow |
| C06_000660_2024Q2_HBM_SOLDOUT_HIGH_EXPECTATION_ENTRY_20240726 | 21 | 19 | 18 | 2 | -4 | 4 | 10 | 70 | Stage4B |
| C06_005930_20240524_HBM_QUALIFICATION_TRUST_BREAK_ENTRY_20240524 | 14 | 5 | 8 | 4 | 1 | 5 | 8 | 45 | Stage4B |
| C06_005930_20240705_Q2_GUIDANCE_HBM_UNRESOLVED_ENTRY_20240705 | 19 | 7 | 9 | 1 | -3 | 5 | 8 | 46 | Stage2 |

Interpretation: the raw total can look optically strong when EPS/FCF and AI/HBM vocabulary are large. The shadow gate should not subtract from true SK hynix customer-capacity positives. It should instead stop Samsung-like "profit recovery + HBM ambition" rows from becoming actionable before customer qualification and booked capacity become visible.

## 6. Current calibrated profile stress test

```yaml
tested_profile_proxy: e2r_2_1_stock_web_calibrated
known_global_rules_respected:
  stage2_actionable_evidence_bonus: not_repeated_as_new_global_finding
  price_only_blowoff_blocks_positive_stage: retained
  full_4b_requires_non_price_evidence: retained
  hard_4c_thesis_break_routes_to_4c: retained
residual_error_found:
  - error_mode: C06 customer qualification gap not separated enough from broad memory recovery
    affected_rows: ["005930 2024-05-24", "005930 2024-07-05"]
  - error_mode: true HBM bridge after large prior rerating still produces high MAE if valuation/expectation already saturated
    affected_rows: ["000660 2024-07-26"]
  - error_mode: early HBM customer-capacity bridge must not be over-penalized by broad memory cyclicality
    affected_rows: ["000660 2024-01-26", "000660 2024-04-26"]
```

## 7. Sector-specific / canonical rule candidate

```yaml
canonical_archetype_rule_candidate: C06_CUSTOMER_QUALIFICATION_BOOKED_CAPACITY_GATE_V1
sector_specific_rule_candidate: L2_HBM_CUSTOMER_CAPACITY_QUALIFICATION_AND_ENTRY_QUALITY_GATE_V1
new_axis_proposed: c06_customer_qualification_booked_capacity_gate
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
production_scoring_changed: false
shadow_weight_only: true
```

Rule candidate:

1. For C06 Stage2-Actionable, require at least one hard C06 bridge:
   - named customer qualification or de facto shipment relationship,
   - sold-out/booked HBM capacity by year,
   - HBM mix/ASP/revision bridge in earnings or company guidance,
   - CAPA expansion explicitly tied to HBM demand already verified by customer demand.
2. If the row has strong memory-cycle earnings but lacks customer qualification, cap it at Stage2 unless price path and subsequent evidence confirm the bridge.
3. If the C06 bridge is real but entry follows a sharp pre-trigger rerating, route to local 4B watch rather than Stage3-Yellow/Green unless MAE risk is controlled.
4. Do not fire hard 4C on competition/qualification anxiety alone if there is no thesis break; use 4B/watch until customer failure or guidance cut is confirmed.

## 8. Machine-readable rows

### 8.1 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"C06_000660_2024Q4_FY23_HBM_SWING_PROFIT_ENTRY_20240126","case_id":"C06_000660_HBM_CUSTOMER_CAPACITY_2024Q4_FY23","symbol":"000660","company_name":"SK하이닉스","market":"KOSPI","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_CAPACITY_QUALIFICATION_AND_BOOKED_SUPPLY","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_timing_rule":"same_day_close_after_earnings_evidence_or_next_trading_day_entry","entry_date":"2024-01-26","entry_price":136000.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":28.6,"MAE_30D_pct":-3.16,"MFE_90D_pct":54.41,"MAE_90D_pct":-3.16,"MFE_180D_pct":82.72,"MAE_180D_pct":-3.16,"peak_price_180D":248500.0,"trough_price_180D":131700.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","corporate_action_window_status":"clean_2024_entry_to_D180; profile corporate_action_candidate_dates end at 2003-04-21","calibration_usable":true,"dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage2-Actionable|2024-01-26","same_entry_group_id":"C06_000660_20240126","dedupe_for_aggregate":true,"aggregate_group_role":"representative","observed_path_label":"positive_high_mfe_low_mae","current_profile_error":false,"profile_would_stage":"Stage2-Actionable","suggested_correct_stage":"Stage2-Actionable","evidence_url":"https://www.kedglobal.com/earnings/newsView/ked202401250004","evidence_summary":"FY2023 Q4 swing to operating profit with HBM/AI demand inflection; early C06 customer-capacity bridge before full price rerating."}
{"row_type":"trigger","trigger_id":"C06_000660_2024Q1_HBM_FULL_RECOVERY_ENTRY_20240426","case_id":"C06_000660_HBM_CUSTOMER_CAPACITY_2024Q1","symbol":"000660","company_name":"SK하이닉스","market":"KOSPI","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_CAPACITY_QUALIFICATION_AND_BOOKED_SUPPLY","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-25","evidence_timing_rule":"same_day_reuters_earnings_then_next_trading_day_entry","entry_date":"2024-04-26","entry_price":177800.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":18.11,"MAE_30D_pct":-4.95,"MFE_90D_pct":39.76,"MAE_90D_pct":-14.74,"MFE_180D_pct":39.76,"MAE_180D_pct":-18.62,"peak_price_180D":248500.0,"trough_price_180D":144700.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","corporate_action_window_status":"clean_2024_entry_to_D180; profile corporate_action_candidate_dates end at 2003-04-21","calibration_usable":true,"dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage3-Yellow|2024-04-26","same_entry_group_id":"C06_000660_20240426","dedupe_for_aggregate":true,"aggregate_group_role":"representative","observed_path_label":"positive_but_mae_risk_rises_after_prior_run","current_profile_error":false,"profile_would_stage":"Stage3-Yellow","suggested_correct_stage":"Stage3-Yellow","evidence_url":"https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/","evidence_summary":"Q1 2024 earnings beat, full memory recovery, HBM-driven advanced DRAM sales, HBM capex and Nvidia supply bridge."}
{"row_type":"trigger","trigger_id":"C06_000660_2024Q2_HBM_SOLDOUT_HIGH_EXPECTATION_ENTRY_20240726","case_id":"C06_000660_HBM_POST_RERATING_HIGH_EXPECTATION_2024Q2","symbol":"000660","company_name":"SK하이닉스","market":"KOSPI","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_CAPACITY_QUALIFICATION_AND_BOOKED_SUPPLY","trigger_type":"Stage4B","trigger_date":"2024-07-25","evidence_timing_rule":"same_day_q2_earnings_after_open; next_trading_day_entry_for_audit","entry_date":"2024-07-26","entry_price":191800.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":5.58,"MAE_30D_pct":-20.96,"MFE_90D_pct":7.4,"MAE_90D_pct":-24.56,"MFE_180D_pct":18.35,"MAE_180D_pct":-24.56,"peak_price_180D":227000.0,"trough_price_180D":144700.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","corporate_action_window_status":"clean_2024_entry_to_D180; profile corporate_action_candidate_dates end at 2003-04-21","calibration_usable":true,"dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage4B|2024-07-26","same_entry_group_id":"C06_000660_20240726","dedupe_for_aggregate":true,"aggregate_group_role":"representative","observed_path_label":"counterexample_real_bridge_but_bad_entry_high_mae","current_profile_error":true,"profile_would_stage":"Stage3-Yellow","suggested_correct_stage":"Stage4B","evidence_url":"https://www.reuters.com/technology/nvidia-supplier-sk-hynixs-q2-profit-soars-ai-boom-2024-07-24/","evidence_summary":"Q2 profit highest since 2018, HBM shipment guidance strong, but expectations already high and price path shows high MAE before durable new upside."}
{"row_type":"trigger","trigger_id":"C06_005930_20240524_HBM_QUALIFICATION_TRUST_BREAK_ENTRY_20240524","case_id":"C06_005930_HBM_QUALIFICATION_BREAK_202405","symbol":"005930","company_name":"삼성전자","market":"KOSPI","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_QUALIFICATION_GAP","trigger_type":"Stage4B","trigger_date":"2024-05-24","evidence_timing_rule":"same_day_reuters_failure_report_close_entry","entry_date":"2024-05-24","entry_price":75900.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":16.73,"MAE_30D_pct":-3.16,"MFE_90D_pct":17.0,"MAE_90D_pct":-18.97,"MFE_180D_pct":17.0,"MAE_180D_pct":-34.26,"peak_price_180D":88800.0,"trough_price_180D":49900.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","corporate_action_window_status":"clean_2024_entry_to_D180; profile corporate_action_candidate_dates end at 2018-05-04","calibration_usable":true,"dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage4B|2024-05-24","same_entry_group_id":"C06_005930_20240524","dedupe_for_aggregate":true,"aggregate_group_role":"representative","observed_path_label":"counterexample_hbm_customer_qualification_gap","current_profile_error":true,"profile_would_stage":"Stage2-Actionable","suggested_correct_stage":"Stage4B","evidence_url":"https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/","evidence_summary":"Samsung HBM chips had not yet passed Nvidia qualification per Reuters sources; Samsung disputed failure characterization but acknowledged optimization with customers."}
{"row_type":"trigger","trigger_id":"C06_005930_20240705_Q2_GUIDANCE_HBM_UNRESOLVED_ENTRY_20240705","case_id":"C06_005930_Q2_GUIDANCE_HBM_APPROVAL_UNRESOLVED_202407","symbol":"005930","company_name":"삼성전자","market":"KOSPI","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_EARNINGS_RECOVERY_WITHOUT_CUSTOMER_UNLOCK","trigger_type":"Stage2","trigger_date":"2024-07-05","evidence_timing_rule":"same_day_samsung_guidance_close_entry","entry_date":"2024-07-05","entry_price":87100.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":1.95,"MAE_30D_pct":-19.4,"MFE_90D_pct":1.95,"MAE_90D_pct":-42.02,"MFE_180D_pct":1.95,"MAE_180D_pct":-42.71,"peak_price_180D":88800.0,"trough_price_180D":49900.0,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","corporate_action_window_status":"clean_2024_entry_to_D180; profile corporate_action_candidate_dates end at 2018-05-04","calibration_usable":true,"dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage2|2024-07-05","same_entry_group_id":"C06_005930_20240705","dedupe_for_aggregate":true,"aggregate_group_role":"representative","observed_path_label":"counterexample_strong_memory_earnings_but_hbm_customer_unlock_unresolved","current_profile_error":true,"profile_would_stage":"Stage2-Actionable","suggested_correct_stage":"Stage2","evidence_url":"https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-second-quarter-2024","evidence_summary":"Samsung guided Q2 2024 operating profit around KRW 10.4T, but C06 customer-capacity unlock was not yet firm; Reuters later noted Nvidia approval remained key."}
```

### 8.2 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_proxy":"e2r_2_1_stock_web_calibrated","shadow_weight_only":true,"production_scoring_changed":false,"trigger_id":"C06_000660_2024Q4_FY23_HBM_SWING_PROFIT_ENTRY_20240126","component_eps_fcf_explosion":18,"component_earnings_visibility":15,"component_bottleneck_pricing_power":16,"component_market_mispricing":13,"component_valuation_rerating":9,"component_capital_allocation":4,"component_information_confidence":9,"raw_total_score":84,"shadow_stage_after_c06_gate":"Stage2-Actionable","comment":""}
{"row_type":"score_simulation","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_proxy":"e2r_2_1_stock_web_calibrated","shadow_weight_only":true,"production_scoring_changed":false,"trigger_id":"C06_000660_2024Q1_HBM_FULL_RECOVERY_ENTRY_20240426","component_eps_fcf_explosion":20,"component_earnings_visibility":18,"component_bottleneck_pricing_power":18,"component_market_mispricing":10,"component_valuation_rerating":7,"component_capital_allocation":5,"component_information_confidence":10,"raw_total_score":88,"shadow_stage_after_c06_gate":"Stage3-Yellow","comment":""}
{"row_type":"score_simulation","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_proxy":"e2r_2_1_stock_web_calibrated","shadow_weight_only":true,"production_scoring_changed":false,"trigger_id":"C06_000660_2024Q2_HBM_SOLDOUT_HIGH_EXPECTATION_ENTRY_20240726","component_eps_fcf_explosion":21,"component_earnings_visibility":19,"component_bottleneck_pricing_power":18,"component_market_mispricing":2,"component_valuation_rerating":-4,"component_capital_allocation":4,"component_information_confidence":10,"raw_total_score":70,"shadow_stage_after_c06_gate":"Stage4B","comment":""}
{"row_type":"score_simulation","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_proxy":"e2r_2_1_stock_web_calibrated","shadow_weight_only":true,"production_scoring_changed":false,"trigger_id":"C06_005930_20240524_HBM_QUALIFICATION_TRUST_BREAK_ENTRY_20240524","component_eps_fcf_explosion":14,"component_earnings_visibility":5,"component_bottleneck_pricing_power":8,"component_market_mispricing":4,"component_valuation_rerating":1,"component_capital_allocation":5,"component_information_confidence":8,"raw_total_score":45,"shadow_stage_after_c06_gate":"Stage4B","comment":""}
{"row_type":"score_simulation","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_proxy":"e2r_2_1_stock_web_calibrated","shadow_weight_only":true,"production_scoring_changed":false,"trigger_id":"C06_005930_20240705_Q2_GUIDANCE_HBM_UNRESOLVED_ENTRY_20240705","component_eps_fcf_explosion":19,"component_earnings_visibility":7,"component_bottleneck_pricing_power":9,"component_market_mispricing":1,"component_valuation_rerating":-3,"component_capital_allocation":5,"component_information_confidence":8,"raw_total_score":46,"shadow_stage_after_c06_gate":"Stage2","comment":""}
```

### 8.3 Aggregate / shadow / residual rows JSONL

```jsonl
{"row_type":"aggregate","aggregate_id":"R2_loop129_C06_HBM_CUSTOMER_CAPACITY","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"mixed_hbm_customer_capacity_qualification_and_booked_supply_leaf_set","new_independent_case_count":5,"reused_case_count":0,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":5,"calibration_usable_case_count":5,"calibration_usable_trigger_count":5,"representative_trigger_count":5,"positive_case_count":2,"counterexample_count":3,"stage4b_case_count":2,"stage4c_case_count":0,"current_profile_error_count":3,"coverage_before_rows":17,"coverage_after_if_accepted":22,"need_to_30_after_if_accepted":8,"need_to_50_after_if_accepted":28,"do_not_propose_new_weight_delta":false,"shadow_rule_candidate":"C06_CUSTOMER_QUALIFICATION_BOOKED_CAPACITY_GATE_V1","loop_contribution_label":"canonical_archetype_rule_candidate"}
{"row_type":"shadow_weight","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","shadow_weight_only":true,"production_scoring_changed":false,"axis":"c06_customer_qualification_booked_capacity_gate","proposed_rule":"Stage2-Actionable requires named customer qualification or booked/sold-out HBM capacity plus mix/ASP/revision bridge; strong memory-cycle earnings without HBM customer unlock remains Stage2/4B depending on price extension and MAE risk.","expected_effect":"Reduce Samsung-like memory recovery false positives while preserving early SK hynix HBM customer-capacity positives.","apply_now":false}
{"row_type":"residual_contribution","selected_round":"R2","selected_loop":129,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","residual_axis":"customer_qualification_vs_memory_cycle_beta","current_profile_false_positive_count_added":3,"current_profile_too_late_count_added":0,"current_profile_correct_positive_count_added":2,"dominant_error_mode":"HBM vocabulary and memory-profit rebound can overpower customer qualification gaps or post-rerating entry risk.","recommended_next_test":"C07 HBM equipment order/revenue conversion and C11 battery orderbook rerating remain under-covered Priority 0 targets."}
```

## 9. Batch ingest self-audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
selected_round: R2
selected_loop: 129
filename_round: R2
filename_loop: 129
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
duplicate_reused_case_count: 0
same_entry_group_representative_count: 5
ready_for_batch_ingest: true
```

## 10. Residual contribution summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 2
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
positive_case_count: 2
counterexample_count: 3
current_profile_error_count: 3
stage4b_case_count: 2
stage4c_case_count: 0
coverage_before: C06 rows 17
coverage_after_if_accepted: C06 rows 22
need_to_30_after_if_accepted: 8
need_to_50_after_if_accepted: 28
loop_contribution_label: canonical_archetype_rule_candidate
```

This loop adds the missing distinction between "HBM customer-capacity rerating" and "generic memory recovery." It also adds the second distinction between "true HBM evidence" and "good entry." C06 can be right at the thesis level but wrong at the entry level when price has already pulled forward the customer-capacity bridge.

## 11. Evidence and price references

Evidence URLs:
- SK hynix FY2023 Q4 HBM/profit inflection: https://www.kedglobal.com/earnings/newsView/ked202401250004
- SK hynix Q1 2024 Reuters earnings/HBM recovery: https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/
- SK hynix HBM sold-out for 2024 / almost sold-out for 2025: https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-hbm-chips-almost-sold-out-2025-2024-05-02/
- SK hynix Q2 2024 Reuters earnings/HBM demand: https://www.reuters.com/technology/nvidia-supplier-sk-hynixs-q2-profit-soars-ai-boom-2024-07-24/
- Samsung HBM Nvidia test issue: https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/
- Samsung Q2 2024 earnings guidance: https://news.samsung.com/global/samsung-electronics-announces-earnings-guidance-for-second-quarter-2024
- Samsung Q2 2024 Reuters AI/HBM commentary: https://www.reuters.com/technology/samsung-q2-profit-up-more-than-15-fold-chip-prices-rise-2024-07-30/
- Samsung 8-layer HBM3E approval update: https://www.reuters.com/technology/artificial-intelligence/samsungs-8-layer-hbm3e-chips-clear-nvidias-tests-use-sources-say-2024-08-06/

Price URLs:
- atlas/manifest.json: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- 000660 profile: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/000/000660.json
- 005930 profile: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/005/005930.json
- 000660 2024 tradable shard: https://github.com/Daikisong/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv?plain=1
- 000660 2025 tradable shard: https://github.com/Daikisong/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/000/000660/2025.csv?plain=1
- 005930 2024 tradable shard: https://github.com/Daikisong/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv?plain=1
- 005930 2025 tradable shard: https://github.com/Daikisong/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/005/005930/2025.csv?plain=1

## 12. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session.

```text
You are the later stock_agent coding agent. Read this MD together with other accepted V12 research MDs. Do not treat the rule candidate as production-ready by itself. Batch-ingest the JSONL trigger rows, validate entry_date, entry_price, canonical trigger_type, full 30/90/180D MFE/MAE, duplicate keys, corporate-action windows, and URL evidence. If accepted, evaluate a shadow-only C06 rule seed named C06_CUSTOMER_QUALIFICATION_BOOKED_CAPACITY_GATE_V1. The intended behavior is to keep early SK hynix-like customer-capacity HBM positives eligible for Stage2-Actionable / Stage3-Yellow while blocking Samsung-like broad memory recovery or HBM ambition rows from Stage2-Actionable until named customer qualification, booked capacity, HBM mix/ASP/revision, or customer shipment evidence is present. Preserve global guardrails: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c. Do not loosen Stage3-Green.
```

## 13. Next research state

```yaml
completed_round: R2
completed_loop: 129
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
next_recommended_archetypes:
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
  - C11_BATTERY_ORDERBOOK_RERATING
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
