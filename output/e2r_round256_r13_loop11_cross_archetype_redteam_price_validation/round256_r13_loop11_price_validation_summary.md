# Round 256 R13 Loop 11 Cross-Archetype RedTeam Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_256.md
- analyst_round_id: round_184
- large_sector: CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION
- cases: 8
- structural_success: 2
- success_candidate: 1
- failed_rerating: 1
- overheat: 1
- hard_4c_case_count: 3
- Stage 3 dated cases: 2
- 4B-watch cases: 4
- price_moved_without_evidence: 2
- deep_sub_archetype_count: 9
- shadow_weight_row_count: 9
- r13_default_stage3_bias: redteam_first_after_price_validation
- full_ohlc_complete: false

## Case Matrix

| case | company | source | type | stage3 | 4B | 4C | round alignment | note |
|---|---|---|---|---|---|---|---|---|
| r13_loop11_sk_hynix_hbm_structural_success_4b_watch | SK하이닉스 | R2 | structural_success | 2024-06-25 | 2026-05-04 |  | aligned | Loop 11 전체의 Stage 3 성공 benchmark다. 다만 5배 이상 MFE 이후에는 신규 Green이 아니라 4B-watch다. |
| r13_loop11_apr_medicube_structural_concentration_4b | APR / Medicube | R5 | structural_success | 2025-10-01 | 2025-10-01 |  | aligned_partial | 실제 sell-through와 해외매출이 찍힌 구조 후보지만 Medicube 매출집중도 91.7% 때문에 4B-watch를 동시에 올린다. |
| r13_loop11_samsung_ea_fadhili_contract_stage2_4b | Samsung E&A Fadhili | R1/R10 | success_candidate |  | 2024-04-03 |  | event_premium_success_candidate | 약 $6B 수주는 강한 Stage 2지만, 공정률·마진·현금회수 전에는 Stage 3-Green이 아니다. |
| r13_loop11_samsung_sds_stablecoin_ai_digital_event_premium | Samsung SDS + KRW stablecoin basket | R6/R8 | overheat |  | 2026-04-15 |  | price_moved_without_evidence_event_premium | AI 자본조달과 stablecoin 정책은 Stage 2/1 신호가 될 수 있지만, 매출 전 +20~200%는 Green이 아니라 4B다. |
| r13_loop11_lg_cns_samsung_biologics_good_evidence_price_failed | LG CNS + Samsung Biologics | R7/R8 | failed_rerating |  |  |  | evidence_good_but_price_failed | 좋은 사업 evidence가 있어도 가격 반응이 실패하면 fresh rerating 축을 낮추고 Green threshold를 낮추지 않는다. |
| r13_loop11_lges_lnf_contract_quality_hard_4c | LGES / L&F contract-quality hard 4C | R3/R4 | 4c_thesis_break |  |  | 2025-12-29 | thesis_break | 고객명·계약금액 headline은 actual call-off, volume, take-or-pay, margin, cash collection 없이는 Green이 아니다. |
| r13_loop11_skt_kumho_operational_trust_hard_4c | SK Telecom / Kumho Tire operational trust hard 4C | R8/R9 | 4c_thesis_break |  |  | 2025-04-28 | thesis_break | 보안·공장·안전·품질 사고는 일반 RedTeam이 아니라 매출성장 점수보다 먼저 보는 hard gate다. |
| r13_loop11_hormuz_iran_macro_hard_4c | Hormuz / Iran macro energy shock | R11 | 4c_thesis_break |  |  | 2026-03-04 | thesis_break | Hormuz/energy/FX shock은 sector-neutral 악재가 아니라 한국 시장 전체에 덮는 macro hard gate다. |

## Interpretation
- SK Hynix and APR/Medicube are aligned structural-success benchmarks, but both need 4B-watch after major rerating.
- Samsung E&A is signed-contract Stage 2, not Green, until progress revenue, margin, and cash collection close.
- Samsung SDS and the stablecoin basket are event premium / price_moved_without_evidence before recurring AI or regulated revenue.
- LG CNS and Samsung Biologics show that good evidence with weak price response should not lower Green gates.
- LGES/L&F and SKT/Kumho are hard 4C anchors for contract quality and operational trust.
- Hormuz/Iran is a macro hard 4C overlay across energy, FX, autos, chips, airlines, and the broad market.
