# Round 304 R9 Loop 15 Mobility/Transport/Leisure Trigger Validation

이번 라운드는 자동차, 로봇, 항공, 여행, 해운 headline을 실제 EPS/FCF 지속 증거와 분리한다.

쉬운 예: `비자 면제`는 손님이 올 수 있다는 신호다. Green은 실제 입국자, 객단가, 호텔 ADR, 면세점 매출, 항공 yield가 확인될 때다.

## Summary

- round_id: round_232
- large_sector: MOBILITY_TRANSPORT_LEISURE
- case_candidate_count: 8
- trigger_count: 10
- stage2_actionable_candidate_count: 5
- stage3_yellow_candidate_count: 1
- stage3_green_confirmed_count: 0
- stage4b_watch_count: 4
- stage4c_watch_count: 4
- hard_4c_case_count: 1
- production_scoring_changed: False
- candidate_generation_input: False
- full_adjusted_ohlc_complete: False
- shadow_weight_only: True

## Core Findings

- Hyundai hybrid/shareholder-return trigger is Stage2-Actionable and Stage3-Yellow candidate, but actual hybrid mix, ASP/margin, tariff absorption and buyback execution are Green gates.
- Kia tariff hit and EV target cut are 4C-watch until hybrid mix offsets tariff-adjusted margin.
- Hyundai/Boston Dynamics robotics is Stage2-Actionable with 4B overlay; orders and unit economics are required before Green.
- Hyundai Georgia localization is operational 4C-watch; capex does not count until workforce, visa, safety and compliance are closed.
- Korean Air/Asiana is Stage2 consolidation; route yield, load factor, LCC integration and debt/synergy must follow.
- Jeju Air crash is hard 4C and blocks travel-demand Green logic.
- China tourism visa-waiver basket is Stage2-Actionable; actual spending/yield evidence is required.
- HMM/Red Sea freight is cyclical Stage2 + 4B-watch, not structural Green without contract mix and duration.
