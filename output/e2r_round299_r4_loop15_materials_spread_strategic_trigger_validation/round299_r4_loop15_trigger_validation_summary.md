# Round 299 R4 Loop 15 Materials/Spread/Strategic Resources Trigger Validation

이번 라운드는 소재 가격 headline이 아니라 tariff, spread, TC/RC, funding, control premium을 분리한다.

쉬운 예: Korea Zinc가 tender battle로 급등해도, 그것은 아연 제련 margin이 좋아진 Green이 아니라 control-premium 4B다.

## Summary

- round_id: round_227
- large_sector: MATERIALS_SPREAD_STRATEGIC_RESOURCES
- case_candidate_count: 10
- trigger_count: 11
- stage2_actionable_candidate_count: 4
- stage3_yellow_candidate_count: 3
- stage3_green_confirmed_count: 0
- stage4b_watch_count: 4
- stage4c_watch_count: 5
- hard_4c_case_count: 0
- production_scoring_changed: False
- candidate_generation_input: False
- full_adjusted_ohlc_complete: False
- shadow_weight_only: True

## Core Findings

- POSCO Future M graphite tariff는 Stage2-Actionable / Yellow candidate지만, capacity/quality/customer gate가 남는다.
- CATL lithium mine suspension은 event premium이다. durable price와 margin 전에는 Stage3가 아니다.
- Hyundai Steel/POSCO anti-dumping은 tariff, import share, relative strength가 있어 Stage2-Actionable이다.
- Hyundai Steel U.S. plant는 funding/IRR/customer demand가 닫히지 않은 localization capex false positive다.
- Korea Zinc tender battle은 control premium 4B이고, U.S. critical-minerals refinery는 Stage2 + 4B governance/dilution overlay다.
- Copper record price와 smelter TC/RC margin은 반대로 움직일 수 있으므로 따로 scoring해야 한다.
