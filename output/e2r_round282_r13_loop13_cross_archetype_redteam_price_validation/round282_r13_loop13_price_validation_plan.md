# Round 282 R13 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, stage prices, full MFE/MAE, call-off, custody control, IPO aftermarket demand, EPC margin, or parent ROI where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- deal_value_anchor
- IPO_price_anchor
- fine_anchor
- revenue_cut_anchor
- market_cap_wipeout_anchor
- contract_collapse_value_anchor
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
| r13_loop13_skt_cybersecurity_hard_4c | Reuters event-return anchors | Revenue forecast cut, compensation cost, data-protection investment and fine validate hard 4C. | reported_event_anchor_not_full_ohlc |
| r13_loop13_jeju_air_safety_hard_4c | Reuters event-price anchor | Fatal crash validates hard safety gate before demand or route scoring. | reported_event_anchor_not_full_ohlc |
| r13_loop13_lnf_tesla_contract_collapse | Reuters contract-collapse value anchor | Contract headline collapsed before Stage 3 revenue validation. | contract_value_anchor_not_full_ohlc |
| r13_loop13_naver_dunamu_upbit_trust_4c_watch | Reuters M&A and abnormal-withdrawal event anchors | M&A price move reversed when digital-asset custody trust entered RedTeam. | reported_event_anchor_not_full_ohlc |
| r13_loop13_lg_cns_ipo_quality_false_positive | IPO debut price anchors | Weak aftermarket demand capped the AI/cloud IPO story. | reported_ipo_anchor_not_full_ohlc |
| r13_loop13_korea_zinc_control_premium_dilution_4b | Reuters / WSJ tender and issuance anchors | Control premium produced 4B-watch before dilution/accounting review risk. | reported_event_anchor_not_full_ohlc |
| r13_loop13_samsung_ea_fadhili_order_not_margin_green | Reuters order event and analyst target anchors | Order headline is Stage 2 valid, but Green needs EPC margin and cash conversion. | reported_event_anchor_not_full_ohlc |
| r13_loop13_hyundai_motor_india_ipo_failed_rerating | Reuters IPO debut anchors | Large subsidiary IPO did not validate parent rerating without aftermarket demand. | reported_ipo_anchor_not_full_ohlc |
