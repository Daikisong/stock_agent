# Census v4 0701 Subagent Feedback Fixes And Current NOT_READY Truth

작성일: 2026-07-01  
기준 repo: `/home/eorb915/projects/stock_agent`

## 한 줄 결론

```text
Stage label은 있다.
하지만 최신 enabled Brain/Web smoke에서도 운영 확정 Stage는 없다.
```

최신 smoke 기준:

```text
output root:
/tmp/census_v4_enabled_provider_probe_after_success_limit_fix

exit:
NOT_READY

census_stage_status rows:
3391

canonical_stage:
0      3306
1        54
2        30
3-Red     1

stage_scope:
CENSUS_EVENT_BOARD 3391
BRAIN_WEB_PARTIAL     0
FULL_THESIS           0

Brain/Web accepted claim:        0
Brain/Web score contribution:    0
Brain/Web StageCourt trace:      0
Brain/Web promoted stage row:    0
```

쉬운 예:

```text
현재 Stage1
= "출석부/이벤트 상태판에서 Stage1처럼 보이는 row"

아직 아닌 것
= "해당 종목의 전체 thesis를 원문 claim으로 채워서 Stage1로 확정한 row"
```

따라서 "Stage가 있는 종목이 있긴 하냐"에 대한 정확한 답은 아래다.

```text
있다: event-board Stage label은 있다.
없다: Brain/Web claim-backed 운영 Stage와 full thesis Stage는 없다.
```

## 이번에 고친 것

이번 패치는 score weight, Stage threshold, 종목별 예외를 건드리지 않았다.  
목표는 "틀린 Stage를 더 잘 만들기"가 아니라 "가짜 Stage를 막고 병목을 정확히 보이게 하기"였다.

### 1. Fetch 본문 target guard 강화

파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
```

기존 위험:

```text
검색 제목/스니펫에는 삼성전자가 있음
실제 fetch 본문에는 월덱스 감사의견만 있음
→ 검색 메타만 보고 extractor로 넘길 수 있음
```

수정:

```text
fetch 본문 자체에 target alias가 없으면 거절한다.
본문 앞 lead에도 target alias가 있어야 통과한다.
검색 title/snippet만으로는 통과하지 못한다.
```

새 회귀 테스트:

```text
test_live_full_bounded_rejects_search_metadata_target_when_fetched_body_lacks_target
```

쉬운 예:

```text
택배 송장에는 "삼성전자"라고 적혀 있는데
상자를 열어보니 월덱스 감사보고서만 들어 있으면
삼성전자 점수 재료로 쓰면 안 된다.
```

단, 이 guard는 1차 필터다.  
본문에 target 이름이 있어도 "고객사/공급사/비교 대상" 언급일 수 있으므로, 최종 direct subject 판정은 adjudicator가 계속 해야 한다.

### 2. Rejected mapping trace의 score_eligible 표기 수정

파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_bundle_export.py
```

기존 위험:

```text
accepted=false인 rejected mapping row가
eligibility_reasons만 비어 있으면 score_eligible=true처럼 보일 수 있었다.
```

수정:

```text
score_eligible = accepted and not eligibility_reasons
```

즉 rejected row는 어떤 경우에도 score-eligible처럼 보이지 않는다.

### 3. Brain Stage promotion trace chain 강화

파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
```

보강한 감사:

```text
brain_to_claim_trace의 promoted census_stage_status_id가
실제 stage row의 claim_id,
score_contribution_id,
primitive_state_id와 모두 맞아야 한다.
```

새 회귀 테스트:

```text
test_promoted_brain_trace_reference_mismatch_is_unsafe
test_brain_partial_stage_without_atomic_id_uses_stage_primitive_chain
```

쉬운 예:

```text
"10점 영수증"은 claim A에서 왔다고 하는데
대표 Stage row는 contribution B를 가리키면
그 Stage row는 통과하면 안 된다.
```

### 4. planner_success_limit 의미 수정

파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
```

기존 위험:

```text
--brain-planner-success-limit 2

앞의 후보 2개가 validator에서 rejected
→ 실제 real_provider_success=0이어도
→ 뒤 후보를 더 보지 않고 종료
```

수정:

```text
validator reject / output missing / provider failure는 성공으로 세지 않는다.
real_provider_success 개수가 success_limit에 도달할 때까지 다음 후보를 계속 본다.
```

새 회귀 테스트:

```text
test_real_planner_success_limit_skips_failed_attempts_and_continues
```

쉬운 예:

```text
시험지 2장을 채점하라는 뜻이 아니라
정답 2개를 찾을 때까지 문제를 넘겨보라는 뜻이다.
오답은 오답으로 기록하지만, 오답 2개가 나왔다고 시험을 종료하면 안 된다.
```

## 최신 enabled smoke 명령

```bash
rm -rf /tmp/census_v4_enabled_provider_probe_after_success_limit_fix && \
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root /tmp/census_v4_enabled_provider_probe_after_success_limit_fix \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 8 \
  --brain-planner-success-limit 2 \
  --brain-planner-batch-size 2 \
  --brain-max-fetches-per-task 2 \
  --brain-claim-extractor-provider auto \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --fail-on-critical-audit true \
  --write-operational-docs false
```

결과:

```text
exit code: 1
stdout: NOT_READY
```

중요한 점:

```text
이번에는 RuntimeError가 아니라 정상적인 NOT_READY다.
leaf_artifact_audit는 PASS이고 critical_count=0이다.
```

## 최신 smoke 핵심 숫자

```text
planner_runs:              24
real_provider_success:      4
source_tasks:             110
source_task_executions:   110
web_search_tasks:          11
web_search_results:        72
web_fetched_documents:     18
web_rejected_documents:    10
claim_extractor_runs:      18
brain_claim_mapping_trace: 228
brain_to_claim_trace:       0
Brain/Web accepted claim:   0
Brain/Web promoted row:     0
```

감사 결과:

```text
leaf_artifact_audit:
  PASS, critical_count=0

primitive_state_chain_audit:
  PASS, critical_count=0

brain_planner_audit:
  PASS

web_naver_acquisition_audit:
  REAL_ACQUISITION_PASS

llm_claim_extraction_audit:
  REAL_EXTRACTION_PASS

brain_web_attempt_audit:
  ATTEMPTED_NOT_CUTOVER_READY
  blocker: Research Brain source tasks produced no accepted claims

brain_stage_promotion_audit:
  BLOCKED
  blockers:
    accepted brain claim count is zero
    brain score contribution count is zero
    brain StageCourt trace count is zero

brain_web_readiness_gate_audit:
  BLOCKED
  blockers:
    web/LLM accepted claim count is zero
    Brain/Web StageCourt traces are not promoted into census_stage_status
    brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED

readiness_verdict:
  NOT_READY
```

## 이번 smoke가 이전보다 나아진 점

이전에는 아래처럼 더 앞에서 막혔다.

```text
LLM/Web을 했다고 metadata는 말하는데
real provider success/search row가 0
→ leaf_artifact_audit FAIL
→ RuntimeError
```

success-limit 패치 후에는 실제로 아래까지 진행됐다.

```text
LLM planner success
→ web search
→ full page fetch
→ LLM contract-blind claim extraction
→ rejected mapping trace 228개
```

그래서 병목이 명확해졌다.

```text
이전 병목:
  planner 실패 후보 두 개에서 실행 종료

현재 병목:
  문서와 raw assertion은 생기지만 accepted claim으로 닫히지 않음
```

## 아직 안 되는 핵심 이유

### 1. Brain/Web accepted claim이 0개다

최신 mapping trace:

```text
accepted=false / REJECTED_BEFORE_SCORE: 228개
accepted=true: 0개
```

상위 거절 사유:

```text
mapping_not_accepted:REJECTED                                  228
primitive_mapping_rejected:no_allowed_primitive_for_predicate   221
semantic_rejected                                               115
target_scope_not_allowed:UNRELATED                              115
target_not_direct:NOT_TARGET_SCOPED                             115
primitive_mapping_rejected:adjudication_not_passed              115
quote_not_found_in_document_text                                 42
```

이건 "검색이 전혀 안 됨" 문제가 아니다.  
이제는 "증거 문장을 실제 아키타입 primitive로 안전하게 받아들이는 단계"가 막힌 것이다.

### 2. 근거가 있어도 primitive 슬롯이 맞지 않으면 전부 거절된다

예시: 그린생명과학 `114450`

실제 원문에는 아래가 있었다.

```text
단일판매ㆍ공급계약체결
계약금액 10,238,670,000원
최근 매출액 대비 41.18%
계약상대방 UPL Limited
```

하지만 planner가 연 task는 C29의 아래 primitive였다.

```text
volume_growth_visible
operating_leverage_visible
```

추출된 claim은 계약 품질/매출 가시성 쪽으로 보였고, 현재 task primitive와 맞지 않아 거절됐다.

쉬운 예:

```text
서류는 "공급계약서"인데
접수창구가 "생산량 증가 증명서"라서 반려된 상태다.
```

다음 패치는 둘 중 하나를 해야 한다.

```text
1. accepted로 억지 통과
   → 안 됨. 또 가짜 점수 위험.

2. claim이 현재 task primitive와 다르면
   contract registry 안에서 맞는 primitive/archetype으로 reroute하거나
   planner에게 "계약 claim을 volume_growth로 열어서 반려됨" 피드백을 넘겨 재계획
   → 이게 맞음.
```

### 3. SK하이닉스는 HBM/C06 smoke가 아니었다

최신 real planner success의 SK하이닉스는 아래 이벤트였다.

```text
event:
SK하이닉스 ADR / 유상증자 / 제3자배정 관련 CompanyGuide radar

primary archetype:
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

즉 이 smoke의 SK하이닉스는 "HBM/C06 full thesis 운영 Stage"가 아니다.  
종목명은 같지만 평가 대상 이벤트가 다르다.

쉬운 예:

```text
하이닉스라는 학생은 시험장에 왔지만
HBM 과목 시험을 본 게 아니라
지배구조/ADR 과목 문제를 본 상태다.
```

삼성전자도 최신 success-limit smoke에서는 real planner success까지 가지 않았다.  
success-limit 2가 채워진 뒤 나머지는 `planner_not_attempted_after_real_planner_limit`로 남았다.

따라서 이 smoke를 삼성전자/하이닉스 HBM Stage 평가로 읽으면 안 된다.

## 다음 패치 방향

### P0. Accepted claim을 억지로 늘리지 않는다

지금 당장 해서는 안 되는 패치:

```text
no_allowed_primitive_for_predicate를 무시하고 accepted=true
target_scope_not_direct를 완화
quote_not_found를 무시
Stage threshold/score weight 완화
종목명 예외 추가
```

이렇게 하면 월덱스/삼성전자 같은 오귀속 문제가 다시 생긴다.

### P1. Primitive/archetype reroute ledger

필요한 동작:

```text
raw claim은 DIRECT/PASS/CURRENT인데
현재 task primitive와만 안 맞아 rejected된 경우
→ accepted로 올리지 말고
→ "reroute proposal"로 별도 ledger에 남긴다.
```

예:

```json
{
  "claim_id": "CLM-...",
  "current_task_primitive": "volume_growth_visible",
  "mapped_predicate": "supply_contract_amount_to_sales",
  "proposed_primitive": "revenue_visibility_contract",
  "proposed_archetype_options": ["C05", "C01"],
  "action": "planner_feedback_required",
  "score_eligible": false
}
```

중요:

```text
reroute proposal은 점수 재료가 아니다.
다음 planner 입력/재조사 입력이다.
```

### P2. Planner feedback에 rejected primitive mismatch를 넣는다

현재 feedback은 claim-level rejection을 일부 넘기지만, 다음 planner가 아래를 명확히 알 수 있어야 한다.

```text
이 문서에서 계약 claim은 찾았다.
하지만 C29 volume_growth_visible로는 못 받았다.
계약/매출가시성 primitive 또는 다른 archetype을 검토해라.
```

LLM에게 시킬 일:

```text
현재 문서를 억지로 점수화하지 말고,
동일 claim을 어떤 evidence contract로 다시 열어야 하는지 계획한다.
```

### P3. Source ranking / direct-subject pruning 강화

최신 smoke에서 web fetch는 18개였지만 일부는 아래처럼 잡음이 컸다.

```text
티스토리 상승률 정리
뉴스1 기자 페이지
타종목 시장 페이지
```

fetch 후 target guard가 일부 막더라도, 애초에 fetch 후보 rank에서 줄여야 한다.

필요한 개선:

```text
title/snippet/source URL만이 아니라
검색결과 rank 전에 official/source family를 우선
블로그/시장페이지/저자페이지 같은 low-signal page class 감점
동일 underlying event duplicate dedupe
source task별 stop-on-resolution 강화
```

단, 이것도 종목별 예외가 아니라 source/task 품질 규칙이어야 한다.

### P4. Full thesis smoke를 별도로 실행해야 한다

삼성전자/하이닉스 HBM을 보려면 daily event-board 후보가 아니라 별도 full thesis SourceTask가 필요하다.

필요한 명령/상태:

```text
symbol: 005930, 000660
thesis: C06/HBM full thesis
as_of_date: 2026-07-01
mode: full_thesis or explicit Samsung/Hynix C06 smoke
output: verified_score / provisional_score / material_gap / stage_scope=FULL_THESIS
```

현재 `census_stage_status`의 Stage1/Stage2를 이 값으로 대체하면 안 된다.

## 교차검증에서 확인한 사항

Subagent/자체 cross-check에서 잡힌 항목과 반영 상태:

```text
1. 검색 metadata target만으로 fetch body를 통과시키던 위험
   → body/lead target guard와 회귀 테스트 추가.

2. brain_to_claim_trace promoted reference 자체를 critical로 보던 audit 의미 오류
   → 참조 자체는 허용, dangling/mismatch만 critical.

3. contribution/primitive mismatch는 아직 안 잡던 위험
   → contribution_id, primitive_state_id subset 검증 추가.

4. BRAIN_WEB_PARTIAL row는 AtomicStageDecision id가 없을 수 있는데 primitive chain audit가 실패할 수 있던 위험
   → BRAIN_WEB_PARTIAL은 stage row primitive chain으로 검증.

5. rejected mapping row가 score_eligible처럼 보일 수 있던 표기 위험
   → accepted and no eligibility reasons일 때만 score_eligible.

6. planner_success_limit가 실패 attempt limit처럼 동작하던 위험
   → real_provider_success count 기준으로 다음 후보를 계속 봄.
```

## 검증

좁은 회귀:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_primitive_state_chain -v

Ran 41 tests
OK
```

넓은 Brain/Web 주변 회귀:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_planner_provider \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_provider_failure_pending \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_bundle_export \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_primitive_state_chain \
  tests.test_census_v4_source_task_satisfaction_chain -v

Ran 92 tests
OK
```

전체 테스트:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 4972 tests in 157.577s
OK

log:
/tmp/stock_agent_full_tests_after_0701_stage_truth_fixes.log
```

## 최종 판정

현재 상태는 아래처럼 부르는 것이 가장 정확하다.

```text
ANTI_FAKE / TRACE_GUARD strengthened
REAL_PLANNER_WEB_EXTRACTOR attempted
MAPPING_TO_ACCEPTED_CLAIM not ready
BRAIN_WEB_STAGE not ready
FULL_THESIS_STAGE not run
```

완료라고 말하면 안 되는 것:

```text
운영 Stage 완성
삼성전자/하이닉스 HBM Stage 판정
Brain/Web accepted claim path 완성
full thesis verified score 완성
```

다음 에이전트가 가장 먼저 공격해야 할 질문:

```text
1. DIRECT/PASS/CURRENT raw claim이 현재 task primitive mismatch 때문에 rejected될 때,
   reroute ledger와 planner feedback이 정확히 생기는가?

2. reroute proposal이 점수로 새지 않는가?

3. 그린생명과학 계약 공시 같은 실제 계약 claim이
   맞는 evidence contract로 다시 열렸을 때 accepted claim까지 닫히는가?

4. 삼성전자/하이닉스 HBM은 daily event-board가 아니라
   C06 full thesis smoke로 별도 실행되고 있는가?

5. web source ranker가 target 이름만 있는 저품질/중복/저자 페이지를
   fetch 예산 전에 충분히 낮추는가?
```

