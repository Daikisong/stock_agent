# Round 251 R8 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- hard_4c_confirmed: true
- Do not invent OHLC, peak, MFE, MAE, stage prices, ARR, paid usage, bookings, OPM, FCF, security costs, or fines.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_event_return
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- relative_underperformance_pp
- transaction_or_capital_anchor
- revenue_or_margin_anchor
- user_or_booking_anchor
- security_or_legal_risk_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r8_loop11_douzone_bizon_eqt_saas | Reuters transaction evidence | EQT $930M for 37.6%, implied equity value about $2.473B | price_data_unavailable_after_deep_search |
| r8_loop11_samsung_sds_kkr_ai_4b | Reuters reported event return anchor | Relative intraday outperformance +17.8pp before recurring AI revenue confirmation | reported_event_anchor_not_full_ohlc |
| r8_loop11_lg_cns_ai_cloud_ipo_price_failed | Reuters IPO price anchor | Debut MAE -3.55% despite cloud/AI services at 54% of sales | reported_price_anchor_not_full_ohlc |
| r8_loop11_naver_webtoon_ip_platform | Reuters / Barron's price and earnings anchors | IPO debut +14.3%, Disney/earnings event +62%, but pre-event post-IPO drawdown -55% | reported_price_anchor_not_full_ohlc |
| r8_loop11_kakao_openai_partnership_price_only | Reuters event return anchor | Two-session cumulative +6.8%, with -11pp fade from peak | reported_event_anchor_not_full_ohlc |
| r8_loop11_krafton_game_ip_india_adk_watch | Reuters India fund and ADK acquisition anchors | ADK $516M and India fund $666M provide business anchors, not stage3 price path | price_data_unavailable_after_deep_search |
| r8_loop11_skt_cybersecurity_operational_trust_hard_4c | Reuters breach / price / fine / revenue-cut anchors | Revenue cut 800B won, customer benefit package 500B won, PIPC fine 134B won | reported_event_anchor_not_full_ohlc |
| r8_loop11_hybe_founder_legal_governance_watch | Reuters / AP legal event anchors | Relative underperformance -5.1pp; warrant later declined so hard 4C remains unconfirmed | reported_event_anchor_not_full_ohlc |
