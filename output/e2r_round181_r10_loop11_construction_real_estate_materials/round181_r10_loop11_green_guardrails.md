# Round-181 R10 Loop-11 Green Guardrails

| target | posture | Green unlock evidence | Loop-11 penalties |
| --- | --- | --- | --- |
| `OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA` | GREEN_POSSIBLE | contract_amount, counterparty, completion_date, cost_ratio_stable, op_eps_revision, cash_conversion_improves | cost_ratio, cash_conversion, low_margin_order, delay |
| `EPC_LOW_MARGIN_ORDER_OVERLAY` | REDTEAM_FIRST |  | cost, delay, margin, cash |
| `AI_DATA_CENTER_REAL_ASSET_KOREA` | WATCH_YELLOW_FIRST | binding_epc_contract, tenant_lease, power_water_secured, noi_affo_or_op_eps_visible | no_contract, no_tenant, power_water, noi_affo |
| `CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA` | REDTEAM_FIRST |  | pf, workout, liquidity, bridge_loan |
| `PF_RESTRUCTURING_RELIEF_KOREA` | WATCH_YELLOW_FIRST | pf_exposure_decreases, pf_refinancing, cash_conversion_improves, cost_ratio_stable | policy_only, pf_exposure, cash_conversion, impairment |
| `APARTMENT_QUALITY_SAFETY_OVERLAY` | REDTEAM_FIRST |  | safety, quality, investigation, brand |
| `LARGE_BUILDER_BALANCE_SHEET_DEFENSE` | GREEN_POSSIBLE | pf_exposure_decreases, cash_conversion_improves, cost_ratio_stable, op_eps_revision, unsold_units_decline | pf, cash, cost_ratio, unsold_units |
| `K_REIT_DIVIDEND_COVERAGE` | WATCH_YELLOW_FIRST | affo_per_share_improves, dividend_coverage_stable, ltv_stable, occupancy_resilient | dividend, ltv, refinancing, occupancy |
| `LOGISTICS_REIT_OCCUPANCY_KOREA` | GREEN_POSSIBLE | occupancy_resilient, rental_growth, affo_per_share_improves, ltv_stable | vacancy, tenant, ltv, dividend |
| `BUILDING_MATERIALS_PRICE_COST_KOREA` | WATCH_YELLOW_FIRST | opm_fcf_improves, volume_defended, raw_material_cost_stable, specialty_mix_margin | volume, raw_material, housing_cycle, integration |
| `CEMENT_REGULATORY_COLLUSION_OVERLAY` | REDTEAM_FIRST |  | collusion, regulation, volume, starts |
| `HOME_INTERIOR_HOUSING_CYCLE` | WATCH_YELLOW_FIRST | opm_fcf_improves, housing_volume_defended, working_capital_clean, valuation_old_frame | transaction, inventory, margin, raw_material |
| `DISCLOSURE_CONFIDENCE_CAP` | REDTEAM_FIRST | contract_amount, pf_detail, noi_affo, cost_ratio, dividend_coverage | disclosure, detail, cashflow, parser_confidence |

## What Not To Change

- Do not apply R10 Loop-11 v11.0 weights to production scoring yet.
- Do not treat EPC order, PF support, rate-cut expectation, AI data-center headline, REIT yield, or cement price hike as Green evidence by itself.
- Do not invent contract amount, PF exposure, NOI/AFFO, cost ratio, dividend coverage, stage prices, or MFE/MAE.
- Green requires contract/PF/NOI/AFFO or cost evidence, clean safety and quality status, and price-path support.
- PF workout, fatal accident, quality cost, dividend cut, no tenant, collusion, and disclosure confidence failures remain RedTeam gates.
