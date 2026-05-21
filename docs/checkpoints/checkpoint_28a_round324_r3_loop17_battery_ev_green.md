# Checkpoint 28A Round 324: R3 Loop 17 Battery / EV / Green Validation

## Scope

- Source round: `docs/round/round_324.md`
- Analyst round id: `round_252`
- Large sector: `SECONDARY_BATTERY_EV_GREEN`
- Method: `trigger_level_backtest_v1_after_redteam`
- Production scoring changed: `false`
- Candidate generation input: `false`
- Shadow weight only: `true`

This patch converts the round into calibration-only data. It does not make any case easier to reach Stage 3-Green.

Easy example: Samsung SDI's ESS LFP contract can be a Stage2-Actionable signal because contract size and event return are clear. It is still not Green until customer, delivery, utilization, margin, and full OHLC validation are present.

## Added Archetypes

The round requires eight exact archetype aliases:

- `ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE`
- `EV_CONTRACT_CANCELLATION_4C`
- `SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH`
- `LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2`
- `SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE`
- `IRA_AMPC_EARNINGS_WITH_POLICY_4B`
- `CAPITAL_RAISE_DILUTION_4B`
- `UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE`

Six missing aliases were added to `E2RArchetype`; the two existing aliases were reused.

## Case Pack

Generated case records:

- Case candidates: `8`
- Trigger rows: `9`
- Stage2-Actionable candidates: `1`
- Stage2 candidates: `5`
- Stage3-Yellow candidates: `4`
- Stage3-Green confirmed: `0`
- Stage4B-watch count: `5`
- Strong 4C cases: `1`

Core interpretation:

- Samsung SDI ESS LFP: clean Stage2-Actionable anchor.
- LGES Ford/Freudenberg cancellations: hard 4C contract-quality break.
- SK On ESS pivot: Stage2, but parent readthrough and losses remain 4B-watch.
- POSCO Future M / L&F lithium rebound: cyclical Stage2, not Green.
- Samsung SDI solid-state timeline: Stage3-Yellow candidate, not Green before pilot yield and revenue.
- LGES AMPC earnings: policy-credit 4B because ex-AMPC margin is near zero.
- Samsung SDI capital raise: dilution 4B.
- POSCO / MinRes lithium JV: Stage2 no-price until direct KRX price, offtake, and margin are available.

## Green Blockers

Green remains blocked by:

- ESS headline without customer, margin, and delivery.
- EV backlog without cancellation check.
- AMPC credit dependency.
- Solid-state timeline without revenue.
- Lithium rebound without durability.
- Capital raise dilution.
- Unlisted subsidiary readthrough overstated into listed parent.
- Missing full adjusted OHLC for MFE/MAE validation.

## Files Generated

- `src/e2r/sector/round324_r3_loop17_secondary_battery_ev_green.py`
- `src/e2r/cli/build_round324_r3_loop17_report.py`
- `tests/test_round324_r3_loop17_secondary_battery_ev_green.py`
- `data/e2r_case_library/cases_r3_loop17_round252.jsonl`
- `data/e2r_trigger_calibration/triggers_r3_loop17_round252.jsonl`
- `data/sector_taxonomy/round324_r3_loop17_secondary_battery_ev_green_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round252_r3_loop17_v1.csv`
- `output/e2r_round324_r3_loop17_secondary_battery_ev_green/`

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round324_r3_loop17_secondary_battery_ev_green -v
PYTHONPATH=src python -m e2r.cli.build_round324_r3_loop17_report
```

Additional full-suite verification is tracked in the commit notes for this round.

## What Not To Change

- Do not change production scoring from this round alone.
- Do not use round 324 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds.
- Do not invent full MFE/MAE without adjusted OHLC.
- Do not treat ESS contracts, AMPC profit, lithium rebound, solid-state timelines, or dilution events as Green without customer, margin, utilization, revenue, and risk-resolution evidence.
