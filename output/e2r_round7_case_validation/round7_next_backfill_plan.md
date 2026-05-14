# Round-7 Next Backfill Plan

- needs_price_path_total: 66
- redteam_guardrail_archetypes: 10

## Priority

1. 가격 경로가 없는 케이스부터 stage price, MFE/MAE, drawdown, 4B/4C를 채운다.
2. Platform, Game, Travel, Construction, Retail, CDMO, Royalty biotech, Holding, Financial, Rare Metals는 Round 7 세부 규칙으로 재검증한다.
3. Green 가능 archetype도 성공 2개 + 반례 2개 + price validation 전에는 scoring weight를 적용하지 않는다.

## What Not To Change

- Stage 3-Green 기준을 낮추지 않는다.
- benchmark/case label을 production candidate generation에 넣지 않는다.
- price-only rally를 EPS/FCF evidence로 바꾸지 않는다.
