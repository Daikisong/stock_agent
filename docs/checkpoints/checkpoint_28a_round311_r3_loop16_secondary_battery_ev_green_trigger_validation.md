# Checkpoint 28A Round 311 R3 Loop 16 2차전지·전기차·친환경 Trigger Validation

## 목적

`docs/round/round_311.md`의 R3 Loop 16 내용을 calibration/evaluation 자료로 반영했다. 이번 라운드는 EV battery, ESS/LFP 전환, OEM 계약취소, JV 재무구조, 리튬 beta, 유상증자 희석, 배터리 안전사고를 하나로 묶지 않고 trigger 단위로 분리한다.

쉬운 예시:

- Samsung SDI의 U.S. LFP ESS 계약은 계약금액, 납품기간, U.S. line conversion, 가격반응이 있어 Stage2-Actionable이다.
- 하지만 ESS margin, line-retrofit yield, repeat order, utilization이 확인되기 전에는 Stage3-Green으로 올리지 않는다.
- LGES Ford 계약취소나 Aricell 화재는 같은 배터리 섹터라도 positive trigger가 아니라 4C-watch 또는 hard 4C다.

## 반영 파일

- `src/e2r/sector/round311_r3_loop16_secondary_battery_ev_green_trigger_validation.py`
- `src/e2r/cli/build_round311_r3_loop16_report.py`
- `tests/test_round311_r3_loop16_secondary_battery_ev_green_trigger_validation.py`
- `data/e2r_case_library/cases_r3_loop16_round239.jsonl`
- `data/e2r_trigger_calibration/triggers_r3_loop16_round239.jsonl`
- `data/sector_taxonomy/round311_r3_loop16_secondary_battery_ev_green_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round239_r3_loop16_v1.csv`
- `output/e2r_round311_r3_loop16_secondary_battery_ev_green_trigger_validation/`

## Canonical Archetype 추가

- `ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE`
- `EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE`
- `EV_DEMAND_SLOWDOWN_4C_WATCH`
- `BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B`
- `LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2`
- `BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM`
- `BATTERY_FACTORY_SAFETY_HARD_4C`
- `CAPITAL_RAISE_DILUTION_4B`

## 케이스 요약

| case | 판정 |
| --- | --- |
| Samsung SDI / U.S. LFP ESS | Stage2-Actionable. Green은 ESS margin, retrofit yield, repeat order 확인 전 보류 |
| LGES / Rivian·Tesla LFP | Stage2 supply contract. Utilization/margin gate와 price-muted overlay |
| LGES / Ford cancellation·Ohio loss | OEM cancellation, operating loss, plant idling 4C-watch |
| SK Innovation / SK E&S merger | Stage2 financial relief + 4B. SK On profit turnaround는 아직 아님 |
| SK Battery America layoffs | customer demand/utilization 4C-watch |
| CATL Yichun lithium beta | cyclical Stage2 / event premium. Cathode ASP/margin 확인 전 Green 금지 |
| Samsung SDI share-sale dilution | capex funding + dilution 4B-watch |
| Aricell / S-Connect fire | battery safety hard 4C |

## Trigger 결과

- case_candidate_count: `8`
- trigger_count: `9`
- target_archetype_count: `8`
- stage2_actionable_candidate_count: `1`
- stage2_event_candidate_count: `3`
- stage3_yellow_candidate_count: `0`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `4`
- stage4c_watch_count: `3`
- hard_4c_case_count: `1`

## 핵심 보정 방향

올릴 축:

- `ESS_LFP_contract_visibility`
- `US_line_conversion_utilization`
- `OEM_contract_cancellation_risk`
- `IRA_tax_credit_dependency`
- `battery_JV_financial_structure`
- `lithium_price_beta_duration`
- `battery_factory_safety_trust`

내릴 축:

- `EV_growth_headline_without_utilization`
- `large_GWh_contract_without_margin`
- `ESS_pivot_without_line_yield`
- `lithium_price_spike_without_margin`
- `restructuring_relief_without_profit`
- `capex_funding_with_dilution`

## Guardrail

- production scoring 변경 없음
- candidate generation input 아님
- shadow weight only
- full adjusted OHLC 미확보
- OHLC 미확보만으로 Stage2/Yellow 후보를 강등하지 않음
- GWh 계약, capex funding, restructuring relief, lithium beta headline만으로 Stage3-Green 금지
- battery fire, death, quality failure는 hard 4C safety gate로 분리

## 검증

실행한 핵심 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round311_r3_loop16_secondary_battery_ev_green_trigger_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round311_r3_loop16_report
```

전용 테스트와 리포트 생성은 통과했다. 전체 테스트는 최종 커밋 전 다시 실행한다.
