# Semis Green Gate Generalization Plan - 2026-06-19

## What Was Actually Fixed

Two generic wiring fixes were applied.

1. Selected-candidate OpenDART disclosures are fetched by official corp code after candidate selection.
   - Before: market-wide date-range preload used the short cheap-scan window, so selected candidates often had `disclosures=0`.
   - After: the selected candidate gets its own 30-day disclosure window without scanning the whole market for 30 days.
   - This is generic for all Korean candidates, not semiconductor-specific.

2. CompanyGuide/WiseReport fields are preserved better.
   - Broker target-table numeric revisions can become `ConsensusRevision` when available.
   - Recent-report action labels such as target-price up/down and EPS up/down are stored as directional parsed fields.
   - Directional labels do not invent numeric revision percentages.

The patch also serializes `stage_gate_diagnostics` and `failed_green_gates` into future targeted smoke run logs. The full Samsung/Hynix reruns in this note were completed just before that serialization patch, so their run logs show the score components and material gaps but not the new serialized gate object.

## Why They Still Did Not Become Green

Green requires more than high EPS/FCF score.

Common remaining requirements:

- total score needs to reach the Green band;
- earnings visibility needs stronger source-backed revenue/OP/FCF bridge;
- valuation rerating needs clearer runway;
- revision score needs a strong selected source;
- FCF source needs to be visible;
- theme evidence must be date-verified and source-backed;
- LLM route/score-gap expansion must complete or fail in a way the run can diagnose.

Simple example: a report saying "HBM demand is strong" is a good clue. Green needs "this company has source-backed volume, margin, revision, FCF, and valuation evidence as of the decision date."

## Current Evidence Shape

| Symbol | Stage | Score | Fixed disclosure? | Fixed revision? | Still missing |
|---|---:|---:|---:|---:|---|
| 005930 | 3-Yellow | 78.41 | yes, 23 rows | partly, 1 report-derived revision | FCF source, stronger revision, visibility, valuation, provider completion |
| 000660 | 2 | 70.8603 | yes, 12 rows | no | OP source, FCF source, revision source, consensus, valuation/mispricing |

## What Not To Do

- Do not lower Stage 3-Green thresholds to force promotion.
- Do not add `005930`, `000660`, `삼성전자`, or `하이닉스` conditions.
- Do not turn routine filings into Green evidence by themselves.
- Do not create fake revision percentages from the word "상향."

## Next General Work

1. Improve FCF and operating cash flow extraction from full reports, IR pages, and DART filings.
2. Improve CompanyGuide snapshot parsing coverage when consensus tables are incomplete or shaped differently.
3. Add parser routes for OP estimate/revision fields from broker PDFs and full-page fetched reports.
4. Keep score-gap context shorter but more structured: current runs spend too much time in route/review loops.
5. Use the new `stage_gate_diagnostics` fields in future run review CLI output.

## Verification Performed

- `PYTHONPATH=src python -m unittest tests.test_sources tests.test_report_consensus_proxy ... tests.test_stage_gate_diagnostics -v`
- `PYTHONPATH=src python -m unittest discover -s tests -v` (`3857` tests passed)
- `python -m py_compile src/e2r/pipeline/korea_live_lite.py src/e2r/sources/company_guide.py src/e2r/research/free_web_research_runner.py`
- Operational reruns for `005930` and `000660` with live page fetch and Codex theme route enabled.
