# E2R Live Materialization Forensic Baseline — Phase 17

## 결론

현재 canonical current/Census 경로의 첫 blocker는 외부 데이터가 아니라 `MISSING_INTERNAL_MATERIALIZER`다.

`run_e2r_current_operation`은 live provider preflight, KRX universe, Research Brain, Evidence OS를 호출하지 않는다. 완성된 `CurrentOperationRunnerInput` JSON을 찾은 뒤 pure evaluator를 실행하거나, 파일이 없으면 `CURRENT_KRX_UNIVERSE_AND_LIVE_SOURCE_INPUT_MANIFEST_UNAVAILABLE`로 exit 3을 반환한다. Census canonical CLI도 인자를 current CLI로 번역하므로 같은 단절을 공유한다.

쉬운 예: OpenDART 열쇠가 있는지 확인하기도 전에 완성된 조사 결과표가 책상 위에 없다는 이유로 퇴근하는 구조다. 따라서 지금 단계에서 모든 문제를 `EXTERNAL_PROVIDER_BLOCKER`라고 부르면 안 된다.

## 감사 기준

- 기준 commit: `c385ee5`
- 감사일: `2026-07-11 KST`
- 변경 전 경로: `src/e2r/cli/run_e2r_current_operation.py`, `src/e2r/cli/run_e2r_census_mode.py`
- pure evaluator: `src/e2r/research_brain/runtime/current_operation_runner.py`
- 별도 legacy/live-lite 경로: `src/e2r/pipeline/korea_live_lite.py`
- source connector: `src/e2r/production/source_connectors/`, `src/e2r/sources/`

이 문서는 report summary를 믿고 만든 결과가 아니다. 아래 함수와 dataclass를 직접 읽어 연결 여부를 판정했다.

## 1. Canonical CLI는 manifest를 어디서 찾는가

`run_e2r_current_operation._resolve_default_input_manifest`의 검색 순서는 다음과 같다.

1. `--input-manifest <path>`
2. `output/current_operation_inputs/<AS_OF_DATE>.json`
3. `data/current_operation/<AS_OF_DATE>.json`

어느 파일도 없으면 provider나 materializer를 호출하지 않는다.

## 2. Manifest 부재 시 exit 3을 만드는 함수

호출 사슬은 다음과 같다.

```text
run_e2r_current_operation.main
→ _resolve_default_input_manifest
→ None
→ write_current_source_pending_run
→ Stage 0 / score_valid=false / exit 3
```

`run_e2r_census_mode.main`은 canonical 모드에서 current CLI 인자로 번역한 뒤 `run_current_operation_main`을 호출한다. 따라서 Census에도 독립 live materializer가 없다.

## 3. CurrentOperationRunnerInput 필드별 현재 생산자

| 필드 | 현재 생산 가능 코드 | canonical live 연결 | 판정 |
|---|---|---:|---|
| `as_of_date` | CLI/manifest loader | manifest에서만 읽음 | 수동 입력 의존 |
| `universe` | Census adapter, fixture/test builder | 없음 | 내부 materializer 누락 |
| `baseline_lanes` | `canonical_current_adapter` | 없음 | legacy snapshot adapter만 존재 |
| `triggers` | Census adapter/current dataclass | 없음 | live fusion 누락 |
| `claims` | claim compiler/atomic runtime 타입 | 없음 | orchestration 누락 |
| `claim_provenance` | strict dataclass/validator | 없음 | live compiler 연결 누락 |
| `source_tasks` | two-pass planner/QuestionSourceTask | 없음 | manifest bridge 누락 |
| `atomic_decisions` | deterministic atomic runtime | 없음 | live input builder 누락 |
| `deep_executions` | current runner contract/test | 없음 | orchestrator 누락 |
| `config` | manifest/test builder | 없음 | run profile loader 누락 |

`canonical_current_adapter.adapt_census_snapshot_to_current_input`은 기존 Census leaf를 one-way 변환할 수 있지만 live I/O를 하지 않고 source task도 빈 tuple로 둔다. 최종 live materializer의 대체물이 아니다.

## 4. KoreaLiveLite 재사용/격리 판정

재사용 가능:

- `load_project_env`와 credential 비노출 방식
- `HttpClient`, `RateLimiter`, cache 통계
- OpenDART detail fetch와 structured normalizer
- KRX OpenAPI request metadata와 fixture parser
- CompanyGuide symbol request/parser
- Naver search transport와 full-page fetcher
- agentic Evidence OS 구성요소

그대로 canonical path에 사용하면 안 되는 부분:

- `KoreaLiveLiteBudget`의 운영 cap 기본값이 다수 `None`인 legacy 연구/backfill 의미
- cheap-scan score threshold로 live depth를 고르는 결합 구조
- `naver_news.py`의 company/sector 고정 query template
- fixture credential fallback을 live 결과처럼 오인할 가능성
- `KoreaLiveLiteResult`가 `CurrentOperationRunnerInput`을 만들지 않는 점
- 기존 score/stage snapshot을 canonical atomic decision 대신 재사용하는 경로

따라서 KoreaLiveLite 전체를 호출하는 방식이 아니라 connector/client/cache/rate-limit 단위를 adapter로 재사용해야 한다.

## 5. Provider별 실제 symbol-specific 여부

| Provider | 현재 live 동작 | symbol-specific score evidence 가능 여부 |
|---|---|---|
| OpenDART | corpCode → symbol disclosure list → document fetch | 부분 가능. bulk daily index/orchestration은 별도 필요 |
| KRX live connector | MDC main HTML 1회 | 불가. `PROVIDER_HEALTH_ONLY` |
| KIND live connector | KIND main HTML 1회 | 불가. `PROVIDER_HEALTH_ONLY` |
| CompanyGuide | `gicode=A<symbol>` company page와 consensus parse | 부분 가능. currentness/claim mapping 필요 |
| IssuerIR | 명시적 `PROVIDER_FAILED` placeholder | 불가 |
| TrustedNews | 명시적 `PROVIDER_FAILED` placeholder | 불가 |
| NaverSearch | LLM이 준 literal query를 실행 가능한 transport | discovery만 가능; snippet score 금지 |
| GeneralWebFetcher | URL full fetch 가능 | original/full document guard 뒤 가능 |

KRX/KIND 메인 페이지는 provider가 살아 있다는 health leaf로는 유용하지만 종목별 관찰값이 아니다.

쉬운 예: 병원 홈페이지가 열렸다는 사실은 특정 환자의 혈액검사 결과가 아니다.

## 6. Generic portal 오인 경로

`KRXLiveConnector.fetch`와 `KINDLiveConnector.fetch`는 현재 요청의 symbol을 structured payload에 넣지만 실제 응답은 모든 symbol에 동일한 메인 페이지다. `SourceFetchResult.counts_as_live`는 mode/status/content anchor만 보므로 이 결과를 live fetched document 수에 포함할 수 있다.

현재 payload에는 `score_usage=provider_coverage_only...`가 있지만 강제 타입이 아니다. 새 materializer에서는 `PROVIDER_HEALTH_ONLY` classification과 `symbol_evidence_allowed=false`를 구조적으로 강제해야 한다.

## 7. KRX current universe 기존 구현

`KRXConnector`에는 KRX OpenAPI의 issue base info와 daily trading request metadata, fixture normalizer가 있다. 그러나 canonical current CLI에서 실제 bulk HTTP 요청을 실행하고 KOSPI/KOSDAQ을 병합·제외·quarantine하는 materializer는 없다.

`KRXLiveConnector`의 MDC main fetch는 universe materialization이 아니다.

## 8. Naver/Web transport와 query generation 분리

canonical planning 모듈에는 두 단계 planner와 LLM literal query validation이 존재한다. `QuestionSourceTask`는 official-first, bounded budget, stop-on-resolution을 강제한다. `NaverSearchProvider`는 전달된 query를 실행하는 transport로 사용할 수 있다.

반면 `src/e2r/sources/naver_news.py`에는 deterministic company/sector query templates가 남아 있다. 이 template는 legacy 경로로 격리하고 canonical live path에서는 호출하지 않아야 한다.

## 9. Accepted claim → provenance → atomic decision 경로

각 독립 구성요소와 검증 타입은 이미 존재한다.

- `runtime/source_acquisition.py`: full document/source guard
- `runtime/claim_compiler.py`: claim/provenance compiler
- `runtime/atomic_score_stage.py`: deterministic atomic score/stage
- `current_operation_runner.py`: strict provenance/evaluator

그러나 이들을 현재 symbol/source task 기준으로 순서대로 호출하고 결과를 하나의 manifest에 넣는 canonical orchestration 함수가 없다.

## 10. Initial bootstrap과 daily incremental 분리

현재 canonical runtime에는 versioned `CurrentStateStore`가 없다. 기존 Census source timeline/last effective thesis와 current adapter는 snapshot leaf를 변환하지만, initial full-history bootstrap과 daily delta update를 별도 run mode/checkpoint로 관리하지 않는다.

## 11. 내부 blocker와 외부 blocker 분리

현재 확인된 내부 blocker:

- `MISSING_INTERNAL_MATERIALIZER`
- `UNIVERSE_MATERIALIZER_NOT_CALLED`
- `CURRENT_STATE_STORE_NOT_IMPLEMENTED`
- `LIVE_BASELINE_ORCHESTRATOR_NOT_IMPLEMENTED`
- `LIVE_TRIGGER_DEPTH_ORCHESTRATOR_NOT_IMPLEMENTED`
- `LIVE_PLANNER_ACQUISITION_BRIDGE_NOT_IMPLEMENTED`
- `LIVE_CLAIM_ATOMIC_MANIFEST_BUILDER_NOT_IMPLEMENTED`
- `LIVE_CENSUS_ORCHESTRATOR_NOT_IMPLEMENTED`

외부 blocker는 아직 canonical path에서 실제 호출되지 않았으므로 최종 판정할 수 없다. credential/provider/network blocker는 materializer preflight와 실제 bounded request leaf가 생긴 뒤에만 확정한다.

## Reuse / Adapter / Deprecate 결정

### 직접 재사용

- pure `CurrentOperationRunner`
- two-pass Research Brain과 `QuestionSourceTask`
- canonical source acquisition/claim compiler/atomic decision
- `load_project_env`, rate limiter, cache/checkpoint primitive
- OpenDART live document fetch
- Naver query transport와 page fetcher

### Adapter 필요

- KRX OpenAPI request/normalizer → bulk current universe/price materializer
- KIND fixture/request metadata → symbol risk batch adapter
- CompanyGuide page → current consensus provenance adapter
- Census source timeline/last effective thesis → versioned current state migration
- production source connector result → canonical `DocumentCandidate`

### Legacy 격리 또는 대체

- KRX/KIND generic portal fetch를 symbol evidence로 세는 connector 동작
- IssuerIR/TrustedNews placeholder connector
- deterministic Naver query template
- KoreaLiveLite의 monolithic score/stage orchestration
- manifest-only canonical production entrypoint

## Phase 17 완료 판정

- manifest-only production reachable path: 확인 완료
- `MISSING_INTERNAL_MATERIALIZER`와 provider blocker: 분리 완료
- 재사용 가능한 서비스: 확정
- adapter/deprecate 대상: 확정
- 다음 단계: Phase 18 authorization/run profile 계약과 live materializer 패키지 경계 구현
