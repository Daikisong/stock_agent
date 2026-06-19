# E2R Stock-Web v12 Residual Research — R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C05_EPC_MEGA_CONTRACT_MARGIN_GAP

```text
research_file = e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
selected_round = R1
selected_loop = 208
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance-quality reinforcement / C05 margin-working-capital failure + 4C timing repair
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = C05_ORDER_HEADLINE_MARGIN_CASHFLOW_AND_KITCHEN_SINK_4C_GUARD
round_schedule_status = coverage_index_selected_after_R4_loop_72_C15; strict R1~R13 sequential scheduler not used in this mode
round_sector_consistency = pass
price_source = Songdaiki/stock-web / atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Execution-mode compliance
- Mode: historical trigger-level sector/archetype residual calibration after the Stock-Web OHLC atlas breakthrough.
- This is not a live scan, not current-stock discovery, not order execution, and not an auto-trading instruction.
- No `stock_agent` production code was opened, edited, or patched. All proposed effects are shadow-only batch-research candidates.
- The No-Repeat Index was used only as a duplicate/coverage ledger. It was not treated as a source of price data.

## 1. Coverage-index selection rationale
The coverage ledger is past the old 80-row fill problem. The remaining problem is not volume; it is whether the batch can tell a real EPC margin conversion story from a shiny order headline. C05 remains Priority 1 because it still needs margin / working-capital failure counterexamples and 4C timing reinforcement. The previous local artifact was R4 / C15, so this run deliberately rotates into R1 / C05 rather than repeating the just-completed C15 residual.

C05 is the EPC version of a restaurant with a full reservation book: the headline says every table is booked, but the trade works only if ingredients do not explode in cost, customers actually pay, and the kitchen can serve without wasting the margin. The residual we are trying to isolate is the gap between **order/backlog optics** and **cash-margin reality**.

| check | result |
| --- | --- |
| strict sequential R1~R13 required | false / coverage-index priority mode |
| selected archetype drives round | true |
| selected_round | R1 |
| selected large sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| selected canonical | C05_EPC_MEGA_CONTRACT_MARGIN_GAP |
| latest local loop seen for R1/C05 | 207 |
| selected_loop for this file | 208 |
| hard duplicate collisions | 0 exact duplicate keys within this run |


## 2. Stock-Web manifest / schema validation
```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_data_source": "Songdaiki/stock-web",
  "price_data_repo": "https://github.com/Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "manifest_min_date": "1995-05-02",
  "manifest_max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "corporate_action_candidate_count": 14435,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```
Schema basis used in every trigger row: tradable shard columns `d,o,h,l,c,v,a,mc,s,m`; raw/unadjusted marcap basis; MFE is max high from entry date through N forward tradable rows divided by entry close minus one; MAE is min low from entry date through N forward tradable rows divided by entry close minus one. A 180-trading-day forward window is required for calibration usability.

## 3. Price-source files used
| symbol | company | profile path | tradable year files checked |
| --- | --- | --- | --- |
| 000720 | Hyundai E&C / 현대건설 | atlas/symbol_profiles/000/000720.json | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv, atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv, atlas/ohlcv_tradable_by_symbol_year/000/000720/2026.csv |
| 006360 | GS E&C / GS건설 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv, atlas/ohlcv_tradable_by_symbol_year/006/006360/2025.csv, atlas/ohlcv_tradable_by_symbol_year/006/006360/2026.csv |
| 028050 | Samsung E&A / 삼성E&A | atlas/symbol_profiles/028/028050.json | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv, atlas/ohlcv_tradable_by_symbol_year/028/028050/2025.csv, atlas/ohlcv_tradable_by_symbol_year/028/028050/2026.csv |


## 4. Profile / corporate-action audit
| symbol | company | first | last | trading days | selected entry dates | corporate-action candidate dates | D~D+180 contamination |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 028050 | Samsung E&A / 삼성E&A | 1997-01-03 | 2026-02-20 | 7265 | 2024-01-31 | 1997-08-22, 1999-01-13, 1999-05-26, 1999-09-29, 2016-02-26 | false for all selected D~D+180 windows |
| 006360 | GS E&C / GS건설 | 1995-05-02 | 2026-02-20 | 7761 | 2024-04-03 | 1999-05-07, 1999-12-01, 2014-06-25 | false for all selected D~D+180 windows |
| 000720 | Hyundai E&C / 현대건설 | 1995-05-02 | 2026-02-20 | 7740 | 2024-04-19, 2024-07-19, 2025-01-22 | 1998-05-23, 1998-11-19, 1999-03-05, 2001-07-06, 2001-07-12, 2004-01-13, 2004-04-07 | false for all selected D~D+180 windows |


## 5. Duplicate and no-repeat ledger
| trigger_id | duplicate key | treatment |
| --- | --- | --- |
| C05_L208_T001_028050_STAGE3_GREEN_20240130 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage3-Green|2024-01-31 | calibration-usable; exact key not repeated within this run; dedupe_for_aggregate=true |
| C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-03 | calibration-usable; exact key not repeated within this run; dedupe_for_aggregate=true |
| C05_L208_T003_000720_STAGE3_YELLOW_20240419 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage3-Yellow|2024-04-19 | calibration-usable; exact key not repeated within this run; dedupe_for_aggregate=true |
| C05_L208_T004_000720_STAGE4B_20240719 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2024-07-19 | calibration-usable; exact key not repeated within this run; dedupe_for_aggregate=true |
| C05_L208_T005_000720_STAGE4C_20250122 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4C|2025-01-22 | calibration-usable; exact key not repeated within this run; dedupe_for_aggregate=true |


## 6. Archetype residual problem statement
C05 is not asking whether the contract is large. It asks whether the contract can survive the long corridor from order announcement to profit recognition. The corridor has four gates: customer quality, execution scope, cost-rate discipline, and working-capital conversion. A headline can pass the first gate while still bleeding at the third and fourth gates. That is why C05 needs more than “mega order + sales growth.” It needs a bridge from backlog to operating profit and then from operating profit to cash.

This run therefore tests five C05 residual shapes:
1. Green-looking annual result that later decays when freshness disappears.
2. Fresh Aramco package headline that works as Stage2 but still lacks margin proof.
3. Q1 profit beat that later fails when raw-material and quality costs arrive.
4. Q2 cost-rate miss that deserves a local 4B watch but not an automatic full exclusion.
5. Severe annual/Q4 loss that looks like hard 4C but behaves like a kitchen-sink reset with a huge rebound.

## 7. Case universe summary
| case_id | symbol | company | trigger_date | entry_date | trigger_type | role | 90D MFE/MAE | 180D MFE/MAE | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_L208_01_SAMSUNG_EA_2023_RESULT_GUIDANCE_LATE_FADE | 028050 | Samsung E&A / 삼성E&A | 2024-01-30 | 2024-01-31 | Stage3-Green | local_positive_late_fade_guardrail | 26.23 / -0.22 | 31.39 / -18.48 | early_positive_then_180D_late_fade |
| C05_L208_02_GS_EC_FADHILI_PACKAGE2_POSITIVE | 006360 | GS E&C / GS건설 | 2024-04-03 | 2024-04-03 | Stage2-Actionable | positive_contract_with_customer_quality_and_event_freshness | 30.52 / -10.17 | 39.16 / -10.17 | positive_MFE180_with_manageable_MAE |
| C05_L208_03_HYUNDAI_EC_Q1_BEAT_COST_RATE_LATE_FAIL | 000720 | Hyundai E&C / 현대건설 | 2024-04-19 | 2024-04-19 | Stage3-Yellow | counterexample_revenue_profit_beat_without_durable_cash_margin_bridge | 8.27 / -12.63 | 8.27 / -27.52 | late_counterexample_MAE180_dominates |
| C05_L208_04_HYUNDAI_EC_Q2_RAW_MATERIAL_COST_4B | 000720 | Hyundai E&C / 현대건설 | 2024-07-19 | 2024-07-19 | Stage4B | local_4B_cost_rate_guardrail_with_later_rebound | 4.75 / -16.87 | 21.78 / -26.07 | 4B_correct_early_but_not_hard_exit |
| C05_L208_05_HYUNDAI_EC_2024_LOSS_HARD4C_FALSE_NEGATIVE | 000720 | Hyundai E&C / 현대건설 | 2025-01-22 | 2025-01-22 | Stage4C | hard4C_timing_false_negative_kitchen_sink_reversal | 160.11 / -9.14 | 199.12 / -9.14 | positive_after_4C_signal |


## 8. Evidence-source map
| trigger_id | evidence URL | compressed evidence |
| --- | --- | --- |
| C05_L208_T001_028050_STAGE3_GREEN_20240130 | https://www.samsungena.com/en/newsroom/news/view?idx=15585 | 2023 annual operating profit KRW 993.1B (+41.3% YoY), revenue KRW 10.6T, backlog/order guidance, and KRW 370B future-technology investment. |
| C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 | https://www.asiae.co.kr/en/article/2024040309065572598 | GS E&C won Saudi Aramco Fadhili Gas Increment Program Package 2 sulfur-recovery facility contract, about USD 1.22B / KRW 1.6T, 41-month construction period. |
| C05_L208_T003_000720_STAGE3_YELLOW_20240419 | https://en.yna.co.kr/view/AEN20240419005652320 | Q1 2024 net profit +38.4% YoY, operating profit +44.6% to KRW 250.9B, revenue +41.7% to KRW 8.55T, and OP beat consensus. |
| C05_L208_T004_000720_STAGE4B_20240719 | https://en.yna.co.kr/view/AEN20240719004551320 | Q2 net income -31.2%, operating profit -34.1%, sales +20.4%; miss versus analyst estimate; company cited raw-material price rise and quality/safety expenses. |
| C05_L208_T005_000720_STAGE4C_20250122 | https://en.yna.co.kr/view/AEN20250122006251320 | Hyundai E&C swung to a Q4 operating loss and full-year 2024 net loss; weak won, raw-material costs, and affiliate one-off project costs weighed, while 2024 orders still exceeded target. |


## 9. Trigger-level actual OHLC at entry
| trigger_id | price_path | entry_date | entry_price | o | h | l | c | v | amount | market_cap | shares | market |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_L208_T001_028050_STAGE3_GREEN_20240130 | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv | 2024-01-31 | 22300.00 | 24500.00 | 24600.00 | 22250.00 | 22300.00 | 3158972 | 71745804000 | 4370800000000 | 196000000 | KOSPI |
| C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv | 2024-04-03 | 15630.00 | 15500.00 | 16550.00 | 15400.00 | 15630.00 | 4065591 | 64698222680 | 1337638688700 | 85581490 | KOSPI |
| C05_L208_T003_000720_STAGE3_YELLOW_20240419 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv | 2024-04-19 | 33250.00 | 32000.00 | 33450.00 | 31600.00 | 33250.00 | 727477 | 23799312600 | 3702579186250 | 111355765 | KOSPI |
| C05_L208_T004_000720_STAGE4B_20240719 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv | 2024-07-19 | 32600.00 | 33100.00 | 33100.00 | 32450.00 | 32600.00 | 775289 | 25298546100 | 3630197939000 | 111355765 | KOSPI |
| C05_L208_T005_000720_STAGE4C_20250122 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv | 2025-01-22 | 28450.00 | 26200.00 | 28450.00 | 25850.00 | 28450.00 | 3258966 | 90189685850 | 3168071514250 | 111355765 | KOSPI |


## 10. Trigger-level MFE / MAE matrix
| trigger_id | entry | MFE30 | MAE30 | 30D end | MFE90 | MAE90 | 90D end | MFE180 | MAE180 | 180D end | peak date | peak price | drawdown after peak | dd low date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_L208_T001_028050_STAGE3_GREEN_20240130 | 22300.00 | 26.23 | -0.22 | 2024-03-15 | 26.23 | -0.22 | 2024-06-14 | 31.39 | -18.48 | 2024-10-29 | 2024-07-30 | 29300.00 | -37.95 | 2024-10-25 |
| C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 | 15630.00 | 6.97 | -10.17 | 2024-05-20 | 30.52 | -10.17 | 2024-08-13 | 39.16 | -10.17 | 2024-12-27 | 2024-08-27 | 21750.00 | -22.48 | 2024-11-13 |
| C05_L208_T003_000720_STAGE3_YELLOW_20240419 | 33250.00 | 8.27 | -4.96 | 2024-06-04 | 8.27 | -12.63 | 2024-08-29 | 8.27 | -27.52 | 2025-01-15 | 2024-05-09 | 36000.00 | -33.06 | 2024-12-09 |
| C05_L208_T004_000720_STAGE4B_20240719 | 32600.00 | 4.75 | -10.89 | 2024-08-30 | 4.75 | -16.87 | 2024-12-02 | 21.78 | -26.07 | 2025-04-17 | 2025-04-15 | 39700.00 | -3.78 | 2025-04-17 |
| C05_L208_T005_000720_STAGE4C_20250122 | 28450.00 | 31.99 | -9.14 | 2025-03-11 | 160.11 | -9.14 | 2025-06-10 | 199.12 | -9.14 | 2025-10-22 | 2025-06-25 | 85100.00 | -36.43 | 2025-09-30 |


## 11. Case-by-case interpretation
### C05_L208_T001_028050_STAGE3_GREEN_20240130 — Samsung E&A / 삼성E&A
- Trigger / entry: 2024-01-30 / 2024-01-31 at close 22300.
- Evidence: 2023 annual operating profit KRW 993.1B (+41.3% YoY), revenue KRW 10.6T, backlog/order guidance, and KRW 370B future-technology investment.
- Price path: 30D 26.23 / -0.22, 90D 26.23 / -0.22, 180D 31.39 / -18.48. Peak 2024-07-30 at 29300; post-peak drawdown -37.95%.
- Current profile read: would often remain Stage3-Green because revision/annual-result evidence is high; that misses late margin-cycle decay without fresh cash-conversion confirmation.
- Proposed shadow read: Stage3-Yellow after initial green, with full-4B watch if no fresh margin/working-capital bridge appears before the peak fades.

### C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 — GS E&C / GS건설
- Trigger / entry: 2024-04-03 / 2024-04-03 at close 15630.
- Evidence: GS E&C won Saudi Aramco Fadhili Gas Increment Program Package 2 sulfur-recovery facility contract, about USD 1.22B / KRW 1.6T, 41-month construction period.
- Price path: 30D 6.97 / -10.17, 90D 30.52 / -10.17, 180D 39.16 / -10.17. Peak 2024-08-27 at 21750; post-peak drawdown -22.48%.
- Current profile read: Stage2-Actionable works; should not be promoted to Green unless margin and working-capital conversion later confirm.
- Proposed shadow read: keep Stage2-Actionable with positive watch; promote only after margin/cash bridge.

### C05_L208_T003_000720_STAGE3_YELLOW_20240419 — Hyundai E&C / 현대건설
- Trigger / entry: 2024-04-19 / 2024-04-19 at close 33250.
- Evidence: Q1 2024 net profit +38.4% YoY, operating profit +44.6% to KRW 250.9B, revenue +41.7% to KRW 8.55T, and OP beat consensus.
- Price path: 30D 8.27 / -4.96, 90D 8.27 / -12.63, 180D 8.27 / -27.52. Peak 2024-05-09 at 36000; post-peak drawdown -33.06%.
- Current profile read: near-Green if profit beat and revenue growth receive too much weight.
- Proposed shadow read: cap at Stage3-Yellow unless cost-rate and working-capital confirmation survives the next reporting cycle.

### C05_L208_T004_000720_STAGE4B_20240719 — Hyundai E&C / 현대건설
- Trigger / entry: 2024-07-19 / 2024-07-19 at close 32600.
- Evidence: Q2 net income -31.2%, operating profit -34.1%, sales +20.4%; miss versus analyst estimate; company cited raw-material price rise and quality/safety expenses.
- Price path: 30D 4.75 / -10.89, 90D 4.75 / -16.87, 180D 21.78 / -26.07. Peak 2025-04-15 at 39700; post-peak drawdown -3.78%.
- Current profile read: full_4B may be too harsh if it ignores backlog resilience and later kitchen-sink clearing.
- Proposed shadow read: local 4B only; full 4B requires repeated cost-rate misses or cash-flow impairment.

### C05_L208_T005_000720_STAGE4C_20250122 — Hyundai E&C / 현대건설
- Trigger / entry: 2025-01-22 / 2025-01-22 at close 28450.
- Evidence: Hyundai E&C swung to a Q4 operating loss and full-year 2024 net loss; weak won, raw-material costs, and affiliate one-off project costs weighed, while 2024 orders still exceeded target.
- Price path: 30D 31.99 / -9.14, 90D 160.11 / -9.14, 180D 199.12 / -9.14. Peak 2025-06-25 at 85100; post-peak drawdown -36.43%.
- Current profile read: hard_4c_thesis_break_routes_to_4c would over-route if it treats all one-off/project-loss recognition as permanent thesis death.
- Proposed shadow read: route to 4C only if loss is paired with backlog collapse, liquidity stress, repeated receivable impairment, or customer/legal break; otherwise Stage4B/contrarian watch.

## 12. Current calibrated-profile stress test
The current v12 profile is good at preventing pure price-only blowoff from passing and at routing hard thesis breaks into 4C. The C05 residual shows the places where that logic still needs finer gears: the batch must not over-promote one good profit beat into Green, and it must not treat every one-off construction loss as permanent 4C if backlog and balance-sheet context remain alive.
| trigger_id | current trigger | score_before | score_after_shadow | current_profile_error | why current misreads / passes | shadow correction |
| --- | --- | --- | --- | --- | --- | --- |
| C05_L208_T001_028050_STAGE3_GREEN_20240130 | Stage3-Green | 89.00 | 80.00 | True | would often remain Stage3-Green because revision/annual-result evidence is high; that misses late margin-cycle decay without fresh cash-conversion confirmation. | Stage3-Yellow after initial green, with full-4B watch if no fresh margin/working-capital bridge appears before the peak fades. |
| C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 | Stage2-Actionable | 77.00 | 78.50 | False | Stage2-Actionable works; should not be promoted to Green unless margin and working-capital conversion later confirm. | keep Stage2-Actionable with positive watch; promote only after margin/cash bridge. |
| C05_L208_T003_000720_STAGE3_YELLOW_20240419 | Stage3-Yellow | 83.00 | 72.50 | True | near-Green if profit beat and revenue growth receive too much weight. | cap at Stage3-Yellow unless cost-rate and working-capital confirmation survives the next reporting cycle. |
| C05_L208_T004_000720_STAGE4B_20240719 | Stage4B | 61.00 | 58.00 | False | full_4B may be too harsh if it ignores backlog resilience and later kitchen-sink clearing. | local 4B only; full 4B requires repeated cost-rate misses or cash-flow impairment. |
| C05_L208_T005_000720_STAGE4C_20250122 | Stage4C | 42.00 | 61.50 | True | hard_4c_thesis_break_routes_to_4c would over-route if it treats all one-off/project-loss recognition as permanent thesis death. | route to 4C only if loss is paired with backlog collapse, liquidity stress, repeated receivable impairment, or customer/legal break; otherwise Stage4B/contrarian watch. |


## 13. Stage2 / Stage3 decision audit
| trigger_id | trigger_type | decision |
| --- | --- | --- |
| C05_L208_T001_028050_STAGE3_GREEN_20240130 | Stage3-Green | Initial Green must decay to Yellow/4B watch if no fresh margin-cash evidence appears. |
| C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 | Stage2-Actionable | Stage2-Actionable retained; no Green without margin bridge. |
| C05_L208_T003_000720_STAGE3_YELLOW_20240419 | Stage3-Yellow | Yellow cap correct; profit beat alone cannot cross Green threshold. |
| C05_L208_T004_000720_STAGE4B_20240719 | Stage4B | Not a Stage2/3 promotion row. |
| C05_L208_T005_000720_STAGE4C_20250122 | Stage4C | Not a Stage2/3 promotion row. |


## 14. Stage4B audit
Stage4B should behave like a speed bump, not a cliff. In C05, local 4B is justified by non-price evidence such as raw-material cost pressure, OP miss, quality/safety expense, receivable stress, or project-loss recognition. Full-window 4B needs persistence: repeated misses, cash-flow damage, or a customer/legal break.
| trigger_id | local_4B_relevant | evidence basis | full-window rule |
| --- | --- | --- | --- |
| C05_L208_T001_028050_STAGE3_GREEN_20240130 | True | non-price evidence present | full 4B only if repeated cost/cash impairment appears |
| C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 | False | not primary 4B row | full 4B only if repeated cost/cash impairment appears |
| C05_L208_T003_000720_STAGE3_YELLOW_20240419 | False | not primary 4B row | full 4B only if repeated cost/cash impairment appears |
| C05_L208_T004_000720_STAGE4B_20240719 | True | non-price evidence present | full 4B only if repeated cost/cash impairment appears |
| C05_L208_T005_000720_STAGE4C_20250122 | False | not primary 4B row | full 4B only if repeated cost/cash impairment appears |


## 15. Stage4C audit
Hard 4C remains necessary for genuine thesis death. The new nuance is that a kitchen-sink loss in a backlog-heavy contractor can be a reset rather than a terminal wound. The model should require more than a single red quarter: backlog collapse, liquidity/receivable stress, repeated project losses, legal/customer break, or dilution risk should accompany the 4C route.
| trigger_id | hard_4C_relevant | observed outcome | rule consequence |
| --- | --- | --- | --- |
| C05_L208_T001_028050_STAGE3_GREEN_20240130 | False | early_positive_then_180D_late_fade | not a hard-4C row |
| C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403 | False | positive_MFE180_with_manageable_MAE | not a hard-4C row |
| C05_L208_T003_000720_STAGE3_YELLOW_20240419 | False | late_counterexample_MAE180_dominates | not a hard-4C row |
| C05_L208_T004_000720_STAGE4B_20240719 | False | 4B_correct_early_but_not_hard_exit | not a hard-4C row |
| C05_L208_T005_000720_STAGE4C_20250122 | True | positive_after_4C_signal | qualify hard 4C with backlog/liquidity/project-loss persistence |


## 16. Positive / counterexample balance
| bucket | count | members |
| --- | --- | --- |
| positive / constructive | 2 | T002 GS E&C Fadhili; T005 Hyundai E&C kitchen-sink rebound |
| counterexample / guardrail | 3 | T001 Samsung E&A late fade; T003 Hyundai Q1 beat late fail; T004 Hyundai Q2 4B timing guard |
| current profile errors | 3 | T001, T003, T005 |


## 17. Sector-specific rule candidate
**L1 / EPC shadow rule candidate:** in industrial-infra EPC, order/backlog/revenue evidence should be discounted unless the evidence also contains a bridge to cost-rate control and working-capital conversion. A high-quality customer or named package can make a Stage2-Actionable row valid, but Stage3-Green should require either realized OP-margin improvement, explicit cost pass-through / reimbursable structure, or clean follow-through in cash-flow and receivables.

## 18. Canonical archetype rule candidate
**C05 shadow rule candidate:** introduce a two-sided timing guard.

- **Green decay guard:** annual result / profit beat / order headline can open Green only if the margin bridge is fresh. If the next evidence cycle introduces raw-material, quality, safety, receivable, or affiliate-project cost pressure, Green decays to Yellow or local 4B.
- **Kitchen-sink 4C guard:** a severe one-off loss routes to hard 4C only when paired with backlog collapse, liquidity stress, repeated cash-flow damage, legal/customer break, or dilution risk. If backlog is intact and the loss looks like a reset, route to Stage4B/contrarian watch rather than permanent thesis death.

## 19. Shadow weight calibration
| feature | current behavior | shadow delta | reason |
| --- | --- | --- | --- |
| c05_contract_headline_raw_size | over-promotes large orders | -0.6 | T001/T003 show headline or beat can decay without cash conversion |
| c05_customer_quality_named_package | under-counts Aramco-type package quality | +0.4 | T002 positive despite no immediate margin bridge |
| c05_margin_cash_bridge_required_for_green | too weak | +1.0 gate / cap | Green requires OP-margin + FCF/receivable confirmation |
| c05_cost_rate_working_capital_penalty | too weak | -1.2 | T003/T004 show raw-material/quality costs dominate later price path |
| c05_kitchen_sink_loss_reversal_guard | missing | +1.1 rescue from hard4C | T005 shows hard4C false negative when loss is reset-like |
| full_4b_requires_non_price_evidence | already present; strengthen for C05 | +0.5 enforcement | 4B should be based on OP miss, cost pressure, cash stress, not price alone |


## 20. Before / after backtest comparison
| metric | before profile read | after shadow read |
| --- | --- | --- |
| representative trigger count | 5 | 5 |
| avg MFE30 / MAE30 | 15.64 / -7.08 | 15.64 / -7.08 |
| avg MFE90 / MAE90 | 45.98 / -9.81 | 45.98 / -9.81 |
| avg MFE180 / MAE180 | 59.94 / -18.28 | 59.94 / -18.28 |
| green-like overpromotion errors | 2: T001/T003 | reduced by margin-cash freshness gate |
| hard4C false negative | 1: T005 | reduced by kitchen-sink/recovery guard |
| 4B timing ambiguity | 1: T004 | local 4B retained, full 4B delayed until persistent impairment |


## 21. Score-return alignment notes
A simple score cannot carry C05 alone because the same bad-looking evidence can either be terminal thesis death or the final clearing print. The alignment fix is not just a numeric penalty. It is a state machine: order headline → margin bridge → working-capital bridge → cost-rate persistence → 4B/4C timing.

## 22. Coverage matrix
| axis | coverage |
| --- | --- |
| symbols | 028050, 006360, 000720 |
| trigger families | Stage2-Actionable, Stage3-Yellow, Stage3-Green, Stage4B, Stage4C |
| evidence types | annual result/guidance, mega contract, Q1 beat, Q2 cost miss, annual/Q4 loss |
| outcome mix | 2 constructive / 3 counterexample or guardrail |
| proxy-only sources | 0 |
| missing MFE/MAE | 0 |


## 23. Residual contribution summary
```json
{
  "new_independent_case_count": 5,
  "reused_case_count": 0,
  "calibration_usable_case_count": 5,
  "calibration_usable_trigger_count": 5,
  "representative_trigger_count": 5,
  "unique_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 5,
  "positive_case_count": 2,
  "counterexample_count": 3,
  "current_profile_error_count": 3,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "avg_MFE_30D_pct": 15.64,
  "avg_MFE_90D_pct": 45.98,
  "avg_MFE_180D_pct": 59.94,
  "avg_MAE_30D_pct": -7.08,
  "avg_MAE_90D_pct": -9.81,
  "avg_MAE_180D_pct": -18.28,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": "c05_kitchen_sink_4c_timing_guard + green_decay_margin_cash_freshness_gate",
  "existing_axis_strengthened": "full_4b_requires_non_price_evidence; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c_qualified",
  "existing_axis_weakened": "none in production; shadow-only qualification of hard4C for one-off reset rows",
  "do_not_propose_new_weight_delta": false
}
```

## 24. Validation scope
| validation item | result |
| --- | --- |
| actual Stock-Web 1D OHLC rows used | true |
| forward 180D complete | true for all 5 triggers |
| corporate-action D~D+180 blocked/checked | checked; no selected-window overlap |
| source proxy only | false |
| production scoring changed | false |
| shadow-only rule proposal | true |
| new independent case count | 5 |
| reused case count | 0 |


## 25. Machine-readable JSONL
{"active_like_symbol_count": 2868, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "corporate_action_candidate_count": 14435, "inactive_or_delisted_like_symbol_count": 2546, "manifest_max_date": "2026-02-20", "manifest_min_date": "1995-05-02", "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"], "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "raw_row_count": 15214118, "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source_name": "FinanceData/marcap", "source_repo_url": "https://github.com/FinanceData/marcap", "symbol_count": 5414, "tradable_row_count": 14354401, "universe_path": "atlas/universe/all_symbols.csv"}
{"avg_MAE_180D_pct": -18.28, "avg_MAE_30D_pct": -7.08, "avg_MAE_90D_pct": -9.81, "avg_MFE_180D_pct": 59.94, "avg_MFE_30D_pct": 15.64, "avg_MFE_90D_pct": 45.98, "calibration_usable_case_count": 5, "calibration_usable_trigger_count": 5, "counterexample_count": 3, "current_profile_error_count": 3, "evidence_url_pending_count": 0, "missing_required_mfe_mae_count": 0, "new_independent_case_count": 5, "positive_case_count": 2, "representative_trigger_count": 5, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "reused_case_count": 0, "row_type": "aggregate", "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 5, "source_proxy_only_count": 0, "unique_symbol_count": 3}
{"MAE_180D_low_date": "2024-10-25", "MAE_180D_low_price": 18180.0, "MAE_180D_pct": -18.48, "MAE_30D_pct": -0.22, "MAE_90D_pct": -0.22, "MFE_180D_pct": 31.39, "MFE_180D_peak_date": "2024-07-30", "MFE_180D_peak_price": 29300.0, "MFE_30D_pct": 26.23, "MFE_90D_pct": 26.23, "actual_outcome": "early_positive_then_180D_late_fade", "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L208_01_SAMSUNG_EA_2023_RESULT_GUIDANCE_LATE_FADE", "close_180D_pct": -17.67, "close_180D_price": 18360.0, "company": "Samsung E&A / 삼성E&A", "corporate_action_overlap_D_to_D180": false, "current_profile_error": true, "current_profile_eval": "would often remain Stage3-Green because revision/annual-result evidence is high; that misses late margin-cycle decay without fresh cash-conversion confirmation.", "dedupe_for_aggregate": true, "drawdown_after_peak_180D_low_date": "2024-10-25", "drawdown_after_peak_180D_pct": -37.95, "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage3-Green|2024-01-31", "entry_amount": 71745804000.0, "entry_c": 22300.0, "entry_date": "2024-01-31", "entry_h": 24600.0, "entry_l": 22250.0, "entry_market": "KOSPI", "entry_market_cap": 4370800000000.0, "entry_o": 24500.0, "entry_price": 22300.0, "entry_shares": 196000000, "entry_v": 3158972, "evidence_summary": "2023 annual operating profit KRW 993.1B (+41.3% YoY), revenue KRW 10.6T, backlog/order guidance, and KRW 370B future-technology investment.", "evidence_url": "https://www.samsungena.com/en/newsroom/news/view?idx=15585", "fine_archetype_id": "C05_ORDER_HEADLINE_MARGIN_CASHFLOW_AND_KITCHEN_SINK_4C_GUARD", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "proposed_shadow_eval": "Stage3-Yellow after initial green, with full-4B watch if no fresh margin/working-capital bridge appears before the peak fades.", "raw_component_score_map": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 8, "contract_score": 7, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "margin_bridge_score": 7, "policy_or_regulatory_score": 2, "relative_strength_score": 5, "revision_score": 8, "valuation_repricing_score": 5}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "row_type": "trigger", "score_after_shadow": 80.0, "score_before": 89.0, "symbol": "028050", "trigger_date": "2024-01-30", "trigger_id": "C05_L208_T001_028050_STAGE3_GREEN_20240130", "trigger_type": "Stage3-Green", "window_180D_end_date": "2024-10-29"}
{"MAE_180D_low_date": "2024-04-19", "MAE_180D_low_price": 14040.0, "MAE_180D_pct": -10.17, "MAE_30D_pct": -10.17, "MAE_90D_pct": -10.17, "MFE_180D_pct": 39.16, "MFE_180D_peak_date": "2024-08-27", "MFE_180D_peak_price": 21750.0, "MFE_30D_pct": 6.97, "MFE_90D_pct": 30.52, "actual_outcome": "positive_MFE180_with_manageable_MAE", "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L208_02_GS_EC_FADHILI_PACKAGE2_POSITIVE", "close_180D_pct": 12.09, "close_180D_price": 17520.0, "company": "GS E&C / GS건설", "corporate_action_overlap_D_to_D180": false, "current_profile_error": false, "current_profile_eval": "Stage2-Actionable works; should not be promoted to Green unless margin and working-capital conversion later confirm.", "dedupe_for_aggregate": true, "drawdown_after_peak_180D_low_date": "2024-11-13", "drawdown_after_peak_180D_pct": -22.48, "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-03", "entry_amount": 64698222680.0, "entry_c": 15630.0, "entry_date": "2024-04-03", "entry_h": 16550.0, "entry_l": 15400.0, "entry_market": "KOSPI", "entry_market_cap": 1337638688700.0, "entry_o": 15500.0, "entry_price": 15630.0, "entry_shares": 85581490, "entry_v": 4065591, "evidence_summary": "GS E&C won Saudi Aramco Fadhili Gas Increment Program Package 2 sulfur-recovery facility contract, about USD 1.22B / KRW 1.6T, 41-month construction period.", "evidence_url": "https://www.asiae.co.kr/en/article/2024040309065572598", "fine_archetype_id": "C05_ORDER_HEADLINE_MARGIN_CASHFLOW_AND_KITCHEN_SINK_4C_GUARD", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "proposed_shadow_eval": "keep Stage2-Actionable with positive watch; promote only after margin/cash bridge.", "raw_component_score_map": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 7, "contract_score": 9, "customer_quality_score": 9, "dilution_cb_risk_score": 0, "execution_risk_score": -2, "legal_or_contract_risk_score": -1, "margin_bridge_score": 3, "policy_or_regulatory_score": 3, "relative_strength_score": 5, "revision_score": 3, "valuation_repricing_score": 4}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "row_type": "trigger", "score_after_shadow": 78.5, "score_before": 77.0, "symbol": "006360", "trigger_date": "2024-04-03", "trigger_id": "C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403", "trigger_type": "Stage2-Actionable", "window_180D_end_date": "2024-12-27"}
{"MAE_180D_low_date": "2024-12-09", "MAE_180D_low_price": 24100.0, "MAE_180D_pct": -27.52, "MAE_30D_pct": -4.96, "MAE_90D_pct": -12.63, "MFE_180D_pct": 8.27, "MFE_180D_peak_date": "2024-05-09", "MFE_180D_peak_price": 36000.0, "MFE_30D_pct": 8.27, "MFE_90D_pct": 8.27, "actual_outcome": "late_counterexample_MAE180_dominates", "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L208_03_HYUNDAI_EC_Q1_BEAT_COST_RATE_LATE_FAIL", "close_180D_pct": -22.11, "close_180D_price": 25900.0, "company": "Hyundai E&C / 현대건설", "corporate_action_overlap_D_to_D180": false, "current_profile_error": true, "current_profile_eval": "near-Green if profit beat and revenue growth receive too much weight.", "dedupe_for_aggregate": true, "drawdown_after_peak_180D_low_date": "2024-12-09", "drawdown_after_peak_180D_pct": -33.06, "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage3-Yellow|2024-04-19", "entry_amount": 23799312600.0, "entry_c": 33250.0, "entry_date": "2024-04-19", "entry_h": 33450.0, "entry_l": 31600.0, "entry_market": "KOSPI", "entry_market_cap": 3702579186250.0, "entry_o": 32000.0, "entry_price": 33250.0, "entry_shares": 111355765, "entry_v": 727477, "evidence_summary": "Q1 2024 net profit +38.4% YoY, operating profit +44.6% to KRW 250.9B, revenue +41.7% to KRW 8.55T, and OP beat consensus.", "evidence_url": "https://en.yna.co.kr/view/AEN20240419005652320", "fine_archetype_id": "C05_ORDER_HEADLINE_MARGIN_CASHFLOW_AND_KITCHEN_SINK_4C_GUARD", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "proposed_shadow_eval": "cap at Stage3-Yellow unless cost-rate and working-capital confirmation survives the next reporting cycle.", "raw_component_score_map": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 7, "contract_score": 5, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": -1, "margin_bridge_score": 4, "policy_or_regulatory_score": 1, "relative_strength_score": 4, "revision_score": 7, "valuation_repricing_score": 4}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "row_type": "trigger", "score_after_shadow": 72.5, "score_before": 83.0, "symbol": "000720", "trigger_date": "2024-04-19", "trigger_id": "C05_L208_T003_000720_STAGE3_YELLOW_20240419", "trigger_type": "Stage3-Yellow", "window_180D_end_date": "2025-01-15"}
{"MAE_180D_low_date": "2024-12-09", "MAE_180D_low_price": 24100.0, "MAE_180D_pct": -26.07, "MAE_30D_pct": -10.89, "MAE_90D_pct": -16.87, "MFE_180D_pct": 21.78, "MFE_180D_peak_date": "2025-04-15", "MFE_180D_peak_price": 39700.0, "MFE_30D_pct": 4.75, "MFE_90D_pct": 4.75, "actual_outcome": "4B_correct_early_but_not_hard_exit", "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L208_04_HYUNDAI_EC_Q2_RAW_MATERIAL_COST_4B", "close_180D_pct": 20.4, "close_180D_price": 39250.0, "company": "Hyundai E&C / 현대건설", "corporate_action_overlap_D_to_D180": false, "current_profile_error": false, "current_profile_eval": "full_4B may be too harsh if it ignores backlog resilience and later kitchen-sink clearing.", "dedupe_for_aggregate": true, "drawdown_after_peak_180D_low_date": "2025-04-17", "drawdown_after_peak_180D_pct": -3.78, "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2024-07-19", "entry_amount": 25298546100.0, "entry_c": 32600.0, "entry_date": "2024-07-19", "entry_h": 33100.0, "entry_l": 32450.0, "entry_market": "KOSPI", "entry_market_cap": 3630197939000.0, "entry_o": 33100.0, "entry_price": 32600.0, "entry_shares": 111355765, "entry_v": 775289, "evidence_summary": "Q2 net income -31.2%, operating profit -34.1%, sales +20.4%; miss versus analyst estimate; company cited raw-material price rise and quality/safety expenses.", "evidence_url": "https://en.yna.co.kr/view/AEN20240719004551320", "fine_archetype_id": "C05_ORDER_HEADLINE_MARGIN_CASHFLOW_AND_KITCHEN_SINK_4C_GUARD", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "proposed_shadow_eval": "local 4B only; full 4B requires repeated cost-rate misses or cash-flow impairment.", "raw_component_score_map": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 6, "contract_score": 4, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": -7, "legal_or_contract_risk_score": -2, "margin_bridge_score": 1, "policy_or_regulatory_score": 1, "relative_strength_score": 3, "revision_score": 2, "valuation_repricing_score": 3}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "row_type": "trigger", "score_after_shadow": 58.0, "score_before": 61.0, "symbol": "000720", "trigger_date": "2024-07-19", "trigger_id": "C05_L208_T004_000720_STAGE4B_20240719", "trigger_type": "Stage4B", "window_180D_end_date": "2025-04-17"}
{"MAE_180D_low_date": "2025-01-22", "MAE_180D_low_price": 25850.0, "MAE_180D_pct": -9.14, "MAE_30D_pct": -9.14, "MAE_90D_pct": -9.14, "MFE_180D_pct": 199.12, "MFE_180D_peak_date": "2025-06-25", "MFE_180D_peak_price": 85100.0, "MFE_30D_pct": 31.99, "MFE_90D_pct": 160.11, "actual_outcome": "positive_after_4C_signal", "calibration_usable": true, "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "case_id": "C05_L208_05_HYUNDAI_EC_2024_LOSS_HARD4C_FALSE_NEGATIVE", "close_180D_pct": 107.03, "close_180D_price": 58900.0, "company": "Hyundai E&C / 현대건설", "corporate_action_overlap_D_to_D180": false, "current_profile_error": true, "current_profile_eval": "hard_4c_thesis_break_routes_to_4c would over-route if it treats all one-off/project-loss recognition as permanent thesis death.", "dedupe_for_aggregate": true, "drawdown_after_peak_180D_low_date": "2025-09-30", "drawdown_after_peak_180D_pct": -36.43, "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4C|2025-01-22", "entry_amount": 90189685850.0, "entry_c": 28450.0, "entry_date": "2025-01-22", "entry_h": 28450.0, "entry_l": 25850.0, "entry_market": "KOSPI", "entry_market_cap": 3168071514250.0, "entry_o": 26200.0, "entry_price": 28450.0, "entry_shares": 111355765, "entry_v": 3258966, "evidence_summary": "Hyundai E&C swung to a Q4 operating loss and full-year 2024 net loss; weak won, raw-material costs, and affiliate one-off project costs weighed, while 2024 orders still exceeded target.", "evidence_url": "https://en.yna.co.kr/view/AEN20250122006251320", "fine_archetype_id": "C05_ORDER_HEADLINE_MARGIN_CASHFLOW_AND_KITCHEN_SINK_4C_GUARD", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "proposed_shadow_eval": "route to 4C only if loss is paired with backlog collapse, liquidity stress, repeated receivable impairment, or customer/legal break; otherwise Stage4B/contrarian watch.", "raw_component_score_map": {"accounting_trust_risk_score": -2, "backlog_visibility_score": 7, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": -8, "legal_or_contract_risk_score": -3, "margin_bridge_score": 0, "policy_or_regulatory_score": 2, "relative_strength_score": 2, "revision_score": 0, "valuation_repricing_score": 5}, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "row_type": "trigger", "score_after_shadow": 61.5, "score_before": 42.0, "symbol": "000720", "trigger_date": "2025-01-22", "trigger_id": "C05_L208_T005_000720_STAGE4C_20250122", "trigger_type": "Stage4C", "window_180D_end_date": "2025-10-22"}
{"canonical_archetype_rule_candidate": "C05 requires green decay when margin-cash freshness disappears and a kitchen-sink 4C guard when severe losses are one-off/reset-like rather than structural.", "production_scoring_changed": false, "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "row_type": "residual_contribution", "sector_specific_rule_candidate": "L1 EPC order/backlog/revenue evidence must be bridged to cost-rate and working-capital conversion before Green promotion.", "shadow_weight_only": true}

## 26. Batch ingest self-audit
```json
{
  "expected_to_be_parsed_by_batch_ingest": true,
  "filename_pattern_match": true,
  "filename_metadata_consistent": true,
  "jsonl_trigger_row_count": 5,
  "calibration_usable_trigger_count": 5,
  "representative_trigger_count": 5,
  "new_independent_case_count": 5,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "missing_required_mfe_mae_count": 0,
  "missing_entry_price_count": 0,
  "missing_entry_date_count": 0,
  "stage4b_or_stage4c_guardrail_count": 2,
  "narrative_only_or_rejected_count": 0,
  "ready_for_ingest": true
}
```

## 27. Deferred coding-agent handoff prompt
Use this file as a research artifact only. Do not patch production scoring directly. In a later batch-evaluation branch, parse the JSONL trigger rows from `e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md` and test the C05 shadow features: green decay margin-cash freshness gate, cost-rate/working-capital penalty, customer-quality named-package support, and kitchen-sink 4C timing guard. Compare against the current v12 calibrated profile using exact duplicate key `canonical_archetype_id + symbol + trigger_type + entry_date`. Require all MFE/MAE fields to be present before any aggregate. If duplicate keys exist in a future corpus, keep only one representative row unless the row is explicitly marked as holdout.

## 28. Next-round state
```json
{
  "completed_round": "R1",
  "completed_loop": 208,
  "completed_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "completed_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "recommended_next_priority": "Continue Priority-1 quality repair but avoid immediate C05 repetition unless the next run targets missing-url/actual-MFE repair. Recommended rotation: C01, C13, C10, or C15 depending on latest index.",
  "next_run_should_avoid_exact_duplicate_keys": [
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage3-Green|2024-01-31",
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-03",
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage3-Yellow|2024-04-19",
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2024-07-19",
    "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4C|2025-01-22"
  ],
  "new_no_repeat_rows_to_append": [
    {
      "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
      "symbol": "028050",
      "trigger_type": "Stage3-Green",
      "entry_date": "2024-01-31",
      "trigger_id": "C05_L208_T001_028050_STAGE3_GREEN_20240130"
    },
    {
      "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
      "symbol": "006360",
      "trigger_type": "Stage2-Actionable",
      "entry_date": "2024-04-03",
      "trigger_id": "C05_L208_T002_006360_STAGE2_ACTIONABLE_20240403"
    },
    {
      "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
      "symbol": "000720",
      "trigger_type": "Stage3-Yellow",
      "entry_date": "2024-04-19",
      "trigger_id": "C05_L208_T003_000720_STAGE3_YELLOW_20240419"
    },
    {
      "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
      "symbol": "000720",
      "trigger_type": "Stage4B",
      "entry_date": "2024-07-19",
      "trigger_id": "C05_L208_T004_000720_STAGE4B_20240719"
    },
    {
      "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
      "symbol": "000720",
      "trigger_type": "Stage4C",
      "entry_date": "2025-01-22",
      "trigger_id": "C05_L208_T005_000720_STAGE4C_20250122"
    }
  ]
}
```

## 29. Source notes
- Stock-Web manifest/schema source: `Songdaiki/stock-web`, tradable raw/unadjusted OHLC atlas.
- Evidence sources are stored per trigger in the JSONL rows. No proxy-only evidence rows were used.
- All proposed rules are shadow-only. Production scoring remains unchanged.
