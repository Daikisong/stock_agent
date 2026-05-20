# Round 281 R12 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- direct_listed_hard_4c_confirmed: false
- Do not invent OHLC, stage prices, pass-through, utilization, trust recovery, enrolment, order backlog, IPO aftermarket demand, or FCF where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- input_cost_anchor
- policy_or_demographic_anchor
- service_trust_anchor
- business_metric_anchor
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
| r12_loop13_kimchi_cabbage_climate_food_input_cost | Reuters cabbage-climate input-cost anchor | Food input-cost shock; company-level OHLC unavailable | price_data_unavailable_after_deep_search |
| r12_loop13_feed_wheat_tender_livestock_cost_watch | Reuters feed-wheat tender anchor | Feed input-cost pressure; company-level OHLC unavailable | price_data_unavailable_after_deep_search |
| r12_loop13_poultry_egg_birdflu_supply_shock | Reuters bird-flu chicken/egg price and import-policy anchors | Two-sided disease/tariff case; company-level OHLC unavailable | price_data_unavailable_after_deep_search |
| r12_loop13_daedong_tym_agri_machinery_labor_substitution | company-profile / listed-business anchor; no reliable event OHLC located | Agri automation optionality only | price_data_unavailable_after_deep_search |
| r12_loop13_cj_logistics_shinsegae_alliance_unit_economics | MarketWatch / Dow Jones CJ Logistics alliance anchor | Good contract but price failed | reported_event_anchor_not_full_ohlc |
| r12_loop13_coupang_life_service_trust_break_reference | Reuters Coupang data-breach and competitor read-through anchor | Life-service trust hard reference; competitor read-through is not automatic Green | reported_event_anchor_not_full_ohlc |
| r12_loop13_waste_recycling_food_waste_rfid_platform | Reuters EQT waste-platform anchor + Guardian food-waste RFID policy anchor | Structural policy infra Stage 2; listed OHLC unavailable | price_data_unavailable_after_deep_search |
| r12_loop13_birthrate_rebound_childcare_education_event | Reuters / Guardian birthrate rebound anchors | Demographic Stage 2, not company Green | price_data_unavailable_after_deep_search |
| r12_loop13_dn_solutions_other_manufacturing_tools_ipo | Reuters DN Solutions IPO anchor + company-profile Heller acquisition reference | IPO quality gate; post-listing OHLC unavailable | price_data_unavailable_after_deep_search |
