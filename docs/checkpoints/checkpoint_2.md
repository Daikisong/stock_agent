# Checkpoint 2 Report

## Files Changed

- `src/e2r/red_team.py`
- `src/e2r/staging.py`
- `src/e2r/__init__.py`
- `tests/test_red_team.py`
- `tests/test_staging.py`
- `docs/checkpoints/checkpoint_2.md`

## What Was Implemented

- Added deterministic Red Team thesis-break monitoring:
  - `RedTeamSignals`
  - `RedTeamAssessment`
  - `RedTeamEngine`
  - `RedTeamRiskLevel`
- Implemented 4B Soft Exit scoring from the spec:
  - return since Stage 3
  - 12-24 month return
  - extreme forward valuation
  - EPS/FCF revision slowdown
  - backlog/RPO/contract slowdown
  - market crowding
  - insider/major event
  - blow-off price pattern
- Implemented Red Team thesis-break scoring:
  - EPS/FCF revision down
  - backlog/RPO decline
  - new order slowdown
  - contract cancellation/delay
  - OPM decline
  - ASP decline
  - supply glut
  - customer capex decline
  - accounting/trust issue
  - cash-flow deterioration
  - receivables/inventory spike
- Added hard-break handling for:
  - contract cancellation/delay
  - accounting/trust issue
  - thesis-break score at or above the hard-break threshold
- Added deterministic stage classifier:
  - `StageClassificationInput`
  - `StageClassifier`
- Implemented the canonical stage outputs:
  - Stage 0
  - Stage 1
  - Stage 2
  - Stage 3-Green
  - Stage 3-Yellow
  - Stage 3-Red
  - Stage 4A
  - Stage 4B
  - Stage 4C
  - Stage 5
- Added point-in-time guardrail:
  - Red Team assessment date cannot be after the score snapshot date.
- Added precedence rules:
  - archive/coverage-impossible conditions can produce Stage 5.
  - hard thesis-break conditions produce Stage 4C before any high-score classification.
  - Soft 4B score can move active Stage 3/4 cases to Stage 4B.
  - supported active thesis can move Stage 3 cases to Stage 4A.
  - Stage 3-Green requires high score, required component thresholds, positive revision score, and low Red Team risk.
  - Stage 3-Yellow captures high-score cases where Green conditions are incomplete.
  - Stage 3-Red captures high-score cases with high Red Team, weak valuation runway, weak visibility, weak bottleneck quality, or theme-overheat diagnostics.

## How It Was Verified

Commands run:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Test result:

```text
Ran 22 tests in 0.002s
OK
```

New test coverage includes:

- weighted 4B Soft Exit score
- Red Team finding creation
- hard-break override
- unknown Red Team signal rejection
- Stage 0 industry-regime classification
- Stage 1 company-event classification
- Stage 2 candidate threshold
- Stage 3-Green
- Stage 3-Yellow
- Stage 3-Red
- Stage 4A
- Stage 4B
- Stage 4C hard-break precedence
- future Red Team data rejection

## What Remains

- Checkpoint 3: implement the point-in-time backtesting engine with MFE/MAE, pre-runup, time-to-4B/4C, and below-entry metrics.
- Checkpoint 4: add fixture cases for success, warning, failure, peak-out, and US boom/bust behavior.
- Checkpoint 5: add mock/fallback data connectors.
- Checkpoint 6: add Korean morning briefing generator.
- Checkpoint 7: add integration tests and final review.

## Assumptions Or Missing Data

- Red Team signal inputs are normalized 0.0 to 1.0 at this checkpoint. Later connector/parser layers can map raw data into those normalized factors.
- Stage classifier uses only `ScoreSnapshot`, `RedTeamAssessment`, and explicit as-of-date classification inputs. It does not inspect future bars, future reports, or historical labels.
- Stage 4B output is descriptive as a graduation/crowding watch state. It does not make buy/sell recommendations.
- No historical winner names are used in the stage or Red Team logic.
- Stage classifier currently assigns simple grades from total score for display. The grade system can be expanded after fixture and integration tests.

