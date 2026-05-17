# Checkpoint 28A Round 67: R1 Loop 3 Industrial Orders / Infrastructure

## 목적

Round 67은 R13 Loop 2의 RedTeam/4B/4C 원칙을 반영해 R1 산업재·수주·인프라를 다시 좁힌 작업이다.

핵심은 단순하다.

```text
수주가 있다
≠ Green

계약금액, 계약기간, 거래상대방, 납품스케줄, 수주잔고 질,
마진, OP/EPS 상향, FCF 전환, 가격경로 리레이팅이 같이 있어야
구조적 후보가 된다.
```

예를 들어 변압기 쇼티지는 강한 구조적 근거가 될 수 있다. 하지만 데이터센터 프로젝트가 지연되거나, 장기계약이 저마진이면 Green을 막아야 한다.

## 반영 내용

- 추가 canonical archetype
  - `SHIPBUILDING_NAVAL_MRO`
  - `NUCLEAR_EXISTING_PPA`
  - `PROJECT_DELAY_CAPEX_OVERLAY`
  - `CAPITAL_ALLOCATION_DILUTION_OVERLAY`
- 추가 모듈
  - `src/e2r/sector/round67_r1_loop3_industrial_infra.py`
  - `src/e2r/cli/build_round67_r1_loop3_report.py`
  - `tests/test_round67_r1_loop3_industrial_infra.py`
- 생성 산출물
  - `data/e2r_case_library/cases_r1_loop3_round67.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round67_r1_loop3_v3.csv`
  - `output/e2r_round67_r1_loop3_industrial_infra/round67_r1_loop3_industrial_infra_summary.md`
  - `output/e2r_round67_r1_loop3_industrial_infra/round67_r1_loop3_case_matrix.csv`
  - `output/e2r_round67_r1_loop3_industrial_infra/round67_r1_loop3_stage_date_plan.csv`
  - `output/e2r_round67_r1_loop3_industrial_infra/round67_r1_loop3_green_guardrails.md`
  - `output/e2r_round67_r1_loop3_industrial_infra/round67_r1_loop3_risk_overlays.md`
  - `output/e2r_round67_r1_loop3_industrial_infra/round67_r1_loop3_price_validation_plan.md`
  - `output/e2r_round67_r1_loop3_industrial_infra/round67_r1_loop3_price_fields.csv`

## 요약

- target: 16개
- case candidate: 13개
- structural success: 1개
- success candidate: 5개
- cyclical success: 1개
- event premium: 2개
- failed rerating: 1개
- Stage 4B marker 포함: 2개
- Stage 4C thesis break: 2개
- hard gate target: 2개

## Loop 3 핵심 변경

1. `GRID_TRANSFORMER_SHORTAGE`는 더 강한 Green 후보로 유지하되, 계약금액·기간·납품·마진·EPS 전환을 필수로 둔다.
2. `AI_DATA_CENTER_POWER_EQUIPMENT`는 orders/backlog가 실제 숫자로 잡히면 Stage 2/3 후보가 될 수 있지만, valuation crowding과 project delay를 같이 본다.
3. `NUCLEAR_EXISTING_PPA`와 `NUCLEAR_SMR_GRID_POLICY`를 분리했다. 기존 원전 PPA는 현금흐름 visibility가 있지만, SMR 정책 테마는 비용초과·고객확보·허가·financing 리스크가 크다.
4. `CAPITAL_ALLOCATION_DILUTION_OVERLAY`를 hard gate로 추가했다. 방산처럼 수주가 좋아도 유상증자나 CAPEX 부담이 주주가치를 희석하면 가격경로가 깨질 수 있다.
5. `SHIPBUILDING_NAVAL_MRO`는 MRO 경험과 초기 계약을 Stage 2 reference로 보되, 고마진 반복 MRO 또는 신조 수주 전까지 Green으로 올리지 않는다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round67_r1_loop3_industrial_infra -v
python -m compileall -q src/e2r/sector/round67_r1_loop3_industrial_infra.py src/e2r/cli/build_round67_r1_loop3_report.py tests/test_round67_r1_loop3_industrial_infra.py
PYTHONPATH=src python -m e2r.cli.build_round67_r1_loop3_report
```

결과:

- Round 67 전용 테스트 11개 통과
- Round 67 리포트 생성 성공
- production scoring/staging/red-team 모듈은 Round 67 case pack을 import하지 않음

## 주의

- production scoring threshold는 바꾸지 않았다.
- case record는 candidate generation input이 아니다.
- 계약금액, 계약기간, 마진, 가격은 확인된 값만 써야 한다.
- API key 또는 민감정보는 산출물에 쓰지 않았다.
- 투자 권고 문구는 추가하지 않았다.
