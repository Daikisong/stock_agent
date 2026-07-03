# Census v4 SourceTask ID Chain Audit

작성일: 2026-07-01

이 문서는 다음 에이전트가 가장 빡세게 공격해야 할 질문 하나를 고정한다.

```text
SourceTask가 있다고 말한 claim이
실제 문서/앵커/점수 기여/StageCourt trace/대표 census row까지 이어졌는가?
```

## 결론

현재 canonical run 기준 결론은 둘로 나눠야 한다.

```text
대표 event-board score claim 67개:
  SourceTask -> accepted claim -> document -> anchor
  -> score contribution -> StageCourt trace -> representative census row
  id chain이 닫혀 있다.

full thesis / live source 운영 점수:
  아직 아니다.
  live_source_task_satisfaction_pass_allowed=false
  full_thesis_stage=FULL_THESIS_NOT_RUN
```

쉬운 예:

```text
현재는 "출석부에 오른 67개 부분 채점지는 원본 서류까지 역추적된다"는 상태다.
하지만 "전 종목 기말고사 100점 만점 채점이 끝났다"는 뜻은 아니다.
```

## 현재 Stage가 있긴 한가?

있다. 하지만 이름을 조심해야 한다.

```text
전체 census_stage_status row: 3391
stage_scope=CENSUS_EVENT_BOARD: 3391
operator_stage_use=NOT_FULL_THESIS_STAGE: 3391
operator_score_use=NOT_FULL_E2R_SCORE: 3391
FULL_THESIS row: 0
FULL_E2R verified score row: 0
```

즉 현재 Stage는 `Census event-board status`다.

```text
Stage0:
  이번 전체 지도에서 봤지만 현재 catalyst claim이 없음

Stage1 / Stage2-Watch:
  최근 공식 이벤트나 material claim이 있어 watch 상태
  단, full thesis 100점 채점은 아님

Red:
  event-board risk/review label
  단, full thesis 4C 운영 판정은 아님
```

삼성전자와 SK하이닉스도 같은 원칙을 따른다.

```text
삼성전자:
  base_stage=Stage1
  base_stage_display=EVENT_BOARD_STAGE1
  operator_stage_use=NOT_FULL_THESIS_STAGE
  operator_score_use=NOT_FULL_E2R_SCORE
  full_thesis_stage=FULL_THESIS_NOT_RUN
  verified_score=null
  full_e2r_verified_score=null

SK하이닉스:
  base_stage=Stage1
  base_stage_display=EVENT_BOARD_STAGE1
  operator_stage_use=NOT_FULL_THESIS_STAGE
  operator_score_use=NOT_FULL_E2R_SCORE
  full_thesis_stage=FULL_THESIS_NOT_RUN
  verified_score=null
  full_e2r_verified_score=null
```

쉬운 예:

```text
삼성전자/하이닉스가 "Stage1"로 보이는 것은
HBM/C06 full thesis가 Stage1이라는 뜻이 아니다.

뜻은:
"이번 daily census에서 공식 이벤트가 있어서 event-board watch row가 생겼다."
```

## 이번 패치 전 문제

기존 `source_task_satisfaction_audit.json`은 너무 약했다.

기존 검사는 사실상 이 정도였다.

```text
EVIDENCE_OS_ACCEPTED source task인데 accepted_claim_ids가 비었는가?
baseline_only_score_claim_count는 몇 개인가?
```

이 검사는 아래 질문에 답하지 못했다.

```text
1. SourceTask claim이 accepted_claims.jsonl에 실제 존재하는가?
2. claim의 document_id가 evidence_documents.jsonl에 있는가?
3. claim의 anchor_id가 evidence_anchors.jsonl에 있는가?
4. claim document가 SourceTask fetched_document_ids에 들어 있는가?
5. claim이 score_contributions.jsonl의 support_claim_ids로 들어갔는가?
6. score contribution이 stagecourt_traces.jsonl에 들어갔는가?
7. 그 StageCourt trace가 대표 census_stage_status row에 올라갔는가?
8. 대표 row 밖 claim이 몰래 대표 score에 섞였는가?
```

쉬운 예:

```text
기존 방식:
  "숙제를 냈다는 칸이 비었는지만 봄"

새 방식:
  "숙제 제출 기록 -> 실제 숙제 파일 -> 채점표 -> 성적표까지
   번호가 끊기지 않는지 봄"
```

## 이번 패치 내용

`src/e2r/census/census_runner_v4.py`의 `_source_task_satisfaction_audit`를 v2로 강화했다.

새 schema:

```text
schema_version: e2r_census_v4_source_task_satisfaction_audit_v2
```

새 감사 chain:

```text
source_task_executions.jsonl
  task_id
  accepted_claim_ids / baseline_claim_ids / score_claim_ids
  fetched_document_ids

accepted_claims.jsonl
  claim_id
  document_id
  anchor_id

evidence_documents.jsonl
  document_id

evidence_anchors.jsonl
  anchor_id

score_contributions.jsonl
  score_contribution_id
  support_claim_ids

stagecourt_traces.jsonl
  stagecourt_trace_id
  accepted_claim_ids
  score_contribution_ids

census_stage_status.jsonl
  accepted_claim_ids
  score_contribution_ids
  stagecourt_trace_id
```

대표 score claim에는 다음 critical 조건을 건다.

```text
representative_score_claim_without_source_task_execution_count == 0
representative_score_claim_missing_accepted_row_count == 0
representative_score_claim_missing_document_row_count == 0
representative_score_claim_missing_anchor_row_count == 0
representative_score_claim_document_not_in_source_task_fetch_count == 0
representative_score_claim_missing_score_contribution_count == 0
representative_score_claim_missing_stagecourt_trace_count == 0
representative_score_claim_missing_representative_stage_row_count == 0
representative_score_claim_missing_representative_stagecourt_row_count == 0
direct_task_without_accepted_claim_count == 0
```

대표 row 밖 claim은 critical이 아니라 warning으로 남긴다.

이유:

```text
accepted claim이 있다고 전부 대표 Stage row가 되는 것은 아니다.
한 symbol에 여러 atomic decision이 있으면 대표 decision 하나만 census_stage_status에 올라간다.
따라서 대표 row 밖 claim은 "왜 빠졌는지 볼 warning"이지,
대표 score에 섞이지 않았다면 즉시 fail은 아니다.
```

## 현재 감사 결과

현재 canonical output:

```text
output/census_v4/2026-07-01/source_task_satisfaction_audit.json
```

핵심 값:

```text
verdict: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
schema_version: e2r_census_v4_source_task_satisfaction_audit_v2
critical_count: 0
warning_count: 25

source_task_execution_count: 92
source_task_claim_reference_count: 92
source_task_claim_reference_unique_count: 92
accepted_claim_count: 92
evidence_document_count: 92
evidence_anchor_count: 92
score_contribution_count: 92
stagecourt_trace_count: 92

representative_stage_row_count: 3391
representative_stage_row_with_evidence_chain_count: 74
representative_stage_claim_count: 67
representative_score_claim_count: 67
representative_score_contribution_count: 67
representative_stagecourt_trace_count: 74

source_task_chain_closed_to_stagecourt_count: 92
source_task_chain_closed_to_representative_stage_count: 67

baseline_only_score_claim_count: 32
baseline_only_stage_promotion_count: 0

live_source_task_satisfaction_pass_allowed: false
```

critical counts:

```text
direct_task_without_accepted_claim_count: 0
representative_score_claim_without_source_task_execution_count: 0
representative_score_claim_missing_accepted_row_count: 0
representative_score_claim_missing_document_row_count: 0
representative_score_claim_missing_anchor_row_count: 0
representative_score_claim_document_not_in_source_task_fetch_count: 0
representative_score_claim_missing_score_contribution_count: 0
representative_score_claim_missing_stagecourt_trace_count: 0
representative_score_claim_missing_representative_stage_row_count: 0
representative_score_claim_missing_representative_stagecourt_row_count: 0
```

warning counts:

```text
non_representative_source_task_claim_count: 25
source_task_claim_satisfaction_mismatch_count: 0
```

해석:

```text
92개 SourceTask claim은 전부 StageCourt trace까지는 닫힌다.
그중 대표 census row에 채택된 score claim은 67개다.
대표 score claim 67개는 SourceTask까지 역추적이 모두 된다.
대표 row 밖 25개 claim은 warning이다.
```

## 왜 92개 claim인데 대표 claim은 67개인가?

현재 장부:

```text
accepted_claims.jsonl: 92
score_contributions.jsonl: 92
stagecourt_traces.jsonl: 92

census_stage_status.accepted_claim_ids unique: 67
census_stage_status.score_contribution_ids unique: 67
```

이것을 이렇게 읽으면 안 된다.

```text
92개 full thesis Stage가 있다.
92개 종목이 full E2R 점수를 받았다.
```

올바른 해석:

```text
SourceTask/claim 후보는 92개다.
대표 상태판에 채택된 event-board score claim은 67개다.
나머지 25개는 대표 row 밖 warning으로 남아 있다.
```

비유:

```text
한 학생이 숙제 초안 3개를 냈지만,
성적표에는 최종 제출본 1개만 반영될 수 있다.
초안 2개가 성적표에 몰래 섞이면 문제지만,
빠진 이유가 장부화되어 있고 성적에 섞이지 않았으면 critical은 아니다.
```

관련 감사:

```text
non_representative_claim_audit.json:
  verdict: PASS
  accepted_claim_count: 92
  representative_stage_claim_count: 67
  non_representative_claim_count: 25
  non_representative_claim_score_leak_count: 0
```

## 이번 테스트

추가 테스트 파일:

```text
tests/test_census_v4_source_task_satisfaction_chain.py
```

추가한 테스트:

```text
1. 현재 artifact의 대표 SourceTask chain이 닫혀 있는지 확인
2. 대표 score claim에 SourceTask execution이 없으면 FAIL
3. 대표 score claim에 evidence anchor가 없으면 FAIL
4. 대표 row 밖 SourceTask claim은 warning이고 대표 proof가 아님
```

실행 결과:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_source_task_satisfaction_chain \
  tests.test_census_v4_goal_required_audits -v

Ran 7 tests
OK
```

전체 테스트:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/census_v4/2026-07-01/test_result_artifact.json \
  --log output/census_v4/2026-07-01/test_result_artifact.log \
  -- python -m unittest discover -s tests -v

test_count: 4942
failed_count: 0
error_count: 0
duration_seconds: 150.0012
status: OK
```

canonical rerun:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider none \
  --brain-source-acquisition live_official_first \
  --brain-universe-limit 30 \
  --brain-planner-success-limit 30 \
  --brain-planner-batch-size 5 \
  --brain-max-fetches-per-task 3 \
  --brain-stage-promotion-mode disabled \
  --target-gate anti_fake \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim true \
  --fail-on-atomic-mismatch true \
  --fail-on-semantic-guard true \
  --fail-on-critical-audit true \
  --write-operational-docs true \
  --test-result-summary 'PYTHONPATH=src python -m unittest discover -s tests; Ran 4942 tests in 170.248s; OK' \
  --test-result-artifact output/census_v4/2026-07-01/test_result_artifact.json

ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

## 이 PASS가 의미하지 않는 것

아래는 아직 아니다.

```text
live source acquisition pass
Brain/Web evidence pass
full thesis smoke pass
meaningful operational stage pass
FULL_E2R_100 verified score
삼성전자/하이닉스 HBM/C06 full thesis Stage
Stage3-Green / Stage3-Yellow / 4B / 4C 운영 판정
```

왜냐하면 현재 canonical mode가 이것이기 때문이다.

```text
run_mode=LEDGER_REFRESH_CENSUS
brain_web_mode=disabled
source_task_real_fetch_count=0
planner_run_count=0
web_search_task_count=0
llm_claim_extractor_attempt_count=0
full_thesis_smoke_status=PENDING_FULL_THESIS_REFRESH
```

쉬운 예:

```text
"서류철 번호가 맞고 위조는 없다"는 통과다.
"새로 현장 조사를 다녀왔고 모든 종목의 투자 thesis를 확정했다"는 뜻은 아니다.
```

## 다음 에이전트가 때려야 할 공격 질문

### 공격 1. 대표 row 밖 25개 claim

질문:

```text
25개 non-representative SourceTask claim은 왜 대표 row에 채택되지 않았는가?
```

현재 답:

```text
non_representative_claim_audit.json이 score leak은 0으로 막는다.
다만 accepted_claim_without_atomic_decision_count=2는 warning으로 남는다.
```

다음 패치:

```text
비대표 claim exclusion reason을 더 세분화한다.

예:
  duplicate_lower_priority
  superseded_by_representative_decision
  same_symbol_non_material_event
  accepted_but_no_atomic_decision
  pending_manual_review
```

### 공격 2. PrimitiveState / Mapping chain

질문:

```text
SourceTask -> claim -> score/stage는 닫혔는데,
PrimitiveState 장부까지 닫혔는가?
```

현재 답:

```text
PrimitiveState 장부도 별도 audit로 닫혔다.
primitive_state_chain_audit.json: PASS
representative_score_claim_with_primitive_state_count: 67
critical_count: 0
```

현재 추가로 닫힌 것:

```text
score_contribution.mapping_ids의 MAP-* 값을
primitive_mappings.jsonl leaf row 92개로 resolve한다.
mapping_leaf_resolution_supported: true
```

### 공격 3. live source와 ledger refresh 혼동

질문:

```text
SourceTask chain이 닫혔다고 live provider fetch 성공이라고 말하는가?
```

현재 답:

```text
아니오.
live_source_task_satisfaction_pass_allowed=false
source_task_realness_audit.live_source_pass_allowed=false
source_task_real_fetch_count=0
```

다음 패치:

```text
Production daily mode에서 real provider fetch가 있을 때만
LIVE_SOURCE_PASS label을 허용한다.
```

### 공격 4. Stage label 오해

질문:

```text
Stage1 / Stage2-Watch label을 full thesis Stage처럼 보여주지 않는가?
```

현재 답:

```text
모든 row에 operator alias가 붙었다.
operator_stage_use=NOT_FULL_THESIS_STAGE 3391개
operator_score_use=NOT_FULL_E2R_SCORE 3391개
base_stage_display=EVENT_BOARD_...
```

다음 패치:

```text
사용자-facing report와 CLI 표에서도 display field만 기본 노출한다.
raw base_stage는 debug/JSON 필드로만 둔다.
```

### 공격 5. 삼성전자/하이닉스 full thesis smoke

질문:

```text
삼성전자/하이닉스는 그래서 실제 운영 Stage 몇인가?
```

현재 답:

```text
아직 full thesis 운영 Stage가 아니다.
daily event-board는 EVENT_BOARD_STAGE1이다.
full_thesis_stage=FULL_THESIS_NOT_RUN이다.
```

다음 패치:

```text
full_thesis_smoke_tasks.jsonl의 14개 C06/HBM SourceTask를 실제 실행한다.
각 primitive는 SourceTask -> claim -> anchor -> score -> StageCourt까지 닫혀야 한다.
그 전에는 Green/Yellow/4B/4C를 말하지 않는다.
```

## 최종 판단

이번 패치로 닫힌 것:

```text
대표 event-board score claim 67개의 SourceTask id-chain 검증
대표 event-board score claim 67개의 PrimitiveState id-chain 검증
대표 score claim에 SourceTask/document/anchor/contribution/StageCourt/census row가 없으면 fail
대표 score claim에 primitive_state_id가 없거나 atomic/stage row와 다르면 fail
대표 row 밖 claim 25개 warning 분리
primitive_mappings.jsonl 92개 생성
테스트 artifact 4942개 OK
acceptance report line 33/34에 chain 숫자 노출
```

아직 남은 것:

```text
live source acquisition
Brain/Web evidence pass
non-representative claim exclusion reason 세분화
삼성전자/하이닉스 C06/HBM full thesis smoke 실행
전 아키타입 Evidence Contract replay
MEANINGFUL_OPERATIONAL_STAGE_PASS
```

한 줄로 정리:

> 현재는 "가짜 Stage/가짜 점수 방지 상태판"의 대표 event-board claim chain은 훨씬 단단해졌다. 하지만 아직 "실제 운영 full thesis Stage 지도"는 아니며, 다음 패치는 live SourceTask와 full thesis smoke를 이 chain 위에 태우는 것이다.
