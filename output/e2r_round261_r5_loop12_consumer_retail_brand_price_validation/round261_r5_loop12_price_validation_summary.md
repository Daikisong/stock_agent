# Round 261 R5 Loop 12 Consumer Retail Brand Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_261.md
- round_id: round_189
- large_sector: CONSUMER_RETAIL_BRAND
- cases: 8
- structural_success: 1
- success_candidate: 5
- overheat: 1
- thesis_break_reference: 1
- hard_4c: 1
- direct_krx_hard_4c_confirmed: false
- Stage 3 dated cases: 1
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r5_loop12_samyang_buldak_export_asp_capacity | Samyang Foods | structural_success_candidate + single-SKU/input 4B-watch | 2024-06-14 | 2024-06-14 | 2024-06-14 |  | aligned_partial | Export, ASP, OP revision and capacity expansion support a Stage 3 candidate; single-SKU concentration remains 4B-watch. |
| r5_loop12_cj_olive_young_hb_global_platform | CJ Olive Young / CJ Corp exposure | success_candidate + insufficient_price_data | 2025-06-05 |  | 2025-06-05 |  | success_candidate_but_insufficient_price_data | Strong H&B retail platform evidence, but Olive Young is unlisted; parent earnings bridge and listed price path are required. |
| r5_loop12_dr_g_loreal_kbeauty_brand_mna_validation | Dr.G / Gowoonsesang / L'Oreal acquisition read-through | success_candidate + M&A validation, not Green | 2024-12-23 |  | 2024-12-23 |  | success_candidate_M&A_validation | Brand M&A validates K-beauty value, but it is not listed-company revenue; ODM/distributor order bridge is required. |
| r5_loop12_dalba_silicon2_cosmax_kolmar_physical_store_test | d'Alba / Silicon2 / Cosmax / Kolmar basket | success_candidate + overheat_watch | 2025-06-05 |  | 2025-06-05 |  | success_candidate_plus_4B_watch | E-commerce growth is strong, but physical-store sell-through, repeat orders, inventory and OPM are required before Green. |
| r5_loop12_emart_shinsegae_alibaba_jv_data_gate | E-Mart / Shinsegae / Alibaba JV | success_candidate + data_gate_watch | 2024-12-26 |  | 2024-12-26 |  | success_candidate_data_gate_watch | JV scale is Stage 2; GMV, take-rate, margin, retention and data compliance are required before Green. |
| r5_loop12_homeplus_mbk_offline_grocery_distress_reference | Homeplus / MBK Partners | 4C-thesis-break reference |  |  |  | 2025-03-01 | thesis_break_reference | Unlisted but important R5 hard reference: offline grocery asset value is not Green without cash flow and debt stability. |
| r5_loop12_lotte_wellfood_india_pepero_localization | Lotte Wellfood / Lotte India | success_candidate + insufficient_price_data | 2025-07-24 |  |  |  | success_candidate_but_insufficient_price_data | India localization is Stage 2; parent-company revenue recognition, margin, FCF and FX/capex risk must confirm. |
| r5_loop12_kyochon_cherrybro_neuromeka_jensen_event | Kyochon F&B / Cherrybro / Neuromeka | overheat / price_moved_without_evidence |  |  | 2025-10-31 |  | price_moved_without_evidence | Viral celebrity food-service event is 4B/event premium until same-store sales, franchise margin and repeat demand confirm. |

## Interpretation
- Samyang is the R5 K-food export benchmark because export, ASP, OP revision and capacity appeared together.
- CJ Olive Young and Dr.G are strong Stage 2 references, but unlisted or indirect exposure blocks automatic Green.
- d'Alba/K-beauty indie and E-Mart/Alibaba JV need physical sell-through or GMV/margin/data-compliance proof.
- Homeplus is an unlisted offline grocery 4C reference, not a Green case.
- Kyochon/Cherrybro/Neuromeka is price_moved_without_evidence from a celebrity food-service event.
