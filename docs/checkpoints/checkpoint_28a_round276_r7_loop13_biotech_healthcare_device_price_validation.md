# Checkpoint 28A Round 276 R7 Loop 13 Biotech Healthcare Device Price Validation

## 목적

`docs/round/round_276.md`의 바이오·헬스케어·의료기기 케이스를 calibration-only 자료로 구조화했다.

이번 라운드의 핵심은 `FDA 승인`, `SC 제형 플랫폼`, `CDMO 미국 공장`, `정책 지원`, `M&A`, `정부 백신 구매`를 Stage 3-Green으로 바로 보지 않는 것이다. 예를 들어 FDA 승인은 강한 Stage 2 신호지만, 실제 처방 증가와 royalty/milestone 현금흐름이 확인되기 전에는 Green 근거가 아니다.

## 반영 내용

- canonical archetype 8개 추가
- Round 276 전용 케이스 팩 추가
- JSONL case library 생성
- audit JSON 생성
- shadow weight, deep sub-archetype, green gate, 4B/4C review 출력
- production scoring, 후보 생성, StageClassifier threshold는 변경하지 않음

## 추가 archetype

- `KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL`
- `PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY`
- `CDMO_US_TARIFF_HEDGE_STAGE2`
- `BIOPHARMA_US_FACTORY_TARIFF_HEDGE`
- `VACCINE_CDMO_M_AND_A_STAGE2`
- `AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT`
- `BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM`
- `VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE`

## 케이스 요약

- 케이스 수: 8
- Stage 3 dated case: 0
- success_candidate: 6
- event_premium: 3
- failed_rerating: 1
- hard 4C direct case: 0
- hard 4C reference: 1

## 핵심 가드레일

- FDA approval만으로 Green 금지
- 플랫폼 기술 headline만으로 royalty cashflow를 만들지 않음
- CDMO 공장 인수만으로 utilization과 margin을 발명하지 않음
- 정책 지원/관세 완화 기대만으로 회사별 FCF 개선을 만들지 않음
- M&A pop은 order book과 utilization 전까지 event premium 또는 4B-watch
- 정부 백신 구매는 실제 접종 수요가 아니므로 administered demand를 별도 확인

## 생성 파일

- `src/e2r/sector/round276_r7_loop13_biotech_healthcare_device_price_validation.py`
- `src/e2r/cli/build_round276_r7_loop13_report.py`
- `tests/test_round276_r7_loop13_biotech_healthcare_device_price_validation.py`
- `data/e2r_case_library/cases_r7_loop13_round276.jsonl`
- `data/sector_taxonomy/round276_r7_loop13_biotech_healthcare_device_price_validation_audit.json`
- `output/e2r_round276_r7_loop13_biotech_healthcare_device_price_validation/`

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests.test_round276_r7_loop13_biotech_healthcare_device_price_validation -v
PYTHONPATH=src python -m compileall -q src/e2r/sector/archetypes.py src/e2r/sector/round276_r7_loop13_biotech_healthcare_device_price_validation.py src/e2r/cli/build_round276_r7_loop13_report.py tests/test_round276_r7_loop13_biotech_healthcare_device_price_validation.py
PYTHONPATH=src python -m e2r.cli.build_round276_r7_loop13_report
PYTHONPATH=src python -m unittest discover -s tests -v
```

라운드 전용 테스트 7개와 전체 테스트 3189개가 통과했다.

## 해석

이번 패치는 점수를 바꾸는 작업이 아니라 바이오/헬스케어 archetype의 실패 패턴을 더 정확히 기록하는 작업이다. `Yuhan/lazertinib`은 FDA 승인으로 Stage 2 후보가 될 수 있지만, 처방 ramp와 royalty cashflow가 있어야 Green 후보가 된다. `SkyCovione`은 승인과 정부 구매가 실제 접종 수요로 이어지지 않을 수 있다는 hard reference다.
