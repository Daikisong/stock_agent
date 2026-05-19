# Checkpoint 28A Round 198 R7 Loop 7 Biotech Healthcare Device Price Validation

## Scope

- source round: `docs/round/round_198.md`
- large sector: `BIOTECH_HEALTHCARE_DEVICE`
- production_scoring_changed: `false`
- candidate_generation_input: `false`
- shadow_weight_only: `true`
- needs_ohlc_backfill: `true`

이번 라운드는 R7 바이오·헬스케어·의료기기에서 `승인/임상/논문/M&A 뉴스`와 `처방량/보험·급여/상업화 매출/로열티/가동률/현금 runway`를 분리한다. 핵심은 승인받았다는 사실이 아니라, 그 승인이 실제 EPS/FCF 체급 변화로 내려오는지다.

쉬운 예: `as_of_date=2024-08-20`에 FDA 승인이 나왔더라도 처방량, J&J 매출, 유한양행 로열티, EPS revision이 확인되지 않았다면 Stage 3-Green이 아니라 강한 Stage 2 후보로 둔다.

## Files Added

- `src/e2r/sector/round198_r7_loop7_biotech_healthcare_device_price_validation.py`
- `src/e2r/cli/build_round198_r7_loop7_report.py`
- `tests/test_round198_r7_loop7_biotech_healthcare_device_price_validation.py`
- `data/e2r_case_library/cases_r7_loop7_round198.jsonl`
- `data/sector_taxonomy/round198_r7_loop7_biotech_healthcare_device_price_validation_audit.json`
- `output/e2r_round198_r7_loop7_biotech_healthcare_device_price_validation/`

## Case Pack

| case | classification | stage decision |
| --- | --- | --- |
| 유한양행 lazertinib | `success_candidate` | FDA approval은 Stage 2; 처방량, 로열티, EPS revision 전 Green 금지 |
| 휴젤 Letybo | `success_candidate` | 미국 launch는 Stage 2; 미국 매출, ASP, 채널 침투, 반복 주문 전 Green 금지 |
| 셀트리온 미국 facility | `success_candidate` | tariff hedge와 현지화는 Stage 2; 제품 이전, 가동률, margin, FCF 전 Green 금지 |
| SK바이오사이언스 IDT | `success_candidate` | CMO 전환 후보지만 M&A 발표 당일 가격 반응은 event premium watch |
| 삼성바이오로직스 GSK facility | `4b_watch` | structural CDMO benchmark지만 신규 Green보다 valuation/capacity saturation 감시 |
| 루닛 external validation | `failed_rerating` | 외부 검증은 Stage 2 후보; 수가, 병원 도입, 반복매출, cash runway 전 Green 금지 |
| R7 hard 4C source gap | `failed_rerating` | 신뢰 가능한 원문 없이 CRL, 임상실패, dilution, 상업화 실패를 hard 4C로 확정하지 않음 |

## Green Gate

R7 Green 후보에는 다음 증거가 필요하다.

- `approval_or_regulatory_clearance`
- `commercial_launch`
- `prescription_volume_or_hospital_adoption`
- `reimbursement_or_payer_access`
- `revenue_recognition`
- `royalty_or_gross_margin_confirmed`
- `cash_runway_and_dilution_risk_passed`
- `partner_execution_risk_passed`
- `price_path_after_commercial_evidence`

반대로 다음은 Green 금지 패턴으로 기록했다.

- `approval_news_only`
- `clinical_headline_only`
- `paper_validation_without_revenue`
- `partner_peak_sales_without_royalty_visibility`
- `mna_announcement_only`
- `fda_clearance_without_sales`
- `cash_runway_short`
- `large_dilution_or_cb_risk`

## 4B / 4C Notes

- 승인, 논문, M&A, partner peak-sales 기대가 상업화보다 먼저 가격에 반영되면 4B-watch로 본다.
- 효능/안전성 CRL은 hard 4C가 될 수 있다.
- 제조시설 inspection CRL은 추가 임상 요구가 없고 기존 승인/효능 근거가 유지되면 상업화 지연 watch로 분리한다.
- 이번 pass에서는 신뢰 가능한 primary/major source가 부족한 hard 4C를 억지로 만들지 않았다.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round198_r7_loop7_biotech_healthcare_device_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round198_r7_loop7_report
```

## What Not To Change

- Round198 케이스를 후보 생성 입력으로 쓰지 않는다.
- Stage 3-Green 기준을 낮추지 않는다.
- 처방량, 보험·급여, 매출, 로열티, 가동률, gross margin, cash runway, dilution, stage price, MFE/MAE를 발명하지 않는다.
- 승인 뉴스, 임상 헤드라인, 논문 성능, M&A 발표만으로 Green을 만들지 않는다.
- manufacturing-inspection CRL과 efficacy/safety CRL을 같은 hard 4C로 취급하지 않는다.

## Next

OHLC backfill로 Stage 2 기준 가격, peak, MFE/MAE, 상대수익률을 채워야 한다. 그 다음 R7 shadow scoring에서 `commercial_revenue`, `prescription_volume`, `royalty_recognition`, `reimbursement_access`, `contract_backlog`, `capacity_utilization`, `cash_runway`, `dilution_risk`가 실제 가격경로와 맞는지 검증한다.
