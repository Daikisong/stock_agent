# Round 235 R5 Price Validation Plan

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
- peak_price
- mfe_1d
- mae_1d
- target_upside_pct
- reported_mfe_since_debut_pct
- reported_mfe_since_january_pct
- relative_growth_vs_us_market_multiple
- visitor_target_growth_pct
- ff_investment_vs_possible_value_pct
- overseas_sales_mix
- opm_estimate
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r5_loop10_samyang_buldak_export_regulatory_watch | MarketWatch/AP/Reuters reported anchors | +5.7% event-day return; target upside +28.3%; Denmark recall/reversal watch | reported_price_anchor_not_full_ohlc |
| r5_loop10_nongshim_shin_global_staple | FT business evidence | Shin 2023 sales $883M, overseas nearly 60%, North America $538M, U.S. target $1.5B by 2030 | price_data_unavailable_after_deep_search |
| r5_loop10_apr_medicube_structural_4b | Vogue Business/FT revenue and market-value anchors | Q4 revenue +124%; overseas +203%; reported MFE since January >+300% | reported_revenue_marketcap_anchor_not_full_ohlc |
| r5_loop10_indie_kbeauty_odm_distribution_watch | Reuters business and reported return anchors | d'Alba shares more than doubled since debut; top5 Korean cosmetics U.S. e-commerce +71% | reported_return_anchor_not_full_ohlc |
| r5_loop10_cj_olive_young_retail_platform | Business Insider/Reuters platform evidence | U.S. K-beauty market $2B, +37%; Olive Young 1,300+ Korea stores and U.S. 2026 plan | price_data_unavailable_after_deep_search |
| r5_loop10_amorepacific_legacy_china_exposure | Vogue AmorePacific context + Reuters global beauty China-demand evidence | L'Oreal Q3 like-for-like +3.4% vs expected +6%; North Asia -6.5%; L'Oreal share decline since June about -20% | price_data_unavailable_after_deep_search |
| r5_loop10_tourism_retail_china_visa_event | Reuters event return and tourism metric anchors | Hyundai Department +7.1%; Hotel Shilla +4.8%; Paradise +2.9%; Hankook Cosmetics +9.9%; visitor target +12.8% | reported_event_anchor_not_full_ohlc |
| r5_loop10_fnf_taylormade_mna_optionality | Reuters deal evidence anchor | TaylorMade possible value $3.5B; F&F 2021 subordinated equity investment 358B KRW | price_data_unavailable_after_deep_search |
