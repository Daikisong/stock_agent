# E2R Reconstruction Phase 8 — Source Acquisition와 Document Selection

## 판정

`SOURCE_ACQUISITION_CONTRACT_PASS`

Phase 7의 `QuestionSourceTask`를 실제 문서 후보와 연결하는 mode-aware acquisition 계약을 만들었다. 검색 결과를 찾았다는 사실과 점수에 쓸 수 있는 문서를 확보했다는 사실을 분리했고, `EvidenceRecipe`가 요구하는 문서 종류·최신성·section을 통과한 문서만 canonical `AcquiredDocument`가 된다.

이 판정은 fixture/contract test 범위다. 실제 live provider 성공이나 Phase 9 claim 검증은 아직 증명하지 않았으므로 `production_runtime_ready=false`다. `AcquiredDocument.runtime_score_eligible`도 항상 false다.

## 왜 별도 acquisition 계약이 필요한가

이전 경로에는 문서 날짜가 없을 때 실행 기준일을 문서 날짜처럼 넣는 호환 fallback이 있었다. 예를 들어 문서의 실제 공개일을 모르는데 `as_of_date=2025-03-31`이라고 해서 `published_at=2025-03-31`로 취급하면, 그 문서가 당시 정말 공개돼 있었는지 알 수 없다.

새 canonical adapter는 이 fallback provenance를 읽으면 날짜를 다시 unknown으로 복원하고 `UNKNOWN_DATE`로 거절한다. legacy V4 runner는 당장 제거하지 않고 adapter 입력으로 남겨 rollback이 가능하게 했다.

## 네 가지 모드

| 모드 | 허용하는 실행 | 점수 의미 |
|---|---|---|
| `PRODUCTION_BOUNDED` | real-provider QuestionSourceTask와 live non-snapshot fetch만 허용 | acquisition 자체는 점수 없음 |
| `HISTORICAL_REPLAY` | 기준일 당시 고정된 snapshot만 허용 | real fetch로 세지 않음 |
| `SOURCE_REPAIR_BACKFILL` | 누락 URL·문서·anchor 수리용 | source repair only |
| `CONTROLLED_SMOKE` | fixture와 contract 검증용 | test only |

쉬운 예: 과거 broker PDF fixture를 다시 읽는 것은 `HISTORICAL_REPLAY`다. 파일을 실제로 읽었다고 해서 오늘 broker 사이트에서 새로 받은 live fetch로 세지 않는다. 반대로 오늘 production connector가 받은 문서를 historical snapshot이라고 다시 라벨링하는 것도 금지한다.

## official-first 실행 순서

engine은 task의 preferred/fallback source를 먼저 시도한다. 문서를 얻지 못하면 `NO_CANDIDATES:DART` 또는 `CONNECTOR_NOT_CONFIGURED:IssuerIR`처럼 source gap을 남긴 다음에만 discovery source를 실행한다.

```text
DART / KIND / KRX / Issuer IR
  → public report / industry / TrustedNews
  → NaverSearch / GeneralWebSearch discovery
```

공식 문서가 recipe에 맞게 선택되면 Naver discovery는 실행하지 않는다. connector가 `max_queries`, `max_candidates`, `max_fetches` 중 하나라도 남은 budget을 넘기면 반환 문서를 채택하지 않고 `OUTSIDE_BUDGET`으로 격리한다.

connector 이름·provider·source family·fake/live·discovery flag도 반환 batch와 일치해야 한다. 예를 들어 실행 route는 `DART`인데 후보가 `NaverSearch → TrustedNews` provenance를 달고 오면 공식 문서처럼 가장할 수 없고 source mismatch로 거절된다. `NaverSearch`나 `GeneralWebSearch` connector를 main source로 잘못 설정해도 engine이 실행하지 않는다.

## 검색 결과와 문서의 경계

snippet은 문서가 아니다. Naver/Web 결과의 제목·snippet·URL은 원문을 발견하는 데만 쓴다. 후보 하나는 반드시 다음 둘 중 하나로 끝난다.

1. 원 출처 URL의 전체 본문을 fetch하고 날짜·대상 회사·SHA-256 hash를 확인한 `AcquiredDocument`
2. 이유가 붙은 `DocumentRejection`

예를 들어 네이버 재게시 URL만 있고 언론사 원문 URL을 확인하지 못하면 `REPOST_WITHOUT_ORIGINAL`이다. 원문 URL은 찾았지만 본문 fetch가 실패하면 `FULL_FETCH_FAILED`다. 제목에는 대상 회사가 있지만 원문 전체가 다른 회사를 설명하면 `WRONG_SUBJECT`다. snippet 텍스트를 `full_text` 자리에 복사해 통과시키는 경로는 없다.

## 문서 preselection guard

다음 후보는 recipe selector에 들어가기 전에 차단한다.

- source-backed `published_at` 또는 `available_at`이 없음: `UNKNOWN_DATE`
- 기준일 이후 공개 또는 이용 가능: `FUTURE_DATE`
- 전체 본문 fetch 없음: `SNIPPET_ONLY`
- 본문 SHA-256 없음 또는 불일치: `NO_CONTENT_HASH`, `CONTENT_HASH_MISMATCH`
- 원 출처 검증 없음: `REPOST_WITHOUT_ORIGINAL`
- 대상 회사 직접 문서가 아님: `WRONG_SUBJECT`
- production에서 snapshot/fake/report replay 사용: `SNAPSHOT_AS_LIVE`, `FAKE_PROVIDER_IN_PRODUCTION`, `REPORT_REPLAY_NOT_REAL_FETCH`
- historical replay에 live/non-snapshot 입력: `LIVE_RESULT_IN_HISTORICAL_REPLAY`, `NON_SNAPSHOT_IN_HISTORICAL_REPLAY`

provider exception과 fetch 실패는 빈 결과로 숨기지 않는다. 선택 문서가 없으면 `PROVIDER_FAILED`, 일부 문서가 있어도 provider error가 있으면 `PARTIAL`로 남는다.

## EvidenceRecipe 기반 document selection

preselection을 통과한 문서도 바로 채택하지 않는다. `RecipeDocumentSelector`가 다음을 확인한다.

- task/recipe ID 연결
- QuestionSourceTask와 EvidenceRecipe가 공통으로 허용한 document type·section
- source family와 document type의 조합
- recipe가 허용한 document type
- `freshness_max_age_days`
- recipe preferred section과 실제 본문의 일치

예를 들어 `DART` source가 `full_article`을 만들었다고 주장하면 source/document mismatch다. recipe는 공시와 뉴스를 모두 허용하더라도 이번 QuestionSourceTask가 공시만 요구하면 뉴스는 선택하지 않는다. `NaverSearch` 같은 검색 provider family도 원문 source family인 것처럼 가장할 수 없다. 오래된 broker PDF가 recipe의 최신성 상한을 넘으면 `STALE_DOCUMENT`다. 계약 recipe인데 본문에 계약·allocation·capacity 관련 section이 하나도 없으면 `RECIPE_SECTION_MISSING`이다.

선택된 section은 문서 전체 hash와 별도로 section text hash 및 matched recipe section을 가진다. 따라서 다음 단계는 “어느 문서의 어느 부분을 왜 읽었는지”를 되짚을 수 있다.

## V4 migration adapter

기존 `SourceAcquisitionRunnerV4`는 현재 CLI rollback을 위해 보존했다. 새 adapter는 다음을 수행한다.

- `IR`, `BrokerPDF`, `News` 같은 legacy source class를 canonical family로 정규화
- parser/provider의 snapshot provenance 보존
- stored report replay를 real fetch로 승격하지 않음
- legacy missing-date score-block reason을 읽어 as-of fallback 날짜를 unknown으로 복원
- canonical selector에서 다시 source/document/section 검증

즉, legacy 결과를 그대로 신뢰하지 않고 새 계약의 후보로만 바꾼다.

## 감사 결과

| 항목 | 결과 |
|---|---:|
| audit result | 4 |
| selected document | 3 |
| explicit rejection | 1 |
| Naver terminal candidate | 2 |
| snapshot-as-live | 0 |
| snippet-as-document | 0 |
| fetched without content hash | 0 |
| provider failure masked | 0 |
| source/document mismatch accepted | 0 |
| report replay counted real fetch | 0 |
| missing task/recipe link | 0 |
| Naver without full fetch or rejection | 0 |

고정 audit hash는 `cebcdea9ed8b1d0df34f5b30818ac6eeef2c4543ab921a59ebf3315e83d5b1bc`다.

## 검증 결과

- Phase 0~8 targeted chain: 150개 통과
- 기존 V4 source acquisition 회귀: 47개 통과
- full suite: 5,455개 실행, 기존 기준선과 동일한 18개 실패
- Phase 8 신규 실패: 0개

18개는 Phase 0부터 기록한 mutable goal4 research-to-runtime operational snapshot 불일치다. 이 실패를 통과로 숨기지 않으며 Phase 8 회귀로도 세지 않는다.

## 주요 파일

- `runtime/source_acquisition.py`: mode, connector, candidate/document/rejection/result schema, acquisition engine, V4 adapter, audit
- `runtime/document_selector.py`: source/document compatibility, freshness, recipe section selection
- `v4_source_acquisition_runner.py`: missing-date score-block provenance
- `tests/test_source_acquisition_document_selection.py`: mode와 hard safety 실행 검증
- `e2r_reconstruction_phase8_acceptance.json`: phase-scoped 고정 판정

## 다음 경계

Phase 8은 질문에 맞는 원문을 안전하게 확보하고 section을 골랐다. 아직 그 section이 계약 구속력이나 FCF를 실제로 증명하는 claim인지는 판단하지 않았다. Phase 9는 score·Stage·primitive gap을 보지 않는 contract-blind extractor로 anchor와 claim을 만들고, 원래 QuestionSourceTask가 정말 해결됐는지를 별도 ledger 상태로 기록한다.
