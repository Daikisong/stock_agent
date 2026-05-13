# Checkpoint 9 Report

## Scope

Checkpoint 9 adds a real source collection layer and a historical case loader on top of the deterministic E2R 2.0 core.

The new flow is:

```text
source fixture or live request plan
-> normalized E2R raw model
-> Evidence
-> FeatureEngineeringInput
-> ScoringPayload
-> StageSnapshot
-> BacktestResult
```

Example:

```text
OpenDART contract fixture
-> DisclosureEvent(contract_duration_months=60, contract_amount_to_prior_sales=0.3707)
-> Evidence
-> contract_quality / backlog_rpo_visibility
-> Stage 3 or Red Team monitoring
```

## Files Added

- `src/e2r/sources/`
  - `krx.py`
  - `opendart.py`
  - `kind.py`
  - `naver_news.py`
  - `naver_webdoc.py`
  - `sec_edgar.py`
  - `report_search.py`
  - `consensus.py`
  - `source_errors.py`
- `src/e2r/research/report_parser.py`
- `src/e2r/historical_cases/__init__.py`
- `data/raw/...` local source fixtures
- `data/historical_cases/*.json`
- `tests/test_sources.py`
- `tests/test_report_parser.py`
- `tests/test_historical_cases.py`
- `docs/source_collection_playbook.md`

## Source Connectors

Each connector now has:

- request builders for future live collection
- fixture mode as the default
- response normalizers into E2R models
- clear missing-credential errors for live-only paths

Implemented source coverage:

- KRX: instruments, price bars, market cap, trading value, 52-week range, listing risk flags from fallback rows
- OpenDART: disclosure search plans, contract/facility/dilution parsing, `DisclosureEvent` and `Evidence`
- KIND: managed issue, caution, halt, unfaithful disclosure, delisting-risk evidence and Red Team candidates
- Naver News: company/sector query templates, event extraction into `NewsItem` and `Evidence`
- Naver Web/Doc and report search: broker PDF/report metadata discovery in fixture mode
- SEC EDGAR: submissions/companyfacts request builders, companyfacts financial mapping, filing evidence
- Consensus CSV: KR/US estimates and revision rows, including FCF and street high/low EPS revisions

## Model Updates

- `ConsensusSnapshot` now includes `fcf_e`.
- `ConsensusRevision` now includes:
  - `street_high_eps_revision_1m`
  - `street_low_eps_revision_1m`
- `ResearchReport` now carries additional parsed fields such as FY3 estimates, 52-week high/low, return windows, ROE, OPM, backlog, new orders, CAPA, export ratio, US revenue ratio, ASP, lead-time, and shortage mentions.

## Historical Case Loader

Added fixture-backed historical cases for:

- HD현대일렉트릭
- 효성중공업
- 일진전기
- 산일전기
- 삼양식품
- 한화에어로스페이스
- NVIDIA
- Zoom
- 씨젠
- SMCI

One additional weak-valuation cable case is included to verify filtering behavior.

The loader can turn one JSON case into:

- `Instrument`
- `FinancialActual`
- `ConsensusSnapshot`
- `ConsensusRevision`
- `DisclosureEvent`
- `ResearchReport`
- `NewsItem`
- `Evidence`
- `FeatureEngineeringInput`
- `ScoreSnapshot`
- `StageSnapshot`
- `BacktestResult`

## Behavior Proven

New tests prove:

- HD현대일렉트릭 reaches Stage 3-Green from raw historical case data.
- 효성중공업 reaches Stage 3-Green after margin and target-revision evidence.
- A weak-valuation, weak-ROE/OPM cable case is filtered below high-confidence Stage 3.
- Zoom and 씨젠 one-off demand cases become Stage 3-Red.
- SMCI-like boom-bust path triggers 4B before 4C.
- Historical company names are not embedded in scoring, staging, Red Team, or feature logic.
- KRX, OpenDART, Naver News, report search, SEC EDGAR, and consensus CSV fixture paths normalize data correctly.
- Korean report text parsing extracts key fields and creates research evidence.

## Verification

```text
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 71 tests
OK
```

## Guardrails Preserved

- Fixture mode is the default.
- Live credentials are not required for tests.
- No live scraping was added.
- Request builders do not execute network calls.
- `as_of_date` and `available_at` remain enforced before scoring.
- Historical names appear in fixture data only, not deterministic logic.
- Deterministic scoring remains separate from narrative or LLM interpretation.
- The project remains a rerating detection and monitoring agent, not a direct investment-instruction tool.
