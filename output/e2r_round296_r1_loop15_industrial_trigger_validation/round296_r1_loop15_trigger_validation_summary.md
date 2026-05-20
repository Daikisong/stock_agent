# Round 296 R1 Loop 15 Industrial Trigger-Level Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_296.md
- round_id: round_224
- large_sector: INDUSTRIALS_ORDERS_INFRASTRUCTURE
- method: trigger_level_backtest_v1
- cases: 7
- triggers: 9
- Stage2 promote candidates: 7
- Stage3-Yellow candidates: 4
- Stage3-Green confirmed: 0
- 4B watch cases: 4
- legal 4C watch cases: 1
- price_validation_completed: partial_with_reported_event_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | best trigger | candidate | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|
| r1_loop15_hyundai_rotem_k2_poland | Hyundai Rotem | T2/T3 | Stage3-Yellow |  |  | missed_structural_risk | Shipment, OP estimate beat, revenue contribution and relative strength make this stronger than plain Stage 2. |
| r1_loop15_lig_nex1_msam | LIG Nex1 | T3 | Stage2-Actionable | 2024-07-02 |  | Stage2_promote_candidate_with_4B_overlay | 4B was valid as a trim signal, but repeat export orders kept the pipeline alive. |
| r1_loop15_hanwha_aerospace_k9_backlog_dilution | Hanwha Aerospace | T1/T2 | Stage3-Yellow + 4B-watch | 2025-03-21 | 2025-03-27 | aligned_if_stage3_plus_4b_overlay_allowed | Order/backlog can be Stage3-Yellow; dilution is 4B overlay, not Stage3 cancellation. |
| r1_loop15_shipbuilding_order_price_basket | Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy / HD Hyundai Mipo | T1/T2 | Stage2-Actionable_to_Stage3-Yellow | 2025-08-27 |  | Stage2_promote_candidate | Order momentum, newbuilding price index, backlog duration and broad relative strength should not remain plain Stage 2. |
| r1_loop15_ls_electric_us_grid | LS Electric | T2_pending_full_ohlc | Stage2_promote_candidate |  |  | inconclusive_but_promote_candidate | Immediate price failed, but structural U.S. grid trigger needs full-window retest before rejection. |
| r1_loop15_samsung_ena_fadhili | Samsung E&A | T1/T2 | Stage3-Yellow | 2024-04-03 |  | Stage2_promote_candidate | Mega-order plus relative strength and target upside supports Stage3-Yellow, not Green. |
| r1_loop15_czech_nuclear_doosan | Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E | T0/T1_if_preferred_bidder_probability_scored | Stage2-Actionable_with_legal_watch |  | 2025-05-06 | event_premium_legal_4C_watch | Preferred bidder is Stage2-Actionable at most; final contract and legal clearance are required for Green. |

## Interpretation
- Hyundai Rotem is the clearest missed-structural risk: shipment, OP estimate beat, revenue contribution and relative strength appeared together.
- LIG Nex1 shows 4B can be a trim signal rather than a hard exit when new order pipeline remains.
- Hanwha Aerospace needs Stage3-Yellow plus dilution 4B overlay, not Stage3 cancellation.
- Shipbuilding basket moves beyond plain Stage2 when orders, pricing, backlog duration and sector relative strength align.
- LS Electric needs full-window retest because immediate price failed despite strong U.S. grid evidence.
- Samsung E&A supports Stage3-Yellow, but EPC cash, working capital and completion margin block Green.
- Czech nuclear remains Stage2 plus legal 4C-watch until final contract and legal clearance.
