# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
round = R2
loop = 1
sector = AI·반도체·전자부품
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
output = standalone_markdown_file
next_round = R3 Loop 1
```

이번 R2는 현재/live 후보 탐색이 아니라 과거 AI·반도체·전자부품 trigger의 **entry timing**을 검증하는 calibration 라운드다.  
핵심 질문은 단순히 “AI/HBM 테마가 좋았나?”가 아니다. 실제 질문은 아래다.

```text
HBM / AI memory:
HBM3E mass production → Nvidia shipment → sold-out capacity → ASP / mix / margin → capex / yield / China-export-control risk

HBM equipment:
SK Hynix contract → TC bonder / advanced packaging capacity → additional customer rumor → relative-strength spike → valuation / customer concentration 4B

Samsung HBM catch-up:
HBM3/HBM3E qualification attempt → Nvidia test failure / heat-power issue → catch-up narrative risk → price failure / delayed rerating
```

이번 라운드는 `stock_agent` 레포를 열지 않았고, 가격은 `Songdaiki/stock-web`의 symbol-year tradable shard만 사용했다.

---

## 1. Round Scope

```text
R2 = AI·반도체·전자부품
```

### Tested question

```text
1. SK하이닉스 HBM first-mover trigger는 Stage3-Green보다 훨씬 앞에서 잡을 수 있었는가?
2. 한미반도체 HBM TC-bonder supply-chain trigger는 Stage2-Actionable로 승격할 만했는가?
3. 삼성전자 HBM catch-up narrative는 Stage2 또는 Yellow로 올릴 수 있었는가, 아니면 4B/false-positive guardrail이 맞았는가?
4. Stage3-Green confirmation은 안전하지만 너무 늦었는가?
5. 4B valuation / positioning / customer-concentration watch는 peak 근처에서 작동했는가?
```

---

## 2. Stock-Web OHLC Input / Price Source Validation

### Manifest / schema / universe

The run validated the required stock-web files before calibration.

```json
{
  "source": "Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Stock-web manifest shows `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `max_date = 2026-02-20`, `tradable_row_count = 14,354,401`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`.  
Schema confirms tradable shard columns `d,o,h,l,c,v,a,mc,s,m` and calibration rules requiring positive OHLC, at least 180 forward tradable days, and no 180D corporate-action contamination.

### Price-source caveat

```text
price_basis = tradable_raw
adjustment_status = raw_unadjusted_marcap
corporate_action_windows_blocked_by_default = true
relative_return_fields = unavailable
```

R2 tickers used here have old corporate-action candidates in profile files, but no corporate-action candidate overlaps the 2024~2025 180D calibration windows used in this run.

---

## 3. Historical Eligibility Gate

| case_id | symbol | company | entry windows | 180D forward available | corporate-action overlap 180D | calibration_usable |
|---|---:|---|---:|---:|---:|---:|
| r2_l1_sk_hynix_hbm_first_mover | 000660 | SK하이닉스 | 2024-03-19 / 2024-05-02 / 2024-06-13 / 2024-07-11 | yes | no | true |
| r2_l1_hanmi_hbm_tcb_supply_chain | 042700 | 한미반도체 | 2024-03-26 / 2024-03-28 / 2024-04-12 / 2024-06-13 | yes | no | true |
| r2_l1_samsung_hbm_catchup_guardrail | 005930 | 삼성전자 | 2024-05-23 | yes | no | true |

```text
calibration_usable_case_count = 3
calibration_usable_trigger_count = 9
```

---

## 4. Canonical Archetypes Tested

```text
HBM_FIRST_MOVER_STAGE2_ACTIONABLE
HBM_CAPACITY_SOLD_OUT_STAGE3_YELLOW
HBM_EQUIPMENT_TCBONDER_STAGE2_ACTIONABLE
HBM_EQUIPMENT_CUSTOMER_EXPANSION_4B
SAMSUNG_HBM_CATCHUP_FALSE_POSITIVE_GUARDRAIL
```

### Archetype interpretation

| archetype | what evidence matters | main risk |
|---|---|---|
| HBM_FIRST_MOVER_STAGE2_ACTIONABLE | HBM3E mass production, Nvidia shipment, booked capacity, AI memory ASP/mix | cycle reversal, capex timing, customer concentration |
| HBM_CAPACITY_SOLD_OUT_STAGE3_YELLOW | capacity sold out / booked, EPS revision, margin mix | Green too late if waiting for full financial confirmation |
| HBM_EQUIPMENT_TCBONDER_STAGE2_ACTIONABLE | SK Hynix order, TSV/TC bonder exposure, HBM packaging bottleneck | single customer, rumor-driven expansion |
| SAMSUNG_HBM_CATCHUP_FALSE_POSITIVE_GUARDRAIL | HBM catch-up narrative without Nvidia qualification | heat/power qualification failure, delayed share recovery |
| HBM_EQUIPMENT_CUSTOMER_EXPANSION_4B | Micron/customer expansion rumor, vertical price spike | rumor not confirmed, valuation / positioning peak |

---

## 5. Case Selection Summary

| bucket | case | symbol | core finding |
|---|---|---:|---|
| structural_success / Stage2-Actionable | SK하이닉스 HBM first-mover | 000660 | 2024-03-19 HBM3E mass production already gave a clean Stage2-Actionable path. Waiting until capacity/profit confirmation was safe but late. |
| structural_success / Stage2-Actionable | 한미반도체 HBM TC bonder supply-chain | 042700 | 2024-03-26 contract/relative-strength trigger gave the best entry; 4B was needed near June peak. |
| failed_rerating / 4B guardrail | 삼성전자 HBM catch-up narrative | 005930 | 2024-05-23 HBM qualification failure source converted catch-up narrative into a 4B/false-positive guardrail, not Stage2 promotion. |

---

## 6. Evidence Source Map

| case_id | trigger | evidence source | evidence available at trigger date |
|---|---|---|---|
| r2_l1_sk_hynix_hbm_first_mover | T1 | Reuters, 2024-03-19 | SK Hynix began mass production of HBM3E, with first shipments to Nvidia expected that month; HBM3E improves heat dissipation and processes up to 1.18 TB/s. |
| r2_l1_sk_hynix_hbm_first_mover | T2 | WSJ, 2024-05-02 | SK Hynix said HBM products were sold out for 2024 and nearly fully booked for 2025; 12-stack HBM3E mass production planned for Q3 2024. |
| r2_l1_hanmi_hbm_tcb_supply_chain | T1/T2 | WSJ, 2024-03-26 / 2024-03-28 | Hanmi supplied SK Hynix with advanced HBM packaging equipment such as TSV-TC bonders and had recent contracts around KRW 200B; media reports of possible Micron deal triggered a second spike. |
| r2_l1_samsung_hbm_catchup_guardrail | T5 | Reuters, 2024-05-23 | Samsung HBM3/HBM3E chips reportedly failed Nvidia tests due to heat and power-consumption issues; Samsung said optimization was ongoing. |

---

## 7. Price Data Source Map

| symbol | profile_path | shard_path examples | profile check |
|---:|---|---|---|
| 000660 | atlas/symbol_profiles/000/000660.json | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv; 2026.csv | old corporate-action candidates only; latest raw close 949000 at 2026-02-20 |
| 042700 | atlas/symbol_profiles/042/042700.json | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv; 2025.csv | old corporate-action candidates only; 2024 windows clean |
| 005930 | atlas/symbol_profiles/005/005930.json | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | 2018 split old candidate; 2024 windows clean |

---

## 8. Case-by-Case Trigger Grid

### Case A — SK하이닉스 / HBM first mover

```text
case_id = r2_l1_sk_hynix_hbm_first_mover
symbol = 000660
primary_archetype = HBM_FIRST_MOVER_STAGE2_ACTIONABLE
```

| trigger | type | trigger_date | evidence | entry_date | entry_price | outcome |
|---|---|---:|---|---:|---:|---|
| T0 | Stage1 awareness | 2024-01-02 | AI memory cycle / HBM leadership narrative | 2024-01-03 | n/a | not scored in this round |
| T1 | Stage2 evidence | 2024-03-19 | HBM3E mass production / Nvidia shipment | 2024-03-19 | 160200 | good_entry |
| T2 | Stage2-Actionable | 2024-05-02 | 2024 HBM sold out, 2025 nearly booked | 2024-05-02 | 173600 | excellent_entry |
| T3 | Stage3-Yellow | 2024-05-23 | HBM demand + price strength + booked capacity | 2024-05-23 | 200000 | good_entry_but_late |
| T4 | Stage3-Green | 2024-06-13 | price / mix / margin confirmation after HBM evidence stack | 2024-06-13 | 222000 | late_entry |
| T5 | Stage4B watch | 2024-07-11 | sharp rerating / positioning / valuation watch | 2024-07-11 | 241000 | peak_near_4b |
| T6 | Stage4C | n/a | no confirmed thesis break inside calibration window | n/a | n/a | hard_4c_not_confirmed |

### Case B — 한미반도체 / HBM TC-bonder supply chain

```text
case_id = r2_l1_hanmi_hbm_tcb_supply_chain
symbol = 042700
primary_archetype = HBM_EQUIPMENT_TCBONDER_STAGE2_ACTIONABLE
```

| trigger | type | trigger_date | evidence | entry_date | entry_price | outcome |
|---|---|---:|---|---:|---:|---|
| T0 | Stage1 awareness | 2024-02-08 | HBM equipment price-volume breakout | 2024-02-08 | 78500 | early_awareness |
| T1 | Stage2 evidence | 2024-03-26 | SK Hynix TSV-TC bonder supply / recent contract wins | 2024-03-26 | 112500 | excellent_entry |
| T2 | Stage2-Actionable | 2024-03-28 | possible Micron customer-expansion report + price confirmation | 2024-03-28 | 134000 | good_entry_with_volatility |
| T3 | Stage3-Yellow | 2024-04-12 | HBM supply chain thesis + repeat contract narrative | 2024-04-12 | 145500 | late_entry |
| T4 | Stage3-Green | n/a | no clean public multi-source Green confirmation separated from price spike | n/a | n/a | no_confirmed_Green |
| T5 | Stage4B watch | 2024-06-13 | vertical price move / customer concentration / valuation risk | 2024-06-13 | 189000 | strong_4b_timing |
| T6 | Stage4C | 2024-09-06 | drawdown / de-rating, but no hard thesis break evidence | 2024-09-06 | 96500 | thesis_break_watch_only |

### Case C — 삼성전자 / HBM catch-up guardrail

```text
case_id = r2_l1_samsung_hbm_catchup_guardrail
symbol = 005930
primary_archetype = SAMSUNG_HBM_CATCHUP_FALSE_POSITIVE_GUARDRAIL
```

| trigger | type | trigger_date | evidence | entry_date | entry_price | outcome |
|---|---|---:|---|---:|---:|---|
| T0 | Stage1 awareness | 2024-01-03 | AI memory recovery / Samsung HBM catch-up narrative | 2024-01-03 | 77000 | weak_watch |
| T1 | Stage2 evidence | n/a | no clean Nvidia qualification evidence by May | n/a | n/a | insufficient_evidence |
| T5 | 4B / false-positive guardrail | 2024-05-23 | reported Nvidia HBM test failure due to heat/power issues | 2024-05-23 | 78300 | false_positive_guardrail |
| T6 | Stage4C | n/a | setback was not final thesis break; catch-up remained possible | n/a | n/a | thesis_break_watch_only |

---

## 9. Trigger-Level OHLC Backtest Tables

### 9.1 Calibration-usable trigger rows

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MFE1Y | MFE2Y | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak | outcome |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| skhynix_T1_20240319 | 000660 | Stage2 | 2024-03-19 | 160200 | 19.5 | 55.1 | 55.1 | 55.1 | 496.1 | -3.8 | -3.8 | -9.7 | 2026-02-20 | 955000 | 0.0 | good_entry |
| skhynix_T2_20240502 | 000660 | Stage2-Actionable | 2024-05-02 | 173600 | 29.6 | 43.1 | 43.1 | 43.1 | 450.1 | -2.1 | -12.7 | -16.6 | 2026-02-20 | 955000 | 0.0 | excellent_entry |
| skhynix_T4_20240613 | 000660 | Stage3-Green | 2024-06-13 | 222000 | 11.9 | 11.9 | 11.9 | 11.9 | 330.2 | -9.9 | -34.8 | -34.8 | 2026-02-20 | 955000 | 0.0 | late_entry |
| skhynix_T5_20240711 | 000660 | Stage4B-watch | 2024-07-11 | 241000 | 3.5 | 3.5 | 3.5 | 3.5 | 296.3 | -13.3 | -40.0 | -40.0 | 2026-02-20 | 955000 | 0.0 | peak_near_4b_but_long_cycle_continued |
| hanmi_T1_20240326 | 042700 | Stage2 | 2024-03-26 | 112500 | 36.2 | 74.4 | 74.4 | 74.4 | 78.2 | -12.4 | -12.4 | -38.1 | 2026-02-20 | 200500 | -65.5 | excellent_entry_then_4B_needed |
| hanmi_T2_20240328 | 042700 | Stage2-Actionable | 2024-03-28 | 134000 | 14.3 | 46.4 | 46.4 | 46.4 | 49.6 | -6.6 | -23.9 | -48.1 | 2026-02-20 | 200500 | -64.5 | good_entry_with_volatility |
| hanmi_T5_20240613 | 042700 | Stage4B-watch | 2024-06-13 | 189000 | 3.8 | 3.8 | 3.8 | 6.1 | 6.1 | -21.3 | -51.0 | -63.2 | 2026-02-20 | 200500 | -65.5 | strong_4b_timing |
| samsung_T5_20240523 | 005930 | 4B / false-positive guardrail | 2024-05-23 | 78300 | 5.4 | 13.4 | 13.4 | 13.4 | 143.0 | -6.1 | -18.0 | -32.1 | 2026-02-20 | 190100 | -40.0 | correct_guardrail |
| samsung_T0_20240103 | 005930 | Stage1/weak watch | 2024-01-03 | 77000 | 2.3 | 11.7 | 15.3 | 15.3 | 116.4 | -8.2 | -8.2 | -19.2 | 2026-01-29 | 166600 | -35.2 | weak_watch_not_green |

**Important:** 1Y/2Y values for long-running AI memory leaders are included for context, but shadow weight calibration below uses 30D/90D/180D only unless explicitly stated. The 2026 HBM cycle extension can make early 2024 signals look even stronger; the cleaner calibration question is whether Stage2/Yellow beat Green over the first 90D/180D window.

---

## 10. 1D Price Path Summaries

### 10.1 SK하이닉스 best early trigger — T1 / 2024-03-19

Entry: 2024-03-19 close 160200.

| offset | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---:|---:|---:|---:|---:|
| D+1 | 2024-03-20 | -2.3 | 0.9 | -3.8 |
| D+2 | 2024-03-21 | 6.1 | 7.1 | -3.8 |
| D+5 | 2024-03-26 | 10.1 | 12.2 | -3.8 |
| D+10 | 2024-04-01 | 15.9 | 18.9 | -3.8 |
| D+20 | 2024-04-16 | 11.7 | 19.5 | -3.8 |
| D+30 | 2024-05-02 | 8.6 | 19.5 | -3.8 |
| D+60 | 2024-06-17 | 39.2 | 43.3 | -3.8 |
| D+90 | 2024-07-25 | 18.6 | 55.1 | -3.8 |
| D+180 | 2024-12-20 | 5.2 | 55.1 | -9.7 |
| D+252 | 2025-03-ish | n/a | 55.1 | n/a |
| D+504 | 2026-02-20 observed | 492.4 | 496.1 | -9.7 |

### 10.2 한미반도체 best early trigger — T1 / 2024-03-26

Entry: 2024-03-26 close 112500.

| offset | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---:|---:|---:|---:|---:|
| D+1 | 2024-03-27 | 1.7 | 5.8 | -12.4 |
| D+2 | 2024-03-28 | 19.1 | 23.6 | -12.4 |
| D+5 | 2024-04-02 | 29.3 | 35.8 | -12.4 |
| D+10 | 2024-04-09 | 18.1 | 36.2 | -12.4 |
| D+20 | 2024-04-23 | 16.8 | 36.2 | -12.4 |
| D+30 | 2024-05-08 | 25.2 | 36.2 | -12.4 |
| D+60 | 2024-06-19 | 57.3 | 74.4 | -12.4 |
| D+90 | 2024-08-07 | -4.1 | 74.4 | -12.4 |
| D+180 | 2024-12-09 | -37.7 | 74.4 | -38.1 |
| D+252 | 2025-03-ish | n/a | 74.4 | -46.7 |
| D+504 | 2026-02-20 observed | 78.2 | 78.2 | -46.7 |

### 10.3 Samsung HBM guardrail trigger — T5 / 2024-05-23

Entry: 2024-05-23 close 78300.

| offset | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---:|---:|---:|---:|---:|
| D+1 | 2024-05-24 | -3.8 | 1.2 | -3.8 |
| D+3 | 2024-05-28 | -0.9 | 1.2 | -5.1 |
| D+5 | 2024-05-30 | -10.2 | 1.2 | -6.1 |
| D+20 | 2024-06-20 | 4.6 | 5.4 | -6.1 |
| D+30 | 2024-07-04 | 8.4 | 8.2 | -6.1 |
| D+60 | 2024-08-19 | 0.0 | 13.4 | -10.5 |
| D+90 | 2024-09-25 | -20.6 | 13.4 | -18.0 |
| D+180 | 2024-12-30 | -32.1 | 13.4 | -32.1 |
| D+504 | 2026-02-20 observed | 142.8 | 143.0 | -40.0 |

This was not a Stage2 promotion case. It was a guardrail case: HBM catch-up narrative existed, but the public evidence on 2024-05-23 was negative qualification evidence.

---

## 11. Case Trigger Comparison

| case_id | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | why |
|---|---|---|---|---|
| r2_l1_sk_hynix_hbm_first_mover | T1/T2 | T4 Stage3-Green | T2 Stage2-Actionable | T2 had booked HBM capacity and clean price strength; T4 Green was safe but lost much of 90D upside. |
| r2_l1_hanmi_hbm_tcb_supply_chain | T1 | T3 Stage3-Yellow / late confirmation | T1 Stage2-Actionable | T1 had contract + supply-chain bottleneck + relative strength; later confirmation came closer to crowded price. |
| r2_l1_samsung_hbm_catchup_guardrail | T5 reject/4B guardrail | possible false Stage2 if narrative-only | reject / 4B guardrail | The relevant evidence was negative qualification evidence, not confirmation. |

---

## 12. Stage2 → Stage4 Audit

### SK하이닉스

1. **Stage2 MFE was large:** T1 MFE90 55.1%, T2 MFE90 43.1%.  
2. **Stage2 MAE was acceptable:** T1 MAE90 -3.8%, T2 MAE90 -12.7%.  
3. **Stage2 beat Green:** T4 Green MFE90 was only 11.9% with MAE90 -34.8%.  
4. **Why Stage2 worked:** HBM3E mass production + Nvidia shipment + capacity sold out / booked evidence created an earnings-visibility bridge before full financial confirmation.  
5. **Calibration verdict:** `Stage3_gate_too_late`; promote HBM first-mover sold-out evidence into Stage2-Actionable / Stage3-Yellow shadow tier.

### 한미반도체

1. **Stage2 MFE was large:** T1 MFE90 74.4%.  
2. **Stage2 MAE was tolerable but not shallow:** T1 MAE90 -12.4%; T2 MAE90 -23.9%.  
3. **Stage2 beat later triggers:** T5 4B entry had MFE90 only 3.8% and MAE90 -51.0%.  
4. **Why Stage2 worked:** confirmed SK Hynix equipment supply + TC-bonder bottleneck + AI/HBM relative strength.  
5. **Calibration verdict:** early evidence should be Stage2-Actionable, but 4B valuation/positioning watch must activate near vertical price spikes.

### 삼성전자

1. **Stage2 promotion failed:** the 2024-05-23 evidence was negative, not positive.  
2. **MAE after guardrail was meaningful:** MAE90 -18.0%, MAE180 -32.1%.  
3. **Why reject was correct:** HBM qualification failure undercut the catch-up thesis.  
4. **Calibration verdict:** narrative-only HBM catch-up must be capped at watch unless customer qualification / mass production evidence closes.

---

## 13. Stage3 Yellow / Green Lateness Audit

### Green lateness ratios

```text
green_lateness_ratio =
(Stage3_Green_entry_price - Stage2_Actionable_entry_price)
/
(peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

| case | Stage2-Actionable entry | Green entry | peak_after_Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| SK하이닉스 | 173600 | 222000 | 248500 | 0.641 | Green captured too little of the initial 90D rerating. |
| 한미반도체 | 112500 | n/a | 196200 | n/a | no confirmed clean Green; T1/T2 acted as Stage2-Actionable, then 4B needed. |
| 삼성전자 | n/a | n/a | n/a | n/a | no valid Green trigger; negative HBM evidence should reject promotion. |

### Interpretation

SK하이닉스 shows the core R2 calibration problem. Green confirmation after full evidence stack was safer, but it gave late entry. The best early trigger was not a vague theme: it had HBM3E mass production, Nvidia shipment, and later sold-out capacity evidence. That is exactly the type of early evidence that should not wait for full Green.

---

## 14. 4B Timing Audit

```text
four_b_peak_proximity =
(Stage4B_entry_price - Stage2_Actionable_entry_price)
/
(peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

| case | Stage2-Actionable price | 4B price | peak price | four_b_peak_proximity | verdict |
|---|---:|---:|---:|---:|---|
| SK하이닉스 | 173600 | 241000 | 248500 | 0.910 | Good near-peak 4B for first-cycle 90D window, but long cycle later resumed. |
| 한미반도체 | 112500 | 189000 | 196200 | 0.914 | Strong 4B timing; 4B captured valuation/positioning risk before deep drawdown. |
| 삼성전자 | n/a | 78300 | 88800 | n/a | 4B was not peak timing; it was false-positive guardrail. |

### 4B lesson

For R2, 4B should not automatically mean thesis exit. In SK하이닉스, July 2024 was a near-term peak watch, but the 2026 HBM supercycle later resumed. In 한미반도체, June 2024 4B was more protective because the post-peak drawdown was severe. Therefore R2 needs two 4B sublabels:

```text
4B-watch-cycle_pause = strong company, near-term crowding/valuation
4B-watch-overheat_customer_concentration = equipment/supplier with vertical rerating and single-customer risk
```

---

## 15. 4C Protection Audit

| case | 4C candidate | label | reasoning |
|---|---|---|---|
| SK하이닉스 | none | hard_4c_not_confirmed | Drawdowns occurred, but no contract/capacity/customer thesis break was confirmed. |
| 한미반도체 | 2024-09-06 watch | thesis_break_watch_only | Price de-rated heavily, but hard evidence of contract cancellation or demand collapse was not confirmed. |
| 삼성전자 | none | false_break_watch_only | 2024-05-23 was a negative qualification setback, not final HBM business collapse. |

R2 should avoid turning every HBM setback into 4C. Qualification delay, customer concentration, or valuation reset is usually 4B/watch first. 4C needs hard evidence: contract cancellation, customer loss, HBM roadmap failure, margin collapse, or accounting/trust issue.

---

## 16. Baseline Score Simulation

`baseline_current_proxy` is a research proxy only. It is not production scoring.

### Baseline behavior

| case | likely baseline selected trigger | stage_label_before | problem |
|---|---|---|---|
| SK하이닉스 | T4 / 2024-06-13 | Stage3-Green | Too late. MFE90 only 11.9% vs T1/T2 55.1% / 43.1%. |
| 한미반도체 | T3 or no clean Green | Stage3-Yellow / watch | Stage2 evidence was actionable; waiting created lower upside and higher drawdown risk. |
| 삼성전자 | could be falsely promoted if narrative-only | Stage2 false positive risk | Negative qualification evidence must block promotion. |

### Proxy component diagnosis

| axis | SK하이닉스 | 한미반도체 | 삼성전자 |
|---|---:|---:|---:|
| evidence_contract_order_score | 65 | 80 | 15 |
| evidence_eps_op_fcf_revision_score | 75 | 55 | 35 |
| evidence_margin_bridge_score | 70 | 45 | 25 |
| evidence_backlog_visibility_score | 85 | 60 | 20 |
| evidence_capacity_or_shipment_score | 90 | 75 | 20 |
| evidence_customer_quality_score | 95 | 85 | 35 |
| evidence_relative_strength_score | 75 | 90 | 35 |
| risk_peak_positioning_score | 45 | 80 | 35 |
| risk_thesis_break_score | 10 | 30 | 55 |

---

## 17. Shadow Profile Optimization Loop

### Profile candidates

| profile_id | hypothesis | selected entry behavior |
|---|---|---|
| P0 baseline_current_proxy | wait for full evidence stack / Green-like confirmation | late for SK, late or noisy for Hanmi, may mishandle Samsung narrative |
| P1 stage2_actionable_early_evidence_plus | promote mass-production + customer-quality + sold-out/capacity or supply contract + relative strength | best R2 profile |
| P2 stage3_yellow_entry_relaxed | allow Yellow when one missing gate remains but customer/volume/revision evidence is strong | good but slightly later |
| P3 green_confirmation_timing_relaxed | relax Green confirmation after booked capacity + price strength | improves SK but risks overpromoting Samsung if guardrail absent |
| P4 four_b_peak_timing_tuned | activate 4B on vertical rerating + customer concentration + valuation/crowding | useful for Hanmi and SK near-term peaks |
| P5 four_c_thesis_break_earlier | earlier 4C on hard qualification/customer failure | rejected for R2 because setbacks were not hard thesis breaks |

### Profile aggregate

| profile_id | case_count | selected_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | hit_rate_MFE90_gt_20 | bad_entry_rate_MAE90_lt_minus_15 | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| baseline_current_proxy | 3 | 3 | 20.0 | 13.4 | -28.3 | -32.1 | 0.33 | 1.00 | 0.33 | 2 | 2 | reference; too late and too narrative-vulnerable |
| stage2_actionable_early_evidence_plus | 3 | 2 | 64.8 | 64.8 | -8.2 | -8.2 | 1.00 | 0.00 | 0.00 | 0 | 0 | best; improves upside capture and reduces false promotion |
| stage3_yellow_entry_relaxed | 3 | 2 | 49.8 | 49.8 | -16.3 | -16.3 | 1.00 | 0.50 | 0.00 | 0 | 1 | good but more volatile |
| green_confirmation_timing_relaxed | 3 | 2 | 38.8 | 38.8 | -17.4 | -17.4 | 1.00 | 0.50 | 0.33 | 1 | 1 | caution; needs Samsung guardrail |
| four_b_peak_timing_tuned | 3 | 2 | 3.8 | 3.8 | -45.5 | -45.5 | 0.00 | 1.00 | 0.00 | n/a | n/a | not entry profile; works as risk overlay |
| four_c_thesis_break_earlier | 3 | 0 | n/a | n/a | n/a | n/a | n/a | n/a | 0.00 | n/a | n/a | rejected; no hard 4C evidence |

---

## 18. Before / After Backtest Comparison

| case_id | symbol | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_entry_date | after_entry_date | baseline_entry_price | after_entry_price | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | baseline_MFE180 | after_MFE180 | baseline_MAE180 | after_MAE180 | return_improvement_90D | risk_change_90D | reason |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| r2_l1_sk_hynix_hbm_first_mover | 000660 | T2 | T4 | T2 | 2024-06-13 | 2024-05-02 | 222000 | 173600 | 11.9 | 43.1 | -34.8 | -12.7 | 11.9 | 43.1 | -34.8 | -16.6 | +31.2 | +22.1 | HBM sold-out/capacity evidence was early and strong enough. |
| r2_l1_hanmi_hbm_tcb_supply_chain | 042700 | T1 | T3 | T1 | 2024-04-12 | 2024-03-26 | 145500 | 112500 | 34.8 | 74.4 | -32.0 | -12.4 | 34.8 | 74.4 | -52.2 | -38.1 | +39.6 | +19.6 | Supply contract + bottleneck + relative strength justified early action. |
| r2_l1_samsung_hbm_catchup_guardrail | 005930 | reject | T5 if narrative-only | reject | 2024-05-23 | n/a | 78300 | n/a | 13.4 | n/a | -18.0 | n/a | 13.4 | n/a | -32.1 | n/a | n/a | avoided false positive | HBM qualification failure blocks promotion. |

### Natural-language conclusion

The best shadow profile is not simply “earlier is better.” The winning rule is **earlier only when evidence is concrete**:

```text
HBM mass production + customer shipment + sold-out/capacity evidence = promote
HBM equipment order + bottleneck + relative strength = promote
HBM catch-up narrative + qualification failure = reject / 4B guardrail
```

---

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE90 | avg_MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_mid_return_high_promote_candidate | 4 | 62 | 78 | 54.8 | -9.1 | Stage2-Actionable should catch these earlier. |
| score_high_return_low_false_positive | 1 | 66 | 44 | 13.4 | -18.0 | Samsung HBM setback must be blocked. |
| score_high_return_high | 1 | 84 | 84 | 34.8 | -32.0 | Hanmi later trigger still had upside but risk was much worse. |
| score_low_return_low_correct_reject | 1 | 40 | 35 | 3.8 | -51.0 | 4B overlay, not entry. |

---

## 20. Weight Sensitivity Table

| axis | baseline | tested | delta | affected_trigger_ids | affected_case_count | avg_MFE90_before | avg_MFE90_after | avg_MAE90_before | avg_MAE90_after | false_positive_before | false_positive_after | missed_structural_before | missed_structural_after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| stage2_actionable_hbm_customer_capacity | 0 | +3 | +3 | skhynix_T1, skhynix_T2 | 1 | 11.9 | 43.1 | -34.8 | -12.7 | 0 | 0 | 1 | 0 | promote adjustment |
| hbm_equipment_order_relative_strength | 0 | +2 | +2 | hanmi_T1, hanmi_T2 | 1 | 34.8 | 74.4 | -32.0 | -12.4 | 0 | 0 | 1 | 0 | positive adjustment |
| qualification_failure_guardrail | 0 | +3 risk block | +3 | samsung_T5 | 1 | 13.4 | reject | -18.0 | n/a | 1 | 0 | 0 | 0 | reject false positive |
| 4b_vertical_rerating_customer_concentration | 60 threshold | 50 threshold when vertical spike | -10 threshold | hanmi_T5, skhynix_T5 | 2 | n/a | n/a | n/a | n/a | 0 | 0 | n/a | n/a | risk overlay, not entry |

---

## 21. Optimization Decision Log

| decision_id | hypothesis | tested_cases | tested_trigger_ids | accepted_or_rejected | delta | reason | why_not_larger_delta | next_validation_needed |
|---|---|---|---|---|---:|---|---|---|
| R2D1 | HBM first-mover mass production + customer shipment + sold-out/capacity should promote earlier than Green | SK하이닉스 | skhynix_T1, skhynix_T2, skhynix_T4 | accepted | +3 | MFE90 improved from 11.9 to 43.1/55.1 while MAE90 improved materially. | Only one pure HBM memory leader case in this round. | Validate Micron/Samsung comparable cases in later US/KR mixed round. |
| R2D2 | HBM equipment order + relative strength should become Stage2-Actionable, with volatility guardrail | 한미반도체 | hanmi_T1, hanmi_T2, hanmi_T5 | accepted | +2 | T1 MFE90 74.4 with MAE90 -12.4; later 4B caught peak risk. | Equipment supplier drawdown was deep after peak, so require 4B overlay. | Add ISC / other HBM supply-chain counterexamples. |
| R2D3 | Samsung HBM catch-up narrative should not promote without qualification evidence | 삼성전자 | samsung_T5 | accepted | +3 risk block | Negative qualification evidence prevented false Stage2/Yellow. | Setback was not hard 4C; do not over-block future confirmed qualification. | Validate Samsung later confirmed supply or HBM4 trigger once 180D window exists. |
| R2D4 | Earlier 4C on HBM setbacks | all | samsung_T5, hanmi_T6 | rejected | 0 | No hard thesis break; setbacks and de-ratings are mostly 4B/watch. | n/a | Need hard cancellation / customer-loss case. |

---

## 22. Overfitting / Robustness Check

```text
usable_trigger_count = 9
usable_case_count = 3
directions_consistent = true for early HBM evidence, mixed for 4C
false_positive_counterexample_present = true, Samsung HBM qualification failure
max_abs_delta_allowed = 3
```

### Robustness notes

1. The early-promotion rule passed SK하이닉스 and 한미반도체, but only where evidence was concrete.
2. The same “HBM” theme failed as a promotion rule for 삼성전자 because customer qualification evidence was negative.
3. The round therefore supports **evidence-specific early promotion**, not broad AI/HBM theme promotion.
4. 4C should not be moved earlier from this sample because no hard thesis break was confirmed.

---

## 23. Cross-case Aggregate Metrics

### Trigger-type aggregate

| trigger_type | usable_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | avg_MFE180 | avg_MAE180 | below_entry_90D_rate | avg_green_lateness_ratio | avg_four_b_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Stage2 | 2 | 64.8 | 64.8 | -8.2 | -8.2 | 64.8 | -24.9 | 0.50 | n/a | n/a | best early entry tier |
| Stage2-Actionable | 2 | 49.8 | 49.8 | -18.2 | -18.2 | 49.8 | -32.3 | 0.50 | n/a | n/a | good with volatility guardrail |
| Stage3-Green / late confirmation | 2 | 23.4 | 23.4 | -33.4 | -33.4 | 23.4 | -43.4 | 1.00 | 0.64 | n/a | too late for R2 winners |
| 4B-watch | 3 | 5.7 | 3.8 | -37.7 | -40.0 | 5.7 | -46.9 | 1.00 | n/a | 0.91 | useful risk overlay, not entry |
| false-positive guardrail | 1 | 13.4 | 13.4 | -18.0 | -18.0 | 13.4 | -32.1 | 1.00 | n/a | n/a | correct reject |

### Profile aggregate

| profile_id | case_count | selected_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | avg_MFE180 | avg_MAE180 | hit_rate_MFE90_gt_20 | bad_entry_rate_MAE90_lt_minus_15 | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| baseline_current_proxy | 3 | 3 | 20.0 | 13.4 | -28.3 | -32.0 | 20.0 | -42.4 | 0.33 | 1.00 | 0.33 | 2 | 2 | too late / false-positive vulnerable |
| stage2_actionable_early_evidence_plus | 3 | 2 | 64.8 | 64.8 | -8.2 | -8.2 | 64.8 | -24.9 | 1.00 | 0.00 | 0.00 | 0 | 0 | selected |
| stage3_yellow_entry_relaxed | 3 | 2 | 49.8 | 49.8 | -16.3 | -16.3 | 49.8 | -32.3 | 1.00 | 0.50 | 0.00 | 0 | 1 | acceptable secondary |
| green_confirmation_timing_relaxed | 3 | 2 | 38.8 | 38.8 | -17.4 | -17.4 | 38.8 | -41.7 | 1.00 | 0.50 | 0.33 | 1 | 1 | only with qualification guardrail |
| four_b_peak_timing_tuned | 3 | 2 | 3.8 | 3.8 | -45.5 | -45.5 | 3.8 | -51.6 | 0.00 | 1.00 | 0.00 | n/a | n/a | risk overlay |
| four_c_thesis_break_earlier | 3 | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 0.00 | n/a | n/a | rejected |

---

## 24. Score-Price Alignment Verdict

```text
score_price_alignment_verdict = early_evidence_specific_promotion_with_guardrails
```

R2 calibration says:

1. HBM first-mover evidence is unusually powerful before full Green.
2. HBM equipment order + relative strength is actionable but volatile.
3. Narrative-only HBM catch-up must not be promoted.
4. Qualification failure / negative customer validation must be a hard promotion block, but not automatic 4C.
5. 4B should be earlier for vertical equipment rerating and near-term HBM leader peak, but must be labelled as watch/overlay, not thesis cancellation.

---

## 25. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_hbm_customer_capacity,0,3,+3,"HBM3E mass production + Nvidia/customer shipment + sold-out capacity produced superior entry vs Green","SK Hynix baseline Green MFE90 11.9 / MAE90 -34.8 improved to Stage2-Actionable MFE90 43.1 / MAE90 -12.7","skhynix_T1_20240319|skhynix_T2_20240502|skhynix_T4_20240613",3,"shadow-only; not production"
shadow_weight,hbm_equipment_order_relative_strength,0,2,+2,"HBM equipment order + relative strength produced high MFE before later confirmation","Hanmi baseline late trigger MFE90 34.8 / MAE90 -32.0 improved to early Stage2 MFE90 74.4 / MAE90 -12.4","hanmi_T1_20240326|hanmi_T2_20240328|hanmi_T5_20240613",3,"shadow-only; pair with 4B overheat guardrail"
shadow_weight,hbm_qualification_failure_promotion_block,0,3,+3,"Negative customer qualification evidence blocked false HBM catch-up promotion","Samsung HBM failure trigger had MAE90 -18.0 and MAE180 -32.1; should be 4B guardrail/reject, not Stage2 promotion","samsung_T5_20240523",1,"shadow-only; not automatic 4C"
```

---

## 26. Machine-Readable Rows

### 26.1 Price source validation row JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 26.2 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"r2_l1_sk_hynix_hbm_first_mover","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"1","sector":"AI·반도체·전자부품","case_type":"structural_success","primary_archetype":"HBM_FIRST_MOVER_STAGE2_ACTIONABLE","best_trigger":"skhynix_T2_20240502","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"missed_structural_if_Green_only","price_source":"Songdaiki/stock-web","notes":"HBM mass production and sold-out capacity evidence supported Stage2-Actionable before full Green."}
{"row_type":"case","case_id":"r2_l1_hanmi_hbm_tcb_supply_chain","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"1","sector":"AI·반도체·전자부품","case_type":"structural_success_with_4B","primary_archetype":"HBM_EQUIPMENT_TCBONDER_STAGE2_ACTIONABLE","best_trigger":"hanmi_T1_20240326","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"Stage2_promote_candidate_with_4B","price_source":"Songdaiki/stock-web","notes":"Early contract/supply-chain evidence was excellent but required 4B near vertical rerating."}
{"row_type":"case","case_id":"r2_l1_samsung_hbm_catchup_guardrail","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"1","sector":"AI·반도체·전자부품","case_type":"failed_rerating_guardrail","primary_archetype":"SAMSUNG_HBM_CATCHUP_FALSE_POSITIVE_GUARDRAIL","best_trigger":"samsung_T5_20240523_reject","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"correct_reject","price_source":"Songdaiki/stock-web","notes":"Negative Nvidia qualification evidence blocked narrative-only HBM catch-up promotion."}
```

### 26.3 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"skhynix_T1_20240319","case_id":"r2_l1_sk_hynix_hbm_first_mover","symbol":"000660","trigger_type":"Stage2","trigger_date":"2024-03-19","entry_date":"2024-03-19","entry_price":160200,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":19.5,"MFE_90D_pct":55.1,"MFE_180D_pct":55.1,"MFE_1Y_pct":55.1,"MFE_2Y_pct":496.1,"MAE_30D_pct":-3.8,"MAE_90D_pct":-3.8,"MAE_180D_pct":-9.7,"MAE_1Y_pct":-9.7,"peak_date":"2026-02-20","peak_price":955000,"drawdown_after_peak_pct":0.0,"green_lateness_ratio":0.641,"four_b_peak_proximity":null,"trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"skhynix_T2_20240502","case_id":"r2_l1_sk_hynix_hbm_first_mover","symbol":"000660","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":173600,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":29.6,"MFE_90D_pct":43.1,"MFE_180D_pct":43.1,"MFE_1Y_pct":43.1,"MFE_2Y_pct":450.1,"MAE_30D_pct":-2.1,"MAE_90D_pct":-12.7,"MAE_180D_pct":-16.6,"MAE_1Y_pct":-16.6,"peak_date":"2026-02-20","peak_price":955000,"drawdown_after_peak_pct":0.0,"green_lateness_ratio":0.641,"four_b_peak_proximity":0.91,"trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"skhynix_T4_20240613","case_id":"r2_l1_sk_hynix_hbm_first_mover","symbol":"000660","trigger_type":"Stage3-Green","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":222000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":11.9,"MFE_90D_pct":11.9,"MFE_180D_pct":11.9,"MFE_1Y_pct":11.9,"MFE_2Y_pct":330.2,"MAE_30D_pct":-9.9,"MAE_90D_pct":-34.8,"MAE_180D_pct":-34.8,"MAE_1Y_pct":-34.8,"peak_date":"2026-02-20","peak_price":955000,"drawdown_after_peak_pct":0.0,"green_lateness_ratio":0.641,"four_b_peak_proximity":null,"trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"hanmi_T1_20240326","case_id":"r2_l1_hanmi_hbm_tcb_supply_chain","symbol":"042700","trigger_type":"Stage2","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":112500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":36.2,"MFE_90D_pct":74.4,"MFE_180D_pct":74.4,"MFE_1Y_pct":74.4,"MFE_2Y_pct":78.2,"MAE_30D_pct":-12.4,"MAE_90D_pct":-12.4,"MAE_180D_pct":-38.1,"MAE_1Y_pct":-46.7,"peak_date":"2026-02-20","peak_price":200500,"drawdown_after_peak_pct":-65.5,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":0.914,"trigger_outcome_label":"excellent_entry_then_4B_needed","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"hanmi_T2_20240328","case_id":"r2_l1_hanmi_hbm_tcb_supply_chain","symbol":"042700","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-28","entry_date":"2024-03-28","entry_price":134000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":14.3,"MFE_90D_pct":46.4,"MFE_180D_pct":46.4,"MFE_1Y_pct":46.4,"MFE_2Y_pct":49.6,"MAE_30D_pct":-6.6,"MAE_90D_pct":-23.9,"MAE_180D_pct":-48.1,"MAE_1Y_pct":-55.2,"peak_date":"2026-02-20","peak_price":200500,"drawdown_after_peak_pct":-64.5,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":0.914,"trigger_outcome_label":"good_entry_with_volatility","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"hanmi_T5_20240613","case_id":"r2_l1_hanmi_hbm_tcb_supply_chain","symbol":"042700","trigger_type":"Stage4B-watch","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":189000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.8,"MFE_90D_pct":3.8,"MFE_180D_pct":3.8,"MFE_1Y_pct":6.1,"MFE_2Y_pct":6.1,"MAE_30D_pct":-21.3,"MAE_90D_pct":-51.0,"MAE_180D_pct":-63.2,"MAE_1Y_pct":-68.3,"peak_date":"2026-02-20","peak_price":200500,"drawdown_after_peak_pct":-65.5,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":0.914,"trigger_outcome_label":"strong_4b_timing","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"samsung_T5_20240523","case_id":"r2_l1_samsung_hbm_catchup_guardrail","symbol":"005930","trigger_type":"4B_false_positive_guardrail","trigger_date":"2024-05-23","entry_date":"2024-05-23","entry_price":78300,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.4,"MFE_90D_pct":13.4,"MFE_180D_pct":13.4,"MFE_1Y_pct":13.4,"MFE_2Y_pct":143.0,"MAE_30D_pct":-6.1,"MAE_90D_pct":-18.0,"MAE_180D_pct":-32.1,"MAE_1Y_pct":-40.0,"peak_date":"2026-02-20","peak_price":190100,"drawdown_after_peak_pct":-40.0,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":"not_applicable","trigger_outcome_label":"correct_guardrail","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"samsung_T0_20240103","case_id":"r2_l1_samsung_hbm_catchup_guardrail","symbol":"005930","trigger_type":"Stage1_weak_watch","trigger_date":"2024-01-03","entry_date":"2024-01-03","entry_price":77000,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.3,"MFE_90D_pct":11.7,"MFE_180D_pct":15.3,"MFE_1Y_pct":15.3,"MFE_2Y_pct":116.4,"MAE_30D_pct":-8.2,"MAE_90D_pct":-8.2,"MAE_180D_pct":-19.2,"MAE_1Y_pct":-35.2,"peak_date":"2026-01-29","peak_price":166600,"drawdown_after_peak_pct":-35.2,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":"not_applicable","trigger_outcome_label":"weak_watch_not_green","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[]}
```

### 26.4 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r2_l1_sk_hynix_hbm_first_mover","trigger_id":"skhynix_T4_20240613","symbol":"000660","trigger_type":"Stage3-Green","weighted_score":86,"stage_label":"Stage3-Green","selected_by_profile":true,"MFE_90D_pct":11.9,"MAE_90D_pct":-34.8,"score_return_alignment_label":"score_high_return_low_false_positive_for_timing"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus","case_id":"r2_l1_sk_hynix_hbm_first_mover","trigger_id":"skhynix_T2_20240502","symbol":"000660","trigger_type":"Stage2-Actionable","weighted_score":79,"stage_label":"Stage2-Actionable","selected_by_profile":true,"MFE_90D_pct":43.1,"MAE_90D_pct":-12.7,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r2_l1_hanmi_hbm_tcb_supply_chain","trigger_id":"hanmi_T3_20240412","symbol":"042700","trigger_type":"Stage3-Yellow","weighted_score":78,"stage_label":"Stage3-Yellow","selected_by_profile":true,"MFE_90D_pct":34.8,"MAE_90D_pct":-32.0,"score_return_alignment_label":"score_high_return_high_but_late_risk"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus","case_id":"r2_l1_hanmi_hbm_tcb_supply_chain","trigger_id":"hanmi_T1_20240326","symbol":"042700","trigger_type":"Stage2-Actionable","weighted_score":77,"stage_label":"Stage2-Actionable","selected_by_profile":true,"MFE_90D_pct":74.4,"MAE_90D_pct":-12.4,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r2_l1_samsung_hbm_catchup_guardrail","trigger_id":"samsung_T5_20240523","symbol":"005930","trigger_type":"4B_false_positive_guardrail","weighted_score":66,"stage_label":"Stage2_if_narrative_only","selected_by_profile":false,"MFE_90D_pct":13.4,"MAE_90D_pct":-18.0,"score_return_alignment_label":"score_high_return_low_false_positive"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus","case_id":"r2_l1_samsung_hbm_catchup_guardrail","trigger_id":"samsung_T5_20240523","symbol":"005930","trigger_type":"4B_false_positive_guardrail","weighted_score":44,"stage_label":"Reject_or_4B_watch","selected_by_profile":false,"MFE_90D_pct":13.4,"MAE_90D_pct":-18.0,"score_return_alignment_label":"score_low_return_low_correct_reject"}
```

### 26.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,verdict
profile_comparison,baseline_current_proxy,3,20.0,-28.3,0.33,1.00,0.33,2,2,"reference; too late and false-positive vulnerable"
profile_comparison,stage2_actionable_early_evidence_plus,3,64.8,-8.2,1.00,0.00,0.00,0,0,"best; improves upside capture with acceptable MAE"
profile_comparison,stage3_yellow_entry_relaxed,3,49.8,-16.3,1.00,0.50,0.00,0,1,"good secondary profile but needs volatility control"
profile_comparison,green_confirmation_timing_relaxed,3,38.8,-17.4,1.00,0.50,0.33,1,1,"use only with qualification guardrail"
profile_comparison,four_b_peak_timing_tuned,3,3.8,-45.5,0.00,1.00,0.00,0,0,"risk overlay, not entry profile"
profile_comparison,four_c_thesis_break_earlier,3,, , , ,0.00,0,0,"rejected; no hard 4C evidence"
```

### 26.6 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"R2D1","hypothesis":"HBM first-mover mass production plus customer shipment and sold-out capacity should promote earlier than Green","tested_trigger_ids":["skhynix_T1_20240319","skhynix_T2_20240502","skhynix_T4_20240613"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"SK Hynix MFE90 improved from 11.9 at Green to 43.1 at Stage2-Actionable while MAE90 improved from -34.8 to -12.7.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Only one pure HBM memory leader case in this round.","next_validation_needed":"Validate with Micron/Samsung confirmed qualification cases."}
{"row_type":"optimization_decision","decision_id":"R2D2","hypothesis":"HBM equipment order plus relative strength should be Stage2-Actionable with 4B overlay","tested_trigger_ids":["hanmi_T1_20240326","hanmi_T2_20240328","hanmi_T5_20240613"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus","backtest_result_summary":"Hanmi early trigger MFE90 74.4 / MAE90 -12.4 beat later confirmation MFE90 34.8 / MAE90 -32.0; June 4B was near peak.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"Equipment supplier post-peak drawdown was severe; require 4B overlay.","next_validation_needed":"Find ISC and other HBM packaging-equipment counterexamples."}
{"row_type":"optimization_decision","decision_id":"R2D3","hypothesis":"HBM catch-up narrative should be blocked when customer qualification evidence is negative","tested_trigger_ids":["samsung_T5_20240523"],"baseline_profile":"baseline_current_proxy","selected_profile":"qualification_failure_guardrail","backtest_result_summary":"Samsung negative HBM evidence led to MAE90 -18.0 and MAE180 -32.1; promotion should be blocked.","accepted_or_rejected":"accepted","delta_magnitude":"+3 risk block","why_not_larger_delta":"Setback was not final hard 4C; future qualification can reopen thesis.","next_validation_needed":"Validate later confirmed Samsung HBM supply triggers once 180D forward window exists."}
```

---

## 27. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, and shadow score profiles.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules

- Use only rows with calibration_usable=true for weight calibration.
- Reject narrative-only rows for score changes.
- Reject rows without OHLC-derived MFE/MAE.
- Reject rows without at least 180 trading days forward window.
- Reject rows blocked by corporate-action-contaminated 180D window unless the user explicitly allows a separate adjusted-price revalidation.
- Reject shadow_weight rows that do not include before/after backtest effect.
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks

1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_peak_proximity.
6. Validate 4C protection labels.
7. Validate calibration_usable filtering.
8. Validate before/after profile comparison rows.
9. Validate score-return alignment labels.
10. Append valid case rows to abstract case library.
11. Append valid trigger rows to trigger calibration dataset.
12. Append score_simulation and profile_comparison rows to shadow calibration dataset.
13. Append shadow weight rows to shadow calibration profile only if before/after backtest effect exists.
14. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
15. Add tests for optimization decision validation.
16. Produce checkpoint summary.

### Expected output

- Concise implementation summary.
- Files changed.
- Tests run.
- Rows accepted.
- Rows rejected and why.
- Shadow profile rows accepted.
- Shadow weight rows accepted.
- Shadow weight rows rejected.
- No investment recommendation language.

---

## 28. Next Round State

```text
current_round_completed = R2 Loop 1
next_round = R3 Loop 1
next_sector = 2차전지·전기차·친환경
production_scoring_changed = false
shadow_weight_only = true
stock_agent_repo_accessed = false
stock_web_price_atlas_accessed = true
```

---

## 29. Source Notes

### Evidence sources

- Reuters, 2024-03-19: SK Hynix began mass production of HBM3E and planned first shipments to Nvidia that month.
- WSJ, 2024-05-02: SK Hynix said HBM products were sold out for 2024 and nearly fully booked for 2025.
- WSJ, 2024-03-26: SK Hynix and Hanmi rallied on AI/HBM demand; Hanmi supplied SK Hynix with TSV-TC bonders and had recent contract wins.
- WSJ, 2024-03-28: Hanmi rose on media reports of a possible Micron equipment deal; company/customer confirmation was not final.
- Reuters, 2024-05-23: Samsung HBM3/HBM3E reportedly failed Nvidia tests due to heat and power-consumption issues; Samsung said optimization was ongoing.

### Stock-web source files validated

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/universe/all_symbols.csv`
- `diagnostics/chatgpt_bundle.txt`
- `atlas/symbol_profiles/000/000660.json`
- `atlas/symbol_profiles/042/042700.json`
- `atlas/symbol_profiles/005/005930.json`
- `atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/000/000660/2026.csv`
- `atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/042/042700/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv`

### Data quality note

All OHLC backtest values are based on stock-web tradable raw OHLC shards. They are not adjusted-price vendor data. No corporate-action candidate overlaps the 2024 180D windows used for calibration in this round, but the raw/unadjusted caveat remains.
