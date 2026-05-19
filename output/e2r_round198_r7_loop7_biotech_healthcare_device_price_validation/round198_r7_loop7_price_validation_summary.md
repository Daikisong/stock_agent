# Round-198 R7 Loop-7 Price-Path Validation Summary

- source_round: `docs/round/round_198.md`
- large_sector: `BIOTECH_HEALTHCARE_DEVICE`
- scope: oncology royalty, botulinum launch, biosimilar/CDMO manufacturing, medical AI, and hard 4C source-gap validation
- case_candidate_count: 7
- required_target_count: 18
- score_adjustment_count: 20
- price_backfill_field_count: 51
- success_candidate_count: 4
- failed_rerating_count: 2
- stage4b_watch_count: 1
- hard_4c_case_count: 0
- stage3_case_count: 0
- stage4b_watch_or_elevated_count: 6
- source_gap_case_count: 1
- needs_ohlc_backfill_count: 7
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true
- needs_ohlc_backfill: true
- hard_4c_confirmed: false in this pass

## Interpretation

- R7은 승인, 임상, 논문, M&A보다 상업화 숫자를 늦게 확인해야 하는 섹터다.
- 유한양행은 FDA 승인으로 Stage 2 후보지만 처방량, 로열티, EPS revision 전 Stage 3는 보류한다.
- 휴젤은 미국 launch가 Stage 2지만 미국 매출, ASP, 채널 침투 전 Green 금지다.
- 셀트리온 미국 공장 인수는 tariff hedge Stage 2지만 제품 이전, 가동률, margin, FCF 전에는 Green이 아니다.
- SK바이오사이언스 IDT 인수는 CMO 전환 후보지만 발표 당일 급등은 event premium watch다.
- 삼성바이오로직스는 CDMO structural benchmark지만 이번 시설 인수는 신규 Green보다 4B/saturation 감시에 가깝다.
- 루닛은 외부검증이 있어도 reimbursement, hospital adoption, recurring revenue 전에는 Stage 3가 아니다.
- 이번 pass에서는 신뢰할 수 있는 원문이 부족한 hard 4C를 억지로 확정하지 않는다.

쉬운 예: `as_of_date=2024-08-20`에 FDA 승인이 나도 실제 처방량과 로열티가 없으면 Stage 3-Green이 아니라 강한 Stage 2다.
