# Census v4 0701 v31 Invalid Partial Output CLI Guard

작성일: 2026-07-02 KST

## 0. 결론

이번 v31 패치는 live run이 중간에 멈췄을 때 생기는 partial output을
운영 readiness, score, Stage 증거로 쓰지 못하게 막는 CLI 안전장치다.

쉽게 말하면:

```text
기존:
  live Brain/Web run이 codex_cli claim extractor 대기 중 KeyboardInterrupt로 멈춤.
  output directory에 일부 leaf가 남을 수 있음.
  사람이 그 일부 파일을 보고 "뭔가 돌았으니 READY 근거"로 오해할 수 있음.

변경:
  KeyboardInterrupt 또는 runner exception 발생 시
  partial_run_invalid.json
  PARTIAL_RUN_INVALID.md
  를 output_root에 쓴다.

  CLI stdout = INVALID_PARTIAL_OUTPUT
  KeyboardInterrupt exit code = 130
  runner exception exit code = 1
```

## 1. Goal 문서 요구와 연결

goal 문서의 관련 원칙:

```text
provider failure는 low score나 Red가 아니라 Pending이다.
Brain/Web/Naver/IR/Report가 실행되지 않았으면 실행됐다고 말하지 않는다.
외부 provider blocker를 success로 숨기지 않는다.
leaf artifact가 source of truth지만, 완료되지 않은 partial leaf는 readiness source of truth가 아니다.
```

이번 패치는 이 원칙을 CLI 실패 경로까지 끌어올린다.

예:

```text
as_of_date=2026-07-01 live run에서 문서 fetch 일부가 끝났다.
그런데 LLM claim extractor가 멈춰서 사용자가 Ctrl-C로 끊었다.

정확한 결과:
  INVALID_PARTIAL_OUTPUT
  readiness_evidence_allowed = false
  score_or_stage_evidence_allowed = false
  full_thesis_promotion_allowed = false

잘못된 결과:
  일부 jsonl이 있으니 Brain/Web ran
  일부 claim이 있으니 Stage 가능
  source가 부족하니 낮은 점수/Red 확정
```

## 2. 코드 패치

변경 파일:

```text
src/e2r/cli/run_e2r_census_v4_until_pass.py
tests/test_census_v4_run_mode_honesty.py
```

추가된 marker:

```text
partial_run_invalid.json
PARTIAL_RUN_INVALID.md
```

`partial_run_invalid.json` 핵심 필드:

```json
{
  "schema_version": "e2r_census_v4_invalid_partial_run_v1",
  "verdict": "INVALID_PARTIAL_OUTPUT",
  "readiness_evidence_allowed": false,
  "score_or_stage_evidence_allowed": false,
  "full_thesis_promotion_allowed": false
}
```

## 3. CLI 동작

KeyboardInterrupt:

```text
stdout = INVALID_PARTIAL_OUTPUT
exit_code = 130
partial_run_invalid.status = INTERRUPTED
partial_run_invalid.reason = keyboard_interrupt
```

Runner exception:

```text
stdout = INVALID_PARTIAL_OUTPUT
exit_code = 1
partial_run_invalid.status = FAILED
partial_run_invalid.reason = runner_exception
partial_run_invalid.exception_type = RuntimeError 또는 실제 예외명
```

정상 run:

```text
기존처럼 readiness verdict 출력
target_gate별 exit code 유지
partial_run_invalid marker 생성하지 않음
```

## 4. 왜 필요한가

v29 live diagnostic에서 실제로 이런 일이 있었다.

```text
sourcequality-v29 live attempt:
  codex_cli claim extractor provider 대기
  KeyboardInterrupt 중단
  최종 readiness/report/manifest 생성 전 종료
  INVALID_PARTIAL_OUTPUT으로 폐기해야 하는 산출물
```

v30은 timeout/provider_error를 audit/gate에 올렸다.
v31은 run 자체가 중단됐을 때 output directory에 무효 표식을 남긴다.

둘의 차이:

```text
v30:
  runner가 끝까지 완료된 경우,
  provider_error/timeout row를 audit/gate에서 BLOCKED 처리.

v31:
  runner가 끝까지 완료되지 못한 경우,
  output_root 자체를 INVALID_PARTIAL_OUTPUT으로 표시.
```

## 5. 테스트

실행:

```text
PYTHONPATH=src python -m unittest tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 20 tests / OK
```

새 테스트:

```text
test_cli_keyboard_interrupt_marks_partial_output_invalid
test_cli_runner_exception_marks_partial_output_invalid
```

확인한 것:

```text
KeyboardInterrupt -> exit code 130
RuntimeError -> exit code 1
partial_run_invalid.json 생성
readiness_evidence_allowed = false
score_or_stage_evidence_allowed = false
full_thesis_promotion_allowed = false
config.brain_claim_extractor_timeout_seconds 보존
```

## 6. 현재 운영 상태

이 패치 이후에도 운영 FULL_THESIS는 아직 완료가 아니다.

```text
FULL_THESIS production row = 0
FULL_E2R_100 verified score row = 0
FULL_THESIS refresh queue = 85
```

이번 패치가 닫은 것은:

```text
partial live output을 readiness evidence로 오해하는 문제
provider/runtime failure를 낮은 점수나 Red로 확정하는 방향의 운영 위험
```

아직 남은 것은:

```text
FULL_THESIS refresh queue 85개 실행
source route quality 개선
accepted claim -> score contribution -> StageCourt -> FULL_THESIS row 생성
C01~C36 replay parity
```

## 7. 다음 에이전트 공격 체크리스트

다음 에이전트는 아래를 확인해야 한다.

```text
1. KeyboardInterrupt에서 partial_run_invalid.json이 항상 생성되는가?
2. runner exception에서도 partial_run_invalid.json이 생성되는가?
3. marker가 readiness_evidence_allowed=false를 명시하는가?
4. marker가 score_or_stage_evidence_allowed=false를 명시하는가?
5. marker가 full_thesis_promotion_allowed=false를 명시하는가?
6. 정상 run에는 partial invalid marker가 잘못 생성되지 않는가?
7. partial_run_invalid.json이 있는 output directory를 artifact manifest/pass 근거로 쓰는 코드가 남아 있는가?
8. 문서에서 INVALID_PARTIAL_OUTPUT을 READY/NOT_READY보다 높은 성공처럼 표현하는 곳이 남아 있는가?
```

## 8. 최종 판정

```text
v31 patch status:
  PASS for CLI invalid partial output guard

operational FULL_THESIS:
  still NOT_READY

safe wording:
  "중단된 live output은 INVALID_PARTIAL_OUTPUT이며,
   readiness/score/Stage 증거로 사용할 수 없다."
```

한 줄 결론:

```text
provider가 멈춘 산출물을 이제 그냥 애매한 output directory로 남기지 않고,
명시적으로 무효 산출물로 표시하게 됐다.
```
