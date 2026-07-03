# Census v4 0701 Source Relevance / Trace Chain Patch And Stage Truth

작성일: 2026-07-01  
기준 repo: `/home/eorb915/projects/stock_agent`

최신 우선 문서:

```text
docs/0701/census_v4_0701_subagent_feedback_fixes_and_current_not_ready_truth_2026-07-01.md
```

이 문서는 `/tmp/census_v4_enabled_provider_probe_after_trace_chain_fix` 기준의 이전 forensic 기록이다.  
이후 subagent feedback, `planner_success_limit` 보정, 최신 enabled smoke `/tmp/census_v4_enabled_provider_probe_after_success_limit_fix`, 전체 테스트 4972개 OK는 위 최신 문서를 우선한다.

## 결론

질문은 "뭔가 잘못되고 있는 거 맞지? stage가 있는 애들이 있긴 해?"였다.

짧게 답하면:

```text
Stage label은 있다.
하지만 현재 live Brain/Web 운영 Stage는 없다.
```

최신 smoke 기준 Stage 분포는 아래와 같다.

```text
output root:
/tmp/census_v4_enabled_provider_probe_after_trace_chain_fix

census_stage_status rows: 3391
canonical_stage:
  0:      3306
  1:        54
  2:        30
  3-Red:     1

stage_scope:
  CENSUS_EVENT_BOARD: 3391
  BRAIN_WEB_PARTIAL:     0
  FULL_THESIS:           0

Brain/Web promoted stage rows: 0
Brain/Web accepted claims:     0
```

쉬운 예:

```text
CENSUS_EVENT_BOARD Stage1
= "이 종목은 전체 Census에서 이벤트/상태판상 Stage1로 표시됨"

FULL_THESIS Stage1
= "이 종목의 전체 투자 thesis를 원문 claim으로 채워서 Stage1로 확정함"

현재 삼성전자/하이닉스 같은 Stage1은 전자다.
HBM/C06 full thesis를 끝까지 검증한 운영 Stage가 아니다.
```

따라서 지금 상태를 "Stage 있는 종목이 있으니 운영 파이프라인이 된다"라고 말하면 틀리다.  
정확한 표현은 아래다.

```text
전 종목 상태판은 생성된다.
Event-board partial Stage label도 있다.
하지만 Brain/Web evidence pass와 full thesis 운영 Stage는 아직 NOT_READY다.
```

## 이번에 실제로 고친 문제

이번 패치는 점수나 Stage threshold를 건드리지 않았다.

고친 것은 세 가지다.

### 1. 웹 fetch 후 target relevance guard

파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
```

문제:

```text
검색 결과 title/snippet에는 target이 있어 보여도
실제 본문 fetch 후 target 회사가 안 나오거나 lead에서 target 맥락이 약하면
LLM extractor에 넘겨질 수 있었다.
```

예:

```text
검색 대상: 삼성전자
본문 실제 주체: 월덱스
본문에 삼성전자는 고객사로만 언급
```

이런 문서는 삼성전자 점수 재료가 되면 안 된다.

패치:

```text
fetch 성공 후 EvidenceDocument 생성 전에 target alias를 본문/lead에서 다시 확인한다.
실패하면 web_rejected_documents.jsonl에 남기고 extractor로 보내지 않는다.
```

새 rejection status:

```text
REJECTED_TARGET_RELEVANCE_AFTER_FETCH
```

새 rejection reason 예:

```text
web_fetch_target_not_found_in_full_text
web_fetch_target_not_in_title_snippet_or_lead
web_fetch_target_alias_missing
```

### 2. rejected mapping reason을 claim trace에 보존

파일:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/census/census_runner_v4.py
```

문제:

기존 `brain_claim_mapping_trace.jsonl`에는 대체로 아래처럼만 남았다.

```text
mapping_not_accepted:REJECTED
```

이러면 다음 planner가 무엇을 고쳐야 하는지 모른다.

패치:

```text
primitive_mapping_rejected:<구체 사유>
```

를 trace에 남긴다.

예:

```text
primitive_mapping_rejected:facility_investment_correction_requires_followup_not_positive_capacity
```

쉬운 예:

```text
"신규시설투자 정정신고, 종료일 연장"
```

이건 CAPA 증가 확정이 아니라 "일정 지연/정정"에 가깝다.  
따라서 `capacity_expansion` 점수로 넣으면 안 되고, rejected reason이 다음 planner feedback으로 돌아가야 한다.

추가로 이번 패치에서 accepted claim에 task-level rejection reason이 섞이는 문제도 막았다.

나쁜 상태:

```text
같은 task 안의 claim A는 accepted,
claim B는 rejected.

그런데 A에도 mapping_not_accepted reason이 붙음.
```

수정 후:

```text
accepted claim에는 rejected source_task_not_eligible_reasons를 붙이지 않는다.
rejected claim에만 구체 rejected reason을 보존한다.
```

### 3. Brain Stage promotion trace chain 보정

파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
```

문제:

이전 smoke에서 Brain/Web claim 1개가 accepted되며 Brain Stage row가 승격됐지만, 대표 row에 아래가 비어 있었다.

```text
score_contribution_ids: 있음
primitive_state_ids: 없음
```

이건 운영상 매우 위험하다.

쉬운 예:

```text
"10점이 들어갔다"는 영수증은 있는데
"그 10점이 어느 증거칸에서 왔는지" 장부가 비어 있는 상태
```

패치:

```text
Brain StageCourt trace에 primitive_state_ids를 기록한다.
Brain stage promotion row가 primitive_state_ids를 그대로 복사한다.
brain_to_claim_trace에도 primitive_state_ids를 기록한다.
Brain StageCourt trace가 score_contribution_ids를 들고 있는데 primitive_state_ids가 없으면 promotion audit가 막는다.
```

또 하나의 audit 의미도 바로잡았다.

이전 leaf audit는 아래처럼 동작했다.

```text
brain_to_claim_trace에 census_stage_status_id가 있으면 critical
```

하지만 정상 승격이라면 trace가 어떤 stage row로 들어갔는지 `census_stage_status_id`가 있어야 한다.

수정 후:

```text
census_stage_status_id 자체는 허용
단, 그 id가 실제 stage row에 없거나,
trace의 stagecourt id / claim id가 stage row와 다르면 critical
```

즉 좋은 연결은 통과하고, 끊긴 연결만 실패한다.

## 최신 smoke 명령

```bash
rm -rf /tmp/census_v4_enabled_provider_probe_after_trace_chain_fix && \
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root /tmp/census_v4_enabled_provider_probe_after_trace_chain_fix \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 8 \
  --brain-planner-success-limit 2 \
  --brain-planner-batch-size 2 \
  --brain-max-fetches-per-task 2 \
  --brain-claim-extractor-provider auto \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --fail-on-critical-audit true \
  --write-operational-docs false
```

결과:

```text
exit code: 1
stdout: NOT_READY
```

중요:

```text
이번에는 RuntimeError critical audit failure가 아니다.
leaf_artifact_audit.json: PASS, critical_count=0
primitive_state_chain_audit.json: PASS, critical_count=0
```

즉 "장부가 깨져서 실패"가 아니라 "Brain/Web accepted claim이 아직 없어서 readiness가 막힌" 상태다.

## 최신 smoke 카운트

```text
planner_runs.jsonl:              24
source_tasks.jsonl:             110
source_task_executions.jsonl:   110
web_search_tasks.jsonl:          11
web_search_results.jsonl:       116
web_fetched_documents.jsonl:     17
web_rejected_documents.jsonl:    17
claim_extractor_runs.jsonl:      17
brain_claim_mapping_trace.jsonl: 86
brain_to_claim_trace.jsonl:       0

Brain/Web accepted claims:        0
Brain/Web score contributions:    0
Brain/Web StageCourt traces:      0
Brain/Web promoted rows:          0
```

Planner provider:

```text
real provider success: 4
provider none/failed rows: 20
```

Extractor:

```text
LLM extractor SUCCESS rows: 17
```

Web fetch rejection:

```text
live_pdf_text_extraction_failed:pypdf extraction failed: Stream has ended unexpectedly: 9
live_pdf_text_extraction_failed:pypdf extraction failed: Cannot find Root object in pdf: 5
web_fetch_target_not_in_title_snippet_or_lead: 2
web_fetch_target_not_found_in_full_text: 1
```

Web result selection:

```text
NOT_SELECTED_BUDGET_EXHAUSTED: 82
SELECTED_FOR_FETCH:           31
REJECTED_TARGET_RELEVANCE_AFTER_FETCH: 3
```

Mapping trace:

```text
REJECTED_BEFORE_SCORE: 86
ACCEPTED_FOR_SCORE:     0
```

상위 rejection reason:

```text
target_scope_not_direct:UNRELATED
mapping_not_accepted:REJECTED
semantic_rejected
target_scope_not_allowed:UNRELATED
target_not_direct:NOT_TARGET_SCOPED
primitive_mapping_rejected:adjudication_not_passed
primitive_mapping_rejected:no_allowed_primitive_for_predicate
```

해석:

```text
LLM/search/fetch/extractor는 실제로 돌았다.
하지만 추출된 claim이 target direct/current/contract primitive 조건을 통과하지 못했다.
따라서 점수와 Stage로 들어가지 않는 것이 맞다.
```

## 최신 audit 결과

```text
leaf_artifact_audit.json
  verdict: PASS
  critical_count: 0

primitive_state_chain_audit.json
  verdict: PASS
  critical_count: 0

brain_stage_promotion_audit.json
  verdict: BLOCKED
  blockers:
    - accepted brain claim count is zero
    - brain score contribution count is zero
    - brain StageCourt trace count is zero
  brain_promoted_stage_row_count: 0
  unsafe_promoted_stage_row_count: 0
  brain_trace_promoted_reference_error_count: 0
  brain_stage_trace_missing_primitive_state_ids_count: 0

brain_web_readiness_gate_audit.json
  verdict: BLOCKED
  brain_web_evidence_pass_allowed: false
  blockers:
    - web/LLM accepted claim count is zero
    - Brain/Web StageCourt traces are not promoted into census_stage_status
    - brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED

readiness_verdict.json
  verdict: NOT_READY
```

## 무엇이 좋아졌나

이전 상태:

```text
Brain accepted claim 1개가 생기면
primitive_state_ids 없는 stage row가 승격될 수 있었다.
leaf audit는 critical로 터졌고,
brain_to_claim_trace의 정상/비정상 promoted reference 의미도 헷갈렸다.
```

현재 상태:

```text
accepted claim이 없으면 승격 0개로 BLOCKED.
accepted claim이 있더라도 primitive_state_ids 없이 score contribution만 있으면 promotion audit가 막음.
정상 promoted reference는 허용하고 dangling/mismatched promoted reference만 critical.
leaf artifact audit와 primitive chain audit는 모두 PASS.
```

즉 "안 되는 것을 된다고 말하는 문제"는 더 줄었다.

## 아직 안 되는 것

가장 큰 미완성은 여전히 이것이다.

```text
Brain/Web이 실제 fetched document에서 accepted score claim을 만들지 못한다.
```

현재 `brain_claim_mapping_trace.jsonl` 86개는 전부 rejected다.

주된 패턴:

1. target direct가 아니다.
2. 문서 주체가 target이 아니다.
3. primitive contract에 맞는 allowed primitive가 아니다.
4. 구조화 필드가 positive bridge가 아니라 정정/일정/간접 언급에 가깝다.

쉬운 예:

```text
대상 회사: 삼성전자
본문 주체: 협력사
문장: 삼성전자가 주요 고객사다

이건 "삼성전자 수주/FCF/계약 질" claim이 아니다.
조사 힌트일 수는 있지만 점수 claim은 아니다.
```

현재 파이프라인은 이걸 점수로 넣지 않는다.  
그건 올바르다.

하지만 운영형 파이프라인이라면 여기서 멈추면 안 된다.  
다음 planner가 rejected reason을 보고 더 좋은 source task를 만들어야 한다.

## 다음 패치 방향

다음 패치는 accepted를 억지로 늘리면 안 된다.

나쁜 패치:

```text
if "계약" in text:
    accepted = true

if company == "삼성전자":
    HBM 점수 인정
```

좋은 패치:

```text
rejected mapping trace를 planner feedback으로 넣는다.
LLM planner가 "왜 rejected됐는지"를 보고 다음 source task를 생성한다.
source task는 official-first, bounded budget, target direct 조건을 유지한다.
문서가 들어오면 contract-blind extractor가 claim을 뽑고,
target/temporal/primitive mapper가 통과시킨 claim만 점수에 들어간다.
```

구체적인 다음 순서:

1. `brain_claim_mapping_trace.jsonl`의 top rejection taxonomy를 planner feedback에 더 강하게 넣는다.
2. `target_scope_not_direct:UNRELATED`가 많으면 LLM planner가 target direct source를 우선 찾도록 만든다.
3. `no_allowed_primitive_for_predicate`가 많으면 primitive contract와 extracted predicate 사이의 mapping diagnostics를 늘린다.
4. PDF fetch 실패가 많으면 PDF fallback/provider 전략을 분리한다. 단 PDF 실패를 낮은 점수로 확정하면 안 된다.
5. C06/HBM 같은 known positive URL-backed fixture에서 accepted claim이 최소 1개 생기는 bounded smoke를 만든다.
6. 삼성전자/하이닉스 live full thesis는 event-board와 분리해 `FULL_THESIS_NOT_RUN` 또는 `PENDING_MATERIAL_GAPS`로만 표시한다.

## 교차검증 포인트

다음 에이전트는 아래를 공격하면 된다.

1. `brain_claim_mapping_trace.jsonl` rejected reason이 claim 단위인가, task 단위 reason이 accepted claim에 섞이지 않는가?
2. Brain StageCourt trace에 `score_contribution_ids`가 있으면 반드시 `primitive_state_ids`도 있는가?
3. `brain_to_claim_trace.census_stage_status_id`가 있으면 실제 `census_stage_status` row와 claim/stagecourt id가 맞는가?
4. `REJECTED_TARGET_RELEVANCE_AFTER_FETCH`가 너무 보수적으로 좋은 문서를 버리지는 않는가?
5. 반대로 target이 lead에 없는데 본문 말미에만 스치듯 등장하는 문서가 점수 claim으로 들어가지 않는가?
6. Stage 분포를 보고 `CENSUS_EVENT_BOARD`와 `FULL_THESIS`를 혼동하지 않는가?
7. `leaf_artifact_audit PASS`를 `Brain/Web operating pass`로 오해하지 않는가?

## 테스트

좁은 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_goal_required_audits -v
```

결과:

```text
Ran 22 tests in 13.136s
OK
```

넓은 관련 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_planner_provider \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_provider_failure_pending \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_bundle_export \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_primitive_state_chain \
  tests.test_census_v4_source_task_satisfaction_chain -v
```

결과:

```text
Ran 88 tests in 29.965s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 4968 tests in 156.795s
OK

log:
/tmp/stock_agent_full_tests_after_source_relevance_trace_chain_fix.log
```

## 최종 판정

현재는 좋아진 상태지만 아직 운영 완료가 아니다.

정확한 상태:

```text
Anti-fake / ledger integrity: PASS
Event-board stage labels: 있음
Brain/Web real acquisition/extraction: 실행됨
Brain/Web accepted score claim: 0
Brain/Web promoted Stage: 0
Full thesis operating Stage: 0
Readiness: NOT_READY
```

한 줄로:

> Stage는 있긴 하지만 지금 있는 Stage는 대부분 event-board 상태판이다. 이번 패치는 잘못된 Brain/Web Stage 승격을 막았고, 현재 남은 핵심 병목은 실제 fetched 문서에서 target-direct accepted claim을 만드는 Evidence OS 경로다.
