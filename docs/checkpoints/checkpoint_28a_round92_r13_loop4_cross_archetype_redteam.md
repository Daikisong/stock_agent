# Checkpoint 28A Round 92: R13 Loop 4 Cross-Archetype RedTeam

## 목적

`round_92.md`는 R1~R12 섹터 후보를 다시 검증하는 공통 R13 레이어다. 섹터 점수를 바꾸는 작업이 아니라, 점수가 높아도 실제로 Green으로 올려도 되는지 확인하는 검문소다.

쉬운 예시는 다음과 같다. 전력기기 후보가 점수는 높아도 계약금액, 고객, 기간, 마진이 공시 detail에서 확인되지 않으면 `DISCLOSURE_CONFIDENCE_CAP`에 걸려 Stage 3 확신을 제한한다.

## 반영 내용

- `src/e2r/sector/round92_r13_loop4_cross_archetype_redteam.py` 추가
- `src/e2r/cli/build_round92_r13_loop4_report.py` 추가
- `tests/test_round92_r13_loop4_cross_archetype_redteam.py` 추가
- `E2RArchetype`에 `CAPEX_AFFO_DILUTION_RISK`, `DISCLOSURE_CONFIDENCE_CAP` 추가
- 산출물 생성:
  - `data/e2r_case_library/cases_r13_loop4_round92.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round92_r13_loop4_v4.csv`
  - `output/e2r_round92_r13_loop4_cross_archetype_redteam/`

## 핵심 결과

- overlay target: 19개
- case candidate: 22개
- hard gate target: 9개
- Stage 4B case: 4개
- Stage 4C case: 8개
- production scoring changed: false
- case records used as candidate-generation input: false

## 새로 추가된 검증축

### CAPEX_AFFO_DILUTION_RISK

데이터센터 REIT나 실물 인프라 후보가 AI 수요를 받더라도, CAPEX가 AFFO per share보다 빠르게 커지면 구조적 증거가 아니다. 예를 들어 매출은 커지는데 주당 현금흐름이 희석되면 좋은 성장처럼 보여도 Green을 막아야 한다.

### DISCLOSURE_CONFIDENCE_CAP

OpenDART 목록에는 계약 제목만 보이고, 실제 계약금액·고객명·용도·기간·마진이 없을 수 있다. 이 경우 Layer 1 후보로는 볼 수 있지만 Stage 3 확신은 detail fetch와 파싱이 확인될 때까지 제한한다.

## 변경하지 않은 것

- StageClassifier threshold는 변경하지 않았다.
- FeatureEngineering / scoring / RedTeam production logic은 이 팩을 import하지 않는다.
- 케이스 레코드는 calibration/evaluation 전용이며 후보 생성 입력으로 쓰지 않는다.
- Stage 3-Green을 쉽게 만들기 위한 완화는 하지 않았다.

## 실행 명령

```bash
PYTHONPATH=src python -m unittest tests.test_round92_r13_loop4_cross_archetype_redteam -v
PYTHONPATH=src python -m e2r.cli.build_round92_r13_loop4_report
```

## 검증 상태

- Round92 대상 테스트: 통과
- 전체 테스트는 최종 커밋 전 재실행 대상

## 다음 작업

R13 Loop 4 이후 다음 라운드는 R1 산업재·수주·인프라 Loop 5로 돌아가되, 이번에 추가한 공통 검증축을 각 섹터별 케이스 팩에 연결해야 한다. 특히 `DISCLOSURE_CONFIDENCE_CAP`는 계약형, 정책형, 의료/바이오, SaaS/ARR 공시 모두에 반복 적용될 수 있다.
