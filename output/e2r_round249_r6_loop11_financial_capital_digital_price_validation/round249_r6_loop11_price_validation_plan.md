# Round 249 R6 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, CET1, K-ICS, credit cost, equity-method income, stablecoin revenue, MFE, or MAE where raw adjusted daily prices or filings are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- transaction_value_anchor
- policy_or_regulatory_anchor
- capital_or_trust_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r6_loop11_big4_financial_valueup_stage2 | Reuters Commercial Act / KOSPI 7000 sector-return anchors | Newly acquired treasury shares must be cancelled within 1 year; existing shares 6-month grace period | reported_sector_anchor_not_full_ohlc |
| r6_loop11_securities_capital_market_boom | Reuters sector-return anchor | Securities relative outperformance vs KOSPI +7.05pp | reported_sector_return_not_full_ohlc |
| r6_loop11_sk_square_nav_discount_valueup | Reuters buyback / NAV-discount anchor | SK Square market value less than half of $18B SK Hynix stake value | price_data_unavailable_after_deep_search |
| r6_loop11_samsung_life_nav_capital_release | Reuters regulatory share-sale anchor | Purpose: resolve local financial-company governance regulation risk | price_data_unavailable_after_deep_search |
| r6_loop11_hana_dunamu_equity_option | Reuters / WSJ transaction anchor | Implied Dunamu equity value about 15.27T won; Upbit share >80% | price_data_unavailable_after_deep_search |
| r6_loop11_naver_dunamu_platform_merger_trust_watch | Reuters transaction / event-return anchor | 15.13T won all-stock deal; 2.54 NAVER Financial shares per Dunamu share | reported_event_return_not_full_ohlc |
| r6_loop11_internet_bank_kbank_kakaobank_watch | Reuters IPO / legal-governance anchors | K Bank IPO up to 984B won; valuation up to about 5T won; H1 OP 86.7B won | kbank_unlisted_kakaobank_ohlc_unavailable |
| r6_loop11_stablecoin_policy_theme_overheat | FT reported return and policy-risk anchors | Margin loan 20.5T won; proposed minimum equity for issuers 500M won | reported_return_anchor_not_full_ohlc |
