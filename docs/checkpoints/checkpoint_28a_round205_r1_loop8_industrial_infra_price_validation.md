# Checkpoint 28A Round 205 R1 Loop 8 Industrial Infrastructure Price Validation

Round 205 반영 범위:

- source round: `docs/round/round_205.md`
- large sector: `INDUSTRIAL_ORDERS_INFRA`
- 목적: 방산 수주, 조선/MRO, IPO 프리미엄, 제재 이벤트, 합병/정책 이벤트의 가격경로를 case-library 검증 자료로 추가
- 상태: calibration/evaluation only

## 추가된 케이스

| case_id | 해석 |
| --- | --- |
| `r1_loop8_hyundai_rotem_k2_aligned` | K2 수출/현지생산 visibility와 이후 대형 가격경로가 맞은 aligned 방산 사례 |
| `r1_loop8_hanwha_aerospace_mfe_4b` | 방산 구조적 성공이지만 대형 MFE 이후에는 신규 Green보다 4B-watch/elevated로 봐야 하는 사례 |
| `r1_loop8_lig_nex1_cheongung_watch` | 천궁/요격 실전 검증은 Stage 2 watch 근거지만 Stage 3에는 계약기간·EPS 전환 확인 필요 |
| `r1_loop8_kai_fa50_stage2` | FA-50 수출 backlog는 Stage 2 watch 근거지만 납품·마진·EPS visibility가 필요 |
| `r1_loop8_hd_hyundai_marine_ipo_premium` | IPO 첫날 급등은 MRO 반복매출 증거가 아니므로 이벤트 프리미엄으로 분리 |
| `r1_loop8_hanwha_ocean_china_sanction` | 중국 제재는 4C-watch지만 매출 차질·계약취소·금융 실패 전까지 hard 4C는 아님 |
| `r1_loop8_hd_hyundai_heavy_mipo_merger_4b` | 조선 합병/정책 이벤트 급등은 Stage 2 watch 가능성이지만 Green 근거는 아님 |

## 핵심 판단

- Green에는 `contract_amount_confirmed`, `delivery_schedule`, `actual_delivery_or_revenue_recognition`, `opm_or_eps_revision`, `backlog_quality`가 필요하다.
- `order_headline_only`, `ipo_first_day_rally`, `mou_or_preliminary_policy_event`, `record_high_on_policy_event`는 Green 금지 패턴이다.
- 예: `as_of_date=2024-05-08`에 HD현대마린솔루션이 IPO 첫날 크게 올라도, 그날 확인 가능한 반복매출·마진·EPS 전환 증거가 없으면 Stage 3-Green이 아니라 이벤트 프리미엄이다.

## 산출물

- `data/e2r_case_library/cases_r1_loop8_round205.jsonl`
- `data/sector_taxonomy/round205_r1_loop8_industrial_infra_price_validation_audit.json`
- `output/e2r_round205_r1_loop8_industrial_infra_price_validation/round205_r1_loop8_price_validation_summary.md`
- `output/e2r_round205_r1_loop8_industrial_infra_price_validation/round205_r1_loop8_case_matrix.csv`
- `output/e2r_round205_r1_loop8_industrial_infra_price_validation/round205_r1_loop8_target_aliases.csv`
- `output/e2r_round205_r1_loop8_industrial_infra_price_validation/round205_r1_loop8_score_adjustments.csv`
- `output/e2r_round205_r1_loop8_industrial_infra_price_validation/round205_r1_loop8_price_validation_fields.csv`
- `output/e2r_round205_r1_loop8_industrial_infra_price_validation/round205_r1_loop8_green_gate_review.md`
- `output/e2r_round205_r1_loop8_industrial_infra_price_validation/round205_r1_loop8_price_validation_plan.md`
- `output/e2r_round205_r1_loop8_industrial_infra_price_validation/round205_r1_loop8_stage4b_4c_review.md`

## 하지 않은 것

- production scoring threshold 변경 없음
- StageClassifier 변경 없음
- case labels를 후보 생성 input으로 사용하지 않음
- 전체 OHLC 가격을 발명하지 않음
- 투자 권고 문구 없음

## 다음 단계

Round 205의 reported price anchors는 정식 OHLC가 아니다. 다음 가격 백필 단계에서는 KRX/Naver/Yahoo 등 조정 일봉 소스로 `stage2_price`, `stage3_price`, `stage4b_price`, `peak_price`, MFE/MAE를 재계산해야 한다.
