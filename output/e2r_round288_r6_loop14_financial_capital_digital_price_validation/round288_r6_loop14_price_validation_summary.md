# Round 288 R6 Loop 14 Finance Capital Digital Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_288.md
- round_id: round_216
- large_sector: FINANCE_CAPITAL_ALLOCATION_DIGITAL_FINANCE
- cases: 8
- Stage 3 dated candidates: 0
- stage4b_watch: 7
- stage4c_watch: 4
- hard_4c: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r6_loop14_financial_holding_value_up_policy_stage2 | KB / Shinhan / Hana / Woori financial holding basket | success_candidate_policy_stage2 | 2026-02-25 |  | 2026-02-25 |  | success_candidate_policy_stage2 | Value-Up law is Stage 2; financial holding Green requires CET1, payout/cancellation execution and credit-cost stability. |
| r6_loop14_sk_square_holdco_discount_buyback | SK Square | success_candidate_but_price_data_unavailable | 2024-11-21 |  | 2024-11-21 |  | success_candidate_but_price_data_unavailable | SK Square is Stage 2: cancellation is useful, but holdco-discount compression and governance execution are the proof. |
| r6_loop14_samsung_ct_activist_valueup_failure | Samsung C&T | false_positive_score | 2024-03-01 |  | 2024-03-15 | 2024-03-15 | false_positive_score | Samsung C&T is the clean false-positive guardrail: proposal failure is not shareholder-return execution. |
| r6_loop14_kbank_digital_bank_ipo_quality_gate | K Bank | success_candidate_IPO_quality_gate | 2024-09-10 |  | 2024-09-10 |  | success_candidate_IPO_quality_gate | K Bank is Stage 2 until listed aftermarket demand, NIM, funding cost, credit quality and CAC are visible. |
| r6_loop14_kakaobank_control_risk_kakao_founder | KakaoBank / Kakao | 4C-watch_then_relief | 2025-10-21 |  |  | 2024-07-23 | thesis_break_watch_then_relief | KakaoBank growth cannot be scored as Green while founder/legal ownership eligibility is unresolved. |
| r6_loop14_naver_financial_dunamu_upbit_trust_gate | Naver Financial / Dunamu / Upbit | event_premium_trust_watch | 2025-11-27 |  | 2025-11-27 | 2025-11-27 | event_premium_trust_watch | Naver/Dunamu is the digital-asset trust lesson: synergy premium reversed when custody/internal-control risk appeared. |
| r6_loop14_hana_bank_dunamu_digital_asset_stake | Hana Financial / Hana Bank / Dunamu | success_candidate_but_price_data_unavailable | 2026-05-14 |  | 2026-05-14 |  | success_candidate_but_price_data_unavailable | Hana/Dunamu is Stage 2; custody, AML/KYC, capital treatment and revenue bridge decide any promotion. |
| r6_loop14_samsung_sds_kkr_cb_stablecoin_event | Samsung SDS / KKR | event_premium_4B_watch | 2026-04-15 |  | 2026-04-15 | 2026-04-15 | event_premium_4B_watch | Samsung SDS/KKR is a 4B-watch event premium until dilution-adjusted ROIC and actual AI/stablecoin revenue are proven. |

## Interpretation
- Financial holding Value-Up and SK Square are Stage 2 paths until actual payout/cancellation, credit cost and discount compression close.
- Samsung C&T is the shareholder-return false-positive guardrail: proposal is not execution.
- K Bank and KakaoBank show that digital-bank growth needs aftermarket, credit and ownership-risk gates.
- Naver/Dunamu, Hana/Dunamu and Samsung SDS/KKR show that digital-asset or stablecoin optionality is Stage 2/4B-watch before custody, AML/KYC, capital treatment and ROIC proof.
