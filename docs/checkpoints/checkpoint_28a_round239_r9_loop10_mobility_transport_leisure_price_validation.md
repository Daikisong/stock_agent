# Checkpoint 28A Round 239 R9 Loop 10 Mobility Transport Leisure Price Validation

## 목적

`docs/round/round_239.md`의 R9 Loop 10 내용을 case-library 가격경로 검증팩으로 반영했다.
이번 라운드는 모빌리티·운송·레저 안에서 미래모빌리티 capex, 자동차부품 recall, 철도 수출, LCC 장거리 노선/통합, 해운 사이클, 관광 reroute, 항공 safety hard 4C를 구분한다.

쉬운 예로, `유럽 노선 배정`은 Stage 2 관심 신호가 될 수 있지만 탑승률, yield, 항공기/승무원/유류비, 안전 운항, FCF가 확인되기 전에는 Stage 3-Green 근거가 아니다.

## 반영 파일

- `src/e2r/sector/round239_r9_loop10_mobility_transport_leisure_price_validation.py`
- `src/e2r/cli/build_round239_r9_loop10_report.py`
- `tests/test_round239_r9_loop10_mobility_transport_leisure_price_validation.py`
- `data/e2r_case_library/cases_r9_loop10_round239.jsonl`
- `data/sector_taxonomy/round239_r9_loop10_mobility_transport_leisure_price_validation_audit.json`
- `output/e2r_round239_r9_loop10_mobility_transport_leisure_price_validation/`

## 핵심 결과

- source_round: `docs/round/round_239.md`
- analyst_round_id: `round_167`
- large_sector: `MOBILITY_TRANSPORT_LEISURE`
- cases: 8
- success_candidate: 4
- cyclical_success: 1
- event_premium: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- 4C-watch cases: 2
- hard_4c_case_count: 1
- price_validation_completed: `partial_with_reported_price_anchors`
- full_ohlc_complete: false
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true

## 새 canonical archetype

- `FUTURE_MOBILITY_AI_ROBOTICS_CAPEX`
- `AUTO_PARTS_QUALITY_RECALL_4C`
- `RAIL_EXPORT_ORDER_TO_DELIVERY`
- `LCC_LONG_HAUL_ROUTE_ALLOCATION`
- `LCC_CONSOLIDATION_INTEGRATION`
- `SHIPPING_DRY_BULK_CYCLE`
- `TOURISM_REDIRECT_EVENT_PREMIUM`
- `AIRLINE_SAFETY_OPERATIONAL_TRUST_4C`

`PRICE_ONLY_RALLY`와 `EVENT_PREMIUM`은 기존 canonical owner로 연결했다.

## 케이스 해석

- 현대차/기아: Saemangeum 10조원, 2026~2030 국내 투자 125.2조원, Nvidia chip 50,000개, robotics 30,000대 계획은 Stage 2 + 4B-watch다. robot/software revenue, utilization, FCF, labor pass가 필요하다.
- 현대모비스: ICCU defect와 현대/기아 EV recall은 auto parts quality RedTeam 입력이다. EV 부품 노출만으로 Green을 만들 수 없다.
- 현대로템: Morocco 2.2조원 / $1.54B / 110대 rail order는 Stage 2다. 납품, 마진, working capital, 현금회수 확인 전 Green 보류.
- 티웨이항공: Paris/Rome/Barcelona/Frankfurt 노선과 A330-200 5대, pilot 100명 지원은 Stage 2다. load factor와 yield가 핵심이다.
- 진에어/에어부산/에어서울: 통합 58대 fleet와 8% capacity share는 Stage 2다. integration cost, route optimization, service/safety quality 확인 필요.
- 팬오션: 4,615원, 목표가 6,700원, 2024 OP 5,360억원 전망은 `cyclical_success`지만 `evidence_good_but_price_failed`로 기록했다. freight-rate floor와 contract coverage 없이는 구조적 Green이 아니다.
- 롯데관광개발/노랑풍선/신세계: 관광 reroute로 Lotte Tour 20%+, Yellow Balloon 24%, Shinsegae 6% 반응이 있었지만 spend, occupancy, casino drop, ADR, FCF 전에는 event premium이다.
- 제주항공: 2024-12-30 fatal crash, 179명 사망, 장중 -15.7%, 6,920원 anchor는 hard 4C reference case다. travel demand 논리가 있어도 safety trust break가 우선한다.

## Guardrail

- Capex, route allocation, fleet count, tourism reroute, freight cycle headline만으로 Green 금지.
- Unit economics, FCF after capex, utilization/load factor, route yield/contract margin, safety/quality trust가 확인돼야 Stage 3 검토 가능.
- Fatal safety accident, operational trust break, quality recall with earnings/reputation damage는 hard 4C 또는 4C-watch로 분리한다.
- 이 팩은 calibration/evaluation 전용이며 production scoring과 candidate generation에는 사용하지 않는다.

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round239_r9_loop10_mobility_transport_leisure_price_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round239_r9_loop10_report`
