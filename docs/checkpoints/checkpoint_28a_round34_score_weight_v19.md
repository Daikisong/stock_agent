# Checkpoint 28A Round 34: Score-Weight v1.9 Calibration

## Scope

Round 34 반영은 production scoring 변경이 아니라 calibration/evaluation 자료 확장이다.

추가 범위:

- `CARBON_CREDIT_CBAM_COMPLIANCE`
- `PAYMENT_FINTECH_INFRA`
- `OPTICAL_NETWORKING_AI_DATACENTER`
- `TELECOM_5G_6G_CAPEX_CYCLE`
- `LITHIUM_BATTERY_RAW_MATERIAL`
- `HOME_LIVING_APPLIANCE_RENTAL`
- `AI_ACCELERATOR_CHIP_PUREPLAY`
- `MOBILITY_RENTAL_MICROMOBILITY`

## Outputs

- `src/e2r/sector/round34_score_weight_v19.py`
- `src/e2r/cli/build_round34_score_weight_report.py`
- `tests/test_round34_score_weight_v19.py`
- `data/e2r_case_library/cases_v16_round34.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round34_v19.csv`
- `output/e2r_round34_score_weight_v19/`

## Summary

- target_count: 8
- case_candidate_count: 32
- success_candidate_count: 11
- stage4b_case_count: 2
- stage4c_case_count: 8
- green_possible_count: 3
- watch_yellow_first_count: 4
- redteam_first_count: 1
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Key Calibration Notes

- 탄소배출권/CBAM은 정책축이지만 Green은 어렵다. 탄소비용 전가, 탄소회계 반복매출, 저탄소 제품 premium이 확인될 때만 점수를 올린다.
- 결제/PG/e-wallet은 Watch-to-Green 가능하지만, 사용자 수가 아니라 거래액, take rate, lock-in, 부가 금융서비스, FCF가 핵심이다.
- 광섬유/광통신은 AI 데이터센터 병목 하위축으로 Green 가능성이 생겼다. 단, hyperscaler 계약과 실제 납품이 있어야 한다.
- 5G/6G 통신장비는 통신사 CAPEX cycle과 지정학/보안심사 리스크가 커서 RedTeam-first로 분리했다.
- 리튬은 가격 반등만으로 Green 금지다. 저비용 구조, 장기 offtake, FCF 방어력이 있어야 한다.
- 생활가전은 hardware cycle이면 Watch/Red, 렌탈·관리 반복매출이면 Green 가능성으로 본다.
- AI accelerator pure-play는 실제 고객, 매출, 수율, 마진 없이는 Green 금지다.
- 공유 모빌리티/렌터카/중고차는 매출 성장보다 FCF와 unit economics가 핵심이다.

## Guardrails

- 케이스 ID와 종목명은 candidate-generation input이 아니다.
- 점수비중 v1.9는 production scoring에 적용하지 않았다.
- stage date, 가격, CBAM 비용전가, fintech take rate, hyperscaler 계약조건, 통신장비 수주, 리튬 원가, 렌탈 해지율, AI칩 수율, 모빌리티 unit economics는 추정해서 채우지 않았다.
- Stage 3-Green 기준은 낮추지 않았다.

## Verification

```bash
PYTHONPATH=src python -m unittest tests.test_round34_score_weight_v19 -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m e2r.cli.build_round34_score_weight_report
```

Round 34 전용 테스트는 통과했다.
