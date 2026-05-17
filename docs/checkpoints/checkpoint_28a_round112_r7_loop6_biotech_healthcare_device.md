# Checkpoint 28A Round 112 R7 Loop 6 Biotech / Healthcare / Medical Device

## Scope

- Source round: `docs/round/round_112.md`
- Large sector: `BIOTECH_HEALTHCARE_DEVICE`
- Purpose: calibration and evaluation only
- Production scoring changed: false
- Case records used as candidate-generation input: false

## What Changed

Round 112 keeps the Round 99 healthcare skeleton but makes Loop 6 stricter around commercialization proof.

Simple example:

- `FDA approval` can be Stage 1 or Stage 2 evidence.
- It cannot become Green by itself.
- Scripts, reimbursement, PBM/formulary access, refills, revenue, OPM/FCF, and price-path validation must follow.

Added or split Round 112 target axes:

- `CRO_FUNDING_CYCLE_OVERLAY`
- `BIOSIMILAR_PBM_FORMULARY_SWITCH`
- `ORAL_GLP1_APPROVAL_COMMERCIALIZATION`
- `MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK`
- `SURGICAL_ROBOT_GLP1_PROCEDURE_MIX_OVERLAY`

## Generated Outputs

- `data/e2r_case_library/cases_r7_loop6_round112.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round112_r7_loop6_v6.csv`
- `output/e2r_round112_r7_loop6_biotech_healthcare_device/round112_r7_loop6_biotech_healthcare_device_summary.md`
- `output/e2r_round112_r7_loop6_biotech_healthcare_device/round112_r7_loop6_case_matrix.csv`
- `output/e2r_round112_r7_loop6_biotech_healthcare_device/round112_r7_loop6_stage_date_plan.csv`
- `output/e2r_round112_r7_loop6_biotech_healthcare_device/round112_r7_loop6_green_guardrails.md`
- `output/e2r_round112_r7_loop6_biotech_healthcare_device/round112_r7_loop6_risk_overlays.md`
- `output/e2r_round112_r7_loop6_biotech_healthcare_device/round112_r7_loop6_price_validation_plan.md`
- `output/e2r_round112_r7_loop6_biotech_healthcare_device/round112_r7_loop6_price_fields.csv`

## Summary Counts

- target_count: 32
- case_candidate_count: 19
- structural_success_count: 2
- success_candidate_count: 9
- stage4c_case_count: 8
- green_possible_count: 5
- watch_yellow_first_count: 13
- redteam_first_count: 14
- gate_only_target_count: 9

## Guardrails

- Do not apply Round 112 weights to production scoring yet.
- Do not use Round 112 case records as candidate-generation input.
- Do not infer prescriptions, PBM coverage, reimbursement, hospital adoption, procedure mix, utilization, FCF, or stage prices when source evidence does not contain them.
- Treat approval-without-uptake, CRO funding crunch, compounded GLP-1 crackdown, GLP-1 price war, biosimilar patent litigation, medical-AI subgroup weakness, and device/counterfeit safety events as RedTeam gates.

## Verification

Round-specific test used during implementation:

```bash
PYTHONPATH=src python -m unittest tests.test_round112_r7_loop6_biotech_healthcare_device -v
```

Full verification was run after report generation.
