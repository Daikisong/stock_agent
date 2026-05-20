# Checkpoint 28A Round 278 R9 Loop 13 Mobility Transport Leisure Price Validation

## 목적

`docs/round/round_278.md`의 모빌리티·운송·레저 케이스를 calibration-only 자료로 구조화했다.

이번 라운드의 핵심은 `판매량`, `IPO valuation`, `관광객 headline`, `운임 spike`, `항공기 주문`, `자산매각 탐색`만으로 Stage 3-Green을 만들지 않는 것이다. 예를 들어 Kia는 미국 판매가 늘었지만 관세 비용으로 OP가 감소했으므로, 판매량보다 관세 이후 OP margin이 먼저다.

## 반영 내용

- canonical archetype 7개 추가
- 기존 `AVIATION_SAFETY_HARD_4C`를 Round 278 타깃으로 재사용
- Round 278 전용 케이스 팩 추가
- JSONL case library 생성
- audit JSON 생성
- shadow weight, deep sub-archetype, green gate, 4B/4C review 출력
- production scoring, 후보 생성, StageClassifier threshold는 변경하지 않음

## 추가 archetype

- `HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2`
- `AUTO_TARIFF_MARGIN_4C_WATCH`
- `INDIA_AUTO_IPO_CAPITAL_RECYCLING`
- `AIRLINE_CONSOLIDATION_STAGE2`
- `AUTO_PARTS_PORTFOLIO_RECYCLING`
- `RED_SEA_FREIGHT_CYCLE_4B_4C`
- `CHINA_TOURISM_LEISURE_EVENT_PREMIUM`

## 케이스 요약

- 케이스 수: 8
- Stage 3 dated case: 0
- success_candidate: 4
- failed_rerating: 1
- cyclical_success: 1
- event_premium: 1
- hard 4C direct case: 1

## 핵심 가드레일

- unit sales without margin Green 금지
- IPO valuation without parent ROI Green 금지
- tourist-flow headline only Green 금지
- freight-rate spike only Green 금지
- fleet order without ROI Green 금지
- exploratory asset sale only Green 금지
- unhedged tariff exposure는 4C-watch
- fatal safety event는 hard 4C

## 생성 파일

- `src/e2r/sector/round278_r9_loop13_mobility_transport_leisure_price_validation.py`
- `src/e2r/cli/build_round278_r9_loop13_report.py`
- `tests/test_round278_r9_loop13_mobility_transport_leisure_price_validation.py`
- `data/e2r_case_library/cases_r9_loop13_round278.jsonl`
- `data/sector_taxonomy/round278_r9_loop13_mobility_transport_leisure_price_validation_audit.json`
- `output/e2r_round278_r9_loop13_mobility_transport_leisure_price_validation/`

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round278_r9_loop13_mobility_transport_leisure_price_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/archetypes.py src/e2r/sector/round278_r9_loop13_mobility_transport_leisure_price_validation.py src/e2r/cli/build_round278_r9_loop13_report.py tests/test_round278_r9_loop13_mobility_transport_leisure_price_validation.py
PYTHONPATH=src python -m e2r.cli.build_round278_r9_loop13_report
PYTHONPATH=src python -m unittest discover -s tests -v
```

라운드 전용 테스트 6개와 전체 테스트 3202개가 통과했다.

## 해석

이번 패치는 점수를 바꾸는 작업이 아니라 모빌리티·운송·레저 archetype의 실패 패턴을 더 정확히 기록하는 작업이다. `Hyundai Motor`는 하이브리드/주주환원 Stage 2 후보지만 관세 이후 마진과 FCF가 필요하다. `Kia`는 판매량보다 마진이 중요하다는 반례다. `Jeju Air`는 항공 안전 신뢰가 무너지면 hard 4C가 된다는 기준점이다. `HMM/Pan Ocean`과 관광 basket은 운임·정책 이벤트가 가격을 움직일 수 있지만, 구조적 Green은 durability와 booking/margin 증거가 필요하다.
