# Checkpoint 28A Round 123 R4 Loop 7 Materials / Spread / Strategic Resources

## Scope

Round 123 updates the R4 materials, spread, and strategic-resources calibration pack.

This is calibration/evaluation material only. It does not change production scoring, StageClassifier thresholds, RedTeam behavior, or candidate generation.

## What Changed

- Added `src/e2r/sector/round123_r4_loop7_materials_spread_strategic.py`.
- Added `src/e2r/cli/build_round123_r4_loop7_report.py`.
- Added tests in `tests/test_round123_r4_loop7_materials_spread_strategic.py`.
- Added canonical calibration archetypes:
  - `RARE_EARTH_CAPITAL_RAISE_DILUTION`
  - `NICKEL_SULFUR_HPAL_INPUT_COST`
  - `PACKAGING_CONSOLIDATION_REMEDY`
- Generated case records:
  - `data/e2r_case_library/cases_r4_loop7_round123.jsonl`
- Generated score profile:
  - `data/sector_taxonomy/score_weight_profiles_round123_r4_loop7_v7.csv`
- Generated reports under:
  - `output/e2r_round123_r4_loop7_materials_spread_strategic/`

## Main Interpretation

R4 Loop 7 separates price movement from structural rerating.

Simple example:

- Copper record highs are useful evidence that AI/data-center/grid demand matters.
- They are not company-level Stage 3-Green unless the company also shows production volume, cash cost, FCF, capital return, and no processing input-cost squeeze.

## Base Score Table

Round 123 records seven calibration axes:

- EPS/FCF transition: 22
- Contract / offtake / price floor visibility: 20
- Bottleneck / pricing power: 18
- Market mispricing / rerating gap: 12
- Valuation room / 4B runway: 8
- Capital discipline / dilution risk: 10
- Information confidence / disclosure detail: 10

These weights are report material only and are not applied to live scoring.

## Stage Caps

- Commodity price, export control, safe-haven demand, China stimulus, supply shortage headline, or science theme alone is capped at Stage 1.
- Price floor, offtake, government investment, customer contract, M&A, production plan, buyback, realized price, or AISC can support Stage 2.
- Stage 3 requires OP/EPS/FCF revision, cost control, stable production, capital return, price-path alignment, and no hard 4C flag.
- Scarcity narratives that are already crowded move to 4B-watch.
- Price collapse, supply restart, dilution, governance shock, event premium unwind, HPAL input-cost squeeze, and speculative science failure are 4C/RedTeam gates.

## Price Alignment Findings

The new score-stage-price alignment report records 10 cases.

Key examples:

- `mp_materials_dod_price_floor_case`: Stage 2 structure is real, but YTD +275% means 4B-watch.
- `mp_materials_capital_raise_dilution_case`: capital raise/dilution matched a negative price reaction.
- `copper_ai_grid_record_high_case`: commodity path matched, but company-level Green needs cash cost, production, FCF, and capital return.
- `barrick_record_gold_buyback_case`: realized gold price, AISC, earnings, and buyback support Stage 2/3 candidate status, but OHLCV backfill is still needed.
- `korea_zinc_tender_offer_event_case`: tender-offer upside is event premium, not strategic-metal structural success.
- `lg_chem_lotte_chemical_oversupply_case`: chemical spread false Green is blocked by oversupply and OP collapse.
- `indonesia_nickel_hpal_sulfur_squeeze_case`: nickel price can rise while HPAL processing economics worsen.

## Guardrails

- Do not use Round-123 case records as candidate-generation input.
- Do not change production scoring from this pack.
- Do not loosen Stage 3-Green to improve recall.
- Do not invent spread, offtake, price floor, AISC, cash cost, processing input cost, FCF, capital return, or stage prices.
- Do not treat commodity price, tender offer, policy headline, safe-haven demand, or science theme as Green evidence by name alone.

## Verification

Focused Round-123 tests passed:

```bash
PYTHONPATH=src python -m unittest tests.test_round123_r4_loop7_materials_spread_strategic -v
```

Full test suite is run before committing this checkpoint.
