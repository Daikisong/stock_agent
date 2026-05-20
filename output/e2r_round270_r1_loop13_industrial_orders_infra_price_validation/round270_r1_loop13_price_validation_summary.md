# Round 270 R1 Loop 13 Industrial Orders / Infrastructure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_270.md
- round_id: round_198
- large_sector: INDUSTRIAL_ORDERS_INFRA
- cases: 8
- success_candidate: 5
- cyclical_success: 1
- overheat: 1
- hard_4c_case_count: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- 4C watch/hard cases: 2
- price_data_unavailable: 2
- price_moved_without_evidence: 3
- target_archetype_count: 8
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r1_loop13_hd_hyundai_heavy_mipo_masga_merger | HD Hyundai Heavy Industries / HD Hyundai Mipo | success_candidate | 2025-08-27 |  | 2025-08-27 |  | success_candidate_4B_watch | 합병과 MASGA는 강한 Stage 2지만 실제 U.S. award, 통합 시너지, 마진, FCF 전에는 Green이 아니다. |
| r1_loop13_hanwha_ocean_us_mro_china_sanction_watch | Hanwha Ocean | success_candidate | 2025-04-28 |  | 2025-04-28 | 2025-10-14 | success_candidate_with_geopolitical_4C_watch | U.S. MRO option은 좋지만 중국 제재가 열려 있어 Green이 아니라 4C-watch를 병행한다. |
| r1_loop13_samsung_heavy_zvezda_cancellation_hard_4c | Samsung Heavy Industries | 4c_thesis_break |  |  |  | 2025-06-18 | thesis_break | 수주금액이 커도 제재·상대방·인도 가능성이 깨지면 hard 4C다. |
| r1_loop13_hyundai_rotem_morocco_oncf_rail_order | Hyundai Rotem | success_candidate | 2025-02-26 |  |  |  | success_candidate | 철도 대형 수주는 좋은 Stage 2지만 납품·현지화·금융조건·마진·현금회수가 필요하다. |
| r1_loop13_hd_hyundai_marine_solution_ipo_aftermarket | HD Hyundai Marine Solution | overheat | 2024-05-08 |  | 2024-05-08 |  | success_candidate_but_4B_overheat | After-market 사업은 좋지만 IPO 첫날 +96.5%는 증거보다 가격이 먼저 간 4B다. |
| r1_loop13_rainbow_robotics_samsung_strategic_equity | Rainbow Robotics | success_candidate | 2024-12-30 |  |  |  | success_candidate_but_insufficient_price_data | 삼성 지분투자는 전략 option이지 로봇 매출이 아니다. 주문·매출·마진 확인 전 Green 금지다. |
| r1_loop13_kai_defense_aerospace_export_optionality | Korea Aerospace Industries | success_candidate | 2025-03-18 |  | 2025-03-18 |  | success_candidate_4B_watch | KAI는 방산 항공우주 option이지만 섹터 랠리만으로 회사별 Stage 3가 되지는 않는다. |
| r1_loop13_korean_shipbuilders_contract_cycle_4b | Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy broad shipbuilding basket | cyclical_success | 2024-03-14 |  | 2024-03-14 |  | cyclical_success_4B_watch | 조선 broad cycle은 긍정이지만 +11~16% 당일 급등은 개별 마진/현금 전환 전 4B-watch다. |

## Interpretation
- R1 Stage 3 is not an order, MOU, merger, IPO, policy cooperation, or sector rally headline.
- HD Hyundai Heavy/Mipo is Stage 2 plus 4B-watch: the merger/MASGA price move came before actual U.S. awards and FCF.
- Hanwha Ocean combines U.S. MRO option with China-sanction 4C-watch.
- Samsung Heavy Zvezda cancellation is the hard 4C reference case for contract quality.
- Hyundai Rotem Morocco is a strong rail-export Stage 2, but delivery/margin/cash collection remain open.
- HD Hyundai Marine shows recurring-service potential, but IPO +96.5% is 4B before durability proof.
- Rainbow Robotics is a strategic equity option, not robot revenue.
- KAI and the broad shipbuilding basket show sector optionality/cycle, not company-specific Green.
