# Checkpoint 28A Round 103: R11 Loop-5 Policy / Geopolitical / Disaster / Event

## Scope

Round 103 expands the R11 policy, geopolitical, disaster, and event pack. This is still calibration material, not production scoring.

Simple example: an outbreak headline can route a company into Stage 1 research. It does not become Stage 3 evidence unless a source shows a government order, stockpile contract, guidance lift, repeat procurement, or FCF conversion.

## Files Added

- `src/e2r/sector/round103_r11_loop5_policy_geopolitical_event.py`
- `src/e2r/cli/build_round103_r11_loop5_report.py`
- `tests/test_round103_r11_loop5_policy_geopolitical_event.py`
- `data/e2r_case_library/cases_r11_loop5_round103.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round103_r11_loop5_v5.csv`
- `output/e2r_round103_r11_loop5_policy_geopolitical_event/`

## Archetype Updates

Added or confirmed:

- `CRITICAL_INFRA_RECONSTRUCTION_FINANCING`
- `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE`
- `PUBLIC_HEALTH_PROCUREMENT_REVERSAL`
- `INDUSTRIAL_POLICY_TARIFF_EVENT`
- `DISCLOSURE_CONFIDENCE_CAP`

Round 103 now covers 20 R11 targets:

- target_count: 20
- watch_yellow_first_count: 9
- redteam_first_count: 11
- gate_only_target_count: 3
- green_possible_count: 0

## Case Pack

The generated case pack has 17 cases:

- success_candidate_count: 6
- event_premium_count: 5
- stage4b_case_count: 2
- stage4c_case_count: 5

Key additions:

- `bavarian_nordic_us_stockpile_contract_case` moved to `GOVERNMENT_STOCKPILE_REVENUE_GUIDANCE`.
- `moderna_cepi_bird_flu_funding_case` captures public-health funding as Stage 2 routing, not durable revenue.
- `moderna_barda_contract_cancel_case` captures funding withdrawal as 4C-style procurement reversal.
- `ukraine_ebrd_power_port_concession_case` separates critical infrastructure financing from generic reconstruction headlines.
- `china_group_visa_tourism_policy_case` keeps tourism visa policy as Stage 1/Event until visitor spend and company margin data exist.

## Guardrails

- Do not apply R11 Loop-5 v5 weights to production scoring yet.
- Do not use case records as candidate-generation input.
- Do not treat policy headlines, disaster events, disease outbreaks, preprints, or local policy as Green evidence alone.
- Do not invent contracts, budgets, government orders, financing, guidance, stage dates, or prices.
- Keep `PUBLIC_HEALTH_PROCUREMENT_REVERSAL`, `POLICY_MARKET_SHOCK_EVENT`, and `THEME_VALUATION_OVERHEAT` as gates.

## Generated Reports

- `round103_r11_loop5_policy_geopolitical_event_summary.md`
- `round103_r11_loop5_case_matrix.csv`
- `round103_r11_loop5_stage_date_plan.csv`
- `round103_r11_loop5_green_guardrails.md`
- `round103_r11_loop5_event_false_positive_caps.md`
- `round103_r11_loop5_price_validation_plan.md`
- `round103_r11_loop5_price_fields.csv`

## Verification

Executed:

```bash
PYTHONPATH=src python -m unittest tests.test_round103_r11_loop5_policy_geopolitical_event -v
PYTHONPATH=src python -m e2r.cli.build_round103_r11_loop5_report
```

Result:

- Round 103 targeted unit tests passed.
- Reports were generated.
- Production scoring, staging, RedTeam, and E2R_STANDARD flow do not import the Round 103 pack.

## Next Step

Backfill price paths only after official price data is available. Until then, all stage prices and MFE/MAE fields remain intentionally null.
