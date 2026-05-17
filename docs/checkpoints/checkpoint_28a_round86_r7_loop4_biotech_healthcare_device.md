# Checkpoint 28A Round86 R7 Loop4 Biotech / Healthcare / Medical Device

## Summary

- source_round: `docs/round/round_86.md`
- large_sector: `BIOTECH_HEALTHCARE_DEVICE`
- target_count: 23
- case_candidate_count: 19
- green_possible_count: 5
- watch_yellow_first_count: 9
- redteam_first_count: 9
- gate_only_target_count: 5
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## What Changed

Round86 tightens the R7 healthcare taxonomy so approvals, AI validation, capacity stories, and telehealth growth are separated from real commercialization evidence.

New or newly separated targets:

- `CDMO_US_TARIFF_HEDGE_CAPACITY`
- `BIOSIMILAR_PATENT_LITIGATION`
- `ORAL_GLP1_MAINTENANCE_THERAPY`
- `COMPOUNDED_GLP1_REGULATORY_RISK`
- `MEDICAL_AI_EXTERNAL_VALIDATION`

Example: an oral GLP-1 approval can be Stage 1/2 evidence. It should not become Stage 3-Green until weekly scripts, insurance coverage, refill behavior, pricing, and OP/EPS evidence are visible.

## Case Pack

Generated:

- `data/e2r_case_library/cases_r7_loop4_round86.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round86_r7_loop4_v4.csv`
- `output/e2r_round86_r7_loop4_biotech_healthcare_device/round86_r7_loop4_biotech_healthcare_device_summary.md`
- `output/e2r_round86_r7_loop4_biotech_healthcare_device/round86_r7_loop4_case_matrix.csv`
- `output/e2r_round86_r7_loop4_biotech_healthcare_device/round86_r7_loop4_stage_date_plan.csv`
- `output/e2r_round86_r7_loop4_biotech_healthcare_device/round86_r7_loop4_green_guardrails.md`
- `output/e2r_round86_r7_loop4_biotech_healthcare_device/round86_r7_loop4_risk_overlays.md`
- `output/e2r_round86_r7_loop4_biotech_healthcare_device/round86_r7_loop4_price_validation_plan.md`
- `output/e2r_round86_r7_loop4_biotech_healthcare_device/round86_r7_loop4_price_fields.csv`

## Guardrails

- FDA/EMA approval, clinical success, AI AUC, pilot adoption, or large TAM is not Green evidence by itself.
- CDMO capacity must be tied to utilization, customer contracts, technology transfer, OPM, and FCF.
- Biosimilar approval must be tied to PBM/coverage, prescriptions, launch timing, and margin.
- Compounded GLP-1 is treated as a RedTeam gate when FDA, DOJ, copycat, quality, or channel shutdown risk appears.
- Medical AI external validation is Stage 1/2 evidence until hospital deployment, reimbursement, recurring revenue, and liability control are proven.

## Verification

Targeted tests passed:

```bash
PYTHONPATH=src python -m unittest tests.test_round86_r7_loop4_biotech_healthcare_device -v
```

Full repository verification was run after report generation before commit.

