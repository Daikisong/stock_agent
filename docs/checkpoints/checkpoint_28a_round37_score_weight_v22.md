# Checkpoint 28A Round 37: Score-Weight Validation v2.2

## 목적

Round 37은 얇게 남아 있던 defense-tech, semiconductor utility infra, cold-chain, water-reuse, satellite connectivity, defense AI software, AI data-center power equipment, counter-UAS 계열을 보강한다.

이번 작업은 production scoring 변경이 아니다. 예를 들어 `Anduril` 같은 케이스명은 후보 생성 근거가 아니고, `government_framework`, `procurement_quantity`, `delivery_schedule`, `op_eps_revision`처럼 실제 증거로 확인되는 필드만 나중에 점수 근거가 될 수 있다.

## 반영 파일

- `src/e2r/sector/round37_score_weight_v22.py`
- `src/e2r/cli/build_round37_score_weight_report.py`
- `tests/test_round37_score_weight_v22.py`
- `data/e2r_case_library/cases_v19_round37.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round37_v22.csv`
- `output/e2r_round37_score_weight_v22/round37_score_weight_v22_summary.md`
- `output/e2r_round37_score_weight_v22/round37_case_candidate_matrix.csv`
- `output/e2r_round37_score_weight_v22/round37_green_guardrail_review.md`
- `output/e2r_round37_score_weight_v22/round37_archetype_price_validation_plan.md`
- `output/e2r_round37_score_weight_v22/round37_defense_tech_review.md`
- `output/e2r_round37_score_weight_v22/round37_utility_infra_review.md`
- `output/e2r_round37_score_weight_v22/round37_recurring_platform_review.md`

## 요약

- target_count: 8
- case_candidate_count: 32
- success_candidate_count: 14
- counterexample_or_risk_count: 18
- stage4b_case_count: 1
- stage4c_case_count: 6
- green_possible_count: 5
- watch_yellow_first_count: 3
- redteam_first_count: 0
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## 핵심 보정

Round 37은 테마명을 점수 근거로 쓰지 않도록 guardrail을 강화했다.

- `DEFENSE_TECH_AUTONOMOUS_SYSTEMS`: prototype이나 private valuation만으로는 점수 근거가 아니다. 정부 framework, 실제 조달수량, 생산능력, 납품 스케줄, OP/EPS 전환이 필요하다.
- `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA`: 반도체 가스는 fab utility-like infra로 볼 수 있지만, long-term onsite contract와 fab ramp-up이 있어야 한다.
- `COLD_CHAIN_REIT_LOGISTICS`: IPO scale보다 occupancy, NOI/AFFO, 에너지비, funding cost, dividend coverage가 중요하다.
- `DATA_CENTER_WATER_REUSE_INFRA`: 물 부족/정책 narrative만으로는 부족하다. 고객 계약과 recurring service revenue가 필요하다.
- `SATELLITE_CONNECTIVITY_INFRA`: SpaceX 관련 label이 아니라 airline/defense contract, backlog, recurring service revenue가 핵심이다.
- `DEFENSE_AI_SOFTWARE_INTELLIGENCE`: AI headline이 아니라 program-of-record와 recurring government software contract가 필요하다.
- `AI_DATA_CENTER_POWER_EQUIPMENT`: bookings가 revenue와 OP로 전환되는지 확인해야 한다.
- `DEFENSE_DRONE_COUNTER_UAS`: M&A나 드론 테마가 아니라 military delivery contract, framework, production capacity, backlog conversion이 필요하다.

## 검증 그룹

- `backlog_contract`: contract-to-backlog-to-revenue conversion, OP/EPS revision, Stage 2 이후 MFE/MAE 검증
- `utility_like_infra`: plant/facility utilization, FCF, customer concentration, energy/funding cost 검증
- `reit_utility_like`: occupancy, NOI/AFFO, dividend coverage, debt cost 검증
- `infra_utility_like`: customer contract, permitting, policy dependency, service margin 검증
- `software_recurring`: recurring revenue, gross margin, RPO/backlog, renewal/churn 검증

## 하지 않은 것

- StageClassifier threshold는 바꾸지 않았다.
- production feature/scoring/staging/red-team 코드는 이 라운드 팩을 import하지 않는다.
- 케이스 레코드는 후보 생성 input이 아니다.
- stage date, price, contract amount, backlog, AFFO, recurring revenue는 임의로 채우지 않았다.

## 실행 명령

```bash
PYTHONPATH=src python -m unittest tests.test_round37_score_weight_v22 -v
PYTHONPATH=src python -m e2r.cli.build_round37_score_weight_report
```

## 테스트 상태

라운드 37 전용 테스트는 통과했다. 전체 테스트는 별도로 실행해 기존 워킹트리 상태를 확인해야 한다.
