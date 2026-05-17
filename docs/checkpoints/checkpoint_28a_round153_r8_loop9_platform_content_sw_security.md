# Checkpoint 28A Round 153 R8 Loop 9 Platform / Content / Software / Security

## 목적

`docs/round/round_153.md`의 R8 Loop 9 내용을 별도 calibration pack으로 반영했다.

R8은 플랫폼, 콘텐츠, 소프트웨어, 보안에서 “AI 기능”, “유저 수”, “신작 기대”, “광고 회복”, “보안 수요”와 실제 반복 매출·FCF를 분리하는 라운드다. 이번 Loop 9의 핵심은 ARR, billings, bookings, ad revenue, contract value, guidance, churn, retention, workflow lock-in, OPM/FCF, operational trust, privacy/youth safety, ad quality를 더 강하게 보는 것이다.

쉬운 예시는 다음과 같다.

- `AI 기능 출시`는 Stage 1 신호다. 유료 계약, ARR, 반복 사용, FCF 전환이 붙어야 더 높은 단계로 올라갈 수 있다.
- `유저 수 증가`는 좋은 출발점이지만 bookings cut이나 age verification friction이 있으면 Roblox식 4C 감시가 먼저다.
- `광고 매출 증가`도 scam ads, privacy lawsuit, ad ARPU 부재가 있으면 Green 근거가 아니다.
- `보안 수요 증가`는 Fortinet처럼 billings/ARR/renewal/OPM으로 확인될 때 의미가 있다. CrowdStrike식 전 세계 장애가 나면 운영 신뢰가 Stage를 막는다.
- `레거시 SaaS AI`는 workflow lock-in을 강화할 수도 있지만, seat/license를 잠식하면 RedTeam overlay가 된다.

## 반영 파일

- `src/e2r/sector/round153_r8_loop9_platform_content_sw_security.py`
- `src/e2r/cli/build_round153_r8_loop9_report.py`
- `tests/test_round153_r8_loop9_platform_content_sw_security.py`
- `data/e2r_case_library/cases_r8_loop9_round153.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round153_r8_loop9_v9.csv`
- `output/e2r_round153_r8_loop9_platform_content_sw_security/`

## v9 기본 점수축

| component | weight | 해석 |
| --- | ---: | --- |
| arr_billings_bookings_ad_revenue_contract_value | 24 | AI 기능, 유저 수, 광고 tier가 아니라 ARR, billings, bookings, 광고 매출, 계약가치, guidance를 확인 |
| recurrence_retention_workflow_lock_in | 20 | 반복 사용, 낮은 churn, workflow lock-in, renewal을 확인 |
| ai_cloud_security_platform_bottleneck | 14 | AI/cloud/security 수요가 실제 billable bottleneck 또는 platform lock-in인지 확인 |
| opm_fcf_gross_margin_conversion | 12 | AI 매출이 compute cost, capex, restructuring에 먹히지 않고 OPM/FCF로 전환되는지 확인 |
| market_mispricing_rerating_gap | 8 | old SaaS/CDN/ad/game frame이 아직 남아 있는지 확인하되, narrative보다 증거 품질을 우선 |
| valuation_room_4b_margin | 8 | 좋은 실적에도 가격이 먼저 간 경우 4B-watch로 분리 |
| operational_trust_legal_privacy_disclosure | 14 | 보안 장애, 개인정보, 청소년 안전, scam ads, disclosure confidence를 hard gate로 반영 |

## 케이스 방향

- Stage 2/3 후보: `Palantir AI workflow`, `Datadog observability AI`, `Akamai AI cloud deal`, `Fortinet security billings`, `Cisco AI infrastructure orders`, `Netflix ad tier`
- 4B 감시: `Palantir strong results but valuation saturation`, `Akamai AI cloud rerating`, `Cisco restructuring watch`, `Netflix privacy watch`
- 4C / RedTeam: `Dynatrace ARR/guidance miss`, `CrowdStrike operational outage`, `Roblox safety friction and bookings cut`, `The Trade Desk revenue miss`, `Meta scam ads`, `Meta youth safety`, `legacy SaaS AI disruption`

## Guardrail

- production scoring은 변경하지 않았다.
- case record는 candidate-generation input이 아니다.
- AI demo, user count, ad tier launch, game trailer, security-demand narrative, NFT/metaverse theme만으로 Green을 만들지 않는다.
- Stage 3는 ARR/billings/bookings/ad revenue/contract value, retention/churn, workflow lock-in, OPM/FCF, legal/privacy/ad-quality stability, 실제 가격경로 동행을 요구한다.
- operational trust break, privacy/youth safety lawsuit, scam ads, ARR/guidance miss, bookings cut, revenue miss, legacy SaaS seat cannibalization은 RedTeam overlay로 유지한다.

## 검증

실행한 명령:

```bash
PYTHONPATH=src python -m unittest tests/test_round153_r8_loop9_platform_content_sw_security.py -v
PYTHONPATH=src python -m e2r.cli.build_round153_r8_loop9_report
```

결과:

- Round 153 전용 테스트 14개 통과
- v9 score profile 생성
- case JSONL 생성
- summary, case matrix, stage date plan, base score axes, guardrail, risk overlay, price validation 리포트 생성
