# Round 248 R5 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, sell-through, GMV, margin, inventory, receivables, MFE, or MAE where raw adjusted daily prices are unavailable.

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
- revenue_or_sales_anchor
- channel_or_user_anchor
- trust_or_policy_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r5_loop11_samyang_buldak_export_packaging_watch | MarketWatch / Reuters reported anchors | target price 830,000 KRW, Q2 OP estimate 81.2B KRW and +84% YoY | reported_price_anchor_not_full_ohlc |
| r5_loop11_nongshim_shin_global_staple | FT business evidence | Shin Ramyun 2023 sales 1.2T KRW / $883M, overseas nearly 60%, North America +10% | price_data_unavailable_after_deep_search |
| r5_loop11_apr_medicube_structural_4b | Business Insider / Vogue Business anchors | Q4 2025 revenue $440M +124%, overseas $362M +203%, Medicube FY revenue $1.1B | reported_price_and_revenue_anchor_not_full_ohlc |
| r5_loop11_indie_kbeauty_odm_distribution_watch | Reuters business and reported return anchors | top-five K-beauty U.S. e-commerce brands +71% over two years vs U.S. market +21% | reported_return_anchor_not_full_ohlc |
| r5_loop11_amore_lghh_legacy_china_exposure | FT / Vogue / Reuters legacy-China beauty context | legacy China/travel retail risk while new K-beauty winners outperform | price_data_unavailable_after_deep_search |
| r5_loop11_emart_shinsegae_alibaba_jv_data_gate | WSJ / Reuters JV and regulatory anchors | JV share 41%, Gmarket 50M customer data, China online imports 4.7T KRW +32% | reported_event_anchor_not_full_ohlc |
| r5_loop11_coupang_breach_ecommerce_trust_reference | Reuters e-commerce breach / competitor anchor | 34M users affected, activity -3.5%, spending -6.3% | reported_event_anchor_not_full_ohlc |
| r5_loop11_tourism_retail_china_visa_event | Reuters event return and tourism policy anchors | Chinese groups of 3+ can stay 15 days visa-free from 2025-09-29 through 2026-06 | reported_event_anchor_not_full_ohlc |
