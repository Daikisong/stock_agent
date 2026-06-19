---
research_file: "e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"
created_at_kst: "2026-06-15"
research_mode: "post_calibrated_residual_historical_research_v12"
selected_round: "R1"
selected_loop: 204
round_schedule_status: "coverage_index_selected"
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
large_sector_id: "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
canonical_archetype_id: "C02_POWER_GRID_DATACENTER_CAPEX"
fine_archetype_id: "C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR"
primary_price_source: "Songdaiki/stock-web"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
calibration_shard_root: "atlas/ohlcv_tradable_by_symbol_year"
new_independent_case_count: 6
new_independent_trigger_count: 6
unique_symbol_count: 5
stage2_count: 2
stage2_actionable_count: 3
stage4b_count: 1
stage4c_count: 0
positive_direct_bridge_count: 4
counterexample_or_guardrail_count: 3
source_proxy_only_count: 0
profile_only_trigger_count: 1
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
current_profile_error_count: 6
production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: false
ready_for_batch_ingest: true
---

# E2R v12 Residual Historical Calibration — R1 / L1 / C02

## 0. Execution declaration

This file follows the v12 post-calibrated residual historical-research procedure.

- **MAIN prompt basis:** `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
- **No-Repeat ledger:** `docs/core/V12_Research_No_Repeat_Index.md`
- **Price source:** `Songdaiki/stock-web`
- **No production code patch:** true
- **No live scan / no current recommendation:** true
- **Shadow calibration only:** true

## 1. Selection rationale

The current ledger is already past the raw row-shortage phase. C01~C32 are all above the old 30/50/80-row thresholds, so this run is not a mechanical row-fill. The selected axis is a **C02 quality-repair / 4B-4C boundary run**:

```text
selected_round: R1
selected_loop: 204
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR
```

The specific residual question:

> In C02, when should a power-grid/data-center headline remain **profile-only Stage2**, become **Stage2-Actionable** through direct order/backlog/margin bridge, or be downgraded to **Stage4B** as a proxy-theme/peak-extension row? Hard 4C should remain rare unless a non-price thesis break appears.

This loop deliberately mixes:

- direct transformer / cable backlog winners,
- cable/profile-only names whose forward price path was good but evidence was not actionable,
- copper-wire / commodity-theme rows where the evidence did not prove a data-center/grid order bridge,
- one peak-proximate Stage4B case.

## 2. Batch summary

```text
new_independent_case_count: 6
new_independent_trigger_count: 6
unique_symbol_count: 5

stage2_count: 2
stage2_actionable_count: 3
stage4b_count: 1
stage4c_count: 0

positive_direct_bridge_count: 4
counterexample_or_guardrail_count: 3
profile_only_trigger_count: 1

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

current_profile_error_count: 6
production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 3. Stock-Web validation

```text
stock_web_repo: Songdaiki/stock-web
manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_schema_columns: d,o,h,l,c,v,a,mc,s,m
mfe_mae_window_basis: entry row inclusive N tradable rows
corporate_action_screen: D through D+180, share-count change >= 20% treated as contaminated
```

All trigger rows below have an actual entry OHLCV row and 30/90/180 trading-row forward windows.

## 4. Trigger table

| symbol | company | trigger | entry | entry close | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak180 | post-peak DD | role |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| 024840 | KBI Metal | Stage4B | 2024-05-21 | 4,040 | 17.45 | -36.14 | 17.45 | -46.16 | 17.45 | -58.74 | 2024-05-21 / 4,745 | -64.87 | proxy_theme_overextension_counterexample |
| 024840 | KBI Metal | Stage2 | 2024-08-14 | 3,065 | 15.17 | -17.46 | 15.17 | -45.61 | 15.17 | -47.90 | 2024-08-16 / 3,530 | -54.76 | earnings_swing_counterexample |
| 103590 | Iljin Electric | Stage2-Actionable | 2024-10-17 | 26,100 | 14.94 | -20.69 | 43.87 | -21.46 | 59.39 | -24.14 | 2025-06-30 / 41,600 | -15.14 | direct_us_transformer_order_positive_control |
| 267260 | HD Hyundai Electric | Stage2-Actionable | 2025-04-22 | 301,000 | 34.39 | -3.16 | 72.76 | -3.16 | 224.25 | -3.16 | 2025-11-04 / 976,000 | -24.59 | direct_backlog_margin_positive_control |
| 001440 | Taihan Cable & Solution | Stage2-Actionable | 2025-04-30 | 11,630 | 45.66 | -0.86 | 56.23 | -0.86 | 154.94 | -0.86 | 2026-01-22 / 29,650 | -10.62 | direct_cable_orders_positive_control |
| 000500 | Gaon Cable | Stage2 | 2025-04-30 | 60,300 | 38.97 | -3.98 | 38.97 | -6.97 | 70.81 | -12.77 | 2026-01-20 / 103,000 | -15.15 | profile_only_positive_path_but_not_actionable |

## 5. Case cards

### Case 1. 024840 KBI Metal — Stage4B / proxy_theme_overextension_counterexample

- **dedupe_key:** `C02_POWER_GRID_DATACENTER_CAPEX|024840|Stage4B|2024-05-21`
- **evidence date:** 2024-04-19/2024-05-21
- **evidence URL:** https://www.asiae.co.kr/en/article/2024041910590184215
- **evidence summary:** Copper-wire/power-line exposure attracted power-grid/copper theme buying, but evidence was mainly product exposure and price/commodity momentum, not customer-specific grid backlog or margin-recognition bridge.
- **direct bridge verdict:** `no_company_specific_grid_order_or_backlog_bridge`
- **actual entry OHLCV:** `d=2024-05-21, o=4155, h=4745, l=3960, c=4040, v=60066232, a=261732979995, mc=138532323160, s=34290179, m=KOSDAQ`
- **stock-web shards:** `atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv; atlas/ohlcv_tradable_by_symbol_year/024/024840/2025.csv`
- **30/90/180D price path:** MFE `17.45/17.45/17.45`, MAE `-36.14/-46.16/-58.74`
- **180D peak / post-peak drawdown:** 2024-05-21 high 4,745; drawdown after peak `-64.87%`
- **corporate-action / forward-window status:** `clean_180D_window`, rows_180D_used=180
- **current-profile stress:** `Stage2-Actionable` → recommended `Stage4B`; `reduce C02 bottleneck/pricing credit when only copper-wire product exposure and theme momentum are present`

### Case 2. 024840 KBI Metal — Stage2 / earnings_swing_counterexample

- **dedupe_key:** `C02_POWER_GRID_DATACENTER_CAPEX|024840|Stage2|2024-08-14`
- **evidence date:** 2024-08-14
- **evidence URL:** https://www.mk.co.kr/en/business/11092877
- **evidence summary:** First-half operating profit jumped sharply, but the article frames stable operating activities/copper-wire manufacturing rather than a power-grid/data-center order backlog bridge.
- **direct bridge verdict:** `earnings_swing_yes__grid_order_backlog_no`
- **actual entry OHLCV:** `d=2024-08-14, o=2710, h=3285, l=2710, c=3065, v=45038083, a=140285344560, mc=106996694935, s=34909199, m=KOSDAQ`
- **stock-web shards:** `atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv; atlas/ohlcv_tradable_by_symbol_year/024/024840/2025.csv`
- **30/90/180D price path:** MFE `15.17/15.17/15.17`, MAE `-17.46/-45.61/-47.90`
- **180D peak / post-peak drawdown:** 2024-08-16 high 3,530; drawdown after peak `-54.76%`
- **corporate-action / forward-window status:** `clean_180D_window`, rows_180D_used=180
- **current-profile stress:** `Stage2-Actionable` → recommended `Stage2`; `cap earnings-only copper wire improvement at Stage2 until explicit grid/data-center order conversion exists`

### Case 3. 103590 Iljin Electric — Stage2-Actionable / direct_us_transformer_order_positive_control

- **dedupe_key:** `C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage2-Actionable|2024-10-17`
- **evidence date:** 2024-10-17
- **evidence URL:** https://www.asiae.co.kr/en/article/2024101708454510488
- **evidence summary:** Analyst article cites expected earnings improvement and a large U.S. ultra-high-voltage transformer contract, with revenue recognition expected to grow from 2025.
- **direct bridge verdict:** `us_transformer_contract_to_revenue_recognition_bridge`
- **actual entry OHLCV:** `d=2024-10-17, o=23550, h=26350, l=23500, c=26100, v=4174733, a=104565656050, mc=1244588679000, s=47685390, m=KOSPI`
- **stock-web shards:** `atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv; atlas/ohlcv_tradable_by_symbol_year/103/103590/2025.csv`
- **30/90/180D price path:** MFE `14.94/43.87/59.39`, MAE `-20.69/-21.46/-24.14`
- **180D peak / post-peak drawdown:** 2025-06-30 high 41,600; drawdown after peak `-15.14%`
- **corporate-action / forward-window status:** `clean_180D_window`, rows_180D_used=180
- **current-profile stress:** `Stage3-Yellow` → recommended `Stage2-Actionable`; `preserve order/revenue bridge but apply high-MAE and margin-timing cap before Yellow/Green`

### Case 4. 267260 HD Hyundai Electric — Stage2-Actionable / direct_backlog_margin_positive_control

- **dedupe_key:** `C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage2-Actionable|2025-04-22`
- **evidence date:** 2025-04-22
- **evidence URL:** https://en.yna.co.kr/view/AEN20250422006151320
- **evidence summary:** Q1 2025 orders, order backlog, sales, operating profit, and North-America profitability all pointed to direct grid-equipment backlog-to-margin conversion.
- **direct bridge verdict:** `orders_backlog_sales_operating_profit_margin_bridge`
- **actual entry OHLCV:** `d=2025-04-22, o=329000, h=333500, l=300000, c=301000, v=706084, a=221732415500, mc=10850187635000, s=36047135, m=KOSPI`
- **stock-web shards:** `atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv; atlas/ohlcv_tradable_by_symbol_year/267/267260/2026.csv`
- **30/90/180D price path:** MFE `34.39/72.76/224.25`, MAE `-3.16/-3.16/-3.16`
- **180D peak / post-peak drawdown:** 2025-11-04 high 976,000; drawdown after peak `-24.59%`
- **corporate-action / forward-window status:** `clean_180D_window`, rows_180D_used=180
- **current-profile stress:** `Stage3-Yellow` → recommended `Stage2-Actionable`; `direct order/backlog/margin bridge gets high-quality Actionable; Green still waits for valuation/FCF breadth`

### Case 5. 001440 Taihan Cable & Solution — Stage2-Actionable / direct_cable_orders_positive_control

- **dedupe_key:** `C02_POWER_GRID_DATACENTER_CAPEX|001440|Stage2-Actionable|2025-04-30`
- **evidence date:** 2025-04-30
- **evidence URL:** https://www.taihan.com/en/news/pr/taihanNewsDetail?idx=683
- **evidence summary:** Q1 2025 revenue and operating profit were stable/high, with strong performance attributed to global orders and overseas subsidiaries.
- **direct bridge verdict:** `q1_revenue_profit_global_order_bridge`
- **actual entry OHLCV:** `d=2025-04-30, o=12020, h=12020, l=11530, c=11630, v=643858, a=7531064800, mc=2168382099000, s=186447300, m=KOSPI`
- **stock-web shards:** `atlas/ohlcv_tradable_by_symbol_year/001/001440/2025.csv; atlas/ohlcv_tradable_by_symbol_year/001/001440/2026.csv`
- **30/90/180D price path:** MFE `45.66/56.23/154.94`, MAE `-0.86/-0.86/-0.86`
- **180D peak / post-peak drawdown:** 2026-01-22 high 29,650; drawdown after peak `-10.62%`
- **corporate-action / forward-window status:** `clean_180D_window`, rows_180D_used=180
- **current-profile stress:** `Stage2` → recommended `Stage2-Actionable`; `direct global order and revenue/profit bridge should reopen Actionable after older cable high-MAE cases`

### Case 6. 000500 Gaon Cable — Stage2 / profile_only_positive_path_but_not_actionable

- **dedupe_key:** `C02_POWER_GRID_DATACENTER_CAPEX|000500|Stage2|2025-04-30`
- **evidence date:** 2025-04-30
- **evidence URL:** https://gaoncable.com/
- **evidence summary:** Company product profile confirms extra-high-voltage, distribution, overhead-line and copper-rod exposure, but no event-date customer order/backlog bridge was used.
- **direct bridge verdict:** `product_profile_only_no_event_order_backlog`
- **actual entry OHLCV:** `d=2025-04-30, o=60000, h=62100, l=57900, c=60300, v=120767, a=7246783550, mc=997549834500, s=16543115, m=KOSPI`
- **stock-web shards:** `atlas/ohlcv_tradable_by_symbol_year/000/000500/2025.csv; atlas/ohlcv_tradable_by_symbol_year/000/000500/2026.csv`
- **30/90/180D price path:** MFE `38.97/38.97/70.81`, MAE `-3.98/-6.97/-12.77`
- **180D peak / post-peak drawdown:** 2026-01-20 high 103,000; drawdown after peak `-15.15%`
- **corporate-action / forward-window status:** `clean_180D_window`, rows_180D_used=180
- **current-profile stress:** `Stage2-Actionable` → recommended `Stage2`; `good forward path cannot promote profile-only row without as-of order/backlog bridge`


## 6. Residual interpretation

### 6.1 Direct bridge rows should survive as Actionable

`267260`, `001440`, and `103590` show the stronger side of C02. The common feature is not just “power equipment is hot.” The evidence includes at least one of:

```text
orders / order backlog
revenue recognition route
operating-profit or margin bridge
global or North America customer demand
transformer / cable capacity or product-specific backlog
```

These rows justify **Stage2-Actionable**. They do not automatically justify Stage3-Green because C02 still needs valuation discipline, FCF/cash-conversion confirmation, and high-MAE control.

### 6.2 Proxy/product-profile rows should not be promoted by price path alone

`000500` had a good forward price path after the clean post-corporate-action entry row, but the as-of evidence used here is a product-profile exposure row rather than an event-date order/backlog trigger. That is a **Stage2 cap**, not an Actionable signal.

This is an important residual: a later positive path cannot backfill missing as-of evidence. Price-path success validates the watchlist lane, not the promotion lane.

### 6.3 Copper-wire / commodity-theme rows need a separate C02 cap

`024840` is useful because it sits near the border between C02 and commodity/material spread logic. Copper-wire and power-line exposure can be adjacent to C02, but unless the evidence names company-specific grid/data-center orders, backlog, capacity, or margin conversion, it should not consume the same Actionable credit as transformer/cable backlog names.

The May 2024 row is peak-proximate and high-MAE, so it is better represented as **Stage4B / overextension watch**. The August 2024 row has real earnings improvement, but not a grid/data-center order bridge, so it remains **Stage2**.

### 6.4 Hard 4C remains intentionally rare in C02

This batch found no clean C02 hard-4C row. That absence is itself a useful holdout signal. A hard 4C in C02 should require non-price thesis break such as:

```text
order cancellation
backlog collapse
customer loss
capacity expansion failure
price/margin break
accounting-trust break tied to grid-equipment backlog quality
```

High MAE, theme exhaustion, or profile-only evidence is not enough. Those are Stage4B/watch or capped Stage2 problems.

## 7. Rule candidate

```text
rule_candidate:
C02_DIRECT_BACKLOG_MARGIN_BRIDGE_AND_PROXY_THEME_4B_GATE

sector_rule_candidate:
L1_GRID_DATACENTER_ORDER_BACKLOG_TO_MARGIN_GATE

core_residual:
- C02 Stage2-Actionable requires direct order, backlog, revenue-recognition,
  margin, capacity, or customer-demand bridge.
- Product profile alone remains Stage2 even if future price path is good.
- Copper-wire / commodity-theme adjacency remains capped unless a grid/data-center
  order bridge is explicit.
- Peak-proximate C02 theme rows with deep 90D/180D MAE route to Stage4B/watch,
  not hard 4C.
- Hard 4C requires non-price thesis break; high MAE alone is insufficient.
```

### 7.1 Shadow weight implication

```text
production_scoring_changed: false
shadow_weight_only: true

component_delta_candidate:
  earnings_visibility:
    +0.15 for explicit order/backlog-to-revenue or revenue/profit bridge
  bottleneck_pricing:
    +0.20 for transformer/cable capacity plus customer/order backlog
    -0.25 for copper-wire or profile-only proxy exposure
  market_mispricing:
    -0.10 when entry is theme-peak-proximate or 90D MAE <= -30 without second bridge
  valuation_rerating:
    Stage3-Green blocker remains until FCF/cash conversion or multi-quarter margin bridge appears
  information_confidence:
    +0.10 for issuer filing/official release/major wire with concrete order-backlog data

guardrail_candidate:
  profile_only_grid_exposure_cap: Stage2
  copper_wire_or_commodity_theme_cap: Stage2 or Stage4B
  stage2_actionable_requires:
    at least one direct order/backlog/revenue/margin/capacity/customer bridge
  hard_4c_requires:
    cancellation/backlog-collapse/customer-loss/capacity-failure/margin-break
```

## 8. Machine-readable JSONL

```jsonl
{"row_type":"v12_trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":204,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR","symbol":"024840","company":"KBI Metal","case_id":"C02_024840_20240521_STAGE4B_THEME_OVEREXTENSION","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|024840|Stage4B|2024-05-21","trigger_type":"Stage4B","entry_date":"2024-05-21","entry_price":4040.0,"actual_entry_ohlcv":{"d":"2024-05-21","o":4155,"h":4745,"l":3960,"c":4040,"v":60066232,"a":261732979995,"mc":138532323160,"s":34290179,"m":"KOSDAQ"},"price_source_validation":{"price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shards":["atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv","atlas/ohlcv_tradable_by_symbol_year/024/024840/2025.csv"],"mfe_mae_window_basis":"entry row inclusive N tradable rows","manifest_max_date":"2026-02-20"},"MFE_30D_pct":17.45,"MAE_30D_pct":-36.14,"MFE_90D_pct":17.45,"MAE_90D_pct":-46.16,"MFE_180D_pct":17.45,"MAE_180D_pct":-58.74,"peak_180D_date":"2024-05-21","peak_180D_price":4745.0,"drawdown_after_peak_pct":-64.87,"trough_after_peak_date":"2024-12-09","corporate_action_window_status":"clean_180D_window","forward_window_trading_rows":180,"evidence_date":"2024-04-19/2024-05-21","evidence_url":"https://www.asiae.co.kr/en/article/2024041910590184215","evidence_summary":"Copper-wire/power-line exposure attracted power-grid/copper theme buying, but evidence was mainly product exposure and price/commodity momentum, not customer-specific grid backlog or margin-recognition bridge.","case_role":"proxy_theme_overextension_counterexample","direct_bridge_verdict":"no_company_specific_grid_order_or_backlog_bridge","residual_label":"proxy_wire_theme_peak_needs_stage4b_not_actionable","current_profile_simulated_stage":"Stage2-Actionable","recommended_stage":"Stage4B","raw_total_score":82.0,"recommended_total_score":70.0,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"primary","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"row_type":"score_simulation","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|024840|Stage4B|2024-05-21","score_component_context":{"eps_fcf_explosion":"direct bridge only if order/backlog/margin or revenue conversion appears","earnings_visibility":"boost for direct Q1/Q2 revenue/profit/order bridge; cap for commodity/product-profile only","bottleneck_pricing":"boost for transformer/cable backlog and capacity tightness; reduce for copper-wire proxy","market_mispricing":"keep positive only when non-price bridge survives high MAE","valuation_rerating":"Green blocker if evidence is profile-only, peak-proximate, or high-MAE without cash/FCF confirmation","information_confidence":"direct issuer/company/major-news source > analyst-only > profile-only"},"current_profile_simulated_stage":"Stage2-Actionable","recommended_stage":"Stage4B","current_profile_error":"would_overcount_commodity_wire_profile_as_grid_capex_actionable","component_adjustment_summary":"reduce C02 bottleneck/pricing credit when only copper-wire product exposure and theme momentum are present","production_scoring_changed":false}
{"row_type":"v12_trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":204,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR","symbol":"024840","company":"KBI Metal","case_id":"C02_024840_20240814_STAGE2_EARNINGS_WITHOUT_GRID_BACKLOG","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|024840|Stage2|2024-08-14","trigger_type":"Stage2","entry_date":"2024-08-14","entry_price":3065.0,"actual_entry_ohlcv":{"d":"2024-08-14","o":2710,"h":3285,"l":2710,"c":3065,"v":45038083,"a":140285344560,"mc":106996694935,"s":34909199,"m":"KOSDAQ"},"price_source_validation":{"price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shards":["atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv","atlas/ohlcv_tradable_by_symbol_year/024/024840/2025.csv"],"mfe_mae_window_basis":"entry row inclusive N tradable rows","manifest_max_date":"2026-02-20"},"MFE_30D_pct":15.17,"MAE_30D_pct":-17.46,"MFE_90D_pct":15.17,"MAE_90D_pct":-45.61,"MFE_180D_pct":15.17,"MAE_180D_pct":-47.9,"peak_180D_date":"2024-08-16","peak_180D_price":3530.0,"drawdown_after_peak_pct":-54.76,"trough_after_peak_date":"2025-04-09","corporate_action_window_status":"clean_180D_window","forward_window_trading_rows":180,"evidence_date":"2024-08-14","evidence_url":"https://www.mk.co.kr/en/business/11092877","evidence_summary":"First-half operating profit jumped sharply, but the article frames stable operating activities/copper-wire manufacturing rather than a power-grid/data-center order backlog bridge.","case_role":"earnings_swing_counterexample","direct_bridge_verdict":"earnings_swing_yes__grid_order_backlog_no","residual_label":"earnings_without_order_backlog_is_capped_stage2","current_profile_simulated_stage":"Stage2-Actionable","recommended_stage":"Stage2","raw_total_score":78.0,"recommended_total_score":69.0,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"primary","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"row_type":"score_simulation","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|024840|Stage2|2024-08-14","score_component_context":{"eps_fcf_explosion":"direct bridge only if order/backlog/margin or revenue conversion appears","earnings_visibility":"boost for direct Q1/Q2 revenue/profit/order bridge; cap for commodity/product-profile only","bottleneck_pricing":"boost for transformer/cable backlog and capacity tightness; reduce for copper-wire proxy","market_mispricing":"keep positive only when non-price bridge survives high MAE","valuation_rerating":"Green blocker if evidence is profile-only, peak-proximate, or high-MAE without cash/FCF confirmation","information_confidence":"direct issuer/company/major-news source > analyst-only > profile-only"},"current_profile_simulated_stage":"Stage2-Actionable","recommended_stage":"Stage2","current_profile_error":"would_lift_spread_or_copper_wire_earnings_into_c02_actionable","component_adjustment_summary":"cap earnings-only copper wire improvement at Stage2 until explicit grid/data-center order conversion exists","production_scoring_changed":false}
{"row_type":"v12_trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":204,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR","symbol":"103590","company":"Iljin Electric","case_id":"C02_103590_20241017_STAGE2A_US_CONTRACT_REVENUE_BRIDGE","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage2-Actionable|2024-10-17","trigger_type":"Stage2-Actionable","entry_date":"2024-10-17","entry_price":26100.0,"actual_entry_ohlcv":{"d":"2024-10-17","o":23550,"h":26350,"l":23500,"c":26100,"v":4174733,"a":104565656050,"mc":1244588679000,"s":47685390,"m":"KOSPI"},"price_source_validation":{"price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shards":["atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv","atlas/ohlcv_tradable_by_symbol_year/103/103590/2025.csv"],"mfe_mae_window_basis":"entry row inclusive N tradable rows","manifest_max_date":"2026-02-20"},"MFE_30D_pct":14.94,"MAE_30D_pct":-20.69,"MFE_90D_pct":43.87,"MAE_90D_pct":-21.46,"MFE_180D_pct":59.39,"MAE_180D_pct":-24.14,"peak_180D_date":"2025-06-30","peak_180D_price":41600.0,"drawdown_after_peak_pct":-15.14,"trough_after_peak_date":"2025-07-07","corporate_action_window_status":"clean_180D_window","forward_window_trading_rows":180,"evidence_date":"2024-10-17","evidence_url":"https://www.asiae.co.kr/en/article/2024101708454510488","evidence_summary":"Analyst article cites expected earnings improvement and a large U.S. ultra-high-voltage transformer contract, with revenue recognition expected to grow from 2025.","case_role":"direct_us_transformer_order_positive_control","direct_bridge_verdict":"us_transformer_contract_to_revenue_recognition_bridge","residual_label":"direct_us_contract_bridge_allows_actionable_but_not_green","current_profile_simulated_stage":"Stage3-Yellow","recommended_stage":"Stage2-Actionable","raw_total_score":86.0,"recommended_total_score":81.0,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"primary","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"row_type":"score_simulation","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage2-Actionable|2024-10-17","score_component_context":{"eps_fcf_explosion":"direct bridge only if order/backlog/margin or revenue conversion appears","earnings_visibility":"boost for direct Q1/Q2 revenue/profit/order bridge; cap for commodity/product-profile only","bottleneck_pricing":"boost for transformer/cable backlog and capacity tightness; reduce for copper-wire proxy","market_mispricing":"keep positive only when non-price bridge survives high MAE","valuation_rerating":"Green blocker if evidence is profile-only, peak-proximate, or high-MAE without cash/FCF confirmation","information_confidence":"direct issuer/company/major-news source > analyst-only > profile-only"},"current_profile_simulated_stage":"Stage3-Yellow","recommended_stage":"Stage2-Actionable","current_profile_error":"high_MAE_should_cap_green_not_remove_actionable","component_adjustment_summary":"preserve order/revenue bridge but apply high-MAE and margin-timing cap before Yellow/Green","production_scoring_changed":false}
{"row_type":"v12_trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":204,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR","symbol":"267260","company":"HD Hyundai Electric","case_id":"C02_267260_20250422_STAGE2A_DIRECT_BACKLOG_MARGIN","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage2-Actionable|2025-04-22","trigger_type":"Stage2-Actionable","entry_date":"2025-04-22","entry_price":301000.0,"actual_entry_ohlcv":{"d":"2025-04-22","o":329000,"h":333500,"l":300000,"c":301000,"v":706084,"a":221732415500,"mc":10850187635000,"s":36047135,"m":"KOSPI"},"price_source_validation":{"price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shards":["atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv","atlas/ohlcv_tradable_by_symbol_year/267/267260/2026.csv"],"mfe_mae_window_basis":"entry row inclusive N tradable rows","manifest_max_date":"2026-02-20"},"MFE_30D_pct":34.39,"MAE_30D_pct":-3.16,"MFE_90D_pct":72.76,"MAE_90D_pct":-3.16,"MFE_180D_pct":224.25,"MAE_180D_pct":-3.16,"peak_180D_date":"2025-11-04","peak_180D_price":976000.0,"drawdown_after_peak_pct":-24.59,"trough_after_peak_date":"2025-12-01","corporate_action_window_status":"clean_180D_window","forward_window_trading_rows":180,"evidence_date":"2025-04-22","evidence_url":"https://en.yna.co.kr/view/AEN20250422006151320","evidence_summary":"Q1 2025 orders, order backlog, sales, operating profit, and North-America profitability all pointed to direct grid-equipment backlog-to-margin conversion.","case_role":"direct_backlog_margin_positive_control","direct_bridge_verdict":"orders_backlog_sales_operating_profit_margin_bridge","residual_label":"direct_backlog_margin_bridge_preserves_actionable","current_profile_simulated_stage":"Stage3-Yellow","recommended_stage":"Stage2-Actionable","raw_total_score":88.5,"recommended_total_score":84.0,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"primary","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"row_type":"score_simulation","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage2-Actionable|2025-04-22","score_component_context":{"eps_fcf_explosion":"direct bridge only if order/backlog/margin or revenue conversion appears","earnings_visibility":"boost for direct Q1/Q2 revenue/profit/order bridge; cap for commodity/product-profile only","bottleneck_pricing":"boost for transformer/cable backlog and capacity tightness; reduce for copper-wire proxy","market_mispricing":"keep positive only when non-price bridge survives high MAE","valuation_rerating":"Green blocker if evidence is profile-only, peak-proximate, or high-MAE without cash/FCF confirmation","information_confidence":"direct issuer/company/major-news source > analyst-only > profile-only"},"current_profile_simulated_stage":"Stage3-Yellow","recommended_stage":"Stage2-Actionable","current_profile_error":"underweights_direct_order_backlog_vs_proxy_theme","component_adjustment_summary":"direct order/backlog/margin bridge gets high-quality Actionable; Green still waits for valuation/FCF breadth","production_scoring_changed":false}
{"row_type":"v12_trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":204,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR","symbol":"001440","company":"Taihan Cable & Solution","case_id":"C02_001440_20250430_STAGE2A_GLOBAL_ORDERS_Q1","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|001440|Stage2-Actionable|2025-04-30","trigger_type":"Stage2-Actionable","entry_date":"2025-04-30","entry_price":11630.0,"actual_entry_ohlcv":{"d":"2025-04-30","o":12020,"h":12020,"l":11530,"c":11630,"v":643858,"a":7531064800,"mc":2168382099000,"s":186447300,"m":"KOSPI"},"price_source_validation":{"price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shards":["atlas/ohlcv_tradable_by_symbol_year/001/001440/2025.csv","atlas/ohlcv_tradable_by_symbol_year/001/001440/2026.csv"],"mfe_mae_window_basis":"entry row inclusive N tradable rows","manifest_max_date":"2026-02-20"},"MFE_30D_pct":45.66,"MAE_30D_pct":-0.86,"MFE_90D_pct":56.23,"MAE_90D_pct":-0.86,"MFE_180D_pct":154.94,"MAE_180D_pct":-0.86,"peak_180D_date":"2026-01-22","peak_180D_price":29650.0,"drawdown_after_peak_pct":-10.62,"trough_after_peak_date":"2026-01-26","corporate_action_window_status":"clean_180D_window","forward_window_trading_rows":180,"evidence_date":"2025-04-30","evidence_url":"https://www.taihan.com/en/news/pr/taihanNewsDetail?idx=683","evidence_summary":"Q1 2025 revenue and operating profit were stable/high, with strong performance attributed to global orders and overseas subsidiaries.","case_role":"direct_cable_orders_positive_control","direct_bridge_verdict":"q1_revenue_profit_global_order_bridge","residual_label":"global_orders_plus_revenue_profit_allows_actionable","current_profile_simulated_stage":"Stage2","recommended_stage":"Stage2-Actionable","raw_total_score":74.0,"recommended_total_score":81.0,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"primary","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"row_type":"score_simulation","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|001440|Stage2-Actionable|2025-04-30","score_component_context":{"eps_fcf_explosion":"direct bridge only if order/backlog/margin or revenue conversion appears","earnings_visibility":"boost for direct Q1/Q2 revenue/profit/order bridge; cap for commodity/product-profile only","bottleneck_pricing":"boost for transformer/cable backlog and capacity tightness; reduce for copper-wire proxy","market_mispricing":"keep positive only when non-price bridge survives high MAE","valuation_rerating":"Green blocker if evidence is profile-only, peak-proximate, or high-MAE without cash/FCF confirmation","information_confidence":"direct issuer/company/major-news source > analyst-only > profile-only"},"current_profile_simulated_stage":"Stage2","recommended_stage":"Stage2-Actionable","current_profile_error":"may_cap_cable_names_too_harshly_after_prior_high_mae_rows","component_adjustment_summary":"direct global order and revenue/profit bridge should reopen Actionable after older cable high-MAE cases","production_scoring_changed":false}
{"row_type":"v12_trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":204,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR","symbol":"000500","company":"Gaon Cable","case_id":"C02_000500_20250430_STAGE2_PROFILE_ONLY_CLEAN_ROW","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|000500|Stage2|2025-04-30","trigger_type":"Stage2","entry_date":"2025-04-30","entry_price":60300.0,"actual_entry_ohlcv":{"d":"2025-04-30","o":60000,"h":62100,"l":57900,"c":60300,"v":120767,"a":7246783550,"mc":997549834500,"s":16543115,"m":"KOSPI"},"price_source_validation":{"price_data_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shards":["atlas/ohlcv_tradable_by_symbol_year/000/000500/2025.csv","atlas/ohlcv_tradable_by_symbol_year/000/000500/2026.csv"],"mfe_mae_window_basis":"entry row inclusive N tradable rows","manifest_max_date":"2026-02-20"},"MFE_30D_pct":38.97,"MAE_30D_pct":-3.98,"MFE_90D_pct":38.97,"MAE_90D_pct":-6.97,"MFE_180D_pct":70.81,"MAE_180D_pct":-12.77,"peak_180D_date":"2026-01-20","peak_180D_price":103000.0,"drawdown_after_peak_pct":-15.15,"trough_after_peak_date":"2026-01-21","corporate_action_window_status":"clean_180D_window","forward_window_trading_rows":180,"evidence_date":"2025-04-30","evidence_url":"https://gaoncable.com/","evidence_summary":"Company product profile confirms extra-high-voltage, distribution, overhead-line and copper-rod exposure, but no event-date customer order/backlog bridge was used.","case_role":"profile_only_positive_path_but_not_actionable","direct_bridge_verdict":"product_profile_only_no_event_order_backlog","residual_label":"profile_only_grid_exposure_remains_stage2_until_order_bridge","current_profile_simulated_stage":"Stage2-Actionable","recommended_stage":"Stage2","raw_total_score":76.0,"recommended_total_score":68.0,"calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"primary","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"row_type":"score_simulation","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|000500|Stage2|2025-04-30","score_component_context":{"eps_fcf_explosion":"direct bridge only if order/backlog/margin or revenue conversion appears","earnings_visibility":"boost for direct Q1/Q2 revenue/profit/order bridge; cap for commodity/product-profile only","bottleneck_pricing":"boost for transformer/cable backlog and capacity tightness; reduce for copper-wire proxy","market_mispricing":"keep positive only when non-price bridge survives high MAE","valuation_rerating":"Green blocker if evidence is profile-only, peak-proximate, or high-MAE without cash/FCF confirmation","information_confidence":"direct issuer/company/major-news source > analyst-only > profile-only"},"current_profile_simulated_stage":"Stage2-Actionable","recommended_stage":"Stage2","current_profile_error":"price_path_was_good_but_profile_only_should_not_be_actionable","component_adjustment_summary":"good forward path cannot promote profile-only row without as-of order/backlog bridge","production_scoring_changed":false}
{"row_type":"shadow_weight_candidate","research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","target_scope":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C02_POWER_GRID_DATACENTER_CAPEX","rule_candidate":"C02_DIRECT_BACKLOG_MARGIN_BRIDGE_AND_PROXY_THEME_4B_GATE","shadow_weight_only":true,"production_scoring_changed":false,"component_delta_candidate":{"earnings_visibility":"+0.15 when issuer-level order/backlog-to-revenue bridge is explicit","bottleneck_pricing":"+0.20 for transformer/cable capacity + customer/order backlog; -0.25 for copper-wire/profile-only proxy","market_mispricing":"-0.10 if entry is theme peak or 90D MAE <= -30 without second bridge","valuation_rerating":"Green blocked until FCF/cash conversion or multi-quarter margin bridge appears","information_confidence":"+0.10 for issuer filing/official release or major wire article with order/backlog numbers"},"guardrail_candidate":{"profile_only_grid_exposure_cap":"Stage2","copper_wire_or_commodity_theme_cap":"Stage2 or Stage4B","stage2_actionable_requires":"at least one direct order/backlog/revenue/margin/capacity/customer bridge","hard_4c_requires":"order cancellation/backlog collapse/customer loss/capacity failure/margin break; high MAE alone is insufficient"}}
```

## 9. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_valid: true
selected_round_present: true
selected_loop_present: true
large_sector_id_present: true
canonical_archetype_id_present: true
fine_archetype_id_present: true

round_sector_consistency:
  R1 -> L1_INDUSTRIALS_INFRA_DEFENSE_GRID: pass
  C02 -> R1/L1 mapping: pass

no_repeat_index_used_as_ledger_only: true
coverage_index_first_selection: true
strict_R1_to_R13_cycle_used: false

hard_duplicate_key_fields_present:
  canonical_archetype_id: true
  symbol: true
  trigger_type: true
  entry_date: true

hard_duplicate_key_policy:
  key_format: canonical_archetype_id + symbol + trigger_type + entry_date
  exact_duplicate_known_in_batch: false
  batch_internal_duplicate_count: 0

price_validation:
  actual_entry_ohlcv_row_present_all: true
  entry_price_present_all: true
  MFE_30D_MAE_30D_present_all: true
  MFE_90D_MAE_90D_present_all: true
  MFE_180D_MAE_180D_present_all: true
  stock_web_shard_path_present_all: true
  manifest_max_date_recorded: true
  corporate_action_screen_recorded_all: true
  insufficient_forward_window_count: 0

source_validation:
  evidence_url_present_all: true
  source_proxy_only_count: 0
  evidence_url_pending_count: 0
  narrative_only_count: 0

balance_validation:
  positive_direct_bridge_count: 4
  counterexample_or_guardrail_count: 3
  stage4b_count: 1
  stage4c_count: 0
  hard_4c_absence_interpreted_as_holdout_signal: true

production_safety:
  production_scoring_changed: false
  code_patch_performed: false
  live_scan_performed: false
  auto_trading_or_recommendation_performed: false
  shadow_weight_only: true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Read this MD as a v12 calibration artifact only.
Do not change production scoring directly.

Potential parser/action items:
1. Ingest JSONL rows where row_type=v12_trigger.
2. Verify dedupe key:
   C02_POWER_GRID_DATACENTER_CAPEX + symbol + trigger_type + entry_date.
3. Add this batch to C02 residual-quality bucket:
   C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR.
4. Treat profile-only/copper-wire proxy rows as Stage2 or Stage4B caps.
5. Treat direct transformer/cable order-backlog-margin rows as Actionable candidates.
6. Keep C02 hard 4C narrow: non-price thesis break required.
7. Apply only as shadow calibration until aggregate validation passes.
```

## 11. Next Research State

```text
completed_round: R1
completed_loop: 204
completed_large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
completed_canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
completed_fine_archetype_id: C02_TRUE_4C_AND_PROXY_THEME_BOUNDARY_REPAIR

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
