# Census v4 Claim Extractor Provider Patch And Review Packet - 2026-07-01

이 문서는 다음 에이전트가 바로 강하게 리뷰할 수 있도록 만든 최신 패치/검증 패킷이다.

최신성 주의:

```text
이 문서는 claim extractor provider auto-selection 패치 당시의 4954개 테스트 artifact를 기록한다.
그 이후 enabled Brain/Web smoke와 로컬 전체 테스트 4959개 OK 기준은 아래 문서를 우선한다.

docs/0701/census_v4_0701_enabled_brainweb_current_truth_and_next_patch_packet_2026-07-01.md
docs/0701/census_v4_enabled_brainweb_leaf_to_claim_gap_forensic_2026-07-01.md
docs/0701/census_v4_0701_latest_truth_review_and_next_patch_plan_2026-07-01.md
```

핵심 질문:

```text
Stage가 있는 애들이 있긴 한가?
그 Stage가 진짜 운영 full thesis Stage인가?
이번 패치가 Brain/Web 운영 경로에서 무엇을 실제로 닫았나?
아직 완료라고 말하면 안 되는 지점은 어디인가?
```

## 한 줄 결론

Stage row는 있다.

하지만 최신 canonical output 기준으로도 전부 `CENSUS_EVENT_BOARD`이고, `FULL_THESIS` 운영 Stage는 0개다.

이번 패치는 `live_full_bounded + real/codex planner` 경로에서 unstructured 문서를 rule fallback이 아니라 Codex LLM claim extractor로 넘기도록 배관을 고친 것이다.

쉬운 예:

```text
이전:
  문서를 가져와도 원문 claim 작성 담당이 연습용 rule fallback일 수 있었다.

패치 후:
  live/full-bounded 운영형 실행이면 원문 claim 작성 담당을 Codex LLM extractor로 고른다.

아직 아님:
  실제 Brain/Web run이 성공해서 운영 Stage가 생긴 것은 아니다.
```

## 최신 출력 교차검증

검증 대상:

```text
output/census_v4/2026-07-01
```

최신 재검산값:

```text
stage_rows: 3391

canonical_stage:
  0: 3306
  1: 54
  2: 30
  3-Red: 1

base_stage:
  Stage0: 3306
  Stage1: 54
  Stage2-Watch: 30
  Red: 1

stage_scope:
  CENSUS_EVENT_BOARD: 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

operator_score_use:
  NOT_FULL_E2R_SCORE: 3391
```

해석:

```text
Stage label은 있다.
운영 full thesis Stage는 아직 없다.
```

틀린 말:

```text
30개 종목이 운영 Stage2다.
삼성전자/하이닉스가 운영 Stage1 4점이다.
3-Red 1개가 운영 Red 판정이다.
```

맞는 말:

```text
30개 row는 event-board Stage2-Watch label이다.
삼성전자/하이닉스는 daily event-board partial 4.0이고 full thesis score는 null이다.
3-Red 1개도 full thesis 운영 Red가 아니라 event-board label이다.
```

## 삼성전자 / 하이닉스 재검산

최신 row 기준:

```text
005930 삼성전자:
  base_stage: Stage1
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  event_evidence_score: 4.0
  daily_event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN
  full_thesis_score_valid_status: NOT_SCORED
  score_scope: EVENT_WEIGHTED_PARTIAL
  operator_stage_use: NOT_FULL_THESIS_STAGE
  operator_score_use: NOT_FULL_E2R_SCORE

000660 SK하이닉스:
  base_stage: Stage1
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  event_evidence_score: 4.0
  daily_event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN
  full_thesis_score_valid_status: NOT_SCORED
  score_scope: EVENT_WEIGHTED_PARTIAL
  operator_stage_use: NOT_FULL_THESIS_STAGE
  operator_score_use: NOT_FULL_E2R_SCORE
```

쉬운 예:

```text
삼성전자 4.0
= 최근 공식 이벤트 하나가 event-board에 올라왔다는 뜻

삼성전자 4.0
!= 삼성전자 HBM/C06 전체 투자 논리 점수
```

`samsung_hynix_full_thesis_smoke.json`도 아직 아래 상태다.

```text
verdict: PENDING_FULL_THESIS_REFRESH
score_allowed_before_execution: false
hardcoded_query_count: 0
blocking_reason: full_thesis_source_tasks_planned_but_not_executed
```

따라서 삼성전자/하이닉스는 아직 `HBM/C06 full thesis score/stage`를 말할 수 없다.

## Brain/Web canonical 상태

최신 canonical run은 Brain/Web disabled다.

```text
readiness_verdict:
  verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
  brain_web_evidence_pass: false
  meaningful_operational_stage_pass: false
  full_thesis_smoke_pass: false

goal_completion_audit:
  goal_completion_ready: false
  blockers:
    - brain_web_evidence_pass_false
    - full_thesis_smoke_pending

brain_web_readiness_gate_audit:
  verdict: NOT_REQUESTED
  llm_planner_call_count: 0
  llm_claim_extractor_attempt_count: 0
  web_search_task_count: 0
  web_fetched_document_count: 0
  source_task_execution_count: 0
  web_or_llm_accepted_claim_count: 0
  brain_stage_trace_count: 0
  brain_promoted_stage_row_count: 0
```

쉬운 예:

```text
NOT_REQUESTED
= 안 돌렸고, 안 돌렸다고 솔직히 적었다.

NOT_REQUESTED
!= 돌렸고 통과했다.
```

## 이번 패치가 닫은 것

닫은 병목:

```text
live_full_bounded run
-> real/codex planner 사용
-> unstructured TEXT_SPAN 문서 fetch
-> contract-blind claim extractor 필요
-> provider_mode=llm extractor run leaf 필요
```

이전에는 `execute_source_tasks_with_evidence_os_v4()`가 명시 extractor를 받지 않으면 `LLMContractBlindRawAssertionExtractor()` 기본값으로 들어갔다.

그 기본값은 `RuleFallbackExtractorProvider`라서 운영 Brain/Web pass의 근거가 될 수 없었다.

패치 후:

```text
ProductionShadowV4Config.claim_extractor_provider = auto

auto 선택 규칙:
  source_acquisition == live_full_bounded
  AND planner_provider not in {none, fake}
    -> CodexCLIExtractorProvider

  그 외 frozen/test/replay/disabled 성격
    -> RuleFallbackExtractorProvider
```

쉬운 예:

```text
실제 운영형 web/news/IR 원문:
  Codex LLM extractor가 읽어야 한다.

냉동 fixture replay:
  외부 도구를 부르면 테스트가 흔들리므로 rule fallback으로 남긴다.
```

수정 파일:

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/cli/run_research_brain_v4_production_shadow.py
src/e2r/census/census_runner_v4.py
src/e2r/cli/run_e2r_census_v4_until_pass.py
tests/test_research_brain_v4_operational_modes.py
```

핵심 CLI:

```text
run_research_brain_v4_production_shadow:
  --claim-extractor-provider auto|codex_cli|rule_fallback

run_e2r_census_v4_until_pass:
  --brain-claim-extractor-provider auto|codex_cli|rule_fallback
```

## 이번 패치가 닫지 않은 것

이번 패치만으로 아래는 아직 아니다.

```text
1. 실제 Brain/Web enabled canonical pass
2. provider_mode=llm extractor run 생성 완료
3. web/news/IR 원문에서 accepted Brain/Web claim 생성 완료
4. accepted claim -> score contribution 연결 완료
5. score contribution -> StageCourt trace 연결 완료
6. StageCourt trace -> representative census_stage_status row strict promotion 완료
7. 삼성전자/하이닉스 HBM/C06 full thesis 실행 완료
8. 전 아키타입 source-backed replay parity 완료
9. MEANINGFUL_OPERATIONAL_STAGE_PASS
```

이 차이를 놓치면 또 같은 사고가 난다.

```text
배관을 올바른 담당자에게 연결했다
!= 담당자가 실제로 문서를 읽고 답안지를 완성했다
```

## 검증 결과

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_bundle_export -v
```

결과:

```text
Ran 43 tests in 25.134s
OK
```

주변 운영/감사 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_provider_failure_pending \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_bundle_export -v
```

결과:

```text
Ran 56 tests in 31.309s
OK
```

전체 테스트 artifact:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/census_v4/2026-07-01/test_result_artifact_after_claim_provider_patch.json \
  --log output/census_v4/2026-07-01/test_result_artifact_after_claim_provider_patch.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
artifact_status: OK
artifact_test_count: 4954
artifact_failed_count: 0
artifact_error_count: 0
artifact_duration_seconds: 157.5068
```

로그 말미:

```text
Ran 4954 tests in 155.641s
OK
```

최신 anti-fake gate:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --test-result-artifact output/census_v4/2026-07-01/test_result_artifact_after_claim_provider_patch.json \
  --target-gate anti_fake \
  --fail-on-critical-audit true
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

중요:

```text
4954개 테스트 OK
+ anti_fake pass
!= goal complete
```

goal은 여전히 아래 blocker 때문에 미완료다.

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
```

## 다른 에이전트가 바로 돌릴 확인 명령

Stage scope 검산:

```bash
python - <<'PY'
import json
from collections import Counter
from pathlib import Path
rows=[json.loads(x) for x in Path("output/census_v4/2026-07-01/census_stage_status.jsonl").read_text().splitlines() if x.strip()]
for field in ["canonical_stage","base_stage","stage_scope","full_thesis_stage","operator_stage_use","operator_score_use"]:
    print(field, dict(Counter(str(r.get(field)) for r in rows)))
PY
```

기대값:

```text
stage_scope: CENSUS_EVENT_BOARD 3391
full_thesis_stage: FULL_THESIS_NOT_RUN 3391
operator_stage_use: NOT_FULL_THESIS_STAGE 3391
```

Brain/Web leaf 검산:

```bash
python - <<'PY'
import json
from pathlib import Path
root=Path("output/census_v4/2026-07-01")
for name in ["planner_runs.jsonl","web_search_tasks.jsonl","web_fetched_documents.jsonl","claim_extractor_runs.jsonl"]:
    p=root/name
    rows=[json.loads(x) for x in p.read_text().splitlines() if x.strip()] if p.exists() else []
    print(name, len(rows))
PY
```

기대값:

```text
planner_runs.jsonl 0
web_search_tasks.jsonl 0
web_fetched_documents.jsonl 0
claim_extractor_runs.jsonl 0
```

이 값이 0인 이유:

```text
canonical run은 Brain/Web disabled다.
```

따라서 0이 문제라는 뜻이 아니라, 0인데 Brain/Web pass라고 말하면 문제라는 뜻이다.

## 다음 패치 방향

### P0. 실제 enabled Brain/Web smoke

목표:

```text
BRAIN_AND_WEB_ACQUISITION_ENABLED
live_full_bounded
real/codex planner
claim_extractor_provider=auto
stage_promotion_mode=strict
```

기대:

```text
planner_runs.jsonl > 0
web_search_tasks.jsonl > 0 또는 official/source task가 명시적으로 해결
web_fetched_documents.jsonl > 0 또는 official document leaf > 0
claim_extractor_runs.jsonl에 provider_mode=llm row 존재
accepted Brain/Web claim 또는 explicit provider/source/material pending
```

주의:

```text
provider failure면 낮은 점수 확정 금지.
Provider/Source Pending으로 남겨야 한다.
```

### P1. extractor prompt/response leaf 강화

현재 `claim_extractor_runs`는 prompt/response hash와 raw ids 중심이다.

다음에는 외부 리뷰용으로 아래를 더 명확히 남긴다.

```text
prompt_path 또는 sanitized_prompt_excerpt
response_path 또는 sanitized_response_excerpt
model
provider command
forbidden_context_seen
input_document_ids
output_raw_assertion_ids
```

목표는 LLM에게 score/gate를 보여 주지 않았다는 것을 파일로 증명하는 것이다.

### P2. strict promotion end-to-end

목표:

```text
accepted Brain/Web claim
-> score contribution
-> StageCourt trace
-> brain_to_claim_trace
-> promoted census_stage_status row
```

pass 조건:

```text
같은 claim_id가 모든 leaf에서 이어진다.
snapshot://, fake provider, snippet-only, source_proxy_only는 production pass로 못 쓴다.
```

### P3. Samsung/Hynix full thesis smoke

목표:

```text
daily event-board 4.0과 HBM/C06 full thesis score를 완전히 분리한 채
005930, 000660에 대해 full thesis SourceTask를 실제 executed 또는 material pending으로 만든다.
```

pass 조건:

```text
full_thesis_claim_ids 또는 material pending reason
full_thesis_score_contribution_ids 또는 score_status=PENDING_MATERIAL_GAP
full_thesis_stagecourt_trace_ids 또는 explicit provider/source blocker
```

### P4. 전 아키타입 replay parity

목표:

```text
C01~C36 Evidence Contract v2
source-backed replay fixture
guard fixture
known-bad fixture
```

금지:

```text
source_proxy_only 연구자료를 production score 정답으로 사용
미래 수익률/성공 label을 extraction prompt에 주입
아키타입별 deterministic query template을 추가해 해결
```

## 다음 리뷰어 공격 질문

다음 에이전트는 아래 질문으로 깨면 된다.

```text
1. `operator_stage_use=NOT_FULL_THESIS_STAGE`인데 운영 Stage처럼 출력하는 코드가 있는가?
2. `full_e2r_verified_score=null`인데 full E2R 점수처럼 쓰는 코드가 있는가?
3. `claim_extractor_provider=auto`가 live_full_bounded + real/codex planner에서 실제 CodexCLIExtractorProvider를 고르는가?
4. frozen/test/replay에서 외부 Codex CLI를 불러 테스트를 흔들지는 않는가?
5. provider_mode=rule_fallback extractor run을 Brain/Web LLM success로 세는가?
6. claim_extractor_runs 없이 Brain/Web evidence pass가 가능한가?
7. source task count만 있고 fetched document/anchor/claim이 없어도 pass가 가능한가?
8. accepted claim만 있고 score contribution/StageCourt trace가 없어도 promoted row가 생기는가?
9. provider failure를 낮은 점수나 Red로 확정하는가?
10. 2020년 old risk나 타사 wrong-subject claim이 current hard break로 들어가는가?
11. LLM extractor prompt에 score, stage, missing primitive, Green gate 같은 오염 context가 들어가는가?
12. `target_gate=anti_fake` exit 0을 goal completion으로 해석하는가?
13. 4942/4951 같은 과거 테스트 숫자를 최신 값처럼 문서에 남기는가?
14. 삼성전자/하이닉스 4.0을 HBM/C06 full thesis score로 출력하는가?
15. all-archetype replay가 source-backed claim contribution으로 닫혔다고 과장하는가?
```

## 최종 판정

이번 패치는 필요했다.

이유:

```text
Brain/Web pass는 LLM claim extractor run 없이는 말할 수 없다.
그런데 live/full-bounded 경로가 extractor provider를 명시하지 않으면 rule fallback으로 흐를 수 있었다.
이제 auto 모드는 live/full-bounded + real/codex planner에서 Codex LLM extractor를 선택한다.
```

하지만 이 패치는 완료 선언 근거가 아니다.

현재 허용되는 최종 문장:

```text
Census v4는 이 문서 작성 시점 코드 기준 4954개 테스트와 anti_fake gate를 통과했다.
최신 로컬 전체 테스트 기준은 이후 문서의 4959개 OK다.
Stage row는 3391개 있지만 전부 event-board scope다.
Brain/Web canonical run은 아직 disabled라 extractor/planner/web leaf가 0개다.
이번 패치는 다음 enabled run에서 LLM extractor를 실제로 쓰도록 provider selection 배관을 고친 것이다.
운영 full thesis Stage와 meaningful operational pass는 아직 아니다.
```
