# Census V4 Full-Thesis Production C05 Audit - 2026-07-05

이 문서는 2026-07-01 v177 production 산출물에서 나온 질문 6개를 그대로 추적한 감사 기록이다.

후속 실행 감사:

- `docs/0705/goal4_manifest_runtime_attempt_patch_audit_2026-07-05.md`

주의:

```text
이 문서는 "이전 산출물에서 왜 10개 production FULL_THESIS가 전부 C05였는가"를 설명한다.
후속 patched Census v4 실행에서는 그 10개 C05 PASS가 유지되지 않고,
production FULL_THESIS row_count=0, production_pass_allowed=false, INVALID_PARTIAL_OUTPUT으로 끝났다.
따라서 최신 운영 상태는 후속 감사 문서의 NOT_READY/PENDING 판단을 기준으로 본다.
```

검증 기준 산출물:

- `docs/operational/census_mode_v4_reproduction_command.md`
- `docs/operational/census_mode_v4_full_thesis_seed_materialization_audit.json`
- `docs/operational/census_mode_v4_full_thesis_production_audit.json`
- `docs/operational/census_mode_v4_full_thesis_production_runner_audit.json`
- `docs/operational/census_mode_v4_samsung_hynix_full_thesis_smoke.json`
- `output/census_v4/2026-07-01-v177-goal-followup-production-after-expanded-brain-web-width/*`

짧은 결론:

```text
FULL_THESIS_PRODUCTION_PASS
!= 모든 아키타입에서 의미 있는 full thesis가 운영 통과했다

현재 의미:
claim-backed FULL_E2R_100 score path가 production run에서 10개 row에 대해 닫혔다

문제:
그 10개가 전부 C05이고, required_positive_missing_primitives/green gap이 남아 있다.
따라서 이 pass는 "score path closed"로 봐야지 "meaningful full thesis passed"로 보면 안 된다.
```

쉬운 예:

```text
정밀검진 예약표 85장을 만들었다.
그중 실제 검사 결과지까지 나온 사람은 10명이다.
그 10명은 전부 같은 진료과(C05)로 처리됐다.
그래서 "병원 접수-검사-결과지 경로가 작동했다"는 말은 가능하지만,
"모든 진료과가 실전 운영 검증을 통과했다"는 말은 아직 아니다.
```

## 1. Production FULL_THESIS 10개가 왜 전부 C05인가?

production runner 요약:

```text
candidate_row_count = 23
promoted_full_thesis_row_count = 10
blocked_candidate_count = 13
promoted_symbols = 001360,001470,002990,010960,034020,034730,043260,047040,060900,097230
blocked_candidate_archetype_counts = C06 1, C01 1, C05 11
```

seed materialization 요약:

```text
seed_event_count = 85
target_archetype_counts = UNKNOWN 85
source_primary_archetype_counts = C05 74, NONE 11
FULL_THESIS_PROMOTED = 10
FULL_THESIS_PROMOTED by source_primary = C05 10
```

즉 seed 단계의 `target_archetype`은 전부 `UNKNOWN/null`이다. C05는 `target_archetype`에서 온 값이 아니라, event-board/refresh queue의 `source_primary_archetype` 맥락과 planner top1이 결합된 결과다.

코드 경로:

```text
full_thesis_refresh_queue.source_primary_archetype
-> seed event structured_payload.source_primary_archetype
-> planner input의 full_thesis_queue_context
-> planner output top_k_archetype_hypotheses[0]
-> v4_production_orchestrator._primary_from_planner()
-> DailyWatchlistItemV4.primary_archetype
-> exported stagecourt trace primary_archetype
-> production row full_thesis_primary_archetype
```

중요한 점:

- `source_primary_archetype`은 코드 주석상 "non-binding event-board context"다.
- 실제 primary 선택은 `top_k_archetype_hypotheses[0]`이다.
- 다만 이번 10개 promoted row는 planner top1도 전부 C05였기 때문에 최종 C05로 닫혔다.

Symbol별 경로:

| symbol | company | seed target_archetype | seed source_primary_archetype | planner top1/top2/top3 | final assigned archetype | assignment source |
|---|---|---|---|---|---|---|
| 001360 | 삼성제약 | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C29 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 001470 | 삼부토건 | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C11 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 002990 | 금호건설 | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C11 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 010960 | 삼호개발 | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C29 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 034020 | 두산에너빌리티 | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C11 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 034730 | SK | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C29 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 043260 | 성호전자 | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C19 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 047040 | 대우건설 | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C29 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 060900 | 에이전트AI | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C29 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |
| 097230 | HJ중공업 | UNKNOWN/null | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05 -> C01 -> C29 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | planner top1, with source_primary context |

## 2. target_archetype_counts는 UNKNOWN인데 최종 C05가 되는 경로

`target_archetype_counts = {"UNKNOWN": 85}`는 seed가 강제로 특정 아키타입을 지정하지 않았다는 뜻이다.

이 값은 정상적으로는 다음 의미다.

```text
target_archetype = null
target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
```

즉 "이번 full thesis refresh에서 planner가 아키타입 가설을 다시 세워라"라는 뜻이지, "아키타입이 없다"는 뜻은 아니다.

그런데 seed 안에는 과거 event-board 문맥이 들어 있다.

```text
source_primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
source_missing_primitives = repeat_evidence_family, cash_or_revision_conversion
source_failed_stage_gates = missing_green_bridge
```

planner는 이 문맥을 보고 `top_k_archetype_hypotheses`를 만든다. 이번 promoted 10개는 모두 top1이 C05였다. 따라서 최종 C05 경로는 다음이다.

```text
target_archetype UNKNOWN
-> source_primary_archetype C05가 planner 참고 문맥으로 들어감
-> planner top1 C05
-> primary_archetype C05
-> Evidence Contract C05로 primitive/state/score 생성
-> production full_thesis_primary_archetype C05
```

감사상 주의:

```text
target_archetype UNKNOWN 자체는 문제가 아니다.
하지만 production 결과가 C05에만 몰렸다면, "전 아키타입 full thesis 운영 검증"이라고 부르면 안 된다.
```

## 3. 27.9998 / 77.9998 점수 formula trace

점수 경로:

```text
ScoreContributionV2 raw_points
-> component별 합산
-> component max로 clamp
-> C05 runtime weight 적용
-> raw_total 합산
-> calibration/floor 확인
-> 0~100 clamp
-> StageCourt threshold 적용
```

C05 runtime weight:

| component | canonical max | C05 weight |
|---|---:|---:|
| eps_fcf_explosion | 20 | 18 |
| earnings_visibility | 20 | 22 |
| bottleneck_pricing | 20 | 10 |
| market_mispricing | 15 | 12 |
| valuation_rerating | 15 | 10 |
| capital_allocation | 5 | 8 |
| information_confidence | 5 | 20 |

공식:

```text
weighted_component = clamp(raw_component, 0, canonical_max) / canonical_max * C05_weight
final_score = clamp(sum(weighted_components) + calibration_bonus - risk_penalty, 0, 100)
```

이번 27.9998은 별도 epsilon이 아니라 소수점 반올림 부산물이다.

```text
earnings_visibility = 13.3333 / 20 * 22 = 14.6666
information_confidence = 3.3333 / 5 * 20 = 13.3332
sum = 27.9998
```

이번 77.9998도 같은 방식이다.

```text
eps_fcf_explosion = 20 / 20 * 18 = 18
earnings_visibility = 13.3333 / 20 * 22 = 14.6666
bottleneck_pricing = 20 / 20 * 10 = 10
market_mispricing = 15 / 15 * 12 = 12
valuation_rerating = 15 / 15 * 10 = 10
information_confidence = 3.3333 / 5 * 20 = 13.3332
sum = 77.9998
```

Stage threshold:

```text
Stage1 threshold = 40
Stage2 threshold = 65
Yellow threshold = 80
Green threshold = 90
```

따라서:

```text
27.9998 -> Stage0
50.0 -> Stage1
77.9998 -> Stage2
```

Symbol별 formula:

| symbol | company | raw component score | weighted formula | score | stage | score_source | score_scale |
|---|---|---|---|---:|---|---|---|
| 001360 | 삼성제약 | earnings_visibility=13.3333/20; information_confidence=3.3333/5 | 13.3333/20*22=14.6666; 3.3333/5*20=13.3332; sum=27.9998 | 27.9998 | 0 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 001470 | 삼부토건 | earnings_visibility=13.3333/20; information_confidence=3.3333/5 | 13.3333/20*22=14.6666; 3.3333/5*20=13.3332; sum=27.9998 | 27.9998 | 0 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 002990 | 금호건설 | earnings_visibility=13.3333/20; information_confidence=3.3333/5 | 13.3333/20*22=14.6666; 3.3333/5*20=13.3332; sum=27.9998 | 27.9998 | 0 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 010960 | 삼호개발 | earnings_visibility=13.3333/20; information_confidence=3.3333/5 | 13.3333/20*22=14.6666; 3.3333/5*20=13.3332; sum=27.9998 | 27.9998 | 0 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 034020 | 두산에너빌리티 | earnings_visibility=13.3333/20; information_confidence=3.3333/5 | 13.3333/20*22=14.6666; 3.3333/5*20=13.3332; sum=27.9998 | 27.9998 | 0 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 034730 | SK | earnings_visibility=13.3333/20; information_confidence=3.3333/5 | 13.3333/20*22=14.6666; 3.3333/5*20=13.3332; sum=27.9998 | 27.9998 | 0 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 043260 | 성호전자 | eps_fcf_explosion=20/20; bottleneck_pricing=20/20; market_mispricing=15/15; valuation_rerating=15/15 | 20/20*18=18; 20/20*10=10; 15/15*12=12; 15/15*10=10; sum=50 | 50.0 | 1 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 047040 | 대우건설 | earnings_visibility=13.3333/20; information_confidence=3.3333/5 | 13.3333/20*22=14.6666; 3.3333/5*20=13.3332; sum=27.9998 | 27.9998 | 0 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 060900 | 에이전트AI | earnings_visibility=13.3333/20; information_confidence=3.3333/5 | 13.3333/20*22=14.6666; 3.3333/5*20=13.3332; sum=27.9998 | 27.9998 | 0 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |
| 097230 | HJ중공업 | eps_fcf_explosion=20/20; earnings_visibility=13.3333/20; bottleneck_pricing=20/20; market_mispricing=15/15; valuation_rerating=15/15; information_confidence=3.3333/5 | 20/20*18=18; 13.3333/20*22=14.6666; 20/20*10=10; 15/15*12=12; 15/15*10=10; 3.3333/5*20=13.3332; sum=77.9998 | 77.9998 | 2 | BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT | FULL_E2R_100 |

이번 10개 row에서 확인한 clamp/floor 상태:

```text
component clamp: 적용 가능 경로 있음. 이번 row들은 raw가 각 component max를 넘지 않음.
total clamp: 0~100 적용. 이번 row들은 100 초과/0 미만 아님.
source-backed green floor: 적용 증거 없음. 점수는 weighted sum 그대로다.
epsilon: 별도 threshold epsilon이 아니라 13.3333 같은 소수 원시점수의 round artifact다.
```

## 4. C05가 아닌 아키타입 후보가 왜 full-thesis production에서 0개인가?

정확히 나누면 다음과 같다.

```text
C06/C01: production runner 후보는 있었지만 source pending gap으로 blocked.
C08/C15/C17/C24/C28: 이번 full-thesis refresh queue/materialization 안에 해당 아키타입 후보가 사실상 없음.
```

Runner blocked candidates:

| archetype | symbol | company | present primitives | missing required/green | source pending gap | blocker |
|---|---|---|---|---|---|---|
| C06 | 005930 | 삼성전자 | medium_term_revision_visibility; revenue_visibility_contract | customer_preorder_or_allocation; hbm_capacity_constraint; hbm_capacity_pre_sold; memory_price_increase_mentioned | customer_preorder_or_allocation; hbm_capacity_pre_sold | source_pending_required_or_green_primitives |
| C01 | 052400 | 코나아이 | contract_quality; delivery_schedule; fcf_quality_score | named_customer_quality; opm_expansion_pctp; order_backlog_to_sales | opm_expansion_pctp | source_pending_required_or_green_primitives |
| C05 | 052710 외 10개 | 아모텍 외 | 일부 계약/납기 primitive | contract_duration_months, margin_bridge_visible 등 | contract_amount/duration/margin 일부 | source_pending_required_or_green_primitives |

주요 아키타입별 상태:

| archetype | 이번 production full-thesis 상태 | blocked reason |
|---|---|---|
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 삼성전자는 후보였지만 blocked. SK하이닉스는 planner top1 C06이었으나 accepted claim이 없어 production candidate로 승격되지 않음. | source_pending_required_or_green_primitives 또는 accepted_claim_not_created |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 후보 0 | refresh queue/source_primary/planner promoted 경로에 없음 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 후보 0 | refresh queue/source_primary/planner promoted 경로에 없음 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 후보 0 | refresh queue/source_primary/planner promoted 경로에 없음 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 후보 0 | refresh queue/source_primary/planner promoted 경로에 없음 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 후보 0 | refresh queue/source_primary/planner promoted 경로에 없음 |

감사 결론:

```text
"C05가 아닌 아키타입이 모두 검증되어 탈락했다"가 아니다.
"이번 production refresh queue가 C05 중심으로 형성됐고, 다른 주요 아키타입은 대부분 후보 경로에 들어오지 않았다"가 맞다.
```

## 5. required_positive_missing_primitives가 있는데 왜 FULL_THESIS_PRODUCTION_PASS인가?

production audit의 숫자:

```text
production_full_thesis_row_count = 10
production_full_thesis_row_with_required_positive_missing_primitives_count = 10
production_full_thesis_row_with_green_gap_primitives_count = 10
production_full_thesis_row_with_blocking_required_gap_primitives_count = 0
production_full_thesis_final_with_source_pending_gap_count = 0
production_pass_allowed = true
```

즉 10개 전부 `full_thesis_required_positive_missing_primitives`와 `full_thesis_green_gap_primitives`가 있다.

예:

```text
001360 삼성제약
score = 27.9998
stage = 0
green_gap = contract_duration_months, margin_bridge_visible
required_positive_missing = contract_duration_months, margin_bridge_visible
source_pending_gap = 없음
```

왜 pass가 됐는가:

```text
현재 pass 조건은 "blocking required/source pending gap이 없는 production FULL_E2R_100 row가 생성됐는가"를 본다.
required_positive_missing_primitives 자체를 hard fail로 보지 않는다.
```

따라서 이 pass의 정확한 의미:

```text
score path closed: YES
meaningful full thesis passed: NO / 과장된 라벨
```

쉬운 예:

```text
계산기는 정상 작동했다.
하지만 답안지가 완성됐다는 뜻은 아니다.
계산 가능한 칸만 계산했고, 아직 채워야 할 증거 칸은 남아 있다.
```

권장 문구:

```text
FULL_THESIS_PRODUCTION_PASS
-> PRODUCTION_FULL_E2R_SCORE_PATH_PASS

meaningful readiness는 별도:
MEANINGFUL_FULL_THESIS_PASS = required_positive_missing_primitives 0
                              AND green_gap_primitives 0 또는 stage가 Green threshold 미만이라 비중요
                              AND 주요 아키타입 coverage 충족
```

## 6. 삼성전자/하이닉스는 왜 production full-thesis row로 안 올라왔나?

삼성전자/하이닉스는 controlled smoke와 production row를 분리해야 한다.

### Controlled smoke

`docs/operational/census_mode_v4_samsung_hynix_full_thesis_smoke.json`은 외부 controlled smoke artifact를 사용했다.

```text
external_smoke_artifact_used = true
external_smoke_artifact_path = output/census_v4/2026-07-01-v162-goal-followup-controlled-full-thesis-smoke-after-official-budget-fix/samsung_hynix_full_thesis_smoke.json
operator_score_use = SMOKE_ONLY_SCORE_NOT_PRODUCTION
operator_stage_use = SMOKE_ONLY_STAGE_NOT_PRODUCTION
```

Controlled smoke 결과:

| symbol | company | full_thesis_archetype | score | stage | operator use |
|---|---|---|---:|---|---|
| 000660 | SK하이닉스 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 88.0 | Stage3-Yellow | SMOKE_ONLY, not production |
| 005930 | 삼성전자 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 72.0 | Stage2-Watch | SMOKE_ONLY, not production |

이 smoke는 "C06 full thesis score path가 URL-backed fixture에서 돈다"를 검증한다. production 운영 row로 섞으면 안 된다.

### Production v177

삼성전자:

```text
production runner blocked candidate로 존재
primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
present = medium_term_revision_visibility, revenue_visibility_contract
missing_required = customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold, memory_price_increase_mentioned
missing_green = customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold
source_pending_gap = customer_preorder_or_allocation, hbm_capacity_pre_sold
blocker = source_pending_required_or_green_primitives
```

즉 삼성전자는 production 후보였지만, C06 Green/required primitive에 대한 source pending gap 때문에 promoted full-thesis row가 아니다.

SK하이닉스:

```text
seed trace에는 존재
planner top1 = C06_HBM_MEMORY_CUSTOMER_CAPACITY
accepted_claim_count = 0
materialization_status = ACCEPTED_CLAIM_NOT_CREATED
final_full_thesis_stage = FULL_THESIS_NOT_RUN
final_full_thesis_score_scale = NO_SCORE
```

즉 하이닉스는 planner가 C06을 봤지만, production refresh materialization에서 accepted claim이 만들어지지 않아 stagecourt trace 후보로 올라오지 못했다.

정리:

```text
삼성전자: production C06 후보였지만 source pending gap으로 blocked.
하이닉스: production seed/planner에는 있었지만 accepted claim이 없어 full-thesis trace 미생성.
controlled smoke의 88/72점은 production 점수가 아니다.
```

## 최종 감사 판단

이번 v177/v178 결과를 정확히 부르면 다음과 같다.

```text
통과한 것:
- full-thesis production score path가 10개 row에서 실제로 생성됐다.
- 10개 row는 FULL_E2R_100 scale과 BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT score_source를 가진다.
- controlled smoke와 production row를 섞지 않는 장치가 있다.

통과하지 않은 것:
- 전 아키타입 full-thesis production coverage.
- C06 삼성/하이닉스 production full-thesis 승격.
- required_positive_missing_primitives 없는 완성형 thesis.
- Green gate까지 닫힌 meaningful full thesis.
```

다음 패치 방향:

```text
1. FULL_THESIS_PRODUCTION_PASS 라벨을 score-path pass와 meaningful-thesis pass로 분리한다.
2. production audit에 promoted row별 planner top_k, seed source_primary, final primary를 항상 기록한다.
3. target_archetype UNKNOWN과 final primary archetype의 연결 trace를 별도 JSON으로 남긴다.
4. required_positive_missing_primitives가 있는 row는 "full thesis complete"가 아니라 "score path closed with remaining thesis gaps"로 표기한다.
5. C06/C08/C15/C17/C24/C28별 production refresh coverage gate를 추가한다.
6. 삼성/하이닉스 controlled smoke 점수는 production 점수와 UI/문서/감사 파일에서 더 강하게 분리한다.
```
