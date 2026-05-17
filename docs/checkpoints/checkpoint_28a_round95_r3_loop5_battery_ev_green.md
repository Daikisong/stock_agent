# Checkpoint 28A Round 95 R3 Loop 5 Battery / EV / Green-Energy Pack

## 목적

`docs/round/round_95.md`의 R3 Loop 5 내용을 case library / score-profile 설계 자료로 반영했다. 이번 패치는 생산 scoring을 바꾸지 않는다. 목적은 2차전지·전기차·친환경 대섹터에서 “EV 성장 narrative”와 “반복 EPS/FCF 증거”를 분리하는 것이다.

쉬운 예시는 이렇다. EV 배터리 공장이 늘어나는 뉴스는 Stage 1 후보가 될 수 있다. 하지만 같은 공장이 idle 상태가 되거나 고객사가 계약을 취소하면 그 증거는 성장 증거가 아니라 4C 리스크다. 반대로 ESS 계약은 고객, 금액, 기간, GWh, 마진, 가동률, FCF가 확인될수록 Stage 2 이상으로 볼 수 있다.

## 반영 내용

- 신규 모듈: `src/e2r/sector/round95_r3_loop5_battery_ev_green.py`
- 신규 CLI: `src/e2r/cli/build_round95_r3_loop5_report.py`
- 신규 테스트: `tests/test_round95_r3_loop5_battery_ev_green.py`
- 신규 archetype:
  - `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`
  - `EV_CAPA_CONTRACT_CANCELLATION`
- 신규/교정 case:
  - `lg_energy_lfp_4_3b_contract_initial_case`
  - `tesla_lges_megapack3_lansing_case`
  - `lges_freudenberg_contract_cancel_case`
  - `ford_lges_ev_contract_cancel_case`를 EV 계약 취소 gate로 이동
  - `lithium_ess_demand_recovery_case` stage2 marker를 `2026-01-04`로 교정

## 산출물

- `data/e2r_case_library/cases_r3_loop5_round95.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round95_r3_loop5_v5.csv`
- `output/e2r_round95_r3_loop5_battery_ev_green/round95_r3_loop5_battery_ev_green_summary.md`
- `output/e2r_round95_r3_loop5_battery_ev_green/round95_r3_loop5_case_matrix.csv`
- `output/e2r_round95_r3_loop5_battery_ev_green/round95_r3_loop5_stage_date_plan.csv`
- `output/e2r_round95_r3_loop5_battery_ev_green/round95_r3_loop5_green_guardrails.md`
- `output/e2r_round95_r3_loop5_battery_ev_green/round95_r3_loop5_risk_overlays.md`
- `output/e2r_round95_r3_loop5_battery_ev_green/round95_r3_loop5_price_validation_plan.md`
- `output/e2r_round95_r3_loop5_battery_ev_green/round95_r3_loop5_price_fields.csv`

## 요약 수치

- target_count: 20
- case_candidate_count: 18
- structural_success_count: 1
- success_candidate_count: 6
- cyclical_success_count: 1
- failed_rerating_count: 1
- overheat_count: 1
- stage4b_case_count: 2
- stage4c_case_count: 8
- green_possible_count: 2
- redteam_first_count: 8
- gate_only_target_count: 4

## 해석

Round 95의 핵심 교정은 두 가지다.

첫째, `ESS_TESLA_MEGAPACK_SUPPLY_CHAIN`은 2025년 최초 LFP 계약 공시의 미공개 리스크와 2026년 Tesla Megapack 3 용도 확인을 분리한다. 고객과 사용처가 확인되면 visibility는 올라가지만, Lansing ramp-up, 실제 매출 인식, ESS OPM, 가동률, FCF가 없으면 Stage 3-Green으로 올리지 않는다.

둘째, `EV_CAPA_CONTRACT_CANCELLATION`은 성장 축이 아니라 RedTeam gate다. 예를 들어 장기 EV 배터리 계약이 있어도 고객 EV 전략 변화로 계약이 취소되면 기대 매출이 사라진 것이므로 4C 후보로 본다.

## 검증 명령

```bash
PYTHONPATH=src python -m e2r.cli.build_round95_r3_loop5_report
PYTHONPATH=src python -m unittest tests.test_round95_r3_loop5_battery_ev_green -v
```

전체 테스트는 커밋 전 최종 검증에서 실행한다.

## Guardrails

- 생산 scoring threshold는 변경하지 않았다.
- case records는 candidate-generation input이 아니다.
- 계약금액, 고객, 기간, GWh, 마진, 가동률, 회수량, SOH, stage price는 추정하지 않는다.
- EV 성장 narrative만으로 Stage 3-Green을 만들지 않는다.
- BESS/EV 화재, 인증, 보험, 시설규제, 계약 취소는 positive score가 아니라 RedTeam gate다.
