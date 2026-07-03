# Census v4 0701 v34 Stage Truth Cross Validation and Source Lineage Patch

작성일: 2026-07-02 KST

## 0. 결론

질문은 두 개로 나눠야 한다.

```text
Stage가 있는 애들이 있나?
  있다. CENSUS_EVENT_BOARD 상태판 Stage는 3,391개 있고, 그중 비 Stage0은 85개다.

운영에서 쓸 FULL_THESIS 점수/Stage가 있나?
  없다. FULL_THESIS row는 0개, FULL_E2R_100 verified score row도 0개다.
```

쉬운 예:

```text
CENSUS_EVENT_BOARD Stage = 접수표
FULL_THESIS Stage = 의사가 서명한 진단서

접수표에는 "검사 필요", "관찰 필요" 같은 상태가 찍힐 수 있다.
하지만 그걸 최종 진단서라고 말하면 안 된다.
```

따라서 현재 삼성전자와 SK하이닉스를 이렇게 말하면 틀린다.

```text
삼성전자와 SK하이닉스는 운영 Stage1이다.
```

정확한 표현은 이것이다.

```text
삼성전자와 SK하이닉스는 CENSUS_EVENT_BOARD 상태판에서 Stage1/Official Event Watch로 보인다.
하지만 full_thesis_stage = FULL_THESIS_NOT_RUN,
full_thesis_verified_score = null 이므로 운영 점수/Stage는 아직 없다.
```

## 1. 이번 교차검증에서 바로잡은 문서 오류

`docs/0701/README.md` 상단이 서로 다른 실행의 숫자를 한 기준처럼 섞고 있었다.

분리해야 하는 기준은 다음이다.

```text
sourcequality-v28
  Brain/Web enabled attempt
  web/search/extractor 시도가 실제로 있음
  verdict = BLOCKED
  FULL_THESIS row = 0

provider-timeout-v30
  queue / timeout guard ledger-refresh verification
  brain_web_mode = disabled
  brain_web_readiness verdict = NOT_REQUESTED
  FULL_THESIS refresh queue = 85
  FULL_THESIS row = 0
```

이 둘을 섞으면 다음 같은 잘못된 문장이 나온다.

```text
v30 latest output에서 source_task_execution_count = 23이고 official_accepted_claim_count = 48이다.
```

실제 v30의 `brain_web_readiness_gate_audit.json`은 이렇게 말한다.

```text
brain_web_mode = disabled
source_task_execution_count = 0
official_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
verdict = NOT_REQUESTED
```

반대로 위 23/48/0 숫자는 v28 Brain/Web enabled diagnostic의 숫자다.

## 2. v30 상태판 Stage 교차검증

기준 산출물:

```text
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30
```

직접 확인 명령:

```bash
wc -l \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/census_stage_status.jsonl \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/full_thesis_refresh_queue.jsonl \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/atomic_stage_decisions.jsonl \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/claim_to_stage_trace.jsonl
```

결과:

```text
3391 census_stage_status.jsonl
85   full_thesis_refresh_queue.jsonl
92   atomic_stage_decisions.jsonl
3391 claim_to_stage_trace.jsonl
```

Stage scope 확인:

```bash
rg '"stage_scope": "CENSUS_EVENT_BOARD"' \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/census_stage_status.jsonl | wc -l

rg '"operator_stage_use": "NOT_FULL_THESIS_STAGE"' \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/census_stage_status.jsonl | wc -l

rg '"is_full_thesis_stage": true' \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/census_stage_status.jsonl | wc -l

rg -v '"full_e2r_verified_score": null' \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/census_stage_status.jsonl | wc -l
```

결과:

```text
CENSUS_EVENT_BOARD rows = 3391
NOT_FULL_THESIS_STAGE rows = 3391
is_full_thesis_stage true rows = 0
FULL_E2R verified score rows = 0
```

Stage 분포:

```bash
rg -o '"canonical_stage": "[^"]+"' \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/census_stage_status.jsonl \
  | sort | uniq -c
```

결과:

```text
3306 "canonical_stage": "0"
54   "canonical_stage": "1"
30   "canonical_stage": "2"
1    "canonical_stage": "3-Red"
```

이 85개 비 Stage0도 전부 운영 Stage가 아니다. 전부:

```text
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_stage = FULL_THESIS_NOT_RUN
verified_score = null
```

## 3. 삼성전자와 SK하이닉스 샘플

직접 확인 명령:

```bash
rg '"symbol": "(005930|000660)"' \
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/census_stage_status.jsonl
```

확인된 공통점:

```text
canonical_stage = 1
base_stage = Stage1
stage_scope = CENSUS_EVENT_BOARD
stage_signal = OFFICIAL_EVENT_WATCH
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
full_thesis_verified_score = null
verified_score = null
full_thesis_missing_primitives = full_thesis_refresh_task_not_run
```

쉬운 예:

```text
삼성전자/하이닉스는 "최근 공식 이벤트가 있으니 봐야 함" 상태다.
하지만 "HBM/C06 전체 thesis가 검증되어 87점, 92점, Green/Yellow" 같은 상태가 아니다.
```

이 구분을 못 하면 이전에 발생했던 문제가 반복된다.

```text
event score 4.0
  -> 제한적인 공식 이벤트 상태판 점수

FULL_E2R_100 verified score
  -> 아키타입별 accepted claim과 score contribution으로 닫힌 100점 스케일 점수
```

두 값은 서로 다른 체계다.

## 4. v28 Brain/Web attempt 교차검증

기준 산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v28
```

`brain_web_readiness_gate_audit.json` 핵심:

```text
brain_web_mode = enabled
llm_planner_call_count = 23
llm_real_provider_success_count = 3
source_task_execution_count = 23
official_accepted_claim_count = 48
web_search_task_count = 6
web_search_call_count = 6
web_search_result_count = 20
web_fetched_document_count = 1
web_rejected_document_count = 14
llm_claim_extractor_attempt_count = 1
web_or_llm_accepted_claim_count = 0
verdict = BLOCKED
```

`full_thesis_production_runner_audit.json` 핵심:

```text
production_mode_requested = true
candidate_row_count = 1
blocked_candidate_count = 1
promoted_full_thesis_row_count = 0
```

즉 v28은 Brain/Web을 켰지만 아직 막혔다.

쉬운 예:

```text
LLM 조사원이 실제로 검색하고 자료를 가져오려고 했다.
하지만 점수 칸에 들어갈 수 있는 web/LLM accepted claim은 0개였다.
그래서 FULL_THESIS 승격은 0개인 게 맞다.
```

## 5. v30 queue / timeout ledger-refresh 교차검증

기준 산출물:

```text
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30
```

`brain_web_readiness_gate_audit.json` 핵심:

```text
brain_web_mode = disabled
source_task_execution_count = 0
official_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
verdict = NOT_REQUESTED
```

`full_thesis_production_audit.json` 핵심:

```text
full_thesis_refresh_queue_candidate_count = 85
full_thesis_row_count = 0
production_full_thesis_row_count = 0
production_mode_requested = false
production_pass_allowed = false
verdict = PENDING_FULL_THESIS_PRODUCTION
```

`full_thesis_production_runner_audit.json` 핵심:

```text
candidate_row_count = 0
blocked_candidate_count = 0
promoted_full_thesis_row_count = 0
production_mode_requested = false
verdict = NOT_REQUESTED
```

주의:

```text
v30의 baseline/source_task_satisfaction 계열에는 source_task_execution_count = 92 같은 숫자가 보인다.
이건 기존 ledger/atomic decision 감사용 숫자다.
Brain/Web enabled attempt나 FULL_THESIS production promotion count가 아니다.
```

다음 에이전트는 반드시 파일별 의미를 나눠서 봐야 한다.

## 6. 이번 v34 코드 패치

문제:

```text
일반 웹/Naver 검색에서 NEWS 페이지를 가져왔다.
source_class가 TrustedNews, IndustryMedia, CompanyNewsroom, ReportPDF처럼 보인다.
그러면 "원문 또는 신뢰 커넥터가 확인한 source"처럼 오해될 수 있다.
```

이건 위험하다.

쉬운 예:

```text
네이버 검색으로 어떤 기사 URL을 찾았다.
그 기사 본문을 fetch했다.

하지만 이것만으로 "TrustedNews connector가 확인한 원문"은 아니다.
검색 결과 경유 URL일 뿐이다.
```

패치:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
```

추가한 rejection reason:

```text
source_lineage_unverified_original:<source_class>:general_web_search_provider
```

적용 대상:

```text
general web/Naver provider가 발견한 NEWS / RESEARCH_REPORT / IR 성격 문서
source_class:
  TrustedNews
  IndustryMedia
  News
  NaverSearch
  CompanyNewsroom
  ReportPDF
  BrokerReportPublicPDF
  IR
```

예외:

```text
DART / KIND / KRX / IssuerOfficial 공식 FILING 상세 원문은 막지 않는다.
```

쉬운 예:

```text
네이버가 찾은 일반 기사:
  source_lineage_unverified_original 때문에 score source 불가.

네이버가 찾았지만 URL이 kind.krx.co.kr 공식 공시 상세이고 document_type=FILING:
  공식 원문으로 인정 가능.
```

이건 종목명/아키타입/검색어 하드코딩이 아니다.
source가 점수 evidence로 들어갈 수 있는지의 입구 규칙이다.

## 7. 추가 테스트

수정 파일:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
docs/0701/README.md
docs/0701/census_v4_0701_v34_stage_truth_cross_validation_source_lineage_patch_2026-07-02.md
```

테스트가 고정한 케이스:

```text
1. 일반 웹에서 발견된 NEWS가 BrokerReportPublicPDF task를 만족하지 못한다.
   reason includes source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider

2. 일반 웹에서 발견된 IndustryMedia NEWS는 TrustedNews connector가 없으면 score source가 아니다.
   reason is also copied into web_rejected_documents.not_eligible_reasons

3. 공식+웹 병합 경로에서 NEWS 문서를 DART로 착각하지 않고 CompanyNewsroom fallback으로 검사한다.
   reason includes source_lineage_unverified_original:CompanyNewsroom:general_web_search_provider

4. 일반 웹에서 발견했더라도 KIND 공식 FILING 상세 원문이면 source_lineage_unverified_original을 붙이지 않는다.

5. post-extraction rejection row에도 source_lineage_unverified_original:TrustedNews:general_web_search_provider가 남는다.
```

## 8. 검증 결과

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_evidence_extraction_from_real_document -v
```

결과:

```text
Ran 16 tests
OK
```

확장 교차검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 120 tests
OK
```

전체 unittest:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5063 tests in 206.508s
OK
```

## 9. 이번 패치가 막은 것

막은 것:

```text
1. Naver/general web에서 발견된 NEWS를 TrustedNews original처럼 점수 source로 쓰는 회귀
2. 일반 웹 NEWS를 CompanyNewsroom/IndustryMedia로 느슨하게 인정하는 회귀
3. 일반 웹에서 발견된 report-like 문서를 BrokerReportPublicPDF/ReportPDF 원문처럼 쓰는 회귀
4. source lineage rejection reason이 web_rejected_documents에 남지 않는 회귀
5. KIND 공식 FILING 상세 원문까지 과하게 막는 회귀
```

막지 않은 것:

```text
1. 실제 TrustedNews connector 구현
2. 증권사 리포트 PDF 원문 connector 구현
3. 회사 newsroom 원문 connector 구현
4. FULL_THESIS production run 성공
5. web_or_llm accepted claim 생성
6. 삼성전자/하이닉스 FULL_E2R_100 verified score 산출
```

## 10. 다음 에이전트가 공격해야 할 질문

다음 리뷰어는 아래를 강하게 확인해야 한다.

```text
1. CENSUS_EVENT_BOARD 비 Stage0 85개가 운영 Stage로 출력되는 경로가 남아 있나?
2. EVENT_WEIGHTED_PARTIAL 점수가 FULL_E2R_100 점수처럼 노출되는 UI/API가 있나?
3. source_task_execution_count=92 같은 baseline 감사 숫자를 Brain/Web attempt 성공으로 오해하는 문서나 코드가 있나?
4. source_lineage_unverified_original reason이 planner feedback으로 충분히 전달되나?
5. 일반 웹에서 찾은 뉴스가 source_class만 바꿔 score source로 들어가는 우회 경로가 있나?
6. KIND/DART 공식 상세 URL은 이번 guard 때문에 막히지 않는가?
7. FULL_THESIS refresh queue 85개를 실제 production bounded mode로 돌릴 때 provider failure가 낮은 점수/Red로 확정되지 않는가?
8. 삼성전자/하이닉스 smoke가 상태판 Stage1을 운영 Stage처럼 설명하지 않는가?
```

## 11. 다음 패치 방향

우선순위는 다음이다.

```text
P0. 문서/출력 scope 혼동 제거
  CENSUS_EVENT_BOARD, EVENT_WEIGHTED_PARTIAL, FULL_THESIS, FULL_E2R_100을 모든 출력에서 분리한다.

P1. Source lineage 원문 커넥터
  TrustedNews / BrokerReportPublicPDF / CompanyNewsroom / IR 원문 route를 실제 connector 또는 verified resolver로 닫는다.

P2. FULL_THESIS refresh queue 실행
  queue 85개를 production bounded mode에서 돌리되, provider/source pending은 낮은 점수로 확정하지 않는다.

P3. Claim-backed score path 완결
  accepted claim -> primitive state -> score contribution -> StageCourt trace -> FULL_THESIS row가 모두 닫힐 때만 운영 Stage로 올린다.

P4. 삼성전자/하이닉스 bounded live smoke 재실행
  결과는 verified_score, score_status, source gaps, missing primitives로 보고한다.
  상태판 Stage1이나 provisional/event score를 운영 score처럼 말하지 않는다.
```

쉬운 예:

```text
다음 작업에서 삼성전자를 돌렸는데 DART 이벤트 하나만 닫혔다.
  -> Stage1 운영 확정이 아니라 CENSUS_EVENT_BOARD Official Event Watch다.

HBM customer allocation, revenue/margin bridge, revision/cashflow claim이 accepted claim으로 닫혔다.
그리고 source family와 Green gate가 통과됐다.
  -> 그때부터 FULL_THESIS 점수/Stage를 말할 수 있다.
```

## 12. 최종 현재 진실표

```text
날짜: 2026-07-02 KST

상태판 Stage:
  있음
  rows = 3391
  non_Stage0 = 85

운영 FULL_THESIS Stage:
  없음
  rows = 0

FULL_E2R_100 verified score:
  없음
  rows = 0

FULL_THESIS refresh queue:
  있음
  rows = 85

Brain/Web enabled attempt:
  v28에서 있음
  verdict = BLOCKED
  web_or_llm_accepted_claim_count = 0

Queue/timeout ledger-refresh:
  v30에서 있음
  Brain/Web = disabled / NOT_REQUESTED
  queue rows = 85

이번 v34 패치:
  일반 웹/Naver-discovered NEWS/IR/report-like 문서가 원문 lineage 검증 없이 score source로 들어가는 경로를 막음

운영 readiness:
  NOT_READY
```
