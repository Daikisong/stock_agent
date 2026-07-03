# Census v4 Enabled Brain/Web Current Truth And Next Patch Packet - 2026-07-01

이 문서는 다음 에이전트가 가장 먼저 읽고 공격적으로 리뷰할 수 있게 만든 최신 단일 진실표다.

대상 실행은 `/tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch` 기준이다.

업데이트:

```text
P2 planner contract primitive filter 패치 후 최신 실행은
/tmp/census_v4_enabled_provider_probe_after_planner_primitive_filter 이다.

최신 수치와 P2 결과는 아래 문서를 우선한다.
docs/0701/census_v4_0701_planner_contract_primitive_filter_cross_validation_2026-07-01.md

P1 rejected mapping feedback retry 패치 후 최신 실행은
/tmp/census_v4_enabled_provider_probe_after_rejected_feedback_patch_v2 이다.

P1 수치와 rejected feedback retry 결과는 아래 문서를 우선한다.
docs/0701/census_v4_0701_rejected_mapping_feedback_retry_patch_2026-07-01.md
```

P2 이후에도 핵심 결론은 유지된다.

```text
Brain/Web accepted claim = 0
Brain/Web StageCourt trace = 0
Brain/Web promoted row = 0
readiness = NOT_READY
```

## 결론

현재 상태는 아래 한 문장으로 정리된다.

```text
Brain/Web leaf는 실제로 생겼지만, Brain/Web accepted claim과 운영 Stage 승격은 아직 0개다.
```

즉 잘못된 방향으로 점수를 억지로 만든 상태는 아니다. 오히려 지금은 점수에 넣으면 안 되는 웹/LLM 결과를 deterministic guard가 막고 있다.

쉬운 예:

```text
자료를 찾았고, LLM이 메모도 썼다.
하지만 그 메모가 "이 문서의 이 문장 때문에 이 점수 칸에 들어간다"까지 통과하지 못했다.
그래서 성적표에는 아직 반영하지 않는 것이 맞다.
```

## 실행 명령

```bash
rm -rf /tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch

PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root /tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch \
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
NOT_READY
```

이 `NOT_READY`는 정상이다. 이유는 leaf 부족이 아니라 cutover chain 미완성이다.

## 최신 숫자

row count:

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
census_stage_status.jsonl:      3391
```

raw assertion 분해:

```text
raw_assertions total: 146
  existing OpenDART/event-board: 92
  Brain/Web attempt:             54

Brain/Web raw source:
  OpenDART structured API record: 8
  LLM contract-blind extraction: 46

Brain/Web raw anchor_verified=True: 54
Brain/Web claim mapping trace rows: 54
```

accepted claim 분해:

```text
accepted_claims total: 92
  source_provider=OpenDART: 92
  brain_web_origin present: 0

Brain/Web accepted claim: 0
Brain/Web score contribution: 0
Brain/Web StageCourt trace: 0
Brain/Web promoted census row: 0
```

중요:

```text
accepted_claims=92
!= 웹/LLM accepted claim 92개

StageCourt trace=92
!= Brain/Web StageCourt trace 92개
```

저 92개는 기존 OpenDART event-board 경로다.

## 감사 파일 판정

핵심 감사:

```text
leaf_artifact_audit.json:
  verdict: PASS

web_naver_acquisition_audit.json:
  verdict: REAL_ACQUISITION_PASS
  web_search_task_count: 4
  web_search_result_count: 40
  web_fetched_document_count: 8

llm_claim_extraction_audit.json:
  verdict: REAL_EXTRACTION_PASS
  llm_claim_extractor_attempt_count: 8
  llm_claim_extractor_real_provider_count: 8

brain_web_attempt_audit.json:
  verdict: ATTEMPTED_NOT_CUTOVER_READY
  brain_raw_assertion_exported_count: 54
  accepted_claim_count: 0
  brain_score_contribution_exported_count: 0
  brain_stagecourt_trace_exported_count: 0

brain_web_readiness_gate_audit.json:
  verdict: BLOCKED
  web_or_llm_accepted_claim_count: 0
  brain_score_contribution_count: 0
  brain_stage_trace_count: 0
  brain_promoted_stage_row_count: 0

readiness_verdict.json:
  verdict: NOT_READY
```

PASS 범위 해석:

```text
REAL_ACQUISITION_PASS
= 검색과 fetch가 실제로 일어났다.

REAL_EXTRACTION_PASS
= LLM extractor 호출과 raw assertion 생성이 실제로 일어났다.

BLOCKED / NOT_READY
= 그 결과가 아직 점수와 Stage로 들어갈 자격은 없다.
```

쉬운 예:

```text
도서관에 다녀온 것: PASS
책에서 메모한 것: PASS
그 메모가 시험 정답으로 인정된 것: 아직 FAIL
```

## Stage가 있는가

있다. 하지만 전부 `CENSUS_EVENT_BOARD`다.

```text
census_stage_status rows: 3391

stage_scope:
  CENSUS_EVENT_BOARD: 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

canonical_stage:
  0:      3306
  1:        54
  2:        30
  3-Red:     1

score_scope:
  NO_SCORE:                3324
  EVENT_WEIGHTED_PARTIAL:    67
```

따라서 정확한 답은 이렇다.

```text
Stage label은 있다.
하지만 full thesis operating Stage는 0개다.
Brain/Web promoted Stage row도 0개다.
```

쉬운 예:

```text
출석부에는 "대기", "검사 필요", "공시 확인" 같은 상태가 붙었다.
하지만 의사가 최종 진단서를 쓴 환자는 아직 없다.
```

## 삼성전자와 SK하이닉스

이번 enabled smoke의 삼성전자/하이닉스 row:

```text
SK하이닉스 000660:
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  full_thesis_stage: FULL_THESIS_NOT_RUN
  accepted_claim_ids: [CLM-14057362610ae62c7e02]
  score_contribution_ids: [SCON-8da68431606c7699ece3]

삼성전자 005930:
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  full_thesis_stage: FULL_THESIS_NOT_RUN
  accepted_claim_ids: [CLM-9aaf6a921e683a2ee9b4]
  score_contribution_ids: [SCON-02bb56e64083a9cd1389]
```

이 값은 HBM/C06 투자논리 Stage가 아니다.

`samsung_hynix_full_thesis_smoke.json`의 실제 상태:

```text
full_thesis_status: PENDING_FULL_THESIS_REFRESH
daily_event_and_full_thesis_separated: true

공통 missing_full_thesis_primitives:
  named_customer_or_customer_quality
  qualification_status
  capacity_allocation_or_pre_sold
  hbm_shipment_or_revenue_mix
  cash_or_revision_conversion
  repeat_evidence_family
  source_quorum

blocking_reason:
  full_thesis_source_tasks_planned_but_not_executed
```

쉬운 예:

```text
삼성전자에 "Stage1"이 보이는 것은
"오늘 공시/이벤트가 있어 출석 체크됨"이라는 뜻이다.

"HBM 논리로 90점/Yellow/Green을 다시 산정했다"는 뜻이 아니다.
```

## 패치 전과 패치 후 병목을 분리해야 한다

패치 전 병목:

```text
웹 검색/fetch/LLM leaf 자체가 0개이거나,
LLM raw assertion이 document/anchor/quote를 제대로 남기지 못했다.
```

패치 후 현재 병목:

```text
Brain/Web raw assertion은 54개 생겼고 anchor도 검증됐다.
하지만 accepted claim은 0개다.
```

현재 더 정확한 병목:

```text
1. Brain/Web adjudicated claim의 top-level document_id/anchor_id/source_provider가 이제 채워진다.
   최신 smoke에서 Brain/Web adjudicated claim 54개 모두 document_id와 anchor_id를 갖는다.

2. Brain/Web claim은 mapping_status가 ACCEPTED로 확정되지 않는다.
   accepted claim으로 올릴 primitive mapping이 없다.

3. 이제 rejected reason은 `brain_claim_mapping_trace.jsonl` 54줄로 claim 단위 확인이 가능하다.
   단, 이 trace를 planner feedback loop로 되돌리는 단계는 아직 남았다.

4. accepted Brain claim이 0개라 score contribution, StageCourt trace, brain_to_claim_trace가 모두 0이다.
```

현재 observed rejection 요약:

```text
brain_claim_mapping_trace rows: 54
trace_status:
  REJECTED_BEFORE_SCORE: 54
mapping_status:
  REJECTED: 54
primitive_gap:
  volume_growth_visible: 50
  official_disclosure_status_current: 4
source_provider:
  Naver web API: 35
  Naver news API: 11
  OpenDART: 8
rejection_reason:
  target_scope_not_direct:UNRELATED;mapping_not_accepted:REJECTED: 35
  mapping_not_accepted:REJECTED: 19
```

이제 다음 질문에는 답할 수 있다.

```text
어느 raw assertion이 어떤 primitive에 매핑 시도됐는가?
왜 REJECTED였는가?
그 rejection은 맞는가, 아니면 mapper가 너무 좁은가?
```

그래서 다음 패치는 accepted를 늘리는 것이 아니라, 이 rejected trace를 LLM planner feedback으로 되돌리는 것이다.

## 왜 accepted claim 0개가 맞을 수 있나

이번 Brain/Web 후보는 대웅/대웅제약의 공시와 웹 문서 중심이었다.

예를 들어 대웅 공시는 "신규시설투자 종료일 연장 / GMP 승인예정일 기준" 성격이다. 이 문서가 `volume_growth_visible`, `operating_leverage_visible`, `mix_improvement` 같은 primitive를 직접 채우지 못하면 accepted claim이 0개인 것이 맞다.

쉬운 예:

```text
시험 문제:
  "실제 매출 성장 근거가 있나?"

찾은 문서:
  "시설투자 종료일이 연장됐다."

정답:
  이 문서는 중요한 follow-up 자료일 수는 있지만,
  매출 성장 점수 칸에는 바로 넣으면 안 된다.
```

따라서 현재 `accepted claim 0`은 무조건 나쁜 것이 아니다.

나쁜 것은 아래 둘이다.

```text
1. 왜 0개인지 claim별로 설명하지 못하는 것.
2. positive source-backed fixture에서도 계속 0개가 나오는 것.
```

## 다음 패치 방향

### P0. rejected Brain/Web claim trace를 만든다

구현됨.

```text
brain_claim_mapping_trace.jsonl
```

최소 필드:

```text
raw_assertion_id
claim_id
source_task_execution_id
source_task_id
candidate_event_id
symbol
company_name
primitive_gap
document_id
source_document_id
anchor_id
source_anchor_id
source_url
source_provider
anchor_verified
quote_text 또는 exact_quote
target_scope_status
semantic_status
temporal_status
mapping_status
primitive_id
support_direction
mapping_rationale
eligibility_reasons
rejection_reason
accepted
score_eligible
```

목적:

```text
accepted claim이 0개여도 다음 에이전트가
"0개가 맞는지, mapper가 틀린지, planner가 잘못 물어본 건지"
바로 볼 수 있게 한다.
```

최신 smoke에서 검증된 값:

```text
brain_claim_mapping_trace.jsonl rows: 54
artifact_manifest row_count: 54
accepted=True rows: 0
REJECTED_BEFORE_SCORE rows: 54
```

### P1. source_task gap과 claim predicate mismatch를 planner feedback으로 되돌린다

현재는 source task가 실패하면 `NO_EVIDENCE_FOUND`로 끝난다.

목표는 아래처럼 구체적인 feedback이다.

```text
primitive_gap=volume_growth_visible
found_claim=facility end-date extension
mapping_status=REJECTED
reason=not revenue/volume realization
next_planner_feedback=look for production start, shipment volume, utilization, sales recognition
```

단, 이 feedback도 deterministic query template을 늘리는 방식이면 안 된다.

```text
나쁜 방식:
  if primitive_gap == volume_growth_visible:
      query = "{company} 매출 성장 가동률 출하량"

좋은 방식:
  LLM에게 rejected claim ledger와 missing primitive context를 보여 주고
  다음에 무엇을 찾아야 하는지 suggested_queries를 다시 생성시킨다.
```

### P2. positive source-backed fixture/live smoke를 만든다

지금 run은 accepted 0개가 맞을 수 있는 후보였다.

다음 검증에는 일부러 source-backed positive 문서를 넣어야 한다.

성공 조건:

```text
web/raw assertion
-> adjudicated claim
-> accepted Brain/Web claim
-> primitive state
-> score contribution
-> StageCourt trace
-> brain_to_claim_trace
-> strict promoted census_stage_status row
```

단, fixture 본문에 expected archetype id나 답안지를 넣으면 안 된다.

### P3. Brain/Web adjudicated claim의 ref 필드를 표준화한다

현재 Brain/Web adjudicated claim은 `source_document_id/source_anchor_id`는 있으나 top-level `document_id`가 null인 row가 있다.

accepted가 아니므로 아직 점수 누수는 아니지만, 다음 cutover 전에 정리해야 한다.

원칙:

```text
accepted 또는 rejected와 무관하게 claim trace에는 source_document_id/source_anchor_id를 보존한다.
accepted claim이 되려면 document_id/anchor_id 또는 동등한 resolved source ref가 반드시 있어야 한다.
```

### P4. 삼성전자/하이닉스 full thesis smoke를 daily event-board와 별도 실행한다

현재 row는 daily event-board Stage1이다.

다음 smoke는 아래를 별도로 닫아야 한다.

```text
C06/HBM source tasks
official/customer/IR/report/news acquisition
contract-blind extraction
target/current/semantic adjudication
primitive mapping
claim-backed score contribution ledger
StageCourt
score_valid_status
```

여기서도 LLM이 직접 점수나 Stage를 부르면 안 된다.

```text
LLM 역할:
  문서에서 claim 추출
  빠진 primitive를 찾기 위한 query 제안

deterministic 역할:
  anchor/date/entity/current/mapping 검증
  score contribution 계산
  StageCourt 판정
```

## 다음 에이전트 공격 질문

1. Brain/Web raw 54개 각각의 accepted/rejected 사유가 claim별 leaf로 보이는가?
2. rejected 사유가 source task execution 요약에만 있고 claim 단위로 사라지지는 않는가?
3. Brain/Web adjudicated claim의 `source_document_id/source_anchor_id`가 top-level `document_id/anchor_id`와 어떻게 연결되는가?
4. `llm_claim_extraction_audit=REAL_EXTRACTION_PASS`를 accepted claim pass로 오해할 수 있는 문구가 남아 있는가?
5. `accepted_claims=92`가 Brain/Web accepted claim으로 오해되지 않게 source provider/origin 분해가 같이 적혔는가?
6. 삼성전자/하이닉스 Stage1을 HBM full thesis Stage로 오해할 수 있는 출력이 남아 있는가?
7. full thesis smoke가 source task planned 상태를 pass로 세지는 않는가?
8. positive source-backed web fixture에서 accepted claim이 실제로 생기는가?
9. accepted Brain claim 없이 strict promotion이 가능한 우회 경로가 있는가?
10. deterministic fallback query template이 늘어나 LLM Research Brain 원칙을 깨지는 않는가?

## 현재 금지 label

아래 label은 아직 쓰면 안 된다.

```text
BRAIN_WEB_EVIDENCE_PASS
MEANINGFUL_OPERATIONAL_STAGE_PASS
FULL_THESIS_SMOKE_PASS
GOAL_COMPLETION_READY
SAMSUNG_HYNIX_C06_STAGE_COMPUTED
```

현재 허용 label:

```text
BRAIN_WEB_LEAFS_REAL_BUT_NOT_CUTOVER_READY
EVENT_BOARD_STAGE_LABELS_PRESENT
FULL_THESIS_NOT_RUN
STRICT_PROMOTION_BLOCKED_CORRECTLY
```

## 검증 명령

targeted 검증:

```text
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
  tests.test_census_v4_brain_bundle_export \
  tests.test_cutover_contract_blind_extraction \
  tests.test_cutover_v2_quote_anchor_validation \
  tests.test_research_brain_v4_evidence_extraction_from_real_document -v

Ran 78 tests in 32.170s
OK
```

전체 테스트는 최신 결과를 아래 칸에 계속 갱신한다.

```text
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 4959 tests in 156.646s
OK
log: /tmp/stock_agent_full_tests_after_mapping_trace_patch.log
```

## 최종 판단

지금 파이프라인이 잘못된 점수를 또 만든 상태는 아니다.

현재 문제는 더 좁다.

```text
웹/LLM 자료를 실제로 가져오고 읽는 데는 성공했다.
하지만 rejected/accepted 판단의 이유 장부가 부족하고,
positive source-backed claim이 Stage까지 닫히는 운영 예제가 아직 없다.
```

다음 패치는 점수를 올리는 패치가 아니다.

```text
다음 패치는 "왜 accepted가 0인지"를 claim 단위로 보이게 만들고,
정말 positive인 source-backed claim만 점수와 Stage로 통과시키는 패치다.
```
