# Checkpoint 28A Round 238 R8 Loop 10 Platform Content SW Security Price Validation

## 목적

`docs/round/round_238.md`의 R8 Loop 10 내용을 case-library 검증팩으로 반영했다.
이번 라운드는 B2B SaaS, AI cloud/IT services, Webtoon/IP, AI partnership, game IP, telecom cybersecurity, K-pop governance risk를 같은 대섹터 안에서 비교한다.

쉬운 예로, `카카오/OpenAI 제휴 + 주가 급등`은 관심 신호나 4B-watch가 될 수 있지만, 유료 사용량, ARPU, OPM/FCF가 확인되기 전에는 Stage 3-Green 근거가 아니다.

## 반영 파일

- `src/e2r/sector/round238_r8_loop10_platform_content_sw_security_price_validation.py`
- `src/e2r/cli/build_round238_r8_loop10_report.py`
- `tests/test_round238_r8_loop10_platform_content_sw_security_price_validation.py`
- `data/e2r_case_library/cases_r8_loop10_round238.jsonl`
- `data/sector_taxonomy/round238_r8_loop10_platform_content_sw_security_price_validation_audit.json`
- `output/e2r_round238_r8_loop10_platform_content_sw_security_price_validation/`

## 핵심 결과

- source_round: `docs/round/round_238.md`
- analyst_round_id: `round_166`
- large_sector: `PLATFORM_CONTENT_SW_SECURITY`
- cases: 8
- success_candidate: 3
- event_premium: 1
- failed_rerating: 2
- overheat: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 8
- strong 4C-watch cases: 2
- hard_4c_case_count: 0
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true

## 케이스 해석

- 더존비즈온: EQT $930M / 37.6% 거래는 B2B SaaS Stage 2 후보지만 ARR, churn, OPM, FCF 확인 전 Green 보류.
- 삼성SDS: KKR CB $820M과 AI capital allocation으로 장중 +20.8%, KOSPI 대비 +17.8pp. AI 매출 전환 전에는 Stage 2 + 4B-watch.
- LG CNS: cloud/AI 비중이 절반 이상이었지만 IPO 가격 61,900원 대비 59,700원으로 첫날 -3.55%. `evidence_good_but_price_failed`.
- NAVER/Webtoon: IPO와 Disney 이벤트는 IP monetization watch지만 MAU만으로는 부족하다. paid usage, ARPU, IP licensing, FCF 필요.
- 카카오/OpenAI: 제휴 전 +9%, 발표일 -2%, two-session +6.8%. `price_moved_without_evidence`.
- 시프트업: 2023 OPM 65.7%, Stellar Blade 300만장 이상은 Stage 2 후보지만 반복 bookings와 pipeline conversion 필요.
- SK텔레콤: 데이터 유출, 매출전망 800B 하향, 보안투자 700B, 과징금 134.8B는 strong 4C-watch.
- HYBE: 창업자 법적 리스크는 governance 4C-watch. 영장 기각으로 hard 4C 확정은 보류.

## Guardrail

- AI partnership headline, IPO/debut premium, M&A announcement, 신작 첫 주 판매량만으로 Green 금지.
- 반복매출, ARR proxy, paid usage, bookings, OPM/FCF, 보안·거버넌스 신뢰가 확인돼야 Stage 3 검토 가능.
- SKT/HYBE처럼 4C-watch인 사건은 hard 4C로 자동 승격하지 않는다. 실제 사업 훼손이 확인돼야 한다.
- 이 팩은 calibration/evaluation 전용이며 production scoring과 candidate generation에는 사용하지 않는다.

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round238_r8_loop10_platform_content_sw_security_price_validation -v`
- `PYTHONPATH=src python -m e2r.cli.build_round238_r8_loop10_report`
