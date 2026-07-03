# Census v4 2026-07-01 v104 Stage Existence / Extractor Retry Patch / Review Packet

작성일: 2026-07-03  
대상 산출물:

```text
v101 live bounded rerun:
  output/census_v4/2026-07-01-v101-live-bounded-rerun

v102 leaf audit replay from v101:
  output/census_v4/2026-07-01-v102-stage-scope-audit-replay-from-v101

v103 readiness trace materiality replay from v102:
  output/census_v4/2026-07-01-v103-readiness-trace-materiality-replay-from-v102
```

## 한 줄 결론

Stage map/status row가 있는 애들은 있다. 하지만 운영자가 쓸 수 있는 `FULL_THESIS` Stage는 아직 0개다.

정확히는:

```text
v101/v102/v103 each stage map/status rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD      3369
  BRAIN_OFFICIAL_PARTIAL    16
  BRAIN_WEB_PARTIAL          6
  FULL_THESIS                0

operator_stage_use:
  NOT_FULL_THESIS_STAGE   3391

operator_score_use:
  NOT_FULL_E2R_SCORE      3391
```

쉬운 예:

```text
CENSUS_EVENT_BOARD = 출석부
BRAIN_*_PARTIAL    = 일부 검사 결과
FULL_THESIS         = 최종 진단서

지금은 출석부와 일부 검사 결과는 있다.
하지만 최종 진단서는 0장이다.
```

따라서 다음 표현은 틀리다.

```text
"삼성전자 운영 Stage1이다"
"하이닉스 운영 점수 60점이다"
```

정확한 표현은:

```text
삼성전자:
  census/event-board 상태판 Stage1 row가 있다.
  FULL_THESIS 운영 Stage는 아니다.

SK하이닉스:
  web/LLM claim-backed partial Stage1 row가 있다.
  FULL_THESIS 운영 Stage는 아니다.
```

## 삼성전자 / SK하이닉스 현재 행

v101/v102/v103 산출물 기준:

```text
삼성전자 005930:
  stage_scope = CENSUS_EVENT_BOARD
  canonical_stage = 1
  base_stage = Stage1
  score_scale = EVENT_WEIGHTED_PARTIAL
  event_evidence_score = 4.0
  accepted_claim_count = 1
  operator_stage_use = NOT_FULL_THESIS_STAGE
  operator_score_use = NOT_FULL_E2R_SCORE
  full_thesis_stage = FULL_THESIS_NOT_RUN

SK하이닉스 000660:
  stage_scope = BRAIN_WEB_PARTIAL
  canonical_stage = 1
  base_stage = 1
  score_scale = EVENT_WEIGHTED_PARTIAL
  event_evidence_score = 60.0
  accepted_claim_count = 3
  accepted_web_llm_claim_count = 3
  operator_stage_use = NOT_FULL_THESIS_STAGE
  operator_score_use = NOT_FULL_E2R_SCORE
  full_thesis_stage = FULL_THESIS_NOT_RUN
```

중요한 해석:

```text
삼성전자 row는 "이번 census에서 볼 일이 있다" 수준이다.
하이닉스 row는 "일부 source-backed claim으로 부분 Stage가 있다" 수준이다.
둘 다 전체 thesis score/stage가 닫힌 결과가 아니다.
```

## 현재까지 고친 것

### 1. v102: `BRAIN_OFFICIAL_PARTIAL` leaf audit 오판 수정

v101 live leaf audit은 아래 2개 critical 때문에 실패했다.

```text
stage_scope_invalid_count = 16
official_claim_but_recent_official_event_zero_count = 19
```

원인:

```text
코드는 official-only Brain trace를 BRAIN_OFFICIAL_PARTIAL로 올렸다.
하지만 auditor가 허용 stage_scope에 BRAIN_OFFICIAL_PARTIAL을 몰라서 invalid로 봤다.
또 official partial row에 official_source_task_count / evidence_document_count가 0으로 남았다.
```

v102 replay 결과 중 최종 PASS artifact:

```text
leaf_artifact_audit_after_v102_count_and_sample_replay.json:
  verdict = PASS
  critical_count = 0
```

주의:

```text
같은 v102 폴더에는 중간 replay 파일도 남아 있다.
예: leaf_artifact_audit_after_v102_replay.json,
    leaf_artifact_audit_after_v102_count_replay.json

이 중간 파일들은 아직 FAIL일 수 있다.
v102 PASS 판정은 leaf_artifact_audit_after_v102_count_and_sample_replay.json 기준이다.
```

### 2. v103: non-representative trace의 StageCourt ref 과잉 차단 수정

v101 readiness gate blocker:

```text
Brain/Web trace rows missing stagecourt_trace_id: 4
```

전수 확인 결과 4개 모두 같은 성격이었다.

```text
symbol = 017670
representative_score_claim = false
score_contribution_id = null
score_support_status = NO_SCORE_CONTRIBUTION
trace_status = CLAIM_EXPORTED_STAGE_NOT_PROMOTED
satisfaction_type = REROUTED_ACCEPTED_CLAIM
satisfies_source_task = false
```

즉 이 4개는 점수 대표 claim이 아니라 보조/비대표 accepted claim이다.  
ScoreContribution도 없고 StageCourt 대표 trace가 없어야 정상인 행이다.

패치 방향:

```text
대표 점수 claim 또는 score contribution이 있는 trace:
  stagecourt_trace_id 없으면 blocker

비대표 accepted claim:
  stagecourt_trace_id 없어도 nonblocking gap으로 기록
```

v103 replay 결과:

```text
brain_web_readiness_gate_audit_after_v103_trace_materiality_replay.json:
  verdict = BLOCKED
  blockers =
    - LLM claim extractor provider errors are unresolved: 5
    - LLM claim extractor timeouts are unresolved: 5
  brain_trace_missing_stagecourt_ref_count = 0
  brain_trace_nonrepresentative_missing_stagecourt_ref_count = 4
```

v104 review-fix replay 결과:

```text
brain_web_readiness_gate_audit_after_v104_review_fixes_replay.json:
  verdict = BLOCKED
  blockers =
    - LLM claim extractor provider errors are unresolved: 5
    - LLM claim extractor timeouts are unresolved: 5
  brain_trace_missing_stagecourt_ref_count = 0
  brain_trace_nonrepresentative_missing_stagecourt_ref_count = 4
  nonblocking_gaps =
    - non-representative Brain/Web accepted claim traces without StageCourt refs: 4
    - Brain/Web evidence pass is forbidden until all blockers are zero
```

쉬운 예:

```text
대표 증거가 "계약금 100억"이면 StageCourt trace가 반드시 있어야 한다.
하지만 참고 증거 "기사에 회사명이 언급됨"은 StageCourt trace가 없어도 점수 누수가 아니다.
```

### 3. v104 코드 패치: production claim extractor timeout 입력 축소와 재시도

Brain/Web readiness artifact blocker 5개는 모두 LLM claim extractor timeout이다.

```text
claim_extractor_runs = 51
timeout rows = 5
provider_error rows = 5
provider_error text = codex_cli_timeout:120s
```

즉 10개가 아니다.

```text
같은 5개 run이
  timeout_count에도 잡히고
  provider_error_count에도 잡힌다.
```

timeout 문서:

```text
002990 금호건설:
  DOC-aae5960126bafd0a2b98
  http://www.snumidas.com/article/2008_1/Team5_Kumho_Industry_080509.pdf
  extractor run status = PROVIDER_FAILED
  source task status = EVIDENCE_OS_ACCEPTED
  timeout 문서 외 다른 문서에서 accepted claims 존재

024110 기업은행:
  DOC-ca0a3349e430c1e3ee8f
  https://securities.miraeasset.com/bbs/download/2105693.pdf?attachmentId=2105693
  extractor run status = PROVIDER_FAILED
  source task status = PROVIDER_FAILED
  해당 timeout source task accepted_claim_ids 없음

043260 성호전자:
  DOC-ff56a163d7463e5f8db9
  https://stockhandbook.blog/2025/11/08/성호전자/
  extractor run status = PROVIDER_FAILED
  source task status = EVIDENCE_OS_ACCEPTED
  timeout 문서 외 accepted claims 존재

052400 코나아이:
  DOC-b14a824d662ef08fb230
  https://stock.pstatic.net/stock-research/company/69/20250613_company_860496000.pdf
  extractor run status = PROVIDER_FAILED
  source task status = PROVIDER_FAILED
  해당 timeout source task accepted_claim_ids 없음

052400 코나아이:
  DOC-5147052c9ccbbc98d48e
  https://stock.pstatic.net/stock-research/company/56/20260612_company_303808000.pdf
  extractor run status = PROVIDER_FAILED
  source task status = PROVIDER_FAILED
  해당 timeout source task accepted_claim_ids 없음
```

주의:

```text
이 timeout은 fetch 실패가 아니다.
5개 문서 모두 web_fetched_documents.jsonl에서 FETCHED_FULL_SOURCE이고,
evidence_documents.jsonl에도 존재한다.

문제를 정확히 말하면:
  "문서를 못 가져온 것"이 아니라
  "가져온 긴 문서에서 LLM claim extractor가 120초 timeout 난 것"이다.

또 코나아이 timeout 문서 2개는 같은 source task에 묶여 있다.
따라서 claim_extractor_runs 기준 timeout row는 5개,
source_task_executions 기준 timeout 포함 provider-error task는 4개로 읽을 수 있다.
```

기존 production extractor 문제:

```text
source_text[:12000]을 통째로 prompt에 넣었다.
긴 PDF/블로그 문서에서 앞부분만 들어가거나 prompt가 무거워졌다.
timeout이 나면 retry 없이 provider_error로 끝났다.
claim_extractor_runs에 prompt 축소 여부, retry 여부도 남지 않았다.
```

v104 패치:

```text
src/e2r/production/claim_extraction/extractor_provider.py
  - prompt schema v2
  - document_text를 first 12000 단순 절단 대신 contract-blind head/signal/tail compact로 생성
  - score_gap, primitive_gap, Green gate, Stage 조건은 계속 prompt에 넣지 않음
  - 1차 limit = 8000 chars
  - timeout 시 2차 retry limit = 3600 chars
  - retry 성공 시 provider_error 없음
  - retry까지 timeout이면 provider_error = codex_cli_timeout:initial=...;retry=...
  - result에 attempt_count, timeout_retry_attempted, initial_prompt_hash, retry_prompt_hash,
    prompt_text_chars, prompt_text_compacted, prompt_text_limit 기록

src/e2r/research_brain/v4_evidence_extraction_bridge.py
  - claim_extractor_runs.jsonl에 위 retry/compact metadata export

tests/test_cutover_contract_blind_extraction.py
  - 긴 문서 prompt compact 테스트 추가
  - timeout 후 작은 contract-blind prompt로 retry 성공하는 테스트 추가
```

v104 교차검증 후 추가 보강:

```text
src/e2r/production/claim_extraction/extractor_provider.py
  - 1차 timeout 후 retry가 non-json/non-zero로 실패해도 예외를 밖으로 새지 않게 provider_error로 포장
  - Codex CLI returncode != 0이면 JSON output이 있어도 실패로 처리
  - source_metadata 안쪽의 primitive_gap / score / stage / hard_break 등 forbidden context key 제거

src/e2r/census/census_runner_v4.py
  - trace의 representative_score_claim=false 자기신고만 믿지 않음
  - 실제 score_contributions.support_claim_ids와 stage row support_claim_ids에서 대표 score claim 여부를 재계산
  - 비대표 StageCourt 누락은 audit 숫자뿐 아니라 nonblocking_gaps에도 기록

tests
  - timeout 후 retry non-json 실패가 provider_error로 남는지 추가
  - non-zero exit + JSON output이 SUCCESS로 둔갑하지 않는지 추가
  - source_metadata 안쪽 forbidden context 제거 테스트 추가
  - 대표 score claim이 trace에서 비대표라고 잘못 표시되어도 blocker가 뜨는 테스트 추가
```

이 패치는 점수 로직을 건드리지 않는다.

```text
점수/Stage/가중치 변경 없음
아키타입별 점수 규칙 변경 없음
LLM에게 "몇 점?" 질문 없음
LLM에게 score_gap/primitive_gap을 보여주지 않음
```

쉬운 예:

```text
나쁜 방식:
  "Green 되려면 FCF가 부족하니 이 문서에서 FCF 찾아줘"

이번 방식:
  "이 문서에서 실제로 말한 사실만 뽑아줘.
   단, 긴 문서라면 회사명/계약/수주/출하/현금흐름/감사/날짜/숫자 문장을 우선 보여줄게."
```

## 현재 산출물 truth와 코드 truth를 섞지 말 것

중요:

```text
v104 extractor retry 패치는 코드에 들어갔다.
하지만 v101 live artifact의 timeout 5개가 자동으로 사라진 것은 아니다.
v101/v102/v103 산출물은 기존 timeout 결과를 그대로 가진다.
```

따라서 최신 상태는:

```text
코드 테스트:
  PASS

v103 artifact readiness:
  BLOCKED

artifact blocker:
  LLM claim extractor timeout rows = 5
  same rows counted as provider_error = 5

다음 확인:
  v104 코드로 full live bounded rerun을 다시 돌려 timeout 5개가 줄었는지 확인해야 한다.
```

운영 readiness blocker는 이보다 더 넓다.

```text
timeout 5개가 다음 live rerun에서 모두 사라져도,
FULL_THESIS row가 0이면 운영 Stage는 여전히 없다.

현재 운영 blocker:
  FULL_THESIS row = 0
  FULL_E2R_100 score row = 0
  operator_stage_use FULL_THESIS_STAGE = 0
  all-archetype source-backed replay = 6/32 수준
  v103 artifact Brain/Web readiness = BLOCKED
```

## 검증 결과

Focused tests:

```bash
PYTHONPATH=src python -m unittest tests.test_cutover_contract_blind_extraction -v
```

결과:

```text
Ran 16 tests
OK
```

Related tests:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  -v
```

결과:

```text
Ran 55 tests
OK
```

Review-fix focused tests:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_cutover_contract_blind_extraction \
  tests.test_census_v4_brain_web_readiness_gate \
  -v
```

결과:

```text
Ran 36 tests
OK
```

Full tests:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

2026-07-03 v104 review-fix 최종 결과:

```text
Ran 5134 tests in 234.621s
OK
```

이 결과는 subagent 교차검증 후 들어간 추가 보강까지 포함한 최종 full unittest 결과다.
즉 코드 단위 검증은 통과했지만, 아래의 live artifact blocker가 사라졌다는 뜻은 아니다.

## 다음 에이전트가 빡세게 봐야 할 공격 포인트

### A. 아직 운영 Stage는 없다

`FULL_THESIS = 0`이다.  
부분 Stage row가 있다는 이유로 운영 readiness를 선언하면 안 된다.

검증 질문:

```text
FULL_THESIS row가 실제로 1개라도 생겼는가?
그 row의 score_scale이 FULL_E2R_100인가?
operator_stage_use가 FULL_THESIS_STAGE인가?
operator_score_use가 FULL_E2R_SCORE인가?
score_contribution_ids와 stagecourt_trace_id가 실제 leaf에 연결되는가?
provider/source pending을 낮은 점수로 확정하지 않았는가?
```

### B. v104 live rerun이 필요하다

이번 timeout retry 패치는 live rerun 전에는 artifact blocker를 제거하지 않는다.

검증 질문:

```text
v104 코드로 같은 v101 조건을 재실행했는가?
claim_extractor_runs의 provider_error가 5에서 줄었는가?
attempt_count=2 / timeout_retry_attempted=true 행이 남았는가?
retry 성공 행은 provider_error 없이 accepted/raw assertion으로 이어졌는가?
retry 실패 행은 ProviderPending/SourcePending으로 남고 점수 확정에 쓰이지 않았는가?
```

### C. timeout retry가 과도한 정보 손실을 만들 수 있다

compact는 timeout을 줄이지만, 문서 중간의 핵심 문장을 놓칠 수 있다.  
그래서 v104 patch는 target alias, high-signal words, generic financial words, head/tail context를 같이 보존한다.

검증 질문:

```text
긴 PDF에서 핵심 문장이 뒤쪽에 있을 때 compact prompt에 남는가?
target alias가 없는 표/본문 claim은 anchor나 source task로 보존되는가?
compact 때문에 claim이 0개가 되면 낮은 점수 확정이 아니라 pending으로 남는가?
```

### D. extractor prompt artifact는 아직 hash/metadata 중심이다

v104는 claim_extractor_runs에 retry/compact metadata를 남긴다.  
다만 planner처럼 raw prompt leaf를 별도로 남기는 구조는 아직 아니다.

검증 질문:

```text
다음 감사에서 timeout prompt 원문까지 봐야 한다면 extractor prompt leaf export가 추가로 필요한가?
개인정보/저작권/원문 길이 문제 때문에 full prompt 대신 compact payload hash + bounded excerpt만 남기는 게 맞는가?
```

### E. all-archetype source-backed replay는 아직 6/32 수준이다

현재 source-backed semantic replay가 있는 대표 아키타입은 C06/C08/C15/C17/C24/C28 쪽이다.  
전 아키타입 운영 parity를 선언하면 안 된다.

검증 질문:

```text
C01~C36 전체 Evidence Contract schema validation만 통과한 것인가?
아니면 source-backed replay까지 전부 통과한 것인가?
source_proxy_only 자료가 운영 score fixture로 새어 들어가지 않았는가?
```

## 최종 판단

현재 상태는:

```text
Stage map/status row 존재:
  YES

운영 FULL_THESIS Stage 존재:
  NO

삼성전자/하이닉스 운영 Stage 확정:
  NO

v102 leaf audit critical:
  fixed by replay

v103 missing StageCourt blocker:
  fixed by materiality split

v104 extractor timeout code mitigation:
  implemented and tested

v104 review fixes:
  implemented and full-tested

Full unittest:
  Ran 5134 tests in 234.621s
  OK

현재 artifact readiness:
  still BLOCKED until live rerun clears extractor timeout/provider_error

운영 readiness:
  still BLOCKED until FULL_THESIS source-backed rows exist
```

한 문장으로:

> 지금은 "Stage가 전혀 없는 상태"는 아니지만, "운영 가능한 최종 Stage가 있는 상태"도 아니다. 부분 Stage와 상태판은 있고, 남은 핵심은 v104 retry 패치로 live rerun을 다시 돌려 extractor timeout을 닫고 `FULL_THESIS`까지 claim-backed로 승격시키는 것이다.
