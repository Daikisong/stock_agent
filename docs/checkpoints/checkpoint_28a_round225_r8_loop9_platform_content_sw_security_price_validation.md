# Checkpoint 28A Round 225 R8 Loop 9 Platform Content SW Security Price Validation

## Scope

Round 225 was converted into a calibration-only case pack for `PLATFORM_CONTENT_SW_SECURITY`.

Production scoring was not changed. The cases are evaluation material only and must not be used as candidate-generation input.

## Files Added

- `src/e2r/sector/round225_r8_loop9_platform_content_sw_security_price_validation.py`
- `src/e2r/cli/build_round225_r8_loop9_report.py`
- `tests/test_round225_r8_loop9_platform_content_sw_security_price_validation.py`
- `data/e2r_case_library/cases_r8_loop9_round225.jsonl`
- `data/sector_taxonomy/round225_r8_loop9_platform_content_sw_security_price_validation_audit.json`
- `output/e2r_round225_r8_loop9_platform_content_sw_security_price_validation/`

## Case Pack Summary

- cases: 8
- success_candidate: 3
- event_premium: 1
- failed_rerating: 2
- overheat: 1
- Stage 3 dated cases: 0
- hard 4C confirmed cases: 0
- full OHLC complete: false
- shadow weight only: true

## Key Interpretation

- 더존비즈온 and 시프트업 are Stage 2 watch examples, not automatic Stage 3-Green.
- 삼성SDS, NAVER/Webtoon, 카카오, and LG CNS separate event premium or price failure from true recurring E2R evidence.
- SK텔레콤 and HYBE are operational-trust/governance risk cases that feed RedTeam and 4C-watch checks.

Easy example: `AI 파트너십 + 당일 급등` is a radar/watch signal. `AI 파트너십 + 유료 전환 + 반복 매출 + OPM/FCF 개선 + 보안/거버넌스 통과` is the evidence bundle that can support Stage 3 review.

## Green Guardrails

Round 225 requires:

- recurring revenue or bookings
- paid usage / ARPU / ARR proxy
- OPM or gross margin improvement
- FCF conversion
- customer retention or churn evidence
- IP monetization beyond launch
- AI feature to paid revenue or cost savings
- privacy/security/governance risk passed
- price path after evidence

Round 225 blocks Green from:

- AI partnership headline only
- AI infrastructure investment plan only
- MAU without ARPU
- IPO/debut premium only
- M&A without integration
- game first-week sales only
- single-IP dependence without retention
- founder legal risk
- security/privacy incident
- data breach revenue cut

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round225_r8_loop9_platform_content_sw_security_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round225_r8_loop9_report
```

Result:

- Round 225 targeted tests passed.
- Round 225 case library, audit JSON, CSV matrices, shadow weights, green-gate review, price-validation plan, and 4B/4C review were generated.
