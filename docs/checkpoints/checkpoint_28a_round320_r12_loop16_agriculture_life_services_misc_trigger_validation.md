# Checkpoint 28A Round320: R12 Loop 16 농업·생활서비스·기타 트리거 검증팩

## 목적

Round320은 농업, 생활서비스, 교육, 반려동물, 인구정책, 의료교육 이벤트를 E2R 케이스 라이브러리 검증팩으로 추가한다.

이 작업은 생산 점수나 StageClassifier를 바꾸지 않는다. 예를 들어 배달앱 M&A 보도는 Stage 2 관찰 신호가 될 수 있지만, 최종 SPA, 승인, GMV, take-rate, 마진 연결이 없으면 Stage 3-Green으로 올리지 않는다.

## 추가된 아키타입

- `FOOD_DELIVERY_PLATFORM_MA_STAGE2_WITH_APPROVAL_4B`
- `EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C`
- `FOOD_PRICE_INFLATION_IMPORT_QUOTA_STAGE2_4B`
- `FEED_WHEAT_COST_SHOCK_4B`
- `PET_WELFARE_POLICY_TRANSITION_STAGE2_NO_PRICE`
- `EDUCATION_EXAM_DEMAND_STAGE2_NO_PRICE`
- `FERTILITY_CHILDCARE_POLICY_STAGE2_NO_PRICE`
- `MEDICAL_EDUCATION_QUOTA_POLICY_4B_RELIEF`

## 케이스 요약

- 배민/Naver/Uber 음식배달 M&A: Stage 2 + 4B-watch. 최종 승인과 단위경제 연결 전에는 Green 금지.
- 쿠팡 데이터 유출/생활배송 점유율 이동: 피해 플랫폼은 hard 4C, 경쟁사 관찰은 GMV·배송량·마진 전환 필요.
- 식품물가/수입할당 정책: 회사별 가격 전가, 수요 탄력성, 매출총이익 회복 전에는 Stage 2/4B.
- 사료용 밀 입찰 실패: 비용 쇼크 4B/4C 리스크이며, 수요 증가 신호가 아니다.
- 개 식용 금지/반려동물 전환: 정책 참조 신호이며, 상장 펫푸드·동물병원·서비스 매출 연결 필요.
- 수능 응시자 증가/교육 수요: ARPU, 반복 등록, 마진 연결 전에는 Stage 2 참조.
- 출산율 반등/보육 파이프라인: 1년 반등만으로는 부족하고 다년 지속성과 상장사 매출 연결 필요.
- 의대 정원 동결/의료교육 완화: 전공의 복귀, 병원 서비스 정상화, 매출 회복 전에는 relief reference.

## 산출물

- `data/e2r_case_library/cases_r12_loop16_round248.jsonl`
- `data/e2r_trigger_calibration/triggers_r12_loop16_round248.jsonl`
- `data/sector_taxonomy/round320_r12_loop16_agriculture_life_services_misc_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round248_r12_loop16_v1.csv`
- `output/e2r_round320_r12_loop16_agriculture_life_services_misc_trigger_validation/`

## 검증 상태

- 케이스 후보: 8개
- 트리거: 8개
- Stage2 후보: 6개
- Stage3-Yellow 후보: 5개
- Stage3-Green 확정: 0개
- Stage4B-watch: 7개
- Stage4C-watch: 3개
- hard 4C: 1개

## 바꾸지 않은 것

- 생산 점수 변경 없음
- 후보 생성 입력으로 케이스 라이브러리 사용 없음
- Stage 3-Green 기준 완화 없음
- 전체 조정 OHLC 없이 MFE/MAE를 지어내지 않음

## 실행 명령

```bash
PYTHONPATH=src python -m e2r.cli.build_round320_r12_loop16_report
PYTHONPATH=src python -m unittest tests.test_round320_r12_loop16_agriculture_life_services_misc_trigger_validation -v
```
