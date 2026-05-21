# Round 331 R10 Loop 17 Price Validation Plan

Full adjusted OHLC is not complete. Reported event anchors are retained, but MFE/MAE, peak and drawdown are not invented.

| case_id | status | event anchor | next backfill |
| --- | --- | --- | --- |
| r10_loop17_samsung_ena_fadhili_epc | price_data_unavailable_after_deep_search | {"capacity_bcf_per_day": 4, "completion_target": "2027-11", "contract_value_usd_bn": 6.0, "event_price_krw": 26750, "event_return_pct": 8.5, "gas_capacity_increase_pct": 60, "kospi_return_pct": -1.4, "market_relative_return_pp": 9.9, "total_project_value_usd_bn": 7.7, "trigger_date": "2024-04-03"} | adjusted OHLC backfill required |
| r10_loop17_czech_nuclear_epc | price_data_unavailable_after_deep_search | {"doosan_3m_return_pct": 48, "kepco_ec_3m_return_pct": 41, "kepco_plant_event_return_pct": 14, "legal_window": "2024-10_to_2025", "trigger_date": "2024-07-17", "unit_cost_czk_bn": 200, "unit_cost_usd_bn": 8.65} | adjusted OHLC backfill required |
| r10_loop17_seoul_housing_supply_reconstruction | price_data_unavailable_after_deep_search | {"direct_builder_price_anchor": "unavailable", "housing_supply_target_units": 400000, "ltv_after_pct": 40, "ltv_before_pct": 50, "seoul_home_price_weekly_pct": 0.76, "trigger_date": "2024-08_to_2025-09"} | adjusted OHLC backfill required |
| r10_loop17_real_estate_pf_restructuring | price_data_unavailable_after_deep_search | {"pf_delinquency_2022_pct": 0.37, "pf_delinquency_2023_pct": 1.19, "pf_delinquency_2024_pct": 2.7, "support_package_krw_trn": 40.6, "syndicated_loan_after_krw_trn": 5, "syndicated_loan_before_krw_trn": 1} | adjusted OHLC backfill required |
| r10_loop17_samsung_ct_valueup_failed | price_data_unavailable_after_deep_search | {"NPS_vote": "management", "activist_proposal": "failed", "event_return_label": "almost_-10", "trigger_date": "2024-03-15"} | adjusted OHLC backfill required |
| r10_loop17_highway_construction_collapse_safety | price_data_unavailable_after_deep_search | {"critical_injuries": "several", "fatalities_context": "at_least_3_to_4", "injured": 6, "public_stock_anchor": "unavailable", "steel_support_height_m": 50, "steel_support_structures": 5, "trigger_date": "2025-02-25"} | adjusted OHLC backfill required |
| r10_loop17_builder_liquidity_rate_relief | price_data_unavailable_after_deep_search | {"BOK_policy_rate_pct": 2.5, "direct_price_anchor": "unavailable", "expected_rate_pct": 2.5, "support_package_krw_trn": 40.6, "trigger_date": "2024-03-27"} | adjusted OHLC backfill required |
