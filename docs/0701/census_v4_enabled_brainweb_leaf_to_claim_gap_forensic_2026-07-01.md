# Census v4 Enabled Brain/Web Leaf To Claim Gap Forensic - 2026-07-01

이 문서는 다음 에이전트가 바로 강하게 리뷰할 수 있도록 만든 최신 enabled Brain/Web smoke 분석 문서다.

대상 질문:

```text
뭔가 잘못되고 있는 게 맞나?
Stage가 있는 애들이 있긴 한가?
이번에는 웹/LLM을 실제로 돌린 건가?
돌렸다면 왜 아직 Brain/Web Stage로 승격되지 않았나?
다음 패치는 어디를 정확히 닫아야 하나?
```

## 한 줄 결론

웹 검색, 웹 원문 fetch, LLM claim extractor leaf는 실제로 생겼다.

초기 smoke에서는 LLM이 뽑은 web raw assertion이 검증 가능한 `document_id`, `anchor`, `quote`까지 충분히 보존하지 못했다.

추가 anchor/decoder 패치 후에는 Brain/Web raw assertion 46개와 `anchor_verified=True` 46개까지 생겼다. 하지만 아직 `mapping`, `score eligibility`, `accepted claim`, `score contribution`, `StageCourt`, `promoted row`로 이어지지 못했다.

그래서 현재 상태는:

```text
웹/LLM leaf 생성: 성공
Brain/Web raw assertion: 46
Brain/Web anchor_verified raw: 46
Brain/Web accepted claim: 0
Brain/Web score contribution: 0
Brain/Web StageCourt trace: 0
Brain/Web promoted census stage row: 0
최신 verdict: NOT_READY
```

쉬운 예:

```text
책은 빌려 왔다.
LLM이 책을 읽고 메모도 일부 남겼다.
하지만 그 메모가 "몇 페이지의 어떤 문장 때문에 몇 점"이라는 채점지에 아직 붙지 않았다.
따라서 최종 성적표에 반영하면 안 된다.
```

## 검증 입력

실행한 smoke:

```bash
rm -rf /tmp/census_v4_enabled_provider_probe

PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root /tmp/census_v4_enabled_provider_probe \
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

CLI 출력:

```text
NOT_READY
```

해석:

```text
정상적인 실패다.
leaf critical failure는 사라졌지만,
Brain/Web accepted claim -> score -> StageCourt -> promoted row 체인이 아직 닫히지 않았다.
```

## Leaf 산출물 숫자

기준 디렉터리:

```text
/tmp/census_v4_enabled_provider_probe
```

주요 파일 row count:

```text
planner_runs.jsonl:              22
source_tasks.jsonl:              106
source_task_executions.jsonl:    106
web_search_tasks.jsonl:            4
web_search_results.jsonl:         40
web_fetched_documents.jsonl:       6
web_rejected_documents.jsonl:      5
claim_extractor_runs.jsonl:        6
raw_assertions.jsonl:            101
adjudicated_claims.jsonl:        101
accepted_claims.jsonl:            92
score_contributions.jsonl:        92
stagecourt_traces.jsonl:          92
brain_to_claim_trace.jsonl:        0
census_stage_status.jsonl:      3391
```

주의:

```text
accepted_claims=92
score_contributions=92
stagecourt_traces=92
```

이 값은 모두 기존 OpenDART/event-board claim 쪽이다.
웹/LLM accepted claim이 92개라는 뜻이 아니다.

실제 accepted claim의 source provider 분포:

```text
accepted_claims.source_provider:
  OpenDART: 92

accepted_claims.brain_web_origin:
  None: 92
```

즉:

```text
웹/LLM accepted claim: 0
```

## 감사 파일 결과

핵심 감사:

```text
leaf_artifact_audit.json:
  verdict: PASS

web_naver_acquisition_audit.json:
  verdict: REAL_ACQUISITION_PASS
  naver_search_call_count: 4
  web_search_result_count: 40
  web_fetched_document_count: 6
  web_rejected_document_count: 5

llm_claim_extraction_audit.json:
  verdict: REAL_EXTRACTION_PASS
  llm_claim_extractor_attempt_count: 6
  llm_claim_extractor_real_provider_count: 6
  llm_claim_extractor_claimed_but_zero_count: 0

brain_web_readiness_gate_audit.json:
  verdict: BLOCKED
  web_or_llm_accepted_claim_count: 0
  brain_score_contribution_count: 0
  brain_stage_trace_count: 0
  brain_promoted_stage_row_count: 0

brain_stage_promotion_audit.json:
  verdict: BLOCKED
  brain_claim_count: 0
  brain_score_contribution_count: 0
  brain_stage_trace_count: 0

readiness_verdict.json:
  verdict: NOT_READY
  target_gate: brain_web
```

해석:

```text
leaf_artifact_audit PASS
!= Brain/Web 운영 pass

web_naver_acquisition REAL_ACQUISITION_PASS
!= accepted claim pass

llm_claim_extraction REAL_EXTRACTION_PASS
!= score/stage pass

Brain/Web pass는 아직 BLOCKED가 맞다.
```

쉬운 예:

```text
웹 검색 PASS
= 자료실에 가서 자료를 실제로 가져왔다.

LLM extraction PASS
= 자료를 읽는 담당자가 실제로 일했다.

Brain/Web readiness BLOCKED
= 그 담당자의 메모가 아직 공식 채점지에 붙지 않았다.
```

## 이번 패치로 실제로 닫힌 것

이번 패치 전 enabled smoke는 다음 critical로 바로 죽었다.

```text
web_claimed_but_zero_search_count: 1
llm_claim_extractor_claimed_but_zero_count: 1
```

원인:

```text
1. LLM planner에게 "Brain/Web 실행이면 외부 web/news query가 필요하다"는 요구가 충분히 전달되지 않았다.
2. planner가 외부 web source task를 뒤쪽에 냈더라도 max task cap 때문에 잘렸다.
3. live_full_bounded task가 official source에서 멈추고 web fallback leaf를 병합하지 못했다.
4. structured DART 문서만 있는 경우에도 "LLM extractor 0"을 critical로 볼 수 있는 과잉 감사가 있었다.
```

패치된 방향:

```text
1. planner evidence context에 brain_web_acquisition_required를 넣었다.
2. planner prompt에 target-scoped query_intent와 external web source task를 요구했다.
3. planner output이 query_intents_empty 또는 no_external_web_source_task이면 LLM에게 한 번 더 repair 요청한다.
4. source_tasks_from_planner_output_v4가 task cap 안에서도 LLM이 만든 external web task 하나는 보존한다.
5. live_full_bounded에서 official-first를 유지하되, LLM이 요청한 external web task는 web fallback leaf까지 병합한다.
6. llm_claim_extractor_claimed_but_zero_count는 unstructured Brain document가 있을 때만 critical로 본다.
```

수정된 주요 코드 위치:

```text
src/e2r/research_brain/v4_planner_runtime.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/census/census_v4_auditor.py
tests/test_research_brain_v4_operational_modes.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_census_v4_run_mode_honesty.py
```

중요:

```text
이번 패치는 웹/LLM leaf가 0개인 거짓 Brain/Web 실행을 막고,
실제 leaf를 만들도록 한 패치다.

아직 LLM web assertion을 accepted claim과 Stage로 승격하는 패치가 아니다.
```

## 초기 smoke에서 막힌 위치

초기 `/tmp/census_v4_enabled_provider_probe` 체인은 여기까지 왔다.

```text
LLM planner
  -> source task
  -> bounded web search
  -> web result
  -> full-source fetch
  -> LLM claim extractor run
  -> raw assertion 일부 생성
```

초기 smoke는 여기서 끊겼다.

```text
LLM raw assertion
  - document_id 없음
  - anchor_id 없음
  - source_provider 없음
  - quote_text 없음
  - adjudication 없음
  - primitive mapping 없음
  - score_eligible 없음
```

초기 smoke의 brain_web raw assertion 예:

```text
raw_assertion_id: RAWASSERTV4-...
brain_web_origin: research_brain_v4_attempt
claim_id: null
document_id: null
quote_text: null
mapping_status: null
primitive_id: null
```

초기 smoke의 adjudicated_claims 쪽에서는 claim_id가 일부 생기지만, 여전히 핵심 필드가 비어 있었다.

```text
claim_id: CLM-...
document_id: null
quote_text: null
mapping: null
adjudication: null
```

그래서 deterministic guard가 accepted claim으로 올리지 않는 것이 맞았다.

쉬운 예:

```text
"대웅제약 관련 설비투자 내용이 있음"이라는 메모만 있고,
"어느 URL의 어느 문장인지"가 비어 있으면 점수에 넣으면 안 된다.
```

## 최신 after-decoder smoke에서 막힌 위치

추가 패치 후 `/tmp/census_v4_enabled_provider_probe_after_decoder_patch`에서는 위 문제의 일부가 해소됐다.

최신 체인:

```text
LLM planner
  -> source task
  -> bounded web search
  -> web result
  -> full-source fetch
  -> LLM claim extractor run
  -> raw assertion
  -> adjudicated claim
```

최신 개선:

```text
Brain/Web raw assertion: 46
Brain/Web raw anchor_verified=True: 46
LLM raw assertion: 38
structured API raw assertion: 8
```

최신 병목:

```text
Brain/Web accepted claim: 0
Brain/Web score contribution: 0
Brain/Web StageCourt trace: 0
brain_to_claim_trace: 0
```

특히 Brain/Web adjudicated claim은 `source_document_id/source_anchor_id`를 보존하지만, top-level `document_id/source_provider`가 null인 row가 남아 있다. 아직 accepted claim이 아니므로 점수 누수는 아니지만, 다음 cutover 전에 claim trace 표준화가 필요하다.

현재 rejected 요약은 `source_task_executions.not_eligible_reasons`에만 짧게 남는다.

```text
mapping_not_accepted:REJECTED
semantic_rejected
target_scope_not_allowed:UNRELATED
target_not_direct:NOT_TARGET_SCOPED
```

따라서 다음 패치의 첫 단계는 점수를 올리는 것이 아니라 `brain_claim_mapping_trace.jsonl` 같은 rejected claim/mapping rationale leaf를 만드는 것이다.

## Stage가 있는 애들이 있긴 한가

있다.

하지만 현재 canonical output의 Stage는 전부 event-board scope다.

기존 canonical 기준:

```text
census_stage_status.jsonl rows: 3391

canonical_stage:
  0: 3306
  1: 54
  2: 30
  3-Red: 1

stage_scope:
  CENSUS_EVENT_BOARD: 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391
```

따라서 정확한 답:

```text
Stage label이 붙은 row는 있다.
Full thesis operating Stage가 끝난 row는 없다.
Brain/Web promoted Stage row도 현재 enabled smoke에서는 0개다.
```

쉬운 예:

```text
출석부에는 "대기", "추가 검사 필요" 같은 상태가 붙어 있다.
하지만 최종 진단서가 나온 환자는 아직 없다.
```

## 왜 이 상태를 완료라고 말하면 안 되나

다음 네 문장은 모두 틀린 말이다.

```text
웹/LLM을 돌렸으니 Brain/Web pass다.
accepted_claims가 92개 있으니 웹 claim도 accepted됐다.
StageCourt trace가 92개 있으니 Brain/Web StageCourt도 됐다.
leaf_artifact_audit PASS니까 goal 완료다.
```

정확한 문장:

```text
웹/LLM leaf는 실제로 생겼다.
하지만 웹/LLM accepted claim은 0개다.
StageCourt trace 92개는 기존 OpenDART event-board trace다.
Brain/Web readiness는 BLOCKED다.
goal completion은 false가 맞다.
```

## 다음 패치 순서

### P0. LLM raw assertion에 source anchor를 붙인다

필수 필드:

```text
extractor_run_id
document_id
anchor_id
source_task_id
candidate_event_id
symbol
company_name
source_provider
quote_text 또는 anchor locator
```

원칙:

```text
LLM이 quote를 말해도 코드가 원문 span/hash로 검증해야 한다.
검증 안 되면 rejected claim으로 남긴다.
```

### P1. raw assertion을 Evidence OS adjudication/mapping으로 통과시킨다

필수 단계:

```text
raw assertion
  -> target/temporal adjudication
  -> primitive mapping
  -> score eligibility derivation
  -> accepted 또는 rejected claim
```

금지:

```text
LLM 출력의 "score_eligible=true" 같은 값을 그대로 믿기
document_id 없는 claim을 accepted로 올리기
quote 없는 unstructured claim을 점수에 넣기
```

### P2. brain_to_claim_trace를 만든다

필수 trace:

```text
source_task_execution_id
web_search_task_id
web_fetched_document_id
claim_extractor_run_id
raw_assertion_id
accepted_or_rejected_claim_id
score_contribution_id
stagecourt_trace_id
promoted_census_stage_row_id
```

이 trace가 없으면 다음 에이전트가 다시 같은 질문을 하게 된다.

```text
"이 점수는 어느 웹 문서의 어느 claim에서 왔어?"
```

### P3. score contribution은 accepted Brain claim만 사용한다

조건:

```text
accepted=true
score_eligible=true
direct target
current/as_of valid
valid anchor
accepted primitive mapping
```

그때만:

```text
Brain/Web score contribution 생성
Brain/Web StageCourt trace 생성
strict promotion 검토
```

### P4. strict promotion은 마지막에만 한다

promotion 조건:

```text
Brain/Web accepted claim > 0
Brain/Web score contribution > 0
Brain/Web StageCourt trace > 0
brain_to_claim_trace > 0
promoted census row가 같은 trace id를 참조
snapshot/fake/provider-failure leakage 0
```

이 조건 전에는 `NOT_READY`가 맞다.

### P5. 삼성전자/하이닉스 full thesis smoke는 별도다

현재 daily event-board와 C06/HBM full thesis는 다른 일이다.

```text
005930 삼성전자 daily event score 4.0
!= 삼성전자 HBM/C06 full thesis score

000660 SK하이닉스 daily event score 4.0
!= SK하이닉스 HBM/C06 full thesis score
```

full thesis smoke는 다음을 실제 실행해야 한다.

```text
C06/HBM source tasks
official/customer/IR/report/news source acquisition
claim-backed primitive states
score contribution ledger
StageCourt
score_valid_status
```

## 다음 테스트로 고정해야 할 것

추가 또는 강화할 테스트:

```text
1. LLM extractor raw assertion은 document_id와 anchor_id 없으면 accepted 불가
2. LLM extractor raw assertion의 quote가 원문에 없으면 rejected
3. LLM extractor가 raw_assertion_id를 중복 반환해도 claim이 증식하지 않음
4. web raw assertion -> accepted claim -> score contribution -> StageCourt trace가 같은 ID 체인으로 이어짐
5. web raw assertion이 0개인 extractor SUCCESS는 readiness pass가 아님
6. accepted_claims=OpenDART only이면 Brain/Web accepted claim count는 0으로 남음
7. web_naver_acquisition REAL_ACQUISITION_PASS만으로 brain_web target gate가 pass되지 않음
8. llm_claim_extraction REAL_EXTRACTION_PASS만으로 brain_web target gate가 pass되지 않음
9. strict promotion은 brain_to_claim_trace가 없으면 불가
10. promoted census row는 source_task_execution/document/anchor/claim/contribution/stagecourt를 모두 역추적 가능해야 함
```

## 이번 교차검증에서 실행한 테스트

관련 targeted test:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_provider_failure_pending \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_bundle_export -v
```

결과:

```text
Ran 59 tests in 31.938s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 4959 tests in 156.646s
OK
```

주의:

```text
테스트 OK
!= Brain/Web 운영 완료

현재 테스트 OK는 "완료인 척하지 않는 guard가 유지된다"는 증거다.
```

## 다음 에이전트 공격 질문

다음 에이전트는 이 질문부터 던지면 된다.

```text
1. web_fetched_documents 6개 중 어느 문서가 어느 raw assertion으로 연결됐나?
2. 그 raw assertion은 document_id/anchor_id/quote를 갖고 있나?
3. accepted_claims 92개 중 brain_web_origin이 있는 claim이 하나라도 있나?
4. score_contributions 92개 중 brain_web_origin 또는 web source family가 있는 것이 있나?
5. brain_to_claim_trace가 왜 0인가?
6. StageCourt trace 92개는 OpenDART event-board trace 아닌가?
7. `REAL_EXTRACTION_PASS`가 accepted claim pass로 오해될 여지가 없는가?
8. `leaf_artifact_audit PASS`가 goal 완료로 오해될 여지가 없는가?
9. 삼성전자/하이닉스 full thesis와 daily event-board가 출력에서 완전히 분리되어 있는가?
10. 다음 패치가 LLM raw assertion을 하드코딩 parser로 우회하지 않고 Evidence OS adjudication으로 넘기는가?
```

## 최종 판정

이번 상태는 나빠진 것이 아니라, 더 정확하게 드러난 것이다.

닫힌 것:

```text
Brain/Web enabled라고 말하면서 web/search/fetch/extractor leaf가 0개인 거짓 실행
```

아직 남은 것:

```text
web/LLM raw assertion을 accepted claim, score contribution, StageCourt, promoted stage row로 연결하는 Evidence OS bridge
```

따라서 현재 올바른 label은:

```text
BRAIN_WEB_LEAFS_REAL_BUT_NOT_CUTOVER_READY
```

완료 label은 아직 금지:

```text
BRAIN_WEB_EVIDENCE_PASS
MEANINGFUL_OPERATIONAL_STAGE_PASS
FULL_THESIS_SMOKE_PASS
GOAL_COMPLETION_READY
```

## 2026-07-01 추가 패치: 웹 anchor와 LLM decoder 정리

위 분석 뒤 다음 최소 패치를 추가했다.

수정 목적:

```text
웹 원문 fetch가 성공했는데 TEXT_SPAN anchor가 char:not-found가 되는 문제를 줄인다.
LLM extractor가 exact_quote 대신 quote_text/quote 같은 alias를 쓰면 검증 가능한 quote로 받아들인다.
빈 quote 또는 같은 raw id 반복은 raw assertion 후보로 세지 않는다.
Brain raw assertion export에 document_id/source_document_id/source_anchor_id/source_url/source_provider/anchor_verified를 붙인다.
```

수정 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/production/claim_extraction/anchor_validator.py
src/e2r/production/claim_extraction/extractor_provider.py
src/e2r/census/census_runner_v4.py
tests/test_cutover_v2_quote_anchor_validation.py
tests/test_cutover_contract_blind_extraction.py
tests/test_census_v4_brain_bundle_export.py
```

쉬운 예:

```text
원문:
  Target issuer reached full
     capacity before peers.

LLM quote:
  Target issuer reached full capacity before peers.

패치 전:
  줄바꿈/공백 차이 때문에 quote_not_found 또는 anchor_not_verified가 될 수 있음.

패치 후:
  정규화된 공백 기준으로도 같은 문장이면 quote_span_verified_normalized_whitespace로 인정.
```

단, 이 패치는 점수를 억지로 올리지 않는다.

```text
quote/anchor가 검증되어도,
대상 회사가 아니거나,
primitive mapping이 맞지 않거나,
해당 task의 점수 칸과 맞지 않으면 accepted claim은 여전히 0이다.
```

## 추가 패치 후 enabled smoke

재실행 디렉터리:

```text
/tmp/census_v4_enabled_provider_probe_after_decoder_patch
```

row count:

```text
planner_runs.jsonl:              22
source_task_executions.jsonl:    106
web_search_tasks.jsonl:            6
web_search_results.jsonl:         60
web_fetched_documents.jsonl:       8
web_rejected_documents.jsonl:      4
claim_extractor_runs.jsonl:        8
raw_assertions.jsonl:            138
adjudicated_claims.jsonl:        138
accepted_claims.jsonl:            92
score_contributions.jsonl:        92
brain_to_claim_trace.jsonl:        0
stagecourt_traces.jsonl:          92
```

개선된 점:

```text
LLM extractor run: 8
LLM raw assertion accepted into raw_assertions.jsonl: 38
Brain/Web raw assertion total: 46
Brain/Web raw anchor_verified=True: 46
빈 quote/중복 raw id 반복은 decoder에서 줄어듦
```

아직 막힌 점:

```text
Brain/Web accepted claim: 0
Brain/Web score contribution: 0
Brain/Web StageCourt trace: 0
Brain/Web promoted census row: 0
readiness_verdict: NOT_READY
```

현재 blockers:

```text
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
```

이번에는 blocker 의미가 이전보다 더 좁고 정확하다.

```text
이전:
  웹/LLM raw가 quote/anchor 문제로 Evidence OS 앞단에서 제대로 못 남음.

현재:
  웹/LLM raw와 adjudicated claim은 남음.
  하지만 실제 task primitive와 맞는 accepted mapping이 없어 점수에는 안 들어감.
```

쉬운 예:

```text
이제 메모지에는 "어느 문서의 어느 문장"이 붙었다.
하지만 그 문장이 이번 시험 문제의 답은 아니라서 점수는 0이다.
```

추가 targeted 검증:

```text
Ran 78 tests in 32.170s
OK
```

다음 패치 우선순위:

```text
1. rejected Brain/Web claim도 mapping rationale을 leaf로 남긴다.
2. planner source task의 primitive_gap과 LLM이 실제로 찾은 claim predicate가 어긋날 때, accepted로 우기지 말고 follow-up planner feedback으로 되돌린다.
3. positive source-backed web claim이 존재하는 fixture/live smoke에서 accepted claim -> score contribution -> StageCourt trace -> strict promotion까지 닫히는지를 검증한다.
4. 삼성전자/하이닉스 full thesis smoke는 daily event-board와 별도로 실행해야 한다.
```

## 추가 패치 2: rejected mapping trace leaf

위 우선순위 1번은 코드와 테스트로 반영했다.

새 leaf:

```text
brain_claim_mapping_trace.jsonl
```

재실행 디렉터리:

```text
/tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch
```

최신 row count:

```text
planner_runs.jsonl:              22
source_task_executions.jsonl:    106
web_search_tasks.jsonl:            4
web_search_results.jsonl:         40
web_fetched_documents.jsonl:       8
web_rejected_documents.jsonl:      3
claim_extractor_runs.jsonl:        8
raw_assertions.jsonl:            146
adjudicated_claims.jsonl:        146
brain_claim_mapping_trace.jsonl:  54
accepted_claims.jsonl:            92
score_contributions.jsonl:        92
stagecourt_traces.jsonl:          92
brain_to_claim_trace.jsonl:        0
```

Brain/Web trace 분해:

```text
Brain/Web raw assertions: 54
Brain/Web adjudicated claims with document_id: 54 / 54
Brain/Web adjudicated claims with anchor_id:   54 / 54
Brain/Web accepted claims: 0

brain_claim_mapping_trace:
  REJECTED_BEFORE_SCORE: 54
  mapping_status=REJECTED: 54
```

대표 rejection:

```text
target_scope_not_direct:UNRELATED;mapping_not_accepted:REJECTED: 35
mapping_not_accepted:REJECTED: 19
```

쉬운 예:

```text
이전에는 "메모가 성적표에 왜 안 붙었는지"가 요약만 있었다.
이제는 각 메모마다 어느 문서, 어느 문장, 어느 primitive_gap, 어떤 mapping_status 때문에 탈락했는지 볼 수 있다.
```

새 테스트:

```text
tests.test_census_v4_brain_bundle_export
tests.test_census_v4_artifact_manifest
tests.test_census_v4_goal_required_audits
```

관련 targeted 검증:

```text
Ran 79 tests in 30.586s
OK
```

남은 다음 단계:

```text
1. `brain_claim_mapping_trace.jsonl`의 rejected reason을 LLM planner feedback으로 되돌린다.
2. positive source-backed fixture/live smoke에서 accepted claim -> score -> StageCourt -> promoted row 체인을 닫는다.
3. 삼성전자/하이닉스 full thesis smoke는 daily event-board와 별도 실행한다.
```
