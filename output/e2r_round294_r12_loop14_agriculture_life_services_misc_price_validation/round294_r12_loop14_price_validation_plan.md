# Round 294 R12 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- direct_KRX_hard_4c_confirmed: false
- sector_hard_reference_confirmed: true
- Do not invent OHLC, stage prices, pass-through, same-store sales, take-rate, recycling yield, customer count, retention, or FCF where raw data are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_event_return_anchor
- food_input_cost_anchor
- farm_equipment_cycle_anchor
- delivery_deal_anchor
- labor_service_anchor
- waste_infra_anchor
- demographic_anchor
- education_demand_anchor
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
| r12_loop14_daedong_tym_agri_equipment_export_cycle | Reuters CNH / Barron's AGCO-Deere global farm-equipment anchors | Global farm-equipment cycle gate; Daedong/TYM direct OHLC unavailable | reported_event_anchor_not_full_ohlc |
| r12_loop14_food_input_cost_inflation_basket | Reuters Korea inflation / food-cost anchor | Food input-cost shock; company-level OHLC unavailable | price_data_unavailable_after_deep_search |
| r12_loop14_fried_chicken_jensen_huang_meme_rally | MarketWatch / FT Jensen Huang fried-chicken rally anchors | Meme event moved listed peers without direct economics | reported_event_anchor_not_full_ohlc |
| r12_loop14_naver_uber_baemin_food_delivery_consolidation | Reuters Delivery Hero Korea recovery and Uber/Naver Baemin bid anchors | Consolidation Stage 2; Naver direct event return unavailable | reported_event_anchor_not_full_ohlc |
| r12_loop14_delivery_labor_service_continuity_reference | Reuters delivery-worker election pause anchor | Delivery labor continuity reference; direct listed OHLC unavailable | price_data_unavailable_after_deep_search |
| r12_loop14_waste_recycling_infra_stage2 | Reuters EQT KJ Environment acquisition and South Korea plastic-waste anchors | Waste infra Stage 2 plus recycling yield and cleanup liability gate | price_data_unavailable_after_deep_search |
| r12_loop14_birthrate_childcare_infant_goods_stage2 | Reuters birthrate rebound anchors | Demographic Stage 2, not automatic childcare revenue Green | price_data_unavailable_after_deep_search |
| r12_loop14_private_education_hagwon_demand_stage2 | FT under-6 hagwon survey anchor | Education-service demand Stage 2 plus social/policy 4C watch | price_data_unavailable_after_deep_search |
