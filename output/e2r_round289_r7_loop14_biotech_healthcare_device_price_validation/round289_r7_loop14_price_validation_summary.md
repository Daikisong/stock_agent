# Round 289 R7 Loop 14 Bio Healthcare Medical Device Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_289.md
- round_id: round_217
- large_sector: BIOTECH_HEALTHCARE_DEVICE
- cases: 8
- success_candidate: 7
- event_premium: 1
- hard_4c: 0
- sector_hard_4c_reference: 1
- Stage 3 dated cases: 1
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r7_loop14_samsung_biologics_gsk_us_facility | Samsung Biologics | evidence_good_but_price_failed | 2025-12-22 |  |  | 2025-12-22 | evidence_good_but_price_failed | U.S. facility acquisition underperformed the market; facility utilization and margin remain the gate. |
| r7_loop14_celltrion_us_factory_tariff_hedge | Celltrion | success_candidate_price_unavailable | 2025-09-23 |  | 2025-11-19 | 2025-11-19 | success_candidate_but_price_data_unavailable | U.S. tariff hedge is Stage 2; product transfer, utilization and margin are still missing. |
| r7_loop14_sk_bioscience_idt_biologika_ma | SK Bioscience | event_premium_success_candidate | 2024-06-27 |  | 2024-06-27 | 2024-06-27 | event_premium_success_candidate | IDT acquisition drove event premium; integration, backlog and margin must be proven. |
| r7_loop14_alteogen_keytruda_qlex_sc_formulation | Alteogen | structural_success_candidate_price_unavailable | 2025-03-27 | 2025-09-19 | 2025-09-19 | 2025-09-19 | structural_success_candidate_but_price_data_unavailable | Strongest structural candidate in this pack; Green waits for adoption, royalty and IP gates. |
| r7_loop14_yuhan_lazertinib_jnj_rybrevant_approval | Yuhan | success_candidate_price_unavailable | 2024-08-20 |  | 2024-08-20 | 2024-12-16 | success_candidate_but_price_data_unavailable | FDA approval is Stage 2; royalty economics and manufacturing regulatory gate remain. |
| r7_loop14_hugel_letybo_us_aesthetic_launch | Hugel | success_candidate_regulatory_watch | 2025-03-01 |  | 2025-03-01 | 2025-11-01 | success_candidate_but_price_data_unavailable | FDA approval and U.S. launch need physician adoption, distributor margin and safety compliance. |
| r7_loop14_adel_sanofi_alzheimers_tech_export_reference | ADEL / Sanofi | success_candidate_reference_only | 2025-12-15 |  | 2025-12-15 | 2025-12-15 | success_candidate_reference_only | Upfront/milestone deal is Stage 2; Phase 2/3 data and royalty probability are required. |
| r7_loop14_global_clinical_fda_failure_hard_reference | HilleVax / Corcept / PepGen reference | sector_hard_4C_reference |  |  |  | 2024-07-08 | thesis_break_reference | Clinical/FDA failure can reset biotech valuation immediately; use as sector hard 4C reference. |

## Interpretation
- CMO/CDMO facility acquisition is Stage 2 until utilization, inspection, tech transfer and margin appear.
- FDA approval is Stage 2 until launch, reimbursement, uptake and royalty economics appear.
- Tech-export upfront value is Stage 2 until Phase 2/3 data, milestones and partner execution improve probability.
- Medical-aesthetic launch is Stage 2 until physician adoption, distributor margin and safety compliance appear.
- Global clinical/FDA failures are sector hard 4C references, not positive candidates.
