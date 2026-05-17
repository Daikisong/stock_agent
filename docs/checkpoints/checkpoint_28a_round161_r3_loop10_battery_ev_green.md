# Checkpoint 28A Round 161 R3 Loop 10 Battery / EV / Green-Energy

## 목적

`docs/round/round_161.md`의 R3 Loop 10 내용을 별도 calibration pack으로 반영했다.

이 라운드는 2차전지, EV, ESS, 전고체, 태양광, 풍력, 수소 같은 친환경 서사를 바로 Green으로 올리지 않는다. 핵심은 “수요 서사”가 아니라 `EPS/FCF 체급 변화`, `실제 매출 인식`, `ESS OPM`, `가동률`, `FCF`, `EPS revision`, `안전/규제 리스크`가 같이 확인되는지다.

쉬운 예시는 다음과 같다.

- `LGES-Tesla Megapack 3` 계약은 고객, 용도, 규모, 기간, 생산 거점이 확인되면 Stage 2 근거가 된다.
- 하지만 Lansing ramp-up, ESS 마진, 가동률, FCF, EPS 상향이 보이기 전에는 Stage 3-Green 근거가 아니다.
- `UFLPA`, `BESS 화재`, `SOH 불투명성`, `계약 취소`, `idle plant`는 좋은 성장 서사를 막는 RedTeam 축이다.

## 반영 파일

- `src/e2r/sector/round161_r3_loop10_battery_ev_green.py`
- `src/e2r/cli/build_round161_r3_loop10_report.py`
- `tests/test_round161_r3_loop10_battery_ev_green.py`
- `data/e2r_case_library/cases_r3_loop10_round161.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round161_r3_loop10_v10.csv`
- `output/e2r_round161_r3_loop10_battery_ev_green/`
- 원문 23개 핵심 target에 인접 R3 guardrail target 3개를 더해 총 26개 target으로 분리 유지

쉬운 예:

```text
ESS_TESLA_MEGAPACK_SUPPLY_CHAIN
-> 고객·용도·기간·생산시점이 있으면 Stage 2 근거

SPECULATIVE_BATTERY_TECH
-> 전고체/신소재 이름표만 있으면 RedTeam-first

둘 다 배터리 테마로 묶이지만,
하나는 계약 visibility이고 다른 하나는 과열 방어 축이다.
```

## v10 기본 점수축

| component | weight | 해석 |
| --- | ---: | --- |
| eps_fcf_opm_transition | 24 | Stage 3의 중심. ESS OPM, FCF, EPS revision 없이는 Green 금지 |
| contract_visibility | 22 | 고객, 금액, 기간, GWh, 생산시점이 확인될수록 Stage 2 강화 |
| demand_durability_structural_change | 16 | EV 성장 서사가 아니라 grid ESS, AI data center storage 같은 지속성 확인 |
| capa_utilization_capital_efficiency_fcf_stability | 10 | 라인 전환, ramp-up, idle plant 해소, 가동률 확인 |
| market_mispricing_rerating_gap | 8 | 시장이 아직 EV CAPA/정책 테마로만 보는지 확인 |
| valuation_room_4b_runway | 6 | 이미 가격에 반영된 테마는 4B-watch로 제한 |
| safety_regulatory_disclosure_confidence | 14 | 계약취소, UFLPA, BESS fire, SOH opacity 같은 안전·규제·공시 리스크 강화 |

원문 순서로 보면 `안전·규제·disclosure confidence`가 14점으로 네 번째 축이다.
예를 들어 BESS 수요가 좋아도 화재·인허가·보험비 문제가 생기면 Stage 3-Green을 막아야 한다.

## 케이스 방향

- Stage 2 후보: `Tesla/LGES Megapack`, `SK On-Flatiron`, `Ford Energy`, `Redwood`, `QuantumScape/VW`
- 4C/RedTeam 후보: `LGES-Ford 계약 취소`, `LGES-Freudenberg 계약 취소`, `Ultium Ohio idle`, `Qcells UFLPA`, `Orsted impairment`
- 안전/투명성 오버레이: `EV/BESS fire`, `BESS permitting`, `SOH transparency`

## 산출 요약

- target_count: 26
- source_target_count: 23
- helper_overlay_target_count: 3
- case_candidate_count: 23
- score_stage_price_alignment_count: 12
- green_possible_count: 2
- watch_yellow_first_count: 14
- redteam_first_count: 10
- gate_only_target_count: 6

## Guardrail

- production scoring은 변경하지 않았다.
- case record는 candidate-generation input이 아니다.
- EV battery CAPA, ESS 계약, solid-state license, solar factory, wind PPA만으로 Green을 만들지 않는다.
- 계약금액, 기간, GWh, ESS margin, utilization, FCF, stage price가 없으면 만들지 않는다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round161_r3_loop10_battery_ev_green.py -v
PYTHONPATH=src python -m e2r.cli.build_round161_r3_loop10_report
```

결과:

- Round 161 전용 테스트 14개 통과
- 전체 테스트 2074개 통과
- v10 score profile 생성
- case JSONL 생성
- summary, guardrail, risk overlay, price validation, stage cap, score-stage-price alignment 리포트 생성
- production scoring 변경 없음
