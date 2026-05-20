# Round 249 R6 Loop 11 Financial Capital Digital Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_249.md
- round_id: round_177
- large_sector: FINANCIAL_CAPITAL_DIGITAL
- cases: 8
- success_candidate: 5
- cyclical_success: 1
- event_premium: 1
- overheat: 1
- hard_4c_confirmed: false
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r6_loop11_big4_financial_valueup_stage2 | KB/Shinhan/Hana/Woori financial groups | market_structure_stage2_not_green | 2026-02-25 |  | 2026-05-06 |  | success_candidate | Bank value-up is Stage 2; ROE/CET1/credit cost and repeated shareholder return required before Green. |
| r6_loop11_securities_capital_market_boom | Korean securities firms basket | cyclical_success_4B-watch | 2026-05-06 |  | 2026-05-06 |  | cyclical_success | Securities rally is Stage 2/cyclical and 4B-watch; brokerage/IB revenue and ROE required before Green. |
| r6_loop11_sk_square_nav_discount_valueup | SK Square | NAV_discount_valueup_stage2 | 2024-11-21 |  |  |  | success_candidate | Actual cancellation supports Stage 2; repeated cancellation and discount narrowing required for Stage 3. |
| r6_loop11_samsung_life_nav_capital_release | Samsung Life | success_candidate_regulatory_watch | 2026-03-19 |  |  |  | success_candidate_regulatory_watch | Capital release is Stage 2; use of proceeds, K-ICS/CSM and shareholder return required before Green. |
| r6_loop11_hana_dunamu_equity_option | Hana Financial / Hana Bank / Dunamu | regulated_digital_asset_equity_option_stage2 | 2026-05-14 |  |  |  | success_candidate | Dunamu stake is Stage 2; regulated revenue, equity-method earnings, capital impact and exchange trust required for Stage 3. |
| r6_loop11_naver_dunamu_platform_merger_trust_watch | NAVER / NAVER Financial / Dunamu | success_candidate_event_premium_4C-watch | 2025-11-27 |  | 2025-11-27 | 2025-11-27 | event_premium_trust_watch | Strong Stage 2 digital-asset merger, but abnormal withdrawal creates exchange-trust 4C-watch. |
| r6_loop11_internet_bank_kbank_kakaobank_watch | K Bank / KakaoBank / Kakao | success_candidate_governance_4C_watch | 2024-09-10 |  |  | 2024-07-23 | success_candidate_for_KBank_thesis_break_watch_for_KakaoBank | K Bank is unlisted Stage 2; KakaoBank Green is blocked by major shareholder legal/ownership risk. |
| r6_loop11_stablecoin_policy_theme_overheat | Kakao Pay / stablecoin policy basket | overheat_price_moved_without_evidence |  |  | 2025-06-01 |  | price_moved_without_evidence | Stablecoin theme rallied before licensed issuer, reserve income, fee revenue or regulatory capital clarity. |

## Interpretation
- Big-4 financial groups value-up is Stage 2, not Green, until ROE/CET1/credit cost and repeated return execution confirm.
- Securities +13.5% is cyclical Stage 2 and 4B-watch before brokerage/IB revenue proof.
- SK Square and Samsung Life are NAV/capital-release Stage 2 cases, not Green without monetization/use-of-proceeds proof.
- Hana/Dunamu and NAVER/Dunamu are digital-asset Stage 2 cases with regulated-revenue and trust gates.
- K Bank is unlisted profitability Stage 2, while KakaoBank has major-shareholder governance 4C-watch.
- Stablecoin basket is price_moved_without_evidence until issuer license, reserve income, fee revenue and regulatory capital are confirmed.
