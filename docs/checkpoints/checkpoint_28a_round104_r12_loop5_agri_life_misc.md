# Checkpoint 28A Round 104 R12 Loop-5 Agriculture / Life Services / Misc

## Summary

Round 104 expanded the R12 agriculture, life services, education, rental, kiosk, and regulated-consumer calibration pack.

This is calibration material only. It does not change production scoring, StageClassifier thresholds, E2R_STANDARD candidate generation, or RedTeam logic.

## What Changed

- Added the Round104 R12 Loop-5 module:
  - `src/e2r/sector/round104_r12_loop5_agri_life_misc.py`
  - `src/e2r/cli/build_round104_r12_loop5_report.py`
  - `tests/test_round104_r12_loop5_agri_life_misc.py`
- Added missing canonical archetype enum members used by Round104.
- Generated case and score-profile outputs:
  - `data/e2r_case_library/cases_r12_loop5_round104.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round104_r12_loop5_v5.csv`
  - `output/e2r_round104_r12_loop5_agri_life_misc/`

## Coverage

- target_count: 28
- case_candidate_count: 21
- success_candidate_count: 5
- cyclical_success_count: 2
- event_premium_count: 2
- failed_rerating_count: 4
- stage4b_case_count: 3
- stage4c_case_count: 8
- green_possible_count: 0
- watch_yellow_first_count: 17
- redteam_first_count: 11
- gate_only_target_count: 6

## Main Guardrails

- R12 essential-demand labels are not Green evidence by themselves.
- Smart farm and vertical farming need orders, utilization, energy cost, unit economics, and FCF.
- Agri machinery demand must pass farm-income, crop-price, financing-cost, and dealer-inventory checks.
- Education AI features need bookings, paid conversion, margin, CAC, and FCF.
- Rental and kiosk stories need recurring service economics, not hardware installation count alone.
- Regulated consumer products need authorization scope, channel, public-health checks, and repeat revenue.

Simple example: a self-checkout rollout can look productive, but if a city requires item limits or staffed lanes, the kiosk economics may be capped. Round104 records that as a RedTeam overlay, not positive evidence.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round104_r12_loop5_agri_life_misc -v
PYTHONPATH=src python -m e2r.cli.build_round104_r12_loop5_report
```

Round104-specific tests passed.

## Production Safety

- Production scoring changed: no
- Case records used as candidate-generation input: no
- Stage 3-Green loosened: no
- API keys written: no
- Buy/sell recommendation wording added: no

## Next Step

Use this pack as calibration/evaluation input for later shadow scoring only after enough price paths, evidence dates, and false-positive examples are backfilled.
