# E2R v12 Stock-Web Residual Research — R3 / L3 / C12 Battery Customer Contract Call-Off Risk

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R3
selected_loop = 224
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality repair + Priority 1 balance spillover
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection / novelty check

The cumulative no-repeat ledger shows all C01~C32 archetypes above the old row-count thresholds, so this run prioritizes direct evidence URL quality, customer call-off / utilization failure balance, and complete Stock-Web price rows rather than simply adding more C05/C10/C13 rows. C12 has 249 representative rows and still needs cleaner separation between customer-inventory/call-off breaks and valid direct customer supply bridges.

Hard duplicate key rule: `canonical_archetype_id + symbol + trigger_type + entry_date`. None of the usable rows below repeats a C12 hard key within this run.

## 2. Price source validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_columns = d,o,h,l,c,v,a,mc,s,m
corporate_action_window_rule = block if candidate date overlaps entry_date~D+180
```

Profile check summary: LG Energy Solution, Samsung SDI, SK IE Technology, LOTTE Energy Materials, EcoPro BM, L&F, and Chunbo all have 180D forward windows available through Stock-Web manifest max date. L&F has older corporate-action candidate dates in 2016/2021, outside this run's 2024~2025 windows; the other selected profiles used here have no 180D corporate-action contamination in the tested windows.

## 3. Batch Ingest Self-Audit

```text
new_independent_case_count = 7
new_independent_trigger_count = 7
unique_symbol_count = 7
calibration_usable_trigger_count = 7

stage2_count = 1
stage2_actionable_count = 1
stage4b_count = 2
stage4c_count = 3

positive_or_second_bridge_control_count = 2
calloff_or_utilization_break_count = 5
high_MAE_180D_count_MAE_le_-20 = 7
deep_MAE_180D_count_MAE_le_-40 = 5

source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0

production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 4. Trigger-level price table

| symbol | name | trigger | entry_date | entry_close | MFE30 / MAE30 | MFE90 / MAE90 | MFE180 / MAE180 | peak180 | trough180 | post-peak DD | role |
|---|---|---|---:|---:|---:|---:|---:|---|---|---:|---|
| 373220 | LG Energy Solution | Stage4B | 2024-10-28 | 416500 | 4.56 / -10.92 | 4.56 / -21.37 | 4.56 / -36.13 | 2024-11-11 | 2025-05-23 | -38.92 | offset_quality_watch |
| 006400 | Samsung SDI | Stage4B | 2024-07-30 | 330500 | 14.98 / -10.89 | 19.06 / -28.74 | 19.06 / -48.56 | 2024-09-30 | 2025-04-09 | -56.80 | slowdown_with_ESS_offset |
| 361610 | SK IE Technology | Stage4C | 2024-07-31 | 37300 | 2.01 / -20.11 | 3.89 / -39.28 | 3.89 / -48.23 | 2024-10-07 | 2025-04-09 | -50.17 | calloff_utilization_break |
| 020150 | LOTTE Energy Materials | Stage4C | 2024-11-01 | 36300 | 3.44 / -42.42 | 3.44 / -44.21 | 3.44 / -46.39 | 2024-11-01 | 2025-05-22 | -48.18 | customer_inventory_adjustment_break |
| 247540 | EcoPro BM | Stage4C | 2024-07-30 | 187500 | 2.35 / -20.69 | 3.73 / -35.79 | 3.73 / -53.60 | 2024-10-10 | 2025-04-03 | -55.27 | asp_volume_inventory_guardrail |
| 066970 | L&F | Stage2-Actionable | 2024-11-04 | 112000 | 12.77 / -17.68 | 12.77 / -37.41 | 12.77 / -58.04 | 2024-11-12 | 2025-05-26 | -62.79 | direct_customer_supply_positive_control_high_mae |
| 278280 | Chunbo | Stage2 | 2024-09-03 | 61300 | 7.18 / -15.01 | 7.18 / -42.25 | 7.18 / -50.98 | 2024-10-08 | 2025-04-09 | -54.26 | north_america_shipments_partial_bridge |

## 5. Case notes

### 1. 373220 LG Energy Solution — Stage4B

- Evidence: Q3 2024 earnings: IRA tax credit exceeded reported OP; ex-credit quarterly OP was negative, while JV/ESS/customer supply offsets remained explicit.
- Evidence URL: https://news.lgensol.com/company-news/press-releases/3343/
- Stock-Web shard: `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv` + `2025.csv`
- Actual entry OHLCV: `2024-10-28, o=403000, h=417500, l=403000, c=416500, v=360352, m=KOSPI`
- Backtest result: 180D MFE/MAE = `4.56% / -36.13%`; peak/trough = `2024-11-11 / 2025-05-23`.
- Interpretation: ugly EV-demand evidence is real, but ESS/JV/customer offset quality prevents sticky hard 4C; keep local 4B/watch until utilization or ex-subsidy economics proves recovery.

### 2. 006400 Samsung SDI — Stage4B

- Evidence: Q2 2024 revenue and OP declined YoY; Automotive & ESS fell short on sluggish demand, but ESS revenue/profit improved on UPS/SBB/data-center demand.
- Evidence URL: https://www.samsungsdi.com/sdi-now/sdi-news/3862.html
- Stock-Web shard: `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv` + `2025.csv`
- Actual entry OHLCV: `2024-07-30, o=333000, h=344500, l=330500, c=330500, v=423808, m=KOSPI`
- Backtest result: 180D MFE/MAE = `19.06% / -48.56%`; peak/trough = `2024-09-30 / 2025-04-09`.
- Interpretation: ugly EV-demand evidence is real, but ESS/JV/customer offset quality prevents sticky hard 4C; keep local 4B/watch until utilization or ex-subsidy economics proves recovery.

### 3. 361610 SK IE Technology — Stage4C

- Evidence: Q2 2024 net loss and operating loss with revenue down 59.3% YoY; separator utilization/call-off break dominates offset quality.
- Evidence URL: https://www.koreatimes.co.kr/business/companies/20240731/korean-companysk-ie-technology-reports-losses-in-q2
- Stock-Web shard: `atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv` + `2025.csv`
- Actual entry OHLCV: `2024-07-31, o=37100, h=37600, l=36600, c=37300, v=121162, m=KOSPI`
- Backtest result: 180D MFE/MAE = `3.89% / -48.23%`; peak/trough = `2024-10-07 / 2025-04-09`.
- Interpretation: direct customer-calloff, utilization, ASP, or inventory-adjustment break is severe enough to protect hard 4C unless later direct customer/volume offset appears.

### 4. 020150 LOTTE Energy Materials — Stage4C

- Evidence: Q3 2024 operating loss; sales volume fell due to customer inventory adjustments and EV-market slowdown; lower utilization and inventory valuation losses pressured OP.
- Evidence URL: https://www.asiae.co.kr/en/article/2024110113530226953
- Stock-Web shard: `atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv` + `2025.csv`
- Actual entry OHLCV: `2024-11-01, o=37300, h=37550, l=35600, c=36300, v=141288, m=KOSPI`
- Backtest result: 180D MFE/MAE = `3.44% / -46.39%`; peak/trough = `2024-11-01 / 2025-05-22`.
- Interpretation: direct customer-calloff, utilization, ASP, or inventory-adjustment break is severe enough to protect hard 4C unless later direct customer/volume offset appears.

### 5. 247540 EcoPro BM — Stage4C

- Evidence: Q2 2024 cathode revenue down 17% QoQ, ASP declined 13% QoQ; sales volume down and EV cathode growth expected to remain limited.
- Evidence URL: https://www.alphaspread.com/es/security/kosdaq/247540/investor-relations/earnings-call/q2-2024
- Stock-Web shard: `atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv` + `2025.csv`
- Actual entry OHLCV: `2024-07-30, o=177100, h=190000, l=176100, c=187500, v=927485, m=KOSDAQ GLOBAL`
- Backtest result: 180D MFE/MAE = `3.73% / -53.60%`; peak/trough = `2024-10-10 / 2025-04-03`.
- Interpretation: direct customer-calloff, utilization, ASP, or inventory-adjustment break is severe enough to protect hard 4C unless later direct customer/volume offset appears.

### 6. 066970 L&F — Stage2-Actionable

- Evidence: High-nickel NCMA95 supply route announced around Q3 2024 earnings; direct named customer route creates Actionable but high MAE blocks Yellow/Green.
- Evidence URL: https://www.kedglobal.com/batteries/newsView/ked202411030003
- Stock-Web shard: `atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv` + `2025.csv`
- Actual entry OHLCV: `2024-11-04, o=114800, h=119000, l=108300, c=112000, v=750031, m=KOSPI`
- Backtest result: 180D MFE/MAE = `12.77% / -58.04%`; peak/trough = `2024-11-12 / 2025-05-26`.
- Interpretation: direct named customer supply route is enough to preserve Stage2-Actionable, but deep 180D MAE blocks Stage3-Yellow/Green.

### 7. 278280 Chunbo — Stage2

- Evidence: North America-bound P-additive/F-electrolyte shipments expanded meaningfully in July, but overall earnings recovery was expected to take time amid depressed China ASP.
- Evidence URL: https://securities.miraeasset.com/bbs/download/2130998.pdf?attachmentId=2130998
- Stock-Web shard: `atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv` + `2025.csv`
- Actual entry OHLCV: `2024-09-03, o=61000, h=62500, l=59900, c=61300, v=25780, m=KOSDAQ`
- Backtest result: 180D MFE/MAE = `7.18% / -50.98%`; peak/trough = `2024-10-08 / 2025-04-09`.
- Interpretation: North America shipment bridge is promising but still early; earnings recovery and margin conversion are not yet strong enough for Actionable.

## 6. Current calibrated profile stress test

| symbol | trigger | component score proxy EPS/Vis/Bott/Mis/Val/Cap/Info | total_proxy | current profile residual |
|---|---|---:|---:|---|
| 373220 | Stage4B | 8/12/8/10/8/4/17 | 67 | watch_not_sticky_4c |
| 006400 | Stage4B | 8/12/8/10/8/4/17 | 67 | watch_not_sticky_4c |
| 361610 | Stage4C | 4/8/4/8/6/3/18 | 51 | hard_4c_confirmation_needed |
| 020150 | Stage4C | 4/8/4/8/6/3/18 | 51 | hard_4c_confirmation_needed |
| 247540 | Stage4C | 4/8/4/8/6/3/18 | 51 | hard_4c_confirmation_needed |
| 066970 | Stage2-Actionable | 12/17/14/12/10/5/14 | 84 | green_blocked_by_high_mae |
| 278280 | Stage2 | 10/14/12/10/8/4/12 | 70 | stage2_cap_until_second_bridge |

Stress-test conclusion: C12 does not need a global Stage2 loosening. It needs a stricter second-bridge gate for customer-calloff risk. Direct supply-route rows can preserve Stage2-Actionable, but the same row should be capped below Yellow/Green when 90D/180D MAE is deep and utilization / ex-subsidy margin / shipment conversion is unproven.

## 7. Residual contribution

```text
rule_candidate = C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1
sector_rule_candidate = L3_BATTERY_CUSTOMER_CALLOFF_UTILIZATION_GREEN_BLOCKER_GATE_V1

core_residual:
- Customer call-off, inventory adjustment, utilization collapse, ASP decline, or fixed-cost absorption evidence can route to Stage4B/Stage4C depending on offset quality.
- AMPC / IRA / JV / North America wording alone does not create Stage2-Actionable or Yellow.
- Stage2-Actionable requires at least one direct second bridge: named customer supply, shipment conversion, utilization rebound, customer pull/call-off recovery, ex-subsidy margin, or order/backlog-to-revenue conversion.
- ESS / JV / North America offset downgrades hard 4C to Stage4B/watch only when the offset is tied to actual shipment, utilization, or revenue.
- High MAE on a valid direct-bridge row blocks Yellow/Green first; it does not erase Stage2-Actionable.
- Stage3-Green remains blocked until direct customer bridge and margin/cashflow evidence repeat across more than one evidence family.
```

## 8. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "research_version": "v12", "selected_round": "R3", "selected_loop": 224, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1", "symbol": "373220", "company_name": "LG Energy Solution", "trigger_type": "Stage4B", "case_role": "offset_quality_watch", "trigger_date": "2024-10-28", "entry_date": "2024-10-28", "entry_price": 416500.0, "entry_ohlcv": {"o": 403000.0, "h": 417500.0, "l": 403000.0, "c": 416500.0, "v": 360352.0, "market": "KOSPI"}, "mfe_30d_pct": 4.56, "mae_30d_pct": -10.92, "mfe_90d_pct": 4.56, "mae_90d_pct": -21.37, "mfe_180d_pct": 4.56, "mae_180d_pct": -36.13, "peak_180d_date": "2024-11-11", "trough_180d_date": "2025-05-23", "post_peak_drawdown_180d_pct": -38.92, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_url": "https://news.lgensol.com/company-news/press-releases/3343/", "evidence_summary": "Q3 2024 earnings: IRA tax credit exceeded reported OP; ex-credit quarterly OP was negative, while JV/ESS/customer supply offsets remained explicit.", "score_simulation": {"eps_fcf_explosion": 8, "earnings_visibility": 12, "bottleneck_pricing": 8, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 17, "total_proxy": 67, "current_profile_error": "watch_not_sticky_4c"}, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|373220|Stage4B|2024-10-28"}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R3", "selected_loop": 224, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1", "symbol": "006400", "company_name": "Samsung SDI", "trigger_type": "Stage4B", "case_role": "slowdown_with_ESS_offset", "trigger_date": "2024-07-30", "entry_date": "2024-07-30", "entry_price": 330500.0, "entry_ohlcv": {"o": 333000.0, "h": 344500.0, "l": 330500.0, "c": 330500.0, "v": 423808.0, "market": "KOSPI"}, "mfe_30d_pct": 14.98, "mae_30d_pct": -10.89, "mfe_90d_pct": 19.06, "mae_90d_pct": -28.74, "mfe_180d_pct": 19.06, "mae_180d_pct": -48.56, "peak_180d_date": "2024-09-30", "trough_180d_date": "2025-04-09", "post_peak_drawdown_180d_pct": -56.8, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_url": "https://www.samsungsdi.com/sdi-now/sdi-news/3862.html", "evidence_summary": "Q2 2024 revenue and OP declined YoY; Automotive & ESS fell short on sluggish demand, but ESS revenue/profit improved on UPS/SBB/data-center demand.", "score_simulation": {"eps_fcf_explosion": 8, "earnings_visibility": 12, "bottleneck_pricing": 8, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 17, "total_proxy": 67, "current_profile_error": "watch_not_sticky_4c"}, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|006400|Stage4B|2024-07-30"}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R3", "selected_loop": 224, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1", "symbol": "361610", "company_name": "SK IE Technology", "trigger_type": "Stage4C", "case_role": "calloff_utilization_break", "trigger_date": "2024-07-31", "entry_date": "2024-07-31", "entry_price": 37300.0, "entry_ohlcv": {"o": 37100.0, "h": 37600.0, "l": 36600.0, "c": 37300.0, "v": 121162.0, "market": "KOSPI"}, "mfe_30d_pct": 2.01, "mae_30d_pct": -20.11, "mfe_90d_pct": 3.89, "mae_90d_pct": -39.28, "mfe_180d_pct": 3.89, "mae_180d_pct": -48.23, "peak_180d_date": "2024-10-07", "trough_180d_date": "2025-04-09", "post_peak_drawdown_180d_pct": -50.17, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_url": "https://www.koreatimes.co.kr/business/companies/20240731/korean-companysk-ie-technology-reports-losses-in-q2", "evidence_summary": "Q2 2024 net loss and operating loss with revenue down 59.3% YoY; separator utilization/call-off break dominates offset quality.", "score_simulation": {"eps_fcf_explosion": 4, "earnings_visibility": 8, "bottleneck_pricing": 4, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 3, "information_confidence": 18, "total_proxy": 51, "current_profile_error": "hard_4c_confirmation_needed"}, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|361610|Stage4C|2024-07-31"}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R3", "selected_loop": 224, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1", "symbol": "020150", "company_name": "LOTTE Energy Materials", "trigger_type": "Stage4C", "case_role": "customer_inventory_adjustment_break", "trigger_date": "2024-11-01", "entry_date": "2024-11-01", "entry_price": 36300.0, "entry_ohlcv": {"o": 37300.0, "h": 37550.0, "l": 35600.0, "c": 36300.0, "v": 141288.0, "market": "KOSPI"}, "mfe_30d_pct": 3.44, "mae_30d_pct": -42.42, "mfe_90d_pct": 3.44, "mae_90d_pct": -44.21, "mfe_180d_pct": 3.44, "mae_180d_pct": -46.39, "peak_180d_date": "2024-11-01", "trough_180d_date": "2025-05-22", "post_peak_drawdown_180d_pct": -48.18, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_url": "https://www.asiae.co.kr/en/article/2024110113530226953", "evidence_summary": "Q3 2024 operating loss; sales volume fell due to customer inventory adjustments and EV-market slowdown; lower utilization and inventory valuation losses pressured OP.", "score_simulation": {"eps_fcf_explosion": 4, "earnings_visibility": 8, "bottleneck_pricing": 4, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 3, "information_confidence": 18, "total_proxy": 51, "current_profile_error": "hard_4c_confirmation_needed"}, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|020150|Stage4C|2024-11-01"}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R3", "selected_loop": 224, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1", "symbol": "247540", "company_name": "EcoPro BM", "trigger_type": "Stage4C", "case_role": "asp_volume_inventory_guardrail", "trigger_date": "2024-07-30", "entry_date": "2024-07-30", "entry_price": 187500.0, "entry_ohlcv": {"o": 177100.0, "h": 190000.0, "l": 176100.0, "c": 187500.0, "v": 927485.0, "market": "KOSDAQ GLOBAL"}, "mfe_30d_pct": 2.35, "mae_30d_pct": -20.69, "mfe_90d_pct": 3.73, "mae_90d_pct": -35.79, "mfe_180d_pct": 3.73, "mae_180d_pct": -53.6, "peak_180d_date": "2024-10-10", "trough_180d_date": "2025-04-03", "post_peak_drawdown_180d_pct": -55.27, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_url": "https://www.alphaspread.com/es/security/kosdaq/247540/investor-relations/earnings-call/q2-2024", "evidence_summary": "Q2 2024 cathode revenue down 17% QoQ, ASP declined 13% QoQ; sales volume down and EV cathode growth expected to remain limited.", "score_simulation": {"eps_fcf_explosion": 4, "earnings_visibility": 8, "bottleneck_pricing": 4, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 3, "information_confidence": 18, "total_proxy": 51, "current_profile_error": "hard_4c_confirmation_needed"}, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|247540|Stage4C|2024-07-30"}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R3", "selected_loop": 224, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1", "symbol": "066970", "company_name": "L&F", "trigger_type": "Stage2-Actionable", "case_role": "direct_customer_supply_positive_control_high_mae", "trigger_date": "2024-11-04", "entry_date": "2024-11-04", "entry_price": 112000.0, "entry_ohlcv": {"o": 114800.0, "h": 119000.0, "l": 108300.0, "c": 112000.0, "v": 750031.0, "market": "KOSPI"}, "mfe_30d_pct": 12.77, "mae_30d_pct": -17.68, "mfe_90d_pct": 12.77, "mae_90d_pct": -37.41, "mfe_180d_pct": 12.77, "mae_180d_pct": -58.04, "peak_180d_date": "2024-11-12", "trough_180d_date": "2025-05-26", "post_peak_drawdown_180d_pct": -62.79, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_url": "https://www.kedglobal.com/batteries/newsView/ked202411030003", "evidence_summary": "High-nickel NCMA95 supply route announced around Q3 2024 earnings; direct named customer route creates Actionable but high MAE blocks Yellow/Green.", "score_simulation": {"eps_fcf_explosion": 12, "earnings_visibility": 17, "bottleneck_pricing": 14, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 5, "information_confidence": 14, "total_proxy": 84, "current_profile_error": "green_blocked_by_high_mae"}, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|066970|Stage2-Actionable|2024-11-04"}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R3", "selected_loop": 224, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1", "symbol": "278280", "company_name": "Chunbo", "trigger_type": "Stage2", "case_role": "north_america_shipments_partial_bridge", "trigger_date": "2024-09-03", "entry_date": "2024-09-03", "entry_price": 61300.0, "entry_ohlcv": {"o": 61000.0, "h": 62500.0, "l": 59900.0, "c": 61300.0, "v": 25780.0, "market": "KOSDAQ"}, "mfe_30d_pct": 7.18, "mae_30d_pct": -15.01, "mfe_90d_pct": 7.18, "mae_90d_pct": -42.25, "mfe_180d_pct": 7.18, "mae_180d_pct": -50.98, "peak_180d_date": "2024-10-08", "trough_180d_date": "2025-04-09", "post_peak_drawdown_180d_pct": -54.26, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_url": "https://securities.miraeasset.com/bbs/download/2130998.pdf?attachmentId=2130998", "evidence_summary": "North America-bound P-additive/F-electrolyte shipments expanded meaningfully in July, but overall earnings recovery was expected to take time amid depressed China ASP.", "score_simulation": {"eps_fcf_explosion": 10, "earnings_visibility": 14, "bottleneck_pricing": 12, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 12, "total_proxy": 70, "current_profile_error": "stage2_cap_until_second_bridge"}, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|278280|Stage2|2024-09-03"}
```

## 9. Shadow weight suggestion

```json
{
  "row_type": "shadow_weight",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "rule_candidate": "C12_CUSTOMER_CALLOFF_UTILIZATION_AND_SECOND_BRIDGE_GATE_V1",
  "do_not_propose_new_global_weight_delta": true,
  "suggested_local_adjustment": {
    "information_confidence": "+2 when direct customer-calloff/utilization evidence is issuer-confirmed",
    "earnings_visibility": "-2 when only AMPC/IRA/JV wording supports the case",
    "stage3_green_gate": "require direct customer bridge plus margin/cashflow conversion across >=2 evidence families",
    "hard_4c_gate": "require utilization/call-off/margin break + weak offset quality"
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD alone. In the later batch coding session, ingest this file together with other v12 MDs, validate all JSONL rows, deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date, and only consider a C12-local rule if aggregate evidence confirms that customer-calloff/utilization breaks create asymmetric false positives while direct second-bridge rows preserve Stage2-Actionable but block Yellow/Green.
```

## 11. Next Research State

```text
completed_round = R3
completed_loop = 224
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality repair + C12 balance reinforcement
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```