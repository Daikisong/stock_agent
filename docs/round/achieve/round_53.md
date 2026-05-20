좋아. 이번은 정해둔 순서의 마지막인 **R13 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**로 간다.

R13은 새 섹터를 더 파는 라운드가 아니라, **R1~R12 전체에 공통으로 씌울 검증 규칙**을 고정하는 라운드다. 지금까지 12개 대섹터와 raw theme tag는 Theme Tag Map v0.5 기준으로 대부분 흡수됐고, R13은 그 위에 “이게 진짜 구조적 E2R인지, 아니면 테마·사이클·이벤트·회계 리스크인지”를 판별하는 마지막 계기판 역할을 한다.

서생원식 기준도 여기서 다시 고정한다. 에이전트가 찾아야 하는 것은 “오늘 오른 테마”가 아니라 **산업 구조 변화 → EPS/FCF 체급 변화 → 시장의 과거 프레임 오해 → 밸류에이션 리레이팅**이 실제로 연결되는 케이스다.

---

# R13. Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리

## 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
```

R13은 독립 산업섹터가 아니라, R1~R12 전체에 공통 적용되는 **상위 검증 레이어**다.

```text
R1~R12에서 후보 발생
→ Evidence / Score / Stage 산출
→ R13 RedTeam overlay 적용
→ 4B/4C/회계/가격경로 검증
→ aligned / false-positive / event / cycle / thesis-break 분류
```

핵심은 이거다.

```text
점수가 높다
≠ 좋은 후보

점수가 높고
+ EPS/FCF evidence가 있고
+ 가격경로가 맞고
+ RedTeam hard flag가 없고
+ 4B 과열이 아직 지나치지 않아야
Stage 3 후보가 된다.
```

---

## 2. 대상 canonical archetype

R13에서 확정할 cross-archetype은 아래로 둔다.

| 구분            | canonical archetype                  | 역할                          |
| ------------- | ------------------------------------ | --------------------------- |
| 회계·감사 신뢰도     | `REDTEAM_ACCOUNTING_TRUST_OVERLAY`   | hard 4C gate                |
| 내부통제·공시 지연    | `FINANCIAL_REPORTING_INTEGRITY_RISK` | hard 4C gate                |
| 가격만 오른 테마     | `PRICE_ONLY_RALLY`                   | Green 차단                    |
| 이벤트 프리미엄      | `EVENT_PREMIUM`                      | Stage 1/Event로 분리           |
| 사이클 성공        | `CYCLICAL_SUCCESS`                   | 구조적 성공과 분리                  |
| 구조적 성공        | `STRUCTURAL_SUCCESS_ALIGNED`         | Green 후보                    |
| 증거는 좋지만 가격 실패 | `EVIDENCE_GOOD_BUT_PRICE_FAILED`     | 점수 재보정                      |
| 점수는 높지만 실적 실패 | `FALSE_POSITIVE_SCORE`               | 감점축 강화                      |
| 4B 과열         | `CROWDED_RERATING_4B_WATCH`          | 비중 축소·졸업 감시                 |
| 4C 논리 훼손      | `THESIS_BREAK_4C`                    | Stage 강등                    |
| 법적·규제 리스크     | `LEGAL_REGULATORY_REDTEAM`           | hard/soft gate              |
| 신뢰·운영 장애      | `OPERATIONAL_TRUST_BREAK`            | 보안·플랫폼 hard gate            |
| 부채·현금흐름 리스크   | `LEVERAGE_FCF_BREAKDOWN`             | Neocloud/REIT/바이오 hard gate |
| 증거 부족         | `UNKNOWN_INSUFFICIENT_EVIDENCE`      | Green 금지                    |

---

## 3. deep sub-archetype

```text
REDTEAM_ACCOUNTING_TRUST_OVERLAY
- 감사인 사임
- 감사보고서 지연
- 내부통제 중대결함
- 재무제표 재작성 가능성
- SEC/검찰/규제기관 조사
- 관련자거래 의혹
- 반복 공시 지연

PRICE_ONLY_RALLY
- 주가만 급등
- EPS/FCF evidence 없음
- 계약/매출/수주 없음
- 테마명만 있음
- SNS/뉴스 기반 과열

EVENT_PREMIUM
- 공개매수
- 경영권 분쟁
- 정책 발표
- 재난/질병 뉴스
- MOU
- 상장 기대
- 인수합병 기대

CYCLICAL_SUCCESS
- 운임 급등
- 원자재 가격 상승
- 정제마진 상승
- 계란/육계/사료 가격 이벤트
- 금·리튬·화학 spread
- EPS peak 이후 정상화 가능성

CROWDED_RERATING_4B_WATCH
- 모두가 새 프레임 인정
- 목표가 과밀 상향
- valuation band 포화
- 1~2년 급등
- EPS 상향보다 multiple 확장이 먼저 감
- 신규 진입자·CAPA 증설 증가

THESIS_BREAK_4C
- 계약 취소
- 프로젝트 취소
- 수주 취소
- 규제 불허
- 대형 보안사고
- 개인정보 유출
- 부채 refinancing 실패
- 현금 runway 붕괴
- 고객사 주문 취소
- 가격/운임/수요 급락

OPERATIONAL_TRUST_BREAK
- 보안 업데이트 장애
- 고객 피해
- 대형 소송
- 갱신율 하락
- 플랫폼 안전성 규제
- 고객 신뢰도 훼손

LEVERAGE_FCF_BREAKDOWN
- 고부채
- FCF 적자
- refinancing pressure
- 고금리
- debt/EBITDA 악화
- GPU 감가상각
- REIT funding cost 상승
```

---

# 4. 성공사례

R13에서의 “성공사례”는 개별 업종 성공사례가 아니라, **가격경로와 증거가 실제로 맞아떨어진 검증 패턴**이다.

## 4-1. 구조적 성공 + 가격경로 aligned

대표 패턴은 `STRUCTURAL_SUCCESS_ALIGNED`다.

```text
산업 구조 변화
→ 실제 계약/수주/매출/EPS 상향
→ 주가 리레이팅
→ 4B 전까지 가격경로가 evidence와 동행
```

예시로 SK하이닉스 HBM/메모리 리레이팅은 R2에서 강한 aligned 사례다. Reuters는 SK하이닉스 주가가 2025년에 274%, 2026년에 200% 이상 상승했고, 시가총액이 16개월 전 1,000억 달러 미만에서 약 9,420억 달러까지 올랐다고 보도했다. 이건 단순 테마가 아니라 AI 서버용 HBM과 메모리 병목이 시장 프레임 전환으로 이어진 강한 가격경로 사례다. ([Reuters][1])

**R13 판정**

```text
case_type = structural_success_aligned
but 4B_watch = true
```

이런 케이스는 성공이지만, 이미 1~2년 급등했다면 “더 사도 되는가”보다 **졸업·4B 감시**가 중요해진다.

---

## 4-2. 자본배분 + 사업전략 + 가격반응 aligned

현대차는 R9의 좋은 cross-case다. 현대차는 하이브리드 라인업 확대, 2030년 판매목표, 4조 원 자사주 매입, 배당 확대를 함께 발표했고, 발표 후 주가는 장중 최대 5%, 종가 기준 4.7% 상승했다. 이건 단순 자동차 판매 뉴스가 아니라 **사업 mix + FCF + 주주환원**이 같이 작동한 case다. ([Reuters][2])

**R13 판정**

```text
case_type = valueup_strategy_aligned
R13 check = capital_allocation_quality + EPS/FCF sustainability
```

이런 케이스는 R6 value-up, R9 완성차, R5 소비재 일부에 공통 적용된다.

---

## 4-3. 이벤트가 실제 계약·실적으로 승격된 케이스

R11의 전염병·재난 이벤트는 대부분 Event지만, 정부계약·매출 가이던스가 붙으면 Stage 2로 승격될 수 있다.

```text
질병 뉴스
→ 관련주 급등
→ 정부 stockpile 계약
→ 매출/EBITDA 가이던스 상향
→ event_to_contract
```

이 경우에도 구조적 Green은 바로 주면 안 된다. 반복 계약이 확인되기 전까지는 `event_to_contract_success_candidate`로 둔다.

---

# 5. 반례

R13에서 반례는 점수정규화의 핵심이다. 반례가 많아질수록 Green gate가 정확해진다.

## 5-1. Supermicro — 회계신뢰도 hard 4C

Supermicro는 AI 서버 수요로 크게 리레이팅된 뒤 회계 신뢰도 이슈로 무너진 대표 반례다. Reuters는 Ernst & Young이 Supermicro 감사인에서 사임하자 주가가 30% 이상 하락했고, EY가 경영진·감사위원회의 진술을 더 이상 신뢰할 수 없다고 판단했다고 보도했다. delayed annual report, Hindenburg의 회계조작 주장, DOJ 조사 보도까지 겹쳤다. ([Reuters][3])

**R13 교훈**

```text
AI 서버 매출 성장
≠ Stage 3 유지

auditor_resignation = hard 4C
filing_delay = hard 4C
internal_control_issue = hard 4C
related_party_risk = hard 4C
```

**가격경로 판정**

```text
early_rerating_success_then_hard_4c
```

---

## 5-2. CrowdStrike — 운영 신뢰도 hard 4C

CrowdStrike는 반복 보안 매출이 있어도 operational trust가 깨지면 바로 hard 4C가 될 수 있음을 보여준다. Reuters는 잘못된 소프트웨어 업데이트로 800만 대 이상 컴퓨터가 영향을 받았고, CrowdStrike 주가가 12일 동안 32% 하락해 250억 달러 시가총액이 사라졌다고 보도했다. Delta는 같은 outage로 1.3 million customers가 영향을 받고 7,000 flights가 취소됐으며 5억 달러 이상 피해를 봤다고 소송을 냈다. ([Reuters][4])

**R13 교훈**

```text
보안 ARR
≠ Green 자동 유지

global outage
customer lawsuit
trust damage
renewal risk
이면 Stage 3 즉시 재검토.
```

**가격경로 판정**

```text
operational_trust_break_4c
```

---

## 5-3. TerraUSD/Luna — stablecoin hard 4C

디지털금융·스테이블코인에서 절대 잊으면 안 되는 반례다. Reuters는 TerraUSD/Luna 붕괴가 약 400억 달러 규모 crypto crash와 연결됐고, Do Kwon이 투자자를 오도한 혐의로 법적 절차를 밟았다고 보도했다. ([Reuters][5])

**R13 교훈**

```text
stablecoin
≠ 모두 같은 안정성

fiat-backed regulated stablecoin
과
algorithmic stablecoin
은 완전히 분리해야 한다.
```

**가격경로 판정**

```text
algorithmic_stablecoin_thesis_break
```

---

## 5-4. Bluebird bio — 승인 후 상업화 실패

Bluebird는 “FDA 승인 제품이 있어도 상업화·환급·현금 runway가 없으면 무너진다”는 R7 대표 반례다. Reuters는 bluebird가 severe cash crunch 속에서 Carlyle·SK Capital에 주당 3달러로 매각되기로 했고, 이는 직전 종가 대비 57.4% 할인된 가격이며 발표 후 주가가 36% 하락했다고 보도했다. 과거 2018년 약 150달러에 거래되던 주식이 크게 무너졌고, gene therapy uptake도 느렸다고 설명했다. ([Reuters][6])

**R13 교훈**

```text
approval
≠ commercialization
≠ EPS/FCF

cash_burn + slow_uptake + reimbursement_uncertainty
= 4C
```

---

## 5-5. Novo Nordisk — 고성장 시장도 4B에서 4C로 간다

GLP-1은 구조적 성장시장처럼 보이지만, 가격·경쟁·copycat/compounded drug이 valuation을 꺾을 수 있다. Reuters는 Novo Nordisk가 2026년 매출·영업이익이 5~13% 감소할 수 있다고 경고하자 주가가 16% 하락하고 약 500억 달러 시총이 사라졌다고 보도했다. ([Reuters][7])

**R13 교훈**

```text
거대한 TAM
≠ Green 유지

price pressure
competition
copycat/compounded alternatives
insurance/reimbursement risk
가 나오면 4B에서 4C로 전환.
```

---

# 6. 4B-watch 사례

R13의 4B는 “좋은 종목이 나쁘다”가 아니라, **좋은 논리가 시장에 너무 많이 반영된 상태**다.

## 6-1. HBM / AI 메모리 4B

```text
조건:
- 1~2년 급등
- 모두가 AI memory rerating 인정
- 시총·valuation band 급상승
- 고객사 가격저항 가능성
- CAPA 증설 뉴스 증가
- EPS 상향은 지속되지만 multiple 확장 여지가 줄어듦
```

SK하이닉스가 2025년 274%, 2026년 200% 이상 상승한 것은 성공사례이면서 동시에 강한 4B 감시 신호다. ([Reuters][1])

---

## 6-2. Value-up / Korea discount 4B

```text
조건:
- 저PBR주 전반 동반 급등
- 자사주 소각·배당 실행보다 PBR band가 먼저 올라감
- 정책 기대가 이미 가격에 반영
- 실제 ROE 개선은 아직 미흡
```

삼성전자처럼 자사주 발표 후 주가가 7.2% 급등할 수 있지만, 사업 경쟁력·EPS 경로가 따라오지 않으면 buyback-only rebound로 분류해야 한다. ([Investopedia][8])

---

## 6-3. AI 서버·AI 인프라 4B

```text
조건:
- AI 서버/광통신/냉각/전력장비 관련주 동반 급등
- 수주보다 valuation이 먼저 감
- 고객사 concentration과 회계 리스크를 무시
- CAPA 증설·lead time 정상화를 시장이 과소평가
```

Supermicro는 초기에 AI 서버 리레이팅이 있었지만 회계 신뢰도 hard flag가 나오자 급락했다. R13에서는 이런 케이스를 **“성공 후 thesis break”**로 따로 분류해야 한다. ([Reuters][3])

---

## 6-4. GLP-1 / 바이오 고성장 4B

```text
조건:
- 시장 크기 narrative 과밀
- 보험·가격·경쟁·copycat 리스크 무시
- 처방량보다 valuation이 먼저 감
```

Novo Nordisk의 16% 급락은 “TAM이 크면 괜찮다”는 착각을 깨는 사례다. ([Reuters][7])

---

## 6-5. 이벤트·정책 테마 4B

```text
조건:
- 정책 발표만으로 관련주 동반 급등
- 실제 계약·예산·매출 없음
- MOU 단계인데 Stage 3처럼 가격이 움직임
```

이건 R11 전반에 적용된다. 우크라 재건, 남북경협, 세종시, 전염병, 초전도체, 지역화폐 같은 테마는 기본값이 4B-watch 또는 Event/Watch다.

---

# 7. 4C-thesis-break 사례

R13에서 4C는 “조정”이 아니라 **논리 훼손**이다.

## 7-1. 회계·감사 4C

```text
auditor_resignation
filing_delay
internal_control_weakness
financial_restatement
regulatory_probe
related_party_transaction
```

Supermicro의 EY 사임은 이 항목의 기준 사례다. ([Reuters][3])

---

## 7-2. 운영 신뢰도 4C

```text
global_outage
customer_damage
mass_lawsuit
renewal_risk
brand_trust_damage
```

CrowdStrike outage는 보안·플랫폼·클라우드·SaaS 전체에 적용할 운영 신뢰도 기준 사례다. ([Reuters][4])

---

## 7-3. 상업화 실패 4C

```text
approval_but_no_uptake
slow_prescription
reimbursement_failure
cash_runway_collapse
discounted_take_private
```

Bluebird bio는 승인 후에도 상업화가 안 되면 주가가 무너지는 기준 사례다. ([Reuters][6])

---

## 7-4. 시장 가격·수요 붕괴 4C

```text
commodity_price_crash
freight_rate_collapse
EV_demand_slowdown
capacity_overbuild
margin_compression
```

이건 R3, R4, R9에 주로 적용된다. 예를 들어 GLP-1처럼 구조 성장시장도 가격·경쟁이 수익 경로를 훼손하면 4C가 된다. ([Reuters][7])

---

## 7-5. 레버리지·FCF 붕괴 4C

```text
FCF_negative
debt_refinancing_pressure
interest_expense_spike
capex_burden
dividend_cut
going_concern
```

이건 Neocloud, REIT, PF 건설, 바이오, 스마트팜, eVTOL에 공통 적용한다.

---

## 7-6. 디지털자산 붕괴 4C

```text
depeg
reserve_failure
convertibility_failure
run
fraud
algorithmic_stablecoin_failure
```

TerraUSD/Luna는 `DIGITAL_ASSET_TOKENIZATION`에서 hard 4C 기준으로 둔다. ([Reuters][5])

---

# 8. 점수비중 보정표 — R13 v1.0

R13은 일반 점수표가 아니라 **gate / overlay / validation score**다.

| cross-archetype                    | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation |  Capital |   Info | 처리                  |
| ---------------------------------- | ------: | ---------: | ---------: | ---------: | --------: | -------: | -----: | ------------------- |
| `STRUCTURAL_SUCCESS_ALIGNED`       |       + |          + |          + |          + |         + | optional |      + | Green 유지 가능         |
| `PRICE_ONLY_RALLY`                 |       0 |          0 |          0 |          - |         - |        0 |      - | Green 금지            |
| `EVENT_PREMIUM`                    |     0~+ |          0 |          0 |          + |         0 |        0 |     보통 | Event로 분리           |
| `CYCLICAL_SUCCESS`                 |       + |         낮음 |          + |          0 |        낮음 |        0 |     보통 | cycle_success 분리    |
| `FALSE_POSITIVE_SCORE`             |       - |          - |          - |          - |         - |        0 |      - | 해당 archetype 점수 재보정 |
| `EVIDENCE_GOOD_BUT_PRICE_FAILED`   |       + |          + |   optional |          0 |         - | optional |      + | 시장 프레임/밸류 재검토       |
| `CROWDED_RERATING_4B_WATCH`        |      유지 |         유지 |         유지 |         약화 |        감점 | optional |     유지 | 비중축소·졸업 감시          |
| `THESIS_BREAK_4C`                  |  hard - |     hard - |     hard - |     hard - |    hard - |   hard - | hard - | Stage 강등            |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` |    gate |       gate |       gate |       gate |      gate |     gate |   gate | hard block          |
| `OPERATIONAL_TRUST_BREAK`          |    gate |       gate |       gate |       gate |      gate |     gate |   gate | hard review         |
| `LEVERAGE_FCF_BREAKDOWN`           |       - |          - |          0 |          - |         - |        - |     보통 | Green 금지            |
| `UNKNOWN_INSUFFICIENT_EVIDENCE`    |       0 |          0 |          0 |          0 |         0 |        0 |     낮음 | Stage 3 금지          |

---

# 9. stage date 후보

R13은 모든 case에 공통으로 아래 stage date를 강제한다.

```text
stage1_date:
산업 변화, 정책, 테마, 임상, 계약 기대, 가격 이벤트가 처음 포착된 날짜

stage2_date:
실제 공시, 계약, 수주, 실적, 처방량, 가동률, 매출, EPS 상향이 확인된 날짜

stage3_date:
중장기 EPS/FCF 상향 + valuation frame 변화 + cross-evidence가 확인된 날짜

stage4b_date:
모두가 새 프레임을 인정하고 valuation이 포화되기 시작한 날짜

stage4c_date:
논리 훼손이 확인된 날짜
```

각 stage의 의미는 아래처럼 고정한다.

```text
Stage 1:
관찰 시작. 테마 가능성은 있으나 Green 아님.

Stage 2:
증거가 생김. 계약·실적·매출·처방·가동률 중 하나 이상 확인.

Stage 3:
구조적 후보. EPS/FCF 지속성과 valuation frame 전환이 같이 확인.

Stage 4B:
졸업·과열 감시. 좋은 논리가 이미 시장에 널리 알려짐.

Stage 4C:
논리 훼손. Stage 강등 또는 제외.
```

---

# 10. 가격경로 검증계획

R13부터는 모든 case를 아래 판정표로 분류한다.

## 10-1. 필수 가격지표

```text
MFE_5D
MFE_20D
MFE_30D
MFE_60D
MFE_90D
MFE_180D
MFE_1Y
MFE_2Y

MAE_5D
MAE_20D
MAE_30D
MAE_60D
MAE_90D
MAE_180D
MAE_1Y

peak_price
drawdown_after_peak
below_stage1_price_flag
below_stage2_price_flag
below_stage3_price_flag
```

## 10-2. 필수 판정값

```text
aligned:
증거 이후 주가·EPS/FCF가 같이 리레이팅.

structural_success:
6~24개월 가격경로와 실적경로가 같이 우상향.

cyclical_success:
가격·운임·원자재·spread로 수익은 났지만 구조적 지속성 낮음.

event_premium:
공개매수·정책·재난·전염병·MOU로 오른 가격.

price_moved_without_evidence:
주가는 올랐지만 계약·실적·EPS 증거 없음.

evidence_good_but_price_failed:
증거는 있었지만 시장이 리레이팅하지 않음.

false_positive_score:
에이전트 점수는 높았지만 가격·실적 검증 실패.

hard_4c_thesis_break:
회계·법적·운영·부채·수요 붕괴로 논리 훼손.

unknown_insufficient_price_data:
가격 backfill이 부족해 판정 유보.
```

## 10-3. archetype별 검증기간

```text
수주·backlog형:
MFE/MAE 180D, 1Y, 2Y 중심

AI·반도체형:
90D, 180D, 1Y, 2Y + 4B drawdown 중심

소비재·브랜드형:
90D, 180D, 1Y + 재고/채권 동행 확인

금융·value-up형:
180D, 1Y, 2Y + PBR band 변화 확인

바이오·헬스케어형:
30D 이벤트 반응 + 180D/1Y 상업화 확인

정책·이벤트형:
5D, 20D, 60D, 90D 중심

사이클형:
가격 peak 이후 drawdown 중심
```

---

# 11. 다음에 에이전트가 채워야 할 price fields

R13은 모든 R1~R12 case에 공통으로 아래 필드를 강제한다.

```text
case_id
symbol
company_name
market
primary_sector_round
primary_archetype
secondary_archetypes
case_type

stage1_date
stage2_date
stage3_date
stage4b_date
stage4c_date

stage1_evidence_type
stage2_evidence_type
stage3_evidence_type
stage4b_evidence_type
stage4c_evidence_type

stage1_price
stage2_price
stage3_price
stage4b_price
stage4c_price
peak_price
peak_date

MFE_5D
MFE_20D
MFE_30D
MFE_60D
MFE_90D
MFE_180D
MFE_1Y
MFE_2Y

MAE_5D
MAE_20D
MAE_30D
MAE_60D
MAE_90D
MAE_180D
MAE_1Y

drawdown_after_peak
below_stage1_price_flag
below_stage2_price_flag
below_stage3_price_flag

revenue_revision_1q
revenue_revision_1y
op_revision_1q
op_revision_1y
eps_revision_1q
eps_revision_1y
fcf_margin_change
gross_margin_change
op_margin_change

valuation_metric_before
valuation_metric_after
pbr_before
pbr_after
per_before
per_after
ev_ebitda_before
ev_ebitda_after

contract_value
contract_duration_months
contract_amount_to_sales
backlog_growth
capacity_utilization
customer_concentration

debt_to_ebitda
net_debt
interest_expense
cash_runway_months
refinancing_risk_flag
dividend_cut_flag
buyback_cancelled_flag

auditor_resignation_flag
filing_delay_flag
internal_control_issue_flag
regulatory_probe_flag
related_party_risk_flag

security_outage_flag
privacy_breach_flag
customer_lawsuit_flag
operational_trust_break_flag

depeg_event_flag
reserve_failure_flag
convertibility_risk_flag

event_only_flag
cycle_only_flag
price_only_rally_flag
crowded_4b_flag
hard_4c_flag

score_before_redteam
score_after_redteam
stage_before_redteam
stage_after_redteam
score_price_alignment
price_validation_status
review_notes
```

---

# R13 최종 결론

R13은 지금까지 만든 12개 대섹터 지도를 실제 시스템으로 만들기 위한 **최종 안전장치**다.

```text
R1~R12:
어디서 후보가 나오는가?

R13:
그 후보가 진짜인가?
이미 늦었는가?
테마뿐인가?
사이클뿐인가?
회계·법적·운영 리스크가 논리를 깨는가?
가격경로가 점수와 맞는가?
```

R13에서 가장 중요한 규칙은 이거다.

```text
Stage 3-Green은 점수만으로 절대 나오면 안 된다.

반드시:
1. cross-evidence
2. EPS/FCF 지속성
3. 가격경로 alignment
4. RedTeam hard flag 부재
5. 4B 과열 미포화

이 다섯 개를 통과해야 한다.
```

그리고 이 원칙은 Checkpoint 20의 증거 품질 철학과도 맞다. OpenDART detail fetch에서 계약금액, 계약기간, 매출 대비 계약금액 같은 필드는 실제로 확인될 때만 쓰고, 없는 값을 만들지 않는 구조를 요구했던 것처럼, R13에서도 **없는 증거를 점수로 만들면 안 된다**.

**R13 점수정규화의 핵심 문장:**

> Cross-archetype 검증은 “좋아 보이는 후보”를 고르는 단계가 아니라, **좋아 보이는 후보 중에서 실제 EPS/FCF와 가격경로가 맞은 것만 남기고, 테마·사이클·이벤트·회계·부채·운영 신뢰 리스크를 제거하는 단계**다.

이제 R13까지 한 바퀴가 끝났다. 다음에 같은 지시로 진행하면, 규칙대로 다시 **R1 — 산업재·수주·인프라**로 돌아가서 두 번째 루프를 시작하면 된다.

[1]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[2]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/?utm_source=chatgpt.com "Hyundai targets 30% rise in sales by 2030, as it doubles hybrid lineups"
[3]: https://www.reuters.com/technology/super-micro-computer-says-ernst-young-resigns-its-accountant-shares-tank-2024-10-30/?utm_source=chatgpt.com "Super Micro Computer says Ernst & Young resigns as auditor, shares tank"
[4]: https://www.reuters.com/legal/crowdstrike-is-sued-by-shareholders-over-huge-software-outage-2024-07-31/?utm_source=chatgpt.com "CrowdStrike is sued by shareholders over huge software outage"
[5]: https://www.reuters.com/legal/government/terrausd-creator-do-kwon-be-sentenced-over-40-billion-crypto-collapse-2025-12-11/?utm_source=chatgpt.com "TerraUSD creator Do Kwon to be sentenced over $40 billion crypto collapse"
[6]: https://www.reuters.com/markets/deals/bluebird-bio-be-taken-private-by-carlyle-sk-capital-amid-cash-crunch-2025-02-21/?utm_source=chatgpt.com "Gene therapy maker bluebird to go private in discounted deal amid cash crunch"
[7]: https://www.reuters.com/business/healthcare-pharmaceuticals/novo-nordisk-plunge-wipes-50-billion-off-obesity-drug-giant-2026-02-04/?utm_source=chatgpt.com "Novo Nordisk plunge wipes $50 billion off obesity drug giant"
[8]: https://www.investopedia.com/samsung-stock-surges-on-usd7-2b-buyback-plan-8745940?utm_source=chatgpt.com "Samsung Stock Surges on $7.2B Buyback Plan"
