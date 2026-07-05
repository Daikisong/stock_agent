## 결론

지금 `main`의 최신 커밋은 `53b4eda`이고, Evidence Contract·claim ledger·Green gate·운영 replay까지 상당히 많이 보강된 게 맞아. 과거 SK하이닉스 C06 fixture는 required primitive `6/6`, claim-backed ratio `100%`, orphan score `0`으로 실제 `3-Green`까지 복원됐어. 그러므로 **점수표나 Stage 판정기가 Green을 못 만드는 문제는 이제 아니야.** ([GitHub][1])

이번 삼성전자·SK하이닉스 결과의 핵심은 이거야.

> **검증이 끝나서 Yellow가 된 게 아니라, 정해진 재조사 횟수가 끝났는데 미해결 증거가 남아 있어 Yellow로 마감된 것**이야.

Yellow로 안전하게 막은 판단 자체는 맞아. 문제는 **“조사 중인 임시 Yellow”와 “찾을 만큼 찾아도 증거가 없어 확정된 Yellow”를 구분하지 않고 있다는 것**이야.

---

## 왜 이번 실행은 검증을 끝내지 않고 멈췄나

보고된 최종 결과는 완전판 실행이 아니었어.

처음에는 `top_results=None`, 문서 32개, gap expansion 2회 등으로 넓게 돌렸지만 삼성전자 첫 종목에서 8분가량 걸려 중단됐고, 최종 점수는 다음처럼 축소한 fast 실행에서 나왔어.

```text
top_results = 5
theme_route_document_limit = 8
max_theme_expansion_rounds = 1
max_score_gap_expansion_rounds = 1
post_parse_gap_expansion_max_queries = 4
page_fetch_timeout_seconds = 5
```

그래서 삼성전자 92.3035점, SK하이닉스 87.8488점이 나왔지만, 둘 다 한 번의 score-gap 재조사 후 남은 날짜·FCF·C06 primitive gap을 들고 Yellow로 종료된 거야. 넓은 실행은 완료된 것이 아니라 수동 중단됐다는 점도 중요해. 

현재 코드의 동작도 정확히 이 흐름이야.

```text
Green 총점 통과
    ↓
날짜·claim·primitive Green gate 검사
    ↓
하나라도 실패
    ↓
Yellow 총점은 통과
    ↓
"Green promotion gates remained unmet"
    ↓
3-Yellow
```

`StageClassifier`는 총점이 높아도 날짜 검증, claim-backed score, Green primitive coverage 중 하나라도 실패하면 Green을 거부하고 Yellow 기준만 만족하면 Yellow를 반환한다. 이 안전장치는 정상적이야. ([GitHub][2])

문제는 그 앞의 조사 runner야. 현재 `max_score_gap_expansion_rounds`는 기본 2회이고, 이번 fast 실행은 1회였어. 제한에 도달한 뒤 이미 검색을 한 번이라도 했다면 `round_limit_reached`를 치명적 실패가 아니라 warning으로 바꿔 점수를 유효하게 유지한다. 그러면 unresolved gap을 가진 채 Stage 판정으로 넘어가고 자연스럽게 Yellow가 돼. ([GitHub][3])

즉 지금 파이프라인에는:

```text
조사 완료
```

가 아니라,

```text
재조사 횟수 소진
```

만 있어.

둘은 전혀 다른 상태인데 현재는 둘 다 최종 Stage로 출력되고 있어.

---

# LLM으로 날짜·claim 검증을 충분히 할 수 있지 않나?

**할 수 있어. 하지만 현재 LLM은 실제로 그 역할을 맡고 있지 않아.**

지금 붙은 Codex LLM은 본질적으로 다음 역할이야.

* 섹터·아키타입 route 판단
* normalized parsed field 생성
* evidence slot present/missing 판정
* 부족한 증거에 대한 검색어 제안

출력 schema에는 다음이 없어.

```text
원문의 정확한 인용 구간
원문에서 확인한 게시 날짜
날짜를 확인한 근거
claim의 subject / predicate / period
claim과 source URL의 직접 연결
다른 문서와의 충돌 판정
독립 verifier의 통과 여부
```

현재 ThemeRoute 출력은 route, normalized fields, evidence slots, missing information, suggested queries 중심이고, 별도의 `DateVerifier`나 `ClaimVerifier` schema가 아니다. ([GitHub][4])

더 결정적인 부분도 있어. LLM route가 만든 field는 현재 내부에서 대략 이렇게 claim으로 바뀐다.

```python
quote_text = f"LLM route normalized field: {field_key}"
as_of_date = 실행 기준일
verified = True
```

실제 원문 인용문이 아니라 `"LLM route normalized field: ..."`라는 합성 문구를 quote로 넣고, 별도 재검증 없이 `verified=True`로 포장하고 있어. 일반 parser가 만든 parsed field 역시 claim compiler에서 기본적으로 `verified=True`가 된다.

그래서 현재 것은 **claim verifier가 아니라 claim 포장기**에 더 가까워. ([GitHub][5])

LLM을 더 많이 호출한다고 자동으로 해결되지는 않아. LLM이 받아야 할 원문과 날짜 metadata가 정확히 들어가고, 출력도 claim 검증용 구조여야 해.

---

# 날짜 검증에는 더 구체적인 코드 문제가 있어

현재 날짜 처리가 서로 반대 방향으로 불안정해.

## 1. 날짜가 없는 full document는 너무 쉽게 통과할 수 있다

현재 `web_research_runner.py`에서는 `SearchResult.date_verified`가 `None`이면 기본적으로 `True`, `green_allowed_by_date`가 `None`이어도 기본적으로 `True`로 처리해.

그리고 `published_at`이 없으면 실제 게시일 대신 **실행의 `as_of_date`를 게시일처럼 채운다.**

```text
실제 게시일 불명
→ as_of_date를 published_at으로 대입
→ 별도 flag가 없으면 date_verified=True
```

이건 false positive 가능성이 있어.

## 2. 반대로 날짜 없는 snippet 하나는 전체 Green을 막는다

본문 fetch가 실패해 snippet-only evidence가 되면 날짜 미검증으로 표시된다. 여기까지는 맞아.

문제는 `features.py`에서 날짜 미검증 문서 수를 계산할 때 **Green 점수에 실제 사용된 claim만 보는 게 아니라 수집된 모든 공시·리포트·뉴스를 본다는 것**이야.

그래서 다음 상황도 가능해.

```text
Green을 지지하는 핵심 공시 4개:
날짜 검증 완료

검색 결과에 따라온 무관한 기사 snippet 1개:
날짜 불명

현재 결과:
전체 date_unverified_document_count > 0
→ Green 차단
```

즉 사용하지도 않은 쓰레기 snippet 한 장이 서류철 전체에 빨간 도장을 찍어 버리는 구조야. 현재 Stage gate도 “미검증 문서가 단 하나도 없어야 한다”는 전역 조건을 쓴다. ([GitHub][6])

따라서 날짜 처리는 지금 **어떤 경우에는 지나치게 관대하고, 어떤 경우에는 지나치게 엄격해.**

---

# C06 primitive 설계에도 문제가 있다

C06의 현재 Green 필수 primitive는 다음 네 개야.

```text
customer_preorder_or_allocation
revenue_visibility_contract
hbm_capacity_constraint
hbm_capacity_pre_sold
```

전부 claim-backed 상태로 존재해야 Green이 열린다. ([GitHub][7])

그런데 실제 HBM 기업 자료는 이런 표현을 써.

```text
2025년 물량 대부분 판매 완료
HBM 매출이 DRAM 매출의 40%
고객 수요에 맞춰 생산능력 확대
12단 HBM3E 공급 확대 예상
```

경제적 의미는 충분해도 정확한 field 이름이:

```text
revenue_visibility_contract
customer_preorder_or_allocation
```

으로 매핑되지 않으면 primitive coverage가 안 올라가.

현재 LLM field와 evidence slot의 연결도 의미 기반 ontology가 아니라 **토큰의 순서가 겹치는지 보는 heuristic**이 섞여 있어. 그러니:

```text
sold out capacity
capacity pre-sold
customer allocation
volume committed
```

처럼 경제적으로 같은 표현이 서로 다른 field로 흩어질 수 있어.

C06의 `revenue_visibility_contract`도 메모리 제조업에는 이름이 조금 어색해. 실제로 필요한 것은 formal contract가 아니라:

```text
hbm_revenue_mix
hbm_shipment_visibility
customer_volume_commitment
```

중 하나일 수 있거든.

현재 Evidence Contract는 단순 배열 구조라 모든 Green primitive가 `AND`야. `A 또는 B`, `3개 중 2개`, 대체 primitive 같은 규칙을 표현하지 못해. 이 문제는 C06뿐 아니라 36개 아키타입 전반에 걸쳐 발생할 수 있어.

---

# 전체 파이프라인에서도 같은 일이 생기나?

**그럴 가능성이 높아. 다만 이번 두 종목만으로 발생률까지 확정할 수는 없어.**

특히 구조적으로 다음 범위가 영향을 받아.

* 전 아키타입: 수집 문서 전체를 보는 전역 날짜 gate
* 전 아키타입: parsed field를 실제 verifier 없이 claim으로 포장하는 경로
* Green primitive가 있는 아키타입: exact field/all-of coverage 문제
* guard primitive가 있는 아키타입: UNKNOWN guard까지 Green 차단

현재 guard 로직은 위험 claim이 실제로 발견됐을 때뿐 아니라 **그 위험이 없는지 확인하지 못한 UNKNOWN 상태도 Green을 막아.** 중요한 바이오 binary risk나 계약 취소 위험에는 맞을 수 있지만, 모든 guard에 똑같이 적용하면 “위험이 있다는 증거”가 아니라 “위험이 없다는 증명을 못 함” 때문에 계속 Yellow가 돼.

더구나 C06은 `guard_primitives`가 없는 비교적 쉬운 아키타입이야. 그런 C06에서도 live evidence closure가 끝나지 않았다면, guard가 많은 C12·C24·C30·R13 계열은 더 자주 막힐 수 있어. ([GitHub][7])

반면 현재 default 설정은 이번 fast 실행보다 넓어.

```text
top_results = 60
theme expansion = 2회
score-gap expansion = 2회
document limit = 32
post-parse query = 10
```

그래서 정식 기본 실행에서는 두 종목 모두 Green으로 복구될 가능성이 이번 fast 실행보다는 높아. 하지만 넓은 실행이 실제로 완료되지 않았으므로 현재 자료만으로 “정식 실행에서도 반드시 Yellow”라고 단정할 수는 없어.

---

# 어떻게 패치해야 하나

## 1. 날짜 gate를 문서 전체가 아니라 Green Dossier 기준으로 바꿔야 해

현재:

```text
수집된 문서 중 미검증 문서가 하나라도 있는가?
```

변경:

```text
Green 점수 및 Green primitive를 실제로 지지한 claim 중
날짜 미검증 claim이 있는가?
```

필요한 diagnostics는 이런 형태가 좋아.

```text
green_support_claim_count
green_support_claim_date_verified_count
green_support_claim_date_verified_ratio
green_support_claim_unknown_date_count
unused_unverified_document_count
```

Green 판정은:

```text
green_support_claim_date_verified_ratio == 100%
```

로 하고, 점수에 사용하지 않은 미검증 snippet은 격리만 해야 해.

---

## 2. 게시일을 `as_of_date`로 위조하는 fallback을 없애야 해

데이터 모델을 분리해야 해.

```text
published_at
observed_at
available_at
date_status
date_evidence
```

예:

```json
{
  "published_at": null,
  "observed_at": "2026-06-21T04:30:00Z",
  "date_status": "UNKNOWN",
  "date_evidence": []
}
```

날짜가 없으면 그대로 `UNKNOWN`이어야지, 실행일을 게시일로 넣으면 안 돼.

날짜 검증 순서는:

```text
검색 API pubDate
→ DART 접수일
→ HTML meta / JSON-LD datePublished
→ PDF 표지·헤더·metadata
→ URL 날짜
→ LLM 날짜 판독
→ 교차검증
```

으로 두는 게 맞아.

LLM은 애매한 날짜를 판독하는 adjudicator로 쓰고, 최종 `<= as_of_date` 비교는 코드가 해야 해.

---

## 3. 실제 ClaimVerifier를 별도 Agent로 만들어야 해

LLM이 다음 JSON을 반환하게 해야 해.

```json
{
  "evidence_id": "news:000660:...",
  "source_url": "...",
  "published_at": "2026-04-23",
  "date_status": "VERIFIED_METADATA",
  "subject": "SK하이닉스",
  "primitive_id": "hbm_capacity_pre_sold",
  "predicate": "HBM 생산능력 판매 완료",
  "value": "2026년 물량 대부분",
  "period": "2026",
  "polarity": "positive",
  "certainty": "confirmed",
  "exact_quote": "원문의 실제 문장",
  "issuer_scoped": true,
  "contradiction_status": "NONE",
  "verifier_result": "PASS"
}
```

그리고 다음 조건이 모두 맞아야 `verified=True`로 바꿔야 해.

```text
실제 source URL 존재
정확한 quote 존재
quote가 원문에 실제 포함
대상 회사가 subject
게시일 검증 완료
as_of_date 이후 정보 아님
primitive 의미와 일치
부정문·전망·루머 구분 완료
```

현재처럼 compiler가 자동으로 `verified=True`를 부여하면 안 돼.

---

## 4. `GreenClosureAgent`를 별도로 둬야 해

일반적인 score-gap search와 Green 승급 검증은 다른 작업이야.

점수가 이미 88~92인데 Green이 막혔다면, 다시 “실적 전망 뉴스”를 넓게 찾는 게 아니라 실패한 서류만 정확히 수리해야 해.

```text
score >= Green threshold
AND Green gate failed
        ↓
GreenClosureAgent 시작
        ↓
1. 기존 evidence 날짜 수리
2. 기존 claim 정확한 quote로 재검증
3. missing Green primitive만 검색
4. guard primitive 확인
5. contradiction 해결
        ↓
Green Dossier 재계산
```

종료 상태도 명확히 나눠야 해.

```text
VERIFIED_GREEN
PENDING_VERIFICATION
EXHAUSTED_YELLOW
CONTRADICTED_YELLOW
HARD_BREAK
```

현재처럼 `round_limit_reached`인데 그냥 최종 `3-Yellow`라고 쓰면 사용자는 “근거가 없어서 Yellow인지, 아직 덜 조사해서 Yellow인지” 알 수가 없어.

---

## 5. Evidence Contract v2에 논리식을 넣어야 해

C06은 예를 들면 이렇게 바꾸는 게 자연스러워.

```yaml
green_gate:
  all:
    - any:
        - customer_preorder_or_allocation
        - hbm_capacity_pre_sold

    - hbm_capacity_constraint

    - any:
        - hbm_revenue_mix_visible
        - hbm_shipment_visibility
        - revenue_visibility_contract

    - medium_term_revision_visibility
```

그리고 alias를 둬야 해.

```yaml
primitive_aliases:
  hbm_capacity_pre_sold:
    - sold_out_capacity
    - capacity_sold_out
    - volume_pre_committed
    - customer_volume_committed

  hbm_revenue_mix_visible:
    - hbm_revenue_share
    - hbm_dram_revenue_mix
    - hbm_sales_mix
```

LLM은 원문 claim을 canonical primitive에 의미적으로 매핑하고, 코드는 허용된 alias인지 검증하면 돼.

---

## 6. guard도 종류를 나눠야 해

현재는 guard가:

```text
PRESENT → Green 차단
UNKNOWN → Green 차단
ABSENT/CLEARED → 통과
```

인데, 모든 위험이 “부재를 명시적으로 입증해야 하는 위험”은 아니야.

```yaml
guards:
  qualification_failure:
    mode: must_explicitly_clear

  valuation_overheat:
    mode: block_if_present

  cost_overrun:
    mode: search_exhaustion_clearable
```

처럼 구분하는 게 맞아.

* `must_explicitly_clear`: 바이오 승인 실패, 계약 취소 같은 핵심 binary risk
* `block_if_present`: 확인되면 차단하지만 UNKNOWN은 중립
* `search_exhaustion_clearable`: 공식자료·주요뉴스를 충분히 검색한 뒤 발견되지 않으면 제한적으로 clear

---

# 패치 우선순위

가중치나 Green 점수 기준은 건드리지 말고 이 순서로 가는 게 맞아.

```text
1. 전역 날짜 gate → Green claim 전용 gate
2. published_at 합성 제거, UNKNOWN 도입
3. ClaimVerifier + exact quote/date/source schema
4. GreenClosureAgent 추가
5. Evidence Contract에 any/all/alias 도입
6. guard mode 세분화
7. 고득점 Yellow에만 동적 조사 예산 적용
```

단순히 `max_score_gap_expansion_rounds=10`으로 올리는 건 해결책이 아니야. 첫 완전판 실행이 삼성전자 하나에서 이미 너무 오래 걸렸고, 계속 일반 검색만 반복하면 비용과 지연만 늘어. 또한 Green gate를 느슨하게 푸는 것도 과거 연구에서 막아 놓은 false positive를 되살려.

전체 종목을 모두 깊게 조사하지 말고:

```text
cheap scan
→ 기본 점수
→ 85점 이상 Yellow
→ GreenClosureAgent 집중 조사
```

처럼 좁혀야 실제 운영 가능한 에이전틱 구조가 돼.

## 최종 판단

이번 Yellow의 일부는 **너무 축소한 fast 테스트 설정** 때문이야. 하지만 그 설정만의 문제는 아니야.

현재 레포는:

> **Evidence Contract와 claim ledger는 생겼지만, 실제 원문을 끝까지 검증해 Green 서류철을 완성하는 closure agent는 아직 없다.**

라고 보는 게 정확해.

그리고 가장 먼저 고칠 곳은 점수기가 아니라:

```text
web_research_runner.py       날짜 상태
evidence_claim.py            실제 verifier
evidence_builder.py          자동 verified 제거
features.py                  claim-scoped date/coverage
free_web_research_runner.py  Green closure loop
staging.py                   Green Dossier gate
evidence_contract.py         any/all/alias/guard mode
```

이야. 이걸 고치면 LLM이 단순히 “증거가 부족합니다”라고 말하고 끝나는 게 아니라, **어느 서류의 어느 칸이 비었는지 보고 직접 다시 찾고, 원문·날짜·claim까지 검증한 뒤 Green 또는 확정 Yellow로 마감하는 파이프라인**이 된다.

[1]: https://github.com/Daikisong/stock_agent/commits/main/ "Commits · Daikisong/stock_agent · GitHub"
[2]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/src/e2r/staging.py "raw.githubusercontent.com"
[3]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/src/e2r/research/free_web_research_runner.py "raw.githubusercontent.com"
[4]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/src/e2r/llm/codex_theme_provider.py "raw.githubusercontent.com"
[5]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/src/e2r/agentic/evidence_claim.py "raw.githubusercontent.com"
[6]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/src/e2r/features.py "raw.githubusercontent.com"
[7]: https://raw.githubusercontent.com/Daikisong/stock_agent/main/configs/e2r_archetype_evidence_contracts_v12.json "raw.githubusercontent.com"
