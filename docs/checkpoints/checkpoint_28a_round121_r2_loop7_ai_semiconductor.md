# Checkpoint 28A Round 121 R2 Loop 7 AI / Semiconductor / Electronics

Round 121 reflects `docs/round/round_121.md` as a calibration-only R2 Loop 7 pack.

This round does not change production scoring. It adds evidence tables that ask a narrower question:

```text
Did the score table catch the right stage?
Did that stage match the observed price path?
Which weight should be raised, capped, or blocked next?
```

Simple example:

```text
Samsung HBM4 shipment can be Stage 2.
It is not Stage 3-Green until qualification, yield, volume shipment, and EPS conversion are verified.
```

## Files Added

- `src/e2r/sector/round121_r2_loop7_ai_semiconductor.py`
- `src/e2r/cli/build_round121_r2_loop7_report.py`
- `tests/test_round121_r2_loop7_ai_semiconductor.py`
- `data/e2r_case_library/cases_r2_loop7_round121.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round121_r2_loop7_v7.csv`
- `output/e2r_round121_r2_loop7_ai_semiconductor/`

## Archetype Changes

Added one calibration archetype:

- `HBM_CATCHUP_EXECUTION_RISK`

This separates Samsung/Micron-style catch-up upside from labor, yield, volume shipment, qualification, and foundry execution risk.

## Summary Counts

Generated from `output/e2r_round121_r2_loop7_ai_semiconductor/round121_r2_loop7_ai_semiconductor_summary.md`:

- target_count: 27
- case_candidate_count: 24
- base_score_component_count: 7
- stage_cap_count: 5
- score_stage_price_alignment_count: 12
- structural_success_count: 1
- success_candidate_count: 13
- event_premium_count: 1
- overheat_count: 2
- failed_rerating_count: 2
- stage4b_case_count: 5
- stage4c_case_count: 1
- green_possible_count: 6
- watch_yellow_first_count: 15
- redteam_first_count: 6
- hard_gate_target_count: 3
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## R2 v7 Base Score Weights

- EPS/FCF revision: 25
- Customer / shipment / revenue visibility: 22
- Bottleneck / pricing power: 19
- Market mispricing gap: 12
- Valuation room / 4B runway: 8
- Capital discipline / FCF stability: 6
- Information confidence / disclosure detail: 8

These are report-only calibration weights. They are not applied to `features.py`, `staging.py`, `red_team.py`, or `e2r_standard_flow.py`.

## Stage Caps

- Stage 1 cap: theme/narrative only, maximum 45
- Stage 2 cap: customer, shipment, contract, order, or guidance exists, maximum 70
- Stage 3: OP/EPS/FCF plus margin or capital return plus price-path alignment
- Stage 4B: good structure but already rerated or crowded
- Stage 4C: accounting, filing, circular financing, FCF/debt, labor/production hard RedTeam

## Core Round 121 Interpretation

- SK하이닉스 HBM is a structural success pattern, but the same evidence also turns on 4B-watch after a huge rerating.
- Samsung HBM4 shipment and AMD MOU are Stage 2 evidence, not automatic Stage 3.
- Kioxia AI storage NAND validates the shortage/profit path, but a 20x stock move makes valuation risk central.
- Applied Materials, Broadcom, Cisco, and Tower show score-to-stage-to-price alignment.
- Foxconn AI server evidence is real revenue evidence, but ODM margin power remains capped.
- Supermicro shows accounting trust is a hard 4C gate.
- CoreWeave shows contract visibility can be contaminated by circular financing and leverage.
- Cerebras shows IPO event premium is not structural Green.
- Ecolab-CoolIT shows AI cooling M&A can still fail the valuation/accretion test.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round121_r2_loop7_ai_semiconductor -v
PYTHONPATH=src python -m e2r.cli.build_round121_r2_loop7_report
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

Results:

- Round 121 tests: 13 passed
- Full test suite: 1572 passed

## Guardrails

- Do not treat all AI beneficiaries as one archetype.
- Do not use case records as candidate-generation input.
- Do not change production scoring yet.
- Do not invent contract values, customers, margins, HBM yield, stage prices, or FCF.
- Do not make CXL, glass substrate, neuromorphic, or AI chip related-stock keywords Green evidence without revenue.
- Accounting trust breaks remain hard RedTeam events.
