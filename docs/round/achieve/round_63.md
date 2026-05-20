좋아. **R9 Loop 2까지 끝났으니, 이번은 R10 Loop 2 — 건설·부동산·건자재**로 넘어간다.

R10은 Theme Tag Map 기준으로 대형 건설사, 중소형 건설사, 부동산 자산 보유, 개발신탁리츠, 건자재, 시멘트·레미콘·콘크리트, 철근, 가구, 거푸집, 우크라 재건, 네옴시티, 세종시를 흡수하는 대섹터다. 이 지도에서도 건설은 **PF와 현금흐름이 먼저**이고, 수주잔고만으로 Green을 주면 위험하다고 정리되어 있다.

서생원식으로 보면 R10의 핵심은 “부동산 회복”이나 “AI 데이터센터 부동산”이라는 이름이 아니라, **PF 리스크·금리·공실·원가율·NOI/AFFO·배당 커버리지·실제 tenant/자산/계약이 EPS/FCF 체급 변화로 이어지는가**다.
또 Checkpoint 20 원칙처럼 계약금액, PF 익스포저, 배당, AFFO, occupancy, 원가율, 자산 취득 여부 같은 값은 실제 확인된 증거만 써야 하고, 비어 있는 값을 추정해서 채우면 안 된다.

---

# R10 Loop 2. 건설·부동산·건자재

## 1. 이번 라운드 대섹터

```text
R10 = 건설·부동산·건자재
Loop 2 목표 = PF credit risk / REIT cashflow / AI data-center real asset / 건자재 cycle을 분리
```

이번 회차의 핵심 질문은 이거다.

```text
이 기업은 진짜 현금흐름이 회복되고 있는가?
아니면 정책지원, 금리인하 기대, 데이터센터 테마, 재건 테마, 고배당 착시로 움직이는가?
```

R10에서 가장 흔한 오판은 아래다.

```text
1. 정부 PF 지원을 구조적 회복으로 착각
2. 건설사 수주잔고를 현금흐름 회복으로 착각
3. 리츠 배당률을 배당 지속성으로 착각
4. 데이터센터 REIT를 tenant/AFFO 없이 AI 인프라 Green으로 처리
5. 콜드체인 규모를 순이익·AFFO 검증 없이 Green으로 처리
6. 건자재 가격인상을 출하량·원가 확인 없이 구조적 리레이팅으로 처리
7. 우크라 재건·네옴시티·세종시를 실제 계약 없이 Stage 3로 오분류
```

---

## 2. 대상 canonical archetype

| canonical archetype                     | Loop 2 정책                                              |
| --------------------------------------- | ------------------------------------------------------ |
| `CONSTRUCTION_REAL_ESTATE_CREDIT`       | Watch/Red. PF·미분양·원가율·cash conversion 먼저               |
| `REIT_DEVELOPMENT_TRUST`                | Watch. 금리·LTV·occupancy·배당 커버리지 확인                     |
| `BUILDING_MATERIALS_CYCLE`              | Watch. 가격전가·출하량·원가·착공량 확인                              |
| `DATA_CENTER_REIT_INFRASTRUCTURE`       | Watch-to-Green. 실제 자산·tenant·NOI/AFFO·전력 확보 필요         |
| `COLD_CHAIN_REIT_LOGISTICS`             | Watch-to-Green. occupancy·NOI/AFFO·에너지비·debt 확인        |
| `INFRA_RECONSTRUCTION_POLICY`           | Event/Watch. 실제 계약·financing·착공 전 Green 금지             |
| `DISASTER_REBUILD_EVENT`                | Event/Watch. one-off 복구수요와 반복매출 분리                     |
| `COMMERCIAL_REAL_ESTATE_CREDIT`         | Watch/Red. 오피스 공실·대출부실·배당삭감 hard risk                  |
| `RESIDENTIAL_HOUSING_CYCLE`             | Watch. 미분양·가계부채·금리·착공량 확인                              |
| `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT` | High-risk Watch. 자산·전력·water·tenant·revenue 전 Green 금지 |
| `PF_CREDIT_REDTEAM_OVERLAY`             | RedTeam gate. PF 연체·브릿지론·워크아웃                          |
| `REIT_AFFO_INTEGRITY_OVERLAY`           | RedTeam gate. AFFO 착시·maintenance capex·배당 커버리지        |
| `AI_INFRA_REAL_ASSET_THEME_OVERLAY`     | RedTeam gate. 무매출 AI data-center 부동산 테마                |

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

REIT_DEVELOPMENT_TRUST
- 리츠
- 개발신탁
- 물류센터
- 오피스
- 리테일 자산
- NAV discount
- 배당 커버리지
- LTV
- refinancing
- funding cost

COMMERCIAL_REAL_ESTATE_CREDIT
- 오피스 공실
- watch-listed loans
- impaired loans
- credit loss reserve
- dividend cut
- non-accrual loans

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
- 에너지비
- 원재료비
- 출하량

DATA_CENTER_REIT_INFRASTRUCTURE
- 데이터센터 REIT
- hyperscale tenant
- investment-grade tenant
- power-secured asset
- cooling/water
- NOI/AFFO
- capex
- funding cost
- tenant concentration

AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT
- AI data-center campus
- dedicated power
- nuclear/gas/solar mix
- long-term power contract
- no-revenue development-stage REIT
- permitting
- execution risk

COLD_CHAIN_REIT_LOGISTICS
- 냉동창고
- 냉장창고
- 식품 supply chain
- 의약품 cold chain
- temperature-controlled warehouse
- occupancy
- energy cost
- NOI/AFFO
- debt

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

# 4. 성공사례

## 4-1. Heidelberg Materials — 건자재가 Watch-to-Green으로 올라가는 조건

Heidelberg Materials는 비용절감과 가격인상 관리로 2025년 3분기 영업이익이 예상보다 높게 나왔고, 2025년 주가가 74% 상승했다. 이 회사는 2026년 말까지 최소 5억 유로의 연간 비용절감 목표도 제시했다. 즉 건자재도 단순 “건설경기 회복”이 아니라 **가격전가 + 비용관리 + 인프라 수요 + 이익 가시성**이 같이 붙으면 Watch-to-Green 후보가 될 수 있다. ([Reuters][1])

```text
가격경로 1차 판정:
BUILDING_MATERIALS_PRICE_COST_ALIGNED_CANDIDATE

좋은 점:
- 비용절감
- 가격인상
- 인프라 투자 기대
- 이익 전망 범위 상향/정교화
- 2025년 주가 +74%

주의:
- 출하량 둔화 가능성
- 에너지비
- 건설경기
- 원재료비
- 가격인상 지속성
```

**Loop 2 교정**

```text
BUILDING_MATERIALS_CYCLE:
가격인상만으로 Green 금지.
출하량 + 비용관리 + OPM + FCF가 같이 확인되면 Watch-to-Green.
```

---

## 4-2. Blackstone Digital Infrastructure Trust — 데이터센터 REIT Stage 1~2 후보지만 아직 Green 아님

Blackstone Digital Infrastructure Trust는 2026년 5월 17.5억 달러 IPO를 했고, newly constructed data center assets를 investment-grade hyperscale tenant에게 임대하는 전략을 제시했다. 다만 상장 첫날 주가는 IPO가 20달러와 같은 가격으로 flat debut했고, Reuters는 아직 데이터센터 자산을 취득하지 않은 상태에서 투자자들이 Blackstone의 실행력과 sector history를 사는 구조라고 설명했다. ([Reuters][2])

```text
가격경로 1차 판정:
DATA_CENTER_REIT_THEME_WITHOUT_ASSETS_YET

좋은 점:
- Blackstone execution capability
- QTS/AirTrunk 등 digital infra track record
- hyperscale tenant 대상 전략
- $25B near-term opportunities 검토

주의:
- 아직 자산 취득 없음
- tenant lease 미확인
- NOI/AFFO 미확인
- funding cost
- AI infrastructure IPO window 과열 가능성
```

**Loop 2 교정**

```text
DATA_CENTER_REIT_INFRASTRUCTURE:
AI 데이터센터 수요는 Stage 1.
실제 asset acquisition + tenant lease + power/water secured + NOI/AFFO 전까지 Green 금지.
```

---

## 4-3. Lineage cold-storage REIT — scale은 강하지만 profitability gate가 필요

Lineage는 세계 최대 cold-storage warehouse operator로 2024년 IPO에서 44.4억 달러를 조달했고, 482개 temperature-controlled warehouse와 13,000개 이상 food supply-chain customers를 가진 것으로 보도됐다. 하지만 같은 Reuters 보도는 상장 전 12개월 기준 순손실 1.628억 달러도 함께 언급했다. 즉 콜드체인은 규모·고객·자산이 강한 후보지만, **NOI/AFFO·에너지비·debt·배당 커버리지**를 통과해야 Green이다. ([Reuters][3])

```text
가격경로 1차 판정:
COLD_CHAIN_SCALE_SUCCESS_CANDIDATE_BUT_PROFITABILITY_WATCH

좋은 점:
- 세계 최대급 cold-storage network
- 식품 supply chain 고객 기반
- 온도관리 물류 수요
- IPO 수요 강함

주의:
- 순손실
- 에너지비
- debt
- occupancy
- AFFO/배당 커버리지
```

**Loop 2 교정**

```text
COLD_CHAIN_REIT_LOGISTICS:
Green 가능은 유지.
하지만 scale, 창고 수, 고객 수만으로 Stage 3 금지.
NOI/AFFO와 energy cost ratio를 반드시 본다.
```

---

## 4-4. Cemex 구조조정 — 건자재 cost-cut survival 후보

Cemex는 2024년 4분기 매출이 전년 대비 5% 감소했지만, 가격인상으로 일부를 상쇄했고 2027년까지 3.5억 달러 earnings boost를 목표로 하는 savings program을 발표했다. 2025년 2분기에는 매출이 5% 줄고 EBITDA가 11% 감소했지만, 구조조정 효과로 순이익은 38% 증가했고 비용절감 목표도 상향됐다. ([Reuters][4])

```text
가격경로 1차 판정:
BUILDING_MATERIALS_COST_CUT_MIXED_CASE

좋은 점:
- 가격인상
- 비용절감
- 구조조정
- 일부 지역 인프라 수요

주의:
- 판매량 감소
- 핵심시장 수요 둔화
- EBITDA 감소
- layoffs 기반 비용절감
```

**Loop 2 교정**

```text
BUILDING_MATERIALS_CYCLE:
비용절감으로 EPS가 좋아져도 출하량이 약하면 structural_success가 아니라 mixed/cycle로 분류.
```

---

## 4-5. 한국 정부 PF 지원 — relief rally 후보, 구조적 성공은 아님

한국 정부는 2024년 3월 고금리와 부동산 경기 둔화로 어려움을 겪는 건설사·중소기업을 지원하기 위해 총 40.6조 원 금융지원책을 발표했다. 건설사에는 보증 확대, 추가 대출, 시장안정펀드 지원을 통해 “수익성 있는 부동산 프로젝트”의 자금조달을 돕겠다고 밝혔다. ([Reuters][5])

```text
가격경로 1차 판정:
PF_POLICY_RELIEF_STAGE1

좋은 점:
- 정책 유동성 지원
- 보증 확대
- 수익성 있는 프로젝트 soft landing 지원

주의:
- 수익성 없는 프로젝트는 구조조정 대상
- 정책지원 자체는 EPS/FCF 회복이 아님
- PF 부실 정리 전 Green 금지
```

**Loop 2 교정**

```text
CONSTRUCTION_REAL_ESTATE_CREDIT:
정부 지원은 Stage 1 relief.
Stage 2는 실제 refinancing 성공과 cash conversion 개선.
Stage 3는 PF risk가 낮아지고 EPS/FCF가 회복될 때만.
```

---

# 5. 반례

## 5-1. 한국 PF 연체율 상승 — `CONSTRUCTION_REAL_ESTATE_CREDIT` hard counterexample

한국 금융감독원은 부동산 프로젝트 평가를 강화하고 구조조정을 촉진하겠다고 밝혔다. 부동산 프로젝트 연체율은 2021년 말 0.37%에서 2022년 말 1.19%, 2023년 말 2.70%까지 상승했다. 이는 건설사·PF 관련주에서 수주잔고보다 **PF 보증·브릿지론·미분양·refinancing**을 먼저 봐야 하는 이유다. ([Reuters][6])

```text
가격경로 1차 판정:
PF_CREDIT_RISK_HARD_COUNTEREXAMPLE

교훈:
수주잔고
≠ Green

건설사는:
- PF exposure
- bridge loan rollover
- 미분양
- debt workout
- cash conversion
- 원가율

이 먼저다.
```

**Loop 2 교정**

```text
CONSTRUCTION_REAL_ESTATE_CREDIT:
Green 거의 제한.
PF exposure와 refinancing_success_flag가 없으면 Stage 3 금지.
```

---

## 5-2. Blackstone Mortgage Trust — 오피스 공실·대출부실·배당삭감 hard 4C

Blackstone Mortgage Trust는 오피스 공실과 고금리 압박 속에서 배당을 24% 삭감했고, 주가는 10% 하락했다. 회사는 추가 credit loss reserve 1.4억 달러를 쌓았고, 미국 오피스 exposure 중 55%가 watch-listed 또는 impaired로 분류됐다. ([Reuters][7])

```text
가격경로 1차 판정:
COMMERCIAL_REAL_ESTATE_CREDIT_4C

4C 조건:
- office vacancy
- impaired loans
- watch-listed loans
- credit loss reserve
- dividend cut
- share price drawdown
```

**Loop 2 교정**

```text
COMMERCIAL_REAL_ESTATE_CREDIT:
배당률이 높아도 dividend_coverage와 impaired_asset_ratio가 나쁘면 Red.
```

---

## 5-3. 데이터센터 REIT AFFO integrity risk — Equinix Hindenburg case

Hindenburg Research는 데이터센터 REIT Equinix에 대해 maintenance capex를 expansion capex로 분류해 AFFO를 과대 표시했다는 의혹을 제기했고, Equinix 주가는 해당 공개 후 약 2% 하락했다. 이 사례는 데이터센터 REIT에서도 **AFFO가 진짜 현금흐름인지, capex 분류가 건전한지**를 봐야 한다는 RedTeam 기준이다. ([Reuters][8])

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

**Loop 2 교정**

```text
REIT_AFFO_INTEGRITY_OVERLAY:
AFFO 성장과 배당 커버리지는 capex 분류 검증을 통과해야 한다.
```

---

## 5-4. 데이터센터 CAPEX 부담 — Equinix AI growth의 또 다른 4B/4C-watch

Equinix는 AI 수요 대응을 위해 2026~2029년 연간 CAPEX를 40억~50억 달러로 높이겠다고 밝혔고, 투자자들은 단기 수익성 부담을 우려해 주가를 9.6% 끌어내렸다. 이는 AI 데이터센터 수요가 있어도 **CAPEX가 AFFO·배당·수익률을 압박하면 주가가 하락할 수 있음**을 보여준다. ([Barron's][9])

```text
가격경로 1차 판정:
AI_DATA_CENTER_CAPEX_BURDEN_4B_TO_4C_WATCH

교훈:
AI data-center demand
≠ 무조건 REIT Green

CAPEX가 AFFO growth보다 먼저 커지면 valuation이 눌린다.
```

---

## 5-5. Fermi — 무매출 AI 데이터센터 real asset의 high-risk Watch

Fermi는 AI 전력·데이터센터 캠퍼스 개발을 목표로 2025년 IPO에서 6.825억 달러를 조달했고, valuation은 124.6억 달러로 책정됐다. 회사는 2038년까지 최대 11GW 전력을 공급하는 AI 데이터센터 캠퍼스를 계획하지만, Reuters는 회사가 아직 초기 개발 단계이고 향후 12개월 내 매출을 기대하지 않으며, 설립 이후 640만 달러 손실을 기록했다고 보도했다. ([Reuters][10])

```text
가격경로 1차 판정:
AI_REAL_ASSET_NO_REVENUE_HIGH_RISK_WATCH

좋은 점:
- AI 전력·데이터센터 수요에 직접 노출
- 대규모 토지·전력 개발 narrative
- 전력 병목에 대한 투자자 관심

주의:
- 무매출
- 장기 개발계획
- 전력·원전·가스·태양광 execution risk
- tenant 계약 불확실
- permitting/funding risk
```

**Loop 2 교정**

```text
AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT:
매출 전 high-risk Watch.
tenant lease + power secured + revenue + AFFO 전까지 Green 금지.
```

---

## 5-6. 콜드체인 post-IPO drawdown risk

Lineage는 IPO 당시 scale과 고객 기반이 강했지만, 이후 냉장창고 수요 둔화·인플레이션으로 식품업체 재고 관리가 약해지며 감원 계획이 보도됐고, 주가가 8월 고점 대비 37% 하락했다는 보도도 나왔다. 이건 cold-chain scale이 있더라도 **demand normalization, net loss, energy cost, debt**가 가격경로를 깨뜨릴 수 있음을 보여준다. ([월스트리트저널][11])

```text
가격경로 1차 판정:
COLD_CHAIN_SCALE_TO_PROFITABILITY_4C_WATCH

교훈:
cold-chain warehouse 수요
≠ 무조건 Green

Scale 다음에는:
- occupancy
- NOI/AFFO
- energy cost
- debt
- dividend coverage
를 확인해야 한다.
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

한국의 40.6조 원 지원책은 relief rally를 만들 수 있지만, 이 정책은 “수익성 있는 프로젝트”를 살리는 구조라서 부실 프로젝트의 구조조정 리스크는 남는다. ([Reuters][5])

---

## 6-2. 데이터센터 REIT IPO 4B-watch

```text
4B 조건:
- AI infrastructure IPO window가 열림
- 자산·tenant·AFFO 없이 Blackstone track record만으로 valuation 형성
- capex·funding cost·power/water risk를 시장이 낮게 봄
```

Blackstone Digital Infrastructure Trust는 IPO 규모와 sponsor는 강하지만, 아직 데이터센터 자산을 취득하지 않은 상태에서 flat debut했다. ([Reuters][2])

---

## 6-3. AI real asset no-revenue 4B-watch

```text
4B 조건:
- 무매출 개발 단계인데 AI 전력·데이터센터 narrative로 고평가
- 2030년대 장기 계획을 현재 valuation에 반영
- tenant·power·water·permitting·financing이 미확정
```

Fermi는 장기적으로 11GW campus 계획을 제시했지만, 초기 단계·무매출·장기 execution risk가 큰 high-risk Watch다. ([Reuters][10])

---

## 6-4. 콜드체인 REIT premium 4B-watch

```text
4B 조건:
- cold-chain warehouse scale만으로 premium 형성
- 순손실·energy cost·debt·AFFO 미확인
- food/pharma temperature-control narrative가 과밀
```

Lineage는 IPO 규모와 warehouse network는 강하지만, 순손실과 post-IPO 수요 둔화 리스크를 같이 봐야 한다. ([Reuters][3])

---

## 6-5. 건자재 가격인상 4B-watch

```text
4B 조건:
- 가격인상·인프라 기대만으로 건자재주 동반 상승
- 출하량 둔화와 원가 부담을 무시
- 비용절감이 구조적 수요 회복처럼 오분류
```

Heidelberg Materials는 가격·비용 관리로 좋은 성과를 냈지만, Cemex는 가격인상에도 핵심시장 물량 둔화와 EBITDA 감소가 확인됐다. ([Reuters][1])

---

# 7. 4C-thesis-break 사례

## 7-1. PF 연체율 상승

```text
4C:
PF_delinquency_increase
bridge_loan_rollover_failure
debt_workout
unprofitable_project_restructuring
```

PF 연체율이 2021년 말 0.37%에서 2023년 말 2.70%까지 상승한 것은 R10의 핵심 hard 4C다. ([Reuters][6])

---

## 7-2. 오피스 공실·대출부실·배당삭감

```text
4C:
office_vacancy
watchlisted_or_impaired_loans
credit_loss_reserve
dividend_cut
share_price_drop
```

Blackstone Mortgage Trust의 배당 24% 삭감과 주가 10% 하락은 commercial real estate credit의 기준 반례다. ([Reuters][7])

---

## 7-3. 데이터센터 REIT AFFO / capex integrity

```text
4C-watch:
AFFO_overstatement_allegation
maintenance_capex_misclassification
AI_pipe_dream_narrative
power_constraint
hyperscaler_concentration
```

Equinix Hindenburg case는 데이터센터 REIT의 cashflow 품질을 반드시 검증해야 한다는 기준이다. ([Reuters][8])

---

## 7-4. AI data-center no-asset/no-revenue thesis break

```text
4C-watch:
no_revenue
no_acquired_assets
no_tenant_lease
power_permitting_delay
water_permitting_delay
funding_gap
execution_risk
```

Fermi와 BXDC는 둘 다 AI 인프라 narrative가 강하지만, 각각 무매출 개발 단계 또는 자산 미취득 상태라는 점 때문에 Green 전 AFFO/tenant/asset proof가 필수다. ([Reuters][10])

---

## 7-5. 콜드체인 순손실·수요 정상화

```text
4C-watch:
net_loss
energy_cost_pressure
inventory_normalization
occupancy_decline
debt_burden
post_IPO_drawdown
```

Lineage는 세계 최대급 규모에도 순손실이 있었고, post-IPO 이후 수요 둔화·감원·주가 drawdown 리스크가 보도됐다. ([Reuters][3])

---

## 7-6. 건자재 수요 둔화

```text
4C-watch:
volume_decline
price_hike_cannot_offset_demand
EBITDA_decline
construction_slowdown
cost_pressure
```

Cemex는 가격인상과 구조조정에도 핵심 시장 수요 둔화와 EBITDA 감소를 겪었다. 이건 건자재 가격인상만으로 Stage 3-Green을 주면 안 된다는 반례다. ([Reuters][4])

---

# 8. 점수비중 보정표 — R10 Loop 2 / v2.0

| canonical archetype                     | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 2 핵심 감점                                              |
| --------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | --------------------------------------------------------- |
| `CONSTRUCTION_REAL_ESTATE_CREDIT`       |      13 |          9 |          5 |         12 |         8 |       0 |    5 | PF, 미분양, refinancing, 원가율, cash conversion                |
| `REIT_DEVELOPMENT_TRUST`                |      15 |         16 |          5 |         13 |        11 |       5 |    5 | 금리, LTV, 공실, 배당 커버리지                                      |
| `BUILDING_MATERIALS_CYCLE`              |      17 |         13 |         12 |         10 |         9 |       3 |    5 | 착공 둔화, 출하량, 원가, 에너지비                                      |
| `DATA_CENTER_REIT_INFRASTRUCTURE`       |      18 |         22 |         18 |         13 |        12 |       5 |    5 | CAPEX, funding cost, tenant concentration, AFFO integrity |
| `COLD_CHAIN_REIT_LOGISTICS`             |      17 |         20 |         12 |         12 |        10 |       5 |    5 | 에너지비, occupancy, debt, 순손실, AFFO                          |
| `INFRA_RECONSTRUCTION_POLICY`           |      12 |         10 |          8 |         10 |         8 |       0 |    4 | 실제 수주 없음, financing, 정책 이벤트                               |
| `DISASTER_REBUILD_EVENT`                |      10 |          6 |          7 |          8 |         6 |       0 |    4 | one-off 수요, 보험·예산 지연                                      |
| `COMMERCIAL_REAL_ESTATE_CREDIT`         |      11 |          8 |          4 |         12 |         7 |       0 |    5 | 공실, impaired loans, 배당삭감                                  |
| `RESIDENTIAL_HOUSING_CYCLE`             |      15 |         12 |          5 |         12 |         9 |       1 |    5 | 미분양, 금리, 가계부채, 착공 둔화                                      |
| `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT` |      15 |         17 |         15 |         13 |         9 |       3 |    5 | 무매출, tenant 부재, power/water permitting                    |
| `PF_CREDIT_REDTEAM_OVERLAY`             |    gate |       gate |       gate |       gate |      gate |    gate | gate | PF 연체, 워크아웃, 브릿지론 실패                                      |
| `REIT_AFFO_INTEGRITY_OVERLAY`           |    gate |       gate |       gate |       gate |      gate |    gate | gate | AFFO 착시, maintenance capex 분류                             |
| `AI_INFRA_REAL_ASSET_THEME_OVERLAY`     |    gate |       gate |       gate |       gate |      gate |    gate | gate | 자산·tenant·매출 없는 AI 테마                                     |

Loop 2의 핵심 보정은 이거다.

```text
1. CONSTRUCTION_REAL_ESTATE_CREDIT 점수는 더 낮춘다.
   PF 연체·구조조정 반례가 강하기 때문.

2. DATA_CENTER_REIT_INFRASTRUCTURE는 Watch-to-Green 유지.
   하지만 asset/tenant/AFFO 전까지 Green 금지.

3. AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT는 별도 high-risk Watch로 분리.
   Fermi처럼 무매출·장기개발·전력인허가 리스크가 크기 때문.

4. COLD_CHAIN_REIT_LOGISTICS는 Green 가능을 유지하되,
   순손실·에너지비·occupancy·debt 감점을 강화.

5. BUILDING_MATERIALS_CYCLE은 가격전가 성공 시 후보지만,
   출하량과 EBITDA가 약하면 cyclical/mixed로 분리.
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

## R10 Loop 2 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. 해당 날짜의 종가를 stage_price로 저장한다.
3. MFE_30D / 90D / 180D / 1Y / 2Y를 계산한다.
4. MAE_30D / 90D / 180D / 1Y를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. PF 지표, 미분양, NOI/AFFO, 배당, occupancy, 원가율, 출하량, 금리, tenant lease와 가격경로를 비교한다.
```

## Loop 2에서 새로 강제할 판정

```text
PF_RELIEF_NOT_RECOVERY:
정부지원이나 금리 기대는 있지만 PF·미분양·현금흐름 개선 없음.

PF_CREDIT_RECOVERY_ALIGNED:
refinancing 성공, PF exposure 감소, cash conversion 개선, 주가 회복.

REIT_AFFO_ALIGNED:
NOI/AFFO, occupancy, 배당 커버리지가 가격경로와 동행.

REIT_AFFO_INTEGRITY_RISK:
AFFO가 maintenance capex 분류·capex burden으로 의심되는 경우.

DATA_CENTER_REIT_THEME_NO_ASSET:
AI 데이터센터 테마는 있으나 자산·tenant·AFFO 없음.

AI_REAL_ASSET_NO_REVENUE_HIGH_RISK:
무매출·장기 개발·전력/수자원/tenant 리스크가 큰 경우.

COLD_CHAIN_SCALE_BUT_LOSS:
창고 규모와 고객은 크지만 순손실·에너지비·debt가 남은 경우.

BUILDING_MATERIALS_PRICE_COST_ALIGNED:
가격전가·비용관리·출하량·OPM이 같이 확인되는 경우.

BUILDING_MATERIALS_VOLUME_FAILURE:
가격인상은 있지만 출하량·EBITDA·수요가 약한 경우.

POLICY_RECONSTRUCTION_EVENT:
우크라·네옴·세종시 등 정책 뉴스는 있으나 실제 계약 없음.
```

## 이번 R10 Loop 2에서 우선 검증할 가격 case

| case_id                                       |              stage2 후보일 | 현재 1차 가격판정                                 |
| --------------------------------------------- | ----------------------: | ------------------------------------------ |
| `korea_pf_delinquency_restructuring_case`     |              2024-05-13 | PF hard counterexample                     |
| `korea_builder_support_relief_case`           |              2024-03-27 | policy relief, not structural success      |
| `blackstone_mortgage_trust_dividend_cut_case` |              2024-07-24 | -10%, CRE credit 4C                        |
| `equinix_affo_integrity_short_case`           |              2024-03-20 | data-center REIT AFFO integrity risk       |
| `equinix_ai_capex_burden_case`                |              2025-06-26 | -9.6%, AI capex pressure                   |
| `blackstone_data_center_reit_flat_debut_case` |              2026-05-14 | flat debut, no asset yet                   |
| `fermi_ai_data_center_no_revenue_case`        |              2025-09-30 | high-risk AI real asset                    |
| `lineage_cold_storage_ipo_case`               |              2024-07-24 | scale success but net loss watch           |
| `lineage_post_ipo_demand_drawdown_case`       |               2024~2025 | cold-chain scale-to-profitability 4C-watch |
| `heidelberg_materials_price_cost_case`        |              2025-11-06 | +74% YTD, aligned candidate                |
| `cemex_demand_slowdown_costcut_case`          | 2025-02-06 / 2025-07-24 | mixed: cost-cut but volume weakness        |
| `ukraine_reconstruction_event_watch_case`     |                     계약별 | actual contract before Green               |
| `neom_city_event_watch_case`                  |                     계약별 | actual contract before Green               |
| `sejong_policy_theme_case`                    |                  정책 발표일 | Event only until budget/contract           |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R10 Loop 2에서는 아래 필드를 채우게 해야 한다.

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
unsold_inventory_units
cash_conversion_cycle
construction_cost_ratio
gross_margin
op_margin_change

revenue_backlog
contract_value
contract_duration_months
contract_margin_signal
project_financing_secured_flag

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
credit_loss_reserve
non_accrual_asset_ratio

maintenance_capex
expansion_capex
affo_integrity_risk_flag
short_report_flag

data_center_asset_acquired_flag
hyperscale_tenant_flag
tenant_concentration
power_secured_flag
water_permitting_flag
cooling_secured_flag
capex_amount
asset_pipeline_value
ai_infra_theme_flag
no_revenue_flag
binding_lease_flag
non_binding_loi_flag
power_delivery_date
local_opposition_flag

cold_storage_warehouse_count
cold_storage_capacity
energy_cost_ratio
customer_count
net_loss_flag
cold_chain_occupancy_rate
post_ipo_drawdown_flag

building_material_volume
cement_price_change
steel_rebar_price_change
energy_cost_change
raw_material_cost_change
price_hike_flag
cost_saving_amount
ebitda_change
volume_decline_flag

policy_support_amount
government_support_flag
reconstruction_contract_flag
budget_allocated_flag
construction_started_flag
project_delay_flag
financing_failure_flag

score_price_alignment
price_validation_status
review_notes
```

---

# R10 Loop 2 결론

이번 2회차에서 R10은 더 명확해졌다.

```text
Green 가능:
데이터센터 REIT 중 실제 자산·tenant·NOI/AFFO·전력/수자원이 확인된 경우
콜드체인 REIT 중 occupancy·NOI/AFFO·배당 커버리지가 확인된 경우
건자재 중 가격전가·비용관리·출하량·OPM이 같이 확인된 경우

Watch-to-Green:
대형 건설사 중 PF 노출이 낮고 cash conversion이 개선되는 기업
리츠 중 occupancy·AFFO·배당 커버리지가 안정적인 기업
AI 데이터센터 real asset 중 binding lease와 power secured가 확인되는 기업
콜드체인·물류창고 중 에너지비와 debt를 통제하는 기업

Watch/Red:
중소형 건설사
개발신탁
오피스 노출 리츠
건자재 cycle
재건·네옴·세종시 정책 테마
무매출 AI data-center 개발사

Hard 4C:
PF 연체율 상승
브릿지론 rollover 실패
워크아웃
오피스 공실·대출부실·배당삭감
AFFO 착시·maintenance capex 논란
자산·tenant 없는 데이터센터 REIT
무매출 AI real asset 과열
콜드체인 순손실·post-IPO drawdown
건자재 출하량 둔화·EBITDA 감소
```

**R10 Loop 2 점수정규화의 핵심 문장:**

> 건설·부동산·건자재는 “수주잔고”, “배당률”, “AI 데이터센터”, “재건 테마”가 아니라 **PF 리스크, cash conversion, occupancy, NOI/AFFO, 배당 커버리지, funding cost, maintenance capex, tenant lease, power/water 확보, 출하량, 원가율**로 봐야 한다.
> 정부지원과 금리 기대는 Stage 1 relief이고, Stage 3-Green은 실제 credit recovery와 cash-flow recovery가 확인될 때만 가능하다.

다음 순서는 **R11 — 정책·지정학·재난·이벤트 Loop 2**다.

[1]: https://www.reuters.com/business/heidelberg-materials-posts-higher-than-expected-q3-profit-cost-price-management-2025-11-06/?utm_source=chatgpt.com "Heidelberg Materials posts higher than expected Q3 profit on cost, price management"
[2]: https://www.reuters.com/technology/blackstone-data-center-vehicle-opens-flat-new-york-debut-after-175-billion-ipo-2026-05-14/?utm_source=chatgpt.com "Blackstone data center vehicle makes muted debut after $1.75 billion IPO"
[3]: https://www.reuters.com/markets/deals/logistics-giant-lineage-raises-445-bln-biggest-ipo-2024-2024-07-24/?utm_source=chatgpt.com "Logistics giant Lineage raises $4.44 bln in biggest IPO of 2024"
[4]: https://www.reuters.com/business/mexican-cement-maker-cemex-ekes-out-profit-starts-350-million-savings-program-2025-02-06/?utm_source=chatgpt.com "Mexican cement maker Cemex ekes out profit, starts $350 million savings program"
[5]: https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/?utm_source=chatgpt.com "South Korea prepares financial support for small businesses, builders"
[6]: https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/?utm_source=chatgpt.com "South Korea tightens scrutiny to speed up real estate restructuring"
[7]: https://www.reuters.com/business/finance/blackstones-battered-mortgage-fund-slumps-empty-offices-intensify-pressure-2024-07-24/?utm_source=chatgpt.com "Blackstone's battered mortgage fund slumps as empty offices intensify pressure"
[8]: https://www.reuters.com/business/media-telecom/hindenburg-research-takes-short-position-data-center-operator-equinix-2024-03-20/?utm_source=chatgpt.com "Hindenburg shorts data center firm Equinix alleging inflated profit metric"
[9]: https://www.barrons.com/articles/equinix-stock-price-ai-capex-922e3582?utm_source=chatgpt.com "Equinix Wants More AI Data Centers-and Investors Are Punishing It"
[10]: https://www.reuters.com/business/rick-perrys-data-center-reit-raises-682-million-us-ipo-2025-09-30/?utm_source=chatgpt.com "Rick Perry-backed Fermi REIT raises $682 million in U.S. IPO amid AI data-center boom"
[11]: https://www.wsj.com/articles/cold-storage-operator-lineage-is-cutting-staff-f8a454bf?utm_source=chatgpt.com "Cold-Storage Operator Lineage Is Cutting Staff"
