# Checkpoint 10 Report

## Scope

Checkpoint 10 adds the local daily scan runner. It takes fixture, CSV, JSON, and parsed text data and produces a Korean morning brief plus machine-readable JSON.

The new execution path is:

```text
DailyScanConfig
-> DailyScanRunner
-> CompanyResearchPipeline per symbol
-> FeatureEngineeringInput
-> ScoreSnapshot
-> RedTeamAssessment
-> StageSnapshot
-> MorningBrief
-> output files
```

Simple example:

```text
data/historical_cases/hd_hyundai_electric_2023.json
-> raw financials, consensus, disclosure, report, news, prices
-> Stage 3-Green
-> Korean morning brief row
```

## Files Added

- `src/e2r/pipeline/__init__.py`
- `src/e2r/pipeline/daily_scan.py`
- `src/e2r/pipeline/company_research.py`
- `src/e2r/pipeline/evidence_builder.py`
- `src/e2r/pipeline/stage_update.py`
- `src/e2r/pipeline/morning_pipeline.py`
- `tests/test_daily_scan.py`

## DailyScanConfig

`DailyScanConfig` now supports:

- `as_of_date`
- `markets`
- `connector_bundle`
- `universe_limit`
- `active_watchlist_symbols`
- `output_directory`
- `fixture_mode`
- `include_historical_cases`
- `historical_case_dir`
- `lookback_days`

## ConnectorBundle

`ConnectorBundle` contains:

- `krx`
- `opendart`
- `kind`
- `naver_news`
- `naver_webdoc`
- `report_search`
- `consensus`
- `sec_edgar`

`ConnectorBundle.local_defaults()` wires the CP9 local fixture connectors together. Tests can also pass an empty bundle to prove missing data is handled without a crash.

## CompanyResearchPipeline

For one instrument the pipeline now:

- collects price bars
- collects financial actuals
- collects consensus and revisions
- collects disclosures
- collects news
- collects report search results
- parses report text when a fixture has `extracted_text`
- builds Evidence records
- builds `FeatureEngineeringInput`
- runs `DeterministicFeatureEngineer`
- runs `RedTeamEngine`
- runs `StageClassifier`
- optionally runs backtest when a Stage 3 date is available

Point-in-time handling remains enforced by the model validators and by the historical case feature input filter.

## DailyScanRunner

The runner now:

- lists instruments from local source connectors
- can include `data/historical_cases` as a fixture universe
- adds active watchlist symbols even if no connector has data
- filters invalid instruments such as halted, managed, preferred, ETF, SPAC, REIT rows
- runs one company pipeline per symbol
- collects scores, stages, evidence, Red Team findings, and backtests
- generates a Korean morning brief
- writes:

```text
{output_directory}/morning_briefs/YYYY-MM-DD.md
{output_directory}/morning_briefs/YYYY-MM-DD.json
```

The JSON output contains compact stage, score, evidence, backtest, and per-company summaries.

## Historical Case Integration

Historical cases can be scanned as a universe:

```python
DailyScanRunner().run(
    DailyScanConfig(
        as_of_date=date(2026, 5, 14),
        include_historical_cases=True,
        historical_case_dir="data/historical_cases",
    )
)
```

In tests:

- HD현대일렉트릭 appears as Stage 3-Green.
- Zoom appears as Stage 3-Red.
- Stage 3-Green and Stage 3-Red both appear in the generated output.
- Future outcome price bars are used only for backtest, not feature scoring.

## Tests Added

New tests verify:

- daily runner scans the historical fixture universe
- stage snapshots are produced
- evidence records are produced
- Korean morning brief text is generated
- markdown and JSON outputs are written
- future data is excluded from feature scoring
- missing connector data is handled gracefully
- Stage 3-Green and Stage 3-Red both appear in fixture output

## Verification

```text
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 76 tests
OK
```

## Guardrails

- No live API calls were added.
- No scraping was added.
- Fixture/local data remains the default.
- `as_of_date` and `available_at` checks remain in the data models.
- The morning brief still rejects direct recommendation wording.
- Deterministic scoring remains separate from narrative interpretation.
