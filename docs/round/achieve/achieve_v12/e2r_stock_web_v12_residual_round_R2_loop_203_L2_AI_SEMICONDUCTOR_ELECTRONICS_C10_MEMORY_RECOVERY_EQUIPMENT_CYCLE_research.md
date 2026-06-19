# E2R v12 Stock-Web Residual Research — R2 / L2 / C10 Memory Recovery Equipment Cycle

```text
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 203
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4
output_file: e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection and novelty check

`V12_Research_No_Repeat_Index.md` is used only as the duplicate-prevention ledger. The current cumulative corpus is no longer a raw row-filling exercise: all C01~C32 canonical archetypes are above 80 representative rows, and C10 already has 210 representative rows but still shows weak 4C coverage and a persistent supplier-order conversion problem. Therefore this run selects C10 quality reinforcement rather than a sequential R1~R13 turn.

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This batch intentionally avoids the previous C10 rows already created in this session, including prior 240810 / 084370 / 095610 / 319660 / 036930 / 166090 / 031980 / 083450 / 281820 combinations. New symbols or new dates are used for every row in this file.

```text
new_independent_case_count: 9
new_independent_trigger_count: 9
unique_symbol_count: 7
stage2_count: 1
stage2_actionable_count: 6
stage3_yellow_count: 1
stage4b_count: 1
stage4c_count: 0
positive_or_reopen_case_count: 6
counterexample_or_guardrail_case_count: 3
source_proxy_only_count: 1
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 2. Stock-Web price source validation

```text
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema: d,o,h,l,c,v,a,mc,s,m
MFE/MAE basis: entry close versus max high / min low from entry row through N forward tradable rows
```

Manifest confirms raw/unadjusted marcap basis, `tradable_row_count=14,354,401`, `symbol_count=5,414`, and `max_date=2026-02-20`. The schema defines MFE/MAE as max high / min low from the entry date through the N-tradable-row window. All usable rows below have 30D/90D/180D MFE and MAE present.

Corporate-action profile check:

| symbol | profile latest name | corporate_action_candidate_dates | 180D contamination |
|---|---|---|---|
| 039030 | 이오테크닉스 | 2003-02-03 | false |
| 089030 | 테크윙 | 2011-12-13, 2011-12-29, 2022-08-01, 2022-08-23 | false |
| 322310 | 오로스테크놀로지 | none | false |
| 110990 | 디아이티 | none | false |
| 003160 | 디아이 | 1997-01-03, 1998-07-03, 1999-10-18 | false |
| 348210 | 넥스틴 | 2021-01-13, 2021-01-27 | false |
| 079370 | 제우스 | 2024-01-16, 2024-02-08 | false for 2025-04-07 entry |

## 3. Evidence summary

### C10 residual question

C10 is not asking whether the memory cycle recovered. It asks whether a Korean supplier has a credible route from customer memory capex / HBM demand into supplier-level order, shipment, revenue, margin, or customer qualification. The failure mode is like mistaking the weather report for rain in your own field: SK Hynix or Samsung capex language can be true, but not every tool maker receives water.

### Direct evidence set

- EO Technics 2023 positive bridge: Hana Securities described EO Technics as a Samsung HBM beneficiary and linked the move to Samsung DRAM exposure / OSAT grooving equipment revenue expansion.
- EO Technics 2024 overextension counterexample: Samsung's HBM supply expansion was real, but the 2024-04-30 EO row lacked a fresh EO-specific order conversion bridge.
- Techwing 2024: IR identified Memory Test Handler, Cube Prober for HBM test, global customers, and a roadmap into HBM test.
- Oros Technology 2024: Samsung customer diversification came with equipment supply contracts of KRW 2.1bn and KRW 8.0bn.
- DIT 2023 / 2025: TheElec reported DIT supplying laser annealing equipment to SK Hynix, then supplying additional kits for HBM3E production.
- DI Corp 2024: AlphaBiz reported HBM test-equipment localization exposure, Samsung supply on a standalone basis, and SK Hynix supply through subsidiary Digital Frontier.
- NexTin 2025: IR framed 2023-2024 as HBM/EUV/package-focused investment and 2025+ as new products / new major customers, but without a fresh order row.
- Zeus 2025: TheElec identified Zeus as supplier of TSV cleaners used in HBM production.

## 4. Trigger-level price path table

|   symbol | name            | trigger           | entry      |   close |   MFE30 |   MAE30 |   MFE90 |   MAE90 |   MFE180 |   MAE180 | peak180    | trough180   | role                                               |
|---------:|:----------------|:------------------|:-----------|--------:|--------:|--------:|--------:|--------:|---------:|---------:|:-----------|:------------|:---------------------------------------------------|
|   039030 | EO Technics     | Stage2-Actionable | 2023-08-16 |  157500 |   16.13 |  -16.76 |   16.13 |  -16.76 |    78.41 |   -16.76 | 2024-04-12 | 2023-09-22  | positive_direct_supplier_beta                      |
|   039030 | EO Technics     | Stage4B           | 2024-04-30 |  240500 |    4.99 |  -21.79 |    4.99 |  -46.2  |     4.99 |   -52.81 | 2024-05-09 | 2024-11-29  | proxy_theme_overextension_counterexample           |
|   089030 | Techwing        | Stage2-Actionable | 2024-04-19 |   35400 |   27.68 |  -13.84 |  100    |  -13.84 |   100    |   -20.2  | 2024-07-11 | 2024-12-11  | product_roadmap_positive_with_yellow_blocker       |
|   322310 | Oros Technology | Stage2-Actionable | 2024-01-24 |   34650 |   17.6  |  -22.94 |   17.6  |  -33.33 |    17.6  |   -56.33 | 2024-02-27 | 2024-09-09  | direct_customer_diversification_high_mae_guardrail |
|   110990 | DIT             | Stage3-Yellow     | 2023-08-10 |   10740 |   28.96 |   -7.45 |  126.72 |   -7.45 |   201.21 |    -7.45 | 2024-04-26 | 2023-08-16  | direct_supplier_order_positive_control             |
|   110990 | DIT             | Stage2-Actionable | 2025-01-15 |   14800 |   31.55 |   -4.73 |   31.55 |  -21.96 |    31.55 |   -25.2  | 2025-01-22 | 2025-08-22  | direct_reorder_reopen_with_high_mae_cap            |
|   003160 | DI Corp         | Stage2-Actionable | 2024-05-23 |   19800 |   55.56 |  -17.17 |   55.56 |  -44.9  |    55.56 |   -50.2  | 2024-06-27 | 2024-12-09  | hbm_tester_localization_high_mae_guardrail         |
|   348210 | NexTin          | Stage2            | 2025-02-17 |   55900 |   14.49 |  -13.51 |   14.49 |  -13.51 |    21.47 |   -27.1  | 2025-11-04 | 2025-09-02  | strategy_roadmap_not_yet_order_conversion          |
|   079370 | Zeus            | Stage2-Actionable | 2025-04-07 |   11850 |   23.12 |   -2.11 |   23.12 |   -2.53 |    44.81 |    -2.87 | 2025-10-14 | 2025-08-20  | hbm_tsv_cleaner_positive_control                   |

## 5. Raw component score simulation

Weights are interpreted through the C10 runtime profile shown in the current No-Repeat Index: `EPS/Vis/Bott/Mis/Val/Cap/Info = 22/18/14/12/10/5/19`. The component values below are shadow simulation points, not a production scoring change.

|   symbol | trigger           |   eps_fcf_explosion |   earnings_visibility |   bottleneck_pricing |   market_mispricing |   valuation_rerating |   capital_allocation |   information_confidence |   raw_total |   after_bonus | decision_note                                                                                                                   |
|---------:|:------------------|--------------------:|----------------------:|---------------------:|--------------------:|---------------------:|---------------------:|-------------------------:|------------:|--------------:|:--------------------------------------------------------------------------------------------------------------------------------|
|   039030 | Stage2-Actionable |                  14 |                    14 |                   11 |                   9 |                    6 |                    2 |                       15 |          71 |            73 | direct-enough supplier bridge preserves Stage2-Actionable; Green blocked until tool order/revenue and margin conversion repeat. |
|   039030 | Stage4B           |                   8 |                     8 |                    8 |                   6 |                    4 |                    1 |                        7 |          42 |            42 | macro HBM capacity language should be Stage4B/watch or capped Stage2, not Actionable/Yellow.                                    |
|   089030 | Stage2-Actionable |                  14 |                    15 |                   12 |                   9 |                    6 |                    2 |                       17 |          75 |            77 | Stage2-Actionable is preserved; Yellow/Green blocked because product launch/customer qualification was still developing.        |
|   322310 | Stage2-Actionable |                  12 |                    14 |                   11 |                   8 |                    5 |                    2 |                       15 |          67 |            69 | Direct contract gives Actionable, but 180D MAE -56.33% makes it a Green blocker and high-MAE cap case.                          |
|   110990 | Stage3-Yellow     |                  17 |                    17 |                   13 |                  10 |                    8 |                    2 |                       18 |          85 |            85 | Strong direct supply and low MAE allow Yellow; Green still blocked until reported revenue/margin/FCF confirmation.              |
|   110990 | Stage2-Actionable |                  13 |                    15 |                   12 |                   8 |                    5 |                    2 |                       17 |          72 |            74 | Reopen as Actionable, but 180D MAE -25.20% and immediate peak keep Yellow/Green blocked.                                        |
|   003160 | Stage2-Actionable |                  13 |                    14 |                   11 |                   8 |                    5 |                    2 |                       14 |          67 |            69 | Supplier route supports Actionable; 90D/180D MAE near -45%/-50% blocks Yellow/Green.                                            |
|   348210 | Stage2            |                   9 |                    10 |                    9 |                   6 |                    4 |                    2 |                       12 |          52 |            52 | Keep as Stage2 until order/shipment/revenue conversion appears.                                                                 |
|   079370 | Stage2-Actionable |                  13 |                    15 |                   12 |                   8 |                    6 |                    2 |                       15 |          71 |            73 | Actionable positive control with clean 180D path; Yellow still requires reported order/revenue/margin family.                   |

## 6. Case analysis

### 6.1 Direct supplier bridge that should reopen Stage2-Actionable

DIT 2023 is the cleanest positive control. The trigger row had direct SK Hynix laser-annealing supply, a quality-test passage, and a next-year mass-supply route. The 180D path delivered `MFE +201.21% / MAE -7.45%`. This is not generic memory beta. It is a supplier bridge with customer, tool type, and production route.

DIT 2025 is the same structural bridge after the first cycle. The evidence is a reorder / additional kit row, not merely customer capex mood. But the price path peaked quickly and then fell to `180D MAE -25.20%`, so the correct residual is Stage2-Actionable reopen plus Green blocker, not full Green.

Techwing, DI Corp, and Zeus are all supplier-route cases, but they differ in quality. Techwing has a company IR bridge into HBM Cube Prober and memory handler leadership; DI Corp has HBM tester localization and named Samsung/SK Hynix supply channels; Zeus has TSV cleaner exposure used in HBM production. These support Actionable, but not automatic Yellow/Green unless order/revenue/margin conversion is separately confirmed.

### 6.2 Direct customer diversification can still be high-MAE

Oros Technology is useful precisely because the evidence was not empty: Samsung equipment contracts were present. Yet the 180D path was `MFE +17.60% / MAE -56.33%`. The residual is not to delete Stage2-Actionable. The residual is to keep a high-MAE cap on Yellow/Green when a single customer-addition row lacks durable revenue / margin follow-through.

### 6.3 Product roadmap is Stage2, not Actionable, until conversion appears

NexTin's 2025 IR has a useful strategic signal: HBM/EUV/package investment focus and 2025+ new products / major customers. But the row is closer to a roadmap than a dated order or shipment. It remains Stage2, with Actionable held back until a second bridge appears.

### 6.4 Macro HBM customer capex is not supplier conversion

EO Technics 2024 is the counterexample. Samsung's HBM supply expansion was real, and EO had a plausible Samsung / laser / HBM narrative. But the entry window sat close to a crowded HBM-expectation area and then produced `180D MFE +4.99% / MAE -52.81%`. That is a Stage4B/watch row, not an Actionable row.

## 7. Residual contribution summary

```text
canonical_rule_candidate:
C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_GATE_V4

sector_rule_candidate:
L2_MEMORY_EQUIPMENT_CUSTOMER_CAPEX_TO_SUPPLIER_CONVERSION_GATE_V4

core residual:
- customer-level memory recovery / Samsung-SK Hynix HBM capex headline alone is not enough for Stage2-Actionable.
- Stage2-Actionable requires at least one supplier-level second bridge:
  order, shipment, customer qualification, named customer route, tool-specific adoption,
  revenue conversion, margin conversion, or repeat reorder.
- A direct supplier bridge can reopen Stage2-Actionable after a weak memory-equipment year.
- High MAE on a valid direct-bridge row blocks Yellow/Green first; it does not delete Stage2-Actionable.
- Product roadmap / strategy deck language remains Stage2 until order or shipment conversion appears.
- Macro customer HBM supply expansion without issuer-level conversion routes to Stage4B/watch or capped Stage2.
- Hard 4C still requires non-price thesis break: order cancellation, capex pushout hitting supplier revenue,
  customer loss, margin break, inventory/backlog failure, or accounting trust break.
```

## 8. Shadow weight note

```text
production_scoring_changed: false
shadow_weight_only: true
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- high_mae_green_blocker
- supplier_order_conversion_gate

new_axis_proposed:
- supplier_order_reopen_clock

do_not_apply_as_global_rule: true
scope_limit:
- large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
- canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

Suggested shadow behavior, not production patch:

```text
before:
C10 could over-credit customer memory capex / HBM macro as supplier conversion.

after:
C10 splits evidence into three lanes:
1. named supplier order / shipment / customer qualification / reorder -> Stage2-Actionable, possible Yellow only if MAE and realized conversion quality are acceptable
2. strategy deck / product roadmap / major-customer plan -> Stage2 cap
3. customer-level HBM capex or macro memory recovery without issuer conversion -> Stage4B/watch or capped Stage2
```

## 9. Machine-readable JSONL trigger rows

```jsonl
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-001","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"039030","company_name":"EO Technics","trigger_type":"Stage2-Actionable","evidence_date":"2023-08-16","entry_date":"2023-08-16","entry_price":157500,"entry_open":155000,"entry_high":162100,"entry_low":154100,"entry_close":157500,"entry_volume":442477,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv","atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv","atlas/ohlcv_tradable_by_symbol_year/039/039030/2025.csv","atlas/ohlcv_tradable_by_symbol_year/039/039030/2026.csv"],"profile_path":"atlas/symbol_profiles/039/039030.json","profile_corporate_action_candidate_dates":["2003-02-03"],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"positive_direct_supplier_beta","evidence_family":"broker_direct_hbm_supplier_exposure","evidence_url":"https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2023/08/15/Eotechnics_0816.pdf","source_proxy_only":false,"evidence_url_pending":false,"mfe_30d_pct":16.13,"mae_30d_pct":-16.76,"mfe_90d_pct":16.13,"mae_90d_pct":-16.76,"mfe_180d_pct":78.41,"mae_180d_pct":-16.76,"peak_180d_date":"2024-04-12","trough_180d_date":"2023-09-22","raw_component_score_breakdown":{"eps_fcf_explosion":14,"earnings_visibility":14,"bottleneck_pricing":11,"market_mispricing":9,"valuation_rerating":6,"capital_allocation":2,"information_confidence":15},"raw_total_score":71,"stage2_actionable_bonus_applied":2.0,"simulated_total_after_actionable_bonus":73.0,"current_profile_error":"too_late_if_direct_supplier_bridge_ignored","decision_note":"direct-enough supplier bridge preserves Stage2-Actionable; Green blocked until tool order/revenue and margin conversion repeat.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-002","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"039030","company_name":"EO Technics","trigger_type":"Stage4B","evidence_date":"2024-04-30","entry_date":"2024-04-30","entry_price":240500,"entry_open":246000,"entry_high":249000,"entry_low":239500,"entry_close":240500,"entry_volume":82886,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv","atlas/ohlcv_tradable_by_symbol_year/039/039030/2025.csv","atlas/ohlcv_tradable_by_symbol_year/039/039030/2026.csv"],"profile_path":"atlas/symbol_profiles/039/039030.json","profile_corporate_action_candidate_dates":["2003-02-03"],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"proxy_theme_overextension_counterexample","evidence_family":"customer_hbm_supply_macro_without_supplier_order","evidence_url":"https://www.koreatimes.co.kr/business/tech-science/20240430/samsung-vows-to-triple-ai-memory-chip-supply-in-2024","source_proxy_only":true,"evidence_url_pending":false,"mfe_30d_pct":4.99,"mae_30d_pct":-21.79,"mfe_90d_pct":4.99,"mae_90d_pct":-46.2,"mfe_180d_pct":4.99,"mae_180d_pct":-52.81,"peak_180d_date":"2024-05-09","trough_180d_date":"2024-11-29","raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":8,"bottleneck_pricing":8,"market_mispricing":6,"valuation_rerating":4,"capital_allocation":1,"information_confidence":7},"raw_total_score":42,"stage2_actionable_bonus_applied":0.0,"simulated_total_after_actionable_bonus":42.0,"current_profile_error":"false_positive_if_macro_customer_capex_is_counted_as_supplier_order","decision_note":"macro HBM capacity language should be Stage4B/watch or capped Stage2, not Actionable/Yellow.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-003","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"089030","company_name":"Techwing","trigger_type":"Stage2-Actionable","evidence_date":"2024-04-19","entry_date":"2024-04-19","entry_price":35400,"entry_open":37100,"entry_high":37650,"entry_low":32400,"entry_close":35400,"entry_volume":1944619,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","atlas/ohlcv_tradable_by_symbol_year/089/089030/2025.csv","atlas/ohlcv_tradable_by_symbol_year/089/089030/2026.csv"],"profile_path":"atlas/symbol_profiles/089/089030.json","profile_corporate_action_candidate_dates":["2011-12-13","2011-12-29","2022-08-01","2022-08-23"],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"product_roadmap_positive_with_yellow_blocker","evidence_family":"company_ir_memory_handler_hbm_cube_prober","evidence_url":"https://files-scs.pstatic.net/2024/04/19/9LYZO70lKM/%ED%85%8C%ED%81%AC%EC%9C%99%2024%EB%85%844%EC%9B%94%20IR%EC%9E%90%EB%A3%8C.pdf","source_proxy_only":false,"evidence_url_pending":false,"mfe_30d_pct":27.68,"mae_30d_pct":-13.84,"mfe_90d_pct":100.0,"mae_90d_pct":-13.84,"mfe_180d_pct":100.0,"mae_180d_pct":-20.2,"peak_180d_date":"2024-07-11","trough_180d_date":"2024-12-11","raw_component_score_breakdown":{"eps_fcf_explosion":14,"earnings_visibility":15,"bottleneck_pricing":12,"market_mispricing":9,"valuation_rerating":6,"capital_allocation":2,"information_confidence":17},"raw_total_score":75,"stage2_actionable_bonus_applied":2.0,"simulated_total_after_actionable_bonus":77.0,"current_profile_error":"too_late_if_hbm_test_tool_bridge_is_not_allowed_actionable","decision_note":"Stage2-Actionable is preserved; Yellow/Green blocked because product launch/customer qualification was still developing.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-004","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"322310","company_name":"Oros Technology","trigger_type":"Stage2-Actionable","evidence_date":"2024-01-24","entry_date":"2024-01-24","entry_price":34650,"entry_open":31050,"entry_high":36600,"entry_low":30800,"entry_close":34650,"entry_volume":4400841,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","atlas/ohlcv_tradable_by_symbol_year/322/322310/2025.csv","atlas/ohlcv_tradable_by_symbol_year/322/322310/2026.csv"],"profile_path":"atlas/symbol_profiles/322/322310.json","profile_corporate_action_candidate_dates":[],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"direct_customer_diversification_high_mae_guardrail","evidence_family":"samsung_equipment_contract_overlay_measurement","evidence_url":"https://www.asiae.co.kr/en/article/2024012410011091331","source_proxy_only":false,"evidence_url_pending":false,"mfe_30d_pct":17.6,"mae_30d_pct":-22.94,"mfe_90d_pct":17.6,"mae_90d_pct":-33.33,"mfe_180d_pct":17.6,"mae_180d_pct":-56.33,"peak_180d_date":"2024-02-27","trough_180d_date":"2024-09-09","raw_component_score_breakdown":{"eps_fcf_explosion":12,"earnings_visibility":14,"bottleneck_pricing":11,"market_mispricing":8,"valuation_rerating":5,"capital_allocation":2,"information_confidence":15},"raw_total_score":67,"stage2_actionable_bonus_applied":2.0,"simulated_total_after_actionable_bonus":69.0,"current_profile_error":"green_overfit_if_customer_contract_ignores_high_mae_and_followthrough","decision_note":"Direct contract gives Actionable, but 180D MAE -56.33% makes it a Green blocker and high-MAE cap case.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-005","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"110990","company_name":"DIT","trigger_type":"Stage3-Yellow","evidence_date":"2023-08-10","entry_date":"2023-08-10","entry_price":10740,"entry_open":11120,"entry_high":11220,"entry_low":10420,"entry_close":10740,"entry_volume":332064,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/110/110990/2023.csv","atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv","atlas/ohlcv_tradable_by_symbol_year/110/110990/2025.csv","atlas/ohlcv_tradable_by_symbol_year/110/110990/2026.csv"],"profile_path":"atlas/symbol_profiles/110/110990.json","profile_corporate_action_candidate_dates":[],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"direct_supplier_order_positive_control","evidence_family":"sk_hynix_laser_annealing_direct_supply","evidence_url":"https://www.thelec.net/news/articleView.html?idxno=4615","source_proxy_only":false,"evidence_url_pending":false,"mfe_30d_pct":28.96,"mae_30d_pct":-7.45,"mfe_90d_pct":126.72,"mae_90d_pct":-7.45,"mfe_180d_pct":201.21,"mae_180d_pct":-7.45,"peak_180d_date":"2024-04-26","trough_180d_date":"2023-08-16","raw_component_score_breakdown":{"eps_fcf_explosion":17,"earnings_visibility":17,"bottleneck_pricing":13,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":2,"information_confidence":18},"raw_total_score":85,"stage2_actionable_bonus_applied":0.0,"simulated_total_after_actionable_bonus":85.0,"current_profile_error":"too_late_if_direct_sk_hynix_supply_is_capped_to_plain_stage2","decision_note":"Strong direct supply and low MAE allow Yellow; Green still blocked until reported revenue/margin/FCF confirmation.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-006","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"110990","company_name":"DIT","trigger_type":"Stage2-Actionable","evidence_date":"2025-01-15","entry_date":"2025-01-15","entry_price":14800,"entry_open":14500,"entry_high":14960,"entry_low":14500,"entry_close":14800,"entry_volume":116664,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/110/110990/2025.csv","atlas/ohlcv_tradable_by_symbol_year/110/110990/2026.csv"],"profile_path":"atlas/symbol_profiles/110/110990.json","profile_corporate_action_candidate_dates":[],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"direct_reorder_reopen_with_high_mae_cap","evidence_family":"additional_sk_hynix_laser_annealing_kits","evidence_url":"https://www.thelec.net/news/articleView.html?idxno=5112","source_proxy_only":false,"evidence_url_pending":false,"mfe_30d_pct":31.55,"mae_30d_pct":-4.73,"mfe_90d_pct":31.55,"mae_90d_pct":-21.96,"mfe_180d_pct":31.55,"mae_180d_pct":-25.2,"peak_180d_date":"2025-01-22","trough_180d_date":"2025-08-22","raw_component_score_breakdown":{"eps_fcf_explosion":13,"earnings_visibility":15,"bottleneck_pricing":12,"market_mispricing":8,"valuation_rerating":5,"capital_allocation":2,"information_confidence":17},"raw_total_score":72,"stage2_actionable_bonus_applied":2.0,"simulated_total_after_actionable_bonus":74.0,"current_profile_error":"overhard_4b_if_reorder_is_ignored_but_green_too_loose_if_immediate_peak_is_ignored","decision_note":"Reopen as Actionable, but 180D MAE -25.20% and immediate peak keep Yellow/Green blocked.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-007","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"003160","company_name":"DI Corp","trigger_type":"Stage2-Actionable","evidence_date":"2024-05-23","entry_date":"2024-05-23","entry_price":19800,"entry_open":20800,"entry_high":21200,"entry_low":19350,"entry_close":19800,"entry_volume":2410649,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv","atlas/ohlcv_tradable_by_symbol_year/003/003160/2025.csv","atlas/ohlcv_tradable_by_symbol_year/003/003160/2026.csv"],"profile_path":"atlas/symbol_profiles/003/003160.json","profile_corporate_action_candidate_dates":["1997-01-03","1998-07-03","1999-10-18"],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"hbm_tester_localization_high_mae_guardrail","evidence_family":"hbm_test_equipment_localization_supplier_route","evidence_url":"https://alphabiz.co.kr/news/view/1065581016884096","source_proxy_only":false,"evidence_url_pending":false,"mfe_30d_pct":55.56,"mae_30d_pct":-17.17,"mfe_90d_pct":55.56,"mae_90d_pct":-44.9,"mfe_180d_pct":55.56,"mae_180d_pct":-50.2,"peak_180d_date":"2024-06-27","trough_180d_date":"2024-12-09","raw_component_score_breakdown":{"eps_fcf_explosion":13,"earnings_visibility":14,"bottleneck_pricing":11,"market_mispricing":8,"valuation_rerating":5,"capital_allocation":2,"information_confidence":14},"raw_total_score":67,"stage2_actionable_bonus_applied":2.0,"simulated_total_after_actionable_bonus":69.0,"current_profile_error":"green_overfit_if_hbm_localization_ignores_extreme_forward_mae","decision_note":"Supplier route supports Actionable; 90D/180D MAE near -45%/-50% blocks Yellow/Green.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-008","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"348210","company_name":"NexTin","trigger_type":"Stage2","evidence_date":"2025-02-17","entry_date":"2025-02-17","entry_price":55900,"entry_open":56700,"entry_high":56900,"entry_low":55400,"entry_close":55900,"entry_volume":38192,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/348/348210/2025.csv","atlas/ohlcv_tradable_by_symbol_year/348/348210/2026.csv"],"profile_path":"atlas/symbol_profiles/348/348210.json","profile_corporate_action_candidate_dates":["2021-01-13","2021-01-27"],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"strategy_roadmap_not_yet_order_conversion","evidence_family":"inspection_market_strategy_new_customers","evidence_url":"https://file.alphasquare.co.kr/media/pdfs/company-ir/20250217%EB%84%A5%EC%8A%A4%ED%8B%B4_2025_Citi_Korea_Corporate_Day_%EC%B0%B8%EC%97%AC.pdf","source_proxy_only":false,"evidence_url_pending":false,"mfe_30d_pct":14.49,"mae_30d_pct":-13.51,"mfe_90d_pct":14.49,"mae_90d_pct":-13.51,"mfe_180d_pct":21.47,"mae_180d_pct":-27.1,"peak_180d_date":"2025-11-04","trough_180d_date":"2025-09-02","raw_component_score_breakdown":{"eps_fcf_explosion":9,"earnings_visibility":10,"bottleneck_pricing":9,"market_mispricing":6,"valuation_rerating":4,"capital_allocation":2,"information_confidence":12},"raw_total_score":52,"stage2_actionable_bonus_applied":0.0,"simulated_total_after_actionable_bonus":52.0,"current_profile_error":"false_actionable_if_strategy_deck_is_treated_as_order_conversion","decision_note":"Keep as Stage2 until order/shipment/revenue conversion appears.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_id":"e2r_stock_web_v12_residual_round_R2_loop_203_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","case_id":"C10-203-009","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","selected_round":"R2","selected_loop":203,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_REPAIR_V4","symbol":"079370","company_name":"Zeus","trigger_type":"Stage2-Actionable","evidence_date":"2025-04-07","entry_date":"2025-04-07","entry_price":11850,"entry_open":12270,"entry_high":12320,"entry_low":11850,"entry_close":11850,"entry_volume":250666,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_shards_used":["atlas/ohlcv_tradable_by_symbol_year/079/079370/2025.csv","atlas/ohlcv_tradable_by_symbol_year/079/079370/2026.csv"],"profile_path":"atlas/symbol_profiles/079/079370.json","profile_corporate_action_candidate_dates":["2024-01-16","2024-02-08"],"window_180D_corporate_action_contaminated":false,"insufficient_forward_window_180D":false,"calibration_usable":true,"case_role":"hbm_tsv_cleaner_positive_control","evidence_family":"hbm_tsv_cleaner_supplier_bridge","evidence_url":"https://www.thelec.net/news/articleView.html?idxno=5216","source_proxy_only":false,"evidence_url_pending":false,"mfe_30d_pct":23.12,"mae_30d_pct":-2.11,"mfe_90d_pct":23.12,"mae_90d_pct":-2.53,"mfe_180d_pct":44.81,"mae_180d_pct":-2.87,"peak_180d_date":"2025-10-14","trough_180d_date":"2025-08-20","raw_component_score_breakdown":{"eps_fcf_explosion":13,"earnings_visibility":15,"bottleneck_pricing":12,"market_mispricing":8,"valuation_rerating":6,"capital_allocation":2,"information_confidence":15},"raw_total_score":71,"stage2_actionable_bonus_applied":2.0,"simulated_total_after_actionable_bonus":73.0,"current_profile_error":"too_late_if_back_end_hbm_cleaning_tool_is_not_counted_as_supplier_bridge","decision_note":"Actionable positive control with clean 180D path; Yellow still requires reported order/revenue/margin family.","production_scoring_changed":false,"shadow_weight_only":true}
```

## 10. Batch Ingest Self-Audit

```text
required_filename_regex_match: true
filename_round_matches_metadata_round: true
filename_loop_matches_metadata_loop: true
selected_round: R2
selected_loop: 203
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_sector_consistency: pass
stock_agent_code_accessed: false
stock_agent_code_patched: false
live_scan_performed: false
current_stock_recommendation_generated: false
price_route_hunt_performed: false
stock_web_manifest_checked: true
stock_web_schema_checked: true
stock_web_actual_ohlcv_rows_used: true
entry_price_present_for_all_usable_rows: true
mfe_mae_30_90_180_present_for_all_usable_rows: true
corporate_action_window_checked: true
same_entry_deduped: true
hard_duplicate_keys_reused: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

When batch-applying v12 residual calibration MDs, parse this file as a C10-specific supplier-order conversion repair candidate.
Treat it as shadow evidence only unless enough other C10 files confirm the same axis.
Do not loosen Stage3-Green globally.
Consider a scoped rule candidate:
C10_SUPPLIER_ORDER_DIRECT_BRIDGE_AND_GREEN_BLOCKER_GATE_V4

Candidate behavior:
- customer-level HBM or memory capex headline alone: cap at Stage2 or Stage4B/watch
- supplier-level named order / shipment / customer qualification / repeat reorder: allow Stage2-Actionable
- product roadmap without dated order/shipment: Stage2 cap
- high MAE direct-bridge winner: preserve Stage2-Actionable, block Yellow/Green
- hard 4C requires direct non-price thesis break, not only price drawdown
```

## 12. Next Research State

```text
completed_round: R2
completed_loop: 203
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 quality reinforcement / C10 supplier-order direct URL repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
