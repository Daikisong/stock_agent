# Round 283 R1 Loop 14 Industrials Orders Infrastructure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_283.md
- round_id: round_211
- large_sector: INDUSTRIALS_ORDERS_INFRASTRUCTURE
- cases: 8
- Stage 3 dated candidates: 1
- stage4b_watch: 4
- stage4c_watch: 2
- hard_4c: 1
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r1_loop14_hyundai_rotem_k2_poland_delivery_stage3_candidate | Hyundai Rotem K2 Poland delivery | aligned_partial Stage 3 candidate | 2025-08-01 | 2024-04-01 |  |  | aligned_partial | Delivery/revenue/OP evidence supports a Stage 3 candidate; financing, local production and margin remain gates. |
| r1_loop14_ls_electric_us_grid_growth_price_failed | LS Electric US grid growth | evidence_good_but_price_failed | 2024-07-01 |  |  |  | evidence_good_but_price_failed | US grid growth is Stage 2 evidence, but actual backlog, capacity, margin and working capital must close. |
| r1_loop14_hyosung_heavy_hico_transformer_capacity | Hyosung Heavy / Hyosung HICO transformer capacity | success_candidate, price unavailable | 2025-12-02 |  |  |  | success_candidate_but_price_data_unavailable | Capacity expansion and shortage are Stage 2; backlog, utilization, ASP/margin and price path must be backfilled. |
| r1_loop14_hd_hhi_mipo_merger_masga_4b | HD Hyundai Heavy / HD Hyundai Mipo merger MASGA | event premium + 4B-watch | 2025-08-27 |  | 2025-08-27 |  | event_premium_4B_watch | Merger/MASGA can be Stage 2 and 4B-watch, not Green before funded orders and synergy. |
| r1_loop14_samsung_heavy_zvezda_cancellation_hard_4c | Samsung Heavy Zvezda cancellation | hard 4C / order cancellation | 2020-01-01 |  |  | 2025-06-18 | thesis_break | Backlog execution failed; large cancellation and sanctions/arbitration risk are hard 4C gates. |
| r1_loop14_hanwha_aerospace_share_sale_dilution | Hanwha Aerospace share-sale dilution | false_positive_score + 4B-watch | 2025-04-18 |  | 2025-03-21 | 2025-03-27 | false_positive_score | Defense order cycle must be dilution-adjusted; FSS filing-quality gate remains part of RedTeam. |
| r1_loop14_rainbow_robotics_samsung_stake_event | Rainbow Robotics Samsung stake event | robotics event premium | 2024-12-30 |  |  |  | event_premium | Strategic stake is Stage 2 optionality; shipment, ASP, deployment, margin and repeat demand are Green gates. |
| r1_loop14_hd_hyundai_marine_ipo_overheat | HD Hyundai Marine Solution IPO overheat | industrial-service IPO overheat | 2024-05-08 |  | 2024-05-08 |  | success_candidate_but_overheat | Good industrial-service business, but +97% IPO debut is a 4B-watch until post-IPO earnings durability and lock-up/PE exit pressure clear. |

## Interpretation
- Hyundai Rotem is the aligned partial Stage 3 candidate because delivery, revenue, OP estimate and price reaction line up.
- LS Electric and Hyosung Heavy/HICO are Stage 2 lessons: grid evidence must still close into backlog, utilization, margin and price path.
- HD HHI/Mipo, Rainbow Robotics and HD Hyundai Marine are event-premium/4B-watch lessons before revenue or aftermarket proof.
- Samsung Heavy/Zvezda is the hard 4C lesson: cancelled backlog is not structural visibility.
- Hanwha Aerospace shows defense order growth must be checked against dilution-adjusted EPS and filing quality.
