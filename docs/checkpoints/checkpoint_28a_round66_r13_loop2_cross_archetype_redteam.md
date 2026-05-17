# Checkpoint 28A Round 66: R13 Loop 2 Cross-Archetype RedTeam / 4B / Price Validation

## 목적

Round 66은 새 섹터를 추가한 작업이 아니라 R1~R12에서 나온 후보를 마지막으로 거르는 공통 검문소다.

쉬운 예시는 이렇다.

- SK하이닉스 HBM처럼 구조가 맞은 사례도, 이미 시장이 대부분 인정해 가격이 많이 반영됐으면 `SECTOR_SUCCESS_BUT_4B_WATCH`로 따로 감시한다.
- Supermicro처럼 AI 서버 매출 성장이 강했어도 감사인 사임, 공시 지연, 내부통제 문제가 나오면 `REDTEAM_ACCOUNTING_TRUST_OVERLAY` hard gate로 Green을 막는다.
- 정책/MOU/질병 이벤트는 실제 정부 주문, 예산, 계약, 매출 가이던스로 올라오기 전까지 `EVENT_PREMIUM`으로 분리한다.

## 반영 내용

- 추가 canonical archetype
  - `EVENT_TO_CONTRACT_ESCALATION`
  - `SECTOR_SUCCESS_BUT_4B_WATCH`
  - `COMMERCIALIZATION_FAILURE`
  - `AFFO_CASHFLOW_INTEGRITY_RISK`
  - `STABLECOIN_CONVERTIBILITY_RISK`
- 추가 모듈
  - `src/e2r/sector/round66_r13_loop2_cross_archetype_redteam.py`
  - `src/e2r/cli/build_round66_r13_loop2_report.py`
  - `tests/test_round66_r13_loop2_cross_archetype_redteam.py`
- 생성 산출물
  - `data/e2r_case_library/cases_r13_loop2_round66.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round66_r13_loop2_v2.csv`
  - `output/e2r_round66_r13_loop2_cross_archetype_redteam/round66_r13_loop2_cross_archetype_redteam_summary.md`
  - `output/e2r_round66_r13_loop2_cross_archetype_redteam/round66_r13_loop2_case_matrix.csv`
  - `output/e2r_round66_r13_loop2_cross_archetype_redteam/round66_r13_loop2_overlay_target_matrix.csv`
  - `output/e2r_round66_r13_loop2_cross_archetype_redteam/round66_r13_loop2_stage_date_plan.csv`
  - `output/e2r_round66_r13_loop2_cross_archetype_redteam/round66_r13_loop2_redteam_gate_plan.md`
  - `output/e2r_round66_r13_loop2_cross_archetype_redteam/round66_r13_loop2_price_validation_plan.md`
  - `output/e2r_round66_r13_loop2_cross_archetype_redteam/round66_r13_loop2_price_fields.csv`

## 케이스 요약

- overlay target: 16개
- case candidate: 18개
- structural success: 1개
- success candidate: 3개
- cyclical success: 1개
- event premium: 1개
- overheat: 1개
- failed rerating: 4개
- Stage 4B marker 포함: 2개
- Stage 4C thesis break: 7개
- hard gate target: 7개

## Green Guardrail

Round 66 기준으로 Stage 3-Green은 점수만으로 나오면 안 된다.

필수 조건은 다음 다섯 가지다.

1. cross-evidence
2. EPS/FCF 지속성
3. 가격경로 alignment
4. hard RedTeam flag 부재
5. 4B 과열 미포화

예를 들어 가격만 오른 테마주는 `PRICE_ONLY_RALLY`로 남겨야 한다. 반대로 실제 주문과 매출 가이던스가 붙은 이벤트는 `EVENT_TO_CONTRACT_ESCALATION`으로 Stage 2 후보가 될 수 있지만, 그래도 바로 Green은 아니다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round66_r13_loop2_cross_archetype_redteam -v
python -m compileall -q src/e2r/sector/round66_r13_loop2_cross_archetype_redteam.py src/e2r/cli/build_round66_r13_loop2_report.py tests/test_round66_r13_loop2_cross_archetype_redteam.py
PYTHONPATH=src python -m e2r.cli.build_round66_r13_loop2_report
```

결과:

- Round 66 전용 테스트 11개 통과
- Round 66 리포트 생성 성공
- production scoring/staging/red-team 모듈은 Round 66 case pack을 import하지 않음

## 주의

- 이 작업은 calibration/evaluation material이다.
- production scoring threshold는 바꾸지 않았다.
- case record는 candidate generation input이 아니다.
- API key 또는 민감정보는 산출물에 쓰지 않았다.
- 투자 권고 문구는 추가하지 않았다.
