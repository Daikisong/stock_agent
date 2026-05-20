# Round 286 R4 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, full MFE/MAE, spread recovery, call-off, offtake, export-license continuity, binding supply terms, or FCF evidence where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_event_price_anchor
- operating_loss_anchor
- contract_value_anchor
- tariff_rate_anchor
- ownership_stake_anchor
- production_capacity_anchor
- export_control_anchor
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
| r4_loop14_lotte_lgchem_petrochemical_spread_collapse | reported operating-loss and spread-collapse anchors | Spread collapse and deep losses should block commodity-rebound Green. | reported_loss_anchor_not_full_ohlc |
| r4_loop14_lotte_hdhyundai_petrochemical_restructuring | reported restructuring and policy-support anchors | Restructuring policy is Stage 2; Green waits for executed cut and spread recovery. | reported_policy_anchor_not_full_ohlc |
| r4_loop14_hyundai_posco_steel_spread_antidumping | reported anti-dumping event-return and weak-demand anchors | Tariff relief can move price, but demand and steel spread decide FCF. | reported_event_anchor_not_full_ohlc |
| r4_loop14_korea_zinc_strategic_metal_control_premium | reported tender-offer and control-premium anchors | Control premium is 4B-watch until operating cashflow and governance quality confirm. | reported_event_anchor_not_full_ohlc |
| r4_loop14_posco_minres_lithium_resource_integration | reported deal-value and MinRes event anchors | Resource security is Stage 2; Green waits for offtake, processing margin and customer call-off. | counterparty_event_anchor_not_POSCO_full_ohlc |
| r4_loop14_posco_future_m_lnf_lithium_squeeze_rally | reported lithium squeeze event-return anchors | Lithium squeeze is event premium unless it becomes ASP, inventory and margin. | reported_event_anchor_not_full_ohlc |
| r4_loop14_lnf_tesla_4680_cathode_contract_collapse | reported contract-value-collapse anchor | Customer-name contract becomes hard 4C when value and call-off collapse. | reported_contract_anchor_not_full_ohlc |
| r4_loop14_rare_earth_export_control_supply_chain | reported export-control and shipment-decline anchors | Rare-earth headline is not beneficiary evidence unless licenses and shipments continue. | export_control_anchor_not_stock_ohlc |
| r4_loop14_lg_chem_cathode_supply_chain_rebalancing | reported stake-shift and non-binding lithium anchors | Supply-chain rebalancing is Stage 2 until binding terms, ramp and margin confirm. | reported_supply_chain_anchor_not_full_ohlc |
