# Checkpoint 13 Report

## Scope

Checkpoint 13 adds the Korea free cheap-scan layer.

The new path is:

```text
KOSPI/KOSDAQ fixture universe
-> free official/quasi-official source scan
-> event candidates
-> targeted web-search query groups
-> FreeWebResearchRunner
```

Simple example:

```text
단일판매 공급계약 + 매출액 대비 30% + 거래대금 급증
-> CheapScanCandidate(reason_codes)
-> recommended_next_layer = deep_research
-> "{company} 장기공급계약 매출액 대비" query group
```

## Added Components

- `src/e2r/cheap_scan/models.py`
  - Adds `CheapScanCandidate`.
  - Adds `RecommendedNextLayer`: `none`, `event_search`, `deep_research`.

- `src/e2r/cheap_scan/korea_sources.py`
  - Adds `KoreaCheapScanSources` bundle.
  - Adds fixture-first `DataGoKrFSCConnector`.
  - Builds request metadata for FSC listed items, stock prices, financial info, disclosure info, and issuance info.
  - Reuses KRX, OpenDART, and KIND connectors.

- `src/e2r/cheap_scan/event_rules.py`
  - Adds deterministic cheap-scan rules for disclosure, price, financial, and risk signals.
  - Separates positive structural events from risk events.
  - Keeps dilution, audit, halt, managed issue, and delisting signals from becoming Green-style escalation.

- `src/e2r/cheap_scan/query_escalation.py`
  - Maps reason codes into targeted web-research queries.
  - Supports the Free Web Research Runner through an `EscalationQueryPlanner`.

- `src/e2r/cheap_scan/korea_scanner.py`
  - Loads Korean instruments.
  - Applies point-in-time source filtering.
  - Produces ranked candidates.
  - Escalates event/deep candidates into `FreeWebResearchRunner` under `SearchBudget`.

## Fixture Coverage

Added small Korea cheap-scan fixtures under `data/raw/korea_cheap_scan/`:

- KRX instruments and prices
- OpenDART disclosures and financial actuals
- KIND listing/risk flags
- data.go.kr FSC instruments and prices

The fixtures include:

- supply contract with contract amount above 10% of prior sales
- long-term contract plus trading value spike
- facility investment plus CAPA increase
- rights offering risk
- price-only runup without disclosure support
- managed/trading-halt risk
- financial turnaround rows

## Behavior Proven

Tests prove:

- supply contract above 10% of sales becomes an `event_search` candidate
- long-term contract plus price/volume confirmation becomes a `deep_research` candidate
- facility investment plus CAPA increase becomes an `event_search` candidate
- rights offering becomes a risk candidate, not a deep-research Green candidate
- price-only runup does not escalate to deep research
- managed/trading-halt status is marked as hard risk
- reason codes emit targeted search templates
- the scanner ranks a small KOSPI/KOSDAQ fixture universe
- future disclosures after `as_of_date` are not used
- at least one cheap-scan candidate is escalated into Free Web Research query groups

## Guardrails

- No paid financial API was added.
- No live API call is required in tests.
- Missing credentials are represented as request/credential errors, not crashes.
- `as_of_date` and `available_at` filtering remain point-in-time.
- Missing fields are not fabricated.
- Deterministic scoring remains separate from narrative interpretation.
- Output is rerating detection and monitoring context, not buy/sell wording.
