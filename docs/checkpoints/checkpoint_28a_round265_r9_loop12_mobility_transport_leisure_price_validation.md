# Checkpoint 28A Round 265 R9 Loop 12 Mobility/Transport/Leisure Price Validation

## 목적

`docs/round/round_265.md`의 R9 Loop 12 내용을 케이스 라이브러리와 가격 검증 보고서로 구조화했다.

이번 라운드는 **캘리브레이션 전용**이다. 생산 점수, StageClassifier 임계값, 후보 생성 로직은 바꾸지 않았다.

쉬운 예시:

- T'way의 유럽 노선권은 `Stage 2` 후보 증거가 될 수 있다.
- 하지만 노선권만으로는 `Stage 3-Green`이 아니다.
- 실제 `route_yield`, `load_factor`, `fuel/lease cost`, `FCF`가 확인돼야 한다.

## 반영 범위

- 원본 라운드: `docs/round/round_265.md`
- 분석 라운드 ID: `round_193`
- 대섹터: `MOBILITY_TRANSPORT_LEISURE`
- 가격 검증 상태: `partial_with_reported_price_anchors`
- 전체 조정 OHLC 완성 여부: `false`
- 생산 scoring 변경: `false`
- shadow weight만 기록: `true`

## 추가한 canonical archetype

이번 라운드에서 다음 archetype을 canonical enum과 정의에 추가했다.

- `AVIATION_SAFETY_HARD_4C`
- `LCC_ROUTE_REMEDY_LONG_HAUL_OPTION`
- `AUTO_COMPONENT_HYBRID_EREV_ASP`
- `AUTO_PARTS_PORTFOLIO_RESTRUCTURING`
- `SHIPPING_GEOPOLITICAL_SECURITY_4C`
- `SHIPPING_FREIGHT_NORMALIZATION_4C`
- `TRAVEL_CASINO_DEMAND_CONVERSION`

기존 `TOURISM_REDIRECT_EVENT_PREMIUM`과 함께 총 8개 target archetype을 라운드 산출물에 매핑했다.

## 케이스 요약

| case | 분류 | 핵심 판단 |
|---|---|---|
| Jeju Air | hard 4C | fatal aviation accident는 안전 신뢰 훼손이므로 load factor보다 먼저 4C gate로 본다. |
| Air Busan | 4C-watch | 사망 사고는 아니지만 항공기 화재는 safety trust gate를 올린다. |
| T'way Air | success candidate | EU route remedy는 Stage 2 증거지만 route yield/load factor가 필요하다. |
| HL Mando | success candidate | hybrid/EREV ASP uplift는 Stage 2 증거지만 margin/FCF 확인 전 Green 금지다. |
| Hyundai Mobis | success candidate | lighting divestiture는 거래가치와 proceeds use 확인 전 Stage 2다. |
| HMM Namu | 4C-watch | 선박 공격은 운임 호재가 아니라 보안/보험/지연 비용 gate다. |
| HMM/Pan Ocean freight cycle | cyclical success + 4C-watch | 운임 급등은 cyclical이며 freight normalization이 4C risk다. |
| Lotte Tour/Yellow Balloon/Shinsegae | event premium | 관광 리다이렉트는 spend conversion 확인 전 event premium이다. |

## 산출물

- `data/e2r_case_library/cases_r9_loop12_round265.jsonl`
- `data/sector_taxonomy/round265_r9_loop12_mobility_transport_leisure_price_validation_audit.json`
- `output/e2r_round265_r9_loop12_mobility_transport_leisure_price_validation/round265_r9_loop12_price_validation_summary.md`
- `output/e2r_round265_r9_loop12_mobility_transport_leisure_price_validation/round265_r9_loop12_case_matrix.csv`
- `output/e2r_round265_r9_loop12_mobility_transport_leisure_price_validation/round265_r9_loop12_shadow_weights.csv`
- `output/e2r_round265_r9_loop12_mobility_transport_leisure_price_validation/round265_r9_loop12_green_gate_review.md`
- `output/e2r_round265_r9_loop12_mobility_transport_leisure_price_validation/round265_r9_loop12_stage4b_4c_review.md`

## 핵심 가드레일

- 라운드 케이스는 candidate-generation input이 아니다.
- shadow weight는 production scoring에 적용하지 않는다.
- 노선권, 관광객 headline, 운임 spike, divestiture headline, component ASP만으로 Green을 만들지 않는다.
- 항공 안전 사고, 선박 공격, 운임 정상화, 관광 spend 실패는 Red Team/4C gate로 유지한다.
- 가격 앵커가 없는 경우 OHLC, MFE, MAE를 만들지 않는다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round265_r9_loop12_mobility_transport_leisure_price_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round265_r9_loop12_report
```

결과:

- 라운드 265 전용 테스트 통과
- 케이스 8개 JSONL 생성
- 감사 JSON 생성
- 가격 검증/Green gate/4B-4C 보고서 생성

## 다음 작업

다음 라운드에서는 이 케이스들을 생산 점수에 바로 넣지 말고, 같은 대섹터의 추가 성공/반례를 더 모아야 한다. 예를 들어 항공은 `route economics`와 `safety trust`, 해운은 `freight floor`와 `security cost`, 관광은 `visitor count`가 아니라 `hotel occupancy/casino drop/ADR/package margin`까지 확인해야 한다.
