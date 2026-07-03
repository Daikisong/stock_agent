# Census v4 0701 SourceQuality v21 Stage Existence Deep Audit / Patch Direction

작성일: 2026-07-02 KST

대상 산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21
```

## 1. 직접 답

```text
Stage가 있는 애들은 있다.
하지만 운영 FULL_THESIS Stage가 있는 애들은 없다.
```

정확한 숫자:

```text
census_stage_status row = 3391
base_stage row = 3391
non-Stage0 event-board row = 85

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391
  BRAIN_WEB_PARTIAL = 0
  FULL_THESIS = 0

base_stage_distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

verified_score rows = 0
full_e2r_verified_score rows = 0
full_thesis_verified_score rows = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3391
```

쉬운 예:

```text
현재 v21은 전교생 출석부에는 "정상 / 관심 / 추가확인 / 리스크 검토" 메모가 붙었다.
하지만 정식 100점 성적표는 아직 한 장도 나오지 않았다.

Stage1/Stage2-Watch/Red가 보이는 85개는 "상태판에서 더 볼 후보"다.
운영 Green/Yellow/Red thesis가 완성된 종목이 아니다.
```

## 2. 결론을 내린 원장 파일

반드시 아래 leaf artifact를 직접 열어 검산한다.

```text
census_stage_status.jsonl
leaf_artifact_audit.json
readiness_verdict.json
brain_web_readiness_gate_audit.json
brain_stage_promotion_audit.json
full_thesis_production_audit.json
full_thesis_production_runner_audit.json
goal_completion_audit.json
goal_requirement_matrix_audit.json
stagecourt_traces.jsonl
accepted_claims.jsonl
score_contributions.jsonl
source_task_executions.jsonl
web_fetched_documents.jsonl
raw_assertion_rejections.jsonl
```

검산 명령 예:

```bash
python - <<'PY'
import json, collections
from pathlib import Path
root=Path('output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21')
rows=[json.loads(l) for l in (root/'census_stage_status.jsonl').read_text().splitlines() if l.strip()]
for key in ['stage_scope','base_stage','score_scope','operator_stage_use','operator_score_use']:
    print(key, dict(collections.Counter(str(r.get(key)) for r in rows)))
print('verified_score rows', sum(1 for r in rows if r.get('verified_score') is not None))
print('full_e2r_verified_score rows', sum(1 for r in rows if r.get('full_e2r_verified_score') is not None))
PY
```

## 3. 왜 Stage처럼 보이는 값이 생겼나

코드 경로:

```text
src/e2r/census/atomic_stage_decision.py
  build_atomic_stage_decisions()
    -> stage_scope = CENSUS_EVENT_BOARD 고정
    -> score_scale = EVENT_WEIGHTED_PARTIAL 또는 NO_SCORE
    -> full_e2r_verified_score = None

src/e2r/census/census_runner_v4.py
  _atomic_decisions_from_v3()
    -> v3 leaf StageCourt trace를 AtomicStageDecision으로 변환

  _stage_rows_from_v3()
    -> CensusStageStatus row 생성
    -> verified_score = None
    -> full_thesis_stage = FULL_THESIS_NOT_RUN
    -> full_thesis_verified_score = None

  _apply_operator_scope_aliases()
    -> stage_scope != FULL_THESIS이면 operator_stage_use = NOT_FULL_THESIS_STAGE
    -> score_scope != FULL_E2R_100이면 operator_score_use = NOT_FULL_E2R_SCORE
```

즉 v21의 `Stage1`, `Stage2-Watch`, `Red`는 `CENSUS_EVENT_BOARD` 상태판 label이다.

추가 코드 검산:

```text
atomic_stage_decisions.jsonl:
  representative event-board atomic decision이 census_stage_status로 복사된다.
  Stage2-Watch atomic decision 37개는 PENDING_MATERIAL_GAPS 성격이다.
  Red atomic decision 1개는 030350의 current direct official risk disclosure다.

census_stage_status.jsonl:
  representative 선택 후 non-Stage0는 85개다.
  Stage2-Watch는 30개만 대표 row로 남는다.
```

쉬운 예:

```text
DART에 공급계약 공시가 있다.
  -> event-board Stage2-Watch까지는 가능하다.

그 공시가 EPS/FCF, 반복 매출, 현금흐름, source quorum까지 닫았다.
  -> 그때만 FULL_THESIS 후보가 된다.
```

## 4. 예시 5개

### 000660 SK하이닉스

```text
base_stage = Stage1
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
verified_score = null
full_e2r_verified_score = null
full_thesis_stage = FULL_THESIS_NOT_RUN
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
accepted_claim_count = 1
accepted_official_claim_count = 1
```

해석:

```text
이건 SK하이닉스 C06/HBM full thesis 결과가 아니다.
최근 공식 이벤트 1개가 있는 상태판 Stage1이다.
```

### 005930 삼성전자

```text
base_stage = Stage1
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
verified_score = null
full_e2r_verified_score = null
full_thesis_stage = FULL_THESIS_NOT_RUN
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
accepted_claim_count = 1
accepted_official_claim_count = 1
```

해석:

```text
이것도 삼성전자 C06/HBM 점수나 Stage가 아니다.
일일 DART/event-board row다.
```

### 001470 삼부토건

```text
base_stage = Stage2-Watch
stage_scope = CENSUS_EVENT_BOARD
stage_decision_status = PENDING_MATERIAL_GAPS
investigation_status = PENDING
event_evidence_score = 4.4
verified_score = null
full_thesis_stage = FULL_THESIS_NOT_RUN
next_actions = RECHECK_SOURCE, FULL_THESIS_REFRESH
```

해석:

```text
공식 material claim은 보이나 repeat evidence / cash bridge / source quorum이 비어 있다.
운영 Yellow/Green이 아니라 source 재확인 후보다.
```

### 030350 드래곤플라이

```text
base_stage = Red
canonical_stage = 3-Red
stage_scope = CENSUS_EVENT_BOARD
stage_decision_status = RISK_REVIEW
event_evidence_score = 4.0
verified_score = null
full_thesis_stage = FULL_THESIS_NOT_RUN
```

해석:

```text
이건 current direct risk review 상태판이다.
기존 thesis가 깨진 4C 전이와 혼동하면 안 된다.
```

### 114450 그린생명과학

대표 event-board row:

```text
base_stage = Stage2-Watch
stage_scope = CENSUS_EVENT_BOARD
event_evidence_score = 4.4
accepted_claim_count = 1
accepted_official_claim_count = 1
full_thesis_stage = FULL_THESIS_NOT_RUN
```

Brain attempt 내부 trace:

```text
stagecourt_trace_id = SCT-BRAIN-b98459cf5cb30412b266
source_origin = research_brain_v4_attempt
accepted_claim_ids = 24
source_provider = OpenDART
score_interval = 42.0 ~ 42.0
base_stage = 1
not_promoted_to_census_stage_status = true
```

해석:

```text
OpenDART 공식 claim은 실제로 생겼다.
하지만 web/LLM accepted claim은 0개라 BRAIN_WEB_PARTIAL로 승격되지 않았다.
또 margin/cash/repeat/source quorum이 닫히지 않아 FULL_THESIS도 아니다.
```

## 5. Brain/Web이 왜 막혔나

`brain_web_readiness_gate_audit.json`:

```text
verdict = BLOCKED

blockers:
  web/LLM accepted claim count is zero
  Brain/Web StageCourt traces are not promoted into census_stage_status
  brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
  planner runs 21/30
  web search tasks 2/20
  web/news search calls 2/20
  fetched documents 1/10
  claim extractor attempts 1/10
  web/LLM accepted claims 0/3
```

`brain_stage_promotion_audit.json`:

```text
brain_claim_count = 24
official_accepted_claim_count = 24
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0

blockers:
  web/LLM accepted brain claim count is zero for BRAIN_WEB_PARTIAL promotion
  brain StageCourt traces have no web/LLM accepted claim support: 1
```

쉬운 예:

```text
공식 DART 서류는 접수됐다.
하지만 "웹/LLM이 추가 빈칸을 실제로 메웠다"는 서류는 0장이다.
그래서 Brain/Web 성공 도장을 찍지 않는다.
```

중요한 코드상 사실:

```text
Brain StageCourt trace가 stagecourt_traces.jsonl에 있어도
자동으로 census_stage_status.jsonl에 들어가지 않는다.

_promote_brain_stage_rows()는 strict mode에서
web_or_llm_accepted_claim_ids와 교집합이 있는 trace만 BRAIN_WEB_PARTIAL로 올린다.

v21의 SCT-BRAIN trace는 accepted_claim 24개를 갖지만,
그 24개가 모두 OpenDART official claim이라 web/LLM accepted 교집합이 0개다.
따라서 not_promoted_to_census_stage_status=true가 맞다.
```

## 6. Web/LLM 시도는 왜 accepted 0개인가

v21의 직접 원인은 "웹 fetch 실패"가 아니다. 웹 문서 1개는 fetch됐고, LLM extractor도 RAWLLM 12개를 뽑았다.
문제는 그 12개가 모두 score eligibility에서 탈락한 것이다.

v21의 실제 web fetch:

```text
symbol = 114450
provider = NaverFreeSearchProvider
query = 그린생명과학 114450 2026 단일판매 공급계약 정정 계약금액 매출액 계약기간
fetched URL = https://www.digitaltoday.co.kr/news/articleView.html?idxno=665445
title = 그린생명과학, AI반도체 소재 공급계약 체결
claim_extractor_runs = 1
raw_assertion_count = 12
accepted_claim_ids = []
```

대표 탈락 사유:

```text
source_task_provider_error_score_block:general_search_not_score_source
source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider
primitive_mapping_rejected:no_allowed_primitive_for_predicate
target_scope_not_allowed:UNRELATED
target_not_direct:NOT_TARGET_SCOPED
```

해석:

```text
LLM이 문서를 읽기는 했다.
하지만 그 문서는 현재 trusted news score source가 아니고,
일부 assertion은 대상회사 직접 claim도 아니며,
점수 primitive에 맞게 accepted되지 않았다.
그래서 score claim은 0개가 맞다.
```

더 구체적인 실패 구조:

```text
T6 task primitive_gap = cost_overrun
실행 query 2개 = 계약금액/매출액/계약기간, 납품 일정/상대방
실제로 필요한 cost_overrun query = "공급계약 정정 지연 해지 원가 부담 뉴스 2026"
하지만 max_queries=2라 세 번째 query가 실행되지 않았다.

즉 "원가 부담을 찾아와"라는 task가
"계약 규모 기사"를 먼저 읽고 끝났다.
```

코드상 의심 지점:

```text
src/e2r/research_brain/v4_planner_runtime.py
  source_task_drafts에 task별 query_intents를 보존하지 못하고
  global query_intents가 모든 task에 복사되는 경로가 있다.

src/e2r/research_brain/v4_production_orchestrator.py
  이벤트 전체에서 official direct accepted가 생기면
  실패한 external web/LLM task의 rejection feedback이 다음 planner retry로 충분히 돌아가지 않는다.

src/e2r/research_brain/v4_evidence_extraction_bridge.py
  general_search_not_score_source와 IndustryMedia provider mismatch가 붙어
  full fetched article과 search snippet을 충분히 분리하지 못한다.
```

## 7. FULL_THESIS가 왜 0개인가

`full_thesis_production_audit.json`:

```text
verdict = PENDING_FULL_THESIS_PRODUCTION
production_pass_allowed = false
production_full_thesis_row_count = 0
blocker = production_full_thesis_runner_no_eligible_rows
```

`full_thesis_production_runner_audit.json`:

```text
verdict = PENDING_PRODUCTION_FULL_THESIS
candidate_row_count = 0
promoted_full_thesis_row_count = 0
blocked_candidate_count = 0
```

구조상 원인:

```text
_apply_production_full_thesis_from_brain()
  candidates =
    stage_rows where
      stage_scope == BRAIN_WEB_PARTIAL
      and stage_source == research_brain_v4_attempt

v21:
  BRAIN_WEB_PARTIAL row = 0
  therefore candidate_row_count = 0
```

중요한 설계 이슈:

```text
공식 DART/CompanyGuide/IR만으로도 특정 thesis가 닫힐 수 있다.
그런데 현재 production full thesis runner는 BRAIN_WEB_PARTIAL row만 후보로 본다.

따라서 official-only complete thesis 경로와 BRAIN_WEB_EVIDENCE_PASS gate를 분리해야 한다.
```

쉬운 예:

```text
공식 공시와 IR만으로 계약금액, 기간, 매출 반영, 현금흐름까지 모두 닫혔다.
이 경우 full thesis가 될 수 있어야 한다.

하지만 "웹/LLM accepted claim이 0개"라서 Brain/Web evidence pass라고 부르면 안 된다.
둘은 별도 gate다.
```

## 8. 지금 잘못되고 있는 부분과 잘 되고 있는 부분

잘 되고 있는 부분:

```text
1. CensusAssessmentEvent를 score evidence로 쓰지 않는다.
2. Stage/score scope alias가 붙어 event-board와 full-thesis를 구분한다.
3. NEWS를 general search provider 경유 score source로 쓰지 않는다.
4. fake KIND path를 official KIND로 승격하지 않는다.
5. v12의 가짜 BRAIN_WEB_PARTIAL 승격이 v21에서 다시 0개로 막혔다.
```

잘못되었거나 아직 미완성인 부분:

```text
1. 운영 FULL_THESIS row가 0개다.
2. full thesis production runner가 BRAIN_WEB_PARTIAL 후보만 스캔한다.
3. official-only complete thesis가 생겨도 FULL_THESIS 후보가 되기 어렵다.
4. web/LLM accepted claim이 0개라 Brain/Web evidence pass를 주장할 수 없다.
5. Naver가 KIND/DART 공식 URL을 찾았을 때 상세 공식 본문으로 resolve하는 경로가 약하다.
6. primitive_mapping_rejected feedback이 다음 planner query를 충분히 바꾸지 못한다.
7. v21 diagnostic 자체는 intentionally small run이라 Brain/Web operational minimum 30/20/10을 충족하지 않는다.
```

## 9. 다음 P0 패치 방향

### P0-A. FULL_THESIS candidate scan을 BRAIN_WEB_PARTIAL 의존에서 분리

현재:

```text
BRAIN_WEB_PARTIAL row가 있어야 FULL_THESIS 후보가 된다.
```

목표:

```text
StageCourt trace 자체를 후보로 본다.
단, FULL_THESIS 승격은 아래를 모두 요구한다.

- source_origin = research_brain_v4_attempt 또는 production full thesis runner
- real planner/provider identity
- live official/source task execution
- accepted claims direct/current/score_eligible
- score_contribution_ids 존재
- primitive_state_ids 존재
- evidence contract green/yellow gate coverage
- source quorum
- score_status FINAL 또는 FINAL_WITH_NONMATERIAL_GAPS
- score_scale FULL_E2R_100로 재계산 가능
```

주의:

```text
official-only complete thesis는 FULL_THESIS가 될 수 있다.
하지만 BRAIN_WEB_EVIDENCE_PASS는 web/LLM accepted claim minimum을 따로 만족해야 한다.
```

구현 시 금지/허용 구분:

```text
금지:
  OpenDART 공식 claim 24개가 있으니 BRAIN_WEB_PARTIAL로 올린다.
  -> Brain/Web gate를 가짜 통과시킨다.

허용:
  OpenDART 공식 claim 24개가 있으니 FULL_THESIS 후보 심사 대상으로 넣는다.
  -> 단 FULL_THESIS 통과는 green/yellow primitive, score contribution,
     source quorum, final score interval, live task chain을 모두 다시 검사해야 한다.
```

### P0-B. KIND/DART detail resolver

현재 v21 web result에는 KIND 공식 URL도 보인다.

```text
https://kind.krx.co.kr/common/disclsviewer.do?method=search&acptno=20260630001605
```

목표:

```text
Naver result가 exact official hostname이면:
  Naver 문서를 score source로 쓰지 않는다.
  KIND/DART 공식 resolver로 넘긴다.
  상세 본문, 첨부, DART 원문, acptno/rcpNo를 resolve한다.
  resolve 실패 시 official_detail_resolve_failed로 남긴다.
```

쉬운 예:

```text
네이버가 "KIND 공시 링크"를 찾아 줬다.
점수 근거는 네이버 검색 결과가 아니라 KIND 공시 상세본문이어야 한다.
```

2026-07-02 부분 패치 결과:

```text
patched:
  src/e2r/research_brain/v4_source_acquisition_runner.py
  tests/test_research_brain_v4_real_source_acquisition.py

implemented:
  1. exact official hostname 기준으로 KIND/DART official detail route 감지
  2. resolved official URL은 EvidenceDocument.source_name = KIND 또는 DART, source_type = FILING
  3. web_search_results/web_fetched_documents에 official_detail_resolution_required/status/id 기록
  4. official URL fetch 실패는 official_detail_resolve_failed로 web_rejected_documents에 기록
  5. fake path에 kind.krx.co.kr 문자열이 있어도 official route로 승격하지 않음

not proven yet:
  1. latest v23 live artifact는 이 P0-B 패치 전 산출물이다.
  2. 다음 live diagnostic에서 official_detail_resolution_* leaf field가 실제로 생기는지 확인해야 한다.
```

### P0-C. rejected primitive feedback loop

현재 반복되는 탈락:

```text
primitive_mapping_rejected:no_allowed_primitive_for_predicate
source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider
target_scope_not_allowed:UNRELATED
```

목표:

```text
planner feedback에 아래를 구조화해서 넣는다.

- rejected predicate
- rejected primitive_gap
- target/directness failure
- provider/source-class failure
- already fetched URL/domain
- next acceptable source classes
- next missing bridge primitive
```

쉬운 예:

```text
"계약 기사"는 읽었지만 margin bridge가 없었다.
다음 query는 또 "계약 기사"가 아니라
IR/실적발표/사업보고서/CompanyGuide에서 매출총이익률, 영업이익률, 현금흐름 전환 근거를 찾게 해야 한다.
```

구체 패치 후보:

```text
1. v4_planner_runtime.py
   - SourceTask draft에 task별 query_intents를 허용한다.
   - draft.query_intents가 있으면 global query_intents보다 우선한다.
   - cost_overrun task는 원가 부담/지연/해지 query가 max_queries 안에 먼저 들어와야 한다.

2. v4_production_orchestrator.py
   - retry guard를 "이벤트 전체 direct accepted 여부"로 멈추지 않는다.
   - 실패한 external web/LLM task가 있고 web/LLM accepted가 0이면
     raw_assertion_rejections와 web_rejected_documents를 planner feedback에 다시 넣는다.

3. v4_evidence_extraction_bridge.py
   - Naver search snippet은 계속 score 금지.
   - 하지만 full fetched article/report는 별도 source admissibility로 분리한다.
   - trusted news/domain allowlist 또는 explicit official resolver를 통과한 full source만 score 가능하게 한다.
```

2026-07-02 부분 패치 결과:

```text
patched:
  src/e2r/research_brain/v4_planner_runtime.py
  src/e2r/research_brain/v4_production_orchestrator.py
  tests/test_research_brain_v4_operational_modes.py

implemented:
  1. source_task_drafts[*].query_intents schema 허용
  2. draft별 query_intents가 있으면 해당 SourceTask에만 우선 적용
  3. draft별 query_intents가 없을 때만 top-level query_intents를 fallback으로 적용
  4. fallback planner draft도 primitive별 query_intents를 보존
  5. direct accepted claim이 있어도 별도 external web/LLM task 실패가 있으면
     rejected_claim_feedback/source_rejection_feedback retry를 막지 않음

not implemented yet:
  1. trusted news/domain allowlist
  2. Naver-discovered KIND/DART official detail resolver live artifact proof
  3. v21 output 재실행으로 web_or_llm_accepted_claim_count >= 1 증명
  4. v21 output 재실행으로 official-only FULL_THESIS candidate scan이 실제 live trace를 후보화하는지 증명
```

2026-07-02 추가 부분 패치 결과:

```text
patched:
  src/e2r/census/census_runner_v4.py
  tests/test_census_v4_brain_stage_promotion_gate.py

implemented:
  1. FULL_THESIS production runner가 BRAIN_WEB_PARTIAL stage row만 보지 않음
  2. stagecourt_traces.jsonl의 research_brain_v4_attempt trace도 직접 후보로 스캔
  3. official-only complete thesis trace도 FULL_THESIS 후보 심사를 받을 수 있음
  4. 별도 Brain/Web evidence gate는 그대로 유지

not implemented yet:
  1. trusted news/domain allowlist
  2. Naver-discovered KIND/DART official detail resolver live artifact proof
  3. v21 output 재실행으로 web_or_llm_accepted_claim_count >= 1 증명
  4. v21 output 재실행으로 official-only FULL_THESIS candidate scan이 실제 live trace를 후보화하는지 증명
```

쉬운 예:

```text
패치 전:
  T1 계약금액 task, T2 납품일정 task, T6 cost_overrun task가
  모두 같은 전체 query 목록을 나눠 썼다.
  max_queries=2이면 T6가 필요한 "원가 부담/지연/해지" query가 실행 전에 잘릴 수 있었다.

패치 후:
  T6 draft 안에 query_intents가 있으면 T6 SourceTask는 그 query만 먼저 쓴다.
  없을 때만 전체 query_intents를 backup으로 쓴다.
```

FULL_THESIS candidate scan 예:

```text
패치 전:
  Research Brain trace가 공식 DART/IR claim으로 full thesis green gate를 모두 닫아도
  BRAIN_WEB_PARTIAL row가 없으면 candidate_row_count=0.

패치 후:
  stagecourt_traces.jsonl의 live research_brain_v4_attempt trace를 직접 후보로 본다.
  단 official-only trace는 여전히 BRAIN_WEB_EVIDENCE_PASS를 만족하지 않는다.
```

또 다른 예:

```text
패치 전:
  계약금액은 DART claim으로 accepted.
  하지만 고객품질 web task는 주식목록/채널 페이지만 걸려 실패.
  이벤트 안에 direct accepted가 있으니 retry 중단.

패치 후:
  DART task는 채워진 것으로 유지.
  고객품질 web task 실패는 source_rejection_feedback으로 LLM planner에 다시 전달.
```

검증한 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_task_query_intents_are_task_specific_before_global_fallback \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_direct_source_task_acceptance_blocks_rejected_claim_feedback_retry \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_direct_source_task_acceptance_does_not_block_external_llm_rejected_claim_feedback_retry \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_direct_source_task_acceptance_does_not_block_failed_external_source_feedback_retry \
  -v

result = Ran 4 tests / OK

PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
result = Ran 33 tests / OK

PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_planner_provider -v
result = Ran 6 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
result = Ran 12 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks -v
result = Ran 7 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_run_mode_honesty -v
result = Ran 18 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_brain_web_readiness_gate -v
result = Ran 14 tests / OK

PYTHONPATH=src python -m unittest discover -s tests -v
result before strict schema test addition = Ran 5044 tests in 196.216s / OK

PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_after_p0b_official_detail_resolver_artifact.json \
  --log output/test_full_repo_0701/full_unittest_after_p0b_official_detail_resolver.log \
  -- python -m unittest discover -s tests -v

latest full unittest after P0-B official detail resolver patch:
  status = OK
  test_count = 5048
  failed_count = 0
  error_count = 0
  duration_seconds = 188.0978
  artifact_sha256 = 71f444f03cfe7f6ef0f5da5f8b285fa37ab51a611a15ce143ed7d3d1ad2a6a1a
  log_sha256 = 12b0088e9ddb22995994770e8d8cd5962c724ab141339b201d0f7a12f9521d2c
```

다음 run 최소 증명:

```text
accepted_claims.jsonl에 RAWLLM-* 기반 accepted claim >= 1
web_or_llm_accepted_claim_count >= 1
해당 claim은 web_fetched_documents.jsonl의 FETCHED_FULL_SOURCE document_id에 연결
검색 snippet 자체는 여전히 score evidence가 아님
```

주의:

```text
위 패치는 "웹/LLM claim을 점수에 넣는 허가"가 아니다.
실패한 web/LLM task가 다음 LLM 계획으로 되돌아가게 만든 배관 패치다.

즉 다음 diagnostic에서 RAWLLM accepted claim이 0이면,
이제는 "query가 task별로 틀렸는가"보다
"source admissibility / official resolver / primitive mapping이 왜 막았는가"를 먼저 봐야 한다.
```

### P0-A/P0-C v22/v23 재실행 결과

별도 상세 문서:

```text
docs/0701/census_v4_0701_sourcequality_v23_patch_rerun_result_and_next_bottleneck_2026-07-02.md
```

v22는 패치 효과 검증 실행이 아니라 schema regression 실행이다.

```text
output = output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v22
readiness = NOT_READY
real_provider_success_count = 0
leaf critical_count = 2
runtime plausibility = FAIL

provider_error:
  strict schema requires every key in properties to be present in required.
  Missing query_intents.
```

원인:

```text
source_task_drafts[*].query_intents를 properties에는 추가했지만
strict provider required 목록에는 추가하지 않았다.
```

수정:

```text
PLANNER_BATCH_OUTPUT_SCHEMA source_task_drafts.items.required += query_intents
test_planner_batch_schema_requires_every_declared_object_property_for_strict_provider 추가
```

v23은 위 schema 수정을 반영한 유효 재실행이다.

```text
output = output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v23
readiness = NOT_READY
leaf critical_count = 0
runtime plausibility = PASS_LIVE_RUNTIME_PLAUSIBILITY

planner_run_count = 22
real_provider_success_count = 2
real_provider_failure_count = 1
source_task_execution_count = 13
web_search_task_count = 4
web_fetched_document_count = 2
llm_claim_extractor_attempt_count = 2
accepted_claim_count = 4
official_accepted_claim_count = 4
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0
```

FULL_THESIS production runner 변화:

```text
v21 candidate_row_count = 0
v23 candidate_row_count = 1
v23 promoted_full_thesis_row_count = 0
```

v23 candidate:

```text
symbol = 003090
primary_archetype = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_source = stagecourt_trace_direct_scan
present_primitives = implementation_timeline
missing_green_primitives =
  direct_company_cash_route
  policy_or_regulatory_confirmed
  subsidy_capture_visible
blocker = missing_green_gate_primitives
```

해석:

```text
P0-A는 "후보 스캔이 BRAIN_WEB_PARTIAL에 묶여 0이 되는 문제"를 일부 고쳤다.
하지만 green gate primitive가 claim-backed로 닫히지 않아 FULL_THESIS 승격은 여전히 0이다.

P0-C는 task-specific query_intents와 retry feedback 배관을 고쳤다.
하지만 v23에서도 web/LLM accepted claim은 0이므로,
다음 병목은 source admissibility, official resolver, primitive mapping feedback 효과다.
```

쉬운 예:

```text
패치 전:
  심사 신청함 자체를 못 열어서 후보가 0.

패치 후:
  신청함은 열렸고 후보 1건을 찾았다.
  하지만 필수 서류 3개가 비어서 합격자는 0.
```

### P0-D. 운영 minimum은 패치 후 크게 돌린다

지금 당장 30/20/10만 맞추려고 더 크게 돌리면 안 된다.

```text
현재 병목:
  web/LLM accepted claim = 0
  v23에서 patched FULL_THESIS 후보 스캔은 candidate 1개까지 반영됨
  하지만 missing green gate primitives로 promoted FULL_THESIS row = 0

먼저 resolver/feedback을 이어서 고치고,
patched candidate scan 효과까지 포함한 새 v21+ diagnostic을 만든 뒤,
그 다음 goal3의 operational minimum을 돌린다.
```

## 10. 다음 에이전트 공격 질문

다음 리뷰어는 아래 질문으로 이 문서를 공격해야 한다.

```text
1. non-Stage0 85개 중 운영 Stage로 오해될 필드가 남아 있는가?
2. EVENT_WEIGHTED_PARTIAL 67개가 verified_score처럼 쓰이는 경로가 남아 있는가?
3. official-only complete thesis가 FULL_THESIS가 될 수 있는 경로가 있는가?
4. official-only trace가 BRAIN_WEB_EVIDENCE_PASS를 가짜로 만족하지는 않는가?
5. Naver-discovered KIND/DART URL이 공식 resolver로 넘어가는가?
6. general NEWS가 trusted connector 없이 score source로 들어가는 길이 없는가?
7. raw assertion rejection reason이 planner feedback에 실제로 반영되는가?
8. Samsung/Hynix daily DART event row가 C06/HBM full thesis로 보이는 필드가 남아 있는가?
9. Red event-board row가 4C transition으로 보이는 필드가 남아 있는가?
10. provider failure나 source pending이 낮은 score/Red로 확정되는 경로가 남아 있는가?
```

## 11. 현재 완료/미완료 판정

```text
ANTI_FAKE / scope honesty:
  mostly PASS

Stage existence:
  event-board Stage exists
  operational FULL_THESIS Stage does not exist

Brain/Web:
  attempted
  not evidence-pass
  web/LLM accepted claim = 0

Full thesis production:
  not ready
  FULL_THESIS row = 0

Goal completion:
  false
```

한 줄 결론:

```text
지금 결과는 "정직한 상태판"으로는 개선됐다.
하지만 사용자가 원하는 "실제 운영 full thesis Stage/score 파이프라인"은 아직 열리지 않았다.
다음 패치는 official/full-thesis candidate path, official detail resolver, rejected-claim feedback loop가 먼저다.
```
