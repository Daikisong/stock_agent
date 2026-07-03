# Census v4 Brain/Web Claim Bridge Audit - 2026-07-01

이 문서는 다음 에이전트가 가장 세게 찔러야 할 부분만 따로 분리한 감사 기록이다.

핵심 질문은 이것이다.

```text
현재 Stage가 있는 애들이 있긴 한가?
있다면 그 Stage는 실제 운영 thesis Stage인가, 아니면 daily/census event 상태판인가?
Research Brain v4에 이미 claim이 있다면 그것을 Census v4 production pass로 써도 되는가?
```

## 결론

```text
Stage label은 있다.
하지만 현재 Census v4의 Stage label은 full thesis Stage가 아니라 event/status-board Stage다.

source-backed accepted claim payload는 있다.
하지만 Brain/Web/LLM live acquisition claim은 아직 없다.

Research Brain v4 기존 보고서는 import해서 참고는 했지만,
snapshot/fixture blocker 때문에 Census production cutover evidence로 쓰면 안 된다.
```

쉬운 예:

```text
현재 된 것:
  raw universe 3940개 중 eligible/stage 대상 3391개 출석부와, 일부 대상 67개의 쪽지시험 채점 근거 92개를 맞춰 봤다.

현재 안 된 것:
  전교생 기말고사 100점 만점 종합 성적표를 채점한 것은 아니다.

Research Brain v4 기존 보고서:
  예전에 모의시험에서 사용한 서류철이다.
  안에 답안 작성 절차는 보이지만 snapshot:// 자료와 fixture blocker가 있어
  실제 운영 시험 답안지로 제출하면 안 된다.
```

## 현재 canonical 출력

기준 산출물:

```text
output/census_v4/2026-07-01
```

핵심 숫자:

```text
stage_status_count: 3391

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

verified_score_present_count: 0
full_e2r_verified_score_present_count: 0
event_evidence_score_present_count: 67

accepted_claims.jsonl: 92 rows
evidence_claims.jsonl: 92 rows
sample_leaf_bundle.jsonl: 67 rows

planner_runs.jsonl: 0 rows
web_search_tasks.jsonl: 0 rows
web_search_results.jsonl: 0 rows
web_fetched_documents.jsonl: 0 rows
claim_extractor_runs.jsonl: 0 rows
brain_to_claim_trace.jsonl: 0 rows
brain_web_attempt_audit.json:
  verdict: NOT_REQUESTED
  attempt_mode: disabled
brain_stage_promotion_audit.json:
  verdict: NOT_REQUESTED
  brain_stage_trace_count: 0
  brain_promoted_stage_row_count: 0
  unsafe_promoted_stage_row_count: 0
brain_web_readiness_gate_audit.json:
  verdict: NOT_REQUESTED
  brain_web_evidence_pass_allowed: false
```

해석:

```text
92개 claim이 67개 event-scored row에 붙어 있다.
67개 row가 full thesis score row라는 뜻은 아니다.
Brain/Web readiness gate도 `NOT_REQUESTED`이므로 Brain/Web claim bridge가 운영 pass라는 뜻이 아니다.
```

## 추가 패치: Brain/Web attempt -> score trace export 경로

canonical `LEDGER_REFRESH_CENSUS` 실행은 여전히 Brain/Web disabled다.
따라서 아래 목록은 현재 canonical output의 실행 증거가 아니라, 별도 `brain_web_mode=enabled` smoke에서 검증해야 할 export 대상이다.

```text
Research Brain v4 production-shadow attempt
-> planner_runs.jsonl
-> research_brain_plans.jsonl
-> source_tasks.jsonl
-> source_task_executions.jsonl
-> evidence_documents.jsonl
-> evidence_anchors.jsonl
-> raw_assertions.jsonl
-> adjudicated_claims.jsonl
-> accepted_claims.jsonl
-> primitive_states.jsonl
-> score_contributions.jsonl
-> stagecourt_traces.jsonl
-> brain_to_claim_trace.jsonl
```

중요한 제한:

```text
이 export가 실제로 생기더라도 claim과 score/stage trace leaf를 남기는 단계다.
아직 census_stage_status.jsonl의 대표 Stage row로 승격하지 않는다.
따라서 accepted claim과 stagecourt trace가 export되어도 brain_web_evidence_pass=false와 NOT_READY를 유지한다.
```

승격 여부는 별도 파일로 확인한다.

```text
output/census_v4/2026-07-01/brain_stage_promotion_audit.json
docs/operational/census_mode_v4_brain_stage_promotion_audit.json
```

canonical run 현재값:

```text
verdict: NOT_REQUESTED
brain_web_mode: disabled
brain_stage_promotion_mode: disabled
brain_stage_trace_count: 0
brain_promoted_stage_row_count: 0
unsafe_promoted_stage_row_count: 0
blockers: []
planner_runs.jsonl: 0 rows
web_fetched_documents.jsonl: 0 rows
claim_extractor_runs.jsonl: 0 rows
brain_to_claim_trace.jsonl: 0 rows
```

해석:

```text
Brain/Web을 요청하지 않았으므로 실패는 아니다.
하지만 Brain/Web 통과도 아니다.
Brain StageCourt trace가 대표 Stage row로 승격된 것도 아니다.
```

쉬운 예:

```text
이제 조사원이 새 서류를 읽으면 서류철과 채점 메모까지 보관함에 들어간다.
하지만 아직 그 채점 메모를 전교 공식 성적표에 자동 반영하지는 않는다.
공식 성적표 승격은 다음 단계에서 census_stage_status 병합으로 닫아야 한다.
```

enabled mode에서 real LLM/provider가 없으면:

```text
planner_runs.jsonl에는 provider failure / not configured row가 남을 수 있다.
real_provider_success_count가 0이면 NOT_READY다.
provider 실패는 낮은 점수나 Red가 아니라 보류/blocker다.
```

예:

```text
어떤 회사가 DART 공급계약 공시를 냈다.
그 공시에서 contract_quality claim 1개와 earnings_visibility claim 1개가 나올 수 있다.
그러면 claim은 2개지만 row는 회사 1개다.

반대로 claim이 있어도 그 claim은 "이번 이벤트 증거"일 수 있고,
"전체 thesis가 100점 만점으로 검증됐다"는 뜻은 아니다.
```

## 새로 고정한 산출물

이번 패치로 추가/강화한 파일:

```text
output/census_v4/2026-07-01/evidence_claims.jsonl
output/census_v4/2026-07-01/research_brain_v4_bridge_audit.json
output/census_v4/2026-07-01/brain_stage_promotion_audit.json
docs/operational/census_mode_v4_research_brain_bridge_audit.json
docs/operational/census_mode_v4_brain_stage_promotion_audit.json
```

`artifact_manifest.json`에도 위 파일이 들어간다.

`evidence_claims.jsonl`의 의미:

```text
accepted_claims.jsonl을 운영 EvidenceClaim payload view로 명시한 파일.
claim_id, document_id, anchor_id, quote_text, subject/target, polarity, temporal_status,
primitive_id, score_eligible 여부를 다시 펼쳐 볼 수 있다.
```

주의:

```text
evidence_claims.jsonl은 Brain/Web live claim이 아니다.
현재 row에는 brain_web_claim=false, full_thesis_claim=false가 찍혀 있다.
```

쉬운 예:

```text
공시 원문에서 "단일판매ㆍ공급계약체결"을 뽑은 것은 증거 claim이다.
하지만 이것만으로 "그 회사의 전체 E2R thesis가 Green"이라고 하면 안 된다.
계약 하나는 쪽지시험 문제 하나의 답이지, 기말고사 전체 답안지가 아니다.
```

## Research Brain v4 bridge audit

기존 Research Brain v4 보고서에서 관측한 값:

```text
bridge_mode: imported_operational_report_bundle
verdict: SHADOW_OR_IMPORT_ONLY
production_cutover_ready: false
shadow_ready: true
accepted_claim_count: 56
unique_accepted_claim_count: 21
real_document_fetched_count: 255
unique_real_document_fetched_count: 63
snapshot_url_count: 255
planner_model_null_count: 30
usable_for_census_cutover: false
```

주의:

```text
여기서 real_document_fetched_count=255는 imported Research Brain report 내부 필드명이다.
같은 audit에 snapshot_url_count=255와 usable_for_census_cutover=false가 있으므로
Census v4 canonical run의 live fetch pass로 읽으면 안 된다.
```

blocker:

```text
Research Brain v4 report is not production_cutover_ready
Research Brain v4 report contains snapshot:// source records
Research Brain v4 readiness text records fixture/snapshot blockers
Research Brain v4 planner rows include missing model identity
```

해석:

```text
Research Brain v4는 "claim extraction 절차가 작동하는 그림"은 보여준다.
하지만 snapshot:// 소스와 fixture blocker가 있으므로
현재 Census v4 production Stage/score 근거로 수입하면 안 된다.
```

쉬운 예:

```text
모의 운전장에서 운전 연습을 한 기록이 있다.
그 기록은 운전 절차 연습 증거로는 유용하다.
하지만 실제 도로 주행 시험 합격증으로 제출하면 안 된다.
```

## readiness verdict가 말하는 것

현재 `readiness_verdict.json` label:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
ATOMIC_STAGE_DECISION_PASS
SCORE_SCALE_PASS
STAGE_SEMANTICS_PASS
SEMANTIC_PRIMITIVE_GUARD_PASS
DAILY_EVENT_FULL_THESIS_SEPARATION_PASS
CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS
FULL_THESIS_SMOKE_PENDING
OFFICIAL_BASELINE_OR_LEDGER_REFRESH_ONLY
OFFICIAL_BASELINE_EVIDENCE_CLAIM_PAYLOAD_PRESENT
RESEARCH_BRAIN_V4_REPORT_BRIDGE_IMPORTED
```

맞는 해석:

```text
가짜 완료 선언을 막는 상태판은 통과했다.
공식 baseline accepted claim payload는 파일로 드러난다.
Research Brain v4 기존 보고서는 import해서 검토했지만 production evidence로 승격하지 않았다.
```

틀린 해석:

```text
Brain/Web이 실제 운영으로 돌았다.
LLM extractor가 이번 Census v4에서 claim을 만들었다.
전 종목 full thesis Stage가 나왔다.
Research Brain v4 결과를 근거로 Brain/Web pass가 됐다.
```

## auditor cross-check

현재 `leaf_artifact_audit.json`에서 0이어야 하는 새 critical count:

```text
accepted_claim_without_evidence_claim_payload_count: 0
evidence_claim_payload_without_accepted_claim_count: 0
evidence_claim_missing_verifiable_anchor_count: 0
evidence_claim_marked_brain_web_in_disabled_run_count: 0
research_brain_bridge_cutover_overclaim_count: 0
```

뜻:

```text
accepted_claim이 있으면 evidence_claim payload view에도 있어야 한다.
evidence_claim은 document_id와 anchor_id가 있어야 한다.
Brain/Web disabled run에서 evidence_claim을 brain_web_claim=true로 표시하면 안 된다.
Research Brain bridge가 snapshot/source blocker를 무시하고 cutover usable이라고 말하면 안 된다.
```

쉬운 예:

```text
상장사 공시에서 뽑은 계약 claim은 증거 파일에 있어야 한다.
그런데 그 claim을 "LLM이 웹에서 찾아온 full thesis claim"이라고 이름표를 바꾸면 감사 실패다.
```

## 왜 아직 운영 Stage가 아닌가

현재 Stage label은 다음 세 층 중 첫 번째에 가깝다.

```text
1. Census/daily event status
   전 종목을 보고 새 이벤트가 있는지 분류한다.

2. Source-backed event score
   특정 공시/리포트/공식자료에서 claim을 뽑아 부분 점수를 준다.

3. Full E2R thesis score
   아키타입별 required primitive를 채우고,
   PrimitiveState -> ScoreContribution -> StageCourt를 통과해 100점 scale과 Stage를 낸다.
```

현재:

```text
1번은 됐다.
2번은 일부 row에 대해 있다.
3번은 전부 FULL_THESIS_NOT_RUN이다.
```

예:

```text
삼성전자 row가 Stage1이면:
  "이번 census 상태판에서 이벤트/근거가 조금 잡혔다"는 뜻이다.

아니다:
  "삼성전자 HBM thesis가 Stage1로 최종 판정됐다"는 뜻이 아니다.
```

## 다음 패치 방향

### P0. 현재 anti-fake layer는 유지

절대 다시 무너뜨리면 안 되는 것:

```text
claim 없는 score 금지
event_evidence_score와 full_e2r_verified_score 혼동 금지
CensusAssessmentEvent를 점수 증거로 사용 금지
Brain/Web artifact 0개인데 Brain/Web pass 금지
Research Brain shadow report를 production cutover evidence로 승격 금지
```

### P1. Production SourceTask 실행 경로를 붙인다

대상은 모든 종목 full thesis가 아니라 먼저 후보 이벤트다.

```text
CandidateEvent
-> SourceTask
-> official-first acquisition
-> EvidenceDocument
-> EvidenceAnchor
-> RawAssertion
-> AdjudicatedClaim
-> EvidenceClaim
```

필수 artifact:

```text
planner_runs.jsonl
llm_prompts.jsonl
llm_responses.jsonl
source_tasks.jsonl
source_task_executions.jsonl
web_search_tasks.jsonl
web_search_results.jsonl
web_fetched_documents.jsonl
web_rejected_documents.jsonl
claim_extractor_runs.jsonl
brain_to_claim_trace.jsonl
evidence_claims.jsonl
```

단, general web은 마지막 fallback이다.

```text
FCF gap -> 먼저 DART/CompanyGuide/IR
계약 gap -> 먼저 DART/KIND/Issuer IR
HBM customer gap -> 회사 IR/고객사 공식/고품질 보도
```

### P2. LLM은 query와 claim extraction에 쓰되, 점수 직접 입력 금지

해야 하는 것:

```text
LLM이 문서에서 assertion을 뽑는다.
코드가 quote/span/date/entity/anchor를 검증한다.
별도 adjudicator가 target/temporal/polarity를 판정한다.
별도 mapper가 primitive 후보를 만든다.
StageCourt는 deterministic하게 결정한다.
```

하지 말아야 하는 것:

```text
LLM에게 "이 종목 몇 점?"을 묻는다.
LLM이 current_score_eligible=true라고 했다는 이유로 점수에 넣는다.
score gap을 extractor prompt에 보여 줘서 원문을 점수 칸에 끼워 맞추게 한다.
```

### P3. Full thesis smoke는 작게, 그러나 진짜로 닫는다

최소 pilot:

```text
삼성전자
SK하이닉스
현재 accepted_claim이 있는 공식 이벤트 row 일부
```

요구:

```text
full_thesis_stage != FULL_THESIS_NOT_RUN
full_e2r_verified_score != null
score_scale == FULL_E2R_100
nonzero ScoreContribution has support_claim_ids
unresolved material gaps -> PENDING, not low score
hard break -> current/direct/source quorum required
```

쉬운 예:

```text
HBM qualification 지연이라는 2024년 과거 기사가 있다.
2026년 Stage에 바로 hard break로 넣으면 안 된다.
후속 자료로 해소/지속/대체 여부를 확인해야 한다.
확인 전이면 hard break가 아니라 follow-up gap이다.
```

### P4. 전 아키타입 replay parity

전 아키타입에 대해 다음을 분리한다.

```text
source-backed fixture: replay 정답으로 사용 가능
source_proxy_only: ontology 참고만 가능
evidence_url_pending: 운영 점수 정답으로 사용 금지
```

완료 조건:

```text
C01~C36 Evidence Contract schema validation
positive fixture replay
guard fixture replay
wrong-subject fixture
historical/superseded fixture
duplicate source family fixture
future leakage fixture
```

## 다음 에이전트에게 던질 공격 질문

1. `evidence_claims.jsonl`의 모든 row가 실제 `document_id`와 `anchor_id`를 갖는가?
2. `evidence_claims.jsonl`과 `accepted_claims.jsonl`의 claim_id set이 같은가?
3. Brain/Web disabled run에서 `brain_web_claim=true`인 row가 하나라도 있는가?
4. `planner_runs/web_search/claim_extractor`가 0인데 Brain/Web pass label이 있는가?
5. Research Brain v4 bridge가 `snapshot://`을 포함하면서 cutover usable이라고 말하는가?
6. `event_evidence_score`를 `verified_score`처럼 표시하는 UI/문서/CSV가 있는가?
7. `full_thesis_stage=FULL_THESIS_NOT_RUN`인데 Stage3/4 운영 설명을 하는 문서가 있는가?
8. `CensusAssessmentEvent`가 candidate_event_ids에 섞여 점수 trigger가 되는가?
9. `score_eligible_candidate_event_count`와 accepted claim/event score count 차이를 설명하는 audit이 있는가?
10. 다음 패치가 old v3 accepted claims를 그대로 full thesis claim으로 승격하지 않는가?

## 최종 판단

현재 상태는 좋아진 부분과 남은 부분이 분명하다.

좋아진 부분:

```text
가짜 full Stage 완료를 막는다.
공식 baseline claim payload를 파일로 드러낸다.
Research Brain v4 기존 보고서가 shadow/import-only임을 readiness에 반영한다.
Brain/Web disabled 상태에서 Brain/Web pass를 주장하지 않는다.
```

남은 부분:

```text
Brain/Web enabled attempt에서는 Research Brain/Web/IR/Report acquisition leaf와 score/stage trace export를 검증해야 한다.
하지만 canonical run은 Brain/Web disabled라서 그 경로를 실제 운영 evidence pass로 실행한 것이 아니다.
LLM claim extractor run artifact가 없다.
full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt trace는 enabled smoke에서 실제 accepted claim이 생길 때만 인정할 수 있으며,
canonical Stage map에는 아직 승격되지 않는다.
전 아키타입 source-backed replay parity가 아직 없다.
```

따라서 다음 패치는 "Stage 숫자를 예쁘게 만드는 패치"가 아니라

```text
CandidateEvent에서 실제 source-backed EvidenceClaim을 만들고,
그 claim으로만 PrimitiveState/ScoreContribution/StageCourt를 돌리는 패치
```

여야 한다.
