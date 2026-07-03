# Census v4 Stage / Brain-Web Final Forensic Brief - 2026-07-01

이 문서는 다음 에이전트가 빡세게 피드백하기 전에 먼저 고정해야 할 사실을 모은 최종 브리프다.

핵심 질문:

```text
뭔가 잘못되고 있는 거 맞지?
Stage가 있는 애들이 있긴 해?
```

짧은 답:

```text
Stage label은 있다.
하지만 full thesis 운영 Stage는 아직 없다.

Brain/Web enabled smoke에서는 accepted claim, score contribution, StageCourt trace까지 일부 생겼다.
그 smoke 자체에서는 representative census_stage_status 승격은 0개였다.
이후 strict promotion producer는 fixture 테스트에서 대표 row 승격까지 통과했다.
하지만 canonical run은 여전히 disabled이고 real live 운영 승격 row는 0개다.
따라서 Brain/Web 운영 Stage도 아직 없다.
```

쉬운 예:

```text
출석부에는 "주의해서 볼 학생" 표시가 있다.
채점 초안도 일부 만들어졌다.
하지만 최종 성적표에는 아직 반영되지 않았다.
```

## 1. Canonical Run Truth

Source of truth:

```text
output/census_v4/2026-07-01
```

canonical run mode:

```text
run_mode: LEDGER_REFRESH_CENSUS
brain_web_mode: disabled
target_gate: anti_fake
verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

이 PASS의 의미:

```text
가짜 점수/가짜 Stage 완료 선언을 막는 상태판은 통과했다.
```

이 PASS가 아닌 것:

```text
전 종목 full E2R 100점 점수 완료
Brain/Web evidence pass
삼성전자/하이닉스 HBM full thesis Stage 완료
Stage3-Green/Yellow/Red/4B/4C 운영 판정 완료
```

현재 분포:

```text
census_stage_status rows: 3391

base_stage:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

canonical_stage:
  0:       3306
    1:         54
    2:         30
  3-Red:      1

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

score_scale:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

verified_score_present: 0
full_e2r_verified_score_present: 0
brain promoted rows: 0
```

해석:

```text
Stage0/Stage1/Stage2-Watch/Red는 daily/census event 상태 label이다.
full thesis Stage가 아니다.
```

예:

```text
Stage2-Watch   30개
!= full E2R thesis Stage2 확정 30개

Red 1개
!= full thesis Stage3-Red 운영 판정 1개
```

## 2. Enabled Codex Smoke Truth And Strict Promotion Fixture

Source of truth:

```text
/tmp/census_v4_codex_smoke_gScqHy/out
tests/test_census_v4_brain_stage_promotion_gate.py
```

이 smoke는 canonical output이 아니다.
Brain/Web enabled path의 현재 병목을 확인하기 위한 격리 실행이다.

관측값:

```text
readiness_verdict: NOT_READY

brain_web_attempt:
  verdict: ATTEMPTED_NOT_CUTOVER_READY
  planner_provider: codex
  planner_run_count: 3
  real_provider_success_count: 1
  source_task_execution_count: 10
  real_document_fetched_count: 12
  accepted_claim_count: 5
  unique_accepted_claim_count: 2
  brain_to_census_claim_exported_count: 2
  brain_stagecourt_trace_exported_count: 1
  brain_to_census_stage_exported_count: 0
  claim_acceptance_ready: true
  stagecourt_trace_ready: true
  cutover_export_ready: false

brain_stage_promotion:
  verdict: PROMOTION_DISABLED_BY_POLICY
  brain_claim_count: 2
  brain_score_contribution_count: 5
  brain_stage_trace_count: 1
  brain_promoted_stage_row_count: 0
  brain_snapshot_document_count: 3

brain_web_readiness_gate:
  verdict: BLOCKED
  brain_web_evidence_pass_allowed: false
  brain_score_contribution_count: 5
  brain_stage_trace_count: 1
  brain_promoted_stage_row_count: 0
```

해석:

```text
패치 전 Codex smoke 병목:
  accepted claim이 0개라 점수 칸으로 못 감.

해당 격리 smoke의 병목:
  accepted claim, score contribution, StageCourt trace는 일부 생김.
  하지만 representative census_stage_status row 승격이 0개라 운영 Stage로 못 감.
```

그 뒤 코드에는 strict promotion producer가 추가됐다.

```text
_promote_brain_stage_rows(...)
```

fixture 검증에서 아래 조건을 만족하면 대표 row로 승격한다.

```text
brain_web_mode=enabled
brain_stage_promotion_mode=strict
real provider success > 0
source_task_executions row 존재
evidence_documents row 존재
evidence_anchors row 존재
accepted_claim -> score_contribution -> StageCourt trace ID chain resolve
snapshot/fake/provider blocker 0
```

승격 row의 scope:

```text
stage_scope = BRAIN_WEB_PARTIAL
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
full_thesis_stage = FULL_THESIS_NOT_RUN
score_scale = EVENT_WEIGHTED_PARTIAL
```

즉 이 producer는 "Brain/Web partial row를 대표 상태판에 올리는 장치"이지,
`FULL_E2R_100` full thesis 점수를 만드는 장치가 아니다.

쉬운 예:

```text
답안 문장과 채점 메모는 있다.
하지만 공식 성적표에 옮기지 않았다.
그래서 "성적 확정"이라고 말하면 안 된다.
```

## 3. 이번에 막은 Overclaim

발견한 문제:

```text
StageCourt trace가 1개 생겼는데,
attempt audit이 cutover_export_ready=true처럼 보일 수 있었다.
```

왜 문제인가:

```text
StageCourt trace
!= representative census_stage_status row
```

패치 후:

```text
brain_stagecourt_trace_exported_count: 1
brain_to_census_stage_exported_count: 0
stagecourt_trace_ready: true
cutover_export_ready: false
blockers:
  - Research Brain StageCourt traces are not promoted into census_stage_status rows
```

추가 방어:

```text
brain_attempt_cutover_without_promotion_count
```

이 critical count는 누가 다시 `cutover_export_ready=true`를 잘못 세팅했는데 promotion audit이 0개면 잡기 위한 장치다.

## 4. 코드 패치 요약

변경 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/agentic/primitive_aggregator.py
tests/test_census_v4_run_mode_honesty.py
tests/test_census_v4_brain_web_readiness_gate.py
tests/test_census_v4_brain_stage_promotion_gate.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

중요 변경:

```text
1. StageCourt trace export와 census_stage_status promotion을 분리했다.
2. promoted row가 0개면 cutover_export_ready=false가 된다.
3. `_promote_brain_stage_rows(...)`가 strict 조건에서만 `BRAIN_WEB_PARTIAL` 대표 row를 만들고 trace refs를 갱신한다.
4. structured numeric contract fields만 positive contract bridge로 인정한다.
5. "자기주식취득신탁계약" title 같은 단어만으로 contract_quality claim을 만들지 않는다.
6. 2024 계약이라도 effective_end가 2027-05-31이면 2026-07-01 기준 current로 유지된다.
7. raw_assertions를 bundle/export 장부에 남겨 claim이 어디서 왔는지 따라갈 수 있게 했다.
8. tests helper import를 `tests.` 절대 import로 바꿔 직접 지정 테스트도 돌게 했다.
```

쉬운 예:

```text
계약 공시:
  계약금액 1500억원
  최근매출액 대비 15%
  계약기간 2024-06-01 ~ 2027-05-31

as_of_date=2026-07-01이면:
  2024년 공시라도 계약기간이 살아 있으므로 현재 claim으로 볼 수 있다.

반대로:
  "자기주식취득신탁계약체결결정"

은 공급계약이나 매출 bridge가 아니므로 contract_quality 점수를 열면 안 된다.
```

## 5. 검증 결과

직접 실행 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate -v

Ran 26 tests in 22.686s
OK
```

Research Brain v4 evidence extraction:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_evidence_extraction_from_real_document -v

Ran 6 tests
OK
```

Research Brain v4 suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -p 'test_research_brain_v4_*.py'

Ran 25 tests
OK
```

전체 suite artifact도 갱신했다.

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/census_v4/2026-07-01/test_result_artifact.json \
  --log output/census_v4/2026-07-01/test_result_artifact.log \
  -- python -m unittest discover -s tests -v

Ran 4942 tests in 170.248s
artifact duration_seconds: 150.0012
OK
```

## 6. 다음 에이전트 공격 질문

```text
1. StageCourt trace와 representative census_stage_status row를 섞은 곳이 남아 있는가?
2. brain_to_census_stage_exported_count가 0인데 cutover_export_ready=true가 되는 경로가 있는가?
3. snapshot:// evidence document가 strict promotion으로 대표 row에 올라갈 수 있는가?
4. accepted claim, score contribution, StageCourt trace의 claim ID chain이 서로 다른데 통과하는가?
5. Brain/Web readiness gate가 attempt count만 보고 pass하는가?
6. canonical disabled run에서 Brain/Web pass label이 붙는가?
7. Stage2-Watch를 full thesis Stage2로 읽게 하는 문서나 UI가 남아 있는가?
8. Samsung/Hynix daily event row를 C06/HBM full thesis 결과로 오해시키는 산출물이 있는가?
9. source_proxy_only, evidence_url_pending, snippet-only, provider failure가 점수로 들어가는가?
10. old risk / wrong subject / normal audit opinion 같은 known-bad가 다시 Stage/Risk로 들어가는가?
```

## 7. 다음 패치 방향

우선순위:

```text
P1. 실제 Brain/Web enabled canonical/smoke run에서 live source task row를 만든다.
P2. LLM claim extractor attempts를 실제 fetched document와 anchor에 연결한다.
P3. 실제 run의 accepted claim -> score contribution -> StageCourt trace를 strict promotion producer에 태운다.
P4. strict promotion 조건은 이미 fixture-tested 상태다. 다음에는 실제 live run에서 이 조건을 만족시켜야 한다.
    - brain_web_mode=enabled
    - brain_stage_promotion_mode=strict
    - real provider success > 0
    - live source task rows > 0
    - non-snapshot document/anchor
    - accepted claim direct/current/source-backed
    - score contribution claim-backed
    - StageCourt trace claim-backed
    - brain_to_claim_trace.census_stage_status_id resolves
    - blocker 0
P5. 삼성전자/하이닉스 C06/HBM full thesis smoke를 planning-only에서 실제 SourceTask 실행으로 전환한다.
P6. `BRAIN_WEB_PARTIAL`과 별도로 `FULL_THESIS` / `FULL_E2R_100` 경로를 닫는다.
P7. 전 아키타입 replay parity를 source-backed fixture 기준으로 검증한다.
```

완료라고 부르면 안 되는 상태:

```text
full_thesis_stage all FULL_THESIS_NOT_RUN
brain_promoted_stage_row_count = 0
brain_web_evidence_pass_allowed = false
verified_score_present = 0
full_e2r_verified_score_present = 0
```

현재는 여전히 이 상태다.
