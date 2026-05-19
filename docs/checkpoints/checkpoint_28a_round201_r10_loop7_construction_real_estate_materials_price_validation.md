# Checkpoint 28A Round 201 R10 Loop 7 Construction Real Estate Materials Price Validation

## Scope

Round 201 반영 범위는 건설, 부동산, 건자재의 가격경로 검증 팩이다.
이번 패치는 production scoring을 바꾸지 않고, case library와 shadow weight 검증 재료만 추가했다.

쉬운 예: `as_of_date=2024-04-03`에 삼성E&A가 대형 EPC 수주를 받아도, 원가율과 현금 회수가 아직 없으면 Stage 3-Green이 아니라 Stage 2 watch다.

## Added Files

- `src/e2r/sector/round201_r10_loop7_construction_real_estate_materials_price_validation.py`
- `src/e2r/cli/build_round201_r10_loop7_report.py`
- `tests/test_round201_r10_loop7_construction_real_estate_materials_price_validation.py`
- `data/e2r_case_library/cases_r10_loop7_round201.jsonl`
- `data/sector_taxonomy/round201_r10_loop7_construction_real_estate_materials_price_validation_audit.json`
- `output/e2r_round201_r10_loop7_construction_real_estate_materials_price_validation/`

## Case Pack

| case_id | company | archetype focus | role |
| --- | --- | --- | --- |
| `samsung_ea_fadhili_epc_backlog_stage2_watch` | 삼성E&A | overseas EPC backlog + low-margin overlay | Stage 2 watch |
| `hyundai_ec_jafurah_gas_infra_stage2_watch` | 현대건설 | overseas gas infrastructure EPC | Stage 2 watch |
| `daewoo_ec_grand_faw_handover_stage2_watch` | 대우건설 | EPC handover / reconstruction policy | Stage 2 watch |
| `taeyoung_pf_workout_credit_hard_4c` | 태영건설 | PF restructuring / credit RedTeam | hard 4C |
| `hdc_hyundai_development_apartment_collapse_hard_4c` | HDC현대산업개발 | apartment quality/safety | hard 4C |
| `posco_ec_dl_construction_workplace_safety_4c_watch` | POSCO E&C / DL건설 | workplace safety / operational trust | 4C-watch |
| `sk_aws_ulsan_ai_data_center_real_asset_insufficient_evidence` | SK/AWS 울산 AI 데이터센터 | real-asset data center / no tenant | Stage 2 watch |

## Green Gate

Round 201의 핵심은 건설 headline과 현금흐름을 분리하는 것이다.

Green에 필요한 필드는 다음과 같다.

- `company_level_order_or_tenant_confirmed`
- `cash_flow_after_working_capital_confirmed`
- `epc_margin_or_noi_affo_confirmed`
- `pf_and_funding_cost_risk_passed`
- `cost_ratio_or_project_progress_stable`
- `tenant_occupancy_or_utilization_confirmed`
- `capex_per_share_or_dilution_passed`
- `safety_quality_trust_passed`
- `price_path_after_cash_flow_evidence`

Green을 막는 패턴은 다음과 같다.

- 수주 headline만 있는 경우
- PF 지원책만 있는 경우
- 부동산 반등 테마만 있는 경우
- 임차인 없는 데이터센터 테마
- NOI/AFFO 없는 자산 headline
- REIT 배당 headline만 있는 경우
- EPC 수주잔고는 있지만 마진이 없는 경우
- 저마진 수주, CAPEX 희석, 품질·안전 사고, 반복 사망사고, working capital 악화

## Stage 4B / 4C Notes

- 태영건설 PF workout은 `pf_workout_or_debt_reschedule` hard 4C다.
- HDC현대산업개발 광주 화정 아이파크 붕괴는 `apartment_collapse_or_quality_accident` hard 4C다.
- POSCO E&C/DL건설 안전 이슈는 4C-watch다. 반복 사망사고와 현장중단은 비용, 면허, 평판, 수주 경쟁력에 영향을 준다.
- 삼성E&A·현대건설·대우건설의 대형 EPC/인프라 이벤트는 Stage 2지만, 마진·공정률·현금 회수 전 Green이 아니다.
- AI 데이터센터 real asset은 임차계약, NOI/AFFO, power/water, capex per share가 확인되어야 한다.

## Outputs

Generated report files:

- `round201_r10_loop7_price_validation_summary.md`
- `round201_r10_loop7_case_matrix.csv`
- `round201_r10_loop7_target_aliases.csv`
- `round201_r10_loop7_score_adjustments.csv`
- `round201_r10_loop7_price_backfill_fields.csv`
- `round201_r10_loop7_green_gate_review.md`
- `round201_r10_loop7_price_backfill_plan.md`
- `round201_r10_loop7_stage4b_4c_review.md`

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round201_r10_loop7_construction_real_estate_materials_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round201_r10_loop7_report
```

Full test suite was also run after the patch.

## What Not To Change

- Do not apply Round 201 score weights to production scoring yet.
- Do not use Round 201 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent cash flow, EPC margin, NOI/AFFO, tenant contracts, power/water, funding cost, capex per share, stage prices, or MFE/MAE.
- Do not treat contract headline, PF support, real-estate rebound, AI data-center headline, REIT yield, or disaster rebuild as Green evidence alone.

## Next

Next step is OHLC/price-path backfill. In practice, 삼성E&A와 현대건설은 수주 발표일 이후의 MFE/MAE를 보되, Stage 3 기준일은 수주일이 아니라 마진·공정률·현금 회수가 확인되는 날로 따로 잡아야 한다.
