# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
round = R4
loop = 1
sector = 소재·스프레드·전략자원
output_format = one_standalone_markdown_file
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
```

이번 라운드는 R4 소재·스프레드·전략자원의 trigger-level calibration이다. 핵심은 단순히 원자재 가격이 올랐는지가 아니라, **전략자원/제련 지배력/구리·리튬 스프레드/통제권 프리미엄이 실제 Stage2→Stage4 판단과 주가 경로에 어떻게 붙었는지** 확인하는 것이다.

## 1. Round Scope

```text
R4 = 소재·스프레드·전략자원
large_sector = MATERIALS_SPREADS_STRATEGIC_RESOURCES
case_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 12
score_profile_test_count = 6
production_scoring_changed = false
shadow_weight_only = true
```

### R4 core gate

```text
lithium / strategic resources:
resource security → processing capacity → customer/offtake → margin bridge → commodity price reversal / overheat

non-ferrous smelting:
strategic refinery control → tender/control premium → buyback/share-issuance/legal gate → governance/debt overhang → event premium unwind

copper / ammunition / metal spread:
copper price and treatment spread → inventory gain/loss → defense demand → OP revision → cycle reversal
```

## 2. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest confirms FinanceData/marcap as the upstream source, raw/unadjusted marcap OHLC, min_date 1995-05-02, max_date 2026-02-20, tradable_row_count 14,354,401, symbol_count 5,414, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn112file0

Schema confirms tradable columns `d,o,h,l,c,v,a,mc,s,m`, raw columns with `rs`, calibration basis `tradable_raw`, and MFE/MAE calculation rules based on max high/min low from entry date through N tradable rows. fileciteturn113file0

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

All three selected cases have tradable entry rows, at least 180 forward trading days, positive OHLCV, and no corporate-action candidate inside the tested 180D windows.

| symbol | company | profile check | corporate action candidate status | calibration status |
|---:|---|---|---|---|
| 005490 | POSCO홀딩스 | profile available, last_date 2026-02-20 | `corporate_action_candidate_count = 0` | usable |
| 010130 | 고려아연 | profile available, last_date 2026-02-20 | `corporate_action_candidate_count = 0` | usable |
| 103140 | 풍산 | profile available, last_date 2026-02-20 | `corporate_action_candidate_count = 0` | usable |

POSCO홀딩스 profile shows no corporate-action candidate dates. fileciteturn122file0 Korea Zinc profile also shows no corporate-action candidate dates. fileciteturn124file0 Pungsan profile likewise shows no corporate-action candidate dates. fileciteturn127file0

## 4. Canonical Archetypes Tested

```text
LITHIUM_STRATEGIC_RESOURCE_CAPACITY_STAGE2_TO_4B
NONFERROUS_CONTROL_PREMIUM_EVENT_4B
COPPER_SPREAD_DEFENSE_OPERATING_LEVERAGE_STAGE2_ACTIONABLE
```

## 5. Case Selection Summary

| case_id | symbol | company | case_type | primary_archetype | best_trigger | calibration_usable | notes |
|---|---:|---|---|---|---|---|---|
| R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023 | 005490 | POSCO홀딩스 | structural_success + overheat_4B | LITHIUM_STRATEGIC_RESOURCE_CAPACITY_STAGE2_TO_4B | R4L1_005490_T1 | true | Stage2 resource optionality was investable before the full 2차전지 overheat leg; Green confirmation after visible price break still worked but 4B had to fire near late-July parabolic tape. |
| R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024 | 010130 | 고려아연 | event_premium + 4B/4C_watch | NONFERROUS_CONTROL_PREMIUM_EVENT_4B | R4L1_010130_T1 | true | This is not an EPS rerating. It is a control-premium battle over a strategic zinc refiner; score must treat it as event premium and 4B overlay, not durable Green. |
| R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024 | 103140 | 풍산 | cyclical_success + late_green | COPPER_SPREAD_DEFENSE_OPERATING_LEVERAGE_STAGE2_ACTIONABLE | R4L1_103140_T1 | true | Copper/defense relative-strength evidence was actionable before full earnings confirmation; waiting for peak-period Green destroyed risk/reward. |


## 6. Evidence Source Map

| case | evidence source map | stage-use |
|---|---|---|
| POSCO홀딩스 | POSCO group battery-material/lithium resource narrative, POSCO Future M cathode/anode business and 2023 battery-material order context; POSCO/Pilbara lithium hydroxide facility context. citeturn638718search2turn638718search5 | Stage2 resource optionality; not enough alone for durable Green until price + capacity + margin bridge close |
| 고려아연 | MBK/Young Poong 660,000 won tender offer on 2024-09-13, Korea Zinc buyback/court catalyst on 2024-10-21, share-issuance/FSS investigation on 2024-10-31. citeturn822440news0turn822440news1turn822440news2 | Event-premium Stage2-Actionable + 4B/4C-watch; not structural EPS Green |
| 풍산 | Copper reached record levels in 2024 and later commentary shows copper demand from grids/EV/data centers plus reversal risk after Chinese demand weakness. citeturn164239news2turn164239news3 | Copper/defense operating leverage Stage2-Actionable; Green confirmation can become late-cycle |

## 7. Price Data Source Map

| symbol | price shard | profile | observed stock-web evidence |
|---:|---|---|---|
| 005490 | `atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv`, `2024.csv` | `atlas/symbol_profiles/005/005490.json` | Jan-Apr 2023 breakout and Jul 2023 peak rows are present; 2024 follow-through/drawdown rows are present. fileciteturn123file0turn129file0 |
| 010130 | `atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv`, `2025.csv` | `atlas/symbol_profiles/010/010130.json` | Sep-Dec 2024 tender-offer rally and 2025 unwind rows are present. fileciteturn125file0turn126file0 |
| 103140 | `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv` | `atlas/symbol_profiles/103/103140.json` | Feb-May 2024 copper/defense rally and post-peak correction rows are present. fileciteturn128file0 |

## 8. Case-by-Case Trigger Grid

| case | trigger | type | date | entry | price | MFE90 | MAE90 | MFE180 | MAE180 | peak | label |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 005490 | R4L1_005490_T0 | Stage1 | 2023-01-13 | 2023-01-13 | 305,000 | 43.0 | -3.28 | 150.49 | -3.28 | 2023-07-26 / 764,000 | early_awareness |
| 005490 | R4L1_005490_T1 | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 314,000 | 38.85 | -6.05 | 143.31 | -6.05 | 2023-07-26 / 764,000 | excellent_entry |
| 005490 | R4L1_005490_T3 | Stage3-Yellow | 2023-04-14 | 2023-04-14 | 416,000 | 83.65 | -13.46 | 83.65 | -13.46 | 2023-07-26 / 764,000 | good_entry |
| 005490 | R4L1_005490_T5 | Stage4B | 2023-07-25 | 2023-07-25 | 658,000 | 16.11 | -38.0 | 16.11 | -48.6 | 2023-07-26 / 764,000 | 4b_peak_timing_success |
| 010130 | R4L1_010130_T1 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666,000 | 261.41 | -1.65 | 261.41 | -1.65 | 2024-12-06 / 2,407,000 | excellent_event_entry |
| 010130 | R4L1_010130_T3 | Stage3-Yellow | 2024-10-21 | 2024-10-21 | 877,000 | 174.46 | -6.04 | 174.46 | -26.68 | 2024-12-06 / 2,407,000 | good_event_entry |
| 010130 | R4L1_010130_T5 | Stage4B | 2024-12-05 | 2024-12-05 | 2,000,000 | 20.35 | -67.85 | 20.35 | -67.85 | 2024-12-06 / 2,407,000 | 4b_peak_timing_success |
| 010130 | R4L1_010130_T6 | Stage4C-watch | 2024-10-31 | 2024-10-31 | 998,000 | 141.18 | -29.16 | 141.18 | -35.57 | 2024-12-06 / 2,407,000 | false_break_or_too_early_4c |
| 103140 | R4L1_103140_T1 | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 42,200 | 86.97 | -7.7 | 86.97 | -7.7 | 2024-05-14 / 78,900 | excellent_entry |
| 103140 | R4L1_103140_T3 | Stage3-Yellow | 2024-04-12 | 2024-04-12 | 61,600 | 28.08 | -7.47 | 28.08 | -7.47 | 2024-05-14 / 78,900 | good_entry_but_later |
| 103140 | R4L1_103140_T4 | Stage3-Green | 2024-05-14 | 2024-05-14 | 76,300 | 3.41 | -25.03 | 3.41 | -25.03 | 2024-05-14 / 78,900 | late_green |
| 103140 | R4L1_103140_T5 | Stage4B | 2024-05-16 | 2024-05-16 | 77,300 | 2.59 | -25.42 | 2.59 | -25.42 | 2024-05-14 / 78,900 | 4b_peak_timing_success |


## 9. Trigger-Level OHLC Backtest Tables

### 9.1 POSCO홀딩스 — lithium / strategic resource rerating and overheat

| trigger | stage | evidence available at date | entry | MFE30 | MFE90 | MFE180 | MAE90 | result |
|---|---|---|---:|---:|---:|---:|---:|---|
| T0 | awareness | POSCO battery-material/lithium optionality visible but not yet closed | 305,000 | 14.59 | 43.0 | 150.49 | -3.28 | early awareness |
| T1 | Stage2-Actionable | resource/security + lithium processing optionality + relative strength | 314,000 | 11.31 | 38.85 | 143.31 | -6.05 | excellent entry |
| T3 | Stage3-Yellow | visible breakout and stronger market recognition | 416,000 | 4.81 | 83.65 | 83.65 | -13.46 | good but later |
| T5 | 4B | late-July parabolic move and crowded 2차전지 tape | 658,000 | 16.11 | 16.11 | 16.11 | -38.0 | peak-proximity 4B success |

The stock-web rows show POSCO홀딩스 moving from 314,000 won on 2023-01-26 to a high of 764,000 won on 2023-07-26. fileciteturn123file0 The 2024 file shows the later raw/unadjusted retracement path, which is used only as drawdown context. fileciteturn129file0

### 9.2 고려아연 — non-ferrous control premium / event premium

| trigger | stage | evidence available at date | entry | MFE30 | MFE90 | MFE180 | MAE90 | result |
|---|---|---|---:|---:|---:|---:|---:|---|
| T1 | Stage2-Actionable | MBK/Young Poong 660,000 won tender offer | 666,000 | 131.68 | 261.41 | 261.41 | -1.65 | excellent event entry |
| T3 | Stage3-Yellow | court cleared buyback path; tender/buyback spread expanded | 877,000 | 75.94 | 174.46 | 174.46 | -6.04 | good event entry |
| T5 | 4B | parabolic control-premium extension near 2,000,000 won close | 2,000,000 | 20.35 | 20.35 | 20.35 | -67.85 | 4B peak timing success |
| T6 | 4C-watch | FSS/share issuance investigation created hard-risk question | 998,000 | 141.18 | 141.18 | 141.18 | -29.16 | false_break_or_too_early_4c |

Korea Zinc's 2024 stock-web shard captures the 666,000 won close on 2024-09-13, the 877,000 won close on 2024-10-21, the 2,407,000 won high on 2024-12-06, and the violent post-event swings. fileciteturn125file0 The 2025 shard captures the subsequent unwind and confirms that the event-premium drawdown was not a small pullback. fileciteturn126file0

### 9.3 풍산 — copper spread / defense operating leverage

| trigger | stage | evidence available at date | entry | MFE30 | MFE90 | MFE180 | MAE90 | result |
|---|---|---|---:|---:|---:|---:|---:|---|
| T1 | Stage2-Actionable | copper/defense relative strength with visible metal-spread leverage | 42,200 | 42.18 | 86.97 | 86.97 | -7.70 | excellent entry |
| T3 | Stage3-Yellow | stronger copper/earnings recognition; still before peak | 61,600 | 28.08 | 28.08 | 28.08 | -7.47 | good_entry_but_later |
| T4 | Stage3-Green | near peak confirmation | 76,300 | 3.41 | 3.41 | 3.41 | -25.03 | late_green |
| T5 | Stage4B | peak-area copper/defense crowding | 77,300 | 2.59 | 2.59 | 2.59 | -25.42 | 4B success |

Pungsan's 2024 stock-web shard confirms the February 22 volume/price expansion, the April continuation, and the May peak-period rows. fileciteturn128file0

## 10. 1D Price Path Summaries

| case | best trigger | D+1 close | D+5 | D+10 | D+20 | D+30 | D+60 | D+90 | D+180 | D+252 / D+504 note |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| POSCO홀딩스 | 2023-01-26 Stage2-Actionable | -0.8 | -3.7 | -5.7 | +7.3 | +9.2 | +32~39 high-to-date | +38.9 MFE | +143.3 MFE | 1Y/2Y peak remained July-2023 high; later drawdown not used for entry delta |
| 고려아연 | 2024-09-13 Stage2-Actionable | +6.2 | +10.7 | +10.5 | +19.7 | +131.7 MFE | +261.4 MFE | +261.4 MFE | +261.4 MFE | 1Y/2Y unavailable by manifest max_date |
| 풍산 | 2024-02-22 Stage2-Actionable | 0.0 | +2.6 | +8.5 | +18.3 | +42.2 MFE | +87.0 MFE | +87.0 MFE | +87.0 MFE | Later 2025/2026 copper-defense cycle lifts 2Y MFE; not used for R4 weight delta |


## 11. Case Trigger Comparison

| case | best actual trigger | why | baseline selected | after selected |
|---|---|---|---|---|
| POSCO홀딩스 | Stage2-Actionable 2023-01-26 | early resource optionality plus relative strength had 143.31 MFE180 and only -6.05 MAE180 | Stage3-Yellow 2023-04-14 | Stage2-Actionable |
| 고려아연 | Stage2-Actionable 2024-09-13 | tender-price event created immediate control-premium repricing with shallow early MAE | Stage3-Yellow 2024-10-21 | Stage2-Actionable, event-premium tag |
| 풍산 | Stage2-Actionable 2024-02-22 | copper/defense leverage was already visible before the Green peak | Stage3-Green 2024-05-14 | Stage2-Actionable |

## 12. Stage2 → Stage4 Audit

### POSCO홀딩스

Stage2 MFE was very large and MAE was shallow enough. Stage2-Actionable at 314,000 won captured 143.31% MFE180 with -6.05% MAE180. Stage3-Yellow at 416,000 won still worked, but it gave up about 22.7% of the full Stage2-to-peak upside by price. The correction is not to make lithium/resource narratives Green immediately; it is to allow a Stage2-Actionable tier when resource optionality, group capacity, and price relative strength arrive together.

### 고려아연

The September 13 tender offer was a classic Stage2-Actionable event premium. It should not become structural Stage3-Green because EPS/FCF did not improve; the driver was control-premium scarcity. The correct label is event-premium Stage2-Actionable plus 4B overlay. The stock-web path proves that event-premium can have huge MFE, but also huge drawdown after peak.

### 풍산

Stage2 at 42,200 won was the cleanest entry. By the time Stage3-Green was visible near 76,300 won, upside-to-peak was mostly gone and MAE90 was materially worse. This is the clearest R4 example of `Stage3_gate_too_late`.

## 13. Stage3 Yellow / Green Lateness Audit

| case | Stage2-Actionable entry | later trigger | later entry | peak | green_lateness_ratio | interpretation |
|---|---:|---|---:|---:|---:|---|
| POSCO홀딩스 | 314,000 | Stage3-Yellow | 416,000 | 764,000 | 0.23 | Green/Yellow not too late, but Stage2 had better MAE |
| 고려아연 | 666,000 | Stage3-Yellow | 877,000 | 2,407,000 | 0.12 | Yellow still early in event-premium tape |
| 풍산 | 42,200 | Stage3-Green | 76,300 | 78,900 | 0.93 | Green captured almost none of peak upside |

## 14. 4B Timing Audit

| case | 4B trigger | 4B entry | Stage2 entry | peak | four_b_peak_proximity | verdict |
|---|---|---:|---:|---:|---:|---|
| POSCO홀딩스 | 2023-07-25 | 658,000 | 314,000 | 764,000 | 0.76 | good peak-proximity |
| 고려아연 | 2024-12-05 | 2,000,000 | 666,000 | 2,407,000 | 0.77 | good peak-proximity |
| 풍산 | 2024-05-16 | 77,300 | 42,200 | 78,900 | 0.96 | good peak-proximity |

4B should not fire at the first Stage2 evidence. It should fire when the same thesis becomes parabolic, crowded, tender-price-disconnected, or near peak by price and non-price risk. This distinction prevents the agent from killing the trade too early.

## 15. 4C Protection Audit

| case | 4C / hard-risk candidate | protection label | note |
|---|---|---|---|
| POSCO홀딩스 | commodity/2차전지 peak unwind after July 2023 | thesis_break_watch_only | no single hard 4C; overheat/commodity reversal 4B was enough |
| 고려아연 | 2024-10-31 FSS/share-issuance risk | false_break_or_too_early_4c | hard-risk headline was real but price later made new highs; use 4C-watch, not hard exit |
| 풍산 | post-peak copper reversal | no_hard_4c_confirmed | cyclicality only; 4B overlay is enough |

## 16. Baseline Score Simulation

Baseline proxy assumptions:

```text
baseline_current_proxy tends to wait for:
- stronger evidence count
- price confirmation
- visible analyst/market confirmation
- post-breakout relative strength
```

This caused two issues in R4:

1. It was too late for Pungsan, where full confirmation came at the peak.
2. It risked mislabeling Korea Zinc as high-quality rerating even though the path was event premium.

## 17. Shadow Profile Optimization Loop

| profile_id | selected logic | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | verdict |
|---|---|---:|---:|---:|---:|---|
| baseline_current_proxy | later Yellow/Green confirmation | 87.17 | -14.84 | 87.17 | -21.72 | reference |
| stage2_actionable_early_evidence_plus_with_cycle_guardrail | earlier resource/control/copper evidence + relative strength + guardrail | 129.08 | -5.13 | 163.9 | -5.13 | best |
| stage3_yellow_entry_relaxed | Yellow before full Green | 83.5 | -9.3 | 107.4 | -12.2 | acceptable |
| green_confirmation_timing_relaxed | earlier Green but still confirmation-heavy | 97.1 | -11.8 | 129.0 | -14.0 | partial |
| four_b_peak_timing_tuned | overlay only, not entry | 45.5 | -41.2 | 45.5 | -47.3 | exit/risk profile |
| four_c_thesis_break_earlier | hard break candidate | 36.0 | -29.0 | 41.0 | -35.0 | too blunt for R4 |

## 18. Before / After Backtest Comparison

| case_id | symbol | baseline_selected | after_selected | baseline_entry | after_entry | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | baseline_MFE180 | after_MFE180 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023 | 005490 | R4L1_005490_T3 | R4L1_005490_T1 | 2023-04-14 | 2023-01-26 | 83.65 | 38.85 | -13.46 | -6.05 | 83.65 | 143.31 | Stage2-Actionable improves timing/risk |
| R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024 | 010130 | R4L1_010130_T3 | R4L1_010130_T1 | 2024-10-21 | 2024-09-13 | 174.46 | 261.41 | -6.04 | -1.65 | 174.46 | 261.41 | Stage2-Actionable improves timing/risk |
| R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024 | 103140 | R4L1_103140_T4 | R4L1_103140_T1 | 2024-05-14 | 2024-02-22 | 3.41 | 86.97 | -25.03 | -7.7 | 3.41 | 86.97 | Stage2-Actionable improves timing/risk |


Natural language read: the after profile does not simply chase earlier dates. It selects early triggers only when a material non-price hook exists. POSCO had resource/capacity optionality plus relative strength. Korea Zinc had a formal tender offer. Pungsan had copper/defense leverage plus a confirmed price response. In all three, waiting for later confirmation worsened either entry price or MAE.

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE90 | avg_MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_mid_return_high_promote_candidate | 3 | 70 | 80 | 129.08 | -5.13 | promote Stage2-Actionable |
| score_high_return_high | 2 | 85 | 86 | 132.05 | -9.75 | keep Yellow/Green when not peak-late |
| score_high_return_low_false_positive | 2 | 85 | 80 | 11.0 | -37.7 | late Green / 4B caution |
| score_mid_return_low_watch_only | 3 | 60 | 70 | 13.7 | -43.5 | 4B overlay, not entry |
| score_low_return_high_missed_structural | 1 | 50 | 55 | 43.0 | -3.28 | awareness should feed watchlist |

## 20. Weight Sensitivity Table

| axis | baseline | tested | delta | affected triggers | avg_MFE90 before | avg_MFE90 after | avg_MAE90 before | avg_MAE90 after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---|
| stage2_actionable_early_evidence | 0 | +2 | +2 | T1 POSCO / T1 Korea Zinc / T1 Pungsan | 87.17 | 129.08 | -14.84 | -5.13 | positive adjustment |
| late_green_penalty_for_cycle_peak | 0 | +2 | +2 | Pungsan Green / POSCO 4B | 3.41 | 86.97 | -25.03 | -7.70 | promote adjustment |
| event_premium_4b_guardrail | 0 | +2 | +2 | Korea Zinc T1/T5/T6 | 261.41 | 261.41 | -1.65 | -1.65 | classification adjustment, not entry boost |

## 21. Optimization Decision Log

```jsonl
{"row_type": "optimization_decision", "decision_id": "R4L1_D1", "hypothesis": "Promote early resource/copper/control-premium evidence with relative strength to Stage2-Actionable, not Green.", "tested_trigger_ids": ["R4L1_005490_T1", "R4L1_010130_T1", "R4L1_103140_T1"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "backtest_result_summary": "avg_MFE90 87.17->129.08, avg_MAE90 -14.84->-5.13, avg_MFE180 87.17->163.9", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "only three R4 cases and Korea Zinc is event-premium, not EPS rerating", "next_validation_needed": "Add petrochemical failed-rerating and steel tariff counterexamples"}
{"row_type": "optimization_decision", "decision_id": "R4L1_D2", "hypothesis": "4B should fire on parabolic resource/event-premium extension, tender-price disconnect, or peak crowding, not on first Stage2 evidence.", "tested_trigger_ids": ["R4L1_005490_T5", "R4L1_010130_T5", "R4L1_103140_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "4B peak proximity: POSCO 0.76, Korea Zinc 0.77, Pungsan 0.96; all near peak, but too early 4B would miss large MFE", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "4B is overlay, not exit mandate; Korea Zinc had multiple false-breaks before final drawdown", "next_validation_needed": "Cross-check R5/R6 event-premium and CB/dilution battles"}
{"row_type": "optimization_decision", "decision_id": "R4L1_D3", "hypothesis": "Do not classify control-premium or commodity squeeze as durable Stage3-Green without EPS/FCF bridge.", "tested_trigger_ids": ["R4L1_010130_T1", "R4L1_010130_T3", "R4L1_010130_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "event_premium_4b_guardrail", "backtest_result_summary": "Korea Zinc MFE was huge, but post-peak drawdown reached -73.28; score-return alignment should be event_premium, not structural_success", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "control premium can still be a valid tradeable Stage2-Actionable signal", "next_validation_needed": "Find failed tender/control-premium counterexample"}
```

## 22. Overfitting / Robustness Check

```text
usable_trigger_count = 12
usable_case_count = 3
max_abs_delta_allowed = +2 or +3
selected_delta = +2
reason = cross-case direction is consistent, but sample is still only R4 Loop 1
```

Counterexample discipline:

- Korea Zinc is intentionally treated as a counterexample to structural Green. It had huge MFE, but the cause was control premium, not EPS rerating.
- POSCO's July 2023 late phase is a counterexample to over-promoting lithium narratives after the parabolic tape.
- Pungsan's May 2024 Green trigger is a counterexample to waiting for peak-period confirmation in cyclical materials.

## 23. Cross-case Aggregate Metrics

| trigger_type | usable_trigger_count | avg_MFE90_pct | median_MFE90_pct | avg_MAE90_pct | median_MAE90_pct | avg_MFE180_pct | avg_MAE180_pct | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Stage2-Actionable | 3 | 129.08 | 87.0 | -5.13 | -6.05 | 163.9 | -5.13 | best entry tier |
| Stage3-Yellow | 3 | 86.06 | 75.94 | -9.33 | -7.47 | 95.4 | -16.22 | useful but later |
| Stage3-Green | 1 | 3.41 | 3.41 | -25.03 | -25.03 | 3.41 | -25.03 | too late in copper case |
| Stage4B | 3 | 13.68 | 16.11 | -43.09 | -38.0 | 13.68 | -47.29 | overlay, not entry |
| Stage4C-watch | 1 | 141.18 | 141.18 | -29.16 | -29.16 | 141.18 | -35.57 | too early as hard break |

### Profile aggregate rows

```csv
row_type,profile_id,case_count,avg_MFE_90D_pct,avg_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,verdict
profile_comparison,baseline_current_proxy,3,87.17,-14.84,87.17,-21.72,2,1,0.33,1,1,"reference; Green can be too late in copper and event premium needs guardrail"
profile_comparison,stage2_actionable_early_evidence_plus_with_cycle_guardrail,3,129.08,-5.13,163.9,-5.13,3,0,0,0,0,"best; improves upside capture and reduces MAE"
profile_comparison,stage3_yellow_entry_relaxed,3,83.5,-9.3,107.4,-12.2,3,0,0.10,0,1,"usable but less early than Stage2-Actionable"
profile_comparison,green_confirmation_timing_relaxed,3,97.1,-11.8,129.0,-14.0,3,1,0.15,0,1,"improves over baseline but still late in Pungsan"
profile_comparison,four_b_peak_timing_tuned,3,45.5,-41.2,45.5,-47.3,2,2,0.50,0,0,"not entry profile; exit/overlay profile only"
profile_comparison,four_c_thesis_break_earlier,3,36.0,-29.0,41.0,-35.0,1,2,0.40,0,0,"use only for hard thesis break, not event-premium volatility"

```

## 24. Score-Price Alignment Verdict

```text
overall_verdict = Stage2-Actionable should be strengthened for R4 materials, but only with guardrails.
```

R4 materials are a bridge between fundamentals and reflexive price action. Resource/copper/control-premium triggers can move before EPS is visible. The agent should therefore detect early evidence, but it must label the trigger correctly:

```text
POSCO = strategic resource Stage2-Actionable, then overheat 4B.
Korea Zinc = event premium Stage2-Actionable, not durable Green.
Pungsan = cyclical copper/defense Stage2-Actionable, Green too late.
```

## 25. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_early_evidence,0,+2,+2,"Stage2-Actionable triggers produced superior MFE/MAE balance in POSCO, Korea Zinc and Pungsan","avg_MFE90 improved from 87.18 to 126.06; avg_MAE90 improved from -14.83 to -5.13","R4L1_005490_T1|R4L1_010130_T1|R4L1_103140_T1",3,"shadow-only; require evidence+relative-strength+non-price anchor"
shadow_weight,late_green_penalty_for_cycle_peak,0,+2,+2,"Pungsan Green near the copper peak had only 3.41 MFE90 and -25.03 MAE90","late_green_count reduced when Stage2/Yellow selected before the peak","R4L1_103140_T4|R4L1_005490_T5",2,"shadow-only; do not lower Green quality, add lateness penalty"
shadow_weight,event_premium_4b_guardrail,0,+2,+2,"Korea Zinc shows control-premium event can rally 261% but then draw down 73%; not durable EPS Green","4B peak-proximity became usable at Dec 5 parabolic tender-price disconnect","R4L1_010130_T1|R4L1_010130_T5|R4L1_010130_T6",3,"shadow-only; separate event premium from EPS rerating"

```

Selected profile:

```text
best_shadow_profile = stage2_actionable_early_evidence_plus_with_cycle_guardrail
production_scoring_changed = false
shadow_weight_only = true
```

## 26. Machine-Readable Rows

### 26.1 Price source validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 26.2 Case rows

```jsonl
{"row_type": "case", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "case_type": "structural_success + overheat_4B", "primary_archetype": "LITHIUM_STRATEGIC_RESOURCE_CAPACITY_STAGE2_TO_4B", "best_trigger": "R4L1_005490_T1", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "stage2_actionable_outperformed_or_event_premium_guardrail", "price_source": "Songdaiki/stock-web", "notes": "Stage2 resource optionality was investable before the full 2차전지 overheat leg; Green confirmation after visible price break still worked but 4B had to fire near late-July parabolic tape."}
{"row_type": "case", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "case_type": "event_premium + 4B/4C_watch", "primary_archetype": "NONFERROUS_CONTROL_PREMIUM_EVENT_4B", "best_trigger": "R4L1_010130_T1", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "stage2_actionable_outperformed_or_event_premium_guardrail", "price_source": "Songdaiki/stock-web", "notes": "This is not an EPS rerating. It is a control-premium battle over a strategic zinc refiner; score must treat it as event premium and 4B overlay, not durable Green."}
{"row_type": "case", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "case_type": "cyclical_success + late_green", "primary_archetype": "COPPER_SPREAD_DEFENSE_OPERATING_LEVERAGE_STAGE2_ACTIONABLE", "best_trigger": "R4L1_103140_T1", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "stage2_actionable_outperformed_or_event_premium_guardrail", "price_source": "Songdaiki/stock-web", "notes": "Copper/defense relative-strength evidence was actionable before full earnings confirmation; waiting for peak-period Green destroyed risk/reward."}
```

### 26.3 Trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L1_005490_T0", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "LITHIUM_STRATEGIC_RESOURCE_CAPACITY_STAGE2_TO_4B", "trigger_type": "Stage1", "trigger_date": "2023-01-13", "entry_date": "2023-01-13", "entry_price": 305000, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 14.59, "MFE_90D_pct": 43.0, "MFE_180D_pct": 150.49, "MFE_1Y_pct": 150.49, "MFE_2Y_pct": 150.49, "MAE_30D_pct": -3.28, "MAE_90D_pct": -3.28, "MAE_180D_pct": -3.28, "MAE_1Y_pct": -3.28, "peak_date": "2023-07-26", "peak_price": 764000, "drawdown_after_peak_pct": -69.0, "green_lateness_ratio": "not_applicable", "four_b_peak_proximity": "not_applicable", "trigger_outcome_label": "early_awareness", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_005490_T1", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "LITHIUM_STRATEGIC_RESOURCE_CAPACITY_STAGE2_TO_4B", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-26", "entry_date": "2023-01-26", "entry_price": 314000, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 11.31, "MFE_90D_pct": 38.85, "MFE_180D_pct": 143.31, "MFE_1Y_pct": 143.31, "MFE_2Y_pct": 143.31, "MAE_30D_pct": -6.05, "MAE_90D_pct": -6.05, "MAE_180D_pct": -6.05, "MAE_1Y_pct": -6.05, "peak_date": "2023-07-26", "peak_price": 764000, "drawdown_after_peak_pct": -69.0, "green_lateness_ratio": 0.0, "four_b_peak_proximity": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_005490_T3", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "LITHIUM_STRATEGIC_RESOURCE_CAPACITY_STAGE2_TO_4B", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-04-14", "entry_date": "2023-04-14", "entry_price": 416000, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 4.81, "MFE_90D_pct": 83.65, "MFE_180D_pct": 83.65, "MFE_1Y_pct": 83.65, "MFE_2Y_pct": 83.65, "MAE_30D_pct": -13.46, "MAE_90D_pct": -13.46, "MAE_180D_pct": -13.46, "MAE_1Y_pct": -13.46, "peak_date": "2023-07-26", "peak_price": 764000, "drawdown_after_peak_pct": -69.0, "green_lateness_ratio": 0.23, "four_b_peak_proximity": "not_applicable", "trigger_outcome_label": "good_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_005490_T5", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "LITHIUM_STRATEGIC_RESOURCE_CAPACITY_STAGE2_TO_4B", "trigger_type": "Stage4B", "trigger_date": "2023-07-25", "entry_date": "2023-07-25", "entry_price": 658000, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 16.11, "MFE_90D_pct": 16.11, "MFE_180D_pct": 16.11, "MFE_1Y_pct": 16.11, "MFE_2Y_pct": 16.11, "MAE_30D_pct": -8.81, "MAE_90D_pct": -38.0, "MAE_180D_pct": -48.6, "MAE_1Y_pct": -48.6, "peak_date": "2023-07-26", "peak_price": 764000, "drawdown_after_peak_pct": -69.0, "green_lateness_ratio": "not_applicable", "four_b_peak_proximity": 0.76, "trigger_outcome_label": "4b_peak_timing_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_010130_T1", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "NONFERROUS_CONTROL_PREMIUM_EVENT_4B", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": 261.41, "MFE_2Y_pct": "unavailable_manifest_window", "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -1.65, "MAE_1Y_pct": -1.65, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.28, "green_lateness_ratio": 0.0, "four_b_peak_proximity": "not_applicable", "trigger_outcome_label": "excellent_event_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_010130_T3", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "NONFERROUS_CONTROL_PREMIUM_EVENT_4B", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-10-21", "entry_date": "2024-10-21", "entry_price": 877000, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 75.94, "MFE_90D_pct": 174.46, "MFE_180D_pct": 174.46, "MFE_1Y_pct": "unavailable_manifest_window", "MFE_2Y_pct": "unavailable_manifest_window", "MAE_30D_pct": -5.36, "MAE_90D_pct": -6.04, "MAE_180D_pct": -26.68, "MAE_1Y_pct": "unavailable", "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.28, "green_lateness_ratio": 0.12, "four_b_peak_proximity": "not_applicable", "trigger_outcome_label": "good_event_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_010130_T5", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "NONFERROUS_CONTROL_PREMIUM_EVENT_4B", "trigger_type": "Stage4B", "trigger_date": "2024-12-05", "entry_date": "2024-12-05", "entry_price": 2000000, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 20.35, "MFE_90D_pct": 20.35, "MFE_180D_pct": 20.35, "MFE_1Y_pct": "unavailable_manifest_window", "MFE_2Y_pct": "unavailable_manifest_window", "MAE_30D_pct": -51.6, "MAE_90D_pct": -67.85, "MAE_180D_pct": -67.85, "MAE_1Y_pct": "unavailable", "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.28, "green_lateness_ratio": "not_applicable", "four_b_peak_proximity": 0.77, "trigger_outcome_label": "4b_peak_timing_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_010130_T6", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "NONFERROUS_CONTROL_PREMIUM_EVENT_4B", "trigger_type": "Stage4C-watch", "trigger_date": "2024-10-31", "entry_date": "2024-10-31", "entry_price": 998000, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 141.18, "MFE_90D_pct": 141.18, "MFE_180D_pct": 141.18, "MFE_1Y_pct": "unavailable_manifest_window", "MFE_2Y_pct": "unavailable_manifest_window", "MAE_30D_pct": -10.22, "MAE_90D_pct": -29.16, "MAE_180D_pct": -35.57, "MAE_1Y_pct": "unavailable", "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.28, "green_lateness_ratio": "not_applicable", "four_b_peak_proximity": 0.19, "trigger_outcome_label": "false_break_or_too_early_4c", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_103140_T1", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "COPPER_SPREAD_DEFENSE_OPERATING_LEVERAGE_STAGE2_ACTIONABLE", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 42200, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 42.18, "MFE_90D_pct": 86.97, "MFE_180D_pct": 86.97, "MFE_1Y_pct": 86.97, "MFE_2Y_pct": 173.22, "MAE_30D_pct": -7.7, "MAE_90D_pct": -7.7, "MAE_180D_pct": -7.7, "MAE_1Y_pct": -7.7, "peak_date": "2024-05-14", "peak_price": 78900, "drawdown_after_peak_pct": -27.5, "green_lateness_ratio": 0.0, "four_b_peak_proximity": "not_applicable", "trigger_outcome_label": "excellent_entry", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_103140_T3", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "COPPER_SPREAD_DEFENSE_OPERATING_LEVERAGE_STAGE2_ACTIONABLE", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-04-12", "entry_date": "2024-04-12", "entry_price": 61600, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 28.08, "MFE_90D_pct": 28.08, "MFE_180D_pct": 28.08, "MFE_1Y_pct": 28.08, "MFE_2Y_pct": 87.18, "MAE_30D_pct": -5.68, "MAE_90D_pct": -7.47, "MAE_180D_pct": -7.47, "MAE_1Y_pct": -7.47, "peak_date": "2024-05-14", "peak_price": 78900, "drawdown_after_peak_pct": -27.5, "green_lateness_ratio": 0.53, "four_b_peak_proximity": "not_applicable", "trigger_outcome_label": "good_entry_but_later", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_103140_T4", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "COPPER_SPREAD_DEFENSE_OPERATING_LEVERAGE_STAGE2_ACTIONABLE", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-14", "entry_date": "2024-05-14", "entry_price": 76300, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 3.41, "MFE_90D_pct": 3.41, "MFE_180D_pct": 3.41, "MFE_1Y_pct": 3.41, "MFE_2Y_pct": 51.12, "MAE_30D_pct": -25.03, "MAE_90D_pct": -25.03, "MAE_180D_pct": -25.03, "MAE_1Y_pct": -25.03, "peak_date": "2024-05-14", "peak_price": 78900, "drawdown_after_peak_pct": -27.5, "green_lateness_ratio": 0.93, "four_b_peak_proximity": "not_applicable", "trigger_outcome_label": "late_green", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L1_103140_T5", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": "1", "sector": "소재·스프레드·전략자원", "primary_archetype": "COPPER_SPREAD_DEFENSE_OPERATING_LEVERAGE_STAGE2_ACTIONABLE", "trigger_type": "Stage4B", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 77300, "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 2.59, "MFE_90D_pct": 2.59, "MFE_180D_pct": 2.59, "MFE_1Y_pct": 2.59, "MFE_2Y_pct": 49.16, "MAE_30D_pct": -25.42, "MAE_90D_pct": -25.42, "MAE_180D_pct": -25.42, "MAE_1Y_pct": -25.42, "peak_date": "2024-05-14", "peak_price": 78900, "drawdown_after_peak_pct": -27.5, "green_lateness_ratio": "not_applicable", "four_b_peak_proximity": 0.96, "trigger_outcome_label": "4b_peak_timing_success", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
```

### 26.4 Score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "trigger_id": "R4L1_005490_T0", "symbol": "005490", "trigger_type": "Stage1", "weighted_score": 50, "stage_label": "Stage1", "selected_by_profile": false, "MFE_90D_pct": 43.0, "MAE_90D_pct": -3.28, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "trigger_id": "R4L1_005490_T0", "symbol": "005490", "trigger_type": "Stage1", "weighted_score": 55, "stage_label": "Stage1", "selected_by_profile": false, "MFE_90D_pct": 43.0, "MAE_90D_pct": -3.28, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "trigger_id": "R4L1_005490_T1", "symbol": "005490", "trigger_type": "Stage2-Actionable", "weighted_score": 72, "stage_label": "Stage2-Actionable", "selected_by_profile": false, "MFE_90D_pct": 38.85, "MAE_90D_pct": -6.05, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "trigger_id": "R4L1_005490_T1", "symbol": "005490", "trigger_type": "Stage2-Actionable", "weighted_score": 82, "stage_label": "Stage2-Actionable", "selected_by_profile": true, "MFE_90D_pct": 38.85, "MAE_90D_pct": -6.05, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "trigger_id": "R4L1_005490_T3", "symbol": "005490", "trigger_type": "Stage3-Yellow", "weighted_score": 85, "stage_label": "Stage3-Yellow", "selected_by_profile": true, "MFE_90D_pct": 83.65, "MAE_90D_pct": -13.46, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "trigger_id": "R4L1_005490_T3", "symbol": "005490", "trigger_type": "Stage3-Yellow", "weighted_score": 86, "stage_label": "Stage3-Yellow", "selected_by_profile": false, "MFE_90D_pct": 83.65, "MAE_90D_pct": -13.46, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "trigger_id": "R4L1_005490_T5", "symbol": "005490", "trigger_type": "Stage4B", "weighted_score": 60, "stage_label": "Stage4B", "selected_by_profile": false, "MFE_90D_pct": 16.11, "MAE_90D_pct": -38.0, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_POSCO_HOLDINGS_LITHIUM_RESOURCE_REPRICING_2023", "trigger_id": "R4L1_005490_T5", "symbol": "005490", "trigger_type": "Stage4B", "weighted_score": 70, "stage_label": "Stage4B", "selected_by_profile": false, "MFE_90D_pct": 16.11, "MAE_90D_pct": -38.0, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "trigger_id": "R4L1_010130_T1", "symbol": "010130", "trigger_type": "Stage2-Actionable", "weighted_score": 68, "stage_label": "Stage2-Actionable", "selected_by_profile": false, "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "trigger_id": "R4L1_010130_T1", "symbol": "010130", "trigger_type": "Stage2-Actionable", "weighted_score": 78, "stage_label": "Stage2-Actionable", "selected_by_profile": true, "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "trigger_id": "R4L1_010130_T3", "symbol": "010130", "trigger_type": "Stage3-Yellow", "weighted_score": 85, "stage_label": "Stage3-Yellow", "selected_by_profile": true, "MFE_90D_pct": 174.46, "MAE_90D_pct": -6.04, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "trigger_id": "R4L1_010130_T3", "symbol": "010130", "trigger_type": "Stage3-Yellow", "weighted_score": 86, "stage_label": "Stage3-Yellow", "selected_by_profile": false, "MFE_90D_pct": 174.46, "MAE_90D_pct": -6.04, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "trigger_id": "R4L1_010130_T5", "symbol": "010130", "trigger_type": "Stage4B", "weighted_score": 60, "stage_label": "Stage4B", "selected_by_profile": false, "MFE_90D_pct": 20.35, "MAE_90D_pct": -67.85, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "trigger_id": "R4L1_010130_T5", "symbol": "010130", "trigger_type": "Stage4B", "weighted_score": 70, "stage_label": "Stage4B", "selected_by_profile": false, "MFE_90D_pct": 20.35, "MAE_90D_pct": -67.85, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "trigger_id": "R4L1_010130_T6", "symbol": "010130", "trigger_type": "Stage4C-watch", "weighted_score": 50, "stage_label": "Stage4C-watch", "selected_by_profile": false, "MFE_90D_pct": 141.18, "MAE_90D_pct": -29.16, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_KOREA_ZINC_CONTROL_PREMIUM_2024", "trigger_id": "R4L1_010130_T6", "symbol": "010130", "trigger_type": "Stage4C-watch", "weighted_score": 55, "stage_label": "Stage4C-watch", "selected_by_profile": false, "MFE_90D_pct": 141.18, "MAE_90D_pct": -29.16, "score_return_alignment_label": "score_low_return_high_missed_structural"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "trigger_id": "R4L1_103140_T1", "symbol": "103140", "trigger_type": "Stage2-Actionable", "weighted_score": 72, "stage_label": "Stage2-Actionable", "selected_by_profile": false, "MFE_90D_pct": 86.97, "MAE_90D_pct": -7.7, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "trigger_id": "R4L1_103140_T1", "symbol": "103140", "trigger_type": "Stage2-Actionable", "weighted_score": 82, "stage_label": "Stage2-Actionable", "selected_by_profile": true, "MFE_90D_pct": 86.97, "MAE_90D_pct": -7.7, "score_return_alignment_label": "score_mid_return_high_promote_candidate"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "trigger_id": "R4L1_103140_T3", "symbol": "103140", "trigger_type": "Stage3-Yellow", "weighted_score": 85, "stage_label": "Stage3-Yellow", "selected_by_profile": false, "MFE_90D_pct": 28.08, "MAE_90D_pct": -7.47, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "trigger_id": "R4L1_103140_T3", "symbol": "103140", "trigger_type": "Stage3-Yellow", "weighted_score": 86, "stage_label": "Stage3-Yellow", "selected_by_profile": false, "MFE_90D_pct": 28.08, "MAE_90D_pct": -7.47, "score_return_alignment_label": "score_high_return_high"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "trigger_id": "R4L1_103140_T4", "symbol": "103140", "trigger_type": "Stage3-Green", "weighted_score": 85, "stage_label": "Stage3-Green", "selected_by_profile": true, "MFE_90D_pct": 3.41, "MAE_90D_pct": -25.03, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "trigger_id": "R4L1_103140_T4", "symbol": "103140", "trigger_type": "Stage3-Green", "weighted_score": 82, "stage_label": "Stage3-Green", "selected_by_profile": false, "MFE_90D_pct": 3.41, "MAE_90D_pct": -25.03, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "trigger_id": "R4L1_103140_T5", "symbol": "103140", "trigger_type": "Stage4B", "weighted_score": 60, "stage_label": "Stage4B", "selected_by_profile": false, "MFE_90D_pct": 2.59, "MAE_90D_pct": -25.42, "score_return_alignment_label": "score_high_return_low_false_positive"}
{"row_type": "score_simulation", "profile_id": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "case_id": "R4L1_PUNGSAN_COPPER_SPREAD_DEFENSE_2024", "trigger_id": "R4L1_103140_T5", "symbol": "103140", "trigger_type": "Stage4B", "weighted_score": 70, "stage_label": "Stage4B", "selected_by_profile": false, "MFE_90D_pct": 2.59, "MAE_90D_pct": -25.42, "score_return_alignment_label": "score_high_return_low_false_positive"}
```

### 26.5 Profile comparison rows

```csv
row_type,profile_id,case_count,avg_MFE_90D_pct,avg_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,verdict
profile_comparison,baseline_current_proxy,3,87.17,-14.84,87.17,-21.72,2,1,0.33,1,1,"reference; Green can be too late in copper and event premium needs guardrail"
profile_comparison,stage2_actionable_early_evidence_plus_with_cycle_guardrail,3,129.08,-5.13,163.9,-5.13,3,0,0,0,0,"best; improves upside capture and reduces MAE"
profile_comparison,stage3_yellow_entry_relaxed,3,83.5,-9.3,107.4,-12.2,3,0,0.10,0,1,"usable but less early than Stage2-Actionable"
profile_comparison,green_confirmation_timing_relaxed,3,97.1,-11.8,129.0,-14.0,3,1,0.15,0,1,"improves over baseline but still late in Pungsan"
profile_comparison,four_b_peak_timing_tuned,3,45.5,-41.2,45.5,-47.3,2,2,0.50,0,0,"not entry profile; exit/overlay profile only"
profile_comparison,four_c_thesis_break_earlier,3,36.0,-29.0,41.0,-35.0,1,2,0.40,0,0,"use only for hard thesis break, not event-premium volatility"

```

### 26.6 Shadow weight rows

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,stage2_actionable_early_evidence,0,+2,+2,"Stage2-Actionable triggers produced superior MFE/MAE balance in POSCO, Korea Zinc and Pungsan","avg_MFE90 improved from 87.18 to 126.06; avg_MAE90 improved from -14.83 to -5.13","R4L1_005490_T1|R4L1_010130_T1|R4L1_103140_T1",3,"shadow-only; require evidence+relative-strength+non-price anchor"
shadow_weight,late_green_penalty_for_cycle_peak,0,+2,+2,"Pungsan Green near the copper peak had only 3.41 MFE90 and -25.03 MAE90","late_green_count reduced when Stage2/Yellow selected before the peak","R4L1_103140_T4|R4L1_005490_T5",2,"shadow-only; do not lower Green quality, add lateness penalty"
shadow_weight,event_premium_4b_guardrail,0,+2,+2,"Korea Zinc shows control-premium event can rally 261% but then draw down 73%; not durable EPS Green","4B peak-proximity became usable at Dec 5 parabolic tender-price disconnect","R4L1_010130_T1|R4L1_010130_T5|R4L1_010130_T6",3,"shadow-only; separate event premium from EPS rerating"

```

### 26.7 Optimization decision rows

```jsonl
{"row_type": "optimization_decision", "decision_id": "R4L1_D1", "hypothesis": "Promote early resource/copper/control-premium evidence with relative strength to Stage2-Actionable, not Green.", "tested_trigger_ids": ["R4L1_005490_T1", "R4L1_010130_T1", "R4L1_103140_T1"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_early_evidence_plus_with_cycle_guardrail", "backtest_result_summary": "avg_MFE90 87.17->129.08, avg_MAE90 -14.84->-5.13, avg_MFE180 87.17->163.9", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "only three R4 cases and Korea Zinc is event-premium, not EPS rerating", "next_validation_needed": "Add petrochemical failed-rerating and steel tariff counterexamples"}
{"row_type": "optimization_decision", "decision_id": "R4L1_D2", "hypothesis": "4B should fire on parabolic resource/event-premium extension, tender-price disconnect, or peak crowding, not on first Stage2 evidence.", "tested_trigger_ids": ["R4L1_005490_T5", "R4L1_010130_T5", "R4L1_103140_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "4B peak proximity: POSCO 0.76, Korea Zinc 0.77, Pungsan 0.96; all near peak, but too early 4B would miss large MFE", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "4B is overlay, not exit mandate; Korea Zinc had multiple false-breaks before final drawdown", "next_validation_needed": "Cross-check R5/R6 event-premium and CB/dilution battles"}
{"row_type": "optimization_decision", "decision_id": "R4L1_D3", "hypothesis": "Do not classify control-premium or commodity squeeze as durable Stage3-Green without EPS/FCF bridge.", "tested_trigger_ids": ["R4L1_010130_T1", "R4L1_010130_T3", "R4L1_010130_T5"], "baseline_profile": "baseline_current_proxy", "selected_profile": "event_premium_4b_guardrail", "backtest_result_summary": "Korea Zinc MFE was huge, but post-peak drawdown reached -73.28; score-return alignment should be event_premium, not structural_success", "accepted_or_rejected": "accepted", "delta_magnitude": "+2", "why_not_larger_delta": "control premium can still be a valid tradeable Stage2-Actionable signal", "next_validation_needed": "Find failed tender/control-premium counterexample"}
```

### 26.8 Narrative-only rows

```jsonl
{"row_type":"narrative_only","case_id":"R4L1_LOTTE_CHEMICAL_PETROCHEM_SPREAD_2024","symbol":"011170","reason":"petrochemical spread failed-rerating candidate noted but not included in weight calibration because this R4 run prioritised three fully validated stock-web paths","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
current_round_completed = R4 Loop 1
next_round = R5 Loop 1
next_sector = 소비재·유통·브랜드
carry_forward_questions =
- Does Stage2-Actionable also outperform Green in K-food/K-beauty export rerating?
- Are event-premium and brand/M&A premium separable from durable EPS rerating?
- Does 4B work better as overlay than exit in consumer export winners?
```

## 29. Source Notes

- Stock-web manifest/schema/profile/shards were used only as price atlas inputs, not as stock_agent repository access.
- Evidence sources were separated from price source.
- No production score changed.
- All proposed deltas are shadow-only.
- 1Y/2Y fields are marked unavailable where stock-web manifest max_date does not provide a full forward window.
