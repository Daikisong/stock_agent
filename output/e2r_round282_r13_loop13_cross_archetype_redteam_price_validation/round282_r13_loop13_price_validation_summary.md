# Round 282 R13 Loop 13 Cross-Archetype RedTeam Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_282.md
- round_id: round_210
- large_sector: CROSS_ARCHETYPE_REDTEAM_4B_ACCOUNTING_TRUST_PRICE_VALIDATION
- cases: 8
- hard_4c: 3
- Stage 3 dated cases: 0
- stage4b_watch: 3
- stage4c_watch: 6
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r13_loop13_skt_cybersecurity_hard_4c | SK Telecom data breach hard 4C | hard 4C / cybersecurity trust break |  |  |  | 2025-04-28 | thesis_break | Data trust break must outrank telecom demand or dividend narratives. |
| r13_loop13_jeju_air_safety_hard_4c | Jeju Air fatal crash hard 4C | hard 4C / aviation safety |  |  |  | 2024-12-30 | thesis_break | Fatal aviation accident is a hard gate for airline and travel recovery narratives. |
| r13_loop13_lnf_tesla_contract_collapse | L&F Tesla 4680 cathode contract collapse | hard 4C / contract value collapse | 2023-02-01 |  |  | 2025-12-29 | thesis_break | Named-customer supply deal must not become Green without call-off, shipment and revenue recognition. |
| r13_loop13_naver_dunamu_upbit_trust_4c_watch | Naver Financial / Dunamu / Upbit trust watch | event premium + 4C-watch | 2025-11-27 |  | 2025-11-27 | 2025-11-27 | event_premium_trust_watch | Digital-asset M&A must clear custody, withdrawal, reserve and regulatory trust gates. |
| r13_loop13_lg_cns_ipo_quality_false_positive | LG CNS AI/cloud IPO weak debut | IPO quality false positive | 2025-02-05 |  |  |  | evidence_good_but_price_failed | IPO size and AI/cloud exposure need post-listing demand, margin and FCF validation. |
| r13_loop13_korea_zinc_control_premium_dilution_4b | Korea Zinc control premium / dilution watch | 4B-watch + governance dilution watch | 2024-09-13 |  | 2024-09-13 | 2024-10-31 | event_premium_4B_watch | Control premium can be a 4B/watch event, not an operating Green source. |
| r13_loop13_samsung_ea_fadhili_order_not_margin_green | Samsung E&A Fadhili mega-order margin gate | success_candidate + order-headline 4B-watch | 2024-04-03 |  | 2024-04-03 |  | event_premium_success_candidate | Mega order can enter Stage 2/watch, but not Green until margin and cash collection are proven. |
| r13_loop13_hyundai_motor_india_ipo_failed_rerating | Hyundai Motor India IPO failed parent rerating | capital recycling IPO failed rerating | 2024-10-14 |  |  | 2024-10-22 | evidence_good_but_price_failed | Capital recycling IPO needs parent ROIC/FCF and post-listing demand before rerating claims. |

## Interpretation
- SK Telecom and Jeju Air are hard trust/safety 4C examples.
- L&F/Tesla shows customer-name contracts need actual call-off and revenue conversion.
- Digital-asset M&A, IPOs, control premiums, and mega-orders can be 4B/watch or Stage 2, not automatic Green.
- Full adjusted OHLC is still missing; reported event anchors are stored separately from invented MFE/MAE.
