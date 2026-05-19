# Round 222 R5 Loop 9 Consumer Retail Brand Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_222.md
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

| case | company | type | stage2 | stage3 | 4B | 4C-watch | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r5_loop9_samyang_buldak_export_regulatory_watch | 삼양식품 | structural_success | 2024-06-14 | 2024-06-14 |  | 2024-06-12 | aligned | Export/ASP/OP revision supports Stage 3 candidate; Denmark recall is regulatory 4C-watch, not hard 4C after partial reversal. |
| r5_loop9_nongshim_global_staple_toomba | 농심 | success_candidate | 2024-05-27 |  |  |  | unknown | Global staple and product extension are Stage 2; OPM/EPS and channel sell-through required for Green. |
| r5_loop9_apr_medicube_structural_4b | APR / Medicube | structural_success | 2025-07-08 | 2025-10-20 | 2025-10-20 |  | aligned | APR is structural success candidate; fourfold rally and $6B valuation require 4B-watch. |
| r5_loop9_dalba_silicon2_indie_kbeauty_watch | d'Alba / Silicon2 / K-beauty indie basket | overheat | 2025-06-05 |  | 2025-06-05 |  | price_moved_without_evidence | Retail talks and e-commerce growth are Stage 2; sell-through, repeat orders, OPM and working-capital quality required before Green. |
| r5_loop9_cj_olive_young_retail_platform | CJ / Olive Young | success_candidate | 2025-10-01 |  |  |  | unknown | Olive Young is Stage 2 platform exposure; direct listed earnings bridge, store economics and OPM required for Green. |
| r5_loop9_amorepacific_legacy_china_exposure | 아모레퍼시픽 | failed_rerating |  |  |  | 2024-08-01 | evidence_good_but_price_failed | K-beauty macro is not enough; China decline and premium beauty weakness block Green. |
| r5_loop9_tourism_retail_china_visa_event | 현대백화점/호텔신라/한국화장품 | event_premium | 2025-08-06 |  | 2025-08-06 |  | price_moved_without_evidence | Visa-free tourist policy is Stage 2/event; tourist spend, sell-through, duty-free sales and OPM required before Green. |
| r5_loop9_fnf_taylormade_mna_optionality | F&F | event_premium |  |  |  |  | price_moved_without_evidence | TaylorMade optionality is Stage 1/2 event; confirmed transaction, financing and EPS accretion required for Green. |

## Interpretation
- 삼양식품과 APR은 R5에서 가장 강한 Stage 3 후보지만 각각 regulatory watch와 4B-watch가 같이 붙는다.
- 농심, CJ/Olive Young, Silicon2류는 Stage 2 후보지만 OPM/EPS/sell-through/working-capital 확인 전 Green이 아니다.
- d'Alba, 관광/면세, F&F는 가격이나 이벤트가 먼저 움직인 event premium이다.
- 아모레퍼시픽은 K-beauty macro와 회사 실적을 분리해야 하는 China exposure 4C-watch다.
