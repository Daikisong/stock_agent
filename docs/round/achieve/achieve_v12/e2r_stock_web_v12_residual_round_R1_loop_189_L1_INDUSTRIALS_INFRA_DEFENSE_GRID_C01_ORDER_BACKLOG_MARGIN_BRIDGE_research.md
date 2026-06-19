# E2R Historical Calibration Prompt v12 — Stock-Web OHLC Atlas / Sector-Archetype Residual Expansion / MD Handoff

## 0. Metadata

```yaml
research_file: e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round: R1
selected_loop: 189
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance / quality reinforcement after Priority 0 URL-proxy and missing-MFE repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_BACKLOG_MARGIN_FCF_CONVERSION
loop_objective: C01 backlog-to-margin/FCF conversion quality repair, with forecast-only false starts and 4B-not-4C timing checks
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This file is a standalone v12 residual research MD. It does not patch `stock_agent`, does not run live discovery, and does not change production scoring.

---

## 1. Current calibrated profile assumption

Current profile is treated as already post-global calibration. The repeated global axes are not re-proposed:

- Stage2-Actionable evidence bonus is already assumed.
- Stage3-Green remains strict and is not loosened.
- Price-only blowoff remains blocked from positive stage promotion.
- Full 4B still requires non-price evidence.
- Hard 4C still routes to 4C only when the non-price thesis break is confirmed.

Residual question for this loop:

> In C01 order-backlog cyclicals, when does backlog actually become margin and FCF, and when is the evidence only a forecast-only bridge that should remain Stage2 or 4B rather than Stage2-Actionable / Green / hard 4C?

---

## 2. Selection / coverage gap check

The No-Repeat Index says all C01~C32 canonical archetypes are now above the 80-row level, so the next priority is quality repair rather than simple row filling. Priority 0 is direct-URL / source-proxy / missing-MFE repair; Priority 1 names C01 with 188 rows and asks for backlog cases where actual FCF does not convert.

Selected target:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE
rows = 188
focus = backlog가 실제 FCF로 전환되지 않는 반례 보강
selected_reason = previous loop covered C05; next Priority 1 quality-repair target is C01
```

Duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Batch hard keys:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2|2022-04-11
C01_ORDER_BACKLOG_MARGIN_BRIDGE|009540|Stage2-Actionable|2023-02-07
C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2-Actionable|2023-04-06
C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage4B|2024-02-06
C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|Stage3-Yellow|2024-04-25
C01_ORDER_BACKLOG_MARGIN_BRIDGE|329180|Stage2-Actionable|2024-05-07
```

Within-batch same-entry dedupe: pass. `010140` appears twice, but the rows have different trigger families and different entry dates: 2022 forecast-only turnaround language versus 2023 quantified backlog-duration evidence. This is not counted as a new-symbol bonus, but it is an independent hard-key row.

---

## 3. Stock-Web manifest / schema validation

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_path: atlas/schema.json
```

Tradable shard columns used: `d,o,h,l,c,v,a,mc,s,m`.

MFE / MAE method:

```text
entry_price = entry_date close
MFE_N_pct = (max high from entry_date through N tradable sessions / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable sessions / entry_price - 1) * 100
```

All six trigger rows have at least 180 forward tradable sessions before the manifest max date. No selected 180D window overlaps a corporate-action candidate date in the corresponding symbol profile.

---

## 4. Archetype compression map

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = SHIPBUILDING_BACKLOG_MARGIN_FCF_CONVERSION
```

Deep sub-archetype slots represented in this loop:

```text
- forecast_only_turnaround_without_actual_margin_bridge
- loss_narrowing_to_order_margin_bridge
- quantified_backlog_duration_bridge
- actual_loss_but_not_hard_4c
- actual_q1_profit_lng_mix_high_mae_positive
- lng_order_unit_price_delivery_bridge
```

---

## 5. Case summary matrix

| Symbol | Company | Trigger | Entry | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Role |
|---|---|---|---:|---:|---:|---:|---:|---|
| 010140 | Samsung Heavy Industries | Stage2 | 2022-04-11 | 5,550 | 16.22/-2.52 | 16.22/-6.67 | 16.22/-9.91 | counterexample |
| 009540 | HD Korea Shipbuilding & Offshore Engineering | Stage2-Actionable | 2023-02-07 | 79,900 | 8.26/-10.26 | 46.56/-10.26 | 62.70/-10.26 | positive |
| 010140 | Samsung Heavy Industries | Stage2-Actionable | 2023-04-06 | 5,240 | 13.93/-2.10 | 80.73/-2.10 | 80.73/-2.10 | positive |
| 010620 | HD Hyundai Mipo Dockyard | Stage4B | 2024-02-06 | 67,900 | 1.91/-12.22 | 20.77/-13.40 | 80.85/-13.40 | guardrail_counterexample |
| 042660 | Hanwha Ocean | Stage3-Yellow | 2024-04-25 | 32,600 | 4.75/-11.66 | 8.28/-22.09 | 68.71/-22.09 | positive_high_mae_guardrail |
| 329180 | HD Hyundai Heavy Industries | Stage2-Actionable | 2024-05-07 | 140,000 | 4.29/-10.07 | 58.93/-10.07 | 135.71/-10.07 | positive |

---

## 6. Case evidence and price-path audits


### 010140 Samsung Heavy Industries — Stage2 / forecast_only_false_start

```yaml
symbol: "010140"
company_name: "Samsung Heavy Industries"
company_name_kr: "삼성중공업"
trigger_type: "Stage2"
evidence_date: "2022-04-11"
entry_date: "2022-04-11"
entry_price: 5550.0
evidence_family: "turnaround_forecast_without_actual_margin_bridge"
source_type: "news_direct_url"
source_url: "https://www.kedglobal.com/shipping-shipbuilding/newsView/ked202204110011"
```

Evidence: 2022 article framed 2023 turnaround expectations on profitable prior orders while the company was still forecast to post another operating loss in 2022.

Entry OHLCV from Stock-Web tradable shard `atlas/ohlcv_tradable_by_symbol_year/010/010140/2022.csv`:

```text
open=5,430 high=5,550 low=5,410 close=5,550 volume=2,120,051 amount=11,655,032,410 market_cap=4,884,000,000,000
```

Price path:

| Window | End date | MFE % | MAE % | Peak date/price | Trough date/price | closed below entry? |
|---|---:|---:|---:|---|---|---:|
| 30D | 2022-05-23 | 16.22 | -2.52 | 2022-04-22 / 6,450 | 2022-04-11 / 5,410 | True |
| 90D | 2022-08-18 | 16.22 | -6.67 | 2022-04-22 / 6,450 | 2022-07-15 / 5,180 | True |
| 180D | 2022-12-28 | 16.22 | -9.91 | 2022-04-22 / 6,450 | 2022-10-26 / 5,000 | True |
| 1Y | 2023-04-13 | 16.22 | -13.69 | 2022-04-22 / 6,450 | 2023-01-06 / 4,790 | True |

Audit interpretation: Backlog/turnaround language alone was not yet an actionable C01 bridge; 180D MFE stalled at 16.22% and the 1Y window made a deeper low before the later multi-year rerating.

Profile contamination note: corporate_action_candidate_dates=[1998-11-05,1999-01-22,1999-07-21,2016-11-28,2018-05-04,2021-11-19]; no selected 2022/2023 180D overlap.


### 009540 HD Korea Shipbuilding & Offshore Engineering — Stage2-Actionable / loss_narrowing_to_order_margin_bridge

```yaml
symbol: "009540"
company_name: "HD Korea Shipbuilding & Offshore Engineering"
company_name_kr: "HD한국조선해양"
trigger_type: "Stage2-Actionable"
evidence_date: "2023-02-07"
entry_date: "2023-02-07"
entry_price: 79900.0
evidence_family: "loss_narrowing_sales_growth_cost_relief"
source_type: "news_direct_url"
source_url: "https://en.yna.co.kr/view/AEN20230207008300320"
```

Evidence: 2022 net loss narrowed sharply; sales rose and operating loss shrank materially from the previous year, giving a cleaner cost/margin bridge than a pure order headline.

Entry OHLCV from Stock-Web tradable shard `atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv`:

```text
open=82,000 high=82,500 low=79,700 close=79,900 volume=240,472 amount=19,406,780,600 market_cap=5,654,771,968,400
```

Price path:

| Window | End date | MFE % | MAE % | Peak date/price | Trough date/price | closed below entry? |
|---|---:|---:|---:|---|---|---:|
| 30D | 2023-03-21 | 8.26 | -10.26 | 2023-02-15 / 86,500 | 2023-03-16 / 71,700 | True |
| 90D | 2023-06-19 | 46.56 | -10.26 | 2023-06-19 / 117,100 | 2023-03-16 / 71,700 | True |
| 180D | 2023-10-31 | 62.70 | -10.26 | 2023-07-17 / 130,000 | 2023-03-16 / 71,700 | True |
| 1Y | 2024-02-15 | 62.7 | -10.26 | 2023-07-17 / 130,000 | 2023-03-16 / 71,700 | True |

Audit interpretation: The as-of setup still carried a -10.26% drawdown, but the 90D/180D MFE of 46.56%/62.70% supports Stage2-Actionable rather than Stage3-Green at entry.

Profile contamination note: corporate_action_candidate_dates=[1999-08-24,2000-01-07,2017-05-10,2018-03-27]; no selected 2023 180D overlap.


### 010140 Samsung Heavy Industries — Stage2-Actionable / confirmed_backlog_duration_bridge

```yaml
symbol: "010140"
company_name: "Samsung Heavy Industries"
company_name_kr: "삼성중공업"
trigger_type: "Stage2-Actionable"
evidence_date: "2023-04-06"
entry_date: "2023-04-06"
entry_price: 5240.0
evidence_family: "backlog_duration_direct_research_pdf"
source_type: "equity_research_direct_pdf"
source_url: "https://rdata.kbsec.com/pdf_data/20230406174254857E.pdf"
```

Evidence: Research report stated shipbuilding/offshore backlog at roughly USD23.8bn, enough work for 3.9 years based on 2023E revenue, at the same entry close used in this test.

Entry OHLCV from Stock-Web tradable shard `atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv`:

```text
open=5,300 high=5,330 low=5,220 close=5,240 volume=3,405,532 amount=17,951,338,600 market_cap=4,611,200,000,000
```

Price path:

| Window | End date | MFE % | MAE % | Peak date/price | Trough date/price | closed below entry? |
|---|---:|---:|---:|---|---|---:|
| 30D | 2023-05-19 | 13.93 | -2.10 | 2023-04-28 / 5,970 | 2023-04-10 / 5,130 | True |
| 90D | 2023-08-16 | 80.73 | -2.10 | 2023-08-02 / 9,470 | 2023-04-10 / 5,130 | True |
| 180D | 2023-12-28 | 80.73 | -2.10 | 2023-08-02 / 9,470 | 2023-04-10 / 5,130 | True |
| 1Y | 2024-04-16 | 80.73 | -2.1 | 2023-08-02 / 9,470 | 2023-04-10 / 5,130 | True |

Audit interpretation: Unlike the 2022 forecast-only setup, this had quantified backlog duration and produced 80.73% MFE in both 90D and 180D with only -2.10% MAE.

Profile contamination note: corporate_action_candidate_dates=[1998-11-05,1999-01-22,1999-07-21,2016-11-28,2018-05-04,2021-11-19]; no selected 2022/2023 180D overlap.


### 010620 HD Hyundai Mipo Dockyard — Stage4B / loss_headline_but_not_hard_4c

```yaml
symbol: "010620"
company_name: "HD Hyundai Mipo Dockyard"
company_name_kr: "HD현대미포"
trigger_type: "Stage4B"
evidence_date: "2024-02-06"
entry_date: "2024-02-06"
entry_price: 67900.0
evidence_family: "actual_loss_with_backlog_cycle_offset"
source_type: "news_direct_url"
source_url: "https://en.yna.co.kr/view/AEN20240206005900320"
```

Evidence: 2023 remained loss-making, with net loss still red; this was a real negative evidence row, but not proof that backlog-to-margin thesis had irreversibly broken.

Entry OHLCV from Stock-Web tradable shard `atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv`:

```text
open=68,100 high=68,400 low=67,500 close=67,900 volume=73,494 amount=4,988,104,800 market_cap=2,712,071,917,100
```

Price path:

| Window | End date | MFE % | MAE % | Peak date/price | Trough date/price | closed below entry? |
|---|---:|---:|---:|---|---|---:|
| 30D | 2024-03-21 | 1.91 | -12.22 | 2024-03-15 / 69,200 | 2024-02-27 / 59,600 | True |
| 90D | 2024-06-20 | 20.77 | -13.40 | 2024-06-20 / 82,000 | 2024-04-16 / 58,800 | True |
| 180D | 2024-11-04 | 80.85 | -13.40 | 2024-07-31 / 122,800 | 2024-04-16 / 58,800 | True |
| 1Y | 2025-02-21 | 112.52 | -13.4 | 2025-01-21 / 144,300 | 2024-04-16 / 58,800 | True |

Audit interpretation: Local 4B was valid because the 90D window drew down -13.40%; hard 4C would have been too severe because 180D MFE reached 80.85% after the market re-priced the cycle.

Profile contamination note: corporate_action_candidate_dates=[1999-07-14,2004-01-29,2018-12-04,2018-12-26]; no selected 2024 180D overlap.


### 042660 Hanwha Ocean — Stage3-Yellow / q1_profit_lng_mix_high_mae_positive

```yaml
symbol: "042660"
company_name: "Hanwha Ocean"
company_name_kr: "한화오션"
trigger_type: "Stage3-Yellow"
evidence_date: "2024-04-25"
entry_date: "2024-04-25"
entry_price: 32600.0
evidence_family: "actual_q1_profit_lng_mix"
source_type: "industry_news_direct_url"
source_url: "https://www.lloydslist.com/LL1148965/Hanwha-Ocean-racks-up-Q1-profit-backed-by-strong-growth-in-LNG-carrier-business"
```

Evidence: The Q1 result showed operating profit and was explicitly attributed to stronger LNG carrier business, giving actual margin evidence rather than only order backlog.

Entry OHLCV from Stock-Web tradable shard `atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv`:

```text
open=33,950 high=34,150 low=32,100 close=32,600 volume=4,021,822 amount=132,306,537,050 market_cap=9,987,300,107,400
```

Price path:

| Window | End date | MFE % | MAE % | Peak date/price | Trough date/price | closed below entry? |
|---|---:|---:|---:|---|---|---:|
| 30D | 2024-06-11 | 4.75 | -11.66 | 2024-04-25 / 34,150 | 2024-05-31 / 28,800 | True |
| 90D | 2024-09-04 | 8.28 | -22.09 | 2024-08-30 / 35,300 | 2024-08-05 / 25,400 | True |
| 180D | 2025-01-21 | 68.71 | -22.09 | 2025-01-21 / 55,000 | 2024-08-05 / 25,400 | True |
| 1Y | 2025-05-13 | 192.33 | -22.09 | 2025-04-28 / 95,300 | 2024-08-05 / 25,400 | True |

Audit interpretation: The 180D MFE of 68.71% validates the positive direction, but the -22.09% MAE says this should remain Yellow/high-MAE until balance-sheet and volatility guardrails clear.

Profile contamination note: corporate_action_candidate_dates=[2016-01-11,2017-10-30,2023-06-13,2023-11-28]; both 2023 candidates are before the 2024-04-25 entry and outside 180D forward window.


### 329180 HD Hyundai Heavy Industries — Stage2-Actionable / lng_order_unit_price_delivery_bridge

```yaml
symbol: "329180"
company_name: "HD Hyundai Heavy Industries"
company_name_kr: "HD현대중공업"
trigger_type: "Stage2-Actionable"
evidence_date: "2024-05-04"
entry_date: "2024-05-07"
entry_price: 140000.0
evidence_family: "lng_order_contract_unit_price_delivery_window"
source_type: "industry_news_direct_url"
source_url: "https://www.imarinenews.com/9004.html"
```

Evidence: Article reported an HD KSOE contract for two LNG carriers worth KRW733.4bn, about USD269m per vessel, to be built by HD Hyundai Heavy Industries and delivered in May 2028.

Entry OHLCV from Stock-Web tradable shard `atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv`:

```text
open=134,700 high=140,000 low=133,100 close=140,000 volume=213,717 amount=29,489,089,100 market_cap=12,428,236,240,000
```

Price path:

| Window | End date | MFE % | MAE % | Peak date/price | Trough date/price | closed below entry? |
|---|---:|---:|---:|---|---|---:|
| 30D | 2024-06-19 | 4.29 | -10.07 | 2024-05-13 / 146,000 | 2024-06-12 / 125,900 | True |
| 90D | 2024-09-12 | 58.93 | -10.07 | 2024-08-09 / 222,500 | 2024-06-12 / 125,900 | True |
| 180D | 2025-02-04 | 135.71 | -10.07 | 2025-01-22 / 330,000 | 2024-06-12 / 125,900 | True |
| 1Y | 2025-05-21 | 208.21 | -10.07 | 2025-05-08 / 431,500 | 2024-06-12 / 125,900 | True |

Audit interpretation: Using the next tradable day after the article, the case produced 135.71% MFE in 180D with -10.07% MAE; this is a clean Stage2-Actionable bridge, not immediate Green.

Profile contamination note: corporate_action_candidate_dates=[]; no selected 180D overlap.


---

## 7. Stage / score-return alignment matrix

| Symbol | Current stage view | Shadow stage view | Residual error label |
|---|---|---|---|
| 010140 | Stage2 / possible Stage2-Actionable if backlog language is over-weighted / total 69.0 | Stage2 only / total 63.0 | stage2_false_positive_if_forecast_backlog_is_promoted_without_actual_margin_or_fcf_bridge |
| 009540 | Stage2-Actionable / total 73.0 | Stage2-Actionable / Stage3-Yellow border, not Green / total 76.0 | none_positive_bridge_with_high_initial_drawdown |
| 010140 | Stage2-Actionable / Stage3-Yellow border / total 76.5 | Stage3-Yellow, not Green until margin/FCF actuals confirm / total 81.0 | none_direct_backlog_duration_bridge |
| 010620 | Stage4C risk if annual red headline dominates / total 45.0 | Stage4B local watch / not full 4C / total 66.0 | overhard_4c_if_red_earnings_headline_is_used_without_backlog_cycle_offset |
| 042660 | Stage3-Yellow / possible Green if profit headline is over-weighted / total 84.0 | Stage3-Yellow high-MAE, not Green / total 80.0 | green_too_early_if_actual_profit_ignores_high_mae_and_balance_sheet_volatility |
| 329180 | Stage2-Actionable / Stage3-Yellow border / total 78.0 | Stage3-Yellow, not Green until earnings conversion / total 82.5 | none_actionable_order_quality_bridge_with_delivery_visibility |


Raw component score simulation, 0-100 component quality scale:

```json
{
  "010140_2022-04-11": {
    "current_total": 69.0,
    "current_stage": "Stage2 / possible Stage2-Actionable if backlog language is over-weighted",
    "shadow_total": 63.0,
    "shadow_stage": "Stage2 only",
    "error_label": "stage2_false_positive_if_forecast_backlog_is_promoted_without_actual_margin_or_fcf_bridge",
    "component_before": {
      "eps_fcf_explosion": 48,
      "earnings_visibility": 60,
      "bottleneck_pricing": 55,
      "market_mispricing": 58,
      "valuation_rerating": 50,
      "capital_allocation": 40,
      "information_confidence": 70
    },
    "component_after": {
      "eps_fcf_explosion": 38,
      "earnings_visibility": 50,
      "bottleneck_pricing": 45,
      "market_mispricing": 48,
      "valuation_rerating": 43,
      "capital_allocation": 38,
      "information_confidence": 72
    }
  },
  "009540_2023-02-07": {
    "current_total": 73.0,
    "current_stage": "Stage2-Actionable",
    "shadow_total": 76.0,
    "shadow_stage": "Stage2-Actionable / Stage3-Yellow border, not Green",
    "error_label": "none_positive_bridge_with_high_initial_drawdown",
    "component_before": {
      "eps_fcf_explosion": 60,
      "earnings_visibility": 70,
      "bottleneck_pricing": 58,
      "market_mispricing": 55,
      "valuation_rerating": 50,
      "capital_allocation": 55,
      "information_confidence": 80
    },
    "component_after": {
      "eps_fcf_explosion": 64,
      "earnings_visibility": 75,
      "bottleneck_pricing": 60,
      "market_mispricing": 55,
      "valuation_rerating": 51,
      "capital_allocation": 58,
      "information_confidence": 82
    }
  },
  "010140_2023-04-06": {
    "current_total": 76.5,
    "current_stage": "Stage2-Actionable / Stage3-Yellow border",
    "shadow_total": 81.0,
    "shadow_stage": "Stage3-Yellow, not Green until margin/FCF actuals confirm",
    "error_label": "none_direct_backlog_duration_bridge",
    "component_before": {
      "eps_fcf_explosion": 62,
      "earnings_visibility": 78,
      "bottleneck_pricing": 70,
      "market_mispricing": 56,
      "valuation_rerating": 58,
      "capital_allocation": 48,
      "information_confidence": 84
    },
    "component_after": {
      "eps_fcf_explosion": 66,
      "earnings_visibility": 84,
      "bottleneck_pricing": 74,
      "market_mispricing": 58,
      "valuation_rerating": 58,
      "capital_allocation": 50,
      "information_confidence": 88
    }
  },
  "010620_2024-02-06": {
    "current_total": 45.0,
    "current_stage": "Stage4C risk if annual red headline dominates",
    "shadow_total": 66.0,
    "shadow_stage": "Stage4B local watch / not full 4C",
    "error_label": "overhard_4c_if_red_earnings_headline_is_used_without_backlog_cycle_offset",
    "component_before": {
      "eps_fcf_explosion": 24,
      "earnings_visibility": 35,
      "bottleneck_pricing": 42,
      "market_mispricing": 38,
      "valuation_rerating": 35,
      "capital_allocation": 45,
      "information_confidence": 74
    },
    "component_after": {
      "eps_fcf_explosion": 44,
      "earnings_visibility": 58,
      "bottleneck_pricing": 54,
      "market_mispricing": 48,
      "valuation_rerating": 44,
      "capital_allocation": 52,
      "information_confidence": 80
    }
  },
  "042660_2024-04-25": {
    "current_total": 84.0,
    "current_stage": "Stage3-Yellow / possible Green if profit headline is over-weighted",
    "shadow_total": 80.0,
    "shadow_stage": "Stage3-Yellow high-MAE, not Green",
    "error_label": "green_too_early_if_actual_profit_ignores_high_mae_and_balance_sheet_volatility",
    "component_before": {
      "eps_fcf_explosion": 75,
      "earnings_visibility": 78,
      "bottleneck_pricing": 72,
      "market_mispricing": 62,
      "valuation_rerating": 60,
      "capital_allocation": 52,
      "information_confidence": 82
    },
    "component_after": {
      "eps_fcf_explosion": 72,
      "earnings_visibility": 76,
      "bottleneck_pricing": 72,
      "market_mispricing": 56,
      "valuation_rerating": 54,
      "capital_allocation": 48,
      "information_confidence": 84
    }
  },
  "329180_2024-05-07": {
    "current_total": 78.0,
    "current_stage": "Stage2-Actionable / Stage3-Yellow border",
    "shadow_total": 82.5,
    "shadow_stage": "Stage3-Yellow, not Green until earnings conversion",
    "error_label": "none_actionable_order_quality_bridge_with_delivery_visibility",
    "component_before": {
      "eps_fcf_explosion": 64,
      "earnings_visibility": 76,
      "bottleneck_pricing": 78,
      "market_mispricing": 58,
      "valuation_rerating": 58,
      "capital_allocation": 54,
      "information_confidence": 82
    },
    "component_after": {
      "eps_fcf_explosion": 68,
      "earnings_visibility": 82,
      "bottleneck_pricing": 82,
      "market_mispricing": 60,
      "valuation_rerating": 58,
      "capital_allocation": 56,
      "information_confidence": 86
    }
  }
}
```

Interpretation:

- Forecast-only backlog / turnaround language should stay Stage2 unless there is a direct margin, cost, delivery, or cash bridge.
- Quantified backlog duration plus actual cost/margin improvement can support Stage2-Actionable or Stage3-Yellow.
- Stage3-Green should not be awarded just because the backlog is large or the first profit print appears; high MAE and cash/capital quality still matter.
- A red earnings headline is valid local 4B evidence, but hard 4C requires irreversible thesis break. The HD Hyundai Mipo 2024 path shows how over-hard 4C would have buried a later valid rerating.

---

## 8. 4B local vs full-window audit

```text
010620 HD Hyundai Mipo:
  local_4B_evidence = 2023 remained in red, 30D MAE -12.22, 90D MAE -13.40
  full_window_result = 180D MFE +80.85, 1Y MFE +112.52
  conclusion = local Stage4B watch was valid; hard Stage4C would be too severe without backlog/cycle offset check

042660 Hanwha Ocean:
  local_positive_evidence = Q1 profit plus LNG mix improvement
  high_MAE_warning = 90D/180D MAE -22.09
  conclusion = Stage3-Yellow is supported; Green is premature until volatility and capital-quality gates clear

010140 Samsung Heavy 2022:
  local_positive_evidence = 2023 turnaround forecast language
  actual_price_path = 180D MFE only +16.22, 1Y MAE -13.69
  conclusion = forecast-only Stage2, not Stage2-Actionable
```

---

## 9. Residual contribution summary

```yaml
new_independent_case_count: 6
new_independent_trigger_count: 6
unique_symbol_count_in_batch: 5
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 4
counterexample_or_guardrail_case_count: 3
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
current_profile_error_count: 3
new_independent_ratio: 1.00
production_scoring_changed: false
shadow_weight_only: true
```

Rule candidate:

```text
C01_BACKLOG_MARGIN_FCF_CONVERSION_GATE
```

Gate logic, shadow only:

```text
If canonical_archetype_id == C01_ORDER_BACKLOG_MARGIN_BRIDGE:
  - Do not promote forecast-only backlog/turnaround language above Stage2 unless at least one bridge exists:
      direct backlog duration + delivery schedule,
      actual margin/cost improvement,
      FCF/working-capital improvement,
      or high-value order quality with ASP/delivery visibility.
  - If red earnings appear while backlog/cycle offset is still intact, prefer local Stage4B watch over hard Stage4C.
  - If actual profit appears but 90D/180D MAE is >20%, keep Stage3-Yellow and block Green until balance-sheet/cash-volatility gates clear.
```

Shadow weight note:

```text
existing_axis_strengthened:
  - stage2_required_bridge
  - direct_evidence_url_quality
  - stage3_yellow_not_green_until_actual_margin_fcf
existing_axis_refined:
  - forecast_only_stage2_false_positive
  - 4B_local_vs_full_4C
  - high_MAE_positive_not_green
existing_axis_weakened:
  - none_global
new_axis_proposed: false
```

---

## 10. Machine-readable JSONL rows

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","selected_round":"R1","selected_loop":189,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_FCF_CONVERSION","case_id":"C01_R1_L189_010140_20220411_Stage2","case_role":"forecast_only_false_start","aggregate_group_role":"counterexample","symbol":"010140","company_name":"Samsung Heavy Industries","trigger_type":"Stage2","trigger_date":"2022-04-11","evidence_date":"2022-04-11","evidence_timing_rule":"entry_date is same tradable date if evidence date is tradable and same-day timing is admissible; otherwise next tradable date. 329180 uses next tradable day after weekend publication.","entry_date":"2022-04-11","entry_price":5550.0,"entry_ohlcv":{"o":5430.0,"h":5550.0,"l":5410.0,"c":5550.0,"v":2120051,"a":11655032410,"mc":4884000000000,"m":"KOSPI"},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_shard":"atlas/ohlcv_tradable_by_symbol_year/010/010140/2022.csv","schema_columns":"d,o,h,l,c,v,a,mc,s,m","forward_180D_trading_rows_available":true,"window_180D_corporate_action_contaminated":false,"corporate_action_note":"corporate_action_candidate_dates=[1998-11-05,1999-01-22,1999-07-21,2016-11-28,2018-05-04,2021-11-19]; no selected 2022/2023 180D overlap.","calibration_usable":true},"price_path":{"window_30D_end_date":"2022-05-23","MFE_30D_pct":16.22,"MAE_30D_pct":-2.52,"peak_30D_date":"2022-04-22","peak_30D_price":6450.0,"trough_30D_date":"2022-04-11","trough_30D_price":5410.0,"window_90D_end_date":"2022-08-18","MFE_90D_pct":16.22,"MAE_90D_pct":-6.67,"peak_90D_date":"2022-04-22","peak_90D_price":6450.0,"trough_90D_date":"2022-07-15","trough_90D_price":5180.0,"window_180D_end_date":"2022-12-28","MFE_180D_pct":16.22,"MAE_180D_pct":-9.91,"peak_180D_date":"2022-04-22","peak_180D_price":6450.0,"trough_180D_date":"2022-10-26","trough_180D_price":5000.0,"window_1Y_end_date":"2023-04-13","MFE_1Y_pct":16.22,"MAE_1Y_pct":-13.69,"peak_1Y_date":"2022-04-22","peak_1Y_price":6450.0,"trough_1Y_date":"2023-01-06","trough_1Y_price":4790.0,"window_2Y_end_date":"2024-04-24","MFE_2Y_pct":82.34,"MAE_2Y_pct":-13.69,"observed_window_end_date":"2025-12-30","observed_full_MFE_pct":485.59,"observed_peak_date":"2025-10-30","observed_peak_price":32500.0,"drawdown_after_observed_peak_pct":-27.08},"evidence":{"evidence_family":"turnaround_forecast_without_actual_margin_bridge","source_title":"Samsung Heavy set for 2023 turnaround after eight years","source_url":"https://www.kedglobal.com/shipping-shipbuilding/newsView/ked202204110011","source_type":"news_direct_url","source_proxy_only":false,"evidence_url_pending":false,"evidence_summary":"2022 article framed 2023 turnaround expectations on profitable prior orders while the company was still forecast to post another operating loss in 2022."},"score_simulation":{"current_total":69.0,"current_stage":"Stage2 / possible Stage2-Actionable if backlog language is over-weighted","shadow_total":63.0,"shadow_stage":"Stage2 only","error_label":"stage2_false_positive_if_forecast_backlog_is_promoted_without_actual_margin_or_fcf_bridge","component_before":{"eps_fcf_explosion":48,"earnings_visibility":60,"bottleneck_pricing":55,"market_mispricing":58,"valuation_rerating":50,"capital_allocation":40,"information_confidence":70},"component_after":{"eps_fcf_explosion":38,"earnings_visibility":50,"bottleneck_pricing":45,"market_mispricing":48,"valuation_rerating":43,"capital_allocation":38,"information_confidence":72}},"dedupe":{"hard_duplicate_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2|2022-04-11","same_entry_group_id":"010140|2022-04-11","dedupe_for_aggregate":false,"is_new_independent_case":true,"reuse_rationale":"same symbol may recur only with different trigger_type/entry_date/evidence_family; hard key is unique"},"residual_contribution":{"production_scoring_changed":false,"shadow_weight_only":true,"residual_label":"stage2_false_positive_if_forecast_backlog_is_promoted_without_actual_margin_or_fcf_bridge","supports_new_axis":false,"supports_existing_axis_refinement":true},"calibration_usable":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","selected_round":"R1","selected_loop":189,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_FCF_CONVERSION","case_id":"C01_R1_L189_009540_20230207_Stage2Actionable","case_role":"loss_narrowing_to_order_margin_bridge","aggregate_group_role":"positive","symbol":"009540","company_name":"HD Korea Shipbuilding & Offshore Engineering","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-07","evidence_date":"2023-02-07","evidence_timing_rule":"entry_date is same tradable date if evidence date is tradable and same-day timing is admissible; otherwise next tradable date. 329180 uses next tradable day after weekend publication.","entry_date":"2023-02-07","entry_price":79900.0,"entry_ohlcv":{"o":82000.0,"h":82500.0,"l":79700.0,"c":79900.0,"v":240472,"a":19406780600,"mc":5654771968400,"m":"KOSPI"},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_shard":"atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv","schema_columns":"d,o,h,l,c,v,a,mc,s,m","forward_180D_trading_rows_available":true,"window_180D_corporate_action_contaminated":false,"corporate_action_note":"corporate_action_candidate_dates=[1999-08-24,2000-01-07,2017-05-10,2018-03-27]; no selected 2023 180D overlap.","calibration_usable":true},"price_path":{"window_30D_end_date":"2023-03-21","MFE_30D_pct":8.26,"MAE_30D_pct":-10.26,"peak_30D_date":"2023-02-15","peak_30D_price":86500.0,"trough_30D_date":"2023-03-16","trough_30D_price":71700.0,"window_90D_end_date":"2023-06-19","MFE_90D_pct":46.56,"MAE_90D_pct":-10.26,"peak_90D_date":"2023-06-19","peak_90D_price":117100.0,"trough_90D_date":"2023-03-16","trough_90D_price":71700.0,"window_180D_end_date":"2023-10-31","MFE_180D_pct":62.7,"MAE_180D_pct":-10.26,"peak_180D_date":"2023-07-17","peak_180D_price":130000.0,"trough_180D_date":"2023-03-16","trough_180D_price":71700.0,"window_1Y_end_date":"2024-02-15","MFE_1Y_pct":62.7,"MAE_1Y_pct":-10.26,"peak_1Y_date":"2023-07-17","peak_1Y_price":130000.0,"trough_1Y_date":"2023-03-16","trough_1Y_price":71700.0,"window_2Y_end_date":"2025-03-04","MFE_2Y_pct":214.77,"MAE_2Y_pct":-10.26,"observed_window_end_date":"2025-12-30","observed_full_MFE_pct":518.9,"observed_peak_date":"2025-11-03","observed_peak_price":494500.0,"drawdown_after_observed_peak_pct":-19.92},"evidence":{"evidence_family":"loss_narrowing_sales_growth_cost_relief","source_title":"KSOE 2022 net loss narrows sharply on weak won and lower costs","source_url":"https://en.yna.co.kr/view/AEN20230207008300320","source_type":"news_direct_url","source_proxy_only":false,"evidence_url_pending":false,"evidence_summary":"2022 net loss narrowed sharply; sales rose and operating loss shrank materially from the previous year, giving a cleaner cost/margin bridge than a pure order headline."},"score_simulation":{"current_total":73.0,"current_stage":"Stage2-Actionable","shadow_total":76.0,"shadow_stage":"Stage2-Actionable / Stage3-Yellow border, not Green","error_label":"none_positive_bridge_with_high_initial_drawdown","component_before":{"eps_fcf_explosion":60,"earnings_visibility":70,"bottleneck_pricing":58,"market_mispricing":55,"valuation_rerating":50,"capital_allocation":55,"information_confidence":80},"component_after":{"eps_fcf_explosion":64,"earnings_visibility":75,"bottleneck_pricing":60,"market_mispricing":55,"valuation_rerating":51,"capital_allocation":58,"information_confidence":82}},"dedupe":{"hard_duplicate_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|009540|Stage2-Actionable|2023-02-07","same_entry_group_id":"009540|2023-02-07","dedupe_for_aggregate":false,"is_new_independent_case":true,"reuse_rationale":"same symbol may recur only with different trigger_type/entry_date/evidence_family; hard key is unique"},"residual_contribution":{"production_scoring_changed":false,"shadow_weight_only":true,"residual_label":"none_positive_bridge_with_high_initial_drawdown","supports_new_axis":false,"supports_existing_axis_refinement":true},"calibration_usable":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","selected_round":"R1","selected_loop":189,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_FCF_CONVERSION","case_id":"C01_R1_L189_010140_20230406_Stage2Actionable","case_role":"confirmed_backlog_duration_bridge","aggregate_group_role":"positive","symbol":"010140","company_name":"Samsung Heavy Industries","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-06","evidence_date":"2023-04-06","evidence_timing_rule":"entry_date is same tradable date if evidence date is tradable and same-day timing is admissible; otherwise next tradable date. 329180 uses next tradable day after weekend publication.","entry_date":"2023-04-06","entry_price":5240.0,"entry_ohlcv":{"o":5300.0,"h":5330.0,"l":5220.0,"c":5240.0,"v":3405532,"a":17951338600,"mc":4611200000000,"m":"KOSPI"},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_shard":"atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv","schema_columns":"d,o,h,l,c,v,a,mc,s,m","forward_180D_trading_rows_available":true,"window_180D_corporate_action_contaminated":false,"corporate_action_note":"corporate_action_candidate_dates=[1998-11-05,1999-01-22,1999-07-21,2016-11-28,2018-05-04,2021-11-19]; no selected 2022/2023 180D overlap.","calibration_usable":true},"price_path":{"window_30D_end_date":"2023-05-19","MFE_30D_pct":13.93,"MAE_30D_pct":-2.1,"peak_30D_date":"2023-04-28","peak_30D_price":5970.0,"trough_30D_date":"2023-04-10","trough_30D_price":5130.0,"window_90D_end_date":"2023-08-16","MFE_90D_pct":80.73,"MAE_90D_pct":-2.1,"peak_90D_date":"2023-08-02","peak_90D_price":9470.0,"trough_90D_date":"2023-04-10","trough_90D_price":5130.0,"window_180D_end_date":"2023-12-28","MFE_180D_pct":80.73,"MAE_180D_pct":-2.1,"peak_180D_date":"2023-08-02","peak_180D_price":9470.0,"trough_180D_date":"2023-04-10","trough_180D_price":5130.0,"window_1Y_end_date":"2024-04-16","MFE_1Y_pct":80.73,"MAE_1Y_pct":-2.1,"peak_1Y_date":"2023-08-02","peak_1Y_price":9470.0,"trough_1Y_date":"2023-04-10","trough_1Y_price":5130.0,"window_2Y_end_date":"2025-04-30","MFE_2Y_pct":202.29,"MAE_2Y_pct":-2.1,"observed_window_end_date":"2025-12-30","observed_full_MFE_pct":520.23,"observed_peak_date":"2025-10-30","observed_peak_price":32500.0,"drawdown_after_observed_peak_pct":-27.08},"evidence":{"evidence_family":"backlog_duration_direct_research_pdf","source_title":"KB Securities Samsung Heavy Industries report, Apr 6 2023","source_url":"https://rdata.kbsec.com/pdf_data/20230406174254857E.pdf","source_type":"equity_research_direct_pdf","source_proxy_only":false,"evidence_url_pending":false,"evidence_summary":"Research report stated shipbuilding/offshore backlog at roughly USD23.8bn, enough work for 3.9 years based on 2023E revenue, at the same entry close used in this test."},"score_simulation":{"current_total":76.5,"current_stage":"Stage2-Actionable / Stage3-Yellow border","shadow_total":81.0,"shadow_stage":"Stage3-Yellow, not Green until margin/FCF actuals confirm","error_label":"none_direct_backlog_duration_bridge","component_before":{"eps_fcf_explosion":62,"earnings_visibility":78,"bottleneck_pricing":70,"market_mispricing":56,"valuation_rerating":58,"capital_allocation":48,"information_confidence":84},"component_after":{"eps_fcf_explosion":66,"earnings_visibility":84,"bottleneck_pricing":74,"market_mispricing":58,"valuation_rerating":58,"capital_allocation":50,"information_confidence":88}},"dedupe":{"hard_duplicate_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2-Actionable|2023-04-06","same_entry_group_id":"010140|2023-04-06","dedupe_for_aggregate":false,"is_new_independent_case":true,"reuse_rationale":"same symbol may recur only with different trigger_type/entry_date/evidence_family; hard key is unique"},"residual_contribution":{"production_scoring_changed":false,"shadow_weight_only":true,"residual_label":"none_direct_backlog_duration_bridge","supports_new_axis":false,"supports_existing_axis_refinement":true},"calibration_usable":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","selected_round":"R1","selected_loop":189,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_FCF_CONVERSION","case_id":"C01_R1_L189_010620_20240206_Stage4B","case_role":"loss_headline_but_not_hard_4c","aggregate_group_role":"guardrail_counterexample","symbol":"010620","company_name":"HD Hyundai Mipo Dockyard","trigger_type":"Stage4B","trigger_date":"2024-02-06","evidence_date":"2024-02-06","evidence_timing_rule":"entry_date is same tradable date if evidence date is tradable and same-day timing is admissible; otherwise next tradable date. 329180 uses next tradable day after weekend publication.","entry_date":"2024-02-06","entry_price":67900.0,"entry_ohlcv":{"o":68100.0,"h":68400.0,"l":67500.0,"c":67900.0,"v":73494,"a":4988104800,"mc":2712071917100,"m":"KOSPI"},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_shard":"atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv","schema_columns":"d,o,h,l,c,v,a,mc,s,m","forward_180D_trading_rows_available":true,"window_180D_corporate_action_contaminated":false,"corporate_action_note":"corporate_action_candidate_dates=[1999-07-14,2004-01-29,2018-12-04,2018-12-26]; no selected 2024 180D overlap.","calibration_usable":true},"price_path":{"window_30D_end_date":"2024-03-21","MFE_30D_pct":1.91,"MAE_30D_pct":-12.22,"peak_30D_date":"2024-03-15","peak_30D_price":69200.0,"trough_30D_date":"2024-02-27","trough_30D_price":59600.0,"window_90D_end_date":"2024-06-20","MFE_90D_pct":20.77,"MAE_90D_pct":-13.4,"peak_90D_date":"2024-06-20","peak_90D_price":82000.0,"trough_90D_date":"2024-04-16","trough_90D_price":58800.0,"window_180D_end_date":"2024-11-04","MFE_180D_pct":80.85,"MAE_180D_pct":-13.4,"peak_180D_date":"2024-07-31","peak_180D_price":122800.0,"trough_180D_date":"2024-04-16","trough_180D_price":58800.0,"window_1Y_end_date":"2025-02-21","MFE_1Y_pct":112.52,"MAE_1Y_pct":-13.4,"peak_1Y_date":"2025-01-21","peak_1Y_price":144300.0,"trough_1Y_date":"2024-04-16","trough_1Y_price":58800.0,"window_2Y_end_date":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"observed_window_end_date":"2025-11-26","observed_full_MFE_pct":278.5,"observed_peak_date":"2025-11-03","observed_peak_price":257000.0,"drawdown_after_observed_peak_pct":-22.84},"evidence":{"evidence_family":"actual_loss_with_backlog_cycle_offset","source_title":"Hyundai Mipo Dockyard remains in red in 2023","source_url":"https://en.yna.co.kr/view/AEN20240206005900320","source_type":"news_direct_url","source_proxy_only":false,"evidence_url_pending":false,"evidence_summary":"2023 remained loss-making, with net loss still red; this was a real negative evidence row, but not proof that backlog-to-margin thesis had irreversibly broken."},"score_simulation":{"current_total":45.0,"current_stage":"Stage4C risk if annual red headline dominates","shadow_total":66.0,"shadow_stage":"Stage4B local watch / not full 4C","error_label":"overhard_4c_if_red_earnings_headline_is_used_without_backlog_cycle_offset","component_before":{"eps_fcf_explosion":24,"earnings_visibility":35,"bottleneck_pricing":42,"market_mispricing":38,"valuation_rerating":35,"capital_allocation":45,"information_confidence":74},"component_after":{"eps_fcf_explosion":44,"earnings_visibility":58,"bottleneck_pricing":54,"market_mispricing":48,"valuation_rerating":44,"capital_allocation":52,"information_confidence":80}},"dedupe":{"hard_duplicate_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage4B|2024-02-06","same_entry_group_id":"010620|2024-02-06","dedupe_for_aggregate":false,"is_new_independent_case":true,"reuse_rationale":"same symbol may recur only with different trigger_type/entry_date/evidence_family; hard key is unique"},"residual_contribution":{"production_scoring_changed":false,"shadow_weight_only":true,"residual_label":"overhard_4c_if_red_earnings_headline_is_used_without_backlog_cycle_offset","supports_new_axis":false,"supports_existing_axis_refinement":true},"calibration_usable":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","selected_round":"R1","selected_loop":189,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_FCF_CONVERSION","case_id":"C01_R1_L189_042660_20240425_Stage3Yellow","case_role":"q1_profit_lng_mix_high_mae_positive","aggregate_group_role":"positive_high_mae_guardrail","symbol":"042660","company_name":"Hanwha Ocean","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-25","evidence_date":"2024-04-25","evidence_timing_rule":"entry_date is same tradable date if evidence date is tradable and same-day timing is admissible; otherwise next tradable date. 329180 uses next tradable day after weekend publication.","entry_date":"2024-04-25","entry_price":32600.0,"entry_ohlcv":{"o":33950.0,"h":34150.0,"l":32100.0,"c":32600.0,"v":4021822,"a":132306537050,"mc":9987300107400,"m":"KOSPI"},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_shard":"atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv","schema_columns":"d,o,h,l,c,v,a,mc,s,m","forward_180D_trading_rows_available":true,"window_180D_corporate_action_contaminated":false,"corporate_action_note":"corporate_action_candidate_dates=[2016-01-11,2017-10-30,2023-06-13,2023-11-28]; both 2023 candidates are before the 2024-04-25 entry and outside 180D forward window.","calibration_usable":true},"price_path":{"window_30D_end_date":"2024-06-11","MFE_30D_pct":4.75,"MAE_30D_pct":-11.66,"peak_30D_date":"2024-04-25","peak_30D_price":34150.0,"trough_30D_date":"2024-05-31","trough_30D_price":28800.0,"window_90D_end_date":"2024-09-04","MFE_90D_pct":8.28,"MAE_90D_pct":-22.09,"peak_90D_date":"2024-08-30","peak_90D_price":35300.0,"trough_90D_date":"2024-08-05","trough_90D_price":25400.0,"window_180D_end_date":"2025-01-21","MFE_180D_pct":68.71,"MAE_180D_pct":-22.09,"peak_180D_date":"2025-01-21","peak_180D_price":55000.0,"trough_180D_date":"2024-08-05","trough_180D_price":25400.0,"window_1Y_end_date":"2025-05-13","MFE_1Y_pct":192.33,"MAE_1Y_pct":-22.09,"peak_1Y_date":"2025-04-28","peak_1Y_price":95300.0,"trough_1Y_date":"2024-08-05","trough_1Y_price":25400.0,"window_2Y_end_date":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"observed_window_end_date":"2025-12-30","observed_full_MFE_pct":365.03,"observed_peak_date":"2025-10-30","observed_peak_price":151600.0,"drawdown_after_observed_peak_pct":-31.73},"evidence":{"evidence_family":"actual_q1_profit_lng_mix","source_title":"Hanwha Ocean racks up Q1 profit backed by strong growth in LNG carrier business","source_url":"https://www.lloydslist.com/LL1148965/Hanwha-Ocean-racks-up-Q1-profit-backed-by-strong-growth-in-LNG-carrier-business","source_type":"industry_news_direct_url","source_proxy_only":false,"evidence_url_pending":false,"evidence_summary":"The Q1 result showed operating profit and was explicitly attributed to stronger LNG carrier business, giving actual margin evidence rather than only order backlog."},"score_simulation":{"current_total":84.0,"current_stage":"Stage3-Yellow / possible Green if profit headline is over-weighted","shadow_total":80.0,"shadow_stage":"Stage3-Yellow high-MAE, not Green","error_label":"green_too_early_if_actual_profit_ignores_high_mae_and_balance_sheet_volatility","component_before":{"eps_fcf_explosion":75,"earnings_visibility":78,"bottleneck_pricing":72,"market_mispricing":62,"valuation_rerating":60,"capital_allocation":52,"information_confidence":82},"component_after":{"eps_fcf_explosion":72,"earnings_visibility":76,"bottleneck_pricing":72,"market_mispricing":56,"valuation_rerating":54,"capital_allocation":48,"information_confidence":84}},"dedupe":{"hard_duplicate_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|Stage3-Yellow|2024-04-25","same_entry_group_id":"042660|2024-04-25","dedupe_for_aggregate":false,"is_new_independent_case":true,"reuse_rationale":"same symbol may recur only with different trigger_type/entry_date/evidence_family; hard key is unique"},"residual_contribution":{"production_scoring_changed":false,"shadow_weight_only":true,"residual_label":"green_too_early_if_actual_profit_ignores_high_mae_and_balance_sheet_volatility","supports_new_axis":false,"supports_existing_axis_refinement":true},"calibration_usable":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","selected_round":"R1","selected_loop":189,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_FCF_CONVERSION","case_id":"C01_R1_L189_329180_20240507_Stage2Actionable","case_role":"lng_order_unit_price_delivery_bridge","aggregate_group_role":"positive","symbol":"329180","company_name":"HD Hyundai Heavy Industries","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-04","evidence_date":"2024-05-04","evidence_timing_rule":"entry_date is same tradable date if evidence date is tradable and same-day timing is admissible; otherwise next tradable date. 329180 uses next tradable day after weekend publication.","entry_date":"2024-05-07","entry_price":140000.0,"entry_ohlcv":{"o":134700.0,"h":140000.0,"l":133100.0,"c":140000.0,"v":213717,"a":29489089100,"mc":12428236240000,"m":"KOSPI"},"price_source_validation":{"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_shard":"atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv","schema_columns":"d,o,h,l,c,v,a,mc,s,m","forward_180D_trading_rows_available":true,"window_180D_corporate_action_contaminated":false,"corporate_action_note":"corporate_action_candidate_dates=[]; no selected 180D overlap.","calibration_usable":true},"price_path":{"window_30D_end_date":"2024-06-19","MFE_30D_pct":4.29,"MAE_30D_pct":-10.07,"peak_30D_date":"2024-05-13","peak_30D_price":146000.0,"trough_30D_date":"2024-06-12","trough_30D_price":125900.0,"window_90D_end_date":"2024-09-12","MFE_90D_pct":58.93,"MAE_90D_pct":-10.07,"peak_90D_date":"2024-08-09","peak_90D_price":222500.0,"trough_90D_date":"2024-06-12","trough_90D_price":125900.0,"window_180D_end_date":"2025-02-04","MFE_180D_pct":135.71,"MAE_180D_pct":-10.07,"peak_180D_date":"2025-01-22","peak_180D_price":330000.0,"trough_180D_date":"2024-06-12","trough_180D_price":125900.0,"window_1Y_end_date":"2025-05-21","MFE_1Y_pct":208.21,"MAE_1Y_pct":-10.07,"peak_1Y_date":"2025-05-08","peak_1Y_price":431500.0,"trough_1Y_date":"2024-06-12","trough_1Y_price":125900.0,"window_2Y_end_date":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"observed_window_end_date":"2025-12-30","observed_full_MFE_pct":357.14,"observed_peak_date":"2025-10-27","observed_peak_price":640000.0,"drawdown_after_observed_peak_pct":-22.42},"evidence":{"evidence_family":"lng_order_contract_unit_price_delivery_window","source_title":"HD Hyundai Heavy Industries receives order for 2 LNG carriers","source_url":"https://www.imarinenews.com/9004.html","source_type":"industry_news_direct_url","source_proxy_only":false,"evidence_url_pending":false,"evidence_summary":"Article reported an HD KSOE contract for two LNG carriers worth KRW733.4bn, about USD269m per vessel, to be built by HD Hyundai Heavy Industries and delivered in May 2028."},"score_simulation":{"current_total":78.0,"current_stage":"Stage2-Actionable / Stage3-Yellow border","shadow_total":82.5,"shadow_stage":"Stage3-Yellow, not Green until earnings conversion","error_label":"none_actionable_order_quality_bridge_with_delivery_visibility","component_before":{"eps_fcf_explosion":64,"earnings_visibility":76,"bottleneck_pricing":78,"market_mispricing":58,"valuation_rerating":58,"capital_allocation":54,"information_confidence":82},"component_after":{"eps_fcf_explosion":68,"earnings_visibility":82,"bottleneck_pricing":82,"market_mispricing":60,"valuation_rerating":58,"capital_allocation":56,"information_confidence":86}},"dedupe":{"hard_duplicate_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|329180|Stage2-Actionable|2024-05-07","same_entry_group_id":"329180|2024-05-07","dedupe_for_aggregate":false,"is_new_independent_case":true,"reuse_rationale":"same symbol may recur only with different trigger_type/entry_date/evidence_family; hard key is unique"},"residual_contribution":{"production_scoring_changed":false,"shadow_weight_only":true,"residual_label":"none_actionable_order_quality_bridge_with_delivery_visibility","supports_new_axis":false,"supports_existing_axis_refinement":true},"calibration_usable":true}
{"row_type":"aggregate","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":6,"new_independent_trigger_count":6,"unique_symbol_count_in_batch":5,"positive_case_count":4,"counterexample_or_guardrail_case_count":3,"calibration_usable_trigger_count":6,"source_proxy_only_count":0,"evidence_url_pending_count":0,"missing_required_mfe_mae_count":0,"corporate_action_contaminated_180D_count":0,"insufficient_forward_window_180D_count":0,"current_profile_error_count":3,"new_independent_ratio":1.0}
{"row_type":"shadow_weight","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","rule_candidate":"C01_BACKLOG_MARGIN_FCF_CONVERSION_GATE","production_scoring_changed":false,"shadow_weight_only":true,"proposed_delta":{"eps_fcf_explosion":0,"earnings_visibility":"+selective if direct margin/FCF bridge","bottleneck_pricing":"no change","market_mispricing":"down-rank forecast-only","valuation_rerating":"no green boost without margin conversion","capital_allocation":"watch cash/working-capital quality","information_confidence":"+direct URL / actual result evidence only"}}
{"row_type":"residual_contribution","research_file":"e2r_stock_web_v12_residual_round_R1_loop_189_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","contribution_label":"C01_backlog_to_margin_FCF_conversion_quality_repair","new_axis_proposed":false,"existing_axis_strengthened":["stage2_required_bridge","direct_evidence_url_quality","stage3_yellow_not_green_until_actual_margin_fcf"],"existing_axis_refined":["4B_local_vs_full_4C","forecast_only_stage2_false_positive"],"existing_axis_weakened":[]}
```

---

## 11. Batch Ingest Self-Audit

```yaml
filename_matches_required_v12_regex: true
metadata_round_matches_filename_round: true
metadata_loop_matches_filename_loop: true
round_sector_consistency: pass
selected_round: R1
selected_loop: 189
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id_present: true
stock_web_manifest_checked: true
stock_web_schema_checked: true
stock_web_actual_1d_ohlcv_used: true
entry_price_present_every_trigger: true
mfe_mae_30_90_180_present_every_trigger: true
corporate_action_window_checked_every_trigger: true
forward_180D_available_every_trigger: true
hard_duplicate_keys_unique_within_batch: true
source_proxy_only_count: 0
evidence_url_pending_count: 0
trigger_type_canonical_labels_only: true
same_entry_deduplication_checked: true
stage2_stage3_4b_4c_alignment_included: true
raw_component_breakdown_included: true
validation_scope_included: true
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

---

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt inside the research session.

You are a coding agent in a later batch implementation session for stock_agent.
Read this Markdown as one v12 residual calibration artifact.
Parse all JSONL rows under section 10.
Validate that every trigger row has:
  - canonical_archetype_id
  - trigger_type
  - symbol
  - entry_date
  - entry_price
  - MFE_30D_pct / MAE_30D_pct
  - MFE_90D_pct / MAE_90D_pct
  - MFE_180D_pct / MAE_180D_pct
  - price_source_validation.calibration_usable == true
  - production_scoring_changed == false

Do not change production scoring directly from this single file.
Add rows to the v12 calibration corpus only if hard duplicate keys are absent from the existing representative set.
If multiple C01 artifacts converge on the same residual, consider a shadow-only rule candidate named:
  C01_BACKLOG_MARGIN_FCF_CONVERSION_GATE

The candidate should be scoped only to:
  large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE

Do not loosen Stage3-Green globally.
Do not promote forecast-only backlog language above Stage2 without a margin/cash/delivery bridge.
Do not route red earnings headlines to hard Stage4C unless the backlog-to-margin thesis is broken and offset evidence is absent.
```

---

## 13. Next Research State

```text
completed_round = R1
completed_loop = 189
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance / quality reinforcement after Priority 0 URL-proxy and missing-MFE repair
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C15_MATERIAL_SPREAD_SUPERCYCLE, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C01_HARD_4C_FCF_BREAK_REPAIR
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
