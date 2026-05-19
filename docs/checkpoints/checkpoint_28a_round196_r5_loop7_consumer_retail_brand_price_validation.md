# Checkpoint 28A Round 196 R5 Loop 7 Consumer Retail Brand Price Validation

## Scope

- source round: `docs/round/round_196.md`
- large sector: `CONSUMER_RETAIL_BRAND`
- production_scoring_changed: `false`
- candidate_generation_input: `false`
- shadow_weight_only: `true`
- needs_ohlc_backfill: `true`

이번 라운드는 K푸드, K뷰티, ODM, 뷰티 디바이스, 유통 플랫폼, 의류/M&A 이벤트를 같은 R5 안에서 분리한다. 핵심은 `K푸드/K뷰티가 핫하다`가 아니라 `반복구매와 채널 sell-through가 OPM/EPS/FCF로 내려왔는가`다.

쉬운 예: `as_of_date=2025-06-05`에 d'Alba가 Costco/Ulta/Target 입점을 논의했다면 Stage 2 관심 근거는 될 수 있다. 하지만 실제 매장 회전율, 반복 발주, OPM, 재고/매출채권 안정이 없으면 Stage 3-Green 근거가 아니다.

## Files Added

- `src/e2r/sector/round196_r5_loop7_consumer_retail_brand_price_validation.py`
- `src/e2r/cli/build_round196_r5_loop7_report.py`
- `tests/test_round196_r5_loop7_consumer_retail_brand_price_validation.py`
- `data/e2r_case_library/cases_r5_loop7_round196.jsonl`
- `data/sector_taxonomy/round196_r5_loop7_consumer_retail_brand_price_validation_audit.json`
- `output/e2r_round196_r5_loop7_consumer_retail_brand_price_validation/`

## Case Pack

| case | classification | stage decision |
| --- | --- | --- |
| 농심 | `success_candidate` | Stage 2 watch; OPM/EPS/channel sell-through 전 Stage 3 보류 |
| APR | `structural_success` | 구조 근거는 강하지만 2025년 4배 상승 anchor 때문에 4B-watch |
| d'Alba Global | `overheat` | retail talks + IPO 2x는 Stage 3가 아니라 4B-watch |
| 코스맥스/한국콜마 | `success_candidate` | ODM leverage는 Stage 2 후보; 주문/OPM/재고/채권 확인 전 Green 금지 |
| 아모레퍼시픽 | `failed_rerating` | K-beauty macro와 China/COSRX 회사 리스크를 분리 |
| CJ/올리브영 | `success_candidate` | 좋은 private platform이지만 listed-parent/holdco cap 필요 |
| F&F | `event_premium` | TaylorMade M&A/ROFR 이벤트는 본업 브랜드 rerating 증거가 아님 |

## Green Gate

R5 Green 후보에는 다음 증거가 필요하다.

- `repeat_purchase_evidence`
- `overseas_sales_mix_growth`
- `channel_sell_through_confirmed`
- `opm_improvement`
- `inventory_and_receivables_stable`
- `asp_or_product_mix_improvement`
- `single_product_dependence_not_excessive`
- `tariff_regulation_recall_passed`
- `price_path_after_evidence`

반대로 다음은 Green 금지 패턴으로 기록했다.

- `tiktok_viral_only`
- `retail_talks_only`
- `ipo_first_month_rally`
- `influencer_endorsement_only`
- `mna_event_only`
- `private_affiliate_value_only`
- `china_decline_without_offset`

## 4B / 4C Notes

- APR: 구조 근거가 강해도 가격이 2~4배 이상 먼저 움직이면 4B-watch가 붙어야 한다.
- d'Alba: 입점 논의와 IPO 직후 2배 상승은 price-path 경고다.
- F&F: M&A 기대와 법적 분쟁은 event premium으로 분리한다.
- hard 4C gates에는 `recall_or_food_safety_issue`, `channel_stuffing`, `inventory_build`, `receivables_spike`, `us_tariff_margin_squeeze`, `mna_event_failure`를 포함했다.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round196_r5_loop7_consumer_retail_brand_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round196_r5_loop7_report
```

## What Not To Change

- Round196 케이스를 후보 생성 입력으로 쓰지 않는다.
- Stage 3-Green 기준을 낮추지 않는다.
- sell-through, OPM, 재고, 매출채권, stage price, MFE/MAE를 발명하지 않는다.
- IPO, retail talks, M&A 이벤트만으로 Green을 만들지 않는다.

## Next

OHLC backfill로 Stage 2/4B 기준 가격, MFE/MAE, peak/drawdown을 채워야 한다. 그 다음 R5 shadow scoring에서 `repeat_demand`, `channel_sell_through`, `inventory_quality`, `receivables_quality`가 실제 가격경로와 맞는지 검증한다.
