# Checkpoint 28A Round 227 R10 Loop 9 Construction Real Estate Materials Price Validation

## Scope

Round 227 was converted into a calibration-only case pack for `CONSTRUCTION_REAL_ESTATE_MATERIALS`.

Production scoring was not changed. The cases are evaluation material only and must not be used as candidate-generation input.

## Files Added

- `src/e2r/sector/round227_r10_loop9_construction_real_estate_materials_price_validation.py`
- `src/e2r/cli/build_round227_r10_loop9_report.py`
- `tests/test_round227_r10_loop9_construction_real_estate_materials_price_validation.py`
- `data/e2r_case_library/cases_r10_loop9_round227.jsonl`
- `data/sector_taxonomy/round227_r10_loop9_construction_real_estate_materials_price_validation_audit.json`
- `output/e2r_round227_r10_loop9_construction_real_estate_materials_price_validation/`

## Case Pack Summary

- cases: 8
- success_candidate: 3
- event_premium: 1
- Stage 3 dated cases: 0
- hard 4C confirmed cases: 3
- full OHLC complete: false
- shadow weight only: true

## Key Interpretation

- Samsung E&A / GS E&C Fadhili and Hyundai E&C Jafurah are Stage 2 EPC/gas-infra watch cases. Stage 3 waits for margin, progress revenue, cash collection, and working-capital control.
- Taeyoung / PF stress is a hard 4C reference point. PF support is relief, not Green evidence.
- Seoul housing supply and reconstruction policy are Stage 1/2 event premium until presales, cost ratio, PF stability, and FCF confirm.
- Hyundai Engineering bridge collapse and POSCO E&C / DL Construction safety cases reinforce safety and operational trust as hard R10 gates.
- SK/AWS and OpenAI/Samsung/SK data-center headlines are Stage 2/event premium until tenant, NOI/AFFO, power/water, and capex per share confirm.
- Hyundai Steel rebar weakness is a building-material demand 4C-watch reference.

Easy example: `대형 EPC 수주 + 당일 주가 +8.5%` is Stage 2/4B-watch. `대형 EPC 수주 + 마진 + 공정률 매출 + 현금회수 + working capital 안정` is the bundle that can support deeper Stage review.

## Green Guardrails

Round 227 requires:

- company-level order or lease confirmed
- margin or NOI/AFFO confirmed
- cash flow after working capital confirmed
- PF and funding-cost risk passed
- project progress or cost ratio stable
- tenant / occupancy / utilization confirmed
- capex per share or dilution passed
- safety and quality trust passed
- price path after evidence

Round 227 blocks Green from:

- contract headline only
- PF relief policy only
- housing supply policy only
- real-estate rebound theme only
- data-center theme without tenant
- asset headline without NOI/AFFO
- EPC backlog without margin
- low-margin order risk
- capex per share dilution
- quality/safety incident
- repeated workplace fatality
- building-material demand weakness

## Verification

Commands run:

```bash
PYTHONPATH=src python -m unittest tests.test_round227_r10_loop9_construction_real_estate_materials_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round227_r10_loop9_report
```

Result:

- Round 227 targeted tests passed.
- Round 227 case library, audit JSON, CSV matrices, shadow weights, green-gate review, price-validation plan, and 4B/4C review were generated.
