좋아. **R9 Loop 5까지 끝났으니, 이번은 R10 Loop 5 — 건설·부동산·건자재**로 넘어간다.

R10은 대형 건설사, 중소형 건설사, 부동산 자산 보유, 개발신탁리츠, 건자재, 시멘트·레미콘·콘크리트, 철근, 가구, 거푸집, 우크라 재건, 네옴시티, 세종시 같은 테마를 흡수하는 대섹터다. Theme Tag Map 기준으로도 이 구간은 **수주잔고보다 PF·현금흐름·원가율이 먼저**이고, 재건·네옴·세종시 같은 정책형 테마는 실제 계약·매출화 전까지 Event/Watch로 둬야 한다.

Checkpoint 20 원칙도 그대로 적용한다. PF 익스포저, 계약금액, 계약기간, 원가율, NOI, AFFO, 배당 커버리지, LTV, tenant lease, 전력·수자원 확보 같은 값은 실제 공시·기사·리포트에서 확인될 때만 써야 한다. R10은 “수주”, “고배당”, “AI 데이터센터”, “재건”이라는 단어 하나로 점수가 쉽게 부풀기 때문에, 없는 값을 추정하면 false-positive가 바로 생긴다.

서생원식으로 보면 R10의 질문은 “건설경기가 좋아지나?”가 아니라 **부채·PF·공실·원가율이라는 할인 요인이 사라지면서 EPS/FCF 체급과 밸류에이션 프레임이 바뀌는가**다. 배당률이 높아도 AFFO가 가짜면 탈락이고, 데이터센터 수요가 커도 tenant·power·water·NOI/AFFO가 없으면 Green이 아니다.

---

# R10 Loop 5. 건설·부동산·건자재

## 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
Loop 5 목표 =
PF credit risk / PF relief rally / REIT AFFO integrity /
AI data-center no-asset IPO / AI real-asset no-revenue /
data-center power-water-permitting / cold-chain REIT /
건자재 price-cost-volume cycle을 더 정밀 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 기업은 진짜 현금흐름이 회복되고 있는가?
아니면 정책지원, 금리인하 기대, 고배당 착시,
AI 데이터센터 테마, 재건 테마로 움직이는가?
```

R10에서 가장 위험한 오판은 여전히 이거다.

```text
수주잔고 / 고배당 / AI 데이터센터
= Green
```

Loop 5부터는 이렇게 갈라야 한다.

```text
좋은 구조 후보:
데이터센터 REIT + 실제 자산 + hyperscale tenant + power/water 확보 + NOI/AFFO
건자재 + 가격전가 + 비용관리 + 출하량 + OPM/FCF
콜드체인 REIT + occupancy + 에너지비 통제 + AFFO + 배당 커버리지
대형 건설사 + PF 익스포저 낮음 + cash conversion 개선 + 원가율 안정

위험한 후보:
PF 지원책만 보고 오른 건설주
오피스 공실·대출부실 노출 리츠
자산·tenant 없는 데이터센터 REIT IPO
무매출 AI 데이터센터 개발사
AFFO 계산이 불투명한 데이터센터 REIT
CAPEX가 AFFO/share growth보다 먼저 커지는 REIT
순손실·에너지비·부채가 큰 콜드체인 REIT
우크라 재건·네옴·세종시 정책 테마
```

---

## 2. 대상 canonical archetype

| canonical archetype                     | Loop 5 정책                                                                     |
| --------------------------------------- | ----------------------------------------------------------------------------- |
| `CONSTRUCTION_REAL_ESTATE_CREDIT`       | Watch/Red. PF·미분양·원가율·cash conversion 먼저                                      |
| `PF_RESTRUCTURING_RELIEF`               | Event/Watch. 정책지원은 Stage 1 relief, 회복 아님                                      |
| `PF_SYNDICATED_LOAN_SOFT_LANDING`       | Watch. soft landing 가능성은 있으나 부실 프로젝트 분리 확인 필요                                 |
| `RESIDENTIAL_HOUSING_CYCLE`             | Watch. 미분양·금리·가계부채·착공량 확인                                                     |
| `REIT_DEVELOPMENT_TRUST`                | Watch. 금리·LTV·occupancy·배당 커버리지 확인                                            |
| `COMMERCIAL_REAL_ESTATE_CREDIT`         | Watch/Red. 오피스 공실·대출부실·배당삭감 hard risk                                         |
| `DATA_CENTER_REIT_INFRASTRUCTURE`       | Watch-to-Green. 자산·tenant·NOI/AFFO·전력/수자원 확보 필요                               |
| `DATA_CENTER_REIT_IPO_NO_ASSET`         | High-risk Watch. 자산 미취득·tenant 미확정이면 Stage 3 금지                               |
| `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT` | High-risk Watch. 무매출·무tenant·장기개발이면 Green 금지                                  |
| `AI_POWER_DATA_CENTER_CAMPUS`           | High-risk Watch. power campus는 강하지만 tenant·permitting·financing 필요            |
| `DATA_CENTER_POWER_WATER_PERMITTING`    | RedTeam gate. 전력·수자원·지역반발·인허가 지연                                              |
| `DATA_CENTER_LOCAL_MORATORIUM_OVERLAY`  | RedTeam overlay. Seattle·Indianapolis류 moratorium, zoning, community pushback |
| `DATA_CENTER_CAPEX_AFFO_DILUTION`       | RedTeam overlay. CAPEX가 per-share AFFO보다 빠르면 감점                               |
| `COLD_CHAIN_REIT_LOGISTICS`             | Watch-to-Green. occupancy·NOI/AFFO·에너지비·debt 확인                               |
| `COLD_CHAIN_DEBT_OCCUPANCY_RISK`        | RedTeam overlay. 순손실·부채·수요 정상화·고객재고 둔화                                        |
| `BUILDING_MATERIALS_PRICE_COST`         | Watch-to-Green. 가격전가·비용관리·출하량·OPM 필요                                          |
| `BUILDING_MATERIALS_VOLUME_FAILURE`     | Watch/Red. 가격인상은 있으나 물량·EBITDA 약하면 탈락                                         |
| `LOW_CARBON_CEMENT_PREMIUM`             | Watch-to-Green. 친환경 시멘트 premium은 고객·보조금·원가 확인                                 |
| `BUILDING_PRODUCTS_MNA_SHIFT`           | Watch. cement → building products 전환은 synergy·multiple·debt 확인                |
| `INFRA_RECONSTRUCTION_POLICY`           | Event/Watch. 실제 계약·financing·착공 전 Green 금지                                    |
| `POLICY_LOCAL_REAL_ESTATE_THEME`        | Event. 세종시·지역개발·기관이전은 예산·계약 전 Stage 1                                         |
| `PF_CREDIT_REDTEAM_OVERLAY`             | RedTeam gate. PF 연체·브릿지론·워크아웃                                                 |
| `REIT_AFFO_INTEGRITY_OVERLAY`           | RedTeam gate. AFFO 착시·maintenance capex·배당 커버리지                               |
| `AI_INFRA_REAL_ASSET_THEME_OVERLAY`     | RedTeam gate. 자산·tenant·매출 없는 AI 테마                                           |
| `DISCLOSURE_CONFIDENCE_CAP`             | RedTeam cap. 계약·tenant·NOI/AFFO·PF detail 부족 시 Stage 3 제한                     |

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
- 워크아웃
- 유동성 지원
- 원가율
- 공사비 상승
- cash conversion

PF_RESTRUCTURING_RELIEF
- 정부 PF 지원
- 보증 확대
- market stabilizing fund
- syndicated loan
- profitable project rescue
- unprofitable project restructuring
- relief rally
- refinancing success

COMMERCIAL_REAL_ESTATE_CREDIT
- 오피스 공실
- watch-listed loans
- impaired loans
- non-accrual loans
- credit loss reserve
- dividend cut
- refinancing wall

DATA_CENTER_REIT_INFRASTRUCTURE
- 데이터센터 REIT
- hyperscale tenant
- investment-grade tenant
- newly constructed asset
- power secured
- cooling/water
- NOI
- AFFO
- capex
- funding cost
- tenant concentration

DATA_CENTER_REIT_IPO_NO_ASSET
- AI infrastructure IPO
- sponsor premium
- acquisition pipeline
- no acquired assets
- no binding lease
- bonus shares
- thematic IPO window
- execution capability premium

AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT
- AI data-center campus
- dedicated power
- natural gas / nuclear / solar mix
- long-term power plan
- no-revenue development-stage REIT
- no tenant
- non-binding LOI
- permitting
- single-site concentration
- execution risk

DATA_CENTER_POWER_WATER_PERMITTING
- local opposition
- water rights
- power interconnection
- grid stress
- diesel generator noise
- environmental impact
- referendum
- moratorium
- project withdrawal

COLD_CHAIN_REIT_LOGISTICS
- 냉동창고
- 냉장창고
- 식품 supply chain
- 의약품 cold chain
- temperature-controlled warehouse
- occupancy
- energy cost
- seasonality
- NOI/AFFO
- debt

BUILDING_MATERIALS_PRICE_COST
- 시멘트
- 레미콘
- 콘크리트
- 철근
- 거푸집
- 건자재
- 가격인상
- 비용절감
- 에너지비
- 출하량
- 착공량

LOW_CARBON_CEMENT_PREMIUM
- net-zero cement
- carbon capture
- evoZero
- CCS subsidy
- green premium
- construction decarbonization
- customer pre-sale
- subsidy durability

INFRA_RECONSTRUCTION_POLICY
- 우크라 재건
- 네옴시티
- 해외 인프라
- 정부 예산
- financing
- 실제 계약
- 착공
- 매출 인식
```

---

# 4. 성공사례 / 구조 후보

## 4-1. Heidelberg Materials — `BUILDING_MATERIALS_PRICE_COST`

Heidelberg Materials는 건자재가 Watch-to-Green으로 올라가는 조건을 보여준다. 2025년 3분기 RCO가 전년 대비 5% 증가한 11.8억 유로로 예상치를 웃돌았고, 비용절감과 가격인상이 핵심 배경이었다. 회사는 2026년 말까지 최소 5억 유로 연간 비용절감 목표도 제시했고, 2025년 주가가 74% 상승한 상태였다. 즉 단순 건설경기 회복이 아니라 **가격전가 + 비용관리 + 인프라 수요 기대 + 이익 가시성**이 같이 붙은 케이스다. ([Reuters][1])

```text
가격경로 1차 판정:
BUILDING_MATERIALS_PRICE_COST_ALIGNED_CANDIDATE

좋은 점:
- 가격인상
- 비용절감
- RCO 예상 상회
- infrastructure upgrade 기대
- 주가 +74% YTD

주의:
- 이미 4B-watch 가능
- 출하량 둔화 가능성
- 에너지비
- 착공 cycle
- 가격전가 지속성
```

**Loop 5 교정**

```text
BUILDING_MATERIALS_PRICE_COST:
가격인상만으로 Green 금지.

Stage 3 조건:
가격전가
+ 비용절감
+ 출하량 안정
+ OPM/FCF 개선
+ 가격경로 alignment
```

---

## 4-2. Heidelberg net-zero cement — `LOW_CARBON_CEMENT_PREMIUM`

Loop 5에서 `LOW_CARBON_CEMENT_PREMIUM`을 추가한다. Heidelberg Materials는 노르웨이 Brevik 공장에서 탄소포집 설비를 통해 evoZero라는 net-zero cement를 생산하고 있으며, 2025년 생산분은 모두 사전 판매됐다고 밝혔다. 해당 설비는 연간 약 40만 톤 CO₂를 포집하고, 노르웨이 Longship CCS 프로젝트의 정부 보조를 받는다. 이건 “친환경 건자재”가 실제 고객 수요로 이어지는 좋은 Stage 2 근거지만, 보조금 지속성과 green premium의 상업성이 Stage 3 gate다. ([Reuters][2])

```text
가격경로 1차 판정:
LOW_CARBON_CEMENT_PREMIUM_STAGE2_CANDIDATE

좋은 점:
- net-zero cement 생산
- 2025년 생산분 pre-sold
- CCS 설비와 고객 decarbonization 수요
- hard-to-abate sector의 green premium 가능성

주의:
- 정부 보조금 의존
- 일반 cement 대비 가격 premium 수용성
- CCS 운송·저장 비용
- 대규모 확장성
```

**Loop 5 교정**

```text
LOW_CARBON_CEMENT_PREMIUM 신규 추가.

Stage 2:
pre-sale
+ CCS 설비
+ 고객 수요
+ 정부지원

Stage 3:
subsidy 없이도 margin 유지
+ 반복계약
+ FCF
+ 생산량 확대
```

---

## 4-3. Cemex — 가격·비용은 좋지만 volume gate 필요

Cemex는 가격인상·비용절감이 있어도 출하량과 구조수요를 같이 봐야 하는 mixed case다. 2024년 4분기에는 가격인상이 매출 감소를 일부 상쇄했고, 2027년까지 3.5억 달러 earnings boost를 목표로 하는 savings program을 시작했지만, 매출은 전년 대비 5% 감소했고 핵심 시장인 멕시코·미국 물량이 약했다. 이후 2025년 3분기에는 가격인상과 비용절감 덕분에 core earnings가 19% 증가했지만, cement volume은 flat이고 ready-mix·aggregate volume은 소폭 하락했다. ([Reuters][3])

2026년 1분기에는 비용절감과 disciplined pricing 덕분에 EBITDA가 전년 대비 34% 증가한 7.94억 달러로 예상치를 웃돌았고, 회사는 high-single-digit EBITDA growth 전망을 유지했다. 다만 미국은 악천후 영향으로 flat sales/earnings였고, 이 케이스는 “가격·비용 관리 성공”과 “물량·지역 cycle 감시”를 동시에 붙여야 한다. ([Reuters][4])

```text
가격경로 1차 판정:
BUILDING_MATERIALS_COST_CUT_MIXED_CASE

좋은 점:
- 가격인상
- 비용절감 프로그램
- EBITDA 개선
- FCF 개선 가능성
- 비핵심 자산매각·자본환원 가능성

주의:
- 물량 둔화
- 핵심시장 수요 둔화
- 일회성 구조조정 비용
- 비용절감이 구조적 수요 회복을 의미하진 않음
```

**Loop 5 교정**

```text
BUILDING_MATERIALS_VOLUME_FAILURE:
가격인상과 cost cut은 Stage 2 후보.
하지만 volume_decline_flag가 켜지면 Stage 3-Green 제한.
```

---

## 4-4. Holcim / Xella — `BUILDING_PRODUCTS_MNA_SHIFT`

Holcim은 독일 walling systems 업체 Xella를 18.5억 유로에 인수하기로 했고, 이는 전통 cement 중심에서 roofing·insulation·walling 같은 building products로 이동하는 전략의 일부다. Xella는 2025년 약 10억 유로 매출이 예상되며, Holcim은 2026년 예상 EBITDA의 8.9배를 지불하고 1년 차부터 earnings accretive를 기대한다고 밝혔다. 이 구조는 단순 시멘트 spread보다 **고부가 building products + M&A synergy + systems-selling**으로 볼 수 있지만, multiple·통합·debt를 확인해야 한다. ([Reuters][5])

```text
가격경로 1차 판정:
BUILDING_PRODUCTS_MNA_SHIFT_STAGE2_CANDIDATE

좋은 점:
- cement pure cycle에서 building products로 mix 전환
- walling systems 시장 진입
- cross-selling / systems-selling 가능성
- year-one earnings accretion 기대

주의:
- 8.9x EBITDA multiple
- 통합 리스크
- 부채·자본배분
- 경기 둔화 시 제품 mix 방어력 확인 필요
```

**Loop 5 교정**

```text
BUILDING_PRODUCTS_MNA_SHIFT 신규 추가.

Stage 2:
M&A 확정
+ target 매출/EBITDA
+ accretion guidance

Stage 3:
synergy 실현
+ margin 개선
+ FCF
+ leverage 안정
```

---

## 4-5. Blackstone Digital Infrastructure Trust — `DATA_CENTER_REIT_IPO_NO_ASSET`

Blackstone Digital Infrastructure Trust, BXDC는 AI 데이터센터 REIT의 강한 Stage 1~2 후보지만 아직 Green은 아니다. BXDC는 2026년 5월 IPO에서 17.5억 달러를 조달했고, newly constructed data center assets를 investment-grade hyperscale tenant에게 임대하는 전략을 제시했다. 하지만 상장 첫날 주가는 IPO 가격인 20달러에서 flat debut했고, Reuters는 아직 데이터센터 자산을 취득하지 않은 상태에서 투자자들이 Blackstone의 실행력과 sector history를 사는 구조라고 설명했다. ([Reuters][6])

```text
가격경로 1차 판정:
DATA_CENTER_REIT_THEME_WITHOUT_ASSETS_YET

좋은 점:
- Blackstone execution capability
- QTS/AirTrunk 등 data center track record
- $25B near-term opportunities 검토
- hyperscale tenant 대상 전략
- AI infrastructure demand와 직접 연결

주의:
- 아직 자산 취득 없음
- tenant lease 미확인
- NOI/AFFO 미확인
- 전력·수자원 확보 미확인
- IPO thematic window 과열 가능성
```

**Loop 5 교정**

```text
DATA_CENTER_REIT_IPO_NO_ASSET:
asset_acquired_flag = false
binding_lease_flag = false
NOI/AFFO = unknown

이면:
Stage 3-Green 금지.
Blackstone sponsor premium은 Stage 1~2 근거일 뿐이다.
```

---

## 4-6. Equinix Malaysia expansion — data center demand는 진짜지만 power/water gate 필요

Equinix는 2026년 5월 말레이시아 Kuala Lumpur에 1.9억 달러 이상을 투자해 네 번째 데이터센터를 만들겠다고 밝혔다. 이 시설은 2,200개 이상 cabinet을 수용하고 AI·HPC 수요를 위해 advanced liquid cooling을 지원할 예정이다. 다만 Reuters는 말레이시아 데이터센터 boom이 전력망·수자원 제약과 미중 AI chip access 관련 지정학 압력 속에서 둔화되고 있다고 설명했다. ([Reuters][7])

```text
가격경로 1차 판정:
DATA_CENTER_DEMAND_REAL_BUT_POWER_WATER_GATE

좋은 점:
- AI/HPC 수요 대응
- advanced liquid cooling
- existing facility nearby expansion
- ASEAN interconnection hub thesis

주의:
- power grid constraint
- water resource constraint
- AI chip access geopolitics
- capex burden
- AFFO per share 전환 확인 필요
```

**Loop 5 교정**

```text
DATA_CENTER_REIT_INFRASTRUCTURE:
수요는 진짜다.
하지만 power/water/grid/AI-chip geopolitics가 stage gate다.

Stage 3 조건:
tenant lease
+ power secured
+ water/cooling secured
+ NOI/AFFO
+ capex per share dilution 없음
```

---

## 4-7. Lineage cold-storage REIT — `COLD_CHAIN_REIT_LOGISTICS`

Lineage는 콜드체인 REIT가 Green 후보가 되기 위해 무엇을 봐야 하는지 보여주는 mixed reference다. Lineage는 2024년 IPO에서 56.9 million shares를 78달러에 팔아 44억 달러를 조달했고, 세계 최대급 cold-storage operator로 482개 시설을 보유했다. 직전 12개월 기준 53억 달러 매출, 18억 달러 NOI, 13억 달러 adjusted EBITDA가 있었지만, 동시에 1.628억 달러 순손실도 기록했다. ([Investopedia][8])

```text
가격경로 1차 판정:
COLD_CHAIN_SCALE_SUCCESS_CANDIDATE_BUT_PROFITABILITY_WATCH

좋은 점:
- 세계 최대급 temperature-controlled warehouse network
- 식품 supply chain 고객 기반
- 482개 시설
- NOI/adjusted EBITDA 존재
- 식품·의약품 cold chain 구조수요

주의:
- 순손실
- debt
- energy cost
- occupancy
- AFFO/배당 커버리지
- post-IPO 수요 둔화 가능성
```

**Loop 5 교정**

```text
COLD_CHAIN_REIT_LOGISTICS:
warehouse_count와 customer_count는 Stage 1~2 증거.
Stage 3는 occupancy + NOI/AFFO + dividend coverage + debt 안정 확인 후.
```

---

## 4-8. 한국 PF 지원책 — `PF_RESTRUCTURING_RELIEF`

한국 정부의 PF 지원책은 R10에서 “성공”이 아니라 **relief rally 후보**로만 둔다. 2024년 3월 한국 정부는 고금리와 부동산 경기 둔화로 어려움을 겪는 중소기업·건설사를 위해 총 40.6조 원 규모 금융지원책을 발표했고, 건설사에는 보증 확대·추가 대출·시장안정펀드를 통해 수익성 있는 프로젝트의 자금조달을 돕겠다고 밝혔다. ([Reuters][9])

```text
가격경로 1차 판정:
PF_POLICY_RELIEF_STAGE1

좋은 점:
- 유동성 지원
- 보증 확대
- profitable project soft landing
- construction credit shock 완화 가능성

주의:
- 정책지원 자체는 EPS/FCF 회복이 아님
- unprofitable project restructuring은 남음
- PF 연체·브릿지론·미분양 리스크는 별도 확인 필요
```

**Loop 5 교정**

```text
PF_RESTRUCTURING_RELIEF:
정책지원은 Stage 1 relief.
Stage 2는 refinancing_success_flag와 PF exposure 감소.
Stage 3는 cash conversion과 원가율 안정이 확인될 때만.
```

---

# 5. 반례 / RedTeam

## 5-1. 한국 PF 연체율 상승 — `CONSTRUCTION_REAL_ESTATE_CREDIT`

한국 금융감독원은 2024년 5월 부동산 프로젝트 평가를 강화하고 구조조정을 촉진하겠다고 밝혔다. 부동산 프로젝트 연체율은 2021년 말 0.37%에서 2022년 말 1.19%, 2023년 말 2.70%까지 상승했다. FSS는 상업은행·보험사가 1조 원 규모 syndicated loan을 준비했고 필요시 5조 원까지 늘릴 수 있다고 설명했다. 이건 건설사·PF 관련주에서 수주잔고보다 **PF 보증, 브릿지론, 본PF 전환, 미분양, refinancing**을 먼저 봐야 한다는 hard counterexample이다. ([Reuters][10])

```text
가격경로 1차 판정:
PF_CREDIT_RISK_HARD_COUNTEREXAMPLE

교훈:
수주잔고
≠ Green

건설사는 먼저:
- PF exposure
- bridge loan rollover
- 미분양
- debt workout
- cash conversion
- 원가율

을 봐야 한다.
```

**Loop 5 교정**

```text
CONSTRUCTION_REAL_ESTATE_CREDIT:
Green 거의 제한.
PF exposure와 refinancing_success_flag가 없으면 Stage 3 금지.
```

---

## 5-2. Blackstone Mortgage Trust — `COMMERCIAL_REAL_ESTATE_CREDIT`

Blackstone Mortgage Trust는 오피스 공실과 고금리 압박 속에서 배당을 24% 삭감했고, 주가는 크게 하락했다. 회사는 credit loss reserve를 추가로 쌓았고, 오피스 loan exposure와 non-accrual/impaired asset 문제가 핵심 리스크로 부각됐다. 이건 고배당 REIT·부동산 credit 관련주에서 배당률보다 **impaired loans, credit reserve, dividend coverage**가 먼저라는 기준이다. ([Business Insider][11])

```text
가격경로 1차 판정:
COMMERCIAL_REAL_ESTATE_CREDIT_4C

4C 조건:
- office_vacancy
- impaired_loans
- watchlisted_loans
- credit_loss_reserve
- dividend_cut
- share_price_drawdown
```

**Loop 5 교정**

```text
COMMERCIAL_REAL_ESTATE_CREDIT:
배당률이 높아도 dividend_coverage와 impaired_asset_ratio가 나쁘면 Red.
```

---

## 5-3. Equinix Hindenburg case — `REIT_AFFO_INTEGRITY_OVERLAY`

데이터센터 REIT도 AI 수혜라는 이름만으로 Green을 줄 수 없다. Hindenburg Research는 Equinix가 maintenance capex를 expansion capex로 잘못 분류해 AFFO를 부풀렸다고 주장했고, Equinix 주가는 해당 공개 후 약 2% 하락했다. 이 사례는 데이터센터 REIT에서 **AFFO가 진짜 현금흐름인지, maintenance capex와 expansion capex가 정확히 분리되는지**를 반드시 검증해야 한다는 RedTeam 기준이다. ([Reuters][12])

```text
가격경로 1차 판정:
REIT_AFFO_INTEGRITY_RISK

교훈:
데이터센터 REIT
≠ AFFO 숫자만 보고 Green

필수 확인:
- maintenance capex
- expansion capex
- AFFO calculation
- power-constrained facility risk
- hyperscaler concentration
```

**Loop 5 교정**

```text
REIT_AFFO_INTEGRITY_OVERLAY:
AFFO 성장과 배당 커버리지는 capex 분류 검증을 통과해야 한다.
```

---

## 5-4. Equinix AI CAPEX burden — `DATA_CENTER_CAPEX_AFFO_DILUTION`

Equinix는 AI inference 수요를 잡기 위해 2026~2029년 연간 CAPEX를 40억~50억 달러로 높이겠다고 밝혔다. 하지만 매출 성장 전망과 AFFO per share 성장 전망이 투자자 기대에 못 미치자 주가는 8% 하락했다. 즉 데이터센터 수요가 구조적으로 강해도, **CAPEX가 AFFO·배당·per-share growth보다 먼저 커지면 valuation이 눌릴 수 있다.** ([Reuters][13])

```text
가격경로 1차 판정:
AI_DATA_CENTER_CAPEX_BURDEN_4B_TO_4C_WATCH

교훈:
AI data-center demand
≠ REIT Green

CAPEX가 AFFO growth보다 먼저 커지면
배당과 per-share growth가 눌린다.
```

**Loop 5 교정**

```text
DATA_CENTER_CAPEX_AFFO_DILUTION:
capex_amount와 affo_per_share_growth를 반드시 같이 본다.
asset growth가 per-share AFFO로 연결되지 않으면 4B/4C-watch.
```

---

## 5-5. Fermi — `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT`

Fermi는 AI 전력·데이터센터 real asset의 high-risk Watch 기준이다. 2025년 IPO에서 6.825억 달러를 조달하고 124.6억 달러 valuation을 받았으며, Amarillo AI 데이터센터 campus에서 2038년까지 최대 11GW 전력을 공급하겠다는 계획을 제시했다. 하지만 회사는 설립 초기 단계였고, 향후 12개월 내 매출을 기대하지 않으며, 설립 후 640만 달러 손실을 기록했다. ([Reuters][14])

이후 Fermi는 2025년 순손실 4.86억 달러와 tenant 미확정 우려로 주가가 13% 하락했다. 한 잠재 고객의 1.5억 달러 funding agreement가 종료됐고, 20년 lease letter도 non-binding 상태로 남아 있다. 이건 “토지·전력·AI narrative”가 있어도 **binding tenant lease와 매출이 없으면 high-risk Watch**라는 기준이다. ([Financial Times][15])

```text
가격경로 1차 판정:
AI_REAL_ASSET_NO_REVENUE_HIGH_RISK_WATCH

좋은 점:
- AI 전력·데이터센터 수요에 직접 노출
- 11GW power campus narrative
- nuclear / gas / solar mix 계획
- power bottleneck theme

주의:
- 무매출
- 장기 개발계획
- tenant lease 미확정
- non-binding LOI
- permitting / water / power execution risk
- single-site concentration
- funding gap
```

**Loop 5 교정**

```text
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT:
매출 전 high-risk Watch.

Stage 3 조건:
binding tenant lease
+ power secured
+ water/permitting secured
+ revenue
+ NOI/AFFO
+ financing stability
```

---

## 5-6. 데이터센터 지역반발·전력·수자원 — `DATA_CENTER_POWER_WATER_PERMITTING`

AI 데이터센터는 real asset 수요를 만들지만, 지역반발·전력·수자원 문제가 project delay로 바뀔 수 있다. 호주 Perth 인근에서는 120MW 규모 데이터센터 계획이 문화·환경 민감지역, 학교·주거지 인접, 디젤 발전기 소음 우려 등으로 약 1,900건 반대 의견을 받고 철회됐다. ([Guardian][16])

미국 Utah의 Stratos AI 데이터센터 프로젝트는 40,000 acre 이상 규모와 9GW 전력수요, 대규모 수자원 사용 우려로 강한 반발을 받고 있으며, 주민들은 승인 철회를 위한 referendum을 추진하고 있다. Seattle은 large data center에 대한 1년 moratorium을 검토 중이고, Indianapolis도 data center moratorium 결의를 통과시켰다. ([Guardian][17])

```text
가격경로 1차 판정:
DATA_CENTER_POWER_WATER_PERMITTING_4C_WATCH

의미:
AI 데이터센터 수요는 강하지만,
전력·수자원·소음·지역반발은 실제 프로젝트 지연과 취소로 이어질 수 있다.

감점 조건:
- local_opposition_flag
- water_permitting_delay_flag
- grid_interconnection_delay_flag
- noise_pollution_flag
- referendum_or_moratorium_flag
- project_withdrawal_flag
```

**Loop 5 교정**

```text
DATA_CENTER_REIT_INFRASTRUCTURE / AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT:
tenant만으로 부족하다.
power, water, grid interconnection, community approval을 stage gate로 둔다.
```

---

## 5-7. Cold-chain post-IPO debt / occupancy risk — `COLD_CHAIN_DEBT_OCCUPANCY_RISK`

콜드체인은 규모와 고객 기반이 강해 보여도, 수요 둔화·에너지비·부채가 가격경로를 깨뜨릴 수 있다. Lineage는 IPO 시점 기준 세계 최대급 규모와 NOI/adjusted EBITDA를 보유했지만, 순손실과 debt 상환 목적의 IPO proceeds가 동시에 있었다. 따라서 cold chain은 **창고 수, cubic feet, 고객 수**만으로 Green을 줄 수 없고, occupancy, NOI/AFFO, debt, energy cost, dividend coverage를 확인해야 한다. ([Investopedia][8])

```text
가격경로 1차 판정:
COLD_CHAIN_SCALE_TO_PROFITABILITY_4C_WATCH

교훈:
cold-chain warehouse scale
≠ Green

필수 확인:
- occupancy
- NOI/AFFO
- energy cost
- debt
- dividend coverage
- customer inventory trend
```

---

# 6. 4B-watch 사례

## 6-1. PF relief rally 4B-watch

```text
4B 조건:
- 정부 지원 뉴스로 건설주 동반 반등
- 실제 PF restructuring 전 valuation 회복
- 미분양·브릿지론·원가율이 그대로인데 가격만 회복
- 수익성 낮은 프로젝트 선별이 끝나지 않음
```

한국의 40.6조 원 지원책은 relief rally를 만들 수 있지만, 이 정책은 수익성 있는 프로젝트의 자금조달을 돕는 구조라서 부실 프로젝트의 구조조정 리스크는 남는다. ([Reuters][9])

---

## 6-2. 데이터센터 REIT IPO 4B-watch

```text
4B 조건:
- AI infrastructure IPO window가 열림
- 자산·tenant·AFFO 없이 sponsor track record만으로 valuation 형성
- capex·funding cost·power/water risk를 시장이 낮게 봄
```

BXDC는 Blackstone sponsor와 sector history는 강하지만, 자산을 아직 취득하지 않은 상태에서 상장했고 첫 거래도 flat이었다. ([Reuters][6])

---

## 6-3. AI real asset no-revenue 4B-watch

```text
4B 조건:
- 무매출 개발 단계인데 AI 전력·데이터센터 narrative로 고평가
- 2030년대 장기 계획을 현재 valuation에 반영
- tenant·power·water·permitting·financing이 미확정
```

Fermi는 AI 전력 bottleneck에 직접 노출되는 후보지만, IPO 시점 기준 향후 12개월 매출이 없고 11GW 계획은 2038년까지의 장기 개발이다. ([Reuters][14])

---

## 6-4. 데이터센터 power/water 4B-watch

```text
4B 조건:
- AI 데이터센터 수요를 모두가 인정
- 전력·수자원·지역반발 리스크를 낮게 봄
- zoning, grid interconnection, water rights가 아직 확정되지 않음
```

Perth 데이터센터 철회, Utah Stratos 반발, Seattle·Indianapolis moratorium 사례는 AI data-center real asset에서 local approval이 실물 프로젝트의 병목이 될 수 있음을 보여준다. ([Guardian][16])

---

## 6-5. 데이터센터 AFFO / capex 4B-watch

```text
4B 조건:
- AI 수요를 근거로 데이터센터 REIT valuation이 먼저 확장
- AFFO per share 성장보다 CAPEX가 더 빠르게 커짐
- maintenance capex와 expansion capex 구분을 시장이 낮게 봄
```

Equinix는 AI 수요를 잡기 위해 CAPEX를 키웠지만, AFFO per share 성장 전망이 낮아지자 주가가 크게 눌렸다. Hindenburg의 AFFO 관련 short report도 데이터센터 REIT의 cash-flow 품질 검증이 필수라는 기준이다. ([Reuters][13])

---

## 6-6. 콜드체인 REIT premium 4B-watch

```text
4B 조건:
- cold-chain warehouse scale만으로 premium 형성
- 순손실·energy cost·debt·AFFO 미확인
- food/pharma temperature-control narrative가 과밀
```

Lineage는 warehouse network와 고객 기반은 강하지만, 순손실과 debt, occupancy·고객재고 정상화 risk를 같이 봐야 한다. ([Investopedia][8])

---

## 6-7. 건자재 가격인상 4B-watch

```text
4B 조건:
- 가격인상·인프라 기대만으로 건자재주 동반 상승
- 출하량 둔화와 원가 부담을 무시
- 비용절감이 구조적 수요 회복처럼 오분류
```

Heidelberg Materials는 가격·비용 관리로 좋은 성과를 냈지만, Cemex 사례처럼 가격인상에도 물량 둔화와 수요 약화가 있으면 mixed/cycle로 내려가야 한다. ([Reuters][1])

---

## 6-8. 친환경 건자재 premium 4B-watch

```text
4B 조건:
- net-zero cement / CCS / green premium narrative가 과밀
- 정부보조금이 없으면 경제성이 불명확
- 고객 pre-sale을 장기 FCF로 과잉 일반화
```

Heidelberg의 Brevik evoZero는 좋은 Stage 2 후보지만, Norway Longship처럼 정부가 project risk를 크게 낮춰준 구조라서 subsidy durability와 commercial green premium을 같이 봐야 한다. ([Reuters][2])

---

# 7. 4C-thesis-break 사례

## 7-1. PF 연체율 상승

```text
4C:
PF_delinquency_increase
bridge_loan_rollover_failure
debt_workout
unprofitable_project_restructuring
refinancing_failure
```

PF 연체율이 2021년 말 0.37%에서 2023년 말 2.70%까지 상승한 것은 R10의 핵심 hard 4C다. ([Reuters][10])

---

## 7-2. 오피스 공실·대출부실·배당삭감

```text
4C:
office_vacancy
watchlisted_or_impaired_loans
credit_loss_reserve
non_accrual_loans
dividend_cut
share_price_drop
```

Blackstone Mortgage Trust의 배당 삭감과 office loan impairment는 commercial real estate credit의 기준 반례다. ([Business Insider][11])

---

## 7-3. 데이터센터 REIT AFFO / capex integrity

```text
4C-watch:
AFFO_overstatement_allegation
maintenance_capex_misclassification
expansion_capex_overuse
AI_pipe_dream_narrative
power_constrained_facility
```

Equinix Hindenburg case는 데이터센터 REIT의 cash-flow 품질을 반드시 검증해야 한다는 기준이다. ([Reuters][12])

---

## 7-4. AI 데이터센터 CAPEX burden

```text
4C-watch:
capex_growth_above_affo_growth
per_share_affo_slowdown
funding_cost_rise
tenant_deal_delay
capacity_expansion_without_yield
```

Equinix의 2026~2029년 연간 40억~50억 달러 CAPEX 계획과 AFFO 성장 전망 하향은 데이터센터 수요가 있어도 주가가 눌릴 수 있음을 보여준다. ([Reuters][13])

---

## 7-5. AI data-center no-asset/no-revenue thesis break

```text
4C-watch:
no_revenue
no_acquired_assets
no_binding_tenant_lease
single_site_concentration
power_permitting_delay
water_permitting_delay
funding_gap
execution_risk
```

Fermi와 BXDC는 둘 다 AI 인프라 narrative가 강하지만, 각각 무매출 개발 단계 또는 자산 미취득 상태이므로 Green 전 AFFO/tenant/asset proof가 필수다. ([Reuters][14])

---

## 7-6. 데이터센터 local opposition / permitting break

```text
4C-watch:
community_opposition
water_rights_delay
grid_interconnection_delay
noise_pollution
zoning_rejection
project_withdrawal
referendum_or_moratorium
```

Perth 데이터센터 철회와 Utah Stratos 반발은 AI 데이터센터 real asset 후보에서 power/water/local approval을 반드시 stage gate로 둬야 하는 이유다. ([Guardian][16])

---

## 7-7. 콜드체인 순손실·부채·수요 정상화

```text
4C-watch:
net_loss
energy_cost_pressure
customer_inventory_normalization
occupancy_decline
debt_burden
post_IPO_drawdown
guidance_cut
```

Lineage는 세계 최대급 규모에도 순손실과 debt 부담이 있었고, cold-chain scale만으로 Stage 3-Green을 주면 안 된다는 기준을 제공한다. ([Investopedia][8])

---

## 7-8. 건자재 수요 둔화

```text
4C-watch:
volume_decline
price_hike_cannot_offset_demand
EBITDA_decline
construction_slowdown
cost_pressure
```

Cemex는 가격인상과 비용절감에도 핵심 시장 물량 둔화를 겪었다. 건자재 가격인상만으로 Stage 3-Green을 주면 안 된다. ([Reuters][3])

---

# 8. 점수비중 보정표 — R10 Loop 5 / v5.0

| canonical archetype                     | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 5 핵심 감점                                              |
| --------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | --------------------------------------------------------- |
| `CONSTRUCTION_REAL_ESTATE_CREDIT`       |      12 |          8 |          5 |         11 |         7 |       0 |    5 | PF, 미분양, refinancing, 원가율, cash conversion                |
| `PF_RESTRUCTURING_RELIEF`               |      10 |          8 |          4 |         10 |         7 |       0 |    5 | 정책지원 착시, 부실 프로젝트 구조조정                                     |
| `PF_SYNDICATED_LOAN_SOFT_LANDING`       |      11 |          9 |          4 |         10 |         7 |       0 |    5 | soft landing 기대, 부실 프로젝트 선별 지연                            |
| `RESIDENTIAL_HOUSING_CYCLE`             |      15 |         12 |          5 |         12 |         9 |       1 |    5 | 미분양, 금리, 가계부채, 착공 둔화                                      |
| `REIT_DEVELOPMENT_TRUST`                |      15 |         16 |          5 |         13 |        11 |       5 |    5 | 금리, LTV, 공실, 배당 커버리지                                      |
| `COMMERCIAL_REAL_ESTATE_CREDIT`         |      10 |          7 |          4 |         11 |         6 |       0 |    5 | 공실, impaired loans, 배당삭감                                  |
| `DATA_CENTER_REIT_INFRASTRUCTURE`       |      18 |         22 |         18 |         13 |        11 |       5 |    5 | CAPEX, funding cost, tenant concentration, AFFO integrity |
| `DATA_CENTER_REIT_IPO_NO_ASSET`         |      11 |         12 |         13 |         12 |         7 |       1 |    5 | 자산 미취득, tenant 미확정, sponsor premium 착시                    |
| `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT` |      13 |         15 |         16 |         13 |         7 |       2 |    5 | 무매출, tenant 부재, single-site, power/water permitting       |
| `AI_POWER_DATA_CENTER_CAMPUS`           |      13 |         15 |         18 |         13 |         7 |       2 |    5 | no tenant, long-dated power delivery, financing gap       |
| `DATA_CENTER_POWER_WATER_PERMITTING`    |    gate |       gate |       gate |       gate |      gate |    gate | gate | 전력·수자원·지역반발·인허가                                           |
| `DATA_CENTER_LOCAL_MORATORIUM_OVERLAY`  |    gate |       gate |       gate |       gate |      gate |    gate | gate | moratorium, zoning, referendum, community opposition      |
| `DATA_CENTER_CAPEX_AFFO_DILUTION`       |    gate |       gate |       gate |       gate |      gate |    gate | gate | CAPEX 과대, AFFO/share 둔화, 배당 커버리지 훼손                       |
| `COLD_CHAIN_REIT_LOGISTICS`             |      17 |         19 |         12 |         12 |        10 |       5 |    5 | 에너지비, occupancy, debt, 순손실, AFFO                          |
| `COLD_CHAIN_DEBT_OCCUPANCY_RISK`        |    gate |       gate |       gate |       gate |      gate |    gate | gate | 순손실, debt, occupancy 하락, 고객재고 정상화                         |
| `BUILDING_MATERIALS_PRICE_COST`         |      18 |         15 |         12 |         11 |        10 |       3 |    5 | 착공 둔화, 출하량, 원가, 에너지비                                      |
| `BUILDING_MATERIALS_VOLUME_FAILURE`     |      13 |          9 |          8 |          8 |         6 |       1 |    5 | volume decline, EBITDA 감소                                 |
| `LOW_CARBON_CEMENT_PREMIUM`             |      16 |         14 |         11 |         12 |         9 |       2 |    5 | subsidy, green premium 지속성, CCS cost                      |
| `BUILDING_PRODUCTS_MNA_SHIFT`           |      17 |         16 |          9 |         12 |        10 |       3 |    5 | acquisition multiple, integration, leverage               |
| `INFRA_RECONSTRUCTION_POLICY`           |      10 |          8 |          8 |         10 |         7 |       0 |    4 | 실제 수주 없음, financing, 정책 이벤트                               |
| `POLICY_LOCAL_REAL_ESTATE_THEME`        |       5 |          5 |          4 |          8 |         5 |       0 |    3 | 예산·계약 부재, 정책 철회                                           |
| `PF_CREDIT_REDTEAM_OVERLAY`             |    gate |       gate |       gate |       gate |      gate |    gate | gate | PF 연체, 워크아웃, 브릿지론 실패                                      |
| `REIT_AFFO_INTEGRITY_OVERLAY`           |    gate |       gate |       gate |       gate |      gate |    gate | gate | AFFO 착시, maintenance capex 분류                             |
| `AI_INFRA_REAL_ASSET_THEME_OVERLAY`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | 자산·tenant·매출 없는 AI 테마                                     |
| `DISCLOSURE_CONFIDENCE_CAP`             |     cap |        cap |        cap |        cap |       cap |     cap |    + | 계약·tenant·NOI/AFFO·PF detail 부족                           |

Loop 5에서 핵심 보정은 이거다.

```text
1. DATA_CENTER_REIT_IPO_NO_ASSET을 유지/강화.
   BXDC처럼 sponsor는 강해도 자산·tenant·AFFO가 없으면 Stage 3 금지.

2. AI_POWER_DATA_CENTER_CAMPUS를 추가.
   Fermi처럼 power campus narrative가 강해도 tenant·매출·permitting 전까지 high-risk Watch다.

3. DATA_CENTER_LOCAL_MORATORIUM_OVERLAY를 추가.
   Perth 철회, Utah 반발, Seattle/Indianapolis moratorium이 project delay risk를 보여줬다.

4. DATA_CENTER_CAPEX_AFFO_DILUTION을 gate로 유지.
   Equinix처럼 AI 수요는 진짜여도 CAPEX가 AFFO/share를 누르면 valuation이 깨진다.

5. COLD_CHAIN_DEBT_OCCUPANCY_RISK를 gate로 유지.
   Lineage처럼 규모와 NOI가 있어도 순손실·debt·occupancy risk가 크면 Green 제한.

6. LOW_CARBON_CEMENT_PREMIUM을 추가.
   Heidelberg evoZero처럼 green cement demand는 실제지만, subsidy와 green premium 지속성을 확인해야 한다.

7. BUILDING_PRODUCTS_MNA_SHIFT를 추가.
   Holcim/Xella처럼 건자재 기업이 cement cycle에서 building products로 전환할 수 있지만, multiple·integration·leverage를 검증해야 한다.

8. BUILDING_MATERIALS_PRICE_COST는 가격전가 성공 시 후보지만,
   출하량과 EBITDA가 약하면 mixed/cycle로 분리.
```

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

## `PF_RESTRUCTURING_RELIEF`

```text
Stage 1:
정부 보증·대출·시장안정펀드 발표

Stage 2:
개별 프로젝트 refinancing 성공, 본PF 전환, 부실 프로젝트 분리 확인

Stage 3:
건설사 cash conversion과 원가율이 실제 개선될 때만

Stage 4B:
정책지원만으로 건설주 동반 급등

Stage 4C:
지원에도 불구하고 연체율 상승, 워크아웃, 손상차손 발생
```

## `COMMERCIAL_REAL_ESTATE_CREDIT`

```text
Stage 1:
고배당·금리하락·CRE 회복 기대

Stage 2:
watch-listed loans 감소, impaired loans 감소, reserve 안정 확인

Stage 3:
배당 커버리지와 loan performance가 정상화될 때만

Stage 4B:
고배당 REIT yield chase 과열

Stage 4C:
office vacancy, impaired loans, credit reserve 증가, dividend cut
```

## `DATA_CENTER_REIT_INFRASTRUCTURE`

```text
Stage 1:
AI 데이터센터 REIT IPO, hyperscale demand, asset pipeline 뉴스

Stage 2:
자산 취득, tenant lease, power/cooling/water 확보, NOI/AFFO 확인

Stage 3:
FFO/AFFO growth와 배당 커버리지 안정 확인

Stage 4B:
AI infrastructure real estate valuation 과열

Stage 4C:
자산 미취득, tenant 부재, power/water permitting 실패, funding cost 상승
```

## `DATA_CENTER_REIT_IPO_NO_ASSET`

```text
Stage 1:
AI 데이터센터 IPO, sponsor track record, acquisition pipeline 제시

Stage 2:
실제 asset acquisition, binding tenant lease, power/water secured 확인

Stage 3:
NOI/AFFO와 dividend coverage가 확인되기 전까지 금지

Stage 4B:
자산 없이 AI infrastructure valuation 과열

Stage 4C:
asset acquisition 지연, tenant 미확정, IPO discount, funding cost 상승
```

## `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT`

```text
Stage 1:
AI data-center campus, dedicated power, land/power narrative

Stage 2:
tenant LOI가 아니라 binding lease/PPA, power secured, permitting, financing 확인

Stage 3:
실제 매출, NOI/AFFO, tenant concentration 관리 확인

Stage 4B:
무매출 AI real asset valuation 과열

Stage 4C:
power delivery 지연, tenant 미확정, funding gap, water/local opposition, capex overrun
```

## `DATA_CENTER_POWER_WATER_PERMITTING`

```text
Stage 1:
AI 데이터센터 수요와 campus 개발 발표

Stage 2:
전력계통 접속, water rights, zoning, community approval, PPA 확인

Stage 3:
인허가·전력·수자원이 확보되고 tenant·NOI/AFFO가 붙을 때

Stage 4B:
전력·수자원 리스크 무시한 AI real asset 과열

Stage 4C:
moratorium, referendum, project withdrawal, water permit failure, noise/environmental rejection
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
순손실, 에너지비 상승, occupancy 하락, debt 부담, post-IPO drawdown
```

## `BUILDING_MATERIALS_PRICE_COST`

```text
Stage 1:
가격인상, 원가 안정, 착공 회복, 인프라 투자 뉴스

Stage 2:
출하량 회복, OPM 개선, 가격 전가 확인

Stage 3:
착공 cycle 개선과 FCF 안정 확인

Stage 4B:
건자재 가격인상 narrative 과열

Stage 4C:
착공 둔화, 출하량 하락, 원재료·에너지비 상승, EBITDA 감소
```

## `LOW_CARBON_CEMENT_PREMIUM`

```text
Stage 1:
net-zero cement, CCS, green construction demand 뉴스

Stage 2:
pre-sale, 고객계약, carbon capture facility, 생산량 확인

Stage 3:
보조금 의존을 넘어 green premium과 FCF가 확인될 때

Stage 4B:
친환경 건자재 premium 과열

Stage 4C:
보조금 축소, CCS 비용 초과, 고객 premium 지불 의지 약화
```

## `BUILDING_PRODUCTS_MNA_SHIFT`

```text
Stage 1:
cement 기업의 walling/roofing/insulation 등 building products M&A

Stage 2:
target 매출·EBITDA·multiple·synergy guidance 확인

Stage 3:
integration 후 margin/FCF 개선과 leverage 안정 확인

Stage 4B:
M&A narrative 과열

Stage 4C:
integration failure, multiple overpay, debt burden, synergy miss
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

## R10 Loop 5 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. PF 지표, 미분양, NOI/AFFO, 배당, occupancy, 원가율, 출하량,
   금리, tenant lease, power/water permitting과 가격경로를 비교한다.
```

## Loop 5에서 새로 강제할 판정

```text
PF_RELIEF_NOT_RECOVERY:
정부지원이나 금리 기대는 있지만 PF·미분양·현금흐름 개선 없음.

PF_CREDIT_RECOVERY_ALIGNED:
refinancing 성공, PF exposure 감소, cash conversion 개선, 주가 회복.

PF_SOFT_LANDING_BUT_NOT_GREEN:
syndicated loan·보증은 있으나 부실 프로젝트 선별 전.

REIT_AFFO_ALIGNED:
NOI/AFFO, occupancy, 배당 커버리지가 가격경로와 동행.

REIT_AFFO_INTEGRITY_RISK:
AFFO가 maintenance capex 분류·capex burden으로 의심되는 경우.

DATA_CENTER_REIT_THEME_NO_ASSET:
AI 데이터센터 테마는 있으나 자산·tenant·AFFO 없음.

DATA_CENTER_CAPEX_AFFO_BREAK:
CAPEX가 커지는데 AFFO/share growth가 둔화되는 경우.

AI_REAL_ASSET_NO_REVENUE_HIGH_RISK:
무매출·장기 개발·전력/수자원/tenant 리스크가 큰 경우.

AI_POWER_CAMPUS_TENANT_GAP:
power campus narrative는 있으나 binding tenant lease 없음.

DATA_CENTER_POWER_WATER_4C:
전력·수자원·지역반발·소음·인허가 때문에 project delay 또는 철회.

DATA_CENTER_LOCAL_MORATORIUM:
지자체 moratorium, zoning pause, referendum이 project timing을 훼손.

COLD_CHAIN_SCALE_BUT_LOSS:
창고 규모와 고객은 크지만 순손실·에너지비·debt가 남은 경우.

BUILDING_MATERIALS_PRICE_COST_ALIGNED:
가격전가·비용관리·출하량·OPM이 같이 확인되는 경우.

BUILDING_MATERIALS_VOLUME_FAILURE:
가격인상은 있지만 출하량·EBITDA·수요가 약한 경우.

LOW_CARBON_CEMENT_STAGE2:
pre-sale과 CCS는 있지만 보조금·green premium 지속성 검증 필요.

BUILDING_PRODUCTS_MNA_SHIFT:
M&A로 mix 개선 가능하지만 multiple·leverage·synergy 검증 필요.

POLICY_RECONSTRUCTION_EVENT:
우크라·네옴·세종시 등 정책 뉴스는 있으나 실제 계약 없음.
```

## 이번 R10 Loop 5에서 우선 검증할 가격 case

| case_id                                       |      stage2 후보일 | 현재 1차 가격판정                                            |
| --------------------------------------------- | --------------: | ----------------------------------------------------- |
| `korea_pf_delinquency_restructuring_case`     |      2024-05-13 | PF hard counterexample                                |
| `korea_builder_support_relief_case`           |      2024-03-27 | policy relief, not structural success                 |
| `korea_pf_syndicated_loan_soft_landing_case`  |      2024-05-13 | soft landing support, still Watch                     |
| `blackstone_mortgage_trust_dividend_cut_case` |         2024-07 | CRE credit 4C                                         |
| `equinix_affo_integrity_short_case`           |      2024-03-20 | data-center REIT AFFO integrity risk                  |
| `equinix_ai_capex_burden_case`                |      2025-06-26 | -8%, AI capex pressure                                |
| `equinix_malaysia_ai_liquid_cooling_case`     |      2026-05-12 | AI/HPC expansion but power/water watch                |
| `blackstone_data_center_reit_flat_debut_case` |      2026-05-14 | flat debut, no asset yet                              |
| `fermi_ai_data_center_no_revenue_case`        |      2025-09-30 | high-risk AI real asset                               |
| `fermi_no_tenant_net_loss_case`               |      2026-03-30 | tenant 부재 + 큰 손실, 4C-watch                            |
| `perth_datacenter_withdrawal_case`            |      2026-05-15 | local opposition / project withdrawal                 |
| `utah_stratos_datacenter_backlash_case`       |      2026-05-13 | 9GW power/water local opposition                      |
| `seattle_datacenter_moratorium_case`          |      2026-05-15 | urban data center moratorium Watch                    |
| `indianapolis_datacenter_moratorium_case`     |      2026-05-15 | local moratorium Watch                                |
| `lineage_cold_storage_ipo_case`               |      2024-07-25 | scale success but net loss watch                      |
| `heidelberg_materials_price_cost_case`        |      2025-11-06 | +74% YTD, aligned candidate                           |
| `heidelberg_evozero_low_carbon_cement_case`   |      2025-06-18 | net-zero cement pre-sold, subsidy/green premium watch |
| `cemex_demand_slowdown_costcut_case`          |      2025-02-06 | mixed: cost-cut but volume weakness                   |
| `cemex_price_cost_restructuring_case`         | 2025-10~2026-04 | price/cost improvement but volume/capex watch         |
| `holcim_xella_building_products_mna_case`     |      2025-10-20 | building products M&A shift                           |
| `ukraine_reconstruction_event_watch_case`     |             계약별 | actual contract before Green                          |
| `neom_city_event_watch_case`                  |             계약별 | actual contract before Green                          |
| `sejong_policy_theme_case`                    |          정책 발표일 | Event only until budget/contract                      |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R10 Loop 5에서는 아래 필드를 채우게 해야 한다.

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
peak_date

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
below_stage2_price_flag
below_stage3_price_flag

pf_exposure
pf_guarantee_amount
pf_delinquency_rate
bridge_loan_exposure
refinancing_success_flag
debt_workout_flag
syndicated_loan_amount
pf_soft_landing_support_flag
unsold_inventory_units
cash_conversion_cycle
construction_cost_ratio
gross_margin
op_margin_change
profitable_project_flag
unprofitable_project_restructuring_flag

revenue_backlog
contract_value
contract_duration_months
contract_margin_signal
project_financing_secured_flag
construction_started_flag
revenue_recognized_flag

reit_type
occupancy_rate
noi_growth
affo_growth
ffo_growth
affo_per_share_growth
dividend_per_share
dividend_cut_flag
dividend_coverage_ratio
ltv_ratio
funding_cost
refinancing_maturity
office_exposure
watchlisted_or_impaired_asset_ratio
credit_loss_reserve
non_accrual_asset_ratio

maintenance_capex
expansion_capex
capex_amount
capex_to_affo_ratio
affo_integrity_risk_flag
short_report_flag

data_center_asset_acquired_flag
hyperscale_tenant_flag
tenant_concentration
binding_lease_flag
non_binding_loi_flag
investment_grade_tenant_flag
power_secured_flag
water_permitting_flag
cooling_secured_flag
advanced_liquid_cooling_flag
grid_interconnection_flag
asset_pipeline_value
ai_infra_theme_flag
no_revenue_flag
single_site_concentration_flag
power_delivery_date
local_opposition_flag
referendum_or_moratorium_flag
project_withdrawal_flag
noise_pollution_flag
urban_datacenter_moratorium_flag
zoning_pause_flag
community_submission_count

ai_power_campus_flag
planned_power_gw
planned_power_delivery_year
nuclear_power_plan_flag
gas_power_plan_flag
solar_power_plan_flag
tenant_signed_flag
tenant_funding_agreement_terminated_flag

cold_storage_warehouse_count
cold_storage_capacity
energy_cost_ratio
customer_count
net_loss_flag
cold_chain_occupancy_rate
post_ipo_drawdown_flag
customer_inventory_normalization_flag
debt_to_ebitda

building_material_volume
cement_price_change
steel_rebar_price_change
energy_cost_change
raw_material_cost_change
price_hike_flag
cost_saving_amount
ebitda_change
volume_decline_flag
infrastructure_demand_flag

low_carbon_cement_flag
net_zero_cement_flag
carbon_capture_capacity_tons
ccs_subsidy_flag
green_premium_flag
product_presold_flag
ccs_storage_contract_flag
subsidy_durability_risk_flag

building_products_mna_flag
target_revenue
target_ebitda
mna_multiple
earnings_accretive_guidance_flag
integration_risk_flag
leverage_after_mna

policy_support_amount
government_support_flag
reconstruction_contract_flag
budget_allocated_flag
project_delay_flag
financing_failure_flag

opendart_rcept_no
opendart_detail_fetched_flag
disclosure_confidence_score
detail_parser_confidence
disclosure_signal_class
routine_disclosure_flag
risk_disclosure_flag
high_signal_disclosure_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R10 Loop 5 결론

이번 5회차에서 R10은 더 좁혀졌다.

```text
Green 가능:
데이터센터 REIT 중 실제 자산·tenant·NOI/AFFO·전력/수자원이 확인된 경우
콜드체인 REIT 중 occupancy·NOI/AFFO·배당 커버리지가 확인된 경우
건자재 중 가격전가·비용관리·출하량·OPM이 같이 확인된 경우
대형 건설사 중 PF 노출이 낮고 cash conversion이 개선되는 경우
친환경 시멘트 중 보조금 이후에도 green premium과 FCF가 확인되는 경우
building products M&A 후 synergy·margin·leverage가 확인되는 경우

Watch-to-Green:
리츠 중 occupancy·AFFO·배당 커버리지가 안정적인 기업
AI 데이터센터 real asset 중 binding lease와 power/water secured가 확인되는 기업
콜드체인·물류창고 중 에너지비와 debt를 통제하는 기업
건자재 중 가격인상과 비용절감이 물량 회복과 같이 가는 기업
AI power campus 중 tenant·permitting·financing이 실제로 붙는 기업

Watch/Red:
중소형 건설사
개발신탁
오피스 노출 리츠
건자재 cycle
재건·네옴·세종시 정책 테마
무매출 AI data-center 개발사
자산 미취득 데이터센터 REIT
CAPEX가 AFFO/share보다 먼저 커지는 데이터센터 REIT

Hard 4C:
PF 연체율 상승
브릿지론 rollover 실패
워크아웃
오피스 공실·대출부실·배당삭감
AFFO 착시·maintenance capex 논란
자산·tenant 없는 데이터센터 REIT
무매출 AI real asset 과열
전력·수자원·지역반발로 인한 데이터센터 지연/철회
데이터센터 moratorium / zoning pause
데이터센터 CAPEX burden으로 AFFO/share 둔화
콜드체인 순손실·debt·occupancy 둔화
건자재 출하량 둔화·EBITDA 감소
계약·tenant·NOI/AFFO·PF detail 부족으로 인한 disclosure confidence cap
```

**R10 Loop 5 점수정규화의 핵심 문장:**

> 건설·부동산·건자재는 “수주잔고”, “배당률”, “AI 데이터센터”, “재건 테마”가 아니라 **PF 리스크, cash conversion, occupancy, NOI/AFFO, 배당 커버리지, funding cost, maintenance capex, tenant lease, power/water 확보, 지역 인허가, 출하량, 원가율**로 봐야 한다.
> Loop 5부터는 특히 `DATA_CENTER_REIT_IPO_NO_ASSET`, `AI_POWER_DATA_CENTER_CAMPUS`, `DATA_CENTER_POWER_WATER_PERMITTING`, `DATA_CENTER_LOCAL_MORATORIUM_OVERLAY`, `DATA_CENTER_CAPEX_AFFO_DILUTION`, `COLD_CHAIN_DEBT_OCCUPANCY_RISK`, `LOW_CARBON_CEMENT_PREMIUM`, `BUILDING_PRODUCTS_MNA_SHIFT`, `DISCLOSURE_CONFIDENCE_CAP`을 강한 보정축으로 넣어야 한다.

다음 순서는 **R11 — 정책·지정학·재난·이벤트 Loop 5**다.

[1]: https://www.reuters.com/business/heidelberg-materials-posts-higher-than-expected-q3-profit-cost-price-management-2025-11-06/ "https://www.reuters.com/business/heidelberg-materials-posts-higher-than-expected-q3-profit-cost-price-management-2025-11-06/"
[2]: https://www.reuters.com/sustainability/climate-energy/heidelberg-sells-out-net-zero-cement-norway-plant-ceo-says-2025-06-18/ "https://www.reuters.com/sustainability/climate-energy/heidelberg-sells-out-net-zero-cement-norway-plant-ceo-says-2025-06-18/"
[3]: https://www.reuters.com/business/mexican-cement-maker-cemex-ekes-out-profit-starts-350-million-savings-program-2025-02-06/ "https://www.reuters.com/business/mexican-cement-maker-cemex-ekes-out-profit-starts-350-million-savings-program-2025-02-06/"
[4]: https://www.reuters.com/business/cemex-posts-record-q1-earnings-maintains-outlook-despite-weather-hit-2026-04-23/ "https://www.reuters.com/business/cemex-posts-record-q1-earnings-maintains-outlook-despite-weather-hit-2026-04-23/"
[5]: https://www.reuters.com/business/holcim-agrees-185-billion-euro-deal-buy-walling-specialist-xella-2025-10-20/ "https://www.reuters.com/business/holcim-agrees-185-billion-euro-deal-buy-walling-specialist-xella-2025-10-20/"
[6]: https://www.reuters.com/technology/blackstone-data-center-vehicle-opens-flat-new-york-debut-after-175-billion-ipo-2026-05-14/ "https://www.reuters.com/technology/blackstone-data-center-vehicle-opens-flat-new-york-debut-after-175-billion-ipo-2026-05-14/"
[7]: https://www.reuters.com/world/asia-pacific/equinix-create-new-malaysia-data-centre-with-over-190-million-investment-2026-05-12/ "https://www.reuters.com/world/asia-pacific/equinix-create-new-malaysia-data-centre-with-over-190-million-investment-2026-05-12/"
[8]: https://www.investopedia.com/lineage-goes-public-in-biggest-ipo-of-2024-8683442 "https://www.investopedia.com/lineage-goes-public-in-biggest-ipo-of-2024-8683442"
[9]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/ "https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/"
[10]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/ "https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/"
[11]: https://www.businessinsider.com/blackstone-mortgage-trust-dividend-real-estate-office-pressures-2024-7 "https://www.businessinsider.com/blackstone-mortgage-trust-dividend-real-estate-office-pressures-2024-7"
[12]: https://www.reuters.com/business/media-telecom/hindenburg-research-takes-short-position-data-center-operator-equinix-2024-03-20/ "https://www.reuters.com/business/media-telecom/hindenburg-research-takes-short-position-data-center-operator-equinix-2024-03-20/"
[13]: https://www.reuters.com/business/equinix-shares-fall-revenue-capital-spending-forecast-disappoint-investors-2025-06-26/ "https://www.reuters.com/business/equinix-shares-fall-revenue-capital-spending-forecast-disappoint-investors-2025-06-26/"
[14]: https://www.reuters.com/business/rick-perrys-data-center-reit-raises-682-million-us-ipo-2025-09-30/ "https://www.reuters.com/business/rick-perrys-data-center-reit-raises-682-million-us-ipo-2025-09-30/"
[15]: https://www.ft.com/content/49a8b5c8-d655-4eb8-b0dc-6bd403860925 "https://www.ft.com/content/49a8b5c8-d655-4eb8-b0dc-6bd403860925"
[16]: https://www.theguardian.com/technology/2026/may/15/developer-withdraws-plans-for-perth-datacentre-after-fierce-community-opposition "https://www.theguardian.com/technology/2026/may/15/developer-withdraws-plans-for-perth-datacentre-after-fierce-community-opposition"
[17]: https://www.theguardian.com/us-news/2026/may/13/utah-approves-datacenter-backlash "https://www.theguardian.com/us-news/2026/may/13/utah-approves-datacenter-backlash"
