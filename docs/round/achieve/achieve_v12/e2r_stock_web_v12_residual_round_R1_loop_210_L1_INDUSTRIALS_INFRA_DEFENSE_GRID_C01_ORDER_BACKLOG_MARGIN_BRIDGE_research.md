# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
file_name: e2r_stock_web_v12_residual_round_R1_loop_210_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round: R1
selected_loop: 210
round: R1
loop: 210
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 C01 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective: counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
```

This loop adds **6 new independent cases**, **3 counterexamples/guardrails**, and **3 residual errors** for `L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE`. It deliberately avoids the immediately prior C01 symbols recorded in the prior local loop (`009540`, `010140`, `010620`, `082740`, `329180`) and tests the narrower gap: backlog headline versus realized margin, working capital, and FCF conversion.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The loop does not re-argue the global rule that Stage2 must be earlier than Green. It stress-tests whether C01 needs a more specific bridge: order/backlog quantity → customer quality → delivery route → margin bridge → working-capital/FCF conversion.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | `R1` |
| selected_loop | `210` |
| large_sector_id | `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` |
| canonical_archetype_id | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` |
| fine_archetype_id | `C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR` |
| loop_objective | `counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair` |
| scope check | C01 maps to R1 / L1, so `round_sector_consistency=pass` |

This is an R1/L1 shipbuilding and industrial backlog-quality repair loop, not an R13 cross-sector red-team file.

## 3. Previous Coverage / Duplicate Avoidance Check

The no-repeat index says all C01~C32 archetypes are above 80 rows, so the remaining job is quality reinforcement rather than row-count filling. C01 is explicitly listed under Priority 1 for backlog-to-FCF counterexample reinforcement, while Priority 0 continues to prefer direct URL/proxy/MFE-MAE repair.

| check | result |
|---|---|
| duplicate key rule | `canonical_archetype_id + symbol + trigger_type + entry_date` |
| duplicate violations | 0 |
| reused case count | 0 |
| new independent case count | 6 |
| same_archetype_new_symbol_count | 6 |
| same_archetype_new_trigger_family_count | 6 |
| direct URL/proxy repair status | direct or traceable evidence source included for every row |

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| price source | Songdaiki/stock-web |
| manifest | `atlas/manifest.json` |
| schema | `atlas/schema.json` |
| universe | `atlas/universe/all_symbols.csv` |
| calibration shard root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw shard root | `atlas/ohlcv_raw_by_symbol_year` |
| price basis | `tradable_raw` |
| price adjustment status | `raw_unadjusted_marcap` |
| manifest max_date | `2026-02-20` |
| tradable rows | `14,354,401` |
| raw rows | `15,214,118` |
| symbol count | `5,414` |

MFE/MAE use the stock-web schema rule: max high or min low from entry_date through N tradable rows divided by entry_price.

## 5. Historical Eligibility Gate

| symbol | profile_path | entry_date | 180D rows | CA window | calibration_usable | block_reasons |
| --- | --- | --- | --- | --- | --- | --- |
| 033500 | atlas/symbol_profiles/033/033500.json | 2023-01-25 | 180 | clean_180D_window | true | [] |
| 017960 | atlas/symbol_profiles/017/017960.json | 2023-07-18 | 180 | clean_180D_window | true | [] |
| 071970 | atlas/symbol_profiles/071/071970.json | 2023-08-01 | 180 | clean_180D_window | true | [] |
| 097230 | atlas/symbol_profiles/097/097230.json | 2024-06-17 | 180 | clean_180D_window | true | [] |
| 042660 | atlas/symbol_profiles/042/042660.json | 2024-07-29 | 180 | clean_180D_window | true | [] |
| 075580 | atlas/symbol_profiles/075/075580.json | 2024-04-03 | 180 | clean_180D_window | true | [] |

Every representative trigger row has a real Stock-Web entry row, at least 180 tradable rows forward, positive OHLCV, clean 180D corporate-action window, and full 30D/90D/180D MFE/MAE fields.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR
compression_path = backlog_quantity -> backlog_quality -> delivery_route -> margin_bridge -> working_capital/FCF_conversion -> durable_rerating
```

C01 should behave like a bridge inspection checklist. A large backlog is the bridge sign at the entrance; it is not proof that the middle span can carry trucks. The missing span in false positives is usually margin or cash conversion.

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | trigger_family | entry_date | entry_price | role | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01_L210_CASE_01_033500_20230120 | 033500 | 동성화인텍 | Stage2-Actionable | direct_lng_insulation_supply_contract_to_backlog_quality | 2023-01-25 | 11,000 | structural_success | 13.36% | -7.82% | 38.36% | -7.82% | current_profile_correct |
| C01_L210_CASE_02_017960_20230717 | 017960 | 한국카본 | Stage2-Actionable | contract_amount_increase_without_near_term_margin_cash_conversion | 2023-07-18 | 14,130 | failed_rerating | 7.86% | -22.15% | 7.86% | -30.15% | current_profile_false_positive |
| C01_L210_CASE_03_071970_20230731 | 071970 | HD현대마린엔진 | Stage2-Actionable | engine_supply_contract_and_group_synergy_order_conversion | 2023-08-01 | 11,660 | high_mae_success | 23.84% | -23.76% | 49.74% | -23.76% | current_profile_correct |
| C01_L210_CASE_04_097230_20240614 | 097230 | HJ중공업 | Stage2 | combined_shipbuilding_construction_backlog_to_delayed_rerating | 2024-06-17 | 3,185 | high_mae_success | 18.84% | -31.40% | 210.83% | -31.55% | current_profile_too_early |
| C01_L210_CASE_05_042660_20240726 | 042660 | 한화오션 | Stage4B | oneoff_cost_loss_should_be_watch_not_thesis_death | 2024-07-29 | 30,100 | 4B_overlay_success | 36.38% | -15.61% | 199.00% | -15.61% | current_profile_4C_too_early |
| C01_L210_CASE_06_075580_20240402 | 075580 | 세진중공업 | Stage2-Actionable | customer_backlog_driven_deckhouse_lpg_tank_margin_recovery | 2024-04-03 | 6,850 | structural_success | 59.42% | -7.74% | 59.42% | -7.74% | current_profile_correct |

## 8. Positive vs Counterexample Balance

| bucket | count | symbols | interpretation |
|---|---:|---|---|
| positive structural success | 3 | 033500, 071970, 075580 | Customer/order quality plus delivery or margin bridge produced useful 180D MFE. |
| counterexample / guardrail | 3 | 017960, 097230, 042660 | Contract/backlog alone was too early, high-MAE, or one-off loss was better treated as 4B watch than hard 4C. |
| 4B row | 1 | 042660 | One-off cost/margin disappointment watch. |
| 4C row | 0 | none | No terminal cancellation/accounting/customer-loss evidence was used. |

## 9. Evidence Source Map

| symbol | company | trigger_date | entry_rule | source | summary |
| --- | --- | --- | --- | --- | --- |
| 033500 | 동성화인텍 | 2023-01-20 | next tradable close when timing unclear or after close; otherwise event-day/next-day close | https://www.hankyung.com/article/202301205854L | 삼성중공업향 LNG운반선 초저온 보냉자재 공급계약. 계약금액 571.4억원, 최근 매출액 대비 15.7%, 계약기간 2023-01-19~2027-11-30. |
| 017960 | 한국카본 | 2023-07-17 | next tradable close when timing unclear or after close; otherwise event-day/next-day close | https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20230717000119&docno=&method=searchInitInfo | LNG선 보냉재 공급계약 정정. 계약금액 증가가 확인됐지만 이후 180D 가격경로는 MAE가 깊고 MFE가 낮아 계약금액 증액만으로는 Green이 부족한 사례. |
| 071970 | HD현대마린엔진 | 2023-07-31 | next tradable close when timing unclear or after close; otherwise event-day/next-day close | https://www.shinyoung.com/files/20230801/51c974724b345.pdf \| https://kr.investing.com/news/stock-market-news/article-902549 | STX중공업/HD현대마린엔진의 선박용 저속엔진, HD현대그룹 편입 기대, 2023~2025 실적 추정 개선 및 2023-04-25 케이조선 선박엔진 공급계약. |
| 097230 | HJ중공업 | 2024-06-14 | next tradable close when timing unclear or after close; otherwise event-day/next-day close | https://www.ibtomato.com/ExternalView.aspx?no=12416&type=1 | 2024년 3월 말 연결 기준 조선 수주잔고 1조4606억원, 건설 수주잔고 5조4883억원, 총 6조6489억원으로 2023년 매출 기준 3년 이상 일감이라는 기사. |
| 042660 | 한화오션 | 2024-07-26 | next tradable close when timing unclear or after close; otherwise event-day/next-day close | https://www.yna.co.kr/view/AKR20240726088500527 \| https://www.businesspost.co.kr/BP?command=article_view&num=360326 | 2024년 2분기 매출 2조5361억원, 영업손실 96억원. 컨테이너 적자호선·외주비·생산 안정화 비용 등으로 적자를 기록했지만 수주/건조 물량과 반복 생산체계는 유지. |
| 075580 | 세진중공업 | 2024-04-02 | next tradable close when timing unclear or after close; otherwise event-day/next-day close | https://ssl.pstatic.net/imgstock/upload/research/company/1712013384054.pdf | Deck House와 LPG Tank 중심, HD현대중공업·현대미포 등 주력 고객사의 수주잔고 증가로 Deck House 공급척수 증가와 2024년 두 자리수 영업이익률 회복 전망. |

## 10. Price Data Source Map

| symbol | shard | entry_date | O | H | L | C/entry | V |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 033500 | atlas/ohlcv_tradable_by_symbol_year/033/033500/2023.csv | 2023-01-25 | 11,050 | 11,100 | 10,900 | 11,000 | 156,999 |
| 017960 | atlas/ohlcv_tradable_by_symbol_year/017/017960/2023.csv | 2023-07-18 | 13,960 | 14,500 | 13,750 | 14,130 | 1,552,564 |
| 071970 | atlas/ohlcv_tradable_by_symbol_year/071/071970/2023.csv | 2023-08-01 | 10,430 | 11,660 | 9,830 | 11,660 | 10,222,255 |
| 097230 | atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv | 2024-06-17 | 3,300 | 3,450 | 3,170 | 3,185 | 197,910 |
| 042660 | atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv | 2024-07-29 | 30,900 | 31,000 | 29,700 | 30,100 | 2,173,949 |
| 075580 | atlas/ohlcv_tradable_by_symbol_year/075/075580/2024.csv | 2024-04-03 | 6,860 | 7,150 | 6,710 | 6,850 | 963,279 |

## 11. Case-by-Case Trigger Grid

| symbol | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | current profile verdict |
|---|---|---|---|---|---|
| 033500 | public_contract_disclosure; customer_or_order_quality; backlog_or_delivery_visibility | margin_bridge_pending_at_trigger; repeat_order_or_conversion_watch | none_at_trigger | none_at_trigger | current_profile_correct |
| 017960 | public_contract_disclosure; customer_or_order_quality; backlog_or_delivery_visibility | margin_bridge_absent_at_trigger; cash_conversion_absent_at_trigger | margin_or_backlog_slowdown_watch; high_MAE_after_contract_positive | none_confirmed | current_profile_false_positive |
| 071970 | customer_or_order_quality; capacity_or_volume_route; backlog_or_delivery_visibility; public_event_or_disclosure | confirmed_revision; durable_customer_confirmation_watch; margin_bridge_partial | event_premium_after_group_synergy_gap; high_MAE_absorption_required | none_confirmed | current_profile_correct |
| 097230 | public_event_or_disclosure; backlog_or_delivery_visibility; customer_or_order_quality | financial_visibility_partial; margin_bridge_pending; cash_conversion_pending | high_MAE_before_delayed_rerating; working_capital_conversion_watch | none_confirmed | current_profile_too_early |
| 042660 | backlog_or_delivery_visibility_survives; capacity_or_volume_route | margin_bridge_temporarily_broken; confirmed_revision_absent | margin_or_backlog_slowdown; oneoff_cost; execution_cost_noise | thesis_evidence_not_broken | current_profile_4C_too_early |
| 075580 | customer_or_order_quality; capacity_or_volume_route; backlog_or_delivery_visibility; early_revision_signal | confirmed_revision; margin_bridge; financial_visibility | price_only_local_peak_later_watch | none_at_trigger | current_profile_correct |


## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 033500 | 2023-01-25 | 11,000 | 5.64% | -3.18% | 13.36% | -7.82% | 38.36% | -7.82% | 2023-07-19 | 15,220 | -23.39% |
| 017960 | 2023-07-18 | 14,130 | 7.86% | -9.34% | 7.86% | -22.15% | 7.86% | -30.15% | 2023-08-10 | 15,240 | -35.24% |
| 071970 | 2023-08-01 | 11,660 | 23.84% | -15.69% | 23.84% | -23.76% | 49.74% | -23.76% | 2024-04-24 | 17,460 | -12.49% |
| 097230 | 2024-06-17 | 3,185 | 18.84% | -1.10% | 18.84% | -31.40% | 210.83% | -31.55% | 2025-03-06 | 9,900 | -21.82% |
| 042660 | 2024-07-29 | 30,100 | 17.28% | -15.61% | 36.38% | -15.61% | 199.00% | -15.61% | 2025-04-25 | 90,000 | -9.00% |
| 075580 | 2024-04-03 | 6,850 | 10.66% | -5.55% | 59.42% | -7.74% | 59.42% | -7.74% | 2024-07-17 | 10,920 | -41.58% |

Key read-throughs:

- `017960` is the clean false-positive: direct contract correction, but 180D MFE only `7.86%` versus 180D MAE `-30.15%`.
- `097230` is not a simple failure: 90D MAE was `-31.40%`, but 180D MFE reached `210.83%`. That is timing risk, not thesis death.
- `042660` shows why one-off loss should be 4B-watch before hard 4C: 180D MFE later reached `199.00%`.

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| How would current profile judge these rows? | It would accept most direct order/backlog rows as Stage2/Stage2-Actionable and risk hard 4C on severe margin disappointment. |
| Did that match MFE/MAE? | Mixed. Three rows aligned, three produced residual timing or false-positive errors. |
| Was Stage2 bonus excessive? | Excessive when the row had contract/backlog quantity but no margin/FCF bridge, especially 017960. |
| Was Yellow threshold 75 excessive? | Not globally. For C01, Yellow should depend more on margin/cash freshness than headline score. |
| Was Green threshold/revision excessive? | The threshold is fine, but C01 Green should require margin/working-capital conversion. |
| Was price-only blowoff guard appropriate? | Kept; this loop does not weaken it. |
| Was full 4B non-price requirement appropriate? | Strengthened; one-off execution cost is enough for watch, not necessarily full 4B thesis exit. |
| Was hard 4C too late or too early? | Too early if applied to one-off cost/loss without cancellation, customer loss, accounting break, or repeated cash damage. |

## 14. Stage2 / Yellow / Green Comparison

| symbol | trigger_type | Stage2 bridge quality | Stage3 bridge at trigger | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- | --- |
| 033500 | Stage2-Actionable | public_contract_disclosure;customer_or_order_quality;backlog_or_delivery_visibility | margin_bridge_pending_at_trigger;repeat_order_or_conversion_watch | not_applicable_no_stage3_green_trigger | contract_backlog_quality_positive_with_delayed_margin_confirmation |
| 017960 | Stage2-Actionable | public_contract_disclosure;customer_or_order_quality;backlog_or_delivery_visibility | margin_bridge_absent_at_trigger;cash_conversion_absent_at_trigger | not_applicable_no_stage3_green_trigger | contract_positive_but_near_term_price_path_failed |
| 071970 | Stage2-Actionable | customer_or_order_quality;capacity_or_volume_route;backlog_or_delivery_visibility;public_event_or_disclosure | confirmed_revision;durable_customer_confirmation_watch;margin_bridge_partial | not_applicable_no_stage3_green_trigger | high_MAE_absorbable_when_order_conversion_bridge_survives |
| 097230 | Stage2 | public_event_or_disclosure;backlog_or_delivery_visibility;customer_or_order_quality | financial_visibility_partial;margin_bridge_pending;cash_conversion_pending | not_applicable_no_stage3_green_trigger | delayed_structural_success_but_bad_90D_entry_risk |
| 042660 | Stage4B | backlog_or_delivery_visibility_survives;capacity_or_volume_route | margin_bridge_temporarily_broken;confirmed_revision_absent | not_applicable_no_stage3_green_trigger | oneoff_loss_4B_watch_not_hard_4C |
| 075580 | Stage2-Actionable | customer_or_order_quality;capacity_or_volume_route;backlog_or_delivery_visibility;early_revision_signal | confirmed_revision;margin_bridge;financial_visibility | not_applicable_no_stage3_green_trigger | customer_backlog_to_margin_recovery_positive |

No Stage3-Green trigger row is used in this loop. That is intentional: the target is the bridge between Stage2 and Green, especially the rows that look like Green candidates only because backlog/order text is strong.

## 15. 4B Local vs Full-window Timing Audit

| symbol | trigger_type | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | timing_verdict |
| --- | --- | --- | --- | --- | --- |
| 033500 | Stage2-Actionable | none_at_trigger | not_applicable_non_4B_row | not_applicable_non_4B_row | not_applicable_non_4B_row |
| 017960 | Stage2-Actionable | margin_or_backlog_slowdown_watch;high_MAE_after_contract_positive | not_applicable_non_4B_row | not_applicable_non_4B_row | not_applicable_non_4B_row |
| 071970 | Stage2-Actionable | event_premium_after_group_synergy_gap;high_MAE_absorption_required | not_applicable_non_4B_row | not_applicable_non_4B_row | not_applicable_non_4B_row |
| 097230 | Stage2 | high_MAE_before_delayed_rerating;working_capital_conversion_watch | not_applicable_non_4B_row | not_applicable_non_4B_row | not_applicable_non_4B_row |
| 042660 | Stage4B | margin_or_backlog_slowdown;oneoff_cost;execution_cost_noise | not_applicable_no_prior_stage2_in_same_case | not_applicable_no_prior_stage2_in_same_case | watch_not_full_4b_without_thesis_break |
| 075580 | Stage2-Actionable | price_only_local_peak_later_watch | not_applicable_non_4B_row | not_applicable_non_4B_row | not_applicable_non_4B_row |

C01 local 4B is useful when margin or execution quality worsens. It should not become hard 4C without terminal non-price evidence. `042660` is the guardrail row.

## 16. 4C Protection Audit

| symbol | stage4c_evidence_fields | four_c_protection_label | interpretation |
| --- | --- | --- | --- |
| 033500 | none_at_trigger | not_applicable_no_hard_4c | no 4C row |
| 017960 | none_confirmed | not_applicable_no_hard_4c | no 4C row |
| 071970 | none_confirmed | not_applicable_no_hard_4c | no 4C row |
| 097230 | none_confirmed | not_applicable_no_hard_4c | no 4C row |
| 042660 | thesis_evidence_not_broken | false_break_or_4c_overkill | hard 4C requires terminal non-price thesis break |
| 075580 | none_at_trigger | not_applicable_no_hard_4c | no 4C row |

No representative hard-4C row is proposed. The important discovery is a **negative 4C rule**: one messy quarter should not be allowed to impersonate thesis death.

## 17. Sector-Specific Rule Candidate

```text
L1 order/backlog evidence should be capped below Green unless realized margin, working-capital, or cash conversion is visible; direct customer quality can justify Stage2-Actionable, but backlog quantity alone must not inherit the same bonus as realized margin/FCF conversion.
```

Rule scope: `sector_specific`. It is supported by six L1 cases with both positive and counterexample rows.

## 18. Canonical-Archetype Rule Candidate

```text
C01 should separate backlog quantity from backlog quality, margin bridge, and FCF conversion. High-MAE rows with a surviving issuer bridge are timing-risk cases, not automatic 4C thesis death. One-off execution-cost or kitchen-sink losses should route to 4B-watch first unless cancellation, funding/customer loss, accounting/trust break, or repeated cash-flow damage confirms thesis death.
```

Rule scope: `canonical_archetype_specific`. It is more precise than the already-applied global Stage2 bridge rule because it specifies which bridge matters inside C01: margin and cash conversion, not backlog size alone.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 6 | 26.62% | -18.08% | 94.20% | -19.44% | 0.5 | mixed; three residual errors remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 6 | 26.62% | -18.08% | 94.20% | -19.44% | 0.67 | worse false-positive control |
| P1_L1_sector_specific_candidate_profile | sector_specific | 4 | 33.25% | -13.73% | 86.63% | -13.73% | 0.25 | improves false-positive control without losing positives |
| P2_C01_canonical_candidate_profile | canonical_archetype_specific | 3 | 32.21% | -13.11% | 49.17% | -13.11% | 0.0 | best alignment in this loop |
| P3_C01_counterexample_guard_profile | counterexample_guard | 3 | 21.03% | -23.05% | 139.23% | -25.77% | 0.33 | guards against both late 4B and over-eager 4C |

The best research proxy in this loop is `P2_C01_canonical_candidate_profile`: it filters weak backlog-only rows while preserving the rows where customer quality and margin conversion exist.

## 20. Score-Return Alignment Matrix

| symbol | before_score | before_stage | after_score | after_stage | MFE90 | MAE90 | MFE180 | alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 033500 | 76 | Stage2-Actionable | 78 | Stage2-Actionable | 13.36% | -7.82% | 38.36% | kept/accepted |
| 017960 | 74 | Stage2-Actionable | 62 | Stage2-watch | 7.86% | -22.15% | 7.86% | residual fixed or reduced |
| 071970 | 77 | Stage2-Actionable | 76 | Stage2-Actionable-with-high-MAE-watch | 23.84% | -23.76% | 49.74% | kept/accepted |
| 097230 | 72 | Stage2-Actionable | 64 | Stage2-watch | 18.84% | -31.40% | 210.83% | residual fixed or reduced |
| 042660 | 44 | Stage4C | 55 | Stage4B-watch | 36.38% | -15.61% | 199.00% | residual fixed or reduced |
| 075580 | 82 | Stage2-Actionable | 84 | Stage3-Yellow | 59.42% | -7.74% | 59.42% | kept/accepted |

Score mechanics: the shadow profile moves a small amount of emphasis away from `contract_score/backlog_visibility_score` when margin/cash conversion is absent, while increasing the importance of `margin_bridge_score` and revision/cash visibility when they are present.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR | 3 | 3 | 1 | 0 | 6 | 0 | 6 | 6 | 3 | yes | yes | C01 direct URL/MFE-MAE repair improved; still need direct FCF/cash-conversion disclosures beyond shipbuilding supply-chain rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: contract/backlog headline false positive; high-MAE delayed-rerating timing risk; one-off execution-cost hard-4C overkill risk
new_axis_proposed: c01_backlog_quality_margin_fcf_conversion_gate_and_high_mae_absorption_guard
existing_axis_strengthened: stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard; full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_qualified_for_oneoff_execution_cost_only
existing_axis_kept: price_only_blowoff_blocks_positive_stage; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: L1 order/backlog evidence should be capped below Green unless realized margin, working-capital, or cash conversion is visible; direct customer quality can justify Stage2-Actionable, but backlog quantity alone must not inherit the same bonus as realized margin/FCF conversion.
canonical_archetype_rule_candidate: C01 should separate backlog quantity from backlog quality, margin bridge, and FCF conversion. High-MAE rows with a surviving issuer bridge are timing-risk cases, not automatic 4C thesis death. One-off execution-cost or kitchen-sink losses should route to 4B-watch first unless cancellation, funding/customer loss, accounting/trust break, or repeated cash-flow damage confirms thesis death.
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

```yaml
validation_scope:
  stock_agent_code_opened: false
  stock_agent_code_patched: false
  live_candidate_scan: false
  current_stock_recommendation: false
  brokerage_api_used: false
  production_scoring_changed: false
  price_data_source: Songdaiki/stock-web
  actual_1d_ohlc_rows_used: true
  forward_window_minimum: 180 trading days
  corporate_action_block_enabled: true
  representative_trigger_count: 6
  rows_missing_required_mfe_mae: 0
non_validation_scope:
  no_current_live_discovery: true
  no_auto_trading: true
  no_stock_agent_src_access: true
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c01_backlog_headline_weight,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,20,17,-3,"headline/backlog-only rows over-promote when margin/FCF bridge is absent","reduced 017960/097230 false-positive pressure","C01_L210_TRG_02_017960_20230718|C01_L210_TRG_04_097230_20240617",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c01_margin_fcf_conversion_weight,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,15,18,+3,"realized margin/working-capital/FCF conversion explains positive rows better than headline size","kept 033500/075580 positives while capping weak contract-only row","C01_L210_TRG_01_033500_20230125|C01_L210_TRG_06_075580_20240403",6,6,3,medium,canonical_shadow_only,"not production; requires batch confirmation"
shadow_weight,c01_oneoff_4c_qualification_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,1,1,0,"qualify hard-4C route for one-off cost/loss rows unless thesis death is confirmed","prevents 042660 one-off loss from hard-4C overkill","C01_L210_TRG_05_042660_20240729",6,6,3,medium,guardrail_shadow_only,"axis qualification only; production unchanged"
```

The proposed changes are shadow-only. They are a later batch-ingest candidate, not a production scoring update.

## 25. Machine-Readable Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "C01_L210_TRG_01_033500_20230125", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_01_033500_20230120", "case_type": "structural_success", "company_name": "동성화인텍", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "notes": "삼성중공업향 LNG운반선 초저온 보냉자재 공급계약. 계약금액 571.4억원, 최근 매출액 대비 15.7%, 계약기간 2023-01-19~2027-11-30.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "aligned", "symbol": "033500"}
{"best_trigger": "C01_L210_TRG_02_017960_20230718", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_02_017960_20230717", "case_type": "failed_rerating", "company_name": "한국카본", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "notes": "LNG선 보냉재 공급계약 정정. 계약금액 증가가 확인됐지만 이후 180D 가격경로는 MAE가 깊고 MFE가 낮아 계약금액 증액만으로는 Green이 부족한 사례.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "residual_error_or_guardrail_needed", "symbol": "017960"}
{"best_trigger": "C01_L210_TRG_03_071970_20230801", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_03_071970_20230731", "case_type": "high_mae_success", "company_name": "HD현대마린엔진", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "notes": "STX중공업/HD현대마린엔진의 선박용 저속엔진, HD현대그룹 편입 기대, 2023~2025 실적 추정 개선 및 2023-04-25 케이조선 선박엔진 공급계약.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "aligned", "symbol": "071970"}
{"best_trigger": "C01_L210_TRG_04_097230_20240617", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_04_097230_20240614", "case_type": "high_mae_success", "company_name": "HJ중공업", "current_profile_verdict": "current_profile_too_early", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "notes": "2024년 3월 말 연결 기준 조선 수주잔고 1조4606억원, 건설 수주잔고 5조4883억원, 총 6조6489억원으로 2023년 매출 기준 3년 이상 일감이라는 기사.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "residual_error_or_guardrail_needed", "symbol": "097230"}
{"best_trigger": "C01_L210_TRG_05_042660_20240729", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_05_042660_20240726", "case_type": "4B_overlay_success", "company_name": "한화오션", "current_profile_verdict": "current_profile_4C_too_early", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "notes": "2024년 2분기 매출 2조5361억원, 영업손실 96억원. 컨테이너 적자호선·외주비·생산 안정화 비용 등으로 적자를 기록했지만 수주/건조 물량과 반복 생산체계는 유지.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "residual_error_or_guardrail_needed", "symbol": "042660"}
{"best_trigger": "C01_L210_TRG_06_075580_20240403", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_06_075580_20240402", "case_type": "structural_success", "company_name": "세진중공업", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "notes": "Deck House와 LPG Tank 중심, HD현대중공업·현대미포 등 주력 고객사의 수주잔고 증가로 Deck House 공급척수 증가와 2024년 두 자리수 영업이익률 회복 전망.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "aligned", "symbol": "075580"}
{"MAE_180D_pct": -7.82, "MAE_1Y_pct": -7.82, "MAE_30D_pct": -3.18, "MAE_90D_pct": -7.82, "MFE_180D_pct": 38.36, "MFE_1Y_pct": 38.36, "MFE_2Y_pct": 112.73, "MFE_30D_pct": 5.64, "MFE_90D_pct": 13.36, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_01_033500_20230120", "company_name": "동성화인텍", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -23.39, "entry_date": "2023-01-25", "entry_price": 11000.0, "evidence_available_at_that_date": "삼성중공업향 LNG운반선 초저온 보냉자재 공급계약. 계약금액 571.4억원, 최근 매출액 대비 15.7%, 계약기간 2023-01-19~2027-11-30.", "evidence_source": "https://www.hankyung.com/article/202301205854L", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["none_at_trigger"], "four_b_full_window_peak_proximity": "not_applicable_non_4B_row", "four_b_local_peak_proximity": "not_applicable_non_4B_row", "four_b_timing_verdict": "not_applicable_non_4B_row", "four_c_protection_label": "not_applicable_no_hard_4c", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "loop_objective": "counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair", "peak_date": "2023-07-19", "peak_price": 15220.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/033/033500/2023.csv", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/033/033500.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_L210_033500_20230125", "sector": "shipbuilding_LNG_insulation_materials", "stage2_evidence_fields": ["public_contract_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["margin_bridge_pending_at_trigger", "repeat_order_or_conversion_watch"], "stage4b_evidence_fields": ["none_at_trigger"], "stage4c_evidence_fields": ["none_at_trigger"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "033500", "trigger_date": "2023-01-20", "trigger_id": "C01_L210_TRG_01_033500_20230125", "trigger_outcome_label": "contract_backlog_quality_positive_with_delayed_margin_confirmation", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -30.15, "MAE_1Y_pct": -30.15, "MAE_30D_pct": -9.34, "MAE_90D_pct": -22.15, "MFE_180D_pct": 7.86, "MFE_1Y_pct": 7.86, "MFE_2Y_pct": 132.48, "MFE_30D_pct": 7.86, "MFE_90D_pct": 7.86, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_02_017960_20230717", "company_name": "한국카본", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -35.24, "entry_date": "2023-07-18", "entry_price": 14130.0, "evidence_available_at_that_date": "LNG선 보냉재 공급계약 정정. 계약금액 증가가 확인됐지만 이후 180D 가격경로는 MAE가 깊고 MFE가 낮아 계약금액 증액만으로는 Green이 부족한 사례.", "evidence_source": "https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20230717000119&docno=&method=searchInitInfo", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown_watch", "high_MAE_after_contract_positive"], "four_b_full_window_peak_proximity": "not_applicable_non_4B_row", "four_b_local_peak_proximity": "not_applicable_non_4B_row", "four_b_timing_verdict": "not_applicable_non_4B_row", "four_c_protection_label": "not_applicable_no_hard_4c", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "loop_objective": "counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair", "peak_date": "2023-08-10", "peak_price": 15240.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017960/2023.csv", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/017/017960.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_L210_017960_20230718", "sector": "shipbuilding_LNG_insulation_materials", "stage2_evidence_fields": ["public_contract_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["margin_bridge_absent_at_trigger", "cash_conversion_absent_at_trigger"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown_watch", "high_MAE_after_contract_positive"], "stage4c_evidence_fields": ["none_confirmed"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "017960", "trigger_date": "2023-07-17", "trigger_id": "C01_L210_TRG_02_017960_20230718", "trigger_outcome_label": "contract_positive_but_near_term_price_path_failed", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -23.76, "MAE_1Y_pct": -23.76, "MAE_30D_pct": -15.69, "MAE_90D_pct": -23.76, "MFE_180D_pct": 49.74, "MFE_1Y_pct": 113.12, "MFE_2Y_pct": null, "MFE_30D_pct": 23.84, "MFE_90D_pct": 23.84, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_03_071970_20230731", "company_name": "HD현대마린엔진", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -12.49, "entry_date": "2023-08-01", "entry_price": 11660.0, "evidence_available_at_that_date": "STX중공업/HD현대마린엔진의 선박용 저속엔진, HD현대그룹 편입 기대, 2023~2025 실적 추정 개선 및 2023-04-25 케이조선 선박엔진 공급계약.", "evidence_source": "https://www.shinyoung.com/files/20230801/51c974724b345.pdf | https://kr.investing.com/news/stock-market-news/article-902549", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["event_premium_after_group_synergy_gap", "high_MAE_absorption_required"], "four_b_full_window_peak_proximity": "not_applicable_non_4B_row", "four_b_local_peak_proximity": "not_applicable_non_4B_row", "four_b_timing_verdict": "not_applicable_non_4B_row", "four_c_protection_label": "not_applicable_no_hard_4c", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "loop_objective": "counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair", "peak_date": "2024-04-24", "peak_price": 17460.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071970/2023.csv", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/071/071970.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_L210_071970_20230801", "sector": "ship_engine_supply_chain", "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route", "backlog_or_delivery_visibility", "public_event_or_disclosure"], "stage3_evidence_fields": ["confirmed_revision", "durable_customer_confirmation_watch", "margin_bridge_partial"], "stage4b_evidence_fields": ["event_premium_after_group_synergy_gap", "high_MAE_absorption_required"], "stage4c_evidence_fields": ["none_confirmed"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "071970", "trigger_date": "2023-07-31", "trigger_id": "C01_L210_TRG_03_071970_20230801", "trigger_outcome_label": "high_MAE_absorbable_when_order_conversion_bridge_survives", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -31.55, "MAE_1Y_pct": -31.55, "MAE_30D_pct": -1.1, "MAE_90D_pct": -31.4, "MFE_180D_pct": 210.83, "MFE_1Y_pct": 210.83, "MFE_2Y_pct": null, "MFE_30D_pct": 18.84, "MFE_90D_pct": 18.84, "aggregate_group_role": "representative", "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_04_097230_20240614", "company_name": "HJ중공업", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_too_early", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -21.82, "entry_date": "2024-06-17", "entry_price": 3185.0, "evidence_available_at_that_date": "2024년 3월 말 연결 기준 조선 수주잔고 1조4606억원, 건설 수주잔고 5조4883억원, 총 6조6489억원으로 2023년 매출 기준 3년 이상 일감이라는 기사.", "evidence_source": "https://www.ibtomato.com/ExternalView.aspx?no=12416&type=1", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["high_MAE_before_delayed_rerating", "working_capital_conversion_watch"], "four_b_full_window_peak_proximity": "not_applicable_non_4B_row", "four_b_local_peak_proximity": "not_applicable_non_4B_row", "four_b_timing_verdict": "not_applicable_non_4B_row", "four_c_protection_label": "not_applicable_no_hard_4c", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "loop_objective": "counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair", "peak_date": "2025-03-06", "peak_price": 9900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/097/097230.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_L210_097230_20240617", "sector": "shipbuilding_construction_backlog_mix", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility_partial", "margin_bridge_pending", "cash_conversion_pending"], "stage4b_evidence_fields": ["high_MAE_before_delayed_rerating", "working_capital_conversion_watch"], "stage4c_evidence_fields": ["none_confirmed"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "097230", "trigger_date": "2024-06-14", "trigger_id": "C01_L210_TRG_04_097230_20240617", "trigger_outcome_label": "delayed_structural_success_but_bad_90D_entry_risk", "trigger_type": "Stage2"}
{"MAE_180D_pct": -15.61, "MAE_1Y_pct": -15.61, "MAE_30D_pct": -15.61, "MAE_90D_pct": -15.61, "MFE_180D_pct": 199.0, "MFE_1Y_pct": 296.68, "MFE_2Y_pct": null, "MFE_30D_pct": 17.28, "MFE_90D_pct": 36.38, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_05_042660_20240726", "company_name": "한화오션", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_4C_too_early", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -9.0, "entry_date": "2024-07-29", "entry_price": 30100.0, "evidence_available_at_that_date": "2024년 2분기 매출 2조5361억원, 영업손실 96억원. 컨테이너 적자호선·외주비·생산 안정화 비용 등으로 적자를 기록했지만 수주/건조 물량과 반복 생산체계는 유지.", "evidence_source": "https://www.yna.co.kr/view/AKR20240726088500527 | https://www.businesspost.co.kr/BP?command=article_view&num=360326", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "oneoff_cost", "execution_cost_noise"], "four_b_full_window_peak_proximity": "not_applicable_no_prior_stage2_in_same_case", "four_b_local_peak_proximity": "not_applicable_no_prior_stage2_in_same_case", "four_b_timing_verdict": "watch_not_full_4b_without_thesis_break", "four_c_protection_label": "false_break_or_4c_overkill", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "loop_objective": "counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair", "peak_date": "2025-04-25", "peak_price": 90000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/042/042660.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_L210_042660_20240729", "sector": "large_shipbuilder", "stage2_evidence_fields": ["backlog_or_delivery_visibility_survives", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge_temporarily_broken", "confirmed_revision_absent"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "oneoff_cost", "execution_cost_noise"], "stage4c_evidence_fields": ["thesis_evidence_not_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "042660", "trigger_date": "2024-07-26", "trigger_id": "C01_L210_TRG_05_042660_20240729", "trigger_outcome_label": "oneoff_loss_4B_watch_not_hard_4C", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -7.74, "MAE_1Y_pct": -7.74, "MAE_30D_pct": -5.55, "MAE_90D_pct": -7.74, "MFE_180D_pct": 59.42, "MFE_1Y_pct": 59.42, "MFE_2Y_pct": null, "MFE_30D_pct": 10.66, "MFE_90D_pct": 59.42, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_06_075580_20240402", "company_name": "세진중공업", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.58, "entry_date": "2024-04-03", "entry_price": 6850.0, "evidence_available_at_that_date": "Deck House와 LPG Tank 중심, HD현대중공업·현대미포 등 주력 고객사의 수주잔고 증가로 Deck House 공급척수 증가와 2024년 두 자리수 영업이익률 회복 전망.", "evidence_source": "https://ssl.pstatic.net/imgstock/upload/research/company/1712013384054.pdf", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak_later_watch"], "four_b_full_window_peak_proximity": "not_applicable_non_4B_row", "four_b_local_peak_proximity": "not_applicable_non_4B_row", "four_b_timing_verdict": "not_applicable_non_4B_row", "four_c_protection_label": "not_applicable_no_hard_4c", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "loop_objective": "counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; direct_url_proxy_mfe_mae_repair", "peak_date": "2024-07-17", "peak_price": 10920.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075580/2024.csv", "primary_archetype": "order_backlog_margin_bridge", "profile_path": "atlas/symbol_profiles/075/075580.json", "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_L210_075580_20240403", "sector": "shipbuilding_modules_tank_deckhouse", "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak_later_watch"], "stage4c_evidence_fields": ["none_at_trigger"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "075580", "trigger_date": "2024-04-02", "trigger_id": "C01_L210_TRG_06_075580_20240403", "trigger_outcome_label": "customer_backlog_to_margin_recovery_positive", "trigger_type": "Stage2-Actionable"}
{"MAE_90D_pct": -7.82, "MFE_90D_pct": 13.36, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_01_033500_20230120", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C01 shadow shifts emphasis from order/backlog headline toward realized margin/working-capital/FCF conversion and treats one-off execution-cost loss as 4B-watch before hard 4C.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c01_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 8, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "margin_bridge_score": 3, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 3, "valuation_repricing_score": 5}, "raw_component_scores_before": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 8, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "margin_bridge_score": 3, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 3, "valuation_repricing_score": 5}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage2-Actionable", "symbol": "033500", "trigger_id": "C01_L210_TRG_01_033500_20230125", "weighted_score_after": 78, "weighted_score_before": 76}
{"MAE_90D_pct": -22.15, "MFE_90D_pct": 7.86, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_02_017960_20230717", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C01 shadow shifts emphasis from order/backlog headline toward realized margin/working-capital/FCF conversion and treats one-off execution-cost loss as 4B-watch before hard 4C.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c01_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 8, "contract_score": 6, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "margin_bridge_score": 1, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 2, "valuation_repricing_score": 5}, "raw_component_scores_before": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 8, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "margin_bridge_score": 2, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 2, "valuation_repricing_score": 5}, "row_type": "score_simulation", "score_return_alignment_label": "residual_error_reduced_by_shadow_gate", "stage_label_after": "Stage2-watch", "stage_label_before": "Stage2-Actionable", "symbol": "017960", "trigger_id": "C01_L210_TRG_02_017960_20230718", "weighted_score_after": 62, "weighted_score_before": 74}
{"MAE_90D_pct": -23.76, "MFE_90D_pct": 23.84, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_03_071970_20230731", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C01 shadow shifts emphasis from order/backlog headline toward realized margin/working-capital/FCF conversion and treats one-off execution-cost loss as 4B-watch before hard 4C.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c01_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 8, "contract_score": 4, "customer_quality_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "margin_bridge_score": 8, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 7, "valuation_repricing_score": 5}, "raw_component_scores_before": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 8, "contract_score": 4, "customer_quality_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "margin_bridge_score": 6, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 6, "valuation_repricing_score": 5}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage2-Actionable-with-high-MAE-watch", "stage_label_before": "Stage2-Actionable", "symbol": "071970", "trigger_id": "C01_L210_TRG_03_071970_20230801", "weighted_score_after": 76, "weighted_score_before": 77}
{"MAE_90D_pct": -31.4, "MFE_90D_pct": 18.84, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_04_097230_20240614", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C01 shadow shifts emphasis from order/backlog headline toward realized margin/working-capital/FCF conversion and treats one-off execution-cost loss as 4B-watch before hard 4C.", "current_profile_verdict": "current_profile_too_early", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c01_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 4, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "margin_bridge_score": 3, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 3, "valuation_repricing_score": 3}, "raw_component_scores_before": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 4, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "margin_bridge_score": 3, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 3, "valuation_repricing_score": 5}, "row_type": "score_simulation", "score_return_alignment_label": "residual_error_reduced_by_shadow_gate", "stage_label_after": "Stage2-watch", "stage_label_before": "Stage2-Actionable", "symbol": "097230", "trigger_id": "C01_L210_TRG_04_097230_20240617", "weighted_score_after": 64, "weighted_score_before": 72}
{"MAE_90D_pct": -15.61, "MFE_90D_pct": 36.38, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_05_042660_20240726", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C01 shadow shifts emphasis from order/backlog headline toward realized margin/working-capital/FCF conversion and treats one-off execution-cost loss as 4B-watch before hard 4C.", "current_profile_verdict": "current_profile_4C_too_early", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c01_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 4, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 7, "legal_or_contract_risk_score": 1, "margin_bridge_score": 2, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 1, "valuation_repricing_score": 5}, "raw_component_scores_before": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 4, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "margin_bridge_score": 2, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 1, "valuation_repricing_score": 5}, "row_type": "score_simulation", "score_return_alignment_label": "residual_error_reduced_by_shadow_gate", "stage_label_after": "Stage4B-watch", "stage_label_before": "Stage4C", "symbol": "042660", "trigger_id": "C01_L210_TRG_05_042660_20240729", "weighted_score_after": 55, "weighted_score_before": 44}
{"MAE_90D_pct": -7.74, "MFE_90D_pct": 59.42, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_L210_CASE_06_075580_20240402", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C01 shadow shifts emphasis from order/backlog headline toward realized margin/working-capital/FCF conversion and treats one-off execution-cost loss as 4B-watch before hard 4C.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c01_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 4, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "margin_bridge_score": 9, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 7, "valuation_repricing_score": 5}, "raw_component_scores_before": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 9, "contract_score": 4, "customer_quality_score": 7, "dilution_cb_risk_score": 0, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "margin_bridge_score": 7, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 6, "valuation_repricing_score": 5}, "row_type": "score_simulation", "score_return_alignment_label": "aligned", "stage_label_after": "Stage3-Yellow", "stage_label_before": "Stage2-Actionable", "symbol": "075580", "trigger_id": "C01_L210_TRG_06_075580_20240403", "weighted_score_after": 84, "weighted_score_before": 82}
{"avg_MAE_180D_pct": -19.44, "avg_MAE_90D_pct": -18.08, "avg_MFE_180D_pct": 94.2, "avg_MFE_90D_pct": 26.62, "avg_four_b_full_window_peak_proximity": "not_applicable_or_watch_only", "avg_four_b_local_peak_proximity": "not_applicable_or_watch_only", "avg_green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "none", "changed_thresholds": "none", "eligible_trigger_count": 6, "false_positive_rate": 0.5, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 0, "loop": 210, "missed_structural_count": 0, "profile_hypothesis": "Current calibrated profile, before C01-specific backlog-to-FCF refinement.", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "mixed; three residual errors remain", "selected_entry_trigger_per_case": "C01_L210_TRG_01_033500_20230125|C01_L210_TRG_02_017960_20230718|C01_L210_TRG_03_071970_20230801|C01_L210_TRG_04_097230_20240617|C01_L210_TRG_05_042660_20240729|C01_L210_TRG_06_075580_20240403", "selected_symbols": ["033500", "017960", "071970", "097230", "042660", "075580"]}
{"avg_MAE_180D_pct": -19.44, "avg_MAE_90D_pct": -18.08, "avg_MFE_180D_pct": 94.2, "avg_MFE_90D_pct": 26.62, "avg_four_b_full_window_peak_proximity": "not_applicable_or_watch_only", "avg_four_b_local_peak_proximity": "not_applicable_or_watch_only", "avg_green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "rollback to old baseline", "changed_thresholds": "looser Stage2 bridge; weaker 4B/4C guard", "eligible_trigger_count": 6, "false_positive_rate": 0.67, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 0, "loop": 210, "missed_structural_count": 0, "profile_hypothesis": "Older headline/backlog-friendly baseline; useful only as rollback reference.", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "worse false-positive control", "selected_entry_trigger_per_case": "C01_L210_TRG_01_033500_20230125|C01_L210_TRG_02_017960_20230718|C01_L210_TRG_03_071970_20230801|C01_L210_TRG_04_097230_20240617|C01_L210_TRG_05_042660_20240729|C01_L210_TRG_06_075580_20240403", "selected_symbols": ["033500", "017960", "071970", "097230", "042660", "075580"]}
{"avg_MAE_180D_pct": -13.73, "avg_MAE_90D_pct": -13.73, "avg_MFE_180D_pct": 86.63, "avg_MFE_90D_pct": 33.25, "avg_four_b_full_window_peak_proximity": "not_applicable_or_watch_only", "avg_four_b_local_peak_proximity": "not_applicable_or_watch_only", "avg_green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "stage2_required_bridge strengthened for order/backlog; local 4B watch guard kept", "changed_thresholds": "Green capped below 87 without margin/FCF conversion", "eligible_trigger_count": 4, "false_positive_rate": 0.25, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 0, "loop": 210, "missed_structural_count": 0, "profile_hypothesis": "L1 order/backlog rows need margin/cash bridge before Green promotion.", "profile_id": "P1_L1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "improves false-positive control without losing positives", "selected_entry_trigger_per_case": "C01_L210_TRG_01_033500_20230125|C01_L210_TRG_03_071970_20230801|C01_L210_TRG_05_042660_20240729|C01_L210_TRG_06_075580_20240403", "selected_symbols": ["033500", "071970", "075580", "042660"]}
{"avg_MAE_180D_pct": -13.11, "avg_MAE_90D_pct": -13.11, "avg_MFE_180D_pct": 49.17, "avg_MFE_90D_pct": 32.21, "avg_four_b_full_window_peak_proximity": "not_applicable_or_watch_only", "avg_four_b_local_peak_proximity": "not_applicable_or_watch_only", "avg_green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "c01_backlog_quality_margin_fcf_conversion_gate_and_high_mae_absorption_guard", "changed_thresholds": "Stage2-Actionable requires direct customer or delivery route; Yellow/Green requires margin/cash freshness", "eligible_trigger_count": 3, "false_positive_rate": 0.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 0, "loop": 210, "missed_structural_count": 0, "profile_hypothesis": "C01 separates backlog quantity, backlog quality, margin bridge, and FCF conversion.", "profile_id": "P2_C01_canonical_candidate_profile", "profile_scope": "canonical_archetype_specific", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "best alignment in this loop", "selected_entry_trigger_per_case": "C01_L210_TRG_01_033500_20230125|C01_L210_TRG_03_071970_20230801|C01_L210_TRG_06_075580_20240403", "selected_symbols": ["033500", "071970", "075580"]}
{"avg_MAE_180D_pct": -25.77, "avg_MAE_90D_pct": -23.05, "avg_MFE_180D_pct": 139.23, "avg_MFE_90D_pct": 21.03, "avg_four_b_full_window_peak_proximity": "not_applicable_or_watch_only", "avg_four_b_local_peak_proximity": "not_applicable_or_watch_only", "avg_green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "changed_axes": "hard_4c_thesis_break_routes_to_4c qualification for one-off execution cost", "changed_thresholds": "Hard 4C requires cancellation/customer loss/accounting break/repeated cash damage", "eligible_trigger_count": 3, "false_positive_rate": 0.33, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "late_green_count": 0, "loop": 210, "missed_structural_count": 0, "profile_hypothesis": "High MAE alone is not hard 4C; one-off loss routes to 4B-watch before thesis death.", "profile_id": "P3_C01_counterexample_guard_profile", "profile_scope": "counterexample_guard", "round": "R1", "row_type": "profile_comparison", "score_return_alignment_verdict": "guards against both late 4B and over-eager 4C", "selected_entry_trigger_per_case": "C01_L210_TRG_02_017960_20230718|C01_L210_TRG_04_097230_20240617|C01_L210_TRG_05_042660_20240729", "selected_symbols": ["042660", "097230", "017960"]}
{"calibration_usable_case_count": 6, "calibration_usable_trigger_count": 6, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "counterexample_count": 3, "current_profile_error_count": 3, "do_not_propose_new_weight_delta": false, "fine_archetype_id": "C01_SHIPBUILDING_SUPPLYCHAIN_BACKLOG_TO_MARGIN_FCF_CONVERSION_REPAIR", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 6, "new_symbol_count": 6, "new_trigger_family_count": 6, "positive_case_count": 3, "production_scoring_changed": false, "representative_trigger_count": 6, "residual_contribution": "c01_backlog_quality_margin_fcf_conversion_gate_and_high_mae_absorption_guard", "reused_case_count": 0, "round": "R1", "row_type": "aggregate", "same_archetype_new_symbol_count": 6, "same_archetype_new_trigger_family_count": 6, "shadow_weight_only": true}
{"canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "canonical_archetype_rule_candidate": "C01 should separate backlog quantity from backlog quality, margin bridge, and FCF conversion. High-MAE rows with a surviving issuer bridge are timing-risk cases, not automatic 4C thesis death. One-off execution-cost or kitchen-sink losses should route to 4B-watch first unless cancellation, funding/customer loss, accounting/trust break, or repeated cash-flow damage confirms thesis death.", "do_not_propose_new_weight_delta": false, "existing_axis_strengthened": "stage2_required_bridge; stage3_green_revision_min_by_margin_cash_freshness; local_4b_watch_guard; full_4b_requires_non_price_evidence", "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_qualified_for_oneoff_execution_cost_only", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 210, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "c01_backlog_quality_margin_fcf_conversion_gate_and_high_mae_absorption_guard", "new_independent_case_count": 6, "new_symbol_count": 6, "new_trigger_family_count": 6, "residual_error_types_found": ["contract/backlog headline false positive", "high-MAE delayed-rerating timing risk", "one-off cost hard-4C overkill risk"], "reused_case_count": 0, "round": "R1", "row_type": "residual_contribution", "sector_specific_rule_candidate": "L1 order/backlog evidence should be capped below Green unless realized margin, working-capital, or cash conversion is visible; direct customer quality can justify Stage2-Actionable, but backlog quantity alone must not inherit the same bonus as realized margin/FCF conversion.", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"]}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

```md
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
```

## 27. Next Round State

```text
completed_round = R1
completed_loop = 210
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C01 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
next_recommended_archetypes = C13 direct AMPC/utilization rows; C10 direct order-conversion rows; C31 direct awarded-cashflow rows; C15 spread freshness rows only if non-duplicate; C01 only if new direct FCF/cash-conversion source rows are available
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` was used as the execution procedure.
- `docs/core/V12_Research_No_Repeat_Index.md` was used only as duplicate/coverage ledger.
- `Songdaiki/stock-web` manifest and schema were used as the price-source authority.
- Local OHLC shard files used: atlas/ohlcv_tradable_by_symbol_year/017/017960/2023.csv, atlas/ohlcv_tradable_by_symbol_year/033/033500/2023.csv, atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv, atlas/ohlcv_tradable_by_symbol_year/071/071970/2023.csv, atlas/ohlcv_tradable_by_symbol_year/075/075580/2024.csv, atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv.
