# Census v4 0701 Stage Existence + C24 Patch Cross-Review Packet

작성일: 2026-07-02  
기준 산출물: `output/census_v4/2026-07-01`  
기준 테스트 artifact: `output/test_full_repo_0701/full_unittest_result_artifact.json`

## 한 줄 결론

```text
Stage는 있다.
하지만 전부 CENSUS_EVENT_BOARD 상태판 Stage다.
FULL_THESIS 운영 Stage와 FULL_E2R_100 verified score는 아직 0개다.
```

쉬운 예:

```text
전교 학생 3391명을 출석부에 올리고 "오늘 별일 없음 / 관찰 필요 / 위험 신호"를 붙인 상태다.
아직 각 학생별로 전체 시험지를 채점해서 100점 만점 등급을 낸 것은 아니다.
```

따라서 다음 두 문장은 동시에 참이다.

```text
1. stage row는 3391개 있다.
2. 운영 full thesis stage row는 0개다.
```

이 둘을 섞으면 다시 "Stage가 있다더니 왜 운영 점수가 없냐"는 혼란이 생긴다.

## 현재 Stage 실측

명령:

```bash
python - <<'PY'
import json, collections
from pathlib import Path
root=Path('output/census_v4/2026-07-01')
rows=[json.loads(l) for l in (root/'census_stage_status.jsonl').read_text().splitlines() if l.strip()]
print('stage_rows', len(rows))
print('base_stage', dict(collections.Counter(r.get('base_stage') for r in rows)))
print('canonical_stage', dict(collections.Counter(r.get('canonical_stage') for r in rows)))
print('stage_scope', dict(collections.Counter(r.get('stage_scope') for r in rows)))
print('score_scope', dict(collections.Counter(r.get('score_scope') for r in rows)))
print('full_thesis_rows', sum(1 for r in rows if r.get('stage_scope')=='FULL_THESIS'))
print('verified_score_rows', sum(1 for r in rows if r.get('verified_score') is not None or r.get('full_e2r_verified_score') is not None))
print('event_evidence_score_rows', sum(1 for r in rows if r.get('event_evidence_score') is not None))
PY
```

결과:

```text
stage_rows = 3391

base_stage:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

stage_scope:
  CENSUS_EVENT_BOARD = 3391

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67

full_thesis_rows = 0
verified_score_rows = 0
event_evidence_score_rows = 67
```

해석:

```text
Stage1/Stage2-Watch/Red가 있긴 하다.
하지만 이것은 daily census event-board 상태다.
삼성전자/하이닉스 같은 full thesis 운영 점수 산출물은 아니다.
```

## 왜 이게 "잘못되고 있는 것"처럼 보였나

이름이 Stage라서 헷갈렸다.

현재 산출물의 Stage는 두 종류가 섞이지 않도록 `stage_scope`로 분리되어 있다.

```text
CENSUS_EVENT_BOARD:
  전체 종목 상태판.
  새 공시, 공식 이벤트, 일부 claim, pending/provider 상태를 표시한다.

FULL_THESIS:
  한 종목에 대해 Evidence OS가 충분한 source-backed claim을 모아
  full E2R score/stage를 확정하는 운영 평가다.
```

현재는:

```text
CENSUS_EVENT_BOARD = 있음
FULL_THESIS = 없음
```

그래서 "stage가 있는 애들이 있긴 해?"의 정확한 답은:

```text
있다. Stage1 54개, Stage2-Watch 30개, Red 1개가 있다.
다만 그건 event-board Stage다.
운영 full thesis Stage는 아직 없다.
```

## Census Event와 Candidate Event 분리 상태

정상 원칙:

```text
CensusAssessmentEvent:
  모든 종목에 붙는 "이번 census에서 평가했다"는 행정 스탬프.
  점수 재료가 아니다.

CandidateEvent:
  실제 공시/실적/뉴스/리스크 같은 사건.
  source-backed claim으로 닫힐 때만 점수 재료가 된다.
```

쉬운 예:

```text
아무 새 공시가 없는 종목:
  CensusAssessmentEvent 있음
  CandidateEvent 없음
  accepted claim 없음
  Stage0 / NO_SCORE

공식 계약 공시가 있는 종목:
  CensusAssessmentEvent 있음
  CandidateEvent 있음
  source-backed claim 있음
  Stage1 또는 Stage2-Watch 가능
```

현재 leaf audit에서 이쪽 핵심 오류는 0이다.

```text
assessment_event_score_evidence_allowed_count = 0
assessment_only_nonzero_score_count = 0
candidate_event_ids_contain_assessment_event_count = 0
market_anomaly_to_score_count = 0
price_path_only_to_score_count = 0
news_snippet_to_score_count = 0
provider_failed_final_score_count = 0
```

즉 "전 종목에 census event가 있으니 억지 점수"로 가는 문제는 현재 audit상 막혀 있다.

## C24 패치 요약

이번 패치로 C24 `BIO_TRIAL_DATA_EVENT_RISK`에 source-backed semantic replay를 추가했다.

추가 산출물:

```text
output/census_v4/2026-07-01/c24_source_backed_semantic_replay.json
```

핵심 결과:

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 5

positive_support_primitive_ids:
  trial_quality_visible

guard_counter_primitive_ids:
  binary_event_unresolved

binary_event_guard_leaked_support_primitives = []
production_score_evidence_allowed = false
```

사용한 source-backed fixture:

```text
Positive:
  HanAll Biopharma / Immunovant batoclimab Phase 2 business update
  URL: https://www.prnewswire.com/news-releases/hanall-biopharma-reports-full-year-2023-financial-results-and-provides-business-update-302095695.html

Guard:
  SillaJen PHOCUS Phase 3 futility/discontinuation announcement
  URL: https://www.prnewswire.com/news-releases/sillajen-announces-conclusions-from-interim-futility-analysis-of-phase-3-phocus-trial-in-hcc-300895539.html
```

쉬운 예:

```text
HanAll source:
  "Phase 2 결과, response/safety가 확인됨"
  -> trial_quality_visible replay positive

SillaJen source:
  "IDMC futility analysis, trial discontinuation"
  -> binary_event_unresolved guard
  -> trial_quality_visible positive로 새면 안 됨
```

현재 결과는 이 오염을 막는다.

```text
binary_event_guard_leaked_support_primitives = []
```

## 코드 패치 범위

변경 파일:

```text
src/e2r/production/claim_extraction/contract_blind_extractor.py
src/e2r/production/claim_extraction/primitive_mapper.py
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
data/replay_source_snapshots/replay_source_snapshots.jsonl
data/replay_source_snapshots/hanall_c24_positive_batoclimab_20240321.txt
data/replay_source_snapshots/sillajen_c24_guard_phocus_futility_20190802.txt
tests/test_census_v4_all_archetype_replay_matrix.py
tests/test_census_v4_goal_required_audits.py
```

중요한 설계 경계:

```text
종목명 하드코딩을 넣은 것이 아니다.
임상/endpoint/response/safety/futility/discontinuation 같은 C24 ontology predicate와 primitive mapping을 추가했다.

이 replay는 production score evidence가 아니다.
replay_only = true
production_score_evidence_allowed = false
```

## All-Archetype Replay Matrix 최신값

```text
all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 5
guard_replay_ready_count = 5
missing_required_archetype_count = 27
```

READY:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
```

우선순위 PENDING:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

주의:

```text
5/32 ready는 좋아진 것이다.
하지만 27개 required archetype이 아직 source-backed positive+guard replay가 없으므로
goal completion은 여전히 false다.
```

## Controlled Semantic Replay 최신값

```text
controlled_semantic_replay_pass = false
case_count = 10
pass_count = 9
pending_count = 1
fail_count = 0
blockers:
  C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

PASS:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
WRONG_SUBJECT_RISK_FIXTURE
OLD_RISK_RESOLVED_FIXTURE
PROVIDER_FAILURE_PENDING_FIXTURE
SEMANTIC_CONTRACT_GUARD_FIXTURE
```

PENDING:

```text
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

## Goal Completion 최신값

```text
goal_completion_ready = false
goal_completion_minimum_pass = false

required_goal_completion_count = 17
required_goal_completion_pass_count = 12
required_goal_completion_pending_count = 5
required_goal_completion_fail_count = 0
```

남은 blocker:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
controlled_semantic_replay_pending
goal_requirement_matrix_pass_false
```

해석:

```text
ANTI_FAKE gate는 통과했다.
하지만 meaningful operation gate는 아직 아니다.
```

쉬운 예:

```text
가짜 pass를 막는 보안문은 통과했다.
하지만 실제 영업 가능한 매장은 아직 아니다.
```

## 테스트 검증

Targeted tests:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_goal_required_audits -v

Ran 12 tests
OK
```

Census v4 tests:

```text
PYTHONPATH=src python -m unittest $(rg --files tests | rg 'tests/test_census_v4_.*\.py$' | sed 's#/#.#g; s#\.py$##') -v

Ran 115 tests
OK
```

Full repo tests:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 4996
failed_count = 0
error_count = 0
duration_seconds = 178.2787
log_sha256 = cc88a7a33fec07f7dd6b1d41def5df6887897dd0d9b01e491ab0dd419d5265b4
```

Canonical output 재생성:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json

ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

## 교차검증 관찰

1. C24 replay는 matrix와 controlled semantic audit에 모두 반영됐다.

```text
matrix:
  source_backed_ready_count 4 -> 5
  guard_replay_ready_count 4 -> 5
  missing_required_archetype_count 28 -> 27

controlled semantic:
  pass_count 8 -> 9
  pending_count 2 -> 1
```

2. C24 replay는 score로 새지 않았다.

```text
production_score_evidence_allowed = false
score_contribution_count = 0
```

3. Stage 상태판은 존재하지만 verified full thesis score는 없다.

```text
EVENT_WEIGHTED_PARTIAL rows = 67
FULL_E2R_100 rows = 0
FULL_THESIS rows = 0
```

4. leaf audit상 old Samsung/Worldex류 오귀속, provider failure final score, snippet score leakage는 0이다.

```text
wrong subject risk fixture = PASS
old resolved risk fixture = PASS
provider failure pending fixture = PASS
news_snippet_to_score_count = 0
source_proxy_to_score_count = 0
evidence_url_pending_to_score_count = 0
```

## 아직 약한 지점

### 1. C24 guard direction 표현이 완전히 아름답지는 않다

현 C24 guard output:

```text
guard_support_primitive_ids = ["binary_event_unresolved"]
guard_counter_primitive_ids = ["binary_event_unresolved"]
```

왜 통과했나:

```text
pass 조건은 binary_event_unresolved counter가 존재하고,
trial_quality_visible support leak이 없어야 한다.
```

리뷰어가 공격할 지점:

```text
같은 primitive가 SUPPORT와 COUNTER에 동시에 나타나는 것이 장기적으로 괜찮은가?
negative/risk primitive의 direction schema를 더 명확히 해야 하지 않는가?
```

내 판단:

```text
현재 C24 replay의 핵심 false-positive 방어에는 문제가 없다.
하지만 후속 패치에서는 guard/risk primitive의 support_direction 표현을 정규화하는 편이 낫다.
```

### 2. C24 positive는 trial quality만 열었다

C24 contract에는 아래 risk/bridge도 있다.

```text
binary_event_unresolved
approval_not_confirmed
safety_signal
cash_runway_risk
```

이번 replay는 C24 전체 Green thesis가 아니다.

```text
trial_quality_visible positive path와 binary-event guard를 닫은 것뿐이다.
```

### 3. C28이 남아 있다

현재 controlled semantic의 마지막 blocker:

```text
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

필요한 것:

```text
positive:
  ARR / RPO / renewal / retention / churn / multi-year contract bridge

guard:
  software/security 키워드만으로 retention bridge를 열지 않기
```

### 4. 27개 required archetype은 여전히 source-backed replay gap

현재 5/32 ready다.

```text
좋아진 것은 맞지만 "전 아키타입 운영 준비"와는 거리가 있다.
```

## 다음 패치 방향

우선순위:

```text
1. C28 source-backed positive + guard replay
2. guard/risk primitive direction schema 정리
3. FULL_THESIS smoke/prod source task execution을 실제 source-backed claim chain에 연결
4. real Brain/Web evidence gate를 실제 provider/planner/fetch/extractor rows로 닫기
5. 나머지 27개 required archetype replay 확장
```

절대 하지 말 것:

```text
1. threshold나 weight를 먼저 조정하지 말 것
2. "Stage가 없으니 낮은 점수라도 확정"으로 처리하지 말 것
3. source_proxy_only / evidence_url_pending 연구자료를 production score evidence로 쓰지 말 것
4. CENSUS_EVENT_BOARD Stage를 FULL_THESIS 운영 Stage처럼 설명하지 말 것
5. C24 replay pass를 C24 운영 Green pass로 부풀리지 말 것
```

## 다음 에이전트 공격 질문

아래 질문에 모두 견뎌야 한다.

```text
1. Stage row가 있다는 말이 FULL_THESIS 운영 Stage와 혼동되지 않는가?
2. Stage1 54개, Stage2-Watch 30개, Red 1개가 왜 전부 event-board scope인지 산출물로 증명했는가?
3. C24 accepted_claim_count=5가 실제 URL anchor에서 온 것인가?
4. C24 source URL이 source-proxy/snapshot URL로 대체되지 않았는가?
5. SillaJen futility guard가 trial_quality_visible positive support로 새지 않았는가?
6. C24 replay가 production score contribution으로 새지 않았는가?
7. C24 pass 반영 후 all_archetype matrix 숫자가 5/32/27로 바뀌었는가?
8. controlled semantic blocker가 C28 하나만 남았는가?
9. full repo test artifact가 최신 4996 OK인가?
10. goal_completion_ready=false를 유지하고 있는가?
11. ANTI_FAKE pass를 meaningful operation pass로 과장하지 않았는가?
12. 다음 패치가 C28과 full thesis/Brain-Web gate라는 점을 명확히 했는가?
```

## 최종 판정

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS:
  PASS

Stage exists:
  YES, CENSUS_EVENT_BOARD scope only

Operational FULL_THESIS Stage:
  NO, 0 rows

FULL_E2R_100 verified score:
  NO, 0 rows

C24 source-backed replay:
  PASS

Controlled semantic replay:
  FALSE, 9/10 pass, C28 pending

All-archetype source-backed replay:
  FALSE, 5/32 ready, 27 pending

Goal completion:
  FALSE
```

