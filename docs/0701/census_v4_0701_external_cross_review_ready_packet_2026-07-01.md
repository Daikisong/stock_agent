# Census v4 0701 External Cross Review Ready Packet - 2026-07-01

작성 목적:

```text
다음 에이전트가 "지금 뭔가 잘못되고 있는 거 맞지?"
"Stage가 있는 애들이 있긴 해?"
"이 PASS가 진짜 운영 PASS야?"
를 바로 공격할 수 있게 최신 산출물 기준으로 한 장에 고정한다.
```

이 문서는 결론을 좋게 포장하지 않는다.
현재 통과한 것은 `ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS`이고,
아직 통과하지 못한 것은 `MEANINGFUL_OPERATIONAL_STAGE_PASS`,
`BRAIN_WEB_EVIDENCE_PASS`, `FULL_THESIS_SMOKE_PASS`다.

쉬운 예:

```text
지금은 "전교생 출석부와 일부 쪽지시험 채점지가 번호까지 맞는지"를 검산한 상태다.
아직 "전교생 기말고사 100점 만점 최종 성적표"가 나온 상태가 아니다.
```

## 최신 기준 산출물

기준 경로:

```text
output/census_v4/2026-07-01
docs/operational/census_mode_v4_*.*
```

최신 핵심 artifact:

```text
census_stage_status.jsonl
leaf_artifact_audit.json
readiness_verdict.json
goal_completion_audit.json
report_generation_audit.json
test_result_artifact.json
test_result_evidence_audit.json
artifact_manifest.json
```

최신 테스트 artifact:

```text
command: python -m unittest discover -s tests -v
test_count: 4942
status: OK
failed_count: 0
error_count: 0
duration_seconds: 170.2478
log_sha256: aa894a5be988f1837df72bf33fa52b2ac452ee32e409b3b1c89fddfad77bf300
```

중요:

```text
4942개 테스트 OK
!= goal.md 전체 완료
!= 전 아키타입 운영 thesis 완료
!= Brain/Web 운영 증거 pass
```

## 현재 결론

짧은 답:

```text
Stage label은 있다.
full E2R thesis Stage는 아직 0개다.
```

현재 있는 것:

```text
Census event-board 상태 label
source-backed partial event score row 67개
accepted claim payload 92개
SourceTask/document/anchor/claim/primitive/score/stage trace ID-chain audit
report가 leaf audit에서 생성됐는지 확인하는 report_generation_audit
known-bad regression PASS
self-repair loop PASS
```

현재 없는 것:

```text
FULL_E2R_100 verified_score
Stage3-Green / Stage3-Yellow / full thesis Stage3-Red
4B / 4C thesis transition
삼성전자/하이닉스 C06/HBM full thesis score
Brain/Web enabled run의 accepted claim -> score contribution -> promoted row 통과
전 아키타입 source-backed replay parity
```

쉬운 예:

```text
삼성전자/하이닉스에 Stage1과 4.0점이 보인다.
이건 "DART/ledger 이벤트가 있어 접수표에 올라왔다"는 뜻이다.
HBM 고객 배정, qualification, capacity sold-out, revenue mix, FCF/revision까지 본
100점짜리 HBM thesis 점수가 아니다.
```

## Stage 존재 여부 재검산값

`census_stage_status.jsonl` 기준:

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

stage_scope:
  CENSUS_EVENT_BOARD: 3391

score_scale:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

score_scope:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

operator_score_use:
  NOT_FULL_E2R_SCORE: 3391
```

따라서 다음 문장은 맞다:

```text
Stage label이 붙은 row는 85개다.
점수가 붙은 representative row는 67개다.
```

다음 문장은 틀리다:

```text
Stage1/Stage2/Red 운영 thesis가 85개 확정됐다.
Green/Yellow/4B/4C 판단이 가능하다.
삼성전자/하이닉스 C06 운영 점수가 나왔다.
```

## Claim과 대표 row 차이

leaf artifact 기준:

```text
accepted_claims.jsonl:       92
evidence_claims.jsonl:       92
score_contributions.jsonl:   92
stagecourt_traces.jsonl:     92

representative scored row:   67
sample_leaf_bundle rows:     67
```

`non_representative_claim_audit.json` 기준:

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

score leak into representative row: 0
```

정확한 해석:

```text
67개 대표 점수 row는 성적표에 실제 반영된 항목이다.
나머지 25개 accepted claim은 leaf에는 있지만 대표 row에 반영되지 않았고,
그 이유는 감사 파일에 warning으로 남아 있다.
현재 critical leak은 0이지만, full 운영 전에는 이 25개를 더 정교하게 분류해야 한다.
```

쉬운 예:

```text
숙제 92장을 받았고 그중 67장이 이번 성적표에 반영됐다.
나머지 25장은 폐기된 것이 아니라 "왜 성적표에 안 들어갔는지" 장부에 남긴 상태다.
성적표에 몰래 섞인 숙제는 0장이다.
```

## SourceTask / Primitive / Report 감사

`source_task_satisfaction_audit.json`:

```text
verdict: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
critical_count: 0
warning_count: 25
representative_score_claim_count: 67
source_task_chain_closed_to_representative_stage_count: 67
source_task_chain_closed_to_stagecourt_count: 92
live_source_task_satisfaction_pass_allowed: false
```

이 PASS는 live source pass가 아니다.
기존 ledger refresh 산출물에서 ID-chain이 닫혀 있는지 검산한 것이다.

`primitive_state_chain_audit.json`:

```text
verdict: PASS
critical_count: 0
representative_score_claim_count: 67
representative_score_claim_with_primitive_state_count: 67
primitive_state_with_id_count: 92
primitive_mapping_count: 92
mapping_leaf_resolution_supported: true
```

`report_generation_audit.json`:

```text
verdict: PASS
critical_count: 0
report_generated_from_leaf_audit: true
report_metrics_source: leaf_artifact_audit.json
readiness_source: readiness_verdict.json
in_memory_summary_used_for_acceptance_count: 0
leaf_report_metric_mismatch_count: 0
report_only_status_change_allowed: false
```

이 감사의 의미:

```text
acceptance_report.md가 임의 요약이나 in-memory counter로 PASS를 꾸미지 않고,
leaf_artifact_audit.json과 readiness_verdict.json에서 온 숫자를 써야 한다.
```

쉬운 예:

```text
보고서에 "67개 채점됨"이라고 쓰려면,
말로 센 숫자가 아니라 실제 채점지 묶음 파일에서 67개가 확인돼야 한다.
```

## Brain/Web 현재 상태

canonical run은 다음 모드다.

```text
run_mode: LEDGER_REFRESH_CENSUS
brain_web_mode: disabled
brain_web_attempt.verdict: NOT_REQUESTED
brain_stage_promotion.verdict: NOT_REQUESTED
brain_web_readiness_gate.verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
planner_run_count: 0
web_search_task_count: 0
claim_extractor_run_count: 0
web_fetched_document_count: 0
```

따라서 현재 canonical run으로는 Brain/Web 운영 통과를 말하면 안 된다.

허용되는 말:

```text
Brain/Web이 disabled였고, disabled였다는 사실을 정직하게 기록했다.
```

금지되는 말:

```text
Brain/Web이 운영 통과했다.
LLM이 실제 원문을 읽고 claim을 추출했다.
Naver/Web 수집이 운영 claim으로 들어갔다.
```

## Brain/Web Provider-Failed Gap Patch

추가 문서:

```text
docs/0701/census_v4_brain_provider_failed_gap_not_promotion_blocker_2026-07-01.md
```

패치 내용:

```text
Brain/Web promotion/readiness audit에서
accepted claim을 만든 task만 document ref mandatory로 본다.

PROVIDER_FAILED / NO_EVIDENCE_FOUND 이고 accepted_claim_ids가 없는 follow-up task는
promotion blocker가 아니라 source/provider gap으로 남긴다.
```

검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_web_readiness_gate \
  -v

Ran 15 tests in 6.718s
OK
```

enabled smoke 재실행:

```text
output: /tmp/census_v4_enabled_brain_probe_after_docref_patch
result: NOT_READY

fixed:
  brain_source_task_without_document_ref_count: 0
  brain_source_task_unresolved_document_ref_count: 0

still blocked:
  accepted Brain claim count: 0
  brain score contribution count: 0
  brain StageCourt trace count: 0
  web_search_task_count: 0
  web_fetched_document_count: 0
```

해석:

```text
이번 패치는 Brain/Web pass가 아니다.
잘못된 promotion blocker 하나를 제거한 것이다.
다음 blocker는 accepted claim 안정 생성과 bounded web/news acquisition artifact 생성이다.
```

## 삼성전자 / SK하이닉스 상태

현재 event-board row:

```text
005930 삼성전자:
  base_stage: Stage1
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  score_scale: EVENT_WEIGHTED_PARTIAL
  event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN

000660 SK하이닉스:
  base_stage: Stage1
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  score_scale: EVENT_WEIGHTED_PARTIAL
  event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN
```

해석:

```text
두 종목은 daily event board에 올라왔다.
두 종목의 C06/HBM full thesis는 아직 실행되지 않았다.
```

`full_thesis_smoke_tasks.jsonl`은 planning-only다.
이 파일이 있다고 해서 full thesis가 실행된 것이 아니다.

## 최신 재현 명령

전체 테스트 artifact 재생성:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/census_v4/2026-07-01/test_result_artifact.json \
  --log output/census_v4/2026-07-01/test_result_artifact.log \
  -- python -m unittest discover -s tests -v
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

Stage/score 재검산:

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
    "stage_scope",
    "score_scope",
    "stage_signal",
    "score_valid_status",
    "operator_stage_use",
    "operator_score_use",
]:
    print(key, dict(Counter(str(row.get(key)) for row in rows)))

print("event_evidence_score_present", sum(row.get("event_evidence_score") is not None for row in rows))
print("verified_score_present", sum(row.get("verified_score") is not None for row in rows))
print("full_e2r_verified_score_present", sum(row.get("full_e2r_verified_score") is not None or row.get("full_thesis_verified_score") is not None for row in rows))
PY
```

report-generation audit 재검산:

```bash
python - <<'PY'
import json
from pathlib import Path

root = Path("output/census_v4/2026-07-01")
audit = json.loads((root / "report_generation_audit.json").read_text())
print(audit["verdict"])
print(audit["report_generated_from_leaf_audit"])
print(audit["in_memory_summary_used_for_acceptance_count"])
print(audit["leaf_report_metric_mismatch_count"])
print(audit["missing_or_mismatched_fragments"])
PY
```

## 다음 리뷰어가 바로 때릴 공격 질문

1. `base_stage`와 `canonical_stage`가 존재한다는 이유로 full thesis Stage를 주장하지 않는가?
2. `stage_scope != FULL_THESIS`인 row가 operator digest에서 Green/Yellow/4B/4C처럼 출력되지 않는가?
3. `event_evidence_score=4.0`을 FULL_E2R_100 점수처럼 보여 주는 곳이 남아 있지 않은가?
4. `verified_score`가 null인데 점수 확정 문구가 출력되지 않는가?
5. Brain/Web disabled run에서 Brain/Web pass를 말하지 않는가?
6. report가 leaf audit이 아니라 in-memory summary 숫자로 PASS를 만든 흔적이 없는가?
7. 92개 accepted claim 중 대표 row 밖 25개가 score/stage에 몰래 섞이지 않는가?
8. `accepted_claim_without_atomic_decision_count=7`이 full 운영 전에 더 구체적인 제외 사유로 줄어드는가?
9. `SourceTask -> document -> anchor -> claim -> primitive -> contribution -> trace -> row` chain이 representative 67개 모두에서 닫혀 있는가?
10. 삼성전자/하이닉스 C06/HBM full thesis를 event-board Stage1과 혼동하지 않는가?
11. `source_proxy_only`, `evidence_url_pending`, `snapshot://` 연구자료가 운영 점수에 들어가지 않는가?
12. provider failure나 not requested가 낮은 점수 확정으로 바뀌지 않는가?

## 다음 패치 방향

우선순위 1:

```text
Brain/Web enabled run에서 실제 bounded SourceTask를 실행한다.
조건:
  planner provider real
  source task execution real
  document_id + anchor_id 존재
  snapshot:// 금지
  accepted claim DIRECT/CURRENT/ACCEPTED/score_eligible
  score contribution support_claim_ids 연결
  StageCourt trace 연결
  promoted census row 연결
```

우선순위 2:

```text
삼성전자/하이닉스 C06/HBM full thesis smoke를 planning-only에서 execution으로 승격한다.
단, material gap이면 낮은 점수 확정이 아니라 PENDING_MATERIAL_GAPS여야 한다.
```

우선순위 3:

```text
accepted claim 92개 중 대표 row 밖 25개를 더 세밀하게 분류한다.
특히 accepted_claim_without_atomic_decision_count=7은
semantic_guard_blocked / duplicate_leaf / non_score_eligible_claim / lifecycle_pending처럼
운영자가 이해 가능한 이유로 쪼개야 한다.
```

우선순위 4:

```text
전 아키타입 source-backed replay parity를 구축한다.
연구 markdown의 성공 label이나 사후 MFE/MAE를 정답으로 쓰지 않는다.
당시 원문 URL, snapshot, quote, table cell, API record만 fixture 정답으로 쓴다.
```

우선순위 5:

```text
MEANINGFUL_OPERATIONAL_STAGE_PASS gate를 anti_fake gate와 완전히 분리해 유지한다.
테스트 수천 개 OK여도 Brain/Web/full-thesis/replay가 없으면 completion false다.
```

## Must-Fail 조건

아래 중 하나라도 발생하면 다음 에이전트는 현재 작업을 실패로 봐야 한다.

```text
1. full_thesis_stage != FULL_THESIS_NOT_RUN인데 full thesis claim/score/trace가 없다.
2. verified_score가 있는데 score_scale != FULL_E2R_100이다.
3. event_evidence_score를 운영 100점 점수로 출력한다.
4. Brain/Web disabled인데 brain_web_evidence_pass=true다.
5. report_generation_audit 없이 acceptance_report PASS를 주장한다.
6. report_generation_audit.leaf_report_metric_mismatch_count > 0이다.
7. representative score claim 67개 중 SourceTask/document/anchor/primitive/trace chain이 끊긴다.
8. 대표 row 밖 25개 claim이 score/stage에 몰래 섞인다.
9. 삼성전자/하이닉스 Stage1 4.0을 HBM/C06 thesis 결과로 말한다.
10. 4942 tests OK를 goal.md 전체 완료라고 말한다.
```

## 최종 판단

현재 상태를 한 문장으로 쓰면:

```text
Census v4는 가짜 점수와 가짜 Stage 완료 선언을 막는 상태판으로는 좋아졌지만,
아직 실제 운영형 full thesis Stage 엔진은 아니다.
```

다음 작업자는 이 문서의 숫자가 틀리면 먼저 산출물 재생성부터 해야 한다.
숫자가 맞다면 다음 싸움은 `Brain/Web enabled real claim chain`과
`삼성전자/하이닉스 C06 full thesis execution`이다.
