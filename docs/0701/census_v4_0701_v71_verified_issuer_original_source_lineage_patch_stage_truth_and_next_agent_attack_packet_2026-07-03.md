# Census v4 0701 v71 Verified Issuer Original Source-Lineage Patch / Stage Truth

작성일: 2026-07-03

이 문서는 다음 에이전트가 빡세게 검증할 수 있게 만든 v71 감사 패킷이다.

한 줄 결론:

```text
v71은 "네이버 검색으로 발견했지만 실제 URL은 회사 공식 도메인 원문"인 경우를
source-lineage 장부에 구분해 적는 패치를 넣었다.

하지만 운영자가 쓸 수 있는 FULL_THESIS Stage는 여전히 0개다.
```

쉬운 예:

```text
네이버가 길 안내를 해줬다.
도착한 건 SK하이닉스 공식 뉴스룸이다.
  -> 길 안내자는 네이버지만 원문 주체는 회사 공식 도메인으로 표시해야 한다.

하지만 공식 뉴스룸 글이 "제품을 전시했다"는 내용이면,
"HBM 고객 물량 배정 확정" 점수는 줄 수 없다.
  -> 공식 원문 여부와 점수 primitive 충족은 별개다.
```

## 1. 현재 Stage 질문에 대한 정확한 답

사용자 질문:

```text
뭔가 잘못되고있는거맞지? stage가 있는애들이 있긴해?
```

v71 산출물 기준 답:

```text
Stage처럼 보이는 행은 있다.
하지만 운영 Stage는 없다.
```

구분:

| 구분 | v71 존재 여부 | 운영 Stage로 사용 가능 여부 | 이유 |
| --- | ---: | --- | --- |
| `CENSUS_EVENT_BOARD` 상태판 row | 3391개 | 아니오 | 전체 종목 상태판이다. Full thesis 채점지가 아니다. |
| event-board non-Stage0 row | 85개 | 아니오 | 정밀 재평가 큐 후보일 뿐이다. |
| accepted claims | 94개 | 단독으로는 아니오 | 대부분 DART/CompanyGuide 기반 부분 claim이다. |
| score contributions | 94개 | 단독으로는 아니오 | 부분 점수 장부이며 FULL_E2R_100 검증 점수가 아니다. |
| `FULL_THESIS` production row | 0개 | 예, 하지만 현재 0개 | 운영자가 쓸 Stage는 이 scope가 있어야 한다. |
| `FULL_E2R_100` verified score row | 0개 | 예, 하지만 현재 0개 | 운영 100점 체계 점수는 아직 없다. |

핵심 문장:

```text
v71도 READY가 아니다.
Stage label은 상태판에만 있고, 운영용 FULL_THESIS Stage는 아직 없다.
```

## 2. 이번 v71 패치가 해결한 것

### 2.1 문제

v70에서 SK하이닉스 공식 뉴스룸 문서가 잡혔지만, source-lineage에서 이렇게 막힐 수 있었다.

```text
검색 provider = 일반 웹 검색
문서 URL = news.skhynix.co.kr
source class = CompanyNewsroom

기존 판단:
  general web search provider가 가져온 뉴스 문서이므로
  source_lineage_unverified_original 또는 provider/document mismatch로 차단
```

문제는 두 종류를 구분하지 못한 것이다.

```text
나쁜 문서:
  네이버 검색 결과의 일반 블로그, 증권 게시판, 독립 뉴스, 종목 프로필 페이지

좋은 후보:
  네이버 검색으로 발견했지만 실제 URL이 회사 공식 홈페이지/뉴스룸/IR 도메인인 원문
```

둘은 다르게 적어야 한다.

### 2.2 패치 방향

패치 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

핵심 변경:

```text
CompanyGuide snapshot의 홈페이지 URL을 issuer 공식 도메인 seed로 사용한다.
검색 결과 URL host가 이 공식 도메인 또는 같은 brand stem의 공식 계열 도메인이면
verified_issuer_original로 표시한다.
```

예:

```text
CompanyGuide 홈페이지 seed:
  www.skhynix.com

검색 결과 URL:
  news.skhynix.co.kr

정규화:
  homepage stem = skhynix
  result stem = skhynix

결과:
  verified_issuer_original = true
  source_name = IssuerOfficialDomain
  source_class = CompanyNewsroom
```

반례:

```text
CompanyGuide 홈페이지 seed:
  www.skhynix.com

검색 결과 URL:
  www.dailian.co.kr/news/view/1594665

정규화:
  homepage stem = skhynix
  result stem = dailian

결과:
  verified_issuer_original = false
```

중요:

```text
이 패치는 점수 unlock 패치가 아니다.
공식 원문인지 장부에 적는 패치다.
점수는 여전히 claim -> adjudication -> primitive mapping -> score eligibility를 통과해야 한다.
```

## 3. 코드 레벨 변경 요약

### 3.1 Source acquisition row에 verified issuer original 필드 추가

위치:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
```

주요 행:

```text
_web_result_row:
  verified_issuer_original
  verified_issuer_original_source_class
  verified_issuer_original_provider_name
  verified_issuer_original_resolver
  verified_issuer_original_document_id
  verified_issuer_homepage_host
  verified_issuer_result_host
  verified_issuer_original_status

_web_fetched_row:
  위 필드를 FETCHED_FULL_SOURCE leaf에도 복사
```

효과:

```text
검색 결과 단계와 fetch 단계 둘 다에서
"검색 provider는 일반 웹이었지만 원문 URL은 issuer official domain"이라는 사실을 추적할 수 있다.
```

### 3.2 공식 issuer domain resolver 추가

위치:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
```

핵심 함수:

```text
_verified_issuer_web_route_from_web_result
_issuer_homepage_hosts_from_companyguide
_companyguide_homepage_urls
_host_matches_homepage_or_subdomain
_domain_brand_stem
```

원칙:

```text
1. CompanyGuide snapshot의 홈페이지 링크를 읽는다.
2. 검색 결과 URL host를 정규화한다.
3. 정확한 서브도메인이면 허용한다.
4. .com / .co.kr처럼 TLD가 달라도 brand stem이 같으면 issuer 계열 후보로 본다.
5. title/snippet에 target alias가 없으면 허용하지 않는다.
```

쉬운 예:

```text
news.skhynix.co.kr
  -> skhynix stem이 같고 title/snippet에 SK하이닉스가 있으므로 issuer official 후보

www.dailian.co.kr
  -> dailian stem이므로 issuer official 아님
```

### 3.3 Evidence extraction bridge에서 일반 웹 lineage block 예외 처리

위치:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
```

핵심:

```text
document.source_lineage_id에 verified_issuer_original이 있고
document.source_type이 NEWS 또는 IR이고
source_class가 CompanyNewsroom / IssuerOfficial / IR이면
general_web_search_provider mismatch를 적용하지 않는다.
```

그러나 이건 source admissibility만 통과시키는 것이다.

```text
product_profile_claim
  -> primitive mapping에서 customer_preorder_or_allocation 거절

customer_allocation_or_qualification_claim
  -> customer_preorder_or_allocation accepted 가능
```

## 4. 추가한 회귀 테스트

### 4.1 Source acquisition 테스트

파일:

```text
tests/test_research_brain_v4_real_source_acquisition.py
```

추가/강화된 테스트:

```text
test_live_full_bounded_marks_company_homepage_subdomain_as_verified_newsroom_original
test_live_full_bounded_does_not_mark_independent_news_as_verified_issuer_original
```

검증:

```text
SK하이닉스 CompanyGuide 홈페이지 seed = www.skhynix.com
URL = news.skhynix.co.kr
  -> verified_issuer_original true

URL = www.dailian.co.kr
  -> verified_issuer_original false
```

### 4.2 Evidence extraction bridge 테스트

파일:

```text
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

추가/강화된 테스트:

```text
test_verified_company_newsroom_original_avoids_general_web_lineage_block_but_profile_claim_still_not_scored
test_verified_company_newsroom_original_can_score_direct_customer_allocation_claim
```

검증:

```text
공식 뉴스룸 원문 + "제품 포트폴리오 공개"
  -> source lineage block은 안 걸림
  -> customer_preorder_or_allocation은 거절
  -> score 0

공식 뉴스룸 원문 + "HBM 고객 물량 배정 확정"
  -> source lineage block은 안 걸림
  -> customer_preorder_or_allocation accepted
```

## 5. 테스트 결과

Targeted tests:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document -v
```

결과:

```text
Ran 56 tests in 0.114s
OK
```

Related tests:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 99 tests in 13.386s
OK
```

Full suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5103 tests in 216.215s
OK
```

Diff check:

```bash
git diff --check
```

결과:

```text
OK
```

중요한 해석:

```text
테스트 통과는 "운영 Stage가 생겼다"는 뜻이 아니다.
테스트 통과는 "source-lineage 표시 패치가 기존 안전장치를 깨지 않았다"는 뜻이다.
```

## 6. v71 live smoke 결과

실행:

```bash
rm -rf output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v71
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 \
E2R_CODEX_EXTRACTOR_TIMEOUT_SECONDS=120 \
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v71 \
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
exit code = 1
stdout = NOT_READY
```

핵심 artifacts:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v71/readiness_verdict.json
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v71/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v71/brain_stage_promotion_audit.json
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v71/web_naver_acquisition_audit.json
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v71/llm_claim_extraction_audit.json
```

핵심 숫자:

| 항목 | v71 |
| --- | ---: |
| verdict | NOT_READY |
| stage_scope_notice | NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST |
| full_thesis_stage_row_count | 0 |
| full_e2r_verified_score_row_count | 0 |
| event_board_non_stage0_count | 85 |
| web_search_task_count | 6 |
| web_search_call_count | 6 |
| web_search_result_count | 20 |
| web_fetched_document_count | 1 |
| llm_claim_extractor_attempt_count | 1 |
| llm_claim_extractor_provider_error_count | 0 |
| web_or_llm_accepted_claim_count | 0 |
| brain_promoted_stage_row_count | 0 |
| official_accepted_claim_count | 2 |

Readiness blockers:

```text
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 6/20
Brain/Web operational minimum web/news search calls not met: 6/20
Brain/Web operational minimum fetched documents not met: 1/10
Brain/Web operational minimum claim extractor attempts not met: 1/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

Stage status row check:

```text
census_stage_status.jsonl rows = 3391
stage_scope = CENSUS_EVENT_BOARD 3391
operator_stage_use = NOT_FULL_THESIS_STAGE 3391
base_stage:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1
FULL_THESIS = 0
```

따라서 v71도 이렇게 말해야 한다.

```text
상태판 Stage는 있다.
운영 Stage는 없다.
```

## 7. v71 live smoke에서 실제 선택된 후보

v71 smoke는 `--brain-universe-limit 1`이지만, 내부 full-thesis queue / planner success limit 때문에
SK하이닉스가 아니라 삼부토건 쪽 real planner success가 실제 실행 중심이 됐다.

확인:

```text
research_brain_plans.jsonl rows = 22
real_provider_success = True 2개
planner_not_attempted_after_real_planner_limit = 18개
FCF/DART-solvable gap sent to general web/news: contract_visibility = 2개
```

실제 fetched web document:

```text
symbol = 001470
company = 삼부토건
url = https://www.valueline.co.kr/finance/turnaround/001470
verified_issuer_original = false
```

해석:

```text
이번 v71 live smoke는 SK하이닉스 뉴스룸 resolver를 live에서 직접 exercise하지 못했다.
그 대신 회귀 테스트에서 resolver 동작을 고정했고,
live에서는 아직 web/LLM accepted claim이 0인 병목을 확인했다.
```

이 점은 다음 에이전트가 반드시 공격해야 한다.

```text
Q: v71 패치가 실제 live smoke에서 SK하이닉스 뉴스룸을 통과시킨 증거가 있는가?
A: 없다. v71 live smoke는 다른 후보/문서를 선택했다.
   현재 증거는 targeted fixture regression이다.
```

## 8. v71에서 해결되지 않은 핵심 병목

### 8.1 Brain/Web accepted claim이 0개다

파일:

```text
brain_web_readiness_gate_audit.json
brain_stage_promotion_audit.json
```

핵심:

```text
web_or_llm_accepted_claim_count = 0
brain_promoted_stage_row_count = 0
```

쉬운 예:

```text
문서를 하나 가져오고 LLM도 한 번 읽었지만,
"이 문장의 이 claim이 이 primitive에 점수를 준다"까지 닫힌 claim이 없다.
그러면 Stage로 올리면 안 된다.
```

### 8.2 Source quality가 아직 낮다

v71 web fetched document:

```text
삼부토건(001470) - 턴어라운드
https://www.valueline.co.kr/finance/turnaround/001470
```

문제:

```text
이건 issuer official / DART / KIND / CompanyGuide 원문이 아니다.
bounded web fetch는 되었지만, score-eligible claim으로 이어지지 않았다.
```

다음 방향:

```text
1. planner가 report/profile/market page를 골랐을 때 post-extraction feedback을 더 구체화해야 한다.
2. source router가 official-solvable gap을 더 강하게 official connector로 되돌려야 한다.
3. report PDF / CompanyNewsroom / IssuerIR가 실제 source document인지 lineage resolver를 더 촘촘히 해야 한다.
```

### 8.3 SK하이닉스 Full Thesis seed는 아직 완성되지 않았다

파일:

```text
samsung_hynix_full_thesis_smoke_audit.json
```

결론:

```text
verdict = PENDING_FULL_THESIS_REFRESH
```

해석:

```text
삼성전자/하이닉스를 운영 점수로 평가한 것이 아니다.
정밀 full thesis refresh가 아직 pending이라는 기록이다.
```

## 9. 다음 에이전트 공격 포인트

### 공격 1. "verified issuer original"이 너무 넓지 않은가?

현재 stem 비교는 이런 의도를 가진다.

```text
skhynix.com
news.skhynix.co.kr
  -> 같은 skhynix stem이므로 issuer 공식 계열 후보
```

공격해야 할 반례:

```text
가짜 도메인:
  news-skhynix.co.kr
  skhynix-investor.co.kr
  skhynix.example.com
  skhynix.com.fake-domain.com

기대:
  verified_issuer_original false
```

현재 패치가 모든 spoof case를 충분히 막는지는 추가 테스트가 필요하다.

권장 보강:

```text
CompanyGuide homepage stem match만으로 끝내지 말고,
issuer official domain candidate를 다음 중 하나로 제한한다.

1. exact homepage host
2. homepage subdomain
3. same brand stem + trusted country corporate suffix + title/snippet target alias
4. 가능하면 issuer homepage에서 outbound link로 발견된 newsroom/IR host
```

### 공격 2. CompanyGuide 홈페이지 seed가 stale이면 어떻게 되는가?

현재:

```text
data/cache/company_guide/{date}/{symbol}_snapshot.html
as_of_date보다 미래 snapshot은 제외
```

공격:

```text
과거 홈페이지 도메인이 바뀌었거나,
CompanyGuide snapshot이 오래됐거나,
상장사 홈페이지가 리뉴얼되어 newsroom host가 달라졌을 때
잘못된 official domain을 계속 신뢰하지 않는가?
```

권장:

```text
issuer_domain_source_as_of_date
issuer_domain_staleness_days
issuer_domain_resolution_status
```

를 leaf에 추가해 stale domain을 audit 가능하게 만든다.

### 공격 3. Source lineage 통과가 점수 unlock으로 새지 않는가?

v71 테스트는 두 케이스를 고정했다.

```text
제품 포트폴리오 공개:
  source lineage block은 없음
  customer_preorder_or_allocation score는 없음

HBM 고객 물량 배정 확정:
  source lineage block은 없음
  customer_preorder_or_allocation accepted
```

다음 에이전트는 아래 표현을 더 공격해야 한다.

```text
고객사와 협업 전시
엔비디아 부스 참여
고객 관심 확대
파트너십 재확인
AI 메모리 포트폴리오 소개
```

기대:

```text
profile / mention / partnership context일 수는 있어도
customer allocation / capacity pre-sold / revenue mix score로 바로 들어가면 안 된다.
```

### 공격 4. v71 live smoke가 SK하이닉스 resolver를 실제로 타지 않았다

중요:

```text
v71 live smoke web_fetched_documents = 1
그 문서는 삼부토건 Valueline page다.
verified_issuer_original = false
```

다음 검증:

```text
SK하이닉스만 명시적으로 target한 bounded live smoke
또는 FixtureSearchProvider가 아니라 실제 Naver 결과에서 news.skhynix.co.kr을 잡는 smoke
```

다만 운영 Stage로 포장하면 안 된다.

```text
목적은 source lineage resolver live exercise다.
점수/Stage 목적이 아니다.
```

### 공격 5. Planner가 official-solvable gap을 web/news로 보내는 문제가 남아 있다

v71 planner error:

```text
FCF/DART-solvable gap sent to general web/news: contract_visibility
```

의미:

```text
현금흐름/계약 가시성처럼 공식 자료로 먼저 풀어야 할 gap을
LLM planner가 웹/뉴스성 source로 보내려 했다.
```

프로젝트 규칙상 deterministic fallback query를 늘리면 안 된다.

해야 할 일:

```text
LLM planner feedback payload에
"이 gap은 DART/KIND/CompanyGuide/IssuerIR 먼저"라는 실패 사유를 되돌리고,
LLM이 다시 source task를 내게 해야 한다.
```

### 공격 6. Event Board Stage와 Full Thesis Stage 오인 가능성

v71에도 상태판 Stage row는 있다.

```text
Stage1 = 54
Stage2-Watch = 30
Red = 1
```

하지만 모두:

```text
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
```

다음 에이전트는 report/operator output에서 이 row가 운영 Stage처럼 표시되는 경로가 없는지 다시 찾아야 한다.

실패 예:

```text
"삼부토건 Stage2-Watch"
```

라고만 출력하면 안 된다.

정확한 출력:

```text
"삼부토건 CENSUS_EVENT_BOARD Stage2-Watch, NOT_FULL_THESIS_STAGE, full thesis refresh pending"
```

## 10. 현재 권장 다음 패치 순서

우선순위:

```text
P0. verified issuer original spoof 방지 테스트 추가
P0. SK하이닉스 공식 뉴스룸 resolver live-targeted smoke 추가
P0. planner가 official-solvable gap을 web/news로 보낼 때 LLM feedback retry를 더 강하게 닫기
P1. Valueline/market profile page를 source document가 아닌 profile/market page로 before-fetch 또는 post-fetch 차단
P1. Full Thesis refresh seed에서 target_archetype_status=BRAIN_HYPOTHESIS_REQUIRED가 계속 남는 원인 분리
P1. Brain/Web accepted claim 0개를 만든 raw assertion rejection reason을 planner feedback에 더 직접 연결
P2. FULL_THESIS promotion까지 가는 최소 real source-backed path를 하나 만들되, smoke/test label과 운영 label을 분리
```

절대 하면 안 되는 것:

```text
1. Event Board Stage를 운영 Stage로 승격 표시
2. web fetch가 됐다는 이유로 score 부여
3. 공식 도메인이라는 이유만으로 점수 unlock
4. LLM planner 실패를 deterministic 검색어 템플릿 추가로 숨기기
5. readiness minimum count를 낮춰 READY 만들기
```

## 11. 최종 판정

v71의 성과:

```text
네이버 검색으로 발견했지만 실제 issuer official domain 원문인 경우를 장부에 표시할 수 있게 했다.
공식 도메인 원문이어도 profile-only claim은 점수로 새지 않게 회귀 테스트를 추가했다.
전체 테스트 5103개가 통과했다.
```

v71의 한계:

```text
live smoke에서는 SK하이닉스 공식 뉴스룸 resolver가 실제로 exercise되지 않았다.
Brain/Web accepted claim은 여전히 0개다.
FULL_THESIS production Stage는 여전히 0개다.
```

따라서 최종 verdict:

```text
NOT_READY 유지.

Stage가 있는 것처럼 보이는 행은 CENSUS_EVENT_BOARD 상태판이다.
운영용 FULL_THESIS Stage는 아직 없다.
```

