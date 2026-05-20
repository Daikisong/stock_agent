# Round 290 R8 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, paid conversion, ARR, retention, creator economics, recurring revenue, governance clearance, security remediation, margin, or FCF where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_event_price_anchor
- ipo_price_anchor
- deal_value_anchor
- revenue_op_anchor
- mau_anchor
- data_breach_cost_anchor
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r8_loop14_naver_webtoon_ipo_aftermarket_gate | Reuters / MarketWatch / Barron's / WSJ event anchors | WBTN +14.3% debut, later -55%, +62% rebound, then -15% after-hours on weak guide | reported_event_anchors_not_full_ohlc |
| r8_loop14_kakao_platform_governance_sm_case | Reuters Kakao founder arrest and prosecution anchors | Kakao -3.4% on founder arrest; YTD -24% context | reported_event_anchor_not_full_ohlc |
| r8_loop14_hybe_ador_newjeans_ip_governance | Reuters HYBE/ADOR audit and share reaction anchor | HYBE shares nearly -8% on ADOR/NewJeans dispute | reported_event_anchor_not_full_ohlc |
| r8_loop14_shift_up_game_ip_ipo_quality_gate | Reuters Shift Up IPO and game-IP anchor | IPO raise/value and game sales anchors; full post-IPO OHLC unavailable | price_data_unavailable_after_deep_search |
| r8_loop14_ncsoft_earnings_buyback_turnaround | WSJ NCSoft Q1 earnings beat / buyback event anchor | Shares up to +14% on earnings beat and buyback | reported_event_anchor_not_full_ohlc |
| r8_loop14_lg_cns_ai_cloud_ipo_false_positive | Reuters LG CNS IPO/debut anchor | IPO price 61,900 KRW; morning trading 59,700 KRW, -3.23% vs IPO | reported_ipo_anchor_not_full_ohlc |
| r8_loop14_douzone_bizon_eqt_enterprise_sw_stage2 | Reuters EQT-Douzone Bizon stake anchor | Direct event return unavailable; $930M for 37.6% stake used as control-premium anchor | price_data_unavailable_after_deep_search |
| r8_loop14_sk_telecom_cybersecurity_trust_hard_4c | Reuters SK Telecom data-breach event, investigation and fine anchors | Shares -8.5% intraday and -6.7% close; later -5.6% on leak validation | reported_event_anchor_not_full_ohlc |
