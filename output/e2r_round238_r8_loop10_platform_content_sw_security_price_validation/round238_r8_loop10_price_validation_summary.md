# Round 238 R8 Loop 10 Platform Content SW Security Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_238.md
- analyst_round_id: round_166
- large_sector: PLATFORM_CONTENT_SW_SECURITY
- cases: 8
- success_candidate: 3
- event_premium: 1
- failed_rerating: 2
- overheat: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 8
- strong 4C-watch cases: 2
- hard_4c_case_count: 0
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round_type | stage2 | stage3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|---|
| r8_loop10_douzone_eqt_b2b_saas_stage2_watch | 더존비즈온 | success_candidate | success_candidate | 2025-11-07 |  |  |  | unknown | Private-equity validation is useful, but ARR, churn, OPM, FCF, and closing conditions decide promotion. |
| r8_loop10_samsung_sds_ai_cloud_kkr_event_premium | 삼성SDS | event_premium | success_candidate_4b_watch | 2026-04-15 |  | 2026-04-15 |  | price_moved_without_evidence | Large price reaction is 4B/event premium until AI/cloud revenue conversion, M&A execution, OPM, and FCF are visible. |
| r8_loop10_lg_cns_ipo_cloud_ai_price_failed | LG CNS | failed_rerating | evidence_good_but_price_failed | 2025-02-05 |  |  |  | evidence_good_but_price_failed | Cloud/AI operating anchors are useful, but the IPO price path failed and integration/FCF evidence is still required. |
| r8_loop10_naver_webtoon_ipo_disney_ip_watch | NAVER/Webtoon | success_candidate | success_candidate_event_premium_watch | 2024-06-27 |  | 2025-08-13 |  | unknown | Webtoon/IP can be a Stage 2 watch, but losses, ads/subscription/IP monetization, and post-IPO price path still gate Green. |
| r8_loop10_kakao_openai_partnership_price_only_rally | 카카오 | overheat | price_moved_without_evidence |  |  | 2025-02-04 |  | price_moved_without_evidence | AI partnership creates a research watch, not Green. Paid usage, ARPU, cost savings, margin, and governance pass are required. |
| r8_loop10_shiftup_single_ip_repeat_monetization_watch | 시프트업 | success_candidate | success_candidate_ipo_watch | 2024-07-01 |  |  |  | unknown | High OPM and sales are useful, but retention, tail monetization, platform expansion, and single-IP risk decide promotion. |
| r8_loop10_skt_data_breach_operational_trust_4c_watch | SK텔레콤 | 4c_thesis_break | strong_4c_watch_operational_trust_break |  |  |  | 2025-04-28 | false_positive_score | Security and privacy breach evidence belongs to RedTeam/4C-watch; it must not be treated as positive rerating evidence. |
| r8_loop10_hybe_founder_legal_governance_4c_watch | HYBE | failed_rerating | governance_legal_4c_watch |  |  |  | 2026-04-21 | false_positive_score | K-pop/IP evidence cannot overcome founder/legal governance risk until the trust issue is resolved and FCF evidence supports rerating. |

## Interpretation
- Douzone and Shift Up are Stage 2 watch examples, not automatic Green.
- Samsung SDS, NAVER/Webtoon, Kakao, and LG CNS show why event premium and price confirmation must be separated.
- SKT and HYBE are trust/governance watch examples; these feed RedTeam/4C checks rather than positive scoring.
- R8 Green needs recurring revenue, paid usage, margin, FCF, retention, operational trust, and price behavior after evidence.
