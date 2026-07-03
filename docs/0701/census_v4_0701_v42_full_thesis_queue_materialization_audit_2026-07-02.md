# Census v4 0701 v42 Full Thesis Queue Materialization Audit

작성일: 2026-07-02 KST

## 0. 결론

v41에서 확인한 현재 진실:

```text
CENSUS_EVENT_BOARD Stage row는 있다.
FULL_THESIS 운영 Stage row는 0개다.
```

v42에서 패치한 것:

```text
full_thesis_refresh_queue가 있는데 왜 production FULL_THESIS candidate가 0개인지
full_thesis_production_runner_audit.json에 직접 드러나게 했다.
```

쉬운 예:

```text
예전:
  full_thesis_refresh_queue_candidate_count = 85
  candidate_row_count = 0

  왜 0개인지 다시 코드와 leaf를 파야 했다.

이제:
  refresh_queue_unmaterialized_candidate_count = 85
  materialization_blocker = full_thesis_refresh_task_has_no_research_brain_stagecourt_trace

  즉 "할 일 목록은 85개 있지만, Research Brain/공식 full-thesis 실행이 StageCourt trace를 아직 만들지 않았다"가 바로 보인다.
```

## 1. 코드 변경

수정:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
```

추가 audit fields:

```text
candidate_source_counts
refresh_queue_materialized_candidate_count
refresh_queue_unmaterialized_candidate_count
refresh_queue_unmaterialized_sample
refresh_queue_to_candidate_rule
```

추가 blocker:

```text
full_thesis_refresh_queue_has_no_brain_stagecourt_trace_candidates
```

단, 이 blocker는 production full-thesis mode가 요청됐는데 queue 후보가 Brain/Web 또는 official-full-thesis StageCourt trace로 materialize되지 않은 경우에 붙는다.

## 2. candidate source 분리

candidate는 두 경로로만 생긴다.

```text
brain_web_partial_stage_row
  Brain/Web partial row가 이미 census_stage_status에 있고,
  그 row가 production FULL_THESIS 승격 후보가 되는 경우.

stagecourt_trace_direct_scan
  census_stage_status에는 아직 BRAIN_WEB_PARTIAL row가 없어도,
  stagecourt_traces.jsonl에 research_brain_v4_attempt trace가 직접 존재해서 후보가 되는 경우.
```

v42는 이 분포를 `candidate_source_counts`로 남긴다.

예:

```json
{"brain_web_partial_stage_row": 1}
```

또는:

```json
{"stagecourt_trace_direct_scan": 1}
```

## 3. queue materialization rule

새 규칙:

```text
full_thesis_refresh_queue row는 그 자체로 production candidate가 아니다.

같은 symbol에 대해 Research Brain 또는 official-full-thesis 실행이
stagecourt_traces.jsonl row를 만들었을 때만 production candidate가 된다.
```

audit에 남는 설명:

```text
A full_thesis_refresh_queue row becomes a production candidate only after Research Brain or official-full-thesis execution produces a direct stagecourt_traces row for the same symbol. Queue rows alone never promote Stage.
```

중요:

```text
queue row만으로 점수나 Stage를 승격하지 않는다.
```

## 4. canonical 재생성 결과

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --target-gate anti_fake \
  --write-operational-docs true \
  --fail-on-critical-audit true
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
STATUS=0
```

생성된 operational audit:

```text
docs/operational/census_mode_v4_full_thesis_production_runner_audit.json
docs/operational/census_mode_v4_readiness_verdict.md.json
```

핵심 값:

```text
verdict = NOT_REQUESTED
production_mode_requested = false
full_thesis_refresh_queue_candidate_count = 85
candidate_row_count = 0
candidate_source_counts = {}
refresh_queue_materialized_candidate_count = 0
refresh_queue_unmaterialized_candidate_count = 85
promoted_full_thesis_row_count = 0
```

readiness에도 같은 요약이 들어간다:

```json
{
  "full_thesis_production_runner_audit": {
    "verdict": "NOT_REQUESTED",
    "production_mode_requested": false,
    "full_thesis_refresh_queue_candidate_count": 85,
    "candidate_row_count": 0,
    "candidate_source_counts": {},
    "refresh_queue_materialized_candidate_count": 0,
    "refresh_queue_unmaterialized_candidate_count": 85,
    "promoted_full_thesis_row_count": 0
  }
}
```

sample에 포함된 예:

```text
000660 SK하이닉스
005930 삼성전자
001470 삼부토건
```

각 sample blocker:

```text
materialization_blocker = full_thesis_refresh_task_has_no_research_brain_stagecourt_trace
blocked_reason = full_thesis_refresh_task_not_run
```

해석:

```text
현재 canonical run은 ledger-refresh/anti-fake run이다.
그래서 Brain/Web이 disabled이고 production FULL_THESIS도 NOT_REQUESTED다.

다만 queue 85개가 모두 "아직 StageCourt trace로 materialize되지 않았다"는 사실이 audit에 명시된다.
```

## 5. 테스트

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 13 tests in 4.438s
OK
```

관련 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_report_generated_from_leaf_audit \
  tests.test_census_v4_manifest_counts_match_report -v
```

결과:

```text
Ran 27 tests in 29.737s
OK
```

readiness 노출 보강 후 추가 타깃 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks -v
```

결과:

```text
Ran 8 tests in 20.052s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v > /tmp/census_v42b_full_unittest.log 2>&1
```

결과:

```text
Ran 5073 tests in 202.898s
OK
```

로그:

```text
/tmp/census_v42b_full_unittest.log
```

## 6. 현재 진실표

v42 이후 현재 진실:

```text
CENSUS_EVENT_BOARD 상태판 Stage:
  존재

full_thesis_refresh_queue:
  85개

refresh_queue materialized candidate:
  0개

FULL_THESIS 운영 Stage:
  0개

FULL_E2R_100 verified score:
  0개
```

이제 오해하면 안 되는 점:

```text
full_thesis_refresh_queue 85개는 "평가해야 할 후보"다.
FULL_THESIS candidate 0개는 "평가 결과가 아직 StageCourt trace로 닫히지 않았다"는 뜻이다.
```

## 7. 다음 패치 방향

다음 단계는 audit을 더 꾸미는 것이 아니다.

필요한 실제 chain:

```text
full_thesis_refresh_queue
-> Research Brain planner
-> official-first source tasks
-> source_task_executions
-> evidence_documents / evidence_anchors
-> accepted_claims
-> primitive_states
-> score_contributions
-> stagecourt_traces
-> production FULL_THESIS candidate
-> census_stage_status stage_scope=FULL_THESIS
```

다음 에이전트가 볼 포인트:

```text
1. production_mode_requested=true인 run에서 refresh_queue_unmaterialized_candidate_count가 줄어드는가?
2. 줄었다면 candidate_source_counts가 brain_web_partial_stage_row 또는 stagecourt_trace_direct_scan으로 잡히는가?
3. candidate가 생겨도 missing_green_gate_primitives / claim_quality_blockers 때문에 promotion이 막히는가?
4. promotion이 되면 brain_to_claim_trace.census_stage_status_id가 채워지는가?
5. 그래도 Brain/Web gate와 FULL_THESIS production gate를 서로 섞어 PASS로 과장하지 않는가?
```

## 8. 한계

v42는 운영 Stage를 만든 패치가 아니다.

v42가 증명한 것:

```text
queue가 있는데 candidate가 없는 상태를 숨기지 않는다.
candidate가 있으면 어떤 경로에서 왔는지 분리한다.
queue row만으로 Stage를 승격하지 않는다.
```

v42가 아직 증명하지 않은 것:

```text
Brain/Web/official-full-thesis 실행이 실제 source-backed FULL_THESIS row를 만든다.
```
