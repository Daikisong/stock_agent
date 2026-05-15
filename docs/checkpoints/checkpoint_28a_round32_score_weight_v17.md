# Checkpoint 28A Round 32: Score-Weight v1.7 Calibration

## Scope

Round 32 반영은 production scoring 변경이 아니라 calibration/evaluation 자료 확장이다.

추가 범위:

- `GENERAL_TRADING_RESOURCE_INFRA`
- `LNG_ENERGY_TRADING_DISTRIBUTION`
- `DISPLAY_OLED_SUPPLYCHAIN`
- `ELECTRONIC_COMPONENTS_MLCC_SENSOR`
- `DIGITAL_HEALTHCARE_REMOTE_MEDICINE`
- `COMMODITY_MEMORY_GENERAL_SEMI`
- `ENERGY_UTILITY_LNG_GAS`
- `AI_CHIP_FABRIC_INFRA`

## Outputs

- `src/e2r/sector/round32_score_weight_v17.py`
- `src/e2r/cli/build_round32_score_weight_report.py`
- `tests/test_round32_score_weight_v17.py`
- `data/e2r_case_library/cases_v14_round32.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round32_v17.csv`
- `output/e2r_round32_score_weight_v17/`

## Summary

- target_count: 8
- case_candidate_count: 32
- success_candidate_count: 15
- stage4c_case_count: 7
- green_possible_count: 5
- watch_yellow_first_count: 2
- redteam_first_count: 1
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Key Calibration Notes

- 종합상사는 단순 매출 규모가 아니라 장기 offtake, 프로젝트 지분, FCF, 자본배분이 같이 있어야 한다.
- LNG/에너지 유통은 장기계약과 pass-through가 있으면 Watch-to-Green 가능하지만, 정제마진/재고손익은 cycle로 제한한다.
- OLED와 MLCC/센서 부품은 Green 가능성이 있지만 CAPEX cycle, 패널 가격경쟁, 고객집중, 재고 cycle을 강하게 본다.
- 원격의료는 병원/보험/기업 고객 계약, 수가, 반복매출, unit economics 없이는 Green으로 보지 않는다.
- 범용 DRAM/NAND는 EPS 회복 점수는 줄 수 있지만, HBM처럼 장기 allocation이나 capacity bottleneck이 없으면 visibility를 낮춘다.
- AI칩 관련주는 실제 고객 계약, 양산 매출, 수율, 고객 검증 전까지 RedTeam-first다.

## Guardrails

- 케이스 ID와 종목명은 candidate-generation input이 아니다.
- 점수비중 v1.7은 production scoring에 적용하지 않았다.
- stage date, 가격, 계약금액, LNG 물량, 요금결과, OLED margin, MLCC 재고, 원격의료 수가, HBM 승인, 파운드리 수율은 추정해서 채우지 않았다.
- Stage 3-Green 기준은 낮추지 않았다.

## Verification

```bash
PYTHONPATH=src python -m unittest tests.test_round32_score_weight_v17 -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m e2r.cli.build_round32_score_weight_report
```

Round 32 전용 테스트는 통과했다.
