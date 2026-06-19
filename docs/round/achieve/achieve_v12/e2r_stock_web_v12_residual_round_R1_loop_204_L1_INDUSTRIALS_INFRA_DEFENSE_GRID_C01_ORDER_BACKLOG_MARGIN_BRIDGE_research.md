# E2R v12 Stock-Web Residual Research — R1 / L1 / C01 Construction Equipment Cashflow Bridge

```text
selected_round: R1
selected_loop: 204
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority_1_balance_reinforcement_after_all_C01_C32_above_80_rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE

loop_objective:
- sector_specific_rule_discovery
- residual_false_positive_mining
- stage2_actionable_bonus_stress_test
- 4B_non_price_requirement_stress_test
- holdout_validation

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 1. Selection Rationale

MAIN EXECUTION PROMPT 기준으로 이번 실행은 `stock_agent` 코드 패치나 live scan이 아니라 Songdaiki/stock-web 1D OHLCV를 사용한 historical trigger-level residual calibration이다.
NO-REPEAT INDEX는 중복 방지 장부로만 사용했다. 현재 장부상 모든 C01~C32 canonical archetype이 80 rows 이상이므로 row filling이 아니라 quality reinforcement 단계이며, Priority 1에 남아 있는 `C01_ORDER_BACKLOG_MARGIN_BRIDGE`의 핵심 보강축은 backlog/order/sales headline이 실제 margin, net cash, working capital, cash conversion으로 이어지는지 분리하는 것이다.

이번 MD는 C01을 조선 prime-yard 중심에서 **construction equipment / compact equipment / wind-tower manufacturing**으로 확장한다. 이 하위 축은 수주잔고라는 단어가 항상 명시되지 않아도, order/sales route가 실제 operating margin과 cash balance로 전환되는지를 보므로 C01의 `backlog -> margin bridge`와 동일한 구조다. 단, dealer inventory adjustment, one-time price renegotiation, promotional-cost burden처럼 cashflow quality가 흔들리는 row는 Actionable/Yellow가 아니라 Stage4B/watch 또는 Stage2 cap으로 묶는다.

### Duplicate guard

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
checked_local_prior_C01_files:
- R1_loop_189_C01 shipbuilding backlog/margin
- R1_loop_201_C01 shipbuilding high-MAE cap
- R1_loop_203_C01 engine/supplier backlog margin

new symbols in this C01 local sequence:
- 267270 HD Hyundai Construction Equipment
- 042670 HD Hyundai Infracore
- 241560 Doosan Bobcat
- 112610 CS Wind

same_symbol_same_trigger_entry_reuse_count: 0
new_independent_case_ratio: 1.00
```

## 2. Stock-Web Price Source Validation

```text
price_atlas_repo: Songdaiki/stock-web
primary_price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
tradable_columns: d,o,h,l,c,v,a,mc,s,m
MFE_MAE_method: entry close vs max high / min low over inclusive N-tradable-row windows
```

### Symbol profile contamination check

| Symbol | Profile status | Corporate-action candidate dates relevant to this batch | 180D contamination |
|---|---|---|---|
| 267270 | active_like, available through 2026-02-20 | 2017-2018 historical, 2026-01-26 after selected windows | false |
| 042670 | profile last tradable 2025-12-26, raw through 2026-01-23 | 2013-12-20, 2021-07-21, 2021-12-28 | false |
| 241560 | active_like | none | false |
| 112610 | active_like | 2021-02-08, 2021-02-22, 2021-03-05 | false |

## 3. Actual Entry OHLCV Rows

| Symbol | Entry date | Open | High | Low | Close/Entry | Volume | Amount | Market cap | Shares | Market | Shard |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 267270 | 2024-02-06 | 55,900 | 56,000 | 52,000 | 53,000 | 784,114 | 42,051,516,000 | 1,044,142,029,000 | 19,700,793 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/267/267270/2024.csv |
| 267270 | 2025-02-06 | 65,800 | 71,400 | 65,600 | 70,900 | 664,753 | 46,116,853,800 | 1,297,866,047,400 | 18,305,586 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/267/267270/2025.csv |
| 042670 | 2024-04-19 | 7,640 | 7,770 | 7,470 | 7,700 | 1,607,405 | 12,216,146,110 | 1,536,946,588,100 | 199,603,453 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv |
| 042670 | 2025-02-04 | 7,200 | 7,530 | 7,130 | 7,530 | 1,701,952 | 12,537,151,320 | 1,450,698,678,510 | 192,655,867 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/042/042670/2025.csv |
| 241560 | 2023-10-27 | 43,700 | 43,900 | 42,150 | 42,400 | 414,070 | 17,688,650,100 | 4,250,564,638,400 | 100,249,166 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/241/241560/2023.csv |
| 241560 | 2024-10-28 | 38,100 | 38,100 | 37,250 | 37,850 | 353,720 | 13,296,174,400 | 3,794,430,933,100 | 100,249,166 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv |
| 112610 | 2023-05-15 | 78,100 | 82,500 | 77,500 | 78,400 | 1,059,683 | 84,542,963,200 | 3,306,237,995,200 | 42,171,403 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/112/112610/2023.csv |
| 112610 | 2024-08-19 | 66,100 | 66,100 | 62,500 | 63,300 | 901,700 | 57,617,759,200 | 2,669,449,809,900 | 42,171,403 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/112/112610/2024.csv |

## 4. Trigger Return Summary

| Symbol | Company | Trigger | Entry | Entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | DD after peak | Case role |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 267270 | HD Hyundai Construction Equipment | Stage2-Actionable | 2024-02-06 | 53,000 | 13.96/-5.28 | 13.96/-7.08 | 33.96/-13.77 | 2024-07-23 | -35.63 | direct_profitability_balance_sheet_bridge |
| 267270 | HD Hyundai Construction Equipment | Stage4B | 2025-02-06 | 70,900 | 29.06/-8.32 | 29.06/-21.16 | 69.25/-21.16 | 2025-10-29 | -17.58 | ugly_annual_result_but_inventory_reset_reopen_watch |
| 042670 | HD Hyundai Infracore | Stage4B | 2024-04-19 | 7,700 | 14.03/-2.99 | 18.96/-16.10 | 18.96/-18.57 | 2024-07-23 | -31.55 | construction_equipment_slump_with_engine_offset_watch |
| 042670 | HD Hyundai Infracore | Stage4B | 2025-02-04 | 7,530 | 35.59/-5.31 | 65.34/-5.31 | 143.03/-5.31 | 2025-10-29 | -7.76 | annual_profit_collapse_with_turnaround_guidance_holdout |
| 241560 | Doosan Bobcat | Stage2-Actionable | 2023-10-27 | 42,400 | 8.73/-11.79 | 23.82/-11.79 | 46.93/-11.79 | 2024-05-27 | -23.11 | net_cash_and_profit_bridge_positive_control |
| 241560 | Doosan Bobcat | Stage4B | 2024-10-28 | 37,850 | 19.68/-4.62 | 41.08/-4.62 | 95.24/-4.62 | 2025-06-24 | -28.55 | dealer_inventory_adjustment_4b_not_4c |
| 112610 | CS Wind | Stage2 | 2023-05-15 | 78,400 | 14.03/-3.83 | 14.03/-28.32 | 14.03/-43.18 | 2023-06-21 | -50.17 | order_backlog_positive_but_cashflow_missing_guardrail |
| 112610 | CS Wind | Stage4B | 2024-08-19 | 63,300 | 16.11/-13.11 | 16.11/-41.23 | 16.11/-52.53 | 2024-09-24 | -59.12 | one_time_price_increase_profit_surprise_high_mae_guardrail |

## 5. Case Notes

### 1. 267270 HD Hyundai Construction Equipment — Stage2-Actionable / direct_profitability_balance_sheet_bridge

Evidence URL: https://www.hd.com/en/newsroom/media-hub/press/view?detailsKey=3255

2023 revenue and operating profit rose, debt ratio improved, and profitability was explained by developed-market infrastructure demand, emerging-market mining demand, price increases, and fixed-cost leverage.

Price path: entry close 53,000; 180D MFE/MAE 33.96% / -13.77%; peak 2024-07-23 at 71,000; trough 2024-09-09 at 45,700.

### 2. 267270 HD Hyundai Construction Equipment — Stage4B / ugly_annual_result_but_inventory_reset_reopen_watch

Evidence URL: https://www.hyundai-ce.com/en/media/newspress/view?detailsKey=2194

2024 revenue and operating profit declined on sluggish global demand, competition, and promotional expenses, but the company cited India/Brazil growth, lower inventories, Ulsan modernization, and market-specific products as reopen offsets.

Price path: entry close 70,900; 180D MFE/MAE 69.25% / -21.16%; peak 2025-10-29 at 120,000; trough 2025-04-09 at 55,900.

### 3. 042670 HD Hyundai Infracore — Stage4B / construction_equipment_slump_with_engine_offset_watch

Evidence URL: https://www.hd.com/en/newsroom/media-hub/press/view?detailsKey=3235

Q1 2024 sales and operating profit fell with construction-equipment market contraction, while the engine division kept a double-digit margin and management expected demand recovery in 2H24.

Price path: entry close 7,700; 180D MFE/MAE 18.96% / -18.57%; peak 2024-07-23 at 9,160; trough 2024-10-29 at 6,270.

### 4. 042670 HD Hyundai Infracore — Stage4B / annual_profit_collapse_with_turnaround_guidance_holdout

Evidence URL: https://www.asiae.co.kr/en/article/2025020417325562571

2024 operating profit fell sharply and the construction-equipment division profit plunged, but management framed 2025 as an advanced-market rebound and infrastructure-investment recovery year.

Price path: entry close 7,530; 180D MFE/MAE 143.03% / -5.31%; peak 2025-10-29 at 18,300; trough 2025-02-04 at 7,130.

### 5. 241560 Doosan Bobcat — Stage2-Actionable / net_cash_and_profit_bridge_positive_control

Evidence URL: https://www.doosanbobcat.com/en/mediacenter/news/detail?id=250&page=3&pageSize=10

Q3 2023 cumulative operating profit exceeded the prior full-year level and Doosan Bobcat converted net debt to net cash through stable cash flow.

Price path: entry close 42,400; 180D MFE/MAE 46.93% / -11.79%; peak 2024-05-27 at 62,300; trough 2023-11-01 at 37,400.

### 6. 241560 Doosan Bobcat — Stage4B / dealer_inventory_adjustment_4b_not_4c

Evidence URL: https://www.doosanbobcat.com/en/mediacenter/news/detail?id=281&page=1&pageSize=10

Q3 2024 revenue fell 28% and operating profit dropped 59% because of dealer inventory adjustment and fixed-cost burden from production cuts; this is a 4B watch unless cash/debt/order collapse is confirmed.

Price path: entry close 37,850; 180D MFE/MAE 95.24% / -4.62%; peak 2025-06-24 at 73,900; trough 2024-10-29 at 36,100.

### 7. 112610 CS Wind — Stage2 / order_backlog_positive_but_cashflow_missing_guardrail

Evidence URL: https://www.cswind.com/en/board/board.download/?n=455&seq=1&t=common

Indexed issuer 1Q23 earnings release indicated order backlog around USD 736m and surplus conversion, but cash/working-capital and durable margin proof were still incomplete as-of the entry.

Price path: entry close 78,400; 180D MFE/MAE 14.03% / -43.18%; peak 2023-06-21 at 89,400; trough 2023-11-02 at 44,550.

### 8. 112610 CS Wind — Stage4B / one_time_price_increase_profit_surprise_high_mae_guardrail

Evidence URL: https://www.asiae.co.kr/en/article/2024081616033571936

Q2 2024 operating profit beat consensus by 221%, but the source identified one-time income from offshore-substructure price renegotiation after a Q1 loss-making OSS project; this needs 4B/high-MAE guardrail before Actionable/Yellow.

Price path: entry close 63,300; 180D MFE/MAE 16.11% / -52.53%; peak 2024-09-24 at 73,500; trough 2025-04-09 at 30,050.


## 6. Score / Return Alignment Stress Test

| Symbol | Trigger | Current calibrated proxy issue | Price-path result | Residual reading |
|---|---|---|---|---|
| 267270 | Stage2-Actionable | C01 positive evidence can over-focus on revenue growth without balance-sheet quality | 180D MFE 33.96%, MAE -13.77% | profitability + debt reduction is a valid second bridge, but not enough for Green without cash-conversion repetition |
| 267270 | Stage4B | weak annual result could be routed too hard to thesis break | 180D MFE 69.25%, MAE -21.16% | negative headline plus inventory reset and market-specific product plan is 4B/watch, not hard 4C |
| 042670 | Stage4B | segment offset may be ignored if headline OP falls | 180D MFE 18.96%, MAE -18.57% | construction equipment slump blocks Actionable, but engine margin/demand-recovery offset blocks hard 4C |
| 042670 | Stage4B | annual collapse can look like 4C | 180D MFE 143.03%, MAE -5.31% | ugly annual result with rebound guidance is a current-profile too-hard risk |
| 241560 | Stage2-Actionable | profit headline alone is not enough | 180D MFE 46.93%, MAE -11.79% | net-cash conversion is the missing second bridge that makes Actionable reasonable |
| 241560 | Stage4B | dealer inventory adjustment can be over-penalized | 180D MFE 95.24%, MAE -4.62% | production/inventory adjustment was 4B/watch; hard 4C needs cash/debt/order collapse |
| 112610 | Stage2 | order backlog can be mistaken for cashflow bridge | 180D MFE 14.03%, MAE -43.18% | backlog without working-capital/cash conversion stays Stage2 cap |
| 112610 | Stage4B | earnings surprise can be over-upgraded | 180D MFE 16.11%, MAE -52.53% | one-time price renegotiation/OSS income requires Green blocker and 4B watch |

## 7. Residual Contribution

```text
rule_candidate: C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE
sector_rule_candidate: L1_INDUSTRIAL_ORDER_SALES_TO_CASHFLOW_GATE

core residual:
- order/sales/backlog headline alone does not create Stage2-Actionable or Yellow in C01.
- Stage2-Actionable requires a direct second bridge: operating-margin conversion, net-cash/debt improvement, working-capital release, customer/dealer inventory normalization, or shipment/cash conversion.
- dealer inventory adjustment, high promotional cost, or one-time margin item should route to Stage4B/watch before hard 4C unless cash/debt/order collapse is confirmed.
- high forward MFE after ugly industrial-cycle results is a holdout warning against hard 4C stickiness.
- Stage3-Green remains blocked until cashflow/working-capital bridge repeats across more than one evidence family.
```

### Shadow weight note

```text
production_scoring_changed: false
shadow_weight_only: true
new_axis_proposed: false
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- hard_4c_confirmation
existing_axis_refined:
- C01 cashflow_or_net_cash_second_bridge requirement
- C01 dealer_inventory_adjustment_not_automatic_4c
existing_axis_weakened:
- none_global
```

## 8. Machine-Readable JSONL Trigger Rows

```jsonl
{"schema_version": "e2r_v12_trigger_row_v1", "row_id": "R1_L204_C01_267270_2024-02-06_Stage2_Actionable", "selected_round": "R1", "selected_loop": 204, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE", "symbol": "267270", "name": "HD Hyundai Construction Equipment", "evidence_date": "2024-02-06", "entry_date": "2024-02-06", "entry_rule": "same_day_close", "trigger_type": "Stage2-Actionable", "case_role": "direct_profitability_balance_sheet_bridge", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|267270|Stage2-Actionable|2024-02-06", "source_quality": "issuer_direct_press", "evidence_url": "https://www.hd.com/en/newsroom/media-hub/press/view?detailsKey=3255", "evidence_summary": "2023 revenue and operating profit rose, debt ratio improved, and profitability was explained by developed-market infrastructure demand, emerging-market mining demand, price increases, and fixed-cost leverage.", "price_source_validation": {"primary_price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267270/2024.csv", "actual_entry_ohlcv": {"d": "2024-02-06", "o": 55900.0, "h": 56000.0, "l": 52000.0, "c": 53000.0, "v": 784114.0, "a": 42051516000.0, "mc": 1044142029000.0, "s": 19700793.0, "m": "KOSPI"}, "entry_price": 53000.0, "mfe_mae_method": "entry close vs max high / min low over inclusive N-tradable-row windows", "mfe_30d_pct": 13.96, "mae_30d_pct": -5.28, "mfe_90d_pct": 13.96, "mae_90d_pct": -7.08, "mfe_180d_pct": 33.96, "mae_180d_pct": -13.77, "peak_180d_date": "2024-07-23", "peak_180d_price": 71000.0, "trough_180d_date": "2024-09-09", "trough_180d_price": 45700.0, "drawdown_after_peak_180d_pct": -35.63, "corporate_action_contamination_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true}, "score_simulation": {"eps_fcf_explosion": 13, "earnings_visibility": 16, "bottleneck_pricing": 8, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 9, "information_confidence": 9, "raw_total_proxy": 70, "stage3_green_blocked": true, "stage2_actionable_requires_second_bridge": true, "cashflow_or_working_capital_bridge_required_for_yellow": true}, "residual_contribution": {"label": "profitability_and_balance_sheet_second_bridge_positive_control", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_rule_candidate": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE"}}
{"schema_version": "e2r_v12_trigger_row_v1", "row_id": "R1_L204_C01_267270_2025-02-06_Stage4B", "selected_round": "R1", "selected_loop": 204, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE", "symbol": "267270", "name": "HD Hyundai Construction Equipment", "evidence_date": "2025-02-06", "entry_date": "2025-02-06", "entry_rule": "same_day_close", "trigger_type": "Stage4B", "case_role": "ugly_annual_result_but_inventory_reset_reopen_watch", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|267270|Stage4B|2025-02-06", "source_quality": "issuer_direct_press", "evidence_url": "https://www.hyundai-ce.com/en/media/newspress/view?detailsKey=2194", "evidence_summary": "2024 revenue and operating profit declined on sluggish global demand, competition, and promotional expenses, but the company cited India/Brazil growth, lower inventories, Ulsan modernization, and market-specific products as reopen offsets.", "price_source_validation": {"primary_price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/267/267270/2025.csv", "actual_entry_ohlcv": {"d": "2025-02-06", "o": 65800.0, "h": 71400.0, "l": 65600.0, "c": 70900.0, "v": 664753.0, "a": 46116853800.0, "mc": 1297866047400.0, "s": 18305586.0, "m": "KOSPI"}, "entry_price": 70900.0, "mfe_mae_method": "entry close vs max high / min low over inclusive N-tradable-row windows", "mfe_30d_pct": 29.06, "mae_30d_pct": -8.32, "mfe_90d_pct": 29.06, "mae_90d_pct": -21.16, "mfe_180d_pct": 69.25, "mae_180d_pct": -21.16, "peak_180d_date": "2025-10-29", "peak_180d_price": 120000.0, "trough_180d_date": "2025-04-09", "trough_180d_price": 55900.0, "drawdown_after_peak_180d_pct": -17.58, "corporate_action_contamination_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true}, "score_simulation": {"eps_fcf_explosion": 7, "earnings_visibility": 11, "bottleneck_pricing": 6, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 8, "information_confidence": 9, "raw_total_proxy": 55, "stage3_green_blocked": true, "stage2_actionable_requires_second_bridge": true, "cashflow_or_working_capital_bridge_required_for_yellow": true}, "residual_contribution": {"label": "negative_headline_with_inventory_reset_offset_should_be_4b_not_4c", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_rule_candidate": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE"}}
{"schema_version": "e2r_v12_trigger_row_v1", "row_id": "R1_L204_C01_042670_2024-04-19_Stage4B", "selected_round": "R1", "selected_loop": 204, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE", "symbol": "042670", "name": "HD Hyundai Infracore", "evidence_date": "2024-04-19", "entry_date": "2024-04-19", "entry_rule": "same_day_close", "trigger_type": "Stage4B", "case_role": "construction_equipment_slump_with_engine_offset_watch", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|042670|Stage4B|2024-04-19", "source_quality": "issuer_direct_press", "evidence_url": "https://www.hd.com/en/newsroom/media-hub/press/view?detailsKey=3235", "evidence_summary": "Q1 2024 sales and operating profit fell with construction-equipment market contraction, while the engine division kept a double-digit margin and management expected demand recovery in 2H24.", "price_source_validation": {"primary_price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv", "actual_entry_ohlcv": {"d": "2024-04-19", "o": 7640.0, "h": 7770.0, "l": 7470.0, "c": 7700.0, "v": 1607405.0, "a": 12216146110.0, "mc": 1536946588100.0, "s": 199603453.0, "m": "KOSPI"}, "entry_price": 7700.0, "mfe_mae_method": "entry close vs max high / min low over inclusive N-tradable-row windows", "mfe_30d_pct": 14.03, "mae_30d_pct": -2.99, "mfe_90d_pct": 18.96, "mae_90d_pct": -16.1, "mfe_180d_pct": 18.96, "mae_180d_pct": -18.57, "peak_180d_date": "2024-07-23", "peak_180d_price": 9160.0, "trough_180d_date": "2024-10-29", "trough_180d_price": 6270.0, "drawdown_after_peak_180d_pct": -31.55, "corporate_action_contamination_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true}, "score_simulation": {"eps_fcf_explosion": 6, "earnings_visibility": 10, "bottleneck_pricing": 6, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 5, "information_confidence": 9, "raw_total_proxy": 50, "stage3_green_blocked": true, "stage2_actionable_requires_second_bridge": true, "cashflow_or_working_capital_bridge_required_for_yellow": true}, "residual_contribution": {"label": "segment_offset_prevents_hard_4c_but_blocks_actionable", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_rule_candidate": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE"}}
{"schema_version": "e2r_v12_trigger_row_v1", "row_id": "R1_L204_C01_042670_2025-02-04_Stage4B", "selected_round": "R1", "selected_loop": 204, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE", "symbol": "042670", "name": "HD Hyundai Infracore", "evidence_date": "2025-02-04", "entry_date": "2025-02-04", "entry_rule": "same_day_close", "trigger_type": "Stage4B", "case_role": "annual_profit_collapse_with_turnaround_guidance_holdout", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|042670|Stage4B|2025-02-04", "source_quality": "direct_news_regulatory_result", "evidence_url": "https://www.asiae.co.kr/en/article/2025020417325562571", "evidence_summary": "2024 operating profit fell sharply and the construction-equipment division profit plunged, but management framed 2025 as an advanced-market rebound and infrastructure-investment recovery year.", "price_source_validation": {"primary_price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042670/2025.csv", "actual_entry_ohlcv": {"d": "2025-02-04", "o": 7200.0, "h": 7530.0, "l": 7130.0, "c": 7530.0, "v": 1701952.0, "a": 12537151320.0, "mc": 1450698678510.0, "s": 192655867.0, "m": "KOSPI"}, "entry_price": 7530.0, "mfe_mae_method": "entry close vs max high / min low over inclusive N-tradable-row windows", "mfe_30d_pct": 35.59, "mae_30d_pct": -5.31, "mfe_90d_pct": 65.34, "mae_90d_pct": -5.31, "mfe_180d_pct": 143.03, "mae_180d_pct": -5.31, "peak_180d_date": "2025-10-29", "peak_180d_price": 18300.0, "trough_180d_date": "2025-02-04", "trough_180d_price": 7130.0, "drawdown_after_peak_180d_pct": -7.76, "corporate_action_contamination_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true}, "score_simulation": {"eps_fcf_explosion": 5, "earnings_visibility": 9, "bottleneck_pricing": 5, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 5, "information_confidence": 8, "raw_total_proxy": 46, "stage3_green_blocked": true, "stage2_actionable_requires_second_bridge": true, "cashflow_or_working_capital_bridge_required_for_yellow": true}, "residual_contribution": {"label": "annual_collapse_but_reopen_guidance_high_mfe_4b_holdout", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_rule_candidate": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE"}}
{"schema_version": "e2r_v12_trigger_row_v1", "row_id": "R1_L204_C01_241560_2023-10-27_Stage2_Actionable", "selected_round": "R1", "selected_loop": 204, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE", "symbol": "241560", "name": "Doosan Bobcat", "evidence_date": "2023-10-27", "entry_date": "2023-10-27", "entry_rule": "same_day_close", "trigger_type": "Stage2-Actionable", "case_role": "net_cash_and_profit_bridge_positive_control", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|241560|Stage2-Actionable|2023-10-27", "source_quality": "issuer_direct_press", "evidence_url": "https://www.doosanbobcat.com/en/mediacenter/news/detail?id=250&page=3&pageSize=10", "evidence_summary": "Q3 2023 cumulative operating profit exceeded the prior full-year level and Doosan Bobcat converted net debt to net cash through stable cash flow.", "price_source_validation": {"primary_price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241560/2023.csv", "actual_entry_ohlcv": {"d": "2023-10-27", "o": 43700.0, "h": 43900.0, "l": 42150.0, "c": 42400.0, "v": 414070.0, "a": 17688650100.0, "mc": 4250564638400.0, "s": 100249166.0, "m": "KOSPI"}, "entry_price": 42400.0, "mfe_mae_method": "entry close vs max high / min low over inclusive N-tradable-row windows", "mfe_30d_pct": 8.73, "mae_30d_pct": -11.79, "mfe_90d_pct": 23.82, "mae_90d_pct": -11.79, "mfe_180d_pct": 46.93, "mae_180d_pct": -11.79, "peak_180d_date": "2024-05-27", "peak_180d_price": 62300.0, "trough_180d_date": "2023-11-01", "trough_180d_price": 37400.0, "drawdown_after_peak_180d_pct": -23.11, "corporate_action_contamination_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true}, "score_simulation": {"eps_fcf_explosion": 14, "earnings_visibility": 15, "bottleneck_pricing": 8, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 10, "information_confidence": 9, "raw_total_proxy": 71, "stage3_green_blocked": true, "stage2_actionable_requires_second_bridge": true, "cashflow_or_working_capital_bridge_required_for_yellow": true}, "residual_contribution": {"label": "cash_conversion_second_bridge_allows_actionable", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_rule_candidate": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE"}}
{"schema_version": "e2r_v12_trigger_row_v1", "row_id": "R1_L204_C01_241560_2024-10-28_Stage4B", "selected_round": "R1", "selected_loop": 204, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE", "symbol": "241560", "name": "Doosan Bobcat", "evidence_date": "2024-10-28", "entry_date": "2024-10-28", "entry_rule": "same_day_close", "trigger_type": "Stage4B", "case_role": "dealer_inventory_adjustment_4b_not_4c", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|241560|Stage4B|2024-10-28", "source_quality": "issuer_direct_press", "evidence_url": "https://www.doosanbobcat.com/en/mediacenter/news/detail?id=281&page=1&pageSize=10", "evidence_summary": "Q3 2024 revenue fell 28% and operating profit dropped 59% because of dealer inventory adjustment and fixed-cost burden from production cuts; this is a 4B watch unless cash/debt/order collapse is confirmed.", "price_source_validation": {"primary_price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv", "actual_entry_ohlcv": {"d": "2024-10-28", "o": 38100.0, "h": 38100.0, "l": 37250.0, "c": 37850.0, "v": 353720.0, "a": 13296174400.0, "mc": 3794430933100.0, "s": 100249166.0, "m": "KOSPI"}, "entry_price": 37850.0, "mfe_mae_method": "entry close vs max high / min low over inclusive N-tradable-row windows", "mfe_30d_pct": 19.68, "mae_30d_pct": -4.62, "mfe_90d_pct": 41.08, "mae_90d_pct": -4.62, "mfe_180d_pct": 95.24, "mae_180d_pct": -4.62, "peak_180d_date": "2025-06-24", "peak_180d_price": 73900.0, "trough_180d_date": "2024-10-29", "trough_180d_price": 36100.0, "drawdown_after_peak_180d_pct": -28.55, "corporate_action_contamination_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true}, "score_simulation": {"eps_fcf_explosion": 5, "earnings_visibility": 9, "bottleneck_pricing": 5, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 7, "information_confidence": 9, "raw_total_proxy": 49, "stage3_green_blocked": true, "stage2_actionable_requires_second_bridge": true, "cashflow_or_working_capital_bridge_required_for_yellow": true}, "residual_contribution": {"label": "dealer_inventory_adjustment_high_mfe_reopen_not_hard_4c", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_rule_candidate": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE"}}
{"schema_version": "e2r_v12_trigger_row_v1", "row_id": "R1_L204_C01_112610_2023-05-15_Stage2", "selected_round": "R1", "selected_loop": 204, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE", "symbol": "112610", "name": "CS Wind", "evidence_date": "2023-05-15", "entry_date": "2023-05-15", "entry_rule": "same_day_close", "trigger_type": "Stage2", "case_role": "order_backlog_positive_but_cashflow_missing_guardrail", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|112610|Stage2|2023-05-15", "source_quality": "issuer_direct_pdf_indexed", "evidence_url": "https://www.cswind.com/en/board/board.download/?n=455&seq=1&t=common", "evidence_summary": "Indexed issuer 1Q23 earnings release indicated order backlog around USD 736m and surplus conversion, but cash/working-capital and durable margin proof were still incomplete as-of the entry.", "price_source_validation": {"primary_price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112610/2023.csv", "actual_entry_ohlcv": {"d": "2023-05-15", "o": 78100.0, "h": 82500.0, "l": 77500.0, "c": 78400.0, "v": 1059683.0, "a": 84542963200.0, "mc": 3306237995200.0, "s": 42171403.0, "m": "KOSPI"}, "entry_price": 78400.0, "mfe_mae_method": "entry close vs max high / min low over inclusive N-tradable-row windows", "mfe_30d_pct": 14.03, "mae_30d_pct": -3.83, "mfe_90d_pct": 14.03, "mae_90d_pct": -28.32, "mfe_180d_pct": 14.03, "mae_180d_pct": -43.18, "peak_180d_date": "2023-06-21", "peak_180d_price": 89400.0, "trough_180d_date": "2023-11-02", "trough_180d_price": 44550.0, "drawdown_after_peak_180d_pct": -50.17, "corporate_action_contamination_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true}, "score_simulation": {"eps_fcf_explosion": 9, "earnings_visibility": 12, "bottleneck_pricing": 8, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 4, "information_confidence": 7, "raw_total_proxy": 55, "stage3_green_blocked": true, "stage2_actionable_requires_second_bridge": true, "cashflow_or_working_capital_bridge_required_for_yellow": true}, "residual_contribution": {"label": "backlog_without_cash_conversion_high_mae_stage2_cap", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_rule_candidate": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE"}}
{"schema_version": "e2r_v12_trigger_row_v1", "row_id": "R1_L204_C01_112610_2024-08-19_Stage4B", "selected_round": "R1", "selected_loop": 204, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE", "symbol": "112610", "name": "CS Wind", "evidence_date": "2024-08-19", "entry_date": "2024-08-19", "entry_rule": "same_day_close", "trigger_type": "Stage4B", "case_role": "one_time_price_increase_profit_surprise_high_mae_guardrail", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|112610|Stage4B|2024-08-19", "source_quality": "direct_news_earnings_detail", "evidence_url": "https://www.asiae.co.kr/en/article/2024081616033571936", "evidence_summary": "Q2 2024 operating profit beat consensus by 221%, but the source identified one-time income from offshore-substructure price renegotiation after a Q1 loss-making OSS project; this needs 4B/high-MAE guardrail before Actionable/Yellow.", "price_source_validation": {"primary_price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112610/2024.csv", "actual_entry_ohlcv": {"d": "2024-08-19", "o": 66100.0, "h": 66100.0, "l": 62500.0, "c": 63300.0, "v": 901700.0, "a": 57617759200.0, "mc": 2669449809900.0, "s": 42171403.0, "m": "KOSPI"}, "entry_price": 63300.0, "mfe_mae_method": "entry close vs max high / min low over inclusive N-tradable-row windows", "mfe_30d_pct": 16.11, "mae_30d_pct": -13.11, "mfe_90d_pct": 16.11, "mae_90d_pct": -41.23, "mfe_180d_pct": 16.11, "mae_180d_pct": -52.53, "peak_180d_date": "2024-09-24", "peak_180d_price": 73500.0, "trough_180d_date": "2025-04-09", "trough_180d_price": 30050.0, "drawdown_after_peak_180d_pct": -59.12, "corporate_action_contamination_180d": false, "insufficient_forward_window_180d": false, "calibration_usable": true}, "score_simulation": {"eps_fcf_explosion": 10, "earnings_visibility": 10, "bottleneck_pricing": 7, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 4, "information_confidence": 7, "raw_total_proxy": 53, "stage3_green_blocked": true, "stage2_actionable_requires_second_bridge": true, "cashflow_or_working_capital_bridge_required_for_yellow": true}, "residual_contribution": {"label": "earnings_surprise_one_time_income_should_not_be_green", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_rule_candidate": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE"}}
```

## 9. Aggregate Rows

```json
{
  "schema_version": "e2r_v12_aggregate_v1",
  "selected_round": "R1",
  "selected_loop": 204,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE",
  "new_independent_case_count": 8,
  "new_independent_trigger_count": 8,
  "unique_symbol_count": 4,
  "stage2_count": 1,
  "stage2_actionable_count": 3,
  "stage4b_count": 4,
  "stage4c_count": 0,
  "positive_or_reopen_case_count": 4,
  "counterexample_or_guardrail_case_count": 4,
  "current_profile_error_count": 6,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "corporate_action_contaminated_180D_count": 0,
  "insufficient_forward_window_180D_count": 0,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "ready_for_batch_ingest": true
}
```

## 10. Batch Ingest Self-Audit

```text
standard_filename_regex_pass: true
selected_round_large_sector_consistency_pass: true
canonical_archetype_present: true
fine_archetype_maps_to_canonical: true
hard_duplicate_key_present_for_each_row: true
actual_stock_web_1D_OHLC_present_for_each_row: true
entry_price_present_for_each_row: true
MFE_MAE_30_90_180_present_for_each_row: true
peak_trough_present_for_each_row: true
corporate_action_contamination_checked: true
insufficient_forward_window_checked: true
source_url_present_for_each_row: true
jsonl_rows_present_for_each_usable_trigger: true
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When batch-applying v12 calibration MDs later, parse this file as a standard v12 result MD.
Use only calibration_usable=true trigger rows.
Do not treat this MD as a production scoring patch by itself.
Evaluate whether C01_ORDER_BACKLOG_MARGIN_BRIDGE needs an archetype-specific rule candidate:
C01_CONSTRUCTION_EQUIPMENT_NET_CASH_DEALER_INVENTORY_CASHFLOW_GATE.

Candidate logic to evaluate:
- Require direct second bridge for Stage2-Actionable in C01: operating-margin conversion, net-cash/debt improvement, working-capital release, dealer/customer inventory normalization, or shipment/cash conversion.
- Keep Stage3-Green blocked until cashflow/working-capital evidence is repeated across multiple evidence families.
- Route dealer inventory adjustment, promotional-cost burden, or one-time margin items to Stage4B/watch before hard 4C unless cash/debt/order collapse is confirmed.
- Do not loosen global Stage3-Green thresholds.
```

## 12. Next Research State

```text
completed_round: R1
completed_loop: 204
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority_1_balance_reinforcement_after_all_C01_C32_above_80_rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
