# Round 285 R3 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, full MFE/MAE, call-off, utilization, AMPC quality, customs clearance, ESS value, hydrogen demand, silicon-anode contracts, or listed EPS bridge where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- contract_value_anchor
- operating_loss_anchor
- factory_investment_anchor
- policy_subsidy_anchor
- customs_supply_chain_anchor
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r3_loop14_lges_ford_freudenberg_contract_cancellation_hard_4c | Reuters contract-cancellation and event-return anchors | Major customer call-off broke expected revenue and utilization thesis. | reported_event_anchor_not_full_ohlc |
| r3_loop14_samsung_sdi_gm_jv_stage2_ev_demand_watch | Reuters GM JV and EV-demand anchors | JV capacity is Stage 2; actual call-off, utilization, AMPC and margin are required. | reported_event_anchor_not_full_ohlc |
| r3_loop14_sk_innovation_skon_restructuring_ess_pivot | Reuters merger, JV dissolution and ESS anchors | Restructuring and ESS pivot are Stage 2; profitability and disclosed ESS economics are required. | reported_event_anchor_not_full_ohlc |
| r3_loop14_battery_material_supply_chain_ford_beta | MarketWatch Ford EV pivot / Korea battery supply-chain anchor | Ford model mix can lower battery content and directly hit material suppliers. | reported_event_anchor_not_full_ohlc |
| r3_loop14_hanwha_qcells_solar_policy_customs_gate | Reuters DOE loan guarantee and Qcells furlough anchors | Policy loan is Stage 2; customs clearance and utilization are Green gates. | direct_event_return_unavailable_after_deep_search |
| r3_loop14_hyundai_hydrogen_fuel_cell_capex_stage2 | Reuters Hyundai hydrogen fuel-cell plant anchor | Hydrogen plant capex is Stage 2; demand, utilization and unit economics are required. | price_data_unavailable_after_deep_search |
| r3_loop14_sk_group14_silicon_anode_stage2 | Reuters Group14 financing and JV-control anchor | Silicon-anode technology is Stage 2; listed SK Green needs contracts, yield, margin and value bridge. | price_data_unavailable_after_deep_search |
| r3_loop14_korean_battery_ess_pivot_cross_reference | Reuters SK On ESS and battery-sector pivot anchors | ESS pivot is Stage 2; PO value, installation, margin and repeat orders are required. | price_data_unavailable_after_deep_search |
