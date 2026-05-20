좋아. 정해둔 순서대로 이번은 **R10 — 건설·부동산·건자재**로 넘어간다.

R10은 Green을 매우 조심해야 하는 라운드다. 이유는 단순하다. 건설·부동산·건자재는 수주잔고나 자산가치가 커 보여도, 실제로는 **PF, 미분양, 금리, 공실, 원가율, 현금흐름, 배당 커버리지**가 먼저다. 업로드된 Theme Tag Map v0.5에서도 대형 건설사·중소형 건설사·개발신탁리츠·건자재·시멘트·철근·가구·거푸집·우크라 재건·네옴시티는 대부분 Watch/Red 또는 Event/Watch로 분류되어 있고, “수주잔고만으로 Green을 주면 위험하다”는 정규화 원칙이 잡혀 있다.

서생원식으로 보면 R10의 질문은 “부동산이 좋아질까?”가 아니라, **PF·금리·공실·원가 리스크가 제거되면서 EPS/FCF 체급과 valuation frame이 같이 바뀌는가**다. 단순 부동산 회복, 정부 지원, 착공 기대, 재건 테마, 리츠 배당률만으로는 Stage 3-Green이 아니다.

---

# R10. 건설·부동산·건자재

## 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
```

R10의 기본 구조는 이렇게 나눈다.

```text
1. 건설·PF 신용위험형
건설사 / 개발신탁 / PF / 미분양 / 유동성
→ 수주보다 현금흐름과 신용위험이 먼저

2. 건자재 cycle형
시멘트 / 레미콘 / 철근 / 거푸집 / 가구
→ 착공량, 원가, 가격인상, OPM

3. REIT·부동산 현금흐름형
리츠 / 데이터센터 REIT / 콜드체인 REIT / 오피스·물류
→ occupancy, NOI/AFFO, 금리, 배당 커버리지

4. 정책·재건 이벤트형
우크라 재건 / 네옴시티 / 세종시 / 재난복구
→ 실제 계약 전까지 Event/Watch
```

---

## 2. 대상 canonical archetype

| 구분                 | canonical archetype                     | Green 정책           |
| ------------------ | --------------------------------------- | ------------------ |
| 건설·PF 신용위험         | `CONSTRUCTION_REAL_ESTATE_CREDIT`       | Watch/Red          |
| 리츠·개발신탁            | `REIT_DEVELOPMENT_TRUST`                | Watch              |
| 건자재 cycle          | `BUILDING_MATERIALS_CYCLE`              | Watch              |
| 데이터센터 REIT         | `DATA_CENTER_REIT_INFRASTRUCTURE`       | Watch-to-Green     |
| 콜드체인 REIT·물류창고     | `COLD_CHAIN_REIT_LOGISTICS`             | Watch-to-Green     |
| 인프라·재건 정책          | `INFRA_RECONSTRUCTION_POLICY`           | Event/Watch        |
| 재난복구 이벤트           | `DISASTER_REBUILD_EVENT`                | Event/Watch        |
| 오피스·상업용 부동산 credit | `COMMERCIAL_REAL_ESTATE_CREDIT`         | Watch/Red          |
| 주택·분양 회복           | `RESIDENTIAL_HOUSING_CYCLE`             | Watch              |
| 데이터센터 전력·부지 개발     | `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT` | Watch/Red-to-Green |

---

## 3. deep sub-archetype

```text
CONSTRUCTION_REAL_ESTATE_CREDIT
- 대형 건설사
- 중소형 건설사
- PF 보증
- 브릿지론
- 본PF 전환
- 미분양
- 유동성 지원
- 원가율
- 공사비 상승

REIT_DEVELOPMENT_TRUST
- 개발신탁
- 리츠
- 배당
- 금리
- LTV
- refinancing
- 공실률
- NAV discount

BUILDING_MATERIALS_CYCLE
- 시멘트
- 레미콘
- 콘크리트
- 철근
- 거푸집
- 건자재
- 가구
- 착공량
- 가격인상
- 원재료·에너지비

DATA_CENTER_REIT_INFRASTRUCTURE
- 데이터센터 REIT
- hyperscale tenant
- AI infrastructure real asset
- 전력·냉각·수자원
- funding cost
- AFFO

COLD_CHAIN_REIT_LOGISTICS
- 냉동창고
- 신선식품 물류
- 의약품 온도관리
- occupancy
- 에너지비
- NOI/AFFO

INFRA_RECONSTRUCTION_POLICY
- 우크라 재건
- 네옴시티
- 해외 인프라
- 실제 계약
- financing

DISASTER_REBUILD_EVENT
- 지진 복구
- 홍수 복구
- 단기 건자재 수요
```

---

# 4. 성공사례

## 4-1. 한국 정부 건설·PF 유동성 지원 — `CONSTRUCTION_REAL_ESTATE_CREDIT`

한국 정부는 고금리와 부동산 경기 둔화로 압박받는 건설사와 중소기업을 지원하기 위해 40.6조 원 규모 금융지원책을 발표했다. 건설사에는 보증 확대, 추가 대출, 시장안정펀드 등을 통해 “수익성 있는 부동산 프로젝트”의 자금조달을 돕겠다고 했고, 태영건설의 debt rescheduling 이후 중견 건설사 유동성 우려가 커진 배경도 언급됐다. ([Reuters][1])

**가격경로 1차 판정**

```text
판정:
policy_relief_candidate / not_structural_success_yet

의미:
정부 지원은 Stage 1 relief다.
실제 Green은 PF 구조조정 후 cash flow, 원가율, 미분양, debt rollover가 개선되어야 가능.
```

**점수 교정**

```text
EPS/FCF: 아직 약함
Structural Visibility: 낮음~중간
Market Mispricing: 중간
Risk Penalty: PF, 미분양, refinancing, 원가율
```

---

## 4-2. 데이터센터 REIT — Blackstone Digital Infrastructure Trust

Blackstone Digital Infrastructure Trust는 17.5억 달러 IPO를 통해 새 데이터센터 REIT를 상장했고, 신규 건설 데이터센터를 investment-grade hyperscale tenant에게 임대하는 자산을 목표로 한다. 다만 상장 첫날 주가는 IPO가인 20달러와 같은 가격으로 flat debut을 했고, 아직 실제 데이터센터 자산을 취득하지 않은 상태라는 점도 보도됐다. ([Reuters][2])

**가격경로 1차 판정**

```text
가격 반응:
IPO가 $20 → 첫 거래 $20, flat debut

판정:
infrastructure_theme_needs_assets

의미:
AI 데이터센터 REIT는 Green 가능성이 있지만,
실제 tenant, asset acquisition, AFFO, funding cost가 확인되기 전까지 Stage 3 금지.
```

**점수 교정**

```text
Structural Visibility: tenant 계약이 붙으면 강함
EPS/FCF: AFFO 확인 전 제한
Capital Allocation: 중요
Risk: CAPEX, funding cost, tenant concentration, 전력·수자원 병목
```

---

## 4-3. NTT DC REIT — 데이터센터 REIT의 tepid debut

Singapore의 NTT DC REIT는 7.73억 달러 IPO를 통해 여섯 개 데이터센터 자산을 들고 상장했지만, 첫 거래에서 1.00싱가포르달러 offer price 대비 1.03싱가포르달러로 소폭 상승하는 데 그쳤다. AI 데이터센터 수요는 강하지만, 시장은 REIT의 자산·tenant·금리·AFFO를 함께 본다는 의미다. ([Reuters][3])

**가격경로 1차 판정**

```text
가격 반응:
IPO $1.00 → $1.03

판정:
mild_price_alignment / no_explosive_rerating

의미:
데이터센터 REIT는 테마만으로 폭발하지 않는다.
자산 질과 배당/FFO가 핵심.
```

---

## 4-4. Lineage cold-storage REIT — `COLD_CHAIN_REIT_LOGISTICS`

Lineage는 세계 최대 냉동·냉장창고 운영사로, 2024년 미국 IPO에서 44.4억 달러를 조달하며 기업가치 180억 달러 이상으로 상장했다. Lineage는 전 세계 482개 temperature-controlled warehouses를 운영하고 13,000개 이상 food supply-chain 고객을 보유한 것으로 보도됐다. 다만 Reuters는 Lineage가 2024년 3월까지 12개월간 1.628억 달러 순손실을 기록했다고도 보도했다. ([Reuters][4])

**가격경로 1차 판정**

```text
판정:
cold_chain_scale_success_candidate_but_profitability_watch

의미:
콜드체인은 실제 자산·고객·반복 물류 수요가 있는 후보.
하지만 순손실, 에너지비, debt, AFFO 커버리지 확인 전 Green 제한.
```

---

## 4-5. 건자재·시멘트: Heidelberg Materials

Heidelberg Materials는 2025년 3분기 비용절감과 가격관리를 통해 예상보다 높은 영업이익을 냈고, 2025년 주가가 74% 상승한 것으로 보도됐다. 회사는 2026년에도 construction markets 안정화와 인프라·방산 지출 증가를 바탕으로 영업이익 증가를 전망했다. ([Reuters][5])

**가격경로 1차 판정**

```text
가격 반응:
2025년 주가 +74% 보도

판정:
building_materials_price_cost_aligned_candidate

의미:
건자재도 가격인상 + 비용관리 + 인프라 수요가 동시에 있으면 Watch-to-Green 가능.
다만 한국 건자재는 착공량·PF·원가·출하량을 별도로 확인해야 한다.
```

**점수 교정**

```text
EPS/FCF: 중간~강함
Structural Visibility: 중간
Bottleneck/Pricing: 중간~강함
Risk: 착공량, 원가, 에너지비, 건설 PF
```

---

## 4-6. Fermi data-center REIT — AI 인프라 부동산의 고위험 후보

Fermi는 AI 데이터센터와 에너지 인프라를 결합한 Texas 기반 REIT로 6.825억 달러 IPO를 했고, valuation은 124.6억 달러로 책정됐다. 이 회사는 2038년까지 11GW 규모 전력을 데이터센터에 공급하는 캠퍼스를 계획하지만, 2026년 말까지 제한적 에너지 공급을 시작할 예정이며 향후 12개월 내 매출 발생을 기대하지 않고, 설립 이후 640만 달러 손실을 기록했다고 보도됐다. ([Reuters][6])

**가격경로 1차 판정**

```text
판정:
AI_infra_real_asset_high_risk_watch

의미:
AI 데이터센터 부동산 테마는 강하지만,
무매출·장기 개발·전력인허가·CAPEX·funding risk가 크면 Stage 3-Green 금지.
```

---

# 5. 반례

## 5-1. 한국 PF 연체율 상승 — `CONSTRUCTION_REAL_ESTATE_CREDIT`

한국 FSS는 부동산 프로젝트 평가를 강화하고 구조조정을 촉진하겠다고 밝혔다. 부동산 프로젝트 연체율은 2021년 말 0.37%에서 2022년 말 1.19%, 2023년 말 2.70%까지 상승했다. 이는 건설·PF 라운드의 핵심 hard risk다. ([Reuters][7])

**교훈**

```text
수주잔고
≠ Green

건설사는:
PF 보증
브릿지론
미분양
원가율
cash conversion
부채 만기
를 먼저 봐야 한다.
```

**가격경로 1차 판정**

```text
판정:
PF_credit_risk_hard_counterexample

의미:
정부 지원이 있어도 부실 프로젝트는 구조조정 대상.
Stage 3-Green은 매우 제한.
```

---

## 5-2. Blackstone Mortgage Trust 배당 삭감 — `COMMERCIAL_REAL_ESTATE_CREDIT`

Blackstone Mortgage Trust는 공실 오피스와 대출 부실 압박으로 배당을 24% 삭감했고, 주가는 10% 하락했다. 미국 office exposure의 55%가 watch-listed 또는 impaired였고, 추가 credit loss reserve 1.4억 달러를 쌓았다는 보도도 있었다. ([Reuters][8])

**교훈**

```text
리츠·부동산 금융의 hard 4C:
공실 증가
대출 부실
배당 삭감
credit loss reserve
refinancing failure
```

**가격경로 1차 판정**

```text
가격 반응:
배당 삭감 후 -10%

판정:
commercial_RE_credit_4c
```

---

## 5-3. 건설사 유동성 지원은 구조적 성공이 아니다

한국 정부의 40.6조 원 지원은 건설사 유동성 위기를 완화하는 relief 신호지만, 구조적 성공은 아니다. 정부는 “수익성 있는 프로젝트”를 지원한다고 했고, 이는 반대로 수익성 낮은 프로젝트는 구조조정 대상이 될 수 있음을 뜻한다. ([Reuters][1])

**교훈**

```text
정책지원
≠ thesis success

정책지원은 Stage 1 relief.
Stage 2는 실제 refinancing 성공과 현금흐름 개선.
Stage 3는 PF risk가 낮아지고 EPS/FCF가 회복될 때만.
```

---

## 5-4. 데이터센터 REIT theme-only risk

Blackstone Digital Infrastructure Trust는 AI 인프라 수요라는 매우 강한 narrative가 있었지만, 아직 데이터센터 자산을 취득하지 않은 상태에서 flat debut했다. 이는 AI 데이터센터 REIT가 자산·tenant·AFFO 없이 테마만으로 리레이팅되기 어렵다는 반례다. ([Reuters][2])

**교훈**

```text
AI data center real estate
≠ Green

필수:
asset acquisition
tenant lease
power/cooling/water 확보
NOI/AFFO
funding cost
```

---

## 5-5. 콜드체인 scale but loss

Lineage는 세계 최대 cold-storage operator이지만, 상장 전 12개월 기준 1.628억 달러 순손실을 기록했다. 규모·고객·자산이 있어도, 에너지비·부채·시설 CAPEX·AFFO가 약하면 Green을 주면 안 된다. ([Reuters][4])

**교훈**

```text
cold-chain asset scale
≠ Green

NOI/AFFO, occupancy, 에너지비, debt, dividend coverage가 핵심.
```

---

## 5-6. Cemex / 수요 둔화와 가격인상 한계 — `BUILDING_MATERIALS_CYCLE`

Cemex는 가격 인상으로 일부 매출 감소를 상쇄했지만, Mexico와 U.S. 주요 시장 수요 약화로 2024년 4분기 매출이 5% 감소했고 순이익도 예상치를 밑돌았다. 회사는 2027년까지 3.5억 달러 비용절감 프로그램을 추진하기로 했다. ([Reuters][9])

**교훈**

```text
건자재 가격인상
≠ Green

볼 것:
출하량
원재료·에너지비
가격 전가
수요 회복
FCF
```

---

# 6. 4B-watch 사례

## 6-1. 데이터센터 REIT IPO 과열

```text
4B 조건:
- AI 데이터센터 REIT가 자산·tenant 없이도 고평가
- IPO 수요가 AI narrative만으로 과열
- AFFO/NOI보다 capex pipeline만 강조
```

Blackstone Digital Infrastructure Trust는 flat debut이라 아직 4B 과열은 제한적이지만, AI infrastructure IPO window가 열려 있다는 점은 4B-watch 신호다. ([Reuters][2])

---

## 6-2. Fermi식 AI 전력·부동산 mega-project 과열

```text
4B 조건:
- revenue 전인데 valuation이 크게 형성
- 2030년대 장기 개발계획을 현재 valuation에 반영
- 전력·인허가·funding 리스크를 시장이 과소평가
```

Fermi는 12개월 내 매출을 기대하지 않는 초기 회사인데도 124.6억 달러 valuation을 받았다. 이는 AI 데이터센터 real asset에서 대표적인 4B-watch 후보다. ([Reuters][6])

---

## 6-3. 건자재 가격인상·인프라 기대 과열

Heidelberg Materials는 cost/price management와 인프라·방산 spending 기대 덕분에 2025년 주가가 74% 상승했다. 성공 후보이지만, 건자재는 착공량·원가·수요가 꺾이면 빠르게 4B에서 4C로 넘어갈 수 있다. ([Reuters][5])

```text
4B 조건:
- 건자재 가격인상 narrative 과밀
- 인프라 지출 기대가 모두 반영
- 출하량 둔화를 시장이 무시
```

---

## 6-4. PF relief rally 4B-watch

```text
4B 조건:
- 정부 지원 뉴스로 건설주 동반 반등
- 실제 PF restructuring과 cash flow 개선 전 valuation 상승
- 부실 프로젝트 선별이 끝나지 않음
```

정부 유동성 지원은 relief rally를 만들 수 있지만, 구조적 개선과는 다르다. ([Reuters][1])

---

# 7. 4C-thesis-break 사례

## 7-1. PF 연체율 상승

```text
4C:
PF delinquency increase
bridge loan rollover failure
default risk assessment
unprofitable project restructuring
```

부동산 프로젝트 연체율이 2021년 말 0.37%에서 2023년 말 2.70%로 상승한 것은 건설·부동산 credit thesis의 핵심 4C다. ([Reuters][7])

---

## 7-2. 오피스 공실·대출부실·배당삭감

```text
4C:
office vacancy
watch-listed or impaired loan
credit loss reserve
dividend cut
share price drop
```

Blackstone Mortgage Trust의 배당 24% 삭감과 주가 10% 하락은 commercial real estate credit 4C의 대표 사례다. ([Reuters][8])

---

## 7-3. 데이터센터 자산 없는 REIT

```text
4C-watch:
no acquired assets
no tenant
no AFFO
AI infrastructure narrative only
```

Blackstone Digital Infrastructure Trust는 flat debut이었고, 아직 데이터센터 자산을 취득하지 않았다. 이는 Stage 1 테마와 Stage 3 자산현금흐름을 분리해야 한다는 기준 사례다. ([Reuters][2])

---

## 7-4. 콜드체인 순손실

```text
4C-watch:
large asset base but net loss
energy cost pressure
debt burden
AFFO uncertainty
```

Lineage는 자산·고객 규모가 크지만, 상장 전 순손실이 있었다. 이는 콜드체인 REIT에서 scale만 보고 Green을 주면 안 된다는 반례다. ([Reuters][4])

---

## 7-5. 건자재 수요 둔화

```text
4C-watch:
volume decline
price increase cannot fully offset demand weakness
cost pressure
construction slowdown
```

Cemex 사례처럼 가격 인상으로도 수요 둔화와 원가 부담을 완전히 상쇄하지 못하면 building materials thesis가 약해진다. ([Reuters][9])

---

# 8. 점수비중 보정표 — R10 v1.0

| canonical archetype                     | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | 핵심 감점                                     |
| --------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ----------------------------------------- |
| `CONSTRUCTION_REAL_ESTATE_CREDIT`       |      14 |         10 |          5 |         12 |         9 |       0 |    5 | PF, 미분양, refinancing, 원가율                 |
| `REIT_DEVELOPMENT_TRUST`                |      15 |         16 |          5 |         13 |        11 |       5 |    5 | 금리, 공실, LTV, 배당 커버리지                      |
| `BUILDING_MATERIALS_CYCLE`              |      17 |         13 |         12 |         10 |         9 |       3 |    5 | 착공 둔화, 원가, 출하량, 에너지비                      |
| `DATA_CENTER_REIT_INFRASTRUCTURE`       |      18 |         23 |         18 |         13 |        13 |       5 |    5 | CAPEX, funding cost, tenant concentration |
| `COLD_CHAIN_REIT_LOGISTICS`             |      17 |         21 |         12 |         12 |        11 |       5 |    5 | 에너지비, occupancy, debt, AFFO               |
| `INFRA_RECONSTRUCTION_POLICY`           |      12 |         10 |          8 |         10 |         8 |       0 |    4 | 실제 수주 없음, financing, 정책 이벤트               |
| `DISASTER_REBUILD_EVENT`                |      10 |          6 |          7 |          8 |         6 |       0 |    4 | one-off 수요, 지속성 부족                        |
| `COMMERCIAL_REAL_ESTATE_CREDIT`         |      12 |          9 |          4 |         12 |         8 |       0 |    5 | 공실, 대출부실, 배당삭감                            |
| `RESIDENTIAL_HOUSING_CYCLE`             |      15 |         12 |          5 |         12 |         9 |       1 |    5 | 미분양, 금리, 가계부채, 착공 둔화                      |
| `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT` |      16 |         18 |         15 |         13 |        10 |       3 |    5 | 자산 부재, 전력·수자원, 장기 개발                      |

---

# 9. stage date 후보

## `CONSTRUCTION_REAL_ESTATE_CREDIT`

```text
Stage 1:
정부 PF 지원, 금리 인하 기대, 부동산 회복 뉴스

Stage 2:
PF refinancing 성공, 미분양 감소, 현금흐름 개선, 원가율 안정 확인

Stage 3:
부실 프로젝트 정리 후 EPS/FCF 회복과 valuation frame 전환

Stage 4B:
PF relief rally 과열

Stage 4C:
PF 연체율 상승, bridge loan rollover 실패, debt workout, 대규모 손상
```

## `REIT_DEVELOPMENT_TRUST`

```text
Stage 1:
금리 하락 기대, 배당 매력, 자산가치 회복 뉴스

Stage 2:
occupancy, 임대료, NOI/AFFO, 배당 커버리지 확인

Stage 3:
배당 지속성과 NAV discount 축소 확인

Stage 4B:
고배당·금리인하 리츠 랠리 과열

Stage 4C:
공실 증가, LTV 악화, refinancing 실패, 배당 삭감
```

## `BUILDING_MATERIALS_CYCLE`

```text
Stage 1:
가격인상, 원가 안정, 착공 회복 뉴스

Stage 2:
출하량 회복, OPM 개선, 가격 전가 확인

Stage 3:
착공 cycle 개선과 FCF 안정 확인

Stage 4B:
건자재 가격인상 narrative 과열

Stage 4C:
착공 둔화, 원재료·에너지비 상승, 출하량 하락
```

## `DATA_CENTER_REIT_INFRASTRUCTURE`

```text
Stage 1:
AI 데이터센터 REIT IPO, hyperscale demand, asset pipeline 뉴스

Stage 2:
자산 취득, tenant lease, power/cooling 확보, NOI/AFFO 확인

Stage 3:
FFO/AFFO growth와 배당 커버리지 안정 확인

Stage 4B:
AI infrastructure real estate valuation 과열

Stage 4C:
자산 미취득, tenant 부재, power/water permitting 실패, funding cost 상승
```

## `COLD_CHAIN_REIT_LOGISTICS`

```text
Stage 1:
cold-storage IPO, food/pharma cold-chain 수요 뉴스

Stage 2:
occupancy, customer contract, NOI/AFFO, 에너지비 통제 확인

Stage 3:
반복 물류수요와 배당 커버리지 안정 확인

Stage 4B:
cold-chain REIT premium 과열

Stage 4C:
순손실, 에너지비 상승, occupancy 하락, debt 부담
```

## `INFRA_RECONSTRUCTION_POLICY`

```text
Stage 1:
우크라 재건, 네옴시티, 재난복구 정책 뉴스

Stage 2:
실제 계약, financing, 공사 착수, 매출 인식 확인

Stage 3:
다년 수주잔고와 마진이 확인될 때만

Stage 4B:
정책 기대만으로 관련주 동반 급등

Stage 4C:
프로젝트 취소, financing 실패, geopolitical setback
```

---

# 10. 가격경로 검증계획

## R10 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. PF 지표, 미분양, NOI/AFFO, 배당, occupancy, 원가율, 출하량, 금리와 가격 경로를 비교한다.
```

## R10에서 반드시 분리할 판정

```text
policy_relief_rally:
정부 지원·금리인하 기대만으로 오른 경우.

credit_recovery_aligned:
PF 리스크가 낮아지고 현금흐름·부채 구조가 개선되며 주가가 회복된 경우.

asset_cashflow_aligned:
REIT/부동산 자산에서 NOI/AFFO, occupancy, 배당 커버리지가 주가와 동행한 경우.

building_materials_cycle_success:
건자재 가격·원가·출하량 덕분에 수익은 났지만 구조적 Green은 아닌 경우.

theme_without_asset:
데이터센터·재건·네옴·우크라 테마는 있으나 실제 자산·tenant·계약 없음.

thesis_break:
PF 연체, debt workout, 배당삭감, 공실, 자산손상, 순손실, refinancing failure.
```

## 이번 R10에서 우선 검증할 가격 case

| case_id                                       |              stage2 후보일 | 현재 1차 가격판정                            |
| --------------------------------------------- | ----------------------: | ------------------------------------- |
| `korea_pf_delinquency_restructuring_case`     |              2024-05-13 | PF hard counterexample                |
| `korea_builder_support_relief_case`           |              2024-03-27 | policy relief, not structural success |
| `blackstone_mortgage_trust_dividend_cut_case` |              2024-07-24 | -10%, CRE credit 4C                   |
| `blackstone_data_center_reit_flat_debut_case` |              2026-05-14 | flat debut, asset cashflow not proven |
| `ntt_dc_reit_tepid_debut_case`                |              2025-07-14 | +3%, mild alignment                   |
| `fermi_ai_data_center_reit_case`              |              2025-09-30 | high-risk theme, no revenue yet       |
| `lineage_cold_storage_reit_ipo_case`          |              2024-07-24 | scale success but net loss watch      |
| `heidelberg_materials_price_cost_case`        | 2025-11-06 / 2026-02-25 | +74% in 2025, aligned candidate       |
| `cemex_demand_slowdown_price_offset_case`     |              2025-02-06 | demand slowdown mixed case            |
| `ukraine_reconstruction_event_watch_case`     |               계약별 확인 필요 | actual contract before Green          |
| `neom_city_event_watch_case`                  |               계약별 확인 필요 | actual contract before Green          |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R10 case library에는 아래 필드가 필요하다.

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

pf_exposure
pf_guarantee_amount
pf_delinquency_rate
bridge_loan_exposure
refinancing_success_flag
debt_workout_flag
unsold_inventory_units
cash_conversion_cycle
construction_cost_ratio
gross_margin
op_margin_change

revenue_backlog
contract_value
contract_duration
contract_margin_signal

reit_type
occupancy_rate
noi_growth
affo_growth
ffo_growth
dividend_per_share
dividend_cut_flag
dividend_coverage_ratio
ltv_ratio
funding_cost
refinancing_maturity
office_exposure
watchlisted_or_impaired_asset_ratio

building_material_volume
cement_price_change
steel_rebar_price_change
energy_cost_change
raw_material_cost_change
price_hike_flag
cost_saving_amount

data_center_asset_acquired_flag
hyperscale_tenant_flag
tenant_concentration
power_secured_flag
water_permitting_flag
capex_amount
asset_pipeline_value
ai_infra_theme_flag

cold_storage_warehouse_count
cold_storage_capacity
energy_cost_ratio
customer_count
net_loss_flag

policy_support_amount
government_support_flag
reconstruction_contract_flag
financing_secured_flag
project_delay_flag

score_price_alignment
price_validation_status
```

---

# R10 결론

R10은 **Green보다 RedTeam이 먼저인 대섹터**다.

```text
Green 가능:
데이터센터 REIT 중 실제 자산·tenant·AFFO가 확인된 경우
콜드체인 REIT 중 occupancy·NOI/AFFO·배당 커버리지가 확인된 경우
건자재 중 가격전가·원가관리·출하량 회복이 같이 있는 경우

Watch:
대형 건설사
건자재
리츠
개발신탁
데이터센터 real asset
콜드체인
재건 인프라

Red/4C 방어 중심:
PF 노출 큰 건설사
중소형 건설사
미분양·bridge loan rollover 실패
오피스 공실·대출부실
배당삭감 리츠
자산 없는 AI 데이터센터 REIT
정책·재건 테마만 있는 종목
```

**R10 점수정규화의 핵심 문장:**

> 건설·부동산·건자재는 “수주·자산·배당률”이 아니라 **PF 리스크, 현금흐름, 원가율, occupancy, NOI/AFFO, 배당 커버리지, funding cost, 실제 계약·자산·tenant**로 봐야 한다.
> 정부 지원과 금리인하 기대는 Stage 1 relief일 뿐이고, Stage 3-Green은 실제 credit recovery와 cash-flow recovery가 확인될 때만 가능하다.

다음에 네가 “다음 라운드 진행해줘”라고 하면, 정해둔 순서에 따라 **R11 — 정책·지정학·재난·이벤트**로 넘어간다.

[1]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[2]: https://www.reuters.com/technology/blackstone-data-center-vehicle-opens-flat-new-york-debut-after-175-billion-ipo-2026-05-14/?utm_source=chatgpt.com "Blackstone data center vehicle makes muted debut after $1.75 billion IPO"
[3]: https://www.reuters.com/markets/asia/data-centre-ntt-dc-reit-opens-flat-debut-after-singapores-biggest-ipo-4-years-2025-07-14/?utm_source=chatgpt.com "Data centre NTT DC REIT makes tepid debut after Singapore's biggest IPO in 4 years"
[4]: https://www.reuters.com/markets/deals/logistics-giant-lineage-raises-445-bln-biggest-ipo-2024-2024-07-24/?utm_source=chatgpt.com "Logistics giant Lineage raises $4.44 bln in biggest IPO of 2024"
[5]: https://www.reuters.com/business/heidelberg-materials-posts-higher-than-expected-q3-profit-cost-price-management-2025-11-06/?utm_source=chatgpt.com "Heidelberg Materials posts higher than expected Q3 profit on cost, price management"
[6]: https://www.reuters.com/business/rick-perrys-data-center-reit-raises-682-million-us-ipo-2025-09-30/?utm_source=chatgpt.com "Rick Perry-backed Fermi REIT raises $682 million in U.S. IPO amid AI data-center boom"
[7]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[8]: https://www.reuters.com/business/finance/blackstones-battered-mortgage-fund-slumps-empty-offices-intensify-pressure-2024-07-24/?utm_source=chatgpt.com "Blackstone's battered mortgage fund slumps as empty offices intensify pressure"
[9]: https://www.reuters.com/business/mexican-cement-maker-cemex-ekes-out-profit-starts-350-million-savings-program-2025-02-06/?utm_source=chatgpt.com "Mexican cement maker Cemex ekes out profit, starts $350 million savings program"
