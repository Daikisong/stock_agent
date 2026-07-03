# Census v4 0701 v82 VerifiedReportOriginal Route Whitelist / Stage Truth Cross-Validation

작성일: 2026-07-03

대상 실행:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82
```

## 0. 최종 결론

최신 v82 기준:

```text
verdict = NOT_READY
operational_stage_use_allowed = false
FULL_THESIS 운영 Stage row = 0
FULL_E2R_100 운영 점수 row = 0
CENSUS_EVENT_BOARD row = 3,390
BRAIN_WEB_PARTIAL row = 1
```

즉 Stage row는 있다. 하지만 운영자가 써도 되는 Stage는 없다. 최신 v82의 유일한 Brain/Web 부분 행도 `operator_stage_use=NOT_FULL_THESIS_STAGE`, `operator_score_use=NOT_FULL_E2R_SCORE`라 운영 Stage/점수가 아니다.

쉬운 예:

```text
CENSUS_EVENT_BOARD
  = 출석부. 전 종목을 한 번 봤다는 상태판이다.

BRAIN_WEB_PARTIAL
  = 몇 문제만 풀린 쪽지시험이다.

FULL_THESIS
  = 최종 성적표다.
```

v82에는 출석부와 SK하이닉스 쪽지시험 1개가 있지만, 최종 성적표는 0개다.

따라서 삼성전자/하이닉스에 대해 지금 말할 수 있는 것은:

```text
full thesis source task는 계획됐지만 실행/채점이 닫히지 않았다.
```

말하면 안 되는 것:

```text
삼성전자 운영 Stage 몇, 운영 점수 몇
SK하이닉스 운영 Stage 몇, 운영 점수 몇
```

## 1. v80/v81은 최신이 아니다

중간 실행의 진실표가 흔들렸다.

```text
v80: BRAIN_WEB_PARTIAL 1개
v81: BRAIN_WEB_PARTIAL 0개
v82: BRAIN_WEB_PARTIAL 1개
```

이 차이는 live web/search/LLM 경로가 bounded smoke 안에서 다른 문서를 잡거나 다른 claim을 통과시키기 때문이다. 하지만 변하지 않는 핵심은 하나다.

```text
FULL_THESIS = 0
FULL_E2R_100 = 0
operator_stage_use = NOT_FULL_THESIS_STAGE for all rows
```

즉 v80/v81/v82 어느 쪽도 production-ready가 아니다. 최신 문서에서는 v82만 truth로 쓴다.

## 2. v82 실행 조건

`run_metadata.json` 기준:

```text
as_of_date = 2026-07-01
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode = enabled
brain_source_acquisition = live_full_bounded
brain_universe_limit = 1
brain_planner_success_limit = 1
brain_planner_batch_size = 1
brain_max_source_tasks_per_plan = 3
brain_max_fetches_per_task = 1
brain_claim_extractor_timeout_seconds = 120
brain_stage_promotion_mode = strict
target_gate = brain_web
```

CLI 결과:

```text
LIVE_RC = 1
NOT_READY
```

이 `NOT_READY`는 실패를 숨기는 값이 아니다. 운영 기준을 못 넘었기 때문에 실패 종료가 맞다.

## 3. Stage Row Truth

`census_stage_status.jsonl` 기준:

| 항목 | count |
|---|---:|
| stage rows | 3,391 |
| `CENSUS_EVENT_BOARD` | 3,390 |
| `BRAIN_WEB_PARTIAL` | 1 |
| `FULL_THESIS` | 0 |
| `operator_stage_use=NOT_FULL_THESIS_STAGE` | 3,391 |
| `operator_score_use=NOT_FULL_E2R_SCORE` | 3,391 |
| `full_thesis_stage=FULL_THESIS_NOT_RUN` | 3,391 |

`canonical_stage` 분포:

| canonical_stage | count | 운영 해석 |
|---|---:|---|
| `0` | 3,306 | Census 상태판 / NoCurrentCatalyst 성격 |
| `1` | 54 | event board 또는 partial 성격 |
| `2` | 30 | event board 성격 |
| `3-Red` | 1 | event board 성격 |

유일한 `BRAIN_WEB_PARTIAL` row:

```json
{
  "symbol": "000660",
  "company_name": "SK하이닉스",
  "canonical_stage": "1",
  "base_stage_display": "BRAIN_WEB_PARTIAL_1",
  "stage_scope": "BRAIN_WEB_PARTIAL",
  "operator_stage_use": "NOT_FULL_THESIS_STAGE",
  "operator_score_use": "NOT_FULL_E2R_SCORE",
  "event_evidence_score": 60.0,
  "verified_score": null,
  "accepted_claim_count": 3,
  "score_contribution_count": 6,
  "full_thesis_stage": "FULL_THESIS_NOT_RUN",
  "is_full_thesis_stage": false,
  "is_full_e2r_score": false,
  "score_scope": "BRAIN_WEB_CLAIM_BACKED_PARTIAL",
  "score_scale": "EVENT_WEIGHTED_PARTIAL"
}
```

이 행은 "SK하이닉스 운영 Stage 1"이 아니다. 정확한 해석은 "Brain/Web이 source-backed claim 일부를 score contribution으로 연결했지만, full thesis refresh가 닫히지 않아 운영 Stage로 쓸 수 없다"이다.

## 4. Readiness Blockers

`readiness_verdict.json` / `brain_web_readiness_gate_audit.json`:

```text
Brain/Web operational minimum planner runs not met: 21/30
Brain/Web operational minimum web search tasks not met: 3/20
Brain/Web operational minimum web/news search calls not met: 3/20
Brain/Web operational minimum fetched documents not met: 1/10
Brain/Web operational minimum claim extractor attempts not met: 1/10
```

주요 감사 파일:

| artifact | verdict/status | 의미 |
|---|---|---|
| `readiness_verdict.json` | `NOT_READY` | 운영 허용 불가 |
| `brain_web_readiness_gate_audit.json` | `BLOCKED` | Brain/Web 운영 최소치 미달 |
| `brain_stage_promotion_audit.json` | `PROMOTION_APPLIED` | 부분 행 1개가 stage status에 반영됨 |
| `leaf_artifact_audit.json` | `PASS`, critical 0 | leaf artifact 자체는 깨지지 않음 |
| `primitive_state_chain_audit.json` | `PASS`, critical 0 | 대표 primitive chain은 통과 |
| `source_task_satisfaction_audit.json` | `PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION`, critical 0 | ledger refresh chain은 통과 |
| `runtime_plausibility_audit.json` | `PASS_LIVE_RUNTIME_PLAUSIBILITY`, critical 0 | live run 자체 과장 없음 |
| `full_thesis_production_audit.json` | `PENDING_FULL_THESIS_PRODUCTION` | full thesis 생산 불가 |

쉬운 예:

```text
쪽지시험 한 장은 채점됐다.
하지만 기말고사 채점이 끝나지 않았고, 운영 성적표는 발급되지 않았다.
```

따라서 `PROMOTION_APPLIED`를 production-ready로 읽으면 안 된다.

## 5. Web / LLM / Claim Counts

v82 live Brain/Web leaf:

| leaf | count |
|---|---:|
| `web_search_tasks.jsonl` | 3 |
| `web_search_results.jsonl` | 19 |
| `web_fetched_documents.jsonl` | 1 |
| `web_rejected_documents.jsonl` | 15 |
| `claim_extractor_runs.jsonl` | 1 |
| `brain_to_claim_trace.jsonl` | 5 |

`llm_claim_extraction_audit.json`:

```text
verdict = REAL_EXTRACTION_PASS
llm_claim_extractor_attempt_count = 1
llm_claim_extractor_real_provider_count = 1
llm_claim_extractor_provider_error_count = 0
llm_claim_extractor_timeout_count = 0
provider_name = codex_cli_contract_blind_extractor
```

`brain_to_claim_trace.jsonl`:

```text
CLAIM_SCORE_TRACE_PROMOTED_TO_CENSUS_STAGE_STATUS = 3
ACCEPTED_NON_REPRESENTATIVE_NOT_SCORE_CONTRIBUTING = 2
```

`web_fetched_documents.jsonl`:

```text
https://stock.pstatic.net/stock-research/company/17/20251031_company_162545000.pdf
verified_report_original = true
```

이 문서는 리포트 원문 URL로 인정됐다. 하지만 만들어진 것은 SK하이닉스 `BRAIN_WEB_PARTIAL` 부분 행이지, full thesis가 아니다.

## 6. VerifiedReportOriginal Route Whitelist

이번 패치의 목적은 일반 웹 검색이나 stored snapshot이 브로커 리포트 원문처럼 위장해 score 경로를 여는 것을 막는 것이다.

막은 공격:

```text
1. host spoof
   https://samsungpop.com.evil.com/research/fake-report.pdf

2. path spoof
   https://evil.example/samsungpop.com/research/fake-report.pdf

3. same-host broad path false positive
   https://www.samsungpop.com/support/report-center/fake.pdf

4. same-host query spoof
   https://www.samsungpop.com/support/download?saveKey=research.pdf&fileName=fake.pdf&contentType=application/pdf

5. same-host common.do query spoof
   https://www.samsungpop.com/common.do?next=research.pdf&contentType=application/pdf

6. cross-host route prefix leak
   https://www.samsungpop.com/media/pdfs/fake.pdf

7. stored snapshot spoof
   data/report_snapshots/report_snapshots.jsonl 에 fake URL을 넣고 BrokerReportPublicPDF처럼 통과

8. forged source_lineage marker
   source_lineage_id에 verified_report_original:broker_report_domain:... 문자열만 삽입
```

핵심 변경:

| 파일 | 변경 |
|---|---|
| `src/e2r/sources/report_search.py` | URL substring이 아니라 parsed hostname/path로 domain 판정 |
| `src/e2r/sources/report_search.py` | broad `"/research"`, `"/report"` path hint 제거 |
| `src/e2r/sources/report_search.py` | path prefix는 host별로만 허용 |
| `src/e2r/sources/report_search.py` | 삼성증권 `common.do`는 `cmd=down`, `saveKey=research.pdf`, PDF `fileName`, `contentType=application/pdf`가 모두 있어야 허용 |
| `src/e2r/sources/report_search.py` | title의 `customer/event/product`는 non-report 차단에 쓰지 않고 URL path/query만 본다 |
| `src/e2r/research_brain/v4_source_acquisition_runner.py` | web result와 stored report snapshot 모두 verified report URL을 통과해야 VerifiedReportOriginal |
| `src/e2r/research_brain/v4_evidence_extraction_bridge.py` | stored snapshot/provider marker만으로 score admissible 되지 않게 차단 |

정상 허용 예:

```text
https://stock.pstatic.net/stock-research/company/...pdf
https://stock.pstatic.net/stock-research/industry/...pdf
https://ssl.pstatic.net/imgstock/upload/research/...pdf
https://file.hanaw.com/download/research/...pdf
https://www.samsungpop.com/common.do?cmd=down&contentType=application/pdf&saveKey=research.pdf&fileName=...pdf
```

차단 예:

```text
https://www.samsungpop.com/customer/event_terms.pdf
https://www.samsungpop.com/privacy.pdf
https://www.samsungpop.com/support/report-center/fake.pdf
https://www.samsungpop.com/support/download?saveKey=research.pdf&fileName=fake.pdf&contentType=application/pdf
https://www.samsungpop.com/common.do?next=research.pdf&contentType=application/pdf
https://www.samsungpop.com/media/pdfs/fake.pdf
https://samsungpop.com.evil.com/research/fake-report.pdf
https://evil.example/samsungpop.com/research/fake-report.pdf
```

tradeoff:

```text
일부 정상 증권사 리포트 route를 놓칠 수 있다.
하지만 운영 점수에서는 false negative가 false positive보다 낫다.
놓친 route는 broad path를 다시 열지 말고 증권사별 원문 route registry로 추가해야 한다.
```

## 7. Tests

타깃 회귀:

```text
Ran 8 tests in 0.072s
OK
```

관련 묶음:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_primitive_state_chain \
  tests.test_census_v4_source_task_satisfaction_chain \
  tests.test_sources -v

Ran 125 tests in 9.580s
OK
```

전체 suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5120 tests in 226.372s
OK
```

v82 live smoke:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82

LIVE_RC=1
NOT_READY
```

## 7.1 최종 교차검증

서브에이전트 최종 재공격 결과:

```text
No High/Medium findings.
```

확인된 내용:

```text
1. /support/download?...saveKey=research.pdf spoof = false
2. /common.do?next=research.pdf spoof = false
3. /media/pdfs/fake.pdf cross-host route leak = false
4. 정상 삼성증권 common.do download route = true
5. 정상 pstatic stock-research URL + customer allocation title = true
6. stored snapshot도 verified URL 없이는 통과 불가
7. forged source_lineage marker 단독으로 score admissible 불가
8. v82 stage truth는 산출물과 일치
```

남는 tradeoff:

```text
m.ibks.com, kiwoom.com, miraeasset.com 등 recognized domain 중 일부는
아직 verified route whitelist가 없어서 원문 리포트로 열리지 않는다.
이건 recall 손실 가능성이지만, 현재 source integrity hardening 목적상
즉시 broad path를 다시 열 문제는 아니다.
```

다음에 정상 리포트 false negative를 줄일 때도 broad `"/report"`/`"/research"`를 되살리면 안 된다. 증권사별 실제 다운로드 route를 registry로 추가해야 한다.

## 8. 삼성전자 / SK하이닉스 Full Thesis Smoke

`samsung_hynix_full_thesis_smoke.json`:

```text
full_thesis_status = PENDING_FULL_THESIS_REFRESH
daily_event_and_full_thesis_separated = true
hardcoded_query_count = 0
```

SK하이닉스:

```text
daily_event_claim_ids = 3
daily_event_score_contribution_ids = 6
full_thesis_claim_ids = []
full_thesis_score_contribution_ids = []
full_thesis_source_task_ids = 7 planned
blocking_reason = full_thesis_source_tasks_planned_but_not_executed
missing_full_thesis_primitives = full_thesis_refresh_task_not_run
smoke_pass_allowed = false
```

삼성전자:

```text
daily_event_claim_ids = 1
daily_event_score_contribution_ids = 1
full_thesis_claim_ids = []
full_thesis_score_contribution_ids = []
full_thesis_source_task_ids = 7 planned
blocking_reason = full_thesis_source_tasks_planned_but_not_executed
missing_full_thesis_primitives = full_thesis_refresh_task_not_run
smoke_pass_allowed = false
```

해석:

```text
daily event와 partial claim은 일부 있다.
full thesis source task는 계획만 됐다.
full thesis claim/score/stagecourt trace는 없다.
따라서 운영 점수와 Stage를 말하면 안 된다.
```

## 9. All-Archetype Replay Truth

`all_archetype_replay_matrix.json`:

```text
all_archetype_replay_pass = false
required_archetype_count = 32
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
source_proxy_leak_count = 0
```

좋은 점:

```text
source_proxy_only 연구자료가 운영 claim으로 새어 들어간 흔적은 없다.
```

부족한 점:

```text
32개 필수 아키타입 전체 source-backed replay parity는 아직 아니다.
현재 준비된 것은 6/32다.
```

## 10. 다음 패치 방향

가장 먼저 해야 할 일은 weight/threshold 조정이 아니다.

필수 chain:

```text
FULL_THESIS_REFRESH_TASK_PLANNED
  -> SOURCE_TASK_EXECUTED
  -> ACCEPTED_CLAIM
  -> PRIMITIVE_STATE
  -> SCORE_CONTRIBUTION
  -> STAGECOURT_TRACE
  -> FULL_THESIS row
```

현재 끊긴 곳:

```text
full_thesis_source_task_ids = planned
full_thesis_claim_ids = []
full_thesis_score_contribution_ids = []
full_thesis_stagecourt_trace_ids = []
```

다음 작업:

```text
1. 삼성전자/하이닉스 full thesis source task를 실제 실행한다.
2. accepted claim / primitive / score contribution / StageCourt trace를 닫는다.
3. FULL_THESIS row가 아니면 operator output에 점수와 Stage를 운영값처럼 내보내지 않는다.
4. Brain/Web operational minimum을 만족하도록 bounded planner/search/fetch/extractor를 충분히 돌린다.
5. all-archetype source-backed replay parity를 32개 필수 아키타입 전체로 확장한다.
6. 증권사 리포트 false negative는 broad path가 아니라 route registry로 고친다.
```

## 11. Reviewer Attack Checklist

다음 에이전트는 최소 이 질문으로 공격하면 된다.

```text
1. `BRAIN_WEB_PARTIAL`을 운영 Stage처럼 말하고 있지 않은가?
2. `event_evidence_score=60.0`을 `FULL_E2R_100` 점수처럼 말하고 있지 않은가?
3. `operator_stage_use=NOT_FULL_THESIS_STAGE`인 row를 operator-facing Stage로 노출하고 있지 않은가?
4. `PROMOTION_APPLIED`를 `PRODUCTION_READY`처럼 오독하고 있지 않은가?
5. stored report snapshot이 verified original URL 없이 score로 들어갈 수 없는가?
6. source_lineage marker 문자열만으로 score admissible이 되지 않는가?
7. host/path/query spoof URL 6종이 모두 막히는가?
8. 정상 네이버 stock-research 리포트가 title의 customer allocation 때문에 false negative 되지 않는가?
9. 삼성전자/하이닉스 full thesis task planned 상태를 full thesis complete로 오독하고 있지 않은가?
10. all-archetype replay 6/32를 완료라고 말하고 있지 않은가?
```

## 12. 최종 판단

이번 패치로 개선된 것:

```text
host spoof 차단
path spoof 차단
same-host broad path false positive 차단
same-host query spoof 차단
common.do arbitrary query spoof 차단
cross-host route prefix leak 차단
stored snapshot spoof 차단
source_lineage marker 단독 신뢰 차단
title의 customer/event/product로 정상 리포트가 막히는 false negative 완화
```

아직 완료되지 않은 것:

```text
운영 FULL_THESIS Stage 생성
삼성전자/하이닉스 full thesis smoke 통과
Brain/Web operational minimum counts 통과
32개 필수 아키타입 source-backed replay parity
```

최신 v82를 한 문장으로 고정하면:

```text
Evidence OS source integrity는 더 안전해졌지만, 운영용 FULL_THESIS Stage는 아직 0개다.
```
