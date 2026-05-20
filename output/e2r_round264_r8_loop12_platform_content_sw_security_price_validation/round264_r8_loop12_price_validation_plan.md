# Round 264 R8 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- hard_4c_confirmed: true
- Do not invent OHLC, peak, MFE, MAE, stage prices, retention, ARPU, take-rate, OPM, FCF, security costs, or compensation liabilities.

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
- transaction_or_ipo_anchor
- revenue_margin_or_user_anchor
- trust_security_or_governance_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r8_loop12_shift_up_game_ip_ipo_single_title_watch | Reuters IPO / sales / earnings anchors | Valuation/revenue 20.7x and valuation/OP 31.5x before repeat-title proof | price_data_unavailable_after_deep_search |
| r8_loop12_pinkfong_kids_content_ip_ipo_event | FT IPO price and financial anchors | Content IPO event premium before repeat-hit and licensing/merchandise proof | reported_event_anchor_not_full_ohlc |
| r8_loop12_sm_tencent_kpop_china_optionality | Reuters SM / Tencent transaction anchor | Implied SM equity value about 2.51T won before actual China ticket revenue | price_data_unavailable_after_deep_search |
| r8_loop12_naver_dunamu_platform_merger_trust_gate | Reuters deal / event return / trust-risk anchors | Deal premium reversed around exchange trust incident; event swing -11.2pp | reported_event_anchor_not_full_ohlc |
| r8_loop12_coupang_platform_data_breach_reference | IBD / Barron's breach and event-return anchors | 33.7M accounts affected; retained data later reported around 3,000 customers | reported_event_anchor_not_full_ohlc_non_KRX |
| r8_loop12_krafton_unknown_worlds_subnautica_governance_watch | Reuters legal ruling / acquisition / earnout anchors | $500M acquisition and $250M earnout dispute anchor governance 4C-watch | price_data_unavailable_after_deep_search |
| r8_loop12_skt_cybersecurity_operational_trust_hard_4c | Reuters breach / July investigation / compensation anchors | Revenue guide cut 800B won, customer benefit package 500B won, possible all-victim compensation nearly 2.3T won | reported_event_anchor_not_full_ohlc |
