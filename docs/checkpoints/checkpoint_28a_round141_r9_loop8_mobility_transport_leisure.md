# Checkpoint 28A Round 141 R9 Loop 8 Mobility / Transport / Leisure

## 목적

`docs/round/round_141.md`의 R9 Loop 8 내용을 별도 calibration pack으로 반영했다.

R9는 완성차, 하이브리드 부품, 로보택시, 자율트럭, 항공, 관광·카지노·면세, 해운, 렌터카·중고차, eVTOL, 위성 connectivity를 다룬다. 이번 라운드의 핵심은 “이동 수요 회복”이나 “기술 출시”가 아니라 OPM, FCF, 반복계약, backlog, fleet utilization, cost per mile, safety record, certification, 실제 가격경로를 확인하는 것이다.

쉬운 예시는 다음과 같다.

- `하이브리드 수요 증가`는 Stage 1 신호다. 현대차처럼 OPM 목표, FCF, 자사주·배당 실행이 붙어야 Stage 2→3 후보가 된다.
- `로보택시 도시 출시`는 Stage 1~2 신호다. 대기시간, misrouting, completion rate, cost per mile, safety record가 없으면 Stage 3가 아니다.
- `자율트럭 paid freight`는 강한 Stage 2 근거다. 그래도 fleet utilization, 보험비, remote support cost, 반복 고객이 없으면 Green 근거가 아니다.
- `Part 135`는 eVTOL 운항자격 이정표일 수 있지만, 기체 Type Certification이나 상업 매출 증거는 아니다.
- `무비자 관광정책`은 이벤트 프리미엄이다. 관광객 spend, casino drop, duty-free ASP, RevPAR, OPM이 확인되기 전에는 구조적 Green 근거가 아니다.

## 반영 파일

- `src/e2r/sector/round141_r9_loop8_mobility_transport_leisure.py`
- `src/e2r/cli/build_round141_r9_loop8_report.py`
- `tests/test_round141_r9_loop8_mobility_transport_leisure.py`
- `data/e2r_case_library/cases_r9_loop8_round141.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round141_r9_loop8_v8.csv`
- `output/e2r_round141_r9_loop8_mobility_transport_leisure/`

## v8 기본 점수축

| component | weight | 해석 |
| --- | ---: | --- |
| eps_fcf_opm_conversion | 22 | 이동·운송·레저 수요가 OPM, FCF, 반복 현금흐름으로 전환되는지 확인 |
| contract_backlog_operating_visibility | 20 | 판매목표, 항공사 계약, gross backlog, paid freight, service area가 매출로 전환되는지 확인 |
| unit_fleet_economics | 18 | utilization, cost per mile, repair cost, residual value, insurance, remote support cost 확인 |
| recurrence_demand_duration | 12 | hybrid mix, recurring connectivity, passenger/cargo mix, tourism spend가 반복되는지 확인 |
| safety_regulatory_certification_disclosure | 12 | safety record, NHTSA, Type Certification, disclosure confidence를 hard gate로 확인 |
| market_mispricing_rerating_gap | 8 | 시장이 여전히 old auto/airline/shipping/space frame으로 보고 있는지 확인 |
| valuation_room_4b_margin | 8 | 가격이 unit economics보다 먼저 간 4B-watch 구간을 분리 |

## 케이스 방향

- Stage 2→3 후보: `Hyundai hybrid value-up`, `Toyota hybrid component bottleneck`, `SES airline connectivity`, `Aurora/Bot Auto paid driverless freight`, `Korean Air integration scale`
- Event/Watch: `China group visa-free tourism`, `Archer Part 135`
- 4C / RedTeam: `Hyundai tariff OPM cut`, `Tesla robotaxi wait/misrouting`, `Waymo flooded-road recall`, `shipping rate collapse`, `Hertz EV rental write-down`, `Michelin demand guidance cut`, `Joby discounted offering`, `Lilium cash crunch`

## Guardrail

- production scoring은 변경하지 않았다.
- case record는 candidate-generation input이 아니다.
- 하이브리드, 관광 재개, 로보택시, 자율트럭, 운임 상승, eVTOL, 위성통신이라는 이름만으로 Green을 만들지 않는다.
- Stage 3는 OPM/FCF, 반복계약, backlog 매출 전환, fleet utilization, cost per mile, repair/residual value, safety record, Type Certification, 실제 가격경로 동행을 요구한다.
- tariff margin cut, robotaxi operational failure, AV recall/probe, shipping rate collapse, EV rental repair/depreciation, eVTOL cash burn, Part 135 오분류는 RedTeam overlay로 유지한다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round141_r9_loop8_mobility_transport_leisure.py -v
PYTHONPATH=src python -m e2r.cli.build_round141_r9_loop8_report
```

결과:

- Round 141 전용 테스트 12개 통과
- v8 score profile 생성
- case JSONL 생성
- summary, case matrix, stage date plan, base score axes, guardrail, risk overlay, price validation 리포트 생성
