# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| research_file | `e2r_stock_web_v12_residual_round_R4_loop_73_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md` |
| generated_at_kst | `2026-06-16` |
| prompt_version | `E2R Historical Calibration Prompt v12 — Stock-Web OHLC Atlas / Sector-Archetype Residual Expansion / MD Handoff` |
| selected_round | `R4` |
| selected_loop | `73` |
| selection_basis | `docs/core/V12_Research_No_Repeat_Index.md` |
| selected_priority_bucket | `Priority 1 / C15 spread reversal + inventory-cycle counterexample quality reinforcement; Priority 0 URL/proxy/MFE-MAE repair compatible` |
| round_schedule_status | `coverage_index_selected; prior C15 loop 72 exact keys avoided; 직전 C05 loop 209 반복 회피` |
| round_sector_consistency | `pass` |
| large_sector_id | `L4_MATERIALS_SPREAD_RESOURCE` |
| canonical_archetype_id | `C15_MATERIAL_SPREAD_SUPERCYCLE` |
| fine_archetype_id | `C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD` |
| loop_objective | `counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test` |
| primary_price_source | `Songdaiki/stock-web` |
| stock_web_manifest_max_date | `2026-02-20` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| production_scoring_changed | `False` |
| shadow_weight_only | `True` |
| current_stock_discovery_allowed | `False` |
| stock_agent_code_accessed_or_patched | `False` |

This loop adds **6 new independent cases**, **3 counterexamples**, and **4 residual errors** for `R4/L4/C15`. The new contribution is the C15 inventory-lag/fresh-spread gate: a material-spread thesis is not the quoted metal price itself; it is the price after it walks through inventory, product pricing, demand, and cash conversion.

## 1. Current Calibrated Profile Assumption

Baseline proxy remains `e2r_2_1_stock_web_calibrated_proxy`: Stage2 bridge bonus, stricter Yellow/Green thresholds, price-only blowoff block, full-4B non-price requirement, and hard-4C thesis-break routing are treated as already applied. This loop does **not** re-prove those global axes; it tests whether C15 needs a more precise spread-freshness and inventory-lag ladder.

## 2. Round / Large Sector / Canonical Archetype Scope

| item | value |
|---|---|
| selected_round | `R4` |
| large_sector_id | `L4_MATERIALS_SPREAD_RESOURCE` |
| canonical_archetype_id | `C15_MATERIAL_SPREAD_SUPERCYCLE` |
| fine_archetype_id | `C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD` |
| scope verdict | `pass: C15 maps to R4 / L4_MATERIALS_SPREAD_RESOURCE` |

## 3. Previous Coverage / Duplicate Avoidance Check

- No-Repeat Index shows C01~C32 are all beyond the old 80-row floor; selection therefore targets quality repair, not raw row count.
- Priority 1 still lists C15 for spread reversal and inventory-cycle counterexample reinforcement.
- Immediate prior local C15 loop 72 keys were avoided: `084010 2021-01-12`, `104700 2021-01-12`, `104700 2024-05-16`, `005010 2023-04-14`.
- This file uses 5 symbols and 6 trigger families; the duplicate key `canonical_archetype_id + symbol + trigger_type + entry_date` is unique for every trigger row.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest/schema field | value |
|---|---|
| source_name | `FinanceData/marcap` |
| source_repo_url | `https://github.com/FinanceData/marcap` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| tradable columns | `d,o,h,l,c,v,a,mc,s,m` |
| manifest max_date | `2026-02-20` |
| tradable_row_count | `14,354,401` |
| raw_row_count | `15,214,118` |
| symbol_count | `5,414` |

## 5. Historical Eligibility Gate

| symbol | trigger_date | entry_date | entry close | forward window | corporate action window | calibration usable |
|---|---|---|---:|---:|---|---|
| `103140` | 2025-02-28 | 2025-03-04 | 59100 | 237 tradable rows available | clean_180D_window | true |
| `103140` | 2022-03-18 | 2022-03-21 | 32650 | 716 tradable rows available | clean_180D_window | true |
| `003030` | 2024-03-19 | 2024-03-20 | 234500 | 466 tradable rows available | clean_180D_window | true |
| `306200` | 2025-02-04 | 2025-02-05 | 144500 | 255 tradable rows available | clean_180D_window | true |
| `001430` | 2024-08-02 | 2024-08-05 | 17380 | 340 tradable rows available | clean_180D_window | true |
| `004560` | 2024-06-26 | 2024-06-27 | 16940 | 367 tradable rows available | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| C15 evidence fragment | Accepted read | Capped / rejected read |
|---|---|---|
| quoted copper/nickel/steel movement | Stage2 watch only unless inventory/demand bridge is clean | raw-material rebound alone as Actionable |
| record operating profit | confirms prior spread capture | Green if no forward spread freshness |
| realized margin + forward demand/offtake | Actionable/Yellow candidate | none |
| one-year margin collapse | 4B/watch first | hard 4C unless repeated non-price thesis damage |
| price reset after weak result | watch/guardrail path | automatic thesis death |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | role | trigger_family | current_profile_verdict |
|---|---|---|---|---|---|---|
| C15_L73_01_POONGSAN_2025_GUIDANCE_COPPER_DEFENSE_STAGE2A | `103140` | 풍산 / Poongsan | Stage2-Actionable | positive | forward_guidance_copper_defense_mix | current_profile_correct |
| C15_L73_02_POONGSAN_2022_RECORD_RESULT_COPPER_LATE_TRAP | `103140` | 풍산 / Poongsan | Stage3-Yellow | counterexample | record_result_after_spread_peak | current_profile_false_positive |
| C15_L73_03_SEAH_HOLDINGS_2024_RECORD_OCTG_STAGE3_GREEN_TRAP | `003030` | 세아제강지주 / SeAH Steel Holdings | Stage3-Green | counterexample | octg_record_profit_result_only | current_profile_false_positive |
| C15_L73_04_SEAH_STEEL_2025_PROFIT_DROP_LOCAL_4B_NOT_4C | `306200` | 세아제강 / SeAH Steel | Stage4B | positive_guardrail | profit_drop_after_oil_country_pipe_peak | current_profile_false_positive |
| C15_L73_05_SEAH_BESTEEL_2024_Q2_SPECIAL_STEEL_WEAKNESS_4B_WATCH | `001430` | 세아베스틸지주 / SeAH Besteel Holdings | Stage4B | positive_guardrail | special_steel_result_deterioration_after_price_reset | current_profile_correct |
| C15_L73_06_HYUNDAI_BNG_2024_NICKEL_LAGGING_TRAP_STAGE2_FALSE_POSITIVE | `004560` | 현대비앤지스틸 / Hyundai BNG Steel | Stage2-Actionable | counterexample | nickel_rebound_inventory_lag_false_recovery | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| bucket | count | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 |
|---|---:|---:|---:|---:|---:|
| positive + guardrail-positive | 3 | 83.21% | -9.77% | 96.01% | -16.05% |
| counterexample | 3 | 4.38% | -26.5% | 4.38% | -36.41% |

## 9. Evidence Source Map

| trigger_id | evidence_source | evidence summary |
|---|---|---|
| C15_R4L73_T001_103140_2025-03-04_Stage2Actionable | `https://money2.daishin.com/m_file/file/271/52839_Daishin%20Securities_Poongsan%20%28103140%20KS%20Mar%204%2C%202025%29.pdf` | Daishin Securities는 2025년 매출 목표 3.8조원, 신동 2.54조원, 방산 1.26조원, 세전이익 2,800억원 가이던스를 제시했다. |
| C15_R4L73_T002_103140_2022-03-21_Stage3Yellow | `https://securities.miraeasset.com/bbs/download/2091868.pdf?attachmentId=2091868` | Mirae Asset 리포트는 2021년 매출 3.5조원(+35.3%), 영업이익 3,141억원(+159.2%)의 사상 최대 실적과 2022년 구리 가격 우호 전망을 제시했다. |
| C15_R4L73_T003_003030_2024-03-20_Stage3Green | `https://eng.snmnews.com/news/articleView.html?idxno=270840` | Steel & Metal News는 SeAH Steel Holdings의 2023년 매출 3.913조원, 영업이익 5,909억원(+4.2%) 사상 최대 영업이익 달성을 보도했다. |
| C15_R4L73_T004_306200_2025-02-05_Stage4B | `https://biz.chosun.com/en/en-industry/2025/02/04/F3CFGXGESVAGBEJHZATA5LAGL4/` | Chosun Biz는 SeAH Steel의 2024년 영업이익 2,251억원(-61.9%), 매출 -5.7%를 보도했다. |
| C15_R4L73_T005_001430_2024-08-05_Stage4B | `https://alphabiz.co.kr/news/print.html?newsid=110270` | AlphaBiz는 SeAH Besteel Holdings의 2024년 2분기 영업이익 645억원(-21.5%), 매출 9,700억원(-12.4%)을 보도했다. |
| C15_R4L73_T006_004560_2024-06-27_Stage2Actionable | `https://m.kisrating.com/fileDown.do?fileName=rs20240626-2.pdf&gubun=2&menuCd=R8 / https://m.kisrating.com/fileDown.do?fileName=rs20250217-1.pdf&gubun=2&menuCd=R8` | KIS Rating은 1Q24 영업손실과 함께 니켈 가격 반등이 가격 인상에 우호적일 수 있으나 수입재·공급부담·가격 하락 압력이 지속된다고 평가했다. |

## 10. Price Data Source Map

| trigger_id | price_shard_path | profile_path | entry row OHLCV |
|---|---|---|---|
| C15_R4L73_T001_103140_2025-03-04_Stage2Actionable | `atlas/ohlcv_tradable_by_symbol_year/103/103140/<year>.csv` | `atlas/symbol_profiles/103/103140.json` | o=56000, h=59500, l=55900, c=59100, v=761197, a=44344972900, mc=1656234829800, s=28024278, m=KOSPI |
| C15_R4L73_T002_103140_2022-03-21_Stage3Yellow | `atlas/ohlcv_tradable_by_symbol_year/103/103140/<year>.csv` | `atlas/symbol_profiles/103/103140.json` | o=32550, h=32750, l=32250, c=32650, v=154360, a=5023778850, mc=914992676700, s=28024278, m=KOSPI |
| C15_R4L73_T003_003030_2024-03-20_Stage3Green | `atlas/ohlcv_tradable_by_symbol_year/003/003030/<year>.csv` | `atlas/symbol_profiles/003/003030.json` | o=230500, h=234500, l=225500, c=234500, v=11639, a=2712947000, mc=971218566500, s=4141657, m=KOSPI |
| C15_R4L73_T004_306200_2025-02-05_Stage4B | `atlas/ohlcv_tradable_by_symbol_year/306/306200/<year>.csv` | `atlas/symbol_profiles/306/306200.json` | o=142100, h=153500, l=138600, c=144500, v=108861, a=15841624100, mc=409845350000, s=2836300, m=KOSPI |
| C15_R4L73_T005_001430_2024-08-05_Stage4B | `atlas/ohlcv_tradable_by_symbol_year/001/001430/<year>.csv` | `atlas/symbol_profiles/001/001430.json` | o=19190, h=19430, l=16640, c=17380, v=205537, a=3712958750, mc=623283628220, s=35862119, m=KOSPI |
| C15_R4L73_T006_004560_2024-06-27_Stage2Actionable | `atlas/ohlcv_tradable_by_symbol_year/004/004560/<year>.csv` | `atlas/symbol_profiles/004/004560.json` | o=16760, h=17230, l=16430, c=16940, v=143518, a=2422160540, mc=255435058340, s=15078811, m=KOSPI |

## 11. Case-by-Case Trigger Grid

### 11.1. C15_L73_01_POONGSAN_2025_GUIDANCE_COPPER_DEFENSE_STAGE2A

- **Symbol/company:** `103140` — 풍산 / Poongsan
- **Trigger / entry:** 2025-02-28 → 2025-03-04 at close `59100`
- **Trigger type:** `Stage2-Actionable`; outcome label `positive_structural_success_forward_spread_and_demand_bridge`
- **Evidence:** Daishin Securities는 2025년 매출 목표 3.8조원, 신동 2.54조원, 방산 1.26조원, 세전이익 2,800억원 가이던스를 제시했다.
- **MFE/MAE:** MFE30/90/180 `19.8 / 152.96 / 191.37`; MAE30/90/180 `-15.57 / -15.57 / -15.57`
- **Mechanism:** Forward-looking spread plus defense demand bridge; not merely a prior result headline.

### 11.2. C15_L73_02_POONGSAN_2022_RECORD_RESULT_COPPER_LATE_TRAP

- **Symbol/company:** `103140` — 풍산 / Poongsan
- **Trigger / entry:** 2022-03-18 → 2022-03-21 at close `32650`
- **Trigger type:** `Stage3-Yellow`; outcome label `counterexample_result_only_green_trap`
- **Evidence:** Mirae Asset 리포트는 2021년 매출 3.5조원(+35.3%), 영업이익 3,141억원(+159.2%)의 사상 최대 실적과 2022년 구리 가격 우호 전망을 제시했다.
- **MFE/MAE:** MFE30/90/180 `3.98 / 3.98 / 3.98`; MAE30/90/180 `-4.59 / -28.64 / -28.64`
- **Mechanism:** Result quality is real, but it is a rear-view mirror; spread freshness and price phase are missing.

### 11.3. C15_L73_03_SEAH_HOLDINGS_2024_RECORD_OCTG_STAGE3_GREEN_TRAP

- **Symbol/company:** `003030` — 세아제강지주 / SeAH Steel Holdings
- **Trigger / entry:** 2024-03-19 → 2024-03-20 at close `234500`
- **Trigger type:** `Stage3-Green`; outcome label `counterexample_result_only_green_trap`
- **Evidence:** Steel & Metal News는 SeAH Steel Holdings의 2023년 매출 3.913조원, 영업이익 5,909억원(+4.2%) 사상 최대 영업이익 달성을 보도했다.
- **MFE/MAE:** MFE30/90/180 `2.56 / 2.56 / 2.56`; MAE30/90/180 `-12.15 / -22.77 / -38.98`
- **Mechanism:** Record profit validates history, not the next spread cycle.

### 11.4. C15_L73_04_SEAH_STEEL_2025_PROFIT_DROP_LOCAL_4B_NOT_4C

- **Symbol/company:** `306200` — 세아제강 / SeAH Steel
- **Trigger / entry:** 2025-02-04 → 2025-02-05 at close `144500`
- **Trigger type:** `Stage4B`; outcome label `guardrail_positive_4b_watch_not_thesis_death`
- **Evidence:** Chosun Biz는 SeAH Steel의 2024년 영업이익 2,251억원(-61.9%), 매출 -5.7%를 보도했다.
- **MFE/MAE:** MFE30/90/180 `50.52 / 50.52 / 50.52`; MAE30/90/180 `-9.48 / -9.48 / -17.44`
- **Mechanism:** A margin collapse is a siren, not yet proof that the bridge has burned down.

### 11.5. C15_L73_05_SEAH_BESTEEL_2024_Q2_SPECIAL_STEEL_WEAKNESS_4B_WATCH

- **Symbol/company:** `001430` — 세아베스틸지주 / SeAH Besteel Holdings
- **Trigger / entry:** 2024-08-02 → 2024-08-05 at close `17380`
- **Trigger type:** `Stage4B`; outcome label `guardrail_positive_4b_watch_not_thesis_death`
- **Evidence:** AlphaBiz는 SeAH Besteel Holdings의 2024년 2분기 영업이익 645억원(-21.5%), 매출 9,700억원(-12.4%)을 보도했다.
- **MFE/MAE:** MFE30/90/180 `16.8 / 46.14 / 46.14`; MAE30/90/180 `-4.26 / -4.26 / -15.13`
- **Mechanism:** The bad result arrived after a price reset; that is a watch state, not automatic death.

### 11.6. C15_L73_06_HYUNDAI_BNG_2024_NICKEL_LAGGING_TRAP_STAGE2_FALSE_POSITIVE

- **Symbol/company:** `004560` — 현대비앤지스틸 / Hyundai BNG Steel
- **Trigger / entry:** 2024-06-26 → 2024-06-27 at close `16940`
- **Trigger type:** `Stage2-Actionable`; outcome label `counterexample_inventory_lag_false_positive`
- **Evidence:** KIS Rating은 1Q24 영업손실과 함께 니켈 가격 반등이 가격 인상에 우호적일 수 있으나 수입재·공급부담·가격 하락 압력이 지속된다고 평가했다.
- **MFE/MAE:** MFE30/90/180 `6.61 / 6.61 / 6.61`; MAE30/90/180 `-27.98 / -28.1 / -41.62`
- **Mechanism:** Raw-material rebound can be trapped inside the inventory conveyor belt before it reaches earnings.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C15_R4L73_T001_103140_2025-03-04_Stage2Actionable | 2025-03-04 | 59100 | 19.8% | -15.57% | 152.96% | -15.57% | 191.37% | -15.57% | 2025-07-30 | 172200 | -46.92% |
| C15_R4L73_T002_103140_2022-03-21_Stage3Yellow | 2022-03-21 | 32650 | 3.98% | -4.59% | 3.98% | -28.64% | 3.98% | -28.64% | 2022-03-24 | 33950 | -31.37% |
| C15_R4L73_T003_003030_2024-03-20_Stage3Green | 2024-03-20 | 234500 | 2.56% | -12.15% | 2.56% | -22.77% | 2.56% | -38.98% | 2024-03-27 | 240500 | -40.5% |
| C15_R4L73_T004_306200_2025-02-05_Stage4B | 2025-02-05 | 144500 | 50.52% | -9.48% | 50.52% | -9.48% | 50.52% | -17.44% | 2025-03-06 | 217500 | -45.15% |
| C15_R4L73_T005_001430_2024-08-05_Stage4B | 2024-08-05 | 17380 | 16.8% | -4.26% | 46.14% | -4.26% | 46.14% | -15.13% | 2024-11-12 | 25400 | -41.93% |
| C15_R4L73_T006_004560_2024-06-27_Stage2Actionable | 2024-06-27 | 16940 | 6.61% | -27.98% | 6.61% | -28.1% | 6.61% | -41.62% | 2024-07-17 | 18060 | -45.24% |

## 13. Current Calibrated Profile Stress Test

| trigger_id | profile read before | actual path | verdict |
|---|---|---|---|
| C15_R4L73_T001_103140_2025-03-04_Stage2Actionable | score_before=78.0 stage_before=Stage3-Yellow | MFE180=191.37%, MAE180=-15.57% | current_profile_correct |
| C15_R4L73_T002_103140_2022-03-21_Stage3Yellow | score_before=88.0 stage_before=Stage3-Green | MFE180=3.98%, MAE180=-28.64% | current_profile_false_positive |
| C15_R4L73_T003_003030_2024-03-20_Stage3Green | score_before=89.0 stage_before=Stage3-Green | MFE180=2.56%, MAE180=-38.98% | current_profile_false_positive |
| C15_R4L73_T004_306200_2025-02-05_Stage4B | score_before=42.0 stage_before=Stage4C | MFE180=50.52%, MAE180=-17.44% | current_profile_false_positive |
| C15_R4L73_T005_001430_2024-08-05_Stage4B | score_before=54.0 stage_before=Stage4B | MFE180=46.14%, MAE180=-15.13% | current_profile_correct |
| C15_R4L73_T006_004560_2024-06-27_Stage2Actionable | score_before=77.0 stage_before=Stage3-Yellow | MFE180=6.61%, MAE180=-41.62% | current_profile_false_positive |

Stress result: current global rules are directionally useful but still over-trust C15 record-result rows. Record profit is a photograph; C15 needs a weather report. The model should ask whether the next spread, inventory cost, demand bridge, and cash conversion are still alive.

## 14. Stage2 / Yellow / Green Comparison

| stage bucket | included rows | interpretation |
|---|---|---|
| Stage2-Actionable | Poongsan 2025, Hyundai BNG 2024 | Same label splits: Poongsan had forward demand/spread bridge; Hyundai BNG had raw-material rebound but negative inventory/supply bridge. |
| Stage3-Yellow/Green | Poongsan 2022, SeAH Holdings 2024 | Both are result-heavy and late; Green should be capped unless forward spread/cash bridge appears. |
| Stage4B | SeAH Steel 2025, SeAH Besteel 2024 | Bad result should often be 4B/watch first, not hard 4C, when price has reset and later MFE remains large. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | 4B evidence type | local proximity proxy | full-window proximity proxy | verdict |
|---|---|---:|---:|---|
| C15_R4L73_T004_306200_2025-02-05_Stage4B | margin_or_backlog_slowdown+explicit_event_cap | 0.6644 | 0.6644 | local_4b_watch_not_hard_4c_without_repeated_thesis_break |
| C15_R4L73_T005_001430_2024-08-05_Stage4B | margin_or_backlog_slowdown+explicit_event_cap | 0.6843 | 0.6843 | local_4b_watch_not_hard_4c_without_repeated_thesis_break |

## 16. 4C Protection Audit

| trigger_id | 4C protection label | note |
|---|---|---|
| C15_R4L73_T004_306200_2025-02-05_Stage4B | false_break_do_not_route_single_year_margin_drop_to_hard_4c | A margin collapse is a siren, not yet proof that the bridge has burned down. |
| C15_R4L73_T005_001430_2024-08-05_Stage4B | not_applicable_no_stage4c | The bad result arrived after a price reset; that is a watch state, not automatic death. |

## 17. Sector-Specific Rule Candidate

L4 material-spread evidence should split quoted raw-material movement, inventory-cost lag, demand/offtake bridge, and result timing. Price/spread headlines can open Stage2 only when inventory lag and demand bridge are not negative; Stage3-Green requires realized margin/cash conversion or forward spread freshness.

## 18. Canonical-Archetype Rule Candidate

C15 needs a spread-freshness and inventory-lag ladder: raw material/spread headline -> Stage2-watch; forward spread plus demand/offtake bridge -> Stage2-Actionable; fresh margin/cash conversion -> Yellow/Green; record result after spread peak -> cap below Green/local 4B; margin collapse from inventory lag/demand reversal -> 4B or hard 4C only after repeated non-price thesis damage.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible selected rows | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | 6 | 43.8% | -18.14% | 50.2% | -26.23% | 0.67 | mixed; record-result traps remain |
| P1_L4_spread_freshness_inventory_gate | sector_specific | 3 | 83.21% | -9.77% | 96.01% | -16.05% | 0.0 | keeps bridge/4B-watch rows, demotes traps |
| P2_C15_forward_spread_cash_ladder | canonical_archetype_specific | 1 | 152.96% | -15.57% | 191.37% | -15.57% | 0.0 | strict but may miss reset-zone 4B guardrails |
| P3_C15_4b_not_4c_margin_collapse_guard | counterexample_guard | 2 | 48.33% | -6.87% | 48.33% | -16.29% | 0.0 | prevents hard-4C overkill after one bad result |

## 20. Score-Return Alignment Matrix

| trigger_id | score before | stage before | score after | stage after | component delta explanation |
|---|---:|---|---:|---|---|
| C15_R4L73_T001_103140_2025-03-04_Stage2Actionable | 78.0 | Stage3-Yellow | 84.0 | Stage3-Yellow | preserve positive because forward spread and demand bridge are visible |
| C15_R4L73_T002_103140_2022-03-21_Stage3Yellow | 88.0 | Stage3-Green | 73.0 | Stage2-Actionable | demote because result-only/raw-material signal lacks forward spread, inventory-lag, demand, or cash bridge |
| C15_R4L73_T003_003030_2024-03-20_Stage3Green | 89.0 | Stage3-Green | 72.0 | Stage2-Actionable | demote because result-only/raw-material signal lacks forward spread, inventory-lag, demand, or cash bridge |
| C15_R4L73_T004_306200_2025-02-05_Stage4B | 42.0 | Stage4C | 57.0 | Stage2 | keep as 4B/watch guardrail; avoid hard 4C without repeated non-price thesis break |
| C15_R4L73_T005_001430_2024-08-05_Stage4B | 54.0 | Stage4B | 59.0 | Stage2 | keep as 4B/watch guardrail; avoid hard 4C without repeated non-price thesis break |
| C15_R4L73_T006_004560_2024-06-27_Stage2Actionable | 77.0 | Stage3-Yellow | 61.0 | Stage2 | demote because result-only/raw-material signal lacks forward spread, inventory-lag, demand, or cash bridge |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD | 3 | 3 | 2 | 0 | 6 | 0 | 6 | 4 | 4 | c15_spread_freshness_inventory_lag_guard | c15_result_only_green_trap_cap | Quality gap reduced: added direct URL + complete MFE/MAE rows for spread reversal/inventory lag and 4B-not-4C timing. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_required_bridge; stage3_green_revision_min; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: result_only_green_trap; inventory_lag_false_positive; hard4c_too_early_after_single_year_margin_drop
new_axis_proposed: c15_spread_freshness_inventory_lag_guard; c15_result_only_green_trap_cap; c15_4b_not_4c_margin_collapse_gate
existing_axis_strengthened: stage2_required_bridge; stage3_green_revision_min_by_forward_spread_and_cash_conversion; local_4b_watch_guard
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_qualified_for_single_year_margin_drop
sector_specific_rule_candidate: L4 material-spread evidence should split quoted raw-material movement, inventory-cost lag, demand/offtake bridge, and result timing. Price/spread headlines can open Stage2 only when inventory lag and demand bridge are not negative; Stage3-Green requires realized margin/cash conversion or forward spread freshness.
canonical_archetype_rule_candidate: C15 needs a spread-freshness and inventory-lag ladder: raw material/spread headline -> Stage2-watch; forward spread plus demand/offtake bridge -> Stage2-Actionable; fresh margin/cash conversion -> Yellow/Green; record result after spread peak -> cap below Green/local 4B; margin collapse from inventory lag/demand reversal -> 4B or hard 4C only after repeated non-price thesis damage.
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger dates, Stock-Web tradable entry rows, 30D/90D/180D MFE/MAE, 180D forward-window availability, selected corporate-action screen, direct evidence URLs, and v12 row-field completeness. Not validated: live/current attractiveness, brokerage execution, production scoring change, or any `stock_agent` source-code behavior.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_spread_freshness_inventory_lag_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Require forward spread/demand/inventory bridge before Green","Demotes three counterexamples whose avg MFE180 is 4.38% and avg MAE180 is -36.41%","C15_R4L73_T002_103140_2022-03-21_Stage3Yellow|C15_R4L73_T003_003030_2024-03-20_Stage3Green|C15_R4L73_T006_004560_2024-06-27_Stage2Actionable",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c15_4b_not_4c_margin_collapse_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Single-year margin collapse routes to 4B/watch before hard 4C","Preserves two guardrail positives with avg MFE180 48.33%","C15_R4L73_T004_306200_2025-02-05_Stage4B|C15_R4L73_T005_001430_2024-08-05_Stage4B",2,2,0,medium,guardrail_shadow_only,"qualifies hard_4c routing, not a global rollback"
```

## 25. Machine-Readable Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "C15_R4L73_T001_103140_2025-03-04_Stage2Actionable", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_01_POONGSAN_2025_GUIDANCE_COPPER_DEFENSE_STAGE2A", "case_type": "positive", "company_name": "풍산 / Poongsan", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "notes": "Forward-looking spread plus defense demand bridge; not merely a prior result headline.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R4", "row_type": "case", "score_price_alignment": "positive_structural_success_forward_spread_and_demand_bridge", "symbol": "103140"}
{"best_trigger": "C15_R4L73_T002_103140_2022-03-21_Stage3Yellow", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_02_POONGSAN_2022_RECORD_RESULT_COPPER_LATE_TRAP", "case_type": "counterexample", "company_name": "풍산 / Poongsan", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "notes": "Result quality is real, but it is a rear-view mirror; spread freshness and price phase are missing.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R4", "row_type": "case", "score_price_alignment": "counterexample_result_only_green_trap", "symbol": "103140"}
{"best_trigger": "C15_R4L73_T003_003030_2024-03-20_Stage3Green", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_03_SEAH_HOLDINGS_2024_RECORD_OCTG_STAGE3_GREEN_TRAP", "case_type": "counterexample", "company_name": "세아제강지주 / SeAH Steel Holdings", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "notes": "Record profit validates history, not the next spread cycle.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R4", "row_type": "case", "score_price_alignment": "counterexample_result_only_green_trap", "symbol": "003030"}
{"best_trigger": "C15_R4L73_T004_306200_2025-02-05_Stage4B", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_04_SEAH_STEEL_2025_PROFIT_DROP_LOCAL_4B_NOT_4C", "case_type": "positive_guardrail", "company_name": "세아제강 / SeAH Steel", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "notes": "A margin collapse is a siren, not yet proof that the bridge has burned down.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R4", "row_type": "case", "score_price_alignment": "guardrail_positive_4b_watch_not_thesis_death", "symbol": "306200"}
{"best_trigger": "C15_R4L73_T005_001430_2024-08-05_Stage4B", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_05_SEAH_BESTEEL_2024_Q2_SPECIAL_STEEL_WEAKNESS_4B_WATCH", "case_type": "positive_guardrail", "company_name": "세아베스틸지주 / SeAH Besteel Holdings", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "notes": "The bad result arrived after a price reset; that is a watch state, not automatic death.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R4", "row_type": "case", "score_price_alignment": "guardrail_positive_4b_watch_not_thesis_death", "symbol": "001430"}
{"best_trigger": "C15_R4L73_T006_004560_2024-06-27_Stage2Actionable", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_06_HYUNDAI_BNG_2024_NICKEL_LAGGING_TRAP_STAGE2_FALSE_POSITIVE", "case_type": "counterexample", "company_name": "현대비앤지스틸 / Hyundai BNG Steel", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "notes": "Raw-material rebound can be trapped inside the inventory conveyor belt before it reaches earnings.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R4", "row_type": "case", "score_price_alignment": "counterexample_inventory_lag_false_positive", "symbol": "004560"}
{"MAE_180D_pct": -15.57, "MAE_1Y_pct": null, "MAE_30D_pct": -15.57, "MAE_90D_pct": -15.57, "MFE_180D_pct": 191.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 19.8, "MFE_90D_pct": 152.96, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_01_POONGSAN_2025_GUIDANCE_COPPER_DEFENSE_STAGE2A", "company_name": "풍산 / Poongsan", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.92, "entry_date": "2025-03-04", "entry_ohlc": {"a": 44344972900, "c": 59100.0, "h": 59500.0, "l": 55900.0, "m": "KOSPI", "mc": 1656234829800, "o": 56000.0, "s": 28024278, "v": 761197}, "entry_price": 59100.0, "evidence_available_at_that_date": "Daishin Securities는 2025년 매출 목표 3.8조원, 신동 2.54조원, 방산 1.26조원, 세전이익 2,800억원 가이던스를 제시했다.", "evidence_source": "https://money2.daishin.com/m_file/file/271/52839_Daishin%20Securities_Poongsan%20%28103140%20KS%20Mar%204%2C%202025%29.pdf", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "forward_window_trading_days": 237, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4b_trigger", "four_c_protection_label": "not_applicable_no_stage4c", "green_lateness_ratio": null, "green_lateness_reason": "no_paired_stage2_actionable_trigger_in_same_case", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "loop_objective": "counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "peak_date": "2025-07-30", "peak_price": 172200.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/<year>.csv", "primary_archetype": "material spread supercycle with inventory lag", "profile_path": "atlas/symbol_profiles/103/103140.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15_R4L73_103140_2025-03-04", "sector": "Materials / steel / copper / spread-cycle", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "customer_or_order_quality", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "103140", "trigger_date": "2025-02-28", "trigger_id": "C15_R4L73_T001_103140_2025-03-04_Stage2Actionable", "trigger_outcome_label": "positive_structural_success_forward_spread_and_demand_bridge", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -28.64, "MAE_1Y_pct": null, "MAE_30D_pct": -4.59, "MAE_90D_pct": -28.64, "MFE_180D_pct": 3.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 3.98, "MFE_90D_pct": 3.98, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_02_POONGSAN_2022_RECORD_RESULT_COPPER_LATE_TRAP", "company_name": "풍산 / Poongsan", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.37, "entry_date": "2022-03-21", "entry_ohlc": {"a": 5023778850, "c": 32650.0, "h": 32750.0, "l": 32250.0, "m": "KOSPI", "mc": 914992676700, "o": 32550.0, "s": 28024278, "v": 154360}, "entry_price": 32650.0, "evidence_available_at_that_date": "Mirae Asset 리포트는 2021년 매출 3.5조원(+35.3%), 영업이익 3,141억원(+159.2%)의 사상 최대 실적과 2022년 구리 가격 우호 전망을 제시했다.", "evidence_source": "https://securities.miraeasset.com/bbs/download/2091868.pdf?attachmentId=2091868", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "forward_window_trading_days": 716, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4b_trigger", "four_c_protection_label": "not_applicable_no_stage4c", "green_lateness_ratio": null, "green_lateness_reason": "no_paired_stage2_actionable_trigger_in_same_case", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "loop_objective": "counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "peak_date": "2022-03-24", "peak_price": 33950.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/<year>.csv", "primary_archetype": "material spread supercycle with inventory lag", "profile_path": "atlas/symbol_profiles/103/103140.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15_R4L73_103140_2022-03-21", "sector": "Materials / steel / copper / spread-cycle", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "103140", "trigger_date": "2022-03-18", "trigger_id": "C15_R4L73_T002_103140_2022-03-21_Stage3Yellow", "trigger_outcome_label": "counterexample_result_only_green_trap", "trigger_type": "Stage3-Yellow"}
{"MAE_180D_pct": -38.98, "MAE_1Y_pct": null, "MAE_30D_pct": -12.15, "MAE_90D_pct": -22.77, "MFE_180D_pct": 2.56, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 2.56, "MFE_90D_pct": 2.56, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_03_SEAH_HOLDINGS_2024_RECORD_OCTG_STAGE3_GREEN_TRAP", "company_name": "세아제강지주 / SeAH Steel Holdings", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.5, "entry_date": "2024-03-20", "entry_ohlc": {"a": 2712947000, "c": 234500.0, "h": 234500.0, "l": 225500.0, "m": "KOSPI", "mc": 971218566500, "o": 230500.0, "s": 4141657, "v": 11639}, "entry_price": 234500.0, "evidence_available_at_that_date": "Steel & Metal News는 SeAH Steel Holdings의 2023년 매출 3.913조원, 영업이익 5,909억원(+4.2%) 사상 최대 영업이익 달성을 보도했다.", "evidence_source": "https://eng.snmnews.com/news/articleView.html?idxno=270840", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "forward_window_trading_days": 466, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4b_trigger", "four_c_protection_label": "not_applicable_no_stage4c", "green_lateness_ratio": null, "green_lateness_reason": "no_paired_stage2_actionable_trigger_in_same_case", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "loop_objective": "counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "peak_date": "2024-03-27", "peak_price": 240500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003030/<year>.csv", "primary_archetype": "material spread supercycle with inventory lag", "profile_path": "atlas/symbol_profiles/003/003030.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15_R4L73_003030_2024-03-20", "sector": "Materials / steel / copper / spread-cycle", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "003030", "trigger_date": "2024-03-19", "trigger_id": "C15_R4L73_T003_003030_2024-03-20_Stage3Green", "trigger_outcome_label": "counterexample_result_only_green_trap", "trigger_type": "Stage3-Green"}
{"MAE_180D_pct": -17.44, "MAE_1Y_pct": null, "MAE_30D_pct": -9.48, "MAE_90D_pct": -9.48, "MFE_180D_pct": 50.52, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 50.52, "MFE_90D_pct": 50.52, "aggregate_group_role": "4B_overlay_only", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_04_SEAH_STEEL_2025_PROFIT_DROP_LOCAL_4B_NOT_4C", "company_name": "세아제강 / SeAH Steel", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": false, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.15, "entry_date": "2025-02-05", "entry_ohlc": {"a": 15841624100, "c": 144500.0, "h": 153500.0, "l": 138600.0, "m": "KOSPI", "mc": 409845350000, "o": 142100.0, "s": 2836300, "v": 108861}, "entry_price": 144500.0, "evidence_available_at_that_date": "Chosun Biz는 SeAH Steel의 2024년 영업이익 2,251억원(-61.9%), 매출 -5.7%를 보도했다.", "evidence_source": "https://biz.chosun.com/en/en-industry/2025/02/04/F3CFGXGESVAGBEJHZATA5LAGL4/", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "forward_window_trading_days": 255, "four_b_evidence_type": ["margin_or_backlog_slowdown", "explicit_event_cap"], "four_b_full_window_peak_proximity": 0.6644, "four_b_local_peak_proximity": 0.6644, "four_b_timing_verdict": "local_4b_watch_not_hard_4c_without_repeated_thesis_break", "four_c_protection_label": "false_break_do_not_route_single_year_margin_drop_to_hard_4c", "green_lateness_ratio": null, "green_lateness_reason": "no_paired_stage2_actionable_trigger_in_same_case", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "loop_objective": "counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "peak_date": "2025-03-06", "peak_price": 217500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/306/306200/<year>.csv", "primary_archetype": "material spread supercycle with inventory lag", "profile_path": "atlas/symbol_profiles/306/306200.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15_R4L73_306200_2025-02-05", "sector": "Materials / steel / copper / spread-cycle", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "306200", "trigger_date": "2025-02-04", "trigger_id": "C15_R4L73_T004_306200_2025-02-05_Stage4B", "trigger_outcome_label": "guardrail_positive_4b_watch_not_thesis_death", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -15.13, "MAE_1Y_pct": null, "MAE_30D_pct": -4.26, "MAE_90D_pct": -4.26, "MFE_180D_pct": 46.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 16.8, "MFE_90D_pct": 46.14, "aggregate_group_role": "4B_overlay_only", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_05_SEAH_BESTEEL_2024_Q2_SPECIAL_STEEL_WEAKNESS_4B_WATCH", "company_name": "세아베스틸지주 / SeAH Besteel Holdings", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": false, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.93, "entry_date": "2024-08-05", "entry_ohlc": {"a": 3712958750, "c": 17380.0, "h": 19430.0, "l": 16640.0, "m": "KOSPI", "mc": 623283628220, "o": 19190.0, "s": 35862119, "v": 205537}, "entry_price": 17380.0, "evidence_available_at_that_date": "AlphaBiz는 SeAH Besteel Holdings의 2024년 2분기 영업이익 645억원(-21.5%), 매출 9,700억원(-12.4%)을 보도했다.", "evidence_source": "https://alphabiz.co.kr/news/print.html?newsid=110270", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "forward_window_trading_days": 340, "four_b_evidence_type": ["margin_or_backlog_slowdown", "explicit_event_cap"], "four_b_full_window_peak_proximity": 0.6843, "four_b_local_peak_proximity": 0.6843, "four_b_timing_verdict": "local_4b_watch_not_hard_4c_without_repeated_thesis_break", "four_c_protection_label": "not_applicable_no_stage4c", "green_lateness_ratio": null, "green_lateness_reason": "no_paired_stage2_actionable_trigger_in_same_case", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "loop_objective": "counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "peak_date": "2024-11-12", "peak_price": 25400.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001430/<year>.csv", "primary_archetype": "material spread supercycle with inventory lag", "profile_path": "atlas/symbol_profiles/001/001430.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15_R4L73_001430_2024-08-05", "sector": "Materials / steel / copper / spread-cycle", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "001430", "trigger_date": "2024-08-02", "trigger_id": "C15_R4L73_T005_001430_2024-08-05_Stage4B", "trigger_outcome_label": "guardrail_positive_4b_watch_not_thesis_death", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -41.62, "MAE_1Y_pct": null, "MAE_30D_pct": -27.98, "MAE_90D_pct": -28.1, "MFE_180D_pct": 6.61, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 6.61, "MFE_90D_pct": 6.61, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_06_HYUNDAI_BNG_2024_NICKEL_LAGGING_TRAP_STAGE2_FALSE_POSITIVE", "company_name": "현대비앤지스틸 / Hyundai BNG Steel", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.24, "entry_date": "2024-06-27", "entry_ohlc": {"a": 2422160540, "c": 16940.0, "h": 17230.0, "l": 16430.0, "m": "KOSPI", "mc": 255435058340, "o": 16760.0, "s": 15078811, "v": 143518}, "entry_price": 16940.0, "evidence_available_at_that_date": "KIS Rating은 1Q24 영업손실과 함께 니켈 가격 반등이 가격 인상에 우호적일 수 있으나 수입재·공급부담·가격 하락 압력이 지속된다고 평가했다.", "evidence_source": "https://m.kisrating.com/fileDown.do?fileName=rs20240626-2.pdf&gubun=2&menuCd=R8", "fine_archetype_id": "C15_SPREAD_REVERSAL_INVENTORY_LAG_RESULT_TIMING_GUARD", "forward_window_trading_days": 367, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4b_trigger", "four_c_protection_label": "not_applicable_no_stage4c", "green_lateness_ratio": null, "green_lateness_reason": "no_paired_stage2_actionable_trigger_in_same_case", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "loop_objective": "counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "peak_date": "2024-07-17", "peak_price": 18060.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004560/<year>.csv", "primary_archetype": "material spread supercycle with inventory lag", "profile_path": "atlas/symbol_profiles/004/004560.json", "reuse_reason": null, "round": "R4", "row_type": "trigger", "same_entry_group_id": "C15_R4L73_004560_2024-06-27", "sector": "Materials / steel / copper / spread-cycle", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "004560", "trigger_date": "2024-06-26", "trigger_id": "C15_R4L73_T006_004560_2024-06-27_Stage2Actionable", "trigger_outcome_label": "counterexample_inventory_lag_false_positive", "trigger_type": "Stage2-Actionable"}
{"avg_MAE_180D_pct": -26.23, "avg_MAE_90D_pct": -18.14, "avg_MFE_180D_pct": 50.2, "avg_MFE_90D_pct": 43.8, "avg_four_b_full_window_peak_proximity": 0.6744, "avg_four_b_local_peak_proximity": 0.6744, "avg_green_lateness_ratio": null, "changed_axes": [], "changed_thresholds": {"stage3_green_requires_forward_spread_or_cash_bridge": false}, "eligible_trigger_count": 6, "false_positive_rate": 0.5, "late_green_count": 2, "missed_structural_count": 0, "profile_hypothesis": "current calibrated profile without C15 inventory-lag ladder", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "row_type": "score_simulation", "score_return_alignment_verdict": "reference_or_stress_test", "selected_entry_trigger_per_case": ["C15_R4L73_T001_103140_2025-03-04_Stage2Actionable", "C15_R4L73_T002_103140_2022-03-21_Stage3Yellow", "C15_R4L73_T003_003030_2024-03-20_Stage3Green", "C15_R4L73_T004_306200_2025-02-05_Stage4B", "C15_R4L73_T005_001430_2024-08-05_Stage4B", "C15_R4L73_T006_004560_2024-06-27_Stage2Actionable"]}
{"avg_MAE_180D_pct": -26.23, "avg_MAE_90D_pct": -18.14, "avg_MFE_180D_pct": 50.2, "avg_MFE_90D_pct": 43.8, "avg_four_b_full_window_peak_proximity": 0.6744, "avg_four_b_local_peak_proximity": 0.6744, "avg_green_lateness_ratio": null, "changed_axes": [], "changed_thresholds": {"stage3_green_requires_forward_spread_or_cash_bridge": false}, "eligible_trigger_count": 6, "false_positive_rate": 0.5, "late_green_count": 2, "missed_structural_count": 0, "profile_hypothesis": "older baseline reference; weaker bridge handling", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "row_type": "score_simulation", "score_return_alignment_verdict": "reference_or_stress_test", "selected_entry_trigger_per_case": ["C15_R4L73_T001_103140_2025-03-04_Stage2Actionable", "C15_R4L73_T002_103140_2022-03-21_Stage3Yellow", "C15_R4L73_T003_003030_2024-03-20_Stage3Green", "C15_R4L73_T004_306200_2025-02-05_Stage4B", "C15_R4L73_T005_001430_2024-08-05_Stage4B", "C15_R4L73_T006_004560_2024-06-27_Stage2Actionable"]}
{"avg_MAE_180D_pct": -16.05, "avg_MAE_90D_pct": -9.77, "avg_MFE_180D_pct": 96.01, "avg_MFE_90D_pct": 83.21, "avg_four_b_full_window_peak_proximity": 0.6744, "avg_four_b_local_peak_proximity": 0.6744, "avg_green_lateness_ratio": null, "changed_axes": ["c15_spread_freshness_inventory_lag_guard"], "changed_thresholds": {"stage3_green_requires_forward_spread_or_cash_bridge": true}, "eligible_trigger_count": 3, "false_positive_rate": 0.0, "late_green_count": 0, "missed_structural_count": 0, "profile_hypothesis": "L4 requires spread freshness plus inventory/demand bridge", "profile_id": "P1_L4_spread_freshness_inventory_gate", "profile_scope": "sector_specific_candidate", "row_type": "score_simulation", "score_return_alignment_verdict": "best_guarded_alignment", "selected_entry_trigger_per_case": ["C15_R4L73_T001_103140_2025-03-04_Stage2Actionable", "C15_R4L73_T004_306200_2025-02-05_Stage4B", "C15_R4L73_T005_001430_2024-08-05_Stage4B"]}
{"avg_MAE_180D_pct": -15.57, "avg_MAE_90D_pct": -15.57, "avg_MFE_180D_pct": 191.37, "avg_MFE_90D_pct": 152.96, "avg_four_b_full_window_peak_proximity": null, "avg_four_b_local_peak_proximity": null, "avg_green_lateness_ratio": null, "changed_axes": ["c15_spread_freshness_inventory_lag_guard"], "changed_thresholds": {"stage3_green_requires_forward_spread_or_cash_bridge": true}, "eligible_trigger_count": 1, "false_positive_rate": 0.0, "late_green_count": 0, "missed_structural_count": 0, "profile_hypothesis": "C15 ladder separates result-only records from forward spread/cash conversion", "profile_id": "P2_C15_forward_spread_cash_ladder", "profile_scope": "canonical_archetype_candidate", "row_type": "score_simulation", "score_return_alignment_verdict": "reference_or_stress_test", "selected_entry_trigger_per_case": ["C15_R4L73_T001_103140_2025-03-04_Stage2Actionable"]}
{"avg_MAE_180D_pct": -16.29, "avg_MAE_90D_pct": -6.87, "avg_MFE_180D_pct": 48.33, "avg_MFE_90D_pct": 48.33, "avg_four_b_full_window_peak_proximity": 0.6744, "avg_four_b_local_peak_proximity": 0.6744, "avg_green_lateness_ratio": null, "changed_axes": ["c15_4b_not_4c_margin_collapse_gate"], "changed_thresholds": {"stage3_green_requires_forward_spread_or_cash_bridge": false}, "eligible_trigger_count": 2, "false_positive_rate": 0.0, "late_green_count": 0, "missed_structural_count": 0, "profile_hypothesis": "Single-year margin collapse becomes 4B/watch unless repeated thesis break appears", "profile_id": "P3_C15_4b_not_4c_margin_collapse_guard", "profile_scope": "counterexample_guard", "row_type": "score_simulation", "score_return_alignment_verdict": "reference_or_stress_test", "selected_entry_trigger_per_case": ["C15_R4L73_T004_306200_2025-02-05_Stage4B", "C15_R4L73_T005_001430_2024-08-05_Stage4B"]}
{"MAE_90D_pct": -15.57, "MFE_90D_pct": 152.96, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_01_POONGSAN_2025_GUIDANCE_COPPER_DEFENSE_STAGE2A", "changed_components": ["margin_bridge_score", "customer_quality_score"], "component_delta_explanation": "forward spread plus demand bridge preserved as positive C15 signal.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 50, "asp_or_spread_score": 92, "backlog_visibility_score": 64, "contract_score": 78, "customer_quality_score": 85, "demand_bridge_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": 55, "inventory_lag_risk_score": -1, "legal_or_contract_risk_score": 0, "margin_bridge_score": 81, "non_price_confirmation_score": 7, "policy_or_regulatory_score": 0, "price_phase_score": 3, "realized_margin_cash_score": 5, "relative_strength_score": 68, "revision_score": 45, "source_quality_score": 4, "valuation_repricing_score": 65}, "raw_component_scores_before": {"accounting_trust_risk_score": 50, "asp_or_spread_score": 92, "backlog_visibility_score": 64, "contract_score": 78, "customer_quality_score": 77, "demand_bridge_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": 55, "inventory_lag_risk_score": -1, "legal_or_contract_risk_score": 0, "margin_bridge_score": 73, "non_price_confirmation_score": 7, "policy_or_regulatory_score": 0, "price_phase_score": 3, "realized_margin_cash_score": 5, "relative_strength_score": 68, "revision_score": 45, "source_quality_score": 4, "valuation_repricing_score": 65}, "row_type": "score_simulation", "score_return_alignment_label": "positive_structural_success_forward_spread_and_demand_bridge", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage3-Yellow", "symbol": "103140", "trigger_id": "C15_R4L73_T001_103140_2025-03-04_Stage2Actionable", "weighted_score_after": 84.0, "weighted_score_before": 78.0}
{"MAE_90D_pct": -28.64, "MFE_90D_pct": 3.98, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_02_POONGSAN_2022_RECORD_RESULT_COPPER_LATE_TRAP", "changed_components": ["margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "result-only or inventory-lag spread signal demoted unless forward spread/demand/cash bridge appears.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 50, "asp_or_spread_score": 86, "backlog_visibility_score": 32, "contract_score": 40, "customer_quality_score": 40, "demand_bridge_score": 4, "dilution_cb_risk_score": 0, "execution_risk_score": 90, "inventory_lag_risk_score": -6, "legal_or_contract_risk_score": 0, "margin_bridge_score": 76, "non_price_confirmation_score": 4, "policy_or_regulatory_score": 0, "price_phase_score": -5, "realized_margin_cash_score": 8, "relative_strength_score": 20, "revision_score": 72, "source_quality_score": 4, "valuation_repricing_score": 13}, "raw_component_scores_before": {"accounting_trust_risk_score": 50, "asp_or_spread_score": 86, "backlog_visibility_score": 32, "contract_score": 40, "customer_quality_score": 40, "demand_bridge_score": 4, "dilution_cb_risk_score": 0, "execution_risk_score": 80, "inventory_lag_risk_score": -6, "legal_or_contract_risk_score": 0, "margin_bridge_score": 96, "non_price_confirmation_score": 4, "policy_or_regulatory_score": 0, "price_phase_score": -5, "realized_margin_cash_score": 8, "relative_strength_score": 20, "revision_score": 72, "source_quality_score": 4, "valuation_repricing_score": 25}, "row_type": "score_simulation", "score_return_alignment_label": "counterexample_result_only_green_trap", "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage3-Green", "symbol": "103140", "trigger_id": "C15_R4L73_T002_103140_2022-03-21_Stage3Yellow", "weighted_score_after": 73.0, "weighted_score_before": 88.0}
{"MAE_90D_pct": -22.77, "MFE_90D_pct": 2.56, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_03_SEAH_HOLDINGS_2024_RECORD_OCTG_STAGE3_GREEN_TRAP", "changed_components": ["margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "result-only or inventory-lag spread signal demoted unless forward spread/demand/cash bridge appears.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 40, "asp_or_spread_score": 80, "backlog_visibility_score": 24, "contract_score": 30, "customer_quality_score": 30, "demand_bridge_score": 3, "dilution_cb_risk_score": 0, "execution_risk_score": 85, "inventory_lag_risk_score": -5, "legal_or_contract_risk_score": 0, "margin_bridge_score": 72, "non_price_confirmation_score": 3, "policy_or_regulatory_score": 0, "price_phase_score": -6, "realized_margin_cash_score": 8, "relative_strength_score": 14, "revision_score": 72, "source_quality_score": 3, "valuation_repricing_score": 8}, "raw_component_scores_before": {"accounting_trust_risk_score": 40, "asp_or_spread_score": 80, "backlog_visibility_score": 24, "contract_score": 30, "customer_quality_score": 30, "demand_bridge_score": 3, "dilution_cb_risk_score": 0, "execution_risk_score": 75, "inventory_lag_risk_score": -5, "legal_or_contract_risk_score": 0, "margin_bridge_score": 92, "non_price_confirmation_score": 3, "policy_or_regulatory_score": 0, "price_phase_score": -6, "realized_margin_cash_score": 8, "relative_strength_score": 14, "revision_score": 72, "source_quality_score": 3, "valuation_repricing_score": 20}, "row_type": "score_simulation", "score_return_alignment_label": "counterexample_result_only_green_trap", "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage3-Green", "symbol": "003030", "trigger_id": "C15_R4L73_T003_003030_2024-03-20_Stage3Green", "weighted_score_after": 72.0, "weighted_score_before": 89.0}
{"MAE_90D_pct": -9.48, "MFE_90D_pct": 50.52, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_04_SEAH_STEEL_2025_PROFIT_DROP_LOCAL_4B_NOT_4C", "changed_components": ["execution_risk_score", "hard_4c_routing_qualification"], "component_delta_explanation": "margin collapse kept as 4B/watch instead of hard 4C when repeated thesis break is absent.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 40, "asp_or_spread_score": 26, "backlog_visibility_score": 16, "contract_score": 20, "customer_quality_score": 20, "demand_bridge_score": 2, "dilution_cb_risk_score": 0, "execution_risk_score": 76, "inventory_lag_risk_score": -4, "legal_or_contract_risk_score": 0, "margin_bridge_score": 0, "non_price_confirmation_score": 2, "policy_or_regulatory_score": 0, "price_phase_score": 6, "realized_margin_cash_score": -7, "relative_strength_score": 86, "revision_score": 0, "source_quality_score": 3, "valuation_repricing_score": 80}, "raw_component_scores_before": {"accounting_trust_risk_score": 40, "asp_or_spread_score": 26, "backlog_visibility_score": 16, "contract_score": 20, "customer_quality_score": 20, "demand_bridge_score": 2, "dilution_cb_risk_score": 0, "execution_risk_score": 70, "inventory_lag_risk_score": -4, "legal_or_contract_risk_score": 0, "margin_bridge_score": 0, "non_price_confirmation_score": 2, "policy_or_regulatory_score": 0, "price_phase_score": 6, "realized_margin_cash_score": -7, "relative_strength_score": 86, "revision_score": 0, "source_quality_score": 3, "valuation_repricing_score": 80}, "row_type": "score_simulation", "score_return_alignment_label": "guardrail_positive_4b_watch_not_thesis_death", "stage_label_after": "Stage2", "stage_label_before": "Stage4C", "symbol": "306200", "trigger_id": "C15_R4L73_T004_306200_2025-02-05_Stage4B", "weighted_score_after": 57.0, "weighted_score_before": 42.0}
{"MAE_90D_pct": -4.26, "MFE_90D_pct": 46.14, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_05_SEAH_BESTEEL_2024_Q2_SPECIAL_STEEL_WEAKNESS_4B_WATCH", "changed_components": ["execution_risk_score", "hard_4c_routing_qualification"], "component_delta_explanation": "margin collapse kept as 4B/watch instead of hard 4C when repeated thesis break is absent.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 40, "asp_or_spread_score": 32, "backlog_visibility_score": 8, "contract_score": 12, "customer_quality_score": 13, "demand_bridge_score": 1, "dilution_cb_risk_score": 0, "execution_risk_score": 71, "inventory_lag_risk_score": -3, "legal_or_contract_risk_score": 0, "margin_bridge_score": 0, "non_price_confirmation_score": 2, "policy_or_regulatory_score": 0, "price_phase_score": 7, "realized_margin_cash_score": -4, "relative_strength_score": 92, "revision_score": 0, "source_quality_score": 3, "valuation_repricing_score": 85}, "raw_component_scores_before": {"accounting_trust_risk_score": 40, "asp_or_spread_score": 32, "backlog_visibility_score": 8, "contract_score": 12, "customer_quality_score": 13, "demand_bridge_score": 1, "dilution_cb_risk_score": 0, "execution_risk_score": 65, "inventory_lag_risk_score": -3, "legal_or_contract_risk_score": 0, "margin_bridge_score": 0, "non_price_confirmation_score": 2, "policy_or_regulatory_score": 0, "price_phase_score": 7, "realized_margin_cash_score": -4, "relative_strength_score": 92, "revision_score": 0, "source_quality_score": 3, "valuation_repricing_score": 85}, "row_type": "score_simulation", "score_return_alignment_label": "guardrail_positive_4b_watch_not_thesis_death", "stage_label_after": "Stage2", "stage_label_before": "Stage4B", "symbol": "001430", "trigger_id": "C15_R4L73_T005_001430_2024-08-05_Stage4B", "weighted_score_after": 59.0, "weighted_score_before": 54.0}
{"MAE_90D_pct": -28.1, "MFE_90D_pct": 6.61, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_L73_06_HYUNDAI_BNG_2024_NICKEL_LAGGING_TRAP_STAGE2_FALSE_POSITIVE", "changed_components": ["margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "result-only or inventory-lag spread signal demoted unless forward spread/demand/cash bridge appears.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 50, "asp_or_spread_score": 74, "backlog_visibility_score": 8, "contract_score": 12, "customer_quality_score": 13, "demand_bridge_score": 1, "dilution_cb_risk_score": 0, "execution_risk_score": 100, "inventory_lag_risk_score": -8, "legal_or_contract_risk_score": 0, "margin_bridge_score": 0, "non_price_confirmation_score": 2, "policy_or_regulatory_score": 0, "price_phase_score": 1, "realized_margin_cash_score": -5, "relative_strength_score": 56, "revision_score": 0, "source_quality_score": 4, "valuation_repricing_score": 43}, "raw_component_scores_before": {"accounting_trust_risk_score": 50, "asp_or_spread_score": 74, "backlog_visibility_score": 8, "contract_score": 12, "customer_quality_score": 13, "demand_bridge_score": 1, "dilution_cb_risk_score": 0, "execution_risk_score": 90, "inventory_lag_risk_score": -8, "legal_or_contract_risk_score": 0, "margin_bridge_score": 0, "non_price_confirmation_score": 2, "policy_or_regulatory_score": 0, "price_phase_score": 1, "realized_margin_cash_score": -5, "relative_strength_score": 56, "revision_score": 0, "source_quality_score": 4, "valuation_repricing_score": 55}, "row_type": "score_simulation", "score_return_alignment_label": "counterexample_inventory_lag_false_positive", "stage_label_after": "Stage2", "stage_label_before": "Stage3-Yellow", "symbol": "004560", "trigger_id": "C15_R4L73_T006_004560_2024-06-27_Stage2Actionable", "weighted_score_after": 61.0, "weighted_score_before": 77.0}
{"aggregate_id": "C15_R4L73_SPREAD_INVENTORY_LAG_SUMMARY", "calibration_usable_case_count": 6, "calibration_usable_trigger_count": 6, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "counterexample_count": 3, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "mean_MAE_180D_counterexamples": -36.41, "mean_MFE_180D_positive_cases": 96.01, "new_symbol_count": 5, "new_trigger_family_count": 6, "positive_case_count": 3, "representative_trigger_count": 4, "residual_error_types_found": ["result_only_green_trap", "inventory_lag_false_positive", "hard4c_too_early_after_single_year_margin_drop"], "round": "R4", "row_type": "aggregate"}
{"axis": "c15_spread_freshness_inventory_lag_guard", "backtest_effect": "Counterexamples avg MFE180 4.38% / MAE180 -36.41% vs positive avg MFE180 96.01% / MAE180 -16.05%", "baseline_value": 0, "calibration_usable_count": 6, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "confidence": "medium", "counterexample_count": 3, "delta": "+1", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "new_independent_case_count": 6, "notes": "not production; post-calibrated residual", "proposal_type": "canonical_shadow_only", "reason": "Require forward spread/demand/inventory bridge before Green", "row_type": "shadow_weight", "scope": "canonical_archetype_specific", "tested_value": 1, "trigger_ids": "C15_R4L73_T001_103140_2025-03-04_Stage2Actionable|C15_R4L73_T002_103140_2022-03-21_Stage3Yellow|C15_R4L73_T003_003030_2024-03-20_Stage3Green|C15_R4L73_T004_306200_2025-02-05_Stage4B|C15_R4L73_T005_001430_2024-08-05_Stage4B|C15_R4L73_T006_004560_2024-06-27_Stage2Actionable"}
{"canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "do_not_propose_new_weight_delta": false, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "loop": "73", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": ["c15_spread_freshness_inventory_lag_guard", "c15_result_only_green_trap_cap", "c15_4b_not_4c_margin_collapse_gate"], "new_independent_case_count": 6, "new_symbol_count": 5, "new_trigger_family_count": 6, "residual_error_types_found": ["result_only_green_trap", "inventory_lag_false_positive", "hard4c_too_early_after_single_year_margin_drop"], "reused_case_count": 0, "round": "R4", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["stage2_required_bridge", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"]}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 4
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- For C15 specifically, test the spread-freshness/inventory-lag ladder before Green promotion.
- Single-year margin collapse should route through 4B/watch before hard 4C unless repeated thesis-break evidence confirms death.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 73
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / C15 spread reversal and inventory-cycle counterexample quality reinforcement
next_recommended_archetypes = C01 direct backlog-to-FCF rows; C13 direct AMPC/utilization rows; C10 direct order-conversion rows; C31 direct awarded-cashflow rows; R13 only for genuinely new taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN prompt: `https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
- No-Repeat Index: `https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md`
- Stock-Web manifest: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json`
- Stock-Web schema: `https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json`
