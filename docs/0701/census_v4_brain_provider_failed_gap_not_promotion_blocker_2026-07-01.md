# Census v4 Brain Provider-Failed Gap Not Promotion Blocker Patch - 2026-07-01

작성 목적:

```text
Brain/Web enabled smoke에서 accepted claim과 StageCourt trace가 있어도,
별도 provider-failed follow-up task 하나 때문에 representative row 승격이 막히는 문제를 분리한다.
```

이 문서는 Brain/Web pass 문서가 아니다.
이번 패치는 `BRAIN_WEB_EVIDENCE_PASS`를 완성하지 않았다.
다만 claim-backed Brain trace 승격을 잘못 막던 guard 하나를 고쳤다.

## 문제

이전 promotion/readiness audit는 모든 Brain source task에 `fetched_document_ids`가 있어야 한다고 봤다.

그런데 enabled smoke에서는 다음 두 종류의 task가 섞인다.

```text
1. claim-producing task
   - accepted_claim_ids 있음
   - score contribution / StageCourt trace를 지지함
   - 반드시 document_id / anchor_id / fetched_document_ids가 있어야 함

2. provider-failed follow-up task
   - accepted_claim_ids 없음
   - 예: IR update check가 live_official_no_fetchable_document로 실패
   - 점수 근거가 아니라 source/provider gap
```

이 둘을 구분하지 않으면 이런 일이 생긴다.

```text
accepted Brain claim 있음
score contribution 있음
Brain StageCourt trace 있음
그런데 별도 IR follow-up task가 provider failed라 문서 0개
→ Brain source task rows missing fetched document refs
→ promotion BLOCKED
```

쉬운 예:

```text
시험 답안지와 채점 근거는 제출됐다.
다만 추가 확인하려던 참고자료 하나가 도서관에 없었다.
이 참고자료 실패 때문에 이미 제출된 답안지 자체를 무효로 만들면 안 된다.
그 실패는 "추가 확인 gap"으로 남겨야 한다.
```

## 패치 원칙

문서 ref 필수 조건을 아래처럼 좁혔다.

```text
문서 ref 필수:
  accepted_claim_ids가 있는 task
  또는 status == EVIDENCE_OS_ACCEPTED 인 task

문서 ref 없어도 promotion blocker가 아닌 것:
  PROVIDER_FAILED
  NO_EVIDENCE_FOUND
  rejected/pending follow-up task
  accepted_claim_ids가 없는 red-team/status check task
```

중요:

```text
accepted claim이 있는데 document ref가 없는 경우는 여전히 fail이다.
snippet-only나 provider-failed task가 점수 근거로 들어가는 것도 여전히 fail이다.
```

## 변경 파일

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
tests/test_census_v4_brain_web_readiness_gate.py
```

새 helper:

```text
_source_task_requires_document_ref(row)
```

의미:

```text
accepted claim을 만든 task만 document ref mandatory로 본다.
provider-failed no-claim task는 source gap으로 남기고 promotion blocker로 쓰지 않는다.
```

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_web_readiness_gate \
  -v
```

결과:

```text
Ran 15 tests in 6.718s
OK
```

추가된 테스트:

```text
test_provider_failed_non_claim_task_does_not_block_brain_stage_promotion
test_provider_failed_non_claim_task_does_not_block_brain_web_readiness
```

검증하는 것:

```text
provider-failed no-claim task가 있어도
claim-backed Brain trace 자체는 promotion/readiness blocker가 되지 않는다.

반대로 accepted claim을 지지하는 task가 document ref 없이 들어가면
기존 guard가 계속 fail한다.
```

## Enabled Smoke 재검증

실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root /tmp/census_v4_enabled_brain_probe_after_docref_patch \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex \
  --brain-source-acquisition live_official_only \
  --brain-universe-limit 3 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-fetches-per-task 2 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --fail-on-critical-audit false \
  --write-operational-docs false
```

결과:

```text
NOT_READY
```

중요 수치:

```text
brain_web_attempt:
  planner_run_count: 21
  real_provider_success_count: 1
  source_task_execution_count: 7
  real_document_fetched_count: 8
  accepted_claim_count: 0

brain_stage_promotion:
  brain_source_task_without_document_ref_count: 0
  brain_source_task_unresolved_document_ref_count: 0
  brain_promoted_stage_row_count: 0
  blockers:
    - accepted brain claim count is zero
    - brain score contribution count is zero
    - brain StageCourt trace count is zero

brain_web_readiness_gate:
  source_task_execution_count: 7
  real_document_fetched_count: 4
  web_search_task_count: 0
  web_fetched_document_count: 0
  web_or_llm_accepted_claim_count: 0
  brain_source_task_without_document_ref_count: 0
```

해석:

```text
이번 패치 후 document-ref false blocker는 사라졌다.
하지만 이 smoke에서는 accepted Brain claim 자체가 0개라 promotion 대상 trace도 없었다.
따라서 Brain/Web pass는 여전히 실패가 맞다.
```

이전 smoke에서는 accepted Brain claim 1개와 StageCourt trace 1개가 생겼지만,
provider-failed no-claim IR task가 promotion blocker로 잡혔다.
이번 패치는 그 잘못된 blocker를 막는 회귀 테스트를 추가한 것이다.
실제 live run은 planner 출력과 source 문서가 달라질 수 있어 accepted claim 생성이 비결정적이다.

## 남은 blocker

아직 닫히지 않은 것:

```text
1. accepted Brain claim 안정 생성
2. Brain score contribution 안정 생성
3. Brain StageCourt trace 안정 생성
4. strict promotion으로 representative census row 승격
5. BRAIN_AND_WEB_ACQUISITION_ENABLED 모드의 web/news/Naver task 생성
6. web_fetched_documents.jsonl 생성
7. LLM claim_extractor_runs.jsonl 생성 또는 structured official extractor skip 사유 명시
8. Samsung/Hynix C06/HBM full thesis execution
```

특히 현재 `live_official_only` smoke는 web/news task를 만들지 않는다.
`BRAIN_AND_WEB_ACQUISITION_ENABLED` pass를 말하려면 `live_full_bounded` 또는 별도 bounded web acquisition path에서
다음 artifact가 생겨야 한다.

```text
web_search_tasks.jsonl
web_search_results.jsonl
web_fetched_documents.jsonl
claim_extractor_runs.jsonl
```

## 다음 패치 방향

우선순위:

```text
1. live_full_bounded / web acquisition mode가 실제 web_search_tasks와 fetched full documents를 내는지 조사한다.
2. official structured extraction과 LLM claim extraction의 audit label을 분리한다.
   - DART/API structured extractor면 claim_extractor_runs=0이어도 structured_skip artifact가 있어야 한다.
   - unstructured web/news/IR/PDF면 claim_extractor_runs가 있어야 한다.
3. accepted Brain claim이 0개인 enabled smoke에서 어떤 문서/primitive가 왜 reject됐는지 rejection audit를 강화한다.
4. accepted claim이 1개 이상 생긴 run에서는 strict promotion이 실제로 representative row를 바꾸는지 재검증한다.
```

## Must-Fail 조건

다음 중 하나라도 발생하면 실패다.

```text
1. accepted_claim_ids가 있는 task가 fetched_document_ids 없이 pass된다.
2. provider-failed no-claim task가 score contribution을 만든다.
3. provider-failed no-claim task가 Red/low score final로 바뀐다.
4. Brain/Web pass가 accepted claim 0개인데 true가 된다.
5. web/news acquisition mode에서 web_search_tasks.jsonl이 0개인데 pass가 된다.
6. structured official extractor와 LLM claim extractor를 같은 것처럼 보고한다.
```

## 최종 판단

이번 패치는 운영 완성이 아니라 배관 정리다.

```text
Before:
  provider-failed no-claim follow-up task도 promotion blocker가 됨

After:
  claim-producing task만 document ref mandatory
  provider-failed no-claim task는 source gap으로 남음
```

다음 승부처는 `accepted claim 안정 생성`과 `bounded web/news acquisition artifact 생성`이다.
