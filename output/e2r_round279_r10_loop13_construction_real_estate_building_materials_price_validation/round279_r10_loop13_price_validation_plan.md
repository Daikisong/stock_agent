# Round 279 R10 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, PF cashflow, EPC margin, legal clearance, presales, spread, safety remediation or FCF where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- policy_or_project_value_anchor
- PF_delinquency_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- safety_trust_anchor
- legal_appeal_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r10_loop13_real_estate_pf_taeyoung_liquidity_watch | Reuters PF/liquidity support and FSS restructuring anchors | Policy support is relief, not project cashflow Green | sector_policy_anchor_not_full_ohlc |
| r10_loop13_samsung_ena_gs_fadhili_epc_order_stage2 | Reuters Aramco Fadhili contract + WSJ Samsung E&A event-return anchor | Mega-order event premium; EPC margin and cashflow required | reported_event_anchor_not_full_ohlc |
| r10_loop13_czech_nuclear_infra_preferred_bidder_legal_watch | Reuters Czech nuclear preferred-bidder and appeal anchors | Preferred bidder drove price first; legal and final contract gates remain | reported_return_anchor_not_full_ohlc |
| r10_loop13_hyundai_steel_construction_material_demand_break | MarketWatch Hyundai Steel demand-risk anchor + Reuters steel anti-dumping anchor | Demand evidence was negative; tariff relief did not prove spread/FCF | reported_event_anchor_not_full_ohlc |
| r10_loop13_seoul_property_policy_ratecut_macro_gate | Reuters property policy / BOK macroprudential anchors | Property/rate-cut expectations remain macro event premium | policy_macro_anchor_not_full_ohlc |
| r10_loop13_anseong_highway_construction_safety_reference | Reuters construction-site collapse safety anchor | Fatal worksite event confirms construction safety hard gate | sector_safety_reference |
| r10_loop13_builder_liquidity_package_policy_relief | Reuters builders support / housing supply policy anchors | Support is Stage 2 relief until project cashflow proves out | policy_relief_anchor_not_full_ohlc |
| r10_loop13_steel_plate_anti_dumping_construction_relief | Reuters steel plate anti-dumping anchor | Tariff relief can move price, but not prove demand/spread/FCF | reported_event_anchor_not_full_ohlc |
