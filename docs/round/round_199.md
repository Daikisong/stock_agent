좋아. 순서상 이번은 **R8 Loop 7 — 플랫폼·콘텐츠·SW·보안 가격경로 검증 라운드**로 진행한다.

이번 R8은 `AI 기능 출시`, `게임 신작`, `K-pop IP`, `플랫폼 MAU`, `웹툰 IPO`, `보안 수요` 같은 말이 주가를 먼저 밀 수 있는 섹터야. 그래서 Stage 3는 꽤 엄격해야 한다. **AI·콘텐츠·플랫폼이라는 이름이 아니라 ARR, 반복매출, bookings, billings, paid usage, OPM/FCF, 운영신뢰도, 법적 리스크 통과가 확인되어야 한다.**

---

# 1. 이번 라운드 대섹터

```text
R8 = 플랫폼·콘텐츠·SW·보안
large_sector = PLATFORM_CONTENT_SW_SECURITY
round = R8 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R8의 기본 영역은 플랫폼, SaaS, 클라우드, AI application software, contact-center AI, kiosk, 게임/IP, 미디어/광고, 보안, 딥페이크, 생성AI IP risk다. Round 40 기준 R8 validation focus는 `arr`, `opm`, `fcf`, `churn`, `paid_usage`, `ip_monetization`, `privacy_security_incident`로 잡혀 있다. 

Round 119 기준으로 R8에서 부족한 증거는 `ai_feature`, `mau_growth`이고, 필요한 증거는 `arr`, `churn`, `arpu`, `fcf`, `operational_trust`다. Green blocker는 `outage`, `privacy_breach`, `regulatory_take_rate_damage`다. 

---

# 2. 대상 canonical archetype

```text
B2B_SAAS_ERP_WORKFLOW
CLOUD_AI_SOFTWARE_INFRA
EDGE_AI_CLOUD_INFRASTRUCTURE
AI_SOFTWARE_APPLICATION
ENTERPRISE_AI_ONTOLOGY_WORKFLOW
PLATFORM_SOFTWARE_INTERNET
WEBTOON_PLATFORM_IP_MONETIZATION
GAME_CONTENT_IP
GAME_CONTENT_IP_REPEAT_MONETIZATION
SINGLE_IP_RELEASE_EVENT_PREMIUM
AD_CONTENT_PLATFORM_GUIDANCE_RISK
KPOP_PLATFORM_CONTENT_IP
PLATFORM_GOVERNANCE_LEGAL_RISK
PLATFORM_PRIVACY_SECURITY_OVERLAY
SECURITY_OPERATIONAL_TRUST_OVERLAY
DISCLOSURE_CONFIDENCE_CAP
```

이번 R8의 핵심 질문은 이거다.

```text
이 회사는 AI·게임·콘텐츠·플랫폼 테마주인가?
아니면 반복매출, bookings, paid usage, enterprise workflow, OPM/FCF로
실제 이익 체급이 바뀌는 회사인가?
```

---

# 3. deep sub-archetype

```text
B2B SaaS / ERP:
- Douzone Bizon
- cloud ERP
- accounting / tax / compliance
- SME lock-in
- recurring revenue
- churn
- ARR proxy
- PE operational improvement

AI cloud / IT services:
- Samsung SDS
- AI infrastructure
- full-stack AI solutions
- GPU / AI infrastructure investment
- physical AI
- stablecoin optionality
- global M&A
- convertible bond / dilution watch

국산 AI / 포털:
- NAVER HyperCLOVA X
- sovereign AI
- Webtoon platform
- creator ecosystem
- MAU
- paid content
- Nasdaq Webtoon IPO
- IP monetization
- platform valuation

게임 IP:
- Krafton PUBG
- inZOI
- repeat bookings
- India expansion
- single-IP dependence
- game launch event premium
- AI-first game development
- ADK animation/IP acquisition

엔터 / K-pop IP:
- HYBE
- BTS comeback
- NewJeans / ADOR dispute
- founder legal risk
- IPO-related investigation
- artist concentration
- content IP monetization

플랫폼 governance:
- KakaoTalk / Kakao AI
- OpenAI partnership
- SM stock manipulation legal overhang
- founder litigation
- governance repair vs platform rerating
```

---

# 4. 국장 신규 후보 case

## Case A — 더존비즈온 `success_candidate / B2B SaaS ERP`

```text
symbol = 012510
archetype = B2B_SAAS_ERP_WORKFLOW / PRIVATE_EQUITY_SOFTWARE_RERATING
case_type = success_candidate
```

더존비즈온은 R8에서 가장 E2R다운 후보 중 하나다. 2025년 11월 EQT는 더존비즈온 지분 37.6%를 약 9.3억 달러에 인수하기로 했다. 더존비즈온은 중소기업 대상 클라우드 ERP, 회계, 세무, 컴플라이언스 소프트웨어를 제공하고, EQT는 장기적으로 운영 개선과 핵심 사업 강화를 추진한다고 밝혔다. 거래는 공정위 승인과 산업통상자원부 인허가 등 조건이 붙어 있다. ([Reuters][1])

### stage date 후보

```text
Stage 1:
2024~2025
- 국내 B2B SaaS / cloud ERP / AI ERP 기대
- SME lock-in 소프트웨어 rerating 기대

Stage 2:
2025-11-07
- EQT 37.6% 지분 인수 발표
- cloud ERP / accounting / tax / compliance 반복수요 확인
- PE operational improvement 기대

Stage 3:
보류
- EQT 거래 자체는 event premium 성격도 있음
- ARR, churn, OPM, FCF conversion, 고객 lock-in 확인 필요

Stage 4B:
거래 발표 후 valuation이 먼저 크게 확장됐다면 후보

Stage 4C:
거래 승인 실패, 성장 둔화, churn 상승, cloud 전환 margin 훼손 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-11-07 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
Stage 2 기준 backfill 필요.

MAE_30D / 90D / 180D / 1Y:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = private_equity_software_rerating_candidate
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

더존비즈온은 R8에서 `ARR_proxy`, `recurring_revenue`, `SME_lock_in`, `OPM_improvement`를 올려줄 수 있다. 다만 EQT 투자는 거래 이벤트이기도 하므로, Stage 3는 **거래 발표가 아니라 실적·마진·반복매출 개선 확인일**에 줘야 한다.

---

## Case B — 삼성SDS `success_candidate + 4B-watch`

```text
symbol = 018260
archetype = CLOUD_AI_SOFTWARE_INFRA / AI_CLOUD_CAPITAL_ALLOCATION
case_type = success_candidate + 4B-watch
```

삼성SDS는 R8에서 `AI cloud / enterprise IT services`를 검증하는 좋은 케이스다. 2026년 4월 KKR은 삼성SDS가 신규 발행하는 8.2억 달러 규모 전환사채를 인수하기로 했고, 주가는 장중 최대 20.8% 상승했다. KKR은 삼성SDS의 M&A, 자본배분, full-stack AI solutions 확장을 자문하고, 삼성SDS는 6.4조 원의 현금과 KKR 자금을 바탕으로 AI 인프라, AI transformation, physical AI, stablecoin 같은 신사업을 추진하겠다고 밝혔다. ([Reuters][2])

이건 Stage 2로는 강하다. 하지만 전환사채는 dilution risk도 있고, KKR 자문과 AI 인프라 투자가 실제 매출·마진·FCF로 내려오기 전에는 Stage 3-Green이 아니다.

### stage date 후보

```text
Stage 1:
2025~2026
- 기업 AI 전환
- 삼성그룹 AI infrastructure / IT services 기대

Stage 2:
2026-04-15
- KKR 8.2억 달러 전환사채 투자
- AI infrastructure / full-stack AI solutions / M&A 기대
- 주가 장중 +20.8%

Stage 3:
보류
- AI 매출, enterprise 계약, margin, recurring cloud revenue 확인 필요
- CB dilution / capital allocation quality 검증 필요

Stage 4B:
2026-04-15
- 이벤트 당일 주가 +20.8%
- AI + KKR + value-up 기대가 가격에 먼저 반영된 구간

Stage 4C:
없음
- 단, CB 희석, M&A 실패, AI 투자 대비 매출 부진, stablecoin 규제 리스크 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2026-04-15 OHLC backfill 필요.

MFE_30D / 90D / 180D:
Stage 2 기준 backfill 필요.

MAE_30D / 90D / 180D:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = event_premium + success_candidate
rerating_result = AI_cloud_capital_allocation_watch
stage_failure_type = should_not_be_green_yet
```

### 교정 포인트

삼성SDS는 `AI infrastructure investment`와 `AI revenue conversion`을 분리해야 한다. **KKR이 들어왔다**는 건 Stage 2 재료지만, Stage 3는 기업 AI 계약·매출·마진이 확인될 때다.

---

## Case C — NAVER `success_candidate / sovereign AI + Webtoon IP`

```text
symbol = 035420
archetype = PLATFORM_SOFTWARE_INTERNET / WEBTOON_PLATFORM_IP_MONETIZATION / SOVEREIGN_KOREAN_AI_MODEL
case_type = success_candidate
```

NAVER는 R8에서 플랫폼·AI·웹툰 IP가 섞인 케이스다. 2024년 6월 Naver의 Webtoon Entertainment는 미국 IPO에서 최대 26.7억 달러 valuation을 목표로 했고, Naver는 IPO 이후에도 Webtoon 지분 63.4%를 보유할 예정이었다. Webtoon은 150개국 약 1.7억 월간 활성 사용자와 2,400만 창작자를 연결하는 플랫폼으로 설명됐다. ([Reuters][3])

또 NAVER Cloud는 HyperCLOVA X THINK 계열 모델을 공개하며 한국어·영어 기반 reasoning model, 한국형 benchmark 성능, 128K context, 비전 변형 등을 제시했다. 이건 sovereign AI 관점에서 Stage 2 attention으로는 의미 있지만, NAVER 주가의 Stage 3-Green으로 바로 연결하려면 cloud/AI 매출, enterprise 계약, search/ad ARPU, margin을 확인해야 한다. ([arXiv][4])

### stage date 후보

```text
Stage 1:
2024~2025
- Webtoon IPO
- sovereign AI / HyperCLOVA X
- AI search / AI cloud 기대

Stage 2:
2024-06-17
- Webtoon IPO valuation target
- global MAU / creator ecosystem 확인

추가 Stage 2:
2026-01-03
- HyperCLOVA X 32B Think 공개
- Korean reasoning / agentic AI 역량 확인

Stage 3:
보류
- Webtoon 수익성, paid content, IP monetization
- NAVER cloud AI 매출, enterprise 계약, margin 확인 필요

Stage 4B:
Webtoon IPO / AI 모델 발표로 주가가 먼저 크게 오른 구간이 있다면 후보

Stage 4C:
광고 둔화, Webtoon valuation 하락, AI 투자비 증가, cloud margin 훼손 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2024-06-17 Webtoon IPO 관련 OHLC backfill
2026-01-03 HyperCLOVA 관련 OHLC backfill

MFE / MAE:
Stage 2 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = platform_AI_IP_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정 포인트

NAVER는 R8에서 `AI capability`와 `AI monetization`을 분리해야 한다. Webtoon MAU와 모델 성능은 Stage 2지만, Stage 3는 **AI/cloud revenue, paid content, ARPU, operating margin**이 확인되어야 한다.

---

## Case D — 카카오 `failed_rerating / governance legal recovery watch`

```text
symbol = 035720
archetype = PLATFORM_SOFTWARE_INTERNET / PLATFORM_GOVERNANCE_LEGAL_RISK
case_type = failed_rerating + governance_watch
```

카카오는 R8 플랫폼 governance의 대표 케이스다. 2025년 2월 OpenAI는 카카오와 한국에서 AI 제품을 공동 개발하기로 했고, 카카오톡 등 카카오 제품에 OpenAI 기술을 활용할 수 있다고 발표했다. 주가는 발표 직후 장 초반 9% 급등했다가 2% 하락했다고 Reuters는 보도했다. 이건 Stage 1~2 attention은 맞지만, Stage 3는 아니다. ([Reuters][5])

반면 카카오 창업자 김범수의 SM엔터 주가조작 혐의는 장기간 platform governance overhang이었다. 2025년 8월 검찰은 징역 15년을 구형했고, 2025년 10월 법원은 무죄를 선고했다. 무죄는 리스크 완화지만, 이것도 곧바로 Stage 3가 아니라 **governance overhang relief**다. ([Reuters][6])

### stage date 후보

```text
Stage 1:
2025-02-04
- OpenAI-Kakao partnership
- KakaoTalk AI product 기대

Stage 2:
보류
- partnership은 강하지만 AI 매출/ARPU/OPM 미확인

Stage 3:
없음
- AI partnership만으로 Green 금지
- 광고, commerce, subscription, AI monetization 확인 필요

Stage 4B:
2025-02-04 장초반 +9% 후 하락
- price moved ahead of monetization

Stage 4C:
2024~2025 governance overhang
- stock manipulation case
단, 2025-10-21 무죄로 hard 4C는 완화
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2025-02-04 OHLC backfill 필요.

MFE_5D / 20D / 60D:
AI partnership event 기준 backfill 필요.

MAE_30D / 90D:
event fade 검증 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = price_moved_without_evidence / governance_relief_watch
rerating_result = event_premium
stage_failure_type = should_have_been_stage1_or_watch
```

### 교정 포인트

카카오는 R8에서 `OpenAI partnership`을 Stage 3로 주면 안 된다. AI 기능은 Stage 1, 제품 출시·유료화·ARPU·OPM 확인이 Stage 2~3다. governance risk는 무죄로 완화돼도, 플랫폼 매출 체급 변화와는 분리해야 한다.

---

## Case E — 크래프톤 `success_candidate + single-IP / AI-first watch`

```text
symbol = 259960
archetype = GAME_CONTENT_IP_REPEAT_MONETIZATION / SINGLE_IP_RELEASE_EVENT_PREMIUM / AI_SOFTWARE_APPLICATION
case_type = success_candidate + 4B-watch 후보
```

크래프톤은 R8 게임/IP에서 좋은 시험지다. 2025년 3월 출시된 inZOI는 early access 첫 주 100만 장 이상 판매됐고, Steam 글로벌 wishlist·seller 순위에서 강한 초기 반응을 보였다. 다만 early access 게임은 초기 판매와 장기 live-service monetization이 다르기 때문에 Stage 3는 bookings/retention/DLC/console 확장까지 봐야 한다. ([위키백과][7])

2025년 6월 크래프톤은 일본 ADK Holdings를 약 5.16억 달러에 인수하기로 했고, ADK는 Doraemon, Yu-Gi-Oh!, Crayon Shin-chan 등 300개 이상 애니메이션 제작에 관여한 광고·애니메이션 IP 회사로 설명됐다. 이는 게임 IP를 애니메이션·콘텐츠 IP로 확장하는 Stage 2 재료다. ([Reuters][8])

2025년 말에는 크래프톤이 `AI-first` 개발사 전환을 선언하고 agentic AI, GPU cluster, 사내 AI workflow에 1,000억 원 이상 투자하겠다고 발표했다. 이건 전략적으로 의미 있지만, 아직은 비용과 capex가 먼저 보이는 Stage 2~4B watch 재료다. ([The Verge][9])

### stage date 후보

```text
Stage 1:
2025-03
- inZOI launch / new IP 기대
- PUBG 이후 second IP 기대

Stage 2:
2025-04
- inZOI 첫 주 100만 장 이상 판매
- early access commercial traction

추가 Stage 2:
2025-06-24
- ADK Holdings 5.16억 달러 인수
- animation / IP pipeline 확장

Stage 3:
보류
- repeat bookings, retention, DLC, console expansion, IP monetization 확인 필요
- AI-first 전략은 비용과 매출 전환을 분리해야 함

Stage 4B:
inZOI 초기 판매·AI-first 발표·ADK 인수 기대가 주가에 먼저 반영되면 후보

Stage 4C:
신작 retention 부진, 리뷰 악화, single-IP 의존, AI capex 부담, IP 인수 integration 실패 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-04 inZOI 판매 발표일 OHLC backfill 필요.
2025-06-24 ADK 인수 발표일 OHLC backfill 필요.

MFE / MAE:
Stage 2별로 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = game_IP_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

크래프톤은 `single launch success`와 `repeat monetization`을 분리해야 한다. Stage 3는 첫 주 판매량이 아니라 **retention, paid content, live-service bookings, IP 확장 매출**에서 나온다.

---

## Case F — 시프트업 `success_candidate / IPO-overheat watch`

```text
symbol = 462870
archetype = GAME_CONTENT_IP / SINGLE_IP_RELEASE_EVENT_PREMIUM
case_type = success_candidate + overheat
```

시프트업은 R8 게임 IP에서 `상업적 성과는 좋지만 single-IP/IPO overheat를 조심해야 하는` 케이스다. Stellar Blade는 2024년 콘솔 히트작이었고, 시프트업은 2024년 7월 한국 게임사 IPO 중 크래프톤 이후 최대 규모로 상장했다. 이후 2025년 PC 버전은 3일 만에 100만 장 이상 판매됐고, 전체 판매량이 300만 장을 넘었다고 정리되어 있다. ([위키백과][10])

다만 시프트업은 상장 이후 valuation, 단일 IP 의존, 후속작/신작 일정, Tencent 지분, PC port 이후 매출 정상화 리스크를 봐야 한다.

### stage date 후보

```text
Stage 1:
2024-04
- Stellar Blade 출시 / 글로벌 console IP 기대

Stage 2:
2024-07-11
- IPO
- Stellar Blade와 Nikke 기반 매출 성장 기대

추가 Stage 2:
2025-06-11
- Stellar Blade PC 버전 출시
- 3일 100만 장 판매 / 총 300만 장 이상

Stage 3:
보류
- single title sales는 강하지만 repeat monetization, portfolio, OPM/FCF 확인 필요

Stage 4B:
IPO 후 valuation 과열 또는 PC port 판매 기대 선반영 구간

Stage 4C:
신작 지연, PC 판매 정상화 이후 매출 공백, 단일 IP 의존 심화 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2024-07-11 IPO 기준 OHLC backfill 필요.
2025-06-11 PC launch 기준 OHLC backfill 필요.

MFE / MAE:
각 이벤트 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate / IPO_overheat_watch
rerating_result = single_IP_success_candidate
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

시프트업은 R8에서 `game sales`는 강하지만, Stage 3-Green은 **IP portfolio와 반복매출**을 요구해야 한다. 단일 게임 판매량은 Stage 2, 장기 rerating은 retention과 차기작 pipeline이 필요하다.

---

## Case G — HYBE `4C-watch / governance legal risk`

```text
symbol = 352820
archetype = KPOP_PLATFORM_CONTENT_IP / PLATFORM_GOVERNANCE_LEGAL_RISK
case_type = 4C-watch
```

HYBE는 콘텐츠 IP가 강해도 governance/legal risk가 Green을 막을 수 있는 케이스다. 2025년 3월 법원은 NewJeans 멤버들이 ADOR 동의 없이 독립 활동을 하는 것을 막는 가처분을 인용했고, 이는 HYBE/ADOR와 NewJeans 간 분쟁이 장기화된 상태였음을 보여준다. ([Reuters][11])

2026년 4월에는 경찰이 HYBE 창업자 방시혁에 대해 IPO 관련 자본시장법 위반 혐의로 구속영장을 신청했다. Reuters는 방시혁이 초기 투자자들을 오도했다는 혐의를 받고 있고 약 1,900억 원 이익을 얻었다는 주장이 있다고 보도했다. HYBE 주가는 해당 소식 후 2.4% 하락했다. ([Reuters][12])

### stage date 후보

```text
Stage 1:
BTS / K-pop platform / Weverse / global IP 기대

Stage 2:
보류
- BTS comeback, Weverse monetization, concert revenue 등은 별도 검증 필요

Stage 3:
없음
- governance/legal overhang이 해소되기 전 Green 금지

Stage 4B:
BTS comeback 기대 또는 K-pop IP 기대가 주가에 먼저 반영되면 후보

Stage 4C:
2025-03-21
- NewJeans 독립활동 금지 가처분
- 핵심 아티스트/레이블 갈등

추가 4C-watch:
2026-04-21
- 방시혁 구속영장 신청
- IPO 관련 법적 리스크
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage4c_price:
2025-03-21 / 2026-04-21 OHLC backfill 필요.

MFE / MAE:
BTS comeback 기대와 legal event 기준 분리 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = thesis_break_watch
rerating_result = legal_governance_overhang
stage_failure_type = should_have_been_red_or_watch
```

### 교정 포인트

HYBE는 R8에서 `content IP`보다 `governance/legal risk`가 먼저다. BTS·K-pop IP는 강하지만, Stage 3는 **IP monetization + legal risk 해소 + artist pipeline 안정**이 같이 필요하다.

---

# 5. 이번 R8 case별 요약표

| case  | 분류                                  | Stage 3 판정 |                          4B/4C 판정 | 가격경로 1차 판단                             |
| ----- | ----------------------------------- | ---------: | --------------------------------: | -------------------------------------- |
| 더존비즈온 | success_candidate                   |         보류 |            EQT 거래 후 과열 시 4B-watch | ERP 반복매출은 좋지만 ARR/OPM 확인 필요            |
| 삼성SDS | success_candidate + 4B-watch        |         보류 |       KKR CB 발표일 +20.8%는 4B-watch | AI infra 투자와 매출 전환 분리                  |
| NAVER | success_candidate                   |         보류 | Webtoon IPO / AI 모델 과열 시 4B-watch | MAU·AI 성능보다 monetization 필요            |
| 카카오   | failed_rerating / governance relief |         없음 |         OpenAI 발표 급등은 price-first | AI partnership은 Stage 1~2              |
| 크래프톤  | success_candidate                   |         보류 |         신작·AI-first 과열 시 4B-watch | inZOI/ADK는 Stage 2, repeat bookings 필요 |
| 시프트업  | success_candidate + overheat        |         보류 |            IPO/single-IP 과열 watch | 단일 IP 판매량은 Stage 2                     |
| HYBE  | 4C-watch                            |         없음 |           NewJeans/방시혁 legal risk | 콘텐츠 IP보다 governance risk 우선            |

---

# 6. 각 case별 stage date 후보 요약

```text
더존비즈온:
Stage 1 = 2024~2025 B2B SaaS / cloud ERP 기대
Stage 2 = 2025-11-07 EQT 37.6% 지분 인수 발표
Stage 3 = 보류 / ARR·churn·OPM·FCF 확인 필요
Stage 4B = 거래 발표 후 valuation 과열 시 후보
Stage 4C = 거래 승인 실패 / 성장 둔화 / churn 상승 시 후보

삼성SDS:
Stage 1 = 기업 AI 전환 / 삼성 AI infra 기대
Stage 2 = 2026-04-15 KKR 8.2억 달러 CB 투자
Stage 3 = 보류 / AI 매출·계약·margin 필요
Stage 4B = 2026-04-15 장중 +20.8%
Stage 4C = CB dilution / AI 투자 매출 부진 / M&A 실패 시 후보

NAVER:
Stage 1 = Webtoon IPO / sovereign AI 기대
Stage 2 = 2024-06-17 Webtoon IPO valuation target
Stage 2 추가 = 2026-01-03 HyperCLOVA X 32B Think 공개
Stage 3 = 보류 / AI cloud revenue·paid content·margin 필요
Stage 4B = IPO/AI 모델 발표 과열 시 후보
Stage 4C = Webtoon valuation 하락 / AI 투자비 부담 / 광고 둔화 시 후보

카카오:
Stage 1 = 2025-02-04 OpenAI partnership
Stage 2 = 보류 / AI monetization 미확인
Stage 3 = 없음
Stage 4B = 발표 직후 +9% 후 하락, price-first event
Stage 4C = 2024~2025 founder legal overhang, 2025-10 무죄로 완화

크래프톤:
Stage 1 = 2025-03 inZOI launch 기대
Stage 2 = 2025-04 inZOI 첫 주 100만 장 이상 판매
Stage 2 추가 = 2025-06-24 ADK Holdings 인수
Stage 3 = 보류 / repeat bookings·retention·DLC 필요
Stage 4B = 신작/AI-first/ADK 기대 과열 시 후보
Stage 4C = retention 부진 / single-IP 의존 / AI capex 부담 시 후보

시프트업:
Stage 1 = Stellar Blade 출시 / 글로벌 IP 기대
Stage 2 = 2024-07-11 IPO
Stage 2 추가 = 2025-06-11 PC 버전 판매 3일 100만 장
Stage 3 = 보류 / repeat monetization·portfolio 필요
Stage 4B = IPO / PC port 기대 과열 시 후보
Stage 4C = 신작 지연 / single-IP 의존 / 매출 공백 시 후보

HYBE:
Stage 1 = K-pop global IP / Weverse / BTS comeback 기대
Stage 2 = 보류 / IP monetization 세부 확인 필요
Stage 3 = 없음
Stage 4B = BTS comeback 기대 선반영 시 후보
Stage 4C = 2025-03-21 NewJeans 가처분, 2026-04-21 방시혁 구속영장 신청
```

---

# 7. 가격경로 검증

R8은 정확한 OHLC backfill 없이 수익률을 확정하면 안 된다. AI partnership, IPO, 게임 출시, M&A, 법적 리스크 같은 이벤트가 많아서 stage별 가격을 반드시 분리해야 한다.

| case  | stage3_price | MFE/MAE                            | below_stage3 | peak/drawdown                  |
| ----- | -----------: | ---------------------------------- | ------------ | ------------------------------ |
| 더존비즈온 |   Stage 3 없음 | Stage 2 EQT 기준 backfill            | N/A          | deal premium fade 확인 필요        |
| 삼성SDS |   Stage 3 없음 | Stage 2 KKR 기준 backfill            | N/A          | +20.8% 이후 drawdown 필요          |
| NAVER |   Stage 3 없음 | Webtoon IPO / AI model 기준 backfill | N/A          | Webtoon valuation, AI rally 분리 |
| 카카오   |   Stage 3 없음 | OpenAI event MFE_5D/20D 필요         | N/A          | event fade / legal relief 분리   |
| 크래프톤  |   Stage 3 없음 | inZOI / ADK / AI-first 기준 backfill | N/A          | 신작 기대 peak/drawdown            |
| 시프트업  |   Stage 3 없음 | IPO / PC launch 기준 backfill        | N/A          | single-IP peak/drawdown        |
| HYBE  |   Stage 3 없음 | legal event 기준 backfill            | N/A          | NewJeans/Bang risk drawdown 필요 |

핵심은 이거다.

```text
R8에서 Stage 3는 이벤트 날짜가 아니라
반복매출·유료화·bookings·ARR·OPM/FCF가 확인되는 날짜다.
```

---

# 8. score-price alignment 판정

```text
더존비즈온:
alignment = success_candidate
EQT 투자와 cloud ERP 반복수요는 좋지만 Stage 3는 ARR/OPM 확인 후.

삼성SDS:
alignment = event_premium + success_candidate
KKR 투자와 AI infra는 Stage 2.
발표일 +20.8%는 4B-watch.

NAVER:
alignment = success_candidate
Webtoon IPO와 HyperCLOVA X는 Stage 2.
AI/cloud monetization 전 Stage 3 금지.

카카오:
alignment = price_moved_without_evidence
OpenAI partnership은 Stage 1~2.
AI revenue 전 Green 금지.

크래프톤:
alignment = success_candidate
inZOI 판매와 ADK 인수는 Stage 2.
repeat bookings / retention 전 Stage 3 금지.

시프트업:
alignment = success_candidate + overheat_watch
Stellar Blade 성과는 강하지만 single-IP/IPO risk.

HYBE:
alignment = thesis_break_watch
K-pop IP가 좋아도 legal/governance risk가 Green을 막음.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
recurring_revenue +5
ARR_proxy +5
bookings_repeatability +4
paid_usage_conversion +4
enterprise_contract_quality +4
OPM_improvement +4
FCF_conversion +4
customer_retention_or_churn +4
IP_monetization_beyond_launch +3
cloud_AI_revenue_conversion +4
operational_trust +4
```

R8에서 진짜 강한 건 “AI 기능”이나 “신작 출시”가 아니라, **반복해서 돈을 내는 고객과 이익률**이다.

## 내릴 축

```text
ai_feature_only -5
partnership_headline_only -4
MAU_without_ARPU -4
game_launch_first_week_only -4
IPO_first_month_rally -4
single_IP_dependence -4
M&A_event_without_integration -3
AI_capex_without_revenue -4
media_report_or_model_release_only -3
founder_legal_risk -5
privacy_or_security_trust_break -5
```

삼성SDS, 카카오, NAVER, 크래프톤, HYBE 때문에 이 감점축이 필요하다.

## Green gate 강화 조건

R8 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. 반복매출 또는 bookings 확인
2. ARPU / paid usage / ARR proxy 확인
3. OPM 또는 gross margin 개선
4. FCF conversion
5. 고객 retention / churn 안정
6. IP monetization이 단발 신작을 넘어 반복화
7. AI 기능이 실제 유료 매출 또는 비용절감으로 연결
8. privacy / security / governance hard risk 통과
9. 가격경로가 증거 이후 따라옴

금지:
AI 기능 출시
OpenAI partnership
모델 논문 / 모델 공개
MAU 증가만 있음
신작 첫 주 판매만 있음
IPO 급등
M&A 발표
founder legal risk
보안/개인정보 신뢰 훼손
```

## 4B 조기감지 조건

```text
4B-watch:
AI partnership 발표 직후 급등
신작 출시 또는 IPO 후 주가 2배 이상
AI infra 투자 발표에 주가가 먼저 반응
Webtoon/IP valuation이 매출보다 먼저 확장
single-IP 기대가 모든 valuation을 설명
보고서가 AI·콘텐츠 macro만 반복

4B-elevated:
신작 retention 둔화
ARR 성장률 둔화
AI capex 증가로 margin 훼손
M&A integration cost 확대
IP pipeline 공백
governance/legal overhang 재점화

4B-graduated:
좋은 실적에도 주가 반응 둔화
신규 AI 기능/파트너십이 더 이상 surprise가 아님
bookings 성장률 normalize
IP launch cycle 종료
```

## 4C hard gate 조건

```text
privacy breach
security outage
founder / major shareholder legal break
regulatory sanction
AI product monetization failure
ARR churn spike
paid user decline
game launch failure
IP litigation
M&A integration failure
single-IP collapse
advertising / commerce take-rate damage
FCF deterioration from AI capex
```

---

# 10. shadow-only 기록

이번 R8 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_127.md
docs/checkpoints/checkpoint_28a_round127_r8_loop7_platform_content_sw_security_price_validation.md
src/e2r/sector/round127_r8_loop7_platform_content_sw_security.py
data/e2r_case_library/cases_r8_loop7_round127.jsonl
data/sector_taxonomy/score_weight_profiles_round127_r8_loop7_v7.csv
output/e2r_round127_r8_loop7_platform_content_sw_security/
```

---

# 이번 R8 Loop 7 결론

R8은 Stage 3 후보가 있다. 더존비즈온, 삼성SDS, NAVER, 크래프톤, 시프트업 같은 기업은 실제로 구조 후보가 될 수 있다. 하지만 R8은 **Stage 3를 너무 빨리 주면 false positive가 가장 많이 쌓이는 섹터**이기도 하다.

이번 라운드의 핵심 교정은 이거다.

```text
1. B2B SaaS는 좋은 구조 후보지만, PE 투자나 거래 발표가 아니라 ARR/OPM/FCF가 Stage 3다.

2. AI cloud/IT services는 KKR·AI infra 투자만으로 Green이 아니다.
   enterprise contract와 AI revenue conversion이 필요하다.

3. NAVER의 Webtoon IPO와 HyperCLOVA X는 Stage 2다.
   paid content, ARPU, AI cloud revenue 전 Stage 3 금지다.

4. 카카오의 OpenAI partnership은 Stage 1~2 attention이다.
   AI monetization 전에는 price_moved_without_evidence로 둔다.

5. 크래프톤·시프트업은 game IP 성과가 강하지만,
   첫 주 판매나 IPO가 아니라 repeat bookings와 IP portfolio가 Stage 3다.

6. HYBE는 K-pop IP가 강해도 governance/legal risk가 Green을 막는다.
```

한 문장으로 압축하면:

> **R8에서 진짜 Stage 3는 “AI·게임·콘텐츠가 핫하다”가 아니라, 반복매출·bookings·paid usage·ARR·OPM/FCF가 확인되는 순간이다.**
> **R8은 성장 서사가 빠르게 가격을 앞질러 가므로, 4B-watch와 governance/privacy/security 4C gate를 가장 빨리 붙여야 한다.**

[1]: https://www.reuters.com/world/asia-pacific/swedish-firm-eqt-shells-out-930-million-slice-south-koreas-douzone-bizon-2025-11-07/?utm_source=chatgpt.com "Swedish firm EQT shells out $930 million for a slice of South Korea's Douzone Bizon"
[2]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[3]: https://www.reuters.com/markets/us/navers-webtoon-entertainment-targets-up-267-bln-valuation-us-ipo-2024-06-17/?utm_source=chatgpt.com "Naver's Webtoon Entertainment aims up to $2.67 bln valuation in US IPO"
[4]: https://arxiv.org/abs/2601.03286?utm_source=chatgpt.com "HyperCLOVA X 32B Think"
[5]: https://www.reuters.com/technology/artificial-intelligence/openai-kakao-jointly-develop-ai-products-south-korea-2025-02-04/?utm_source=chatgpt.com "OpenAI clinches deal with Kakao, talks with SoftBank and Samsung about Stargate"
[6]: https://www.reuters.com/business/media-telecom/south-korea-prosecutors-seek-15-year-jail-term-kakao-founder-kim-2025-08-29/?utm_source=chatgpt.com "South Korea prosecutors seek 15-year jail term for Kakao founder Kim"
[7]: https://en.wikipedia.org/wiki/InZOI?utm_source=chatgpt.com "InZOI"
[8]: https://www.reuters.com/en/south-korean-game-company-krafton-acquire-japans-adk-516-mln-2025-06-24/?utm_source=chatgpt.com "South Korean game company Krafton to acquire Japan's ADK for $516 mln"
[9]: https://www.theverge.com/news/805509/krafton-pubg-ai-first-developer-agentic-gpu-cluster?utm_source=chatgpt.com "PUBG maker Krafton is turning into an 'AI first' developer"
[10]: https://en.wikipedia.org/wiki/Shift_Up?utm_source=chatgpt.com "Shift Up"
[11]: https://www.reuters.com/lifestyle/south-korea-court-blocks-k-pop-group-newjeans-leaving-agency-2025-03-21/?utm_source=chatgpt.com "South Korea court blocks K-pop group NewJeans from leaving agency"
[12]: https://www.reuters.com/world/asia-pacific/south-korea-police-seek-detention-warrant-hybe-chairman-yonhap-says-2026-04-21/?utm_source=chatgpt.com "South Korea police seek detention warrant for BTS agency founder Bang"
