# Round 7 Case Validation Framework

Round 7은 점수비중을 바꾸기 전, 케이스 라이브러리가 “성공”과 “반례”를 더 엄격히 구분하도록 만든 calibration 문서다.

쉬운 예시:

```text
주가가 많이 올랐다
하지만 EPS/FCF 상향이나 반복 매출 증거가 없다
= 구조적 E2R 성공이 아니라 테마/이벤트 반례
```

## Success Case

성공 사례 후보는 다음을 같이 만족해야 한다.

- evidence score가 높다.
- Stage 2 또는 Stage 3에 해당하는 근거가 있다.
- 그 근거 이후 주가 리레이팅이 확인된다.
- EPS/OP/FCF revision이 동행한다.
- 빠른 4C가 없다.

## Counterexample

반례는 “나쁜 회사”가 아니라 점수체계가 속을 수 있는 사례다.

- 주가 급등은 있었지만 EPS/FCF 증거가 없다.
- 점수는 높았지만 주가 리레이팅이 없었다.
- EPS가 폭발했지만 다음 해 정상화되었다.
- Stage 2 이후 빠른 4C가 왔다.
- 공개매수, 정책, 경영권 분쟁 같은 event premium만 있었다.

## Round 7 Archetype Posture

- `GREEN_ELIGIBLE_AFTER_VALIDATION`: 향후 Green shadow scoring 후보지만 성공/반례와 가격 경로가 먼저 필요하다.
- `WATCH_YELLOW_DEFAULT`: 기본은 Stage 3-Watch/Yellow다. 반복성, FCF, 낮은 리스크가 있어야 Green을 검토한다.
- `REDTEAM_GUARDRAIL`: RedTeam과 4B/4C 방어가 우선이다.

## Specific Corrections

- Platform/Software: MAU나 AI narrative가 아니라 ARPU, take-rate, OPM, FCF가 필요하다.
- Game/IP: 신작 기대와 출시 후 반복 monetization을 분리한다.
- Travel/Leisure: reopening rebound와 구조적 수익성 개선을 분리한다.
- Construction/Credit: 수주보다 PF, 유동성, 현금흐름 리스크가 먼저다.
- Retail: 매출 회복보다 OPM, 재고, 온라인 경쟁, 고객 mix가 중요하다.
- CDMO: pre-revenue biotech이 아니라 장기 생산계약, 가동률, FCF로 본다.
- Royalty biotech: 임상 headline이 아니라 approval -> commercialization -> royalty/revenue 경로가 필요하다.
- Holding/Governance: event premium과 NAV/FCF 기반 구조적 rerating을 분리한다.
- Financial: 저PBR만으로는 부족하고 ROE, CET1, credit cost, 주주환원 실행이 필요하다.
- Rare Metals: 금속가격 상승, 공개매수, 전략소재 bottleneck을 분리한다.

## What Not To Change

- Stage 3-Green 기준을 낮추지 않는다.
- 케이스 라이브러리를 candidate generation input으로 쓰지 않는다.
- 주가 급등을 EPS/FCF evidence로 바꾸지 않는다.
- price path가 없는 케이스로 score weight를 바꾸지 않는다.
