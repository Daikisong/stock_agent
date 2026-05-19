# Checkpoint 28A Round 199 R8 Loop 7 Platform Content SW Security Price Validation

## Scope

- source round: `docs/round/round_199.md`
- large sector: `PLATFORM_CONTENT_SW_SECURITY`
- production_scoring_changed: `false`
- candidate_generation_input: `false`
- shadow_weight_only: `true`
- needs_ohlc_backfill: `true`

이번 라운드는 R8 플랫폼·콘텐츠·SW·보안에서 `AI 기능/파트너십/모델 공개/MAU/신작 첫 주 판매/IPO/M&A 발표`와 `ARR/bookings/paid usage/ARPU/retention/OPM/FCF/운영신뢰`를 분리한다. 핵심은 AI·콘텐츠라는 이름이 아니라, 반복해서 돈을 내는 고객과 이익률이 실제로 보이는지다.

쉬운 예: `as_of_date=2025-02-04`에 카카오가 OpenAI 제휴를 발표해도 AI 유료화, ARPU, OPM이 없으면 Stage 3-Green이 아니라 Stage 1~2 watch다.

## Files Added

- `src/e2r/sector/round199_r8_loop7_platform_content_sw_security_price_validation.py`
- `src/e2r/cli/build_round199_r8_loop7_report.py`
- `tests/test_round199_r8_loop7_platform_content_sw_security_price_validation.py`
- `data/e2r_case_library/cases_r8_loop7_round199.jsonl`
- `data/sector_taxonomy/round199_r8_loop7_platform_content_sw_security_price_validation_audit.json`
- `output/e2r_round199_r8_loop7_platform_content_sw_security_price_validation/`

## Case Pack

| case | classification | stage decision |
| --- | --- | --- |
| 더존비즈온 | `success_candidate` | EQT deal과 cloud ERP는 Stage 2; ARR, churn, OPM, FCF 전 Green 금지 |
| 삼성SDS | `success_candidate` | KKR CB와 AI infra는 Stage 2; 발표일 급등은 4B-watch |
| NAVER | `success_candidate` | Webtoon IPO와 HyperCLOVA X는 Stage 2; paid content, ARPU, AI/cloud margin 전 Green 금지 |
| 카카오 | `failed_rerating` | OpenAI partnership은 Stage 1~2 attention; AI monetization 전 price_moved_without_evidence |
| 크래프톤 | `success_candidate` | inZOI와 ADK는 Stage 2; repeat bookings, retention, IP monetization 전 Green 금지 |
| 시프트업 | `overheat` | Stellar Blade 판매는 강하지만 single-IP/IPO overheat를 분리 |
| HYBE | `failed_rerating` | K-pop IP가 강해도 governance/legal risk가 Green을 막음 |

## Green Gate

R8 Green 후보에는 다음 증거가 필요하다.

- `recurring_revenue_or_bookings_confirmed`
- `arr_arpu_paid_usage_or_billings_confirmed`
- `opm_or_gross_margin_improving`
- `fcf_conversion_visible`
- `retention_or_churn_stable`
- `ip_monetization_beyond_single_launch`
- `ai_feature_converts_to_paid_revenue_or_cost_savings`
- `privacy_security_governance_trust_passed`
- `price_path_after_repeat_economics`

반대로 다음은 Green 금지 패턴으로 기록했다.

- `ai_feature_only`
- `partnership_headline_only`
- `model_release_or_paper_only`
- `mau_without_arpu`
- `game_launch_first_week_only`
- `ipo_first_month_rally`
- `mna_announcement_only`
- `single_ip_dependence_without_repeat_monetization`
- `ai_capex_without_revenue`
- `founder_legal_risk`
- `privacy_or_security_trust_break`

## 4B / 4C Notes

- AI partnership, Webtoon/IP valuation, 신작 출시, IPO, M&A가 반복경제보다 먼저 가격에 반영되면 4B-watch로 본다.
- ARR 둔화, retention 약화, AI capex에 따른 margin 훼손, M&A integration cost 확대는 4B-elevated 후보가 된다.
- privacy/security/founder legal risk는 플랫폼과 IP가 강해도 Green을 막을 수 있다.
- hard 4C는 신뢰 가능한 원문으로 privacy breach, security outage, legal break, monetization failure, churn spike, launch failure 등이 확인될 때만 확정한다.

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round199_r8_loop7_platform_content_sw_security_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round199_r8_loop7_report
```

## What Not To Change

- Round199 케이스를 후보 생성 입력으로 쓰지 않는다.
- Stage 3-Green 기준을 낮추지 않는다.
- ARR, bookings, paid usage, ARPU, retention, churn, OPM, FCF, stage price, MFE/MAE를 발명하지 않는다.
- AI 기능, OpenAI 제휴, 모델 공개, MAU, 신작 첫 주 판매, IPO, M&A 발표만으로 Green을 만들지 않는다.
- legal/governance risk를 IP나 플랫폼 성장 서사로 덮지 않는다.

## Next

OHLC backfill로 Stage 2/4B/4C 기준 가격과 MFE/MAE를 채워야 한다. 그 다음 R8 shadow scoring에서 `recurring_revenue`, `ARR_proxy`, `bookings_repeatability`, `paid_usage_conversion`, `OPM_improvement`, `FCF_conversion`, `operational_trust`가 실제 가격경로와 맞는지 검증한다.
