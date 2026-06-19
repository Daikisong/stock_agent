# Samsung Green Gate Autopsy - 2026-06-19

## Scope

- Target: Samsung Electronics (`005930`)
- Operational sample: `as_of_date=2026-06-12`
- Patched run log: `output/0618_green_gate_live_patched_2026-06-12/005930/korea_live_lite/2026-06-12_run_log.json`
- Previous comparison run log: `output/0618_green_gate_live_current_2026-06-12/005930/korea_live_lite/2026-06-12_run_log.json`
- Mode: `fixture_mode=False`, `live_enabled=True`, `targeted_smoke_only=True`, live page fetch enabled, Codex theme route enabled.

Samsung is a regression thermometer here. No production rule was allowed to key on `005930` or the company name.

## Result

| Item | Before patch | After patch |
|---|---:|---:|
| Stage | 3-Yellow | 3-Yellow |
| visible_score | 78.8721 | 78.41 |
| price_bars | 247 | 247 |
| financial_actuals | 5 | 5 |
| disclosures | 0 | 23 |
| consensus | 1 | 1 |
| consensus_revisions | 0 | 1 |
| research_reports | 22 | 33 |
| news_items | 21 | 10 |
| information_confidence_score | 3.0 | 3.75 |

The patch fixed the obvious wiring bug: recent target-company OpenDART disclosures now reach `FeatureEngineeringInput.disclosures`, and at least one revision-like source reaches the score path. This did not force Green.

## Current Score Shape

| Component | After patch |
|---|---:|
| eps_fcf_explosion_score | 20.0 |
| earnings_visibility_score | 13.9341 |
| bottleneck_pricing_score | 16.2009 |
| market_mispricing_score | 11.0405 |
| valuation_rerating_score | 9.979 |
| capital_allocation_score | 2.0183 |
| information_confidence_score | 3.75 |
| risk_penalty | 0.0 |

The Green block is not a single missing file anymore. It is the combination of:

- total score still below the Green region;
- earnings visibility below the Green threshold area;
- valuation rerating just below the Green threshold area;
- FCF source still missing;
- revision exists but is weak and report-derived, not a strong independent consensus revision;
- score-gap expansion ended with provider timeout in this run.

Easy example: the pipeline sees a strong engine (`eps_fcf=20`) and decent road condition (`bottleneck`, `mispricing`), but it still does not see enough fuel gauge and brake evidence: FCF, durable revision, and valuation runway.

## Evidence Fix Confirmed

Target-company OpenDART disclosure evidence after patch: 23 rows.

Examples:

- `분기보고서 (2026.03)`, 2026-05-15, routine
- `동일인등출자계열회사와의상품ㆍ용역거래변경`, 2026-05-15, unknown
- ownership and major holder reports in May and June 2026

These should not by themselves create Green. They now correctly serve as official source-backed filings that can support date verification and future parser extraction.

## Remaining Gaps

Material unresolved gaps after patch:

- `selected_fcf_source_missing`
- emerging-theme deep research not completed because the provider timed out
- date-unverified snippet evidence still exists
- independent consensus and consensus-revision families are still not strong enough for Green

The most important remaining source gap is not "more news." It is source-backed FCF/operating cash flow conversion and stronger estimate revision evidence.

## Latency Notes

Phase log showed material LLM latency:

- Initial theme route: about 180 seconds.
- Theme evidence review: about 50 seconds.
- Post-parse expansion added 7 queries.
- Score-gap route then hit provider timeout before adding post-score-gap queries.

So the operating bottleneck is partly data wiring and partly LLM/provider latency.

