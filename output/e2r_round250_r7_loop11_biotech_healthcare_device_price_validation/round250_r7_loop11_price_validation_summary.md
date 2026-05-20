# Round 250 R7 Loop 11 Biotech Healthcare Device Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_250.md
- analyst_round_id: round_178
- large_sector: BIOTECH_HEALTHCARE_DEVICE
- cases: 8
- success_candidate: 5
- event_premium: 1
- failed_rerating: 2
- evidence_good_but_price_failed: 1
- price_moved_without_evidence: 2
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- 4C-watch cases: 2
- hard_4c_case_count: 0
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round type | stage2 | stage3 | 4B | 4C-watch | alignment | note |
|---|---|---|---|---|---|---|---|---|---|
| r7_loop11_alteogen_keytruda_sc_platform_royalty | Alteogen | success_candidate | success_candidate_4b_watch | 2025-03-27 |  |  |  | unknown | Platform royalty story is Stage 2; Green requires royalty/supply revenue, launch adoption and patent durability. |
| r7_loop11_yuhan_lazertinib_global_approval | Yuhan / Oscotec / Lazertinib | success_candidate | success_candidate_launch_revenue_gate | 2024-08-20 |  |  | 2024-12-16 | unknown | Global approval is Stage 2; royalty, milestone, prescription uptake and revenue recognition decide promotion. |
| r7_loop11_samsung_biologics_gsk_facility_price_failed | Samsung Biologics | success_candidate | evidence_good_but_price_failed | 2025-12-22 |  |  |  | evidence_good_but_price_failed | Good U.S. CDMO evidence failed immediate price confirmation; utilization and FCF are still required. |
| r7_loop11_celltrion_us_tariff_hedge_factory | Celltrion | success_candidate | success_candidate_us_tariff_hedge_manufacturing | 2025-09-23 |  |  |  | unknown | U.S. tariff-hedge manufacturing is Stage 2; product transfer, utilization, margin and FCF decide Stage 3. |
| r7_loop11_sk_bioscience_idt_cmo_mna | SK Bioscience | success_candidate | success_candidate_event_premium | 2024-06-27 |  | 2024-06-27 |  | price_moved_without_evidence | M&A is Stage 2/event premium; backlog, utilization, margin and FCF are required before Green. |
| r7_loop11_hanall_immunovant_batoclimab_ted_failure | HanAll Biopharma / Immunovant | failed_rerating | 4C-watch |  |  |  | 2026-04-02 | false_positive_score | Partner trial failure is 4C-watch; hard 4C is not forced without broader pipeline or cashflow impairment. |
| r7_loop11_lunit_medical_ai_external_validation | Lunit | failed_rerating | insufficient_evidence | 2025-03-17 |  |  |  | unknown | External validation is Stage 2 evidence; reimbursement, hospital adoption, recurring revenue and cash runway block Green. |
| r7_loop11_biopharma_tariff_policy_relief_basket | Biopharma tariff-policy basket | event_premium | event_premium_policy_relief | 2025-05-21 |  | 2025-05-21 |  | price_moved_without_evidence | Policy relief is event premium; company-level revenue, margin and FCF are required before Green. |

## Interpretation
- Alteogen is a strong platform royalty Stage 2, but Green waits for launch adoption, royalty/supply revenue and patent durability.
- Yuhan/lazertinib is global approval Stage 2, not Stage 3 until royalty, milestone and prescription uptake are visible.
- Samsung Biologics has good U.S. CDMO evidence but immediate price confirmation failed.
- Celltrion and SK Bioscience need product transfer, utilization, backlog, margin and FCF before Green.
- HanAll/Immunovant partner trial failure is RedTeam 4C-watch, not a forced hard 4C for the whole company.
- Lunit external validation is useful but reimbursement, hospital adoption and recurring revenue decide promotion.
- Biopharma tariff policy is event relief, not company-level Green.
