# Checkpoint 28A Round 332 R11 Loop 17 Policy Geopolitics Disaster Event

## Scope

- Source round: `docs/round/round_332.md`
- Analyst round id: `round_260`
- Large sector: `POLICY_GEOPOLITICS_DISASTER_EVENT`
- Method: `trigger_level_backtest_v1_after_redteam`
- Production scoring changed: `false`
- Candidate-generation input: `false`
- Shadow weight only: `true`

This round adds policy, tax, political-risk, export-control, industrial-support, defense-dilution, labor-risk, and disaster calibration material. It is not production scoring.

## Files Added

- `src/e2r/sector/round332_r11_loop17_policy_geopolitics_disaster_event_trigger_validation.py`
- `src/e2r/cli/build_round332_r11_loop17_report.py`
- `tests/test_round332_r11_loop17_policy_geopolitics_disaster_event_trigger_validation.py`
- `data/e2r_case_library/cases_r11_loop17_round260.jsonl`
- `data/e2r_trigger_calibration/triggers_r11_loop17_round260.jsonl`
- `data/sector_taxonomy/round332_r11_loop17_policy_geopolitics_disaster_event_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round260_r11_loop17_v1.csv`
- `output/e2r_round332_r11_loop17_policy_geopolitics_disaster_event_trigger_validation/`

## Case Summary

- Case candidates: `9`
- Trigger rows: `12`
- Target archetypes: `9`
- Stage2-Actionable candidates: `3`
- Stage2 candidates: `5`
- Stage3-Green confirmed: `0`
- Stage4B watch cases: `8`
- Hard 4C cases: `1`
- Price unavailable cases: `2`

## Key Decisions

- Commercial Act reform is Stage2-Actionable because law passage and KOSPI reaction are visible. It is not company-level Green until buyback cancellation, dividend execution, or board action appears.
- Capital-gains tax reversal is Stage2 relief with tax 4B. The shock/reversal price path is visible, but transaction-tax and future-tax risks remain.
- Martial law is political-risk 4B with liquidity relief. Liquidity support can prevent systemic hard 4C, but it is not a Green signal.
- AI windfall tax comments and U.S. chip-waiver revocation are 4B overlays for AI/memory leaders. They must not be ignored as noise.
- Semiconductor support is Stage2 relief no-price until equipment/material orders, capex conversion, or company revenue appears.
- Hanwha Aerospace combines defense export Stage2 with dilution 4B. Order value and backlog must be scored together with equity-financing risk.
- Samsung strike threat is national-champion labor 4B, not hard 4C unless production disruption becomes material.
- Wildfire disaster is hard 4C at disaster/social level, but listed-stock hard 4C and MFE/MAE are not created without public price anchors.

## What Not To Change

- Do not apply shadow weights to production scoring.
- Do not use round 332 cases as candidate-generation input.
- Do not force Stage 3-Green from policy, geopolitical, labor, or disaster headlines.
- Do not create MFE/MAE without full adjusted OHLC.
- Do not treat liquidity backstop, policy support, export-control relief, or strike arbitration as Green without company execution and risk resolution.

## Verification

```bash
PYTHONPATH=src python -m unittest tests.test_round332_r11_loop17_policy_geopolitics_disaster_event_trigger_validation -v
PYTHONPATH=src python -m e2r.cli.build_round332_r11_loop17_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

Example interpretation: a 33T won semiconductor support package is useful Stage2 relief, but it is not the same as a supplier receiving orders. The evidence must move from policy money to company revenue before Stage3 can be considered.
