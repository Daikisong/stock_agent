# LLM Theme Rebalance Agent Implementation Plan

작성일: 2026-06-08

목적: 기존 E2R 파이프라인에서 `확인 부족 -> Stage2/Yellow에서 정지`로 끝나는 문제를 고친다. 초반 cheap scan은 계속 싸게 거르되, 살아남은 소수 종목은 LLM이 아키타입 전환/혼합을 판단하고 꼬리 검색을 확장한 뒤 deterministic scorer가 최종 score와 Stage를 계산하게 만든다.

투자 권고가 아니라 Stage 상태기계 개선 문서다. 최종 출력은 `Stage 2`, `3-Yellow`, `3-Green`, `4B-watch` 같은 모니터링 언어를 유지한다.

## 1. 현재 로직 확인 결과

### 1.1 현재 production 흐름

현재 `E2RStandardFlow`는 다음 순서다.

```text
cheap scan
-> report radar
-> web research
-> feature engineering
-> deterministic score
-> deterministic Stage
-> optional LLM explanation
```

확인 위치:

- `src/e2r/pipeline/e2r_standard_flow.py:83-109`
- `src/e2r/pipeline/e2r_standard_flow.py:146-172`
- `src/e2r/pipeline/e2r_standard_flow.py:174-196`

문제는 LLM이 `Stage` 결정 뒤에만 돈다는 점이다. 현재 LLM은 설명자에 가깝다.

쉬운 예:

```text
NAVER 검색 결과에서 "NVIDIA, AI 데이터센터, GPU 클라우드"가 보여도
현재 구조에서는 점수/Stage가 이미 끝난 뒤 LLM이 설명만 한다.
그래서 LLM이 "이건 C26 플랫폼 + AI 인프라 전환"이라고 라우팅해서 추가 검색을 시키지 못한다.
```

### 1.2 현재 cheap scan은 초반 후보를 줄이는 역할을 이미 한다

`KoreaCheapScanner`는 가격, 공시, 실적, 리스크를 먼저 싸게 본다.

확인 위치:

- `src/e2r/cheap_scan/korea_scanner.py:96-179`
- 후보가 `EVENT_SEARCH` 또는 `DEEP_RESEARCH`일 때만 web research로 간다: `src/e2r/cheap_scan/korea_scanner.py:181-210`

따라서 이번 패치의 핵심은 초반 필터를 완화하는 것이 아니다. 살아남은 후보에 대해 조사 깊이를 늘리는 것이다.

### 1.3 현재 query escalation은 고정 검색어 중심이다

`queries_for_candidate()`는 cheap-scan reason code를 고정 query template으로 바꾼다.

확인 위치:

- `src/e2r/cheap_scan/query_escalation.py:13-103`
- `src/e2r/cheap_scan/query_escalation.py:143-158`
- `src/e2r/cheap_scan/query_escalation.py:161-190`

현재 검색어는 수주, CAPA, ASP, 실적 서프라이즈 중심이다. 플랫폼 기업이 AI 인프라 기업처럼 리레이팅되는 경우에는 부족하다.

쉬운 예:

```text
기존 검색:
NAVER 수주잔고
NAVER 목표주가 상향
NAVER 컨센서스 상회

필요한 검색:
NAVER Cloud GPUaaS 매출
NAVER AI 데이터센터 CAPEX FCF 영향
네이버클라우드 외부 고객 계약
NAVER NVIDIA 협력 매출 인식
```

### 1.4 현재 검색 결과 fetch 실패 시 증거가 대부분 사라진다

`WebResearchRunner`는 검색 결과를 rank/select한 뒤 URL 본문 fetch를 시도한다. fetch 실패 시 drop하고 다음 결과로 넘어간다.

확인 위치:

- 검색, ranking, selection: `src/e2r/research/web_research_runner.py:93-96`
- fetch 실패 drop: `src/e2r/research/web_research_runner.py:104-110`
- evidence는 parsed report/news/disclosure에서만 생성: `src/e2r/research/web_research_runner.py:126-132`

`PageFetcher`는 fixture-first이며 live fetch adapter가 아직 없다.

확인 위치:

- `src/e2r/research/page_fetcher.py:24-68`

문제:

```text
Naver Search API는 title/snippet/link/pubDate를 준다.
그런데 본문 fetch가 안 되면 title/snippet이 "조사 트리거"로도 남지 않는다.
그래서 NAVER AI 데이터센터 뉴스가 있어도 evidence_count=0으로 끝날 수 있다.
```

### 1.5 현재 LLM schema는 route와 expansion을 표현하지 못한다

현재 `LLMAnalystOutput`은 `missing_information`, `suggested_queries`는 있지만, 아키타입 전환/혼합 route, evidence slot 상태, Green unlock 조건을 표현하지 못한다.

확인 위치:

- `src/e2r/llm/schemas.py:12-42`
- `src/e2r/llm/research_analyst.py:15-28`

현재 analyst는 stage override를 제거한다. 이 원칙은 유지한다. 다만 LLM을 사후 설명자가 아니라 중간 research/router로 추가해야 한다.

### 1.6 현재 archetype은 단일 canonical 중심이다

`classify_v12_archetype()`은 하나의 `canonical_archetype_id`를 반환한다.

확인 위치:

- `src/e2r/archetype_classifier.py:32-95`
- 플랫폼 분류: `src/e2r/archetype_classifier.py:181-186`

현재 `ScoringPayload`도 하나의 canonical archetype만 정식 필드로 갖는다.

확인 위치:

- `src/e2r/scoring.py:41-59`
- runtime weight apply도 단일 canonical 기준: `src/e2r/scoring.py:177-204`

문제:

```text
NAVER = C26 플랫폼
하지만 현재 테마 = C26 플랫폼 + AI 인프라/데이터센터/GPU 클라우드

기존 구조는 C26 하나 또는 C02 하나로만 밀어 넣으려 한다.
정답은 primary + secondary/emerging route다.
```

### 1.7 Stage Green gate는 deterministic이다

Stage 3-Green은 점수, revision, visibility, risk를 보고 deterministic하게 결정된다.

확인 위치:

- Stage 흐름: `src/e2r/staging.py:126-204`
- Green 조건: `src/e2r/staging.py:254-280`

이 원칙은 유지한다. LLM이 직접 Green을 주면 안 된다. LLM은 조사와 정규화만 한다.

## 2. 목표 구조

새 구조:

```text
cheap scan
-> initial query plan
-> search API results
-> snippet evidence candidate 생성
-> LLM Theme Rebalance Agent
-> 부족한 evidence slot 식별
-> follow-up query 생성
-> search expansion loop
-> normalized evidence / parsed_fields 생성
-> FeatureEngineeringInput
-> DeterministicFeatureEngineer
-> ScoringPayload
-> DeterministicScorer
-> StageClassifier
```

핵심:

```text
LLM 역할:
- 아키타입 전환/혼합 판단
- 부족한 증거 슬롯 찾기
- 추가 검색어 생성
- 검색 결과에서 새 키워드 발견
- 증거를 parsed_fields와 route diagnostics로 정규화

Rule engine 역할:
- score 계산
- Green gate 통과 여부 판단
- 최종 Stage 결정
```

## 3. 1차 패치 원칙

### 3.1 제한을 빡세게 두지 않는다

초반 cheap scan에서 이미 많은 종목이 탈락한다. 따라서 후보로 살아남은 종목은 더 깊게 조사한다.

권장 기본값:

```text
EVENT_SEARCH 후보:
- 기본 max_queries_per_symbol: 40 유지
- LLM transition 감지 시 80까지 확장

DEEP_RESEARCH 후보:
- 기본 max_queries_per_symbol: 80
- LLM transition/mixed/emerging 감지 시 120까지 확장

확장 round:
- 기본 3
- 새 evidence slot이 계속 생기면 최대 5
```

중단 조건:

```text
1. 검색 예산 소진
2. 같은 URL/같은 claim만 반복
3. 2개 round 연속으로 새로운 evidence slot이 없음
4. thesis break 또는 hard risk가 명확함
5. Green/Yellow 판단에 필요한 핵심 slot이 충분히 채워짐
```

중요: `확인 부족`은 즉시 감점이 아니라 `추가 검색 실행`의 이유다.

### 3.2 검색 snippet은 조사 트리거로 살리되 Green 증거로 과대평가하지 않는다

검색 API snippet은 본문보다 약한 증거다. 하지만 버리면 안 된다.

추가할 필드:

```python
parsed_fields = {
    "search_snippet_only": True,
    "source_url": result.url,
    "source_query": result.query,
    "parser_confidence": 0.35,
}
```

Green 제한:

```text
search_snippet_only 뉴스만으로는 Green 불가
search_snippet_only는 LLM expansion trigger와 Stage1/Stage2 context에만 강하게 사용
Green은 report/disclosure/financial/consensus/full-body news 중 하나 이상이 bridge를 채워야 함
```

이유:

```text
"NVIDIA와 협력" 제목만 있으면 조사할 이유는 충분하다.
하지만 "본체 EPS/FCF가 오른다"는 증거는 아니다.
```

### 3.3 1차는 breaking change 없이 diagnostic route로 넣는다

`ScoringPayload`는 현재 단일 canonical 필드만 받는다. 바로 정식 구조를 바꾸면 영향 범위가 크다.

1차 구현:

```text
canonical_archetype_id = 기존 primary canonical 유지
diagnostic_scores에 route 숫자 진단 추가
parsed_fields에 theme evidence slot 추가
```

2차 구현:

```text
ScoringPayload에 ArchetypeRoute 정식 필드 추가
runtime weight profile에 emerging theme/blend profile 추가
```

## 4. 신규 모듈 설계

### 4.1 `src/e2r/llm/theme_router.py`

신규 클래스:

```python
class LLMThemeRebalanceAgent:
    def __init__(self, provider: ThemeRouteProvider) -> None: ...

    def route(self, inputs: ThemeRouteInput) -> ThemeRouteOutput:
        ...
```

역할:

```text
1. 검색 결과 title/snippet/body와 parsed_fields를 읽는다.
2. 현재 primary archetype 후보를 추정한다.
3. secondary/emerging theme 여부를 판단한다.
4. 부족한 evidence slot을 계산한다.
5. follow-up queries를 생성한다.
6. deterministic feature에 넣을 parsed_fields를 반환한다.
```

주의:

```text
LLMThemeRebalanceAgent는 Stage를 반환하지 않는다.
attempted_stage_override가 들어오면 버린다.
```

### 4.2 `src/e2r/llm/theme_schemas.py`

신규 dataclass:

```python
@dataclass(frozen=True)
class ThemeRouteInput:
    symbol: str
    company_name: str
    as_of_date: date
    candidate_reason_codes: tuple[str, ...]
    current_queries: tuple[str, ...]
    search_results: tuple[SearchResult, ...]
    parsed_fields: Mapping[str, Any]
    primary_archetype_hint: str | None = None

@dataclass(frozen=True)
class EvidenceSlotStatus:
    slot: str
    status: str  # missing | partial | confirmed | contradicted
    confidence: float
    evidence_refs: tuple[str, ...]
    next_queries: tuple[str, ...]

@dataclass(frozen=True)
class ThemeRouteOutput:
    thesis_state: str  # stable | transitioning | mixed | emerging | broken
    primary_archetype_id: str | None
    secondary_archetype_id: str | None
    emerging_theme_id: str | None
    route_confidence: float
    evidence_slots: tuple[EvidenceSlotStatus, ...]
    suggested_queries: tuple[str, ...]
    normalized_parsed_fields: Mapping[str, Any]
    green_unlock_candidate: bool
    stop_reason: str | None = None
```

허용 slot 예:

```text
eps_fcf_bridge
cloud_revenue_bridge
external_customer_contract
rpo_or_backlog_bridge
gpu_capacity_or_datacenter_capa
capex_fcf_burden
opm_or_unit_economics
consensus_revision
valuation_rerating
risk_overlay
```

### 4.3 `src/e2r/research/search_snippet_evidence.py`

신규 함수:

```python
def news_item_from_search_result(
    *,
    result: SearchResult,
    company_name: str,
    symbol: str,
    sector: str | None,
    market: Market,
    as_of_date: date,
    company_aliases: Sequence[str] = (),
) -> NewsItem | None:
    ...
```

생성 규칙:

```text
title은 필수, snippet은 없어도 됨
published_at이 as_of_date 이후면 None
회사명/별칭/심볼 또는 source_query의 회사 단서가 없으면 None
강한 테마 키워드가 없으면 None
source_tier = SourceTier.TIER_3
confidence = 0.25 ~ 0.55
parsed_fields.search_snippet_only = True
parsed_fields.source_url = result.url
parsed_fields.source_query = result.query
parsed_fields.source_title = result.title
```

중요:

```text
한국 종목 symbol은 035420처럼 숫자인 경우가 많다.
따라서 symbol만 보면 "네이버, 엔비디아와..." 같은 제목을 NAVER 증거로 연결하지 못한다.
company_name, company_aliases, source_query를 함께 봐야 한다.
```

쉬운 예:

```text
symbol = 035420
company_name = NAVER
company_aliases = ("네이버", "네이버클라우드")
title = "네이버, 엔비디아 GPU 기반 AI 데이터센터 확대"
-> 회사 별칭과 테마 키워드가 모두 있으므로 snippet evidence 가능
```

날짜 없는 검색 결과 처리:

```text
result.published_at is None이면 synthetic published_at = as_of_date 08:00을 넣는다.
대신 parsed_fields.date_verified = False
parsed_fields.search_snippet_date_unverified = True
parsed_fields.green_allowed_by_date = False
를 반드시 남긴다.

날짜가 확인되지 않은 snippet evidence는 Yellow/조사 확장에는 쓸 수 있지만
그 자체로 Stage 3-Green unlock 증거가 되면 안 된다.
```

추가 keyword parser:

```text
AI 인프라:
- AI 데이터센터
- 데이터센터
- GPU
- GPUaaS
- NVIDIA
- 엔비디아
- 클라우드
- AI factory
- SuperPod

수익화 bridge:
- 매출
- 영업이익
- OPM
- EPS
- FCF
- 컨센서스 상향
- 목표주가 상향

리스크:
- CAPEX
- 투자비
- 감가상각
- 비용 증가
- FCF 부담
- 합병 지연
```

### 4.4 `configs/e2r_emerging_theme_profiles_v1.json`

신규 config. 1차 구현에서는 코드에 하드코딩하지 않고 config로 둔다.

예시:

```json
{
  "EMERGING_AI_INFRA_PLATFORM_DATACENTER": {
    "allowed_primary_archetypes": [
      "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
      "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
      "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"
    ],
    "positive_keywords": [
      "AI 데이터센터",
      "GPUaaS",
      "NVIDIA",
      "엔비디아",
      "AI cloud",
      "데이터센터",
      "네이버클라우드"
    ],
    "required_green_slots": [
      "eps_fcf_bridge",
      "cloud_revenue_bridge",
      "capex_fcf_burden",
      "consensus_revision"
    ],
    "risk_slots": [
      "capex_burden",
      "cost_increase",
      "mou_only",
      "price_only_blowoff"
    ],
    "query_templates": [
      "{company} GPUaaS 매출",
      "{company} AI 데이터센터 CAPEX FCF",
      "{company} 클라우드 영업이익률",
      "{company} AI 인프라 EPS 상향 리포트",
      "{company} NVIDIA 협력 계약 매출"
    ]
  }
}
```

## 5. 기존 파일별 변경안

### 5.1 `src/e2r/research/web_research_runner.py`

변경 위치:

- fetch 실패 처리: `src/e2r/research/web_research_runner.py:104-110`
- unknown document drop: `src/e2r/research/web_research_runner.py:123-124`
- parsed evidence 생성: `src/e2r/research/web_research_runner.py:126-132`
- news parser: `src/e2r/research/web_research_runner.py:251-271`

선행 보정:

```text
snippet evidence를 붙이기 전에 뉴스 evidence_id 충돌을 먼저 고친다.
현재 evidence_builder.py와 features.py는 news:{symbol}:{date}:{source} 형태라
같은 날짜/같은 source 뉴스가 여러 개면 하나로 합쳐질 수 있다.
```

필수 변경:

```text
src/e2r/pipeline/evidence_builder.py
- evidence_from_news_item()의 evidence_id에 stable hash 추가
- url_or_identifier에는 parsed_fields.source_url 또는 source_url equivalent 저장

src/e2r/features.py
- _evidence_ids()의 news id도 동일한 stable hash 규칙 사용
```

권장 id:

```text
news:{symbol}:{published_date}:{source}:{hash(source_url || title)}
```

패치:

```python
if not fetch.ok or not fetch.text:
    snippet_news = news_item_from_search_result(
        result=result,
        company_name=inputs.company_name,
        symbol=inputs.symbol,
        sector=inputs.sector,
        market=inputs.market,
        as_of_date=inputs.as_of_date,
        company_aliases=inputs.company_aliases,
    )
    if snippet_news is not None:
        parsed_news.append(snippet_news)
        dropped.append(DroppedSearchResult(result=result, reason="fetch_unavailable_snippet_evidence_used"))
    else:
        dropped.append(DroppedSearchResult(result=result, reason=fetch.reason or "fetch_unavailable"))
    continue
```

추가 패치:

```text
fetch는 성공했지만 classify_search_result(result)가 unknown이면
바로 unknown_document_type으로 버리기 전에 snippet/title 보존 후보로 한 번 더 본다.
```

쉬운 예:

```text
Naver web/doc 결과:
title = "네이버클라우드 AI 데이터센터 투자 확대"
fetch.ok = True
classify_search_result = unknown
-> 현재는 unknown_document_type drop
-> 수정 후에는 search_snippet_only NewsItem 후보로 보존
```

추가 진단:

```text
fetch_unavailable_snippet_evidence_used
unknown_document_type_snippet_evidence_used
snippet_evidence_count
snippet_evidence_source_count
```

### 5.2 `src/e2r/research/free_web_research_runner.py`

변경 위치:

- initial query loop: `src/e2r/research/free_web_research_runner.py:98-133`
- WebResearchRunner 호출: `src/e2r/research/free_web_research_runner.py:139-157`
- FeatureEngineeringInput 생성: `src/e2r/research/free_web_research_runner.py:158-169`

패치:

```text
1. initial query 실행
2. collected SearchResult를 ThemeRouteInput으로 전달
3. LLMThemeRebalanceAgent.route()
4. suggested_queries를 SearchBudgetTracker로 추가 실행
5. 새 결과가 있으면 최대 round까지 반복
6. expansion QuerySpec까지 포함한 final_query_plan 생성
7. 최종 results_by_query와 final_query_plan을 WebResearchRunner에 전달
8. route output의 normalized_parsed_fields를 NewsItem 또는 FeatureEngineeringInput에 주입
```

절대 빠지면 안 되는 연결:

```text
WebResearchRunner는 QueryPlan.queries에 있는 query만 다시 읽는다.
따라서 expansion query 결과를 results_by_query에만 넣고 QueryPlan에 넣지 않으면
실제로 파싱/스코어에 사용되지 않는다.
```

구현 형태:

```python
final_specs = tuple(query_plan.queries) + tuple(expansion_specs)
final_query_plan = QueryPlan(
    company_name=query_plan.company_name,
    symbol=query_plan.symbol,
    sector=query_plan.sector,
    market=query_plan.market,
    as_of_date=query_plan.as_of_date,
    queries=final_specs,
)

web_runner = WebResearchRunner(
    query_planner=_FixedQueryPlanner(final_query_plan),
    search_provider=FixtureSearchProvider(results_by_query=results_by_query),
    ...
)
```

dedupe 규칙:

```text
query는 normalized query 기준으로 중복 제거
search result는 URL 기준으로 중복 제거
같은 URL이라도 더 좋은 published_at/source metadata가 있으면 더 완전한 row를 선택
```

새 입력 필드:

```python
@dataclass(frozen=True)
class FreeWebResearchInput:
    ...
    company_aliases: tuple[str, ...] = field(default_factory=tuple)
    candidate_reason_codes: tuple[str, ...] = field(default_factory=tuple)
    theme_rebalance_enabled: bool = False
    theme_route_provider: ThemeRouteProvider | None = None
    max_theme_expansion_rounds: int = 3
```

호출 지점 호환성:

```text
FreeWebResearchInput은 여러 곳에서 이미 생성된다.
새 필드는 모두 default를 가져야 기존 호출이 깨지지 않는다.
```

확인된 기존 호출:

```text
src/e2r/pipeline/e2r_standard_flow.py
src/e2r/pipeline/korea_live_lite.py
src/e2r/cheap_scan/korea_scanner.py
src/e2r/research/asof_web_research.py
tests/test_free_web_research_runner.py
```

새 result 필드:

```python
@dataclass(frozen=True)
class WebResearchPipelineResult:
    ...
    theme_route: ThemeRouteOutput | None = None
    expansion_queries_run: tuple[str, ...] = field(default_factory=tuple)
    theme_route_diagnostics: Mapping[str, Any] = field(default_factory=dict)
```

provider 규칙:

```text
theme_rebalance_enabled=True인데 theme_route_provider가 None이면
LLM이 기본형이라고 판단한 것처럼 조용히 기록하지 않는다.
theme_route_diagnostics.theme_rebalance_status = "disabled_no_provider"를 남기고
원래의 canonical deterministic scoring만 실행한다.
```

이유:

```text
"LLM이 판단해서 아키타입 전환을 봤다"와
"LLM provider가 없어서 전환 판단 자체를 못 했다"는 완전히 다르다.
둘을 섞으면 나중에 왜 Green이 안 나왔는지 추적할 수 없다.
```

### 5.3 `src/e2r/cheap_scan/query_escalation.py`

변경 위치:

- 고정 query template: `src/e2r/cheap_scan/query_escalation.py:13-103`
- `queries_for_candidate`: `src/e2r/cheap_scan/query_escalation.py:151-158`

패치:

```text
고정 query는 initial seed로만 사용한다.
LLM suggested_queries가 있으면 follow-up query로 추가한다.
```

주의:

```text
정적 template에 모든 산업을 다 넣으려고 하지 않는다.
그렇게 하면 parser 유지보수가 불가능하다.
산업 전환 감지는 LLM route가 맡는다.
```

### 5.4 `src/e2r/features.py`

변경 위치:

- sector profile inference: `src/e2r/features.py:225-234`
- diagnostic_scores 생성: `src/e2r/features.py:241-247`
- archetype classifier 호출: `src/e2r/features.py:251-263`
- parsed_fields 수집: `src/e2r/features.py:955-1025`
- evidence family diagnostics: `src/e2r/features.py:852-865`

패치:

1. `ThemeRouteOutput.normalized_parsed_fields`는 실제 SearchResult/NewsItem/Report/Disclosure evidence ref에 붙어야 한다.

주의:

```text
LLM route만으로 별도 synthetic NewsItem을 만들면 안 된다.
그렇게 하면 "LLM이 말한 것"이 "원천 증거"처럼 evidence family/source_count에 들어가
정보신뢰도와 Green gate를 조용히 올릴 수 있다.
```

정답:

```text
source_url/source_query/evidence_ref가 있는 route field:
-> 해당 NewsItem.parsed_fields에 merge 가능

source_url/source_query/evidence_ref가 없는 route field:
-> WebResearchPipelineResult.theme_route_diagnostics에만 보관
-> score component 직접 상승 금지
```

2. 아래 parsed_fields를 FeatureEngineer가 인식하게 한다.

```text
theme_transition_detected
theme_mixed_archetype
emerging_theme_ai_infra_platform_datacenter
gpu_cloud_revenue_visible
ai_datacenter_capa_visible
external_customer_contract_visible
cloud_opm_or_unit_economics_visible
capex_fcf_burden_checked
capex_fcf_burden_risk
ai_infra_consensus_revision_visible
llm_deep_research_completed
llm_expansion_rounds
llm_new_evidence_slot_count
search_snippet_only_count
```

3. `diagnostic_scores`에 route 숫자값 추가:

```text
theme_transition_detected = 0/100
theme_route_confidence = 0~100
emerging_theme_ai_infra_platform_datacenter = 0/100
green_unlock_evidence_score = 0~100
llm_deep_research_completed = 0/100
search_snippet_only_evidence_count_capped = 0~100
```

주의:

```text
diagnostic_scores에는 숫자만 넣는다.
emerging_theme_id, thesis_state, missing_slots 같은 문자열은 parsed_fields나
WebResearchPipelineResult.theme_route_diagnostics에 남긴다.
```

4. snippet-only 뉴스가 evidence family를 과대평가하지 않도록 보정:

```text
evidence_family_news는 유지
하지만 snippet-only만 있을 경우:
- snippet_only_news_family = 100
- full_news_family = 0
- Green unlock에는 full_news_family 또는 report/consensus/disclosure/financial 필요
```

5. snippet-only 뉴스가 information confidence를 과대평가하지 않도록 보정:

```text
현재 _information_confidence_score()는 inputs.news_items가 있으면 source_count를 올린다.
따라서 search_snippet_only 뉴스만 있는 경우:
- information_confidence source_count 가산을 제한
- 또는 diagnostic_scores.snippet_only_information_confidence_discount 적용
```

쉬운 예:

```text
Naver 제목/요약 1개만 있음
-> "뉴스 source가 있다"는 사실은 맞지만,
   full article/report/disclosure와 같은 신뢰도로 보지 않는다.
```

### 5.5 `src/e2r/sector_profiles.py`

변경 위치:

- 현재 SectorProfile enum: `src/e2r/sector_profiles.py`
- profile inference: `src/e2r/sector_profiles.py`

패치:

```python
class SectorProfile(str, Enum):
    ...
    AI_INFRA_PLATFORM = "AI_INFRA_PLATFORM"
```

추가 시 주의:

```text
기존 enum 순서와 _PROFILE_IDS 값을 바꾸지 않는다.
새 profile은 마지막 id로 추가한다.

현재 마지막은 BATTERY_OVERHEAT = 7이므로
AI_INFRA_PLATFORM은 8처럼 뒤에 붙인다.
```

Profile definition:

```text
preferred_visibility_fields:
- gpu_cloud_revenue_visible
- external_customer_contract_visible
- ai_datacenter_capa_visible
- ai_infra_consensus_revision_visible

preferred_bottleneck_fields:
- ai_datacenter_capa_visible
- gpu_capacity_or_superpod_visible
- cloud_capacity_constraint

preferred_pricing_fields:
- cloud_opm_or_unit_economics_visible
- premium_ai_cloud_pricing
- target_multiple_rerating

red_team_risk_fields:
- capex_fcf_burden_risk
- mou_only
- price_only_blowoff_score
- cost_increase_without_revenue

contract_required_for_green:
- false
```

쉬운 예:

```text
변압기 회사는 수주/장기계약이 Green 핵심이다.
플랫폼 AI 인프라 전환은 장기 공급계약보다
"클라우드 매출, 고객 계약, CAPEX 대비 FCF, 컨센서스 상향"이 Green 핵심이다.
```

### 5.6 `src/e2r/archetype_classifier.py`

변경 위치:

- single classification return: `src/e2r/archetype_classifier.py:32-95`
- C26/C27/C28 분기: `src/e2r/archetype_classifier.py:181-186`

1차 패치:

```text
primary canonical은 기존대로 C26/C28 등을 유지한다.
LLM route는 classification reason/diagnostics로 전달한다.
```

2차 패치:

```python
@dataclass(frozen=True)
class ArchetypeRoute:
    primary: ArchetypeClassification
    secondary_canonical_archetype_id: str | None
    emerging_theme_id: str | None
    thesis_state: str
    confidence: float
```

주의:

```text
종목명 하드코딩 금지.
"NAVER"가 아니라 "platform + ai infra + datacenter + gpu cloud + revenue bridge" 패턴으로 판단한다.
```

추가 주의:

```text
secondary_canonical_archetype_id나 emerging_theme_id를 ScoringPayload.canonical_archetype_id에 넣지 않는다.
ScoringPayload는 canonical_archetype_id와 large_sector_id가 taxonomy상 서로 맞아야 한다.
예: primary C26은 L8인데 secondary C31은 L10이다.
이 둘을 canonical/large_sector에 섞어 넣으면 scoring validation에서 깨진다.
```

정답:

```text
canonical_archetype_id = primary canonical만 사용
secondary_canonical_archetype_id = parsed_fields 또는 route_diagnostics에 보관
emerging_theme_id = parsed_fields 또는 route_diagnostics에 보관
```

### 5.7 `src/e2r/scoring.py`

변경 위치:

- `ScoringPayload`: `src/e2r/scoring.py:41-59`
- runtime weight apply: `src/e2r/scoring.py:177-204`
- stage3 cross evidence buffer: `src/e2r/scoring.py:236-258`
- non-price bridge: `src/e2r/scoring.py:270-284`

1차 패치:

```text
ScoringPayload schema는 유지.
diagnostic_scores 기반으로 emerging theme score를 추가한다.
```

예:

```text
green_unlock_evidence_score =
  eps_fcf_bridge 25
  cloud_revenue_bridge 20
  capex_fcf_burden_checked 15
  consensus_revision 20
  external_customer_or_capacity 20
```

추가 guard:

```text
search_snippet_only만 있으면 stage3_cross_evidence_green_buffer 적용 금지
emerging_theme_active인데 llm_deep_research_completed가 0이면 Green buffer 적용 금지
llm_route_unbacked_by_source가 1이면 component bonus 적용 금지
```

2차 패치:

```text
runtime_profile.apply()에 blend profile 지원
primary C26 60% + emerging AI infra platform 40% 같은 route weighting 가능
```

하지만 1차는 scoring total 자체를 크게 흔들기보다 feature slot을 채워 기존 component 계산이 자연스럽게 올라가게 한다.

### 5.8 `src/e2r/staging.py`

변경 위치:

- Stage 흐름: `src/e2r/staging.py:126-204`
- Stage3 Green: `src/e2r/staging.py:254-280`
- non-price bridge: `src/e2r/staging.py:331-345`

패치:

```python
def _emerging_theme_green_allowed(score: ScoreSnapshot) -> bool:
    if _score_diagnostic(score, "emerging_theme_active") <= 0:
        return True
    if _score_diagnostic(score, "llm_deep_research_completed") <= 0:
        return False
    if _score_diagnostic(score, "green_unlock_evidence_score") < 60.0:
        return False
    if _score_diagnostic(score, "snippet_only_green_block") > 0:
        return False
    return True
```

그리고 `_is_stage_3_green()`에 추가:

```python
and StageClassifier._emerging_theme_green_allowed(score)
```

이건 Green을 막기 위한 제한이 아니라, LLM이 충분히 찾아본 경우 Green을 열어주기 위한 조건이다.

쉬운 예:

```text
NVIDIA 협력 뉴스 제목만 있음:
emerging_theme_active = 100
llm_deep_research_completed = 100
green_unlock_evidence_score = 25
-> Green 불가, Yellow/Stage2

NVIDIA 협력 + GPUaaS 매출 + 클라우드 고객 + EPS/OP 상향 리포트:
green_unlock_evidence_score = 75
-> 기존 Green 조건도 통과하면 3-Green 가능
```

추가 주의:

```text
KoreaLiveLite에는 StageClassifier 이후에도 별도 Green 후처리 guard가 있다.
_enforce_cross_evidence_stage3_green()는 independent_evidence_types를 본다.
snippet-only news가 독립 news evidence로 계산되면 Green guard를 우회할 수 있으므로
_independent_evidence_types()에서도 search_snippet_only/date_unverified는 제외한다.
```

### 5.9 `src/e2r/pipeline/korea_live_lite.py`

변경 위치:

- candidate별 web research loop: `src/e2r/pipeline/korea_live_lite.py` 내 selected_candidates loop
- selected candidate cap: `_select_candidates_for_research`
- `_search_budget()` currently `max_queries_per_symbol=40`

패치:

```text
1. FreeWebResearchInput에 candidate.reason_codes 전달
2. theme_rebalance_enabled config 추가
3. candidate가 DEEP_RESEARCH이면 max_queries_per_symbol을 80 이상으로 설정
4. LLM transition 감지 후 expansion loop에서는 120까지 허용
5. run_log에 theme_route, expansion_queries, missing_slots, stop_reason 저장
```

config 필드:

```python
theme_rebalance_enabled: bool = False
theme_route_provider: ThemeRouteProvider | None = None
max_theme_expansion_rounds: int = 3
```

run log 저장 규칙:

```text
ThemeRouteOutput dataclass를 그대로 JSON에 넣지 않는다.
run_log에는 plain dict/list/str/number/bool만 넣는다.
```

예:

```text
theme_route = {
  "thesis_state": "transitioning",
  "primary_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "emerging_theme_id": "EMERGING_AI_INFRA_PLATFORM_DATACENTER",
  "route_confidence": 0.72,
  "missing_slots": ["eps_fcf_bridge", "capex_fcf_burden"],
  "stop_reason": "max_rounds_or_no_new_evidence"
}
```

주의:

```text
전체 일일 Naver budget은 유지한다.
하지만 후보당 query cap은 살아남은 후보에게 더 넉넉하게 준다.
```

추가 run_log 필드:

```text
theme_routes: tuple[Mapping[str, Any], ...]
theme_expansion_queries: tuple[Mapping[str, Any], ...]
theme_missing_slots: tuple[Mapping[str, Any], ...]
theme_rebalance_status_counts: Mapping[str, int]
```

이유:

```text
targeted_smoke_results에만 남기면 production 후보에서는 route 판단을 추적하기 어렵다.
run_log 최상위에도 symbol별 route summary가 있어야 한다.
```

### 5.10 `src/e2r/pipeline/e2r_standard_flow.py`

변경 위치:

- config: `src/e2r/pipeline/e2r_standard_flow.py:30-45`
- web research input 생성: `src/e2r/pipeline/e2r_standard_flow.py:151-169`
- 현재 LLM 위치: `src/e2r/pipeline/e2r_standard_flow.py:174-196`

패치:

```text
1. E2RStandardConfig에도 theme_rebalance_enabled/theme_route_provider 추가
2. FreeWebResearchInput에 theme route 설정 전달
3. 기존 _run_llm()은 사후 설명용으로 유지
4. route LLM과 사후 설명 LLM을 같은 의미로 섞지 않는다
```

이유:

```text
E2RStandardFlow는 현재 LLM을 score/stage 이후에만 호출한다.
사용자가 원하는 "확인 부족하면 검색 확장"은 score/stage 이전 FreeWebResearchRunner 단계에서 돌아야 한다.
```

쉬운 예:

```text
사후 설명 LLM:
- "현재 Stage 2인 이유는 증거 부족입니다"라고 설명

theme rebalance LLM:
- "증거 부족이면 네이버클라우드 매출, CAPEX, 컨센서스 상향을 더 검색하세요"라고 query를 확장
```

### 5.10.1 `src/e2r/cheap_scan/korea_scanner.py`와 `src/e2r/research/asof_web_research.py`

직접 `FreeWebResearchInput`을 생성하는 보조 경로다.

패치 원칙:

```text
기본값 때문에 기존 실행은 깨지지 않아야 한다.
route를 켜는 경우에만 explicit config를 전달한다.
as-of replay에서 route를 켜면 AsOfDateFilteredSearchProvider를 반드시 통과한다.
```

주의:

```text
as_of_date=2024-06-01 replay인데 LLM이 2026년에 알려진 테마를 query에 섞으면 안 된다.
LLM input은 as_of_date 이전 evidence만 넣고,
suggested_queries에도 as_of_date 이후 연도/사건이 들어가면 validation에서 제거한다.
```

쉬운 예:

```text
as_of_date = 2024-06-01
LLM suggested query = "NAVER 2026 엔비디아 데이터센터 계약"
-> query 자체가 미래 단서를 포함하므로 실행하지 않는다.
```

### 5.11 package export와 import cycle 방지

신규 모듈을 추가하면 아래 export도 같이 맞춘다.

```text
src/e2r/llm/__init__.py
src/e2r/research/__init__.py
src/e2r/research/free_web_research_runner.py __all__
src/e2r/research/web_research_runner.py __all__
```

주의:

```text
theme_schemas.py에서 SearchResult가 필요하면
from e2r.research.search_provider import SearchResult
처럼 leaf module에서 직접 import한다.

from e2r.research import SearchResult
처럼 package import를 쓰면
free_web_research_runner import 순서와 섞여 순환 import가 날 수 있다.
```

## 6. NAVER형 케이스 처리 예시

이 예시는 구현 하드코딩이 아니다. 테스트 fixture 이름으로만 사용한다.

### 6.1 1차 검색에서 발견되는 내용

```text
NAVER + NVIDIA
NAVER + AI 데이터센터
NAVER + GPU 클라우드
NAVER + 네이버클라우드
```

LLM route:

```json
{
  "thesis_state": "transitioning",
  "primary_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "secondary_archetype_id": null,
  "emerging_theme_id": "EMERGING_AI_INFRA_PLATFORM_DATACENTER",
  "route_confidence": 0.72
}
```

### 6.2 부족 slot

```text
eps_fcf_bridge: missing
cloud_revenue_bridge: partial
external_customer_contract: missing
capex_fcf_burden: missing
consensus_revision: missing
valuation_rerating: partial
```

### 6.3 LLM follow-up queries

```text
NAVER Cloud GPUaaS 매출
네이버클라우드 GPUaaS 외부 고객 계약
NAVER AI 데이터센터 CAPEX FCF
NAVER AI 인프라 EPS 상향 리포트
NAVER 클라우드 영업이익률 개선
NAVER NVIDIA 협력 계약 규모
```

### 6.4 Stage 결과 예시

Case A:

```text
증거:
- NVIDIA 협력 뉴스
- 주가 급등
- AI 데이터센터 언급

부족:
- 매출/OP/EPS/FCF 연결 없음
- 고객 계약 없음
- CAPEX 부담 확인 없음

결과:
- Stage2 또는 3-Yellow
```

Case B:

```text
증거:
- NVIDIA 협력 뉴스
- GPUaaS 매출 또는 외부 고객 계약
- 클라우드 OP/OPM 개선
- EPS/OP 컨센서스 상향 리포트
- CAPEX/FCF 부담이 감당 가능하다는 근거

결과:
- 기존 Green 조건까지 통과하면 3-Green 가능
```

## 7. 테스트 계획

### 7.1 신규 테스트 파일

```text
tests/test_llm_theme_rebalance_router.py
tests/test_search_snippet_evidence.py
tests/test_free_web_research_expansion_loop.py
tests/test_emerging_theme_green_gate.py
tests/test_theme_rebalance_public_exports.py
tests/test_theme_rebalance_field_validation.py
tests/test_korea_live_lite_theme_rebalance_guard.py
```

### 7.2 테스트 1: snippet fetch 실패를 evidence candidate로 살린다

목표:

```text
SearchResult(title/snippet 있음)
PageFetcher fetch 실패
그래도 parsed_news에 snippet-only NewsItem 생성
evidence에 news evidence 생성
search_snippet_only = True
```

검증:

```text
fetch_unavailable_snippet_evidence_used drop reason 존재
evidence_family_news = 1
snippet_only_green_block = 1
```

추가 검증:

```text
같은 symbol/date/source 뉴스 2개가 서로 다른 URL/title이면 evidence_id가 달라야 한다.
예: 같은 날 네이버뉴스 기사 A, 기사 B가 모두 살아남아야 한다.
```

### 7.3 테스트 2: LLM이 부족 slot 기반 follow-up query를 만든다

Fixture:

```text
title: NAVER, NVIDIA와 AI 데이터센터 협력
snippet: 네이버클라우드 GPU 인프라 협력
```

Fake provider output:

```text
thesis_state = transitioning
emerging_theme_id = EMERGING_AI_INFRA_PLATFORM_DATACENTER
missing slots = eps_fcf_bridge, capex_fcf_burden, consensus_revision
suggested_queries = NAVER Cloud GPUaaS 매출, NAVER AI 데이터센터 CAPEX FCF
```

검증:

```text
FreeWebResearchRunner가 suggested_queries를 실제로 추가 실행
expansion_queries_run에 기록
web_result.queries_run에도 expansion query가 포함
web_result.query_plan.queries에도 expansion QuerySpec 포함
```

### 7.4 테스트 3: snippet-only로는 Green이 열리지 않는다

Fixture:

```text
검색 snippet만 AI/NVIDIA 강함
리포트/공시/실적/컨센서스 없음
```

검증:

```text
emerging_theme_active = 100
llm_deep_research_completed = 100
green_unlock_evidence_score < 60
Stage != 3-Green
```

### 7.5 테스트 4: 숫자 bridge가 있으면 Green 가능

Fixture:

```text
AI 인프라 전환 뉴스
GPUaaS 매출 가시화 parsed_field
cloud_opm_or_unit_economics_visible
ai_infra_consensus_revision_visible
capex_fcf_burden_checked
red_team low
```

검증:

```text
primary C26 유지
emerging_theme_ai_infra_platform_datacenter = 100
green_unlock_evidence_score >= 60
기존 Stage3 Green component 조건도 충족 시 Stage 3-Green
```

### 7.6 테스트 5: as_of_date 누수 방지

Fixture:

```text
as_of_date = 2026-06-08
검색 결과 published_at = 2026-06-09
```

검증:

```text
검색 결과 제외
LLM input에도 들어가지 않음
```

### 7.7 테스트 6: 날짜 없는 snippet은 Green unlock 불가

Fixture:

```text
as_of_date = 2026-06-08
SearchResult.published_at = None
title = "네이버 AI 데이터센터 확대"
```

검증:

```text
snippet NewsItem은 synthetic published_at = 2026-06-08 08:00으로 생성
parsed_fields.date_verified = False
parsed_fields.search_snippet_date_unverified = True
Stage 3-Green unlock에는 사용되지 않음
```

### 7.8 테스트 7: package export와 import cycle

검증:

```text
from e2r.llm import ThemeRouteInput, ThemeRouteOutput, FakeThemeRouteProvider
from e2r.research import news_item_from_search_result
가 깨지지 않는다.
```

### 7.9 테스트 8: unknown document type도 snippet 보존 후보

Fixture:

```text
SearchResult.is_news = False
SearchResult.is_report_domain = False
fetch.ok = True
classify_search_result = unknown
title/snippet에 AI 데이터센터 강한 키워드 존재
```

검증:

```text
unknown_document_type_snippet_evidence_used drop reason 존재
parsed_news에 search_snippet_only NewsItem 생성
Stage 3-Green unlock에는 사용되지 않음
```

### 7.10 테스트 9: LLM field 타입 validation

Fixture:

```text
gpu_cloud_revenue_visible = "visible"
op_revision_pct = "상향"
missing_slots = ["eps_fcf_bridge"]
```

검증:

```text
boolean/numeric field가 잘못된 타입이면 route validation error 또는 field drop
diagnostic_scores에는 숫자 0~100만 들어감
문자열 route 정보는 route_diagnostics에만 들어감
```

### 7.11 테스트 10: snippet-only는 information confidence 할인

Fixture:

```text
news_items = snippet-only 1개
research_reports/disclosures/consensus 없음
```

검증:

```text
evidence_family_news는 기록
snippet_only_news_family = 100
full_news_family = 0
information_confidence가 full news처럼 올라가지 않음
```

### 7.12 테스트 11: live-lite independent evidence guard

Fixture:

```text
cheap evidence 1종 + snippet-only news
StageClassifier 결과는 일단 3-Green 후보
```

검증:

```text
_independent_evidence_types()가 snippet-only news를 제외
KoreaLiveLite 후처리에서 Stage 3-Yellow로 downgrade
```

## 8. 구현 순서

### Phase 1: 검색 snippet 보존

파일:

```text
src/e2r/research/search_snippet_evidence.py
src/e2r/research/web_research_runner.py
src/e2r/pipeline/evidence_builder.py
src/e2r/features.py
tests/test_search_snippet_evidence.py
tests/test_theme_rebalance_field_validation.py
```

작업:

```text
1. 뉴스 evidence_id collision 선행 수정
2. search result -> snippet NewsItem 변환 함수 추가
3. fetch 실패 시 snippet evidence 보존 경로 적용
4. unknown_document_type snippet evidence 보존 경로 적용
5. snippet-only/date-unverified 진단 parsed_fields 추가
6. 테스트 작성
```

완료 기준:

```text
NAVER 같은 live search 결과에서 URL fetch가 안 되어도 evidence_count가 0으로 끝나지 않는다.
```

### Phase 2: LLM Theme Router schema와 fake provider

파일:

```text
src/e2r/llm/theme_schemas.py
src/e2r/llm/theme_router.py
src/e2r/llm/provider.py 또는 별도 src/e2r/llm/theme_provider.py
src/e2r/llm/theme_profiles.py
src/e2r/llm/__init__.py
tests/test_llm_theme_rebalance_router.py
tests/test_theme_rebalance_field_validation.py
```

작업:

```text
1. ThemeRouteInput/Output dataclass 추가
2. ThemeRouteProvider protocol 추가
3. FakeThemeRouteProvider 추가
4. route output validation 추가
5. emerging theme config loader 추가
6. public export 추가
7. suggested query as_of_date validation 추가
```

완료 기준:

```text
LLM output이 Stage를 직접 바꾸지 않고 query/slot/parsed_fields만 반환한다.
```

### Phase 3: FreeWebResearchRunner expansion loop

파일:

```text
src/e2r/research/free_web_research_runner.py
tests/test_free_web_research_expansion_loop.py
```

작업:

```text
1. FreeWebResearchInput에 theme_rebalance_enabled, candidate_reason_codes 추가
2. initial search 후 ThemeRouteAgent 호출
3. suggested_queries를 budget tracker로 실행
4. round별 novelty check 추가
5. expansion QuerySpec을 final QueryPlan에 추가
6. expansion_queries_run/result.theme_route 기록
```

완료 기준:

```text
"확인 부족"이 추가 검색으로 이어진다.
고정 query template에 없는 GPUaaS/CAPEX/FCF query도 실행된다.
확장 query 결과가 WebResearchRunner 파싱 대상에 실제 포함된다.
```

### Phase 4: FeatureEngineer route fields 반영

파일:

```text
src/e2r/features.py
src/e2r/sector_profiles.py
tests/test_emerging_theme_green_gate.py
tests/test_theme_rebalance_field_validation.py
```

작업:

```text
1. AI_INFRA_PLATFORM profile 추가
2. theme route parsed_fields를 diagnostics에 반영
3. green_unlock_evidence_score 계산
4. snippet-only count와 full evidence count 분리
5. snippet-only information confidence 할인
6. source-backed route field만 score 반영
```

완료 기준:

```text
AI 인프라 전환 evidence가 EPS/FCF, visibility, bottleneck, valuation, information confidence 쪽에 반영된다.
```

### Phase 5: Stage Green gate 보강

파일:

```text
src/e2r/staging.py
tests/test_emerging_theme_green_gate.py
```

작업:

```text
1. _emerging_theme_green_allowed() 추가
2. _is_stage_3_green()에 조건 연결
3. snippet-only Green block 테스트
4. bridge evidence Green 가능 테스트
```

완료 기준:

```text
새 테마라서 무조건 Yellow로 막지 않는다.
하지만 제목/테마/가격만으로 Green을 주지도 않는다.
```

### Phase 6: production flow 연결

파일:

```text
src/e2r/pipeline/korea_live_lite.py
src/e2r/pipeline/e2r_standard_flow.py
src/e2r/audit/parser_audit.py
tests/test_korea_live_lite_theme_rebalance_guard.py
```

작업:

```text
1. config에 theme_rebalance_enabled 추가
2. candidate.reason_codes를 FreeWebResearchInput에 전달
3. DEEP_RESEARCH 후보의 per-symbol query budget 확대
4. run_log에 theme_route와 expansion diagnostics 저장
5. E2RStandardFlow에도 동일 config/pass-through 추가
6. 기존 사후 설명 LLM과 route LLM을 분리
7. live-lite independent evidence guard에서 snippet-only 제외
8. parser audit에 snippet-only 전용 code 추가
```

완료 기준:

```text
NAVER targeted smoke 실행 시:
- initial query
- LLM expansion query
- snippet evidence
- theme_route
- missing slots
- final Stage reason
이 run output에 남는다.
```

## 9. 교차검증 체크리스트

문서 작성 후 실제 로직 기준으로 다시 확인한 내용:

```text
[확인] LLM은 현재 사후 설명 위치다.
       e2r_standard_flow.py:174-196

[확인] FreeWebResearchRunner는 검색 후 바로 WebResearchRunner를 호출한다.
       free_web_research_runner.py:98-157

[확인] WebResearchRunner는 fetch 실패 시 drop한다.
       web_research_runner.py:104-110

[확인] PageFetcher live adapter는 아직 구현되어 있지 않다.
       page_fetcher.py:56-68

[확인] FeatureEngineer는 news_items.parsed_fields를 이미 읽는다.
       features.py:1021-1025

[확인] FeatureEngineer diagnostic_scores에 숫자 route 진단을 넣을 수 있다.
       features.py:241-247

[확인] ScoringPayload는 diagnostic_scores를 허용한다.
       scoring.py:41-59

[확인] StageClassifier는 ScoreSnapshot.diagnostic_scores를 읽어 Green gate를 확장할 수 있다.
       staging.py:254-280

[확인] cheap scan은 이미 초반 후보를 줄인다.
       korea_scanner.py:96-179

[확인] query budget은 후보당 확장 가능하다.
       search_budget.py:18-95

[필수보정] expansion 결과는 final QueryPlan에 들어가야 한다.
          free_web_research_runner.py:139-146
          web_research_runner.py:93-94

[필수보정] 뉴스 evidence_id가 현재 source/date 단위라 충돌 가능하다.
          evidence_builder.py:136-140
          features.py:935-952

[필수보정] SearchResult에는 company_name이 없다.
          search_provider.py:16-25
          snippet helper는 company_name/company_aliases를 별도 입력으로 받아야 한다.

[필수보정] NewsItem에는 URL 필드가 없다.
          models.py:427-440
          source_url은 parsed_fields에 넣고 Evidence.url_or_identifier로 승격해야 한다.

[필수보정] 날짜 없는 검색 결과는 as-of replay 원칙처럼 Green unlock에서 제외한다.
          asof_web_research.py:120-140

[필수보정] E2RStandardFlow와 KoreaLiveLiteConfig 둘 다 route config가 아직 없다.
          e2r_standard_flow.py:30-45
          korea_live_lite.py:64-101

[필수보정] 외부 LLM provider는 현재 구현되어 있지 않다.
          llm/provider.py:11-41
          fake provider로 route loop를 먼저 고정 테스트한다.

[필수보정] FreeWebResearchInput 호출 지점이 pipeline 외에도 있다.
          korea_scanner.py:203-213
          asof_web_research.py:162-175
          새 필드는 모두 default가 있어야 한다.

[필수보정] unknown_document_type도 snippet 보존 후보로 봐야 한다.
          web_research_runner.py:123-124

[필수보정] _ParsedFieldSource는 첫 parsed_fields 값을 우선한다.
          features.py:1050-1056
          LLM field merge 순서와 충돌 규칙이 필요하다.

[필수보정] snippet-only news도 현재 information confidence source_count를 올릴 수 있다.
          features.py:818-836

[필수보정] live-lite Green 후처리 guard는 independent evidence type을 본다.
          korea_live_lite.py:1440-1501
          snippet-only news는 독립 evidence type에서 제외해야 한다.

[필수보정] parser audit은 low confidence evidence를 warning/block 근거로 본다.
          parser_audit.py:90-103
          parser_audit.py:165-175
          snippet-only 전용 audit code가 필요하다.

[필수보정] canonical_archetype_id와 large_sector_id는 taxonomy상 일치해야 한다.
          scoring.py:207-227
          taxonomy.py:79-115
          secondary/emerging route를 canonical에 넣지 않는다.
```

## 10. 최종 구현 방향 한 줄 요약

```text
초반에는 싸게 걸러서 후보 수를 줄이고,
살아남은 후보는 LLM이 아키타입 전환/혼합을 판단해 꼬리 검색을 확장하고,
그 결과를 parsed_fields와 diagnostics로 정규화한 뒤,
최종 score와 Stage는 deterministic rule engine이 계산한다.
```

## 11. 구현 시 주의할 실제 제약

### 11.1 `diagnostic_scores`에는 숫자만 넣는다

`ScoringPayload.__post_init__()`는 `diagnostic_scores`의 value가 0~100 범위 숫자라고 가정한다. 문자열 route를 그대로 넣으면 validation 또는 이후 score path가 깨진다.

따라서 아래처럼 분리한다.

```text
parsed_fields:
- emerging_theme_id = "EMERGING_AI_INFRA_PLATFORM_DATACENTER"
- thesis_state = "transitioning"
- missing_slots = "eps_fcf_bridge,capex_fcf_burden"

diagnostic_scores:
- emerging_theme_active = 100.0
- theme_route_confidence = 72.0
- green_unlock_evidence_score = 45.0
- llm_deep_research_completed = 100.0
```

### 11.2 `FeatureEngineeringInput`의 as-of 검증을 우회하지 않는다

`FeatureEngineeringInput`은 price, actual, consensus, disclosure, report, news가 `as_of_date` 이후이면 에러를 낸다. LLM expansion query 결과도 반드시 이 검증을 통과해야 한다.

쉬운 예:

```text
as_of_date = 2026-06-08
검색 결과 published_at = 2026-06-09
-> LLM input에도 넣지 않고 snippet evidence도 만들지 않는다.
```

### 11.3 `NewsItem.symbol`은 후보 symbol과 맞춰야 한다

`FeatureEngineeringInput._validate_point_in_time()`는 `NewsItem.symbol`이 `None` 또는 후보 symbol일 때만 허용한다. snippet evidence를 만들 때 symbol을 임의로 회사명이나 URL domain으로 넣으면 깨진다.

정답:

```text
symbol = inputs.symbol
sector = inputs.sector
source = result.source
body = result.snippet
```

### 11.4 LLM route는 source URL과 query를 남긴다

LLM이 만든 parsed_fields는 반드시 어떤 search result에서 왔는지 추적 가능해야 한다.

필수 필드:

```text
source_url
source_query
source_title
source_published_at
llm_evidence_refs
```

이유:

```text
"AI 인프라 전환"이라는 말만 남으면 나중에 왜 점수가 올라갔는지 재현할 수 없다.
E2R은 as_of_date 기준 재현 가능해야 한다.
```

### 11.5 기존 연구 weight profile을 바로 덮어쓰지 않는다

`configs/e2r_archetype_weight_profile_v2_2.json`은 canonical archetype runtime weight다. 1차 패치에서 emerging theme를 여기에 바로 섞으면 기존 C26/C02/C28 회귀 테스트가 흔들릴 수 있다.

1차:

```text
emerging theme는 별도 config와 diagnostics로 운용
primary canonical은 기존 weight profile 사용
```

2차:

```text
충분한 backtest row가 쌓인 뒤 blend profile을 runtime weight로 승격
```

### 11.6 테스트는 fake LLM으로 먼저 고정한다

실제 LLM provider를 붙이기 전에 fake provider로 deterministic test를 먼저 만든다.

이유:

```text
LLM 응답은 매번 달라질 수 있다.
먼저 fake output으로 expansion loop, parsed_fields, Green gate가 정확히 작동하는지 고정해야 한다.
```

최소 fake output:

```text
thesis_state = transitioning
emerging_theme_id = EMERGING_AI_INFRA_PLATFORM_DATACENTER
suggested_queries = [...]
normalized_parsed_fields = {...}
```

### 11.7 확장 검색은 QueryPlan까지 확장해야 한다

`FreeWebResearchRunner`는 먼저 provider로 검색하고, 그 결과를 `FixtureSearchProvider(results_by_query=...)`로 감싼 뒤 `WebResearchRunner`에 넘긴다. 그런데 `WebResearchRunner`는 `QueryPlan.queries`에 들어있는 query만 다시 검색한다.

따라서 아래는 실패 패턴이다.

```text
results_by_query["NAVER AI 데이터센터 CAPEX FCF"] = (...)
하지만 final QueryPlan.queries에는 해당 query가 없음
-> WebResearchRunner가 그 결과를 읽지 않음
-> parsed_news/report/evidence/score에 반영 안 됨
```

정답:

```text
expansion query 실행
-> results_by_query 추가
-> expansion QuerySpec 생성
-> final QueryPlan.queries에 추가
-> WebResearchRunner에 final QueryPlan 전달
```

### 11.8 뉴스 evidence_id 충돌을 먼저 해결한다

현재 뉴스 evidence id는 대략 아래 형태다.

```text
news:{symbol}:{date}:{source}
```

이러면 같은 날 같은 source에서 기사 2개가 나오면 하나로 합쳐질 수 있다. snippet evidence는 짧은 기사/검색 결과가 여러 개 생기므로 충돌 가능성이 더 높다.

정답:

```text
news:{symbol}:{date}:{source}:{stable_hash(source_url || title)}
```

쉬운 예:

```text
2026-06-08 네이버뉴스 기사 A: "네이버 AI 데이터센터 확대"
2026-06-08 네이버뉴스 기사 B: "네이버클라우드 GPUaaS 매출 기대"

기존 id:
news:035420:2026-06-08:Naver News
-> 둘 중 하나가 사라질 수 있음

수정 id:
news:035420:2026-06-08:Naver News:hash_A
news:035420:2026-06-08:Naver News:hash_B
-> 둘 다 증거로 남음
```

### 11.9 회사명/별칭 없이 symbol만 보면 한국 뉴스 매칭이 약하다

`SearchResult`에는 `company_name`이 없고, 한국 주식 symbol은 숫자인 경우가 많다.

따라서 `news_item_from_search_result()`는 반드시 아래를 같이 받아야 한다.

```text
company_name
company_aliases
symbol
source_query
```

쉬운 예:

```text
symbol = 035420
기사 제목 = "네이버, 엔비디아와 AI 인프라 협력"

symbol만 보면 035420이 제목에 없어서 탈락 가능
company_aliases에 "네이버"가 있으면 정상 연결 가능
```

### 11.10 날짜 없는 snippet은 조사 확장용이지 Green unlock용이 아니다

날짜가 없는 검색 결과를 전부 버리면 너무 많은 후보가 사라질 수 있다. 반대로 날짜 없는 결과로 Green을 열면 as_of_date 원칙이 깨질 수 있다.

정답:

```text
date 없음:
- synthetic published_at = as_of_date 08:00
- date_verified = False
- search_snippet_date_unverified = True
- green_allowed_by_date = False

사용 가능:
- LLM follow-up query 생성
- Yellow/Stage2 조사 근거

사용 금지:
- 단독 Stage 3-Green unlock
```

### 11.11 route LLM과 사후 설명 LLM은 다른 역할이다

현재 `E2RStandardFlow._run_llm()`은 score/stage 이후에 호출된다. 이 위치에서는 이미 stage가 정해진 뒤라서 “부족하면 더 검색”을 할 수 없다.

정답:

```text
theme route LLM:
- FreeWebResearchRunner 내부
- score/stage 이전
- query expansion과 parsed_fields 생성

사후 설명 LLM:
- score/stage 이후
- 결정론 결과 설명
- score/stage 변경 금지
```

### 11.12 provider 없음은 기본 점수 대체가 아니라 실행 불가 진단이다

외부 LLM provider가 없는 상태에서 `theme_rebalance_enabled=True`를 켰다면, LLM이 기본형이라고 판단한 것처럼 조용히 넘어가면 안 된다.

정답:

```text
theme_route_diagnostics.theme_rebalance_status = "disabled_no_provider"
theme_route = None
기존 deterministic path는 실행
```

이건 기본형으로 대체 점수를 주는 것이 아니다. “LLM 전환 판단을 못 했다”는 상태를 명시적으로 남기고, 기존 canonical scoring만 별도로 수행한다는 뜻이다.

### 11.13 신규 모듈 export와 순환 import를 같이 본다

테스트나 외부 호출에서 package import를 쓰면 `__init__.py` export가 필요하다.

추가 대상:

```text
src/e2r/llm/__init__.py
src/e2r/research/__init__.py
src/e2r/research/free_web_research_runner.py __all__
src/e2r/research/web_research_runner.py __all__
```

순환 import 방지:

```text
theme_schemas.py가 SearchResult를 필요로 하면
e2r.research.search_provider에서 직접 import한다.
e2r.research package import는 피한다.
```

### 11.14 새 dataclass 필드는 기존 호출을 깨지 않게 default를 둔다

`FreeWebResearchInput`은 production pipeline 외에도 cheap scanner와 as-of replay에서 직접 생성된다.

정답:

```text
company_aliases = ()
candidate_reason_codes = ()
theme_rebalance_enabled = False
theme_route_provider = None
max_theme_expansion_rounds = 3
```

이렇게 둬야 기존 fixture/test/as-of replay는 코드 수정 없이 동일하게 돈다.

주의:

```text
as-of replay에서 route를 켜는 경우에도 검색 결과는 AsOfDateFilteredSearchProvider를 통과해야 한다.
미래 문서나 날짜 미검증 문서가 Green을 열면 안 된다.
```

### 11.15 Stage 3 cross-evidence buffer와 snippet-only를 분리한다

기존 scoring에는 evidence가 여러 family에 걸치면 Stage 3 쪽 buffer가 붙는 경로가 있다. snippet-only 뉴스가 evidence count를 늘리면 의도보다 Green에 가까워질 수 있다.

정답:

```text
full_news_family:
- fetch 성공 뉴스
- 날짜 검증 뉴스
- body/parsed_fields 신뢰도 충분

snippet_only_news_family:
- fetch 실패 후 title/snippet만 사용
- 날짜 미검증 가능

Green unlock:
- snippet_only_news_family만으로는 불가
```

### 11.16 구현 시작 전 필수 선행 순서

아래 순서를 바꾸면 디버깅이 어려워진다.

```text
1. evidence_id collision 수정
2. snippet NewsItem helper와 as_of/date_verified 규칙 구현
3. fake ThemeRouteProvider와 schema 구현
4. FreeWebResearchRunner expansion loop 구현
5. final QueryPlan 연결 테스트
6. FeatureEngineer diagnostics 연결
7. Stage Green gate 연결
8. KoreaLiveLite/E2RStandardFlow config 연결
```

쉬운 예:

```text
4번 expansion loop를 먼저 만들면 query는 실행된다.
하지만 1번 evidence_id와 5번 final QueryPlan이 안 되어 있으면
"검색은 했는데 점수에 반영이 안 되는" 상태가 된다.
```

## 12. 2차 라인바이라인 논리검증 결과

아래는 실제 코드 경로를 다시 보면서 추가로 발견한 구현 전 blocker다.

### 12.1 LLM-only synthetic evidence 금지

문제:

```text
LLM route 결과를 별도 synthetic NewsItem으로 만들면
LLM 판단이 원천 증거처럼 evidence_family_news/source_count에 들어간다.
```

영향:

```text
information_confidence 상승
cross_evidence_family_count 상승
Stage 3 buffer/Green gate 오염 가능
```

정답:

```text
LLM normalized field는 반드시 source_url/source_query/evidence_ref를 가져야 score 반영 가능
원천 ref 없는 LLM route field는 theme_route_diagnostics에만 저장
```

쉬운 예:

```text
LLM이 "AI 데이터센터 매출 연결 가능"이라고 말함
하지만 어떤 기사/리포트/공시 근거인지 없음
-> 점수 상승 금지, route_diagnostics에만 기록
```

### 12.2 parsed_fields merge 순서와 충돌 규칙

현재 `_ParsedFieldSource.combined_fields()`는 먼저 나온 값을 우선한다.

문제:

```text
LLM field를 앞에 넣으면 실제 공시/리포트 값을 덮을 수 있다.
LLM field를 뒤에 넣으면 기존 값 때문에 반영되지 않을 수 있다.
```

정답:

```text
1. 원천 공시/리포트/실적/컨센서스 값을 최우선
2. full article/news parsed field
3. snippet-only parsed field
4. LLM route field는 같은 source_url/evidence_ref가 있을 때만 보조
```

충돌 시:

```text
숫자 충돌: 더 보수적인 값 선택 또는 conflict diagnostic 기록
boolean 충돌: 원천 공시/리포트가 우선
LLM-only 충돌: score 반영 금지
```

### 12.3 LLM 출력 타입 정규화

현재 `_to_bool()`은 `"true"`, `"yes"`, `"1"` 같은 값만 true로 본다. `"visible"`, `"partial"`, `"확인"` 같은 문자열은 false가 될 수 있다.

정답:

```text
ThemeRouteOutput validation에서 parsed field 타입을 강제한다.
boolean field는 True/False
numeric field는 float
percent field는 40.0처럼 percent 단위로 저장
ratio field는 0.4처럼 ratio 단위로 저장
```

쉬운 예:

```text
잘못된 값:
gpu_cloud_revenue_visible = "visible"

정상 값:
gpu_cloud_revenue_visible = True
```

주의:

```text
diagnostic_scores는 0~100 숫자만 가능하다.
음수 delta, 문자열, list는 넣지 않는다.
```

### 12.4 snippet-only는 정보신뢰도도 할인한다

현재 `_information_confidence_score()`는 `inputs.news_items`가 있으면 source_count를 올린다.

문제:

```text
fetch 실패 후 제목/요약만 있는 snippet-only도 news_items에 들어가면
정보신뢰도가 full news처럼 조금 올라갈 수 있다.
```

정답:

```text
snippet-only만 있는 news_items는 information_confidence source_count에서 제외하거나 할인
diagnostic_scores.snippet_only_information_confidence_discount 기록
```

### 12.5 unknown document type도 snippet 보존 후보로 본다

현재 `WebResearchRunner`는 fetch 성공 후에도 `classify_search_result()`가 unknown이면 drop한다.

문제:

```text
Naver web/doc 결과가 AI 데이터센터 핵심 제목을 갖고 있어도
news/report/disclosure로 분류되지 않으면 unknown_document_type으로 사라질 수 있다.
```

정답:

```text
fetch failure뿐 아니라 unknown_document_type도 snippet preservation 후보로 본다.
단, search_snippet_only=True와 낮은 confidence를 반드시 남긴다.
```

### 12.6 live-lite 독립 증거 guard에서도 snippet-only 제외

`KoreaLiveLiteRunner._enforce_cross_evidence_stage3_green()`는 독립 evidence type 수를 본다.

문제:

```text
snippet-only가 source_type=news로 들어가면
독립 news evidence처럼 보일 수 있다.
```

정답:

```text
_independent_evidence_types()에서 아래는 제외:
- parsed_fields.search_snippet_only == True
- parsed_fields.search_snippet_date_unverified == True
- parsed_fields.green_allowed_by_date == False
```

### 12.7 parser audit은 snippet-only를 별도 code로 다룬다

snippet-only confidence는 0.25~0.55로 낮게 둔다.

문제:

```text
기존 audit은 confidence < 0.5면 low_parser_confidence warning을 낸다.
snippet-only가 많으면 경고가 과도하게 쌓일 수 있다.
```

정답:

```text
search_snippet_only는 low_parser_confidence와 별도 code로 분리:
- snippet_only_evidence_used
- snippet_only_green_block
- date_unverified_snippet_evidence
```

Green에는 hard block, Yellow/조사 확장에는 warning으로 본다.

### 12.8 suggested query validation

LLM은 현재 날짜나 외부 지식을 알고 있을 수 있다. 과거 as-of replay에서는 이게 미래 누수가 될 수 있다.

정답:

```text
LLM input은 as_of_date 이전 evidence만 포함
suggested query에 as_of_date 이후 연도/사건/날짜가 들어가면 실행하지 않음
검색 결과도 published_at/as_of filter를 다시 통과
```

쉬운 예:

```text
as_of_date = 2024-06-01
suggested query = "NAVER 2026 엔비디아 데이터센터 계약"
-> 실행 금지
```

### 12.9 budget/captcha stop과 expansion loop

`SearchBudgetTracker`는 `stopped_reason`이 있으면 이후 query를 막는다.

정답:

```text
initial query 중 captcha_or_block_detected 발생
-> expansion loop 시작 금지
-> theme_route_diagnostics.stop_reason = "captcha_or_block_detected"
```

그리고 expansion query도 기존 budget tracker를 공유해야 한다.

### 12.10 canonical taxonomy와 emerging theme를 섞지 않는다

`ScoringPayload`는 `canonical_archetype_id`와 `large_sector_id`가 taxonomy상 맞아야 한다.

문제:

```text
primary C26 = L8
secondary C31 = L10
emerging AI infra theme = canonical taxonomy에 없음

이 값을 canonical_archetype_id/large_sector_id에 섞으면 scoring error 또는 잘못된 weight 적용 가능
```

정답:

```text
canonical_archetype_id = primary canonical only
secondary/emerging route = parsed_fields 또는 theme_route_diagnostics only
```

### 12.11 구현 전 blocker 최종 목록

```text
1. evidence_id stable hash
2. source_url -> Evidence.url_or_identifier 승격
3. snippet helper company_alias/source_query/date_verified 처리
4. unknown_document_type snippet 보존
5. LLM schema/fake provider
6. LLM parsed field type validation
7. source-backed route field만 scoring 반영
8. expansion QuerySpec -> final QueryPlan 연결
9. snippet-only information confidence 할인
10. scoring/staging Green guard
11. live-lite independent evidence guard
12. parser audit snippet-only code 분리
13. E2RStandard/KoreaLiveLite/as-of replay config pass-through
14. package __all__ export와 import cycle 테스트
```

## 13. 3차 연결/호출부 라인바이라인 검증

이번 검증은 "필드 추가가 기존 플로우를 깨는가"와 "새 증거가 기존 gate를 우회하는가"를 중심으로 봤다.

### 13.1 새 `FreeWebResearchInput` 필드는 default 필수

확인한 직접 호출부:

```text
src/e2r/pipeline/e2r_standard_flow.py:161-169
src/e2r/pipeline/korea_live_lite.py:365-375
src/e2r/cheap_scan/korea_scanner.py:203-213
src/e2r/research/asof_web_research.py:166-175
tests/test_free_web_research_runner.py:238,268
```

판단:

```text
새 필드가 default 없으면 기존 테스트/보조 경로가 바로 깨진다.
company_aliases, candidate_reason_codes, theme_rebalance_enabled,
theme_route_provider, max_theme_expansion_rounds는 모두 default가 있어야 한다.
```

### 13.2 `WebResearchPipelineResult` 새 필드는 끝에 default로만 추가

현재 생성부:

```text
src/e2r/research/free_web_research_runner.py:184-195
```

판단:

```text
theme_route, expansion_queries_run, theme_route_diagnostics는 dataclass 끝에 default로 추가한다.
중간에 필드를 끼우거나 필수 인자로 만들면 기존 생성부/테스트가 깨진다.
```

### 13.3 snippet-only가 Stage 0/1 event score를 올리는 문제

현재 Stage 입력:

```text
src/e2r/research/free_web_research_runner.py:178-180
theme_regime_score = 80 if parsed_news or parsed_reports else 0
company_event_score = 80 if parsed_disclosures or parsed_reports or parsed_news else 0
```

문제:

```text
fetch 실패/unknown type에서 만든 search_snippet_only NewsItem도 parsed_news에 들어간다.
그러면 제목/요약만으로 company_event_score가 80이 되어 Stage 1로 올라갈 수 있다.
```

정답:

```text
snippet-only news는 theme_regime_score/company_event_score 산정에서 full news와 분리한다.
full news/report/disclosure가 있으면 기존 로직 유지.
snippet-only만 있으면:
- theme_regime_score는 낮은 조사 트리거 값 또는 0
- company_event_score는 0 또는 별도 low_confidence_event_score
```

쉬운 예:

```text
"네이버 AI 데이터센터" 검색 제목만 있음
실제 기사 fetch 실패, 공시/리포트 없음
-> Stage 1 company event처럼 취급하면 안 됨
```

### 13.4 evidence_id 변경은 free web만의 문제가 아니다

`evidence_from_news_item()`는 여러 파이프라인에서 사용된다.

확인한 영향 경로:

```text
src/e2r/research/web_research_runner.py:126-132
src/e2r/pipeline/company_research.py:151-162
src/e2r/pipeline/company_research.py:204-215
src/e2r/pipeline/daily_scan.py:96
src/e2r/pipeline/korea_live_lite.py:389-390
```

판단:

```text
뉴스 evidence_id stable hash는 전역 변경이다.
따라서 tests 일부가 exact evidence_id를 기대하면 같이 수정해야 한다.
```

정답:

```text
공통 helper를 만든다.
예: stable_news_evidence_id(symbol, published_date, source, source_url, title)
features.py와 evidence_builder.py가 같은 helper를 사용한다.
```

### 13.5 Python built-in `hash()` 사용 금지

현재 `NaverNewsConnector.to_evidence()`는 title에 `abs(hash(news.title))`를 쓴다.

문제:

```text
Python hash()는 프로세스마다 달라질 수 있다.
as_of_date 재현성과 evidence_id 안정성에 맞지 않는다.
```

정답:

```text
hashlib.sha1 또는 sha256 기반 짧은 stable hash 사용
source_url이 있으면 source_url 우선, 없으면 title 사용
```

### 13.6 red-team finding evidence_id도 같은 helper를 써야 한다

현재:

```text
NaverNewsConnector.to_evidence(): naver-news:{symbol}:{date}:{hash(title)}
NaverNewsConnector.to_red_team_finding(): naver-news:{symbol}:{date}
```

문제:

```text
red-team finding이 가리키는 evidence_id와 실제 evidence_id가 다를 수 있다.
snippet/news negative event를 추가하면 audit/briefing에서 근거 연결이 끊긴다.
```

정답:

```text
NewsItem.parsed_fields.evidence_id 또는 공통 stable_news_evidence_id helper로 일치시킨다.
```

### 13.7 logical query budget과 실제 HTTP request budget이 다르다

현재 live Naver search는 한 logical query가 여러 endpoint를 호출할 수 있다.

확인한 코드:

```text
src/e2r/research/naver_search_provider.py:73-98
src/e2r/pipeline/korea_live_lite.py:1316-1341
src/e2r/pipeline/korea_live_lite.py:377
```

문제:

```text
source_call_counts["naver_search_queries"]는 logical query 수를 더한다.
하지만 Naver news/web/doc를 모두 쓰면 실제 HTTP request는 query당 최대 3개다.
expansion loop에서 per-symbol query를 120까지 열면 실제 요청은 더 커질 수 있다.
```

정답:

```text
expansion budget은 logical query와 actual HTTP request를 모두 본다.
run_log에는 둘 다 남긴다.
live mode에서는 search_domains 수를 고려해 cap을 계산한다.
```

### 13.8 initial query가 예산을 다 쓰면 expansion이 못 돈다

현재 기본 `QueryPlanner`는 discovery/confirmation/monitoring/sector_regime query를 많이 만든다. `SearchBudget.max_queries_per_symbol` 기본값은 40이다.

문제:

```text
initial plan이 35개 가까이 실행되면 expansion query 여지가 거의 없다.
사용자가 원하는 "부족하면 꼬리 검색"이 실제로는 예산 때문에 못 돌 수 있다.
```

정답:

```text
theme_rebalance_enabled이면 expansion reserve를 둔다.
예: initial query는 20~30개까지만 실행, 나머지는 LLM expansion용으로 예약.
또는 DEEP_RESEARCH 후보만 max_queries_per_symbol을 80/120으로 늘린다.
```

### 13.9 company alias 공급 경로가 필요하다

문서상 `company_aliases`를 추가했지만 현재 `Instrument`에는 alias 필드가 없다.

문제:

```text
company_name=NAVER
기사 제목=네이버, 엔비디아와...
symbol=035420
```

이 경우 alias가 없으면 title 기준 매칭이 약하다.

정답:

```text
1차는 source_query가 company-specific이면 보조 매칭 허용
예: query="NAVER AI 데이터센터", title="네이버 AI 데이터센터"

2차는 configs/company_aliases_kr.json 같은 alias config 추가
예: NAVER -> 네이버, 네이버클라우드
```

주의:

```text
sector query 결과에서는 source_query만으로 회사 매칭을 허용하지 않는다.
반드시 company-specific query일 때만 허용한다.
```

### 13.10 route output은 JSON-safe primitive만 가진다

`KoreaLiveLite._jsonable()`은 dataclass를 재귀 직렬화한다.

확인한 코드:

```text
src/e2r/pipeline/korea_live_lite.py:1696-1718
```

문제:

```text
ThemeRouteOutput 안에 SearchResult 원본, provider 객체, exception 객체가 들어가면
run_log 직렬화나 디버깅 출력이 깨질 수 있다.
```

정답:

```text
ThemeRouteOutput은 str/int/float/bool/list/dict/date iso string 수준으로 제한한다.
SearchResult는 input에서만 쓰고 output에는 source_url/source_title/source_query만 남긴다.
```

### 13.11 E2RStandardFlow red_team_findings 중복 가능성

확인한 코드:

```text
FreeWebResearchRunner result.red_team_findings =
  web_result.red_team_findings + red_team.findings

E2RStandardFlow red_team_findings =
  result.red_team.findings + result.red_team_findings
```

문제:

```text
현재도 red_team.findings가 중복될 수 있다.
snippet/news red-team finding을 추가하면 출력 중복이 더 보일 수 있다.
```

정답:

```text
새 red_team finding을 추가할 때는 finding_id 또는 (symbol, risk_type, evidence_ids) 기준 dedupe를 같이 넣는다.
```

### 13.12 실제 진행 가능 판단

현재 문서 기준으로 구현은 가능하지만, 바로 코드를 건드리기 전 아래를 먼저 확정해야 한다.

```text
필수 선행 확정:
1. stable_news_evidence_id helper 위치
2. snippet-only가 stage input theme/company event score에 주는 영향
3. expansion reserve budget 정책
4. company alias 1차 전략(source_query 허용 범위)
5. ThemeRouteOutput JSON-safe schema
```

위 5개를 문서 원칙대로 고정하면 기존 플로우를 깨지 않고 패치에 들어갈 수 있다.
