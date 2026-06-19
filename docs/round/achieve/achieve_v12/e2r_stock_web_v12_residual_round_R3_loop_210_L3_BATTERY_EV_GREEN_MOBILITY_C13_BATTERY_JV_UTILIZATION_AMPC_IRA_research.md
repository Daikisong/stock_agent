# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```text
research_file = e2r_stock_web_v12_residual_round_R3_loop_210_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
selected_round = R3
selected_loop = 210
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / balance-quality reinforcement + Priority 0 direct URL and MFE/MAE repair
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD
loop_objective = AMPC/IRA persistence, JV utilization failure, policy-financing high-MAE guard, hard-4C confirmation
round_schedule_status = coverage_index_selected; immediate C15/C05/C01 repetition avoided
round_sector_consistency = pass
price_source = Songdaiki/stock-web / atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption
Assumption: the current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. It already has the global Stage2 bridge, Yellow/Green thresholds, full-4B non-price requirement, price-only guard, and hard-4C routing. This run does not change production scoring; it only proposes a C13/L3 shadow refinement.

For C13, the remaining error is not “subsidy good” versus “subsidy bad.” It is a plumbing problem. AMPC/IRA credit is cash-like only when tied to actual North America volume, customer shipment, and utilization. A factory loan is a pipe in the wall; utilization is water moving through it. The profile must learn the difference.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
| --- | --- |
| selected_round | R3 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA |
| fine_archetype_id | C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD |
| sector scope | battery cells, EV battery JVs, North America AMPC/IRA credit, utilization ramp, policy financing, demand slowdown protection |
| non-scope | live candidate scan, current recommendation, brokerage/API use, stock_agent code patch |

## 3. Previous Coverage / Duplicate Avoidance Check
The ledger shows that every C01~C32 archetype is already beyond the 80-row floor, so new work should improve quality rather than add duplicate bulk. The Priority-1 table explicitly lists C13 as needing AMPC/IRA persistence and JV-utilization failure cases. This run uses direct company/government/Reuters URLs and complete Stock-Web 30D/90D/180D rows.

| duplicate control | status |
| --- | --- |
| immediate prior local artifacts | C15 loop72, C05 loop208, C01 loop209; not repeated |
| selected C13 top-symbol risk | 373220, 006400, 096770 are known C13-heavy symbols, but every row uses a new trigger family and exact date key in this run |
| hard duplicate key | `canonical_archetype_id + symbol + trigger_type + entry_date`; no duplicate within this artifact |
| source quality | direct LGES/Samsung SDI/DOE URLs plus Reuters confirmation for BlueOval SK |
| price quality | all six mandatory 30/90/180 MFE/MAE fields present in every usable trigger row |

## 4. Stock-Web OHLC Input / Price Source Validation
```json
{
  "source_name": "FinanceData/marcap",
  "price_data_source": "Songdaiki/stock-web",
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
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```
All quantitative rows use `tradable_raw` Stock-Web shards. The raw basis is intentionally unadjusted; corporate-action windows are blocked when the profile candidate date overlaps entry through D+180.

| schema rule | applied handling |
| --- | --- |
| tradable columns | `d,o,h,l,c,v,a,mc,s,m` |
| entry price | close column `c` on selected entry date |
| MFE_N_pct | max high from entry through N tradable rows / entry close - 1 |
| MAE_N_pct | min low from entry through N tradable rows / entry close - 1 |
| minimum quantitative window | 180 forward tradable rows |
| price adjustment | raw_unadjusted_marcap; no corporate-action adjustment assumed |

## 5. Historical Eligibility Gate
| trigger_id | trigger_date | entry_date | entry timing rule | 180D end | corporate-action status | calibration_usable | block reasons |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725 | 2024-07-25 | 2024-07-26 | company release date had no machine-verified intraday timestamp in this run; use next stock-web tradable close | 2025-04-24 | clean_180D_window | true | [] |
| C13_L210_T002_373220_STAGE3_GREEN_20241028 | 2024-10-28 | 2024-10-29 | company release date had no machine-verified intraday timestamp in this run; use next stock-web tradable close | 2025-07-24 | clean_180D_window | true | [] |
| C13_L210_T003_006400_STAGE3_YELLOW_20240730 | 2024-07-30 | 2024-07-31 | company release date had no machine-verified intraday timestamp in this run; use next stock-web tradable close | 2025-04-29 | clean_180D_window | true | [] |
| C13_L210_T004_006400_STAGE4C_20241030 | 2024-10-30 | 2024-10-31 | company release date had no machine-verified intraday timestamp in this run; use next stock-web tradable close | 2025-07-28 | clean_180D_window | true | [] |
| C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216 | 2024-12-16 | 2024-12-17 | U.S. DOE/Reuters event reached Korea after the Dec. 16 Korean close; use next stock-web tradable close | 2025-09-12 | clean_180D_window | true | [] |
| C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124 | 2025-01-24 | 2025-01-31 | company release date had no machine-verified intraday timestamp in this run and Korea holiday gap followed; use next available stock-web tradable close | 2025-10-27 | clean_180D_window | true | [] |

## 6. Canonical Archetype Compression Map
| C13 subproblem | evidence that counts | evidence that must be capped | likely model error |
| --- | --- | --- | --- |
| AMPC / IRA credit | credit amount + actual North America volume/customer shipment + utilization bridge | credit amount alone | reported-OP Green false positive |
| JV utilization | production start, customer offtake, stable ramp, ex-credit profit progress | factory construction or financing alone | policy event promoted too high |
| demand slowdown | revenue/profit collapse plus guidance/demand language plus deep MAE | one bad quarter without route confirmation | hard 4C too late or too early |
| capex discipline repair | capex cut, demand-mix rotation, revenue guidance, later price confirmation | management aspiration only | too-late Stage2/Yellow recovery |

## 7. Case Selection Summary
| case_id | trigger_id | symbol | company | trigger_type | trigger_family | pos/counter | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C13_L210_CASE_01_LGES_Q2_AMPC_VOLUME_UTILIZATION_BRIDGE | C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725 | 373220 | LG Energy Solution / LG에너지솔루션 | Stage2-Actionable | ampc_credit_plus_north_america_volume_despite_ex_credit_loss | positive | current_profile_missed_structural |
| C13_L210_CASE_02_LGES_Q3_AMPC_GREEN_TRAP | C13_L210_T002_373220_STAGE3_GREEN_20241028 | 373220 | LG Energy Solution / LG에너지솔루션 | Stage3-Green | reported_operating_profit_masked_by_ampc_credit_ex_credit_loss | counterexample | current_profile_false_positive |
| C13_L210_CASE_03_SAMSUNG_SDI_Q2_SEQUENTIAL_OP_HIGH_MAE | C13_L210_T003_006400_STAGE3_YELLOW_20240730 | 006400 | Samsung SDI / 삼성SDI | Stage3-Yellow | sequential_operating_profit_improvement_inside_ev_demand_slowdown | counterexample | current_profile_false_positive |
| C13_L210_CASE_04_SAMSUNG_SDI_Q3_DEMAND_SLOWDOWN_4C | C13_L210_T004_006400_STAGE4C_20241030 | 006400 | Samsung SDI / 삼성SDI | Stage4C | revenue_operating_profit_collapse_and_demand_slowdown_hard_4c | counterexample | current_profile_4C_too_late |
| C13_L210_CASE_05_SKINNO_BLUEOVAL_POLICY_FINANCING_HIGH_MAE | C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216 | 096770 | SK Innovation / SK이노베이션 | Stage2-Actionable | jv_policy_financing_without_utilization_or_profit_conversion | counterexample | current_profile_false_positive |
| C13_L210_CASE_06_LGES_FY2024_CAPEX_DISCIPLINE_ESS_REPAIR | C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124 | 373220 | LG Energy Solution / LG에너지솔루션 | Stage2-Actionable | capex_discipline_after_utilization_downcycle_and_forward_revenue_guidance | positive | current_profile_correct |

## 8. Positive vs Counterexample Balance
| bucket | count | average MFE_180D | average MAE_180D | interpretation |
| --- | ---: | ---: | ---: | --- |
| positive | 2 | 39.26 | -14.45 | AMPC/capex discipline can work when paired with volume or repair evidence, but Green still needs ex-credit profit/utilization |
| counterexample | 4 | 12.88 | -41.43 | subsidy mask, demand slowdown, and policy financing without utilization produce high-MAE traps |

## 9. Evidence Source Map
| evidence_key | source type | URL | compressed evidence |
| --- | --- | --- | --- |
| LGES_Q2_2024 | direct_company_release | https://news.lgensol.com/company-news/press-releases/3096/ | LG Energy Solution Q2 2024 reported KRW 447.8B estimated IRA tax credit; excluding the credit it would have recorded KRW 252.5B operating loss; credit rose with increased North America volume while utilization adjustment burdened fixed cost. |
| LGES_Q3_2024 | direct_company_release | https://news.lgensol.com/company-news/press-releases/3343/ | LG Energy Solution Q3 2024 reported KRW 448.3B operating profit including KRW 466B estimated IRA tax credit; excluding the credit it would have recorded KRW 17.7B operating loss. |
| SAMSUNG_SDI_Q2_2024 | direct_company_release | https://www.samsungsdi.com/sdi-now/sdi-news/3862.html | Samsung SDI Q2 2024 reported revenue of KRW 4.45T and operating profit of KRW 280.2B; revenue declined 24% YoY and 13% QoQ while operating profit fell 38% YoY but rose 5% QoQ. |
| SAMSUNG_SDI_Q3_2024 | direct_company_release | https://www.samsungsdi.com/sdi-now/sdi-news/4082.html | Samsung SDI Q3 2024 reported KRW 3.94T revenue, down 30% YoY, and KRW 129.9B operating profit, down 72% YoY; Q4 improvement could remain limited by slowing demand. |
| DOE_BLUEOVAL_SK_2024 | government_direct_release | https://www.energy.gov/edf/articles/doe-announces-963-billion-loan-blueoval-sk-further-expand-us-manufacturing-electric | U.S. DOE announced a $9.63B direct loan to BlueOval SK to finance three EV battery manufacturing plants in Tennessee and Kentucky. |
| REUTERS_BLUEOVAL_SK_2024 | reputable_news_confirmation | https://www.reuters.com/business/autos-transportation/us-finalizes-963-billion-loan-ford-sk-joint-battery-venture-2024-12-16/ | Reuters reported the DOE loan finalization for the Ford/SK On BlueOval SK joint venture and noted production plans for 2025. |
| LGES_FY2024 | direct_company_release | https://news.lgensol.com/company-news/press-releases/3587/ | LG Energy Solution FY2024 reported KRW 25.6T consolidated revenue and KRW 575.4B operating profit; 2025 guidance called for 5–10% revenue growth and a 20–30% capex reduction. |

## 10. Price Data Source Map
| symbol | company | profile path | corporate-action candidate dates considered | tradable shard files touched |
| --- | --- | --- | --- | --- |
| 373220 | LG Energy Solution / LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | [] — no corporate_action_candidate_dates in checked profile | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv, atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv |
| 006400 | Samsung SDI / 삼성SDI | atlas/symbol_profiles/006/006400.json | ['1996-01-03', '1998-11-03', '2014-07-15'] — profile candidate dates are pre-2024 and outside all sampled windows | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv, atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv |
| 096770 | SK Innovation / SK이노베이션 | atlas/symbol_profiles/096/096770.json | ['2024-11-20'] — 2024-11-20 candidate blocks pre-event 180D rows; selected 2024-12-17 entry is after the candidate date | atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv, atlas/ohlcv_tradable_by_symbol_year/096/096770/2025.csv |

## 11. Case-by-Case Trigger Grid
| trigger_id | entry row OHLCV | evidence read | model read |
| --- | --- | --- | --- |
| C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725 | 2024-07-26 o=332000 h=334000 l=322500 c=325000 v=165067 a=53916369961 mc=76050000000000 | LG Energy Solution Q2 2024 reported KRW 447.8B estimated IRA tax credit; excluding the credit it would have recorded KRW 252.5B operating loss; credit rose with increased North America volume while utilization adjustment burdened fixed cost. | AMPC is not automatically fake quality. When the credit is tied to actual North America production volume, it can be a valid Stage2-to-Yellow bridge even while ex-credit profit is still negative. |
| C13_L210_T002_373220_STAGE3_GREEN_20241028 | 2024-10-29 o=410000 h=412500 l=400500 c=409000 v=281126 a=114255967000 mc=95706000000000 | LG Energy Solution Q3 2024 reported KRW 448.3B operating profit including KRW 466B estimated IRA tax credit; excluding the credit it would have recorded KRW 17.7B operating loss. | The headline profit looks like Green, but the ex-credit loss is the trapdoor. The forward path confirms the trap: small MFE and deep 180D MAE. |
| C13_L210_T003_006400_STAGE3_YELLOW_20240730 | 2024-07-31 o=330000 h=331500 l=312000 c=319500 v=808998 a=258022147000 mc=21970267335000 | Samsung SDI Q2 2024 reported revenue of KRW 4.45T and operating profit of KRW 280.2B; revenue declined 24% YoY and 13% QoQ while operating profit fell 38% YoY but rose 5% QoQ. | A QoQ operating-profit uptick is a spark, not a battery pack. The forward path gives a temporary MFE but a larger 180D MAE, so the evidence should stay below Green. |
| C13_L210_T004_006400_STAGE4C_20241030 | 2024-10-31 o=334500 h=341000 l=327000 c=327000 v=378994 a=125792837000 mc=22486001310000 | Samsung SDI Q3 2024 reported KRW 3.94T revenue, down 30% YoY, and KRW 129.9B operating profit, down 72% YoY; Q4 improvement could remain limited by slowing demand. | This is not just volatility. The thesis engine lost torque: revenue, operating profit, demand, and price path all point in the same direction. |
| C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216 | 2024-12-17 o=121600 h=122100 l=116900 c=119200 v=348803 a=41499634200 mc=18003345299200 | U.S. DOE announced a $9.63B direct loan to BlueOval SK to finance three EV battery manufacturing plants in Tennessee and Kentucky. | Policy financing is oxygen for the factory, not proof the factory is breathing at full rate. Until utilization and margins arrive, it is a watch bridge, not Green. |
| C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124 | 2025-01-31 o=353500 h=356500 l=346500 c=352000 v=147908 a=51977272500 mc=82368000000000 | LG Energy Solution FY2024 reported KRW 25.6T consolidated revenue and KRW 575.4B operating profit; 2025 guidance called for 5–10% revenue growth and a 20–30% capex reduction. | The repair worked over 180D, but the first half of the path still cut deep. The right label is patient Yellow, not immediate Green. |

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | entry_date | entry_price | MFE_30D | MAE_30D | 30D end | MFE_90D | MAE_90D | 90D end | MFE_180D | MAE_180D | 180D end | peak_date | peak_price | drawdown_after_peak |
| --- | --- | ---: | ---: | ---: | --- | ---: | ---: | --- | ---: | ---: | --- | --- | ---: | ---: |
| C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725 | 2024-07-26 | 325000.00 | 28.92 | -4.31 | 2024-09-06 | 36.62 | -4.31 | 2024-12-09 | 36.62 | -4.46 | 2025-04-24 | 2024-10-08 | 444000.00 | -30.07 |
| C13_L210_T002_373220_STAGE3_GREEN_20241028 | 2024-10-29 | 409000.00 | 6.48 | -9.29 | 2024-12-09 | 6.48 | -19.93 | 2025-03-13 | 6.48 | -34.96 | 2025-07-24 | 2024-11-11 | 435500.00 | -38.92 |
| C13_L210_T003_006400_STAGE3_YELLOW_20240730 | 2024-07-31 | 319500.00 | 18.94 | -7.82 | 2024-09-11 | 23.16 | -26.29 | 2024-12-12 | 23.16 | -46.79 | 2025-04-29 | 2024-09-30 | 393500.00 | -56.80 |
| C13_L210_T004_006400_STAGE4C_20241030 | 2024-10-31 | 327000.00 | 4.28 | -27.98 | 2024-12-11 | 4.28 | -42.87 | 2025-03-17 | 4.28 | -51.77 | 2025-07-28 | 2024-10-31 | 341000.00 | -53.75 |
| C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216 | 2024-12-17 | 119200.00 | 10.07 | -7.72 | 2025-02-05 | 17.62 | -22.99 | 2025-05-02 | 17.62 | -32.21 | 2025-09-12 | 2025-03-13 | 140200.00 | -42.37 |
| C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124 | 2025-01-31 | 352000.00 | 9.80 | -7.67 | 2025-03-14 | 9.80 | -24.43 | 2025-06-13 | 41.90 | -24.43 | 2025-10-27 | 2025-10-27 | 499500.00 | -3.90 |

### 12.1 Path notes
- `C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725`: below-entry flags 30/90/180 = True/True/True; D+180 window low 2025-04-03 at 310500.00; post-peak drawdown low 2025-04-03.
- `C13_L210_T002_373220_STAGE3_GREEN_20241028`: below-entry flags 30/90/180 = True/True/True; D+180 window low 2025-05-23 at 266000.00; post-peak drawdown low 2025-05-23.
- `C13_L210_T003_006400_STAGE3_YELLOW_20240730`: below-entry flags 30/90/180 = True/True/True; D+180 window low 2025-04-09 at 170000.00; post-peak drawdown low 2025-04-09.
- `C13_L210_T004_006400_STAGE4C_20241030`: below-entry flags 30/90/180 = True/True/True; D+180 window low 2025-05-22 at 157700.00; post-peak drawdown low 2025-05-22.
- `C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216`: below-entry flags 30/90/180 = True/True/True; D+180 window low 2025-05-23 at 80800.00; post-peak drawdown low 2025-05-23.
- `C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124`: below-entry flags 30/90/180 = True/True/True; D+180 window low 2025-05-23 at 266000.00; post-peak drawdown low 2025-10-27.

## 13. Current Calibrated Profile Stress Test
| trigger_id | before profile stage/score | after shadow stage/score | current verdict | actual path verdict |
| --- | --- | --- | --- | --- |
| C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725 | Stage2 / 72.0 | Stage3-Yellow / 80.5 | current_profile_missed_structural | MFE180 36.62 / MAE180 -4.46; positive_when_ampc_credit_has_volume_bridge_but_green_capped_by_ex_credit_loss |
| C13_L210_T002_373220_STAGE3_GREEN_20241028 | Stage3-Green / 88.0 | Stage2-Actionable / 73.0 | current_profile_false_positive | MFE180 6.48 / MAE180 -34.96; counterexample_ampc_masked_green_false_positive |
| C13_L210_T003_006400_STAGE3_YELLOW_20240730 | Stage3-Yellow / 80.0 | Stage2-Actionable / 68.0 | current_profile_false_positive | MFE180 23.16 / MAE180 -46.79; counterexample_yellow_should_not_green_when_sequential_op_improves_but_cycle_decays |
| C13_L210_T004_006400_STAGE4C_20241030 | Stage4B / 61.0 | Stage4C / 42.0 | current_profile_4C_too_late | MFE180 4.28 / MAE180 -51.77; hard_4c_protection_success_demand_slowdown_confirmed |
| C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216 | Stage3-Yellow / 77.0 | Stage2-Actionable / 65.0 | current_profile_false_positive | MFE180 17.62 / MAE180 -32.21; counterexample_policy_financing_not_utilization_green |
| C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124 | Stage2-Actionable / 70.0 | Stage3-Yellow / 76.0 | current_profile_correct | MFE180 41.90 / MAE180 -24.43; positive_repair_after_capex_discipline_but_high_mae_yellow_cap |

Key stress-test answers: Stage2 bridge is useful but incomplete for C13 unless it distinguishes credit quality. Yellow 75 is acceptable when AMPC has volume bridge, but too generous when the same credit merely masks ex-credit loss. Green 87/revision 55 is too permissive for reported OP that depends entirely on AMPC. Full 4B non-price requirement remains appropriate. Hard 4C should fire earlier when revenue/profit collapse, demand language, and deep 180D MAE align.

## 14. Stage2 / Yellow / Green Comparison
| evidence pattern | Stage2 handling | Yellow handling | Green handling |
| --- | --- | --- | --- |
| AMPC amount + North America volume bridge but ex-credit loss | allowed | allowed with cap | blocked until ex-credit profit/utilization improves |
| reported OP positive only because AMPC > operating profit | allowed as watch | maybe capped | blocked |
| QoQ OP improvement while YoY revenue/profit still falling | allowed | cautious only | blocked unless order/utilization bridge appears |
| DOE/JV financing before production ramp | allowed as policy bridge | blocked unless utilization/offtake appears | blocked |
| capex discipline + forward revenue guidance after downcycle | allowed | allowed if path confirms | blocked until high-MAE risk fades and profit bridge appears |

## 15. 4B Local vs Full-window Timing Audit
| trigger_id | local 4B signal | full-window 4B signal | verdict |
| --- | --- | --- | --- |
| C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725 | no | no | not a 4B overlay; promotion still capped by non-price evidence |
| C13_L210_T002_373220_STAGE3_GREEN_20241028 | yes | yes | use 4B watch/guard; do not use as positive promotion row |
| C13_L210_T003_006400_STAGE3_YELLOW_20240730 | yes | yes | use 4B watch/guard; do not use as positive promotion row |
| C13_L210_T004_006400_STAGE4C_20241030 | yes | yes | escalate beyond 4B to hard 4C after evidence + path confirmation |
| C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216 | yes | yes | use 4B watch/guard; do not use as positive promotion row |
| C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124 | yes | yes | use 4B watch/guard; do not use as positive promotion row |

## 16. 4C Protection Audit
| trigger_id | hard 4C required? | reason |
| --- | --- | --- |
| C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725 | no | no durable thesis-death evidence; keep as Stage2/Yellow/4B watch depending on path. |
| C13_L210_T002_373220_STAGE3_GREEN_20241028 | no | no durable thesis-death evidence; keep as Stage2/Yellow/4B watch depending on path. |
| C13_L210_T003_006400_STAGE3_YELLOW_20240730 | no | no durable thesis-death evidence; keep as Stage2/Yellow/4B watch depending on path. |
| C13_L210_T004_006400_STAGE4C_20241030 | yes | revenue down 30%, operating profit down 72%, demand slowdown language, and 180D MAE below -50% align. |
| C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216 | no | no durable thesis-death evidence; keep as Stage2/Yellow/4B watch depending on path. |
| C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124 | no | no durable thesis-death evidence; keep as Stage2/Yellow/4B watch depending on path. |

## 17. Sector-Specific Rule Candidate
`L3 battery/EV green-mobility evidence should split policy credit, factory financing, and utilization conversion. AMPC/IRA credit can support Stage2/Yellow only when tied to realized regional production volume, customer shipments, or utilization; policy/JV financing alone remains a watch bridge. Reported operating profit that depends on AMPC while ex-credit profit is negative should be capped below Green.`

## 18. Canonical-Archetype Rule Candidate
`C13_BATTERY_JV_UTILIZATION_AMPC_IRA needs an AMPC quality ladder: (1) credit amount, (2) production volume/customer shipment, (3) utilization/capex discipline, (4) ex-credit operating-profit trend. Green requires at least steps 2~4, not step 1 alone. Hard 4C triggers when demand slowdown, revenue/profit collapse, and deep MAE align.`

## 19. Before / After Backtest Comparison
| trigger_id | before score | after shadow score | score movement | MFE_90D | MAE_90D | alignment |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725 | 72.0 | 80.5 | +8.5 | 36.62 | -4.31 | positive_when_ampc_credit_has_volume_bridge_but_green_capped_by_ex_credit_loss |
| C13_L210_T002_373220_STAGE3_GREEN_20241028 | 88.0 | 73.0 | -15.0 | 6.48 | -19.93 | counterexample_ampc_masked_green_false_positive |
| C13_L210_T003_006400_STAGE3_YELLOW_20240730 | 80.0 | 68.0 | -12.0 | 23.16 | -26.29 | counterexample_yellow_should_not_green_when_sequential_op_improves_but_cycle_decays |
| C13_L210_T004_006400_STAGE4C_20241030 | 61.0 | 42.0 | -19.0 | 4.28 | -42.87 | hard_4c_protection_success_demand_slowdown_confirmed |
| C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216 | 77.0 | 65.0 | -12.0 | 17.62 | -22.99 | counterexample_policy_financing_not_utilization_green |
| C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124 | 70.0 | 76.0 | +6.0 | 9.80 | -24.43 | positive_repair_after_capex_discipline_but_high_mae_yellow_cap |

## 20. Score-Return Alignment Matrix
| alignment class | trigger_ids | lesson |
| --- | --- | --- |
| constructive positive but Green-capped | C13_L210_T001, C13_L210_T006 | positive paths need volume/capex bridge but still tolerate high-MAE caution |
| subsidy-mask false positive | C13_L210_T002 | reported OP can be a mirror; ex-credit profit is the face |
| demand-slowdown high-MAE trap | C13_L210_T003, C13_L210_T004 | YoY decline and demand language should dominate small sequential improvements |
| policy financing without utilization | C13_L210_T005 | money committed to a plant is not yet throughput or margin |

## 21. Coverage Matrix
| metric | value |
| --- | ---: |
| new_independent_case_count | 6 |
| reused_case_count | 0 |
| calibration_usable_case_count | 6 |
| calibration_usable_trigger_count | 6 |
| symbol_count | 3 |
| trigger_family_count | 6 |
| positive_case_count | 2 |
| counterexample_count | 4 |
| current_profile_error_count | 5 |

## 22. Residual Contribution Summary
```json
{
  "row_type": "residual_contribution",
  "round": "R3",
  "loop": "210",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD",
  "new_independent_case_count": 6,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "new_trigger_family_count": 6,
  "tested_existing_calibrated_axes": [
    "Stage2 bridge requirement",
    "Stage3-Green revision minimum",
    "full 4B non-price requirement",
    "hard 4C thesis-break routing",
    "price-only blowoff guard"
  ],
  "residual_error_types_found": [
    "ampc_masked_green_false_positive",
    "policy_financing_without_utilization_false_positive",
    "demand_slowdown_hard4c_too_late",
    "positive_ampc_volume_bridge_missed_by_over_strict_filter"
  ],
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```
Contribution label: `canonical_archetype_rule_candidate`. The useful residual is narrow: make C13 understand the AMPC/JV utilization ladder without loosening the global profile.

## 23. Validation Scope / Non-Validation Scope
| scope | included? | note |
| --- | --- | --- |
| Stock-Web 1D OHLC row validation | yes | local shards from `atlas/ohlcv_tradable_by_symbol_year` |
| complete 30/90/180D MFE/MAE | yes | all six mandatory fields included in every trigger row |
| corporate-action 180D block check | yes | 096770 pre-Nov-20 rows avoided; selected Dec-17 row clean |
| direct evidence URLs | yes | company, government, Reuters URLs |
| live trading signal | no | explicitly out of scope |
| stock_agent code patch | no | handoff only, no production change |

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c13_ampc_quality_ladder,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"distinguish AMPC amount from AMPC quality/volume bridge","Q2 LGES positive retained while Q3 AMPC-mask Green false positive is capped","C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725|C13_L210_T002_373220_STAGE3_GREEN_20241028",6,6,4,medium,canonical_shadow_only,"not production; requires batch aggregation"
shadow_weight,c13_ex_credit_operating_profit_green_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"reported OP can be subsidy-flipped while ex-credit profit is negative","blocks Q3 LGES Green trap and preserves Yellow/Stage2 split",C13_L210_T002_373220_STAGE3_GREEN_20241028,6,6,4,medium,canonical_shadow_only,"not production; Green cap only"
shadow_weight,c13_policy_financing_utilization_gate,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"DOE/JV financing does not equal realized utilization or profit conversion","keeps SKI/BlueOval policy event at Stage2 despite headline size",C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216,6,6,4,medium,sector_shadow_only,"not production; policy event watch guard"
shadow_weight,c13_demand_slowdown_hard4c_confirmation,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"severe revenue/profit collapse plus deep 180D MAE should route earlier to protection","supports SDI Q3 hard 4C confirmation",C13_L210_T004_006400_STAGE4C_20241030,6,6,4,medium,canonical_shadow_only,"not production; hard4C protection only"
```

## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "C13_L210_CASE_01_LGES_Q2_AMPC_VOLUME_UTILIZATION_BRIDGE", "symbol": "373220", "company_name": "LG Energy Solution / LG에너지솔루션", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "case_type": "structural_success_with_ampc_quality_bridge", "positive_or_counterexample": "positive", "best_trigger": "C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_when_ampc_credit_has_volume_bridge_but_green_capped_by_ex_credit_loss", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "AMPC is not automatically fake quality. When the credit is tied to actual North America production volume, it can be a valid Stage2-to-Yellow bridge even while ex-credit profit is still negative."}
{"row_type": "case", "case_id": "C13_L210_CASE_02_LGES_Q3_AMPC_GREEN_TRAP", "symbol": "373220", "company_name": "LG Energy Solution / LG에너지솔루션", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "case_type": "green_false_positive_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "C13_L210_T002_373220_STAGE3_GREEN_20241028", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_ampc_masked_green_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The headline profit looks like Green, but the ex-credit loss is the trapdoor. The forward path confirms the trap: small MFE and deep 180D MAE."}
{"row_type": "case", "case_id": "C13_L210_CASE_03_SAMSUNG_SDI_Q2_SEQUENTIAL_OP_HIGH_MAE", "symbol": "006400", "company_name": "Samsung SDI / 삼성SDI", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "case_type": "high_mae_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "C13_L210_T003_006400_STAGE3_YELLOW_20240730", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_yellow_should_not_green_when_sequential_op_improves_but_cycle_decays", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A QoQ operating-profit uptick is a spark, not a battery pack. The forward path gives a temporary MFE but a larger 180D MAE, so the evidence should stay below Green."}
{"row_type": "case", "case_id": "C13_L210_CASE_04_SAMSUNG_SDI_Q3_DEMAND_SLOWDOWN_4C", "symbol": "006400", "company_name": "Samsung SDI / 삼성SDI", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "case_type": "hard_4c_confirmation", "positive_or_counterexample": "counterexample", "best_trigger": "C13_L210_T004_006400_STAGE4C_20241030", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_protection_success_demand_slowdown_confirmed", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "This is not just volatility. The thesis engine lost torque: revenue, operating profit, demand, and price path all point in the same direction."}
{"row_type": "case", "case_id": "C13_L210_CASE_05_SKINNO_BLUEOVAL_POLICY_FINANCING_HIGH_MAE", "symbol": "096770", "company_name": "SK Innovation / SK이노베이션", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "case_type": "policy_financing_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_policy_financing_not_utilization_green", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Policy financing is oxygen for the factory, not proof the factory is breathing at full rate. Until utilization and margins arrive, it is a watch bridge, not Green."}
{"row_type": "case", "case_id": "C13_L210_CASE_06_LGES_FY2024_CAPEX_DISCIPLINE_ESS_REPAIR", "symbol": "373220", "company_name": "LG Energy Solution / LG에너지솔루션", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "case_type": "positive_but_high_mae_repair", "positive_or_counterexample": "positive", "best_trigger": "C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_repair_after_capex_discipline_but_high_mae_yellow_cap", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "The repair worked over 180D, but the first half of the path still cut deep. The right label is patient Yellow, not immediate Green."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725", "case_id": "C13_L210_CASE_01_LGES_Q2_AMPC_VOLUME_UTILIZATION_BRIDGE", "symbol": "373220", "company_name": "LG Energy Solution / LG에너지솔루션", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "sector": "battery_cells", "primary_archetype": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "loop_objective": "AMPC/IRA persistence, JV utilization failure, policy-financing high-MAE guard, and Green-cap repair", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-25", "evidence_available_at_that_date": "company release date had no machine-verified intraday timestamp in this run; use next stock-web tradable close", "evidence_source": "https://news.lgensol.com/company-news/press-releases/3096/", "stage2_evidence_fields": ["IRA/AMPC credit amount disclosed", "North America volume increased", "utilization fixed-cost burden explicitly disclosed"], "stage3_evidence_fields": ["not Green because ex-credit operating loss remained large"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-26", "entry_price": 325000.0, "MFE_30D_pct": 28.92, "MFE_90D_pct": 36.62, "MFE_180D_pct": 36.62, "MFE_1Y_pct": 36.62, "MFE_2Y_pct": null, "MAE_30D_pct": -4.31, "MAE_90D_pct": -4.31, "MAE_180D_pct": -4.46, "MAE_1Y_pct": -18.15, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "peak_date": "2024-10-08", "peak_price": 444000.0, "drawdown_after_peak_pct": -30.07, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b_overlay", "four_b_evidence_type": null, "four_c_protection_label": null, "trigger_outcome_label": "positive_when_ampc_credit_has_volume_bridge_but_green_capped_by_ex_credit_loss", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|2024-07-25|ampc_credit_plus_north_america_volume_despite_ex_credit_loss", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C13_L210_T002_373220_STAGE3_GREEN_20241028", "case_id": "C13_L210_CASE_02_LGES_Q3_AMPC_GREEN_TRAP", "symbol": "373220", "company_name": "LG Energy Solution / LG에너지솔루션", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "sector": "battery_cells", "primary_archetype": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "loop_objective": "AMPC/IRA persistence, JV utilization failure, policy-financing high-MAE guard, and Green-cap repair", "trigger_type": "Stage3-Green", "trigger_date": "2024-10-28", "evidence_available_at_that_date": "company release date had no machine-verified intraday timestamp in this run; use next stock-web tradable close", "evidence_source": "https://news.lgensol.com/company-news/press-releases/3343/", "stage2_evidence_fields": ["reported operating profit positive", "IRA/AMPC credit disclosed"], "stage3_evidence_fields": ["reported OP rebound is not enough because ex-credit OP is still a loss"], "stage4b_evidence_fields": ["local high-MAE warning if promoted on reported OP alone"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-29", "entry_price": 409000.0, "MFE_30D_pct": 6.48, "MFE_90D_pct": 6.48, "MFE_180D_pct": 6.48, "MFE_1Y_pct": 28.85, "MFE_2Y_pct": null, "MAE_30D_pct": -9.29, "MAE_90D_pct": -19.93, "MAE_180D_pct": -34.96, "MAE_1Y_pct": -34.96, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "peak_date": "2024-11-11", "peak_price": 435500.0, "drawdown_after_peak_pct": -38.92, "green_lateness_ratio": 0.753, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b_overlay", "four_b_evidence_type": "non_price_required", "four_c_protection_label": null, "trigger_outcome_label": "counterexample_ampc_masked_green_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|2024-10-28|reported_operating_profit_masked_by_ampc_credit_ex_credit_loss", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C13_L210_T003_006400_STAGE3_YELLOW_20240730", "case_id": "C13_L210_CASE_03_SAMSUNG_SDI_Q2_SEQUENTIAL_OP_HIGH_MAE", "symbol": "006400", "company_name": "Samsung SDI / 삼성SDI", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "sector": "battery_cells_ess", "primary_archetype": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "loop_objective": "AMPC/IRA persistence, JV utilization failure, policy-financing high-MAE guard, and Green-cap repair", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-07-30", "evidence_available_at_that_date": "company release date had no machine-verified intraday timestamp in this run; use next stock-web tradable close", "evidence_source": "https://www.samsungsdi.com/sdi-now/sdi-news/3862.html", "stage2_evidence_fields": ["operating profit improved QoQ", "company retained battery profitability language"], "stage3_evidence_fields": ["YoY revenue and operating profit declined sharply; demand slowdown not solved"], "stage4b_evidence_fields": ["large 90D/180D drawdown after temporary MFE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-31", "entry_price": 319500.0, "MFE_30D_pct": 18.94, "MFE_90D_pct": 23.16, "MFE_180D_pct": 23.16, "MFE_1Y_pct": 23.16, "MFE_2Y_pct": null, "MAE_30D_pct": -7.82, "MAE_90D_pct": -26.29, "MAE_180D_pct": -46.79, "MAE_1Y_pct": -50.64, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "peak_date": "2024-09-30", "peak_price": 393500.0, "drawdown_after_peak_pct": -56.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b_overlay", "four_b_evidence_type": "non_price_required", "four_c_protection_label": null, "trigger_outcome_label": "counterexample_yellow_should_not_green_when_sequential_op_improves_but_cycle_decays", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|2024-07-30|sequential_operating_profit_improvement_inside_ev_demand_slowdown", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C13_L210_T004_006400_STAGE4C_20241030", "case_id": "C13_L210_CASE_04_SAMSUNG_SDI_Q3_DEMAND_SLOWDOWN_4C", "symbol": "006400", "company_name": "Samsung SDI / 삼성SDI", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "sector": "battery_cells_ess", "primary_archetype": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "loop_objective": "AMPC/IRA persistence, JV utilization failure, policy-financing high-MAE guard, and Green-cap repair", "trigger_type": "Stage4C", "trigger_date": "2024-10-30", "evidence_available_at_that_date": "company release date had no machine-verified intraday timestamp in this run; use next stock-web tradable close", "evidence_source": "https://www.samsungsdi.com/sdi-now/sdi-news/4082.html", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["reported demand slowdown and limited near-term improvement"], "stage4c_evidence_fields": ["YoY revenue down 30%", "operating profit down 72%", "180D MAE below -50%"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-31", "entry_price": 327000.0, "MFE_30D_pct": 4.28, "MFE_90D_pct": 4.28, "MFE_180D_pct": 4.28, "MFE_1Y_pct": 8.41, "MFE_2Y_pct": null, "MAE_30D_pct": -27.98, "MAE_90D_pct": -42.87, "MAE_180D_pct": -51.77, "MAE_1Y_pct": -51.77, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "peak_date": "2024-10-31", "peak_price": 341000.0, "drawdown_after_peak_pct": -53.75, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b_overlay", "four_b_evidence_type": "non_price_required", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_protection_success_demand_slowdown_confirmed", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|2024-10-30|revenue_operating_profit_collapse_and_demand_slowdown_hard_4c", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216", "case_id": "C13_L210_CASE_05_SKINNO_BLUEOVAL_POLICY_FINANCING_HIGH_MAE", "symbol": "096770", "company_name": "SK Innovation / SK이노베이션", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "sector": "battery_parent_and_energy", "primary_archetype": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "loop_objective": "AMPC/IRA persistence, JV utilization failure, policy-financing high-MAE guard, and Green-cap repair", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-12-16", "evidence_available_at_that_date": "U.S. DOE/Reuters event reached Korea after the Dec. 16 Korean close; use next stock-web tradable close", "evidence_source": "https://www.energy.gov/edf/articles/doe-announces-963-billion-loan-blueoval-sk-further-expand-us-manufacturing-electric ; https://www.reuters.com/business/autos-transportation/us-finalizes-963-billion-loan-ford-sk-joint-battery-venture-2024-12-16/", "stage2_evidence_fields": ["large DOE loan finalized", "JV capacity construction financing", "production expected later"], "stage3_evidence_fields": ["no realized utilization/profit bridge at trigger date"], "stage4b_evidence_fields": ["high-MAE guard after policy headline"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv", "profile_path": "atlas/symbol_profiles/096/096770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-17", "entry_price": 119200.0, "MFE_30D_pct": 10.07, "MFE_90D_pct": 17.62, "MFE_180D_pct": 17.62, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.72, "MAE_90D_pct": -22.99, "MAE_180D_pct": -32.21, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "peak_date": "2025-03-13", "peak_price": 140200.0, "drawdown_after_peak_pct": -42.37, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b_overlay", "four_b_evidence_type": "non_price_required", "four_c_protection_label": null, "trigger_outcome_label": "counterexample_policy_financing_not_utilization_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|096770|2024-12-16|jv_policy_financing_without_utilization_or_profit_conversion", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124", "case_id": "C13_L210_CASE_06_LGES_FY2024_CAPEX_DISCIPLINE_ESS_REPAIR", "symbol": "373220", "company_name": "LG Energy Solution / LG에너지솔루션", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "sector": "battery_cells", "primary_archetype": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "loop_objective": "AMPC/IRA persistence, JV utilization failure, policy-financing high-MAE guard, and Green-cap repair", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-24", "evidence_available_at_that_date": "company release date had no machine-verified intraday timestamp in this run and Korea holiday gap followed; use next available stock-web tradable close", "evidence_source": "https://news.lgensol.com/company-news/press-releases/3587/", "stage2_evidence_fields": ["2025 revenue guidance +5~10%", "capex reduction 20~30%", "explicit focus on volatility response and fundamental competitiveness"], "stage3_evidence_fields": ["do not Green immediately because 90D MAE remains large"], "stage4b_evidence_fields": ["high-MAE watch in first 90D"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-31", "entry_price": 352000.0, "MFE_30D_pct": 9.8, "MFE_90D_pct": 9.8, "MFE_180D_pct": 41.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.67, "MAE_90D_pct": -24.43, "MAE_180D_pct": -24.43, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "below_entry_price_flag_180D": true, "peak_date": "2025-10-27", "peak_price": 499500.0, "drawdown_after_peak_pct": -3.9, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b_overlay", "four_b_evidence_type": "non_price_required", "four_c_protection_label": null, "trigger_outcome_label": "positive_repair_after_capex_discipline_but_high_mae_yellow_cap", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|2025-01-24|capex_discipline_after_utilization_downcycle_and_forward_revenue_guidance", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13_L210_CASE_01_LGES_Q2_AMPC_VOLUME_UTILIZATION_BRIDGE", "trigger_id": "C13_L210_T001_373220_STAGE2_ACTIONABLE_20240725", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 45, "relative_strength_score": 70, "customer_quality_score": 70, "policy_or_regulatory_score": 78, "valuation_repricing_score": 52, "execution_risk_score": 40, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 72.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 62, "margin_bridge_score": 48, "revision_score": 52, "relative_strength_score": 76, "customer_quality_score": 74, "policy_or_regulatory_score": 86, "valuation_repricing_score": 56, "execution_risk_score": 42, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 80.5, "stage_label_after": "Stage3-Yellow", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "margin_bridge_score", "relative_strength_score"], "component_delta_explanation": "lift Stage2 to Yellow only when AMPC credit is paired with realized regional volume or shipments; do not promote to Green while ex-credit operating profit remains negative.", "MFE_90D_pct": 36.62, "MAE_90D_pct": -4.31, "score_return_alignment_label": "positive_when_ampc_credit_has_volume_bridge_but_green_capped_by_ex_credit_loss", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13_L210_CASE_02_LGES_Q3_AMPC_GREEN_TRAP", "trigger_id": "C13_L210_T002_373220_STAGE3_GREEN_20241028", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 72, "revision_score": 72, "relative_strength_score": 82, "customer_quality_score": 72, "policy_or_regulatory_score": 92, "valuation_repricing_score": 58, "execution_risk_score": 32, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 52, "backlog_visibility_score": 55, "margin_bridge_score": 38, "revision_score": 48, "relative_strength_score": 70, "customer_quality_score": 70, "policy_or_regulatory_score": 82, "valuation_repricing_score": 52, "execution_risk_score": 48, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8}, "weighted_score_after": 73.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "cap at Stage2-Actionable when AMPC/IRA credit flips reported OP but ex-credit profit is still negative and utilization is not demonstrably tightening.", "MFE_90D_pct": 6.48, "MAE_90D_pct": -19.93, "score_return_alignment_label": "counterexample_ampc_masked_green_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13_L210_CASE_03_SAMSUNG_SDI_Q2_SEQUENTIAL_OP_HIGH_MAE", "trigger_id": "C13_L210_T003_006400_STAGE3_YELLOW_20240730", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 66, "revision_score": 62, "relative_strength_score": 76, "customer_quality_score": 74, "policy_or_regulatory_score": 48, "valuation_repricing_score": 50, "execution_risk_score": 38, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 80.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 43, "backlog_visibility_score": 46, "margin_bridge_score": 50, "revision_score": 42, "relative_strength_score": 65, "customer_quality_score": 70, "policy_or_regulatory_score": 45, "valuation_repricing_score": 46, "execution_risk_score": 60, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["revision_score", "margin_bridge_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "when YoY revenue and profit are still falling, require order/utilization confirmation before allowing Yellow to become Green.", "MFE_90D_pct": 23.16, "MAE_90D_pct": -26.29, "score_return_alignment_label": "counterexample_yellow_should_not_green_when_sequential_op_improves_but_cycle_decays", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13_L210_CASE_04_SAMSUNG_SDI_Q3_DEMAND_SLOWDOWN_4C", "trigger_id": "C13_L210_T004_006400_STAGE4C_20241030", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 36, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 62, "policy_or_regulatory_score": 40, "valuation_repricing_score": 40, "execution_risk_score": 72, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 61.0, "stage_label_before": "Stage4B", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 30, "margin_bridge_score": 20, "revision_score": 18, "relative_strength_score": 32, "customer_quality_score": 58, "policy_or_regulatory_score": 38, "valuation_repricing_score": 35, "execution_risk_score": 88, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 42.0, "stage_label_after": "Stage4C", "changed_components": ["revision_score", "margin_bridge_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "route to hard 4C when demand slowdown is confirmed by revenue/profit collapse and 180D MAE confirms severe damage.", "MFE_90D_pct": 4.28, "MAE_90D_pct": -42.87, "score_return_alignment_label": "hard_4c_protection_success_demand_slowdown_confirmed", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13_L210_CASE_05_SKINNO_BLUEOVAL_POLICY_FINANCING_HIGH_MAE", "trigger_id": "C13_L210_T005_096770_STAGE2_ACTIONABLE_20241216", "symbol": "096770", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 52, "backlog_visibility_score": 58, "margin_bridge_score": 34, "revision_score": 42, "relative_strength_score": 66, "customer_quality_score": 68, "policy_or_regulatory_score": 92, "valuation_repricing_score": 54, "execution_risk_score": 52, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 8}, "weighted_score_before": 77.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 52, "margin_bridge_score": 25, "revision_score": 34, "relative_strength_score": 58, "customer_quality_score": 65, "policy_or_regulatory_score": 78, "valuation_repricing_score": 50, "execution_risk_score": 68, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 8}, "weighted_score_after": 65.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "execution_risk_score", "revision_score"], "component_delta_explanation": "score policy/JV financing as Stage2 bridge only; require production ramp, customer offtake, utilization, or ex-subsidy profit before Yellow/Green expansion.", "MFE_90D_pct": 17.62, "MAE_90D_pct": -22.99, "score_return_alignment_label": "counterexample_policy_financing_not_utilization_green", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13_L210_CASE_06_LGES_FY2024_CAPEX_DISCIPLINE_ESS_REPAIR", "trigger_id": "C13_L210_T006_373220_STAGE2_ACTIONABLE_20250124", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 54, "margin_bridge_score": 36, "revision_score": 48, "relative_strength_score": 62, "customer_quality_score": 72, "policy_or_regulatory_score": 70, "valuation_repricing_score": 50, "execution_risk_score": 55, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_before": 70.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 52, "backlog_visibility_score": 58, "margin_bridge_score": 42, "revision_score": 58, "relative_strength_score": 68, "customer_quality_score": 74, "policy_or_regulatory_score": 74, "valuation_repricing_score": 52, "execution_risk_score": 52, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5}, "weighted_score_after": 76.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["revision_score", "execution_risk_score", "policy_or_regulatory_score", "relative_strength_score"], "component_delta_explanation": "allow Yellow when capex discipline/revenue guidance appears after a downcycle, but require realized profit/utilization before Green.", "MFE_90D_pct": 9.8, "MAE_90D_pct": -24.43, "score_return_alignment_label": "positive_repair_after_capex_discipline_but_high_mae_yellow_cap", "current_profile_verdict": "current_profile_correct"}
```

### 25.5 aggregate row
```jsonl
{"row_type": "aggregate", "aggregate_id": "C13_LOOP210_AMPC_JV_UTILIZATION_SUMMARY", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "calibration_usable_case_count": 6, "positive_case_count": 2, "counterexample_count": 4, "new_symbol_count": 3, "new_trigger_family_count": 6, "mean_MFE_180D_positive_cases": 39.26, "mean_MAE_180D_counterexamples": -41.43, "residual_error_types_found": ["ampc_masked_green_false_positive", "policy_financing_without_utilization_false_positive", "demand_slowdown_hard4c_too_late", "positive_ampc_volume_bridge_missed_by_over_strict_filter"]}
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "210", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AMPC_IRA_JV_UTILIZATION_GREEN_TRAP_AND_POLICY_FINANCING_HIGH_MAE_GUARD", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["Stage2 bridge requirement", "Stage3-Green revision minimum", "full 4B non-price requirement", "hard 4C thesis-break routing", "price-only blowoff guard"], "residual_error_types_found": ["ampc_masked_green_false_positive", "policy_financing_without_utilization_false_positive", "demand_slowdown_hard4c_too_late", "positive_ampc_volume_bridge_missed_by_over_strict_filter"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "production_scoring_changed": false, "shadow_weight_only": true}
```

### 25.7 narrative_only row
```jsonl
{"row_type": "narrative_only", "case_id": "C13_L210_NARR_096770_SKON_Q2_LOSS_CORP_ACTION_BLOCKED", "symbol": "096770", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "reason": "SK Innovation 2024-08-02 Q2 battery-loss row was not used for quantitative weight calibration because 096770 profile contains a 2024-11-20 corporate-action candidate inside the D~D+180 window.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied `e2r_2_1_stock_web_calibrated` profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<symbol>.json`.

### Rules
1. Use only `calibration_usable=true` rows for quantitative calibration.
2. Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
3. Do not treat schema-rematerialization-only or duplicate low-value loops as new evidence.
4. Do not apply global deltas unless multiple large_sector_id values support the same direction.
5. Prefer sector-specific or canonical-archetype-specific shadow profiles.
6. Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
7. 4B rows are overlay/risk calibration only.
8. 4C rows are thesis-break/protection calibration only.
9. Price-only rows cannot promote Stage2/Stage3.
10. For C13 specifically, enforce the AMPC quality ladder and JV utilization freshness gate before Green promotion.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Any proposed shadow profile changes marked as non-production until explicit promotion.

## 27. Next Round State
```text
last_completed_round = R3
last_completed_loop = 210
last_completed_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
last_completed_canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C15_MATERIAL_SPREAD_SUPERCYCLE repair-only, C05/C01 only for URL/MFE missing-row repair; avoid immediate C13 repetition unless adding new direct utilization/offtake rows
do_not_repeat_exact_keys = C13|373220|Stage2-Actionable|2024-07-26; C13|373220|Stage3-Green|2024-10-29; C13|006400|Stage3-Yellow|2024-07-31; C13|006400|Stage4C|2024-10-31; C13|096770|Stage2-Actionable|2024-12-17; C13|373220|Stage2-Actionable|2025-01-31
```

## 28. Source Notes
- Main execution prompt: `https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat ledger: `https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md`.
- Stock-Web manifest: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json`.
- Stock-Web schema: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json`.
- External evidence URLs are listed in section 9 and repeated in machine-readable rows.
- This file is a historical calibration artifact only; it is not investment advice or a live signal.
