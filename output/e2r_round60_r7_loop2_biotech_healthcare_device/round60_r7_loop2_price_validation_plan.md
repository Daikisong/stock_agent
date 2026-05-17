# Round-60 R7 Loop-2 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare capacity, utilization, prescriptions, PBM/insurance, reimbursement, patient uptake, hospital adoption, procedure volume, consumables, cash runway, CAC, churn, safety, and regulatory events with price path.
6. Mark capacity-without-utilization, approval-without-uptake, GLP-1 4B-to-4C, telehealth volatility, AI validation-not-commercial, gene-therapy cash crunch, and device safety 4C explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `samsung_biologics_gsk_us_facility_case` | `CDMO_HEALTHCARE_CONTRACT` | 2025-12-22 | needs_price_backfill |
| `samsung_biologics_cdmo_capacity_reference` | `CDMO_HEALTHCARE_CONTRACT` | undated | needs_source_date_and_price_backfill |
| `straumann_dental_implant_vbp_case` | `MEDICAL_DEVICE_DENTAL_IMPLANT` | 2026-02-18 | needs_price_backfill |
| `lilly_foundayo_fda_approval_case` | `OBESITY_GLP1_COMMERCIALIZATION` | 2026-04-01 | needs_price_backfill |
| `lilly_foundayo_prescription_uptake_case` | `OBESITY_GLP1_COMMERCIALIZATION` | 2026-05-08 | needs_price_backfill |
| `lilly_foundayo_switch_maintenance_case` | `OBESITY_GLP1_COMMERCIALIZATION` | 2026-05-12 | needs_price_backfill |
| `biosimilar_access_slow_uptake_case` | `BIOSIMILAR_COMMERCIALIZATION` | 2024-05-01 | missing_direct_symbol_mapping |
| `novo_glp1_price_pressure_case` | `OBESITY_GLP1_COMMERCIALIZATION` | 2026-02-04 | needs_price_backfill |
| `hims_branded_glp1_pivot_loss_case` | `PHARMA_CHANNEL_AND_PRIVACY_RISK` | 2026-05-12 | needs_price_backfill |
| `hims_novo_partnership_case` | `PHARMA_CHANNEL_AND_PRIVACY_RISK` | 2026-03-09 | needs_price_backfill |
| `hims_compounded_glp1_crackdown_case` | `PHARMA_CHANNEL_AND_PRIVACY_RISK` | 2026-02-07 | needs_price_backfill |
| `bluebird_gene_therapy_cash_crunch_case` | `GENE_THERAPY_RARE_DISEASE` | 2025-02-21 | needs_price_backfill |
| `charles_river_cro_funding_crunch_case` | `CRO_CLINICAL_SERVICE` | 2024-08-07 | needs_price_backfill |
| `teladoc_betterhelp_impairment_case` | `TELEHEALTH_BEHAVIORAL_HEALTH` | 2024-08-01 | needs_price_backfill |
| `recursion_exscientia_ai_drug_case` | `AI_DRUG_DISCOVERY_PLATFORM` | 2024-08-08 | needs_price_backfill |
| `lunit_dbt_subgroup_validation_case` | `DIGITAL_HEALTHCARE_AI` | 2025-03-17 | needs_price_backfill |
| `botox_counterfeit_fda_warning_case` | `BOTULINUM_AESTHETIC_REGULATED` | 2025-11-05 | missing_direct_symbol_mapping |

## Alignment Labels

- `COMMERCIALIZATION_ALIGNED`: commercialization, utilization, prescriptions, procedures, reimbursement, or FCF moves with price rerating.
- `APPROVAL_WITHOUT_UPTAKE`: approval exists but patient uptake, reimbursement, prescriptions, or sales are missing.
- `CAPACITY_WITHOUT_UTILIZATION`: capacity/site expansion exists, but contract and utilization are still missing.
- `GLP1_4B_TO_4C`: price/competition/coverage/compounded-drug pressure breaks a GLP-1 narrative.
- `TELEHEALTH_CHANNEL_VOLATILITY`: partnership or channel change creates price action without durable economics.
- `AI_CLINICAL_VALIDATION_NOT_COMMERCIAL`: paper/AUC validates model quality but not paid deployment.
- `GENE_THERAPY_CASH_CRUNCH`: approval fails to convert into cash-flow-safe commercialization.
- `DEVICE_SAFETY_REGULATORY_4C`: counterfeit, VBP, safety, or unapproved-channel risk blocks Green.
