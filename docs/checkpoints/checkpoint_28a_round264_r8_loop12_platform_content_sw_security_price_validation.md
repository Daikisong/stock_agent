# Checkpoint 28A Round 264 R8 Loop 12 Platform Content SW Security Price Validation

## 반영 범위

- 원문: `docs/round/round_264.md`
- analyst_round_id: `round_192`
- 대섹터: `PLATFORM_CONTENT_SW_SECURITY`
- 산출 모듈: `src/e2r/sector/round264_r8_loop12_platform_content_sw_security_price_validation.py`
- 생성 CLI: `src/e2r/cli/build_round264_r8_loop12_report.py`
- production scoring 변경: `false`
- candidate generation input: `false`
- shadow weight only: `true`

## 추가한 canonical archetype

- `GAME_IP_IPO_SINGLE_TITLE_RISK`
- `KIDS_CONTENT_IP_IPO_EVENT_PREMIUM`
- `KPOP_IP_CHINA_OPTIONALITY`
- `DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE`
- `ECOMMERCE_PLATFORM_DATA_BREACH_4C`
- `GAME_STUDIO_M_AND_A_GOVERNANCE_4C`
- `TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C`

## 케이스 요약

| case | 판정 | 핵심 |
|---|---|---|
| Shift Up | Stage 2/watch | IPO와 히트 타이틀은 강하지만 retention, repeat title, FCF 전 Green 금지 |
| Pinkfong | event premium | Baby Shark 조회수와 IPO pop은 반복 현금흐름 증거가 아님 |
| SM/Tencent | Stage 2 optionality | 중국 재개 기대는 실제 공연/티켓 매출 전 Green 금지 |
| NAVER/Dunamu | Stage 2 + 4C-watch | deal value보다 exchange trust와 abnormal withdrawal을 먼저 봄 |
| Coupang | non-KRX 4C reference | 플랫폼 데이터 유출 guardrail 참고사례 |
| Krafton/Unknown Worlds | 4C-watch | 인수 IP는 release revenue와 governance clarity 전 Green 금지 |
| SK Telecom | direct KRX hard 4C | 보안 사고가 가격, 매출전망, 보안투자, 보상 리스크로 연결됨 |

## Green gate 보정 방향

이번 라운드는 점수 적용이 아니라 보정 재료다. 예를 들어 `IPO +62%`는 강한 이벤트지만, 후속 IP와 licensing margin이 없으면 Stage 3-Green 근거가 아니다. `M&A deal value`도 closing, integration, regulated revenue, trust recovery가 없으면 Stage 2/watch에 머문다.

강화해야 할 축:

- paid user / active user retention
- ARPU / take-rate / paid usage
- repeat hit generation
- IP licensing / merchandise / platform fee revenue
- live-service retention
- platform / exchange trust
- cybersecurity control
- data governance
- regulatory closing
- operating leverage / FCF

감점해야 할 축:

- IPO pop only
- single-title or single-IP concentration
- M&A announcement only
- China reopening optionality only
- digital-asset platform without trust recovery
- exchange abnormal withdrawal
- data breach
- cybersecurity revenue cut

## 산출물

- `data/e2r_case_library/cases_r8_loop12_round264.jsonl`
- `data/sector_taxonomy/round264_r8_loop12_platform_content_sw_security_price_validation_audit.json`
- `output/e2r_round264_r8_loop12_platform_content_sw_security_price_validation/round264_r8_loop12_price_validation_summary.md`
- `output/e2r_round264_r8_loop12_platform_content_sw_security_price_validation/round264_r8_loop12_case_matrix.csv`
- `output/e2r_round264_r8_loop12_platform_content_sw_security_price_validation/round264_r8_loop12_green_gate_review.md`
- `output/e2r_round264_r8_loop12_platform_content_sw_security_price_validation/round264_r8_loop12_stage4b_4c_review.md`

## 검증

실행 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round264_r8_loop12_platform_content_sw_security_price_validation.py -v
PYTHONPATH=src python -m e2r.cli.build_round264_r8_loop12_report
```

결과:

- round_264 target test: 통과
- report generation: 통과

## 유지할 제한

- 이 라운드 케이스는 calibration/evaluation 전용이다.
- production scoring, StageClassifier threshold, candidate generation은 변경하지 않았다.
- full adjusted OHLC가 없는 케이스는 `price_data_unavailable_after_deep_search` 또는 reported anchor로만 남겼다.
- 비KRX 사례인 Coupang은 직접 KR 후보가 아니라 platform trust guardrail 참고사례로만 둔다.
