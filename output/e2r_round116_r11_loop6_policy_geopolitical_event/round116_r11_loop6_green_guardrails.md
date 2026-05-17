# Round-116 R11 Loop-6 Green Guardrails

| target | posture | Green unlock evidence | Red flags |
| --- | --- | --- | --- |
| `NORTH_KOREA_POLICY_EVENT` | REDTEAM_FIRST | sanctions_relief, funded_project, cash_flow_project, revenue_visibility | sanctions, military_tension, facility_dismantle, road_rail_destroyed, policy_reversal |
| `GEOPOLITICAL_RECONSTRUCTION` | WATCH_YELLOW_FIRST | actual_project, project_financing, company_contract, margin_visibility | mou_only, financing_missing, geopolitical_setback, project_delay |
| `REAL_RECONSTRUCTION_FINANCING` | WATCH_YELLOW_FIRST | project_financing, operating_company, infrastructure_asset, company_contract, revenue_visibility | war_risk, financing_delay, no_company_contract, insurance_absent |
| `CRITICAL_INFRA_RECONSTRUCTION_FINANCING` | WATCH_YELLOW_FIRST | project_financing, guarantee_structure, critical_infra_asset, company_contract, revenue_visibility | war_risk, insurance_absent, guarantee_failure, no_company_contract, project_delay |
| `STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT` | WATCH_YELLOW_FIRST | domestic_capacity_flag, alternative_supply_contract_flag, offtake_contract_flag, price_floor_flag, revenue_recognized_flag | export_control_relief, no_domestic_capacity, no_offtake_contract, price_spike_normalization |
| `EXPORT_CONTROL_TO_OFFTAKE_ESCALATION` | WATCH_YELLOW_FIRST | alternative_supply_contract_flag, offtake_contract_flag, price_floor_flag, domestic_capacity_flag, volume_margin_visibility | offtake_absent, price_floor_absent, capacity_delay, export_control_relief |
| `DISASTER_REBUILD_EVENT` | WATCH_YELLOW_FIRST | rebuild_order, budget_approved, margin_visibility, repeat_demand | one_off_demand, budget_delay, insurance_delay, inventory |
| `CLIMATE_DISASTER_EVENT` | WATCH_YELLOW_FIRST | repeat_demand, grid_capex, sales_or_order, margin_visibility, vpp_or_ess_revenue | seasonality, weather_fade, inventory, no_sales_conversion |
| `CLIMATE_EVENT_TO_GRID_INFRA` | WATCH_YELLOW_FIRST | vpp_program, battery_program_capacity, grid_service_revenue, repeat_program_expansion | seasonal_demand, pilot_only, budget_delay, no_sales_conversion |
| `EVENT_DISEASE_PEST_DEMAND` | REDTEAM_FIRST | government_order, stockpile_contract, guide_up, recurring_procurement | one_off_outbreak, demand_normalization, purchase_end, inventory |
| `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE` | WATCH_YELLOW_FIRST | stockpile_contract_flag, guidance_raised_flag, government_order_flag, contract_value, repeat_procurement | one_off_stockpile, procurement_uncertainty, funding_withdrawal, demand_normalization |
| `PUBLIC_HEALTH_PROCUREMENT_REVERSAL` | REDTEAM_FIRST | funding_secured, procurement_schedule, repeat_procurement, commercialization | government_contract_cancelled, funding_withdrawal, procurement_uncertainty, clinical_delay |
| `DIAGNOSTICS_INFECTIOUS_EVENT` | REDTEAM_FIRST | non_event_revenue, recurring_testing_demand, margin_normalization, fcf_conversion | covid_like_one_off, sales_decline, guide_down, inventory |
| `SPECULATIVE_SCIENCE_THEME` | REDTEAM_FIRST | replication_success, commercial_product, customer_contract, revenue | replication_failure, no_commercial_product, preprint_only, sns_only |
| `ADVANCED_MATERIAL_SPECULATIVE_THEME` | REDTEAM_FIRST | technical_validation, pilot_customer, revenue_conversion, margin_visibility | paper_only, no_customer, no_revenue, funding_need |
| `POLICY_LOCAL_THEME` | REDTEAM_FIRST | budget_approved, contract_awarded, revenue_visibility, margin_visibility | budget_missing, policy_reversal, project_delay, no_exposure |
| `TOURISM_POLICY_EVENT` | WATCH_YELLOW_FIRST | visitor_arrivals, average_spend, casino_drop_amount, duty_free_sales, hotel_revpar, opm_visibility | spend_missing, drop_amount_missing, policy_ends, opm_missing |
| `INDUSTRIAL_POLICY_TARIFF_EVENT` | WATCH_YELLOW_FIRST | actual_rule, budget_allocated, company_eps_fcf_impact, margin_visibility | tariff_reversal, subsidy_cut, policy_delay, input_cost_risk |
| `ONE_OFF_EVENT_DEMAND` | REDTEAM_FIRST | recurrence_proven, post_event_revenue_base, fcf_conversion | one_off_risk, normalization, purchase_end, margin_reversal |
| `EVENT_TO_CONTRACT_ESCALATION` | WATCH_YELLOW_FIRST | actual_contract, budget_or_financing, revenue_recognized, margin_visibility | headline_only, contract_missing, budget_missing, revenue_missing |
| `POLICY_MARKET_SHOCK_EVENT` | REDTEAM_FIRST | company_eps_fcf_impact, policy_clarity, low_risk_premium | windfall_tax_comment, citizen_dividend_comment, corporate_tax_uncertainty, market_wide_selloff, government_clarification_needed |
| `AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK` | REDTEAM_FIRST | policy_clarity, company_level_eps_impact, risk_premium_normalized | windfall_tax_comment, citizen_dividend_comment, corporate_tax_uncertainty, market_wide_selloff |
| `THEME_VALUATION_OVERHEAT` | REDTEAM_FIRST | cross_evidence, eps_fcf_path, redteam_low | price_only, crowding, no_cash_flow, dilution |
| `DISCLOSURE_CONFIDENCE_CAP` | REDTEAM_FIRST |  | budget_detail_missing, contract_detail_missing, order_detail_missing, construction_start_missing, parser_confidence_low |

## What Not To Change

- Do not apply these R11 Loop-6 v6 weights to production scoring yet.
- Do not treat policy headlines, war/reconstruction slogans, disasters, outbreaks, local policy, or preprints as Green evidence by itself.
- Do not invent contracts, government orders, budgets, dose amounts, project financing, construction starts, revenue, guidance, or price-path fields.
- Do not lower Stage 3-Green for event recall. Green requires source-backed contract, budget, revenue, recurring demand, or EPS/FCF conversion.
- Treat replication failure, facility dismantling, military escalation, demand normalization, purchase end, budget delay, and no-customer science themes as RedTeam evidence.
