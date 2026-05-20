좋아. **R10 Loop 5까지 끝났으니, 이번은 R11 Loop 5 — 정책·지정학·재난·이벤트**로 간다.

R11은 새 종목군을 많이 찾는 라운드라기보다, **R1~R12에서 나온 테마가 “뉴스성 이벤트”인지, 아니면 실제 계약·예산·조달·financing·반복매출로 승격됐는지 걸러내는 방어 라운드**다. Theme Tag Map 기준으로도 남북경협, DMZ, 개성공단, 금강산 관광, 황사·마스크, 엠폭스, 코로나 진단, 초전도체, 맥신, 그래핀, 양자기술 같은 태그는 대부분 Event/Red 또는 SPECULATIVE_SCIENCE_THEME 성격이고, Stage 3-Green보다 RedTeam/4B 방어가 중요하다.

Checkpoint 20 원칙도 그대로 적용한다. 정부계약, 예산, 공사착수, stockpile 주문, 계약금액, 매출 가이던스, 진단매출 감소, 재현 실패 같은 값은 실제 확인된 증거만 써야 한다. 정책·재난·과학 테마는 “뉴스가 크다”는 이유로 없는 매출·계약·EPS를 만들어 넣으면 가장 빨리 점수체계가 오염된다.

서생원식으로도 R11의 기준은 선명하다. **정책·재난·지정학 뉴스가 크냐**가 아니라, 그 뉴스가 실제 계약·예산·반복매출·EPS/FCF 체급 변화로 넘어갔느냐다. 이벤트는 Stage 1을 만들 수 있지만, Stage 3-Green을 만들려면 숫자로 확인되는 수익화 증거가 필요하다.

---

# R11 Loop 5. 정책·지정학·재난·이벤트

## 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
Loop 5 목표 =
뉴스성 이벤트 / 정책 기대 / 지정학 리스크 / 전염병 one-off /
기후재난 / 과학 테마 / 정책 shock / 정부조달 / 재건 financing을
실제 계약·예산·매출 승격 여부로 재분류
```

이번 회차의 핵심 질문은 이거다.

```text
이 뉴스는 단순 이벤트인가?
아니면 실제 정부계약, 예산, financing, 공사착수, stockpile,
반복매출, EPS/FCF로 승격됐는가?
```

R11에서 가장 위험한 오판은 여전히 이거다.

```text
뉴스가 크다
= 구조적 Green
```

Loop 5부터는 이렇게 자른다.

```text
좋은 Stage 2 후보:
전염병 이벤트 + 정부 stockpile 계약 + 매출 가이던스 상향
재건 테마 + 실제 EBRD/IFC financing + 운영회사/자산
전쟁 복구 + 전력·통신·항만 등 critical infrastructure financing
폭염 이벤트 + 실제 VPP/배터리 프로그램 + 전력망 투자
정책 발표 + 예산 배정 + 계약 + 착공 + 매출 인식

위험한 후보:
정책 발표만 있는 지역 테마
MOU만 있는 재건 테마
정상회담 기대만 있는 남북경협
전염병 뉴스만 있는 진단·백신 테마
정부계약이 취소되는 백신·방역 테마
황사·폭염·지진·빈대 같은 one-off 수요
초전도체·맥신·그래핀 같은 재현/상용화 전 과학 테마
주가만 먼저 움직인 테마주
```

---

## 2. 대상 canonical archetype

| canonical archetype                       | Loop 5 정책                                         |
| ----------------------------------------- | ------------------------------------------------- |
| `NORTH_KOREA_POLICY_EVENT`                | Event/Red. 실제 사업 재개·제재 완화 전 Green 금지              |
| `GEOPOLITICAL_RECONSTRUCTION`             | Event/Watch. 실제 계약·financing·착공 확인 필요             |
| `REAL_RECONSTRUCTION_FINANCING`           | Watch-to-Green 후보. 재건이 실제 금융·운영회사·자산으로 연결된 경우     |
| `CRITICAL_INFRA_RECONSTRUCTION_FINANCING` | Watch-to-Green 후보. 전력망·통신망·항만·보호시설 financing 확인   |
| `DISASTER_REBUILD_EVENT`                  | Event/Watch. one-off 복구수요와 반복 매출 분리               |
| `CLIMATE_DISASTER_EVENT`                  | Watch. 폭염·냉각·전력망·VPP로 연결될 때만 점수 상승                |
| `CLIMATE_EVENT_TO_GRID_INFRA`             | Watch-to-Green 후보. 기후 이벤트가 grid/VPP/ESS 계약으로 승격   |
| `EVENT_DISEASE_PEST_DEMAND`               | Event/Red. 정부 stockpile·반복 조달 전까지 Green 제한        |
| `EVENT_TO_CONTRACT_ESCALATION`            | Watch-to-Green 후보. 이벤트가 실제 계약·예산·매출로 승격           |
| `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE`   | Watch-to-Green 후보. stockpile 계약이 가이던스까지 올리는 경우    |
| `PUBLIC_HEALTH_PROCUREMENT_REVERSAL`      | RedTeam overlay. 정부계약 취소·funding withdrawal       |
| `DIAGNOSTICS_INFECTIOUS_EVENT`            | Event/Red. 진단 one-off 정상화 리스크 큼                   |
| `SPECULATIVE_SCIENCE_THEME`               | Red. 재현·상용화·계약·매출 전 Green 금지                      |
| `ADVANCED_MATERIAL_SPECULATIVE_THEME`     | Watch/Red. 실제 제품·고객·매출 필요                         |
| `POLICY_LOCAL_THEME`                      | Event. 예산·계약·착공 전 Stage 1                         |
| `POLICY_MARKET_SHOCK_EVENT`               | RedTeam overlay. 세금·배당·분배 발언이 시장 전체를 흔드는 경우       |
| `INDUSTRIAL_POLICY_TARIFF_EVENT`          | Watch/Event. 관세·보조금·수입규제는 수혜와 리스크를 동시에 만듦         |
| `ONE_OFF_EVENT_DEMAND`                    | RedTeam overlay. 일회성 수요를 구조적 수요와 분리               |
| `THEME_VALUATION_OVERHEAT`                | RedTeam overlay. 주가만 급등한 테마 차단                    |
| `DISCLOSURE_CONFIDENCE_CAP`               | RedTeam cap. 예산·계약·수주·공사착수 detail 부족 시 Stage 3 제한 |

---

## 3. deep sub-archetype

```text
NORTH_KOREA_POLICY_EVENT
- 금강산 관광
- 개성공단
- DMZ
- 남북철도
- 북한 광물자원
- 제재 완화 기대
- 정상회담
- 군사 긴장
- 시설 철거
- 도로·철도 폭파

GEOPOLITICAL_RECONSTRUCTION
- 우크라 재건
- 통신망 복구
- 전력망 복구
- 주거·교량·도로 복구
- 의료 인프라
- 항만 concession
- 지뢰 제거
- 실제 financing
- 실제 참여기업
- 실제 공사착수

CRITICAL_INFRA_RECONSTRUCTION_FINANCING
- EBRD
- IFC
- port terminal concession
- transformer protection shelters
- renewable energy expansion
- telecom resilience
- grid resilience
- guarantee structure
- infrastructure asset
- operating company

CLIMATE_DISASTER_EVENT
- 폭염
- 냉각수요
- 에어컨
- 전력피크
- 전력망 stress
- 수요반응
- VPP
- plug-in battery
- 황사·미세먼지
- 공기정화
- 마스크

EVENT_DISEASE_PEST_DEMAND
- 엠폭스
- 코로나
- H5N1
- 빈대
- 조류독감
- ASF
- 백신 stockpile
- 정부 비축
- 방역제
- 마스크

EVENT_TO_CONTRACT_ESCALATION
- government order
- vaccine stockpile
- contract option
- revenue guidance raised
- EBITDA margin raised
- budget allocated
- project financing
- actual construction start

PUBLIC_HEALTH_PROCUREMENT_REVERSAL
- BARDA funding withdrawal
- government contract cancellation
- vaccine procurement reversal
- political health-policy shock
- clinical development funding gap
- late-stage trial uncertainty

DIAGNOSTICS_INFECTIOUS_EVENT
- 코로나 진단
- 엠폭스 진단
- 전염병 진단키트
- 검사 수요 정상화
- 진단 매출 급감
- 재고 증가

SPECULATIVE_SCIENCE_THEME
- 초전도체
- LK-99
- 맥신
- 그래핀
- 양자 소재
- 페라이트
- 논문·preprint
- 재현 실패
- 상용화 부재

POLICY_MARKET_SHOCK_EVENT
- 세금정책
- AI 배당금
- 초과이익 환수 발언
- 거래세·양도세·법인세
- 배당세 정책
- 정책 코멘트로 인한 지수 급락
```

---

# 4. 성공사례 / Stage 2 승격 후보

## 4-1. Bavarian Nordic — `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE`

Bavarian Nordic은 R11에서 보기 드문 `EVENT_TO_CONTRACT_ESCALATION` 후보로 둔다. 회사는 미국 정부로부터 Jynneos 동결건조 제형 추가 계약 옵션 9,700만 달러를 받았고, 이 계약을 반영해 2026년 매출 가이던스를 50억~52억 덴마크크로네에서 55억~57억 덴마크크로네로, EBITDA margin 전망을 25%에서 약 28%로 올렸다. 이건 단순 엠폭스 뉴스가 아니라 **정부 stockpile 계약 + 매출 가이던스 상향 + EBITDA margin 상향**으로 승격된 사례다. ([Reuters][1])

```text
가격경로 1차 판정:
EVENT_TO_CONTRACT_SUCCESS_CANDIDATE

좋은 점:
- 정부계약
- stockpile 수요
- 매출 가이던스 상향
- EBITDA margin 상향
- FDA 승인 제형과 정부 비축 연결

주의:
- 전염병 수요는 반복성이 약할 수 있음
- stockpile 계약이 반복되는지 확인 필요
- outbreak 정상화 시 EPS 정상화 가능
```

**Loop 5 교정**

```text
EVENT_DISEASE_PEST_DEMAND:
뉴스만 있으면 Event/Red.

정부계약 + 매출 가이던스 + 반복 stockpile 가능성이 있으면 Stage 2 후보.

Stage 3는 반복 조달과 FCF 확인 전까지 제한.
```

---

## 4-2. Moderna bird-flu vaccine — `PUBLIC_HEALTH_PROCUREMENT_REVERSAL`

Loop 5에서는 전염병 계약의 반대축도 추가한다. Moderna는 CEPI로부터 mRNA 기반 조류독감 백신 mRNA-1018의 late-stage 개발을 위해 최대 5,430만 달러 funding을 확보했지만, 그 전에는 미국 정부가 Moderna의 pandemic flu/H5N1 백신 개발·구매를 위한 7.66억 달러 규모 BARDA funding을 취소했다. 즉 전염병·백신 테마는 계약이 있으면 Stage 2 후보가 될 수 있지만, **정부계약 취소·정책 전환·funding withdrawal**이 나오면 즉시 4C-watch다. ([Reuters][2])

```text
가격경로 1차 판정:
PUBLIC_HEALTH_PROCUREMENT_REVERSAL_4C_WATCH

교훈:
질병 리스크
≠ 정부계약 지속

감점 조건:
- BARDA_funding_withdrawal
- government_contract_cancelled
- late_stage_trial_funding_gap
- political_health_policy_shock
- procurement_uncertainty
```

**Loop 5 교정**

```text
GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE와
PUBLIC_HEALTH_PROCUREMENT_REVERSAL을 분리한다.

좋은 이벤트:
계약 + stockpile + 가이던스 상향

나쁜 이벤트:
계약 취소 + funding withdrawal + trial uncertainty
```

---

## 4-3. 우크라이나 통신망 복구 — `REAL_RECONSTRUCTION_FINANCING`

우크라 재건은 대부분 Event/Watch지만, 실제 금융기관 자금과 인프라 자산이 붙으면 Stage 2 후보가 된다. EBRD와 IFC는 우크라이나의 Lifecell과 Datagroup-Volia를 결합한 신규 통신회사에 총 4.35억 달러를 제공하기로 했고, 이는 네트워크 속도·커버리지·회복력을 높이는 통신 인프라 투자로 설명된다. 이 사례는 재건 테마가 **실제 외국인 투자·인프라 자산·운영회사**로 구체화된 경우다. ([Reuters][3])

```text
가격경로 1차 판정:
REAL_RECONSTRUCTION_FINANCING_CANDIDATE

좋은 점:
- EBRD·IFC financing
- 실제 통신 인프라 자산
- 인수·합병 완료 회사
- network resilience 개선 목적
- 보증 구조 존재

주의:
- 한국 관련주로 직접 매핑하려면 실제 수주·계약·매출 연결 필요
- 재건 선언이나 MOU와 구분해야 함
- 전쟁·보험·보증·환율 리스크는 남음
```

**Loop 5 교정**

```text
GEOPOLITICAL_RECONSTRUCTION:
재건회의·지원선언·MOU = Stage 1.

financing + 참여기업 + 자산 + 계약 = Stage 2.

다년 매출·마진·수주잔고 확인 전 Stage 3 금지.
```

---

## 4-4. 우크라 critical infra financing — `CRITICAL_INFRA_RECONSTRUCTION_FINANCING`

Loop 5에서는 우크라 재건을 더 쪼갠다. EBRD는 2026년 5월 기준 우크라이나의 민영화·전력 인프라 회복을 지원할 수 있다고 밝혔고, Chornomorsk 항만 40년 concession, 700MW 재생에너지 확대, critical electricity transformer 보호시설 135개 중 118개를 연말까지 확보하는 계획 등이 언급됐다. 이건 단순 재건 테마가 아니라 **항만 concession + 전력망 보호 + 재생에너지 expansion**처럼 실제 infrastructure financing으로 넘어가는 축이다. ([Reuters][4])

```text
가격경로 1차 판정:
CRITICAL_INFRA_RECONSTRUCTION_STAGE2_REFERENCE

좋은 점:
- 항만 concession 구조
- transformer protection shelters
- renewable capacity expansion
- EBRD/IFC structuring
- 실제 critical infrastructure asset

주의:
- 전쟁 지속
- 공습·보험·보증 리스크
- 한국 상장사 직접 수주 연결 확인 필요
- concession·financing이 매출로 인식되는 시점 확인 필요
```

**Loop 5 교정**

```text
CRITICAL_INFRA_RECONSTRUCTION_FINANCING 신규 추가.

Stage 1:
재건 필요성·지원선언.

Stage 2:
concession / financing / 보호시설 / 전력망 / 통신망 asset 확인.

Stage 3:
개별 기업 수주·매출·마진으로 연결될 때.
```

---

## 4-5. 폭염·냉각·전력망 — `CLIMATE_EVENT_TO_GRID_INFRA`

폭염 자체는 `CLIMATE_DISASTER_EVENT`지만, 전력망·냉각·수요반응·VPP로 연결되면 R1/R2/R3와 교차하는 구조증거가 될 수 있다. 독일 사례 연구는 폭염 시나리오에서 가정용 이동식 에어컨 보급률이 19%에서 35%로 올라가면 피크 전력수요가 12.9GW 이상 증가할 수 있고, 오후 피크가 태양광 출력 저하 시간과 겹쳐 전력계통 안정성 부담을 키울 수 있다고 분석했다. ([arXiv][5])

뉴욕에서는 폭염 피크 시간대 창문형 에어컨 부하를 줄이기 위해 임차인에게 plug-in battery를 제공하는 시범 프로그램이 진행 중이고, 200kW flexible capacity에서 2MW 이상·1,000가구 이상으로 확장될 예정이라고 보도됐다. 이건 폭염 테마가 단순 에어컨 이벤트가 아니라 **수요반응·분산배터리·VPP**로 연결될 수 있음을 보여준다. ([AP News][6])

```text
가격경로 1차 판정:
CLIMATE_EVENT_TO_GRID_INFRA_WATCH

좋은 점:
- 폭염 → 전력피크
- 에어컨 → grid stress
- battery/VPP → 실제 프로그램
- R1 전력망, R2 냉각, R3 ESS와 교차 가능

주의:
- 폭염 자체는 계절성 이벤트
- 개별 종목은 실제 계약·매출·OPM 필요
- 파일럿 프로그램은 Stage 2 후보일 뿐, 대규모 반복매출은 별도 확인 필요
```

**Loop 5 교정**

```text
CLIMATE_DISASTER_EVENT:
폭염·황사는 Stage 1 event.

전력망 투자, 냉각 수주, ESS/VPP 계약이 붙으면
다른 대섹터의 Stage 2로 이관.

이관 전에는 one-off event로 유지.
```

---

# 5. 반례 / RedTeam

## 5-1. 남북경협·금강산 관광 — `NORTH_KOREA_POLICY_EVENT` hard Red bias 유지

남북경협은 R11에서 기본값을 `Event/Red`로 유지한다. 북한은 금강산 지역의 이산가족 상봉 시설을 철거하고 있고, 한국 정부는 이를 반인도적 행위로 비판했다. Reuters는 북한이 한국을 “적대국”으로 규정했고, 남북 도로·철도 일부도 폭파한 적이 있다고 보도했다. 이런 환경에서는 금강산 관광, 개성공단, 남북철도, DMZ, 북한 광물개발 관련주는 실제 사업 재개·제재 완화·정부 승인·현금흐름 전까지 Green을 주면 안 된다. ([Reuters][7])

```text
가격경로 1차 판정:
NORTH_KOREA_POLICY_EVENT_RED_BIAS

교훈:
남북경협 기대
≠ 구조적 Green

4C 조건:
- 시설 철거
- 도로·철도 폭파
- 군사 긴장
- 제재 지속
- hostile state rhetoric
```

**Loop 5 교정**

```text
NORTH_KOREA_POLICY_EVENT:
회담·관광 기대는 Stage 1 event.

군사·제재·시설철거 flag가 켜지면 Red.

실제 사업 재개·제재 완화·정부 승인·현금흐름 전까지 Stage 3-Green 금지.
```

---

## 5-2. LK-99 — `SPECULATIVE_SCIENCE_THEME` hard counterexample

LK-99는 R11에서 가장 중요한 과학 테마 반례다. 독립 재현 연구는 실온·상압 초전도성을 확인하지 못했다. 한 arXiv 연구는 LK-99 샘플이 실온에서 초전도 신호를 보이지 않았고, SQUID magnetization 측정에서도 실온 초전도 신호가 없었다고 보고했다. 또 다른 연구는 원 논문에서 초전도 증거처럼 보인 저항·열용량 이상이 Cu₂S, 즉 copper sulfide 불순물의 구조전이에 의해 설명될 수 있다고 지적했다. 즉 LK-99는 **preprint·SNS·영상 기반 테마가 실제 재현·상용화·매출로 넘어가지 못한 대표 사례**다. ([arXiv][8])

```text
가격경로 1차 판정:
SPECULATIVE_SCIENCE_FAILURE_HARD_4C

교훈:
논문·preprint·영상
≠ 제품
≠ 고객계약
≠ EPS/FCF

Stage 3 금지 조건:
- 재현 실패
- peer review 없음
- 상용 제품 없음
- 고객사 없음
- 매출 없음
```

**Loop 5 교정**

```text
SPECULATIVE_SCIENCE_THEME:
기본값 Red.

Stage 2가 되려면:
independent replication
+ peer-reviewed validation
+ prototype customer validation
+ 계약

이 필요.
```

---

## 5-3. 전염병 진단 one-off — COVID 검사 수요 정상화

전염병 진단은 EPS가 폭발할 수 있지만 지속성이 약하다. Abbott의 2025년 3분기 diagnostics segment 매출은 COVID-19와 당뇨 검사 수요 약화 등으로 6.6% 감소했고, 회사의 전체 매출도 시장 예상에 소폭 못 미쳤다. 이 사례는 진단키트·전염병 수요가 정상화되면 EPS가 빠르게 꺾일 수 있음을 보여준다. ([Reuters][9])

```text
가격경로 1차 판정:
DIAGNOSTICS_ONE_OFF_NORMALIZATION_4C

교훈:
전염병 진단 매출
≠ 구조적 Green

Green 조건:
- 설치기반
- 다양한 검사 메뉴
- 비전염병 반복검사
- 장기 고객계약
- one-off 수요 이후에도 FCF 유지
```

---

## 5-4. 정책 코멘트 shock — `POLICY_MARKET_SHOCK_EVENT`

R11은 개별 테마뿐 아니라 시장 전체 정책 이벤트도 RedTeam으로 본다. 2026년 5월 12일 한국 증시는 AI 수익 일부를 국민에게 돌려야 한다는 취지의 정책성 발언 이후 코스피가 장중 5.1% 하락하고 종가 기준 2.3% 하락했다. 이후 해당 발언은 세율 인상이 아니라 늘어난 세수 활용에 관한 취지라고 해명됐지만, 이미 과열된 AI·반도체·value-up rally에서는 정책 코멘트 하나도 price-path를 크게 흔들 수 있다. ([마켓워치][10])

```text
가격경로 1차 판정:
POLICY_MARKET_SHOCK_EVENT

의미:
정책 발언은 기업 실적을 직접 바꾸지 않아도
valuation과 risk premium을 즉시 흔들 수 있다.

감점 조건:
- windfall_tax_comment
- citizen_dividend_comment
- corporate_tax_uncertainty
- market_wide_selloff
- policy_clarification_needed
```

**Loop 5 교정**

```text
POLICY_MARKET_SHOCK_EVENT:
개별 종목 Stage 3를 깨는 hard 4C는 아니더라도,
4B 과열 구간에서는 price-path validation에 반드시 넣는다.
```

---

## 5-5. 관광·비자 정책 이벤트 — `POLICY_LOCAL_THEME` / `TOURISM_POLICY_EVENT`

한국의 중국 단체관광객 무비자 정책은 면세점, 카지노, 호텔, 화장품에 강한 Stage 1 촉매가 될 수 있다. 한국은 2025년 9월 29일부터 2026년 6월까지 중국 단체관광객에게 최대 15일 무비자 입국을 허용하기로 했고, 이 발표 직후 백화점·호텔·카지노·화장품 관련주가 중국 소비 기대감으로 움직였다. 하지만 R11 기준에서는 이 정책을 **관광객 수·객단가·drop amount·면세 매출·OPM 확인 전까지 Event/Watch**로 둬야 한다. ([Reuters][11])

```text
가격경로 1차 판정:
POLICY_TOURISM_EVENT_STAGE1

교훈:
정책 완화
≠ 소비재/관광 구조적 Green

필수 확인:
- visitor_arrivals
- average_spend
- casino_drop_amount
- duty_free_sales
- hotel_revpar
- OPM
```

---

# 6. 4B-watch 사례

## 6-1. 전염병 백신·진단 4B-watch

```text
4B 조건:
- WHO emergency 또는 outbreak 뉴스 직후 관련주 급등
- 실제 정부 주문보다 기대가 먼저 반영
- stockpile 계약 지속성 미확인
- outbreak 정상화 가능성을 시장이 무시
- 정부계약 취소 가능성을 무시
```

Bavarian Nordic은 정부계약과 가이던스 상향이 붙어 Stage 2 후보지만, Moderna의 bird-flu funding 사례처럼 공중보건 조달은 정책 변화로 뒤집힐 수 있다. 따라서 질병 테마는 `EVENT_TO_CONTRACT`와 `PROCUREMENT_REVERSAL`을 동시에 점검해야 한다. ([Reuters][1])

---

## 6-2. 우크라 재건 4B-watch

```text
4B 조건:
- 재건회의·지원선언·MOU만으로 관련주 동반 급등
- 실제 financing·계약·착공 없음
- 참여 기업과 매출 인식 경로가 불명확
- 지정학 리스크를 시장이 낮게 봄
```

EBRD·IFC의 우크라 통신 인프라 투자는 좋은 Stage 2 reference지만, 한국 상장주에 매핑하려면 실제 계약·수주·매출 연결이 필요하다. 재건 테마 전체를 이 사례 하나로 Green 처리하면 안 된다. ([Reuters][3])

---

## 6-3. Critical infra reconstruction 4B-watch

```text
4B 조건:
- 전력망 보호·항만 concession·재생에너지 financing 뉴스로 관련주 급등
- 실제 참여기업·계약금액·공사착수 없음
- 전쟁 리스크와 보험·보증 비용을 낮게 봄
- transformer shelter나 port concession을 국내 관련주 매출로 과잉 매핑
```

EBRD가 항만 concession, transformer 보호시설, 재생에너지 확장을 지원할 수 있다는 점은 재건의 질을 높이는 reference지만, 개별 기업 수주·마진이 없으면 Stage 3가 아니다. ([Reuters][4])

---

## 6-4. 남북경협 4B-watch

```text
4B 조건:
- 정상회담·관광 재개 기대만으로 관련주 급등
- 제재·군사 긴장·시설 철거를 무시
- 실제 사업 재개 승인 없음
```

금강산 시설 철거와 남북 도로·철도 폭파 사례는 남북경협 테마가 언제든 4C로 전환될 수 있음을 보여준다. ([Reuters][7])

---

## 6-5. 초전도체·맥신·그래핀 4B-watch

```text
4B 조건:
- preprint·영상·SNS만으로 관련주 급등
- 거래소 투자경고
- 독립 재현 전 valuation 과열
- 상용화·고객계약 없음
```

LK-99는 독립 재현 실패와 copper sulfide impurity explanation이 나온 뒤 speculative science theme의 핵심 4B/4C 기준 사례가 됐다. ([arXiv][8])

---

## 6-6. 폭염·전력망 테마 4B-watch

```text
4B 조건:
- 폭염 뉴스 후 에어컨·전력·냉각·배터리 관련주 동반 급등
- 실제 수주·프로그램·매출 전 가격이 먼저 감
- 계절성 수요를 구조적 수요로 오판
```

폭염은 전력피크와 grid stress를 만들 수 있지만, 개별 종목은 전력망 투자·수요반응·배터리/VPP 계약 등으로 연결될 때만 Stage 2 후보가 된다. 독일 AC peak-load 연구와 뉴욕 plug-in battery pilot은 구조증거 후보지만, 개별 상장사 매출 연결은 별도로 검증해야 한다. ([arXiv][5])

---

## 6-7. 정책 shock 4B-watch

```text
4B 조건:
- 이미 AI·반도체·밸류업 rally가 과열
- 정책 코멘트 하나로 index와 주도주가 크게 흔들림
- 정부 해명 전까지 risk premium이 급등
```

AI 시민배당·세수배분성 발언으로 코스피가 장중 5.1% 하락했다는 보도는, crowded rally에서는 정책 이벤트가 sector thesis를 깨지 않아도 가격경로를 강하게 훼손할 수 있음을 보여준다. ([마켓워치][10])

---

# 7. 4C-thesis-break 사례

## 7-1. 남북관계 악화

```text
4C:
facility_dismantle
road_rail_destroyed
hostile_state_rhetoric
sanctions_continue
military_tension
```

금강산 시설 철거와 남북 도로·철도 폭파는 `NORTH_KOREA_POLICY_EVENT`의 hard 4C다. ([Reuters][7])

---

## 7-2. 과학 테마 재현 실패

```text
4C:
replication_failure
impurity_explanation
no_peer_reviewed_validation
no_product
no_customer_contract
no_revenue
```

LK-99는 독립 재현 실패와 Cu₂S 불순물 설명 때문에 `SPECULATIVE_SCIENCE_THEME`의 hard 4C 기준 사례다. ([arXiv][8])

---

## 7-3. 전염병 수요 정상화

```text
4C:
outbreak_normalization
government_purchase_ends
diagnostic_sales_decline
inventory_build
EPS_normalization
```

Abbott diagnostics 매출 감소는 진단키트 one-off 구조를 보여준다. 전염병 검사 매출이 구조적 진단 플랫폼 매출로 바뀌지 않으면 Stage 3-Green은 막아야 한다. ([Reuters][9])

---

## 7-4. 정부 조달 취소 / funding withdrawal

```text
4C:
government_contract_cancelled
BARDA_or_public_funding_withdrawal
late_stage_trial_funding_gap
clinical_development_delay
policy_reversal
```

Moderna의 bird-flu vaccine funding 사례는 “질병 위험이 커서 정부가 계속 돈을 넣을 것”이라는 가정이 틀릴 수 있음을 보여준다. 정부 조달형 바이오·방역주는 계약 지속성과 정책 방향을 같이 봐야 한다. ([AP News][12])

---

## 7-5. 재건 financing failure

```text
4C-watch:
financing_delay
insurance_absent
war_reescalation
project_delay
no_contract_after_MOU
```

우크라 재건은 실제 financing·참여기업·자산이 붙으면 Stage 2가 될 수 있지만, 선언·회의·MOU만 있으면 event premium으로 둬야 한다. ([Reuters][3])

---

## 7-6. 기후·재난 one-off 수요

```text
4C-watch:
seasonal_demand_normalization
inventory_build
weather_event_ends
no_follow_on_contract
policy_budget_delay
```

폭염·황사·재난복구는 실제 전력망·냉각·VPP·ESS·복구 계약으로 승격되지 않으면 one-off로 분류해야 한다. ([arXiv][5])

---

## 7-7. 정책 코멘트로 인한 price-path break

```text
4C-watch:
market_wide_policy_shock
tax_or_redistribution_comment
government_clarification_needed
valuation_risk_premium_spike
crowded_trade_unwind
```

정책 코멘트가 실제 세금으로 확정되지 않았더라도, 주도주와 지수가 이미 4B 구간에 있으면 price-path를 깨는 강한 overlay가 된다. ([마켓워치][10])

---

# 8. 점수비중 보정표 — R11 Loop 5 / v5.0

| canonical archetype                       | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Loop 5 핵심 감점                       |
| ----------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | ---------------------------------- |
| `NORTH_KOREA_POLICY_EVENT`                |       4 |          3 |          5 |          8 |         4 |       0 |    3 | 제재, 군사긴장, 시설철거, 실제 계약 없음           |
| `GEOPOLITICAL_RECONSTRUCTION`             |      12 |         11 |          8 |         10 |         8 |       0 |    4 | financing, 전쟁 지속, 실제 수주 없음         |
| `REAL_RECONSTRUCTION_FINANCING`           |      14 |         15 |          9 |         11 |         9 |       0 |    5 | 한국 상장사 직접 연결 부재, 전쟁 리스크            |
| `CRITICAL_INFRA_RECONSTRUCTION_FINANCING` |      15 |         16 |         10 |         12 |         9 |       0 |    5 | 보험·보증·공습 리스크, 매출 인식 불명확            |
| `DISASTER_REBUILD_EVENT`                  |      10 |          6 |          7 |          8 |         6 |       0 |    4 | one-off 수요, 보험·예산 지연               |
| `CLIMATE_DISASTER_EVENT`                  |      13 |         14 |         11 |         10 |         8 |       0 |    5 | 계절성, 매출화 불명확, 재고                   |
| `CLIMATE_EVENT_TO_GRID_INFRA`             |      15 |         16 |         13 |         11 |         9 |       0 |    5 | 파일럿 수준, 개별 매출 연결 미확인               |
| `EVENT_DISEASE_PEST_DEMAND`               |      13 |          9 |          8 |          8 |         6 |       0 |    5 | outbreak 정상화, 정부 구매 종료             |
| `EVENT_TO_CONTRACT_ESCALATION`            |      15 |         14 |          8 |         10 |         8 |       0 |    5 | 반복계약 부재, one-off stockpile         |
| `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE`   |      16 |         15 |          8 |         11 |         8 |       0 |    5 | stockpile 반복성, 정부 예산, outbreak 정상화 |
| `PUBLIC_HEALTH_PROCUREMENT_REVERSAL`      |    gate |       gate |       gate |       gate |      gate |    gate | gate | 정부계약 취소, funding withdrawal        |
| `DIAGNOSTICS_INFECTIOUS_EVENT`            |      19 |          5 |          5 |          5 |         5 |       0 |    5 | one-off demand, 검사 수요 급감           |
| `SPECULATIVE_SCIENCE_THEME`               |       5 |          4 |          5 |          5 |         5 |       0 |    3 | 재현 실패, 상용화 부재, 논문·테마만 있음           |
| `ADVANCED_MATERIAL_SPECULATIVE_THEME`     |       7 |          6 |          6 |          8 |         6 |       0 |    3 | 실제 제품·고객·매출 부재                     |
| `POLICY_LOCAL_THEME`                      |       5 |          5 |          5 |          8 |         5 |       0 |    3 | 정책 의존, 예산·계약 부재                    |
| `INDUSTRIAL_POLICY_TARIFF_EVENT`          |      10 |         10 |          8 |         10 |         7 |       0 |    5 | 관세 반전, 수입규제, 수혜·피해 동시 발생           |
| `POLICY_MARKET_SHOCK_EVENT`               |    gate |       gate |       gate |       gate |      gate |    gate | gate | 세금·분배·규제 발언 shock                  |
| `ONE_OFF_EVENT_DEMAND`                    |       8 |          5 |          5 |          6 |         5 |       0 |    4 | 지속성 부족, 수요 정상화                     |
| `THEME_VALUATION_OVERHEAT`                |    gate |       gate |       gate |       gate |      gate |    gate | gate | price-only rally, 증거 없는 급등         |
| `DISCLOSURE_CONFIDENCE_CAP`               |     cap |        cap |        cap |        cap |       cap |     cap |    + | 예산·계약·수주·착공 detail 부족              |

Loop 5에서 핵심 보정은 이거다.

```text
1. CRITICAL_INFRA_RECONSTRUCTION_FINANCING을 추가.
   우크라 재건도 통신망·전력망·항만·변압기 보호시설처럼 실제 financing과 asset이 붙으면 Stage 2 후보가 된다.

2. GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE를 추가.
   Bavarian Nordic처럼 정부 stockpile 계약이 매출·EBITDA 가이던스를 올리면 단순 질병 이벤트보다 강하다.

3. PUBLIC_HEALTH_PROCUREMENT_REVERSAL을 gate로 추가.
   Moderna bird-flu funding 취소처럼 정부 조달·보조금은 정책 방향이 바뀌면 바로 4C-watch다.

4. CLIMATE_EVENT_TO_GRID_INFRA를 유지/강화.
   폭염 자체는 event지만, 전력망·VPP·plug-in battery program으로 넘어가면 다른 대섹터 구조수요로 이관 가능하다.

5. NORTH_KOREA_POLICY_EVENT은 더 보수적으로 유지.
   시설철거·군사긴장·제재 리스크가 강하기 때문이다.

6. SPECULATIVE_SCIENCE_THEME은 Red 고정.
   LK-99가 기준 반례다.

7. POLICY_MARKET_SHOCK_EVENT는 gate로 유지.
   테마 자체가 틀리지 않아도 정책 발언이 가격경로를 깨뜨릴 수 있기 때문이다.
```

---

# 9. stage date 후보

## `NORTH_KOREA_POLICY_EVENT`

```text
Stage 1:
정상회담, 관광 재개 기대, 제재 완화 뉴스

Stage 2:
실제 정부 승인, 사업 재개 계약, 제재 완화, 현금흐름 경로 확인

Stage 3:
극히 제한적. 다년 계약과 실제 매출 확인 전 금지

Stage 4B:
회담 기대만으로 관련주 동반 급등

Stage 4C:
군사 긴장, 시설 철거, 도로·철도 폭파, 제재 강화
```

## `GEOPOLITICAL_RECONSTRUCTION`

```text
Stage 1:
재건회의, 지원선언, MOU, 정책 뉴스

Stage 2:
실제 프로젝트, financing, 참여기업, 계약금액, 공사착수 확인

Stage 3:
다년 매출·마진·수주잔고가 확인된 경우만

Stage 4B:
재건 테마 동반 과열

Stage 4C:
전쟁 재격화, financing 실패, 보험·보증 부재, 착공 지연
```

## `REAL_RECONSTRUCTION_FINANCING`

```text
Stage 1:
재건 필요성, 국제기구 지원 의향, MOU

Stage 2:
EBRD/IFC/정부기관 financing, guarantee, 운영회사, 실제 자산 확인

Stage 3:
개별 기업의 수주·매출·마진·현금흐름으로 연결될 때

Stage 4B:
financing 사례 하나를 전체 재건 테마로 과잉 일반화

Stage 4C:
financing 지연, 전쟁 재격화, 보증 부재, 프로젝트 취소
```

## `CRITICAL_INFRA_RECONSTRUCTION_FINANCING`

```text
Stage 1:
전력망·항만·통신망 복구 필요성, 국제기구 지원 뉴스

Stage 2:
concession, financing, guarantee, transformer shelter, renewable capacity, operating asset 확인

Stage 3:
개별 기업의 장기 수주·운영매출·마진이 확인될 때

Stage 4B:
critical infra 재건 뉴스만으로 관련주 동반 과열

Stage 4C:
공습·보험·보증 실패, project delay, concession 취소, financing failure
```

## `CLIMATE_DISASTER_EVENT`

```text
Stage 1:
폭염·한파·황사·산불·홍수 뉴스

Stage 2:
전력망 투자, 냉각 수주, 수요반응/VPP 계약, 복구 계약, 실제 제품 판매 확인

Stage 3:
반복 수요와 구조적 설비투자로 연결될 때만

Stage 4B:
계절성 테마 급등

Stage 4C:
수요 정상화, 기상 이벤트 소멸, 재고 증가
```

## `CLIMATE_EVENT_TO_GRID_INFRA`

```text
Stage 1:
폭염·냉각 수요·전력피크 이슈 발생

Stage 2:
VPP, plug-in battery, ESS, grid response program, 냉각 인프라 계약 확인

Stage 3:
파일럿이 반복 매출·grid service revenue·설비투자로 확장될 때

Stage 4B:
폭염 뉴스만으로 전력·ESS·냉각주 무차별 급등

Stage 4C:
파일럿 종료, 예산 지연, 수요 정상화, 후속 계약 부재
```

## `EVENT_DISEASE_PEST_DEMAND`

```text
Stage 1:
WHO emergency, outbreak, 정부 방역 강화 뉴스

Stage 2:
정부 주문, stockpile 계약, 매출 가이던스 상향 확인

Stage 3:
반복 조달·상시 수요가 확인된 경우만

Stage 4B:
전염병 뉴스 후 관련주 동반 과열

Stage 4C:
outbreak 정상화, 정부 구매 종료, 수요 급감
```

## `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE`

```text
Stage 1:
질병·재난·안보성 비축 필요성 발생

Stage 2:
정부 stockpile 계약, 계약금액, 조달기관, 매출·EBITDA 가이던스 상향 확인

Stage 3:
반복 조달과 FCF가 확인될 때

Stage 4B:
stockpile 계약 하나를 전체 테마로 과잉 일반화

Stage 4C:
계약 종료, 조달 취소, funding withdrawal, 수요 정상화
```

## `PUBLIC_HEALTH_PROCUREMENT_REVERSAL`

```text
Stage 1:
정부 보조금·BARDA·CEPI·stockpile funding 발표

Stage 2:
계약금액, 임상 단계, 생산능력, 조달 일정 확인

Stage 3:
반복 조달·상업화·FCF 전환 전까지 제한

Stage 4B:
질병 리스크와 정부 funding 기대 과열

Stage 4C:
정부계약 취소, funding withdrawal, 임상 지연, procurement policy reversal
```

## `DIAGNOSTICS_INFECTIOUS_EVENT`

```text
Stage 1:
검사 수요 급증, outbreak, 진단키트 승인·수출 뉴스

Stage 2:
실제 검사 매출·정부 주문·설치기반 확대 확인

Stage 3:
전염병 one-off를 넘은 반복 진단 플랫폼이 확인될 때만

Stage 4B:
진단키트 관련주 급등

Stage 4C:
검사 수요 급감, 재고 증가, 진단 매출 감소
```

## `SPECULATIVE_SCIENCE_THEME`

```text
Stage 1:
preprint, 논문, 영상, SNS, 학회 발표

Stage 2:
독립 재현, peer-reviewed validation, 고객사 테스트, 계약 확인

Stage 3:
상용 고객 + 반복 매출 + EPS/FCF 전환 전까지 금지

Stage 4B:
논문·SNS만으로 관련주 급등

Stage 4C:
재현 실패, 상용화 실패, 불순물 설명, 거래소 투자경고
```

## `POLICY_MARKET_SHOCK_EVENT`

```text
Stage 1:
세금·분배·규제·산업정책 발언 발생

Stage 2:
실제 법안, 예산안, 세율, 규제 초안 확인

Stage 3:
개별 기업 EPS/FCF에 구조적으로 반영될 때만

Stage 4B:
crowded rally에서 정책 리스크를 시장이 무시

Stage 4C:
지수 급락, sector risk premium 상승, 세금·규제 실제화
```

---

# 10. 가격경로 검증계획

## R11 Loop 5 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. stage1 event 발생일의 종가를 저장한다.
3. MFE_5D / 20D / 60D / 90D / 180D를 계산한다.
4. MAE_5D / 20D / 60D / 90D / 180D를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 실제 계약·예산·정부 주문·매출·EPS evidence가 있는지 확인한다.
7. 없으면 price_moved_without_evidence 또는 event_premium으로 분류한다.
```

## Loop 5에서 새로 강제할 판정

```text
EVENT_PREMIUM:
뉴스로 주가가 올랐지만 실제 매출·계약 없음.

EVENT_TO_CONTRACT:
이벤트가 실제 정부계약·stockpile·financing·공사착수로 이어짐.

GOVERNMENT_STOCKPILE_GUIDANCE_ALIGNED:
정부 stockpile 계약이 매출·EBITDA 가이던스를 실제로 올림.

PROCUREMENT_REVERSAL_4C:
정부계약·funding이 취소되거나 정책방향이 바뀜.

REAL_RECONSTRUCTION_FINANCING:
재건 테마가 국제기구 financing·보증·운영회사·자산으로 구체화됨.

CRITICAL_INFRA_FINANCING_ALIGNED:
전력망·통신망·항만·transformer shelter 같은 critical infra financing 확인.

EVENT_TO_INFRA_CROSSOVER:
폭염·재난 이벤트가 전력망·냉각·VPP·ESS 등 다른 대섹터 구조수요로 넘어감.

PRICE_MOVED_WITHOUT_EVIDENCE:
정책·SNS·논문만으로 주가가 움직임.

SPECULATIVE_SCIENCE_FAILURE:
재현 실패 또는 상용화 부재로 thesis break.

ONE_OFF_REVENUE:
매출은 있었지만 다음 해 수요 정상화.

POLICY_RELIEF_ONLY:
정책은 있었지만 예산·계약·공사 없음.

POLICY_MARKET_SHOCK:
정책 발언·세금·분배 이슈가 가격경로를 급격히 훼손.

NORTH_KOREA_HARD_RED:
남북관계 악화·제재·시설철거로 thesis break.

DISCLOSURE_CONFIDENCE_CAPPED:
예산·계약·수주·공사착수 detail 부족으로 Stage 3 제한.
```

## 이번 R11 Loop 5에서 우선 검증할 가격 case

| case_id                                      |    stage2 후보일 | 현재 1차 가격판정                                        |
| -------------------------------------------- | ------------: | ------------------------------------------------- |
| `bavarian_nordic_us_stockpile_contract_case` |    2026-05-11 | 정부계약 + 가이던스 상향, event-to-contract                 |
| `moderna_cepi_bird_flu_funding_case`         |    2025-12-18 | CEPI funding, public health procurement Stage 2   |
| `moderna_barda_contract_cancel_case`         |    2025-05-29 | government funding withdrawal 4C-watch            |
| `ukraine_telecom_ebrd_ifc_case`              |    2024-10-10 | $435m financing, reconstruction Stage 2 reference |
| `ukraine_ebrd_power_port_concession_case`    |    2026-05-15 | critical infra financing reference                |
| `north_korea_kumgang_dismantle_case`         |    2025-02-13 | 남북경협 hard Red                                     |
| `lk99_superconductor_no_replication_case`    |       2023-08 | speculative science failure                       |
| `lk99_cu2s_impurity_case`                    |       2023-11 | impurity explanation, hard 4C                     |
| `abbott_diagnostics_demand_wane_case`        |    2025-10-15 | diagnostics one-off normalization                 |
| `heatwave_ac_grid_stress_case`               | 2025-07 study | climate event → grid/VPP watch                    |
| `nyc_ac_battery_vpp_case`                    |       2026-05 | heatwave demand-response Stage 2 reference        |
| `ai_citizen_dividend_policy_shock_case`      |    2026-05-12 | KOSPI intraday -5.1%, close -2.3%, policy shock   |
| `china_group_visa_tourism_policy_case`       |    2025-08~09 | tourism policy Stage 1, spend 확인 전                |
| `yellow_dust_mask_event_case`                |         case별 | one-off demand                                    |
| `disaster_rebuild_material_case`             |         case별 | 실제 계약 전 Event/Watch                               |
| `policy_local_theme_case`                    |         case별 | 예산·계약 전 Green 금지                                  |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R11 Loop 5에서는 아래 필드를 채우게 해야 한다.

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

MFE_5D
MFE_20D
MFE_60D
MFE_90D
MFE_180D

MAE_5D
MAE_20D
MAE_60D
MAE_90D
MAE_180D

drawdown_after_peak
below_stage1_price_flag
below_stage2_price_flag
below_stage3_price_flag

event_type
policy_event_flag
geopolitical_event_flag
disaster_event_flag
climate_event_flag
disease_event_flag
science_preprint_flag
social_media_theme_flag

actual_contract_flag
contract_value
contract_duration_months
government_order_flag
stockpile_contract_flag
vaccine_order_doses
vaccine_stockpile_flag
public_procurement_agency
procurement_reversal_flag
government_funding_cancelled_flag
funding_withdrawal_amount
clinical_development_delay_flag

project_financing_flag
financing_amount
guarantee_structure_flag
operating_company_flag
infrastructure_asset_flag
critical_infra_flag
telecom_infra_flag
power_grid_infra_flag
port_concession_flag
transformer_shelter_flag
renewable_capacity_mw
budget_allocated_flag
construction_started_flag
revenue_recognized_flag
guidance_raised_flag
ebitda_margin_guidance_change

outbreak_status
who_emergency_flag
government_purchase_amount
diagnostic_sales_change
demand_normalization_flag
inventory_build_flag

replication_success_flag
replication_failure_flag
peer_review_status
commercial_product_flag
customer_contract_flag
impurity_explanation_flag

sanctions_status
military_tension_flag
tourism_reopen_flag
facility_dismantle_flag
road_rail_destroyed_flag
hostile_state_rhetoric_flag

rebuild_project_count
rebuild_budget_amount
insurance_payout_status
one_off_demand_flag

heatwave_event_flag
peak_load_increase_estimate
grid_stress_flag
vpp_program_flag
battery_program_capacity
battery_program_households
cooling_order_flag
energy_system_investment_flag

policy_budget_flag
local_policy_flag
regional_development_contract_flag
visa_policy_event_flag
tourist_arrivals_after_policy
average_spend_after_policy
casino_drop_after_policy
duty_free_sales_after_policy

tax_policy_event_flag
windfall_tax_comment_flag
citizen_dividend_comment_flag
corporate_tax_uncertainty_flag
market_wide_selloff_flag
government_clarification_flag

event_premium_flag
price_moved_without_evidence_flag
one_off_revenue_flag
policy_relief_only_flag
north_korea_hard_red_flag
speculative_science_failure_flag
event_to_contract_flag
event_to_infra_crossover_flag
critical_infra_financing_flag
government_stockpile_guidance_aligned_flag
procurement_reversal_4c_flag
disclosure_confidence_capped_flag

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

# R11 Loop 5 결론

이번 5회차에서 R11은 더 좁혀졌다.

```text
Green 가능성이 매우 제한적으로 생기는 경우:
전염병 이벤트가 실제 정부 stockpile 계약과 가이던스 상향으로 연결되는 경우
우크라 재건이 실제 financing·참여기업·인프라 자산으로 연결되는 경우
전력망·통신망·항만·transformer shelter 같은 critical infra financing이 확인되는 경우
폭염·재난 이벤트가 전력망·냉각·VPP·ESS 같은 구조수요로 승격되는 경우
정책 발표가 실제 예산·계약·공사착수·매출 인식으로 연결되는 경우

Watch:
우크라 재건
폭염·전력망
재난복구
동물·전염병 stockpile
탄소·기후 적응 인프라
정책 지역 테마 중 예산이 붙은 경우
관광·비자 정책 중 실제 spend가 확인되는 경우

Event/Red:
남북경협
금강산·개성공단
황사·마스크
진단키트 one-off
빈대·엠폭스 뉴스만 있는 종목
세종시·지역정책 발표만 있는 종목
정책 코멘트만 있는 테마
초전도체·맥신·그래핀 등 재현 전 과학 테마

Hard 4C:
남북관계 악화·시설철거
LK-99식 재현 실패
전염병 검사 수요 정상화
정부 구매 종료
정부계약 취소·funding withdrawal
재건 financing 실패
기후·재난 수요 one-off
세금·분배·규제 정책 shock으로 인한 price-path break
예산·계약·수주·공사착수 detail 부족으로 인한 disclosure confidence cap
```

**R11 Loop 5 점수정규화의 핵심 문장:**

> 정책·지정학·재난·이벤트는 “뉴스가 크다”가 아니라 **실제 계약, 예산, 정부 주문, financing, 공사착수, 반복 매출, EPS/FCF 전환**으로 봐야 한다.
> Loop 5부터는 특히 `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE`, `PUBLIC_HEALTH_PROCUREMENT_REVERSAL`, `CRITICAL_INFRA_RECONSTRUCTION_FINANCING`, `CLIMATE_EVENT_TO_GRID_INFRA`, `SPECULATIVE_SCIENCE_THEME`, `POLICY_MARKET_SHOCK_EVENT`, `DISCLOSURE_CONFIDENCE_CAP`을 강한 보정축으로 넣어야 한다.

다음 순서는 **R12 — 농업·생활서비스·기타 Loop 5**다.

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/denmarks-bavarian-nordic-raises-2026-forecast-2026-05-11/?utm_source=chatgpt.com "Bavarian Nordic raises 2026 forecast on additional US vaccine contract"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/moderna-secures-up-543-million-funding-bird-flu-vaccine-global-coalition-2025-12-18/?utm_source=chatgpt.com "Moderna secures up to $54.3 million funding for bird flu vaccine from global coalition"
[3]: https://www.reuters.com/world/uk/ebrd-ifc-provide-435-mln-ukraines-newly-merged-telecoms-firm-2024-10-10/?utm_source=chatgpt.com "EBRD and IFC to provide $435 mln for Ukraine's newly merged telecoms firm"
[4]: https://www.reuters.com/sustainability/climate-energy/ebrd-backs-privatisation-efforts-ukraine-could-provide-funding-2026-05-15/?utm_source=chatgpt.com "EBRD backs privatisation efforts in Ukraine, could provide funding"
[5]: https://arxiv.org/abs/2507.13534?utm_source=chatgpt.com "The impact of heatwave-driven air conditioning adoption on electricity demand: A spatio-temporal case study for Germany"
[6]: https://apnews.com/article/26ebb0eafe344a661bf722a99a070371?utm_source=chatgpt.com "Air conditioning battery program for renters could help cities manage grid stress during heat waves"
[7]: https://www.reuters.com/world/asia-pacific/north-korea-dismantling-facility-near-border-separated-families-seoul-says-2025-02-13/?utm_source=chatgpt.com "North Korea dismantling facility near border for separated families, Seoul says"
[8]: https://arxiv.org/abs/2308.03544?utm_source=chatgpt.com "Absence of superconductivity in LK-99 at ambient conditions"
[9]: https://www.reuters.com/business/healthcare-pharmaceuticals/abbott-posts-higher-quarterly-revenue-strong-medical-device-demand-2025-10-15/?utm_source=chatgpt.com "Abbott revenue falls short of estimates on weak demand for diagnostic devices"
[10]: https://www.marketwatch.com/story/the-hottest-stock-market-in-the-world-finally-met-its-match-taxes-55cf54c6?utm_source=chatgpt.com "The hottest stock market in the world finally met its match: taxes"
[11]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/?utm_source=chatgpt.com "South Korea to offer visa-free entry to Chinese tourists from late September"
[12]: https://apnews.com/article/ca14251649cf6a065342196a8b021f92?utm_source=chatgpt.com "Trump administration cancels $766 million Moderna contract to fight pandemic flu"
