# Checkpoint 21 Live Shadow Validation

## Purpose

Checkpoint 21 adds an operator command for post-Checkpoint20 shadow validation.

It runs the same live-lite pipeline in a gated sequence:

```text
tiny
-> targeted smoke
-> small
-> optional standard_shadow only if gates pass
```

The command is conservative. Fixture mode is safe for CI and local checks. Live mode must be explicit.

## Command

Fixture mode:

```bash
PYTHONPATH=src python -m e2r.cli.run_korea_shadow_validation \
  --date YYYY-MM-DD \
  --fixture \
  --output-directory output
```

Live mode:

```bash
PYTHONPATH=src python -m e2r.cli.run_korea_shadow_validation \
  --date YYYY-MM-DD \
  --live \
  --output-directory output
```

Optional standard shadow:

```bash
PYTHONPATH=src python -m e2r.cli.run_korea_shadow_validation \
  --date YYYY-MM-DD \
  --live \
  --standard-shadow \
  --output-directory output
```

`standard_shadow` runs only if tiny, targeted smoke, and small gates pass.

## Output Layout

Each step gets its own output folder so files do not overwrite each other:

```text
output/korea_shadow_validation/tiny/korea_live_lite/
output/korea_shadow_validation/targeted_smoke/korea_live_lite/
output/korea_shadow_validation/small/korea_live_lite/
output/korea_shadow_validation/standard_shadow/korea_live_lite/
```

Each step includes:

```text
candidates.json
evidence.json
brief.md
run_log.json
cheap_scan_calibration.json
cheap_scan_calibration.md
review summary
```

The top-level summary is written to:

```text
output/korea_shadow_validation/YYYY-MM-DD_summary.md
```

## Gates

The gate checks:

```text
no API key leaks
source_modes are known
live_requests_failed is not excessive
rate_limit_skips are explainable
routine_audit_count is not flooding
high_signal_audit_count is bounded
targeted smoke is excluded from production candidates
Stage 3-Green still requires cross-evidence
no hard audit finding remains Green
```

Simple example:

```text
targeted smoke query runs
-> real evidence not found
-> run_log.targeted_smoke_results records insufficient_evidence
-> production candidates and brief do not include the smoke symbol
```

## Standard Shadow Decision

The command does not guess. It only runs `standard_shadow` when:

```text
tiny gate = pass
targeted smoke gate = pass
small gate = pass
--standard-shadow was explicitly requested
```

This keeps broad shadow runs tied to evidence from the run logs, not optimism.
