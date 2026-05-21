순서상 이번은 **R11 Loop 8 — 정책·지정학·재난·이벤트 가격경로 검증 라운드**다.

이번 R11은 구조적으로 **Stage 3-Green을 찾는 라운드가 아니라, event premium을 Stage 3로 잘못 올리지 않게 막는 라운드**다. 원시 수정주가 일봉 OHLC를 안정적으로 직접 추출하지 못한 종목은 숫자를 만들지 않았고, Reuters / WSJ / AP / FT / arXiv에 남은 **가격 anchor, 이벤트 수익률, 계약·정책·시장충격 수치**로 계산 가능한 값만 계산했다.

```text
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
r11_default_stage3_bias = very_conservative
```

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
large_sector = POLICY_GEOPOLITICAL_EVENT
round = R11 Loop 8 / price-path validation
```

R11의 핵심은 “정책이 크다”, “지정학 이벤트가 세다”, “자원 발견 가능성이 있다”가 아니라, **그 이벤트가 실제 계약·예산·financing·발주·매출·EPS/FCF로 승격됐는가**다.

---

# 2. 대상 canonical archetype

```text
DOMESTIC_RESOURCE_DISCOVERY_EVENT
ENERGY_SECURITY_POLICY_EVENT
NUCLEAR_POLICY_TO_CONTRACT
SMR_AI_POWER_POLICY_EVENT
GEOPOLITICAL_SHIPBUILDING_POLICY
US_SHIPBUILDING_REBUILD_POLICY
EVENT_DISEASE_PEST_DEMAND
SPECULATIVE_SCIENCE_THEME
MARKET_STRUCTURE_SHORT_SELLING_POLICY
POLICY_MARKET_SHOCK_EVENT
PRICE_ONLY_RALLY
EVENT_PREMIUM
THESIS_BREAK_4C
```

이번 R11의 핵심 질문은 이거다.

```text
뉴스가 큰가?
아니면 뉴스가 계약·예산·수익으로 내려왔는가?
```

---

# 3. deep sub-archetype

```text
자원 발견 / 에너지 안보:
- East Sea oil and gas
- Korea Gas
- exploration approval
- reserve estimate
- commerciality unknown
- drilling cost
- resource estimate vs revenue conversion

원전 / SMR / AI 전력:
- Czech nuclear preferred bidder
- Doosan Enerbility
- KHNP
- X-energy / AWS / Fermi America
- preferred bidder vs final contract
- court/legal delay
- equipment backlog
- SMR MOU vs funded order

미국 조선정책:
- MASGA
- HD Hyundai Heavy / HD Hyundai Mipo
- U.S.-Korea shipbuilding cooperation
- MOU / merger / record high
- funded order vs policy premium

질병·수급 이벤트:
- Brazil bird flu
- South Korea chicken import restriction
- Harim / Maniker poultry basket
- import ban / restriction easing
- one-off disease demand

과학 테마:
- LK-99
- room-temperature superconductor claim
- replication failure
- speculative science rally
- theme collapse

시장구조 / 정치 shock:
- martial law shock
- short-selling resumption
- MSCI market accessibility
- market-level overlay
```

---

# 4. 국장 신규 후보 case

## Case A — 한국가스공사 `price_moved_without_evidence / 자원발견 event premium`

```text
symbol = 036460
case_type = event_premium / price_moved_without_evidence
archetype = DOMESTIC_RESOURCE_DISCOVERY_EVENT / ENERGY_SECURITY_POLICY_EVENT
```

### evidence

2024년 6월 3일 정부의 동해 석유·가스 시추 승인 발표 이후 한국가스공사 주가는 장중 최대 30% 올라 38,700원을 기록했다. WSJ는 최대 140억 배럴의 석유·가스 가능성이 언급됐지만, 경제성은 아직 결정되지 않았고 최소 5차례 시추가 필요하며, 1회 시추 비용은 약 1,000억 원이라고 보도했다. 이건 명확히 **Stage 1 resource-discovery event**이지 Stage 3가 아니다. ([월스트리트저널][1])

### stage date

```text
Stage 1:
2024-06-03
- 동해 석유·가스 탐사 승인
- 최대 140억 배럴 가능성 언급
- drilling approval / energy-security event

Stage 2:
없음 또는 매우 약함
- 시추 결과 없음
- 경제성 없음
- 상업생산 없음

Stage 3:
없음
- reserve estimate와 drilling approval만으로 Green 금지

Stage 4B:
2024-06-03
- 장중 +30%
- 38,700원
- 가격이 증거보다 먼저 감

Stage 4C:
시추 실패, 경제성 부재, 정책 후퇴, 개발비 부담 확인 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported intraday price anchor

stage3_price:
N/A

event_peak_price:
38,700원

event_MFE_1D:
+30.0%

implied_pre_event_reference_price:
38,700 / 1.30
= 약 29,769원

drilling_cost_per_attempt:
약 100B won

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
- WSJ는 event-day anchor만 제공.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
38,700원 event-day anchor

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
success
- Stage 3 증거 없이 당일 +30%면 즉시 4B/event premium 처리.
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = resource_discovery_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### 교정

```text
내릴 축:
resource_estimate_without_drilling
policy_approval_only
price_rally_before_commerciality

Green gate:
drilling_result
commerciality
development_plan
production_timeline
revenue_conversion
```

---

## Case B — 두산에너빌리티 / 체코 원전·SMR `success_candidate / policy-to-contract watch`

```text
symbol = 034020
case_type = success_candidate + 4C-watch
archetype = NUCLEAR_POLICY_TO_CONTRACT / SMR_AI_POWER_POLICY_EVENT
```

### evidence

2024년 7월 체코 정부는 KHNP를 신규 원전 2기 건설 우선협상대상자로 선정했다. Reuters는 이것이 한국의 2009년 UAE 원전 이후 첫 대형 해외 원전 수주 기대이며, 최종 계약금액은 아직 협상 전이라고 설명했다. 같은 기사에서 두산에너빌리티 주가는 체코 수주 기대 등으로 최근 3개월간 48% 상승했다고 보도했다. ([Reuters][2])

2025년 5월에는 EDF의 법적 이의로 체코 법원이 KHNP 계약 서명을 일시적으로 막았고, 이는 policy-to-contract 경로의 4C-watch였다. 이후 2025년 6월 체코 측은 하급심 제동이 해소된 뒤 KHNP와 2기 원전 계약을 체결했다. AP는 계약가치가 4,070억 코루나, 약 187억 달러라고 보도했다. ([AP News][3])

2025년 8월 한미 정상회담 투자 패키지에서는 KHNP·두산에너빌리티가 X-energy, AWS와 SMR 설계·건설·공급망 협력에 참여했고, 두산에너빌리티가 Fermi America의 Texas AI project에 원전·SMR 장비를 공급하는 합의도 포함됐다. 다만 이런 MOU/협력은 Stage 2 후보일 뿐, 장비 수주잔고와 마진이 확인되기 전 Stage 3가 아니다. ([Reuters][4])

### stage date

```text
Stage 1:
2024-07-17
- Czech nuclear preferred bidder
- 한국 원전 수출 재개 기대

Stage 2:
2025-06-04
- Czech nuclear contract signed after court clearance
- 407B koruna / $18.7B project

추가 Stage 2:
2025-08-26
- X-energy / AWS / Fermi America SMR cooperation
- Doosan equipment-supply agreement

Stage 3:
보류
- Doosan의 실제 장비 수주잔고
- 납기, 마진, EPS revision, cashflow 확인 필요

Stage 4B:
2024-07-17 전후
- Doosan Enerbility +48% over 3 months
- 원전 수출 기대가 가격에 먼저 반영된 구간

Stage 4C-watch:
2025-05-06
- Czech court blocks signing temporarily
- 법적 지연 / final-contract risk

4C relief:
2025-06-04
- Czech deal signed after court clearance
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters / AP reported return and contract anchors

stage3_price:
N/A

reported_MFE_3M:
Doosan Enerbility +48% over three months

Czech_project_initial_unit_cost_estimate:
200B koruna per unit when building two at same site

signed_contract_value:
407B koruna / $18.7B

reactor_count:
2

contract_value_per_reactor:
407B / 2
= 203.5B koruna per reactor

SMR_US_investment_event:
price_data_unavailable_after_deep_search
- Reuters summit article provides policy/MOU evidence but not Doosan stock reaction anchor.

MFE_30D / 90D / 180D:
reported_MFE_90D = +48%
other windows unavailable

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

peak_price:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search

Stage 4B peak-before 여부:
partial_success
- preferred-bidder 단계에서 이미 +48%면 4B-watch 필요.
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = policy_to_contract_watch
stage_failure_type = stage2_watch_success
```

### 교정

```text
올릴 축:
preferred_bidder_to_final_contract
funded_contract
equipment_backlog_visibility

내릴 축:
MOU_only
SMR_story_without_order
court_or_legal_delay
price_rally_before_backlog
```

---

## Case C — HD현대중공업 / HD현대미포 `event_premium + policy-to-order watch`

```text
symbols = 329180 / 010620
case_type = success_candidate + 4B-watch
archetype = GEOPOLITICAL_SHIPBUILDING_POLICY / US_SHIPBUILDING_REBUILD_POLICY
```

### evidence

2025년 8월 27일 HD현대중공업은 HD현대미포와 합병해 미국 조선시장 진출을 확대하겠다고 밝혔다. Reuters는 이 계획이 한미 정상회담 이후 한국 측이 “Make American Shipbuilding Great Again”이라고 부른 미·한 조선협력 프로젝트와 연결되어 있다고 보도했다. 발표 전후 HD현대중공업은 11.3%, HD현대미포는 14.6% 상승해 record high로 마감했다. ([Reuters][5])

2025년 한미 정상회담 투자 패키지에서도 HD현대와 한국산업은행이 Cerberus와 미국 해양역량 강화 공동펀드 MOU를 맺고, 삼성중공업이 Vigor Marine Group과 미 해군 지원함 MRO·조선소 현대화·공동 건조 관련 preliminary deal을 체결한 것으로 보도됐다. 이는 R11에서는 Stage 1~2 정책 event이지, funded order와 margin 전 Stage 3가 아니다. ([Reuters][4])

### stage date

```text
Stage 1:
2025-04~08
- U.S. shipbuilding rebuild
- MASGA / U.S.-Korea maritime capacity cooperation

Stage 2:
2025-08-27
- HD Hyundai Heavy / HD Hyundai Mipo merger announcement
- U.S. shipbuilding market expansion target

Stage 3:
없음
- 합병·MOU·정책 이벤트만으로 Green 금지
- 실제 funded order, contract amount, margin, revenue conversion 필요

Stage 4B:
2025-08-27
- HD Hyundai Heavy +11.3%
- HD Hyundai Mipo +14.6%
- both record highs

Stage 4C:
MOU 불발, 미국 예산 미반영, 수주 지연, integration cost, China sanction risk 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return anchor

stage3_price:
N/A

HD_Hyundai_Heavy_event_MFE_1D:
+11.3%

HD_Hyundai_Mipo_event_MFE_1D:
+14.6%

record_high_status:
both closed at record highs

share_exchange_ratio:
1 HD Hyundai Mipo share for 1.04059146 HD Hyundai Heavy shares

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4B peak-before 여부:
success
- policy/merger news로 record high라면 4B-watch.
```

### alignment

```text
score_price_alignment = event_premium + success_candidate
rerating_result = US_shipbuilding_policy_watch
stage_failure_type = stage2_watch_success
```

### 교정

```text
Stage 2 가능:
MOU
merger
policy package
U.S. Navy / shipyard cooperation

Stage 3 조건:
funded order
contract amount
delivery schedule
margin
revenue conversion
```

---

## Case D — 하림 / 마니커류 poultry basket `event_premium / disease-demand fade`

```text
symbols = poultry basket, e.g. Harim / Maniker류
case_type = event_premium
archetype = EVENT_DISEASE_PEST_DEMAND
```

### evidence

2025년 5월 브라질 상업농장에서 고병원성 조류독감이 발생하면서 EU·중국·한국 등 주요 수입국이 브라질산 닭고기 수입제한을 걸었다. Reuters는 브라질이 세계 최대 poultry exporter이며, South Korea도 초기에는 전국 단위 수입금지를 적용했다고 보도했다. ([Reuters][6])

그러나 2025년 6월 23일 South Korea는 브라질이 상업농장 조류독감 청정 상태를 회복했다고 선언한 뒤, 수입제한을 전국 단위에서 affected region 중심으로 완화했다. 이는 poultry basket의 one-off event premium이 빠르게 fade될 수 있음을 보여준다. ([Reuters][7])

### stage date

```text
Stage 1:
2025-05-19
- Brazil bird flu
- South Korea import restriction
- domestic poultry substitution theme

Stage 2:
없음 또는 보류
- 국내 업체별 판매가격, 출하량, 마진 확인 필요

Stage 3:
없음
- 질병·수입금지 이벤트만으로 Green 금지

Stage 4B:
2025-05~06
- poultry basket이 수입금지 뉴스로 급등했다면 4B/event premium

Stage 4C:
2025-06-23
- South Korea eases restrictions
- one-off disease event fade
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters disease/import-restriction evidence

stage3_price:
N/A

stock_price:
price_data_unavailable_after_deep_search
- Reuters는 Harim/Maniker 등 한국 poultry stock reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

Brazil_2024_poultry_exports:
over 5M tons

EU_share_of_Brazil_exports:
4.4%

restriction_start_reference:
2025-05-19 Reuters report

restriction_easing:
2025-06-23

event_duration:
35 calendar days

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
conceptual_success
- 수입제한 완화 뉴스가 event fade trigger.
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = one_off_disease_event
stage_failure_type = stage1_attention_only
```

### 교정

```text
질병 이벤트:
Stage 1

Stage 3 조건:
국내 판매량 증가
가격전가
feed cost 통과
재고 안정
OPM 개선

4C/event fade:
수입제한 완화
청정상태 선언
수급 정상화
```

---

## Case E — LK-99 / 초전도체 basket `overheat / speculative science thesis break`

```text
symbols = 신성델타테크·서남·모비스류 초전도체 basket
case_type = overheat / thesis_break
archetype = SPECULATIVE_SCIENCE_THEME
```

### evidence

2023년 7월 22일 한국 연구진은 arXiv preprint에서 LK-99가 상온·상압 초전도체라고 주장했다. 해당 preprint는 임계온도 400K 이상과 Meissner effect 등을 근거로 제시했다. ([arXiv][8])

하지만 2023년 8월 7일 공개된 독립 재현 논문은 LK-99가 상온에서 초전도 signature를 보이지 않았다고 보고했다. 이후 여러 재현 시도와 검증을 거쳐 2023년 8월 중순에는 순수 LK-99가 실온 초전도체가 아니며, 관찰된 일부 현상은 불순물이나 일반 자기 반응으로 설명될 수 있다는 쪽으로 정리됐다. ([arXiv][9])

### stage date

```text
Stage 1:
2023-07-22
- LK-99 arXiv preprint
- room-temperature superconductor claim

Stage 2:
없음
- peer review / independent replication / commercial path 없음

Stage 3:
없음
- preprint / science claim만으로 Green 금지

Stage 4B:
2023-08 초
- superconductor theme rally
- speculative science event premium

Stage 4C:
2023-08-07 이후
- independent replication failure
- scientific thesis break
```

### 실제 가격경로 검증

```text
price_data_source:
arXiv / LK-99 summary evidence

stage3_price:
N/A

stock_price:
price_data_unavailable_after_deep_search
- Reuters/Bloomberg 등 정확한 Korean basket OHLC anchor를 이번 pass에서 확보하지 못함.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

claim_date:
2023-07-22

negative_replication_date:
2023-08-07

claim_to_negative_replication:
16 calendar days

consensus_reversal_period:
mid-August 2023

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
success_by_science_gate
- independent replication gate를 요구했다면 Green 자체가 차단됨.
```

### alignment

```text
score_price_alignment = thesis_break / price_moved_without_evidence
rerating_result = speculative_science_theme_overheat
stage_failure_type = should_have_been_stage1_or_red
```

### 교정

```text
preprint:
Stage 1

independent replication:
Stage 2 후보

commercial product / revenue:
Stage 3 후보

replication failure:
4C / thesis break
```

---

## Case F — 계엄·정치 shock `macro 4C-watch / market-level RedTeam`

```text
symbol = KOSPI / Korea risk premium basket
case_type = policy_market_shock / macro 4C-watch
archetype = POLICY_MARKET_SHOCK_EVENT
```

### evidence

2024년 12월 3일 윤석열 당시 대통령의 비상계엄 선포와 해제 직후 한국 금융당국은 시장 안정화를 위해 “무제한” 유동성 공급을 약속했고, 금융당국은 필요 시 최대 10조 원 규모 증시안정펀드를 가동할 수 있다고 밝혔다. Reuters는 이 사건이 원화 급락과 정치 안정성 우려를 낳았다고 보도했다. ([Reuters][10])

2024년 12월 4일 Reuters는 KOSPI가 거의 2% 하락했고, 원화가 달러 대비 2년 저점 부근에 머물렀으며, KOSPI가 연초 대비 7% 넘게 하락한 상태였다고 보도했다. 이건 개별 종목 Stage가 아니라 **macro policy shock overlay**다. ([Reuters][11])

### stage date

```text
Stage 1:
2024-12-03
- emergency martial law declaration

Stage 2:
없음

Stage 3:
없음

Stage 4B:
해당 없음

Stage 4C:
2024-12-04
- KOSPI nearly -2%
- won near two-year low
- market-level policy shock
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters macro-market event anchors

stage3_price:
N/A

KOSPI_event_MAE:
nearly -2%

KOSPI_YTD_drawdown_context:
more than -7%

market_stabilization_fund:
up to 10T won

liquidity_support:
unlimited liquidity pledged

MFE:
N/A

MAE_5D / 20D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A

Stage 4C 큰 하락 이전 포착 여부:
macro shock itself
- 사전 예측보다는 발생 즉시 macro risk overlay로 적용.
```

### alignment

```text
score_price_alignment = macro_policy_shock
rerating_result = market_risk_premium_event
stage_failure_type = macro_redteam_overlay
```

### 교정

```text
개별 기업 score:
직접 Green/Red로 바꾸지 않음

overlay:
macro_risk_penalty
FX_volatility
foreign_outflow_risk
liquidity_support_watch
policy_stability_risk
```

---

## Case G — 공매도 재개 / MSCI 접근성 `market_structure_watch / not company Green`

```text
symbol = broad market / securities basket
case_type = success_candidate / market_structure_watch
archetype = MARKET_STRUCTURE_SHORT_SELLING_POLICY
```

### evidence

2025년 6월 MSCI는 한국의 short-selling accessibility 평가가 개선됐다고 밝혔다. Reuters는 한국이 2025년 3월 5년 만의 전면 공매도 금지를 해제했고, 이는 외국인 투자자와 MSCI 시장 접근성의 핵심 이슈였다고 보도했다. 다만 MSCI 선진국 watchlist 편입 가능성은 여전히 50% 미만으로 보는 시각이 있었고, 외환시장 접근성 문제도 남아 있었다. ([Reuters][12])

### stage date

```text
Stage 1:
2025-03
- full short-selling ban lifted after five years

Stage 2:
2025-06-20
- MSCI says short-selling accessibility improved

Stage 3:
없음
- 개별 증권사 이익, 거래대금, 외국인 유입, 수수료 수익 확인 필요

Stage 4B:
MSCI developed-market 기대가 시장을 먼저 밀면 후보

Stage 4C:
불법 공매도 재발, market trust damage, MSCI watchlist 실패, FX access issue 지속 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters market-structure evidence

stage3_price:
N/A

stock/basket price:
price_data_unavailable_after_deep_search
- Reuters는 securities basket 주가 reaction anchor를 제공하지 않음.
- KRX/Naver/Yahoo/Stooq 원시 OHLC 직접 확보 실패.

short_selling_ban_period:
about five years

MSCI_watchlist_probability_context:
less than 50% according to analysts cited by Reuters

remaining_issue:
foreign exchange market access

MFE / MAE:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = success_candidate / market_structure_watch
rerating_result = market_accessibility_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정

시장구조 개선은 R11에서 중요한 positive overlay지만, 개별 종목 Stage 3가 아니다.

```text
Stage 3 조건:
foreign inflow 지속
거래대금 증가
증권사 이익 증가
MSCI watchlist / upgrade path 구체화
market multiple expansion
```

---

# 5. 이번 R11 case별 요약표

| case                 | 분류                           |                                                        실제 가격검증 | alignment                         |
| -------------------- | ---------------------------- | -------------------------------------------------------------: | --------------------------------- |
| 한국가스공사 / 동해 가스       | price_moved_without_evidence |                        38,700원, 장중 +30%, implied prior 29,769원 | event_premium                     |
| 두산에너빌리티 / 원전·SMR     | success_candidate + 4B-watch |                 최근 3개월 +48%, Czech signed contract 407B koruna | policy_to_contract_watch          |
| HD현대중공업/미포           | success_candidate + 4B       |                                  +11.3% / +14.6%, record highs | event_premium + success_candidate |
| poultry basket       | event_premium                | Brazil ban → Korea easing in 35 days, stock anchor unavailable | one_off_disease_event             |
| LK-99 basket         | overheat / thesis_break      |   claim→negative replication 16 days, stock anchor unavailable | speculative_science_break         |
| martial law shock    | macro 4C-watch               |             KOSPI nearly -2%, stabilization fund up to 10T won | macro_policy_shock                |
| short-selling / MSCI | market_structure_watch       |        short-selling access improved, price anchor unavailable | market_structure_stage2           |

---

# 6. score-price alignment 판정

```text
price_moved_without_evidence:
- 한국가스공사 동해 가스
- LK-99 speculative science basket
- HD현대중공업/미포 MASGA event 일부

event_premium:
- 한국가스공사
- poultry disease event
- HD현대중공업/미포 merger/policy rally

success_candidate:
- 두산에너빌리티 원전·SMR
- HD현대중공업/미포 미국 조선정책
- 공매도/MSCI market structure

thesis_break:
- LK-99 replication failure

macro_policy_shock:
- 계엄·정치 shock

4B-watch:
- 한국가스공사 +30%
- 두산에너빌리티 preferred-bidder 기대 +48% over 3M
- HD현대중공업/미포 record highs
- poultry import-ban basket
- LK-99 speculative rally

4C-watch:
- 체코 원전 court delay
- poultry restriction easing
- martial law macro shock
- MSCI/short-selling reform failure risk
```

---

# 7. 점수비중 교정

## 올릴 축

```text
funded_budget +5
actual_contract +5
revenue_conversion +5
financing_secured +5
procurement_award +4
commerciality_confirmed +5
independent_replication_or_validation +5
event_to_contract_escalation +5
policy_durability +4
```

### 이유

두산에너빌리티/체코 원전은 R11에서 이벤트가 Stage 2로 승격되는 좋은 예다. preferred bidder 단계에서 주가가 먼저 +48% 움직였지만, 실제로 체코 원전 계약이 체결되면서 policy-to-contract 경로가 일부 검증됐다. 다만 두산의 장비 수주잔고·마진·EPS revision 전에는 Stage 3가 아니다. ([Reuters][2])

## 내릴 축

```text
policy_news_only -5
mou_only -5
geopolitical_headline_only -5
resource_estimate_without_drilling -5
preprint_or_science_claim_only -5
disease_import_ban_only -4
market_structure_reform_without_earnings -3
price_rally_before_contract -5
event_fade_risk -5
```

### 이유

한국가스공사는 경제성과 상업성 확인 전 장중 +30% 올랐고, poultry event는 수입제한이 35일 만에 완화됐으며, LK-99는 preprint 후 독립 재현 실패로 thesis가 꺾였다. 이런 사건은 R11에서 기본적으로 Stage 1 / event premium으로 둬야 한다. ([월스트리트저널][1])

## Green gate 강화 조건

```text
R11 Stage 3-Green 필수:
1. 정책/이벤트가 회사 단위 계약으로 승격
2. 계약금액 또는 예산 확인
3. financing 확인
4. 실제 발주 또는 조달계약
5. 매출 인식 가능성
6. margin 또는 EPS/FCF revision 확인
7. event fade가 아니라 반복 수요 확인
8. 가격경로가 증거 이후 따라옴

금지:
정책 뉴스만 있음
MOU만 있음
지정학 headline만 있음
자원 매장 가능성만 있음
질병/재난 이벤트만 있음
preprint/과학 claim만 있음
정부 발표 후 관련주 급등만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
뉴스 발표일 장중 상한가/급등
정책·MOU·자원발견 테마주 동반 급등
과학 preprint 후 관련주 급등
질병·재난 이벤트로 5D/20D 급등
MOU가 계약처럼 가격에 반영
계약 전부터 목표가·테마 리포트 반복

4B-elevated:
후속 공시 없이 가격만 유지
정부 예산/financing이 불명확
시추/검증/재현 결과가 나오기 전 valuation 확장
제도개선 기대가 기업 이익보다 먼저 반영
```

## 4C hard gate 조건

```text
시추 실패
경제성 부재
MOU 불발
예산 미반영
정부 정책 후퇴
수입제한 완화로 one-off demand fade
과학 claim 재현 실패
regulatory reversal
정치 shock
제도개선 기대 실패
contract cancellation
financing failure
```

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
r11_default_stage3_bias = very_conservative
```

이번 세션에서 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉을 안정적으로 직접 확보하지 못했다. 대신 Reuters / WSJ / AP / FT / arXiv의 가격 anchor와 이벤트 수익률, 계약·정책·시장충격 수치를 사용해 계산 가능한 부분은 직접 계산했다.

---

# 9. patch-ready 출력

## docs/round/round_143.md 요약

```md
# R11 Loop 8. Policy / Geopolitical / Disaster / Event Price Validation

이번 라운드는 R11 price-validation 라운드다.

핵심 결론:
- 한국가스공사 동해 가스 이벤트는 38,700원, 장중 +30%로 price_moved_without_evidence다. 시추·경제성·상업성 전 Stage 3 금지다.
- 두산에너빌리티는 체코 원전 preferred bidder 기대 등으로 3개월 +48%였고, 이후 체코 계약은 407B koruna / $18.7B로 체결됐다. 그러나 두산 장비 수주잔고·마진 전 Stage 3는 아니다.
- HD현대중공업/미포는 MASGA·미국 조선정책 기대와 합병 발표로 +11.3% / +14.6% record high를 기록했다. funded order 전 Green 금지다.
- poultry basket은 Brazil bird flu import ban event이지만 한국이 35일 후 제한을 완화했다. one-off disease event로 분류한다.
- LK-99는 preprint claim 후 16일 만에 negative replication이 나왔고, speculative science thesis break로 분류한다.
- martial law shock은 KOSPI nearly -2%, market stabilization fund up to 10T won이 동반된 macro RedTeam overlay다.
- short-selling / MSCI accessibility 개선은 market structure Stage 2지만 개별 기업 Stage 3가 아니다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 143 R11 Loop 8 Policy Geopolitical Event Price Validation

## 반영 내용
- R11 Loop 8 price-validation 라운드를 추가했다.
- Resource discovery, nuclear policy-to-contract, U.S. shipbuilding policy, poultry disease event, speculative science, martial-law macro shock, short-selling/MSCI market structure를 비교했다.
- Reuters/WSJ/AP/FT/arXiv reported anchors로 가능한 MFE/MAE 및 policy/contract/event metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- funded budget, actual contract, financing, procurement award, independent validation 가중치 강화
- policy news only, MOU only, resource estimate without drilling, disease event only, preprint-only 감점 강화
- R11 기본 Stage 3 bias를 very conservative로 설정
```

## case row 초안

```jsonl
{"case_id":"r11_loop8_kogas_east_sea_resource_event","symbol":"036460","company_name":"한국가스공사","case_type":"event_premium","primary_archetype":"DOMESTIC_RESOURCE_DISCOVERY_EVENT","stage1_date":"2024-06-03","stage4b_date":"2024-06-03","price_validation":{"price_data_source":"WSJ reported intraday price anchor","stage3_price":null,"event_peak_price":38700,"event_mfe_1d_pct":30.0,"implied_pre_event_reference_price":29769,"drilling_cost_per_attempt_krw_bn":100,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"resource_discovery_event_premium","notes":"Resource estimate and drilling approval are Stage 1; commerciality and revenue conversion required for Stage 3."}
{"case_id":"r11_loop8_doosan_nuclear_policy_to_contract","symbol":"034020","company_name":"두산에너빌리티","case_type":"success_candidate","primary_archetype":"NUCLEAR_POLICY_TO_CONTRACT","stage1_date":"2024-07-17","stage2_date":"2025-06-04","stage4b_date":"2024-07-17","stage4c_date":"2025-05-06","price_validation":{"price_data_source":"Reuters/AP reported anchors","stage3_price":null,"reported_mfe_3m_pct":48.0,"signed_contract_value_koruna_bn":407,"signed_contract_value_usd_bn":18.7,"reactor_count":2,"contract_value_per_reactor_koruna_bn":203.5,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate","rerating_result":"policy_to_contract_watch","notes":"Preferred bidder and final contract are Stage 2; Doosan equipment backlog and margin required for Stage 3."}
{"case_id":"r11_loop8_hd_hyundai_masga_shipbuilding_event","symbol":"329180/010620","company_name":"HD현대중공업/HD현대미포","case_type":"success_candidate","primary_archetype":"US_SHIPBUILDING_REBUILD_POLICY","stage2_date":"2025-08-27","stage4b_date":"2025-08-27","price_validation":{"price_data_source":"Reuters reported event return anchor","stage3_price":null,"hd_hyundai_heavy_mfe_1d_pct":11.3,"hd_hyundai_mipo_mfe_1d_pct":14.6,"record_high_status":true,"share_exchange_ratio_mipo_per_heavy":1.04059146,"price_validation_status":"reported_event_return_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"US_shipbuilding_policy_watch","notes":"MASGA/merger/MOU is Stage 2 and 4B-watch; funded order and margin required for Stage 3."}
{"case_id":"r11_loop8_poultry_bird_flu_import_ban_event","symbol":"Harim/Maniker_basket","company_name":"Poultry basket","case_type":"event_premium","primary_archetype":"EVENT_DISEASE_PEST_DEMAND","stage1_date":"2025-05-19","stage4c_date":"2025-06-23","price_validation":{"price_data_source":"Reuters import restriction evidence","stage3_price":null,"brazil_2024_poultry_exports_mn_tons":5.0,"eu_share_of_brazil_exports_pct":4.4,"event_duration_days":35,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"one_off_disease_event","notes":"Import ban is one-off Stage 1; South Korea restriction easing is event fade."}
{"case_id":"r11_loop8_lk99_speculative_science_break","symbol":"superconductor_basket","company_name":"LK-99 초전도체 basket","case_type":"overheat","primary_archetype":"SPECULATIVE_SCIENCE_THEME","stage1_date":"2023-07-22","stage4c_date":"2023-08-07","price_validation":{"price_data_source":"arXiv / LK-99 scientific evidence","stage3_price":null,"claim_to_negative_replication_days":16,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"speculative_science_theme_overheat","notes":"Preprint is Stage 1; independent replication failure is 4C/thesis break."}
{"case_id":"r11_loop8_martial_law_macro_market_shock","symbol":"KOSPI_macro","company_name":"Korea market macro shock","case_type":"macro_4c_watch","primary_archetype":"POLICY_MARKET_SHOCK_EVENT","stage4c_date":"2024-12-04","price_validation":{"price_data_source":"Reuters macro-market anchors","stage3_price":null,"kospi_event_mae_pct":-2.0,"kospi_ytd_drawdown_context_pct":-7.0,"market_stabilization_fund_krw_trn":10,"liquidity_support":"unlimited","price_validation_status":"reported_macro_anchor_not_full_ohlc"},"score_price_alignment":"macro_policy_shock","rerating_result":"market_risk_premium_event","notes":"Macro overlay, not company-specific Stage 3/4C."}
{"case_id":"r11_loop8_short_selling_msci_market_structure","symbol":"market_structure_basket","company_name":"Short-selling / MSCI accessibility","case_type":"success_candidate","primary_archetype":"MARKET_STRUCTURE_SHORT_SELLING_POLICY","stage1_date":"2025-03","stage2_date":"2025-06-20","price_validation":{"price_data_source":"Reuters market-structure evidence","stage3_price":null,"short_selling_ban_period_years":5,"watchlist_probability_context_pct":50,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"market_structure_watch","rerating_result":"market_accessibility_watch","notes":"Market accessibility is Stage 2 overlay; company EPS or brokerage revenue needed for Stage 3."}
```

## shadow weight row 초안

```csv
archetype,funded_budget,actual_contract,financing,procurement_award,revenue_conversion,independent_validation,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
DOMESTIC_RESOURCE_DISCOVERY_EVENT,+0,+0,+0,+0,+0,+0,-5,+5,+5,Korea Gas East Sea event is price_moved_without_evidence until drilling/commerciality/revenue.
NUCLEAR_POLICY_TO_CONTRACT,+4,+5,+4,+4,+4,+0,-2,+5,+4,Doosan/Czech nuclear shows policy-to-contract Stage 2 but equipment backlog/margin needed for Green.
US_SHIPBUILDING_REBUILD_POLICY,+3,+3,+3,+3,+3,+0,-4,+5,+4,HD Hyundai MASGA/merger event is Stage 2 and 4B-watch until funded order/margin.
EVENT_DISEASE_PEST_DEMAND,+0,+0,+0,+0,+1,+0,-5,+5,+5,Poultry import ban is one-off event; easing is event fade.
SPECULATIVE_SCIENCE_THEME,+0,+0,+0,+0,+0,+5,-5,+5,+5,LK-99 preprint is Stage 1; independent replication failure is thesis break.
POLICY_MARKET_SHOCK_EVENT,+0,+0,+0,+0,+0,+0,-3,+3,+5,Martial-law shock is macro RedTeam overlay.
MARKET_STRUCTURE_SHORT_SELLING_POLICY,+2,+0,+0,+0,+2,+0,-3,+3,+3,Short-selling/MSCI accessibility is positive market-structure overlay but not company Green.
```

---

# 이번 R11 Loop 8 결론

R11은 거의 항상 Stage 3를 보류해야 한다.

```text
1. 한국가스공사 동해 가스 이벤트는 Stage 1 / 4B-watch다.
   장중 +30%였지만 시추·경제성·상업성 전 Stage 3가 아니다.

2. 두산에너빌리티 원전은 R11에서 드문 success_candidate다.
   preferred bidder에서 final contract로 일부 승격됐지만, 장비 수주잔고·마진 전 Green은 아니다.

3. HD현대중공업/미포 MASGA 이벤트는 정책·합병·record high가 섞인 4B-watch다.
   funded order와 FCF 전 Stage 3 금지다.

4. 조류독감·수입제한은 one-off event다.
   한국의 제한 완화가 곧 event fade trigger다.

5. LK-99는 speculative science hard 반례다.
   preprint는 Stage 1, 독립 재현 실패는 thesis break다.

6. 계엄·정치 shock은 개별 기업보다 macro RedTeam overlay로 둬야 한다.

7. 공매도 재개와 MSCI 접근성 개선은 긍정적 market-structure Stage 2지만,
   외국인 유입·거래대금·증권사 이익·시장 multiple 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R11에서 진짜 Stage 3는 “정책·지정학·재난 뉴스가 크다”가 아니라, 그 뉴스가 계약·예산·financing·발주·매출·EPS/FCF로 승격되는 순간이다.**
> **R11의 기본값은 Green이 아니라 Event Premium이며, 가격이 먼저 뛴 경우 4B-watch를 가장 빨리 붙여야 한다.**

[1]: https://www.wsj.com/articles/korea-gas-leads-energy-rally-on-seoul-s-offshore-oil-drilling-approval-c8c4d428?utm_source=chatgpt.com "Korea Gas Leads Energy Rally on Seoul's Offshore Oil Drilling Approval"
[2]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[3]: https://apnews.com/article/2dcaa77856b7837c596cb0291dad5659?utm_source=chatgpt.com "A Czech court blocks the signing of a deal with South Korea's KHNP to build 2 nuclear reactors"
[4]: https://www.reuters.com/business/aerospace-defense/south-korean-firms-pledge-150-billion-us-investments-summit-2025-08-26/?utm_source=chatgpt.com "South Korean firms pledge $150 billion in US investments at summit"
[5]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/brazil-can-no-longer-export-poultry-meat-eu-due-bird-flu-2025-05-19/?utm_source=chatgpt.com "Brazil can no longer export poultry and meat to EU due to bird flu"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/iraq-removes-south-korea-eases-restrictions-import-brazil-chicken-meat-2025-06-23/?utm_source=chatgpt.com "Iraq removes, South Korea eases restrictions on import of Brazil chicken meat"
[8]: https://arxiv.org/abs/2307.12008?utm_source=chatgpt.com "The First Room-Temperature Ambient-Pressure Superconductor"
[9]: https://arxiv.org/abs/2308.03544?utm_source=chatgpt.com "Absence of superconductivity in LK-99 at ambient conditions"
[10]: https://www.reuters.com/markets/asia/skorea-authorities-vow-stabilize-markets-parliament-votes-lift-martial-law-2024-12-03/?utm_source=chatgpt.com "South Korea rushes to stabilise markets after Yoon's martial law bid"
[11]: https://www.reuters.com/markets/global-markets-wrapup-1-2024-12-04/?utm_source=chatgpt.com "Asian stocks slip, rattled by South Korean political unrest"
[12]: https://www.reuters.com/world/asia-pacific/south-koreas-short-selling-accessibility-has-improved-msci-says-2025-06-20/?utm_source=chatgpt.com "South Korea's short-selling accessibility has improved, MSCI says"
