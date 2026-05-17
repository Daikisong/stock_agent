# Round-97 R5 Loop-5 Price Validation Plan

## Method

1. Assign stage dates from source evidence only.
2. Store stage-date close prices from official price data.
3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_30D / 90D / 180D / 1Y.
5. Compare export, sell-through, reorder, OPM, EPS revision, inventory, receivables, churn, regulation, and price path.
6. Mark food recall, tariff, data breach, supplier regulation, channel stuffing, hardware cycle, and IP/product safety explicitly.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `samyang_buldak_export_rerating_case` | `EXPORT_RECURRING_CONSUMER` | 2024-06-14 | needs_price_backfill |
| `samyang_buldak_denmark_recall_case` | `FOOD_SAFETY_RECALL_OVERLAY` | 2024-06-12 | needs_price_backfill |
| `samyang_buldak_denmark_partial_reversal_case` | `FOOD_SAFETY_RECALL_OVERLAY` | 2024-08-08 | needs_price_backfill |
| `kbeauty_us_export_overtake_france_case` | `K_BEAUTY_EXPORT_DISTRIBUTION` | 2025-06-05 | missing_direct_symbol_mapping |
| `olive_young_us_retail_platform_case` | `K_BEAUTY_RETAIL_PLATFORM` | undated | needs_exact_stage_date_backfill |
| `kbeauty_us_tariff_risk_case` | `TARIFF_IMPORT_REGULATION_OVERLAY` | undated | needs_exact_stage_date_backfill |
| `kbeauty_france_us_tariff_competition_case` | `TARIFF_IMPORT_REGULATION_OVERLAY` | undated | needs_exact_stage_date_backfill |
| `apr_medicube_beauty_device_case` | `BEAUTY_DEVICE_EXPORT` | 2025-10-20 | needs_price_backfill |
| `medicube_ulta_tiktok_omnichannel_case` | `BEAUTY_DEVICE_AFFILIATE_COMMERCE` | 2026-02-13 | missing_direct_symbol_mapping |
| `kbeauty_oem_odm_fast_beauty_case` | `BEAUTY_OEM_ODM_SUPPLYCHAIN` | 2025-06-05 | missing_direct_symbol_mapping |
| `coupang_data_breach_case` | `DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY` | 2025-11-29 | needs_exact_stage_date_backfill |
| `coupang_supplier_payment_regulation_case` | `DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY` | 2026-02-26 | needs_price_backfill |
| `coway_rental_recurring_case` | `HOME_LIVING_APPLIANCE_RENTAL` | undated | needs_source_date_and_price_backfill |
| `whirlpool_dividend_suspension_case` | `HOME_APPLIANCE_HARDWARE_CYCLE` | undated | needs_exact_stage_date_backfill |
| `shein_temu_ip_litigation_case` | `ULTRA_LOW_COST_CROSSBORDER_PLATFORM` | 2026-05-11 | missing_public_price_data |
| `shein_temu_eu_product_safety_case` | `ULTRA_LOW_COST_CROSSBORDER_PLATFORM` | undated | needs_exact_stage_date_backfill |

## Alignment Labels

- `EXPORT_RECURRING_ALIGNED`: export, ASP, OPM, EPS revision, and price path align.
- `FOOD_SAFETY_REGULATORY_4C_WATCH`: recall or country sales ban requires Stage 3 review.
- `KBEAUTY_STRUCTURAL_SUCCESS_CANDIDATE`: channel and export evidence route research; sell-through must be verified.
- `RETAIL_PLATFORM_STAGE2_NOT_STAGE3`: retail platform expansion is useful, but store-level sell-through, reorder, and inventory must be verified.
- `BEAUTY_DEVICE_ALIGNED_BUT_4B`: successful device/export story, but valuation and price run require 4B-watch.
- `AFFILIATE_COMMERCE_MARGIN_WATCH`: affiliate sales need CAC and discount checks before margin-quality credit.
- `ECOMMERCE_DATA_SECURITY_HARD_4C`: trust/regulation breaks the scale narrative.
- `POST_BREACH_TRUST_WATCH`: remediation claims need regulator confirmation before trust risk is cleared.
- `SUPPLIER_REGULATION_4C_WATCH`: margin quality breaks when supplier pressure or payment delay is visible.
- `HARDWARE_CYCLE_FAILURE`: appliance hardware cycle lacks recurring service economics.
- `FAST_FASHION_LEGAL_REGULATORY_4C_WATCH`: IP, supplier, product safety, or customs risk blocks Green.
