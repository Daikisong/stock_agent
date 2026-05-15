# Round-47 R7 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Calculate peak price, drawdown after peak, and below-stage3 flag.
6. Compare price paths with utilization, prescriptions, reimbursement, patient uptake, hospital adoption, procedure volume, consumables, cash runway, CAC, churn, and safety/regulatory events.

## Priority Case Checks

| case_id | stage candidate | check |
| --- | --- | --- |
| `samsung_biologics_gsk_us_facility_case` | 2025-12-22 | needs_price_backfill |
| `samsung_biologics_cdmo_contract_reference` | needs_source_date | needs_source_date_and_price_backfill |
| `straumann_dental_implant_growth_case` | 2026-02-18 | needs_price_backfill |
| `botox_counterfeit_fda_warning_case` | 2025-11-05 | missing_direct_symbol_mapping |
| `lunit_mammography_ai_subgroup_case` | 2025-03-17 | needs_price_backfill |
| `lilly_oral_glp1_foundayo_case` | 2026-05-08 | needs_price_backfill |
| `novo_wegovy_outlook_cut_case` | 2025-05-07 | needs_price_backfill |
| `hims_glp1_strategy_shift_case` | 2026-05-11 | needs_price_backfill |
| `bluebird_gene_therapy_cash_crunch_case` | 2025-02-21 | needs_price_backfill |
| `bluebird_revised_offer_event_premium_case` | 2025-05-14 | needs_price_backfill |
| `charles_river_cro_funding_crunch_case` | 2024-08-07 | needs_price_backfill |
| `teladoc_betterhelp_impairment_case` | 2024-08-01 | needs_price_backfill |
| `recursion_exscientia_ai_drug_platform_case` | 2024-08-08 | needs_price_backfill |

## Alignment Labels

- `aligned`: commercialization, utilization, prescriptions, procedures, reimbursement, or FCF moves with price rerating.
- `delayed_or_uncertain`: strategic evidence exists, but price or EPS/FCF conversion is not yet confirmed.
- `approval_without_commercialization`: approval exists but patient uptake, reimbursement, or sales are missing.
- `clinical_or_ai_hype`: paper, AI model, or PoC drives attention without paid deployment.
- `event_premium`: M&A or revised offer moves price without operational rerating.
- `thesis_break`: cash crunch, forecast cut, safety event, impairment, or one-off demand normalization breaks the thesis.
