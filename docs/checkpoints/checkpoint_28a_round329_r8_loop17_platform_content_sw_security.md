# Checkpoint 28A Round 329 R8 Loop 17: Platform / Content / Software / Security Trigger Validation

`docs/round/round_329.md`의 R8 Loop 17 분석을 calibration-only case library와 trigger validation pack으로 반영했다. 이번 라운드는 AI 채팅 플랫폼, sovereign AI cloud infra, Webtoon/content platform, game IP, AI/cloud IT services IPO, cyber breach, K-pop label governance, platform founder/regulatory risk를 분리했다.

## 반영 범위

- production scoring 변경 없음
- candidate generation 입력으로 사용하지 않음
- shadow weight only
- full adjusted OHLC 미완료
- reported event anchor만 보존
- MFE/MAE/peak/drawdown은 만들지 않음

## 추가된 canonical archetype

- `AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED`
- `SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B`
- `WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT`
- `GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B`
- `IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED`
- `CYBER_BREACH_HARD_4C_SECURITY_CAPEX`
- `KPOP_LABEL_GOVERNANCE_4B`
- `PLATFORM_GOVERNANCE_REGULATORY_4B`

## 핵심 해석

- Kakao/OpenAI는 Stage2 price-failed다. 예를 들어 “AI 파트너십 발표 후 +9%”는 관심 신호지만, 이후 -2%로 꺾이고 유료 사용/ARPU가 없으면 Green 근거가 아니다.
- Naver sovereign AI는 Stage2다. GPU/Blackwell/CapEx는 중요하지만, 기업·정부 계약과 utilization이 확인되어야 한다.
- Webtoon은 Stage2-Actionable 후보지만 Naver parent holdco discount가 4B gate다.
- Shift Up은 게임 IP Stage2, Krafton/Subnautica는 studio control/legal 4B overlay다.
- LG CNS는 AI/cloud 매출 mix가 있어도 issue price 아래 거래되어 price-failed다.
- SK Telecom data breach는 hard 4C다. 보안 capex와 보상 부담은 성장 capex가 아니라 thesis-break cost로 본다.
- HYBE와 Kakao founder/legal risk는 Green 차단용 governance 4B overlay다.

## 생성 파일

- `src/e2r/sector/round329_r8_loop17_platform_content_sw_security_trigger_validation.py`
- `src/e2r/cli/build_round329_r8_loop17_report.py`
- `tests/test_round329_r8_loop17_platform_content_sw_security_trigger_validation.py`
- `data/e2r_case_library/cases_r8_loop17_round257.jsonl`
- `data/e2r_trigger_calibration/triggers_r8_loop17_round257.jsonl`
- `data/sector_taxonomy/round329_r8_loop17_platform_content_sw_security_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round257_r8_loop17_v1.csv`
- `output/e2r_round329_r8_loop17_platform_content_sw_security_trigger_validation/`

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round329_r8_loop17_platform_content_sw_security_trigger_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round329_r8_loop17_report`

## 다음 작업

다음 라운드에서는 R9 Loop 17로 넘어가되, 여전히 case library와 trigger calibration을 scoring input으로 쓰면 안 된다. 먼저 adjusted OHLC backfill과 price-alignment 검증을 채운 뒤, shadow score에서만 archetype별 weight를 비교해야 한다.
