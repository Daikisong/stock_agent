좋아. 순서상 이번은 **R2 Loop 7 — AI·반도체·전자부품 가격경로 검증 라운드**로 진행한다.

이번 라운드는 `SK하이닉스 HBM 대성공` 같은 기존 대표 case를 또 설명하는 게 아니라, **국장 안에서 HBM 장비, AI칩 디자인하우스, 삼성 HBM 후발, 정책성 파운드리, AI PCB/기판류 과열 가능성**을 나눠서 본다. 단, 중소형주는 공개 영문/해외 소스만으로 stage price와 MFE/MAE를 완전히 채우기 어렵기 때문에, 정확한 수익률 계산은 `needs_ohlc_backfill`로 남긴다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
large_sector = AI_SEMICONDUCTOR_ELECTRONICS
round = R2 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R2의 기본 검증축은 HBM, 범용 메모리, 반도체 장비, 소재, 패키징, AI 서버 supply chain, neocloud, 광통신, 냉각, 회계신뢰도 overlay다. Round 40 지도에서도 R2 validation focus는 `eps_revision`, `capacity_bottleneck`, `customer_order`, `gross_margin`, `inventory`, `accounting_trust`로 잡혀 있다. 

Round 119 기준으로 R2에서 부족한 증거는 `ai_name`, `server_theme`이고, 필요한 증거는 `hbm_lta`, `prepayment`, `capacity_constraint`, `consensus_revision`, `rerating_room`이다. Green blocker는 `capex_cut`, `supply_glut`, `circular_financing`이다. 

---

# 2. 대상 canonical archetype

이번 R2 Loop 7에서 새로 archetype을 늘리기보다, 기존 R2 안에서 가격경로 검증이 필요한 축만 사용한다.

```text
MEMORY_HBM_CAPACITY
MEMORY_HBM_LTA_PREPAYMENT
HBM_CATCHUP_EXECUTION
SEMI_EQUIPMENT_AI_CAPEX
HBM_BONDER_EQUIPMENT_KOREA
ADVANCED_PACKAGING_EQUIPMENT_KOREA
ADVANCED_PACKAGING_PCB
AI_CHIP_FABRIC_INFRA
SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER
AI_ACCELERATOR_CHIP_PUREPLAY
COMMODITY_MEMORY_GENERAL_SEMI
AI_DATA_CENTER_INFRASTRUCTURE
REDTEAM_ACCOUNTING_TRUST_OVERLAY
AI_CAPEX_CROWDING_OVERLAY
CIRCULAR_AI_FINANCING_OVERLAY
DISCLOSURE_CONFIDENCE_CAP
```

이번 라운드의 핵심 문장은 이거다.

```text
AI 반도체 수혜주인가?
아니면 AI 인프라 병목을 실제 매출·마진·EPS·FCF로 바꾸는 회사인가?
```

---

# 3. deep sub-archetype

```text
HBM 장비:
- TSV-TC bonder
- HBM packaging equipment
- HBM test equipment
- HBM probe / handler / cube prober
- SK hynix-linked HBM supply chain
- Micron customer expansion
- 고객 다변화
- order-to-revenue conversion

HBM 후발 / catch-up:
- Samsung HBM3E / HBM4 qualification
- Nvidia qualification
- sampling vs volume shipment
- yield
- labor disruption
- talent retention
- foundry/base-die execution

AI칩 디자인하우스:
- Samsung 2nm GAA
- Preferred Networks AI chip
- Gaonchips design
- customer design win
- tape-out
- 양산 전환
- revenue conversion

AI PCB / 기판:
- AI server MLB
- advanced PCB
- Nvidia/AI server supply chain
- capacity expansion
- capital raise / dilution
- customer concentration

정책성 파운드리:
- 40nm public-private foundry
- DB HiTek candidate
- policy event
- actual order absence
- government funding vs company revenue

RedTeam:
- accounting trust
- IP leakage
- labor strike
- circular AI financing
- price-only AI rally
- AI CAPEX crowding
```

---

# 4. 국장 신규 후보 case

## Case A — 한미반도체 `structural_success + 4B-watch`

```text
symbol = 042700
archetype = HBM_BONDER_EQUIPMENT_KOREA / SEMI_EQUIPMENT_AI_CAPEX
case_type = structural_success + 4B-watch
```

한미반도체는 R2에서 장비주의 Stage 3 검증에 좋은 anchor다. 2024년 3월 WSJ 보도 기준, 한미반도체는 SK하이닉스에 HBM 패키징 장비인 TSV-TC bonder를 공급하고 있었고, 최근 SK하이닉스로부터 214.8억 원 계약을 포함해 누적 약 2,000억 원 규모의 최근 계약을 확보했다. 같은 보도에서 주가는 AI 반도체 기대와 함께 하루 16% 상승했다. ([월스트리트 저널][1])

며칠 뒤 한미반도체는 Micron 공급 가능성 보도만으로 장중 22%까지 급등했고, 장중 139,100원까지 올랐다. 그런데 이 Micron deal은 당시 양사 확인이 없던 “media report” 성격이었다. 이 구간은 Stage 3 이후 4B-watch가 빨리 붙어야 하는 구간이다. ([월스트리트 저널][2])

### stage date 후보

```text
Stage 1:
2023~2024
- HBM 장비 수혜 테마
- SK하이닉스 HBM CAPA 확대 기대

Stage 2:
2024-03-26
- SK하이닉스향 TSV-TC bonder 공급
- 최근 계약 누적 약 2,000억 원 보도
- 장비 수주가 실제 고객/제품과 연결됨

Stage 3:
2024-03-26 후보
- 고객사 SK하이닉스
- HBM packaging equipment
- 계약 누적 규모
- HBM CAPA 병목과 직접 연결
- 단, 정확한 Stage 3 확정은 매출 인식/마진/EPS revision backfill 필요

Stage 4B:
2024-03-28 후보
- Micron deal 미확인 보도만으로 장중 +22%
- 장중 139,100원
- 고객 다변화 기대가 가격에 선반영된 구간

Stage 4C:
없음
```

### 가격경로 검증

```text
stage3_price:
2024-03-26 종가 backfill 필요
2024-03-28 장중 anchor = 139,100원

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
alignment = aligned, 단 4B-watch 조기 부착 필요
rerating_result = true_rerating 후보
stage_failure_type = green_success 후보
```

### 교정 포인트

한미반도체는 `contract_quality`, `customer_visibility`, `capacity_bottleneck`, `order_to_revenue_conversion` 점수를 올려준다. 하지만 Micron 미확인 보도처럼 **확정 계약 전 가격이 먼저 뛰는 구간**은 `4B-watch` 또는 `price_ahead_of_evidence`로 따로 잡아야 한다.

---

## Case B — 가온칩스 `success_candidate`

```text
symbol = 399720
archetype = SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER / AI_CHIP_FABRIC_INFRA
case_type = success_candidate
```

가온칩스는 삼성전자 2nm AI칩 수주/디자인하우스 경로를 보는 case다. 2024년 7월 Reuters는 삼성전자가 일본 Preferred Networks의 AI칩을 2nm 공정과 첨단 패키징으로 생산하는 첫 공개 수주를 확보했고, 이 AI칩 설계를 한국의 가온칩스가 맡았다고 보도했다. 이 칩은 생성AI·대형언어모델용 고성능 컴퓨팅 하드웨어에 들어가는 구조다. ([Reuters][3])

다만 이건 바로 Stage 3-Green이 아니다. 디자인하우스의 경우 `design win`은 Stage 2로 강하지만, Stage 3는 tape-out, 양산, 매출 인식, gross margin, 반복 고객까지 확인되어야 한다.

### stage date 후보

```text
Stage 1:
2024년 AI칩 / 시스템반도체 / 삼성 2nm 기대

Stage 2:
2024-07-09
- Preferred Networks AI칩 설계 참여
- 삼성 2nm GAA + 첨단 패키징 첫 공개 수주
- company-level evidence 있음

Stage 3:
보류
- design win만으로는 부족
- tape-out, 양산, 매출 인식, margin 확인 필요

Stage 4B:
없음
- 단, 주가가 먼저 과열됐다면 별도 backfill 필요

Stage 4C:
없음
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

Stage2_price:
2024-07-09 OHLC backfill 필요

MFE / MAE:
Stage 2 기준 backfill 가능
Stage 3 기준은 N/A

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
rerating_result = success_candidate
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

가온칩스는 R2에서 **AI chip design win은 Stage 2까지는 강하지만 Stage 3는 아니다**라는 기준을 강화한다.

```text
올릴 축:
customer_design_win
advanced_node_visibility
packaging_link

막을 축:
design_win_without_revenue
tapeout_before_volume
no_margin_visibility
```

---

## Case C — 삼성전자 `failed_rerating / HBM_CATCHUP_EXECUTION 보류`

```text
symbol = 005930
archetype = HBM_CATCHUP_EXECUTION / REDTEAM_OPERATIONAL_TRUST
case_type = failed_rerating 또는 evidence_good_but_price_failed
```

삼성전자는 R2에서 “대형주라 무조건 Green”이 아니라, HBM 후발 추격을 별도로 검증해야 하는 case다. 2025년 1분기 Reuters 보도에서 삼성전자의 반도체 부문 이익은 전년 대비 42% 감소했고, AI 프로세서에 쓰이는 HBM 매출이 줄었다. 기사에서는 삼성전자가 Nvidia향 HBM 공급에서 SK하이닉스에 뒤처져 있다고 설명했다. ([Reuters][4])

2026년에는 AI 반도체 랠리로 삼성전자가 다시 강하게 올랐고, KOSPI가 7,000을 돌파한 날 삼성전자도 14.4% 상승하며 1조 달러 클럽에 들어갔다. 하지만 이건 Stage 3를 2025년 초 HBM catch-up에 줘야 한다는 뜻이 아니다. 2025년 당시에는 HBM sales decline, Nvidia qualification lag, foundry/logic 약세가 있었기 때문에 Stage 3-Green을 보류하는 게 맞았다. ([Reuters][5])

또 2026년 5월에는 삼성전자 노동조합 파업 리스크가 커졌고, 정부도 생산 차질과 수출 영향 우려를 표명했다. Reuters는 잠재적 파업이 반도체 생산과 공급망에 리스크가 될 수 있다고 보도했다. ([Reuters][6])

### stage date 후보

```text
Stage 1:
2024~2025
- 삼성 HBM catch-up 기대
- HBM3E sample / HBM4 기대

Stage 2:
2025-04-30
- HBM sales bottoming 기대는 있으나
- 반도체 부문 이익 -42%
- Nvidia향 HBM lag 확인
- Stage 2 watch로만 처리

Stage 3:
보류
- HBM 매출, qualification, volume shipment, EPS revision이 확인되지 않음

Stage 4B:
2026-05-06 후보
- AI 반도체 전체 랠리로 삼성전자 +14.4%
- KOSPI AI rally와 함께 valuation re-expansion

Stage 4C:
2026-05-18 현재 hard 4C 아님
- 단, 파업이 실제 생산 차질·고객 이탈·실적 훼손으로 연결되면 4C 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

MFE / MAE:
Stage 2 watch 기준 backfill 필요

below_stage3_price_flag:
N/A

peak_price:
2026 AI rally 구간 backfill 필요

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = evidence_good_but_price_failed 후보
rerating_result = failed_rerating_from_2025_hbm_catchup
2026 rally = broad_ai_memory_rerating / 4B-watch 후보
stage_failure_type = should_have_been_yellow_or_watch
```

### 교정 포인트

삼성전자 case는 R2에서 아주 중요하다.

```text
HBM sample
≠ Stage 3

HBM catch-up story
≠ Stage 3

Stage 3 조건:
qualification
volume shipment
customer visibility
HBM sales growth
margin
EPS revision
```

그리고 operational trust도 올려야 한다.

```text
파업 / 생산차질 / talent drain
= Stage 3-Green 감점 또는 4C watch
```

---

## Case D — DB하이텍 `event_premium / policy route only`

```text
symbol = 000990
archetype = AI_CHIP_FABRIC_INFRA / POLICY_FOUNDRY_EVENT
case_type = event_premium / insufficient_evidence
```

DB하이텍은 R2에서 정책성 파운드리 이벤트를 검증하는 case다. 2025년 12월 Reuters는 한국 정부가 AI 시대 반도체 경쟁력 강화를 위해 4.5조 원 규모 12인치 40nm 파운드리 구축을 검토하고, 삼성전자와 DB하이텍 같은 국내 파운드리 기업과 협의할 것이라고 보도했다. ([Reuters][7])

하지만 이건 DB하이텍의 Stage 3 증거가 아니다. 정부 정책 검토와 협의 대상 언급은 Stage 1~2 attention에 가깝고, 실제 수주, 투자 구조, 생산능력, 고객, 마진, 매출 인식이 확인되어야 Stage 3가 가능하다.

### stage date 후보

```text
Stage 1:
2025-12-10
- 정부 4.5조 원 파운드리 검토
- DB하이텍 협의 대상 언급

Stage 2:
보류 또는 약한 Stage 2
- 회사 단위 계약/투자확정/고객 확보가 아님

Stage 3:
없음
- revenue conversion 없음
- customer order 없음
- EPS revision 없음

Stage 4B:
정책 테마로 주가만 먼저 급등했다면 4B/price-only 후보
- 가격 backfill 필요

Stage 4C:
없음
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

MFE / MAE:
정책 이벤트 기준 backfill 가능

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = event_premium 또는 price_moved_without_evidence 후보
rerating_result = policy_event_rerating 후보
stage_failure_type = should_have_been_stage1_or_stage2
```

### 교정 포인트

DB하이텍은 R2에서 `policy_foundry`, `AI chip national strategy` 같은 테마를 Stage 3로 올리면 안 된다는 반례다.

```text
정책 발표
≠ 매출

정부 협의
≠ 고객 주문

파운드리 계획
≠ EPS/FCF 체급 변화
```

---

## Case E — 이수페타시스 `overheat / price_moved_without_evidence 후보`

```text
symbol = 007660
archetype = ADVANCED_PACKAGING_PCB / AI_SERVER_PCB_SUBSTRATE_SECOND_WAVE
case_type = overheat 또는 insufficient_evidence
```

이수페타시스는 AI 서버 PCB/MLB 쪽에서 반드시 검증해야 할 국장 case다. 다만 이번 공개소스 1차 확인에서는 회사 단위의 최신 고객명, 계약금액, 납품기간, AI 서버 매출 비중, OPM, EPS revision을 충분히 확인하지 못했다. 공개 요약 수준에서는 AI chip boom이 한국 회로기판 업체의 주가를 크게 밀어올렸다는 Bloomberg/Forbes 계열 언급이 남아 있지만, 이 정도로는 E2R Stage 3-Green을 줄 수 없다. ([위키백과][8])

이수페타시스는 오히려 R2의 중요한 시험지다. 가격이 먼저 움직였고, AI server PCB narrative가 강하지만, `customer_order`, `contract_amount`, `margin`, `capacity`, `EPS revision`, `inventory risk`를 채워야 한다.

### stage date 후보

```text
Stage 1:
2023~2024
- AI server PCB / Nvidia supply chain narrative

Stage 2:
보류
- 공개소스 기준 고객/계약/마진/매출비중 확인 부족
- DART/리포트 backfill 필요

Stage 3:
없음
- 현 단계에서는 Green 금지

Stage 4B:
가격이 이미 크게 오른 구간이 있다면 4B-watch 후보
- OHLC와 증거일 backfill 필요

Stage 4C:
없음
- 단, 유상증자/인수/재고/마진 훼손이 확인되면 4C 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

MFE / MAE:
Stage 1 narrative 기준 backfill 가능

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = price_moved_without_evidence 후보
rerating_result = theme_overheat 후보
stage_failure_type = insufficient_evidence
```

### 교정 포인트

이수페타시스는 `AI server PCB`를 무조건 Stage 3로 올리지 말라는 장치다.

```text
Green 필수:
AI server PCB 매출 비중
고객/납품 구조
capacity constraint
ASP / OPM
EPS revision
재고/채권 안정

Green 금지:
AI PCB 태그
Nvidia 연상
주가 급등
증권가 목표주가만 있음
```

---

## Case F — SK하이닉스 `4B benchmark only`

```text
symbol = 000660
archetype = MEMORY_HBM_CAPACITY / MEMORY_HBM_LTA_PREPAYMENT
case_type = 4B-watch benchmark
```

SK하이닉스는 기존 대표 성공사례라 이번 신규 case로 반복하지 않는다. 다만 R2의 4B 기준을 잡기 위한 **benchmark anchor**로만 사용한다.

Reuters는 2026년 5월 SK하이닉스가 AI 수요로 1조 달러 시총에 근접했고, 주가가 2025년에 274% 오른 뒤 2026년에도 200% 이상 상승했다고 보도했다. HBM과 전통 메모리 모두 AI 서버 수요의 핵심으로 작용했고, 시총은 16개월 전 1,000억 달러 미만에서 약 9,420억 달러까지 커졌다. ([Reuters][9])

또 2026년 1월에는 SK하이닉스가 AI 메모리 수요 대응을 위해 19조 원 규모 첨단 패키징 공장을 짓기로 했고, HBM 시장 점유율 61%로 선두라는 Macquarie 자료도 보도됐다. ([Reuters][10])

### stage date 후보

```text
Stage 3:
이미 과거 case-library에서 다뤄야 하는 구간.
이번 라운드에서는 신규 Stage 3 case로 쓰지 않음.

Stage 4B:
2026-05-14
- 2025년 +274%, 2026년 +200% 이상
- 1조 달러 시총 근접
- HBM 구조가 맞더라도 valuation/crowding watch 필요

Stage 4C:
없음
- 단, 고객 가격저항, CAPA 정상화, HBM 가격 하락, AI capex cut은 4C 후보
```

### 가격경로 검증

```text
stage3_price:
기존 case-library backfill 대상

MFE:
이미 대형 MFE 확인

4B_price:
2026-05-14 OHLC backfill 필요

drawdown_after_peak:
아직 관찰 필요
```

### score-price alignment

```text
alignment = aligned
rerating_result = true_rerating
4B_status = watch 또는 elevated
```

### 교정 포인트

SK하이닉스는 “R2 점수표가 진짜 대시세를 잡을 수 있는가”의 대표 anchor지만, 지금부터는 **추가 매수 Stage 3가 아니라 4B 감시 case**로 봐야 한다.

---

# 5. 이번 R2 case별 요약표

| case   | 분류                                |   Stage 3 판정 |                                 4B/4C 판정 | 가격경로 1차 판단                              |
| ------ | --------------------------------- | -----------: | ---------------------------------------: | --------------------------------------- |
| 한미반도체  | structural_success + 4B-watch     |        가능 후보 |                Micron 미확인 보도 구간 4B-watch | 장비 수주와 가격경로 align, 단 과열 빠름              |
| 가온칩스   | success_candidate                 |           보류 |                                       없음 | design win은 Stage 2, 양산/매출 전 Stage 3 금지 |
| 삼성전자   | failed_rerating / HBM catch-up 보류 |  2025년 기준 보류 | 2026 AI rally는 4B-watch 후보, 파업은 4C-watch | HBM sales decline / lag 때문에 Green 금지    |
| DB하이텍  | event_premium                     |           없음 |                 정책 테마 급등 시 4B/price-only | 정부 파운드리 계획은 Stage 1~2                   |
| 이수페타시스 | overheat / insufficient           |           없음 |                      가격 선행 시 4B-watch 후보 | AI PCB 태그만으로 Green 금지                   |
| SK하이닉스 | 4B benchmark                      | 기존 성공 anchor |                   2026 4B-watch/elevated | 신규 case 아님, 4B 기준점                      |

---

# 6. 각 case별 stage date 후보 요약

```text
한미반도체:
Stage 1 = 2023~2024 HBM 장비 테마
Stage 2 = 2024-03-26 SK하이닉스 TSV-TC bonder 계약/누적 수주 보도
Stage 3 = 2024-03-26 후보, 매출/마진/EPS backfill 필요
Stage 4B = 2024-03-28 Micron 미확인 보도 + 장중 139,100원
Stage 4C = 없음

가온칩스:
Stage 1 = 2024 AI칩 디자인하우스 테마
Stage 2 = 2024-07-09 Preferred Networks AI칩 설계 참여 보도
Stage 3 = 보류
Stage 4B = 없음
Stage 4C = 없음

삼성전자:
Stage 1 = 2024~2025 HBM catch-up 기대
Stage 2 = 2025-04-30 HBM sales bottoming 기대, 하지만 chip profit -42%
Stage 3 = 보류
Stage 4B = 2026-05-06 AI rally + 삼성전자 +14.4%
Stage 4C = 파업/생산차질이 실제화되면 후보

DB하이텍:
Stage 1 = 2025-12-10 정부 4.5조 원 파운드리 검토
Stage 2 = 보류 또는 약한 Stage 2
Stage 3 = 없음
Stage 4B = 정책 테마 가격 급등 시 후보
Stage 4C = 없음

이수페타시스:
Stage 1 = AI server PCB narrative
Stage 2 = DART/리포트 backfill 전 보류
Stage 3 = 없음
Stage 4B = 가격 선행 구간 있으면 후보
Stage 4C = 유상증자/인수/마진/재고 훼손 확인 시 후보

SK하이닉스:
Stage 3 = 기존 성공 anchor
Stage 4B = 2026-05-14 1조 달러 시총 근접 / 2025~2026 폭등
Stage 4C = 없음
```

---

# 7. 가격경로 검증

이번 R2는 정확한 OHLC backfill 없이는 수익률을 숫자로 확정하면 안 된다. 그래서 아래처럼 남긴다.

| case   |                                     stage3_price | MFE/MAE                      | below_stage3        | peak/drawdown             |
| ------ | -----------------------------------------------: | ---------------------------- | ------------------- | ------------------------- |
| 한미반도체  | 2024-03-26 종가 필요 / 2024-03-28 장중 139,100원 anchor | needs_ohlc_backfill          | needs_ohlc_backfill | needs_ohlc_backfill       |
| 가온칩스   |                                       Stage 3 없음 | Stage 2 기준 backfill          | N/A                 | needs_ohlc_backfill       |
| 삼성전자   |                                       Stage 3 없음 | Stage 2 watch 기준 backfill    | N/A                 | 2026 AI rally 구간 backfill |
| DB하이텍  |                                       Stage 3 없음 | 정책 이벤트 기준 backfill           | N/A                 | needs_ohlc_backfill       |
| 이수페타시스 |                                       Stage 3 없음 | narrative 기준 backfill        | N/A                 | needs_ohlc_backfill       |
| SK하이닉스 |                                 기존 case backfill | 대형 MFE 확인, exact 수치 backfill | 기존 case backfill    | 2026 4B price backfill    |

핵심은 이거다.

```text
한미반도체:
Stage 3 후보 가능.
단, 4B도 빨리 붙어야 함.

가온칩스:
Stage 2까지만.
Stage 3는 양산/매출/마진 전 금지.

삼성전자:
2025년 HBM catch-up은 Stage 3 금지.
2026년 랠리는 별도 4B-watch로 분리.

DB하이텍:
정책 이벤트는 Stage 1~2.
회사 매출 evidence 전 Green 금지.

이수페타시스:
AI PCB narrative는 주목 대상.
하지만 고객/계약/마진/EPS 전 Green 금지.

SK하이닉스:
Stage 3 성공 anchor가 아니라 이제 4B benchmark.
```

---

# 8. score-price alignment 판정

```text
한미반도체:
alignment = aligned
단, 2024-03-28 Micron 미확인 보도 급등은 4B-watch / price_ahead_of_confirmed_customer

가온칩스:
alignment = unknown_insufficient_evidence
design win은 강하지만 Stage 3-Green 아님

삼성전자:
alignment = evidence_good_but_price_failed 또는 failed_rerating
2025년 HBM catch-up에 Green을 줬다면 false_positive_score

DB하이텍:
alignment = event_premium
정책 파운드리 테마만으로 Green 금지

이수페타시스:
alignment = price_moved_without_evidence 후보
DART/리포트/가격 backfill 전 insufficient_evidence

SK하이닉스:
alignment = aligned
단, 신규 Stage 3가 아니라 4B-watch benchmark
```

---

# 9. 점수비중 교정

## 올릴 축

```text
customer_visibility +3
order_to_revenue_conversion +3
hbm_capacity_bottleneck +3
gross_margin_visibility +3
eps_revision +3
customer_diversification_confirmed +2
advanced_packaging_direct_link +2
price_path_alignment +2
```

한미반도체처럼 고객·제품·장비·HBM 병목이 실제로 연결되는 경우는 R2 Stage 3-Green 후보로 볼 수 있다. 다만 이때도 매출 인식과 마진 확인이 필요하다.

## 내릴 축

```text
ai_keyword -4
server_theme -3
design_win_without_revenue -3
policy_foundry_without_order -3
media_report_without_company_confirmation -3
stock_price_rally_before_evidence -4
customer_name_unknown -2
margin_unknown -2
```

가온칩스, DB하이텍, 이수페타시스 때문에 이 감점축이 필요하다. R2는 narrative가 너무 강해서, 가격이 증거보다 먼저 달리는 경우가 많다.

## Green gate 강화 조건

R2 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. company-level customer evidence
2. order / contract / shipment / design win의 질 구분
3. 매출 인식 가능성
4. gross margin 또는 OPM 개선
5. EPS/FCF revision
6. 고객 다변화 또는 장기 수요
7. 가격경로가 증거 이후 따라왔는지 확인

금지:
AI 이름
HBM 단어
서버 테마
증권사 목표가만 있음
미확인 media report
정책 수혜만 있음
주가가 먼저 움직임
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~3배 이상 상승
미확인 고객 다변화 보도에 급등
HBM/AI CAPEX consensus가 한쪽으로 몰림
신규 수주에도 주가 반응 둔화
forward PER / PBR이 기존 산업 프레임을 완전히 벗어남

4B-elevated:
HBM 공급망 전반이 한꺼번에 급등
고객 CAPEX가 이미 모두 가격에 반영
장비주가 수주보다 valuation으로 움직임
정책/미디어/고객루머가 가격을 끌고 감

4B-graduated:
실적 beat에도 주가가 못 감
신규 고객에도 추가 rerating이 약함
장비 order peak 우려가 등장
```

## 4C hard gate 조건

```text
HBM 고객 qualification 실패
order push-out
customer capex cut
HBM/메모리 가격 하락
capacity oversupply
고객 집중 리스크 현실화
파업/생산차질 장기화
회계/공시 신뢰 훼손
IP leakage / 기술유출
circular AI financing 확인
유상증자/CB로 기존 thesis 희석
```

삼성전자의 파업 리스크는 아직 hard 4C가 아니다. 하지만 생산 차질, 고객 품질 우려, HBM 납품 지연, EPS 하향으로 이어지면 4C 후보로 승격해야 한다. ([Reuters][6])

---

# 10. shadow-only 기록

이번 R2 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_121.md
docs/checkpoints/checkpoint_28a_round121_r2_loop7_ai_semiconductor_price_validation.md
src/e2r/sector/round121_r2_loop7_ai_semiconductor.py
data/e2r_case_library/cases_r2_loop7_round121.jsonl
data/sector_taxonomy/score_weight_profiles_round121_r2_loop7_v7.csv
output/e2r_round121_r2_loop7_ai_semiconductor/
```

---

# 이번 R2 Loop 7 결론

R2 점수표의 방향은 맞다. 하지만 **Stage 3를 너무 쉽게 주면 바로 망가진다.**

이번 라운드에서 얻은 교정은 이거다.

```text
1. HBM 장비주는 Stage 3 가능성이 있다.
   단, 고객·수주·매출·마진·EPS가 연결되어야 한다.

2. AI칩 디자인하우스는 design win만으로 Stage 3가 아니다.
   양산, 매출 인식, margin이 필요하다.

3. 삼성 HBM catch-up은 2025년에는 Stage 3-Green이 아니었다.
   HBM sales decline, Nvidia lag, 반도체 이익 감소가 있었기 때문이다.

4. 정책성 파운드리와 AI칩 육성책은 Stage 1~2 attention이다.
   회사 단위 revenue conversion 전 Green 금지다.

5. AI PCB/기판주는 반드시 고객·계약·마진·EPS backfill이 필요하다.
   가격이 먼저 뛰면 price_moved_without_evidence로 둔다.

6. SK하이닉스는 이제 신규 Stage 3가 아니라 4B benchmark다.
   대시세 이후 valuation/crowding/고객 가격저항/CAPA 정상화를 감시해야 한다.
```

한 문장으로 압축하면:

> **R2에서 진짜 Stage 3는 “AI 반도체”라는 이름이 아니라, AI 병목이 고객 주문·매출 인식·마진·EPS/FCF로 내려오는 순간이다.**
> **그리고 R2는 4B가 빨리 붙어야 한다. HBM·AI 장비주는 맞는 논리라도 가격이 너무 빨리 논리를 앞질러 간다.**

[1]: https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996?utm_source=chatgpt.com "South Korean Chip Shares Rally as AI Frenzy Persists"
[2]: https://www.wsj.com/articles/hanmi-semiconductor-climbs-after-media-reports-of-possible-deal-with-micron-e85398fb?utm_source=chatgpt.com "Hanmi Semiconductor Climbs After Media Reports of Possible Deal With Micron"
[3]: https://www.reuters.com/technology/artificial-intelligence/samsung-electronics-wins-cutting-edge-ai-chip-order-japans-preferred-networks-2024-07-09/?utm_source=chatgpt.com "Samsung Electronics wins cutting-edge AI chip order from Japan's Preferred Networks"
[4]: https://www.reuters.com/business/samsung-electronics-operating-profit-rises-slightly-q1-2025-04-30/?utm_source=chatgpt.com "Samsung Elec drops Q2 outlook due to trade uncertainties"
[5]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/?utm_source=chatgpt.com "Korea's KOSPI breaks 7,000 as AI rally catapults Samsung into $1 trillion club"
[6]: https://www.reuters.com/business/world-at-work/samsung-electronics-its-south-korean-union-resume-pay-talks-strike-risks-loom-2026-05-18/?utm_source=chatgpt.com "Samsung Electronics, union hold last-ditch talks to avert strike threatening global supply chains"
[7]: https://www.reuters.com/world/asia-pacific/south-korea-consider-setting-up-31-bln-foundry-grow-local-chip-sector-2025-12-10/?utm_source=chatgpt.com "South Korea to consider setting up $3.1 bln foundry to grow local chip sector"
[8]: https://en.wikipedia.org/wiki/Isu_Group?utm_source=chatgpt.com "Isu Group"
[9]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[10]: https://www.reuters.com/world/asia-pacific/sk-hynix-invest-nearly-13-bln-chip-packaging-plant-south-korea-2026-01-13/?utm_source=chatgpt.com "SK Hynix to invest nearly $13 bln in chip packaging plant in South Korea"
