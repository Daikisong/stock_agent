# Checkpoint 28A Round 325: R4 Loop 17 Materials / Spreads / Strategic Resources

## Scope

- Source round: `docs/round/round_325.md`
- Analyst round id: `round_253`
- Large sector: `MATERIALS_SPREADS_STRATEGIC_RESOURCES`
- Method: `trigger_level_backtest_v1_after_redteam`
- Production scoring changed: `false`
- Candidate generation input: `false`
- Shadow weight only: `true`

This patch converts the R4 Loop 17 analyst round into calibration-only records. It does not change production scoring or Stage 3-Green thresholds.

Easy example: Hyundai Steel/POSCO anti-dumping can be Stage2-Actionable because tariff rate and price reaction are visible. It is not Green until domestic spread and margin recovery show up in earnings.

## Added Archetypes

The round requires ten exact archetype aliases:

- `CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B`
- `SMELTER_TC_SPREAD_4B`
- `CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B`
- `STEEL_ANTIDUMPING_PROTECTION_STAGE2`
- `STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B`
- `PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF`
- `PETROCHEMICAL_OVERSUPPLY_4B`
- `REFINING_MARGIN_SPREAD_PRICE_FAILED`
- `UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE`
- `RARE_EARTH_EXPORT_CONTROL_4B`

Nine missing aliases were added to `E2RArchetype`; the existing upstream lithium no-price alias was reused.

## Case Pack

Generated case records:

- Case candidates: `9`
- Trigger rows: `13`
- Stage2-Actionable candidates: `1`
- Stage2 candidates: `6`
- Stage3-Yellow candidates: `5`
- Stage3-Green confirmed: `0`
- Stage4B-watch count: `8`
- Hard 4C confirmed count: `0`
- Strong 4C-watch count: `5`

Core interpretation:

- Korea Zinc control premium: Stage2, not operating Green.
- Korea Zinc / Teck TC cut: smelter-margin 4B.
- Korea Zinc U.S. critical-minerals plant: Stage2 with capex/dilution 4B.
- Hyundai Steel/POSCO anti-dumping: cleanest Stage2-Actionable R4 trigger.
- Hyundai/POSCO Louisiana steel plant: localization hedge Stage2 with tariff 4B.
- Lotte/LG Chem petrochemical oversupply: failed rerating with restructuring relief only.
- SK Innovation refining spread: mixed recovery candidate with segment-quality 4B.
- POSCO/MinRes lithium JV: upstream Stage2, no POSCO direct price validation.
- China rare-earth export control: sector-wide 4B.

## Green Blockers

Green remains blocked by:

- Control premium without operating margin.
- Anti-dumping without margin recovery.
- Critical-minerals capex without funding, offtake, construction, and dilution clarity.
- Petrochemical restructuring without spread recovery.
- Refining OP without segment quality.
- Upstream lithium without POSCO price validation or offtake/downstream margin.
- Rare-earth headline without company-specific cost or order impact.
- Missing full adjusted OHLC for MFE/MAE validation.

## Files Generated

- `src/e2r/sector/round325_r4_loop17_materials_spreads_strategic.py`
- `src/e2r/cli/build_round325_r4_loop17_report.py`
- `tests/test_round325_r4_loop17_materials_spreads_strategic.py`
- `data/e2r_case_library/cases_r4_loop17_round253.jsonl`
- `data/e2r_trigger_calibration/triggers_r4_loop17_round253.jsonl`
- `data/sector_taxonomy/round325_r4_loop17_materials_spreads_strategic_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round253_r4_loop17_v1.csv`
- `output/e2r_round325_r4_loop17_materials_spreads_strategic/`

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round325_r4_loop17_materials_spreads_strategic -v
PYTHONPATH=src python -m e2r.cli.build_round325_r4_loop17_report
```

Additional full-suite verification is tracked in the commit notes for this round.

## What Not To Change

- Do not change production scoring from this round alone.
- Do not use round 325 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds.
- Do not invent full MFE/MAE without adjusted OHLC.
- Do not treat control premium, anti-dumping, critical capex, lithium stake, or restructuring as Green without margin, offtake, funding, and risk-resolution evidence.
