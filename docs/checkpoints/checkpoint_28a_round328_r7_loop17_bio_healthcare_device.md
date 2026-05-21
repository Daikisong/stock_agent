# Checkpoint 28A Round 328 R7 Loop 17 Bio/Healthcare/Medical Device

## 목적

`docs/round/round_328.md`의 바이오/헬스케어/의료기기 트리거 검증 내용을 case-library와 shadow weight 산출물로 구조화했다.

이번 패치는 생산 scoring/staging을 바꾸지 않는다. 예를 들어, FDA 승인이나 미국 공장 인수는 Stage2 신호가 될 수 있지만, 실제 매출 전환, 가동률, royalty economics, sell-through가 없으면 Stage3-Green으로 승격하지 않는다.

## 추가된 canonical archetype

- `BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE`
- `CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED`
- `VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE`
- `BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE`
- `PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW`
- `AESTHETIC_TOXIN_US_FDA_STAGE2`
- `MEDICAL_AESTHETIC_DEVICE_MA_STAGE2`
- `BIOSIMILAR_PATENT_LITIGATION_4B`

## 케이스 요약

- SK Bioscience / IDT Biologika: `Stage2-Actionable`
- Samsung Biologics policy support: `Stage2-Actionable`
- Samsung Biologics / GSK U.S. facility: `Stage2`, evidence-good but price-failed
- Celltrion U.S. factory localization: `Stage2`, no direct price anchor
- Alteogen / Keytruda SC: `Stage3-Yellow candidate`, not Green
- Hugel / Letybo U.S. FDA launch: `Stage2`
- Jeisys / Archimed medical aesthetic M&A: `Stage2 reference`
- Samsung Bioepis / Amgen patent litigation: `4B-watch`, not hard 4C

## 산출물

- `data/e2r_case_library/cases_r7_loop17_round256.jsonl`
- `data/e2r_trigger_calibration/triggers_r7_loop17_round256.jsonl`
- `data/sector_taxonomy/round328_r7_loop17_bio_healthcare_device_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round256_r7_loop17_v1.csv`
- `output/e2r_round328_r7_loop17_bio_healthcare_device_trigger_validation/round328_summary.md`
- `output/e2r_round328_r7_loop17_bio_healthcare_device_trigger_validation/stage_rules.md`
- `output/e2r_round328_r7_loop17_bio_healthcare_device_trigger_validation/stage4b_4c_review.md`
- `output/e2r_round328_r7_loop17_bio_healthcare_device_trigger_validation/price_validation_plan.md`

## Green 금지 조건

- 시설 인수만 있고 가동률이 없는 경우
- 정책 지원만 있고 회사별 계약이나 마진 브리지가 없는 경우
- FDA 승인만 있고 sell-through가 없는 경우
- 플랫폼 linkage만 있고 royalty visibility가 없는 경우
- M&A reference지만 public liquidity가 없는 경우
- biosimilar opportunity가 있지만 patent clearance가 없는 경우
- sourced price anchor 없이 hard 4C를 단정하는 경우

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round328_r7_loop17_bio_healthcare_device_trigger_validation -v`

## 다음 작업

- full adjusted OHLC를 별도 backfill해서 MFE/MAE/peak/drawdown을 채워야 한다.
- CDMO 시설 인수 케이스는 utilization, customer transfer, batch margin을 추적해야 한다.
- 플랫폼 효소 케이스는 royalty/supply economics와 patent litigation containment가 Stage3-Green 전 필수 gate다.
