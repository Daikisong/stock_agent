# E2R v12 Residual Research — R5 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / loop 135

```yaml
schema_version: e2r_stock_web_v12_residual_research
selected_round: R5
selected_loop: 135
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C20 direct URL/proxy quality, global distribution sell-through bridge, legacy-China/duty-free profitability break split
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution contract

This standalone Markdown file follows the v12 historical calibration runner contract. It does not run live discovery, does not open or patch `stock_agent` source code, does not create a production scoring change, and uses `Songdaiki/stock-web` as the price atlas. The only purpose is to add C20 residual evidence for later batch ingestion.

C20 is already above the minimum row-count regime, so this loop is not a quantity-fill exercise. It is a quality-repair pass: direct URL support, source-proxy labeling, complete 30/90/180D MFE/MAE, and a cleaner split between real global distribution sell-through and legacy-channel/profitability breaks.

## 1. No-Repeat / novelty audit

Recent in-session canonical outputs avoided: C05, C01, C13, C15, C10, C02, C16, R13_HIGH_MAE_GUARDRAIL, C17, C07, C06, C14, C11, C12, C09, C03, C04, C08, C18, C19.

No hard duplicate key is intentionally reused. Because C20's top symbols already include heavily studied names, this loop focuses on new trigger families / direct-source repair rather than claiming all symbols are novel.

```text
selected_canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_count = 0
new_independent_case_count = 6
same_archetype_distinct_symbol_count = 6
same_archetype_new_symbol_count_estimate = 1
same_archetype_new_trigger_family_count = 6
reused_case_count = 0
calibration_usable_case_count = 6
calibration_usable_trigger_count = 6
positive_case_count = 4
counterexample_count = 2
stage4b_case_count = 2
stage4c_case_count = 1
source_proxy_only_count = 2
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
```

## 2. Case universe

| case_id | symbol | company | trigger_date | entry_date | trigger_type | outcome_bucket | evidence_family | source_proxy_only |
|---|---:|---|---|---|---|---|---|---|
| C20-R5L135-01 | 257720 | Silicon2 / 실리콘투 | 2024-05-22 | 2024-05-23 | Stage3-Green | positive_with_local_4b_watch | global_kbeauty_platform_distribution_warehouse_export_mix | true |
| C20-R5L135-02 | 192820 | Cosmax / 코스맥스 | 2025-02-24 | 2025-02-25 | Stage3-Green | positive_clean_global_odm | record_2024_sales_indie_brand_us_japan_indirect_export | false |
| C20-R5L135-03 | 161890 | Kolmar Korea / 한국콜마 | 2024-08-09 | 2024-08-12 | Stage2-Actionable | positive_but_high_mae_confirmation_needed | official_2q24_earnings_odm_export_suncare_global_client_bridge | false |
| C20-R5L135-04 | 018290 | VT / 브이티 | 2024-05-14 | 2024-05-14 | Stage3-Green | positive_product_global_brand_sellthrough | reedle_shot_global_product_sales_profit_acceleration | false |
| C20-R5L135-05 | 090430 | Amorepacific / 아모레퍼시픽 | 2024-10-24 | 2024-10-25 | Stage4B | counterexample_china_loss_offsets_global_brand | cosrx_western_growth_offset_by_china_dutyfree_loss | true |
| C20-R5L135-06 | 051900 | LG Household & Health Care / LG생활건강 | 2025-04-28 | 2025-04-29 | Stage4C | counterexample_global_sales_not_enough_when_beauty_profitability_breaks | overseas_growth_but_domestic_global_slowdown_and_profitability_decline | false |

## 3. Evidence and source map

| case_id | primary evidence URL | supporting/direct URL | evidence summary |
|---|---|---|---|
| C20-R5L135-01 | https://securities.miraeasset.com/bbs/maildownload/20240522104231970_182 | https://www.siliconii.com/en/sub/sub03_01.php?boardid=newsen&category=&idx=5&mode=view&offset=56&sk=&sw= | Record 1Q24 result / worldwide K-beauty distributor bridge. Direct company source later confirms overseas logistics centers and partnerships with Sephora, Ulta, Costco, Watsons. Entry uses next tradable day after the research trigger. |
| C20-R5L135-02 | https://www.mk.co.kr/en/business/11249094 | https://file.alphasquare.co.kr/media/pdfs/company-ir/20250325%EC%BD%94%EC%8A%A4%EB%A7%A5%EC%8A%A4_HSBC_Global_Investment_Summit_%EC%B0%B8%EA%B0%80.pdf | 2024 consolidated sales rose 21.9% and operating profit rose 51.6%; K-beauty indie brand/overseas subsidiary mix created a real revenue and operating profit bridge rather than a generic theme. |
| C20-R5L135-03 | https://www.kolmar.co.kr/eng/ir/report.php | https://www.kolmar.co.kr/eng/ | Official IR page lists 2024 2Q earnings release. Business is ODM platform service with global technology/quality-control claims, but price route shows high MAE before later 180D MFE, so Green should wait for drawdown-aware confirmation. |
| C20-R5L135-04 | https://www.asiae.co.kr/en/article/2024051409253622995 | https://globalvt-cosmetics.com/ | Q1 2024 consolidated sales +113% YoY and OP jump were tied to cosmetics business. Official global product page supports Reedle Shot product identity; same-day close is allowed because evidence was published intraday. |
| C20-R5L135-05 | https://www.asiae.co.kr/en/article/2024102407520634414 | https://www.apgroup.com/int/en/investors/amorepacific-corporation/ir-reports/quarterly-results/__icsFiles/afieldfile/2025/02/06/AP_4Q24_EN_vff.pdf | COSRX/Western region growth was not enough to erase China subsidiary and travel-retail weakness. This is not pure price weakness; it is a non-price bridge-quality cap for C20. |
| C20-R5L135-06 | https://www.asiae.co.kr/en/article/2025042816110121788 | https://www.lghnh.com:984/ir/finance-info/ir-material.jsp | Reported profitability decline despite Japan/North America overseas sales growth. Price route has low MFE and deep 180D MAE; C20 global-distribution language must not override core profitability break. |

## 4. Price path verification

Price rows use `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`. MFE/MAE is computed from the entry close to each forward trading-window's max high / min low. Every usable row below has complete 30D/90D/180D fields.

| case_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | 180D peak | 180D trough |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| C20-R5L135-01 | 257720 | 2024-05-23 | 31450 | 72.3370 | -7.3132 | 72.3370 | -7.3132 | 72.3370 | -25.9141 | 2024-06-19 / 54200 | 2024-12-09 / 23300 |
| C20-R5L135-02 | 192820 | 2025-02-25 | 166000 | 13.0723 | -10.1807 | 72.8916 | -10.1807 | 72.8916 | -10.1807 | 2025-06-25 / 287000 | 2025-04-09 / 149100 |
| C20-R5L135-03 | 161890 | 2024-08-12 | 66300 | 17.7979 | -8.8989 | 18.7029 | -25.2640 | 32.7300 | -25.2640 | 2025-05-09 / 88000 | 2024-12-09 / 49550 |
| C20-R5L135-04 | 018290 | 2024-05-14 | 25500 | 56.8627 | -3.5294 | 56.8627 | -3.5294 | 72.5490 | -3.5294 | 2024-12-16 / 44000 | 2024-05-14 / 24600 |
| C20-R5L135-05 | 090430 | 2024-10-25 | 117300 | 9.2072 | -13.3845 | 10.8269 | -15.1748 | 26.4280 | -15.1748 | 2025-06-24 / 148300 | 2024-12-09 / 99500 |
| C20-R5L135-06 | 051900 | 2025-04-29 | 341000 | 2.6393 | -9.6774 | 4.2522 | -14.8094 | 4.2522 | -25.3666 | 2025-06-20 / 355500 | 2025-12-29 / 254500 |

## 5. Trigger JSONL

```jsonl
{"MAE_180D_pct": -25.9141, "MAE_30D_pct": -7.3132, "MAE_90D_pct": -7.3132, "MFE_180D_pct": 72.337, "MFE_30D_pct": 72.337, "MFE_90D_pct": 72.337, "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "C20-R5L135-01", "company": "Silicon2 / 실리콘투", "do_not_count_as_new_case": false, "entry_date": "2024-05-23", "entry_price": 31450.0, "evidence_family": "global_kbeauty_platform_distribution_warehouse_export_mix", "evidence_url_pending": false, "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "notes": "Record 1Q24 result / worldwide K-beauty distributor bridge. Direct company source later confirms overseas logistics centers and partnerships with Sephora, Ulta, Costco, Watsons. Entry uses next tradable day after the research trigger.", "outcome_bucket": "positive_with_local_4b_watch", "peak_180D_date": "2024-06-19", "peak_180D_high": 54200.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "research_id": "e2r_stock_web_v12_residual_round_R5_loop_135_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "row_type": "trigger", "same_entry_group_key": "C20|257720|2024-05-23", "selected_loop": 135, "selected_round": "R5", "source_proxy_only": true, "symbol": "257720", "trigger_date": "2024-05-22", "trigger_type": "Stage3-Green", "trough_180D_date": "2024-12-09", "trough_180D_low": 23300.0}
{"MAE_180D_pct": -10.1807, "MAE_30D_pct": -10.1807, "MAE_90D_pct": -10.1807, "MFE_180D_pct": 72.8916, "MFE_30D_pct": 13.0723, "MFE_90D_pct": 72.8916, "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "C20-R5L135-02", "company": "Cosmax / 코스맥스", "do_not_count_as_new_case": false, "entry_date": "2025-02-25", "entry_price": 166000.0, "evidence_family": "record_2024_sales_indie_brand_us_japan_indirect_export", "evidence_url_pending": false, "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "notes": "2024 consolidated sales rose 21.9% and operating profit rose 51.6%; K-beauty indie brand/overseas subsidiary mix created a real revenue and operating profit bridge rather than a generic theme.", "outcome_bucket": "positive_clean_global_odm", "peak_180D_date": "2025-06-25", "peak_180D_high": 287000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "research_id": "e2r_stock_web_v12_residual_round_R5_loop_135_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "row_type": "trigger", "same_entry_group_key": "C20|192820|2025-02-25", "selected_loop": 135, "selected_round": "R5", "source_proxy_only": false, "symbol": "192820", "trigger_date": "2025-02-24", "trigger_type": "Stage3-Green", "trough_180D_date": "2025-04-09", "trough_180D_low": 149100.0}
{"MAE_180D_pct": -25.264, "MAE_30D_pct": -8.8989, "MAE_90D_pct": -25.264, "MFE_180D_pct": 32.73, "MFE_30D_pct": 17.7979, "MFE_90D_pct": 18.7029, "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "C20-R5L135-03", "company": "Kolmar Korea / 한국콜마", "do_not_count_as_new_case": false, "entry_date": "2024-08-12", "entry_price": 66300.0, "evidence_family": "official_2q24_earnings_odm_export_suncare_global_client_bridge", "evidence_url_pending": false, "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "notes": "Official IR page lists 2024 2Q earnings release. Business is ODM platform service with global technology/quality-control claims, but price route shows high MAE before later 180D MFE, so Green should wait for drawdown-aware confirmation.", "outcome_bucket": "positive_but_high_mae_confirmation_needed", "peak_180D_date": "2025-05-09", "peak_180D_high": 88000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "research_id": "e2r_stock_web_v12_residual_round_R5_loop_135_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "row_type": "trigger", "same_entry_group_key": "C20|161890|2024-08-12", "selected_loop": 135, "selected_round": "R5", "source_proxy_only": false, "symbol": "161890", "trigger_date": "2024-08-09", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-12-09", "trough_180D_low": 49550.0}
{"MAE_180D_pct": -3.5294, "MAE_30D_pct": -3.5294, "MAE_90D_pct": -3.5294, "MFE_180D_pct": 72.549, "MFE_30D_pct": 56.8627, "MFE_90D_pct": 56.8627, "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "C20-R5L135-04", "company": "VT / 브이티", "do_not_count_as_new_case": false, "entry_date": "2024-05-14", "entry_price": 25500.0, "evidence_family": "reedle_shot_global_product_sales_profit_acceleration", "evidence_url_pending": false, "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "notes": "Q1 2024 consolidated sales +113% YoY and OP jump were tied to cosmetics business. Official global product page supports Reedle Shot product identity; same-day close is allowed because evidence was published intraday.", "outcome_bucket": "positive_product_global_brand_sellthrough", "peak_180D_date": "2024-12-16", "peak_180D_high": 44000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "research_id": "e2r_stock_web_v12_residual_round_R5_loop_135_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "row_type": "trigger", "same_entry_group_key": "C20|018290|2024-05-14", "selected_loop": 135, "selected_round": "R5", "source_proxy_only": false, "symbol": "018290", "trigger_date": "2024-05-14", "trigger_type": "Stage3-Green", "trough_180D_date": "2024-05-14", "trough_180D_low": 24600.0}
{"MAE_180D_pct": -15.1748, "MAE_30D_pct": -13.3845, "MAE_90D_pct": -15.1748, "MFE_180D_pct": 26.428, "MFE_30D_pct": 9.2072, "MFE_90D_pct": 10.8269, "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "C20-R5L135-05", "company": "Amorepacific / 아모레퍼시픽", "do_not_count_as_new_case": false, "entry_date": "2024-10-25", "entry_price": 117300.0, "evidence_family": "cosrx_western_growth_offset_by_china_dutyfree_loss", "evidence_url_pending": false, "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "notes": "COSRX/Western region growth was not enough to erase China subsidiary and travel-retail weakness. This is not pure price weakness; it is a non-price bridge-quality cap for C20.", "outcome_bucket": "counterexample_china_loss_offsets_global_brand", "peak_180D_date": "2025-06-24", "peak_180D_high": 148300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "research_id": "e2r_stock_web_v12_residual_round_R5_loop_135_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "row_type": "trigger", "same_entry_group_key": "C20|090430|2024-10-25", "selected_loop": 135, "selected_round": "R5", "source_proxy_only": true, "symbol": "090430", "trigger_date": "2024-10-24", "trigger_type": "Stage4B", "trough_180D_date": "2024-12-09", "trough_180D_low": 99500.0}
{"MAE_180D_pct": -25.3666, "MAE_30D_pct": -9.6774, "MAE_90D_pct": -14.8094, "MFE_180D_pct": 4.2522, "MFE_30D_pct": 2.6393, "MFE_90D_pct": 4.2522, "calibration_usable": true, "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "case_id": "C20-R5L135-06", "company": "LG Household & Health Care / LG생활건강", "do_not_count_as_new_case": false, "entry_date": "2025-04-29", "entry_price": 341000.0, "evidence_family": "overseas_growth_but_domestic_global_slowdown_and_profitability_decline", "evidence_url_pending": false, "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "notes": "Reported profitability decline despite Japan/North America overseas sales growth. Price route has low MFE and deep 180D MAE; C20 global-distribution language must not override core profitability break.", "outcome_bucket": "counterexample_global_sales_not_enough_when_beauty_profitability_breaks", "peak_180D_date": "2025-06-20", "peak_180D_high": 355500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "research_id": "e2r_stock_web_v12_residual_round_R5_loop_135_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "row_type": "trigger", "same_entry_group_key": "C20|051900|2025-04-29", "selected_loop": 135, "selected_round": "R5", "source_proxy_only": false, "symbol": "051900", "trigger_date": "2025-04-28", "trigger_type": "Stage4C", "trough_180D_date": "2025-12-29", "trough_180D_low": 254500.0}
```

## 6. Score simulation JSONL

```jsonl
{"alignment_note": "C20 bridge gate raises visibility/information confidence; market-mispricing and valuation are trimmed when evidence is only theme/proxy.", "case_id": "C20-R5L135-01", "raw_components": {"bottleneck_pricing": 58, "capital_allocation": 40, "earnings_visibility": 88, "eps_fcf_explosion": 86, "information_confidence": 74, "market_mispricing": 66, "valuation_rerating": 55}, "row_type": "score_simulation", "score_after_shadow": 73.62, "score_before": 72.83, "stage_after_shadow": "Stage2-Actionable", "stage_before_proxy": "Stage2-Actionable", "symbol": "257720", "trigger_type": "Stage3-Green", "weight_after_shadow": {"bottleneck_pricing": 11, "capital_allocation": 4, "earnings_visibility": 25, "eps_fcf_explosion": 22, "information_confidence": 12, "market_mispricing": 14, "valuation_rerating": 12}, "weight_before": {"bottleneck_pricing": 12, "capital_allocation": 4, "earnings_visibility": 23, "eps_fcf_explosion": 22, "information_confidence": 10, "market_mispricing": 16, "valuation_rerating": 13}}
{"alignment_note": "C20 bridge gate raises visibility/information confidence; market-mispricing and valuation are trimmed when evidence is only theme/proxy.", "case_id": "C20-R5L135-02", "raw_components": {"bottleneck_pricing": 55, "capital_allocation": 45, "earnings_visibility": 86, "eps_fcf_explosion": 90, "information_confidence": 82, "market_mispricing": 68, "valuation_rerating": 60}, "row_type": "score_simulation", "score_after_shadow": 75.71, "score_before": 74.86, "stage_after_shadow": "Stage3-Yellow", "stage_before_proxy": "Stage2-Actionable", "symbol": "192820", "trigger_type": "Stage3-Green", "weight_after_shadow": {"bottleneck_pricing": 11, "capital_allocation": 4, "earnings_visibility": 25, "eps_fcf_explosion": 22, "information_confidence": 12, "market_mispricing": 14, "valuation_rerating": 12}, "weight_before": {"bottleneck_pricing": 12, "capital_allocation": 4, "earnings_visibility": 23, "eps_fcf_explosion": 22, "information_confidence": 10, "market_mispricing": 16, "valuation_rerating": 13}}
{"alignment_note": "C20 bridge gate raises visibility/information confidence; market-mispricing and valuation are trimmed when evidence is only theme/proxy.", "case_id": "C20-R5L135-03", "raw_components": {"bottleneck_pricing": 48, "capital_allocation": 43, "earnings_visibility": 69, "eps_fcf_explosion": 72, "information_confidence": 76, "market_mispricing": 61, "valuation_rerating": 52}, "row_type": "score_simulation", "score_after_shadow": 63.99, "score_before": 63.31, "stage_after_shadow": "Stage2", "stage_before_proxy": "Stage2", "symbol": "161890", "trigger_type": "Stage2-Actionable", "weight_after_shadow": {"bottleneck_pricing": 11, "capital_allocation": 4, "earnings_visibility": 25, "eps_fcf_explosion": 22, "information_confidence": 12, "market_mispricing": 14, "valuation_rerating": 12}, "weight_before": {"bottleneck_pricing": 12, "capital_allocation": 4, "earnings_visibility": 23, "eps_fcf_explosion": 22, "information_confidence": 10, "market_mispricing": 16, "valuation_rerating": 13}}
{"alignment_note": "C20 bridge gate raises visibility/information confidence; market-mispricing and valuation are trimmed when evidence is only theme/proxy.", "case_id": "C20-R5L135-04", "raw_components": {"bottleneck_pricing": 64, "capital_allocation": 40, "earnings_visibility": 84, "eps_fcf_explosion": 92, "information_confidence": 78, "market_mispricing": 72, "valuation_rerating": 57}, "row_type": "score_simulation", "score_after_shadow": 76.16, "score_before": 75.57, "stage_after_shadow": "Stage3-Yellow", "stage_before_proxy": "Stage3-Yellow", "symbol": "018290", "trigger_type": "Stage3-Green", "weight_after_shadow": {"bottleneck_pricing": 11, "capital_allocation": 4, "earnings_visibility": 25, "eps_fcf_explosion": 22, "information_confidence": 12, "market_mispricing": 14, "valuation_rerating": 12}, "weight_before": {"bottleneck_pricing": 12, "capital_allocation": 4, "earnings_visibility": 23, "eps_fcf_explosion": 22, "information_confidence": 10, "market_mispricing": 16, "valuation_rerating": 13}}
{"alignment_note": "C20 bridge gate raises visibility/information confidence; market-mispricing and valuation are trimmed when evidence is only theme/proxy.", "case_id": "C20-R5L135-05", "raw_components": {"bottleneck_pricing": 45, "capital_allocation": 42, "earnings_visibility": 50, "eps_fcf_explosion": 58, "information_confidence": 72, "market_mispricing": 55, "valuation_rerating": 48}, "row_type": "score_simulation", "score_after_shadow": 53.99, "score_before": 53.58, "stage_after_shadow": "Stage4B", "stage_before_proxy": "Stage4B", "symbol": "090430", "trigger_type": "Stage4B", "weight_after_shadow": {"bottleneck_pricing": 11, "capital_allocation": 4, "earnings_visibility": 25, "eps_fcf_explosion": 22, "information_confidence": 12, "market_mispricing": 14, "valuation_rerating": 12}, "weight_before": {"bottleneck_pricing": 12, "capital_allocation": 4, "earnings_visibility": 23, "eps_fcf_explosion": 22, "information_confidence": 10, "market_mispricing": 16, "valuation_rerating": 13}}
{"alignment_note": "C20 bridge gate raises visibility/information confidence; market-mispricing and valuation are trimmed when evidence is only theme/proxy.", "case_id": "C20-R5L135-06", "raw_components": {"bottleneck_pricing": 38, "capital_allocation": 45, "earnings_visibility": 38, "eps_fcf_explosion": 42, "information_confidence": 80, "market_mispricing": 45, "valuation_rerating": 40}, "row_type": "score_simulation", "score_after_shadow": 45.42, "score_before": 44.74, "stage_after_shadow": "Stage4C", "stage_before_proxy": "Stage4C", "symbol": "051900", "trigger_type": "Stage4C", "weight_after_shadow": {"bottleneck_pricing": 11, "capital_allocation": 4, "earnings_visibility": 25, "eps_fcf_explosion": 22, "information_confidence": 12, "market_mispricing": 14, "valuation_rerating": 12}, "weight_before": {"bottleneck_pricing": 12, "capital_allocation": 4, "earnings_visibility": 23, "eps_fcf_explosion": 22, "information_confidence": 10, "market_mispricing": 16, "valuation_rerating": 13}}
```

## 7. Aggregate / dedupe result

```json
{
  "row_type": "aggregate",
  "selected_round": "R5",
  "selected_loop": 135,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
  "fine_archetype_id": "K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_BRIDGE",
  "representative_trigger_count": 6,
  "same_entry_group_count": 6,
  "deduped_trigger_count": 6,
  "positive_case_count": 4,
  "counterexample_count": 2,
  "stage4b_case_count": 2,
  "stage4c_case_count": 1,
  "source_proxy_only_count": 2,
  "evidence_url_pending_count": 0,
  "rows_missing_required_mfe_mae": 0,
  "avg_MFE_90D_pct": 39.3122,
  "avg_MAE_90D_pct": -12.7119,
  "avg_MFE_180D_pct": 46.8646,
  "avg_MAE_180D_pct": -17.5716
}
```

## 8. Residual contribution summary

C20 has a deceptively simple headline: K-beauty/K-food goes global. The residual error is that the phrase can mean three very different things.

First, it can mean a real distribution machine: named overseas regions, warehouses, channel partners, reorder or sell-through, and operating-profit conversion. Silicon2, Cosmax, VT, and, with more drawdown caution, Kolmar belong here.

Second, it can mean a brand story whose global growth is still being eaten by older weak channels. Amorepacific's COSRX/Western growth and LG H&H's overseas growth were not enough to erase China, travel-retail, or core beauty profitability drag. This group should not receive automatic Stage2-Actionable/Green treatment merely because the global distribution vocabulary is present.

Third, it can mean broker or news proxy. The price path may be tradable, but promotion should be capped until a direct IR/company/disclosure/earnings URL confirms the bridge.

## 9. Shadow rule candidate

```json
{
  "row_type": "shadow_rule_candidate",
  "axis": "C20_GLOBAL_DISTRIBUTION_SELLTHROUGH_PROFIT_BRIDGE_GATE",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "scope": {
    "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
    "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION"
  },
  "rule": "Do not unlock C20 Stage2-Actionable or Green from generic K-beauty/K-food/global-distribution/export/Amazon wording alone. Require at least two of: named overseas region/channel, repeat sell-through/reorder signal, overseas sales-mix acceleration, warehouse/fulfillment/distribution infrastructure, current revenue/OP/revision conversion, and non-China diversification quality. If China/duty-free/legacy-brand loss or core beauty profitability decline remains material, cap at Stage4B or route to Stage4C depending on direct thesis break.",
  "weight_before_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/23/12/16/13/4/10",
  "weight_after_shadow_EPS_Vis_Bott_Mis_Val_Cap_Info": "22/25/11/14/12/4/12",
  "delta": "0/+2/-1/-2/-1/0/+2",
  "expected_effect": "Raises visibility and information-confidence weight for direct sell-through evidence while trimming market-mispricing/valuation credit for theme-only global distribution rows."
}
```

### Rule intuition

C20 global distribution is not just a flag planted on a world map. The E2R bridge should see goods moving through the harbor: warehouse capacity, overseas channel access, repeat consumer pull, and the receipt that shows up in revenue and operating profit. A map without cargo is theme; cargo without margin is weak Stage2; cargo plus repeat margin conversion is the real rerating bridge.

## 10. Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff and requires non-price bridge for full 4B. This C20 loop does not re-propose the global rule. It adds a C20-specific bridge shape:

```text
C20 positive unlock = distribution channel + sell-through/reorder + revenue/OP bridge
C20 4B cap = global growth present, but China/duty-free/legacy channel or high-MAE risk still unresolved
C20 4C route = core profitability or thesis bridge breaks despite overseas growth vocabulary
```

## 11. Batch ingest self-audit

```text
standard_v12_filename = pass
filename_round_matches_metadata = pass
filename_loop_matches_metadata = pass
round_sector_consistency = pass
canonical_archetype_id_valid = pass
trigger_type_canonical_label_only = pass
complete_30_90_180_mfe_mae = pass
stock_web_price_source_used = pass
manifest_max_date_respected = pass
corporate_action_contamination_check = pass_no_180D_overlap_for_selected_windows
source_proxy_only_explicitly_marked = pass
evidence_url_pending_count = 0
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent for stock_agent. Do not use this research file as a production patch by itself. Ingest it together with the full v12 corpus, deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date, verify all price rows against Songdaiki/stock-web, then test whether C20_GLOBAL_DISTRIBUTION_SELLTHROUGH_PROFIT_BRIDGE_GATE improves C20 false-positive handling without suppressing clean Silicon2/Cosmax/VT-style positive routes.

Candidate implementation note:
- Scope only C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.
- Add/strengthen evidence predicates for overseas channel, sell-through/reorder, warehouse/fulfillment infrastructure, overseas revenue mix, OP/revision conversion, and non-China diversification quality.
- Cap theme-only rows at Stage2/Watch.
- Route legacy-channel/profitability break rows to 4B/4C depending on direct evidence severity.
- Keep production scoring unchanged until batch validation and regression tests pass.
```

## 13. Research state footer

```text
completed_round = R5
completed_loop = 135
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C20 direct URL/proxy quality, global distribution sell-through bridge, legacy-China/duty-free profitability break split
next_recommended_archetypes = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN; C22_INSURANCE_RATE_CYCLE_RESERVE; C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION; C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
