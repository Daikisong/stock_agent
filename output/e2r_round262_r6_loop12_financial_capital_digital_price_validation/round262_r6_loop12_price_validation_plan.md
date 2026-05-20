# Round 262 R6 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, ROE, CET1, K-ICS, credit cost, digital revenue, FX stability, or trust resolution where raw data are unavailable.

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
- relative_performance_vs_kospi
- capital_return_or_ratio_anchor
- digital_revenue_or_equity_anchor
- trust_privacy_or_fx_gate
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r6_loop12_financial_holdings_valueup_stage2 | Reuters Commercial Act / KOSPI 7000 event-return anchors | Relative performance vs KOSPI -2.25pp on KOSPI 7000 context | reported_sector_anchor_not_full_ohlc |
| r6_loop12_securities_market_volume_cycle | Reuters KOSPI 7000 sector-return anchor | Securities relative outperformance vs KOSPI +7.05pp | reported_sector_anchor_not_full_ohlc |
| r6_loop12_samsung_life_nav_capital_release | Reuters regulatory share-sale anchor | Capital release Stage 2; full Samsung Life OHLC unavailable | price_data_unavailable_after_deep_search |
| r6_loop12_hana_bank_dunamu_equity_option | Reuters / WSJ transaction anchors | Implied Dunamu equity value about 15.27T KRW; full Hana price path unavailable | price_data_unavailable_after_deep_search |
| r6_loop12_naver_dunamu_platform_merger_trust_watch | Reuters transaction / event-return / trust-risk anchor | Event swing -11.2pp after 54B KRW abnormal withdrawal; Upbit to cover using own assets | reported_event_anchor_not_full_ohlc |
| r6_loop12_toss_facepay_fintech_superapp_privacy_watch | Reuters global expansion / FT FacePay anchors | User target requires +108.3%; merchant target requires +203.0%; no listed OHLC | unlisted_no_ohlc |
| r6_loop12_kakao_kakaobank_governance_gate | Reuters Kakao founder arrest / bank ownership-risk anchors | Conviction risk could affect KakaoBank control due bank ownership restrictions | kakaobank_ohlc_unavailable_after_deep_search |
| r6_loop12_stablecoin_policy_overheat_fx_gate | FT stablecoin / kimchi-bond / FX-risk anchors | Q1 stablecoin trading 57T KRW / $42B and capital outflow context >$19B | reported_return_anchor_not_full_ohlc |
