# Round 248 R5 Loop 11 Consumer Retail Brand Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_248.md
- round_id: round_176
- large_sector: CONSUMER_RETAIL_BRAND
- cases: 8
- structural_success: 2
- success_candidate: 2
- overheat: 1
- event_premium: 1
- failed_rerating: 1
- hard_4c_reference: 1
- hard_4c_krx_confirmed: false
- Stage 3 dated cases: 1
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r5_loop11_samyang_buldak_export_packaging_watch | Samyang Foods | structural_success_candidate_4C-watch | 2024-06-14 | 2024-06-14 |  | 2026-03-26 | aligned_partial | Export/ASP/OP revision supports Stage 3 candidate; packaging/input risk requires 4C-watch. |
| r5_loop11_nongshim_shin_global_staple | Nongshim | success_candidate | 2024-05-27 |  |  |  | success_candidate | Global staple and overseas expansion are Stage 2; OPM/EPS and channel sell-through required for Green. |
| r5_loop11_apr_medicube_structural_4b | APR / Medicube | structural_success_4B-watch | 2025-07-08 |  | 2025-07-08 |  | aligned | Revenue conversion supports structural success, but Medicube concentration and valuation require 4B-watch. |
| r5_loop11_indie_kbeauty_odm_distribution_watch | d'Alba / Silicon2 / Cosmax / Kolmar basket | success_candidate_overheat | 2025-06-05 |  | 2025-06-05 |  | price_moved_without_evidence_for_dalba_success_candidate_for_odm_distribution | Retail talks and ecommerce growth are Stage 2; physical sell-through, repeat orders, OPM and working-capital quality required before Green. |
| r5_loop11_amore_lghh_legacy_china_exposure | AmorePacific / LG Household & Health Care | failed_rerating_4C-watch |  |  |  |  | thesis_break_watch_insufficient_price_data | K-beauty macro is not enough; China and travel-retail weakness block Green until U.S./Europe offset is proven. |
| r5_loop11_emart_shinsegae_alibaba_jv_data_gate | E-Mart / Shinsegae / Alibaba JV | success_candidate_data_privacy_watch | 2025-09-18 |  |  |  | success_candidate_regulatory_data_watch | JV scale is Stage 2; GMV, take-rate, margin, retention and data compliance required before Green. |
| r5_loop11_coupang_breach_ecommerce_trust_reference | Coupang breach / Naver-E-Mart-CJ Logistics competitor basket | hard_4C_reference_competitor_success_candidate |  |  |  | 2026-02-25 | thesis_break_for_Coupang_success_candidate_for_competitors | Coupang is non-KRX but is the clean R5 platform-trust hard 4C reference; competitors need GMV/margin confirmation before Green. |
| r5_loop11_tourism_retail_china_visa_event | Hotel Shilla / Hyundai Department Store / Paradise / Hankook Cosmetics | event_premium_success_candidate | 2025-08-06 |  | 2025-08-06 |  | event_premium_success_candidate | Visa-free tourist policy is Stage 2/event; tourist spend, sell-through, duty-free sales and OPM required before Green. |

## Interpretation
- Samyang is an export/ASP/OP revision Stage 3 candidate, but packaging/input shock stays on 4C-watch.
- Nongshim is global-staple Stage 2 until OPM/EPS and channel sell-through confirm.
- APR/Medicube is structural success, but Medicube concentration and valuation need 4B-watch.
- d'Alba and the indie K-beauty/ODM basket are Stage 2/overheat until physical sell-through and working capital confirm.
- Legacy Amore/LG H&H must clear China and travel-retail weakness before any Green interpretation.
- E-Mart/Shinsegae-Alibaba JV is Stage 2 scale optionality with data-compliance gates.
- Coupang breach is a non-KRX hard 4C reference for platform trust; competitor opportunities still need GMV/margin proof.
- Tourism retail is an event premium until tourist spend, duty-free sales, casino drop/hold and OPM confirm.
