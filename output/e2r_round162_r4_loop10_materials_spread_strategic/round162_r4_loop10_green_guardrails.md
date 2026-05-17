# Round-162 R4 Loop-10 Green Guardrails

| target | posture | Green unlock evidence | Loop-10 penalties |
| --- | --- | --- | --- |
| `REFINING_OIL_SPREAD` | WATCH_YELLOW_FIRST | repeat_fcf, core_margin_durable, inventory_noise_excluded | refining_margin, inventory_gain_loss, logistics, geopolitics |
| `LUBRICANTS_HIGH_MARGIN_MIX` | GREEN_POSSIBLE | high_margin_mix_durable, repeat_demand, fcf_conversion, capital_return | oil_price, mix, demand, margin |
| `CHEMICAL_SPREAD` | REDTEAM_FIRST | supply_glut_easing, capacity_restructuring, durable_fcf | oversupply, supply_glut, china_middle_east_capacity, inventory |
| `STEEL_METAL_SPREAD` | WATCH_YELLOW_FIRST | supply_discipline, demand_recovery, fcf_margin | china_demand, iron_ore, steel_spread, dividend |
| `IRON_ORE_CHINA_DEMAND_CYCLE` | REDTEAM_FIRST | low_cost_position, fcf_defense, dividend_supported_by_fcf, demand_recovery | china_demand, iron_ore_price, dividend_cut, profit_downcycle |
| `NONFERROUS_STRATEGIC_METALS` | WATCH_YELLOW_FIRST | cost_curve_advantage, supply_constraint, fcf_conversion, capital_return | metal_price, smelting_margin, event_premium, china_demand |
| `COPPER_AI_GRID_STRUCTURAL_DEMAND` | GREEN_POSSIBLE | low_cost_production, production_volume_stable, fcf_conversion, capital_return | tariff_inventory, mine_restart, demand_destruction, stockpile |
| `COPPER_PROCESSING_INPUT_COST_OVERLAY` | REDTEAM_FIRST | not_applicable | sulfuric_acid, processing_input_cost, mine_disruption, tariff_inventory |
| `NICKEL_SULFUR_HPAL_INPUT_COST` | REDTEAM_FIRST | not_applicable | sulfur, sulfuric_acid, hpal_margin, input_cost |
| `FERTILIZER_INPUT_COST_SULFURIC_ACID` | REDTEAM_FIRST | not_applicable | sulfuric_acid, sulfur, ammonia, urea, production_curtailment, guidance_withdrawal |
| `RARE_METALS_PRICE_FLOOR_OFFTAKE` | GREEN_POSSIBLE | government_support, price_floor, offtake_contract, production_capacity, fcf_conversion | policy, production_ramp, project_execution, price_floor |
| `RARE_EARTH_MAGNET_SUPPLY_CHAIN` | GREEN_POSSIBLE | magnet_production, customer_qualification, offtake_contract, recycled_feedstock, fcf_conversion | magnet_ramp, customer_qualification, feedstock, policy_support |
| `RARE_METALS_EXPORT_CONTROL_EVENT` | WATCH_YELLOW_FIRST | price_floor, offtake_contract, production_capacity, fcf_conversion | export_control_relief, price_spike, no_production_capacity, policy_truce |
| `RARE_EARTH_CAPITAL_RAISE_DILUTION` | REDTEAM_FIRST | not_applicable | capital_raise, dilution, capex, valuation_runup |
| `LITHIUM_ESS_DEMAND_CYCLE` | WATCH_YELLOW_FIRST | low_cost_mine, offtake_contract, fcf_defense, capex_discipline | lithium_price, mine_restart, ev_demand, sodium_ion |
| `PRECIOUS_METALS_SAFE_HAVEN_MINERS` | WATCH_YELLOW_FIRST | realized_price, aisc_control, capital_return, fcf_conversion, production_stable | gold_price, aisc, production, jurisdiction |
| `GOLD_MINER_JURISDICTION_RERATING` | WATCH_YELLOW_FIRST | safe_jurisdiction_assets, fcf_conversion, capital_return, reserve_replacement | mna_dilution, integration, gold_price, production |
| `GENERAL_TRADING_RESOURCE_INFRA` | GREEN_POSSIBLE | long_term_offtake, project_stake, fcf, capital_return | commodity, fx, conglomerate_discount, project_delay |
| `LNG_ENERGY_TRADING_DISTRIBUTION` | GREEN_POSSIBLE | long_term_contract, fid_status, project_stake, margin_visible, repeat_fcf | fid, lng_price, project_financing, margin |
| `PAPER_PACKAGING_CYCLE` | WATCH_YELLOW_FIRST | volume_recovery, price_cost_spread, cash_return, fcf_stable | cost, competition, mature_industry, regulatory_remedy |
| `PACKAGING_CONSOLIDATION_REMEDY` | WATCH_YELLOW_FIRST | synergy_realization, fcf_stable, cash_return, regulatory_remedy_completed | regulatory_remedy, plant_divestment, synergy, mature_industry |
| `ADVANCED_MATERIAL_SPECULATIVE_THEME` | REDTEAM_FIRST | commercial_contract, revenue_conversion, fcf_path | commercialization, customer_validation, revenue, dilution |
| `SPECULATIVE_SCIENCE_THEME` | REDTEAM_FIRST | commercial_revenue, customer_validation, fcf_path | replication, commercial_product, customer, revenue |
| `EVENT_PREMIUM_GOVERNANCE_OVERLAY` | REDTEAM_FIRST | not_applicable | event_premium, governance, capital_structure, hostile_takeover |
| `COMMODITY_PRICE_4C_OVERLAY` | REDTEAM_FIRST | not_applicable | commodity_price, supply_restart, dividend, capex |
| `DISCLOSURE_CONFIDENCE_CAP` | REDTEAM_FIRST | not_applicable | contract_value, price_terms, counterparty, duration |

## What Not To Change

- Do not apply R4 Loop-10 v10.0 weights to production scoring yet.
- Do not treat commodity price, spread recovery, tender offers, policy headlines, or science themes as Green evidence by themselves.
- Do not invent spread, offtake, price floor, production capacity, AISC, cash cost, FCF, capital return, project FID, sulfur input cost, or stage prices.
- Treat oversupply, mine restart, dividend cut, inventory distortion, event premium, capital raise, dilution, sulfur/HPAL input-cost squeeze, fertilizer sulfuric-acid squeeze, and no commercialization as RedTeam fields.
