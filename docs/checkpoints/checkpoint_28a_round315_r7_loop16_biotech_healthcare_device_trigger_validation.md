# Checkpoint 28A Round 315 R7 Loop 16: Bio / Healthcare / Medical Device Trigger Validation

## 목적

`docs/round/round_315.md`의 R7 Loop 16 분석을 레포의 case-library / trigger-calibration 형식으로 반영했다. 이번 라운드는 바이오, CDMO, 의료기기 이벤트를 “승인/시설/인수/소송/관세 헤드라인”만으로 Green 처리하지 않기 위한 검증팩이다.

쉬운 예시는 FDA 승인이다. FDA 승인은 Stage 2 근거가 될 수 있지만, 실제 로열티, 매출, 파트너 제품 채택률, 제조 품질 문제가 같이 확인되지 않으면 Stage 3-Green으로 올리지 않는다.

## 추가한 canonical archetype

- `SC_FORMULATION_PLATFORM_STAGE3_YELLOW`
- `BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2`
- `CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED`
- `BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE`
- `ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B`
- `AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2`
- `PHARMA_TARIFF_4B_4C_WATCH`

기존에 있던 `VACCINE_CDMO_MA_STAGE2_ACTIONABLE`, `BIOSIMILAR_PATENT_LITIGATION_4C_WATCH`도 이번 라운드의 target alias에 포함했다.

## 반영한 케이스

- Alteogen / Merck Keytruda Qlex: Stage 3-Yellow candidate
- Samsung Biologics / Korea biopharma policy support: Stage 2 policy support
- Samsung Biologics / GSK U.S. facility: Stage 2, price-muted
- SK Bioscience / IDT Biologika: Stage 2-Actionable M&A
- Celltrion / U.S. factory localization: Stage 2 with capex gate
- Yuhan / J&J Rybrevant lazertinib: Stage 2 plus manufacturing 4B-watch
- Samsung Bioepis / Amgen Prolia-Xgeva litigation: 4C-watch
- Jeisys Medical / ArchiMed: Stage 2 M&A with control-premium overlay
- Korea pharma tariff localization basket: 4B/4C-watch plus localization hedge

## 핵심 규칙

- `Stage 2-Actionable`: 승인, M&A, 시설, 정책 이벤트가 있고 가격/거래 반응이나 명시적 경제성이 있을 때.
- `Stage 3-Yellow`: 제품 판매, 채택률, 로열티 가능성이 보이지만 직접 가격 앵커나 전체 OHLC가 부족할 때.
- `Stage 3-Green`: 로열티/매출/시설 가동률/특허 해결/제조 품질/마진 보호가 같이 확인될 때만 가능.
- `4B/4C-watch`: 승인 헤드라인이 먼저 가격에 반영됐거나, 제조 CRL, 특허소송, 관세 충격, 시설 가동률 부재가 있을 때.

## 생성 파일

- `src/e2r/sector/round315_r7_loop16_biotech_healthcare_device_trigger_validation.py`
- `src/e2r/cli/build_round315_r7_loop16_report.py`
- `tests/test_round315_r7_loop16_biotech_healthcare_device_trigger_validation.py`
- `data/e2r_case_library/cases_r7_loop16_round243.jsonl`
- `data/e2r_trigger_calibration/triggers_r7_loop16_round243.jsonl`
- `data/sector_taxonomy/round315_r7_loop16_biotech_healthcare_device_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round243_r7_loop16_v1.csv`
- `output/e2r_round315_r7_loop16_biotech_healthcare_device_trigger_validation/`

## 안전장치

- production scoring 변경 없음.
- candidate generation 입력으로 사용하지 않음.
- shadow weight only.
- 전체 adjusted OHLC / MFE / MAE가 없으므로 Green 확정에 사용하지 않음.
- case library는 calibration/evaluation 전용이다.

## 다음 단계

`R8 Loop 16`에서는 실제 adjusted OHLC 가격 경로를 보강하고, 승인/시설/M&A 이벤트가 Stage 2 이후 어떤 가격 검증을 통과했는지 별도 row로 분리해야 한다.
