# Checkpoint 28A Round 250 R7 Loop 11 Biotech Healthcare Device Price Validation

## 목적

`docs/round/round_250.md`의 R7 Loop 11 바이오·헬스케어·의료기기 가격검증 내용을 구조화했다.

이번 라운드는 production scoring 변경이 아니다. 케이스 라이브러리와 shadow weight, Green gate, 4B/4C 감시 조건을 보강하는 calibration/evaluation 작업이다.

쉬운 예시:

- `FDA 승인`은 Stage 2 관심 신호다.
- 하지만 `처방량`, `로열티/매출`, `수가`, `병원 도입`, `마진`, `FCF`가 확인되기 전에는 Stage 3-Green이 아니다.

## 반영 파일

- `src/e2r/sector/round250_r7_loop11_biotech_healthcare_device_price_validation.py`
- `src/e2r/cli/build_round250_r7_loop11_report.py`
- `tests/test_round250_r7_loop11_biotech_healthcare_device_price_validation.py`
- `data/e2r_case_library/cases_r7_loop11_round250.jsonl`
- `data/sector_taxonomy/round250_r7_loop11_biotech_healthcare_device_price_validation_audit.json`
- `output/e2r_round250_r7_loop11_biotech_healthcare_device_price_validation/`

## 추가/확인한 Archetype

- `BIO_PLATFORM_ROYALTY_CONVERSION`
- `KOREAN_NEW_DRUG_GLOBAL_APPROVAL`
- `CDMO_US_TARIFF_HEDGE_CAPACITY`
- `CMO_M_AND_A_TRANSITION`
- `BIOPHARMA_POLICY_TARIFF_RELIEF`
- `AUTOIMMUNE_PARTNER_TRIAL_FAILURE`
- `MEDICAL_AI_EXTERNAL_VALIDATION`
- `APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN`
- `EVENT_PREMIUM`
- `EVIDENCE_GOOD_BUT_PRICE_FAILED`

## 케이스 요약

| case | 판단 |
|---|---|
| Alteogen / Keytruda SC | platform royalty Stage 2. 로열티·공급매출·특허 지속성 전 Green 금지 |
| Yuhan / Lazertinib | 글로벌 승인 Stage 2. 처방·마일스톤·로열티 인식 전 Green 금지 |
| Samsung Biologics | U.S. CDMO 시설 증거는 좋지만 가격 확인 실패. `evidence_good_but_price_failed` |
| Celltrion | U.S. tariff hedge manufacturing Stage 2. 제품 이전·가동률·마진·FCF 필요 |
| SK Bioscience | IDT CMO M&A Stage 2 + event premium. backlog/utilization 전 Green 금지 |
| HanAll / Immunovant | partner trial failure 4C-watch. 회사 전체 hard 4C는 확정하지 않음 |
| Lunit | 외부검증 AUC 0.91 Stage 2. 수가·도입·반복매출 전 Green 금지 |
| Biopharma policy basket | 정책지원 event premium. 회사별 매출·마진·FCF 전 Green 금지 |

## Green Gate 보강

R7 Stage 3-Green 필수 조건을 명시했다.

- approval/clearance/launch 확인
- commercial launch 이후 매출 확인
- prescription/procedure volume 확인
- reimbursement/payer/ASP 확인
- royalty/milestone/supply revenue 확인
- gross margin 또는 royalty margin 확인
- capacity utilization 또는 contract backlog 확인
- cash runway/dilution risk 통과
- partner execution risk 통과
- evidence 이후 price path 확인

금지 패턴도 별도 분리했다.

- FDA approval only
- clinical headline only
- external validation without revenue
- policy support without order
- M&A without utilization
- facility acquisition without backlog
- partner pipeline without indication success
- royalty unconfirmed platform story
- medical AI AUC without reimbursement

## 4B / 4C 감시

4B-watch:

- FDA 승인 직후 가격 급등
- 대형 파트너명만으로 valuation 급등
- 로열티 인식 전 platform stock rerating
- M&A 발표 전후 event premium
- 정책지원 당일 sector rally
- 의료AI 외부검증만으로 가격 급등
- CDMO capacity premium이 가동률보다 먼저 확장

Hard 4C gate:

- FDA CRL / 허가 거절
- 효능·안전성 임상 실패
- partner trial failure
- commercial launch failure
- royalty non-recognition
- reimbursement failure
- manufacturing inspection failure
- subgroup clinical performance failure
- capacity utilization failure
- large dilution / cash runway break

이번 라운드에서는 `hard_4c_confirmed=false`를 유지했다.

## 산출물

- `round250_r7_loop11_price_validation_summary.md`
- `round250_r7_loop11_case_matrix.csv`
- `round250_r7_loop11_target_aliases.csv`
- `round250_r7_loop11_deep_sub_archetypes.csv`
- `round250_r7_loop11_score_adjustments.csv`
- `round250_r7_loop11_shadow_weights.csv`
- `round250_r7_loop11_price_validation_fields.csv`
- `round250_r7_loop11_green_gate_review.md`
- `round250_r7_loop11_price_validation_plan.md`
- `round250_r7_loop11_stage4b_4c_review.md`

## 유지한 제약

- production scoring 변경 없음
- candidate generation input 아님
- Stage 3-Green 기준 완화 없음
- full OHLC 없는 항목은 `price_data_unavailable_after_deep_search`로 유지
- 로열티, 처방량, 수가, 가동률, 마진, FCF를 임의 생성하지 않음
- 투자 권고 문구 없음
