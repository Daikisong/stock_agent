# Round 275 R6 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, CET1, RBC, ROE, NIM, credit cost, RWA, exchange trust, fee revenue or regulatory clearance where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_price_anchor
- reported_return_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- bank_quality_anchor
- capital_return_anchor
- digital_asset_trust_gate
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r6_loop13_financial_holdings_valueup_sector_4b | Reuters / analyst round value-up and KOSPI 7000 reported anchors | Foreign net purchase 3.1T KRW; bank-quality metrics not verified | reported_sector_anchor_not_full_ohlc |
| r6_loop13_sk_square_holdco_discount_buyback | Analyst round SK Square holdco-discount reported anchors | Buyback/cancellation 200B KRW; full adjusted OHLC unavailable | reported_NAV_anchor_not_full_ohlc |
| r6_loop13_samsung_life_samsung_electronics_stake_regulatory_gate | Analyst round Samsung Life regulatory stake-sale anchors | Book value about 0.5x; insurance earnings bridge not confirmed | price_data_unavailable_after_deep_search |
| r6_loop13_hana_bank_dunamu_digital_asset_stake | Analyst round Hana/Dunamu transaction anchors | Implied Dunamu equity 15.31T KRW; regulatory bridge not confirmed | price_data_unavailable_after_deep_search |
| r6_loop13_naver_dunamu_fintech_ma_trust_gate | Reuters transaction and event-return anchors | Event swing -11.2pp after abnormal withdrawal; Upbit to cover using own assets | reported_event_anchor_not_full_ohlc |
| r6_loop13_kbank_internet_bank_ipo_overhang | Analyst round K Bank IPO anchors | Raise max 984B KRW; no listed price path before listing | unlisted_pre_IPO_no_ohlc |
| r6_loop13_stablecoin_policy_overheat_fx_gate | Analyst round stablecoin basket reported anchors | Won weakness quarter 4%; issuer/license/reserve/fee not confirmed | reported_return_anchor_not_full_ohlc |
| r6_loop13_bithumb_operational_error_hard_reference | Analyst round Bithumb operational-error reported anchors | Bithumb BTC -17% on exchange; regulator inspection | unlisted_hard_reference_reported_anchor |
