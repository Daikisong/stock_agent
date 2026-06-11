# E2R V12 Rolling Calibration Architecture

이 문서는 `docs/round`에 쌓이는 v12 연구 MD가 실제 점수체계와 Stage 판정까지 어떻게 연결되는지 고정한 운영 문서다.

핵심 결론은 단순하다.

```text
연구 MD를 쌓기만 하는 구조가 아니다.
run-v12-calibration 한 번으로 검증, 중복제거, 전이분석, 패치생성, 아키타입별 점수비중 갱신, E2R 2.2 active profile 반영까지 간다.
```

현재 기본 active profile은 다음과 같다.

```text
configs/e2r_scoring_profile_active.yaml
active_profile: e2r_2_2
rollback_profile: calibrated
```

따라서 v12의 표준 작업 명령은 이것이다.

```bash
PYTHONPATH=src python -m e2r.calibration.cli run-v12-calibration \
  --md-input-root docs/round \
  --data-directory data/e2r/calibration/v12 \
  --report-directory reports/e2r_calibration/v12
```

`run-v12-full`은 감사용 진단 명령이다. 기본 점수체계에 반영하려면 `run-v12-calibration`을 사용한다.

새 연구 케이스를 고르기 전에는 다음 문서를 함께 본다.

```text
docs/core/V12_Research_No_Repeat_Index.md
```

이 문서는 이미 쌓인 v12 corpus에서 같은 `canonical_archetype_id + symbol + trigger_type + entry_date`가 반복되는지 확인하는 장부다.
예를 들어 `C20 / 257720 / Stage3-Green / 2024-05-10`이 이미 여러 번 들어왔다면, 다음 연구는 같은 조합을 반복하지 말고 새 종목, 새 trigger family, 반례, 4B/4C, 또는 증거 URL 보강으로 가야 한다.

## Preflight Gate

`docs/round`에는 연구 결과 MD뿐 아니라 prompt txt, 과거 archive, 중복 파일이 같이 들어올 수 있다.
그래서 표준 실행 전에 입력을 먼저 점검한다.

```text
root 새 MD
archive MD
prompt/spec 파일
parser 실패 문서
trigger 없는 문서
unknown large sector
unknown canonical archetype
```

이 중 가장 위험한 것은 `unknown canonical archetype`이다.

```text
예:
  C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY 연구자료가 들어왔다.
  그런데 runtime profile에는 C08 weight가 없다.

그냥 진행하면:
  rolling scoring은 ArchetypeClassificationError로 중단된다.
  C08 전용 "고객 인증/품질/반복 소모품" 특성이 없으면 점수를 만들지 않는다.

올바른 처리:
  1. agent/research layer가 검색, 공시, 리포트 텍스트로 C08이 맞는지 먼저 판별한다.
  2. C08이 맞고 weight seed가 없으면 C08 seed를 추가한다.
  3. 테스트로 canonical match를 확인하고 전체 v12 calibration을 실행한다.
```

runtime scoring에서 대섹터 fallback은 허용하지 않는다.
분류가 빠졌으면 에이전트가 검색/LLM/파싱 텍스트로 L/C를 확정한 뒤 scoring으로 넘겨야 한다.
직접 scorer를 우회 호출한 payload만 예외로 막는다.

## 전체 흐름

```mermaid
flowchart TD
    A[docs/round v12 research MD] --> B[md_discovery.py<br/>파일 발견과 schema 분류]
    B --> C[md_parser.py<br/>metadata, case, trigger, table 파싱]
    C --> D[validation.py<br/>가격경로, 증거, sector/archetype 검증]
    D --> E[dedupe.py<br/>동일 symbol/entry 중복 제거]
    E --> F[aggregate.py<br/>대섹터, archetype, trigger 통계]
    E --> G[transition.py<br/>Stage2, Green, 4B, 4C 전이 요약]
    F --> H[v12_shadow.py<br/>rolling calibration ledger 생성]
    G --> H
    H --> I[v12_promotion_planner.py<br/>apply, hold, block 결정]
    I --> J[data/e2r/calibration/v12/v12_patch_specs.jsonl]
    J --> K[v12_apply.py<br/>safe patch만 runtime profile로 변환]
    F --> W[archetype_weight_profile.py<br/>아키타입별 점수비중 + 가격경로 support]
    G --> W
    W --> X[configs/e2r_archetype_weight_profile_v2_2.json]
    K --> L[configs/e2r_scoring_profile_v2_2.yaml]
    K --> M[configs/e2r_scoring_profile_active.yaml<br/>active_profile: e2r_2_2]
    L --> N[scoring_profile.py<br/>active profile loader]
    X --> O
    M --> N
    N --> O[scoring.py<br/>DeterministicScorer<br/>archetype weighted total]
    O --> P[staging.py<br/>StageClassifier]
```

예를 들어 `C22_INSURANCE_RATE_CYCLE_RESERVE` 연구가 들어오면 바로 Stage 기준 전체를 낮추는 게 아니다.

```text
1. 파일명과 metadata에서 C22 archetype을 읽는다.
2. trigger row가 검증을 통과한다.
3. 같은 symbol, 같은 entry의 반복 row는 대표 1개로 줄인다.
4. C22의 성공/반례/4B/4C 전이를 집계한다.
5. apply_next_patch로 판정된 축만 v2.2 profile에 들어간다.
6. 실제 런타임 payload에 canonical_archetype_id=C22...가 붙고 비가격 증거가 있을 때만 보정이 작동한다.
```

## 코드 호출 지도

| 단계 | 코드 | 입력 | 출력 |
|---|---|---|---|
| 명령 | `src/e2r/calibration/cli.py` | CLI 인자 | 전체 파이프라인 실행 |
| 발견 | `md_discovery.py` | `docs/round/**/*.md` | `MarkdownDocument` 목록 |
| 파싱 | `md_parser.py` | v12 MD | raw case, trigger, residual row |
| 검증 | `validation.py` | raw trigger rows | validated rows, rejected rows |
| 중복제거 | `dedupe.py` | validated rows | representative rows |
| 집계 | `aggregate.py` | representative rows | sector/archetype metrics |
| 전이 | `transition.py` | representative rows | stage transition summary |
| 후보장부 | `v12_shadow.py` | metrics, transitions | rolling ledger, candidate profile |
| 패치결정 | `v12_promotion_planner.py` | candidate rows | promotion decisions, patch specs |
| 반영 | `v12_apply.py` | patch specs | v2.2 profile, active profile |
| 아키타입 점수비중 | `archetype_weight_profile.py` | v12 aggregate metrics, transition support | `configs/e2r_archetype_weight_profile_v2_2.json` |
| 런타임 로드 | `scoring_profile.py` | active yaml | active `ScoringProfile` |
| 점수 | `scoring.py` | `ScoringPayload` | 아키타입별 weighted total이 반영된 `ScoreSnapshot` |
| Stage | `staging.py` | `ScoreSnapshot`, RedTeam | weighted component gate가 반영된 `StageSnapshot` |

## 데이터 산출물

`run-v12-calibration`은 다음 파일을 만든다.

| 파일 | 의미 |
|---|---|
| `data/e2r/calibration/v12/v12_md_registry.jsonl` | 어떤 v12 MD를 읽었는지 |
| `data/e2r/calibration/v12/v12_extracted_triggers_raw.jsonl` | 파싱된 원본 trigger row |
| `data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl` | 검증 통과 row |
| `data/e2r/calibration/v12/rejected_v12_rows.jsonl` | 탈락 row와 이유 |
| `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` | 중복제거 후 대표 row |
| `data/e2r/calibration/v12/v12_aggregate_metrics.json` | 대섹터와 archetype별 통계 |
| `data/e2r/calibration/v12/stage_transition_summary.jsonl` | Stage2, Green, 4B, 4C 전이 요약 |
| `data/e2r/calibration/v12/v12_promotion_decisions.jsonl` | apply, hold, block 판정 |
| `data/e2r/calibration/v12/v12_patch_specs.jsonl` | 실제 적용 가능한 safe patch |
| `configs/e2r_scoring_profile_v2_2.yaml` | E2R 2.2 rolling runtime profile |
| `configs/e2r_archetype_weight_profile_v2_2.json` | 아키타입별 runtime 점수비중 profile |
| `configs/e2r_scoring_profile_active.yaml` | active profile 선택 |

보고서는 다음 위치에 쌓인다.

```text
reports/e2r_calibration/v12/
```

가장 먼저 볼 파일은 다음 다섯 개다.

```text
ingest_summary.md
apply_next_patch_plan.md
rolling_calibration_apply_report.md
blocked_axes_report.md
archetype_weight_runtime_report.md
```

## Archetype Weight Runtime

v12의 핵심 변경은 이제 safe patch만이 아니다. `canonical_archetype_id`별로 점수비중도 달라진다.

```text
기존:
  모든 archetype이 EPS/FCF 20, visibility 20, bottleneck 20, mispricing 15, valuation 15, capital 5, info 5를 사용

현재:
  C20 K-food/K-beauty는 export/channel/repeat demand/OPM/EPS revision 비중을 크게 본다.
  C03 Defense/Grid는 계약, 정부 고객, 수주잔고, 납품 visibility를 크게 본다.
  C22 Insurance는 ROE/PBR, reserve/rate cycle, 자본환원을 크게 본다.
```

런타임 계산 방식은 이렇다.

```text
1. Feature Engineering이 기존 7개 component score를 만든다.
2. ScoringPayload에 canonical_archetype_id 또는 large_sector_id가 붙는다.
3. scoring.py가 configs/e2r_archetype_weight_profile_v2_2.json에서 해당 weight를 찾는다.
4. 각 component를 "raw score / 기존 max * archetype weight"로 다시 합산한다.
5. StageClassifier는 weighted component gate를 본다.
```

쉬운 예시는 다음과 같다.

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  계약공시가 없어도 수출 증가, 채널 확장, 반복수요, OPM, EPS revision이 있으면 visibility/total 기여가 커진다.

C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  계약금액, 수주잔고, 정부 고객, 납품 visibility가 약하면 Stage 3 쪽으로 쉽게 못 간다.

C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
  단순 HBM 장비 CAPEX보다 고객 인증, 품질 lock-in, 반복 소모품 수요, 매출 전환, 마진 지속성을 더 본다.
```

중요한 제한:

```text
과거 가격경로는 weight를 보정하는 근거다.
실전 runtime 판단에는 as_of_date 당시 보이는 가격과 증거만 쓴다.
미래 MFE/MAE/peak는 그날 점수에 직접 들어가지 않는다.
```

## Patch Decision

v12 row는 바로 점수로 들어가지 않는다. 반드시 `v12_promotion_planner.py`에서 네 가지 중 하나로 분류된다.

| decision | 의미 | 다음 행동 |
|---|---|---|
| `apply_next_patch` | 지금 적용 가능한 작은 패치 | `v12_patch_specs.jsonl`에 기록 후 v2.2 profile 반영 |
| `hold_for_more_evidence` | 근거 수가 아직 부족 | 해당 sector/archetype 연구 추가 |
| `blocked_by_data_quality` | URL, source proxy, 가격경로 등 데이터 품질 문제 | 증거 URL, 가격, as-of 근거 보강 |
| `blocked_by_logic_risk` | E2R 철학상 위험 | Green 제한, RedTeam guard 강화 |

예시는 이렇다.

```text
C20 K뷰티 positive가 많지만 source proxy가 높다.
-> hold 또는 blocked_by_data_quality.

C22 보험은 positive/counterexample 균형과 전이 경로가 충분하다.
-> apply_next_patch.

price-only 테마 급등 row가 많다.
-> Stage2 보너스가 아니라 local_4b_watch_guard 또는 Green 차단 guard.
```

## Patch Axis

현재 v2.2에 들어갈 수 있는 safe axis는 여섯 개다.

| axis | 런타임 의미 |
|---|---|
| `stage2_bonus_candidate_delta` | 해당 scope에서 비가격 증거가 있을 때 Stage2 근처에 최대 +1 |
| `stage2_required_bridge` | 해당 scope에서 Stage2가 되려면 비가격 bridge 필요 |
| `local_4b_watch_guard` | price-only blowoff는 positive Stage 또는 full 4B로 올리지 않음 |
| `full_4b_overlay_candidate` | full 4B는 비가격 증거가 있어야 인정 |
| `earlier_thesis_break_watch` | hard 4C 전 단계의 thesis-break watch 강화 |
| `hard_4c_confirmation` | 비가격 thesis-break 확인 시 4C 판정 강화 |
| `archetype_weight_runtime` | archetype별 점수비중을 total score와 Stage gate에 반영 |

Stage 3-Green 기준은 v12에서 낮추지 않는다.

```text
Green을 쉽게 만들기 위한 패치가 아니라,
Stage2/Yellow 관찰을 더 빨리 잡고
4B/4C와 가격만 오른 false positive를 더 잘 막는 패치다.
```

## Runtime Scoring Flow

```mermaid
sequenceDiagram
    participant FE as Feature Engineering
    participant S as DeterministicScorer
    participant P as ScoringProfile
    participant C as StageClassifier
    FE->>S: ScoringPayload(symbol, components, diagnostics, large_sector_id, canonical_archetype_id)
    S->>P: get_active_scoring_profile()
    P-->>S: e2r_2_2_rolling_calibrated
    S->>S: scope label 생성<br/>large_sector:L5..., canonical_archetype:C20...
    S->>S: archetype weight profile 조회<br/>raw component를 weighted component로 재합산
    S->>S: L/C 분류 없거나 unknown이면 예외로 중단
    S->>S: scope가 profile에 있고 비가격 증거가 있으면 bounded bonus/diagnostic flag 적용
    S-->>C: ScoreSnapshot(total_score, diagnostic_scores with weighted components)
    C->>P: active thresholds and guardrails 조회
    C->>C: weighted component gate, price-only guard, Stage2 bridge, 4B/4C guard 확인
    C-->>FE: StageSnapshot
```

중요한 연결 조건은 `large_sector_id`와 `canonical_archetype_id`다.

```text
payload에 canonical_archetype_id가 없으면 C20, C22 같은 scope patch가 작동할 수 없다.
```

rolling scoring은 fallback을 조용히 숨기지 않는다. 표준 흐름에서는 agent/feature pipeline이 먼저
분류 오류를 리서치로 보강해 L/C를 확정하고, 그 다음 rolling score를 만든다. 단, 이미 만들어진
`ScoringPayload`가 L/C 없이 scorer로 직접 들어오면 계산하지 않고 예외로 막는다.

| 직접 scorer 오류 조건 | agent pipeline의 올바른 처리 |
|---|---|
| missing `large_sector_id` | 검색/리포트/공시 텍스트로 L1~L10을 판별한 뒤 scoring |
| missing `canonical_archetype_id` | C01~C32 또는 R13 archetype을 판별한 뒤 scoring |
| unknown canonical archetype | 입력값을 그대로 쓰지 말고 agent mapper가 다시 분류, seed가 없으면 보강 |
| unknown large sector | 지원 taxonomy로 다시 매핑 |
| L/C mismatch | canonical 또는 evidence 기준으로 L/C를 정정 |

쉬운 예시는 이렇다.

```text
raw input A:
  canonical_archetype_id 없음
  large_sector_id 없음

결과:
  agent가 먼저 리서치한다.
  예: 전력기기 + 수주잔고 + 리드타임이면 C02로 분류하고 C02 weight로 score를 만든다.

의미:
  모른다고 기본형으로 계산하지 않는다. 먼저 판별하고 계산한다.
```

```text
raw input B:
  canonical_archetype_id = UNKNOWN_ARCHETYPE
  large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION

결과:
  UNKNOWN_ARCHETYPE은 버리고, K-food/K-beauty/브랜드/재고 증거를 다시 본다.
  글로벌 유통 반복수요면 C20, 재고/마진 문제면 C19, 수출채널 재주문이면 C18로 보낸다.

의미:
  L5 weight로 내려가는 게 아니라 agent가 세부 archetype을 판정한다.
```

쉬운 예시는 이렇다.

```text
payload A:
  canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
  evidence_family_financial_actual = 1
  evidence_family_disclosure = 1
  eps_fcf_explosion >= Stage2 기준

결과:
  C22 Stage2 bonus scope가 있으면 최대 +1이 붙을 수 있다.

payload B:
  canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
  price_only_blowoff_score = 80
  비가격 증거 없음

결과:
  +1 보너스 없음.
  Stage2/Stage3 positive 승격도 price-only guard에 막힌다.
```

## Safety Rules

이 파이프라인이 절대 하지 않는 것:

```text
종목명 하드코딩
benchmark label을 scoring input으로 사용
case library를 후보 생성 input으로 사용
Stage 3-Green 전역 기준 완화
미래 데이터 사용
가격만 오른 row를 Green이나 full 4B로 승격
투자 권고 문구 출력
자동매매 또는 증권사 API 연결
```

v12 적용은 scope 제한이다.

```text
전역 Stage2 기준을 낮추는 것이 아니다.
특정 대섹터 또는 archetype에 대해,
검증된 증거 조건이 맞을 때만 작은 보정, guard, archetype-specific weight가 작동한다.
```

## 운영 Cadence

연구와 점수반영은 분리하지 않는다. 한 배치가 들어오면 바로 다음 순서로 돈다.

```text
1. 새 v12 MD를 docs/round에 추가한다.
2. run-v12-calibration을 실행한다.
3. apply_next_patch_plan.md에서 적용된 patch를 확인한다.
4. rolling_calibration_apply_report.md에서 active profile 변경을 확인한다.
5. blocked_axes_report.md에서 다음 연구가 필요한 곳만 본다.
6. 새 연구가 들어오면 같은 명령을 다시 실행한다.
```

이 구조에서는 “계속 쌓기만 하는 것”이 아니다.

```text
새 연구가 safe patch gate를 통과하면 바로 v2.2 profile에 들어간다.
통과하지 못하면 그 이유가 blocked_axes_report.md에 남는다.
```

## 현재 배치 상태

최근 실행 기준:

```text
v12_result_md_count: 373
v12_validated_trigger_rows: 2988
v12_representative_trigger_rows: 2416
stage_transition_summary_rows: 1990
large_sectors_covered: 10
canonical_archetypes_covered: 36
applied_patch_count: 52
archetype_weight_count: 36
large_sector_weight_count: 10
active_profile: e2r_2_2
rollback_profile: calibrated
```

적용 축:

```text
stage2_required_bridge: 36
local_4b_watch_guard: 13
earlier_thesis_break_watch: 2
hard_4c_confirmation: 1
```

## Naming Note

일부 내부 파일명에는 과거 호환 때문에 `shadow`가 남아 있다.

```text
sector_shadow_profile.json
archetype_shadow_profile.json
v12_shadow_weight_candidates.jsonl
```

하지만 현재 사용자-facing 의미는 passive shadow가 아니다.

```text
이 파일들은 rolling calibration ledger다.
run-v12-calibration은 이 장부에서 apply_next_patch를 뽑아 active E2R 2.2 profile에 실제 반영한다.
```

나중에 파일명까지 바꾸려면 migration이 필요하다. 현재는 기존 테스트와 산출물 호환을 위해 내부 파일명을 유지하고, 문서와 보고서의 의미를 rolling calibration으로 고정한다.

## Verification Checklist

문서나 파이프라인을 바꾼 뒤 최소 확인:

```bash
PYTHONPATH=src python -m unittest tests.test_calibration_v12_pipeline -v
PYTHONPATH=src python -m unittest tests.test_calibration_pipeline -v
PYTHONPATH=src python -m compileall -q src tests
git diff --check
```

코드 로직을 바꿨다면 전체 테스트도 실행한다.

```bash
PYTHONPATH=src python -m pytest
PYTHONPATH=src python -m unittest discover -s tests -v
```
