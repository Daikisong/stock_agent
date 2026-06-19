# 2026-06-11 추정치 proxy 품질 방어 구현 계획

## 목적

이 문서는 다음 패치를 바로 시작할 수 있게 만든 구현 지시서다.

해결하려는 문제는 하나다.

> 검색/리포트에서 뽑힌 약한 숫자가 구조화된 컨센서스보다 최신이라는 이유만으로 EPS, 목표가, revision 점수에 들어가면 안 된다.

쉬운 예시:

- 구조화 컨센서스: FY2026 EPS `43,833`, 목표가 `437,500`
- 검색 리포트 proxy: FY2026 EPS `5,721`, 목표가 `110,000`
- 현재 위험: proxy 날짜가 하루 더 최신이면 `_latest_consensus()`가 proxy를 대표값처럼 잡을 수 있다.
- 원하는 동작: 둘 다 evidence에는 남기되, 점수 대표값은 구조화 컨센서스를 우선한다. proxy는 충돌 진단과 보조 증거로만 쓴다.

이 규칙은 삼성전자, SK하이닉스, NAVER 같은 종목명을 조건으로 쓰지 않는다. 모든 종목/섹터/아키타입에 공통으로 적용되는 `source quality + metric conflict + point-in-time` 규칙이어야 한다.

## 현재 코드 확인

### 1. 리포트에서 consensus proxy 생성

현재 `src/e2r/research/report_consensus_proxy.py`는 parsed report 숫자를 바로 `ConsensusSnapshot`과 `ConsensusRevision`으로 바꾼다.

확인 라인:

- `src/e2r/research/report_consensus_proxy.py:26`-`55`: `build_report_consensus_proxy()`가 모든 parsed report를 순회한다.
- `src/e2r/research/report_consensus_proxy.py:58`-`84`: `_consensus_from_report()`가 `fy1_sales/op/eps`, `est_per/pbr`, `target_price`를 `source="report_proxy"`로 만든다.
- `src/e2r/research/report_consensus_proxy.py:87`-`110`: `_revision_from_report()`가 `target_revision_pct` 등을 `ConsensusRevision`으로 만든다.
- `src/e2r/research/report_consensus_proxy.py:120`-`129`: `_first_number()`는 첫 숫자만 float 변환한다. 품질/단위/충돌 검증은 없다.

문제:

- proxy 생성 전 `parser_confidence`, `raw_text`, `search_snippet_only`, `date_verified`, `source_url`을 점수 사용 자격으로 보지 않는다.
- `ConsensusRevision`에는 `source` 필드가 없어 proxy revision과 구조화 revision을 구분할 수 없다.
- 말이 안 되는 변경률이 생성되어도 score 계산 전에 막지 않는다.

실제 산출물에서 확인된 예:

- `output/live_verify_005930_2026-06-11_operational_companyguide_patch/korea_live_lite/2026-06-11_evidence.json`
- `consensus:005930:2026-06-11:2026`에 `source_name="report_proxy"`, `eps_e=5721`, `target_price=110000`
- `revision:005930:2026-06-11:2026`에 `target_price_revision_1m=1374900`

### 2. web research merge

현재 `FreeWebResearchRunner`는 proxy를 만든 뒤 base input에 바로 합친다.

확인 라인:

- `src/e2r/research/free_web_research_runner.py:235`: `build_report_consensus_proxy(...)`
- `src/e2r/research/free_web_research_runner.py:237`-`244`: proxy를 feature input에 넘긴다.
- `src/e2r/research/free_web_research_runner.py:617`-`633`: base consensus와 proxy consensus를 단순 병합한다.
- `src/e2r/research/free_web_research_runner.py:637`-`659`: proxy evidence에 `consensus_proxy_created=True`만 표시한다.
- `src/e2r/research/free_web_research_runner.py:662`-`664`: consensus dedupe key가 `(symbol, date, fiscal_year, source)`라 구조화 consensus와 proxy가 둘 다 남는다.
- `src/e2r/research/free_web_research_runner.py:667`-`669`: revision dedupe key가 `(symbol, date, fiscal_year)`라 source 구분이 없다.

문제:

- merge 시점에서 "evidence에는 남기되 score 대표값에서는 제외"하는 통로가 없다.
- revision은 source가 없어서 proxy outlier를 나중에 필터링하기 어렵다.

### 3. 리포트 파싱 경로

현재 `WebResearchRunner`는 fetch된 본문이 있으면 report로 파싱한다.

확인 라인:

- `src/e2r/research/web_research_runner.py:111`-`129`: fetch 실패 시 snippet은 news evidence로만 사용한다.
- `src/e2r/research/web_research_runner.py:172`-`183`: report로 분류되면 parsed report에 들어간다.
- `src/e2r/research/web_research_runner.py:303`-`325`: `_parse_report()`가 `title + snippet + text`를 합쳐 `extract_e2r_text_fields()`에 넣는다.

문제:

- fetch 실패 snippet은 report proxy가 되지 않는 구조라 방향은 맞다.
- 다만 fetch 성공 report에서도 title/snippet 숫자가 full text 숫자와 같은 provenance로 섞인다.
- 따라서 "본문에서 확인된 숫자"와 "검색 결과 snippet에서만 온 숫자"를 구분하는 metadata가 필요하다.

### 4. feature scoring 대표값 선택

현재 점수 엔진은 대표 consensus를 단순 최신값으로 고른다.

확인 라인:

- `src/e2r/features.py:842`-`884`: `_eps_fcf_explosion()`이 `_latest_consensus()`의 `op_e/eps_e/fcf_e`를 사용한다.
- `src/e2r/features.py:903`-`930`: `_revision_score()`가 모든 revision 값과 parsed field max를 모아 최대값을 쓴다.
- `src/e2r/features.py:945`-`987`: `_valuation_score()`가 `_latest_consensus()`의 `per_e/pbr_e`를 사용한다.
- `src/e2r/features.py:1005`-`1046`: `_actual_profit_conversion_score()`가 parsed field max를 사용한다.
- `src/e2r/features.py:1079`-`1097`: `_information_confidence_score()`는 consensus가 하나라도 있으면 source family로 인정한다.
- `src/e2r/features.py:1199`-`1203`: `_latest_consensus()`는 `(date, fiscal_year)` 정렬 후 마지막 하나를 반환한다.
- `src/e2r/features.py:1269`-`1428`: `_ParsedFieldSource`가 disclosure/report/news/agent fields를 모두 모은 뒤 `max_number()`와 `max_percent()`에서 최대값을 반환한다.

문제:

- "최신"과 "신뢰 가능"이 분리되어 있지 않다.
- 구조화 consensus가 전일이고 report proxy가 당일이면 proxy가 대표값이 될 수 있다.
- revision은 최대값을 쓰므로 말이 안 되는 숫자 하나가 revision score를 지배할 수 있다.
- news/report parsed fields도 품질 등급 없이 같은 pool에서 최대값 경쟁을 한다.

### 5. evidence tier

현재 consensus evidence는 source와 무관하게 같은 tier/confidence를 받는다.

확인 라인:

- `src/e2r/pipeline/evidence_builder.py:50`-`72`: 모든 consensus가 `SourceTier.TIER_3`, confidence `0.7`
- `src/e2r/pipeline/evidence_builder.py:75`-`98`: 모든 consensus revision도 `SourceTier.TIER_3`, source_name `"ConsensusRevision"`
- `src/e2r/pipeline/evidence_builder.py:121`-`138`: research report는 `SourceTier.TIER_1`

문제:

- `company_guide_snapshot`과 `report_proxy`가 evidence audit에서 같은 consensus tier처럼 보인다.
- revision evidence는 source_name이 고정이라 proxy revision임을 잃는다.

### 6. live pipeline 유입 경로

CompanyGuide 유입은 이미 운영 경로에 연결되어 있다.

확인 라인:

- `src/e2r/pipeline/korea_live_lite.py:430`-`439`: selected candidates에 CompanyGuide 실행
- `src/e2r/pipeline/korea_live_lite.py:440`-`455`: CompanyGuide consensus/report를 base feature input에 주입
- `src/e2r/pipeline/korea_live_lite.py:1646`-`1744`: snapshot/recent report fetch와 parse
- `src/e2r/pipeline/korea_live_lite.py:1950`-`1984`: `_base_feature_input_for_candidate()`가 extra consensus/report를 `FeatureEngineeringInput`에 넣는다.
- `src/e2r/pipeline/korea_live_lite.py:2024`-`2026`: consensus dedupe도 `(symbol, date, fiscal_year, source)` 기준

문제:

- live pipeline 연결은 되어 있다.
- 부족한 부분은 수집 연결이 아니라, 들어온 숫자 간 우선순위/충돌 처리다.

## 2차 라인바이라인 검증에서 발견한 추가 이슈

처음 문서 설계대로 바로 구현하면 아래 문제가 생긴다. 따라서 구현 계획을 이 섹션 기준으로 보정한다.

### 이슈 A. diagnostic에는 문자열을 넣을 수 없다

확인 라인:

- `src/e2r/scoring.py:80`-`85`: `ScoringPayload.diagnostic_scores` 값은 `0~100` 숫자여야 한다.
- `src/e2r/models.py:551`-`554`: `ScoreSnapshot.diagnostic_scores`도 숫자 검증을 한다.
- `src/e2r/features.py:303`-`318`: `FeatureEngineeringResult.source_fields`는 `float | str`를 담을 수 있다.

보정:

- `estimate_selected_eps_source_quality=90.0` 같은 숫자 diagnostic은 `diagnostic_scores`에 넣는다.
- `estimate_selected_eps_source="company_guide_snapshot"` 같은 문자열은 `source_fields`에 넣는다.
- run log에서 사람이 보기 쉽게 하려면 `korea_live_lite.py`의 targeted smoke row에 핵심 estimate diagnostics/source_fields 일부를 노출해야 한다.

### 이슈 B. 품질 context를 함수마다 따로 만들면 중복/불일치가 생긴다

확인 라인:

- `src/e2r/features.py:246`-`319`: `engineer()`가 전체 feature 흐름을 조립한다.
- `src/e2r/features.py:257`: `_sector_metrics()`가 먼저 호출된다.
- `src/e2r/features.py:258`: `_components()`가 그 다음 호출된다.
- `src/e2r/features.py:260`: `revision_score`를 다시 계산한다.
- `src/e2r/features.py:372`-`373`: `_components()` 내부에서 `_revision_score()`와 `_valuation_score()`를 또 호출한다.
- `src/e2r/features.py:609`-`645`: `_medium_term_revision_visibility_score()`도 `_revision_score()`를 다시 호출한다.

문제:

- 문서 초안처럼 `_eps_fcf_explosion()`, `_valuation_score()`, `_revision_score()` 안에서 각각 `select_consensus_metrics()`를 부르면 같은 conflict가 여러 번 계산될 수 있다.
- diagnostics와 실제 score 계산에 사용된 선택값이 어긋날 수 있다.

보정:

- `engineer()` 초반에서 `EstimateQualityContext`를 한 번 만든다.
- 이후 `_sector_metrics()`, `_components()`, `_medium_term_revision_visibility_score()`, `_eps_fcf_explosion()`, `_revision_score()`, `_valuation_score()`에 같은 context를 넘긴다.

예상 흐름:

```python
field_source = _ParsedFieldSource(inputs)
estimate_quality = build_estimate_quality_context(
    inputs=inputs,
    fields=field_source,
    latest_price=self._latest_price_bar(inputs.price_bars),
)
sector_metrics = self._sector_metrics(inputs, field_source, sub_scores, sector_profile, estimate_quality)
components = self._components(inputs, field_source, sub_scores, sector_metrics, estimate_quality)
revision_score = self._revision_score(inputs, field_source, estimate_quality)
```

### 이슈 C. `ConsensusSnapshot`에는 품질 metadata를 담을 곳이 없다

확인 라인:

- `src/e2r/models.py:256`-`288`: `ConsensusSnapshot`에는 `source`만 있고 `parsed_fields`/metadata가 없다.
- `src/e2r/research/report_consensus_proxy.py:75`-`82`: proxy consensus는 `source="report_proxy"`만 담는다.
- `src/e2r/pipeline/evidence_builder.py:50`-`72`: evidence builder는 `ConsensusSnapshot`의 필드만 보고 evidence를 만든다.

문제:

- 문서 초안은 `report_proxy full text`와 `weak report_proxy`를 구분한다고 했지만, 둘 다 `source="report_proxy"`이면 downstream에서 구분할 수 없다.
- report에 붙인 `consensus_proxy_score_eligible=False` metadata가 consensus row로 전달되지 않는다.

보정:

- `ConsensusSnapshot`에도 `parsed_fields: Mapping[str, Any] = field(default_factory=dict)`를 추가한다.
- `ConsensusRevision`에도 `source`와 `parsed_fields`를 추가한다.
- `report_consensus_proxy.py`에서 생성한 proxy quality metadata를 consensus/revision 객체의 `parsed_fields`에 복사한다.
- `evidence_builder.py`는 consensus/revision evidence의 `parsed_fields`에 item metadata를 merge한다.

쉬운 예시:

```python
ConsensusSnapshot(
    source="report_proxy",
    eps_e=5721,
    parsed_fields={
        "consensus_proxy_quality": "weak",
        "consensus_proxy_score_eligible": False,
        "derived_from_source_type": "research_report",
    },
)
```

이렇게 해야 evidence, feature selection, audit이 같은 품질 정보를 본다.

### 이슈 D. evidence id가 source를 포함하지 않아 evidence가 사라질 수 있다

확인 라인:

- `src/e2r/pipeline/evidence_builder.py:53`: consensus evidence id가 `consensus:{symbol}:{date}:{fiscal_year}`
- `src/e2r/pipeline/evidence_builder.py:78`: revision evidence id가 `revision:{symbol}:{date}:{fiscal_year}`
- `src/e2r/features.py:1255`-`1256`: score evidence id도 source 없이 만든다.
- `src/e2r/pipeline/korea_live_lite.py:2619`-`2623`: evidence dedupe는 `evidence_id` 기준으로 첫 항목만 남긴다.
- `src/e2r/pipeline/daily_scan.py:256`-`260`, `src/e2r/pipeline/company_research.py:415`-`419`, `src/e2r/backtest/asof_evidence_bundle.py:238`-`242`도 같은 dedupe 패턴이다.

문제:

- 같은 날짜/회계연도에 `company_guide_snapshot`과 `report_proxy`가 같이 있으면 feature input에는 둘 다 있어도 evidence output에서는 하나가 사라질 수 있다.
- "evidence는 보존한다"는 설계와 충돌한다.

보정:

- consensus/revision evidence id에 source key를 포함한다.

권장 형식:

```python
consensus:{symbol}:{date}:{fiscal_year}:{source_key}
revision:{symbol}:{date}:{fiscal_year}:{source_key}
```

- `source_key`는 공백/특수문자를 안정적으로 정규화한다.
- `features._evidence_ids()`와 `evidence_builder.py`가 같은 helper를 써야 한다.
- 기존 테스트는 구형 id를 기대하므로 수정한다.
- 하위 호환 감사용으로 evidence `parsed_fields["legacy_evidence_id"]`에 기존 id를 넣는 것은 가능하다.

### 이슈 E. report parser와 financial text parser의 목표가 변경률 로직이 다르다

확인 라인:

- `src/e2r/research/report_parser.py:578`-`593`: 목표가 변경률 계산 시 `만원/원` 단위를 `_scale_price()`로 보정한다.
- `src/e2r/research/financial_text_fields.py:200`-`216`: 비슷한 목표가 변경률 계산이 있지만 단위 보정이 없다.
- `src/e2r/research/web_research_runner.py:321`-`322`: `_parse_report()`에서 `extract_e2r_text_fields(parse_context)` 결과가 기존 parsed report fields를 `update()`로 덮어쓴다.

문제:

- `8만원 -> 110000원` 같은 텍스트가 있으면 단위 보정 없는 parser는 `(110000 / 8 - 1) * 100 = 1,374,900%` 같은 값을 만들 수 있다.
- report parser가 안전하게 계산한 값을 `extract_e2r_text_fields()` 결과가 덮어쓸 수도 있다.

보정:

- 목표가 변경률 parser를 한 곳으로 통합하거나 `financial_text_fields.py`에도 unit scaling을 넣는다.
- `web_research_runner._parse_report()` merge는 숫자 민감 필드에 대해 `update()`가 아니라 `setdefault()` 또는 allowlist merge를 쓴다.
- 특히 아래 필드는 덮어쓰기 금지 우선 대상이다.

```python
target_revision_pct
target_price_revision_pct
target_price
fy1_eps
fy1_op
fy1_sales
est_per
est_pbr
```

### 이슈 F. report proxy가 독립 consensus family를 과대계산할 수 있다

확인 라인:

- `src/e2r/features.py:1079`-`1097`: consensus가 하나라도 있으면 information confidence source family로 센다.
- `src/e2r/features.py:1113`-`1127`: `evidence_family_consensus`도 `bool(inputs.consensus)`만 본다.
- `src/e2r/staging.py:350`-`359`: Stage 2 bridge가 evidence family count를 사용한다.
- `src/e2r/scoring.py:272`-`286`: scoring calibration bonus도 evidence family count를 사용한다.
- `src/e2r/pipeline/korea_live_lite.py:2421`-`2424`: pipeline cross evidence에서는 `derived_from_source_type="research_report"`이면 research_report로 되돌린다.

문제:

- 리포트 하나에서 파생된 proxy consensus가 `research_report`와 `consensus` 두 독립 가족처럼 세어질 수 있다.
- 그러면 cross evidence family count가 실제보다 높아져 Stage gate에 영향을 줄 수 있다.

보정:

- `evidence_family_consensus`는 구조화/독립 consensus만 센다.
- `report_proxy`는 evidence에는 consensus source_type으로 남길 수 있지만, `derived_from_source_type="research_report"`이면 독립 consensus family로 세지 않는다.
- 별도 diagnostic은 남긴다.

```python
evidence_family_consensus_proxy = 1.0
evidence_family_consensus_structured = 1.0
```

- `information_confidence_score`의 analyst bonus도 score-eligible structured consensus의 analyst_count만 사용한다.

### 이슈 G. CompanyGuide recent report 숫자는 consensus selector 후보로 직접 들어오지 않는다

확인 라인:

- `src/e2r/sources/company_guide.py:192`-`224`: recent report payload는 `ResearchReport(target_price, fy1_eps, raw_text=comment)`로 들어온다.
- `src/e2r/pipeline/korea_live_lite.py:453`-`455`: CompanyGuide consensus와 reports를 base feature input에 넣는다.
- `src/e2r/research/free_web_research_runner.py:235`: `build_report_consensus_proxy()`는 `web_result.parsed_reports`에만 적용된다.
- `src/e2r/features.py:1333`-`1379`: `_ParsedFieldSource`가 report fields를 일부 복사하지만 `target_price`는 복사하지 않는다.

문제:

- 문서 초안의 `structured broker metadata` 등급을 만들어도, CompanyGuide recent report의 `target_price/fy1_eps`가 consensus selector 후보로 안 들어올 수 있다.
- 반대로 무조건 consensus proxy로 승격하면 report 하나가 consensus family를 과대계산할 수 있다.

보정:

- `EstimateQualityContext`는 `inputs.consensus`뿐 아니라 `inputs.research_reports`도 후보로 읽는다.
- `ResearchReport.parsed_fields["source"] == "company_guide_recent_report"`이면 `structured_broker_metadata` quality로 metric 후보를 만들 수 있다.
- 단 이 후보는 `derived_from_source_type="research_report"`로 표시하고 독립 consensus family로 세지 않는다.
- `_ParsedFieldSource`에는 report attribute 중 `target_price`도 복사 후보에 추가하되, score numeric filter를 통과한 경우에만 사용한다.

### 이슈 H. revision source를 추가해도 dedupe key가 그대로면 revision이 사라질 수 있다

확인 라인:

- `src/e2r/research/free_web_research_runner.py:667`-`669`: `_dedupe_revisions()` key가 `(symbol, date, fiscal_year)`이다.
- `src/e2r/research/free_web_research_runner.py:627`-`629`: base revisions와 proxy revisions를 합친 뒤 이 dedupe를 탄다.

문제:

- structured revision과 report proxy revision이 같은 날짜/회계연도이면 source가 달라도 하나로 덮인다.
- `ConsensusRevision.source`를 추가해도 merge 단계에서 잃으면 downstream에서 구분할 수 없다.

보정:

- `_dedupe_revisions()` key를 `(symbol, date, fiscal_year, source)`로 바꾼다.
- sort key도 `(date, fiscal_year, source)`로 바꾼다.
- source가 없는 기존 revision은 모델 기본값 `unknown`을 사용한다.

### 이슈 I. source-aware evidence id는 이미 있는 helper 파일에 추가해야 한다

확인 라인:

- `src/e2r/evidence_ids.py:1`-`33`: `stable_text_hash()`와 `stable_news_evidence_id()`가 이미 있다.
- `src/e2r/features.py:11`, `92`-`100`: feature evidence id가 이 helper를 import해서 news id를 만든다.
- `src/e2r/pipeline/evidence_builder.py:19`, `50`-`98`: evidence builder도 같은 helper를 import하지만 consensus/revision id는 아직 직접 문자열로 만든다.

문제:

- 문서 초안처럼 "helper 추가"라고만 쓰면 새 파일을 만들 가능성이 있다.
- 그러면 `features._evidence_ids()`와 `pipeline.evidence_builder`가 서로 다른 id 규칙을 가질 수 있다.
- 예: score에는 `consensus:005930:2026-06-11:2026:company_guide_snapshot`가 들어가는데 evidence bundle에는 `consensus:005930:2026-06-11:2026`만 있으면, 나중에 stage/evidence 링크가 안 맞는다.

보정:

- consensus/revision id helper는 새 파일이 아니라 기존 `src/e2r/evidence_ids.py`에 추가한다.
- 함수 예시는 다음처럼 둔다.

```python
def stable_estimate_source_key(source: str | None) -> str: ...
def stable_consensus_evidence_id(*, symbol: str, estimate_date: date, fiscal_year: int, source: str | None) -> str: ...
def stable_revision_evidence_id(*, symbol: str, estimate_date: date, fiscal_year: int, source: str | None) -> str: ...
```

- `stable_estimate_source_key()`는 공백을 `_`로 바꾸고, 너무 길거나 비 ASCII/특수문자가 많으면 `stable_text_hash()` suffix를 붙여 id가 깨지지 않게 한다.
- `features._evidence_ids()`와 `pipeline.evidence_builder`는 반드시 이 공통 helper만 사용한다.
- 기존 id는 evidence `parsed_fields["legacy_evidence_id"]`로만 남긴다.

### 이슈 J. 파일/CSV/historical loader도 metadata를 통과시켜야 한다

확인 라인:

- `src/e2r/sources/source_errors.py:223`-`229`: 다른 source connector들은 `parsed_fields_from_record()`로 unknown column을 metadata에 보존한다.
- `src/e2r/connectors.py:147`-`153`: generic connector에도 `_parsed_fields_with_unknowns()`가 이미 있다.
- `src/e2r/sources/consensus.py:57`-`96`: `ConsensusCSVConnector`는 현재 consensus/revision row의 `parsed_fields`와 unknown column을 버린다.
- `src/e2r/connectors.py:505`-`545`: `CSVJSONDataConnector`도 consensus/revision row metadata를 버린다.
- `src/e2r/historical_cases/__init__.py:314`-`350`: historical case consensus/revision loader도 metadata를 버린다.

문제:

- live report proxy에는 `consensus_proxy_quality`가 붙어도, CSV/fixture/backtest 데이터에서는 같은 필드가 사라질 수 있다.
- 그러면 단위 테스트는 통과해도 실제 backtest 재현에서는 source quality selector가 `unknown`으로 떨어진다.

보정:

- `ConsensusSnapshot`/`ConsensusRevision` 모델에 `parsed_fields`를 추가한 뒤, 아래 normalizer도 함께 수정한다.
- `src/e2r/sources/consensus.py`는 `parsed_fields_from_record()`를 import해서 consensus/revision known key를 제외한 나머지를 metadata로 보존한다.
- `src/e2r/connectors.py`는 기존 `_parsed_fields_with_unknowns()`를 consensus/revision에도 사용한다.
- `src/e2r/historical_cases/__init__.py`는 이미 import한 `parsed_fields_from_record()`를 consensus/revision에도 적용한다.
- revision은 `source=str(row.get("source") or "...")`도 넣는다.

예:

```python
ConsensusRevision(
    ...,
    source=str(row.get("source") or "consensus-csv"),
    parsed_fields=parsed_fields_from_record(row, known),
)
```

### 이슈 K. 기존 테스트의 old evidence id 기대값은 의도적으로 깨진다

확인 라인:

- `tests/test_free_web_research_runner.py:301`, `353`, `778`: 기존 `consensus:{symbol}:{date}:{fiscal_year}`를 직접 기대한다.
- `tests/test_free_web_research_runner.py:304`, `356`: report proxy만 있는 케이스도 `evidence_family_consensus == 1.0`을 기대한다.

문제:

- 패치 후 source-aware id가 정상 적용되면 기존 id assert는 실패해야 맞다.
- report proxy를 독립 consensus family로 세지 않게 바꾸면 기존 `evidence_family_consensus == 1.0` assert도 실패해야 맞다.

보정:

- 테스트 기대값을 새 의미에 맞춘다.
- evidence id는 `stable_consensus_evidence_id(...)` helper로 기대값을 만들고, `legacy_evidence_id`도 확인한다.
- report proxy만 있는 케이스는 다음을 확인한다.

```python
self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus"], 0.0)
self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus_proxy"], 1.0)
```

- structured consensus가 있는 케이스는 `evidence_family_consensus == 1.0`을 유지한다.

### 이슈 L. historical case evidence id는 기존부터 별도 prefix를 쓴다

확인 라인:

- `src/e2r/historical_cases/__init__.py:90`-`103`: historical case도 `FeatureEngineeringInput`을 만들어 feature engineer를 탄다.
- `src/e2r/historical_cases/__init__.py:507`: historical consensus evidence id는 `historical-consensus:{symbol}:{date}:{fiscal_year}`이다.
- `src/e2r/historical_cases/__init__.py:526`: historical revision evidence id는 `historical-revision:{symbol}:{date}:{fiscal_year}`이다.
- `src/e2r/historical_cases/__init__.py:168`-`175`: Stage 분류에는 score evidence ids와 historical evidence ids가 함께 들어간다.

판단:

- 이번 패치의 필수 범위는 historical consensus/revision의 source/metadata 전달이다.
- historical evidence id prefix까지 `consensus:*`로 통합하면 과거 리포트/감사 출력이 바뀌는 별도 구조변경이 된다.
- StageClassifier는 evidence id matching을 강제하지 않고 ids를 합쳐 보존하므로 즉시 깨지는 호출 문제는 아니다.

보정:

- 이번 패치에서는 historical loader metadata 전달만 필수로 한다.
- historical evidence id 통합은 별도 개선 항목으로 남긴다.
- 단 새 테스트에서는 historical metadata가 `FeatureEngineeringInput`과 score quality selector까지 전달되는지만 본다.

### 이슈 M. dataclass JSON 출력은 additive schema 변경이 된다

확인 라인:

- `src/e2r/pipeline/korea_live_lite.py:2636`-`2657`: `_jsonable()`은 dataclass `fields()`를 전부 JSON으로 쓴다.
- `src/e2r/backtest/*`, `src/e2r/research/*_snapshot_store.py`에도 같은 방식의 `_jsonable()`이 있다.

판단:

- `ConsensusSnapshot.parsed_fields`, `ConsensusRevision.source`, `ConsensusRevision.parsed_fields`를 추가하면 JSON 로그/백테스트 출력에 새 key가 추가된다.
- 기본값은 `{}` 또는 `"unknown"`이라 기존 로직을 깨지는 않지만, exact JSON schema를 기대하는 외부 소비자는 새 key를 보게 된다.

보정:

- 이 변경은 의도적인 additive schema 변경으로 문서화한다.
- repo 내부 테스트에서는 exact JSON 전체 비교보다 필요한 key 위주로 검증한다.
- output schema 문서를 따로 관리한다면 패치 후 새 필드를 반영한다.

## 구현 원칙

1. 종목명 하드코딩 금지

금지:

```python
if symbol in {"005930", "000660"}:
    prefer_company_guide = True
```

허용:

```python
if consensus.source == "company_guide_snapshot":
    source_quality = STRUCTURED_CONSENSUS
```

2. LLM 역할과 deterministic 역할 분리

- LLM: 부족한 슬롯을 찾아 추가 검색하고, 텍스트에서 후보 숫자와 문맥을 뽑는다.
- deterministic engine: 어떤 숫자가 점수 대표값으로 쓸 수 있는지 결정한다.

쉬운 예시:

- LLM이 "목표가 11만원, EPS 5,721원"을 찾아온다.
- deterministic layer가 "구조화 컨센서스와 70% 이상 충돌하고 source가 report_proxy이므로 대표값에서는 제외"라고 결정한다.

3. evidence 보존, scoring 사용 제한

숫자를 완전히 버리면 나중에 감사가 안 된다. 따라서:

- evidence에는 남긴다.
- score 대표값 후보에서는 제외하거나 낮은 우선순위로 둔다.
- diagnostic에 `estimate_proxy_quarantined_count_capped`, `estimate_conflict_count_capped`를 남긴다.

4. point-in-time 유지

기존 `as_of_date` 검증은 유지한다.

쉬운 예시:

- `as_of_date=2026-06-11`이면 2026-06-12 리포트 숫자는 후보에도 들어가면 안 된다.
- 이 검증은 `ConsensusSnapshot.__post_init__`, `ConsensusRevision.__post_init__`, `ResearchReport.__post_init__`에 이미 일부 있다.

## 권장 패치 구조

### 새 모듈

새 파일을 추가한다.

`src/e2r/estimate_quality.py`

역할:

- source를 품질 등급으로 분류
- consensus/revision/parsed field 후보를 metric 단위로 점수 사용 가능 여부 판단
- 충돌/격차 진단값 생성

예상 API:

```python
@dataclass(frozen=True)
class EstimateMetricCandidate:
    metric: str
    value: float
    source: str
    source_quality: int
    date: date
    fiscal_year: int | None = None
    evidence_id: str | None = None
    parser_confidence: float | None = None
    weak_reason: str | None = None

@dataclass(frozen=True)
class EstimateMetricSelection:
    metric: str
    selected_value: float | None
    selected_source: str | None
    selected_quality: int | None
    quarantined_count: int = 0
    conflict_count: int = 0
    weak_reasons: tuple[str, ...] = ()

@dataclass(frozen=True)
class EstimateQualityContext:
    selections: Mapping[str, EstimateMetricSelection]
    revision_selection: EstimateMetricSelection
    diagnostic_scores: Mapping[str, float]
    source_fields: Mapping[str, float | str]

def consensus_source_quality(source: str) -> int: ...
def select_best_consensus_metric(candidates: Sequence[EstimateMetricCandidate]) -> EstimateMetricSelection: ...
def estimate_quality_diagnostics(selections: Sequence[EstimateMetricSelection]) -> dict[str, float]: ...
```

품질 점수는 숫자가 클수록 강하다.

| quality | source class | 예 |
|---:|---|---|
| 100 | official actual/disclosure | OpenDART/data.go actual, exchange disclosure |
| 90 | structured consensus | `company_guide_snapshot`, CSV/JSON structured consensus |
| 75 | structured broker metadata | `company_guide_recent_report` |
| 60 | full-text report proxy | fetch 성공, 본문 존재, parser confidence 충분 |
| 35 | weak report proxy | provenance 불명확, 본문 짧음, snippet/title 숫자 의존 |
| 10 | snippet/news hint | fetch 실패 snippet, 날짜 미검증 |

중요:

- `snippet/news hint`는 consensus/revision 대표값 후보가 아니다.
- `weak report proxy`는 구조화 consensus가 없을 때만 제한적으로 보조 사용한다.
- 구조화 consensus가 있으면 낮은 품질 proxy가 최신이어도 대표값을 빼앗지 못한다.

### 모델 변경

`src/e2r/models.py`

1. `ConsensusSnapshot`에 `parsed_fields`를 추가한다.

2차 검증에서 확인한 이유:

- proxy quality를 report에만 붙이면 consensus row에서 사라진다.
- evidence builder와 feature selector가 같은 quality metadata를 봐야 한다.

권장 변경:

```python
class ConsensusSnapshot:
    ...
    target_multiple: float | None = None
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)
```

`__post_init__`에서:

```python
object.__setattr__(self, "parsed_fields", _copy_mapping(self.parsed_fields))
```

2. `ConsensusRevision`에 `source: str = "unknown"`과 `parsed_fields`를 추가한다.

현재 `ConsensusSnapshot`에는 `source`가 있지만 `ConsensusRevision`에는 없다. 이 때문에 report proxy revision과 다른 revision을 구분할 수 없다.

변경 위치:

- 현재 `ConsensusRevision`은 `src/e2r/models.py:291`-`317`

권장 변경:

```python
class ConsensusRevision:
    symbol: str
    date: date
    fiscal_year: int
    as_of_date: date
    ...
    street_low_eps_revision_1m: float | None = None
    source: str = "unknown"
    parsed_fields: Mapping[str, Any] = field(default_factory=dict)
```

주의:

- 내부 검색 결과 현재 repo의 `ConsensusRevision(...)` 호출은 전부 키워드 기반이다.
- 그래도 외부/오래된 코드가 positional 5번째 인자로 `eps_revision_1w`를 넘겼을 가능성을 줄이기 위해 `source`는 기존 optional numeric field 뒤에 추가한다.
- 쉬운 예: 예전 코드가 `ConsensusRevision("005930", d, 2026, as_of, 30)`처럼 썼다면, `source`를 `as_of_date` 바로 뒤에 끼우는 순간 `30`이 revision 값이 아니라 source로 해석될 수 있다.
- 기존 테스트/fixture가 source를 안 넣어도 `unknown`으로 동작해야 한다.
- `__post_init__`에 `_require_text(self.source, "source")` 추가한다.
- `parsed_fields`는 `_copy_mapping()`으로 복사한다.

3. 모델 변경 후 import 확인

`models.py`는 이미 `field`, `Any`, `Mapping`을 import하고 있어서 새 import는 필요 없다.

### report proxy 생성 가드

수정 파일:

- `src/e2r/research/report_consensus_proxy.py`

변경 위치:

- `build_report_consensus_proxy()` 주변 `26`-`55`
- `_consensus_from_report()` 주변 `58`-`84`
- `_revision_from_report()` 주변 `87`-`110`

추가 함수:

```python
def _report_proxy_quality(report: ResearchReport) -> tuple[str, tuple[str, ...]]:
    ...
```

결정 규칙:

1. `report.publish_date > as_of_date`이면 proxy 생성 금지

이건 모델에서도 막히지만 함수 단계에서도 명시한다.

2. `report.parsed_fields["search_snippet_only"] is True`이면 consensus/revision proxy 생성 금지

fetch 실패 snippet은 news evidence로는 남아도 된다. 숫자 proxy는 안 된다.

3. `parser_confidence < 0.55`이면 proxy 생성 금지

단, 구조화 source가 `company_guide_recent_report`이고 명시 metadata에서 나온 값이면 report evidence로는 남긴다. consensus proxy로는 만들지 않는다.

4. `raw_text`가 없거나 너무 짧으면 `weak_report_proxy`

1차 기준:

- `raw_text`가 없으면 weak
- `raw_text.strip()` 길이 `< 80`이면 weak
- 숫자가 title/snippet에서만 온 것으로 보이면 weak

5. weak proxy는 생성은 하되 `parsed_fields`에 다음 metadata를 붙인다.

```python
{
    "consensus_proxy_quality": "weak",
    "consensus_proxy_weak_reasons": (...),
    "consensus_proxy_score_eligible": False,
}
```

이 metadata는 `ResearchReport.parsed_fields`뿐 아니라 생성되는 `ConsensusSnapshot.parsed_fields`와 `ConsensusRevision.parsed_fields`에도 들어가야 한다.

6. full-text proxy는 다음 metadata를 붙인다.

```python
{
    "consensus_proxy_quality": "full_text_report",
    "consensus_proxy_score_eligible": True,
}
```

주의:

- 이 함수에서 proxy를 완전히 막는 경우는 `future date`, `snippet only`, `very low confidence` 정도로 제한한다.
- 그 외에는 evidence 보존을 위해 만들되 score layer에서 선택 제한한다.

### revision source 추가

수정 파일:

- `src/e2r/research/report_consensus_proxy.py`
- `src/e2r/pipeline/evidence_builder.py`
- 테스트 fixture 전반

변경:

```python
return ConsensusRevision(
    symbol=report.symbol,
    date=report.publish_date,
    fiscal_year=_fiscal_year(report),
    as_of_date=as_of_date,
    source="report_proxy",
    parsed_fields={
        "consensus_proxy_created": True,
        "consensus_proxy_source": "research_report",
        "derived_from_source_type": "research_report",
        "consensus_proxy_quality": proxy_quality,
        "consensus_proxy_score_eligible": score_eligible,
    },
    **values,
)
```

그리고 structured connector가 revision을 만드는 곳은 가능한 source를 넣는다.

현재 `ConsensusRevision(` 생성 위치는 아래 6곳이다. 패치 시 전부 확인한다.

- `src/e2r/research/report_consensus_proxy.py:104`: report proxy revision. 반드시 `source="report_proxy"`를 넣는다.
- `src/e2r/sources/consensus.py:80`-`96`: CSV/JSON consensus source normalizer. row의 `source`가 있으면 쓰고 없으면 `consensus-csv` 계열 기본값을 넣는다.
- `src/e2r/connectors.py:528`-`540`: generic file connector. row의 `source`가 있으면 쓰고 없으면 `file` 계열 기본값을 넣는다.
- `src/e2r/historical_cases/__init__.py:337`-`350`: historical case loader. row의 `source`가 있으면 쓰고 없으면 `historical_case`를 넣는다.
- `tests/test_features.py:73`-`83`: feature test fixture. 기본값으로 통과하지만 source-aware 테스트를 추가한다.
- `tests/test_sector_profiles.py:69`-`78`: sector profile test fixture. 기본값으로 통과하지만 필요하면 `source="test"`를 명시한다.

기존 생성자가 깨지지 않도록 `source="unknown"` 기본값을 둔다.

### feature scoring 대표값 선택 변경

수정 파일:

- `src/e2r/features.py`

1. `EstimateQualityContext`를 `engineer()`에서 한 번 만든다.

변경 위치:

- `src/e2r/features.py:246`-`319`

권장 흐름:

```python
field_source = _ParsedFieldSource(inputs)
estimate_quality = build_estimate_quality_context(
    inputs=inputs,
    fields=field_source,
    latest_price=self._latest_price_bar(inputs.price_bars),
)
```

그 다음 아래 내부 함수 시그니처를 함께 바꾼다.

```python
_sector_metrics(..., estimate_quality)
_components(..., estimate_quality)
_medium_term_revision_visibility_score(..., estimate_quality)
_eps_fcf_explosion(..., estimate_quality)
_revision_score(..., estimate_quality)
_valuation_score(..., estimate_quality)
_information_confidence_score(..., estimate_quality)
_evidence_family_diagnostics(..., estimate_quality)
```

이렇게 해야 score 계산과 diagnostics가 같은 선택값을 공유한다.

2. `_latest_consensus()` 직접 사용 축소

현재 사용:

- `src/e2r/features.py:844`
- `src/e2r/features.py:946`

변경:

```python
selected = select_consensus_metrics(inputs.consensus)
op_e = selected.get("op_e").selected_value
eps_e = selected.get("eps_e").selected_value
fcf_e = selected.get("fcf_e").selected_value
per_e = selected.get("per_e").selected_value
pbr_e = selected.get("pbr_e").selected_value
```

3. metric별 선택

한 consensus row 전체를 대표로 고르지 말고 metric별로 고른다.

쉬운 예시:

- 구조화 consensus에 EPS만 있고 OP가 없다.
- full-text report proxy에 OP가 있다.
- 결과: EPS는 구조화 consensus, OP는 full-text proxy를 쓴다.

이게 중요하다. 구조화 source가 하나라도 있다고 proxy를 전부 버리면 좋은 보조 숫자도 못 쓴다.

4. 최신성은 source 품질 안에서만 tie-breaker

정렬 우선순위:

1. `score_eligible`
2. `source_quality`
3. `metric completeness`
4. `date`
5. `analyst_count`

즉 낮은 품질 최신 proxy가 높은 품질 전일 structured consensus를 이기면 안 된다.

5. conflict quarantine

같은 symbol/fiscal_year/metric에서 고품질 후보와 저품질 후보가 크게 다르면 저품질 후보는 대표값 후보에서 제외한다.

1차 기준:

| metric | conflict 기준 |
|---|---:|
| `eps_e`, `op_e`, `sales_e`, `fcf_e` | 상대 차이 50% 초과 |
| `target_price` | 상대 차이 50% 초과 또는 최근가 대비 5배 초과 |
| `per_e`, `pbr_e` | 상대 차이 60% 초과 |
| revision pct | 절대값 300% 초과는 score 제외 |

주의:

- negative EPS/OP turnaround는 단순 상대 차이가 깨질 수 있다. 둘 중 하나가 0 이하이면 conflict 판단은 절대값 비교 대신 "둘 다 score 대표값으로 쓰지 않고 diagnostic만 남김"이 안전하다.

6. diagnostic/source_fields 추가

`FeatureEngineeringResult` 생성 시 `diagnostic_scores`에 추가한다.

예상 키:

```python
"estimate_selected_eps_source_quality": 90.0
"estimate_selected_target_price_source_quality": 90.0
"estimate_conflict_count_capped": 1.0
"estimate_proxy_quarantined_count_capped": 1.0
"estimate_revision_outlier_count_capped": 1.0
"estimate_low_quality_proxy_present": 1.0
```

문자열 source 이름은 `diagnostic_scores`가 아니라 `source_fields`에 넣는다.

예상 `source_fields`:

```python
"estimate_selected_eps_source": "company_guide_snapshot"
"estimate_selected_target_price_source": "company_guide_snapshot"
"estimate_selected_revision_source": "report_proxy"
```

7. `_ParsedFieldSource`에도 weak numeric filter 추가

현재 `src/e2r/features.py:1396`-`1408`의 `values/max_number/max_percent`는 source 품질을 모른다.

추가 API:

```python
def values_for_scoring(self, *keys: str) -> tuple[Any, ...]:
    ...

def max_percent_for_scoring(self, *keys: str) -> float | None:
    ...
```

filter 규칙:

- `search_snippet_only=True`인 mapping의 숫자는 score 대표값 max에서 제외
- `green_allowed_by_date=False`인 mapping의 숫자는 score 대표값 max에서 제외
- `consensus_proxy_score_eligible=False`인 mapping의 EPS/target/revision 숫자는 제외
- boolean theme hint는 기존처럼 남길 수 있다. 숫자만 제한한다.

적용 위치:

- `_revision_score()`에서 revision pct 관련 parsed fields
- `_valuation_score()`에서 `est_per`, `pbr_e`, target multiple 관련 fields
- `_actual_profit_conversion_score()`에서 news에서 뽑힌 actual numeric fields
- 단, 공식 `FinancialActual`에서 만든 actual_fields는 항상 score eligible

8. evidence family와 information confidence를 source-aware로 바꾼다.

수정 위치:

- `src/e2r/features.py:1079`-`1097`
- `src/e2r/features.py:1113`-`1127`

규칙:

- structured consensus만 `evidence_family_consensus=1`에 포함한다.
- report-derived proxy는 `evidence_family_consensus_proxy=1`로 따로 표시하되 독립 consensus family로 세지 않는다.
- `cross_evidence_family_count`는 report proxy consensus를 research_report family와 중복 계산하지 않는다.
- analyst bonus는 score-eligible structured consensus의 `analyst_count`만 사용한다.

### evidence tier/source 변경

수정 파일:

- `src/e2r/pipeline/evidence_builder.py`
- `src/e2r/features.py`

변경 위치:

- `evidence_from_consensus()` `50`-`72`
- `evidence_from_consensus_revision()` `75`-`98`
- `_evidence_ids()` `src/e2r/features.py:1252`-`1266`

추가 함수:

```python
def _consensus_evidence_tier(source: str) -> tuple[SourceTier, float]:
    ...
```

추가 helper:

```python
def consensus_evidence_id(item: ConsensusSnapshot) -> str: ...
def consensus_revision_evidence_id(item: ConsensusRevision) -> str: ...
def source_key(source: str) -> str: ...
```

`evidence_builder.py`와 `features.py`가 같은 helper를 써야 evidence id가 어긋나지 않는다.

권장 매핑:

| source | tier | confidence |
|---|---:|---:|
| `company_guide_snapshot` | `TIER_2` | `0.85` |
| structured CSV/connector consensus | `TIER_2` | `0.80` |
| `report_proxy` full text | `TIER_3` | `0.65` |
| weak `report_proxy` | `TIER_4` | `0.45` |
| unknown | `TIER_3` | `0.60` |

`ConsensusRevision`에는 `source`를 추가한 뒤:

```python
source_name=item.source
source_tier=...
```

evidence id는 source-aware 형식으로 바꾼다.

```python
consensus:{symbol}:{date}:{fiscal_year}:{source_key}
revision:{symbol}:{date}:{fiscal_year}:{source_key}
```

기존 id는 `parsed_fields["legacy_evidence_id"]`에 넣어 감사 추적을 돕는다.

`parsed_fields`는 기존 numeric fields와 item metadata를 merge한다.

```python
parsed_fields={
    **item.parsed_fields,
    "sales_e": item.sales_e,
    "op_e": item.op_e,
    "eps_e": item.eps_e,
    "fcf_e": item.fcf_e,
    "target_price": item.target_price,
}
```

객체의 정규화 numeric 값이 마지막에 와야 한다. metadata 안에 같은 key가 있어도 core value를 덮으면 안 된다.

주의:

- tier는 evidence 감사/리포팅용이다.
- stage는 여전히 deterministic score와 gate가 결정한다.

### report parser merge 순서와 목표가 변경률 보강

수정 파일:

- `src/e2r/research/web_research_runner.py`
- `src/e2r/research/financial_text_fields.py`
- 가능하면 `src/e2r/research/report_parser.py`

변경 위치:

- `src/e2r/research/web_research_runner.py:321`-`322`
- `src/e2r/research/financial_text_fields.py:200`-`216`
- `src/e2r/research/report_parser.py:578`-`593`

필수 보정:

1. `financial_text_fields._target_price_revision_pct()`에 단위 보정을 넣는다.

`report_parser._target_price_revision_pct()`처럼 old/new 각각의 unit을 읽고 `만원`이면 `* 10_000` 한다.

2. 같은 기능의 parser가 둘로 갈라지지 않게 한다.

가장 안전한 구현은 공통 helper를 새로 만들거나, `financial_text_fields.py`에서 report parser의 단위 scaling 규칙과 같은 코드를 사용한다.

3. `_parse_report()` merge는 민감 숫자를 덮어쓰지 않는다.

현재:

```python
merged_fields.update(extract_e2r_text_fields(...))
```

변경:

```python
for key, value in extracted.items():
    if key in SENSITIVE_REPORT_NUMERIC_FIELDS and key in merged_fields:
        continue
    merged_fields.setdefault(key, value)
```

또는 boolean/theme hint만 `update()`하고, 숫자 필드는 `setdefault()`로 보충한다.

민감 숫자:

```python
target_revision_pct
target_price_revision_pct
target_price
fy1_eps
fy1_op
fy1_sales
fy2_eps
fy2_op
fy2_sales
est_per
est_pbr
```

4. outlier guard는 parser와 feature 양쪽에 둔다.

- parser: 명백히 300% 초과인 target revision은 `target_price_revision_outlier=True`로 표시하고 numeric field는 넣지 않는다.
- feature: 혹시 들어온 outlier도 score에서는 제외한다.

### parser audit 보강

수정 파일:

- `src/e2r/audit/parser_audit.py`

현재 `target_revision_pct > 300`만 warning이다.

확인 라인:

- `src/e2r/audit/parser_audit.py:79`-`90`

추가 체크:

```python
("target_price_revision_1m", "target_price_revision_too_high", 300.0, "hard", "score_exclude", ...)
("eps_revision_1m", "eps_revision_too_high", 300.0, "warning", "score_exclude", ...)
("op_revision_1m", "op_revision_too_high", 300.0, "warning", "score_exclude", ...)
```

중요:

- audit은 사후 경고다.
- score 제외는 feature layer에서 먼저 해야 한다.
- audit은 output에서 사람이 볼 수 있게 남기는 보조 방어선이다.

## 호출 흐름 변경 후 기대 플로우

변경 전:

1. LLM/search가 report를 찾음
2. parser가 EPS/목표가/revision을 뽑음
3. `report_proxy` consensus 생성
4. base consensus와 proxy consensus 단순 병합
5. `_latest_consensus()`가 최신 row 하나를 선택
6. score/stage 계산

변경 후:

1. LLM/search가 report를 찾음
2. parser가 EPS/목표가/revision 후보를 뽑음
3. `report_proxy` 생성 시 proxy 품질 metadata 부여
4. base consensus와 proxy consensus는 evidence용으로 보존
5. feature layer가 metric별로 score-eligible 후보만 선택
6. 구조화 consensus와 proxy가 충돌하면 proxy는 quarantine
7. score/stage 계산
8. diagnostics에 선택 source quality, conflict, quarantine 숫자 기록

쉬운 예시:

- 종목 A: structured EPS 없음, full-text report에 EPS 있음
  - full-text proxy EPS 사용 가능
- 종목 B: structured EPS `10,000`, weak proxy EPS `2,000`
  - structured EPS 사용
  - weak proxy는 evidence에는 남고 `estimate_proxy_quarantined_count_capped=1`
- 종목 C: structured consensus 없음, snippet-only 뉴스에 목표가 있음
  - 목표가 score 사용 불가
  - news/theme hint로만 남음

## 테스트 계획

### 신규 테스트 파일

`tests/test_estimate_quality.py`

필수 케이스:

1. structured consensus가 weak report proxy보다 하루 오래돼도 대표값으로 선택된다.
2. structured consensus에 없는 metric은 full-text report proxy로 보완된다.
3. weak proxy와 structured consensus가 50% 넘게 충돌하면 weak proxy가 quarantine된다.
4. revision pct가 300%를 넘으면 score 대표값에서 제외된다.
5. negative EPS/OP turnaround에서는 상대 차이로 잘못 quarantine하지 않고 diagnostic만 남긴다.
6. source 문자열이 새로 들어와도 unknown quality로 처리되고 예외가 나지 않는다.
7. report-derived proxy는 독립 consensus family로 세지 않는다.
8. CompanyGuide recent report의 `fy1_eps/target_price`는 `structured_broker_metadata` 후보가 되지만 독립 consensus family는 아니다.

### 기존 테스트 보강

`tests/test_features.py`

추가 케이스:

- `ConsensusSnapshot(source="company_guide_snapshot", date=2026-06-10, eps_e=43833)`와 `ConsensusSnapshot(source="report_proxy", date=2026-06-11, eps_e=5721)`를 같이 넣었을 때 EPS/FCF score가 proxy 최신값에 끌려가지 않는다.
- `ConsensusRevision(source="report_proxy", target_price_revision_1m=1374900)`가 있어도 `revision_score`가 100으로 튀지 않는다.
- `search_snippet_only=True` parsed field의 `target_revision_pct`는 `fields.max_percent_for_scoring()`에서 제외된다.
- report proxy consensus만 있는 경우 `evidence_family_consensus_proxy=1`, `evidence_family_consensus=0`인지 확인한다.
- structured consensus가 있는 경우 `evidence_family_consensus=1`인지 확인한다.
- `source_fields["estimate_selected_eps_source"]` 같은 문자열 source가 diagnostic_scores가 아니라 source_fields에 들어가는지 확인한다.

`tests/test_report_parser.py`

추가 케이스:

- `목표주가 8만원에서 110000원으로 상향`은 1,374,900%가 아니라 37.5%로 계산되어야 한다.
- `목표주가 기존 80,000원에서 110,000원으로 상향`도 37.5%로 계산되어야 한다.
- `target price from KRW 80,000 to KRW 110,000`도 정상 범위로 계산되어야 한다.

`tests/test_web_research_runner.py`

추가 케이스:

- `parse_research_report_text()`가 이미 넣은 `target_revision_pct`를 `extract_e2r_text_fields()`가 더 나쁜 값으로 덮어쓰지 않는다.
- fetched report의 title/snippet 숫자는 `parse_context`에 들어가더라도 민감 숫자 덮어쓰기 금지 규칙을 따른다.

`tests/test_free_web_research_runner.py`

기존 테스트 영향:

- `test_report_title_snippet_forward_estimate_flows_to_consensus_proxy`는 proxy row 생성 자체를 기대한다.
- 이 테스트는 유지하되, evidence id와 family expectation은 수정한다.
- 기존 `tests/test_free_web_research_runner.py:301`, `353`, `778`의 old id 직접 문자열 assert는 source-aware helper 기반 assert로 바꾼다.
- 기존 `tests/test_free_web_research_runner.py:304`, `356`의 `evidence_family_consensus == 1.0`은 report proxy 단독 케이스에서는 `0.0`으로 바꾸고, `evidence_family_consensus_proxy == 1.0`을 추가한다.

추가 assert 예:

```python
self.assertEqual(result.feature_input.consensus[0].source, "report_proxy")
self.assertIn("consensus_proxy_quality", result.web_result.parsed_reports[0].parsed_fields)
self.assertEqual(result.score.diagnostic_scores["evidence_family_consensus_proxy"], 1.0)
```

그리고 "full text가 너무 짧은 report proxy는 score eligible false" 케이스를 추가한다.

기존 `consensus:123456:2026-06-08:2026` id 기대는 source-aware id로 바꾼다.

예:

```python
stable_consensus_evidence_id(symbol="123456", estimate_date=date(2026, 6, 8), fiscal_year=2026, source="report_proxy")
```

추가 dedupe 케이스:

- 같은 symbol/date/fiscal_year에 `source="structured_revision"`과 `source="report_proxy"` revision이 같이 들어오면 둘 다 `feature_input.consensus_revisions`에 남는다.

`tests/test_sources.py`

추가 케이스:

- `ConsensusCSVConnector`가 consensus row의 `parsed_fields` JSON과 unknown column을 `ConsensusSnapshot.parsed_fields`에 보존한다.
- `ConsensusCSVConnector`가 revision row의 `source`와 `parsed_fields`를 `ConsensusRevision`에 보존한다.
- 기존 fixture에 `parsed_fields`가 없어도 기본 동작은 깨지지 않는다.

`tests/test_connectors.py`

추가 케이스:

- `CSVJSONDataConnector`의 consensus/revision fixture row에 `parsed_fields`와 extra column이 있을 때 metadata가 보존된다.
- `ConsensusRevision.source`가 없으면 기본값 또는 connector 기본 source로 들어간다.

`tests/test_historical_cases.py`

추가 케이스:

- historical case의 `consensus_evidence`/`revision_evidence`에 들어온 quality metadata가 모델까지 전달된다.

`tests/test_evidence_builder.py`

추가 케이스:

- `evidence_from_consensus()`와 `features._evidence_ids()`가 같은 source-aware id를 만든다.
- `evidence_from_consensus_revision()`도 같은 규칙을 쓴다.
- `legacy_evidence_id`가 `parsed_fields`에 남는다.
- `report_proxy` evidence는 tier/confidence가 structured consensus보다 낮다.

`tests/test_korea_live_lite.py`

추가 케이스:

- targeted smoke에서 CompanyGuide consensus와 web report proxy가 같이 있을 때 feature input count는 둘 다 유지된다.
- 하지만 score diagnostics에는 structured source 선택과 proxy conflict가 남는다.

예상 assert:

```python
self.assertEqual(smoke["feature_input_counts"]["consensus"], 2)
self.assertGreaterEqual(score.diagnostic_scores["estimate_conflict_count_capped"], 1.0)
self.assertEqual(score.diagnostic_scores["estimate_selected_eps_source_quality"], 90.0)
```

추가로 targeted smoke row에 estimate summary가 노출되는지 확인한다.

```python
self.assertIn("estimate_quality", smoke)
self.assertEqual(smoke["estimate_quality"]["selected_eps_source"], "company_guide_snapshot")
```

`tests/test_parser_audit.py`

추가 케이스:

- evidence parsed field에 `target_price_revision_1m=1374900`이면 audit finding이 나온다.
- 단 audit finding만으로 score 제외를 검증하지 않는다. score 제외는 `test_features.py`에서 본다.

`tests/test_evidence_builder.py` 또는 기존 evidence builder 테스트

추가 케이스:

- 같은 symbol/date/fiscal_year에 source가 다른 consensus 두 개가 있으면 evidence id가 달라 둘 다 남는다.
- `legacy_evidence_id`가 parsed_fields에 남는다.
- `derived_from_source_type="research_report"` metadata가 evidence까지 보존된다.

### 전체 검증 명령

```bash
PYTHONPATH=src python -m unittest tests.test_estimate_quality tests.test_features tests.test_report_parser tests.test_web_research_runner tests.test_free_web_research_runner tests.test_sources tests.test_connectors tests.test_historical_cases tests.test_korea_live_lite tests.test_parser_audit tests.test_evidence_builder -v
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 엣지 케이스 정적 검증 목록

패치 후 아래 케이스를 코드 리뷰로 한 번 더 확인한다.

1. consensus가 하나도 없으면 기존처럼 0/field fallback으로 간다.
2. structured consensus만 있으면 기존보다 점수가 낮아지지 않는다.
3. weak proxy만 있으면 evidence는 남지만 score 대표값 사용은 제한된다.
4. full-text proxy만 있으면 score에 사용할 수 있다.
5. structured EPS는 있고 OP가 없으면 OP는 full-text proxy로 보완 가능하다.
6. structured와 proxy가 같은 값이면 conflict가 잡히지 않는다.
7. structured와 proxy가 50% 넘게 다르면 낮은 품질 proxy만 quarantine된다.
8. 두 structured source가 충돌하면 최신/analyst_count로 tie-break하고 conflict diagnostic을 남긴다.
9. fiscal_year가 다른 후보끼리는 직접 충돌 비교하지 않는다.
10. future date consensus/revision은 모델에서 계속 막힌다.
11. `ConsensusRevision(source=...)` 추가가 기존 생성자를 깨지 않는다.
12. evidence id 형식은 `revision:{symbol}:{date}:{fiscal_year}:{source_key}`처럼 source-aware가 된다.
13. source_name은 `"ConsensusRevision"` 고정이 아니라 실제 source를 반영한다.
14. `target_price_revision_1m=1374900` 같은 outlier는 score 제외된다.
15. `target_revision_pct=37.5` 같은 정상 수치는 유지된다.
16. `search_snippet_only=True` news 숫자는 score numeric max에서 제외된다.
17. snippet-only boolean theme hint는 기존 Green block과 함께 유지된다.
18. fetched full news의 actual-like 숫자는 official actual처럼 다루지 않는다.
19. official `FinancialActual`은 parsed news actual보다 우선한다.
20. actual field가 news에서만 왔으면 diagnostic에 source quality가 낮게 남는다.
21. recent price가 없으면 target price conflict의 price 대비 검사는 건너뛴다.
22. PER/PBR이 0 또는 음수이면 기존 non-negative validation과 score guard가 유지된다.
23. EPS가 음수에서 양수로 전환되는 turnaround는 상대 차이 quarantine으로 오판하지 않는다.
24. analyst_count가 있는 structured consensus는 tie-break에서 유리하다.
25. unknown source는 예외 없이 중간 품질로 처리한다.
26. CompanyGuide recent report는 report evidence로 남는다.
27. CompanyGuide recent report comment 숫자가 무조건 consensus proxy로 승격되지는 않는다.
28. LLM agent fields는 routing/theme hint로 남되 numeric score에는 별도 eligibility를 적용한다.
29. Stage enum은 바꾸지 않는다.
30. Stage 2/3 threshold는 이번 패치에서 바꾸지 않는다.
31. parser audit warning은 stage를 직접 바꾸지 않는다.
32. hard audit은 기존처럼 Green block 또는 manual review 경로에 남는다.
33. dedupe가 evidence를 잃지 않는다.
34. cache/output schema가 source field 추가로 JSON 직렬화 실패하지 않는다.
35. full unittest가 fixture 기반으로 통과한다.
36. `diagnostic_scores`에는 문자열이 들어가지 않는다.
37. selected source 이름은 `source_fields` 또는 run log summary로만 노출된다.
38. 같은 날짜/회계연도에 source가 다른 consensus evidence 두 개가 모두 남는다.
39. 같은 날짜/회계연도에 source가 다른 revision evidence 두 개가 모두 남는다.
40. source-aware evidence id 변경 후 기존 test expectation을 모두 수정한다.
41. `legacy_evidence_id`가 evidence parsed_fields에 남아 감사 추적이 가능하다.
42. report-derived proxy는 `evidence_family_consensus_proxy`로 표시되지만 `evidence_family_consensus`에는 포함되지 않는다.
43. structured consensus는 `evidence_family_consensus`에 포함된다.
44. CompanyGuide recent report 숫자는 structured broker metadata 후보로 쓰일 수 있지만 독립 consensus family로 세지 않는다.
45. target price revision parser가 `만원`과 `원` 혼합 표기를 정상 스케일링한다.
46. `web_research_runner._parse_report()`가 더 약한 text extractor 숫자로 report parser 숫자를 덮어쓰지 않는다.
47. `EstimateQualityContext`가 한 번만 만들어지고 내부 scoring 함수들이 같은 context를 공유한다.
48. revision score와 medium-term revision visibility가 서로 다른 revision selection을 쓰지 않는다.
49. information confidence analyst bonus가 weak/report-derived proxy analyst_count로 올라가지 않는다.
50. targeted smoke run log에서 estimate quality summary를 사람이 확인할 수 있다.
51. historical case loader는 consensus/revision metadata를 score quality selector까지 전달한다.
52. historical evidence id prefix 통합은 이번 패치 범위 밖으로 두고 기존 출력 호환성을 유지한다.
53. dataclass JSON 출력에 새 key가 추가돼도 내부 `_jsonable()` 직렬화가 실패하지 않는다.

## 작업 순서

1. `src/e2r/research/financial_text_fields.py` 목표가 변경률 단위 보정
2. `src/e2r/research/web_research_runner.py` report merge를 민감 숫자 덮어쓰기 금지 방식으로 변경
3. `src/e2r/models.py`에 `ConsensusSnapshot.parsed_fields`, `ConsensusRevision.source`, `ConsensusRevision.parsed_fields` 추가
4. `src/e2r/sources/consensus.py`, `src/e2r/connectors.py`, `src/e2r/historical_cases/__init__.py`에서 consensus/revision `parsed_fields`와 revision `source` 전달
5. `src/e2r/evidence_ids.py`에 consensus/revision evidence id helper 추가
6. `src/e2r/pipeline/evidence_builder.py`와 `features._evidence_ids()`에서 공통 id helper 사용
7. `src/e2r/research/free_web_research_runner.py`의 `_dedupe_revisions()`를 source-aware key로 변경
8. `src/e2r/estimate_quality.py` 추가
9. `src/e2r/research/report_consensus_proxy.py`에 proxy quality metadata와 revision source/parsed_fields 추가
10. `src/e2r/pipeline/evidence_builder.py`에 source-aware tier/confidence, metadata merge, legacy id 보존 적용
11. `src/e2r/features.py`에서 `EstimateQualityContext`를 한 번 만들고 내부 scoring 함수에 전달
12. `src/e2r/features.py`에서 `_latest_consensus()` 직접 사용을 metric selection으로 교체
13. `src/e2r/features.py`의 `_ParsedFieldSource`에 scoring용 numeric filter와 source-aware mapping metadata 추가
14. `src/e2r/features.py`의 evidence family/information confidence를 source-aware로 변경
15. `src/e2r/pipeline/korea_live_lite.py` targeted smoke row에 핵심 estimate quality summary 추가
16. `src/e2r/audit/parser_audit.py`에 revision outlier field 추가
17. 테스트 추가/수정
18. targeted unit tests 실행
19. full unittest 실행
20. 삼성전자/SK하이닉스 운영형 재실행은 선택 검증으로 수행

## 구현 완료 기준

패치는 다음 조건을 만족해야 완료다.

1. 구조화 consensus와 report proxy가 충돌해도 최신 proxy가 대표 EPS/target/PER/PBR을 빼앗지 않는다.
2. `target_price_revision_1m` outlier가 revision score를 100으로 만들지 않는다.
3. proxy evidence는 삭제되지 않고 audit 가능한 상태로 남는다.
4. score diagnostics에 선택 source quality와 quarantine/conflict count가 남는다.
5. 문자열 source 이름은 `source_fields` 또는 run log summary에 남고, numeric-only diagnostic validation을 깨지 않는다.
6. 같은 날짜/회계연도에 source가 다른 consensus/revision evidence가 둘 다 보존된다.
7. report-derived proxy가 독립 consensus evidence family를 과대계산하지 않는다.
8. 목표가 변경률 단위 오류로 1,374,900% 같은 값이 만들어지지 않는다.
9. 종목명/섹터명 하드코딩이 없다.
10. 기존 Stage enum과 Stage threshold는 유지된다.
11. `PYTHONPATH=src python -m unittest discover -s tests -v`가 통과한다.

## 이번 문서 작성 후 교차검증 결과

실제 코드와 문서를 대조한 결론:

- live API 연결 부족 문제가 아니라, 들어온 숫자를 점수로 쓰기 전의 품질 선택 레이어가 부족하다.
- CompanyGuide는 이미 live pipeline에 들어온다.
- `report_proxy`는 evidence 보존 자체는 맞지만 score 대표값으로 바로 경쟁하면 안 된다.
- `ConsensusRevision`에 source가 없어 proxy revision 방어가 약하다.
- `ConsensusSnapshot`에도 metadata가 없어 proxy quality가 downstream으로 전달되지 않는다.
- consensus/revision evidence id에 source가 없어 같은 날짜의 여러 source evidence가 dedupe로 사라질 수 있다.
- report parser와 financial text parser의 목표가 변경률 단위 처리 차이가 outlier를 만들 수 있다.
- parser audit은 일부 이상치를 경고하지만, score 계산 전에 numeric outlier를 제외하는 기능은 아직 없다.
- 따라서 다음 패치는 수집기 추가가 아니라 `parser numeric guard + estimate_quality + source-aware evidence` 레이어가 우선이다.
