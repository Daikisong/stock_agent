# Score Deduction Mechanics and Green Truth Table - 2026-06-19

## 결론

삼전/하닉이 낮게 나온 이유는 "연구자료가 누적되지 않아서"가 아니다.

연구자료는 누적되어 있고, C06 weight도 실제로 적용된다. 하지만 누적 연구가 바꾼 것은 주로 `7개 component의 비중`과 `guardrail`이다. 연구 문장 자체를 운영 scoring field로 바꾸는 변환부는 아직 부족하다.

쉬운 예:

- 연구자료: "하닉은 HBM 물량이 사실상 매진이고 Q1 surprise와 revision이 있으니 Green."
- 운영 scorer: "`hbm_capacity_pre_sold`, `customer_preorder_or_allocation`, `opm_expansion_pctp`, `actual_fcf`, 독립 revision/news family가 충분히 들어왔나?"
- 결과: 일부는 읽었지만 최종 `bottleneck_pricing`과 total로는 부족해서 Yellow.

## Green 연구 사례는 실제로 있었나

있다. 하지만 모든 Green이 weight에 같은 힘으로 들어간 것은 아니다.

`data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` 기준:

| 항목 | 값 |
| --- | ---: |
| total representative rows | 12,471 |
| Stage3-Green labels | 381 |
| usable_for_weight_calibration=true Green | 162 |
| usable_for_weight_calibration=false Green | 219 |
| dedupe_for_aggregate=true Green | 161 |
| dedupe_for_aggregate=false Green | 220 |

Green의 aggregate role:

| role | count |
| --- | ---: |
| label_comparison_only | 183 |
| representative | 147 |
| null/legacy shape | 48 |
| 4B_overlay_only | 2 |
| green_lateness_comparison_not_representative | 1 |

해석:

- "Green 사례가 381개"와 "381개가 모두 점수표에 직접 들어갔다"는 다르다.
- 실제 weight calibration usable Green은 162개다.
- label comparison Green은 "이 시점까지 기다리면 늦다/맞다"를 비교하는 용도라 weight 본체에는 약하게 들어간다.

## C06 HBM Green 정답표

C06 전체 대표 장부:

| 항목 | 값 |
| --- | ---: |
| C06 trigger rows | 229 |
| C06 Stage3-Green labels | 9 |
| C06 usable Green | 7 |
| C06 good Stage2 | 82 |
| C06 bad Stage2 | 42 |
| C06 false positive | 66 |
| C06 missed structural | 11 |
| C06 too late | 36 |

대표 Green:

| symbol | date | trigger | role | usable | verdict | 핵심 근거 |
| --- | --- | --- | --- | --- | --- | --- |
| 000660 SK하이닉스 | 2024-03-19 | Stage3-Green | representative | true | current_profile_correct_green_with_drawdown_aware_hold | HBM3E 양산, Nvidia shipment, 2024 HBM capacity booked |
| 000660 SK하이닉스 | 2024-04-25 | Stage3-Green | representative/null | true | current_profile_correct | Q1 surprise, HBM sold/booked-out capacity, revision visibility |
| 000660 SK하이닉스 | 2024-05-02 | Stage3-Green | label_comparison_only | false | current_profile_correct | 2024 sold out, 2025 almost booked |
| 000660 SK하이닉스 | 2024-06-13 | Stage3-Green | representative | false | current_profile_too_late | 논리는 맞지만 entry가 이미 늦음 |
| 000660 SK하이닉스 | 2024-09-26 | Stage3-Green | representative | true | partly too permissive if late valuation not penalized | 12-layer HBM3E 후속 확인 |
| 007660 이수페타시스 | 2023-01-19 | Stage3-Green | representative | true | current_profile_correct_entry_but_4B_overlay_needed_after_peak | AI server MLB 고객/수주/증설 bridge |

따라서 "하닉은 과거에 Green으로 잡혀야 했다"는 연구 장부 기준으로 맞다.

## 하닉 2024-04-30은 어디서 깎였나

as-of replay 결과:

| 항목 | 값 |
| --- | ---: |
| stage | Stage3-Yellow |
| total | 76.7639 |
| Green total 기준 | 87.0000 |
| total gap | 10.2361 |
| failed gates | failed_stage3_total_score, failed_stage3_bottleneck |

C06 weight 적용 전후:

| component | raw | C06 max | weighted | Green effective threshold | 결과 |
| --- | ---: | ---: | ---: | ---: | --- |
| EPS/FCF | 20.0000 / 20 | 24 | 24.0000 | 20.4000 | 통과 |
| visibility | 15.1502 / 20 | 21 | 15.9077 | 15.7500 | 통과 |
| bottleneck | 11.6339 / 20 | 19 | 11.0522 | 14.2500 | 실패 |
| mispricing | 12.8520 / 15 | 15 | 12.8520 | 10.0000 | 통과 |
| valuation | 12.3390 / 15 | 12 | 9.8712 | 8.0000 | 통과 |
| capital | 0.1010 / 5 | 4 | 0.0808 | n/a | n/a |
| confidence | 3.0000 / 5 | 5 | 3.0000 | n/a | n/a |

핵심:

- C06 weight는 하닉 점수를 깎지 않았다. raw 합 `75.0761`에서 weighted total `76.7639`로 약 `+1.6878` 올렸다.
- 그런데 `bottleneck`은 C06에서 더 중요한 축인데도 weighted `11.0522`로 Green effective threshold `14.2500`에 못 미친다.
- bottleneck만 threshold까지 올려도 total은 약 `79.9617`이다. Green 87까지는 여전히 약 `7.0383`점 더 필요하다.

즉 문제는 한 군데가 아니다.

1. HBM capacity/customer evidence가 `capa_constraint=0`, `contract_quality=0`, `backlog_rpo_visibility=15`로 약하게 남는다.
2. `domain_specific_evidence_score=80`, `medium_term_revision_visibility=100`인데 최종 `bottleneck_pricing`으로는 `11.6339/20`만 들어간다.
3. report-derived consensus/revision proxy는 일부 점수에는 들어가지만, Green confidence family에서는 independent `consensus`, `consensus_revision`, `news`가 missing으로 남는다.

## 삼성전자는 같은 문제가 아닌가

삼성전자는 두 갈래다.

2024년 C06 연구 장부에서는 삼성전자가 하닉처럼 "HBM first-mover Green"이 아니었다. 오히려 다음 반례가 더 강하다.

| date | stage/research label | verdict | 의미 |
| --- | --- | --- | --- |
| 2024-01-02 | Stage2-Watch | false positive risk | 메모리 회복은 있지만 직접 HBM 고객 qualification 부족 |
| 2024-03-20 | Stage3-Yellow/Weak-Green | false positive | catch-up 기대는 있지만 named qualification/volume 부족 |
| 2024-05-24 | Stage4C-thesis-break | 4C too late | HBM customer qualification issue |
| 2024-07-05 | Stage2-Actionable | false positive | Q2 memory recovery without durable HBM3E qualification |
| 2024-10-08 | Stage4C | 4C too late | Q3 profit miss and HBM3E delay |

그래서 2024년 초중반 삼성전자는 "메모리 턴어라운드 저평가"는 가능하지만, "하닉형 HBM Green"과는 다르게 봐야 한다.

다만 운영 replay의 별도 문제도 있다.

- 2024-04-30 삼성전자는 stage gate에서 떨어진 것이 아니라 `failed_official_cheap_scan`으로 후보 진입 전 단계에서 빠졌다.
- 따라서 삼성 쪽은 scoring conversion뿐 아니라 후보 scan/cheap 조건도 따로 봐야 한다.

쉬운 예:

- 하닉 문제: 후보는 들어왔고 Yellow까지 갔는데 Green 변환이 약함.
- 삼성 문제: 2024-04-30 기준으로는 후보 문 앞에서 빠진 문제도 있음.

## 왜 "누적 연구로 점수표를 만들었는데도" 이런 일이 생겼나

현재 pipeline은 세 단계가 분리되어 있다.

1. 연구 장부: 사람이 이해하기 쉬운 축으로 Green/반례를 기록한다.
2. calibration: 그 장부를 보고 아키타입별 component weight와 guardrail을 만든다.
3. runtime: 실제 문서에서 normalized field를 뽑고 7개 component로 점수를 계산한다.

문제는 2번은 많이 진행됐지만 3번이 부족하다는 것이다.

예:

- C06 weight는 `EPS/FCF 24`, `visibility 21`, `bottleneck 19`로 바뀌었다.
- 하지만 runtime parser가 "HBM sold out"을 `hbm_capacity_pre_sold=true`, `capacity_precommitted=true`, `customer_preorder_or_allocation=true`, `opm_expansion_pctp`로 못 바꾸면 weighted component에 넣을 재료가 없다.

요리로 비유하면:

- 연구 장부는 "좋은 카레 레시피"를 많이 모았다.
- weight profile은 "카레에는 고기와 향신료 비중이 중요하다"고 배웠다.
- 그런데 주방 parser가 고기를 채소로 분류하거나 향신료를 못 알아보면, 레시피가 있어도 맛이 안 난다.

## 전체 아키타입도 같은가

같다. C06만의 문제가 아니다.

대표 Green evidence field 상위값:

| field | count |
| --- | ---: |
| confirmed_revision | 171 |
| financial_visibility | 169 |
| multiple_public_sources | 154 |
| margin_bridge | 90 |
| low_red_team_risk | 52 |
| durable_customer_confirmation | 38 |
| repeat_order_or_conversion | 22 |

그런데 이 evidence field들은 `features.py` runtime scoring field와 exact match가 `0`개다.

Green 관련 score_simulation numeric key도 마찬가지다.

| research key | runtime exact match |
| --- | --- |
| margin_bridge_score | 없음 |
| customer_quality_score | 없음 |
| contract_score | 없음 |
| backlog_visibility_score | 없음 |
| valuation_repricing_score | 없음 |
| commercialization_score | 없음 |
| reserve_quality_score | 없음 |
| arr/retention류 key | 없음 |

간접 매핑은 가능하다. 예를 들어 `margin_bridge_score`는 `opm_expansion_pctp`, `actual_op_yoy_pct`, `fcf_growth_pct`로 바꿔 넣을 수 있다. 하지만 그 번역기가 아직 부족하다.

## 최종 진단

지금 문제는 "Green threshold를 낮추면 해결"이 아니다.

하닉만 보면 threshold 완화가 유혹적이지만, 전체 장부에는 false positive와 high-MAE 반례도 많다. Green 기준을 낮추면 삼성 2024 HBM catch-up headline, C30 PF/정책 이벤트, C31 policy headline 같은 것들이 같이 올라올 위험이 있다.

해야 할 일은 다음이다.

1. C06 HBM 문장을 normalized field로 더 정확히 바꾼다.
2. `sold/booked-out capacity`, `customer allocation`, `HBM ASP/mix`, `Q1 surprise`, `multi-quarter revision`이 final component로 충분히 들어가게 한다.
3. 동시에 삼성 2024 catch-up false positive, R13/C30/C31 반례 replay를 같이 둔다.
4. 그 다음 C01/C02/C20/C21/C22/C23/C28 같은 다른 Green 다발 아키타입도 같은 방식으로 mapping/replay한다.

한 줄로 말하면:

> 연구자료는 누적됐다. 점수 비중도 누적 반영됐다. 하지만 연구 문장을 운영 점수 필드로 번역하는 부분이 아직 덜 누적됐다. 그래서 하닉 같은 정답 사례도 운영 replay에서는 Yellow에 머문다.
