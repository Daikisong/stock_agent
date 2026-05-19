# Round 221 R4 Loop 9 Materials Spread Strategic Resources Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_221.md
- large_sector: MATERIALS_SPREAD_STRATEGIC
- cases: 7
- success_candidate: 3
- cyclical_success: 1
- event_premium: 1
- failed_rerating: 2
- 4B watch cases: 5
- 4C watch cases: 3
- hard_4c: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C-watch | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r4_loop9_posco_hyundai_steel_tariff_watch | POSCO Holdings / Hyundai Steel | failed_rerating |  |  |  | 2025-02-10 | unknown | U.S. tariff shock is 4C-watch for Korean steel exporters; Green requires actual spread and export margin resilience. |
| r4_loop9_korea_zinc_strategic_governance | Korea Zinc / YoungPoong | success_candidate | 2025-12-15 |  | 2025-12-15 | 2025-12-16 | price_moved_without_evidence | Strategic minerals are Stage 2; governance, dilution, offtake, and FCF must clear before Stage 3. |
| r4_loop9_lotte_hd_petrochemical_restructuring | Lotte Chemical / HD Hyundai Chemical | failed_rerating | 2026-02-24 |  |  |  | false_positive_score | Capacity shutdown and support are Stage 2 relief; spread, OPM and FCF recovery are required for Green. |
| r4_loop9_sk_innovation_soil_refining_cycle | SK Innovation / S-Oil | cyclical_success | 2026-01-28 |  |  |  | aligned | Refining rebound is cyclical Stage 2; Green needs multi-quarter margin floor, FCF, deleveraging and battery loss control. |
| r4_loop9_posco_minres_lithium_jv | POSCO Holdings / MinRes lithium JV | success_candidate | 2025-11-11 |  |  |  | unknown | Lithium mine stake is Stage 2; Stage 3 requires offtake economics, downstream margin and FCF. |
| r4_loop9_oci_non_china_polysilicon | OCI Holdings | success_candidate | 2025-06-07 |  | 2026-04-14 |  | unknown | U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract terms, margin and FCF confirm. |
| r4_loop9_poongsan_hanwha_mna_rumor_fade | Poongsan | event_premium |  |  | 2026-04-03 | 2026-04-09 | price_moved_without_evidence | M&A rumor faded in six days; Stage 3 requires confirmed transaction or copper/ammunition margin and FCF. |

## Interpretation
- 철강 관세는 한국 수출업체에는 4C-watch가 될 수 있다.
- 고려아연은 전략광물 Stage 2 후보지만 governance/dilution/offtake/FCF 전 Green은 아니다.
- 롯데케미칼 구조조정은 relief이지 spread/OPM/FCF 확인 전 Green이 아니다.
- SK Innovation/S-Oil 정유 반등은 cyclical Stage 2다.
- POSCO lithium JV와 OCI non-China polysilicon은 Stage 2 후보지만 commodity/capex/media-report risk가 남아 있다.
- 풍산 M&A rumor는 6일 만에 fade된 event premium이다.
