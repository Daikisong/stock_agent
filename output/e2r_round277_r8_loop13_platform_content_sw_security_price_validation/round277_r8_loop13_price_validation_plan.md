# Round 277 R8 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, paid conversion, ARPU, take-rate, creator economics, recurring revenue, governance clearance, cybersecurity remediation, margin or FCF where raw data are unavailable.

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
- platform_monetization_anchor
- governance_or_legal_anchor
- cybersecurity_trust_cost_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r8_loop13_naver_line_yahoo_data_sovereignty_watch | Reuters data leak / SoftBank talks / LY buyback anchors | Data-sovereignty relief, not Green; NAVER OHLC unavailable | naver_ohlc_unavailable_after_deep_search |
| r8_loop13_naver_webtoon_entertainment_ipo | Reuters / FT Webtoon IPO anchors | Debut high $24, +14.3%; NAVER parent value bridge unconfirmed | reported_ipo_anchor_not_full_ohlc |
| r8_loop13_kakao_sm_founder_legal_governance | Reuters Kakao arrest/acquittal anchors | Kakao shares -3.4% on founder arrest | reported_event_anchor_not_full_ohlc |
| r8_loop13_hybe_ador_bang_legal_ip_governance | Reuters / AP HYBE governance and legal-risk anchors | HYBE nearly -8% on ADOR dispute; -2.4% on warrant request | reported_event_anchor_not_full_ohlc |
| r8_loop13_shiftup_game_ip_ipo_overheat | Reuters Shift Up IPO anchor | Full OHLC unavailable; single-IP durability unconfirmed | price_data_unavailable_after_deep_search |
| r8_loop13_lg_cns_ai_cloud_ipo_quality_gate | Reuters LG CNS IPO and debut anchors | Debut price below IPO price, -3.23% | reported_ipo_anchor_not_full_ohlc |
| r8_loop13_krafton_india_game_platform_option | Reuters / FT Krafton India platform anchors | ARPU, paid conversion, regulatory clearance and second-hit proof required | price_data_unavailable_after_deep_search |
| r8_loop13_skt_data_breach_cybersecurity_hard_4c | Reuters SK Telecom breach / investigation / fine / compensation anchors | Shares -8.5% intraday and -6.7% close after breach; later -5.6% on leak validation | reported_event_anchor_not_full_ohlc |
