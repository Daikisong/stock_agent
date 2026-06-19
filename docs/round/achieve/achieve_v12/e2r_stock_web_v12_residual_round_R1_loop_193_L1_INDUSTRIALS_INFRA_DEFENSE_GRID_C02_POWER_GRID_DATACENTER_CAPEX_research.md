# E2R Stock-Web V12 Residual Research — R1 / L1 / C02

```yaml
research_mode: post_calibrated_residual_historical_research_v12
selected_round: R1
selected_loop: 193
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_family: GRID_DATACENTER_POWER_EQUIPMENT_ORDER_BACKLOG_TO_MARGIN_GATE
output_filename: e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
main_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
created_at_kst: 2026-06-16
```

## 1. Execution Scope

This run follows the v12 Stock-Web residual research workflow: no `stock_agent` code patch, no live discovery, no current recommendation, and no production scoring change. The only output is this standalone calibration MD with machine-readable trigger rows. The No-Repeat Index is used only as a duplicate and coverage ledger.

Selected axis: `C02_POWER_GRID_DATACENTER_CAPEX`. The current No-Repeat ledger shows C02 as already high-row but with a notable 4B/4C imbalance (`4B=50`, `4C=0`), so this run focuses on the quality distinction between company-specific backlog/margin positives, late price-extension 4B, and cases that should **not** be forced into hard 4C merely because of drawdown.

## 2. Atlas / Price Validation

| Item | Value |
|---|---|
| stock_web_manifest_max_date | 2026-02-20 |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| tradable schema | `d,o,h,l,c,v,a,mc,s,m` |
| price basis | `tradable_raw` |
| adjustment status | `raw_unadjusted_marcap` |
| MFE/MAE definition | max high / min low from entry row through N tradable rows, divided by entry close |
| corporate-action contaminated 180D rows | 0 |
| insufficient 180D forward-window rows | 0 |

## 3. Batch Novelty / Duplicate Check

Hard duplicate key: `canonical_archetype_id + symbol + trigger_type + entry_date`.

| Metric | Count |
|---|---:|
| new_independent_trigger_count | 7 |
| unique_symbol_count | 5 |
| reused_symbol_new_trigger_family_count | 2 |
| calibration_usable_trigger_count | 7 |
| positive_or_missed_positive_case_count | 4 |
| high_MAE_or_4B_guardrail_case_count | 3 |
| hard_4C_case_count | 0 |
| source_proxy_only_count | 0 |
| evidence_url_pending_count | 0 |
| missing_required_mfe_mae_count | 0 |
| production_scoring_changed | 0 |

## 4. Trigger Summary

| # | Symbol | Company | Trigger | Entry | Entry Close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Peak 180D | Trough 180D | Role |
|---:|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 267260 | HD Hyundai Electric | Stage2-Actionable | 2024-04-24 | 255,000 | 23.14/-10.20 | 46.86/-10.20 | 71.18/-11.57 | 2025-01-20 | 2024-09-09 | positive_order_backlog_margin_bridge |
| 2 | 010120 | LS ELECTRIC | 4B | 2024-07-25 | 215,500 | 19.26/-38.33 | 19.26/-41.44 | 40.84/-41.44 | 2025-02-19 | 2024-09-09 | late_extension_high_mae_guardrail |
| 3 | 010120 | LS ELECTRIC | Stage2-Actionable | 2025-04-22 | 172,600 | 54.84/-0.41 | 93.51/-0.41 | 220.97/-0.41 | 2026-01-14 | 2025-04-22 | positive_direct_backlog_us_order_bridge |
| 4 | 298040 | Hyosung Heavy Industries | Stage2-Actionable | 2025-04-29 | 520,000 | 49.04/-6.35 | 160.77/-6.35 | 377.50/-6.35 | 2025-11-04 | 2025-04-29 | positive_visible_profit_uptrend |
| 5 | 103590 | Iljin Electric | Stage2-Actionable | 2024-11-15 | 24,650 | 15.42/-16.84 | 52.33/-16.84 | 80.12/-19.68 | 2025-07-29 | 2025-04-09 | positive_backlog_chart_bridge |
| 6 | 033100 | JeRyong Electric | Stage2-Actionable | 2024-05-29 | 73,900 | 35.05/-17.73 | 36.27/-41.54 | 36.27/-50.54 | 2024-07-11 | 2024-12-09 | high_mae_stage2_actionable_counterexample |
| 7 | 033100 | JeRyong Electric | 4B | 2024-12-03 | 41,100 | 45.99/-11.07 | 56.20/-35.64 | 56.20/-35.64 | 2025-01-23 | 2025-04-09 | hard_4c_holdout_competition_order_slowing |

## 5. Case Notes

### 1. 267260 HD Hyundai Electric — Stage2-Actionable / positive_order_backlog_margin_bridge

- fine_archetype_id: `GRID_DATACENTER_TRANSFORMER_BACKLOG_MARGIN_BRIDGE`
- evidence: HD Hyundai Electric — Another earnings surprise, Mirae Asset, 2024-04-24
- evidence_url: https://securities.miraeasset.com/bbs/download/2125932.pdf?attachmentId=2125932
- evidence_summary: 1Q24 revenue and operating profit beat, North America power transformer sales and backlog mix strong, new orders reached around 40% of full-year guidance, data-center and US electricity demand cited as demand drivers.
- actual_1D_OHLC_row: `d=2024-04-24, o=245000, h=257000, l=232500, c=255000, v=1352522, a=332222269500, mc=9192019425000, s=36047135, m=KOSPI`
- stock_web_shard: `atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv; atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv`
- price_result: 30D `23.14/-10.20`, 90D `46.86/-10.20`, 180D `71.18/-11.57`
- score_proxy_weighted_total: `79.85`
- residual_label: `company_specific_backlog_margin_bridge_positive`
- current_profile_error: `under_green_but_usable_stage2_actionable_positive`

### 2. 010120 LS ELECTRIC — 4B / late_extension_high_mae_guardrail

- fine_archetype_id: `GRID_DATACENTER_ELECTRIC_BUSINESS_PRICE_EXTENSION_4B`
- evidence: LS ELECTRIC 2Q24 Results
- evidence_url: https://www.ls-electric.com/ko/company/data/24_2Q_Results.pdf
- evidence_summary: 2Q24 official deck reports highest quarterly operating profit driven by US electric business, including SWGR and high-voltage transformer growth.
- actual_1D_OHLC_row: `d=2024-07-25, o=249500, h=257000, l=214500, c=215500, v=2303383, a=522520506500, mc=6465000000000, s=30000000, m=KOSPI`
- stock_web_shard: `atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2026.csv`
- price_result: 30D `19.26/-38.33`, 90D `19.26/-41.44`, 180D `40.84/-41.44`
- score_proxy_weighted_total: `67.18`
- residual_label: `price_extension_high_mae_4b_not_hard_4c`
- current_profile_error: `over_promotion_risk_without_extension_guard`

### 3. 010120 LS ELECTRIC — Stage2-Actionable / positive_direct_backlog_us_order_bridge

- fine_archetype_id: `GRID_DATACENTER_US_ORDER_BACKLOG_REACCELERATION`
- evidence: LS ELECTRIC 1Q25 Results
- evidence_url: https://www.ls-electric.com/ko/company/data/25_1Q_Results.pdf
- evidence_summary: 1Q25 deck shows strong HVTR/SWGR growth momentum, order backlog rising from KRW2.6tn in 1Q24 to KRW3.9tn in 1Q25, and US-origin new orders exceeding half of Q1 orders.
- actual_1D_OHLC_row: `d=2025-04-22, o=173700, h=179400, l=171900, c=172600, v=340505, a=59789951000, mc=5178000000000, s=30000000, m=KOSPI`
- stock_web_shard: `atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2026.csv`
- price_result: 30D `54.84/-0.41`, 90D `93.51/-0.41`, 180D `220.97/-0.41`
- score_proxy_weighted_total: `80.96`
- residual_label: `official_backlog_reacceleration_positive`
- current_profile_error: `missed_stage3_yellow_candidate`

### 4. 298040 Hyosung Heavy Industries — Stage2-Actionable / positive_visible_profit_uptrend

- fine_archetype_id: `GRID_DATACENTER_HIGH_VALUE_TRANSFORMER_BACKLOG_MARGIN_BRIDGE`
- evidence: Hyosung Heavy Industries — Visible profit uptrend, Mirae Asset, 2025-04-29
- evidence_url: https://securities.miraeasset.com/bbs/download/2135886.pdf?attachmentId=2135886
- evidence_summary: 1Q25 report shows revenue growth, operating profit uptrend, KRW10.4tn heavy-industries backlog, new orders above KRW2tn, high-value project revenue recognition, and improving overseas subsidiary margins.
- actual_1D_OHLC_row: `d=2025-04-29, o=492000, h=522000, l=487000, c=520000, v=92036, a=47150316250, mc=4848764960000, s=9324548, m=KOSPI`
- stock_web_shard: `atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv; atlas/ohlcv_tradable_by_symbol_year/298/298040/2026.csv`
- price_result: 30D `49.04/-6.35`, 90D `160.77/-6.35`, 180D `377.50/-6.35`
- score_proxy_weighted_total: `82.11`
- residual_label: `backlog_margin_revenue_recognition_positive`
- current_profile_error: `missed_structural_positive_candidate`

### 5. 103590 Iljin Electric — Stage2-Actionable / positive_backlog_chart_bridge

- fine_archetype_id: `GRID_DATACENTER_CABLE_HEAVY_ELECTRIC_BACKLOG_BRIDGE`
- evidence: Iljin Electric, Mirae Asset, 2024-11-15
- evidence_url: https://securities.miraeasset.com/bbs/download/2132362.pdf?attachmentId=2132362
- evidence_summary: Report includes quarterly order-backlog trends for power cables/systems and heavy electric, plus revenue and operating-margin bridge and capacity ramp-up plans.
- actual_1D_OHLC_row: `d=2024-11-15, o=25450, h=25550, l=24500, c=24650, v=828250, a=20599008600, mc=1175444863500, s=47685390, m=KOSPI`
- stock_web_shard: `atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv; atlas/ohlcv_tradable_by_symbol_year/103/103590/2025.csv`
- price_result: 30D `15.42/-16.84`, 90D `52.33/-16.84`, 180D `80.12/-19.68`
- score_proxy_weighted_total: `71.77`
- residual_label: `component_specific_backlog_positive`
- current_profile_error: `proper_stage2_actionable_positive`

### 6. 033100 JeRyong Electric — Stage2-Actionable / high_mae_stage2_actionable_counterexample

- fine_archetype_id: `GRID_DATACENTER_DISTRIBUTION_TRANSFORMER_EXPORT_HIGH_MAE`
- evidence: JeRyong Electric Q1 surge and US transformer shortage, The Bigdata, 2024-05-29
- evidence_url: https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23
- evidence_summary: Article cites Q1 sales and operating profit growth, export share of 94%, US transformer shortage, and KRW305.6bn order backlog equal to about 1.1 years of 2024 expected sales.
- actual_1D_OHLC_row: `d=2024-05-29, o=78100, h=78900, l=72500, c=73900, v=1114957, a=83659733800, mc=1187012025100, s=16062409, m=KOSDAQ`
- stock_web_shard: `atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv`
- price_result: 30D `35.05/-17.73`, 90D `36.27/-41.54`, 180D `36.27/-50.54`
- score_proxy_weighted_total: `65.88`
- residual_label: `strong_evidence_but_late_high_mae_guardrail`
- current_profile_error: `over_promotion_risk_due_to_valuation_and_peak_proximity`

### 7. 033100 JeRyong Electric — 4B / hard_4c_holdout_competition_order_slowing

- fine_archetype_id: `GRID_DATACENTER_TRANSFORMER_COMPETITION_SLOWING_4B_HOLDOUT`
- evidence: JeRyong Electric drawdown and US order competition risk, Daily Invest, 2024-12-03
- evidence_url: https://www.dailyinvest.kr/news/articleView.html?idxno=62181
- evidence_summary: Article discusses export share rising to 92% YTD 3Q24 and order backlog to be recognized until 3Q25, while also flagging possible order-flow slowing and intensifying US competition.
- actual_1D_OHLC_row: `d=2024-12-03, o=39350, h=41150, l=39250, c=41100, v=305716, a=12388907600, mc=660165009900, s=16062409, m=KOSDAQ`
- stock_web_shard: `atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv`
- price_result: 30D `45.99/-11.07`, 90D `56.20/-35.64`, 180D `56.20/-35.64`
- score_proxy_weighted_total: `55.27`
- residual_label: `local_4b_not_hard_4c_despite_order_slowing_language`
- current_profile_error: `avoid_hard_4c_without_cancellation_or_margin_break`

## 6. Raw Component Breakdown

Weights used for this C02 simulation proxy: `eps_fcf_explosion=21`, `earnings_visibility=24`, `bottleneck_pricing=20`, `market_mispricing=13`, `valuation_rerating=12`, `capital_allocation=5`, `information_confidence=5`. These are shadow research inputs only, not production changes.

| Case | EPS/FCF | Visibility | Bottleneck/Pricing | Mispricing | Valuation | Capital | Info | Weighted total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C02_R1L193_267260_20240424_STAGE2A | 84 | 86 | 89 | 70 | 66 | 50 | 85 | 79.85 |
| C02_R1L193_010120_20240725_4B | 79 | 82 | 85 | 32 | 30 | 45 | 78 | 67.18 |
| C02_R1L193_010120_20250422_STAGE2A | 82 | 88 | 86 | 76 | 72 | 52 | 86 | 80.96 |
| C02_R1L193_298040_20250429_STAGE2A | 87 | 88 | 86 | 78 | 74 | 48 | 82 | 82.11 |
| C02_R1L193_103590_20241115_STAGE2A | 76 | 80 | 78 | 65 | 58 | 40 | 72 | 71.77 |
| C02_R1L193_033100_20240529_STAGE2A_HMAE | 82 | 85 | 82 | 25 | 28 | 35 | 70 | 65.88 |
| C02_R1L193_033100_20241203_4B_HOLDOUT | 65 | 68 | 60 | 35 | 30 | 35 | 68 | 55.27 |

## 7. Residual Interpretation

C02 behaves like a transformer under load: the macro current is real, but the signal only becomes useful when it passes through company-specific copper — direct backlog, order conversion, lead-time/pricing, regional mix, and margin recognition. Generic data-center or US grid language is a live wire, not yet a calibrated circuit.

Observed residuals:

- **Positive bridge:** HD Hyundai Electric, LS ELECTRIC 1Q25, Hyosung Heavy Industries, and Iljin Electric show that quantified order backlog, North America demand, high-value transformer/cable exposure, and margin recognition can justify `Stage2-Actionable` and sometimes a missed `Stage3-Yellow` candidate.
- **Late extension guard:** LS ELECTRIC 2Q24 and JeRyong Electric May 2024 show strong evidence but severe 90D/180D MAE after price extension. The rule should not convert good evidence into Green when the market has already capitalized the shortage narrative.
- **Hard 4C restraint:** JeRyong Electric December 2024 shows competition/order-flow concern but also remaining backlog and later upside. C02 should not route to hard 4C without direct cancellation, backlog collapse, margin break, or capacity/customer thesis failure.

## 8. Shadow Rule Candidate

```text
canonical_rule_candidate: C02_GRID_BACKLOG_MARGIN_EXTENSION_GATE
sector_rule_candidate: L1_POWER_GRID_DATACENTER_ORDER_TO_REVENUE_GATE
production_scoring_changed: false
shadow_weight_only: true

rule:
  Stage2-Actionable requires at least one company-specific bridge:
    - quantified order backlog / new orders,
    - North America / data-center / grid customer mix tied to company revenue,
    - transformer/cable capacity or lead-time evidence,
    - margin recognition or ASP/pricing bridge.
  Stage3-Yellow candidate requires at least two bridges plus actual margin or backlog-to-revenue conversion.
  Green remains blocked when evidence is only macro shortage / data-center demand / peer valuation rerating.
  Local 4B watch is preferred when the stock is already at/near evidence-window peak or 90D MAE exceeds -30%.
  Hard 4C requires non-price evidence of cancellation, backlog collapse, pricing/margin break, or customer/capacity thesis failure.
```

### Shadow weight delta candidate

| Scope | Before | After candidate | Rationale |
|---|---|---|---|
| `C02_POWER_GRID_DATACENTER_CAPEX` | `21/24/20/13/12/5/5` | `21/25/21/13/10/5/5` | Shift small weight from valuation rerating into earnings visibility and bottleneck/pricing when company-specific backlog and margin bridge are present. |

This is a shadow-only calibration candidate. It does not change active production scoring.

## 9. Machine-Readable JSONL

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":193,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_TRANSFORMER_BACKLOG_MARGIN_BRIDGE","case_id":"C02_R1L193_267260_20240424_STAGE2A","symbol":"267260","company_name":"HD Hyundai Electric","trigger_type":"Stage2-Actionable","case_role":"positive_order_backlog_margin_bridge","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":255000.0,"actual_1d_ohlc_row":{"d":"2024-04-24","o":245000.0,"h":257000.0,"l":232500.0,"c":255000.0,"v":1352522,"a":332222269500.0,"mc":9192019425000.0,"s":36047135,"m":"KOSPI"},"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv; atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv","mfe_30d_pct":23.14,"mae_30d_pct":-10.2,"peak_30d_date":"2024-05-27","trough_30d_date":"2024-05-03","mfe_90d_pct":46.86,"mae_90d_pct":-10.2,"peak_90d_date":"2024-07-24","trough_90d_date":"2024-05-03","mfe_180d_pct":71.18,"mae_180d_pct":-11.57,"peak_180d_date":"2025-01-20","trough_180d_date":"2024-09-09","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"evidence_title":"HD Hyundai Electric — Another earnings surprise, Mirae Asset, 2024-04-24","evidence_url":"https://securities.miraeasset.com/bbs/download/2125932.pdf?attachmentId=2125932","evidence_quality":"analyst_report_direct_url_company_data","evidence_summary":"1Q24 revenue and operating profit beat, North America power transformer sales and backlog mix strong, new orders reached around 40% of full-year guidance, data-center and US electricity demand cited as demand drivers.","component_scores":{"eps_fcf_explosion":84,"earnings_visibility":86,"bottleneck_pricing":89,"market_mispricing":70,"valuation_rerating":66,"capital_allocation":50,"information_confidence":85},"component_weights":{"eps_fcf_explosion":21,"earnings_visibility":24,"bottleneck_pricing":20,"market_mispricing":13,"valuation_rerating":12,"capital_allocation":5,"information_confidence":5},"weighted_total_proxy":79.85,"current_profile_error":"under_green_but_usable_stage2_actionable_positive","residual_label":"company_specific_backlog_margin_bridge_positive","source_proxy_only":false,"evidence_url_pending":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":193,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_ELECTRIC_BUSINESS_PRICE_EXTENSION_4B","case_id":"C02_R1L193_010120_20240725_4B","symbol":"010120","company_name":"LS ELECTRIC","trigger_type":"4B","case_role":"late_extension_high_mae_guardrail","trigger_date":"2024-07-25","entry_date":"2024-07-25","entry_price":215500.0,"actual_1d_ohlc_row":{"d":"2024-07-25","o":249500.0,"h":257000.0,"l":214500.0,"c":215500.0,"v":2303383,"a":522520506500.0,"mc":6465000000000.0,"s":30000000,"m":"KOSPI"},"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2026.csv","mfe_30d_pct":19.26,"mae_30d_pct":-38.33,"peak_30d_date":"2024-07-25","trough_30d_date":"2024-09-05","mfe_90d_pct":19.26,"mae_90d_pct":-41.44,"peak_90d_date":"2024-07-25","trough_90d_date":"2024-09-09","mfe_180d_pct":40.84,"mae_180d_pct":-41.44,"peak_180d_date":"2025-02-19","trough_180d_date":"2024-09-09","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"evidence_title":"LS ELECTRIC 2Q24 Results","evidence_url":"https://www.ls-electric.com/ko/company/data/24_2Q_Results.pdf","evidence_quality":"company_official_results_pdf","evidence_summary":"2Q24 official deck reports highest quarterly operating profit driven by US electric business, including SWGR and high-voltage transformer growth.","component_scores":{"eps_fcf_explosion":79,"earnings_visibility":82,"bottleneck_pricing":85,"market_mispricing":32,"valuation_rerating":30,"capital_allocation":45,"information_confidence":78},"component_weights":{"eps_fcf_explosion":21,"earnings_visibility":24,"bottleneck_pricing":20,"market_mispricing":13,"valuation_rerating":12,"capital_allocation":5,"information_confidence":5},"weighted_total_proxy":67.18,"current_profile_error":"over_promotion_risk_without_extension_guard","residual_label":"price_extension_high_mae_4b_not_hard_4c","source_proxy_only":false,"evidence_url_pending":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":193,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_US_ORDER_BACKLOG_REACCELERATION","case_id":"C02_R1L193_010120_20250422_STAGE2A","symbol":"010120","company_name":"LS ELECTRIC","trigger_type":"Stage2-Actionable","case_role":"positive_direct_backlog_us_order_bridge","trigger_date":"2025-04-22","entry_date":"2025-04-22","entry_price":172600.0,"actual_1d_ohlc_row":{"d":"2025-04-22","o":173700.0,"h":179400.0,"l":171900.0,"c":172600.0,"v":340505,"a":59789951000.0,"mc":5178000000000.0,"s":30000000,"m":"KOSPI"},"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2026.csv","mfe_30d_pct":54.84,"mae_30d_pct":-0.41,"peak_30d_date":"2025-06-09","trough_30d_date":"2025-04-22","mfe_90d_pct":93.51,"mae_90d_pct":-0.41,"peak_90d_date":"2025-08-05","trough_90d_date":"2025-04-22","mfe_180d_pct":220.97,"mae_180d_pct":-0.41,"peak_180d_date":"2026-01-14","trough_180d_date":"2025-04-22","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"evidence_title":"LS ELECTRIC 1Q25 Results","evidence_url":"https://www.ls-electric.com/ko/company/data/25_1Q_Results.pdf","evidence_quality":"company_official_results_pdf","evidence_summary":"1Q25 deck shows strong HVTR/SWGR growth momentum, order backlog rising from KRW2.6tn in 1Q24 to KRW3.9tn in 1Q25, and US-origin new orders exceeding half of Q1 orders.","component_scores":{"eps_fcf_explosion":82,"earnings_visibility":88,"bottleneck_pricing":86,"market_mispricing":76,"valuation_rerating":72,"capital_allocation":52,"information_confidence":86},"component_weights":{"eps_fcf_explosion":21,"earnings_visibility":24,"bottleneck_pricing":20,"market_mispricing":13,"valuation_rerating":12,"capital_allocation":5,"information_confidence":5},"weighted_total_proxy":80.96,"current_profile_error":"missed_stage3_yellow_candidate","residual_label":"official_backlog_reacceleration_positive","source_proxy_only":false,"evidence_url_pending":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":193,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_HIGH_VALUE_TRANSFORMER_BACKLOG_MARGIN_BRIDGE","case_id":"C02_R1L193_298040_20250429_STAGE2A","symbol":"298040","company_name":"Hyosung Heavy Industries","trigger_type":"Stage2-Actionable","case_role":"positive_visible_profit_uptrend","trigger_date":"2025-04-29","entry_date":"2025-04-29","entry_price":520000.0,"actual_1d_ohlc_row":{"d":"2025-04-29","o":492000.0,"h":522000.0,"l":487000.0,"c":520000.0,"v":92036,"a":47150316250.0,"mc":4848764960000.0,"s":9324548,"m":"KOSPI"},"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv; atlas/ohlcv_tradable_by_symbol_year/298/298040/2026.csv","mfe_30d_pct":49.04,"mae_30d_pct":-6.35,"peak_30d_date":"2025-06-16","trough_30d_date":"2025-04-29","mfe_90d_pct":160.77,"mae_90d_pct":-6.35,"peak_90d_date":"2025-07-28","trough_90d_date":"2025-04-29","mfe_180d_pct":377.5,"mae_180d_pct":-6.35,"peak_180d_date":"2025-11-04","trough_180d_date":"2025-04-29","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"evidence_title":"Hyosung Heavy Industries — Visible profit uptrend, Mirae Asset, 2025-04-29","evidence_url":"https://securities.miraeasset.com/bbs/download/2135886.pdf?attachmentId=2135886","evidence_quality":"analyst_report_direct_url_company_data","evidence_summary":"1Q25 report shows revenue growth, operating profit uptrend, KRW10.4tn heavy-industries backlog, new orders above KRW2tn, high-value project revenue recognition, and improving overseas subsidiary margins.","component_scores":{"eps_fcf_explosion":87,"earnings_visibility":88,"bottleneck_pricing":86,"market_mispricing":78,"valuation_rerating":74,"capital_allocation":48,"information_confidence":82},"component_weights":{"eps_fcf_explosion":21,"earnings_visibility":24,"bottleneck_pricing":20,"market_mispricing":13,"valuation_rerating":12,"capital_allocation":5,"information_confidence":5},"weighted_total_proxy":82.11,"current_profile_error":"missed_structural_positive_candidate","residual_label":"backlog_margin_revenue_recognition_positive","source_proxy_only":false,"evidence_url_pending":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":193,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_CABLE_HEAVY_ELECTRIC_BACKLOG_BRIDGE","case_id":"C02_R1L193_103590_20241115_STAGE2A","symbol":"103590","company_name":"Iljin Electric","trigger_type":"Stage2-Actionable","case_role":"positive_backlog_chart_bridge","trigger_date":"2024-11-15","entry_date":"2024-11-15","entry_price":24650.0,"actual_1d_ohlc_row":{"d":"2024-11-15","o":25450.0,"h":25550.0,"l":24500.0,"c":24650.0,"v":828250,"a":20599008600.0,"mc":1175444863500.0,"s":47685390,"m":"KOSPI"},"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv; atlas/ohlcv_tradable_by_symbol_year/103/103590/2025.csv","mfe_30d_pct":15.42,"mae_30d_pct":-16.84,"peak_30d_date":"2024-12-18","trough_30d_date":"2024-11-29","mfe_90d_pct":52.33,"mae_90d_pct":-16.84,"peak_90d_date":"2025-01-24","trough_90d_date":"2024-11-29","mfe_180d_pct":80.12,"mae_180d_pct":-19.68,"peak_180d_date":"2025-07-29","trough_180d_date":"2025-04-09","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"evidence_title":"Iljin Electric, Mirae Asset, 2024-11-15","evidence_url":"https://securities.miraeasset.com/bbs/download/2132362.pdf?attachmentId=2132362","evidence_quality":"analyst_report_direct_url_company_data","evidence_summary":"Report includes quarterly order-backlog trends for power cables/systems and heavy electric, plus revenue and operating-margin bridge and capacity ramp-up plans.","component_scores":{"eps_fcf_explosion":76,"earnings_visibility":80,"bottleneck_pricing":78,"market_mispricing":65,"valuation_rerating":58,"capital_allocation":40,"information_confidence":72},"component_weights":{"eps_fcf_explosion":21,"earnings_visibility":24,"bottleneck_pricing":20,"market_mispricing":13,"valuation_rerating":12,"capital_allocation":5,"information_confidence":5},"weighted_total_proxy":71.77,"current_profile_error":"proper_stage2_actionable_positive","residual_label":"component_specific_backlog_positive","source_proxy_only":false,"evidence_url_pending":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":193,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_DISTRIBUTION_TRANSFORMER_EXPORT_HIGH_MAE","case_id":"C02_R1L193_033100_20240529_STAGE2A_HMAE","symbol":"033100","company_name":"JeRyong Electric","trigger_type":"Stage2-Actionable","case_role":"high_mae_stage2_actionable_counterexample","trigger_date":"2024-05-29","entry_date":"2024-05-29","entry_price":73900.0,"actual_1d_ohlc_row":{"d":"2024-05-29","o":78100.0,"h":78900.0,"l":72500.0,"c":73900.0,"v":1114957,"a":83659733800.0,"mc":1187012025100.0,"s":16062409,"m":"KOSDAQ"},"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv","mfe_30d_pct":35.05,"mae_30d_pct":-17.73,"peak_30d_date":"2024-07-10","trough_30d_date":"2024-06-10","mfe_90d_pct":36.27,"mae_90d_pct":-41.54,"peak_90d_date":"2024-07-11","trough_90d_date":"2024-09-09","mfe_180d_pct":36.27,"mae_180d_pct":-50.54,"peak_180d_date":"2024-07-11","trough_180d_date":"2024-12-09","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"evidence_title":"JeRyong Electric Q1 surge and US transformer shortage, The Bigdata, 2024-05-29","evidence_url":"https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23","evidence_quality":"article_with_broker_quote_company_metrics","evidence_summary":"Article cites Q1 sales and operating profit growth, export share of 94%, US transformer shortage, and KRW305.6bn order backlog equal to about 1.1 years of 2024 expected sales.","component_scores":{"eps_fcf_explosion":82,"earnings_visibility":85,"bottleneck_pricing":82,"market_mispricing":25,"valuation_rerating":28,"capital_allocation":35,"information_confidence":70},"component_weights":{"eps_fcf_explosion":21,"earnings_visibility":24,"bottleneck_pricing":20,"market_mispricing":13,"valuation_rerating":12,"capital_allocation":5,"information_confidence":5},"weighted_total_proxy":65.88,"current_profile_error":"over_promotion_risk_due_to_valuation_and_peak_proximity","residual_label":"strong_evidence_but_late_high_mae_guardrail","source_proxy_only":false,"evidence_url_pending":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":193,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_TRANSFORMER_COMPETITION_SLOWING_4B_HOLDOUT","case_id":"C02_R1L193_033100_20241203_4B_HOLDOUT","symbol":"033100","company_name":"JeRyong Electric","trigger_type":"4B","case_role":"hard_4c_holdout_competition_order_slowing","trigger_date":"2024-12-03","entry_date":"2024-12-03","entry_price":41100.0,"actual_1d_ohlc_row":{"d":"2024-12-03","o":39350.0,"h":41150.0,"l":39250.0,"c":41100.0,"v":305716,"a":12388907600.0,"mc":660165009900.0,"s":16062409,"m":"KOSDAQ"},"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_shard":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv; atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv","mfe_30d_pct":45.99,"mae_30d_pct":-11.07,"peak_30d_date":"2025-01-16","trough_30d_date":"2024-12-09","mfe_90d_pct":56.2,"mae_90d_pct":-35.64,"peak_90d_date":"2025-01-23","trough_90d_date":"2025-04-09","mfe_180d_pct":56.2,"mae_180d_pct":-35.64,"peak_180d_date":"2025-01-23","trough_180d_date":"2025-04-09","calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window_180D":false,"evidence_title":"JeRyong Electric drawdown and US order competition risk, Daily Invest, 2024-12-03","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=62181","evidence_quality":"article_with_broker_quote_company_metrics","evidence_summary":"Article discusses export share rising to 92% YTD 3Q24 and order backlog to be recognized until 3Q25, while also flagging possible order-flow slowing and intensifying US competition.","component_scores":{"eps_fcf_explosion":65,"earnings_visibility":68,"bottleneck_pricing":60,"market_mispricing":35,"valuation_rerating":30,"capital_allocation":35,"information_confidence":68},"component_weights":{"eps_fcf_explosion":21,"earnings_visibility":24,"bottleneck_pricing":20,"market_mispricing":13,"valuation_rerating":12,"capital_allocation":5,"information_confidence":5},"weighted_total_proxy":55.27,"current_profile_error":"avoid_hard_4c_without_cancellation_or_margin_break","residual_label":"local_4b_not_hard_4c_despite_order_slowing_language","source_proxy_only":false,"evidence_url_pending":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"aggregate","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":193,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_trigger_count":7,"unique_symbol_count":5,"calibration_usable_trigger_count":7,"positive_or_missed_positive_case_count":4,"high_mae_or_4b_guardrail_case_count":3,"hard_4c_case_count":0,"source_proxy_only_count":0,"evidence_url_pending_count":0,"missing_required_mfe_mae_count":0,"corporate_action_contaminated_180D_count":0,"insufficient_forward_window_180D_count":0,"new_independent_ratio":1.0}
{"row_type":"shadow_weight","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","scope":"C02_POWER_GRID_DATACENTER_CAPEX","before_weights":{"eps_fcf_explosion":21,"earnings_visibility":24,"bottleneck_pricing":20,"market_mispricing":13,"valuation_rerating":12,"capital_allocation":5,"information_confidence":5},"after_candidate_weights":{"eps_fcf_explosion":21,"earnings_visibility":25,"bottleneck_pricing":21,"market_mispricing":13,"valuation_rerating":10,"capital_allocation":5,"information_confidence":5},"production_scoring_changed":false,"candidate_status":"shadow_only_requires_parser_validation_and_cross_batch_confirmation"}
{"row_type":"residual_contribution","research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","canonical_rule_candidate":"C02_GRID_BACKLOG_MARGIN_EXTENSION_GATE","positive_bridge":"company-specific backlog + order + North America/data-center/grid demand + margin recognition improves Stage2-Actionable/Stage3-Yellow quality","negative_guardrail":"late price extension and high MAE require local 4B watch rather than Green","hard_4c_rule":"do not force hard 4C from price drawdown alone; require non-price cancellation/backlog/margin/capacity break","production_scoring_changed":false}
{"row_type":"narrative_only","note":"C02 now needs quality repair more than row-count expansion; the key split is company-specific order-to-margin evidence vs macro data-center/grid theme and price extension.","promotion_eligible":false}
```

## 10. Batch Ingest Self-Audit

```text
batch_ingest_self_audit:
  selected_round: R1
  selected_loop: 193
  large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
  round_sector_consistency: pass
  coverage_index_first: pass
  no_repeat_index_used_only_as_duplicate_ledger: pass
  hard_duplicate_key_checked: canonical_archetype_id + symbol + trigger_type + entry_date
  duplicate_key_collision_in_batch: 0
  new_independent_trigger_count: 7
  unique_symbol_count: 5
  calibration_usable_trigger_count: 7
  actual_stock_web_1d_ohlc_rows_present: 7
  mfe_mae_30_90_180_present: 7
  missing_required_mfe_mae_count: 0
  corporate_action_contaminated_180D_count: 0
  insufficient_forward_window_180D_count: 0
  source_proxy_only_count: 0
  evidence_url_pending_count: 0
  production_scoring_changed: false
  shadow_weight_only: true
```

## 11. Next Research State

```text
completed_round: R1
completed_loop: 193
completed_large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
completed_canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
completion_status: standalone_md_ready_for_v12_ingest

next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - C02_POWER_GRID_DATACENTER_CAPEX_4B_4C_DIRECT_BREAK_REPAIR
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
```
