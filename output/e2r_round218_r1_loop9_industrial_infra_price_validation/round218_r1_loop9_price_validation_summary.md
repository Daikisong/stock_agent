# Round 218 R1 Loop 9 Industrial Infra Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_218.md
- large_sector: INDUSTRIAL_ORDERS_INFRA
- cases: 7
- success_candidate: 4
- 4B watch cases: 5
- 4C watch cases: 2
- overheat: 1
- hard_4c: 0
- price_moved_without_evidence: 2
- evidence_good_but_price_failed: 1
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C-watch | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r1_loop9_ls_electric_us_grid_watch | LS ELECTRIC | success_candidate | 2024-07-01 |  |  |  | evidence_good_but_price_failed | 미국 grid/data-center 성장 근거는 좋지만 보도 시점 가격이 빠졌다. Green은 회사별 주문·마진·FCF와 이후 가격경로 확인 뒤다. |
| r1_loop9_k_transformer_bottleneck_basket | HD현대일렉트릭/효성중공업 | success_candidate | 2026-05-11 |  |  |  | unknown | 미국 transformer shortage는 강한 Stage 2 sector evidence다. 다만 회사별 order/margin/FCF와 가격경로 전 Stage 3는 보류한다. |
| r1_loop9_samsung_ea_fadhili_epc | 삼성E&A | success_candidate | 2024-04-03 |  | 2024-04-03 |  | aligned | Fadhili $6B 계약은 좋은 Stage 2 사례다. Stage 3는 EPC margin, progress revenue, cash collection 확인 뒤다. |
| r1_loop9_doosan_czech_nuclear_policy_to_contract | 두산에너빌리티 | success_candidate | 2025-06-04 |  | 2024-07-17 | 2025-05-06 | unknown | 체코 원전은 preferred bidder에서 final contract로 일부 검증됐다. 두산 장비 수주잔고·마진·EPS revision 전 Green은 아니다. |
| r1_loop9_hd_hyundai_heavy_mipo_masga_event | HD현대중공업/HD현대미포 | 4b_watch | 2025-08-27 |  | 2025-08-27 |  | price_moved_without_evidence | MASGA·합병 이벤트는 Stage 2 + 4B-watch다. funded U.S. order와 margin 전 Stage 3는 금지다. |
| r1_loop9_hanwha_ocean_china_sanction_watch | 한화오션 | failed_rerating |  |  |  | 2025-10-14 | unknown | 한화오션은 hard 4C가 아니라 4C-watch다. 실제 매출·수주·공급 차질이 확인되면 hard 4C로 승격한다. |
| r1_loop9_hd_hyundai_marine_solution_ipo_premium | HD현대마린솔루션 | overheat | 2024-05-08 |  | 2024-05-08 |  | price_moved_without_evidence | 좋은 MRO 구조일 수 있지만 IPO 첫날 +96.5%는 Stage 3가 아니라 4B/event premium이다. |

## Interpretation
- LS Electric은 미국 grid evidence가 좋지만 보도 시점 가격이 빠져 `evidence_good_but_price_failed`다.
- Transformer basket은 sector bottleneck은 강하지만 회사별 주문·마진·FCF 전 Stage 2다.
- 삼성E&A와 두산에너빌리티는 큰 계약/정책-to-contract가 있으나 margin과 장비 backlog 전 Green은 보류한다.
- HD현대중공업/미포와 HD현대마린솔루션은 event premium과 4B-watch를 분리한다.
- 한화오션은 sanction event를 hard 4C가 아닌 4C-watch로 기록한다.
