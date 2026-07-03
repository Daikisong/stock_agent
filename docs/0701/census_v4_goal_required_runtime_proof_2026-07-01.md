# Census v4 Goal-Required Runtime Proof - 2026-07-01

이 문서는 `goal.md`, `goal2.md`, `goal3.md`가 요구한 런타임 증거 장부가 현재 v4에 어디까지 반영됐는지 따로 정리한 것이다.

## 결론

```text
통과한 것:
  anti-fake / ledger-refresh runtime proof

아직 통과하지 않은 것:
  live Brain/Web/LLM source acquisition
  full E2R 100점 verified score
  전 아키타입 full thesis replay parity
  삼성전자/하이닉스 C06 full thesis smoke 실행

새로 생긴 planning-only 장부:
  full_thesis_smoke_tasks.jsonl
  row_count=14
  hardcoded_query_count=0
  score_allowed_before_execution=false
```

쉬운 예:

```text
현재는 기존 채점지 67장을 다시 꺼내서
"점수 row -> claim -> source/timeline -> trace"가 맞는지 검산했다.

아직 오늘 새로 raw universe 3940개 중 eligible/stage 대상 3391개를 모두 full thesis 조사해서
100점 만점 종합 성적표를 만든 것은 아니다.
```

## 추가된 runtime proof 파일

Canonical output:

```text
output/census_v4/2026-07-01/claim_to_stage_forensic_audit.json
output/census_v4/2026-07-01/source_task_realness_audit.json
output/census_v4/2026-07-01/existing_ledger_reuse_audit.json
output/census_v4/2026-07-01/last_effective_thesis_audit.json
output/census_v4/2026-07-01/source_coverage_audit.json
output/census_v4/2026-07-01/runtime_plausibility_audit.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
```

Docs copy:

```text
docs/operational/census_mode_v4_claim_to_stage_forensic_audit.json
docs/operational/census_mode_v4_source_task_realness_audit.json
docs/operational/census_mode_v4_existing_ledger_reuse_audit.json
docs/operational/census_mode_v4_last_effective_thesis_audit.json
docs/operational/census_mode_v4_source_coverage_audit.json
docs/operational/census_mode_v4_runtime_plausibility_audit.json
docs/operational/census_mode_v4_brain_web_readiness_gate_audit.json
```

Reviewer aliases:

```text
docs/operational/census_mode_v4_reviewer_A_trace_forensics.json
docs/operational/census_mode_v4_reviewer_D_runtime_plausibility.json
```

## 파일별 의미

### 1. claim_to_stage_forensic_audit

묻는 질문:

```text
점수 row가 claim id, score contribution id, StageCourt trace id를 실제 장부에서 찾을 수 있는가?
```

현재값:

```text
verdict: PASS
critical_count: 0
scored_row_count: 67
stage2plus_or_risk_row_count: 36
```

주의:

```text
stage2plus_or_risk_row_count = 36
는 event_board_stage2plus_or_risk_label_count로 읽어야 한다.

full thesis Stage2+ count가 아니다.
현재 full thesis Stage row count는 0이다.
```

중요한 0:

```text
scored_row_missing_claim_ids: 0
scored_row_missing_score_contribution_ids: 0
scored_row_missing_stagecourt_trace: 0
claim_id_not_found_count: 0
score_contribution_id_not_found_count: 0
stagecourt_trace_id_not_found_count: 0
support_claim_not_accepted_count: 0
source_proxy_support_claim_count: 0
provider_failed_final_score_count: 0
source_pending_marked_red_count: 0
```

쉬운 예:

```text
성적표에 4점이 있으면
그 4점이 어떤 채점 항목이고,
어떤 근거 문서 claim 때문에 붙었는지 번호표가 있어야 한다.
```

주의:

```text
census_stage_status row의 accepted_claim_ids / score_contribution_ids는
claim_to_stage_trace row의 집계 목록 전체와 항상 1:1 동일하다는 뜻이 아니다.

대표 row에는 대표 stage decision에 필요한 id가 들어가고,
claim_to_stage_trace에는 같은 symbol의 더 넓은 trace 집계가 들어갈 수 있다.

통과 조건은 "대표 id가 trace/ledger 안에서 실제로 발견되는가"이지,
"두 목록이 글자 그대로 같은가"가 아니다.
```

쉬운 예:

```text
성적표에는 최종 채점에 쓴 답안 번호 1개가 적혀 있고,
감사 장부에는 그 학생에게 검토된 관련 답안 번호 여러 개가 함께 적혀 있을 수 있다.
중요한 것은 성적표 번호가 감사 장부 안에서 사라지지 않는 것이다.
```

### 2. source_task_realness_audit

묻는 질문:

```text
이번 run의 source task는 live fetch였는가, cache/ledger 재검산이었는가?
```

현재값:

```text
verdict: PASS_LEDGER_REFRESH_REALNESS
verdict_scope: LEDGER_REFRESH_REALNESS_PASS
live_source_pass_allowed: false
critical_count: 0
source_task_planned_count: 92
source_task_execution_count: 92
source_task_claim_producing_count: 60
source_task_real_fetch_count: 0
source_task_fresh_provider_cache_count: 60
source_task_lifecycle_refresh_count: 32
classification_distribution:
  FRESH_PROVIDER_CACHE: 60
  EXISTING_ACCEPTED_CLAIM_LIFECYCLE_REFRESH: 32
```

해석:

```text
현재 canonical run은 live web/API fetch pass가 아니다.
기존 source-backed ledger/cache를 재검산한 run이다.
```

스코프 주의:

```text
source_task_realness_audit.source_task_execution_count = 92
  -> ledger-refresh / 기존 Evidence OS leaf 재검산 task 수

brain_web_readiness_gate.source_task_execution_count = 0
  -> 이번 canonical run에서 새로 실행한 Brain/Web live source task 수

둘은 같은 이름처럼 보이지만 범위가 다르다.
```

보조 source task satisfaction 현재값:

```text
verdict: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
verdict_scope: LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS
live_source_task_satisfaction_pass_allowed: false
baseline_only_score_claim_count: 32
```

뜻:

```text
ledger-refresh 범위에서는 source task 만족성 감사가 실패하지 않았다.
하지만 live SourceTask -> EvidenceDocument -> AcceptedClaim -> ScoreContribution -> StageCourt 전체 id-chain이 닫혔다는 뜻은 아니다.
```

주의:

```text
source_task_executions.jsonl 원시 row에는
candidate_event_id=CE-LIVE-DART-*
budget_used.fetches=1
fetched_document_ids
document_urls
같은 필드가 남아 있을 수 있다.

이 필드만 보면 live fetch처럼 보일 수 있지만,
현재 canonical run에서는 source_task_execution_origin=production_cutover_v3_leaf_artifact이고
source_task_realness_audit.source_task_real_fetch_count=0이다.
source_task_realness_audit.live_source_pass_allowed=false이다.

따라서 원시 row의 fetch 모양 필드를 live operation pass로 읽으면 안 된다.
```

쉬운 예:

```text
도서관에 새 책을 가지러 간 것이 아니라,
이미 보관된 원본 서류철을 다시 꺼내 번호와 날짜를 확인한 것이다.
```

### 3. existing_ledger_reuse_audit

묻는 질문:

```text
기존 claim을 그냥 복사했는가, 아니면 source locator와 lifecycle을 다시 연결했는가?
```

현재값:

```text
verdict: PASS
critical_count: 0
v3_leaf_imported_claim_count: 92
reused_claim_count: 92
lifecycle_refreshed_reused_claim_count: 92
reused_claim_in_claim_to_stage_trace_count: 92
reused_claim_in_representative_stage_count: 67
new_brain_web_claim_count: 0
```

중요한 0:

```text
existing_claim_without_source_locator_count: 0
lifecycle_refresh_missing_count: 0
previous_stage_blind_copy_count: 0
reused_claim_not_in_trace_count: 0
stale_claim_reused_current_count: 0
```

쉬운 예:

```text
작년 서류를 그대로 붙인 게 아니라,
서류 번호와 현재성 갱신 도장을 다시 확인한 것이다.
```

### 4. last_effective_thesis_audit

묻는 질문:

```text
전 종목에 현재 상태판이 붙었는가?
Stage0/NoCurrentCatalyst도 아무 근거 없이 만든 더미가 아닌가?
```

현재값:

```text
verdict: PASS
critical_count: 0
last_effective_thesis_count: 3391
source_timeline_count: 3391
status_distribution:
  NO_KNOWN_THESIS: 3306
  ACTIVE_THESIS: 74
  SOURCE_PENDING: 8
  NEEDS_REFRESH: 3
```

쉬운 예:

```text
모든 종목에 "평가 이벤트"는 붙었다.
하지만 모든 종목에 "사업 트리거"가 생겼다는 뜻은 아니다.

아무 새 이벤트가 없으면:
  CensusAssessmentEvent 있음
  CandidateEvent 없음
  Stage0 / NoCurrentCatalyst
```

### 5. source_coverage_audit

묻는 질문:

```text
source coverage를 어디까지 주장하는가?
live full-source pass라고 과장하지 않는가?
```

현재값:

```text
verdict: PASS_LEDGER_REFRESH_COVERAGE
critical_count: 0
accepted_claim_count: 92
reused_or_imported_claim_count: 92
newly_verified_claim_count: 0
provider_cache_used_count: 92
cutover_replay_only_symbol_count: 67
operational_live_source_coverage_pass: false
```

중요한 0:

```text
symbol_without_any_census_time_source_attempt_count: 0
source_proxy_production_claim_count: 0
stale_cache_used_count: 0
```

해석:

```text
전 종목 source family attempt 흔적은 있다.
하지만 새 live fetch로 full thesis claim을 만든 것은 아니다.
```

쉬운 예:

```text
출석 확인은 전원 했다.
하지만 전원에게 새 시험지를 풀린 것은 아니다.
```

### 6. runtime_plausibility_audit

묻는 질문:

```text
runtime 숫자와 실행 주장 사이에 모순이 없는가?
```

현재값:

```text
verdict: PASS_LEDGER_REFRESH_RUNTIME_HONESTY
critical_count: 0
runtime_mode: LEDGER_REFRESH
run_mode: LEDGER_REFRESH_CENSUS
runtime_seconds: 약 0.3~1.5초
provider_call_count: 0
llm_call_count: 0
web_search_task_count: 0
web_fetched_document_count: 0
evidence_extraction_count: 0
source_task_real_fetch_count: 0
```

해석:

```text
짧은 runtime과 provider/LLM 0회가 서로 일치한다.
이 숫자로 live web/LLM acquisition pass를 주장하면 실패다.
```

### 7. brain_web_readiness_gate_audit

묻는 질문:

```text
Brain/Web 개별 감사가 0건 PASS처럼 보이더라도,
실제로 Brain/Web evidence pass를 주장할 수 있는가?
```

현재값:

```text
verdict: NOT_REQUESTED
minimum_gate_applies: false
brain_web_evidence_pass_allowed: false
llm_planner_call_count: 0
llm_real_provider_success_count: 0
source_task_execution_count: 0
real_document_fetched_count: 0
web_search_task_count: 0
web_fetched_document_count: 0
llm_claim_extractor_attempt_count: 0
web_or_llm_accepted_claim_count: 0
brain_to_claim_trace_count: 0
brain_score_contribution_count: 0
brain_stage_trace_count: 0
brain_promoted_stage_row_count: 0
brain_trace_missing_accepted_claim_count: 0
brain_trace_missing_score_contribution_ref_count: 0
brain_trace_missing_stagecourt_ref_count: 0
brain_contribution_without_accepted_support_count: 0
brain_stage_trace_without_accepted_claim_count: 0
promoted_stage_without_brain_trace_count: 0
blockers: []
```

해석:

```text
현재 canonical run은 Brain/Web을 요청하지 않았다.
따라서 위 연결성 지표가 0인 것은 "Brain/Web claim이 잘 연결됐다"는 뜻이 아니라,
연결할 Brain/Web claim 자체가 0개라는 뜻이다.

enabled run에서는 accepted claim, trace, score contribution, StageCourt trace, promoted row의 claim ID가 모두 이어져야 하며,
하나라도 어긋나면 `BLOCKED`가 맞다.
따라서 NOT_REQUESTED가 맞고, BRAIN_WEB_EVIDENCE_PASS는 금지된다.
```

쉬운 예:

```text
시험을 안 본 학생은 "결시"다.
"틀린 문제가 없으니 합격"이 아니다.
```

## 한 번에 검증하는 명령

```bash
python - <<'PY'
import json
root="output/census_v4/2026-07-01/"
names=[
  "claim_to_stage_forensic_audit.json",
  "source_task_realness_audit.json",
  "existing_ledger_reuse_audit.json",
  "last_effective_thesis_audit.json",
  "source_coverage_audit.json",
  "runtime_plausibility_audit.json",
  "brain_web_readiness_gate_audit.json",
]
for name in names:
    obj=json.load(open(root + name))
    if name == "brain_web_readiness_gate_audit.json":
        print(name, obj.get("verdict"), "pass_allowed", obj.get("brain_web_evidence_pass_allowed"))
    else:
        print(name, obj.get("verdict"), "critical_count", obj.get("critical_count"))
PY
```

기대값:

```text
claim_to_stage_forensic_audit.json PASS critical_count 0
source_task_realness_audit.json PASS_LEDGER_REFRESH_REALNESS critical_count 0
source_task_satisfaction_audit.json PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION critical_count 0 warning_count 25 live_pass_allowed false
primitive_state_chain_audit.json PASS critical_count 0 primitive_mapping_count 92 representative_score_claim_with_primitive_state_count 67
existing_ledger_reuse_audit.json PASS critical_count 0
last_effective_thesis_audit.json PASS critical_count 0
source_coverage_audit.json PASS_LEDGER_REFRESH_COVERAGE critical_count 0
runtime_plausibility_audit.json PASS_LEDGER_REFRESH_RUNTIME_HONESTY critical_count 0
brain_web_readiness_gate_audit.json NOT_REQUESTED pass_allowed false
```

## Seven Audits Do Not Cover

위 7개 감사는 goal1의 anti-fake/runtime proof 범위를 주로 닫는다.
다음 항목은 아직 별도 hard gate로 남아 있으며, 이 항목이 닫히기 전에는 goal completion을 말할 수 없다.

```text
1. Real Brain/Web 최소 실행 수량
2. Web/Naver/News full-source fetch와 snippet-score 차단
3. LLM claim extractor 실제 attempt/accepted/rejected trace
4. Samsung/Hynix C06/HBM full thesis smoke 실행
5. Brain/Web promoted claim의 document/anchor/date/target/current 검증
6. 대표 row 밖 25개 SourceTask claim의 exclusion reason 세분화와 live/full-thesis chain 적용
7. reviewer A/B/C/D/E의 독립 재계산
8. existing ledger reuse의 supersession/contradiction/as_of freshness 검증
```

따라서 이 문서의 7개 감사 PASS만으로는 아래 label을 줄 수 없다.

```text
MEANINGFUL_OPERATIONAL_STAGE_PASS
BRAIN_WEB_EVIDENCE_PASS
FULL_THESIS_SMOKE_PASS
```

현재는 별도 deterministic suite로 `KNOWN_BAD_REGRESSION_PASS`가 닫혔다.
이 문서의 7개 감사만으로 닫힌 것이 아니라, `known_bad_regression_report.json`의 `status=PASS`, `case_count=10`, `failed_case_count=0`이 근거다.

현재는 별도 `self_repair_log.json`으로 `SELF_REPAIR_LOOP_PASS`도 닫혔다.
근거는 `status=RUN_COMPLETE`, `final_status=PASS`, `loop_executed=true`, `unresolved_failures=[]`다.
단 이 pass는 Brain/Web/full-thesis pending을 대신 닫지 않는다.

쉬운 예:

```text
7개 감사는 "서류철이 비어 있지 않고 번호가 맞는가"를 본다.
known-bad와 self-repair는 "일부러 망가진 서류를 넣었을 때 잡아내고 고쳤는가"를 본다.
둘은 서로 다른 시험이다.
```

P0 코드 패치 후보:

```text
1. 구현됨: source_task_realness verdict를 PASS_LEDGER_REFRESH_REALNESS와 LIVE_SOURCE_PASS로 분리
2. 구현됨: runtime_plausibility verdict를 PASS_LEDGER_REFRESH_RUNTIME_HONESTY처럼 범위 포함 이름으로 변경
3. 구현됨: CLI에 --target-gate를 추가해 anti_fake exit 0과 meaningful/full_thesis exit 0을 분리
4. 구현됨: test_result_summary 문자열 대신 e2r_test_result_artifact_v1 JSON artifact hash/path를 검증
5. 구현됨/유지 필요: BRAIN_AND_WEB_ACQUISITION_ENABLED에서는 web/search/fetch 최소조건을 accepted claim shortcut으로 우회하지 못하게 변경
```

## 다음 리뷰어가 공격해야 할 지점

```text
1. source_task_real_fetch_count=0인데 live source pass라고 쓰인 문서가 있는가?
2. newly_verified_claim_count=0인데 새 Brain/Web claim pass라고 주장하는가?
3. operational_live_source_coverage_pass=false인데 production full operation ready라고 말하는가?
4. full_e2r_verified_score_present_count=0인데 full thesis Stage라고 말하는가?
5. Stage2-Watch/Red label을 canonical Stage enum이나 full thesis Stage로 섞었는가?
6. runtime_seconds가 1초 안팎인데 LLM extraction을 했다고 주장하는가?
7. 기존 ledger claim 92개를 재사용할 때 source locator와 lifecycle 확인 없이 blind copy했는가?
8. source pending row를 낮은 Red/4C로 확정했는가?
9. Brain StageCourt trace가 strict promotion 없이 representative row로 올라갔는가?
10. brain_web_readiness_gate가 NOT_REQUESTED 또는 BLOCKED인데 Brain/Web pass를 주장하는가?
11. docs/operational copy와 output canonical copy가 서로 다르게 오염됐는가?
```

## 다음 패치 방향

```text
P0:
  현재 anti-fake / ledger-refresh 감사는 유지한다.

P1:
  production SourceTask를 실제 provider fetch / official-first / bounded budget으로 연결한다.

P2:
  fetched source에서 EvidenceDocument -> EvidenceAnchor -> RawAssertion -> EvidenceClaim을 만든다.

P3:
  accepted claim만 PrimitiveState / ScoreContribution / StageCourt에 넣는다.

P4:
  Brain/Web StageCourt trace를 strict promotion audit 통과 후에만 representative census_stage_status row에 반영한다.

P5:
  삼성전자/하이닉스 C06 full thesis smoke task 14개를 event score와 분리해서 실행한다.
  현재는 task 계획서만 있고 accepted full thesis claim/score/stage는 없다.

P6:
  전 아키타입 Evidence Contract v2와 source-backed replay parity를 닫는다.
```

현재 문서의 가장 중요한 문장:

```text
트리거는 조사를 여는 문이고,
claim만 점수를 여는 열쇠다.
```
