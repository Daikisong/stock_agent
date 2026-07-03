# Census v4 External Reviewer Attack Packet - 2026-07-01

작성 목적:

다음 에이전트가 `Census v4`를 빡세게 리뷰할 때 바로 공격할 수 있게,
현재 상태를 산출물 기준으로 고정한 문서다.

이 문서는 칭찬용 문서가 아니다.
다음 리뷰어가 아래 질문을 던지면 현재 구현이 어디까지 버티고,
어디서 아직 막히는지 바로 드러나야 한다.

```text
1. Stage가 있는 종목은 정말 있는가?
2. 그 Stage가 full thesis 운영 Stage인가?
3. Brain/Web/LLM은 실제로 실행됐는가?
4. source task 92개와 Brain/Web source task 0개는 왜 같이 존재하는가?
5. 삼성전자/하이닉스는 HBM/C06 thesis 점수가 나온 것인가?
6. PASS라고 쓰인 파일들이 실제 운영 pass인가, disabled honesty pass인가?
7. 다음 패치는 어디부터 해야 하는가?
```

짧은 답:

```text
Stage label은 있다.
full thesis 운영 Stage는 아직 없다.
Brain/Web canonical run은 disabled이고, 안 했다고 솔직히 기록했다.
현재 pass는 anti-fake/ledger-refresh 검산 pass다.
운영 점수/Stage pass가 아니다.
```

쉬운 예:

```text
지금은 전교생 출석부와 일부 쪽지시험 답안지 번호 검산은 끝났다.
하지만 전교생 기말고사 100점 만점 점수와 최종 등급은 아직 채점하지 않았다.
```

## Source Of Truth

이 문서의 기준 원본은 아래 leaf artifacts다.

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/census_stage_summary.json
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/goal_completion_audit.json
output/census_v4/2026-07-01/brain_web_attempt_audit.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01/brain_stage_promotion_audit.json
output/census_v4/2026-07-01/samsung_hynix_full_thesis_smoke.json
output/census_v4/2026-07-01/test_result_artifact.json
```

`docs/operational`과 `docs/0701`은 사람이 읽기 위한 복사본/해설이다.
원본 leaf artifact와 문서가 충돌하면 leaf artifact가 이긴다.

가장 먼저 읽을 보조 해설:

```text
docs/0701/census_v4_stage_truth_final_cross_validation_packet_2026-07-01.md
```

이 보조 문서는 `census_stage_status`, `census_stage_map`, readiness/goal/smoke audit를 3중 대조해
"Stage label은 있지만 full thesis 운영 Stage는 0개"라는 현재 사실과 다음 패치 순서를 한 장으로 고정한다.

## Current Canonical Truth

현재 canonical run:

```text
run_mode: LEDGER_REFRESH_CENSUS
brain_web_mode: disabled
target_gate: anti_fake
verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
target_gate_pass: true
brain_web_evidence_pass: false
meaningful_operational_stage_pass: false
full_thesis_smoke_pass: false
```

이 말은 아래 뜻이다.

```text
가짜 완료 선언을 막는 상태판은 통과했다.
운영용 full E2R Stage 지도는 아직 통과하지 않았다.
```

## Stage Reality

`census_stage_status.jsonl` 재검산 결과:

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

investigation_status:
  NO_CURRENT_CATALYST: 3306
  PENDING:               48
  COMPLETE:              36
  RISK_REVIEW:            1

verified_score_present: 0
full_e2r_verified_score_present: 0
```

정확한 해석:

```text
Stage0 3306개:
  전 종목 census 평가 대상에 올라왔지만 현재 candidate event가 없는 row.

Stage1         54개:
  공식/ledger 이벤트가 있어 watch로 올라온 row.
  full thesis 점수 row가 아니다.

Stage2-Watch   30개:
  material claim 또는 candidate event가 있어 추가 조사가 필요한 watch row.
  full thesis Stage2 확정이 아니다.

Red 1개:
  현재 event 상태판의 risk-review 표시다.
  full thesis Stage3-Red 운영 판정과 동일시하면 안 된다.
```

따라서 다음 주장은 맞다.

```text
Stage 상태 label이 있는 종목은 있다.
```

다음 주장은 틀리다.

```text
전체 KRX full E2R 100점 운영 Stage가 확정됐다.
```

## Samsung / Hynix Ground Truth

삼성전자:

```text
symbol: 005930
company_name: 삼성전자
base_stage: Stage1
canonical_stage: 1
full_thesis_stage: FULL_THESIS_NOT_RUN
score_scale: EVENT_WEIGHTED_PARTIAL
verified_score: null
full_e2r_verified_score: null
score_contribution_count: 1
investigation_status: COMPLETE
```

SK하이닉스:

```text
symbol: 000660
company_name: SK하이닉스
base_stage: Stage1
canonical_stage: 1
full_thesis_stage: FULL_THESIS_NOT_RUN
score_scale: EVENT_WEIGHTED_PARTIAL
verified_score: null
full_e2r_verified_score: null
score_contribution_count: 1
investigation_status: COMPLETE
```

쉬운 해석:

```text
맞는 말:
  삼성전자/하이닉스는 daily event board에 올라왔다.

틀린 말:
  삼성전자/하이닉스 HBM/C06 full thesis 점수와 Stage가 나왔다.
```

## PASS Scope Table

현재 `PASS`처럼 보이는 값은 범위가 서로 다르다.

| Artifact | 현재 값 | 의미 | 운영 pass인가 |
| --- | --- | --- | --- |
| `readiness_verdict.json` | `ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS` | anti-fake target gate 통과 | 아니오 |
| `leaf_artifact_audit.json` | `PASS`, critical 0 | leaf bundle 내부 연결성 검산 | 부분 |
| `known_bad_regression_report.json` | `PASS` | known-bad fixture 방어 | 부분 |
| `test_result_artifact.json` | `OK`, 4942 tests | 테스트 산출물 증거 존재 | 부분 |
| `source_task_realness_audit.json` | `PASS_LEDGER_REFRESH_REALNESS` | ledger-refresh source task 정직성 | live pass 아님 |
| `source_coverage_audit.json` | `PASS_LEDGER_REFRESH_COVERAGE` | 기존 ledger/source coverage 검산 | live pass 아님 |
| `runtime_plausibility_audit.json` | `PASS_LEDGER_REFRESH_RUNTIME_HONESTY` | 실행 시간이 주장 범위와 맞음 | live pass 아님 |
| `web_naver_acquisition_audit.json` | `DISABLED_HONESTY_PASS` | Web/Naver를 안 했고 안 했다고 기록 | 아니오 |
| `llm_claim_extraction_audit.json` | `DISABLED_HONESTY_PASS` | LLM claim extraction을 안 했고 안 했다고 기록 | 아니오 |
| `brain_web_readiness_gate_audit.json` | `NOT_REQUESTED` | Brain/Web disabled | 아니오 |
| `brain_stage_promotion_audit.json` | `NOT_REQUESTED` | Brain stage promotion disabled | 아니오 |
| `goal_completion_audit.json` | `goal_completion_ready=false` | goal completion 미완료 | 아니오 |

절대 금지:

```text
DISABLED_HONESTY_PASS를 Brain/Web 성공으로 읽기.
PASS_LEDGER_REFRESH_REALNESS를 live provider fetch 성공으로 읽기.
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS를 MEANINGFUL_OPERATIONAL_STAGE_PASS로 읽기.
```

## Brain/Web Canonical State

canonical output 기준:

```text
brain_web_attempt_audit:
  verdict: NOT_REQUESTED
  planner_run_count: 0
  real_provider_success_count: 0
  source_task_execution_count: 0
  accepted_claim_count: 0
  unique_accepted_claim_count: 0
  brain_source_task_exported_count: 0
  brain_source_task_execution_exported_count: 0
  brain_evidence_document_exported_count: 0
  brain_evidence_anchor_exported_count: 0
  brain_score_contribution_exported_count: 0
  brain_stagecourt_trace_exported_count: 0
  brain_to_census_stage_exported_count: 0
  stagecourt_trace_ready: false
  cutover_export_ready: false

brain_web_readiness_gate_audit:
  verdict: NOT_REQUESTED
  brain_web_evidence_pass_allowed: false
  llm_planner_call_count: 0
  web_search_task_count: 0
  web_search_result_count: 0
  web_fetched_document_count: 0
  real_document_fetched_count: 0
  web_or_llm_accepted_claim_count: 0
```

정확한 뜻:

```text
Brain/Web이 죽어서 몰래 낮은 점수로 확정된 것이 아니다.
이번 canonical run에서는 Brain/Web을 요청하지 않았고, 안 했다고 기록했다.
```

쉬운 예:

```text
시험지를 제출하지 않은 학생에게 0점을 준 게 아니다.
"아직 시험 대상이 아니었음"이라고 따로 적은 상태다.
```

## SourceTask Count Confusion

현재 가장 헷갈리는 부분:

```text
source_task_realness_audit.source_task_execution_count: 92
brain_web_readiness_gate.source_task_execution_count: 0
```

이 둘은 같은 뜻이 아니다.

```text
92개:
  기존 ledger/cutover 기반 source task 정직성 검산.
  현재 `LEDGER_REFRESH_CENSUS` 범위에서 source-backed event claim이 있는지 본다.

0개:
  canonical Brain/Web run에서 새로 실행된 Web/Naver/LLM source task 수.
  brain_web_mode=disabled라서 0이 맞다.
```

비유:

```text
92개는 "기존 서류철에 붙어 있던 증빙 번호표를 다시 맞춰 본 것"이다.
0개는 "오늘 새로 웹 검색해서 가져온 서류가 없다"는 뜻이다.
```

따라서 아래 주장은 틀리다.

```text
source task가 92개 있으니 Web/Naver/LLM acquisition도 성공했다.
```

추가 가드:

```text
Brain/Web attempt summary count가 1 이상이어도,
아래 exported leaf count 중 하나라도 빠지면 운영 pass가 아니다.

brain_source_task_exported_count
brain_source_task_execution_exported_count
brain_evidence_document_exported_count
brain_evidence_anchor_exported_count
brain_score_contribution_exported_count
brain_stagecourt_trace_exported_count
brain_to_census_stage_exported_count
```

쉬운 예:

```text
"자료를 찾았다"는 말만 있고 실제 첨부파일 번호가 없으면 채점하면 안 된다.
```

## Full Thesis Smoke State

`samsung_hynix_full_thesis_smoke.json`:

```text
verdict: PENDING_FULL_THESIS_REFRESH
full_thesis_status: PENDING_FULL_THESIS_REFRESH
smoke_task_count: 14
target_full_thesis_archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
daily_event_and_full_thesis_separated: true
hardcoded_query_count: 0
score_allowed_before_execution: false
```

정확한 뜻:

```text
삼성전자/하이닉스 C06/HBM full thesis에 필요한 조사 task 계획은 있다.
하지만 이 task가 실제 source-backed claim, score contribution, StageCourt trace로 닫힌 것은 아니다.
```

쉬운 예:

```text
시험 범위표는 만들었다.
시험을 치르고 채점한 것은 아니다.
```

## Cross-Validation Commands

다음 리뷰어는 먼저 이 명령으로 산출물을 다시 읽어야 한다.

```bash
python - <<'PY'
import json, collections
from pathlib import Path

root = Path("output/census_v4/2026-07-01")
rows = [
    json.loads(line)
    for line in (root / "census_stage_status.jsonl").read_text().splitlines()
    if line.strip()
]

print("rows", len(rows))
for field in [
    "base_stage",
    "canonical_stage",
    "full_thesis_stage",
    "score_scale",
    "score_status",
    "investigation_status",
    "transition_overlay",
]:
    print(field, dict(collections.Counter(str(r.get(field)) for r in rows).most_common()))

print("verified_score_present", sum(r.get("verified_score") is not None for r in rows))
print("full_e2r_verified_score_present", sum(r.get("full_e2r_verified_score") is not None for r in rows))

for symbol in ["005930", "000660"]:
    row = next(r for r in rows if str(r.get("symbol")) == symbol)
    print(symbol, {
        "company_name": row.get("company_name"),
        "base_stage": row.get("base_stage"),
        "canonical_stage": row.get("canonical_stage"),
        "full_thesis_stage": row.get("full_thesis_stage"),
        "score_scale": row.get("score_scale"),
        "verified_score": row.get("verified_score"),
        "full_e2r_verified_score": row.get("full_e2r_verified_score"),
        "score_contribution_count": row.get("score_contribution_count"),
        "investigation_status": row.get("investigation_status"),
    })

for name in [
    "readiness_verdict.json",
    "goal_completion_audit.json",
    "brain_web_attempt_audit.json",
    "brain_web_readiness_gate_audit.json",
    "brain_stage_promotion_audit.json",
    "samsung_hynix_full_thesis_smoke.json",
    "test_result_artifact.json",
]:
    obj = json.loads((root / name).read_text())
    print(name, {
        key: obj.get(key)
        for key in [
            "verdict",
            "target_gate_verdict",
            "goal_completion_ready",
            "brain_web_evidence_pass_allowed",
            "full_thesis_smoke_pass_allowed",
            "attempt_mode",
            "planner_run_count",
            "real_provider_success_count",
            "source_task_execution_count",
            "accepted_claim_count",
            "brain_stagecourt_trace_exported_count",
            "brain_to_census_stage_exported_count",
            "cutover_export_ready",
            "brain_stage_trace_count",
            "brain_promoted_stage_row_count",
            "full_thesis_status",
            "test_count",
            "status",
        ]
        if key in obj
    })
PY
```

기대되는 핵심값:

```text
rows 3391
full_thesis_stage {'FULL_THESIS_NOT_RUN': 3391}
verified_score_present 0
full_e2r_verified_score_present 0
brain_web_attempt_audit.verdict NOT_REQUESTED
brain_web_readiness_gate_audit.brain_web_evidence_pass_allowed False
brain_stage_promotion_audit.brain_promoted_stage_row_count 0
samsung_hynix_full_thesis_smoke.verdict PENDING_FULL_THESIS_REFRESH
test_result_artifact.test_count 4942
test_result_artifact.status OK
```

## Overclaim Trap List

다음 문장이 보이면 실패로 봐야 한다.

```text
1. "전체 KRX 운영 Stage map 완성"
2. "삼성전자/하이닉스 HBM 점수 산출 완료"
3. "Brain/Web evidence pass"
4. "LLM claim extraction pass"
5. "Web/Naver acquisition pass"
6. "source task 92개라서 live source fetch 성공"
7. "Stage2-Watch   30개가 full thesis Stage2 30개"
8. "Red 1개가 full thesis Stage3-Red 운영 판정"
9. "accepted_claim_count 92개가 full thesis 92개"
10. "full_thesis_smoke_tasks 14개가 full thesis 실행 완료"
11. "DISABLED_HONESTY_PASS가 기능 성공"
12. "anti_fake exit 0이 meaningful/brain_web/full_thesis exit 0"
```

## Must-Fail Negative Review Cases

다음 조건이 하나라도 관측되면 다음 에이전트는 fail을 걸어야 한다.

```text
1. verified_score가 null이 아닌 row가 있는데 score_scale != FULL_E2R_100
2. full_e2r_verified_score가 null이 아닌 row가 있는데 full thesis trace가 없음
3. full_thesis_stage != FULL_THESIS_NOT_RUN인데 full thesis StageCourt trace가 없음
4. Brain/Web disabled인데 brain_web_evidence_pass_allowed=true
5. planner_run_count=0인데 LLM-driven Census라고 문서화
6. web_search_task_count=0인데 Web/Naver acquisition pass라고 문서화
7. brain_stagecourt_trace_exported_count > 0인데 accepted claim/support id 없이 stage promotion
8. brain_to_census_stage_exported_count=0인데 operating Stage promotion 완료라고 문서화
9. source_task_real_fetch_count=0인데 live source coverage pass라고 문서화
10. Stage0/NoCurrentCatalyst row에 score evidence가 붙음
11. source_proxy_only/snapshot evidence가 production accepted claim으로 승격
12. old risk 또는 wrong-subject claim이 current hard break로 반영
```

## Patch Direction

다음 패치는 아래 순서가 맞다.

### P0. 현재 truth/honesty gate 고정

목표:

```text
현재처럼 anti-fake pass와 운영 pass를 분리한 상태를 유지한다.
문서나 CLI가 Brain/Web/full-thesis 미실행을 pass로 말하지 못하게 한다.
```

검증:

```text
target_gate=meaningful
target_gate=brain_web
target_gate=full_thesis
```

가 현재 상태에서 exit 0으로 끝나면 안 된다.

### P1. Production SourceTask -> EvidenceClaim acquisition 구현

목표:

```text
CandidateEvent
-> official-first SourceTask
-> EvidenceDocument
-> EvidenceAnchor
-> raw assertion
-> accepted/rejected EvidenceClaim
```

중요:

```text
일반 웹/Naver는 fallback이다.
DART/KIND/KRX/IR/CompanyGuide로 풀 수 있는 gap은 먼저 official source로 가야 한다.
```

### P2. Contract-blind LLM extractor

목표:

```text
LLM은 점수표를 보지 않고 원문에서 claim 후보만 뽑는다.
LLM 출력에는 score, stage, current_score_eligible, verified final이 들어가면 안 된다.
```

쉬운 예:

```text
나쁜 방식:
  "C06 Green에 뭐가 부족한지 보고 이 문서에서 점수 칸을 채워라."

좋은 방식:
  "이 문서가 말하는 주체, 사건, 날짜, 수치, 문장 위치를 뽑아라."
```

### P3. Entity/Temporal/Primitive adjudication 분리

목표:

```text
주체가 대상 회사인지,
현재 as_of_date에 살아 있는 claim인지,
어느 primitive에 mapping되는지,
각 단계를 분리해 기록한다.
```

월덱스/삼성전자 오류를 막는 핵심이다.

```text
월덱스 감사의견 정상 + 삼성전자 고객사 언급
-> subject는 월덱스
-> target은 삼성전자
-> relation은 indirect/customer/supplier
-> polarity는 normal
-> 삼성전자 accounting hard break는 0
```

### P4. Brain Stage strict promotion

목표:

```text
Brain/Web claim
-> score contribution
-> StageCourt trace
-> representative census_stage_status row
```

이 네 단계가 같은 claim/support id로 이어질 때만
`brain_to_census_stage_exported_count`를 1 이상으로 올린다.

### P5. Samsung/Hynix C06 full thesis smoke

목표:

```text
daily event Stage1과 별도로
C06/HBM full thesis SourceTask를 실제 실행한다.
```

성공 조건:

```text
source-backed C06 primitive coverage
score contribution ledger
StageCourt trace
score interval / material gap status
full_thesis_stage update 또는 explicit PENDING_MATERIAL_GAPS
```

점수가 낮아도 괜찮다.
근거 없는 점수나 매 실행마다 바뀌는 점수는 안 된다.

### P6. All-archetype Evidence Contract v2 / replay parity

목표:

```text
C01~C36 아키타입별
required/alternative primitive,
source quorum,
freshness/lifecycle,
guard/hard break,
stage gate를 schema로 고정한다.
```

주의:

```text
아키타입별 ontology는 필요하다.
종목명/URL/키워드 예외 하드코딩은 금지다.
```

## Final Reviewer Questions

다음 에이전트가 마지막에 물어야 할 질문:

```text
1. 지금 말하는 PASS가 정확히 어떤 target_gate의 PASS인가?
2. FULL_E2R_100 점수가 하나라도 존재하는가?
3. Brain/Web accepted claim이 representative census row로 승격됐는가?
4. 삼성전자/하이닉스 full thesis Stage가 `FULL_THESIS_NOT_RUN`에서 벗어났는가?
5. 벗어났다면 source-backed claim, contribution, StageCourt trace가 모두 연결됐는가?
6. source_task 92개가 live fetch라고 오해될 문구가 남았는가?
7. disabled honesty pass를 기능 success처럼 쓴 문구가 남았는가?
8. Stage2-Watch/Red를 full thesis operating stage처럼 쓴 문구가 남았는가?
9. known-bad fixture가 report가 아니라 leaf artifact/code path를 실제로 검사하는가?
10. target_gate=meaningful/brain_web/full_thesis가 미완료 상태에서 실패하는가?
```

## Final Judgment

현재 상태를 한 문장으로 고정하면 다음이다.

> `Census v4`는 가짜 완료 선언과 trace/score 혼합을 막는 anti-fake 상태판으로는 통과했지만, Brain/Web/LLM source acquisition과 삼성전자/하이닉스 C06 full thesis 운영 점수는 아직 실행/승격되지 않았다.

따라서 다음 리뷰어가 내려야 할 기본 판정:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS: 인정
MEANINGFUL_OPERATIONAL_STAGE_PASS: 불인정
BRAIN_WEB_EVIDENCE_PASS: 불인정
FULL_THESIS_SMOKE_PASS: 불인정
전 아키타입 replay parity: 불인정
```

이 상태를 숨기지 않고 드러낸 것이 이번 문서화의 목적이다.
