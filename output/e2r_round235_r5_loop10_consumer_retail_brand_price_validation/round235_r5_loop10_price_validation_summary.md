# Round 235 R5 Loop 10 Consumer Retail Brand Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_235.md
- round_id: round_163
- large_sector: CONSUMER_RETAIL_BRAND
- cases: 8
- structural_success: 2
- success_candidate: 2
- overheat: 1
- failed_rerating: 1
- event_premium: 2
- Stage 3 dated cases: 2
- 4B-watch cases: 6
- 4C-watch cases: 2
- full_ohlc_complete: false

## Case Matrix

| case | company | type | stage2 | stage3 | 4B | 4C-watch | round alignment | note |
|---|---|---|---|---|---|---|---|---|
| r5_loop10_samyang_buldak_export_regulatory_watch | 삼양식품 | structural_success | 2024-06-14 | 2024-06-14 |  | 2024-06-12 | aligned_partial | Export/ASP/OP revision supports Stage 3 candidate; Denmark recall is regulatory 4C-watch, not hard 4C after partial reversal. |
| r5_loop10_nongshim_shin_global_staple | 농심 | success_candidate | 2024-05-27 |  |  |  | success_candidate | Global staple and overseas expansion are Stage 2; OPM/EPS and channel sell-through required for Green. |
| r5_loop10_apr_medicube_structural_4b | APR / Medicube | structural_success | 2025-07-01 | 2025-10-01 | 2025-10-01 |  | aligned_plus_4B_watch | Revenue conversion supports structural success, but single-brand/device concentration and fourfold rally require 4B-watch. |
| r5_loop10_indie_kbeauty_odm_distribution_watch | d'Alba / Silicon2 / Cosmax / Kolmar basket | overheat | 2025-06-05 |  | 2025-06-05 |  | price_moved_without_evidence_for_dAlba_success_candidate_for_ODM_distribution | Retail talks and ecommerce growth are Stage 2; sell-through, repeat orders, OPM and working-capital quality required before Green. |
| r5_loop10_cj_olive_young_retail_platform | CJ / Olive Young | success_candidate | 2025-10-01 |  |  |  | success_candidate | Olive Young is Stage 2 platform exposure; direct listed earnings bridge, store economics and OPM required for Green. |
| r5_loop10_amorepacific_legacy_china_exposure | 아모레퍼시픽 | failed_rerating |  |  |  | 2024-10-22 | thesis_break_watch_insufficient_price_data | K-beauty macro is not enough; China/duty-free weakness and premium beauty slowdown block Green until U.S./Europe offset is proven. |
| r5_loop10_tourism_retail_china_visa_event | 호텔신라/현대백화점/파라다이스/한국화장품 | event_premium | 2025-08-06 |  | 2025-08-06 |  | event_premium_success_candidate | Visa-free tourist policy is Stage 2/event; tourist spend, sell-through, duty-free sales and OPM required before Green. |
| r5_loop10_fnf_taylormade_mna_optionality | F&F | event_premium |  |  |  |  | event_premium | TaylorMade optionality is Stage 1/2 event; confirmed transaction, financing and EPS accretion required for Green. |

## Interpretation
- 삼양식품은 수출, ASP, OP revision이 같이 확인된 Stage 3 후보지만 local-regulatory 4C-watch가 붙는다.
- APR/Medicube는 강한 structural success 후보지만 주가 4배 이상 상승과 single-device concentration 때문에 4B-watch가 필요하다.
- 농심, CJ/Olive Young, Silicon2/Cosmax/Kolmar류는 Stage 2 후보지만 OPM/EPS/sell-through/working-capital 확인 전 Green이 아니다.
- d'Alba, 관광/면세, F&F는 가격이나 이벤트가 먼저 움직인 event premium이다.
- 아모레퍼시픽은 K-beauty macro와 회사 실적을 분리해야 하는 China exposure thesis-break watch다.
