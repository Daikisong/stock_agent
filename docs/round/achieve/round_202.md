좋아. 순서상 이번은 **R11 Loop 7 — 정책·지정학·재난·이벤트 가격경로 검증 라운드**로 진행한다.

이번 R11은 다른 섹터보다 더 엄격해야 한다. R11의 기본값은 **Green이 아니라 Event / Watch / RedTeam**이다. 정책, MOU, 자원 발견, 질병, 전쟁, 재난, 과학 테마는 주가를 먼저 밀 수 있지만, E2R Stage 3는 **계약·예산·financing·실제 발주·매출 인식·EPS/FCF revision**으로 승격될 때만 가능하다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
large_sector = POLICY_GEOPOLITICAL_EVENT
round = R11 Loop 7 / price-path validation
목표 = Stage 3 / 4B / 4C가 실제 가격경로와 맞았는지 검증하고 shadow weight 보정
```

R11의 기본 영역은 남북정책, 재건, 기후·재난, 질병·해충, speculative science, advanced material theme, local policy, one-off demand, theme overheat다. Round 40 기준 R11 validation focus는 `event_date`, `contract_absence`, `mfe_5d_20d_60d`, `drawdown_after_news_fade`, `eps_fcf_absence`다. 

Round 119 기준으로 R11에서 부족한 증거는 `policy_news`, `mou`, `geopolitical_headline`이고, 필요한 증거는 `contract`, `budget`, `financing`, `actual_order`, `revenue_conversion`이다. Green blocker는 `policy_reversal`, `unfunded_budget`, `event_fade`다. 

---

# 2. 대상 canonical archetype

```text
DOMESTIC_RESOURCE_DISCOVERY_EVENT
ENERGY_SECURITY_POLICY_EVENT
EVENT_PRICE_RALLY_NOT_STAGE3
POLICY_DIRECTIONALITY_ERROR
GEOPOLITICAL_RECONSTRUCTION
REAL_RECONSTRUCTION_FINANCING
CRITICAL_INFRA_RECONSTRUCTION_FINANCING
NORTH_KOREA_POLICY_EVENT
CLIMATE_DISASTER_EVENT
EVENT_DISEASE_PEST_DEMAND
GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE
PUBLIC_HEALTH_PROCUREMENT_REVERSAL
SPECULATIVE_SCIENCE_THEME
ADVANCED_MATERIAL_SPECULATIVE_THEME
POLICY_LOCAL_THEME
MARKET_STRUCTURE_SHORT_SELLING_POLICY
POLICY_MARKET_SHOCK_EVENT
```

이번 R11의 핵심 질문은 이거다.

```text
이 회사는 정책·지정학·재난·과학 테마로 오른 것인가?
아니면 그 이벤트가 계약·예산·발주·매출·EPS/FCF로 승격됐는가?
```

---

# 3. deep sub-archetype

```text
자원 발견 / 에너지 안보:
- East Sea offshore oil and gas
- 대왕고래 / 동해 가스전
- Korea Gas
- Korea National Oil / government exploration
- drilling approval
- probability of discovery
- exploration cost
- reserve estimate vs commercial confirmation

원전 / SMR / 전략산업 정책:
- Czech nuclear preferred bidder
- KHNP / Doosan Enerbility
- X-energy / AWS SMR cooperation
- Fermi America AI power project
- non-binding strategic investment
- policy-to-contract escalation
- equipment order / backlog conversion

질병·해충 이벤트:
- Brazil bird flu
- poultry import ban
- Harim / Maniker-style poultry basket
- import restriction
- regional ban reversal
- one-off disease demand
- feed cost / inventory / price pass-through

과학·테마 이벤트:
- LK-99
- room-temperature superconductor claim
- replication failure
- Korean superconductor stocks
- speculative science theme
- event fade

시장구조 / 정치 shock:
- martial law shock
- impeachment/political unrest
- short-selling ban/resumption
- MSCI developed market watch
- liquidity support
- broad-market risk-off

재건 / 지정학:
- Ukraine reconstruction
- North Korea policy
- U.S. shipbuilding policy
- strategic supply chain export control
- MOU vs funded order
```

---

# 4. 국장 신규 후보 case

## Case A — 한국가스공사 `event_premium / price_moved_without_evidence`

```text
symbol = 036460
archetype = DOMESTIC_RESOURCE_DISCOVERY_EVENT / ENERGY_SECURITY_POLICY_EVENT
case_type = event_premium / price_moved_without_evidence
```

한국가스공사는 R11에서 가장 전형적인 “자원 발견 이벤트는 Stage 3가 아니다” 케이스다. 2024년 6월 윤석열 대통령은 동해 심해 가스·석유 탐사를 승인했고, 정부는 최대 140억 배럴 규모의 석유·가스 가능성을 언급했다. 다만 시추 성공률은 20%로 보도됐고, 초기 시추는 2024년 말부터 시작해 2025년 상반기 결과를 기대하는 구조였다. 이 뉴스 이후 서울 에너지주가 뛰었고, 한국가스공사 주가는 장중 최대 30% 급등했다. ([Reuters][1])

### stage date 후보

```text
Stage 1:
2024-06-03
- 대통령의 동해 석유·가스 탐사 승인
- 최대 140억 배럴 가능성 언급
- 에너지 안보 / domestic resource discovery theme

Stage 2:
보류
- 실제 시추 결과, 경제성, 매장량 확정, 개발계획 전에는 약한 Stage 1~2

Stage 3:
없음
- reserve estimate와 exploration approval만으로 EPS/FCF 체급 변화 없음
- 상업 생산, 개발비, 회수기간, 가스 판매계약 확인 필요

Stage 4B:
2024-06-03
- 한국가스공사 장중 +30%
- price moved before evidence

Stage 4C:
시추 실패, 경제성 부재, 개발 지연, 정책 후퇴 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2024-06-03 OHLC backfill 필요.

MFE_5D / 20D / 60D:
resource discovery event premium 검증용으로 필요.

MAE_30D / 90D:
event fade 검증 필요.

below_stage3_price_flag:
N/A

peak_price:
2024-06-03 장중 급등 anchor 존재, exact OHLC backfill 필요.

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = price_moved_without_evidence
rerating_result = event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### 교정 포인트

한국가스공사는 R11에서 `domestic_resource_discovery`를 절대 Stage 3로 바로 올리면 안 된다는 기준점이다.

```text
올릴 수 있는 것:
resource_discovery_attention
exploration_budget
drilling_start

Stage 3 금지:
reserve_unconfirmed
commerciality_unknown
development_cost_unknown
revenue_conversion_absent
```

---

## Case B — 두산에너빌리티 `success_candidate / policy-to-contract watch`

```text
symbol = 034020
archetype = ENERGY_SECURITY_POLICY_EVENT / NUCLEAR_SMR_GRID_POLICY
case_type = success_candidate
```

두산에너빌리티는 R11에서 정책 이벤트가 Stage 2까지 승격될 수 있는 케이스다. 2024년 7월 체코 정부는 한국수력원자력을 신규 원전 2기 건설 우선협상대상자로 선정했고, Reuters는 이 발표 뒤 두산에너빌리티, 한전기술, 한전KPS 등 관련 한국 원전주가 상승했다고 보도했다. 다만 최종 계약, 금액, 실제 장비 수주로 내려오기 전에는 Stage 3가 아니다. ([Reuters][2])

2025년 8월 한미 정상회담 관련 투자 패키지에서는 KHNP와 두산에너빌리티가 X-energy, Amazon Web Services와 SMR 설계·건설·공급망 협력에 참여했고, 두산에너빌리티가 Fermi America의 Texas AI 프로젝트에 원전·SMR 장비를 공급하는 합의도 나왔다. 이것도 강한 Stage 2 후보지만, MOU·협력·장비 공급 합의가 실제 수주잔고와 EPS로 연결되는지 확인해야 한다. ([Reuters][3])

### stage date 후보

```text
Stage 1:
2024-07-17
- 체코 원전 우선협상대상자 선정
- 한국 원전 수출 재개 기대

Stage 2:
2025-08-26
- X-energy / AWS / Fermi America SMR·AI power 프로젝트 협력
- Doosan Enerbility 장비 공급 합의
- nuclear + AI data center power theme

Stage 3:
보류
- final contract, equipment order, backlog, margin, EPS revision 확인 전 Green 금지

Stage 4B:
원전/SMR 테마로 주가가 먼저 과열되면 후보

Stage 4C:
최종 계약 실패, 법적 분쟁, financing 지연, SMR 프로젝트 취소, 원전정책 후퇴 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2024-07-17 OHLC backfill 필요.

stage2_price:
2025-08-26 OHLC backfill 필요.

MFE_30D / 90D / 180D / 1Y:
Stage 1/2 각각 backfill 필요.

MAE_30D / 90D / 180D:
needs_ohlc_backfill

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
policy/SMR event fade 기준 backfill 필요
```

### score-price alignment

```text
alignment = success_candidate
rerating_result = policy_to_contract_watch
stage_failure_type = stage2_watch_success 후보
```

### 교정 포인트

두산에너빌리티는 R11에서 `policy_to_contract_escalation`을 보여준다. 다만 Stage 3는 **우선협상대상자·MOU가 아니라 장비 수주와 마진**이다.

```text
Stage 2 가능:
preferred_bidder
strategic_MOU
equipment_supply_agreement

Stage 3 조건:
final_contract
equipment_backlog
margin_visibility
cash_flow
EPS_revision
```

---

## Case C — HD현대 / 삼성중공업 U.S. 조선정책 `success_candidate / MOU-watch`

```text
symbols = 267250 / 010140
archetype = GEOPOLITICAL_RECONSTRUCTION / STRATEGIC_INDUSTRIAL_POLICY
case_type = success_candidate / MOU-watch
```

R11에서 미국 조선 재건 정책은 중요한 테마다. 2025년 8월 한미 정상회담 투자 패키지에서 HD현대는 한국산업은행과 함께 Cerberus Capital과 미국 해양 역량 강화를 위한 대형 공동펀드 MOU를 체결했고, 삼성중공업은 Vigor Marine Group과 미국 해군 지원함 MRO, 조선소 현대화, 공동 건조 관련 preliminary deal을 맺었다. 이건 R1 조선·방산과도 겹치지만, R11에서는 **정책·지정학 이벤트가 실제 수주로 승격되는지**를 보는 case다. ([Reuters][3])

### stage date 후보

```text
Stage 1:
2025-08-26
- 한미 전략산업 투자 패키지
- 미국 조선 재건 / MRO / 해군 지원함 theme

Stage 2:
보류 또는 약한 Stage 2
- HD현대 MOU, 삼성중공업 preliminary deal
- 아직 funded order / backlog / margin 확인 전

Stage 3:
없음
- MOU / preliminary deal만으로 Green 금지

Stage 4B:
미국 조선 재건 테마로 관련주가 선반영되면 후보

Stage 4C:
MOU 불발, 예산 미반영, 미 해군 발주 지연, 현지 조선소 integration 실패 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2025-08-26 관련주별 OHLC backfill 필요.

MFE_5D / 20D / 60D:
policy event basket 기준 backfill 필요.

MAE_30D / 90D:
event fade 확인 필요.

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = success_candidate / event_premium_watch
rerating_result = policy_event_rerating_candidate
stage_failure_type = stage1_or_stage2_attention_only
```

### 교정 포인트

이 케이스는 R11에서 `MOU`를 Stage 3로 올리면 안 된다는 기준이다.

```text
MOU:
Stage 1~2

Stage 3 조건:
funded order
contract amount
duration
margin
delivery schedule
revenue conversion
```

---

## Case D — 하림 / 마니커류 poultry basket `event_premium / disease-demand watch`

```text
symbols = poultry basket, e.g. Harim / Maniker류
archetype = EVENT_DISEASE_PEST_DEMAND
case_type = event_premium / insufficient_evidence
```

2025년 5월 브라질에서 상업 농장 조류독감이 확인되자 중국·EU·한국 등 주요 수입국이 브라질산 닭고기에 수입제한을 걸었다. Reuters는 브라질이 세계 최대 닭고기 수출국이고, 한국도 초기에는 전국 단위 수입금지 프로토콜을 적용했다고 보도했다. 이후 2025년 6월 한국은 브라질이 상업농장 조류독감 청정 상태를 회복했다고 발표한 뒤, 제한을 전국 단위에서 affected region 중심으로 완화했다. ([Reuters][4])

이 이벤트는 국내 poultry basket에는 단기 가격 모멘텀을 줄 수 있지만, Stage 3는 아니다. 국내 상장 육계 기업의 매출·마진·원가·재고·사료비·가격전가가 확인되어야 한다.

### stage date 후보

```text
Stage 1:
2025-05-19
- 브라질 조류독감
- 한국 등 수입제한
- 국내 poultry substitution theme

Stage 2:
보류
- 국내 업체별 판매가격, 출하량, 마진 확인 필요

Stage 3:
없음
- disease event만으로 Green 금지

Stage 4B:
국내 육계주가 수입금지 뉴스만으로 급등하면 event premium / 4B-watch

Stage 4C:
2025-06-23
- 한국이 제한을 지역 단위로 완화
- event thesis fade 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2025-05-19 poultry basket OHLC backfill 필요.

MFE_5D / 20D / 60D:
disease event premium 검증용으로 필요.

MAE_30D / 90D:
import restriction easing 이후 fade 확인 필요.

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
rerating_result = one_off_disease_event
stage_failure_type = stage1_attention_only
```

### 교정 포인트

R11 질병 이벤트는 대부분 Stage 3가 아니다.

```text
Stage 1:
질병 / 수입금지 / 공급차질

Stage 3 조건:
국내 업체의 가격전가
판매량 증가
마진 개선
사료비 통과
재고 정상
반복 수요
```

---

## Case E — LK-99 / 초전도체 basket `overheat / thesis_break`

```text
symbols = 신성델타테크·서남·모비스류 초전도체 basket
archetype = SPECULATIVE_SCIENCE_THEME / ADVANCED_MATERIAL_SPECULATIVE_THEME
case_type = overheat / thesis_break
```

LK-99는 R11 speculative science의 교과서적 반례다. 2023년 7월 한국 연구진은 arXiv preprint에서 LK-99가 상온·상압 초전도체라고 주장했다. 그러나 이후 여러 재현 시도와 검증 과정에서 실온 초전도체라는 결론은 받아들여지지 않았고, LK-99 관련 문헌 요약은 2023년 8월 중순까지 순수 LK-99가 실온 초전도체가 아니며, 관찰된 현상은 Cu₂S 불순물이나 통상적 자기 반응으로 설명될 수 있다는 쪽으로 정리됐다. ([arXiv][5])

또 LK-99 문헌 요약은 초기 흥분 속에서 한국·중국 기술주가 올랐지만, 검증 의문과 Nature 보도 이후 한국 초전도체 관련주가 추가로 하락했다고 정리한다. 이 케이스는 R11에서 “과학 헤드라인 → 주가 급등 → 재현 실패 → thesis break” 구조다. ([위키백과][6])

### stage date 후보

```text
Stage 1:
2023-07-22
- LK-99 arXiv preprint
- room-temperature superconductor claim

Stage 2:
없음
- peer review, independent replication, commercial pathway 없음

Stage 3:
없음
- 과학 claim만으로 Green 금지

Stage 4B:
2023-08 초
- 초전도체 관련주 급등 / meme-science rally

Stage 4C:
2023-08 중순
- independent replication failure / scientific consensus reversal
- thesis break
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage1_price:
2023-07-24 이후 basket OHLC backfill 필요.

MFE_5D / 20D:
speculative science event premium 검증용.

MAE_30D / 90D:
replication failure 이후 drawdown 확인 필요.

below_stage3_price_flag:
N/A

peak_price:
초전도체 basket별 backfill 필요.

drawdown_after_peak:
needs_ohlc_backfill
```

### score-price alignment

```text
alignment = thesis_break / price_moved_without_evidence
rerating_result = theme_overheat
stage_failure_type = should_have_been_stage1_or_red
```

### 교정 포인트

R11에서 speculative science는 거의 무조건 Green 금지다.

```text
preprint:
Stage 1

independent replication:
Stage 2 후보

commercial contract / validated product / revenue:
Stage 3 후보

replication failure:
4C / thesis break
```

---

## Case F — 2024 계엄·정치 shock `policy_market_shock / hard market RedTeam`

```text
symbol = broad KOSPI / politically sensitive Korea basket
archetype = POLICY_MARKET_SHOCK_EVENT / POLITICAL_SYSTEM_SHOCK_KOREA
case_type = 4C-watch / market shock
```

2024년 12월 윤석열 대통령의 비상계엄 선포와 해제는 R11의 정치 shock 기준점이다. Reuters는 비상계엄이 신속히 철회됐음에도 아시아 증시가 흔들렸고, KOSPI가 거의 2% 하락했으며, 원화가 2년 저점 부근에 머물렀다고 보도했다. 정부와 한국은행은 시장 안정화를 위해 유동성 공급과 안정조치를 언급했다. ([Reuters][7])

이건 개별 종목 Stage 3/4C라기보다, 전체 한국시장 risk premium과 외국인 수급에 영향을 주는 `policy_market_shock`이다. R11에서는 이런 사건을 sector score에 직접 넣기보다, 모든 R1~R12 case의 `macro_policy_shock_overlay`로 둬야 한다.

### stage date 후보

```text
Stage 1:
2024-12-03
- 비상계엄 선포

Stage 2:
없음
- positive stage 아님

Stage 3:
없음

Stage 4B:
해당 없음

Stage 4C:
2024-12-04
- KOSPI 급락, 원화 약세, 정치 불확실성
- market-level policy shock
```

### 가격경로 검증

```text
stage3_price:
없음.

stage4c_price:
2024-12-04 KOSPI / sector basket / individual names OHLC backfill 필요.

MFE / MAE:
사건 전후 5D / 20D / 60D 기준 필요.

below_stage3_price_flag:
N/A

peak_price:
N/A

drawdown_after_peak:
market shock drawdown backfill 필요
```

### score-price alignment

```text
alignment = thesis_break_watch / macro_policy_shock
rerating_result = market_risk_premium_event
stage_failure_type = macro_redteam_overlay
```

### 교정 포인트

정치 shock은 개별 회사의 Stage 3 논리를 바꾸지 않을 수도 있지만, **위험프리미엄과 외국인 수급**을 바꾼다. 따라서 R11에서 broad overlay로 둬야 한다.

```text
개별 종목 score:
직접 변경하지 않음

단,
macro_risk_penalty
foreign_outflow_risk
FX_volatility
liquidity_support_watch
```

---

## Case G — 공매도 재개 / MSCI 접근성 `market_structure_event / not company Green`

```text
symbol = broad market / securities basket
archetype = MARKET_STRUCTURE_SHORT_SELLING_POLICY
case_type = success_candidate / event_premium
```

2025년 한국은 5년 만에 전면 공매도 금지를 해제했고, MSCI는 한국의 공매도 접근성 평가가 개선됐다고 밝혔다. Reuters는 공매도 금지 해제가 외국인 투자자와 MSCI 시장 접근성의 핵심 이슈였고, MSCI 선진국 편입 기대와 연결됐다고 보도했다. 다만 MSCI는 외환시장 접근성 등 다른 제약도 남아 있다고 지적했다. ([Reuters][8])

이건 좋은 시장구조 이벤트지만, 개별 증권주나 금융주를 Stage 3로 만들지는 않는다. 시장 접근성 개선이 거래대금, 외국인 자금 유입, 브로커 수익, 밸류에이션으로 내려와야 Stage 2~3가 된다.

### stage date 후보

```text
Stage 1:
2025-03
- 5년 만의 공매도 전면 재개
- MSCI 접근성 개선 기대

Stage 2:
2025-06-20
- MSCI가 short-selling market accessibility 개선 언급

Stage 3:
없음
- 개별 증권사 이익, 거래대금, 외국인 유입, 수수료 수익 확인 필요

Stage 4B:
MSCI/선진국 편입 기대가 시장 전체를 먼저 밀면 후보

Stage 4C:
불법 공매도 재발, 시장 신뢰 훼손, MSCI watchlist 실패, 외환 접근성 문제 지속 시 후보
```

### 가격경로 검증

```text
stage3_price:
없음. Stage 3 미부여.

stage2_price:
2025-06-20 broad market / securities basket OHLC backfill 필요.

MFE_30D / 90D / 180D:
market structure event 기준 backfill 필요.

MAE_30D / 90D:
needs_ohlc_backfill

below_stage3_price_flag:
N/A

peak_price:
needs_ohlc_backfill

drawdown_after_peak:
event fade / MSCI decision 이후 backfill 필요
```

### score-price alignment

```text
alignment = success_candidate / event_premium
rerating_result = market_structure_watch
stage_failure_type = stage2_evidence_not_green
```

### 교정 포인트

시장구조 이벤트는 강하지만, R11에서는 “국장 전체의 valuation frame”을 바꿀 수 있는 조건으로만 둬야 한다.

```text
Stage 3 조건:
외국인 순유입 지속
거래대금 증가
증권사 이익 증가
시장 multiple expansion
MSCI watchlist / upgrade path 구체화
```

---

# 5. 이번 R11 case별 요약표

| case                  | 분류                            | Stage 3 판정 |                  4B/4C 판정 | 가격경로 1차 판단                                     |
| --------------------- | ----------------------------- | ---------: | ------------------------: | ---------------------------------------------- |
| 한국가스공사 / 동해 가스        | event_premium                 |         없음 |         +30% 급등은 4B-watch | reserve estimate는 Stage 1, 시추·상업성 전 Green 금지   |
| 두산에너빌리티 / 원전·SMR      | success_candidate             |         보류 |         원전/SMR 테마 과열 시 4B | preferred bidder/MOU는 Stage 2, 장비수주 전 Green 금지 |
| HD현대·삼성중공업 U.S. 조선    | success_candidate / MOU-watch |         없음 |            정책 이벤트 과열 시 4B | MOU/preliminary deal은 Stage 1~2                |
| 하림/마니커 poultry basket | event_premium                 |         없음 |      수입제한 완화 시 event fade | 질병 수요는 Stage 1, 마진 확인 전 Green 금지               |
| LK-99 초전도체 basket     | overheat / thesis_break       |         없음 |                재현 실패 후 4C | speculative science hard 반례                    |
| 계엄·정치 shock           | macro 4C-watch                |         없음 | market-level policy shock | 개별 case overlay로 사용                            |
| 공매도·MSCI 접근성          | market_structure_watch        |         없음 |         선진국 편입 기대 과열 시 4B | 시장구조 개선은 Stage 2, 기업 EPS 전 Green 금지            |

---

# 6. 각 case별 stage date 후보 요약

```text
한국가스공사:
Stage 1 = 2024-06-03 동해 석유·가스 탐사 승인
Stage 2 = 보류 / 시추 결과·경제성 확인 전
Stage 3 = 없음
Stage 4B = 2024-06-03 장중 +30%
Stage 4C = 시추 실패 / 경제성 부재 / 정책 후퇴 시 후보

두산에너빌리티:
Stage 1 = 2024-07-17 체코 원전 preferred bidder
Stage 2 = 2025-08-26 X-energy/AWS/Fermi SMR 협력·장비공급 합의
Stage 3 = 보류 / final contract·backlog·margin 필요
Stage 4B = 원전/SMR 테마 과열 시 후보
Stage 4C = 계약 실패 / financing 지연 / SMR 취소 시 후보

HD현대·삼성중공업:
Stage 1 = 2025-08-26 미국 조선 재건 MOU/preliminary deal
Stage 2 = 보류 또는 약한 Stage 2
Stage 3 = 없음
Stage 4B = 미국 조선정책 테마 급등 시 후보
Stage 4C = MOU 불발 / 예산 미반영 / 발주 지연 시 후보

Poultry basket:
Stage 1 = 2025-05-19 브라질 조류독감 / 한국 수입제한
Stage 2 = 보류 / 국내 기업 마진 확인 전
Stage 3 = 없음
Stage 4B = 수입금지 뉴스 급등 시 후보
Stage 4C = 2025-06-23 한국 제한 완화로 event fade 후보

LK-99:
Stage 1 = 2023-07-22 arXiv preprint
Stage 2 = 없음
Stage 3 = 없음
Stage 4B = 2023-08 초 speculative rally
Stage 4C = 2023-08 중순 재현 실패 / consensus reversal

계엄·정치 shock:
Stage 1 = 2024-12-03 비상계엄 선포
Stage 2 = 없음
Stage 3 = 없음
Stage 4B = 없음
Stage 4C = 2024-12-04 market-level shock

공매도·MSCI:
Stage 1 = 2025-03 공매도 재개
Stage 2 = 2025-06-20 MSCI 접근성 개선 언급
Stage 3 = 없음
Stage 4B = MSCI 선진국 편입 기대 과열 시 후보
Stage 4C = 규제 신뢰 훼손 / upgrade path 실패 시 후보
```

---

# 7. 가격경로 검증

R11은 정확한 OHLC backfill 없이 수익률을 확정하면 안 된다. 특히 event-driven basket은 5D / 20D / 60D MFE와 30D / 90D MAE가 핵심이다. R11의 “좋은 신호”는 장기 MFE보다 **짧은 MFE 후 fade가 얼마나 빠른지**를 잡는 데 있다.

| case           | stage3_price | MFE/MAE                               | below_stage3 | peak/drawdown                     |
| -------------- | -----------: | ------------------------------------- | ------------ | --------------------------------- |
| 한국가스공사         |   Stage 3 없음 | 2024-06-03 event 기준 MFE_5D/20D/60D 필요 | N/A          | exploration event fade 확인         |
| 두산에너빌리티        |   Stage 3 없음 | 체코/SMR event별 backfill                | N/A          | 원전 테마 peak/drawdown 필요            |
| HD현대·삼성중공업     |   Stage 3 없음 | U.S. shipbuilding policy event 기준     | N/A          | MOU fade 확인                       |
| Poultry basket |   Stage 3 없음 | bird flu import ban 기준                | N/A          | 제한 완화 후 drawdown 필요               |
| LK-99 basket   |   Stage 3 없음 | preprint 이후 MFE_5D/20D                | N/A          | replication failure 후 drawdown 필수 |
| 계엄·정치 shock    |   Stage 3 없음 | market shock 기준 MAE_5D/20D            | N/A          | liquidity support 후 recovery 필요   |
| 공매도·MSCI       |   Stage 3 없음 | market-structure event 기준             | N/A          | MSCI decision fade 필요             |

핵심은 이거다.

```text
R11에서 Stage 3는 거의 항상 보류다.
Event가 계약·예산·매출·EPS/FCF로 승격될 때만 Stage 3를 준다.
```

---

# 8. score-price alignment 판정

```text
한국가스공사:
alignment = price_moved_without_evidence
reserve estimate와 exploration approval만으로 주가가 먼저 움직임.

두산에너빌리티:
alignment = success_candidate
policy-to-contract escalation 후보.
하지만 final contract와 장비 backlog 전 Stage 3 금지.

HD현대·삼성중공업:
alignment = event_premium / success_candidate
MOU·preliminary deal은 attention.
funded order 전 Green 금지.

Poultry basket:
alignment = event_premium
질병·수입금지는 단기 MFE 가능.
반복마진 확인 전 Green 금지.

LK-99:
alignment = thesis_break / price_moved_without_evidence
speculative science hard 반례.

계엄·정치 shock:
alignment = macro_policy_shock
개별 기업 thesis보다 시장 risk premium overlay.

공매도·MSCI:
alignment = market_structure_watch
좋은 제도 변화지만 기업 EPS 전 Stage 3 아님.
```

---

# 9. 점수비중 교정

## 올릴 축

```text
funded_budget +5
actual_contract +5
revenue_conversion +5
financing_secured +4
government_stockpile_order +4
procurement_award +4
commerciality_confirmed +4
independent_replication_or_validation +4
event_to_contract_escalation +4
policy_durability +3
```

R11에서 이벤트가 진짜가 되려면 **계약·예산·발주·매출**이 붙어야 한다. 말은 깃발이고, 돈이 깃대를 세운다.

## 내릴 축

```text
policy_news_only -5
mou_only -5
geopolitical_headline_only -5
resource_estimate_without_drilling -5
preprint_or_science_claim_only -5
disease_import_ban_only -4
tourist_or_reconstruction_policy_only -4
market_structure_reform_without_earnings -3
price_rally_before_contract -5
event_fade_risk -4
```

R11은 감점축이 강해야 한다. 이 섹터는 “맞아 보이는 이야기”가 많고, 그 대부분은 실제 EPS/FCF로 내려오지 않는다.

## Green gate 강화 조건

R11 Stage 3-Green은 앞으로 이렇게 줘야 한다.

```text
필수 gate:
1. 정책/이벤트가 회사 단위 계약으로 승격
2. 계약금액 또는 예산 확인
3. financing 확인
4. 실제 발주 또는 조달계약
5. 매출 인식 가능성
6. margin 또는 EPS/FCF revision 확인
7. event fade가 아니라 반복 수요 확인
8. 가격경로가 증거 이후 따라옴

금지:
정책 뉴스만 있음
MOU만 있음
지정학 headline만 있음
자원 매장 가능성만 있음
질병/재난 이벤트만 있음
preprint/과학 claim만 있음
정부 발표 후 관련주 급등만 있음
```

## 4B 조기감지 조건

```text
4B-watch:
뉴스 발표일 장중 상한가/급등
정책·MOU·자원발견 테마주 동반 급등
과학 preprint 후 관련주 급등
질병·재난 이벤트로 5D/20D 급등
MOU가 계약처럼 가격에 반영
계약 전부터 목표가·테마 리포트 반복

4B-elevated:
후속 공시 없이 가격만 유지
정부 예산/financing이 불명확
시추/검증/재현 결과가 나오기 전 valuation 확장
제도개선 기대가 기업 이익보다 먼저 반영

4B-graduated:
이벤트 후 추가 뉴스에도 주가 반응 둔화
실제 계약 부재로 거래대금 감소
초기 MFE 후 MAE가 커지기 시작
```

## 4C hard gate 조건

```text
시추 실패
경제성 부재
MOU 불발
예산 미반영
정부 정책 후퇴
수입제한 완화로 one-off demand fade
과학 claim 재현 실패
regulatory reversal
정치 shock
제도개선 기대 실패
contract cancellation
financing failure
```

---

# 10. shadow-only 기록

이번 R11 Loop 7은 production scoring에 바로 반영하면 안 된다.

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
needs_ohlc_backfill = true
r11_default_stage3_bias = conservative
```

레포에 넣는다면 파일명은 이렇게 가는 게 자연스럽다.

```text
docs/round/round_130.md
docs/checkpoints/checkpoint_28a_round130_r11_loop7_policy_geopolitical_event_price_validation.md
src/e2r/sector/round130_r11_loop7_policy_geopolitical_event.py
data/e2r_case_library/cases_r11_loop7_round130.jsonl
data/sector_taxonomy/score_weight_profiles_round130_r11_loop7_v7.csv
output/e2r_round130_r11_loop7_policy_geopolitical_event/
```

---

# 이번 R11 Loop 7 결론

R11은 대부분 Stage 3가 아니다. R11의 진짜 임무는 **event premium을 구조적 E2R로 착각하지 않게 막는 것**이다.

```text
1. 한국가스공사 동해 가스 이벤트는 강한 Stage 1이지만,
   시추·경제성·상업화 전 Stage 3가 아니다.

2. 두산에너빌리티 원전·SMR은 Stage 2 후보가 될 수 있다.
   그러나 우선협상자·MOU가 아니라 장비수주·마진·EPS가 Stage 3다.

3. 미국 조선정책 MOU는 좋은 관심 재료지만,
   funded order 전에는 Stage 3 금지다.

4. 조류독감·질병 이벤트는 단기 MFE가 날 수 있지만,
   수입제한 완화가 곧 event fade가 된다.

5. LK-99는 speculative science hard 반례다.
   preprint는 Stage 1이고, 재현 실패는 4C다.

6. 계엄·정치 shock은 개별 기업보다 macro RedTeam overlay로 둬야 한다.

7. 공매도·MSCI 접근성 개선은 시장구조 Stage 2지만,
   개별 기업 EPS/FCF 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R11에서 진짜 Stage 3는 “정책·지정학·재난 뉴스가 크다”가 아니라, 그 뉴스가 계약·예산·financing·발주·매출·EPS/FCF로 승격되는 순간이다.**
> **R11의 기본값은 Green이 아니라 Event Premium이고, 가격이 먼저 뛴 경우 4B-watch를 가장 빨리 붙여야 한다.**

[1]: https://www.reuters.com/world/asia-pacific/skoreas-yoon-says-vast-amount-oil-gas-reserve-possible-off-east-coast-2024-06-03/?utm_source=chatgpt.com "South Korea's Yoon approves exploration of vast oil and gas prospects"
[2]: https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/?utm_source=chatgpt.com "South Korea's winning bid for Czech nuclear power project"
[3]: https://www.reuters.com/business/aerospace-defense/south-korean-firms-pledge-150-billion-us-investments-summit-2025-08-26/?utm_source=chatgpt.com "South Korean firms pledge $150 billion in US investments at summit"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/brazil-can-no-longer-export-poultry-meat-eu-due-bird-flu-2025-05-19/?utm_source=chatgpt.com "Brazil can no longer export poultry and meat to EU due to bird flu"
[5]: https://arxiv.org/abs/2307.12008?utm_source=chatgpt.com "The First Room-Temperature Ambient-Pressure Superconductor"
[6]: https://en.wikipedia.org/wiki/LK-99?utm_source=chatgpt.com "LK-99"
[7]: https://www.reuters.com/markets/global-markets-wrapup-1-2024-12-04/?utm_source=chatgpt.com "Asian stocks slip, rattled by South Korean political unrest"
[8]: https://www.reuters.com/world/asia-pacific/south-koreas-short-selling-accessibility-has-improved-msci-says-2025-06-20/?utm_source=chatgpt.com "South Korea's short-selling accessibility has improved, MSCI says"
