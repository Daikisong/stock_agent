# Round-184 R13 Loop-11 RedTeam Gate Plan

| target | hard gate | stage3 allowed | red flags |
| --- | --- | --- | --- |
| `STRUCTURAL_STAGE3_EARLY_CAPTURE` | false | true | hard_redteam, crowded_4b, revision_down |
| `STAGE2_STRONG_NOT_GREEN` | false | false | stage3_evidence_missing, conversion_missing, detail_missing |
| `EVENT_PRICE_RALLY_NOT_STAGE3` | true | false | price_only, no_eps_fcf, no_contract, event_only |
| `STRUCTURAL_SUCCESS_BUT_4B_WATCH` | false | false | crowding, valuation_saturation, revision_slowdown |
| `CYCLE_SUCCESS_NOT_STRUCTURAL` | false | false | cycle_normalization, new_supply, spot_reversal |
| `DISCLOSURE_CONFIDENCE_CAP` | false | false | media_only, mou_loi, non_binding, detail_missing |
| `PRIVATE_OR_HOLDCO_LINK_CAP` | false | false | holdco_link_missing, security_risk, regulatory_risk |
| `OPERATIONAL_TRUST_HARD_4C` | true | false | fatal_accident, cyber_incident, safety, quality, ransomware |
| `LEGAL_GOVERNANCE_4C_WATCH` | true | false | founder_legal, management_legal, lawsuit, governance |
| `POLICY_MARKET_SHOCK_OVERLAY` | true | false | policy_market_shock, risk_premium, valuation_compression |

## What Not To Change

- Do not apply Round184 overlay weights to production scoring yet.
- Do not use case records as candidate-generation input.
- Do not convert event rallies, private asset value, media reports, MOU, LOI, or non-binding terms into Stage 3 evidence.
- Do not invent stage prices, MFE/MAE, customer names, contract amounts, durations, royalties, ARR, AFFO, prescription volume, or FCF signals.
- Hard 4C gates such as PF workout, fatal accident, cyber incident, legal overhang, policy shock, and contract cancellation block Green.
