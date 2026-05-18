# Round-174 R3 Loop-11 Score -> Stage -> Price Alignment

## Base Score Weights

| component | points | direction | reason |
| --- | ---: | --- | --- |
| `eps_fcf_opm_conversion` | 24 | keep_high | Stage 3 requires OP/EPS/FCF and margin conversion, not EV or ESS keywords. |
| `contract_visibility` | 22 | raise_detail_requirement | Customer, amount, GWh/tonnage, period, production start, offtake, and JV stake drive Stage 2. |
| `capa_utilization_line_conversion` | 14 | raise_after_ev_slowdown | After EV slowdown, installed CAPA is not a positive unless it can be utilized or converted. |
| `structural_demand_shift` | 12 | focus_ess_supply_chain_security | EV-to-ESS, data-center power, graphite security, and resource security matter when they convert to earnings. |
| `early_price_path_validation` | 10 | loop11_axis | The score must test 60D/120D price validation and avoid late event-rally chasing. |
| `safety_regulatory_disclosure_confidence` | 8 | hard_review | Safety, regulation, disclosure gaps, customer secrecy, and non-binding terms cap Stage 3. |
| `valuation_room_4b_runway` | 10 | raise_4b_focus | Battery materials often require 4B cooling when policy or commodity events drive price before revisions. |

## Stage Caps

| stage band | max score | evidence | examples | Green policy |
| --- | --- | --- | --- | --- |
| `Stage 1` | 45 | ev_growth, ess_growth, lithium_rebound, graphite_tariff, cathode_anode_separator_electrolyte_theme | lnf_lithium_event_rally_case | Theme keywords route research only. Green is blocked before contract, utilization, margin, and FCF evidence. |
| `Stage 2` | 70 | contract_amount, customer_name, gwh_or_tonnage, supply_period, offtake_or_jv_stake, production_start | samsung_sdi_ess_lfp_stage2_case, posco_holdings_lithium_resource_stage2_case | Stage 2 can be strong, but Stage 3 waits for OPM, utilization, revenue recognition, and repeat orders. |
| `Stage 2 strong` | watch | large_contract, line_conversion, price_reaction, customer_or_use_case_visible, stage3_fields_pending | samsung_sdi_ess_lfp_stage2_case | Diagnostic band only. It is not canonical Stage 3 and cannot override missing OPM/utilization. |
| `Stage 3` | requires_4_of_7 | confirmed_customer_amount_period, op_eps_revision_or_beat, ev_capa_to_ess_conversion, utilization_recovery, 60d_mfe_20pct, opm_defended_despite_raw_materials, repeat_contract_or_new_customer | samsung_sdi_ess_lfp_stage2_case | Stage 3 is possible only when contracts and utilization convert into earnings and price path before 4B. |
| `Stage 4B` | requires_3_of_5 | stage2_120d_mfe_80pct, one_day_event_rally_10_20pct, policy_or_commodity_event_drives_price, op_eps_revision_lags_price, lithium_graphite_ess_keyword_crowding | posco_future_m_graphite_tariff_4b_case, lnf_lithium_event_rally_case | Policy, tariff, and commodity rallies are cooled when earnings cannot follow. |
| `Stage 4C` | hard_gate | customer_contract_cancelled, factory_idle_or_utilization_collapse, sale_review_or_restructuring, automaker_ev_strategy_retreat, lithium_nickel_price_crash_inventory_loss, customer_terms_undisclosed, operating_loss_persistent | skiet_separator_sale_review_4c_case, ecopro_materials_ev_slowdown_4c_case | Hard RedTeam overrides battery growth narratives when EV demand, utilization, customer strategy, or losses break the path. |

## Alignment Cases

| case | detected stage | price-path status | verdict | adjustment |
| --- | --- | --- | --- | --- |
| `samsung_sdi_ess_lfp_stage2_case` | Stage 2 strong | Contract day +6.1% reference reaction; KRX exact price path needs backfill | stage2_strong_not_green_yet | credit contract value, period, ESS line conversion; cap customer undisclosed and OPM/utilization missing |
| `posco_future_m_graphite_tariff_4b_case` | Stage 2 + 4B-watch | Graphite offtake is Stage 2; tariff +20% is event-rally 4B watch | supply_chain_event_not_green | credit graphite supply security; haircut quarterly pricing, anode OPM missing, and tariff rally |
| `posco_holdings_lithium_resource_stage2_case` | Stage 2 | $765m lithium JV stake is resource security, but lithium cycle caps Green | resource_security_with_cycle_cap | credit named mines and stake; cap before offtake economics, FCF, and low-cost proof |
| `lg_chem_cathode_toyota_stage2_case` | Stage 2 | Toyota Tsusho stake reduces China dependency but plant OPM and utilization remain pending | supply_chain_realign_not_green_yet | credit ownership realignment; cap before customer contract, utilization, and FCF |
| `lg_chem_exxon_non_binding_lithium_case` | Stage 1/2 option | Non-binding lithium deal is not final offtake | non_binding_cap_correct | support research routing; block Stage 3 before final terms |
| `lnf_lithium_event_rally_case` | Stage 1 event / 4B-watch | CATL mine suspension +10% reference move is commodity event premium | event_rally_not_structural | credit price reaction only lightly; block Green without contract, margin, and demand evidence |
| `skiet_separator_sale_review_4c_case` | 4C-watch | EV slowdown, SK On losses, and sale review break separator demand visibility | hard_redteam_alignment | apply separator utilization and parent restructuring penalty |
| `ecopro_materials_ev_slowdown_4c_case` | 4C-watch | Weak EV demand, operating losses, and Ford EV strategy shock hit the material thesis | customer_strategy_break | apply EV demand slowdown, loss, and customer strategy risk gates |
| `enchem_electrolyte_capa_watch_case` | Watch | Electrolyte CAPA needs customer, OPM, and price path backfill | watch_not_green_yet | cap before contract and margin evidence |
| `daejoo_silicon_anode_commercialization_case` | Stage 1/2 watch | Silicon anode commercialization needs customer qualification and volume revenue | commercialization_not_green_yet | cap before commercial volume, ASP, and margin proof |

## Interpretation

- Samsung SDI is the cleanest R3 Stage 2 strong test, but it remains capped before OPM/utilization proof.
- POSCO Future M graphite proves why supply-chain security and event-rally 4B can coexist.
- POSCO Holdings and LG Chem resource/cathode cases are Stage 2 options until FCF and utilization are visible.
- SKIET and EcoPro Materials show why EV slowdown, operating loss, and customer strategy risk must cool CAPA narratives.
