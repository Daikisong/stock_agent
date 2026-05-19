# Round-207 R3 Loop-8 Price Validation Plan

## Required Fields

- `price_data_source`
- `full_ohlc_available`
- `reported_price_anchor`
- `reported_return_anchor`
- `stage2_price`
- `stage3_price`
- `stage4b_price`
- `stage4c_price`
- `peak_price`
- `mfe_1d`
- `mae_1d`
- `mae_1d_secondary`
- `contract_value_drawdown_pct`
- `lost_revenue_vs_prior_revenue_pct`
- `net_debt_increase_pct`
- `loss_worsening_pct`
- `price_validation_status`

## Case Anchors

| case | price data source | reported anchor | status |
| --- | --- | --- | --- |
| `r3_loop8_lges_ess_pivot_contract_break` | Reuters reported event returns and contract anchors | -1.6% after Q2 demand warning; -7.6% intraday after Ford cancellation | `reported_event_anchor_not_full_ohlc` |
| `r3_loop8_lnf_tesla_contract_collapse` | Reuters contract value anchor | $2.9B expected contract value cut to $7,386 | `contract_value_anchor_stock_ohlc_unavailable` |
| `r3_loop8_samsung_sdi_ess_lfp_stage2` | Reuters event returns and offering-price anchor | +6.1% ESS contract intraday; offering price -13.6%; YTD -29.5% | `reported_event_anchor_not_full_ohlc` |
| `r3_loop8_sk_innovation_skon_failed_rerating` | FT debt/loss anchor and Reuters merger return anchor | +5% merger approval intraday; net debt +437.9% | `reported_event_anchor_not_full_ohlc` |
| `r3_loop8_skiet_separator_demand_break` | Reuters business event anchor | SK On Q1 loss widened from 18.6bn KRW to 332.0bn KRW | `price_data_unavailable_after_deep_search` |
| `r3_loop8_posco_future_m_lithium_event` | WSJ/Reuters event return anchors | +8.3% CATL lithium event; -8.2% Ford EV retreat shock | `reported_event_anchor_not_full_ohlc` |
| `r3_loop8_ecopro_materials_precursor_overheat` | MarketWatch reported price anchor | -11% to 119,200 KRW; about -5% Ford supply-chain event | `reported_event_anchor_not_full_ohlc` |

## Backfill Rule

- Use reported Reuters/WSJ/FT/MarketWatch anchors only for fields they explicitly support.
- Keep full OHLC unavailable until official or adjusted daily price backfill is done.
- Separate Stage 2 ESS/contract evidence, Green-required operating proof, 4B event premium, and 4C contract-quality breaks.
- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.
