# E2R Theme Refinement Round 12

Round 12 refines the theme taxonomy where Round 10 was still too broad.

The important rule is unchanged:

> Theme names route research. Evidence creates score.

Easy examples:

- `편의점` routes to `RETAIL_CONVENIENCE_OFFLINE`, but Stage quality depends on same-store sales, PB mix, OPM, and FCF.
- `손해보험` routes to `INSURANCE_UNDERWRITING_CYCLE`, but Stage quality depends on loss ratio, CSM/capital, ROE, and shareholder return.
- `스테이블코인` routes to `DIGITAL_ASSET_TOKENIZATION`, but it stays RedTeam-first until regulated revenue and adoption exist.
- `초전도체` routes to `SPECULATIVE_SCIENCE_THEME`, but it cannot become Green from the theme tag alone.

## Refined Sub-Archetypes

Round 12 adds 18 refinement targets:

- `RETAIL_CONVENIENCE_OFFLINE`
- `ECOMMERCE_FRESH_LOGISTICS`
- `INSURANCE_UNDERWRITING_CYCLE`
- `PAYMENT_FINTECH_INFRA`
- `DIGITAL_ASSET_TOKENIZATION`
- `BEAUTY_OEM_ODM_SUPPLYCHAIN`
- `AGRI_LIVESTOCK_FOOD_COMMODITY`
- `BUILDING_MATERIALS_CYCLE`
- `RENEWABLE_ENERGY_POLICY`
- `HYDROGEN_FUEL_CELL_INFRA`
- `SOLAR_TARIFF_SUPPLYCHAIN`
- `TIRE_AUTO_COMPONENT_SPREAD`
- `EVENT_DISEASE_PEST_DEMAND`
- `SPECULATIVE_SCIENCE_THEME`
- `WASTE_RECYCLING_ENVIRONMENT`
- `MEDIA_AD_CONTENT_CYCLE`
- `CLOUD_AI_SOFTWARE_INFRA`
- `SECURITY_IDENTITY_DEEPFAKE`

## Output Files

- `data/sector_taxonomy/theme_tag_map_round12.csv`
- `output/e2r_round12_theme_refinement/round12_theme_refinement_summary.md`
- `output/e2r_round12_theme_refinement/round12_sub_archetype_refinements.csv`
- `output/e2r_round12_theme_refinement/round12_case_candidate_plan.csv`
- `output/e2r_round12_theme_refinement/round12_theme_tag_map_schema.md`
- `output/e2r_round12_theme_refinement/round12_next_case_library_plan.md`

## Guardrails

- Do not use theme tags as production evidence.
- Do not apply `score_weight_profile` to production scoring yet.
- Do not lower Stage 3-Green thresholds.
- Do not turn one-off disease, speculative science, or tokenization themes Green without verified recurring revenue and EPS/FCF evidence.
