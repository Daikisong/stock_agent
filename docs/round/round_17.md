응. **구조적으로는 이제 거의 다 흡수 가능해졌다고 봐도 된다.**
다만 “점수까지 완성됐다”는 뜻은 아니야.

정확히 나누면 이렇다.

```text
1. 테마 흡수 구조
→ 거의 됨.
→ 네가 보낸 세부 테마 대부분은 12개 대섹터 + 70개 안팎 archetype/sub-archetype으로 품을 수 있음.

2. 점수정규화 구조
→ 방향은 잡힘.
→ 성공/반례 기반으로 EPS/FCF, visibility, bottleneck, mispricing, valuation, risk 비중을 다르게 주는 틀은 생김.

3. 실제 검증
→ 아직 해야 함.
→ 각 archetype별 성공 2개 + 반례 2개 + price path validation이 차야 진짜 적용 가능.
```

핵심은 여전히 이거야.

> 테마명은 점수 근거가 아니다.
> 테마명은 검색·분류·쿼리 생성용 tag다.
> 점수는 실제 evidence에서 나온다.

서생원식 원칙도 단순히 “테마가 좋다”가 아니라, **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅** 순서야.
그리고 후보를 점수화할 때도 장기계약, 수주잔고, 선수금, RPO, CAPA, 가격 결정력 같은 실제 증거를 봐야 하지, missing field를 추정해서 채우면 안 된다. OpenDART detail fetch 쪽에서도 계약금액, 계약기간, 매출대비 계약금액 같은 실제 필드만 추출하고 없는 값은 만들지 않는 원칙이 잡혀 있었어.

---

# 1. “테마 다 흡수됐냐?”에 대한 정확한 답

## 구조적 흡수 기준으로는 거의 Yes

네가 준 테마들은 대략 아래 구조로 거의 다 들어간다.

```text
12개 대섹터
→ 70개 안팎 archetype / sub-archetype
→ 200개+ raw theme tag
```

즉, 아래 같은 테마들도 따로 if문을 만들 필요 없이 흡수 가능해.

```text
편의점
손해보험
스테이블코인
HBM
초전도체
마켓컬리·오아시스
화장품 OEM/ODM
전고체 배터리
원전
CRO
STO
엠폭스
전선·케이블
AI 데이터센터 냉각
남북경협
우크라 재건
치아 임플란트
양돈주
피지컬AI
```

## 다만 검증 기준으로는 아직 No

왜냐하면 “테마가 어떤 archetype에 들어간다”와 “그 archetype의 점수비중이 맞다”는 다른 문제야.

예를 들어:

```text
네이버 → PLATFORM_SOFTWARE_INTERNET
```

으로 흡수는 가능해.
하지만 네이버를 Stage 3 성공사례로 넣으려면 실제로:

```text
ARPU 상승
OPM 개선
AI 비용 통제
FCF 개선
주가 리레이팅
```

이 같이 확인되어야 해.

그게 없으면 그냥 “좋은 플랫폼 회사”일 수는 있어도, 서생원식 E2R 성공사례는 아니야.

---

# 2. 최종 구조: 12개 대섹터

이제 대섹터는 이렇게 두면 거의 모든 테마를 품을 수 있어.

|  # | 대섹터           | 역할                                      |
| -: | ------------- | --------------------------------------- |
|  1 | 산업재·수주·인프라    | 전력설비, 전선, 조선, 방산, 원전, 철도, 건설기계          |
|  2 | AI·반도체·전자부품   | HBM, CXL, 시스템반도체, PCB, OLED, MLCC, 유리기판 |
|  3 | 2차전지·전기차·친환경  | 2차전지, 폐배터리, 전고체, 수소, 태양광, 풍력            |
|  4 | 소재·스프레드·전략자원  | 화학, 정유, 철강, 비철, 리튬, 희토류, 금은, 그래핀        |
|  5 | 소비재·유통·브랜드    | 편의점, 라면, K푸드, 화장품, 의류, 홈쇼핑, 건기식         |
|  6 | 금융·자본배분·디지털금융 | 은행, 보험, 증권, 밸류업, 고배당, 결제, STO, 스테이블코인   |
|  7 | 바이오·헬스케어·의료기기 | CMO, CRO, 바이오시밀러, 진단, 의료AI, 미용기기, 보톡스   |
|  8 | 플랫폼·콘텐츠·SW·보안 | 게임, 엔터, 클라우드, AI SW, 보안, 딥페이크, 메타버스     |
|  9 | 모빌리티·운송·레저    | 항공, 해운, 렌터카, 여행, 카지노, 면세, 자율주행          |
| 10 | 건설·부동산·건자재    | 대형/중소형 건설, 리츠, 시멘트, 철근, 가구, 개발신탁        |
| 11 | 정책·지정학·재난·이벤트 | 남북경협, 우크라 재건, 세종시, 지진, 폭염, 전염병, 황사      |
| 12 | 농업·생활서비스·기타   | 교육, 취업, 키즈, 스마트팜, 양돈, 육계, 사료, 참치        |

이 12개는 “큰 서랍”이고, 실제 점수는 그 안의 archetype이 한다.

---

# 3. Archetype 확장 v0.5

기존 32개에서 이제는 아래 정도로 확장해야 테마 커버리지가 거의 닫힌다.

## 산업재·수주·인프라

```text
CONTRACT_BACKLOG_INDUSTRIAL
DEFENSE_GOVERNMENT_BACKLOG
SHIPBUILDING_OFFSHORE_BACKLOG
AI_DATA_CENTER_INFRASTRUCTURE
NUCLEAR_SMR_GRID_POLICY
RAIL_INFRASTRUCTURE
GEOPOLITICAL_RECONSTRUCTION
SMART_FACTORY_AUTOMATION
```

## AI·반도체·전자부품

```text
MEMORY_HBM_CAPACITY
SEMI_EQUIPMENT_CAPEX
SEMI_MATERIALS_PROCESS
ADVANCED_PACKAGING_PCB
DISPLAY_OLED_EQUIPMENT
ELECTRONIC_COMPONENTS
AI_CHIP_FABRIC_INFRA
CYBER_AI_SECURITY
```

## 2차전지·전기차·친환경

```text
BATTERY_MATERIALS_CAPEX_OVERHEAT
BATTERY_EQUIPMENT_PARTS
BATTERY_RECYCLING_ESS_SHIFT
EV_INFRASTRUCTURE
HYDROGEN_FUEL_CELL_INFRA
RENEWABLE_ENERGY_POLICY
SOLAR_TARIFF_SUPPLYCHAIN
ENERGY_DISTRIBUTION_FUEL
```

## 소재·스프레드·전략자원

```text
REFINING_OIL_SPREAD
CHEMICAL_SPREAD
STEEL_METAL_SPREAD
NONFERROUS_STRATEGIC_METALS
RARE_METALS_STRATEGIC_MATERIALS
ADVANCED_MATERIAL_THEMES
PAPER_PACKAGING
AGRI_COMMODITY_INPUTS
```

## 소비재·유통·브랜드

```text
EXPORT_RECURRING_CONSUMER
FOOD_AGRI_LIVESTOCK_CYCLE
RETAIL_CONVENIENCE_OFFLINE
ECOMMERCE_FRESH_LOGISTICS
K_BEAUTY_EXPORT_DISTRIBUTION
BEAUTY_OEM_ODM_SUPPLYCHAIN
APPAREL_BRAND_OEM
HOME_LIVING_APPLIANCE
```

## 금융·자본배분·디지털금융

```text
FINANCIAL_SPREAD_BALANCE_SHEET
INSURANCE_UNDERWRITING_CYCLE
SECURITIES_BROKERAGE_CYCLE
VALUE_UP_SHAREHOLDER_RETURN
HOLDING_RESTRUCTURING_GOVERNANCE
PAYMENT_FINTECH_INFRA
DIGITAL_ASSET_TOKENIZATION
```

## 바이오·헬스케어·의료기기

```text
BIOTECH_PRE_REVENUE_REGULATORY
BIOTECH_ROYALTY_COMMERCIALIZATION
CDMO_HEALTHCARE_CONTRACT
DIAGNOSTICS_INFECTIOUS_DISEASE
MEDICAL_DEVICE_HEALTHCARE_EXPORT
DIGITAL_HEALTHCARE_AI
CRO_CLINICAL_SERVICE
CANNABIS_REGULATED_HEALTH
```

## 플랫폼·콘텐츠·SW·보안

```text
PLATFORM_SOFTWARE_INTERNET
GAME_CONTENT_IP
MEDIA_AD_CONTENT_CYCLE
METAVERSE_NFT_THEME
AI_SOFTWARE_APPLICATION
CLOUD_AI_SOFTWARE_INFRA
SECURITY_IDENTITY_DEEPFAKE
EDUCATION_SPECIALTY_SERVICES
```

## 모빌리티·운송·레저

```text
AIRLINE_TRAVEL_CYCLE
TRAVEL_LEISURE_REOPENING
CASINO_DUTYFREE_TOURISM
SHIPPING_FREIGHT_CYCLE
AUTO_MOBILITY_COMPLETED_VEHICLE
AUTO_MOBILITY_COMPONENTS
TIRE_AUTO_COMPONENT_SPREAD
RENTAL_USED_CAR_MOBILITY
URBAN_AIR_DRONE
```

## 건설·부동산·건자재

```text
CONSTRUCTION_REAL_ESTATE_CREDIT
REIT_DEVELOPMENT_TRUST
BUILDING_MATERIALS_CYCLE
INFRA_RECONSTRUCTION_POLICY
DISASTER_REBUILD_EVENT
```

## 정책·지정학·재난·이벤트

```text
NORTH_KOREA_POLICY_EVENT
GEOPOLITICAL_RECONSTRUCTION
CLIMATE_DISASTER_EVENT
EVENT_DISEASE_PEST_DEMAND
SPECULATIVE_SCIENCE_THEME
POLICY_LOCAL_THEME
```

## 농업·생활서비스·기타

```text
SMART_FARM_AGRI_TECH
AGRI_LIVESTOCK_FOOD_COMMODITY
HOME_CHILD_EDUCATION
WASTE_RECYCLING_ENVIRONMENT
SERVICE_KIOSK_AUTOMATION
CONSUMER_REGULATED_PRODUCT
```

이 정도면 네가 준 테마의 대부분은 흡수된다.

---

# 4. Theme Tag Map v0.5 초안

아래는 실제 `theme_tag_map.csv`로 넣을 수 있는 형태의 축약본이야.

| theme_tag    | large_sector  | primary_archetype                 | green_policy   |
| ------------ | ------------- | --------------------------------- | -------------- |
| 편의점          | 소비재·유통·브랜드    | RETAIL_CONVENIENCE_OFFLINE        | watch_to_green |
| 홈쇼핑          | 소비재·유통·브랜드    | RETAIL_CONVENIENCE_OFFLINE        | watch_only     |
| 음식료          | 소비재·유통·브랜드    | EXPORT_RECURRING_CONSUMER         | watch_to_green |
| 라면           | 소비재·유통·브랜드    | EXPORT_RECURRING_CONSUMER         | green_allowed  |
| K-푸드         | 소비재·유통·브랜드    | EXPORT_RECURRING_CONSUMER         | green_allowed  |
| 건강기능식품       | 소비재·유통·브랜드    | EXPORT_RECURRING_CONSUMER         | watch_to_green |
| 마켓컬리·오아시스    | 소비재·유통·브랜드    | ECOMMERCE_FRESH_LOGISTICS         | event_watch    |
| 콜드체인         | 소비재·유통·브랜드    | ECOMMERCE_FRESH_LOGISTICS         | watch_to_green |
| 화장품 브랜드      | 소비재·유통·브랜드    | K_BEAUTY_EXPORT_DISTRIBUTION      | green_allowed  |
| 화장품 OEM·ODM  | 소비재·유통·브랜드    | BEAUTY_OEM_ODM_SUPPLYCHAIN        | green_allowed  |
| 화장품 원재료·부자재  | 소비재·유통·브랜드    | BEAUTY_OEM_ODM_SUPPLYCHAIN        | watch_to_green |
| 의류 브랜드       | 소비재·유통·브랜드    | APPAREL_BRAND_OEM                 | watch_only     |
| 의류 OEM·ODM   | 소비재·유통·브랜드    | APPAREL_BRAND_OEM                 | watch_only     |
| 손해보험         | 금융·자본배분·디지털금융 | INSURANCE_UNDERWRITING_CYCLE      | green_allowed  |
| 생명보험         | 금융·자본배분·디지털금융 | INSURANCE_UNDERWRITING_CYCLE      | watch_to_green |
| 은행           | 금융·자본배분·디지털금융 | FINANCIAL_SPREAD_BALANCE_SHEET    | green_allowed  |
| 금융지주회사       | 금융·자본배분·디지털금융 | FINANCIAL_SPREAD_BALANCE_SHEET    | green_allowed  |
| 증권사          | 금융·자본배분·디지털금융 | SECURITIES_BROKERAGE_CYCLE        | watch_only     |
| 벤처캐피탈        | 금융·자본배분·디지털금융 | SECURITIES_BROKERAGE_CYCLE        | watch_only     |
| 고배당주         | 금융·자본배분·디지털금융 | VALUE_UP_SHAREHOLDER_RETURN       | watch_to_green |
| 밸류업 지수 편입    | 금융·자본배분·디지털금융 | VALUE_UP_SHAREHOLDER_RETURN       | watch_only     |
| 결제서비스        | 금융·자본배분·디지털금융 | PAYMENT_FINTECH_INFRA             | watch_to_green |
| 토스 관련주       | 금융·자본배분·디지털금융 | PAYMENT_FINTECH_INFRA             | event_watch    |
| STO          | 금융·자본배분·디지털금융 | DIGITAL_ASSET_TOKENIZATION        | watch_only     |
| 스테이블코인       | 금융·자본배분·디지털금융 | DIGITAL_ASSET_TOKENIZATION        | watch_only     |
| NFT          | 플랫폼·콘텐츠·SW·보안 | METAVERSE_NFT_THEME               | red_flag       |
| 디지털자산·블록체인   | 금융·자본배분·디지털금융 | DIGITAL_ASSET_TOKENIZATION        | watch_only     |
| 전력설비         | 산업재·수주·인프라    | CONTRACT_BACKLOG_INDUSTRIAL       | green_allowed  |
| 전선·케이블       | 산업재·수주·인프라    | CONTRACT_BACKLOG_INDUSTRIAL       | green_allowed  |
| 피팅밸브         | 산업재·수주·인프라    | SHIPBUILDING_OFFSHORE_BACKLOG     | watch_to_green |
| 방위산업         | 산업재·수주·인프라    | DEFENSE_GOVERNMENT_BACKLOG        | green_allowed  |
| 항공우주         | 산업재·수주·인프라    | DEFENSE_GOVERNMENT_BACKLOG        | watch_to_green |
| 조선           | 산업재·수주·인프라    | SHIPBUILDING_OFFSHORE_BACKLOG     | green_allowed  |
| 조선 기자재       | 산업재·수주·인프라    | SHIPBUILDING_OFFSHORE_BACKLOG     | watch_to_green |
| LNG선 기자재     | 산업재·수주·인프라    | SHIPBUILDING_OFFSHORE_BACKLOG     | watch_to_green |
| 원자력·원전       | 산업재·수주·인프라    | NUCLEAR_SMR_GRID_POLICY           | watch_to_green |
| 철도           | 산업재·수주·인프라    | RAIL_INFRASTRUCTURE               | watch_only     |
| 건설기계         | 산업재·수주·인프라    | CONTRACT_BACKLOG_INDUSTRIAL       | watch_to_green |
| 우크라 재건       | 정책·지정학·재난·이벤트 | GEOPOLITICAL_RECONSTRUCTION       | event_watch    |
| 네옴시티         | 정책·지정학·재난·이벤트 | GEOPOLITICAL_RECONSTRUCTION       | event_watch    |
| 세종시          | 정책·지정학·재난·이벤트 | POLICY_LOCAL_THEME                | event_only     |
| 남북경협         | 정책·지정학·재난·이벤트 | NORTH_KOREA_POLICY_EVENT          | event_only     |
| 금강산 관광       | 정책·지정학·재난·이벤트 | NORTH_KOREA_POLICY_EVENT          | event_only     |
| 개성공단         | 정책·지정학·재난·이벤트 | NORTH_KOREA_POLICY_EVENT          | event_only     |
| 반도체-HBM      | AI·반도체·전자부품   | MEMORY_HBM_CAPACITY               | green_allowed  |
| 반도체-CXL      | AI·반도체·전자부품   | MEMORY_HBM_CAPACITY               | watch_only     |
| 시스템반도체       | AI·반도체·전자부품   | AI_CHIP_FABRIC_INFRA              | watch_to_green |
| 뉴로모픽 반도체     | AI·반도체·전자부품   | AI_CHIP_FABRIC_INFRA              | watch_only     |
| 퓨리오사AI 관련주   | AI·반도체·전자부품   | AI_CHIP_FABRIC_INFRA              | event_watch    |
| 반도체 전공정 장비   | AI·반도체·전자부품   | SEMI_EQUIPMENT_CAPEX              | watch_to_green |
| 반도체 후공정 장비   | AI·반도체·전자부품   | SEMI_EQUIPMENT_CAPEX              | watch_to_green |
| 반도체 전공정 소재   | AI·반도체·전자부품   | SEMI_MATERIALS_PROCESS            | watch_to_green |
| 반도체 후공정 소재   | AI·반도체·전자부품   | SEMI_MATERIALS_PROCESS            | watch_to_green |
| PCB          | AI·반도체·전자부품   | ADVANCED_PACKAGING_PCB            | green_allowed  |
| 유리기판         | AI·반도체·전자부품   | ADVANCED_PACKAGING_PCB            | watch_only     |
| OLED 장비      | AI·반도체·전자부품   | DISPLAY_OLED_EQUIPMENT            | watch_only     |
| OLED 소재·부품   | AI·반도체·전자부품   | DISPLAY_OLED_EQUIPMENT            | watch_only     |
| MLCC         | AI·반도체·전자부품   | ELECTRONIC_COMPONENTS             | watch_only     |
| 스마트폰 부품·소재   | AI·반도체·전자부품   | ELECTRONIC_COMPONENTS             | watch_only     |
| 카메라          | 모빌리티·운송·레저    | AUTO_MOBILITY_COMPONENTS          | watch_only     |
| 무선충전         | AI·반도체·전자부품   | ELECTRONIC_COMPONENTS             | red_watch      |
| 2차전지 소재      | 2차전지·전기차·친환경  | BATTERY_MATERIALS_CAPEX_OVERHEAT  | watch_only     |
| 2차전지 부품      | 2차전지·전기차·친환경  | BATTERY_EQUIPMENT_PARTS           | watch_only     |
| 2차전지 공정장비    | 2차전지·전기차·친환경  | BATTERY_EQUIPMENT_PARTS           | watch_to_green |
| 폐배터리         | 2차전지·전기차·친환경  | BATTERY_RECYCLING_ESS_SHIFT       | watch_only     |
| 전고체 배터리      | 2차전지·전기차·친환경  | BATTERY_RECYCLING_ESS_SHIFT       | red_watch      |
| 전기차 인프라      | 2차전지·전기차·친환경  | EV_INFRASTRUCTURE                 | watch_only     |
| 전기차 화재       | 2차전지·전기차·친환경  | BATTERY_RECYCLING_ESS_SHIFT       | red_flag       |
| 수소차 연료전지     | 2차전지·전기차·친환경  | HYDROGEN_FUEL_CELL_INFRA          | watch_to_green |
| 수소차 인프라      | 2차전지·전기차·친환경  | HYDROGEN_FUEL_CELL_INFRA          | watch_only     |
| 태양광          | 2차전지·전기차·친환경  | SOLAR_TARIFF_SUPPLYCHAIN          | watch_only     |
| 풍력           | 2차전지·전기차·친환경  | RENEWABLE_ENERGY_POLICY           | watch_only     |
| 탄소배출권        | 2차전지·전기차·친환경  | RENEWABLE_ENERGY_POLICY           | event_watch    |
| LNG 발전유통     | 2차전지·전기차·친환경  | ENERGY_DISTRIBUTION_FUEL          | watch_only     |
| 화학           | 소재·스프레드·전략자원  | CHEMICAL_SPREAD                   | red_watch      |
| 정유           | 소재·스프레드·전략자원  | REFINING_OIL_SPREAD               | watch_only     |
| 윤활유          | 소재·스프레드·전략자원  | REFINING_OIL_SPREAD               | watch_to_green |
| 철강 주요업체      | 소재·스프레드·전략자원  | STEEL_METAL_SPREAD                | watch_only     |
| 철강 중소형업체     | 소재·스프레드·전략자원  | STEEL_METAL_SPREAD                | red_watch      |
| 비철금속         | 소재·스프레드·전략자원  | NONFERROUS_STRATEGIC_METALS       | watch_only     |
| 구리           | 소재·스프레드·전략자원  | NONFERROUS_STRATEGIC_METALS       | watch_only     |
| 리튬           | 소재·스프레드·전략자원  | BATTERY_MATERIALS_CAPEX_OVERHEAT  | red_watch      |
| 희토류          | 소재·스프레드·전략자원  | RARE_METALS_STRATEGIC_MATERIALS   | event_watch    |
| 금은           | 소재·스프레드·전략자원  | COMMODITY_SPREAD                  | watch_only     |
| 초전도체         | 정책·지정학·재난·이벤트 | SPECULATIVE_SCIENCE_THEME         | red_flag       |
| 맥신           | 정책·지정학·재난·이벤트 | SPECULATIVE_SCIENCE_THEME         | red_flag       |
| 그래핀          | 정책·지정학·재난·이벤트 | SPECULATIVE_SCIENCE_THEME         | red_flag       |
| 양자 기술        | 정책·지정학·재난·이벤트 | SPECULATIVE_SCIENCE_THEME         | red_watch      |
| 게임           | 플랫폼·콘텐츠·SW·보안 | GAME_CONTENT_IP                   | watch_only     |
| 엔터           | 플랫폼·콘텐츠·SW·보안 | GAME_CONTENT_IP                   | watch_only     |
| 미디어 콘텐츠      | 플랫폼·콘텐츠·SW·보안 | GAME_CONTENT_IP                   | watch_only     |
| 음원서비스        | 플랫폼·콘텐츠·SW·보안 | GAME_CONTENT_IP                   | watch_only     |
| 광고           | 플랫폼·콘텐츠·SW·보안 | MEDIA_AD_CONTENT_CYCLE            | watch_only     |
| 클라우드 컴퓨팅     | 플랫폼·콘텐츠·SW·보안 | CLOUD_AI_SOFTWARE_INFRA           | watch_to_green |
| 인공지능 AI      | 플랫폼·콘텐츠·SW·보안 | AI_SOFTWARE_APPLICATION           | watch_only     |
| IT보안         | 플랫폼·콘텐츠·SW·보안 | SECURITY_IDENTITY_DEEPFAKE        | watch_to_green |
| 딥페이크         | 플랫폼·콘텐츠·SW·보안 | SECURITY_IDENTITY_DEEPFAKE        | watch_only     |
| 생체인식         | 플랫폼·콘텐츠·SW·보안 | SECURITY_IDENTITY_DEEPFAKE        | watch_only     |
| CCTV         | 플랫폼·콘텐츠·SW·보안 | SECURITY_IDENTITY_DEEPFAKE        | watch_only     |
| 메타버스         | 플랫폼·콘텐츠·SW·보안 | METAVERSE_NFT_THEME               | red_watch      |
| 항공사          | 모빌리티·운송·레저    | AIRLINE_TRAVEL_CYCLE              | watch_only     |
| 여행·레저        | 모빌리티·운송·레저    | TRAVEL_LEISURE_REOPENING          | watch_only     |
| 야놀자 관련주      | 모빌리티·운송·레저    | TRAVEL_LEISURE_REOPENING          | event_watch    |
| 카지노          | 모빌리티·운송·레저    | CASINO_DUTYFREE_TOURISM           | watch_only     |
| 면세점          | 모빌리티·운송·레저    | CASINO_DUTYFREE_TOURISM           | watch_only     |
| 해운           | 모빌리티·운송·레저    | SHIPPING_FREIGHT_CYCLE            | red_watch      |
| 택배·종합물류      | 모빌리티·운송·레저    | ECOMMERCE_FRESH_LOGISTICS         | watch_only     |
| 렌터카·중고차      | 모빌리티·운송·레저    | RENTAL_USED_CAR_MOBILITY          | watch_only     |
| 자율주행         | 모빌리티·운송·레저    | AUTO_MOBILITY_COMPONENTS          | watch_only     |
| 현대·기아차 부품주   | 모빌리티·운송·레저    | AUTO_MOBILITY_COMPONENTS          | watch_to_green |
| 타이어          | 모빌리티·운송·레저    | TIRE_AUTO_COMPONENT_SPREAD        | watch_to_green |
| 드론·플라잉카      | 모빌리티·운송·레저    | URBAN_AIR_DRONE                   | red_watch      |
| 대형 건설사       | 건설·부동산·건자재    | CONSTRUCTION_REAL_ESTATE_CREDIT   | red_watch      |
| 중소형 건설사      | 건설·부동산·건자재    | CONSTRUCTION_REAL_ESTATE_CREDIT   | red_watch      |
| 부동산 자산 보유    | 건설·부동산·건자재    | HOLDING_RESTRUCTURING_GOVERNANCE  | watch_only     |
| 리츠           | 건설·부동산·건자재    | REIT_DEVELOPMENT_TRUST            | watch_only     |
| 건자재          | 건설·부동산·건자재    | BUILDING_MATERIALS_CYCLE          | watch_only     |
| 시멘트·레미콘·콘크리트 | 건설·부동산·건자재    | BUILDING_MATERIALS_CYCLE          | watch_only     |
| 철근           | 건설·부동산·건자재    | BUILDING_MATERIALS_CYCLE          | watch_only     |
| 가구           | 건설·부동산·건자재    | BUILDING_MATERIALS_CYCLE          | watch_only     |
| 거푸집          | 건설·부동산·건자재    | BUILDING_MATERIALS_CYCLE          | watch_only     |
| CMO·원료의약품    | 바이오·헬스케어·의료기기 | CDMO_HEALTHCARE_CONTRACT          | green_allowed  |
| CRO          | 바이오·헬스케어·의료기기 | CRO_CLINICAL_SERVICE              | watch_only     |
| 바이오시밀러       | 바이오·헬스케어·의료기기 | CDMO_HEALTHCARE_CONTRACT          | watch_to_green |
| 의료AI         | 바이오·헬스케어·의료기기 | DIGITAL_HEALTHCARE_AI             | watch_only     |
| 원격의료         | 바이오·헬스케어·의료기기 | DIGITAL_HEALTHCARE_AI             | watch_only     |
| AI 신약개발      | 바이오·헬스케어·의료기기 | BIOTECH_PRE_REVENUE_REGULATORY    | red_watch      |
| 비만 치료제       | 바이오·헬스케어·의료기기 | BIOTECH_ROYALTY_COMMERCIALIZATION | watch_only     |
| 탈모치료         | 바이오·헬스케어·의료기기 | BIOTECH_PRE_REVENUE_REGULATORY    | red_watch      |
| 치매치료         | 바이오·헬스케어·의료기기 | BIOTECH_PRE_REVENUE_REGULATORY    | red_watch      |
| 이중항체         | 바이오·헬스케어·의료기기 | BIOTECH_ROYALTY_COMMERCIALIZATION | watch_only     |
| 면역세포치료제      | 바이오·헬스케어·의료기기 | BIOTECH_PRE_REVENUE_REGULATORY    | red_watch      |
| 줄기세포치료제      | 바이오·헬스케어·의료기기 | BIOTECH_PRE_REVENUE_REGULATORY    | red_watch      |
| 보톡스          | 바이오·헬스케어·의료기기 | MEDICAL_DEVICE_HEALTHCARE_EXPORT  | green_allowed  |
| 치아·임플란트      | 바이오·헬스케어·의료기기 | MEDICAL_DEVICE_HEALTHCARE_EXPORT  | green_allowed  |
| 미용기기         | 바이오·헬스케어·의료기기 | MEDICAL_DEVICE_HEALTHCARE_EXPORT  | green_allowed  |
| 전염병 진단       | 바이오·헬스케어·의료기기 | DIAGNOSTICS_INFECTIOUS_DISEASE    | red_watch      |
| 엠폭스          | 정책·지정학·재난·이벤트 | EVENT_DISEASE_PEST_DEMAND         | event_only     |
| 코로나19 제약     | 정책·지정학·재난·이벤트 | EVENT_DISEASE_PEST_DEMAND         | red_watch      |
| 빈대퇴치         | 정책·지정학·재난·이벤트 | EVENT_DISEASE_PEST_DEMAND         | event_only     |
| 황사마스크        | 정책·지정학·재난·이벤트 | EVENT_DISEASE_PEST_DEMAND         | event_only     |
| 양돈주          | 농업·생활서비스·기타   | AGRI_LIVESTOCK_FOOD_COMMODITY     | red_watch      |
| 육계주          | 농업·생활서비스·기타   | AGRI_LIVESTOCK_FOOD_COMMODITY     | red_watch      |
| 배합사료         | 농업·생활서비스·기타   | AGRI_LIVESTOCK_FOOD_COMMODITY     | watch_only     |
| 대두           | 농업·생활서비스·기타   | AGRI_LIVESTOCK_FOOD_COMMODITY     | event_watch    |
| 스마트팜         | 농업·생활서비스·기타   | SMART_FARM_AGRI_TECH              | watch_only     |
| 농기계          | 농업·생활서비스·기타   | SMART_FARM_AGRI_TECH              | watch_only     |
| 교육           | 농업·생활서비스·기타   | EDUCATION_SPECIALTY_SERVICES      | watch_only     |
| 취업일자리        | 농업·생활서비스·기타   | EDUCATION_SPECIALTY_SERVICES      | event_watch    |
| 키즈·유아용품      | 농업·생활서비스·기타   | HOME_CHILD_EDUCATION              | watch_only     |
| 전자담배         | 농업·생활서비스·기타   | CONSUMER_REGULATED_PRODUCT        | watch_only     |

---

# 5. 이제 “테마 다 흡수”라고 볼 수 있는가?

## 사실상 구조적 흡수는 됐다

네가 준 리스트를 기준으로 보면, 이제 대부분의 테마는 아래 중 하나로 들어간다.

```text
green_allowed
watch_to_green
watch_only
red_watch
event_only
red_flag
```

즉 구조적으로는 거의 닫혔다.

## 하지만 100% 완료라고 하려면 audit가 필요하다

다음 작업에서 반드시 해야 할 것:

```text
1. 네가 준 전체 theme list를 CSV로 넣는다.
2. 각 theme_tag를 primary_archetype에 매핑한다.
3. unmatched_theme_tag를 출력한다.
4. unmatched가 0이 될 때까지 추가 archetype 또는 alias를 만든다.
5. green_policy 분포를 본다.
```

그래야 진짜로:

```text
“테마 흡수율 100%”
```

라고 말할 수 있어.

현재 말로 판단하면 **95% 이상은 흡수 가능**하고, 나머지는 이름이 애매한 테마나 중복 테마 alias 문제일 가능성이 크다.

---

# 6. 지금 가장 중요한 다음 구조

에이전트에 넣을 때는 이렇게 가야 해.

```text
data/sector_taxonomy/theme_tag_map_v05.csv
data/sector_taxonomy/theme_aliases.yml
data/e2r_case_library/cases_v03.jsonl
output/theme_coverage_report.md
```

그리고 report는 이렇게 나와야 한다.

```text
total_theme_tags: N
mapped_theme_tags: N
unmatched_theme_tags: 0
green_allowed: count
watch_to_green: count
watch_only: count
red_watch: count
event_only: count
red_flag: count
```

이게 나오면, 그때는 진짜로:

> “테마 구조는 거의 다 흡수됐다.”

라고 말할 수 있다.

---

# 7. 최종 답

응. **이제 사실상 테마는 거의 다 흡수된 구조라고 볼 수 있다.**

다만 정확한 표현은 이거야.

> **테마 구조 흡수는 거의 완료.**
> **점수정규화는 성공/반례/주가검증이 더 필요.**
> **production scoring 적용은 아직 이르다.**
> **다음은 theme_tag_map을 CSV화하고 unmatched audit를 돌려서 100% 커버리지를 확인하는 단계다.**

즉, 네가 준 긴 테마 목록은 이제 다음 구조로 거의 모두 들어간다.

```text
12개 대섹터
→ 70개 안팎 archetype/sub-archetype
→ 200개+ theme tag
→ green_policy
→ must-have evidence
→ red-flag evidence
→ case library
→ price-path validation
```

이렇게 되면 에이전트가 세부 테마를 하나씩 if문으로 외우지 않고도, 각 테마를 적절한 E2R 구조로 보내서 판단할 수 있게 된다.
