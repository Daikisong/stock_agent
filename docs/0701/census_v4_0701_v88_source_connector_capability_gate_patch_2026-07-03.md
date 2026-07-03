# Census v4 v88 - Source Connector Capability Gate Patch

작성일: 2026-07-03

목적: v87에서 확인한 "Stage row는 있지만 운영 FULL_THESIS Stage는 0개" 문제의 다음 원인을 코드 audit에 연결한다. 이번 패치는 실제 live fetch를 새로 만든 것이 아니라, FULL_THESIS가 요구하는 source class가 production connector로 감당 가능한지 정직하게 장부화하고 readiness/goal gate에 연결한 패치다.

## 결론

새 audit:

```text
source_connector_capability_audit.json
```

이번 검증에서 실제 확인한 artifact 위치:

```text
output/test_census_v4_cached/source_connector_capability_audit.json
```

운영 문서 export 경로:

```text
docs/operational/census_mode_v4_source_connector_capability_audit.json
```

단, `docs/operational` 복사본은 `CensusV4RunConfig.write_operational_docs=True` 실행에서 쓰는 export다. 테스트 fixture 검증은 `output/test_census_v4_cached`의 원본 artifact를 기준으로 한다.

새 goal gate:

```text
SOURCE_CONNECTOR_CAPABILITY_PASS
```

현재 결과:

```text
verdict = PENDING_SOURCE_CONNECTOR_CAPABILITY
source_connector_capability_pass_allowed = false
full_thesis_required_source_class_count = 11
blocking_full_thesis_source_class_count = 7
blocking_full_thesis_task_count = 97
placeholder_source_classes = IssuerIR, TrustedNews
missing_connector_source_classes =
  BrokerReportPublicPDF
  CompanyNewsroom
  GeneralWebSearch
  IssuerOfficial
  NaverSearch
  ReportPDF
```

쉽게 말하면:

```text
FULL_THESIS가 "IR, 뉴스, 리포트, 회사 newsroom도 봐야 한다"고 요구하고 있는데,
현재 production connector 장부에는 IR/TrustedNews가 placeholder이고,
리포트 PDF, 회사 newsroom, Naver, general web search는 registry source connector로 닫혀 있지 않다.
```

따라서 FULL_THESIS 운영 준비가 통과하면 안 된다.

## 코드 패치

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_goal_required_audits.py
docs/0701/README.md
docs/0701/census_v4_0701_v88_source_connector_capability_gate_patch_2026-07-03.md
```

추가된 함수:

```text
_source_connector_capability_audit
_connector_capability_status
_source_class_capability_status
_source_connector_requirement_rows
_source_connector_requirement_rows_from_task
_source_class_list
_row_is_full_thesis_requirement
_canonical_source_class
```

## Audit가 하는 일

네트워크/API 호출은 하지 않는다. 정적 검사만 한다.

검사 대상:

```text
1. production SourceProviderRegistry에 등록된 connector
2. full_thesis_refresh_queue.jsonl의 preferred/fallback source classes
3. source_tasks.jsonl의 preferred/fallback/requested source classes
4. source_task_executions.jsonl의 embedded source_task source classes
```

source class 이름을 맞춘다.

예:

```text
OpenDART -> DART
DART -> DART
IR -> IssuerIR
IssuerIR -> IssuerIR
BrokerPDF -> BrokerReportPublicPDF
Web / GeneralWeb -> GeneralWebSearch
```

그리고 각 source class를 이렇게 분류한다.

```text
LIVE_FETCH_IMPLEMENTED
PLACEHOLDER_PROVIDER_FAILED
SNAPSHOT_ONLY
NO_PRODUCTION_CONNECTOR_REGISTERED
```

## 현재 connector 상태

등록 connector 6개:

```text
OpenDARTLiveConnector -> DART -> LIVE_FETCH_IMPLEMENTED
KINDLiveConnector -> KIND -> LIVE_FETCH_IMPLEMENTED
KRXLiveConnector -> KRX -> LIVE_FETCH_IMPLEMENTED
CompanyGuideLiveConnector -> CompanyGuide -> LIVE_FETCH_IMPLEMENTED
IssuerIRLiveConnector -> IssuerIR -> PLACEHOLDER_PROVIDER_FAILED
TrustedNewsLiveConnector -> TrustedNews -> PLACEHOLDER_PROVIDER_FAILED
```

중요:

```text
LIVE_FETCH_IMPLEMENTED는 "코드 경로가 있다"는 뜻이지,
이번 run에서 실제 fetch가 성공했다는 뜻이 아니다.
실제 fetch 성공은 source_task_realness_audit/source_task_executions/evidence_documents로 따로 증명해야 한다.
```

## Goal gate 연결

`goal_requirement_matrix_audit.json`에 추가:

```text
SOURCE_CONNECTOR_CAPABILITY_PASS
```

현재 pending:

```text
SOURCE_CONNECTOR_CAPABILITY_PASS
FULL_THESIS_PRODUCTION_PASS
FULL_THESIS_SEED_PROMOTION_PASS
BRAIN_WEB_EVIDENCE_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
FULL_TEST_ARTIFACT_PASS
```

`goal_completion_audit.json` blocker에 추가:

```text
source_connector_capability_pending
```

`readiness_verdict.json` remaining gap에도 추가:

```text
full-thesis source connector capability is pending:
BrokerReportPublicPDF, CompanyNewsroom, GeneralWebSearch,
IssuerIR, NaverSearch, ReportPDF, TrustedNews
```

## 왜 이 패치가 필요한가

이전 상태에서도 source task chain과 id link audit은 있었다.

```text
source_task_satisfaction_audit = PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
source_task_realness_audit = PASS_LEDGER_REFRESH_REALNESS
```

하지만 이건 "기존 ledger-refresh chain이 끊기지 않았다"는 뜻이었다.

이번 audit는 다른 질문에 답한다.

```text
FULL_THESIS가 요구하는 source class를 실제 production connector registry가 감당할 수 있는가?
```

현재 답은 no다.

쉬운 예:

```text
기존 감사:
  창고에 있던 서류번호와 검토표 번호가 서로 맞는지 확인했다.

이번 감사:
  앞으로 새 서류를 받으려면 팩스, 이메일, 등기, 담당자 연락처가 실제로 연결되어 있는지 확인한다.

지금은 DART/KIND/KRX/CompanyGuide 쪽 통로는 있지만,
IR/TrustedNews는 "준비 안 됨" 응답만 내고,
리포트 PDF/회사 newsroom/Naver/general web은 production connector registry에 통로가 없다.
```

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_report_generated_from_leaf_audit -v
```

결과:

```text
Ran 17 tests in 35.682s
OK
```

추가 전체 Census v4 검증:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
```

결과:

```text
Ran 139 tests in 78.382s
OK
```

추가 전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5122 tests in 235.838s
OK
```

검증된 내용:

```text
source_connector_capability_audit.json 파일 존재
IssuerIR/TrustedNews placeholder 감지
ReportPDF/CompanyNewsroom 미등록 감지
SOURCE_CONNECTOR_CAPABILITY_PASS가 pending gate로 들어감
source_connector_capability_pending이 goal_completion blocker로 들어감
readiness remaining_operational_gaps에 source capability gap 표시
```

## 남은 일

이번 패치는 "실제 운영 source 수집을 성공시킨 패치"가 아니다.

남은 작업:

```text
1. IssuerIR connector를 placeholder가 아닌 실제 issuer IR/source discovery로 교체
2. TrustedNews를 일반 검색 synonym이 아니라 trusted full-source fetch provider로 구현
3. ReportPDF/BrokerReportPublicPDF connector를 production registry에 연결
4. CompanyNewsroom connector를 issuer official domain registry + as_of_date 검증으로 연결
5. NaverSearch/GeneralWebSearch는 production daily에서 bounded SourceTask로만 연결
6. 연결 후에도 accepted claim -> ScoreContribution -> StageCourt -> FULL_THESIS row까지 닫아야 함
```

중요:

```text
이 패치로 운영 Stage가 생긴 것은 아니다.
오히려 운영 Stage가 아직 생기면 안 되는 이유가 더 명확해졌다.
```

## 최종 판정

현재 상태:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS = true
SOURCE_CONNECTOR_CAPABILITY_PASS = false
MEANINGFUL_OPERATIONAL_STAGE_PASS = false
READY_FOR_FULL_THESIS_OPERATION = false
```

다음 에이전트가 이 패치를 공격하려면 아래를 확인하면 된다.

```text
1. source_connector_capability_audit.json이 실제로 생성되는가?
2. placeholder connector가 PASS로 계산되지 않는가?
3. missing connector source class가 goal blocker로 남는가?
4. DART/KIND/KRX/CompanyGuide의 static implemented 상태를 live fetch success로 과장하지 않는가?
5. FULL_THESIS row가 생기지 않았는데 운영 ready라고 하지 않는가?
```

현재 답은 모두 방어 가능하다.

다만 이 방어는 "운영 Stage가 있다"는 방어가 아니다. 정확한 방어는 아래다.

```text
Stage row 자체는 존재한다.
하지만 FULL_THESIS/FULL_E2R 운영 Stage는 아직 없다.
그리고 source connector capability gate가 그 상태를 READY로 과장하지 못하게 막는다.
```
