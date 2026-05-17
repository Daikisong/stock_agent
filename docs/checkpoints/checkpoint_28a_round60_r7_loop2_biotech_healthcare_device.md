# Checkpoint 28A Round 60: R7 Loop 2 바이오·헬스케어·의료기기

## 반영 요약

- 원문: `docs/round/round_60.md`
- 신규 calibration 모듈: `src/e2r/sector/round60_r7_loop2_biotech_healthcare_device.py`
- 신규 CLI: `src/e2r/cli/build_round60_r7_loop2_report.py`
- 신규 테스트: `tests/test_round60_r7_loop2_biotech_healthcare_device.py`
- 케이스 팩: `data/e2r_case_library/cases_r7_loop2_round60.jsonl`
- 점수 비중 초안: `data/sector_taxonomy/score_weight_profiles_round60_r7_loop2_v2.csv`
- 산출물 디렉터리: `output/e2r_round60_r7_loop2_biotech_healthcare_device/`

## 핵심 판단

R7 Loop 2는 `허가`, `임상 성공`, `AI 논문`, `대형 시장`, `사용자 수`를 실제 상업화 증거와 분리한다.

쉬운 예시:

- `FDA 허가`는 Stage 1~2 신호일 수 있다.
- 하지만 처방량, 보험/환급, 매출, OPM, FCF가 없으면 Stage 3-Green 근거로 쓰면 안 된다.
- `AI 의료영상 AUC 0.91`도 좋은 연구 증거지만, 병원 도입, 수가, 반복매출이 없으면 상업화 증거가 아니다.

## Round 60 coverage

- target_count: 16
- case_candidate_count: 17
- structural_success_count: 1
- success_candidate_count: 8
- event_premium_count: 1
- stage4c_case_count: 7
- green_possible_count: 4
- watch_yellow_first_count: 7
- redteam_first_count: 5
- gate_only_target_count: 1

## Green 가능 축

- `CDMO_HEALTHCARE_CONTRACT`: 장기계약, capacity utilization, 고객사 다변화, FCF conversion 필요.
- `OBESITY_GLP1_COMMERCIALIZATION`: 처방량, 보험, 가격 방어, 공급능력, OP/EPS 필요.
- `MEDICAL_DEVICE_HEALTHCARE_EXPORT`: 수출국, 반복시술, 소모품, OPM/ROE 필요.
- `MEDICAL_DEVICE_DENTAL_IMPLANT`: 반복시술/소모품은 긍정적이나 VBP/ASP 하락 감시 필요.

## RedTeam / Watch 강화 축

- `PHARMA_CHANNEL_AND_PRIVACY_RISK`는 일반 점수 bucket이 아니라 gate-only overlay로 둔다.
- `GENE_THERAPY_RARE_DISEASE`는 승인 후에도 uptake, reimbursement, cash runway가 없으면 4C가 될 수 있다.
- `AI_DRUG_DISCOVERY_PLATFORM`은 milestone, 임상 진입, cash runway 전까지 Green 금지.
- `TELEHEALTH_BEHAVIORAL_HEALTH`는 CAC, churn, impairment, privacy가 핵심 risk다.
- `DIAGNOSTICS_INFECTIOUS_DISEASE`는 one-off 진단 수요를 구조적 수요로 과대외삽하지 않는다.

## 주요 케이스

- `samsung_biologics_gsk_us_facility_case`: 미국 생산거점과 capacity는 전략적이나, 고객계약/가동률/FCF 필요.
- `lilly_foundayo_fda_approval_case`: GLP-1 허가 자체는 Stage 1~2, 처방량/보험/가격이 Green gate.
- `lilly_foundayo_prescription_uptake_case`: 초기 처방량이 modest하면 approval-without-uptake로 진단.
- `novo_glp1_price_pressure_case`: 거대 TAM도 가격/경쟁/보험 압박으로 4B→4C 가능.
- `hims_compounded_glp1_crackdown_case`: 조제약 채널 규제는 pharma channel hard risk.
- `bluebird_gene_therapy_cash_crunch_case`: 승인 치료제도 상업화·현금흐름 실패 시 thesis break.
- `lunit_dbt_subgroup_validation_case`: 외부검증/AUC는 의미 있지만 수가·병원도입·반복매출 필요.
- `botox_counterfeit_fda_warning_case`: 미용시술 반복수요가 있어도 위조품/미승인/안전 이슈는 hard risk.

## Green Guardrails

- 허가/임상/논문/AUC/파일럿만으로 Green 금지.
- CDMO capacity만으로 Green 금지. 가동률과 계약이 필요하다.
- GLP-1 TAM만으로 Green 금지. 처방량·보험·가격·OP/EPS가 필요하다.
- 의료AI 성능 논문만으로 Green 금지. 병원 도입·수가·반복매출이 필요하다.
- 유전자치료제 승인을 상업화로 착각 금지. 환급·환자 투여·cash runway가 필요하다.
- 처방량, 환급, 가동률, 병원도입, 현금 runway, CAC, churn, stage price는 비어 있으면 비워 둔다.

## 검증

실행한 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_round60_r7_loop2_biotech_healthcare_device -v
```

결과:

- 12개 테스트 통과

## 다음 단계

Round 60은 production scoring을 바꾸지 않는다. 이 팩은 다음 shadow scoring에서 “상업화가 확인된 헬스케어”와 “허가·AI·TAM만 있는 헬스케어”를 분리하기 위한 검증 자료다.
