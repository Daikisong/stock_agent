# Checkpoint 28A Round 292 R10 Loop 14 Construction Real Estate Building Materials Price Validation

## 반영 범위

- 입력 문서: `docs/round/round_292.md`
- analyst round id: `round_220`
- 대섹터: `CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS`
- 생산 점수 변경: 없음
- candidate generation 입력 사용: 없음
- 적용 방식: `shadow_weight_only`

이번 라운드는 건설·부동산·건자재를 “수주가 많다”로만 보지 않도록 만든 가격경로 검증팩이다. 예를 들어 `6B USD 해외 EPC 수주`는 강한 Stage 2 이벤트지만, 선급금, 원가 lock-in, 운전자본, claim risk, 완공마진이 확인되기 전에는 Stage 3-Green이 아니다.

## 추가된 Canonical Archetype

- `PF_LIQUIDITY_HARD_4C_WATCH`
- `REAL_ESTATE_POLICY_STAGE2_NOT_GREEN`
- `CONSTRUCTION_SAFETY_HARD_4C`
- `OVERSEAS_EPC_ORDER_4B_WATCH`
- `NUCLEAR_CONSTRUCTION_EXPORT_STAGE2`
- `BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING`
- `BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM`
- `US_LOCALIZATION_CAPEX_FALSE_POSITIVE`

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| Taeyoung E&C / PF liquidity | hard 4C-watch | 40.6T KRW 지원, PF 연체율 2.70%, 1T~5T syndicated loan. 수주잔고가 있어도 PF 상환과 차환이 막히면 Green 불가 |
| Seoul property policy | policy Stage 2 + 4B-watch | LTV 50%에서 40%, 거래허가구역, LH 토지 공급은 정책 Stage 2. 실제 인허가, 착공, 분양률, PF cashflow 필요 |
| HDC Hyundai Development / Gwangju collapse | hard 4C reference | 6명 사망, 부실시공·자재, 구조 변경, 회장 사임. 건설 safety/quality trust가 backlog보다 우선 |
| Samsung E&A / Fadhili EPC | success candidate + event premium | $6B 수주와 +8.5% 이벤트. Green은 선급금, 원가, 미청구공사, 완공마진 확인 필요 |
| Czech nuclear construction export | success candidate + legal watch | KHNP preferred bidder와 관련주 3개월 급등. 최종계약과 EDF 법적 리스크가 남아 Stage 2 |
| Hyundai Steel weak construction demand | failed rerating | 철근 가격 -10% 예상, 순이익 추정치 -73%, 목표가 -14%. 건설경기 둔화가 건자재 P&L로 내려옴 |
| Hyundai Steel / POSCO anti-dumping | event premium | 관세 27.91%~38.02%, 현대제철 +5.8%, POSCO +3.9%. ASP·물량·spread 전에는 Green 아님 |
| Hyundai Steel U.S. plant | false positive | $6B 미국공장 발표 후 주가 -21% 이상. 현지화 CAPEX는 IRR, funding clarity, tariff saving 확인 필요 |

## Green Gate 보정 방향

올릴 축:

- PF repayment visibility
- pre-sale absorption
- construction cost margin
- unbilled receivables control
- safety / quality trust
- completion-margin visibility
- working capital / advance payment
- final contract signing
- building-material ASP / volume
- capex IRR / funding clarity

내릴 축:

- order value headline only
- policy support headline only
- property supply policy only
- preferred bidder without final contract
- tariff relief without ASP/margin
- localization capex without IRR
- housing price rally without presales
- backlog without PF cashflow
- unresolved safety risk

## 4B / 4C 해석

- `4B-watch`: 해외 EPC 수주 당일 급등, 원전 preferred bidder basket 급등, 건자재 관세 relief, 부동산 공급정책, 현지화 CAPEX처럼 가격이 증거보다 먼저 갈 수 있는 상태.
- `hard 4C`: PF workout/debt rescheduling, 사망 건설 안전사고, 대규모 하자·재시공·보상, 계약 법적 차단, funding gap처럼 thesis가 손상되는 상태.

## 생성 산출물

- `data/e2r_case_library/cases_r10_loop14_round292.jsonl`
- `data/sector_taxonomy/round292_r10_loop14_construction_real_estate_building_materials_price_validation_audit.json`
- `output/e2r_round292_r10_loop14_construction_real_estate_building_materials_price_validation/round292_r10_loop14_price_validation_summary.md`
- `output/e2r_round292_r10_loop14_construction_real_estate_building_materials_price_validation/round292_r10_loop14_case_matrix.csv`
- `output/e2r_round292_r10_loop14_construction_real_estate_building_materials_price_validation/round292_r10_loop14_shadow_weights.csv`
- `output/e2r_round292_r10_loop14_construction_real_estate_building_materials_price_validation/round292_r10_loop14_green_gate_review.md`
- `output/e2r_round292_r10_loop14_construction_real_estate_building_materials_price_validation/round292_r10_loop14_stage4b_4c_review.md`

## 검증

```bash
PYTHONPATH=src python -m unittest tests/test_round292_r10_loop14_construction_real_estate_building_materials_price_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round292_r10_loop14_report
```

결과:

- round_292 단위 테스트 통과
- case library 레코드 validation 통과
- 리포트 생성 완료
- production scoring 변경 없음

## 다음 라운드에 남긴 기준

R10의 핵심은 “수주·정책·관세·CAPEX 뉴스가 좋다”가 아니라 “PF 상환, 분양률, 원가율, 미청구공사, safety trust, advance payment, completion margin, ASP/volume, capex IRR이 실제 숫자로 닫히는가”다. 쉽게 말해 건설은 계약서만 보는 업종이 아니라, 돈이 회수되는 순서까지 봐야 하는 업종이다.
