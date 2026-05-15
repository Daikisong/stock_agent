# Checkpoint 28A Round 47 - R7 Biotech / Healthcare / Medical Device

Round 47 adds the R7 biotech, healthcare, and medical-device calibration pack.
This is still case-library and score-weight design material only. It does not
change production scoring, StageClassifier thresholds, or RedTeam logic.

## Files Added

- `src/e2r/sector/round47_r7_biotech_healthcare_device.py`
- `src/e2r/cli/build_round47_r7_report.py`
- `tests/test_round47_r7_biotech_healthcare_device.py`
- `data/e2r_case_library/cases_r7_round47.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round47_r7_v1.csv`
- `output/e2r_round47_r7_biotech_healthcare_device/`

## Archetype Updates

Round 47 adds R7-specific canonical archetype labels:

- `CRO_CLINICAL_SERVICE`
- `BIOSIMILAR_COMMERCIALIZATION`
- `BIOSIMILAR_ORIGINATOR_DEFENSE`
- `OBESITY_GLP1_COMMERCIALIZATION`
- `GENE_THERAPY_RARE_DISEASE`
- `AI_DRUG_DISCOVERY_PLATFORM`
- `DIGITAL_HEALTHCARE_AI`
- `DIGITAL_HEALTHCARE_REMOTE_MEDICINE`
- `TELEHEALTH_BEHAVIORAL_HEALTH`
- `PHARMA_CHANNEL_AND_PRIVACY_RISK`
- `MEDICAL_DEVICE_DENTAL_IMPLANT`
- `BOTULINUM_AESTHETIC_REGULATED`
- `DIAGNOSTICS_INFECTIOUS_DISEASE`
- `ANIMAL_HEALTH_BIOSECURITY`

## R7 Split

R7 is not treated as one generic biotech bucket.

- Green-eligible with strict proof: CDMO, GLP-1 commercialization, medical devices, dental implants.
- Watch-to-Green: CRO, biosimilar commercialization, medical AI, remote medicine, botulinum aesthetics, animal health.
- RedTeam-first: gene therapy rare disease, AI drug discovery, telehealth behavioral health, pharma channel/privacy, infectious diagnostics.

Example: a CDMO contract can support higher conviction only when contract duration,
capacity utilization, margin, and FCF conversion appear together. In contrast, an
AI-drug discovery press release is only Stage 1/2 context until milestone revenue,
clinical proof, cash runway, and commercialization evidence exist.

## Case Pack

Round 47 stores 13 calibration records:

- Samsung Biologics US facility acquisition
- Samsung Biologics CDMO contract reference
- Straumann dental implant growth
- FDA counterfeit Botox warning
- Lunit mammography AI subgroup risk
- Lilly oral GLP-1 Foundayo uptake
- Novo Nordisk Wegovy outlook cut
- Hims & Hers GLP-1 strategy shift
- bluebird bio cash crunch
- bluebird revised offer event premium
- Charles River CRO funding crunch
- Teladoc BetterHelp impairment
- Recursion / Exscientia AI drug-discovery platform

All case records are marked as calibration/evaluation material. Missing prices
remain open for backfill.

## R7 Green Rule

R7 Green is not "approval", "clinical success", "AI model AUC", "pilot", or
"disease outbreak demand" by itself. It requires evidence such as:

- contracted capacity and utilization
- prescription volume and insurance coverage
- reimbursement or hospital adoption
- recurring procedures and consumables
- patient uptake and cash runway
- repeat revenue and FCF conversion

## What Not To Change

- Do not apply R7 v1.0 weights to production scoring yet.
- Do not use R7 case records as candidate-generation input.
- Do not lower Stage 3-Green thresholds for biotech recall.
- Do not invent prescriptions, reimbursement, patient uptake, AUC, procedure volume, CAC, churn, or price-path fields.
- Do not treat approval, clinical result, paper, PoC, or AI label as Green evidence alone.

## Verification

Commands used:

```bash
PYTHONPATH=src python -m unittest tests/test_round47_r7_biotech_healthcare_device.py -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/round47_r7_biotech_healthcare_device.py src/e2r/cli/build_round47_r7_report.py tests/test_round47_r7_biotech_healthcare_device.py
PYTHONPATH=src python -m e2r.cli.build_round47_r7_report
```

Full-suite status is tracked separately because the local tree still has
pre-existing deleted `docs/round/round_17.md` files that break the older
round-17 tests.
