# Round 295 R13 Price Validation Plan

- price_validation_completed: partial_with_reported_event_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent adjusted OHLC, stage prices, contract call-off, IRR, post-IPO validation, governance execution, drilling economics, or operating cashflow where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- contract_value_collapse_anchor
- share_sale_dilution_anchor
- resource_economic_viability_anchor
- IPO_aftermarket_anchor
- valueup_execution_anchor
- data_trust_liability_anchor
- localization_capex_IRR_anchor
- control_premium_separation_anchor
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
| r13_loop14_hanwha_aerospace_backlog_dilution_4b | FT / Reuters share-sale and FSS filing-revision anchors | shares -13% after share-sale plan; YTD pre-event gain more than double | reported_event_anchor_not_full_ohlc |
| r13_loop14_lnf_tesla_signed_contract_collapse_hard_4c | Reuters L&F/Tesla contract-value collapse anchor | contract value collapse -99.9997% | reported_contract_collapse_anchor_not_full_ohlc |
| r13_loop14_kogas_blue_whale_resource_event_premium | Reuters / WSJ resource-discovery event anchors | KOGAS +30%, Daesung +30%, SK Innovation +6%, SK Gas +7% | reported_event_anchor_not_full_ohlc |
| r13_loop14_lg_cns_ai_cloud_ipo_false_positive | Reuters LG CNS IPO/debut anchor | morning trade -3.55% vs IPO price | reported_IPO_aftermarket_anchor_not_full_ohlc |
| r13_loop14_samsung_ct_valueup_proposal_failure | FT activist proposal failure anchor | Samsung C&T almost -10% after proposal failure | reported_event_anchor_not_full_ohlc |
| r13_loop14_skt_data_trust_hard_4c | Reuters SK Telecom breach, government investigation and compensation anchors | revenue forecast cut 800B KRW; possible compensation 2.3T KRW | reported_hard_4c_anchor_not_full_ohlc |
| r13_loop14_hyundai_steel_us_localization_capex_false_positive | Reuters Hyundai Steel U.S. plant investor-backlash anchor | Hyundai Steel -21.2%, POSCO -18.3%, KOSPI -5.5% | reported_event_anchor_not_full_ohlc |
| r13_loop14_korea_zinc_control_premium_4b | Reuters Korea Zinc tender-offer anchor | Korea Zinc +19.8%, Young Poong +30% | reported_event_anchor_not_full_ohlc |
