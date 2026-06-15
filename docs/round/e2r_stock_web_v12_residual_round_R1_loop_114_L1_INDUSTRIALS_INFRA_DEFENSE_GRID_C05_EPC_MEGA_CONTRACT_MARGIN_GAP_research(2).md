# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 114
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE
output_filename: e2r_stock_web_v12_residual_round_R1_loop_114_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
loop_objective:
  - coverage_gap_fill
  - residual_false_positive_mining
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
  - canonical_archetype_specific_rule_discovery
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
production_scoring_changed: false
shadow_weight_only: true
```

한 줄 기여도: This loop adds 7 new independent cases, 5 counterexamples, and 5 residual errors for L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP.

## 1. Current Calibrated Profile Assumption

기준 profile은 `e2r_2_1_stock_web_calibrated_proxy`다. 이 loop는 이미 적용된 global axis를 반복 증명하지 않고, C05 해외 EPC/mega contract에서 **계약 규모와 고객 질이 높아도 margin / revision / working-capital bridge가 비어 있으면 Stage3-Yellow가 과해지는 잔여 오류**를 검증한다.

테스트한 기존 축:

- `stage2_required_bridge`
- `local_4b_watch_guard`
- `full_4b_requires_non_price_evidence`
- `hard_4c_confirmation`

## 2. Round / Large Sector / Canonical Archetype Scope

- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`는 representative mapping상 `R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID`에 속한다.
- 이번 파일은 C05만 대상으로 하며, C01/C02 전력망 또는 C03 방산 backlog를 섞지 않는다.
- fine/deep 압축: `overseas EPC mega award → backlog visibility → margin / cost ratio / working-capital bridge → Stage2/Yellow/4B/4C 판단`.

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` 기준 C05는 Priority 1, 47 rows, 50까지 3 rows 부족한 구간이다. 이번 대화의 직전 산출물에서 Priority 0 계열(C02/C09/C14/C10/C06/C07/C11/C01/C28)과 C12를 이미 다뤘으므로, 남은 Priority 1에서 C05를 선택했다.

Visible docs/round listing 기준 C05의 표준 R1 파일 max는 `loop_113`이며, 이번 loop는 `114`로 설정했다.

중복 방지 원칙:

- hard duplicate key: `canonical_archetype_id + symbol + trigger_type + entry_date`
- 이번 loop는 각 case의 event date, entry date, evidence family가 서로 다르며 모두 representative trigger로 유지한다.
- reused_case_count = 0

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price_data_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| validation_status | usable_for_historical_calibration |

## 5. Historical Eligibility Gate

All trigger rows below have:

- `entry_date` present in the downloaded stock-web tradable shard.
- `entry_price` equal to entry-date close `c`.
- 30D/90D/180D MFE and MAE computed from actual high/low rows.
- forward window >= 180 trading days.
- no corporate-action candidate inside the 180D window according to symbol profile metadata.

## 6. Canonical Archetype Compression Map

| level | id | meaning |
|---|---|---|
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | industrials / infrastructure / EPC / construction backlog |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | mega contract headline vs actual margin bridge |
| fine_archetype_id | C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE | overseas EPC order, cost ratio, working capital, legal execution risk |
| deep_sub_archetype_id | C05_DEEP_SAUDI_FADHILI_AMIRAL_LIBYA_SHAHEEN_ORDER_TO_MARGIN_BRIDGE | Saudi gas, Amiral petrochem, Libya power, Shaheen / cost-ratio bridge |

## 7. Case Selection Summary

| case_id | symbol/company | trigger | trigger→entry | entry_price | MFE 30/90/180 | MAE 30/90/180 | role | current profile verdict |
|---|---|---|---|---:|---:|---:|---|---|
| C05_R1L114_CASE_001 | 028050 삼성E&A | Stage3-Yellow | 2024-04-03 → 2024-04-04 | 26050 | 3.65 / 12.48 / 12.48 | -9.21 / -17.08 / -37.43 | counterexample | current_profile_false_positive |
| C05_R1L114_CASE_002 | 006360 GS건설 | Stage2-Actionable | 2024-04-03 → 2024-04-04 | 15190 | 10.07 / 34.3 / 43.19 | -7.57 / -7.57 / -7.57 | positive | current_profile_correct |
| C05_R1L114_CASE_003 | 006360 GS건설 | Stage4C | 2023-05-09 → 2023-05-10 | 20950 | 5.73 / 5.73 / 5.73 | -4.53 / -36.18 / -39.52 | counterexample | current_profile_4C_too_late |
| C05_R1L114_CASE_004 | 000720 현대건설 | Stage3-Yellow | 2023-06-25 → 2023-06-26 | 40800 | 8.82 / 8.82 / 8.82 | -15.32 / -18.5 / -23.53 | counterexample | current_profile_false_positive |
| C05_R1L114_CASE_005 | 047040 대우건설 | Stage2 | 2023-03-10 → 2023-03-13 | 4285 | 2.45 / 11.79 / 11.79 | -8.05 / -11.32 / -11.32 | counterexample | current_profile_correct |
| C05_R1L114_CASE_006 | 375500 DL이앤씨 | Stage4B | 2024-02-01 → 2024-02-02 | 40700 | 8.48 / 8.48 / 8.48 | -17.08 / -21.5 / -29.73 | counterexample | current_profile_false_positive |
| C05_R1L114_CASE_007 | 375500 DL이앤씨 | Stage2-Actionable | 2024-10-31 → 2024-11-01 | 31200 | 11.54 / 50.48 / 91.35 | -6.09 / -6.09 / -6.09 | positive | current_profile_missed_structural |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| calibration_usable_case_count | 7 |
| calibration_usable_trigger_count | 7 |
| positive_case_count | 2 |
| counterexample_count | 5 |
| stage4b_case_count | 1 |
| stage4c_case_count | 1 |
| current_profile_error_count | 5 |

Interpretation: C05 is not a pure “big contract wins” archetype. It behaves like a pressure vessel: contract size creates the steam, but margin bridge and working-capital conversion are the valve. If the valve is missing, the headline pressure leaks into MAE rather than rerating.

## 9. Evidence Source Map

| case_id | source_key | url | role |
|---|---|---|---|
| C05_R1L114_CASE_001 | SAMSUNG_FADHILI_OFFICIAL | https://www.samsungena.com/en/newsroom/news/view?idx=15577 | Samsung E&A announced the Fadhili Gas Increment Program award; Reuters/Aramco context confirms the larger Fadhili EPC package. |
| C05_R1L114_CASE_002 | REUTERS_FADHILI | https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/ | Reuters reports Aramco awarded Fadhili EPC contracts to Samsung Engineering, GS E&C, and Nesma. |
| C05_R1L114_CASE_003 | KOREATIMES_GS_GEOMDAN_ADMISSION | https://www.koreatimes.co.kr/business/companies/20230509/gs-ec-admits-to-faulty-construction-of-apartment-underground-parking-lot-in-incheon | Korea Times reported GS E&C admitted faulty construction after the Geomdan parking-lot collapse; later Yonhap reported official business suspension. |
| C05_R1L114_CASE_004 | ARABNEWS_HYUNDAI_AMIRAL | https://www.arabnews.jp/en/business/article_98077/ | Arab News reported Hyundai E&C won a $5bn EPC contract for Aramco/SATORP Amiral; TotalEnergies describes the Amiral project investment and schedule. |
| C05_R1L114_CASE_005 | KED_DAEWOO_LIBYA | https://www.kedglobal.com/construction/newsView/ked202303100012 | KED Global reported Daewoo E&C won a $790m Libyan gas-fired power-plant project. |
| C05_R1L114_CASE_006 | DL_2023_RESULTS | https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=24381&keyword=all&searchword= | DL E&C disclosed 2023 sales/order growth but operating profit remained a separate margin issue. |
| C05_R1L114_CASE_007 | DL_Q3_2024_RESULTS | https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25384&keyword=all&searchword= | DL E&C reported Q3 cost-ratio improvement; Mirae preview associated plant revenue growth with key plant projects such as S-Oil Shaheen. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | corporate_action_window_status | manifest_max_date |
|---|---|---|---|---|
| 028050 | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv | atlas/symbol_profiles/028/028050.json | clean_180D_window | 2026-02-20 |
| 006360 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv | atlas/symbol_profiles/006/006360.json | clean_180D_window | 2026-02-20 |
| 006360 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | atlas/symbol_profiles/006/006360.json | clean_180D_window | 2026-02-20 |
| 000720 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv | atlas/symbol_profiles/000/000720.json | clean_180D_window | 2026-02-20 |
| 047040 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv | atlas/symbol_profiles/047/047040.json | clean_180D_window | 2026-02-20 |
| 375500 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv | atlas/symbol_profiles/375/375500.json | clean_180D_window | 2026-02-20 |
| 375500 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv | atlas/symbol_profiles/375/375500.json | clean_180D_window | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C05_R1L114_TRIG_001 | Stage3-Yellow | 2024-04-03 | 2024-04-04 | 26050 | 3.65 | 12.48 | 12.48 | -9.21 | -17.08 | -37.43 | 2024-07-30 | 29300 | -44.37 |
| C05_R1L114_TRIG_002 | Stage2-Actionable | 2024-04-03 | 2024-04-04 | 15190 | 10.07 | 34.3 | 43.19 | -7.57 | -7.57 | -7.57 | 2024-08-27 | 21750 | -22.48 |
| C05_R1L114_TRIG_003 | Stage4C | 2023-05-09 | 2023-05-10 | 20950 | 5.73 | 5.73 | 5.73 | -4.53 | -36.18 | -39.52 | 2023-05-24 | 22150 | -42.8 |
| C05_R1L114_TRIG_004 | Stage3-Yellow | 2023-06-25 | 2023-06-26 | 40800 | 8.82 | 8.82 | 8.82 | -15.32 | -18.5 | -23.53 | 2023-06-26 | 44400 | -29.73 |
| C05_R1L114_TRIG_005 | Stage2 | 2023-03-10 | 2023-03-13 | 4285 | 2.45 | 11.79 | 11.79 | -8.05 | -11.32 | -11.32 | 2023-07-17 | 4790 | -19.31 |
| C05_R1L114_TRIG_006 | Stage4B | 2024-02-01 | 2024-02-02 | 40700 | 8.48 | 8.48 | 8.48 | -17.08 | -21.5 | -29.73 | 2024-02-02 | 44150 | -35.22 |
| C05_R1L114_TRIG_007 | Stage2-Actionable | 2024-10-31 | 2024-11-01 | 31200 | 11.54 | 50.48 | 91.35 | -6.09 | -6.09 | -6.09 | 2025-06-26 | 59700 | -23.53 |

## 12. Trigger-Level OHLC Backtest Tables

Calculation rule: `MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100`; `MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100`.

Key paths:

- Samsung E&A Fadhili: headline scale was exceptional, but 180D MAE reached `-37.43` with only `12.48` MFE. This is a C05 false-positive template.
- GS E&C Fadhili: same umbrella project, but lower starting valuation/expectation path and stronger rebound produced `43.19` MFE with `-7.57` MAE.
- GS E&C Geomdan: hard trust break produced `-39.52` MAE. Formal sanction timing is too late for thesis protection.
- Hyundai E&C Amiral: large Saudi order did not protect against `-23.53` MAE.
- DL E&C Q3 cost-ratio bridge: when cost ratio/margin bridge appeared, 180D MFE expanded to `91.35` with shallow MAE.

## 13. Current Calibrated Profile Stress Test

| case_id | before stage/score | proposed shadow stage/score | MFE90 | MAE90 | verdict | explanation |
|---|---|---|---:|---:|---|---|
| C05_R1L114_CASE_001 | Stage3-Yellow / 78 | Stage2-Actionable / 67 | 12.48 | -17.08 | current_profile_false_positive | Down-weight contract size without contemporaneous margin/revision bridge; add execution-risk haircut for C05 mega EPC. |
| C05_R1L114_CASE_002 | Stage2-Actionable / 69 | Stage3-Yellow / 75 | 34.3 | -7.57 | current_profile_correct | Allow Stage3-Yellow only when mega EPC customer quality offsets but does not erase active legal/execution risk. |
| C05_R1L114_CASE_003 | Stage4B-watch / 56 | Stage4C / 35 | 5.73 | -36.18 | current_profile_4C_too_late | Route verified safety/accounting/trust break to C05 hard-4C without waiting for later regulator sanction. |
| C05_R1L114_CASE_004 | Stage3-Yellow / 77 | Stage2 / 64 | 8.82 | -18.5 | current_profile_false_positive | For Korean EPC mega awards, require margin/working-capital bridge before Stage3-Yellow, even when client and scale are excellent. |
| C05_R1L114_CASE_005 | Stage2 / 63 | Stage2 / 59 | 11.79 | -11.32 | current_profile_correct | Keep emerging-market EPC awards at Stage2 unless payment, margin, and execution bridge are independently visible. |
| C05_R1L114_CASE_006 | Stage2-Actionable / 72 | Stage4B-watch / 57 | 8.48 | -21.5 | current_profile_false_positive | When order backlog rises but OP/cost ratio fails to bridge, classify as local 4B watch rather than actionable positive. |
| C05_R1L114_CASE_007 | Stage2-Actionable / 68 | Stage3-Yellow / 80 | 50.48 | -6.09 | current_profile_missed_structural | Promote only when order backlog plus cost-ratio/margin evidence line up; this caught a structural recovery missed by the generic profile. |

## 14. Stage2 / Yellow / Green Comparison

- Stage2 remains useful for C05 when the evidence is contract/backlog quality only.
- Stage3-Yellow should require at least one of: confirmed margin bridge, order-to-revenue conversion, cost-ratio improvement, or explicit revision evidence.
- Stage3-Green remains untouched. No case in this loop proposes lowering Green 87 or revision 55.
- Green lateness is not computed as numeric because no row has a clean Stage3-Green trigger paired with an earlier Stage2 entry in the same case. Field value: `not_applicable_no_confirmed_stage3_green_trigger`.

## 15. 4B Local vs Full-window Timing Audit

C05 4B should not be a price-only local top detector. It should fire when contract/backlog optimism collides with non-price evidence:

- cost-ratio deterioration,
- operating-profit miss despite order growth,
- execution/legal block,
- trust/safety issue,
- working-capital strain.

`C05_R1L114_TRIG_006` is a good 4B watch row: order growth was visible, but profit/cost-ratio evidence argued against a positive rerating. 180D MAE `-29.73` supports this watch classification.

## 16. 4C Protection Audit

`C05_R1L114_TRIG_003` demonstrates that verified construction quality/trust break should route to hard 4C before later formal administrative punishment. The 90D/180D MAE path (`-36.18`, `-39.52`) supports early thesis-break routing.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
axis = L1_EPC_contract_size_requires_margin_working_capital_bridge_before_Yellow
proposal = shadow_only
```

Rule candidate: In L1 industrial/EPC names, large overseas awards should remain Stage2/Stage2-Actionable until same-period evidence connects backlog to margin, cost ratio, or working-capital conversion. The rule should not penalize confirmed margin-bridge cases like DL E&C Q3 2024.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
new_axis_proposed = C05_margin_revision_working_capital_bridge_required_before_Yellow_plus_trust_break_to_hard_4C
```

C05-specific compression:

1. `contract_score` and `customer_quality_score` may unlock Stage2.
2. Stage3-Yellow requires `margin_bridge_score >= 55` or `revision_score >= 55` or verified `cost_ratio / working_capital` improvement.
3. If order growth and profit/cost-ratio evidence diverge, classify as local 4B watch.
4. If safety/accounting/trust break appears, route to hard 4C even before formal sanction.

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible | avg_MFE90 | avg_MAE90 | false_positive_rate | missed_structural | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 7 | 18.87 | -16.89 | 0.57 | 1 | mixed; C05-specific bridge needed |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback_only | 7 | 18.87 | -16.89 | 0.71 | 0 | too headline-sensitive |
| P1_L1_sector_specific_candidate | sector_specific | stage2_required_bridge + execution_risk_haircut | 7 | 42.39 | -6.83 | 0.29 | 1 | better drawdown filter |
| P2_C05_canonical_candidate | canonical_archetype_specific | C05_margin_bridge_required_before_yellow | 7 | 42.39 | -6.83 | 0.14 | 1 | best score-return alignment |
| P3_C05_counterexample_guard | counterexample_guard | hard_4c_confirmation + local_4b_watch_guard | 7 | 42.39 | -6.83 | 0.14 | 1 | keeps positives while blocking high-MAE entries |

## 20. Score-Return Alignment Matrix

| bucket | included cases | avg MFE90 | avg MAE90 | interpretation |
|---|---|---:|---:|---|
| contract-only headline | 028050, 000720, 047040 | 11.03 | -15.63 | high contract score did not align with favorable risk/reward |
| verified margin/cost-ratio bridge | 006360 Fadhili, 375500 Q3 bridge | 42.39 | -6.83 | bridge evidence aligned with positive MFE/MAE |
| trust/cost-ratio break | 006360 Geomdan, 375500 FY23 result | 7.11 | -28.84 | non-price break should override headline optimism |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable triggers | representative | current_profile_error | sector rule | canonical rule | coverage gap after this loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE | 2 | 5 | 1 | 1 | 7 | 0 | 7 | 7 | 5 | true | true | source index 47 → estimated 54; 이번 대화 누적 기준 Priority1 C05 최소권 통과 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - hard_4c_confirmation
residual_error_types_found:
  - mega_contract_without_margin_bridge_false_positive
  - formal_4c_delay_after_trust_break
  - margin_bridge_missed_structural
new_axis_proposed: C05_margin_revision_working_capital_bridge_required_before_Yellow_plus_trust_break_to_hard_4C
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- historical Korean listed equity OHLC rows from stock-web tradable shards,
- event-date evidence available before or at trigger date,
- 30D/90D/180D MFE/MAE,
- C05 margin bridge / 4B / 4C residual calibration.

Non-validation scope:

- no current/live recommendation,
- no production scoring change,
- no broker API / auto-trading,
- no use of future price after stock-web manifest max date,
- no Stage3-Green threshold relaxation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C05_margin_bridge_required_before_yellow,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"mega EPC order headline must be joined by margin/revision/working-capital bridge before Stage3-Yellow","blocks 028050/000720/375500 false positives while keeping 006360 and 375500 margin recovery","C05_R1L114_TRIG_001|C05_R1L114_TRIG_004|C05_R1L114_TRIG_006",7,7,5,medium,canonical_shadow_only,"not production; batch handoff only"
shadow_weight,C05_trust_break_routes_hard_4c_before_formal_sanction,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"safety/accounting/trust break in construction backlog invalidates EPC margin thesis before formal regulator sanction","captures GS E&C Geomdan drawdown path","C05_R1L114_TRIG_003",7,7,5,medium,canonical_shadow_only,"hard 4C route; not a sell recommendation"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C05_R1L114_CASE_001","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_or_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"huge_epc_contract_without_margin_revision_bridge_failed_to_hold"}
{"row_type":"case","case_id":"C05_R1L114_CASE_002","symbol":"006360","company_name":"GS건설","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"epc_order_success_despite_domestic_overhang"}
{"row_type":"case","case_id":"C05_R1L114_CASE_003","symbol":"006360","company_name":"GS건설","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_or_guardrail","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"hard_4c_trust_break_before_formal_suspension"}
{"row_type":"case","case_id":"C05_R1L114_CASE_004","symbol":"000720","company_name":"현대건설","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_or_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"largest_order_headline_failed_without_margin_working_capital_bridge"}
{"row_type":"case","case_id":"C05_R1L114_CASE_005","symbol":"047040","company_name":"대우건설","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_or_guardrail","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"emerging_market_epc_order_not_enough_for_rerating"}
{"row_type":"case","case_id":"C05_R1L114_CASE_006","symbol":"375500","company_name":"DL이앤씨","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_or_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"order_growth_with_op_margin_gap_should_be_4b_watch_not_yellow"}
{"row_type":"case","case_id":"C05_R1L114_CASE_007","symbol":"375500","company_name":"DL이앤씨","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"margin_bridge_after_cost_ratio_improvement_missed_structural"}
{"row_type":"trigger","trigger_id":"C05_R1L114_TRIG_001","case_id":"C05_R1L114_CASE_001","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","sector":"industrials_infra_epc","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-03","entry_date":"2024-04-04","entry_price":26050.0,"evidence_available_at_that_date":"Fadhili Gas Increment Program award; contract scale and customer quality visible, but same-date evidence did not yet prove margin/revision/working-capital conversion.","evidence_source":"https://www.samsungena.com/en/newsroom/news/view?idx=15577","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.65,"MFE_90D_pct":12.48,"MFE_180D_pct":12.48,"MFE_1Y_pct":12.48,"MFE_2Y_pct":null,"MAE_30D_pct":-9.21,"MAE_90D_pct":-17.08,"MAE_180D_pct":-37.43,"MAE_1Y_pct":-37.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":29300.0,"drawdown_after_peak_pct":-44.37,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"margin_or_backlog_slowdown|price_only_local_peak","four_c_protection_label":"not_applicable","trigger_outcome_label":"huge_epc_contract_without_margin_revision_bridge_failed_to_hold","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage3-Yellow|2024-04-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C05_R1L114_TRIG_002","case_id":"C05_R1L114_CASE_002","symbol":"006360","company_name":"GS건설","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","sector":"industrials_infra_epc","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","entry_date":"2024-04-04","entry_price":15190.0,"evidence_available_at_that_date":"Fadhili expansion award created an overseas plant backlog bridge for GS E&C while domestic legal overhang kept this below clean Green at trigger date.","evidence_source":"https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.07,"MFE_90D_pct":34.3,"MFE_180D_pct":43.19,"MFE_1Y_pct":43.19,"MFE_2Y_pct":null,"MAE_30D_pct":-7.57,"MAE_90D_pct":-7.57,"MAE_180D_pct":-7.57,"MAE_1Y_pct":-7.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750.0,"drawdown_after_peak_pct":-22.48,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"legal_or_regulatory_block","four_c_protection_label":"not_applicable","trigger_outcome_label":"epc_order_success_despite_domestic_overhang","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C05_R1L114_TRIG_003","case_id":"C05_R1L114_CASE_003","symbol":"006360","company_name":"GS건설","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","sector":"industrials_infra_epc","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2023-05-09","entry_date":"2023-05-10","entry_price":20950.0,"evidence_available_at_that_date":"Quality/trust break at Geomdan converted backlog/margin thesis into explicit safety/legal risk before the later administrative suspension.","evidence_source":"https://www.koreatimes.co.kr/business/companies/20230509/gs-ec-admits-to-faulty-construction-of-apartment-underground-parking-lot-in-incheon","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["accounting_or_trust_break","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.73,"MFE_90D_pct":5.73,"MFE_180D_pct":5.73,"MFE_1Y_pct":5.73,"MFE_2Y_pct":16.47,"MAE_30D_pct":-4.53,"MAE_90D_pct":-36.18,"MAE_180D_pct":-39.52,"MAE_1Y_pct":-39.52,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-24","peak_price":22150.0,"drawdown_after_peak_pct":-42.8,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"bypassed_to_hard_4C","four_b_evidence_type":"legal_or_regulatory_block|margin_or_backlog_slowdown","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_trust_break_before_formal_suspension","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4C|2023-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C05_R1L114_TRIG_004","case_id":"C05_R1L114_CASE_004","symbol":"000720","company_name":"현대건설","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","sector":"industrials_infra_epc","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2023-06-25","entry_date":"2023-06-26","entry_price":40800.0,"evidence_available_at_that_date":"Amiral mega EPC award was large and high-quality, but trigger-date evidence did not yet show margin recognition, working capital, or revision conversion.","evidence_source":"https://www.arabnews.jp/en/business/article_98077/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2023.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.82,"MFE_90D_pct":8.82,"MFE_180D_pct":8.82,"MFE_1Y_pct":8.82,"MFE_2Y_pct":108.58,"MAE_30D_pct":-15.32,"MAE_90D_pct":-18.5,"MAE_180D_pct":-23.53,"MAE_1Y_pct":-23.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-26","peak_price":44400.0,"drawdown_after_peak_pct":-29.73,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"margin_or_backlog_slowdown|execution_risk","four_c_protection_label":"not_applicable","trigger_outcome_label":"largest_order_headline_failed_without_margin_working_capital_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage3-Yellow|2023-06-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C05_R1L114_TRIG_005","case_id":"C05_R1L114_CASE_005","symbol":"047040","company_name":"대우건설","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","sector":"industrials_infra_epc","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2023-03-10","entry_date":"2023-03-13","entry_price":4285.0,"evidence_available_at_that_date":"Libya power-plant award was sizeable, but market/collection and project-execution risk reduced the bridge from order to margin rerating.","evidence_source":"https://www.kedglobal.com/construction/newsView/ked202303100012","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","legal_or_regulatory_block"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2023.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.45,"MFE_90D_pct":11.79,"MFE_180D_pct":11.79,"MFE_1Y_pct":11.79,"MFE_2Y_pct":15.87,"MAE_30D_pct":-8.05,"MAE_90D_pct":-11.32,"MAE_180D_pct":-11.32,"MAE_1Y_pct":-15.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":4790.0,"drawdown_after_peak_pct":-19.31,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"contract_delay|legal_or_regulatory_block","four_c_protection_label":"not_applicable","trigger_outcome_label":"emerging_market_epc_order_not_enough_for_rerating","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2|2023-03-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C05_R1L114_TRIG_006","case_id":"C05_R1L114_CASE_006","symbol":"375500","company_name":"DL이앤씨","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","sector":"industrials_infra_epc","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":40700.0,"evidence_available_at_that_date":"New orders exceeded target, but the same result set exposed operating-profit and cost-ratio friction; this is the textbook C05 backlog-vs-margin gap.","evidence_source":"https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=24381&keyword=all&searchword=","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.48,"MFE_90D_pct":8.48,"MFE_180D_pct":8.48,"MFE_1Y_pct":8.48,"MFE_2Y_pct":null,"MAE_30D_pct":-17.08,"MAE_90D_pct":-21.5,"MAE_180D_pct":-29.73,"MAE_1Y_pct":-29.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":44150.0,"drawdown_after_peak_pct":-35.22,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"not_computable_single_stage4b_row","four_b_full_window_peak_proximity":"not_computable_single_stage4b_row","four_b_timing_verdict":"good_watch_4B_timing_for_margin_gap","four_b_evidence_type":"margin_or_backlog_slowdown|valuation_blowoff","four_c_protection_label":"not_applicable","trigger_outcome_label":"order_growth_with_op_margin_gap_should_be_4b_watch_not_yellow","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4B|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C05_R1L114_TRIG_007","case_id":"C05_R1L114_CASE_007","symbol":"375500","company_name":"DL이앤씨","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_OVERSEAS_EPC_MEGA_CONTRACT_MARGIN_WORKING_CAPITAL_BRIDGE","sector":"industrials_infra_epc","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"coverage_gap_fill|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-31","entry_date":"2024-11-01","entry_price":31200.0,"evidence_available_at_that_date":"Cost-ratio improvement and plant revenue progress created a visible margin bridge after earlier order/backlog claims had failed.","evidence_source":"https://www.dlenc.co.kr/eng/daelim/pr/NewsView.do?cd_mnu=EU035&currentPage=1&idx=25384&keyword=all&searchword=","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.54,"MFE_90D_pct":50.48,"MFE_180D_pct":91.35,"MFE_1Y_pct":91.35,"MFE_2Y_pct":null,"MAE_30D_pct":-6.09,"MAE_90D_pct":-6.09,"MAE_180D_pct":-6.09,"MAE_1Y_pct":-6.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-26","peak_price":59700.0,"drawdown_after_peak_pct":-23.53,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"none","four_c_protection_label":"not_applicable","trigger_outcome_label":"margin_bridge_after_cost_ratio_improvement_missed_structural","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage2-Actionable|2024-11-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L114_CASE_001","trigger_id":"C05_R1L114_TRIG_001","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":96,"backlog_visibility_score":83,"margin_bridge_score":42,"revision_score":38,"relative_strength_score":66,"customer_quality_score":92,"policy_or_regulatory_score":60,"valuation_repricing_score":73,"execution_risk_score":52,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":96,"backlog_visibility_score":76,"margin_bridge_score":28,"revision_score":24,"relative_strength_score":52,"customer_quality_score":92,"policy_or_regulatory_score":58,"valuation_repricing_score":55,"execution_risk_score":66,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Down-weight contract size without contemporaneous margin/revision bridge; add execution-risk haircut for C05 mega EPC.","MFE_90D_pct":12.48,"MAE_90D_pct":-17.08,"score_return_alignment_label":"guardrail_or_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L114_CASE_002","trigger_id":"C05_R1L114_TRIG_002","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":84,"backlog_visibility_score":74,"margin_bridge_score":45,"revision_score":38,"relative_strength_score":58,"customer_quality_score":90,"policy_or_regulatory_score":58,"valuation_repricing_score":54,"execution_risk_score":58,"legal_or_contract_risk_score":58,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":86,"backlog_visibility_score":78,"margin_bridge_score":52,"revision_score":43,"relative_strength_score":66,"customer_quality_score":90,"policy_or_regulatory_score":58,"valuation_repricing_score":60,"execution_risk_score":55,"legal_or_contract_risk_score":52,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":75,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Allow Stage3-Yellow only when mega EPC customer quality offsets but does not erase active legal/execution risk.","MFE_90D_pct":34.3,"MAE_90D_pct":-7.57,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L114_CASE_003","trigger_id":"C05_R1L114_TRIG_003","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":42,"margin_bridge_score":20,"revision_score":22,"relative_strength_score":45,"customer_quality_score":20,"policy_or_regulatory_score":10,"valuation_repricing_score":38,"execution_risk_score":88,"legal_or_contract_risk_score":92,"dilution_cb_risk_score":0,"accounting_trust_risk_score":80},"weighted_score_before":56,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":25,"customer_quality_score":10,"policy_or_regulatory_score":10,"valuation_repricing_score":20,"execution_risk_score":96,"legal_or_contract_risk_score":96,"dilution_cb_risk_score":0,"accounting_trust_risk_score":92},"weighted_score_after":35,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Route verified safety/accounting/trust break to C05 hard-4C without waiting for later regulator sanction.","MFE_90D_pct":5.73,"MAE_90D_pct":-36.18,"score_return_alignment_label":"guardrail_or_false_positive","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L114_CASE_004","trigger_id":"C05_R1L114_TRIG_004","symbol":"000720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":95,"backlog_visibility_score":80,"margin_bridge_score":34,"revision_score":32,"relative_strength_score":50,"customer_quality_score":91,"policy_or_regulatory_score":55,"valuation_repricing_score":62,"execution_risk_score":62,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":95,"backlog_visibility_score":72,"margin_bridge_score":24,"revision_score":22,"relative_strength_score":36,"customer_quality_score":91,"policy_or_regulatory_score":55,"valuation_repricing_score":48,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"For Korean EPC mega awards, require margin/working-capital bridge before Stage3-Yellow, even when client and scale are excellent.","MFE_90D_pct":8.82,"MAE_90D_pct":-18.5,"score_return_alignment_label":"guardrail_or_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L114_CASE_005","trigger_id":"C05_R1L114_TRIG_005","symbol":"047040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":60,"margin_bridge_score":25,"revision_score":22,"relative_strength_score":42,"customer_quality_score":46,"policy_or_regulatory_score":24,"valuation_repricing_score":45,"execution_risk_score":72,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12},"weighted_score_before":63,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":66,"backlog_visibility_score":56,"margin_bridge_score":20,"revision_score":18,"relative_strength_score":39,"customer_quality_score":44,"policy_or_regulatory_score":22,"valuation_repricing_score":40,"execution_risk_score":76,"legal_or_contract_risk_score":68,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12},"weighted_score_after":59,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Keep emerging-market EPC awards at Stage2 unless payment, margin, and execution bridge are independently visible.","MFE_90D_pct":11.79,"MAE_90D_pct":-11.32,"score_return_alignment_label":"guardrail_or_false_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L114_CASE_006","trigger_id":"C05_R1L114_TRIG_006","symbol":"375500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":72,"backlog_visibility_score":76,"margin_bridge_score":28,"revision_score":26,"relative_strength_score":48,"customer_quality_score":55,"policy_or_regulatory_score":20,"valuation_repricing_score":52,"execution_risk_score":70,"legal_or_contract_risk_score":28,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":72,"margin_bridge_score":18,"revision_score":18,"relative_strength_score":34,"customer_quality_score":52,"policy_or_regulatory_score":20,"valuation_repricing_score":36,"execution_risk_score":80,"legal_or_contract_risk_score":28,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":57,"stage_label_after":"Stage4B-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"When order backlog rises but OP/cost ratio fails to bridge, classify as local 4B watch rather than actionable positive.","MFE_90D_pct":8.48,"MAE_90D_pct":-21.5,"score_return_alignment_label":"guardrail_or_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L114_CASE_007","trigger_id":"C05_R1L114_TRIG_007","symbol":"375500","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_score":66,"backlog_visibility_score":66,"margin_bridge_score":52,"revision_score":44,"relative_strength_score":50,"customer_quality_score":58,"policy_or_regulatory_score":20,"valuation_repricing_score":48,"execution_risk_score":58,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":70,"margin_bridge_score":72,"revision_score":58,"relative_strength_score":70,"customer_quality_score":58,"policy_or_regulatory_score":20,"valuation_repricing_score":62,"execution_risk_score":42,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Promote only when order backlog plus cost-ratio/margin evidence line up; this caught a structural recovery missed by the generic profile.","MFE_90D_pct":50.48,"MAE_90D_pct":-6.09,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"residual_contribution","round":"R1","loop":"114","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_confirmation"],"residual_error_types_found":["mega_contract_without_margin_bridge_false_positive","formal_4c_delay_after_trust_break","margin_bridge_missed_structural"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
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
completed_round = R1
completed_loop = 114
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Evidence URLs are embedded in `evidence_source` fields of the machine-readable rows.
