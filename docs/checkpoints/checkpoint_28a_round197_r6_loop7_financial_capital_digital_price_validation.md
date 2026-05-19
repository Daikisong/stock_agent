# Checkpoint 28A Round 197 R6 Loop 7 Financial Capital Digital Price Validation

## Scope

- source round: `docs/round/round_197.md`
- large sector: `FINANCIAL_CAPITAL_DIGITAL`
- production_scoring_changed: `false`
- candidate_generation_input: `false`
- shadow_weight_only: `true`
- needs_ohlc_backfill: `true`

이번 라운드는 R6 금융·자본배분·디지털금융에서 `저PBR/밸류업/스테이블코인 테마`와 `ROE/CET1/실제 소각/credit cost/규제수익`을 분리한다. 핵심은 싸다는 사실이 아니라, 자본비율을 훼손하지 않고 주주환원과 수익성이 반복될 수 있는지다.

쉬운 예: `as_of_date=2025-06-18`에 원화 스테이블코인 정책 기대가 커져 관련주가 올라도, 실제 발행권, 수수료, reserve income이 없으면 Stage 3-Green 근거가 아니다.

## Files Added

- `src/e2r/sector/round197_r6_loop7_financial_capital_digital_price_validation.py`
- `src/e2r/cli/build_round197_r6_loop7_report.py`
- `tests/test_round197_r6_loop7_financial_capital_digital_price_validation.py`
- `data/e2r_case_library/cases_r6_loop7_round197.jsonl`
- `data/sector_taxonomy/round197_r6_loop7_financial_capital_digital_price_validation_audit.json`
- `output/e2r_round197_r6_loop7_financial_capital_digital_price_validation/`

## Case Pack

| case | classification | stage decision |
| --- | --- | --- |
| SK스퀘어 | `structural_success` | 자사주 소각과 NAV discount는 강하지만 SK하이닉스 랠리 뒤 4B-watch 필요 |
| 하나금융/하나은행 | `success_candidate` | 두나무 지분은 Stage 2 후보; 지분법/규제수익/자본비율 전 Green 금지 |
| 삼성생명 | `success_candidate` | NAV discount는 좋지만 규제성 지분매각과 capital release 확인 필요 |
| 카카오뱅크 | `failed_rerating` | 인터넷은행 성장성보다 대주주 적격성/지배력 규제 리스크가 우선 |
| 카카오페이/아톤 등 스테이블코인 테마 | `overheat` | 정책 테마 급등은 Stage 1/4B-watch; 수익모델 전 Green 금지 |
| 카카오페이 privacy | `4c_thesis_break` | payment volume보다 privacy/data trust break가 hard RedTeam |
| 우리금융 | `success_candidate` | 비은행 확장과 CET1/credit cost/주주환원을 함께 확인해야 함 |

## Green Gate

R6 Green 후보에는 다음 증거가 필요하다.

- `roe_structurally_improving_or_sustained`
- `cet1_or_kics_capital_buffer`
- `actual_buyback_cancellation`
- `dividend_or_cancel_policy_durable`
- `credit_cost_pf_risk_passed`
- `pbr_rerating_runway`
- `company_level_capital_allocation_evidence`
- `digital_asset_revenue_model_or_equity_method_income`
- `regulatory_privacy_governance_trust_passed`

반대로 다음은 Green 금지 패턴으로 기록했다.

- `low_pbr_only`
- `policy_valueup_only`
- `treasury_buyback_without_cancellation`
- `stablecoin_policy_theme_only`
- `digital_asset_equity_option_without_revenue`
- `fintech_user_growth_without_profit`
- `non_bank_acquisition_with_capital_ratio_weakening`
- `major_shareholder_legal_risk`
- `privacy_or_data_trust_break`

## 4B / 4C Notes

- SK스퀘어: 실제 소각과 NAV discount는 좋지만, SK하이닉스 가격 의존이 커지면 4B-watch가 필요하다.
- 하나금융: 두나무 지분은 Stage 2 후보지만, 규제수익과 자본비율 영향 확인 전 Stage 3는 보류한다.
- 삼성생명: 삼성전자 NAV 할인 해소 기대와 규제성 지분매각을 함께 본다.
- 카카오뱅크/카카오페이: 대주주 법적 리스크, 개인정보, 데이터 신뢰 훼손은 Green 차단 또는 4C 후보로 둔다.
- 스테이블코인 테마: 실제 라이선스, 수수료, reserve income 전에는 price_moved_without_evidence로 분리한다.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round197_r6_loop7_financial_capital_digital_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round197_r6_loop7_report
```

## What Not To Change

- Round197 케이스를 후보 생성 입력으로 쓰지 않는다.
- Stage 3-Green 기준을 낮추지 않는다.
- ROE, CET1, K-ICS, credit cost, 소각 실행, 규제수익, stage price, MFE/MAE를 발명하지 않는다.
- 저PBR, 밸류업 정책 기대, 스테이블코인 테마만으로 Green을 만들지 않는다.

## Next

OHLC backfill로 Stage 2/4B/4C 기준 가격과 MFE/MAE를 채워야 한다. 그 다음 R6 shadow scoring에서 `roe_sustainability`, `cet1_buffer`, `real_buyback_cancellation`, `credit_cost_control`, `regulated_revenue_visibility`가 실제 가격경로와 맞는지 검증한다.
