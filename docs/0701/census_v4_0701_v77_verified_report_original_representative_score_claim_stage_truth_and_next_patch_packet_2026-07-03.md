# Census v4 0701 v77 Verified Report Original / Representative Score Claim / Stage Truth / Next Patch Packet

작성일: 2026-07-03

이 문서는 v75, v76, v77 산출물을 교차검증한 리뷰 패킷이다. 다음 에이전트는 이 문서를 성공 보고서로 읽으면 안 된다.

한 줄 결론:

```text
Stage가 있긴 있다.
하지만 운영자가 쓸 수 있는 FULL_THESIS Stage는 아직 0개다.

v77 기준:
  CENSUS_EVENT_BOARD = 3390개
  BRAIN_WEB_PARTIAL = 1개
  FULL_THESIS = 0개

이번 패치로 고친 것은 "비점수 accepted claim이 대표 Stage row에 섞이는 증거 체인 오류"다.
운영 Full Thesis 완성은 아직 아니다.
```

쉬운 예:

```text
보고서에서 문장 24개를 뽑았다.
그중 실제 채점표 칸에 들어간 문장은 7개다.

고치기 전:
  24개를 전부 "점수 증거"처럼 Stage row에 붙임
  -> 17개는 primitive/score contribution이 없어서 감사 실패

고친 후:
  점수에 들어간 7개만 대표 Stage row에 붙임
  나머지 17개는 "추출됐지만 비대표/비점수 claim"으로 남김
  -> leaf audit, primitive chain audit PASS
```

## 1. 사용한 산출물

주요 비교 대상:

```text
v75:
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v75

v76:
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v76

v77:
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v77
```

v77 실행 명령:

```bash
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 \
E2R_CODEX_EXTRACTOR_TIMEOUT_SECONDS=120 \
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v77 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-timeout-seconds 120 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

실행 결과:

```text
exit code = 1
stdout = NOT_READY
```

이 `NOT_READY`는 패치 실패와 같은 뜻이 아니다. v77에서는 leaf chain critical fail이 닫혔고, 남은 blocker는 운영 최소 수집량과 Full Thesis 미완성이다.

## 2. 질문에 대한 정확한 답: Stage가 있긴 한가?

v77 `census_stage_status.jsonl`:

```text
total rows = 3391
stage_scope=CENSUS_EVENT_BOARD = 3390
stage_scope=BRAIN_WEB_PARTIAL = 1
stage_scope=FULL_THESIS = 0
operator_stage_use=NOT_FULL_THESIS_STAGE = 3391
```

base stage 분포:

| base_stage | count | 해석 |
| --- | ---: | --- |
| Stage0 | 3306 | 현재 catalyst 없는 상태판 row |
| Stage1 | 53 | 상태판 후보 row |
| Stage2-Watch | 30 | 상태판 watch row |
| 2 | 1 | Brain/Web partial row의 canonical Stage2 |
| Red | 1 | 상태판 risk-review row |

정확한 답:

```text
상태판 Stage는 있다.
Brain/Web partial Stage도 1개 있다.
운영 FULL_THESIS Stage는 없다.
```

쉬운 예:

```text
CENSUS_EVENT_BOARD:
  "오늘 전체지도에서 이 종목을 한번 확인했다"는 표식.

BRAIN_WEB_PARTIAL:
  "원문/LLM claim 일부가 score chain까지 닫혔다"는 부분 증거 표식.

FULL_THESIS:
  "전체 아키타입 thesis, Green/Yellow/Red gate, full score까지 닫혔다"는 운영 Stage.

v77은 세 번째가 아직 0개다.
```

## 3. 삼성전자와 SK하이닉스 현재 상태

v77 기준 삼성전자:

```text
symbol = 005930
company_name = 삼성전자
base_stage = Stage1
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
score_scope = EVENT_WEIGHTED_PARTIAL
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
score_valid_status = FINAL_WITH_NONMATERIAL_GAPS
accepted_claim_count = 1
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
full_e2r_verified_score = null
stage_signal = OFFICIAL_EVENT_WATCH
missing_primitives = repeat_evidence_family, cash_or_revision_conversion
failed_stage_gates = missing_green_bridge
```

해석:

```text
삼성전자는 운영 Full Thesis가 아니다.
4.0점은 전체 E2R 점수가 아니라 event-board partial score다.
예전처럼 2020년 감사/타사 감사의견을 hard break로 넣는 문제는 v77의 핵심 산출물에서는 보이지 않는다.
```

v77 기준 SK하이닉스:

```text
symbol = 000660
company_name = SK하이닉스
base_stage = 2
canonical_stage = 2
stage_scope = BRAIN_WEB_PARTIAL
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 75.8333
score_valid_status = FINAL
accepted_claim_count = 7
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
full_e2r_verified_score = null
stage_signal = BRAIN_WEB_CLAIM_BACKED_STAGE
missing_primitives = hbm_capacity_constraint
failed_stage_gates = hbm_capacity_constraint
```

해석:

```text
SK하이닉스는 Brain/Web partial row가 1개 있다.
하지만 이 75.8333은 FULL_E2R_100 운영 점수가 아니다.
FULL_THESIS 승격에는 hbm_capacity_constraint 등 Green/full-thesis primitive coverage가 아직 부족하다.
```

쉬운 예:

```text
하이닉스 partial 75.8333:
  "보고서 일부 문장으로 C06 일부 칸은 채웠다"

하이닉스 FULL_THESIS:
  "C06 필수 primitive와 stage gate가 모두 닫혀 운영 Stage로 쓸 수 있다"

v77은 전자만 있다.
```

## 4. v75에서 실제로 잘못됐던 것

v75에서는 broker/report PDF에서 LLM claim extraction이 실제로 돌았고, accepted claim도 나왔다.

그러나 대표 Stage row에 다음 문제가 있었다.

```text
BRAIN_WEB_PARTIAL accepted_claim_ids = 17개
primitive_state_ids = 4개
score_contribution_ids = 6개
scored_claim_without_primitive_state_count = 12
leaf_artifact_audit = FAIL
primitive_state_chain_audit = FAIL
```

핵심 오류:

```text
accepted claim 전체를 대표 score claim처럼 Stage row에 실었다.
그중 12개는 primitive state와 score contribution으로 이어지지 않았다.
```

왜 문제가 심각한가:

```text
accepted claim
  원문에서 뽑혀 deterministic guard를 통과한 claim.

representative score claim
  실제 score contribution의 support_claim_ids로 쓰인 claim.

둘은 같지 않다.
accepted claim 전체를 Stage 증거로 실으면
"점수에 쓰이지 않은 문장"이 점수 근거처럼 보인다.
```

쉬운 예:

```text
리포트에서 문장 17개를 형광펜으로 표시했다.
그중 5개만 실제 시험 답안에 근거로 사용했다.

그런데 제출 파일에는 17개 전부를 "답안 근거"라고 붙였다.
감사자는 "12개 근거는 답안 번호가 없는데?"라고 실패시킨다.
```

## 5. v76/v77 패치 내용

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
tests/test_census_v4_brain_web_readiness_gate.py
```

### 5.1 StageCourt trace accepted claim 범위 축소

기존:

```text
stagecourt_traces.accepted_claim_ids = item accepted_claim_ids 전체
```

변경:

```text
stagecourt_traces.accepted_claim_ids = positive score contribution의 support_claim_ids만
stagecourt_traces.score_support_claim_ids = 동일
stagecourt_traces.all_accepted_claim_ids = 전체 accepted claim 보존
stagecourt_traces.non_score_accepted_claim_ids = accepted됐지만 점수 contribution에는 안 들어간 claim
```

의미:

```text
대표 Stage row에는 score에 실제 기여한 claim만 싣는다.
나머지는 삭제하지 않고 non_score_accepted_claim_ids로 추적한다.
```

### 5.2 brain_to_claim_trace 승격 표시 분리

기존:

```text
같은 stagecourt_trace_id를 가진 brain_to_claim_trace row는 모두 census_stage_status_id를 받았다.
```

변경:

```text
대표 score claim만 census_stage_status_id를 받는다.
비대표 accepted claim은 census_stage_status_id=null로 남고,
not_promoted_reason=accepted_claim_not_in_representative_score_claim_ids를 기록한다.
```

v77 실제 분포:

```text
brain_to_claim_trace total = 24
CLAIM_SCORE_TRACE_PROMOTED_TO_CENSUS_STAGE_STATUS = 7
ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING = 17
```

### 5.3 readiness gate에서 비대표 claim contribution 강제 제거

기존:

```text
accepted Brain/Web trace row에 score_contribution_id가 없으면 blocker
```

변경:

```text
representative_score_claim=True 또는 SCORE_SUPPORTED인 row만 contribution을 강제한다.
ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING은 blocker가 아니다.
```

v76에서 남았던 blocker:

```text
Brain/Web trace rows missing score_contribution_id: 4
```

v77에서 제거됨:

```text
brain_trace_missing_score_contribution_ref_count = 0
```

## 6. Verified broker/report original route 상태

v77에서는 general web에서 발견한 broker/report PDF가 무조건 score source가 되는 것이 아니다.

현재 인정 조건:

```text
문서가 PDF/report-like여야 한다.
recognized report domain이어야 한다.
fetch된 원문과 EvidenceAnchor가 있어야 한다.
LLM/raw assertion -> adjudicated claim -> primitive mapping -> score contribution chain을 통과해야 한다.
```

v77 fetched report:

```text
web_fetched_documents.jsonl = 2

1. https://www.samsungpop.com/common.do?...research.pdf...
   verified_report_original = true
   verified_report_original_source_class = BrokerReportPublicPDF
   verified_report_result_host = samsungpop.com

2. https://stock.pstatic.net/stock-research/company/34/20251104_company_405753000.pdf
   verified_report_original = true
   verified_report_original_source_class = BrokerReportPublicPDF
   verified_report_result_host = stock.pstatic.net
```

중요한 공격 지점:

```text
recognized report domain은 source-quality ontology다.
점수 규칙은 아니다.

다만 samsungpop.com 같은 넓은 도메인은 다음 에이전트가 꼭 공격해야 한다.
브로커 도메인이라고 해서 그 도메인의 모든 PDF가 report original이라고 보면 안 된다.
다음 패치에서는 path, content-type, PDF text header, report metadata, analyst/report title 등을 추가 검증하는 것이 안전하다.
```

쉬운 예:

```text
증권사 홈페이지 PDF라고 해서 전부 리서치 보고서는 아니다.
약관 PDF, 이벤트 안내 PDF, 공지 PDF도 있을 수 있다.
따라서 "증권사 도메인 + PDF"만으로는 장기적으로 부족하다.
```

## 7. v77 교차검증 결과

### 7.1 Leaf artifact audit

```text
artifact = leaf_artifact_audit.json
verdict = PASS
critical_count = 0
scored_claim_without_primitive_state_count = 0
scored_row_missing_claim_ids = 0
scored_row_missing_primitive_state_ids = 0
scored_row_missing_score_contribution_ids = 0
scored_row_missing_stagecourt_trace = 0
```

v75와의 차이:

```text
v75 scored_claim_without_primitive_state_count = 12
v77 scored_claim_without_primitive_state_count = 0
```

### 7.2 Primitive state chain audit

```text
artifact = primitive_state_chain_audit.json
verdict = PASS
critical_count = 0
representative_stage_primitive_claim_set_mismatch_count = 0
representative_score_claim_without_primitive_state_count = 0
representative_score_mapping_id_not_found_count = 0
```

### 7.3 Source task satisfaction audit

```text
artifact = source_task_satisfaction_audit.json
verdict = PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
critical_count = 0
representative_score_claim_without_source_task_execution_count = 0
representative_score_claim_missing_document_row_count = 0
representative_score_claim_missing_anchor_row_count = 0
representative_score_claim_missing_score_contribution_count = 0
representative_score_claim_missing_stagecourt_trace_count = 0
```

### 7.4 Brain stage promotion audit

```text
artifact = brain_stage_promotion_audit.json
verdict = PROMOTION_APPLIED
blockers = []
web_or_llm_accepted_claim_count = 24
llm_extracted_accepted_claim_count = 24
brain_promoted_stage_row_count = 1
brain_score_contribution_count = 6
brain_stage_trace_count = 1
```

주의:

```text
PROMOTION_APPLIED는 BRAIN_WEB_PARTIAL row 승격이다.
FULL_THESIS 승격이 아니다.
```

### 7.5 Brain/Web readiness gate

```text
artifact = brain_web_readiness_gate_audit.json
verdict = BLOCKED
brain_web_evidence_pass_allowed = false
brain_trace_missing_score_contribution_ref_count = 0
```

남은 blockers:

```text
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 7/20
Brain/Web operational minimum web/news search calls not met: 7/20
Brain/Web operational minimum fetched documents not met: 2/10
Brain/Web operational minimum claim extractor attempts not met: 2/10
```

해석:

```text
증거 체인은 닫혔다.
하지만 이 smoke는 universe-limit=1, planner-success-limit=1, max-fetches-per-task=1이라
운영 최소량 30/20/20/10/10을 채우도록 설계된 실행이 아니다.
```

절대 하면 안 되는 패치:

```text
운영 readiness를 통과시키려고 minimum count를 낮추는 것.
```

해야 하는 것:

```text
운영 readiness를 주장하려면 더 넓은 bounded live run을 돌려 실제 최소량을 채운다.
작은 smoke는 "증거 체인 smoke"라고 표시하고 production readiness라고 말하지 않는다.
```

## 8. Goal requirement matrix 상태

v77 `goal_requirement_matrix_audit.json` blockers:

```text
full_thesis_smoke_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
brain_web_evidence_pass_false
source_backed_replay_parity_all_archetypes_pending
```

해석:

```text
이번 패치는 anti-fake leaf / primitive chain / source satisfaction 쪽 critical을 닫았다.
하지만 goal.md 전체 완료는 아니다.
FULL_THESIS production, seed promotion, all-archetype replay parity가 남아 있다.
```

## 9. 테스트 결과

패치 후 실행한 관련 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_primitive_state_chain \
  tests.test_census_v4_source_task_satisfaction_chain \
  -v
```

결과:

```text
Ran 40 tests in 10.530s
OK
```

문법 확인:

```bash
python -m py_compile src/e2r/census/census_runner_v4.py
```

결과:

```text
OK
```

v77 live smoke:

```text
exit code = 1
stdout = NOT_READY
leaf_artifact_audit = PASS
primitive_state_chain_audit = PASS
source_task_satisfaction_audit = PASS
brain_stage_promotion_audit = PROMOTION_APPLIED
brain_web_readiness_gate_audit = BLOCKED
```

## 10. 다음 에이전트 공격 체크리스트

다음 에이전트는 아래를 반드시 공격해야 한다.

### 10.1 Stage truth 공격

확인할 것:

```text
FULL_THESIS row가 0개인데 운영 Stage라고 말하는 곳이 없는가?
BRAIN_WEB_PARTIAL 75.8333을 FULL_E2R_100 점수처럼 노출하지 않는가?
CENSUS_EVENT_BOARD Stage1/Stage2-Watch를 운영 Stage처럼 쓰는 곳이 없는가?
operator_stage_use가 전부 NOT_FULL_THESIS_STAGE인지 확인했는가?
```

v77 정답:

```text
operational_stage_use_allowed = false
FULL_THESIS = 0
FULL_E2R_100 verified score = 0
```

### 10.2 Representative claim 공격

확인할 것:

```text
stage row accepted_claim_ids가 score contribution support_claim_ids와 맞는가?
accepted됐지만 점수에 안 들어간 claim이 대표 Stage row에 섞이지 않는가?
brain_to_claim_trace에서 비대표 claim에 census_stage_status_id가 붙지 않는가?
```

v77 정답:

```text
brain_to_claim_trace:
  SCORE_SUPPORTED = 7
  ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING = 17

BRAIN_WEB_PARTIAL stage row:
  accepted_claim_count = 7
```

### 10.3 Source route 공격

확인할 것:

```text
recognized report domain이 너무 넓지 않은가?
samsungpop.com 전체 domain 허용이 약하지 않은가?
stock.pstatic.net report path는 path 검증이 충분한가?
PDF fetch 실패, quote anchor 실패, 날짜 실패가 score로 새지 않는가?
```

다음 패치 후보:

```text
VerifiedReportOriginal v2:
  recognized domain
  AND report path pattern
  AND PDF/content-type
  AND extracted title/report header
  AND publish/as-of date
  AND target company mention/directness
  AND anchor quote
```

### 10.4 Readiness gate 공격

확인할 것:

```text
비대표 accepted claim 때문에 readiness가 막히지는 않는가?
반대로 대표 score claim이 contribution 없이 readiness를 통과하지는 않는가?
small smoke를 production readiness로 오해하지 않는가?
```

v77 정답:

```text
brain_trace_missing_score_contribution_ref_count = 0
readiness verdict = BLOCKED
block 이유 = 운영 최소 수집량 미달
```

### 10.5 Full Thesis 공격

확인할 것:

```text
SK하이닉스 BRAIN_WEB_PARTIAL이 왜 FULL_THESIS가 아닌가?
missing hbm_capacity_constraint가 실제 Green/full thesis gate에서 필요한가?
full thesis seed promotion이 왜 pending인가?
all-archetype replay parity가 아직 pending인데 완료라고 말하지 않는가?
```

## 11. 다음 패치 방향

우선순위:

```text
1. VerifiedReportOriginal v2 hardening
   broad broker domain -> report-specific path/header/date/content validation으로 강화.

2. Brain/Web operational minimum run
   small smoke가 아니라 30 planner / 20 web tasks / 20 calls / 10 fetches / 10 extractor attempts를
   실제 bounded live 설정으로 채우는 실행을 따로 돌린다.

3. Full Thesis production promotion
   BRAIN_WEB_PARTIAL 1개를 FULL_THESIS로 착각하지 않는다.
   C06 missing primitive를 공식/리포트/IR source task로 닫아 full-thesis gate를 통과해야 한다.

4. All-archetype source-backed replay parity
   C06 일부 성공만으로 전체 완료라고 하지 않는다.
   C01~C36 replay matrix의 source-backed parity가 닫혀야 한다.

5. 출력/운영 UI guard
   event-board partial score, brain-web partial score, full E2R score를 화면/CSV/JSON에서 계속 분리한다.
```

절대 금지:

```text
운영 readiness minimum을 낮춰서 PASS 만들기.
비대표 accepted claim을 primitive에 억지 매핑하기.
BRAIN_WEB_PARTIAL을 FULL_THESIS로 라벨만 바꾸기.
broker domain이면 모든 PDF를 report original로 인정하기.
```

## 12. 최종 판정

v77의 정확한 상태:

```text
증거 체인 critical fail:
  해결됨.

Brain/Web partial Stage:
  1개 있음.

운영 FULL_THESIS Stage:
  0개.

운영 Brain/Web readiness:
  아직 BLOCKED.

goal.md 전체 완료:
  아직 아님.
```

따라서 다음 에이전트에게 넘길 메시지는 이렇다.

```text
"Stage가 있긴 하다"는 말은 맞다.
하지만 운영 Stage는 아니다.

이번 패치로 대표 점수 claim과 비대표 accepted claim을 분리해 감사 체인을 닫았다.
다음은 source route를 더 단단히 하고, bounded live를 운영 최소량까지 키우고,
Full Thesis 승격 조건과 all-archetype replay를 닫아야 한다.
```
