맞아. 네가 붙여준 테마 목록을 보면, **지금 우리가 말한 10개 대섹터만으로는 너무 크고, 32개 archetype도 아직 촘촘하지 않다.**

다만 방향은 이렇게 잡아야 해.

```text
테마 하나 = archetype 하나
```

로 만들면 안 돼. 그러면 수백 개 if문이 되고, 점수체계가 망가져.

정답은 이 구조야.

```text
대섹터
→ E2R 구조 archetype
→ 세부 theme tag
→ 증거 필드
→ 성공/반례 case
→ 주가 검증
→ 점수비중 보정
```

즉, 네가 준 `편의점`, `손해보험`, `라면`, `HBM`, `전선-케이블`, `초전도체`, `엠폭스`, `스테이블코인`, `야놀자 관련주` 같은 건 대부분 **theme tag**고, 실제 점수는 그 위의 **E2R archetype**이 담당해야 해.

현재 레포 28A는 아직 fixture-only 상태야. sector taxonomy도 현재는 13개 종목, 8개 archetype만 매핑되어 있고, case library도 25개 archetype 중 “성공 2개 + 반례 2개”를 채운 항목이 0개야.
그래서 지금은 점수 적용보다 **테마 커버리지 확장 + 성공/반례 case matrix 확장**이 먼저 맞다.

---

# 1. 결론: 10개 대섹터는 유지하되, 중간층을 더 쪼개야 함

## 현재 판단

```text
10개 대섹터
→ 너무 뭉툭하지만 top layer로는 OK

32개 archetype
→ 방향은 맞지만 theme coverage가 부족

필요한 구조
→ 12개 대섹터
→ 55~65개 E2R archetype/sub-archetype
→ 200개+ raw theme tag
```

대섹터는 너무 많아지면 안 돼.
하지만 archetype은 더 세분화해야 해.

---

# 2. 확장된 대섹터 v0.3

네가 준 테마 전체를 품으려면 대섹터는 이렇게 12개 정도가 적당해.

| 대섹터               | 설명                                                    |
| ----------------- | ----------------------------------------------------- |
| 1. 산업재·수주·인프라     | 전력설비, 전선, 방산, 조선, 건설기계, 피팅밸브, 원전, 철도                  |
| 2. AI·반도체·전자부품    | HBM, CXL, 시스템반도체, PCB, OLED, MLCC, 유리기판, 클린룸, 스마트폰 부품 |
| 3. 2차전지·전기차·친환경   | 2차전지 소재/부품/장비, 전고체, 폐배터리, 전기차 인프라, 수소, 태양광, 풍력        |
| 4. 소재·스프레드·전략자원   | 화학, 정유, 철강, 비철금속, 리튬, 희토류, 구리, 금은, 페라이트               |
| 5. 소비재·유통·브랜드     | 편의점, 홈쇼핑, 라면, K푸드, 음식료, 화장품, 의류, 건강기능식품               |
| 6. 금융·자본배분·디지털금융  | 은행, 보험, 증권, 금융지주, 고배당, 밸류업, 결제, STO, 스테이블코인           |
| 7. 바이오·헬스케어·의료기기  | CMO, CRO, 바이오시밀러, 임상, 의료AI, 미용기기, 보톡스, 임플란트, 진단       |
| 8. 플랫폼·콘텐츠·SW·보안  | 게임, 엔터, 미디어, 클라우드, AI, IT보안, 딥페이크, 메타버스, NFT          |
| 9. 모빌리티·운송·레저     | 항공, 해운, 택배, 렌터카, 중고차, 여행, 카지노, 면세, 골프                 |
| 10. 건설·부동산·건자재    | 대형/중소형 건설, 리츠, 개발신탁, 건자재, 시멘트, 철근, 가구                 |
| 11. 정책·지정학·재난·이벤트 | 남북경협, 우크라 재건, 네옴시티, 세종시, 지진, 폭염, 황사, 전염병              |
| 12. 교육·생활서비스·농수축산 | 교육, 취업, 키즈, 유아용품, 스마트팜, 농기계, 양돈, 육계, 배합사료, 참치         |

이 12개는 **상위 폴더**야.
점수는 여기서 바로 주면 안 되고, 아래 archetype에서 줘야 해.

---

# 3. 네 테마를 품기 위한 확장 archetype v0.3

아래는 네가 준 테마들을 흡수할 수 있게 확장한 archetype 구조야.

## A. 산업재·수주·인프라

| Archetype                     | 포함 테마                                                |
| ----------------------------- | ---------------------------------------------------- |
| CONTRACT_BACKLOG_INDUSTRIAL   | 전력설비, 전선-케이블, 강관, 피팅 밸브, 건설기계, 조선 기자재, LNG선 기자재      |
| AI_DATA_CENTER_INFRASTRUCTURE | 전력설비, 전선, 광섬유·광케이블·광통신, 냉각시스템, PCB, 클린룸, AI 데이터센터 관련 |
| DEFENSE_GOVERNMENT_BACKLOG    | 방위산업, 항공우주, 드론·플라잉카, 스페이스X 관련                        |
| SHIPBUILDING_OFFSHORE_BACKLOG | 조선, 조선 기자재, LNG선 기자재, 엔진(조선-AI), 피팅밸브                |
| NUCLEAR_SMR_GRID_POLICY       | 원자력, 원전, 스마트그리드, 전력망, 전력설비                           |
| RAIL_INFRASTRUCTURE           | 철도, 우크라 재건, 네옴시티, 대형 인프라                             |
| SMART_FACTORY_AUTOMATION      | 제조용 로봇, 스마트팩토리, 컨택센터 일부, 키오스크 일부                     |

## B. AI·반도체·전자부품

| Archetype              | 포함 테마                                 |
| ---------------------- | ------------------------------------- |
| MEMORY_HBM_CAPACITY    | 반도체-HBM, 종합반도체, 반도체-CXL, 뉴로모픽 반도체 일부  |
| SEMI_EQUIPMENT_CAPEX   | 반도체 전공정 장비, 후공정 장비, 2차전지 공정장비와 교차 가능  |
| SEMI_MATERIALS_PROCESS | 반도체 전공정 소재, 후공정 소재, 클린룸, OLED 소재부품    |
| ADVANCED_PACKAGING_PCB | 인쇄회로기판 PCB, CXL, 유리기판, 후공정, 이수페타시스류   |
| DISPLAY_OLED_EQUIPMENT | OLED 장비, OLED 소재부품, 디스플레이 이송장비        |
| ELECTRONIC_COMPONENTS  | MLCC, 카메라, 스마트폰 부품·소재, 무선충전, LED      |
| AI_CHIP_FABRIC_INFRA   | 퓨리오사AI 관련주, 인공지능 AI, 시스템반도체, 뉴로모픽 반도체 |
| CYBER_AI_SECURITY      | IT보안, 딥페이크, 생체인식, CCTV                |

## C. 2차전지·전기차·친환경

| Archetype                        | 포함 테마                                  |
| -------------------------------- | -------------------------------------- |
| BATTERY_MATERIALS_CAPEX_OVERHEAT | 2차전지 소재, 2차전지 생산·판매, 전고체 배터리, 리튬, 폐배터리 |
| BATTERY_EQUIPMENT_PARTS          | 2차전지 공정장비, 2차전지 부품, 전기차 부품             |
| EV_INFRASTRUCTURE                | 전기차 인프라, 전기차 화재, 무선충전, 수소차 인프라         |
| HYDROGEN_FUEL_CELL               | 수소차 연료전지, 수소차 기타부품, 수소차 인프라            |
| RENEWABLE_ENERGY_POLICY          | 태양광, 풍력, 탄소배출권, 탈 플라스틱                 |
| ENERGY_DISTRIBUTION_FUEL         | LNG 발전유통, LPG, 유가 상승 수혜 유류도소매, 윤활유     |

## D. 소재·스프레드·전략자원

| Archetype                   | 포함 테마                         |
| --------------------------- | ----------------------------- |
| CHEMICAL_SPREAD             | 화학, 페인트, 탈 플라스틱, 주정 일부        |
| REFINING_OIL_SPREAD         | 화학-정유, 유가 상승 수혜, 윤활유, LPG     |
| STEEL_METAL_SPREAD          | 철강 주요업체, 철강 중소형업체, 강관, 건자재 철근 |
| NONFERROUS_STRATEGIC_METALS | 비철금속, 구리, 리튬, 희토류, 금은, 페라이트   |
| ADVANCED_MATERIAL_THEMES    | 그래핀, 맥신, 초전도체, 양자 기술, 페라이트    |
| PAPER_PACKAGING             | 제지, 골판지, 탈 플라스틱 포장재           |
| AGRI_COMMODITY_INPUTS       | 대두, 배합사료, 농업 종자·비료·농약         |

## E. 소비재·유통·브랜드

| Archetype                    | 포함 테마                          |
| ---------------------------- | ------------------------------ |
| EXPORT_RECURRING_CONSUMER    | 라면, K푸드, 음식료, 건강기능식품, 음식료 유통   |
| FOOD_AGRI_LIVESTOCK_CYCLE    | 양돈주, 육계주, 참치 원양어업, 대두, 배합사료    |
| RETAIL_CONVENIENCE_OFFLINE   | 편의점, 홈쇼핑, 음식료 유통, 마켓컬리·오아시스 관련 |
| ECOMMERCE_FRESH_LOGISTICS    | 마켓컬리·오아시스, 콜드체인, 택배와 종합물류      |
| K_BEAUTY_EXPORT_DISTRIBUTION | 화장품 브랜드, K뷰티, 화장품 유통           |
| BEAUTY_OEM_ODM_SUPPLYCHAIN   | 화장품 OEM·ODM, 화장품 원재료 및 부자재     |
| APPAREL_BRAND_OEM            | 의류 브랜드, 의류 OEM·ODM, 의류 소재      |
| HOME_LIVING_APPLIANCE        | 밥솥, 스마트홈, 유아용품, 키즈             |

## F. 금융·자본배분·디지털금융

| Archetype                      | 포함 테마                            |
| ------------------------------ | -------------------------------- |
| FINANCIAL_SPREAD_BALANCE_SHEET | 은행, 금융지주회사, 생명보험, 손해보험           |
| INSURANCE_UNDERWRITING_CYCLE   | 손해보험, 생명보험, 화재, 고배당주             |
| SECURITIES_BROKERAGE_CYCLE     | 증권사, 벤처캐피탈 VC                    |
| VALUE_UP_SHAREHOLDER_RETURN    | 밸류업 지수 편입, 고배당주, 부동산 자산 보유, 금융지주 |
| PAYMENT_FINTECH_INFRA          | 결제서비스, 토스 관련주, 지역화폐, 신용정보        |
| DIGITAL_ASSET_TOKENIZATION     | 스테이블코인, STO, 디지털자산·블록체인, NFT     |

## G. 바이오·헬스케어·의료기기

| Archetype                         | 포함 테마                                  |
| --------------------------------- | -------------------------------------- |
| BIOTECH_PRE_REVENUE_REGULATORY    | 치매치료, 희귀질환 치료제, 면역세포치료제, 줄기세포치료제, 이중항체 |
| BIOTECH_ROYALTY_COMMERCIALIZATION | AI 신약개발, 비만 치료제, 탈모치료, 난임, 치매치료        |
| CDMO_HEALTHCARE_CONTRACT          | CMO·원료의약품, 바이오시밀러, CRO 임상시험수탁          |
| DIAGNOSTICS_INFECTIOUS_DISEASE    | 전염병 진단, 코로나19 제약, 엠폭스, 동물백신·방역         |
| MEDICAL_DEVICE_HEALTHCARE_EXPORT  | 미용기기, 치아·임플란트, 보툴리눔 톡신, 수술용 로봇         |
| DIGITAL_HEALTHCARE_AI             | 의료 AI, 원격의료, 유전체검사, 마이크로바이옴            |
| CANNABIS_REGULATED_HEALTH         | 마리화나 대마초, 규제형 바이오 이벤트                  |

## H. 플랫폼·콘텐츠·SW·보안

| Archetype                    | 포함 테마                         |
| ---------------------------- | ----------------------------- |
| PLATFORM_SOFTWARE_INTERNET   | 클라우드 컴퓨팅, 원격근무, 컨택센터, 광고      |
| GAME_CONTENT_IP              | 게임, 엔터, 미디어 콘텐츠, 음원서비스, 방송·언론 |
| METAVERSE_NFT_THEME          | 메타버스, NFT, 디지털자산, STO와 교차     |
| AI_SOFTWARE_APPLICATION      | 인공지능 AI, AI 신약개발, 의료AI, 딥페이크  |
| SECURITY_IDENTITY_INFRA      | IT보안, 생체인식, CCTV, 딥페이크        |
| EDUCATION_SPECIALTY_SERVICES | 교육, 취업일자리, 키즈, 유아용품 일부        |

## I. 모빌리티·운송·레저

| Archetype                | 포함 테마                         |
| ------------------------ | ----------------------------- |
| AIRLINE_TRAVEL_CYCLE     | 항공사, 여행·레저, 야놀자 관련주           |
| CASINO_DUTYFREE_TOURISM  | 카지노, 면세점, 금강산 관광              |
| SHIPPING_FREIGHT_CYCLE   | 해운, 택배와 종합물류 일부               |
| AUTO_COMPLETED_VEHICLE   | 현대·기아차 부품주 일부, 자동차 연비개선 경량화   |
| AUTO_COMPONENTS_EV_ADAS  | 자율주행, 전기차 부품, 카메라, 스마트폰 부품 일부 |
| RENTAL_USED_CAR_MOBILITY | 렌터카·중고차, 자전거                  |
| URBAN_AIR_DRONE          | 드론·플라잉카, 항공우주, 스페이스X          |

## J. 건설·부동산·건자재

| Archetype                       | 포함 테마                          |
| ------------------------------- | ------------------------------ |
| CONSTRUCTION_REAL_ESTATE_CREDIT | 대형 건설사, 중소형 건설사, 부동산 자산 보유     |
| REIT_DEVELOPMENT_TRUST          | 부동산 개발신탁리츠, 리츠, 부동산 자산 보유      |
| BUILDING_MATERIALS_CYCLE        | 건자재, 시멘트·레미콘·콘크리트, 철근, 거푸집, 가구 |
| INFRA_RECONSTRUCTION_POLICY     | 우크라 재건, 네옴시티, 세종시, 철도          |
| DISASTER_REBUILD_EVENT          | 지진, 폭염, 재난복구, 건자재 이벤트          |

## K. 정책·지정학·재난·이벤트

| Archetype                   | 포함 테마                           |
| --------------------------- | ------------------------------- |
| NORTH_KOREA_POLICY_EVENT    | 남북경협, DMZ, 개성공단, 금강산 관광, 광물자원개발 |
| GEOPOLITICAL_RECONSTRUCTION | 우크라 재건, 네옴시티, 원전 수출, 철도         |
| CLIMATE_DISASTER_EVENT      | 폭염, 황사·미세먼지, 공기정화, 마스크, 지진      |
| INFECTIOUS_DISEASE_EVENT    | 엠폭스, 코로나19, 전염병 진단, 빈대퇴치        |
| SPECULATIVE_SCIENCE_THEME   | 초전도체, 맥신, 그래핀, 양자 기술            |
| POLICY_LOCAL_THEME          | 세종시, 지역화폐, 취업일자리                |

## L. 농업·생활서비스·기타

| Archetype                   | 포함 테마                   |
| --------------------------- | ----------------------- |
| SMART_FARM_AGRI_TECH        | 스마트팜, 농업 종자비료농약, 농기계    |
| LIVESTOCK_FISHERY_CYCLE     | 양돈주, 육계주, 참치 원양어업, 배합사료 |
| HOME_CHILD_EDUCATION        | 키즈, 유아용품, 교육, 밥솥        |
| WASTE_RECYCLING_ENVIRONMENT | 폐기물처리, 폐배터리, 탈 플라스틱     |
| SERVICE_KIOSK_AUTOMATION    | 키오스크, 컨택센터, 스마트홈        |

---

# 4. 이걸 보면 무엇이 부족했나

기존 32개 archetype에는 아래가 부족했어.

```text
1. 편의점/홈쇼핑/콜드체인/마켓컬리·오아시스
   → Retail + E-commerce Fresh Logistics 필요

2. 손해보험/생명보험/증권/VC/신용정보
   → Financial을 은행 하나로 보면 안 됨

3. 화장품 원재료/OEM/ODM/브랜드
   → K-Beauty 안에서도 supply chain 분리 필요

4. 농업/양돈/육계/사료/대두/참치
   → Food consumer가 아니라 agri/livestock cycle 필요

5. 건자재 세부
   → 건설과 다르게 cement/rebar/furniture/formwork cycle 필요

6. 디지털자산/STO/스테이블코인/결제
   → Platform이 아니라 fintech/tokenization 필요

7. 의료기기/바이오/진단/CMO/CRO/원격의료
   → biotech 하나로 묶으면 위험

8. 남북경협/우크라재건/세종시/네옴시티
   → policy/geopolitical event archetype 필요

9. 황사/폭염/지진/전염병/빈대
   → event-demand archetype 필요

10. 초전도체/맥신/그래핀/양자
   → speculative science theme으로 Green 제한 필요
```

즉, 네가 준 리스트를 보니 기존 분류는 **방향은 맞지만 granular coverage가 부족**했다.

---

# 5. 점수비중은 어떻게 바뀌어야 하나

## 5-1. Green 가능성이 높은 구조

```text
CONTRACT_BACKLOG_INDUSTRIAL
AI_DATA_CENTER_INFRASTRUCTURE
DEFENSE_GOVERNMENT_BACKLOG
SHIPBUILDING_OFFSHORE_BACKLOG
EXPORT_RECURRING_CONSUMER
K_BEAUTY_EXPORT_DISTRIBUTION
CDMO_HEALTHCARE_CONTRACT
MEDICAL_DEVICE_HEALTHCARE_EXPORT
MEMORY_HBM_CAPACITY
SEMI_EQUIPMENT_CAPEX
FINANCIAL_SPREAD_BALANCE_SHEET
VALUE_UP_SHAREHOLDER_RETURN
```

공통점:

```text
EPS/FCF 체급 변화가 숫자로 확인 가능
visibility가 1년 이상 지속
시장 프레임이 바뀔 여지
```

## 5-2. Watch/Yellow 중심 구조

```text
PLATFORM_SOFTWARE_INTERNET
GAME_CONTENT_IP
ROBOTICS_FACTORY_AUTOMATION
AUTO_COMPONENTS_EV_ADAS
NUCLEAR_SMR_GRID_POLICY
HOLDING_RESTRUCTURING_GOVERNANCE
TRAVEL_LEISURE_REOPENING
EDUCATION_SPECIALTY_SERVICES
RARE_METALS_STRATEGIC_MATERIALS
UTILITIES_REGULATED_TARIFF
```

공통점:

```text
좋은 후보가 나올 수 있지만
정책/이벤트/밸류/매출화 리스크가 커서 Green은 제한
```

## 5-3. Red/4B 방어 중심 구조

```text
SHIPPING_FREIGHT_CYCLE
COMMODITY_SPREAD
BATTERY_MATERIALS_CAPEX_OVERHEAT
CONSTRUCTION_REAL_ESTATE_CREDIT
BIOTECH_PRE_REVENUE_REGULATORY
ONE_OFF_EVENT_DEMAND
THEME_VALUATION_OVERHEAT
SPECULATIVE_SCIENCE_THEME
INFECTIOUS_DISEASE_EVENT
NORTH_KOREA_POLICY_EVENT
```

공통점:

```text
주가가 급등할 수 있음
EPS가 일시적으로 폭발할 수 있음
하지만 구조적 E2R로 오판하면 위험
```

---

# 6. 테마별 점수 기준의 핵심

## 테마 태그는 점수를 직접 주면 안 됨

예를 들어:

```text
초전도체
맥신
그래핀
스페이스X
퓨리오사AI
야놀자
마켓컬리
금강산 관광
엠폭스
빈대퇴치
```

이런 건 대부분 **테마 태그**야.

이 태그 자체로 점수 주면 안 돼.

점수는 이렇게 줘야 해.

```text
테마 태그
→ 실제 공시/리포트/재무/가격 evidence
→ 해당 archetype의 must-have field 충족 여부
→ EPS/FCF 체급 변화 가능성
→ Stage 판정
```

예:

```text
초전도체 테마
→ 실제 매출/계약/상용화 없음
→ SPECULATIVE_SCIENCE_THEME
→ Green 금지, Stage 1 또는 Red

퓨리오사AI 관련주
→ 실제 지분/계약/매출 exposure 확인
→ AI_CHIP_FABRIC_INFRA or THEME_OVERHEAT
→ exposure 없으면 Green 금지

야놀자 관련주
→ 실제 지분/상장/여행 회복/실적 연결 확인
→ TRAVEL_LEISURE_REOPENING or EVENT_PREMIUM
```

---

# 7. 지금 추가해야 할 case record 그룹

다음 case pack에는 아래를 추가해야 해.

```text
Retail/E-commerce:
- convenience_store_efficiency_success_candidate
- ecommerce_fresh_logistics_candidate
- home_shopping_margin_decline_counterexample
- china_direct_purchase_margin_pressure_counterexample

Insurance/Financial:
- nonlife_insurance_loss_ratio_success_candidate
- life_insurance_csm_candidate
- low_pbr_no_roe_value_trap
- pf_credit_cost_financial_4c

Beauty Supply Chain:
- kbeauty_oem_odm_success_candidate
- cosmetic_raw_material_supplier_candidate
- china_dependency_counterexample
- channel_stuffing_receivables_4c

Agri/Livestock/Food Commodity:
- pork_price_cycle_candidate
- poultry_disease_event_candidate
- feed_cost_squeeze_counterexample
- soybean_cost_pressure_counterexample

Construction Materials:
- cement_price_hike_candidate
- rebar_spread_candidate
- housing_slowdown_materials_4c
- construction_pf_credit_4c

Digital Finance:
- stablecoin_payment_infra_candidate
- sto_platform_candidate
- crypto_theme_no_revenue_counterexample
- regulation_crackdown_4c

Healthcare:
- botox_export_success_candidate
- dental_implant_export_candidate
- cro_cmo_contract_candidate
- clinical_biotech_dilution_4c
- infectious_disease_oneoff_counterexample

Policy/Event:
- north_korea_policy_event_counterexample
- ukraine_reconstruction_order_confirmed_candidate
- neom_city_theme_no_order_counterexample
- speculative_science_theme_counterexample

Climate/Event:
- heatwave_power_demand_candidate
- fine_dust_mask_oneoff_counterexample
- disaster_rebuild_materials_event
- bedbug_event_oneoff
```

---

# 8. 중간 결론

네가 보낸 테마 리스트를 기준으로 보면:

```text
현재 10 대섹터만으로는 너무 큼.
현재 32 archetype만으로는 부족.
하지만 12 대섹터 + 55~65 archetype/sub-archetype + theme tag 구조면 전부 품을 수 있음.
```

그리고 중요한 건:

```text
테마명 자체는 점수 입력이 아니다.
테마명은 검색/분류/쿼리 생성용 tag다.
점수는 EPS/FCF, visibility, bottleneck, mispricing, valuation, risk evidence로 들어가야 한다.
```

---

# 9. 다음 라운드에서 할 작업

다음 라운드는 이렇게 가는 게 좋다.

```text
Round 9:
네가 준 테마 리스트를 theme tag taxonomy로 변환
→ 각 theme tag를 대섹터/archetype에 매핑
→ unmatched theme 0개 목표
→ green_allowed / watch_only / red_flag 중심으로 구분
→ case record 추가 후보 생성
```

그다음 에이전트에 넣을 때는:

```text
data/sector_taxonomy/theme_tag_map.csv
data/e2r_case_library/cases_v03.jsonl
output/e2r_case_library_v03/theme_coverage_report.md
```

형태로 넣으면 된다.

---

# 10. 최종 답

네 리스트를 보면, 지금 우리가 만든 10개 대섹터는 **상위 구조로는 괜찮지만**, 실제 전 종목·전 테마 커버리지에는 부족하다.

그래서 나는 다음처럼 확장하는 게 맞다고 본다.

```text
10개 대섹터
→ 12개 대섹터로 확장

32개 archetype
→ 55~65개 archetype/sub-archetype으로 확장

수백 개 테마명
→ theme tag로 별도 관리

점수
→ theme tag가 아니라 archetype별 evidence와 price-validation으로 부여
```

이렇게 해야 네가 준 편의점, 손해보험, 라면, HBM, 스테이블코인, 전선, 원전, 초전도체, 카지노, 화장품 OEM, CMO, 콜드체인, 우크라 재건, 피지컬AI 같은 세부 테마를 전부 품으면서도, 기존 서생원식 정신을 잃지 않을 수 있어.
