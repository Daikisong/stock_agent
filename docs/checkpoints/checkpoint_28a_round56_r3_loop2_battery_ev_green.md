# Checkpoint 28A Round56 R3 Loop-2 Battery / EV / Green-Energy

## Scope

Round56 반영 범위는 `docs/round/round_56.md`의 R3 Loop 2 보강이다.

핵심 변경은 `EV 성장`과 `반복 FCF 구조`를 분리한 것이다.

예:

- EV 배터리 CAPA 증설은 고객 수요, 가동률, OPM, FCF가 없으면 Green 근거가 아니다.
- ESS 전환은 계약금액, 계약기간, 고객, 가동률, ESS margin이 확인될 때 Stage 2 이상 후보가 된다.
- 폐기물처리는 허가권, 처리량, 장기계약, 반복 FCF가 있으면 R3에서 드물게 Green 가능성이 있다.
- 태양광/풍력은 보조금이나 정책만으로 Green이 아니며, 통관·관세·UFLPA·금리·원가·impairment가 hard 4C가 될 수 있다.
- EV 화재·배터리 인증·리콜·보험비용은 별도 RedTeam overlay다.

## Added

- `src/e2r/sector/round56_r3_loop2_battery_ev_green.py`
- `src/e2r/cli/build_round56_r3_loop2_report.py`
- `tests/test_round56_r3_loop2_battery_ev_green.py`

## Canonical Archetype Updates

Round56에서 canonical enum으로 추가한 R3 Loop-2 archetype:

- `BATTERY_EQUIPMENT_PARTS`
- `BATTERY_RECYCLING_ESS_SHIFT`
- `EV_INFRASTRUCTURE`
- `HYDROGEN_FUEL_CELL_INFRA`
- `SOLAR_TARIFF_SUPPLYCHAIN`
- `RENEWABLE_ENERGY_POLICY`
- `ENERGY_DISTRIBUTION_FUEL`
- `WASTE_RECYCLING_ENVIRONMENT`
- `CARBON_CREDIT_CBAM_COMPLIANCE`
- `DATA_CENTER_WATER_REUSE_INFRA`
- `EV_FIRE_RISK_OVERLAY`

## Case Pack

Generated calibration cases:

- `data/e2r_case_library/cases_r3_loop2_round56.jsonl`

Case count:

- total: 13
- structural_success: 1
- success_candidate: 5
- cyclical_success: 1
- 4B-watch marker cases: 2
- 4C thesis-break cases: 6

Important cases:

- `lg_energy_solution_ess_shift_case`
- `lg_energy_tesla_lfp_ess_contract_case`
- `sk_on_flatiron_ess_7_2gwh_case`
- `redwood_recycling_energy_storage_case`
- `hyundai_hydrogen_fuel_cell_plant_case`
- `eqt_kj_environment_waste_platform_case`
- `gm_lg_ultium_ohio_idle_case`
- `ford_lges_ev_contract_cancel_case`
- `qcells_customs_detention_furlough_case`
- `orsted_sunrise_wind_impairment_case`
- `lithium_price_86pct_crash_case`
- `albemarle_cost_cut_low_lithium_case`
- `korea_ev_battery_certification_fire_case`

## Outputs

Generated files:

- `data/sector_taxonomy/score_weight_profiles_round56_r3_loop2_v2.csv`
- `output/e2r_round56_r3_loop2_battery_ev_green/round56_r3_loop2_battery_ev_green_summary.md`
- `output/e2r_round56_r3_loop2_battery_ev_green/round56_r3_loop2_case_matrix.csv`
- `output/e2r_round56_r3_loop2_battery_ev_green/round56_r3_loop2_stage_date_plan.csv`
- `output/e2r_round56_r3_loop2_battery_ev_green/round56_r3_loop2_green_guardrails.md`
- `output/e2r_round56_r3_loop2_battery_ev_green/round56_r3_loop2_risk_overlays.md`
- `output/e2r_round56_r3_loop2_battery_ev_green/round56_r3_loop2_price_validation_plan.md`
- `output/e2r_round56_r3_loop2_battery_ev_green/round56_r3_loop2_price_fields.csv`

## Guardrails

- Production scoring was not changed.
- Case records are calibration/evaluation material only.
- Case records are not candidate-generation input.
- Stage 3-Green thresholds were not loosened.
- Missing prices and stage prices remain null until backfilled from official price history.
- No contract value, margin, utilization, recovery volume, stage price, or FCF is invented.

Simple example:

`ESS 전환`이라는 뉴스는 좋은 Stage 1~2 재료일 수 있다. 하지만 “라인을 ESS로 바꿀 수 있다”만 있고 계약금액, 계약기간, 고객, 가동률, margin이 없으면 Stage 3-Green 근거로 쓰면 안 된다.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m compileall -q src/e2r/sector/round56_r3_loop2_battery_ev_green.py src/e2r/cli/build_round56_r3_loop2_report.py tests/test_round56_r3_loop2_battery_ev_green.py
PYTHONPATH=src python -m unittest tests.test_round56_r3_loop2_battery_ev_green -v
PYTHONPATH=src python -m e2r.cli.build_round56_r3_loop2_report
```

Round56 targeted tests:

- 13 tests passed.

Full verification after report generation:

```bash
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

Full repository test result is recorded in the final commit/report for this round.

Result:

- 863 tests passed.
