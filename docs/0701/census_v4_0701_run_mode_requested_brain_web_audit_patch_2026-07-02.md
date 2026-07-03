# Census v4 0701 Run-Mode Requested Brain/Web Audit Patch

작성 시각: 2026-07-02 KST

## 한 줄 결론

`brain_web_mode=enabled`만 보고 Brain/Web audit이 요청됐는지 판단하던 구멍을 막았다.

이제 `run_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED` 또는 `run_mode=FULL_LIVE_BRAIN_CENSUS`처럼 실행 모드 자체가 Brain/Web/Web acquisition을 요구하면, 별도 flag가 `disabled`여도 개별 audit이 `DISABLED_HONESTY_PASS`로 넘어가지 않는다.

쉬운 예:

```text
나쁜 이전 해석:
  run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
  brain_web_mode = disabled
  web audit = DISABLED_HONESTY_PASS

문제:
  실행 모드 이름은 웹/두뇌를 요구하는데,
  세부 flag만 보고 "안 돌린 게 정직하니 PASS"처럼 보일 수 있다.

패치 후:
  run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
  brain_web_mode = disabled
  brain audit = FAIL
  web audit = FAIL
  extractor audit = FAIL
```

## 왜 중요한가

`goal2.md`, `goal3.md`의 핵심 요구는 이것이다.

```text
LLM Brain / Web / Naver / IR / Report를 안 돌렸으면 안 돌렸다고 낮게 라벨링한다.
돌렸다고 말하려면 planner/search/fetch/extractor/claim/trace leaf가 실제로 있어야 한다.
```

그런데 audit 요청 여부를 `brain_web_mode` 하나로만 보면 다음 같은 혼선이 가능했다.

```text
run_mode가 BRAIN_AND_WEB_ACQUISITION_ENABLED
→ 운영자는 Brain/Web acquisition을 요구했다고 이해

brain_web_mode가 disabled
→ 개별 web/extractor audit은 DISABLED_HONESTY_PASS
```

이건 goal의 “run mode hard labels”와 맞지 않는다.

## 코드 변경

파일:

```text
src/e2r/census/census_runner_v4.py
```

추가/변경한 판단 축:

```text
_config_requests_brain_planner
_config_requests_web_acquisition
_config_requests_llm_claim_extraction
_run_mode_requests_brain_planner
_run_mode_requests_web_acquisition
_run_mode_requests_llm_claim_extraction
```

적용 대상:

```text
_brain_audit
_web_audit
_extractor_audit
_config_requests_brain_web
```

새 출력 필드:

```text
requested_by_run_mode
requested_by_brain_web_mode
```

이 필드는 다음 에이전트가 “이 audit이 왜 requested로 판단됐는지”를 바로 확인할 수 있게 한다.

## 모드별 의도

### BRAIN_TRIAGE_ENABLED

```text
Brain planner 필요
Web fetch / LLM claim extractor는 필수 아님
```

따라서:

```text
brain audit: requested_by_run_mode=true, planner 없으면 FAIL
web audit: requested_by_run_mode=false, DISABLED_HONESTY_PASS 가능
extractor audit: requested_by_run_mode=false, DISABLED_HONESTY_PASS 가능
```

### BRAIN_AND_WEB_ACQUISITION_ENABLED

```text
Brain planner 필요
Web/news acquisition 필요
Claim extractor 필요
```

따라서:

```text
brain audit: planner 없으면 FAIL
web audit: search/fetch 없으면 FAIL
extractor audit: extractor run 없으면 FAIL
```

### FULL_LIVE_BRAIN_CENSUS

`BRAIN_AND_WEB_ACQUISITION_ENABLED`보다 더 강한 운영 모드로 같은 방향의 gate가 적용된다.

### LEDGER_REFRESH_CENSUS

현재 canonical output의 모드다.

```text
Brain/Web/Web acquisition 요청 안 됨
planner calls = 0
web tasks = 0
claim extractor runs = 0
```

이 경우 개별 audit은 disabled honesty pass를 낼 수 있지만, readiness는 Brain/Web pass를 claim하지 않는다.

## 테스트

추가 테스트:

```text
tests/test_census_v4_run_mode_honesty.py

test_run_mode_request_prevents_disabled_brain_web_audit_pass
test_brain_triage_run_mode_requires_planner_but_not_web_fetch
```

검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate -v
```

결과:

```text
Ran 28 tests
OK
```

V4 전체:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
```

결과:

```text
Ran 109 tests in 63.167s
OK
```

Full repo:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
exit_code = 0
test_count = 4992
failed_count = 0
error_count = 0
duration_seconds = 184.878
log_sha256 = 2207625b90762539d78da558bdcfb16a129f50d493375d3f3e8bf4485f5a4043
```

## 재생성한 output

```text
output/test_census_v4_verified_full_tests
output/test_census_v4_verified_full_tests_smoke
output/census_v4/2026-07-01
docs/operational/census_mode_v4_*
```

Canonical output 현재값:

```text
run_mode = LEDGER_REFRESH_CENSUS
brain_web_mode = disabled

brain_planner_audit:
  verdict = PASS
  requested_by_run_mode = false
  requested_by_brain_web_mode = false
  llm_claimed_but_zero_calls_count = 0

web_naver_acquisition_audit:
  verdict = DISABLED_HONESTY_PASS
  requested_by_run_mode = false
  requested_by_brain_web_mode = false
  web_claimed_but_zero_search_count = 0

llm_claim_extraction_audit:
  verdict = DISABLED_HONESTY_PASS
  requested_by_run_mode = false
  requested_by_brain_web_mode = false
  llm_claim_extractor_claimed_but_zero_count = 0
```

즉 canonical run은 여전히 Brain/Web을 돌린 것이 아니다. 하지만 이제 run mode가 Brain/Web을 요구하면 개별 audit이 disabled pass로 숨지 못한다.

## 남은 blocker

이번 패치는 honesty gate를 더 정확히 만든 것이다. 운영 완료는 아니다.

계속 남는 goal blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
controlled_semantic_replay_pending
```

다음 실질 패치 방향:

```text
1. BRAIN_AND_WEB_ACQUISITION_ENABLED 또는 HYBRID_CENSUS에서 실제 provider/source/extractor leaf를 생성
2. accepted Brain/Web claim -> primitive -> score contribution -> StageCourt -> census_stage_status promotion 닫기
3. production FULL_THESIS row를 controlled smoke가 아니라 production source chain으로 만들기
```

## 다음 에이전트 공격 질문

1. `run_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED`인데 `brain_web_mode=disabled`이면 모든 Brain/Web 관련 audit이 실패하는가?
2. `run_mode=BRAIN_TRIAGE_ENABLED`는 planner만 요구하고 web/extractor는 요구하지 않는가?
3. `HYBRID_CENSUS --brain-web-mode enabled`에서는 Brain/Web readiness gate가 실제 provider/source/extractor leaf를 요구하는가?
4. canonical `LEDGER_REFRESH_CENSUS`가 여전히 Brain/Web을 돌렸다고 overclaim하지 않는가?
5. readiness report가 `BRAIN_WEB_EVIDENCE_PASS`를 붙이는 조건이 leaf artifact 기반인가?
