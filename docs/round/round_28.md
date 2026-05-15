좋아. **Round 22: 얇은 archetype + 주요 archetype 점수비중 v1.3 보강**으로 계속 채울게.

이번 라운드는 특히 아직 얇았던 **원전/SMR, 전략금속, 데이터센터 REIT·부동산 인프라, 스마트그리드/AI 전력, 희귀 이벤트·정책 테마** 쪽을 더 파고든다.

기본 원칙은 그대로다.

> 테마명은 점수 근거가 아니다.
> 점수는 실제 공시·리포트·뉴스·재무·가격 evidence에서만 나온다.
> 서생원식 핵심은 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**이다.
> 계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 필드는 실제로 확인된 값만 써야 하고, 없는 숫자를 만들어 넣으면 안 된다.

---

# Round 22에서 더 파는 Archetype

```text
1. NUCLEAR_SMR_GRID_POLICY
2. RARE_METALS_STRATEGIC_MATERIALS
3. DATA_CENTER_REIT_INFRASTRUCTURE
4. UTILITIES_AI_POWER_PPA
5. SMART_GRID_FLEXIBLE_DATACENTER
6. NORTH_KOREA_POLICY_EVENT
7. METAVERSE_NFT_THEME
8. ADVANCED_MATERIAL_SPECULATIVE_THEME
9. VALUE_UP_SHAREHOLDER_RETURN
10. AI_DATA_CENTER_INFRASTRUCTURE 재보정
```

---

# 1. NUCLEAR_SMR_GRID_POLICY

## 원전 / SMR / AI 전력 / 원전 기자재

### 핵심 구조

```text
AI 데이터센터 전력수요
→ 장기 무탄소 전력 확보 필요
→ 원전 PPA / SMR / 기존 원전 재가동
→ 장기 전력계약·기자재 수주·정책 지원
→ 단, 비용·허가·소송·상용화 지연 리스크 큼
```

### 성공 후보

Meta가 Constellation의 Clinton 원전과 20년 전력계약을 맺은 사례는 원전 archetype에서 중요한 성공 후보야. 이 계약은 AI 데이터센터 전력 수요 때문에 Big Tech가 장기 무탄소 전력을 확보하려는 흐름을 보여주고, 2027년부터 기존 보조금 종료 이후 원전의 재허가·운영 안정성을 지원하는 구조다. ([Reuters][1])

Microsoft가 Three Mile Island Unit 1 재가동 전력구매 계약을 맺은 사례도 같은 축이야. 이건 신규 SMR보다 기존 원전 재가동이 먼저 AI 전력 수요에 연결될 수 있음을 보여준다. ([위키백과][2])

### 반례

NuScale-UAMPS Carbon Free Power Project 취소는 SMR 반례의 기준이다. 프로젝트는 비용 상승과 전력가격 부담 때문에 2023년 취소됐고, 초기 추정 대비 비용이 크게 올라가면서 첫 미국 SMR 상용화 프로젝트의 경제성이 의심받았다. ([위키백과][3])

즉 원전/SMR은 정책·AI 전력 narrative만으로 Green을 주면 위험하다.

### 점수비중 v1.3

```text
EPS/FCF: 18
Structural Visibility: 22
Bottleneck/Pricing: 10
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 2
Information Confidence: 5
Risk Penalty: licensing / cost_overrun / legal_delay / project_financing
```

### Green 조건

```text
Green 가능:
- 실제 PPA 또는 장기 전력계약
- 기존 원전 재가동 또는 확정된 프로젝트
- 기자재 매출화 경로
- 법적·허가 리스크 낮음
- FY2/FY3 매출·OP visibility

Green 금지:
- SMR 테마만 있음
- 우선협상/LOI만 있음
- 프로젝트 비용·전력단가 불확실
- 허가·소송·financing 미확정
```

### 정규화 교정

원전/SMR은 **Watch-to-Green**이다.
기존 원전 PPA는 Green에 가까울 수 있고, 신규 SMR은 비용·허가·상용화 리스크 때문에 더 보수적으로 봐야 한다.

---

# 2. RARE_METALS_STRATEGIC_MATERIALS

## 희토류 / 리튬 / 비철금속 / 구리 / 전략광물

### 핵심 구조

```text
지정학·공급망 리스크
→ 정부 지원·가격 floor·장기 offtake
→ 광산/제련/자석 생산 CAPEX
→ FCF 전환
```

### 성공 후보

MP Materials와 미국 국방부의 희토류 자석 공급망 계약은 이 archetype의 좋은 성공 후보야. 미국 국방부가 MP Materials에 4억 달러 우선주 투자를 하고 최대주주가 되었으며, NdPr에 10년 가격 floor와 10년 offtake 구조가 붙었다. 이건 단순 희토류 테마가 아니라 **정부 지원 + 가격 하방 + 장기 구매계약**이 결합된 구조적 visibility 사례다. ([Reuters][4])

### 반례

Korea Zinc는 전략금속·거버넌스·공개매수 이벤트가 섞인 케이스다. MBK와 Young Poong의 공개매수 발표 후 주가가 급등했지만, 이것은 구조적 FCF 리레이팅인지 이벤트 프리미엄인지 분리해야 한다. 공개매수·경영권 분쟁은 주가를 크게 움직일 수 있지만, EPS/FCF 체급 변화가 없으면 `event_premium`으로 분류해야 한다. ([Reuters][5])

### 점수비중 v1.3

```text
EPS/FCF: 18
Structural Visibility: 18
Bottleneck/Pricing: 18
Market Mispricing: 14
Valuation Rerating: 13
Capital Allocation: 5
Information Confidence: 5
Risk Penalty: commodity_price / geopolitical_policy / project_execution / governance_event
```

### Green 조건

```text
Green 가능:
- 정부 지원 또는 장기 offtake
- 가격 floor 또는 구매 보장
- 실제 생산능력 확장
- 고객사·국방·산업 수요 확인
- FCF 전환 경로

Green 금지:
- 희토류/리튬/구리 가격 뉴스만 있음
- 공개매수·경영권 분쟁만 있음
- 광산 개발 계획만 있고 생산·판매 없음
```

### 정규화 교정

전략금속은 commodity보다 visibility를 더 높게 줄 수 있지만, 반드시 **정부계약·offtake·생산능력·FCF**가 있어야 한다. 가격 상승만으로는 commodity cycle이다.

---

# 3. DATA_CENTER_REIT_INFRASTRUCTURE

## 데이터센터 REIT / IDC / AI 인프라 부동산

### 핵심 구조

```text
AI CAPEX
→ 데이터센터 임대수요
→ hyperscale tenant 장기 임대계약
→ 전력·냉각·토지 확보
→ REIT/infra FFO 성장
```

### 성공 후보

Blackstone Digital Infrastructure Trust는 AI 데이터센터 REIT archetype의 기준 케이스가 될 수 있다. 이 REIT는 17.5억 달러 IPO를 통해 hyperscale 고객용 신규 데이터센터 자산에 투자하려 하고, Blackstone은 이미 QTS·AirTrunk 같은 데이터센터 자산에서 큰 포트폴리오를 보유하고 있다. ([Reuters][6])

Equinix의 말레이시아 데이터센터 투자도 성공 후보야. Equinix는 Kuala Lumpur에 1.9억 달러 이상을 투자해 AI·고성능 컴퓨팅 수요를 지원하는 시설을 짓고, 액체냉각 기술도 포함한다고 밝혔다. 이건 데이터센터 REIT/infra가 AI 수요와 직접 연결되는 사례다. ([Reuters][7])

### 반례

그러나 데이터센터 인프라도 CAPEX 부담이 크다. Equinix가 AI 수요 대응을 위해 CAPEX를 크게 늘리겠다고 하자 투자자들이 단기 수익성 부담을 우려해 주가를 압박했다는 보도가 있다. 즉 AI 데이터센터 자산은 수요가 강해도 **CAPEX가 AFFO/FCF를 압박하면 4B 또는 4C 위험**이 된다. ([Barron's][8])

### 점수비중 v1.3

```text
EPS/FCF: 18
Structural Visibility: 23
Bottleneck/Pricing: 18
Market Mispricing: 13
Valuation Rerating: 13
Capital Allocation: 5
Information Confidence: 5
Risk Penalty: capex_burden / power_water_constraint / tenant_concentration / funding_cost
```

### Green 조건

```text
Green 가능:
- hyperscale tenant 장기계약
- 전력·냉각·토지 확보
- FFO/AFFO 성장
- 높은 occupancy
- funding cost 통제

Green 금지:
- AI 데이터센터 테마만 있음
- 아직 자산 없음
- CAPEX만 증가하고 FFO 개선 없음
- 전력·수자원·인허가 병목
```

### 정규화 교정

데이터센터 REIT는 Green 가능성이 있지만, **부동산/REIT라서 FFO, occupancy, tenant quality, funding cost**를 봐야 한다. 일반 AI 인프라 점수와 다르게 `capital_allocation`과 `funding_cost risk`를 더 반영한다.

---

# 4. UTILITIES_AI_POWER_PPA

## 전력 PPA / 유틸리티 / 원전·전력회사 / AI 데이터센터 전력

### 핵심 구조

```text
AI 전력수요
→ 장기 PPA
→ 발전소 수명연장·재가동·CAPEX
→ 안정적 cash flow
→ 단, 규제·요금·전력망 리스크
```

### 성공 후보

Meta-Constellation 20년 원전 PPA는 이 archetype의 대표 사례다. 기존 원전의 경제성을 AI 데이터센터 전력수요가 보강하면서 발전소 재허가와 운영 안정성을 지원하는 구조다. ([Reuters][1])

### 반례

PPA가 없고 단순히 “전력수요 증가 수혜”만 있는 유틸리티는 Green을 주면 안 된다. 유틸리티는 규제요금, 부채, CAPEX, 정치 리스크가 강하다. 전력수요가 늘어도 요금 전가가 안 되면 EPS/FCF가 안 따라올 수 있다.

### 점수비중 v1.3

```text
EPS/FCF: 17
Structural Visibility: 22
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 5
Information Confidence: 5
Risk Penalty: regulation / tariff / debt / grid_connection / capex
```

### Green 조건

```text
Green 가능:
- 장기 PPA
- 전력 판매 가격/수익성 확인
- 발전소 수명연장 또는 capacity 확보
- 규제 리스크 낮음
- FCF·배당 안정

Green 금지:
- AI 전력수요 테마만 있음
- 요금전가 불확실
- 부채·CAPEX 부담 큼
- 정책 리스크 큼
```

---

# 5. SMART_GRID_FLEXIBLE_DATACENTER

## 스마트그리드 / AI 데이터센터 전력 유연화 / ESS / 전력망 소프트웨어

### 핵심 구조

```text
AI 데이터센터 전력수요 급증
→ 전력망 병목
→ 데이터센터 부하 유연화·ESS·스마트그리드
→ 기존 전력망 효율 개선
→ 소프트웨어/장비/서비스 매출
```

### 성공 후보

AI 데이터센터를 전력망 유연자원으로 전환하는 field demonstration 연구는 이 archetype의 방향을 보여준다. Phoenix의 상용 hyperscale 데이터센터에서 AI workload를 조절해 피크 전력 사용을 3시간 동안 25% 줄이면서 AI 품질을 유지한 결과가 보고됐다. 이건 스마트그리드·데이터센터 전력 소프트웨어가 단순 전력설비가 아니라 새로운 병목 해결 솔루션이 될 수 있음을 보여준다. ([arXiv][9])

### 반례

```text
- 스마트그리드 정책만 있음
- ESS 설치 뉴스만 있고 수익모델 없음
- 데이터센터와 직접 연결 없음
- 전력망 소프트웨어가 PoC 단계에 머묾
- 실제 고객/반복 매출 없음
```

### 점수비중 v1.3

```text
EPS/FCF: 18
Structural Visibility: 18
Bottleneck/Pricing: 16
Market Mispricing: 13
Valuation Rerating: 11
Capital Allocation: 2
Information Confidence: 6
Risk Penalty: commercialization / utility_adoption / regulation / project_delay
```

### Green 조건

```text
Green 가능:
- 실제 데이터센터/유틸리티 고객
- 반복 소프트웨어 또는 서비스 매출
- 전력 절감·피크관리 성과
- 규제·인센티브 구조

Green 금지:
- 스마트그리드 테마만 있음
- 연구/PoC만 있음
- 매출화 경로 없음
```

### 정규화 교정

스마트그리드/전력 유연화는 아직 **Watch-to-Green**이다. 기술적 가치는 크지만, 실제 고객과 수익모델이 확인되어야 한다.

---

# 6. NORTH_KOREA_POLICY_EVENT

## 남북경협 / DMZ / 개성공단 / 금강산 / 광물자원개발

### 핵심 구조

```text
정책·외교 이벤트
→ 관련주 급등
→ 실제 계약·사업권·현금흐름 없는 경우 대부분 이벤트 프리미엄
```

### 반례 중심

이 archetype은 거의 `event_only`로 봐야 한다. 남북경협·DMZ·개성공단·금강산 관광·북한 광물자원개발은 주가를 급등시킬 수 있지만, 실제 사업 재개·계약·현금흐름이 없으면 정통 E2R이 아니다.

북한의 핵·군사 리스크는 이 테마의 구조적 red flag다. 북한의 실험용 경수로가 트리튬·플루토늄 생산 가능성과 연결될 수 있다는 연구는, 남북경협이 단순 정책 기대가 아니라 안보 리스크에 강하게 묶여 있음을 보여준다. ([arXiv][10])

### 점수비중 v1.3

```text
EPS/FCF: 5
Structural Visibility: 5
Bottleneck/Pricing: 5
Market Mispricing: 8
Valuation Rerating: 5
Capital Allocation: 0
Information Confidence: 3
Risk Penalty: extreme_policy_security
```

### Green 조건

사실상 Green 금지에 가깝다.

```text
Stage 1:
정책 뉴스, 회담, 제재 완화 기대

Stage 2:
실제 사업 재개 계약이 있을 때만

Stage 3:
극히 제한적. 다년 계약·매출·현금흐름 확인 필요

4C:
외교 악화, 군사 도발, 제재 강화, 사업 중단
```

### 정규화 교정

남북경협은 **event trade**로 분류한다.
E2R 성공사례로 쓰면 점수체계가 망가진다.

---

# 7. METAVERSE_NFT_THEME

## NFT / 메타버스 / 디지털자산 테마

### 핵심 구조

```text
신기술 narrative
→ 가격·거래량 급등
→ 반복매출·FCF 없으면 붕괴
```

### 반례 중심

NFT와 메타버스는 대부분 `theme_overheat`로 둬야 한다. NFT·메타버스는 한때 강한 narrative를 만들었지만, 실제 반복매출·FCF·고객 lock-in이 없으면 리레이팅이 아니라 price-only rally가 된다.

스테이블코인·토큰화 금융과 NFT는 분리해야 한다. 스테이블코인은 규제·준비금·결제망·거래량이 붙으면 금융 인프라가 될 수 있지만, NFT는 상당수가 수익모델이 약한 투기성 테마에 머물렀다.

### 점수비중 v1.3

```text
EPS/FCF: 5
Structural Visibility: 5
Bottleneck/Pricing: 5
Market Mispricing: 6
Valuation Rerating: 5
Capital Allocation: 0
Information Confidence: 3
Risk Penalty: extreme_theme / no_revenue / liquidity_collapse
```

### Green 조건

거의 없다.

```text
Green 가능하려면:
- 실제 반복 플랫폼 매출
- 거래수수료 안정
- 규제 리스크 낮음
- EPS/FCF 전환

대부분:
Stage 1 / Red / 4B-watch
```

---

# 8. ADVANCED_MATERIAL_SPECULATIVE_THEME

## 초전도체 / 맥신 / 그래핀 / 양자 / 페라이트

### 핵심 구조

```text
논문·기술 narrative
→ 주가 급등
→ 상용화·매출·계약 확인 전까지 EPS/FCF 없음
```

### 반례 중심

이 archetype은 Green을 거의 막는 필터야. 초전도체, 맥신, 그래핀, 양자 기술은 기술적으로 중요할 수 있지만, 종목 점수로 들어가려면 **제품, 고객, 계약, 매출, OP/FCF**가 있어야 한다.

### 점수비중 v1.3

```text
EPS/FCF: 5
Structural Visibility: 5
Bottleneck/Pricing: 5
Market Mispricing: 5
Valuation Rerating: 5
Capital Allocation: 0
Information Confidence: 3
Risk Penalty: extreme_speculative / no_commercialization
```

### Green 조건

```text
Green 금지:
- 논문
- 샘플
- 관련주 편입
- 특허/뉴스만 있음

Stage 2 가능:
- 실제 제품 공급계약
- 상용 고객
- 매출 인식

Stage 3 가능:
- 반복 매출 + EPS/FCF 전환
```

---

# 9. VALUE_UP_SHAREHOLDER_RETURN

## 밸류업 / 저PBR / 자사주 / 배당 / 지주

### 핵심 구조

```text
저PBR·NAV discount
→ 자사주·소각·배당
→ ROE 개선
→ 시장 프레임 변화
```

### 성공 후보

금융지주·보험·일부 지주사는 실제 ROE, 배당, 자사주 소각이 붙으면 Green 가능성이 있다. 다만 “밸류업 지수 편입” 자체는 점수가 아니다.

### 반례

```text
- 자사주 매입 후 미소각
- ROE 낮은 저PBR주
- 배당만 높고 FCF 약함
- 지배주주 리스크
- 이벤트성 주주환원 공시
```

### 점수비중 v1.3

```text
EPS/FCF: 12
Structural Visibility: 18
Bottleneck/Pricing: 4
Market Mispricing: 20
Valuation Rerating: 25
Capital Allocation: 10
Information Confidence: 5
Risk Penalty: governance / execution / low_ROE / no_cancellation
```

### Green 조건

```text
Green 가능:
- ROE 유지/개선
- 반복 환원정책
- 실제 소각
- 배당 지속성
- NAV/PBR discount 해소 근거

Green 금지:
- 밸류업 지수 편입만 있음
- 저PBR만 있음
- 자사주 매입 후 소각 없음
```

---

# 10. AI_DATA_CENTER_INFRASTRUCTURE 재보정

### 핵심 구조

```text
AI CAPEX
→ 전력·냉각·서버·네트워크·PCB·메모리 병목
→ 다년 CAPEX visibility
→ 수주·납품·OP/EPS 상향
```

### 성공 후보

Blackstone의 데이터센터 REIT, Equinix의 AI 대응 데이터센터 투자, Ecolab/CoolIT의 액체냉각, Meta·Microsoft의 원전 PPA는 모두 AI 데이터센터 인프라가 단순 GPU를 넘어 **전력·냉각·부동산·전력계약·네트워크**로 확장되고 있음을 보여준다. ([Reuters][6])

### 점수비중 v1.3

```text
EPS/FCF: 22
Structural Visibility: 23
Bottleneck/Pricing: 20
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 2
Information Confidence: 5
Risk Penalty: AI_capex_cut / project_delay / grid_constraint / overbuild
```

### 정규화 교정

AI 인프라는 Green 가능성이 높지만, 테마가 너무 넓어서 각 하위축을 따로 봐야 한다.

```text
Green 가능:
- 전력설비/변압기/전선
- 데이터센터 냉각
- AI 서버 PCB
- 장기 전력 PPA
- 데이터센터 REIT with hyperscale lease

Watch:
- 스마트그리드 PoC
- 수소/원전 기대
- 일반 HVAC
- AI 관련주로 묶인 종목

Red:
- AI CAPEX 테마만 있음
- 매출 exposure 불명확
- project delay
- overbuild
```

---

# Round 22 점수비중 요약표

| Archetype                | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | 핵심 리스크                   |
| ------------------------ | ------: | ---------: | ---------: | ---------: | --------: | ------: | ------------------------ |
| NUCLEAR_SMR_GRID_POLICY  |      18 |         22 |         10 |         14 |        12 |       2 | 허가, 비용, financing        |
| RARE_METALS_STRATEGIC    |      18 |         18 |         18 |         14 |        13 |       5 | commodity, 정책, execution |
| DATA_CENTER_REIT_INFRA   |      18 |         23 |         18 |         13 |        13 |       5 | CAPEX, 전력·수자원, funding   |
| UTILITIES_AI_POWER_PPA   |      17 |         22 |         12 |         12 |        10 |       5 | 규제, 부채, 요금               |
| SMART_GRID_FLEX_DC       |      18 |         18 |         16 |         13 |        11 |       2 | 상용화, 유틸리티 채택             |
| NORTH_KOREA_POLICY_EVENT |       5 |          5 |          5 |          8 |         5 |       0 | 안보·정책 극단 리스크             |
| METAVERSE_NFT_THEME      |       5 |          5 |          5 |          6 |         5 |       0 | 수익모델 부재                  |
| ADVANCED_MATERIAL_SPEC   |       5 |          5 |          5 |          5 |         5 |       0 | 상용화 부재                   |
| VALUE_UP_SHAREHOLDER     |      12 |         18 |          4 |         20 |        25 |      10 | 실행·거버넌스                  |
| AI_DATA_CENTER_INFRA     |      22 |         23 |         20 |         14 |        12 |       2 | CAPEX cut, overbuild     |

---

# cases_v10 추가 후보

```text
NUCLEAR_SMR_GRID_POLICY:
- meta_constellation_20y_nuclear_ppa_success_candidate
- microsoft_tmi_reopen_ppa_candidate
- nuscale_uamps_cost_cancel_4c
- smr_policy_no_financing_counterexample

RARE_METALS_STRATEGIC_MATERIALS:
- mp_materials_dod_price_floor_offtake_success_candidate
- korea_zinc_tender_event_premium
- pure_rare_earth_price_theme_counterexample
- mining_project_no_production_counterexample

DATA_CENTER_REIT_INFRASTRUCTURE:
- blackstone_digital_infra_reit_candidate
- equinix_malaysia_ai_liquid_cooling_candidate
- data_center_reit_capex_burden_4c
- hyperscale_tenant_concentration_counterexample

UTILITIES_AI_POWER_PPA:
- meta_constellation_power_ppa_candidate
- nuclear_no_ppa_utility_theme_counterexample
- tariff_no_pass_through_4c
- utility_debt_capex_burden_counterexample

SMART_GRID_FLEXIBLE_DATACENTER:
- ai_datacenter_grid_interactive_demo_candidate
- smart_grid_policy_no_revenue_counterexample
- ess_no_revenue_model_counterexample
- utility_adoption_delay_4c

NORTH_KOREA_POLICY_EVENT:
- north_korea_policy_rally_event_only
- kaesong_reopen_expectation_counterexample
- kumgang_tourism_policy_event_only
- military_security_risk_4c

METAVERSE_NFT_THEME:
- nft_price_rally_no_revenue_counterexample
- metaverse_platform_no_fcf_counterexample
- digital_asset_infra_vs_nft_split_case
- nft_liquidity_collapse_4c

ADVANCED_MATERIAL_SPECULATIVE_THEME:
- superconductor_theme_counterexample
- graphene_mxene_no_commercialization_counterexample
- quantum_policy_no_revenue_watch
- material_sample_no_contract_counterexample

VALUE_UP_SHAREHOLDER_RETURN:
- financial_valueup_roe_pbr_success_candidate
- buyback_cancellation_success_candidate
- buyback_no_cancel_counterexample
- low_roe_low_pbr_value_trap_counterexample

AI_DATA_CENTER_INFRASTRUCTURE:
- ai_power_cooling_reit_integrated_success_candidate
- ai_capex_overbuild_4c
- grid_interconnection_delay_4c
- ai_theme_no_revenue_counterexample
```

---

# 이번 라운드 핵심 교정

```text
1. 원전/SMR은 AI 전력 수요로 강한 Stage 1~2가 가능하지만, 비용·허가·PPA가 없으면 Green 금지.
2. 희토류/전략금속은 정부 지원·가격 floor·offtake가 있으면 Green 가능성이 생김.
3. 데이터센터 REIT는 AI 인프라 수혜지만 FFO/AFFO, tenant, funding cost를 봐야 함.
4. 유틸리티는 장기 PPA가 있으면 점수 상승. 단순 전력수요 테마는 부족.
5. 스마트그리드는 기술적으로 매력적이나, 실제 고객·수익모델 없으면 Watch.
6. 남북경협은 거의 event_only. E2R 성공사례로 쓰면 안 됨.
7. NFT/메타버스/초전도체/그래핀은 Green 거의 금지.
8. 밸류업은 지수 편입이 아니라 실제 ROE·소각·배당·NAV discount 해소가 핵심.
9. AI 데이터센터 인프라는 전력·냉각·REIT·PPA·PCB를 통합하되, 각 하위축별 evidence가 필요.
```

---

# 현재 판단

이제 테마 흡수 구조와 점수비중 가설은 꽤 넓어졌다.
하지만 여전히 마지막 검증은 남아 있다.

```text
1. cases_v10 반영
2. 각 case stage date 후보 설정
3. price path backfill
4. MFE/MAE/drawdown 계산
5. score-price alignment 확인
6. shadow scoring
7. 틀린 archetype 재교정
```

지금 우리가 하는 건 **점수비중의 지도**를 만드는 작업이고, 다음 단계는 그 지도가 실제 시장 주가 경로와 맞는지 확인하는 작업이다.

[1]: https://www.reuters.com/sustainability/climate-energy/meta-signs-power-agreement-with-constellation-nuclear-plant-2025-06-03/?utm_source=chatgpt.com "Meta signs power agreement with Constellation nuclear plant"
[2]: https://en.wikipedia.org/wiki/Three_Mile_Island_Nuclear_Generating_Station?utm_source=chatgpt.com "Three Mile Island Nuclear Generating Station"
[3]: https://en.wikipedia.org/wiki/NuScale_Power?utm_source=chatgpt.com "NuScale Power"
[4]: https://www.reuters.com/business/mp-materials-partners-with-department-defense-boost-us-rare-earth-magnet-supply-2025-07-10/?utm_source=chatgpt.com "MP Materials shares surge on mega deal with defense department to boost US magnet supply"
[5]: https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/?utm_source=chatgpt.com "Private equity MBK, Young Poong launch $1.5 bln tender offer for Korea Zinc shares"
[6]: https://www.reuters.com/technology/blackstone-data-center-vehicle-opens-flat-new-york-debut-after-175-billion-ipo-2026-05-14/?utm_source=chatgpt.com "Blackstone data center vehicle makes muted debut after $1.75 billion IPO"
[7]: https://www.reuters.com/world/asia-pacific/equinix-create-new-malaysia-data-centre-with-over-190-million-investment-2026-05-12/?utm_source=chatgpt.com "Equinix to create new Malaysia data centre with over $190 million investment"
[8]: https://www.barrons.com/articles/equinix-stock-price-ai-capex-922e3582?utm_source=chatgpt.com "Equinix Wants More AI Data Centers-and Investors Are Punishing It"
[9]: https://arxiv.org/abs/2507.00909?utm_source=chatgpt.com "Turning AI Data Centers into Grid-Interactive Assets: Results from a Field Demonstration in Phoenix, Arizona"
[10]: https://arxiv.org/abs/2412.11993?utm_source=chatgpt.com "Estimating Potential Tritium and Plutonium Production in North Korea's Experimental Light Water Reactor"
