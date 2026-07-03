# Census v3 Stage Map Audit - 2026-07-01

> 최신 v4 현재값 문서가 아니다.
>
> 이 파일은 `output/census_v3/2026-07-01`의 과거 forensic 기록이다.
> v4 최신 Stage 분포, 테스트 수, Brain/Web 상태는
> `census_v4_current_truth_table_2026-07-01.md`와
> `census_v4_stage_reality_audit_2026-07-01.md`를 기준으로 봐야 한다.
>
> 쉬운 예: 이 문서는 "이전 시험지에서 어디가 틀렸는지" 보는 답안 해설이고,
> 현재 성적표가 아니다.

작성일: 2026-07-01  
대상 산출물: `output/census_v3/2026-07-01`  
대상 코드 HEAD: `baaf2e72c3c0861969f5144691cfea0db6e4ffe5`  
주의: 감사 시작 시점에 `docs/core/goal*.md`에는 이미 별도 수정이 있었다. 이 문서는 그 파일들을 건드리지 않고 `docs/0701`에 새로 작성한 독립 감사 기록이다.

## 최종 판정

현재 산출물은 그대로 **실제 운영 확정 Stage 지도**라고 부르면 안 된다.

더 정확한 이름은 다음이다.

```text
Anti-fake full-universe status board
= 전 종목에 상태 row를 만들고,
  claim 없는 점수, price-only 점수, provider failure를 낮은 점수로 확정하는 문제를 막은 상태판
```

아직 아닌 것:

```text
Meaningful operational Stage map
= 전 종목 또는 운영 후보에 대해
  같은 evidence chain에서 나온 full E2R score/stage를 안정적으로 산출한 지도
```

쉬운 예:

```text
현재 PASS:
출석부 3,391명 모두 있음.
일부 학생은 채점지 번호도 있음.
채점지 없는 학생에게 점수를 주지는 않았음.

아직 부족:
그 채점지가 같은 시험의 점수인지,
4.4점이 100점 만점 점수인지,
Stage2라는 말이 시험 합격인지 단순 재확인 대상인지
아직 섞여 있음.
```

## 교차검증 요약

이번 감사는 세 관점으로 교차검증했다.

### 결과물 관점

결론:

- Stage가 있는 종목은 있다.
- 그러나 `Stage1` 안에 검증 완료와 미채점 대기가 섞여 있다.
- 일부 종목은 최종 row의 `base_stage/verified_score`와 `stagecourt_trace_id`가 가리키는 trace가 서로 맞지 않는다.
- `contract_quality` claim에 매출 계약과 금융/지분/담보성 계약이 섞이는 semantic noise가 있다.

### 코드 경로 관점

결론:

- `Stage2-Watch + verified_score 1.5~4.4`는 코드상 설명된다.
- 이유는 `Stage2-Watch`가 45점 이상이라는 뜻이 아니라, production cutover StageCourt의 `base_stage == "2"`를 v3가 `Stage2-Watch`로 번역하기 때문이다.
- 하지만 v3가 여러 날짜/여러 이벤트를 종목 단위로 합치면서 stage, score, score status, trace id가 서로 다른 row에서 올 수 있다.

### 테스트/수용조건 관점

결론:

- `4834 tests OK`와 `FULL_UNIVERSE_STAGE_MAP_PASS`는 거짓 점수 방지에는 의미가 있다.
- 그러나 운영적으로 의미 있는 Stage 품질까지 보장하지 않는다.
- 특히 test/self-repair/full-run 사실이 readiness verdict의 hard input으로 묶여 있지 않고, auditor도 score scale/trace atomicity/semantic quality를 직접 검증하지 않는다.

## 현재 산출물 숫자

`output/census_v3/2026-07-01` 기준:

```text
raw_universe_count: 3940
eligible_symbol_count: 3391
stage_status_count: 3391
missing_symbol_count: 0
duplicate_symbol_count: 0
```

Stage 분포:

```text
Stage0:       3306
Stage1:         47
Stage2-Watch:   37
Red:             1
```

상태 분포:

```text
SCANNED:        3306
DEEP_VERIFIED:    74
LIGHT_ONLY:        3
PENDING_SOURCE:    8
```

점수 상태:

```text
NO_CURRENT_EVENT:          3306
FINAL_WITH_NONMATERIAL_GAPS: 38
PENDING_MATERIAL_GAPS:       36
NOT_SCORED:                  11
```

Evidence/trace:

```text
accepted_claim_count:       92
score_contribution_count:   92
stagecourt_trace_count:     92
claim-backed stage rows:    74
verified_score rows:        74
non-Stage0 rows:            85
```

중요한 점:

```text
Stage3-Green:  0
Stage3-Yellow: 0
4A/4B/4C:      0
Stage5:        0
```

따라서 현재 지도는 "상위 Stage 후보를 잘 잡았다"가 아니라 "대부분은 Stage0/NoCurrentCatalyst, 일부 공식 이벤트는 Watch/Pending으로 표시했다"에 가깝다.

## 사용자가 물은 질문에 대한 정확한 답

질문:

```text
뭔가 잘못되고있는거맞지? stage가 있는애들이 있긴해?
```

답:

```text
Stage가 있는 종목은 있다.
비-Stage0은 85개이고, claim/score/StageCourt trace까지 있는 row는 74개다.

하지만 현재 결과를 운영 확정 Stage 지도라고 보면 안 된다.
Stage2-Watch 대부분은 점수 확정이 아니라 material gap pending 상태이고,
삼성전자/하이닉스는 전체 HBM thesis를 평가한 것이 아니라
2026-06-24 DART 공시 이벤트 한두 개만 반영한 Stage1 row다.
```

쉬운 예:

```text
삼성전자 Stage1 / 4.0
= "삼성전자의 HBM 전체 투자 논리가 4점"이라는 뜻이 아니다.
= "2026-06-24 DART 해명 공시 한 건이 information_confidence 이벤트로 잡혔다"는 뜻이다.

SK하이닉스 Stage1 / 4.0
= "하이닉스 HBM 논리가 4점"이라는 뜻이 아니다.
= "유상증자/증권신고서 공시 이벤트가 capital_allocation/information_confidence로 잡혔다"는 뜻이다.
```

## 대표 사례

### 삼성전자 `005930`

최종 row:

```text
base_stage: Stage1
census_status: DEEP_VERIFIED
assessment_depth: VERIFIED_STAGE
score_valid_status: FINAL_WITH_NONMATERIAL_GAPS
verified_score: 4.0
accepted_claim_count: 1
score_contribution_count: 1
```

accepted claim:

```text
primitive_id: information_confidence
quote_text: 삼성전자(005930) 풍문또는보도에대한해명(미확정) OpenDART 접수번호 20260624801004 접수일 2026-06-24
source_provider: OpenDART
```

해석:

```text
이건 HBM/C06 thesis 평가가 아니다.
단일 DART 해명 공시 이벤트를 정보 신뢰도 claim으로 반영한 것이다.
```

패치 요구:

```text
삼성전자/하이닉스 live smoke는 "최근 DART 이벤트 점수"와 "full thesis score"를 분리해야 한다.
```

### SK하이닉스 `000660`

최종 row:

```text
base_stage: Stage1
verified_score: 4.0
accepted_claim_count: 2
score_contribution_count: 2
```

accepted claims:

```text
1. 주요사항보고서(유상증자결정) -> capital_allocation_event
2. 증권신고서(지분증권) -> information_confidence
```

문제:

```text
최종 row score_interval_lower는 4.0인데,
연결된 stagecourt_trace_id가 가리키는 trace의 score_interval은 3.2다.
```

이건 종목에 여러 trace가 있을 때 v3가 "첫 trace"를 연결하면서, score는 다른 row에서 가져오는 혼합 문제다.

### 삼부토건 `001470`

최종 row:

```text
base_stage: Stage2-Watch
verified_score: 4.4
score_valid_status: FINAL_WITH_NONMATERIAL_GAPS
stagecourt_trace_id: SCT-4573383bbf611733cd8d
```

그런데 `SCT-4573383bbf611733cd8d` trace:

```text
base_stage: 1
score_interval: 4.0 ~ 4.0
score_status: FINAL_WITH_NONMATERIAL_GAPS
```

같은 종목의 다른 trace에는 Stage2/4.4가 있다.

쉬운 예:

```text
최종 성적표에는 "수학 2등급, 4.4점"이라고 써 있는데,
첨부한 채점지는 "영어 1등급, 4.0점"인 상태다.
```

패치 요구:

```text
최종 stage row는 반드시 하나의 원자적 StageCourt result를 대표 trace로 선택하고,
base_stage / verified_score / score_valid_status / claim ids / contribution ids / trace id가 모두 그 trace에서 와야 한다.
```

### 드래곤플라이 `030350`

최종 row:

```text
base_stage: Red
verified_score: 4.0
score_valid_status: FINAL_WITH_NONMATERIAL_GAPS
```

accepted claim:

```text
주권매매거래정지기간변경 (개선기간 부여)
primitive_id: information_confidence
```

해석:

```text
Red는 점수 4.0 때문이 아니라, current direct official risk disclosure라는 StageCourt 판단 때문이다.
```

패치 요구:

```text
Red/Reject/4B/4C 계열은 점수와 별개로 risk overlay 성격이 있으므로,
base_stage 하나에 섞지 말고 risk_stage_signal 또는 transition_overlay로 분리해야 한다.
```

## 핵심 문제 1: PASS 라벨이 과장되어 있다

현재 `FULL_UNIVERSE_STAGE_MAP_PASS`는 다음을 보장하는 것처럼 보인다.

```text
전체 KRX에 대해 실제 운영 가능한 Stage map이 완성됐다.
```

하지만 실제로 보장하는 것은 더 좁다.

```text
전체 eligible symbol에 row가 있고,
claim 없는 score를 주지 않았고,
source/proxy/price-only 같은 금지 경로는 대부분 막았다.
```

이 둘은 다르다.

쉬운 예:

```text
ANTI_FAKE_PASS:
가짜 영수증으로 돈을 청구하지 않았는지 확인.

MEANINGFUL_STAGE_PASS:
그 지출이 실제 매출 성장에 도움이 되는지까지 판단.
```

현재는 전자에 가깝다.

### 패치 방향

readiness label을 분리한다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
  - 모든 symbol row 존재
  - claim 없는 점수 없음
  - price-only/source-proxy/provider-failure 점수 없음
  - Stage0/NoCurrentCatalyst trace 존재

MEANINGFUL_OPERATIONAL_STAGE_PASS
  - full score/stage가 같은 StageCourt result에서 나옴
  - score scale이 명시됨
  - pending material gap은 final stage로 표시하지 않음
  - semantic primitive 품질 검증 통과
  - controlled replay에서 Stage2/3/Red/4B/4C가 기대대로 나옴
```

`FULL_UNIVERSE_STAGE_MAP_PASS`는 후자를 만족할 때만 쓰거나, 이름을 바꿔야 한다.

## 핵심 문제 2: stage/score/trace가 원자적으로 묶이지 않는다

코드 경로 요약:

```text
production_cutover_leaf_loader
  -> output/production_cutover_v3/2026-* 여러 날짜 leaf를 모두 로드

census_runner_v3._stage_rows
  -> accepted_ids, score_ids, stagecourt_id가 있으면 DEEP_VERIFIED
  -> base_stage = _stage_from_watch_or_trace(watch_rows, trace_rows)
  -> score = _score_from_watch_or_contributions(watch_rows, contributions)
  -> stagecourt_trace_id = trace["stagecourt_trace_id"]
```

문제:

```text
한 종목에 여러 날짜/여러 event/여러 StageCourt trace가 있으면
base_stage는 가장 높은 신호,
score는 watchlist max 또는 contribution sum,
score_status는 첫 watch/trace,
stagecourt_trace_id는 첫 trace
처럼 서로 다른 row에서 섞일 수 있다.
```

실측 mismatch:

```text
mismatched_trace_rows: 3
- 000660 SK하이닉스: final score 4.0, linked trace score 3.2
- 001470 삼부토건: final Stage2-Watch/4.4, linked trace Stage1/4.0
- 007460 에이프로젠: final score 4.0, linked trace score 3.2
```

### 패치 방향

`RepresentativeStageEvent` 또는 `AtomicStageDecision`을 먼저 만든다.

```python
class AtomicStageDecision:
    symbol: str
    candidate_event_id: str
    stagecourt_trace_id: str
    base_stage: str
    score_status: str
    score_interval_lower: float | None
    score_interval_upper: float | None
    accepted_claim_ids: list[str]
    score_contribution_ids: list[str]
    source_cutover_date: str
```

그 다음 최종 census row는 반드시 이 객체 하나에서 필드를 가져온다.

금지:

```text
stage는 trace A
score는 watch row B
status는 watch row C
trace id는 trace D
```

허용:

```text
representative trace 하나를 고른다.
나머지는 merged_event_trace_ids/backlog로 붙인다.
```

## 핵심 문제 3: `verified_score`라는 이름이 오해를 만든다

현재 `verified_score`는 경우에 따라 의미가 달라질 수 있다.

```text
watchlist row에 verified_score가 있음
  -> production쪽 weighted score일 가능성

watchlist row에 verified_score가 없음
  -> score_contributions.raw_points 단순 합산 fallback
```

이 둘은 같은 스케일이 아니다.

실측:

```text
verified_score rows: 74
scored_under_10: 74
Stage2-Watch score range: 1.5 ~ 4.4
Red score: 4.0
```

이 숫자는 전체 E2R 100점 점수처럼 보이면 안 된다.

쉬운 예:

```text
4.4점
= 전체 투자 점수 4.4점이 아니라
= "단일 공식 공시 이벤트가 earnings_visibility 일부 항목에 4.4점 기여"라는 의미에 가깝다.
```

### 패치 방향

필드를 나눈다.

```text
event_evidence_score
  - 단일 candidate event 또는 제한된 source task에서 나온 점수

full_e2r_verified_score
  - full Evidence OS + deterministic scorer가 모든 필수 component를 평가한 운영 점수

score_scale
  - FULL_E2R_100
  - EVENT_WEIGHTED_PARTIAL
  - RAW_CONTRIBUTION_SUM

score_source
  - WATCHLIST_WEIGHTED_SCORE
  - STAGECOURT_SCORE_INTERVAL
  - RAW_CONTRIBUTION_FALLBACK
```

그리고 `verified_score`는 `FULL_E2R_100`일 때만 쓰거나, schema에서 deprecate한다.

## 핵심 문제 4: `Stage2-Watch` 의미가 두 개다

현재 사용자 기대:

```text
Stage2면 어느 정도 점수와 사업 논리가 올라온 후보
```

현재 production cutover 의미:

```text
direct official material claim이 있어서 watch해야 하는 이벤트
```

그래서 다음이 가능해졌다.

```text
Stage2-Watch + verified_score 1.5
Stage2-Watch + verified_score 4.4
```

코드상으로는 말이 된다. 하지만 출력 명칭은 사용자를 속인다.

쉬운 예:

```text
"입학 2단계 합격"처럼 보이지만,
실제로는 "서류 한 장 들어왔으니 2차 확인 필요"라는 뜻이다.
```

### 패치 방향

Stage를 세 축으로 분리한다.

```text
base_stage
  - canonical E2R stage: 0/1/2/3-Green/3-Yellow/3-Red/4A/4B/4C/5

stage_signal
  - NO_CURRENT_CATALYST
  - OFFICIAL_EVENT_WATCH
  - MATERIAL_CLAIM_WATCH
  - RISK_REVIEW
  - FULL_THESIS_STAGE

investigation_status
  - COMPLETE
  - PENDING_SOURCE
  - PENDING_MATERIAL_GAPS
  - PROVIDER_PENDING
  - NO_CURRENT_CATALYST

transition_overlay
  - NONE/4A/4B/4C
```

현재 `Stage2-Watch` 대부분은 `base_stage=1 or 2?`보다 `stage_signal=MATERIAL_CLAIM_WATCH`, `investigation_status=PENDING_MATERIAL_GAPS`로 보여주는 편이 맞다.

## 핵심 문제 5: semantic primitive 품질이 약하다

현재 claim primitive 분포:

```text
contract_quality:          39
capital_allocation_event:  32
information_confidence:    16
capacity_expansion:         5
```

의심 사례:

```text
자기주식취득신탁계약체결결정 -> contract_quality -> earnings_visibility
주식담보제공계약체결 -> contract_quality -> earnings_visibility
```

문제:

```text
"계약"이라는 단어가 있다고 모두 매출/수주/고객 품질 계약이 아니다.
```

쉬운 예:

```text
고객사와 3년 공급계약
  -> 매출 가시성/수주 품질 가능

자기주식취득 신탁계약
  -> 자본정책/주주환원/정보 이벤트 가능
  -> 매출 가시성 계약은 아님

주식담보제공 계약
  -> 지배구조/리스크/금융 이벤트 가능
  -> 고객 수요 계약은 아님
```

### 패치 방향

primitive를 분리한다.

```text
commercial_supply_contract
customer_order_or_backlog
framework_agreement_without_revenue_visibility
financial_contract
shareholder_return_contract
pledge_or_collateral_contract
administrative_disclosure
information_confidence_only
```

`contract_quality -> earnings_visibility`는 아래 조건이 있을 때만 허용한다.

```text
target company direct
AND customer/counterparty or product/service scope exists
AND revenue/volume/period/backlog/order value exists
AND not share buyback/trust/collateral/equity issuance/admin clarification
```

LLM 역할:

```text
문서가 어떤 종류의 계약인지 분류한다.
```

코드 역할:

```text
allowed primitive registry와 source anchor로 score eligibility를 계산한다.
```

## 핵심 문제 6: `DEEP_VERIFIED/COMPLETE`가 너무 강한 말이다

현재:

```text
accepted_ids + score_ids + stagecourt_id가 있으면
census_status=DEEP_VERIFIED
assessment_depth=VERIFIED_STAGE
investigation_status=COMPLETE
```

하지만 Stage2-Watch 37개 중 36개는:

```text
score_valid_status=PENDING_MATERIAL_GAPS
missing_primitives:
  - cash_or_revision_conversion
  - repeat_evidence_family
```

즉 source task 하나는 끝났지만 thesis 판단은 끝나지 않았다.

쉬운 예:

```text
서류 한 장은 확인 완료.
하지만 합격 심사에 필요한 추천서/성적표는 아직 없음.
이걸 "심사 완료"라고 하면 안 된다.
```

### 패치 방향

완료 상태를 쪼갠다.

```text
source_task_status: COMPLETE
claim_adjudication_status: ACCEPTED
stage_decision_status: PENDING_MATERIAL_GAPS
thesis_evaluation_status: NOT_FULLY_EVALUATED
```

`investigation_status=COMPLETE`는 full thesis material gap이 없을 때만 쓴다.

## 핵심 문제 7: `source_task_execution` status 해석이 불명확하다

실측:

```text
source_task_execution status:
EVIDENCE_OS_ACCEPTED:       60
EVIDENCE_OS_BASELINE_ONLY:  32
```

`EVIDENCE_OS_BASELINE_ONLY`인데 `score_claim_ids`가 있는 row:

```text
32
```

이 자체가 무조건 오류라는 뜻은 아니다. 기존 baseline accepted claim을 재사용한 경로일 수 있다.

하지만 운영 문서에서는 다음을 분명히 해야 한다.

```text
EVIDENCE_OS_ACCEPTED
  - 해당 source task가 accepted claim을 직접 만들었다.

EVIDENCE_OS_BASELINE_ONLY
  - task primitive를 직접 만족하지 않았지만 기존 baseline claim이 score에 쓰였다.
  - 이 경우 score/status/follow-up에서 "direct source task success"처럼 보이면 안 된다.
```

### 패치 방향

audit count 추가:

```text
baseline_only_score_claim_count
baseline_only_stage_promotion_count
source_task_claim_satisfaction_mismatch_count
```

그리고 `satisfies_source_task=false` claim이 Stage2/Red 승급에 쓰이는 경우 별도 검토가 필요하다.

## 핵심 문제 8: official event count가 0으로 남는다

OpenDART accepted claim 기반 row 74개도 `recent_official_event_count=0`으로 남아 있다.

문제:

```text
사용자는 "공식 공시 기반 Stage"라고 보는데,
카운터는 공식 이벤트 0개라고 말한다.
```

### 패치 방향

`recent_official_event_count` 계산에 다음을 포함한다.

```text
candidate_events source_family=DART/KIND/KRX
accepted_claims source_provider=OpenDART
source_task_executions document_urls dart.fss.or.kr
```

또는 필드를 분리한다.

```text
recent_candidate_event_count
accepted_official_claim_count
official_source_task_count
```

## 현재 PASS가 잡는 것과 못 잡는 것

### 잘 잡는 것

```text
missing symbol
duplicate symbol
accepted claim 0인데 전체 pass
score contribution 0인데 전체 pass
claim 없는 verified_score
source_proxy_only score
evidence_url_pending score
price-only score
market anomaly score
news snippet score
provider failure final score
전체 Unknown
전체 ProviderPending
전체 Stage0
```

### 못 잡는 것

```text
base_stage와 linked stagecourt trace 불일치
score interval과 linked stagecourt trace 불일치
score scale 혼합
Stage2-Watch가 threshold stage인지 event watch인지 의미 혼합
PENDING_MATERIAL_GAPS인데 COMPLETE로 표시
semantic primitive 오분류
금융/지분 계약을 earnings visibility 계약으로 오인
source task baseline-only claim을 direct accepted task처럼 해석
official event count 불일치
readiness verdict가 full test/self-repair를 실제 gate로 사용하지 않음
```

## 즉시 추가해야 할 audit counts

`leaf_artifact_auditor.py`에 추가해야 한다.

```text
stage_trace_stage_mismatch_count
stage_trace_score_interval_mismatch_count
stage_trace_score_status_mismatch_count
stage_trace_claim_set_mismatch_count
stage_trace_contribution_set_mismatch_count
score_scale_missing_count
score_scale_mixed_fallback_count
verified_score_not_full_e2r_count
pending_material_marked_complete_count
stage2_pending_material_count
stage2_low_score_without_signal_explanation_count
baseline_only_score_claim_count
baseline_only_stage_promotion_count
contract_quality_semantic_guard_missing_count
official_claim_but_recent_official_event_zero_count
readiness_missing_test_gate_count
readiness_missing_self_repair_gate_count
```

Hard fail로 둘 것:

```text
stage_trace_stage_mismatch_count > 0
stage_trace_score_interval_mismatch_count > 0
score_scale_missing_count > 0
verified_score_not_full_e2r_count > 0 when field name is verified_score
pending_material_marked_complete_count > 0
contract_quality_semantic_guard_missing_count > 0
```

Warning으로 둘 것:

```text
stage2_pending_material_count > 0
baseline_only_score_claim_count > 0
official_claim_but_recent_official_event_zero_count > 0
```

## 패치 우선순위

### P0 - 표시/판정 과장 차단

목표:

```text
다시 "4.4점 Stage2"를 전체 운영 점수처럼 말하지 못하게 한다.
```

작업:

1. `verified_score`를 `event_evidence_score`와 `full_e2r_verified_score`로 분리한다.
2. `score_scale`, `score_source`, `stage_source` 필드를 추가한다.
3. `FULL_UNIVERSE_STAGE_MAP_PASS`를 현재 의미에 맞게 downgrade하거나 label을 분리한다.
4. `PENDING_MATERIAL_GAPS` row는 `investigation_status=COMPLETE`가 아니라 `stage_decision_status=PENDING_MATERIAL_GAPS`로 출력한다.

### P0 - Atomic StageDecision 선택

목표:

```text
최종 row가 참조하는 trace와 row 내용이 반드시 일치하게 한다.
```

작업:

1. 종목별 stage row를 만들기 전에 candidate event별 `AtomicStageDecision`을 만든다.
2. 대표 decision을 하나 선택한다.
3. 최종 row의 stage/score/status/claim/contribution/trace id는 모두 대표 decision에서 가져온다.
4. 여러 event가 있으면 `additional_stage_decision_ids`로 별도 보존한다.
5. mismatch audit을 hard fail로 추가한다.

### P0 - Semantic contract guard

목표:

```text
DART report title에 "계약"이 있다고 매출 계약으로 점수 주는 문제를 차단한다.
```

작업:

1. `contract_quality`를 revenue-facing contract와 financial/admin contract로 분리한다.
2. 자기주식취득신탁, 주식담보, 지분증권, 해명공시, 유상증자 등은 `earnings_visibility`에 직접 들어가지 못하게 한다.
3. LLM extractor는 계약 종류를 분류하고, deterministic mapper가 allowed primitive만 score eligible로 통과시킨다.

### P1 - Meaningful operational stage acceptance

목표:

```text
거짓 점수 방지와 운영 Stage 품질을 분리해서 통과시킨다.
```

새 acceptance:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
MEANINGFUL_OPERATIONAL_STAGE_PASS
```

`MEANINGFUL_OPERATIONAL_STAGE_PASS` 조건:

```text
1. full_e2r_verified_score가 있는 row는 score_scale=FULL_E2R_100.
2. every Stage2/3/Red/4 row has atomic StageDecision match.
3. PENDING_MATERIAL_GAPS는 final operational stage로 표시하지 않음.
4. source task와 accepted claim satisfaction이 일치.
5. controlled replay에서 Stage2/3-Green/3-Yellow/3-Red/4B/4C 기대 결과 통과.
6. 삼성전자/하이닉스 C06/HBM smoke는 recent DART event가 아니라 full thesis task로 별도 실행.
7. semantic contract guard 통과.
8. readiness verdict가 full tests/self-repair/auditor/reviewer 결과를 실제 input으로 사용.
```

### P1 - 삼성전자/하이닉스 smoke 재정의

현재 결과:

```text
삼성전자: DART 해명 공시 event score
SK하이닉스: DART 유상증자/증권신고서 event score
```

필요한 결과:

```text
삼성전자/하이닉스 C06/HBM full thesis score
```

SourceTask는 다음을 분리해야 한다.

```text
daily_event_task
  - 오늘 새 공시/뉴스 event가 있는지 확인

full_thesis_refresh_task
  - HBM customer allocation, qualification, capacity, revenue mix, margin/FCF/revision bridge를 확인
```

두 결과를 같은 `verified_score`에 넣으면 안 된다.

## 다음 구현자에게 주는 작업 지시

다음 에이전트는 바로 코드 패치를 시작하지 말고 아래 순서로 들어가야 한다.

1. `census_runner_v3._stage_rows`에서 stage row 생성 경로를 먼저 읽는다.
2. `production_cutover_leaf_loader`가 여러 날짜의 artifacts를 어떻게 합치는지 확인한다.
3. `official_live_shadow.py`의 production StageCourt 정책을 확인한다.
4. `leaf_artifact_auditor.py`에 atomic mismatch counts를 추가한다.
5. `tests/test_census_v3_*`에 아래 regression을 추가한다.

필수 regression:

```text
1. 한 종목에 Stage1 trace와 Stage2 trace가 같이 있을 때 final row가 Stage2면 linked trace도 Stage2여야 한다.
2. final score interval이 linked trace score interval과 다르면 audit FAIL.
3. Stage2-Watch + PENDING_MATERIAL_GAPS는 investigation_status COMPLETE로 출력하지 않는다.
4. verified_score는 score_scale=FULL_E2R_100 없이는 출력하지 않는다.
5. raw contribution fallback은 event_evidence_score로만 출력한다.
6. 자기주식취득신탁계약은 contract_quality/earnings_visibility로 score eligible이 아니다.
7. 주식담보제공계약은 customer contract_quality가 아니다.
8. DART accepted claim이 있으면 official claim counter가 0이면 안 된다.
9. readiness verdict는 full test summary와 self-repair result가 없으면 FULL pass를 주지 않는다.
10. 삼성전자/하이닉스 DART event score와 C06/HBM thesis score를 같은 필드에 넣지 않는다.
```

## 용어 정리

### Stage가 있다

현재 산출물에서 `base_stage != Stage0`인 row가 있다는 뜻.

```text
현재 85개.
```

### 검증된 Stage row가 있다

`accepted_claim_ids`, `score_contribution_ids`, `stagecourt_trace_id`가 있는 row가 있다는 뜻.

```text
현재 74개.
```

### 운영 확정 Stage다

다음까지 만족해야 한다.

```text
full thesis evidence path
same atomic StageCourt trace
score_scale=FULL_E2R_100
score_status final
material gap 없음 또는 stage boundary에 영향 없음
semantic primitive guard 통과
```

현재 산출물은 이 기준을 충족한다고 보기 어렵다.

## 최종 결론

현재 Census v3는 분명히 이전보다 나아졌다.

좋아진 점:

```text
전 종목 row 생성
claim 없는 점수 차단
price-only 점수 차단
provider failure를 낮은 점수로 확정하지 않음
Stage0/NoCurrentCatalyst 대량 처리
일부 공식 claim 기반 Watch row 생성
```

하지만 아직 위험한 점:

```text
PASS 라벨이 운영 Stage 완성처럼 보인다.
Stage/score/trace가 원자적으로 묶이지 않는 사례가 있다.
verified_score 의미가 full score와 event score 사이에서 모호하다.
Stage2-Watch가 점수 Stage인지 watch signal인지 혼동된다.
semantic primitive 품질이 약해 "계약" 단어가 earnings visibility로 새는 사례가 있다.
삼성전자/하이닉스 결과는 HBM full thesis 평가가 아니다.
```

따라서 다음 패치의 목표는 점수를 더 높이는 것이 아니다.

```text
목표:
이 row가 "운영 확정 점수"인지,
"단일 이벤트 watch"인지,
"source pending"인지,
"full thesis refresh 필요"인지
사용자가 절대 헷갈리지 않게 schema와 audit을 고치는 것.
```

이 작업이 끝나기 전에는 `FULL_UNIVERSE_STAGE_MAP_PASS`를 운영 확정 의미로 사용하면 안 된다.
