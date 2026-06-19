# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
file_name: e2r_stock_web_v12_residual_round_R1_loop_209_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
round: R1
loop: 209
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD
selected_priority_bucket: Priority 1 / balance-quality reinforcement + Priority 0 URL/proxy quality repair
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
```

This loop adds **5 new independent cases**, **3 counterexamples**, and **3 residual errors** for `L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE`. The immediate research focus is not another generic proof that Stage2 is earlier than Green. The focus is narrower: in C01, an order/backlog headline is only a loaded ship on the slipway; it becomes investable calibration evidence only when the hull actually floats through margin, working capital, and FCF conversion.

## 1. Current Calibrated Profile Assumption

Current proxy profile: `e2r_2_1_stock_web_calibrated_proxy`.

Applied global axes treated as already present:

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

The loop tests those axes only where C01 has residual error: backlog-to-margin timing, working-capital conversion, parent/subsidiary lag, and price-only local 4B.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R1 |
| selected_loop | 209 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE |
| fine_archetype_id | C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD |
| loop_objective | `counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test` |
| hard round-sector gate | pass |

C01 maps to R1/L1. This is therefore not an R13 cross-redteam file and not an L2 grid/datacenter file.

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` reports that every C01~C32 archetype already exceeds the old 30/50/80 row gates, so the next objective is quality repair rather than raw row count. Priority 1 includes C01 with the specific shortage: **backlog가 실제 FCF로 전환되지 않는 반례 보강**.

Immediate anti-repeat note: the prior local outputs in this run stream used C15 and C05. This loop therefore moves to C01 inside the same Priority 1 balance-quality bucket.

Duplicate gate applied:

| duplicate dimension | status |
|---|---|
| same canonical + symbol + trigger_type + entry_date | avoided |
| new symbol count inside this loop | 5 |
| new trigger family count | 6 |
| counterexample count | 3 |
| 4B overlay path | 1 price-only local 4B watch row |
| reused case count | 0 |

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| source | Songdaiki/stock-web |
| source_url | https://github.com/Songdaiki/stock-web |
| manifest | `atlas/manifest.json` |
| schema | `atlas/schema.json` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| min_date | `1995-05-02` |
| max_date | `2026-02-20` |
| tradable_row_count | `14,354,401` |
| symbol_count | `5,414` |

The schema formula used here is the stock-web canonical formula:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| symbol | entry window | 180D forward rows | corporate action window | calibration status |
|---|---:|---:|---|---|
| 010140 | 2023-04-28 onward | 180 | clean_180D_window | usable |
| 082740 | 2023-05-31 onward | 180 | clean_180D_window | usable |
| 010620 | 2023-06-05 onward | 180 | clean_180D_window | usable |
| 329180 | 2023-07-28 onward | 180 | clean_180D_window | usable |
| 009540 | 2023-07-28 onward | 180 | clean_180D_window | usable |
| 010620 4B overlay | 2023-08-02 onward | 180 | clean_180D_window | usable as overlay, not representative |

All representative trigger rows include entry_date, entry_price, canonical Stage trigger_type, and complete 30D/90D/180D MFE/MAE fields.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD
```

Compression rule tested in this loop:

```text
order/backlog headline
  -> backlog quality and customer/ship type
  -> actual margin bridge
  -> working-capital / FCF conversion
  -> recurring profitability
```

A backlog headline without the middle two steps is a bridge drawn on paper. It may explain why investors look, but not why a Stage3-Green label should be granted.

## 7. Case Selection Summary

| symbol | company | trigger_type | entry_date | entry_price | role | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---|---|---:|---:|---|---:|---:|---:|---:|---|
| 010140 | 삼성중공업 | Stage2-Actionable | 2023-04-28 | 5,680 | positive | 66.73% | -5.81% | 66.73% | -5.81% | current_profile_correct |
| 082740 | 한화엔진 | Stage2-Actionable | 2023-05-31 | 8,740 | positive | 45.88% | -5.03% | 45.88% | -13.50% | current_profile_correct |
| 010620 | HD현대미포 | Stage2 | 2023-06-05 | 81,900 | counterexample | 18.07% | -10.87% | 18.07% | -27.23% | current_profile_false_positive |
| 329180 | HD현대중공업 | Stage3-Yellow | 2023-07-28 | 135,700 | counterexample | 3.24% | -25.20% | 3.24% | -25.20% | current_profile_too_early |
| 009540 | HD한국조선해양 | Stage3-Yellow | 2023-07-28 | 123,700 | counterexample | 1.46% | -28.05% | 4.28% | -28.05% | current_profile_too_early |

## 8. Positive vs Counterexample Balance

| bucket | count | interpretation |
|---|---:|---|
| positive structural success | 2 | Samsung Heavy and Hanwha Engine show backlog quality + margin bridge alignment. |
| counterexample / delayed rerating | 3 | Mipo, HD Hyundai Heavy, and KSOE show backlog or profit headlines that were too early for a 180D entry window. |
| 4B overlay | 1 | Mipo local peak shows why price-only 4B should remain watch-only. |
| 4C | 0 | No clean hard thesis-break/cancellation row found in this loop. |

## 9. Evidence Source Map

| symbol | company | trigger_date | evidence_source | evidence summary |
|---|---|---:|---|---|
| 010140 | 삼성중공업 | 2023-04-27 | https://www.yna.co.kr/view/AKR20230427139501527 | 1Q23 영업이익 196억원으로 22개 분기 만의 흑자전환. 2021년 이후 수주 실적, 건조량 증가, 선가 회복, 원자재 부담 둔화가 동시에 언급됨. |
| 082740 | 한화엔진 | 2023-05-30 | https://ssl.pstatic.net/imgstock/upload/research/company/1685406605395.pdf | 1Q23 말 수주잔고에서 LNG 운반선 비중 59%, 신규수주 중 D/F 엔진 비중 89%; D/F 엔진은 가격과 마진이 높은 믹스 개선으로 설명됨. |
| 010620 | HD현대미포 | 2023-06-02 | https://m.thebell.co.kr/m/newsview.asp?newskey=202306011532258160103317&svccode= | 고가 일감이 계약자산으로 들어오고 잔고 금액은 늘었지만, 저가 물량 해소와 이익 개선 속도가 상대적으로 늦다는 내용이 동시에 존재. |
| 329180 | HD현대중공업 | 2023-07-27 | https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2023/07/27/HDHHI_230728_2Q23Re.pdf | 2Q23 영업이익 685억원, 엔진 부문이 실적 개선 견인, 누적 신규수주 72.7억달러와 수주잔고 증가가 확인됐지만 직후 180D 가격경로는 고MAE. |
| 009540 | HD한국조선해양 | 2023-07-27 | https://www.yna.co.kr/view/AKR20230727109201527 | 2Q23 연결 영업이익 712억원 흑자전환. 조선부문 매출 증가와 고부가가치 선박 반영이 언급됐지만, holding/자회사 혼합 구조상 초기 180D는 고MAE. |

## 10. Price Data Source Map

| symbol | price shard(s) | profile path | 180D status |
|---|---|---|---|
| 010140 | atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv + next-year shard as needed | atlas/symbol_profiles/010/010140.json | clean_180D_window |
| 082740 | atlas/ohlcv_tradable_by_symbol_year/082/082740/2023.csv + next-year shard as needed | atlas/symbol_profiles/082/082740.json | clean_180D_window |
| 010620 | atlas/ohlcv_tradable_by_symbol_year/010/010620/2023.csv + next-year shard as needed | atlas/symbol_profiles/010/010620.json | clean_180D_window |
| 329180 | atlas/ohlcv_tradable_by_symbol_year/329/329180/2023.csv + next-year shard as needed | atlas/symbol_profiles/329/329180.json | clean_180D_window |
| 009540 | atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv + next-year shard as needed | atlas/symbol_profiles/009/009540.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### 11.1 010140 / 삼성중공업 — positive structural success

The trigger had both event evidence and a plausible margin bridge: 1Q23 profit turned positive after 22 quarters, and the evidence itself tied the improvement to backlog-driven volume, ship price recovery, and easing raw-material pressure. The 90D/180D MFE of `66.73%` with only `-5.81%` MAE is exactly the kind of C01 row that should survive the post-calibrated profile.

### 11.2 082740 / 한화엔진 — positive but needs 4B watch discipline

The D/F engine mix gave the backlog a quality vector. MFE90 reached `45.88%`, while MAE90 stayed at `-5.03%`; however, the drawdown after the 180D peak was `-40.71%`. This does not disprove the Stage2 thesis. It says the ship was fast, but the deck got slippery near the local peak.

### 11.3 010620 / HD현대미포 — backlog value did not immediately become FCF

The case is a clean C01 counterexample. Contract-asset and backlog-value evidence looked positive, but the same evidence family noted slow profit recovery from low-price backlog. MFE90 stopped at `18.07%`, while MAE180 widened to `-27.23%`. The current profile would be too generous if it promoted this from backlog watch to Green without realized margin/working-capital proof.

### 11.4 329180 / HD현대중공업 — true thesis, bad 180D timing

The 2Q23 data showed a valid backlog and profit turn, but the entry sat near a local peak. MFE180 was only `3.24%`, MAE180 was `-25.20%`, while 1Y MFE later reached `62.86%`. This is not a 4C thesis death; it is a Stage3 timing error. C01 should distinguish “eventually right” from “calibration entry was right.”

### 11.5 009540 / HD한국조선해양 — parent-company lag and subsidiary-mix delay

The parent-company signal had genuine sector value, but the holding-company structure diluted immediate conversion timing. MFE180 was only `4.28%`, MAE180 was `-28.05%`, while 1Y MFE later reached `72.19%`. This supports a canonical rule: parent-level backlog evidence needs subsidiary-level margin/FCF confirmation before Green.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | aggregate_role |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C01_R1L209_T001_010140_20230428_Stage2Actionable | 010140 | Stage2-Actionable | 2023-04-28 | 5,680 | 16.90% | 66.73% | 66.73% | -5.81% | -5.81% | -5.81% | representative |
| C01_R1L209_T002_082740_20230531_Stage2Actionable | 082740 | Stage2-Actionable | 2023-05-31 | 8,740 | 42.56% | 45.88% | 45.88% | -1.14% | -5.03% | -13.50% | representative |
| C01_R1L209_T003_010620_20230605_Stage2 | 010620 | Stage2 | 2023-06-05 | 81,900 | 15.14% | 18.07% | 18.07% | -4.76% | -10.87% | -27.23% | representative |
| C01_R1L209_T004_329180_20230728_Stage3Yellow | 329180 | Stage3-Yellow | 2023-07-28 | 135,700 | 3.24% | 3.24% | 3.24% | -12.75% | -25.20% | -25.20% | representative |
| C01_R1L209_T005_009540_20230728_Stage3Yellow | 009540 | Stage3-Yellow | 2023-07-28 | 123,700 | 1.46% | 1.46% | 4.28% | -10.91% | -28.05% | -28.05% | representative |
| C01_R1L209_T006_010620_20230802_STAGE4B_PRICE_ONLY_LOCAL_PEAK | 010620 | Stage4B | 2023-08-02 | 93,500 | 3.42% | 3.42% | 3.42% | -13.58% | -26.95% | -37.11% | 4B_overlay_only |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | verdict |
|---|---|---|---|
| 010140 | Stage2-Actionable / Yellow-to-Green eligible | strong MFE, shallow MAE | current_profile_correct |
| 082740 | Stage2-Actionable / Yellow eligible | strong MFE, later peak drawdown | current_profile_correct with 4B watch need |
| 010620 | Yellow/Green risk if backlog value overweighted | MAE180 -27.23% | current_profile_false_positive |
| 329180 | Yellow/Green risk on Q2 profit + backlog | MFE180 3.24%, MAE180 -25.20%, but 1Y success | current_profile_too_early |
| 009540 | Yellow/Green risk on parent profit turn | MFE180 4.28%, MAE180 -28.05%, but 1Y success | current_profile_too_early |

Answer to the stress-test questions:

1. The current calibrated profile correctly accepts backlog + realized margin rows but remains too eager when backlog is not yet cash/margin conversion.
2. Stage2 bonus is not globally wrong; it is too generous for C01 when backlog is size-only or parent-level.
3. Yellow threshold is acceptable if the label remains watch/Actionable rather than Green.
4. Green threshold/revision requirements should be sector-qualified by margin and FCF conversion.
5. Price-only blowoff and full-4B non-price guards remain necessary.
6. No hard 4C adjustment is proposed because delayed success rows should not be classified as thesis death.

## 14. Stage2 / Yellow / Green Comparison

| rule | observation | candidate adjustment |
|---|---|---|
| Stage2 | works for 010140/082740; risky for 010620 if backlog value only | keep Stage2, but require bridge note |
| Stage2-Actionable | useful when backlog quality is explicit | preserve bonus only with customer/order quality or margin evidence |
| Stage3-Yellow | acceptable for HD현대중공업/KSOE as watch | do not auto-Green on one-quarter profit turn |
| Stage3-Green | dangerous without recurring margin/FCF | require C01 margin/working-capital conversion gate |

No confirmed Stage3-Green trigger is used as a representative in this loop, so `green_lateness_ratio = not_applicable` for representative rows.

## 15. 4B Local vs Full-window Timing Audit

The 010620 overlay row tests the current full-4B non-price requirement.

```text
Stage2 entry price = 81,900
Stage4B watch entry price = 93,500
local/full observed 180D peak = 96,700
four_b_local_peak_proximity = 0.7838
four_b_full_window_peak_proximity = 0.7838
```

The timing is good as a local risk watch, but the evidence is price-only. Therefore it should not become a full 4B. The existing `full_4b_requires_non_price_evidence` axis is strengthened, not weakened.

## 16. 4C Protection Audit

No hard 4C row is proposed. The two high-MAE rows, 329180 and 009540, later produced strong 1Y MFE. Treating them as hard 4C would kill a thesis that only needed more time. The correct classification is `thesis_break_watch_only` or `too_early_stage3`, not `hard_4c_success`.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
candidate_axis = backlog_to_fcf_conversion_gate
```

For L1 order/backlog industrials, Stage3-Green should require at least one of the following after the backlog headline:

```text
- realized margin bridge
- working-capital / contract-asset conversion improvement
- recurring quarterly profit, not just one-off or parent-level effect
- customer/order quality plus delivery visibility with margin carry-through
```

Sector-specific rule candidate:

```text
L1 backlog/order evidence should be capped at Stage2-Actionable or Stage3-Yellow unless the research row has realized margin or working-capital/FCF conversion evidence. Backlog size alone cannot promote to Green.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
candidate_axis = c01_backlog_quality_to_margin_fcf_ladder
```

Canonical rule candidate:

```text
C01 should split backlog evidence into backlog_size, backlog_quality, realized_margin_bridge, and fcf_conversion. Green requires the bridge terms; parent-level or size-only backlog is a watch signal. High-MAE but later 1Y success should be classified as too-early timing, not hard 4C.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | alignment verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 5 | 27.07% | -14.99% | 27.64% | -19.96% | 0.60 | mixed; 2 clean positives but 3 180D high-MAE/too-early rows |
| P0b_e2r_2_0_baseline_reference | rollback | 3 | 43.56% | -7.24% | 43.56% | -15.51% | 0.33 | lower false positive, but misses HSD/turnaround speed |
| P1_L1_sector_fcf_margin_bridge_gate | sector_specific | 2 | 56.30% | -5.42% | 56.30% | -9.66% | 0.00 | best 90/180D alignment in this loop |
| P2_C01_backlog_quality_to_margin_conversion | canonical_archetype_specific | 3 | 43.56% | -7.24% | 43.56% | -15.51% | 0.33 | keeps positives and demotes weak bridge rows |
| P3_C01_4B_local_peak_watch_guard | counterexample_guard | 5 | 27.07% | -14.99% | 27.64% | -19.96% | 0.40 | risk overlay improves drawdown handling but not entry selection |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | component_delta_explanation |
|---|---:|---|---:|---|---|
| 010140 | 84 | Stage3-Yellow | 87 | Stage3-Green | margin_bridge +2, revision +1; actual quarterly margin bridge makes this a valid C01 positive rather than price-only rerating. |
| 082740 | 82 | Stage3-Yellow | 86 | Stage3-Yellow | customer/order quality +2 and margin bridge +2 because backlog quality, not just size, was specified. |
| 010620 | 76 | Stage3-Yellow | 69 | Stage2 | backlog visibility kept, but margin bridge -5 and execution risk +4; backlog size without FCF/margin conversion should not Green. |
| 329180 | 86 | Stage3-Yellow | 78 | Stage2-Actionable | margin bridge and execution risk are reweighted until recurring shipbuilding margin, not single quarter backlog, confirms conversion. |
| 009540 | 84 | Stage3-Yellow | 76 | Stage2-Actionable | parent-company signal requires subsidiary-level margin/FCF confirmation before Green; execution risk +3 and visibility discount applied. |

Canonical component keys used in the proxy scoring rows:

```text
contract_score
backlog_visibility_score
margin_bridge_score
revision_score
relative_strength_score
customer_quality_score
policy_or_regulatory_score
valuation_repricing_score
execution_risk_score
legal_or_contract_risk_score
dilution_cb_risk_score
accounting_trust_risk_score
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD | 2 | 3 | 1 | 0 | 5 | 0 | 6 | 5 | 3 | backlog_to_fcf_conversion_gate | c01_backlog_quality_to_margin_fcf_ladder | C01 now has additional FCF-conversion counterexamples and a price-only 4B watch row |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_revision_min; full_4b_requires_non_price_evidence
residual_error_types_found: backlog_size_without_fcf_conversion_false_positive; parent_subsidiary_margin_lag_high_mae; price_only_local_4b_should_remain_watch
new_axis_proposed: c01_backlog_quality_to_margin_fcf_ladder
existing_axis_strengthened: full_4b_requires_non_price_evidence; stage3_green_revision_min_by_realized_margin_bridge
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L1 backlog/order evidence capped below Green unless realized margin or working-capital/FCF conversion is present.
canonical_archetype_rule_candidate: C01 separates backlog size from backlog quality, margin bridge, and FCF conversion; later 1Y success after high MAE is too-early timing, not hard 4C.
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable OHLC rows
- entry date and entry close
- 30D/90D/180D MFE and MAE
- 1Y where available
- corporate-action window status from symbol profile dates
- C01 novelty by new symbol/trigger family selection
```

Not validated:

```text
- live candidate status
- brokerage execution
- current watchlist suitability
- production scoring code
- exact DART filing parser extraction
- post-2026-02-20 price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,backlog_to_fcf_conversion_gate,sector_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"L1 backlog/order rows need margin or working-capital conversion before Green","P1 improves avg_MFE90 to 56.30% and avg_MAE90 to -5.42% by selecting the two clean bridge rows","C01_R1L209_T001_010140_20230428_Stage2Actionable|C01_R1L209_T002_082740_20230531_Stage2Actionable",5,5,3,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,c01_backlog_quality_to_margin_fcf_ladder,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"C01 should split size, quality, margin bridge, FCF conversion","Demotes three high-MAE 180D rows from Green risk to Stage2/Yellow watch", "C01_R1L209_T003_010620_20230605_Stage2|C01_R1L209_T004_329180_20230728_Stage3Yellow|C01_R1L209_T005_009540_20230728_Stage3Yellow",5,5,3,medium,canonical_shadow_only,"do not treat later 1Y success as hard 4C"
shadow_weight,price_only_local_4b_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"Mipo local peak timing was useful but price-only evidence should remain watch","Prevents full 4B overclassification while flagging -37.11% MAE180 after peak entry","C01_R1L209_T006_010620_20230802_STAGE4B_PRICE_ONLY_LOCAL_PEAK",1,0,1,medium,guardrail_shadow_only,"strengthens existing full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C01_R1L209_010140_20230428_SAMSUNG_HEAVY_Q1_TURNAROUND","symbol":"010140","company_name":"삼성중공업","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C01_R1L209_T001_010140_20230428_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"order_backlog_to_margin_bridge_positive_q1_turnaround"}
{"row_type":"case","case_id":"C01_R1L209_082740_20230531_HSD_ENGINE_DF_BACKLOG_MIX","symbol":"082740","company_name":"한화엔진","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C01_R1L209_T002_082740_20230531_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"df_engine_backlog_mix_positive_but_high_peak_drawdown"}
{"row_type":"case","case_id":"C01_R1L209_010620_20230605_MIPO_LOW_PRICE_BACKLOG_DELAY","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C01_R1L209_T003_010620_20230605_Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_counterexample_or_too_early_for_180D","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"backlog_value_not_fcf_counterexample_low_price_backlog_delay"}
{"row_type":"case","case_id":"C01_R1L209_329180_20230728_HHI_Q2_BACKLOG_DELAYED_REPRICE","symbol":"329180","company_name":"HD현대중공업","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"C01_R1L209_T004_329180_20230728_Stage3Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_counterexample_or_too_early_for_180D","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"valid_backlog_but_180d_entry_too_early_high_mae_later_1y_success"}
{"row_type":"case","case_id":"C01_R1L209_009540_20230728_KSOE_PARENT_BACKLOG_DELAYED_REPRICE","symbol":"009540","company_name":"HD한국조선해양","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"C01_R1L209_T005_009540_20230728_Stage3Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_counterexample_or_too_early_for_180D","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"parent_backlog_signal_delayed_reprice_high_mae_before_1y_success"}
{"row_type":"trigger","trigger_id":"C01_R1L209_T001_010140_20230428_Stage2Actionable","case_id":"C01_R1L209_010140_20230428_SAMSUNG_HEAVY_Q1_TURNAROUND","symbol":"010140","company_name":"삼성중공업","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","sector":"shipbuilding","primary_archetype":"order_backlog_margin_fcf_conversion","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-27","entry_date":"2023-04-28","entry_price":5680.0,"evidence_available_at_that_date":"1Q23 영업이익 196억원으로 22개 분기 만의 흑자전환. 2021년 이후 수주 실적, 건조량 증가, 선가 회복, 원자재 부담 둔화가 동시에 언급됨.","evidence_source":"https://www.yna.co.kr/view/AKR20230427139501527","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010140/2023.csv","profile_path":"atlas/symbol_profiles/010/010140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.9014,"MFE_90D_pct":66.7254,"MFE_180D_pct":66.7254,"MFE_1Y_pct":78.169,"MFE_2Y_pct":null,"MAE_30D_pct":-5.8099,"MAE_90D_pct":-5.8099,"MAE_180D_pct":-5.8099,"MAE_1Y_pct":-5.8099,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-02","peak_price":9470.0,"drawdown_after_peak_pct":-28.0887,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_stage4c","trigger_outcome_label":"order_backlog_to_margin_bridge_positive_q1_turnaround","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1L209_010140_20230428_SAMSUNG_HEAVY_Q1_TURNAROUND_2023-04-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01_R1L209_T002_082740_20230531_Stage2Actionable","case_id":"C01_R1L209_082740_20230531_HSD_ENGINE_DF_BACKLOG_MIX","symbol":"082740","company_name":"한화엔진","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","sector":"ship_engine","primary_archetype":"order_backlog_margin_fcf_conversion","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-30","entry_date":"2023-05-31","entry_price":8740.0,"evidence_available_at_that_date":"1Q23 말 수주잔고에서 LNG 운반선 비중 59%, 신규수주 중 D/F 엔진 비중 89%; D/F 엔진은 가격과 마진이 높은 믹스 개선으로 설명됨.","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1685406605395.pdf","stage2_evidence_fields":["customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/082/082740/2023.csv","profile_path":"atlas/symbol_profiles/082/082740.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.5629,"MFE_90D_pct":45.881,"MFE_180D_pct":45.881,"MFE_1Y_pct":58.9245,"MFE_2Y_pct":270.1373,"MAE_30D_pct":-1.1442,"MAE_90D_pct":-5.0343,"MAE_180D_pct":-13.5011,"MAE_1Y_pct":-13.5011,"MAE_2Y_pct":-13.5011,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2023-08-02","peak_price":12750.0,"drawdown_after_peak_pct":-40.7059,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_stage4c","trigger_outcome_label":"df_engine_backlog_mix_positive_but_high_peak_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1L209_082740_20230531_HSD_ENGINE_DF_BACKLOG_MIX_2023-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01_R1L209_T003_010620_20230605_Stage2","case_id":"C01_R1L209_010620_20230605_MIPO_LOW_PRICE_BACKLOG_DELAY","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","sector":"mid_size_shipbuilding","primary_archetype":"order_backlog_margin_fcf_conversion","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2023-06-02","entry_date":"2023-06-05","entry_price":81900.0,"evidence_available_at_that_date":"고가 일감이 계약자산으로 들어오고 잔고 금액은 늘었지만, 저가 물량 해소와 이익 개선 속도가 상대적으로 늦다는 내용이 동시에 존재.","evidence_source":"https://m.thebell.co.kr/m/newsview.asp?newskey=202306011532258160103317&svccode=","stage2_evidence_fields":["backlog_or_delivery_visibility","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010620/2023.csv","profile_path":"atlas/symbol_profiles/010/010620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.1404,"MFE_90D_pct":18.0708,"MFE_180D_pct":18.0708,"MFE_1Y_pct":18.0708,"MFE_2Y_pct":null,"MAE_30D_pct":-4.7619,"MAE_90D_pct":-10.8669,"MAE_180D_pct":-27.2283,"MAE_1Y_pct":-28.2051,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-02","peak_price":96700.0,"drawdown_after_peak_pct":-38.3661,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_stage4c","trigger_outcome_label":"backlog_value_not_fcf_counterexample_low_price_backlog_delay","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1L209_010620_20230605_MIPO_LOW_PRICE_BACKLOG_DELAY_2023-06-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01_R1L209_T004_329180_20230728_Stage3Yellow","case_id":"C01_R1L209_329180_20230728_HHI_Q2_BACKLOG_DELAYED_REPRICE","symbol":"329180","company_name":"HD현대중공업","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","sector":"large_shipbuilding","primary_archetype":"order_backlog_margin_fcf_conversion","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2023-07-27","entry_date":"2023-07-28","entry_price":135700.0,"evidence_available_at_that_date":"2Q23 영업이익 685억원, 엔진 부문이 실적 개선 견인, 누적 신규수주 72.7억달러와 수주잔고 증가가 확인됐지만 직후 180D 가격경로는 고MAE.","evidence_source":"https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2023/07/27/HDHHI_230728_2Q23Re.pdf","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/329/329180/2023.csv","profile_path":"atlas/symbol_profiles/329/329180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.2424,"MFE_90D_pct":3.2424,"MFE_180D_pct":3.2424,"MFE_1Y_pct":62.8592,"MFE_2Y_pct":null,"MAE_30D_pct":-12.7487,"MAE_90D_pct":-25.2027,"MAE_180D_pct":-25.2027,"MAE_1Y_pct":-25.2027,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-01","peak_price":140100.0,"drawdown_after_peak_pct":-27.5517,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_stage4c","trigger_outcome_label":"valid_backlog_but_180d_entry_too_early_high_mae_later_1y_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1L209_329180_20230728_HHI_Q2_BACKLOG_DELAYED_REPRICE_2023-07-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01_R1L209_T005_009540_20230728_Stage3Yellow","case_id":"C01_R1L209_009540_20230728_KSOE_PARENT_BACKLOG_DELAYED_REPRICE","symbol":"009540","company_name":"HD한국조선해양","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","sector":"shipbuilding_holding_company","primary_archetype":"order_backlog_margin_fcf_conversion","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2023-07-27","entry_date":"2023-07-28","entry_price":123700.0,"evidence_available_at_that_date":"2Q23 연결 영업이익 712억원 흑자전환. 조선부문 매출 증가와 고부가가치 선박 반영이 언급됐지만, holding/자회사 혼합 구조상 초기 180D는 고MAE.","evidence_source":"https://www.yna.co.kr/view/AKR20230727109201527","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009540/2023.csv","profile_path":"atlas/symbol_profiles/009/009540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.4551,"MFE_90D_pct":1.4551,"MFE_180D_pct":4.2846,"MFE_1Y_pct":72.1908,"MFE_2Y_pct":null,"MAE_30D_pct":-10.9135,"MAE_90D_pct":-28.0517,"MAE_180D_pct":-28.0517,"MAE_1Y_pct":-28.0517,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":129000.0,"drawdown_after_peak_pct":-14.1085,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_stage4c","trigger_outcome_label":"parent_backlog_signal_delayed_reprice_high_mae_before_1y_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1L209_009540_20230728_KSOE_PARENT_BACKLOG_DELAYED_REPRICE_2023-07-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01_R1L209_T006_010620_20230802_STAGE4B_PRICE_ONLY_LOCAL_PEAK","case_id":"C01_R1L209_010620_20230605_MIPO_LOW_PRICE_BACKLOG_DELAY","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_CONVERSION_GUARD","sector":"mid_size_shipbuilding","primary_archetype":"order_backlog_margin_fcf_conversion","loop_objective":"counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2023-08-02","entry_date":"2023-08-02","entry_price":93500.0,"evidence_available_at_that_date":"Stage2 이후 2023-08-02가 180D observed local/full peak에 가까웠지만 non-price 4B 근거가 없어 full 4B가 아니라 watch overlay로만 취급.","evidence_source":"Songdaiki/stock-web price path only; no independent non-price 4B evidence found for this loop","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010620/2023.csv","profile_path":"atlas/symbol_profiles/010/010620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.4225,"MFE_90D_pct":3.4225,"MFE_180D_pct":3.4225,"MFE_1Y_pct":31.3369,"MFE_2Y_pct":null,"MAE_30D_pct":-13.5829,"MAE_90D_pct":-26.9519,"MAE_180D_pct":-37.1123,"MAE_1Y_pct":-37.1123,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-02","peak_price":96700.0,"drawdown_after_peak_pct":-39.1934,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.7838,"four_b_full_window_peak_proximity":0.7838,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable_no_stage4c","trigger_outcome_label":"price_only_local_4b_watch_saves_from_full_4b_overclassification","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1L209_010620_20230605_MIPO_LOW_PRICE_BACKLOG_DELAY_2023-08-02","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_new_trigger_family_4b_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L209_AGGREGATE","trigger_id":"representative_trigger_set","symbol":"MULTI","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":null,"stage_label_before":"aggregate_profile_comparison","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":null,"stage_label_after":"aggregate_profile_comparison","changed_components":[],"component_delta_explanation":"current calibrated profile selects all five representative C01 rows when backlog/revenue/turnaround evidence crosses Stage2/Yellow.","MFE_90D_pct":27.0749,"MAE_90D_pct":-14.9931,"score_return_alignment_label":"mixed; 2 clean positives but 3 180D high-MAE/too-early rows","current_profile_verdict":"aggregate_profile_stress_test"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","case_id":"C01_R1L209_AGGREGATE","trigger_id":"representative_trigger_set","symbol":"MULTI","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":null,"stage_label_before":"aggregate_profile_comparison","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":null,"stage_label_after":"aggregate_profile_comparison","changed_components":["rollback_reference_only"],"component_delta_explanation":"old baseline is less eager on evidence bridge and misses part of the early structural positives.","MFE_90D_pct":43.5591,"MAE_90D_pct":-7.237,"score_return_alignment_label":"lower false positive, but misses HSD/turnaround speed","current_profile_verdict":"aggregate_profile_stress_test"}
{"row_type":"score_simulation","profile_id":"P1_L1_sector_fcf_margin_bridge_gate","case_id":"C01_R1L209_AGGREGATE","trigger_id":"representative_trigger_set","symbol":"MULTI","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":null,"stage_label_before":"aggregate_profile_comparison","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":null,"stage_label_after":"aggregate_profile_comparison","changed_components":["fcf_conversion_gate","working_capital_bridge_required_for_green"],"component_delta_explanation":"L1 order/backlog rows require realized margin/working-capital bridge before Green; pure backlog goes Stage2 watch.","MFE_90D_pct":56.3032,"MAE_90D_pct":-5.4221,"score_return_alignment_label":"best 90/180D alignment in this loop","current_profile_verdict":"aggregate_profile_stress_test"}
{"row_type":"score_simulation","profile_id":"P2_C01_backlog_quality_to_margin_conversion","case_id":"C01_R1L209_AGGREGATE","trigger_id":"representative_trigger_set","symbol":"MULTI","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":null,"stage_label_before":"aggregate_profile_comparison","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":null,"stage_label_after":"aggregate_profile_comparison","changed_components":["backlog_quality_score_not_size_only","margin_bridge_score_min_for_yellow_to_green"],"component_delta_explanation":"C01 compresses backlog size, backlog quality, actual margin, and FCF conversion into a staged ladder.","MFE_90D_pct":43.5591,"MAE_90D_pct":-7.237,"score_return_alignment_label":"keeps positives and demotes weak bridge rows","current_profile_verdict":"aggregate_profile_stress_test"}
{"row_type":"score_simulation","profile_id":"P3_C01_4B_local_peak_watch_guard","case_id":"C01_R1L209_AGGREGATE","trigger_id":"representative_trigger_set","symbol":"MULTI","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":null,"stage_label_before":"aggregate_profile_comparison","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":null,"stage_label_after":"aggregate_profile_comparison","changed_components":["price_only_local_4b_watch_guard"],"component_delta_explanation":"When backlog thesis is still alive but price has run into local peak without non-price 4B evidence, label 4B watch not full 4B.","MFE_90D_pct":27.075,"MAE_90D_pct":-14.9931,"score_return_alignment_label":"risk overlay improves drawdown handling but not entry selection","current_profile_verdict":"aggregate_profile_stress_test"}
{"row_type":"residual_contribution","round":"R1","loop":"209","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence"],"residual_error_types_found":["backlog_size_without_fcf_conversion_false_positive","parent_subsidiary_margin_lag_high_mae","price_only_local_4b_should_remain_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 1
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
completed_round = R1
completed_loop = 209
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / balance-quality reinforcement + Priority 0 URL/proxy quality repair
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA; C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE; C15_MATERIAL_SPREAD_SUPERCYCLE; C05_EPC_MEGA_CONTRACT_MARGIN_GAP only for missing-url/MFE repair; C01 only if new FCF/cash-conversion direct source rows are found
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
STOCK-WEB MANIFEST: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
STOCK-WEB SCHEMA: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
Samsung Heavy evidence: https://www.yna.co.kr/view/AKR20230427139501527
Hanwha Engine/HSD evidence: https://ssl.pstatic.net/imgstock/upload/research/company/1685406605395.pdf
HD Hyundai Mipo evidence: https://m.thebell.co.kr/m/newsview.asp?newskey=202306011532258160103317&svccode=
HD Hyundai Heavy evidence: https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2023/07/27/HDHHI_230728_2Q23Re.pdf
HD Korea Shipbuilding evidence: https://www.yna.co.kr/view/AKR20230727109201527
```
