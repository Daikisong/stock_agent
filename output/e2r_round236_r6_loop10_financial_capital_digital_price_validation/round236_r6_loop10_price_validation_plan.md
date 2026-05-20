# Round 236 R6 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, peak, MFE, MAE, stage prices, or business metrics where source anchors are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- event_swing_pp
- discount_to_nav_or_book
- transaction_value
- implied_equity_value
- reported_theme_basket_return
- regulated_revenue_confirmed
- issuer_license_confirmed
- reserve_income_confirmed
- exchange_trust_incident
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r6_loop10_bank_valueup_big4_kb_watch | public company profile + Reuters sector rally anchor | KB 2025 net profit 5.84T KRW, +15.1%; Big4 nearly 18T KRW; financial groups +4.2% on KOSPI 7,000 event | reported_sector_anchor_not_full_ohlc |
| r6_loop10_securities_capital_market_boom | Reuters sector return anchor | KOSPI +6.45%, securities +13.5%, financial groups +4.2%, foreign net purchase 3.1T KRW | reported_sector_return_not_full_ohlc |
| r6_loop10_sk_square_nav_discount_valueup | Reuters buyback / NAV-discount anchor | 200B KRW buyback/cancel programme; SK Hynix stake 20%; minimum NAV discount >50% | price_data_unavailable_after_deep_search |
| r6_loop10_samsung_life_nav_capital_release | Reuters regulatory share-sale anchor | Samsung Electronics stake sale 1.3T KRW / $867.07M; governance-regulation risk resolution purpose | price_data_unavailable_after_deep_search |
| r6_loop10_hana_dunamu_equity_option | Reuters transaction anchor | 1.0T KRW for 6.55% stake; implied Dunamu equity value about 15.27T KRW; Upbit trading volume share >80% | price_data_unavailable_after_deep_search |
| r6_loop10_naver_dunamu_platform_merger_trust_watch | Reuters transaction / event-return anchor | initially >+7%, then -4.2% after Upbit abnormal withdrawal; deal value 15.13T KRW | reported_event_return_not_full_ohlc |
| r6_loop10_internet_bank_kbank_kakaobank_watch | Reuters IPO / legal-governance anchors | K Bank IPO max 984B KRW; Kakao -3.4%, YTD -24%; bank ownership cap risk if convicted | kbank_unlisted_kakaobank_ohlc_unavailable |
| r6_loop10_stablecoin_policy_theme_overheat | FT reported return and policy-risk anchors | Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x before regulated revenue clarity | reported_return_anchor_not_full_ohlc |
