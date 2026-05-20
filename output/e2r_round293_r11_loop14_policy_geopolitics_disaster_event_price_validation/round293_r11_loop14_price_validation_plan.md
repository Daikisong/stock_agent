# Round 293 R11 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, drilling result, sanction removal, tax law, foreign flow, claims, contract margin, labor continuity or FCF where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_event_price_anchor
- policy_amount_anchor
- liquidity_facility_anchor
- sanction_scope_anchor
- disaster_casualty_anchor
- labor_loss_estimate_anchor
- order_value_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r11_loop14_kogas_blue_whale_resource_event_premium | Reuters / WSJ resource-discovery event anchors | Resource headline moved price before reserve confirmation, drilling result, CAPEX/IRR or production cashflow | reported_event_anchor_not_full_ohlc |
| r11_loop14_hanwha_ocean_china_sanctions_4c_watch | Reuters / AP China sanctions anchors | China sanctions hit shipbuilding geopolitics before order execution clarity | reported_event_anchor_not_full_ohlc |
| r11_loop14_martial_law_political_liquidity_shock | Reuters / FT martial-law market-stabilization anchors | Political shock repriced KOSPI/won before any company evidence | reported_index_fx_anchor_not_full_ohlc |
| r11_loop14_tax_policy_market_confidence_4c | MarketWatch / Reuters / Barron's tax-policy anchors | Tax policy can break Value-Up and AI rerating confidence even when later clarified | reported_market_anchor_not_full_ohlc |
| r11_loop14_short_selling_market_access_reform_stage2 | Reuters MSCI accessibility and unfair-trading reform anchors | Market access reform is Stage 2 until foreign flow and brokerage earnings confirm | policy_anchor_not_full_ohlc |
| r11_loop14_medical_reform_doctors_strike_service_disruption | Reuters / Guardian doctors strike anchors | Policy objective cannot become investable Green while hospital operations are disrupted | service_disruption_reference_not_full_ohlc |
| r11_loop14_2025_wildfire_disaster_recovery_reference | Reuters / AP wildfire-disaster anchors | Disaster recovery theme requires claims, government budget, actual contracts and margin | disaster_reference_not_full_ohlc |
| r11_loop14_hanwha_aerospace_romania_k9_geopolitical_order | Reuters Romania K9 order and later dilution-watch anchors | Defense order is Stage 2 until delivery, margin, cash collection and dilution-adjusted EPS confirm | reported_event_anchor_not_full_ohlc |
| r11_loop14_samsung_strike_labor_policy_systemic_export_risk | Reuters Samsung strike / government emergency arbitration anchor | Samsung labor dispute is national export-chain risk until production continuity clears | labor_policy_anchor_not_full_ohlc |
