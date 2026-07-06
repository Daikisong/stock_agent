# Goal4 Runtime Attempt After Source Task Guard - 2026-07-06

이 문서는 `0705 Goal4 소스태스크 재시도 오진 보정` 이후 clean output root에서 다시 실행한 결과를 기록한다.

이번 실행은 Goal4 완료가 아니다. 결과는 `INVALID_PARTIAL_OUTPUT`이다.

쉬운 예:

```text
이전 retry2:
작업지시서가 있는데도 접수대에서 "외부웹 신청 더 해와"라고 돌려보냄
→ 검사실(source execution)로 못 내려감

이번 실행:
접수대 통과
→ planner 111개 완료
→ source execution까지 내려감
→ 하지만 검사 결과가 아직 의미 있는 full thesis pass로 닫히지 않음
```

## 실행 명령

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-05 \
  --universe krx \
  --output-root output/census_v4/2026-07-06-goal4-all-archetype-runtime-attempt-after-source-task-guard \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 111 \
  --brain-planner-success-limit 111 \
  --brain-planner-batch-size 5 \
  --brain-max-source-tasks-per-plan 5 \
  --brain-max-fetches-per-task 3 \
  --brain-accepted-claim-target 36 \
  --brain-max-distinct-candidate-attempts 111 \
  --brain-retry-max 1 \
  --brain-claim-extractor-provider auto \
  --brain-claim-extractor-timeout-seconds 180.0 \
  --brain-runtime-budget-seconds 7200.0 \
  --brain-candidate-event-seed-path docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate full_thesis \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim true \
  --fail-on-atomic-mismatch true \
  --fail-on-semantic-guard true \
  --fail-on-critical-audit true \
  --write-operational-docs true
```

결과:

```text
exit_code: 1
status: INVALID_PARTIAL_OUTPUT
output_root: output/census_v4/2026-07-06-goal4-all-archetype-runtime-attempt-after-source-task-guard
```

## 핵심 진전

```text
planner attempted: 111
real provider success: 105
distinct planner top archetype: 34
source task executions: 745
real/provider fetched documents: 595
attempt accepted claims: 57
StageCourt traces from full-thesis seed: 105
runtime budget exhausted: false
```

이전 retry2와 다른 점은 크다.

```text
이전: missing external web retry에 걸려 source execution으로 충분히 못 내려감
이번: planner 111개를 끝까지 시도하고 source execution까지 내려감
```

즉 `source_task_drafts`를 external-web gap으로 잘못 본 문제는 실제 run에서 완화됐다.

## C05-only 문제 상태

이번 run의 planner top archetype은 C05 하나로 몰리지 않았다.

관찰:

```text
distinct planner top archetype: 34
C08/C15/C17/C24/C28 planner top1 등장
C01~C32 대부분 planner top1 등장
```

쉬운 예:

```text
이전에는 모든 답안지가 "C05 계약형"으로 쏠렸다.
이번에는 최소한 문제 배정 단계에서는 반도체, 바이오, 소재, 금융, 소비재, R13 guard까지 나뉘었다.
```

하지만 이것은 완료가 아니다. planner에서 아키타입이 다양해진 것과 accepted claim/full thesis가 의미 있게 닫힌 것은 다르다.

## 남은 blockers

`brain_web_readiness_gate_audit.json` 기준:

```text
verdict: BLOCKED

blockers:
- web/LLM accepted claim count is zero
- Brain/Web source task budget caps were exceeded: 6
- Brain/Web stage row was promoted despite blockers
- brain stage promotion verdict is not PROMOTION_APPLIED: FAIL_UNSAFE_PROMOTION
- Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

수치:

```text
full_thesis_seed_planner_run_count: 111
full_thesis_seed_real_provider_success_count: 105
full_thesis_seed_source_task_execution_count: 745
full_thesis_seed_accepted_claim_count: 57
attempt_real_document_fetched_count: 595
attempt_accepted_claim_count: 57
web_fetched_document_count: 23
llm_claim_extractor_attempt_count: 37
llm_extracted_accepted_claim_count: 0
web_or_llm_accepted_claim_count: 0
source_task_budget_cap_exceeded_count: 6
```

해석:

```text
source execution 자체는 돌았다.
하지만 web/LLM route에서 accepted claim이 아직 0이다.
일부 row는 blocker가 있는데도 promotion trace가 생겨 unsafe promotion으로 막혔다.
```

쉬운 예:

```text
검사실까지는 갔다.
공식 서류/캐시/기존 ledger에서는 일부 서류가 접수됐다.
하지만 "웹/LLM이 새로 읽어 증거 claim을 만들었다"는 칸은 아직 비어 있다.
그래서 운영 합격증을 줄 수 없다.
```

## Full Thesis Production 상태

`full_thesis_production_audit.json` 기준:

```text
status: PENDING_FULL_THESIS_PRODUCTION
production_full_thesis_row_count: 4
production_pass_allowed: false
production_symbols: 003380, 005930, 047810, 052400
required_positive_missing_primitives rows: 4/4
green_gap_primitives rows: 4/4
```

이전 C05 10개보다 production row 수는 줄었고 삼성전자 `005930`은 production row에 올라왔다. 하지만 4개 전부 required-positive와 Green gap이 남아 있으므로 meaningful pass가 아니다.

## R13 validator blocker

이번 run에서 R13 실패가 6건 발생했다.

실패 메시지:

```text
R13 primary is only allowed for explicit red-team events
```

실제 실패 seed:

```text
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  primitive_gap:
    - restatement_risk
    - auditor_or_disclosure_risk
    - share_count_drift

R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  primitive_gap:
    - high_mae_history
    - liquidity_or_microcap_risk
    - valuation_overheat
```

원인:

```text
Goal4 follow-up seed가 raw_reason_codes와 event_summary에 R13_CROSS_ARCHETYPE_*를 명시했는데,
validator는 일부 redteam/false-positive 표현만 explicit R13으로 인정했다.
```

패치:

```text
src/e2r/research_brain/v4_planner_runtime.py
src/e2r/research_brain/v3_llm_planner_provider.py

event text에 "r13_cross_archetype"가 있으면 explicit R13 follow-up으로 인정
```

주의:

```text
이건 R13을 아무 종목에 강제하는 하드코딩이 아니다.
Goal4 source route/materialization seed가 명시적으로 R13_CROSS_ARCHETYPE_*를 들고 있는 경우만 허용한다.
```

## 아직 완료가 아닌 이유

Goal4 완료 조건은 다음이다.

```text
C05 외 C01~C32/C36 전체에 대해:
- attempt 존재
- source route 존재
- source execution 존재
- accepted claim 존재
- full thesis 상태가 전수 matrix로 증명됨
```

이번 run이 증명한 것:

```text
attempt/planner 다양성: 개선됨
source execution 진입: 개선됨
accepted claim: 일부 있음
meaningful full thesis: 미완료
web/LLM accepted claim: 0
production full thesis: pending
R13 overlay validator: 일부 실패
```

따라서 Goal4는 계속 active다.

## 다음 작업

```text
1. R13_CROSS_ARCHETYPE_* explicit follow-up seed validator 패치
2. 해당 회귀 테스트 추가
3. brain_web_readiness_gate blockers를 source route별로 분해
4. web/LLM accepted claim이 0인 이유 확인
5. unsafe promotion trace 5건을 blocker-aware pending으로 바꿈
6. clean root에서 다시 runtime attempt 실행
```

