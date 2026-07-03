# Census v4 v90 - Operational Stage Truth Cross Validation And Next Patch Direction

작성일: 2026-07-03

이 문서는 다음 에이전트가 2026-07-01 Census v4 결과를 빡세게 검증할 때 먼저 읽어야 하는 최신 상태판이다.

핵심 질문:

```text
뭔가 잘못되고 있는가?
Stage가 있는 종목이 있기는 한가?
있다면 운영 Stage인가, 아니면 상태판 Stage인가?
```

## 1. 짧은 결론

Stage row는 있다.

하지만 현재 운영자가 "이 종목은 FULL_THESIS 기준 Stage 2/3/Green/Yellow"라고 써도 되는 row는 없다.

```text
census_stage_map.csv rows = 3391
canonical_stage != 0 rows = 85
stage_scope = CENSUS_EVENT_BOARD rows = 3390
stage_scope = BRAIN_WEB_PARTIAL rows = 1
stage_scope = FULL_THESIS rows = 0
FULL_E2R_100 verified score rows = 0
operator_stage_use = NOT_FULL_THESIS_STAGE rows = 3391
operator_score_use = NOT_FULL_E2R_SCORE rows = 3391
```

쉽게 말하면:

```text
CENSUS_EVENT_BOARD Stage = 출석부/상태판
BRAIN_WEB_PARTIAL Stage = 부분 쪽지시험
FULL_THESIS Stage = 운영 진단서

현재 출석부와 쪽지시험은 있지만,
운영 진단서는 0장이다.
```

따라서 지금 "Stage가 있는 애들이 있긴 해?"의 정확한 답은:

```text
상태판 Stage는 있다.
운영 FULL_THESIS Stage는 없다.
```

## 2. 근거 파일

기준 output:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82
```

핵심 근거:

```text
census_stage_map.csv
readiness_verdict.json
goal_completion_audit.json
brain_web_readiness_gate_audit.json
full_thesis_production_audit.json
samsung_hynix_full_thesis_smoke.json
all_archetype_replay_matrix.json
```

v89 source capability 검증 artifact:

```text
output/test_census_v4_cached/source_connector_capability_audit.json
```

주의:

```text
v82 output은 live Brain/Web bounded run의 현재 truth다.
v83~v90은 주로 거짓 pass를 막는 guard/audit/code/doc patch다.
v90 문서는 v82 truth를 READY로 바꾸지 않는다.
```

## 3. Stage row 재계산

직접 재계산한 값:

```text
stage_scope:
  CENSUS_EVENT_BOARD = 3390
  BRAIN_WEB_PARTIAL = 1
  FULL_THESIS = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

score_scale:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1
```

이 값이 의미하는 것:

```text
canonical_stage 1/2/3-Red가 있어도
stage_scope가 FULL_THESIS가 아니면 운영 Stage가 아니다.
```

쉬운 예:

```text
학생 명단에 "주의 필요"라고 표시됨
-> 선생님이 한번 더 볼 필요가 있다는 상태판 표시

정식 성적표 90점
-> 시험 채점이 완료된 운영 결과

현재 Census v4에는 첫 번째 표시가 있고,
두 번째 성적표는 없다.
```

## 4. 삼성전자 / SK하이닉스 상태

삼성전자:

```text
symbol = 005930
stage_scope = CENSUS_EVENT_BOARD
canonical_stage = 1
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
full_thesis_stage = FULL_THESIS_NOT_RUN
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_e2r_verified_score = null
```

SK하이닉스:

```text
symbol = 000660
stage_scope = BRAIN_WEB_PARTIAL
canonical_stage = 1
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 60.0
full_thesis_stage = FULL_THESIS_NOT_RUN
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_e2r_verified_score = null
```

중요:

```text
SK하이닉스 60점은 FULL_E2R_100 운영 점수가 아니다.
삼성전자 4점도 FULL_E2R_100 운영 점수가 아니다.
둘 다 EVENT_WEIGHTED_PARTIAL이다.
```

`samsung_hynix_full_thesis_smoke.json`도 같은 결론이다.

```text
verdict = PENDING_FULL_THESIS_REFRESH
full_thesis_status = PENDING_FULL_THESIS_REFRESH
target_full_thesis_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
score_allowed_before_execution = false
hardcoded_query_count = 0
daily_event_and_full_thesis_separated = true
```

각 symbol의 blocker:

```text
blocking_reason = full_thesis_source_tasks_planned_but_not_executed
full_thesis_claim_ids = []
full_thesis_score_contribution_ids = []
full_thesis_stagecourt_trace_ids = []
missing_full_thesis_primitives = full_thesis_refresh_task_not_run
smoke_pass_allowed = false
```

쉽게 말하면:

```text
삼성전자/하이닉스 C06 full thesis용 준비물 목록은 만들어졌지만,
그 준비물로 실제 원문을 가져와 claim을 만들고 점수를 낸 실행은 아직 안 끝났다.
```

## 5. Readiness / Goal 상태

`readiness_verdict.json`:

```text
verdict = NOT_READY
meaningful_operational_stage_pass = false
brain_web_evidence_pass = false
full_thesis_production_pass = false
operational_stage_use_allowed = false
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
event_board_non_stage0_count = 84
full_thesis_refresh_queue_candidate_count = 84
```

`goal_completion_audit.json`:

```text
goal_completion_ready = false
meaningful_operational_stage_pass_allowed = false
brain_web_evidence_pass_allowed = false
full_thesis_smoke_pass_allowed = false
full_thesis_production_pass_allowed = false
full_thesis_seed_promotion_pass_allowed = false
all_archetype_replay_pass_allowed = false
```

현재 goal blocker:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
source_backed_replay_parity_all_archetypes_pending
goal_requirement_matrix_pass_false
```

`goal_requirement_matrix_audit.json`:

```text
required_goal_completion_count = 19
required_goal_completion_pass_count = 14
required_goal_completion_pending_count = 5
required_goal_completion_fail_count = 0
pending_gate_ids =
  FULL_THESIS_SMOKE_PASS
  FULL_THESIS_PRODUCTION_PASS
  FULL_THESIS_SEED_PROMOTION_PASS
  BRAIN_WEB_EVIDENCE_PASS
  ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

중요한 해석:

```text
fail이 0개라는 말은 성공했다는 뜻이 아니다.
pending이 5개라서 goal_completion_ready=false다.
```

쉬운 예:

```text
서류 심사에서 "반려"는 없지만,
필수 서류 5개가 아직 미제출이면 합격이 아니다.
```

## 6. Brain/Web은 어디까지 왔나

`brain_web_readiness_gate_audit.json`:

```text
verdict = BLOCKED
brain_web_evidence_pass_allowed = false
llm_planner_call_count = 21 / required 30
web_search_task_count = 3 / required 20
web_search_call_count = 3 / required 20
web_fetched_document_count = 1 / required 10
llm_claim_extractor_attempt_count = 1 / required 10
web_or_llm_accepted_claim_count = 5 / required 3
```

여기서 accepted claim 5개가 있어도 pass가 아닌 이유:

```text
운영 Brain/Web pass는 claim 개수만 보는 게 아니다.
planner, web task, search call, fetched document, claim extractor attempt,
score contribution, StageCourt, census promotion이 모두 닫혀야 한다.
```

쉬운 예:

```text
정답 5개를 썼어도,
시험지가 아니라 연습장에 쓴 답이면 성적표가 아니다.
```

## 7. FULL_THESIS production runner 상태

`full_thesis_production_audit.json`:

```text
verdict = PENDING_FULL_THESIS_PRODUCTION
production_pass_allowed = false
production_mode_requested = true
production_runner_implemented = true
full_thesis_refresh_queue_candidate_count = 84
production_full_thesis_row_count = 0
full_thesis_row_count = 0
blockers = production_full_thesis_runner_no_eligible_rows
```

해석:

```text
runner 자체는 있다.
하지만 현재 queue에서 FULL_THESIS row로 승격 가능한 eligible row가 없다.
```

이걸 "Stage가 없다"와 구분해야 한다.

```text
Stage 표시 row는 있다.
FULL_THESIS production row가 없다.
```

## 8. All-archetype replay 상태

`all_archetype_replay_matrix.json`:

```text
all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
source_proxy_leak_count = 0
```

status:

```text
SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY = 6
GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
SOURCE_GAP_PENDING = 26
```

해석:

```text
source_proxy가 점수로 새는 문제는 막고 있다.
하지만 전체 아키타입 32개 기준 source-backed positive/guard replay parity는 아직 6개뿐이다.
```

즉 "모든 아키타입이 운영 점수로 닫혔다"라고 말하면 안 된다.

## 9. v89 source capability 패치의 정확한 의미

v89는 중요한 진전이다.

v88에서는 registry connector만 보고 다음 source class까지 "통로 없음"으로 봤다.

```text
NaverSearch
GeneralWebSearch
CompanyNewsroom
BrokerReportPublicPDF
ReportPDF
```

v89에서는 이들을 bounded `SourceAcquisitionRunnerV4` 경로로 분류했다.

```text
bounded_web_acquisition_source_classes =
  BrokerReportPublicPDF
  CompanyNewsroom
  GeneralWebSearch
  NaverSearch
  ReportPDF

registry_missing_but_acquisition_covered_source_classes =
  BrokerReportPublicPDF
  CompanyNewsroom
  GeneralWebSearch
  NaverSearch
  ReportPDF

blocking_full_thesis_source_class_count = 2
blocking_full_thesis_source_classes =
  IssuerIR
  TrustedNews

blocking_full_thesis_task_count = 0
full_thesis_task_executable_source_path_pass_allowed = true
full_thesis_task_with_blocking_source_class_count = 83
```

정확한 해석:

```text
83개 task가 IssuerIR/TrustedNews를 언급하지만,
다른 실행 가능한 source class도 같이 갖고 있으므로
"실행 가능한 source path가 전혀 없는 task"는 0개다.
```

하지만 이 말은 점수 가능이라는 뜻이 아니다.

```text
source path executable
!= fetched document exists
!= accepted claim exists
!= score contribution exists
!= FULL_THESIS Stage exists
```

쉬운 예:

```text
우편함이 생겼다.
하지만 우편물이 실제로 도착했고,
그 안에 필요한 서류가 있고,
그 서류가 유효하다는 뜻은 아니다.
```

## 10. 다음 에이전트가 공격해야 할 지점

다음 에이전트는 아래 질문을 반드시 던져야 한다.

```text
1. v89의 bounded acquisition capability가 live fetch success로 과장되고 있지 않은가?
2. Naver/title/snippet만으로 score contribution이 생기는 경로가 남아 있지 않은가?
3. CompanyNewsroom lineage가 as_of_date 이후에 추가된 공식 domain registry를 쓰지 않는가?
4. BrokerReportPublicPDF가 arbitrary PDF나 블로그 PDF를 report original로 받아들이지 않는가?
5. IssuerIR/TrustedNews placeholder를 진짜 blocker로 계속 남기고 있는가?
6. FULL_THESIS_SMOKE를 production FULL_THESIS로 대체하는 문구가 남아 있지 않은가?
7. `EVENT_WEIGHTED_PARTIAL` 60점을 FULL_E2R_100 점수처럼 표시하는 UI/리포트가 남아 있지 않은가?
8. `canonical_stage=1/2/3-Red`를 stage_scope 확인 없이 운영 Stage로 읽는 코드가 남아 있지 않은가?
9. 삼성전자/하이닉스 full thesis smoke의 `full_thesis_claim_ids=[]` 상태를 숨기고 있지 않은가?
10. 84개 refresh queue가 실제 SourceTaskExecution으로 닫히지 않았는데 ready처럼 표시하는 곳이 없는가?
```

## 11. 다음 패치 우선순위

### P0. 운영 Stage 표시 차단은 유지

절대 바꾸면 안 되는 것:

```text
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
FULL_THESIS row = 0이면 운영 Stage 없음
FULL_E2R_100 row = 0이면 운영 점수 없음
```

`canonical_stage`만 보고 Stage를 출력하면 다시 같은 사고가 난다.

### P1. FULL_THESIS refresh queue를 실제 execution으로 닫기

현재:

```text
full_thesis_refresh_queue_candidate_count = 84
full_thesis_stage = FULL_THESIS_NOT_RUN
```

목표:

```text
refresh queue candidate
-> bounded SourceTaskExecution
-> EvidenceDocument
-> EvidenceAnchor
-> accepted claim
-> PrimitiveState
-> ScoreContribution
-> StageCourt
-> promoted FULL_THESIS row
```

이 중 하나라도 빠지면 운영 Stage가 아니다.

### P2. IssuerIR / TrustedNews source class를 닫기

현재 남은 source capability blocker:

```text
IssuerIR = PLACEHOLDER_PROVIDER_FAILED
TrustedNews = PLACEHOLDER_PROVIDER_FAILED
```

선택지는 둘 중 하나다.

```text
1. 실제 provider 구현
2. Evidence Contract/source policy에서 대체 가능한 source class로 명시 재분류
```

주의:

```text
"TrustedNews가 없으니 NaverSearch로 대체"를 암묵적으로 하면 안 된다.
source quorum과 lineage policy에 명시해야 한다.
```

### P3. Brain/Web 운영 minimum을 채우기

현재 blocker:

```text
planner runs 21/30
web search tasks 3/20
web/news search calls 3/20
fetched documents 1/10
claim extractor attempts 1/10
```

목표는 단순 숫자 채우기가 아니다.

```text
source task가 실제 원문을 가져오고,
그 원문에서 accepted claim이 생기고,
claim이 score contribution과 StageCourt까지 연결되어야 한다.
```

### P4. All-archetype source-backed replay를 32개로 확장

현재:

```text
required_archetype_count = 32
source_backed_ready_count = 6
missing_required_archetype_count = 26
```

다음 목표:

```text
각 required archetype마다
positive replay와 guard replay를 source-backed로 닫는다.
source_proxy_only row는 운영 정답으로 쓰지 않는다.
```

### P5. v82 live output을 최신 guard로 재실행

v83~v90은 guard와 audit를 강화했다.

하지만 현재 live truth artifact는 아직:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82
```

이다.

따라서 다음 큰 실행은:

```text
latest code
same as_of_date or explicit new as_of_date
bounded production daily mode
Brain/Web enabled
write_operational_docs=True
```

로 다시 돌려야 한다.

그때도 반드시 아래를 분리한다.

```text
state board result
partial Brain/Web result
FULL_THESIS result
FULL_E2R_100 score
provider/source pending
```

## 12. 다음 에이전트 acceptance 질문

다음 에이전트는 "테스트 통과"만 보지 말고 아래 질문에 답해야 한다.

```text
1. FULL_THESIS row가 0보다 커졌는가?
2. 그 row의 operator_stage_use가 FULL_THESIS_STAGE_USE_ALLOWED인가?
3. 그 row의 score_scale이 FULL_E2R_100인가?
4. nonzero score contribution마다 support_claim_id가 있는가?
5. support_claim_id가 EvidenceAnchor와 SourceTaskExecution까지 이어지는가?
6. source path가 controlled smoke나 snapshot fixture가 아닌가?
7. Brain/Web minimum count가 실제 leaf row 기준으로 충족되는가?
8. 삼성전자/하이닉스는 C06 full thesis로 실행됐는가, 아니면 daily event partial인가?
9. 2020년/타사/정상 감사의견 같은 wrong-subject old-risk fixture가 계속 0점인가?
10. all-archetype replay 32개가 source-backed positive/guard로 닫혔는가?
```

이 질문 중 하나라도 답이 "아니오"면 아직 운영 ready가 아니다.

## 13. 현재 검증 결과

최신 코드/문서 패치 후 실행:

```bash
PYTHONPATH=src python -m py_compile src/e2r/census/census_runner_v4.py
PYTHONPATH=src python -m unittest tests.test_census_v4_goal_required_audits -v
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
py_compile = OK
tests.test_census_v4_goal_required_audits = 4 tests OK
census v4 test_census_v4_* = 139 tests OK
full unittest discover = 5122 tests OK
```

중요:

```text
테스트 통과는 "거짓 READY를 막는 guard가 작동한다"는 뜻이다.
운영 FULL_THESIS Stage가 생겼다는 뜻이 아니다.
```

## 14. 최종 판단

현재 시스템은 이전보다 정직해졌다.

좋아진 점:

```text
Stage row와 운영 Stage를 분리한다.
EVENT_WEIGHTED_PARTIAL과 FULL_E2R_100을 분리한다.
controlled smoke와 production full thesis를 분리한다.
registry connector와 bounded acquisition capability를 분리한다.
snippet/source_proxy/old wrong-subject risk가 score로 새는 것을 막는 테스트가 있다.
```

아직 안 된 점:

```text
운영 FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
Brain/Web operational minimum 미충족
FULL_THESIS refresh queue 84개 미실행
IssuerIR/TrustedNews placeholder 잔존
all-archetype source-backed replay 6/32
```

따라서 현재 결론은:

```text
NOT_READY가 맞다.
Stage가 전혀 없는 것은 아니지만,
운영에 써도 되는 FULL_THESIS Stage는 아직 없다.
다음 패치는 점수 threshold 조정이 아니라
refresh queue -> source task execution -> accepted claim -> score contribution -> StageCourt -> FULL_THESIS row 경로를 실제로 닫는 것이다.
```
