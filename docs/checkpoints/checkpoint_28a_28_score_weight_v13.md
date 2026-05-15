# Checkpoint 28A-28: Round 28 Score-Weight v1.3 Calibration

## Purpose

Round 28 was applied as calibration material only.

The change adds v1.3 score-weight hypotheses and case candidates for:

- NUCLEAR_SMR_GRID_POLICY
- RARE_METALS_STRATEGIC_MATERIALS
- DATA_CENTER_REIT_INFRASTRUCTURE
- UTILITIES_AI_POWER_PPA
- SMART_GRID_FLEXIBLE_DATACENTER
- NORTH_KOREA_POLICY_EVENT
- METAVERSE_NFT_THEME
- ADVANCED_MATERIAL_SPECULATIVE_THEME
- VALUE_UP_SHAREHOLDER_RETURN
- AI_DATA_CENTER_INFRASTRUCTURE

Production scoring, StageClassifier thresholds, RedTeam rules, and candidate generation were not changed.

## Outputs

- `src/e2r/sector/round28_score_weight_v13.py`
- `src/e2r/cli/build_round28_score_weight_report.py`
- `tests/test_round28_score_weight_v13.py`
- `data/e2r_case_library/cases_v10_round28.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round28_v13.csv`
- `output/e2r_round28_score_weight_v13/round28_score_weight_v13_summary.md`
- `output/e2r_round28_score_weight_v13/round28_case_candidate_matrix.csv`
- `output/e2r_round28_score_weight_v13/round28_green_guardrail_review.md`
- `output/e2r_round28_score_weight_v13/round28_event_theme_boundary_review.md`
- `output/e2r_round28_score_weight_v13/round28_risk_boundary_review.md`
- `output/e2r_round28_score_weight_v13/round28_price_validation_plan.md`

## Summary

- target_count: 10
- case_candidate_count: 40
- success_candidate_count: 10
- counterexample_or_risk_count: 30
- stage4b_case_count: 0
- stage4c_case_count: 8
- green_possible_count: 4
- watch_yellow_first_count: 3
- redteam_first_count: 3
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Key Interpretation

Round 28 expands the map into power, policy, event, and speculative-theme boundaries.

Example: nuclear/SMR can be important because AI data centers need clean power. But `SMR` as a keyword is not score evidence. A stronger case needs PPA, licensing, financing, project economics, and revenue path.

Example: data-center REITs can be Green-possible, but the evidence must be REIT-specific: FFO/AFFO growth, occupancy, tenant quality, power/cooling/land, and funding cost.

Example: North Korea policy events, NFT/metaverse, and speculative advanced materials are RedTeam-first. A price rally from policy, NFT volume, a paper, a sample, or a patent is not structural E2R without contracts, revenue, and FCF.

Example: value-up is not index inclusion. It needs ROE, actual cancellation, repeated shareholder return, dividend sustainability, and a credible NAV/PBR discount-closure path.

## Green-Possible With Strict Gates

- RARE_METALS_STRATEGIC_MATERIALS
- DATA_CENTER_REIT_INFRASTRUCTURE
- VALUE_UP_SHAREHOLDER_RETURN
- AI_DATA_CENTER_INFRASTRUCTURE

## Watch-First / 4C-Sensitive

- NUCLEAR_SMR_GRID_POLICY
- UTILITIES_AI_POWER_PPA
- SMART_GRID_FLEXIBLE_DATACENTER

## RedTeam-First

- NORTH_KOREA_POLICY_EVENT
- METAVERSE_NFT_THEME
- ADVANCED_MATERIAL_SPECULATIVE_THEME

## Guardrails

- Do not use Round 28 case IDs as candidate-generation input.
- Do not apply v1.3 weights to production scoring yet.
- Do not score policy headlines, LOIs, PoCs, samples, patents, or price rallies without source-backed economics.
- Do not invent stage dates, prices, PPA economics, FFO/AFFO, offtake terms, revenue, FCF, or cancellation status.
- Keep Stage 3-Green strict and cross-evidence based.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round28_score_weight_v13 -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/round28_score_weight_v13.py src/e2r/cli/build_round28_score_weight_report.py tests/test_round28_score_weight_v13.py
PYTHONPATH=src python -m e2r.cli.build_round28_score_weight_report \
  --output-directory output/e2r_round28_score_weight_v13 \
  --cases data/e2r_case_library/cases_v10_round28.jsonl \
  --score-profiles data/sector_taxonomy/score_weight_profiles_round28_v13.csv
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Verification Result

- Round 28 unit tests passed.
- Compileall passed.
- Full repository test run still has an unrelated pre-existing blocker: `docs/round/round_17.md` is deleted in the working tree, so Round 17 tests cannot read their source document.

## Next Step

1. Backfill tradable case price paths.
2. Validate nuclear/SMR PPA economics, data-center REIT FFO/AFFO, strategic-metals offtake, and value-up execution.
3. Keep North Korea policy, NFT/metaverse, and speculative advanced materials RedTeam-first unless contracts, revenue, and FCF are source-backed.
4. Do not apply v1.3 weights to production scoring before shadow score-price validation.
