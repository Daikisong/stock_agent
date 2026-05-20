# Checkpoint 28A Round 257 R1 Loop 12 Industrial Orders / Infrastructure Price Validation

## 반영 내용

- `docs/round/round_257.md`의 R1 Loop 12 내용을 calibration-only 데이터로 반영했다.
- 대섹터는 `INDUSTRIAL_ORDERS_INFRA`, analyst round id는 `round_185`로 기록했다.
- 신규 canonical archetype 정의를 추가했다.
  - `DEFENSE_EXPORT_BACKLOG_COMPOUNDING`
  - `MISSILE_DEFENSE_COMBAT_VALIDATION`
  - `ARMORED_VEHICLE_DELIVERY_TO_REVENUE`
  - `GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK`
  - `US_GRID_EQUIPMENT_LOCALIZATION`
  - `DILUTION_AFTER_RERATING_4B`
- 기존 archetype `OVERSEAS_EPC_MEGA_ORDER`, `POLICY_CAPEX_FALSE_POSITIVE`와 함께 총 8개 target archetype을 이번 라운드에 매핑했다.
- production scoring과 candidate generation은 변경하지 않았다.

## 생성 파일

- `src/e2r/sector/round257_r1_loop12_industrial_orders_infra_price_validation.py`
- `src/e2r/cli/build_round257_r1_loop12_report.py`
- `tests/test_round257_r1_loop12_industrial_orders_infra_price_validation.py`
- `data/e2r_case_library/cases_r1_loop12_round257.jsonl`
- `data/sector_taxonomy/round257_r1_loop12_industrial_orders_infra_price_validation_audit.json`
- `output/e2r_round257_r1_loop12_industrial_orders_infra_price_validation/round257_r1_loop12_price_validation_summary.md`
- `output/e2r_round257_r1_loop12_industrial_orders_infra_price_validation/round257_r1_loop12_case_matrix.csv`
- `output/e2r_round257_r1_loop12_industrial_orders_infra_price_validation/round257_r1_loop12_shadow_weights.csv`
- `output/e2r_round257_r1_loop12_industrial_orders_infra_price_validation/round257_r1_loop12_green_gate_review.md`
- `output/e2r_round257_r1_loop12_industrial_orders_infra_price_validation/round257_r1_loop12_stage4b_4c_review.md`

## 케이스 요약

| case | 분류 | 판정 |
|---|---|---|
| Hanwha Aerospace Romania K9 | success_candidate + 4B-watch | 1.38조원 / $1B 수주와 backlog compounding은 강하지만, 납품·마진·현금회수 전 Green 보류. 이후 대형 증자 리스크를 4B-watch로 기록. |
| LIG Nex1 Iraq Cheongung-II | success_candidate + geopolitical 4B-watch | Iraq $2.8B 수주는 Stage 2. 지정학 rally가 납품·마진보다 앞서면 4B-watch. |
| Hyundai Rotem Poland K2 | success_candidate | 18대 K2 출하와 2,700억원 매출 기여 anchor가 있어 좋은 Stage 2. 현지생산 경제성·현금회수 전 Green 보류. |
| LS Electric U.S. transformer | success_candidate / insufficient price | $312M 변압기 계약과 U.S. GSU 수요 +274%는 강한 Stage 2. full OHLC는 미확보. |
| Hyosung HICO | success_candidate / capex watch | $157M U.S. 현지화 투자는 Stage 2. firm order·가동률·마진·FCF 전 Green 금지. |
| Samsung E&A Fadhili | event_premium | $6B EPC 수주와 +8.5% rally는 Stage 2 / 4B-watch. 공정률·마진·운전자본 확인 필요. |
| Hyundai Steel U.S. plant | failed_rerating | 정책 CAPEX false positive. 발표 초기 +5%가 -4.4%로 뒤집히고 이후 -21.2% drawdown. |
| Hanwha Aerospace capital raise | 4B-watch | 3.6조원 증자 계획과 -13% 충격을 dilution after rerating 4B-watch로 기록. |

## 핵심 결론

이번 라운드의 핵심은 `수주 headline = Stage 3`가 아니라는 점이다. 예를 들어 방산 수주가 있어도 실제 Stage 3 근거가 되려면 납품, 매출 인식, 마진, 현금회수, 반복 수주까지 이어져야 한다.

`Hyundai Steel`처럼 미국 공장 투자 발표는 좋아 보일 수 있지만, 자금조달·고객수요·마진·FCF가 불명확하면 false positive로 처리한다. 반대로 `Hyundai Rotem`처럼 납품이 실제 매출로 내려오는 증거는 단순 수주보다 높은 Stage 2 품질로 본다.

## Shadow Weight 보정

올릴 축:
- `confirmed_order +5`
- `delivery_to_revenue +5`
- `backlog_compounding +5`
- `local_production_economics +4`
- `MRO_or_aftermarket_revenue +4`
- `production_capacity_visibility +4`
- `cash_collection_quality +5`
- `working_capital_control +5`
- `repeat_export_customer +4`
- `price_path_alignment +5`

내릴 축:
- `contract_headline_only -5`
- `policy_capex_without_funding -5`
- `local_production_without_margin -4`
- `defense_rally_without_delivery -4`
- `EPC_order_without_working_capital -5`
- `capacity_expansion_without_order -4`
- `dilution_after_rerating -5`
- `unconfirmed_geopolitical_replenishment -4`
- `input_cost_unknown -3`

## Green Gate

R1 Stage 3-Green 필수 조건:
- confirmed order
- delivery schedule 확인
- delivery-to-revenue 또는 progress revenue 확인
- OPM / gross margin 확인
- working capital / receivables / cash collection 안정
- local-production economics 확인
- capex/dilution risk 통과
- repeat customer / aftermarket / MRO revenue 확인
- 가격경로가 evidence 이후 따라옴

금지 조건:
- 수주 headline만 있음
- 정책 CAPEX만 있음
- 공장투자만 있음
- 현지생산 margin 불명
- 증자 shock 존재
- 운전자본 악화
- geopolitical headline만 있음

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round257_r1_loop12_industrial_orders_infra_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round257_r1_loop12_report
```

결과:
- round257 전용 테스트 8개 통과
- case JSONL, audit JSON, summary/CSV/Markdown 리포트 생성 완료

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation input으로 사용하지 않음
- StageClassifier threshold 변경 없음
- full OHLC가 없는 항목의 MFE/MAE를 발명하지 않음
- hard 4C를 억지로 확정하지 않음

