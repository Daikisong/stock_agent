# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
research_session = historical_calibration_after_stock_web_ohlc_breakthrough
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
round = R1
loop = 1
sector = 산업재·수주·인프라
sector_slug = industrials_orders_infrastructure
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_file = e2r_stock_web_historical_calibration_round_R1_loop_1_industrials_orders_infrastructure_research.md
```

이 파일은 현재/live 후보 탐색이 아니라 과거 trigger-level calibration 파일이다. 이번 실행 중에는 `stock_agent` 레포를 열지 않았고, 가격 검증에는 `Songdaiki/stock-web`의 symbol-year CSV shard만 사용했다.

## 1. Round Scope

```text
R1 = 산업재·수주·인프라
```

이번 R1의 목적은 수주/인프라형 headline이 실제로 어느 trigger에서 좋은 entry가 되었는지 확인하는 것이다. 핵심은 “큰 계약” 자체가 아니라 아래 연결고리다.

```text
계약/수주/우선협상대상자
→ 수주잔고 또는 project visibility
→ capacity / delivery / margin bridge
→ EPS/OP/FCF revision
→ valuation rerating
→ 4B legal / dilution / overheat / execution risk
```

이번 라운드에서는 3개 calibration-usable case를 선택했다.

| case_id | symbol | company | bucket | reason |
|---|---:|---|---|---|
| r1_l1_samsung_ea_fadhili | 028050 | 삼성E&A | EPC contract / counterexample | 대형 EPC 계약은 즉시 반응했지만 180D 구조적 rerating으로 이어지지 못했다. |
| r1_l1_doosan_czech_nuclear | 034020 | 두산에너빌리티 | nuclear infrastructure / missed structural | preferred bidder trigger는 높은 MAE를 동반했지만 1Y MFE가 매우 컸다. |
| r1_l1_ls_electric_us_grid | 010120 | LS ELECTRIC | grid equipment / volatile promote candidate | US grid/data-center 성장 리포트는 큰 upside를 만들었지만 MAE가 깊었다. |

## 2. Stock-Web OHLC Input / Price Source Validation

### 2.1 Manifest validation

`Songdaiki/stock-web`에서 확인한 price atlas 메타데이터:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

### 2.2 Schema validation

Tradable shard columns were interpreted as:

```text
d=date
o=open
h=high
l=low
c=close
v=volume
a=amount
mc=market_cap
s=shares
m=market
```

The schema formula used:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

### 2.3 Price source validation row

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

| rule | status |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in stock-web tradable shard | pass for 028050 / 034020 / 010120 |
| at least 180 forward trading days available | pass |
| high/low/close/volume present | pass |
| MFE/MAE 30D/90D/180D computed | pass |
| 180D corporate-action contamination | no 2024~2025 overlap in selected windows |
| 2Y / 504D full window | unavailable for selected 2024 mid-year triggers because manifest max_date is 2026-02-20 |

Corporate-action candidates in symbol profiles were historical and outside the selected 2024~2025 calibration windows. 2Y fields are therefore marked `insufficient_forward_window_in_stock_web` rather than fabricated.

## 4. Canonical Archetypes Tested

| primary_archetype | tested case | gate being tested |
|---|---|---|
| OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE | 삼성E&A / Fadhili | huge EPC contract + immediate relative strength but margin/cash conversion gate |
| NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B | 두산에너빌리티 / Czech nuclear | preferred bidder vs final contract / legal appeal 4B |
| GRID_EQUIPMENT_US_GROWTH_STAGE2_YELLOW | LS ELECTRIC / US grid growth | report-driven US revenue growth / data-center demand vs volatile valuation |

## 5. Case Selection Summary

| case_id | type | calibration_usable | best_trigger | score_price_alignment |
|---|---|---:|---|---|
| r1_l1_samsung_ea_fadhili | evidence_good_but_price_failed | true | T2 Stage2-Actionable | score_mid_return_low_watch_only |
| r1_l1_doosan_czech_nuclear | missed_structural / volatile_success | true | T1/T2 Stage2-Actionable | score_low_return_high_missed_structural |
| r1_l1_ls_electric_us_grid | Stage2_promote_candidate with MAE risk | true | T1/T2 Stage2-Actionable | score_mid_return_high_promote_candidate |

## 6. Evidence Source Map

| case | trigger | evidence source | evidence available at trigger |
|---|---|---|---|
| 삼성E&A | 2024-04-02 / 2024-04-03 | Reuters, WSJ/MarketWatch | Aramco awarded $7.7B Fadhili expansion contracts to Samsung Engineering, GS E&C and Nesma; project capacity 2.5→4.0 bscf/d, completion Nov 2027. Samsung E&A share rose up to 8.5% on estimated $6B contract while KOSPI fell 1.4%. |
| 두산에너빌리티 | 2024-07-17 | Reuters | Czech government selected KHNP as preferred bidder to build two nuclear reactors; final contract and value still to be negotiated; Doosan Enerbility, KEPCO Plant S&E, KEPCO E&C named as related beneficiaries. |
| 두산에너빌리티 | 2024-10-30 / 2024-10-31 | Reuters | Czech UOHS temporarily blocked contract signing amid EDF/Westinghouse appeals, then rejected/stopped parts of the appeals but decisions were not final. |
| LS ELECTRIC | 2024-07-01 | MarketWatch / WSJ Market Talk | Daiwa raised LS Electric target to KRW280,000; US revenue expected to rise from below 5% of total in 2022 to around 20% in 2024, linked to data-center construction, renewables, and EV value chain. |

Evidence URLs used in this MD:

```text
Reuters — Aramco awards $7.7 bln in contracts for Fadhili gas expansion
https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/

WSJ/MarketWatch — Samsung E&A Shares Rise on $6 Billion Saudi Contract Win
https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4

Reuters — South Korea's winning bid for Czech nuclear power project
https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/

Reuters — Czech watchdog prohibits nuclear power contract signing amid appeals
https://www.reuters.com/business/energy/czech-watchdog-prohibits-nuclear-power-contract-signing-amid-appeals-2024-10-30/

Reuters — Czech watchdog rejects appeals in nuclear power tender
https://www.reuters.com/business/energy/czech-watchdog-rejects-appeals-nuclear-power-tender-2024-10-31/

MarketWatch — LS Electric Could Gain From Solid U.S. Business Growth Opportunity
https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067
```

## 7. Price Data Source Map

| symbol | company | profile_path | shard paths used | profile contamination status |
|---:|---|---|---|---|
| 028050 | 삼성E&A | atlas/symbol_profiles/028/028050.json | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv; 2025.csv | corporate-action candidates exist historically but none overlap selected 2024~2025 windows |
| 034020 | 두산에너빌리티 | atlas/symbol_profiles/034/034020.json | atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv; 2025.csv | corporate-action candidates 2019/2020 only; no selected-window overlap |
| 010120 | LS ELECTRIC | atlas/symbol_profiles/010/010120.json | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; 2025.csv | corporate-action candidates 1995/1999/2003 only; no selected-window overlap |

## 8. Case-by-Case Trigger Grid

### 8.1 Samsung E&A / Fadhili EPC

| trigger_id | type | trigger_date | entry_date | entry_price | evidence | label |
|---|---|---:|---:|---:|---|---|
| r1_samsung_t1 | Stage2 | 2024-04-02 | 2024-04-03 | 25,300 | Aramco award announced after/around market hours; use next tradable close. | Stage2 evidence |
| r1_samsung_t2 | Stage2-Actionable | 2024-04-03 | 2024-04-03 | 25,300 | Samsung E&A contract value/relative strength confirmed by market reaction. | evidence_good_but_price_failed |
| r1_samsung_t5 | 4B-watch | 2024-08-01 | 2024-08-01 | 28,400 | Peak-price/contract-margin conversion watch; no hard 4C evidence. | peak_watch_only |

### 8.2 Doosan Enerbility / Czech nuclear

| trigger_id | type | trigger_date | entry_date | entry_price | evidence | label |
|---|---|---:|---:|---:|---|---|
| r1_doosan_t1 | Stage2 | 2024-07-17 | 2024-07-17 | 21,250 | KHNP selected as preferred bidder. | Stage2 evidence |
| r1_doosan_t2 | Stage2-Actionable | 2024-07-17 | 2024-07-17 | 21,250 | preferred bidder + sector rerating + related-stock beneficiary identification. | missed_structural |
| r1_doosan_t5 | 4B-watch | 2024-10-30 | 2024-10-30 | 21,400 | UOHS temporary contract-signing block amid appeals. | 4B_too_early_or_noise |

### 8.3 LS ELECTRIC / US grid growth

| trigger_id | type | trigger_date | entry_date | entry_price | evidence | label |
|---|---|---:|---:|---:|---|---|
| r1_ls_t1 | Stage2 | 2024-07-01 | 2024-07-01 | 204,500 | Daiwa target + US revenue mix / data-center demand evidence. | Stage2 evidence |
| r1_ls_t2 | Stage2-Actionable | 2024-07-01 | 2024-07-01 | 204,500 | US grid growth thesis, but stock was down that day. | volatile_promote_candidate |
| r1_ls_t5 | 4B-watch | 2024-07-24 | 2024-07-24 | 260,000 | local peak/valuation watch after report-driven rally, no non-price 4B evidence. | price_only_4b_watch |

## 9. Trigger-Level OHLC Backtest Tables

Return unit is percentage, not decimal. `2Y` is unavailable because 504 trading days are not fully available by stock-web manifest max_date.

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | MFE1Y | MAE1Y | MFE2Y | peak_date | peak_price | drawdown_after_peak | usable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| r1_samsung_t1 | 25,300 | 6.72 | -3.75 | 15.81 | -14.62 | 15.81 | -35.57 | 15.81 | -35.57 | unavailable | 2024-08-01 | 29,300 | -44.37 | true |
| r1_samsung_t2 | 25,300 | 6.72 | -3.75 | 15.81 | -14.62 | 15.81 | -35.57 | 15.81 | -35.57 | unavailable | 2024-08-01 | 29,300 | -44.37 | true |
| r1_doosan_t1 | 21,250 | 17.65 | -28.71 | 17.65 | -28.71 | 45.41 | -28.71 | 239.76 | -28.71 | unavailable | 2025-06-30 | 72,200 | -39.4 | true |
| r1_doosan_t2 | 21,250 | 17.65 | -28.71 | 17.65 | -28.71 | 45.41 | -28.71 | 239.76 | -28.71 | unavailable | 2025-06-30 | 72,200 | -39.4 | true |
| r1_doosan_t5 | 21,400 | 6.54 | -20.98 | 44.39 | -20.98 | 45.33 | -20.98 | unavailable | unavailable | unavailable | 2025-02-19 | 30,900 | -35.40 | true |
| r1_ls_t1 | 204,500 | 34.23 | -29.1 | 34.23 | -38.29 | 48.41 | -38.29 | 58.68 | -38.29 | unavailable | 2025-06-24 | 324,500 | -54.03 | true |
| r1_ls_t2 | 204,500 | 34.23 | -29.1 | 34.23 | -38.29 | 48.41 | -38.29 | 58.68 | -38.29 | unavailable | 2025-06-24 | 324,500 | -54.03 | true |

## 10. 1D Price Path Summaries

### 10.1 Samsung E&A — best Stage2-Actionable trigger

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2024-04-04 | +2.96 | +6.32 | 0.00 |
| D+2 | 2024-04-05 | +3.16 | +6.72 | 0.00 |
| D+5 | 2024-04-11 | -1.19 | +6.72 | -2.77 |
| D+10 | 2024-04-18 | +2.77 | +6.72 | -2.96 |
| D+30 | 2024-05-17 | -3.75 | +6.72 | -3.75 |
| D+60 | 2024-07-01 | -5.93 | +6.72 | -14.62 |
| D+90 | 2024-08-13 | +4.35 | +15.81 | -14.62 |
| D+180 | 2024-12-09 | -35.53 | +15.81 | -35.57 |

### 10.2 Doosan Enerbility — preferred bidder trigger

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2024-07-18 | -1.18 | +17.65 | -1.18 |
| D+2 | 2024-07-19 | -4.00 | +17.65 | -5.88 |
| D+10 | 2024-08-01 | -12.00 | +17.65 | -12.00 |
| D+20 | 2024-08-16 | -11.76 | +17.65 | -28.71 |
| D+30 | 2024-08-30 | -14.82 | +17.65 | -28.71 |
| D+90 | 2024-11-12 | -1.65 | +17.65 | -28.71 |
| D+180 | 2025-04-30 | +36.24 | +45.41 | -28.71 |
| D+252 | 2025-06-30 | +221.88 | +239.76 | -28.71 |

### 10.3 LS ELECTRIC — Daiwa US growth trigger

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2024-07-02 | +2.93 | +7.58 | -2.15 |
| D+3 | 2024-07-04 | -1.71 | +7.58 | -4.89 |
| D+10 | 2024-07-15 | +13.69 | +14.43 | -5.87 |
| D+20 | 2024-07-29 | -2.05 | +34.23 | -5.87 |
| D+30 | 2024-08-13 | -17.70 | +34.23 | -29.10 |
| D+60 | 2024-09-19 | -25.00 | +34.23 | -38.29 |
| D+90 | 2024-10-14 | -17.36 | +34.23 | -38.29 |
| D+180 | 2025-03-31 | -14.28 | +48.41 | -38.29 |
| D+252 | 2025-06-24 | +52.08 | +58.68 | -38.29 |

## 11. Case Trigger Comparison

| case_id | best_actual_trigger | why |
|---|---|---|
| r1_l1_samsung_ea_fadhili | T2 Stage2-Actionable, but watch-only | Entry MAE was shallow early, but 180D MFE did not expand and peak-to-trough drawdown was large. This is not a clean structural rerating. |
| r1_l1_doosan_czech_nuclear | T1/T2 Stage2-Actionable | Early trigger had deep MAE, but 1Y MFE was extremely high. A Green-only gate would likely miss the setup. |
| r1_l1_ls_electric_us_grid | T1/T2 Stage2-Actionable with volatility guardrail | Early report was correct about the structural theme, but the path included a -38.29% 90D MAE. It should be promoted only with smaller sizing / Yellow posture. |

## 12. Stage2 → Stage4 Audit

### 12.1 Did Stage2 produce large MFE?

| case | Stage2 MFE90 | Stage2 MFE180 | verdict |
|---|---:|---:|---|
| Samsung E&A | 15.81 | 15.81 | not enough for structural rerating |
| Doosan Enerbility | 17.65 | 45.41 | yes, but not smooth |
| LS ELECTRIC | 34.23 | 48.41 | yes, but drawdown was severe |

### 12.2 Was Stage2 MAE tolerable?

| case | MAE90 | verdict |
|---|---:|---|
| Samsung E&A | -14.62 | acceptable |
| Doosan Enerbility | -28.71 | too deep for full-size Green |
| LS ELECTRIC | -38.29 | too deep for full-size Green |

### 12.3 Main Stage2 lesson

Stage2 evidence should not be ignored in R1 industrials. However, the correct promotion is not automatic Green. The backtest points toward a **Stage2-Actionable / Stage3-Yellow early tier with volatility guardrail**:

```text
promote when:
- contract / preferred bidder / credible report is paired with strategic sector tailwind
- relative strength or volume confirms market attention
- final-contract / margin / execution gate remains open

do not promote to Green when:
- final contract is missing
- report-only thesis has not yet passed price-volatility digestion
- 90D MAE is likely to exceed -25% without new evidence
```

## 13. Stage3 Yellow / Green Lateness Audit

Green trigger was not fully confirmed for the selected early triggers. Therefore:

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger_from_same-day_public_evidence
```

Operational interpretation:

- Doosan and LS suggest that waiting for classical Green can miss the rerating path.
- Samsung E&A shows why early evidence alone cannot be Green; huge EPC contract did not become durable rerating.

## 14. 4B Timing Audit

| case | candidate_4B | four_b_peak_proximity | verdict |
|---|---|---:|---|
| Samsung E&A | 2024-08-01 peak watch | 1.00 | good price-only peak watch, but no non-price 4B evidence |
| Doosan Enerbility | 2024-10-30 legal block | 0.02 vs later 2025 peak | too early; legal 4B did not stop later rerating |
| LS ELECTRIC | 2024-07-24 local peak | 1.00 local, 0.38 vs 2025 peak | price-only 4B too early if treated as exit |

4B rule adjustment:

```text
Do not treat price-only peak as full 4B.
Require at least one non-price factor:
- capital raise / dilution / CB
- final contract delay
- margin or backlog slowdown
- valuation blowoff plus revision slowdown
```

## 15. 4C Protection Audit

No hard 4C was confirmed in this R1 calibration set.

| case | 4C label | verdict |
|---|---|---|
| Samsung E&A | thesis_break_watch_only | price failed, but no hard contract cancellation / accounting break |
| Doosan Enerbility | false_break risk | legal block was 4B/watch, not hard 4C |
| LS ELECTRIC | no hard 4C | deep MAE was volatility/valuation digestion, not thesis break |

## 16. Baseline Score Simulation

The following is research proxy only.

| trigger_id | baseline_score | baseline_label | selected_by_baseline | score_return_alignment |
|---|---:|---|---:|---|
| r1_samsung_t2 | 72 | Stage2-Actionable watch | true | score_mid_return_low_watch_only |
| r1_doosan_t2 | 61 | Stage2, final contract missing | false | score_low_return_high_missed_structural |
| r1_ls_t2 | 66 | Stage2, report-only volatility risk | false | score_mid_return_high_promote_candidate |

Baseline problem:

```text
baseline_current_proxy is too conservative for nuclear/grid Stage2 evidence,
but Samsung E&A proves the gate should not be relaxed into unconditional Green.
```

## 17. Shadow Profile Optimization Loop

| profile_id | hypothesis | selected triggers | avg_MFE90 | avg_MAE90 | verdict |
|---|---|---|---:|---:|---|
| P0_baseline_current_proxy | conservative; selects only higher-confidence event | Samsung only | 15.81 | -14.62 | reference |
| P1_stage2_actionable_early_evidence_plus | promote credible early industrial evidence | Samsung, Doosan, LS | 22.56 | -27.21 | improves upside capture but MAE worsens |
| P2_stage3_yellow_entry_relaxed | use Yellow rather than Green for early R1 setup | Doosan, LS | 25.94 | -33.50 | useful but volatile |
| P3_green_confirmation_timing_relaxed | make Green easier | Samsung, Doosan, LS | 22.56 | -27.21 | rejected; would false-Green Samsung and high-MAE LS |
| P4_four_b_peak_timing_tuned | avoid price-only 4B, require non-price 4B | none as hard 4B | n/a | n/a | accepted as guardrail |
| P5_four_c_thesis_break_earlier | hard 4C earlier | none | n/a | n/a | no sample; no delta |

Best profile:

```text
best_shadow_profile = stage2_actionable_early_evidence_plus_with_volatility_guardrail
```

## 18. Before / After Backtest Comparison

| case_id | best_actual_trigger | baseline_selected | after_selected | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | return_improvement_90D | risk_change_90D | reason |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| r1_l1_samsung_ea_fadhili | T2 | T2 | T2-watch | 15.81 | 15.81 | -14.62 | -14.62 | 0.00 | 0.00 | keep as watch; not structural Green |
| r1_l1_doosan_czech_nuclear | T1/T2 | none/late | T2 | 0.00 | 17.65 | 0.00 | -28.71 | +17.65 | -28.71 | early Stage2 captures missed structural setup |
| r1_l1_ls_electric_us_grid | T1/T2 | none/late | T2-Yellow | 0.00 | 34.23 | 0.00 | -38.29 | +34.23 | -38.29 | report was directionally right but needs volatility guardrail |

The after profile improves upside capture but also introduces deep MAE. Therefore the proposed adjustment is exploratory, not aggressive.

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE90 | avg_MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_mid_return_low_watch_only | 2 | 72 | 72 | 15.81 | -14.62 | keep watch-only for EPC when no margin bridge |
| score_low_return_high_missed_structural | 2 | 61 | 70 | 17.65 | -28.71 | promote to Stage2-Actionable with sizing guardrail |
| score_mid_return_high_promote_candidate | 2 | 66 | 73 | 34.23 | -38.29 | promote only to Yellow; MAE guardrail mandatory |

## 20. Weight Sensitivity Table

| axis | baseline | tested | delta | affected | MFE90 before | MFE90 after | MAE90 before | MAE90 after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---|
| early_contract_or_preferred_bidder_evidence | 0 | 1 | +1 | r1_doosan_t1/r1_doosan_t2 | 0.00 | 17.65 | 0.00 | -28.71 | cautious positive |
| grid_power_us_growth_report_evidence | 0 | 1 | +1 | r1_ls_t1/r1_ls_t2 | 0.00 | 34.23 | 0.00 | -38.29 | promote but Yellow only |
| mega_epc_contract_without_margin_bridge | 0 | 0 | 0 | r1_samsung_t1/r1_samsung_t2 | 15.81 | 15.81 | -14.62 | -14.62 | no Green relaxation |
| price_only_4b_peak_watch | 1 | 0 | -1 | r1_ls_t5/r1_doosan_t5 | n/a | n/a | n/a | n/a | require non-price 4B confirmation |

## 21. Optimization Decision Log

| decision_id | hypothesis | accepted_or_rejected | delta | reason | why_not_larger_delta |
|---|---|---|---:|---|---|
| r1_l1_decision_001 | preferred bidder / contract evidence should enter Stage2-Actionable earlier | accepted | +1 | Doosan 1Y MFE was very large; Green-only would miss it. | 90D MAE was -28.71, so +2/+3 is too aggressive. |
| r1_l1_decision_002 | US grid/data-center report can be Stage3-Yellow earlier | accepted | +1 | LS Electric report trigger produced +34.23% MFE90 and +48.41% MFE180. | 90D MAE was -38.29, so only Yellow/small-size tier. |
| r1_l1_decision_003 | large EPC contract alone can become Green | rejected | 0 | Samsung E&A produced shallow early MFE and then deep drawdown. | Needs margin/backlog/cash conversion evidence. |
| r1_l1_decision_004 | price-only peak should trigger full 4B | rejected | -1 | Doosan and LS had later upside after price-only/local 4B watches. | Require non-price evidence such as dilution, revision slowdown, contract delay. |

## 22. Overfitting / Robustness Check

```text
usable_case_count = 3
usable_trigger_count = 7
max_abs_delta_allowed = 2_or_3 by sample rule
actual_delta_used = +1 / -1 only
reason = directions are mixed and MAE is high
counterexample = Samsung E&A contract trigger
counterexample_search_status = partial_but_present
```

No production scoring change is justified from this single R1 file. The result supports **shadow-only exploratory deltas**.

## 23. Cross-case Aggregate Metrics

### 23.1 Trigger type aggregate

| trigger_type | usable_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | avg_MFE180 | avg_MAE180 | below_entry_90D_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Stage2 | 3 | 22.56 | 17.65 | -27.21 | -28.71 | 36.54 | -34.19 | 1.00 | high upside, high volatility |
| Stage2-Actionable | 3 | 22.56 | 17.65 | -27.21 | -28.71 | 36.54 | -34.19 | 1.00 | viable as Yellow/watch, not full Green |
| 4B-watch | 2 | mixed | mixed | mixed | mixed | mixed | mixed | n/a | price-only 4B should not be full 4B |

### 23.2 Profile aggregate

| profile_id | case_count | selected_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | avg_MFE180 | avg_MAE180 | hit_rate_MFE90_gt_20pct | bad_entry_rate_MAE90_lt_minus_15pct | false_positive_rate | missed_structural_count | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| baseline_current_proxy | 3 | 1 | 15.81 | 15.81 | -14.62 | -14.62 | 15.81 | -35.57 | 0.00 | 0.00 | 0.00 | 2 | too conservative |
| stage2_actionable_early_evidence_plus | 3 | 3 | 22.56 | 17.65 | -27.21 | -28.71 | 36.54 | -34.19 | 0.33 | 0.67 | 0.33 | 0 | better recall but high MAE |
| stage2_actionable_with_volatility_guardrail | 3 | 2 | 25.94 | 25.94 | -33.50 | -33.50 | 46.71 | -33.50 | 0.50 | 1.00 | 0.00 | 0 | best as small-size Yellow tier |

## 24. Score-Price Alignment Verdict

```text
main_verdict =
R1 industrials should add an early Stage2-Actionable / Stage3-Yellow path for
preferred-bidder, grid-growth, and credible contract triggers,
but this tier must be explicitly volatility-aware.

Do not relax Stage3-Green broadly.
Do not treat price-only 4B as full 4B.
Do not upgrade EPC mega-contract to Green without margin/cash/backlog bridge.
```

## 25. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,early_contract_or_preferred_bidder_evidence,0,1,+1,"Doosan Czech preferred-bidder trigger produced large forward MFE but high MAE","MFE90 17.65; MFE180 45.41; MFE1Y 239.76; MAE90 -28.71","r1_doosan_t1|r1_doosan_t2",2,"shadow-only; Stage2-Actionable/Yellow, not Green"
shadow_weight,grid_power_us_growth_report_evidence,0,1,+1,"LS Electric US revenue/data-center thesis was directionally right but volatile","MFE90 34.23; MFE180 48.41; MAE90 -38.29","r1_ls_t1|r1_ls_t2",2,"shadow-only; require volatility guardrail"
shadow_weight,mega_epc_contract_without_margin_bridge,0,0,0,"Samsung E&A contract was large but not durable rerating by 180D","MFE180 15.81; MAE180 -35.57","r1_samsung_t1|r1_samsung_t2",2,"do not Green without margin/cash conversion"
shadow_weight,price_only_4b_peak_watch,1,0,-1,"Price-only peaks were not reliable full 4B signals in this sample","Doosan and LS both had later upside after local price peaks","r1_doosan_t5|r1_ls_t5",2,"require non-price 4B factor"
```

## 26. Machine-Readable Rows

### 26.1 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"r1_l1_samsung_ea_fadhili","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"1","sector":"산업재·수주·인프라","case_type":"evidence_good_but_price_failed","primary_archetype":"OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE","best_trigger":"r1_samsung_t2","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_low_watch_only","price_source":"Songdaiki/stock-web","notes":"Large EPC contract but no durable 180D rerating; keep watch-only without margin bridge."}
{"row_type":"case","case_id":"r1_l1_doosan_czech_nuclear","symbol":"034020","company_name":"두산에너빌리티","round":"R1","loop":"1","sector":"산업재·수주·인프라","case_type":"missed_structural","primary_archetype":"NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B","best_trigger":"r1_doosan_t2","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_low_return_high_missed_structural","price_source":"Songdaiki/stock-web","notes":"Preferred bidder trigger had high MAE but very large 1Y MFE; early Yellow/Stage2-Actionable needed."}
{"row_type":"case","case_id":"r1_l1_ls_electric_us_grid","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"1","sector":"산업재·수주·인프라","case_type":"Stage2_promote_candidate","primary_archetype":"GRID_EQUIPMENT_US_GROWTH_STAGE2_YELLOW","best_trigger":"r1_ls_t2","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_high_promote_candidate","price_source":"Songdaiki/stock-web","notes":"US grid/data-center report was correct directionally but MAE was too deep for Green."}
```

### 26.2 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"r1_samsung_t2","case_id":"r1_l1_samsung_ea_fadhili","symbol":"028050","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":25300,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":6.72,"MFE_90D_pct":15.81,"MFE_180D_pct":15.81,"MFE_1Y_pct":15.81,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-3.75,"MAE_90D_pct":-14.62,"MAE_180D_pct":-35.57,"MAE_1Y_pct":-35.57,"peak_date":"2024-08-01","peak_price":29300,"drawdown_after_peak_pct":-44.37,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":1.0,"trigger_outcome_label":"evidence_good_but_price_failed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"r1_doosan_t2","case_id":"r1_l1_doosan_czech_nuclear","symbol":"034020","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":21250,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.65,"MFE_90D_pct":17.65,"MFE_180D_pct":45.41,"MFE_1Y_pct":239.76,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-28.71,"MAE_90D_pct":-28.71,"MAE_180D_pct":-28.71,"MAE_1Y_pct":-28.71,"peak_date":"2025-06-30","peak_price":72200,"drawdown_after_peak_pct":-39.40,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":"not_applicable","trigger_outcome_label":"missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"r1_doosan_t5","case_id":"r1_l1_doosan_czech_nuclear","symbol":"034020","trigger_type":"4B-watch","trigger_date":"2024-10-30","entry_date":"2024-10-30","entry_price":21400,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":6.54,"MFE_90D_pct":44.39,"MFE_180D_pct":45.33,"MAE_30D_pct":-20.98,"MAE_90D_pct":-20.98,"MAE_180D_pct":-20.98,"peak_date":"2025-02-19","peak_price":30900,"drawdown_after_peak_pct":-35.40,"four_b_peak_proximity":0.02,"trigger_outcome_label":"4B_too_early_or_noise","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"r1_ls_t2","case_id":"r1_l1_ls_electric_us_grid","symbol":"010120","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":204500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":34.23,"MFE_90D_pct":34.23,"MFE_180D_pct":48.41,"MFE_1Y_pct":58.68,"MFE_2Y_pct":"unavailable_insufficient_forward_window","MAE_30D_pct":-29.10,"MAE_90D_pct":-38.29,"MAE_180D_pct":-38.29,"MAE_1Y_pct":-38.29,"peak_date":"2025-06-24","peak_price":324500,"drawdown_after_peak_pct":-54.03,"green_lateness_ratio":"not_applicable","four_b_peak_proximity":"price_only_local_peak","trigger_outcome_label":"volatile_promote_candidate","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
```

### 26.3 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r1_l1_samsung_ea_fadhili","trigger_id":"r1_samsung_t2","symbol":"028050","trigger_type":"Stage2-Actionable","weighted_score":72,"stage_label":"Stage2-Actionable watch","selected_by_profile":true,"MFE_90D_pct":15.81,"MAE_90D_pct":-14.62,"score_return_alignment_label":"score_mid_return_low_watch_only"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r1_l1_doosan_czech_nuclear","trigger_id":"r1_doosan_t2","symbol":"034020","trigger_type":"Stage2-Actionable","weighted_score":61,"stage_label":"Stage2","selected_by_profile":false,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"score_return_alignment_label":"score_low_return_high_missed_structural"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus","case_id":"r1_l1_doosan_czech_nuclear","trigger_id":"r1_doosan_t2","symbol":"034020","trigger_type":"Stage2-Actionable","weighted_score":70,"stage_label":"Stage2-Actionable","selected_by_profile":true,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"score_return_alignment_label":"score_low_return_high_missed_structural"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"r1_l1_ls_electric_us_grid","trigger_id":"r1_ls_t2","symbol":"010120","trigger_type":"Stage2-Actionable","weighted_score":66,"stage_label":"Stage2","selected_by_profile":false,"MFE_90D_pct":34.23,"MAE_90D_pct":-38.29,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus","case_id":"r1_l1_ls_electric_us_grid","trigger_id":"r1_ls_t2","symbol":"010120","trigger_type":"Stage2-Actionable","weighted_score":73,"stage_label":"Stage3-Yellow","selected_by_profile":true,"MFE_90D_pct":34.23,"MAE_90D_pct":-38.29,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
```

### 26.4 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,verdict
profile_comparison,baseline_current_proxy,3,15.81,-14.62,0.00,0.00,0.00,2,0,"reference; too conservative"
profile_comparison,stage2_actionable_early_evidence_plus,3,22.56,-27.21,0.33,0.67,0.33,0,0,"improved recall/upside but excessive MAE"
profile_comparison,stage2_actionable_with_volatility_guardrail,3,25.94,-33.50,0.50,1.00,0.00,0,0,"best shadow profile; Yellow/small-size only"
```

### 26.5 Optimization decision rows JSONL

```jsonl
{"row_type":"optimization_decision","decision_id":"r1_l1_decision_001","hypothesis":"preferred bidder and credible grid-growth evidence should be promoted earlier","tested_trigger_ids":["r1_doosan_t2","r1_ls_t2"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_volatility_guardrail","backtest_result_summary":"Doosan MFE1Y 239.76, LS MFE180 48.41, but MAE90 was -28.71 and -38.29.","accepted_or_rejected":"accepted","delta_magnitude":"+1","why_not_larger_delta":"MAE risk and sample size","next_validation_needed":"Find additional R1 counterexamples with report-only or preferred-bidder failure."}
{"row_type":"optimization_decision","decision_id":"r1_l1_decision_002","hypothesis":"large EPC contract can be Green without margin bridge","tested_trigger_ids":["r1_samsung_t2"],"baseline_profile":"baseline_current_proxy","selected_profile":"none","backtest_result_summary":"Samsung E&A MFE180 15.81 and MAE180 -35.57.","accepted_or_rejected":"rejected","delta_magnitude":"0","why_not_larger_delta":"failed 180D durability","next_validation_needed":"Test EPC cases with explicit margin/cash conversion."}
```

### 26.6 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"r1_l1_doosan_czech_nuclear","symbol":"034020","reason":"2025-05 court block was reviewed as possible 4C, but price path and evidence show legal 4B/watch rather than hard thesis break within this R1 file.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

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

## 28. Next Round State

```text
current_round = R1 Loop 1
next_round = R2 Loop 1
next_sector = AI·반도체·전자부품
production_scoring_changed = false
shadow_weight_only = true
carry_forward_questions =
- Does early Stage2 evidence work better in AI/HBM where revision is faster?
- Does Stage3-Green become too late in memory/HBM?
- Are 4B signals more reliable when valuation/revision slowdown is explicit rather than price-only?
```

## 29. Source Notes

- `Songdaiki/stock-web` OHLC rows are raw/unadjusted `FinanceData/marcap` transformed into assistant-readable symbol-year shards.
- 180D windows for selected triggers were calibration usable.
- 2Y windows were not used for calibration because 504 trading days were not fully available by manifest max_date.
- This file is not an investment recommendation.
- This file is not a production scoring patch.
