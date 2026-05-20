# Checkpoint 28A Round 273 R4 Loop 13 Materials Spread Strategic Resources Price Validation

## 반영 요약

`docs/round/round_273.md`의 R4 Loop 13 내용을 케이스 라이브러리용 구조화 자료로 반영했다. 이번 라운드는 소재·스프레드·전략자원에서 `전략광물`, `graphite`, `lithium`, `철강 관세`, `정책 CAPEX`, `석유화학 구조조정`, `방산금속` 같은 단어만으로 Stage 3-Green을 만들면 안 된다는 가격검증 팩이다.

예를 들면 Korea Zinc는 전략광물 후보이지만, 주가를 먼저 움직인 것은 지배권 프리미엄과 희석·거버넌스 이슈였다. 따라서 offtake, margin, FCF, funding quality, dilution control이 닫히기 전에는 operating Green이 아니다.

## 추가한 항목

- 신규 R4 Loop 13 canonical archetype 4개
- 기존 R4 archetype 4개와 연결한 라운드 273 케이스 팩
- 라운드 273 리포트 생성 CLI
- 케이스 JSONL, taxonomy audit JSON, output 리포트 CSV/MD
- 단위 테스트 7개

## 케이스 요약

| case | 판정 |
|---|---|
| Korea Zinc | strategic minerals Stage 2 + governance/dilution 4B-watch |
| POSCO Future M | graphite/lithium policy-price event premium |
| POSCO / Hyundai / SeAH Steel | domestic relief와 export tariff risk가 같이 있는 two-sided case |
| Hyundai Steel U.S. plant | policy CAPEX false positive |
| LG Chem / Hanwha / DL / YNCC | petrochemical credit/spread 4C-watch |
| Lotte / HD Hyundai Chemical | restructuring relief, not Green |
| Lotte Chemical overseas | overseas capex success_candidate지만 spread-gated |
| Poongsan | defense-metals optionality가 있지만 M&A rumor는 event premium |

## 산출물

- `src/e2r/sector/round273_r4_loop13_materials_spread_strategic_price_validation.py`
- `src/e2r/cli/build_round273_r4_loop13_report.py`
- `tests/test_round273_r4_loop13_materials_spread_strategic_price_validation.py`
- `data/e2r_case_library/cases_r4_loop13_round273.jsonl`
- `data/sector_taxonomy/round273_r4_loop13_materials_spread_strategic_price_validation_audit.json`
- `output/e2r_round273_r4_loop13_materials_spread_strategic_price_validation/`

## Green Gate

R4 Stage 3-Green은 다음 증거가 닫혀야 가능하다.

- product spread 개선
- cost curve advantage
- actual offtake / contract / call-off
- capacity utilization
- working capital 안정
- restructuring 이후 FCF
- governance / dilution risk 해소
- export tariff / China restriction 통과
- restructuring이면 shutdown 이후 margin 회복
- 증거 이후 따라온 가격 경로

금지 패턴도 명시했다.

- control premium only
- M&A rumor only
- commodity price event only
- tariff relief only
- policy CAPEX only
- restructuring plan only
- capacity shutdown only

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round273_r4_loop13_materials_spread_strategic_price_validation -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m e2r.cli.build_round273_r4_loop13_report
```

결과:

- 라운드 273 단위 테스트 7개 통과
- compileall 통과
- 리포트 생성 CLI 정상 실행

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation input 변경 없음
- StageClassifier threshold 변경 없음
- case library를 scoring input으로 사용하지 않음
- full OHLC가 없는 항목은 임의 MFE/MAE를 만들지 않음

## 다음 작업

R4는 이제 “정책·관세·구조조정·지배권 프리미엄”과 “실제 spread/FCF 개선”을 더 엄격히 분리한다. 다음 shadow scoring에서는 `product_spread_visibility`, `working_capital_control`, `governance_dilution_control`, `export_control_resilience`, `policy_relief_to_margin_bridge`를 진단 축으로만 먼저 비교해야 한다.
