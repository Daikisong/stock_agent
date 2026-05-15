좋아. 정해둔 순서대로 이번은 **R6 — 금융·자본배분·디지털금융**으로 넘어간다.

R6는 이름만 보면 “은행·보험·증권·밸류업·스테이블코인”이라 단순해 보이지만, 실제 점수정규화는 꽤 까다롭다. 이유는 이 대섹터가 **EPS 폭발형**이 아니라 대체로 **ROE/PBR 재평가, 자본배분, 규제 승인, 반복 금융 인프라 매출**로 움직이기 때문이다.

업로드된 Theme Tag Map v0.5에서도 R6는 은행, 금융지주, 손해보험, 생명보험, 증권사, VC, 고배당, 밸류업, 결제서비스, 토스, 신용정보, STO, 스테이블코인을 흡수하는 대섹터로 정리되어 있고, 은행·금융지주·손해보험은 Green 가능, 증권·VC는 Watch, STO·스테이블코인은 규제와 실제 발행·수익모델 전까지 Watch로 구분되어 있다.

서생원식으로 보면 R6의 질문은 이거다. “저PBR이라 싸다”가 아니라, **ROE/FCF/환원정책/지배구조가 바뀌면서 시장이 과거의 Korea discount 프레임을 버리는가**다. 단순 고배당, 저PBR, 밸류업 지수 편입, 스테이블코인 뉴스만으로는 Stage 3-Green이 아니다.

---

# R6. 금융·자본배분·디지털금융

## 1. 이번 라운드 대섹터

```text
R6 = 금융·자본배분·디지털금융
```

R6의 기본 구조는 세 갈래다.

```text
1. 전통 금융 리레이팅형
은행 / 금융지주 / 보험
→ ROE, CET1, K-ICS, CSM, 손해율, credit cost
→ 배당·자사주·소각
→ PBR-ROE 프레임 변화

2. 자본배분·지배구조형
저PBR / 지주 / NAV discount / 밸류업
→ 실제 자사주 소각, 배당, ROE 개선, governance 개선
→ Korea discount 축소

3. 디지털금융 인프라형
결제 / PG / e-wallet / 신용정보 / STO / 스테이블코인
→ 규제 승인, 거래액, take rate, 반복 수수료, 보안 안정성
→ 금융 인프라 매출화
```

이 라운드의 핵심은 **이익 체급 변화가 EPS 폭발이 아니라 “할인 요인 제거”에서 나오는 경우가 많다**는 점이다.

---

## 2. 대상 canonical archetype

| 구분              | canonical archetype                | Green 정책       |
| --------------- | ---------------------------------- | -------------- |
| 은행·금융지주         | `FINANCIAL_SPREAD_BALANCE_SHEET`   | Green 가능       |
| 보험 underwriting | `INSURANCE_UNDERWRITING_CYCLE`     | Green 가능       |
| 증권·브로커리지        | `SECURITIES_BROKERAGE_CYCLE`       | Watch          |
| 주주환원·밸류업        | `VALUE_UP_SHAREHOLDER_RETURN`      | Watch-to-Green |
| 지주·NAV discount | `HOLDING_RESTRUCTURING_GOVERNANCE` | Watch-to-Green |
| 결제·PG·e-wallet  | `PAYMENT_FINTECH_INFRA`            | Watch-to-Green |
| STO·스테이블코인      | `DIGITAL_ASSET_TOKENIZATION`       | Watch          |
| 신용정보·데이터 금융     | `CREDIT_DATA_INFRA`                | Watch-to-Green |
| VC·회수시장         | `VC_EXIT_MARKET_CYCLE`             | Watch/Red      |
| 디지털자산 테마·NFT    | `DIGITAL_ASSET_THEME_OVERHEAT`     | Red/Watch      |

---

## 3. deep sub-archetype

```text
FINANCIAL_SPREAD_BALANCE_SHEET
- 은행
- 금융지주
- NIM
- CET1
- credit cost
- PF exposure
- corporate loan growth
- PBR-ROE 리레이팅

INSURANCE_UNDERWRITING_CYCLE
- 손해보험
- 생명보험
- CSM
- K-ICS
- 손해율
- 자본비율
- 보증보험
- 사이버 운영 리스크

SECURITIES_BROKERAGE_CYCLE
- 증권사
- 브로커리지
- 거래대금
- IB / IPO / ECM / DCM
- 자기자본 운용손익
- PF·대체투자 손실
- VC exit market

VALUE_UP_SHAREHOLDER_RETURN
- 고배당
- 자사주 매입
- 자사주 소각
- treasury share cancellation
- 배당소득세 개편
- 밸류업 지수
- capital allocation

HOLDING_RESTRUCTURING_GOVERNANCE
- 지주회사
- NAV discount
- 자회사 가치
- 공개매수
- 경영권 분쟁
- activist campaign
- governance discount

PAYMENT_FINTECH_INFRA
- 결제서비스
- PG
- e-wallet
- Toss
- GCash
- Stripe류
- 거래액
- take rate
- 부가 금융서비스

DIGITAL_ASSET_TOKENIZATION
- 스테이블코인
- 원화 stablecoin
- STO
- 토큰증권
- 수탁
- 정산
- 결제망 채택
- 규제 승인

CREDIT_DATA_INFRA
- 신용정보
- 신용평가
- 데이터 매출
- 금융기관 반복계약

DIGITAL_ASSET_THEME_OVERHEAT
- NFT
- 코인 관련주
- 알고리즘 스테이블코인
- 실질 매출 없는 블록체인 테마
```

---

# 4. 성공사례

## 4-1. 한국 Commercial Act 개정 — `VALUE_UP_SHAREHOLDER_RETURN`

한국 국회는 2026년 2월 상장사가 새로 취득한 자사주를 1년 안에 소각하도록 하는 상법 개정안을 통과시켰다. Reuters는 이 개정이 Korea Discount를 줄이기 위한 정책이며, 코스피가 1년 사이 두 배 이상 오르고 6,000선을 처음 돌파했다고 보도했다. 이건 R6 전체의 Stage 1~2 배경으로 매우 중요하다. 단순 “밸류업 기대”가 아니라, 자사주가 지배력 강화 도구로 쓰이던 loophole을 막고 소각을 강제하는 쪽으로 정책이 바뀌었기 때문이다. ([Reuters][1])

**가격경로 1차 판정**

```text
가격 반응:
코스피가 1년 사이 2배 이상 상승했고, 6,000선 돌파 보도 확인.

판정:
macro_policy_aligned_candidate

의미:
정책 자체가 R6의 valuation rerating background로 작동.
하지만 개별 종목은 실제 소각·배당·ROE 개선을 따로 검증해야 함.
```

**점수 교정**

```text
VALUE_UP_SHAREHOLDER_RETURN:
valuation_rerating과 capital_allocation 점수 강화.

단, 지수 편입/정책 기대만으로 Green 금지.
실제 소각·배당·ROE 개선 필요.
```

---

## 4-2. 배당세·주주보호 개혁 — `VALUE_UP_SHAREHOLDER_RETURN`

2025년 6월 한국 정부는 배당 확대를 유도하기 위한 세제 개편과 주주보호 강화 방안을 추진했다. Reuters는 이 뉴스 이후 코스피가 1.23% 올라 2022년 1월 이후 최고 수준인 2,907.04를 기록했다고 보도했다. 이는 “주주환원 정책 변화 → 시장 리레이팅 기대 → 가격 반응”의 초기 사례로 볼 수 있다. ([Reuters][2])

**가격경로 1차 판정**

```text
가격 반응:
정책 뉴스 후 KOSPI +1.23%

판정:
Stage1_policy_price_aligned

의미:
value-up policy는 시장 전체 PBR/PER band 변화의 촉매가 될 수 있음.
다만 개별 종목에서는 실행 여부 확인 필요.
```

---

## 4-3. SK Square 자사주 소각·추가 매입 — `HOLDING_RESTRUCTURING_GOVERNANCE`

SK Square는 SK하이닉스 지분 20%를 가진 지주회사인데, Reuters에 따르면 회사의 시장가치는 보유한 SK하이닉스 지분 가치의 절반에도 못 미쳤다. SK Square는 기존 1,000억 원어치 자사주 소각과 추가 1,000억 원 자사주 매입·소각 계획을 발표했고, 독립이사 선임도 추진했다. 이건 `HOLDING_RESTRUCTURING_GOVERNANCE`에서 **NAV discount + 실제 소각 + governance 개선**이 함께 있는 성공 후보 사례다. ([Reuters][3])

**가격경로 1차 판정**

```text
판정:
holding_valueup_success_candidate

가격 확인:
보도 단위에서 즉시 주가 반응 수치는 부족.
stage2_date = 2024-11-21로 잡고 price backfill 필요.

의미:
저PBR/저NAV 자체가 아니라 실제 소각과 독립이사, NAV discount 축소 가능성이 점수 근거.
```

**점수 교정**

```text
Market Mispricing: 강함
Valuation Rerating: 강함
Capital Allocation: 강함
EPS/FCF: 직접 영업보다는 자회사 가치/NAV 중심
Risk: 자회사 주가 의존, 지주 discount 지속, 소각 규모 부족
```

---

## 4-4. 삼성전자 자사주 매입 — `VALUE_UP_SHAREHOLDER_RETURN`의 mixed case

삼성전자는 2024년 11월 10조 원, 약 72억 달러 규모의 자사주 매입 계획을 발표했고, 이 중 3조 원어치는 3개월 내 매입 후 소각한다고 밝혔다. Reuters는 삼성전자 주가가 발표 당일 7.2% 반등했지만, 여전히 연초 대비 32% 하락한 상태였고, 애널리스트들은 주가를 더 지지하려면 구체적인 사업계획이 필요하다고 봤다고 보도했다. ([Reuters][4])

**가격경로 1차 판정**

```text
가격 반응:
발표 당일 +7.2%

판정:
buyback_price_aligned_but_business_risk_remaining

의미:
소각은 단기 가격 반응을 만들 수 있음.
하지만 사업 펀더멘탈, AI/HBM 경쟁력, 이익 경로가 없으면 지속 리레이팅은 제한.
```

**점수 교정**

```text
Capital Allocation: 강화
Valuation Rerating: 단기 강화
EPS/FCF: 별도 확인 필요
Risk: buyback-only, business thesis weakness
```

---

## 4-5. 금융지주·은행 — `FINANCIAL_SPREAD_BALANCE_SHEET`

한국 금융지주·은행은 R6에서 Green 가능성이 있는 축이다. Theme Map 기준으로 은행·금융지주는 ROE, CET1, 환원, credit cost를 핵심 증거로 한다.

2025~2026년 Korea Discount 해소 정책, 배당세 개편, 자사주 소각 강제, 주주보호 강화가 결합되면서 은행·금융지주는 기존 “저PBR value trap”에서 “ROE/PBR rerating 후보”로 바뀔 수 있다. 다만 Green은 다음이 있어야 한다.

```text
ROE 유지 또는 개선
CET1 안정
credit cost 낮음
PF·부동산 익스포저 관리
실제 배당·자사주·소각
PBR band 상승
```

**가격경로 1차 판정**

```text
판정:
sector_success_candidate

검증 필요:
KB, 신한, 하나, 우리별 PBR band 변화
2025~2026 KOSPI/금융업지수 대비 상대수익률
배당/자사주 실행일 이후 MFE/MAE
```

---

## 4-6. GCash / Mynt — `PAYMENT_FINTECH_INFRA`

필리핀 e-wallet GCash 운영사 Mynt는 결제·e-wallet archetype의 좋은 참고 성공 후보다. Reuters는 Mynt가 2026년 IPO에서 최소 80억 달러 valuation을 목표로 하고, GCash가 약 1억 2천만 인구의 필리핀에서 9,400만 명 사용자를 보유하며, bill payment, 송금, 저축, 대출, 보험 접근을 제공한다고 보도했다. 이건 단순 결제 앱이 아니라 **e-wallet → 금융서비스 플랫폼**으로 확장되는 구조다. ([Reuters][5])

**가격경로 1차 판정**

```text
판정:
payment_platform_success_reference

주의:
비상장/해외 reference.
사용자 수만으로 Green 금지.
실제 거래액, take rate, 금융서비스 수익, 연체율, FCF 확인 필요.
```

**점수 교정**

```text
Structural Visibility: 중간~강함
EPS/FCF: 실제 흑자/FCF 확인 전 중간
Risk: credit loss, regulation, security, take rate pressure
```

---

## 4-7. Toss 원화 스테이블코인·글로벌 확장 — `PAYMENT_FINTECH_INFRA` / `DIGITAL_ASSET_TOKENIZATION`

Toss는 한국 디지털금융의 대표 성공 후보이지만, 아직 Green은 아니다. Reuters는 Toss가 2025년 말 호주 진출을 시작으로 해외 확장을 추진하고, 규제가 허용되면 원화 스테이블코인을 발행하려 한다고 보도했다. Toss는 한국에서 3,000만 명 이상 사용자를 보유하고, 미국 IPO를 준비 중이며 100억~150억 달러 valuation이 거론된다고 했다. ([Reuters][6])

**가격경로 1차 판정**

```text
판정:
fintech_success_candidate + stablecoin_watch

의미:
Toss super app / 금융서비스 경쟁력은 성공 후보.
원화 스테이블코인은 규제 승인 전까지 Stage 1~2 Watch.
```

**점수 교정**

```text
PAYMENT_FINTECH_INFRA:
거래액, 사용자 retention, 금융서비스 attach, 흑자/FCF가 중요.

DIGITAL_ASSET_TOKENIZATION:
규제 승인, 발행량, 거래량, 수수료 모델 전까지 Green 금지.
```

---

# 5. 반례

## 5-1. Samsung C&T activist proposal rejection — `HOLDING_RESTRUCTURING_GOVERNANCE`

삼성물산은 행동주의 투자자들의 배당·자사주 확대 요구를 거부했고, FT는 이 결정 이후 삼성물산 주가가 거의 10% 하락했다고 보도했다. 이 사례는 R6에서 매우 중요하다. 저PBR·지주·자산가치가 있어도 **지배구조와 자본배분 실행이 없으면 value-up thesis가 깨질 수 있다.** ([Financial Times][7])

**교훈**

```text
NAV discount 자체
≠ Green

Green 조건:
실제 소각
배당 확대
소수주주 보호
지배구조 개선

반례 조건:
행동주의 요구 거부
자본배분 후퇴
지배주주 우선 구조
```

**가격경로 1차 판정**

```text
가격 반응:
주가 약 -10% 보도

판정:
governance_execution_failure_4c_watch
```

---

## 5-2. Korea Zinc 공개매수·자사주 이벤트 — `HOLDING_RESTRUCTURING_GOVERNANCE`

Korea Zinc는 경영권 분쟁과 자사주 매입 이벤트로 주가가 크게 움직였다. Reuters는 한국 법원이 Young Poong의 자사주 공개매수 금지 가처분을 기각하자 Korea Zinc 주가가 6.4% 올라 877,000원에 마감했고, 이는 공개매수가 890,000원에 근접한 수준이라고 보도했다. 동시에 Korea Zinc의 debt-to-equity ratio가 4배로 뛸 수 있다는 우려도 제기됐다. ([Reuters][8])

**교훈**

```text
공개매수·자사주 이벤트
≠ 구조적 value-up

이건 우선:
event_premium
governance_battle
capital_structure_risk
로 분류해야 한다.
```

**가격경로 1차 판정**

```text
가격 반응:
+6.4%, 공개매수가 근접

판정:
event_premium + governance_watch

의미:
자본배분이 소수주주 가치 제고인지, 경영권 방어인지 분리해야 함.
```

---

## 5-3. 세금 정책 shock — `VALUE_UP_SHAREHOLDER_RETURN` / `SECURITIES_BROKERAGE_CYCLE`

밸류업 정책은 긍정적일 수 있지만, 세금 정책은 시장 전체와 증권사 거래대금에 부정적 충격을 줄 수 있다. 2025년 8월 한국 주식시장은 새 세금 정책 제안으로 코스피가 3.9% 하락했고, 이는 4월 이후 최대 낙폭이었다. MarketWatch는 대주주 양도세 기준 하향, 법인세·배당세·거래세 인상 우려가 시장 랠리를 꺾었다고 설명했다. ([마켓워치][9])

**교훈**

```text
증권사·거래대금·밸류업:
정책 민감도가 큼.

Green 조건:
거래대금 증가 + IB 회복 + PF 리스크 낮음 + 자본환원.

4C-watch:
거래세 인상
대주주 과세 강화
투자심리 급랭
거래대금 급감
```

**가격경로 1차 판정**

```text
가격 반응:
KOSPI -3.9%

판정:
policy_tax_shock_4c_watch
```

---

## 5-4. 삼성전자 자사주 mixed case — buyback-only risk

삼성전자는 자사주 매입 발표 후 주가가 7.2% 반등했지만, Reuters는 회사가 AI칩 공급 경쟁에서 뒤처진 실적 우려와 HBM 경쟁력 문제를 겪고 있었고, 자사주만으로는 장기 주가를 지탱하기 어렵다는 분석을 전했다. ([Reuters][4])

**교훈**

```text
자사주 매입
≠ 구조적 Green

소각은 점수 강화.
하지만 사업 경쟁력·EPS 경로가 없으면 단기 반등에 그칠 수 있음.
```

---

## 5-5. TerraUSD / Do Kwon — `DIGITAL_ASSET_TOKENIZATION` hard 4C

알고리즘 스테이블코인 TerraUSD/Luna 붕괴는 디지털자산 archetype의 대표 hard 4C다. Reuters는 TerraUSD·Luna 붕괴로 약 400억 달러 규모 손실이 발생했고, Do Kwon이 투자자를 오도한 혐의로 미국에서 형사 절차를 밟았다고 보도했다. ([Reuters][10])

**교훈**

```text
Stablecoin
≠ 모두 같은 위험

fiat-backed, fully reserved, regulated stablecoin
과
algorithmic stablecoin
은 완전히 다른 archetype으로 봐야 함.
```

**가격경로 1차 판정**

```text
판정:
algorithmic_stablecoin_thesis_break

의미:
스테이블코인 관련주는 규제·준비금·상환능력·유동성·시장조작 리스크를 강하게 봐야 함.
```

---

## 5-6. Stablecoin convertibility risk

Bank of England 총재 Andrew Bailey는 stablecoin이 위기 시 실제 달러로 전환되는 방식과 국제 규제 기준을 둘러싼 위험을 경고했다. Reuters는 Bailey가 stablecoin이 cross-border payments에 널리 쓰이면 systemic risk가 커질 수 있고, convertibility obligation이 약하면 run 상황에서 문제가 된다고 우려했다고 보도했다. ([Reuters][11])

**교훈**

```text
스테이블코인 Green 조건:
규제 승인
준비금 투명성
상환 가능성
유동성
거래량
수익모델

Green 금지:
convertibility 불명확
알고리즘 구조
준비금·상환 리스크
```

---

# 6. 4B-watch 사례

## 6-1. Korea value-up crowded trade

한국 상법 개정과 주주환원 정책은 R6 전체에 긍정적이지만, 코스피가 1년 사이 두 배 이상 오르고 6,000을 돌파한 구간에서는 **value-up crowded trade**를 감시해야 한다. ([Reuters][1])

```text
4B 조건:
- 모두가 Korea discount 해소를 인정
- 저PBR주 전반 동반 급등
- 실제 소각·배당보다 PBR band가 먼저 오름
- 금융·지주·보험주 목표가 과밀 상향
```

---

## 6-2. 밸류업 지수 편입 4B-watch

```text
4B 조건:
- 지수 편입만으로 주가 상승
- 실제 ROE/배당/소각 변화 없음
- PBR만 과거보다 올라감
```

밸류업은 지수 편입이 아니라 실제 자본배분 실행이 핵심이다. Theme Map에서도 “밸류업 지수 편입”은 Watch로 분류되어 있고, 편입 자체보다 환원 실행을 보라고 되어 있다.

---

## 6-3. Stablecoin/STO 4B-watch

```text
4B 조건:
- 법안 발의만으로 관련주 동반 급등
- 실제 발행량·거래량·수익모델 없음
- 관련주 지분 구조 불명확
- STO 플랫폼 이름만 붙음
```

Toss의 원화 스테이블코인 추진은 후보지만, 규제 승인 전까지는 Watch다. ([Reuters][6])

---

## 6-4. Payment fintech valuation 4B

GCash/Mynt처럼 사용자 수와 금융서비스 확장이 강한 기업도, IPO valuation이 실제 take rate·수익성·연체율보다 앞서가면 4B-watch가 필요하다. Mynt는 9,400만 사용자와 80억 달러 IPO valuation 목표를 가지고 있지만, 시장상황과 규제 승인을 전제로 한다. ([Reuters][5])

---

# 7. 4C-thesis-break 사례

## 7-1. 자사주 미소각·governance failure

```text
4C:
자사주 매입 후 미소각
행동주의 제안 거부
소수주주 보호 실패
지배주주 방어 목적 자사주 활용
```

Samsung C&T의 activist proposal rejection과 주가 하락은 지주·value-up thesis의 대표 4C-watch다. ([Financial Times][7])

---

## 7-2. 경영권 이벤트로 인한 부채·자본구조 악화

```text
4C-watch:
공개매수·자사주 방어
부채비율 급등
governance battle 장기화
minority shareholder conflict
```

Korea Zinc 사례는 자사주와 공개매수가 항상 value-up이 아니라, 경영권 방어 이벤트일 수도 있음을 보여준다. ([Reuters][8])

---

## 7-3. 거래세·양도세 shock

```text
4C-watch:
세금 정책으로 거래대금 감소
증권사 브로커리지 수익 둔화
시장 sentiment 악화
```

세금 개편 우려로 코스피가 3.9% 하락한 사례는 증권사와 value-up rally에 대한 hard macro-policy watch다. ([마켓워치][9])

---

## 7-4. Algorithmic stablecoin collapse

```text
4C:
de-peg
run
reserve failure
fraud / market manipulation
regulatory prosecution
```

TerraUSD/Luna 붕괴는 디지털자산 archetype에서 절대 잊으면 안 되는 hard 4C다. ([Reuters][10])

---

## 7-5. Stablecoin convertibility failure

```text
4C-watch:
상환 불능
crypto exchange 경유 상환
준비금 불투명
liquidity run
국제 규제 충돌
```

Bailey의 stablecoin convertibility 경고는 fiat-backed stablecoin도 규제와 상환 구조를 확인해야 함을 보여준다. ([Reuters][11])

---

# 8. 점수비중 보정표 — R6 v1.0

| canonical archetype                | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | 핵심 감점                    |
| ---------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ------------------------ |
| `FINANCIAL_SPREAD_BALANCE_SHEET`   |      15 |         20 |          5 |         15 |        25 |      10 |    5 | credit cost, PF, CET1 악화 |
| `INSURANCE_UNDERWRITING_CYCLE`     |      15 |         21 |          4 |         15 |        25 |      10 |    5 | 손해율, K-ICS, cyber/운영 리스크 |
| `SECURITIES_BROKERAGE_CYCLE`       |      18 |         14 |          5 |         15 |        18 |       8 |    5 | 거래대금 급감, PF, 자기자본 손실     |
| `VALUE_UP_SHAREHOLDER_RETURN`      |      12 |         18 |          4 |         20 |        25 |      10 |    5 | 실행 부재, 미소각, 낮은 ROE       |
| `HOLDING_RESTRUCTURING_GOVERNANCE` |      12 |         17 |          4 |         22 |        24 |      10 |    5 | 지배주주 리스크, event premium  |
| `PAYMENT_FINTECH_INFRA`            |      18 |         20 |          8 |         14 |        14 |       2 |    5 | take rate 압박, 보안, 연체     |
| `DIGITAL_ASSET_TOKENIZATION`       |      16 |         18 |          8 |         16 |        12 |       3 |    5 | 규제, 유동성, convertibility  |
| `CREDIT_DATA_INFRA`                |      17 |         19 |          7 |         13 |        12 |       1 |    5 | 개인정보, 규제, 고객집중           |
| `VC_EXIT_MARKET_CYCLE`             |      16 |         11 |          4 |         12 |        10 |       2 |    5 | IPO 시장 둔화, 평가손실          |
| `DIGITAL_ASSET_THEME_OVERHEAT`     |       5 |          5 |          5 |          6 |         5 |       0 |    3 | 실질매출 부재, de-peg, NFT식 과열 |

---

# 9. stage date 후보

## `FINANCIAL_SPREAD_BALANCE_SHEET`

```text
Stage 1:
Korea discount 해소 정책, 배당세 개편, 주주보호 개정, 금융주 PBR 재평가 뉴스

Stage 2:
ROE 개선, CET1 안정, credit cost 하락, 배당·자사주 발표

Stage 3:
PBR-ROE 프레임 전환, 반복 환원정책, ROE 유지, credit risk 안정

Stage 4B:
금융주 PBR이 과거 band를 크게 넘고 value-up crowded trade가 형성

Stage 4C:
credit cost 상승, PF 손실, CET1 악화, 환원정책 후퇴
```

## `INSURANCE_UNDERWRITING_CYCLE`

```text
Stage 1:
손해율 개선, CSM 증가, value-up 기대

Stage 2:
ROE 개선, K-ICS 안정, 배당·자사주 실행

Stage 3:
PBR-ROE 재평가와 반복 환원 확인

Stage 4B:
보험 value-up이 모두에게 인정되어 PBR이 정상화

Stage 4C:
손해율 악화, 자본비율 훼손, 대체투자 손실, 사이버 운영 리스크
```

## `SECURITIES_BROKERAGE_CYCLE`

```text
Stage 1:
거래대금 증가, 증시 랠리, IPO/IB 회복 기대

Stage 2:
브로커리지 수익 증가, IB fee 증가, OP/EPS 상향

Stage 3:
PF 리스크 낮고 ROE 구조 개선이 확인될 때만

Stage 4B:
거래대금 peak, 증권주 동반 과열

Stage 4C:
거래세/양도세 shock, 거래대금 급감, PF 손실, 자기자본 운용손실
```

## `VALUE_UP_SHAREHOLDER_RETURN`

```text
Stage 1:
상법 개정, 배당세 개편, 밸류업 지수, 자사주 정책 뉴스

Stage 2:
실제 자사주 소각, 배당 확대, ROE 개선 확인

Stage 3:
PBR/NAV discount 축소와 반복 환원정책 확인

Stage 4B:
value-up narrative가 과밀하고 PBR band가 이미 크게 상승

Stage 4C:
미소각, 행동주의 거부, 자본배분 후퇴, 지배주주 리스크
```

## `PAYMENT_FINTECH_INFRA`

```text
Stage 1:
사용자 수 증가, 해외 진출, 결제·송금·금융서비스 확장 뉴스

Stage 2:
거래액, take rate, 금융서비스 attach, 흑자/FCF 확인

Stage 3:
반복 금융 인프라 매출과 규제 안정성 확인

Stage 4B:
IPO valuation 과열, 사용자 수 narrative 과밀

Stage 4C:
보안사고, 연체율 상승, take rate 하락, 규제 제재
```

## `DIGITAL_ASSET_TOKENIZATION`

```text
Stage 1:
스테이블코인/STO 법안, 사업 진출, 제휴 뉴스

Stage 2:
규제 승인, 실제 발행량, 거래량, 수수료 모델 확인

Stage 3:
결제·수탁·정산 인프라로 고착되고 반복 매출이 확인될 때

Stage 4B:
법안 기대만으로 관련주 동반 급등

Stage 4C:
de-peg, convertibility failure, 준비금 문제, 규제 불허, fraud
```

---

# 10. 가격경로 검증계획

## R6 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. ROE, PBR, CET1, CSM, 손해율, 배당, 자사주, 거래대금, take rate, stablecoin volume과 가격 경로를 비교한다.
```

## R6에서 반드시 분리할 판정

```text
aligned:
ROE/PBR/환원정책/거래액이 실제 가격 리레이팅과 동행.

policy_rerating:
정책 변화로 sector 전체가 리레이팅되었지만 개별 실행 검증은 필요.

buyback_only_rebound:
자사주 발표로 단기 반등했지만 사업·ROE 변화가 없음.

event_premium:
공개매수, 경영권 분쟁, IPO 기대만으로 상승.

false_positive_score:
저PBR/밸류업 기대는 있었지만 소각·배당·ROE 개선이 없음.

thesis_break:
governance failure, de-peg, stablecoin run, tax shock, credit cost spike.
```

## 이번 R6에서 우선 검증할 가격 case

| case_id                                           | stage2 후보일 | 현재 1차 가격판정                                    |
| ------------------------------------------------- | ---------: | --------------------------------------------- |
| `korea_commercial_act_treasury_share_cancel_case` | 2026-02-25 | KOSPI 6,000 돌파, macro policy aligned          |
| `korea_dividend_tax_reform_case`                  | 2025-06-11 | KOSPI +1.23%, Stage1 policy aligned           |
| `sk_square_buyback_cancel_case`                   | 2024-11-21 | holding value-up candidate, price backfill 필요 |
| `samsung_electronics_buyback_mixed_case`          | 2024-11-15 | +7.2%, buyback aligned but business risk      |
| `samsung_ct_activist_rejection_case`              |       2024 | 약 -10%, governance failure watch              |
| `korea_zinc_buyback_event_case`                   | 2024-10-21 | +6.4%, event premium                          |
| `korea_tax_policy_shock_case`                     | 2025-08-01 | KOSPI -3.9%, policy 4C-watch                  |
| `mynt_gcash_payment_platform_case`                | 2026-05-14 | payment platform reference, 비상장               |
| `toss_won_stablecoin_case`                        | 2025-09-09 | fintech success + stablecoin watch            |
| `terrausd_do_kwon_collapse_case`                  |  2022~2025 | algorithmic stablecoin hard 4C                |
| `boe_stablecoin_convertibility_warning_case`      | 2026-05-08 | stablecoin regulatory 4C-watch                |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R6 case library에는 아래 필드가 필요하다.

```text
case_id
symbol
company_name
primary_archetype
secondary_archetypes

stage1_date
stage2_date
stage3_date
stage4b_date
stage4c_date

stage1_price
stage2_price
stage3_price
stage4b_price
stage4c_price
peak_price

MFE_30D
MFE_90D
MFE_180D
MFE_1Y
MFE_2Y

MAE_30D
MAE_90D
MAE_180D
MAE_1Y

drawdown_after_peak
below_stage3_price_flag

roe
roa
pbr
cet1_ratio
k_ics_ratio
csm_growth
loss_ratio
credit_cost
pf_exposure

dividend_payout_ratio
dividend_growth
buyback_amount
buyback_cancelled_flag
treasury_share_cancel_deadline
shareholder_return_policy

trading_value
brokerage_revenue
ib_fee_revenue
ipo_pipeline_count
vc_exit_volume
proprietary_trading_gain_loss

payment_volume
take_rate
active_users
merchant_count
financial_service_attach_rate
credit_loss_rate
security_incident_flag

stablecoin_issued_amount
stablecoin_transaction_volume
redemption_reserve_ratio
convertibility_risk_flag
regulatory_approval_flag
depeg_event_flag

governance_event_flag
activist_campaign_flag
tender_offer_flag
minority_shareholder_protection_flag

score_price_alignment
price_validation_status
```

---

# R6 결론

R6는 “싼 금융주”를 찾는 라운드가 아니다. 핵심은 **할인 요인이 실제로 제거되는지**다.

```text
Green 가능:
은행·금융지주
손해보험
일부 생명보험
실제 소각·배당·ROE 개선이 있는 value-up
NAV discount 축소가 실행되는 지주

Watch-to-Green:
증권사
결제·PG·e-wallet
신용정보
Toss류 fintech
STO·스테이블코인

Red/4C 방어 중심:
NFT·코인 테마
알고리즘 스테이블코인
자사주 미소각
governance failure
세금 정책 shock
PF·credit cost spike
```

**R6 점수정규화의 핵심 문장:**

> 금융·자본배분·디지털금융은 “저PBR”이나 “밸류업”이라는 이름이 아니라 **ROE, 자본비율, 손해율, credit cost, 실제 자사주 소각, 배당, 거래액, take rate, 규제 승인, stablecoin 상환 안정성**으로 봐야 한다.
> 정책 기대와 사용자 수는 Stage 1이고, 실제 환원·수익모델·가격경로가 확인되어야 Stage 3 후보가 된다.

다음에 네가 “다음 라운드 진행해줘”라고 하면, 정해둔 순서에 따라 **R7 — 바이오·헬스케어·의료기기**로 넘어간다.

[1]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-parliament-approves-commercial-act-revision-aimed-boosting-share-2026-02-25/?utm_source=chatgpt.com "South Korea parliament approves commercial act revision aimed at boosting share valuations"
[2]: https://www.reuters.com/world/asia-pacific/south-korea-revamp-tax-scheme-boost-dividends-part-stock-market-reform-2025-06-11/?utm_source=chatgpt.com "South Korea to revamp tax scheme to boost dividends as part of stock market reform"
[3]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[4]: https://www.reuters.com/technology/samsung-electronics-plans-72-bln-buyback-boost-shareholder-value-2024-11-15/?utm_source=chatgpt.com "Samsung Electronics plans $7.2 billion buyback after share price plunges"
[5]: https://www.reuters.com/world/asia-pacific/philippine-e-wallet-firm-mynt-aiming-8-billion-valuation-ipo-sources-say-2026-05-14/?utm_source=chatgpt.com "Philippine e-wallet firm Mynt aiming for $8 billion valuation in IPO, sources say"
[6]: https://www.reuters.com/business/finance/south-korean-fintech-toss-plans-global-push-starting-australia-aims-issue-won-2025-09-09/?utm_source=chatgpt.com "South Korean fintech Toss plans global push starting in Australia, aims to issue won stablecoin"
[7]: https://www.ft.com/content/647fe2ef-9b01-4ab9-a93b-15b18f474563?utm_source=chatgpt.com "Samsung quashes activist proposals backed by Norway's oil fund"
[8]: https://www.reuters.com/markets/deals/korea-zinc-shares-surge-record-high-after-court-clears-hurdle-buyback-offer-2024-10-21/?utm_source=chatgpt.com "Korea Zinc shares surge to record high after court clears hurdle for buyback offer"
[9]: https://www.marketwatch.com/story/south-koreas-new-tax-proposals-derail-one-of-the-worlds-best-performing-stock-markets-of-2025-9432538d?utm_source=chatgpt.com "South Korea's new tax proposals derail one of the world's best performing stock markets of 2025."
[10]: https://www.reuters.com/legal/government/terrausd-creator-do-kwon-be-sentenced-over-40-billion-crypto-collapse-2025-12-11/?utm_source=chatgpt.com "TerraUSD creator Do Kwon to be sentenced over $40 billion crypto collapse"
[11]: https://www.reuters.com/sustainability/boards-policy-regulation/bank-englands-bailey-sees-wrestle-with-us-stablecoin-regulation-2026-05-08/?utm_source=chatgpt.com "Bank of England's Bailey sees 'wrestle' with US on stablecoin regulation"
