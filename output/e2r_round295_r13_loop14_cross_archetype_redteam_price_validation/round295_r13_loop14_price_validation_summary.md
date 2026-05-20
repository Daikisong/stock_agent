# Round 295 R13 Loop 14 Cross-archetype RedTeam Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_295.md
- round_id: round_223
- large_sector: CROSS_ARCHETYPE_REDTEAM_4B_ACCOUNTING_TRUST_PRICE_VALIDATION
- cases: 8
- 4B watch cases: 4
- 4C watch cases: 5
- hard 4C cases: 2
- price_moved_without_evidence: 2
- false_positive_score: 5
- evidence_good_but_price_failed: 1
- price_validation_completed: partial_with_reported_event_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r13_loop14_hanwha_aerospace_backlog_dilution_4b | Hanwha Aerospace | overheat / false_positive_score / 4B-watch |  |  | 2025-03-21 | 2025-03-27 | false_positive_score | Order backlog and geopolitical premium must be adjusted for dilution and disclosure quality. |
| r13_loop14_lnf_tesla_signed_contract_collapse_hard_4c | L&F | hard_4C | 2023-02-01 |  |  | 2025-12-29 | thesis_break | Customer-name and signed contract amount are not Green without actual call-off or revenue recognition. |
| r13_loop14_kogas_blue_whale_resource_event_premium | Korea Gas / Daesung Energy / SK Innovation / SK Gas | price_moved_without_evidence |  |  | 2024-06-03 |  | price_moved_without_evidence | Resource estimate and presidential announcement moved price before drilling and economic viability. |
| r13_loop14_lg_cns_ai_cloud_ipo_false_positive | LG CNS | evidence_good_but_price_failed | 2025-02-05 |  | 2025-02-05 |  | evidence_good_but_price_failed | AI/cloud sales mix and IPO oversubscription failed aftermarket validation. |
| r13_loop14_samsung_ct_valueup_proposal_failure | Samsung C&T | false_positive_score |  |  |  | 2024-03-15 | false_positive_score | Value-Up proposal is not Green unless board adoption and cash-return execution occur. |
| r13_loop14_skt_data_trust_hard_4c | SK Telecom | hard_4C |  |  |  | 2025-04-28 | thesis_break | Data breach is not a one-off event when it changes revenue forecast, capex, compensation and contingent liability. |
| r13_loop14_hyundai_steel_us_localization_capex_false_positive | Hyundai Steel | false_positive_score |  |  |  | 2025-04-22 | false_positive_score | Localization capex needs funding clarity, IRR, customer demand and tariff-saving durability. |
| r13_loop14_korea_zinc_control_premium_4b | Korea Zinc / Young Poong / MBK | 4B-watch |  |  | 2024-09-13 |  | event_premium_4B_watch | Tender/control premium must be separated from operating cashflow, smelter margin and FCF. |

## Interpretation
- Hanwha Aerospace is a backlog-dilution 4B example: strong orders do not remove dilution math.
- L&F/Tesla is hard 4C: signed amount and customer name did not become actual call-off revenue.
- Korea Gas/Blue Whale is price moved without evidence: resource headline moved price before drilling and economics.
- LG CNS is an IPO quality gate: oversubscription did not survive aftermarket price validation.
- Samsung C&T separates Value-Up proposal from actual capital return execution.
- SK Telecom is data-trust hard 4C because the event affected revenue forecast, capex, compensation and liability.
- Hyundai Steel shows localization capex can be a funding/IRR risk, not automatic tariff hedge Green.
- Korea Zinc separates control premium from operating cashflow rerating.
