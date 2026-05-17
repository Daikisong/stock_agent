# Checkpoint 28A Round 85: R6 Loop 4 Financial / Capital / Digital

## Scope

Round 85 extends the R6 financial-capital-digital calibration pack. This is still case-library and score-weight design material only. It is not production scoring input.

Simple example: `자사주 매입 발표` is only a Stage 1 style signal. `실제 소각 완료 + ROE 개선 + 사업 EPS/FCF 경로`가 같이 있어야 Stage 3 검토 근거가 된다.

## What Changed

- Added new canonical archetypes:
  - `TREASURY_SHARE_CANCEL_EXECUTION`
  - `FINTECH_SUPERAPP_IPO_OPTION`
  - `BANK_DIGITAL_ASSET_EQUITY_STAKE`
- Added Round 85 R6 Loop 4 pack:
  - `src/e2r/sector/round85_r6_loop4_financial_capital_digital.py`
  - `src/e2r/cli/build_round85_r6_loop4_report.py`
  - `tests/test_round85_r6_loop4_financial_capital_digital.py`
- Generated calibration outputs:
  - `data/e2r_case_library/cases_r6_loop4_round85.jsonl`
  - `data/sector_taxonomy/score_weight_profiles_round85_r6_loop4_v4.csv`
  - `output/e2r_round85_r6_loop4_financial_capital_digital/`

## Round 85 Summary

- target_count: 19
- case_candidate_count: 18
- success_candidate_count: 8
- failed_rerating_count: 1
- event_premium_count: 1
- stage4b_case_count: 1
- stage4c_case_count: 7
- green_possible_count: 2
- watch_yellow_first_count: 11
- redteam_first_count: 6
- gate_only_target_count: 4

## Key Guardrails

- Do not apply Round 85 v4.0 weights to production scoring yet.
- Do not use case records as candidate-generation input.
- Do not treat low PBR, value-up policy, buyback news, fintech user count, IPO optionality, bank exchange stake, exchange market share, or stablecoin law news as Green evidence alone.
- Do not invent ROE, CET1, K-ICS, CSM, cancellation completion, take rate, FCF, stablecoin reserve/volume, equity-method income, collaboration revenue, security status, or stage prices.

## Interpretation

Round 85 separates three previously blended ideas:

- `TREASURY_SHARE_CANCEL_EXECUTION`: buyback/cancellation execution is stronger than policy news, but still needs business EPS/FCF and ROE/PBR confirmation.
- `FINTECH_SUPERAPP_IPO_OPTION`: users and IPO valuation are routing evidence, not durable economics. Take rate, FCF, credit loss, regulation, and security are required.
- `BANK_DIGITAL_ASSET_EQUITY_STAKE`: a bank buying an exchange stake is strategic Stage 1/2 evidence. Green remains blocked until equity-method income, collaboration revenue, regulatory approval, and security stability are visible.

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round85_r6_loop4_financial_capital_digital -v
PYTHONPATH=src python -m e2r.cli.build_round85_r6_loop4_report
```

Targeted Round 85 tests passed.
