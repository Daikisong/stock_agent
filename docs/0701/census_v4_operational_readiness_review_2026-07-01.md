# Census v4 Operational Readiness Review - 2026-07-01

작성일: 2026-07-01  
대상 실행: `output/census_v4/2026-07-01`  
대상 문서/리포트: `docs/operational/census_mode_v4_*`  
주의: 이 문서는 다음 에이전트가 강하게 피드백할 수 있도록, 통과한 것과 아직 못 통과한 것을 의도적으로 분리해서 적는다.

## 한 줄 결론

현재 v4는 **가짜 운영 Stage처럼 보이는 문제를 많이 막은 상태판**이다.

하지만 아직 **실제 운영 full E2R Stage/점수 지도**는 아니다.

정확한 현재 이름은 다음이다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
= 전 종목 상태 row는 만들었고,
  단일 이벤트 점수와 full thesis 점수를 섞지 않으며,
  trace/claim/score id가 서로 다른 row에서 섞이는 문제를 막은 상태
```

아직 아닌 것:

```text
MEANINGFUL_OPERATIONAL_STAGE_PASS
= 현재부터 실제 운영한다고 했을 때,
  전 종목 또는 운영 후보의 full thesis를 증거 claim으로 채워
  verified_score와 Stage를 안정적으로 산출한 상태
```

## PASS 범위 경고

이 문서에서 말하는 PASS는 운영 점수/Stage 준비 완료가 아니다.

```text
현재 PASS:
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS 범위

뜻:
- 전 종목 상태 row가 있다.
- CensusAssessmentEvent와 CandidateEvent를 섞지 않는다.
- claim 없는 점수, score/trace 혼합, event score를 full score처럼 보이게 하는 문제를 막는다.
- 부분 이벤트 점수가 붙은 row는 `sample_leaf_bundle.jsonl`과 `artifact_manifest.json`으로 재검산할 수 있다.
- legacy v1 runner, 빈 claim builder, old CLI pass claim, v4 CLI miswire는 static audit에서 0이어야 한다.

아직 PASS 아님:
- Brain/Web/LLM acquisition
- full thesis scoring
- FULL_E2R_100 verified score
- Stage3-Green / Stage3-Yellow / Stage3-Red / 4B / 4C 운영 판정
- 전 아키타입 연구자료 replay parity
```

쉬운 예:

```text
현재 PASS는 "가짜 성적표 방지 장치가 작동한다"는 뜻이다.
"학생별 기말고사 점수가 모두 채점됐다"는 뜻이 아니다.
```

쉬운 예:

```text
현재 v4:
출석부는 전원 있고,
오늘 확인된 공시 이벤트에는 번호표와 근거가 붙어 있다.
하지만 전체 기말고사 점수는 아직 안 냈다.

아직 필요한 상태:
각 학생의 전체 시험 답안지를 채점해서,
100점 만점 종합 점수와 등급을 재현 가능하게 내는 것.
```

## 사용자가 물은 질문에 대한 답

질문:

```text
뭔가 잘못되고있는거맞지? stage가 있는애들이 있긴해?
```

답:

```text
Stage가 있는 종목은 있다.
하지만 그 Stage는 전부 "full thesis 운영 Stage"가 아니라
"공식 이벤트/부분 증거 상태 Stage"다.
```

v4 산출물 기준:

아래 `Stage0/Stage1/Stage2-Watch/Red`는 event-board display label이다.
`Stage3-Green/Yellow/Red/4A/4B/4C/5` 0개는 full thesis operating Stage label이 아직 없다는 뜻으로 읽어야 한다.

```text
총 row: 3391

Stage0:       3306
Stage1:         54
Stage2-Watch:   30
Red:             1

Stage3-Green:   0
Stage3-Yellow:  0
Stage3-Red:     0
4A/4B/4C/5:      0
```

주의:

```text
canonical_stage 3-Red: 1
!= full thesis operating Stage3-Red 1

현재 canonical_stage 3-Red 1개는 event-board Red를 canonical enum으로 매핑한 값이다.
stage_scope=CENSUS_EVENT_BOARD라서 운영 full thesis Red가 아니다.
```

Stage 용어 주의:

```text
base_stage의 Stage2-Watch / Red는 현재 v4 산출물의 표시 label이다.
canonical_stage는 프로젝트 canonical enum으로 따로 기록된다.

canonical_stage:
0:       3306
  1:         54
  2:         30
3-Red:      1

여기서 `Stage3-Red: 0`과 `canonical_stage 3-Red: 1`은 모순이 아니다.
```

```text
Stage3-Red: 0
= full thesis 운영 Stage3-Red 확정 row는 0개다.

canonical_stage 3-Red: 1
= 표시 label Red 1개가 canonical enum으로는 3-Red에 매핑됐다는 뜻이다.
  이 row도 full_thesis_stage는 FULL_THESIS_NOT_RUN이다.
```

```text
Stage2-Watch   30개
!= full thesis Stage 2 확정 30개

뜻:
candidate event 또는 material claim이 있어서 watch 상태로 올라왔고,
cash/revision/multi-source bridge 같은 material gap이 남은 row 30개다.
```

중요한 해석:

```
Stage1 / Stage2-Watch가 있다는 것
!= full E2R verified_score가 있다는 것

현재 full_e2r_verified_score가 있는 row: 0
현재 full_thesis_stage: 전부 FULL_THESIS_NOT_RUN
```

이벤트 분리 기준:

```
ASSESSMENT_ONLY:           3306
CANDIDATE_EVENTS_PRESENT:   85

candidate_event_count: 226
score_eligible_candidate_event_count: 92
sample_leaf_bundle_count: 67
```

해석:

```
모든 종목에는 CensusAssessmentEvent가 있다.
하지만 실제 후보 이벤트가 있는 종목은 85개뿐이다.
3306개는 평가 대상에 올렸지만 현재 catalyst가 없으므로 Stage0이다.
```

따라서 지금 `Stage2-Watch   30개`는 다음처럼 읽어야 한다.

```
맞는 해석:
공식 이벤트 또는 일부 claim이 있어서 watch 상태로 올랐고,
material gap이 남아 있다.

틀린 해석:
full thesis 평가가 끝났고 100점 만점 운영 점수로 Stage2가 확정됐다.
```

## v3에서 잘못됐던 핵심

v3의 문제는 단순히 점수가 낮거나 높았던 것이 아니다. **서로 다른 의미의 결과를 같은 필드에 담은 것**이 가장 컸다.

### 1. trace와 최종 row가 원자적으로 묶이지 않았다

예: 삼부토건 `001470`

```
최종 row:
Stage2-Watch / 4.4

연결된 stagecourt_trace:
Stage1 / 4.0
```

쉬운 예:

```
성적표에는 "수학 2등급 4.4점"이라고 적혀 있는데,
첨부된 채점지는 "영어 1등급 4.0점"인 상태다.
```

v4 패치:

```
AtomicStageDecision을 만들고,
최종 row의 stage/score/status/claim_ids/contribution_ids/trace_id가
같은 원자적 결정에서 왔는지 auditor가 강제한다.
```

v4 audit 결과:

```
stage_trace_stage_mismatch_count: 0
stage_trace_score_interval_mismatch_count: 0
stage_trace_score_status_mismatch_count: 0
stage_trace_claim_set_mismatch_count: 0
stage_trace_contribution_set_mismatch_count: 0
```

### 2. `verified_score`가 full E2R 점수처럼 보였다

v3에서는 `verified_score=4.0` 같은 값이 full E2R 점수처럼 보일 수 있었다.

하지만 실제로는 단일 DART 이벤트나 제한된 source task 점수였다.

v4 패치:

```
verified_score: null
event_evidence_score: 4.0 같은 부분 이벤트 점수
full_e2r_verified_score: null
score_scale: EVENT_WEIGHTED_PARTIAL 또는 NO_SCORE
```

이렇게 분리했다.

쉬운 예:

```
event_evidence_score = 쪽지시험 점수
full_e2r_verified_score = 기말고사 종합 점수

쪽지시험 점수를 기말고사 점수 칸에 넣지 않게 막은 것이다.
```

v4 audit 결과:

```
event_evidence_score_present_count: 67
full_e2r_verified_score_present_count: 0
verified_score_not_full_e2r_count: 0
```

### 3. Stage2-Watch 의미가 섞였다

v3의 Stage2-Watch는 다음 둘이 섞여 보였다.

```
1. 진짜 점수 threshold를 넘은 운영 Stage2
2. 공식 이벤트가 있어서 watch로 올린 상태
```

v4 패치:

```
base_stage
stage_signal
stage_decision_status
investigation_status
risk_stage_signal
transition_overlay
```

를 분리했다.

예:

```
Stage2-Watch + MATERIAL_CLAIM_WATCH + PENDING_MATERIAL_GAPS
= 의미 있는 claim은 있으나 full thesis 검증은 아직 부족하다.

Stage1 + OFFICIAL_EVENT_WATCH + FINAL
= 단일 공식 이벤트는 확인됐지만 full thesis는 아니다.

Stage0 + NO_CURRENT_CATALYST
= Census 평가는 했지만 현재 점수 재료 claim은 없다.
```

### 4. DART의 모든 "계약"이 계약 품질 점수처럼 들어갈 위험이 있었다

문제 예:

```
자사주 신탁계약
담보/질권 계약
증권신고서/유상증자
풍문 해명 공시
```

이런 것은 매출 계약이나 고객 수주가 아니다.

v4 패치:

```
semantic primitive guard를 추가했다.
contract_quality / earnings_visibility에 점수를 넣으려면
commercial_supply_contract로 분류되어야 한다.
```

차단 예:

```
노머스 473980:
share_buyback_trust_contract
-> score_scale NO_SCORE
-> Stage1 / EVIDENCE_INSUFFICIENT

성호전자 043260:
pledge_or_collateral_contract
-> score_scale NO_SCORE
-> Stage1 / EVIDENCE_INSUFFICIENT
```

주의:

```
이 guard는 완전한 LLM Evidence OS가 아니다.
현재는 DART 이벤트 오분류를 막는 보수적 방화벽이다.
최종 구조에서는 LLM claim extraction + entity/temporal adjudication + primitive mapping으로 대체/확장되어야 한다.
```

### 5. 삼성전자/하이닉스 daily event와 full thesis가 섞였다

v3에서 사용자가 가장 크게 혼란스러웠던 부분이다.

v4 기준 삼성전자 `005930`:

```
base_stage: Stage1
stage_signal: OFFICIAL_EVENT_WATCH
event_evidence_score: 4.0
verified_score: null
full_e2r_verified_score: null
full_thesis_stage: FULL_THESIS_NOT_RUN
```

v4 기준 SK하이닉스 `000660`:

```
base_stage: Stage1
stage_signal: OFFICIAL_EVENT_WATCH
event_evidence_score: 4.0
verified_score: null
full_e2r_verified_score: null
full_thesis_stage: FULL_THESIS_NOT_RUN
```

정확한 해석:

```
삼성전자/하이닉스 전체 HBM thesis 점수가 4점이라는 뜻이 아니다.
2026-07-01 기준 Census daily event board에서
최근 공식 이벤트 한두 개가 잡혔다는 뜻이다.
```

쉬운 예:

```
삼성전자 HBM 논문 전체를 채점한 것이 아니라,
"오늘 학교 게시판에 삼성전자 관련 공지 한 장이 붙었다"는 것을 기록한 상태다.
```

따라서 이 산출물로는 다음 질문에 답하면 안 된다.

```
삼성전자 지금 Green인가?
하이닉스 HBM thesis 점수는 몇 점인가?
```

현재 답은:

```
full thesis refresh task를 아직 안 돌렸으므로 미평가다.
```

### 6. CensusAssessmentEvent와 CandidateEvent를 분리했다

사용자가 말한 핵심 요구는 이것이었다.

```
전 종목에 "평가를 여는 행정 이벤트"는 있어도,
전 종목에 "사업/투자 trigger"가 있는 것은 아니다.
```

v4 row에는 이제 두 축이 따로 들어간다.

```
census_assessment_event_id
= 모든 eligible 종목에 하나씩 붙는 평가 개시 이벤트
= 점수 재료가 아님

candidate_event_ids
= 실제 공시/claim/report/market anomaly/research memory hint 같은 조사 후보 이벤트
= 이 중 source-backed accepted claim만 점수 후보가 됨
```

감사 결과:

```
missing_census_assessment_event_id_count: 0
assessment_event_score_evidence_allowed_count: 0
candidate_event_ids_contain_assessment_event_count: 0
assessment_only_nonzero_score_count: 0
no_current_catalyst_with_candidate_event_count: 0
score_eligible_candidate_without_accepted_claim_count: 0
```

쉬운 예:

```
000020:
  CensusAssessmentEvent 있음
  candidate_event_ids 없음
  -> Stage0 / NO_CURRENT_CATALYST / NO_SCORE

삼성전자:
  CensusAssessmentEvent 있음
  DART 해명 공시, ExistingClaimEvent, report snapshot, memory hint 있음
  -> Stage1 / OFFICIAL_EVENT_WATCH / event_evidence_score 4.0
  -> full thesis는 여전히 FULL_THESIS_NOT_RUN
```

## v4에서 실제로 통과한 것

### 실행 verdict

```
verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
anti_fake_blockers: []
remaining_operational_gaps:
  - full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt path not run
  - Brain/Web/LLM acquisition artifacts are not produced in this disabled ledger-refresh run
  - source-backed replay parity across all archetypes is not proven
meaningful_operational_stage_pass: False
brain_web_evidence_pass: False
```

readiness labels:

```
IMPLEMENTATION_MERGED
V3_FORENSIC_REVIEW_COMPLETE
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
ATOMIC_STAGE_DECISION_PASS
SCORE_SCALE_PASS
STAGE_SEMANTICS_PASS
SEMANTIC_PRIMITIVE_GUARD_PASS
DAILY_EVENT_FULL_THESIS_SEPARATION_PASS
CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS
FULL_THESIS_SMOKE_PENDING
OFFICIAL_BASELINE_OR_LEDGER_REFRESH_ONLY
```

의도적으로 없는 label:

```
FULL_UNIVERSE_STAGE_MAP_PASS
MEANINGFUL_OPERATIONAL_STAGE_PASS
BRAIN_WEB_EVIDENCE_PASS
FULL_THESIS_SMOKE_PASS
```

### leaf artifact audit

핵심 critical count는 모두 0이다.

```
critical_count: 0
missing_symbol_count: 0
duplicate_symbol_count: 0
stage_status_count_mismatch: 0
scored_row_missing_claim_ids: 0
scored_row_missing_score_contribution_ids: 0
scored_row_missing_stagecourt_trace: 0
provider_failed_final_score_count: 0
pending_material_marked_complete_count: 0
verified_score_not_full_e2r_count: 0
semantic_guard_blocked_score_count: 0
source_proxy_to_score_count: 0
news_snippet_to_score_count: 0
price_path_only_to_score_count: 0
web_claimed_but_zero_search_count: 0
llm_claimed_but_zero_calls_count: 0
atomic_candidate_event_is_assessment_count: 0
atomic_candidate_event_not_in_symbol_candidate_events_count: 0
canonical_stage_invalid_count: 0
canonical_stage_display_label_count: 0
stage_trace_canonical_stage_mismatch_count: 0
legacy_runner_production_reachable_count: 0
legacy_v3_runner_production_reachable_count: 0
empty_claims_stage_builder_production_count: 0
old_cli_can_claim_pass_count: 0
official_cli_not_v4_runner_count: 0
sample_bundle_missing_scored_row_count: 0
```

이 `critical_count: 0`의 범위도 anti-fake leaf artifact audit에 한정된다.

```
맞는 해석:
현재 disabled ledger refresh 산출물에서 row/trace/claim/score/event 분리 불변식이 깨지지 않았다.
부분 이벤트 점수가 붙은 67개 row는 sample_leaf_bundle에서 빠지지 않는다.
예전 v1/빈 claim/old CLI 경로가 production pass를 주장하지 못한다.

틀린 해석:
Brain/Web까지 실제로 돌았고 full thesis 운영 Stage가 준비됐다.
```

### 전체 테스트

실행 명령:

```
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```
Ran 4942 tests in 170.248s
OK
```

중요한 신규/관련 테스트 축:

```
AtomicStageDecision trace consistency
legacy v1 runner lockout
run mode honesty
score field split
Samsung/Hynix daily event vs full thesis split
semantic guard for share buyback/pledge contracts
canonical stage vs display label split
stage signal split
Worldex audit opinion does not create Samsung 4C
atomic candidate_event_id does not point to CensusAssessmentEvent
artifact manifest row_count/sha256 parity
sample_leaf_bundle contains every scored or claim-backed row
legacy/static empty-claim production path lockout
official v4 CLI uses v4 runner
```

### docs/operational 오염 방지

한 번 문제가 있었다.

```
Brain/Web enabled 실패 스모크를 /tmp output으로 돌렸는데,
docs/operational/census_mode_v4_* 공용 문서까지 FAIL 산출물로 덮였다.
```

이제 CLI 기본값은 다음이다.

```
--write-operational-docs auto

canonical output:
  output/census_v4/<as_of_date>
  -> docs/operational 갱신

temporary smoke output:
  /tmp/.../out
  -> docs/operational 갱신 금지
```

따라서 다음 에이전트가 `docs/operational`에서 `run_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED`와 `output_root=/tmp/...`를 보면, 그것은 오래된 오염이거나 `--write-operational-docs true`로 강제 실행한 것이다. canonical run을 다시 생성해서 문서 장부를 맞춰야 한다.

## 아직 절대 완료가 아닌 것

다음은 아직 안 됐다. 다음 에이전트는 이 부분을 강하게 공격해야 한다.

### 1. full thesis scoring은 아직 안 됐다

현재 모든 row:

```
full_thesis_stage: FULL_THESIS_NOT_RUN
full_e2r_verified_score: null
```

따라서 현재 v4는 다음을 주장하면 안 된다.

```
전 종목 full E2R 점수 산출 완료
삼성전자/하이닉스 HBM thesis 점수 산출 완료
Green/Yellow 최종 판정 완료
과거 연구자료 parity 달성
```

### 2. Brain/Web/LLM acquisition은 아직 실행되지 않았다

v4 audit:

```
planner_run_count: 0
web_search_task_count: 0
web_search_result_count: 0
claim_extractor_run_count: 0
```

이건 실패가 아니라, 현재 run mode가 `LEDGER_REFRESH_CENSUS`라서 정직하게 꺼 둔 것이다.

중요한 점:

```
0 calls인데 Brain/Web pass라고 주장하지 않도록 막은 것이 v4의 성과다.
하지만 실제 운영 Brain/Web 파이프라인을 통과한 것은 아니다.
```

쉬운 예:

```
인터넷 검색을 안 했는데 "검색 성공"이라고 말하지 않게 만든 것.
아직 검색 엔진을 제대로 돌려서 점수까지 넣은 것은 아니다.
```

### 3. C01~C36 모든 아키타입 Evidence Contract v2는 아직 완성되지 않았다

현재 semantic guard는 좁은 방어막이다.

최종 목표는 다음이어야 한다.

```
문서
-> raw assertion extraction
-> target/entity adjudication
-> temporal/lifecycle adjudication
-> primitive mapping
-> score contribution ledger
-> deterministic score/stage
```

즉 단순 키워드 guard가 아니라, 전 아키타입에 대해 다음을 가져야 한다.

```
required / alternative primitives
source quorum
freshness / expiry / supersession rule
guard mode
hard-break rule
score cap
unknown/material gap policy
```

### 4. source task satisfaction은 아직 운영 완료가 아니다

현재는 공식 ledger refresh 결과를 정직하게 상태판으로 만들었다.

하지만 production daily mode라면 각 material gap에 대해 다음이 필요하다.

```
SourceTask 생성
official-first provider 실행
budget / stop condition 기록
provider failure면 pending
claim 확인 시 stop-on-resolution
```

예:

```
FCF gap이면 뉴스 1000개가 아니라 DART/IR/CompanyGuide task부터 실행해야 한다.
provider가 막히면 0점 확정이 아니라 ProviderPending이어야 한다.
```

### 5. 과거 연구자료 parity는 아직 증명되지 않았다

과거 연구자료는 두 종류로 나눠야 한다.

```
실제 URL/원문 snapshot이 있는 자료:
golden replay fixture로 사용 가능

source_proxy_only / evidence_url_pending 자료:
ontology와 Evidence Contract 설계 참고만 가능
운영 점수 정답으로 사용 금지
```

현재 v4는 과거 연구자료 전체 parity를 입증하지 않았다.

## 다음 패치 방향

아래 순서가 안전하다. 한 번에 "전부 Green"을 만들려고 하면 또 점수가 흔들린다.

### P0. 현재 v4 상태를 더 엄격히 고정

목표:

```
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS는 유지하되,
그 의미를 절대 운영 점수 pass로 오해하지 못하게 한다.
```

해야 할 일:

```
1. v4 README/0701 문서와 operational verdict의 용어를 동기화한다.
2. FULL_THESIS_NOT_RUN row에서 verified_score가 생기면 audit fail.
3. Brain/Web artifacts가 0인데 pass label이 있으면 audit fail.
4. 모든 Stage2-Watch는 stage_signal과 stage_decision_status를 필수로 가진다.
```

### P1. CensusAssessmentEvent와 CandidateEvent 분리 유지

원칙:

```
CensusAssessmentEvent
= 모든 종목을 평가 대상으로 올리는 행정 이벤트

CandidateEvent
= 실제 공시/실적/리포트/가격이상/리스크 사건
```

예:

```
아무 새 공시 없는 종목:
CensusAssessmentEvent 있음
CandidateEvent 없음
accepted claim 없음
-> Stage0 / NO_CURRENT_CATALYST

공급계약 공시 있는 종목:
CensusAssessmentEvent 있음
CandidateEvent supply_contract 있음
accepted claim 있음
-> Stage1~Stage2-Watch 가능
```

절대 금지:

```
전 종목에 CensusAssessmentEvent가 있으니 전 종목이 trigger 있음
-> 억지 점수 산출
-> 낮으면 Red
```

현재 v4 반영 상태:

```
구현됨:
- census_assessment_event_id와 candidate_event_ids 분리
- CAE는 score_evidence_allowed=false로 고정
- CAE가 candidate_event_ids에 섞이면 audit fail
- candidate가 없는 ASSESSMENT_ONLY row에서 점수가 생기면 audit fail

아직 남음:
- CandidateEvent를 full Evidence OS SourceTask로 실제 실행하는 Brain/Web/IR/Report 경로
- source task 결과가 primitive/score contribution으로 닫히는 운영 루프
```

### P2. Production SourceTask -> EvidenceClaim Acquisition Gate 구현

목표:

```
SourceTask를 실행했다고 말하려면 실제 official-first provider/search/fetch/extractor artifact가 있어야 한다.
Brain/Web은 이 중 general web fallback에 가까우며, DART/KIND/KRX/IR/CompanyGuide가 먼저다.
```

필수 산출물:

```
planner_runs.jsonl
llm_prompts.jsonl
llm_responses.jsonl
web_search_tasks.jsonl
web_search_results.jsonl
web_fetched_documents.jsonl
web_rejected_documents.jsonl
claim_extractor_runs.jsonl
brain_to_claim_trace.jsonl
evidence_claims.jsonl
```

정책:

```
zero artifact -> Brain/Web pass 금지
provider_error -> 낮은 점수 확정 금지, pending
official source로 풀 수 있는 gap -> general web fallback 금지
production daily mode -> unbounded fetch 금지
Pending이면 full_e2r_verified_score=null
Pending이면 score_valid=false
Pending이면 낮은 Red/Reject로 확정 금지
```

### P3. EvidenceClaim 독립 장부와 score delta audit 먼저 닫기

LLM은 점수나 Stage를 부르지 않는다.
LLM은 원문에서 claim 후보를 만들고, deterministic 코드가 source anchor, entity, 날짜, 현재성, source quorum을 검증한다.

필수 장부:

```
EvidenceClaim
PrimitiveState
ScoreContribution
ScoreDelta
```

ScoreDelta는 SourceTask 점수가 들어가는 첫 순간부터 필요하다.
P5로 미루면 다시 92점 -> 63점 같은 변화가 설명 없이 쌓일 수 있다.

필수:

```
before_score
after_score
delta
added_claim_ids
removed_claim_ids
superseded_claim_ids
contradicted_claim_ids
reason
```

### P4. 삼성전자/하이닉스 full thesis smoke를 진짜로 실행

현재 상태:

```
FULL_THESIS_SMOKE_PENDING
```

목표:

```
삼성전자/하이닉스에 대해 C06/HBM full thesis refresh task를 별도로 실행한다.
```

필수 조건:

```
1. daily DART event score와 full thesis score는 별도 field.
2. HBM customer allocation, capacity, revenue mix, cash/revision bridge를 claim으로 확인.
3. 오래된 qualification delay는 current/open/superseded 여부를 판정.
4. hard break는 direct target + current OPEN + source quorum 없으면 금지.
5. 결과가 pending이면 pending이라고 표시.
6. 삼성/하이닉스 전용 하드코딩이 아니라 generic Evidence Contract와 SourceTask로만 실행.
```

쉬운 예:

```
2024년 HBM qualification delay 기사
-> 2026년 현재도 미해결인지 후속 자료 확인
-> 후속 공급/qualification 자료가 있으면 superseded
-> 확인 못 하면 현재 risk 점수 0, follow-up gap
```

### P5. Evidence OS를 전 아키타입으로 확장

최종 구조:

```
EvidenceDocument
-> EvidenceAnchor
-> RawAssertion
-> EvidenceClaim
-> Target/Temporal Adjudication
-> PrimitiveMappingProposal
-> AcceptedPrimitiveState
-> ScoreContributionLedger
-> StageCourt
```

LLM 역할:

```
문서에서 사실 claim을 뽑고,
누가/언제/무엇을 말했는지 구조화한다.
```

코드 역할:

```
anchor 검증
entity directness
as_of_date/future leakage
lifecycle/supersession
source quorum
score 합산
Stage gate
```

금지:

```
LLM이 "이 종목 92점"이라고 직접 결정
키워드 하나로 accounting risk true
종목명 예외 하드코딩
old unresolved event를 current risk로 자동 감점
```

### P6. Append-only ledger와 replay parity

앞으로 점수가 변하면 반드시 설명되어야 한다.

필수:

```
before_score
after_score
delta
added_claim_ids
removed_claim_ids
superseded_claim_ids
contradicted_claim_ids
reason
```

원칙:

```
0보다 큰 모든 점수 변화는 claim delta로 설명한다.
5점 이상 변화는 critical audit event다.
```

쉬운 예:

```
삼성전자 92 -> 63
```

이런 변화가 다시 나오면 다음 없이는 실패해야 한다.

```
어떤 claim이 빠졌는지
어떤 claim이 새로 들어왔는지
어떤 risk claim이 current OPEN으로 인정됐는지
왜 source quorum을 만족하는지
```

## 다음 에이전트가 반드시 때려봐야 할 체크리스트

### A. run-mode honesty

확인:

```
Brain/Web artifact 0개인데 Brain/Web pass label이 있는가?
FULL_THESIS_NOT_RUN인데 verified_score가 들어갔는가?
event_evidence_score를 full_e2r_verified_score처럼 쓰는가?
```

### B. Stage 의미

확인:

```
Stage2-Watch가 MATERIAL_CLAIM_WATCH/PENDING_MATERIAL_GAPS 없이 나오는가?
Red가 current direct risk trace 없이 나오는가?
SourcePending이 final reject/red로 바뀌는가?
```

### C. claim/trace atomicity

확인:

```
최종 row의 stagecourt_trace_id가 같은 score/status/claims/contributions를 가리키는가?
동일 종목 여러 trace 중 다른 trace의 score를 섞지 않는가?
atomic_stage_decision_id가 없는 scored row가 있는가?
```

### D. semantic guard

확인:

```
자사주 신탁계약이 contract_quality로 점수화되는가?
담보/질권 계약이 고객 계약으로 들어가는가?
증권신고서/유상증자가 earnings_visibility가 되는가?
풍문 해명이 HBM thesis bridge가 되는가?
```

### E. current risk lifecycle

확인:

```
타사 감사의견을 target accounting risk로 붙이는가?
과거 risk를 current OPEN 확인 없이 hard break로 쓰는가?
"적정" 감사의견을 부정 risk로 읽는가?
후속 해소/정정/대체 공시를 supersession 처리하는가?
```

### F. Samsung/Hynix full thesis

확인:

```
삼성전자/하이닉스 daily event score를 HBM full thesis score로 부르는가?
C06/HBM primitive coverage 없이 Green/Yellow를 말하는가?
old qualification delay와 current capacity/revenue evidence를 lifecycle로 대조하는가?
```

### G. source task realness

확인:

```
SourceTask가 실제 provider request와 연결됐는가?
official-first가 지켜졌는가?
provider failure가 low score final로 바뀌지 않는가?
production daily mode에서 unbounded fetch가 가능한가?
```

## 재현 명령

v4 실행:

```
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --fail-on-critical-audit true \
  --write-operational-docs auto \
  --test-result-summary 'PYTHONPATH=src python -m unittest discover -s tests; Ran 4942 tests in 170.248s; OK' \
  --test-result-artifact output/census_v4/2026-07-01/test_result_artifact.json
```

전체 테스트:

```
PYTHONPATH=src python -m unittest discover -s tests -v
```

현재 확인된 결과:

```
v4 verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
full operational pass: false
brain/web pass: false
tests: 4942 OK
```

## 관련 파일

핵심 코드:

```
src/e2r/census/atomic_stage_decision.py
src/e2r/census/census_v4_auditor.py
src/e2r/census/census_runner_v4.py
src/e2r/cli/run_e2r_census_v4_until_pass.py
src/e2r/cli/run_e2r_census_mode.py
src/e2r/evidence/contract_semantic_classifier.py
src/e2r/evidence/primitive_semantic_guard.py
configs/e2r_contract_semantic_guard_v1.json
```

핵심 문서:

```
docs/operational/census_mode_v3_forensic_review.md
docs/operational/census_mode_v4_internal_patch_plan.md
docs/operational/census_mode_v4_acceptance_report.md
docs/operational/census_mode_v4_readiness_verdict.md
docs/operational/census_mode_v4_leaf_artifact_audit.json
docs/operational/census_mode_v4_research_brain_bridge_audit.json
docs/operational/census_mode_v4_samsung_hynix_full_thesis_smoke.json
docs/0701/census_v4_brain_web_claim_bridge_audit_2026-07-01.md
```

핵심 테스트:

```
tests/test_census_v4_atomic_stage_decision.py
tests/test_census_v4_legacy_runner_lockout.py
tests/test_census_v4_run_mode_honesty.py
tests/test_census_v4_evidence_claim_payload_view.py
tests/test_census_v4_research_brain_bridge_honesty.py
tests/test_census_v4_brain_web_readiness_gate.py
tests/test_census_v4_sambo_trace_mismatch_fails.py
tests/test_census_v4_score_field_split.py
tests/test_census_v4_semantic_guard.py
tests/test_census_v4_stage_signal_split.py
tests/test_contract_semantic_classifier.py
```

## 추가 감사: Claim Payload / Research Brain Bridge / Brain Score Trace Export / Promotion Gate

이번 추가 패치로 `accepted_claims.jsonl`을 감사 가능한 `evidence_claims.jsonl` view로 명시했다.

현재 값:

```
accepted_claims.jsonl: 92
evidence_claims.jsonl: 92
event_evidence_score_present_count: 67
planner_run_count: 0
web_search_task_count: 0
claim_extractor_run_count: 0
research_brain_bridge_verdict: SHADOW_OR_IMPORT_ONLY
research_brain_bridge_snapshot_url_count: 255
research_brain_bridge_usable_for_census_cutover: false
brain_stage_promotion_verdict: NOT_REQUESTED
brain_web_readiness_gate_verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
brain_trace_missing_accepted_claim_count: 0
brain_trace_missing_score_contribution_ref_count: 0
brain_trace_missing_stagecourt_ref_count: 0
brain_contribution_without_accepted_support_count: 0
brain_stage_trace_without_accepted_claim_count: 0
promoted_stage_without_brain_trace_count: 0
brain_stage_trace_count: 0
brain_stage_promoted_row_count: 0
brain_stage_promotion_unsafe_promoted_count: 0
claim_to_stage_forensic_audit: PASS
source_task_realness_audit: PASS_LEDGER_REFRESH_REALNESS
source_task_realness_scope: LEDGER_REFRESH_REALNESS_PASS
source_task_realness_audit.live_source_pass_allowed: false
existing_ledger_reuse_audit: PASS
last_effective_thesis_audit: PASS
source_coverage_audit: PASS_LEDGER_REFRESH_COVERAGE
runtime_plausibility_audit: PASS_LEDGER_REFRESH_RUNTIME_HONESTY
brain_web_readiness_gate_audit: NOT_REQUESTED
source_task_claim_producing_count: 60
source_task_real_fetch_count: 0
source_task_fresh_provider_cache_count: 60
source_task_lifecycle_refresh_count: 32
operational_live_source_coverage_pass: false
```

해석:

```
92개 claim payload는 있다.
하지만 이는 Brain/Web live claim이나 full thesis claim이 아니라
공식 baseline/source-backed accepted claim을 감사 가능하게 펼친 view다.
```

쉬운 예:

```
DART 공시에서 계약 claim을 뽑았다는 서류는 있다.
그러나 그 서류 하나를 "LLM이 웹까지 돌려 전체 thesis를 채점했다"로 바꾸면 안 된다.
```

추가 구현:

```
brain_web_mode=enabled 경로는 별도 smoke에서 Research Brain v4 bundle을 Census leaf로 export하는지 검증해야 한다.
현재 canonical run은 disabled라서 아래 leaf들은 실행 증거가 아니라 검증 대상 목록이다.

export 대상:
  planner_runs.jsonl
  research_brain_plans.jsonl
  source_tasks.jsonl
  source_task_executions.jsonl
  evidence_documents.jsonl
  evidence_anchors.jsonl
  raw_assertions.jsonl
  adjudicated_claims.jsonl
  accepted_claims.jsonl
  primitive_states.jsonl
  score_contributions.jsonl
  stagecourt_traces.jsonl
  brain_to_claim_trace.jsonl
  brain_stage_promotion_audit.json
```

하지만 아직 남은 제한:

```
export된 Brain StageCourt trace는 census_stage_status.jsonl 대표 Stage row로 승격하지 않는다.
따라서 canonical output은 여전히 Brain/Web disabled이고,
Brain/Web evidence pass나 meaningful operational Stage pass를 주장하지 않는다.
```

이를 기계적으로 막는 새 감사 파일:

```
output/census_v4/2026-07-01/brain_stage_promotion_audit.json
docs/operational/census_mode_v4_brain_stage_promotion_audit.json
```

현재 canonical 값:

```
verdict: NOT_REQUESTED
blockers: []
brain_stage_trace_count: 0
brain_promoted_stage_row_count: 0
unsafe_promoted_stage_row_count: 0
```

다음 조건 없이는 Brain StageCourt trace를 대표 row로 승격하면 안 된다.

```
brain_web_mode=enabled
brain_stage_promotion_mode=strict
real planner/provider success > 0
source task executions > 0
accepted brain claims > 0
claim-backed score contributions > 0
brain StageCourt traces > 0
zero snapshot:// promoted evidence documents
zero fake provider rows
zero unsafe promoted representative rows
```

## 추가 감사: Goal-required runtime proof files

Goal 문서가 요구한 전용 감사 파일도 추가했다.

```
output/census_v4/2026-07-01/claim_to_stage_forensic_audit.json
output/census_v4/2026-07-01/source_task_realness_audit.json
output/census_v4/2026-07-01/existing_ledger_reuse_audit.json
output/census_v4/2026-07-01/last_effective_thesis_audit.json
output/census_v4/2026-07-01/source_coverage_audit.json
output/census_v4/2026-07-01/runtime_plausibility_audit.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
```

같은 내용은 `docs/operational/census_mode_v4_*` 파일로도 복사된다.

현재 canonical 값:

```
claim_to_stage_forensic_audit:
  verdict: PASS
  critical_count: 0
  scored_row_count: 67

source_task_realness_audit:
  verdict: PASS_LEDGER_REFRESH_REALNESS
  verdict_scope: LEDGER_REFRESH_REALNESS_PASS
  live_source_pass_allowed: false
  source_task_claim_producing_count: 60
  source_task_real_fetch_count: 0
  source_task_fresh_provider_cache_count: 60
  source_task_lifecycle_refresh_count: 32

source_task_satisfaction_audit:
  verdict: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
  verdict_scope: LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS
  live_source_task_satisfaction_pass_allowed: false
  baseline_only_score_claim_count: 32

existing_ledger_reuse_audit:
  verdict: PASS
  reused_claim_count: 92
  lifecycle_refreshed_reused_claim_count: 92

last_effective_thesis_audit:
  verdict: PASS
  last_effective_thesis_count: 3391
  source_timeline_count: 3391

source_coverage_audit:
  verdict: PASS_LEDGER_REFRESH_COVERAGE
  cutover_replay_only_symbol_count: 67
  operational_live_source_coverage_pass: false

runtime_plausibility_audit:
  verdict: PASS_LEDGER_REFRESH_RUNTIME_HONESTY
  runtime_mode: LEDGER_REFRESH
  provider_call_count: 0
  llm_call_count: 0

brain_web_readiness_gate_audit:
  verdict: NOT_REQUESTED
  minimum_gate_applies: false
  brain_web_evidence_pass_allowed: false
  llm_planner_call_count: 0
  source_task_execution_count: 0
  web_or_llm_accepted_claim_count: 0
  brain_trace_missing_accepted_claim_count: 0
  brain_trace_missing_score_contribution_ref_count: 0
  brain_trace_missing_stagecourt_ref_count: 0
  brain_contribution_without_accepted_support_count: 0
  brain_stage_trace_without_accepted_claim_count: 0
  promoted_stage_without_brain_trace_count: 0
```

쉬운 예:

```
채점지 67장은 claim/trace까지 모두 맞아 떨어진다.
하지만 이 채점지는 새로 시험을 본 결과가 아니라, 기존 source-backed 장부를 다시 펼쳐 검산한 것이다.

그래서 source realness는 PASS지만,
live source coverage는 아직 false다.
```

즉 현재 상태는:

```
가짜 점수/trace 혼합 방지: 통과
기존 source-backed ledger 재검산: 통과
새 live Brain/Web/IR/Report 운영 채점: 아직 아님
```

쉬운 예:

```
서류철과 채점 메모를 보관함에 넣는 길은 생겼다.
아직 그 채점 메모를 공식 성적표에 반영하는 결재 단계는 남아 있다.
```

Research Brain v4 기존 보고서는 import 검토만 했다.

```
accepted_claim_count: 56
real_document_fetched_count: 255
snapshot_url_count: 255
production_cutover_ready: false
```

주의:

```
real_document_fetched_count=255는 imported Research Brain report 내부 값이다.
snapshot_url_count=255와 함께 있으므로 live provider fetch pass가 아니다.
usable_for_census_cutover=false인 상태에서 production evidence로 승격하면 안 된다.
```

따라서 기존 Research Brain v4 보고서를 Census v4 production evidence로 승격하면 안 된다.

쉬운 예:

```
예전 모의시험 답안지는 절차가 맞는지 참고할 수 있다.
하지만 snapshot/fixture blocker가 남아 있으면 실제 시험 합격증으로 제출하면 안 된다.
```

## Not Yet Covered Hard Gates

현재 7개 핵심 감사가 통과했다고 해서 goal2/goal3가 닫힌 것은 아니다.
아래 항목은 아직 hard gate로 남아 있다.

| Hard gate | 현재 상태 | 왜 아직 완료가 아닌가 |
| --- | --- | --- |
| Real Brain planner minimum | `llm_call_count=0`, Brain/Web `NOT_REQUESTED` | goal2의 `llm_planner_call_count >= 30` 또는 external blocker 조건을 충족하지 않았다 |
| Web/Naver/News acquisition | `web_search_task_count=0`, `web_fetched_document_count=0` | 웹/뉴스/네이버 원문 fetch가 없으므로 `BRAIN_WEB_EVIDENCE_PASS`가 아니다 |
| LLM claim extractor | `llm_claim_extractor_attempt_count=0` | unstructured 문서에서 claim을 뽑은 실행이 없다 |
| Brain/Web promoted Stage | `brain_stage_trace_count=0`, promoted row 0 | accepted Brain/Web claim이 대표 `census_stage_status` row로 strict promotion된 적이 없다 |
| Samsung/Hynix full thesis | `FULL_THESIS_NOT_RUN`, smoke `PENDING_FULL_THESIS_REFRESH`, task 14개 planning-only | C06/HBM full thesis와 daily DART event score를 분리했고 다음 조사 task는 만들었지만 full thesis 채점은 안 했다 |
| Known-bad regression | `PASS`, `case_count=10`, `failed_case_count=0` | 이 blocker는 닫혔다. 다만 새 회귀가 생기면 suite에 추가해야 한다 |
| Self-repair loop | `RUN_COMPLETE`, `unresolved_failures=[]` | 이 blocker는 닫혔다. 단 Brain/Web/full-thesis deferred blocker를 대신 닫은 것은 아니다 |
| Source task satisfaction | `PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION`, schema v2, representative score claim 67개 chain closed, `critical_count=0`, `warning_count=25` | live source pass는 아니며 대표 row 밖 SourceTask claim 25개 warning이 다음 refinement다 |
| Primitive state chain | `primitive_state_chain_audit: PASS`, `critical_count=0`, representative score claim 67개가 primitive/mapping leaf까지 closed, `primitive_mapping_count=92` | live/Brain/Web/full thesis claim은 아직 이 chain을 통과하지 않았다 |
| CLI completion target | `--target-gate anti_fake|meaningful|brain_web|full_thesis` 구현됨 | exit 0은 target gate와 함께 해석해야 하며, meaningful/brain_web/full_thesis는 아직 `NOT_READY`가 정상 |
| Test result evidence | `MACHINE_READABLE_TEST_ARTIFACT_PASS`, `artifact_test_count=4942` | 문자열 주입 blocker는 닫혔지만, 이것만으로 goal completion은 아님 |

쉬운 예:

```
현재 통과한 7개 감사는 "서류철 번호가 맞는지"를 본 것이다.
known-bad 오답 검사는 이제 통과했다.
아직 "새 시험을 보고, 재시험 로그까지 남겼고, full thesis와 Brain/Web 증거까지 연결했는지"는 보지 않았다.
```

따라서 다음 문구는 금지된다.

```
Real Brain/Web operational pass
FULL_THESIS_SMOKE_PASS
MEANINGFUL_OPERATIONAL_STAGE_PASS
READY_FOR_OPERATIONAL_STAGE_USE
READY_FOR_FULL_THESIS_OPERATION
```

허용되는 현재 문구:

```
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
LEDGER_REFRESH_REALNESS_PASS
Brain/Web NOT_REQUESTED
FULL_THESIS_SMOKE_PENDING
meaningful_operational_stage_pass=false
full_thesis_smoke_task_count=14
full_thesis_smoke_task_score_allowed_before_execution=false
```

## 최종 판단

이번 v4 패치의 의미:

```
좋아진 것:
- 가짜 full stage pass를 덜 말하게 됐다.
- event score와 full verified score를 분리했다.
- trace/claim/score 혼합을 audit로 막았다.
- 자사주/담보/증권신고서 같은 DART 계약 노이즈를 보수적으로 차단했다.
- 삼성전자/하이닉스 daily event와 full HBM thesis를 분리했다.

아직 아닌 것:
- 실제 Brain/Web/LLM acquisition이 돈 것은 아니다.
- 전 아키타입 full Evidence OS가 완성된 것은 아니다.
- 삼성전자/하이닉스 full thesis 점수가 나온 것은 아니다.
- 과거 연구자료 parity가 증명된 것은 아니다.
- 운영 Stage3-Green/Yellow/Red/4B/4C 판정이 완성된 것은 아니다.
```

따라서 다음 에이전트가 이 문서를 본 뒤 내려야 할 출발점은 이것이다.

```
v4는 최종 운영 파이프라인이 아니라,
거짓 완료 선언을 막는 방어막과 다음 구현 방향을 고정한 중간 단계다.

다음 패치는
"점수 더 잘 나오게 만들기"가 아니라
"SourceTask -> EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt"
전체 경로를 실제 운영 데이터로 닫는 작업이어야 한다.
```
