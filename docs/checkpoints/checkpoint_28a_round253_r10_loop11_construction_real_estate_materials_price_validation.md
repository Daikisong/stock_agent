# Checkpoint 28A Round 253 R10 Loop 11 Construction Real Estate Materials Price Validation

## 반영 내용

- `docs/round/round_253.md`의 R10 Loop 11 케이스를 calibration/evaluation 전용 케이스팩으로 반영했다.
- 신규 canonical archetype 별칭을 추가했다.
  - `OVERSEAS_EPC_MEGA_ORDER`
  - `GAS_INFRA_DELIVERY_VALIDATION`
  - `AI_DATA_CENTER_REAL_ASSET`
  - `CONSTRUCTION_SAFETY_REGULATORY_4C`
- 기존 R10 archetype과 함께 다음 축을 비교했다.
  - 해외 EPC 대형 수주
  - 가스 인프라 delivery validation
  - AI 데이터센터 real asset
  - 주택 공급/대출 정책 event
  - PF credit break
  - 건설 안전 규제 4C-watch
  - 건자재 수요 cycle
  - 항만 인프라 delivery

## 핵심 결론

- Samsung E&A Fadhili는 `Stage 2 + 4B-watch`다. 약 60억 달러 계약과 +8.5% 이벤트 가격 반응은 강하지만, 진행매출·마진·운전자본·현금회수 전에는 Green이 아니다.
- Hyundai E&C Jafurah는 gas infra Stage 2다. Aramco/Jafurah 프로젝트 milestone은 좋지만, 상장사 단위 package·margin·cashflow가 필요하다.
- AI 데이터센터 real asset은 Stage 2 후보지만, tenant·NOI/AFFO·전력·용수·인허가·capex per share 전에는 event premium에 머문다.
- 서울 주택정책은 event/policy watch다. 예를 들어 LTV 50%에서 40%로 내려간 것은 정책 변화이지, 건설사의 FCF evidence가 아니다.
- PF/Taeyoung basket은 hard 4C다. PF 연체율이 0.37%에서 2.70%로 상승했고, 40.6조 원 지원은 crisis relief이지 Green 근거가 아니다.
- POSCO E&C/DL Construction 안전 규제는 4C-watch다. 반복 사망사고가 벌금·면허취소·대형 현장중단으로 연결되면 hard 4C로 승격한다.
- Hyundai Steel 철근 proxy는 건자재 demand 4C-watch다. 순이익 추정치 -73%, 철근 가격 -10% 전망은 건설수요 약화를 보여준다.
- Daewoo E&C Grand Faw Port는 delivery Stage 2다. 5개 dock 완공은 단순 수주보다 강하지만, 추가 backlog·margin·cash collection 전에는 Stage 3가 아니다.

## 산출물

- `src/e2r/sector/round253_r10_loop11_construction_real_estate_materials_price_validation.py`
- `src/e2r/cli/build_round253_r10_loop11_report.py`
- `tests/test_round253_r10_loop11_construction_real_estate_materials_price_validation.py`
- `data/e2r_case_library/cases_r10_loop11_round253.jsonl`
- `data/sector_taxonomy/round253_r10_loop11_construction_real_estate_materials_price_validation_audit.json`
- `output/e2r_round253_r10_loop11_construction_real_estate_materials_price_validation/`

## 적용하지 않은 것

- production scoring은 바꾸지 않았다.
- candidate generation input으로 쓰지 않는다.
- full adjusted OHLC가 없는 케이스의 MFE/MAE를 만들지 않았다.
- Stage 3-Green 기준을 낮추지 않았다.

## 쉬운 예시

`as_of_date=2024-04-03`에서 Samsung E&A 계약 뉴스와 +8.5% 가격 반응은 쓸 수 있다. 하지만 2024년 이후에 확인된 공정률, 현금회수, 마진 정보가 그 날짜에 없었다면 그날 Stage 3-Green 판단에는 쓰면 안 된다.
