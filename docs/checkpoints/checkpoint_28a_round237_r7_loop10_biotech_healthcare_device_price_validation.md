# Checkpoint 28A Round 237 R7 Loop 10 Biotech Healthcare Device Price Validation

## 반영 범위

`docs/round/round_237.md`의 R7 바이오·헬스케어·의료기기 가격경로 검증 라운드를 case-library 보강팩으로 반영했다.

- source round: `docs/round/round_237.md`
- analyst round id: `round_165`
- large sector: `BIOTECH_HEALTHCARE_DEVICE`
- production scoring changed: `false`
- candidate generation input: `false`
- shadow weight only: `true`
- price validation: `partial_with_reported_price_anchors`
- full OHLC complete: `false`
- hard 4C confirmed: `false`

## 핵심 해석

R7의 Stage 3는 `FDA 승인`, `임상 성공`, `논문 성능`, `M&A 발표`, `미국 공장 인수`가 아니다. 실제 Stage 3 후보가 되려면 처방량, 시술량, 병원 도입, 보험·수가, 상업 매출, 로열티, 가동률, 마진, FCF가 확인되어야 한다.

쉬운 예시:

- `AUC 0.91 의료AI 논문`은 Stage 2 evidence다. 병원 도입과 수가, 반복 매출 전에는 Green이 아니다.
- `미국 launch`는 좋은 Stage 2다. 미국 매출, 채널 침투, ASP, 반복 시술, OPM 전에는 Green이 아니다.
- `M&A 발표 + 당일 주가 급등`은 4B/event premium이다. 가동률, backlog, margin, FCF 전에는 Green이 아니다.
- `파트너 임상 실패`는 한국 상장사 OHLC가 없어도 RedTeam/4C-watch로 들어간다.

## 추가 케이스

| case | company | classification | interpretation |
| --- | --- | --- | --- |
| `r7_loop10_jeisys_aesthetic_device_take_private` | Jeisys Medical | `success_candidate` | PE take-private은 미용 의료기기 수요 검증이지만 listed peer Green 조건은 아님 |
| `r7_loop10_hugel_letybo_us_launch` | 휴젤 | `success_candidate` | Letybo 미국 launch는 Stage 2, 미국 매출·채널·반복시술·OPM 확인 필요 |
| `r7_loop10_sk_bioscience_idt_cmo_mna` | SK바이오사이언스 | `event_premium` | IDT Biologika 인수와 +11.7% event return은 Stage 2/4B-watch |
| `r7_loop10_celltrion_us_manufacturing_tariff_hedge` | 셀트리온 | `success_candidate` | ImClone 인수와 미국 증설은 tariff hedge Stage 2, 제품 이전·가동률·FCF 필요 |
| `r7_loop10_samsung_biologics_gsk_facility_price_failed` | 삼성바이오로직스 | `success_candidate` | GSK facility는 좋은 CDMO 증거지만 발표일 상대수익률이 약해 evidence_good_but_price_failed |
| `r7_loop10_hanall_immunovant_batoclimab_ted_failure` | 한올바이오파마/Immunovant | `failed_rerating` | partner TED 임상 실패는 강한 4C-watch, 단 hard 4C는 회사 전체 훼손 확인 전 보류 |
| `r7_loop10_lunit_medical_ai_external_validation` | 루닛 | `failed_rerating` | 외부검증 AUC는 Stage 2, subgroup weakness와 수가·도입·매출 부재가 Green을 차단 |

## Green Gate

R7 Stage 3-Green 후보에는 다음 증거가 필요하다.

- `approval_clearance_or_launch_confirmed`
- `commercial_launch_after_approval`
- `commercial_revenue_or_royalty_recognition`
- `prescription_procedure_volume_or_hospital_adoption`
- `reimbursement_payer_access_or_asp_confirmed`
- `capacity_utilization_or_channel_penetration`
- `gross_margin_or_fcf_visibility`
- `repeat_treatment_consumables_or_contract_backlog`
- `cash_runway_and_dilution_risk_passed`
- `partner_execution_risk_passed`
- `price_path_after_evidence`

다음 패턴은 Green을 막는다.

- `approval_news_only`
- `clinical_headline_only`
- `external_validation_without_revenue`
- `mna_without_utilization`
- `take_private_premium_only`
- `fda_approval_without_commercial_sales`
- `partner_pipeline_without_indication_success`
- `pre_revenue_medical_ai_story`
- `cash_burn_or_dilution_risk`
- `subgroup_performance_risk`
- `facility_acquisition_without_product_transfer`
- `us_launch_without_channel_sales`

## 산출물

- `src/e2r/sector/round237_r7_loop10_biotech_healthcare_device_price_validation.py`
- `src/e2r/cli/build_round237_r7_loop10_report.py`
- `tests/test_round237_r7_loop10_biotech_healthcare_device_price_validation.py`
- `data/e2r_case_library/cases_r7_loop10_round237.jsonl`
- `data/sector_taxonomy/round237_r7_loop10_biotech_healthcare_device_price_validation_audit.json`
- `output/e2r_round237_r7_loop10_biotech_healthcare_device_price_validation/`

## 검증 명령

```bash
PYTHONPATH=src python -m e2r.cli.build_round237_r7_loop10_report
PYTHONPATH=src python -m unittest tests.test_round237_r7_loop10_biotech_healthcare_device_price_validation -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
git diff --check
```

## 남은 작업

원시 수정주가 OHLC가 없는 항목은 `price_data_unavailable_after_deep_search` 또는 `reported_*_anchor_not_full_ohlc`로 남겼다. 다음 가격 backfill 라운드에서 Stage 2/4B/4C 기준 가격, MFE/MAE, peak/drawdown을 채워야 한다.

이번 패치는 production scoring을 바꾸지 않는다. 예를 들어 `FDA 승인 + launch 뉴스`는 학습용 Stage 2 근거일 뿐, 실제 매출·수가·채널·마진 확인 전에는 라이브 Stage 3-Green 승격 입력으로 쓰이지 않는다.
