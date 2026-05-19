# Round 216 R12 Loop 8 Agri Life Service Misc Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_216.md
- large_sector: EDUCATION_LIFE_AGRI_MISC
- cases: 8
- success_candidate: 3
- event_premium: 3
- overheat: 1
- watch: 1
- price_moved_without_evidence: 2
- Stage 3 dated cases: 0
- 4B-watch cases: 8
- r12_default_stage3_bias: conservative_except_recurring_service
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage2 | stage3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r12_loop8_coway_recurring_rental_service_candidate | 코웨이 | success_candidate |  |  |  |  | unknown | R12에서 가장 구조적인 후보지만 Green은 렌탈 계정, churn, ARPU, OPM, FCF 확인 뒤에만 가능하다. |
| r12_loop8_daedong_tym_agri_machinery_export_watch | 대동 / TYM | success_candidate |  |  |  |  | unknown | 농기계는 export theme보다 dealer sell-through, inventory, financing, OPM, FCF를 우선한다. |
| r12_loop8_megastudy_medical_quota_policy_event | 메가스터디교육 | event_premium | 2025-03-07 |  |  |  | unknown | 교육정책은 routing이고 실제 수강생, repeat course, ARPU, OPM 전에는 Stage 3가 아니다. |
| r12_loop8_edtech_phone_ban_policy_watch | 교육·에듀테크 basket | 4b_watch |  |  |  |  | unknown | 같은 정책도 오프라인 학원에는 우호적, 에듀테크에는 악재일 수 있어 회사별 매출경로 전 Green 금지다. |
| r12_loop8_poultry_brazil_bird_flu_import_ban_event | Poultry basket | event_premium |  |  | 2025-05-19 | 2025-06-23 | price_moved_without_evidence | 축산 질병 이벤트는 Stage 1이며 판매량, 가격전가, feed cost, OPM 확인 전 Stage 3 금지다. |
| r12_loop8_kyochon_chicken_celebrity_food_event | Kyochon F&B / chicken-event basket | overheat |  |  | 2025-10-31 |  | price_moved_without_evidence | 유명인/바이럴 외식 이벤트는 매출 evidence가 아니라 price_moved_without_evidence다. |
| r12_loop8_smart_farm_unit_economics_watch | 스마트팜 basket | event_premium |  |  |  |  | unknown | 스마트팜은 정책/논문보다 상업 설치, 유지보수 계약, unit economics, FCF 확인이 먼저다. |
| r12_loop8_ktng_regulated_consumer_cashflow_watch | KT&G | success_candidate |  |  |  |  | unknown | 규제소비재 cashflow 후보지만 최신 배당·소각·HNB 성장·volume decline·규제 리스크 확인 전 Stage 3 보류다. |

## Interpretation
- R12 Green is possible mainly for recurring rental/service or regulated cashflow cases after unit economics and FCF are visible.
- Coway and KT&G stay success candidates, not Green, until fresh account, churn, ARPU, shareholder return, regulation, and price-path evidence are checked.
- Medical-quota policy, phone-ban policy, bird flu, smart-farm papers, and celebrity food events are routing or event premium evidence.
- Kyochon/chicken-event basket is the clean example: +20~30% without store traffic or margin evidence is 4B/event premium, not E2R.
