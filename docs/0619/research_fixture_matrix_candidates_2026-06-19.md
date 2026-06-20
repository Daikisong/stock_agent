# Research Fixture Matrix Candidates - 2026-06-19

## 결론

다음 구현은 HBM 전용 패치가 아니라 positive/guard fixture 쌍부터 고정해야 한다.

이 문서는 `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl`에서 실제 연구 row를 뽑아, 어떤 케이스를 살리고 어떤 케이스를 막아야 하는지 정리한 후보 목록이다.

쉬운 예:

- 하닉 positive만 넣으면 HBM 점수 과적합이 된다.
- 하닉 positive와 삼성 HBM catch-up guard를 같이 넣어야 한다.
- 같은 방식으로 금융은 KB/JB금융 positive와 카카오뱅크 value-up beta guard를 같이 둔다.

## 선택 기준

positive 후보:

- 가능하면 `trigger_type=Stage3-Green`
- 가능하면 `usable_for_weight_calibration=true`
- `MFE_90D`가 의미 있고 `MAE_90D`가 과도하지 않은 row
- source proxy가 아닌 row 우선

guard 후보:

- `current_profile_false_positive` 또는 verdict에 false-positive가 있는 row
- price-only, theme-only, source-proxy, high-MAE, late-entry, qualification failure row
- positive를 살리는 패치가 같이 뚫으면 안 되는 row

## 핵심 Fixture Matrix

| group | positive candidate | guard candidate | bridge requirement |
| --- | --- | --- | --- |
| C06 HBM memory | SK하이닉스 `000660`, 2024-03-19, Stage3-Green, MFE90 55.12, MAE90 -3.81 | 삼성전자 `005930`, 2024-03-20, Stage3-Yellow/false-positive, MFE90 15.21, MAE90 -4.42 | HBM customer qualification, booked/sold-out capacity, allocation/share, revision, FCF bridge가 있어야 Green |
| C06 HBM hard guard | SK하이닉스 `000660`, 2024-04-25, Stage3-Green, MFE90 45.66, MAE90 -11.14 | 삼성전자 `005930`, 2024-05-24, Stage4C/qualification break, MFE90 16.73, MAE90 -21.08 | HBM optimism과 qualification failure를 분리해야 함 |
| C01 backlog/margin | 현대로템 `064350`, 2025-02-26, Stage3-Green, MFE90 157.59, MAE90 -8.64 | 대원전선 `006340`, 2024-06-27, Stage2 false-positive, MFE90 9.77, MAE90 -41.38 | order/backlog headline이 아니라 backlog-to-margin-to-cash bridge 필요 |
| C02 power grid | HD현대일렉트릭 `267260`, 2024-02-16, Stage3-Green, MFE90 179.12, MAE90 -0.52 | 그리드위즈 `453450`, 2024-06-14, Stage4B false-positive, MFE90 66.06, MAE90 -61.09 | transformer/grid backlog, lead time, margin, datacenter capex bridge 필요 |
| C03 defense | 한화에어로스페이스 `012450`, 2024-02-14, Stage3-Green, MFE90 74.98, MAE90 -8.34 | 퍼스텍 `010820`, 2022-02-24, Stage2 false-positive, MFE90 8.99, MAE90 -35.00 | sovereign export backlog, delivery schedule, margin/cash bridge 필요 |
| C08 semi test/socket | 네오셈 `092870`, 2024-02-19, Stage3-Green, MFE90 73.00, MAE90 -17.00 | ISC `095340`, 2024-03-29, Stage4B false-positive, MFE90 4.69, MAE90 -58.06 | customer qualification, repeat order, realized revision, margin bridge 필요 |
| C20 beauty/food | 삼양식품 `003230`, 2024-05-17, Stage3-Green, MFE90 60.81, MAE90 0.00 | 아모레퍼시픽 `090430`, 2023-02-10, Stage3-Green false-positive, MFE90 1.83, MAE90 -36.47 | global demand, sell-through, reorder, margin/revision bridge 필요 |
| C20 distribution | 실리콘투 `257720`, 2024-05-10, Stage3-Green, MFE90 106.50, MAE90 -17.90 | 토니모리 `214420`, 2024-08-16, Stage2 false-positive, MFE90 11.86, MAE90 -42.20 | export platform leverage와 roadshop/channel rebound를 분리해야 함 |
| C21 financial | JB금융지주 `175330`, 2024-09-24/25, Stage3-Green, MFE90 31.75~36.39, MAE90 -4.76~-1.40 | 카카오뱅크 `323410`, 2024-02-26, Stage2 false-positive, MFE90 1.66, MAE90 -33.50 | low-PBR/ROE + executed capital return 필요, sector beta만으로는 금지 |
| C22 insurance | 삼성화재 `000810`, 2024-11-18, Stage3-Green, MFE90 28.90, MAE90 -8.80 | 미래에셋생명 `085620`, 2024-02-01, Stage2 false-positive, MFE90 12.65, MAE90 -23.66 | CSM, K-ICS, reserve quality, loss ratio, payout execution 필요 |
| C23 bio approval | 유한양행 `000100`, 2024-08-20/21, Stage3-Green, MFE90 76.99~77.55, MAE90 -2.97~-2.66 | HLB `028300`, 2024-04-25/30, Stage3-Green false-positive, MFE90 2.79~4.29, MAE90 -59 내외 | approval-to-commercialization/royalty route 필요, pre-PDUFA 기대감 금지 |
| C25 medical device | 비올 `335890`, 2023-01-13, Stage3-Green, MFE90 57.94, MAE90 -4.46 | JLK `322510`, 2023-08-10, Stage3-Green false-positive, MFE90 8.77, MAE90 -54.74 | export traction, consumable/reorder visibility, reimbursement-to-revenue bridge 필요 |
| C28 software/security | 이엠로 `058970`, 2023-03-15, Stage3-Green, MFE90 223.84, MAE90 0.00 | 안랩 `053800`, 2022-03-23, Stage2 false-positive, MFE90 24.29, MAE90 -53.92 | SaaS/contract retention, recurring revenue, partner economics 필요; political theme 금지 |
| C30 PF/construction | strict positive 부족, 현대건설 `000720` 2021-05-27은 late Green comparison only | 코오롱글로벌 `003070`, 2024-06-20, Stage4B false-positive, MFE90 2.35, MAE90 -46.00 | PF repair, balance-sheet cash bridge, legal/quality guard가 먼저 필요 |
| C31 policy | KB금융 `105560`, 2024-04-26, Stage3-Green, MFE90 29.70, MAE90 -5.90, source-proxy | 심텍 `222800`, 2024-05-23, Stage2 false-positive, MFE90 10.37, MAE90 -49.93 | policy headline이 아니라 company cash route, capital return execution 필요 |
| C32 governance | 고려아연 `010130`, 2024-09-13, Stage3-Green, MFE90 261.41, MAE90 -1.65 | 영풍정밀 `036560`, 2024-10-11, Stage2 false-positive, MFE90 11.99, MAE90 -62.98 | tender/control premium은 finite floor와 ongoing rerating을 분리해야 함 |
| R13 red-team | 유한양행 `000100`, 2024-08-20, Stage3-Green, MFE90 77.55, MAE90 -2.66 | 신라젠 `215600`, 2019-08-01, Stage3-Green false-positive, MFE90 2.02, MAE90 -82.45 | binary/event risk, accounting/source trust, high-MAE guard 필요 |

## C06 세부 해석

### 살려야 할 row

`C06-127-002`

- symbol: `000660`
- entry: 2024-03-19
- label: Stage3-Green
- MFE90: 55.12
- MAE90: -3.81
- evidence: HBM3E mass production, Nvidia shipment, fully booked 2024 HBM capacity
- source: `docs/round/e2r_stock_web_v12_residual_round_R2_loop_127_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md:342`

필요한 runtime field:

- `hbm_capacity_pre_sold`
- `hbm_capacity_constraint`
- `customer_preorder_or_allocation`
- `medium_term_revision_visibility`
- `actual_fcf_yoy_pct` 또는 `fcf_quality_score`

### 막아야 할 row

`R2L12_C06_SAMSUNG_20240320_HBM_OPTIMISM_FALSE_GREEN`

- symbol: `005930`
- entry: 2024-03-20
- label: Stage3-Yellow / false-positive
- MFE90: 15.21
- MAE90: -4.42
- evidence: HBM catch-up candidate였지만 named customer qualification과 high-volume AI GPU supply가 미확인
- source: `docs/round/achieve/achieve_v12/e2r_stock_web_v12_residual_round_R2_loop_12_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md:396`

추가 hard guard:

`R2L12_C06_SAMSUNG_20240524_QUALIFICATION_BREAK_4C`

- symbol: `005930`
- entry: 2024-05-24
- label: Stage4C
- evidence: Samsung HBM chips had not passed Nvidia tests due to heat/power issues; customer optimization ongoing
- source: `docs/round/achieve/achieve_v12/e2r_stock_web_v12_residual_round_R2_loop_12_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md:397`

핵심:

- 하닉 Green을 살릴 때 삼성 2024-03/05/07/08 partial qualification row가 같이 Green으로 올라오면 실패다.
- C06 bridge는 `HBM mentioned`가 아니라 `qualification + capacity lock + allocation + revision + cash conversion`이어야 한다.

## 비-HBM에서 같은 패턴

### C21 금융

positive:

- JB금융지주 `175330`, 2024-09-24/25, Stage3-Green
- 핵심: high ROE, low PBR, value-up/capital-return execution

guard:

- 카카오뱅크 `323410`, 2024-02-26, Stage2 false-positive
- 핵심: financial sector/value-up beta는 있었지만 low-PBR capital-return mechanics가 약함

필요 field:

- `roe`
- `pbr`
- `capital_return_execution`
- `buyback_cancellation`
- `dividend_visibility`
- `credit_cost_quality`

### C22 보험

positive:

- 삼성화재 `000810`, 2024-11-18, Stage3-Green
- evidence: underwriting quality, CSM/K-ICS visibility, capital return confirmation

guard:

- 미래에셋생명 `085620`, 2024-02-01, Stage2 false-positive
- evidence: insurance theme/price beta without durable CSM/reserve-quality follow-through

필요 field:

- `csm_growth`
- `k_ics_ratio`
- `reserve_quality`
- `loss_ratio_quality`
- `payout_execution`

### C23 바이오

positive:

- 유한양행 `000100`, 2024-08-20/21, Stage3-Green
- evidence: FDA approval of Rybrevant/Lazcluze combination; direct commercialization/economics route

guard:

- HLB `028300`, 2024-04-25/30, false Green
- evidence: pre-PDUFA optionality and relative strength before final approval/commercialization evidence

필요 field:

- `regulatory_approval_confirmed`
- `approval_to_revenue_bridge`
- `partner_economics`
- `royalty_route`
- `binary_event_unresolved`

### C28 software/security

positive:

- 이엠로 `058970`, 2023-03-15, Stage3-Green
- evidence: SCM SaaS contract/partner rerating

guard:

- 안랩 `053800`, 2022-03-23, political/theme false-positive

필요 field:

- `arr_growth`
- `rpo_to_sales`
- `retention_or_renewal`
- `partner_contract_quality`
- `recurring_margin_leverage`
- `political_theme_risk`

## 구현상 주의

이 fixture matrix를 점수 기준 완화에 쓰면 안 된다.

해야 할 일:

1. positive row가 요구하는 research axis를 runtime primitive로 번역한다.
2. guard row가 같이 올라오지 않도록 hard guard primitive도 같이 둔다.
3. replay에서 positive/guard 쌍을 동시에 검증한다.

나쁜 예:

- C06 HBM이면 `bottleneck_pricing +5`
- C23 approval이면 `information_confidence +10`
- C21 value-up이면 `capital_allocation +5`

좋은 예:

- C06: HBM capacity lock + named customer qualification + revision + FCF bridge가 모두 있을 때만 Green 가능
- C23: approval confirmed + partner economics + royalty/revenue route가 있어야 Green 가능
- C21: low-PBR + ROE + executed buyback/cancellation/dividend route가 있어야 Green 가능

## 다음 작업

1. 이 후보 matrix를 테스트 fixture로 옮긴다.
2. 각 row의 expected runtime fields를 `EvidenceBridgeSpec`에 매핑한다.
3. current replay에서 positive row의 observed runtime fields와 missing fields를 출력한다.
4. guard row가 Green으로 뚫리지 않는지 같이 확인한다.
