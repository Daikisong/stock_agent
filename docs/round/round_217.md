순서상 이번은 **R13 Loop 8 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**다.

이번 R13은 새 섹터가 아니라, **R1~R12에서 나온 모든 후보를 다시 부수는 라운드**다. 특히 이번에는 `Stage 3 성공`, `4B 조기감지`, `4C hard gate`, `price_moved_without_evidence`를 한 테이블에 놓고 비교한다.

```text
round = R13 Loop 8
round_id = round_145
large_sector = CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION
production_scoring_changed = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

원시 수정주가 일봉 OHLC를 직접 안정적으로 추출하지 못한 항목은 숫자를 만들지 않았다. 대신 Reuters / WSJ / FT / MarketWatch / Tom’s Hardware 등에서 확인된 **가격 anchor, 이벤트 수익률, 계약가치, 시총 변화**로 계산 가능한 값만 계산했다.

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
```

R13의 핵심 질문은 이거다.

```text
Stage 3가 실제 대형 MFE를 만들었나?
4B가 peak 전후에서 과열을 잡았나?
4C가 큰 하락 전에 thesis break를 잡았나?
가격이 증거보다 먼저 간 케이스를 Green으로 착각하지 않았나?
```

---

# 2. 대상 canonical archetype

```text
STRUCTURAL_SUCCESS_ALIGNED
STRUCTURAL_SUCCESS_BUT_4B_WATCH
CROWDED_RERATING_4B_WATCH
PRICE_ONLY_RALLY
EVENT_PREMIUM
FALSE_POSITIVE_SCORE
EVIDENCE_GOOD_BUT_PRICE_FAILED
THESIS_BREAK_4C
OPERATIONAL_TRUST_BREAK
CONTRACT_QUALITY_BREAK
GOVERNANCE_DILUTION_EVENT
LEGAL_REGULATORY_REDTEAM
MARKET_STRUCTURE_WATCH
UNKNOWN_INSUFFICIENT_EVIDENCE
```

---

# 3. deep sub-archetype

```text
성공 검증:
- HBM / AI memory Stage 3 success
- K-defense export delivery / revenue conversion
- Stage 3 이후 대형 MFE

4B 검증:
- 대시세 이후 시총 milestone
- 대형 증자 / CB / capital raise
- event-day 20~30% 급등
- IPO / MOU / 정책 / 미확정 보도 급등

4C 검증:
- 계약 취소
- 계약가치 붕괴
- 안전사고
- 법적·규제 리스크
- governance / dilution trust shock
- operational trust break

false Green 방지:
- 자원발견 가능성
- stablecoin policy theme
- MOU / preliminary deal
- 정책 이벤트
- commodity event
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success_aligned + 4B-watch`

```text
symbol = 000660
source_sector = R2
case_type = structural_success + 4B-watch
archetype = MEMORY_HBM_CAPACITY / STRUCTURAL_SUCCESS_BUT_4B_WATCH
```

### stage date

```text
Stage 1:
2024년 상반기
- AI server / HBM demand
- old memory-cycle frame break

Stage 2:
2024-06-25
- Nomura가 SK하이닉스 2024 OP 추정치를 30조 원, 2025 OP 추정치를 53조 원으로 상향
- HBM dominance + DRAM price upcycle + EPS revision

Stage 3:
2024-06-25 후보
- stage3_price anchor = 222,000원

Stage 4B:
2026-05-14
- 2025년 +274%
- 2026년 YTD +200% 이상
- 시총 약 $942B
- 1조 달러 근접

추가 4B-watch:
2026-05-11
- Intel EMIB 협업 보도 후 장중 1,946,000원 all-time high
```

Nomura의 2024년 6월 25일 추정치 상향은 단순 AI 테마가 아니라 **HBM 지배력 + 메모리 가격 상승 + 영업이익 revision**이 동시에 나온 Stage 3 anchor로 볼 수 있다. 당시 SK하이닉스 주가는 222,000원이었다. 이후 Reuters는 SK하이닉스가 2025년에 274% 상승하고 2026년에도 200% 넘게 올랐으며, 시총이 16개월 전 1,000억 달러 미만에서 약 9,420억 달러까지 커졌다고 보도했다. Tom’s Hardware는 2026년 5월 Intel EMIB 협업 보도 후 SK하이닉스가 장중 1,946,000원까지 올라 사상 최고가를 기록했다고 전했다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters / Tom’s Hardware reported anchors

entry_date:
2024-06-25

stage3_price:
222,000원

reported_peak_price:
1,946,000원

MFE_from_stage3_to_reported_peak:
(1,946,000 / 222,000) - 1
= +776.6%

reported_return_2025:
+274%

reported_return_2026_to_2026-05-14:
> +200%

minimum_compounded_return_from_start_2025_to_2026-05-14:
(1 + 2.74) * (1 + 2.00) - 1
= +1,022% 이상

market_cap_path:
< $100B → 약 $942B

minimum_market_cap_MFE:
(942 / 100) - 1
= +842% 이상

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_rerating
4B_status = 4B-watch / 4B-elevated
```

### R13 판정

SK하이닉스는 **Stage 3가 실제 대형 MFE를 만들 수 있음을 증명한 benchmark**다. 다만 2026년 5월 기준 신규 Stage 3가 아니라 **4B-watch**다.

---

## Case B — 현대로템 `structural_success_aligned / R1 성공 검증`

```text
symbol = 064350
source_sector = R1
case_type = structural_success
archetype = DEFENSE_GOVERNMENT_BACKLOG / ORDER_TO_REVENUE_CONVERSION
```

### stage date

```text
Stage 1:
2022~2024
- Poland K2 tank export
- European rearmament

Stage 2:
2024-04-09
- K2 18대 폴란드 납품이 1Q 실적을 견인할 것으로 추정
- OP YoY +85% 예상
- K2 수출 매출 2,700억 원, 분기 매출의 약 1/3

Stage 3:
2024-04-09 후보
- stage3_price anchor = 41,300원

Stage 4B:
2025-08-01
- Poland second K2 contract
- $6.5B 규모, 180대, 현지생산 포함
```

현대로템은 2024년 4월 9일 K2 전차 납품이 실적을 끌어올릴 것이라는 증권사 추정이 나오면서 9.3% 상승해 41,300원을 기록했다. KB증권은 K2 18대 납품으로 1분기 영업이익이 전년 대비 85% 증가할 수 있다고 봤고, K2 폴란드 매출 2,700억 원이 분기 매출의 약 3분의 1을 차지할 수 있다고 추정했다. 이후 2025년 8월 폴란드는 현대로템과 K2 180대 추가 계약을 체결했고, 이 계약은 약 65억 달러 규모이며 일부 현지 생산을 포함했다. ([월스트리트저널][2])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / Reuters reported price and contract anchors

entry_date:
2024-04-09

stage3_price:
41,300원

stage3_event_MFE_1D:
+9.3%

implied_pre_event_reference_price:
41,300 / 1.093
= 약 37,786원

KOSPI_same_context_return:
-0.3%

relative_outperformance:
9.3 - (-0.3)
= +9.6 percentage points

K2_export_revenue_1Q_estimate:
270B won

OP_growth_estimate:
+85% YoY

Poland_second_contract:
$6.5B

MFE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

peak_price:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = defense_export_revenue_conversion
stage_failure_type = green_success_candidate
```

### R13 판정

현대로템은 R1에서 **수주 headline이 아니라 납품·매출·OP revision이 Stage 3를 만든다**는 기준점이다.

---

## Case C — 한화에어로스페이스 `4B-watch / dilution shock is not automatic 4C`

```text
symbol = 012450
source_sector = R1 / R13
case_type = 4B-watch
archetype = CROWDED_RERATING_4B_WATCH / CAPITAL_ALLOCATION_DILUTION_OVERLAY
```

### stage date

```text
Stage 1~3:
2024~2025
- K-defense export cycle
- Europe rearmament
- overseas production expansion

Stage 4B:
2025-03-21
- 3.6조 원 유상증자 발표 후 주가 -13%
- 주가가 이미 YTD 2배 이상 오른 뒤 발생

Stage 4C:
아님
- dilution shock이지만, 수요·수주 thesis break는 아님
```

한화에어로스페이스는 2025년 3월 3.6조 원 규모 증자를 발표했고, 주가는 다음 날 13% 급락했다. Reuters와 FT 모두 이 증자가 해외 생산 확대와 투자 목적이었으나, 투자자들이 희석과 자금조달 필요성을 우려했다고 보도했다. FT는 당시 주가가 연초 이후 이미 두 배 이상 오른 상태였다고 전했다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / FT reported event anchors

stage3_price:
N/A in this overlay row

capital_raise_size:
3.6T won

stage4b_event_MAE_1D:
-13%

share_sale_price:
605,000원

discount_to_prior_close:
-16%

reported_pre_event_YTD_status:
more than doubled

MFE_30D / 90D:
price_data_unavailable_after_deep_search

drawdown_after_peak:
at least -13% event drawdown
```

### alignment

```text
score_price_alignment = aligned_4B_detection
rerating_result = true_rerating_with_dilution_watch
stage_failure_type = not_4C
```

### R13 판정

한화에어로스페이스는 **4B와 4C를 분리해야 하는 기준점**이다.

```text
대시세 후 증자:
4B-watch / 4B-elevated

수주 취소·마진 붕괴·EPS 하향:
4C 후보
```

---

## Case D — 한국가스공사 `price_moved_without_evidence`

```text
symbol = 036460
source_sector = R11
case_type = event_premium / price_moved_without_evidence
archetype = DOMESTIC_RESOURCE_DISCOVERY_EVENT
```

### stage date

```text
Stage 1:
2024-06-03
- 동해 석유·가스 탐사 승인
- 최대 140억 배럴 가능성

Stage 2:
없음
- 시추 결과 없음
- 경제성 없음

Stage 3:
없음

Stage 4B:
2024-06-03
- 장중 +30%
- 38,700원

Stage 4C:
시추 실패, 경제성 부재, 정책 후퇴 시 후보
```

한국가스공사는 동해 석유·가스 탐사 승인 발표 당일 장중 최대 30% 상승해 38,700원을 기록했다. 그러나 WSJ는 당시 대통령이 매장량의 경제성이 아직 결정되지 않았고, 최소 5차례 시추가 필요하며 시추 1회당 약 1,000억 원이 든다고 말했다고 보도했다. ([월스트리트저널][4])

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
100B won

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
N/A
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = resource_discovery_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### R13 판정

한국가스공사는 R11/R13에서 **정책·자원발견 이벤트를 Green으로 올리면 안 되는 대표 case**다.

---

## Case E — LG에너지솔루션 / L&F `contract-quality hard 4C`

```text
symbols = 373220 / 066970
source_sector = R3
case_type = 4C-thesis-break
archetype = CONTRACT_QUALITY_BREAK / THESIS_BREAK_4C
```

### stage date

```text
LGES Stage 4C:
2025-12-18
- Ford EV battery supply deal cancellation
- 주가 장중 -7.6%

LGES 추가 4C:
2025-12-26
- Freudenberg 3.9조 원 계약 종료
- Ford + Freudenberg 총 13.5조 원 기대매출 손실

L&F Stage 4C:
2025-12-29
- Tesla 공급계약 예상가치 $2.9B → $7,386
```

LG에너지솔루션은 Ford와 Freudenberg 계약 종료로 약 13.5조 원의 기대매출을 잃게 됐고, 이는 2024년 매출 25.62조 원의 절반을 넘는 규모다. Reuters는 Ford 계약 취소 이후 LGES 주가가 장중 7.6% 하락했다고 보도했다. L&F는 Tesla향 high-nickel cathode 공급계약 예상가치가 29억 달러에서 7,386달러로 축소됐다고 밝혔다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return and contract-value anchors

LGES_stage4c_event_MAE_1D:
-7.6%

LGES_lost_expected_revenue:
13.5T won

LGES_2024_revenue:
25.62T won

lost_revenue_vs_2024_revenue:
13.5 / 25.62
= 52.7%

L&F_initial_contract_value:
$2.9B

L&F_revised_contract_value:
$7,386

L&F_contract_value_drawdown:
1 - 7,386 / 2,900,000,000
= 99.999745% collapse

stage3_price:
N/A for both

stock_OHLC:
price_data_unavailable_after_deep_search beyond reported event anchors
```

### alignment

```text
LGES_alignment = thesis_break
L&F_alignment = thesis_break
rerating_result = contract_quality_failure
stage_failure_type = false_green_prevention_case
```

### R13 판정

R3에서 `계약 headline`, `고객명`, `계약금액`은 Stage 3 충분조건이 아니다. **actual call-off, take-or-pay, GWh delivery, OPM, FCF**가 없으면 Green을 막아야 한다.

---

## Case F — 제주항공 `operational trust hard 4C`

```text
symbol = 089590
source_sector = R9
case_type = 4C-thesis-break
archetype = OPERATIONAL_TRUST_BREAK
```

### stage date

```text
Stage 1:
2023~2024
- LCC 여행수요 회복

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2024-12-30
- fatal crash
- 179명 사망
- 주가 장중 -15.7%
- 6,920원 record low
```

제주항공은 무안공항 사고 이후 장중 15.7% 하락해 6,920원까지 떨어졌고, 상장 이후 최저가를 기록했다. Reuters는 이 사고로 179명이 사망했고, 제주항공 시가총액이 최대 957억 원 증발했다고 보도했다. 같은 보도에서 AK홀딩스는 최대 12%, 한진·여행주 일부도 동반 하락했다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported price/event anchors

stage3_price:
N/A

stage4c_price_anchor:
6,920원

stage4c_event_MAE_1D:
-15.7%

implied_pre_event_reference_price:
6,920 / (1 - 0.157)
= 약 8,209원

market_cap_wipeout:
95.7B won

AK_Holdings_MAE:
-12%

Korean_Air_MAE:
-1.3%

Asiana_MAE:
-0.8%

Hanatour_MAE:
-7%

Very_Good_Tour_MAE:
-11%
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = operational_trust_break
stage_failure_type = hard_4C
```

### R13 판정

제주항공은 R13의 **operational trust hard 4C 기준점**이다. 여행수요가 좋아도 fatal accident가 나오면 Green은 즉시 차단해야 한다.

---

## Case G — 카카오페이 / stablecoin basket `price_moved_without_evidence`

```text
symbols = 377300 / LG CNS / Aton / ME2ON
source_sector = R6
case_type = overheat / price_moved_without_evidence
archetype = KRW_STABLECOIN_POLICY_THEME
```

### stage date

```text
Stage 1:
2025-06
- 원화 stablecoin policy 기대
- digital asset reform 기대

Stage 2:
없음 또는 약한 Stage 2
- 법안·정책 논의는 있었지만 회사별 수익모델 미확인

Stage 3:
없음

Stage 4B:
2025-06
- Kakao Pay >2배
- LG CNS +70%
- Aton +80%
- ME2ON 3배

Stage 4C:
규제 지연, 비은행 발행 제한, 외환리스크 우려 현실화 시 후보
```

FT는 원화 스테이블코인 기대 속에 Kakao Pay가 한 달 동안 두 배 이상, LG CNS가 약 70%, Aton이 80%, ME2ON이 세 배 올랐다고 보도했다. 같은 기사에서 정부의 구체적 crypto 규제 framework는 아직 명확하지 않고, 한국은행은 비은행 스테이블코인 발행이 통화정책과 자본흐름에 부담이 될 수 있다고 우려했다. ([Financial Times][7])

### 실제 가격경로 검증

```text
price_data_source:
FT reported return anchors

stage3_price:
N/A

Kakao_Pay_reported_MFE_month:
> +100%

LG_CNS_reported_MFE_month:
+70%

Aton_reported_MFE_month:
+80%

ME2ON_reported_MFE_month:
+200%

regulated_revenue:
not confirmed

issuer_license:
not confirmed

reserve_income:
not confirmed

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = stablecoin_policy_theme_overheat
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### R13 판정

stablecoin theme은 R6/R13에서 **가장 강한 event-premium 감점축**이다. 발행권·reserve income·수수료·규제자본이 나오기 전 Stage 3 금지다.

---

## Case H — 고려아연 `strategic-material success_candidate + governance/dilution RedTeam`

```text
symbol = 010130
source_sector = R4
case_type = success_candidate + event_premium + dilution_watch
archetype = STRATEGIC_MATERIALS_WITH_GOVERNANCE_OVERLAY
```

### stage date

```text
Stage 1:
2024-09~10
- MBK / YoungPoong control battle
- tender offer / buyback / governance event

Stage 2:
2025-12
- U.S. critical minerals smelter
- $7.4B Tennessee project
- U.S.-led supply-chain restructuring

Stage 3:
없음
- offtake, capex, FCF, dilution, project execution 확인 전 Green 금지

Stage 4B:
2024 control battle rally
2025 U.S. smelter event rally

Stage 4C-watch:
2024-10 / 2025-12
- share issuance / dilution concern
- governance battle
```

고려아연은 전략광물 관점에서 Stage 2 후보가 될 수 있다. 2025년 12월 미국 critical minerals refinery 계획은 74억 달러 규모이며, 법원이 해당 프로젝트 자금조달을 위한 19억 달러 신주발행 저지 요청을 기각하자 고려아연 주가는 최대 5% 상승했다. 그러나 Reuters는 이 신주발행이 약 10% 지분을 미국 정부 주도 JV에 넘기는 구조이며, MBK·영풍 측이 희석과 공정성 문제를 제기했다고 보도했다. 2024년에도 고려아연의 18억 달러 신주발행 계획은 금융감독원의 조사 대상이 됐다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event anchors

stage3_price:
N/A

U.S._smelter_project_value:
$7.4B

new_share_issue_for_project:
$1.9B

new_investor_stake:
around 10%

U.S._smelter_event_MFE:
+5%

YoungPoong_event_MAE:
-10.5%

2024_share_issue_plan:
about $1.8B

2024_regulator_action:
investigation / revision risk

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = success_candidate + event_premium + governance_watch
rerating_result = strategic_material_project_watch
stage_failure_type = stage2_evidence_not_green
```

### R13 판정

고려아연은 **좋은 전략자원 후보라도 governance/dilution이 붙으면 Stage 3를 늦게 줘야 한다**는 기준점이다.

---

# 5. 이번 R13 case별 요약표

| case                          | source R | 분류                           |                                                   실제 가격검증 | R13 판정            |
| ----------------------------- | -------: | ---------------------------- | --------------------------------------------------------: | ----------------- |
| SK하이닉스                        |       R2 | structural_success + 4B      | 222,000원 → 1,946,000원, +776.6%; 2025 +274%, 2026 +200% 이상 | Stage 3 성공, 현재 4B |
| 현대로템                          |       R1 | structural_success           |                           41,300원, +9.3%; KOSPI 대비 +9.6pp | Stage 3 후보 성공     |
| 한화에어로스페이스                     |       R1 | 4B-watch                     |                              3.6조 증자 후 -13%, 이미 YTD 2배 이상 | 4B이지 hard 4C 아님   |
| 한국가스공사                        |      R11 | price-only event             |                             38,700원, +30%; 시추 1회 1,000억 원 | Green 금지          |
| LGES / L&F                    |       R3 | hard 4C                      |           LGES -7.6%; 기대매출 손실 13.5조; L&F 계약가치 -99.999745% | contract 4C       |
| 제주항공                          |       R9 | hard 4C                      |                                6,920원, -15.7%, 시총 957억 증발 | safety hard 4C    |
| Kakao Pay / stablecoin basket |       R6 | price-only rally             |                                   Kakao Pay >2배, ME2ON 3배 | event premium     |
| 고려아연                          |       R4 | strategic + governance watch |          $7.4B smelter, +5%; $1.9B share issue, 10% stake | Stage 2, Green 보류 |

---

# 6. score-price alignment 판정

```text
aligned:
- SK하이닉스
- 현대로템

4B-watch_success:
- SK하이닉스 1조 달러 근접
- 한화에어로스페이스 증자 shock
- Kakao Pay / stablecoin basket
- 한국가스공사 resource event
- 고려아연 governance / U.S. smelter event

price_moved_without_evidence:
- 한국가스공사
- Kakao Pay stablecoin basket

thesis_break / hard_4C:
- 제주항공
- LGES
- L&F

success_candidate_but_not_green:
- 고려아연
- 두산에너빌리티류 policy-to-contract cases from R11
- NAV / digital asset / data center / strategic material projects

event_premium:
- 한국가스공사
- stablecoin basket
- 고려아연 governance battle
```

---

# 7. 점수비중 교정

## 올릴 축

```text
price_path_alignment +5
stage3_to_large_MFE_confirmation +5
order_to_revenue_conversion +5
eps_fcf_revision +5
actual_contract +5
customer_visibility +4
operational_trust +5
hard_4c_early_warning +5
contract_quality +5
```

### 왜 올리나

SK하이닉스는 HBM dominance와 EPS revision이 확인된 뒤 대형 MFE가 나왔고, 현대로템은 K2 납품·매출·OP revision이 주가 반응과 맞았다. 이 둘은 Stage 3가 잘 잡히면 실제 대형 수익률을 만들 수 있음을 보여준다. ([마켓워치][1])

## 내릴 축

```text
policy_news_only -5
resource_estimate_without_commerciality -5
stablecoin_policy_theme_only -5
AI_capex_or_partnership_without_revenue -4
contract_headline_without_calloff -5
MOU_or_preliminary_deal -5
governance_premium_only -5
dilution_without_clear_fcf -4
high_score_without_price_validation -5
```

### 왜 내리나

한국가스공사는 경제성·상업성 없이 장중 30% 상승했고, stablecoin basket은 실제 규제수익 전 2~3배 움직였다. L&F는 Tesla 고객명과 대형 계약 headline이 있었지만 계약가치가 거의 사라졌다. ([월스트리트저널][4])

## Green gate 강화 조건

```text
R13 공통 Stage 3-Green 필수:
1. 회사 단위 evidence가 있음
2. revenue / EPS / FCF로 내려오는 경로가 있음
3. price path가 evidence 이후 따라옴
4. Stage 3 이후 MFE가 의미 있게 큼
5. MAE가 과도하지 않음
6. 4B saturation 상태가 아님
7. hard RedTeam 없음
8. contract / operational / governance trust 통과
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~5배 이상 상승
시총 milestone이 headline화
대형 증자 / CB / share issue
뉴스 발표일 20~30% 급등
정책·MOU·자원발견·stablecoin 테마 급등
좋은 뉴스에도 주가 반응 둔화
valuation이 evidence보다 먼저 감

4B-elevated:
SK하이닉스처럼 시총 1조 달러 근접
한화에어로스페이스처럼 대시세 후 대형 증자
고려아연처럼 governance battle과 dilution이 반복
stablecoin처럼 실제 수익모델 전 2~3배 급등
```

## 4C hard gate 조건

```text
contract_cancellation
contract_value_collapse
fatal_safety_accident
operational_trust_break
major_governance_legal_break
privacy_or_security_trust_break
PF_workout_or_credit_break
regulatory_reversal
commercialization_failure
financing_failure
```

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_145.md 요약

```md
# R13 Loop 8. Cross-archetype RedTeam / 4B / Price Validation

이번 라운드는 R1~R12를 다시 검증한 R13 price-validation 라운드다.

핵심 결론:
- SK하이닉스와 현대로템은 Stage 3가 실제 대형 MFE를 만들 수 있음을 보여주는 aligned success다.
- SK하이닉스는 222,000원 Stage 3 anchor에서 1,946,000원 reported peak까지 +776.6% MFE가 확인된다. 현재는 신규 Stage 3가 아니라 4B-watch다.
- 현대로템은 K2 납품·매출·OP revision과 주가 +9.3%가 맞물린 R1 aligned success 후보다.
- 한화에어로스페이스 증자 shock은 4B-watch이지 hard 4C가 아니다.
- 한국가스공사 동해 가스 이벤트는 경제성·상업성 전 +30% price-only rally다.
- LGES와 L&F는 contract-quality hard 4C 기준점이다.
- 제주항공 fatal crash는 operational trust hard 4C 기준점이다.
- Kakao Pay / stablecoin basket은 실제 규제수익 전 2~3배 움직인 event premium이다.
- 고려아연은 strategic material 후보지만 governance/dilution overlay 때문에 Stage 3는 보류한다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 145 R13 Loop 8 Cross-archetype Price Validation

## 반영 내용
- R13 Loop 8 cross-archetype price-validation 라운드를 추가했다.
- Structural success, 4B timing, contract hard 4C, operational trust hard 4C, event premium, governance/dilution watch를 비교했다.
- Reuters/WSJ/FT/MarketWatch/Tom's Hardware reported anchors로 가능한 MFE/MAE 및 contract/event metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- price_path_alignment, stage3_to_large_MFE_confirmation, order_to_revenue_conversion, hard_4c_early_warning 강화
- policy_news_only, resource_estimate_without_commerciality, stablecoin_policy_theme_only, contract_headline_without_calloff 감점 강화
- 4B-watch와 hard 4C 구분 강화
```

## case row 초안

```jsonl
{"case_id":"r13_loop8_sk_hynix_hbm_stage3_4b","symbol":"000660","company_name":"SK하이닉스","source_sector":"R2","case_type":"structural_success","primary_archetype":"STRUCTURAL_SUCCESS_BUT_4B_WATCH","stage3_date":"2024-06-25","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"MarketWatch/Reuters/Tom's Hardware reported anchors","stage3_price":222000,"peak_price":1946000,"peak_return_from_stage3_pct":776.6,"reported_return_2025_pct":274,"reported_return_2026_ytd_pct":200,"minimum_compounded_return_from_2025_start_pct":1022,"market_cap_mfe_minimum_pct":842,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"HBM dominance and EPS revision produced large MFE; now 4B-watch."}
{"case_id":"r13_loop8_hyundai_rotem_k2_delivery_aligned","symbol":"064350","company_name":"현대로템","source_sector":"R1","case_type":"structural_success","primary_archetype":"ORDER_TO_REVENUE_CONVERSION","stage3_date":"2024-04-09","stage4b_date":"2025-08-01","price_validation":{"price_data_source":"WSJ/Reuters reported anchors","stage3_price":41300,"mfe_1d_pct":9.3,"implied_pre_event_reference_price":37786,"relative_outperformance_vs_kospi_pp":9.6,"k2_export_revenue_1q_krw_bn":270,"op_growth_estimate_pct":85,"poland_second_contract_usd_bn":6.5,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"defense_export_revenue_conversion","notes":"K2 delivery/revenue/OP revision aligned with price reaction."}
{"case_id":"r13_loop8_hanwha_aero_dilution_4b_not_4c","symbol":"012450","company_name":"한화에어로스페이스","source_sector":"R1","case_type":"4b_watch","primary_archetype":"CAPITAL_ALLOCATION_DILUTION_OVERLAY","stage4b_date":"2025-03-21","price_validation":{"price_data_source":"Reuters/FT reported anchors","stage3_price":null,"capital_raise_krw_trn":3.6,"event_mae_1d_pct":-13,"share_sale_price":605000,"discount_to_prior_close_pct":-16,"pre_event_ytd_status":"more_than_doubled","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"aligned_4B_detection","rerating_result":"true_rerating_with_dilution_watch","notes":"Large rally plus capital raise is 4B-watch/elevated, not hard 4C unless business thesis breaks."}
{"case_id":"r13_loop8_kogas_resource_price_only","symbol":"036460","company_name":"한국가스공사","source_sector":"R11","case_type":"event_premium","primary_archetype":"PRICE_ONLY_RALLY","stage1_date":"2024-06-03","stage4b_date":"2024-06-03","price_validation":{"price_data_source":"WSJ reported intraday price anchor","stage3_price":null,"event_peak_price":38700,"mfe_1d_pct":30.0,"implied_pre_event_reference_price":29769,"drilling_cost_per_attempt_krw_bn":100,"price_validation_status":"reported_event_anchor_not_stage3"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"resource_discovery_event_premium","notes":"Resource estimate and drilling approval are not commerciality."}
{"case_id":"r13_loop8_lges_lnf_contract_quality_4c","symbol":"373220/066970","company_name":"LG에너지솔루션/L&F","source_sector":"R3","case_type":"4c_thesis_break","primary_archetype":"CONTRACT_QUALITY_BREAK","stage4c_date":"2025-12-18/2025-12-29","price_validation":{"price_data_source":"Reuters reported event and contract-value anchors","stage3_price":null,"lges_mae_1d_pct":-7.6,"lges_lost_expected_revenue_krw_trn":13.5,"lges_lost_revenue_vs_2024_revenue_pct":52.7,"lnf_initial_contract_value_usd_bn":2.9,"lnf_revised_contract_value_usd":7386,"lnf_contract_value_drawdown_pct":-99.999745,"price_validation_status":"reported_event_and_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"contract_quality_failure","notes":"Contract headline/customer name without actual call-off must not become Green."}
{"case_id":"r13_loop8_jeju_air_operational_trust_hard_4c","symbol":"089590","company_name":"제주항공","source_sector":"R9","case_type":"4c_thesis_break","primary_archetype":"OPERATIONAL_TRUST_BREAK","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters reported price/event anchors","stage3_price":null,"stage4c_price_anchor":6920,"mae_1d_pct":-15.7,"implied_pre_event_reference_price":8209,"market_cap_wipeout_krw_bn":95.7,"ak_holdings_mae_pct":-12,"hanatour_mae_pct":-7,"very_good_tour_mae_pct":-11,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"operational_trust_break","notes":"Fatal crash is hard 4C and blocks any travel-demand Green."}
{"case_id":"r13_loop8_stablecoin_theme_price_only","symbol":"377300/LG_CNS/158430/ME2ON","company_name":"Kakao Pay / stablecoin basket","source_sector":"R6","case_type":"overheat","primary_archetype":"KRW_STABLECOIN_POLICY_THEME","stage1_date":"2025-06","stage4b_date":"2025-06","price_validation":{"price_data_source":"FT reported return anchors","stage3_price":null,"kakao_pay_mfe_month_pct":100,"lg_cns_mfe_month_pct":70,"aton_mfe_month_pct":80,"me2on_mfe_month_pct":200,"regulated_revenue_confirmed":false,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"stablecoin_policy_theme_overheat","notes":"Stablecoin policy rally occurred before issuer licensing/reserve income/fee revenue clarity."}
{"case_id":"r13_loop8_korea_zinc_strategic_governance_watch","symbol":"010130","company_name":"고려아연","source_sector":"R4","case_type":"success_candidate","primary_archetype":"STRATEGIC_MATERIALS_WITH_GOVERNANCE_OVERLAY","stage2_date":"2025-12","stage4b_date":"2025-12-24","price_validation":{"price_data_source":"Reuters reported event anchors","stage3_price":null,"us_smelter_project_usd_bn":7.4,"share_issue_for_project_usd_bn":1.9,"new_investor_stake_pct":10,"event_mfe_pct":5,"youngpoong_mae_pct":-10.5,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_event_premium_governance_watch","rerating_result":"strategic_material_project_watch","notes":"Strategic material project is Stage 2; offtake, FCF, dilution, governance and execution must clear before Green."}
```

## shadow weight row 초안

```csv
archetype,price_path_alignment,stage3_mfe_confirmation,order_to_revenue,eps_fcf_revision,actual_contract,contract_quality,operational_trust,event_penalty,governance_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
STRUCTURAL_SUCCESS_ALIGNED,+5,+5,+5,+5,+4,+3,+3,0,+0,+4,+2,SK Hynix and Hyundai Rotem show Stage 3 can create large MFE when evidence converts to earnings/revenue.
STRUCTURAL_SUCCESS_BUT_4B_WATCH,+5,+5,+4,+4,+4,+3,+3,-1,+2,+5,+3,SK Hynix now requires 4B-watch after market-cap milestone and crowding.
CAPITAL_ALLOCATION_DILUTION_OVERLAY,+2,+3,+2,+2,+2,+2,+2,-2,+5,+5,+3,Hanwha Aero capital raise after large rally is 4B-watch, not automatic 4C.
PRICE_ONLY_RALLY,+0,+0,+0,+0,+0,+0,+1,-5,+1,+5,+3,Korea Gas and stablecoin basket show price moved before revenue evidence.
CONTRACT_QUALITY_BREAK,+0,+0,+0,+0,+5,+5,+2,+0,+1,+3,+5,LGES and L&F show cancellation/value collapse hard 4C.
OPERATIONAL_TRUST_BREAK,+0,+0,+0,+0,+0,+1,+5,+0,+2,+3,+5,Jeju Air fatal crash is hard operational trust 4C.
KRW_STABLECOIN_POLICY_THEME,+0,+0,+0,+0,+0,+0,+2,-5,+3,+5,+4,Stablecoin policy rally is not Green until regulated revenue is visible.
STRATEGIC_MATERIALS_WITH_GOVERNANCE_OVERLAY,+2,+2,+2,+3,+3,+3,+2,-3,+5,+5,+4,Korea Zinc strategic project is Stage 2 but governance/dilution blocks Stage 3.
```

---

# 이번 R13 Loop 8 결론

R13의 결론은 분명하다.

```text
1. Stage 3는 잘 잡히면 진짜 대형 MFE를 만든다.
   SK하이닉스와 현대로템이 그 증거다.

2. 4B는 hard exit가 아니다.
   한화에어로스페이스 증자처럼 dilution shock이 있어도 business thesis가 살아 있으면 4B-watch/elevated다.

3. price_moved_without_evidence는 Green을 막아야 한다.
   한국가스공사와 stablecoin basket이 대표적이다.

4. 4C는 가볍게 쓰면 안 되지만,
   계약취소·계약가치 붕괴·fatal safety accident는 hard 4C다.
   LGES, L&F, 제주항공이 기준점이다.

5. 전략자원·디지털자산·정책·데이터센터는 Stage 2 후보가 될 수 있지만,
   offtake, revenue, FCF, governance, regulatory trust 전에는 Stage 3가 아니다.
```

한 문장으로 압축하면:

> **R13의 역할은 “좋아 보이는 후보”를 한 번 더 부수는 것이다. Stage 3는 대형 MFE로 증명되고, 4B는 가격 선반영·crowding·자본조달로 증명되며, 4C는 계약·안전·운영·규제·신뢰 훼손으로 증명된다.**

[1]: https://www.marketwatch.com/story/sk-hynix-s-hbm-dominance-higher-chip-prices-could-lift-earnings-market-talk-6508cbf8?utm_source=chatgpt.com "SK Hynix's HBM Dominance, Higher Chip Prices Could Lift Earnings -- Market Talk"
[2]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com "Hyundai Rotem Rallies on Hopes Tank Exports Will Boost Earnings"
[3]: https://www.reuters.com/business/aerospace-defense/south-korea-market-watchdog-orders-hanwha-aerospace-revise-share-issuance-plan-2025-03-27/?utm_source=chatgpt.com "S. Korea watchdog blocks Hanwha Aerospace $2.5 billion capital raising plan"
[4]: https://www.wsj.com/articles/korea-gas-leads-energy-rally-on-seoul-s-offshore-oil-drilling-approval-c8c4d428?utm_source=chatgpt.com "Korea Gas Leads Energy Rally on Seoul's Offshore Oil Drilling Approval"
[5]: https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com "LG Energy Solution cancels 3.9 trillion won battery order with Freudenberg"
[6]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[7]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"
[8]: https://www.reuters.com/world/asia-pacific/south-korean-court-rejects-injunction-request-block-korea-zincs-share-sale-2025-12-24/?utm_source=chatgpt.com "South Korean court rejects bid to block Korea Zinc share sale funding US smelter"
