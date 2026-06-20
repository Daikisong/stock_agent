# Green Case Score Axis Conversion Audit - 2026-06-19

## 목적

사용자 질문의 핵심은 이것이다.

> 연구자료에는 Green까지 간 애들이 있었고, 그 연구자료를 누적해서 점수표를 만들었다면 왜 운영 파이프라인은 삼성전자/SK하이닉스 같은 대형 HBM 케이스도 낮게 보느냐?

이번 문서는 연구자료의 Green 사례들이 실제로 어떤 점수축을 썼는지, 그리고 그 축이 운영 scorer에 얼마나 직접 연결되어 있는지 본다.

## 구조화 추출 결과

대상:

- `docs/round/achieve/achieve_v12/**/*.md`

추출:

- JSON row: `39,866`
- strict `row_type=trigger` + `trigger_type`에 `Stage3-Green` 포함: `338`
- `row_type=score_simulation` + before/after label에 `Stage3-Green` 포함: `470`
- calibration representative trigger file 기준 `Stage3-Green` label: `381`
- 그중 `usable_for_weight_calibration=true`: `162`

즉 Green 연구 사례는 실제로 많다. 하닉/C06만의 이야기가 아니다.
위 `338`은 raw MD JSON trigger만 센 값이고, `381`은 `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl`의 현재 대표 장부 기준이다.

## Green trigger가 많은 아키타입

| archetype | Stage3-Green trigger count |
| --- | ---: |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 35 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 31 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 30 |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 29 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 24 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 16 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 14 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 14 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 14 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 13 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 12 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 12 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 11 |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 11 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 10 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 9 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 8 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 7 |

해석:

- 연구자료는 Green 사례를 꽤 많이 쌓았다.
- C06 HBM도 Green이 있지만, 더 많은 Green은 소비재/금융/보험/바이오/플랫폼/산업재에도 있다.
- 따라서 "HBM 변환만 고치면 끝"이 아니다.

## Green이 되려면 연구자료는 무엇을 봤나

strict Stage3-Green trigger의 `stage3_evidence_fields` 상위값:

| evidence field | count |
| --- | ---: |
| confirmed_revision | 197 |
| financial_visibility | 194 |
| multiple_public_sources | 173 |
| margin_bridge | 107 |
| low_red_team_risk | 57 |
| durable_customer_confirmation | 44 |
| repeat_order_or_conversion | 29 |

쉬운 해석:

- Green은 "테마가 좋다"가 아니다.
- Green은 보통 `실적 상향 + 재무 가시성 + 여러 공개출처 + 마진/현금흐름 bridge + 낮은 red-team risk`가 같이 있어야 했다.

예:

- 하닉 C06 Green: HBM sold/booked-out capacity + Q1 surprise + revision/financial visibility.
- HD현대일렉 C02 Green: 변압기 backlog + 데이터센터/grid 수요 + 실적/마진 bridge.
- 유한양행 C23 Green: FDA approval + partnered commercialization + revision/financial visibility.
- 실리콘투 C20 Green: 글로벌 유통 확장 + 반복 수요 + margin/revision bridge.

## Green score_simulation이 쓴 세부 점수축

Green 관련 `score_simulation`에서 나온 raw score key는 현재 추출 기준 `285`개다. 반면 운영 `features.py`가 직접 읽는 scoring field key는 helper 호출까지 포함한 최신 추출 기준 `190`개다.

주의: 이 숫자는 추출 방식에 따라 조금 달라질 수 있다. 중요한 점은 Green score key와 runtime scoring field key의 exact match가 현재 `0`개라는 점이다.

이 차이가 핵심이다.

자주 나온 연구 score key:

| research score key | occurrence | 운영 field exact match |
| --- | ---: | --- |
| margin_bridge_score | 928 | 없음 |
| relative_strength_score | 920 | 없음 |
| execution_risk_score | 914 | 없음 |
| valuation_repricing_score | 904 | 없음 |
| revision_score | 898 | 없음 |
| contract_score | 896 | 없음 |
| backlog_visibility_score | 896 | 없음 |
| customer_quality_score | 896 | 없음 |
| policy_or_regulatory_score | 886 | 없음 |
| legal_or_contract_risk_score | 886 | 없음 |
| dilution_cb_risk_score | 886 | 없음 |
| accounting_trust_risk_score | 886 | 없음 |
| positioning_overheat_score | 143 | 없음 |
| thesis_break_score | 90 | 없음 |
| channel_reorder_score | 83 | 없음 |
| roe_pbr_capital_return_score | 65 | 없음 |
| capacity_or_shipment_score | 44 | 없음 |
| reserve_quality_score | 30 | 없음 |
| commercialization_score | 25 | 없음 |
| order_conversion_score | 18 | 없음 |
| sell_through_score | 18 | 없음 |
| fcf_conversion_score | 16 | 없음 |
| capital_return_execution_score | 16 | 없음 |

주의:

- "exact match 없음"이 "전혀 반영 안 됨"이라는 뜻은 아니다.
- 예를 들어 `contract_score`는 운영에서 `multi_year_contract`, `contract_duration_months`, `contract_amount_to_prior_sales`, `customer_prepayment` 등으로 일부 반영될 수 있다.
- 하지만 연구자료의 shadow axis가 운영 parser/feature key로 정확히 컴파일되어 있지 않기 때문에 정보 손실이 크다.

쉬운 예:

- 연구자료: `customer_quality_score=9`, `margin_bridge_score=8`, `revision_score=8`이라 Green.
- 운영 scorer: `customer_quality_score`라는 field는 직접 읽지 않는다. 대신 `customer_preorder_or_allocation`, `minimum_revenue_guarantee`, `eps_revision_pct` 같은 좁은 key가 있어야 점수가 오른다.
- 문서에 "우량 고객향 물량이 잠겼다"는 말이 있어도 parser가 `customer_preorder_or_allocation=True`로 못 바꾸면 운영 점수는 덜 오른다.

## 대표 Green 사례

| archetype | symbol | case | before -> after | MFE90 | MAE90 | 연구 verdict |
| --- | --- | --- | --- | ---: | ---: | --- |
| C27 | 194480 | Cookie Run Kingdom IP | 83 -> 88 | 833.33 | -12.75 | current_profile_correct |
| C11 | 348370 | Enchem US electrolyte orderbook | 82 -> 88 | 374.73 | -5.17 | current_profile_too_late |
| C17 | 298020 | Hyosung TNC spandex | 82 -> 89 | 280.28 | -3.29 | current_profile_correct |
| C07 | 089030 | Techwing HBM test handler | 79 -> 89 | 279.45 | -11.71 | current_profile_too_late |
| C32 | 010130 | Korea Zinc control contest | 88 -> 91 | 261.41 | -1.65 | current_profile_4B_too_late |
| C02 | 267260 | HD Hyundai Electric transformer | 88 -> 91 | 219.93 | -5.24 | current_profile_correct |
| C24 | 310210 | Voronoi trial data | 78 -> 89 | 189.07 | -7.38 | current_profile_too_late |
| C06 | 007660 | Isu Petasys big-tech MLB route | 90 -> 88 | 157.52 | -2.51 | current_profile_correct_entry_but_4B_overlay_needed |
| C10 | 317330 | Duksan Techopia advanced materials | 88 -> 89 | 146.97 | -6.27 | current_profile_reasonable |
| C23 | 000100 | Yuhan Lazcluze FDA approval | 88.5 -> 91 | 76.99 | -2.97 | current_profile_correct |

이 표가 말하는 것:

- 연구자료는 winner를 Green으로 올리는 사례를 실제로 많이 갖고 있다.
- 하지만 다수 Green 사례의 핵심축은 아키타입별 세부축이다.
- 운영 scorer는 지금 그 세부축을 모두 직접 보지 않는다.

## 운영 scorer의 현재 구조

운영 `DeterministicFeatureEngineer`는 최종적으로 7개 공통 component로 압축한다.

| component | max |
| --- | ---: |
| eps_fcf_explosion | 20 |
| earnings_visibility | 20 |
| bottleneck_pricing | 20 |
| market_mispricing | 15 |
| valuation_rerating | 15 |
| capital_allocation | 5 |
| information_confidence | 5 |

아키타입 weight profile이 켜지면 이 component들의 비중만 바뀐다.

예: C06 HBM

| component | C06 max |
| --- | ---: |
| eps_fcf_explosion | 24 |
| earnings_visibility | 21 |
| bottleneck_pricing | 19 |
| market_mispricing | 15 |
| valuation_rerating | 12 |
| capital_allocation | 4 |
| information_confidence | 5 |

하지만 Green gate는 여전히 다음을 요구한다.

- total >= 87
- EPS/FCF >= 17
- visibility >= 15
- bottleneck >= 15
- mispricing >= 10
- valuation >= 10
- revision_score >= 55
- structural_visibility >= 45

즉 연구 weight는 "어느 component를 더 중요하게 볼지"를 바꿀 뿐, 연구자료의 `customer_quality_score`, `margin_bridge_score`, `commercialization_score`를 그대로 운영 score로 넣어주지는 않는다.

## 변환부의 구조적 문제

### 1. 연구축과 운영 field key가 다르다

연구 Green에서 자주 쓰인 축:

- `margin_bridge_score`
- `backlog_visibility_score`
- `customer_quality_score`
- `commercialization_score`
- `order_conversion_score`
- `sell_through_score`
- `fcf_conversion_score`
- `capital_return_execution_score`
- `reserve_quality_score`

운영 scorer가 직접 읽는 예:

- `multi_year_contract`
- `contract_amount_to_prior_sales`
- `backlog_record_high`
- `record_backlog`
- `customer_preorder_or_allocation`
- `eps_revision_pct`
- `op_revision_pct`
- `fcf_revision_pct`
- `target_price_revision_pct`
- `recurring_consumer_demand`
- `export_channel_expansion`
- `hbm_capacity_constraint`
- `advanced_packaging_bottleneck`

연구축이 운영 field로 변환되지 않으면 점수는 낮게 남는다.

### 2. 방향성 revision이 약하다

운영 `_revision_score()`는 numeric revision이나 `estimate_upgrade_mentioned`를 강하게 본다.

하지만 CompanyGuide recent report는 `eps_revision_up_mentioned`를 만들고, 이 field는 현재 `_revision_score()`에서 직접 Green revision 55로 연결되지 않는다.

예:

- 리포트: "추정 EPS 상향"
- 현재 parser: `eps_revision_up_mentioned=True`
- 현재 scorer: `estimate_upgrade_mentioned`가 아니고 numeric `eps_revision_pct`도 없으면 revision_score가 충분히 안 오른다.

### 3. source-backed family가 부족하면 Green이 막힌다

운영 evidence family는 independent consensus/revision을 보수적으로 본다. report-derived proxy는 별도 proxy family로 남는다.

그래서 리포트가 많아도:

- independent consensus `0`
- independent consensus_revision `0`

이면 Green 확정에서 불리하다.

### 4. Green을 쉽게 풀면 false positive도 같이 늘어난다

R13 연구자료가 계속 경고하는 점:

- bridge 없는 price-MFE
- theme spillover
- late spike
- data-quality contamination
- source-proxy-only

이런 행은 Green을 풀면 바로 false positive가 된다.

따라서 해결책은 Green threshold 완화가 아니다. 해결책은 연구축을 source-backed 운영 feature로 정확히 변환하는 것이다.

## 왜 삼성/하닉 현재 점수가 낮은가

### SK하이닉스

연구자료상 하닉은 다음 구간에서 잡혀야 했다.

- 2023-10-27 Stage2-Actionable
- 2024-02-22 Stage2-Actionable
- 2024-04-26 Stage3-Green
- 2024-07-11 Stage4B overlay

그런데 2026-06-12 운영 실행은 다음이 비어 있었다.

- consensus `0`
- consensus_revisions `0`
- selected OP source 없음
- selected FCF source 없음
- selected revision source 없음

그래서 `EPS/FCF=20`이어도 total이 70.86에 머물렀다.

### 삼성전자

연구자료상 삼성전자는 C06에서 대체로 "HBM catch-up headline만으로 Green 주면 안 된다"는 false-positive 쪽이다.

예:

- 2024-03-20: Stage3-Yellow/Weak-Green, named qualification 없음
- 2024-05-24: qualification issue, 4C/watch 성격
- 2024-08-07: HBM3E headline but margin/revision bridge 없음

그래서 삼성전자가 2024년 초중반에 하닉처럼 Green이어야 했다는 결론은 연구자료와 맞지 않는다. 다만 2025~2026 다른 시점에서 HBM qualification/revenue bridge가 충분했는지는 별도 replay가 필요하다.

## 전면 결론

현재 전체 문제는 세 가지다.

1. 연구자료는 충분히 쌓였다.
   - raw MD 기준 Green trigger 338개, Green score simulation 470개가 있다.
   - representative trigger 기준 Green label 381개, weight-calibration usable Green 162개가 있다.

2. 점수표는 누적으로 반영됐지만, 주로 7개 component weight 반영이다.
   - 예: C06은 EPS/FCF 24, visibility 21, bottleneck 19로 바뀐다.
   - 하지만 research shadow axis 자체가 운영 feature로 모두 들어간 것은 아니다.

3. 운영 parser/feature 변환부가 아직 research Green의 세부 evidence를 많이 잃는다.
   - 특히 margin bridge, customer quality, backlog/order conversion, commercialization, FCF conversion, capital-return execution, reserve quality, sell-through 같은 축.

쉬운 예:

- 연구자료는 "이 회사는 좋은 계약 + 마진 + 고객 + revision이 다 맞아서 Green"이라고 썼다.
- 운영 scorer는 "계약 기간 숫자, 계약금액/매출 비율, EPS revision %, FCF growth %, 독립 consensus revision이 있냐?"라고 묻는다.
- 문서에 좋은 말이 있어도 그 key로 변환되지 않으면 점수는 낮다.

## 다음 작업

완전한 해결은 아래 순서가 맞다.

1. C06 historical replay
   - SK하이닉스 2023-10-27, 2024-02-22, 2024-04-26, 2024-07-11
   - 삼성전자 2024-03-20, 2024-05-24, 2024-08-07
2. Green 대표 아키타입 replay set 생성
   - C02 HD현대일렉
   - C07 Techwing
   - C11 Enchem
   - C20 Silicon2
   - C21 KB금융
   - C22 삼성생명/보험 rate-cycle
   - C23 유한양행
   - C28 더존비즈온
3. 연구축 -> 운영 field mapping table 작성
4. parser patch
   - `eps_revision_up_mentioned` -> revision score 연결
   - `sold/booked-out capacity` -> C06 capacity/customer allocation field 연결
   - `margin_bridge` -> OP/OPM/FCF bridge field 연결
   - `customer_quality` -> named customer/order/allocation field 연결
5. false-positive replay
   - Green recall 패치 후 R13 high-MAE / false-positive guard가 유지되는지 검증

투자 권고가 아니라 파이프라인 진단 기록이다.
