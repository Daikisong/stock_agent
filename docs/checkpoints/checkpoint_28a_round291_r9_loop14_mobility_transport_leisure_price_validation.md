# Checkpoint 28A Round 291 R9 Loop 14 Mobility Transport Leisure Price Validation

## 반영 범위

- 입력 문서: `docs/round/round_291.md`
- analyst round id: `round_219`
- 대섹터: `MOBILITY_TRANSPORT_LEISURE`
- 생산 점수 변경: 없음
- candidate generation 입력 사용: 없음
- 적용 방식: `shadow_weight_only`

이번 라운드는 자동차 관세·하이브리드 mix, 중동 물류 차질, 항공 통합/노선 remedy, 항공 안전, 중국 관광, 컨테이너 운임 이벤트를 같은 대섹터 안에서 더 좁게 쪼갠 검증팩이다. 예를 들어 `중국 관광객 +48%`는 좋은 Stage 1/2 신호지만, 객단가·호텔 ADR/occupancy·카지노 drop·OPM으로 닫히기 전에는 Stage 3-Green 증거가 아니다.

## 추가된 Canonical Archetype

- `AUTO_TARIFF_HYBRID_MIX_STAGE2`
- `AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH`
- `AIRLINE_REMEDY_ROUTE_CARGO_STAGE2`
- `OVERSEAS_AUTO_IPO_FAILED_RERATING`
- `CONTAINER_SHIPPING_RATE_EVENT_PREMIUM`
- `USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE`

기존에 있던 `AIRLINE_CONSOLIDATION_STAGE2`, `AVIATION_SAFETY_HARD_4C`, `CHINA_TOURISM_LEISURE_EVENT_PREMIUM`도 Round 291 검증팩에서 함께 사용한다.

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| Hyundai Motor / Kia tariff and hybrid mix | success candidate + 4C-watch | 관세 25%에서 15% 인하는 Stage 2. Green은 관세 전가, 현지생산 hedge, 인센티브 통제, hybrid/high-margin mix가 OP/FCF로 닫혀야 가능 |
| Hyundai Motor / Hyundai Glovis Middle East logistics | 4C-watch | 중동 항로 차질은 고마진 수출과 납기, 물류비를 훼손할 수 있는 자동차/물류 hard gate |
| Korean Air / Asiana integration | success candidate | 합병 완료와 매출/OP 증가는 Stage 2. Green은 yield, load factor, integration cost, LCC consolidation 확인 필요 |
| T'way / Air Incheon remedy | success candidate + execution watch | 노선권과 화물 자산은 Stage 2. aircraft utilization, cargo customer retention, maintenance reliability 필요 |
| Jeju Air safety event | hard 4C | 사망 사고와 안전 점검은 여행 수요나 밸류 회복 논리보다 우선하는 thesis break |
| Hyundai Motor India IPO | failed rerating | 대형 IPO와 인도 성장 내러티브가 약한 debut, 첫 실적, 내수/수출 감소로 검증 실패 |
| China tourism leisure basket | event premium + 4B-watch | visa-free와 관광객 수는 이벤트. spend-per-head와 margin conversion 전에는 Green 아님 |
| HMM / Red Sea freight cycle | event premium + 4B-watch | spot 운임 spike는 Stage 2. contract-rate mix와 route security, cash yield durability 필요 |
| Korea used-car export logistics | 4C reference | 수출 수요가 있어도 목적지 항로와 보관 흐름이 막히면 구조적 visibility가 깨짐 |

## Green Gate 보정 방향

올릴 축:

- tariff pass-through
- hybrid/high-margin mix margin
- local production hedge
- route security continuity
- logistics cost control
- load factor and route yield
- aviation safety trust
- integration synergy execution
- tourist spend-per-head
- freight-rate durability

내릴 축:

- tariff relief headline only
- visitor count only
- merger completion only
- route rights without load factor
- cargo asset purchase without customer retention
- freight spot rate only
- overseas IPO size only
- EV/hybrid mix without margin
- unresolved safety risk

## 4B / 4C 해석

- `4B-watch`: 관세 relief, 관광정책, 항공 합병, 노선권, freight spot rate처럼 가격이 증거보다 먼저 갈 수 있는 상태.
- `hard 4C`: Jeju Air처럼 항공 안전 신뢰가 깨진 상태. 이 경우 여행 수요 회복이나 저평가 논리보다 안전/규제/소비자 신뢰가 우선한다.

## 생성 산출물

- `data/e2r_case_library/cases_r9_loop14_round291.jsonl`
- `data/sector_taxonomy/round291_r9_loop14_mobility_transport_leisure_price_validation_audit.json`
- `output/e2r_round291_r9_loop14_mobility_transport_leisure_price_validation/round291_r9_loop14_price_validation_summary.md`
- `output/e2r_round291_r9_loop14_mobility_transport_leisure_price_validation/round291_r9_loop14_case_matrix.csv`
- `output/e2r_round291_r9_loop14_mobility_transport_leisure_price_validation/round291_r9_loop14_shadow_weights.csv`
- `output/e2r_round291_r9_loop14_mobility_transport_leisure_price_validation/round291_r9_loop14_green_gate_review.md`
- `output/e2r_round291_r9_loop14_mobility_transport_leisure_price_validation/round291_r9_loop14_stage4b_4c_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests/test_round291_r9_loop14_mobility_transport_leisure_price_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round291_r9_loop14_report
```

결과:

- round_291 단위 테스트 통과
- case library 레코드 validation 통과
- 리포트 생성 완료
- production scoring 변경 없음

## 다음 라운드에 남긴 기준

이 라운드의 핵심은 “이동 수요가 있다”가 아니라 “그 수요가 비용, 안전, 항로, yield, margin을 지나 OP/FCF로 닫히는가”다. 예를 들어 항공 합병은 규모의 경제처럼 보일 수 있지만, 실제로는 load factor와 yield가 개선되고 통합비용이 통제되어야 Stage 3 후보가 된다.
