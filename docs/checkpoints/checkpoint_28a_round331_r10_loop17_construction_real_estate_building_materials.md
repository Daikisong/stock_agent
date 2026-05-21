# Checkpoint 28A Round 331 R10 Loop 17 Construction Real Estate Building Materials

## Scope

- Source round: `docs/round/round_331.md`
- Analyst round id: `round_259`
- Large sector: `CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS`
- Method: `trigger_level_backtest_v1_after_redteam`
- Production scoring changed: `false`
- Candidate-generation input: `false`
- Shadow weight only: `true`

This round adds construction, real-estate PF, housing policy, value-up, and safety trigger calibration material. It is a case-library and validation pack only.

## Files Added

- `src/e2r/sector/round331_r10_loop17_construction_real_estate_building_materials_trigger_validation.py`
- `src/e2r/cli/build_round331_r10_loop17_report.py`
- `tests/test_round331_r10_loop17_construction_real_estate_building_materials_trigger_validation.py`
- `data/e2r_case_library/cases_r10_loop17_round259.jsonl`
- `data/e2r_trigger_calibration/triggers_r10_loop17_round259.jsonl`
- `data/sector_taxonomy/round331_r10_loop17_construction_real_estate_building_materials_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round259_r10_loop17_v1.csv`
- `output/e2r_round331_r10_loop17_construction_real_estate_building_materials_trigger_validation/`

## Case Summary

- Case candidates: `7`
- Trigger rows: `9`
- Target archetypes: `7`
- Stage2-Actionable candidates: `1`
- Stage2 candidates: `4`
- Stage3-Green confirmed: `0`
- Stage4B watch cases: `6`
- Hard 4C cases: `1`
- Price unavailable cases: `3`

## Key Decisions

- Samsung E&A Fadhili is Stage2-Actionable because the 6B USD EPC contract and +8.5% event reaction are visible. It is not Green until progress billing, EPC margin, schedule, and cash collection are visible.
- Czech nuclear is Stage2 with legal 4B. A preferred bidder result is useful evidence, but final contract, legal appeal clearance, listed-company scope, and margin must be verified.
- Seoul housing supply policy is Stage2 no-price. Policy and housing-price movement are not the same as builder EPS/FCF until permits, pre-sales, backlog, and cash conversion appear.
- PF restructuring and builder liquidity are relief paths. They remain 4B/Stage2 relief until bad-project cleanup, refinancing, and pre-sale cash recovery are visible.
- Samsung C&T value-up failed rerating is kept as a counterexample. Activist pressure without board-approved capital return and share cancellation is not enough.
- Fatal construction-site safety is hard 4C style evidence. With no listed stock-price anchor, it is sector/project risk evidence rather than a positive candidate.

## What Not To Change

- Do not apply these shadow weights to production scoring yet.
- Do not use round 331 cases as candidate-generation input.
- Do not force Stage 3-Green from construction headlines.
- Do not create MFE/MAE without full adjusted OHLC.
- Do not treat policy support, preferred-bidder status, or liquidity packages as Green without margin, final contract, permits, PF cleanup, board action, or safety clearance.

## Verification

```bash
PYTHONPATH=src python -m unittest tests.test_round331_r10_loop17_construction_real_estate_building_materials_trigger_validation -v
PYTHONPATH=src python -m e2r.cli.build_round331_r10_loop17_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

Example interpretation: a large EPC contract is like a signed project backlog. It can justify Stage2 monitoring, but if the project later shows cost overrun or slow receivables, the EPS/FCF bodyweight may never materialize. That is why the round keeps contract headlines below Green until cash and margin evidence appear.
