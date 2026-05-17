# Round-66 R13 Loop-2 RedTeam Gate Plan

| target | posture | hard gate | Green allowed | Red flags |
| --- | --- | --- | --- | --- |
| `STRUCTURAL_SUCCESS_ALIGNED` | GREEN_POSSIBLE | false | true | crowded_4b, valuation_saturation, revision_slowdown |
| `SECTOR_SUCCESS_BUT_4B_WATCH` | WATCH_YELLOW_FIRST | false | false | crowding, valuation_saturation, revision_slowdown, capacity_addition |
| `PRICE_ONLY_RALLY` | REDTEAM_FIRST | false | false | no_eps_fcf, no_contract, no_revenue, theme_only |
| `EVENT_PREMIUM` | WATCH_YELLOW_FIRST | false | false | mou_only, policy_only, event_only, deal_failure |
| `EVENT_TO_CONTRACT_ESCALATION` | WATCH_YELLOW_FIRST | false | false | mou_only, unfunded_policy, single_headline |
| `CYCLICAL_SUCCESS` | WATCH_YELLOW_FIRST | false | false | normalization_risk, new_supply, spot_price_reversal |
| `FALSE_POSITIVE_SCORE` | REDTEAM_FIRST | false | false | score_overfit, no_eps_fcf, price_failed, redteam_ignored |
| `EVIDENCE_GOOD_BUT_PRICE_FAILED` | WATCH_YELLOW_FIRST | false | false | price_failed, valuation_frame_stuck, liquidity_low |
| `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | REDTEAM_FIRST | true | false | auditor_resignation, filing_delay, internal_control_issue, related_party_risk |
| `OPERATIONAL_TRUST_BREAK` | REDTEAM_FIRST | true | false | security_outage, privacy_breach, customer_lawsuit, operational_trust_damage |
| `LEGAL_REGULATORY_REDTEAM` | REDTEAM_FIRST | true | false | lawsuit, regulatory_probe, approval_denial, license_risk |
| `LEVERAGE_FCF_BREAKDOWN` | REDTEAM_FIRST | true | false | negative_fcf, cash_runway, refinancing, dilution, dividend_cut |
| `COMMERCIALIZATION_FAILURE` | REDTEAM_FIRST | true | false | slow_uptake, reimbursement_failure, commercial_revenue_missing, cash_runway_collapse |
| `AFFO_CASHFLOW_INTEGRITY_RISK` | REDTEAM_FIRST | true | false | affo_integrity_risk, maintenance_capex, tenant_concentration, power_constraint |
| `STABLECOIN_CONVERTIBILITY_RISK` | REDTEAM_FIRST | true | false | depeg_event, reserve_failure, convertibility_risk, algorithmic_stablecoin_failure |
| `UNKNOWN_INSUFFICIENT_EVIDENCE` | REDTEAM_FIRST | false | false | missing_evidence, date_unverified, single_source, unknown |

## What Not To Change

- Do not apply Round66 overlay symbols to production scoring yet.
- Do not lower Stage 3-Green to improve recall.
- Do not use R13 Loop-2 case records as candidate-generation input.
- Do not treat price-only movement, event premium, or cycle success as structural Green by itself.
- Do not ignore hard RedTeam evidence such as auditor resignation, filing delay, global outage, regulatory denial, cash runway collapse, AFFO integrity risk, or stablecoin de-peg.
