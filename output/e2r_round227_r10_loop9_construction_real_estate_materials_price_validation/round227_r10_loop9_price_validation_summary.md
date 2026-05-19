# Round 227 R10 Loop 9 Construction Real Estate Materials Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_227.md
- large_sector: CONSTRUCTION_REAL_ESTATE_MATERIALS
- cases: 8
- success_candidate: 3
- event_premium: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 4
- hard_4c_case_count: 3
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage2 | stage3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r10_loop9_samsung_ea_gs_fadhili_epc | 삼성E&A / GS건설 | success_candidate | 2024-04-03 |  | 2024-04-03 |  | aligned | 대형 Fadhili EPC는 Stage 2 후보지만, 마진·공정률·현금회수·working capital 확인 전 Stage 3-Green은 금지한다. |
| r10_loop9_hyundai_ec_jafurah_gas_infra | 현대건설 | success_candidate | 2024-06-30 |  |  |  | unknown | 사우디 가스 인프라 수주는 Stage 2 후보지만 회사별 주가 앵커와 마진·현금회수가 아직 없다. |
| r10_loop9_taeyoung_pf_credit_hard_4c | 태영건설 / 건설 PF stress | 4c_thesis_break |  |  |  | 2023-12-01 | false_positive_score | PF 채무재조정과 연체율 급등은 hard 4C다. 정책지원은 Green 증거가 아니라 RedTeam relief다. |
| r10_loop9_seoul_housing_supply_policy_watch | 서울 주택공급 / 재건축 정책 basket | event_premium | 2025-09-07 |  |  |  | price_moved_without_evidence | 주택공급·재건축 정책은 관심 이벤트지만, 분양률·원가율·PF 안정·FCF 전에는 Green이 아니다. |
| r10_loop9_hyundai_engineering_bridge_collapse_watch | 현대엔지니어링 / 천안 교량 붕괴 | 4c_thesis_break |  |  |  | 2025-02-25 | false_positive_score | 직접 상장사는 아니지만 건설 안전 신뢰 4C 게이트를 검증하는 사례다. |
| r10_loop9_posco_ec_dl_construction_safety_regulation | POSCO E&C / DL Construction 안전 규제 | 4c_thesis_break |  |  |  | 2025-09-15 | false_positive_score | 반복 사망사고·현장중단·벌금·면허 리스크는 R10에서 Green을 막는 operational trust 4C다. |
| r10_loop9_ai_data_center_real_asset_event | SK/AWS·OpenAI·Samsung C&T 데이터센터 | success_candidate | 2025-10-01 |  | 2025-06-20 |  | price_moved_without_evidence | 데이터센터 real asset은 구조 후보지만 tenant, NOI/AFFO, 전력·물·인허가, capex per share 전에는 Stage 3가 아니다. |
| r10_loop9_hyundai_steel_rebar_construction_demand_watch | 현대제철 / 철근·건자재 수요 proxy | 4c_thesis_break |  |  |  | 2024-06-21 | false_positive_score | 철근·건자재 수요 약화는 건설 cycle 4C-watch다. 수요·spread·margin 안정 전 Green은 막는다. |

## Interpretation
- Samsung E&A/GS E&C and Hyundai E&C are Stage 2 EPC/gas-infra watch cases, not Stage 3-Green.
- Taeyoung/PF stress is a hard 4C reference point.
- Housing supply policy and AI data-center headlines are event premium until company-level cash flow appears.
- Construction safety events and building-material demand weakness block unsafe Green.
