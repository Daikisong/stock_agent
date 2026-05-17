# Checkpoint 28A Round 73 - R7 Loop 3 Biotech / Healthcare / Medical Device

Round 73 반영 완료.

## Scope

- source round: `docs/round/round_73.md`
- large sector: `BIOTECH_HEALTHCARE_DEVICE`
- loop: `R7 Loop 3 / v3.0`
- production scoring changed: `false`
- case records are candidate-generation input: `false`

이번 라운드는 `허가`, `임상`, `AI 논문`, `TAM`, `공장 증설` 같은 내러티브와 실제 상업화 증거를 분리한다.
쉬운 예로, FDA 승인은 Stage 1~2 증거가 될 수 있지만 주간 처방량, 보험/PBM 접근성, 가격 방어, OP/EPS가 따라오지 않으면 Stage 3-Green 근거가 아니다.

## Targets

- target_count: 20
- green_possible_count: 5
- watch_yellow_first_count: 7
- redteam_first_count: 8
- gate_only_target_count: 4

추가/강화된 핵심 타깃:

- `GLP1_TELEHEALTH_CHANNEL`: GLP-1 약 자체와 Hims 같은 DTC/telehealth 유통채널을 분리.
- `SURGICAL_ROBOT_INSTALLED_BASE`: installed base, procedure growth, instruments/accessories 반복매출을 별도 구조로 분리.
- `COMMERCIALIZATION_FAILURE_OVERLAY`: 승인 후 uptake, 환급, 매출, cash runway 실패를 RedTeam gate로 분리.
- `REIMBURSEMENT_ACCESS_OVERLAY`: 보험, PBM, 수가, 환급 실패를 RedTeam overlay로 분리.
- `DEVICE_SAFETY_COUNTERFEIT_OVERLAY`: 위조품, 무허가 제품, 리콜, 제품안전 문제를 RedTeam overlay로 분리.

## Case Pack

- case_candidate_count: 19
- structural_success_count: 2
- success_candidate_count: 8
- event_premium_count: 1
- stage4c_case_count: 8

우선 검증 케이스:

- `samsung_biologics_gsk_us_facility_case`
- `samsung_biologics_cdmo_capacity_reference`
- `intuitive_surgical_q1_2026_procedure_growth_case`
- `straumann_dental_implant_vbp_case`
- `lilly_foundayo_fda_approval_case`
- `lilly_foundayo_prescription_uptake_case`
- `lilly_foundayo_switch_maintenance_case`
- `boehringer_goodrx_humira_biosimilar_case`
- `novo_glp1_price_pressure_case`
- `hims_branded_glp1_pivot_loss_case`
- `hims_novo_partnership_case`
- `hims_compounded_glp1_crackdown_case`
- `bluebird_gene_therapy_cash_crunch_case`
- `charles_river_cro_funding_crunch_case`
- `teladoc_betterhelp_impairment_case`
- `recursion_exscientia_ai_drug_case`
- `lunit_dbt_subgroup_validation_case`
- `amgen_samsung_bioepis_biosimilar_litigation_case`
- `botox_counterfeit_fda_warning_case`

## Outputs

- `data/e2r_case_library/cases_r7_loop3_round73.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round73_r7_loop3_v3.csv`
- `output/e2r_round73_r7_loop3_biotech_healthcare_device/round73_r7_loop3_biotech_healthcare_device_summary.md`
- `output/e2r_round73_r7_loop3_biotech_healthcare_device/round73_r7_loop3_case_matrix.csv`
- `output/e2r_round73_r7_loop3_biotech_healthcare_device/round73_r7_loop3_stage_date_plan.csv`
- `output/e2r_round73_r7_loop3_biotech_healthcare_device/round73_r7_loop3_green_guardrails.md`
- `output/e2r_round73_r7_loop3_biotech_healthcare_device/round73_r7_loop3_risk_overlays.md`
- `output/e2r_round73_r7_loop3_biotech_healthcare_device/round73_r7_loop3_price_validation_plan.md`
- `output/e2r_round73_r7_loop3_biotech_healthcare_device/round73_r7_loop3_price_fields.csv`

## Guardrails

- R7 Loop 3 weights are calibration material only.
- Case records must not be used as candidate-generation input.
- Approval, clinical success, AI AUC, external-validation paper, pilot, user growth, or disease-event demand cannot create Green alone.
- Do not invent prescription volume, PBM/insurance coverage, reimbursement, capacity utilization, patient uptake, hospital adoption, procedure volume, consumable revenue, cash runway, CAC, churn, or stage prices.
- Safety, reimbursement, commercialization failure, and pharma-channel risks are explicit RedTeam overlays.

## Verification

- `PYTHONPATH=src python -m unittest tests.test_round73_r7_loop3_biotech_healthcare_device -v`
- `PYTHONPATH=src python -m e2r.cli.build_round73_r7_loop3_report`
