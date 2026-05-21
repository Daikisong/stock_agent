# Checkpoint 28A Round 302 R7 Loop 15 Bio/Healthcare/Medical Device Trigger Validation

## 목적

`docs/round/round_302.md`의 R7 Loop 15 내용을 calibration/evaluation 전용 case pack으로 반영했다.

이번 라운드의 핵심은 FDA 승인, CDMO 공장 인수, 기술이전 LO, 의료기기 M&A를 한 신호로 묶지 않는 것이다. 쉬운 예로, FDA 승인은 제품이 허가 문턱을 넘은 것이지만, Stage 3-Green은 실제 출시, 채택, 매출 또는 로열티가 확인되어야 한다.

## 반영 내용

- R7 canonical archetype 9개를 추가했다.
- Alteogen, Samsung Biologics, Celltrion, SK Bioscience, Hugel, Jeisys Medical, Samsung Bioepis, ADEL reference case를 구조화했다.
- trigger-level reported event anchor를 저장했다.
- full adjusted OHLC가 없다는 이유로 Stage 후보를 강등하지 않고 `reported_event_anchor_not_full_ohlc`로 분리했다.
- 생산 scoring/staging/candidate generation은 변경하지 않았다.

## 추가된 산출물

- `src/e2r/sector/round302_r7_loop15_bio_healthcare_medical_device_trigger_validation.py`
- `src/e2r/cli/build_round302_r7_loop15_report.py`
- `tests/test_round302_r7_loop15_bio_healthcare_medical_device_trigger_validation.py`
- `data/e2r_case_library/cases_r7_loop15_round230.jsonl`
- `data/e2r_trigger_calibration/triggers_r7_loop15_round230.jsonl`
- `data/sector_taxonomy/round302_r7_loop15_bio_healthcare_medical_device_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round230_r7_loop15_v1.csv`
- `output/e2r_round302_r7_loop15_bio_healthcare_medical_device_trigger_validation/`

## 핵심 판정

- Alteogen / Keytruda Qlex는 Stage3-Yellow to Green candidate다.
- Alteogen / Halozyme patent risk는 hard 4C가 아니라 4C-watch다.
- Samsung Biologics와 Celltrion의 U.S. localization은 utilization, customer transfer, order, margin 전에는 Stage2다.
- SK Bioscience / IDT Biologika는 M&A와 +11.7% event return이 있어 Stage2-Actionable이다.
- Hugel / Letybo는 FDA-approved U.S. launch지만 clinic adoption, sell-through, margin 전에는 Yellow가 아니다.
- Jeisys / ArchiMed는 operating Green이 아니라 control-premium M&A event다.
- Samsung Bioepis / Amgen lawsuit는 biosimilar patent litigation 4C-watch다.
- ADEL / Sanofi는 private reference이며 public-market candidate input이 아니다.

## Green Guardrail

Stage 3-Green을 막는 대표 조건:

- FDA trial result only
- FDA approval without launch or revenue
- CDMO capacity headline only
- factory acquisition without utilization
- total LO value without upfront and milestone probability
- biosimilar approval without patent clearance
- aesthetic launch without clinic sell-through
- policy support without company order or margin
- private company reference used as public candidate

즉, `FDA 승인`은 Stage2 또는 Yellow 후보일 수 있지만, `매출/로열티/채택률/특허 리스크 해소`가 없으면 Green 확정 근거가 아니다.

## 테스트

실행:

```bash
PYTHONPATH=src python -m unittest tests.test_round302_r7_loop15_bio_healthcare_medical_device_trigger_validation -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m e2r.cli.build_round302_r7_loop15_report
```

결과:

- round_302 전용 테스트 통과
- compileall 통과
- R7 output pack 생성 완료

## 변경하지 않은 것

- production scoring 변경 없음
- StageClassifier threshold 변경 없음
- candidate generation 변경 없음
- case library를 production input으로 사용하지 않음
- full OHLC/MFE/MAE를 발명하지 않음
- 투자 권고 문구 없음

## 다음 작업

R7은 trigger-level anchor만 확보된 상태다. 다음 단계에서는 각 trigger date 기준 30D/90D/180D/1Y adjusted OHLC, below-entry 여부, royalty recognition, utilization, settlement, clinic sell-through를 채워야 한다.
