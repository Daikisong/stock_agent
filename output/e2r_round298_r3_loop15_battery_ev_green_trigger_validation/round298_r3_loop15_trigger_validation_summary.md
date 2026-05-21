# Round 298 R3 Loop 15 Battery/EV/Green Trigger Validation

이번 라운드는 2차전지, EV, ESS, 소재, 친환경 공급망을 calibration-only로 정리한다.

쉬운 예: `계약금액 2조원`은 시작점일 뿐이다. 실제 납품, 고객 생산계획, 보조금 제외 margin이 닫히지 않으면 Green이 아니라 Stage2 또는 Yellow에 머문다.

## Summary

- round_id: round_226
- large_sector: SECONDARY_BATTERY_EV_GREEN
- case_candidate_count: 8
- trigger_count: 9
- stage2_actionable_candidate_count: 4
- stage3_yellow_candidate_count: 2
- stage3_green_confirmed_count: 0
- stage4b_watch_count: 3
- stage4c_watch_count: 4
- hard_4c_case_count: 2
- production_scoring_changed: False
- candidate_generation_input: False
- full_adjusted_ohlc_complete: False
- shadow_weight_only: True

## Core Findings

- LGES AMPC profit beat는 Stage3-Yellow 후보지만, 보조금 제외 OP와 고객 call-off가 남아 Green은 아니다.
- Samsung SDI ESS LFP pivot은 Stage2-Actionable이다. 다만 delivery와 converted-line margin 전에는 Green이 아니다.
- SK On/Ford, LGES/Ford/Freudenberg, L&F/Tesla는 EV 계약 headline이 4C로 바뀔 수 있음을 보여준다.
- CATL mine suspension에 따른 lithium rally는 event premium이다. 지속 가격과 소재 margin 확인 전 Stage3가 아니다.
- Aricell/S-Connect 및 EV battery disclosure 이슈는 safety/trust hard gate다.
