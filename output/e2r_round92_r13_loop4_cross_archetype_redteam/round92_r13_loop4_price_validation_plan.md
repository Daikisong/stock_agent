# Round-92 R13 Loop-4 Price / Stage Validation Plan

## Method

1. Assign Stage 1/2/3/4B/4C dates only from dated evidence.
2. Store stage-date close prices from official price data.
3. Calculate MFE_5D / 20D / 30D / 60D / 90D / 180D / 1Y / 2Y.
4. Calculate MAE_5D / 20D / 30D / 60D / 90D / 180D / 1Y.
5. Compare score-before-RedTeam vs score-after-RedTeam and stage-before-RedTeam vs stage-after-RedTeam.

## Priority Case Checks

| case_id | target | stage marker | check |
| --- | --- | --- | --- |
| `sk_hynix_hbm_memory_structural_4b_watch_case` | `STRUCTURAL_SUCCESS_ALIGNED` | 2026-05-14 | needs_price_backfill |
| `hyundai_motor_valueup_strategy_aligned_case` | `STRUCTURAL_SUCCESS_ALIGNED` | 2024-08-28 | needs_price_backfill |
| `korea_buyback_cancellation_policy_to_execution_case` | `EVENT_TO_CONTRACT_ESCALATION` | 2026-02-25 | needs_price_backfill |
| `circle_regulated_stablecoin_infra_4b_watch_case` | `SECTOR_SUCCESS_BUT_4B_WATCH` | 2026-05-11 | needs_price_backfill |
| `event_to_contract_escalation_reference_case` | `EVENT_TO_CONTRACT_ESCALATION` | undated | needs_price_backfill |
| `korea_ai_tax_policy_market_shock_case` | `POLICY_MARKET_SHOCK_EVENT` | 2026-05-12 | needs_price_backfill |
| `supermicro_accounting_trust_4c_case` | `REDTEAM_ACCOUNTING_TRUST_OVERLAY` | 2024-10-30 | needs_price_backfill |
| `crowdstrike_operational_trust_break_case` | `OPERATIONAL_TRUST_BREAK` | 2024-07-31 | needs_price_backfill |
| `terrausd_luna_algorithmic_stablecoin_break_case` | `STABLECOIN_CONVERTIBILITY_RISK` | 2022-05-12 | needs_price_backfill |
| `bluebird_bio_commercialization_failure_case` | `COMMERCIALIZATION_FAILURE` | 2025-02-21 | needs_price_backfill |
| `novo_nordisk_glp1_4b_to_4c_case` | `SECTOR_SUCCESS_BUT_4B_WATCH` | 2026-02-04 | needs_price_backfill |
| `equinix_affo_cashflow_integrity_case` | `AFFO_CASHFLOW_INTEGRITY_RISK` | 2024-03-20 | needs_price_backfill |
| `equinix_capex_affo_dilution_case` | `CAPEX_AFFO_DILUTION_RISK` | 2026-05-08 | needs_price_backfill |
| `opendart_disclosure_confidence_cap_reference_case` | `DISCLOSURE_CONFIDENCE_CAP` | undated | needs_price_backfill |
| `price_only_theme_rally_case` | `PRICE_ONLY_RALLY` | undated | needs_price_backfill |
| `event_premium_policy_mou_case` | `EVENT_PREMIUM` | undated | needs_price_backfill |
| `cyclical_success_peak_normalization_case` | `CYCLICAL_SUCCESS` | undated | needs_price_backfill |
| `false_positive_score_high_score_failure_case` | `FALSE_POSITIVE_SCORE` | undated | needs_price_backfill |
| `evidence_good_but_price_failed_case` | `EVIDENCE_GOOD_BUT_PRICE_FAILED` | undated | needs_price_backfill |
| `legal_regulatory_redteam_denial_case` | `LEGAL_REGULATORY_REDTEAM` | undated | needs_price_backfill |
| `leverage_fcf_breakdown_reference_case` | `LEVERAGE_FCF_BREAKDOWN` | undated | needs_price_backfill |
| `unknown_insufficient_evidence_case` | `UNKNOWN_INSUFFICIENT_EVIDENCE` | undated | needs_price_backfill |

## Alignment Labels

- `aligned`: EPS/FCF, structural evidence, and price path validate together.
- `price_moved_without_evidence`: price or event moved first, but EPS/FCF evidence is absent.
- `evidence_good_but_price_failed`: evidence looked valid, but price/valuation frame did not confirm.
- `false_positive_score`: model score was high but earnings, price, or RedTeam later invalidated it.
- `thesis_break`: 4C evidence such as audit, trust, legal, cash runway, commercialization, AFFO, or convertibility break appears.
- `disclosure_confidence_capped`: contract/list evidence exists, but core detail is missing, so Stage 3 confidence is capped.
