# Checkpoint 28A Round 303 R8 Loop 15 Platform/Content/SW/Security Trigger Validation

## 반영 내용

- `docs/round/round_303.md`의 R8 Loop 15 내용을 calibration-only 패키지로 반영했다.
- 생산 scoring/staging/candidate generation은 변경하지 않았다.
- Kakao/OpenAI, Naver/Webtoon/Nvidia, LG CNS, Samsung SDS/KKR, Krafton/ADK/India, Shift Up, HYBE/NewJeans/SM-Tencent, SK Telecom data breach를 trigger 단위로 분리했다.
- full adjusted OHLC window는 아직 없으므로 reported event anchor만 기록하고, MFE/MAE를 발명하지 않았다.

## 핵심 결론

- Kakao/OpenAI는 Stage2-Actionable이지만 Green은 아니다. KakaoTalk 97% 기반과 OpenAI 제휴는 신호지만, paid usage, retention, ad uplift, API/cloud margin이 필요하다.
- Naver/Webtoon/Nvidia AI infra는 Stage2-Actionable이다. Webtoon IPO +14.3%, 170M MAU, Blackwell chip purchase는 강하지만 parent-level monetization이 필요하다.
- LG CNS는 evidence_good_but_price_failed다. Cloud/AI sales mix 54%에도 IPO debut가 issue price 아래였다.
- Samsung SDS/KKR CB는 Stage2-Actionable + 4B-watch다. +20.8% trigger는 강하지만 CB dilution, AI order backlog, margin gate가 남아 있다.
- Krafton/ADK/India fund와 Shift Up은 game/content IP Stage2-Actionable이다. Integration, retention, recurring IP revenue가 Green gate다.
- HYBE/NewJeans는 artist governance 4C-watch다. Artist IP는 계약/활동권이 깨지면 매출보다 먼저 thesis gate가 깨질 수 있다.
- SK Telecom data breach는 hard 4C reference다. 보안투자는 성장 capex가 아니라 trust-repair cost로 기록한다.

## 생성 파일

- `src/e2r/sector/round303_r8_loop15_platform_content_sw_security_trigger_validation.py`
- `src/e2r/cli/build_round303_r8_loop15_report.py`
- `tests/test_round303_r8_loop15_platform_content_sw_security_trigger_validation.py`
- `data/e2r_case_library/cases_r8_loop15_round231.jsonl`
- `data/e2r_trigger_calibration/triggers_r8_loop15_round231.jsonl`
- `data/sector_taxonomy/round303_r8_loop15_platform_content_sw_security_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round231_r8_loop15_v1.csv`
- `output/e2r_round303_r8_loop15_platform_content_sw_security_trigger_validation/`

## What Not To Change

- Round 303 case records must not be used as candidate-generation input.
- Do not apply Round 303 shadow weights to production scoring yet.
- Do not treat AI partnership, IPO pop, CB investment, IP acquisition, or post-breach security capex as Stage 3-Green evidence by itself.
- Do not downgrade Stage2/4C candidates only because full OHLC is missing.

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round303_r8_loop15_platform_content_sw_security_trigger_validation -v`
- `PYTHONPATH=src python -m compileall -q src/e2r/sector/archetypes.py src/e2r/sector/round303_r8_loop15_platform_content_sw_security_trigger_validation.py src/e2r/cli/build_round303_r8_loop15_report.py tests/test_round303_r8_loop15_platform_content_sw_security_trigger_validation.py`

## 다음 작업

- trigger date 기준 30/90/180일 adjusted OHLC를 채워 price validation을 보강한다.
- AI paid usage, enterprise backlog, cloud margin, content/IP recurring revenue, game retention, artist contract stability, breach churn/cost를 별도 evidence field로 연결한다.
- 이후에도 Stage 3-Green은 headline이 아니라 paid usage, recurring revenue, margin, security/governance gate 통과로만 승격한다.
