# Round 288 R6 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, full MFE/MAE, capital-return execution, credit quality, custody controls, AML/KYC clearance, ROIC, revenue contribution, or stage prices where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- reported_event_price_anchor
- deal_value_anchor
- buyback_amount_anchor
- ipo_range_anchor
- cb_value_anchor
- stake_percent_anchor
- regulatory_restriction_anchor
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
| r6_loop14_financial_holding_value_up_policy_stage2 | Reuters/FT Commercial Act and Value-Up reform anchors | Treasury-share cancellation law anchor; KOSPI crossed 6000 in reform rally context | price_data_unavailable_after_deep_search |
| r6_loop14_sk_square_holdco_discount_buyback | Reuters SK Square buyback / activist / holdco discount anchor | 200B KRW cancellation-related plan; 20% SK Hynix stake value context | price_data_unavailable_after_deep_search |
| r6_loop14_samsung_ct_activist_valueup_failure | FT activist proposal / share-price failure anchor | Activist proposal failed; NPS sided with management | reported_event_anchor_not_full_ohlc |
| r6_loop14_kbank_digital_bank_ipo_quality_gate | Reuters K Bank IPO plan anchor | Raise up to 984B KRW; valuation up to 5T KRW; H1 OP 86.7B KRW; 10M+ customers | unlisted_ipo_plan_no_aftermarket_ohlc |
| r6_loop14_kakaobank_control_risk_kakao_founder | Reuters Kakao founder arrest / KakaoBank control-risk anchors | Bank ownership above 10% could be restricted if financial-crime conviction occurred; later acquittal was relief | reported_event_anchor_not_full_ohlc |
| r6_loop14_naver_financial_dunamu_upbit_trust_gate | Reuters Naver Financial-Dunamu deal and Upbit abnormal withdrawal anchor | 15.13T KRW deal; 54B KRW abnormal withdrawal turned the same-day trust gate negative | reported_event_anchor_not_full_ohlc |
| r6_loop14_hana_bank_dunamu_digital_asset_stake | Reuters Hana Bank-Dunamu stake acquisition anchor | 1T KRW stake; 6.55%; implied Dunamu value 15.27T KRW; Upbit volume share context >80% | price_data_unavailable_after_deep_search |
| r6_loop14_samsung_sds_kkr_cb_stablecoin_event | Reuters KKR convertible-bond and Samsung SDS share reaction anchor | $820M CB and AI/stablecoin/M&A use-of-funds headline moved shares before ROIC proof | reported_event_anchor_not_full_ohlc |
