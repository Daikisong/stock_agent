좋아. 이번 라운드는 **“대섹터 누락 보정 + 점수-주가 정합성 강화 + 성공/반례 판별 기준 고도화”**로 갈게.

현재 레포 28A는 구조는 잘 깔렸지만 아직 전체 시장판은 아니야. `full_live_taxonomy_built: False`, `fixture_only: True`, mapped symbols 13개, archetypes used 8개뿐이고, case library도 25개 archetype 중 2개 성공 + 2개 반례를 채운 항목이 0개라서 전부 `insufficient_case_coverage` 상태야.
그러니까 지금은 scoring을 바꾸는 단계가 아니라, **케이스 매트릭스를 더 깊게 채우고, 점수와 실제 주가 리레이팅이 맞았는지 검증하는 단계**가 맞아.

핵심 정신은 유지해야 해.

> 산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅 → 논리 훼손 전까지 보유.

이게 서생원식 에이전트의 중심이고, 단순 테마·단기 실적·일회성 수요·주가 급등은 정통 E2R이 아니야.

---

# Round 7 핵심 업데이트

이번 라운드에서 더 강하게 추가할 기준은 이거야.

```text
점수 높음 + 주가 리레이팅 O + EPS/FCF 동행 O
= 성공 사례 후보

점수 높음 + 주가 리레이팅 X
= 점수비중 실패 반례

주가 급등 O + EPS/FCF 동행 X
= 테마/이벤트/사이클 반례

EPS 폭발 O + 다음 해 정상화/붕괴
= one-off / cyclical / 4B-4C 반례
```

즉 이제 성공사례는 “좋아 보이는 종목”이 아니라, **Stage 2/3 근거 이후 주가와 실적이 같이 리레이팅된 케이스**여야 한다.

---

# 1. Platform / Software / Internet — 더 엄격하게 반례화

## 이번 결론

플랫폼은 “좋은 회사”와 “E2R 성공”을 강하게 분리해야 해. 네이버, 카카오를 무심코 성공사례로 넣으면 점수체계가 망가질 가능성이 크다.

특히 Naver는 2026년 1분기 매출과 영업이익은 늘었지만 순이익이 전년 대비 31% 감소했고, AI 투자와 GPU/CapEx 부담이 마진 압박 요인으로 거론됐다. 주가도 그해 KOSPI 대비 부진했다는 보도가 있어, “AI 플랫폼”이라는 키워드만으로 E2R 성공사례로 넣으면 안 된다. ([월스트리트저널][1])

Kakao는 플랫폼 자산이 있어도, SM엔터 인수 과정의 주가조작 의혹과 창업자 관련 법적 리스크가 강한 governance/RedTeam 사례다. ([Reuters][2])

## 케이스 분류

| 케이스         | 분류            | 판단                                                       |
| ----------- | ------------- | -------------------------------------------------------- |
| NAVER       | 성공후보 또는 반례 후보 | 광고·커머스·AI가 OP/FCF로 연결되고 주가가 리레이팅돼야 성공. AI 비용이 마진을 누르면 반례 |
| Kakao       | 반례 후보         | 플랫폼 자산은 있으나 규제·거버넌스·법적 리스크가 valuation rerating을 막을 수 있음  |
| 더존비즈온       | 성공후보          | ERP/SaaS 반복매출, AI/클라우드, OPM 레버리지 확인 필요                   |
| MAU만 높은 플랫폼 | 반례            | 트래픽이 수익화되지 않으면 E2R 아님                                    |

## 점수-주가 검증 규칙

```text
점수 높게 줄 수 있는 조건:
- ARPU / take-rate 상승
- OPM 개선
- 반복매출 증가
- FY1/FY2 OP 상향
- AI 비용이 FCF를 훼손하지 않음

반례 조건:
- MAU/AI narrative는 강한데 OP/FCF가 안 따라옴
- 규제/거버넌스 이슈로 multiple이 눌림
- Stage 3 후보처럼 보였지만 주가가 리레이팅되지 않음
```

## 점수비중 보정

```text
EPS/FCF: 20
Visibility: 22
Bottleneck/Pricing: 6~8
Mispricing: 16
Valuation: 14
Risk penalty: regulation / AI cost / governance
```

플랫폼은 Green보다 **Stage 2-Watch / Stage 3-Watch**가 더 자주 맞을 가능성이 높다.

---

# 2. Game / Content / IP — 신작 기대와 반복 IP 분리

## 이번 결론

게임/IP는 **신작 기대**와 **실제 반복 monetization**을 분리해야 해. 신작 뉴스로 주가가 올라도, 출시 후 OP/EPS가 안 따라오면 성공사례가 아니라 반례야.

Krafton은 BGMI/India exposure가 있는 글로벌 IP 후보로 볼 수 있다. Reuters는 Krafton이 Naver·Mirae와 함께 인도 tech 투자 펀드를 추진했고, Krafton이 BGMI를 통해 인도 게임시장에 큰 exposure를 가진다고 보도했다. BGMI는 2억 4천만 다운로드 이상이라는 설명도 있다. ([Reuters][3])

Shift Up은 Nikke·Stellar Blade라는 IP와 2024년 IPO 이후 고마진 게임사 후보로 볼 수 있지만, 단일 IP·신작 의존 리스크도 같이 봐야 한다. ([위키백과][4])

## 케이스 분류

| 케이스           | 분류            | 판단                                                              |
| ------------- | ------------- | --------------------------------------------------------------- |
| Krafton       | 성공후보          | PUBG/BGMI 글로벌 IP, India exposure. 규제 리스크와 반복 monetization 동시 확인 |
| Shift Up      | 성공후보          | Nikke/Stellar Blade, 높은 OPM 후보. 단일 IP 의존도 확인                    |
| HYBE/JYP/SM   | 성공후보 또는 반례 후보 | IP·투어·팬덤 monetization 가능. 아티스트/계약/거버넌스 리스크                      |
| 신작 기대만 있는 게임주 | 반례            | 출시 후 매출이 안 나오면 4C                                               |
| 단일 IP 의존 게임주  | 반례            | 한 게임 꺾이면 EPS 경로 깨짐                                              |

## Stage 기준

```text
Stage 1:
신작, 컴백, 투어, 예약판매, 다운로드 증가

Stage 2:
실제 매출화, OP/EPS 상향, IP 반복성 확인

Stage 3:
IP portfolio, 글로벌 monetization, 낮은 churn, 반복 revenue

4B:
신작 흥행 peak, 기대 과열, multiple saturation

4C:
신작 실패, 핵심 IP 훼손, 계약 리스크, 규제/판호 리스크
```

## 점수-주가 검증 규칙

```text
성공:
신작/콘텐츠 이후 OP/EPS가 실제 상향되고 주가가 6~24개월 리레이팅

반례:
출시 전 주가만 오르고 출시 후 매출/OP가 기대 미달
```

---

# 3. Travel / Leisure / Airline — 리오프닝과 구조 E2R 분리

## 이번 결론

여행·항공·카지노·면세는 리오프닝 rebound와 구조적 E2R을 구분해야 해. 주가가 강하게 튀어도 유가, 환율, 관광객 peak, 중국 의존이 꺾이면 4C가 빨리 올 수 있다.

Korean Air는 2024년에 연간 매출 16조원, 영업이익 2조원을 기록했고 Asiana 인수로 글로벌 경쟁력이 커졌지만, 2025년에는 미국 노선과 cargo 약화로 순이익이 급감했다는 보도도 있다. 이건 **리오프닝/통합 시너지 성공후보이면서 동시에 경기·관세·수요 둔화 반례**가 될 수 있다. ([Reuters][5])

Korean Air가 100대 이상 Boeing 항공기를 구매하기로 한 대규모 장기 투자도 성장/효율화 신호이지만, 동시에 CAPEX와 cycle risk를 같이 봐야 한다. ([AP News][6])

## 케이스 분류

| 케이스            | 분류           | 판단                                                                            |
| -------------- | ------------ | ----------------------------------------------------------------------------- |
| Korean Air     | 성공후보 + 반례 후보 | Asiana 통합, record revenue, cargo/passenger mix. 그러나 tariff·미국 여행·cargo 둔화 리스크 |
| 호텔신라/신세계       | 성공후보         | 면세/관광 회복. 중국 의존도와 객단가 확인                                                      |
| 파라다이스/GKL      | 성공후보         | 카지노 drop amount, VIP mix 확인                                                   |
| 면세 중국 단체관광 기대주 | 반례           | 실제 매출/OP 없이 기대만 있으면 Stage 1                                                   |
| 항공 유가·환율 악화    | 반례           | 수요 좋아도 마진 훼손                                                                  |

## Stage 기준

```text
Stage 1:
출입국 회복, 관광객 증가, 면세/카지노/항공 매출 회복

Stage 2:
OP/EPS 상향, fixed cost leverage, 고마진 고객 mix

Stage 3:
중국 의존도 낮음, 비용 안정, 반복 관광 수요, FCF 개선

4B:
reopening 기대 모두 반영, 관광객 peak, 항공기 CAPEX 부담

4C:
유가/환율 악화, 경기 둔화, 중국/미국 노선 수요 약화
```

## 점수비중

```text
EPS/FCF: 18
Visibility: 14
Bottleneck/Pricing: 5
Mispricing: 12
Valuation: 10
Cyclical risk cap: 강함
```

---

# 4. Construction / Real Estate / Credit — 수주보다 신용 리스크 우선

## 이번 결론

건설은 수주잔고가 있어도 PF·미분양·유동성 리스크가 있으면 Green 금지다. “낙폭과대 + 유동성 지원”은 Stage 1 relief일 수 있지만, 구조적 E2R은 아니다.

한국 부동산 PF 연체율은 2021년 말 0.37%에서 2023년 말 2.70%로 상승했고, 금융당국은 구조조정 강화를 발표했다. ([Reuters][7])

## 케이스 분류

| 케이스            | 분류   | 판단                             |
| -------------- | ---- | ------------------------------ |
| PF 리스크 해소형 건설사 | 성공후보 | 부실 정리 후 cash flow 회복 시 후보      |
| 해외 플랜트/인프라 수주형 | 성공후보 | 수주 질과 마진이 확정적이면 후보             |
| PF 부실 건설사      | 반례   | 수주잔고보다 credit risk 우선          |
| 유동성 지원 의존 건설사  | 반례   | 지원은 Stage 1 relief, 구조적 E2R 아님 |
| 원가 상승 미반영 건설사  | 반례   | 매출 증가에도 OP/FCF 훼손              |

## Stage 기준

```text
Stage 1:
PF 우려 완화, 유동성 지원, 주가 낙폭과대

Stage 2:
부실 정리, cash flow 개선, 원가율 안정, 부채 감소

Stage 3:
매우 제한적. 구조조정 후 반복 cash flow, 해외수주 마진 확정, PF risk 낮음

4B:
부동산 회복 기대 과열, 미분양 risk 무시

4C:
PF 부실, 미분양 증가, 신용등급 하락, 유동성 위기
```

## 점수-주가 검증 규칙

```text
주가 반등 + PF 미해결
= credit relief rally, E2R 성공 아님

수주 증가 + 원가율 악화
= false positive
```

---

# 5. Retail / E-commerce / Offline Consumer — 구조 경쟁과 비용 레버리지

## 이번 결론

리테일은 점포수나 매출보다 **OPM, 재고, 온라인 경쟁, 고객 mix**가 핵심이다.

중국 e-commerce/Alibaba 계열과 Shinsegae/Gmarket 관련 JV는 국내 온라인 retail 경쟁 구조를 바꿀 수 있다. 한국 당국은 AliExpress Korea와 Shinsegae unit JV를 조건부 승인하면서 고객 데이터와 cross-border e-commerce 점유율 문제를 언급했다. 2024년 한국인의 중국 직구 지출은 32% 증가했고, Alibaba가 해당 시장에서 큰 점유율을 차지했다. ([Reuters][8])

## 케이스 분류

| 케이스                           | 분류    | 판단                                |
| ----------------------------- | ----- | --------------------------------- |
| 편의점 BGF/GS                    | 성공후보  | 점포효율, PB, 비용레버리지 확인               |
| 호텔신라/신세계                      | 성공후보  | 관광/면세 회복. 중국 의존도 위험               |
| E-Mart / Shinsegae e-commerce | 후보/반례 | JV 기대는 있지만 온라인 경쟁·마진·데이터 규제 확인 필요 |
| 대형마트 구조 경쟁 심화                 | 반례    | 온라인 경쟁으로 OPM 악화                   |
| 중국 직구 확산 피해주                  | 반례    | 가격경쟁과 마진 압박                       |

## Stage 기준

```text
Stage 1:
소비 회복, same-store sales, 관광객 증가, 온라인 JV

Stage 2:
OPM 개선, 재고 정상화, PB/고마진 mix, 비용 레버리지

Stage 3:
점포 효율 구조 변화, 반복 고객, FCF 개선, valuation discount 해소

4B:
소비 회복 선반영, 점포 성장 한계

4C:
재고 증가, 온라인 경쟁 심화, 소비 둔화, data/regulatory issue
```

---

# 6. CDMO / Revenue Healthcare — 바이오와 분리

## 이번 결론

Samsung Biologics 같은 CDMO는 pre-revenue biotech이 아니라 **contract/backlog healthcare archetype**에 가깝다. 장기 생산계약, capacity, 고객사 다변화, 가동률, FCF가 핵심이다.

Samsung Biologics는 2025년에 GSK로부터 미국 생산시설을 2억 8천만 달러에 인수해 미국 시장 대응을 강화한다고 발표했고, 해당 시설은 60,000L drug substance capacity를 가진 것으로 보도됐다. ([Reuters][9])
또 Samsung Biologics는 CDMO로서 대형 글로벌 제약사와 협력하고, 2025년 기준 Plant 5 포함 총 785,000L 생산능력으로 정리된다. ([위키백과][10])

## 케이스 분류

| 케이스                               | 분류     | 판단                                                                                |
| --------------------------------- | ------ | --------------------------------------------------------------------------------- |
| Samsung Biologics                 | 성공후보   | CDMO capacity, 글로벌 고객, 장기 수요, 미국 생산시설                                             |
| Celltrion                         | 성공후보   | 바이오시밀러 매출화, 글로벌 판매. litigation/가격경쟁 확인                                            |
| Samsung Bioepis patent litigation | 반례/리스크 | Amgen이 Prolia/Xgeva biosimilar 관련 patent suit 제기. 법적 지연 리스크로 봐야 함 ([Reuters][11]) |
| pre-revenue biotech               | 반례     | 매출화 전 Green 금지                                                                    |

## Stage 기준

```text
Stage 1:
대형 생산계약, capacity 확장, 글로벌 고객

Stage 2:
가동률 상승, 매출/OP 상향, 장기계약

Stage 3:
다년 생산 visibility, 고객사 다변화, 높은 FCF conversion

4B:
capacity 기대 과열, valuation 포화

4C:
계약 지연, 가동률 하락, patent/litigation, 가격경쟁
```

## 점수비중

```text
EPS/FCF: 20
Visibility: 24
Bottleneck/Pricing: 12
Mispricing: 12
Valuation: 12
Risk: litigation / capacity utilization
```

---

# 7. Royalty / Drug Commercialization Biotech

## 이번 결론

바이오 중에서도 유한양행 Lazertinib처럼 실제 승인·판매·로열티 경로가 있는 경우는 pre-revenue biotech과 분리해야 해.

Lazertinib은 한국에서 2021년 승인됐고, 미국에서는 amivantamab 병용으로 2024년 승인, EU에서는 2025년 승인된 것으로 정리된다. 이 유형은 임상 뉴스가 아니라 **approval → commercialization → royalty/revenue** 경로가 핵심이다. ([위키백과][12])

## 케이스 분류

| 케이스                          | 분류   | 판단                                                      |
| ---------------------------- | ---- | ------------------------------------------------------- |
| Yuhan / Lazertinib           | 성공후보 | approval, commercialization, royalty/revenue visibility |
| Alteogen                     | 성공후보 | 기술이전/SC 제형/로열티 visibility 필요                            |
| pre-revenue clinical biotech | 반례   | 임상 뉴스만으로 Green 금지                                       |
| 기술이전 headline만 있는 바이오        | 반례   | milestone/royalty 불확실하면 Stage 1~2                       |
| CB/유증 반복 바이오                 | 반례   | dilution risk                                           |

## Stage 기준

```text
Stage 1:
임상/허가/기술이전 뉴스

Stage 2:
approval 가능성, milestone, partner validation

Stage 3:
실제 매출/로열티, EPS/FCF 전환, dilution risk 낮음

4B:
신약 기대 과열, valuation이 매출화보다 먼저 감

4C:
임상 실패, 허가 지연, partner 계약 해지, 유증/CB
```

---

# 8. Holding / Governance / Shareholder Return

## 이번 결론

이 archetype은 한국 시장에서 매우 중요해졌지만, event premium과 구조적 E2R을 분리해야 해.

SK Square는 SK Hynix 지분가치 대비 저평가 상태에서 자사주 매입·소각과 독립이사 선임 등 value-up 조치를 발표했고, 이는 holding discount 해소 후보로 볼 수 있다. ([Reuters][13])

Korea Zinc는 경영권 분쟁과 자사주 매입, 공개매수 프리미엄으로 주가가 움직인 이벤트 사례다. 15억 달러 buyback과 경영권 분쟁, 유통주식 감소로 주가가 record high까지 움직였다는 Reuters 보도가 있다. ([Reuters][14])

## 케이스 분류

| 케이스            | 분류                              | 판단                                  |
| -------------- | ------------------------------- | ----------------------------------- |
| SK Square      | 성공후보                            | 자회사 가치, 자사주 소각, holding discount 해소 |
| Korea Zinc     | event premium + governance case | 구조적 FCF rerating인지 이벤트 프리미엄인지 분리    |
| 삼성물산/삼성생명      | 성공후보                            | NAV, governance, 환원, 자회사 가치         |
| 자사주 발표만 있는 지주사 | 반례                              | 소각·반복환원 없으면 value trap              |
| 경영권 분쟁만 있는 종목  | 반례                              | EPS/FCF 변화 없으면 Stage 3 금지           |

## Stage 기준

```text
Stage 1:
자사주, 소각, 배당, 경영권 분쟁, value-up 공시

Stage 2:
실제 소각, 반복 환원정책, 자회사 실적 개선

Stage 3:
governance regime change, NAV discount 구조적 해소, 반복 환원

4B:
이벤트 프리미엄 반영 완료, 공개매수/분쟁 종결

4C:
환원 미이행, 자회사 가치 훼손, 지배주주 리스크 재부각
```

---

# 9. Financial Spread / Value-Up

## 이번 결론

금융주는 EPS/FCF 폭발보다는 **ROE, PBR, 자본비율, 주주환원**이 핵심이다. 한국의 value-up/거버넌스 개혁 흐름은 금융주 리레이팅의 배경이 될 수 있지만, 정책만으로 Green을 주면 안 된다.

2026년 한국 대통령이 Korea discount 해소를 위한 추가 주식시장 개혁과 중복상장 제한 등을 언급했고, 시장은 큰 폭으로 반응했다. 이런 정책 환경은 금융·지주·저PBR archetype의 Stage 1/2 신호가 될 수 있다. ([Reuters][15])

## 케이스 분류

| 케이스           | 분류   | 판단                          |
| ------------- | ---- | --------------------------- |
| KB금융          | 성공후보 | ROE, PBR, 자사주/배당, CET1      |
| 신한지주/하나금융     | 성공후보 | capital return, credit cost |
| 메리츠금융/삼성화재    | 성공후보 | 자본효율, 보험계약마진, 자사주/배당        |
| 단순 저PBR 금융주   | 반례   | ROE/환원 없으면 value trap       |
| PF/충당금 리스크 금융 | 반례   | credit cost 상승이면 4C         |

## Stage 기준

```text
Stage 1:
value-up 공시, 자사주/배당, 저PBR

Stage 2:
ROE 개선, 자본비율 안정, 충당금 안정, 환원 실행

Stage 3:
PBR-ROE 프레임 변화, recurring ROE, credible shareholder return

4B:
PBR이 ROE 대비 정상화, 모두가 value-up 성공주로 인정

4C:
credit cost 증가, PF 부실, 자본비율 악화
```

---

# 10. Rare Metals / Strategic Materials

## 이번 결론

이건 Commodity와 Holding/Governance 사이에 걸친 별도 archetype으로 두는 게 맞다.

```text
전략금속 / 제련마진 / 공급망 / 경영권 / 자본배분
```

## 케이스

| 케이스             | 분류                          | 판단                                                       |
| --------------- | --------------------------- | -------------------------------------------------------- |
| Korea Zinc      | event + strategic materials | 세계 최대급 zinc smelter, 경영권 분쟁, 자사주/공개매수, 전략소재 supply chain |
| 단순 금속가격 상승주     | 반례                          | 가격만 오르면 commodity cycle                                  |
| 공개매수 이벤트만 있는 종목 | 반례                          | EPS/FCF 변화 없이 이벤트 프리미엄이면 Stage 3 금지                      |
| 경영권 분쟁 장기화      | 4C 후보                       | 투자 지연, governance discount                               |

## Stage 기준

```text
Stage 1:
금속가격 상승, 공개매수, supply chain 뉴스

Stage 2:
제련마진 개선, 자본배분 개선, cash flow 개선

Stage 3:
공급망 bottleneck + FCF + governance rerating

4B:
공개매수 프리미엄 반영 완료

4C:
경영권 분쟁 장기화, 투자 지연, 마진 악화
```

---

# 11. 이번 Round 7의 정리된 case-library 설계 원칙

## Case 성공판정

```text
success_case =
  evidence_score_high
  + stage2_or_stage3_signal
  + price_rerating_after_signal
  + EPS/OP/FCF_revision_confirmed
  + no_fast_4C
```

## Case 반례판정

```text
counterexample =
  price_up_without_EPS
  OR score_high_but_price_no_rerating
  OR EPS_spike_one_off
  OR fast_4C_after_stage2
  OR event_premium_only
```

## Price validation 필수 필드

```text
stage1_price
stage2_price
stage3_price
stage4b_price
stage4c_price
peak_price
MFE_90D
MFE_180D
MFE_1Y
MAE_90D
MAE_180D
MAE_1Y
drawdown_after_peak
below_stage3_price_flag
```

---

# 12. 현재까지 Green 허용도 업데이트

## Green 가능성이 높은 쪽

```text
AI Data Center Infrastructure
Contract / Backlog Industrial
Defense / Government Backlog
Shipbuilding / Offshore Backlog
Export / Recurring Consumer
K-Beauty / Export Distribution
Memory / HBM Capacity
Semi Equipment / Advanced Packaging
CDMO / Healthcare Contract
Medical Device / Healthcare Export
Financial Spread / Shareholder Return
Turnaround / Cost Restructuring
```

## Stage 3-Watch / Yellow 중심

```text
Platform / Software
Game / Content / IP
Robotics / Factory Automation
Auto / Mobility
Nuclear / SMR / Grid Policy
Holding / Governance
Travel / Leisure
Education / Specialty Services
Rare Metals / Strategic Materials
Utilities / Regulated Tariff
Royalty / Drug Commercialization Biotech
```

## Red / 4B 방어 중심

```text
Shipping / Freight Cycle
Commodity Spread
Battery Materials / Capex Overheat
Construction / Real Estate / Credit
Pre-revenue Biotech
One-off Event Demand
Theme / Valuation Overheat
```

---

# 13. 다음 라운드에서 더 채울 곳

아직 더 깊게 봐야 할 곳은 이거야.

```text
1. Turnaround / Cost Restructuring
   실제 구조조정 성공 vs 일회성 비용절감 반례

2. Commodity Spread
   정유/화학/철강/비철을 각각 분리

3. Auto Components
   완성차와 부품/전장/EV 부품 분리

4. Financial
   KB/신한/메리츠/삼성화재 price-path와 ROE/PBR 정합성 확인

5. CDMO / Medical Device
   삼성바이오, 셀트리온, 클래시스, 휴젤, 파마리서치, 원텍 비교

6. Platform
   네이버/더존/카카오를 실제 stage-price alignment로 확정

7. Education / Specialty Services
   아직 케이스가 약함

8. AI Data Center Infrastructure
   전력기기 외 냉각/PCB/IDC/ESS 케이스 보강
```

---

# 결론

이번 라운드의 핵심은 이거야.

> **성공사례는 점수가 높아야 할 뿐 아니라, 그 점수 이후 주가가 EPS/FCF 리레이팅 방향으로 움직였어야 한다.**
> **반례는 “나쁜 기업”이 아니라, 점수상 좋아 보일 수 있었지만 실제 주가·실적·4C 경로가 E2R이 아니었던 케이스다.**

이 기준을 넣으면, 네가 말한 것처럼 “플랫폼에서 네이버를 높게 줬는데 실제론 리레이팅이 안 됐다” 같은 실패를 case library에서 잡아낼 수 있다.

[1]: https://www.wsj.com/business/earnings/naver-posts-weaker-first-quarter-earnings-1a3511ec?utm_source=chatgpt.com "Naver Posts Weaker First-Quarter Earnings"
[2]: https://www.reuters.com/business/south-korea-court-decide-arrest-warrant-kakao-founder-2024-07-22/?utm_source=chatgpt.com "South Korea court to decide on arrest warrant for Kakao founder"
[3]: https://www.reuters.com/world/asia-pacific/pubg-maker-krafton-leads-south-korean-trio-666-million-india-tech-bet-2025-12-19/?utm_source=chatgpt.com "PUBG maker Krafton leads South Korean trio in $666 million India tech bet"
[4]: https://en.wikipedia.org/wiki/Shift_Up?utm_source=chatgpt.com "Shift Up"
[5]: https://www.reuters.com/business/aerospace-defense/korean-air-reports-record-annual-revenue-flags-uncertainties-global-politics-2025-02-07/?utm_source=chatgpt.com "Korean Air reports record annual revenue, flags uncertainties from global politics"
[6]: https://apnews.com/article/72da477d948558534cbe0112969c3136?utm_source=chatgpt.com "Korean Air plans to buy more than 100 Boeing aircraft"
[7]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[8]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-conditionally-approves-aliexpress-shinsegae-unit-joint-venture-2025-09-18/?utm_source=chatgpt.com "South Korea conditionally approves AliExpress, Shinsegae unit joint venture"
[9]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/?utm_source=chatgpt.com "Samsung Biologics to buy US drug production facility from GSK for $280 million"
[10]: https://en.wikipedia.org/wiki/Samsung_Biologics?utm_source=chatgpt.com "Samsung Biologics"
[11]: https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/?utm_source=chatgpt.com "Amgen sues Samsung biotech unit over bone drug copies"
[12]: https://en.wikipedia.org/wiki/Lazertinib?utm_source=chatgpt.com "Lazertinib"
[13]: https://www.reuters.com/technology/artificial-intelligence/south-koreas-ai-chip-investor-announces-plan-share-buybacks-2024-11-21/?utm_source=chatgpt.com "South Korea's AI chip investor announces plan for share buybacks"
[14]: https://www.reuters.com/markets/commodities/korea-zinc-attempts-fend-off-takeover-with-stake-buyback-2024-10-28/?utm_source=chatgpt.com "Korea Zinc attempts to fend off takeover with $1.5 billion share buyback"
[15]: https://www.reuters.com/sustainability/boards-policy-regulation/skorean-president-lee-vows-more-stock-market-reforms-triggering-share-rally-2026-03-18/?utm_source=chatgpt.com "S.Korean President Lee vows more stock market reforms,  triggering share rally"
