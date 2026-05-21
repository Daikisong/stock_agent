# Round 328 R7 Loop 17 Price Validation Plan

Full adjusted OHLC is not complete. Do not create MFE/MAE or peak/drawdown values from reported event anchors.

| case_id | status | event anchor | next backfill |
| --- | --- | --- | --- |
| r7_loop17_sk_bioscience_idt_biologika | price_data_unavailable_after_deep_search | {"deal_value_krw_bn": 339, "deal_value_usd_mn": 243.75, "event_return_pct": 11.7, "stake_pct": 60, "trigger_date": "2024-06-27"} | adjusted OHLC backfill required |
| r7_loop17_samsung_biologics_policy_support | price_data_unavailable_after_deep_search | {"kospi_event_return_pct": 0.99, "market_relative_outperformance_pp": 5.24, "pharma_exports_usd_bn": 9.59, "pharma_sector_event_return_pct": 3.97, "samsung_biologics_event_return_pct": 6.23, "trigger_date": "2025-05-21", "us_export_share_pct": 16} | adjusted OHLC backfill required |
| r7_loop17_samsung_biologics_gsk_us_facility | price_data_unavailable_after_deep_search | {"broader_market_event_return_pct": 2.0, "capacity_liters": 60000, "deal_value_usd_mn": 280, "relative_event_return_pp": -2.4, "samsung_bio_event_return_pct": -0.4, "trigger_date": "2025-12-22"} | adjusted OHLC backfill required |
| r7_loop17_celltrion_us_factory_localization | price_data_unavailable_after_deep_search | {"additional_expansion_krw_bn": 700, "direct_price_anchor": null, "imclone_acquisition_usd_mn": 330, "planned_initial_investment_krw_bn": 700, "preferred_bidder_date": "2025-07-29"} | adjusted OHLC backfill required |
| r7_loop17_alteogen_keytruda_sc | price_data_unavailable_after_deep_search | {"clinical_trigger_date": "2024-11-19", "expected_peak_adoption_pct": "30-40", "fda_target_action_date": "2025-09-23", "iv_minutes": 30, "keytruda_2024_sales_usd_bn": 30, "launch_plan_date": "2025-03-27", "planned_us_launch_date": "2025-10-01", "sc_minutes": 2} | adjusted OHLC backfill required |
| r7_loop17_hugel_letybo_us_fda | price_data_unavailable_after_deep_search | {"botox_unit_price_usd": "12-18", "commercial_rollout_date": "2025-03", "direct_price_anchor": null, "letybo_unit_price_usd": "9-12"} | adjusted OHLC backfill required |
| r7_loop17_jeisys_archimed_medical_aesthetic_ma | price_data_unavailable_after_deep_search | {"deal_value_usd_mn": 742, "event_reaction_context": "little_changed", "reported_close_price_krw": 12860, "trigger_date": "2024-09-11"} | adjusted OHLC backfill required |
| r7_loop17_samsung_bioepis_amgen_patent_litigation | price_data_unavailable_after_deep_search | {"asserted_patents": 34, "direct_price_anchor": null, "hard_4c_status": "not_confirmed", "prolia_prior_year_us_sales_usd_bn": 2.7, "trigger_date": "2024-08-13", "xgeva_prior_year_us_sales_usd_bn": 1.5} | adjusted OHLC backfill required |
