# Round 261 R5 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, stage prices, sell-through, inventory, receivables, GMV, margin, or FCF where raw adjusted data are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- business_anchor
- platform_or_channel_anchor
- data_or_trust_gate
- retail_distress_anchor
- price_validation_status

## Case Anchors

| case | data source | reported anchor | status |
|---|---|---|---|
| r5_loop12_samyang_buldak_export_asp_capacity | MarketWatch / WSJ Market Talk reported price and earnings anchor | Shares +5.7% on 2024-06-14; implied prior close 611,921 KRW; target upside +28.3% | reported_price_anchor_not_full_ohlc |
| r5_loop12_cj_olive_young_hb_global_platform | Reuters K-beauty / Olive Young business anchor | LA store plan and global platform evidence without parent price path | price_data_unavailable_after_deep_search |
| r5_loop12_dr_g_loreal_kbeauty_brand_mna_validation | Reuters L'Oreal / Dr.G acquisition anchor | Mibelle 2023 revenue 661M CHF / about $739M; brand validation only | price_data_unavailable_after_deep_search |
| r5_loop12_dalba_silicon2_cosmax_kolmar_physical_store_test | Reuters K-beauty retail / e-commerce / d'Alba price anchor | Top-five K-beauty U.S. e-commerce +71% vs overall market +21%; d'Alba >+100% since debut | reported_return_anchor_not_full_ohlc |
| r5_loop12_emart_shinsegae_alibaba_jv_data_gate | WSJ / Reuters JV and regulatory anchors | 50:50 JV; expected cross-border share 41%; Gmarket 50M customers; 3-year data-sharing restriction | reported_event_anchor_not_full_ohlc |
| r5_loop12_homeplus_mbk_offline_grocery_distress_reference | Reuters Homeplus restructuring / sale-plan anchors | Liquidation value 3.7T KRW, assets 6.8T KRW, MBK write-off 2.5T KRW | unlisted_sector_reference |
| r5_loop12_lotte_wellfood_india_pepero_localization | Times of India / Lotte India business anchor | 2027 target 3,000 crore rupees vs 2025 >2,000 crore; FY25-26 capex 475 crore | price_data_unavailable_after_deep_search |
| r5_loop12_kyochon_cherrybro_neuromeka_jensen_event | Tom's Hardware / MarketWatch event-return anchors | Only Neuromeka reportedly retained gains by close; no same-store sales or franchise margin evidence | reported_event_return_not_full_ohlc |
