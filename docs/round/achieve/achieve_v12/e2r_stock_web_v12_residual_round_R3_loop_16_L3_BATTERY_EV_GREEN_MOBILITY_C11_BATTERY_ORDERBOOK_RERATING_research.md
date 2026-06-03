# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

scheduled_round = R3  
scheduled_loop = 16  
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY  
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING  
fine_archetype_id = BATTERY_MATERIALS_ORDERBOOK_RERATING_WITH_CALLOFF_GUARD  
research_session = post_calibrated_sector_archetype_residual_research  
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12  
price_source = Songdaiki/stock-web  
price_basis = tradable_raw  
price_adjustment_status = raw_unadjusted_marcap  
stock_web_manifest_max_date = 2026-02-20  
production_scoring_changed = false  
shadow_weight_only = true  
round_schedule_status = valid  
round_sector_consistency = pass  


This loop adds **4** new independent cases, **2** counterexamples, and **3** current-profile residual errors for **R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING**.

## 1. Current Calibrated Profile Assumption

Current proxy profile: `e2r_2_1_stock_web_calibrated_proxy`.

Assumed existing global axes:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This research does **not** re-propose those axes globally. It tests whether C11 battery orderbook rerating needs a tighter archetype-specific split between:

```text
valid_orderbook_to_delivery_path
vs
headline/orderbook identity without customer delivery/utilization proof
```

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R3 |
| scheduled_loop | 16 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| fine_archetype_id | BATTERY_MATERIALS_ORDERBOOK_RERATING_WITH_CALLOFF_GUARD |
| loop_objective | coverage_gap_fill, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, stage2_actionable_bonus_stress_test, green_strictness_stress_test, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test |
| rule_scope_candidate | canonical_archetype_specific |
| output_file | e2r_stock_web_v12_residual_round_R3_loop_16_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md |

R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`; the round-sector consistency gate passes.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 R3 artifacts already covered:

```text
R3 Loop 10: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
R3 Loop 11: C14_EV_DEMAND_SLOWDOWN_4B_4C
R3 Loop 12: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
R3 Loop 13: C11_BATTERY_ORDERBOOK_RERATING
R3 Loop 14: C14_EV_DEMAND_SLOWDOWN_4B_4C
R3 Loop 15: C14_EV_DEMAND_SLOWDOWN_4B_4C
```

Prior R3 symbols included `006400`, `096770`, `373220`, `003670`, `066970`, `086520`, `247540`, `051910`, `361610`, `020150`, and `011790`.

This loop deliberately selects **348370 / 002710 / 278280 / 393890**, all new counted R3 C11 representative symbols. The same canonical archetype is allowed; the duplicate-avoidance gate is based on symbol + trigger_date + entry_date + evidence family, and this loop does not reuse any prior counted R3 C11 trigger.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest was read before case selection. The manifest reports `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. It also states that raw/unadjusted OHLC is used, zero-volume and zero-OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default. fileciteturn1377file0L3-L60

| source field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 5. Historical Eligibility Gate

| symbol | company | profile_path | first_date | last_date | corporate_action_window_status | calibration_usable |
|---:|---|---|---|---|---|---|
| 348370 | 엔켐 | atlas/symbol_profiles/348/348370.json | 2021-11-01 | 2026-02-20 | clean_180D_window | true |
| 002710 | TCC스틸 | atlas/symbol_profiles/002/002710.json | 1995-05-02 | 2026-02-20 | old CA candidate 2009 only; clean tested window | true |
| 278280 | 천보 | atlas/symbol_profiles/278/278280.json | 2019-02-11 | 2026-02-20 | clean_180D_window | true |
| 393890 | 더블유씨피 | atlas/symbol_profiles/393/393890.json | 2022-09-30 | 2026-02-20 | clean_180D_window | true |

Profile checks: Enchem has no corporate-action candidates in its profile. fileciteturn1378file0L23-L93 TCC Steel has a historical corporate-action candidate on 2009-05-08, outside the tested 2023 window. fileciteturn1379file0L33-L40 fileciteturn1380file0L3-L16 Chunbo has no corporate-action candidates. fileciteturn1383file0L29-L109 WCP has no corporate-action candidates. fileciteturn1384file0L29-L94

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING

compressed fine archetypes:
- US_ELECTROLYTE_CAPACITY_ORDERBOOK_RERATING
- CYLINDRICAL_BATTERY_CAN_MATERIAL_RERATING
- ELECTROLYTE_SALT_RECOVERY_WITHOUT_CUSTOMER_DELIVERY
- SEPARATOR_ORDERBOOK_RERATING_BROKEN_BY_UTILIZATION

compression thesis:
C11 is not merely "battery orderbook headline." The useful compression is:
  orderbook/customer/capacity evidence + visible delivery or utilization route
  minus call-off/utilization/commodity margin risk.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | entry_date | MFE90 | MAE90 | current_profile_verdict | notes |
|---|---:|---|---|---|---|---:|---:|---|---|
| R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102 | 348370 | 엔켐 | structural_success | positive | 2024-01-02 | 374.73 | -5.17 | current_profile_too_late | Electrolyte orderbook/capacity identity was strong enough for Stage2-actionable before financial confirmation; later price-only overheat needs 4B-watch, not full 4B. |
| R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323 | 002710 | TCC스틸 | high_mae_success | positive | 2023-03-23 | 230.99 | -13.14 | current_profile_correct | A battery-material identity/orderbook rerating produced very high MFE but also early MAE; Stage2-actionable is justified, Green should still wait for delivery/margin confirmation. |
| R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102 | 278280 | 천보 | failed_rerating | counterexample | 2024-01-02 | 1.19 | -28.35 | current_profile_false_positive | Electrolyte theme recovery without customer delivery/utilization proof created almost no upside and a deep drawdown. |
| R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102 | 393890 | 더블유씨피 | 4C_success | counterexample | 2024-01-02 | 10.06 | -33.92 | current_profile_false_positive | Separator orderbook identity failed when utilization/order drawdown became the dominant evidence; 4C-watch should dominate later. |

## 8. Positive vs Counterexample Balance

| bucket | count | symbols | interpretation |
|---|---:|---|---|
| positive_structural_success / high-MAE success | 2 | 348370, 002710 | Orderbook/capacity identity produced real MFE when paired with relative strength and delivery/capacity route. |
| counterexample / failed rerating / 4C success | 2 | 278280, 393890 | Theme/orderbook identity without customer delivery or utilization proof produced low MFE and deep MAE. |
| 4B overlay case | 1 | 348370 | Price-only peak proximity is useful as watch overlay, not full 4B. |
| 4C overlay case | 1 | 393890 | Utilization/order-drawdown should demote C11 before the full price collapse. |

## 9. Evidence Source Map

| case_id | evidence family | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102 | electrolyte orderbook/capacity rerating | public event, capacity route, customer/order quality, relative strength | financial visibility only partial | price-only 4B watch near 2024-04-08 peak |
| R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323 | cylindrical battery-can material rerating | public event, capacity route, backlog visibility, relative strength | still incomplete margin/revision bridge | high-MAE success; later overheat watch needed |
| R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102 | electrolyte salt recovery without delivery proof | weak public/theme evidence | none | call-off/utilization risk; thesis evidence not proven |
| R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102 | separator orderbook thesis broken by utilization | public/orderbook identity | none | later 4C-watch after utilization/order-drawdown behavior |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | stock-web rows cited |
|---:|---|---|---|---|
| 348370 | 엔켐 | atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv | atlas/symbol_profiles/348/348370.json | 2024-01-02 close 83,100; 2024-04-08 high 394,500; later drawdown rows |
| 002710 | TCC스틸 | atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv | atlas/symbol_profiles/002/002710.json | 2023-03-23 close 22,750; 2023-07-26 high 75,300 |
| 278280 | 천보 | atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv | atlas/symbol_profiles/278/278280.json | 2024-01-02 close 109,700; 2024-08-05 low 49,000 |
| 393890 | 더블유씨피 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json | 2024-01-02 close 45,250; 2024-09-09 low 16,800 |

Stock-web row anchors: Enchem's 2024 file contains 2024-01-02 close 83,100 and 2024-04-08 high 394,500. fileciteturn1386file0L4-L70 Enchem later rows show the post-peak decline, including August lows. fileciteturn1388file0L3-L43 TCC Steel's 2023 file contains the March battery-material acceleration and July peak area. fileciteturn1389file0L59-L72 fileciteturn1390file0L3-L71 fileciteturn1391file0L3-L56 Chunbo's 2024 file shows weak upside from 2024-01-02 and a later August low. fileciteturn1392file0L4-L71 fileciteturn1396file0L3-L43 WCP's 2024 file shows January entry, April/May relief, and the later utilization-style decline. fileciteturn1393file0L4-L71 fileciteturn1395file0L3-L70 fileciteturn1394file0L3-L67

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | current_profile | aggregate_role |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| TRG-R3L16-C11-348370-STAGE2-20240102 | 348370 | Stage2-Actionable | 2024-01-02 | 2024-01-02 | 83100 | 258.6 | -5.17 | 374.73 | -5.17 | 374.73 | -5.17 | 2024-04-08 | 394500 | current_profile_too_late | representative |
| TRG-R3L16-C11-348370-4B-WATCH-20240408 | 348370 | 4B-Overlay-Watch | 2024-04-08 | 2024-04-08 | 358000 | 10.2 | -38.41 | 10.2 | -52.18 | 10.2 | -58.38 | 2024-04-08 | 394500 | current_profile_correct | 4B_overlay_only |
| TRG-R3L16-C11-002710-STAGE2-20230323 | 002710 | Stage2-Actionable | 2023-03-23 | 2023-03-23 | 22750 | 115.38 | -13.14 | 230.99 | -13.14 | 230.99 | -13.14 | 2023-07-26 | 75300 | current_profile_correct | representative |
| TRG-R3L16-C11-278280-STAGE2-20240102 | 278280 | Stage2-Actionable-Candidate | 2024-01-02 | 2024-01-02 | 109700 | 1.19 | -24.52 | 1.19 | -28.35 | 1.19 | -55.33 | 2024-01-02 | 111000 | current_profile_false_positive | representative |
| TRG-R3L16-C11-393890-STAGE2-20240102 | 393890 | Stage2-Actionable-Candidate | 2024-01-02 | 2024-01-02 | 45250 | 10.06 | -15.36 | 10.06 | -33.92 | 10.06 | -62.87 | 2024-01-05 | 49800 | current_profile_false_positive | representative |
| TRG-R3L16-C11-393890-4C-WATCH-20240722 | 393890 | 4C-Thesis-Break-Watch | 2024-07-22 | 2024-07-22 | 25250 | 6.34 | -22.1 | 6.34 | -33.47 | 6.34 | -33.47 | 2024-07-22 | 26850 | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger aggregate rows

| symbol | entry_date | entry_price | MFE30 / MAE30 | MFE90 / MAE90 | MFE180 / MAE180 | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---|---:|---:|
| 348370 | 2024-01-02 | 83,100 | +258.60 / -5.17 | +374.73 / -5.17 | +374.73 / -5.17 | 2024-04-08 | 394,500 | -62.23 |
| 002710 | 2023-03-23 | 22,750 | +115.38 / -13.14 | +230.99 / -13.14 | +230.99 / -13.14 | 2023-07-26 | 75,300 | -36.19 |
| 278280 | 2024-01-02 | 109,700 | +1.19 / -24.52 | +1.19 / -28.35 | +1.19 / -55.33 | 2024-01-02 | 111,000 | -55.86 |
| 393890 | 2024-01-02 | 45,250 | +10.06 / -15.36 | +10.06 / -33.92 | +10.06 / -62.87 | 2024-01-05 | 49,800 | -66.27 |

### 12.2 Overlay rows

| trigger | entry_date | entry_price | MFE90 / MAE90 | overlay verdict |
|---|---|---:|---:|---|
| TRG-R3L16-C11-348370-4B-WATCH-20240408 | 2024-04-08 | 358,000 | +10.20 / -52.18 | Price-only peak proximity worked as a warning, but not full 4B. |
| TRG-R3L16-C11-393890-4C-WATCH-20240722 | 2024-07-22 | 25,250 | +6.34 / -33.47 | Utilization/order-drawdown 4C watch protected against further loss. |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| 348370 Enchem | Stage3-Yellow only after strong price/revision visibility | Early Stage2 had much better asymmetry than late Green; price-only 4B watch later worked | current_profile_too_late |
| 002710 TCC Steel | Stage2/Yellow with high volatility | Correct to allow Stage2 but Green should wait; high MAE confirms sizing/volatility guard | current_profile_correct |
| 278280 Chunbo | Could over-promote electrolyte recovery theme | Actual MFE90 only +1.19, MAE180 -55.33 | current_profile_false_positive |
| 393890 WCP | Could over-promote separator orderbook identity | Actual MFE90 +10.06, MAE180 -62.87; later 4C should dominate | current_profile_false_positive |

Answers to required stress-test questions:

```text
1. current calibrated profile judgement:
   Mixed. It can catch strong orderbook/material beta, but C11 lacks a delivery/utilization split.
2. alignment with actual MFE/MAE:
   Correct for 002710, too late for 348370, false-positive for 278280/393890.
3. Stage2 bonus:
   Useful for 348370/002710, too loose for weak orderbook-delivery evidence.
4. Yellow 75:
   Adequate only with customer/delivery proof; too loose for electrolyte/separator recovery labels alone.
5. Green 87 / revision 55:
   Still appropriate; neither 348370 nor 002710 should be Green from price alone.
6. price-only blowoff guard:
   Strengthened by Enchem 2024-04-08.
7. full 4B non-price requirement:
   Kept. Enchem's row is a watch overlay, not full 4B.
8. hard 4C routing:
   Needs faster C11-specific utilization/order-drawdown watch for pure separator/electrolyte cases.
```

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | Stage2 entry_price | inferred Green/late confirmation | green_lateness_ratio | interpretation |
|---:|---|---:|---|---:|---|
| 348370 | 2024-01-02 | 83,100 | 2024-04-03/04 area after major rerating | 0.75 | Green based on later confirmation would miss most upside. |
| 002710 | 2023-03-23 | 22,750 | July orderbook/price maturity area | 0.55 | Green is materially late; Stage2-actionable was the useful label. |
| 278280 | 2024-01-02 | 109,700 | none | not_applicable | No valid Green trigger; recovery label failed. |
| 393890 | 2024-01-02 | 45,250 | none | not_applicable | No valid Green trigger; 4C watch later dominates. |

The loop does not re-propose a lower global Green threshold. It proposes a C11-specific split: early Stage2-actionable is allowed only when orderbook/capacity evidence has a delivery path, and weak orderbook labels are capped.

## 15. 4B Local vs Full-window Timing Audit

| trigger | Stage2 anchor | 4B watch entry | local peak proximity | full-window peak proximity | 4B evidence type | verdict |
|---|---|---|---:|---:|---|---|
| TRG-R3L16-C11-348370-4B-WATCH-20240408 | 2024-01-02 close 83,100 | 2024-04-08 close 358,000 | 0.88 | 0.88 | price_only, valuation_blowoff, positioning_overheat | Price-only 4B watch is useful, but full 4B remains blocked without non-price evidence. |

## 16. 4C Protection Audit

| trigger | prior entry | 4C watch entry | observed post-watch MAE90 | protection label | interpretation |
|---|---|---|---:|---|---|
| TRG-R3L16-C11-393890-4C-WATCH-20240722 | 2024-01-02 close 45,250 | 2024-07-22 close 25,250 | -33.47 | hard_4c_success | Once utilization/order-drawdown dominated separator orderbook identity, C11 positive scoring should be demoted. |
| TRG-R3L16-C11-278280-STAGE2-20240102 | 2024-01-02 close 109,700 | no separate overlay row | -55.33 by 180D | thesis_break_watch_only | Weak delivery/customer proof should cap the initial positive label before hard 4C. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate_axis = battery_orderbook_delivery_quality_bonus
tested_delta = +2 shadow-only
condition:
  apply only when customer/order/capacity evidence has visible delivery, utilization, or conversion route.
counter-condition:
  do not apply when evidence is merely theme/orderbook identity without customer call-off protection.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING

candidate_1:
  axis = C11_orderbook_delivery_quality_bonus
  delta = +2 shadow-only
  reason = valid C11 positives were not just battery-theme moves; they had capacity/orderbook route plus relative strength.

candidate_2:
  axis = C11_calloff_utilization_guard
  delta = -3 shadow-only
  reason = weak electrolyte/separator orderbook labels generated false positives when utilization/delivery proof was absent.

candidate_3:
  axis = C11_price_only_peak_watch_not_full_4B
  delta = 0; strengthens existing axis
  reason = Enchem 2024-04-08 was a good watch overlay but not full 4B without non-price evidence.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 4 | representative per case | 154.24 | -20.15 | 154.24 | -34.13 | 0.50 | 1 | 2 | 0.65 | 0.88 | 0.88 | high MFE average hides two severe false positives |
| P0b e2r_2_0_baseline_reference | rollback_reference | none | 4 | representative per case | 154.24 | -20.15 | 154.24 | -34.13 | 0.50 | 1 | 2 | 0.65 | 0.88 | 0.88 | weaker guard; repeats false positive pattern |
| P1 sector_specific_candidate_profile | sector_specific | C11_delivery_quality_bonus; C11_calloff_guard | 2 | 348370 + 002710 | 302.86 | -9.16 | 302.86 | -9.16 | 0.00 | 0 | 2 | 0.65 | 0.88 | 0.88 | better score-return alignment |
| P2 canonical_archetype_candidate_profile | canonical_archetype_specific | same as P1, scoped to C11 | 2 | 348370 + 002710 | 302.86 | -9.16 | 302.86 | -9.16 | 0.00 | 0 | 2 | 0.65 | 0.88 | 0.88 | best compression candidate |
| P3 counterexample_guard_profile | canonical_archetype_specific | stricter call-off/utilization guard | 2 positive + 4C watch | 348370, 002710, 393890 4C overlay | 205.12 | -18.24 | 205.12 | -26.18 | 0.00 | 0 | 2 | 0.65 | 0.88 | 0.88 | protects counterexamples; watch overlay not positive promotion |


## 20. Score-Return Alignment Matrix

| bucket | score behavior | return behavior | alignment |
|---|---|---|---|
| strong orderbook + capacity route | 348370 / 002710 promoted to Stage2/Y | large MFE with acceptable or high-but-compensated MAE | aligned |
| theme/orderbook identity without delivery | 278280 / 393890 capped or demoted | low MFE, deep 180D MAE | aligned after shadow guard |
| price-only peak proximity | 348370 4B watch | watch row followed by severe drawdown | useful overlay, not full 4B |
| utilization/order-drawdown 4C | 393890 4C watch | further downside after watch | protection label works |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | BATTERY_MATERIALS_ORDERBOOK_RERATING_WITH_CALLOFF_GUARD | 2 | 2 | 1 | 1 | 4 | 0 | 6 | 4 | 3 | true | true | Remaining C11 gap is larger holdout across non-Korean battery-material orderbook cycles and explicit customer call-off disclosures. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C11_orderbook_without_delivery_false_positive
  - pure_separator_utilization_4C_too_late
  - price_only_4B_watch_not_full_4B
  - C11_capacity_orderbook_stage2_too_late
new_axis_proposed:
  - C11_orderbook_delivery_quality_bonus
  - C11_calloff_utilization_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Actual stock-web 1D OHLC rows were used for entry/peak/MFE/MAE.
- Entry dates are historical.
- Every representative trigger has at least 180 trading days available before manifest max_date.
- Corporate-action windows were checked through stock-web profiles.
- Same entry group dedupe is explicitly marked.
- Production scoring is unchanged; all changes are shadow-only.
```

Not validated:

```text
- This is not a live scan.
- This is not an investment recommendation.
- This does not patch stock_agent code.
- This does not prove a global scoring delta.
- Evidence labels are research proxy labels; future implementation should map them to formal source rows.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_delivery_quality_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,+2,+2,"Promote only when orderbook/capacity evidence has visible delivery or customer quality.","Raises Enchem/TCC without lifting Chunbo/WCP false positives.","TRG-R3L16-C11-348370-STAGE2-20240102|TRG-R3L16-C11-002710-STAGE2-20230323",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_calloff_utilization_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,-3,-3,"Cap orderbook rerating when customer call-off/utilization risk dominates.","Blocks Chunbo/WCP false positives while preserving high-MFE orderbook cases.","TRG-R3L16-C11-278280-STAGE2-20240102|TRG-R3L16-C11-393890-STAGE2-20240102|TRG-R3L16-C11-393890-4C-WATCH-20240722",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_price_only_peak_watch_not_full_4B,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,true,true,0,"Keep existing full 4B non-price requirement; use price-only blowoff as watch overlay.","Enchem price-only proximity captured risk, but not a full 4B thesis-break evidence row.","TRG-R3L16-C11-348370-4B-WATCH-20240408",4,4,2,medium,axis_strengthening,"strengthens existing full_4b_requires_non_price_evidence"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "US_ELECTROLYTE_CAPACITY_ORDERBOOK_RERATING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG-R3L16-C11-348370-STAGE2-20240102", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "structural_success", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Electrolyte orderbook/capacity identity was strong enough for Stage2-actionable before financial confirmation; later price-only overheat needs 4B-watch, not full 4B."}
{"row_type": "case", "case_id": "R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CYLINDRICAL_BATTERY_CAN_MATERIAL_RERATING", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TRG-R3L16-C11-002710-STAGE2-20230323", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "high_mae_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "A battery-material identity/orderbook rerating produced very high MFE but also early MAE; Stage2-actionable is justified, Green should still wait for delivery/margin confirmation."}
{"row_type": "case", "case_id": "R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_SALT_RECOVERY_WITHOUT_CUSTOMER_DELIVERY", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R3L16-C11-278280-STAGE2-20240102", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Electrolyte theme recovery without customer delivery/utilization proof created almost no upside and a deep drawdown."}
{"row_type": "case", "case_id": "R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "SEPARATOR_ORDERBOOK_RERATING_BROKEN_BY_UTILIZATION", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R3L16-C11-393890-STAGE2-20240102", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "4C_success", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Separator orderbook identity failed when utilization/order drawdown became the dominant evidence; 4C-watch should dominate later."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG-R3L16-C11-348370-STAGE2-20240102", "case_id": "R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "US_ELECTROLYTE_CAPACITY_ORDERBOOK_RERATING", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating_with_calloff_guard", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "stage2_actionable_bonus_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "Battery electrolyte orderbook/capacity identity visible at start of the 2024 rerating leg; price row entry uses 2024-01-02 close.", "evidence_source": "stock-web profile and 2024 tradable rows; public electrolyte orderbook/capacity reporting used as qualitative evidence.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "profile_path": "atlas/symbol_profiles/348/348370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-02", "entry_price": 83100, "MFE_30D_pct": 258.6, "MFE_90D_pct": 374.73, "MFE_180D_pct": 374.73, "MFE_1Y_pct": 374.73, "MFE_2Y_pct": null, "MAE_30D_pct": -5.17, "MAE_90D_pct": -5.17, "MAE_180D_pct": -5.17, "MAE_1Y_pct": -62.23, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 394500, "drawdown_after_peak_pct": -62.23, "green_lateness_ratio": 0.75, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_late_price_only_4B", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16-348370-20240102-83100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L16-C11-348370-4B-WATCH-20240408", "case_id": "R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "US_ELECTROLYTE_CAPACITY_ORDERBOOK_RERATING", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating_with_calloff_guard", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "stage2_actionable_bonus_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "4B-Overlay-Watch", "trigger_date": "2024-04-08", "evidence_available_at_that_date": "Observed cycle was near the 2024 local/full-window peak after a very rapid electrolyte rerating; non-price 4B evidence was insufficient for full 4B.", "evidence_source": "stock-web 2024 tradable rows around 2024-04-08 high/close and subsequent drawdown.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "profile_path": "atlas/symbol_profiles/348/348370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-08", "entry_price": 358000, "MFE_30D_pct": 10.2, "MFE_90D_pct": 10.2, "MFE_180D_pct": 10.2, "MFE_1Y_pct": 10.2, "MFE_2Y_pct": null, "MAE_30D_pct": -38.41, "MAE_90D_pct": -52.18, "MAE_180D_pct": -58.38, "MAE_1Y_pct": -58.38, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 394500, "drawdown_after_peak_pct": -62.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "price_only_watch_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "price_only_4B_watch_worked_but_not_full_4B", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16-348370-20240408-358000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L16-C11-002710-STAGE2-20230323", "case_id": "R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "CYLINDRICAL_BATTERY_CAN_MATERIAL_RERATING", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating_with_calloff_guard", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "stage2_actionable_bonus_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-23", "evidence_available_at_that_date": "Battery-can material identity and orderbook-style rerating became visible during the March 2023 battery-material acceleration.", "evidence_source": "stock-web 2023 tradable rows; public battery-can material rerating narrative used as qualitative evidence.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv", "profile_path": "atlas/symbol_profiles/002/002710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-23", "entry_price": 22750, "MFE_30D_pct": 115.38, "MFE_90D_pct": 230.99, "MFE_180D_pct": 230.99, "MFE_1Y_pct": 230.99, "MFE_2Y_pct": null, "MAE_30D_pct": -13.14, "MAE_90D_pct": -13.14, "MAE_180D_pct": -13.14, "MAE_1Y_pct": -36.19, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 75300, "drawdown_after_peak_pct": -36.19, "green_lateness_ratio": 0.55, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16-002710-20230323-22750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L16-C11-278280-STAGE2-20240102", "case_id": "R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "ELECTROLYTE_SALT_RECOVERY_WITHOUT_CUSTOMER_DELIVERY", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating_with_calloff_guard", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "stage2_actionable_bonus_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "Stage2-Actionable-Candidate", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "Electrolyte-salt recovery narrative existed, but delivery/customer utilization proof was weak relative to the theme label.", "evidence_source": "stock-web 2024 tradable rows; public electrolyte-salt recovery/slowdown context used as qualitative evidence.", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv", "profile_path": "atlas/symbol_profiles/278/278280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-02", "entry_price": 109700, "MFE_30D_pct": 1.19, "MFE_90D_pct": 1.19, "MFE_180D_pct": 1.19, "MFE_1Y_pct": 1.19, "MFE_2Y_pct": null, "MAE_30D_pct": -24.52, "MAE_90D_pct": -28.35, "MAE_180D_pct": -55.33, "MAE_1Y_pct": -55.33, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 111000, "drawdown_after_peak_pct": -55.86, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16-278280-20240102-109700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L16-C11-393890-STAGE2-20240102", "case_id": "R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "SEPARATOR_ORDERBOOK_RERATING_BROKEN_BY_UTILIZATION", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating_with_calloff_guard", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "stage2_actionable_bonus_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "Stage2-Actionable-Candidate", "trigger_date": "2024-01-02", "evidence_available_at_that_date": "Separator orderbook identity remained visible, but pure EV separator utilization risk was not resolved.", "evidence_source": "stock-web 2024 tradable rows; public separator-utilization slowdown context used as qualitative evidence.", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-02", "entry_price": 45250, "MFE_30D_pct": 10.06, "MFE_90D_pct": 10.06, "MFE_180D_pct": 10.06, "MFE_1Y_pct": 10.06, "MFE_2Y_pct": null, "MAE_30D_pct": -15.36, "MAE_90D_pct": -33.92, "MAE_180D_pct": -62.87, "MAE_1Y_pct": -62.87, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-05", "peak_price": 49800, "drawdown_after_peak_pct": -66.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success_later_than_initial_stage2", "trigger_outcome_label": "orderbook_rerating_broken_by_utilization_4C", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16-393890-20240102-45250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L16-C11-393890-4C-WATCH-20240722", "case_id": "R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "SEPARATOR_ORDERBOOK_RERATING_BROKEN_BY_UTILIZATION", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery_orderbook_rerating_with_calloff_guard", "loop_objective": ["coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "stage2_actionable_bonus_stress_test", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "4C-Thesis-Break-Watch", "trigger_date": "2024-07-22", "evidence_available_at_that_date": "By late July the separator orderbook rerating thesis had become dominated by utilization/order-drawdown behavior; price path shows protective value from a 4C-watch overlay.", "evidence_source": "stock-web 2024 tradable rows around 2024-07-22 and the subsequent Aug-Sep drawdown.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-22", "entry_price": 25250, "MFE_30D_pct": 6.34, "MFE_90D_pct": 6.34, "MFE_180D_pct": 6.34, "MFE_1Y_pct": 6.34, "MFE_2Y_pct": null, "MAE_30D_pct": -22.1, "MAE_90D_pct": -33.47, "MAE_180D_pct": -33.47, "MAE_1Y_pct": -33.47, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-22", "peak_price": 26850, "drawdown_after_peak_pct": -37.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_watch_protects_against_further_drawdown", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L16-393890-20240722-25250", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102", "trigger_id": "TRG-R3L16-C11-348370-STAGE2-20240102", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow axis applied.", "MFE_90D_pct": 374.73, "MAE_90D_pct": -5.17, "score_return_alignment_label": "structural_success_with_late_price_only_4B", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102", "trigger_id": "TRG-R3L16-C11-348370-STAGE2-20240102", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow axis applied.", "MFE_90D_pct": 374.73, "MAE_90D_pct": -5.17, "score_return_alignment_label": "structural_success_with_late_price_only_4B", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102", "trigger_id": "TRG-R3L16-C11-348370-STAGE2-20240102", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 15, "capacity_route_score": 14, "calloff_guard_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["orderbook_delivery_score", "capacity_route_score", "calloff_guard_score"], "component_delta_explanation": "capacity/orderbook rerating should promote earlier but 4B remains price-only watch", "MFE_90D_pct": 374.73, "MAE_90D_pct": -5.17, "score_return_alignment_label": "structural_success_with_late_price_only_4B", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102", "trigger_id": "TRG-R3L16-C11-348370-STAGE2-20240102", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 15, "capacity_route_score": 14, "calloff_guard_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["orderbook_delivery_score", "capacity_route_score", "calloff_guard_score"], "component_delta_explanation": "capacity/orderbook rerating should promote earlier but 4B remains price-only watch", "MFE_90D_pct": 374.73, "MAE_90D_pct": -5.17, "score_return_alignment_label": "structural_success_with_late_price_only_4B", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L16-C11-348370-ENCHEM-US-ELECTROLYTE-ORDERBOOK-20240102", "trigger_id": "TRG-R3L16-C11-348370-STAGE2-20240102", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 12, "backlog_visibility_score": 16, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 12, "valuation_repricing_score": 12, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 15, "capacity_route_score": 14, "calloff_guard_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["calloff_guard_score", "orderbook_delivery_score", "thesis_break_score"], "component_delta_explanation": "capacity/orderbook rerating should promote earlier but 4B remains price-only watch Counterexample guard is slightly stricter on weak orderbook proof.", "MFE_90D_pct": 374.73, "MAE_90D_pct": -5.17, "score_return_alignment_label": "structural_success_with_late_price_only_4B", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323", "trigger_id": "TRG-R3L16-C11-002710-STAGE2-20230323", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow axis applied.", "MFE_90D_pct": 230.99, "MAE_90D_pct": -13.14, "score_return_alignment_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323", "trigger_id": "TRG-R3L16-C11-002710-STAGE2-20230323", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow axis applied.", "MFE_90D_pct": 230.99, "MAE_90D_pct": -13.14, "score_return_alignment_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323", "trigger_id": "TRG-R3L16-C11-002710-STAGE2-20230323", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 10, "capacity_route_score": 12, "calloff_guard_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow-shadow", "changed_components": ["orderbook_delivery_score", "capacity_route_score", "calloff_guard_score"], "component_delta_explanation": "orderbook material identity works as Stage2/Y; Green still needs margin", "MFE_90D_pct": 230.99, "MAE_90D_pct": -13.14, "score_return_alignment_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323", "trigger_id": "TRG-R3L16-C11-002710-STAGE2-20230323", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 10, "capacity_route_score": 12, "calloff_guard_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow-shadow", "changed_components": ["orderbook_delivery_score", "capacity_route_score", "calloff_guard_score"], "component_delta_explanation": "orderbook material identity works as Stage2/Y; Green still needs margin", "MFE_90D_pct": 230.99, "MAE_90D_pct": -13.14, "score_return_alignment_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L16-C11-002710-TCCSTEEL-CAN-MATERIAL-ORDERBOOK-20230323", "trigger_id": "TRG-R3L16-C11-002710-STAGE2-20230323", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 9, "backlog_visibility_score": 13, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 18, "customer_quality_score": 9, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 10, "capacity_route_score": 12, "calloff_guard_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow-shadow", "changed_components": ["calloff_guard_score", "orderbook_delivery_score", "thesis_break_score"], "component_delta_explanation": "orderbook material identity works as Stage2/Y; Green still needs margin Counterexample guard is slightly stricter on weak orderbook proof.", "MFE_90D_pct": 230.99, "MAE_90D_pct": -13.14, "score_return_alignment_label": "high_mae_structural_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102", "trigger_id": "TRG-R3L16-C11-278280-STAGE2-20240102", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow axis applied.", "MFE_90D_pct": 1.19, "MAE_90D_pct": -28.35, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102", "trigger_id": "TRG-R3L16-C11-278280-STAGE2-20240102", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow axis applied.", "MFE_90D_pct": 1.19, "MAE_90D_pct": -28.35, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102", "trigger_id": "TRG-R3L16-C11-278280-STAGE2-20240102", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 0, "capacity_route_score": 1, "calloff_guard_score": -13}, "weighted_score_after": 55, "stage_label_after": "Stage1/Reject", "changed_components": ["orderbook_delivery_score", "capacity_route_score", "calloff_guard_score"], "component_delta_explanation": "electrolyte recovery theme without delivery/customer proof should be capped", "MFE_90D_pct": 1.19, "MAE_90D_pct": -28.35, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102", "trigger_id": "TRG-R3L16-C11-278280-STAGE2-20240102", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 0, "capacity_route_score": 1, "calloff_guard_score": -13}, "weighted_score_after": 55, "stage_label_after": "Stage1/Reject", "changed_components": ["orderbook_delivery_score", "capacity_route_score", "calloff_guard_score"], "component_delta_explanation": "electrolyte recovery theme without delivery/customer proof should be capped", "MFE_90D_pct": 1.19, "MAE_90D_pct": -28.35, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L16-C11-278280-CHUNBO-ELECTROLYTE-RECOVERY-FALSE-20240102", "trigger_id": "TRG-R3L16-C11-278280-STAGE2-20240102", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 0, "capacity_route_score": 1, "calloff_guard_score": -13}, "weighted_score_after": 53, "stage_label_after": "Stage1/Reject", "changed_components": ["calloff_guard_score", "orderbook_delivery_score", "thesis_break_score"], "component_delta_explanation": "electrolyte recovery theme without delivery/customer proof should be capped Counterexample guard is slightly stricter on weak orderbook proof.", "MFE_90D_pct": 1.19, "MAE_90D_pct": -28.35, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102", "trigger_id": "TRG-R3L16-C11-393890-STAGE2-20240102", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow-false-positive", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage3-Yellow-false-positive", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow axis applied.", "MFE_90D_pct": 10.06, "MAE_90D_pct": -33.92, "score_return_alignment_label": "orderbook_rerating_broken_by_utilization_4C", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102", "trigger_id": "TRG-R3L16-C11-393890-STAGE2-20240102", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow-false-positive", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage3-Yellow-false-positive", "changed_components": [], "component_delta_explanation": "P0/P0b proxy only; no shadow axis applied.", "MFE_90D_pct": 10.06, "MAE_90D_pct": -33.92, "score_return_alignment_label": "orderbook_rerating_broken_by_utilization_4C", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102", "trigger_id": "TRG-R3L16-C11-393890-STAGE2-20240102", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow-false-positive", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 1, "capacity_route_score": 0, "calloff_guard_score": -15, "thesis_break_score": -10}, "weighted_score_after": 57, "stage_label_after": "Stage2-Risk/4C-Watch", "changed_components": ["orderbook_delivery_score", "capacity_route_score", "calloff_guard_score"], "component_delta_explanation": "pure separator exposure must route utilization/order drawdown into guard rather than positive rerating", "MFE_90D_pct": 10.06, "MAE_90D_pct": -33.92, "score_return_alignment_label": "orderbook_rerating_broken_by_utilization_4C", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102", "trigger_id": "TRG-R3L16-C11-393890-STAGE2-20240102", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow-false-positive", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 1, "capacity_route_score": 0, "calloff_guard_score": -15, "thesis_break_score": -10}, "weighted_score_after": 57, "stage_label_after": "Stage2-Risk/4C-Watch", "changed_components": ["orderbook_delivery_score", "capacity_route_score", "calloff_guard_score"], "component_delta_explanation": "pure separator exposure must route utilization/order drawdown into guard rather than positive rerating", "MFE_90D_pct": 10.06, "MAE_90D_pct": -33.92, "score_return_alignment_label": "orderbook_rerating_broken_by_utilization_4C", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L16-C11-393890-WCP-SEPARATOR-ORDERBOOK-THESIS-BREAK-20240102", "trigger_id": "TRG-R3L16-C11-393890-STAGE2-20240102", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow-false-positive", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "orderbook_delivery_score": 1, "capacity_route_score": 0, "calloff_guard_score": -15, "thesis_break_score": -10}, "weighted_score_after": 55, "stage_label_after": "Stage2-Risk/4C-Watch", "changed_components": ["calloff_guard_score", "orderbook_delivery_score", "thesis_break_score"], "component_delta_explanation": "pure separator exposure must route utilization/order drawdown into guard rather than positive rerating Counterexample guard is slightly stricter on weak orderbook proof.", "MFE_90D_pct": 10.06, "MAE_90D_pct": -33.92, "score_return_alignment_label": "orderbook_rerating_broken_by_utilization_4C", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_delivery_quality_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,+2,+2,"Promote only when orderbook/capacity evidence has visible delivery or customer quality.","Raises Enchem/TCC without lifting Chunbo/WCP false positives.","TRG-R3L16-C11-348370-STAGE2-20240102|TRG-R3L16-C11-002710-STAGE2-20230323",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_calloff_utilization_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,-3,-3,"Cap orderbook rerating when customer call-off/utilization risk dominates.","Blocks Chunbo/WCP false positives while preserving high-MFE orderbook cases.","TRG-R3L16-C11-278280-STAGE2-20240102|TRG-R3L16-C11-393890-STAGE2-20240102|TRG-R3L16-C11-393890-4C-WATCH-20240722",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_price_only_peak_watch_not_full_4B,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,true,true,0,"Keep existing full 4B non-price requirement; use price-only blowoff as watch overlay.","Enchem price-only proximity captured risk, but not a full 4B thesis-break evidence row.","TRG-R3L16-C11-348370-4B-WATCH-20240408",4,4,2,medium,axis_strengthening,"strengthens existing full_4b_requires_non_price_evidence"

```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "16", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "scheduled_round": "R3", "scheduled_loop": 16, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "estimated +58: four new R3 C11 symbols/families, two positives, two counterexamples, one price-only 4B watch, one 4C watch; wrong_round_penalty=0", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["C11_orderbook_without_delivery_false_positive", "pure_separator_utilization_4C_too_late", "price_only_4B_watch_not_full_4B", "C11_capacity_orderbook_stage2_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.  
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

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
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 16
next_round = R4
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Manifest validation comes from `atlas/manifest.json`.
- Stock profiles used:
  - `atlas/symbol_profiles/348/348370.json`
  - `atlas/symbol_profiles/002/002710.json`
  - `atlas/symbol_profiles/278/278280.json`
  - `atlas/symbol_profiles/393/393890.json`
- Price rows used:
  - `atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv`
- All prices are raw/unadjusted marcap-derived OHLC. This report is a historical calibration artifact only.
