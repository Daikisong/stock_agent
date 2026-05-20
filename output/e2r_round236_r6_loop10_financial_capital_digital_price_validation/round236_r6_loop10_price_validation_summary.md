# Round 236 R6 Loop 10 Financial Capital Digital Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_236.md
- analyst_round_id: round_164
- large_sector: FINANCIAL_CAPITAL_DIGITAL
- cases: 8
- success_candidate: 5
- cyclical_success: 1
- event_premium: 1
- overheat: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 8
- 4C-watch cases: 2
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage2 | stage3 | 4B | 4C-watch | round alignment | note |
|---|---|---|---|---|---|---|---|---|
| r6_loop10_bank_valueup_big4_kb_watch | KB/Shinhan/Hana/Woori financial groups | success_candidate | 2025-01-01 |  |  |  | success_candidate | Bank value-up is Stage 2; ROE/CET1/credit cost and repeated shareholder return required before Green. |
| r6_loop10_securities_capital_market_boom | Korean securities firms basket | cyclical_success | 2026-05-06 |  | 2026-05-06 |  | cyclical_success | Securities rally is Stage 2/cyclical and 4B-watch; brokerage/IB revenue and ROE required before Green. |
| r6_loop10_sk_square_nav_discount_valueup | SK스퀘어 | success_candidate | 2024-11-21 |  |  |  | success_candidate | Actual cancellation supports Stage 2; repeated cancellation and discount narrowing required for Stage 3. |
| r6_loop10_samsung_life_nav_capital_release | 삼성생명 | success_candidate | 2026-03-19 |  |  |  | success_candidate_regulatory_watch | Capital release is Stage 2; use of proceeds, K-ICS/CSM and shareholder return required before Green. |
| r6_loop10_hana_dunamu_equity_option | 하나금융/하나은행/Dunamu | success_candidate | 2026-05-14 |  |  |  | success_candidate | Dunamu stake is Stage 2; regulated revenue, equity-method earnings, capital impact and exchange trust required for Stage 3. |
| r6_loop10_naver_dunamu_platform_merger_trust_watch | NAVER / NAVER Financial / Dunamu | event_premium | 2025-11-27 |  | 2025-11-27 | 2025-11-27 | event_premium_trust_watch | Strong Stage 2 digital-asset merger, but abnormal withdrawal creates exchange-trust 4C-watch. |
| r6_loop10_internet_bank_kbank_kakaobank_watch | K Bank / KakaoBank / Kakao | success_candidate | 2024-09-10 |  |  | 2024-07-23 | success_candidate_for_KBank_thesis_break_watch_for_KakaoBank | K Bank is unlisted Stage 2; KakaoBank Green is blocked by major shareholder legal/ownership risk. |
| r6_loop10_stablecoin_policy_theme_overheat | Kakao Pay / stablecoin policy basket | overheat |  |  | 2025-06-01 |  | price_moved_without_evidence | Stablecoin theme rallied before licensed issuer, reserve income, fee revenue or regulatory capital clarity. |

## Interpretation
- KB 중심 은행주는 Stage 2 후보지만 ROE, CET1, credit cost, 반복 주주환원 실행 전 Green이 아니다.
- 증권주 basket은 cyclical_success와 4B-watch다. 거래대금 사이클만으로 Green을 만들지 않는다.
- SK스퀘어와 삼성생명은 NAV/capital-release Stage 2 후보지만 실제 환원과 자본비율 확인이 필요하다.
- 하나은행/Dunamu는 강한 Stage 2지만 지분법 이익, 규제수익, 자본비율 영향, 거래소 신뢰를 확인해야 한다.
- NAVER/Dunamu는 platform merger Stage 2와 exchange-trust 4C-watch가 동시에 뜬다.
- K Bank는 unlisted Stage 2이고, KakaoBank는 대주주 법적 리스크가 Green을 막는다.
- Stablecoin basket은 라이선스, reserve income, fee revenue 전 가격이 먼저 움직인 price_moved_without_evidence다.
