# SK Hynix Green Gate Autopsy - 2026-06-19

## Scope

- Target: SK hynix (`000660`)
- Operational sample: `as_of_date=2026-06-12`
- Patched run log: `output/0618_green_gate_live_patched_2026-06-12/000660/korea_live_lite/2026-06-12_run_log.json`
- Previous comparison run log: `output/0618_green_gate_live_current_2026-06-12/000660/korea_live_lite/2026-06-12_run_log.json`
- Mode: `fixture_mode=False`, `live_enabled=True`, `targeted_smoke_only=True`, live page fetch enabled, Codex theme route enabled.

SK hynix is also only a regression sample. The fix must generalize to any selected Korean candidate with the same evidence shape.

## Result

| Item | Before patch | After patch |
|---|---:|---:|
| Stage | 2 | 2 |
| visible_score | 68.0162 | 70.8603 |
| price_bars | 247 | 247 |
| financial_actuals | 5 | 5 |
| disclosures | 0 | 12 |
| consensus | 0 | 0 |
| consensus_revisions | 0 | 0 |
| research_reports | 20 | 21 |
| news_items | 19 | 10 |
| information_confidence_score | 3.0 | 3.75 |

The OpenDART disclosure wiring bug is fixed here too. The remaining block is broader than disclosure: consensus, revision, OP estimate, and FCF estimate sources are still missing.

## Current Score Shape

| Component | After patch |
|---|---:|
| eps_fcf_explosion_score | 20.0 |
| earnings_visibility_score | 13.5256 |
| bottleneck_pricing_score | 14.9822 |
| market_mispricing_score | 6.062 |
| valuation_rerating_score | 8.6446 |
| capital_allocation_score | 2.122 |
| information_confidence_score | 3.75 |
| risk_penalty | 0.0 |

This explains why it stays Stage 2. The pipeline sees strong EPS/FCF explosion evidence, but the market-mispricing and valuation components are not close enough for Stage 3, and the estimate bridge is incomplete.

Easy example: a company can have a strong growth story, but if the model cannot see the analyst revision, OP bridge, FCF bridge, and valuation runway as structured evidence, it treats the case as watch/actionable rather than Green.

## Evidence Fix Confirmed

Target-company OpenDART disclosure evidence after patch: 12 rows.

Examples:

- `분기보고서 (2026.03)`, 2026-05-15, routine
- `주요사항보고서(자기주식처분결정)`, 2026-05-13, unknown
- governance, large-group, ownership, and related-party disclosures in May and June 2026

These disclosures are now visible to feature engineering, but most are routine or non-contract filings. They improve official evidence coverage, not Green by themselves.

## Remaining Gaps

Material unresolved gaps after patch:

- `selected_revision_source_missing`
- `selected_fcf_source_missing`
- `selected_operating_profit_source_missing`
- theme-overheat guard still requests source-backed revenue, EPS, FCF, and valuation bridge
- date-unverified snippet evidence still exists
- independent consensus and consensus-revision families are missing

The post-score-gap loop added 20 queries and still hit the round limit. This means the LLM correctly asked for the right evidence families, but the current search/parser path did not convert them into structured OP/FCF/revision inputs.

## Latency Notes

Phase log showed repeated LLM/search cycles:

- Theme route round 0 to round 1: about 43 seconds.
- Round 1 route to initial web research: about 143 seconds.
- Post-parse expansion added 2 queries.
- Score-gap round 0 added 10 queries.
- Score-gap round 1 added another 10 queries.
- Final status: `score_gap_round_limit`.

The common bottleneck is now not only data availability. It is conversion of found documents into structured estimate/FCF/revision fields.

