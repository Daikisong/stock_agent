응. **Round 14 진행할게.**
이번 라운드는 이전보다 더 “정규화 검증”에 초점을 둘게. 즉, 단순히 테마를 흡수하는 게 아니라:

```text
이 테마가 어떤 archetype에 들어가는가?
성공사례라면 실제로 EPS/FCF와 주가가 같이 갔는가?
반례라면 어떤 조건에서 Green을 막아야 하는가?
점수비중은 어떤 축을 높이고 어떤 축을 눌러야 하는가?
```

이걸 기준으로 더 채운다.

기존 정신은 그대로다. 에이전트는 테마봇이 아니라, **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**을 찾는 시스템이어야 한다. 테마명은 검색과 분류를 위한 태그일 뿐이고, 점수는 실제 공시·리포트·뉴스·재무·가격 evidence에서 나와야 한다.
또 OpenDART 상세공시처럼 계약금액, 계약기간, 매출 대비 계약금액, OP YoY 같은 필드는 실제로 존재할 때만 써야 하고, 없는 숫자를 추정해서 채우면 안 된다.

---

# Round 14 핵심 결론

이번 라운드에서 더 채운 쪽은 이거야.

```text
1. 철도 / 대형 인프라 수주
2. AI 데이터센터 냉각 / HVAC / 액침냉각
3. 폐기물처리 / 재활용 / 폐배터리
4. 보안 / 딥페이크 / 생체인식 / IT 보안
5. 클라우드 / ERP / B2B 소프트웨어
6. 교육 / 키즈 / 저출산 역풍
7. 의류 브랜드 / 의류 OEM·ODM
8. 건자재 / 시멘트 / 철근 / 부동산 사이클
9. REIT / 부동산 자산 보유 / 배당
10. CRO / 임상서비스 / CDMO 보조축
```

여기서 몇 개는 **Green 가능**이고, 몇 개는 **Watch 중심**, 몇 개는 **Red/4B 방어 중심**이야.

---

# 1. RAIL_INFRASTRUCTURE

철도 / 고속철 / 인프라 수출

## 포함 테마

```text
철도
우크라 재건 일부
네옴시티 일부
대형 인프라
현대로템 철도
고속철 수출
```

## 핵심 구조

```text
국가 인프라 예산 / 해외 발주
→ 대형 수주
→ 납품 스케줄
→ 매출·OP 인식
→ 수주잔고 기반 visibility
```

## 성공사례 후보

**현대로템 철도 수출**은 이 archetype의 좋은 후보야. 현대 로템은 모로코 국영철도 ONCF로부터 약 2.2조원, 15억 달러 규모의 2층 전동차 수주를 따냈고, Reuters는 이를 현대 로템 철도사업 사상 최대 수주라고 보도했다. 이건 단순 철도 테마가 아니라 **대형 계약 + 납품 visibility + 해외 인프라 수요**가 있는 Stage 1~2 사례로 볼 수 있다. ([Reuters][1])

## 반례

```text
- 철도 정책 기대만 있는 관련주
- 실제 수주 없이 우크라 재건/네옴시티/철도 테마만 붙은 종목
- 수주는 있으나 납기·마진·원가가 불명확한 종목
- 프로젝트 financing 지연
```

## Stage 기준

```text
Stage 1:
철도 정책
해외 입찰
대형 인프라 뉴스
거래대금 증가

Stage 2:
실제 계약
계약금액/매출 비중
납품 스케줄
OP/EPS 상향 가능성

Stage 3:
다년 수주잔고
마진이 확인된 납품 구조
해외 고객 다변화
시장에 아직 방산/철도 저평가 프레임 존재

4B:
대형 수주 기대가 대부분 가격에 반영
추가 수주 공백
밸류에이션 정상화

4C:
계약 취소
납품 지연
원가 상승
프로젝트 financing 실패
```

## 점수비중 v0.6

```text
EPS/FCF: 20
Structural Visibility: 23
Bottleneck/Pricing: 12
Market Mispricing: 14
Valuation Rerating: 12
Capital Allocation: 1
Information Confidence: 5
Risk Penalty: project_delay / margin_uncertainty
```

**정규화 포인트:**
철도는 `CONTRACT_BACKLOG_INDUSTRIAL`과 비슷하지만 방산보다 마진과 납품 리스크가 더 중요하다. 실제 수주가 있으면 Stage 2 이상 가능. 정책 테마만 있으면 event_watch.

---

# 2. AI_DATA_CENTER_COOLING / HVAC / 액침냉각

## 포함 테마

```text
냉각시스템
액침냉각
반도체·디스플레이 클린룸
AI 데이터센터
HVAC
전력망
ESS
서버 인프라
```

## 핵심 구조

```text
AI 서버 고밀도화
→ 발열 증가
→ 액체냉각 / HVAC / 전력·냉각 병목
→ 데이터센터 CAPEX와 동행
→ 수주·납품·서비스 매출
```

## 성공사례 후보

데이터센터 냉각은 이제 별도 sub-archetype으로 둬야 해. Ecolab은 AI 데이터센터 냉각 수요를 잡기 위해 CoolIT Systems를 47.5억 달러에 인수한다고 발표했고, Reuters는 액체냉각이 고밀도 AI 서버 전력·열 부하를 관리하는 핵심 솔루션으로 부상했다고 보도했다. ([Reuters][2])
삼성전자도 독일 HVAC 기업 FlaktGroup을 15억 유로에 인수해 AI 데이터센터용 냉각 역량을 강화하려고 했다. 이는 냉각이 단순 설비가 아니라 AI 인프라 supply chain의 병목으로 커지고 있음을 보여준다. ([Reuters][3])

## 반례

```text
- 액침냉각 테마만 있고 실제 고객·납품 없음
- 데이터센터 CAPEX 지연
- 프로젝트는 있으나 마진이 낮은 설비업체
- 기술은 있으나 양산·유지보수 역량 없음
```

## Stage 기준

```text
Stage 1:
AI 데이터센터 발열/전력 뉴스
냉각·HVAC 수요 증가
클린룸·액침냉각 키워드

Stage 2:
실제 수주
고객사 데이터센터 CAPEX와 연결
매출 인식 시점 확인
OP/EPS 상향

Stage 3:
다년 데이터센터 CAPEX
핵심 냉각 병목 지위
서비스/유지보수 반복매출
가격전가력

4B:
AI CAPEX narrative 과열
냉각 관련주 동반 급등
설비 CAPA 과잉 우려

4C:
데이터센터 프로젝트 지연
AI CAPEX cut
마진 훼손
고객사 취소
```

## 점수비중 v0.6

```text
EPS/FCF: 21
Structural Visibility: 22
Bottleneck/Pricing: 22
Market Mispricing: 13
Valuation Rerating: 12
Information Confidence: 5
Risk Penalty: AI_capex_delay / project_margin
```

**정규화 포인트:**
냉각은 AI 데이터센터 인프라 안에서도 독립 sub-archetype으로 둘 가치가 있어. 다만 테마만으로 Green 금지. 실제 고객·수주·납품·반복 서비스가 있어야 한다.

---

# 3. WASTE_RECYCLING_ENVIRONMENT

폐기물처리 / 재활용 / 폐배터리 / 탈플라스틱

## 포함 테마

```text
폐기물처리
폐배터리
탈 플라스틱
플라스틱 재활용
폐기물 에너지화
골판지·제지 일부
```

## 핵심 구조

```text
규제 강화 / 처리 수요
→ 허가권 / 처리시설 / 장기계약
→ 반복 처리량
→ 반복 FCF
```

## 성공사례 후보

폐기물처리는 의외로 E2R 가능성이 있는 테마야. EQT는 한국 KJ Environment와 계열사를 인수해 플라스틱 재활용·폐기물 에너지화 플랫폼을 만들기로 했고, Reuters는 이 플랫폼이 한국 인구의 절반 이상을 커버하는 재활용·폐기물 처리 네트워크가 될 수 있다고 보도했다. 이건 폐기물처리가 단순 ESG 테마가 아니라 **허가권·처리시설·반복 FCF 인프라**가 될 수 있음을 보여준다. ([Reuters][4])

## 반례

```text
- 폐배터리 테마만 있고 실제 회수량 없음
- 재활용 설비는 있으나 가동률 낮음
- 금속가격 하락으로 회수 마진 악화
- 규제 기대만 있고 실제 처리량 없음
```

## Stage 기준

```text
Stage 1:
폐기물 규제
재활용 설비
폐배터리·플라스틱 재활용 뉴스

Stage 2:
처리량 증가
장기계약
가동률 상승
OP/FCF 개선

Stage 3:
허가권·처리시설 병목
반복 FCF
고객사 다변화
시장에 아직 단순 ESG 테마 프레임

4B:
ESG/재활용 테마 과열
폐배터리 기대 선반영

4C:
가동률 하락
금속가격 하락
CAPEX 부담
규제 지연
```

## 점수비중 v0.6

```text
EPS/FCF: 18
Structural Visibility: 22
Bottleneck/Pricing: 15
Market Mispricing: 13
Valuation Rerating: 12
Information Confidence: 5
Risk Penalty: utilization / commodity_price / capex
```

**정규화 포인트:**
폐기물처리는 Green 가능. 폐배터리는 Watch 중심. 실제 처리량과 FCF가 없으면 테마다.

---

# 4. SECURITY_IDENTITY_DEEPFAKE

IT보안 / 딥페이크 / 생체인식 / CCTV

## 포함 테마

```text
IT 보안
딥페이크
생체인식
CCTV
클라우드 보안
AI 보안
컨택센터 보안 일부
```

## 핵심 구조

```text
보안 위협 증가 / 규제 강화
→ 기업·정부 보안 지출
→ 반복 구독 또는 장기계약
→ OPM·ARR·FCF 개선
```

## 성공사례 후보

보안은 구조적 수요가 커질 수 있지만, Green은 조심해야 한다. 한국은 2024년에 딥페이크 성범죄 대응을 위해 시청·소지까지 처벌하는 법안을 통과시켰고, 경찰 수사 건수도 크게 늘었다. 이런 규제·사회적 압력은 딥페이크 탐지·보안 수요의 Stage 1 신호가 될 수 있다. ([Reuters][5])

## 반례

CrowdStrike는 보안 SW archetype의 중요한 반례야. 보안 수요가 구조적으로 강해도, 2024년 faulty update로 전 세계 850만대 이상의 Windows 기기가 영향을 받았고, 주주 소송과 Delta 등 고객 손실 문제가 발생했다. Reuters는 CrowdStrike 주가가 12일 동안 32% 하락하며 250억 달러 시총이 사라졌다고 보도했다. 즉 보안업체는 반복매출이 있어도 **운영 신뢰도와 장애 리스크가 hard 4C**가 될 수 있다. ([Reuters][6])

## Stage 기준

```text
Stage 1:
보안 사고 증가
딥페이크/AI 보안 규제
정부·기업 보안 투자 뉴스

Stage 2:
실제 계약
구독/ARR 증가
고객사 다변화
OPM 개선

Stage 3:
반복 보안 구독
고객 이탈 낮음
규제 수혜
시장에 아직 단순 보안 테마 프레임

4B:
보안 테마 과열
멀티플 과다
신규 경쟁자 급증

4C:
대형 장애
고객 소송
보안 신뢰 훼손
갱신율 하락
```

## 점수비중 v0.6

```text
EPS/FCF: 20
Structural Visibility: 20
Bottleneck/Pricing: 10
Market Mispricing: 14
Valuation Rerating: 13
Information Confidence: 5
Risk Penalty: operational_trust / outage / legal
```

**정규화 포인트:**
보안은 Green 가능성이 있지만, 단순 테마가 아니라 ARR/계약/갱신율이 필요하다. 대형 장애는 바로 4C.

---

# 5. CLOUD_AI_SOFTWARE_INFRA

클라우드 / ERP / B2B 소프트웨어 / 컨택센터

## 포함 테마

```text
클라우드 컴퓨팅
원격근무
컨택센터
ERP
B2B SaaS
AI 소프트웨어
광고 플랫폼 일부
```

## 핵심 구조

```text
반복 소프트웨어 매출
→ 고객 lock-in
→ ARPU / take-rate / OPM 개선
→ FCF 개선
```

## 성공사례 후보

더존비즈온은 국내 B2B 소프트웨어 archetype의 핵심 후보야. EQT는 더존비즈온 지분 37.6%를 약 9.3억 달러에 인수하기로 했고, Reuters는 더존비즈온이 한국 중소기업 대상 클라우드 ERP·회계·세무·컴플라이언스 소프트웨어를 제공한다고 설명했다. 이건 `CLOUD_AI_SOFTWARE_INFRA`에서 반복매출·SMB lock-in·운영 개선을 볼 수 있는 Stage 1~2 사례다. ([Reuters][7])

## 반례

```text
- AI 기능만 추가하고 FCF 훼손
- 클라우드 비용 증가로 OPM 하락
- 고객 이탈/가격 인상 실패
- 컨택센터/원격근무 테마만 있고 반복매출 없음
```

## Stage 기준

```text
Stage 1:
클라우드 전환
ERP/SaaS 수요
AI 기능 도입
B2B 고객 증가

Stage 2:
반복매출 증가
ARPU 상승
OPM 개선
고객 retention 확인

Stage 3:
고객 lock-in
높은 FCF conversion
가격 인상 가능
시장에 아직 전통 SW 프레임

4B:
SaaS/AI SW narrative 과열
multiple 포화

4C:
고객 이탈
AI 비용 과다
OPM 하락
경쟁 심화
```

## 점수비중 v0.6

```text
EPS/FCF: 20
Structural Visibility: 23
Bottleneck/Pricing: 8
Market Mispricing: 16
Valuation Rerating: 14
Information Confidence: 5
Risk Penalty: ai_cost / churn / margin
```

**정규화 포인트:**
클라우드/SaaS는 Green 가능. 하지만 반복매출, OPM, FCF가 핵심이지 AI 키워드가 핵심이 아니다.

---

# 6. EDUCATION_SPECIALTY_SERVICES

교육 / 취업 / 키즈 / 유아용품

## 포함 테마

```text
교육
취업일자리
키즈
유아용품
학습지
에듀테크
입시
성인교육
```

## 핵심 구조

```text
반복 수강 / 가격 인상 / 브랜드 lock-in
→ OPM 개선
→ 저출산 리스크를 상쇄하는 확장성
```

## 성공사례 후보

교육은 구조적 반복수요가 있지만 저출산 리스크도 매우 크다. 한국에서는 사교육 경쟁이 여전히 강해 미취학 아동까지 사교육 참여가 높고, private education spending이 가계 부담으로 작용한다는 보도가 있다. 이건 교육기업의 수요 기반이 강하다는 Stage 1 신호이면서, 동시에 정책·저출산 리스크를 봐야 한다는 뜻이다. ([Financial Times][8])

## 반례

```text
- 저출산으로 TAM 축소
- 사교육 규제
- 단기 입시제도 변경 테마
- AI 튜터 경쟁으로 가격 하락
- 키즈/유아용품은 출생아 수 감소에 취약
```

## Stage 기준

```text
Stage 1:
입시제도 변화
수강생 증가
가격 인상
교육비 증가

Stage 2:
반복매출
OPM 개선
온라인/성인교육 확장
해외 수강생 증가

Stage 3:
저출산 리스크를 상쇄하는 성인/해외/프리미엄 확장
가격 결정력
FCF 개선

4B:
입시 테마 과열
정책 기대 선반영

4C:
사교육 규제
학생 수 감소
가격 인하
AI 대체
```

## 점수비중 v0.6

```text
EPS/FCF: 18
Structural Visibility: 18
Bottleneck/Pricing: 5
Market Mispricing: 12
Valuation Rerating: 12
Information Confidence: 5
Risk Penalty: birthrate / regulation / ai_substitution
```

**정규화 포인트:**
교육은 Watch 중심. 저출산을 상쇄하는 성인교육/해외/구독형 매출 없으면 Green 제한.

---

# 7. APPAREL_BRAND_OEM

의류 브랜드 / 의류 OEM·ODM / 의류소재

## 포함 테마

```text
의류 브랜드
의류 OEM·ODM
의류소재
키즈·유아용품 일부
K패션 브랜드
```

## 핵심 구조

```text
브랜드 / 수출 / 고객사 주문
→ 재고 관리
→ OPM·FCF 개선
```

## 성공사례 후보

한국 패션 브랜드는 K컬처 확산으로 글로벌 진출 가능성이 있지만, 대부분은 inventory와 유행 리스크가 크다. 브랜드가 진짜 E2R이 되려면 **해외 채널, 반복 구매, 재고 회전, OPM 개선**이 필요하다. 단순 협업·팝업·셀럽 노출만으로는 Green이 아니다.

## 반례

```text
- 단일 유행 브랜드
- 재고 증가
- 할인 판매 증가
- 중국/단일 채널 의존
- OEM 고객사 주문 둔화
```

## Stage 기준

```text
Stage 1:
해외 팝업
K패션 협업
주문 증가
셀럽·IP 콜라보

Stage 2:
해외 매출 증가
재고 회전 안정
OPM 개선
고객사 다변화

Stage 3:
브랜드 반복 구매
글로벌 채널 확장
FCF 개선
시장에 아직 내수 패션 프레임

4B:
브랜드 hype 과열
재고 리스크 확대

4C:
재고 증가
할인 판매
채널 둔화
주문 취소
```

## 점수비중 v0.6

```text
EPS/FCF: 18
Structural Visibility: 16
Bottleneck/Pricing: 8
Market Mispricing: 14
Valuation Rerating: 12
Information Confidence: 5
Risk Penalty: inventory / fashion_cycle / channel_concentration
```

**정규화 포인트:**
의류는 K뷰티/K푸드보다 Green을 더 보수적으로. 재고와 할인율이 핵심 Red flag.

---

# 8. BUILDING_MATERIALS_CYCLE / REIT_DEVELOPMENT_TRUST

## 포함 테마

```text
건자재
시멘트
레미콘
콘크리트
철근
거푸집
가구
리츠
개발신탁
부동산 자산 보유
```

## 핵심 구조

```text
건설 착공 / 원가 / 가격인상 / 금리
→ OPM·배당·FCF 변화
```

## 성공사례 후보

건자재는 가격 인상과 원가 안정이 같이 있을 때 Stage 2까지 가능하다. 리츠는 금리 하락, 임대료 상승, 배당 안정성이 있으면 Watch-to-Green 후보가 될 수 있다. 하지만 건설 PF와 착공 감소가 있으면 바로 눌린다.

## 반례

```text
- PF 부실로 착공 감소
- 원가 상승
- 가격 인상 실패
- 리츠 금리 상승
- 공실률 상승
- 배당 삭감
```

## Stage 기준

```text
Stage 1:
가격 인상
금리 하락
착공 회복
배당 매력

Stage 2:
OPM 개선
원가 안정
출하량 회복
배당 안정

Stage 3:
공급 재편
가격협상력
반복 임대수익
부채 리스크 낮음

4B:
부동산 회복 기대 선반영
배당주 과열

4C:
PF 부실
착공 감소
공실률 증가
배당 삭감
```

## 점수비중 v0.6

```text
EPS/FCF: 17
Structural Visibility: 12
Bottleneck/Pricing: 12
Market Mispricing: 12
Valuation Rerating: 12
Capital Allocation: 5
Information Confidence: 5
Risk Penalty: credit / rates / vacancy
```

**정규화 포인트:**
건자재/리츠는 Green을 쉽게 주면 안 된다. 금리·PF·공실·배당 안정성이 핵심.

---

# 9. CRO_CLINICAL_SERVICE

## 포함 테마

```text
CRO
임상시험수탁기관
AI 신약개발 일부
제약바이오 서비스
```

## 핵심 구조

```text
제약·바이오 R&D 증가
→ 임상시험 수탁
→ 반복 서비스 매출
→ 고객사 다변화
```

## 성공사례 후보

CRO는 pre-revenue biotech과 다르다. CRO는 실제 서비스 매출이 있고, 고객사·임상 파이프라인이 늘면 반복 매출이 될 수 있다. 다만 고객사 R&D cycle과 바이오 투자심리에 영향을 받는다.

## 반례

```text
- 바이오 투자심리 둔화
- 고객사 임상 축소
- 단일 고객 의존
- 수주잔고는 있으나 마진 낮음
```

## Stage 기준

```text
Stage 1:
임상 건수 증가
제약 R&D 증가
수주잔고 증가

Stage 2:
매출/OP 증가
고객사 다변화
반복 서비스 매출

Stage 3:
다년 수주잔고
고객사 포트폴리오 다변화
높은 FCF conversion

4B:
바이오 R&D 기대 과열

4C:
임상 축소
고객사 예산 삭감
수주 취소
```

## 점수비중 v0.6

```text
EPS/FCF: 18
Structural Visibility: 20
Bottleneck/Pricing: 8
Market Mispricing: 12
Valuation Rerating: 12
Information Confidence: 5
Risk Penalty: biotech_funding_cycle / customer_concentration
```

**정규화 포인트:**
CRO는 Green 가능하지만 CDMO보다 약하다. 수주잔고와 고객 다변화가 핵심.

---

# 10. 이번 라운드 후 Green 정책 업데이트

## Green 가능성이 더 명확해진 archetype

```text
MEMORY_HBM_CAPACITY
CONTRACT_BACKLOG_INDUSTRIAL
AI_DATA_CENTER_INFRASTRUCTURE
AI_DATA_CENTER_COOLING
CDMO_HEALTHCARE_CONTRACT
WASTE_RECYCLING_ENVIRONMENT
K_BEAUTY_EXPORT_DISTRIBUTION
BEAUTY_OEM_ODM_SUPPLYCHAIN
FINANCIAL_SPREAD_BALANCE_SHEET
INSURANCE_UNDERWRITING_CYCLE
```

## Watch 중심으로 유지해야 할 archetype

```text
CLOUD_AI_SOFTWARE_INFRA
SECURITY_IDENTITY_DEEPFAKE
EDUCATION_SPECIALTY_SERVICES
APPAREL_BRAND_OEM
BUILDING_MATERIALS_CYCLE
REIT_DEVELOPMENT_TRUST
RAIL_INFRASTRUCTURE
CRO_CLINICAL_SERVICE
ROBOTICS_FACTORY_AUTOMATION
DIGITAL_ASSET_TOKENIZATION
```

## Red/4B 방어 중심

```text
CHEMICAL_SPREAD
SHIPPING_FREIGHT_CYCLE
BATTERY_MATERIALS_CAPEX_OVERHEAT
CONSTRUCTION_REAL_ESTATE_CREDIT
EVENT_DISEASE_PEST_DEMAND
SPECULATIVE_SCIENCE_THEME
METAVERSE_NFT_THEME
BIOTECH_PRE_REVENUE_REGULATORY
```

---

# 11. 이번 라운드의 핵심 정규화 업데이트

```text
1. 철도는 실제 해외 대형 수주가 있으면 Stage 2 이상 가능.
   단, 정책/재건 테마만 있으면 event_watch.

2. AI 냉각/HVAC는 AI Data Center Infra의 핵심 sub-archetype으로 분리.
   실제 고객·수주·납품·서비스 매출 없으면 Green 금지.

3. 폐기물처리는 허가권·처리시설·반복 FCF가 있으면 Green 가능.
   폐배터리/재활용 테마만 있으면 Watch.

4. 보안/딥페이크는 규제 수요는 강하지만,
   CrowdStrike 같은 운영 신뢰 리스크가 hard 4C.

5. 클라우드/ERP는 반복매출·OPM·FCF가 있으면 Green 가능.
   AI 기능만 있으면 Watch.

6. 교육은 저출산과 규제 리스크 때문에 Watch 중심.
   성인교육/해외/반복매출이 있어야 Green 가능.

7. 의류는 K브랜드라도 재고/할인율/단일채널 리스크가 커서 Watch 중심.

8. 건자재/리츠는 금리·PF·공실·배당 안정성이 핵심.
   부동산 회복 테마만으로 Green 금지.

9. CRO는 CDMO보다 약하지만 실제 수주·고객 다변화가 있으면 Watch-to-Green 가능.
```

---

# 12. 이제 얼마나 채워졌나

현재 기준으로 보면:

```text
테마 흡수:
거의 95% 이상 구조화 가능

대섹터:
12개로 충분히 커버 가능

Archetype/sub-archetype:
70개 안팎 필요

점수정규화:
주요 archetype은 방향 잡힘
얇았던 archetype 일부 보강됨

아직 필요한 것:
각 case별 price path validation
성공 2개 + 반례 2개 coverage audit
shadow scoring
```

즉, 이제 “테마가 빠져서 못 본다”는 문제는 많이 줄었고, 다음 문제는 **각 archetype의 점수비중이 실제 주가·EPS 경로와 맞는지**야.

---

# 13. 다음에 해야 할 작업

다음 라운드는 이제 진짜로 아래 두 가지 중 하나로 가면 돼.

```text
A. cases_v04 후보를 더 확장
   - 이번 라운드의 under-covered archetype별 성공/반례 추가

B. theme_tag_map_v05를 더 압축된 CSV 형태로 정리
   - raw_theme_tag
   - primary_archetype
   - green_policy
   - must_have_evidence
   - red_flag_evidence
```

지금은 꽤 많이 채워졌지만, **production scoring은 아직 안 된다.**
이제부터는 에이전트가 price path를 채우고, shadow score와 실제 MFE/MAE를 비교해야 한다.

[1]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[2]: https://www.reuters.com/business/ecolab-acquire-coolit-systems-475-billion-2026-03-20/?utm_source=chatgpt.com "Ecolab to buy CoolIT for $4.75 billion to tap into AI data center boom"
[3]: https://www.reuters.com/markets/deals/samsung-electronics-buy-flktgroup-15-bln-euro-2025-05-13/?utm_source=chatgpt.com "Samsung to buy German cooling system maker FlaktGroup for $1.7 billion"
[4]: https://www.reuters.com/markets/deals/eqt-strikes-deal-acquire-south-korean-waste-treatment-platform-2024-08-16/?utm_source=chatgpt.com "EQT strikes deal to acquire South Korean waste treatment platform"
[5]: https://www.reuters.com/world/asia-pacific/south-korea-criminalise-watching-or-possessing-sexually-explicit-deepfakes-2024-09-26/?utm_source=chatgpt.com "South Korea to criminalise watching or possessing sexually explicit deepfakes"
[6]: https://www.reuters.com/legal/crowdstrike-is-sued-by-shareholders-over-huge-software-outage-2024-07-31/?utm_source=chatgpt.com "CrowdStrike is sued by shareholders over huge software outage"
[7]: https://www.reuters.com/world/asia-pacific/swedish-firm-eqt-shells-out-930-million-slice-south-koreas-douzone-bizon-2025-11-07/?utm_source=chatgpt.com "Swedish firm EQT shells out $930 million for a slice of South Korea's Douzone Bizon"
[8]: https://www.ft.com/content/4babaa33-5ad8-4290-b7d3-835165ed8091?utm_source=chatgpt.com "South Korea's academic race pushes half of under-6s into 'cram' schools"
