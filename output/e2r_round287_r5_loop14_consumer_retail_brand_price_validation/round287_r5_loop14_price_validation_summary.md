# Round 287 R5 Loop 14 Consumer Retail Brand Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_287.md
- round_id: round_215
- large_sector: CONSUMER_RETAIL_BRAND
- cases: 9
- Stage 3 dated candidates: 1
- stage4b_watch: 6
- stage4c_watch: 6
- hard_4c: 1
- service_trust_hard_reference: 1
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r5_loop14_samyang_buldak_export_stage3_candidate | Samyang Foods / Buldak export | structural_success_candidate + regulatory 4C-watch | 2024-06-14 | 2024-06-14 | 2024-06-14 | 2024-06-12 | aligned_partial | Samyang is the closest R5 Stage 3 candidate, but Denmark recall keeps regulatory fit as an explicit Green gate. |
| r5_loop14_nongshim_shin_ramyun_global_expansion | Nongshim / Shin Ramyun global expansion | success_candidate + insufficient_price_data | 2024-05-27 |  |  |  | success_candidate_but_price_data_unavailable | Nongshim has global brand evidence, but no event-day price anchor or margin/FCF bridge in this round. |
| r5_loop14_apr_medicube_beauty_device_brand_4b | APR / Medicube beauty device | structural_success_candidate + 4B-overheat | 2025-07-01 |  | 2025-10-01 | 2025-10-01 | aligned_partial_but_4B_watch | APR is useful as a K-beauty device success candidate and 4B-watch; repeat purchase and return-rate decide Green durability. |
| r5_loop14_kbeauty_us_expansion_basket | K-beauty U.S. expansion basket | success_candidate + tariff/physical sell-through 4C-watch | 2025-06-05 |  | 2025-06-05 | 2025-06-05 | success_candidate_but_offline_sellthrough_unproven | K-beauty U.S. expansion is a Stage 2 path; physical-store sell-through and tariff absorption decide upgrade. |
| r5_loop14_china_tourism_retail_event_premium | China tourism retail/dutyfree/beauty event basket | tourism_event_premium + 4B-watch | 2025-08-06 |  | 2025-08-06 |  | event_premium_visitor_count_not_spend | Tourism policy can move a basket, but R5 Green needs spend per head, conversion and margin. |
| r5_loop14_shinsegae_emart_alibaba_gmarket_jv_data_gate | Shinsegae / E-Mart / Alibaba-Gmarket JV | success_candidate + data gate | 2025-09-18 |  | 2024-12-26 | 2025-09-18 | success_candidate_data_gate | Gmarket/AliExpress JV is Stage 2 until take-rate, GMV, data compliance and fulfilment economics prove FCF. |
| r5_loop14_coupang_data_breach_retail_trust_hard_reference | Coupang data breach / retail trust hard reference | hard 4C service trust reference |  |  |  | 2026-02-25 | thesis_break_reference | Coupang breach is the hard trust reference: competitor traffic gain must still prove GMV and margin before any positive stage. |
| r5_loop14_cj_logistics_shinsegae_fulfillment_unit_economics | CJ Logistics / Shinsegae fulfilment | stage2_candidate_but_price_failed | 2024-06-17 |  | 2024-06-17 |  | evidence_good_but_price_failed | CJ Logistics has revenue uplift evidence, but weak event return and missing unit economics keep it below Green. |
| r5_loop14_domestic_retail_sales_shock_4c_watch | Domestic retail sales shock discretionary basket | domestic consumption 4C-watch |  |  |  | 2025-02-03 | domestic_consumption_shock_watch | Domestic consumption shock is a RedTeam overlay; export/tourism headlines must not hide weak discretionary demand. |

## Interpretation
- Samyang/Buldak is the closest R5 Stage 3 candidate, but local regulatory fit remains a Green gate.
- Nongshim and K-beauty U.S. expansion are Stage 2 paths until price, sell-through, margin and tariff evidence close.
- Tourism and JV scale are event premium or Stage 2 until spend-per-head, take-rate and compliance are proven.
- Coupang data breach is a hard trust reference; competitor read-through cannot become Green by itself.
