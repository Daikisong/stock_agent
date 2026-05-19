# Checkpoint 28A Round 206 R2 Loop 8 AI Semiconductor Price Validation

Round 206 반영 범위:

- source round: `docs/round/round_206.md`
- large sector: `AI_SEMICONDUCTOR_ELECTRONICS`
- 목적: HBM 리더, HBM 장비, HBM catch-up, design win, policy foundry, export-control shock, OpenAI/Stargate 이벤트의 가격경로를 case-library 검증 자료로 추가
- 상태: calibration/evaluation only

## 추가된 케이스

| case_id | 해석 |
| --- | --- |
| `r2_loop8_sk_hynix_hbm_aligned_4b` | SK하이닉스 HBM dominance와 EPS revision이 대형 MFE와 맞은 aligned benchmark. 2026년에는 4B-watch/elevated |
| `r2_loop8_hanmi_semiconductor_hbm_bonder_4b` | confirmed SK Hynix HBM bonder order는 Stage 3 후보지만, unconfirmed Micron report 급등은 4B-watch |
| `r2_loop8_samsung_memory_recovery_hbm_watch` | 삼성전자 commodity memory 회복은 Stage 2 watch. HBM execution 전 Green 보류 |
| `r2_loop8_gaonchips_pfn_design_win` | 가온칩스 design win은 Stage 2 evidence. tape-out, 양산, 매출, margin 전 Green 금지 |
| `r2_loop8_db_hitek_policy_foundry` | DB하이텍 policy foundry 협의는 Stage 1~약한 Stage 2 이벤트. 회사 단위 order/utilization/EPS 전 Green 금지 |
| `r2_loop8_hana_micron_hanmi_export_control_watch` | export-control shock은 4C-watch. 실제 생산·매출 차질 전 hard 4C 아님 |
| `r2_loop8_openai_stargate_memory_4b` | OpenAI/Stargate는 AI memory 수요 검증이지만, 이미 오른 HBM winner에게는 4B-watch |

## 핵심 판단

- R2 Stage 3-Green에는 company-level customer evidence, product-specific exposure, order/shipment/revenue path, margin/OPM, EPS/FCF revision, capacity bottleneck이 필요하다.
- `ai_keyword_only`, `server_theme_only`, `design_win_without_revenue`, `policy_foundry_without_order`, `unconfirmed_customer_media_report`는 Green 금지 패턴이다.
- 예: `as_of_date=2024-07-09`에 가온칩스가 Preferred Networks AI chip 설계사로 언급되어도, 그날 양산·매출·마진이 없으면 Stage 3-Green이 아니라 Stage 2 watch다.

## 산출물

- `data/e2r_case_library/cases_r2_loop8_round206.jsonl`
- `data/sector_taxonomy/round206_r2_loop8_ai_semiconductor_price_validation_audit.json`
- `output/e2r_round206_r2_loop8_ai_semiconductor_price_validation/round206_r2_loop8_price_validation_summary.md`
- `output/e2r_round206_r2_loop8_ai_semiconductor_price_validation/round206_r2_loop8_case_matrix.csv`
- `output/e2r_round206_r2_loop8_ai_semiconductor_price_validation/round206_r2_loop8_target_aliases.csv`
- `output/e2r_round206_r2_loop8_ai_semiconductor_price_validation/round206_r2_loop8_score_adjustments.csv`
- `output/e2r_round206_r2_loop8_ai_semiconductor_price_validation/round206_r2_loop8_price_validation_fields.csv`
- `output/e2r_round206_r2_loop8_ai_semiconductor_price_validation/round206_r2_loop8_green_gate_review.md`
- `output/e2r_round206_r2_loop8_ai_semiconductor_price_validation/round206_r2_loop8_price_validation_plan.md`
- `output/e2r_round206_r2_loop8_ai_semiconductor_price_validation/round206_r2_loop8_stage4b_4c_review.md`

## 하지 않은 것

- production scoring threshold 변경 없음
- StageClassifier 변경 없음
- case labels를 후보 생성 input으로 사용하지 않음
- 전체 OHLC 가격을 발명하지 않음
- 투자 권고 문구 없음

## 다음 단계

Round 206의 가격값은 Reuters/WSJ/FT/MarketWatch/Tom's Hardware reported anchor다. 다음 가격 백필 단계에서는 조정 일봉으로 Stage 2/3/4B 가격, MFE/MAE, peak 이후 drawdown을 재계산해야 한다.
