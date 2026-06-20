# Production Replay Failure Inventory and Requirements - 2026-06-19

## 결론

현재 문제는 "하닉/HBM 점수 하나가 이상하다"가 아니다.

최신 운영 replay와 누적 연구 장부를 같이 보면 다음 네 층이 동시에 막힌다.

1. 후보 funnel이 일부 구조 변화 이벤트를 초기에 못 올린다.
2. 후보가 올라와도 연구 문장이 normalized runtime field로 충분히 번역되지 않는다.
3. 36개 아키타입 연구축이 9개 sector profile과 7개 component로 너무 거칠게 압축된다.
4. Green gate가 AND 조건이라 total/bottleneck/visibility 중 하나만 비어도 Green이 닫힌다.

쉬운 예:

- 하닉: 연구 장부에는 Green 근거가 있는데, runtime에서는 `capa_constraint=0`, `contract_quality=0`, `backlog_rpo_visibility=15`라 bottleneck gate가 닫힌다.
- 삼성: 강한 OP/FCF 개선이 있었지만 cheap scan에서는 `turnaround` rule에 덜 잡혀 후보 승격부터 약했다.
- 보험/바이오/플랫폼: 연구 장부에는 CSM, K-ICS, approval-to-revenue, ARR/retention 같은 Green 축이 있지만, 전용 runtime profile이 부족하다.

따라서 다음 작업은 HBM 특수 가산이 아니라 전역 evidence translation과 archetype adapter 보강이어야 한다.

## 현재 운영 replay 상태

기준 파일:

- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/score_components_by_candidate.csv`
- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/stage_gate_matrix.csv`
- `output/0619_asof_stage_promotion_benchmark_current_2023_2026/feature_input_coverage.csv`

주의: 이 문서의 수치는 `parser_target_revision_date_leak_fix_2026-06-19.md` 수정 이후 재생성한 값이다. 수정 전에는 목표가 상향률에 날짜가 들어가면서 hard audit 45개가 추가로 잡혔다.

운영 replay 후보 120개 stage 분포:

| stage | count |
| --- | ---: |
| Stage0 | 7 |
| Stage1 | 67 |
| Stage2 | 34 |
| Stage3-Yellow | 12 |
| Stage3-Green | 0 |

sector profile별 stage 분포:

| sector_profile | Stage0 | Stage1 | Stage2 | Stage3-Yellow | Stage3-Green |
| --- | ---: | ---: | ---: | ---: | ---: |
| DEFENSE | 0 | 12 | 0 | 0 | 0 |
| GENERIC | 7 | 22 | 0 | 0 | 0 |
| K_BEAUTY_EXPORT | 0 | 11 | 0 | 0 | 0 |
| MEMORY_HBM | 0 | 7 | 1 | 12 | 0 |
| POWER_EQUIPMENT | 0 | 15 | 33 | 0 | 0 |

이 표의 의미:

- 현재 운영 후보 replay에서 Green은 하나도 열리지 않았다.
- HBM만 Green이 안 열린 것이 아니라 POWER, DEFENSE, K-beauty, GENERIC 모두 Green이 닫혔다.
- 다만 이 replay는 운영 funnel이 끌어온 120개 후보만 본 것이므로, 36개 전체 아키타입의 runtime 상태를 모두 증명하지는 않는다. 이 자체가 다음 replay coverage 과제다.

## Gate 실패가 어디에 몰렸나

전체 후보 120개 기준:

| failed gate | count |
| --- | ---: |
| `failed_stage3_total_score` | 120 |
| `failed_stage3_bottleneck` | 120 |
| `failed_stage3_visibility` | 87 |
| `failed_stage2_total_score` | 67 |
| `failed_stage3_valuation` | 67 |
| `failed_stage2_information_confidence` | 63 |
| `failed_sector_bottleneck` | 56 |
| `failed_stage3_market_mispricing` | 56 |
| `failed_stage2_eps_fcf` | 45 |
| `failed_stage3_eps_fcf` | 45 |
| `failed_green_cross_evidence` | 40 |
| `failed_stage3_contract_quality` | 37 |
| `failed_domain_specific_evidence` | 33 |
| `failed_sector_visibility` | 33 |
| `failed_structural_visibility_quality` | 33 |
| `failed_stage3_revision` | 22 |
| `failed_stage3_red_team` | 0 |

가장 중요한 두 줄:

- 120개 전부 `failed_stage3_total_score`
- 120개 전부 `failed_stage3_bottleneck`

즉 Green이 닫힌 직접 위치는 total과 bottleneck이다.

하지만 이걸 "total 기준을 낮추자"로 풀면 안 된다. bottleneck이 낮은 이유가 아키타입마다 다르기 때문이다.

쉬운 예:

- HBM bottleneck: CAPA lock/customer allocation/sold-out 물량 번역 부족
- 전력기기 bottleneck: lead time/backlog/margin delivery bridge 번역 부족
- 보험 bottleneck: 사실 bottleneck이 아니라 reserve/capital adequacy/CSM visibility를 다른 component로 번역해야 함
- 바이오 bottleneck: approval 자체보다 approval-to-revenue/royalty bridge가 필요

## Sector별 평균 점수

| sector_profile | n | avg score | EPS/FCF | visibility | bottleneck | mispricing | valuation | revision | contract | backlog | capa | structural visibility | sector bottleneck | domain evidence |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DEFENSE | 12 | 35.65 | 0.00 | 12.11 | 2.80 | 9.22 | 8.45 | 83.33 | 62.00 | 70.00 | 0.00 | 67.95 | 14.65 | 40.00 |
| GENERIC | 29 | 28.40 | 7.59 | 5.55 | 2.37 | 4.14 | 3.59 | 37.93 | 13.28 | 0.00 | 0.00 | 19.72 | 11.08 | 5.31 |
| K_BEAUTY_EXPORT | 11 | 50.09 | 9.00 | 11.66 | 9.36 | 9.93 | 8.73 | 100.00 | 35.00 | 0.00 | 0.00 | 74.76 | 63.38 | 96.00 |
| MEMORY_HBM | 20 | 74.90 | 20.00 | 14.78 | 10.82 | 12.79 | 12.31 | 99.00 | 0.00 | 14.25 | 0.00 | 68.86 | 49.56 | 79.00 |
| POWER_EQUIPMENT | 48 | 60.59 | 17.88 | 11.81 | 7.90 | 11.12 | 10.31 | 90.14 | 21.20 | 51.56 | 32.43 | 48.64 | 37.49 | 37.12 |

해석:

- MEMORY_HBM은 EPS/FCF, revision, domain evidence가 높다. 그런데 contract/capa/backlog가 약해 bottleneck이 평균 10.82에 머문다.
- POWER_EQUIPMENT는 EPS/FCF와 backlog 일부는 높지만, bottleneck 평균 8.05라 Green bottleneck 기준에 멀다.
- DEFENSE는 contract/backlog는 높은데 EPS/FCF가 0이고 bottleneck이 2.80이다. 납품/마진/실적 전환 field가 비어 있다.
- K_BEAUTY_EXPORT는 revision/domain/structural visibility가 높은데 EPS/FCF와 cross evidence가 약하다.
- GENERIC은 전반적으로 도메인 신호가 거의 소실된다.

쉬운 예:

- 하닉은 "시험 점수는 높은데 필수 과목 하나가 0점"이다.
- 방산은 "계약서는 있는데 실적 전환 과목이 0점"이다.
- 금융/보험/바이오는 이 표에 제대로 등장하지도 않는다. 운영 benchmark 후보 coverage 자체가 부족하기 때문이다.

## Sector별 실패 게이트

| sector_profile | n | total fail | visibility fail | bottleneck fail | revision fail | contract fail | structural visibility fail | sector bottleneck fail | green cross evidence fail | domain evidence fail |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DEFENSE | 12 | 12/12 | 12/12 | 12/12 | 0/12 | 0/12 | 0/12 | 12/12 | 0/12 | 0/12 |
| GENERIC | 29 | 29/29 | 29/29 | 29/29 | 18/29 | 0/29 | 18/29 | 29/29 | 18/29 | 29/29 |
| K_BEAUTY_EXPORT | 11 | 11/11 | 11/11 | 11/11 | 0/11 | 0/11 | 0/11 | 0/11 | 11/11 | 0/11 |
| MEMORY_HBM | 20 | 20/20 | 9/20 | 20/20 | 0/20 | 0/20 | 0/20 | 0/20 | 7/20 | 0/20 |
| POWER_EQUIPMENT | 48 | 48/48 | 26/48 | 48/48 | 4/48 | 37/48 | 15/48 | 15/48 | 4/48 | 4/48 |

핵심:

- HBM은 revision/domain/sector visibility는 대부분 통과한다. 반복 실패는 bottleneck/total이다.
- POWER는 contract/visibility/revision도 꽤 같이 막힌다.
- DEFENSE는 contract는 통과하지만 EPS/FCF와 bottleneck/revision이 막힌다.
- GENERIC은 domain evidence 자체가 거의 안 잡힌다.
- K_BEAUTY는 cross-evidence family가 전부 막힌다.

## 누적 연구 장부에서 보이는 반대 증거

기준 파일:

- `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl`
- `data/e2r/calibration/v12/v12_raw_shadow_weight_rows.jsonl`

대표 trigger rows:

| metric | value |
| --- | ---: |
| total rows | 12,471 |
| Stage3-Green rows | 381 |
| strict usable Green rows | 162 |
| current_profile_false_positive | 2,297 |
| current_profile_too_late | 473 |
| current_profile_missed_structural | 213 |

Green row의 current profile verdict:

| verdict | count |
| --- | ---: |
| `current_profile_too_late` | 130 |
| `current_profile_false_positive` | 90 |
| `current_profile_correct` | 82 |
| missing verdict | 37 |
| `current_profile_too_early` | 6 |
| `current_profile_4B_too_late` | 4 |

해석:

- 연구 장부에는 Green 사례가 실제로 있다.
- 하지만 그 Green 사례 자체도 "너무 늦게 잡음", "false-positive 위험", "정확히 맞음"이 섞여 있다.
- 따라서 단순 recall 보정은 위험하다. positive와 false-positive를 한 쌍으로 검증해야 한다.

쉬운 예:

- 하닉 Green을 살리는 패치를 만들 때 삼성 catch-up headline도 같이 Green이 되면 실패다.
- 보험 Green을 살리는 패치를 만들 때 reserve quality 없는 금리 수혜주도 같이 Green이 되면 실패다.
- 바이오 approval Green을 살리는 패치를 만들 때 매출/royalty 없는 승인 뉴스도 같이 Green이 되면 실패다.

## Shadow axis가 말하는 것

`v12_raw_shadow_weight_rows.jsonl`:

| metric | value |
| --- | ---: |
| shadow rows | 3,741 |
| production_default_scoring_changed=true | 0 |

상위 shadow axis:

| axis | count |
| --- | ---: |
| `stage2_required_bridge` | 191 |
| `local_4b_watch_guard` | 182 |
| `high_MAE_guardrail` | 129 |
| `full_4b_requires_non_price_evidence` | 11 |
| `hard_4c_thesis_break_routes_to_4c` | 10 |
| `share_count_drift_independent_weight_reduction` | 8 |
| `C08_socket_customer_quality_bridge_required` | 6 |
| `C19_inventory_margin_absence_guard` | 6 |
| `C11_orderbook_false_positive_guardrail` | 5 |
| `c10_order_conversion_freshness_ladder` | 5 |

이건 연구자료가 계속 같은 말을 했다는 뜻이다.

- Stage2/Green은 non-price bridge가 필요하다.
- 4B watch와 full exit를 구분해야 한다.
- high-MAE 반례를 guard해야 한다.
- share count/accounting/source 품질을 따로 봐야 한다.
- order/customer/channel/margin/cash bridge가 필요하다.

하지만 이 axis들은 대부분 production scoring field로 직접 승격되지 않았다.

## 실제 결손 모델

현재까지 확인한 결손은 6개다.

| layer | 결손 | 예시 | 필요한 수정 |
| --- | --- | --- | --- |
| candidate funnel | 구조 변화가 cheap scan에서 빠짐 | 삼성 OP/FCF 급증이 turnaround가 아니라 약하게 처리 | 아키타입별 구조 변화 signal을 후보 승격에 반영 |
| parser | 문장이 field로 안 바뀜 | `HBM CAPA 제약`이 `hbm_capacity_constraint`로 안 들어감 | domain primitive parser 확장 |
| evidence bridge | 연구축이 source-backed field로 번역 안 됨 | `customer_quality_score`, `margin_bridge_score`가 직접 runtime field가 아님 | EvidenceBridgeSpec |
| feature adapter | 36개 archetype을 9개 profile로 압축 | C21/C22/C23/C28 generic 처리 | archetype-specific adapters |
| evidence family | report proxy와 independent source 사이 간극 | consensus/revision/news missing 반복 | source-backed directional revision 인정 규칙 |
| stage explanation | 실패 이유가 너무 추상적 | total/bottleneck fail만 표시 | field-level score loss report |

## 구현 요구사항

### Requirement 1. Green target fixture matrix

각 priority archetype은 positive와 false-positive를 같이 둔다.

| group | positive fixture | guard fixture |
| --- | --- | --- |
| C06 HBM | SK하이닉스 sold-out capacity/revision | 삼성 generic HBM catch-up without direct customer/qualification |
| C01/C02 power | backlog + margin + lead-time winner | cable/theme/order headline without margin/FCF |
| C03 defense | sovereign backlog + delivery + margin | contract headline without delivery/margin conversion |
| C20 consumer export | reorder/sell-through/margin bridge | channel headline or event premium only |
| C21 finance | ROE/PBR + executed capital return | value-up headline without execution |
| C22 insurance | CSM/K-ICS/reserve + payout | rate-cycle headline without reserve quality |
| C23/C25 bio/medical | approval/reimbursement to revenue | approval/device theme without commercialization |
| C28 software/security | ARR/RPO/retention + margin | contract headline without renewal/retention |
| C30/C31/C32 guard | cash route/tender floor correctly classified | policy/governance/PF headline overpromotion |

### Requirement 2. EvidenceBridgeSpec

Research axis를 runtime field로 바꾸는 명세를 둔다.

| research axis | runtime primitive examples |
| --- | --- |
| `margin_bridge_score` | OPM expansion, gross margin mix, FCF growth, cash conversion |
| `customer_quality_score` | named customer, customer tier, repeat order, allocation, renewal |
| `backlog_visibility_score` | order backlog/sales, RPO/sales, delivery schedule, channel reorder |
| `contract_score` | duration, amount/sales, prepayment, cancellation terms |
| `policy_or_regulatory_score` | policy-to-company revenue, subsidy capture, legal enforceability |
| `reserve_quality_score` | CSM, K-ICS, loss ratio, reserve adequacy |
| `commercialization_score` | approval-to-sales, partner economics, royalty/reimbursement |
| `retention_score` | ARR, NRR, renewal, churn, RPO conversion |
| `accounting_trust_risk_score` | restatement, auditor, share count drift, source conflict |

주의:

- 이건 검색어 하드코딩이 아니다.
- LLM이 찾아온 문서와 parser가 뽑은 source-backed evidence를 deterministic score field로 변환하는 규칙이다.

### Requirement 3. Score loss report

Green 실패 시 다음 형태의 설명을 출력해야 한다.

```text
research_axis=HBM_capacity_lock
expected_runtime_fields=hbm_capacity_pre_sold,hbm_capacity_constraint,customer_preorder_or_allocation
observed_runtime_fields=customer_preorder_or_allocation
lost_components=capa_constraint=0,backlog_rpo_visibility=15,bottleneck_pricing=11.63/20
failed_gate=stage3_bottleneck,total
```

다른 예:

```text
research_axis=insurance_reserve_capital_quality
expected_runtime_fields=CSM_growth,K-ICS,reserve_quality,loss_ratio,capital_return_execution
observed_runtime_fields=capital_allocation_partial,valuation_rerating
lost_components=earnings_visibility_partial,information_confidence_low
failed_gate=total,visibility
```

### Requirement 4. Replay coverage expansion

현재 운영 replay는 120개 후보와 5개 sector profile 중심이다.

다음은 반드시 별도 fixture replay가 필요하다.

- C21 금융
- C22 보험
- C23/C24/C25 바이오/의료
- C26/C27/C28 플랫폼/콘텐츠/SW/security
- C29 mobility
- C30 PF/건설
- C31 정책
- C32 지배구조

이유:

- 이 아키타입들은 연구 장부에는 Green/반례가 많다.
- 하지만 현재 benchmark replay에는 충분히 등장하지 않는다.
- 등장하지 않으면 "runtime이 고쳤다"를 증명할 수 없다.

## 한 줄 진단

지금까지 연구는 아키타입별 Green/반례를 상당히 쌓았다.  
하지만 운영 파이프라인은 그 연구축을 normalized field, evidence family, feature adapter, stage explanation으로 충분히 승격하지 못했다.

그래서 하닉처럼 연구 Green 근거가 있어도 Yellow에 머물고, 삼성처럼 후보 전 단계에서 빠지는 일이 생긴다. 같은 구조가 다른 아키타입에도 남아 있다.
