# Census v4 0701 v70 Source Router / Stage Truth Cross-Audit

작성일: 2026-07-03

이 문서는 다음 에이전트가 바로 공격 검증할 수 있게 만든 v70 감사 패킷이다.

한 줄 결론:

```text
v70은 v69보다 live web fetch / LLM extraction 단계는 되살렸지만,
운영자가 쓸 수 있는 FULL_THESIS Stage는 여전히 0개다.
```

쉬운 예:

```text
출석부에는 3391명이 올라와 있다.
그중 85명은 "다시 정밀 채점 필요" 표시가 붙었다.
하지만 실제 100점짜리 채점지와 최종 등급표가 완성된 학생은 아직 0명이다.
```

따라서 현재 상태를 이렇게 말해야 한다.

```text
Stage 비슷한 상태판 row는 있다.
운영 Stage는 없다.
```

## 1. 이번에 확인한 핵심 질문

사용자 질문:

```text
뭔가 잘못되고있는거맞지? stage가 있는애들이 있긴해?
```

정확한 답:

```text
예, 아직 운영 Stage가 없다는 판단이 맞다.
다만 "아무것도 안 돈다"는 뜻은 아니다.
현재 파이프라인은 후보/상태판/부분 claim은 만들고 있지만,
그것을 FULL_THESIS 운영 Stage로 승격시키는 마지막 다리가 아직 닫히지 않았다.
```

구분은 반드시 이렇게 해야 한다.

| 구분 | 현재 존재 여부 | 운영자가 Stage로 써도 되는가 | 설명 |
| --- | ---: | --- | --- |
| `CENSUS_EVENT_BOARD` 상태판 row | 3391개 | 아니오 | 전체 universe 평가 스탬프와 얕은 상태 |
| event-board non-Stage0 row | 85개 | 아니오 | 정밀 재평가 큐 후보 |
| accepted EvidenceClaim payload | 93개 | 단독으로는 아니오 | 대부분 DART/CompanyGuide 기반 부분 claim |
| Research Brain StageCourt trace | 1개 | 아직 아니오 | census stage row로 promotion 안 됨 |
| `FULL_THESIS` production row | 0개 | 예, 하지만 현재 0개 | 운영 Stage의 핵심 산출물 |
| `FULL_E2R_100` verified score row | 0개 | 예, 하지만 현재 0개 | 100점 체계 운영 점수 |

## 2. v70에서 실제로 바뀐 패치

패치 범위:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
```

### 2.1 Web relevance가 title+symbol 영문 alias를 쓴다

문제:

```text
SK하이닉스 000660 후보
검색 결과 제목: "SK Hynix 000660 - Research Report"
본문: "SK Hynix ..."

기존 web relevance는 한국어명/티커 중심이라 본문에 000660이나 SK하이닉스가 없으면
대상회사 문서가 아니라고 버릴 수 있었다.
```

패치:

```text
검색 결과 title에 target ticker가 같이 있을 때만,
title에서 안전한 영문 회사 alias를 임시 추출한다.

"SK Hynix 000660 - Research Report"
  -> "SK Hynix" alias 허용

"Research Report 000660"
  -> 일반 단어라 alias 불허
```

이건 점수 unlock이 아니다.

```text
문서 fetch relevance 통과용 alias일 뿐,
claim이 점수에 들어가려면 여전히
raw assertion -> adjudication -> primitive mapping -> score eligibility를 통과해야 한다.
```

### 2.2 Investing.com 시장요약/주가프로필을 before-fetch에서 더 빨리 거절한다

문제:

```text
v69에서 Investing.com generic market/profile 페이지가 선택되어
fetch 예산을 잡아먹고, HTTP 403 또는 비대상 문서로 끝나는 일이 있었다.
```

패치:

```text
investing.com/news/stock-market-news/
investing.com/equities/
증시/3대지수/FOMC/연준/국채금리 같은 시장요약
오늘의주가/실시간티커/stockprice/stocknews 같은 주가프로필
```

이런 결과는 대상회사 source document가 아니면 fetch 전에 거절한다.

쉬운 예:

```text
"오늘 미국 증시 요약, SK하이닉스 언급"
  -> 조사 힌트일 수는 있지만 C06 HBM 증거 문서가 아니다.

"SK하이닉스 GTC 2026 HBM 제품 포트폴리오 공개"
  -> 최소한 대상회사 문서 후보라 fetch 가능하다.
```

## 3. 회귀 테스트 결과

Targeted tests:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_source_acquisition -v
```

결과:

```text
Ran 33 tests in 0.028s
OK
```

추가된 핵심 테스트:

```text
test_live_full_bounded_rejects_investing_market_digest_before_fetching_target_article
test_live_full_bounded_web_relevance_uses_title_symbol_english_alias
```

Related tests:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_bundle_export -v
```

결과:

```text
Ran 69 tests in 4.133s
OK
```

Full suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5099 tests in 211.890s
OK
```

중요한 해석:

```text
테스트 통과는 "운영 Stage가 생겼다"는 뜻이 아니다.
테스트 통과는 "이번 source-router 패치가 기존 안전장치를 깨지 않았다"는 뜻이다.
```

## 4. v68 / v69 / v70 live smoke 비교

### 실행 조건

v70 실행:

```bash
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 \
E2R_CODEX_EXTRACTOR_TIMEOUT_SECONDS=120 \
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70 \
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
exit = 1
stdout = NOT_READY
```

### 주요 숫자

| 항목 | v68 | v69 | v70 |
| --- | ---: | ---: | ---: |
| `web_search_results.jsonl` | 51 | 27 | 54 |
| `web_fetched_documents.jsonl` | 2 | 0 | 2 |
| `web_rejected_documents.jsonl` | 11 | 27 | 10 |
| `claim_extractor_runs.jsonl` | 2 | 0 | 2 |
| `llm_claim_extractor_provider_error_count` | 1 | 0 | 0 |
| `web_or_llm_accepted_claim_count` | 0 | 0 | 0 |
| `brain_promoted_stage_row_count` | 0 | 0 | 0 |
| verdict | NOT_READY | NOT_READY | NOT_READY |

해석:

```text
v69: source router가 너무 보수적으로/나쁘게 선택해서 fetch와 extractor가 0으로 죽었다.
v70: fetch와 extractor는 되살아났다.
하지만 web/LLM claim이 score-eligible accepted claim으로 이어지지 않아 Stage promotion은 0이다.
```

## 5. v70 artifact 교차검증

### 5.1 readiness verdict

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/readiness_verdict.json
```

핵심값:

```text
verdict = NOT_READY
target_gate = brain_web
target_gate_pass = false
stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
meaningful_operational_stage_pass = false
operational_stage_use_allowed = false
event_board_non_stage0_count = 85
```

공격 포인트:

```text
event_board_non_stage0_count=85를 운영 Stage라고 부르면 안 된다.
readiness가 직접 stage_scope_notice로 "NO_FULL_THESIS_STAGE_ROWS"를 말한다.
```

### 5.2 census stage status

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/census_stage_status.jsonl
```

집계:

```text
rows = 3391
stage_scope = CENSUS_EVENT_BOARD 3391
operator_stage_use = NOT_FULL_THESIS_STAGE 3391

base_stage:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1
```

해석:

```text
이 row들은 "현재 상태판"이다.
FULL_THESIS 운영 Stage가 아니다.
```

쉬운 예:

```text
Stage2-Watch라고 적힌 event-board row는
"이 종목을 정밀 채점하러 보내라"는 표식이지,
"운영 Stage2로 확정했다"는 뜻이 아니다.
```

### 5.3 Brain/Web readiness gate

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/brain_web_readiness_gate_audit.json
```

핵심값:

```text
verdict = BLOCKED
web_search_task_count = 5
web_search_call_count = 5
web_search_result_count = 54
web_fetched_document_count = 2
llm_claim_extractor_attempt_count = 2
llm_claim_extractor_provider_error_count = 0
web_or_llm_accepted_claim_count = 0
brain_promoted_stage_row_count = 0
minimum_required_counts:
  web_search_task_count = 20
  web_search_call_count = 20
  web_fetched_document_count = 10
  llm_claim_extractor_attempt_count = 10
  web_or_llm_accepted_claim_count = 3
```

차단 사유:

```text
web/LLM accepted claim count is zero
```

해석:

```text
v70은 "읽기"까지는 성공했지만 "점수 가능한 web/LLM claim"은 못 만들었다.
따라서 Stage 승격이 막힌 것은 정상 방어다.
```

### 5.4 Web acquisition audit

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/web_naver_acquisition_audit.json
```

핵심값:

```text
verdict = REAL_ACQUISITION_PASS
naver_search_call_count = 5
web_search_call_count = 5
web_search_result_count = 54
web_fetched_document_count = 2
web_rejected_document_count = 10
```

해석:

```text
web acquisition 자체는 v69보다 개선됐다.
하지만 acquisition pass는 score/stage pass가 아니다.
```

### 5.5 LLM claim extraction audit

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/llm_claim_extraction_audit.json
```

핵심값:

```text
verdict = REAL_EXTRACTION_PASS
configured_timeout_seconds = 120.0
llm_claim_extractor_attempt_count = 2
llm_claim_extractor_real_provider_count = 2
llm_claim_extractor_provider_error_count = 0
llm_claim_extractor_timeout_count = 0
```

해석:

```text
v68의 extractor timeout/provider error 문제는 v70에서는 재현되지 않았다.
이번 blocker는 provider failure가 아니라 claim admissibility다.
```

### 5.6 Brain stage promotion audit

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/brain_stage_promotion_audit.json
```

핵심값:

```text
verdict = BLOCKED
brain_claim_count = 1
brain_stage_trace_count = 1
brain_score_contribution_count = 2
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
brain_promoted_stage_row_count = 0
```

차단 사유:

```text
web/LLM accepted brain claim count is zero for BRAIN_WEB_PARTIAL promotion
```

해석:

```text
CompanyGuide 기반 official accepted claim 1개는 생겼지만,
그 claim은 web/LLM C06 thesis claim이 아니고, FULL_THESIS 승격 조건도 만족하지 않았다.
```

## 6. v70에서 fetch된 실제 문서

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/web_fetched_documents.jsonl
```

fetch된 문서 2개:

```text
1. SK hynix Newsroom
   title = SK하이닉스, GTC 2026서 엔비디아와 파트너십 재확인...
   url = https://news.skhynix.co.kr/gtc-2026-exhibition-booth/

2. Dailian
   title = SK하이닉스, 美서 HBM4 16단 최초 공개...메모리 솔루션 전시 [CES 2026]
   url = https://www.dailian.co.kr/news/view/1594665/...
```

둘 다 fetch와 LLM extraction은 됐다.

하지만 거절 결과:

```text
post_extraction_no_score_eligible_claim
```

즉:

```text
제품 공개 / 전시 / 파트너십 재확인 문장은 추출됐지만,
C06 Green/Stage를 열 수 있는 capacity pre-sold, customer allocation,
qualification pass, revenue mix 같은 claim으로 인정되지 않았다.
```

이 거절은 오히려 맞는 방어다.

쉬운 예:

```text
"엔비디아 협업 존에서 제품을 전시했다"
  -> 제품 프로필/마케팅 claim
  -> C06 customer allocation 점수로 쓰면 안 된다.

"특정 고객에게 HBM 공급이 배정됐고 2026년 capacity가 선판매됐다"
  -> C06 점수 후보 claim
  -> source lineage와 quote 검증 뒤 점수 가능
```

## 7. v70 rejected document 분포

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/web_rejected_documents.jsonl
```

거절 사유:

```text
web_result_low_quality_blog_or_social_not_score_source = 7
post_extraction_no_score_eligible_claim = 2
web_fetch_site_archive_or_sitemap_not_source_document = 1
```

v69와 비교:

```text
v69 rejected:
  site archive/sitemap = 7
  target not found after fetch = 5
  stock list/channel = 5
  HTTP 403 = 4
  target not in title/snippet/lead = 4

v70 rejected:
  low-quality blog/social = 7
  post-extraction no score eligible claim = 2
  archive/sitemap = 1
```

해석:

```text
v70 source router는 v69의 시장요약/프로필/403 낭비를 줄였다.
하지만 검색 결과 품질 자체는 아직 블로그/전시 기사 위주라 C06 점수 claim으로 이어지지 않았다.
```

## 8. accepted_claims가 93개인데 왜 Stage가 0개인가

이 부분을 다음 에이전트가 반드시 공격해야 한다.

v70 accepted claims:

```text
accepted_claims.jsonl rows = 93
source_task_executions rows = 104
source_task_executions EVIDENCE_OS_ACCEPTED = 61
stagecourt_traces rows = 93
```

하지만 readiness:

```text
full_e2r_verified_score_row_count = 0
full_thesis_stage_row_count = 0
production_full_thesis_row_count = 0
```

왜?

```text
대부분 accepted claims는 DART/CompanyGuide 기반 event-board/partial claim이다.
이들은 개별 공시나 컨센서스 claim으로는 유효할 수 있지만,
FULL_THESIS 운영 Stage의 100점 점수표를 완성한 것이 아니다.
```

쉬운 예:

```text
공시 하나에서 "단일판매공급계약" claim을 얻었다.
  -> contract_quality 일부는 열 수 있다.

하지만 Green/Yellow 운영 Stage에는 보통 다음이 더 필요하다.
  -> 반복성
  -> 현금흐름/수익성 bridge
  -> 독립 source family
  -> red-team guard 해소
  -> StageCourt trace promotion

계약 claim 하나가 있다고 FULL_THESIS Stage가 바로 생기면 안 된다.
```

## 9. v70에서 생긴 단 하나의 Brain claim

파일:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v70/brain_to_claim_trace.jsonl
```

claim:

```text
symbol = 000660
source_provider = CompanyGuide
primitive_id = medium_term_revision_visibility
satisfaction_type = REROUTED_ACCEPTED_CLAIM
satisfies_source_task = false
trace_status = CLAIM_SCORE_TRACE_EXPORTED_STAGE_NOT_PROMOTED
```

quote:

```text
투자의견 컨센서스 [2026/07/01] ...
목표주가 EPS PER 추정기관수 ...
```

해석:

```text
이 claim은 SK하이닉스 컨센서스 visibility claim으로는 쓸 수 있다.
하지만 원래 C06 핵심 gap인 HBM capacity pre-sold / customer allocation /
qualification / revenue mix를 만족한 claim이 아니다.
그래서 rerouted accepted claim으로 남고, source task 자체는 satisfies_source_task=false다.
```

중요:

```text
이 claim을 억지로 C06 Green/Yellow로 fan-out하면 다시 예전 오류로 돌아간다.
```

## 10. 현재 병목의 정확한 이름

v69 병목:

```text
Source Router가 fetch/extractor까지 못 보냄
```

v70 병목:

```text
Source Router는 일부 문서를 fetch했고 LLM extraction도 성공했지만,
공식 원천성 / source class / requested primitive satisfaction이 닫히지 않아
web/LLM accepted claim이 0이다.
```

더 구체적으로:

```text
1. SK hynix official newsroom 문서가 Naver general web discovery 경로로 들어와
   CompanyNewsroom 원천 문서로 승격되지 못했다.

2. 그래서 일부 direct claim도
   source_provider_document_type_mismatch:CompanyNewsroom:general_web_search_provider
   source_lineage_unverified_original:CompanyNewsroom:general_web_search_provider
   로 막혔다.

3. 제품 전시/파트너십 재확인 문장은 C06 customer allocation이나 capacity pre-sold로
   매핑되면 안 되므로 post-extraction no-score-eligible은 정상 방어다.

4. CompanyGuide 컨센서스 claim은 medium_term_revision_visibility로 인정됐지만,
   원래 source task primitive를 만족한 것이 아니어서 Stage promotion이 막혔다.
```

## 11. 이 패치가 해결한 것과 해결하지 못한 것

해결한 것:

```text
1. v69처럼 fetch 0 / extractor 0으로 멈추는 상태는 v70에서 재현되지 않았다.
2. 영문 title+symbol alias가 web relevance에서 target 문서를 살릴 수 있다.
3. generic Investing.com market/profile 페이지를 before-fetch에서 더 빨리 거절한다.
4. 5099개 전체 테스트를 깨지 않았다.
```

해결하지 못한 것:

```text
1. 운영 FULL_THESIS Stage row는 여전히 0개다.
2. web/LLM accepted claim은 여전히 0개다.
3. SK hynix official newsroom을 verified issuer-official source로 승격하지 못한다.
4. fetched web 문서는 C06 핵심 primitive를 만족하지 못했다.
5. all-archetype source-backed replay는 6/32 수준이고 26개 required archetype gap이 남아 있다.
6. production full thesis runner는 refresh queue 85개 중 1개만 materialized했고 promoted row는 0개다.
```

## 12. 다음 패치 방향

### P0. Official Domain / Source Lineage Resolver

문제:

```text
news.skhynix.co.kr 원문을 Naver search로 발견하면,
현재는 general_web_search_provider 경로로 남아 source lineage가 약하다.
```

필요한 패치:

```text
URL domain이 issuer official domain인지 검증하는 resolver를 둔다.
DART/CompanyGuide/KRX/공식 홈페이지 정보에서 official domain을 확보하고,
웹 검색으로 발견된 공식 newsroom 원문은 IssuerOfficial 또는 CompanyNewsroom 원천으로 재분류한다.
```

주의:

```text
이건 "SK하이닉스면 news.skhynix.co.kr" 같은 종목별 하드코딩이 아니다.
EntityRegistry / official domain registry / source provenance resolver 문제다.
```

패치 후에도 점수 unlock 조건은 그대로 유지한다.

```text
official source로 승격됐다고 해서 제품 전시 문장이 customer allocation 점수가 되면 안 된다.
```

### P0. SourceTask satisfaction을 primitive 단위로 닫기

v70의 CompanyGuide claim:

```text
primitive_id = medium_term_revision_visibility
satisfies_source_task = false
```

이 상태는 맞다.

다음 패치에서 해야 할 것:

```text
accepted claim이 있어도 요청한 primitive gap을 만족하지 않으면 Stage promotion 금지.
대신 그 accepted claim은 rerouted evidence로 ledger에 남기고,
남은 C06 gap을 다시 planner에게 넘겨야 한다.
```

즉:

```text
medium_term_revision_visibility를 찾았으니 좋다.
하지만 hbm_capacity_pre_sold / customer_allocation은 아직 비었다.
그러니 Stage를 주는 게 아니라 다음 search task를 더 정확히 내야 한다.
```

### P0. Post-extraction feedback을 LLM planner에 더 세게 되돌리기

v70의 반복 입력은 다음을 planner가 알아야 한다.

```text
fetched official/newsroom docs produced no score-eligible C06 claim
reason:
  product showcase / partnership reaffirmation only
  no capacity pre-sold
  no customer allocation
  no revenue mix
  no qualification pass
```

좋은 다음 query는 deterministic template로 만들면 안 된다.
LLM planner가 위 실패 사유를 보고 직접 새 query/task를 제안해야 한다.

단, 코드는 다음만 검증한다.

```text
as_of_date 이후 문서 금지
target scoped query인지 확인
official-first source budget 유지
unbounded general search 금지
중복 query 금지
```

### P1. Production Full Thesis Runner queue 처리 확대

v70:

```text
full_thesis_refresh_queue_candidate_count = 85
refresh_queue_materialized_candidate_count = 1
promoted_full_thesis_row_count = 0
```

다음에는 큐 전체를 무제한으로 긁으면 안 된다.
대신 bounded shard 방식이 필요하다.

```text
queue shard
  -> official-first SourceTask
  -> claim extraction / adjudication / mapping
  -> StageCourt
  -> promotion gate
```

예:

```text
한 번에 85개 전부를 무한 웹검색하지 않는다.
sector/sample/budget 기준으로 N개씩 처리하고,
provider pending과 no-current-catalyst를 낮은 점수로 확정하지 않는다.
```

### P1. all-archetype replay gap 26개 축소

현재:

```text
required_archetype_count = 32
source_backed_ready_count = 6
missing_required_archetype_count = 26
```

이것이 goal complete의 가장 큰 blocker 중 하나다.

다음 패치는 C06 하나만 Stage로 만드는 게 아니라,
각 archetype의 source-backed replay fixture를 최소 하나씩 닫는 방향이어야 한다.

단:

```text
source_proxy_only 연구자료를 운영 점수 정답으로 쓰면 안 된다.
실제 URL / anchor / claim / primitive / score chain이 닫힌 사례만 replay ready로 세야 한다.
```

## 13. 다음 에이전트 공격 질문

다음 에이전트는 아래 질문에 답해야 한다.

```text
1. v70에서 FULL_THESIS row가 0인데도 어떤 문서가 운영 Stage가 있다고 과장하는가?
2. accepted_claims 93개 중 FULL_E2R_100 score에 들어간 것이 실제로 있는가?
3. CompanyGuide medium_term_revision_visibility claim이 왜 C06 capacity/customer gap을 만족하지 않는가?
4. SK hynix newsroom 원문을 official source로 재분류할 수 있는 근거 데이터가 어디 있는가?
5. official source로 재분류해도 제품 전시 claim을 capacity allocation으로 오매핑하지 않는 테스트가 있는가?
6. v70의 post_extraction_no_score_eligible_claim 사유가 planner retry context로 충분히 전달되는가?
7. web/LLM accepted claim count가 0인데 brain stage promotion을 우회하는 경로가 남아 있는가?
8. production full thesis runner가 queue 85개를 bounded하게 처리하는가?
9. all-archetype replay 26개 gap을 source_proxy 없이 줄이는 계획이 있는가?
10. 테스트 통과와 운영 readiness를 README가 혼동하지 않는가?
```

## 14. 현재 최종 판정

```text
verdict = NOT_READY
```

운영적으로 말하면:

```text
아직 daily 운영 Stage를 내면 안 된다.
현재 산출물은 event-board 상태판 + partial evidence ledger + full-thesis refresh queue다.
```

패치 방향은 맞지만 다음 단계가 남았다.

```text
1. official domain/source lineage resolver
2. source task primitive satisfaction loop 강화
3. post-extraction failure feedback을 LLM planner에 전달
4. bounded production full thesis runner 확대
5. all-archetype source-backed replay 확장
```

가장 중요한 금지:

```text
web fetch 2개 / extractor 2개 성공을 Stage 성공으로 포장하지 말 것.
accepted_claims 93개를 FULL_THESIS 운영 Stage 개수로 포장하지 말 것.
CompanyGuide 컨센서스 claim 하나로 C06 thesis를 채웠다고 말하지 말 것.
```

