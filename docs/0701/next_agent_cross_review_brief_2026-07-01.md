# Next Agent Cross Review Brief - 2026-07-01

이 문서는 다음 에이전트가 `Census v4` 작업을 검증할 때 바로 때려볼 질문과 명령을 모아 둔 것이다.
`Stage가 있긴 한가`만 빠르게 보려면 먼저
`docs/0701/census_v4_0701_external_cross_review_ready_packet_2026-07-01.md`,
`docs/0701/census_v4_stage_truth_final_cross_validation_packet_2026-07-01.md`,
`docs/0701/census_v4_external_reviewer_attack_packet_2026-07-01.md`,
`docs/0701/census_v4_stage_reality_audit_2026-07-01.md`와
`docs/0701/census_v4_stage_presence_cross_check_and_patch_direction_2026-07-01.md`,
`docs/0701/census_v4_0701_stage_and_brainweb_final_forensic_2026-07-01.md`,
`docs/0701/census_v4_full_thesis_gap_forensic_and_patch_plan_2026-07-01.md`,
`docs/0701/census_v4_pass_scope_dictionary_2026-07-01.md`,
`docs/0701/census_v4_brain_claim_score_eligibility_guard_2026-07-01.md`,
`docs/0701/census_v4_live_official_source_bridge_patch_2026-07-01.md`,
`docs/0701/census_v4_live_brain_candidate_and_opendart_forensic_2026-07-01.md`,
`docs/0701/census_v4_brain_provider_failed_gap_not_promotion_blocker_2026-07-01.md`,
`docs/0701/census_v4_facility_correction_semantic_guard_patch_2026-07-01.md`,
`docs/0701/census_v4_enabled_codex_smoke_forensic_2026-07-01.md`,
`docs/0701/census_v4_subagent_cross_validation_findings_2026-07-01.md`를 읽으면 된다.

둘의 차이:

```text
external_cross_review_ready_packet:
  최신 artifact 기준의 단일 진입점이다.
  Stage label은 있지만 full thesis 운영 Stage는 0개라는 결론,
  4942개 테스트 artifact, report_generation_audit,
  92개 accepted claim과 67개 representative scored row의 차이,
  다음 패치 우선순위를 한 장에 고정한다.

stage_reality_audit:
  전체 3391 row에서 Stage label, score field, full_thesis_stage 분포를 본다.

stage_truth_final_cross_validation_packet:
  `census_stage_status`, `census_stage_map`, readiness/goal/smoke audit를 3중 대조한다.
  "Stage label은 있지만 full thesis 운영 Stage는 0개"라는 현재 사실과 다음 패치 순서를 한 장으로 고정한다.

full_thesis_gap_forensic:
  삼성전자/하이닉스 leaf artifact를 claim -> contribution -> StageCourt까지 따라가서
  왜 현재 4.0이 HBM/C06 full thesis 점수가 아닌지 확인한다.

pass_scope_dictionary:
  PASS가 실행 성공인지, disabled honesty인지, ledger refresh 검산인지 나눠 본다.

brain_claim_score_eligibility_guard:
  Brain/Web accepted claim이 생겨도 document/anchor/date/DIRECT/CURRENT/ACCEPTED/snapshot guard를 통과하지 못하면
  score_eligible=false가 되고 Brain/Web pass와 promotion을 막는지 본다.

live_official_source_bridge_patch:
  `live_official_*` 모드가 snapshot만 뒤지던 문제를 고쳐 live connector 결과를 EvidenceDocument/Anchor로 만들 수 있는지 본다.
  이 문서는 live document bridge 검증이지 Brain/Web evidence pass나 full thesis Stage pass 검증이 아니다.

live_brain_candidate_and_opendart_forensic:
  최신 enabled probe 기준으로 첫 planner 후보가 DART URL-backed live 후보로 바뀌었는지,
  OpenDART document.xml ZIP/CSS가 claim quote에 새지 않는지,
  그런데도 accepted Brain claim이 0개인 이유가 Brain/Web attempt 기준 정상 방어인지 본다.
  동시에 같은 대웅 공시가 기존 event-board leaf에서는 capacity_expansion claim/contribution으로 남더라도
  대표 row 점수는 semantic guard로 차단되는지 본다.

brain_provider_failed_gap_not_promotion_blocker:
  provider-failed no-claim follow-up task가 claim-backed Brain/Web trace promotion을 잘못 막지 않도록 한 패치를 본다.
  이 패치 후 document-ref false blocker는 사라졌지만, 최신 enabled smoke는 accepted Brain claim 0개와 web/news acquisition 0개 때문에 여전히 NOT_READY다.

stage_presence_cross_check:
  Stage label은 존재하지만 full thesis 운영 Stage는 0개라는 현재 답을
  숫자, leaf artifact 차이, 코드 병목, 다음 패치 순서까지 묶어서 본다.
```

## 먼저 결론부터 의심할 것

현재 작업자는 다음을 주장한다.

```text
맞는 주장:
- v4는 v3의 stage/score/trace 혼합을 막았다.
- event score와 full E2R verified score를 분리했다.
- 삼성전자/하이닉스 daily event와 full HBM thesis를 분리했다.
- Brain/Web을 실행하지 않았으므로 Brain/Web pass를 주장하지 않는다.
- base_stage 표시 label과 canonical_stage enum을 분리했다.
- sample_leaf_bundle과 artifact manifest로 부분 점수 row를 재검산할 수 있다.
- accepted_claims와 evidence_claims payload view가 92개로 일치한다.
- Research Brain v4 기존 보고서는 import 검토만 됐고 `SHADOW_OR_IMPORT_ONLY`로 남아 있다.
- Brain Stage promotion audit가 추가됐고 canonical run에서는 `NOT_REQUESTED`, Brain trace 0개, promoted row 0개다.
- Brain/Web readiness gate가 추가됐고 canonical run에서는 `NOT_REQUESTED`, `brain_web_evidence_pass_allowed=false`다.
- 이전 Codex-enabled smoke에서는 accepted claim unique 2개, score contribution 5개, Brain StageCourt trace 1개가 생긴 사례가 있었지만, representative `census_stage_status` 승격은 0개라서 pass가 아니었다.
- 최신 `/tmp/census_v4_enabled_probe`는 real provider success 1회, source task execution 7개, fetched real document 6개, unique real document 4개까지 갔지만 accepted Brain claim 0개, Brain score contribution 0개, Brain StageCourt trace 0개다. `leaf_artifact_audit.json`도 `FAIL`, `critical_count=2`라서 Brain/Web full readiness로 쓰면 안 된다.
- 최신 probe의 대웅 `003090` 공시는 Brain/Web attempt에서는 일정 연장 정정으로 보류됐고, 기존 event-board leaf의 `capacity_expansion` claim/contribution도 대표 row에서는 `semantic_guard_status=BLOCKED`, `score_scale=NO_SCORE`, `Stage1`로 차단된다.
- subagent 지적으로 count-only readiness pass 위험을 추가 차단했다. `brain_web_attempt` 집계 숫자만으로는 pass가 안 되고, 실제 `source_task_executions/evidence_documents/evidence_anchors/accepted_claims` row가 resolve되어야 한다.
- legacy v1 runner / 빈 claim builder / old CLI pass claim / v4 CLI miswire가 static audit에서 0이다.
- canonical output과 `test_result_artifact.json`은 최신 워크트리 기준 `4942개 OK`로 재생성했다.
- 삼성전자/하이닉스 full thesis smoke는 아직 `PENDING_FULL_THESIS_REFRESH`다.
- `full_thesis_smoke_tasks.jsonl`은 14개 planning-only task를 만든다. 2개 종목 x 7개 C06/HBM primitive gap이고, hardcoded query는 0개이며 점수 근거가 아니다.
- 하이닉스는 daily atomic decision이 2개지만 대표 row는 4.0 trace 하나를 선택한다. 이걸 합산 점수처럼 말하면 안 된다.
- `verdict=PASS`만 보고 완료라고 말하면 안 된다. `brain_planner_audit=PASS`도 `attempt_verdict=NOT_REQUESTED`, planner call 0이면 미실행 정직성이다.
- accepted claim leaf는 92개지만 representative `census_stage_status`에 직접 연결된 부분 점수 row는 67개다. 이제 `non_representative_claim_audit.json`이 이 차이를 장부화한다. 현재 `critical_count=0`, `non_representative_claim_score_leak_count=0`, 대표 밖 claim은 25개다.
- `base_stage=Stage2-Watch`와 `canonical_stage=3-Red` 같은 label은 full thesis Stage가 아니라 Census event board label이다. 이제 모든 current row에 `stage_scope=CENSUS_EVENT_BOARD`가 붙고, `FULL_THESIS` scope는 0개다.

금지된 주장:
- 전 종목 full E2R 운영 점수가 완성됐다.
- 삼성전자/하이닉스 HBM thesis 점수가 나왔다.
- `full_thesis_smoke_tasks.jsonl`이 있으니 full thesis가 실행됐다.
- Stage3/Green 후보가 나왔다.
- Brain/Web/LLM acquisition이 실제로 운영 통과했다.
- Codex-enabled smoke에서 source task가 돌았으니 Stage도 나온 것이다.
- Codex-enabled smoke에서 Brain StageCourt trace 1개가 있으니 운영 Stage도 나온 것이다.
- Research Brain v4 기존 snapshot 보고서를 Census production evidence로 승격했다.
- Brain/Web StageCourt trace가 representative `census_stage_status` row로 승격됐다.
- live official connector가 문서를 하나 가져왔으니 Brain/Web evidence pass가 됐다.
- 과거 연구자료 parity가 전 아키타입에서 증명됐다.
```

PASS 범위 주의:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
!= MEANINGFUL_OPERATIONAL_STAGE_PASS

현재 PASS는 가짜 성적표 방지 장치가 통과했다는 뜻이다.
full E2R 100점 만점 점수나 Stage3-Green/Yellow/Red/4B/4C 운영 판정이 완성됐다는 뜻이 아니다.
```

다음 에이전트는 위 주장을 그대로 믿지 말고 아래 명령으로 검증해야 한다.

## 0. v4 canonical run 재실행

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

주의:

```text
이 재실행은 Brain/Web disabled다.
따라서 이 결과로 Brain/Web 운영 통과를 주장하면 안 된다.
```

## 1. v4 산출물 숫자 재검산

```bash
python - <<'PY'
import json, pathlib, collections
rows=[
    json.loads(line)
    for line in pathlib.Path("output/census_v4/2026-07-01/census_stage_status.jsonl").read_text().splitlines()
    if line.strip()
]
for key in ["base_stage", "canonical_stage", "stage_signal", "stage_decision_status", "score_scale", "candidate_event_scope", "full_thesis_stage"]:
    print(key, dict(collections.Counter(r.get(key) for r in rows)))
print("rows", len(rows))
print("verified_score_present", sum(r.get("verified_score") is not None for r in rows))
print("full_e2r_verified_score_present", sum(r.get("full_e2r_verified_score") is not None for r in rows))
print("event_evidence_score_present", sum(r.get("event_evidence_score") is not None for r in rows))
print("candidate_event_count", sum(int(r.get("candidate_event_count") or 0) for r in rows))
print("score_eligible_candidate_event_count", sum(int(r.get("score_eligible_candidate_event_count") or 0) for r in rows))
audit=json.load(open("output/census_v4/2026-07-01/leaf_artifact_audit.json"))
print("sample_leaf_bundle_count", audit["metrics"].get("sample_leaf_bundle_count"))
print("evidence_claim_payload_count", audit["metrics"].get("evidence_claim_payload_count"))
print("planner_run_count", audit["metrics"].get("planner_run_count"))
print("web_search_task_count", audit["metrics"].get("web_search_task_count"))
print("claim_extractor_run_count", audit["metrics"].get("claim_extractor_run_count"))
bridge=json.load(open("output/census_v4/2026-07-01/research_brain_v4_bridge_audit.json"))
print("research_brain_bridge_verdict", bridge.get("verdict"))
print("research_brain_bridge_snapshot_url_count", bridge.get("snapshot_url_count"))
promotion=json.load(open("output/census_v4/2026-07-01/brain_stage_promotion_audit.json"))
print("brain_stage_promotion_verdict", promotion.get("verdict"))
print("brain_stage_trace_count", promotion.get("brain_stage_trace_count"))
print("brain_promoted_stage_row_count", promotion.get("brain_promoted_stage_row_count"))
print("unsafe_promoted_stage_row_count", promotion.get("unsafe_promoted_stage_row_count"))
brain_gate=json.load(open("output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json"))
print("brain_web_readiness_gate_verdict", brain_gate.get("verdict"))
print("brain_web_evidence_pass_allowed", brain_gate.get("brain_web_evidence_pass_allowed"))
print("brain_web_readiness_gate_blocker_count", len(brain_gate.get("blockers") or []))
for name in [
    "claim_to_stage_forensic_audit.json",
    "source_task_realness_audit.json",
    "existing_ledger_reuse_audit.json",
    "last_effective_thesis_audit.json",
    "source_coverage_audit.json",
    "runtime_plausibility_audit.json",
    "brain_web_readiness_gate_audit.json",
]:
    obj=json.load(open("output/census_v4/2026-07-01/" + name))
    if name == "brain_web_readiness_gate_audit.json":
        print(name, obj.get("verdict"), "pass_allowed", obj.get("brain_web_evidence_pass_allowed"))
    else:
        print(name, obj.get("verdict"), "critical_count", obj.get("critical_count"))
PY
```

기대값:

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
candidate_event_scope:
  ASSESSMENT_ONLY 3306
  CANDIDATE_EVENTS_PRESENT 85
full_thesis_stage:
  FULL_THESIS_NOT_RUN 3391
verified_score_present: 0
full_e2r_verified_score_present: 0
event_evidence_score_present: 67
summary.verified_score_present_count: 0
summary.full_thesis_stage_distribution:
  FULL_THESIS_NOT_RUN 3391
candidate_event_count: 226
score_eligible_candidate_event_count: 92
sample_leaf_bundle_count: 67
evidence_claim_payload_count: 92
planner_run_count: 0
web_search_task_count: 0
claim_extractor_run_count: 0
research_brain_bridge_verdict: SHADOW_OR_IMPORT_ONLY
research_brain_bridge_snapshot_url_count: 255
brain_stage_promotion_verdict: NOT_REQUESTED
brain_stage_trace_count: 0
brain_promoted_stage_row_count: 0
unsafe_promoted_stage_row_count: 0
brain_web_readiness_gate_verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
brain_web_readiness_gate_blocker_count: 0
claim_to_stage_forensic_audit.json: PASS critical_count 0
source_task_realness_audit.json: PASS_LEDGER_REFRESH_REALNESS critical_count 0
existing_ledger_reuse_audit.json: PASS critical_count 0
last_effective_thesis_audit.json: PASS critical_count 0
source_coverage_audit.json: PASS_LEDGER_REFRESH_COVERAGE critical_count 0
runtime_plausibility_audit.json: PASS_LEDGER_REFRESH_RUNTIME_HONESTY critical_count 0
brain_web_readiness_gate_audit.json: NOT_REQUESTED pass_allowed false
```

검증 포인트:

```text
verified_score가 하나라도 있으면 현재 문서의 핵심 주장이 깨진다.
full_thesis_stage가 FULL_THESIS_NOT_RUN이 아닌 row가 있으면 실제 full thesis 산출물이 있는지 trace를 따라가야 한다.
CensusAssessmentEvent만 있는 ASSESSMENT_ONLY row에서 점수가 나오면 실패다.
canonical_stage에 Stage2-Watch/Red 같은 표시 label이 들어가면 실패다.
Brain trace가 없는데 brain_stage_promotion_verdict가 PROMOTION_APPLIED면 실패다.
unsafe_promoted_stage_row_count가 0보다 크면 실패다.
brain_web_readiness_gate가 NOT_REQUESTED/BLOCKED인데 BRAIN_WEB_EVIDENCE_PASS가 붙으면 실패다.
source_coverage_audit가 PASS_LEDGER_REFRESH_COVERAGE인데 operational_live_source_coverage_pass=true면 실패다.
summary의 legacy stage_distribution은 base/display label 분포로 읽어야 한다.
canonical enum 분포는 canonical_stage_distribution이다.
```

## 1-A. enabled Codex smoke 공격 질문

별도 smoke는 canonical output이 아니지만, enabled 경로의 현재 병목을 보여 준다.

기대값:

```text
readiness_verdict: NOT_READY
brain_web_attempt.verdict: ATTEMPTED_NOT_CUTOVER_READY
real_provider_success_count: 1
source_task_execution_count: 7
real_document_fetched_count: 6
unique_real_document_fetched_count: 4
accepted_claim_count: 0
unique_accepted_claim_count: 0
brain_to_census_claim_exported_count: 0
brain_source_task_exported_count: 7
brain_source_task_execution_exported_count: 7
brain_evidence_document_exported_count: 4
brain_evidence_anchor_exported_count: 6
brain_score_contribution_exported_count: 0
brain_stagecourt_trace_exported_count: 0
brain_to_census_stage_exported_count: 0
claim_acceptance_ready: false
stagecourt_trace_ready: false
cutover_export_ready: false
brain_web_readiness_gate.verdict: BLOCKED
leaf_artifact_audit: FAIL, critical_count 2
```

검증 포인트:

```text
real_provider_success_count > 0 이어도 pass가 아니다.
accepted claim과 score contribution이 생겨도 representative row 승격이 없으면 pass가 아니다.
StageCourt trace는 내부 판정 장부이고, 운영 Stage는 census_stage_status promoted row다.
attempt summary count가 1 이상이어도 exported leaf count가 0이면 pass가 아니다.
특히 `brain_source_task_execution_exported_count`, `brain_evidence_document_exported_count`,
`brain_evidence_anchor_exported_count`, `brain_score_contribution_exported_count`를 따로 봐야 한다.
이 상태에서 `cutover_export_ready=true` 또는 `ATTEMPTED_WITH_SOURCE_TASKS`가 나오면 과대평가 버그다.
```

쉬운 예:

```text
검색 담당자가 책을 가져왔고, 채점 담당자가 초안 점수도 만들었다.
하지만 그 점수가 공식 성적표에 아직 옮겨지지 않았다.
지금 smoke는 그 상태다.
```

쉬운 예:

```text
001470 삼부토건:
  base_stage Stage2-Watch
  canonical_stage 2
  full_thesis_stage FULL_THESIS_NOT_RUN

030350 드래곤플라이:
  base_stage Red
  canonical_stage 3-Red
  full_thesis_stage FULL_THESIS_NOT_RUN

따라서 둘 다 "표시 상태"와 "canonical enum"은 분리되어야 한다.
```

## 2. leaf audit critical count 확인

```bash
python - <<'PY'
import json
obj=json.load(open("output/census_v4/2026-07-01/leaf_artifact_audit.json"))
print("verdict", obj["verdict"])
print("critical_count", obj["critical_count"])
for k, v in sorted(obj["critical_counts"].items()):
    if v:
        print(k, v)
print("sample_leaf_bundle_count", obj["metrics"].get("sample_leaf_bundle_count"))
for k in [
    "legacy_runner_production_reachable_count",
    "legacy_v3_runner_production_reachable_count",
    "empty_claims_stage_builder_production_count",
    "old_cli_can_claim_pass_count",
    "official_cli_not_v4_runner_count",
    "sample_bundle_missing_scored_row_count",
]:
    print(k, obj["critical_counts"].get(k))
PY
```

기대값:

```text
verdict PASS
critical_count 0
sample_leaf_bundle_count 67
legacy_runner_production_reachable_count 0
legacy_v3_runner_production_reachable_count 0
empty_claims_stage_builder_production_count 0
old_cli_can_claim_pass_count 0
official_cli_not_v4_runner_count 0
sample_bundle_missing_scored_row_count 0
```

특히 봐야 할 항목:

```text
missing_census_assessment_event_id_count
assessment_event_score_evidence_allowed_count
candidate_event_ids_contain_assessment_event_count
assessment_only_nonzero_score_count
no_current_catalyst_with_candidate_event_count
score_eligible_candidate_without_accepted_claim_count
atomic_candidate_event_is_assessment_count
atomic_candidate_event_not_in_symbol_candidate_events_count
canonical_stage_invalid_count
canonical_stage_display_label_count
stage_trace_canonical_stage_mismatch_count
stage_trace_stage_mismatch_count
stage_trace_score_interval_mismatch_count
stage_trace_score_status_mismatch_count
stage_trace_claim_set_mismatch_count
stage_trace_contribution_set_mismatch_count
verified_score_not_full_e2r_count
pending_material_marked_complete_count
semantic_guard_blocked_score_count
web_claimed_but_zero_search_count
llm_claimed_but_zero_calls_count
legacy_runner_production_reachable_count
legacy_v3_runner_production_reachable_count
empty_claims_stage_builder_production_count
old_cli_can_claim_pass_count
official_cli_not_v4_runner_count
sample_bundle_missing_scored_row_count
```

주의:

```text
canonical disabled run의 leaf audit 원본은 output/census_v4/2026-07-01/leaf_artifact_audit.json이다.
docs/operational/census_mode_v4_leaf_artifact_audit.json은 canonical run을 다시 생성하면 같은 PASS 장부여야 한다.

만약 docs/operational 쪽이 run_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED, output_root=/tmp/...인 FAIL 파일이면
임시 enabled 스모크가 공용 문서를 오염시킨 상태다.
현재 CLI 기본값은 /tmp output에서 docs/operational을 쓰지 않는 auto guard를 갖는다.
```

## 3. 삼성전자/하이닉스 오해 방지 검증

```bash
python - <<'PY'
import json, pathlib
rows=[
    json.loads(line)
    for line in pathlib.Path("output/census_v4/2026-07-01/census_stage_status.jsonl").read_text().splitlines()
    if line.strip()
]
for sym in ["005930", "000660"]:
    row=next(r for r in rows if str(r.get("symbol")).zfill(6)==sym)
    print(sym, {
        "base_stage": row.get("base_stage"),
        "stage_signal": row.get("stage_signal"),
        "event_evidence_score": row.get("event_evidence_score"),
        "verified_score": row.get("verified_score"),
        "full_e2r_verified_score": row.get("full_e2r_verified_score"),
        "full_thesis_stage": row.get("full_thesis_stage"),
        "full_thesis_missing_primitives": row.get("full_thesis_missing_primitives"),
        "census_assessment_event_id": row.get("census_assessment_event_id"),
        "candidate_event_count": row.get("candidate_event_count"),
        "score_eligible_candidate_event_count": row.get("score_eligible_candidate_event_count"),
    })
PY
```

기대값:

```text
005930:
  base_stage Stage1
  stage_signal OFFICIAL_EVENT_WATCH
  event_evidence_score 4.0
  verified_score null
  full_e2r_verified_score null
  full_thesis_stage FULL_THESIS_NOT_RUN
  candidate_event_count > 0
  score_eligible_candidate_event_count > 0

000660:
  base_stage Stage1
  stage_signal OFFICIAL_EVENT_WATCH
  event_evidence_score 4.0
  verified_score null
  full_e2r_verified_score null
  full_thesis_stage FULL_THESIS_NOT_RUN
  candidate_event_count > 0
  score_eligible_candidate_event_count > 0
```

검증 포인트:

```text
이 결과를 "삼성전자/하이닉스 HBM 점수 4점"이라고 해석하면 안 된다.
현재는 daily event board다.
```

## 4. semantic guard 검증

```bash
PYTHONPATH=src python -m unittest \
  tests.test_contract_semantic_classifier \
  tests.test_census_v4_semantic_guard \
  tests.test_web_research_runner.WebResearchRunnerTests.test_worldex_audit_opinion_with_samsung_customer_mention_does_not_create_samsung_4c \
  -v
```

검증 포인트:

```text
자사주 신탁계약이 고객 계약으로 점수화되면 실패해야 한다.
담보/질권 계약이 고객 계약으로 점수화되면 실패해야 한다.
월덱스 감사의견이 삼성전자 4C로 붙으면 실패해야 한다.
```

## 5. run-mode honesty 검증

```bash
cat docs/operational/census_mode_v4_readiness_verdict.md
cat docs/operational/census_mode_v4_brain_planner_audit.json
cat docs/operational/census_mode_v4_web_naver_acquisition_audit.json
cat docs/operational/census_mode_v4_llm_claim_extraction_audit.json
```

기대값:

```text
anti_fake_blockers: []
remaining_operational_gaps:
  - full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt path not run
  - Brain/Web/LLM acquisition artifacts are not produced in this disabled ledger-refresh run
  - source-backed replay parity across all archetypes is not proven
meaningful_operational_stage_pass: False
brain_web_evidence_pass: False
planner_run_count: 0
web_search_task_count: 0
claim_extractor_run_count: 0
```

검증 포인트:

```text
0 calls인데 Brain/Web pass label이 있으면 거짓 pass다.
현재는 OFFICIAL_BASELINE_OR_LEDGER_REFRESH_ONLY가 맞다.
```

negative smoke:

```bash
tmp=$(mktemp -d)
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root "$tmp/out" \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --fail-on-critical-audit false \
  --write-operational-docs auto
echo "exit=$?"
```

기대값:

```text
stdout: NOT_READY
exit=1
tmp/out/leaf_artifact_audit.json:
  llm_claimed_but_zero_calls_count: 1
  web_claimed_but_zero_search_count: 1
  llm_claim_extractor_claimed_but_zero_count: 1

docs/operational은 이 temporary smoke 때문에 덮이면 안 된다.
```

## 6. Brain stage promotion gate 검증

```bash
cat output/census_v4/2026-07-01/brain_stage_promotion_audit.json
cat docs/operational/census_mode_v4_brain_stage_promotion_audit.json
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
```

기대값:

```text
canonical brain_stage_promotion_audit:
  verdict: NOT_REQUESTED
  brain_stage_trace_count: 0
  brain_promoted_stage_row_count: 0
  unsafe_promoted_stage_row_count: 0
  blockers: []

unit test:
  Ran 3 tests
  OK
```

검증 포인트:

```text
stagecourt_traces.jsonl에 SCT-BRAIN-* trace가 생겨도 대표 row로 자동 승격되면 안 된다.
snapshot:// 문서를 쓴 Brain trace가 representative census_stage_status row가 되면 실패다.
provider none/fake/failure 상태에서 Brain promoted row가 생기면 실패다.
brain_stage_promotion_unsafe_promoted_count가 0보다 크면 실패다.
```

쉬운 예:

```text
조사원이 임시 채점 메모를 만들었다.
그 메모가 공식 성적표에 올라가려면 promotion audit가 strict 조건을 통과해야 한다.
현재 canonical run에서는 메모 자체가 없으므로 NOT_REQUESTED가 맞다.
```

## 7. Goal-required runtime proof 검증

Goal 문서가 요구한 감사 장부는 별도 파일로 분리돼 있다. 다음 에이전트는 `leaf_artifact_audit.json`만 보고 끝내면 안 된다.

```bash
python - <<'PY'
import json
root="output/census_v4/2026-07-01/"
for name in [
    "claim_to_stage_forensic_audit.json",
    "source_task_realness_audit.json",
    "existing_ledger_reuse_audit.json",
    "last_effective_thesis_audit.json",
    "source_coverage_audit.json",
    "runtime_plausibility_audit.json",
    "brain_web_readiness_gate_audit.json",
]:
    obj=json.load(open(root + name))
    print("\n" + name)
    for key in [
        "verdict",
        "critical_count",
        "scored_row_count",
        "stage2plus_or_risk_row_count",
        "source_task_execution_count",
        "source_task_claim_producing_count",
        "source_task_real_fetch_count",
        "source_task_fresh_provider_cache_count",
        "source_task_lifecycle_refresh_count",
        "reused_claim_count",
        "lifecycle_refreshed_reused_claim_count",
        "new_brain_web_claim_count",
        "last_effective_thesis_count",
        "source_timeline_count",
        "operational_live_source_coverage_pass",
        "cutover_replay_only_symbol_count",
        "runtime_mode",
        "provider_call_count",
        "llm_call_count",
        "minimum_gate_applies",
        "brain_web_evidence_pass_allowed",
        "web_or_llm_accepted_claim_count",
        "brain_to_claim_trace_count",
    ]:
        if key in obj:
            print(key, obj[key])
PY
```

기대값:

```text
claim_to_stage_forensic_audit:
  verdict PASS
  critical_count 0
  scored_row_count 67
  stage2plus_or_risk_row_count 36

source_task_realness_audit:
  verdict PASS_LEDGER_REFRESH_REALNESS
  verdict_scope LEDGER_REFRESH_REALNESS_PASS
  live_source_pass_allowed false
  source_task_execution_count 92
  source_task_claim_producing_count 60
  source_task_real_fetch_count 0
  source_task_fresh_provider_cache_count 60
  source_task_lifecycle_refresh_count 32

source_task_satisfaction_audit:
  schema_version e2r_census_v4_source_task_satisfaction_audit_v2
  verdict PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
  verdict_scope LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS
  critical_count 0
  warning_count 25
  representative_score_claim_count 67
  source_task_chain_closed_to_representative_stage_count 67
  source_task_chain_closed_to_stagecourt_count 92
  non_representative_source_task_claim_count 25
  live_source_task_satisfaction_pass_allowed false
  baseline_only_score_claim_count 32

primitive_state_chain_audit:
  schema_version e2r_census_v4_primitive_state_chain_audit_v1
  verdict PASS
  critical_count 0
  primitive_mapping_count 92
  primitive_state_count 92
  primitive_state_with_id_count 92
  representative_score_claim_count 67
  representative_score_claim_with_primitive_state_count 67
  mapping_leaf_resolution_supported true

existing_ledger_reuse_audit:
  verdict PASS
  reused_claim_count 92
  lifecycle_refreshed_reused_claim_count 92
  new_brain_web_claim_count 0

last_effective_thesis_audit:
  verdict PASS
  last_effective_thesis_count 3391
  source_timeline_count 3391

source_coverage_audit:
  verdict PASS_LEDGER_REFRESH_COVERAGE
  operational_live_source_coverage_pass false
  cutover_replay_only_symbol_count 67

runtime_plausibility_audit:
  verdict PASS_LEDGER_REFRESH_RUNTIME_HONESTY
  runtime_mode LEDGER_REFRESH
  provider_call_count 0
  llm_call_count 0

brain_web_readiness_gate_audit:
  verdict NOT_REQUESTED
  minimum_gate_applies false
  brain_web_evidence_pass_allowed false
  web_or_llm_accepted_claim_count 0
  brain_to_claim_trace_count 0
```

검증 포인트:

```text
claim_to_stage_forensic PASS:
  점수 row 67개는 claim id, contribution id, stage trace를 모두 따라갈 수 있다는 뜻이다.
  대표 row의 id 목록과 claim_to_stage_trace의 집계 목록이 1:1로 완전히 같다는 뜻은 아니다.
  대표 row id가 trace/ledger 안에서 실제로 발견되는지가 핵심이다.

source_task_realness PASS_LEDGER_REFRESH_REALNESS:
  현재 source task는 기존 source-backed ledger/cache를 재검산했다는 뜻이다.
  live_source_pass_allowed=false이면 대시보드에서 이 PASS를 live source pass로 표시하면 안 된다.
  live fetch가 0인데 live source pass라고 말하면 실패다.
  source_task_executions 원시 row의 CE-LIVE-DART-* 또는 budget_used.fetches=1 같은 필드는
  과거 leaf artifact에서 온 실행 모양일 수 있으므로 source_task_execution_origin과 realness audit를 같이 봐야 한다.

source_task_execution_count 스코프:
  source_task_realness_audit의 92는 ledger-refresh 재검산 task 수다.
  brain_web_readiness_gate의 0은 Brain/Web live source task 수다.
  두 숫자를 같은 모수로 비교하면 안 된다.

existing_ledger_reuse PASS:
  기존 claim 92개를 그냥 복사한 게 아니라 lifecycle/source locator 검사를 거쳐 trace에 연결했다는 뜻이다.

source_coverage PASS_LEDGER_REFRESH_COVERAGE:
  coverage honesty pass다.
  operational_live_source_coverage_pass=false이므로 full live operation pass가 아니다.

runtime_plausibility PASS_LEDGER_REFRESH_RUNTIME_HONESTY:
  0.3~1초대 runtime에서 provider/LLM 호출 0개라는 주장이 서로 맞다는 뜻이다.
  이 runtime으로 live web/LLM extraction을 했다고 주장하면 실패다.

brain_web_readiness_gate NOT_REQUESTED:
  Brain/Web을 요청하지 않았고 pass_allowed=false라는 뜻이다.
  NOT_REQUESTED를 BRAIN_WEB_EVIDENCE_PASS로 읽으면 실패다.

brain_web_readiness_gate 연결성 지표:
  brain_trace_missing_accepted_claim_count 0
  brain_trace_missing_score_contribution_ref_count 0
  brain_trace_missing_stagecourt_ref_count 0
  brain_contribution_without_accepted_support_count 0
  brain_stage_trace_without_accepted_claim_count 0
  promoted_stage_without_brain_trace_count 0
  현재 0인 이유는 Brain/Web이 disabled라 연결할 Brain claim 자체가 없기 때문이다.
  enabled run에서는 이 값들이 0이어야만 Brain/Web evidence pass를 말할 수 있다.
```

쉬운 예:

```text
현재 상태는 "semantic guard를 통과한 기존 채점지 67장을 꺼내서 번호표와 근거 서류가 맞는지 검산했다"에 가깝다.
"오늘 새로 모든 종목을 조사해서 full thesis 점수를 냈다"가 아니다.
```

## 8. 전체 테스트 재실행

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

canonical artifact 기록:

```text
Ran 4942 tests in 170.248s
OK
```

주의:

```text
테스트 통과는 "v4가 거짓 완료를 덜 말한다"는 증거다.
"full production E2R Stage가 완성됐다"는 증거가 아니다.
이번 문서 기준으로는 canonical output의 `test_result_artifact.json`도 4942개 결과를 가리킨다.
```

## 9. 다음 패치를 요구할 때의 기준

다음 에이전트가 패치를 제안한다면, 최소한 아래를 만족해야 한다.

```text
1. CensusAssessmentEvent와 CandidateEvent를 혼동하지 않는다.
2. claim 없는 종목은 점수 확정이 아니라 Stage0/NoCurrentCatalyst 또는 Pending이다.
3. provider failure는 low score final이 아니라 Source/Provider Pending이다.
4. full thesis 점수는 daily event score와 다른 필드에 저장한다.
5. Brain/Web을 실행하지 않았으면 Brain/Web pass를 말하지 않는다.
6. LLM은 점수를 직접 부르지 않고, source-backed claim을 만든다.
7. hard break는 direct target + current OPEN + source quorum 없이는 불가능하다.
8. 모든 score delta는 claim delta로 설명된다.
9. 부분 점수 row는 sample_leaf_bundle과 artifact_manifest로 재검산 가능해야 한다.
10. legacy v1/old CLI/빈 claim builder가 production pass를 주장하지 못해야 한다.
11. Brain StageCourt trace는 promotion audit strict 조건 없이는 대표 Stage row로 승격하지 않는다.
12. Brain/Web accepted claim, trace, score contribution, StageCourt trace, promoted row가 같은 claim ID로 이어져야 한다.
13. full thesis smoke task는 source task 계획서일 뿐이다. accepted full thesis claim, score contribution, StageCourt trace가 생기기 전까지 `full_thesis_stage=FULL_THESIS_NOT_RUN`이 맞다.
```

## 10. CLI Acceptance Table

다음 에이전트는 명령별 기대 결과를 먼저 고정해야 한다.
이 표와 다르게 종료되면 "성공"이 아니라 "라벨/CLI 정직성 버그"로 본다.

| 목적 | 예시 명령 핵심 | 기대 exit | 기대 verdict/label | 필수 artifact | 해석 |
| --- | --- | --- | --- | --- | --- |
| canonical anti-fake | `--run-mode LEDGER_REFRESH_CENSUS --brain-web-mode disabled` | 0 | `ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS` | leaf artifacts, manifest, readiness, seven audits | 가짜 Stage 방지 통과 |
| Brain/Web disabled honesty | canonical과 동일 | 0 | `brain_web_readiness_gate=NOT_REQUESTED`, `brain_web_evidence_pass=false` | `brain_web_readiness_gate_audit.json` | Brain/Web을 안 했다고 솔직히 적음 |
| Brain/Web requested but provider none | `--run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED --brain-web-mode enabled --brain-planner-provider none` | 1 | `NOT_READY`, gate `BLOCKED` | planner/source/web/extractor blocker trace | 낮은 점수 확정 금지 |
| Brain/Web real/codex provider attempt | `--brain-web-mode enabled --brain-planner-provider real|codex` | 1 또는 0 | real success 없으면 `EXTERNAL_PROVIDER_BLOCKER_NOT_READY`; success면 ID chain 검사 | planner prompts/responses, source tasks, fetched docs, accepted claims | 단순 호출 수가 아니라 claim-to-stage 연결이 필요 |
| goal3 self-repair command | `--mode HYBRID_CENSUS --max-iterations 10 --fail-on-* true` | 1 | `NOT_READY` 또는 `fail-on-critical-audit=true`면 critical audit RuntimeError | self_repair_log, known_bad_report, completion audit | flag와 self-repair/known-bad는 닫혔지만 full-thesis/BrainWeb blocker 때문에 완료는 아님 |
| full live success 후보 | `FULL_LIVE_BRAIN_CENSUS` 계열 | 0은 모든 hard gate 통과 때만 | `BRAIN_WEB_EVIDENCE_PASS`, `FULL_THESIS_SMOKE_PASS`, `MEANINGFUL_OPERATIONAL_STAGE_PASS` | live/codex provider, web fetch, extractor, known-bad, self-repair, full thesis smoke | 최종 운영 후보 |

쉬운 예:

```text
enabled/provider-none 실행은 "실패"가 맞다.
이 경우 낮은 점수/Red를 내면 안 되고, Provider/Brain/Web blocker로 끝나야 한다.
```

CLI exit 해석 주의:

```text
현재 v4 CLI는 --target-gate anti_fake|meaningful|brain_web|full_thesis를 받는다.
anti_fake target은 현재 exit 0이 가능하다.
meaningful / brain_web / full_thesis target은 현재 hard false라 NOT_READY가 정상이다.
따라서 exit 0은 "goal1~3 최종 완료"가 아니라 "요청한 target gate가 통과했다"는 뜻으로만 읽어야 한다.
```

테스트 증거 주의:

```text
현재 canonical run은 test_result_artifact.json을 검증해 MACHINE_READABLE_TEST_ARTIFACT_PASS를 기록한다.
artifact는 command, exit_code, test_count, log_sha256을 포함한다.
테스트 증거 blocker, known-bad regression blocker, self-repair audit loop blocker는 닫혔다.
다만 full thesis/Brain-Web blockers는 아직 남아 있다.
```

현재 CLI flag 상태:

```text
--mode
--max-iterations
--fail-on-run-mode-overclaim
--fail-on-atomic-mismatch
--fail-on-semantic-guard
위 flag들은 현재 CLI가 받는다.
known-bad와 self-repair audit/recheck loop는 leaf artifact로 닫혔다.
다만 full-thesis와 Brain/Web은 아직 닫히지 않았다.
```

따라서 이 flag들이 존재하더라도, full-thesis와 Brain/Web이 실제 leaf artifact로 닫히기 전에는 pass로 끝나면 안 된다.

## 최종 공격 질문

다음 질문에 답하지 못하면 운영 준비가 아니다.

```text
1. 이 Stage는 full thesis Stage인가, daily event Stage인가?
2. 이 점수는 100점 만점 full E2R score인가, event partial score인가?
3. 이 claim은 target 회사 자체 claim인가, 고객/공급사/업계 claim인가?
4. 이 claim은 as_of_date 현재 살아 있는가, 과거/해소/superseded인가?
5. 이 source는 원문 anchor가 있는가, snippet/proxy인가?
6. 이 gap은 source task로 조사됐는가, 그냥 비어 있는가?
7. provider 실패가 낮은 점수로 확정되지 않았는가?
8. 동일 입력을 다시 돌리면 같은 score/stage가 나오는가?
9. 점수가 바뀌면 어떤 claim delta 때문인지 설명되는가?
10. "PASS"라는 단어가 실제로 무엇을 pass했다는 뜻인지 문서와 코드가 일치하는가?
11. sample_leaf_bundle에 모든 scored/claim-backed row가 들어 있는가?
12. artifact_manifest의 row_count/sha256이 실제 파일과 일치하는가? `census_stage_map.csv`도 row_count=3391이어야 한다.
13. Brain/Web enabled export가 score/stage trace를 만들더라도 census_stage_status 대표 Stage row로 몰래 승격하지 않는가?
14. source_task_executions 원시 row의 live-looking 필드를 source_task_realness_audit 없이 live fetch로 오해하지 않았는가?
15. representative row id와 claim_to_stage_trace 집계 목록을 1:1 동일해야 한다고 잘못 검증하지 않았는가?
16. Brain/Web accepted claim ID와 contribution/stage/promoted row의 claim ID가 서로 다른데 숫자만 보고 통과시키지 않는가?
```
