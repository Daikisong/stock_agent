# Census v4 Stage Presence Cross Check And Patch Direction - 2026-07-01

작성 목적:

```text
뭔가 잘못되고 있는 거 맞지?
Stage가 있는 애들이 있긴 해?
있다면 그 Stage는 실제 운영 Stage야, 아니면 상태판 label이야?
```

이 문서는 다음 에이전트가 위 질문을 바로 공격할 수 있게,
현재 산출물과 코드 경로를 같이 고정한다.

## 결론

짧은 답:

```text
Stage label이 붙은 종목은 있다.
하지만 full E2R 100점 thesis 운영 Stage가 끝난 종목은 현재 0개다.
```

현재 있는 것은 이쪽이다.

```text
Census/event 상태판 Stage
daily/ledger event 기반 부분 상태
claim-backed EVENT_WEIGHTED_PARTIAL row
```

현재 없는 것은 이쪽이다.

```text
FULL_E2R_100 verified score
삼성전자/하이닉스 HBM/C06 full thesis score
Stage3-Green / Stage3-Yellow 운영 판정
4B / 4C thesis transition 판정
Brain/Web promoted operating Stage row
```

쉬운 예:

```text
지금은 병원 접수표에 "대기", "추가 검사 필요", "위험 신호 있음"이 붙은 상태다.
하지만 최종 진단서와 치료 등급이 나온 상태는 아니다.
```

## 검산 원본

기준 파일:

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/leaf_artifact_audit.json
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/brain_web_attempt_audit.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01/brain_stage_promotion_audit.json
output/census_v4/2026-07-01/samsung_hynix_full_thesis_smoke.json
output/census_v4/2026-07-01/test_result_artifact.json
```

검산 명령:

```bash
python - <<'PY'
import json
from collections import Counter
from pathlib import Path

root = Path("output/census_v4/2026-07-01")
rows = [
    json.loads(line)
    for line in (root / "census_stage_status.jsonl").read_text().splitlines()
    if line.strip()
]

print("rows", len(rows))
for key in [
    "base_stage",
    "canonical_stage",
    "full_thesis_stage",
    "score_scale",
    "census_status",
    "assessment_depth",
    "stage_signal",
    "score_valid_status",
]:
    print(key, dict(Counter(str(row.get(key)) for row in rows)))

print("non_NO_SCORE", sum(1 for row in rows if row.get("score_scale") != "NO_SCORE"))
print("rows_with_accepted_claim_ids", sum(1 for row in rows if row.get("accepted_claim_ids")))
print("rows_with_score_contribution_ids", sum(1 for row in rows if row.get("score_contribution_ids")))
print("rows_with_stagecourt_trace_id", sum(1 for row in rows if row.get("stagecourt_trace_id")))
print("verified_score_present", sum(1 for row in rows if row.get("verified_score") is not None))
print("full_e2r_verified_score_present", sum(1 for row in rows if row.get("full_thesis_verified_score") is not None))
PY
```

현재 기대값:

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

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

score_scale:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

stage_scope:
  CENSUS_EVENT_BOARD: 3391

score_scope:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

census_status:
  SCANNED:        3306
  DEEP_VERIFIED:    67
  PENDING_SOURCE:   15
  LIGHT_ONLY:        3

assessment_depth:
  CHEAP_BASELINE: 3309
  VERIFIED_STAGE:   67
  OFFICIAL_LIGHT:   15

stage_signal:
  NO_CURRENT_CATALYST: 3306
  OFFICIAL_EVENT_WATCH: 36
  MATERIAL_CLAIM_WATCH: 30
  EVIDENCE_INSUFFICIENT: 10
  SOURCE_PENDING: 8
  RISK_REVIEW: 1

score_valid_status:
  NO_CURRENT_EVENT: 3306
  FINAL_WITH_NONMATERIAL_GAPS: 37
  PENDING_MATERIAL_GAPS: 30
  NOT_SCORED: 11
  INVALID_EVIDENCE: 7

non_NO_SCORE: 67
rows_with_accepted_claim_ids: 67
rows_with_score_contribution_ids: 67
rows_with_stagecourt_trace_id: 74
verified_score_present: 0
full_e2r_verified_score_present: 0
```

주의:

```text
DEEP_VERIFIED, VERIFIED_STAGE, FINAL_WITH_NONMATERIAL_GAPS, COMPLETE
같은 단어는 이 문서에서 모두 event-board / partial-score 범위다.

stage_scope=CENSUS_EVENT_BOARD
AND full_thesis_stage=FULL_THESIS_NOT_RUN
AND verified_score_present=0
AND full_e2r_verified_score_present=0

이면 full thesis 운영 Stage가 아니다.
```

쉬운 예:

```text
"쪽지시험 답안 번호가 맞다"는 VERIFIED이지,
"기말고사 최종 등급이 확정됐다"는 VERIFIED가 아니다.
```

## Stage가 "있다"는 말의 정확한 의미

`base_stage`는 현재 상태판 label이다.

```text
Stage0:
  이번 census에서 평가 대상에는 올렸지만 현재 candidate event가 없다.

Stage1:
  공식 이벤트나 일부 ledger claim이 있어 watch 대상이다.

Stage2-Watch:
  material claim이 있어 더 볼 필요가 있지만,
  Yellow/Green에 필요한 cash/revision/multi-source bridge가 부족하다.

Red:
  risk review signal이 있다.
  하지만 full thesis 4C transition 판정은 아니다.
```

`canonical_stage`는 프로젝트 canonical enum에 맞춘 표시값이다.

```text
Stage2-Watch -> canonical 2
Red          -> canonical 3-Red
```

주의:

```text
canonical 2 또는 3-Red가 있다고 해서 full thesis Stage2/Stage3-Red가 끝났다는 뜻은 아니다.
full_thesis_stage가 전부 FULL_THESIS_NOT_RUN이기 때문이다.
```

쉬운 예:

```text
Stage2-Watch   30개
= "이 종목은 공식 claim이 있어 추가 조사해야 한다"
!= "E2R 100점 thesis에서 Stage2가 확정됐다"
```

## 삼성전자 / SK하이닉스

삼성전자:

```text
symbol: 005930
company_name: 삼성전자
base_stage: Stage1
canonical_stage: 1
stage_signal: OFFICIAL_EVENT_WATCH
score_scale: EVENT_WEIGHTED_PARTIAL
event_evidence_score: 4.0
verified_score: null
full_e2r_verified_score: null
full_thesis_stage: FULL_THESIS_NOT_RUN
accepted_claim_ids: 1개
score_contribution_ids: 1개
```

SK하이닉스:

```text
symbol: 000660
company_name: SK하이닉스
base_stage: Stage1
canonical_stage: 1
stage_signal: OFFICIAL_EVENT_WATCH
score_scale: EVENT_WEIGHTED_PARTIAL
event_evidence_score: 4.0
verified_score: null
full_e2r_verified_score: null
full_thesis_stage: FULL_THESIS_NOT_RUN
accepted_claim_ids: 1개
score_contribution_ids: 1개
```

정확한 해석:

```text
맞음:
  삼성전자/하이닉스는 daily event board에 올라왔다.

틀림:
  삼성전자/하이닉스 HBM/C06 full thesis 점수와 Stage가 나왔다.
```

쉬운 예:

```text
삼성전자/하이닉스의 현재 4.0은 "접수표에 붙은 부분 이벤트 점수"다.
HBM 고객 배정, qualification, shipment/revenue mix, FCF/revision bridge를 다 본
100점짜리 thesis 점수가 아니다.
```

## 92개 accepted claim과 67개 scored row의 차이

현재 leaf artifact 수:

```text
accepted_claims.jsonl:       92
evidence_claims.jsonl:       92
score_contributions.jsonl:   92
stagecourt_traces.jsonl:     92

census_stage_status row with accepted_claim_ids:        67
census_stage_status row with score_contribution_ids:    67
census_stage_status row with stagecourt_trace_id:       74
```

이 차이를 다음처럼 읽으면 안 된다.

```text
92개 full thesis가 있다.
92개 Stage row가 있다.
```

현재 구조는 대표 row를 만들 때 symbol별 대표 atomic decision만 `census_stage_status`에 올린다.
그래서 leaf에는 claim/trace가 더 많고, 대표 상태판에는 67개 부분 점수 row만 남는다.

이제 이 차이는 `non_representative_claim_audit.json`으로 장부화된다.

현재 값:

```text
verdict: PASS
critical_count: 0
warning_count: 7
accepted_claim_count: 92
representative_stage_claim_count: 67
non_representative_claim_count: 25

reason_distribution:
  non_representative_atomic_decision: 18
  accepted_claim_without_atomic_decision: 7

critical_counts:
  non_representative_claim_unreasoned_count: 0
  non_representative_claim_score_leak_count: 0
  representative_atomic_claim_not_in_stage_row_count: 0
```

해석:

```text
18개 claim은 비대표 atomic decision에 묶여 대표 row로 선택되지 않았다.
7개 claim은 accepted claim leaf에는 있지만 atomic decision에는 없다.
다만 이 25개가 대표 점수에 몰래 섞인 수는 0이다.
```

따라서 7개 warning은 다음 refinement 대상이다.
하지만 현재 anti-fake 기준에서는 score leak이 없으므로 critical fail은 아니다.

다음 에이전트가 반드시 때려봐야 하는 공격 지점은 남아 있다.

```text
질문 1:
  대표 row 밖에 남은 25개 claim이 왜 제외됐는가?

질문 2:
  제외 사유가 duplicate/non-representative/pending/invalid로 장부화돼 있는가?

질문 3:
  같은 symbol의 여러 claim 중 대표 trace를 고르는 정책이 deterministic한가?

질문 4:
  대표 row 밖 claim이 몰래 score나 Stage에 섞이지 않는가?
```

현재 문서화 기준에서는 이 차이를 completion blocker로 보지는 않는다.
다만 `accepted_claim_without_atomic_decision_count=7`은 full operational readiness 전에 줄이거나 별도 제외 사유를 더 구체화해야 한다.

## SourceTask ID Chain 최신 패치

이제 `source_task_satisfaction_audit.json`은 단순 count-only 감사가 아니다.

현재 schema:

```text
e2r_census_v4_source_task_satisfaction_audit_v2
```

대표 score claim에는 아래 체인을 강제한다.

```text
SourceTaskExecution/task_id
-> accepted_claims.claim_id
-> evidence_documents.document_id
-> evidence_anchors.anchor_id
-> score_contributions.support_claim_ids
-> stagecourt_traces.score_contribution_ids / accepted_claim_ids
-> census_stage_status.accepted_claim_ids / score_contribution_ids / stagecourt_trace_id
```

현재 canonical 값:

```text
representative_score_claim_count: 67
source_task_chain_closed_to_representative_stage_count: 67
source_task_chain_closed_to_stagecourt_count: 92
critical_count: 0
warning_count: 25
non_representative_source_task_claim_count: 25
live_source_task_satisfaction_pass_allowed: false
```

해석:

```text
대표 event-board score claim 67개는 SourceTask까지 역추적된다.
하지만 accepted claim 92개 중 25개는 대표 row 밖 warning이다.
그리고 이 PASS는 live source pass가 아니라 ledger refresh 검산 pass다.
```

쉬운 예:

```text
성적표에 반영된 숙제 67개는 제출 기록과 채점표까지 번호가 맞는다.
하지만 제출된 초안 25개는 성적표에 안 들어갔고, 왜 빠졌는지는 warning으로 계속 추적해야 한다.
```

## 현재 진짜로 잘못될 수 있는 부분

### 1. Stage라는 단어가 너무 강하다

`base_stage=Stage2-Watch`는 의미상 상태판 label인데,
사용자는 당연히 "E2R Stage2"로 읽는다.

따라서 다음 패치에서 아래 중 하나가 필요하다.

```text
선택 A:
  필드명은 유지하되 operator 문서와 API 출력에
  census_base_stage / full_thesis_stage를 항상 같이 표시한다.

선택 B:
  내부 field를 census_base_stage로 바꾸고,
  기존 base_stage는 backward compatibility alias로만 둔다.
```

최소 요구:

```text
full_thesis_stage=FULL_THESIS_NOT_RUN이면
Stage3-Green/Yellow/Red/4B/4C 운영 문구를 출력하지 않는다.
```

### 2. `canonical_stage=3-Red`가 오해를 만든다

현재 Red 1개는 event 상태판의 `RISK_REVIEW`다.
하지만 canonical enum으로는 `3-Red`에 들어간다.

이 말은 아래처럼 읽히면 안 된다.

```text
full thesis Stage3-Red reject 확정
```

정확한 해석:

```text
event board risk-review signal
full_thesis_stage=FULL_THESIS_NOT_RUN
transition_overlay 없음
4C 아님
```

다음 패치 방향:

```text
base_stage/canonical_stage 옆에 stage_scope를 둔다.

stage_scope:
  CENSUS_EVENT_BOARD
  BRAIN_WEB_PARTIAL
  FULL_THESIS
```

그리고 `stage_scope != FULL_THESIS`이면 operator digest에서
`Stage3-Red 운영 판정`이라는 표현을 금지한다.

### 3. Brain/Web은 StageCourt trace까지 가도 대표 Stage가 아니다

현재 canonical run:

```text
brain_web_mode: disabled
brain_web_attempt.verdict: NOT_REQUESTED
brain_stage_promotion.verdict: NOT_REQUESTED
brain_web_readiness_gate.verdict: NOT_REQUESTED
```

별도 enabled smoke에서는 일부가 더 진행됐다.

```text
real provider success: 1
source task: 10
accepted unique claim: 2
score contribution: 5
Brain StageCourt trace: 1
promoted census_stage_status row: 0
```

따라서 Brain/Web 경로가 완전히 죽은 것은 아니지만,
대표 운영 Stage로 올라가는 마지막 다리가 없다.

코드상 병목:

```text
_brain_score_stage_export_rows()
  Brain StageCourt trace를 만들 수 있다.
  하지만 not_promoted_to_census_stage_status=True로 남긴다.

_stage_rows_from_v3()
  대표 census_stage_status row를 만든다.
  현재 v3/ledger 대표 decision만 보고 Brain trace를 병합하지 않는다.

_brain_stage_promotion_audit()
  이미 승격된 Brain row가 안전한지 검사할 수 있다.
  strict/live/real fixture에서는 producer가 만든 승격 row를 검증할 수 있다.

_brain_web_readiness_gate_audit()
  accepted claim -> contribution -> StageCourt trace -> promoted row 연결을 요구한다.
  그래서 현재는 pass가 막히는 것이 정상이다.
```

현재 코드 상태:

```text
1. _promote_brain_stage_rows(...)는 구현됐다.
2. strict/live/real provider fixture에서 Brain StageCourt trace를 대표 row로 승격하는 테스트가 있다.
3. snapshot://, provider none, fake source, missing document/anchor, missing contribution이면 승격 금지다.
4. 승격 row는 stage_scope=BRAIN_WEB_PARTIAL, score_scope=BRAIN_WEB_CLAIM_BACKED_PARTIAL, score_scale=EVENT_WEIGHTED_PARTIAL이다.
5. 승격 row도 full_thesis_stage=FULL_THESIS_NOT_RUN이다.
6. full thesis runner가 끝난 row만 FULL_E2R_100/FULL_THESIS로 승격할 수 있다.
```

남은 패치 방향:

```text
1. 실제 enabled live/codex run에서 source task, document, anchor, accepted claim, contribution, StageCourt trace를 만든다.
2. 그 실제 run 산출물을 _promote_brain_stage_rows(...)에 태운다.
3. BRAIN_WEB_PARTIAL promoted row가 생기더라도 FULL_THESIS와 분리한다.
4. full thesis runner가 끝난 row만 FULL_E2R_100으로 승격한다.
```

### 4. `EVENT_WEIGHTED_PARTIAL`을 verified score로 읽으면 다시 사고 난다

현재 67개 부분 점수 row는 source-backed claim이 있지만 full thesis 점수가 아니다.

금지:

```text
event_evidence_score 4.0
-> verified_score 4.0으로 복사
-> "삼성전자 4점"이라고 출력
```

허용:

```text
event_evidence_score:
  daily event 상태판용 부분 점수

verified_score:
  FULL_E2R_100 thesis runner가 끝난 뒤에만 채움

full_thesis_verified_score:
  full thesis 전용 점수
```

### 5. "없는 Stage"를 낮은 점수로 확정하면 안 된다

Brain/Web, full thesis, provider가 안 돌았거나 pending이면 낮은 점수 확정이 아니다.

쉬운 예:

```text
뉴스를 못 찾았다
!= 계약이 없다
!= 고객이 없다
!= Stage0 확정
```

현재 v4의 좋은 점은 이것을 어느 정도 막고 있다는 점이다.

```text
NO_CURRENT_CATALYST
SOURCE_PENDING
PENDING_MATERIAL_GAPS
FULL_THESIS_NOT_RUN
```

이런 상태가 낮은 점수 확정과 분리되어 있다.

## 다음 패치 순서

다음 에이전트는 Stage label을 더 많이 만드는 작업부터 하면 안 된다.
순서는 아래가 맞다.

### 1. Stage scope를 더 강하게 운영 출력에 노출한다

현재 구현된 필드:

```text
stage_scope:
  CENSUS_EVENT_BOARD
  BRAIN_WEB_PARTIAL
  FULL_THESIS

score_scope:
  NO_SCORE
  EVENT_WEIGHTED_PARTIAL
  BRAIN_WEB_CLAIM_BACKED_PARTIAL
  FULL_E2R_100
```

현재 canonical run:

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD: 3391

score_scope_distribution:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67
```

남은 완료 조건:

```text
stage_scope != FULL_THESIS이면
운영 Green/Yellow/Red/4B/4C 문구를 출력하지 않는다.
```

### 2. non-representative claim warning을 줄인다

현재 92개 accepted claim 중 67개만 대표 Stage row에 직접 연결된다.
이 차이는 이제 artifact로 남는다.

추가된 파일:

```text
non_representative_claim_audit.json
```

필수 필드:

```text
accepted_claim_count
representative_stage_claim_count
non_representative_claim_count
reason_distribution
sample_non_representative_claims
unexpected_score_leak_count
```

현재 통과 조건:

```text
non_representative claim이 score/stage에 몰래 들어간 경우 0
reason 없는 제외 claim 0
```

남은 refinement:

```text
accepted_claim_without_atomic_decision_count: 7
```

이 7개는 점수 leak은 아니지만, 장기적으로는 `semantic_guard_blocked`, `duplicate_leaf`, `non_score_eligible_claim`처럼 더 구체적인 이유로 분류해야 한다.

### 3. Brain/Web strict promotion producer는 구현됐고, 실제 live 적용이 남았다

현재는 producer와 audit gate가 있다.
다만 canonical run은 `brain_web_mode=disabled`, `brain_stage_promotion_mode=disabled`라서 promoted row가 0개다.

구현된 함수:

```text
_promote_brain_stage_rows(...)
```

필수 gate:

```text
brain_web_mode=enabled
brain_stage_promotion_mode=strict
planner provider is real
source acquisition is live official-first or approved bounded live
accepted claim has document_id + anchor_id
document is not snapshot://
claim is DIRECT, CURRENT, ACCEPTED, score_eligible
score contribution supports accepted claim
StageCourt trace supports same claim and contribution
brain_to_claim_trace connects claim -> contribution -> trace
```

이미 검증된 것:

```text
tests.test_census_v4_brain_stage_promotion_gate
  test_strict_live_connected_promoted_brain_row_is_promotion_applied
  test_strict_live_connected_brain_trace_promotes_representative_row_and_updates_trace_refs
```

아직 검증되지 않은 것:

```text
실제 live/codex enabled run에서 위 fixture와 같은 id-chain이 생기는가.
```

완료 조건:

```text
brain_web_readiness_gate_audit.verdict = READY_FOR_BRAIN_WEB_EVIDENCE_PASS
brain_web_evidence_pass_allowed = true
brain_to_census_stage_exported_count > 0
```

주의:

```text
Brain/Web strict promotion은 full thesis pass가 아니다.
이 단계에서도 FULL_E2R_100 verified_score를 만들면 안 된다.
```

### 4. 삼성전자/하이닉스 full thesis smoke를 실제 실행한다

현재 `full_thesis_smoke_tasks.jsonl`은 planning-only다.

다음에 필요한 것:

```text
005930 / 000660
target archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
required primitives:
  named_customer_or_customer_class
  qualification_status
  capacity_allocation_or_sold_out
  shipment_or_revenue_mix
  cash_or_revision_conversion
  repeat_evidence_family
  negative_guard_current_status
```

완료 조건:

```text
full thesis claim ids 존재
full thesis score contribution ids 존재
full thesis StageCourt trace ids 존재
score interval 존재
material gaps이면 pending으로 기록
충분하면 full_thesis_stage와 full_thesis_verified_score 기록
```

### 5. 과거 연구자료 parity는 source-backed replay로만 검증한다

연구 markdown의 결론 label을 정답으로 쓰면 미래누수다.

사용 가능:

```text
당시 원문 URL
snapshot
quote
table cell
API record
```

사용 금지:

```text
source_proxy_only score
evidence_url_pending score
사후 MFE/MAE
연구자가 붙인 성공 label
```

## 다음 리뷰어가 바로 때려볼 must-fail 조건

아래 중 하나라도 발생하면 현재 문서의 결론은 깨진다.

```text
1. full_thesis_stage != FULL_THESIS_NOT_RUN 인 row가 있는데 full thesis claim/score/trace가 없다.
2. verified_score가 있는데 score_scale != FULL_E2R_100이다.
3. Stage3-Green/Yellow/Red/4B/4C 운영 문구가 stage_scope 없이 출력된다.
4. Brain/Web disabled인데 brain_web_evidence_pass=true다.
5. Brain StageCourt trace가 있는데 promoted row 없이 READY_FOR_BRAIN_WEB_EVIDENCE_PASS가 된다.
6. accepted claim이 document_id/anchor_id 없이 score contribution에 들어간다.
7. 대표 row 밖 claim이 score/stage에 섞이거나, warning 25개의 제외 사유가 더 이상 추적되지 않는다.
8. 삼성전자/하이닉스 event_evidence_score를 HBM/C06 full thesis score로 출력한다.
9. source_proxy_only 연구 row가 운영 score contribution으로 들어간다.
10. provider failure 또는 not requested를 낮은 점수 확정으로 출력한다.
```

## 최종 판단

현재 v4는 "Stage가 아예 없다"가 아니다.

정확한 현재 위치:

```text
Stage label: 있음
claim-backed partial event row: 있음, 67개
Stage2-Watch label: 있음, 30개
Red risk-review label: 있음, 1개

full thesis operating Stage: 없음
FULL_E2R_100 verified score: 없음
Brain/Web promoted Stage row: 없음
Samsung/Hynix HBM thesis result: 없음
```

따라서 사용자가 느낀 불안은 맞다.
Stage라는 단어가 이미 나오기 때문에 운영 Stage처럼 보일 수 있다.

하지만 현재 패치의 방어막은 그 오해를 막기 위해 다음 사실을 산출물에 남긴다.

```text
full_thesis_stage=FULL_THESIS_NOT_RUN
verified_score=null
full_e2r_verified_score=null
brain_web_evidence_pass=false
meaningful_operational_stage_pass=false
goal_completion_ready=false
```

다음 작업은 Stage label을 억지로 늘리는 것이 아니다.
이미 추가된 `stage_scope`와 `non_representative_claim_audit`를 기준으로,
다음은 Brain/Web strict promotion과 삼성전자/하이닉스 full thesis smoke를 닫는 것이다.
