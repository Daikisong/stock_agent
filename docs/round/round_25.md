좋아. **Round 19: 얇은 archetype + 주요 archetype 점수비중 v1.0 보강**으로 계속 진행할게.

이번 라운드의 기준은 이거야.

```text
성공사례가 많을수록:
→ 어떤 증거에 가중치를 줘야 하는지 선명해짐

반례가 많을수록:
→ 어떤 조건에서 Green을 막아야 하는지 선명해짐

주가검증이 붙으면:
→ 그 점수비중이 실제 시장에서 맞았는지 확인 가능
```

기본 정신은 그대로 유지해야 해. 에이전트는 테마봇이 아니라, **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**을 찾는 시스템이야.
그리고 실제 점수는 테마명에서 나오면 안 돼. 계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 필드는 실제 공시·리포트에서 확인될 때만 써야 하고, 없는 값은 절대 만들어 넣으면 안 된다.

---

# 1. AI_DATA_CENTER_COOLING / AI_DATA_CENTER_INFRASTRUCTURE

## 핵심 구조

```text
AI 서버 고밀도화
→ 발열·전력 밀도 상승
→ 액체냉각 / HVAC / 전력망 / ESS / PCB 병목
→ 데이터센터 CAPEX와 동행
→ 수주·납품·서비스 매출
```

## 성공사례 후보

Ecolab의 CoolIT 인수는 AI 데이터센터 냉각이 별도 sub-archetype으로 분리되어야 한다는 강한 근거야. Ecolab은 CoolIT Systems를 약 47.5억 달러에 인수하기로 했고, Reuters는 AI 인프라 투자 증가로 공랭에서 고밀도 전력부하를 처리할 수 있는 액체냉각으로 이동하고 있다고 설명했다. CoolIT은 Nvidia·AMD 같은 주요 칩메이커에 냉각 시스템을 공급하는 업체로 보도됐다. ([Reuters][1])

여기서 점수화 핵심은 “냉각 테마”가 아니라:

```text
실제 고객사
실제 수주/납품
데이터센터 CAPEX와 직접 연결
냉각 병목 지위
반복 서비스·모니터링 매출
FY1/FY2 OP 상향
```

이야.

## 반례

```text
- 액침냉각 테마만 있고 실제 고객·납품 없음
- 데이터센터 CAPEX 지연
- HVAC 매출은 있으나 AI 데이터센터 exposure가 작은 기업
- 수주는 있으나 저마진 설비 납품에 그치는 기업
- AI CAPEX cut 발생
```

## 점수비중 v1.0

```text
EPS/FCF: 21
Structural Visibility: 22
Bottleneck/Pricing: 22
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: AI_capex_delay / project_margin / customer_concentration
```

## 정규화 교정

AI 냉각은 **Green 가능 archetype**으로 올려도 된다.
다만 Green 조건은 빡세다.

```text
Green 가능:
고객사 데이터센터 CAPEX와 직접 연결
+ 실제 수주/납품
+ 냉각 기술 병목
+ 서비스/유지보수 반복매출
+ OP/EPS 상향

Green 금지:
액침냉각 키워드만 있음
AI 데이터센터 관련주라고만 묶임
실제 매출 exposure 불명확
```

---

# 2. SECURITY_IDENTITY_DEEPFAKE

## 핵심 구조

```text
보안 위협 증가 / 규제 강화
→ 기업·정부 보안 지출
→ 반복 구독 또는 장기계약
→ ARR·OPM·FCF 개선
```

## 성공사례 후보

성공 쪽은 실제 반복 보안 계약, 낮은 churn, 고객 다변화, ARR 증가가 있는 기업이야. 딥페이크, 생체인식, CCTV, IT보안은 모두 이 archetype에 들어갈 수 있지만, **공공·기업 계약과 반복매출이 확인되기 전까지는 Watch**다.

## 강한 반례: CrowdStrike

CrowdStrike는 반드시 case library에 넣어야 하는 반례야. 구조적 사이버보안 수요가 강해도, 2024년 faulty software update로 글로벌 장애가 발생했고, Reuters는 이 사건이 800만 대 이상 컴퓨터에 영향을 주었으며 CrowdStrike 주가가 12일간 32% 하락해 약 250억 달러 시총이 사라졌다고 보도했다. ([Reuters][2])

이 반례가 주는 교훈은 아주 중요해.

```text
보안 SaaS는 반복매출이 있어도
운영 신뢰도 / 업데이트 안정성 / 고객 피해 / 소송 리스크가 깨지면
바로 4C다.
```

## 점수비중 v1.0

```text
EPS/FCF: 20
Structural Visibility: 20
Bottleneck/Pricing: 10
Market Mispricing: 14
Valuation Rerating: 13
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: operational_trust / outage / legal / customer_retention
```

## 정규화 교정

보안은 Green 가능성이 있지만, `operational_trust`를 강한 gate로 넣어야 한다.

```text
Green 조건:
반복 구독 매출
+ 낮은 churn
+ 고객 다변화
+ OPM 개선
+ 대형 장애/소송 리스크 부재

4C 조건:
대형 장애
고객 소송
보안 신뢰 훼손
갱신율 하락
```

---

# 3. CRO_CLINICAL_SERVICE

## 핵심 구조

```text
제약·바이오 R&D 증가
→ 임상시험 수탁
→ 반복 서비스 매출
→ 고객사 다변화
→ OP/FCF 개선
```

## 성공사례 후보

CRO는 pre-revenue biotech보다 훨씬 점수화하기 좋다. 실제 서비스 매출, backlog, 고객사 다변화가 있기 때문이야. 하지만 CDMO보다는 funding cycle에 더 민감하다.

## 강한 반례: Charles River

Charles River Laboratories는 CRO/바이오서비스의 핵심 반례다. Reuters는 Charles River가 바이오 고객사의 funding crunch가 지속되면서 2024년 전망을 낮췄고, 이 소식에 주가가 premarket에서 15% 하락했다고 보도했다. 이 사례는 CRO가 반복 서비스처럼 보여도 **바이오 funding cycle과 고객사 R&D 예산이 꺾이면 4C로 가야 한다**는 걸 보여준다. ([Reuters][3])

## 점수비중 v1.0

```text
EPS/FCF: 18
Structural Visibility: 20
Bottleneck/Pricing: 8
Market Mispricing: 12
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: biotech_funding_cycle / customer_concentration / backlog_quality
```

## 정규화 교정

CRO는 이렇게 봐야 해.

```text
CDMO:
장기 생산계약 + capacity + 가동률
→ Green 가능성이 더 높음

CRO:
수주잔고 + 고객사 다변화 + R&D funding cycle
→ Watch-to-Green

Pre-revenue biotech:
임상 뉴스만으로 Green 금지
```

Green 조건:

```text
수주잔고 증가
고객사 다변화
매출/OP 증가
R&D funding cycle 안정
고마진 서비스 mix
```

---

# 4. SOLAR_TARIFF_SUPPLYCHAIN

## 핵심 구조

```text
정책·보조금·관세
→ 생산시설·부품 공급망
→ 가동률·마진
→ OP/FCF 전환
```

## 성공후보와 반례: Qcells

Qcells/Hanwha Solutions는 태양광 supply chain archetype의 좋은 검증 케이스야. 미국 내 대규모 태양광 생산 투자를 진행 중인 것은 Stage 1~2 후보 신호지만, AP는 미국 세관이 중국 강제노동방지법 관련으로 Qcells 공장의 핵심 부품 수입을 억류하면서 약 1,000명의 노동자 근무시간·임금을 줄이고 300명의 계약직을 해고했다고 보도했다. ([AP News][4])

이건 태양광의 핵심 반례를 정확히 보여줘.

```text
정책 수혜가 있어도
부품 공급망 / 관세 / 통관 / 보조금 리스크가 있으면
가동률과 FCF가 바로 깨질 수 있다.
```

## 점수비중 v1.0

```text
EPS/FCF: 18
Structural Visibility: 17
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation Rerating: 10
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: tariff / customs / subsidy / supply_chain
```

## 정규화 교정

태양광은 Green을 매우 조심해야 한다.

```text
Green 조건:
가동률 상승
+ 부품 공급 안정
+ 관세 리스크 낮음
+ OP/FCF 개선
+ 고객사 또는 장기 수요 확인

4C 조건:
부품 억류
관세/통관 문제
보조금 축소
가동률 하락
```

---

# 5. RETAIL_ECOMMERCE_LOGISTICS

## 핵심 구조

```text
물류망 / 점포망 / PB상품
→ same-store sales
→ 물류비·재고 통제
→ OPM / FCF 개선
```

## 성공 후보

```text
- 편의점: PB mix, 점포 효율, OPM 개선
- 콜드체인: 의약품/신선식품 반복 물류계약
- 이커머스: 물류 효율과 FCF 개선
```

## 반례 조건

```text
- 매출 성장하지만 물류비·배송비로 FCF 악화
- 홈쇼핑 구조 둔화
- 상장 기대만 있는 관련주
- 중국 직구/저가 e-commerce 압박
- 공급업체 압박·규제 리스크
- 데이터 유출·보안 리스크
```

## 점수비중 v1.0

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 5
Market Mispricing: 13
Valuation Rerating: 14
Capital Allocation: 3
Information Confidence: 5
Risk Penalty: logistics_cost / inventory / supplier_regulation / data_security
```

## 정규화 교정

유통·이커머스는 Green을 보수적으로 줘야 한다.

```text
매출 성장만 있음:
Stage 1~2

OPM 개선 + 물류비 안정 + FCF 개선:
Stage 2~3 가능

재고 증가 / 물류비 증가 / 규제 리스크:
4C 또는 RedTeam
```

---

# 6. INSURANCE_UNDERWRITING_CYCLE

## 핵심 구조

```text
손해율 안정
→ CSM / ROE 개선
→ 자본비율 안정
→ 주주환원
→ PBR-ROE 프레임 리레이팅
```

## 성공 후보

```text
- 삼성화재 / DB손보: 손해율, CSM, ROE, 자본비율, 환원
- 생명보험사: CSM, 금리, 자본비율, 배당여력
- 보증보험: 반복 보증료, 신용 리스크 관리
```

## 반례

```text
- 단순 저PBR 보험주
- 손해율 악화
- 자본비율 낮아 환원 제한
- 사이버 장애 / 랜섬웨어
- PF / 대체투자 손실
```

## 점수비중 v1.0

```text
EPS/FCF: 15
Structural Visibility: 21
Bottleneck/Pricing: 4
Market Mispricing: 15
Valuation Rerating: 25
Capital Allocation: 10
Information Confidence: 5
Risk Penalty: underwriting / capital_ratio / cyber_operational / credit_cost
```

## 정규화 교정

보험은 EPS 폭발형이 아니라 **PBR-ROE-환원 리레이팅형**이다.

```text
Green 조건:
ROE 개선
+ CSM 또는 손해율 안정
+ 자본비율 안정
+ 실제 배당·자사주
+ credit/cyber risk 낮음
```

---

# 7. DIGITAL_HEALTHCARE_AI

## 핵심 구조

```text
임상 문제
→ AI 진단·판독·문서화 솔루션
→ 병원 도입
→ 수가·보험·반복 사용
→ 매출/FCF 전환
```

## 성공 후보

```text
- 의료영상 AI
- 병원 workflow AI
- 임상문서화 AI
- 유전체검사·정밀의료 플랫폼
```

## 반례

```text
- 논문 성능은 좋지만 병원 매출 없음
- 수가/보험 없음
- 병원 workflow 도입 실패
- 오진·책임소재 리스크
- 규제 승인 지연
```

## 점수비중 v1.0

```text
EPS/FCF: 18
Structural Visibility: 17
Bottleneck/Pricing: 8
Market Mispricing: 13
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 7
Risk Penalty: regulation / reimbursement / clinical_validation / liability
```

## 정규화 교정

의료AI는 **Watch-to-Green**이다.

```text
Green 조건:
외부 임상 검증
+ 규제 승인
+ 병원 도입
+ 수가·보험 또는 반복 과금
+ 매출/OP 전환

Green 금지:
논문
PoC
AI 키워드
병원 파일럿만 있음
```

---

# 8. BATTERY_RECYCLING_ESS_SHIFT

## 핵심 구조

```text
EV 성장 기대
→ 소재/부품/CAPA 투자
→ EV 수요 둔화·광물가격·CAPA 과잉 리스크
→ ESS 전환이 일부 보완 가능
```

## 성공후보와 반례

ESS 전환은 새로운 후보가 될 수 있지만, EV 수요 둔화는 여전히 4C 리스크다. 배터리/ESS/폐배터리 쪽은 **성장 테마와 CAPEX 과잉 리스크가 동시에 존재**하기 때문에 Green을 제한해야 한다.

## 점수비중 v1.0

```text
EPS/FCF: 20
Structural Visibility: 16
Bottleneck/Pricing: 14
Market Mispricing: 10
Valuation Rerating: 10
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: EV_demand / mineral_price / capex_overbuild / policy
```

## 정규화 교정

```text
Stage 2 가능:
실제 ESS 수요
고객사 계약
가동률 개선
FCF 훼손 없는 CAPEX

Stage 3 제한:
장기계약 + 가격전가 + 수요지속 + valuation 여지

4C:
EV 수요 둔화
광물가격 하락
CAPA 과잉
margin compression
```

2차전지는 Green보다 **과열 방어와 4B/4C 감지**가 더 중요하다.

---

# 9. SECURITIES_BROKERAGE_CYCLE

## 핵심 구조

```text
거래대금 증가
→ 브로커리지 수수료 증가
→ IPO/IB 회복
→ 자기자본 운용성과
→ ROE 개선
```

## 성공 후보

```text
- 거래대금 증가와 브로커리지 수익 증가가 확인되는 증권사
- IPO·ECM·DCM pipeline 회복 증권사
- PF 리스크 낮고 자본비율 안정적인 대형 증권사
- VC 회수시장 회복 기업
```

## 반례

```text
- 거래대금 단기 급증 후 소멸
- 부동산 PF/대체투자 손실
- 자기자본 운용손실
- IPO 회복 기대만 있고 실적 없음
- VC 회수시장 막힘
```

## 점수비중 v1.0

```text
EPS/FCF: 18
Structural Visibility: 14
Bottleneck/Pricing: 5
Market Mispricing: 15
Valuation Rerating: 18
Capital Allocation: 8
Information Confidence: 5
Risk Penalty: market_turnover / PF / proprietary_loss / IPO_cycle
```

## 정규화 교정

증권사는 은행·보험보다 훨씬 사이클성이 강하다.

```text
Stage 1:
거래대금 증가, 증시 랠리, IPO 기대

Stage 2:
브로커리지 수익 증가, IB fee 증가, OP/EPS 상향

Stage 3:
반복적 시장활동 회복 + PF 리스크 낮음 + ROE 구조 개선

4C:
거래대금 급감, PF 손실, 자기자본 운용손실
```

Green보다 Watch 중심으로 둔다.

---

# 10. MEMORY_HBM_CAPACITY — 4B 보정 계속 강화

## 핵심 구조

```text
AI 수요
→ HBM/DRAM/NAND 병목
→ 장기계약·선수금·가격밴드
→ EPS/FCF 다년 상향
→ 시클리컬 할인 제거
```

SK하이닉스는 구조적 성공사례이면서, 동시에 4B-watch의 기준 사례다. AI 수요로 2025년 274%, 2026년 200% 이상 주가가 상승하고 시총 1조 달러에 접근했다는 보도는 리레이팅 성공 이후에도 crowding·valuation saturation을 감시해야 한다는 근거다. ([Reuters][5])

## 점수비중 v1.0

```text
EPS/FCF: 24
Structural Visibility: 21
Bottleneck/Pricing: 19
Market Mispricing: 15
Valuation Rerating: 12
Capital Allocation: 0
Information Confidence: 5
Risk Penalty: cycle / capex_reversal / crowding
```

## 4B-watch 조건

```text
주가 1~2년 급등
시총/멀티플 포화
고객사 가격 저항
CAPEX 증설 뉴스
모두가 AI memory rerating을 인정
글로벌 자금 crowded
```

HBM은 Green 가능성이 높지만, 성공 후에는 4B-watch가 반드시 필요하다.

---

# Round 19 점수비중 요약표

| Archetype                    | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | 핵심 리스크                   |
| ---------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ------------------------ |
| AI_DATA_CENTER_COOLING       |      21 |         22 |         22 |         13 |        12 |       0 | AI CAPEX 지연, 저마진 프로젝트    |
| SECURITY_IDENTITY_DEEPFAKE   |      20 |         20 |         10 |         14 |        13 |       0 | 장애, 소송, 신뢰도              |
| CRO_CLINICAL_SERVICE         |      18 |         20 |          8 |         12 |        12 |       0 | 바이오 funding cycle        |
| SOLAR_TARIFF_SUPPLYCHAIN     |      18 |         17 |         12 |         12 |        10 |       0 | 관세, 통관, 보조금              |
| RETAIL_ECOMMERCE_LOGISTICS   |      18 |         16 |          5 |         13 |        14 |       3 | 물류비, 재고, 규제              |
| INSURANCE_UNDERWRITING_CYCLE |      15 |         21 |          4 |         15 |        25 |      10 | 손해율, 자본비율                |
| DIGITAL_HEALTHCARE_AI        |      18 |         17 |          8 |         13 |        12 |       0 | 허가, 수가, 책임소재             |
| BATTERY_RECYCLING_ESS_SHIFT  |      20 |         16 |         14 |         10 |        10 |       0 | EV 수요, CAPA 과잉           |
| SECURITIES_BROKERAGE_CYCLE   |      18 |         14 |          5 |         15 |        18 |       8 | 거래대금, PF, IB cycle       |
| MEMORY_HBM_CAPACITY          |      24 |         21 |         19 |         15 |        12 |       0 | CAPEX reversal, crowding |

---

# cases_v07 추가 후보

```text
AI_DATA_CENTER_COOLING:
- ecolab_coolit_ai_liquid_cooling_candidate
- liquid_cooling_theme_no_order_counterexample
- ai_capex_delay_cooling_4c
- low_margin_hvac_project_counterexample

SECURITY_IDENTITY_DEEPFAKE:
- recurring_security_subscription_candidate
- crowdstrike_outage_4c
- deepfake_regulation_stage1_candidate
- security_theme_no_contract_counterexample

CRO_CLINICAL_SERVICE:
- cro_revenue_backlog_candidate
- charles_river_funding_crunch_4c
- biotech_customer_budget_cut_counterexample
- cro_customer_diversification_success_candidate

SOLAR_TARIFF_SUPPLYCHAIN:
- qcells_us_supply_chain_candidate
- qcells_customs_detention_4c
- solar_subsidy_dependency_counterexample
- solar_component_tariff_risk

RETAIL_ECOMMERCE_LOGISTICS:
- convenience_store_pb_efficiency_candidate
- ecommerce_logistics_scale_candidate
- ecommerce_fresh_loss_counterexample
- supplier_regulation_margin_risk

INSURANCE_UNDERWRITING_CYCLE:
- samsung_fire_underwriting_valueup_candidate
- db_insurance_loss_ratio_candidate
- low_pbr_insurer_no_capital_return_counterexample
- insurance_cyber_operational_risk_4c

DIGITAL_HEALTHCARE_AI:
- medical_ai_external_validation_candidate
- medical_ai_no_reimbursement_counterexample
- hospital_ai_poC_no_revenue_counterexample
- medical_ai_liability_risk_4c

BATTERY_RECYCLING_ESS_SHIFT:
- ess_shift_candidate
- ev_demand_slowdown_4c
- battery_recycling_no_volume_counterexample
- solid_state_no_commercialization_counterexample

SECURITIES_BROKERAGE_CYCLE:
- brokerage_trading_value_rally_candidate
- securities_pf_loss_4c
- ipo_pipeline_recovery_candidate
- vc_exit_market_weakness_counterexample

MEMORY_HBM_CAPACITY:
- sk_hynix_hbm_success_case
- sk_hynix_4b_crowding_watch
- simple_dram_rebound_counterexample
- ai_capex_cut_memory_4c
```

---

# 이번 라운드 핵심 교정

```text
1. AI 냉각은 Green 가능이지만, 실제 고객·수주·서비스 매출이 필요.
2. 보안은 구조적 수요가 있지만, 대형 장애·소송은 hard 4C.
3. CRO는 pre-revenue biotech보다 강하지만, biotech funding cycle에 취약.
4. 태양광은 정책 수혜보다 관세·통관·부품 공급망 리스크가 더 중요할 수 있음.
5. 유통·이커머스는 매출 성장보다 OPM/FCF가 핵심.
6. 보험은 PBR-ROE-환원 리레이팅형. EPS 폭발형이 아님.
7. 의료AI는 논문·PoC가 아니라 허가·수가·병원 도입·매출화가 필요.
8. 배터리 ESS/폐배터리는 후보지만, EV 수요 둔화와 CAPA 과잉 때문에 Green 제한.
9. 증권사는 거래대금/IB cycle이라 Watch 중심.
10. HBM은 Green 가능성이 높지만, 성공 후 4B-watch를 반드시 켜야 함.
```

---

# 현재 판단

지금까지 상당히 많이 채워졌고, 이제 점수비중도 꽤 정교해졌다.
하지만 여전히 production scoring 적용 전에는 반드시 아래가 필요하다.

```text
1. cases_v07까지 case library 반영
2. 각 case stage date 후보 설정
3. 가격 path backfill
4. MFE/MAE/drawdown 계산
5. shadow scoring
6. score-price alignment 확인
7. 틀린 archetype 점수비중 재교정
```

즉 지금은 **정규화 가설을 굉장히 많이 쌓은 상태**고, 다음부터는 이 가설이 실제 주가 경로와 맞는지 검증하는 단계로 넘어가야 한다.

[1]: https://www.reuters.com/business/ecolab-acquire-coolit-systems-475-billion-2026-03-20/?utm_source=chatgpt.com "Ecolab to buy CoolIT for $4.75 billion to tap into AI data center boom"
[2]: https://www.reuters.com/legal/crowdstrike-is-sued-by-shareholders-over-huge-software-outage-2024-07-31/?utm_source=chatgpt.com "CrowdStrike is sued by shareholders over huge software outage"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/charles-river-cuts-2024-forecast-funding-crunch-among-biotech-clients-persists-2024-08-07/?utm_source=chatgpt.com "Charles River cuts 2024 forecast as funding crunch among biotech clients persists"
[4]: https://apnews.com/article/f49d0579e0584d689f1feec36ff16ad1?utm_source=chatgpt.com "South Korean solar firm cuts pay and hours for Georgia workers as US officials detain imports"
[5]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
