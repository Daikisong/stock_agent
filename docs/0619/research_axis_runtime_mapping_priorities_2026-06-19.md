# Research Axis Runtime Mapping Priorities - 2026-06-19

## 목적

이 문서는 다음 패치를 위한 번역표다.

연구자료는 `margin_bridge_score`, `customer_quality_score`, `commercialization_score`처럼 사람이 이해하기 쉬운 축을 쓴다. 운영 scorer는 `op_revision_pct`, `order_backlog_to_sales`, `customer_preorder_or_allocation`처럼 normalized field를 읽는다.

따라서 Green recall을 고치려면 research axis를 runtime field로 바꿔야 한다.

쉬운 예:

- 연구축: `margin_bridge_score=9`
- 운영 field 후보: `opm_expansion_pctp`, `actual_op_yoy_pct`, `fy2_op`, `fcf_growth_pct`
- 패치 목표: 리포트 문장 "HBM mix로 OPM 개선"을 `high_margin_mix_improvement=true`, `opm_expansion_pctp=...` 같은 field로 만들기

## 최우선 Mapping

| priority | research axis | Green score_sim occurrence | 현재 runtime direct key | runtime field 후보 | 주 영향 아키타입 | 문제 |
| ---: | --- | ---: | --- | --- | --- | --- |
| 1 | `margin_bridge_score` | 928 | 없음 | `opm_expansion_pctp`, `opm_expansion`, `actual_op_yoy_pct`, `fy1_op`, `fy2_op`, `fcf_growth_pct`, `high_margin_mix_improvement` | C01, C02, C06, C20, C23, C28 | 연구 Green의 핵심인데 문장형 margin bridge가 numeric/boolean으로 안 바뀌면 visibility/valuation이 낮다. |
| 2 | `revision_score` | 898 | 없음 | `eps_revision_pct`, `op_revision_pct`, `fcf_revision_pct`, `target_price_revision_pct`, `estimate_upgrade_mentioned`, `target_price_upgrade_mentioned`, `earnings_beat_mentioned` | 전 아키타입 | `eps_revision_up_mentioned` 같은 방향성 field가 Green revision으로 충분히 연결되지 않는다. |
| 3 | `customer_quality_score` | 896 | 없음 | `customer_preorder_or_allocation`, `government_customer`, `hyperscaler_customer`, `data_center_contract`, `export_contract`, `take_or_pay` | C02, C03, C06, C07, C08, C20, C28 | "우량 고객향" 문장이 구체 고객/계약 field로 안 바뀌면 Green 확신이 떨어진다. |
| 4 | `backlog_visibility_score` | 896 | 없음 | `order_backlog_to_sales`, `backlog_to_sales`, `rpo_to_sales`, `record_backlog`, `backlog_yoy_pct`, `new_orders_yoy_pct`, `revenue_visibility_contract` | C01, C02, C03, C07, C11, C28 | 수주잔고/ARR/RPO visibility가 숫자로 없으면 visibility component가 약하다. |
| 5 | `contract_score` | 896 | 없음 | `contract_duration_months`, `contract_amount_to_prior_sales`, `multi_year_contract`, `customer_prepayment`, `non_cancellable`, `take_or_pay` | C01, C02, C03, C05, C11, C12 | 장기계약/선수금/취소불가 조건이 없으면 structural shortage가 낮아진다. |
| 6 | `valuation_repricing_score` | 904 | 없음 | `est_per`, `est_pbr`, `pbr_e`, `target_multiple_before`, `target_multiple_after`, `target_multiple_delta`, `market_frame_shift`, `target_multiple_rerating` | C21, C22, C26, C28, C32 | 연구는 rerating을 보지만 운영은 숫자 밸류/멀티플 변화가 없으면 valuation을 덜 준다. |
| 7 | `relative_strength_score` | 920 | 없음 | `price_stage_score`, price bars, underreaction score | 전 아키타입 | 이 축은 조심해야 한다. price-only false positive가 많아 Green 직접 승격축으로 쓰면 위험하다. |
| 8 | `execution_risk_score` | 914 | 없음 | red-team fields, `contract_cancelled_or_delayed`, `delivery_delay`, `cost_overrun`, `revision_slowdown`, `customer_capex_decline` | 전 아키타입 | 연구는 실행리스크를 낮은 점수/높은 점수로 표현하지만 runtime red-team field로 직접 잘 안 들어간다. |
| 9 | `policy_or_regulatory_score` | 886 | 없음 | classifier context only, 별도 scoring field 부족 | C04, C16, C23, C24, C31 | policy/approval headline은 classification에는 쓰이지만, cashflow conversion 없이는 scoring 축이 약하다. |
| 10 | `accounting_trust_risk_score` | 886 | 없음 | `accounting_or_trust_issue`, R13 route | R13, C30, C31, C32 | guardrail은 있으나 연구축을 세밀한 risk penalty로 나누는 field가 부족하다. |

## C06 HBM 전용 Mapping

| research phrase / axis | runtime field 후보 | 현재 문제 | 패치 방향 |
| --- | --- | --- | --- |
| HBM sold-out capacity | `capacity_precommitted`, `hbm_capacity_pre_sold`, `hbm_capacity_constraint` | 문장으로는 읽혀도 `capa_constraint`가 0으로 남을 수 있다. | report/news parser에서 sold-out/booked-out/pre-sold를 capacity precommit으로 구조화 |
| customer allocation | `customer_preorder_or_allocation` | 하닉 replay에서는 일부 반영됐지만 final bottleneck으로 약하게 압축됐다. | allocation + HBM + named/customer context가 있으면 C06 domain/bottleneck에 더 직접 연결 |
| advanced packaging bottleneck | `advanced_packaging_bottleneck` | domain evidence에는 들어가지만 final component가 낮다. | packaging bottleneck이 capacity lock과 같이 있으면 `capa_constraint`도 보강 |
| HBM ASP/mix improvement | `asp_yoy_pct`, `price_increase_pct`, `high_margin_mix_improvement`, `opm_expansion_pctp` | "mix 개선"이 OPM/ASP field로 안 바뀌면 margin bridge가 약하다. | HBM mix, DRAM ASP, premium mix 문장 parser 추가 |
| Q1 surprise / beat | `earnings_beat_mentioned`, `consensus_beat_mentioned`, `actual_op_yoy_pct`, `actual_eps_yoy_pct` | actual은 있어도 independent consensus beat가 약하면 Green confidence가 낮다. | 실적발표/리뷰 문장에서 beat 여부와 숫자를 구조화 |
| multi-quarter revision | `eps_revision_pct`, `op_revision_pct`, `estimate_upgrade_mentioned`, `medium_term_revision_visibility` | 방향성 "EPS 상향"만으로는 부족하다. | `eps_revision_up_mentioned`를 revision score에 연결하거나 numeric proxy를 더 정확히 추출 |

## 산업재/전력/방산 Mapping

| research axis | runtime field 후보 | 주의점 |
| --- | --- | --- |
| order/backlog delivery bridge | `order_backlog_to_sales`, `record_backlog`, `delivery_schedule`, `new_orders_yoy_pct` | 단순 "수주" headline만으로 Green을 열면 C01/C02 false positive가 늘어난다. |
| contract quality | `contract_duration_months`, `contract_amount_to_prior_sales`, `multi_year_contract`, `government_customer`, `export_contract` | 계약명보다 금액/기간/고객/납품 일정이 중요하다. |
| margin/cash bridge | `opm_expansion_pctp`, `actual_op_yoy_pct`, `fcf_growth_pct`, `actual_fcf` | backlog가 있어도 margin/FCF 없으면 Green보다 Stage2/Yellow가 맞다. |
| capacity bottleneck | `lead_time_months`, `lead_time_extended`, `capacity_constraint`, `capa_shortage` | 전력기기 Green은 병목/리드타임이 핵심이다. |

## 소비재 수출 Mapping

| research axis | runtime field 후보 | 주의점 |
| --- | --- | --- |
| global distribution | `export_channel_expansion`, `overseas_channel_expansion`, `platform_distribution_scale`, `brand_channel_expansion` | 채널명이 source-backed일 때만 인정해야 한다. |
| repeat demand / reorder | `recurring_consumer_demand`, `repeat_purchase` | 일회성 히트상품과 반복 reorder를 분리해야 한다. |
| sell-through | 현재 direct field 부족 | C19/C20 false positive 방지를 위해 sell-through/inventory field가 필요하다. |
| margin bridge | `high_margin_mix_improvement`, `opm_expansion_pctp`, `actual_op_yoy_pct` | 수출 증가만 있고 마진이 없으면 Green 과승격 위험이 있다. |

## 금융/보험 Mapping

| research axis | runtime field 후보 | 현재 문제 |
| --- | --- | --- |
| ROE/PBR rerating | `roe`, `est_pbr`, `pbr_e`, actual equity/BPS | valuation에는 일부 들어가지만 C21/C22 전용 수익성/자본환원 축이 부족하다. |
| capital return execution | direct field 부족 | 배당/자사주/소각 실행이 capital_allocation에 충분히 안 들어간다. |
| reserve quality / K-ICS | direct field 부족 | C22 보험 Green의 핵심인데 runtime scoring field가 부족하다. |
| rate cycle | classifier context 중심 | 보험료율/손해율/CSM 흐름을 normalized field로 추가해야 한다. |

## 바이오/헬스케어 Mapping

| research axis | runtime field 후보 | 현재 문제 |
| --- | --- | --- |
| regulatory approval | classifier context only | 승인 자체는 C23/C24 분류에는 쓰이나 Green 점수로는 약하다. |
| commercialization | direct field 부족 | revenue/royalty conversion field가 없으면 approval Green을 못 만든다. |
| partner quality | direct field 부족 | 글로벌 파트너/판매 경로가 customer quality로 잘 안 들어간다. |
| reimbursement/export conversion | direct field 부족 | C25 의료기기 Green의 핵심인데 generic field로 압축된다. |

## 플랫폼/소프트웨어/보안 Mapping

| research axis | runtime field 후보 | 현재 문제 |
| --- | --- | --- |
| ARR / retention | direct field 부족 | C28 Green 핵심축이 generic visibility로만 들어간다. |
| ARPU / monetization | direct field 부족 | C26 platform ad revenue Green이 약하게 반영된다. |
| margin leverage | `opm_expansion_pctp`, `actual_op_yoy_pct` | 영업 레버리지 문장을 숫자로 뽑아야 한다. |
| contract retention | `multi_year_contract`, `revenue_visibility_contract` 일부 | SaaS retention과 산업재 계약은 성격이 다르다. 전용 field가 필요하다. |

## 보호형/반례 아키타입 Mapping

| research axis | runtime field 후보 | 주의점 |
| --- | --- | --- |
| high MAE guardrail | `high_mae_risk`, R13 guard | 미래 MAE를 runtime에 쓰면 안 된다. 과거 연구는 guard 설계 근거로만 사용한다. |
| PF/legal break | `hard_4c_thesis_break_score`, `accounting_or_trust_issue` 등 | C30은 positive보다 4C/Watch 보호가 중요하다. |
| price-only blowoff | `price_only_blowoff_score`, `theme_overheat_score` | relative strength를 Green으로 쓰기 전에 price-only false positive를 막아야 한다. |
| policy headline | classifier context, C31 guard | 정책 수혜 headline만으로 positive stage를 열면 안 된다. company-specific cash bridge 필요. |

## 패치 순서 제안

### 1. C06부터 고친다

이유:

- 하닉은 사용자가 지적한 명확한 winner다.
- 현재 as-of replay 증거가 있다.
- 실패 원인이 `bottleneck_pricing` 변환으로 좁혀졌다.

최소 성공조건:

- SK하이닉스 2024-04-26 fixture에서 Stage3-Green 또는 최소 Green gate 직전까지 상승.
- 삼성전자 2024 catch-up/headline false-positive는 Green으로 과승격되지 않음.

### 2. 공통 margin/revision/customer/backlog mapping을 고친다

이유:

- Green score_sim 상위축 대부분이 이 네 축이다.
- C06만이 아니라 C01/C02/C20/C23/C28에도 공통으로 먹힌다.

최소 성공조건:

- `margin_bridge_score`에 해당하는 source-backed 문장이 runtime field로 구조화된다.
- `eps_revision_up_mentioned`나 방향성 revision이 Green revision score에 더 일관되게 반영된다.
- 단, source proxy 또는 snippet-only는 그대로 보수적으로 처리한다.

### 3. 금융/보험/바이오/소프트웨어 전용 field를 별도 설계한다

이유:

- 현재 sector profile이 이 아키타입들을 충분히 세분화하지 않는다.
- Green 연구 사례는 많지만 runtime field가 generic이다.

최소 성공조건:

- C21/C22: ROE/PBR + capital return/reserve quality field
- C23/C25: approval + commercialization/reimbursement conversion field
- C28: ARR/retention/margin leverage field

### 4. R13/C30/C31 false-positive replay를 반드시 같이 돌린다

이유:

- Green recall만 올리면 반례가 같이 뚫린다.
- 전체 장부에서 false positive가 3,559개, bad Stage2가 2,438개다.

최소 성공조건:

- 하닉/C06 Green recall 개선
- policy/PF/price-only false positive 증가 없음

## 결론

다음 구현은 "점수 threshold 낮추기"가 아니다.

해야 할 일은:

1. 연구축을 normalized field로 번역한다.
2. 번역된 field가 7개 component에 충분히 반영되게 한다.
3. Green 대표 케이스와 false-positive 대표 케이스를 동시에 replay한다.

이 순서로 가지 않으면 하닉은 잡아도 다른 아키타입에서 false positive가 터질 가능성이 높다.
