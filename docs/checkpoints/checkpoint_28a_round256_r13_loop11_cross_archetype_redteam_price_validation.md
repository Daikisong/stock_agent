# Checkpoint 28A Round 256 R13 Loop 11 Cross-Archetype RedTeam Price Validation

Round 256 reflects `docs/round/round_256.md` as a calibration-only cross-archetype RedTeam and price-validation pack. It does not change production scoring, candidate generation, Stage thresholds, or Red Team execution logic.

## Scope

- Source round: `docs/round/round_256.md`
- Analyst round id: `round_184`
- Large sector: `CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION`
- Cases added: 8
- Stage 3 dated cases: 2
- 4B-watch cases: 4
- Hard 4C cases: 3
- Full adjusted OHLC complete: no
- Shadow weights only: yes

Easy example: SK Hynix can be a valid Stage 3 success benchmark at `222,000 KRW`, but after a reported record high of `1,447,000 KRW`, the correct next state is 4B-watch rather than another fresh Green promotion.

## Cases

| Case | Main Archetype | Result |
|---|---|---|
| SK Hynix HBM | `STRUCTURAL_SUCCESS_BUT_4B_WATCH` | Stage 3 success benchmark, now 4B-watch after large MFE |
| APR / Medicube | `STRUCTURAL_SUCCESS_BUT_4B_WATCH` | structural K-beauty sell-through, but single-brand concentration 4B-watch |
| Samsung E&A Fadhili | `STAGE2_STRONG_NOT_GREEN` | signed EPC contract is Stage 2 until margin and cash collection close |
| Samsung SDS / KRW stablecoin basket | `AI_CAPITAL_ALLOCATION_EVENT_PREMIUM` | AI/digital policy event premium; price moved before revenue evidence |
| LG CNS / Samsung Biologics | `EVIDENCE_GOOD_BUT_PRICE_FAILED` | good evidence, weak price response; do not lower Green gates |
| LGES / L&F | `CONTRACT_QUALITY_HARD_4C` | contract cancellation/value collapse hard 4C |
| SK Telecom / Kumho Tire | `OPERATIONAL_TRUST_HARD_4C` | data breach and factory fire hard 4C |
| Hormuz / Iran shock | `MACRO_GEOPOLITICAL_HARD_4C` | macro energy/FX hard overlay |

## Guardrails

- Do not use these cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to improve recall.
- Do not treat contract headlines, AI capital allocation, stablecoin policy, IPO stories, or facility M&A as Green by themselves.
- Do not ignore hard 4C gates: contract cancellation, data breach, factory fire, or macro energy/FX shock.
- Do not invent OHLC, MFE, MAE, or stage dates where only reported anchors exist.

## Outputs

- `data/e2r_case_library/cases_r13_loop11_round256.jsonl`
- `data/sector_taxonomy/round256_r13_loop11_cross_archetype_redteam_price_validation_audit.json`
- `output/e2r_round256_r13_loop11_cross_archetype_redteam_price_validation/round256_r13_loop11_price_validation_summary.md`
- `output/e2r_round256_r13_loop11_cross_archetype_redteam_price_validation/round256_r13_loop11_case_matrix.csv`
- `output/e2r_round256_r13_loop11_cross_archetype_redteam_price_validation/round256_r13_loop11_shadow_weights.csv`
- `output/e2r_round256_r13_loop11_cross_archetype_redteam_price_validation/round256_r13_loop11_stage4b_4c_review.md`

## Verification

- `PYTHONPATH=src python -m unittest tests.test_round256_r13_loop11_cross_archetype_redteam_price_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round256_r13_loop11_report`

