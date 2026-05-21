# Checkpoint 28A Round 323 R2 Loop 17 AI Semiconductor

## Scope

- Source round: `docs/round/round_323.md`
- Analyst round id: `round_251`
- Large sector: `AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS`
- Method: `trigger_level_backtest_v1_after_redteam`
- Production scoring changed: `false`
- Candidate-generation input: `false`
- Shadow weights only: `true`

## What Changed

- Added 8 canonical AI semiconductor / HBM archetypes.
- Added calibration-only case records for HBM first mover, HBM4 certification, OpenAI Stargate memory demand, Samsung HBM catch-up, HBM packaging equipment, memory earnings price-failed, China export-control 4B, and labor supply-disruption 4B.
- Added trigger calibration rows and shadow weight profiles.
- Added a CLI: `PYTHONPATH=src python -m e2r.cli.build_round323_r2_loop17_report`.

## Key Result

- Case candidates: `8`
- Trigger rows: `8`
- Stage2-Actionable candidates: `3`
- Stage2 candidates: `5`
- Stage3-Yellow candidates: `4`
- Stage3-Green confirmed: `0`
- 4B-watch count: `6`
- Strong 4C count: `0`
- Evidence-good but price-failed count: `1`

## Interpretation

Round 323 keeps the same guardrail as prior rounds: HBM and AI memory headlines can promote a case to Stage2 or Yellow review, but not to Green by themselves.

Easy example: OpenAI Stargate memory demand is a strong signal, but a LOI is not a binding purchase order. Until volume, ASP, delivery schedule, margin and payment terms are confirmed, it remains Stage2-Actionable with a 4B overlay.

## Green Blockers

- HBM mass production without customer order volume.
- HBM4 certification without top-customer confirmed volume.
- LOI without binding order.
- HBM catch-up without large volume or yield.
- HBM equipment order without repeat order or customer diversification.
- Record profit with negative event return.
- China export-control risk ignored.
- Labor disruption ignored.
- Full adjusted OHLC missing for Green confirmation.

## Files Generated

- `data/e2r_case_library/cases_r2_loop17_round251.jsonl`
- `data/e2r_trigger_calibration/triggers_r2_loop17_round251.jsonl`
- `data/sector_taxonomy/round323_r2_loop17_ai_semiconductor_electronics_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round251_r2_loop17_v1.csv`
- `output/e2r_round323_r2_loop17_ai_semiconductor_electronics/`

## Verification

- `PYTHONPATH=src python -m unittest tests.test_round323_r2_loop17_ai_semiconductor_electronics -v`

## What Not To Change

- Do not use round323 cases as candidate-generation input.
- Do not lower Stage3-Green thresholds to improve recall.
- Do not invent full MFE/MAE without adjusted OHLC.
- Do not treat HBM mass production, certification, LOI, or record profit as Green without volume, yield, ASP, margin, capacity and risk-resolution evidence.
