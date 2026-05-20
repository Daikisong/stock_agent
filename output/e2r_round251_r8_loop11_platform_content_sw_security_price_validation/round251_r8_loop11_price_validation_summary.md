# Round 251 R8 Loop 11 Platform Content SW Security Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_251.md
- analyst_round_id: round_179
- large_sector: PLATFORM_CONTENT_SW_SECURITY
- cases: 8
- success_candidate: 4
- failed_rerating: 2
- overheat: 1
- hard_4c_case_count: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- 4C-watch cases: 1
- evidence_good_but_price_failed: 1
- price_moved_without_evidence: 3
- full_ohlc_complete: false

## Case Matrix

| case | company | type | round type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|---|---|
| r8_loop11_douzone_bizon_eqt_saas | Douzone Bizon | success_candidate | success_candidate_b2b_saas_stage2 | 2025-11-07 |  |  |  | false | unknown | EQT investment validates business quality, but Green requires ARR proxy, churn, OPM and FCF conversion. |
| r8_loop11_samsung_sds_kkr_ai_4b | Samsung SDS | success_candidate | success_candidate_4b_watch | 2026-04-15 |  | 2026-04-15 |  | false | price_moved_without_evidence | KKR/AI capital allocation is Stage 2 plus 4B-watch; recurring AI revenue and FCF are required for Green. |
| r8_loop11_lg_cns_ai_cloud_ipo_price_failed | LG CNS | failed_rerating | evidence_good_but_price_failed | 2025-02-05 |  |  |  | false | evidence_good_but_price_failed | Cloud/AI mix is useful Stage 2 evidence, but IPO price action failed and Green needs recurring revenue, retention, margin and FCF. |
| r8_loop11_naver_webtoon_ip_platform | NAVER / Webtoon | success_candidate | success_candidate_event_premium_watch | 2024-06-27 |  | 2025-08-13 |  | false | price_moved_without_evidence | IP platform is Stage 2; paid usage, ARPU, IP licensing, operating leverage and FCF are required before Green. |
| r8_loop11_kakao_openai_partnership_price_only | Kakao | overheat | price_moved_without_evidence |  |  | 2025-02-04 |  | false | price_moved_without_evidence | OpenAI partnership moved price before monetization; paid usage, ARPU and margin are required for Green. |
| r8_loop11_krafton_game_ip_india_adk_watch | Krafton | success_candidate | success_candidate_execution_watch | 2025-06-24 |  |  |  | false | unknown | Game/IP expansion is Stage 2; bookings, retention, IP conversion, India regulation and FCF decide promotion. |
| r8_loop11_skt_cybersecurity_operational_trust_hard_4c | SK Telecom | 4c_thesis_break | hard_4c_cybersecurity_operational_trust_break |  |  |  | 2025-04-28 | true | false_positive_score | Cybersecurity breach directly hit price, revenue guide, compensation and fine; this is hard 4C. |
| r8_loop11_hybe_founder_legal_governance_watch | HYBE | failed_rerating | governance_legal_4c_watch |  |  |  | 2026-04-21 | false | false_positive_score | K-pop IP monetization cannot outrank governance/legal overhang; warrant declined, so hard 4C is not confirmed. |

## Interpretation
- Douzone is B2B SaaS Stage 2; ARR, churn, OPM and FCF decide promotion.
- Samsung SDS is AI capital-allocation Stage 2 plus 4B-watch because price moved before recurring AI revenue.
- LG CNS has cloud/AI evidence but IPO price action failed.
- Webtoon is IP-platform Stage 2; paid usage, ARPU, IP licensing and FCF are required before Green.
- Kakao/OpenAI is price_moved_without_evidence until paid AI usage and monetization appear.
- Krafton is game/IP expansion Stage 2; bookings, retention, regulation and FCF decide promotion.
- SK Telecom is hard 4C because the breach hit price, revenue outlook, compensation, security spend and fine.
- HYBE is governance 4C-watch; warrant relief means hard 4C is not confirmed.
