# Round 237 R7 Loop 10 Biotech Healthcare Device Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_237.md
- analyst_round_id: round_165
- large_sector: BIOTECH_HEALTHCARE_DEVICE
- cases: 7
- success_candidate: 4
- event_premium: 1
- failed_rerating: 2
- evidence_good_but_price_failed: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 6
- 4C-watch cases: 1
- hard_4c_case_count: 0
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round type | stage2 | stage3 | 4B | 4C-watch | alignment | note |
|---|---|---|---|---|---|---|---|---|---|
| r7_loop10_jeisys_aesthetic_device_take_private | Jeisys Medical | success_candidate | success_candidate_event_premium | 2024-09-11 |  |  |  | price_moved_without_evidence | Take-private validates aesthetic-device demand but is Stage 2; recurring sales, consumables, margin and FCF are required for Green. |
| r7_loop10_hugel_letybo_us_launch | 휴젤 | success_candidate | success_candidate | 2025-03-01 |  |  |  | unknown | U.S. launch is Stage 2; U.S. sales, channel penetration, ASP, repeat treatment and OPM are required before Green. |
| r7_loop10_sk_bioscience_idt_cmo_mna | SK바이오사이언스 | event_premium | success_candidate_event_premium | 2024-06-27 |  | 2024-06-27 |  | price_moved_without_evidence | IDT acquisition is Stage 2/event premium; utilization, backlog, margin and FCF are required before Green. |
| r7_loop10_celltrion_us_manufacturing_tariff_hedge | 셀트리온 | success_candidate | success_candidate | 2025-09-23 |  |  |  | unknown | U.S. facility is Stage 2 tariff hedge evidence; product transfer, quality readiness, utilization, margin and FCF decide promotion. |
| r7_loop10_samsung_biologics_gsk_facility_price_failed | 삼성바이오로직스 | success_candidate | evidence_good_but_price_failed | 2025-12-22 |  |  |  | evidence_good_but_price_failed | Good U.S. CDMO capacity event but immediate price reaction failed; utilization/contract transfer is needed for a fresh Stage 3 path. |
| r7_loop10_hanall_immunovant_batoclimab_ted_failure | 한올바이오파마 / Immunovant | failed_rerating | 4C-watch |  |  |  | 2026-04-02 | false_positive_score | Partner trial failure is 4C-watch; hard 4C requires broader pipeline or cashflow impairment confirmation. |
| r7_loop10_lunit_medical_ai_external_validation | 루닛 | failed_rerating | insufficient_evidence | 2025-03-17 |  |  |  | unknown | External validation is Stage 2 evidence; reimbursement, hospital adoption, recurring revenue, gross margin and cash runway are required before Green. |

## Interpretation
- Jeisys validates aesthetic device demand through take-private valuation, but that is Stage 2/event premium for listed peers.
- Hugel Letybo U.S. launch is Stage 2 until U.S. sales, channel penetration, ASP, repeat treatment, and OPM confirm.
- SK Bioscience and Celltrion facility/M&A events need utilization, backlog, product transfer, margin, and FCF before Green.
- Samsung Biologics has good U.S. CDMO evidence but immediate price confirmation failed, so it remains evidence_good_but_price_failed.
- HanAll/Immunovant is 4C-watch because partner trial failure matters, but hard 4C is not forced without broader impairment.
- Lunit external validation is Stage 2 evidence; reimbursement, hospital adoption, recurring revenue, and cash runway decide promotion.
