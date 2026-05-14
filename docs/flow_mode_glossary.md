# Flow Mode Glossary

## Production Flow

```text
E2R_STANDARD
```

This is the canonical flow for live runs and serious blind backtests.

It means:

```text
official cheap scan
-> detail fetch
-> Report Radar
-> Free Web Research
-> evidence
-> deterministic score
-> StageClassifier
-> Red Team
-> audit
-> lifecycle monitor
```

## Diagnostic Modes

These are not production flow:

```text
official_only
case_fixture
hybrid
```

They are for:

```text
evidence coverage diagnosis
regression testing
fixture replay
mode comparison
```

## Important Warning

```text
case_fixture success is regression success,
not proof of live discovery.
```

Example:

```text
case_fixture includes an old broker report.
E2R_STANDARD blind discovery must prove the agent could find or had archived that report.
```

## Benchmark Labels

Benchmark labels are evaluation-only.

They must never be input to:

```text
cheap scan
Report Radar
web research
feature engineering
StageClassifier
RedTeam
```

They are used only after candidates are generated.

## Fixture Proxy

`--allow-fixture-source-proxy` is a diagnostic escape hatch.

It means:

```text
curated historical case fixtures may stand in for missing archived sources
```

It does not mean:

```text
the agent would have found the same evidence live on that date
```

So the user-facing interpretation is:

```text
fixture proxy success = regression success
true E2R_STANDARD success = blind discovery evidence
```
