좋아. 순서상 이번은 **R12 Loop 7 — 농업·생활서비스·기타 가격경로 검증 라운드**로 진행한다.

이번 R12는 앞선 R5 소비재와 조금 닮았지만, 더 산발적이다. 스마트팜, 농기계, 교육, 렌탈, 키오스크, 규제 소비재, 축산 질병 이벤트가 한 바구니에 들어와서 **테마는 많지만 Stage 3-Green은 드물다.** R12에서 진짜 E2R이 되려면 반복매출, unit economics, 규제 통과, 가동률, 해외 판매, 현금전환이 확인되어야 한다.

---

# 1. 이번 라운드 대섹터

```text
R12 = 농업·생활서비스·기타
large_sector = EDUCATION_LIFE_AGRI_MISC
round = R12 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R12의 기본 영역은 스마트팜, 농기계, 종자·비료·농약, 양돈·육계, 동물백신, 교육, 키즈·유아용품, 생활가전 렌탈, 키오스크, 전자담배·주정 같은 규제 소비재다. Round 40 기준 R12 validation focus는 `commercial_installation`, `recurring_service`, `disease_event`, `repeat_course`, `churn`, `regulatory_approval`이다. 

Round 119 기준으로 R12에서 부족한 증거는 `defensive_theme`, `education_policy`, `agri_cycle`이고, 필요한 증거는 `recurring_revenue`, `unit_economics`, `regulatory_pass`, `cash_conversion`이다. Green blocker는 `policy_cap`, `commodity_reversal`, `one_off_disease_event`다. 

---

# 2. 대상 canonical archetype

```text
SMART_FARM_AGRI_TECH
AGRI_MACHINERY_DEMAND_CYCLE
AGRI_MACHINERY_SOFTWARE_LOCKIN
AGRI_LIVESTOCK_FOOD_COMMODITY
LIVESTOCK_DISEASE_PRICE_REGULATORY
AGRI_DISEASE_EVENT_OVERLAY
ANIMAL_HEALTH_BIOSECURITY
EDUCATION_SPECIALTY_SERVICES
HOME_CHILD_EDUCATION
EDTECH_AI_DISRUPTION
HOME_LIVING_APPLIANCE_RENTAL
SERVICE_KIOSK_SELF_CHECKOUT
CONSUMER_REGULATED_PRODUCT
NICOTINE_ALTERNATIVE_REGULATED
REGULATED_CONSUMER_APPROVAL_OVERLAY
```

이번 R12의 핵심 질문은 이거다.

```text
이 회사는 농업·교육·렌탈·규제소비재 테마주인가?
아니면 반복매출, 설치대수, 해외판매, 가동률, unit economics, 규제 통과가
실제로 EPS/FCF 체급을 바꾸는 회사인가?
```

---

# 3. deep sub-archetype

```text
생활가전 렌탈:
- Coway
- water purifier rental
- air purifier / bidet / mattress rental
- Malaysia / overseas subsidiaries
- recurring account base
- churn
- ARPU
- service network
- product safety / recall risk

농기계 / 스마트농업:
- Daedong / KIOTI
- TYM
- tractors / combines / utility vehicles
- North America dealer channel
- autonomous tractor / precision agriculture
- export cycle
- farmer financing
- inventory / dealer stocking risk

교육:
- MegaStudy Education
- medical school quota policy
- cram school demand
- repeat course
- policy cap
- birth-rate structural decline
- mobile-phone ban / classroom regulation
- AI education disruption

축산 / 질병 이벤트:
- Harim / Maniker류 poultry basket
- Brazil bird flu
- import restriction
- one-off poultry price event
- feed cost
- inventory
- policy reversal

규제 소비재:
- KT&G
- cigarettes
- heated tobacco
- ginseng / KGC
- regulation / youth-safety
- global distribution
- shareholder return
- volume decline vs pricing power

키오스크 / 생활서비스:
- self-checkout
- unmanned store
- minimum wage / labor cost
- local regulation
- merchant churn
- payment integration
```

---

# 4. 국장 신규 후보 case

## Case A — 코웨이 `structural_success 후보 / rental recurring revenue`

```text
symbol = 021240
archetype = HOME_LIVING_APPLIANCE_RENTAL
case_type = structural_success 후보
```

코웨이는 R12에서 가장 E2R에 가까운 케이스다. 이유는 단순 생활가전 제조가 아니라 정수기·공기청정기·비데·매트리스 렌탈 기반의 반복매출 구조이기 때문이다. 공개 요약 기준 코웨이는 국내 최대 정수기 회사이고, 말레이시아·미국·태국·인도네시아 등 해외 법인을 갖고 있으며, 말레이시아 법인이 해외 매출의 큰 비중을 차지하는 구조로 정리되어 있다. 다만 현재 pass에서는 최신 DART/IR 숫자까지 직접 검증하지 못했기 때문에, Stage 3 확정은 보류한다. ([위키백과][1])

### stage date 후보

```text
Stage 1:
2022~2024
- 렌탈 계정 기반 반복매출
- 말레이시아 등 해외 렌탈 확장
- 생활가전 서비스 플랫폼화

Stage 2:
DART/IR backfill 필요
- 해외 계정 증가
- 렌탈 ARPU
- 해지율/churn
- OPM/FCF 확인 필요

Stage 3:
조건부 후보
- recurring revenue + churn 안정 + 해외 성장 + FCF conversion 확인 시 가능

Stage 4B:
렌탈 안정성만으로 valuation이 과도하게 확장되면 후보

Stage 4C:
제품 안전 리콜, 해외 성장 둔화, churn 상승, Netmarble 지배구조/자본배분 훼손 시 후보
```

### 가격경로 검증

```text
stage3_price:
최신 실적/IR에서 Stage 3 evidence date 확정 후 backfill 필요.

MFE_30D / 90D / 180D / 1Y / 2Y:
needs_ohlc_backfill

MAE_30D / 90D / 180D / 1Y:
needs_ohlc_backfill

below_stage3_price_flag:
needs_ohlc_backfill

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = recurring_service_rerating_candidate
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

코웨이는 R12에서 `recurring_revenue`, `churn`, `ARPU`, `cash_conversion`, `overseas_account_growth`를 올려주는 케이스다. 다만 Stage 3는 브랜드 안정성이 아니라 **계정 증가와 FCF**에서 나와야 한다.

---

## Case B — 대동 / TYM `success_candidate / agri machinery export watch`

```text
symbols = 000490 / 002900
archetype = AGRI_MACHINERY_DEMAND_CYCLE / AGRI_MACHINERY_SOFTWARE_LOCKIN
case_type = success_candidate / insufficient_evidence
```

대동과 TYM은 R12 농기계 축의 대표 국장 후보지만, 이번 pass에서는 Stage 3를 줄 수 없다. 공개 요약 기준 대동은 KIOTI 브랜드로 알려진 한국 농기계 기업이고 트랙터·콤바인·엔진 등을 생산한다. TYM도 트랙터·콤바인·경운기·이앙기 등을 생산하고 40개국 이상에서 사업을 하는 농기계 기업으로 정리되어 있다. 이 정도는 R12 attention으로 충분하지만, Stage 3에는 북미 딜러 판매, 재고, 금융조건, OPM, FCF, 자율주행/정밀농업 매출이 필요하다. ([위키백과][2])

### stage date 후보

```text
Stage 1:
2023~2025
- 북미 농기계 수출
- KIOTI / TYM tractor channel
- 스마트농업 / 자율주행 농기계 기대

Stage 2:
보류
- 회사별 수출계약, 딜러 재고, 북미 판매량, OPM 확인 필요

Stage 3:
없음
- 농기계 export theme만으로 Green 금지

Stage 4B:
북미 농기계 수요 회복/자율주행 테마로 주가가 먼저 급등하면 후보

Stage 4C:
미국 농가 수요 둔화, 딜러 재고 증가, 금융조건 악화, 농산물 가격 하락 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
농기계 수출/자율주행 테마 발생일별 backfill 필요.

MFE / MAE:
theme basket 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = unknown_insufficient_evidence
rerating_result = agri_machinery_watch
stage_failure_type = stage1_attention_only
```

### 교정 포인트

R12 농기계는 `export_growth`보다 `dealer sell-through`, `inventory`, `financing`, `OPM`, `software/precision agriculture attachment`를 봐야 한다.

---

## Case C — 메가스터디교육 `event_premium / education policy watch`

```text
symbol = 215200
archetype = EDUCATION_SPECIALTY_SERVICES / HOME_CHILD_EDUCATION
case_type = event_premium / policy_watch
```

메가스터디교육은 의대 증원·입시정책 이벤트에 민감한 교육주로 볼 수 있다. 2024~2025년 한국 정부의 의대 정원 확대 정책은 학원·입시 시장의 기대를 키울 수 있었지만, 정책이 수차례 조정되면서 단순 policy event만으로 Stage 3를 주면 안 된다. 2025년 3월 Reuters는 정부가 13개월간 이어진 의료계 갈등을 끝내기 위해 2026학년도 의대 정원을 기존 약 3,000명 수준으로 동결할 수 있다고 보도했다. ([Reuters][3])

또 2026년 2월 AP는 한국 정부가 2027~2031년 의대 정원을 늘리되, 2027년 3,548명에서 2031년 3,871명으로 가는 비교적 완만한 증가 계획을 발표했다고 보도했다. 이는 2024년의 연 2,000명 증원안보다 훨씬 완만한 정책이다. 즉 교육주는 의대정원 테마로 움직일 수 있지만, 정책 경로가 자주 바뀌므로 Stage 3는 **repeat course 매출과 margin**으로만 줘야 한다. ([AP News][4])

### stage date 후보

```text
Stage 1:
2024-02 이후
- 의대 정원 확대 정책
- 의대 입시 사교육 수요 기대

Stage 2:
2024~2026 정책 확정/조정 이벤트별로 분리
- 2025-03-07 정원 동결 가능성
- 2026-02-10 완만한 정원 확대 계획

Stage 3:
없음
- 정책 이벤트만으로 Green 금지
- 실제 수강생 증가, repeat course, ARPU, OPM 확인 필요

Stage 4B:
의대 증원 뉴스로 교육주가 먼저 급등하면 event premium 4B-watch

Stage 4C:
정책 후퇴, 정원 축소, 사교육 규제, 출생아 감소에 따른 장기 수요 훼손 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
의대 증원 발표일별 OHLC backfill 필요.

MFE_5D / 20D / 60D:
education policy event 검증용.

MAE_30D / 90D:
정책 조정/후퇴 후 event fade 확인.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = event_premium / unknown_insufficient_evidence
rerating_result = education_policy_watch
stage_failure_type = stage1_or_stage2_attention_only
```

### 교정 포인트

교육주는 정책이 강하게 보이더라도 Stage 3는 매출로만 준다.

```text
의대 정원 확대:
Stage 1~2

Stage 3 조건:
수강생 증가
repeat course
ARPU
OPM
cash conversion

Green blocker:
정책 후퇴
사교육 규제
학령인구 감소
```

---

## Case D — 교육/에듀테크 basket `4C-watch / AI·교실 규제`

```text
symbols = NE능률 / YBM넷 / 웅진씽크빅 등 교육·에듀테크 basket
archetype = EDTECH_AI_DISRUPTION / HOME_CHILD_EDUCATION
case_type = 4C-watch / policy_watch
```

R12 교육주는 의대정원 같은 호재뿐 아니라 정책·기술 변화의 역풍도 같이 봐야 한다. 2025년 8월 Reuters는 한국이 2026년 3월부터 학교 교실 내 휴대전화와 디지털기기 사용을 전국적으로 금지하는 법을 시행한다고 보도했다. 청소년 소셜미디어 과몰입 우려에 따른 조치이고, 장애·교육 필요 학생은 예외가 있을 수 있다. 이 이벤트는 오프라인 학습 discipline에는 긍정적으로 해석될 여지도 있지만, 에듀테크·디지털 학습 플랫폼에는 정책 friction이 될 수 있다. ([Reuters][5])

### stage date 후보

```text
Stage 1:
2025-08-27
- 교실 내 휴대전화·디지털기기 금지 법안
- 교육정책 변화 / 디지털 학습 friction

Stage 2:
없음
- 특정 상장사 매출 증가·감소 확인 전 정책 이벤트

Stage 3:
없음
- 정책 이벤트만으로 Green 금지

Stage 4B:
교육정책 뉴스로 교육주 basket이 급등하면 event premium

Stage 4C:
디지털 교재·에듀테크 사용 제한, AI 교육 disruption, 학령인구 감소가 매출 훼손으로 확인되면 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2025-08-27 교육 basket OHLC backfill 필요.

MFE / MAE:
policy event 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = unknown_insufficient_evidence
rerating_result = policy_watch
stage_failure_type = stage1_attention_only
```

### 교정 포인트

교육주는 `정책 방향`이 양날의 칼이다. R12에서는 교육정책을 score가 아니라 routing으로만 쓰고, 실제 수강생·ARPU·churn·margin을 요구해야 한다.

---

## Case E — 하림 / 마니커류 poultry basket `event_premium / one-off disease demand`

```text
symbols = Harim / Maniker류 poultry basket
archetype = LIVESTOCK_DISEASE_PRICE_REGULATORY / AGRI_DISEASE_EVENT_OVERLAY
case_type = event_premium / one_off
```

브라질 조류독감 이벤트는 R12 축산·질병 이벤트의 교과서다. 2025년 5월 브라질 상업농장에서 조류독감이 확인되자 중국·EU·한국 등 주요 수입국이 브라질산 닭고기에 수입제한을 걸었다. Reuters는 브라질이 세계 최대 닭고기 수출국이고, 한국도 초기에는 브라질산 닭고기 수입을 전국 단위로 제한했다고 보도했다. ([Reuters][6])

그러나 2025년 6월 한국은 브라질이 상업 농장 조류독감 청정 상태를 회복했다고 밝힌 뒤, 제한을 전국 단위에서 affected region 중심으로 완화했다. 즉 이 이벤트는 국내 poultry basket에 단기 MFE를 줄 수 있지만, R12 Stage 3가 아니라 **one-off disease event**다. ([Reuters][7])

### stage date 후보

```text
Stage 1:
2025-05-19
- 브라질 조류독감
- 한국 등 수입제한
- 국내 닭고기 가격/수급 기대

Stage 2:
보류
- 국내 업체별 판매가격, 출하량, 마진 확인 필요

Stage 3:
없음
- 질병 이벤트만으로 Green 금지

Stage 4B:
수입제한 뉴스로 poultry basket이 급등하면 4B-watch

Stage 4C:
2025-06-23
- 한국의 수입제한 완화
- one-off event fade
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2025-05-19 poultry basket OHLC backfill 필요.

MFE_5D / 20D / 60D:
disease event premium 검증용.

MAE_30D / 90D:
수입제한 완화 이후 event fade 확인.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = event_premium
rerating_result = one_off_disease_event
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### 교정 포인트

축산 질병 이벤트는 가격이 빠르게 반응하지만 반복 수요가 아니다.

```text
Stage 1:
질병 / 수입제한

Stage 3 조건:
국내 판매량 증가
가격전가
feed cost 통과
재고 안정
OPM 개선

Green blocker:
수입제한 완화
질병 청정 선언
사료비 상승
```

---

## Case F — KT&G `success_candidate / regulated consumer cashflow`

```text
symbol = 033780
archetype = CONSUMER_REGULATED_PRODUCT / NICOTINE_ALTERNATIVE_REGULATED
case_type = success_candidate / regulatory_watch
```

KT&G는 R12의 규제 소비재 축이다. 공개 요약 기준 KT&G는 한국의 대표 담배·인삼 기업이고, 담배 시장에서 Philip Morris, BAT, Japan Tobacco 등 글로벌 업체와 경쟁하는 구조로 정리된다. 안정적 현금흐름과 규제산업이라는 특성은 R12 Stage 2 후보가 될 수 있지만, Stage 3는 담배 판매량·가격 인상·해외 성장·HNB 전환·주주환원·규제 리스크를 확인해야 한다. ([위키백과][8])

### stage date 후보

```text
Stage 1:
2024~2025
- 방어주 / 규제소비재 / 주주환원 기대
- 궐련형 전자담배 / 해외 판매 기대

Stage 2:
보류
- 최신 DART/IR에서 주주환원, 해외매출, HNB 성장, OPM 확인 필요

Stage 3:
없음 또는 조건부 후보
- 반복현금흐름은 좋지만, regulatory risk와 volume decline 확인 전 Green 보류

Stage 4B:
방어주·고배당·주주환원 기대만으로 valuation이 확장되면 후보

Stage 4C:
담배세/규제 강화, 청소년 안전규제, 해외시장 부진, HNB 경쟁 심화 시 후보
```

### 가격경로 검증

```text
stage3_price:
최신 주주환원/실적 evidence date 확정 후 backfill 필요.

MFE / MAE:
needs_ohlc_backfill

below_stage3_price_flag:
needs_ohlc_backfill

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = regulated_cashflow_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

KT&G는 `regulated_cashflow`, `pricing_power`, `shareholder_return`을 올려줄 수 있지만, `volume_decline`, `youth_safety_regulation`, `HNB_competition`을 동시에 감점해야 한다.

---

## Case G — 스마트팜 / Green Plus·우듬지팜류 `insufficient_evidence`

```text
symbols = Green Plus / 우듬지팜류 스마트팜 basket
archetype = SMART_FARM_AGRI_TECH / VERTICAL_FARMING_UNIT_ECONOMICS
case_type = insufficient_evidence
```

스마트팜은 R12에서 장기적으로 중요한 테마지만, 이번 pass에서는 Stage 3를 줄 근거가 부족하다. 2025년 스마트팜 채택 연구는 한국 스마트팜 기술이 생산성·지속가능성 측면에서 주목받지만, 실제 채택은 농가 연령, 교육 수준, 농지 규모, 정부지원, 기술 장벽, 자금 부담에 영향을 받는다고 설명한다. 즉 스마트팜은 정책·기술 narrative는 강하지만, 상장사 단위 Stage 3에는 설치대수, 수주, 반복서비스, 유지보수 매출, unit economics가 필요하다. ([arXiv][9])

### stage date 후보

```text
Stage 1:
2024~2025
- 스마트팜 / AI 농업 / 청년농 정책
- 농업 자동화 기대

Stage 2:
보류
- 회사별 상업 설치, 수주, 유지보수 매출 확인 필요

Stage 3:
없음
- 스마트팜 정책·기술 논문만으로 Green 금지

Stage 4B:
스마트팜 테마주가 정책/AI농업 뉴스로 먼저 급등하면 후보

Stage 4C:
설치 지연, unit economics 실패, 정부보조 축소, 농가 채택률 부진 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
스마트팜 정책/테마 발생일별 backfill 필요.

MFE / MAE:
theme basket 기준 backfill 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = unknown_insufficient_evidence
rerating_result = smart_farm_policy_watch
stage_failure_type = stage1_attention_only
```

### 교정 포인트

스마트팜은 R12에서 stage를 늦게 줘야 한다.

```text
정책/AI농업:
Stage 1

Stage 2:
상업 설치
수주
농가 채택
유지보수 계약

Stage 3:
반복서비스
unit economics
FCF
보조금 의존도 낮음
```

---

# 5. 이번 R12 case별 요약표

| case                  | 분류                                   | Stage 3 판정 |                  4B/4C 판정 | 가격경로 1차 판단                             |
| --------------------- | ------------------------------------ | ---------: | ------------------------: | -------------------------------------- |
| 코웨이                   | structural_success 후보                |     조건부 가능 | 리콜/churn/해외 둔화 시 4C-watch | 렌탈 반복매출은 R12에서 가장 강한 구조                |
| 대동/TYM                | success_candidate / insufficient     |         없음 |      농기계 수요 둔화 시 4C-watch | export/자율주행은 Stage 1~2, 재고·OPM 확인 필요   |
| 메가스터디교육               | event_premium / policy watch         |         없음 |              정책 후퇴 시 fade | 의대정원 정책은 Stage 1~2, 수강생·OPM 전 Green 금지 |
| 교육/에듀테크 basket        | 4C-watch / policy watch              |         없음 |        교실 디지털기기 규제는 watch | 정책 방향이 양날의 칼                           |
| Harim/Maniker poultry | event_premium / one-off              |         없음 |    수입제한 완화가 4C/event fade | 질병 이벤트는 단기 MFE용                        |
| KT&G                  | success_candidate / regulatory watch |     조건부 보류 |   규제·volume decline watch | 현금흐름은 좋지만 규제와 HNB 경쟁 확인 필요             |
| 스마트팜 basket           | insufficient_evidence                |         없음 |       정책 테마 과열 시 4B-watch | 설치·수주·unit economics 전 Green 금지        |

---

# 6. 각 case별 stage date 후보 요약

```text
코웨이:
Stage 1 = 렌탈 반복매출 / 해외법인 성장
Stage 2 = 최신 DART/IR 계정·ARPU·churn 확인 후 확정
Stage 3 = 조건부 후보 / recurring revenue + FCF 확인 필요
Stage 4B = 렌탈 안정성 valuation 과열 시 후보
Stage 4C = 제품안전·churn·해외성장 둔화 시 후보

대동/TYM:
Stage 1 = 농기계 수출 / 자율주행 농기계 기대
Stage 2 = 보류 / 북미 딜러 판매·재고·OPM 확인 필요
Stage 3 = 없음
Stage 4B = 자율주행/수출 테마 급등 시 후보
Stage 4C = 농가 수요 둔화·딜러 재고 증가·금융조건 악화 시 후보

메가스터디교육:
Stage 1 = 의대정원 확대 정책
Stage 2 = 2025~2026 정원 조정·확정 이벤트
Stage 3 = 없음
Stage 4B = 의대 증원 뉴스 급등 시 후보
Stage 4C = 정책 후퇴·사교육 규제·학령인구 감소 시 후보

교육/에듀테크:
Stage 1 = 2025-08-27 교실 휴대전화·디지털기기 금지 법안
Stage 2 = 없음
Stage 3 = 없음
Stage 4B = 정책 뉴스 급등 시 후보
Stage 4C = 디지털 학습 플랫폼 매출 훼손 시 후보

Harim/Maniker:
Stage 1 = 2025-05-19 브라질 조류독감 / 한국 수입제한
Stage 2 = 보류 / 국내 업체 마진 확인 필요
Stage 3 = 없음
Stage 4B = 수입금지 뉴스 급등 시 후보
Stage 4C = 2025-06-23 한국 제한 완화

KT&G:
Stage 1 = 규제소비재 / HNB / 주주환원 기대
Stage 2 = 최신 실적·주주환원·HNB 매출 확인 후 확정
Stage 3 = 보류
Stage 4B = 방어주·고배당 과열 시 후보
Stage 4C = 담배규제·volume decline·HNB 경쟁 심화 시 후보

스마트팜 basket:
Stage 1 = AI농업 / 스마트팜 정책
Stage 2 = 보류 / 상업 설치·수주 확인 필요
Stage 3 = 없음
Stage 4B = 정책 테마 급등 시 후보
Stage 4C = unit economics 실패·정부보조 축소 시 후보
```

---

# 7. 가격경로 검증

R12는 정확한 OHLC backfill 없이 수익률을 확정하면 안 된다. 특히 교육·질병·스마트팜·농기계는 이벤트성 가격 반응이 많고, 코웨이·KT&G 같은 방어/반복매출주는 장기 가격경로를 별도로 봐야 한다.

| case          |           stage3_price | MFE/MAE                       | below_stage3   | peak/drawdown                    |
| ------------- | ---------------------: | ----------------------------- | -------------- | -------------------------------- |
| 코웨이           | 최신 IR evidence date 필요 | needs_ohlc_backfill           | needs backfill | rental rerating peak 필요          |
| 대동/TYM        |             Stage 3 없음 | export/theme 기준 backfill      | N/A            | agri machinery cycle drawdown 필요 |
| 메가스터디교육       |             Stage 3 없음 | 의대정원 정책별 MFE_5D/20D/60D       | N/A            | 정책 후퇴 fade 필요                    |
| 교육/에듀테크       |             Stage 3 없음 | phone-ban policy event 기준     | N/A            | event fade 필요                    |
| Harim/Maniker |             Stage 3 없음 | bird-flu event MFE_5D/20D/60D | N/A            | 수입제한 완화 이후 drawdown              |
| KT&G          | 최신 실적·주주환원 evidence 필요 | needs_ohlc_backfill           | needs backfill | regulated cashflow rerating peak |
| 스마트팜 basket   |             Stage 3 없음 | policy/theme 기준 backfill      | N/A            | theme fade 필요                    |

핵심은 이거다.

```text
R12에서 Stage 3는 테마가 아니라
반복매출·unit economics·규제 통과·현금전환이 확인되는 날짜다.
```

---

# 8. score-price alignment 판정

```text
코웨이:
alignment = success_candidate
R12에서 가장 구조적인 recurring-service 후보.
다만 최신 계정·churn·FCF backfill 필요.

대동/TYM:
alignment = unknown_insufficient_evidence
농기계 수출과 자율주행 테마는 attention.
딜러 sell-through / 재고 / OPM 전 Stage 3 금지.

메가스터디교육:
alignment = event_premium
의대정원 정책은 강한 이벤트지만, 수강생·ARPU 전 Stage 3 아님.

교육/에듀테크 basket:
alignment = policy_watch
교실 디지털기기 규제는 특정 회사 Green 증거가 아님.

Harim/Maniker:
alignment = event_premium
조류독감 수입제한은 one-off demand.
제한 완화 시 event fade.

KT&G:
alignment = success_candidate
규제소비재 cashflow는 좋지만, volume·HNB·규제 확인 전 Stage 3 보류.

스마트팜 basket:
alignment = unknown_insufficient_evidence
스마트팜은 장기 테마지만, 설치·수주·unit economics 전 Green 금지.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
recurring_revenue +5
churn_stability +5
ARPU_or_repeat_course +4
cash_conversion +5
unit_economics +5
commercial_installation +4
service_contract_visibility +4
dealer_sell_through +4
inventory_quality +4
regulatory_pass +4
pricing_power_after_input_cost +3
```

R12에서 가장 강한 건 “생활필수”가 아니라 **반복해서 결제되는 구조**다. 코웨이 렌탈처럼 고객이 계속 돈을 내고, churn이 낮고, 현금전환이 좋으면 R12에서 진짜 E2R 후보가 될 수 있다.

## 내릴 축

```text
defensive_theme_only -5
education_policy_only -5
agri_cycle_only -4
smart_farm_policy_only -5
disease_event_only -5
import_ban_event_only -4
unconfirmed_export_theme -3
dealer_inventory_unknown -4
subsidy_dependent_unit_economics -4
regulated_product_without_growth -3
```

R12는 방어주·정책주·질병주가 많아서, 테마 자체를 점수로 쓰면 false positive가 쌓인다.

## Green gate 강화 조건

R12 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. 반복매출 또는 반복구매 확인
2. churn / retention 안정
3. ARPU 또는 가격전가 확인
4. unit economics 확인
5. cash conversion 확인
6. 재고·매출채권 안정
7. 규제 리스크 통과
8. 보조금 의존도 낮음
9. 가격경로가 증거 이후 따라옴

금지:
정책 뉴스만 있음
질병 이벤트만 있음
수입금지 뉴스만 있음
스마트팜 테마만 있음
농기계 수출 테마만 있음
교육정책 기대만 있음
방어주라서 좋다는 논리만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
정책 뉴스로 교육/스마트팜/농기계주 급등
질병 이벤트로 poultry basket 급등
방어주·고배당 프레임만으로 valuation 확장
렌탈/규제소비재가 성장률보다 multiple이 먼저 오름
의대정원/사교육 정책 기대가 수강생 증가보다 먼저 가격에 반영

4B-elevated:
churn 상승
dealer inventory 증가
수입제한 완화
정책 후퇴
규제 강화
보조금 축소
성장률 둔화에도 valuation 유지

4B-graduated:
좋은 실적에도 주가 반응 둔화
정책/질병 이벤트가 반복돼도 MFE가 줄어듦
렌탈 계정 성장률이 normalize
```

## 4C hard gate 조건

```text
recall / product safety issue
churn spike
ARPU 하락
dealer inventory build
farmer financing stress
education policy reversal
private education regulation
birth-rate demand collapse
import ban reversal
disease event cleared
regulatory ban / youth-safety restriction
subsidy withdrawal
unit economics failure
cash conversion deterioration
```

---

# 10. shadow-only 기록

이번 R12 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
r12_default_stage3_bias = conservative_except_recurring_service
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_131.md
docs/checkpoints/checkpoint_28a_round131_r12_loop7_agri_life_misc_price_validation.md
src/e2r/sector/round131_r12_loop7_agri_life_misc.py
data/e2r_case_library/cases_r12_loop7_round131.jsonl
data/sector_taxonomy/score_weight_profiles_round131_r12_loop7_v7.csv
output/e2r_round131_r12_loop7_agri_life_misc/
```

---

# 이번 R12 Loop 7 결론

R12는 구조 후보가 있긴 하지만, 대부분 Stage 1~2에 머무른다.

```text
1. 코웨이는 R12에서 가장 좋은 recurring-service 후보가 될 수 있다.
   단, 계정·churn·ARPU·FCF backfill 전 Stage 3 확정은 보류한다.

2. 대동/TYM 농기계는 수출·자율주행 테마만으로 Green 금지다.
   dealer sell-through, 재고, OPM, farmer financing을 봐야 한다.

3. 메가스터디교육과 교육주는 정책 이벤트에 민감하지만,
   실제 수강생·ARPU·OPM 전 Stage 3가 아니다.

4. 조류독감·수입금지 같은 축산 이벤트는 one-off MFE용이다.
   수입제한 완화가 곧 event fade가 된다.

5. KT&G 같은 규제소비재는 cashflow 후보지만,
   volume decline, HNB 경쟁, 규제 리스크를 같이 봐야 한다.

6. 스마트팜은 장기 테마지만,
   상업 설치·수주·unit economics·반복서비스 전 Green 금지다.
```

한 문장으로 압축하면:

> **R12에서 진짜 Stage 3는 “농업·교육·생활서비스가 방어적이다”가 아니라, 반복매출·unit economics·규제 통과·현금전환이 확인되는 순간이다.**
> **R12는 코웨이 같은 recurring-service는 Green 후보가 될 수 있지만, 교육정책·질병·스마트팜·농기계 테마는 기본적으로 Watch/Event로 둬야 한다.**

[1]: https://en.wikipedia.org/wiki/Coway_%28company%29?utm_source=chatgpt.com "Coway (company)"
[2]: https://en.wikipedia.org/wiki/Daedong_%28company%29?utm_source=chatgpt.com "Daedong (company)"
[3]: https://www.reuters.com/world/asia-pacific/south-korea-prepared-freeze-new-medical-student-numbers-minister-says-2025-03-07/?utm_source=chatgpt.com "South Korea offers to freeze medical student numbers to resolve 13-month dispute"
[4]: https://apnews.com/article/5ad78e1ce91ed5c3dface44438dcb814?utm_source=chatgpt.com "South Korea will boost medical school admissions to tackle physician shortage"
[5]: https://www.reuters.com/business/media-telecom/south-korea-ban-mobile-phones-school-classrooms-2025-08-27/?utm_source=chatgpt.com "South Korea to ban mobile phones in school classrooms"
[6]: https://www.reuters.com/business/healthcare-pharmaceuticals/brazil-can-no-longer-export-poultry-meat-eu-due-bird-flu-2025-05-19/?utm_source=chatgpt.com "Brazil can no longer export poultry and meat to EU due to bird flu"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/iraq-removes-south-korea-eases-restrictions-import-brazil-chicken-meat-2025-06-23/?utm_source=chatgpt.com "Iraq removes, South Korea eases restrictions on import of Brazil chicken meat"
[8]: https://en.wikipedia.org/wiki/Korea_Tobacco_%26_Ginseng_Corporation?utm_source=chatgpt.com "Korea Tobacco & Ginseng Corporation"
[9]: https://arxiv.org/abs/2504.01795?utm_source=chatgpt.com "Factors Influencing Farmers' Motivation to Adopt Smart Farm Technology in South Korea"
