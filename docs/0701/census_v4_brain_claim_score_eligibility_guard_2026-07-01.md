# Census v4 Brain Claim Score Eligibility Guard - 2026-07-01

작성 목적:

```text
Brain/Web이 accepted claim을 만들었을 때,
그 claim이 자동으로 점수 입력값이 되지 못하게 막는다.
```

이전 위험:

```text
Brain/Web accepted claim export가 score_eligible=True를 무조건 찍었다.
```

쉬운 예:

```text
월덱스 감사의견 문서에 삼성전자가 고객사로 언급됐다.
LLM/파서가 accepted claim처럼 보이는 row를 만들었다.
그 row가 score_eligible=True로 자동 기록되면,
삼성전자 회계 리스크처럼 잘못 점수에 들어갈 수 있다.
```

이번 패치는 `score_eligible`을 LLM이나 bridge가 직접 정하는 값이 아니라,
코드가 검증 결과로 파생하는 값으로 바꾼다.

## 패치 위치

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_web_readiness_gate.py
tests/test_census_v4_brain_stage_promotion_gate.py
```

핵심 함수:

```text
_accepted_claim_payload_from_brain
_brain_claim_score_eligibility_reasons
_brain_claim_quality_counts
_brain_web_readiness_gate_audit
_brain_stage_promotion_audit
build_source_acquisition_report_v4
```

## 새 Eligibility 조건

Brain/Web claim은 아래 조건을 모두 만족해야 `score_eligible=true`가 된다.

```text
1. document_id가 있고 실제 EvidenceDocument row가 있다.
2. anchor_id가 있고 실제 EvidenceAnchor row가 있다.
3. event_date 또는 source_cutover_date가 있다.
4. target_scope_status == DIRECT
5. temporal_status in CURRENT / PRESENT_CURRENT / OPEN
6. mapping_status == ACCEPTED
7. primitive_id가 있다.
8. source_url이 snapshot:// 이 아니다.
```

하나라도 실패하면:

```text
score_eligible=false
eligibility_reasons=[...]
```

예:

```json
{
  "source_url": "snapshot://opendart/111111/202405210001",
  "target_scope_status": "DIRECT",
  "temporal_status": "CURRENT",
  "mapping_status": "ACCEPTED",
  "primitive_id": "contract_amount_to_prior_sales",
  "score_eligible": false,
  "eligibility_reasons": ["snapshot_source_not_score_eligible"]
}
```

중요:

```text
DIRECT/CURRENT/ACCEPTED primitive라도 snapshot source면 production score eligible이 아니다.
```

쉬운 예:

```text
"답안 내용은 그럴듯함"
!=
"공식 시험지에 채점 가능한 답안으로 인정됨"
```

## Gate 변화

이제 Brain/Web readiness gate와 promotion audit는 아래 값을 감시한다.

```text
brain_claim_score_ineligible_count
```

이 값이 0보다 크면:

```text
Brain/Web evidence pass 금지
Brain/Web stage promotion 금지
```

차단 문구:

```text
accepted Brain/Web claims are not score eligible by deterministic guard: N
```

## Source Count Semantics 패치

추가로 `build_source_acquisition_report_v4`의 문서 수 카운트도 분리했다.

이전 위험:

```text
snapshot:// 문서도 real_document_fetched_count에 들어갈 수 있었다.
```

새 의미:

```text
fetched_document_count:
  snapshot 포함, 어떤 문서든 가져온 총량

snapshot_document_fetched_count:
  snapshot:// 문서 수

live_document_fetched_count:
  snapshot:// 이 아닌 live/source URL 문서 수

real_document_fetched_count:
  live_document_fetched_count와 같은 의미
  즉 운영 pass용 live non-snapshot document count

real_document_count_semantics:
  live_non_snapshot_document_only
```

쉬운 예:

```text
복사본 서류를 열람한 것은 fetched_document_count다.
당일 원본 발급 서류를 확보한 것은 real_document_fetched_count다.
```

## 격리 Enabled Smoke 결과

canonical output을 바꾸지 않는 `/tmp` 격리 실행:

```text
/tmp/census_v4_live_count_smoke_3uVXgd/out
```

실행 성격:

```text
run_mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode: enabled
brain_planner_provider: codex
brain_source_acquisition: frozen_real_source_snapshot
brain_stage_promotion_mode: strict
target_gate: meaningful
```

관측값:

```text
readiness_verdict: NOT_READY

brain_web_attempt:
  verdict: ATTEMPTED_NOT_CUTOVER_READY
  planner_run_count: 1
  real_provider_success_count: 1
  source_task_execution_count: 10
  real_document_fetched_count: 0
  unique_real_document_fetched_count: 0
  accepted_claim_count: 5
  unique_accepted_claim_count: 2

brain_stage_promotion:
  verdict: BLOCKED
  brain_snapshot_document_count: 3
  brain_claim_score_ineligible_count: 2

brain_web_readiness_gate:
  verdict: BLOCKED
  real_document_fetched_count: 0
  brain_web_evidence_pass_allowed: false
  brain_claim_score_ineligible_count: 2
```

accepted Brain/Web claims:

```text
CLM-a78c0fa3b1f24fcb7478
  source_url: snapshot://opendart/111111/202405210001
  score_eligible: false
  eligibility_reasons:
    - snapshot_source_not_score_eligible

CLM-d36bc69a69251fe54fae
  source_url: snapshot://opendart/111111/202405210001
  score_eligible: false
  eligibility_reasons:
    - snapshot_source_not_score_eligible
```

해석:

```text
Codex planner와 source task는 실행됐다.
accepted claim과 StageCourt trace도 일부 생겼다.
하지만 snapshot source라 운영 score eligible이 아니고,
representative census_stage_status row 승격도 0개라 pass가 막혔다.
```

이게 정상이다.

쉬운 예:

```text
연습장 답안은 써졌다.
하지만 원본 시험지/검증 anchor가 아니라서 성적표에 반영하지 않았다.
```

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 13 tests
OK
```

추가된 회귀 조건:

```text
score_eligible=false인 Brain/Web claim은 readiness pass를 막는다.
snapshot:// source에서 export된 Brain/Web accepted claim은 score_eligible=false가 된다.
```

## 남은 것

이번 패치는 운영 full thesis를 완료한 것이 아니다.

아직 남은 blocker:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
```

다음 패치 방향:

```text
1. live_official_first 또는 live_full_bounded에서 실제 source_url/doc/anchor를 만든다.
2. snapshot source가 아닌 accepted claim을 만든다.
3. Brain/Web strict promotion으로 representative census_stage_status row를 만든다.
4. 그 후에도 full thesis는 별도 FULL_E2R_100 scope로만 승격한다.
```

최종 판단:

> 이번 패치는 "Brain/Web accepted claim이 생겼다"와 "점수에 넣어도 된다"를 분리한 guard다.
