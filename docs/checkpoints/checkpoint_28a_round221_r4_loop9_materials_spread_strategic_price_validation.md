# Checkpoint 28A Round 221 R4 Loop 9 Materials/Spread/Strategic Price Validation

## Scope

`docs/round/round_221.md`를 반영해 소재, 스프레드, 전략자원 가격경로 검증 팩을 추가했다. 이 라운드는 캘리브레이션/평가용이며 생산 scoring, StageClassifier, 후보 생성 로직은 바꾸지 않았다.

쉬운 예시:

- 철강 관세 뉴스는 한국 철강 수출업체에 좋은 신호가 아니라 수출마진 훼손 가능성이다. 그래서 `4C-watch`로 본다.
- 리튬 JV나 미국 polysilicon 증설은 Stage 2 후보가 될 수 있지만, offtake, 제품 스프레드, FCF, CAPEX 부담이 확인되기 전에는 Stage 3-Green 근거가 아니다.
- M&A 보도는 거래가 확정되기 전까지 event premium이다.

## Files Added

- `src/e2r/sector/round221_r4_loop9_materials_spread_strategic_price_validation.py`
- `src/e2r/cli/build_round221_r4_loop9_report.py`
- `tests/test_round221_r4_loop9_materials_spread_strategic_price_validation.py`
- `data/e2r_case_library/cases_r4_loop9_round221.jsonl`
- `data/sector_taxonomy/round221_r4_loop9_materials_spread_strategic_price_validation_audit.json`
- `output/e2r_round221_r4_loop9_materials_spread_strategic_price_validation/`

## Case Pack

Round 221 adds seven calibration cases:

| Case | Type | Main Decision |
|---|---|---|
| POSCO / Hyundai Steel tariff watch | failed_rerating | Tariff headline is export-margin 4C-watch, not Green evidence. |
| Korea Zinc / YoungPoong | success_candidate | Strategic minerals are Stage 2, but governance, dilution, offtake, and FCF block Green. |
| Lotte Chemical / HD Hyundai Chemical | failed_rerating | NCC shutdown and support package are Stage 2 relief until spread/OPM/FCF recover. |
| SK Innovation / S-Oil | cyclical_success | Refining rebound is cyclical Stage 2, not structural Green. |
| POSCO / MinRes lithium JV | success_candidate | Lithium resource security needs offtake economics and downstream margin before Green. |
| OCI Holdings | success_candidate | Non-China supply-chain option remains Stage 2 until contract terms, margin, and FCF confirm. |
| Poongsan / Hanwha rumor | event_premium | Unconfirmed M&A rumor faded in six days; no Stage 3 evidence. |

## Canonical Alias Handling

The round text uses several target labels that are mapped to existing canonical archetypes instead of expanding production enums blindly.

Examples:

- `STEEL_TARIFF_SPREAD_OVERLAY` -> `STEEL_TARIFF_EVENT_KOREA`
- `CRITICAL_MINERALS_US_SUPPLY_CHAIN` -> `RARE_METALS_STRATEGIC_MATERIALS`
- `M_AND_A_OPTIONALITY_EVENT` -> `EVENT_PREMIUM`

## Green Guardrails

Stage 3-Green remains strict. Required evidence includes:

- actual product spread
- FCF after working capital
- supply discipline or capacity shutdown
- inventory build absent
- price floor or offtake
- medium-term EPS revision
- capex/dilution risk passed
- policy/tariff/sanction stress passed
- price path after evidence

Forbidden Green shortcuts include:

- commodity price spike only
- tariff headline only
- tender offer premium
- governance battle only
- policy support without FCF
- unconfirmed media report
- M&A rumor without transaction
- restructuring plan without margin

## Price Validation Status

Full OHLC paths are not complete. The pack stores reported event anchors and explicitly marks:

- `price_validation_completed = partial_with_reported_price_anchors`
- `full_ohlc_complete = false`

This means the report can say “the event had a reported +27% or -13% anchor,” but it must not invent MFE/MAE over 90D/180D/1Y without adjusted historical prices.

## Verification

Commands:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m unittest tests.test_round221_r4_loop9_materials_spread_strategic_price_validation -v
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m e2r.cli.build_round221_r4_loop9_report
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m unittest discover -s tests -v
```

Result:

- Round 221 targeted tests: 11 tests passed.
- Full test suite: 2735 tests passed.
- Report CLI completed and wrote case JSONL, audit JSON, markdown, and CSV outputs.

## What Not To Change

- Do not apply these shadow weights to production scoring yet.
- Do not use Round 221 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds.
- Do not treat commodity, tariff, governance, policy, unconfirmed media, or M&A rumor events as Green evidence.
- Do not invent full OHLC, stage prices, spreads, offtakes, or FCF.
