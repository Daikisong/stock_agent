# Checkpoint 28A Round 304 R9 Loop 15 Mobility/Transport/Leisure Trigger Validation

## Scope

`docs/round/round_304.md` 내용을 calibration/evaluation 전용 케이스 팩으로 반영했다.

쉬운 예: 현대차 하이브리드 목표와 자사주 매입은 Stage2 신호가 될 수 있지만, 실제 하이브리드 믹스와 마진, 관세 흡수, 자사주 실행이 확인되기 전에는 Stage3-Green으로 쓰면 안 된다.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round304_r9_loop15_mobility_transport_leisure_trigger_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/archetypes.py src/e2r/sector/round304_r9_loop15_mobility_transport_leisure_trigger_validation.py src/e2r/cli/build_round304_r9_loop15_report.py tests/test_round304_r9_loop15_mobility_transport_leisure_trigger_validation.py
PYTHONPATH=src python -m e2r.cli.build_round304_r9_loop15_report
```

## Outputs

- `data/e2r_case_library/cases_r9_loop15_round232.jsonl`
- `data/e2r_trigger_calibration/triggers_r9_loop15_round232.jsonl`
- `data/sector_taxonomy/round304_r9_loop15_mobility_transport_leisure_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round232_r9_loop15_v1.csv`
- `output/e2r_round304_r9_loop15_mobility_transport_leisure_trigger_validation/`

## Summary

- case candidates: 8
- trigger records: 10
- Stage2-Actionable candidates: 5
- Stage3-Yellow candidate: 1
- Stage3-Green confirmed: 0
- Stage4B-watch: 4
- Stage4C-watch: 4
- hard 4C: 1
- production scoring changed: false
- candidate generation input: false
- shadow weight only: true

## Added Canonical Archetypes

- `HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW`
- `ROBOTICS_OPTIONALITY_STAGE2_WITH_4B`
- `AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C`
- `AIRLINE_SAFETY_HARD_4C`
- `TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE`
- `CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B`

Existing archetypes reused:

- `AUTO_TARIFF_MARGIN_4C_WATCH`
- `AIRLINE_CONSOLIDATION_STAGE2`

## Core Findings

- Hyundai hybrid/shareholder-return is Stage2-Actionable and Stage3-Yellow candidate, but Green requires actual hybrid mix, ASP/margin, tariff absorption, and buyback execution.
- Kia is EV-target softening plus tariff 4C-watch; unit sales cannot offset OP deterioration without margin proof.
- Hyundai/Boston Dynamics robotics is Stage2-Actionable with 4B overlay; demo, capex, and factory plan need orders and unit economics.
- Hyundai Georgia localization is operational 4C-watch; localization capex must clear workforce, visa, safety, and compliance gates.
- Korean Air/Asiana is Stage2 consolidation; merger closing is not synergy proof.
- Jeju Air fatal accident is hard 4C and blocks travel-demand Green logic.
- China tourism visa waiver is Stage2-Actionable; actual arrivals, spending, ADR, duty-free/casino sales, and airline yield remain gates.
- HMM Red Sea freight is cyclical Stage2 plus 4B-watch; spot freight spike is not structural Green without contract mix and duration.

## What Not To Change

- Do not apply Round 304 shadow weights to production scoring yet.
- Do not use Round 304 case records as candidate-generation input.
- Do not treat mobility/transport/leisure headline events as Stage3-Green.
- Do not invent MFE/MAE or adjusted OHLC where full price history is unavailable.

## Next Step

Backfill adjusted OHLC and source snapshots for the Round 304 triggers, then run the same cases through shadow scoring only. Production Stage gates should remain unchanged until multiple mobility/transport/leisure rounds agree on the same evidence pattern.
