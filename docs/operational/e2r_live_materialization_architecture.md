# E2R Bounded Live Materialization Architecture — Phase 18

## 목적

네트워크를 사용하지 않는 pure evaluator 앞에 별도 live materializer를 둔다.

```text
LiveMaterializer
→ CurrentOperationRunnerInput
→ pure CurrentOperationRunner
→ LiveOperationalRunEnvelope
```

쉬운 예: 조리실에서 재료를 씻고 계량하는 단계가 materializer이고, 정해진 레시피대로 맛과 안전을 판정하는 단계가 evaluator다. evaluator가 직접 시장 데이터를 다운로드하게 만들지 않는다.

## 실행 경계

| 경로 | 필요한 인자 | live I/O | 현재 Phase 18 결과 |
|---|---|---:|---|
| Manifest replay | `--input-manifest` | 없음 | 기존 pure evaluator 실행 |
| Authorized live | `--materialize-live-input true --live-materialization-authorized true --run-profile ...` | 향후 materializer에서 수행 | 내부 materializer 미완료를 exit 2로 명시 |
| Fail closed | 위 두 경로 모두 없음 | 없음 | 기존 Stage 0/source pending exit 3 |
| Rejected | live 요청/승인/profile 조합 오류 | 없음 | authorization blocker exit 2 |

승인된 live 요청이 manifest 부재라는 이유로 기존 external exit 3으로 떨어지는 경로는 제거했다. Phase 18에서는 아직 materializer가 없으므로 `MISSING_INTERNAL_MATERIALIZER`를 숨기지 않는다. Phase 31에서 이 분기를 실제 materializer 호출로 교체한다.

## Run modes

- `MANIFEST_REPLAY`: 동일 manifest deterministic evaluator 재생
- `LIVE_BOOTSTRAP`: KRX 전체 universe와 versioned CurrentStateStore 초기화
- `LIVE_DAILY_INCREMENTAL`: bootstrap 상태에 오늘 delta를 반영
- `LIVE_CENSUS_BASELINE`: 전체 universe baseline만 실행
- `LIVE_CENSUS_SELECTIVE_DEEP`: 전체 baseline 후 bounded L3~L5 실행
- `TARGETED_LIVE_SMOKE`: 명시된 validation 대상과 섹터 sample
- `TEST_FIXTURE`: transport fixture 전용, production label 금지

## Package boundary

```text
runtime/live_materialization/
├── authorization.py  # CLI authorization path만 결정, I/O 없음
├── schemas.py        # bounded run profile / operational envelope
├── provider_capabilities.py
├── credential_audit.py
├── universe_materializer.py
├── current_state_store.py
├── baseline_materializer.py
├── trigger_fusion.py
├── depth_selector.py
├── brain_planner_runner.py
├── source_task_builder.py
├── source_acquisition_runner.py
├── claim_compiler_runner.py
├── adaptive_closure_controller.py
├── atomic_decision_builder.py
├── current_input_manifest_builder.py
├── current_orchestrator.py
├── census_orchestrator.py
├── checkpoint_store.py
└── observability.py
```

Phase 18은 앞의 두 contract 파일을 구현한다. 이후 Phase는 같은 경계 안에 기능을 추가한다.

## Run profile contract

production profile은 다음 budget을 모두 양의 정수로 가진다.

- official-light target
- deep/Brain/acquisition candidate
- candidate별 LLM call/SourceTask/fetch/retry/general-web fetch
- 전체 runtime seconds

`None`이나 무제한 값은 허용하지 않는다. official-first와 general-web official-gap 조건도 profile validator가 강제한다.

현재 profile:

- `configs/e2r_current_bootstrap_v1.json`
- `configs/e2r_production_daily_v1.json`
- `configs/e2r_census_selective_deep_v1.json`

## Authorization invariants

1. input manifest와 live materialization을 동시에 지정하지 않는다.
2. live materialization flag만 켜고 authorization을 빼면 실행하지 않는다.
3. authorization만 켜고 materialization 요청을 빼도 실행하지 않는다.
4. production live에는 run profile이 필수다.
5. `TEST_FIXTURE`는 live authorization 및 production READY를 가질 수 없다.
6. authorization decision은 secret을 포함하지 않는다.

## Operational envelope

Pure evaluator result의 `production_runtime_ready=false` 안전 경계는 유지한다. 실제 운영 readiness는 별도 `LiveOperationalRunEnvelope`가 다음을 모두 확인한 뒤에만 연다.

- materializer/evaluator run ID
- source corpus/input manifest/evaluator leaf SHA-256
- actual live source와 fresh provider cache 수
- accepted current claim과 atomic decision 수
- provider blocker와 critical count

actual live source, accepted claim, atomic decision 중 하나라도 0이면 envelope가 READY overclaim을 거절한다.

## Phase 18 완료 상태

- pure evaluator/live materializer 경계: 타입과 문서로 고정
- manifest replay/live authorization/fail-closed/rejected 경로: 분리
- bounded production profiles: 추가
- authorized live 요청의 manifest-missing external exit 3: 차단
- 실제 materializer: 다음 Phase 구현 대상
