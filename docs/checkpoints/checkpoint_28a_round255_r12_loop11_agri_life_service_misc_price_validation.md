# Checkpoint 28A Round 255 R12 Loop 11 Agri Life Service Misc Price Validation

Round 255 reflects `docs/round/round_255.md` as a calibration-only R12 case pack. It does not change production scoring, candidate generation, Stage thresholds, or Red Team rules.

## Scope

- Source round: `docs/round/round_255.md`
- Analyst round id: `round_183`
- Large sector label: `AGRI_LIFE_SERVICE_MISC`
- Mapped large sector: `EDUCATION_LIFE_AGRI_MISC`
- Cases added: 8
- Full adjusted OHLC complete: no
- Shadow weights only: yes

Easy example: a medical-school quota expansion can explain why education names deserve monitoring, but it is not Stage 3-Green until paid enrollment, ARPU, OPM, and cash conversion are visible.

## Cases

| Case | Archetype | Result |
|---|---|---|
| Coway recurring rental | `HOME_LIVING_RENTAL_RECURRING` | recurring-service success candidate, but accounts/churn/ARPU/FCF are still insufficient |
| Medical quota education basket | `EDUCATION_POLICY_MEDICAL_QUOTA` | policy event / Stage 1-2 watch, not Green |
| AI textbook rollback / classroom device regulation | `EDTECH_AI_TEXTBOOK_POLICY_REVERSAL` | 4C-watch policy friction |
| Fertility / childcare policy basket | `CHILDCARE_DEMOGRAPHIC_POLICY_EVENT` | demographic policy watch; utilization and paid demand still required |
| Kimchi cabbage input shock | `AGRI_FOOD_INPUT_COST_SHOCK` | 4C-watch unless pass-through and margin stability are proven |
| Feed wheat / livestock input-cost basket | `FEED_GRAIN_INPUT_COST_4C` | 4C-watch for feed/livestock processors |
| Dog-meat ban / pet welfare transition | `PET_WELFARE_POLICY_TRANSITION` | policy transition watch; monetization still required |
| Kyochon / Cherrybro / Neuromeka Jensen event | `FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM` | price moved without evidence / 4B-watch |

## Guardrails

- Do not use these cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds.
- Do not treat policy headlines, birthrate rebound, pet-welfare policy, input-cost shocks, or celebrity food events as structural evidence by themselves.
- Do not call price-only movement evidence-backed rerating.
- Keep all changes in calibration/evaluation outputs until score changes are separately validated.

## Outputs

- `data/e2r_case_library/cases_r12_loop11_round255.jsonl`
- `data/sector_taxonomy/round255_r12_loop11_agri_life_service_misc_price_validation_audit.json`
- `output/e2r_round255_r12_loop11_agri_life_service_misc_price_validation/round255_r12_loop11_price_validation_summary.md`
- `output/e2r_round255_r12_loop11_agri_life_service_misc_price_validation/round255_r12_loop11_case_matrix.csv`
- `output/e2r_round255_r12_loop11_agri_life_service_misc_price_validation/round255_r12_loop11_shadow_weights.csv`
- `output/e2r_round255_r12_loop11_agri_life_service_misc_price_validation/round255_r12_loop11_stage4b_4c_review.md`

## Verification

- `PYTHONPATH=src python -m unittest tests.test_round255_r12_loop11_agri_life_service_misc_price_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round255_r12_loop11_report`

