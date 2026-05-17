# Checkpoint 28A Round 80 - R1 Loop 4 Industrial Orders / Infrastructure

Round 80 반영 완료.

## Scope

- source round: `docs/round/round_80.md`
- large sector: `INDUSTRIAL_ORDERS_INFRA`
- loop: `R1 Loop 4 / v4.0`
- production scoring changed: `false`
- case records are candidate-generation input: `false`

이번 라운드는 R13 공통 RedTeam 이후 다시 R1로 돌아와 산업재, 전력망, 방산, 조선, 철도, 원전, 재건 테마를 더 촘촘히 나눈다.
쉬운 예로, “수주잔고가 크다”는 Stage 1 또는 Stage 2 근거가 될 수 있지만, Stage 3-Green에는 계약금액, 계약기간, 납품 스케줄, 마진, OP/EPS 상향, FCF 전환, 가격경로 검증이 같이 필요하다.

## Targets

- target_count: 16
- green_possible_count: 5
- watch_yellow_first_count: 7
- redteam_first_count: 4
- hard_gate_target_count: 3

새로 분리하거나 강화한 핵심 타깃:

- `GRID_MEDIUM_VOLTAGE_EXPANSION`: 변압기뿐 아니라 중전압, switchgear, substation 장비 확장까지 전력망 병목 후보로 분리.
- `DEFENSE_LOCAL_PRODUCTION_PLATFORM`: 해외 정부 고객과 현지생산 visibility를 보되, 현지 공장 CAPEX와 마진 희석을 같이 본다.
- `DEFENSE_CAPITAL_ALLOCATION_SHOCK`: 좋은 방산 수주라도 대규모 증자와 목적 불명확 CAPEX가 있으면 RedTeam gate로 분리.
- `DEFENSE_UNMANNED_NAVAL_SYSTEMS`: 수중드론, 무인 해군 시스템은 양산계약과 납품 전까지 Watch로 제한.
- `NUCLEAR_EXISTING_PPA_RESTART`: 기존 원전 PPA와 재가동은 SMR 정책 테마보다 현금흐름 visibility가 강하므로 별도 archetype으로 분리.
- `DATA_CENTER_GRID_PERMITTING_OVERLAY`: 데이터센터 전력 수요가 있어도 지역 반발, 수자원, 전력망 접속, moratorium, noise risk를 hard overlay로 기록.

## Case Pack

- case_candidate_count: 16
- structural_success_count: 1
- success_candidate_count: 8
- cyclical_success_count: 0
- event_premium_count: 2
- failed_rerating_count: 1
- stage4b_case_count: 2
- stage4c_case_count: 3

대표 케이스:

- `us_transformer_shortage_import_slots_case`
- `abb_medium_voltage_expansion_case`
- `ge_vernova_data_center_orders_case`
- `perth_data_center_withdrawal_case`
- `seattle_indianapolis_data_center_moratorium_case`
- `hanwha_aerospace_romania_k9_case`
- `hanwha_aerospace_europe_sales_visibility_case`
- `hanwha_aerospace_dilution_case`
- `hanwha_ocean_us_shipbuilding_sanction_case`
- `hanwha_vatn_underwater_drone_case`
- `hyundai_rotem_morocco_rail_case`
- `meta_constellation_existing_nuclear_ppa_case`
- `constellation_tmi_microsoft_restart_case`
- `nuscale_uamps_smr_cancel_case`

## Outputs

- `data/e2r_case_library/cases_r1_loop4_round80.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round80_r1_loop4_v4.csv`
- `output/e2r_round80_r1_loop4_industrial_infra/round80_r1_loop4_industrial_infra_summary.md`
- `output/e2r_round80_r1_loop4_industrial_infra/round80_r1_loop4_case_matrix.csv`
- `output/e2r_round80_r1_loop4_industrial_infra/round80_r1_loop4_stage_date_plan.csv`
- `output/e2r_round80_r1_loop4_industrial_infra/round80_r1_loop4_green_guardrails.md`
- `output/e2r_round80_r1_loop4_industrial_infra/round80_r1_loop4_risk_overlays.md`
- `output/e2r_round80_r1_loop4_industrial_infra/round80_r1_loop4_price_validation_plan.md`
- `output/e2r_round80_r1_loop4_industrial_infra/round80_r1_loop4_price_fields.csv`

## Guardrails

- Round80 case pack은 calibration/evaluation material이다.
- Case record를 후보 생성 input으로 쓰지 않는다.
- Stage 3-Green 기준은 낮추지 않는다.
- 수주 뉴스, MOU, 정책 기대, prototype, 프로젝트 headline만으로 Green을 만들지 않는다.
- 예를 들어 `as_of_date=2025-02-26`에 철도 수주가 확인되면 Stage 2 근거가 될 수 있지만, 그날 기준으로 마진, financing, warranty, 납품 스케줄, OP/EPS 경로가 확인되지 않으면 Green 근거로 쓰지 않는다.
- 데이터센터 수요가 강해도 인허가 지연이나 프로젝트 철회가 있으면 전력장비 수요 경로를 다시 검증한다.

## Verification

- `PYTHONPATH=src python -m unittest tests.test_round80_r1_loop4_industrial_infra -v`
- `PYTHONPATH=src python -m e2r.cli.build_round80_r1_loop4_report`
- `PYTHONPATH=src python -m compileall -q src tests`
- `PYTHONPATH=src python -m unittest discover -s tests -v`
- `git diff --check`
