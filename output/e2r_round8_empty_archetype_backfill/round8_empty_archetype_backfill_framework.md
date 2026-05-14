# Round-8 Empty-Archetype Backfill Framework

Source round: `docs/round/round_08.md`

이 문서는 calibration 전용이다. production scoring과 StageClassifier threshold를 바꾸지 않는다.

## 핵심

Round 8은 빈 archetype과 얇은 archetype을 성공/반례/가격경로까지 채우기 위한 계획이다.

쉬운 예시:

`흑자전환`이 한 번 나왔다고 성공이 아니다. OPM과 FCF가 2분기 이상 이어지고 주가가 그 이후 리레이팅돼야 성공 후보가 된다.

## Targets

| archetype | priority | focus |
|---|---|---|
| TURNAROUND_COST_RESTRUCTURING | HIGH | 적자에서 흑자 전환이 아니라 비용구조 변화와 FCF 지속성을 검증한다. |
| COMMODITY_SPREAD | REDTEAM | Refining, chemical, steel/metal spread를 분리하고 중국 공급과잉/재고 반례를 채운다. |
| AUTO_MOBILITY_COMPLETED_VEHICLE | MEDIUM | 완성차는 hybrid/mix/shareholder return과 저PBR 프레임 해소를 검증한다. |
| AUTO_MOBILITY_COMPONENTS | MEDIUM | 부품주는 고객 다변화와 원가전가가 완성차보다 더 중요하다. |
| FINANCIAL_SPREAD_BALANCE_SHEET | HIGH | ROE-PBR-CET1-주주환원 실행으로 value trap을 분리한다. |
| VALUE_UP_SHAREHOLDER_RETURN | HIGH | 저PBR/지주 이벤트와 실제 자사주 소각, 반복 환원, NAV/FCF 개선을 분리한다. |
| CDMO_HEALTHCARE_CONTRACT | HIGH | CDMO는 pre-revenue biotech이 아니라 장기계약, capacity, 가동률, FCF archetype이다. |
| BIOTECH_ROYALTY_COMMERCIALIZATION | WATCH | Approval -> commercialization -> royalty/revenue 경로를 pre-revenue 임상 뉴스와 분리한다. |
| PLATFORM_SOFTWARE_INTERNET | WATCH | 좋은 회사와 E2R 성공사례를 분리하고 ARPU/OPM/FCF를 확인한다. |
| SHIPPING_FREIGHT_CYCLE | REDTEAM | EPS 폭발이 가능하지만 운임 정상화/overcapacity로 cycle boom-bust를 분리한다. |
| NUCLEAR_SMR_GRID_POLICY | WATCH | 원전은 정책 + 수주 + 법적 리스크 + 기자재 매출화 archetype이다. |
| AI_DATA_CENTER_INFRASTRUCTURE | HIGH | AI 데이터센터 capex가 전력기기, 전선, IDC, 냉각, PCB, ESS로 번지는지 검증한다. |
| MEMORY_HBM_CAPACITY | HIGH | SK Hynix류 성공과 4B-watch를 동시에 캘리브레이션한다. |

## Guardrails
- 케이스 레코드는 candidate generation input이 아니다.
- Stage 3-Green을 늘리기 위해 threshold를 낮추지 않는다.
- price-only, event-only, one-off EPS는 반드시 반례로 남긴다.
