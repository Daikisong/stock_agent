# Census v4 Live Official Source Bridge Patch - 2026-07-01

작성 목적:

```text
Stage가 있는 애들이 있긴 한가?
그 Stage가 실제 운영 Stage인가?
Brain/Web enabled를 켰을 때 실제 live source가 들어오는가?
snapshot이나 count-only 장부가 또 real evidence처럼 둔갑하지 않는가?
```

이 문서는 위 질문을 다음 에이전트가 바로 공격할 수 있게 현재 사실, 패치, 검증 결과, 남은 blocker를 한 곳에 고정한다.

최신 enabled probe와 추가 패치는 아래 문서를 같이 봐야 한다.

```text
docs/0701/census_v4_live_brain_candidate_and_opendart_forensic_2026-07-01.md
```

최신 보강 사항:

```text
1. live planner 첫 후보가 fixture/cache가 아니라 CE-LIVE-DART-* URL-backed 후보가 되도록 discovery/order를 보강했다.
2. candidate purity registry가 output/census_v3/v4 universe.jsonl도 alias registry로 읽게 했다.
3. OpenDART document.xml ZIP payload가 PK 바이너리 quote로 새지 않게 디코딩했다.
4. OpenDART XML CSS 노이즈를 제거했다.
5. 그래도 최신 enabled probe는 accepted Brain claim 0개로 NOT_READY다.
```

## 짧은 결론

현재 답은 둘로 나눠야 한다.

```text
1. Stage label은 있다.
2. full E2R 100점 thesis 운영 Stage는 아직 0개다.
```

현재 `output/census_v4/2026-07-01/census_stage_status.jsonl` 재검산값:

```text
rows: 3391

base_stage:
  Stage0       3306
  Stage1         54
  Stage2-Watch   30
  Red             1

canonical_stage:
  0       3306
  1         54
  2         30
  3-Red      1

stage_scope:
  CENSUS_EVENT_BOARD 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE 3391

operator_score_use:
  NOT_FULL_E2R_SCORE 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN 3391

score_scale:
  NO_SCORE               3324
  EVENT_WEIGHTED_PARTIAL   67

verified_score_present: 0
full_e2r_verified_score_present: 0
```

재검산 명령:

```bash
python - <<'PY'
import json
from collections import Counter
from pathlib import Path

p = Path("output/census_v4/2026-07-01/census_stage_status.jsonl")
rows = [json.loads(line) for line in p.read_text().splitlines() if line.strip()]
print("rows", len(rows))
for key in [
    "base_stage",
    "canonical_stage",
    "stage_scope",
    "operator_stage_use",
    "operator_score_use",
    "full_thesis_stage",
    "score_scale",
]:
    print(key, dict(Counter(row.get(key) for row in rows)))
print("verified_score_present", sum(1 for r in rows if r.get("verified_score") not in (None, "", "null")))
print("full_e2r_verified_score_present", sum(1 for r in rows if r.get("full_e2r_verified_score") not in (None, "", "null")))
PY
```

쉬운 예:

```text
지금 Stage label은 병원 접수표의 "대기 / 추가 검사 필요 / 위험 신호 있음"에 가깝다.
최종 진단서, 즉 full thesis 운영 Stage는 아직 나온 종목이 없다.
```

따라서 지금 `Stage1`, `Stage2-Watch`, `3-Red` 같은 label을 보고 "삼성전자/하이닉스 운영 Stage가 나왔다"고 말하면 실패다.

## 이번에 확인한 핵심 문제

`src/e2r/production/source_connectors/`에는 live connector가 이미 있었다.

```text
OpenDARTLiveConnector
KINDLiveConnector
KRXLiveConnector
CompanyGuideLiveConnector
IssuerIRLiveConnector
TrustedNewsLiveConnector
```

하지만 `SourceAcquisitionRunnerV4`는 `live_official_first`, `live_official_only`, `live_full_bounded` 모드에서도 먼저 저장 snapshot만 뒤졌다.

이전 구조:

```text
live_official_only
  -> _candidate_snapshots()
  -> snapshot://company_guide/...
  -> snapshot://opendart/...
```

문제:

```text
live connector가 있어도 EvidenceDocument로 들어오지 않았다.
그래서 Brain/Web enabled smoke에서 accepted claim이 생겨도 source_url이 snapshot://이면 score eligible이 아니었다.
```

쉬운 예:

```text
학교에 원본 성적 조회 시스템이 있는데,
실제 채점 장부는 계속 예전 복사본 파일만 보고 있던 상태다.
```

## 패치 내용

변경 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/production/source_connectors/opendart_live_connector.py
tests/test_research_brain_v4_real_source_acquisition.py
```

핵심 변경:

```text
SourceAcquisitionRunnerV4(mode=live_official_*)
  -> SourceProviderRegistry에서 source_class에 맞는 live connector 선택
  -> connector.fetch(..., mode="live")
  -> SourceFetchResult.counts_as_live 확인
  -> EvidenceDocument + EvidenceAnchor 생성
  -> canonical_url이 snapshot://가 아닌 live URL이면 real_document_fetched_count로 집계 가능
```

새 helper:

```text
_acquire_live_official_sources
_source_fetch_text
_score_block_reasons_for_live_result
_date_or_datetime_from_any
```

중요한 방어:

```text
1. live mode라도 fetched result가 snapshot://이면 real로 세지 않는다.
2. KIND/KRX portal main page처럼 symbol claim이 아닌 provider coverage 문서는 score_block_reasons를 단다.
3. IssuerIR/TrustedNews 미구현은 provider failure로 남기고 "증거 없음"으로 확정하지 않는다.
4. live_official_only는 live provider 실패 시 snapshot fallback을 쓰지 않는다.
5. live_official_first/live_full_bounded는 live 실패 후 snapshot fallback을 diagnostic으로 쓸 수 있지만, snapshot은 score eligible이 아니다.
```

쉬운 예:

```text
원본 서류를 가져오면 "원본 확보"로 센다.
복사본 서류는 참고 자료로 볼 수는 있어도 운영 점수 서류로 승격하지 않는다.
```

## OpenDART Detail 패치

추가로 `OpenDARTLiveConnector`를 확장했다.

이전 동작:

```text
OpenDARTLiveConnector.fetch(live)
  -> corpCode.xml
  -> company.json
  -> 회사 기본정보 문서만 반환
```

문제:

```text
company.json은 공식 live 문서지만 계약/공시 detail claim을 만들기에는 부족하다.
예: 회사 주소와 업종만 보고 "계약금액/계약상대방/계약기간"을 채울 수는 없다.
```

새 동작:

```text
OpenDARTLiveConnector.fetch(live)
  -> corpCode.xml로 corp_code 확인
  -> list.json에서 최근 540일 watch 공시 확인
  -> watch 공시가 있으면 document.xml detail fetch
  -> 기존 normalize_disclosure_detail parser 재사용
  -> detail parsed fields를 SourceFetchResult.structured_payload에 넣음
  -> 없거나 실패하면 list-only/company-profile score block 부여
```

score block:

```text
opendart_list_only_detail_not_fetched
company_profile_not_score_evidence
```

중요:

```text
list.json 제목만으로는 contract_quality나 earnings_visibility를 열지 않는다.
document.xml detail에서 계약금액, 매출액 대비, 기간, 상대방 같은 anchor가 나와야 claim 후보가 된다.
```

쉬운 예:

```text
"계약 공시가 있었다"는 접수증이다.
"계약금액 4,000억원, 매출액 대비 45%, 계약기간 2024~2027, 상대방 북미 유틸리티"가 본문에 있어야 채점 가능한 계약서다.
```

## 새 테스트

추가한 테스트:

```text
tests/test_research_brain_v4_real_source_acquisition.py

test_live_official_mode_uses_connector_document_not_snapshot_fallback
test_live_official_document_counts_as_real_non_snapshot_document
test_opendart_live_connector_prefers_detail_disclosure_over_company_profile
test_opendart_live_connector_blocks_list_only_disclosure_when_detail_fails
```

검증 내용:

```text
fake live connector가 https://example.com/companyguide/A005930 문서를 반환
-> SourceAcquisitionRunnerV4(mode=live_official_only)가 snapshot fallback 없이 EvidenceDocument 생성
-> build_source_acquisition_report_v4에서:
   fetched_document_count = 1
   snapshot_document_fetched_count = 0
   real_document_fetched_count = 1
   unique_real_document_fetched_count = 1
   real_document_count_semantics = live_non_snapshot_document_only
```

OpenDART detail 테스트 검증 내용:

```text
fake OpenDART list.json이 단일판매·공급계약체결 row 반환
fake document.xml이 계약금액/매출액 대비/계약기간/계약상대방 본문 반환
-> OpenDARTLiveConnector가 company.json으로 내려가지 않고 detail disclosure 반환
-> canonical_url = https://dart.fss.or.kr/dsaf001/main.do?rcpNo=...
-> structured_payload.contract_amount_to_prior_sales = 0.45
-> structured_payload.counterparty = 북미 유틸리티
-> score_usage 없음

document.xml 실패
-> row_source = opendart_list
-> score_usage = opendart_list_only_detail_not_fetched
-> contract_amount_to_prior_sales 없음

score_usage가 있는 live provider coverage 문서
-> EvidenceDocument.score_block_reasons로 전파
-> PARSED 문서라도 점수 후보가 아님
```

## 실행한 검증

컴파일:

```bash
python -m py_compile \
  src/e2r/research_brain/v4_source_acquisition_runner.py \
  src/e2r/production/source_connectors/opendart_live_connector.py \
  tests/test_research_brain_v4_real_source_acquisition.py
```

결과:

```text
OK
```

타깃 테스트 1:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition -v
```

결과:

```text
Ran 6 tests in 0.010s
OK
```

타깃 테스트 2:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_cutover_v2_opendart_real_fetch \
  tests.test_cutover_real_source_connectors \
  tests.test_research_brain_v4_candidate_discovery_live_official \
  tests.test_research_brain_v4_static_logic_audit -v
```

결과:

```text
Ran 12 tests in 22.531s
OK
```

타깃 테스트 3:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits -v
```

결과:

```text
Ran 31 tests in 12.714s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 4942 tests in 170.248s
OK
```

주의:

```text
이 값은 facility correction semantic guard 패치까지 포함한 현재 워크트리 기준 로컬 전체 테스트 결과다.
canonical output의 test_result_artifact.json도 4942개 테스트 증거로 재생성했다.
그래도 이 테스트 통과는 Brain/Web evidence pass나 full thesis Stage pass가 아니다.
```

실제 live connector smoke:

```bash
PYTHONPATH=src python - <<'PY'
from datetime import date
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from tests.research_brain_v4_test_helpers import c06_source_task, sample_v4_event

result = SourceAcquisitionRunnerV4(mode="live_official_only").acquire(
    event=sample_v4_event(),
    task=c06_source_task(),
    as_of_date=date(2026, 6, 29),
)
print({
    "status": result.status,
    "provider_name": result.provider_name,
    "fetched_document_count": len(result.fetched_document_ids),
    "document_urls": tuple(url[:120] for url in result.document_urls),
    "provider_errors": result.provider_errors,
    "budget_used": dict(result.budget_used),
    "stop_reason": result.stop_reason,
})
PY
```

관측값:

```text
status: PARSED
provider_name: live_official_source_provider_registry
fetched_document_count: 1
document_urls:
  https://wcomp.fnguide.com
provider_errors:
  issuer_ir_discovery_not_configured; do not treat missing IR as no evidence
budget_used:
  queries: 2
  candidates: 2
  fetches: 1
stop_reason: live_official_source_parsed
```

해석:

```text
CompanyGuide live fetch는 EvidenceDocument로 들어왔다.
IssuerIR은 아직 미구현이므로 provider failure로 남았다.
이 smoke는 live document bridge 검증이지, score/stage pass 검증이 아니다.
```

실제 DART live source task smoke:

```text
mode: live_official_only
preferred_source_classes: DART
symbol: 005930
as_of_date: 2026-06-29
status: PARSED
provider_name: live_official_source_provider_registry
fetched_document_count: 1
document_urls:
  https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260515002181
provider_errors: ()
budget_used:
  queries: 1
  candidates: 1
  fetches: 1
stop_reason: live_official_source_parsed
source_name: OpenDART
score_block_reasons: ()
```

해석:

```text
OpenDART live connector가 실제 DART viewer URL 문서를 EvidenceDocument로 만들 수 있음은 확인됐다.
다만 이 smoke는 "문서 확보" 검증이지, 그 문서에서 삼성전자 HBM/C06 full thesis 점수가 산출됐다는 뜻이 아니다.
```

## 아직 완료가 아닌 이유

이번 패치는 "실제 문서를 가져오는 배관"만 연다.

아직 남은 큰 구멍:

```text
1. CompanyGuide live page는 가져오지만, full numeric revision/FCF parser가 아직 score claim까지 만들지 못한다.
2. OpenDART detail disclosure는 이제 가져올 수 있지만, full thesis용 claim coverage는 아직 공시 종류별로 제한적이다.
3. KIND/KRX live connector는 portal coverage page라서 symbol-specific risk claim으로 쓰면 안 된다.
4. IssuerIR discovery는 아직 provider_failed placeholder다.
5. TrustedNews/general web은 아직 bounded score source로 연결되지 않았다.
6. unstructured document LLM Claim Extractor가 full thesis primitive를 채우는 경로가 아직 대표 Stage row로 승격되지 않았다.
7. 삼성전자/하이닉스 C06/HBM full thesis smoke는 아직 `FULL_THESIS_NOT_RUN`이다.
```

쉬운 예:

```text
이번 패치는 시험지를 교실로 가져오는 문을 연 것이다.
아직 답안 채점, 오답 검증, 최종 등급 산출까지 끝난 것은 아니다.
```

## 다음 패치 방향

우선순위는 아래 순서다.

```text
1. OpenDART list/detail disclosure live connector coverage를 넓힌다.
   - 오늘 패치로 rcept_no detail fetch와 일부 계약 detail parsed field는 v4 acquisition에 들어온다.
   - 다음은 공시 종류별 정정/철회/감사의견/투자/잠정실적 detail anchor를 더 넓혀야 한다.

2. CompanyGuide live document에서 revision/target price/EPS/OP/FCF 관련 structured anchor를 만든다.
   - page fetch 성공만으로 score를 주지 않는다.
   - 숫자 field와 날짜가 anchor로 검증될 때만 claim 후보가 된다.

3. IssuerIR discovery를 bounded official-first SourceTask로 구현한다.
   - 회사 IR/실적발표/컨콜/자료실 URL을 찾되, 무제한 검색은 금지한다.

4. TrustedNews는 general web fallback이 아니라 bounded fallback으로 둔다.
   - source task가 허용한 경우에만 제한적으로 실행한다.
   - snippet-only는 score evidence가 아니다.

5. LLM Claim Extractor를 contract-blind로 live document text에 붙인다.
   - score gap이나 Green 목표를 보여 주지 않는다.
   - 먼저 문서가 실제로 무슨 말을 하는지만 추출한다.

6. Target/Temporal/Primitive Mapping을 분리한다.
   - 월덱스 감사의견 같은 wrong-subject/normal/historical claim은 여기서 점수 불가가 되어야 한다.

7. strict promotion 조건을 닫는다.
   - accepted claim -> primitive state -> score contribution -> StageCourt trace -> representative census row
   - 같은 claim id로 전부 이어질 때만 운영 Stage row 승격.

8. 삼성전자/하이닉스 C06/HBM full thesis smoke를 별도 실행한다.
   - daily event board score와 절대 섞지 않는다.
```

## 다음 에이전트 공격 질문

다음 에이전트는 아래 질문을 먼저 때려야 한다.

```text
Q1. `live_official_only`가 아직 snapshot:// 문서를 반환하는가?
    기대: 반환하지 않아야 한다. 실패하면 provider failure/no evidence가 맞다.

Q2. `real_document_fetched_count`가 snapshot을 포함하는가?
    기대: 포함하면 안 된다. live non-snapshot URL만 포함해야 한다.

Q3. CompanyGuide/KIND/KRX portal fetch만으로 score claim이 생기는가?
    기대: 생기면 안 된다. provider coverage와 score evidence는 다르다.

Q4. OpenDART company.json만으로 계약 quality 점수가 생기는가?
    기대: 생기면 안 된다. company.json과 list-only disclosure는 score-blocked여야 한다.
    단, document.xml detail이 fetch/anchor/parse된 disclosure는 별도 검증 후 claim 후보가 될 수 있다.

Q5. Brain/Web accepted claim이 score_eligible=true로 자동 승격되는가?
    기대: document/anchor/date/DIRECT/CURRENT/ACCEPTED/primitive/non-snapshot guard를 모두 통과해야 한다.

Q6. Stage label이 full thesis 운영 Stage로 표시되는가?
    기대: 현재 canonical output에서는 전부 NOT_FULL_THESIS_STAGE여야 한다.

Q7. 삼성전자/하이닉스가 C06 full thesis Stage로 나온 것처럼 보이는가?
    기대: 현재는 FULL_THESIS_NOT_RUN이어야 한다.
```

## 최종 판정

이번 패치 후 말할 수 있는 것:

```text
live_official_* source acquisition이 실제 live connector 결과를 EvidenceDocument/Anchor로 만들 수 있게 됐다.
snapshot은 계속 score-ineligible이고 real_document_fetched_count에 들어가지 않는다.
현재 0701 canonical run은 여전히 anti-fake 상태판 PASS일 뿐, full thesis 운영 Stage PASS가 아니다.
```

말하면 안 되는 것:

```text
Brain/Web evidence pass 완료
삼성전자/하이닉스 full thesis Stage 산출
전 종목 E2R 100점 verified score 산출
Stage3-Green/Yellow/4B/4C 운영 판정 완료
```

한 줄로 정리하면:

> 문서 원본을 가져오는 첫 배관은 열었다. 그러나 그 원본을 claim, primitive, score, Stage로 안전하게 승격하는 검증 사슬은 아직 남아 있다.
