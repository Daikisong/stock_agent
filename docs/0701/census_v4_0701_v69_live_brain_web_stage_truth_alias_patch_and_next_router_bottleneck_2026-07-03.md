# Census v4 0701 v69 Live Brain/Web Stage Truth, Alias Patch, and Next Router Bottleneck

작성일: 2026-07-03

## 한 줄 결론

`2026-07-01` Census v4에는 아직 운영용 `FULL_THESIS` Stage가 없다.

상태판 메모는 있다. 하지만 운영자가 써도 되는 Stage는 아직 0개다.

쉽게 말하면:

```text
출석부에는 "이 학생은 관찰 대상"이라고 적혀 있다.
하지만 시험지는 아직 채점되지 않았다.
따라서 점수와 등급을 발표하면 안 된다.
```

## 왜 이 문서를 남기나

이 문서는 다음 에이전트가 빡세게 공격할 수 있게 만든 v69 감사 패킷이다.

확인한 핵심 질문은 네 가지다.

```text
1. stage가 있는 애들이 있나?
2. v68/v69 live Brain/Web 실행은 어디까지 갔나?
3. 이번 패치가 무엇을 고쳤고 무엇을 고치지 않았나?
4. 다음 패치는 어디부터 건드려야 하나?
```

## Stage 존재 여부

v69 기준:

```text
artifact:
  output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v69

census_stage_status.jsonl:
  rows: 3391
  stage: None 3391
  stage_scope: CENSUS_EVENT_BOARD 3391
  operator_stage_use: NOT_FULL_THESIS_STAGE 3391
  base_stage memo:
    Stage0: 3306
    Stage1: 54
    Stage2-Watch: 30
    Red: 1

census_stage_summary.json:
  FULL_THESIS rows: 0
  FULL_E2R_100 verified score rows: 0
  verified_score_present_count: 0
```

해석:

```text
Stage0 / Stage1 / Stage2-Watch / Red 메모는 Census Event Board 상태값이다.
이 값은 운영 Stage가 아니다.
운영 Stage는 stage 필드에 들어가야 하는데, 현재 전부 None이다.
```

예:

```text
삼성제약에 Stage1 메모가 있다
  -> "관찰 상태판에서 Stage1 후보처럼 보인다"는 뜻

삼성제약 stage = None
  -> "FULL_THESIS 운영 Stage는 아직 없다"는 뜻
```

따라서 현재 답은 분명하다.

```text
stage가 있는 애들이 있긴 해?
  -> 운영 Stage 기준으로는 없다.
  -> 상태판 메모 기준으로는 있다.
  -> 운영에 써도 되는 FULL_THESIS Stage는 0개다.
```

## v68와 v69 비교

| 항목 | v68 | v69 |
| --- | ---: | ---: |
| artifact | `2026-07-01-real-brain-web-live-full-bounded-v68` | `2026-07-01-real-brain-web-live-full-bounded-v69` |
| 최종 verdict | `BLOCKED / NOT_READY` | `BLOCKED / NOT_READY` |
| web_search_task_count | 5 | 3 |
| web_search_call_count | 5 | 3 |
| web_fetched_document_count | 2 | 0 |
| claim_extractor_runs | 2 | 0 |
| claim_extractor_success | 1 | 0 |
| claim_extractor_provider_error | 1 | 0 |
| web_or_llm_accepted_claim_count | 0 | 0 |
| brain_promoted_stage_row_count | 0 | 0 |
| full_thesis_claim_count | 0 | 0 |
| census_stage_status.stage | `None` 3391개 | `None` 3391개 |

중요한 차이:

```text
v68:
  full-source web document 2개를 fetch했다.
  LLM claim extractor도 2회 시도했다.
  그러나 accepted web/LLM claim은 0개였다.

v69:
  web search는 됐다.
  하지만 full-source fetch가 0개라 LLM claim extractor까지 가지 못했다.
```

즉 v69는 v68보다 점수가 좋아지거나 나빠진 실행이 아니다.
입력 문서 단계가 달라졌기 때문에 Stage 비교 실행으로 보면 안 된다.

## v68에서 발견한 실제 문제

v68에서는 다음 문서가 fetch됐다.

```text
DOC-dcf47af35a721bbad33a
  title: SK Hynix 000660 - Research Report | Mirae Asset Securities
  url: https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2338176

DOC-e85626d82f3e295486db
  title: SK hynix newsroom / HPE Discover 2026
  url: https://news.skhynix.co.kr/hpe-discover-2026/
```

Mirae 리포트에서는 LLM extractor가 성공했고 raw assertion 14개를 만들었다.
그런데 13개가 `UNRELATED`로 adjudication rejected 됐다.

대표 예:

```json
{
  "subject": "SK Hynix",
  "predicate": "revision_claim",
  "exact_quote": "We maintain our Buy rating on SK Hynix and raise our target price by 12% to W1,540,000 (from W1,370,000).",
  "target_entity_id": "TICKER:000660",
  "target_scope_status": "UNRELATED"
}
```

이건 사람이 보면 틀렸다.

```text
리포트 제목: SK Hynix 000660
대상 티커: 000660
원문 주체: SK Hynix

정상 판정:
  target_scope_status = DIRECT

기존 판정:
  target_scope_status = UNRELATED
```

원인은 단순했다.

```text
기존 target_aliases:
  SK하이닉스
  000660
  SK하이닉스(000660)
  SK하이닉스 (000660)

원문 subject:
  SK Hynix

결과:
  문자열 exact match 실패
  wrong subject로 탈락
```

## 이번 v69 전 패치 내용

### 1. Entity adjudication alias 정규화

파일:

```text
src/e2r/production/claim_extraction/entity_temporal_adjudicator.py
```

변경:

```text
기존:
  assertion.subject in set(target_aliases)

변경:
  casefold
  공백/구두점 제거
  Co / Corp / Inc / Ltd 등 영문 법인 suffix 제거
  정규화된 subject와 정규화된 alias 비교
```

쉬운 예:

```text
target_aliases = ("SK hynix Inc.", "000660")
subject = "SK Hynix"

기존:
  "SK Hynix" != "SK hynix Inc."
  -> wrong subject

변경:
  skhynix == skhynix
  -> DIRECT
```

### 2. 웹 fetch row title에서 안전한 영어 별칭 보강

파일:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
```

변경:

```text
문서/검색결과 title 안에 target ticker가 함께 있을 때만
영어 회사명 후보를 target_aliases에 추가한다.
```

예:

```text
title = "SK Hynix 000660 - Research Report | Broker"
symbol = "000660"

추가 alias:
  SK Hynix
```

반대로 이건 안 된다.

```text
본문 어딘가에 SK Hynix가 등장했다.
하지만 title에 000660이 없다.

-> target alias로 승격하지 않는다.
```

이유:

```text
삼성전자 기사에 월덱스, SK Hynix, Nvidia가 언급됐다고
그 회사들을 삼성전자 alias로 삼으면 다시 wrong-subject hard break가 터진다.
```

### 3. claim quote 출력 보정

파일:

```text
src/e2r/census/census_runner_v4.py
```

변경:

```text
adjudicated_claims / brain_claim_mapping_trace / accepted_claim payload에서
quote_text는 anchor 전체 텍스트보다 raw_assertion.exact_quote를 우선 사용한다.
```

이유:

```text
anchor가 리포트 전체 본문이면 quote_text가 너무 길어져서
"어느 문장 때문에 claim이 생겼는지"를 감사하기 어렵다.
```

쉬운 예:

```text
나쁜 출력:
  리포트 전체 첫 500자

좋은 출력:
  We maintain our Buy rating on SK Hynix...
```

단, 구조화 signal 쪽은 raw assertion 자체가 anchor 기반으로 만들어지는 경우가 있어
아직 quote가 길게 남을 수 있다. 이건 다음 별도 패치 대상이다.

## 이번 패치가 일부러 하지 않은 것

중요하다.

```text
이번 패치는 점수를 올리지 않았다.
Green/Yellow/Red gate를 건드리지 않았다.
general web source lineage guard를 풀지 않았다.
BrokerReportPublicPDF를 일반 검색 결과만으로 score source로 인정하지 않았다.
```

예:

```text
SK Hynix 000660 리포트가 general web search로 발견됐다.
subject는 DIRECT로 고친다.
하지만 원출처/connector lineage가 검증되지 않으면 점수에는 안 들어간다.
```

이게 맞다.

```text
주체 판정 오류를 고치는 것
  -> 필요

일반 검색 리포트를 바로 점수로 열어 주는 것
  -> 위험
```

## 추가한 테스트

### Focused tests

```bash
PYTHONPATH=src python -m unittest tests.test_structured_api_claim_requires_adjudication -v
```

결과:

```text
Ran 2 tests
OK
```

핵심 추가 테스트:

```text
test_english_alias_matching_is_case_and_suffix_normalized
```

검증:

```text
subject = SK Hynix
target_aliases = SK hynix Inc., 000660
-> DIRECT / PASS
```

### Evidence extraction focused tests

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_evidence_extraction_from_real_document -v
```

결과:

```text
Ran 19 tests
OK
```

핵심 추가 테스트:

```text
test_web_title_symbol_alias_maps_english_subject_without_unlocking_general_search_score
```

검증:

```text
title = SK Hynix 000660 - Research Report | Broker
subject = SK Hynix
target = 000660 / SK하이닉스

기대:
  target_scope_status = DIRECT

동시에 기대:
  accepted_claim_ids = []
  source_lineage_unverified_original:BrokerReportPublicPDF:general_web_search_provider

즉:
  wrong subject는 고치지만
  general search 리포트는 점수로 열지 않는다.
```

### Bundle export tests

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_bundle_export -v
```

결과:

```text
Ran 8 tests
OK
```

핵심 추가 검증:

```text
adjudicated_claims.quote_text == raw_assertions.exact_quote
brain_claim_mapping_trace.quote_text == raw_assertions.exact_quote
```

### Related wider tests

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_structured_api_claim_requires_adjudication \
  -v
```

결과:

```text
Ran 21 tests
OK
```

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 61 tests
OK
```

## v69 live smoke command

```bash
rm -rf output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v69
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 \
E2R_CODEX_EXTRACTOR_TIMEOUT_SECONDS=120 \
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v69 \
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

결과:

```text
exit code: 1
stdout: NOT_READY
```

이건 좋은 결과는 아니지만, 정직한 결과다.
full-source web document가 없고 web/LLM accepted claim도 없으므로 Stage를 만들면 안 된다.

## v69 audit 핵심

### brain_web_readiness_gate_audit.json

```text
verdict: BLOCKED

blockers:
  - Brain/Web acquisition mode requires fetched full-source web/news documents
  - web/LLM accepted claim count is zero
  - Brain/Web StageCourt traces are not promoted into census_stage_status
  - brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
  - Brain/Web operational minimum planner runs not met: 22/30
  - Brain/Web operational minimum web search tasks not met: 3/20
  - Brain/Web operational minimum web/news search calls not met: 3/20
  - Brain/Web operational minimum fetched documents not met: 0/10
  - Brain/Web operational minimum claim extractor attempts not met: 0/10
  - Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

### web_naver_acquisition_audit.json

```text
verdict: WEB_RESULTS_ONLY_NOT_FETCHED
```

해석:

```text
검색 결과는 있었지만,
full-source 문서로 fetch된 것이 없다.
```

### llm_claim_extraction_audit.json

```text
verdict: FAIL
claim_extractor_runs: 0
```

해석:

```text
LLM extractor가 실패한 것이 아니다.
extractor까지 갈 full-source document가 없었다.
```

### brain_stage_promotion_audit.json

```text
verdict: BLOCKED

blockers:
  - web/LLM accepted brain claim count is zero for BRAIN_WEB_PARTIAL promotion
  - brain StageCourt traces have no web/LLM accepted claim support: 1
```

해석:

```text
StageCourt trace는 있어도 web/LLM accepted claim support가 없으면
운영 Stage로 승격하지 않는다.
```

이 차단은 맞다.

## v69 web path 세부

```text
web_search_tasks.jsonl:
  rows: 3

web_search_results.jsonl:
  rows: 27
  SELECTED_FOR_FETCH: 4
  REJECTED_TARGET_RELEVANCE_AFTER_FETCH: 9
  REJECTED_NON_EVIDENCE_RESULT_METADATA: 13
  REJECTED_DUPLICATE_WEB_RESULT: 1

web_rejected_documents.jsonl:
  rows: 27
  live_fetch_failed:HTTPError:HTTP Error 403: Forbidden: 4
  web_fetch_target_not_found_in_full_text: 5
  web_fetch_target_not_in_title_snippet_or_lead: 4
  web_result_site_archive_or_sitemap_not_source_document: 7
  web_result_stock_list_or_channel_page_not_source_document: 5
  duplicate_web_result_url_not_refetched: 1
  web_result_low_quality_blog_or_social_not_score_source: 1

web_fetched_documents.jsonl:
  rows: 0
```

대표로 선택된 결과:

```text
query:
  삼성제약 001360 회사 뉴스룸 계약 생산 매출 수익성 2026

selected:
  Investing.com market news pages
  Investing.com S&S Tech stock news/profile pages

rejection:
  403 Forbidden
  target not found
  stock quote/profile page
```

해석:

```text
Source Router가 "증거 문서"가 아니라 "검색 결과에서 상위에 걸린 시장/시세/아카이브 페이지"를
fetch 후보로 뽑고 있다.
```

이건 다음 P0다.

## 현재 병목 지도

## 교차검증 추가 지적

읽기 전용 교차검증에서 아래 지적이 추가로 나왔다.

```text
교차검증 결론:
  현재 Census v4는 "정직한 보류 시스템"까지는 왔지만
  "운영 Stage 산출 시스템"은 아니다.
```

이 결론은 본 문서의 판정과 일치한다.

### 추가 지적 1. 웹 fetch relevance는 아직 영어 alias 보강을 공유하지 않는다

이번 패치는 claim adjudication 단계의 target aliases를 보강했다.
하지만 source acquisition 쪽 웹 relevance 검사는 아직 더 좁다.

관련 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
```

현재 위험:

```text
검색 결과 제목:
  SK Hynix 000660 - Research Report

본문:
  SK Hynix raised guidance...

웹 fetch relevance가 보는 기본 alias:
  SK하이닉스
  000660

본문에 000660이 없고 SK Hynix만 있으면:
  fetch 이후 target relevance에서 떨어질 수 있다.
```

이번 v68에서는 리포트가 실제 fetch됐으므로 이 문제가 항상 재현된 것은 아니다.
하지만 구조적으로는 맞는 지적이다.

다음 패치 방향:

```text
1. Source acquisition relevance도 Evidence extraction alias policy와 같은 안전한 alias 보강을 공유한다.
2. 단, "본문에 영어명이 있다"만으로 alias를 만들면 안 된다.
3. title/result metadata에 target ticker가 함께 있거나 EntityRegistry가 확인한 alias만 사용한다.
```

쉬운 예:

```text
허용:
  title = "SK Hynix 000660 - Research Report"
  -> SK Hynix를 000660 alias로 사용

금지:
  삼성전자 기사 본문에 SK Hynix가 언급됨
  -> SK Hynix를 삼성전자 alias로 사용
```

### 추가 지적 2. General search 차단은 맞지만 trusted connector 통로가 부족하다

현재 일반 웹 검색 결과는 score source로 바로 인정되지 않는다.
이 원칙은 맞다.

문제는:

```text
BrokerReportPublicPDF
TrustedNews
CompanyNewsroom
IR
```

같은 원출처/신뢰 출처 connector가 충분히 닫히지 않으면,
일반 검색을 막기만 하고 accepted web/LLM claim으로 가는 길이 거의 없다.

예:

```text
Naver search로 증권사 리포트 URL을 찾았다.
  -> discovery로는 유용

하지만 점수에 넣으려면:
  증권사 리포트 원문 connector 또는 원출처 lineage 검증이 필요
```

다음 패치 방향:

```text
1. general search는 discovery-only로 유지한다.
2. 발견한 URL이 증권사/공식 IR/뉴스 원문이면 source class별 connector로 재해결한다.
3. connector가 없으면 낮은 점수 확정이 아니라 SourcePending으로 남긴다.
```

### 추가 지적 3. 540일 blanket temporal rule은 장기 claim에 위험하다

현재 간단한 adjudication 경로에는:

```text
event_date가 as_of_date보다 540일 이상 오래됨
  -> HISTORICAL
```

규칙이 있다.

이 규칙은 2020년 감사/회계 이슈를 2026년 current risk로 잘못 넣는 문제를 줄이는 데 도움은 된다.
하지만 모든 claim에 일괄 적용하면 틀릴 수 있다.

틀릴 수 있는 예:

```text
3년 공급계약:
  2024년에 체결됐고 2027년까지 유효하면 2026년 현재도 살아 있다.

장기 소송:
  2023년에 제기됐지만 2026년에도 미종결이면 current risk일 수 있다.

임상:
  2024년 환자 등록 시작 후 2026년 readout 대기라면 historical이 아니다.

CAPA:
  2024년 투자 발표, 2026년 준공/가동 예정이면 현재성 판단은 lifecycle을 봐야 한다.
```

따라서 정답은 날짜 cutoff 하나가 아니다.

```text
claim type별 lifecycle policy:
  contract -> 종료일/취소/연장/정정공시
  audit -> 최신 감사보고서가 이전 의견 supersede
  litigation -> 종결/합의/판결까지 open 가능
  clinical -> 후속 readout/중단/승인 여부
  capacity -> 준공/지연/취소/가동개시
```

다음 패치 방향:

```text
1. 540일 rule을 최종 lifecycle 판정으로 쓰지 않는다.
2. missing lifecycle policy가 있으면 낮은 score가 아니라 follow-up/pending으로 둔다.
3. long-lived primitive는 EvidenceContract freshness/lifecycle rule에서 판단한다.
```

### 병목 1. 실제 운영 Stage 0개

증상:

```text
census_stage_status.stage = None 3391개
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
```

원인:

```text
web/LLM accepted claim이 없거나 부족하다.
direct source task satisfaction도 부족하다.
StageCourt trace가 있어도 운영 row로 promotion 되지 않는다.
```

판단:

```text
이건 버그라기보다 정직한 차단이다.
claim 없는 Stage를 만들면 과거 90점/60점 사태를 반복한다.
```

### 병목 2. Source Router가 live web에서 full-source 증거까지 못 간다

증상:

```text
v69:
  web_search_results = 27
  selected_for_fetch = 4
  web_fetched_documents = 0
```

원인:

```text
selected fetch 후보가 403, stock quote/profile, target mismatch 쪽으로 흐른다.
```

쉬운 예:

```text
우리가 원하는 것:
  삼성제약 공식 공시, 회사 IR, 신뢰 뉴스, 원문 리포트

현재 잡힌 것:
  Investing.com 시장 뉴스
  타 종목 시세 페이지
  뉴스룸 목록/검색 페이지
```

다음 패치 방향:

```text
1. fetch 후보 선정 전에 source document type 점수를 더 강하게 적용한다.
2. stock quote/profile/list/archive/digest는 fetch 전 단계에서 더 일찍 버린다.
3. source class가 BrokerReportPublicPDF면 증권사 리포트 원문/리서치 도메인을 우선한다.
4. CompanyNewsroom이면 회사 공식 newsroom/IR/news URL만 우선한다.
5. TrustedNews면 article page를 우선하고 search/list/tag page를 뒤로 민다.
6. 403 또는 non-evidence fetch가 나오면 같은 task 예산 안에서 다음 후보를 시도할 수 있게 한다.
```

주의:

```text
이걸 top_results=None 무한 fetch로 해결하면 안 된다.
bounded budget 안에서 후보 품질을 높여야 한다.
```

### 병목 3. v68 영어 alias 문제는 unit으로 고쳤지만 live로 재증명은 아직 못 했다

증상:

```text
v68:
  SK Hynix 000660 리포트를 fetch했다.
  하지만 subject = SK Hynix가 UNRELATED로 reject됐다.

v69:
  web_fetched_documents = 0
  따라서 영어 alias 패치가 live path에서 재실행되지 않았다.
```

현재 상태:

```text
unit test로는 고쳤다.
live artifact로는 아직 proof가 없다.
```

다음 검증:

```text
fixture 또는 bounded live smoke에서
title = "SK Hynix 000660 - Research Report"
subject = "SK Hynix"
claim target_scope_status = DIRECT
accepted_claim_ids = [] if source lineage unverified
```

즉 target adjudication과 score admissibility를 둘 다 확인해야 한다.

### 병목 4. 영어 alias는 장기적으로 registry가 필요하다

이번 패치는 제한적이다.

```text
title에 ticker가 같이 있을 때만 영어 alias를 추출한다.
```

이걸로 막을 수 없는 사례:

```text
Samsung Electronics Q2 review
  제목에 005930이 없음

Hyundai Motor earnings call
  제목에 005380이 없음

LG Chem investor day
  제목에 051910이 없음
```

장기 패치:

```text
EntityRegistry에 공식 alias를 넣어야 한다.

source:
  KRX 종목 영문명
  DART 법인 영문명
  회사 IR / 공식 홈페이지 표기
  과거 상호
  자회사/모회사 alias

adjudication:
  subject_entity_id를 문자열이 아니라 entity id로 해석
```

절대 하면 안 되는 방식:

```python
if symbol == "000660":
    aliases.append("SK Hynix")
```

이건 종목명 하드코딩이다.

### 병목 5. raw exact quote와 structured quote가 아직 완전히 같지 않다

이번 패치:

```text
LLM/raw assertion exact_quote를 출력 row에서 우선 사용한다.
```

남은 문제:

```text
structured signal 경로에서는 raw assertion exact_quote 자체가 anchor 긴 텍스트인 경우가 있다.
```

예:

```text
분기보고서 전체 앞부분 500자
  -> claim quote로는 너무 크다.

원하는 quote:
  계약금액 1500억원 최근매출액 대비 15.0%
  또는 TARGET_PRC / EPS / CONSENSUS_AS_OF_DATE가 들어간 구체 table row
```

다음 패치:

```text
structured row signal도 field-level quote 또는 table-cell anchor를 갖게 해야 한다.
```

## 다음 패치 우선순위

### P0. Source Router fetch candidate 품질 패치

목표:

```text
web_search_results가 있어도 아무 페이지나 fetch하지 않는다.
bounded budget 안에서 full-source evidence document로 갈 확률을 올린다.
```

해야 할 일:

```text
1. fetch 전 selection_status에 source_class compatibility를 더 강하게 반영한다.
2. stock quote/profile/list/archive/tag/search page는 selection 전에 더 강하게 reject한다.
3. source class별 preferred URL/type rule을 registry로 둔다.
4. 403/non-evidence fetch 실패 시 max_fetches budget 안에서 다음 후보를 시도한다.
5. rejected 이유를 web_rejected_documents에 남긴다.
```

예:

```text
BrokerReportPublicPDF task
  좋은 후보:
    securities.* / researchReportsView / PDF / report domain

  나쁜 후보:
    Investing.com stock news/profile
    Naver stock quote page
    generic market digest
```

### P1. Official/source-first 재라우팅 강화

v69 planner error:

```text
FCF/DART-solvable gap sent to general web/news: contract_visibility
```

해석:

```text
공시로 풀어야 할 gap을 일반 웹으로 보내는 planner output이 아직 나온다.
```

다음 패치:

```text
planner에게 "공시/IR/CompanyGuide로 풀 수 있는 gap을 general web으로 보냈다"는 feedback을
source feedback으로 돌려보내고, 같은 task를 공식 source class로 재생성하게 한다.
```

단:

```text
코드가 deterministic query를 새로 만들면 안 된다.
LLM planner가 source task를 다시 내야 한다.
코드는 정책 위반과 실패 이유만 알려준다.
```

### P2. Direct source task satisfaction을 Stage promotion gate와 더 붙이기

현재 여러 실행에서:

```text
accepted claim은 일부 생긴다.
하지만 task primitive gap이 직접 닫히지 않고 rerouted accepted로 남는다.
direct_source_task_satisfied_count = 0인 경우가 많다.
```

해석:

```text
좋은 claim은 찾았지만, 원래 닫으려던 gap은 안 닫혔다.
```

예:

```text
찾으려던 것:
  cash_or_revision_conversion

찾은 것:
  medium_term_revision_visibility

결과:
  좋은 claim이지만 Green gate를 닫으면 안 된다.
```

다음 패치:

```text
Stage promotion은 accepted claim count가 아니라
direct_source_task_satisfied_count와 material primitive coverage를 봐야 한다.
```

이 방향은 이미 일부 반영돼 있으나, 다음 live run에서 계속 검증해야 한다.

### P3. EntityRegistry alias 확장

이번 패치는 `title + ticker` 기반의 안전한 임시 보강이다.
궁극적으로는 registry가 필요하다.

목표:

```text
subject string -> entity id -> target relation
```

예:

```text
SK Hynix
SK hynix Inc.
에스케이하이닉스
SK하이닉스
000660

모두 TICKER:000660 / DART corp_code와 연결
```

이걸 해야 영어 리포트, 영문 IR, 글로벌 뉴스가 안정적으로 들어온다.

### P4. Structured signal quote를 table-cell/field-level anchor로 줄이기

현재:

```text
structured signal claim quote가 anchor 긴 텍스트로 남을 수 있다.
```

목표:

```text
claim row만 보고도 어떤 field가 어떤 값을 만들었는지 알 수 있게 한다.
```

예:

```text
quote_text:
  CONSENSUS_AS_OF_DATE=2026-06-30, EPS=12345, TARGET_PRC=1540000, provider_count=22

또는:
  DART row: 계약금액=1500억원, 최근매출액대비=15.0%, 계약기간=2024-06-01~2027-05-31
```

## 다음 에이전트 공격 체크리스트

다음 에이전트는 아래를 공격해야 한다.

```text
1. v69에서 selected_for_fetch 4개가 왜 모두 나쁜 후보였는가?
2. source router ranking이 target/source_class compatibility보다 rank를 너무 믿고 있지 않은가?
3. Investing.com, stock quote/profile, market digest가 fetch 후보로 올라오는 이유는 무엇인가?
4. max_fetches=1 스모크가 너무 빡빡해서 정상 후보까지 못 간 것인가, 아니면 ranking 자체가 틀린 것인가?
5. LLM planner가 DART-solvable gap을 general web으로 보낼 때 feedback retry가 충분한가?
6. v68 SK Hynix alias 오판은 unit test로만 막혔는데 live fixture로 고정할 수 있는가?
7. quote_text가 raw exact quote 우선으로 바뀌었는지 export artifact에서 검증하는 테스트가 충분한가?
8. structured signal quote가 여전히 anchor 전체인 문제가 score audit에 치명적인가?
9. FULL_THESIS stage 0개가 정직한 차단인지, 아니면 source router 불능 때문에 영원히 0개가 되는 구조인지?
10. 다음 패치는 source router인가, EntityRegistry인가, official source provider coverage인가?
```

## 현재 패치에 대한 자기 비판

### 위험 1. 영어 alias 보강이 아직 너무 제한적이다

장점:

```text
wrong-subject false positive를 크게 늘리지 않는다.
```

단점:

```text
title에 ticker가 없는 영어 공식 문서는 여전히 DIRECT가 안 될 수 있다.
```

판단:

```text
지금은 안전한 최소 패치로 맞다.
다음 단계에서 EntityRegistry로 풀어야 한다.
```

### 위험 2. alias 정규화가 다른 회사명을 과하게 합칠 수 있다

예상 위험:

```text
ABC Co. Ltd. -> abc
ABC Corp. -> abc
```

이건 같은 회사일 수도 있지만 다른 회사일 수도 있다.

완화:

```text
이번 patch는 title+symbol alias 보강과 함께 쓴다.
symbol 없는 임의 영어 이름을 바로 target alias로 만들지 않는다.
```

다음 보강:

```text
EntityRegistry에서 corp_code/ticker 기반으로 alias를 관리한다.
```

### 위험 3. v69 live smoke가 alias patch를 직접 증명하지 못했다

v69에서는 web fetched document가 0개라 alias path가 live에서 실행되지 않았다.

따라서 문서화 결론은 이렇게 써야 한다.

```text
패치는 unit/regression으로 검증됐다.
v69 live에서 alias path는 재현되지 않았다.
다음 live 또는 frozen fixture에서 반드시 재증명해야 한다.
```

### 위험 4. Source Router가 현 상태면 LLM Evidence OS까지 못 간다

Evidence OS가 아무리 좋아도 full-source 문서가 없으면 작동하지 않는다.

```text
검색 결과 있음
fetch 문서 없음
LLM extractor 없음
accepted claim 없음
Stage 없음
```

이게 v69다.

## 최종 판정

현재 상태:

```text
verdict: NOT_READY
operational FULL_THESIS stage: 0
web/LLM accepted claim: 0
Brain/Web promotion: BLOCKED
```

이번 패치로 해결한 것:

```text
1. 영어 subject alias exact-match 실패를 일부 해결했다.
2. title에 ticker가 붙은 영어 리포트에서 target alias를 안전하게 보강한다.
3. claim audit row의 quote_text가 raw exact_quote를 우선 보게 했다.
4. 이 변경이 general web source score unlock으로 이어지지 않게 테스트했다.
```

아직 해결하지 못한 것:

```text
1. live web source router가 full-source evidence까지 안정적으로 못 간다.
2. v69에서는 web_fetched_document_count가 0이라 LLM extractor가 실행되지 않았다.
3. 운영 Stage는 여전히 0개다.
4. 영어 alias는 registry 기반이 아니라 title+symbol 기반 최소 패치다.
5. structured signal quote는 여전히 field-level이 아닐 수 있다.
```

다음 패치 최우선:

```text
Source Router fetch candidate 품질을 고쳐라.

더 많이 긁는 패치가 아니다.
bounded budget 안에서 "증거 문서"를 먼저 고르는 패치다.
```

운영 판단:

```text
지금 Stage가 없는 것은 맞다.
지금 Stage를 억지로 만들면 안 된다.
먼저 full-source -> raw assertion -> adjudicated claim -> accepted claim -> direct source task satisfaction -> Stage promotion 경로를 닫아야 한다.
```
