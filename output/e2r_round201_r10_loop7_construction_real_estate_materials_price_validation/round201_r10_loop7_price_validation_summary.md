# Round-201 R10 Loop-7 Price-Path Validation Summary

- source_round: `docs/round/round_201.md`
- large_sector: `CONSTRUCTION_REAL_ESTATE_MATERIALS`
- scope: PF credit, overseas EPC, apartment safety, AI data-center real assets, REIT/AFFO, and rebuild headline risk
- case_candidate_count: 7
- required_target_count: 15
- score_adjustment_count: 21
- price_backfill_field_count: 52
- success_candidate_count: 4
- hard_4c_case_count: 2
- stage3_case_count: 0
- stage4b_watch_or_elevated_count: 5
- needs_ohlc_backfill_count: 7
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true
- needs_ohlc_backfill: true

## Interpretation

- R10은 수주, PF 지원, 데이터센터, 부동산 반등 headline이 가격을 먼저 밀기 쉬운 섹터다.
- 삼성E&A·현대건설·대우건설은 Stage 2 후보지만, EPC margin과 cash collection 전 Green이 아니다.
- 태영건설 PF workout은 R10 hard 4C 기준점이다.
- HDC현대산업개발 붕괴 사고는 품질·안전 hard 4C 기준점이다.
- POSCO E&C/DL건설 안전 이슈는 operational trust RedTeam watch다.
- SK/AWS 데이터센터는 좋은 구조 후보지만 listed vehicle의 tenant, NOI/AFFO, power/water 전 Green이 아니다.

쉬운 예: `as_of_date=2024-04-03`에 삼성E&A가 대형 수주를 받아도, 원가율과 현금 회수가 아직 없으면 Stage 3-Green이 아니라 Stage 2 watch다.
