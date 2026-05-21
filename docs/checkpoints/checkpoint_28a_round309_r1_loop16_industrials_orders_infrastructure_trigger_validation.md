# Checkpoint 28A Round 309 R1 Loop 16 산업재·수주·인프라 Trigger Validation

## 목적

`docs/round/round_309.md`의 R1 Loop 16 내용을 calibration/evaluation 자료로 반영했다. 이번 라운드는 산업재·수주·인프라에서 수주, 합병, 전력기기 shortage, 로봇 전략지분, 데이터센터 cooling M&A가 실제 Stage 승격에 어떤 의미를 갖는지 trigger 단위로 분리한다.

쉬운 예시:

- Samsung E&A의 Fadhili 수주는 계약금액과 주가 반응이 강하므로 Stage2-Actionable 후보가 될 수 있다.
- 하지만 EPC 마진, 현금회수, 원가초과 위험이 닫히기 전에는 Stage3-Green으로 올리지 않는다.

## 반영 파일

- `src/e2r/sector/round309_r1_loop16_industrials_orders_infrastructure_trigger_validation.py`
- `src/e2r/cli/build_round309_r1_loop16_report.py`
- `tests/test_round309_r1_loop16_industrials_orders_infrastructure_trigger_validation.py`
- `data/e2r_case_library/cases_r1_loop16_round237.jsonl`
- `data/e2r_trigger_calibration/triggers_r1_loop16_round237.jsonl`
- `data/sector_taxonomy/round309_r1_loop16_industrials_orders_infrastructure_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round237_r1_loop16_v1.csv`
- `output/e2r_round309_r1_loop16_industrials_orders_infrastructure_trigger_validation/`

## Canonical Archetype 추가

- `OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE`
- `GRID_TRANSFORMER_DATA_CENTER_STAGE2`
- `SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B`
- `SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE`
- `SHIPBUILDING_ORDER_CANCELLATION_4C`
- `GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH`
- `ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE`
- `DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED`
- `AEROSPACE_EXPORT_CONTRACT_STAGE2`

## 케이스 요약

| case | 판정 |
| --- | --- |
| Samsung E&A / Fadhili | Stage2-Actionable / Stage3-Yellow 후보. Green은 마진·현금회수 확인 전 금지 |
| LS Electric / U.S. transformer | 구조적 Stage2 event. 회사별 수주잔고·CAPA·마진 필요 |
| HD Hyundai Heavy / Mipo merger | Stage2-Actionable + integration 4B-watch |
| Korean shipbuilding contract-win basket | Stage2-Actionable basket. delivery margin과 steel cost가 Green gate |
| Samsung Heavy / Zvezda cancellation | order-cancellation 4C-watch |
| Hanwha Ocean / China sanctions | geopolitical 4C-watch |
| Rainbow Robotics / Samsung | Stage2 strategic control. 외부 주문·공장 deployment 전에는 Yellow 금지 |
| Samsung / FlaktGroup | data-center cooling Stage2지만 price-muted. 고객 주문과 통합 마진 필요 |

## Trigger 결과

- case_candidate_count: `8`
- trigger_count: `8`
- target_archetype_count: `9`
- stage2_actionable_candidate_count: `3`
- stage2_event_candidate_count: `3`
- stage3_yellow_candidate_count: `4`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `4`
- stage4c_watch_count: `2`
- hard_4c_case_count: `0`

## 핵심 보정 방향

올릴 축:

- `signed_contract_value_vs_backlog`
- `market_relative_event_strength`
- `grid_transformer_backlog_capacity`
- `shipbuilding_newbuilding_price_backlog`
- `merger_integration_synergy`
- `robotics_order_revenue_bridge`
- `geopolitical_sanction_overlay`
- `data_center_cooling_order_conversion`

내릴 축:

- `headline_order_without_margin`
- `transformer_demand_without_company_margin`
- `shipbuilding_order_without_delivery_margin`
- `merger_announcement_without_integration`
- `strategic_stake_without_orders`
- `MA_without_customer_orders`
- `geopolitical_opportunity_without_sanction_check`

## Guardrail

- production scoring 변경 없음
- candidate generation input 아님
- shadow weight only
- full adjusted OHLC 미확보
- OHLC 미확보만으로 Stage2/Yellow 후보를 강등하지 않음
- 대형수주, 합병, 전력기기 shortage, 로봇 전략지분, cooling M&A headline만으로 Stage3-Green 금지

## 검증

실행한 핵심 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round309_r1_loop16_industrials_orders_infrastructure_trigger_validation -v
PYTHONPATH=src python -m e2r.cli.build_round309_r1_loop16_report
```

전용 테스트는 통과했다. 전체 테스트는 최종 커밋 전 다시 실행한다.
