# Checkpoint 28A Round 259 R3 Loop 12 Battery EV Green Price Validation

## 반영 범위

`docs/round/round_259.md`의 R3 Loop 12 가격검증 내용을 calibration-only 데이터로 반영했다.

생산 점수, 후보 생성, StageClassifier threshold는 바꾸지 않았다.

## 추가 파일

- `src/e2r/sector/round259_r3_loop12_battery_ev_green_price_validation.py`
- `src/e2r/cli/build_round259_r3_loop12_report.py`
- `tests/test_round259_r3_loop12_battery_ev_green_price_validation.py`
- `data/e2r_case_library/cases_r3_loop12_round259.jsonl`
- `data/sector_taxonomy/round259_r3_loop12_battery_ev_green_price_validation_audit.json`
- `output/e2r_round259_r3_loop12_battery_ev_green_price_validation/`

## Archetype 반영

신규 또는 명시 보강한 canonical archetype:

- `US_BATTERY_LOCALIZATION_DILUTION`
- `EV_BATTERY_JV_RESTRUCTURING`
- `SILICON_ANODE_OPTIONALITY`
- `HYDROGEN_FUELCELL_CAPEX_OPTIONALITY`
- `US_FACTORY_EXECUTION_VISA_RISK`

기존 R3 archetype도 Round 259 기준으로 함께 사용했다:

- `EV_BATTERY_CONTRACT_QUALITY_BREAK`
- `EV_TO_ESS_CAPACITY_REDEPLOYMENT`
- `BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK`
- `SOLAR_US_SUPPLY_CHAIN_LOCALIZATION`
- `SOLAR_CUSTOMS_UFLPA_4C_WATCH`

쉬운 예시:

- LGES의 Ford/Freudenberg 계약 취소는 기대매출이 실제로 사라진 hard 4C다.
- SK On의 Flatiron ESS 7.2GWh는 좋은 Stage 2 단서지만, 계약금액·가동률·OPM·FCF가 확인되기 전에는 Green이 아니다.
- Qcells의 DOE loan guarantee와 미국 현지화는 Stage 2 단서지만, UFLPA/customs로 component flow가 막히면 4C-watch다.

## 케이스 요약

- 케이스 수: 8
- `success_candidate`: 4
- `failed_rerating`: 3
- `4c_thesis_break`: 1
- hard 4C: 1
- Stage 3 dated case: 0
- 4C-watch 또는 hard 4C: 6

주요 케이스:

- Samsung SDI / StarPlus: 미국 현지화 CAPEX와 JV는 dilution과 customer-exit risk가 있으면 Green이 아니라 failed rerating / 4C-watch.
- LGES / Ford·Freudenberg·Ultium: 기대매출 13.5조 원 손실, 2024 매출 대비 52.7%, 이벤트 -7.6%. 이번 라운드의 확정 hard 4C.
- SK On / Ford JV + ESS: $11.4B JV split은 EV thesis damage, Flatiron 7.2GWh ESS는 Stage 2 pivot.
- POSCO Future M / SK IE Tech / EcoPro Materials: Ford EV retreat이 소재·분리막·전구체로 전이된 supply-chain demand shock.
- SK / Group14: silicon-anode optionality Stage 2. offtake, utilization, margin, 지분가치 확인 필요.
- Hanwha Qcells: solar localization Stage 2 plus customs/UFLPA 4C-watch.
- Hyundai hydrogen fuel-cell plant: 930B won capex Stage 2. offtake, utilization, hydrogen economics 확인 필요.
- Hyundai-LG Georgia: visa/skilled-worker execution 4C-watch. 정확한 일자를 만들지 않고 `stage4c_month=2025-09` 메타데이터로 보존했다.

## Green Gate

Round 259 R3 Stage 3-Green 필수 조건:

- actual call-off 또는 take-or-pay 확인
- GWh volume과 supply period 확인
- delivery 또는 revenue recognition 시작
- utilization improvement
- OPM 또는 gross margin 확인
- FCF after capex
- subsidy 제외 unit economics
- customs / visa / labor / supply-chain flow risk 통과
- price path follows evidence

금지 패턴:

- EV JV headline only
- U.S. localization capex only
- ESS pivot only
- hydrogen plant only
- silicon-anode optionality only
- solar loan guarantee only
- demand quality 없는 share issuance for capex
- contract cancellation 존재
- customs detention 존재
- factory startup delay 존재

## Shadow Weight 보정

올릴 축:

- `actual_calloff +5`
- `take_or_pay_quality +5`
- `GWh_volume +5`
- `delivery_schedule +5`
- `utilization_visibility +5`
- `ESS_revenue_conversion +5`
- `line_redeployment_execution +4`
- `OPM_visibility +5`
- `FCF_after_capex +5`
- `supply_chain_flow_reliability +5`
- `factory_execution_readiness +5`

내릴 축:

- `EV_JV_headline_only -5`
- `U.S._localization_capex_only -5`
- `share_issuance_for_capex -5`
- `customer_exit_report -5`
- `ESS_pivot_without_contract_value -4`
- `silicon_anode_optionality_only -4`
- `hydrogen_capex_without_offtake -5`
- `solar_loan_guarantee_without_component_flow -5`
- `factory_startup_visa_risk -5`
- `EV_demand_shock -5`

## 산출물

- `round259_r3_loop12_price_validation_summary.md`
- `round259_r3_loop12_case_matrix.csv`
- `round259_r3_loop12_target_aliases.csv`
- `round259_r3_loop12_score_adjustments.csv`
- `round259_r3_loop12_shadow_weights.csv`
- `round259_r3_loop12_deep_sub_archetypes.csv`
- `round259_r3_loop12_price_validation_fields.csv`
- `round259_r3_loop12_green_gate_review.md`
- `round259_r3_loop12_price_validation_plan.md`
- `round259_r3_loop12_stage4b_4c_review.md`

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round259_r3_loop12_battery_ev_green_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round259_r3_loop12_report
```

결과:

- Round 259 신규 테스트 8개 통과.
- case JSONL, audit JSON, summary/CSV/Markdown 리포트 생성 완료.

## 변경하지 않은 것

- production scoring 변경 없음
- candidate generation input으로 사용하지 않음
- StageClassifier threshold 변경 없음
- full OHLC가 없는 항목의 MFE/MAE를 발명하지 않음
- Hyundai-LG Georgia의 month-only 이벤트는 임의 일자로 만들지 않고 메타데이터로 보존
- LGES 계약품질 break 외의 watch case를 hard 4C로 강제 확정하지 않음
