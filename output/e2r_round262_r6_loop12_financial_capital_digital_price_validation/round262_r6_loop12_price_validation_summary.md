# Round 262 R6 Loop 12 Financial Capital Digital Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_262.md
- round_id: round_190
- large_sector: FINANCIAL_CAPITAL_DIGITAL
- cases: 8
- success_candidate: 5
- cyclical_success: 1
- overheat: 1
- watch_cases: 1
- hard_4c: 0
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r6_loop12_financial_holdings_valueup_stage2 | Korean financial holding value-up basket | success_candidate / Stage 2, not Green | 2026-02-25 |  | 2026-05-06 |  | success_candidate | Value-up policy and sector rally are Stage 2; ROE/CET1/credit cost and actual recurring shareholder return are required before Green. |
| r6_loop12_securities_market_volume_cycle | Korean securities firms basket | cyclical_success + 4B-watch | 2026-05-06 |  | 2026-05-06 |  | cyclical_success | Securities +13.5% is cyclical success and 4B-watch until brokerage/IB revenue and ROE confirm. |
| r6_loop12_samsung_life_nav_capital_release | Samsung Life | success_candidate + regulatory_watch | 2026-03-19 |  |  |  | success_candidate_regulatory_watch | Capital release is Stage 2; K-ICS, CSM, dividend/buyback and use of proceeds are required before Green. |
| r6_loop12_hana_bank_dunamu_equity_option | Hana Financial / Hana Bank / Dunamu | success_candidate / regulated digital-asset equity option | 2026-05-14 |  | 2026-05-14 |  | success_candidate | Dunamu stake is Stage 2; regulated revenue, equity-method earnings, capital impact and exchange trust are required before Green. |
| r6_loop12_naver_dunamu_platform_merger_trust_watch | NAVER / NAVER Financial / Dunamu | success_candidate + event_premium + 4C-watch | 2025-11-27 |  | 2025-11-27 | 2025-11-27 | event_premium_trust_watch | Digital-asset platform Stage 2, but abnormal withdrawal creates exchange-trust 4C-watch. |
| r6_loop12_toss_facepay_fintech_superapp_privacy_watch | Toss / Viva Republica / FacePay | success_candidate + privacy_watch | 2025-09-09 |  | 2026-05-01 |  | success_candidate_unlisted | Biometric payment is Stage 2; take-rate, credit cost, privacy/data compliance and IPO pricing are required. |
| r6_loop12_kakao_kakaobank_governance_gate | Kakao / KakaoBank | 4C-watch / governance gate |  |  |  | 2024-07-22 | thesis_break_watch | KakaoBank Green is blocked by major-shareholder legal and bank-ownership suitability risk. |
| r6_loop12_stablecoin_policy_overheat_fx_gate | Stablecoin policy basket / FX gate | overheat + 4C-watch |  |  | 2025-06-01 | 2025-06-30 | price_moved_without_evidence + FX_4C_watch | Stablecoin policy rally happened before regulated revenue, while FX outflow risk remains 4C-watch. |

## Interpretation
- Financial value-up is Stage 2 until ROE, capital buffers, credit cost, and actual return execution confirm.
- Securities are cyclical success when market volume jumps before brokerage and IB earnings proof.
- Bank or platform digital-asset exposure must pass regulated revenue, equity-method income and trust gates.
- Toss FacePay is unlisted Stage 2 with biometric privacy/data gates.
- KakaoBank governance and stablecoin FX outflow are 4C-watch, not Green evidence.
