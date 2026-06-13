---
expected_v12_result_file: true
filename_pattern_pass: true
filename_matches_metadata: true
selected_round: R3
selected_loop: 96
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: mixed_C14_ev_slowdown_order_cut_offset_guard_set
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective: coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 5
reused_case_count: 0
calibration_usable_trigger_count: 5
representative_trigger_count: 5
positive_case_count: 2
counterexample_count: 3
four_b_case_count: 3
four_c_case_count: 2
current_profile_error_count: 3
do_not_propose_new_weight_delta: false
---

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

File: `e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md`

## 0. Research Metadata
| field | value |
| --- | --- |
| expected_v12_result_file | true |
| filename_pattern_pass | true |
| filename_matches_metadata | true |
| selected_round | R3 |
| selected_loop | 96 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C |
| fine_archetype_id | mixed_C14_ev_slowdown_order_cut_offset_guard_set |
| selection_basis | docs/core/V12_Research_No_Repeat_Index.md |
| selected_priority_bucket | Priority 0 / under 30 rows |
| round_schedule_status | coverage_index_selected |
| round_sector_consistency | pass |
| loop_objective | coverage_gap_fill | counterexample_mining | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression |
| price_source | Songdaiki/stock-web |
| stock_web_manifest_max_date | 2026-02-20 |
| new_independent_case_count | 5 |
| reused_case_count | 0 |
| calibration_usable_trigger_count | 5 |
| representative_trigger_count | 5 |
| positive_case_count | 2 |
| counterexample_count | 3 |
| four_b_case_count | 3 |
| four_c_case_count | 2 |
| current_profile_error_count | 3 |
| do_not_propose_new_weight_delta | false |

## 1. Current Calibrated Profile Assumption

Assumption: the active production selector is the post-stock-web E2R 2.2 family, but this MD treats every scoring change as shadow-only. The stress test is not the old global claim that hard 4C exists. It asks whether C14 still needs a narrower split between **true customer/order/ASP/production break** and **EV-slowdown offset cases** where US localization, ESS demand, or named customer capacity can make a blanket hard-4C route too pessimistic.

## 2. Round / Large Sector / Canonical Archetype Scope
| scope item | value |
| --- | --- |
| selected_round | R3 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C |
| fine_archetype_id | mixed_C14_ev_slowdown_order_cut_offset_guard_set |
| allowed purpose | historical residual calibration only; no live recommendation; no production patch |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat ledger marks C14 as Priority 0 / under 30 rows, with rows=11 and need-to-30=19. The ledger's visible top-covered C14 symbols include 001570, 002710, 020150, 051910, 066970, and 078600. This loop avoids those visible top-covered symbols and also avoids the prior session-local C14 case set 361610/006400/003670/247540/373220.

| symbol | novelty key | reuse status |
| --- | --- | --- |
| 093370 | C14_EV_DEMAND_SLOWDOWN_4B_4C|093370|Stage4C|2023-04-17 | new_independent_case |
| 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C|278280|Stage4C|2023-08-23 | new_independent_case |
| 348370 | C14_EV_DEMAND_SLOWDOWN_4B_4C|348370|Stage2-Actionable|2024-03-28 | new_independent_case |
| 121600 | C14_EV_DEMAND_SLOWDOWN_4B_4C|121600|Stage4B|2024-03-13 | new_independent_case |
| 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C|336370|Stage4B|2024-04-24 | new_independent_case |

## 4. Stock-Web OHLC Input / Price Source Validation

Price source is Songdaiki/stock-web tradable raw OHLCV. Formula: `MFE_N_pct = (max high from entry_date through N trading rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N trading rows / entry_price - 1) * 100`. All five rows have at least 180 forward trading rows before manifest max_date 2026-02-20.

| symbol | price_shard_path | profile_path | profile/corp-action summary | window_end | corporate_action_window_status |
| --- | --- | --- | --- | --- | --- |
| 093370 | atlas/ohlcv_tradable_by_symbol_year/093/093370/2023.csv|atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv | atlas/symbol_profiles/093/093370.json | KOSPI / active_like / corporate_action_candidate_count=0 | 2024-01-10 | clean_180D_window |
| 278280 | atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv|atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv | atlas/symbol_profiles/278/278280.json | KOSDAQ,KOSDAQ GLOBAL history / active_like / corporate_action_candidate_count=0 | 2024-05-21 | clean_180D_window |
| 348370 | atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv|atlas/ohlcv_tradable_by_symbol_year/348/348370/2025.csv | atlas/symbol_profiles/348/348370.json | KOSDAQ / active_like / corporate_action_candidate_count=0 | 2024-12-23 | clean_180D_window |
| 121600 | atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv|atlas/ohlcv_tradable_by_symbol_year/121/121600/2025.csv | atlas/symbol_profiles/121/121600.json | KOSDAQ / active_like / historical corporate_action_candidate_date=2015-12-17 only | 2024-12-05 | clean_180D_window |
| 336370 | atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv|atlas/ohlcv_tradable_by_symbol_year/336/336370/2025.csv | atlas/symbol_profiles/336/336370.json | KOSPI / active_like / corporate_action_candidate_dates=2024-01-08,2024-01-30; before selected 2024-04-24 entry window | 2025-01-20 | clean_180D_window |

## 5. Historical Eligibility Gate
| symbol | trigger_date | entry_date | entry_price | available 180D? | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | calibration_usable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 093370 | 2023-04-17 | 2023-04-17 | 14890 | yes | 4.1 | -26.12 | 4.1 | -35.86 | true |
| 278280 | 2023-08-22 | 2023-08-23 | 139800 | yes | 11.52 | -31.19 | 11.52 | -49.07 | true |
| 348370 | 2024-03-28 | 2024-03-28 | 236500 | yes | 66.81 | -37.0 | 66.81 | -54.33 | true |
| 121600 | 2024-03-13 | 2024-03-13 | 139800 | yes | 8.44 | -32.05 | 8.44 | -57.58 | true |
| 336370 | 2024-04-24 | 2024-04-24 | 19440 | yes | 20.88 | -38.68 | 20.88 | -60.91 | true |

## 6. Canonical Archetype Compression Map
| fine/deep family | mechanism | stage implication |
| --- | --- | --- |
| C14_LIPF6_PRODUCTION_HALT_INVENTORY_PRICE_COLLAPSE | production halt + customer inventory + ASP collapse | hard 4C route succeeds; positive-stage blocked |
| C14_LITHIUM_PRICE_DROP_PRODUCTION_DELAY_THESIS_BREAK | lithium/electrolyte ASP fall + shipment delay + capex timing stress | hard 4C or 4B-to-4C route |
| C14_US_LOCALIZATION_OFFSET_FALSE_HARD_4C | sector slowdown exists but US local supply/customer proximity offsets demand risk | Stage2-Actionable allowed, but blowoff requires 4B watch |
| C14_CNT_CAPA_GROWTH_STORY_WITH_EV_DEMAND_MAE | growth narrative and CAPA expansion without confirmed margin/FCF resilience | cap at 4B watch when MAE90/180 is severe |
| C14_COPPER_FOIL_REVENUE_GROWTH_WITH_FIXED_COST_LOSS_GUARD | volume/revenue improvement but fixed-cost loss remains | do not Green; 4B watch until loss bridge clears |

## 7. Case Selection Summary
| symbol | company | case_type | trigger_type | trigger_date | entry_date | fine_archetype_id |
| --- | --- | --- | --- | --- | --- | --- |
| 093370 | 후성 | hard_4c_protection_success | Stage4C | 2023-04-17 | 2023-04-17 | C14_LIPF6_PRODUCTION_HALT_INVENTORY_PRICE_COLLAPSE |
| 278280 | 천보 | hard_4c_protection_success | Stage4C | 2023-08-22 | 2023-08-23 | C14_LITHIUM_PRICE_DROP_PRODUCTION_DELAY_THESIS_BREAK |
| 348370 | 엔켐 | false_hard_4c_counterexample_with_4b_blowoff | Stage2-Actionable | 2024-03-28 | 2024-03-28 | C14_US_LOCALIZATION_OFFSET_FALSE_HARD_4C |
| 121600 | 나노신소재 | growth_story_high_mae_counterexample | Stage4B | 2024-03-13 | 2024-03-13 | C14_CNT_CAPA_GROWTH_STORY_WITH_EV_DEMAND_MAE |
| 336370 | 솔루스첨단소재 | loss_narrowing_revenue_growth_false_positive | Stage4B | 2024-04-24 | 2024-04-24 | C14_COPPER_FOIL_REVENUE_GROWTH_WITH_FIXED_COST_LOSS_GUARD |

## 8. Evidence Notes
| symbol | evidence summary | evidence_url |
| --- | --- | --- |
| 093370 | LiPF6 생산 중단, 전방 고객 재고조정, 자체 재고 증가, 원가 부담, LiPF6 가격 하락이 동시에 확인된 hard thesis break. | https://www.mk.co.kr/news/stock/10714626 |
| 278280 | 리튬 가격 하락으로 판가가 떨어졌고, 전해질 생산 중단/출하 급감, 설비 완공 지연까지 겹친 customer-demand/ASP thesis break. | https://dealsite.co.kr/articles/108862/068020 |
| 348370 | 2023년 EV 둔화 영향은 맞지만 2024년 북미 현지화/캐파 증설/고객 공장 인근 공급망이 구조적 offset으로 작동한 false hard-4C 케이스. | https://ssl.pstatic.net/imgstock/upload/research/company/1711582963859.pdf |
| 121600 | CNT 도전재 해외 양산과 사상최대 실적 기대는 있었지만, 실제 90/180D 경로는 EV/battery 소재 risk-off를 크게 맞은 Stage4B watch 케이스. | https://www.newspim.com/news/view/20240313000094 |
| 336370 | 1Q24 매출 증가와 영업손실 축소 뉴스는 positive처럼 보였지만, 전지박 고정비/적자 부담이 남아 180D MAE가 크게 벌어진 4B guard 케이스. | https://securities.miraeasset.com/bbs/download/2125875.pdf?attachmentId=2125875 |

## 9. Backtest Price Path by Trigger
| symbol | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date/price | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 093370 | 2023-04-17 @ 14890 | 4.1 | -15.78 | 4.1 | -26.12 | 4.1 | -35.86 | 2023-04-18 / 15500 | -38.39% by 2023-10-26 |
| 278280 | 2023-08-23 @ 139800 | 11.52 | -16.88 | 11.52 | -31.19 | 11.52 | -49.07 | 2023-08-30 / 155900 | -54.33% by 2024-04-19 |
| 348370 | 2024-03-28 @ 236500 | 66.81 | -5.07 | 66.81 | -37.0 | 66.81 | -54.33 | 2024-04-08 / 394500 | -72.62% by 2024-11-15 |
| 121600 | 2024-03-13 @ 139800 | 8.44 | -20.6 | 8.44 | -32.05 | 8.44 | -57.58 | 2024-03-19 / 151600 | -60.88% by 2024-11-15 |
| 336370 | 2024-04-24 @ 19440 | 3.65 | -20.27 | 20.88 | -38.68 | 20.88 | -60.91 | 2024-07-01 / 23500 | -67.66% by 2024-12-10 |

## 10. Current Calibrated Profile Stress Test

### 093370 후성 — hard_4c_protection_success

- Trigger: `Stage4C` on `2023-04-17`, entry `2023-04-17` close `14890`.
- Evidence: LiPF6 생산 중단, 전방 고객 재고조정, 자체 재고 증가, 원가 부담, LiPF6 가격 하락이 동시에 확인된 hard thesis break.
- Price path: 90D MFE `4.1%` / MAE `-26.12%`; 180D MFE `4.1%` / MAE `-35.86%`; peak `2023-04-18` at `15500`, drawdown-after-peak `-38.39%`.
- Current profile verdict: `current_profile_correct`.
- Proposed shadow stage: `Stage4C`.

### 278280 천보 — hard_4c_protection_success

- Trigger: `Stage4C` on `2023-08-22`, entry `2023-08-23` close `139800`.
- Evidence: 리튬 가격 하락으로 판가가 떨어졌고, 전해질 생산 중단/출하 급감, 설비 완공 지연까지 겹친 customer-demand/ASP thesis break.
- Price path: 90D MFE `11.52%` / MAE `-31.19%`; 180D MFE `11.52%` / MAE `-49.07%`; peak `2023-08-30` at `155900`, drawdown-after-peak `-54.33%`.
- Current profile verdict: `current_profile_correct`.
- Proposed shadow stage: `Stage4C`.

### 348370 엔켐 — false_hard_4c_counterexample_with_4b_blowoff

- Trigger: `Stage2-Actionable` on `2024-03-28`, entry `2024-03-28` close `236500`.
- Evidence: 2023년 EV 둔화 영향은 맞지만 2024년 북미 현지화/캐파 증설/고객 공장 인근 공급망이 구조적 offset으로 작동한 false hard-4C 케이스.
- Price path: 90D MFE `66.81%` / MAE `-37.0%`; 180D MFE `66.81%` / MAE `-54.33%`; peak `2024-04-08` at `394500`, drawdown-after-peak `-72.62%`.
- Current profile verdict: `current_profile_missed_structural`.
- Proposed shadow stage: `Stage2-Actionable+4B-watch`.

### 121600 나노신소재 — growth_story_high_mae_counterexample

- Trigger: `Stage4B` on `2024-03-13`, entry `2024-03-13` close `139800`.
- Evidence: CNT 도전재 해외 양산과 사상최대 실적 기대는 있었지만, 실제 90/180D 경로는 EV/battery 소재 risk-off를 크게 맞은 Stage4B watch 케이스.
- Price path: 90D MFE `8.44%` / MAE `-32.05%`; 180D MFE `8.44%` / MAE `-57.58%`; peak `2024-03-19` at `151600`, drawdown-after-peak `-60.88%`.
- Current profile verdict: `current_profile_false_positive`.
- Proposed shadow stage: `Stage4B-watch`.

### 336370 솔루스첨단소재 — loss_narrowing_revenue_growth_false_positive

- Trigger: `Stage4B` on `2024-04-24`, entry `2024-04-24` close `19440`.
- Evidence: 1Q24 매출 증가와 영업손실 축소 뉴스는 positive처럼 보였지만, 전지박 고정비/적자 부담이 남아 180D MAE가 크게 벌어진 4B guard 케이스.
- Price path: 90D MFE `20.88%` / MAE `-38.68%`; 180D MFE `20.88%` / MAE `-60.91%`; peak `2024-07-01` at `23500`, drawdown-after-peak `-67.66%`.
- Current profile verdict: `current_profile_false_positive`.
- Proposed shadow stage: `Stage4B-watch`.

## 11. Score Component Breakdown

The component values below are research proxy scores, not production scores. Risk keys such as execution_risk_score are intentionally high when risk evidence is present.


### Score simulation — 093370 후성

```json
{
  "symbol": "093370",
  "raw_component_scores_before": {
    "contract_score": 20,
    "backlog_visibility_score": 10,
    "margin_bridge_score": 5,
    "revision_score": 5,
    "relative_strength_score": 5,
    "customer_quality_score": 10,
    "policy_or_regulatory_score": 25,
    "valuation_repricing_score": 20,
    "execution_risk_score": 90,
    "legal_or_contract_risk_score": 20,
    "dilution_cb_risk_score": 10,
    "accounting_trust_risk_score": 15
  },
  "weighted_score_before": 38,
  "stage_label_before": "Stage4C",
  "raw_component_scores_after": {
    "contract_score": 20,
    "backlog_visibility_score": 10,
    "margin_bridge_score": 0,
    "revision_score": 5,
    "relative_strength_score": 5,
    "customer_quality_score": 10,
    "policy_or_regulatory_score": 25,
    "valuation_repricing_score": 20,
    "execution_risk_score": 100,
    "legal_or_contract_risk_score": 20,
    "dilution_cb_risk_score": 10,
    "accounting_trust_risk_score": 15
  },
  "weighted_score_after": 30,
  "stage_label_after": "Stage4C",
  "component_delta_explanation": "C14 hard 4C requires order-cut/utilization/production-halt/ASP collapse. US localization/ESS/customer offset prevents blanket 4C, while growth-only stories are capped by high-MAE 4B guard."
}
```

### Score simulation — 278280 천보

```json
{
  "symbol": "278280",
  "raw_component_scores_before": {
    "contract_score": 25,
    "backlog_visibility_score": 20,
    "margin_bridge_score": 5,
    "revision_score": 10,
    "relative_strength_score": 10,
    "customer_quality_score": 30,
    "policy_or_regulatory_score": 15,
    "valuation_repricing_score": 25,
    "execution_risk_score": 85,
    "legal_or_contract_risk_score": 25,
    "dilution_cb_risk_score": 40,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_before": 42,
  "stage_label_before": "Stage4C",
  "raw_component_scores_after": {
    "contract_score": 25,
    "backlog_visibility_score": 20,
    "margin_bridge_score": 0,
    "revision_score": 10,
    "relative_strength_score": 10,
    "customer_quality_score": 30,
    "policy_or_regulatory_score": 15,
    "valuation_repricing_score": 25,
    "execution_risk_score": 95,
    "legal_or_contract_risk_score": 25,
    "dilution_cb_risk_score": 40,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_after": 34,
  "stage_label_after": "Stage4C",
  "component_delta_explanation": "C14 hard 4C requires order-cut/utilization/production-halt/ASP collapse. US localization/ESS/customer offset prevents blanket 4C, while growth-only stories are capped by high-MAE 4B guard."
}
```

### Score simulation — 348370 엔켐

```json
{
  "symbol": "348370",
  "raw_component_scores_before": {
    "contract_score": 70,
    "backlog_visibility_score": 65,
    "margin_bridge_score": 45,
    "revision_score": 55,
    "relative_strength_score": 85,
    "customer_quality_score": 75,
    "policy_or_regulatory_score": 70,
    "valuation_repricing_score": 80,
    "execution_risk_score": 50,
    "legal_or_contract_risk_score": 15,
    "dilution_cb_risk_score": 25,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_before": 68,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 70,
    "backlog_visibility_score": 65,
    "margin_bridge_score": 45,
    "revision_score": 55,
    "relative_strength_score": 85,
    "customer_quality_score": 80,
    "policy_or_regulatory_score": 75,
    "valuation_repricing_score": 90,
    "execution_risk_score": 50,
    "legal_or_contract_risk_score": 15,
    "dilution_cb_risk_score": 25,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_after": 63,
  "stage_label_after": "Stage2-Actionable+4B-watch",
  "component_delta_explanation": "C14 hard 4C requires order-cut/utilization/production-halt/ASP collapse. US localization/ESS/customer offset prevents blanket 4C, while growth-only stories are capped by high-MAE 4B guard."
}
```

### Score simulation — 121600 나노신소재

```json
{
  "symbol": "121600",
  "raw_component_scores_before": {
    "contract_score": 45,
    "backlog_visibility_score": 50,
    "margin_bridge_score": 35,
    "revision_score": 60,
    "relative_strength_score": 45,
    "customer_quality_score": 45,
    "policy_or_regulatory_score": 25,
    "valuation_repricing_score": 70,
    "execution_risk_score": 60,
    "legal_or_contract_risk_score": 15,
    "dilution_cb_risk_score": 45,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_before": 66,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 45,
    "backlog_visibility_score": 50,
    "margin_bridge_score": 25,
    "revision_score": 60,
    "relative_strength_score": 45,
    "customer_quality_score": 45,
    "policy_or_regulatory_score": 25,
    "valuation_repricing_score": 75,
    "execution_risk_score": 70,
    "legal_or_contract_risk_score": 15,
    "dilution_cb_risk_score": 45,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_after": 48,
  "stage_label_after": "Stage4B-watch",
  "component_delta_explanation": "C14 hard 4C requires order-cut/utilization/production-halt/ASP collapse. US localization/ESS/customer offset prevents blanket 4C, while growth-only stories are capped by high-MAE 4B guard."
}
```

### Score simulation — 336370 솔루스첨단소재

```json
{
  "symbol": "336370",
  "raw_component_scores_before": {
    "contract_score": 50,
    "backlog_visibility_score": 45,
    "margin_bridge_score": 25,
    "revision_score": 45,
    "relative_strength_score": 60,
    "customer_quality_score": 45,
    "policy_or_regulatory_score": 30,
    "valuation_repricing_score": 65,
    "execution_risk_score": 80,
    "legal_or_contract_risk_score": 20,
    "dilution_cb_risk_score": 35,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_before": 64,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 50,
    "backlog_visibility_score": 45,
    "margin_bridge_score": 15,
    "revision_score": 45,
    "relative_strength_score": 60,
    "customer_quality_score": 45,
    "policy_or_regulatory_score": 30,
    "valuation_repricing_score": 70,
    "execution_risk_score": 90,
    "legal_or_contract_risk_score": 20,
    "dilution_cb_risk_score": 35,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_after": 46,
  "stage_label_after": "Stage4B-watch",
  "component_delta_explanation": "C14 hard 4C requires order-cut/utilization/production-halt/ASP collapse. US localization/ESS/customer offset prevents blanket 4C, while growth-only stories are capped by high-MAE 4B guard."
}
```

## 12. Profile Simulation Summary
| profile_id | scope | hypothesis | false_positive_rate | missed_structural_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Global rules active; C14 still needs utilization/order-cut vs offset split. | 0.4 | 1 | 22.35 | -33.01 | 22.35 | -51.55 | mixed_residual_error |
| P0b_e2r_2_0_baseline_reference | rollback_reference | Baseline over-credits battery beta and misses hard 4C/liquidity risk. | 0.6 | 1 | 22.35 | -33.01 | 22.35 | -51.55 | poor |
| P1_L3_C14_sector_candidate | sector_specific | EV slowdown score requires utilization/order-cut/ASP collapse; named US-localization/ESS offset prevents automatic hard 4C. | 0.2 | 0 | 22.35 | -33.01 | 22.35 | -51.55 | better |
| P2_C14_canonical_candidate | canonical_archetype_specific | C14 hard 4C only when order cut/utilization loss/ASP collapse or production halt is observed; growth-only stories stay 4B-watch. | 0.1 | 0 | 22.35 | -33.01 | 22.35 | -51.55 | best_shadow_fit |
| P3_C14_counterexample_guard_profile | counterexample_guard | When MFE spikes early but MAE90<-30 follows, convert growth/offset cases to Stage2+4B-watch instead of Green. | 0.1 | 0 | 22.35 | -33.01 | 22.35 | -51.55 | best_for_drawdown_control |

## 13. 4B Local vs Full-Window Peak Proximity / 4C Protection Audit
| symbol | 4B evidence type | 4C verdict | peak_date | drawdown_after_peak_pct | interpretation |
| --- | --- | --- | --- | --- | --- |
| 093370 | margin_or_backlog_slowdown | hard_4c_success | 2023-04-18 | -38.39 | hard 4C protected capital |
| 278280 | margin_or_backlog_slowdown|contract_delay | hard_4c_success | 2023-08-30 | -54.33 | hard 4C protected capital |
| 348370 | positioning_overheat|valuation_blowoff | false_break | 2024-04-08 | -72.62 | early MFE does not justify Green; use 4B watch / false-hard-4C split |
| 121600 | positioning_overheat|price_only|valuation_blowoff | thesis_break_watch_only | 2024-03-19 | -60.88 | early MFE does not justify Green; use 4B watch / false-hard-4C split |
| 336370 | margin_or_backlog_slowdown|positioning_overheat | thesis_break_watch_only | 2024-07-01 | -67.66 | early MFE does not justify Green; use 4B watch / false-hard-4C split |

## 14. Sector / Canonical Rule Candidate

```yaml
rule_scope: canonical_archetype_specific
sector_specific_rule_candidate: L3_C14_EV_SLOWDOWN_UTILIZATION_ORDER_CUT_OFFSET_SPLIT
canonical_archetype_rule_candidate: C14_ORDER_CUT_UTILIZATION_HARD_4C_WITH_OFFSET_EXCEPTION
new_axis_proposed:
  - C14_HARD_4C_REQUIRES_ORDER_CUT_UTILIZATION_OR_PRODUCTION_HALT
  - C14_US_LOCALIZATION_ESS_OFFSET_FALSE_4C_BUFFER
  - C14_GROWTH_STORY_HIGH_MAE_4B_CAP
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
do_not_propose_global_delta: true
shadow_only: true
```

Mechanism: C14 should behave like a fire alarm with two sensors. Smoke alone is not enough. Hard 4C requires heat: observed customer order cut, utilization collapse, production halt, ASP collapse, or operating loss confirmation. If the company has named customer proximity, US localization, ESS/non-EV offset, or battery-chemistry mix resilience, the alarm should become Stage2+4B-watch rather than full hard 4C.

## 15. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C14_L96_093370_1","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_LIPF6_PRODUCTION_HALT_INVENTORY_PRICE_COLLAPSE","symbol":"093370","company":"후성","case_type":"hard_4c_protection_success","classification":"positive_protection","trigger_date":"2023-04-17","entry_date":"2023-04-17","evidence_url":"https://www.mk.co.kr/news/stock/10714626","calibration_usable":true}
{"row_type":"trigger","case_id":"C14_L96_093370_1","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_LIPF6_PRODUCTION_HALT_INVENTORY_PRICE_COLLAPSE","symbol":"093370","company":"후성","trigger_type":"Stage4C","trigger_date":"2023-04-17","entry_date":"2023-04-17","entry_price":14890.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2023.csv|atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv","profile_path":"atlas/symbol_profiles/093/093370.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.1,"MAE_30D_pct":-15.78,"MFE_90D_pct":4.1,"MAE_90D_pct":-26.12,"MFE_180D_pct":4.1,"MAE_180D_pct":-35.86,"peak_date":"2023-04-18","peak_price":15500.0,"trough_date":"2023-10-26","trough_price":9550.0,"drawdown_after_peak_pct":-38.39,"forward_window_trading_days":180,"window_end":"2024-01-10","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"current_profile_verdict":"current_profile_correct","four_b_evidence_type":"margin_or_backlog_slowdown","four_c_verdict":"hard_4c_success","evidence_summary":"LiPF6 생산 중단, 전방 고객 재고조정, 자체 재고 증가, 원가 부담, LiPF6 가격 하락이 동시에 확인된 hard thesis break.","evidence_url":"https://www.mk.co.kr/news/stock/10714626"}
{"row_type":"score_simulation","case_id":"C14_L96_093370_1","profile_id":"P2_C14_canonical_candidate","symbol":"093370","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":5,"customer_quality_score":10,"policy_or_regulatory_score":25,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15},"weighted_score_before":38,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":5,"customer_quality_score":10,"policy_or_regulatory_score":25,"valuation_repricing_score":20,"execution_risk_score":100,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15},"weighted_score_after":30,"stage_label_after":"Stage4C","component_delta_explanation":"C14-specific split: hard 4C requires observed order-cut/utilization/production-halt/ASP collapse; growth-only or localization-offset cases are capped at Stage2+4B-watch until margin/FCF bridge confirms."}
{"row_type":"case","case_id":"C14_L96_278280_2","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_LITHIUM_PRICE_DROP_PRODUCTION_DELAY_THESIS_BREAK","symbol":"278280","company":"천보","case_type":"hard_4c_protection_success","classification":"positive_protection","trigger_date":"2023-08-22","entry_date":"2023-08-23","evidence_url":"https://dealsite.co.kr/articles/108862/068020","calibration_usable":true}
{"row_type":"trigger","case_id":"C14_L96_278280_2","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_LITHIUM_PRICE_DROP_PRODUCTION_DELAY_THESIS_BREAK","symbol":"278280","company":"천보","trigger_type":"Stage4C","trigger_date":"2023-08-22","entry_date":"2023-08-23","entry_price":139800.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv|atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","profile_path":"atlas/symbol_profiles/278/278280.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.52,"MAE_30D_pct":-16.88,"MFE_90D_pct":11.52,"MAE_90D_pct":-31.19,"MFE_180D_pct":11.52,"MAE_180D_pct":-49.07,"peak_date":"2023-08-30","peak_price":155900.0,"trough_date":"2024-04-19","trough_price":71200.0,"drawdown_after_peak_pct":-54.33,"forward_window_trading_days":180,"window_end":"2024-05-21","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"current_profile_verdict":"current_profile_correct","four_b_evidence_type":"margin_or_backlog_slowdown|contract_delay","four_c_verdict":"hard_4c_success","evidence_summary":"리튬 가격 하락으로 판가가 떨어졌고, 전해질 생산 중단/출하 급감, 설비 완공 지연까지 겹친 customer-demand/ASP thesis break.","evidence_url":"https://dealsite.co.kr/articles/108862/068020"}
{"row_type":"score_simulation","case_id":"C14_L96_278280_2","profile_id":"P2_C14_canonical_candidate","symbol":"278280","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":10,"customer_quality_score":30,"policy_or_regulatory_score":15,"valuation_repricing_score":25,"execution_risk_score":85,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":40,"accounting_trust_risk_score":10},"weighted_score_before":42,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":10,"customer_quality_score":30,"policy_or_regulatory_score":15,"valuation_repricing_score":25,"execution_risk_score":95,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":40,"accounting_trust_risk_score":10},"weighted_score_after":34,"stage_label_after":"Stage4C","component_delta_explanation":"C14-specific split: hard 4C requires observed order-cut/utilization/production-halt/ASP collapse; growth-only or localization-offset cases are capped at Stage2+4B-watch until margin/FCF bridge confirms."}
{"row_type":"case","case_id":"C14_L96_348370_3","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_US_LOCALIZATION_OFFSET_FALSE_HARD_4C","symbol":"348370","company":"엔켐","case_type":"false_hard_4c_counterexample_with_4b_blowoff","classification":"counterexample","trigger_date":"2024-03-28","entry_date":"2024-03-28","evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1711582963859.pdf","calibration_usable":true}
{"row_type":"trigger","case_id":"C14_L96_348370_3","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_US_LOCALIZATION_OFFSET_FALSE_HARD_4C","symbol":"348370","company":"엔켐","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-28","entry_date":"2024-03-28","entry_price":236500.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv|atlas/ohlcv_tradable_by_symbol_year/348/348370/2025.csv","profile_path":"atlas/symbol_profiles/348/348370.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":66.81,"MAE_30D_pct":-5.07,"MFE_90D_pct":66.81,"MAE_90D_pct":-37.0,"MFE_180D_pct":66.81,"MAE_180D_pct":-54.33,"peak_date":"2024-04-08","peak_price":394500.0,"trough_date":"2024-11-15","trough_price":108000.0,"drawdown_after_peak_pct":-72.62,"forward_window_trading_days":180,"window_end":"2024-12-23","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"current_profile_verdict":"current_profile_missed_structural","four_b_evidence_type":"positioning_overheat|valuation_blowoff","four_c_verdict":"false_break","evidence_summary":"2023년 EV 둔화 영향은 맞지만 2024년 북미 현지화/캐파 증설/고객 공장 인근 공급망이 구조적 offset으로 작동한 false hard-4C 케이스.","evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1711582963859.pdf"}
{"row_type":"score_simulation","case_id":"C14_L96_348370_3","profile_id":"P2_C14_canonical_candidate","symbol":"348370","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":65,"margin_bridge_score":45,"revision_score":55,"relative_strength_score":85,"customer_quality_score":75,"policy_or_regulatory_score":70,"valuation_repricing_score":80,"execution_risk_score":50,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":25,"accounting_trust_risk_score":10},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":65,"margin_bridge_score":45,"revision_score":55,"relative_strength_score":85,"customer_quality_score":80,"policy_or_regulatory_score":75,"valuation_repricing_score":90,"execution_risk_score":50,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":25,"accounting_trust_risk_score":10},"weighted_score_after":63,"stage_label_after":"Stage2-Actionable+4B-watch","component_delta_explanation":"C14-specific split: hard 4C requires observed order-cut/utilization/production-halt/ASP collapse; growth-only or localization-offset cases are capped at Stage2+4B-watch until margin/FCF bridge confirms."}
{"row_type":"case","case_id":"C14_L96_121600_4","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_CNT_CAPA_GROWTH_STORY_WITH_EV_DEMAND_MAE","symbol":"121600","company":"나노신소재","case_type":"growth_story_high_mae_counterexample","classification":"counterexample","trigger_date":"2024-03-13","entry_date":"2024-03-13","evidence_url":"https://www.newspim.com/news/view/20240313000094","calibration_usable":true}
{"row_type":"trigger","case_id":"C14_L96_121600_4","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_CNT_CAPA_GROWTH_STORY_WITH_EV_DEMAND_MAE","symbol":"121600","company":"나노신소재","trigger_type":"Stage4B","trigger_date":"2024-03-13","entry_date":"2024-03-13","entry_price":139800.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv|atlas/ohlcv_tradable_by_symbol_year/121/121600/2025.csv","profile_path":"atlas/symbol_profiles/121/121600.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.44,"MAE_30D_pct":-20.6,"MFE_90D_pct":8.44,"MAE_90D_pct":-32.05,"MFE_180D_pct":8.44,"MAE_180D_pct":-57.58,"peak_date":"2024-03-19","peak_price":151600.0,"trough_date":"2024-11-15","trough_price":59300.0,"drawdown_after_peak_pct":-60.88,"forward_window_trading_days":180,"window_end":"2024-12-05","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"current_profile_verdict":"current_profile_false_positive","four_b_evidence_type":"positioning_overheat|price_only|valuation_blowoff","four_c_verdict":"thesis_break_watch_only","evidence_summary":"CNT 도전재 해외 양산과 사상최대 실적 기대는 있었지만, 실제 90/180D 경로는 EV/battery 소재 risk-off를 크게 맞은 Stage4B watch 케이스.","evidence_url":"https://www.newspim.com/news/view/20240313000094"}
{"row_type":"score_simulation","case_id":"C14_L96_121600_4","profile_id":"P2_C14_canonical_candidate","symbol":"121600","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":50,"margin_bridge_score":35,"revision_score":60,"relative_strength_score":45,"customer_quality_score":45,"policy_or_regulatory_score":25,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":45,"accounting_trust_risk_score":10},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":50,"margin_bridge_score":25,"revision_score":60,"relative_strength_score":45,"customer_quality_score":45,"policy_or_regulatory_score":25,"valuation_repricing_score":75,"execution_risk_score":70,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":45,"accounting_trust_risk_score":10},"weighted_score_after":48,"stage_label_after":"Stage4B-watch","component_delta_explanation":"C14-specific split: hard 4C requires observed order-cut/utilization/production-halt/ASP collapse; growth-only or localization-offset cases are capped at Stage2+4B-watch until margin/FCF bridge confirms."}
{"row_type":"case","case_id":"C14_L96_336370_5","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_COPPER_FOIL_REVENUE_GROWTH_WITH_FIXED_COST_LOSS_GUARD","symbol":"336370","company":"솔루스첨단소재","case_type":"loss_narrowing_revenue_growth_false_positive","classification":"counterexample","trigger_date":"2024-04-24","entry_date":"2024-04-24","evidence_url":"https://securities.miraeasset.com/bbs/download/2125875.pdf?attachmentId=2125875","calibration_usable":true}
{"row_type":"trigger","case_id":"C14_L96_336370_5","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_COPPER_FOIL_REVENUE_GROWTH_WITH_FIXED_COST_LOSS_GUARD","symbol":"336370","company":"솔루스첨단소재","trigger_type":"Stage4B","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":19440.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv|atlas/ohlcv_tradable_by_symbol_year/336/336370/2025.csv","profile_path":"atlas/symbol_profiles/336/336370.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.65,"MAE_30D_pct":-20.27,"MFE_90D_pct":20.88,"MAE_90D_pct":-38.68,"MFE_180D_pct":20.88,"MAE_180D_pct":-60.91,"peak_date":"2024-07-01","peak_price":23500.0,"trough_date":"2024-12-10","trough_price":7600.0,"drawdown_after_peak_pct":-67.66,"forward_window_trading_days":180,"window_end":"2025-01-20","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"current_profile_verdict":"current_profile_false_positive","four_b_evidence_type":"margin_or_backlog_slowdown|positioning_overheat","four_c_verdict":"thesis_break_watch_only","evidence_summary":"1Q24 매출 증가와 영업손실 축소 뉴스는 positive처럼 보였지만, 전지박 고정비/적자 부담이 남아 180D MAE가 크게 벌어진 4B guard 케이스.","evidence_url":"https://securities.miraeasset.com/bbs/download/2125875.pdf?attachmentId=2125875"}
{"row_type":"score_simulation","case_id":"C14_L96_336370_5","profile_id":"P2_C14_canonical_candidate","symbol":"336370","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":25,"revision_score":45,"relative_strength_score":60,"customer_quality_score":45,"policy_or_regulatory_score":30,"valuation_repricing_score":65,"execution_risk_score":80,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":35,"accounting_trust_risk_score":10},"weighted_score_before":64,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":15,"revision_score":45,"relative_strength_score":60,"customer_quality_score":45,"policy_or_regulatory_score":30,"valuation_repricing_score":70,"execution_risk_score":90,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":35,"accounting_trust_risk_score":10},"weighted_score_after":46,"stage_label_after":"Stage4B-watch","component_delta_explanation":"C14-specific split: hard 4C requires observed order-cut/utilization/production-halt/ASP collapse; growth-only or localization-offset cases are capped at Stage2+4B-watch until margin/FCF bridge confirms."}
{"row_type":"aggregate","selected_round":"R3","selected_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","eligible_trigger_count":5,"calibration_usable_case_count":5,"positive_case_count":2,"counterexample_count":3,"four_b_case_count":3,"four_c_case_count":2,"current_profile_error_count":3,"avg_MFE_90D_pct":22.35,"avg_MAE_90D_pct":-33.01,"avg_MFE_180D_pct":22.35,"avg_MAE_180D_pct":-51.55,"loop_contribution_label":"canonical_archetype_rule_candidate"}
{"row_type":"shadow_weight","rule_scope":"canonical_archetype_specific","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","rule_candidate_id":"C14_ORDER_CUT_UTILIZATION_HARD_4C_WITH_OFFSET_EXCEPTION","shadow_only":true,"do_not_apply_now":true,"proposed_axes":["C14_HARD_4C_REQUIRES_ORDER_CUT_UTILIZATION_OR_PRODUCTION_HALT","C14_US_LOCALIZATION_ESS_OFFSET_FALSE_4C_BUFFER","C14_GROWTH_STORY_HIGH_MAE_4B_CAP"],"existing_axis_strengthened":["hard_4c_thesis_break_routes_to_4c","full_4b_requires_non_price_evidence"],"existing_axis_weakened":[]}
{"row_type":"residual_contribution","selected_round":"R3","selected_loop":96,"contribution":"C14 now distinguishes true customer/ASP/production-break hard 4C from localization/ESS/customer-offset cases that should not be blanket-routed to 4C; growth-only CNT/copper-foil narratives are capped by high-MAE 4B watch."}
```

## 16. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation/coding agent. Do not treat this research MD as a production patch by itself. Ingest this file only through the existing v12 calibration batch flow. Validate every row_type=trigger for canonical price keys MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct. If rows pass, evaluate the shadow-only candidate rule C14_ORDER_CUT_UTILIZATION_HARD_4C_WITH_OFFSET_EXCEPTION. Compare against existing C14 rows and reject if the new rule is already represented or if URL/source quality fails. Do not change production scoring without aggregate validation across the full v12 corpus.
```

## 17. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 18. Residual Contribution Summary

```yaml
completed_round: R3
completed_loop: 96
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
new_independent_case_count: 5
reused_case_count: 0
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 3
current_profile_error_count: 3
diversity_score_summary: 5 new symbols / 5 fine trigger families / positive protection 2 + counterexample 3 + 4B 3 + 4C 2
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
next_recommended_archetypes: C02_POWER_GRID_DATACENTER_CAPEX | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
