# Checkpoint 28A Round 252: R9 Loop 11 Mobility/Transport/Leisure Price Validation

## 목적

`docs/round/round_252.md`의 R9 Loop 11 내용을 calibration/evaluation 자료로 구조화했다.
이번 패치는 production scoring을 바꾸지 않는다.

쉬운 예시:

- 현대차 주주환원 발표는 강한 Stage 2다. 하지만 관세 반영 후 마진과 FCF가 확인되기 전에는 Stage 3-Green이 아니다.
- 금호타이어 공장 화재는 수요가 좋아도 생산능력이 직접 멈췄으므로 hard 4C다.

## 반영 파일

- `src/e2r/sector/round252_r9_loop11_mobility_transport_leisure_price_validation.py`
- `src/e2r/cli/build_round252_r9_loop11_report.py`
- `tests/test_round252_r9_loop11_mobility_transport_leisure_price_validation.py`
- `data/e2r_case_library/cases_r9_loop11_round252.jsonl`
- `data/sector_taxonomy/round252_r9_loop11_mobility_transport_leisure_price_validation_audit.json`
- `output/e2r_round252_r9_loop11_mobility_transport_leisure_price_validation/`

## 추가/확정한 canonical archetype

- `AUTO_HYBRID_SHAREHOLDER_RETURN`
- `AUTO_TARIFF_MARGIN_SHOCK`
- `AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION`
- `AIRLINE_CONSOLIDATION_INTEGRATION`
- `AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C`
- `AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C`
- `TOURISM_REDIRECT_POLICY_EVENT`
- `CYCLICAL_SUCCESS`

## 케이스 요약

| case | 판단 |
|---|---|
| Hyundai Motor hybrid/shareholder return | Stage 2. hybrid mix, tariff-adjusted margin, FCF 확인 전 Green 금지 |
| Hyundai/Kia U.S. tariff shock | 4C-watch. 관세 비용이 영업이익과 주가에 직접 반영 |
| Hyundai/Glovis Middle East logistics disruption | 4C-watch. 수출 route, delivery, logistics cost 훼손 |
| Korean Air/Asiana consolidation | Stage 2. yield, load factor, cost synergy, debt, safety/service quality 확인 필요 |
| Kumho Tire factory fire | direct-listed hard 4C. 생산중단과 매출 목표 리스크 |
| Daejeon auto-parts supplier fire | sector hard 4C. Hyundai/Kia supplier network safety gate |
| Pan Ocean shipping freight cycle | cyclical_success. rate floor, contract coverage, FCF 전 Green 금지 |
| Lotte Tour / Yellow Balloon tourism redirect | event_premium. spend, occupancy, casino drop/hold, OPM 전 Green 금지 |

## R9 Green gate 원칙

R9에서 Stage 3-Green은 “수요가 좋아진다”가 아니라 “비용과 운영 리스크까지 통과한다”다.

필수 확인 축:

- unit economics
- tariff-adjusted margin
- FCF after capex
- route yield / load factor / fleet utilization
- logistics cost와 delivery delay 통제
- supply-chain continuity
- safety / quality / operational trust
- 관광주는 arrivals보다 spend, occupancy, casino drop, OPM
- evidence 이후 price path 정렬

## 4B/4C 원칙

- 4B-watch: 전략발표, 항공통합, 관광정책, freight-rate spike가 실적보다 먼저 가격에 반영된 경우.
- hard 4C: 관세 비용으로 OP가 훼손되거나, 공장 화재/생산중단/사망사고/공급망 차질이 발생한 경우.

예시:

- `Hyundai shareholder return`: 좋은 Stage 2지만 관세 반영 후 마진과 FCF 확인 전 Green이 아니다.
- `Kumho Tire fire`: 생산능력 20% 가까운 공장 중단이므로 수요논리를 바로 막는 hard 4C다.

## 산출물

CLI:

```bash
PYTHONPATH=src python -m e2r.cli.build_round252_r9_loop11_report
```

생성 파일:

- `round252_r9_loop11_price_validation_summary.md`
- `round252_r9_loop11_case_matrix.csv`
- `round252_r9_loop11_target_aliases.csv`
- `round252_r9_loop11_deep_sub_archetypes.csv`
- `round252_r9_loop11_score_adjustments.csv`
- `round252_r9_loop11_shadow_weights.csv`
- `round252_r9_loop11_price_validation_fields.csv`
- `round252_r9_loop11_green_gate_review.md`
- `round252_r9_loop11_price_validation_plan.md`
- `round252_r9_loop11_stage4b_4c_review.md`
- `round252_r9_loop11_deep_sub_archetypes.md`

## 유지한 제약

- production scoring 변경 없음
- candidate generation input 아님
- shadow weight only
- full adjusted OHLC 미완성 상태를 명시
- Stage 3-Green threshold 완화 없음
- buy/sell 문구 없음
- API key 출력 없음

## 다음 작업

다음 라운드에서는 full OHLC, tariff-adjusted OPM, FCF after capex, route yield, load factor, tourist spend, casino drop, factory restart 여부를 채워야 한다.
현재 round_252는 R9의 “수요보다 비용·물류·안전이 먼저 깨질 수 있다”는 guardrail을 정리한 검증팩이다.
