# Round-49 R9 Green Guardrails

| target | posture | Green unlock evidence | Red flags |
| --- | --- | --- | --- |
| `AUTO_MOBILITY_COMPLETED_VEHICLE` | GREEN_POSSIBLE | op_fcf_stability, hybrid_or_mix_improvement, shareholder_return, roe_pbr_rerating, tariff_risk_low | tariff, recall, peak_margin, policy_risk, demand_slowdown |
| `AUTO_MOBILITY_COMPONENTS` | WATCH_YELLOW_FIRST | customer_diversification, cost_pass_through, op_eps_revision, quality_cost_low | customer_concentration, raw_material, quality_cost, oem_pressure |
| `TIRE_AUTO_COMPONENT_SPREAD` | WATCH_YELLOW_FIRST | oe_re_mix, raw_material_spread, op_eps_revision, fcf_margin | north_america_demand, raw_material, china_competition, tariff |
| `AIRLINE_TRAVEL_CYCLE` | WATCH_YELLOW_FIRST | load_factor, yield_or_margin, fuel_fx_risk_low, integration_cost_controlled | fuel, fx, integration_cost, cargo_cycle, regulatory_condition |
| `TRAVEL_LEISURE_REOPENING` | WATCH_YELLOW_FIRST | visitor_spend, hotel_occupancy, revpar, opm_improvement | tourist_mix, policy_event_only, cost_inflation, occupancy_slowdown |
| `CASINO_DUTYFREE_TOURISM` | WATCH_YELLOW_FIRST | tourist_arrivals, casino_drop_amount, duty_free_sales, opm_improvement | china_dependence, drop_amount, capex, policy_event_only |
| `SHIPPING_FREIGHT_CYCLE` | REDTEAM_FIRST | contract_vs_spot_rate, fleet_capacity_discipline, ebitda_cashflow, overcapacity_low | overcapacity, freight_peak, demand_slowdown, route_normalization |
| `LOGISTICS_PARCEL_FREIGHT` | WATCH_YELLOW_FIRST | volume_growth, unit_price_stable, labor_cost_control, opm_improvement | unit_price_pressure, labor_cost, volume_slowdown |
| `RENTAL_USED_CAR_MOBILITY` | WATCH_YELLOW_FIRST | residual_value, repair_cost_per_vehicle, utilization_rate, fcf_margin | residual_value, repair_cost, interest_rate, fleet_writedown |
| `MOBILITY_RENTAL_MICROMOBILITY` | WATCH_YELLOW_FIRST | micromobility_revenue, micromobility_fcf, utilization_rate, debt_maturity_manageable | unit_economics, debt, regulation, seasonality |
| `AUTO_COMPONENTS_EV_ADAS` | WATCH_YELLOW_FIRST | actual_adoption, customer_diversification, op_eps_revision | actual_adoption_missing, customer_concentration, development_cost |
| `URBAN_AIR_DRONE` | REDTEAM_FIRST | type_certification_flag, commercial_revenue, cash_runway_months, dilution_risk_low | certification, cash_burn, dilution, pre_revenue, discounted_offering |
| `SPACE_SUPPLYCHAIN` | REDTEAM_FIRST | actual_delivery_contract, revenue_conversion, backlog_visibility | no_contract, launch_delay, capex_debt, theme_only |
| `SATELLITE_CONNECTIVITY_INFRA` | GREEN_POSSIBLE | satellite_backlog, connectivity_revenue_growth, airline_contract_count, capex_debt_ratio_ok | capex_debt, launch_delay, competitor_constellation, contract_cancellation |

## What Not To Change

- Do not apply these R9 v1.0 weights to production scoring yet.
- Do not treat demand recovery, tourist arrivals, freight spikes, EV fleet expansion, Part 135, SpaceX theme, or policy headlines as Green evidence by itself.
- Do not invent OPM, FCF, unit economics, tourist spend, freight rates, fuel/FX exposure, residual value, certification, backlog, or price-path fields.
- Do not lower Stage 3-Green for mobility recall. Green requires source-backed OPM/FCF, unit economics, valuation room, and low cycle or cash-burn risk.
- Treat overcapacity, fuel/FX shock, EV residual-value failure, discounted offering, certification delay, and policy-event-only rallies as RedTeam evidence.
