# Round 257 R1 Loop 12 Industrial Orders / Infrastructure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_257.md
- round_id: round_185
- large_sector: INDUSTRIAL_ORDERS_INFRA
- cases: 8
- success_candidate: 5
- event_premium: 1
- failed_rerating: 1
- 4B-watch case_type: 1
- hard_4c_case_count: 0
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- price_data_unavailable: 2
- false_positive_score: 1
- target_archetype_count: 8
- deep_sub_archetype_count: 8
- shadow_weight_row_count: 8
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r1_loop12_hanwha_aerospace_romania_k9_dilution_watch | Hanwha Aerospace | success_candidate | 2024-07-10 |  | 2024-07-10 |  | success_candidate_with_4B_dilution_watch | 방산 수주잔고는 강하지만 대형 증자와 현금회수 리스크가 있어 Green 전 4B-watch를 병행한다. |
| r1_loop12_lig_nex1_iraq_cheongung_missile_defense | LIG Nex1 | success_candidate | 2024-09-20 |  | 2026-01-01 |  | success_candidate_geopolitical_4B_watch | Iraq/Saudi 수주와 전투검증 서사는 강하지만 지정학 rally가 실적보다 앞서면 4B-watch다. |
| r1_loop12_hyundai_rotem_k2_poland_delivery_to_revenue | Hyundai Rotem | success_candidate | 2024-04-09 |  |  |  | success_candidate | 납품→매출 증거가 있어 품질 높은 Stage 2지만 현지생산 마진·현금회수 전 Green은 보류다. |
| r1_loop12_ls_electric_us_datacenter_transformer | LS Electric | success_candidate | 2025-11-01 |  |  |  | success_candidate_insufficient_price_data | 미국 데이터센터 변압기 bottleneck은 강한 Stage 2지만 납품·마진·원가 전가·현금회수 확인이 필요하다. |
| r1_loop12_hyosung_hico_us_grid_equipment_localization | Hyosung Heavy / Hyosung HICO | success_candidate | 2025-12-01 |  |  |  | success_candidate_capex_watch | 미국 현지화 CAPA는 Stage 2다. firm order·가동률·마진·FCF가 없으면 Green이 아니다. |
| r1_loop12_samsung_ea_fadhili_epc_stage2 | Samsung E&A | event_premium | 2024-04-03 |  | 2024-04-03 |  | event_premium_success_candidate | EPC mega-order와 +8.5% rally는 Stage 2/4B-watch다. 공정률·마진·현금회수 전 Green은 금지다. |
| r1_loop12_hyundai_steel_us_policy_capex_false_positive | Hyundai Steel | failed_rerating | 2025-03-25 |  |  | 2025-04-22 | false_positive_score_prevention | 정책 CAPEX와 관세 hedge 서사만으로는 Green이 아니다. 자금조달·고객수요·마진·FCF가 빠져 실패 반례다. |
| r1_loop12_hanwha_aerospace_capital_raise_dilution_4b | Hanwha Aerospace | 4b_watch | 2025-03-21 |  | 2025-03-27 |  | 4B_watch | 방산 리레이팅 후 대형 증자는 4B/dilution watch다. ROI와 FCF per share가 확인되기 전 긍정 증거로 쓰면 안 된다. |

## Interpretation
- R1 Stage 3 is not an order headline. It needs delivery, revenue, margin, cash collection, and repeat order evidence.
- Hanwha Aerospace, LIG Nex1, and Hyundai Rotem are strong Stage 2 examples, but delivery/margin/cash gates remain.
- LS Electric and Hyosung HICO are grid bottleneck Stage 2 cases with insufficient full OHLC in this pass.
- Samsung E&A is EPC Stage 2 plus 4B-watch before progress revenue, margin, and working capital proof.
- Hyundai Steel is the policy-CAPEX false-positive example: funding and FCF uncertainty blocked rerating.
- No hard 4C is forced in this round; 4C-watch remains separate from hard 4C.
