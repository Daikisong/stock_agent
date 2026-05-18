# Round-174 R3 Loop-11 Green Guardrails

| target | posture | Green unlock evidence | Loop-11 penalties |
| --- | --- | --- | --- |
| `ESS_LFP_GRID_STORAGE_KOREA` | GREEN_POSSIBLE | customer_or_use_case, contract_value, supply_period, utilization, ess_opm, fcf_conversion | customer_disclosure, opm_utilization, line_conversion |
| `EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA` | WATCH_YELLOW_FIRST | ess_customer_contract, converted_line_utilization, ess_opm, fcf_conversion | utilization, conversion_cost, contract_absent |
| `ANODE_GRAPHITE_SUPPLYCHAIN_KOREA` | WATCH_YELLOW_FIRST | graphite_offtake, tonnage, customer_adoption, anode_margin, fcf_conversion | event_rally, pricing_risk, opm_missing |
| `CATHODE_LONG_CONTRACT_VISIBILITY` | WATCH_YELLOW_FIRST | customer_contract, plant_utilization, opm_fcf, price_pass_through | margin, lithium_price, customer_concentration |
| `LITHIUM_RESOURCE_SECURITY_KOREA` | WATCH_YELLOW_FIRST | offtake_economics, low_cost_structure, margin_benefit, fcf_improvement | commodity_cycle, capex, impairment |
| `BATTERY_MATERIALS_CAPEX_OVERHEAT_KOREA` | REDTEAM_FIRST | utilization, margin, fcf, customer_demand | ev_demand, losses, customer_strategy, capa_overbuild |
| `SEPARATOR_EV_DEMAND_CYCLE` | REDTEAM_FIRST | utilization_recovery, margin, customer_diversification | ev_demand, utilization, sale_review |
| `ELECTROLYTE_CAPA_SUPPLYCHAIN` | WATCH_YELLOW_FIRST | customer_contract, shipment, opm, fcf_conversion | contract_missing, utilization, price_pressure |
| `SILICON_ANODE_COMMERCIALIZATION` | WATCH_YELLOW_FIRST | commercial_volume, customer_qualification, asp_margin, op_eps_revision | commercialization, volume, margin |
| `EVENT_LITHIUM_PRICE_RALLY` | REDTEAM_FIRST |  | event_rally, commodity_cycle, op_eps_missing |
| `CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK` | REDTEAM_FIRST | customer_strategy_stable, contract_reaffirmed, utilization_recovered | customer_strategy_risk, contract_cancelled, factory_idle, losses |
| `DISCLOSURE_CONFIDENCE_CAP` | REDTEAM_FIRST | customer, amount, period, gwh_or_tonnage, opm, utilization | disclosure_confidence, detail_missing |

## What Not To Change

- Do not apply R3 Loop-11 v11.0 weights to production scoring yet.
- Do not lower Stage 3-Green thresholds because ESS or battery-material stocks moved.
- Do not use Round 174 case records as candidate-generation input.
- Do not treat EV growth, ESS keyword, lithium rebound, graphite tariff, non-binding offtake, or CAPA narrative as Green by itself.
- Do not invent customer names, contract amounts, GWh/tonnage, utilization, margins, stage prices, MFE/MAE, or raw-material exposure.
- Apply 4B-watch when policy, tariff, lithium, graphite, or ESS keyword rallies outrun OP/EPS revision.
- Apply 4C/hard review for contract cancellation, factory idle, sale review, customer EV strategy retreat, operating losses, or missing contract terms.
