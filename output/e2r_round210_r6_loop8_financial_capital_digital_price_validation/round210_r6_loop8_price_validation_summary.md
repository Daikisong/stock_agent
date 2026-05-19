# Round 210 R6 Loop 8 Financial Capital Digital Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_210.md
- large_sector: FINANCIAL_CAPITAL_DIGITAL
- cases: 7
- success_candidate: 3
- event_premium: 1
- overheat: 1
- failed_rerating: 1
- 4c_thesis_break: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- hard_4c_case_count: 2
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage2 | stage3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r6_loop8_sk_square_valueup_nav_discount | SK스퀘어 | success_candidate | 2024-11-21 |  | 2026-05-14 |  | unknown | Actual cancellation supports Stage 2; Stage 3 requires repeated cancellation and NAV discount narrowing in the price path. |
| r6_loop8_hana_dunamu_equity_option | 하나금융지주/하나은행 | success_candidate | 2026-05-14 |  |  |  | unknown | Dunamu stake is a regulated digital-asset Stage 2 option; Stage 3 needs earnings contribution, capital impact, and regulatory clarity. |
| r6_loop8_samsung_life_nav_valueup | 삼성생명 | success_candidate | 2026-03-19 |  |  |  | unknown | Hidden NAV and book discount support Stage 2; use of proceeds, K-ICS/CSM, and shareholder return are required for Stage 3. |
| r6_loop8_naver_dunamu_digital_asset_event | 네이버/네이버파이낸셜 | event_premium | 2025-11-27 |  | 2025-11-27 | 2025-11-27 | price_moved_without_evidence | The Dunamu transaction is strong Stage 2/event material, but abnormal withdrawal creates exchange-trust 4C-watch before Green. |
| r6_loop8_kakaobank_kakao_governance_watch | 카카오뱅크/카카오 | failed_rerating |  |  |  | 2024-07-23 | false_positive_score | For KakaoBank, major-shareholder legal risk and bank ownership caps come before internet-bank growth scoring. |
| r6_loop8_stablecoin_theme_overheat | Kakao Pay/LG CNS/Aton/ME2ON | overheat |  |  | 2025-06-01 |  | price_moved_without_evidence | Stablecoin policy theme moved before licensing, reserve income, fee revenue, or capital rules; this is 4B/event premium. |
| r6_loop8_kakao_pay_privacy_4c_watch | 카카오페이 | 4c_thesis_break |  |  |  | 2025-04-01 | false_positive_score | Payment fintech Green should be blocked by privacy/data-transfer trust break even when payment-volume narratives look attractive. |

## Interpretation
- SK Square, Hana, and Samsung Life are Stage 2 candidates until capital execution and price-path proof improve.
- Naver/Dunamu is digital-asset Stage 2/event material with exchange-trust 4C-watch.
- Stablecoin basket rallies are price-moved-without-evidence until licensing, reserve income, fee revenue, and capital rules exist.
- KakaoBank/Kakao and Kakao Pay privacy cases show governance and data trust can block Green before growth scoring matters.
