# Census v4 Facility Correction Semantic Guard Patch - 2026-07-01

이 문서는 다음 에이전트가 대웅 `003090` 사례를 다시 공격할 수 있게, 시설투자 정정공시가 capacity expansion 점수로 들어가던 문제와 패치 결과를 고정한다.

## 한 줄 결론

```text
Brain/Web attempt는 대웅 공시를 이미 accepted claim으로 승인하지 않았다.
하지만 기존 event-board ledger 경로에는 capacity_expansion claim/contribution 흔적이 남아 있었다.

최신 패치 후 대표 census_stage_status row는 이 흔적을 점수로 쓰지 않는다.
semantic_guard_status=BLOCKED
semantic_guard_class=facility_investment_correction_followup_required
score_scale=NO_SCORE
base_stage=Stage1
```

쉬운 예:

```text
"공장 증설 완료"는 점수 재료가 될 수 있다.
"공장 증설 종료일을 연장하는 정정공시"는 오히려 후속 확인이 필요한 일정 지연 신호다.
따라서 둘을 같은 capacity expansion 점수로 넣으면 안 된다.
```

## 실제 최신 row

최신 canonical run:

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
```

대웅 `003090` 대표 row:

```text
symbol: 003090
company_name: 대웅
base_stage: Stage1
canonical_stage: 1
score_scale: NO_SCORE
event_evidence_score: null
raw_contribution_score: null
semantic_guard_status: BLOCKED
semantic_guard_class: facility_investment_correction_followup_required
blocked_claim_ids:
  - CLM-d4ccf4c0a0b39f2b0142
blocked_score_contribution_ids:
  - SCON-39d486c6eb07fb5f9d98
```

중요한 해석:

```text
claim/contribution leaf가 존재한다
!= 대표 점수에 반영됐다

대표 점수 row에서는 semantic guard가 contribution을 막았고,
raw_contribution_score도 운영 표면에서는 null로 정규화한다.
그 결과 partial score row 72개가 67개로 줄었다.
대표 밖 non-representative claim은 20개에서 25개로 늘었고,
non_representative_claim_score_leak_count=0이다.
```

## 패치 위치

```text
src/e2r/production/claim_extraction/primitive_mapper.py
src/e2r/evidence/primitive_semantic_guard.py
src/e2r/census/census_runner_v4.py
```

핵심 변경:

```text
1. primitive mapper에서 시설투자 정정/종료일 연장/취소 문구는
   positive capacity_investment_claim mapping으로 승인하지 않는다.

2. score contribution semantic guard에서
   capacity_expansion / capacity_precommitted / bottleneck_pricing support claim이
   정정, 지연, 연장, 취소 문맥이면 score_allowed=false로 막는다.

3. Brain/Web source_task_executions export에 top-level symbol,
   candidate_event_id, source_origin, brain_web_origin을 붙여
   다음 리뷰어가 attempt row를 추적할 수 있게 했다.
```

이건 종목명 예외처리가 아니다.

```text
나쁜 방식:
  if symbol == "003090": score = 0

이번 방식:
  모든 종목에서 facility investment correction/delay/cancellation 문맥은
  positive capacity score support로 쓰지 않는다.
```

## 검증 결과

Targeted tests:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_cutover_contract_blind_extraction \
  tests.test_contract_semantic_classifier \
  tests.test_census_v4_semantic_guard -v
```

결과:

```text
Ran 17 tests
OK
```

관련 Census v4 tests:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_source_task_satisfaction_chain \
  tests.test_census_v4_primitive_state_chain \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_non_representative_claim_audit \
  tests.test_census_v4_semantic_guard \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 43 tests
OK
```

전체 suite artifact:

```text
output/census_v4/2026-07-01/test_result_artifact.json

artifact_status: OK
artifact_test_count: 4942
artifact_failed_count: 0
artifact_error_count: 0
artifact_duration_seconds: 170.2478
```

canonical v4 재실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --fail-on-critical-audit true \
  --write-operational-docs auto \
  --test-result-artifact output/census_v4/2026-07-01/test_result_artifact.json
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

## 최신 canonical 숫자

```text
rows: 3391

base_stage:
  Stage0 3306
  Stage1 54
  Stage2-Watch 30
  Red 1

canonical_stage:
  0 3306
  1 54
  2 30
  3-Red 1

score_scale:
  NO_SCORE 3324
  EVENT_WEIGHTED_PARTIAL 67

stage_scope:
  CENSUS_EVENT_BOARD 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN 3391

verified_score_present: 0
full_e2r_verified_score_present: 0
event_evidence_score_present: 67
```

감사 파일:

```text
leaf_artifact_audit.json
  verdict: PASS
  critical_count: 0
  sample_leaf_bundle_count: 67
  non_representative_claim_count: 25

source_task_satisfaction_audit.json
  verdict: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
  critical_count: 0
  representative_score_claim_count: 67
  source_task_chain_closed_to_representative_stage_count: 67
  source_task_execution_count: 92
  accepted_claim_count: 92

primitive_state_chain_audit.json
  verdict: PASS
  critical_count: 0
  representative_score_claim_count: 67
  representative_score_claim_with_primitive_state_count: 67
  accepted_claim_count: 92

non_representative_claim_audit.json
  verdict: PASS
  critical_count: 0
  non_representative_claim_count: 25
  accepted_claim_count: 92
```

## enabled probe와 헷갈리면 안 되는 점

별도 enabled probe:

```text
/tmp/census_v4_enabled_probe
```

이 probe는 Brain/Web live 시도를 확인하기 위한 격리 run이다.

```text
real_provider_success_count: 1
source_task_execution_count: 7
fetched real document: 6
unique real document: 4
accepted Brain claim: 0
Brain score contribution: 0
Brain StageCourt trace: 0
verdict: NOT_READY
```

따라서:

```text
canonical disabled run PASS
  = anti-fake 상태판과 ledger refresh 검산 PASS

/tmp enabled probe NOT_READY
  = live Brain/Web이 아직 accepted claim을 만들지 못함

둘을 합쳐서 "Brain/Web 운영 Stage PASS"라고 말하면 실패다.
```

## 다음 에이전트 공격 질문

```text
1. 다른 시설투자 정정/지연/취소 공시도 capacity score로 막히는가?
2. 정정공시라도 "금액 증액/기간 단축/투자 확정"처럼 긍정 bridge가 명시되면 follow-up으로 남기는가, 무조건 0점으로 죽이는가?
3. semantic guard가 contribution만 막고 원본 claim leaf는 audit trace로 남기는가?
4. representative row 밖 claim 25개가 score leak 없이 non_representative audit에 남는가?
5. 이 패치가 C29/C31에만 묶인 종목별 예외가 아니라 전역 primitive semantic guard인가?
6. Brain/Web accepted claim이 생긴 경우에도 같은 guard가 score contribution 전에 적용되는가?
```

현재 답:

```text
1, 3, 4, 5는 테스트와 canonical audit로 닫혔다.
2와 6은 다음 live Brain/Web accepted-claim 단계에서 더 빡세게 확인해야 한다.
```
