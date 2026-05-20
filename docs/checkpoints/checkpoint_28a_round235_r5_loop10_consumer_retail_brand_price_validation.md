# Checkpoint 28A Round 235: R5 Loop 10 Consumer Retail Brand Price Validation

## 반영 내용

`docs/round/round_235.md`의 R5 Loop 10 소비재·유통·브랜드 검증 라운드를 구조화했다.

추가된 항목:

- `src/e2r/sector/round235_r5_loop10_consumer_retail_brand_price_validation.py`
- `src/e2r/cli/build_round235_r5_loop10_report.py`
- `tests/test_round235_r5_loop10_consumer_retail_brand_price_validation.py`
- `data/e2r_case_library/cases_r5_loop10_round235.jsonl`
- `data/sector_taxonomy/round235_r5_loop10_consumer_retail_brand_price_validation_audit.json`
- `output/e2r_round235_r5_loop10_consumer_retail_brand_price_validation/`

이번 패치는 case library와 shadow-weight 설계 자료만 추가한다. Production scoring, StageClassifier threshold, candidate generation은 변경하지 않았다.

## 핵심 해석

R5의 Stage 3는 “브랜드가 핫하다”가 아니다.

쉬운 예:

```text
미국 입점 논의
-> Stage 2 관심 신호
-> 실제 매장 sell-through, 반복 주문, OPM, 재고/채권 품질 확인 전에는 Green 금지
```

반대로 삼양식품처럼 수출, ASP, OP revision이 같이 보이면 Stage 3 후보가 될 수 있다. 단, Denmark recall 같은 현지 규제 이슈는 별도 4C-watch로 남긴다.

## 반영된 케이스

| case | 판단 |
|---|---|
| 삼양식품 | Buldak 수출, ASP, OP revision으로 Stage 3 후보. Denmark recall/reversal은 local-regulatory 4C-watch |
| 농심 | Shin Ramyun global staple 후보. OPM/EPS, channel sell-through 전 Green 보류 |
| APR / Medicube | 강한 structural success 후보. 주가 4배 이상 상승과 single-device 집중 때문에 4B-watch |
| d’Alba / Silicon2 / Cosmax / Kolmar | K-beauty U.S. channel Stage 2 후보지만 retail talks와 post-debut rally만으로 Green 금지 |
| CJ / Olive Young | K-beauty retail platform 후보. 상장 vehicle 이익 연결과 store economics 전 Green 금지 |
| 아모레퍼시픽 | K-beauty macro와 legacy China exposure를 분리. China/duty-free weakness는 thesis-break watch |
| 호텔신라 / 현대백화점 / 파라다이스 / 한국화장품 | 중국 무비자 정책 event premium. tourist spend, duty-free sales, OPM 전 Green 금지 |
| F&F / TaylorMade | M&A optionality event. signed transaction, financing, EPS accretion 전 Green 금지 |

## 보강된 R5 Gate

Green 필수 확인:

- 반복구매 / 반복수요
- 해외 매출 비중 증가
- channel sell-through
- ASP 또는 product mix 개선
- OPM 개선
- 재고·매출채권 안정
- tariff / recall / regulation 통과
- single-SKU / single-device risk 관리
- evidence 이후 가격경로 확인

Green 금지 패턴:

- viral TikTok만 있음
- 입점 논의만 있음
- IPO/debut rally만 있음
- influencer endorsement만 있음
- M&A optionality만 있음
- China decline offset 없음
- single product story만 있음

## 4B / 4C 감시

4B-watch:

- Stage 3 이후 2~4배 이상 상승
- IPO/debut 후 단기간 2배 이상 상승
- single SKU / single device 의존도 높음
- 미국 입점 기대가 sell-through보다 먼저 가격화
- 관광정책 발표일 retail/beauty basket 동반 급등
- M&A optionality가 signed transaction보다 먼저 가격화

Hard 4C:

- food safety recall 확산
- regulatory ban
- channel stuffing
- inventory build
- receivables spike
- single product fad collapse
- U.S. tariff margin squeeze
- retail channel sell-through failure
- China sales collapse not offset by U.S./Europe
- M&A event failure / impairment

이번 라운드에서 hard 4C는 확정하지 않았다.

## 산출물

CLI:

```bash
PYTHONPATH=src python -m e2r.cli.build_round235_r5_loop10_report
```

생성 파일:

- `round235_r5_loop10_price_validation_summary.md`
- `round235_r5_loop10_case_matrix.csv`
- `round235_r5_loop10_target_aliases.csv`
- `round235_r5_loop10_deep_sub_archetypes.csv`
- `round235_r5_loop10_score_adjustments.csv`
- `round235_r5_loop10_shadow_weights.csv`
- `round235_r5_loop10_price_validation_fields.csv`
- `round235_r5_loop10_green_gate_review.md`
- `round235_r5_loop10_price_validation_plan.md`
- `round235_r5_loop10_stage4b_4c_review.md`
- `round235_r5_loop10_deep_sub_archetypes.md`

## Guardrails

- Production scoring 변경 없음.
- Stage 3-Green threshold 완화 없음.
- Case library를 candidate-generation input으로 사용하지 않음.
- OHLC, peak, MFE, MAE, stage price를 임의 생성하지 않음.
- 투자 권고 문구 없음.
