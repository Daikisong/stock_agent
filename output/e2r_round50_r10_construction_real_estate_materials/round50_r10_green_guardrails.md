# Round-50 R10 Green Guardrails

| target | posture | Green unlock evidence | Red flags |
| --- | --- | --- | --- |
| `CONSTRUCTION_REAL_ESTATE_CREDIT` | REDTEAM_FIRST | refinancing_success, cash_flow_improvement, unsold_inventory_decline, cost_ratio_stable | pf_exposure, unsold_inventory, refinancing, construction_cost_ratio, debt_workout |
| `REIT_DEVELOPMENT_TRUST` | WATCH_YELLOW_FIRST | occupancy, noi_affo, dividend_coverage, ltv_stable, funding_cost_controlled | vacancy, ltv, refinancing, dividend_cut, funding_cost |
| `BUILDING_MATERIALS_CYCLE` | WATCH_YELLOW_FIRST | volume_recovery, price_hike, cost_pass_through, opm_improvement, fcf_stability | volume_decline, energy_cost, raw_material_cost, construction_slowdown |
| `DATA_CENTER_REIT_INFRASTRUCTURE` | GREEN_POSSIBLE | asset_acquisition, hyperscale_tenant, noi_affo, dividend_coverage, power_secured | no_assets, tenant_concentration, capex, funding_cost, power_water_permitting |
| `COLD_CHAIN_REIT_LOGISTICS` | GREEN_POSSIBLE | occupancy, customer_count, noi_affo, energy_cost_control, dividend_coverage | net_loss, energy_cost, debt, occupancy, affo_uncertainty |
| `INFRA_RECONSTRUCTION_POLICY` | REDTEAM_FIRST | actual_contract, financing_secured, contract_margin_visible, delivery_schedule | no_actual_contract, financing, policy_event_only, project_delay |
| `DISASTER_REBUILD_EVENT` | REDTEAM_FIRST | actual_order, margin_visibility, repeat_demand | one_off_demand, inventory, margin_reversal, policy_event_only |
| `COMMERCIAL_REAL_ESTATE_CREDIT` | REDTEAM_FIRST | vacancy_stabilization, loan_quality_recovery, dividend_coverage | office_exposure, vacancy, impaired_asset, credit_loss_reserve, dividend_cut |
| `RESIDENTIAL_HOUSING_CYCLE` | WATCH_YELLOW_FIRST | unsold_inventory_decline, cost_ratio_stable, cash_flow_recovery, credit_risk_low | unsold_inventory, household_debt, rate, construction_cost, starts_decline |
| `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT` | WATCH_YELLOW_FIRST | tenant_lease, power_secured, funding_secured, revenue_start | pre_revenue, permitting, funding, power_water, tenant_missing |

## What Not To Change

- Do not apply these R10 v1.0 weights to production scoring yet.
- Do not treat backlog, asset value, dividend yield, policy support, rate cuts, reconstruction headlines, or AI data-center labels as Green evidence by itself.
- Do not invent PF exposure, unsold inventory, NOI/AFFO, dividend coverage, LTV, occupancy, power, tenant, or price-path fields.
- Do not lower Stage 3-Green for construction recall. Green requires source-backed credit repair, cash-flow recovery, asset cash flow, or contract economics.
- Treat PF delinquency, bridge-loan rollover failure, dividend cuts, impaired CRE loans, net losses, no assets, no tenants, and funding gaps as RedTeam evidence.
