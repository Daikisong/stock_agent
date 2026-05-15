# Round-37 Archetype Price Validation Plan

Round 37 expands score-price validation for backlog, utility-like infrastructure, and recurring software/platform archetypes.

| target | validation_group | metrics | success | failure |
|---|---|---|---|---|
| DEFENSE_TECH_AUTONOMOUS_SYSTEMS | backlog_contract | mfe_90d, mfe_180d, mfe_1y, mae_180d, backlog_growth, contract_conversion, gross_margin | Framework agreement converting into procurement, delivery, EPS revision, and rerating is aligned. | Prototype, news, or private valuation without revenue is price_moved_without_evidence. |
| INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA | utility_like_infra | mfe_180d, mfe_1y, fab_schedule, op_margin, capex_payback, customer_concentration | Fab ramp-up and gas supplier FCF moving together is aligned. | Fab delay or customer capex cut turning plant utilization weak is thesis_break. |
| COLD_CHAIN_REIT_LOGISTICS | reit_utility_like | mfe_180d, mae_1y, affo_growth, occupancy, energy_cost_margin, debt_cost, dividend_coverage | NOI/AFFO and occupancy moving with price is aligned. | Scale or IPO without AFFO quality, funding discipline, and occupancy is no_rerating. |
| DATA_CENTER_WATER_REUSE_INFRA | infra_utility_like | mfe_180d, mfe_1y, contract_to_revenue, permitting_success, service_margin, policy_drawdown | Water-reuse contracts plus recurring service revenue can support Watch-to-Green. | Policy or water-scarcity narrative without customer revenue is event_watch. |
| SATELLITE_CONNECTIVITY_INFRA | software_recurring | mfe_90d, mfe_180d, mfe_1y, backlog_growth, revenue_growth, ebitda_margin, debt_capex | Contract, backlog, recurring connectivity revenue, and margin growth moving together is aligned. | Space or satellite theme without revenue or with debt/capex pressure is false_positive. |
| DEFENSE_AI_SOFTWARE_INTELLIGENCE | software_recurring | mfe_180d, mae_1y, government_revenue_growth, gross_margin, rpo_backlog, program_renewal | Prototype converting into program-of-record and recurring revenue is aligned. | Prototype/news without follow-on contracts is price_only. |
| AI_DATA_CENTER_POWER_EQUIPMENT | backlog_contract | mfe_180d, mfe_1y, bookings_growth, backlog_conversion, gross_margin, valuation_crowding | Bookings converting into revenue and OP is aligned. | Theme rally followed by bookings slowdown or margin miss becomes 4B/4C. |
| DEFENSE_DRONE_COUNTER_UAS | backlog_contract | mfe_180d, mfe_1y, mna_drawdown, backlog_conversion, gross_margin, program_renewal | Defense-tech narrative converting into delivery, backlog, and EPS is aligned. | M&A/prototype/theme without OP/FCF is false_positive. |

## Group Rules
- backlog_contract: validate contract-to-backlog-to-revenue conversion, OP/EPS revisions, and MFE/MAE after Stage 2.
- utility_like_infra/reit_utility_like/infra_utility_like: validate occupancy, plant/facility utilization, AFFO/FCF, and funding or energy cost.
- software_recurring: validate recurring revenue, gross margin, RPO/backlog, churn or renewal, and legal/security drawdowns.
