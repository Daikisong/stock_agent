# Round 263 R7 Loop 12 Biotech Healthcare Device Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_263.md
- round_id: round_191
- large_sector: BIOTECH_HEALTHCARE_DEVICE
- cases: 8
- success_candidate: 4
- event_premium: 1
- failed_rerating: 1
- watch_cases: 2
- hard_4c: 0
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r7_loop12_jeisys_medical_ebd_global_buyout | Jeisys Medical | structural_success_candidate / PE buyout | 2024-09-11 |  | 2024-09-11 |  | business_validated_delisting_tracking_gap | EBD business quality is validated, but delisting prevents listed-equity Stage 3 path tracking. |
| r7_loop12_apr_medicube_device_crossover | APR / Medicube device | structural_success_candidate + 4B-watch | 2025-10-20 |  | 2025-10-20 |  | aligned_partial_4B_concentration_watch | APR device demand has revenue evidence, but concentration/channel/regulatory durability must be proven before Green. |
| r7_loop12_classys_aesthetic_device_export_platform | Classys | success_candidate / insufficient_price_data | 2025-01-01 |  |  |  | success_candidate_but_insufficient_price_data | Aesthetic export platform is Stage 2; installed base, consumables, OPM, FCF and price path are missing. |
| r7_loop12_hugel_letybo_us_toxin_launch | Hugel / Letybo | success_candidate / U.S. toxin launch | 2025-03-31 |  |  |  | success_candidate | FDA approval and price advantage are Stage 2; provider adoption and repeat injection economics are required. |
| r7_loop12_medytox_innotox_unauthorized_distribution | Medytox / Innotox | 4C-watch / safety trust |  |  |  | 2025-07-01 | thesis_break_watch | Unauthorized toxin distribution is a safety/trust watch and blocks Green until resolved. |
| r7_loop12_lunit_insight_dbt_validation_not_revenue | Lunit / INSIGHT DBT | insufficient_evidence / validation not revenue | 2025-03-17 |  |  | 2025-03-17 | insufficient_evidence | Aggregate AUC is useful validation, but Green needs reimbursement, adoption and recurring revenue. |
| r7_loop12_medical_quota_doctors_strike_disruption | Medical-school quota / doctors' strike | medical-service 4C-watch | 2026-02-10 |  |  | 2025-03-07 | thesis_break_watch | Medical quota policy is not Green until procedure volume, utilization and reimbursement are visible. |
| r7_loop12_osstem_zimvie_dental_mna_event | Osstem Implant / ZimVie | event_premium / global dental M&A validation | 2024-07-18 |  | 2024-07-18 |  | event_premium | Target-stock event return validates M&A interest, but delisted buyer and unconfirmed close block Green. |

## Interpretation
- Aesthetic device buyouts validate business quality, but delisting can close public Stage 3 tracking.
- Beauty-device growth needs repeat demand and channel durability, not viral demand alone.
- FDA approval and AI AUC are Stage 2 until adoption, reimbursement and revenue conversion confirm.
- Unauthorized toxin distribution and medical-service disruption are 4C-watch, not Green evidence.
- Dental M&A rumor is event premium until close, integration and public listed bridge are visible.
