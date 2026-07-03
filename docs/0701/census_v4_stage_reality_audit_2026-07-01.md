# Census v4 Stage Reality Audit - 2026-07-01

이 문서는 질문 하나에 답하기 위한 감사 기록이다.

```text
뭔가 잘못되고 있는가?
Stage가 있는 종목이 있긴 한가?
```

## 짧은 답

```text
Stage가 있는 종목은 있다.
하지만 현재 v4의 Stage는 full E2R thesis Stage가 아니라 Census/event 상태판이다.
```

즉, 지금 산출물을 이렇게 읽으면 맞다.

```text
Stage0:
  이번 census에서 평가 대상에는 올렸지만 현재 catalyst claim이 없다.

Stage1:
  공식 이벤트나 일부 claim은 있어서 watch 대상이다.

Stage2-Watch:
  material claim은 있지만 cash/revision/multi-source 같은 full thesis bridge가 부족하다.

Red:
  risk review signal이 있지만 full thesis transition 4C 판정은 아니다.
```

이렇게 읽으면 틀리다.

```text
Stage1/Stage2-Watch/Red가 있으니
전 종목 full E2R 100점 thesis 평가가 끝났다.
```

## 검산 결과

재검산 명령:

```bash
python - <<'PY'
import json, pathlib, collections
p=pathlib.Path("output/census_v4/2026-07-01/census_stage_status.jsonl")
rows=[json.loads(line) for line in p.read_text().splitlines() if line.strip()]
print("rows", len(rows))
print("base_stage", dict(collections.Counter(r.get("base_stage") for r in rows)))
print("canonical_stage", dict(collections.Counter(r.get("canonical_stage") for r in rows)))
print("score_scale", dict(collections.Counter(r.get("score_scale") for r in rows)))
print("candidate_event_scope", dict(collections.Counter(r.get("candidate_event_scope") for r in rows)))
print("full_thesis_stage", dict(collections.Counter(r.get("full_thesis_stage") for r in rows)))
print("verified_score_present", sum(r.get("verified_score") is not None for r in rows))
print("full_e2r_verified_score_present", sum(r.get("full_e2r_verified_score") is not None for r in rows))
print("event_evidence_score_present", sum(r.get("event_evidence_score") is not None for r in rows))
audit=json.load(open("output/census_v4/2026-07-01/leaf_artifact_audit.json"))
print("sample_leaf_bundle_count", audit["metrics"].get("sample_leaf_bundle_count"))
promotion=json.load(open("output/census_v4/2026-07-01/brain_stage_promotion_audit.json"))
print("brain_stage_promotion_verdict", promotion.get("verdict"))
print("brain_stage_trace_count", promotion.get("brain_stage_trace_count"))
print("brain_promoted_stage_row_count", promotion.get("brain_promoted_stage_row_count"))
PY
```

관측값:

```text
rows: 3391

base_stage:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

canonical_stage:
  0:       3306
    1:         54
    2:         30
  3-Red:      1

score_scale:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

candidate_event_scope:
  ASSESSMENT_ONLY:          3306
  CANDIDATE_EVENTS_PRESENT:   85

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

verified_score_present: 0
full_e2r_verified_score_present: 0
event_evidence_score_present: 67
accepted_claim_count: 92
evidence_claim_payload_count: 92
sample_leaf_bundle_count: 67
planner_run_count: 0
web_search_task_count: 0
claim_extractor_run_count: 0
research_brain_bridge_verdict: SHADOW_OR_IMPORT_ONLY
brain_stage_promotion_verdict: NOT_REQUESTED
brain_web_readiness_gate_verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
brain_stage_trace_count: 0
brain_promoted_stage_row_count: 0
```

## 핵심 해석

`base_stage`와 `canonical_stage`는 다르다.

92개 claim payload는 67개 부분 이벤트 score row의 근거다.
Brain/Web live acquisition claim이나 full thesis claim이 아니다.
Brain StageCourt trace에서 승격된 대표 Stage row도 아니다.
Brain/Web readiness gate도 `NOT_REQUESTED`이므로 Brain/Web evidence pass가 아니다.

`census_stage_summary.json`의 legacy `stage_distribution` key는 base/display label 분포다.
canonical enum 분포는 `canonical_stage_distribution`을 봐야 한다.
새 산출물에는 같은 의미를 더 분명히 하는 `base_stage_distribution` alias도 함께 기록한다.

```text
base_stage
= 사람이 보는 표시 label

canonical_stage
= 프로젝트 canonical enum
```

쉬운 예:

```text
001470 삼부토건
  base_stage: Stage2-Watch
  canonical_stage: 2
  score_scale: EVENT_WEIGHTED_PARTIAL
  full_thesis_stage: FULL_THESIS_NOT_RUN

뜻:
  공급계약성 claim이 있어서 watch로 올라왔지만,
  full thesis 100점 평가가 끝난 것은 아니다.
```

```text
030350 드래곤플라이
  base_stage: Red
  canonical_stage: 3-Red
  score_scale: EVENT_WEIGHTED_PARTIAL
  full_thesis_stage: FULL_THESIS_NOT_RUN

뜻:
  risk review signal은 있지만,
  기존 thesis가 깨진 4C transition 판정은 아니다.
```

```text
005930 삼성전자 / 000660 SK하이닉스
  base_stage: Stage1
  canonical_stage: 1
  stage_signal: OFFICIAL_EVENT_WATCH
  event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN

뜻:
  daily event board에는 걸렸지만,
  HBM/C06 full thesis 점수와 Stage는 아직 산출되지 않았다.
```

## 지금 잘못될 수 있는 오해

### 오해 1. Stage2-Watch   30개면 Stage2 종목이 30개다

틀렸다.

```text
Stage2-Watch   30개
= candidate event 또는 material claim이 있고 material gap이 남은 watch row 30개
!= full E2R Stage2 확정 30개
```

### 오해 2. Red 1개면 운영상 3-Red/4C reject가 확정됐다

틀렸다.

현재 Red는 canonical enum으로는 `3-Red`에 매핑되지만, `full_thesis_stage=FULL_THESIS_NOT_RUN`이다.
따라서 아직 full thesis reject나 4C transition으로 읽으면 안 된다.

### 오해 3. 삼성전자/하이닉스 점수가 4점이다

틀렸다.

```text
event_evidence_score 4.0
= daily event board의 부분 이벤트 점수
!= full E2R 100점 verified score
```

100점 thesis 점수는 다음 필드가 있어야 한다.

```text
full_e2r_verified_score
full_thesis_verified_score
full_thesis_stage != FULL_THESIS_NOT_RUN
```

현재는 전부 없다.

## 교차검증된 방어막

leaf artifact audit:

```text
verdict: PASS
critical_count: 0
```

특히 아래 항목이 0이다.

```text
assessment_only_nonzero_score_count: 0
score_eligible_candidate_without_accepted_claim_count: 0
stage_trace_stage_mismatch_count: 0
stage_trace_score_interval_mismatch_count: 0
stage_trace_claim_set_mismatch_count: 0
stage_trace_contribution_set_mismatch_count: 0
verified_score_not_full_e2r_count: 0
canonical_stage_invalid_count: 0
canonical_stage_display_label_count: 0
stage_trace_canonical_stage_mismatch_count: 0
web_claimed_but_zero_search_count: 0
llm_claimed_but_zero_calls_count: 0
legacy_runner_production_reachable_count: 0
legacy_v3_runner_production_reachable_count: 0
empty_claims_stage_builder_production_count: 0
old_cli_can_claim_pass_count: 0
official_cli_not_v4_runner_count: 0
sample_bundle_missing_scored_row_count: 0
```

`sample_leaf_bundle.jsonl`은 부분 이벤트 점수가 붙은 row 67개를 빠르게 펼쳐 보기 위한 묶음이다.
이 묶음에 포함됐다는 뜻은 full thesis 점수가 있다는 뜻이 아니라,
점수/claim/trace가 붙은 row를 누락 없이 재검산할 수 있다는 뜻이다.

전체 테스트:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 4942 tests in 170.248s
OK
```

## 현재 v4가 실제로 보장하는 것

보장한다.

```text
전 종목에 CensusAssessmentEvent가 있다.
CandidateEvent와 CensusAssessmentEvent가 분리된다.
Assessment-only row에서 점수가 나오지 않는다.
claim 없는 score contribution이 없다.
event score와 full E2R verified score가 분리된다.
Brain/Web을 돌리지 않았으면 Brain/Web pass를 주장하지 않는다.
canonical_stage에 표시 label이 섞이지 않는다.
부분 점수 또는 claim-backed row가 sample_leaf_bundle에서 빠지지 않는다.
legacy v1 runner나 빈 claim builder가 production pass를 주장하지 못한다.
```

보장하지 않는다.

```text
전 종목 full thesis 점수가 있다.
Stage3-Green/Yellow/Red 운영 판정이 있다.
4A/4B/4C transition 판정이 있다.
삼성전자/하이닉스 HBM thesis 점수가 있다.
Research Brain/Web acquisition이 실제 운영 통과했다.
과거 연구자료 전체 replay parity가 검증됐다.
```

## 다음 패치 방향

다음 에이전트는 아래 순서로 봐야 한다.

### 1. Full thesis runner를 별도 경로로 닫기

현재 v4는 event board다.
다음 단계는 selected candidate에 대해 실제 `EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt` 경로를 돌려야 한다.

쉬운 예:

```text
삼성전자:
  지금은 "공식 이벤트 watch"까지만 있음.

다음에 필요한 것:
  HBM customer allocation, qualification, shipment/revenue mix,
  cash/revision bridge claim을 source-backed로 추출하고,
  full thesis score_scale=FULL_E2R_100으로 따로 계산.
```

### 2. Brain/Web enabled mode는 진짜 artifacts가 있어야 pass

지금 disabled run은 disabled honesty와 anti-fake 범위만 통과했다.
Brain/Web 실행 통과가 아니다.
enabled run에서 아래가 0이면 실패해야 한다.

```text
planner calls
web search tasks
fetched documents
extracted claims
source-backed anchors
```

### 3. Event score와 full thesis score를 계속 분리

절대 금지:

```text
event_evidence_score 4.0
-> verified_score 4.0으로 복사
-> "삼성전자 4점"이라고 출력
```

허용:

```text
event_evidence_score 4.0
-> daily event board용

full_e2r_verified_score
-> full thesis 경로가 끝났을 때만 생성
```

### 4. Red/4C를 분리

`Red` 표시 label은 risk review signal일 수 있다.
4C는 기존 thesis가 있었고, 현재 OPEN hard-break claim이 source quorum을 만족할 때만 붙여야 한다.

쉬운 예:

```text
처음 보는 종목에 회계 리스크가 발견됨:
  Red/Reject 또는 RiskReview 가능
  하지만 "4C로 추락"은 아님

기존 Green thesis 종목에 현재 계약 취소 공식 공시가 나옴:
  4C transition 후보 가능
```

### 5. 과거 연구자료 parity는 source-backed fixture로만 증명

연구 markdown에 정답이 적혀 있다고 그대로 쓰면 미래누수다.

```text
사용 가능:
  당시 원문 URL/snapshot/quote/table/API record

사용 금지:
  연구 md의 사후 MFE/MAE, 성공 label, source_proxy_only score
```

## 최종 판단

현재 v4는 잘못 가고 있는 부분을 상당히 막았다.
하지만 아직 운영 점수기가 완성된 것은 아니다.

정확한 현재 위치는 다음이다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS: yes
MEANINGFUL_OPERATIONAL_STAGE_PASS: no
BRAIN_WEB_EVIDENCE_PASS: no
FULL_THESIS_SMOKE_PASS: no
FULL_E2R_100 verified score: no
```

다음 작업의 목표는 Stage label을 더 많이 만드는 것이 아니다.
목표는 full thesis 경로가 끝난 row에만 full thesis 점수와 Stage를 만들고,
나머지는 정직하게 `Stage0`, `Watch`, `Pending`, `ProviderPending`으로 남기는 것이다.
