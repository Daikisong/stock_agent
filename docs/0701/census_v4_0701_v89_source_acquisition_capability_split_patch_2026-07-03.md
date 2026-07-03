# Census v4 v89 - Source Acquisition Capability Split Patch

작성일: 2026-07-03

목적: v88의 `source_connector_capability_audit`를 더 정확하게 만든다. v88은 production connector registry만 보고 `NaverSearch`, `CompanyNewsroom`, `ReportPDF`, `BrokerReportPublicPDF`, `GeneralWebSearch`까지 "통로 없음"으로 분류했다. 그런데 현재 코드에는 `SourceAcquisitionRunnerV4.live_full_bounded`가 bounded web search, page fetch, issuer-original lineage, broker-report-original lineage를 이미 구현하고 있다.

이번 패치는 registry connector와 bounded source acquisition capability를 분리한다.

## 결론

현재 최신 audit:

```text
output/test_census_v4_cached/source_connector_capability_audit.json
```

현재 결과:

```text
verdict = PENDING_SOURCE_CONNECTOR_CAPABILITY
source_connector_capability_pass_allowed = false
full_thesis_required_source_class_count = 11
blocking_full_thesis_source_class_count = 2
blocking_full_thesis_source_classes = IssuerIR, TrustedNews
blocking_full_thesis_task_count = 0
full_thesis_task_executable_source_path_pass_allowed = true
full_thesis_task_with_blocking_source_class_count = 83
registered_live_connector_count = 4
acquisition_capability_count = 5
```

쉽게 말하면:

```text
v88:
  리포트 PDF, 회사 뉴스룸, 네이버도 "우편함 없음"으로 봤다.

v89:
  리포트 PDF, 회사 뉴스룸, 네이버는 전용 registry connector는 없지만
  bounded web acquisition 경로가 있으므로 "우편함은 있다"로 본다.
  단 실제 서류가 도착했는지는 SourceTaskExecution/evidence document/claim으로 따로 증명해야 한다.

아직 진짜 blocker:
  IssuerIR, TrustedNews는 placeholder connector라서 FULL_THESIS source capability pass 불가.

production full-thesis task 관점:
  83개 task가 IssuerIR/TrustedNews를 함께 언급하지만,
  DART/KIND/KRX/CompanyGuide 또는 bounded web acquisition 대체 경로도 있으므로
  "실행 가능한 source path가 전혀 없는 task"는 0개다.
```

## 코드 패치

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_goal_required_audits.py
docs/0701/README.md
docs/0701/census_v4_0701_v89_source_acquisition_capability_split_patch_2026-07-03.md
```

추가/변경된 audit 필드:

```text
acquisition_capability_count
acquisition_capability_rows
bounded_web_acquisition_source_classes
registry_missing_but_acquisition_covered_source_classes
registry_capability_status
acquisition_capability_status
acquisition_capability_scope
acquisition_score_evidence_rule
```

추가된 helper:

```text
_source_class_registry_capability_status
_source_class_capability_can_execute_source_task
_source_acquisition_capability_rows
```

## 새 Capability 분류

Registry live connector:

```text
DART -> LIVE_FETCH_IMPLEMENTED
KIND -> LIVE_FETCH_IMPLEMENTED
KRX -> LIVE_FETCH_IMPLEMENTED
CompanyGuide -> LIVE_FETCH_IMPLEMENTED
```

Bounded acquisition path:

```text
NaverSearch -> BOUNDED_WEB_SEARCH_FETCH_IMPLEMENTED
GeneralWebSearch -> BOUNDED_WEB_SEARCH_FETCH_IMPLEMENTED
CompanyNewsroom -> BOUNDED_WEB_VERIFIED_ISSUER_ORIGINAL_IMPLEMENTED
BrokerReportPublicPDF -> BOUNDED_WEB_VERIFIED_REPORT_ORIGINAL_IMPLEMENTED
ReportPDF -> BOUNDED_WEB_VERIFIED_REPORT_ORIGINAL_IMPLEMENTED
```

Still blocking:

```text
IssuerIR -> PLACEHOLDER_PROVIDER_FAILED
TrustedNews -> PLACEHOLDER_PROVIDER_FAILED
```

Missing but not full-thesis-blocking in current queue:

```text
IssuerOfficial -> NO_PRODUCTION_CONNECTOR_REGISTERED
```

## 중요한 제한

이 패치는 실제 live fetch 성공을 의미하지 않는다.

```text
BOUNDED_WEB_SEARCH_FETCH_IMPLEMENTED
```

의 뜻은:

```text
SourceTask가 max_queries/max_candidates/max_fetches budget을 들고
LLM query intent를 제공하면,
검색 결과를 가져오고,
full page fetch를 시도하고,
snippet-only 점수화를 막는 코드 경로가 있다.
```

의 뜻이다.

점수에 들어가려면 여전히 아래가 필요하다.

```text
SourceTaskExecution
-> EvidenceDocument
-> EvidenceAnchor
-> accepted claim
-> ScoreContribution
-> StageCourt
```

쉬운 예:

```text
네이버 검색 결과 제목:
  "SK하이닉스 HBM 기사"

이건 아직 점수 0점이다.

점수가 되려면:
  기사 원문 fetch 성공
  원문 안에 SK하이닉스 직접 claim 존재
  날짜가 as_of_date 이전
  quote/anchor 검증
  LLM/검증기를 거쳐 accepted claim 생성
  score contribution에 support_claim_id로 연결
```

## 왜 이 패치가 필요한가

v88은 좋은 방향이었지만 너무 뭉뚱그렸다.

```text
registry connector 없음
```

과

```text
bounded source acquisition path 없음
```

은 다르다.

예를 들어 `CompanyNewsroom`은 별도 connector class는 없지만, 현재 `SourceAcquisitionRunnerV4`가 다음 방식으로 검증한다.

```text
CompanyGuide snapshot 또는 issuer official domain registry에서 공식 홈페이지 domain 확인
-> 검색 결과 URL host가 그 domain 또는 subdomain인지 확인
-> title/snippet에 대상회사 alias가 있는지 확인
-> full page fetch
-> verified_issuer_original lineage 부여
```

따라서 "통로 없음"이라고 하면 부정확하다. 정확한 표현은:

```text
bounded acquisition 통로는 있으나, 실제 live execution pass와 accepted claim pass는 아직 별도 증명 필요.
```

## Goal gate 영향

현재도:

```text
SOURCE_CONNECTOR_CAPABILITY_PASS = false
READY_FOR_FULL_THESIS_OPERATION = false
```

다만 blocker 의미가 더 좁아졌다.

```text
v88 blocker class count = 7
v89 blocker class count = 2
```

남은 blocker:

```text
1. IssuerIR placeholder를 실제 issuer IR discovery/fetch provider로 교체
2. TrustedNews placeholder를 trusted full-source provider로 교체하거나,
   TrustedNews 요구를 verified CompanyNewsroom/BrokerReportPublicPDF/Naver full-source fallback 정책으로 재분류
```

단, 현재 production full-thesis queue task 자체는 대체 source path를 갖고 있다.

```text
blocking_full_thesis_task_count = 0
full_thesis_task_with_blocking_source_class_count = 83
```

따라서 다음 구현 우선순위는 "task가 아예 실행 불가능하다"가 아니라:

```text
1. IssuerIR/TrustedNews source class 요구를 실제 provider로 닫을 것인지,
2. 아니면 CompanyNewsroom/BrokerReportPublicPDF/Naver full-source fallback으로 충분한 task는
   source policy에서 명시적으로 재분류할 것인지
```

를 결정하는 것이다.

Controlled smoke note:

```text
FTSMOKE controlled URL-backed replay task는 production source connector capability blocker 계산에서 제외했다.
controlled smoke는 FULL_THESIS production source capability가 아니라 별도 smoke/replay gate다.
```

## 테스트

실행:

```bash
PYTHONPATH=src python -m py_compile src/e2r/census/census_runner_v4.py
PYTHONPATH=src python -m unittest tests.test_census_v4_goal_required_audits -v
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
py_compile = OK
tests.test_census_v4_goal_required_audits = 4 tests OK
census v4 test_census_v4_* = 139 tests OK
full unittest discover = 5122 tests OK
```

중요:

```text
위 테스트 통과는 SOURCE_CONNECTOR_CAPABILITY_PASS가 통과됐다는 뜻이 아니다.
v89는 blocker를 더 정확히 분류했을 뿐이고,
IssuerIR/TrustedNews placeholder 때문에 pass_allowed는 여전히 false다.
```

추가 Census v4 전체 검증:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
```

결과:

```text
Ran 139 tests in 80.038s
OK
```

전체 회귀 검증:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5122 tests in 225.644s
OK
```

검증된 내용:

```text
ReportPDF/CompanyNewsroom은 더 이상 missing connector로 분류하지 않음
ReportPDF/BrokerReportPublicPDF/CompanyNewsroom은 registry_missing_but_acquisition_covered로 분류
NaverSearch/GeneralWebSearch는 bounded_web_acquisition_source_classes에 포함
IssuerIR/TrustedNews placeholder는 계속 blocker로 남음
FTSMOKE controlled smoke task는 production source connector blocker 계산에서 제외
blocking_full_thesis_task_count는 0으로 분리
SOURCE_CONNECTOR_CAPABILITY_PASS는 여전히 false
```

## 다음 에이전트 공격 포인트

다음 에이전트는 아래를 확인하면 된다.

```text
1. bounded acquisition capability를 live fetch success로 과장하지 않았는가?
2. snippet-only source가 score evidence로 들어갈 수 있는가?
3. CompanyNewsroom lineage가 as_of_date 이후 registry entry를 쓰지 않는가?
4. BrokerReportPublicPDF가 임의 PDF나 블로그 PDF를 original report로 오인하지 않는가?
5. IssuerIR/TrustedNews placeholder가 여전히 pass blocker로 남는가?
```

현재 패치의 의도는 READY 선언이 아니다. 남은 blocker를 더 정확히 좁히는 것이다.
