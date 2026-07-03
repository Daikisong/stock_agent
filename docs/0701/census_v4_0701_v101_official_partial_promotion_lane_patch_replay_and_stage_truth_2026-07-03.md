# Census v4 0701 v101 Official Partial Promotion Lane Patch / Replay / Stage Truth

이 문서는 다음 에이전트가 빡세게 공격할 수 있게 만든 v101 감사 패킷이다.

핵심 질문:

```text
뭔가 잘못되고 있는가?
Stage가 있는 애들이 있긴 한가?
```

짧은 답:

```text
v100 실제 bounded ramp 산출물 기준:
  Stage row는 있지만 전부 CENSUS_EVENT_BOARD다.
  Brain StageCourt trace 21개는 최종 census_stage_status에 0개 승격됐다.
  FULL_THESIS 운영 Stage는 0개다.

v101 정책 replay 기준:
  Brain StageCourt trace 21개가 부분 Stage row로 승격된다.
  BRAIN_WEB_PARTIAL = 2개
  BRAIN_OFFICIAL_PARTIAL = 19개
  FULL_THESIS = 0개

따라서 "Stage가 하나도 없다"는 말은 틀렸다.
하지만 "운영자가 믿고 쓰는 Full Thesis Stage가 있다"도 틀렸다.
정확한 현재 상태는 "claim-backed partial Stage는 생겼지만, 전부 NOT_FULL_THESIS_STAGE"다.
```

쉬운 예:

```text
전교생 상태판에는 이름과 출석 상태가 있다.
몇 명은 답안지 일부도 채점됐다.
하지만 졸업 판정 성적표는 아직 0명이다.

CENSUS_EVENT_BOARD      = 출석/상태판
BRAIN_*_PARTIAL         = 일부 답안 채점
FULL_THESIS             = 졸업 판정 성적표
```

## 1. 기준 산출물

v100 실제 실행 산출물:

```text
output/census_v4/2026-07-01-v100-external-seed-real-extractor-bounded-ramp
```

v101 정책 replay 산출물:

```text
output/census_v4/2026-07-01-v101-promotion-policy-replay-from-v100
```

주의:

```text
v101은 v100 live run을 처음부터 다시 돈 것이 아니다.
v100 산출물을 복사한 뒤, v101 promotion policy와 full thesis attempt만 재적용한 replay다.
그러므로 v101은 "정책 패치가 v100 증거에 적용되면 어떻게 되는가"를 보는 검증이다.
```

중요한 혼선:

```text
v101 replay 폴더 안의 기본 brain_web_readiness_gate_audit.json은 v100에서 복사된 원본이다.
그래서 여전히 BLOCKED라고 적혀 있다.

v101 판단은 아래 파일들을 기준으로 봐야 한다.

brain_stage_promotion_audit_after_v101_policy_replay.json
brain_stage_promotion_export_after_v101_policy_replay.json
census_stage_status_after_v101_policy_replay.jsonl
census_stage_status_after_v101_policy_replay_and_full_thesis_attempt.jsonl
full_thesis_production_runner_audit_after_v101_policy_replay.json
full_thesis_production_audit_after_v101_policy_replay.json
```

## 2. v100에서 실제로 막힌 위치

v100은 real planner, bounded live acquisition, real LLM claim extractor를 켠 bounded ramp였다.

v100에서 이미 확인된 것:

```text
real_provider_success_count = 30
source_task_execution_count = 228
web_search_task_count = 37
web_search_call_count = 37
web_fetched_document_count = 31
llm_claim_extractor_attempt_count = 31
llm_claim_extractor_real_provider_count = 31
Brain accepted claims = 93
Brain score contributions = 53
Brain StageCourt traces = 21
```

하지만 최종 `census_stage_status.jsonl`은 이렇게 끝났다.

```text
rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391
  BRAIN_WEB_PARTIAL  = 0
  FULL_THESIS        = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3391
```

v100의 핵심 버그:

```text
Brain StageCourt trace 21개 중 19개가 OpenDART official-only였다.
기존 promotion audit은 official-only trace를 "web/LLM support 없음"으로 run-global blocker 처리했다.
그 결과 web/LLM claim이 있는 2개 trace까지 함께 최종 상태판에 승격되지 못했다.
```

쉬운 예:

```text
21명 중 19명이 공문서 답안지만 냈고, 2명은 웹/LLM 추출 답안지도 냈다.
기존 규칙은 "공문서 답안만 있는 학생이 있으니 전체 반 성적표 반영 금지"처럼 동작했다.
그래서 2명의 웹/LLM 답안까지 같이 묶여 0건 반영됐다.
```

## 3. v101 코드 패치 방향

v101 패치는 "official-only를 FULL_THESIS로 올리자"가 아니다.

패치의 정확한 의도:

```text
1. web/LLM claim-backed StageCourt trace는 BRAIN_WEB_PARTIAL로 부분 승격한다.
2. official claim-backed StageCourt trace는 BRAIN_OFFICIAL_PARTIAL로 부분 승격한다.
3. 두 lane 모두 operator_stage_use=NOT_FULL_THESIS_STAGE를 유지한다.
4. 두 lane 모두 operator_score_use=NOT_FULL_E2R_SCORE를 유지한다.
5. FULL_THESIS/Green은 절대 이 패치로 만들지 않는다.
6. claim support가 전혀 없는 trace만 promotion blocker로 남긴다.
```

패치된 코드 위치:

```text
src/e2r/census/census_runner_v4.py
  _promote_brain_stage_rows
    BRAIN_WEB_PARTIAL / BRAIN_OFFICIAL_PARTIAL lane 분리
    promoted_web_llm_stage_row_count 기록
    promoted_official_stage_row_count 기록
    skipped_unsupported_trace_count 기록

  _brain_stage_promotion_audit
    web/LLM claim count와 official claim count 분리
    without_web_or_llm은 정보값으로 유지
    without_supported_claim만 blocker 처리

  _with_operator_scope_aliases / _operator_scope_note
    BRAIN_OFFICIAL_PARTIAL 표시와 operator note 추가

  _primitive_state_chain_audit
    BRAIN_WEB_PARTIAL과 BRAIN_OFFICIAL_PARTIAL의 atom-less primitive chain 허용
```

테스트 위치:

```text
tests/test_census_v4_brain_stage_promotion_gate.py
  test_official_only_brain_claim_promotes_as_official_partial_not_brain_web
  test_mixed_web_and_official_brain_traces_promote_per_trace_without_global_blocker
```

## 4. v101 replay 결과

기준 파일:

```text
output/census_v4/2026-07-01-v101-promotion-policy-replay-from-v100/brain_stage_promotion_export_after_v101_policy_replay.json
output/census_v4/2026-07-01-v101-promotion-policy-replay-from-v100/brain_stage_promotion_audit_after_v101_policy_replay.json
output/census_v4/2026-07-01-v101-promotion-policy-replay-from-v100/census_stage_status_after_v101_policy_replay.jsonl
```

promotion export:

```text
promoted_stage_row_count = 21
promoted_web_llm_stage_row_count = 2
promoted_official_stage_row_count = 19
skipped_unsupported_trace_count = 0
```

promotion audit:

```text
verdict = PROMOTION_APPLIED
brain_stage_trace_count = 21
brain_promoted_stage_row_count = 21
brain_stage_trace_with_web_or_llm_claim_count = 2
brain_stage_trace_with_official_claim_count = 20
brain_stage_trace_without_web_or_llm_claim_count = 19
brain_stage_trace_without_supported_claim_count = 0
unsafe_promoted_stage_row_count = 0
blockers = []
```

`brain_stage_trace_with_official_claim_count = 20`인데 official promoted row가 19인 이유:

```text
두산에너빌리티 trace 하나가 web/LLM claim과 official claim을 같이 가진 mixed trace다.
promotion lane은 web/LLM 우선으로 BRAIN_WEB_PARTIAL에 들어간다.
그래서 official claim을 가진 trace 수는 20개지만, official lane row는 19개다.
```

v101 replay 후 `census_stage_status_after_v101_policy_replay.jsonl`:

```text
rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD      = 3370
  BRAIN_OFFICIAL_PARTIAL  = 19
  BRAIN_WEB_PARTIAL       = 2

score_scale:
  NO_SCORE               = 3320
  EVENT_WEIGHTED_PARTIAL = 71

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391
```

즉 v101은 "부분 Stage row가 상태판에 보이게 하는 패치"다.
운영 Stage나 Green을 만든 패치가 아니다.

## 5. v101에서 Stage가 있는 종목

v101 replay 기준 partial Stage row:

```text
000660 SK하이닉스      canonical_stage=0  stage_scope=BRAIN_WEB_PARTIAL       lane=web_llm
034020 두산에너빌리티  canonical_stage=1  stage_scope=BRAIN_WEB_PARTIAL       lane=web_llm

001360 삼성제약        canonical_stage=1  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
001470 삼부토건        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
002460 HS화성          canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
002990 금호건설        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
003090 대웅            canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
003380 하림지주        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
005930 삼성전자        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
005960 동부건설        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
006050 국영지앤엠      canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
007980 TP              canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
010130 고려아연        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
010950 S-Oil           canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
010960 삼호개발        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
028100 동아지질        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
034730 SK              canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
034830 한국토지신탁    canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
042370 비츠로테크      canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
047040 대우건설        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
052400 코나아이        canonical_stage=0  stage_scope=BRAIN_OFFICIAL_PARTIAL  lane=official
```

해석:

```text
Stage row는 있다.
하지만 대부분 canonical_stage=0이고, 전부 NOT_FULL_THESIS_STAGE다.
삼성전자도 BRAIN_OFFICIAL_PARTIAL row는 생겼지만 canonical_stage=0이다.
SK하이닉스도 BRAIN_WEB_PARTIAL row는 생겼지만 canonical_stage=0이다.
```

쉬운 예:

```text
삼성전자 005930:
  "공식 claim-backed partial row가 상태판에 올라왔다"는 뜻이다.
  "삼성전자 운영 Stage가 확정됐다"는 뜻이 아니다.

SK하이닉스 000660:
  "LLM/web claim-backed partial row가 상태판에 올라왔다"는 뜻이다.
  "C06 Full Thesis Green/Yellow가 확정됐다"는 뜻이 아니다.
```

## 6. 왜 canonical_stage 분포가 v100과 달라졌나

v100 최종 상태판:

```text
canonical_stage:
  0      = 3306
  1      = 54
  2      = 30
  3-Red  = 1
```

v101 replay 상태판:

```text
canonical_stage:
  0      = 3325
  1      = 44
  2      = 21
  3-Red  = 1
```

이 변화는 "점수가 좋아졌다/나빠졌다"가 아니다.
같은 symbol row를 Census event-board row에서 Brain partial row로 교체하면서,
더 보수적인 claim-backed StageCourt base_stage가 들어간 결과다.

쉬운 예:

```text
Census event-board는 "공시가 있으니 Stage1/2 후보"라고 볼 수 있다.
Brain partial은 "claim이 실제로 점수 primitive를 얼마나 닫았나"를 본다.

공시 제목은 있어도 Green primitive가 부족하면,
event-board Stage2 후보가 Brain partial Stage0으로 내려올 수 있다.
```

이것은 정상적인 보수화다.
오히려 이 구분이 없으면 "후보 발견 상태"를 "운영 Stage"로 착각하게 된다.

## 7. Full Thesis 시도 결과

기준 파일:

```text
full_thesis_production_runner_audit_after_v101_policy_replay.json
full_thesis_production_audit_after_v101_policy_replay.json
census_stage_status_after_v101_policy_replay_and_full_thesis_attempt.jsonl
```

결과:

```text
candidate_row_count = 21
candidate_source_counts:
  brain_web_partial_stage_row = 2
  stagecourt_trace_direct_scan = 19

promoted_full_thesis_row_count = 0
blocked_candidate_count = 21
blocked_candidate_follow_up_source_task_count = 53
blocked_candidate_follow_up_seed_event_count = 53
verdict = PENDING_PRODUCTION_FULL_THESIS
```

production full thesis audit:

```text
full_thesis_row_count = 0
production_full_thesis_row_count = 0
production_pass_allowed = false
status = PENDING_FULL_THESIS_PRODUCTION
verdict = PENDING_FULL_THESIS_PRODUCTION
```

full thesis attempt 후에도 상태판은 그대로 안전하다.

```text
stage_scope:
  CENSUS_EVENT_BOARD      = 3370
  BRAIN_OFFICIAL_PARTIAL  = 19
  BRAIN_WEB_PARTIAL       = 2

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391
```

쉬운 예:

```text
21명이 일부 답안지를 제출했다.
졸업심사 후보로는 올렸지만, Green 필수 증빙이 부족해서 21명 모두 졸업 성적표는 보류됐다.
대신 부족한 서류 53개를 다음 Research Brain source task seed로 내보냈다.
```

## 8. 삼성전자 / 하이닉스 현재 해석

### 삼성전자 005930

v101 replay:

```text
stage_scope = BRAIN_OFFICIAL_PARTIAL
brain_partial_evidence_lane = official
canonical_stage = 0
score_scale = EVENT_WEIGHTED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
```

해석:

```text
삼성전자는 공식 claim-backed partial row가 생겼다.
하지만 C06 Green primitive coverage가 닫힌 Full Thesis가 아니다.
운영 Stage 3-Yellow/Green으로 말하면 안 된다.
```

### SK하이닉스 000660

v101 replay:

```text
stage_scope = BRAIN_WEB_PARTIAL
brain_partial_evidence_lane = web_llm
canonical_stage = 0
score_scale = EVENT_WEIGHTED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
```

Full thesis candidate blocker:

```text
present_primitives:
  customer_preorder_or_allocation
  hbm_capacity_pre_sold

missing_green_primitives:
  hbm_capacity_constraint
  revenue_visibility_contract
```

해석:

```text
하이닉스는 web/LLM claim-backed partial row가 생겼다.
하지만 C06 Full Thesis Green/Yellow를 확정할 만큼 필수 primitive가 닫히지 않았다.
그래서 다음 source task가 필요하다.
```

## 9. 안전성 검증

이번 패치가 반드시 지켜야 하는 안전선:

```text
1. official-only trace가 BRAIN_WEB_PARTIAL로 위장되면 안 된다.
2. web/LLM trace와 official trace가 서로를 global blocker로 막으면 안 된다.
3. partial row가 FULL_THESIS로 보이면 안 된다.
4. partial row가 operator usable score/stage로 보이면 안 된다.
5. FULL_THESIS/Green promotion은 별도 production gate가 막아야 한다.
```

검증 결과:

```text
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
  Ran 17 tests
  OK

PYTHONPATH=src python -m unittest tests.test_census_v4_brain_web_readiness_gate tests.test_census_v4_stage_signal_split tests.test_census_v4_primitive_state_chain -v
  Ran 34 tests
  OK

PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4_*.py' -v
  Ran 141 tests
  OK

PYTHONPATH=src python -m unittest discover -s tests -v
  Ran 5126 tests in 242.369s
  OK
```

## 10. 교차검증 결론

현재 답변:

```text
Q. 뭔가 잘못되고 있는 거 맞나?
A. v100 기준으로는 맞다. Brain StageCourt trace 21개가 있었는데 promotion policy가 global blocker로 막아 최종 상태판에 0개만 보였다.

Q. Stage가 있는 애들이 있긴 한가?
A. 있다. v101 replay 기준 21개 partial Stage row가 있다.
   단, 이것은 FULL_THESIS 운영 Stage가 아니다.

Q. 삼성전자/하이닉스는 Stage가 확정됐나?
A. 아니다.
   삼성전자는 BRAIN_OFFICIAL_PARTIAL canonical_stage=0.
   하이닉스는 BRAIN_WEB_PARTIAL canonical_stage=0.
   둘 다 operator_stage_use=NOT_FULL_THESIS_STAGE다.

Q. v101 패치로 운영 준비가 끝났나?
A. 아니다.
   v101은 "부분 Stage 존재를 상태판에 올리는 문제"만 고쳤다.
   Full Thesis production runner는 여전히 21개 후보 모두 blocked 처리했고, 53개 follow-up source task seed를 만들었다.
```

## 11. 다음 패치 방향

v101 다음 단계는 partial Stage row를 더 올리는 것이 아니라, Full Thesis 후보의 missing primitive를 닫는 것이다.

우선순위:

```text
1. v101 replay가 아니라 v101 코드로 full live bounded rerun을 수행한다.
2. 새 run에서 brain_web_readiness_gate_audit이 v101 promotion policy를 반영하는지 확인한다.
3. BRAIN_WEB_PARTIAL 2개와 BRAIN_OFFICIAL_PARTIAL 19개가 live run에서도 재현되는지 확인한다.
4. full_thesis_blocker_follow_up_seed_events.jsonl 53개를 다음 Research Brain planner input으로 실제 실행한다.
5. source-backed accepted claim으로 missing_green_primitives를 닫는다.
6. 그 뒤에도 FULL_THESIS가 0이면, primitive mapping / source task satisfaction / score contribution ledger 중 어디서 끊기는지 추적한다.
7. FULL_THESIS가 생기더라도 operator_stage_use=FULL_THESIS_STAGE, operator_score_use=FULL_E2R_SCORE, score interval, source quorum, Green primitive coverage가 모두 닫혔는지 확인한다.
```

절대 하면 안 되는 것:

```text
1. BRAIN_OFFICIAL_PARTIAL을 FULL_THESIS처럼 표시하기
2. CENSUS_EVENT_BOARD Stage1/2를 운영 Stage라고 말하기
3. partial score를 100점 E2R score처럼 비교하기
4. missing primitive가 남았는데 Green/Yellow 확정하기
5. 삼성전자/하이닉스 예외를 코드에 박기
```

쉬운 예:

```text
하이닉스에 customer allocation claim이 있다.
그래도 hbm_capacity_constraint와 revenue_visibility_contract가 빠졌으면 C06 Green은 닫히지 않는다.
이때 해야 할 일은 "하이닉스는 Green"이라고 말하는 게 아니라,
부족한 primitive를 source task로 보내고 claim으로 닫는 것이다.
```

## 12. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 우선 공격하면 된다.

```text
1. BRAIN_OFFICIAL_PARTIAL이 정말 official accepted claim만으로 구성되는가?
2. BRAIN_WEB_PARTIAL 2개가 정말 web/LLM claim-backed인가?
3. mixed trace인 두산에너빌리티가 official lane과 web lane에 중복 승격되지 않는가?
4. partial row의 operator_stage_use/operator_score_use가 모두 NOT_FULL인지?
5. full thesis attempt가 partial row를 몰래 FULL_THESIS로 바꾸지 않는지?
6. v101 replay가 기본 brain_web_readiness_gate_audit.json을 갱신하지 않은 점이 리포트에서 오해를 만들지 않는지?
7. live rerun에서도 같은 promotion count가 재현되는지?
8. 53개 follow-up source task seed가 실제 Research Brain planner input으로 소비되는지?
9. follow-up 실행 뒤 score delta가 claim delta로 설명되는지?
10. 삼성전자/하이닉스가 부분 상태판을 운영 Stage처럼 출력하지 않는지?
```

## 13. 최종 판정

```text
v101 patch verdict:
  PARTIAL_STAGE_VISIBILITY_FIXED_BY_REPLAY

operational readiness:
  NOT_READY

full thesis:
  0

production pass:
  false

main remaining blocker:
  partial Stage row는 생겼지만, Full Thesis green-gate primitive coverage와 source-backed production runner closure가 아직 닫히지 않았다.
```

한 문장으로 정리:

```text
v101은 "Stage가 있는 애들이 있긴 한가"라는 질문에 partial 기준으로는 "있다"고 답하게 만든 패치다.
하지만 "운영 Stage가 있나"라는 질문의 답은 여전히 "없다"다.
```
