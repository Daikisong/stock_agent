# Checkpoint 20 Detail Fetch, Calibration, and Recall

## What Changed

Checkpoint 20 improves the live-lite quality loop after the first live validation produced zero candidates and too many low-confidence OpenDART list findings.

The key design is:

```text
Layer 1 = broad recall
Stage 3-Green = strict precision
```

Simple example:

```text
OpenDART list: "단일판매·공급계약체결"
-> enough to route a candidate to event_search
-> not enough by itself for Stage 3-Green
-> document.xml detail fetch must parse amount/duration or another independent evidence type must confirm
```

## OpenDART Detail Fetch

The runner now plans and can execute capped OpenDART `document.xml` detail fetches for watch disclosures only.

Watch examples:

```text
단일판매·공급계약체결
신규시설투자
잠정실적
영업실적 전망
유상증자 / 전환사채 / 신주인수권부사채
감사의견 / 거래정지
계약 해지 / 계약 취소 / 계약 정정
```

Routine list rows are not detail-fetched.

Caps:

```text
tiny: 3
small: 10
standard_shadow: 50
```

Raw XML and extracted text are cached under:

```text
data/cache/opendart_detail/YYYY-MM-DD/
```

The parser extracts only explicit fields, for example:

```text
contract_amount
contract_amount_to_prior_sales
contract_start / contract_end / contract_duration_months
counterparty
product_or_service
facility_investment_amount
facility_investment_to_market_cap
expected_completion_date
op_yoy_pct
dilution_type
```

Missing fields stay missing. The parser does not fill blanks from a company name or from historical winners.

## Disclosure Signal Filtering

OpenDART list disclosures are classified as:

```text
high_signal
risk_signal
routine
unknown
```

Routine examples:

```text
투자설명서
일괄신고
증권발행실적보고서
단순 행정 정정
```

Routine rows may be stored, but they do not create positive cheap-scan score, do not trigger detail fetch, and do not count as independent evidence for Stage 3-Green.

Risk rows remain visible to Red Team.

## Cheap-Scan Calibration

Each run writes:

```text
output/korea_live_lite/YYYY-MM-DD_cheap_scan_calibration.json
output/korea_live_lite/YYYY-MM-DD_cheap_scan_calibration.md
```

The report includes:

```text
reason-code distribution
dropped reason distribution
near-miss top 50
top high-signal disclosures
top price-signal instruments
top financial-signal instruments
risk-blocked instruments
missing price bars
```

This report is diagnostic. It is not a way to force candidates.

## Report Radar

Report Radar adds a light search path for high-signal research phrases such as:

```text
목표주가 상향 EPS 상향 PDF
컨센서스 상회 Review PDF
수주잔고 OPM 수출 비중 PDF
장기공급계약 매출액 대비 PDF
ASP 상승 판가 상승 리드타임 PDF
```

It uses a capped universe slice and `SearchBudget`. It does not deep-search every listed company.

Report Radar candidates are marked:

```text
candidate_source_path = report_radar
```

They may enter event search or deep research, but they cannot become Stage 3-Green without normal evidence rules.

## Targeted Smoke

Targeted smoke is a pipeline test, not evidence.

Smoke candidates are marked:

```text
test_injected = True
candidate_source_path = targeted_smoke
production_candidate = False
```

They are excluded from production candidate JSON and from the production morning brief. If no real search result or parsable document is found, the run records `insufficient_evidence`.

## Parser Audit Refinement

Routine OpenDART list rows no longer flood low-confidence audit findings. Detail evidence and high-signal/risk evidence are still audited normally.

Run log now includes:

```text
audit_findings_by_source_type
audit_findings_by_signal_class
high_signal_audit_count
routine_audit_count
```

Hard audit findings still block Stage 3-Green.

## Tests

Added or extended tests cover:

```text
OpenDART detail fetch cap/cache/parser
routine list audit suppression
cheap-scan calibration output
Report Radar source path and budget behavior
targeted smoke exclusion from production output
historical Layer-1 recall backtest
one-off cases not becoming Stage 3-Green
SMCI-like 4B before 4C
```
