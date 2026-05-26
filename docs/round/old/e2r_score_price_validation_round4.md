# Round 4 Score-Price Validation

Round 4 adds a calibration layer, not a production scoring change.

The core question is:

```text
Did the score and Stage label match the later price path?
```

Easy example:

```text
as_of_date = 2023-07-27
Stage 3 evidence exists on or before 2023-07-27
-> after that date, we measure MFE/MAE, peak return, and 4B/4C timing
-> we do not use 2023-07-28+ reports as evidence for the original Stage
```

## New Case Fields

Round 4 expects the case library to store:

- `peak_return_from_stage3`
- `time_to_50pct`
- `time_to_100pct`
- `time_to_200pct`
- `stage_failure_type`

The new `stage_failure_type` values are:

- `green_success`
- `yellow_success`
- `stage2_watch_success`
- `false_green`
- `false_yellow`
- `should_have_been_red`
- `missed_structural`
- `unknown`

## Alignment Labels

- `aligned`: evidence, Stage, and price path agree.
- `false_positive_score`: scoring would have promoted a bad case.
- `missed_due_to_score`: evidence existed but score missed it.
- `price_moved_without_evidence`: price moved, but EPS/FCF evidence was missing.
- `evidence_good_but_price_failed`: evidence looked good, but price did not rerate.

## Archetype Notes

Platform/software:
MAU alone is not enough. ARPU, take rate, OPM, and FCF must explain the price path.

Robotics:
Strategic investment or MOU is Stage 1/2 material. Green needs actual revenue and margin conversion.

Construction/PF:
Orders cannot override PF, cash-flow, and credit risk.

Nuclear:
Policy headlines are not enough. Contract economics, project financing, and legal delay risk must be visible.

Biotech:
Clinical or approval news without revenue/royalty conversion is Green-blocked.

## Guardrails

- Do not change StageClassifier thresholds from Round 4.
- Do not use case records as candidate-generation input.
- Do not treat event premium as true structural rerating.
- Do not treat price-only rallies as structural evidence.
