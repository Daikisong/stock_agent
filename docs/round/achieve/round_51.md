좋아. 정해둔 순서대로 이번은 **R11 — 정책·지정학·재난·이벤트**로 넘어간다.

R11은 거의 “Green 발굴 라운드”가 아니라 **false-positive 방어 라운드**다. 이쪽은 주가가 가장 빨리 튀지만, EPS/FCF가 가장 안 따라오는 구간이 많다. 업로드된 Theme Tag Map에서도 남북경협, DMZ, 개성공단, 금강산 관광, 지진, 폭염, 황사, 엠폭스, 빈대, 코로나, 초전도체, 맥신, 그래핀, 양자기술은 대부분 `Event/Red`, `Watch/Red`, `SPECULATIVE_SCIENCE_THEME`로 분류되어 있고, Stage 3-Green보다 RedTeam·4B 방어가 중요하다고 정리되어 있다.

서생원식으로 보면 R11의 핵심은 단순하다. **정책·재난·과학 뉴스가 아니라, EPS/FCF 체급 변화와 밸류에이션 프레임 변화가 실제로 확인되는가**를 봐야 한다. 사건이 아니라 구조를 사는 것이고, 이벤트로 오른 가격은 대부분 오래 머물지 않는다.

---

# R11. 정책·지정학·재난·이벤트

## 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11의 기본 구조는 이렇게 봐야 한다.

```text
정책 뉴스 / 지정학 이벤트 / 재난 / 전염병 / 과학 논문
→ 관련주 급등
→ 실제 계약·매출·반복수요·EPS가 없으면 대부분 event premium
→ 뉴스 소멸 또는 검증 실패 후 drawdown
```

R11에서 가장 중요한 문장은 이거다.

```text
이벤트는 Stage 1을 만들 수 있지만,
Stage 3-Green은 거의 만들지 못한다.
```

---

## 2. 대상 canonical archetype

| 구분              | canonical archetype                   | Green 정책        |
| --------------- | ------------------------------------- | --------------- |
| 남북경협·금강산·개성공단   | `NORTH_KOREA_POLICY_EVENT`            | Event/Red       |
| 우크라 재건·전후 복구    | `GEOPOLITICAL_RECONSTRUCTION`         | Event/Watch     |
| 재난복구·지진·홍수      | `DISASTER_REBUILD_EVENT`              | Event/Watch     |
| 폭염·전력수요·냉각      | `CLIMATE_DISASTER_EVENT`              | Watch           |
| 황사·미세먼지         | `CLIMATE_DISASTER_EVENT`              | Event/Watch     |
| 엠폭스·코로나·전염병     | `EVENT_DISEASE_PEST_DEMAND`           | Event/Red       |
| 전염병 진단키트        | `DIAGNOSTICS_INFECTIOUS_EVENT`        | Event/Red       |
| 빈대·해충·방역        | `EVENT_DISEASE_PEST_DEMAND`           | Event/Red       |
| 초전도체·맥신·그래핀     | `SPECULATIVE_SCIENCE_THEME`           | Red             |
| 양자·페라이트·고급소재 테마 | `ADVANCED_MATERIAL_SPECULATIVE_THEME` | Watch/Red       |
| 세종시·지역화폐·정책 테마  | `POLICY_LOCAL_THEME`                  | Event           |
| 뉴스성 과열 전반       | `THEME_VALUATION_OVERHEAT`            | RedTeam overlay |

---

## 3. deep sub-archetype

```text
NORTH_KOREA_POLICY_EVENT
- 금강산 관광
- 개성공단
- DMZ
- 남북철도
- 북한 광물자원
- 남북 정상회담
- 제재 완화 기대
- 군사 긴장

GEOPOLITICAL_RECONSTRUCTION
- 우크라 재건
- 전후 인프라 복구
- 에너지망 복구
- 통신망 복구
- 지뢰 제거
- 병원·주거·공공 인프라

DISASTER_REBUILD_EVENT
- 지진
- 산불
- 홍수
- 태풍
- 건자재·복구 수요
- 보험·재건 비용

CLIMATE_DISASTER_EVENT
- 폭염
- 냉각수요
- 전력수요
- 에어컨
- 미세먼지
- 공기정화
- 마스크

EVENT_DISEASE_PEST_DEMAND
- 엠폭스
- 코로나
- 빈대
- 조류독감
- 진단키트
- 백신 stockpile
- 방역제
- 마스크

SPECULATIVE_SCIENCE_THEME
- 초전도체
- LK-99
- 맥신
- 그래핀
- 양자 소재
- 페라이트
- 상온초전도체
- 논문·preprint 기반 테마

POLICY_LOCAL_THEME
- 세종시
- 지역화폐
- 특정 지자체 이전
- 정책 수혜 기대
```

---

# 4. 성공사례

## 4-1. 엠폭스 백신 stockpile — `EVENT_DISEASE_PEST_DEMAND`

Bavarian Nordic는 엠폭스·천연두 백신 Jynneos의 동결건조 제형을 미국 정부에 공급하는 추가 계약 옵션 9,700만 달러를 받았고, 이에 따라 2026년 매출·EBITDA margin 전망을 상향했다. 이건 R11에서 보기 드문 “이벤트가 실제 정부계약·실적가이던스로 연결된” 사례다. 다만 이조차도 구조적 Green이라기보다는 **정부 stockpile 기반의 event-to-contract 후보**로 분류해야 한다. ([Reuters][1])

**가격경로 1차 판정**

```text
판정:
event_to_contract_success_candidate

좋은 점:
- 실제 정부 계약
- 매출 가이던스 상향
- EBITDA margin 상향
- stockpile 수요

주의:
- 전염병 이벤트 수요는 반복성이 약할 수 있음
- WHO emergency나 outbreak 뉴스만으로 Green 금지
- stockpile 계약이 다음 해에도 반복되는지 확인 필요
```

**점수 교정**

```text
EPS/FCF: 중간~강함
Structural Visibility: 낮음~중간
Bottleneck/Pricing: 중간
Market Mispricing: 낮음~중간
Valuation Rerating: 낮음
Risk: outbreak normalization, 정부 조달 종료, one-off demand
```

---

## 4-2. 엠폭스 emergency price path — `EVENT_DISEASE_PEST_DEMAND`

2024년 WHO의 엠폭스 국제보건비상사태 선언 이후 Bavarian Nordic 주가는 단기간 크게 반응했다. WSJ 보도 기준으로 주가는 하루 약 8% 상승했고, 그 주에는 28% 이상 상승했다. MarketWatch는 다음 날에도 주가가 19% 올라 5일간 51% 상승했다고 보도했다. 이건 R11의 전형적인 가격경로다. **뉴스 → 급등 → 이후 실제 주문·계약·실적가이던스 확인 여부로 갈림**이다. ([월스트리트저널][2])

**가격경로 1차 판정**

```text
가격 반응:
5일 +51% 보도

판정:
event_premium_with_contract_validation_needed

의미:
초기 급등은 event premium.
정부 주문·가이던스 상향이 붙으면 Stage 2로 승격 가능.
그렇지 않으면 one-off event.
```

---

## 4-3. 우크라 재건 — 실제 프로젝트가 붙으면 Stage 2 후보

우크라 재건은 대부분 Event/Watch지만, 실제 프로젝트·자금·회사명이 나오면 Stage 2 후보로 바뀔 수 있다. 스위스와 우크라이나는 2025년에 인프라, 대중교통, 의료, 인도적 지뢰 제거 등 12개 스위스 지원 재건 프로젝트를 공개했고, Geberit, Divario, Roche Diagnostics 같은 구체적 회사와 약 1억 스위스프랑 규모 지원이 언급됐다. ([Reuters][3])

**가격경로 1차 판정**

```text
판정:
reconstruction_project_stage2_reference

좋은 점:
- 실제 프로젝트
- 실제 자금
- 실제 참여 기업
- 인프라·의료·주거·지뢰제거 구체화

주의:
- 한국 재건 관련주로 직접 매핑하려면 실제 수주·계약·매출 확인 필요
- 단순 우크라 재건 테마는 Stage 1 event
```

**점수 교정**

```text
GEOPOLITICAL_RECONSTRUCTION:
정책 뉴스만 있으면 Event/Watch.
실제 계약·자금·공사·매출 인식이 있으면 Stage 2.
Stage 3는 다년 수주잔고와 마진 확인 전까지 금지.
```

---

## 4-4. 우크라 통신망 복구 — `GEOPOLITICAL_RECONSTRUCTION`

EBRD와 IFC는 우크라이나 신규 통합 통신회사에 4.35억 달러를 투자하기로 했다. 이 투자는 Lifecell과 Datagroup-Volia를 결합해 우크라이나의 두 번째 대형 통신사를 만들고, 네트워크 속도·커버리지·복원력을 높이는 데 쓰인다. 이건 “재건 테마”가 실제 금융기관 자금, 통신 인프라, 네트워크 복구로 연결된 사례다. ([Reuters][4])

**가격경로 1차 판정**

```text
판정:
real_reconstruction_financing_candidate

의미:
재건이 투자·대출·인프라 자산으로 구체화되면 Stage 2.
하지만 상장주 점수화는 수혜 회사의 계약·매출 연결 확인이 필요.
```

---

## 4-5. 폭염·냉각·전력수요 — `CLIMATE_DISASTER_EVENT`

폭염은 단순 “에어컨 테마”로 보면 이벤트지만, 전력망·냉각·수요관리로 연결되면 구조적 Watch가 된다. 2025년 연구는 독일에서 폭염 시 이동식 에어컨 보급률이 19%에서 35%로 늘면 피크 전력수요가 12.9GW 이상 증가할 수 있고, 오후 전력 피크와 태양광 발전 감소 시간이 겹쳐 전력계통 안정성 부담을 키울 수 있다고 분석했다. ([arXiv][5])

**가격경로 1차 판정**

```text
판정:
climate_event_to_grid_watch

의미:
폭염 자체는 Event.
하지만 전력망, 냉각, 수요반응, 변압기, ESS, HVAC로 연결되면 R1/R2/R3 archetype과 교차 가능.
```

**점수 교정**

```text
폭염 테마:
Stage 1 event.

전력수요·냉각·그리드 병목:
다른 대섹터의 구조적 증거와 연결될 때만 점수 상승.
```

---

# 5. 반례

## 5-1. 남북경협·금강산 관광 — `NORTH_KOREA_POLICY_EVENT`

남북경협은 거의 Event/Red다. 2025년 Reuters는 북한이 금강산 이산가족 상봉 시설을 철거하고 있다고 보도했고, 북한은 남한을 “적대국”으로 규정했으며, 2024년에는 남북 도로·철도 일부를 폭파했다. 이런 상황에서는 금강산 관광, 개성공단, 남북철도, DMZ 관련주는 실제 계약 전 Green을 절대 주면 안 된다. ([Reuters][6])

**교훈**

```text
남북경협 뉴스
≠ 구조적 Green

볼 것:
제재 완화
실제 계약
사업 재개
정부 승인
현금흐름

현재 기본값:
Event/Red
```

**가격경로 1차 판정**

```text
판정:
north_korea_policy_event_red_bias

의미:
회담·관광 재개 기대가 주가를 움직여도 대부분 event premium.
군사·정책 리스크가 항상 hard 4C.
```

---

## 5-2. LK-99 초전도체 — `SPECULATIVE_SCIENCE_THEME`

LK-99는 R11에서 반드시 넣어야 할 대표 반례다. 2023년 한국 연구진이 상온·상압 초전도체라고 주장한 preprint가 나오며 전 세계적으로 관심이 폭발했고 관련주가 급등했지만, 여러 재현 연구는 초전도성 증거를 관찰하지 못했다. 한 arXiv 재현 연구는 LK-99 샘플에서 초전도 신호를 찾지 못했다고 보고했고, 후속 연구는 Cu₂S 불순물이 초전도처럼 보이는 현상을 만들 수 있다고 분석했다. ([arXiv][7])

**교훈**

```text
논문·preprint
≠ 매출
≠ EPS
≠ Green

초전도체·맥신·그래핀·양자 소재는:
실제 제품
고객사
계약
매출
OP/FCF
전까지 Green 금지.
```

**가격경로 1차 판정**

```text
판정:
speculative_science_hard_counterexample

의미:
주가가 크게 움직였어도 price_moved_without_evidence.
실제 상용화와 재무 증거가 없으면 Stage 3 금지.
```

---

## 5-3. 전염병 진단키트 one-off — `DIAGNOSTICS_INFECTIOUS_EVENT`

전염병 진단은 EPS가 폭발할 수 있지만 지속성이 약하다. COVID 진단 수요가 줄자 Abbott은 COVID 검사 매출 감소와 진단기기 수요 약화로 주가가 하락했고, 2025년 3분기에도 diagnostics segment 매출이 6.6% 감소했다. 이건 진단키트가 전염병 이벤트에서는 강하지만, 정상화 이후 EPS가 급격히 꺾일 수 있음을 보여준다. ([Reuters][8])

**교훈**

```text
전염병 진단 매출
≠ 구조적 Green

Green이 되려면:
설치기반
다양한 검사 메뉴
반복 진단 수요
비전염병 매출
이 필요하다.
```

---

## 5-4. 재난복구·건자재 이벤트

산불·지진·홍수 이후 건자재·복구 수요가 생길 수 있지만, 대부분은 지역적·일회성이다. 2025년 Southern California 산불 이후 James Hardie가 Habitat for Humanity와 협력해 fire-resistant building materials를 기부한다는 사례는 재난 이후 복구 수요가 생긴다는 점을 보여주지만, 이것만으로 상장 건자재 기업의 구조적 Green을 만들지는 않는다. ([Veranda][9])

**교훈**

```text
재난복구 수요
≠ 구조적 EPS 체급 변화

Stage 2가 되려면:
보험금
정부 재건예산
실제 공급계약
물량·마진
반복 수요
가 확인되어야 함.
```

---

## 5-5. 정책·지역 테마 — `POLICY_LOCAL_THEME`

세종시, 지역화폐, 특정 기관 이전, 지방 개발 정책 같은 테마는 대부분 Stage 1 이벤트다. 정책이 실제 예산, 계약, 민간 투자, 매출로 연결되지 않으면 Green을 주면 안 된다.

**교훈**

```text
정책 발표
≠ 매출
≠ EPS

정책 테마는 기본값 Event.
```

---

# 6. 4B-watch 사례

## 6-1. 엠폭스 백신 급등 4B-watch

```text
4B 조건:
- WHO emergency 선언 직후 관련 백신주 급등
- 실제 정부 주문보다 기대가 먼저 반영
- 생산능력·가격·주문 지속성을 확인하지 않음
```

Bavarian Nordic는 엠폭스 뉴스로 5일 51% 상승한 가격반응이 확인됐다. 이후 정부계약과 가이던스 상향이 붙으면 Stage 2로 일부 승격되지만, outbreak 자체는 언제든 정상화될 수 있다. ([마켓워치][10])

---

## 6-2. 우크라 재건 4B-watch

```text
4B 조건:
- 재건회의·지원선언만으로 관련주 동반 급등
- 실제 수주·금융약정·공사착수 없음
- 관련주가 과거 재건 테마로만 움직임
```

우크라 재건은 실제 프로젝트가 붙으면 Stage 2 후보가 되지만, 선언·MOU 단계에서는 event premium으로 둔다. ([Reuters][3])

---

## 6-3. 폭염·냉각 테마 4B-watch

```text
4B 조건:
- 폭염 뉴스 후 에어컨·전력·냉각 관련주 동반 급등
- 실제 판매량·전력망 투자·수주 없이 주가만 움직임
- 계절성 수요를 구조적 수요로 오판
```

폭염은 전력망 스트레스와 냉각수요를 키울 수 있지만, 개별 종목은 실제 수주·매출·OPM을 확인해야 한다. ([arXiv][5])

---

## 6-4. LK-99·초전도체 4B-watch

```text
4B 조건:
- preprint·영상·SNS만으로 관련주 급등
- 거래소 투자경고
- 재현 실패가 나오기 전 가격이 먼저 과열
```

LK-99는 중반 이후 재현 실패와 불순물 설명이 나오면서 speculative science theme의 핵심 4B/4C 기준 사례가 되었다. ([위키백과][11])

---

## 6-5. 남북경협 4B-watch

```text
4B 조건:
- 정상회담·관광 재개 기대만으로 주가 급등
- 제재·군사 리스크를 무시
- 실제 사업 재개 계약 없음
```

북한이 금강산 시설을 해체하고 남북 도로·철도 일부를 폭파한 사례는, 남북경협이 언제든 4C로 전환될 수 있음을 보여준다. ([Reuters][6])

---

# 7. 4C-thesis-break 사례

## 7-1. 남북관계 악화

```text
4C:
시설 철거
도로·철도 폭파
군사합의 파기
남한 적대국 규정
제재 강화
```

금강산 시설 철거와 남북 도로·철도 폭파는 남북경협 관련주 thesis break 조건이다. ([Reuters][6])

---

## 7-2. LK-99 재현 실패

```text
4C:
재현 실패
불순물 설명
상용화 부재
실제 계약·매출 없음
```

LK-99는 초전도체 관련주를 구조적 후보가 아니라 `SPECULATIVE_SCIENCE_THEME`로 고정해야 하는 대표 사례다. ([arXiv][7])

---

## 7-3. 전염병 수요 정상화

```text
4C:
검사 수요 급감
정부 구매 종료
진단 매출 감소
재고 증가
EPS 정상화
```

COVID 검사 수요 약화로 Abbott의 diagnostics 매출이 감소한 사례는, 진단키트 one-off 구조를 보여준다. ([Reuters][8])

---

## 7-4. 재건 financing failure

```text
4C-watch:
재건 프로젝트 financing 지연
정치·전쟁 리스크
보험·보증 부족
실제 착공 지연
```

우크라 재건은 실제 프로젝트와 금융이 붙어야 Stage 2가 되며, 선언만 있으면 이벤트다. EBRD·IFC의 우크라이나 통신 투자처럼 구체적 자금·자산·회사명이 있어야 검증 대상이 된다. ([Reuters][4])

---

## 7-5. 재난복구 one-off

```text
4C-watch:
재난 후 수요 단기 집중
보험금 지연
정부예산 지연
기부·지원으로 매출화 안 됨
```

산불 이후 복구 소재 기부 같은 사례는 사회적으로 의미가 있지만, 기업 EPS 구조 변화와는 별개로 볼 수 있다. ([Veranda][9])

---

# 8. 점수비중 보정표 — R11 v1.0

| canonical archetype                   | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | 핵심 감점                            |
| ------------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | ------: | ---: | -------------------------------- |
| `NORTH_KOREA_POLICY_EVENT`            |       5 |          5 |          5 |          8 |         5 |       0 |    3 | 군사 리스크, 제재, 실제 계약 없음             |
| `GEOPOLITICAL_RECONSTRUCTION`         |      12 |         10 |          8 |         10 |         8 |       0 |    4 | financing, 전쟁 지속, 실제 수주 없음       |
| `DISASTER_REBUILD_EVENT`              |      10 |          6 |          7 |          8 |         6 |       0 |    4 | one-off 수요, 보험·예산 지연             |
| `CLIMATE_DISASTER_EVENT`              |      12 |         12 |         10 |         10 |         8 |       0 |    5 | 계절성, 일회성 수요, 매출화 불명확             |
| `EVENT_DISEASE_PEST_DEMAND`           |      12 |          8 |          8 |          8 |         6 |       0 |    5 | outbreak normalization, 정부 주문 종료 |
| `DIAGNOSTICS_INFECTIOUS_EVENT`        |      20 |          5 |          5 |          5 |         5 |       0 |    5 | one-off demand, 검사 수요 급감         |
| `SPECULATIVE_SCIENCE_THEME`           |       5 |          5 |          5 |          5 |         5 |       0 |    3 | 상용화 부재, 재현 실패                    |
| `ADVANCED_MATERIAL_SPECULATIVE_THEME` |       7 |          6 |          6 |          8 |         6 |       0 |    3 | 실제 제품·고객·매출 부재                   |
| `POLICY_LOCAL_THEME`                  |       5 |          5 |          5 |          8 |         5 |       0 |    3 | 정책 의존, 예산·계약 부재                  |
| `ONE_OFF_EVENT_DEMAND`                |       8 |          5 |          5 |          6 |         5 |       0 |    4 | 지속성 부족, 수요 정상화                   |
| `THEME_VALUATION_OVERHEAT`            |    gate |       gate |       gate |       gate |      gate |    gate | gate | price-only rally, 증거 없는 급등       |

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
실제 프로젝트, 자금, 참여기업, 계약금액, 공사착수 확인

Stage 3:
다년 매출·마진·수주잔고가 확인된 경우만

Stage 4B:
재건 테마 동반 과열

Stage 4C:
전쟁 재격화, financing 실패, 보험·보증 부재, 착공 지연
```

## `CLIMATE_DISASTER_EVENT`

```text
Stage 1:
폭염·한파·황사·산불·홍수 뉴스

Stage 2:
실제 제품 판매 증가, 전력망 투자, 복구 계약, 냉각 수주 확인

Stage 3:
반복 수요와 구조적 설비투자로 연결될 때만

Stage 4B:
계절성 테마 급등

Stage 4C:
수요 정상화, 기상 이벤트 소멸, 재고 증가
```

## `EVENT_DISEASE_PEST_DEMAND`

```text
Stage 1:
WHO emergency, 정부 방역 강화, outbreak 뉴스

Stage 2:
정부 주문, stockpile 계약, 매출 가이던스 상향 확인

Stage 3:
반복 조달·상시 수요가 확인된 경우만

Stage 4B:
전염병 뉴스 후 관련주 동반 과열

Stage 4C:
outbreak 정상화, 정부 구매 종료, 수요 급감
```

## `SPECULATIVE_SCIENCE_THEME`

```text
Stage 1:
preprint, 논문, 영상, SNS, 학회 발표

Stage 2:
실제 제품, 고객사 테스트, 계약, 매출 확인 시에만

Stage 3:
상용 고객 + 반복 매출 + EPS/FCF 전환 전까지 금지

Stage 4B:
논문·SNS만으로 관련주 급등

Stage 4C:
재현 실패, 상용화 실패, 불순물 설명, 거래소 투자경고
```

## `POLICY_LOCAL_THEME`

```text
Stage 1:
정책 발표, 이전 계획, 지역 개발 뉴스

Stage 2:
예산 배정, 실제 계약, 공사 착수, 매출 확인

Stage 3:
극히 제한적. 다년 매출·수익성 확인 필요

Stage 4B:
정책 테마 동반 급등

Stage 4C:
정책 철회, 예산 삭감, 사업 지연
```

---

# 10. 가격경로 검증계획

## R11 공통 검증 방식

```text
1. 각 case의 stage1_date, stage2_date, stage3_date를 지정한다.
2. stage1 event 발생일의 종가를 저장한다.
3. MFE_5D / 20D / 60D / 90D / 180D를 계산한다.
4. MAE_5D / 20D / 60D / 90D / 180D를 계산한다.
5. peak_price와 drawdown_after_peak를 계산한다.
6. 실제 계약·매출·EPS evidence가 있는지 확인한다.
7. 없으면 price_moved_without_evidence 또는 event_premium으로 분류한다.
```

## R11에서 반드시 분리할 판정

```text
event_premium:
뉴스로 주가가 올랐지만 실제 매출·계약 없음.

event_to_contract:
이벤트가 실제 정부계약·발주·매출로 이어짐.

price_moved_without_evidence:
논문·정책·SNS만으로 주가가 움직임.

speculative_science_failure:
재현 실패 또는 상용화 부재로 thesis break.

one_off_revenue:
매출은 있었지만 다음 해 정상화.

policy_relief_only:
정책은 있었지만 예산·계약·공사 없음.

thesis_break:
제재 강화, 군사 긴장, 계약 취소, 수요 종료, 재현 실패.
```

## 이번 R11에서 우선 검증할 가격 case

| case_id                                      |    stage2 후보일 | 현재 1차 가격판정                        |
| -------------------------------------------- | ------------: | --------------------------------- |
| `bavarian_nordic_mpox_emergency_case`        | 2024-08-15~16 | 5일 +51%, event premium            |
| `bavarian_nordic_us_stockpile_contract_case` |    2026-05-11 | 정부계약 + 가이던스 상향, event-to-contract |
| `north_korea_kumgang_dismantle_case`         |    2025-02-13 | 남북경협 hard Red                     |
| `ukraine_swiss_reconstruction_projects_case` |    2025-08-28 | 실제 프로젝트, Stage 2 reference        |
| `ukraine_telecom_ebrd_ifc_case`              |    2024-10-10 | 실제 금융투자, Stage 2 reference        |
| `lk99_superconductor_theme_case`             |    2023-07~08 | speculative science failure       |
| `lk99_replication_failure_case`              |       2023-08 | 4C thesis break                   |
| `covid_diagnostics_demand_wane_case`         |    2025-10-15 | diagnostics one-off normalization |
| `heatwave_ac_grid_stress_case`               |    2025 study | climate event → grid watch        |
| `california_wildfire_rebuild_material_case`  |       2026-04 | disaster rebuild event, one-off   |
| `local_policy_theme_case`                    |         case별 | 예산·계약 전 Green 금지                  |

---

# 11. 다음에 에이전트가 채워야 할 price fields

R11 case library에는 아래 필드가 필요하다.

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

event_type
policy_event_flag
geopolitical_event_flag
disaster_event_flag
disease_event_flag
science_preprint_flag

actual_contract_flag
contract_value
government_order_flag
stockpile_contract_flag
project_financing_flag
budget_allocated_flag
construction_started_flag
revenue_recognized_flag

outbreak_status
government_purchase_amount
diagnostic_sales_change
vaccine_order_doses
demand_normalization_flag

replication_success_flag
replication_failure_flag
peer_review_status
commercial_product_flag
customer_contract_flag

sanctions_status
military_tension_flag
tourism_reopen_flag
facility_dismantle_flag
road_rail_destroyed_flag

rebuild_project_count
rebuild_budget_amount
insurance_payout_status
one_off_demand_flag

score_price_alignment
price_validation_status
```

---

# R11 결론

R11은 거의 전부 **Stage 1 이벤트 필터링 라운드**다. 여기서 중요한 건 좋은 종목을 고르는 것보다, **이벤트성 급등을 구조적 E2R로 착각하지 않는 것**이다.

```text
Green 가능성이 매우 제한적인 경우:
- 전염병 이벤트가 실제 정부 stockpile 계약과 반복 매출로 이어지는 경우
- 우크라 재건이 실제 프로젝트·자금·계약·공사로 연결되는 경우
- 폭염·재난이 다른 대섹터의 구조적 수요, 예를 들어 전력망·냉각·수처리로 연결되는 경우

대부분 Event/Watch:
- 우크라 재건 선언
- 폭염·황사·재난복구
- 지역 정책
- 전염병 방역
- 진단키트

Red/4C 방어 중심:
- 남북경협
- 금강산·개성공단
- 초전도체·LK-99
- 맥신·그래핀
- NFT식 과학 테마
- 전염병 one-off 진단
- 정책 발표만 있는 테마
```

**R11 점수정규화의 핵심 문장:**

> 정책·지정학·재난·이벤트는 “뉴스가 크다”가 아니라 **실제 계약, 예산, 정부 주문, 반복 매출, EPS/FCF 전환이 있는지**로 봐야 한다.
> 그 증거가 없으면 대부분은 구조적 성공이 아니라 `event_premium`, `price_moved_without_evidence`, `one_off_revenue`, `speculative_science_failure`다.

다음에 네가 “다음 라운드 진행해줘”라고 하면, 정해둔 순서에 따라 **R12 — 농업·생활서비스·기타**로 넘어간다.

[1]: https://www.reuters.com/business/healthcare-pharmaceuticals/denmarks-bavarian-nordic-raises-2026-forecast-2026-05-11/?utm_source=chatgpt.com "Bavarian Nordic raises 2026 forecast on additional US vaccine contract"
[2]: https://www.wsj.com/health/healthcare/bavarian-nordics-shares-jump-on-mpox-outbreak-328a3497?utm_source=chatgpt.com "Bavarian Nordic's Shares Jump on Mpox Outbreak"
[3]: https://www.reuters.com/world/swiss-president-discusses-peace-reconstruction-with-ukrainian-pm-2025-08-28/?utm_source=chatgpt.com "Swiss president discusses peace, reconstruction with Ukrainian PM"
[4]: https://www.reuters.com/world/uk/ebrd-ifc-provide-435-mln-ukraines-newly-merged-telecoms-firm-2024-10-10/?utm_source=chatgpt.com "EBRD and IFC to provide $435 mln for Ukraine's newly merged telecoms firm"
[5]: https://arxiv.org/abs/2507.13534?utm_source=chatgpt.com "The impact of heatwave-driven air conditioning adoption on electricity demand: A spatio-temporal case study for Germany"
[6]: https://www.reuters.com/world/asia-pacific/north-korea-dismantling-facility-near-border-separated-families-seoul-says-2025-02-13/?utm_source=chatgpt.com "North Korea dismantling facility near border for separated families, Seoul says"
[7]: https://arxiv.org/abs/2308.03823?utm_source=chatgpt.com "Synthesis and characterisation of LK-99"
[8]: https://www.reuters.com/business/healthcare-pharmaceuticals/abbott-posts-higher-quarterly-revenue-strong-medical-device-demand-2025-10-15/?utm_source=chatgpt.com "Abbott revenue falls short of estimates on weak demand for diagnostic devices"
[9]: https://www.veranda.com/home-decorators/a70945529/james-hardie-habitat-for-humanity-wildfires-homes/?utm_source=chatgpt.com "James Hardie Teams Up With Habitat for Humanity to Rebuild Homes After Devastating 2025 California Wildfires"
[10]: https://www.marketwatch.com/story/mpox-vaccine-makers-stock-continues-to-surge-913d9b1a?utm_source=chatgpt.com "Mpox vaccine maker's stock continues to surge"
[11]: https://en.wikipedia.org/wiki/LK-99?utm_source=chatgpt.com "LK-99"
