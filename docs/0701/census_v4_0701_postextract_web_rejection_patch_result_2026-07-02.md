# Census v4 0701 Post-Extraction Web Rejection Patch Result

작성 시점: 2026-07-02 KST  
repo: `/home/eorb915/projects/stock_agent`  
patched diagnostic: `output/census_v4/2026-07-01-brain-web-diagnostic-postextract-v1`  
as_of_date: `2026-07-01`

2026-07-02 추가 패치 이후 우선 문서:

```text
docs/0701/census_v4_0701_brain_web_metric_split_patch_result_2026-07-02.md
```

이 문서는 post-extraction web rejection ledger 패치 결과를 기록한다.
최신 Brain/Web accepted claim split 수치는 metric split 문서를 우선한다.

## 한 줄 결론

```text
웹/뉴스 문서를 fetch한 뒤 Evidence OS에서 점수 claim으로 못 쓴 이유가
이제 web_rejected_documents.jsonl에 문서 단위로 남는다.

하지만 운영 FULL_THESIS Stage는 여전히 0개다.
```

쉬운 예:

```text
이전:
  웹 기사 4개를 읽었는데 점수로 안 들어갔다.
  그런데 "왜 버렸는지" 영수증이 web_rejected_documents에 없었다.

패치 후:
  웹 기사/페이지를 읽고 버린 이유가 문서별로 남는다.
  예: target이 다름, primitive가 안 맞음, historical, quote/anchor 문제.
```

## 코드 패치

변경 파일:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

핵심 변경:

```text
1. SourceAcquisitionResultV4.web_fetched_documents의 document_id를 Evidence OS 처리에 전달.
2. fetch된 웹 문서가 accepted claim 없이 끝나면 post-extraction rejection row 생성.
3. row에는 document_id, source_task_id, raw_assertion_ids, rejected_claim_ids, not_eligible_reasons를 기록.
4. acquisition 단계 reject와 구분하기 위해 rejection_phase=post_extraction_evidence_os 추가.
5. snippet_score_forbidden=true 유지.
6. extraction_audit.post_extraction_web_rejected_document_count 추가.
```

새 row 예시 필드:

```text
schema_version = e2r_research_brain_v4_web_rejected_document_v1
rejection_phase = post_extraction_evidence_os
rejection_reason = post_extraction_no_score_eligible_claim
document_id = DOC-...
source_task_id = ST-...
raw_assertion_ids = [...]
rejected_claim_ids = [...]
not_eligible_reasons = [...]
snippet_score_forbidden = true
```

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_cutover_contract_blind_extraction \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_evidence_extraction_from_real_document -v
```

결과:

```text
Ran 39 tests
OK
```

추가된 핵심 테스트:

```text
test_web_fetched_document_rejected_after_extraction_gets_document_level_rejection_row
```

검증 내용:

```text
web_fetched_documents = 1
web_rejected_documents = 1
rejection_phase = post_extraction_evidence_os
rejection_reason = post_extraction_no_score_eligible_claim
raw_assertion_ids가 source_task_execution.raw_assertion_ids와 연결됨
rejected_claim_ids가 source_task_execution.rejected_claim_ids와 연결됨
not_eligible_reasons에 primitive mapping rejection 이유가 남음
```

## Post-Patch Diagnostic

실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-postextract-v1 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-provider codex_cli \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate brain_web \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --write-operational-docs false
```

결과:

```text
stdout = NOT_READY
```

`NOT_READY`는 예상된 상태다.
이번 패치의 목적은 Brain/Web pass 선언이 아니라, 웹 문서 reject trace 누락을 고치는 것이다.

## Diagnostic 수치

`output/census_v4/2026-07-01-brain-web-diagnostic-postextract-v1` 직접 집계:

```text
stage_scope:
  CENSUS_EVENT_BOARD = 3391
  FULL_THESIS = 0
  BRAIN_WEB_PARTIAL = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

web_fetched_documents.jsonl = 7
web_rejected_documents.jsonl = 8

web_rejected_documents rejection_phase:
  post_extraction_evidence_os = 7
  acquisition/policy phase = 1

web_rejected_documents rejection_reason:
  post_extraction_no_score_eligible_claim = 6
  post_extraction_no_extractable_claim = 1
  web_fetch_target_not_in_title_snippet_or_lead = 1
```

Brain/Web readiness gate:

```text
verdict = BLOCKED
brain_web_evidence_pass_allowed = false

llm_planner_call_count = 22 / required 30
web_search_task_count = 4 / required 20
web_search_call_count = 4 / required 20
web_fetched_document_count = 7 / required 10
llm_claim_extractor_attempt_count = 7 / required 10
web_or_llm_accepted_claim_count = 0 / required 3

web_rejected_document_count = 8
naver_search_call_count = 4
snippet_to_score_count = 0
fake_provider_used_count = 0
```

Planner 상태:

```text
planner_runs.jsonl = 22
planner_run_role:
  initial = 21
  feedback_retry = 1

feedback_retry:
  provider_name = codex_cli_planner
  real_provider_success = true
  rejected_claim_feedback_count = 8
  planner_feedback = ["previous_claims_rejected_before_score"]
```

중요한 개선:

```text
feedback-v1에서는 rejected claim feedback retry가 0회였다.
postextract-v1에서는 rejected feedback 8개를 들고 feedback_retry가 1회 실행됐다.
```

쉬운 예:

```text
이전:
  "이 문서들은 점수에 못 쓴다"까지만 내부적으로 알고 끝났다.

이제:
  "왜 못 썼는지" 8개 feedback을 planner에게 다시 보여 주고,
  planner가 한 번 더 검색/소스 계획을 만들었다.
```

## 이번 실행에서 더 엄격해진 점

`feedback-v1`에서는 OpenDART Brain/Web partial accepted claim 2개가 있었다.
`postextract-v1`에서는 latest live planner/source path가 달라져 accepted Brain/Web claim이 0개였다.

```text
accepted_claims.jsonl = 92
accepted source_provider:
  OpenDART = 92

web/news accepted score claim = 0
Brain/Web promoted stage row = 0
BRAIN_WEB_PARTIAL row = 0
```

이건 패치 실패가 아니라 현재 gate가 더 정직해진 결과로 봐야 한다.
웹/뉴스 문서를 읽었지만 점수로 쓸 수 있는 claim이 없으면 partial stage를 올리지 않는다.

주의:

```text
accepted 0개를 "점수 낮음"으로 해석하면 안 된다.
현재는 "운영 점수 확정 불가 / Brain-Web evidence blocked"다.
```

## 새로 확인된 실제 reject 예시

예시 1:

```text
url = https://www.kdpress.co.kr/news/articleView.html?idxno=205554
rejection_phase = post_extraction_evidence_os
rejection_reason = post_extraction_no_score_eligible_claim
not_eligible_reasons:
  mapping_not_accepted:REJECTED
  primitive_mapping_rejected:no_allowed_primitive_for_predicate
  semantic_rejected
  target_scope_not_allowed:UNRELATED
  target_not_direct:NOT_TARGET_SCOPED
```

예시 2:

```text
url = https://plumsec.com/ko/report/detail?rcept_no=20260630801612
rejection_phase = post_extraction_evidence_os
rejection_reason = post_extraction_no_score_eligible_claim
not_eligible_reasons:
  future_event
  semantic_rejected
  target_scope_not_allowed:UNRELATED
  temporal_not_allowed:UNKNOWN
  primitive_mapping_rejected:no_allowed_primitive_for_predicate
```

예시 3:

```text
url = https://timeli.tistory.com/1028
rejection_phase = post_extraction_evidence_os
rejection_reason = post_extraction_no_extractable_claim
raw_assertion_ids = []
rejected_claim_ids = []
```

## 남은 P0

이번 패치로 닫힌 것:

```text
웹 fetch 후 Evidence OS reject가 문서 단위로 보이지 않던 문제.
```

아직 안 닫힌 것:

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
web/news accepted score claim = 0
BRAIN_WEB_EVIDENCE_PASS = false
all-archetype source-backed replay = 6/32
production full thesis runner pass = false
```

다음 P0 패치 후보:

```text
1. web_or_llm_accepted_claim_count를 official/web/LLM/full-thesis claim으로 분리.
2. feedback retry가 만든 새 source tasks가 실제 acquisition까지 이어지는지 강화.
3. source task / primitive gap 단위로 direct accepted와 missing material gap을 분리.
4. full thesis refresh eligible row가 0인 이유를 runner policy와 artifact에 명시.
5. C01~C32 source-backed replay parity 확장.
```

## 최종 판단

```text
post-extraction web rejection ledger 패치는 성공했다.
그러나 전체 goal completion은 아직 아니다.
```

지금 상태는 더 정직해졌다.
웹을 읽고 점수로 못 쓴 문서가 숨겨지지 않는다.
다음 단계는 이 reject feedback을 이용해 planner/source acquisition이 더 적절한 원문을 찾도록 만드는 것이다.
