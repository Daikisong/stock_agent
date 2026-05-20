# Round 275 R6 Loop 13 Financial Capital Digital Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_275.md
- round_id: round_203
- large_sector: FINANCIAL_CAPITAL_DIGITAL
- cases: 8
- success_candidate: 5
- event_premium: 2
- overheat: 1
- hard_4c: 1
- direct_listed_hard_4c: false
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r6_loop13_financial_holdings_valueup_sector_4b | KB / Shinhan / Hana / Woori financial holding basket | success_candidate + 4B-watch | 2024-05-02 |  | 2026-05-06 |  | success_candidate_4B_watch | Value-up and sector flow can be Layer 1/Stage 2, but not Green without bank-quality metrics. |
| r6_loop13_sk_square_holdco_discount_buyback | SK Square | structural_success_candidate | 2024-11-21 |  | 2024-11-21 |  | success_candidate | Buyback cancellation is stronger than headline value-up, but Green needs repeated execution and NAV durability. |
| r6_loop13_samsung_life_samsung_electronics_stake_regulatory_gate | Samsung Life Insurance | success_candidate + 4C-watch | 2026-03-19 |  | 2026-03-19 | 2026-03-19 | success_candidate_4C_watch | Affiliate stake value can be Stage 2, but regulation and use-of-proceeds uncertainty stay visible. |
| r6_loop13_hana_bank_dunamu_digital_asset_stake | Hana Financial Group / Hana Bank / Dunamu | success_candidate + 4B-watch | 2026-05-14 |  | 2026-05-14 |  | success_candidate_4B_watch | Dunamu stake can be an option, but bank EPS/FCF needs regulated revenue, capital and trust gates. |
| r6_loop13_naver_dunamu_fintech_ma_trust_gate | Naver Financial / Dunamu / Upbit | success_candidate + event_premium + 4C-watch | 2025-11-27 |  | 2025-11-27 | 2025-11-27 | event_premium_trust_watch | M&A premium is not Green while abnormal withdrawal and closing/regulatory gates remain unresolved. |
| r6_loop13_kbank_internet_bank_ipo_overhang | K Bank | event_premium_insufficient_evidence | 2024-09-10 |  | 2024-09-10 |  | event_premium_insufficient_evidence | Customer count and IPO valuation are not enough; credit quality, NIM and deposit concentration decide bank quality. |
| r6_loop13_stablecoin_policy_overheat_fx_gate | Stablecoin policy basket | overheat + 4C-watch |  |  | 2025-06-01 | 2025-06-01 | price_moved_without_evidence_FX_watch | Stablecoin basket is 4B/FX watch until issuer economics and FX stability are visible. |
| r6_loop13_bithumb_operational_error_hard_reference | Bithumb | hard_4C_reference |  |  |  | 2026-02-07 | thesis_break_reference | Operational control failure is a hard reference. It must feed RedTeam, not create digital-finance Green. |

## Interpretation
- Financial value-up is Stage 2 until CET1, ROE, NIM, credit cost, RWA and real capital return confirm.
- Holdco and insurance stake rerating need repeated execution, use of proceeds and capital buffer evidence.
- Digital-asset stakes and M&A must pass regulatory, earnings, exchange-trust and internal-control gates.
- Stablecoin and securities-volume baskets are 4B/event premium until regulated revenue or recurring fee evidence appears.
- Bithumb is a hard 4C reference, but not a direct listed-company hard 4C case.
