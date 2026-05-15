# Checkpoint 28A Round 46 - R6 Financial / Capital Allocation / Digital Finance

## Scope

Round 46 adds the R6 financial, capital-allocation, and digital-finance
calibration pack. This is calibration/evaluation material only. It does not
change production feature engineering, scoring, staging, RedTeam, or candidate
generation.

## Files Added

- `src/e2r/sector/round46_r6_financial_capital_digital.py`
- `src/e2r/cli/build_round46_r6_report.py`
- `tests/test_round46_r6_financial_capital_digital.py`
- `data/e2r_case_library/cases_r6_round46.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round46_r6_v1.csv`
- `output/e2r_round46_r6_financial_capital_digital/`

## Archetype Updates

Round 46 adds R6-specific canonical archetype labels:

- `INSURANCE_UNDERWRITING_CYCLE`
- `SECURITIES_BROKERAGE_CYCLE`
- `PAYMENT_FINTECH_INFRA`
- `DIGITAL_ASSET_TOKENIZATION`
- `CREDIT_DATA_INFRA`
- `VC_EXIT_MARKET_CYCLE`
- `DIGITAL_ASSET_THEME_OVERHEAT`

Example: a bank can be Green-eligible when ROE, CET1, credit cost, PF exposure,
and shareholder return execution all line up. A stablecoin headline is only
Stage 1/Watch until regulation, reserves, convertibility, transaction volume,
and fee model are proven.

## Output Summary

- target_count: 10
- case_candidate_count: 12
- success_candidate_count: 6
- event_premium_count: 2
- stage4c_case_count: 4
- green_possible_count: 2
- watch_yellow_first_count: 6
- redteam_first_count: 2
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Case Coverage

Positive / watch-to-Green candidates:

- `korea_commercial_act_treasury_share_cancel_case`
- `korea_dividend_tax_reform_case`
- `sk_square_buyback_cancel_case`
- `korean_financial_holdings_valueup_case`
- `mynt_gcash_payment_platform_case`
- `toss_won_stablecoin_case`

Event / mixed cases:

- `samsung_electronics_buyback_mixed_case`
- `korea_zinc_buyback_event_case`

4C / RedTeam guardrail cases:

- `samsung_ct_activist_rejection_case`
- `korea_tax_policy_shock_case`
- `terrausd_do_kwon_collapse_case`
- `boe_stablecoin_convertibility_warning_case`

## R6 Green Rule

R6 Green is not “low PBR” or “value-up label” by itself. It requires the
discount-removal loop to close:

`ROE/capital quality -> executed buyback cancellation or dividend -> governance protection -> valuation band change -> price-path validation`

For digital finance, the equivalent loop is:

`regulated product -> transaction volume -> take rate or fee model -> reserve/convertibility safety -> recurring revenue`

Easy example: SK Square can be a higher-quality holding-company case because
NAV discount, cancellation, additional buyback, and independent-director
evidence appear together. Samsung Electronics buyback is useful evidence, but
buyback alone cannot solve business/EPS weakness.

## What Not To Change

- Do not apply R6 v1.0 weights to production scoring yet.
- Do not use these case records as candidate-generation input.
- Do not treat low PBR, value-up index inclusion, user count, buyback headline, or stablecoin/STO headline as structural evidence by itself.
- Do not invent ROE, CET1, K-ICS, credit cost, PF exposure, buyback cancellation, payment volume, take rate, reserve ratio, transaction volume, or price-path fields.
- Do not lower Stage 3-Green thresholds for financial or fintech stories.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests/test_round46_r6_financial_capital_digital.py -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/round46_r6_financial_capital_digital.py src/e2r/cli/build_round46_r6_report.py tests/test_round46_r6_financial_capital_digital.py
PYTHONPATH=src python -m e2r.cli.build_round46_r6_report
```

Result:

- Round 46 targeted tests passed.
- Report generation succeeded.
- Production scoring modules do not import the Round 46 pack.
